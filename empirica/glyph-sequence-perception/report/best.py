#!/usr/bin/env python3
"""A read-off (concern 5): the sequences best recognised as sequences (METHODOLOGY §1; Joseph, 2026-10-05: "generation
is for exploring the space but also counts as a recognition, but recognition is the final goal -- 'best recognized
sequences as sequences' is the goal"). It reads the tree and writes BEST.md; nothing reads BEST.md back, so its
criteria cannot steer probing, the tree, priority or the port. The tree supplies facts (counts per family); every
decision here follows one standard (§2a), stated once.

THE STANDARD
  Estimate  Each family's proportion is a Beta posterior (Jeffreys); a test's estimate is the equal-weight mean over the
            families that answered, its spread treated as normal (an approximation). TR.estimate, TR.estimate_vs.
  Decide    90% one-sided (Z), and >= FAMILIES_MIN families everywhere (1, Joseph, 2026-10-05: "Let's drop the >= 2
            model family cap in 'best'"; the per-family counts stay on every row, so universality stays visible).
    choice  triad middles and order lines: SUPPORTED when the lower bound is >= LEVEL, CONTRADICTED when the upper
            bound is < LEVEL.
    yes/no  against the family's matched control: a whole run (cohere) against its SHUFFLED controls -- the same glyphs
            in an order the run does not predict; a link (inhibit) against NEAR decoys. The difference's lower bound > 0
            is "yes beyond the control", its upper bound < 0 "no beyond it". No fallback where a family lacks controls.
  LEVEL = 0.5 and 90% are choices made without evidence; they gate nothing outside this file.

WHAT IS TESTED
  A run, as a whole  cohere answers about it in either orientation: RECOGNISED when "yes" is beyond the shuffled
            control, REJECTED when "no" is. Evidence about that run only, never its sub-runs.
  A link    positive evidence, counted one way (§2a): GENERATED when >= FAMILIES_MIN families name it as a continuation -- S on
            shown answers (the deciding context, the longest asked suffix, in either reading direction), else W on
            written answers, else P on forced picks (the generator pass, METHODOLOGY §4a). A "none" or another continuation is not evidence against a link (§2b: "a proposal list
            that omits x is not a rejection of x"); it is evidence about an end or a branch. RECOGNISED (R) when not
            generated but recognition answers at the link say "yes" beyond the near control. REJECTED (X) when they
            say "no" beyond it -- the only evidence against a link, and it overrides generation (shown as a conflict).
  Tests     skip tests (yes/no: does the glyph after next come directly after? a sequence predicts no), triads and
            order answers (choice), as before (Tree.consistency_evidence).

TABLES, in this order: runs recognised as wholes (sorted by length, then recognition strength; Joseph: "sort by length
but don't necessarily make that the 'ranking' number"); runs rejected as wholes; candidates -- runs carried by positive
link evidence, not yet asked as wholes; manifested cycles; the controls; link recognition. Candidates are grown from the
strongest single edges by following each context's strongest branch (strongest_paths; Joseph, 2026-10-05), so a
minority answer at a sequence's boundary does not join two sequences; nothing is merged. Seed votes are never evidence. Reasoned and first-impression answers stay apart: the *unr* column. Display only: a run monotonic in numeric
value (else in code points) is shown ascending.

HISTORY: until 2026-10-05 this file confirmed links by continue answers alone, by majority (lower bound >= 0.5), with
"none" counting against -- one kind of evidence among many, used against §2b's own sentence. Morph ladders such as
Joseph's `-=>})|` were invisible as a result (METHODOLOGY §2a).
"""
import collections, json, pathlib, sys, unicodedata

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "tree"))
import tree as TR                                           # noqa: E402

LEVEL = 0.5
FAMILIES_MIN = 1      # families a decision needs (Joseph, 2026-10-05: drop the >= 2 cap in BEST; until then 2)
Z = 1.2816
TOP = 150
BANDS = [(12, 999), (7, 11), (5, 6), (3, 4)]   # length sections of the recognised table (chosen without evidence)
BAND_TOP = 100                                 # rows shown per section
POSITIVE = ("S", "W", "P", "R")
FA = {"claude": "cl", "gemini": "ge", "grok": "gr", "muse": "mu"}

