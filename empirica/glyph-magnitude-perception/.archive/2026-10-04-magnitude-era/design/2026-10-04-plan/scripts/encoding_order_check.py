#!/usr/bin/env python3
"""Does whole-set (gestalt) reconstruction of the top-40 survey sequences track magnitude, or known
encoding/conventional order? Existing v1.0 ledgers only; no new judge calls.

For each of the 117 top-40 candidates:
  written    = the surveyor's written order
  cp_mono    = written order is monotone in codepoint (ascending or descending)
  strict     = pairwise: share of adjacent steps consistent-directed (both orders) in the frontier-majority
               direction, mean over the six frontier judges (same definition as analysis/views/orderings.py)
  exact      = share of frontier gestalt answers that reproduce the FULL written order or its reverse
               (every glyph placed, none to EXTRA)
  cp_exact   = share of frontier gestalt answers that equal the full codepoint-sorted order or its reverse
Parser: the builder's p1.3 (harness/runner/instruments.py), unchanged.
Run from anywhere: python3 encoding_order_check.py
"""
import json, pathlib, sys, collections, statistics as stx
EXP = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(EXP / "harness/runner"))
import instruments as I

RUNS, STIM = EXP / "data/runs-v1", EXP / "data/stimuli-v1"
FRONTIER = ["opus55", "sonnet55", "haiku45", "grok46", "gemini31pro", "gemini38flash"]

def judge_of(run):
    return json.load(open(RUNS / run / "spec.json"))["judge_label"]

def ledger(run):
    p = RUNS / run / "ledger.jsonl"
    return [json.loads(l) for l in open(p)] if p.exists() else []

cands = {c["cand"]: c for c in json.load(open(STIM / "top40-candidates.json"))["candidates"]}

# ---- pairwise strict, per candidate per judge (adjacent steps of the written order)
step_rows = {}
for f in ("top40-steps.jsonl", "top40b-steps.jsonl"):
    for l in open(STIM / f):
        r = json.loads(l); step_rows[r["pid"]] = r
pres = collections.defaultdict(lambda: collections.defaultdict(dict))  # judge -> (cand, step) -> order -> verdict
for run in sorted(p.name for p in RUNS.iterdir() if p.is_dir()):
    if not (run.startswith("top40-perp") or run.startswith("top40b-perp")):
        continue
    j = judge_of(run)
    if j not in FRONTIER:
        continue
    for r in ledger(run):
        res = r["result"]
        if not res.get("raw") or res.get("error") or r.get("sheet_incomplete") is not None:
            continue
        if r.get("sheet"):
            items = [{"id": it["id"], "a": step_rows[it["pid"]]["a"], "b": step_rows[it["pid"]]["b"]} for it in r["items"]]
            p = I.parse_sheet(res["raw"], items)
            for it in r["items"]:
                st = step_rows[it["pid"]]; v = p.get(it["id"], ("unparsed", None, None))
                pres[j][(st["cand"], st["step"])][st["order"]] = (v, st)
        else:
            st = step_rows[r["pids"][0]]; v = I.parse_pair(res["raw"], st["a"], st["b"])
            pres[j][(st["cand"], st["step"])][st["order"]] = (v, st)

with_ = collections.defaultdict(lambda: collections.Counter())
for j, d in pres.items():
    for (cand, k), od in d.items():
        c = with_[(cand, j)]; c["n"] += 1
        if 0 in od and 1 in od:
            (v0, s0), (v1, _) = od[0], od[1]
            if v0[0] == "dir" and v1[0] == "dir" and v0[1] == v1[1]:
                c["up" if v0[1] == s0["later"] else "down"] += 1

# ---- gestalt
g_rows = {}
for f in ("top40-gestalt.jsonl", "top40b-gestalt.jsonl"):
    for l in open(STIM / f):
        r = json.loads(l); g_rows[r["pid"]] = r
answers = collections.defaultdict(list)  # cand -> list of parsed gestalt
for run in sorted(p.name for p in RUNS.iterdir() if p.is_dir()):
    if not (run.startswith("top40-gestalt") or run.startswith("top40b-gestalt")):
        continue
    if judge_of(run) not in FRONTIER:
        continue
    for r in ledger(run):
        res = r["result"]
        if not res.get("raw") or res.get("error"):
            continue
        st = g_rows[r["pids"][0]]
        answers[int(st["seq"].split("-")[1])].append(I.parse_gestalt(res["raw"], st["glyphs"]))

rows = []
for ci, c in cands.items():
    w = c["glyphs"]
    cps = [ord(g) for g in w]
    cp_sorted = [chr(x) for x in sorted(cps)]
    cp_mono = cps == sorted(cps) or cps == sorted(cps, reverse=True)
    js = [with_[(ci, j)] for j in FRONTIER if with_[(ci, j)]["n"]]
    U = sum(x["up"] for x in js); D = sum(x["down"] for x in js)
    strict = stx.mean((x["up"] if U >= D else x["down"]) / x["n"] for x in js) if js else float("nan")
    ans = answers.get(ci, [])
    orders = ["".join(a["order"]) for a in ans if a.get("kind") == "order" and not a.get("extra")]
    full = lambda s: [o for o in orders if o in (s, s[::-1])]
    n = len(ans)
    exact = len(full("".join(w))) / n if n else float("nan")
    cpx = len(full("".join(cp_sorted))) / n if n else float("nan")
    rows.append(dict(cand=ci, seq="".join(w), n=len(w), cp_mono=cp_mono, strict=strict, exact=exact, cp_exact=cpx, n_ans=n))

def summ(sel, label):
    if not sel: print(f"{label}: none"); return
    print(f"{label}: k={len(sel)}  mean strict={stx.mean(r['strict'] for r in sel):.2f}  "
          f"mean exact-written={stx.mean(r['exact'] for r in sel):.2f}  mean exact-codepoint={stx.mean(r['cp_exact'] for r in sel):.2f}")

ok = [r for r in rows if r["n_ans"]]
print(f"candidates with frontier gestalt answers: {len(ok)} of {len(rows)}\n")
summ([r for r in ok if r["cp_mono"]], "written order IS codepoint-monotone ")
summ([r for r in ok if not r["cp_mono"]], "written order NOT codepoint-monotone")
print()
summ([r for r in ok if r["cp_mono"] and r["strict"] < 0.5], "cp-monotone, pairwise strict < 0.5   ")
summ([r for r in ok if not r["cp_mono"] and r["strict"] < 0.5], "not cp-monotone, strict < 0.5        ")
print("\n-- low pairwise (strict < 0.5): written order rebuilt whole anyway? --")
for r in sorted(ok, key=lambda r: r["strict"]):
    if r["strict"] < 0.5:
        print(f"  {r['seq']:<14} n={r['n']:<2} cp_mono={'Y' if r['cp_mono'] else 'n'} strict={r['strict']:.2f} "
              f"exact-written={r['exact']:.2f} exact-codepoint={r['cp_exact']:.2f} (answers {r['n_ans']})")
print("\n-- not codepoint-monotone: does the whole-set answer follow the written (magnitude) order or codepoint order? --")
for r in sorted(ok, key=lambda r: -r["exact"]):
    if not r["cp_mono"]:
        print(f"  {r['seq']:<16} strict={r['strict']:.2f} exact-written={r['exact']:.2f} exact-codepoint={r['cp_exact']:.2f}")
