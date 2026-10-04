#!/usr/bin/env python3
"""The 2026-08-25 stochastic walk, run as recorded (see harness/walk/METHOD.md for every source).

  walk.py pool   r1                         seed pool: all survey-record glyphs + uniform long-tail dilution
  walk.py pairs  r1                         round 1: uniform random pairs over the pool (~8 comparisons/glyph)
  walk.py pairs  rN --from r1 [r2 ...]      densification round: 60% within structured 2-hop neighbourhoods,
                                            25% structured-vs-pool, 15% uniform long tail (pilot walk2/walk4)
  walk.py triads rN --from r1 [...]         triad round, same mixture; reverse cycles split across a judge pair (walk5)
  walk.py run    rN JUDGE [--workers N]     one fresh judge instance per sheet; append-only ledger; resumable
  walk.py graph  r1 [r2 ...] [--judges ..]  edges (both presentations name the same winner), ties, ⟂, chains

Pair rounds put both orders of a pair on the SAME sheet, shuffled (pilot walk1–4; Joseph 08-25: "make sure anything
stochastically in there left()right is also in a nearby one or even the same answer-sheet as right()left").
Triad rounds give judge 2p the cycle AB,BC,CA and judge 2p+1 the reverse BA,CB,AC (pilot walk5).
Response set: glyph + felt distance (somewhat/much/vastly), ≈, ⟂; option order permuted per sheet (walk5b);
glyph-echo with word fallbacks; ≈ ⟂ ⊥ banned from stimuli (DESIGN fix #1). No prior orderings, families or
expected values enter sampling or edge-finding (Joseph 08-25; discover2.py).
"""
import argparse, collections, concurrent.futures as cf, datetime as dt, glob, hashlib, json, pathlib, sys, threading
import unicodedata as U

HERE = pathlib.Path(__file__).resolve().parent
EXP = HERE.parents[1]
sys.path.insert(0, str(EXP / "harness/runner"))
import instruments as I
from fate import rng, digest
from judges import make_judge, ADAPTER_VERSION

PROTOCOL = "gmp-walk-0.1"
WALK = EXP / "data/walk"
SHEET = 40          # presentations per sheet (one judge instance per sheet)
BANNED = {"≈", "⟂", "⊥"}

def ok_glyph(ch):
    return (len(ch) == 1 and U.category(ch)[0] in "LNPS" and ch not in BANNED
            and not (0xFE00 <= ord(ch) <= 0xFE0F) and not ch.isspace())

# ------------------------------------------------------------------ pool
def survey_glyphs():
    out = {}
    files = sorted(glob.glob(str(EXP / "data/surveys-v1/extracted/*.jsonl"))) + \
            sorted(glob.glob(str(EXP / "data/surveys-v1/extracted/corrections/*.jsonl")))
    for f in files:
        for line in open(f):
            if not line.strip():
                continue
            r = json.loads(line)
            chars = []
            cps = r.get("codepoints")
            if isinstance(cps, list) and cps:
                for c in cps:
                    if isinstance(c, str) and c.startswith("U+"):
                        try:
                            chars.append(chr(int(c[2:].split()[0], 16)))
                        except ValueError:
                            pass
            else:
                chars = [c for c in str(r.get("glyphs") or "") if ord(c) > 0x7F]
            for ch in chars:
                if ok_glyph(ch):
                    out.setdefault(ch, set()).add(r["id"])
    return out

def tail_glyph(r):
    """The pilot's long-tail sampler (walk2/walk4/walk5 rand_glyph), verbatim ranges."""
    while True:
        cp = r.choice([r.randint(0x20, 0x2BFF), r.randint(0x1F000, 0x1FBFF),
                       r.randint(0x2E80, 0x33FF), r.randint(0x1D300, 0x1D7FF)])
        ch = chr(cp)
        try:
            U.name(ch)
        except ValueError:
            continue
        if ok_glyph(ch):
            return ch

