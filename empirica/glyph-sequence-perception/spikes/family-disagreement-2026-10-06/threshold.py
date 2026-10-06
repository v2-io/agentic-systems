"""Is the Sonnet/Grok end-placement asymmetry a threshold difference? Determinacy of a context's continuation is
measured by minds OTHER than the two compared: the share of their answers that continue with the most common glyph.
Then, per determinacy bin, P(A stops) and P(B stops)."""
import collections, sys
import endplace as E

A, B = (sys.argv[1:3] if len(sys.argv) > 2 else ("sonnet55", "grok46"))
rows = E.table(A, B)
bins = collections.defaultdict(lambda: [0, 0, 0, 0])
for ctx, a, b, d in rows:
    others = [v for m, vs in d.items() if m not in (A, B) for v in vs]
    if len(others) < 2: continue
    cont = [v for v in others if not v.startswith("∅")]
    top = collections.Counter(cont).most_common(1)[0][1] if cont else 0
    det = top / len(others)
    k = min(int(det * 5), 4)
    bins[k][0] += a == "∅none"; bins[k][1] += b == "∅none"; bins[k][2] += 1
    bins[k][3] += (a == b)
print(f"determinacy (others' top-glyph share)  n   P({A} none)  P({B} none)  same modal")
for k in sorted(bins):
    sa, sb, n, ag = bins[k]
    print(f"  [{k/5:.1f},{(k+1)/5:.1f})  {n:6d}   {sa/n:.3f}      {sb/n:.3f}     {ag/n:.3f}")
