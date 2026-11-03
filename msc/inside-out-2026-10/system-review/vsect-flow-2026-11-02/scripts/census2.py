import os, glob, collections, subprocess, yaml
import sys; root = sys.argv[1] if len(sys.argv)>1 else "."
C = collections.Counter
ev = []
for p in glob.glob(root + "/.vsect/events/*/*/*.yaml"):
    d = yaml.safe_load(open(p)); d["_path"]=p; d["_kind"]=p.split("/events/")[1].split("/")[0]; d["_slug"]=p.split("/events/")[1].split("/")[1]; ev.append(d)
def git(*a): return subprocess.run(["git","-C",root,*a],capture_output=True,text=True).stdout
# 1. recheck/close events: commit that added the event; did that commit touch the item file?
print("== recheck/close events: did the adding commit also touch the item file? ==")
res = C()
sample = []
for e in ev:
    if e["act"] not in ("recheck","close"): continue
    rel = os.path.relpath(e["_path"], root)
    h = git("log","--format=%h","--diff-filter=A","--",rel).split()
    if not h: res[(e["act"], e.get("outcome"), "event-uncommitted")]+=1; continue
    files = git("show","--name-only","--format=","-M",h[0]).split()
    touched = any(f.startswith("items/") and e["_slug"] in f for f in files)
    res[(e["act"], e.get("outcome"), "file-touched" if touched else "events-only")]+=1
    if not touched and len(sample)<6: sample.append((h[0], e["act"], e.get("outcome"), e["_slug"]))
for k,n in sorted(res.items()): print(k,n)
print("sample events-only:", sample)
# 2. sprint-written-text share: securing events and place-findings whose target version is not the record's root (pre-sprint) version
print("\n== securing/finding events on sprint-written text ==")
rev = collections.defaultdict(list)
for e in ev:
    if e["act"]=="revise": rev[e["about"]].append((e["at"], e["from-version"], e["own-version"], e.get("change")))
roots = {}
for rid, L in rev.items():
    owns = {o for _,_,o,_ in L}
    froms = {f for _,f,_,_ in L}
    roots[rid] = froms - owns  # versions that were never produced by a sprint revise = pre-sprint
SEC = ("rederive","read-check","run","instantiate","read")
cnt = C()
for e in ev:
    if e["act"] in SEC or e["act"]=="place-finding":
        about = e["about"]
        tv = e.get("target-version")
        if tv is None and e["act"]=="place-finding":
            # basis carries target version
            b = e.get("basis") or []
            for x in b:
                if isinstance(x,dict) and x.get("id")==about: tv = x.get("version")
        if about not in rev: cls = "no-revise-in-sprint"
        elif tv in roots[about]: cls = "pre-sprint-text"
        else: cls = "sprint-written-text"
        cnt[(e["act"] if e["act"]=="place-finding" else "securing", cls)] += 1
for k,n in sorted(cnt.items()): print(k,n)
# broken/narrowed outcomes on sprint-written text
cnt2 = C()
for e in ev:
    if e["act"] in SEC and e.get("outcome") in ("broken","narrowed"):
        about=e["about"]; tv=e.get("target-version")
        cls = "no-revise" if about not in rev else ("pre-sprint" if tv in roots[about] else "sprint-written")
        cnt2[(e["outcome"],cls)]+=1
print("broken/narrowed by text origin:", dict(cnt2))
# revise change classification
print("\nrevise change:", C(e.get("change") for e in ev if e["act"]=="revise"))
print("revises per segment (top):", C(e["about"] for e in ev if e["act"]=="revise").most_common(8))
print("segments revised:", len(rev))
# 3. questions census
print("\n== questions ==")
qs = glob.glob(root+"/questions/*.md")
closer=C(); concerns_n=C(); askers=C()
for p in qs:
    fm = yaml.safe_load(open(p).read().split("---")[1])
    closer[str(fm.get("closer"))]+=1; c=fm.get("concerns") or []; concerns_n[len(c) if isinstance(c,list) else 1]+=1; askers[str(fm.get("asked-by"))[:40]]+=1
print("n:",len(qs),"closer:",dict(closer),"concerns count:",dict(concerns_n))
print("askers:",askers.most_common(10))
# 4. reviews census
print("\n== reviews ==")
import re
rv = glob.glob(root+"/reviews/*.md")
items_per=C(); roles=C(); kinds=C()
for p in rv:
    t=open(p).read()
    fm = yaml.safe_load(t.split("---")[1])
    roles[str((fm.get("author") or {}).get("role"))]+=1
    n=len(re.findall(r"^## [CF]\d+ \((check|finding)\)", t, re.M)); items_per[n//5*5]+=1
    for m in re.findall(r"^## [CF]\d+ \((check|finding)\)", t, re.M): kinds[m]+=1
print("n:",len(rv),"roles:",dict(roles),"items/review buckets:",dict(sorted(items_per.items())),"item kinds:",dict(kinds))
# finding lifecycle: findings open by role of placer; answered by whom relative to placer
print("\n== finding lifecycle ==")
placed={}; 
for e in ev:
    if e["act"]=="place-finding": placed[e["finding"]]=e
ans=C(); 
for e in ev:
    if e["act"]=="review-finding":
        p=placed.get(e["finding"]); 
        if p: ans[("same-actor" if p["actor"]["name"]==e["actor"]["name"] else "other-actor", "reviser-recorded" if e.get("reviser-recorded") else "")]+=1
        else: ans[("unplaced",)]+=1
print("review-finding vs placer:", dict(ans))
openf=[f for f in placed if f not in {e["finding"] for e in ev if e["act"]=="review-finding" and e.get("outcome")=="answered"}]
print("open findings:",len(openf),"placed:",len(placed))
print("open findings by target top:", C(placed[f]["target"] for f in openf).most_common(10))
print("open findings by placer role:", C(placed[f]["actor"].get("role") for f in openf).most_common())
