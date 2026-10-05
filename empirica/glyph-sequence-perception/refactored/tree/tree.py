#!/usr/bin/env python3
"""Concern 2: the context tree, and the sequences read off it (METHODOLOGY §2-3). Built from canonical answer records
only; it never reads `source` (why a question was asked).

  tree.py                -> ../data/tree/SEQUENCES.md, ../data/tree/sequences.json, ../data/tree/nodes.json

NODES are contexts exactly as a mind was shown them (oriented runs). A node holds, per family, the answers given at
it: continuations with their rank, "none" (an end), and non-glyph content. Answers given at a longer context are NOT
pooled into its suffixes: pooling would mix in whichever longer contexts happened to be asked, and k* (the shortest
sufficient context) needs answers asked at each length. Through the triad era few suffixes were asked exactly, so
k* is mostly still unknown, and it is shown as such.

AGREEMENT at a node, for a continuation x: per family, the share of that family's answers that name x first; then
the mean over the families that answered. A soft quantity: it orders and is shown; nothing is cut by it.

SEQUENCES are paths read off the tree. From every node, take its most-agreed first continuation x (any agreement > 0;
ties broken by families naming it, then answers, then codepoint) and walk: at each step, look up the longest suffix
(>= 2 glyphs, <= 8) of the path so far that was asked exactly, and take its most-agreed continuation. The walk stops
at an END (that node's most common answer is "none"), at an OPEN end (no suffix of the path was ever asked: the
planner's work), or where the continuation is already in the path (a WRAP: shown, never declared a cycle, since a
cycle needs a manifested repeat, which the triad era never asked for). Each path is walked in both directions (the
reverse is the same sequence), and a path contained in a longer one in the same order is that one at an earlier
stage, shown once.

Per position the walk records which node carried the step (its context length), the agreement, the families naming
it, and the runner-up continuation there: a branch candidate. Triads and order answers are not used to build paths;
each sequence shows how many triad answers on its consecutive triples agree with its order and how many don't.
"""
import collections, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[1]                     # refactored/
ANS = ROOT / "data" / "answers"
OUT = ROOT / "data" / "tree"
MAXK = 8

def load():
    recs = []
    for f in sorted(ANS.glob("*.jsonl")):
        recs += [json.loads(l) for l in open(f) if l.strip()]
    return recs

class Tree:
    def __init__(self, recs):
        self.nodes = collections.defaultdict(lambda: collections.defaultdict(list))   # ctx -> family -> answers
        self.triads = collections.defaultdict(collections.Counter)                     # sorted triple -> outcome
        for r in recs:
            if r["kind"] in ("next", "continue") and r["outcome"] in ("proposals", "continuation", "none"):
                ctx = tuple(r["context"])
                if r["outcome"] == "none":
                    first, props = "<none>", []
                else:
                    props = [p["g"] for p in sorted(r.get("proposals", []), key=lambda p: p["rank"])]
                    first = props[0] if props else ("<other>" if r.get("other_content") else "<none>")
                self.nodes[ctx][r["family"]].append({"first": first, "props": props, "mind": r["mind"]})
            elif r["kind"] == "triad" and r["outcome"] in ("mid", "two", "none"):
                t = tuple(sorted(r["shown"]))
                self.triads[t][tuple(r["answer"]) if r["outcome"] != "none" else ("none",)] += 1

    def dist(self, ctx):
        """-> {x: (agreement, families naming x first, answers naming x first)} at an exactly-asked context."""
        fam = self.nodes.get(ctx)
        if not fam:
            return {}
        per = collections.defaultdict(dict); cnt = collections.Counter(); fams = collections.defaultdict(set)
        for f, ans in fam.items():
            c = collections.Counter(a["first"] for a in ans)
            for x, n in c.items():
                per[x][f] = n / len(ans); cnt[x] += n; fams[x].add(f)
        nf = len(fam)
        return {x: (sum(per[x].values()) / nf, len(fams[x]), cnt[x]) for x in per}

    def best(self, ctx):
        d = self.dist(ctx)
        if not d:
            return None
        ranked = sorted(d.items(), key=lambda kv: (-kv[1][0], -kv[1][1], -kv[1][2], kv[0]))
        return ranked

    def lookup(self, run):
        """longest suffix of run (2..MAXK) asked exactly."""
        for j in range(min(MAXK, len(run)), 1, -1):
            if tuple(run[-j:]) in self.nodes:
                return tuple(run[-j:])
        return None

    def walk(self, path):
        """extend `path` forward; -> (path, steps, stop)."""
        path = list(path); steps = []
        while len(path) < 64:
            ctx = self.lookup(path)
            if ctx is None:
                return path, steps, "open"
            ranked = self.best(ctx)
            x, (agr, nfam, n) = ranked[0]
            alt = next(((y, v) for y, v in ranked[1:] if y not in ("<none>", "<other>")), None)
            if x == "<none>":
                return path, steps, "end"
            if x == "<other>":
                return path, steps, "other"
            if x in path:
                steps.append({"ctx": "".join(ctx), "k": len(ctx), "x": x, "agreement": agr, "families": nfam, "answers": n,
                              "alt": alt and [alt[0], alt[1][0]]})
                return path, steps, "wrap→" + x
            steps.append({"ctx": "".join(ctx), "k": len(ctx), "x": x, "agreement": agr, "families": nfam, "answers": n,
                          "alt": alt and [alt[0], alt[1][0]]})
            path.append(x)
        return path, steps, "cap"

    def triad_check(self, g):
        agree = against = 0
        for a, m, b in zip(g, g[1:], g[2:]):
            c = self.triads.get(tuple(sorted((a, m, b))), {})
            for out, n in c.items():
                if out[0] == "mid":
                    agree += n if out[1] == m else 0
                    against += n if out[1] != m else 0
                else:
                    against += n
        return agree, against

