#!/usr/bin/env python3
"""The catalog (CATALOG.md, concern 6): build version 0.

One stated model over every answer, stored in Postgres 18 with the answer IDs behind every number. This build
implements part of CATALOG v5 and says which part:

  built   R (whole-run recognition against shuffled controls, per rater, Abbott-corrected, families combined by their
          discrimination on non-contiguous sets); certainty as a Bayes factor; the chart route's contested positions
          (steps and triples, CATALOG §7a) with D and triad preferences, read asymmetrically (§7b); route states (§7c);
          the default view (§11); lookalike substitution as a run-level quantity.
  not yet O (Plackett-Luce over order lines), L and G as parts of a record, B, seed raters, link states (§8), maximal
          runs from links, order lines as position evidence, the name route (reported "unmeasured" until the
          name-only question is validated, §7a), posterior predictive checks.

The seal (audits/SEAL-canary-choose-2026-10-06.md): until the seal file records the commit the model was frozen at,
every `choose` and `names` answer touching a canary glyph is dropped before anything is computed, so no build can
show them. The count dropped is in the manifest.

Records: every run asked whole as a real cohere question (both orientations are one record), the ordered seeds, and
the triad era's grown rows. Parameters marked "chosen without evidence" are listed in PARAMS and go into the
manifest; the freeze (CATALOG §13) commits them.

Usage: python3 catalog/build.py [--db empirica_glyph_sequence] [--no-db]   (writes data/catalog/<build>/ either way)
"""
import argparse, collections, csv, datetime as dt, hashlib, json, math, pathlib, platform, subprocess, sys, unicodedata as U

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tree")); sys.path.insert(0, str(ROOT / "probe")); sys.path.insert(0, str(ROOT / "priority"))
import run as RUN                                   # noqa: E402  answers(), seeds()
import tree as TR                                   # noqa: E402
import plan as PL                                   # noqa: E402  block()

MODEL = "catalog-v5-build0"
SEAL_FILE = ROOT / "audits" / "SEAL-canary-choose-2026-10-06.md"
CANARY = set("▁▂▃▄▅▆▇█🮆🮅🮄▀🮃🮂▔▉")
PARAMS = {                                           # every one chosen without evidence (CATALOG §13 freezes them)
    "BF_CERTAIN": 10.0,           # a Bayes factor at or above this is "with certainty", for every part
    "K_MULTIPLICITY": 1.0,        # a route's positive needs BF >= BF_CERTAIN * K * (contested positions asked), §7c
    "EVIDENCE_MIN": 1,            # answers naming or recognising a link before it is evidence (felt alternatives)
    "GRID": 400,                  # points on [0, 1] for the Bayes-factor integrals
    "SUFFIX_MIN": 2,              # shortest context suffix at which an alternative counts as felt
}

