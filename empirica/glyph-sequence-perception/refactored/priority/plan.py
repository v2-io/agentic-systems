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
    def full(self):
        return len(self.qs) >= self.budget
    def add(self, kind, ctx, cand=None, **src):
        ctx = list(ctx)
        if not (2 <= len(ctx) <= 8) or len(set(ctx)) != len(ctx) or not all(PR.is_glyph(x) for x in ctx):
            return False
        key = (kind, tuple(ctx), cand)
        if key in self.keys or (kind == "continue" and tuple(ctx) in self.asked):
            return False
        if kind == "inhibit" and ((tuple(ctx), cand) in self.T.inhibit or cand in ctx or not PR.is_glyph(cand)):
            return False
        self.keys.add(key)
        self.qs.append(PR.question(kind, ctx, cand, source=dict(src, round=self.rid)))
        return True

TIER = {"end": 1, "cycle-probe": 1, "seed-step": 2, "kstar": 3, "branch": 4, "inside": 5}

def sequence_work(P, s, r):
    g = s["glyphs"]; T = P.T
    out = []
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

def explore(P, seeds, n, rid):
    r = PR.R("explore", {"round": rid})
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
        if sd and r.random() < 0.5:
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
    work = []                                                  # (tier, sequence order, item order, item)
    for si, s in enumerate(seqs):
        r = PR.R("sequence-work", {"round": rid, "seq": s["glyphs"]})
        for ii, (kind, ctx, cand, src) in enumerate(sequence_work(P, s, r)):
            work.append((TIER[src["why"]], si, ii, kind, ctx, cand, dict(src, rank=round(s["rank"], 4))))
    work.sort(key=lambda w: w[:3])
    served, tiers_reached = set(), collections.Counter()
    for tier, si, ii, kind, ctx, cand, src in work:
        if P.full():
            break
        if P.add(kind, ctx, cand, **src):
            served.add(si); tiers_reached[tier] += 1
    last_rank = min((seqs[i]["rank"] for i in served), default=None)
    served = len(served)
    if not P.full():                                         # few sequences yet: more exploration
        explore(P, seeds, budget - len(P.qs), rid + "-more")
    stats = {"round": rid, "protocol": PR.PROTOCOL, "questions": len(P.qs), "budget": budget,
             "by_why": dict(collections.Counter(q["source"].get("why") for q in P.qs)),
             "by_kind": dict(collections.Counter(q["kind"] for q in P.qs)),
             "sequences": len(seqs), "sequences_served": served, "lowest_rank_served": last_rank,
             "by_tier": {str(k): v for k, v in sorted(tiers_reached.items())},
             "contexts_in_tree": len(T.nodes)}
    return P.qs, stats
