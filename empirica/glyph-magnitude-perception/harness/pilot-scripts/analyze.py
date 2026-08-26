#!/usr/bin/env python3
"""Defensible analysis of probe results.

Per sequence:
  - pair-level scoring (majority over samples; resamples are NOT independent trials)
  - Wilson 95% CI on pair-level accuracy
  - Bradley-Terry latent scale fit -> Kendall tau vs recorded order, min rung gap
  - logistic accuracy-vs-gap slope (discriminability)
Global: side-bias estimate, parse-failure rate, instinct-vs-think paired gap with
sign-test p, family-level pooled accuracies.
"""
import json, math, sys
from collections import defaultdict

rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip().startswith("{")]
MODE_MAIN = "instinct"

def wilson(k, n, z=1.96):
    if n == 0: return (float("nan"),) * 2
    p = k / n; d = 1 + z*z/n
    c = (p + z*z/(2*n)) / d; h = z * math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return c - h, c + h

# ---- pair-level majority table
pairs = defaultdict(lambda: defaultdict(list))  # (seq)(pairkey) -> per-mode votes
meta = {}
for r in rows:
    if r["ans"] is None: continue
    key = (r["a"], r["b"])
    pairs[r["seq"]][(key, r["mode"])].append((r["ans"], r["truth"], r["gap"]))
    meta[r["seq"]] = r["family"]

def pair_units(seq, mode):
    out = []
    for (key, m), votes in pairs[seq].items():
        if m != mode: continue
        n_corr = sum(a == t for a, t, _ in votes)
        maj = n_corr * 2 > len(votes)
        unanimous = len({a for a, _, _ in votes}) == 1
        out.append({"key": key, "maj": maj, "unan": unanimous, "gap": votes[0][2],
                    "truth": votes[0][1], "ans_maj": max(set(a for a,_,_ in votes),
                    key=[a for a,_,_ in votes].count)})
    return out

# ---- Bradley-Terry per sequence (on instinct majority answers)
def bt_fit(seq):
    # wins[i][j]: i judged more than j
    glyph_pos = {}
    units = pair_units(seq, MODE_MAIN)
    for u in units:
        for g in u["key"]: glyph_pos.setdefault(g, len(glyph_pos))
    n = len(glyph_pos)
    wins = [[0.0]*n for _ in range(n)]
    for u in units:
        a, b = u["key"]; ia, ib = glyph_pos[a], glyph_pos[b]
        if u["ans_maj"] == ">": wins[ia][ib] += 1
        else: wins[ib][ia] += 1
    # iterative BT with light smoothing
    for i in range(n):
        for j in range(n):
            if i != j: wins[i][j] += 0.1
    p = [1.0]*n
    for _ in range(200):
        newp = []
        for i in range(n):
            num = sum(wins[i][j] for j in range(n) if j != i)
            den = sum((wins[i][j]+wins[j][i])/(p[i]+p[j]) for j in range(n) if j != i)
            newp.append(num/den if den else p[i])
        s = sum(newp); p = [x*len(newp)/s for x in newp]
    return glyph_pos, p

def kendall_tau_vs_recorded(seq, seq_str_map):
    glyph_pos, p = bt_fit(seq)
    order = seq_str_map[seq]
    items = [(order.index(g), p[i]) for g, i in glyph_pos.items() if g in order]
    conc = disc = 0
    for x in range(len(items)):
        for y in range(x+1, len(items)):
            d = (items[x][0]-items[y][0]) * (items[x][1]-items[y][1])
            conc += d > 0; disc += d < 0
    tot = conc + disc
    return (conc - disc) / tot if tot else float("nan")

seq_strs = {}
for r in rows: pass
# reconstruct recorded orders from probe.py definitions
import re
src = open("probe.py").read()
for m in re.finditer(r'\("([-\w]+)",\s*"\w+",\s*"([^"]+)"\)', src):
    seq_strs[m.group(1)] = m.group(2)

def logistic_gap_slope(units):
    # crude MLE for P(correct)=sigmoid(a+b*gap) via grid; report b
    best, bestll = (0, 0), -1e18
    for a in [x/4 for x in range(-8, 17)]:
        for b in [x/4 for x in range(0, 13)]:
            ll = 0
            for u in units:
                z = a + b*u["gap"]; pr = 1/(1+math.exp(-z))
                pr = min(max(pr, 1e-6), 1-1e-6)
                ll += math.log(pr if u["maj"] else 1-pr)
            if ll > bestll: bestll, best = ll, (a, b)
    return best

print(f"{'sequence':<16}{'fam':<9}{'acc(maj)':>9}{'95%CI':>14}{'unan':>6}{'tau':>6}{'b(gap)':>7}")
famacc = defaultdict(lambda: [0, 0])
for seq in sorted(pairs, key=lambda s: meta[s]):
    units = pair_units(seq, MODE_MAIN)
    if not units: continue
    k = sum(u["maj"] for u in units); n = len(units)
    lo, hi = wilson(k, n)
    unan = sum(u["unan"] for u in units) / n
    tau = kendall_tau_vs_recorded(seq, seq_strs) if seq in seq_strs else float("nan")
    a, b = logistic_gap_slope(units)
    famacc[meta[seq]][0] += k; famacc[meta[seq]][1] += n
    print(f"{seq:<16}{meta[seq]:<9}{k}/{n:>2} {k/n:>4.0%} [{lo:.0%},{hi:.0%}]{unan:>6.0%}{tau:>6.2f}{b:>7.2f}")

print("\nFamily pooled (instinct, pair-majority, Wilson 95%):")
for fam, (k, n) in sorted(famacc.items(), key=lambda kv: -kv[1][0]/max(kv[1][1],1)):
    lo, hi = wilson(k, n)
    print(f"  {fam:<10} {k}/{n} = {k/n:.0%}  [{lo:.0%}, {hi:.0%}]")

# side bias + parse failures + mode gap
allv = [r for r in rows if r["mode"] == MODE_MAIN]
gt = sum(r["ans"] == ">" for r in allv if r["ans"])
n_ans = sum(1 for r in allv if r["ans"])
fails = sum(1 for r in rows if r["ans"] is None)
print(f"\nSide bias: P(>)={gt/n_ans:.0%} (n={n_ans}; 50% = unbiased since truth sides randomized)")
print(f"Parse failures: {fails}/{len(rows)} = {fails/len(rows):.1%}")

# paired instinct vs think at pair level, sign test
w = l = 0
for seq in pairs:
    ui = {u["key"]: u["maj"] for u in pair_units(seq, "instinct")}
    ut = {u["key"]: u["maj"] for u in pair_units(seq, "think")}
    for key in ui.keys() & ut.keys():
        if ut[key] and not ui[key]: w += 1
        elif ui[key] and not ut[key]: l += 1
m_ = w + l
if m_:
    from math import comb
    pval = sum(comb(m_, i) for i in range(w, m_+1)) / 2**m_
    print(f"Think beats instinct on {w} pairs, loses on {l} (sign test one-sided p={pval:.3f})")