# ------------------------------------------------------------------ the two decision forms
def choice(units):
    """units: [{family: (k, n)}] -> (verdict, observed, lower, families naming); verdict "supported" | "contradicted" | None"""
    units = [u for u in units if u]
    if not units:
        return None, None, None, set()
    obs, mean, sd, fams = TR.estimate(units)
    if len(set().union(*units)) < FAMILIES_MIN:
        return None, obs, mean - Z * sd, fams
    if mean - Z * sd >= LEVEL:
        return "supported", obs, mean - Z * sd, fams
    if mean + Z * sd < LEVEL:
        return "contradicted", obs, mean - Z * sd, fams
    return None, obs, mean - Z * sd, fams

def yesno(counts, control):
    """counts, control: {family: (yes, n)} -> (verdict, difference, sd); verdict "beyond" | "below" | None"""
    d, sd, fams = TR.estimate_vs(counts, control)
    if d is None or len(fams) < FAMILIES_MIN:
        return None, d, sd
    if d - Z * sd > 0:
        return "beyond", d, sd
    if d + Z * sd < 0:
        return "below", d, sd
    return None, d, sd

def strength(counts, control):
    """how surely a whole run is recognised, for RANKING only (the verdict stays yesno's). Per family, "yes" beyond its
    shuffled rate as a share of what is possible beyond it -- Abbott's correction, (p - c) / (1 - c), so families with
    different baselines are on one scale (Grok calls 39% of shuffles coherent, Claude 21%) -- then the families
    combined by precision (inverse variance; the fixed-effect estimate), so a family with one answer adds a little and
    more answers raise confidence instead of diluting it (2026-10-06: an equal-weight mean ranked the block ladder,
    Claude 3/3 and Grok 1/1, below a chart walk only Claude had answered) -> (mean, sd)"""
    num = den = 0.0
    for f, (k, n) in counts.items():
        ck, cn = control.get(f, (0, 0))
        if not n or not cn:
            continue
        (m, v), (mc, vc) = TR.beta_mv(k, n), TR.beta_mv(ck, cn)
        a = (m - mc) / (1 - mc)
        va = (v + vc * ((1 - m) / (1 - mc)) ** 2) / (1 - mc) ** 2      # delta method
        num += a / va; den += 1 / va
    return (num / den, (1 / den) ** 0.5) if den else (None, None)

def near(Tp, counts):
    return {f: Tp.control_counts(f, "near") for f in counts}

def shuffled(Tp, counts):
    return {f: Tp.cohere_control_counts(f, "shuffled") for f in counts}

# ------------------------------------------------------------------ links
def link(g, i, Tp):
    """the evidence on link g[i]-g[i+1], both reading directions -> {status, gen, obs, fams, rec, uk, un}"""
    a, b = g[i], g[i + 1]
    fwd, bwd = g[:i + 1], g[i + 1:][::-1]                  # the run before b (forward); before a (backward)
    shown = [d for d in (Tp.shown_dir(fwd, b), Tp.shown_dir(bwd, a)) if d]
    written = [w for w in (Tp.written_dir(fwd, b), Tp.written_dir(bwd, a)) if w]
    naming = lambda ds: set().union(*({f for f, (k, n) in d["counts"].items() if k > 0} for d in ds)) if ds else set()
    picked = [d for d in (Tp.pick_dir(fwd, b), Tp.pick_dir(bwd, a)) if d]
    sf, wf, pf = naming(shown), naming(written), naming(picked)
    gen = "S" if len(sf) >= FAMILIES_MIN else ("W" if len(wf) >= FAMILIES_MIN else ("P" if len(pf) >= FAMILIES_MIN else None))
    basis = {"W": written, "P": picked}.get(gen) or shown or written or picked
    obs, mean, sd = (TR.estimate([d["counts"] for d in basis])[:3]) if basis else (None, None, None)
    rc = collections.defaultdict(lambda: [0, 0])
    for d in (Tp.recognition_dir(fwd, b), Tp.recognition_dir(bwd, a)):
        for f, (y, n) in (d or {}).items():
            rc[f][0] += y; rc[f][1] += n
    rc = {f: tuple(v) for f, v in rc.items()}
    rec = yesno(rc, near(Tp, rc))[0] if rc else None
    status = "X" if rec == "below" else (gen or ("R" if rec == "beyond" else None))
    return {"status": status, "gen": gen, "obs": obs, "mean": mean, "sd": sd, "fams": len({"S": sf, "W": wf, "P": pf}.get(gen, set())), "rec": rec,
            "uk": sum(d["uk"] for d in shown), "un": sum(d["un"] for d in shown)}

