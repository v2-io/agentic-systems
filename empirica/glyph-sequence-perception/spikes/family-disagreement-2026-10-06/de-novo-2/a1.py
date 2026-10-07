import sys, json, collections
SP="/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception/spikes/family-disagreement-2026-10-06"
sys.path.insert(0, SP)
import lib
recs, man = lib.load()
pre = json.load(open(SP+"/prereg-flat-splits.json"))
ctxs = {tuple(c["context_glyphs"]) for c in pre["contexts"]}
print(len(recs), man["kept"])
keys=collections.Counter()
rows=[]
for r in recs:
    if r["kind"]=="continue" and tuple(r.get("context") or ())in ctxs and r["mind"] in ("sonnet55","grok46"):
        t=r.get("tags") or {}
        rows.append((r["mind"], r["round"], r["outcome"], t.get("variant"), t.get("sheet_n") or r.get("sheet_n"), t.get("soft_target"), t.get("position"), r.get("protocol"), r.get("era"), t.get("control")))
print("example record keys:", sorted(r.keys()) if False else "")
ex=[r for r in recs if r["kind"]=="continue" and tuple(r.get("context") or ()) in ctxs][0]
print(json.dumps({k:v for k,v in ex.items() if k not in ("raw",)}, ensure_ascii=False)[:1500])
c=collections.Counter((m,rd[:1]+str(int(rd[1:])//10*10) if rd[1:].isdigit() else rd) for m,rd,*_ in rows)
print(sorted(c.items()))
print(collections.Counter((m,v,st is not None) for m,rd,o,v,sn,st,*_ in rows))
print(collections.Counter((m,sn) for m,rd,o,v,sn,*_ in rows))
print(collections.Counter((m,e,p) for m,rd,o,v,sn,st,pos,p,e,cc in rows))
