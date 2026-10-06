"""Concern 3: what to ask next (METHODOLOGY §5). Reads the tree; writes questions, never evidence. Seeds live here
only, as contexts to query.

Joseph's rule, as written:
  "various minds start to find a sequence -- call it a sequence of three glyphs. The priority is then to extend that
   sequence to the right and to the left as far as they will go while still spending time looking for other 'kernels'
   ... square away the most obvious and stable (empirically) sequences"
  "15% of our effort was always 'hot' -- exploring the space for more kernels ... based on bumps from the original seed"

ONE ORDER for 85% of a round: by TIER first, then sequences most stable first within each tier (tree rank: mean
agreement, scaled down for walks shorter than 4 steps), taken greedily until the budget is spent. So every sequence's
ends are asked before any sequence's deeper squaring-away. (Until c001 the order was sequence first: each sequence
brought all its tiers, and c001 served only the top 9 of 540. Joseph noticed the arrow row `↓ ↘ → ↗ ↑ ↖ ←` missing
`↙`, at rank 75, with both ends never asked: "extend ... to the right and to the left as far as they will go" comes
before squaring away.) Tiers:
  1 ends    an OPEN end: a continue question from the end, outward (context 3-8 glyphs, fated). A WRAP end: a cycle
            probe -- a continue question showing only the end of the suspected period (ceil(p/2) glyphs, >= 2), so a
            repeat would be the mind's own; periods with < 4 distinct glyphs are out of scope and not probed.
  2 seeds   each walked step carried only by seed votes: the seeded context put to the real minds. (Seeds already
            count as votes, so confirming them comes after every sequence's ends.)
  3 k*      for each walked step whose shortest sufficient context is not yet known: the SHORTEST unasked suffix of its
            run (down to 2 glyphs), as a continue question.
  4 branch  where a step had a runner-up continuation: an inhibit question (context, runner-up) -- does it continue?
  5 inside  continue questions at contexts ending on interior glyphs, either direction, never asked (2-4 glyphs).
15% HOT: continue questions on 2-glyph contexts never asked: half from seeds (two adjacent glyphs of a seed's written
order, either direction, drawn by bump), half fresh -- a first glyph from the whole symbol space (printable ASCII 4 :
2-byte 3 : 3-byte symbol blocks 2 : 4-byte symbol blocks 1), and a second glyph that is its codepoint neighbour
(the faint prior edge, METHODOLOGY §1) or another fresh glyph, 1:1. Glyphs already settled in a top-ranked sequence
(restful) are redrawn with probability 1/2.
A context already asked in any round is not asked again (more answers at the same context add replication, which the
rank does not yet need).
"""
import collections, math, pathlib, sys, unicodedata as U

HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[1] / "probe"))
sys.path.insert(0, str(HERE.parents[1] / "tree"))
import probe as PR                                          # noqa: E402
import tree as TR                                           # noqa: E402

EXPLORE_SHARE = 0.15
REASONED_PER_ROUND = 20      # reasoned-pass questions a round (chosen without evidence; the reasoner is the costly mind)
REFLECT_PER_ROUND = 20       # reflection questions a round, outside the budget (chosen without evidence)
FALSIFY_PER_ROUND = 60       # falsification tests a round, highest-ranked sequences first (chosen without evidence)
THIN_PER_ROUND = 80          # precision replications a round (chosen without evidence)
JOIN_PER_ROUND = 60          # join probes a round (chosen without evidence)
JOIN_WEAK = 0.75             # the planner's own cut for a "weak" link inside a strong run (chosen without evidence)
# A weak context is replicated at most ONCE (one more round of answers there), whatever the result: re-asking a weak
# link "until it passes" is optional stopping, which would let noise carry links over any cut.
WRITTEN_RECOGNIZE_PER_ROUND = 40   # recognition questions for written continuations past shown ends (chosen without evidence)
COHERE_PER_ROUND = 80        # whole-run recognition questions a round, each with its shuffled control (chosen without evidence)
PICK_PER_ROUND = 30          # forced-pick contexts a round, each sampled PR.SAMPLES times by each generator mind (chosen without evidence)
# Every pick is a branch; nothing is excluded (Joseph, 2026-10-05: "I wouldn't outright exclude *anything* -- when I
# do stochastic work I always use s-curves with there always being a long tail allowing for the most improbably things
# to sneak in still"). A branch's priority is an S-curve on its share q of its context's draws:
#   w(q) = FLOOR + (1 - FLOOR) / (1 + exp(-(q - MID) / WIDTH))
# so a main branch (q ~ 0.7) weighs ~1, a weaker one at q = 0.13 (A in Joseph's example) ~0.67, a single draw of 20
# (q = 0.05) ~0.24, and nothing falls below FLOOR. All three chosen without evidence; the nulls show what spread
# chance alone produces. (Until 2026-10-05 an answer had to be drawn twice: a cut, against §7, under which a 2%
# answer in 20 draws was followed ~6% of the time -- found by a side agent.)
BRANCH_FLOOR, BRANCH_MID, BRANCH_WIDTH = 0.02, 0.10, 0.04
PICK_NULL_EVERY = 4          # one null (fresh random) context per this many real ones, same length (chosen without evidence)
ORDER_PER_ROUND = 40         # order questions a round (chosen without evidence)
CHART_CONTROL_SHARE = 0.25   # share of runs that also get a chart window -- a descriptive measurement, not a decoy (chosen without evidence)
FRESH_TIERS = {"1-byte": (4, [(0x21, 0x7E)]), "2-byte": (3, [(0xA1, 0x7FF)]),
               "3-byte": (2, [(0x2000, 0x2BFF), (0x2E80, 0x33FF)]), "4-byte": (1, [(0x1D300, 0x1D7FF), (0x1F000, 0x1FBFF)])}

