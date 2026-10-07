# within-item effects of protocol era (c096+: soft target, fated option order) and single-item sheets on stopping
import sys, json, collections, numpy as np
SP="/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception/spikes/family-disagreement-2026-10-06"
sys.path.insert(0, SP)
import lib
from values import ckey
recs, man = lib.load()
D=collections.defaultdict(lambda: collections.defaultdict(list))
for r in recs:
    if r["kind"]!="continue" or r["outcome"] not in ("none","continuation"): continue
    t=r.get("tags") or {}
    if t.get("variant") not in (None,"plain") or t.get("null"): continue
    rd=int(r["round"][1:]) if r["round"][1:].isdigit() else -1
    D[(r["mind"],ckey(r))]["new" if rd>=96 else "old"].append(r["outcome"]=="none")
    D[(r["mind"],ckey(r))]["n1" if t.get("sheet_n")==1 else "nk"].append(r["outcome"]=="none")
def matched(mind,a,b):
    ds=[]
    for (m,q),d in D.items():
        if m!=mind or not d[a] or not d[b]: continue
        ds.append(np.mean(d[a])-np.mean(d[b]))
    ds=np.array(ds)
    return f"{a}-{b}: {ds.mean():+.3f} ± {ds.std(ddof=1)/np.sqrt(len(ds)):.3f} (items {len(ds)})" if len(ds)>2 else "-"
for mind in ("sonnet55","opus55","haiku45nt","grok46","gemini38flash","gemini31pro"):
    print(mind, "|", matched(mind,"new","old"), "|", matched(mind,"n1","nk"))
