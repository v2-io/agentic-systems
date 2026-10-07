"""Prequential report for 2mf, irtu, beta-binomial and LNB (all-data parameters); LNB's features from all snapshot items."""
import sys, json, numpy as np
sys.path.insert(0, "de-novo-2")
import irt, irtu, bb, lnb, checks2, preq
items, seq, S, N, X = irt.load("continue-stop")
which = sys.argv[1:] or ["2mf", "irtu", "bb", "lnb"]
for w in which:
    if w == "2mf": ad = checks2.Adapt2mf(irt.Model(2, True, True).fit(S, N, X)); lab = "2mf"
    if w == "irtu":
        P = json.load(open("de-novo-2/tau-pred.json"))["params"]; m = irtu.ModelU()
        for k in ("alpha", "slope", "gamma", "tau", "pi", "eps", "dlt"): setattr(m, k, np.array(P[k]))
        ad = checks2.AdaptU(m); lab = "irtu (tau-pred.json)"
    if w == "bb": ad = checks2.AdaptBB(bb.BB(fam=True).fit(S, N, X)); lab = "beta-binomial"
    if w == "lnb":
        Fo, Ft, _ = lnb.block_features(items, S, N); m = lnb.LNB(feats=True).fit(S, N, X, Fo, Ft)
        print("LNB parameters:"); [print(f"   {mm:14s} a {m.alpha[j]:+.2f} s {m.slope[j]:.2f} g {m.gamma[j]:+.2f} tau {m.tau[j]:.2f} lam {m.lam[j]:+.2f} kap {m.kap[j]:+.2f}") for j, mm in enumerate(irt.MINDS)]
        ad = lnb.Adapter(m, Fo, Ft); lab = "LNB (mind x block)"
        import pickle; pickle.dump(m, open("/private/tmp/claude-505/-Users-josephwecker-v2-src-arch-asf-empirica-glyph-sequence-perception/2c3109cb-51be-4d66-937d-88f689223324/scratchpad/lnb_all.pkl", "wb"))
    preq.report(preq.score({None: ad}, None, items, seq, X), lab)
