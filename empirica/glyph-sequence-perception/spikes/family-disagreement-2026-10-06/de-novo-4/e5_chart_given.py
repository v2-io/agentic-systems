# FINDINGS §7 "the larger Claude minds walk the chart more": is it the CHART (contiguous runs with no given order) or
# contiguous runs in general (alphabets and numbers, which are given walks)? Paired, model-free: for each pair of minds,
# contexts both answered (first plain continue answer each), stop rates by class:
#   cg = contiguous in code points AND a given walk (catalog/given_walk.py, min_len 2)
#   cn = contiguous, not a given walk (a pure chart walk, as far as the givens know)
#   mono = monotone not contiguous;  oth = other
import sys, collections, math
SP = "/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception/spikes/family-disagreement-2026-10-06"
ROOT = "/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception"
sys.path.insert(0, SP); sys.path.insert(0, ROOT + "/catalog")
import lib, features as F, given_walk as GW
from values import ckey
recs, _ = lib.load()
first = collections.defaultdict(dict)
order = sorted((r for r in recs if r["kind"] == "continue" and (r.get("tags") or {}).get("variant") in (None, "plain")
                and r["outcome"] in ("none", "continuation")), key=lambda r: (int(r["round"][1:]) if r["round"][1:].isdigit() else -1))
for r in order:
    first[ckey(r)].setdefault(r["mind"], r["outcome"] == "none")
cls = {}
for q in first:
    g = list(q[1]); cc = F.chart_class(g)
    if cc == "contiguous":
        cls[q] = "cg" if GW.is_given(GW.classify_cached(tuple(g), 2)) else "cn"
    else:
        cls[q] = {"monotone": "mono", "other": "oth"}[cc]
print("contexts by class:", collections.Counter(cls.values()))
def lg(k, n): return math.log((k + .5) / (n - k + .5))
pairs = [("sonnet55", "grok46"), ("opus55", "grok46"), ("sonnet55", "gemini38flash"), ("opus55", "gemini38flash"),
         ("sonnet55", "haiku45nt"), ("haiku45nt", "grok46"), ("grok46", "gemini38flash"), ("sonnet55", "opus55"), ("haiku45", "grok46")]
for a, b in pairs:
    t = {c: [0, 0, 0] for c in ("cg", "cn", "mono", "oth")}
    for q, d in first.items():
        if a in d and b in d:
            x = t[cls[q]]; x[0] += 1; x[1] += d[a]; x[2] += d[b]
    s = " | ".join(f"{c} n={n:5d} {a[:5]} {sa/max(n,1):.3f} {b[:5]} {sb/max(n,1):.3f}" for c, (n, sa, sb) in t.items())
    # difference in differences on the logit scale: (b - a) on cn minus (b - a) on cg, and on cn minus oth
    def dd(c1, c2):
        n1, a1, b1 = t[c1]; n2, a2, b2 = t[c2]
        return (lg(b1, n1) - lg(a1, n1)) - (lg(b2, n2) - lg(a2, n2))
    print(f"{a:13s} vs {b:13s} {s}\n      logit gap ({b[:5]} minus {a[:5]}) cn {lg(t['cn'][2], t['cn'][0]) - lg(t['cn'][1], t['cn'][0]):+.2f}, cg {lg(t['cg'][2], t['cg'][0]) - lg(t['cg'][1], t['cg'][0]):+.2f}, mono {lg(t['mono'][2], t['mono'][0]) - lg(t['mono'][1], t['mono'][0]):+.2f}, oth {lg(t['oth'][2], t['oth'][0]) - lg(t['oth'][1], t['oth'][0]):+.2f}")