def fresh_glyph(r):
    while True:
        tier = r.choices(list(FRESH_TIERS), weights=[FRESH_TIERS[t][0] for t in FRESH_TIERS])[0]
        spans = FRESH_TIERS[tier][1]
        lo, hi = r.choices(spans, weights=[b - a + 1 for a, b in spans])[0]
        ch = chr(r.randint(lo, hi))
        if PR.is_glyph(ch) and U.category(ch) != "Cn":
            return ch

class Plan:
    def __init__(self, rid, T, budget):
        self.rid, self.T, self.budget = rid, T, budget
        self.asked = set(T.real)                 # seed-voted contexts are still asked of the real minds
        self.qs, self.keys = [], set()
        self.n_join = 0
        self.n_thin = 0
        self.n_falsify = 0
        self.join_links = set()
    def full(self):
        return len(self.qs) >= self.budget
    def add(self, kind, ctx, cand=None, variant=None, probe=None, replicate=False, **src):
        ctx = list(ctx)
        distinct = variant == "reflection" or len(set(ctx)) == len(ctx)       # reflections turn back on themselves
        lo, hi = {"cohere": (3, PR.MAX_RUN), "order": (4, PR.MAX_ORDER), "pick": (2, PR.MAX_RUN)}.get(kind, (2, 8))   # (2, 8) for continue/inhibit/triad: chosen without evidence
        # (until 2026-10-06 pick fell to the continue limit of 8, silently refusing every longer context: the
        # tendrils stopped at 8 glyphs, and roots longer than 8 -- Joseph's block cycle among them -- were never asked)
        if not (lo <= len(ctx) <= hi) or not distinct or not all(PR.is_glyph(x) for x in ctx):
            return False
        if kind == "order":
            if not hasattr(self, "_ordered"):
                self._ordered = {frozenset(sh) for items in self.T.orders.values() for _, sh, _ in items}
            if frozenset(ctx) in self._ordered:
                return False
        if kind == "pick" and tuple(ctx) in (self.T.pick_null if (probe or {}).get("null") else self.T.picks):
            return False
        if kind == "cohere" and (tuple(ctx) in self.T.cohere or tuple(ctx[::-1]) in self.T.cohere
                                 or ((probe or {}).get("control") and tuple(ctx) in self.T.cohere_ctl)):
            return False                         # a run asked once; a control once (a former control may be asked as a run)
        if kind == "triad" and (len(ctx) != 3 or tuple(sorted(ctx)) in self.T.triads_fam):
            return False
        if variant == "reflection" and tuple(ctx) in self.T.reflections:
            return False
        key = (kind, tuple(ctx), cand, variant, tuple(sorted((probe or {}).items())))
        if key in self.keys:
            return False
        if kind == "continue" and variant is None and tuple(ctx) in self.asked and not replicate:
            return False
        if str(src.get("why", "")).startswith("falsify"):
            if self.n_falsify >= FALSIFY_PER_ROUND:
                return False
            self.n_falsify += 1
        if src.get("why") == "thin":
            if self.n_thin >= THIN_PER_ROUND:
                return False
            self.n_thin += 1
        if str(src.get("why", "")).startswith("join"):
            lk = frozenset(src.get("link") or src.get("bridge") or "")      # one probe per link a round
            if self.n_join >= JOIN_PER_ROUND or (lk and lk in self.join_links):
                return False
            self.n_join += 1
            if lk:
                self.join_links.add(lk)
        if variant == "reasoned" and tuple(ctx) in self.T.reasoned:
            return False
        if kind == "inhibit" and ((tuple(ctx), cand) in self.T.inhibit or cand in ctx or not PR.is_glyph(cand)):
            return False
        self.keys.add(key)
        self.qs.append(dict(PR.question(kind, ctx, cand, source=dict(src, round=self.rid), variant=variant, probe=probe),
                            **({"variant": variant} if variant else {}), **({"probe": probe} if probe else {})))
        return True

TIER = {"falsify-skip": 1, "falsify-lengthen": 1, "falsify-triad": 1, "recognize": 1, "recognize-written": 1, "control": 1, "cohere": 1, "order": 1, "join-reverse": 1, "join-replicate": 1, "join-end": 1, "end": 1, "cycle-probe": 1, "seed-step": 2, "kstar": 3, "thin": 3, "branch": 4, "inside": 5}

