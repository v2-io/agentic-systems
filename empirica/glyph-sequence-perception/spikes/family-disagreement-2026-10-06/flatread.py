"""What the calibrated model (irt.py, variant given) says about flat-split items. For each flat split between A and B
(each >= 2 answers, unanimous, opposite): the posterior over the item's component given ALL its answers; the predicted
probability that A's and B's next answers repeat; and the expected reduction in the posterior variance of the item's
position b (class M) from one more answer of each mind -- against the same quantity averaged over all items those minds
answered. Plus where the flat items sit: posterior class mass and mean b."""
import sys
import numpy as np
import irt

name = sys.argv[1] if len(sys.argv) > 1 else "continue-stop"; variant = sys.argv[2] if len(sys.argv) > 2 else "2mf"
items, seq, S, N, X = irt.load(name)
m = irt.Model(int(variant[0]), "m" in variant, "f" in variant).fit(S, N, X)
M = irt.MINDS
L = m.comp_loglik(S, N, X); R = np.exp(L - np.logaddexp.reduce(L, axis=1)[:, None])
def ev_gain(i, j):
    """expected reduction in Var(b | answers) from one more answer of mind j (b only within class M; class mass kept)"""
    P = m.comp_probs(X[i])[:, j]; r = R[i]
    def varb(w):
        wm = w[2:]; t = wm.sum()
        if t <= 0: return 0.0
        mu = (wm * irt.G).sum() / t; return t * ((wm * (irt.G - mu) ** 2).sum() / t)   # class-M mass x Var(b | M)
    v0 = varb(r); p1 = r @ P
    v1 = varb(r * P / max(p1, 1e-12)); v0_ = varb(r * (1 - P) / max(1 - p1, 1e-12))
    return v0 - (p1 * v1 + (1 - p1) * v0_)
for A, B in (("sonnet55", "grok46"), ("haiku45nt", "grok46"), ("sonnet55", "haiku45nt")):
    a, b = M.index(A), M.index(B)
    flat, allb = [], []
    for i in range(len(items)):
        if N[i, a] > 0 and N[i, b] > 0:
            allb.append(i)
            if N[i, a] >= 2 and N[i, b] >= 2 and S[i, a] == 0 and S[i, b] == N[i, b]:
                flat.append(i)
    def summ(ix):
        ix = np.array(ix); P = np.array([m.comp_probs(X[i]) for i in ix])           # (n, K, M)
        pa = np.einsum("nk,nk->n", R[ix], P[:, :, a]); pb = np.einsum("nk,nk->n", R[ix], P[:, :, b])
        cls = R[ix][:, :2].mean(0).tolist() + [R[ix][:, 2:].sum(1).mean()]
        mb = (R[ix][:, 2:] * irt.G).sum(1) / np.maximum(R[ix][:, 2:].sum(1), 1e-12)
        ga = np.mean([ev_gain(i, a) for i in ix]); gb = np.mean([ev_gain(i, b) for i in ix])
        gmax = np.mean([max(ev_gain(i, j) for j in range(len(M))) for i in ix])
        return pa, pb, cls, mb, ga, gb, gmax
    pa, pb, cls, mb, ga, gb, gmax = summ(flat)
    _, _, cls_all, _, ga_all, gb_all, gmax_all = summ(allb)
    print(f"{A} continues / {B} stops, flat items {len(flat)}:")
    print(f"   P(next {A} answer continues) mean {1-pa.mean():.2f} (median {np.median(1-pa):.2f});  P(next {B} answer stops) mean {pb.mean():.2f} (median {np.median(pb):.2f})")
    print(f"   posterior class mass C / S / M: {np.round(cls, 2).tolist()} (all items both answered: {np.round(cls_all, 2).tolist()});  mean b in M: {mb.mean():+.2f}")
    print(f"   expected variance reduction of b from one more answer: {A} {ga:.4f}, {B} {gb:.4f}, best mind {gmax:.4f}"
          f"   (all items both answered: {ga_all:.4f}, {gb_all:.4f}, best {gmax_all:.4f})")
