#!/usr/bin/env python3
"""Joseph's question (2026-10-05, mid-spike): "given 2 codepoints' tokens in embedded space [can you] find other
codepoints within some dimension ... putting a line through any two code points and seeing if that line intersects
with other code-points anywhere -- or, equivalently, doing a handful of known ones and figuring out the PCA or
something and extrapolating to more?"

For every instance whose context has >= 2 glyphs (… p q → truth), rank the universe by:
  nn        cosine to q                                  (plain nearest neighbour; context ignored)
  offset    cosine to q + (q - p)                        (the parallelogram / analogy step)
  line      -distance to the ray q + s(q - p), s in [0.5, 3] (a line through p and q, ahead of q)
  meanstep  cosine to q + mean consecutive step of the whole context (>= 2 steps -> the "handful of known ones")
  pc1       q + one context-step along the context's first principal component (contexts of >= 3 glyphs)
and the same moves in codepoint space as the comparator: cp (|x-q|), cp-offset (|x-(2q-p)|).

Also a direct geometry check, independent of retrieval: along agreed paths a b c (consecutive truth steps), the
cosine between step vectors (b-a) and (c-b). If sequences were straight lines in the space, it would be near 1;
the baseline is the same cosine for random glyph triples.

  python3 eval_lines.py [--gt r011] [--truth first2] EMBFILE ...
"""
import argparse, collections, json
import numpy as np
from lib import DER
import rankers as RK

ap = argparse.ArgumentParser()
ap.add_argument("--gt", default="r011"); ap.add_argument("--truth", default="first2")
ap.add_argument("embs", nargs="+")
a = ap.parse_args()
G = json.load(open(DER / f"gt-{a.gt}.json"))
KS = (1, 3, 10, 30, 100)

def truth(I):
    return [g for g, p in I["props"].items()
            if len(set(p["fams_first"] if a.truth.startswith("first") else p["fams"]) - {"muse"}) >= int(a.truth[-1])
            and g not in I["ctx_all"] and g != I["node"] and g in RK.IDX]

inst = [(k, I, truth(I)) for k, I in G["instances"].items()
        if len(I["ctx"]) >= 2 and all(g in RK.IDX for g in I["ctx"])]
inst = [x for x in inst if x[2]]

def ranks(score, excl):
    s = score.astype(np.float64) + RK.JITTER
    for g in excl:
        s[RK.IDX[g]] = -np.inf
    o = np.argsort(-s, kind="stable"); r = np.empty(len(s), dtype=np.int64); r[o] = np.arange(1, len(s) + 1)
    return r

def unit(v):
    return v / (np.linalg.norm(v) + 1e-9)

def run(name, scorefn):
    rows = collections.defaultdict(list)
    for k, I, T in inst:
        sc = scorefn(I)
        if sc is None:
            continue
        r = ranks(sc, set(I["ctx_all"]) | {I["node"]})
        best = min(r[RK.IDX[g]] for g in T)
        st = "cp-near" if any(abs(ord(g) - ord(I["node"])) <= 1 for g in T) else "cp-far"
        for s_ in ("all", st):
            rows[s_].append(best)
    out = {}
    for s_, b in rows.items():
        b = np.array(b); out[s_] = {f"hit@{kk}": float((b <= kk).mean()) for kk in KS} | {"n": len(b)}
    return out

CPf = RK.CP.astype(np.float64)
methods = {
    "cp": lambda I: -np.abs(CPf - ord(I["node"])),
    "cp-offset": lambda I: -np.abs(CPf - (2 * ord(I["node"]) - ord(I["ctx"][-2]))),
}
res = {}
for m, f in methods.items():
    res[m] = run(m, f)
geom = {}
for emb in a.embs:
    X = np.load(DER / "emb" / f"{emb}.npy").astype(np.float32)
    X /= (np.linalg.norm(X, axis=1, keepdims=True) + 1e-9)
    E = lambda g: X[RK.IDX[g]]
    def nn(I): return X @ E(I["node"])
    def offset(I):
        q, p = E(I["node"]), E(I["ctx"][-2]); return X @ unit(q + (q - p))
    def line(I):
        q, p = E(I["node"]), E(I["ctx"][-2]); d = q - p; dd = float(d @ d) + 1e-12
        s = np.clip(((X - q) @ d) / dd, 0.5, 3.0)
        D = X - q[None, :] - s[:, None] * d[None, :]
        return -np.linalg.norm(D, axis=1)
    def meanstep(I):
        C = np.stack([E(g) for g in I["ctx"]])
        if len(C) < 3: return None
        return X @ unit(C[-1] + np.diff(C, axis=0).mean(0))
    def pc1(I):
        C = np.stack([E(g) for g in I["ctx"]])
        if len(C) < 3: return None
        Cc = C - C.mean(0); u = np.linalg.svd(Cc, full_matrices=False)[2][0]
        if (C[-1] - C[0]) @ u < 0: u = -u
        step = np.abs(np.diff(C @ u)).mean()
        return X @ unit(C[-1] + step * u)
    for m, f in (("nn", nn), ("offset", offset), ("line", line), ("meanstep", meanstep), ("pc1", pc1)):
        res[f"{emb}:{m}"] = run(m, f)
    # geometry: straightness of agreed paths a b c
    cs, rnd = [], []
    rng = np.random.default_rng(0)
    for k, I, T in inst:
        a_, b_ = I["ctx"][-2], I["ctx"][-1]
        for c_ in T:
            u1, u2 = E(b_) - E(a_), E(c_) - E(b_)
            cs.append(float(unit(u1) @ unit(u2)))
        i, j, l = rng.integers(0, len(RK.GL), 3)
        rnd.append(float(unit(X[j] - X[i]) @ unit(X[l] - X[j])))
    geom[emb] = {"step_cos_mean": float(np.mean(cs)), "step_cos_median": float(np.median(cs)),
                 "random_triple_mean": float(np.mean(rnd)), "n": len(cs)}

print(f"gt={a.gt} truth={a.truth}: {len(inst)} instances with >= 2 context glyphs")
for st in ("all", "cp-near", "cp-far"):
    print(f"\n[{st}]  {'method':56s} " + " ".join(f"hit@{k:<4d}" for k in KS) + "   n")
    for m, r in res.items():
        if st in r:
            print(f"        {m:56s} " + " ".join(f"{r[st][f'hit@{k}']:.3f}   " for k in KS) + f"{r[st]['n']}")
print("\nstraightness: cos((b-a),(c-b)) along agreed paths vs random triples")
for e, g in geom.items():
    print(f"  {e:44s} paths {g['step_cos_mean']:+.3f} (median {g['step_cos_median']:+.3f}, n={g['n']})   random {g['random_triple_mean']:+.3f}")
p = DER / f"lines-{a.gt}-{a.truth}.json"
old = json.load(open(p)) if p.exists() else {}
old.update({"retrieval": {**old.get("retrieval", {}), **res}, "geometry": {**old.get("geometry", {}), **geom}})
json.dump(old, open(p, "w"), indent=1)
