#!/usr/bin/env python3
"""Rounds of the study (METHODOLOGY): plan (concern 3) -> ask (concern 1) -> record (concern 1) -> tree
(concern 2) -> progress -> commit.

  run.py plan RID [--budget N]      questions + sheets -> data/rounds/RID/
  run.py ask RID [--minds m ...]    call the judges; verbatim ledgers -> data/rounds/RID/raw/<mind>/ledger.jsonl
  run.py record RID                 ledgers -> data/answers/RID.jsonl (canonical records; regenerable)
  run.py tree                       SEQUENCES.md (+ data/tree/*.json) and BEST.md (report/best.py, a read-off)
  run.py progress                   PROGRESS.md: what the tree holds after each round
  run.py round RID [--budget N]     plan, ask the DRIVER minds (Claude), record every round, tree, progress, commit
  run.py loop [--budget N]          rounds c001, c002, ... until data/rounds/STOP exists or a round fails
  run.py drain --minds m ...        a separate process: asks these minds' open sheets in every round, oldest first,
                                    paced by pace.json, until data/rounds/STOP exists

Cadence (Joseph, 2026-10-05: "let claude go ahead ideally so we can start at least getting the claude-supported
sequences well defined in the data"; then "move forward without stopping on claude responses … start slowing down the
claude responses a bit … once they are running asynchronously … really slow down gemini"): Claude drives the rounds;
every other family drains its sheets asynchronously and is folded in whenever a round re-records. pace.json is re-read
before every call, so pacing can be retuned while everything runs.

Truth: data/rounds/<RID>/{questions,sheets}.jsonl, plan.json and raw/<mind>/ledger.jsonl (verbatim prompts and
answers), committed. Everything in data/answers/ and data/tree/ is rebuilt from them (and from the triad era's
ledgers via port/port_triad_era.py).
"""
import argparse, collections, concurrent.futures as cf, datetime as dt, hashlib, json, pathlib, re, subprocess, sys, threading, time

ROOT = pathlib.Path(__file__).resolve().parent       # the study root (refactored/ until 2026-10-06)
DATA = ROOT / "data"
for sub in ("core", "probe", "tree", "priority", "report"):
    sys.path.insert(0, str(ROOT / sub))
import probe as PR                                          # noqa: E402
import tree as TR                                           # noqa: E402
import plan as PL                                           # noqa: E402
import best as BE                                           # noqa: E402  (a read-off; nothing reads it back)

def rj(p):
    """jsonl -> rows; a last line still being written by another process (drain) is skipped, not fatal"""
    p = pathlib.Path(p)
    if not p.exists():
        return []
    rows = []
    for l in open(p):
        if l.strip():
            try:
                rows.append(json.loads(l))
            except json.JSONDecodeError:
                if l.endswith("\n"):
                    raise
    return rows

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
    """the survey seeds, plus the dropspot (data/seeds/*.jsonl; its README gives the format: id, kind, glyphs as a
    string or list, author, ...), normalised to the survey shape (sid, type, glyphs as a list, surveyor). Retracted
    dropspot seeds are left out. (Until 2026-10-06 dropspot seeds were deduplicated by a `sid` they don't have, so only
    the first one was ever read.)"""
    s = rj(DATA / "seeds.jsonl")
    have = {x.get("sid") for x in s}
    for f in sorted((DATA / "seeds").glob("*.jsonl")):          # the dropspot
        rows = rj(f)
        retracted = {x["retracts"] for x in rows if x.get("retracts")}
        for x in rows:
            if x.get("retracts") or x.get("id") in retracted:
                continue
            g = x.get("glyphs")
            x = dict(x, sid=x.get("sid") or f"drop:{f.stem}:{x.get('id')}", type=x.get("type") or x.get("kind"),
                     surveyor=x.get("surveyor") or x.get("author"), glyphs=list(g) if isinstance(g, str) else g)
            if x["sid"] not in have:
                s.append(x); have.add(x["sid"])
    return s

