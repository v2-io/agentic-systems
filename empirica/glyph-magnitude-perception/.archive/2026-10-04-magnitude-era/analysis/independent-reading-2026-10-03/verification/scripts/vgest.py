import collections, itertools, sys
from vload import *
import vsgest as _v; tau = _v.tau
FR = ["opus55","sonnet55","sonnet5","haiku45","grok46","gpt56terra","gemini31pro","gemini38flash"]
G = {}
for rid in runs("gestalt-gestalt-"):
    j = rid.split("-", 3)[3]
    G[j] = gestalt_answers(rid)
want = sys.argv[1:] or ["dice","noise-0","noise-1","noise-2","noise-3","unfold","risebar","drain","elab-n","elab-s","elab-l"]
for seq in want:
    print("=====", seq, STIM[[p for p,s in STIM.items() if s.get("set")=="gestalt" and s.get("seq")==seq][0]]["intended"])
    for j in FR + [x for x in G if x not in FR]:
        out = []
        for p, s in STIM.items():
            if s.get("set") != "gestalt" or s.get("seq") != seq: continue
            a = G[j].get(p)
            if not a: out.append((s["shuffle"], "MISSING")); continue
            if a["kind"] == "order":
                t, n = tau(a["order"], s["intended"]); out.append((s["shuffle"], f"τ{abs(t) if t is not None else float('nan'):.2f} cov{n}/{len(s['intended'])} {''.join(a['order'])}" + (f" X:{''.join(a['extra'])}" if a.get('extra') else "")))
            else: out.append((s["shuffle"], a["kind"] + " " + a["raw"].strip()[:30].replace("\n"," ")))
        print(f"  {j:14s}", " | ".join(x[1] for x in sorted(out)))