def written_recognition(P, seqs):
    """Momentum past a felt end (METHODOLOGY §4): where the shown answers end a sequence (top answer "none") but minds
    writing past that point continued with x, ask the first-impression roster whether x comes directly after the shown
    context -- recognition of what was generated. Ordered by how many written answers carry x."""
    T = P.T
    cands = collections.Counter()
    for s in seqs:
        g = s["glyphs"]
        for side, stop in (("right", s["stop_right"]), ("left", s["stop_left"])):
            if stop != "end":
                continue
            run = g if side == "right" else g[::-1]
            ctx = T.lookup(run)
            if not ctx or T.top(ctx) != TR.NONE:
                continue
            for j in range(2, min(TR.MAXK, len(run)) + 1):
                for f, xs in T.written.get(tuple(run[-j:]), {}).items():
                    for x in xs:
                        if x not in ctx and PR.is_glyph(x) and (ctx, x) not in T.inhibit:
                            cands[(ctx, x)] += 1
    return [("inhibit", list(ctx), x, {"why": "recognize-written", "written_answers": n})
            for (ctx, x), n in cands.most_common(WRITTEN_RECOGNIZE_PER_ROUND)]

def cohere_work(P, seqs, written_seqs, seeds, rid):
    """Recognition of whole runs (METHODOLOGY §1, §4a: "best recognized sequences as sequences" is the goal). Candidates
    from every source the planner has -- the tree's walks (most stable first), the runs written answers carry, the
    survey sequences (a fated order), and the branches the picks have grown (main branches first) -- interleaved, so no source crowds out the others. Each run is asked once, as it was
    found (orientation is not chosen by outcome), with its shuffled control: no stopping rule. Runs of 3-MAX_RUN glyphs;
    a seed whose glyphs repeat (other than a cycle's closing repeat) is not a run and is left out.
    -> [(kind, run, None, src)] with each control right after its run"""
    def runs_from(gs, how):
        for g in gs:
            yield list(g), how
    sd = seed_list(seeds, ORDERED_SEEDS, rid, "cohere-seed-order")
    branches = weighted_order(pick_branches(P.T), lambda b: b[1], PR.R("cohere-branch-order", {"round": rid}))  # S-curve draw; each asked once
    # shuffles a mind called coherent: an order the shuffle discovered (Joseph, 2026-10-05: "I can absolutely attest to
    # seeing ideated sequences that are better after some shuffling"). Asked fresh as a run, with its own control; its
    # answers as a control stay in the baseline and never count for it. Most-yes first.
    found = sorted(((sum(c["yes"] for c in fc.values()), list(run)) for run, fc in P.T.cohere_ctl.items()
                    if P.T.cohere_ctl_class.get(run) == "shuffled" and sum(c["yes"] for c in fc.values()) > 0),
                   key=lambda t: (-t[0], t[1]))
    sources = [runs_from([s["glyphs"] for s in seqs], "walk"), runs_from([s["glyphs"] for s in written_seqs], "written"),
               ((g, "seed:" + str(sid)) for g, sid in sd), runs_from([c for c, _ in branches], "pick-branch"),
               runs_from([g for _, g in found], "reordered")]
    out, seen = [], set()
    n_runs = 0
    while sources and n_runs < COHERE_PER_ROUND:
        for src in list(sources):                        # each source adds one run per pass
            while True:
                nxt = next(src, None)
                if nxt is None:
                    sources.remove(src); break
                g, how = nxt
                key = tuple(min(g, g[::-1]))
                if key in seen or not (3 <= len(g) <= PR.MAX_RUN) or tuple(g) in P.T.cohere or tuple(g[::-1]) in P.T.cohere:
                    continue
                ctl = PR.shuffled_control(g, rid)
                if ctl is not None:
                    break
            if nxt is None:
                continue
            seen.add(key)
            out.append(("cohere", g, None, {"why": "cohere", "from": how}))
            out.append(("cohere", ctl, None, {"why": "control", "control": "shuffled", "probe": {"control": "shuffled"}, "of": "".join(g)}))
            if PR.R("cohere-chart-draw", {"round": rid, "run": g}).random() < CHART_CONTROL_SHARE:
                ch = PR.chart_control(g, rid)
                if ch:
                    out.append(("cohere", ch, None, {"why": "control", "control": "chart", "probe": {"control": "chart"}, "of": "".join(g)}))
            n_runs += 1
            if n_runs >= COHERE_PER_ROUND:
                break
    return out

def branch_weight(k, n):
    q = k / n
    return BRANCH_FLOOR + (1 - BRANCH_FLOOR) / (1 + math.exp(-(q - BRANCH_MID) / BRANCH_WIDTH))

ORDERED_SEEDS = {"sequence", "morph", "cyclic", "generator"}   # seed types that propose an order: runs
ORDER_ONLY_SEEDS = {"set", "negative"}                         # no order proposed (a set; a proposed non-sequence): order question only

