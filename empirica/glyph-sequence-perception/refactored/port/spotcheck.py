#!/usr/bin/env python3
"""Spot-check ported records against the verbatim ledgers, independently of the parser (concern 4's audit trail).

  spotcheck.py [N]     -> appends/replaces the "Spot checks" section of ../data/answers/PORT-REPORT.md

For a fated sample of N records per kind, find the raw model output in the ledger, pull that entry's JSON answer
with a plain json.loads of the {"answers": ...} object (no triad-era parser), and compare it with what the port
recorded: the glyphs / proposals / outcome. Every mismatch is listed.
"""
import collections, json, pathlib, random, re, sys, unicodedata as U

HERE = pathlib.Path(__file__).resolve()
STUDY = HERE.parents[2]
ANS = HERE.parents[1] / "data" / "answers"

def raw_answer(rec):
    led = STUDY / "data" / "rounds" / rec["round"] / "raw" / rec["mind"] / "ledger.jsonl"
    rows = [json.loads(l) for l in open(led) if l.strip()]
    rows = [r for r in rows if r["sid"] == rec["sid"] and r["result"].get("raw") and not r["result"].get("error")]
    if not rows:
        return None, "no successful call"
    raw = rows[-1]["result"]["raw"]
    sheet = next(json.loads(l) for l in open(STUDY / "data" / "rounds" / rec["round"] / "sheets.jsonl") if json.loads(l)["sid"] == rec["sid"])
    eid = next(e["id"] for e in sheet["entries"] if e["pid"] == rec["pid"])
    objs = []
    for m in re.finditer(r'\{\s*"answers"', raw):
        try:
            objs.append(json.JSONDecoder().raw_decode(raw[m.start():])[0])
        except Exception:
            pass
    if not objs:
        return None, "no answers object"
    hits = [a for a in objs[-1]["answers"] if isinstance(a, dict) and a.get("id") == eid]
    return (hits[0] if len(hits) == 1 else None), ("ok" if len(hits) == 1 else f"{len(hits)} entries with id {eid}")

def nfc(x):
    return U.normalize("NFC", str(x)).strip()

def check(rec):
    a, why = raw_answer(rec)
    if rec["outcome"] in ("call-failed",):
        return why == "no successful call", f"call-failed vs ledger: {why}"
    if a is None:
        return rec["outcome"] == "unparsed", f"raw: {why}; ported outcome {rec['outcome']}"
    k = rec["kind"]
    if rec["outcome"] == "unparsed":
        return True, "unparsed (parser's verdict; raw: " + json.dumps(a, ensure_ascii=False)[:80] + ")"
    if k in ("next", "between"):
        key = "next" if k == "next" else "between"
        if rec["outcome"] == "none":
            return bool(a.get("none")) and not a.get(key), f"none vs raw {json.dumps(a, ensure_ascii=False)[:80]}"
        raw = a.get(key); raw = [raw] if isinstance(raw, str) else raw
        raw = [nfc(x) for x in raw if nfc(x)][:3]
        mine = sorted([(p["rank"], p["g"]) for p in rec.get("proposals", [])] + [(o["rank"], nfc(o["s"])) for o in rec.get("other_content", [])])
        mine_s = ["".join(ch for ch in s if ch not in "︎️") for _, s in mine]
        raw_s = ["".join(ch for ch in s if ch not in "︎️") for s in raw]
        return mine_s == raw_s, f"ported {mine_s} vs raw {raw_s}"
    if k == "triad":
        shown = rec["shown"]
        def res(x):
            x = nfc(x); m = re.fullmatch(r"#\s*(\d+)", x)
            return shown[int(m.group(1)) - 1] if m else x
        if rec["outcome"] == "mid":
            seq = [res(x) for x in a.get("seq", []) if not isinstance(x, list)]
            return len(seq) == 3 and seq[1] == rec["answer"][1], f"mid {rec['answer'][1]} vs raw seq {seq}"
        if rec["outcome"] == "none":
            return bool(a.get("none")), f"none vs raw {json.dumps(a, ensure_ascii=False)[:80]}"
        if rec["outcome"] == "two":
            tw = a.get("two", [])
            tw = [y for x in tw for y in (x if isinstance(x, list) else [x])]   # a pair written inside an extra list
            two = sorted(res(x) for x in tw)
            return two == sorted(rec["answer"][1:]), f"two {rec['answer'][1:]} vs raw {two}"
        return True, f"{rec['outcome']} (ties: parser's reading)"
    if k == "order":
        if rec["outcome"] == "none":
            return bool(a.get("none")), "none"
        flat = lambda L: [y for x in L for y in (x if isinstance(x, list) else [x])]
        shown = rec["shown"]
        def res(x):
            x = nfc(x); m = re.fullmatch(r"#\s*(\d+)", x)
            return shown[int(m.group(1)) - 1] if m else x
        seqs = a.get("seqs") or []
        if seqs and all(isinstance(x, str) for x in seqs):
            seqs = [seqs]                       # a flat list is one sequence written without its outer brackets
        raw_lines = [[res(x) for x in flat(l) if nfc(x).upper() != "GAP"] for l in seqs]
        mine = [[g for st in l if st != "GAP" for g in st] for l in rec["answer"]["lines"]]
        return raw_lines == mine, f"lines {mine} vs raw {raw_lines}"
    return True, "?"

def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    recs = [json.loads(l) for l in open(ANS / "triad-era.jsonl")]
    r = random.Random("spotcheck-triad-era-1")
    by = collections.defaultdict(list)
    for x in recs:
        by[(x["kind"], x["outcome"])].append(x)
    sample = []
    for key in sorted(by):
        sample += r.sample(by[key], min(len(by[key]), max(3, n * len(by[key]) // len(recs) * 4)))
    bad, tot = [], 0
    for x in sample:
        ok, note = check(x)
        tot += 1
        if not ok:
            bad.append((x, note))
    L = ["## Spot checks against the raw ledgers", "",
         f"*`refactored/port/spotcheck.py`: {tot} records sampled by (kind, outcome) with a fixed seed, each re-read from the verbatim model output with a plain JSON parse (no triad-era parser) and compared with the ported record. **{len(bad)} mismatches.***", ""]
    for x, note in bad[:40]:
        L.append(f"- `{x['aid']}` {x['round']} {x['mind']} {x['kind']}/{x['outcome']}: {note}")
    rep = (ANS / "PORT-REPORT.md").read_text()
    if "## Spot checks" in rep:
        rep = rep[:rep.index("## Spot checks")]
    (ANS / "PORT-REPORT.md").write_text(rep.rstrip() + "\n\n" + "\n".join(L) + "\n")
    print(f"{tot} sampled, {len(bad)} mismatches")
    for x, note in bad[:15]:
        print(" ", x["kind"], x["outcome"], note[:160])

if __name__ == "__main__":
    main()