# ------------------------------------------------------------------ helpers
def sha(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()

def frozen_commit():
    """the commit the model was frozen at, from the seal file, or None"""
    for line in SEAL_FILE.read_text().splitlines():
        if line.startswith("**Model frozen at commit:**"):
            v = line.split(":**", 1)[1].strip()
            return None if (not v or v.startswith("*(")) else v
    return None

def sealed(r):
    if r.get("kind") not in ("choose", "names"):
        return False
    gs = set(r.get("context") or []) | set(r.get("candidates") or []) | set(r.get("shown") or [])
    return bool(gs & CANARY)

def chart_class(g):
    d = [ord(b) - ord(a) for a, b in zip(g, g[1:])]
    if all(x == 1 for x in d) or all(x == -1 for x in d):
        return "contiguous"
    if all(x > 0 for x in d) or all(x < 0 for x in d):
        return "monotone"
    return "other"

def set_class(gs):
    """the control class of a glyph SET: contiguous if its code points are consecutive. A shuffled control is a
    property of the set, so its false-positive rate is indexed by the set, not by any one order of it."""
    o = sorted(ord(x) for x in gs)
    return "contiguous" if all(b - a == 1 for a, b in zip(o, o[1:])) else "other"

def canonical(g):
    g = list(g)
    return tuple(min(g, g[::-1], key=lambda s: [ord(x) for x in s]))

def logsumexp(xs):
    m = max(xs)
    return m + math.log(sum(math.exp(x - m) for x in xs))

def bf_excess(obs, grid):
    """Bayes factor for beta > 0 against beta = 0 in P(yes) = c + (1 - c) * beta, beta common to the raters, uniform
    prior on [0, 1]. obs: [(yes, no, c)]."""
    def ll(beta):
        s = 0.0
        for y, n_, c in obs:
            p = min(max(c + (1 - c) * beta, 1e-12), 1 - 1e-12)
            s += y * math.log(p) + n_ * math.log(1 - p)
        return s
    pts = [(i + 0.5) / grid for i in range(grid)]
    return math.exp(logsumexp([ll(b) for b in pts]) - math.log(grid) - ll(0.0))

def bf_preference(k, n, b):
    """Bayes factor for p != b (uniform prior on p) against p = b, from k of n: 1 / ((n + 1) C(n, k) b^k (1 - b)^(n - k))"""
    if n == 0:
        return 1.0
    lc = math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
    return math.exp(-(math.log(n + 1) + lc + k * math.log(b) + (n - k) * math.log(1 - b)))

def delta(p, b):
    return (p - b) / (1 - b) if p >= b else (p - b) / b

# ------------------------------------------------------------------ load
def load():
    recs = RUN.answers()
    void = set(json.load(open(ROOT / "data" / "rounds" / "VOID.json"))["rounds"])
    frozen = frozen_commit()
    keep, dropped_seal = [], 0
    for r in recs:
        if not frozen and sealed(r):
            dropped_seal += 1; continue
        keep.append(r)
    return keep, {"void_rounds": sorted(void), "frozen_commit": frozen, "sealed_dropped": dropped_seal}

def rater(r):
    t = r.get("tags") or {}
    return f'{r["mind"]}|{t.get("variant") or "plain"}|{r.get("era")}'

# ------------------------------------------------------------------ R: whole-run recognition
def r_part(recs):
    """per real run: per rater (yes, n) and the answer IDs; per rater and set class, the shuffled control rate"""
    runs = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0]))
    aids = collections.defaultdict(list)
    ctl = collections.defaultdict(lambda: [0, 0])                     # (rater, set class) -> [yes, n]
    fam_of = {}
    for r in recs:
        if r["kind"] != "cohere" or r.get("outcome") not in ("yes", "no", "cant-tell"):
            continue
        rt = rater(r); fam_of[rt] = r["family"]
        c = (r.get("tags") or {}).get("control")
        y = 1 if r["outcome"] == "yes" else 0
        if c == "shuffled":
            k = (rt, set_class(r["context"])); ctl[k][0] += y; ctl[k][1] += 1
        elif not c:
            g = canonical(r["context"])
            runs[g][rt][0] += y; runs[g][rt][1] += 1; aids[g].append(r["aid"])
    return runs, aids, ctl, fam_of

def rater_c(ctl, rt, cls):
    y, n = ctl.get((rt, cls), (0, 0))
    if n == 0:                                                         # the rater's controls of the other class
        y = sum(v[0] for (r_, _), v in ctl.items() if r_ == rt); n = sum(v[1] for (r_, _), v in ctl.items() if r_ == rt)
    return (y, n) if n else None

def family_weights(runs, ctl, fam_of):
    """CATALOG §9: each family's discrimination on non-contiguous sets, where the chart can't help: real-run yes rate on
    "other"-class runs minus its shuffled rate on "other" sets"""
    ry = collections.defaultdict(lambda: [0, 0]); cy = collections.defaultdict(lambda: [0, 0])
    for g, by in runs.items():
        if chart_class(g) != "other":
            continue
        for rt, (y, n) in by.items():
            ry[fam_of[rt]][0] += y; ry[fam_of[rt]][1] += n
    for (rt, cls), (y, n) in ctl.items():
        if cls == "other":
            cy[fam_of[rt]][0] += y; cy[fam_of[rt]][1] += n
    w = {}
    for f in ry:
        if ry[f][1] and cy[f][1]:
            w[f] = max(ry[f][0] / ry[f][1] - cy[f][0] / cy[f][1], 0.0)
    return w