def answers():
    """every answer record, one per answer ID (as tree.load: 46 triad-era records are identical repeats)"""
    recs, seen = [], set()
    for f in sorted((DATA / "answers").glob("*.jsonl")):
        for r in rj(f):
            if r.get("aid") not in seen:
                seen.add(r.get("aid")); recs.append(r)
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
        if s.get("variant") == "reasoned":                # the reasoned pass goes to reasoner minds only
            s["minds"] = list(reg["roster"].get("reasoners", []))
            continue
        if s["kind"] == "pick":                            # the generator pass goes to generator minds only (METHODOLOGY §4a)
            s["minds"] = list(reg["roster"].get("generators", []))
            continue
        s["minds"] = list(core) + [m for m in second if PR.R("second-mind", {"sid": s["sid"], "m": m}).random() < share]
    wj(rd / "questions.jsonl", qs); wj(rd / "sheets.jsonl", sh)
    stats["sheets"] = len(sh)
    import unicodedata; stats["unicode"] = unicodedata.unidata_version
    json.dump(stats, open(rd / "plan.json", "w"), ensure_ascii=False, indent=1)
    print(json.dumps(stats, ensure_ascii=False))

# ------------------------------------------------------------------ ask
MAX_ATTEMPTS = {None: 3, "no-lookup": 2, "reasoned": 3, "reflection": 3}   # calls per (sheet, mind, prompt variant) before it is left unanswered;
                          # 3 is the triad era's resume passes, 2 for the re-ask variant is a choice made without evidence
DEFAULT_PACE = {"workers": 2, "interval_s": 0}
LIMIT_RE = re.compile(r"hit your .{0,20}limit|usage limit|rate.?limit|quota|resets \d|\b429\b|resource.?exhausted", re.I)
LIMIT_PAUSE_S = 600       # the longest wait after a limit (sized for Claude's weekly limit; chosen without evidence)
LIMIT_BACKOFF_S = 30      # the first wait; it doubles with each limit in a row and resets on a call that is not one.
                          # Most limits are rate limits (Joseph, 2026-10-06: "When there are limits, they are usually
                          # rate-limits, not overall usage limits"), which a short wait clears; a usage limit reaches
                          # the cap within five. Both numbers chosen without evidence.

def limit_hit(res):
    """a call refused for a limit, a rate limit or a usage limit (found 2026-10-06: Claude's weekly limit, "You've hit your weekly limit ·
    resets 7am", answered every call of rounds c028-c079 with an error). Not an attempt at the sheet: it is not
    counted toward MAX_ATTEMPTS, and the mind pauses, so the loop waits inside its round instead of planning blind
    ones. A row already relabelled "limit" is one too: agy's detail lives only in the error, which the relabel moves
    to limit_detail (found 2026-10-06: Gemini's limits of c096-c097 were relabelled to a bare "limit" that this test
    missed, so its drain never paused and each limit spent one of the sheet's attempts). A call that returned an answer
    is never a limit, even when the answer fails to parse: its text is the mind's, and glyph answers mention
    "quotation" marks and code points such as 429 (found the same day: three false 600 s pauses of grok46g)."""
    err = res.get("error")
    if err == "limit":
        return True
    if not err or err == "no-answers-object":
        return False
    return bool(LIMIT_RE.search(f"{res.get('raw') or ''} {err}"))

RESET_RE = re.compile(r"resets? in\s*(?:(\d+)\s*h)?\s*(?:(\d+)\s*m)?\s*(?:(\d+)\s*s)?", re.I)
PAUSED = DATA / "logs" / "paused.json"     # operational state, not truth: minds paused until a quota resets

def reset_seconds(res):
    """the service's own "Resets in 93h55m15s" -> seconds, or None (Claude's "resets 7am" gives no duration)"""
    m = RESET_RE.search(f"{res.get('raw') or ''} {res.get('limit_detail') or ''} {res.get('error') or ''}")
    if not m or not any(m.groups()):
        return None
    h, mi, se = (int(x) if x else 0 for x in m.groups())
    return h * 3600 + mi * 60 + se

