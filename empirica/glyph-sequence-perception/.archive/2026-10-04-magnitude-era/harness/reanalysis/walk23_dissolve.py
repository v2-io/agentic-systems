#!/usr/bin/env python3
"""Re-derive the pilot's demand-characteristics number (walk2 -> walk3, same sheets)
from the raw workflow outputs, and characterize WHICH directed edges dissolved to ⟂.

walk2 = w2ojawgjt.json (response set: glyph / ≈), walk3 = wlj4rajuj.json (glyph / ≈ / ⟂).
Both used walk2-key-*.json (pair -> two presentations on one judge's sheet).
A pair is 'consistent-directed' when both presentations name the same glyph.

Run from anywhere:  python3 walk23_dissolve.py
"""
import json, pathlib, unicodedata
from collections import defaultdict, Counter

J = pathlib.Path(__file__).resolve().parents[2] / "data" / "judgments-v0"

def load(fname):
    data = json.load(open(J / fname))["result"]["walk"]
    out = {}  # frozenset pair -> (verdict, more)
    for entry in data:
        key = json.load(open(J / f"walk2-key-{entry['chunk']}.json"))
        amap = {a["id"]: a["more"] for a in (entry["answers"] or [])}
        bypair = defaultdict(list)
        for s in key["sheet"]:
            bypair[s["pair"]].append(s)
        for pk, pres in bypair.items():
            picks = []
            for s in pres:
                a = amap.get(s["id"])
                if a is None:
                    picks = None; break
                if a not in (s["a"], s["b"], "≈", "⟂"):
                    a = (s["a"] if s["a"] in a else s["b"] if s["b"] in a
                         else "≈" if "≈" in a else "⟂" if "⟂" in a else None)
                picks.append(a)
            if not picks or len(picks) != 2 or None in picks:
                continue
            g = frozenset((pres[0]["a"], pres[0]["b"]))
            if len(g) != 2:
                continue
            p0, p1 = picks
            if p0 == p1 and p0 not in ("≈", "⟂"):
                out[(entry["chunk"], pk)] = ("dir", p0, g)
            elif p0 == p1 == "≈":
                out[(entry["chunk"], pk)] = ("tie", None, g)
            elif p0 == p1 == "⟂":
                out[(entry["chunk"], pk)] = ("perp", None, g)
            else:
                out[(entry["chunk"], pk)] = ("mixed", (p0, p1), g)
    return out

w2 = load("w2ojawgjt.json")
w3 = load("wlj4rajuj.json")
print("walk2 verdicts:", Counter(v[0] for v in w2.values()))
print("walk3 verdicts:", Counter(v[0] for v in w3.values()))

common = set(w2) & set(w3)
d2 = [k for k in common if w2[k][0] == "dir"]
fate = Counter()
for k in d2:
    v3 = w3[k]
    if v3[0] == "dir":
        fate["dir-same" if v3[1] == w2[k][1] else "dir-flipped"] += 1
    else:
        fate[v3[0]] += 1
print(f"\nwalk2 consistent-directed pairs also scored in walk3: {len(d2)}")
for k, n in fate.most_common():
    print(f"  -> walk3 {k}: {n} ({n/len(d2):.1%})")

# characterize dissolved vs surviving by Unicode block proxy (same block vs cross-block)
def block(ch):
    cp = ord(ch[0])
    try:
        import subprocess
    except Exception:
        pass
    return cp >> 7  # coarse 128-codepoint page as a structure-blind proxy

def cat(ch):
    return unicodedata.category(ch[0])

same_page = Counter(); n_by = Counter()
for k in d2:
    a, b = tuple(w2[k][2])
    sp = block(a) == block(b)
    v3 = w3[k][0]
    n_by[sp] += 1
    if v3 == "dir":
        same_page[sp] += 1
print("\nsurvival (still directed in walk3) by same-128-codepoint-page proxy:")
for sp in (True, False):
    print(f"  same_page={sp}: {same_page[sp]}/{n_by[sp]} = {same_page[sp]/max(n_by[sp],1):.0%}")

print("\nsurviving directed edges (walk2 & walk3 agree):")
print("  ", " ".join(f"{''.join(sorted(w2[k][2]-{w2[k][1]}))}<{w2[k][1]}" for k in d2 if w3[k][0]=='dir' and w3[k][1]==w2[k][1]))
print("\nsample of dissolved edges (walk2 directed -> walk3 ⟂):")
diss = [k for k in d2 if w3[k][0] == "perp"]
print("  ", " ".join(f"{''.join(sorted(w2[k][2]-{w2[k][1]}))}<{w2[k][1]}" for k in diss[:200]))

print("\nsame-page walk2-directed pairs NOT surviving as same-direction in walk3:")
for k in d2:
    a, b = tuple(w2[k][2])
    if block(a) == block(b) and not (w3[k][0] == "dir" and w3[k][1] == w2[k][1]):
        lo = ''.join(w2[k][2] - {w2[k][1]})
        print(f"   {lo}<{w2[k][1]}  walk3={w3[k][0]} {w3[k][1] or ''}")
print("\nflipped (walk3 directed opposite to walk2):")
for k in d2:
    if w3[k][0] == "dir" and w3[k][1] != w2[k][1]:
        lo = ''.join(w2[k][2] - {w2[k][1]})
        print(f"   walk2 {lo}<{w2[k][1]}   walk3 more={w3[k][1]}")
