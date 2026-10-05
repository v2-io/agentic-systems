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
    items, pres, parsed, sheets = load_all(d)
    prev = rounds(d)
    fit = json.load(open(d / "rounds" / prev[-1] / "fit.json")) if prev and (d / "rounds" / prev[-1] / "fit.json").exists() else None
    mind_names = core_minds(a, d)
    samples = [M.from_snapshot(s, [], mind_names) for s in (fit or {}).get("samples", [])][:12]
    T = (fit or {}).get("next_T", 1.0)
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
    # ---- follow-ups: Latin rotation reps 1,2 when any mind did not answer ⟂ at rep 0; a ⟂ recheck share
    first = collections.defaultdict(list)
    for r in parsed:
        p = pres[r["pid"]]
        if p["kind"] == "triad" and p["rep"] == 0 and r["status"] == "ok":
            first[p["iid"]].append(r["answer"][0])
    follow = []
    for iid, outs in first.items():
        it = items[iid]
        if any(o != "none" for o in outs):
            follow += [(it, rp) for rp in (1, 2) if rp not in asked_rep[iid]]
        elif R("perp-recheck", {"iid": iid}).random() < Q.P_PERP_RECHECK and 1 not in asked_rep[iid]:
            follow.append((it, 1))
    # ---- candidate items by category
    cats = collections.defaultdict(list)
    def score(it, cat, bump=1.0):
        inf = Q.info(it, samples, mind_names)
        nov = _novelty(it, parsed, pres)
        return (bump if cat[1] == "seed" else 1.0) * (inf + 0.1 * nov) if samples else math.log(bump) + 0.1 * nov
    rs = R("seed-subset", {"round": rid})
    sub = list(seeds); rs.shuffle(sub)
    for s in sub[:400]:
        for it in Q.seed_items(s):
            cat = (it["kind"], "seed")
            cats[cat].append((it, score(it, cat, s.get("bump", Q.SEED_BUMP))))
    pl = sorted(pool)
    for it in Q.tail_items(pl, rid, 200, 60):
        cats[(it["kind"], "tail")].append((it, 0.0))
    if fit and fit["best"]["cands"]:
        snap = fit["best"]
        nb = _neighbours(snap, parsed, pres, props)
        for ci in range(len(snap["cands"])):
            for it in Q.cand_items(snap, nb.get(ci, []), rid, ci):
                cat = (it["kind"], "cand")
                cats[cat].append((it, score(it, cat)))
        for x in props[-400:]:
            if len(x["ctx"]) >= 2 and x["g"] not in x["ctx"]:
                try:
                    it = I.make_item("triad", [x["ctx"][-2], x["ctx"][-1], x["g"]] if x["kind"] == "next" else
                                     [x["ctx"][0], x["g"], x["ctx"][-1]], source={"kind": "cand", "ref": "proposal", "mind": x["mind"]})
                except AssertionError:
                    continue
                cats[("triad", "cand")].append((it, score(it, ("triad", "cand")) + 0.5))
    base = Q.LATE if (fit and fit["best"]["cands"]) else Q.EARLY
    avail = {c: _top_mean([p for _, p in cats.get(c, [])], round(base[c] * a.budget)) for c in base}
    quotas = Q.reweight(base, avail) if samples else dict(base)
    # ---- budget in presentations: follow-ups first
    cost = {"triad": 1, "order": 2, "next": 1, "between": 1}
    fu_cost = len(follow)
    follow = follow[: int(0.5 * a.budget)]
    n_new = max(10, a.budget - len(follow))
    mean_cost = sum(quotas[c] * cost[c[0]] for c in quotas)
    N = int(n_new / mean_cost)
    chosen = Q.draw(cats, quotas, N, T, rid, asked0)
    sel_items, new_pres = {}, []
    for it, cat, pri in chosen:
        it = dict(it, category=list(cat), priority=pri, round=rid)
        sel_items[it["iid"]] = it
        reps = [0, 1] if it["kind"] == "order" else [0]
        new_pres += [I.presentation(it, rp, rid) for rp in reps]
    for it, rp in follow:
        sel_items.setdefault(it["iid"], dict(it, category=["triad", "followup"], round_created=it.get("round"), round=rid))
        new_pres.append(I.presentation(it, rp, rid))
    sheets_out = []
    for k in I.KINDS:
        ps = [p for p in new_pres if p["kind"] == k]
        if ps:
            sheets_out += I.build_sheets(rid, sel_items, ps, k)
    second = second_minds(a, d)
    for s in sheets_out:
        s["minds"] = list(mind_names) + [m for m in second if R("second-mind", {"sid": s["sid"], "m": m}).random() < 0.2]
    rd.mkdir(parents=True, exist_ok=True)
    write_jsonl(rd / "queue.jsonl", [{"iid": it["iid"], "cat": list(c), "priority": p, "kind": it["kind"], "glyphs": it["glyphs"],
                                      "source": it["source"]} for c, lst in sorted(cats.items()) for it, p in lst])
    write_jsonl(rd / "items.jsonl", list(sel_items.values()))
    write_jsonl(rd / "presentations.jsonl", new_pres)
    write_jsonl(rd / "sheets.jsonl", sheets_out)
    json.dump({"round": rid, "quotas": {"|".join(c): v for c, v in quotas.items()}, "available_info": {"|".join(c): v for c, v in avail.items()},
               "T": T, "follow_ups": len(follow), "follow_ups_wanted": fu_cost, "new_items": len(chosen),
               "presentations": len(new_pres), "sheets": len(sheets_out)}, open(rd / "plan.json", "w"), indent=1)
    print(f"{rid}: {len(chosen)} new items + {len(follow)} follow-up presentations -> {len(new_pres)} presentations, "
          f"{len(sheets_out)} sheets (T={T:.2f})")

