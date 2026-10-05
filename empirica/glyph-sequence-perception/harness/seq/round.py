#!/usr/bin/env python3
"""Round driver (PLAN.md §5).

  round.py [--data DIR] init [--synth]           pool + seeds (real: surveys + data/seeds/ + uniform tail;
                                                  --synth: the synthetic world)
  round.py [--data DIR] plan RID [--budget N]    draw a round from the queue -> items, presentations, sheets
  round.py [--data DIR] run RID [--minds ...] [--synth] [--workers N]
                                                  send sheets; append-only ledgers; resumable
  round.py [--data DIR] analyze RID              parse every round so far, fit (anneal), write fit + report
  round.py [--data DIR] loop N --synth           init/plan/run/analyze N rounds against synthetic minds

Truth is the JSONL under DIR (default: <study>/data). Everything else is rebuilt from it.
"""
import argparse, collections, concurrent.futures as cf, datetime as dt, hashlib, json, math, pathlib, sys, threading
import unicodedata as U
from common import EXP, PROTOCOL, R, read_jsonl, write_jsonl, append_jsonl, ok_glyph, minds as load_minds, uid
import items as I
import parse as P
import model as M
import squeue as Q
import growth as G

def D(a):
    return pathlib.Path(a.data) if a.data else EXP / "data"

def rounds(d):
    return sorted(p.name for p in (d / "rounds").glob("r*") if p.is_dir())

# ------------------------------------------------------------------ init
def survey_seeds():
    out = []
    for f in sorted((EXP / "data/surveys-v1/extracted").glob("*.jsonl")) + sorted((EXP / "data/surveys-v1/extracted/corrections").glob("*.jsonl")):
        for r in read_jsonl(f):
            g = []
            cps = r.get("codepoints")
            if isinstance(cps, list):
                for c in cps:
                    if isinstance(c, str) and c.startswith("U+"):
                        try:
                            g.append(chr(int(c[2:].split()[0], 16)))
                        except ValueError:
                            pass
            g = [x for x in dict.fromkeys(g) if ok_glyph(x)]
            if len(g) >= 2:
                out.append({"sid": "survey:" + r["id"], "glyphs": g, "bump": 1.5,
                            "type": r.get("type") or r.get("record_type"), "surveyor": r.get("surveyor")})
    return out

def domain_seeds():
    out = []
    for f in sorted((EXP / "data/seeds").glob("*.jsonl")):
        for r in read_jsonl(f):
            if r.get("retracts"):
                continue
            g = [x for x in (r["glyphs"] if isinstance(r["glyphs"], list) else list(r["glyphs"])) if ok_glyph(x)]
            if r["kind"] == "lattice":
                # a lattice is a triad generator: sample chains along each factor, and across them
                cells, fac = r["cells"], r["factors"]
                names = list(fac)
                for fi, fname in enumerate(names):
                    other = names[1 - fi]
                    for ov in fac[other]:
                        chain = [cells[f"{v}|{ov}" if fi == 0 else f"{ov}|{v}"] for v in fac[fname]
                                 if (f"{v}|{ov}" if fi == 0 else f"{ov}|{v}") in cells]
                        out.append({"sid": f"{r['id']}:{fname}@{ov}", "glyphs": chain, "bump": r.get("bump", 2.0), "type": "lattice"})
            else:
                out.append({"sid": r["id"], "glyphs": g, "bump": r.get("bump", 2.0), "type": r["kind"]})
    return out

def tail_glyphs(n, exclude):
    """The pilot's long-tail sampler ranges (walk2/4/5), fated."""
    out, i = [], 0
    while len(out) < n:
        r = R("pool-tail", {"i": i}); i += 1
        cp = r.choice([r.randint(0x20, 0x2BFF), r.randint(0x1F000, 0x1FBFF), r.randint(0x2E80, 0x33FF), r.randint(0x1D300, 0x1D7FF)])
        ch = chr(cp)
        try:
            U.name(ch)
        except ValueError:
            continue
        if ok_glyph(ch) and ch not in exclude and ch not in out:
            out.append(ch)
    return out

