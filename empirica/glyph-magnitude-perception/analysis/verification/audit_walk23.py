#!/usr/bin/env python3
"""Independent re-parse of walk2 (w2ojawgjt) and walk3 (wlj4rajuj) for the 2026-10-03 audit.

Written from scratch (does not import harness/reanalysis/walk23_dissolve.py) so that agreement
is evidence, not echo. Read-only over data/; prints only.
"""
import json, pathlib, unicodedata
from collections import Counter, defaultdict

EXP = pathlib.Path(__file__).resolve().parents[2]
J = EXP / "data" / "judgments-v0"

def raw(fname):
    """-> {(chunk, pair): [(a, b, answer_or_None), (a, b, answer_or_None)]}"""
    out = {}
    for e in json.load(open(J / fname))["result"]["walk"]:
        key = json.load(open(J / f"walk2-key-{e['chunk']}.json"))
        ans = {a["id"]: a["more"] for a in (e["answers"] or [])}
        dup = [i for i, n in Counter(a["id"] for a in (e["answers"] or [])).items() if n > 1]
        if dup:
            print(f"  {fname} chunk {e['chunk']}: duplicate answer ids {dup}")
        by = defaultdict(list)
        for s in key["sheet"]:
            by[s["pair"]].append((s["a"], s["b"], ans.get(s["id"])))
        for p, pres in by.items():
            out[(e["chunk"], p)] = pres
    return out

def norm(a, b, x):
    if x is None: return "MISSING"
    if x in (a, b, "≈", "⟂"): return x
    return "OTHER:" + repr(x)

def verdict(pres):
    (a, b, x0), (_, _, x1) = pres
    p0, p1 = norm(a, b, x0), norm(a, b, x1)
    if "MISSING" in (p0, p1) or p0.startswith("OTHER") or p1.startswith("OTHER"):
        return ("unparsed", (p0, p1))
    if p0 == p1:
        return ({"≈": "tie", "⟂": "perp"}.get(p0, "dir"), p0)
    return ("mixed", tuple(sorted((p0, p1))))

for name, f in (("walk2", "w2ojawgjt.json"), ("walk3", "wlj4rajuj.json")):
    R = raw(f)
    V = {k: verdict(p) for k, p in R.items()}
    print(f"{name}: {len(R)} pairs; verdicts {Counter(v[0] for v in V.values())}")
    others = Counter(x for p in R.values() for (a, b, x) in p if norm(a, b, x).startswith(("OTHER", "MISSING")))
    print(f"  non-exact answers: {dict(others)}")
    # mixed breakdown by kind
    kinds = Counter()
    for v in V.values():
        if v[0] == "mixed":
            s = set(v[1])
            kind = ("⟂/≈" if s == {"⟂", "≈"} else
                    "glyph/⟂" if "⟂" in s else "glyph/≈" if "≈" in s else "glyphA/glyphB")
            kinds[kind] += 1
    print(f"  mixed by kind: {dict(kinds)}")
    globals()[name] = V

common = set(walk2) & set(walk3)
d2 = [k for k in common if walk2[k][0] == "dir"]
fate = Counter()
detail = defaultdict(list)
for k in d2:
    v3 = walk3[k]
    lab = v3[0] if v3[0] != "dir" else ("dir-same" if v3[1] == walk2[k][1] else "dir-flip")
    fate[lab] += 1
    detail[lab].append((k, v3))
print(f"\nwalk2-dir pairs: {len(d2)} -> {dict(fate)}")
print("  the mixed ones:", [v for _, v in detail["mixed"]])
print("  the tie ones:", [k for k, _ in detail["tie"]])
# record says 426 dissolved; candidates for the +1: a walk3 mixed containing ⟂ with no glyph
print("  walk2-dir -> walk3 mixed containing ⟂:", sum(1 for _, v in detail["mixed"] if "⟂" in v[1]))

# survival split by 128-codepoint page, same-direction vs any-direction
def page(g): return ord(g[0]) >> 7
R2 = raw("w2ojawgjt.json")
same_any = Counter(); same_dir = Counter(); n = Counter()
for k in d2:
    a, b, _ = R2[k][0]
    sp = page(a) == page(b)
    n[sp] += 1
    same_any[sp] += walk3[k][0] == "dir"
    same_dir[sp] += walk3[k][0] == "dir" and walk3[k][1] == walk2[k][1]
for sp in (True, False):
    print(f"  same_page={sp}: any-direction survival {same_any[sp]}/{n[sp]}, same-direction {same_dir[sp]}/{n[sp]}")

# flips, with UCD numeric values
print("\nflips (walk2 winner -> walk3 winner), with unicodedata.numeric:")
for k, v3 in detail["dir-flip"]:
    a, b, _ = R2[k][0]
    nv = {g: unicodedata.numeric(g, None) for g in (a, b)}
    print(f"   walk2 more={walk2[k][1]}  walk3 more={v3[1]}  numeric={nv}")
