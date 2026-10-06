#!/usr/bin/env python3
"""Concern 2: the context tree, and what is read off it (METHODOLOGY §2-3). Built from canonical answer records only;
never reads `source` (why a question was asked).

  tree.py   -> ../data/tree/SEQUENCES.md (+ sequences.json, cycles.json; regenerable, not committed)

NODES are contexts exactly as a mind was SHOWN them (oriented runs, 2-8 glyphs). A node holds, per family, the first
continuation each answer gave (a what-comes-next proposal of rank 1, or a continue answer's first written glyph),
"none" (an end), or "other" (not a glyph). Answers at a longer context are NOT pooled into its suffixes: k* needs each
length asked as itself.
WRITTEN answers (METHODOLOGY §4: "One answer yields a whole path of edges, each conditioned on everything before it"):
each glyph after a continue answer's first is that mind's continuation at its own context -- everything shown and
written before it (its last <= 8 glyphs, trimmed back to the nearest repeat, so contexts hold distinct glyphs as shown
ones do). They are stored as their own channel, `written` (ctx -> family -> [next]): an answer obtained from a context
the mind wrote itself rather than one it was shown, a probing distinction (concern 1) the tree keeps, not a reason to
drop anything. NODES stay answers to SHOWN contexts (plus seed votes): the walk below -- the planner's view of the
tree -- and k* read them. Which read-off pools which channel is that read-off's own stated choice (BEST.md reports
them separately). Tree(recs, written=True) pools written answers into the nodes, for read-offs that want candidates
from them. History: until 2026-10-05 no read-off and not the planner used `written` (this docstring claimed the
planner did), a bug against §4 that left about half of every multi-glyph answer unused.
SEEDS (Joseph, 2026-10-05): survey sequences count as votes from the surveyor's family (port/port_seeds.py), tagged
era "seed". They join nodes like any answer, so seeded paths are walkable at once; a context counts as ASKED only once
a real mind answered it (`real`), so the planner still asks every seeded context and k* is never "known" from seeds.
Tree(recs, seeds=False) gives the pure tree for a write-up.
INHIBITION: inhibit answers at (context, candidate): yes / no / can't tell, per family (METHODOLOGY §2b).
COHERENCE (METHODOLOGY §1, §4a): cohere answers about a whole shown run, yes / no / can't tell per family, keyed by the
run as shown (`cohere`); their controls -- the same glyphs shuffled -- and chart windows (a measurement, not a decoy:
probe.py) apart (`cohere_ctl`, and per family and class in `cohere_rate`); the why of every answer kept (`cohere_why`),
not read by anything yet. A run's coherence is evidence
about that run only, never about its sub-runs.
TRIADS and ORDER answers (§4: consistency checks; they create no edges): triads per family (`triads_fam`, both eras),
order answers indexed by glyph (`orders`, the triad era's). REFLECTIONS (§3): answers to contexts that turn back on
themselves, kept apart (`reflections`); they never grow a sequence.
AGREEMENT for a continuation x at a node: per family, the share of its answers naming x first; mean over the families
that answered. Soft: it orders and is shown, nothing is cut by it.

SEQUENCES: walks. At each step take the longest suffix (2-8 glyphs) of the path so far that was asked exactly, and its
most-agreed continuation (ties: families, answers, codepoint). Stops: end (the node's top answer is "none"), open (no
suffix of the path was asked: the planner's work), other (top answer not a glyph), wrap (the continuation is already
in the path). Each walk runs both ways (a sequence and its reverse are one sequence); a walk contained in a longer one
in the same order is that one at an earlier stage. A sequence holds SUPPORTED LINKS only: the starting context was shown,
not walked, and an asked context may hold a gap (the triad era asked `⑩ ⑪ ⑬ ⑭`, `㊳ ㊲ ㉒ ㉑`), so each link that no step
walked is checked against the tree (the longest asked context ending at either glyph names the other as its top), and
the walk is split where none does; a split end is open (found 2026-10-05: 18 "settled" sequences carried such gaps).
k*: per walked step, the shortest asked suffix whose top continuation is the step's glyph, with every asked longer
suffix agreeing. It is KNOWN when every shorter suffix down to 2 glyphs has been asked; otherwise it is an upper bound.
CYCLES (METHODOLOGY §3): only where a continue answer MANIFESTS one: the shown context plus what the mind wrote holds a
stretch with period p of length >= 2p + 1 (2p edges, "the entire pattern has repeated itself"), of which the mind
wrote at least p + 1 and was shown less than one whole period (writing again a period that was shown whole is
repetition, not closure: METHODOLOGY §4; found 2026-10-05 on end questions over 4-glyph runs). Periods with fewer than 4 distinct glyphs are recorded but out of scope for now.
"""
import collections, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[1]
ANS = ROOT / "data" / "answers"
OUT = ROOT / "data" / "tree"
MAXK = 8
NONE, OTHER = "<none>", "<other>"

