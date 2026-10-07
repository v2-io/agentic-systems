# Symmetric version of verifier 2's a15: for a target pair (A, B), runs both answered; the panel is every OTHER mind
# (neither A nor B); keep runs where the panel gave >= NP answers, all yes. Then A's and B's 'no' rate on the SAME runs.
# a15 conditions each mind on "everyone else", which for Grok includes Sonnet (the strictest on non-contiguous runs)
# and for Sonnet doesn't: an asymmetric filter.
import sys, collections
SP = "/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception/spikes/family-disagreement-2026-10-06"
sys.path.insert(0, SP)
import lib, abbott
from values import ckey
recs, _ = lib.load()
A = collections.defaultdict(lambda: collections.defaultdict(list)); cls = {}
for r in recs:
    t = r.get("tags") or {}
    if r["kind"] != "cohere" or t.get("control") or t.get("variant") not in (None, "plain") or r["outcome"] not in ("yes", "no"): continue
    q = ckey(r); A[q][r["mind"]].append(r["outcome"] == "yes"); cls[q] = abbott.setcls(r["context"])
M = abbott.MINDS
def rate(ys): return sum(1 - y for y in ys), len(ys)
for NP in (2, 3):
    print(f"\npanel >= {NP} answers, all yes; per pair, no-rate of each on the same runs (all their answers)")
    for a in M:
        for b in M:
            if a >= b: continue
            row = []
            for c in ("contig", "other"):
                na = nn_a = nb = nn_b = k = 0
                for q, d in A.items():
                    if cls[q] != c or a not in d or b not in d: continue
                    oth = [y for m2, ys in d.items() if m2 not in (a, b) for y in ys]
                    if len(oth) >= NP and all(oth):
                        x, n = rate(d[a]); na += x; nn_a += n
                        x, n = rate(d[b]); nb += x; nn_b += n; k += 1
                row.append(f"{c}: runs {k:4d} {a[:6]} {na}/{nn_a}={na/max(nn_a,1):.3f} {b[:6]} {nb}/{nn_b}={nb/max(nn_b,1):.3f}")
            if "sonnet55" in (a, b): print(f"{a:13s} {b:13s} " + " | ".join(row))
# a15 as written, and the same but with Sonnet removed from every 'other' panel
print("\na15 with Sonnet excluded from the panel (for minds other than Sonnet):")
for mm in M:
    out = []
    for c in ("contig", "other"):
        no = n = 0
        for q, d in A.items():
            if cls[q] != c or mm not in d: continue
            oth = [y for m2, ys in d.items() if m2 not in (mm, "sonnet55") for y in ys]
            if len(oth) >= 3 and all(oth): n += len(d[mm]); no += len(d[mm]) - sum(d[mm])
        out.append(f"{c}: no {no}/{n} = {no/max(n,1):.3f}")
    print(f"{mm:14s} " + " | ".join(out))
