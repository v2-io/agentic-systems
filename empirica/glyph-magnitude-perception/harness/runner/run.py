#!/usr/bin/env python3
"""v1.0 runner: frozen stimulus set x judge -> append-only ledger (one row per call).

  run.py STIM JUDGE [--format perp|tie|forced] [--mode single|sheet] [--sheet-size N]
         [--reps N] [--workers N] [--limit N] [--dry]

STIM   one of triads, format, conflict, holistic, gestalt  (data/stimuli-v1/<file>.jsonl)
JUDGE  a label in judges-v1.json

Raw truth: data/runs-v1/<run_id>/ledger.jsonl (append-only; resumable — calls already
recorded without error are skipped) + spec.json (written once; a resume with a different
spec refuses). Parsing is never done here; see parse.py (versioned, re-runnable).
"""
import argparse, concurrent.futures as cf, datetime as dt, hashlib, json, pathlib, sys, threading
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import instruments as I
from fate import rng, digest
from judges import make_judge, ADAPTER_VERSION

EXP = pathlib.Path(__file__).resolve().parents[2]
STIMS = {"triads": "triads.jsonl", "format": "format-pairs.jsonl", "conflict": "conflict.jsonl",
         "holistic": "holistic-pairs.jsonl", "gestalt": "gestalt.jsonl",
         "signa": "consumer-signa-pairs.jsonl", "signa-gestalt": "consumer-signa-gestalt.jsonl"}

def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()

def load_stim(stim):
    return [json.loads(l) for l in open(EXP / "data/stimuli-v1" / STIMS[stim])]

def group_of(row):
    # presentations that must not share a sheet: the two orders of a pair / the two triad orientation sets
    return row.get("oset", row.get("order", 0))

