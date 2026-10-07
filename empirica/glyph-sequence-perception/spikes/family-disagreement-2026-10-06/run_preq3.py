"""LNB with block-set features (lnb.GROUPINGS['blockset']), fitted on all snapshot continue answers (120 EM iterations
at most), its parameters, and the prequential report (preq.py), with same-round pairs."""
import pickle, numpy as np
import irt, lnb, preq
items, seq, S, N, X = irt.load("continue-stop")
Fo, Ft, _ = lnb.block_features(items, S, N, grouping="blockset")
m = lnb.LNB(feats=True).fit(S, N, X, Fo, Ft, iters=120)
print(f"LNB blockset: ll {m.ll:.1f}, iters {m.iters}")
for j, mm in enumerate(irt.MINDS):
    print(f"   {mm:14s} a {m.alpha[j]:+.2f} s {m.slope[j]:.2f} g {m.gamma[j]:+.2f} tau {m.tau[j]:.2f} lam {m.lam[j]:+.2f} kap {m.kap[j]:+.2f}")
pickle.dump((m, Fo, Ft), open("/private/tmp/claude-505/-Users-josephwecker-v2-src-arch-asf-empirica-glyph-sequence-perception/2c3109cb-51be-4d66-937d-88f689223324/scratchpad/lnb_blockset_all.pkl", "wb"))
preq.report(preq.score({None: lnb.Adapter(m, Fo, Ft)}, None, items, seq, X), "LNB, block-set features, all-data parameters")
