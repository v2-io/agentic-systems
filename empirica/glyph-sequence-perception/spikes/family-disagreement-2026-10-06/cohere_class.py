"""Whole-run recognition (cohere) by class of run, per pair of minds, on runs both answered. Each mind's yes share on
real runs is Abbott-corrected by its own shuffled-control rate for the run's set class (contiguous / other), so a mind
that says yes more to everything is not counted as recognising more. Difference A - B per class, bootstrap SE over
runs (seed 0). Real runs: cohere answers with no control tag; controls: tag 'shuffled'."""
import collections, random, sys
import lib, features as F
from values import canon_run

recs, man = lib.load()
co = [r for r in recs if r["kind"] == "cohere" and r["outcome"] in ("yes", "no", "cant-tell")
      and (r.get("tags") or {}).get("variant") in (None, "plain")]
def setcls(g):
    o = sorted(ord(x) for x in g)
    return "contiguous" if all(b - a == 1 for a, b in zip(o, o[1:])) else "other"
ctl = collections.defaultdict(lambda: [0, 0])
real = collections.defaultdict(lambda: collections.defaultdict(list))
for r in co:
    g = tuple(r["context"]); c = (r.get("tags") or {}).get("control")
    y = r["outcome"] == "yes"
    if c == "shuffled":
        k = ctl[(r["mind"], setcls(g))]; k[0] += y; k[1] += 1
    elif c is None:
        real[canon_run(g)][r["mind"]].append(y)
crate = {k: (v[0] + 0.5) / (v[1] + 1) for k, v in ctl.items()}
FEAT = {g: F.feats(g) for g in real}

def abbott(p, c): return (p - c) / (1 - c)

def compare(A, B, feat):
    cells = collections.defaultdict(list)
    for g, d in real.items():
        if d.get(A) and d.get(B):
            sc = setcls(g)
            ea = abbott(sum(d[A]) / len(d[A]), crate[(A, sc)]); eb = abbott(sum(d[B]) / len(d[B]), crate[(B, sc)])
            cells[FEAT[g][feat] if feat else "all"].append((ea, eb))
    out = {}
    rng = random.Random(0)
    for k, L in cells.items():
        if len(L) < 25: continue
        m = lambda S: sum(a - b for a, b in S) / len(S)
        diff = m(L); bs = sorted(m([L[rng.randrange(len(L))] for _ in L]) for _ in range(300))
        se = (sum((x - diff) ** 2 for x in bs) / 300) ** 0.5
        out[k] = (len(L), sum(a for a, _ in L) / len(L), sum(b for _, b in L) / len(L), diff, se)
    return out

if __name__ == "__main__":
    print("control rates:", {k: round(v, 3) for k, v in sorted(crate.items()) if k[0] in ("sonnet55", "grok46", "gemini38flash", "haiku45nt", "opus55")})
    pairs = [("sonnet55", "grok46"), ("sonnet55", "gemini38flash"), ("grok46", "gemini38flash"), ("sonnet55", "haiku45nt"), ("haiku45nt", "grok46"), ("sonnet55", "opus55")]
    for feat in [None] + (sys.argv[1:] or ["chart", "group", "cat", "blocks", "familiar"]):
        print(f"\n== by {feat or 'all'}  (excess yes, Abbott; A - B)")
        for A, B in pairs:
            for k, (n, ea, eb, d, se) in sorted(compare(A, B, feat).items()):
                flag = " *" if abs(d) > 2.5 * se else ""
                print(f"  {A:9s}-{B:13s} {k:22s} n={n:5d}  {ea:+.3f} {eb:+.3f}  diff={d:+.3f}±{se:.3f}{flag}")
