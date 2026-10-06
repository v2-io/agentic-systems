"""Is commitment (continue vs stop) a per-mind threshold only, or do particular contexts carry family-specific
commitment? Model: logit P(stop | mind m, context i) = alpha_m + beta_i. alpha_m is fitted on all contexts (by
alternating Newton steps); for the test, beta_i of each test context is re-estimated from the answers of minds OTHER
than the two compared (A, B), so the prediction for A and B is out of sample. Then over contexts where A and B each
answered at least twice: observed vs predicted counts of 'flat' commit splits (A continues every time, B stops every
time, and the reverse), with a parametric bootstrap of the predicted count."""
import collections, math, random, sys
import lib
from values import value, ckey

def sig(x): return 1 / (1 + math.exp(-x))
recs, man = lib.load()
ans = collections.defaultdict(lambda: collections.defaultdict(list))   # context -> mind -> [stop 0/1]
for r in recs:
    if r["kind"] != "continue": continue
    t = r.get("tags") or {}
    if t.get("variant") not in (None, "plain"): continue
    v = value(r)
    if v is None or (v.startswith("∅") and v != "∅none"): continue
    ans[ckey(r)][r["mind"]].append(1 if v == "∅none" else 0)
minds = sorted({m for d in ans.values() for m in d})
alpha = {m: 0.0 for m in minds}
items = [q for q, d in ans.items() if sum(len(v) for v in d.values()) >= 2]
beta = {q: 0.0 for q in items}
def fit_beta(d, alpha, excl=()):
    b = 0.0
    obs = [(alpha[m], y) for m, ys in d.items() if m not in excl for y in ys]
    if not obs: return None
    for _ in range(25):
        g = sum(y - sig(a + b) for a, y in obs); h = sum(sig(a + b) * (1 - sig(a + b)) for a, _ in obs) + 0.25
        b += (g - 0.25 * b) / h        # a weak N(0, 4) prior keeps all-stop / all-continue items finite
    return b
for it in range(8):
    for q in items: beta[q] = fit_beta(ans[q], alpha)
    for m in minds:
        obs = [(beta[q], y) for q in items for y in ans[q].get(m, [])]
        a = alpha[m]
        for _ in range(10):
            g = sum(y - sig(a + b) for b, y in obs); h = sum(sig(a + b) * (1 - sig(a + b)) for b, _ in obs) + 1e-9
            a += g / h
        alpha[m] = a
    shift = alpha["sonnet55"]; alpha = {m: v - shift for m, v in alpha.items()}
print("alpha (logit of stopping, relative to sonnet55):", {m: round(v, 2) for m, v in sorted(alpha.items(), key=lambda x: x[1])})
rng = random.Random(0)
for A, B in (("sonnet55", "grok46"), ("sonnet55", "haiku45nt"), ("haiku45nt", "grok46")):
    obs_ab = obs_ba = 0; preds = []
    for q in items:
        d = ans[q]
        if len(d.get(A, [])) >= 2 and len(d.get(B, [])) >= 2:
            b = fit_beta(d, alpha, excl=(A, B))
            if b is None: continue
            pa, pb = sig(alpha[A] + b), sig(alpha[B] + b)
            preds.append((len(d[A]), len(d[B]), pa, pb))
            obs_ab += all(y == 0 for y in d[A]) and all(y == 1 for y in d[B])
            obs_ba += all(y == 1 for y in d[A]) and all(y == 0 for y in d[B])
    e_ab = sum((1 - pa) ** na * pb ** nb for na, nb, pa, pb in preds)
    e_ba = sum(pa ** na * (1 - pb) ** nb for na, nb, pa, pb in preds)
    sims = []
    for _ in range(500):
        c1 = c2 = 0
        for na, nb, pa, pb in preds:
            ya = [rng.random() < pa for _ in range(na)]; yb = [rng.random() < pb for _ in range(nb)]
            c1 += (not any(ya)) and all(yb); c2 += all(ya) and not any(yb)
        sims.append((c1, c2))
    s1 = sorted(x for x, _ in sims); s2 = sorted(y for _, y in sims)
    print(f"{A} vs {B}: contexts {len(preds)}  {A} continues/{B} stops: observed {obs_ab}, predicted {e_ab:.1f} (95% {s1[12]}-{s1[487]})"
          f";  reverse: observed {obs_ba}, predicted {e_ba:.1f} (95% {s2[12]}-{s2[487]})")