def cmd_init(a):
    d = D(a)
    if a.synth:
        import synth as S
        w = S.world_default()
        seeds = [dict(s, bump=1.5) for s in w["seeds"]]
        pool = {g: "seed" for s in seeds for g in s["glyphs"]}
        planted = {g: "planted" for s in w["seqs"].values() for st in s for g in st}
        for g in list(planted) + w["distractors"]:
            pool.setdefault(g, "tail")
        d.mkdir(parents=True, exist_ok=True)
        json.dump({"world": w}, open(d / "world.json", "w"), ensure_ascii=False)
    else:
        seeds = survey_seeds() + domain_seeds()
        pool = {g: "seed" for s in seeds for g in s["glyphs"]}
        for g in tail_glyphs(round(len(pool) * 90 / 188), set(pool)):   # the pilot's dilution ratio
            pool[g] = "tail"
    d.mkdir(parents=True, exist_ok=True)
    json.dump({"protocol": PROTOCOL, "pool": pool, "synth": bool(a.synth)}, open(d / "pool.json", "w"), ensure_ascii=False, indent=0)
    write_jsonl(d / "seeds.jsonl", seeds)
    print(f"init: {len(pool)} glyphs in pool, {len(seeds)} seeds -> {d}")

# ------------------------------------------------------------------ evidence
def load_all(d, upto=None):
    items, pres, parsed, sheets = {}, {}, [], {}
    for rid in rounds(d):
        rd = d / "rounds" / rid
        for it in read_jsonl(rd / "items.jsonl"):
            items.setdefault(it["iid"], it)
        for p in read_jsonl(rd / "presentations.jsonl"):
            pres[p["pid"]] = p
        for s in read_jsonl(rd / "sheets.jsonl"):
            sheets[s["sid"]] = s
        for f in sorted((rd / "raw").glob("*/ledger.jsonl")):
            mind = f.parent.name
            last = {}
            for row in read_jsonl(f):
                if row["result"].get("raw") and not row["result"].get("error"):
                    last[row["sid"]] = row
            for sid, row in last.items():
                pp = P.parse_sheet(row["result"]["raw"], sheets[sid])
                for pid, v in pp.items():
                    parsed.append({"mind": mind, "pid": pid, "round": rid, **v})
        if upto and rid == upto:
            break
    return items, pres, parsed, sheets

def proposals(parsed, pres):
    out = []
    for r in parsed:
        if r["status"] == "ok" and r.get("answer", {}) and isinstance(r["answer"], dict) and r["answer"].get("proposals"):
            p = pres[r["pid"]]
            ctx = [g for g in p["shown"] if g != "GAP"]
            for g in r["answer"]["proposals"]:
                if ok_glyph(g):
                    out.append({"mind": r["mind"], "kind": p["kind"], "ctx": ctx, "shown": p["shown"], "g": g})
    return out