def paused_until(m):
    try:
        return json.load(open(PAUSED)).get(m, 0)
    except Exception:
        return 0

def pause_mind(m, seconds, why):
    """found 2026-10-06: gemini38flashg's model (gemini-3.8-flash-medium) answered "Individual quota reached ...
    Resets in 93h55m15s". Backing off 600 s at a time kept its drain waiting on it for four days, so the drain's
    other minds made no calls. A limit the service says lasts longer than LIMIT_PAUSE_S pauses that mind until then."""
    try:
        d = json.load(open(PAUSED))
    except Exception:
        d = {}
    d[m] = max(d.get(m, 0), time.time() + seconds)
    PAUSED.parent.mkdir(parents=True, exist_ok=True)
    json.dump(d, open(PAUSED, "w"), indent=1)
    print(f"{dt.datetime.now():%H:%M:%S} {m}: paused for {seconds / 3600:.1f} h ({why[:100]!r})", flush=True)

def cut_short(row):
    """a timeout under a shorter limit than this mind's limit now: not an attempt at the sheet (2026-10-06: grok46g's
    limit went from 600 s to 1800 s after a quarter of its calls timed out; the sheets that ran out of attempts that
    way are asked again)"""
    if (row.get("result") or {}).get("error") != "timeout":
        return False
    then = (row.get("judge") or {}).get("timeout", 600)
    try:
        now = json.load(open(ROOT / "core" / "minds.json"))["minds"].get(row.get("mind"), {}).get("timeout", 600)
    except Exception:
        return False
    return then < now

def void_rounds():
    """rounds not to be asked any further (data/rounds/VOID.json): planned while the driving minds could not answer,
    so their questions are planned again in live rounds. Their ledgers stay, and answers already given stay answers."""
    try:
        return set(json.load(open(DATA / "rounds" / "VOID.json"))["rounds"])
    except FileNotFoundError:
        return set()

def pace(m, spec):
    """pacing for one mind from pace.json, re-read on every call: minds.<m> overrides adapters.<adapter>"""
    try:
        P = json.load(open(ROOT / "pace.json"))
    except Exception:
        P = {}
    out = dict(DEFAULT_PACE)
    out.update((P.get("adapters") or {}).get(spec["adapter"], {}))
    out.update((P.get("minds") or {}).get(m, {}))
    return out

def driver_minds(reg):
    return {m for m, s in reg["minds"].items() if s.get("family") == "claude"}

