#!/usr/bin/env python3
"""Independent recomputation of the feature-correlate table (doc §2) for the 2026-10-03 audit.

Own edge extraction (does not import harness/reanalysis/feature_correlates_pilot.py), plus checks
the original does not make: duplicate glyph pairs across triads, Wilson intervals, the UCD value
source cross-checked against Python's unicodedata, cross-font ink comparisons, and (for 3B) how many
'consistent' edges rest on responses that echoed both glyphs. Read-only over data/; prints only.
"""
import csv, json, math, pathlib, unicodedata
from collections import Counter, defaultdict

csv.field_size_limit(10**9)
EXP = pathlib.Path(__file__).resolve().parents[2]
J = EXP / "data" / "judgments-v0"
UTF = pathlib.Path.home() / "src/arch/firmatum/utils/utf"

INK, FACE, CELLS = {}, {}, {}
for r in csv.DictReader(open(UTF / "bmp-metrics-ghostty.tsv"), delimiter="\t", quoting=csv.QUOTE_NONE):
    try:
        INK[r["char"]] = float(r["packed_density"]); FACE[r["char"]] = r["used_face"]; CELLS[r["char"]] = r["cells"]
    except (ValueError, KeyError):
        pass
VAL_ALL, VAL_UCD = {}, {}   # numeric_value as the original script reads it / gated on ucd_numeric == yes
for r in csv.DictReader(open(UTF / "axes/data/unicode-axes.tsv"), delimiter="\t", quoting=csv.QUOTE_NONE):
    v = (r.get("numeric_value") or "").strip()
    if v:
        try:
            n, _, d = v.partition("/"); x = float(n) / float(d or 1)
        except ValueError:
            continue
        VAL_ALL[r["char"]] = x
        if r.get("ucd_numeric") == "yes": VAL_UCD[r["char"]] = x
VAL = VAL_ALL

def wilson(k, n, z=1.96):
    if not n: return (float("nan"),) * 2
    p = k / n; den = 1 + z * z / n; c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (c - h, c + h)

# ---- edge extraction ------------------------------------------------------------------
def walk_edges(fname, prefix):
    out = []
    for e in json.load(open(J / fname))["result"]["walk"]:
        key = json.load(open(J / f"{prefix}-key-{e['chunk']}.json"))
        ans = {a["id"]: a["more"] for a in (e["answers"] or [])}
        by = defaultdict(list)
        for s in key["sheet"]: by[s["pair"]].append(s)
        for pres in by.values():
            x = [ans.get(s["id"]) for s in pres]
            a, b = pres[0]["a"], pres[0]["b"]
            if len(x) == 2 and x[0] == x[1] and x[0] in (a, b):
                out.append(((b if x[0] == a else a), x[0], None))
    return out

def triad_edges(fname):
    T = json.load(open(J / "walk5-triads.json"))
    rel = defaultdict(dict)  # (chunk) -> (a,b) per triad
    for e in json.load(open(J / fname))["result"]["walk"]:
        key = json.load(open(J / f"walk5-key-{e['chunk']}.json"))
        ans = {a["id"]: a["more"] for a in (e["answers"] or [])}
        for s in key:
            if s["id"] in ans: rel[(e["chunk"], s["triad"])][(s["a"], s["b"])] = ans[s["id"]]
    out = []
    for ti in range(len(T)):
        p = ti % 6
        r1, r2 = rel.get((2 * p, ti), {}), rel.get((2 * p + 1, ti), {})
        for (a, b), m in r1.items():
            if m in (a, b) and r2.get((b, a)) == m:
                out.append(((b if m == a else a), m, ti))
    return out

def edges_3b():
    rows = [json.loads(l) for l in open(EXP / "pilot/results5-llama3.2_3b.jsonl")]
    by = defaultdict(dict)
    for r in rows: by[r["triad"]][(r["a"], r["b"])] = r
    out = []; both_echo = 0
    for t, rel in by.items():
        for (a, b), r in rel.items():
            r2 = rel.get((b, a))
            if r2 and a < b and r["more"] in (a, b) and r2["more"] == r["more"]:
                m = r["more"]
                echo = (a in r["raw"] and b in r["raw"]) or (a in r2["raw"] and b in r2["raw"])
                both_echo += echo
                out.append(((b if m == a else a), m, ("echo-both" if echo else "clean")))
    return out, both_echo

