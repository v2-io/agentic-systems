"""The behavioural chart test (whys-basis spike §2): at discriminator positions (unsealed `choose` answers only: lib
drops every sealed one), the share choosing the chart's candidate, per mind, real context against the neutral-context
control (CATALOG §12). Also paired: positions answered by both Claude (Sonnet) and Grok."""
import collections
import lib

recs, man = lib.load()
ch = [r for r in recs if r["kind"] == "choose" and r["outcome"] == "chose"
      and (r.get("tags") or {}).get("variant") in (None, "plain")]
def is_ctl(r): return (r.get("tags") or {}).get("control") == "neutral"
by = collections.defaultdict(lambda: [0, 0, 0, 0])   # mind -> [chart real, n real, chart ctl, n ctl]
for r in ch:
    b = by[r["mind"]]
    if is_ctl(r):
        b[2] += r["choice"] == r["chart"]; b[3] += 1
    else:
        b[0] += r["choice"] == r["chart"]; b[1] += 1
print("mind            P(chart | real context)   P(chart | neutral control)")
for m, (a, n, c, nc) in sorted(by.items()):
    print(f"  {m:14s} {a:4d}/{n:4d} = {a/max(n,1):.3f}        {c:4d}/{nc:4d} = {c/max(nc,1):.3f}")
# paired: same position (context + pair), Sonnet vs Grok vs Gemini Flash
pos = collections.defaultdict(lambda: collections.defaultdict(list))
for r in ch:
    if is_ctl(r): continue
    pos[(tuple(r["context"]), frozenset(r["candidates"]))][r["mind"]].append(r["choice"] == r["chart"])
for A, B in (("sonnet55", "grok46"), ("sonnet55", "gemini38flash"), ("grok46", "gemini38flash"), ("sonnet55", "haiku45nt"), ("haiku45nt", "grok46")):
    P = [(sum(d[A]) / len(d[A]), sum(d[B]) / len(d[B])) for d in pos.values() if d.get(A) and d.get(B)]
    if P:
        a = sum(x for x, _ in P) / len(P); b = sum(y for _, y in P) / len(P)
        both = sum(1 for x, y in P if x == y) / len(P)
        print(f"paired {A:13s} {B:13s} positions={len(P):4d}  P(chart) {a:.3f} vs {b:.3f}   same choice {both:.3f}")
