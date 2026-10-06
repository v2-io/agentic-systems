"""Mind-by-mind agreement on identical questions, per kind. For each pair of minds, over the questions both answered
(plain prompt variant only, so a no-lookup re-ask isn't compared with its own tool attempt), the share of answer pairs
that agree, and Cohen's kappa. Also each mind's retest agreement with itself (the same question answered twice, in
different rounds or presentations): the noise floor."""
import collections, itertools, math, sys
import lib
from values import value, qkey

recs, man = lib.load()
by = collections.defaultdict(lambda: collections.defaultdict(list))   # (kind) -> q -> [(mind, value, round)]
fam = {}
for r in recs:
    if r["era"] == "seed": continue
    if (r.get("tags") or {}).get("variant") not in (None, "plain"): continue
    v = value(r)
    if v is None: continue
    q = qkey(r)
    if q is None: continue
    by[r["kind"]][q].append((r["mind"], v, r["round"]))
    fam[r["mind"]] = r["family"]

def kappa(pairs):
    n = len(pairs)
    if n == 0: return float("nan"), float("nan")
    po = sum(a == b for a, b in pairs) / n
    ca = collections.Counter(a for a, _ in pairs); cb = collections.Counter(b for _, b in pairs)
    pe = sum(ca[x] * cb[x] for x in ca) / n / n
    return po, (po - pe) / (1 - pe) if pe < 1 else float("nan")

MINDS = ["sonnet55", "opus55", "haiku45nt", "haiku45", "grok46", "gemini38flash", "gemini31pro"]
kinds = sys.argv[1:] or ["cohere", "inhibit", "continue", "triad", "order", "choose", "names", "next", "pick"]
for kind in kinds:
    qs = by[kind]
    print(f"\n=== {kind}  (questions {len(qs)})")
    # retest
    rt = {}
    for m in set(fam):
        pairs = []
        for q, L in qs.items():
            vs = [v for mm, v, _ in L if mm == m]
            if len(vs) >= 2:
                pairs.append((vs[0], vs[1]))
        if len(pairs) >= 20:
            rt[m] = (len(pairs),) + kappa(pairs)
    for m, (n, po, k) in sorted(rt.items()):
        print(f"  retest {m:16s} n={n:5d} agree={po:.3f} kappa={k:.3f}")
    ms = [m for m in MINDS + sorted(set(fam) - set(MINDS)) if any(m == mm for L in qs.values() for mm, _, _ in L)]
    for a, b in itertools.combinations(ms, 2):
        pairs = []
        for q, L in qs.items():
            va = [v for mm, v, _ in L if mm == a]; vb = [v for mm, v, _ in L if mm == b]
            if va and vb:
                pairs.append((va[0], vb[0]))
        if len(pairs) >= 20:
            po, k = kappa(pairs)
            tag = "same-fam" if fam[a] == fam[b] else "cross"
            print(f"  {a:14s} {b:14s} {tag:8s} n={len(pairs):5d} agree={po:.3f} kappa={k:.3f}")
