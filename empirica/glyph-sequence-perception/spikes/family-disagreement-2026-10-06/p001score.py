"""Score round p001 (the 43 flat contexts asked again, one question per sheet) per context under three models, as
held-out data, AFTER model choice on the snapshot (NOTES, strengthening 2 criterion): 2mf (prereg-flat-splits.json),
irtu (de-novo-2/tau-pred.json, written before p001 was read), and LNB with block-set features (fitted on all snapshot
continue answers; the context's posterior given all its snapshot answers; features from the snapshot). Grok: P(stop);
Sonnet: P(continue). Answers other than a continuation or "none" are left out, as the pre-registration specifies."""
import json, pickle, numpy as np
import irt, lnb, lib
SP = "/private/tmp/claude-505/-Users-josephwecker-v2-src-arch-asf-empirica-glyph-sequence-perception/2c3109cb-51be-4d66-937d-88f689223324/scratchpad/lnb_blockset_all.pkl"
pre = json.load(open("prereg-flat-splits.json")); tau = json.load(open("de-novo-2/tau-pred.json"))
items, seq, S, N, X = irt.load("continue-stop")
m, Fo, Ft = pickle.load(open(SP, "rb")); ad = lnb.Adapter(m, Fo, Ft)
idx = {"".join(q[1]): i for i, q in enumerate(items)}
def lnb_p(ctx, mind):
    i = idx[ctx]; j = irt.MINDS.index(mind)
    ad.rows = np.array([i]); L = ad.comp_loglik(S[i:i+1], N[i:i+1], X[i:i+1])[0]; ad.rows = None
    r = np.exp(L - np.logaddexp.reduce(L)); return float(r @ ad.cond_next_item(i, X[i], j, int(S[i, j]), int(N[i, j])))
recs = [json.loads(l) for l in open(lib.ROOT / "data" / "answers" / "p001.jsonl") if l.strip()]
recs = [r for r in recs if not lib.sealed(r)]
ans = {(r["mind"], "".join(r["context"])): r for r in recs}
P = {"2mf": ({c["context"]: c["p_stop_next"]["grok46"] for c in pre["contexts"]}, {c["context"]: 1 - c["p_stop_next"]["sonnet55"] for c in pre["contexts"]}),
     "irtu": (dict(zip(tau["ctx"], tau["grok_p"])), dict(zip(tau["ctx"], tau["sonnet_p"]))),
     "lnb-blockset": ({c["context"]: lnb_p(c["context"], "grok46") for c in pre["contexts"]}, {c["context"]: 1 - lnb_p(c["context"], "sonnet55") for c in pre["contexts"]})}
def pb(ps):
    d = np.array([1.0])
    for p in ps: d = np.convolve(d, [1 - p, p])
    return d
out = {}
for who, mind, want, side in (("Grok stops", "grok46", "none", 0), ("Sonnet continues", "sonnet55", "continuation", 1)):
    cs = [c for c in P["2mf"][side] if ans.get((mind, c)) and ans[(mind, c)]["outcome"] in ("none", "continuation")]
    k = sum(ans[(mind, c)]["outcome"] == want for c in cs)
    print(f"{who}: {k} of {len(cs)}")
    for name, (pg, ps) in P.items():
        p = pg if side == 0 else ps; q = [p[c] for c in cs]; d = pb(q)
        ll = sum(np.log(p[c] if ans[(mind, c)]["outcome"] == want else 1 - p[c]) for c in cs)
        lo = int(np.searchsorted(np.cumsum(d), 0.025)); hi = int(np.searchsorted(np.cumsum(d), 0.975))
        print(f"   {name:13s} expected {sum(q):5.1f} [{lo}-{hi}]  P(>= {k}) {d[k:].sum():.4f}  per-context log score {ll:7.2f}")
        out[(who, name)] = ll
for name in P: print(f"total log score {name:13s} {out[('Grok stops', name)] + out[('Sonnet continues', name)]:.2f}")
