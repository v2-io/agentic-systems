# Derive the empirical state machine (states, transitions, counts) per record kind from the vsect trail.
import glob, collections, yaml, json
import sys; root = sys.argv[1] if len(sys.argv)>1 else "."; C=collections.Counter
ev=[]
for p in glob.glob(root+"/.vsect/events/*/*/*.yaml"):
    d=yaml.safe_load(open(p)); d["_kind"]=p.split("/events/")[1].split("/")[0]; ev.append(d)
ev.sort(key=lambda e:e["at"])
# ---- items ----
items={}
prov={}
for p in glob.glob(root+"/items/*.md")+glob.glob(root+"/items/imported/*.md"):
    fm=yaml.safe_load(open(p).read().split("---")[1]); slug=p.split("/")[-1][:-3]
    prov["item:"+slug]= "imported" if fm.get("provenance")=="imported" else "noted"
T=C(); state={}
for rid,pv in prov.items(): state[rid]=pv; T[("SOURCE", pv)]+=1
item_closed=set()
for e in ev:
    if e["_kind"]!="item": continue
    rid=e["about"]; s=state.get(rid,"?")
    if e["act"]=="recheck":
        o=e["outcome"]; ns="held" if o=="holds" else f"closed:{o}"
        T[(s,ns)]+=1; state[rid]=ns
        if o!="holds": item_closed.add(rid)
    elif e["act"]=="close":
        ns=f"closed:{e['outcome']}"; T[(s,ns)]+=1; state[rid]=ns; item_closed.add(rid)
    elif e["act"]=="raise":
        T[(s,s+" (raised)")]+=1
    elif e["act"]=="place-finding":
        T[(s,s+" (finding placed on item)")]+=1
print("== ITEM transitions ==")
for k,n in sorted(T.items(), key=lambda x:-x[1]): print(f"{n:5}  {k[0]} -> {k[1]}")
print("final item states:", C(state.values()))
raise_on_closed=sum(1 for e in ev if e["_kind"]=="item" and e["act"]=="raise" and e["about"] in item_closed)
print("raises onto items that ended closed:", raise_on_closed, "of", sum(1 for e in ev if e["_kind"]=="item" and e["act"]=="raise"))
# ---- findings ----
F=C(); placed={}
for e in ev:
    if e["act"]=="place-finding": placed[e["finding"]]="open"; F[("review item (take)","finding:open")]+=1
    if e["act"]=="review-finding":
        f=e["finding"]; F[(f"finding:{placed.get(f,'?')}", f"finding:{e['outcome']}")]+=1; placed[f]=e["outcome"]
    if e["act"]=="dispose-finding": F[("finding:open","finding:disposed")]+=1
print("\n== FINDING transitions ==")
for k,n in sorted(F.items(), key=lambda x:-x[1]): print(f"{n:5}  {k[0]} -> {k[1]}")
print("findings final:", C(placed.values()))
# ---- checks (securing events) ----
S=C()
SEC=("rederive","read-check","run","instantiate","read")
indep_roles=lambda r: ("integrator" if r and "integrator" in r else ("author" if r and ("author" in r or "adopter" in r or "B.1" in r) else "independent"))
for e in ev:
    if e["act"] in SEC:
        role=indep_roles(e["actor"].get("role"))
        S[(f"check recorded by {role}", f"outcome:{e['outcome']}")]+=1
        if e["outcome"] in ("broken","narrowed"): S[(f"outcome:{e['outcome']}","finding:open (auto)")]+=1
print("\n== CHECK transitions (recording) ==")
for k,n in sorted(S.items(), key=lambda x:-x[1]): print(f"{n:5}  {k[0]} -> {k[1]}")
# per-line confirmed counts by role class
L=C()
for e in ev:
    if e["act"] in SEC and e["outcome"]=="confirmed": L[(e.get("line"), indep_roles(e["actor"].get("role")))]+=1
print("confirmed by line x role-class:", dict(L))
# ---- segment versions ----
V=C()
for e in ev:
    if e["act"]=="revise": V[("version v_i", f"version v_i+1 [{e.get('change')}]")]+=1
    if e["act"]=="confirm-rewording": V[(f"pair pending second mind", f"pair {e['outcome']} [{e.get('scope') if isinstance(e.get('scope'),str) else 'scoped'}]")]+=1
    if e["act"]=="refute": V[("live","refuted")]+=1
    if e["act"]=="supersede": V[("refuted/live","superseded")]+=1
print("\n== SEGMENT/VERSION transitions ==")
for k,n in sorted(V.items(), key=lambda x:-x[1]): print(f"{n:5}  {k[0]} -> {k[1]}")
# questions
Q=C(); qs=len(glob.glob(root+"/questions/*.md"))
Q[("SOURCE","question:open")]=qs
for e in ev:
    if e["_kind"]=="question" and e["act"]=="answer": Q[("question:open","question:answered")]+=1
    if e["_kind"]=="question" and e["act"]=="raise": Q[("question:open","question:open (raised)")]+=1
print("\n== QUESTION transitions ==")
for k,n in Q.items(): print(f"{n:5}  {k[0]} -> {k[1]}")
# reviews
R=C()
for e in ev:
    if e["act"]=="take": R["reviews taken"]+=1; R["items in taken reviews"]+=len(e.get("items") or [])
print("\nreviews:", dict(R))
# corrections
print("correct events by kind:", C(e["_kind"] for e in ev if e["act"]=="correct"))