def load():
    recs = []
    for f in sorted(ANS.glob("*.jsonl")):
        recs += [json.loads(l) for l in open(f) if l.strip()]
    return recs

def _in_order(ps, cyclic):
    """positions in order, either direction; for a cycle, monotone round the circle (at most one wrap)"""
    for q in (ps, ps[::-1]):
        drops = sum(1 for x, y in zip(q, q[1:]) if y < x)
        if drops == 0 or (cyclic and drops == 1 and q[-1] < q[0]):
            return True
    return False

def beta_mv(k, n):
    """posterior mean and variance of a family's share naming x, from k of n answers, Jeffreys prior Beta(1/2, 1/2)"""
    a, b = k + 0.5, n - k + 0.5
    return a / (a + b), a * b / ((a + b) ** 2 * (a + b + 1))

def estimate(dirs):
    """A link's agreement from its reading directions. dirs: [{family: (k, n)}] -> (observed, mean, sd, families naming).
    observed: the mean over directions of the mean over families of each family's share (the perceptual quantity);
    mean / sd: the same over Beta posteriors (Jeffreys), the means treated as normal (an approximation) -- how sure we
    are of it. Readers choose their own confidence (lower bound = mean - z * sd)."""
    obs, mean, var, fams = [], [], [], set()
    for d in dirs:
        F = len(d)
        mv = [beta_mv(k, n) for k, n in d.values()]
        obs.append(sum(k / n for k, n in d.values()) / F)
        mean.append(sum(m for m, _ in mv) / F)
        var.append(sum(v for _, v in mv) / F ** 2)
        fams |= {f for f, (k, n) in d.items() if k > 0}
    D = len(dirs)
    return sum(obs) / D, sum(mean) / D, (sum(var) / D ** 2) ** 0.5, fams

def estimate_vs(counts, control):
    """A yes/no proportion against a control. counts, control: {family: (k, n)} -> (difference, sd, families used): per
    family the Beta-posterior (Jeffreys) mean of counts minus that of its control, variances added; the equal-weight
    mean over the families that have both, sd as in estimate()."""
    d, v, fams = [], [], []
    for f, (k, n) in counts.items():
        ck, cn = control.get(f, (0, 0))
        if n and cn:
            (m1, v1), (m2, v2) = beta_mv(k, n), beta_mv(ck, cn)
            d.append(m1 - m2); v.append(v1 + v2); fams.append(f)
    if not d:
        return None, None, []
    F = len(d)
    return sum(d) / F, (sum(v) / F ** 2) ** 0.5, fams

def canon_cycle(P):
    rots = [tuple(P[i:] + P[:i]) for i in range(len(P))]
    return min(rots + [tuple(reversed(r)) for r in rots])

