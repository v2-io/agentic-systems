#!/usr/bin/env python3
"""Prospective probe: what do frontier minds propose next to glyphs the study has NEVER shown them?

This is the decision-relevant population for hot exploration: unexplored nodes. The study's own answers are
selection-biased toward contexts the old planner built (mostly codepoint runs), so a ranker that looks good there
may only be good at what was already asked. Here, glyphs are sampled fresh, each shown ALONE as a one-symbol
"next" item, using the study's own sheet wording (harness/seq/items.sheet_prompt, imported read-only), sheets of 5,
"none" offered. Answers live only in this spike dir (probe/), never in the study's data/.

  python3 probe.py sample [--seed 0]        -> probe/glyphs.json
  python3 probe.py run MIND [MIND ...]      -> probe/raw/<mind>.jsonl (resumable)
  python3 probe.py gt                       -> derived/gt-probe.json (same instance format as gt.py)
"""
import argparse, concurrent.futures as cf, json, random, sys, time
from lib import DER, SPIKE, ok
STUDY = SPIKE.parents[2]
sys.path.insert(0, str(STUDY / "harness/seq")); sys.path.insert(0, str(STUDY / "harness/core"))
import items as IT  # noqa: E402
import parse as P  # noqa: E402

import os
SET = os.environ.get("PROBE_SET", "fresh")          # fresh (probe/) | carry (probe-carry/)
PD = SPIKE / ("probe" if SET == "fresh" else f"probe-{SET}"); (PD / "raw").mkdir(parents=True, exist_ok=True)
GTNAME = "probe" if SET == "fresh" else f"probe-{SET}"
MINDS = json.load(open(STUDY / "harness/core/minds.json"))["minds"]

def seen_glyphs():
    s = set()
    for l in open(DER / "answers-r012.jsonl"):
        r = json.loads(l)
        s.update(g for g in r["shown"] if g != "GAP")
        a = r.get("answer")
        if isinstance(a, dict):
            s.update(x for x in (a.get("proposals") or []) if isinstance(x, str))
    return s

def cmd_sample_carry(a):
    """The UTF-8 carry test: obscure letters at the end of a 64-code-point run (cp % 64 == 63, so cp+1 needs a carry
    into the previous UTF-8 byte) vs controls from the same blocks in mid-run (cp % 64 in 16..47). Both q and q+1 must
    be assigned letters of the same block, never shown in the study. Shown in shuffled order, same sheets as 'fresh'."""
    from lib import block, ucd
    seen = seen_glyphs()
    rng = random.Random(a.seed)
    def good(cp):
        q, n = chr(cp), chr(cp + 1)
        return (ok(q) and ok(n) and ucd()[q][1][0] == "L" and ucd()[n][1][0] == "L" and block(q) == block(n)
                and q not in seen and cp >= 0x800 and not ucd()[q][0].startswith(("CJK", "HANGUL", "YI ", "TANGUT")))
    bnd = [cp for cp in range(0x800, 0x30000) if cp % 64 == 63 and good(cp)]
    pick_b = rng.sample(bnd, 35)
    out = []
    for cp in pick_b:
        out.append({"g": chr(cp), "bytes": len(chr(cp).encode()), "arm": "boundary"})
        ctl = [c for c in range(cp - 47, cp - 15) if good(c)]
        if ctl:
            c = rng.choice(ctl); out.append({"g": chr(c), "bytes": len(chr(c).encode()), "arm": "control"})
    rng.shuffle(out)
    json.dump(out, open(PD / "glyphs.json", "w"), ensure_ascii=False, indent=0)
    print(len(out), "glyphs:", "".join(x["g"] for x in out))

def cmd_sample(a):
    if SET == "carry":
        return cmd_sample_carry(a)
    gl = json.load(open(DER / "emb" / "glyphs.json"))
    seen = seen_glyphs()
    rng = random.Random(a.seed)
    out = []
    # Joseph's exploration weighting (METHODOLOGY §5): printable ASCII, then 2-, 3-, 4-byte. Every ASCII glyph has
    # surely been seen, so ASCII is sampled from all of it; the others only from never-shown glyphs.
    for nb, n in ((1, 15), (2, 40), (3, 40), (4, 40)):
        pool = [g for g in gl if len(g.encode()) == nb and ok(g) and (nb == 1 or g not in seen)]
        out += [{"g": g, "bytes": nb, "seen": g in seen} for g in rng.sample(pool, n)]
    rng.shuffle(out)
    json.dump(out, open(PD / "glyphs.json", "w"), ensure_ascii=False, indent=0)
    print(len(out), "glyphs:", "".join(x["g"] for x in out))

