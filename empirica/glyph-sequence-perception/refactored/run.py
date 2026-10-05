#!/usr/bin/env python3
"""Rounds of the refactored study (METHODOLOGY): plan (concern 3) -> ask (concern 1) -> record (concern 1) -> tree
(concern 2) -> progress -> commit.

  run.py plan RID [--budget N]      questions + sheets -> data/rounds/RID/
  run.py ask RID [--minds m ...]    call the judges; verbatim ledgers -> data/rounds/RID/raw/<mind>/ledger.jsonl
  run.py record RID                 ledgers -> data/answers/RID.jsonl (canonical records; regenerable)
  run.py tree                       SEQUENCES.md (+ data/tree/*.json) and BEST.md (report/best.py, a read-off)
  run.py progress                   PROGRESS.md: what the tree holds after each round
  run.py round RID [--budget N]     all of the above, then commit
  run.py loop [--budget N]          rounds c001, c002, ... until data/rounds/STOP exists or a round fails

Truth: data/rounds/<RID>/{questions,sheets}.jsonl, plan.json and raw/<mind>/ledger.jsonl (verbatim prompts and
answers), committed. Everything in data/answers/ and data/tree/ is rebuilt from them (and from the triad era's
ledgers via port/port_triad_era.py).
"""
import argparse, collections, concurrent.futures as cf, datetime as dt, hashlib, json, pathlib, subprocess, sys, threading

ROOT = pathlib.Path(__file__).resolve().parent
STUDY = ROOT.parent
DATA = ROOT / "data"
for sub in ("core", "probe", "tree", "priority", "report"):
    sys.path.insert(0, str(ROOT / sub))
import probe as PR                                          # noqa: E402
import tree as TR                                           # noqa: E402
import plan as PL                                           # noqa: E402
import best as BE                                           # noqa: E402  (a read-off; nothing reads it back)

def rj(p):
    p = pathlib.Path(p)
    return [json.loads(l) for l in open(p) if l.strip()] if p.exists() else []

def wj(p, rows, mode="w"):
    p = pathlib.Path(p); p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, mode) as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")

def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()

def minds():
    return json.load(open(ROOT / "core" / "minds.json"))

def seeds():
    s = rj(STUDY / "data" / "seeds.jsonl")
    have = {x.get("sid") for x in s}
    for f in sorted((STUDY / "data" / "seeds").glob("*.jsonl")):          # the dropspot
        for x in rj(f):
            if x.get("sid") not in have:
                s.append(x); have.add(x.get("sid"))
    return s

def answers():
    recs = []
    for f in sorted((DATA / "answers").glob("*.jsonl")):
        recs += rj(f)
    return recs

# ------------------------------------------------------------------ plan
def cmd_plan(a):
    rd = DATA / "rounds" / a.round
    if (rd / "sheets.jsonl").exists():
        sys.exit(f"{a.round} already planned (truth is append-only)")
    qs, stats = PL.plan(a.round, answers(), seeds(), a.budget)
    sh = PR.sheets(a.round, qs)
    reg = minds(); core, second = reg["roster"]["core"], reg["roster"]["second"]
    share = reg["roster"].get("second_share", 0.2)
    for s in sh:
        s["minds"] = list(core) + [m for m in second if PR.R("second-mind", {"sid": s["sid"], "m": m}).random() < share]
    wj(rd / "questions.jsonl", qs); wj(rd / "sheets.jsonl", sh)
    stats["sheets"] = len(sh)
    json.dump(stats, open(rd / "plan.json", "w"), ensure_ascii=False, indent=1)
    print(json.dumps(stats, ensure_ascii=False))

# ------------------------------------------------------------------ ask
AGY_WORKERS = 3           # Gemini via agy: 3 concurrent calls (Joseph, 2026-10-05: "go ahead and speed up gemini")
GRACE_MIN = 20            # once every Claude mind has finished, other minds get this many more minutes, then the round
                          # moves on (Joseph: "when we start hitting rate limits we can let claude go ahead"); their
                          # unanswered sheets stay open and `run.py ask RID` later backfills them (ledgers resume)

