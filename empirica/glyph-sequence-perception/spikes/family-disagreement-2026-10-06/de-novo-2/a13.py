import json, numpy as np
ST="/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception"
SP=ST+"/spikes/family-disagreement-2026-10-06"
pre=json.load(open(SP+"/prereg-flat-splits.json")); tau=json.load(open("tau-pred.json"))
R=[json.loads(l) for l in open(ST+"/data/answers/p001.jsonl") if l.strip()]
ans={(r["mind"],"".join(r["context"])):r for r in R}
p0g={c["context"]:c["p_stop_next"]["grok46"] for c in pre["contexts"]}; p0s={c["context"]:1-c["p_stop_next"]["sonnet55"] for c in pre["contexts"]}
p1g=dict(zip(tau["ctx"],tau["grok_p"])); p1s=dict(zip(tau["ctx"],tau["sonnet_p"]))
def pb(ps):
    d=np.array([1.0])
    for p in ps: d=np.convolve(d,[1-p,p])
    return d
for who,mind,want,a,b in (("Grok stops","grok46","none",p0g,p1g),("Sonnet continues","sonnet55","continuation",p0s,p1s)):
    cs=[c for c in a if ans.get((mind,c)) and ans[(mind,c)]["outcome"] in ("none","continuation")]
    k=sum(ans[(mind,c)]["outcome"]==want for c in cs)
    d0=pb([a[c] for c in cs]); d1=pb([b[c] for c in cs])
    tail0=d0[k:].sum(); tail1=d1[k:].sum()
    ll0=sum(np.log(a[c] if ans[(mind,c)]["outcome"]==want else 1-a[c]) for c in cs)
    ll1=sum(np.log(b[c] if ans[(mind,c)]["outcome"]==want else 1-b[c]) for c in cs)
    print(f"{who}: {k}/{len(cs)}; 2mf expected {sum(a[c] for c in cs):.1f}, P(>= k) {tail0:.2e}; tau expected {sum(b[c] for c in cs):.1f}, P(>=k) {tail1:.3f};"
          f" count LR log10(tau:2mf) {np.log10(d1[k]/d0[k]):+.2f}; per-context log score 2mf {ll0:.2f} tau {ll1:.2f}")
print()
for c in pre["contexts"]:
    ctx=c["context"]; g=ans.get(("grok46",ctx)); s=ans.get(("sonnet55",ctx))
    f=lambda r: ("none" if r["outcome"]=="none" else ("".join(r.get("continuation") or [])[:8] if r["outcome"]=="continuation" else r["outcome"])) if r else "-"
    print(f"{ctx:10s} grok {f(g):10s} (p_stop 2mf {p0g[ctx]:.2f} tau {p1g[ctx]:.2f}) | sonnet {f(s):10s} (p_cont 2mf {p0s[ctx]:.2f} tau {p1s[ctx]:.2f}) st={(g or {}).get('tags',{}).get('soft_target')}")
