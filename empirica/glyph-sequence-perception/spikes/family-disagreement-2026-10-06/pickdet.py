"""Out-of-family test of 'content agrees, commitment differs': forced picks (no option to decline), split by how
determined the same context is in FIRST-IMPRESSION continue answers (all minds; share naming the top glyph; contexts
with >= 3 continue answers). Per bin, the noise-free distance D between generator minds, within Claude and across."""
import collections, itertools
import lib, distance as DS
from values import value

recs, man = lib.load()
cont = collections.defaultdict(list)
for r in recs:
    if r["kind"] == "continue" and (r.get("tags") or {}).get("variant") in (None, "plain"):
        v = value(r)
        if v is not None: cont[tuple(r["context"])].append(v)
det = {}
for c, vs in cont.items():
    if len(vs) >= 3:
        g = [v for v in vs if not v.startswith("∅")]
        det[c] = (collections.Counter(g).most_common(1)[0][1] / len(vs)) if g else 0.0
by = DS.prepare({"pick"})
by = {q: d for q, d in by.items() if not q[2] and q[1] in det}
bins = {"low (<0.5)": lambda x: x < 0.5, "mid [0.5,0.8)": lambda x: 0.5 <= x < 0.8, "high (>=0.8)": lambda x: x >= 0.8}
for name, f in bins.items():
    sub = {q: d for q, d in by.items() if f(det[q[1]])}
    print(f"== first-impression determinacy {name}: contexts {len(sub)}")
    for a, b in (("sonnet55g", "haiku45g"), ("sonnet55g", "grok46g"), ("haiku45g", "grok46g"), ("sonnet55g", "gemini38flashg"), ("grok46g", "gemini38flashg")):
        s = DS.distance(sub, a, b)
        if s: print(f"   {a:15s}{b:15s} n={s['n']:4d}  w_a={s['wa']:.2f} w_b={s['wb']:.2f} cross={s['C']:.2f}  D={s['D']:.3f}±{s['se']:.3f}")