def judge(g, Tp):
    return [link(g, i, Tp) for i in range(len(g) - 1)]

def link_summary(ls):
    c = collections.Counter(l["status"] or "–" for l in ls)
    conflict = sum(1 for l in ls if l["status"] == "X" and l["gen"])
    obs = [l["obs"] for l in ls if l["obs"] is not None]
    return {"kinds": c, "conflict": conflict, "agreement": sum(obs) / len(obs) if obs else None,
            "unreasoned": (sum(l["uk"] for l in ls), sum(l["un"] for l in ls))}

def link_cell(s):
    c = s["kinds"]
    out = " ".join(f"{k}{c[k]}" for k in ("S", "W", "P", "R", "X", "–") if c.get(k))
    return out + (f" ⚠{s['conflict']}" if s["conflict"] else "")

def tests(Tp, g, cyclic=False):
    """skip, triad and order evidence on a run -> {kind: (passed, challenged)}"""
    ev = Tp.consistency_evidence(g, cyclic)
    out = {}
    v = [yesno(u, near(Tp, u))[0] for u in ev["skip"]]          # a sequence predicts "no"
    out["skip"] = (v.count("below"), v.count("beyond"))
    for kind in ("triad", "order"):
        v = [choice([u])[0] for u in ev[kind]]
        out[kind] = (v.count("supported"), v.count("contradicted"))
    return out

def test_cell(t):
    detail = " ".join(f"{kind[0]}{p}/{c}" for kind, (p, c) in t.items() if p + c)
    return (("⚠ " if any(c for _, c in t.values()) else "") + detail) if detail else "–"

# ------------------------------------------------------------------ candidate runs: strongest edges, strongest branches
def fam_dist(fl):
    """{family: [answers]} -> ranked [(x, (agreement, families naming, answers))], as Tree.dist/ranked do"""
    per = collections.defaultdict(dict); cnt = collections.Counter(); fams = collections.defaultdict(set)
    for f, xs in fl.items():
        for x, n in collections.Counter(xs).items():
            per[x][f] = n / len(xs); cnt[x] += n; fams[x].add(f)
    d = {x: (sum(per[x].values()) / len(fl), len(fams[x]), cnt[x]) for x in per}
    return sorted(d.items(), key=lambda kv: (-kv[1][0], -kv[1][1], -kv[1][2], kv[0]))

def strongest(Tp, run):
    """the strongest branch after `run`: at the deciding shown context (the longest asked suffix), else the longest
    picked suffix (forced picks), else the longest written one -> (x, agreement, families) or None"""
    ctx = Tp.lookup(run)
    if ctx:
        x, (agr, nf, _) = Tp.ranked(ctx)[0]
        return x, agr, nf
    for store, kmax in ((Tp.picks, TR.PICK_MAXK), (Tp.written, TR.MAXK)):
        for j in range(min(kmax, len(run)), 1, -1):
            fl = store.get(tuple(run[-j:]))
            if fl:
                x, (agr, nf, _) = fam_dist(fl)[0]
                return x, agr, nf
    return None

def follow(Tp, path, cap=64):
    """extend `path` forward along the strongest branch until an end ("none" or another non-glyph is strongest), a
    branch named by fewer than 2 families, a return to a glyph already in the path, or no evidence"""
    path = list(path)
    while len(path) < cap:
        s = strongest(Tp, path)
        if not s or s[0] in (TR.NONE, TR.OTHER) or s[2] < FAMILIES_MIN or s[0] in path:
            break
        path.append(s[0])
    return path