def cmd_pool(a):
    d = WALK / a.round; d.mkdir(parents=True, exist_ok=True)
    seeds = survey_glyphs()
    n_tail = round(len(seeds) * 90 / 188)   # the pilot's dilution ratio (188 prior + 90 random)
    tail, i = [], 0
    while len(tail) < n_tail:
        ch = tail_glyph(rng(PROTOCOL, "pool-tail", {"round": a.round, "i": i})); i += 1
        if ch not in seeds and ch not in tail:
            tail.append(ch)
    pool = {"protocol": PROTOCOL, "round": a.round, "unicode_version": U.unidata_version,
            "seed": sorted(seeds), "seed_records": {g: sorted(v) for g, v in sorted(seeds.items())}, "tail": tail,
            "rule": "seed = every L/N/P/S glyph named by any surveys-v1 record (all types, all 7 surveys, plus capture-"
                    "corrections), minus ≈⟂⊥ and variation selectors; tail = the pilot's long-tail sampler, sized at the "
                    "pilot's dilution ratio 90/188 of the seed count. Lineage per glyph: survey-seed | uniform-tail."}
    json.dump(pool, open(d / "pool.json", "w"), ensure_ascii=False, indent=0)
    print(f"{a.round}: {len(seeds)} seed glyphs + {len(tail)} tail glyphs = {len(seeds) + len(tail)}")

# ------------------------------------------------------------------ sampling
def load_pool(rounds):
    pool, lineage = [], {}
    for rd in rounds:
        p = WALK / rd / "pool.json"
        if p.exists():
            P = json.load(open(p))
            for g in P["seed"]:
                lineage.setdefault(g, "survey-seed")
            for g in P["tail"]:
                lineage.setdefault(g, "uniform-tail")
        sp = WALK / rd / "stimuli.jsonl"
        if sp.exists():
            for line in open(sp):
                s = json.loads(line)
                for g in s["glyphs"]:
                    lineage.setdefault(g, s.get("lineage", {}).get(g, "uniform-tail"))
    pool = sorted(lineage)
    return pool, lineage

