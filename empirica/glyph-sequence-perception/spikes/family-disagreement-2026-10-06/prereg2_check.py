#!/usr/bin/env python3
"""Score test round p002 against prereg-third-minds.json, by the reading fixed in that file: per mind, each model's
per-context log score over the mind's answered contexts; a model "wins" a mind when it beats each other model by more
than log(10); otherwise "not discriminating". Stop counts against each model's 95% Poisson-binomial band. Written
before any p002 answer was read. Answers other than a continuation or "none" are listed and left out."""
import collections, json, math, pathlib

HERE = pathlib.Path(__file__).resolve().parent
STUDY = HERE.parents[1]

def band(ps, lo=0.025, hi=0.975):
    dist = [1.0]
    for p in ps:
        nd = [0.0] * (len(dist) + 1)
        for k, v in enumerate(dist):
            nd[k] += v * (1 - p); nd[k + 1] += v * p
        dist = nd
    c, a, b = 0.0, None, None
    for k, v in enumerate(dist):
        c += v
        if a is None and c >= lo:
            a = k
        if b is None and c >= hi:
            b = k
    return a, b

def main():
    pre = json.load(open(HERE / "prereg-third-minds.json"))
    by = {tuple(c["context"]): c for c in pre["contexts"]}
    recs = [json.loads(l) for l in open(STUDY / "data" / "answers" / "p002.jsonl") if l.strip()]
    ans = collections.defaultdict(dict); other = []
    for r in recs:
        c = tuple(r["context"])
        if r["outcome"] in ("continuation", "none"):
            ans[r["mind"]][c] = 1 if r["outcome"] == "none" else 0
        else:
            other.append((r["mind"], "".join(c), r["outcome"], "".join((r.get("continuation") or [])[:6])))
    models = ["2mf", "irtu", "lnb"]
    for m in ("opus55", "haiku45nt", "haiku45"):
        a = ans.get(m, {})
        if not a:
            print(m, "no answers"); continue
        stops = sum(a.values())
        ls = {}
        print(f"{m}: {stops} stops of {len(a)} answered")
        for mo in models:
            ps = [by[c]["p_stop"][m][mo] for c in a]
            ls[mo] = sum(math.log(p if y else 1 - p) for c, y, p in zip(a, a.values(), ps))
            lo, hi = band(ps)
            print(f"   {mo:5} expected {sum(ps):5.1f} [95% {lo}-{hi}]  log score {ls[mo]:8.2f}")
        best = max(ls, key=ls.get)
        margin = min(ls[best] - ls[o] for o in models if o != best)
        print(f"   -> {best} wins (by {margin:.2f} nats over the next)" if margin > math.log(10)
              else f"   -> not discriminating (best {best}, by {margin:.2f} nats; a win needs > {math.log(10):.2f})")
    if other:
        print("left out:", other)

if __name__ == "__main__":
    main()