def tally(edges, dedup=False):
    if dedup:
        seen = {};
        for l, w, tag in edges: seen.setdefault(frozenset((l, w)), (l, w, tag))
        edges = list(seen.values())
    c = defaultdict(lambda: [0, 0, 0, 0, 0, 0])  # num_n,num_w, ink_n,ink_w, inkSameFace_n,inkSameFace_w
    for l, w, _ in edges:
        k = "both" if (l in VAL and w in VAL) else "neither" if (l not in VAL and w not in VAL) else "one"
        x = c[k]
        if k == "both" and VAL[l] != VAL[w]:
            x[0] += 1; x[1] += VAL[w] > VAL[l]
        if l in INK and w in INK and abs(INK[l] - INK[w]) > 0.005:
            x[2] += 1; x[3] += INK[w] > INK[l]
            if FACE[l] == FACE[w] and CELLS[l] == CELLS[w]:
                x[4] += 1; x[5] += INK[w] > INK[l]
    return c, len(edges)

def fmt(k, n):
    if not n: return "n/a"
    lo, hi = wilson(k, n)
    return f"{k}/{n}={k/n:.0%} [{lo:.0%},{hi:.0%}]"

runs = [("walk2", walk_edges("w2ojawgjt.json", "walk2")), ("walk3", walk_edges("wlj4rajuj.json", "walk2")),
        ("walk4", walk_edges("w6p64psmb.json", "walk4")), ("walk5", triad_edges("wl7e4u1p9.json")),
        ("walk5b", triad_edges("wg09eag3s.json"))]
e3b, n_echo = edges_3b(); runs.append(("3b", e3b))
import sys
if "--ucd" in sys.argv:
    VAL = VAL_UCD
    print("VALUE SOURCE: numeric_value gated on ucd_numeric == yes (letters-as-numerals excluded)")
else:
    print("VALUE SOURCE: numeric_value as read by feature_correlates_pilot.py (includes gematria/Milesian letters)")
for dedup in (False, True):
    print(f"\n=== {'DEDUPLICATED by unordered glyph pair' if dedup else 'as in the doc (edge instances)'} ===")
    for name, E in runs:
        c, n = tally(E, dedup)
        b, ne = c["both"], c["neither"]
        print(f"{name:<7} edges {n:>4} | both-numeric value {fmt(b[1], b[0]):<26} ink {fmt(b[3], b[2]):<24}"
              f"| neither ink {fmt(ne[3], ne[2]):<24} same-face&width ink {fmt(ne[5], ne[4])}")

print(f"\n3B: {len(e3b)} consistent edges; {n_echo} rest on at least one response that contained BOTH glyphs "
      f"(parse took the first-occurring one)")
for tag in ("clean", "echo-both"):
    c, n = tally([e for e in e3b if e[2] == tag])
    b, ne = c["both"], c["neither"]
    print(f"   {tag:<9} edges {n:>4} | value {fmt(b[1], b[0])} | neither ink {fmt(ne[3], ne[2])}")

# pooled 'numeric pairs: ink anti-informative?' over the Sonnet runs (non-independent: walk5/5b share items)
k = n = 0
for name, E in runs[:5]:
    c, _ = tally(E); k += c["both"][3]; n += c["both"][2]
print(f"\nSonnet pooled both-numeric ink-winner rate {fmt(k, n)} (walk5/5b re-use the same triads)")

# UCD value table vs Python unicodedata, over every glyph that appears in any edge
mism = []
for _, E in runs:
    for l, w, _ in E:
        for g in (l, w):
            pv = unicodedata.numeric(g, None) if len(g) == 1 else None
            tv = VAL.get(g)
            if (pv is None) != (tv is None) or (pv is not None and abs(pv - tv) > 1e-9):
                mism.append((g, f"U+{ord(g[0]):04X}", tv, pv))
print("\nUCD value table vs unicodedata (python", unicodedata.unidata_version, ") mismatches:", sorted(set(mism)))

# the both-numeric edges each run got WRONG, for inspection
for name, E in runs:
    wrong = Counter(f"{w}>{l}" for l, w, _ in E if l in VAL and w in VAL and VAL[w] < VAL[l])
    print(f"{name:<7} value-wrong edges: {dict(wrong)}")