def write_pair_sheets(rd, pairs, lineage, kind):
    """pairs: list of (a,b). Both orders of each pair on the same sheet; sheets shuffled (fated)."""
    d = WALK / rd; d.mkdir(parents=True, exist_ok=True)
    r = rng(PROTOCOL, "pair-order", {"round": rd, "n": len(pairs)})
    pairs = list(pairs); r.shuffle(pairs)
    per = SHEET // 2
    with open(d / "stimuli.jsonl", "w") as f:
        for s in range(0, len(pairs), per):
            chunk = pairs[s:s + per]
            items = []
            for k, (x, y) in enumerate(chunk):
                items.append({"pair": k, "order": 0, "a": x, "b": y})
                items.append({"pair": k, "order": 1, "a": y, "b": x})
            rng(PROTOCOL, "sheet-shuffle", {"round": rd, "sheet": s // per}).shuffle(items)
            for i, it in enumerate(items):
                it["id"] = i
            glyphs = sorted({g for p in chunk for g in p})
            row = {"round": rd, "kind": kind, "sheet": s // per, "items": items,
                   "glyphs": glyphs, "lineage": {g: lineage.get(g, "uniform-tail") for g in glyphs}}
            row["sid"] = "W" + digest({"p": PROTOCOL, **{k: row[k] for k in ("round", "sheet", "items")}})[:12]
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"{rd}: {len(pairs)} pairs -> {(len(pairs) + per - 1) // per} sheets of {SHEET}")

def structure(prev_rounds, judges=None):
    """Glyphs in any consistent directed edge, from any judge, in earlier rounds; adjacency over those edges."""
    E = edges(prev_rounds, judges)
    adj = collections.defaultdict(set)
    for (j, lo, hi) in E["dir"]:
        adj[lo].add(hi); adj[hi].add(lo)
    return adj

def cmd_pairs(a):
    if not a.frm:
        pool, lineage = load_pool([a.round])
        N = len(pool)
        target = N * 4  # ~8 comparisons per glyph (pilot round 1)
        pairs, k = set(), 0
        while len(pairs) < target:
            r = rng(PROTOCOL, "r1-pair", {"round": a.round, "k": k}); k += 1
            i, j = r.sample(range(N), 2)
            pairs.add((pool[min(i, j)], pool[max(i, j)]))
        write_pair_sheets(a.round, sorted(pairs), lineage, "uniform")
        return
    pool, lineage = load_pool(a.frm)
    adj = structure(a.frm)
    structured = sorted(adj)
    n = a.n
    pairs, k = set(), 0
    def add(x, y):
        if x != y:
            pairs.add(tuple(sorted((x, y))))
    while len(pairs) < round(n * 0.60):   # densify within structured neighbourhoods, 2-hop mixing
        r = rng(PROTOCOL, "dense", {"round": a.round, "k": k}); k += 1
        x = r.choice(structured)
        nb = sorted((adj[x] | {z for y in adj[x] for z in adj[y]}) - {x})
        add(x, r.choice(nb) if nb and r.random() < 0.7 else r.choice(structured))
    while len(pairs) < round(n * 0.85):   # structured vs anywhere in pool
        r = rng(PROTOCOL, "struct-pool", {"round": a.round, "k": k}); k += 1
        add(r.choice(structured), r.choice(pool))
    while len(pairs) < n:                 # pure long tail
        r = rng(PROTOCOL, "tail", {"round": a.round, "k": k}); k += 1
        x = tail_glyph(r); y = tail_glyph(r) if r.random() < 0.5 else r.choice(pool)
        lineage.setdefault(x, "uniform-tail"); lineage.setdefault(y, "uniform-tail")
        add(x, y)
    write_pair_sheets(a.round, sorted(pairs), lineage, "mixture-60/25/15")

def cmd_triads(a):
    pool, lineage = load_pool(a.frm)
    adj = structure(a.frm)
    structured = sorted(adj)
    triads, seen, k = [], set(), 0
    def add(t):
        if len(set(t)) == 3 and frozenset(t) not in seen:
            seen.add(frozenset(t)); triads.append(tuple(t))
    n = a.n
    while len(triads) < round(n * 0.60):
        r = rng(PROTOCOL, "tri-dense", {"round": a.round, "k": k}); k += 1
        x = r.choice(structured)
        nb = sorted((adj[x] | {z for y in adj[x] for z in adj[y]}) - {x})
        add([x] + (r.sample(nb, 2) if len(nb) >= 2 else r.sample(structured, 2)))
    while len(triads) < round(n * 0.85):
        r = rng(PROTOCOL, "tri-wild", {"round": a.round, "k": k}); k += 1
        g = tail_glyph(r); lineage.setdefault(g, "uniform-tail")
        add([r.choice(structured), r.choice(structured), g])
    while len(triads) < n:
        r = rng(PROTOCOL, "tri-tail", {"round": a.round, "k": k}); k += 1
        g1, g2 = tail_glyph(r), tail_glyph(r)
        g3 = r.choice(structured + [tail_glyph(r)])
        for g in (g1, g2, g3):
            lineage.setdefault(g, "uniform-tail")
        add([g1, g2, g3])
    rng(PROTOCOL, "triad-order", {"round": a.round}).shuffle(triads)
    d = WALK / a.round; d.mkdir(parents=True, exist_ok=True)
    per = SHEET // 3  # triads per sheet
    with open(d / "stimuli.jsonl", "w") as f:
        for s in range(0, len(triads), per):
            chunk = triads[s:s + per]
            for side in (0, 1):   # the complementary judge pair: cycle / reverse cycle
                items = []
                for t, (A, B, C) in enumerate(chunk):
                    prs = ((A, B), (B, C), (C, A)) if side == 0 else ((B, A), (C, B), (A, C))
                    for x, y in prs:
                        items.append({"triad": s + t, "side": side, "a": x, "b": y})
                rng(PROTOCOL, "sheet-shuffle", {"round": a.round, "sheet": s // per, "side": side}).shuffle(items)
                for i, it in enumerate(items):
                    it["id"] = i
                glyphs = sorted({g for t in chunk for g in t})
                row = {"round": a.round, "kind": "triads-60/25/15", "sheet": f"{s // per}{'ab'[side]}", "items": items,
                       "triads": [list(t) for t in chunk], "glyphs": glyphs,
                       "lineage": {g: lineage.get(g, "uniform-tail") for g in glyphs}}
                row["sid"] = "T" + digest({"p": PROTOCOL, **{k: row[k] for k in ("round", "sheet", "items")}})[:12]
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"{a.round}: {len(triads)} triads -> {2 * ((len(triads) + per - 1) // per)} sheets")

# ------------------------------------------------------------------ run
def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()

def cmd_run(a):
    judges = json.load(open(EXP / "harness/runner/judges-v1.json"))
    jspec = judges["judges"][a.judge]
    sheets = [json.loads(l) for l in open(WALK / a.round / "stimuli.jsonl")]
    rdir = WALK / a.round / "runs" / a.judge; rdir.mkdir(parents=True, exist_ok=True)
    spec = {"protocol": PROTOCOL, "round": a.round, "judge_label": a.judge, "judge": jspec,
            "adapter_version": ADAPTER_VERSION[jspec["adapter"]], "system_prompt": I.SYSTEM,
            "stimulus_digest": digest(sheets), "format": "perp", "sheet_size": SHEET,
            "context_residue": judges.get("context_residue", {}).get(jspec["adapter"]),
            "created": dt.datetime.now(dt.timezone.utc).isoformat()}
    sp = rdir / "spec.json"
    if sp.exists():
        old = json.load(open(sp))
        for k in ("protocol", "judge", "stimulus_digest", "adapter_version"):
            if old.get(k) != spec[k]:
                sys.exit(f"refusing to resume: {k} differs")
    else:
        json.dump(spec, open(sp, "w"), ensure_ascii=False, indent=1)
    ledger = rdir / "ledger.jsonl"
    done = set()
    if ledger.exists():
        for line in open(ledger):
            r = json.loads(line)
            if r["result"].get("raw") and not r["result"].get("error") and r.get("sheet_incomplete") is None:
                done.add(r["sid"])
    todo = [s for s in sheets if s["sid"] not in done]
    if a.limit:
        todo = todo[:a.limit]
    print(f"{a.round}/{a.judge}: {len(sheets)} sheets, {len(done)} done, {len(todo)} to run", flush=True)
    judge = make_judge(jspec); lock = threading.Lock(); sys_sha = sha(I.SYSTEM)
    cnt = collections.Counter()
    def one(s):
        items = [{"id": it["id"], "a": it["a"], "b": it["b"]} for it in s["items"]]
        prompt = I.sheet_prompt(items, "perp", {"protocol": PROTOCOL, "sid": s["sid"]})
        res = judge(I.SYSTEM, prompt)
        inc = None
        if res.get("raw") and not res.get("error"):
            p = I.parse_sheet(res["raw"], items)
            cov = sum(1 for v in p.values() if v[0] != "unparsed") / max(1, len(items))
            if cov < 0.9:
                inc = round(cov, 3)
        row = {"protocol": PROTOCOL, "round": a.round, "sid": s["sid"], "sheet": s["sheet"], "judge_label": a.judge,
               "sheet_incomplete": inc, "prompt_sha256": sha(prompt), "prompt": prompt, "system_sha256": sys_sha,
               "ts": dt.datetime.now(dt.timezone.utc).isoformat(), "result": res}
        with lock:
            with open(ledger, "a") as f:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
        return "ok" if (res.get("raw") and not res.get("error") and inc is None) else "retry"
    with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:
        for i, st in enumerate(ex.map(one, todo)):
            cnt[st] += 1
            if (i + 1) % 25 == 0:
                print(f"  {i + 1}/{len(todo)} {dict(cnt)}", flush=True)
    print(f"{a.round}/{a.judge}: finished {dict(cnt)} (re-run to re-ask incomplete or failed sheets)", flush=True)

# ------------------------------------------------------------------ graph
def presentations(rounds, judges=None):
    """-> list of (round, judge, sheet-row, item, verdict) over valid ledger rows (last valid answer per sheet)."""
    out = []
    for rd in rounds:
        sheets = {json.loads(l)["sid"]: json.loads(l) for l in open(WALK / rd / "stimuli.jsonl")}
        for jd in sorted((WALK / rd / "runs").glob("*")):
            j = jd.name
            if judges and j not in judges:
                continue
            last = {}
            for line in open(jd / "ledger.jsonl"):
                r = json.loads(line)
                if r["result"].get("raw") and not r["result"].get("error") and r.get("sheet_incomplete") is None:
                    last[r["sid"]] = r
            for sid, r in last.items():
                s = sheets[sid]
                items = [{"id": it["id"], "a": it["a"], "b": it["b"]} for it in s["items"]]
                p = I.parse_sheet(r["result"]["raw"], items)
                for it in s["items"]:
                    out.append((rd, j, s, it, p.get(it["id"], ("unparsed", None, None))))
    return out

def edges(rounds, judges=None):
    """Pair rounds: an edge needs both orders (same judge instance, same sheet) to name the same winner.
    Triad rounds: an edge needs the two complementary judges' reverse presentations to name the same winner."""
    P = presentations(rounds, judges)
    E = {"dir": collections.Counter(), "tie": collections.Counter(), "perp": collections.Counter(),
         "mixed": collections.Counter(), "flip": collections.Counter(), "unparsed": collections.Counter(), "by": collections.defaultdict(list)}
    grp = collections.defaultdict(list)
    for rd, j, s, it, v in P:
        if "pair" in it:
            grp[(rd, j, s["sid"], it["pair"])].append((it, v))
        else:
            # triads: match cycle sheet 'Na' with reverse sheet 'Nb' of the SAME judge label (two fresh instances)
            grp[(rd, j, str(s["sheet"])[:-1], it["triad"], frozenset((it["a"], it["b"])))].append((it, v))
    for key, lst in grp.items():
        j = key[1]
        if len(lst) != 2:
            continue
        (i0, v0), (i1, v1) = lst
        k = frozenset((i0["a"], i0["b"]))
        kinds = (v0[0], v1[0])
        if "unparsed" in kinds:
            E["unparsed"][(j, k)] += 1
        elif kinds == ("dir", "dir"):
            if v0[1] == v1[1]:
                hi = v0[1]; lo = next(g for g in k if g != hi)
                E["dir"][(j, lo, hi)] += 1
                E["by"][(j, lo, hi)] += [v0[2], v1[2]]
            else:
                E["flip"][(j, k)] += 1
        elif kinds == ("perp", "perp"):
            E["perp"][(j, k)] += 1
        elif kinds == ("tie", "tie"):
            E["tie"][(j, k)] += 1
        else:
            E["mixed"][(j, k)] += 1
    return E

def chains(dir_edges):
    succ = collections.defaultdict(set)
    for (lo, hi) in dir_edges:
        succ[lo].add(hi)
    memo, onpath = {}, set()
    def lf(n):
        if n in memo:
            return memo[n]
        if n in onpath:
            return []
        onpath.add(n); best = []
        for m in sorted(succ.get(n, ())):
            p = lf(m)
            if len(p) > len(best):
                best = p
        onpath.discard(n); memo[n] = [n] + best
        return memo[n]
    nodes = set(succ) | {m for v in succ.values() for m in v}
    out, seen = [], set()
    for ch in sorted((lf(n) for n in sorted(nodes)), key=len, reverse=True):
        if len(ch) < 3:
            break
        if len(set(ch) & seen) > len(ch) // 2:
            continue
        seen.update(ch); out.append(ch)
    return out

def cmd_graph(a):
    E = edges(a.rounds, a.judges)
    js = sorted({k[0] for c in ("dir", "tie", "perp", "mixed", "flip", "unparsed") for k in E[c]})
    print("judge                 dir   tie   perp  mixed  flip  unparsed")
    for j in js:
        c = {cat: sum(v for k, v in E[cat].items() if k[0] == j) for cat in ("dir", "tie", "perp", "mixed", "flip", "unparsed")}
        print(f"{j:20s} {c['dir']:5d} {c['tie']:5d} {c['perp']:6d} {c['mixed']:6d} {c['flip']:5d} {c['unparsed']:8d}")
    # cross-judge agreement on edges both committed
    per = collections.defaultdict(dict)
    for (j, lo, hi) in E["dir"]:
        per[j][frozenset((lo, hi))] = hi
    print("\ncross-judge: same winner / both committed")
    for i, x in enumerate(js):
        for y in js[i + 1:]:
            both = set(per[x]) & set(per[y])
            if both:
                print(f"  {x:18s} {y:18s} {sum(per[x][k] == per[y][k] for k in both)}/{len(both)}")
    # consensus: edges committed by >= 2 judges with no judge committing the opposite direction
    votes = collections.defaultdict(collections.Counter)
    for (j, lo, hi) in E["dir"]:
        votes[frozenset((lo, hi))][hi] += 1
    cons = [(next(g for g in k if g != w), w) for k, c in votes.items() for w, n in c.items() if n >= 2 and len(c) == 1]
    print(f"\nconsensus edges (>=2 judges, none opposed): {len(cons)}")
    for ch in chains(cons)[:a.top]:
        print(f"  [{len(ch)}] {''.join(ch)}")

def main():
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("pool"); p.add_argument("round"); p.set_defaults(f=cmd_pool)
    p = sub.add_parser("pairs"); p.add_argument("round"); p.add_argument("--from", dest="frm", nargs="*", default=[])
    p.add_argument("--n", type=int, default=0); p.set_defaults(f=cmd_pairs)
    p = sub.add_parser("triads"); p.add_argument("round"); p.add_argument("--from", dest="frm", nargs="+", required=True)
    p.add_argument("--n", type=int, default=600); p.set_defaults(f=cmd_triads)
    p = sub.add_parser("run"); p.add_argument("round"); p.add_argument("judge")
    p.add_argument("--workers", type=int, default=4); p.add_argument("--limit", type=int, default=0); p.set_defaults(f=cmd_run)
    p = sub.add_parser("graph"); p.add_argument("rounds", nargs="+"); p.add_argument("--judges", nargs="*")
    p.add_argument("--top", type=int, default=40); p.set_defaults(f=cmd_graph)
    a = ap.parse_args(); a.f(a)

if __name__ == "__main__":
    main()