def manifest(S, shown):
    """smallest period p with a stretch of length >= 2p+1 in S, >= p+1 of it written (index >= shown), and less than a
    whole period of it shown -> P or None. The last condition (2026-10-05): end questions on 4-glyph runs showed the whole
    period (`◁ ▽ ▷ △ | ◁ ▽ ▷ △ …`), and writing it again is repeating what was shown, not closing a cycle oneself;
    METHODOLOGY §4: a repeat must be the mind's own."""
    n = len(S)
    for p in range(2, n // 2 + 1):
        run_start = 0
        for j in range(n - p + 1):
            if j + p < n and S[j] == S[j + p]:
                # stretch [run_start, j + p] is p-periodic
                L = j + p - run_start + 1
                P = S[run_start:run_start + p]
                if any(p % q == 0 and P == P[:q] * (p // q) for q in range(1, p)):
                    continue                     # a repeat of a shorter period, already judged at that period
                if L >= 2 * p + 1 and (j + p + 1 - max(shown, run_start)) >= p + 1 and max(0, shown - run_start) < p:
                    return S[run_start:run_start + p]
            else:
                run_start = j + 1
    return None

class Tree:
    def __init__(self, recs, seeds=True, written=False):
        self.nodes = collections.defaultdict(lambda: collections.defaultdict(list))     # ctx -> family -> [first]
        self.written = collections.defaultdict(lambda: collections.defaultdict(list))   # ctx -> family -> [next]
        self.inhibit = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))  # (ctx,x)->fam->verdict
        self.triads = collections.defaultdict(collections.Counter)
        self.triads_fam = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))  # glyphs->fam->ans
        self.orders = collections.defaultdict(list)       # glyph -> [(family, shown, lines)] for order answers (triad era)
        self.reflections = collections.defaultdict(list)  # ctx -> [{family, mind, continuation, outcome}] (§3)
        self.inhibit_rate = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))  # fam->class->verdict
        self.cohere = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))      # run -> fam -> verdict
        self.cohere_ctl = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))  # shuffled run -> ...
        self.cohere_rate = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))  # fam -> class -> verdict
        self.cohere_why = collections.defaultdict(list)     # run -> [(family, mind, verdict, why)]
        self.control_pairs = set()                        # (ctx, candidate) asked as controls (kept out of `inhibit`)
        self.cycles = {}
        self.real = set()                       # contexts some real mind answered (not only seed votes)
        self.unreasoned = collections.defaultdict(list)   # ctx -> [first] from answers given with 0 thinking tokens
        self.reasoned = collections.defaultdict(list)     # ctx -> [{mind, family, continuation, tools}] (reasoned pass)
        self.seeded = set()
        self.replicated = set()                 # shown contexts answered in more than one round (asked again)
        self._rounds = {}
        for r in recs:
            k, o = r["kind"], r["outcome"]
            if k == "seed":
                if seeds:
                    ctx = tuple(r["context"])
                    self.nodes[ctx][r["family"]].append(r["continuation"][0]); self.seeded.add(ctx)
                continue
            if k == "continue" and (r.get("tags") or {}).get("variant") == "reflection":
                # METHODOLOGY §3: the minds' grammar of sequences, not their perception of the glyphs; never grows one
                if o in ("continuation", "none", "other"):
                    self.reflections[tuple(r["context"])].append({"family": r["family"], "mind": r["mind"], "outcome": o,
                                                                  "continuation": r.get("continuation") or []})
                continue
            if k == "continue" and (r.get("tags") or {}).get("variant") == "reasoned":
                # generation, not evidence: kept apart (METHODOLOGY §4); its candidates are put to recognition
                if o in ("continuation", "none"):
                    self.reasoned[tuple(r["context"])].append({"mind": r["mind"], "family": r["family"],
                                                               "continuation": r.get("continuation") or [], "outcome": o})
                continue
            if k in ("next", "continue") and o in ("proposals", "continuation", "none", "other"):
                ctx = tuple(r["context"])
                if o == "none":
                    first = NONE
                elif k == "next":
                    props = [p["g"] for p in sorted(r.get("proposals", []), key=lambda p: p["rank"])]
                    first = props[0] if props else OTHER
                else:
                    seq = r.get("continuation") or []
                    first = seq[0] if seq else OTHER
                    S = list(ctx) + seq
                    for i in range(1, len(seq)):
                        c2 = list(S[max(0, len(ctx) + i - MAXK):len(ctx) + i])
                        while len(set(c2)) < len(c2):               # back to the nearest repeat
                            c2 = c2[1:]
                        if len(c2) < 2:
                            continue
                        c2 = tuple(c2)
                        self.written[c2][r["family"]].append(seq[i])
                        if written:
                            self.nodes[c2][r["family"]].append(seq[i])
                            if (r.get("tags") or {}).get("thinking_tokens") == 0:
                                self.unreasoned[c2].append(seq[i])
                    P = manifest(S, len(ctx))
                    if P:
                        key = canon_cycle(list(P))
                        e = self.cycles.setdefault(key, {"pattern": list(key), "answers": 0, "families": set(), "minds": set(),
                                                         "distinct": len(set(key)), "examples": []})
                        e["answers"] += 1; e["families"].add(r["family"]); e["minds"].add(r["mind"])
                        if len(e["examples"]) < 3:
                            e["examples"].append(" ".join(ctx) + " | " + " ".join(seq))
                self.nodes[ctx][r["family"]].append(first); self.real.add(ctx)
                self._rounds.setdefault(ctx, set()).add(r.get("round"))
                if len(self._rounds[ctx]) > 1:
                    self.replicated.add(ctx)
                if (r.get("tags") or {}).get("thinking_tokens") == 0:
                    self.unreasoned[ctx].append(first)
            elif k == "inhibit" and o in ("yes", "no", "cant-tell"):
                ctl = (r.get("tags") or {}).get("control")
                self.inhibit_rate[r["family"]][ctl or "real"][o] += 1     # probing tag (§2a: the tree may split by it)
                if ctl:
                    self.control_pairs.add((tuple(r["context"]), r["candidate"]))
                else:
                    self.inhibit[(tuple(r["context"]), r["candidate"])][r["family"]][o] += 1
            elif k == "cohere" and o in ("yes", "no", "cant-tell"):
                ctl = (r.get("tags") or {}).get("control")
                run = tuple(r["context"])
                self.cohere_rate[r["family"]][ctl or "real"][o] += 1
                (self.cohere_ctl if ctl else self.cohere)[run][r["family"]][o] += 1
                self.cohere_why[run].append((r["family"], r["mind"], o, r.get("why", "")))
            elif k == "triad" and o in ("mid", "two", "none"):
                t = tuple(sorted(r["shown"]))
                ans = tuple(r["answer"]) if o != "none" else ("none",)
                self.triads[t][ans] += 1
                self.triads_fam[t][r["family"]][ans] += 1
            elif k == "order" and o == "lines":
                lines = (r.get("answer") or {}).get("lines") or []
                item = (r["family"], tuple(r["shown"]), lines)
                for x in set(r["shown"]):
                    self.orders[x].append(item)

    # ---- node read-offs
    def dist(self, ctx):
        fam = self.nodes.get(ctx)
        if not fam:
            return {}
        per = collections.defaultdict(dict); cnt = collections.Counter(); fams = collections.defaultdict(set)
        for f, firsts in fam.items():
            c = collections.Counter(firsts)
            for x, n in c.items():
                per[x][f] = n / len(firsts); cnt[x] += n; fams[x].add(f)
        nf = len(fam)
        return {x: (sum(per[x].values()) / nf, len(fams[x]), cnt[x]) for x in per}

    def ranked(self, ctx):
        return sorted(self.dist(ctx).items(), key=lambda kv: (-kv[1][0], -kv[1][1], -kv[1][2], kv[0]))

    def top(self, ctx):
        r = self.ranked(ctx)
        return r[0][0] if r else None

    def lookup(self, run):
        """the longest suffix (2-8 glyphs) of `run` that has answers"""
        for j in range(min(MAXK, len(run)), 1, -1):
            if tuple(run[-j:]) in self.nodes:
                return tuple(run[-j:])
        return None

    def kstar(self, run, x):
        """-> (k*, known) for x after `run`: shortest asked suffix whose top is x with all asked longer ones agreeing."""
        asked = [(j, self.top(tuple(run[-j:]))) for j in range(2, min(MAXK, len(run)) + 1) if tuple(run[-j:]) in self.real]
        if not asked:
            return None, False
        ks = None
        for j, t in sorted(asked, reverse=True):
            if t == x:
                ks = j
            else:
                break
        if ks is None:
            return None, False
        known = all(tuple(run[-j:]) in self.real for j in range(2, ks))
        return ks, known

    def inhibition(self, ctx, x):
        c = self.inhibit.get((tuple(ctx), x))
        if not c:
            return None
        tot = collections.Counter()
        for f, v in c.items():
            tot.update(v)
        return dict(tot)

    # ---- walks
    def walk(self, path):
        path = list(path); steps = []
        while len(path) < 64:
            ctx = self.lookup(path)
            if ctx is None:
                return path, steps, "open"
            rk = self.ranked(ctx)
            x, (agr, nfam, n) = rk[0]
            alt = next(((y, v) for y, v in rk[1:] if y not in (NONE, OTHER)), None)
            if x == NONE:
                return path, steps, "end"
            if x == OTHER:
                return path, steps, "other"
            ks, known = self.kstar(path, x)
            st = {"ctx": list(ctx), "k": len(ctx), "x": x, "agreement": agr, "families": nfam, "answers": n,
                  "seed_only": ctx not in self.real,
                  "alt": alt and [alt[0], alt[1][0]], "kstar": ks, "kstar_known": known}
            if x in path:
                return path, steps + [st], "wrap→" + x
            steps.append(st); path.append(x)
        return path, steps, "cap"

    # ---- what the evidence says about a link or a path (read by SEQUENCES, BEST and the planner alike)
    def shown_dir(self, run, x):
        """one reading direction of a link on shown answers: per-family (k naming x, n) at the deciding context (the
        longest asked suffix of `run`), its top answer, and the unreasoned (k, n) there -> dict or None"""
        if len(run) < 2:
            return None
        ctx = self.lookup(run)
        if not ctx:
            return None
        u = self.unreasoned.get(ctx, [])
        return {"counts": {f: (sum(1 for y in xs if y == x), len(xs)) for f, xs in self.nodes[ctx].items()},
                "top": self.top(ctx), "uk": sum(1 for f in u if f == x), "un": len(u)}

    def written_dir(self, run, x):
        """one reading direction on written answers whose context is a suffix of `run` -> {"counts": ...} or None"""
        if len(run) < 2:
            return None
        per = collections.defaultdict(list)
        for j in range(2, min(MAXK, len(run)) + 1):
            for f, xs in self.written.get(tuple(run[-j:]), {}).items():
                per[f] += xs
        return {"counts": {f: (sum(1 for y in xs if y == x), len(xs)) for f, xs in per.items()}} if per else None

    def contradicts(self, run, x, none_counts):
        """does the shown deciding context after `run` name something other than x? ("none" only if none_counts)"""
        ctx = self.lookup(run) if len(run) >= 2 else None
        if not ctx:
            return False
        top = self.top(ctx)
        if top == x:
            return False
        if top == NONE:
            return none_counts
        return top != OTHER

    def control_counts(self, family, cls="near"):
        """a family's (yes, n) over its inhibit answers of a class ("real", "near", "far")"""
        c = self.inhibit_rate.get(family, {}).get(cls) or {}
        return c.get("yes", 0), sum(c.values())

    def consistency_evidence(self, g, cyclic=False):
        """FACTS for testing a path against the non-edge evidence (§2b, §4, §6); decisions are the reader's. Each unit
        is {family: (k, n)} -- k answers giving the response the unit counts, of n:
          skip   for each a -> b -> c (either reading direction), inhibit answers at the longest context ending at a
                 (within the run) that asked about c: k = "yes" (c directly after?), to be read against controls
          triad  for each triple a b c, its triad answers (both eras): k = middle named b
          order  for each order answer set within g (>= 3 glyphs, triad era): k = answers whose every line runs in g's
                 order, either direction -- round the circle if g is a cycle (cyclic=True: a line starting elsewhere on
                 the circle is in order)
        -> {"skip": [...], "triad": [...], "order": [...]}"""
        out = {"skip": [], "triad": [], "order": []}
        for run in (g, g[::-1]):
            for i in range(len(run) - 2):
                prefix, x = run[:i + 1], run[i + 2]
                for j in range(min(MAXK, len(prefix)), 1, -1):          # the longest context asked about x decides
                    fam = self.inhibit.get((tuple(prefix[-j:]), x))
                    if fam:
                        out["skip"].append({f: (c["yes"], sum(c.values())) for f, c in fam.items()})
                        break
        for i in range(len(g) - 2):
            fam = self.triads_fam.get(tuple(sorted(g[i:i + 3])))
            if fam:
                out["triad"].append({f: (c[("mid", g[i + 1])], sum(c.values())) for f, c in fam.items()})
        pos = {x: i for i, x in enumerate(g)}
        sets = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0]))
        seen = set()
        for x in g:
            for item in self.orders.get(x, []):
                fam, shown, lines = item
                if id(item) in seen or len(shown) < 3 or not all(y in pos for y in shown):
                    continue
                seen.add(id(item))
                agree = True
                for line in lines:
                    ps = [pos[y] for step in line for y in (step if isinstance(step, list) else [step]) if y in pos]
                    if len(ps) >= 2 and not _in_order(ps, cyclic):
                        agree = False
                sets[shown][fam][0] += agree
                sets[shown][fam][1] += 1
        out["order"] = [{f: tuple(v) for f, v in fam.items()} for fam in sets.values()]
        return out

    def coherence(self, g, cyclic=False):
        """FACTS for "g is recognised as a sequence": cohere answers about g as shown in either direction (a sequence and
        its reverse are one sequence), and round the circle if cyclic -> {family: (yes, n)}, or {} if never asked"""
        g = list(g)
        runs = {tuple(g), tuple(g[::-1])}
        if cyclic:
            runs |= {tuple(h[i:] + h[:i]) for h in (g, g[::-1]) for i in range(len(h))}
        tot = collections.defaultdict(collections.Counter)
        for run in runs:
            for f, c in self.cohere.get(run, {}).items():
                tot[f].update(c)
        return {f: (c["yes"], sum(c.values())) for f, c in tot.items()}

    def cohere_control_counts(self, family):
        """a family's (yes, n) over cohere answers to shuffled controls"""
        c = self.cohere_rate.get(family, {}).get("shuffled") or {}
        return c.get("yes", 0), sum(c.values())

    def recognition_evidence(self):
        """FACTS for recognition: per candidate (controls excluded), per family (yes, n) -> [{ctx, x, counts}]"""
        return [{"ctx": ctx, "x": x, "counts": {f: (c["yes"], sum(c.values())) for f, c in fc.items()}}
                for (ctx, x), fc in self.inhibit.items()]

    def triad_check(self, g):
        agree = against = 0
        for a, m, b in zip(g, g[1:], g[2:]):
            for out, n in self.triads.get(tuple(sorted((a, m, b))), {}).items():
                if out[0] == "mid" and out[1] == m:
                    agree += n
                else:
                    against += n
        return agree, against

