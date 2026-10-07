import json, numpy as np
SP="/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception/spikes/family-disagreement-2026-10-06"
pre=json.load(open(SP+"/prereg-flat-splits.json")); tau=json.load(open("tau-pred.json"))
ctx=[c["context"] for c in pre["contexts"]]
p0g={c["context"]:c["p_stop_next"]["grok46"] for c in pre["contexts"]}; p0s={c["context"]:1-c["p_stop_next"]["sonnet55"] for c in pre["contexts"]}
p1g=dict(zip(tau["ctx"],tau["grok_p"])); p1s=dict(zip(tau["ctx"],tau["sonnet_p"]))
def pb(ps):
    d=np.array([1.0])
    for p in ps: d=np.convolve(d,[1-p,p])
    return d
for who,a,b in (("grok stops",p0g,p1g),("sonnet continues",p0s,p1s)):
    d0=pb([a[c] for c in ctx]); d1=pb([b[c] for c in ctx])
    print(who, "| k: log10 LR (tau model : 2mf)")
    print("  ", " ".join(f"{k}:{np.log10(d1[k]/d0[k]):+.1f}" for k in range(15,44)))