def r_record(g, by, ctl, fam_of, weights, grid):
    cls = set_class(g)
    fam = collections.defaultdict(lambda: [0.0, 0.0])                 # precision-weighted Abbott per family
    obs = []
    per_fam_counts = collections.defaultdict(lambda: [0, 0])
    for rt, (y, n) in sorted(by.items()):
        cc = rater_c(ctl, rt, cls)
        if not cc or not n:
            continue
        (m, v), (mc, vc) = TR.beta_mv(y, n), TR.beta_mv(*cc)
        a = (m - mc) / (1 - mc)
        va = (v + vc * ((1 - m) / (1 - mc)) ** 2) / (1 - mc) ** 2
        f = fam_of[rt]
        fam[f][0] += a / va; fam[f][1] += 1 / va
        obs.append((y, n - y, mc))
        per_fam_counts[f][0] += y; per_fam_counts[f][1] += n
    fams = {f: (s / p, (1 / p) ** 0.5) for f, (s, p) in fam.items() if p}
    num = den = var = 0.0
    for f, (a, sd) in sorted(fams.items()):
        w = weights.get(f, 0.0)
        num += w * a; den += w; var += (w * sd) ** 2
    comb = (num / den, var ** 0.5 / den) if den else (None, None)
    bf = bf_excess(obs, grid) if obs else None
    return {"families": {f: {"strength": round(a, 4), "sd": round(sd, 4), "yes": per_fam_counts[f][0], "n": per_fam_counts[f][1]}
                         for f, (a, sd) in fams.items()},
            "strength": comb[0], "sd": comb[1], "bf": bf}

# ------------------------------------------------------------------ chart positions (CATALOG §7a-§7c)
def chart_positions(g):
    """-> [{kind, idx, glyphs, run_choice, alternative, state}] for one orientation of a run"""
    out = []
    for i in range(1, len(g) - 1):                                     # step g[i] -> g[i+1] after g[i-1] -> g[i]
        p, a, b = g[i - 1], g[i], g[i + 1]
        c = PL.chart_neighbour(p, a)
        if c == b:
            st = "congruent"
        elif c is None or c in g:
            st = "no candidate"
        elif PL.contested(c, a):
            st = "contested"
        else:
            st = "uncontested"
        out.append({"kind": "step", "idx": i, "context": list(g[:i + 1]), "run_choice": b, "alternative": c, "state": st})
    for i in range(len(g) - 2):
        t = g[i:i + 3]
        med = sorted(t, key=ord)[1]
        if t[1] == med:
            st = "congruent"
        else:
            bl = {x: PL.block(x) for x in t}
            lo, hi = sorted(t, key=ord)[0], sorted(t, key=ord)[2]
            chart_pairs = [(lo, med), (med, hi)]                       # adjacent in code-point order
            run_adj = {frozenset((t[0], t[1])), frozenset((t[1], t[2]))}
            split = [pr for pr in chart_pairs if bl[pr[0]] == bl[pr[1]] and frozenset(pr) not in run_adj]
            st = "contested" if split else "uncontested"
        out.append({"kind": "triple", "idx": i, "context": list(t), "run_choice": t[1], "alternative": med, "state": st})
    return out

class Index:
    """the answers a position needs, by structure (never by `source`)"""
    def __init__(self, recs):
        self.choose = collections.defaultdict(list)       # (ctx, frozenset pair) -> [(aid, family, choice)]
        self.choose_ctl = collections.defaultdict(list)   # frozenset pair -> [(aid, family, choice)]
        self.triad = collections.defaultdict(list)        # sorted triple -> [(aid, family, middle)]
        self.inhibit = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0]))  # (ctx, x) -> fam -> [yes, n]
        self.near = collections.defaultdict(lambda: [0, 0])                                       # fam -> [yes, n]
        self.named = collections.defaultdict(set)         # ctx -> glyphs written first or picked there
        self.lookalike = collections.defaultdict(lambda: {"lookalike": [0, 0, []], "lookalike-ctl": [0, 0, []]})
        for r in recs:
            k, o, t = r["kind"], r.get("outcome"), r.get("tags") or {}
            if k == "choose" and o == "chose":
                pair = frozenset(r["candidates"])
                if t.get("control") == "neutral":
                    self.choose_ctl[pair].append((r["aid"], r["family"], r["choice"]))
                else:
                    self.choose[(tuple(r["context"]), pair)].append((r["aid"], r["family"], r["choice"]))
            elif k == "triad" and o == "mid":
                self.triad[tuple(sorted(r.get("shown") or r["context"]))].append((r["aid"], r["family"], r["answer"][1]))
            elif k == "inhibit" and o in ("yes", "no", "cant-tell"):
                y = 1 if o == "yes" else 0
                if t.get("control") == "near":
                    self.near[r["family"]][0] += y; self.near[r["family"]][1] += 1
                elif not t.get("control"):
                    c = self.inhibit[(tuple(r["context"]), r["candidate"])][r["family"]]; c[0] += y; c[1] += 1
            elif k in ("continue", "next", "pick") and o == "continuation" and r.get("continuation"):
                if not t.get("null"):
                    self.named[tuple(r["context"])].add(r["continuation"][0])
            elif k == "cohere" and t.get("control") in ("lookalike", "lookalike-ctl") and o in ("yes", "no", "cant-tell"):
                e = self.lookalike[t.get("of")][t["control"]]
                e[0] += 1 if o == "yes" else 0; e[1] += 1; e[2].append(r["aid"])

    def felt(self, ctx, x):
        """CATALOG §7b: x has L beyond its near control, or G evidence, at ctx or a suffix of at least SUFFIX_MIN glyphs"""
        for j in range(len(ctx), PARAMS["SUFFIX_MIN"] - 1, -1):
            c = tuple(ctx[-j:])
            if x in self.named.get(c, ()):
                return True
            fam = self.inhibit.get((c, x))
            if fam:
                diff, sd, fams = TR.estimate_vs({f: tuple(v) for f, v in fam.items()}, {f: tuple(self.near[f]) for f in fam})
                if diff is not None and diff - 1.2816 * sd > 0:
                    return True
        return False