def build_calls(stim, rows, fmt, mode, sheet_size, reps):
    calls = []
    if stim in ("gestalt", "signa-gestalt") or mode == "single":
        for rep in range(reps):
            for r in rows:
                if stim in ("gestalt", "signa-gestalt"):
                    prompt = I.gestalt_prompt(r["glyphs"])
                else:
                    prompt = I.pair_prompt(r["a"], r["b"], fmt, {"pid": r["pid"], "fmt": fmt, "rep": rep})
                calls.append({"rep": rep, "pids": [r["pid"]], "prompt": prompt, "sheet": None})
        return calls
    groups = {}
    for r in rows:
        groups.setdefault(group_of(r), []).append(r)
    for rep in range(reps):
        for g, lst in sorted(groups.items()):
            lst = list(lst)
            rng(I.PROTOCOL, "sheet-shuffle", {"stim": stim, "fmt": fmt, "group": g, "rep": rep}).shuffle(lst)
            for k in range(0, len(lst), sheet_size):
                chunk = lst[k:k + sheet_size]
                items = [{"id": i, "a": r["a"], "b": r["b"]} for i, r in enumerate(chunk)]
                sheet_id = f"{stim}/{fmt}/g{g}/r{rep}/s{k // sheet_size}"
                prompt = I.sheet_prompt(items, fmt, {"sheet": sheet_id, "fmt": fmt, "rep": rep})
                calls.append({"rep": rep, "pids": [r["pid"] for r in chunk], "prompt": prompt, "sheet": sheet_id,
                              "items": [{"id": i, "pid": r["pid"]} for i, r in enumerate(chunk)]})
    return calls

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stim"); ap.add_argument("judge")
    ap.add_argument("--format", default="perp"); ap.add_argument("--mode", default="single")
    ap.add_argument("--sheet-size", type=int, default=40); ap.add_argument("--reps", type=int, default=1)
    ap.add_argument("--workers", type=int, default=4); ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry", action="store_true"); ap.add_argument("--tag", default="")
    a = ap.parse_args()
    judges = json.load(open(EXP / "harness/runner/judges-v1.json"))
    jspec = judges["judges"][a.judge]
    fmt = "gestalt" if a.stim in ("gestalt", "signa-gestalt") else a.format
    rows = load_stim(a.stim)
    stim_digest = digest(rows)
    run_id = f"{a.stim}-{fmt}-{a.mode}-{a.judge}" + (f"-{a.tag}" if a.tag else "")
    rdir = EXP / "data/runs-v1" / run_id
    rdir.mkdir(parents=True, exist_ok=True)
    spec = {"run_id": run_id, "protocol": I.PROTOCOL, "instrument": a.stim, "format": fmt, "mode": a.mode,
            "sheet_size": a.sheet_size if a.mode == "sheet" else None, "reps": a.reps,
            "stimulus_file": f"data/stimuli-v1/{STIMS[a.stim]}", "stimulus_digest": stim_digest,
            "judge_label": a.judge, "judge": jspec, "adapter_version": ADAPTER_VERSION[jspec["adapter"]],
            "system_prompt": I.SYSTEM,
            "context_residue": judges.get("context_residue", {}).get(jspec["adapter"]),
            "created": dt.datetime.now(dt.timezone.utc).isoformat()}
    sp = rdir / "spec.json"
    if sp.exists():
        old = json.load(open(sp))
        for k in ("protocol", "instrument", "format", "mode", "sheet_size", "stimulus_digest", "judge", "adapter_version"):
            if k == "adapter_version" and k not in old:
                continue  # specs written before adapter versioning (all a1 at that time)
            if old.get(k) != spec.get(k):
                sys.exit(f"refusing to resume {run_id}: spec field {k!r} differs ({old.get(k)!r} vs {spec.get(k)!r})")
        if old.get("reps", 1) < a.reps:
            old["reps"] = a.reps; json.dump(old, open(sp, "w"), ensure_ascii=False, indent=1)
    else:
        json.dump(spec, open(sp, "w"), ensure_ascii=False, indent=1)
    calls = build_calls(a.stim, rows, fmt, a.mode, a.sheet_size, a.reps)
    ledger = rdir / "ledger.jsonl"
    done = set()
    if ledger.exists():
        for line in open(ledger):
            try:
                r = json.loads(line)
            except Exception:
                continue
            if r["result"].get("raw") and not r["result"].get("error") and not r.get("sheet_incomplete"):
                done.add((r["rep"], tuple(r["pids"])))
    todo = [c for c in calls if (c["rep"], tuple(c["pids"])) not in done]
    if a.limit:
        todo = todo[:a.limit]
    print(f"{run_id}: {len(calls)} calls total, {len(done)} done, {len(todo)} to run", flush=True)
    if a.dry:
        print(todo[0]["prompt"] if todo else "(nothing)"); return
    judge = make_judge(jspec)
    lock = threading.Lock()
    sys_sha = sha(I.SYSTEM)
    n_ok = n_err = 0
    bypid = {r["pid"]: r for r in rows}
    def sheet_coverage(c, raw):
        items = [{"id": it["id"], "a": bypid[it["pid"]]["a"], "b": bypid[it["pid"]]["b"]} for it in c["items"]]
        p = I.parse_sheet(raw, items)
        return sum(1 for v in p.values() if v[0] != "unparsed") / max(1, len(items))
    def one(c):
        res = judge(I.SYSTEM, c["prompt"])
        incomplete = None
        if c["sheet"] and res.get("raw") and not res.get("error"):
            cov = sheet_coverage(c, res["raw"])
            if cov < 0.9:  # completeness gate only (raw kept verbatim); a resume re-asks this sheet
                incomplete = round(cov, 3)
        row = {"sheet_incomplete": incomplete, "ledger_version": 1, "run_id": run_id, "protocol": I.PROTOCOL, "instrument": a.stim, "format": fmt,
               "mode": a.mode, "rep": c["rep"], "pids": c["pids"], "sheet": c["sheet"], "items": c.get("items"),
               "prompt_sha256": sha(c["prompt"]), "prompt": c["prompt"], "system_sha256": sys_sha,
               "judge_label": a.judge, "ts": dt.datetime.now(dt.timezone.utc).isoformat(), "result": res}
        with lock:
            with open(ledger, "a") as f:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
        if incomplete is not None:
            res = dict(res, _incomplete=True, error=f"sheet-incomplete coverage={incomplete}")
        return res
    with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:
        for i, res in enumerate(ex.map(one, todo)):
            if res.get("error") or not res.get("raw") or res.get("_incomplete"):
                n_err += 1
                if n_err <= 5:
                    print(f"  error: {str(res.get('error'))[:300]}", flush=True)
            else:
                n_ok += 1
            if (i + 1) % 50 == 0:
                print(f"  {i + 1}/{len(todo)} ok={n_ok} err={n_err}", flush=True)
    print(f"{run_id}: finished ok={n_ok} err={n_err}", flush=True)

if __name__ == "__main__":
    main()