def is_steward(x):
    return "joseph" in str(x.get("surveyor") or x.get("author") or "").lower()

def seed_list(seeds, types, rid, purpose):
    """seeds of the given types as runs [(glyphs, sid)] in a fated order, the steward's first (Joseph's seeds are his
    questions to the study); a cycle written closed is opened; glyphs that repeat are not a run"""
    out = []
    for x in seeds:
        if (x.get("type") or x.get("kind")) not in types or not isinstance(x.get("glyphs"), list):
            continue
        g = list(x["glyphs"])
        if len(g) > 1 and g[-1] == g[0]:
            g = g[:-1]
        if len(set(g)) == len(g):
            out.append((g, x.get("sid"), is_steward(x)))
    PR.R(purpose, {"round": rid}).shuffle(out)
    out.sort(key=lambda t: not t[2])
    return [(g, sid) for g, sid, _ in out]

def order_work(P, seqs, seeds, rid):
    """The order question (METHODOLOGY §4a): a set, scrambled -- which order, if any, do minds put it in? Sets from the
    survey sequences (a fated order), the shuffles a mind called coherent, the pick branches (S-curve draw) and the
    tree's walks, 4-MAX_ORDER glyphs, interleaved; each set asked once. A longer run is not asked (yet).
    -> [(kind, glyphs, None, src)]"""
    T = P.T
    def ok(g):
        return 4 <= len(g) <= PR.MAX_ORDER and len(set(g)) == len(g) and all(PR.is_glyph(c) for c in g)
    sd = [(g, "seed:" + str(sid)) for g, sid in seed_list(seeds, ORDERED_SEEDS | ORDER_ONLY_SEEDS, rid, "order-seed-order") if ok(g)]
    reord = [(list(run), "reordered") for run, fc in sorted(T.cohere_ctl.items())
             if T.cohere_ctl_class.get(run) == "shuffled" and sum(c["yes"] for c in fc.values()) > 0 and ok(list(run))]
    br = [(c, "pick-branch") for c, _ in weighted_order(pick_branches(T), lambda b: b[1], PR.R("order-branch", {"round": rid})) if ok(c)]
    wk = [(s["glyphs"], "walk") for s in seqs if ok(s["glyphs"])]
    sources = [iter(sd), iter(reord), iter(br), iter(wk)]
    out, seen = [], set()
    while sources and len(out) < ORDER_PER_ROUND:
        for src in list(sources):
            nxt = next(src, None)
            while nxt is not None and frozenset(nxt[0]) in seen:
                nxt = next(src, None)
            if nxt is None:
                sources.remove(src); continue
            seen.add(frozenset(nxt[0]))
            out.append(("order", nxt[0], None, {"why": "order", "from": nxt[1]}))
            if len(out) >= ORDER_PER_ROUND:
                break
    return out

def pick_branches(T):
    """every branch the picks have grown so far: for each picked context c, every answer x -> [(c + [x], weight)]"""
    out = []
    for ctx in T.picks:
        b = T.pick_branches(ctx)
        n = sum(b.values())
        for x, k in b.items():
            if x not in (TR.NONE, TR.OTHER) and x not in ctx and PR.is_glyph(x):
                out.append((list(ctx) + [x], branch_weight(k, n)))
    return out

def weighted_order(items, weight, r):
    """a fated draw of every item without replacement, each next one with probability proportional to its weight
    (Efraimidis-Spirakis keys u^(1/w)): heavy items early, light ones still anywhere -> list"""
    keyed = [(r.random() ** (1 / weight(it)), i) for i, it in enumerate(items)]
    return [items[i] for _, i in sorted(keyed, reverse=True)]

