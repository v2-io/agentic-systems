"""Pilot llama3.2:3b triad run (probe5): orientation-set structure, slot preference, cycle rate."""
import json, collections, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
R = [json.loads(l) for l in open(os.path.join(ROOT, "pilot/results5-llama3.2_3b.jsonl"))]
d = [r for r in R if r["more"] in (r["a"], r["b"])]
p = sum(r["more"] == r["a"] for r in d) / len(d)
g = collections.defaultdict(list)
for r in R: g[(r["chunk"], r["triad"])].append(r)
fo = cyc = cyclic = 0
for v in g.values():
    A = collections.Counter(x["a"] for x in v); B = collections.Counter(x["b"] for x in v)
    cyclic += len(v) == 3 and set(A) == set(B) and max(A.values()) == 1
    if len(v) == 3 and all(x["more"] in (x["a"], x["b"]) for x in v):
        fo += 1; cyc += max(collections.Counter(x["more"] for x in v).values()) == 1
print(f"sets {len(g)} cyclic {cyclic}; P(first|dir) {p:.3f}; fully oriented {fo}, cycles {cyc} = {cyc/fo:.3f}; pure-slot prediction {p**3+(1-p)**3:.3f}")
