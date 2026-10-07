import sys, json, numpy as np
sys.path.insert(0, "de-novo-2")
import irt, irtu, bb, checks2, preq
items, seq, S, N, X = irt.load("continue-stop")
which = sys.argv[1:] or ["2mf", "irtu", "bb"]
if "2mf" in which:
    preq.report(preq.score({None: checks2.Adapt2mf(irt.Model(2, True, True).fit(S, N, X))}, None, items, seq, X), "2mf, all-data parameters")
if "irtu" in which:
    P = json.load(open("de-novo-2/tau-pred.json"))["params"]; m = irtu.ModelU()
    for k in ("alpha", "slope", "gamma", "tau", "pi", "eps", "dlt"): setattr(m, k, np.array(P[k]))
    preq.report(preq.score({None: checks2.AdaptU(m)}, None, items, seq, X), "irtu, all-data parameters (tau-pred.json)")
if "bb" in which:
    preq.report(preq.score({None: checks2.AdaptBB(bb.BB(fam=True).fit(S, N, X))}, None, items, seq, X), "beta-binomial, all-data parameters")
