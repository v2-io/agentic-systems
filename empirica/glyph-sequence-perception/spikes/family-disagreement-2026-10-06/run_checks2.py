import sys, json, numpy as np
sys.path.insert(0, "de-novo-2")
import irt, irtu, bb, checks2
items, seq, S, N, X = irt.load("continue-stop")
which = sys.argv[1:] or ["2mf", "irtu", "bb"]
if "2mf" in which:
    checks2.show(checks2.run(checks2.Adapt2mf(irt.Model(2, True, True).fit(S, N, X)), items, seq, S, N, X, "2mf (no mind x item term)"))
if "irtu" in which:
    P = json.load(open("de-novo-2/tau-pred.json"))["params"]; m = irtu.ModelU()
    for k in ("alpha", "slope", "gamma", "tau", "pi", "eps", "dlt"): setattr(m, k, np.array(P[k]))
    checks2.show(checks2.run(checks2.AdaptU(m), items, seq, S, N, X, "irtu (the verifier's: 2mf + Gaussian mind x item intercept)"))
if "bb" in which:
    checks2.show(checks2.run(checks2.AdaptBB(bb.BB(fam=True).fit(S, N, X)), items, seq, S, N, X, "beta-binomial, nonparametric b"))