def pick_work(P, seqs, seeds, rid):
    """The generator: tendrils from known sequences (METHODOLOGY §4a; Joseph, 2026-10-05: "s = known sequence -- e.g.,
    'abc' ... {"d" => 72, "A" => 7, "1" => 13, "α" => 2} now you have one 'main' branch and 3 weaker branches. Leading
    to a strong 'abcdefg...' and weaker, more obscure, but equally easily recognized: 'abc123', 'abcABC', 'abcαβ...'
    sequences. Branching from seeds like tendrils ... If, on the other hand, the responses are far more random and
    spread out -- still follow any bumps, but the point is still on the recognition side.")
      CHILDREN  every branch grown so far (pick_branches): the picked context extended by any answer, asked again. Drawn
                by a fated weighted draw on the S-curve weight (BRANCH_*): the main branch most often, weaker ones
                still, a single draw sometimes -- a long tail, never a cut (§7).
      ROOTS     known sequences not yet picked: the survey sequences and the tree's walks, each in both directions
                (a sequence and its reverse are one sequence; extending leftward is extending the reverse), whole when
                <= MAX_RUN glyphs, else their last MAX_RUN.
      Half the round's contexts go to children and half to roots, either half lending to the other when short
      (chosen without evidence). Each context is asked once, SAMPLES times by each generator mind; nulls -- fresh
      random glyphs of the same length, asked the same way -- one per PICK_NULL_EVERY contexts.
    Every branch path also goes to whole-run recognition (cohere_work): recognition decides, generation explores.
    -> [(kind, ctx, None, src, probe)]"""
    T = P.T
    r = PR.R("pick-draw", {"round": rid})
    kids = weighted_order([(c, w) for c, w in pick_branches(T) if len(c) <= PR.MAX_RUN and tuple(c) not in T.picks],
                          lambda kw: kw[1], r)
    chosen = [(c, "branch") for c, _ in kids[:PICK_PER_ROUND // 2]]
    kids = kids[PICK_PER_ROUND // 2:]
    steward = [g for g, _ in seed_list([x for x in seeds if is_steward(x)], ORDERED_SEEDS, rid, "pick-steward")]
    roots = []
    for g in [g for g, _ in seed_list(seeds, ORDERED_SEEDS, rid, "pick-seed-order")] + [s["glyphs"] for s in seqs]:
        if len(g) < 2 or len(set(g)) != len(g):
            continue
        for h in (g, g[::-1]):
            roots.append(h[-PR.MAX_RUN:])
    r.shuffle(roots)
    roots = [h for g in steward for h in (g[-PR.MAX_RUN:], g[::-1][-PR.MAX_RUN:])] + roots     # the steward's first
    seen = {tuple(c) for c, _ in chosen}
    for h in roots:
        if len(chosen) >= PICK_PER_ROUND:
            break
        if tuple(h) not in seen and tuple(h) not in T.picks and all(PR.is_glyph(c) for c in h):
            seen.add(tuple(h)); chosen.append((h, "root"))
    while kids and len(chosen) < PICK_PER_ROUND:                 # roots ran short: the rest to children
        chosen.append((kids.pop(0)[0], "branch"))
    out = []
    for n, (ctx, how) in enumerate(chosen, 1):
        out += [("pick", ctx, None, {"why": "pick", "from": how}, {"sample": k}) for k in range(PR.SAMPLES)]
        if n % PICK_NULL_EVERY == 0:
            rn = PR.R("pick-null", {"round": rid, "ctx": ctx})
            null = []
            while len(null) < len(ctx):
                c = fresh_glyph(rn)
                if c not in null:
                    null.append(c)
            out += [("pick", null, None, {"why": "pick-null"}, {"sample": k, "null": True}) for k in range(PR.SAMPLES)]
    return out

def reflection_work(P, seqs, rid):
    """Reflection (METHODOLOGY §3; Joseph's postulate that any linear sequence becomes periodic played backwards at its
    end): `a b c b -> ?` -- does a family turn round (a), or not? Asked of the first-impression roster at points inside
    the best-ranked sequences, worded as a plain continue question; answers kept apart, never growing a sequence."""
    out = []
    for s in seqs:
        g = s["glyphs"]
        if len(g) < 4 or s["rank"] < JOIN_WEAK:
            continue
        r = PR.R("reflection-at", {"round": rid, "seq": g})
        i = r.randint(2, len(g) - 2)
        k = r.randint(2, 3)
        ctx = g[max(0, i - k):i + 1] + [g[i - 1]]                       # ... a b c, then back to b
        out.append(("continue", ctx, None, {"why": "reflection", "seq": "".join(g), "mirror": g[i - 2]}))
    return out

def reasoned_work(P, seqs, rid):
    """the reasoned pass (METHODOLOGY §4): generation at felt ends, then recognition of what it generates.
    -> (recognition inhibit questions, reasoned continue questions)"""
    T = P.T
    recog = []
    for ctx, rows in T.reasoned.items():
        top = T.top(ctx)
        for x in dict.fromkeys(r["continuation"][0] for r in rows if r["continuation"]):
            if x != top and x not in ctx and PR.is_glyph(x) and (ctx, x) not in T.inhibit:
                recog.append(("inhibit", list(ctx), x, {"why": "recognize", "reasoned_by": sorted({r["mind"] for r in rows})}))
    gen = []
    for s in seqs:
        g = s["glyphs"]
        for side, stop in (("right", s["stop_right"]), ("left", s["stop_left"])):
            if stop != "end":
                continue
            run = g if side == "right" else g[::-1]
            k = min(len(run), PR.R("reasoned-k", {"round": rid, "seq": g, "side": side}).randint(3, 8))
            gen.append(("continue", run[-k:], None, {"why": "reasoned", "seq": "".join(g), "side": side, "rank": round(s["rank"], 4)}))
    return recog, gen

def join_work(P, s, r, ends):
    """Join probes (Joseph, 2026-10-05: "yes please -- for example, row #1 and row #14 will be joined hopefully soon"),
    asked before the sequence's other tier-1 work:
      a weak link inside a strong run (agreement < JOIN_WEAK, with >= 2 steps at or above it on each side): ask it from
        the other direction, a context not yet asked; failing that, replicate the weak context itself once (one more
        round of answers, whatever they say) -- the one place the planner re-asks a context;
      an open end whose written answers (>= 2) name an end glyph of another sequence: its end question, first."""
    g = s["glyphs"]; T = P.T
    out = []
    pos = {x: i for i, x in enumerate(g)}
    links = []
    for st in s["steps"]:
        a, b = st["ctx"][-1], st["x"]
        if a in pos and b in pos and abs(pos[a] - pos[b]) == 1:
            links.append((min(pos[a], pos[b]), st))
    for i, st in links:
        if st["agreement"] >= JOIN_WEAK:
            continue
        left = sum(1 for j, o in links if j < i and o["agreement"] >= JOIN_WEAK)
        right = sum(1 for j, o in links if j > i and o["agreement"] >= JOIN_WEAK)
        if left < 2 or right < 2:
            continue
        a, b = st["ctx"][-1], st["x"]
        other = g[pos[b]:][::-1] if pos[b] > pos[a] else g[:pos[b] + 1]   # approaching b from the far side
        k = min(len(other), r.randint(3, 8))
        if tuple(other[-k:]) not in T.real:
            out.append(("continue", other[-k:], None, {"why": "join-reverse", "seq": "".join(g), "link": a + b}))
        elif tuple(st["ctx"]) not in T.replicated:
            out.append(("continue", st["ctx"], None, {"why": "join-replicate", "seq": "".join(g), "link": a + b, "replicate": True}))
    for side, stop in (("right", s["stop_right"]), ("left", s["stop_left"])):
        if stop != "open":
            continue
        run = g if side == "right" else g[::-1]
        w = collections.Counter()
        for j in range(2, min(TR.MAXK, len(run)) + 1):
            for f, xs in T.written.get(tuple(run[-j:]), {}).items():
                w.update(xs)
        bridge = [(x, n) for x, n in w.most_common() if n >= 2 and x not in g and x in ends]
        if bridge:
            k = min(len(run), r.randint(3, 8))
            out.append(("continue", run[-k:], None, {"why": "join-end", "seq": "".join(g), "side": side, "bridge": bridge[0][0]}))
    return out

def falsify_work(P, s, r):
    """Tests that could break a sequence (Joseph, 2026-10-05: "think in terms of the scientific method as well as a
    counter-balance -- we're looking for things that disprove or call into question certain sequences"), aimed at the
    strongest claims first (sequences are served by rank). For a walked step a -> b followed by c:
      skip      inhibit at a's context with candidate c: does c come DIRECTLY after? A sequence predicts "no"; "yes"
                beyond the family's control rate challenges the adjacency (order without adjacency, or a chart walk).
      lengthen  a longer context along the same path, not yet asked (METHODOLOGY §3: a stable edge "stays put when the
                context is lengthened backward ... flips are where branches live"). The longest context decides, so a
                flip there breaks the link wherever links are judged.
    At most one of each per sequence a round, alternating which step, so the tests spread across sequences."""
    g = s["glyphs"]; T = P.T
    pos = {x: i for i, x in enumerate(g)}
    strong = [st for st in s["steps"] if st["agreement"] >= JOIN_WEAK and st["ctx"][-1] in pos and st["x"] in pos
              and abs(pos[st["ctx"][-1]] - pos[st["x"]]) == 1]
    if not strong:
        return []
    out = []
    st = strong[r.randrange(len(strong))]
    a, b = st["ctx"][-1], st["x"]
    step = pos[b] - pos[a]                                      # +1 forward, -1 backward
    ic = pos[b] + step
    if 0 <= ic < len(g) and g[ic] not in st["ctx"]:
        out.append(("inhibit", st["ctx"], g[ic], {"why": "falsify-skip", "seq": "".join(g), "link": a + b}))
    # triad: a triple of the run whose two links are both strong predicts its middle (§4); never asked as a triad
    sl = {frozenset((x["ctx"][-1], x["x"])) for x in strong}
    triples = [g[i:i + 3] for i in range(len(g) - 2)
               if frozenset(g[i:i + 2]) in sl and frozenset(g[i + 1:i + 3]) in sl and tuple(sorted(g[i:i + 3])) not in T.triads_fam]
    if triples:
        t = triples[r.randrange(len(triples))]
        out.append(("triad", t, None, {"why": "falsify-triad", "seq": "".join(g), "mid": t[1]}))
    st = strong[r.randrange(len(strong))]
    a, b = st["ctx"][-1], st["x"]
    path = g[:pos[a] + 1] if pos[b] > pos[a] else g[pos[a]:][::-1]      # the run up to a, in reading order
    for k in range(len(st["ctx"]) + 2, min(TR.MAXK, len(path)) + 1):
        if tuple(path[-k:]) not in T.real:
            out.append(("continue", path[-k:], None, {"why": "falsify-lengthen", "seq": "".join(g), "link": a + b, "k": k}))
            break
    return out

def sequence_work(P, s, r, ends=frozenset()):
    g = s["glyphs"]; T = P.T
    out = falsify_work(P, s, r) + join_work(P, s, r, ends)
    # 1 ends
    for side, stop in (("right", s["stop_right"]), ("left", s["stop_left"])):
        run = g if side == "right" else g[::-1]
        if stop == "open":
            k = min(len(run), r.randint(3, 8))
            out.append(("continue", run[-k:], None, {"why": "end", "seq": "".join(g), "side": side}))
        elif stop.startswith("wrap→"):
            x = stop.split("→", 1)[1]
            if x in run:
                period = run[run.index(x):]
                if len(set(period)) >= 4:
                    k = max(2, math.ceil(len(period) / 2))
                    if k < len(period):
                        out.append(("continue", period[-k:], None, {"why": "cycle-probe", "seq": "".join(g), "period": "".join(period)}))
    # 1b seed-only steps: ask the seeded context itself of the real minds
    for st in s["steps"]:
        if st.get("seed_only"):
            out.append(("continue", st["ctx"], None, {"why": "seed-step", "seq": "".join(g), "step": st["x"]}))
    # 2 k*: the shortest unasked suffix of each walked step's run
    for st in s["steps"]:
        if st["kstar_known"]:
            continue
        ctx = st["ctx"]
        for j in range(2, len(ctx)):
            if tuple(ctx[-j:]) not in T.real:
                out.append(("continue", ctx[-j:], None, {"why": "kstar", "seq": "".join(g), "step": st["x"], "k": len(ctx)}))
                break
    # 3b thin: precision where the strongest runs rest on few answers (METHODOLOGY §5, "square away the most obvious and
    # stable (empirically) sequences"). A walked step whose deciding context some answering family answered fewer than
    # twice is replicated once -- chosen by how many answers there are, never by what they say, so it cannot favour any
    # outcome; at most once (Tree.replicated), so no stopping rule.
    for st in s["steps"]:
        c = tuple(st["ctx"])
        if c in T.real and c not in T.replicated and min(len(v) for v in T.nodes[c].values()) < 2:
            out.append(("continue", st["ctx"], None, {"why": "thin", "seq": "".join(g), "step": st["x"], "replicate": True}))
    # 3 branches: does the runner-up continue?
    for st in s["steps"]:
        if st["alt"] and st["alt"][1] > 0:
            out.append(("inhibit", st["ctx"], st["alt"][0], {"why": "branch", "seq": "".join(g), "step": st["x"]}))
    # 4 inside: contexts ending on interior glyphs, either direction
    inside = []
    for run in (g, g[::-1]):
        for i in range(2, len(run) - 1):
            k = min(i + 1, r.randint(2, 4))
            ctx = run[i + 1 - k:i + 1]
            if tuple(ctx) not in T.real:
                inside.append(ctx)
    r.shuffle(inside)
    out += [("continue", c, None, {"why": "inside", "seq": "".join(g)}) for c in inside]
    return out

def triad_kernels(T):
    """§4: "a triad answer is also an unconditioned hint that a 3-glyph path exists, which makes it a cheap way to find
    kernels". Per triad (both eras), its most-named middle m: the path a m c, if the tree has not been shown it
    (neither [a, m] nor [c, m] asked). Weight: the estimated agreement on m (TR.estimate's posterior mean, families
    equal) -- a soft weight, never a cut (§7: "Priority uses it continuously, as a weight in the stochastic choice").
    -> [(a, m, c, weight)]"""
    out = []
    for t, fam in T.triads_fam.items():
        mids = collections.Counter(ans[1] for c in fam.values() for ans, n in c.items() for _ in range(n) if ans[0] == "mid")
        if not mids:
            continue
        m = mids.most_common(1)[0][0]
        a, c = [x for x in t if x != m]
        if tuple([a, m]) in T.real or tuple([c, m]) in T.real:
            continue
        _, mean, _, _ = TR.estimate([{f: (cnt[("mid", m)], sum(cnt.values())) for f, cnt in fam.items()}])
        out.append((a, m, c, mean))
    return out

def explore(P, seeds, n, rid):
    """Hot exploration (§5), in thirds by a fated draw (chosen without evidence): seed bumps, fresh glyphs (with their
    code-point neighbour or another fresh glyph), and triad-agreed kernels (§4) weighted by their middle's agreement."""
    r = PR.R("explore", {"round": rid})
    kernels = triad_kernels(P.T)
    settled = set()
    for s in P.seqs[:200]:
        if s["rank"] >= 0.9:
            settled.update(s["glyphs"])
    sd = [x for x in seeds if len(list(dict.fromkeys(x["glyphs"]))) >= 3]
    weights = [x.get("bump", 1.0) for x in sd]
    tries = 0
    added = 0
    while added < n and tries < n * 50:
        tries += 1
        u = r.random()
        if kernels and u < 1 / 3:
            a_, m_, c_ = r.choices(kernels, weights=[k[3] for k in kernels])[0][:3]
            ctx = [a_, m_] if r.random() < 0.5 else [c_, m_]
            how = {"why": "explore", "how": "triad-kernel"}
        elif sd and (u < 2 / 3 if kernels else u < 0.5):
            x = r.choices(sd, weights=weights)[0]
            gl = list(dict.fromkeys(x["glyphs"]))
            i = r.randrange(len(gl) - 1)
            ctx = gl[i:i + 2] if r.random() < 0.5 else gl[i:i + 2][::-1]
            how = {"why": "explore", "how": "seed", "seed": x.get("sid")}
        else:
            a = fresh_glyph(r)
            if a in settled and r.random() < 0.5:
                continue
            if r.random() < 0.5:
                b = chr(ord(a) + r.choice((-1, 1)))
                if not PR.is_glyph(b) or U.category(b) == "Cn":
                    continue
                how = {"why": "explore", "how": "codepoint-neighbour"}
            else:
                b = fresh_glyph(r)
                how = {"why": "explore", "how": "fresh"}
            ctx = [a, b]
        if P.add("continue", ctx, **how):
            added += 1
    return added

def plan(rid, recs, seeds, budget):
    T = TR.Tree(recs)
    seqs = TR.sequences(T)
    P = Plan(rid, T, budget)
    P.seqs = seqs
    n_explore = round(EXPLORE_SHARE * budget)
    explore(P, seeds, n_explore, rid)
    ends = {x for q in seqs for x in (q["glyphs"][0], q["glyphs"][-1])}
    work = []                                                  # (tier, sequence order, item order, item)
    for si, s in enumerate(seqs):
        r = PR.R("sequence-work", {"round": rid, "seq": s["glyphs"]})
        for ii, (kind, ctx, cand, src) in enumerate(sequence_work(P, s, r, ends)):
            work.append((TIER[src["why"]], si, ii, kind, ctx, cand, dict(src, rank=round(s["rank"], 4))))
    recog, gen = reasoned_work(P, seqs, rid)
    recog += written_recognition(P, seqs)
    # each recognition question gets a matched control at the same context (PR.control_candidate), near or far by fate
    paired = []
    for kind, ctx, cand, src in recog:
        paired.append((kind, ctx, cand, src))
        ck = "near" if PR.R("control-kind", {"round": rid, "context": ctx, "x": cand}).random() < 0.5 else "far"
        paired.append((kind, ctx, PR.control_candidate(ctx, cand, ck, rid), {"why": "control", "control": ck, "probe": {"control": ck}}))
    work += [(1, -1, ii, kind, ctx, cand, src) for ii, (kind, ctx, cand, src) in enumerate(paired)]
    written_seqs = TR.sequences(TR.Tree(recs, written=True))
    cw = cohere_work(P, seqs, written_seqs, seeds, rid)
    work += [(1, -1, len(paired) + ii, kind, ctx, cand, src) for ii, (kind, ctx, cand, src) in enumerate(cw)]
    work += [(1, -1, len(paired) + len(cw) + ii, kind, ctx, cand, src)
             for ii, (kind, ctx, cand, src) in enumerate(order_work(P, seqs, seeds, rid))]
    work.sort(key=lambda w: w[:3])
    n_reasoned = 0
    for kind, ctx, cand, src in gen:                       # outside the budget's tiers: asked only of reasoner minds
        if n_reasoned >= REASONED_PER_ROUND:
            break
        if P.add(kind, ctx, cand, variant="reasoned", **src):
            n_reasoned += 1
    n_reflect = 0
    for kind, ctx, cand, src in reflection_work(P, seqs, rid):          # outside the budget's tiers, like the reasoned pass
        if n_reflect >= REFLECT_PER_ROUND:
            break
        if P.add(kind, ctx, cand, variant="reflection", **src):
            n_reflect += 1
    n_pick = 0
    for kind, ctx, cand, src, probe in pick_work(P, seqs, seeds, rid):   # outside the budget's tiers: generator minds only
        if P.add(kind, ctx, cand, probe=probe, **src):
            n_pick += 1
    P.budget += n_reasoned + n_reflect + n_pick
    served, tiers_reached = set(), collections.Counter()
    for tier, si, ii, kind, ctx, cand, src in work:
        if P.full():
            break
        src = dict(src); probe = src.pop("probe", None)
        if P.add(kind, ctx, cand, probe=probe, **src):
            tiers_reached[tier] += 1
            if si >= 0:                                  # recognition questions belong to no one sequence
                served.add(si)
    last_rank = min((seqs[i]["rank"] for i in served), default=None)
    served = len(served)
    if not P.full():                                         # few sequences yet: more exploration
        explore(P, seeds, budget - len(P.qs), rid + "-more")
    stats = {"round": rid, "protocol": PR.PROTOCOL, "questions": len(P.qs), "budget": budget,
             "by_why": dict(collections.Counter(q["source"].get("why") for q in P.qs)),
             "by_kind": dict(collections.Counter(q["kind"] for q in P.qs)),
             "sequences": len(seqs), "sequences_served": served, "lowest_rank_served": last_rank,
             "by_tier": {str(k): v for k, v in sorted(tiers_reached.items())},
             "by_variant": dict(collections.Counter(q.get("variant") or "plain" for q in P.qs)),
             "contexts_in_tree": len(T.nodes)}
    return P.qs, stats
