#!/usr/bin/env python3
"""Summarize probe results: per-sequence and per-family recoverability, immediacy
proxies (instinct accuracy, instinct-think gap), consistency, latency."""
import json, sys
from collections import defaultdict

rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip() and l.startswith("{")]

def acc(rs):
    v = [r["correct"] for r in rs if r["ans"]]
    return sum(v) / len(v) if v else float("nan")

def consistency(rs):
    # fraction of pairs whose 3 samples all agree
    by = defaultdict(list)
    for r in rs:
        by[(r["a"], r["b"])].append(r["ans"])
    ok = [len(set(a)) == 1 for a in by.values() if len(a) > 1]
    return sum(ok) / len(ok) if ok else float("nan")

groups = defaultdict(list)
for r in rows:
    groups[(r["seq"], r["family"])].append(r)

print(f"{'sequence':<16}{'family':<10}{'inst':>6}{'think':>7}{'gap':>7}{'cons':>6}{'lat-i':>7}{'lat-t':>7}")
table = []
for (seq, fam), rs in groups.items():
    inst = [r for r in rs if r["mode"] == "instinct"]
    thnk = [r for r in rs if r["mode"] == "think"]
    ai, at = acc(inst), acc(thnk)
    li = sum(r["latency"] for r in inst) / max(len(inst), 1)
    lt = sum(r["latency"] for r in thnk) / max(len(thnk), 1)
    table.append((seq, fam, ai, at, at - ai, consistency(inst), li, lt))
for t in sorted(table, key=lambda x: -x[2]):
    print(f"{t[0]:<16}{t[1]:<10}{t[2]:>6.0%}{t[3]:>7.0%}{t[4]:>+7.0%}{t[5]:>6.0%}{t[6]:>7.2f}{t[7]:>7.2f}")

print("\nBy family:")
fams = defaultdict(list)
for r in rows: fams[r["family"]].append(r)
for fam, rs in sorted(fams.items(), key=lambda kv: -acc([r for r in kv[1] if r["mode"]=="instinct"])):
    inst = [r for r in rs if r["mode"] == "instinct"]; thnk = [r for r in rs if r["mode"] == "think"]
    print(f"  {fam:<10} instinct {acc(inst):.0%}  think {acc(thnk):.0%}  gap {acc(thnk)-acc(inst):+.0%}")

print("\nBy gap distance (instinct mode):")
byg = defaultdict(list)
for r in rows:
    if r["mode"] == "instinct": byg[r["gap"]].append(r)
for g in sorted(byg): print(f"  gap {g}: {acc(byg[g]):.0%}  (n={len(byg[g])})")
