"""Single-answer form of the additive-threshold test. Over items answered by A and B (first answer each) and by at
least one other mind: observed disagreement vs disagreement predicted by logit P = alpha_m + beta_i, beta_i from the
other minds only. The ratio observed/predicted is read RELATIVE to same-family pairs (noisy beta biases the prediction
for every pair alike); an excess for cross-family pairs over same-family pairs would be family-specific interaction."""
import collections, math, sys
import additive as AD, lib
from values import ckey

def run(name, pairs):
    recs, man = lib.load()
    ans = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in recs:
        x = AD.outcome(r)
        if not x or x[0] != name or x[1] is None: continue
        ans[ckey(r)][r["mind"]].append(x[1])
    minds = sorted({m for d in ans.values() for m in d}); items = list(ans)
    alpha = {m: 0.0 for m in minds}
    sig = AD.sig
    def fit_beta(d, excl=()):
        obs = [(alpha[m], y) for m, ys in d.items() if m not in excl for y in ys]
        if not obs: return None
        b = 0.0
        for _ in range(25):
            g = sum(y - sig(a + b) for a, y in obs); h = sum(sig(a + b) * (1 - sig(a + b)) for a, _ in obs) + 0.25
            b += (g - 0.25 * b) / h
        return b
    beta = {}
    for _ in range(6):
        for q in items: beta[q] = fit_beta(ans[q])
        for m in minds:
            obs = [(beta[q], y) for q in items for y in ans[q].get(m, [])]
            a = alpha[m]
            for _ in range(10):
                g = sum(y - sig(a + b) for b, y in obs); h = sum(sig(a + b) * (1 - sig(a + b)) for b, _ in obs) + 1e-9
                a += g / h
            alpha[m] = a
    print(f"\n== {name}")
    for A, B in pairs:
        n = od = pd = 0.0
        for q in items:
            d = ans[q]
            if A in d and B in d and any(m not in (A, B) for m in d):
                b = fit_beta(d, excl=(A, B)); pa, pb = sig(alpha[A] + b), sig(alpha[B] + b)
                n += 1; od += d[A][0] != d[B][0]; pd += pa * (1 - pb) + pb * (1 - pa)
        if n >= 50:
            fam = "same" if AD_fam(A) == AD_fam(B) else "cross"
            print(f"  {A:13s} {B:14s} {fam:5s} n={int(n):5d} observed {od/n:.3f}  predicted {pd/n:.3f}  ratio {od/pd:.2f}")

def AD_fam(m): return "claude" if m.startswith(("sonnet", "opus", "haiku")) else ("grok" if m.startswith("grok") else "gemini")
if __name__ == "__main__":
    for name in sys.argv[1:] or ["continue-stop", "triad-commit", "cohere-yes", "inhibit-yes"]:
        run(name, AD.P + [("opus55", "grok46"), ("opus55", "gemini38flash"), ("haiku45", "haiku45nt")])