# ------------------------------------------------------------------ plan
def cmd_plan(a):
    d = D(a); rid = a.round
    rd = d / "rounds" / rid
    if (rd / "sheets.jsonl").exists():
        sys.exit(f"{rid} already planned (truth is append-only; plan a new round id)")
    pool = json.load(open(d / "pool.json"))["pool"]
    seeds = read_jsonl(d / "seeds.jsonl")
    if not json.load(open(d / "pool.json")).get("synth"):
        # the dropspot: seeds added to data/seeds/ since the last plan enter now (append-only), with their glyphs
        have = {x["sid"] for x in seeds}
        new = [x for x in domain_seeds() if x["sid"] not in have]
        if new:
            for x in new:
                x["added_round"] = rid
                append_jsonl(d / "seeds.jsonl", x)
                for g in x["glyphs"]:
                    pool.setdefault(g, "seed")
            seeds += new
            print(f"{rid}: {len(new)} new seed(s) from data/seeds/")
    items, pres, parsed, sheets = load_all(d)
    # the basis is the latest round that HAS a fit: probe rounds (round.py probe) carry evidence but no fit of their own
    # (bug found 2026-10-04: r004 was planned against probe round r003p, i.e. as if nothing had been fit)
    prev = [r for r in rounds(d) if r != rid and (d / "rounds" / r / "fit.json").exists()]
    fit = json.load(open(d / "rounds" / prev[-1] / "fit.json")) if prev else None
    mind_names = core_minds(a, d)
    # proposals from next/between answers enter the pool
    props = proposals(parsed, pres)
    for x in props:
        pool.setdefault(x["g"], "frontier-proposal")
    json.dump({"protocol": PROTOCOL, "pool": pool, "synth": json.load(open(d / "pool.json")).get("synth")},
              open(d / "pool.json", "w"), ensure_ascii=False, indent=0)
    asked_rep = collections.defaultdict(set)
    for p in pres.values():
        asked_rep[p["iid"]].add(p["rep"])
    asked0 = {iid for iid, reps in asked_rep.items() if 0 in reps}
    obs = M.observations(parsed, pres)
    cur = M.from_snapshot(fit["best"], obs, sorted({r["mind"] for r in parsed})) if fit and fit["best"]["cands"] else None
    fam = family_of(d)
    # sequences: every one the answers grow (growth.py), most stable first; nothing filtered (Joseph, 2026-10-04).
    # The fit's candidates remain a source of guesses, asked in the link tier.
    pieces = G.piece_table(obs, parsed, pres, fam) if obs else []
    in_piece = set()
    for pc in pieces:
        in_piece.update(pc["glyphs"])
    bump = {}
    for sd in seeds:
        for g in sd["glyphs"]:
            bump[g] = max(bump.get(g, 1.0), sd.get("bump", Q.SEED_BUMP))
    cooc = _cooc(parsed, pres, props) if pieces else {}
    seed_next = Q.seed_continuations(seeds) if pieces else {}
    # ---- ONE priority order (Joseph's rule; squeue: "one priority order"). Two parts:
    #      (1) EXPLORE_SHARE: hot exploration + rotation follow-ups that confirm exploratory kernels;
    #      (2) the rest: established sequences, most stable first, each with its work in a fixed order, taken greedily.
    first = collections.defaultdict(list)
    for r in parsed:
        p = pres[r["pid"]]
        if p["kind"] == "triad" and p["rep"] == 0 and r["status"] == "ok":
            first[p["iid"]].append(r["answer"][0])
    follows = []                       # (item, rep, minds that ordered it at rep 0)
    for iid in sorted(first):
        outs = first[iid]; it = items[iid]
        n_ord = sum(o != "none" for o in outs)
        if n_ord >= 1:
            follows += [(it, rp, n_ord) for rp in (1, 2) if rp not in asked_rep[iid]]
        elif R("perp-recheck", {"iid": iid}).random() < Q.P_PERP_RECHECK and 1 not in asked_rep[iid]:
            follows.append((it, 1, 0))
    follow_by_glyph = collections.defaultdict(list)
    for f in follows:
        for g in f[0]["glyphs"]:
            follow_by_glyph[g].append(f)
    B = a.budget
    B_explore = round(Q.EXPLORE_SHARE * B) if pieces else B
    sel_items, new_pres, spent = {}, [], 0
    used_follow = set()
    def take_item(it, cat):
        nonlocal spent
        if it["iid"] in sel_items or it["iid"] in asked0:
            return False
        sel_items[it["iid"]] = dict(it, category=list(cat), round=rid)
        reps = [0, 1] if it["kind"] == "order" else [0]
        new_pres.extend(I.presentation(it, rp, rid) for rp in reps)
        spent += len(reps)
        return True
    def take_follow(f, cat):
        nonlocal spent
        it, rp, _ = f
        if (it["iid"], rp) in used_follow:
            return False
        used_follow.add((it["iid"], rp))
        sel_items.setdefault(it["iid"], dict(it, category=list(cat), round_created=it.get("round"), round=rid))
        new_pres.append(I.presentation(it, rp, rid)); spent += 1
        return True
    # (1) exploration: first confirm exploratory kernels (follow-ups of triads any mind ordered, most minds first),
    #     up to a third of the share; then hot items in their fated (seed-bumped) random order
    kern = sorted([f for f in follows if not all(g in in_piece for g in f[0]["glyphs"])],
                  key=lambda f: (-f[2], f[0]["iid"], f[1]))
    for f in kern:
        if spent >= B_explore / 3:
            break
        take_follow(f, ["triad", "kernel-followup"])
    # test what minds proposed BETWEEN two glyphs (far pairs and gaps): triad (left, proposal, right), up to a sixth
    bt = collections.Counter()
    for r_ in parsed:
        p_ = pres[r_["pid"]]
        if p_["kind"] != "between" or r_["status"] != "ok":
            continue
        gi = p_["shown"].index("GAP"); lft, rgt = p_["shown"][gi - 1], p_["shown"][gi + 1]
        for g_ in r_["answer"].get("proposals", []):
            if ok_glyph(g_) and g_ not in (lft, rgt):
                bt[(lft, g_, rgt)] += 1
    for (lft, g_, rgt), n_ in sorted(bt.items(), key=lambda t: (-t[1], t[0])):
        if spent >= B_explore / 2:
            break
        try:
            take_item(I.make_item("triad", [lft, g_, rgt], source={"kind": "explore", "how": "between-proposal", "proposers": n_}),
                      ["triad", "between-test"])
        except AssertionError:
            continue
    for it, _ in Q.explore_items(sorted(pool), bump, seeds, rid, n_tri=600, n_set=200, n_next=80, n_between=120):
        if spent >= B_explore:
            break
        if take_item(it, [it["kind"], "explore"]):
            for g in it["glyphs"]:
                pool.setdefault(g, "uniform-tail")      # fresh glyphs join the pool once asked
    n_explore = spent
    # (2) sequences in stability order, each with its full work list, greedily
    served, last_stab = 0, None
    if pieces:
        support_by_glyph = collections.defaultdict(list)
        for cid in (list(cur.cands) if cur else []):
            for it, _ in Q.support_items(cur, cid, rid):
                key = it["source"].get("link") or it["source"].get("tie") or ""
                for g in key:
                    support_by_glyph[g].append(it)
        for pc in pieces:
            if spent >= B:
                break
            ends = [Q.end_state(pc, side, parsed, pres, items) for side in ("right", "left")]
            got = 0
            for tier, w in Q.sequence_work(pc, ends, cooc, seed_next, support_by_glyph, follow_by_glyph, rid):
                if spent >= B:
                    break
                name = {1: "end", 2: "link", 3: "followup", 4: "end", 5: "square", 6: "branch"}[tier]
                if isinstance(w, tuple):
                    got += take_follow(w, ["triad", name])
                else:
                    got += take_item(dict(w, source=dict(w["source"], seq="".join(pc["glyphs"]), stability=round(pc["stability"], 4))),
                                     [w["kind"], name])
            if got:
                served += 1; last_stab = pc["stability"]
    # anything left (few sequences yet): more exploration
    if spent < B:
        for it, _ in Q.explore_items(sorted(pool), bump, seeds, rid + "-more", n_tri=600, n_set=100, n_next=40):
            if spent >= B:
                break
            take_item(it, [it["kind"], "explore"])
    sheets_out = []
    for k in I.KINDS:
        ps = [p for p in new_pres if p["kind"] == k]
        if ps:
            sheets_out += I.build_sheets(rid, sel_items, ps, k)
    second = second_minds(a, d)
    for s in sheets_out:
        s["minds"] = list(mind_names) + [m for m in second if R("second-mind", {"sid": s["sid"], "m": m}).random() < 0.2]
    rd.mkdir(parents=True, exist_ok=True)
    json.dump({"protocol": PROTOCOL, "pool": pool, "synth": json.load(open(d / "pool.json")).get("synth")},
              open(d / "pool.json", "w"), ensure_ascii=False, indent=0)
    if fit:   # provenance: the exact fit this round was drawn from (a later re-analysis may overwrite fit.json)
        json.dump(dict(fit, basis_of=rid, basis_from=prev[-1]), open(rd / "basis-fit.json", "w"), ensure_ascii=False)
    write_jsonl(rd / "items.jsonl", list(sel_items.values()))
    write_jsonl(rd / "presentations.jsonl", new_pres)
    write_jsonl(rd / "sheets.jsonl", sheets_out)
    cats_n = collections.Counter("/".join(it["category"]) for it in sel_items.values())
    json.dump({"round": rid, "scheme": "single-priority (Joseph's rule, 2026-10-04)", "explore_share": Q.EXPLORE_SHARE,
               "explore_presentations": n_explore, "established_sequences": len(pieces), "sequences_served": served,
               "lowest_stability_served": last_stab, "items_by_category": dict(cats_n),
               "presentations": len(new_pres), "sheets": len(sheets_out)}, open(rd / "plan.json", "w"), ensure_ascii=False, indent=1)
    print(f"{rid}: {len(new_pres)} presentations on {len(sheets_out)} sheets; exploration {n_explore}; "
          f"{served} of {len(pieces)} sequences served (lowest stability served {last_stab})")

