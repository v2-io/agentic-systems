#!/usr/bin/env python3
"""Strengthening attempt: maybe raw embedding geometry is the wrong test, and a LEARNED linear view of the space
holds sequences (Joseph's "axis/line" intuition, made trainable). Learn a low-rank bilinear successor score
    s(q, x) = (A e_q) . (B e_x)          A, B: d -> r (r = 64), e = a fixed embedding
from minds' answers, with a softmax over the WHOLE universe (InfoNCE), and test on Unicode BLOCKS never seen in
training (5-fold split by the node's block), so the probe must generalize to new regions, as tendrils would.

Training pairs: every (node -> first-choice proposal by >=1 family) from r011 next/between answers plus every
survey step. Test: the held-out-block instances of the r011 'first2' set (the headline reference set), ranked over
the universe with context glyphs excluded, compared with codepoint order on the very same instances.

  python3 probe_linear.py EMBFILE [--rank 64] [--steps 600]
"""
import argparse, collections, hashlib, json
import numpy as np, torch
from lib import DER, block
import rankers as RK

ap = argparse.ArgumentParser()
ap.add_argument("emb"); ap.add_argument("--rank", type=int, default=64); ap.add_argument("--steps", type=int, default=600)
ap.add_argument("--folds", type=int, default=5)
ap.add_argument("--residual", action="store_true",
                help="score = 10*cos(e_q, e_x) + learned bilinear term (initialised near zero): the probe can only add "
                     "to plain nearest-neighbour, so any loss of held-out skill is the learned part's doing")
a = ap.parse_args()
torch.manual_seed(0)
X = np.load(DER / "emb" / f"{a.emb}.npy").astype(np.float32)
X /= (np.linalg.norm(X, axis=1, keepdims=True) + 1e-9)
XT = torch.tensor(X)
fold_of = lambda g: int(hashlib.md5(block(g).encode()).hexdigest(), 16) % a.folds

pairs = []
for gt in ("r011", "survey"):
    G = json.load(open(DER / f"gt-{gt}.json"))
    for I in G["instances"].values():
        q = I["node"]
        if q not in RK.IDX:
            continue
        for g, p in I["props"].items():
            if p["fams_first"] and g in RK.IDX and g != q:
                pairs.append((RK.IDX[q], RK.IDX[g], fold_of(q)))
pairs = np.array(pairs)
G = json.load(open(DER / "gt-r011.json"))
tests = []
for k, I in G["instances"].items():
    q = I["node"]
    T = [g for g, p in I["props"].items() if len(set(p["fams_first"]) - {"muse"}) >= 2 and g not in I["ctx_all"]
         and g != q and g in RK.IDX]
    if q in RK.IDX and T:
        tests.append((q, T, I["ctx_all"], fold_of(q)))

KS = (1, 3, 10, 30, 100)
res = collections.defaultdict(list)
for fold in range(a.folds):
    tr = pairs[pairs[:, 2] != fold]
    A = torch.nn.Linear(X.shape[1], a.rank, bias=False); B = torch.nn.Linear(X.shape[1], a.rank, bias=False)
    with torch.no_grad():
        if a.residual:
            A.weight.mul_(0.01); B.weight.mul_(0.01)
        else:
            B.weight.copy_(A.weight)
    base = (lambda qv: 10.0 * qv @ XT.T) if a.residual else (lambda qv: 0.0)
    opt = torch.optim.Adam(list(A.parameters()) + list(B.parameters()), lr=3e-3, weight_decay=1e-4)
    for step in range(a.steps):
        idx = np.random.default_rng(step + 1000 * fold).integers(0, len(tr), 256)
        q, g = torch.tensor(tr[idx, 0]), torch.tensor(tr[idx, 1])
        logits = A(XT[q]) @ B(XT).T * 10.0 + base(XT[q])
        loss = torch.nn.functional.cross_entropy(logits, g)
        opt.zero_grad(); loss.backward(); opt.step()
    with torch.no_grad():
        BX = B(XT)
        for q, T, ctx, f in tests:
            if f != fold:
                continue
            qv = XT[RK.IDX[q]][None]
            s = (A(qv) @ BX.T * 10.0 + base(qv))[0].numpy().astype(np.float64) + RK.JITTER
            c = RK.cp_scores(q)
            near = any(abs(ord(t) - ord(q)) <= 1 for t in T)
            nn = (XT[RK.IDX[q]] @ XT.T).numpy().astype(np.float64) + RK.JITTER
            for name, sc in (("learned", s), ("cp", c), ("nn", nn)):
                sc = sc.copy()
                for x in set(ctx) | {q}:
                    if x in RK.IDX: sc[RK.IDX[x]] = -np.inf
                r = (sc[None, :] > np.array([sc[RK.IDX[t]] for t in T])[:, None]).sum(1) + 1
                for st in ("all", "cp-near" if near else "cp-far"):
                    res[(name, st)].append(int(r.min()))
    print(f"fold {fold}: {len(tr)} training pairs, final loss {loss.item():.2f}", flush=True)

print(f"\n{a.emb}  rank={a.rank} residual={a.residual} steps={a.steps}  held-out-block test instances: {len(res[('cp', 'all')])}")
out = {}
for st in ("all", "cp-near", "cp-far"):
    print(f"[{st}]")
    for name in ("cp", "nn", "learned"):
        b = np.array(res[(name, st)])
        out[f"{name}|{st}"] = {f"hit@{k}": float((b <= k).mean()) for k in KS} | {"n": len(b)}
        print(f"   {name:8s} " + " ".join(f"hit@{k}={(b <= k).mean():.3f}" for k in KS) + f"  n={len(b)}")
p = DER / "probe-linear.json"
old = json.load(open(p)) if p.exists() else {}
old[f"{a.emb}|r{a.rank}{'|residual' if a.residual else ''}|steps{a.steps}"] = out; json.dump(old, open(p, "w"), indent=1)
