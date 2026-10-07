"""Pre-registration 2 (proposed round p002): the 43 flat Sonnet-continues / Grok-stops contexts of prereg-flat-splits.json,
asked once each, as a plain continue question on one-question sheets, of third minds: opus55, haiku45nt, haiku45 (the
Gemini minds are paused). For each context and mind, each model's P(stop), conditioned on every snapshot answer AND the
p001 answers (round p001 counted as one more round), with each model's parameters as fitted on the snapshot:
  2mf   irt.py variant 2mf (no mind x item term)
  irtu  the verifier's model (de-novo-2/irtu.py, parameters de-novo-2/tau-pred.json)
  lnb   lnb.py with block-set features (strengthening 2's chosen model), features from the snapshot
Reading, fixed here: per mind, the per-context log score of each model, and the log likelihood ratio between models
(sum over that mind's answered contexts). A model 'wins' a mind when its log score beats each other model's by more
than log(10) (a Bayes factor of 10 between point predictions); otherwise the result is reported as not discriminating.
The count of stops per mind is also reported against each model's 95% Poisson-binomial band.
  python3 prereg2_gen.py --out prereg-third-minds.json"""
import argparse, datetime, json, pickle, subprocess, sys
import numpy as np
sys.path.insert(0, "de-novo-2")
import irt, irtu, lnb, lib

MINDS3 = ["opus55", "haiku45nt", "haiku45"]
def load_p001():
    recs = [json.loads(l) for l in open(lib.ROOT / "data" / "answers" / "p001.jsonl") if l.strip()]
    return [r for r in recs if not lib.sealed(r) and r["outcome"] in ("none", "continuation")]

def main(out, lnb_pickle):
    items, seq, S, N, X = irt.load("continue-stop")
    pre = json.load(open("prereg-flat-splits.json")); ctxs = [c["context"] for c in pre["contexts"]]
    idx = {"".join(q[1]): i for i, q in enumerate(items)}
    S2, N2 = S.copy(), N.copy()
    for r in load_p001():
        c = "".join(r["context"]); i = idx[c]; j = irt.MINDS.index(r["mind"]); S2[i, j] += r["outcome"] == "none"; N2[i, j] += 1
    m0 = irt.Model(2, True, True).fit(S, N, X)
    P = json.load(open("de-novo-2/tau-pred.json"))["params"]; mu = irtu.ModelU()
    for k in ("alpha", "slope", "gamma", "tau", "pi", "eps", "dlt"): setattr(mu, k, np.array(P[k]))
    ml, Fo, Ft = pickle.load(open(lnb_pickle, "rb")); ad = lnb.Adapter(ml, Fo, Ft)
    rows = []
    for c in ctxs:
        i = idx[c]; row = {"context": c, "answers_so_far_incl_p001": {mm: [int(S2[i, j]), int(N2[i, j])] for j, mm in enumerate(irt.MINDS) if N2[i, j] > 0}, "p_stop": {}}
        L0 = m0.comp_loglik(S2[i:i+1], N2[i:i+1], X[i:i+1])[0]; r0 = np.exp(L0 - np.logaddexp.reduce(L0))
        ad.rows = np.array([i]); Ll = ad.comp_loglik(S2[i:i+1], N2[i:i+1], X[i:i+1])[0]; ad.rows = None; rl = np.exp(Ll - np.logaddexp.reduce(Ll))
        for mm in MINDS3:
            j = irt.MINDS.index(mm)
            row["p_stop"][mm] = {"2mf": round(float(r0 @ m0.comp_probs(X[i])[:, j]), 4),
                                 "irtu": round(float(mu.predict_next(S2[i], N2[i], X[i], j)), 4),
                                 "lnb": round(float(rl @ ad.cond_next_item(i, X[i], j, int(S2[i, j]), int(N2[i, j]))), 4)}
        rows.append(row)
    summ = {mm: {mod: round(sum(r["p_stop"][mm][mod] for r in rows), 2) for mod in ("2mf", "irtu", "lnb")} for mm in MINDS3}
    res = {"what": __doc__.split("\n  python3")[0], "written": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
           "git_head_at_writing": subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=str(lib.ROOT)).stdout.strip(),
           "expected_stops_of_43": summ, "contexts": rows}
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1); print(json.dumps(summ))

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True)
    ap.add_argument("--lnb-pickle", default="/private/tmp/claude-505/-Users-josephwecker-v2-src-arch-asf-empirica-glyph-sequence-perception/2c3109cb-51be-4d66-937d-88f689223324/scratchpad/lnb_blockset_all.pkl")
    a = ap.parse_args(); main(a.out, a.lnb_pickle)
