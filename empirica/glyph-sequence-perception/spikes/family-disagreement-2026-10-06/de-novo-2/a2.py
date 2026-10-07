import sys, json, collections, math, glob
SP="/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception/spikes/family-disagreement-2026-10-06"
ST="/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception"
sys.path.insert(0, SP)
import lib
recs, man = lib.load()
# sheet prompt option order
first_none={}
for f in glob.glob(ST+"/data/rounds/c*/sheets.jsonl"):
    rd=f.split("/")[-2]
    if not rd[1:].isdigit() or int(rd[1:])<96: continue
    for l in open(f):
        s=json.loads(l)
        if s["kind"]!="continue": continue
        p=s["prompt"]; first_none[s["sid"]]= p.index('- "none"') < p.index('- "continue"')
def stopp(L):
    n=len(L); k=sum(L); return f"{k}/{n}={k/n:.3f}" if n else "-"
for mind in ("sonnet55","grok46","opus55","haiku45nt","gemini38flash"):
    by_order=collections.defaultdict(list); by_st=collections.defaultdict(list); by_n=collections.defaultdict(list); pre=collections.defaultdict(list)
    for r in recs:
        if r["kind"]!="continue" or r["mind"]!=mind or r["outcome"] not in ("none","continuation"): continue
        t=r.get("tags") or {}
        if t.get("variant") not in (None,"plain") or t.get("null"): continue
        y = r["outcome"]=="none"
        rd=int(r["round"][1:]) if r["round"][1:].isdigit() else -1
        by_n[(rd>=96, t.get("sheet_n"))].append(y)
        if rd>=96:
            if r["sid"] in first_none: by_order[first_none[r["sid"]]].append(y)
            stg=t.get("soft_target")
            if stg is not None: by_st[0 if stg<=8 else (1 if stg<=16 else 2)].append(y)
    print(mind, "| none-first:", stopp(by_order[True]), "continue-first:", stopp(by_order[False]),
          "| soft 3-8:", stopp(by_st[0]), "9-16:", stopp(by_st[1]), "17-24:", stopp(by_st[2]))
    print("   sheet_n pre-c096:", {k[1]:stopp(v) for k,v in sorted(by_n.items(), key=lambda kv: (kv[0][0], kv[0][1] or 0)) if not k[0]})
    print("   sheet_n c096+   :", {k[1]:stopp(v) for k,v in sorted(by_n.items(), key=lambda kv: (kv[0][0], kv[0][1] or 0)) if k[0]})