def sequences(T):
    found = {}
    for ctx in list(T.nodes):
        t = T.top(ctx)
        if t is None or t in (NONE, OTHER) or t in ctx:
            continue
        fwd, fsteps, fstop = T.walk(list(ctx))
        bwd, bsteps, bstop = T.walk(fwd[::-1])
        g = bwd[::-1]
        steps = fsteps + bsteps
        # A sequence is made only of walked links (METHODOLOGY §3). The starting context was SHOWN, not walked, and an
        # asked context can hold a gap (the triad era asked `⑩ ⑪ ⑬ ⑭` and `㊳ ㊲ ㉒ ㉑`, cut from its own gapped rows).
        # So split wherever neighbouring glyphs are joined by no walked step in either direction; a split end is open.
        linked = {frozenset((st["ctx"][-1], st["x"])) for st in steps}
        def supported(i):
            """g[i]-g[i+1] is walked, or the tree's longest asked context ending at either one names the other as top"""
            if frozenset((g[i], g[i + 1])) in linked:
                return True
            fc, bc = T.lookup(g[:i + 1]), T.lookup(g[i + 1:][::-1])
            return bool((fc and T.top(fc) == g[i + 1]) or (bc and T.top(bc) == g[i]))
        cuts = [i for i in range(len(g) - 1) if not supported(i)]
        bounds = [0] + [i + 1 for i in cuts] + [len(g)]
        for a, b in zip(bounds, bounds[1:]):
            piece = g[a:b]
            if len(piece) < 2:
                continue
            pl = {frozenset(p) for p in zip(piece, piece[1:])}
            key = tuple(min(piece, piece[::-1]))
            if key not in found:
                found[key] = {"glyphs": piece, "start": list(ctx), "stop_left": bstop if a == 0 else "open",
                              "stop_right": fstop if b == len(g) else "open",
                              "steps": [st for st in steps if frozenset((st["ctx"][-1], st["x"])) in pl]}
    seqs = sorted(found.values(), key=lambda s: -len(s["glyphs"]))
    def contained(a, b):
        n = len(a)
        return n < len(b) and any(b[i:i + n] in (a, a[::-1]) for i in range(len(b) - n + 1))
    kept = []
    for s in seqs:
        if not any(contained(s["glyphs"], k["glyphs"]) for k in kept):
            kept.append(s)
    for s in kept:
        w = [st for st in s["steps"] if not st["x"] in s["glyphs"][:0]]
        s["walked"] = len(w)
        s["agreement"] = min((st["agreement"] for st in w), default=0.0)
        s["mean_agreement"] = sum(st["agreement"] for st in w) / len(w) if w else 0.0
        s["k_used"] = sorted({st["k"] for st in w})
        s["kstar_known"] = sum(1 for st in w if st["kstar_known"])
        s["seed_only"] = sum(1 for st in w if st.get("seed_only"))
        s["branches"] = [f"{''.join(st['ctx'])}→{st['alt'][0]} ({st['alt'][1]:.2f})" for st in w if st["alt"] and st["alt"][1] >= 0.25]
        s["triads"] = T.triad_check(s["glyphs"])
        s["rank"] = s["mean_agreement"] * min(1.0, s["walked"] / 4)
        for side in ("stop_left", "stop_right"):
            if s[side].startswith("wrap"):
                key = canon_cycle(s["glyphs"])
                if key in T.cycles:
                    s[side] = "cycle (manifested)"
    kept.sort(key=lambda s: (-s["rank"], -len(s["glyphs"]), s["glyphs"]))
    return kept

