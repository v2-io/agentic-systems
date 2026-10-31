#!/usr/bin/env python3
"""Tables for the I.10 account from a measure.py run.

    python3 -I summarize.py data/<label>   (reads <label>-claims.tsv and <label>-places.tsv)

Prints markdown. Groups: 'random' (all random:* strata pooled), 'purposive', 'census'.
"""
import collections
import csv
import statistics
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import i10lib as L  # noqa: E402

pre = sys.argv[1]
claims = list(csv.DictReader(open(pre + "-claims.tsv"), delimiter="\t"))
places = list(csv.DictReader(open(pre + "-places.tsv"), delimiter="\t"))


def group(st):
    return "census" if not st else st.split(":")[0]


refs = list(dict.fromkeys(c["ref"] for c in claims))
sha = {c["ref"]: c["sha"] for c in claims}
gof = {(c["ref"], c["slug"]): group(c["sample"]) for c in claims}
per = collections.defaultdict(lambda: collections.Counter())
for c in claims:
    k = (c["ref"], c["slug"])
    d = per[k]
    d["signal_b"] = int(c["body_words"]) + int(c["ledger_block_words"])
    d["signal_s"] = int(c["body_words"]) + int(c["ledger_section_words"])
    d["own_wn"] = int(c["own_wn_words"])
    d["ledger_n"] = int(c["ledger_n"])
    d["ledger_keyed"] = int(c["ledger_keyed"])
for p in places:
    if p["class"] not in L.NOISE:
        continue
    d = per[(p["ref"], p["slug"])]
    b, s, st = int(p["block_words"]), int(p["section_words"]), p["accounted"]
    d["places"] += 1
    d["places_" + st] += 1
    if p["class"] == "msc-effort":
        d["places_effort"] += 1
    for u, w in (("b", b), ("s", s)):
        d["raw_" + u] += w
        if st in "UHD":
            d["strict_" + u] += w
        if st in "UH":
            d["drain_" + u] += w

for g in ("random", "purposive", "census"):
    rows = {r: [per[k] for k in per if k[0] == r and gof[k] == g] for r in refs}
    if not any(rows.values()):
        continue
    n = len(rows[refs[0]])
    print(f"\n### {g} ({n} claims)\n")
    print("| quantity | " + " | ".join(f"{r} (`{sha[r]}`)" for r in refs) + " |")
    print("|---|" + "---|" * len(refs))

    def line(label, f, med=True):
        cells = []
        for r in refs:
            vals = [f(d) for d in rows[r]]
            tot = sum(vals)
            cells.append(f"{tot:,}" + (f" (median {statistics.median(vals):,.0f})" if med else ""))
        print(f"| {label} | " + " | ".join(cells) + " |")

    line("noise places (live, outside body and ledger)", lambda d: d["places"])
    line("  of which the effort's own residue (`msc/inside-out-2026-10/`)", lambda d: d["places_effort"])
    line("  pointed to by a ledger record about the claim (L)", lambda d: d["places_L"], False)
    line("  named only in a drain account (D)", lambda d: d["places_D"], False)
    line("  named only by the segment file itself (H)", lambda d: d["places_H"], False)
    line("  named nowhere (U)", lambda d: d["places_U"], False)
    line("ledger records mentioning the claim (keyed to it)", lambda d: d["ledger_n"], False)
    for u, nm in (("b", "block"), ("s", "section")):
        line(f"[{nm}] signal words: body + ledger", lambda d, u=u: d["signal_" + u])
        line(f"[{nm}] noise words, every place + own WN", lambda d, u=u: d["raw_" + u] + d["own_wn"])
        line(f"[{nm}] must-read, ledger discounts (strict)", lambda d, u=u: d["strict_" + u] + d["own_wn"])
        line(f"[{nm}] must-read, ledger and drain discount", lambda d, u=u: d["drain_" + u] + d["own_wn"])
        for lab, key in (("raw", "raw_"), ("strict", "strict_"), ("with drain", "drain_")):
            cells = []
            for r in refs:
                sig = sum(d["signal_" + u] for d in rows[r])
                noi = sum(d[key + u] + d["own_wn"] for d in rows[r])
                shares = [d["signal_" + u] / max(1, d["signal_" + u] + d[key + u] + d["own_wn"]) for d in rows[r]]
                cells.append(f"{sig / max(1, sig + noi):.2f} (median {statistics.median(shares):.2f})")
            print(f"| [{nm}] signal share, {lab} | " + " | ".join(cells) + " |")

# places by class
print("\n### noise places by class, random and purposive pooled with census excluded\n")
cls = collections.Counter()
for p in places:
    if p["class"] in L.NOISE and gof[(p["ref"], p["slug"])] != "census":
        cls[(p["class"], p["ref"], p["accounted"])] += 1
classes = sorted({c for c, _, _ in cls})
print("| class | " + " | ".join(refs) + f" | at {refs[-1]}: L / D / H / U |")
print("|---|" + "---|" * (len(refs) + 1))
for c in classes:
    tots = [sum(v for (cc, r, _), v in cls.items() if cc == c and r == rr) for rr in refs]
    last = " / ".join(str(cls[(c, refs[-1], k)]) for k in "LDHU")
    print(f"| {c} | " + " | ".join(map(str, tots)) + f" | {last} |")