def cmd_ask(a):
    rd = DATA / "rounds" / a.round
    sheets = rj(rd / "sheets.jsonl")
    reg = minds()
    sys.path.insert(0, str(ROOT / "core"))
    from judges import make_judge, ADAPTER_VERSION
    want = a.minds or sorted({m for s in sheets for m in s["minds"]})
    stop = threading.Event()
    def run_mind(m):
        spec = reg["minds"][m]; judge = make_judge(spec)
        led = rd / "raw" / m / "ledger.jsonl"; lock = threading.Lock()
        for p in range(3):                                   # resume passes: failed sheets are re-asked
            if stop.is_set() and reg["minds"][m]["family"] != "claude":
                break
            done = {r["sid"] for r in rj(led) if r["result"].get("raw") and not r["result"].get("error")}
            todo = [s for s in sheets if m in s["minds"] and s["sid"] not in done]
            if not todo:
                break
            def one(s):
                if stop.is_set() and reg["minds"][m]["family"] != "claude":
                    return
                res = judge(PR.SYSTEM, s["prompt"])
                row = {"protocol": PR.PROTOCOL, "round": a.round, "sid": s["sid"], "mind": m, "judge": spec,
                       "adapter_version": ADAPTER_VERSION[spec["adapter"]], "system_sha256": sha(PR.SYSTEM),
                       "prompt_sha256": sha(s["prompt"]), "prompt": s["prompt"],
                       "ts": dt.datetime.now(dt.timezone.utc).isoformat(), "result": res}
                if res.get("raw") and not res.get("error") and PR._answers(res["raw"]) is None:
                    row["result"] = dict(res, error="no-answers-object")      # raw kept; re-asked next pass
                with lock:
                    wj(led, [row], "a")
            workers = AGY_WORKERS if spec["adapter"] == "agy" else 6
            with cf.ThreadPoolExecutor(max_workers=workers) as ex:
                list(ex.map(one, todo))
        n = len({r["sid"] for r in rj(led) if r["result"].get("raw") and not r["result"].get("error")})
        return m, n, sum(1 for s in sheets if m in s["minds"])
    with cf.ThreadPoolExecutor(max_workers=len(want)) as ex:
        futs = {m: ex.submit(run_mind, m) for m in want}
        claude = [f for m, f in futs.items() if reg["minds"][m]["family"] == "claude"]
        cf.wait(claude)
        rest = [f for m, f in futs.items() if reg["minds"][m]["family"] != "claude"]
        _, pending = cf.wait(rest, timeout=GRACE_MIN * 60)
        if pending:
            print(f"{a.round}: grace of {GRACE_MIN} min after Claude finished is over; stopping "
                  f"{[m for m, f in futs.items() if f in pending]} (backfill later with `run.py ask {a.round}`)", flush=True)
            stop.set()
        for m, f in futs.items():
            mm, n, tot = f.result()
            print(f"{a.round}/{mm}: {n}/{tot} sheets answered", flush=True)

# ------------------------------------------------------------------ record
def cmd_record(a):
    rd = DATA / "rounds" / a.round
    sheets = {s["sid"]: s for s in rj(rd / "sheets.jsonl")}
    qs = {q["qid"]: q for q in rj(rd / "questions.jsonl")}
    reg = minds()["minds"]
    out = []
    for led in sorted((rd / "raw").glob("*/ledger.jsonl")):
        m = led.parent.name
        by = collections.defaultdict(list)
        for row in rj(led):
            by[row["sid"]].append(row)
        for sid, rows in by.items():
            out += PR.records(sheets[sid], rows, m, reg[m]["family"], reg[m], qs)
    wj(DATA / "answers" / f"{a.round}.jsonl", out)
    c = collections.Counter((r["kind"], r["outcome"]) for r in out)
    print(f"{a.round}: {len(out)} records " + json.dumps({f"{k}/{o}": n for (k, o), n in sorted(c.items())}))

# ------------------------------------------------------------------ tree + progress
def cmd_tree(a):
    TR.main()
    BE.main()

SETTLED_AGREEMENT = 0.75     # read-off only (PROGRESS): a sequence counts as settled when every walked step has at
                             # least this agreement and it walked >= 3 steps; chosen without evidence, gates nothing

