#!/usr/bin/env python3
"""Tables for the I.10 account from a measure.py run.

    python3 -I summarize.py data/<label>   (reads <label>-claims.tsv and <label>-places.tsv)

Prints markdown, per group ('random' = all random:* strata pooled, 'purposive', 'census'):
the places and their accounted states, then total reading and signal share under each
discount variant, at every ref, plus the last ref with this effort's residue removed
(the state I.8 aims at). METHOD.md defines every term.
"""
import collections
import csv
import os
import statistics
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i10lib as L  # noqa: E402

# discount variants: which accounted states a reader may skip
VARIANTS = [("raw (nothing discounts)", ""),
            ("strict (ledger discounts)", "L"),
            ("ledger + indexes and trackers", "LT"),
            ("ledger + drain accounts", "LD"),
            ("ledger + drain + indexes", "LDT")]

pre = sys.argv[1]
claims = list(csv.DictReader(open(pre + "-claims.tsv"), delimiter="\t"))
places = list(csv.DictReader(open(pre + "-places.tsv"), delimiter="\t"))
refs = list(dict.fromkeys(c["ref"] for c in claims))
sha = {c["ref"]: c["sha"] for c in claims}
grp = {(c["ref"], c["slug"]): ("census" if not c["sample"] else c["sample"].split(":")[0]) for c in claims}

# per claim: signal and own-WN words; per (state, effort?) place counts and words
sig = {}
own = {}
pw = collections.defaultdict(collections.Counter)
plist = collections.defaultdict(list)
for c in claims:
    k = (c["ref"], c["slug"])
    sig[k] = {"b": int(c["body_words"]) + int(c["ledger_block_words"]),
              "s": int(c["body_words"]) + int(c["ledger_section_words"])}
    own[k] = int(c["own_wn_words"])
    pw[k]["ledger_n"] = int(c["ledger_n"])
    pw[k]["ledger_keyed"] = int(c["ledger_keyed"])
for p in places:
    if p["class"] not in L.NOISE:
        continue
    k = (p["ref"], p["slug"])
    eff = "E" if p["class"] == "msc-effort" else "N"
    st = p["accounted"][0]
    pw[k]["n" + st + eff] += 1
    plist[k].append((p["accounted"], eff, int(p["block_words"]), int(p["section_words"])))


def must(k, u, disc, drop_effort):
    """own WN + every noise place that no record in `disc` names (dropping effort residue if asked)."""
    tot = own[k]
    for flags, eff, b, s_ in plist[k]:
        if drop_effort and eff == "E":
            continue
        if any(f in disc for f in flags):
            continue
        tot += b if u == "b" else s_
    return tot


for g in ("random", "purposive", "census"):
    keys = {r: [k for k in sig if k[0] == r and grp[k] == g] for r in refs}
    if not keys[refs[0]]:
        continue
    print(f"\n### {g} ({len(keys[refs[0]])} claims)\n")
    print("| places | " + " | ".join(f"{r} (`{sha[r]}`)" for r in refs) + " |")
    print("|---|" + "---|" * len(refs))

    def cnt(label, f):
        cells = []
        for r in refs:
            v = [f(pw[k]) for k in keys[r]]
            cells.append(f"{sum(v):,} (median {statistics.median(v):,.0f})")
        print(f"| {label} | " + " | ".join(cells) + " |")

    cnt("noise places (live, outside body and ledger)", lambda d: sum(d["n" + s + e] for s in "LDTHU" for e in "EN"))
    cnt("of which this effort's residue (`msc/inside-out-2026-10/`)", lambda d: sum(d["n" + s + "E"] for s in "LDTHU"))
    for s, lab in (("L", "named by a ledger record about the claim (L)"), ("D", "else named by a drain account (D)"),
                   ("T", "else named by an index or tracker file (T)"), ("H", "else named by the segment file (H)"),
                   ("U", "named nowhere (U)")):
        cnt(lab, lambda d, s=s: d["n" + s + "E"] + d["n" + s + "N"])
    cnt("ledger records mentioning the claim", lambda d: d["ledger_n"])
    cnt("of which keyed to it", lambda d: d["ledger_keyed"])

    last = refs[-1]
    cols = [(r, False) for r in refs] + [(last, True)]
    hdr = [f"{r}" for r in refs] + [f"{last}, effort residue removed"]
    for u, unit in (("b", "block"), ("s", "section")):
        print(f"\n| total reading, {unit} unit (signal + must-read) | " + " | ".join(hdr) + " |")
        print("|---|" + "---|" * len(cols))
        for lab, disc in VARIANTS:
            cells = []
            for r, drop in cols:
                s_ = sum(sig[k][u] for k in keys[r])
                m_ = sum(must(k, u, disc, drop) for k in keys[r])
                cells.append(f"{s_ + m_:,} (share {s_ / max(1, s_ + m_):.2f})")
            print(f"| {lab} | " + " | ".join(cells) + " |")

print("\n### noise places by class, random and purposive pooled\n")
cls = collections.Counter()
for p in places:
    if p["class"] in L.NOISE and grp[(p["ref"], p["slug"])] != "census":
        cls[(p["class"], p["ref"], p["accounted"][0])] += 1
classes = sorted({c for c, _, _ in cls})
print("| class | " + " | ".join(refs) + " | " + " | ".join(f"{r}: L / D / T / H / U" for r in refs) + " |")
print("|---|" + "---|" * (2 * len(refs)))
for c in classes:
    tots = [sum(v for (cc, r, _), v in cls.items() if cc == c and r == rr) for rr in refs]
    st = [" / ".join(str(cls[(c, r, k)]) for k in "LDTHU") for r in refs]
    print(f"| {c} | " + " | ".join(map(str, tots)) + " | " + " | ".join(st) + " |")