def strongest_paths(Tp):
    """Candidate runs for display (Joseph, 2026-10-05: "finding some of the strongest single edges, then following
    their strongest branch ... something that stops 'best' from pulling in too much of the cross-sequence jumps").
    Edges: each context's strongest continuation, named by >= FAMILIES_MIN families (shown contexts, and picked ones), strongest
    first. From each edge not yet in a path, follow the strongest branch forward and then backward; keep the stretch
    around the edge whose every link has positive evidence (S, W, P or R). A weaker branch is not erased: it is a row
    of its own once its own edge comes up. Nothing is merged."""
    edges = []
    for ctx in Tp.nodes:
        x, (agr, nf, _) = Tp.ranked(ctx)[0]
        if x not in (TR.NONE, TR.OTHER) and nf >= FAMILIES_MIN and x not in ctx:
            edges.append((agr, ctx, x))
    for ctx, fl in Tp.picks.items():
        x, (agr, nf, _) = fam_dist(fl)[0]
        if x not in (TR.NONE, TR.OTHER) and nf >= FAMILIES_MIN and x not in ctx:
            edges.append((agr, ctx, x))
    edges.sort(key=lambda e: (-e[0], e[1], e[2]))
    covered, out = set(), []
    for agr, ctx, x in edges:
        if frozenset((ctx[-1], x)) in covered:
            continue
        full = follow(Tp, follow(Tp, list(ctx) + [x])[::-1])[::-1]
        i = next(k for k in range(len(full) - 1) if full[k] == ctx[-1] and full[k + 1] == x)
        ls = judge(full, Tp)
        a, b = i, i
        while a > 0 and ls[a - 1]["status"] in POSITIVE:
            a -= 1
        while b < len(ls) - 1 and ls[b + 1]["status"] in POSITIVE:
            b += 1
        if ls[i]["status"] not in POSITIVE:
            covered.add(frozenset((ctx[-1], x))); continue
        seg, sl = full[a:b + 2], ls[a:b + 1]
        covered |= {frozenset(p) for p in zip(seg, seg[1:])}
        if len(seg) >= 3:
            out.append({"glyphs": seg, "links": sl, "seed": agr})
    kept = []
    for c in sorted(out, key=lambda c: -len(c["glyphs"])):
        if not any(contained(c["glyphs"], k["glyphs"]) for k in kept):
            kept.append(c)
    return kept

def contained(g, k):
    """is run g part of run k, in either direction?"""
    n = len(g)
    return n <= len(k) and any(list(k[i:i + n]) in (list(g), list(g)[::-1]) for i in range(len(k) - n + 1))

def shown_order(g):
    """display only: a run strictly monotonic in Unicode numeric value (every glyph having one) is shown ascending by
    value, else a run monotonic in code points ascending"""
    vals = [unicodedata.numeric(c, None) for c in g]
    keys = vals if all(v is not None for v in vals) else [ord(c) for c in g]
    return g[::-1] if all(b < a for a, b in zip(keys, keys[1:])) else g