def sheets():
    G = json.load(open(PD / "glyphs.json"))
    out = []
    for i in range(0, len(G), 5):
        ent = [{"id": n, "pid": f"p{i + n}", "shown": [x["g"]]} for n, x in enumerate(G[i:i + 5])]
        s = {"sid": f"spike-probe-{i // 5:03d}", "kind": "next", "factors": {"perp": True, "tie": False, "gap": False},
             "entries": ent}
        s["prompt"] = IT.sheet_prompt(s)
        out.append(s)
    return out

def cmd_run(a):
    from judges import make_judge
    S = sheets()
    for mind in a.minds:
        f = PD / "raw" / f"{mind}.jsonl"
        done = {json.loads(l)["sid"] for l in open(f)} if f.exists() else set()
        todo = [s for s in S if s["sid"] not in done]
        judge = make_judge(MINDS[mind])
        def one(s):
            r = judge(IT.SYSTEM, s["prompt"])
            return s, r
        with cf.ThreadPoolExecutor(a.workers) as ex:
            for s, r in ex.map(one, todo):
                with open(f, "a") as fh:
                    fh.write(json.dumps({"sid": s["sid"], "mind": mind, "t": time.time(), "prompt": s["prompt"],
                                         "result": r}, ensure_ascii=False) + "\n")
                print(mind, s["sid"], "ok" if r.get("raw") and not r.get("error") else f"ERR {r.get('error')}", flush=True)

def cmd_gt(a):
    S = {s["sid"]: s for s in sheets()}
    inst = {}
    stats = {}
    for f in sorted((PD / "raw").glob("*.jsonl")):
        last = {}
        for l in open(f):
            row = json.loads(l)
            if row["result"].get("raw") and not row["result"].get("error"):
                last[row["sid"]] = row
        mind = f.stem; fam = MINDS[mind]["family"]
        st = stats.setdefault(mind, {"ok": 0, "unparsed": 0, "none": 0})
        for sid, row in last.items():
            for e, (pid, v) in zip(S[sid]["entries"], P.parse_sheet(row["result"]["raw"], S[sid]).items()):
                q = e["shown"][0]
                I = inst.setdefault(q, {"node": q, "ctx": [q], "ctx_all": [q], "kind": GTNAME, "round": GTNAME,
                                        "category": ["probe", str(len(q.encode()))], "props": {}, "answers": 0,
                                        "none": 0, "fams_answered": []})
                if v["status"] != "ok":
                    st["unparsed"] += 1; continue
                st["ok"] += 1; I["answers"] += 1
                if fam not in I["fams_answered"]:
                    I["fams_answered"].append(fam)
                props = v["answer"].get("proposals") or []
                if not props:
                    I["none"] += 1; st["none"] += 1
                for rank, g in enumerate(props):
                    if not ok(g):
                        continue
                    p = I["props"].setdefault(g, {"fams": [], "minds": [], "n": 0, "fams_first": [], "n_first": 0})
                    p["n"] += 1
                    if fam not in p["fams"]: p["fams"].append(fam)
                    if mind not in p["minds"]: p["minds"].append(mind)
                    if rank == 0:
                        p["n_first"] += 1
                        if fam not in p["fams_first"]: p["fams_first"].append(fam)
    json.dump({"upto": "probe", "instances": inst, "triads": {}, "orderadj": {}}, open(DER / f"gt-{GTNAME}.json", "w"),
              ensure_ascii=False)
    print(stats)
    print(len(inst), "instances;", sum(1 for I in inst.values() for p in I["props"].values() if len(p["fams"]) >= 2),
          "proposals agreed by >=2 families (any rank)")

ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
x = sp.add_parser("sample"); x.add_argument("--seed", type=int, default=0)
x = sp.add_parser("run"); x.add_argument("minds", nargs="+"); x.add_argument("--workers", type=int, default=4)
sp.add_parser("gt")
a = ap.parse_args()
{"sample": cmd_sample, "run": cmd_run, "gt": cmd_gt}[a.cmd](a)