def _cooc(parsed, pres, props):
    """glyph -> other glyphs it has been placed in a sequence with (non-none triad answers, order lines) or proposed
    next to, most frequent first."""
    cnt = collections.defaultdict(collections.Counter)
    for r in parsed:
        if r["status"] != "ok":
            continue
        p = pres[r["pid"]]; a_ = r["answer"]
        if p["kind"] == "triad" and a_[0] != "none":
            gs = [g for g in p["shown"]] if a_[0] != "two" else list(a_[1:])
        elif p["kind"] == "order" and isinstance(a_, dict) and a_.get("lines"):
            for line in a_["lines"]:
                gs = [g for st in line if st != "GAP" for g in st]
                for x in gs:
                    for y in gs:
                        if x != y:
                            cnt[x][y] += 1
            continue
        else:
            continue
        for x in gs:
            for y in gs:
                if x != y:
                    cnt[x][y] += 1
    for x in props:
        if x["ctx"]:
            cnt[x["ctx"][-1]][x["g"]] += 2
    return {g: [h for h, _ in c.most_common(20)] for g, c in cnt.items()}




# ------------------------------------------------------------------ run
def core_minds(a, d):
    if json.load(open(d / "pool.json")).get("synth"):
        import synth as S
        return sorted(S.minds_default())
    return load_minds()["roster"]["core"]