def ask_mind(rid, m, reg, stop=None, kinds=None):
    """ask one mind every sheet of round `rid` it is on and has not answered (up to MAX_ATTEMPTS calls a sheet),
    paced by pace.json -> (answered, assigned, calls made now)"""
    sys.path.insert(0, str(ROOT / "core"))
    from judges import make_judge, ADAPTER_VERSION
    rd = DATA / "rounds" / rid
    sheets = [s for s in rj(rd / "sheets.jsonl") if m in s["minds"] and (kinds is None or s["kind"] in kinds)]
    spec = reg["minds"][m]; judge = make_judge(spec)
    led = rd / "raw" / m / "ledger.jsonl"; lock = threading.Lock()
    rows = rj(led)
    by = collections.defaultdict(list)
    for r in rows:
        by[r["sid"]].append(r)
    def target(sh):
        """-> (variant,) this sheet should be asked in next, or () if nothing more to ask. A sheet's own variant
        (reasoned) is kept; a plain sheet that drew a tool attempt is re-asked as no-lookup."""
        sid = sh["sid"]; rs = by[sid]; base = sh.get("variant")
        v = "no-lookup" if base is None and any(PR.tool_attempt(r) for r in rs) else base
        if any(PR.good_row(r) for r in rs if r.get("variant") == v) or (v and any(PR.good_row(r) for r in rs)):
            return ()
        if sum(1 for r in rs if r.get("variant") == v and not limit_hit(r["result"]) and not cut_short(r)) >= MAX_ATTEMPTS[v]:
            return ()
        return (v,)
    todo = collections.deque(s for s in sheets if target(s))
    calls = [0]; streak = [0]                     # limits in a row, for this mind in this round
    if paused_until(m) > time.time():             # a quota the service says resets later: leave this mind's sheets
        todo.clear()
    def worker(i):
        while not (stop and stop()):
            if paused_until(m) > time.time():
                return
            pc = pace(m, spec)
            with lock:
                if not todo:
                    return
                if i >= pc["workers"]:                   # pace.json lowered the worker count: this one idles
                    s = None
                else:
                    s = todo.popleft()
            if s is None:
                time.sleep(5); continue
            with lock:
                t = target(s)
            if not t:
                continue
            variant = t[0]
            text = s["prompt"] if variant == s.get("variant") else PR.prompt(s, variant)
            res = judge(PR.SYSTEM, text)
            row = {"protocol": PR.PROTOCOL, "round": rid, "sid": s["sid"], "mind": m, "judge": spec,
                   "adapter_version": ADAPTER_VERSION[spec["adapter"]], "system_sha256": sha(PR.SYSTEM),
                   "prompt_sha256": sha(text), "prompt": text, "variant": variant,
                   "ts": dt.datetime.now(dt.timezone.utc).isoformat(), "result": res}
            if res.get("raw") and not res.get("error") and PR._answers(res["raw"]) is None:
                row["result"] = dict(res, error="no-answers-object")      # raw kept; re-asked
            if limit_hit(res):
                row["result"] = dict(res, error="limit", limit_detail=res.get("error"))
            with lock:
                wj(led, [row], "a")
                by[s["sid"]].append(row); calls[0] += 1
                if target(s):
                    todo.append(s)                         # re-asked after the rest, as the old resume passes did
            if limit_hit(row["result"]):
                rs = reset_seconds(row["result"])
                if rs and rs > LIMIT_PAUSE_S:
                    pause_mind(m, rs, row["result"].get("limit_detail") or row["result"].get("raw") or "")
                    return
            with lock:
                streak[0] = streak[0] + 1 if limit_hit(row["result"]) else 0
                wait = min(LIMIT_PAUSE_S, LIMIT_BACKOFF_S * 2 ** (streak[0] - 1)) if streak[0] else 0
            if wait:
                detail = row["result"].get("limit_detail") or row["result"].get("raw") or ""
                print(f"{dt.datetime.now():%H:%M:%S} {rid}/{m}: limit ({detail[:80]!r}); limit {streak[0]} in a row, pausing {wait} s", flush=True)
                t0 = time.time()
                while time.time() - t0 < wait and not (stop and stop()):
                    time.sleep(min(10, wait))
            time.sleep(pc["interval_s"])
    nmax = max(pace(m, spec)["workers"], 8)
    with cf.ThreadPoolExecutor(max_workers=nmax) as ex:
        list(ex.map(worker, range(nmax)))
    n = len({r["sid"] for r in rj(led) if PR.good_row(r)})
    return n, len(sheets), calls[0]

def cmd_ask(a):
    """ask RID: the named minds (default: every mind on the round's sheets), in parallel"""
    reg = minds()
    want = a.minds or sorted({m for s in rj(DATA / "rounds" / a.round / "sheets.jsonl") for m in s["minds"]})
    with cf.ThreadPoolExecutor(max_workers=len(want)) as ex:
        futs = {m: ex.submit(ask_mind, a.round, m, reg) for m in want}
        for m, f in futs.items():
            n, tot, _ = f.result()
            print(f"{a.round}/{m}: {n}/{tot} sheets answered", flush=True)

def ctx_rounds():
    """context rounds in order, by number (c1000 after c999: a three-digit glob and a string sort would have stalled the
    loop there; planner audit 2026-10-06)"""
    return sorted((p.name for p in (DATA / "rounds").iterdir() if p.is_dir() and p.name[:1] == "c" and p.name[1:].isdigit()
                   and (p / "sheets.jsonl").exists()), key=lambda n: int(n[1:]))