def position_evidence(pos, ix):
    """pool the answers at a contested position -> estimate and interpretation (CATALOG §7b)"""
    b, alt = pos["run_choice"], pos["alternative"]
    if pos["kind"] == "step":
        pair = frozenset((b, alt))
        ans = []
        ctx = pos["context"]
        for j in range(min(8, len(ctx)), PARAMS["SUFFIX_MIN"] - 1, -1):     # the shown context and its suffixes
            ans += ix.choose.get((tuple(ctx[-j:]), pair), [])
        k = sum(1 for _, _, ch in ans if ch == b); n = len(ans)
        ctl = ix.choose_ctl.get(pair, [])
        if ctl:
            kc = sum(1 for _, _, ch in ctl if ch == b)
            base = (kc + 0.5) / (len(ctl) + 1)                                # Jeffreys mean of the control's share
            controlled = True
        else:
            base, controlled = 0.5, False
        instrument, aids = "D", [a for a, _, _ in ans] + [a for a, _, _ in ctl]
        felt_ctx = ctx
    else:
        ans = [x for x in ix.triad.get(tuple(sorted(pos["context"])), []) if x[2] in (b, alt)]
        k = sum(1 for _, _, m in ans if m == b); n = len(ans)
        base, controlled, instrument, aids = 0.5, False, "triad", [a for a, _, _ in ans]
        felt_ctx = None
    if n == 0:
        return dict(instrument=instrument, n=0, k=0, p=None, baseline=base, delta=None, bf=None, interp="unasked",
                    controlled=controlled, felt=None, aids=aids)
    p = k / n
    bf = bf_preference(k, n, base)
    certain = bf >= PARAMS["BF_CERTAIN"]
    felt = ix.felt(felt_ctx, alt) if felt_ctx is not None else None
    if not certain:
        interp = "inconclusive"
    elif p > base:
        interp = "positive"
    elif felt is False:
        interp = "negative"
    else:
        interp = "branch"            # the alternative is felt there (or, for triads, can't be shown not felt): chart or branch
    return dict(instrument=instrument, n=n, k=k, p=round(p, 4), baseline=round(base, 4), delta=round(delta(p, base), 4),
                bf=bf, interp=interp, controlled=controlled, felt=felt, aids=aids)

def route_state(positions):
    """CATALOG §7c, over both orientations' contested positions"""
    con = [p for p in positions if p["state"] == "contested"]
    if not con:
        return "undiscriminable"
    asked = [p for p in con if p["ev"]["n"]]
    m = max(len(asked), 1)
    pos = [p for p in asked if p["ev"]["interp"] == "positive" and p["ev"]["bf"] >= PARAMS["BF_CERTAIN"] * PARAMS["K_MULTIPLICITY"] * m]
    neg = [p for p in asked if p["ev"]["interp"] == "negative"]
    br = [p for p in asked if p["ev"]["interp"] == "branch"]
    if pos and neg:
        return "mixed"
    if pos:
        return "positive"
    if neg:
        return "negative"
    if br:
        return "chart or branch"
    return "undecided"

def view_group(recognised, chart, name):
    if not recognised:
        return None
    s = {chart, name}
    if chart == "positive" and name == "positive":
        return "1 intuitive"
    if (chart, name) in (("positive", "undiscriminable"), ("undiscriminable", "positive")):
        return "2 independent where measurable"
    if s & {"negative", "mixed"}:
        return "3 leaning"
    if "chart or branch" in s:
        return "4 chart or branch"
    if chart == "undiscriminable" and name == "undiscriminable":
        return "5 undiscriminable"
    return "6 undecided"