def main(seeds=True):
    T = Tree(load(), seeds=seeds)
    seqs = sequences(T)
    OUT.mkdir(parents=True, exist_ok=True)
    json.dump(seqs, open(OUT / "sequences.json", "w"), ensure_ascii=False)
    cyc = sorted(({**v, "families": sorted(v["families"]), "minds": sorted(v["minds"])} for v in T.cycles.values()),
                 key=lambda c: (-len(c["families"]), -c["answers"]))
    json.dump(cyc, open(OUT / "cycles.json", "w"), ensure_ascii=False)
    stops = collections.Counter()
    for s in seqs:
        stops[s["stop_left"].split("→")[0]] += 1; stops[s["stop_right"].split("→")[0]] += 1
    rounds = sorted({r for r in (json.loads(l)["round"] for f in ANS.glob("*.jsonl") for l in open(f) if l.strip())})
    L = ["# Sequences read off the context tree", "",
         f"*Generated by `refactored/tree/tree.py` from the canonical answer records in `refactored/data/answers/` (rounds {rounds[0]}–{rounds[-1]}; the triad era is ported, see its PORT-REPORT). {len(T.nodes)} asked contexts; {len(seqs)} sequences; {sum(1 for c in cyc if c['distinct'] >= 4)} manifested cycles in scope.*", "",
         "**How to read a row.** A sequence is a path through the context tree. Starting from an asked context, each step takes the continuation most agreed on at the longest stretch of the path so far that the minds were actually shown, and the walk runs both ways.",
         "- **walked:** steps taken by the walk; the starting context's glyphs were shown, not walked.",
         "- **agreement min / mean:** per family, the share of its answers naming that continuation first, averaged over the families that answered.",
         "- **seed-only:** walked steps carried by a context that only seed votes have answered so far (the survey sequences, counted as votes from the surveyor's family and tagged; Joseph, 2026-10-05). The planner asks every such context of the real minds. `tree.py --pure` leaves seeds out.",
         "- **k used:** the context lengths that carried the steps. **k\\* known:** steps whose shortest sufficient context is pinned down, with every shorter context also asked.",
         "- **ends:** what stopped each walk:",
         "  - *end*: the minds answered \"none\";",
         "  - *open*: never asked, so this is the planner's work;",
         "  - *wrap→x*: the continuation is already in the path, not a cycle unless manifested;",
         "  - *cycle (manifested)*: a mind wrote the whole pattern twice;",
         "  - *other*: the answer was not a single glyph.",
         "- **branches:** runner-up continuations with agreement ≥ 0.25: `context→alternative (agreement)`.",
         "- **triads:** triad answers on consecutive triples, agreeing with the order : not.", "",
         "Walk stops over all ends: " + ", ".join(f"{k} {v}" for k, v in stops.most_common()) + ".", ""]
    if cyc:
        L += ["## Manifested cycles", "", "| period | distinct | answers | families | example (shown \\| written) |", "|---|---|---|---|---|"]
        for c in cyc[:60]:
            L.append(f"| `{' '.join(c['pattern'])}` | {c['distinct']}{'' if c['distinct'] >= 4 else ' (out of scope)'} | {c['answers']} | {', '.join(c['families'])} | `{c['examples'][0]}` |")
        L.append("")
    L += ["## Sequences", "", "| # | sequence | n | walked | seed-only | agreement min / mean | k used | k* known | ends (left / right) | branches | triads |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, s in enumerate(seqs[:400], 1):
        L.append(f"| {i} | `{' '.join(s['glyphs'])}` | {len(s['glyphs'])} | {s['walked']} | {s['seed_only']} | {s['agreement']:.2f} / {s['mean_agreement']:.2f} | "
                 f"{','.join(map(str, s['k_used']))} | {s['kstar_known']}/{s['walked']} | {s['stop_left']} / {s['stop_right']} | {';<br>'.join(s['branches'][:4])} | {s['triads'][0]}:{s['triads'][1]} |")
    (ROOT / ("SEQUENCES.md" if seeds else "data/tree/SEQUENCES-pure.md")).write_text("\n".join(L) + "\n")
    print(f"{len(T.nodes)} contexts; {len(seqs)} sequences; {len(cyc)} manifested cycles; stops {dict(stops)}")

if __name__ == "__main__":
    main(seeds="--pure" not in sys.argv)