def test_rounds():
    """pre-registered test rounds (p001, ...): a fixed set of questions asked once to named minds, to check a prediction
    written before they were asked (first: the family-disagreement spike's flat splits, 2026-10-06). Not planned and
    not drained; recorded and committed with the context rounds, and their answers are ordinary evidence."""
    return sorted((p.name for p in (DATA / "rounds").iterdir() if p.is_dir() and p.name[:1] == "p" and p.name[1:].isdigit()
                   and (p / "sheets.jsonl").exists()), key=lambda n: int(n[1:]))

def cmd_drain(a):
    """drain --minds m ...: until STOP, ask these minds' open sheets, oldest round first; idle when caught up.
    --newest-first: newest round first. --kinds-first K ...: first the sheets of these question kinds (every round, in
    round order), then the rest. (Joseph, 2026-10-06, for Gemini: "Go ahead and have Gemini prioritize newer
    questions": at its pacing it never reached the kinds asked from c015 on -- cohere, picks, order -- and it is the
    only non-Claude mind that answers without thinking.) After each pass it starts again from the top, so the newest
    work always comes first."""
    reg = minds(); stopf = DATA / "rounds" / "STOP"
    stop = stopf.exists
    passes = [set(a.kinds_first), None] if a.kinds_first else [None]
    while not stop():
        worked = False
        void = void_rounds()
        rounds = [r for r in ctx_rounds() if r not in void]
        if a.newest_first:
            rounds = rounds[::-1]
        for kinds in passes:
            for rid in rounds:
                if stop():
                    break
                with cf.ThreadPoolExecutor(max_workers=len(a.minds)) as ex:
                    res = dict(zip(a.minds, ex.map(lambda m: ask_mind(rid, m, reg, stop, kinds), a.minds)))
                line = ", ".join(f"{m} {n}/{t} ({c} calls)" for m, (n, t, c) in res.items() if c)
                if line:
                    print(f"{dt.datetime.now():%H:%M:%S} drain {rid}{' ' + ','.join(sorted(kinds)) if kinds else ''}: {line}", flush=True)
                    worked = True
                    break                                   # back to the top: the newest work first
            if worked:
                break
        time.sleep(10 if worked else 120)
    print("== drain: STOP found", flush=True)

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
    import importlib
    importlib.reload(BE)          # a read-off nothing reads back: safe to pick up its latest code every round
    BE.main()

SETTLED_AGREEMENT = 0.75     # read-off only (PROGRESS): a sequence counts as settled when every walked step has at
                             # least this agreement and it walked >= 3 steps; chosen without evidence, gates nothing

def cmd_progress(a):
    recs = answers()
    order = sorted({r["round"] for r in recs if r["round"][:1] in "rc"}, key=lambda x: (x[0] != "r", int("".join(c for c in x[1:] if c.isdigit()) or 0), x))
    extra = {r["round"] for r in recs if r["round"] != "seed" and r["round"][:1] not in "rc"}   # test rounds: no row of their
                                     # own; like answers drained later, they count from the next row computed after they arrive
    seedrecs = [r for r in recs if r["round"] == "seed"]
    # A row is the tree as it stood when its round closed: every answer recorded by then, for that round and earlier
    # ones (plus the seed votes). It is computed once and kept. Answers drained later into earlier rounds count from the
    # next row computed after they arrive. (2026-10-06: rebuilding every row every round had grown to 11 minutes of a
    # 25-minute round; a cumulative content signature didn't help, because the drains append to old rounds all the time
    # and every row after the touched round went stale.) Only a round with no row yet is computed.
    by_round = collections.defaultdict(list)
    for r in recs:
        by_round[r["round"]].append(r)
    def content(rs):
        return hashlib.sha256("\n".join(sorted(json.dumps(r, sort_keys=True, ensure_ascii=False) for r in rs)).encode()).hexdigest()
    try:
        cache = {row["round"]: row for row in json.load(open(DATA / "tree" / "progress.json")) if row.get("sig")}
    except Exception:
        cache = {}
    sig = content(seedrecs)
    rows = []
    for i, rid in enumerate(order):
        sig = hashlib.sha256((sig + content(by_round[rid])).encode()).hexdigest()
        if rid in cache:
            rows.append(cache[rid]); continue
        upto = set(order[:i + 1]) | extra
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
                     "inhibit": sum(1 for r in recs if r["round"] == rid and r["kind"] == "inhibit"), "sig": sig})
    L = ["# Progress by round", "",
         f"*Generated by `run.py progress`: each row is the context tree as it stood when that round closed, from every answer recorded by then for that round and earlier ones (r000–r012 are the ported triad era; c001 on are context-tree rounds). Rows are computed once: answers drained later into earlier rounds count from the next row on. Rows before c096 were computed under an earlier rule and may include answers drained after their round closed. Seed votes (the survey sequences, tagged) are included in every row; *settled without seeds* rebuilds the tree from real answers only. **Settled** is a read-off that gates nothing: a sequence whose walk took at least 3 steps, each agreed at ≥ {SETTLED_AGREEMENT}. **k\\* known:** walked steps whose shortest sufficient context is pinned down. **Ends** count the stops of every walk: *open* is never asked, *end* is the minds saying none, *wrap* is a return to a glyph already in the path. **Cycles:** manifested, with ≥ 4 distinct glyphs (≥ 2 families).*", "",
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
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)

