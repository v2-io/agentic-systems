"""Holistic / gestalt (P13-P15), plus every holistic set's pairwise vs gestalt signature per judge.
 pairwise cdir = consistent-directed pairs / all pairs in the set (incomplete pairs count in the denominator
                 and are reported separately)
 author-agree   = of cdir pairs, fraction whose winner is the later rung in the author's order
 gestalt        = mean |tau| over shuffles answered with an order (⟂ and unparsed reported separately)."""
import collections, json, statistics as stx
from common import *
hol = {s["name"]: s for s in json.load(open(ROOT / "harness/runner/holistic-sets-v1.json"))["sets"]}
pair = collections.defaultdict(dict)   # (seq) -> judge -> (cdir, n, agree, incomplete)
for run in runs("holistic-perp"):
    j = judge_of(run)
    rows, pres = parsed_presentations(run, "holistic-pairs.jsonl")
    by = collections.defaultdict(dict)
    for pid, st in rows.items(): by[st["seq"]][pid] = st
    for seq, rs in by.items():
        pv = pair_verdicts(rs, {p: pres[p] for p in rs if p in pres})
        order = hol[seq]["order"] if seq in hol else None
        n = len(pv); cd = [(k, w) for k, (kind, w, _) in pv.items() if kind == "cdir"]
        ag = sum(1 for k, w in cd if order and w == max(k, key=order.index))
        inc = sum(1 for v in pv.values() if v[0] == "incomplete")
        pair[seq][j] = (len(cd), n, ag, inc)
gest = collections.defaultdict(dict)
grows = stim_rows("gestalt.jsonl")
for run in runs("gestalt-gestalt"):
    j = judge_of(run)
    by = collections.defaultdict(list)
    for r in ledger(run):
        st = grows[r["pids"][0]]; raw = r["result"].get("raw")
        if not raw or r["result"].get("error"): by[st["seq"]].append(("err", None)); continue
        g = I.parse_gestalt(raw, st["glyphs"])
        if g["kind"] == "order":
            t, n = kendall_tau(g["order"], st["intended"]); by[st["seq"]].append(("order", abs(t) if t is not None else None))
        else: by[st["seq"]].append((g["kind"], None))
    for seq, lst in by.items():
        taus = [t for k, t in lst if k == "order" and t is not None]
        gest[seq][j] = (stx.mean(taus) if taus else None, len(taus), sum(k == "perp" for k, _ in lst), sum(k in ("unparsed", "err") for k, _ in lst), [round(t, 2) for t in taus])
judges = ["opus55", "sonnet55", "sonnet5", "haiku45", "sonnet55[sheet]", "grok46[sheet]", "gpt56terra[sheet]", "gemini31pro[sheet]", "gemini38flash[sheet]",
          "glimmer30b[sheet]", "llama32-3b", "qwen25-3b", "gemma3-4b", "phi4mini", "mistral7b", "hermes3-3b"]
gj = lambda j: j.replace("[sheet]", "")
out = []; P = out.append
for seq in list(hol) + [f"noise-{i}" for i in range(4)]:
    s = hol.get(seq, {"kind": "noise-foil", "order": []})
    P(f"\n== {seq}  [{s['kind']}]  {''.join(s['order'])}")
    P(f"   {'judge':22s} {'pair cdir/n':>12s} {'agree':>6s} {'inc':>4s} | {'gestalt mean|tau| (n)':>22s} {'⟂':>2s} {'?':>2s}  taus")
    for j in judges:
        pp = pair.get(seq, {}).get(j)
        g = gest.get(seq, {}).get(gj(j)) if "[sheet]" not in j or gj(j) not in ("sonnet55",) else None
        if j == "sonnet55": g = gest.get(seq, {}).get("sonnet55")
        if not pp and not g: continue
        ps = f"{pp[0]:3d}/{pp[1]:3d}={pp[0]/pp[1]:.2f} {pp[2]:3d} {pp[3]:4d}" if pp else f"{'-':>12s} {'':>6s} {'':>4s}"
        gs = (f"{(g[0] if g[0] is not None else float('nan')):.2f} ({g[1]})".rjust(22) + f" {g[2]:2d} {g[3]:2d}  {g[4]}") if g else ""
        P(f"   {j:22s} {ps} | {gs}")
txt = "HOLISTIC SETS: pairwise (perp) vs gestalt, per judge. Gestalt runs were single-mode for all judges; shown on the judge's row.\n" + "\n".join(out)
print(txt); open(ROOT / "reading/tables/holistic.txt", "w").write(txt + "\n")
