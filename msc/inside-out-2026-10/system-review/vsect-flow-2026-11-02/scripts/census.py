import os, sys, glob, collections, re
import yaml
import sys; root = sys.argv[1] if len(sys.argv)>1 else "."
ev = []
for p in glob.glob(root + "/.vsect/events/*/*/*.yaml"):
    with open(p) as f:
        try:
            d = yaml.safe_load(f)
        except Exception as e:
            print("BAD", p, e); continue
    d["_kind"] = p.split("/events/")[1].split("/")[0]
    d["_slug"] = p.split("/events/")[1].split("/")[1]
    ev.append(d)
print("events:", len(ev))
C = collections.Counter
print("\n== act x kind ==")
for (k,a),n in sorted(C((e["_kind"], e["act"]) for e in ev).items()): print(f"{k:10} {a:20} {n}")
print("\n== act x outcome ==")
for (a,o),n in sorted(C((e["act"], str(e.get("outcome"))) for e in ev).items()): print(f"{a:20} {o:20} {n}")
print("\n== actor role x act ==")
for (r,a),n in sorted(C((str(e.get("actor",{}).get("role")), e["act"]) for e in ev).items()): print(f"{r:20} {a:20} {n}")
print("\n== top-level keys by act ==")
keys = collections.defaultdict(C)
for e in ev:
    for k in e: 
        if not k.startswith("_"): keys[e["act"]][k]+=1
for a in sorted(keys): print(a, dict(keys[a]))
print("\n== events by date (UTC) ==")
for d,n in sorted(C(str(e.get("at"))[:10] for e in ev).items()): print(d, n)
print("\n== events by hour ==")
for d,n in sorted(C(str(e.get("at"))[:13] for e in ev).items()): print(d, n)
print("\n== distinct actors ==")
for a,n in C(str(e.get("actor",{}).get("name")) for e in ev).most_common(): print(n, a)
# per slug event count for segments
print("\n== segments with most events ==")
for s,n in C(e["_slug"] for e in ev if e["_kind"]=="segment").most_common(15): print(n, s)
# distinct segments with events
print("segments with events:", len(set(e["_slug"] for e in ev if e["_kind"]=="segment")))
print("items with events:", len(set(e["_slug"] for e in ev if e["_kind"]=="item")))
# recheck outcome × items/ vs items/imported
print("\n== recheck outcome by file location ==")
loc = {}
for p in glob.glob(root+"/items/*.md"): loc[os.path.basename(p)[:-3]] = "items"
for p in glob.glob(root+"/items/imported/*.md"): loc[os.path.basename(p)[:-3]] = "imported"
for (o,l),n in sorted(C((str(e.get("outcome")), loc.get(e["_slug"],"GONE")) for e in ev if e["act"]=="recheck").items()): print(f"{o:15} {l:10} {n}")
# imported files: closed line present?
print("\n== imported files frontmatter closed: ==")
closed = C()
for p in glob.glob(root+"/items/imported/*.md"):
    fm = open(p).read().split("---")[1]
    closed["closed:" in fm] += 1
print(dict(closed))
# imported files lacking closed but with recheck event that closes
rechecked = collections.defaultdict(list)
for e in ev:
    if e["act"]=="recheck": rechecked[e["_slug"]].append(e.get("outcome"))
n_mismatch=0; n_noevent=0
for p in glob.glob(root+"/items/imported/*.md"):
    s = os.path.basename(p)[:-3]
    fm = open(p).read().split("---")[1]
    if "closed:" not in fm:
        if s in rechecked: n_mismatch+=1
        else: n_noevent+=1
print("imported w/o closed: but rechecked:", n_mismatch, " imported w/o closed and never rechecked:", n_noevent)
# items/ (held) : owner distribution
print("\n== held items owner ==")
own=C(); prov=C()
for p in glob.glob(root+"/items/*.md"):
    fm = yaml.safe_load(open(p).read().split("---")[1])
    own[str(fm.get("owner"))]+=1; prov[str(fm.get("provenance"))]+=1
for o,n in own.most_common(): print(n,o)
print("provenance:", dict(prov))
# imported items: source file distribution
print("\n== imported items by source file ==")
src=C()
for p in glob.glob(root+"/items/imported/*.md"):
    fm = yaml.safe_load(open(p).read().split("---")[1])
    src[str(fm.get("source")).split(":")[0]]+=1
for o,n in src.most_common(): print(n,o)
# raise events: how many distinct items raised; sources
print("\n== raise: distinct items raised, raises per item ==")
r = C(e["_slug"] for e in ev if e["act"]=="raise")
print("distinct:", len(r), "max per item:", r.most_common(3))
print("raise actors:", C(str(e.get("actor",{}).get("name")) for e in ev if e["act"]=="raise").most_common(8))
