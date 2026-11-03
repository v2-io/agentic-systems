import os, glob, collections, json, re, random, yaml
import sys; root = sys.argv[1] if len(sys.argv)>1 else "."; C=collections.Counter
ev=[]
for p in glob.glob(root + "/.vsect/events/*/*/*.yaml"):
    d=yaml.safe_load(open(p)); d["_kind"]=p.split("/events/")[1].split("/")[0]; ev.append(d)
# open.json distinct
d=json.load(open((sys.argv[2] if len(sys.argv)>2 else "open.json")))
rows=d["items"]
print("open rows:",len(rows),"distinct items:",len({r["item"] for r in rows}))
print("by kind distinct:", {k:len({r["item"] for r in rows if r["kind"]==k}) for k in set(r["kind"] for r in rows)})
print("imported_unchecked:", len(d["imported_unchecked"]) if isinstance(d["imported_unchecked"],list) else d["imported_unchecked"])
# target distribution for item rows
print("item rows target=(the store):", sum(1 for r in rows if r["kind"]=="item" and r["target"]=="(the store)"))
# items files: concerns coverage
n=0; withc=0; nconc=C(); opened_by=C()
for p in glob.glob(root+"/items/*.md"):
    fm=yaml.safe_load(open(p).read().split("---")[1]); n+=1
    c=fm.get("concerns") or []
    if c: withc+=1
    nconc[len(c) if isinstance(c,list) else 1]+=1
    opened_by[str(fm.get("opened-by"))[:38]]+=1
print("held items:",n,"with concerns:",withc, dict(sorted(nconc.items())))
print("opened-by top:", opened_by.most_common(12))
# check yield by review (round)
by_rev=collections.defaultdict(C)
for e in ev:
    if e["act"] in ("rederive","read-check","run","instantiate","read"):
        rv=(e.get("from") or "").split("#")[0]; by_rev[rv][e.get("outcome")]+=1
    if e["act"]=="place-finding":
        rv=(e.get("finding") or "").split("#")[0]; by_rev[rv]["finding"]+=1
print("\n== yield by review (checks: confirmed/broken/narrowed; findings) ==")
def key(s):
    m=re.search(r"(check|round|integration|reread)-?(\d+)",s); return s
for rv in sorted(by_rev, key=lambda s: s):
    c=by_rev[rv]; tot=c["confirmed"]+c["broken"]+c["narrowed"]
    print(f"{rv:60} chk={tot:3} broken={c['broken']:2} narrowed={c['narrowed']:2} findings={c['finding']:2}")
# sample held items for kind classification
random.seed(7)
files=sorted(glob.glob(root+"/items/*.md")); samp=random.sample(files,45)
print("\n== 45 random held items (owner | concerns | title) ==")
for p in samp:
    t=open(p).read(); fm=yaml.safe_load(t.split("---")[1])
    title=[l for l in t.split("---",2)[2].splitlines() if l.startswith("# ")]
    print(f"- [{fm.get('owner')}] [{len(fm.get('concerns') or [])}c] {title[0][2:200] if title else '(no title)'}")