def commit(rid):
    """the round just planned, plus every earlier round's ledgers (drain minds keep appending to them)"""
    paths = [f"data/rounds/{r}" for r in ctx_rounds() + test_rounds()] + ["SEQUENCES.md", "PROGRESS.md", "BEST.md", "CATALOG-VIEW.md", "CATALOG-GIVEN.md", "data/catalog"]   # relative to ROOT (git -C); data/catalog: manifests only (.gitignore)
    git("add", *paths)
    if git("diff", "--cached", "--quiet", "--", *paths).returncode == 0:
        return None                                          # nothing new (e.g. a resumed round already committed)
    r = git("commit", "-q", "-m", f"empirica/glyph-sequence: context-tree round {rid} (planned, Claude answered; drained answers "
            "of earlier rounds; SEQUENCES + PROGRESS)\n\n"
            "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n"
            "Claude-Session: https://claude.ai/code/session_019jmniPAmbTD5NxnH7FPY9v", "--", *paths)
    return r.returncode == 0

def cmd_record_all(a):
    for rid in ctx_rounds() + test_rounds():
        cmd_record(argparse.Namespace(round=rid))

def cmd_catalog(a):
    """rebuild the catalog (concern 6) into Postgres, so a current one is always there for its readers (2026-10-06:
    about a minute). A failed build is reported and the round goes on: no reader depends on it yet."""
    r = subprocess.run([sys.executable, str(ROOT / "catalog" / "build.py")], capture_output=True, text=True)
    tail = (r.stdout + r.stderr).strip().splitlines()[-2:]
    print(("catalog: " if r.returncode == 0 else "!! catalog build failed: ") + " | ".join(tail)[:300], flush=True)
    if r.returncode == 0:                         # read-offs of the catalog: the default view (CATALOG §11, runs that
        for rep in ("view.py", "given.py"):       # aren't given walks) and the givens page
            v = subprocess.run([sys.executable, str(ROOT / "report" / rep)], capture_output=True, text=True)
            print(((v.stdout + v.stderr).strip().splitlines() or [rep + ": no output"])[-1][:300] if v.returncode == 0
                  else f"!! {rep} failed: " + (v.stderr.strip().splitlines() or ["?"])[-1][:300], flush=True)
    builds = sorted(p for p in (DATA / "catalog").iterdir() if p.is_dir() and p.name.startswith("b"))
    for old in builds[:-CATALOG_KEEP]:            # each build's CSVs are ~45 MB: keep the last few; manifests stay
        for f in old.iterdir():
            if f.name != "manifest.json":
                f.unlink()

CATALOG_KEEP = 3          # builds whose tables stay on disk (Postgres holds the current one and the one before)