def render(g, links):
    """a run for display, a visual aid (Joseph, 2026-10-05): glyphs joined by a space, or by "│" at a BREAK -- a link
    confidently weaker than the run's typical link, from the links' posteriors (Joseph: "Aren't there bayesian updates
    happening? Don't we have real confidences?"): its 90% upper bound is below the median posterior mean of the run's
    links. A link on thin evidence (a wide interval) or without generation evidence is not marked: it is not known to be
    weak. Shown ascending when monotonic (shown_order), the marks following."""
    means = sorted(l["mean"] for l in links if l["gen"] and l["mean"] is not None)
    med = means[len(means) // 2] if means else None
    flags = [not (med is not None and l["gen"] and l["mean"] is not None and l["mean"] + Z * l["sd"] < med) for l in links]
    g = list(g)
    if shown_order(g) != g:
        g, flags = g[::-1], flags[::-1]
    return g[0] + "".join((" " if f else "│") + x for f, x in zip(flags, g[1:]))

def orders_found(Tp):
    """per shown set, the order its answers most often give (METHODOLOGY §4a, the order question; both eras pooled):
    each answer's main line (its longest), steps in order, a tie as one step, either direction counted as one ->
    [{set, best, k, n, per family {f: (k, n)}}]"""
    by = collections.defaultdict(list)
    for x, items in Tp.orders.items():
        for f, shown, lines in items:
            by[frozenset(shown)].append((f, tuple(shown), lines))
    out = []
    for key, rows in by.items():
        seen, cnt, fam = set(), collections.Counter(), collections.defaultdict(lambda: [0, 0])
        canon_of = []
        for f, shown, lines in rows:
            if (f, shown, id(lines)) in seen:
                continue
            seen.add((f, shown, id(lines)))
            main = max(lines, key=lambda ln: sum(len(st) for st in ln if st != "GAP"))
            c = tuple("…" if st == "GAP" else "=".join(sorted(st)) for st in main)
            c = min(c, c[::-1])
            canon_of.append((f, c))
        for f, c in canon_of:
            cnt[c] += 1
        best, k = cnt.most_common(1)[0]
        for f, c in canon_of:
            fam[f][1] += 1; fam[f][0] += c == best
        out.append({"set": key, "best": best, "k": k, "n": len(canon_of), "fam": {f: tuple(v) for f, v in fam.items()}})
    return out

def fold(w):
    return f" (+{w['folded']})" if w.get("folded") else ""

def us(g):
    return sum(len(c.encode("utf-8")) for c in g) / len(g)

def fam_cells(counts, fams):
    return " ".join(f"{FA.get(f, f)} {counts[f][0]}/{counts[f][1]}" for f in fams if f in counts) or "–"

# ------------------------------------------------------------------ BEST.md
def wholes(Tp):
    """runs asked as wholes, one entry per run (either orientation), keyed by the lesser orientation -> {key: {glyphs,
    counts, verdict (yesno's: "beyond" | "below" | None), d, s, lb}}. Also read by report/view.py, which sets BEST's
    verdicts beside the catalog's."""
    whole = {}
    for run in Tp.cohere:
        key = tuple(min(list(run), list(run)[::-1]))
        if key not in whole:
            counts = Tp.coherence(list(run))
            own = Tp.own_shuffles(run)               # recognised as a SEQUENCE: against its own glyphs shuffled, not the
            v, d, _ = yesno(counts, own) if own else (None, None, None)   # pooled shuffle rate (until 2026-10-06, when
            sm, ss = strength(counts, own) if own else (None, None)       # sets coherent in any order passed; Joseph:
                                                                          # "Our entire premise was based on recognizing
                                                                          # sequences-- not sets.")
            whole[key] = {"glyphs": list(run), "counts": counts, "verdict": v, "d": d, "s": sm,
                          "lb": (sm - Z * ss) if sm is not None else None}
    return whole

def main():
    recs = TR.load()
    Tp = TR.Tree(recs, seeds=False)
    rounds = sorted({r["round"] for r in recs if r["round"] != "seed"}, key=lambda x: (x[0] != "r", int("".join(c for c in x[1:] if c.isdigit()) or 0), x))
    fams_all = sorted(set(Tp.cohere_rate) | set(Tp.inhibit_rate))

    whole = wholes(Tp)
    recognised = [w for w in whole.values() if w["verdict"] == "beyond"]
    rejected = [w for w in whole.values() if w["verdict"] == "below"]
    undecided = [w for w in whole.values() if w["verdict"] is None]
    for w in recognised + rejected:
        w["ls"] = judge(w["glyphs"], Tp)
        w["links"] = link_summary(w["ls"])
        w["tests"] = tests(Tp, w["glyphs"])
    recognised.sort(key=lambda w: (-len(w["glyphs"]), -w["lb"], w["glyphs"]))
    kept = []                                            # display: a recognised run folds into a longer recognised one that
    for w in recognised:                                 # contains it AND is at least as confidently recognised (lower bound);
        host = next((k for k in kept if contained(w["glyphs"], k["glyphs"]) and k["lb"] >= w["lb"]), None)   # else it stands
        if host:
            host["folded"] = host.get("folded", 0) + 1
        else:
            kept.append(w)
    n_recognised, recognised = len(recognised), kept
    rejected.sort(key=lambda w: (-len(w["glyphs"]), w["d"], w["glyphs"]))

    cand = [c for c in strongest_paths(Tp) if tuple(min(c["glyphs"], c["glyphs"][::-1])) not in whole]
    for c in cand:
        c["summary"] = link_summary(c["links"])
        c["fmin"] = min(l["fams"] for l in c["links"])
    cand.sort(key=lambda c: (-len(c["glyphs"]), -c["fmin"], c["glyphs"]))

    cyc = sorted((c for c in Tp.cycles.values() if c["distinct"] >= 4), key=lambda c: (-len(c["families"]), -c["answers"]))
    fa = lambda fs: " ".join(FA.get(f, f) for f in sorted(fs))

    L = ["# Sequences recognised as sequences", "",
         f"*Generated by `report/best.py` after {rounds[-1]}. A read-off: nothing reads it back. The goal (METHODOLOGY §1) is sequences recognised as sequences: runs that minds of several families, shown the whole run, perceive as a progression. Decisions follow one standard (`best.py`): per family a Beta posterior (Jeffreys), averaged over families, 90% confidence; one family suffices, and each row shows its families. A whole run is **recognised as a sequence** when its families' \"yes, coherent\" rate is beyond their rate for **its own glyphs shuffled** (the controls asked beside it): the order, not just the set, is what they recognise. A run whose shuffles were never asked is undecided. Links carry positive evidence one way: a \"none\" or another continuation is never evidence against a link, only a \"no\" beyond the control is. Seed votes are never evidence. The full tree is in `SEQUENCES.md`.*", "",
         f"**{n_recognised} runs recognised as wholes** ({len(recognised)} after folding runs contained in longer ones), {len(rejected)} rejected, {len(undecided)} undecided so far (of {len(whole)} asked); **{len(cand)} candidate runs** carried by positive link evidence, not yet asked as wholes; **{len(cyc)} manifested cycles**.", ""]

    L += ["## Recognised as wholes", "",
          f"*In sections by length (the organiser), each ordered by recognition strength, so short runs are not pushed off the page by long ones (2026-10-06: the single length-sorted table showed only runs of ~14+ glyphs, almost all single-block, and hid every short cross-block run). Up to {BAND_TOP} rows a section.*", ""]
    for lo, hi in BANDS:
        band = sorted((w for w in recognised if lo <= len(w["glyphs"]) <= hi), key=lambda w: (-w["lb"], -len(w["glyphs"]), w["glyphs"]))
        L += [f"### {lo}–{hi} glyphs ({len(band)})" if hi < 99 else f"### {lo}+ glyphs ({len(band)})", "",
              "| # | run | n | us | ≥ | beyond chance | yes/n per family | links | unr | tests |", "|---|---|---|---|---|---|---|---|---|---|"]
        for i, w in enumerate(band[:BAND_TOP], 1):
            k, n = w["links"]["unreasoned"]
            L.append(f"| {i} | `{render(w['glyphs'], w['ls'])}`{fold(w)} | {len(w['glyphs'])} | {us(w['glyphs']):.1f} | {w['lb']:+.2f} | {w['s']:+.2f} | {fam_cells(w['counts'], fams_all)} | {link_cell(w['links'])} | {f'{k}/{n}' if n else '–'} | {test_cell(w['tests'])} |")
        if not band:
            L.append("| – | *none yet* | | | | | | | | |")
        if len(band) > BAND_TOP:
            L += ["", f"*{len(band) - BAND_TOP} more in this section, weaker.*"]
        L.append("")
    L += ["", "*Key:*",
          "- **n**: glyphs. **us**: the mean UTF-8 bytes per glyph (1 = ASCII … 4 = astral planes). **(+k)**: k recognised runs contained in this one, and no more confidently recognised than it, folded into it. A contained run recognised more confidently than the run around it stands as its own row.",
          "- **beyond chance**: recognition strength. Per family, \"yes, coherent\" beyond its rate for shuffled runs, as a share of what is possible beyond that rate (Abbott's correction, so families with different baselines share one scale). The families are combined by precision, so a family with one answer adds a little. 1 = every answer yes; 0 = no better than shuffled.",
          "- **≥**: how surely, the 90% lower bound of *beyond chance*. It orders runs within a section, so more answers and more families raise a run rather than dilute it. The verdict, recognised or not, is the yes/no standard above, unchanged. (Until 2026-10-06 an equal-weight mean ordered the runs, and the block ladder, Claude 3/3 and Grok 1/1, ranked below a chart walk only Claude had answered.)",
          "- **yes/n per family**: \"yes\" answers / answers about this run, either orientation (cl = Claude, ge = Gemini, gr = Grok).",
          "- **links**: each link's strongest evidence. **S**: generated in shown answers. **W**: generated in written answers. **P**: picked in the forced generator pass (METHODOLOGY §4a). **R**: not generated, but recognised (yes beyond the near control). **X**: rejected (no beyond the near control). **–**: no evidence either way yet. **⚠**: generated *and* rejected.",
          "- **unr**: shown answers given with 0 thinking tokens that name the links, of all such answers there. Reasoned and first-impression answers stay apart until the data says whether they differ (METHODOLOGY §2a).",
          "- **tests**: passed/challenged. **s**: skip tests (a sequence predicts no). **t**: triads. **o**: order answers (triad era). A ⚠ marks a challenge; **–** means untested.",
          "- **│** between two glyphs: a break, a link confidently weaker than the run's typical link. Its 90% upper bound (from the link's posterior) is below the median posterior mean of the run's links. A link on thin evidence, or without generation evidence, is not marked, because it isn't known to be weak. A visual aid only; it decides nothing.",
          "- Display: a run monotonic in numeric value (else in code points) is shown ascending.", ""]

    L += ["## Rejected as wholes", "", "| # | run | n | yes − shuffled | yes/n per family | links | tests |", "|---|---|---|---|---|---|---|"]
    for i, w in enumerate(rejected[:TOP], 1):
        L.append(f"| {i} | `{render(w['glyphs'], w['ls'])}` | {len(w['glyphs'])} | {w['d']:+.2f} | {fam_cells(w['counts'], fams_all)} | {link_cell(w['links'])} | {test_cell(w['tests'])} |")
    if not rejected:
        L.append("| – | *none yet* | | | | | |")
    L += ["", "*\"No, not coherent\" beyond the shuffled control: the families find this run *less* coherent than runs shuffled out of order. Shown as asked, not reordered.*", ""]

    L += ["## Candidates: positive link evidence, not yet asked as wholes", "", "| # | run | n | us | agr | links | ≥ fam | unr |", "|---|---|---|---|---|---|---|---|"]
    for i, c in enumerate(cand[:TOP], 1):
        s = c["summary"]; k, n = s["unreasoned"]
        agr = f"{s['agreement']:.2f}" if s["agreement"] is not None else "–"
        L.append(f"| {i} | `{render(c['glyphs'], c['links'])}` | {len(c['glyphs'])} | {us(c['glyphs']):.1f} | {agr} | {link_cell(s)} | {c['fmin']} | {f'{k}/{n}' if n else '–'} |")
    if len(cand) > TOP:
        L += ["", f"*{len(cand) - TOP} shorter candidates not shown.*"]
    L += ["", "*Strongest edges first: each context's strongest continuation, then the strongest branch followed forward and backward until \"none\" is the strongest answer, or the path returns on itself. Each row is the stretch around its edge whose every link has positive evidence (S, W, P or R, as above). A weaker branch is its own row once its own edge comes up, and nothing is merged. Candidates, not findings: recognition of the whole run decides. **agr**: the mean share of answers naming each link where it was asked, a perceptual quantity and not a gate. **≥ fam**: the fewest families generating any one link (0 where a link rests on recognition alone).*", ""]

    od = [o for o in orders_found(Tp) if o["k"] >= 2]
    od.sort(key=lambda o: (-sum(1 for st in o["best"] if st != "…"), -o["k"] / o["n"], o["best"]))
    L += ["## Orders found", "", "| # | order | set | agree | per family |", "|---|---|---|---|---|"]
    for i, o in enumerate(od[:TOP], 1):
        b = list(o["best"]); vals = [st for st in b if st != "…" and "=" not in st]
        if len(vals) == len(b) and shown_order(vals) != vals:
            b = b[::-1]
        L.append(f"| {i} | `{' '.join(b)}` | {len(o['set'])} | {o['k']}/{o['n']} | {fam_cells(o['fam'], sorted(o['fam']))} |")
    L += ["", "*Order questions (a set shown scrambled: put it in the sequence it seems to form; the triad era's and the new rounds' pooled): per set, the order its answers most often give as their main line, either direction counted as one. **=** joins symbols put at the same step; **…** is a GAP, a step the mind thinks is missing. **set**: glyphs shown. **agree**: answers giving this order / answers with a line. Sets where at least two answers agree; sorted by how many glyphs the order places.*", ""]
    if cyc:
        L += ["## Manifested cycles", "", "| cycle | n | ans | fam |", "|---|---|---|---|"]
        L += [f"| `{' '.join(c['pattern'])} ↻` | {len(c['pattern'])} | {c['answers']} | {fa(c['families'])} |" for c in cyc[:40]]
        L += ["", "*A mind wrote the whole period twice after being shown less than one period. **n**: glyphs in the period. **ans**: answers that manifested it. **fam**: families.*", ""]

    L += ["## Controls", "", "| family | cohere: runs | shuffled | chart windows | inhibit: candidates | near | far |", "|---|---|---|---|---|---|---|"]
    for f in fams_all:
        cells = []
        for cls in ("real", "shuffled", "chart"):
            y, n = Tp.cohere_control_counts(f, cls)
            cells.append(f"{y / n:.2f} ({n})" if n else "—")
        for cls in ("real", "near", "far"):
            y, n = Tp.control_counts(f, cls)
            cells.append(f"{y / n:.2f} ({n})" if n else "—")
        L.append(f"| {f} | " + " | ".join(cells) + " |")
    L += ["", "*\"Yes\" rates (answers).*",
          "- **cohere**: whole runs, asked *does this look like a coherent sequence?* **shuffled**: the same glyphs in an order the run does not predict; this is the decision baseline. **chart windows**: contiguous code-point runs from elsewhere in Unicode. They are a measurement, not a decoy, because Unicode lays many real sequences out in chart order.",
          "- **inhibit**: does a candidate come directly after a shown run? **near** / **far**: matched decoys, from the same neighbourhood of the code chart or from a distant part of Unicode.", ""]

    rec = Tp.recognition_evidence()
    if rec:
        for r in rec:
            r["verdict"] = yesno(r["counts"], near(Tp, r["counts"]))[0]
        good = [r for r in rec if r["verdict"] == "beyond"]
        L += ["## Link recognition", "", f"**{len(good)} of {len(rec)} candidate links recognised** (yes beyond the near control).", "",
              "| context | cand. | rec. | yes/n per family |", "|---|---|---|---|"]
        for r in sorted(rec, key=lambda r: (r["verdict"] != "beyond", r["verdict"] != "below", r["x"]))[:80]:
            L.append(f"| `{' '.join(r['ctx'])}` | `{r['x']}` | {'yes' if r['verdict'] == 'beyond' else ('no' if r['verdict'] == 'below' else '–')} | {fam_cells(r['counts'], sorted(r['counts']))} |")
        L += ["", "*Inhibit questions: does the candidate come directly after the shown run? **rec.**: yes = recognised, no = rejected beyond the control, – = undecided.*", ""]
    (ROOT / "BEST.md").write_text("\n".join(L) + "\n")
    print("\n".join(L[:5]))

if __name__ == "__main__":
    main()
