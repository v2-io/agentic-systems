# cohere, real runs: per mind, 'no' rate on items every OTHER answering mind called coherent (>=3 other yes, 0 other no),
# by set class -- a lapse rate at the top that a logit without an asymptote would read as a smaller contiguity offset.
import sys, collections
SP="/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception/spikes/family-disagreement-2026-10-06"
sys.path.insert(0, SP)
import lib, abbott
from values import ckey
recs,_=lib.load()
A=collections.defaultdict(lambda: collections.defaultdict(list)); cls={}
for r in recs:
    t=r.get("tags") or {}
    if r["kind"]!="cohere" or t.get("control") or t.get("variant") not in (None,"plain") or r["outcome"] not in ("yes","no"): continue
    q=ckey(r); A[q][r["mind"]].append(r["outcome"]=="yes"); cls[q]=abbott.setcls(r["context"])
for mm in abbott.MINDS:
    out=[]
    for c in ("contig","other"):
        no=n=0
        for q,d in A.items():
            if cls[q]!=c or mm not in d: continue
            oth=[y for m2,ys in d.items() if m2!=mm for y in ys]
            if len(oth)>=3 and all(oth): n+=len(d[mm]); no+=len(d[mm])-sum(d[mm])
        out.append(f"{c}: no {no}/{n} = {no/max(n,1):.3f}")
    print(f"{mm:14s} " + " | ".join(out))
