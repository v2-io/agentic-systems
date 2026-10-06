"""The additive-threshold test (rasch.py), generalised to any binary decision:
  continue-stop   continue answers: "none" (1) vs a glyph (0)
  triad-commit    triads: a middle named (1) vs two / none / tie (0)
  cohere-yes      cohere, real runs only (no control tag): yes (1) vs no (0); can't-tell dropped
  inhibit-yes     inhibit, real candidates only (no control tag): yes vs no
logit P(1 | m, i) = alpha_m + beta_i; beta_i of a test item from minds other than the pair compared; observed vs
predicted flat splits (each of A's answers 0 and each of B's 1, and the reverse), NMIN answers each."""
import collections, math, random, sys
import lib
from values import value, ckey

def sig(x): return 1 / (1 + math.exp(-x))
def outcome(r):
    k, o = r["kind"], r["outcome"]; t = r.get("tags") or {}
    if t.get("variant") not in (None, "plain"): return None
    if k == "continue":
        return ("continue-stop", 1 if o == "none" else (0 if o == "continuation" else None))
    if k == "triad":
        return ("triad-commit", 1 if o == "mid" else (0 if o in ("two", "none", "tie2", "tie3") else None))
    if k in ("cohere", "inhibit") and not t.get("control"):
        return (k + "-yes", 1 if o == "yes" else (0 if o == "no" else None))
    return None

def run(name, pairs, NMIN=2, seed=0):
    recs, man = lib.load()
    ans = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in recs:
        x = outcome(r)
        if not x or x[0] != name or x[1] is None: continue
        ans[ckey(r)][r["mind"]].append(x[1])
    minds = sorted({m for d in ans.values() for m in d})
    items = [q for q, d in ans.items() if sum(len(v) for v in d.values()) >= 2]
    alpha = {m: 0.0 for m in minds}; beta = {}
    def fit_beta(d, excl=()):
        obs = [(alpha[m], y) for m, ys in d.items() if m not in excl for y in ys]
        if not obs: return None
        b = 0.0
        for _ in range(25):
            g = sum(y - sig(a + b) for a, y in obs); h = sum(sig(a + b) * (1 - sig(a + b)) for a, _ in obs) + 0.25
            b += (g - 0.25 * b) / h
        return b
    for _ in range(8):
        for q in items: beta[q] = fit_beta(ans[q])
        for m in minds:
            obs = [(beta[q], y) for q in items for y in ans[q].get(m, [])]
            if not obs: continue
            a = alpha[m]
            for _ in range(10):
                g = sum(y - sig(a + b) for b, y in obs); h = sum(sig(a + b) * (1 - sig(a + b)) for b, _ in obs) + 1e-9
                a += g / h
            alpha[m] = a
        s = alpha.get("sonnet55", 0); alpha = {m: v - s for m, v in alpha.items()}
    print(f"\n== {name}: items {len(items)}; alpha rel. sonnet55:",
          {m: round(v, 2) for m, v in sorted(alpha.items(), key=lambda x: x[1]) if m in ("sonnet55", "opus55", "haiku45", "haiku45nt", "grok46", "gemini38flash", "gemini31pro")})
    rng = random.Random(seed)
    for A, B in pairs:
        preds = []; o1 = o2 = 0
        for q in items:
            d = ans[q]
            if len(d.get(A, [])) >= NMIN and len(d.get(B, [])) >= NMIN:
                b = fit_beta(d, excl=(A, B))
                if b is None: continue
                preds.append((len(d[A]), len(d[B]), sig(alpha[A] + b), sig(alpha[B] + b)))
                o1 += (not any(d[A])) and all(d[B]); o2 += all(d[A]) and not any(d[B])
        if len(preds) < 20: continue
        e1 = sum((1 - pa) ** na * pb ** nb for na, nb, pa, pb in preds); e2 = sum(pa ** na * (1 - pb) ** nb for na, nb, pa, pb in preds)
        sims = []
        for _ in range(400):
            c1 = c2 = 0
            for na, nb, pa, pb in preds:
                ya = [rng.random() < pa for _ in range(na)]; yb = [rng.random() < pb for _ in range(nb)]
                c1 += (not any(ya)) and all(yb); c2 += all(ya) and not any(yb)
            sims.append((c1, c2))
        s1 = sorted(x for x, _ in sims); s2 = sorted(y for _, y in sims)
        print(f"  {A:13s}{B:14s} items {len(preds):5d} | A=0,B=1: obs {o1:4d} pred {e1:6.1f} [{s1[10]}-{s1[389]}] | A=1,B=0: obs {o2:4d} pred {e2:6.1f} [{s2[10]}-{s2[389]}]")

P = [("sonnet55", "grok46"), ("sonnet55", "gemini38flash"), ("grok46", "gemini38flash"), ("gemini38flash", "gemini31pro"),
     ("sonnet55", "opus55"), ("sonnet55", "haiku45"), ("haiku45", "grok46"), ("grok46", "gemini31pro"), ("sonnet55", "haiku45nt"), ("haiku45nt", "grok46")]
if __name__ == "__main__":
    for name in sys.argv[1:] or ["triad-commit", "cohere-yes", "inhibit-yes"]:
        run(name, P)
