#!/usr/bin/env python3
"""Read the coordinator's scratch 'ones' probe: 18 dresses of the digit one, every pair in both orders
(⟂/≈/directed available), plus the whole set shuffled 3x. Builder's parser p1.3, unchanged.

usage: ones_probe.py ROOT   (ROOT = a directory with harness/runner, data/stimuli-v1, data/runs-v1)
Per judge: verdict mix over the 153 pairs; the directed (both-orders-agree) edges; a Copeland order
over those edges; and its whole-set answers verbatim. Then cross-judge agreement on directed edges.
"""
import json, pathlib, sys, collections, itertools
ROOT = pathlib.Path(sys.argv[1])
sys.path.insert(0, str(ROOT / "harness/runner"))
import instruments as I
RUNS, STIM = ROOT / "data/runs-v1", ROOT / "data/stimuli-v1"
rows = {json.loads(l)["pid"]: json.loads(l) for l in open(STIM / "ones-pairs.jsonl")}
grows = {json.loads(l)["pid"]: json.loads(l) for l in open(STIM / "ones-gestalt.jsonl")}
glyphs = next(iter(grows.values()))["intended"]

def judge(run): return json.load(open(run / "spec.json"))["judge_label"]

res = {}
for run in sorted(RUNS.glob("ones-perp-*")):
    j = judge(run); pres = {}
    for l in open(run / "ledger.jsonl"):
        r = json.loads(l); x = r["result"]
        if not x.get("raw") or x.get("error") or r.get("sheet_incomplete") is not None: continue
        if r.get("sheet"):
            items = [{"id": it["id"], "a": rows[it["pid"]]["a"], "b": rows[it["pid"]]["b"]} for it in r["items"]]
            p = I.parse_sheet(x["raw"], items)
            for it in r["items"]: pres[it["pid"]] = p.get(it["id"], ("unparsed", None, None))
        else:
            st = rows[r["pids"][0]]; pres[r["pids"][0]] = I.parse_pair(x["raw"], st["a"], st["b"])
    by = collections.defaultdict(dict)
    for pid, st in rows.items():
        by[frozenset((st["a"], st["b"]))][st["order"]] = pres.get(pid, ("missing", None, None))
    verd = {}
    for k, d in by.items():
        v0, v1 = d.get(0, ("missing",)), d.get(1, ("missing",))
        kinds = (v0[0], v1[0])
        if "missing" in kinds or "unparsed" in kinds: verd[k] = ("incomplete", None)
        elif kinds == ("dir", "dir"): verd[k] = ("cdir", v0[1]) if v0[1] == v1[1] else ("flip", None)
        elif kinds == ("perp", "perp"): verd[k] = ("cperp", None)
        elif kinds == ("tie", "tie"): verd[k] = ("ctie", None)
        else: verd[k] = ("mixed", None)
    res[j] = verd

print("glyphs:", " ".join(glyphs), "\n")
print(f"{'judge':22s} " + " ".join(f"{k:>10s}" for k in ("cdir", "ctie", "cperp", "mixed", "flip", "incomplete")))
for j, v in res.items():
    c = collections.Counter(x[0] for x in v.values())
    print(f"{j:22s} " + " ".join(f"{c[k]:>10d}" for k in ("cdir", "ctie", "cperp", "mixed", "flip", "incomplete")))

print("\nCopeland order over consistent-directed edges (wins - losses), per judge:")
for j, v in res.items():
    sc = collections.Counter()
    for k, (kind, w) in v.items():
        if kind == "cdir":
            l = next(g for g in k if g != w); sc[w] += 1; sc[l] -= 1
    if sc:
        print(f"  {j:20s} " + "  ".join(f"{g}{s:+d}" for g, s in sorted(sc.items(), key=lambda t: -t[1])))

print("\nCross-judge: on pairs both judges call consistent-directed, share with the same winner")
js = list(res)
for a, b in itertools.combinations(js, 2):
    both = [k for k in res[a] if res[a][k][0] == "cdir" and res[b].get(k, ("",))[0] == "cdir"]
    if both:
        agree = sum(res[a][k][1] == res[b][k][1] for k in both)
        print(f"  {a:20s} {b:20s} {agree}/{len(both)}")

print("\nWhole-set answers (3 shuffles each), verbatim parse:")
for run in sorted(RUNS.glob("ones-gestalt-*")):
    j = judge(run)
    for l in open(run / "ledger.jsonl"):
        r = json.loads(l); x = r["result"]
        if not x.get("raw") or x.get("error"): print(f"  {j:20s} (error)"); continue
        g = I.parse_gestalt(x["raw"], grows[r["pids"][0]]["glyphs"])
        print(f"  {j:20s} {g['kind']:6s} {''.join(g.get('order') or [])}  EXTRA: {''.join(g.get('extra') or [])}")