def _top_mean(ps, k):
    ps = sorted(ps, reverse=True)[:max(1, k)]
    return sum(ps) / len(ps) if ps else 0.0

def _novelty(it, parsed, pres, _cache={}):
    key = id(parsed)
    if key not in _cache:
        cnt = collections.Counter()
        for r in parsed:
            for g in pres[r["pid"]]["shown"]:
                cnt[g] += 1
        _cache.clear(); _cache[key] = cnt
    cnt = _cache[key]
    return sum(1 / (1 + cnt[g] / 15) for g in it["glyphs"]) / len(it["glyphs"])

def _neighbours(snap, parsed, pres, props):
    """per candidate: glyphs that co-occur with its members in non-none answers, or were proposed next to them."""
    mem = {ci: set(g for st in c["steps"] for g in st) for ci, c in enumerate(snap["cands"])}
    g2c = collections.defaultdict(set)
    for ci, s in mem.items():
        for g in s:
            g2c[g].add(ci)
    cnt = collections.defaultdict(collections.Counter)
    for r in parsed:
        if r["status"] != "ok":
            continue
        p = pres[r["pid"]]
        a = r["answer"]
        if p["kind"] == "triad" and a[0] != "none":
            gs = [g for g in p["shown"]]
        elif p["kind"] == "order" and isinstance(a, dict) and a.get("lines"):
            gs = [g for line in a["lines"] for st in line if st != "GAP" for g in st]
        else:
            continue
        for g in gs:
            for ci in g2c.get(g, ()):
                for h in gs:
                    if h not in mem[ci]:
                        cnt[ci][h] += 1
    for x in props:
        for g in x["ctx"]:
            for ci in g2c.get(g, ()):
                if x["g"] not in mem[ci]:
                    cnt[ci][x["g"]] += 2
    return {ci: [g for g, _ in c.most_common(12)] for ci, c in cnt.items()}

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
    prev = [r for r in rounds(d) if r < rid]
    warm = []
    if prev and (d / "rounds" / prev[-1] / "fit.json").exists():
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
        chains.append((mod.objective(), mod.snapshot(), smp))
        print(f"  chain {ch}: objective {mod.objective():.1f}, {len(mod.cands)} candidates", flush=True)
    chains.sort(key=lambda t: -t[0])
    best = chains[0][1]
    samples = [s for _, _, smp in chains for s in smp]
    fam = family_of(d)
    support = _support(best, [c[1] for c in chains] + samples)
    pr = collections.Counter((r["mind"], r["status"]) for r in parsed if r["round"] == rid)
    fit = {"round": rid, "n_obs": len(obs), "minds": mind_names, "best": best, "support": support,
           "alternatives": [c[1] for c in chains[1:]], "samples": samples, "next_T": max(0.2, 0.8 * json.load(open(rd / "plan.json")).get("T", 1.0)),
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
         "s3 = perception in triads, s4 = in sets of 4+, per family (mean over its minds). support = share of chains and posterior samples holding a matching candidate.", "",
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
    p = sub.add_parser("loop"); p.add_argument("n", type=int); p.add_argument("--synth", action="store_true")
    p.add_argument("--budget", type=int, default=300); p.add_argument("--chains", type=int, default=4)
    p.add_argument("--iters", type=int, default=0); p.add_argument("--workers", type=int, default=0); p.set_defaults(f=cmd_loop)
    a = ap.parse_args(); a.f(a)

if __name__ == "__main__":
    main()
