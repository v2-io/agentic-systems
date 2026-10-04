"""Conflict battery (P9-P12), presentation-level, committed answers = 'dir' presentations, pooled over both orders
and all reps, per judge. Also per-item tallies for every judge (reading/tables/conflict-items.tsv)."""
import collections, json
from common import *
items = {it["id"]: it for it in json.load(open(ROOT / "harness/runner/conflict-items-v1.json"))["items"]}
P9 = ["roman-8-9", "roman-3-5", "roman-lc-8-9", "roman-lc-3-4", "roman-lc-4-5", "sup9-vs-2", "sub8-vs-3", "sup7-vs-1",
      "seg-0-vs-1", "seg-0-vs-7", "frac-8th-vs-half", "frac-9th-vs-3rd", "frac-10th-vs-5th"]
EQLINE = {"gram-earth-vs-heaven": "☰", "gram-yin-vs-yang": "⚊", "gram-gyin-vs-gyang": "⚌"}
FRONTIER = {"haiku45", "sonnet5", "sonnet55", "opus55", "sonnet55[sheet]", "grok46[sheet]", "gpt56terra[sheet]", "gemini31pro[sheet]", "gemini38flash[sheet]"}

per = {}  # judge -> item -> Counter of answers (winner glyph / 'perp' / 'tie' / 'unparsed')
for run in runs("conflict-perp"):
    j = judge_of(run)
    rows = stim_rows("conflict.jsonl")
    c = collections.defaultdict(collections.Counter)
    for r in ledger(run):
        res = r["result"]
        if not res.get("raw") or res.get("error") or r.get("sheet_incomplete") is not None: continue
        if r.get("sheet"):
            its = [{"id": it["id"], "a": rows[it["pid"]]["a"], "b": rows[it["pid"]]["b"]} for it in r["items"]]
            p = I.parse_sheet(res["raw"], its)
            for it in r["items"]:
                v = p.get(it["id"], ("unparsed", None, None)); st = rows[it["pid"]]
                c[st["item"]][v[1] if v[0] == "dir" else v[0]] += 1
        else:
            st = rows[r["pids"][0]]; v = I.parse_pair(res["raw"], st["a"], st["b"])
            c[st["item"]][v[1] if v[0] == "dir" else v[0]] += 1
    per[j] = c

def frac(j, ids, side_of):
    k = n = 0
    for i in ids:
        c = per[j].get(i, {})
        for ans, m in c.items():
            if ans in ("perp", "tie", "unparsed"): continue
            n += m; k += m * (ans == side_of(i))
    return k, n

out = []; P = out.append
P("P9 value wins (13 compiled-decode items) | P10a ☷>⚌ | P10b equal-line items: yang/ink side | P11 ‱ over %,‰ | P12 ⁹/9, ⚄/5: ≈ or ⟂ share of presentations")
P(f"{'judge':22s} {'P9':>15s} {'P10a':>12s} {'P10b':>12s} {'P11':>12s} {'P12':>12s}  {'reps(max n per item)':>20s}")
pool = collections.defaultdict(lambda: [0, 0])
for j in sorted(per):
    p9 = frac(j, P9, lambda i: items[i]["predict"]["value"])
    p10a = frac(j, ["gram-earth-vs-gyang"], lambda i: "☷")
    p10b = frac(j, list(EQLINE), lambda i: EQLINE[i])
    p11 = frac(j, ["permille-mille-vs-myriad", "permille-pct-vs-myriad"], lambda i: "‱")
    eq = [per[j].get(i, {}) for i in ("sup9-vs-9-equal", "die5-vs-5-equal")]
    e_k = sum(c.get("perp", 0) + c.get("tie", 0) for c in eq); e_n = sum(sum(v for a, v in c.items() if a != "unparsed") for c in eq)
    mx = max((sum(c.values()) for c in per[j].values()), default=0)
    f = lambda t: f"{t[0]:3d}/{t[1]:3d}={t[0]/t[1] if t[1] else float('nan'):.2f}"
    P(f"{j:22s} {f(p9):>15s} {f(p10a):>12s} {f(p10b):>12s} {f(p11):>12s} {f((e_k, e_n)):>12s}  {mx:20d}")
    if j in FRONTIER:
        for key, t in (("P9", p9), ("P10a", p10a), ("P10b", p10b), ("P11", p11), ("P12", (e_k, e_n))):
            pool[key][0] += t[0]; pool[key][1] += t[1]
P("pooled frontier: " + "  ".join(f"{k} {v[0]}/{v[1]}={v[0]/v[1]:.2f}" for k, v in pool.items()))
txt = "\n".join(out); print(txt)
open(ROOT / "reading/tables/conflict.txt", "w").write(txt + "\n")
with open(ROOT / "reading/tables/conflict-items.tsv", "w") as f:
    js = sorted(per)
    f.write("item\ta\tb\tdesigner-predict\t" + "\t".join(js) + "\n")
    for i, it in items.items():
        cells = []
        for j in js:
            c = per[j].get(i, {})
            cells.append(" ".join(f"{(a if a not in ('perp','tie','unparsed') else {'perp':'⟂','tie':'≈','unparsed':'?'}[a])}{m}" for a, m in sorted(c.items(), key=lambda x: -x[1])))
        f.write(f"{i}\t{it['a']}\t{it['b']}\t{json.dumps(it['predict'], ensure_ascii=False)}\t" + "\t".join(cells) + "\n")