def second_minds(a, d):
    if json.load(open(d / "pool.json")).get("synth"):
        return []
    return load_minds()["roster"]["second"]

def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()

def cmd_run(a):
    d = D(a); rd = d / "rounds" / a.round
    sheets = read_jsonl(rd / "sheets.jsonl")
    synth = json.load(open(d / "pool.json")).get("synth")
    if synth:
        import synth as S
        truth = S.Truth(S.world_default(), S.minds_default())
    reg = load_minds()
    want = a.minds or sorted({m for s in sheets for m in s["minds"]})
    for m in want:
        my = [s for s in sheets if m in s["minds"]]
        led = rd / "raw" / m / "ledger.jsonl"
        done = {r["sid"] for r in read_jsonl(led) if r["result"].get("raw") and not r["result"].get("error")}
        todo = [s for s in my if s["sid"] not in done]
        if a.limit:
            todo = todo[: a.limit]
        print(f"{a.round}/{m}: {len(my)} sheets, {len(done)} done, {len(todo)} to run", flush=True)
        if synth:
            for s in todo:
                raw = truth.answer_sheet(m, s)
                append_jsonl(led, {"protocol": PROTOCOL, "round": a.round, "sid": s["sid"], "mind": m, "synthetic": True,
                                   "prompt_sha256": sha(s["prompt"]), "ts": dt.datetime.now(dt.timezone.utc).isoformat(),
                                   "result": {"raw": raw, "error": None}})
            continue
        sys.path.insert(0, str(EXP / "harness/core"))
        from judges import make_judge, ADAPTER_VERSION
        spec = reg["minds"][m]
        judge = make_judge(spec)
        lock = threading.Lock()
        def one(s):
            res = judge(I.SYSTEM, s["prompt"])
            row = {"protocol": PROTOCOL, "round": a.round, "sid": s["sid"], "mind": m, "judge": spec,
                   "adapter_version": ADAPTER_VERSION[spec["adapter"]], "system_sha256": sha(I.SYSTEM),
                   "prompt_sha256": sha(s["prompt"]), "prompt": s["prompt"],
                   "ts": dt.datetime.now(dt.timezone.utc).isoformat(), "result": res}
            if res.get("raw") and not res.get("error"):
                pp = P.parse_sheet(res["raw"], s)
                if not any(v["status"] == "ok" for v in pp.values()):
                    row["result"] = dict(res, error="no-entry-parsed")   # raw kept; re-asked on resume
            with lock:
                append_jsonl(led, row)
            return bool(row["result"].get("raw")) and not row["result"].get("error")
        workers = a.workers or (1 if spec["adapter"] in ("llamacpp", "agy") else 6)
        with cf.ThreadPoolExecutor(max_workers=workers) as ex:
            ok = sum(ex.map(one, todo))
        print(f"{a.round}/{m}: ok {ok}/{len(todo)}", flush=True)

