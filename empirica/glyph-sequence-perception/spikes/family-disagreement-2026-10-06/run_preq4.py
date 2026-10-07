"""LNB block-set, refitted with the corrected tau update; prequential report with features from earlier rounds only
(lnb_prefix.py). Also reports the item-level models' prequential score again for comparison on the same rows."""
import pickle, numpy as np
import irt, lnb, preq, lnb_prefix
items, seq, S, N, X = irt.load("continue-stop")
Fo, Ft, _ = lnb.block_features(items, S, N, grouping="blockset")
m = lnb.LNB(feats=True).fit(S, N, X, Fo, Ft, iters=150)
print(f"LNB blockset (tau fixed): ll {m.ll:.1f}, iters {m.iters}", flush=True)
for j, mm in enumerate(irt.MINDS):
    print(f"   {mm:14s} a {m.alpha[j]:+.2f} s {m.slope[j]:.2f} g {m.gamma[j]:+.2f} tau {m.tau[j]:.2f} lam {m.lam[j]:+.2f} kap {m.kap[j]:+.2f}", flush=True)
pickle.dump((m, Fo, Ft), open("/private/tmp/claude-505/-Users-josephwecker-v2-src-arch-asf-empirica-glyph-sequence-perception/2c3109cb-51be-4d66-937d-88f689223324/scratchpad/lnb_blockset_all.pkl", "wb"))
rows = preq.prefixes(items, seq, irt.MINDS)
PFo, PFt = lnb_prefix.prefix_features(items, seq, rows)
print("prefix features built", flush=True)
preq.report(preq.score({None: lnb_prefix.RowAdapter(m, PFo, PFt, rows)}, None, items, seq, X), "LNB block-set, features from earlier rounds only")