def cmd_round(a, resume=False):
    """plan (unless resuming a planned round), ask the drivers, record every round, tree, progress, commit. Asking
    resumes from the ledgers, so a loop restarted mid-round finishes that round before planning the next."""
    drivers = sorted(driver_minds(minds()))
    steps = (() if resume else ((cmd_plan, a),)) + ((cmd_ask, argparse.Namespace(round=a.round, minds=drivers)),
             (cmd_record_all, a), (cmd_tree, a), (cmd_progress, a), (cmd_catalog, a))
    for f, aa in steps:
        print(f"== {a.round} {f.__name__} {dt.datetime.now():%H:%M:%S}", flush=True)
        f(aa)
    c = commit(a.round)
    print(f"== {a.round} committed" if c else (f"== {a.round} nothing new to commit" if c is None else f"!! {a.round} commit failed"), flush=True)

def cmd_loop(a):
    done = ctx_rounds()
    if done and not (DATA / "rounds" / "STOP").exists():          # finish the last round first (a restart mid-round)
        print(f"== {done[-1]} resumed {dt.datetime.now():%H:%M:%S}", flush=True)
        cmd_round(argparse.Namespace(round=done[-1], budget=a.budget), resume=True)
        round_gap()
    while not (DATA / "rounds" / "STOP").exists():
        done = ctx_rounds()
        rid = f"c{(int(done[-1][1:]) + 1) if done else 1:03d}"
        try:
            cmd_round(argparse.Namespace(round=rid, budget=a.budget))
        except Exception as ex:
            print(f"!! {rid} failed: {ex!r}", flush=True); raise
        round_gap()
    print("== STOP found", flush=True)

def round_gap():
    """pause between rounds: pace.json round_gap_min, re-read every 30 s (so lowering it shortens a wait already under
    way); cut short by STOP"""
    t0 = time.time()
    while not (DATA / "rounds" / "STOP").exists():
        try:
            gap = json.load(open(ROOT / "pace.json")).get("round_gap_min", 0)
        except Exception:
            gap = 0
        if time.time() >= t0 + 60 * gap:
            return
        time.sleep(30)

MIN_UNICODE = 16          # what counts as a glyph is unicodedata's call (probe.is_glyph): on older data a newer character
                          # reads as unassigned, so it can never be asked and an answer naming it is cut there. Found
                          # 2026-10-05: everything through c002 ran on mise's Python 3.11 (Unicode 14); Homebrew's 3.14 has 16.

def main():
    import unicodedata
    if int(unicodedata.unidata_version.split(".")[0]) < MIN_UNICODE:
        sys.exit(f"run.py: this Python's Unicode data is {unicodedata.unidata_version}; it needs {MIN_UNICODE}+. "
                 "On Joseph's machine: /opt/homebrew/bin/python3 run.py ...")
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(required=True)
    p = sub.add_parser("plan"); p.add_argument("round"); p.add_argument("--budget", type=int, default=700); p.set_defaults(f=cmd_plan)
    p = sub.add_parser("ask"); p.add_argument("round"); p.add_argument("--minds", nargs="*"); p.set_defaults(f=cmd_ask)
    p = sub.add_parser("record"); p.add_argument("round"); p.set_defaults(f=cmd_record)
    p = sub.add_parser("tree"); p.set_defaults(f=cmd_tree)
    p = sub.add_parser("progress"); p.set_defaults(f=cmd_progress)
    p = sub.add_parser("round"); p.add_argument("round"); p.add_argument("--budget", type=int, default=700); p.set_defaults(f=cmd_round)
    p = sub.add_parser("loop"); p.add_argument("--budget", type=int, default=700); p.set_defaults(f=cmd_loop)
    p = sub.add_parser("drain"); p.add_argument("--minds", nargs="+", required=True)
    p.add_argument("--newest-first", action="store_true"); p.add_argument("--kinds-first", nargs="*", default=[])
    p.set_defaults(f=cmd_drain)
    a = ap.parse_args(); a.f(a)

if __name__ == "__main__":
    main()