# ------------------------------------------------------------------ build
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="empirica_glyph_sequence")
    ap.add_argument("--no-db", action="store_true")
    a = ap.parse_args()
    t0 = dt.datetime.now()
    build = f"b{t0:%Y%m%d_%H%M%S}"
    out = ROOT / "data" / "catalog" / build
    out.mkdir(parents=True, exist_ok=True)
    recs, meta = load()

    # manifest
    files = sorted((ROOT / "data" / "answers").glob("*.jsonl"))
    manifest = {"model": MODEL, "build": build, "started": t0.isoformat(timespec="seconds"), **meta, "params": PARAMS,
                "python": platform.python_version(), "unicode": U.unidata_version,
                "answer_files": {f.name: sha(f) for f in files},
                "unicode_files": {f.name: sha(f) for f in sorted((ROOT / "data" / "unicode").glob("*.txt"))},
                "seed_files": {f.name: sha(f) for f in sorted((ROOT / "data" / "seeds").glob("*.jsonl"))},
                "growth_files": {f.name: sha(f) for f in sorted((ROOT / "data" / "triad-era" / "growth").glob("*.json"))},
                "code": {p: sha(ROOT / p) for p in ("catalog/build.py", "priority/plan.py", "tree/tree.py", "run.py")},
                "git_head": subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()}

    # records: runs asked whole, ordered seeds, the triad era's grown rows
    runs, raids, ctl, fam_of = r_part(recs)
    weights = family_weights(runs, ctl, fam_of)
    manifest["family_weights"] = weights
    sources = collections.defaultdict(set)
    for g in runs:
        sources[g].add("asked whole")
    for g, sid in PL.seed_list(RUN.seeds(), PL.ORDERED_SEEDS, "catalog", "catalog-seeds"):
        if len(g) >= 3 and len(set(g)) == len(g):
            sources[canonical(g)].add("seed:" + str(sid))
    for f in sorted((ROOT / "data" / "triad-era" / "growth").glob("r0*.json")):
        for row in json.load(open(f)):
            g = row["glyphs"]
            if len(g) >= 3 and len(set(g)) == len(g):
                sources[canonical(g)].add("grown:" + f.stem)
    ix = Index(recs)

    rows, prow = [], []
    for g in sorted(sources, key=lambda s: [ord(x) for x in s]):
        by = runs.get(g, {})
        R = r_record(g, by, ctl, fam_of, weights, PARAMS["GRID"]) if by else {"families": {}, "strength": None, "sd": None, "bf": None}
        recognised = bool(R["bf"] is not None and R["bf"] >= PARAMS["BF_CERTAIN"] and (R["strength"] or 0) > 0)
        positions = []
        for orient, s in (("forward", list(g)), ("reverse", list(g)[::-1])):
            for p in chart_positions(s):
                if p["kind"] == "triple" and orient == "reverse":
                    continue                                             # a triple is the same set and middle either way
                p["orientation"] = orient
                p["ev"] = position_evidence(p, ix) if p["state"] == "contested" else None
                positions.append(p)
        chart = route_state(positions)
        name = "unmeasured"                                               # CATALOG §7a: until validated
        group = view_group(recognised, chart, name)
        la = ix.lookalike.get("".join(g)) or ix.lookalike.get("".join(g[::-1]))
        rid = hashlib.sha256("".join(g).encode()).hexdigest()[:12]
        rows.append({"id": rid, "glyphs": "".join(g), "length": len(g), "chart_class": chart_class(g), "set_class": set_class(g),
                     "sources": sorted(sources[g]), "r_strength": R["strength"], "r_sd": R["sd"], "r_bf": R["bf"],
                     "r_families": R["families"], "recognised": recognised, "chart_state": chart, "name_state": name,
                     "view": group,
                     "contested": sum(1 for p in positions if p["state"] == "contested"),
                     "contested_asked": sum(1 for p in positions if p["ev"] and p["ev"]["n"]),
                     "lookalike": ({k: {"yes": v[0], "n": v[1]} for k, v in la.items()} if la else None),
                     "evidence": raids.get(g, [])})
        for p in positions:
            ev = p["ev"] or {}
            prow.append({"record": rid, "orientation": p["orientation"], "kind": p["kind"], "idx": p["idx"],
                         "context": "".join(p["context"]), "run_choice": p["run_choice"], "alternative": p["alternative"] or "",
                         "state": p["state"], "instrument": ev.get("instrument"), "n": ev.get("n"), "k": ev.get("k"),
                         "p": ev.get("p"), "baseline": ev.get("baseline"), "delta": ev.get("delta"), "bf": ev.get("bf"),
                         "interp": ev.get("interp"), "controlled": ev.get("controlled"), "felt": ev.get("felt"),
                         "evidence": ev.get("aids") or []})

    rates = [{"rater": rt, "set_class": cls, "yes": y, "n": n} for (rt, cls), (y, n) in sorted(ctl.items())]
    manifest["finished"] = dt.datetime.now().isoformat(timespec="seconds")
    manifest["counts"] = {"answers": len(recs), "records": len(rows), "positions": len(prow),
                          "recognised": sum(r["recognised"] for r in rows),
                          "view": dict(collections.Counter(r["view"] for r in rows if r["view"])),
                          "chart_state": dict(collections.Counter(r["chart_state"] for r in rows))}
    json.dump(manifest, open(out / "manifest.json", "w"), indent=1, ensure_ascii=False, sort_keys=True)
    def write(name, rs, cols):
        with open(out / f"{name}.csv", "w", newline="") as fh:
            w = csv.writer(fh)
            for r in rs:
                w.writerow([json.dumps(r[c], ensure_ascii=False) if isinstance(r[c], (list, dict)) else ("" if r[c] is None else r[c]) for c in cols])
    RC = ["id", "glyphs", "length", "chart_class", "set_class", "sources", "r_strength", "r_sd", "r_bf", "r_families", "recognised",
          "chart_state", "name_state", "view", "contested", "contested_asked", "lookalike", "evidence"]
    PC = ["record", "orientation", "kind", "idx", "context", "run_choice", "alternative", "state", "instrument", "n", "k", "p",
          "baseline", "delta", "bf", "interp", "controlled", "felt", "evidence"]
    write("records", rows, RC); write("positions", prow, PC); write("rates", rates, ["rater", "set_class", "yes", "n"])
    print(json.dumps(manifest["counts"], ensure_ascii=False))
    print("sealed answers dropped:", meta["sealed_dropped"], "| frozen:", meta["frozen_commit"])
    if a.no_db:
        return
    schema = "catalog_" + build
    sql = f"""
BEGIN;
CREATE SCHEMA {schema};
CREATE TABLE {schema}.manifest (doc jsonb);
CREATE TABLE {schema}.records (id text primary key, glyphs text, length int, chart_class text, set_class text, sources jsonb,
  r_strength double precision, r_sd double precision, r_bf double precision, r_families jsonb, recognised boolean,
  chart_state text, name_state text, "view" text, contested int, contested_asked int, lookalike jsonb, evidence jsonb);
CREATE TABLE {schema}.positions (record text, orientation text, kind text, idx int, context text, run_choice text, alternative text,
  state text, instrument text, n int, k int, p double precision, baseline double precision, delta double precision,
  bf double precision, interp text, controlled boolean, felt boolean, evidence jsonb);
CREATE TABLE {schema}.rates (rater text, set_class text, yes int, n int);
\\copy {schema}.records FROM '{out / "records.csv"}' WITH (FORMAT csv)
\\copy {schema}.positions FROM '{out / "positions.csv"}' WITH (FORMAT csv)
\\copy {schema}.rates FROM '{out / "rates.csv"}' WITH (FORMAT csv)
INSERT INTO {schema}.manifest VALUES ('{json.dumps(manifest, ensure_ascii=False).replace("'", "''")}'::jsonb);
CREATE INDEX ON {schema}.positions (record);
DROP SCHEMA IF EXISTS catalog_previous CASCADE;
DO $$ BEGIN IF EXISTS (SELECT 1 FROM pg_namespace WHERE nspname = 'catalog') THEN ALTER SCHEMA catalog RENAME TO catalog_previous; END IF; END $$;
ALTER SCHEMA {schema} RENAME TO catalog;
COMMIT;
"""
    (out / "load.sql").write_text(sql)
    r = subprocess.run(["psql-18", "-v", "ON_ERROR_STOP=1", "-q", a.db, "-f", str(out / "load.sql")], capture_output=True, text=True)
    print("postgres:", "loaded into schema catalog" if r.returncode == 0 else r.stderr[-2000:])

if __name__ == "__main__":
    main()