# ------------------------------------------------------------------ analyze
def cmd_analyze(a):
    d = D(a); rid = a.round; rd = d / "rounds" / rid
    items, pres, parsed, sheets = load_all(d, upto=rid)
    mind_names = sorted({r["mind"] for r in parsed})
    obs = M.observations(parsed, pres)
    prev = [r for r in rounds(d) if r < rid and (d / "rounds" / r / "fit.json").exists()]
    warm = []
    if prev:
        warm = [c["steps"] for c in json.load(open(d / "rounds" / prev[-1] / "fit.json"))["best"]["cands"]]
    iters = a.iters or min(20000, 1500 + 3 * len(obs) // 10)
    # restart points (PLAN §4): even chains warm-start from the last round's fit; odd chains from the seeds whose
    # glyphs have been asked (>= 3 asked glyphs, restricted to those glyphs), so seeds can only start a search
    asked = {g for o in obs for g in o["tri"]}
    seed_starts = []
    for sd in read_jsonl(d / "seeds.jsonl"):
        g = [x for x in sd["glyphs"] if x in asked]
        if len(g) >= 3:
            seed_starts.append([[x] for x in g])
    chains = []
    for ch in range(a.chains):
        mod = M.Model(obs, mind_names, cands=warm if ch % 2 == 0 else seed_starts)
        mod.recompute_all()
        smp = M.anneal(mod, {"round": rid, "chain": ch}, iters=iters, sample_every=max(50, iters // 40), n_samples=4)
        chains.append((mod.objective(), mod.snapshot(), smp, ch % 2 == 0 and bool(warm)))
        print(f"  chain {ch}: objective {mod.objective():.1f}, {len(mod.cands)} candidates", flush=True)
    chains.sort(key=lambda t: -t[0])
    best = chains[0][1]
    samples = [s for _, _, smp, _ in chains for s in smp]
    fam = family_of(d)
    # support counts only COLD chains (started from seeds, not from the last fit) and their samples: warm chains
    # inherit the previous fit, so their agreement with it is not independent evidence (found 2026-10-04: an
    # untested ordering showed support 1.00 because warm chains kept it)
    cold = [(c[1], c[2]) for c in chains if not c[3]]
    support = _support(best, [b for b, _ in cold] + [s for _, smp in cold for s in smp])
    pr = collections.Counter((r["mind"], r["status"]) for r in parsed if r["round"] == rid)
    fit = {"round": rid, "n_obs": len(obs), "minds": mind_names, "best": best, "support": support,
           "alternatives": [c[1] for c in chains[1:]], "cold_chains": len(cold), "samples": samples, "next_T": max(0.2, 0.8 * (json.load(open(d / "rounds" / prev[-1] / "fit.json")).get("next_T", 1.0) if prev else 1.0)),
           "parse": {f"{m}|{s}": n for (m, s), n in pr.items()}}
    json.dump(fit, open(rd / "fit.json", "w"), ensure_ascii=False)
    (rd / "report.md").write_text(report(rid, fit, fam, items, pres, parsed))
    print((rd / "report.md").read_text()[:3000])

def family_of(d):
    if json.load(open(d / "pool.json")).get("synth"):
        import synth as S
        return {m: v[0] for m, v in S.minds_default().items()}
    return {m: v["family"] for m, v in load_minds()["minds"].items()}

def _match(c1, c2):
    a, b = set(g for st in c1["steps"] for g in st), set(g for st in c2["steps"] for g in st)
    return len(a & b) / max(1, len(a | b))

def _support(best, others):
    return [sum(1 for o in others if any(_match(c, x) >= 0.7 for x in o["cands"])) / max(1, len(others)) for c in best["cands"]]

def report(rid, fit, fam, items, pres, parsed):
    best = fit["best"]
    fams = sorted(set(fam.get(m, m) for m in fit["minds"]))
    L = [f"# Round {rid} — fit report", "",
         f"Observations (triple-level, cumulative): {fit['n_obs']}. Minds: {', '.join(fit['minds'])}.", "",
         "## Candidate sequences (best chain), by family-mean perception", "",
         "s3 = perception in triads, s4 = in sets of 4+, per family (mean over its minds). support = share of the cold-started chains (from seeds, not from the last fit) and their posterior samples holding a matching candidate.", "",
         "| # | sequence | n | support | " + " | ".join(f"{f} s3/s4" for f in fams) + " |",
         "|---|---|---|---|" + "---|" * len(fams)]
    rows = []
    for i, c in enumerate(best["cands"]):
        per = {}
        for f in fams:
            ms = [m for m in fit["minds"] if fam.get(m, m) == f]
            per[f] = (sum(c["s"][m]["s3"] for m in ms) / len(ms), sum(c["s"][m]["s4"] for m in ms) / len(ms))
        score = sum(max(v) for v in per.values()) / len(per)
        seq = " ".join("=".join(st) for st in c["steps"])
        rows.append((score, f"| {i} | `{seq}` | {sum(len(st) for st in c['steps'])} | {fit['support'][i]:.2f} | "
                     + " | ".join(f"{per[f][0]:.2f}/{per[f][1]:.2f}" for f in fams) + " |"))
    L += [r for _, r in sorted(rows, key=lambda t: -t[0])]
    L += ["", "## Minds: nuisance parameters", "", "| mind | eps | nn | nt | beta | tau |", "|---|---|---|---|---|---|"]
    for m, th in sorted(best["theta"].items()):
        L.append(f"| {m} | {th['eps']} | {th['nn']} | {th['nt']} | {th['beta']} | {th['tau']} |")
    L += ["", "## Minds: slot bias read directly from the Latin rotations (no model)", "",
          "Over triads whose three rotations were all answered with an order: share of answers naming the glyph shown in the middle (1/3 = no slot preference), and share of triads given the same middle in all three rotations.", "",
          "| mind | triads | middle = shown middle | same middle 3/3 |", "|---|---|---|---|"]
    rot = collections.defaultdict(lambda: collections.defaultdict(dict))
    for r in parsed:
        p = pres[r["pid"]]
        if p["kind"] == "triad" and r["status"] == "ok":
            rot[r["mind"]][p["iid"]][p["rep"]] = (r["answer"], p["shown"])
    for m in sorted(rot):
        full = [d for d in rot[m].values() if all(k in d for k in (0, 1, 2)) and all(d[k][0][0] == "mid" for k in (0, 1, 2))]
        if not full:
            continue
        hit = sum(d[k][0][1] == d[k][1][1] for d in full for k in (0, 1, 2)) / (3 * len(full))
        same = sum(len({d[k][0][1] for k in (0, 1, 2)}) == 1 for d in full) / len(full)
        L.append(f"| {m} | {len(full)} | {hit:.2f} | {same:.2f} |")
    L += ["", "## Parse status this round", ""]
    L += [f"- {k}: {v}" for k, v in sorted(fit["parse"].items())]
    return "\n".join(L) + "\n"


# ------------------------------------------------------------------ probe
def cmd_probe(a):
    """A targeted probe round (Joseph, 2026-10-04: "get additional data points so we have a good spread"): for each
    named seed, EVERY triad of its glyphs (all three Latin rotations) and order items over the whole set and over
    fated subsets (2 shuffles each), sent to every API mind on the roster, not to a sample. Same instruments, same
    randomization, same parser; category ("<kind>", "probe") so the analysis and the record can tell it apart."""
    import itertools
    d = D(a); rid = a.round; rd = d / "rounds" / rid
    if (rd / "sheets.jsonl").exists():
        sys.exit(f"{rid} already planned")
    seeds = {x["sid"]: x for x in read_jsonl(d / "seeds.jsonl")}
    for x in domain_seeds():
        seeds.setdefault(x["sid"], x)
    sel, pres = {}, []
    for sid in a.seeds:
        g = [x for x in dict.fromkeys(seeds[sid]["glyphs"]) if ok_glyph(x)]
        src = {"kind": "probe", "ref": sid}
        for t in itertools.combinations(g, 3):
            it = dict(I.make_item("triad", list(t), source=src), category=["triad", "probe"], round=rid)
            if it["iid"] not in sel:
                sel[it["iid"]] = it; pres += [I.presentation(it, r, rid) for r in (0, 1, 2)]
        subsets = [g] if 4 <= len(g) <= 8 else []
        r = R("probe-subsets", {"round": rid, "sid": sid})
        for _ in range(a.subsets):
            if len(g) >= 5:
                k = r.randint(4, min(7, len(g) - 1)); subsets.append(r.sample(g, k))
        for sub in subsets:
            it = dict(I.make_item("order", sub, source=src), category=["order", "probe"], round=rid)
            if it["iid"] not in sel:
                sel[it["iid"]] = it; pres += [I.presentation(it, rep, rid) for rep in range(a.shuffles)]
    sheets_out = []
    for k in I.KINDS:
        ps = [p for p in pres if p["kind"] == k]
        if ps:
            sheets_out += I.build_sheets(rid, sel, ps, k)
    reg = load_minds()
    api = [m for m in reg["roster"]["core"] + reg["roster"]["second"] if reg["minds"][m]["adapter"] != "llamacpp"]
    for s in sheets_out:
        s["minds"] = api
    rd.mkdir(parents=True, exist_ok=True)
    write_jsonl(rd / "items.jsonl", list(sel.values()))
    write_jsonl(rd / "presentations.jsonl", pres)
    write_jsonl(rd / "sheets.jsonl", sheets_out)
    json.dump({"round": rid, "probe": a.seeds, "items": len(sel), "presentations": len(pres), "sheets": len(sheets_out),
               "minds": api, "why": a.why}, open(rd / "plan.json", "w"), ensure_ascii=False, indent=1)
    print(f"{rid}: probe of {len(a.seeds)} seed(s): {len(sel)} items, {len(pres)} presentations, {len(sheets_out)} sheets, to {', '.join(api)}")

# ------------------------------------------------------------------ loop
def cmd_loop(a):
    d = D(a)
    if not (d / "pool.json").exists():
        cmd_init(argparse.Namespace(**{**vars(a), "synth": True}))
    for n in range(a.n):
        rid = f"r{len(rounds(d)):03d}"
        cmd_plan(argparse.Namespace(**{**vars(a), "round": rid}))
        cmd_run(argparse.Namespace(**{**vars(a), "round": rid, "minds": None, "limit": 0}))
        cmd_analyze(argparse.Namespace(**{**vars(a), "round": rid}))

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--data")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("init"); p.add_argument("--synth", action="store_true"); p.set_defaults(f=cmd_init)
    p = sub.add_parser("plan"); p.add_argument("round"); p.add_argument("--budget", type=int, default=300); p.set_defaults(f=cmd_plan)
    p = sub.add_parser("run"); p.add_argument("round"); p.add_argument("--minds", nargs="*"); p.add_argument("--synth", action="store_true")
    p.add_argument("--workers", type=int, default=0); p.add_argument("--limit", type=int, default=0); p.set_defaults(f=cmd_run)
    p = sub.add_parser("analyze"); p.add_argument("round"); p.add_argument("--chains", type=int, default=4)
    p.add_argument("--iters", type=int, default=0); p.set_defaults(f=cmd_analyze)
    p = sub.add_parser("probe"); p.add_argument("round"); p.add_argument("seeds", nargs="+")
    p.add_argument("--subsets", type=int, default=8); p.add_argument("--shuffles", type=int, default=2)
    p.add_argument("--why", default=""); p.set_defaults(f=cmd_probe)
    p = sub.add_parser("loop"); p.add_argument("n", type=int); p.add_argument("--synth", action="store_true")
    p.add_argument("--budget", type=int, default=300); p.add_argument("--chains", type=int, default=4)
    p.add_argument("--iters", type=int, default=0); p.add_argument("--workers", type=int, default=0); p.set_defaults(f=cmd_loop)
    a = ap.parse_args(); a.f(a)

if __name__ == "__main__":
    main()
