#!/usr/bin/env python3
"""Concern 2: the context tree, and what is read off it (METHODOLOGY §2-3). Built from canonical answer records only;
never reads `source` (why a question was asked).

  tree.py   -> ../data/tree/SEQUENCES.md (+ sequences.json, cycles.json; regenerable, not committed)

NODES are contexts exactly as a mind was SHOWN them (oriented runs, 2-8 glyphs). A node holds, per family, the first
continuation each answer gave (a what-comes-next proposal of rank 1, or a continue answer's first written glyph),
"none" (an end), or "other" (not a glyph). Answers at a longer context are NOT pooled into its suffixes: k* needs each
length asked as itself.
WRITTEN edges: a continue answer writes a path; its later glyphs are continuations of contexts the mind produced
itself (context + what it wrote so far). They are kept apart (`written`): a different measurement (the mind's own
momentum) from a shown context. They feed cycle manifestation and the planner's candidates, not the walk.
SEEDS (Joseph, 2026-10-05): survey sequences count as votes from the surveyor's family (port/port_seeds.py), tagged
era "seed". They join nodes like any answer, so seeded paths are walkable at once; a context counts as ASKED only once
a real mind answered it (`real`), so the planner still asks every seeded context and k* is never "known" from seeds.
Tree(recs, seeds=False) gives the pure tree for a write-up.
INHIBITION: inhibit answers at (context, candidate): yes / no / can't tell, per family (METHODOLOGY §2b).
AGREEMENT for a continuation x at a node: per family, the share of its answers naming x first; mean over the families
that answered. Soft: it orders and is shown, nothing is cut by it.

SEQUENCES: walks. At each step take the longest suffix (2-8 glyphs) of the path so far that was asked exactly, and its
most-agreed continuation (ties: families, answers, codepoint). Stops: end (the node's top answer is "none"), open (no
suffix of the path was asked: the planner's work), other (top answer not a glyph), wrap (the continuation is already
in the path). Each walk runs both ways (a sequence and its reverse are one sequence); a walk contained in a longer one
in the same order is that one at an earlier stage.
k*: per walked step, the shortest asked suffix whose top continuation is the step's glyph, with every asked longer
suffix agreeing. It is KNOWN when every shorter suffix down to 2 glyphs has been asked; otherwise it is an upper bound.
CYCLES (METHODOLOGY §3): only where a continue answer MANIFESTS one: the shown context plus what the mind wrote holds a
stretch with period p of length >= 2p + 1 (2p edges, "the entire pattern has repeated itself"), of which the mind
wrote at least p + 1. Periods with fewer than 4 distinct glyphs are recorded but out of scope for now.
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

def canon_cycle(P):
    rots = [tuple(P[i:] + P[:i]) for i in range(len(P))]
    return min(rots + [tuple(reversed(r)) for r in rots])

def manifest(S, shown):
    """smallest period p with a stretch of length >= 2p+1 in S, >= p+1 of it written (index >= shown) -> P or None"""
    n = len(S)
    for p in range(2, n // 2 + 1):
        run_start = 0
        for j in range(n - p + 1):
            if j + p < n and S[j] == S[j + p]:
                # stretch [run_start, j + p] is p-periodic
                L = j + p - run_start + 1
                if L >= 2 * p + 1 and (j + p + 1 - max(shown, run_start)) >= p + 1:
                    return S[run_start:run_start + p]
            else:
                run_start = j + 1
    return None

class Tree:
    def __init__(self, recs, seeds=True):
        self.nodes = collections.defaultdict(lambda: collections.defaultdict(list))     # ctx -> family -> [first]
        self.written = collections.defaultdict(lambda: collections.defaultdict(list))   # ctx -> family -> [next]
        self.inhibit = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))  # (ctx,x)->fam->verdict
        self.triads = collections.defaultdict(collections.Counter)
        self.cycles = {}
        self.real = set()                       # contexts some real mind answered (not only seed votes)
        self.seeded = set()
        for r in recs:
            k, o = r["kind"], r["outcome"]
            if k == "seed":
                if seeds:
                    ctx = tuple(r["context"])
                    self.nodes[ctx][r["family"]].append(r["continuation"][0]); self.seeded.add(ctx)
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
                        c2 = tuple(S[max(0, len(ctx) + i - MAXK):len(ctx) + i])
                        self.written[c2][r["family"]].append(seq[i])
                    P = manifest(S, len(ctx))
                    if P:
                        key = canon_cycle(list(P))
                        e = self.cycles.setdefault(key, {"pattern": list(key), "answers": 0, "families": set(), "minds": set(),
                                                         "distinct": len(set(key)), "examples": []})
                        e["answers"] += 1; e["families"].add(r["family"]); e["minds"].add(r["mind"])
                        if len(e["examples"]) < 3:
                            e["examples"].append(" ".join(ctx) + " | " + " ".join(seq))
                self.nodes[ctx][r["family"]].append(first); self.real.add(ctx)
            elif k == "inhibit" and o in ("yes", "no", "cant-tell"):
                self.inhibit[(tuple(r["context"]), r["candidate"])][r["family"]][o] += 1
            elif k == "triad" and o in ("mid", "two", "none"):
                t = tuple(sorted(r["shown"]))
                self.triads[t][tuple(r["answer"]) if o != "none" else ("none",)] += 1

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
        key = tuple(min(g, g[::-1]))
        if key not in found:
            found[key] = {"glyphs": g, "start": list(ctx), "stop_left": bstop, "stop_right": fstop,
                          "steps": fsteps + bsteps}
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