def cmd_progress(a):
    recs = answers()
    order = sorted({r["round"] for r in recs if r["round"] != "seed"}, key=lambda x: (x[0] != "r", x))
    seedrecs = [r for r in recs if r["round"] == "seed"]
    rows = []
    for i, rid in enumerate(order):
        upto = set(order[:i + 1])
        T = TR.Tree(seedrecs + [r for r in recs if r["round"] in upto])
        seqs = TR.sequences(T)
        settled = [s for s in seqs if s["walked"] >= 3 and s["agreement"] >= SETTLED_AGREEMENT]
        Tp = TR.Tree([r for r in recs if r["round"] in upto], seeds=False)
        pure = [s for s in TR.sequences(Tp) if s["walked"] >= 3 and s["agreement"] >= SETTLED_AGREEMENT]
        sl = sorted(len(s["glyphs"]) for s in settled)
        stops = collections.Counter(x.split("→")[0].split(" ")[0] for s in seqs for x in (s["stop_left"], s["stop_right"]))
        cyc = [c for c in T.cycles.values() if c["distinct"] >= 4]
        rows.append({"round": rid, "records": sum(1 for r in recs if r["round"] == rid), "contexts": len(T.nodes),
                     "sequences": len(seqs), "settled": len(settled), "settled_glyphs": sum(sl),
                     "longest_settled": sl[-1] if sl else 0, "settled_pure": len(pure), "kstar_known": sum(s["kstar_known"] for s in seqs),
                     "steps": sum(s["walked"] for s in seqs), "open": stops["open"], "end": stops["end"],
                     "wrap": stops["wrap"], "cycles": len(cyc), "cycles_2fam": sum(1 for c in cyc if len(c["families"]) >= 2),
                     "inhibit": sum(1 for r in recs if r["round"] == rid and r["kind"] == "inhibit")})
    L = ["# Progress by round", "",
         f"*Generated by `refactored/run.py progress`: the context tree rebuilt from every answer up to and including each round (r000–r012 are the ported triad era; c001 on are context-tree rounds). Seed votes (the survey sequences, tagged) are included in every row; *settled without seeds* rebuilds the tree from real answers only. **Settled** is a read-off that gates nothing: a sequence whose walk took at least 3 steps, each agreed at ≥ {SETTLED_AGREEMENT}. **k\\* known:** walked steps whose shortest sufficient context is pinned down. **Ends** count the stops of every walk: *open* is never asked, *end* is the minds saying none, *wrap* is a return to a glyph already in the path. **Cycles:** manifested, with ≥ 4 distinct glyphs (≥ 2 families).*", "",
         "| round | answers | contexts | sequences | settled | settled without seeds | settled glyphs | longest settled | k* known / steps | ends open / end / wrap | cycles (≥2 fam) | inhibit answers |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        L.append(f"| {r['round']} | {r['records']} | {r['contexts']} | {r['sequences']} | {r['settled']} | {r['settled_pure']} | {r['settled_glyphs']} | {r['longest_settled']} | "
                 f"{r['kstar_known']} / {r['steps']} | {r['open']} / {r['end']} / {r['wrap']} | {r['cycles']} ({r['cycles_2fam']}) | {r['inhibit']} |")
    (ROOT / "PROGRESS.md").write_text("\n".join(L) + "\n")
    json.dump(rows, open(DATA / "tree" / "progress.json", "w"), indent=0)
    print("\n".join(L[-3:]))

# ------------------------------------------------------------------ round / loop
def git(*args):
    return subprocess.run(["git", "-C", str(STUDY.parents[1]), *args], capture_output=True, text=True)

def commit(rid):
    rel = ROOT.relative_to(STUDY.parents[1])
    paths = [str(rel / "data" / "rounds" / rid), str(rel / "SEQUENCES.md"), str(rel / "PROGRESS.md"), str(rel / "BEST.md")]
    git("add", *paths)
    r = git("commit", "-q", "-m", f"empirica/glyph-sequence: context-tree round {rid} (planned, answered, recorded; SEQUENCES + PROGRESS)\n\n"
            "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n"
            "Claude-Session: https://claude.ai/code/session_01MfWNNnWTnFYD1Y8Jh7KFHF", "--", *paths)
    return r.returncode == 0

def cmd_round(a):
    for f, aa in ((cmd_plan, a), (cmd_ask, argparse.Namespace(round=a.round, minds=None)), (cmd_record, a),
                  (cmd_tree, a), (cmd_progress, a)):
        print(f"== {a.round} {f.__name__} {dt.datetime.now():%H:%M:%S}", flush=True)
        f(aa)
    print(f"== {a.round} committed" if commit(a.round) else f"!! {a.round} commit failed", flush=True)

def cmd_loop(a):
    while not (DATA / "rounds" / "STOP").exists():
        done = sorted(p.name for p in (DATA / "rounds").glob("c[0-9][0-9][0-9]") if (p / "sheets.jsonl").exists())
        rid = f"c{(int(done[-1][1:]) + 1) if done else 1:03d}"
        try:
            cmd_round(argparse.Namespace(round=rid, budget=a.budget))
        except Exception as ex:
            print(f"!! {rid} failed: {ex!r}", flush=True); raise
    print("== STOP found", flush=True)

def main():
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(required=True)
    p = sub.add_parser("plan"); p.add_argument("round"); p.add_argument("--budget", type=int, default=700); p.set_defaults(f=cmd_plan)
    p = sub.add_parser("ask"); p.add_argument("round"); p.add_argument("--minds", nargs="*"); p.set_defaults(f=cmd_ask)
    p = sub.add_parser("record"); p.add_argument("round"); p.set_defaults(f=cmd_record)
    p = sub.add_parser("tree"); p.set_defaults(f=cmd_tree)
    p = sub.add_parser("progress"); p.set_defaults(f=cmd_progress)
    p = sub.add_parser("round"); p.add_argument("round"); p.add_argument("--budget", type=int, default=700); p.set_defaults(f=cmd_round)
    p = sub.add_parser("loop"); p.add_argument("--budget", type=int, default=700); p.set_defaults(f=cmd_loop)
    a = ap.parse_args(); a.f(a)

if __name__ == "__main__":
    main()