def sequences(T):
    found = {}
    for ctx in T.nodes:
        ranked = T.best(ctx)
        if not ranked or ranked[0][0] in ("<none>", "<other>") or ranked[0][0] in ctx:
            continue
        fwd, fsteps, fstop = T.walk(list(ctx))
        bwd, bsteps, bstop = T.walk(fwd[::-1])
        g = bwd[::-1]
        key = tuple(min(g, g[::-1]))
        if key in found:
            continue
        # steps along g, in g's order: backward steps added glyphs at g's start (reversed), forward ones at its end.
        # The context's own glyphs were shown, not walked.
        found[key] = {"glyphs": g, "start_ctx": "".join(ctx), "stop_left": bstop, "stop_right": fstop,
                      "steps_right": fsteps, "steps_left": bsteps}
    seqs = list(found.values())
    # an earlier stage: contained in a longer one, same order (either direction)
    def contained(a, b):
        n = len(a)
        return n < len(b) and any(b[i:i + n] in (a, a[::-1]) for i in range(len(b) - n + 1))
    seqs.sort(key=lambda s: -len(s["glyphs"]))
    kept = []
    for s in seqs:
        if not any(contained(s["glyphs"], k["glyphs"]) for k in kept):
            kept.append(s)
    for s in kept:
        walked = s["steps_right"] + s["steps_left"]
        s["walked"] = len(walked)
        s["agreement"] = min((w["agreement"] for w in walked), default=0.0)
        s["mean_agreement"] = sum(w["agreement"] for w in walked) / len(walked) if walked else 0.0
        s["families_min"] = min((w["families"] for w in walked), default=0)
        s["k_used"] = sorted({w["k"] for w in walked})
        s["branches"] = [f"{w['ctx']}→{w['alt'][0]} ({w['alt'][1]:.2f})" for w in walked if w["alt"] and w["alt"][1] >= 0.25]
        s["triads"] = T.triad_check(s["glyphs"])
    kept.sort(key=lambda s: (-s["mean_agreement"] * min(1.0, s["walked"] / 4), -len(s["glyphs"]), s["glyphs"]))
    return kept

def main():
    recs = load()
    T = Tree(recs)
    seqs = sequences(T)
    OUT.mkdir(parents=True, exist_ok=True)
    json.dump(seqs, open(OUT / "sequences.json", "w"), ensure_ascii=False)
    nodes = {"".join(c): {f: [a["first"] for a in v] for f, v in fam.items()} for c, fam in T.nodes.items()}
    json.dump(nodes, open(OUT / "nodes.json", "w"), ensure_ascii=False)
    fams = sorted({f for fam in T.nodes.values() for f in fam})
    stops = collections.Counter()
    for s in seqs:
        stops[s["stop_left"].split("→")[0]] += 1; stops[s["stop_right"].split("→")[0]] += 1
    L = ["# Sequences read off the context tree", "",
         f"*Generated by `refactored/tree/tree.py` from the canonical answer records in `refactored/data/answers/` (the triad era, ported; see its PORT-REPORT). Built from what-comes-next answers only, at the contexts exactly as asked; triads and order sets are a check column. {len(T.nodes)} asked contexts; {len(seqs)} sequences.*", "",
         "**How to read a row.** The sequence is a path through the tree. Starting from an asked context, each step takes the continuation most agreed on at the longest stretch of the path so far that the minds were actually shown. Each step is walked in both directions.",
         "- **walked:** steps taken by the walk; the starting context's glyphs were shown, not walked.",
         "- **agreement:** per family, the share of its answers naming that continuation first, averaged over the families that answered. *min* is the weakest walked step and *mean* the average.",
         "- **k used:** the context lengths that carried the steps. These are lengths that happened to be asked in the triad era, *not yet k\\*.* Shorter suffixes were almost never asked.",
         "- **ends:** what stopped each walk:",
         "  - *end*: the minds answered \"none\" there;",
         "  - *open*: no stretch of the path was ever asked, so this is the planner's work;",
         "  - *wrap→x*: the continuation is already in the path. A wrap is not a cycle until a mind manifests the repeat;",
         "  - *other*: the answer was not a single glyph, e.g. \"10\".",
         "- **branches:** runner-up continuations with agreement ≥ 0.25 at a step: `context→alternative (agreement)`.",
         "- **triads:** triad answers on the path's consecutive triples, agreeing with its order : not.", "",
         f"Walk stops over all ends: " + ", ".join(f"{k} {v}" for k, v in stops.most_common()) + ".", "",
         "| # | sequence | n | walked | agreement min / mean | k used | ends (left / right) | branches | triads |",
         "|---|---|---|---|---|---|---|---|---|"]
    for i, s in enumerate(seqs[:400], 1):
        L.append(f"| {i} | `{' '.join(s['glyphs'])}` | {len(s['glyphs'])} | {s['walked']} | {s['agreement']:.2f} / {s['mean_agreement']:.2f} | "
                 f"{','.join(map(str, s['k_used']))} | {s['stop_left']} / {s['stop_right']} | {';<br>'.join(s['branches'][:4])} | {s['triads'][0]}:{s['triads'][1]} |")
    (OUT / "SEQUENCES.md").write_text("\n".join(L) + "\n")
    print("\n".join(L[:16 + 1]))
    print(f"{len(seqs)} sequences; lengths:", sorted(collections.Counter(len(s['glyphs']) for s in seqs).items()))

if __name__ == "__main__":
    main()
