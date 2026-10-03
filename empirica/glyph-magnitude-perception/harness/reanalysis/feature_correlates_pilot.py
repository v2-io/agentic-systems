#!/usr/bin/env python3
"""Post-hoc feature-correlate pass over the pilot's directed edges (exploratory; pilot tier).

Question: when a judge commits to a direction, how often does the winner carry
(a) more measured ink (Ghostty packed_density, BMP only) and (b) a larger UCD numeric value?
And when ink and numeric value point opposite ways, which one wins?

Features come from ~/src/arch/firmatum/utils/utf (measured 2026-08-24; Ghostty face stack;
the model never sees these pixels -- ink here is a human-terminal rendering measurement used
as a candidate correlate, not as the model's input).
"""
import csv, json, pathlib, sys
from collections import defaultdict, Counter

csv.field_size_limit(10**9)
HERE = pathlib.Path(__file__).resolve()
EXP = HERE.parents[2]
J = EXP / "data" / "judgments-v0"
UTF = pathlib.Path.home() / "src/arch/firmatum/utils/utf"

ink = {}; cls = {}
for r in csv.DictReader(open(UTF / "bmp-metrics-ghostty.tsv"), delimiter="\t", quoting=csv.QUOTE_NONE):
    try:
        ink[r["char"]] = float(r["packed_density"]); cls[r["char"]] = r["packed_class"]
    except (ValueError, KeyError):
        pass
num = {}
for r in csv.DictReader(open(UTF / "axes/data/unicode-axes.tsv"), delimiter="\t", quoting=csv.QUOTE_NONE):
    v = r.get("numeric_value") or ""
    if v.strip() and (r.get("ucd_numeric") or "").strip() == "yes":  # UCD values only (audit 2026-10-03)
        try:
            num[r["char"]] = float(eval(v)) if "/" in v else float(v)
        except Exception:
            pass

def edges_walk(fname, keyprefix, keyed_sheet=True):
    """both-orders-consistent directed edges from a pair walk (walk2/3/4 style)."""
    data = json.load(open(J / fname))["result"]["walk"]
    out = []
    for entry in data:
        key = json.load(open(J / f"{keyprefix}-key-{entry['chunk']}.json"))
        amap = {a["id"]: a["more"] for a in (entry["answers"] or [])}
        bypair = defaultdict(list)
        for s in key["sheet"]:
            bypair[s["pair"]].append(s)
        for pres in bypair.values():
            picks = [amap.get(s["id"]) for s in pres]
            if len(picks) == 2 and picks[0] == picks[1] and picks[0] in (pres[0]["a"], pres[0]["b"]):
                w = picks[0]; l = pres[0]["a"] if pres[0]["b"] == w else pres[0]["b"]
                out.append((l, w))
    return out

def edges_triads(fname):
    data = json.load(open(J / fname))["result"]["walk"]
    triads = json.load(open(J / "walk5-triads.json"))
    rel = defaultdict(dict)   # triad -> judge -> (a,b)->more
    for entry in data:
        c = entry["chunk"]; key = json.load(open(J / f"walk5-key-{c}.json"))
        amap = {a["id"]: a["more"] for a in (entry["answers"] or [])}
        for s in key:
            if s["id"] in amap:
                rel[s["triad"]].setdefault(c, {})[(s["a"], s["b"])] = amap[s["id"]]
    out = []
    for ti in range(len(triads)):
        p = ti % 6; j1, j2 = 2*p, 2*p+1
        r1 = rel[ti].get(j1, {}); r2 = rel[ti].get(j2, {})
        for (a, b), m1 in r1.items():
            m2 = r2.get((b, a))
            if m1 in (a, b) and m2 == m1:
                out.append((b if m1 == a else a, m1))
    return out

def edges_3b():
    rows = [json.loads(l) for l in open(EXP / "pilot/results5-llama3.2_3b.jsonl")]
    by = defaultdict(dict)
    for r in rows:
        by[r["triad"]][(r["a"], r["b"])] = r["more"]
    out = []
    for t, rel in by.items():
        for (a, b), m in rel.items():
            m2 = rel.get((b, a))
            if m in (a, b) and m2 == m and a < b:
                out.append((b if m == a else a, m))
    return out

def report(name, edges):
    n_ink = ink_w = 0; n_num = num_w = 0; conf = Counter(); n_same_cls = ink_w_same = 0
    for l, w in edges:
        if l in ink and w in ink and abs(ink[l] - ink[w]) > 0.005:
            n_ink += 1; ink_w += ink[w] > ink[l]
            if cls[l] == cls[w]:
                n_same_cls += 1; ink_w_same += ink[w] > ink[l]
        if l in num and w in num and num[l] != num[w]:
            n_num += 1; num_w += num[w] > num[l]
            if l in ink and w in ink and abs(ink[l] - ink[w]) > 0.005:
                ink_says = ink[w] > ink[l]; num_says = num[w] > num[l]
                if ink_says != num_says:
                    conf["value-won" if num_says else "ink-won"] += 1
    pct = lambda a, b: f"{a}/{b} = {a/b:.0%}" if b else "n/a"
    print(f"{name:<34} edges {len(edges):>4} | winner more ink {pct(ink_w, n_ink):>16} "
          f"(same width-class {pct(ink_w_same, n_same_cls)}) | winner larger value {pct(num_w, n_num):>16} "
          f"| ink-vs-value conflicts {dict(conf)}")

report("walk2 (glyph/≈, forced-ish)", edges_walk("w2ojawgjt.json", "walk2"))
report("walk3 (glyph/≈/⟂ same sheets)", edges_walk("wlj4rajuj.json", "walk2"))
report("walk4 (graded + ⟂, fresh pairs)", edges_walk("w6p64psmb.json", "walk4"))
report("walk5 triads (cross-judge)", edges_triads("wl7e4u1p9.json"))
report("walk5b triads (cross-judge)", edges_triads("wg09eag3s.json"))
report("llama3.2:3b triads (both pres.)", edges_3b())

print("\n-- split by whether the pair carries UCD numeric values (ink-winner rate; value-winner rate)")
def split(name, edges):
    cell = defaultdict(lambda: [0, 0, 0, 0])  # n_ink, ink_w, n_num, num_w
    for l, w in edges:
        k = ("both-numeric" if (l in num and w in num) else
             "neither-numeric" if (l not in num and w not in num) else "one-numeric")
        c = cell[k]
        if l in ink and w in ink and abs(ink[l] - ink[w]) > 0.005:
            c[0] += 1; c[1] += ink[w] > ink[l]
        if k == "both-numeric" and num[l] != num[w]:
            c[2] += 1; c[3] += num[w] > num[l]
    s = []
    for k in ("both-numeric", "one-numeric", "neither-numeric"):
        c = cell[k]
        s.append(f"{k}: ink {c[1]}/{c[0]}" + (f" ({c[1]/c[0]:.0%})" if c[0] else "") +
                 (f", value {c[3]}/{c[2]} ({c[3]/c[2]:.0%})" if c[2] else ""))
    print(f"{name:<34} " + " | ".join(s))
split("walk2", edges_walk("w2ojawgjt.json", "walk2"))
split("walk3", edges_walk("wlj4rajuj.json", "walk2"))
split("walk4", edges_walk("w6p64psmb.json", "walk4"))
split("walk5", edges_triads("wl7e4u1p9.json"))
split("walk5b", edges_triads("wg09eag3s.json"))
split("3b", edges_3b())
