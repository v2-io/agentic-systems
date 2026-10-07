"""De novo 3, check 9 (POST HOC: computed after p002's answers were read; nothing tuned). Strengthening 2's two-factor
model (twof.py, no features, as in its section 5), fitted on the snapshot exactly as run_twof.py does, conditioned on
snapshot + p001 answers at each of the 43 contexts as prereg2_gen.py does, gives P(stop) for opus55, haiku45nt and
haiku45. Scored with prereg2_check.py's log score. Question: does the spike's own Haiku axis account for the
pre-registered models' failure on Haiku with thinking?"""
import sys, json, math, pathlib, numpy as np
HERE = pathlib.Path(__file__).resolve().parent; SP = HERE.parent; STUDY = SP.parents[1]
sys.path.insert(0, str(SP)); import os; os.chdir(SP)
import irt, twof, lib
items, seq, S, N, X = irt.load("continue-stop")
pre = json.load(open("prereg-flat-splits.json")); ctxs = [c["context"] for c in pre["contexts"]]
idx = {"".join(q[1]): i for i, q in enumerate(items)}
S2, N2 = S.copy(), N.copy()
for l in open(lib.ROOT / "data" / "answers" / "p001.jsonl"):
    r = json.loads(l)
    if lib.sealed(r) or r["outcome"] not in ("none", "continuation"): continue
    i = idx["".join(r["context"])]; j = irt.MINDS.index(r["mind"]); S2[i, j] += r["outcome"] == "none"; N2[i, j] += 1
m = twof.TwoF(feats=False, nf=2).fit(S, N, X)
print("fit ll", round(m.ll, 1), "iters", m.iters, "loadings", dict(zip(irt.MINDS, np.round(m.t, 2))), flush=True)
Z = np.zeros((1, len(irt.MINDS)))
P = {}
for c in ctxs:
    i = idx[c]; L = m.comp_loglik_full(S2[i:i+1], N2[i:i+1], X[i:i+1], Z, Z)[0]; R = np.exp(L - np.logaddexp.reduce(L))
    P[c] = {mm: float(R @ m.cond_next_row(Z[0], Z[0], X[i], irt.MINDS.index(mm))) for mm in ("opus55", "haiku45nt", "haiku45")}
ans = {}
for l in open(STUDY / "data" / "answers" / "p002.jsonl"):
    r = json.loads(l)
    if r["outcome"] in ("continuation", "none"): ans.setdefault(r["mind"], {})["".join(r["context"])] = int(r["outcome"] == "none")
for mm in ("opus55", "haiku45nt", "haiku45"):
    a = ans[mm]; ps = [P[c][mm] for c in a]
    print(f"{mm}: stops {sum(a.values())}; two-factor expected {sum(ps):.1f}; log score {sum(math.log(p if y else 1 - p) for p, y in zip(ps, a.values())):.2f}")
json.dump(P, open(HERE / "twof-p002-posthoc.json", "w"), ensure_ascii=False, indent=0)
