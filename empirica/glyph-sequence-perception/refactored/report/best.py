#!/usr/bin/env python3
"""A read-off (concern 5): the best-confirmed stretches of sequence in the tree right now. It reads the tree and writes
BEST.md; nothing reads BEST.md back (the planner never sees it), so its definition of "best" cannot steer probing, the
tree, priority or the port. The tree supplies the evidence as facts (counts per family); every DECISION here follows
one standard, stated once (Joseph, 2026-10-05: "make sure the evidence is very defensible and not a ... mishmash of
heuristics").

THE STANDARD
  Estimate  For any test, each family's proportion of the response the claim predicts is a Beta posterior (Jeffreys
            prior, Beta(1/2, 1/2)); the test's estimate is the equal-weight mean over the families that answered -- the
            claims are about families -- with its spread (the means treated as normal: an approximation). TR.estimate,
            TR.estimate_vs.
  Decide    90% one-sided (Z), and >= 2 families, everywhere. Two forms, by the kind of answer:
    choice  the mind picks among answers (continuations, triad middles, order lines): SUPPORTED when the lower bound
            is >= LEVEL ("most answers give it"), CONTRADICTED when the upper bound is < LEVEL, else undecided.
    yes/no  the mind may say yes to anything (recognition, skip tests): against the family's NEAR control (decoys
            from the same neighbourhood of the code chart -- the right reference for an in-block candidate): the
            difference's lower bound > 0 means "yes beyond the control"; its upper bound < 0, "no beyond it". A family
            without near-control answers cannot decide yet (no fallback).
  LEVEL = 0.5 and the 90% are choices made without evidence; they gate nothing outside this file.

WHAT IS TESTED
  Links (choice). A link a-b of a candidate run, from both reading directions (a sequence and its reverse are one
            sequence): in each direction the answers at the deciding shown context (the longest asked suffix of the run
            up to the earlier glyph -- the most specific question asked there), every answer counting, "none" as not
            naming the link. CONFIRMED when supported, with >= 2 families naming it. A one-way link (e.g. ⓪ -> ①
            forward but "none" backward) reads as weaker, as it is.
  Written   Only where neither direction has shown answers: the same on written answers (the later glyphs of continue
            answers) whose context is a suffix of the run before the link. Written contexts are not chosen by anyone
            -- each is however much the mind had written -- so all of them consistent with the run are pooled.
  Tests     For confirmed stretches (Tree.consistency_evidence): skip tests (yes/no: does the glyph after next come
            directly after? A sequence predicts no), triads (choice: each triple's middle, both eras), order answers
            (choice: lines in the stretch's order, triad era). Each is passed (supported / no beyond control) or
            challenged (contradicted / yes beyond control).
  Recognition (yes/no): a candidate is recognised when "yes" is beyond the near control.

TABLES: stretches (maximal runs of confirmed links, >= 3 glyphs); runs carried by written answers awaiting shown
confirmation; recognition. Candidates are walks of the tree with seed votes and of the tree with written answers pooled
in; overlapping runs are merged and judged again (a link's context depends on the run before it); confirmed rotations
are one entry, marked as wrapping. Ranked by length, then the weakest link's lower bound. Display only: a run monotonic
in numeric value (else in code points) is shown ascending.
"""
import collections, pathlib, sys, unicodedata

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "tree"))
import tree as TR                                           # noqa: E402

LEVEL = 0.5
Z = 1.2816
TOP = 150
TOP_WRITTEN = 100

# ------------------------------------------------------------------ the two decision forms
def choice(units):
    """units: [{family: (k, n)}] (one per reading direction or one test) -> (verdict, observed, lower, families naming).
    verdict: "supported" | "contradicted" | None"""
    units = [u for u in units if u]
    if not units:
        return None, None, None, set()
    obs, mean, sd, fams = TR.estimate(units)
    answering = set().union(*units)
    if len(answering) < 2:
        return None, obs, mean - Z * sd, fams
    if mean - Z * sd >= LEVEL:
        return "supported", obs, mean - Z * sd, fams
    if mean + Z * sd < LEVEL:
        return "contradicted", obs, mean - Z * sd, fams
    return None, obs, mean - Z * sd, fams

def yesno(counts, Tp):
    """counts: {family: (yes, n)} -> "beyond" (yes beyond the near control) | "below" (no beyond it) | None"""
    control = {f: Tp.control_counts(f, "near") for f in counts}
    d, sd, fams = TR.estimate_vs(counts, control)
    if d is None or len(fams) < 2:
        return None
    if d - Z * sd > 0:
        return "beyond"
    if d + Z * sd < 0:
        return "below"
    return None

# ------------------------------------------------------------------ links
def judge(g, Tp):
    """-> per link i (g[i]-g[i+1]): ("S"|"W", observed, families naming, unreasoned k, n, lower bound) | None"""
    out = []
    for i in range(len(g) - 1):
        a, b = g[i], g[i + 1]
        fwd, bwd = g[:i + 1], g[i + 1:][::-1]                  # the run before b (forward); before a (backward)
        ds = [d for d in (Tp.shown_dir(fwd, b), Tp.shown_dir(bwd, a)) if d]
        st = None
        if ds:
            v, obs, lb, fams = choice([d["counts"] for d in ds])
            if v == "supported" and len(fams) >= 2:
                st = ("S", obs, len(fams), sum(d["uk"] for d in ds), sum(d["un"] for d in ds), lb)
        else:
            ws = [w for w in (Tp.written_dir(fwd, b), Tp.written_dir(bwd, a)) if w]
            if ws:
                v, obs, lb, fams = choice([w["counts"] for w in ws])
                if v == "supported" and len(fams) >= 2:
                    st = ("W", obs, len(fams), 0, 0, lb)
        out.append(st)
    return out

def tests(Tp, g, cyclic=False):
    """falsification and consistency of a confirmed stretch (a wrapping one tested as a cycle) -> {kind: (passed, challenged)}"""
    ev = Tp.consistency_evidence(g, cyclic)
    out = {}
    v = [yesno(u, Tp) for u in ev["skip"]]                     # a sequence predicts "no"
    out["skip"] = (v.count("below"), v.count("beyond"))
    for kind in ("triad", "order"):
        v = [choice([u])[0] for u in ev[kind]]
        out[kind] = (v.count("supported"), v.count("contradicted"))
    return out

# ------------------------------------------------------------------ runs
def runs(g, links, allowed, need_w):
    """maximal runs of links whose status is in `allowed` (>= 2 links), optionally holding >= 1 'W'"""
    out, cur = [], []
    for i, lk in enumerate(links + [None]):
        if lk and lk[0] in allowed:
            cur.append((i, lk))
            continue
        if len(cur) >= 2 and (not need_w or any(l[0] == "W" for _, l in cur)):
            a, b = cur[0][0], cur[-1][0] + 1
            ls = [l for _, l in cur]
            out.append({"glyphs": g[a:b + 1], "agreement": sum(l[1] for l in ls) / len(ls),
                        "families_min": min(l[2] for l in ls), "lb": min(l[5] for l in ls),
                        "written_links": sum(1 for l in ls if l[0] == "W"), "shown_links": sum(1 for l in ls if l[0] == "S"),
                        "unreasoned": (sum(l[3] for l in ls), sum(l[4] for l in ls))})
        cur = []
    return out

def join2(a, b):
    """a and b overlapping by >= 2 glyphs (a's end = b's start) with no other shared glyph -> the joined run, else None"""
    for k in range(min(len(a), len(b)) - 1, 1, -1):
        if a[-k:] == b[:k] and not set(a[:-k]) & set(b[k:]):
            return a + b[k:]
    return None

def merge(seqs):
    """merge runs that overlap by >= 2 glyphs, in either orientation, until none do"""
    seqs = [list(s) for s in seqs]
    while True:
        done = False
        for i in range(len(seqs)):
            for j in range(len(seqs)):
                if i == j:
                    continue
                for b in (seqs[j], seqs[j][::-1]):
                    m = join2(seqs[i], b)
                    if m:
                        seqs = [x for k, x in enumerate(seqs) if k not in (i, j)] + [m]
                        done = True
                        break
                if done:
                    break
            if done:
                break
        if not done:
            return seqs

def collect(cands, Tp, allowed, need_w):
    found = {}
    for g in cands:
        for st in runs(g, judge(g, Tp), allowed, need_w):
            key = tuple(min(st["glyphs"], st["glyphs"][::-1]))
            if key not in found or st["lb"] > found[key]["lb"]:
                found[key] = st
    return list(found.values())

def dedupe(items):
    """one entry per run (either orientation); confirmed rotations of one run are one entry marked as wrapping (a cycle
    confirmed link by link, which is not the same as a manifested one); runs contained in a longer one are that one"""
    best = {}
    for s in items:
        key = tuple(min(s["glyphs"], s["glyphs"][::-1]))
        if key not in best or s["lb"] > best[key]["lb"]:
            best[key] = s
    rot = collections.defaultdict(list)
    for key, s in best.items():
        if len(set(s["glyphs"])) == len(s["glyphs"]):
            rot[TR.canon_cycle(list(s["glyphs"]))].append(key)
    for keys in rot.values():
        if len(keys) > 1:
            keep = max(keys, key=lambda k: best[k]["lb"])
            best[keep]["wraps"] = True
            for k in keys:
                if k != keep:
                    best.pop(k)
    kept = []
    for s in sorted(best.values(), key=lambda s: (-len(s["glyphs"]), not s.get("wraps"), -s["lb"])):
        if not any(k is not s and contained(s["glyphs"], k) for k in kept):
            kept.append(s)
    kept.sort(key=lambda s: (-len(s["glyphs"]), -s["lb"], s["glyphs"]))
    return kept

def contained(g, k):
    """is run g part of run k (either direction)? Round the circle if k wraps."""
    kg = list(k["glyphs"]) * (2 if k.get("wraps") else 1)
    n = len(g)
    return n <= len(k["glyphs"]) and any(kg[i:i + n] in (list(g), list(g)[::-1]) for i in range(len(kg) - n + 1))

def table(allowed, need_w, cands, Tp):
    first = collect(cands, Tp, allowed, need_w)
    merged = merge([s["glyphs"] for s in first])
    return dedupe(first + collect(merged, Tp, allowed, need_w))

def shown_order(g):
    """display only (a sequence and its reverse are one sequence; Joseph, 2026-10-05): a run strictly monotonic in Unicode
    numeric value (every glyph having one) is shown ascending by value -- `¹ ² ³` (Latin-1) beside `⁰ ⁴ … ⁹`
    (U+2070-2079) are not monotonic in code points -- else a run monotonic in code points is shown ascending"""
    vals = [unicodedata.numeric(c, None) for c in g]
    keys = vals if all(v is not None for v in vals) else [ord(c) for c in g]
    return g[::-1] if all(b < a for a, b in zip(keys, keys[1:])) else g

# ------------------------------------------------------------------ BEST.md
def main():
    recs = TR.load()
    Tp = TR.Tree(recs, seeds=False)
    cands = [s["glyphs"] for s in TR.sequences(TR.Tree(recs, seeds=True))]
    cands += [s["glyphs"] for s in TR.sequences(TR.Tree(recs, seeds=True, written=True))]
    kept = table({"S"}, False, cands, Tp)
    carried = table({"S", "W"}, True, cands, Tp)
    carried = [c for c in carried if not any(contained(c["glyphs"], k) for k in kept)]
    for s in kept:
        s["tests"] = tests(Tp, s["glyphs"], cyclic=bool(s.get("wraps")))
    cyc = sorted((c for c in Tp.cycles.values() if c["distinct"] >= 4), key=lambda c: (-len(c["families"]), -c["answers"]))
    rounds = sorted({r["round"] for r in recs if r["round"] != "seed"}, key=lambda x: (x[0] != "r", x))
    lens = collections.Counter(min(len(s["glyphs"]), 10) for s in kept)
    FA = {"claude": "cl", "gemini": "ge", "grok": "gr", "muse": "mu"}
    fa = lambda fs: " ".join(FA.get(f, f) for f in sorted(fs))
    L = ["# Best-confirmed sequences", "",
         f"*Generated by `refactored/report/best.py` after {rounds[-1]}. A read-off: nothing reads it back. Its decisions follow one standard, stated in `best.py`: for every test, each family's proportion of the predicted answer is a Beta posterior (Jeffreys), averaged over families, decided at 90% confidence with ≥ 2 families. **Choice** answers (continuations, triad middles, order lines) are *supported* when confidently ≥ {LEVEL} and *contradicted* when confidently < {LEVEL}. **Yes/no** answers (recognition, skip tests) are compared with the family's near control. A link's **agreement** is the perceptual quantity: how strongly the minds converge on it, from both reading directions, with a \"none\" counting as not naming it. A link is **confirmed** when it is supported and ≥ 2 families name it. Answers come in two channels, kept apart (METHODOLOGY §4): **shown**, and **written** (the later glyphs of a continue answer). Seed votes never confirm. The full tree is in `SEQUENCES.md`.*", "",
         f"**{len(kept)} confirmed stretches of 3+ glyphs** (by length: " + ", ".join(f"{k if k < 10 else '10+'}: {lens[k]}" for k in sorted(lens)) + f"); **{len(cyc)} manifested cycles**; **{len(carried)} runs carried by written answers** awaiting shown confirmation.", ""]
    if cyc:
        L += ["## Cycles", "", "| cycle | n | ans | fam |", "|---|---|---|---|"]
        L += [f"| `{' '.join(c['pattern'])} ↻` | {len(c['pattern'])} | {c['answers']} | {fa(c['families'])} |" for c in cyc[:40]]
        L += ["", "*Manifested: a mind wrote the whole period twice, after being shown less than one period. **n**: glyphs in the period. **ans**: answers that manifested it. **fam**: families (cl = Claude, ge = Gemini, gr = Grok).*", ""]
    L += ["## Stretches", "", "| # | stretch | n | us | agr | ≥ | fam | unr | tests |", "|---|---|---|---|---|---|---|---|---|"]
    for i, s in enumerate(kept[:TOP], 1):
        k, n = s["unreasoned"]
        t = s["tests"]
        detail = " ".join(f"{kind[0]}{p}/{c}" for kind, (p, c) in t.items() if p + c)
        tcell = (("⚠ " if any(c for _, c in t.values()) else "") + detail) if detail else "–"
        us = sum(len(c.encode("utf-8")) for c in s["glyphs"]) / len(s["glyphs"])
        L.append(f"| {i} | `{' '.join(shown_order(s['glyphs']))}`{' ↻' if s.get('wraps') else ''} | {len(s['glyphs'])} | {us:.1f} | {s['agreement']:.2f} | {s['lb']:.2f} | {s['families_min']} | {f'{k}/{n}' if n else '–'} | {tcell} |")
    if len(kept) > TOP:
        L += ["", f"*{len(kept) - TOP} shorter stretches not shown.*"]
    L += ["", "*Key:*",
          "- **n**: glyphs.",
          "- **us**: Unicode size, the mean UTF-8 bytes per glyph in the stretch (1 = ASCII … 4 = astral planes).",
          "- **agr**: observed agreement, the mean over the stretch's links.",
          f"- **≥**: the weakest link's 90% lower bound (every link is ≥ {LEVEL}).",
          "- **fam**: families naming the link, the fewest over the links.",
          "- **unr**: *unreasoned*, the answers given with 0 thinking tokens that name the links, out of all such answers at those contexts. A slice of the confirming answers, not independent evidence; it shows recognition rather than working-out (METHODOLOGY §4). **–**: none yet.",
          "- **tests**: passed/challenged, by kind. A ⚠ marks at least one challenge; **–** means untested so far.",
          "  - **s**: skip tests. Does the glyph *after next* come directly after the run? A sequence predicts no. *Passed* means no beyond the near control; *challenged* means yes beyond it: order without adjacency, or a chart walk.",
          "  - **t**: triads. Each triple's middle, from both eras. Supported or contradicted.",
          "  - **o**: order answers. Shown sets within the stretch, lines in its order (triad era). Supported or contradicted.",
          "  - Lengthening tests need no column: a longer context that flips already breaks the link.",
          "- **↻**: the run wraps. Its rotations are all confirmed, so it is a cycle confirmed link by link; not the same as manifested.",
          "- Display: a run monotonic in numeric value (or else in code points) is shown ascending.", ""]
    L += ["## Carried by written answers (awaiting shown confirmation)", "", "| # | run | n | W/S | agr | ≥ | fam |", "|---|---|---|---|---|---|---|"]
    for i, s in enumerate(carried[:TOP_WRITTEN], 1):
        L.append(f"| {i} | `{' '.join(shown_order(s['glyphs']))}`{' ↻' if s.get('wraps') else ''} | {len(s['glyphs'])} | {s['written_links']}/{s['shown_links']} | {s['agreement']:.2f} | {s['lb']:.2f} | {s['families_min']} |")
    if len(carried) > TOP_WRITTEN:
        L += ["", f"*{len(carried) - TOP_WRITTEN} shorter runs not shown.*"]
    L += ["", "*Runs in which some links are carried only by **written** answers: the minds' own generation, not yet confirmed when shown. A link is judged on written answers only where neither reading direction has shown answers. Long runs here are often code-chart walks. The planner asks such contexts shown, and puts written continuations past shown ends to recognition. **W/S**: links carried by written answers / confirmed by shown answers. Other columns as above.*", ""]
    rec = Tp.recognition_evidence()
    if rec:
        fams = sorted(Tp.inhibit_rate)
        L += ["## Recognition, and its controls", "", "| family | real | near | far |", "|---|---|---|---|"]
        for f in fams:
            cells = []
            for cls in ("real", "near", "far"):
                y, n = Tp.control_counts(f, cls)
                cells.append(f"{y / n:.2f} ({n})" if n else "—")
            L.append(f"| {f} | " + " | ".join(cells) + " |")
        for r in rec:
            r["verdict"] = yesno(r["counts"], Tp)
        good = [r for r in rec if r["verdict"] == "beyond"]
        L += ["", "*Yes-rates (n), per family. Recognition (inhibit) questions ask whether a candidate comes directly after a shown run: yes / no / can't tell. **real**: the candidates, from reasoned answers and from written answers that run past where shown answers end. **near** / **far**: matched controls, decoys at the same context, shuffled onto the same sheets. Near decoys come from the same neighbourhood of the code chart, not adjacent; far ones from a distant part of Unicode. Controls began in c007.*", "",
              f"**{len(good)} of {len(rec)} candidates recognised**: yes beyond the near control, at 90% confidence, from ≥ 2 families.", "",
              "| context | cand. | rec. | yes/n per family |", "|---|---|---|---|"]
        for r in sorted(rec, key=lambda r: (r["verdict"] != "beyond", r["x"]))[:80]:
            v = "; ".join(f"{FA.get(f, f)} {y}/{n}" for f, (y, n) in sorted(r["counts"].items()))
            L.append(f"| `{' '.join(r['ctx'])}` | `{r['x']}` | {'yes' if r['verdict'] == 'beyond' else ('no' if r['verdict'] == 'below' else '–')} | {v} |")
        L += ["", "*Per family: yes answers / all answers. **rec.**: yes = recognised; no = rejected beyond the control; – = undecided.*"]
    (ROOT / "BEST.md").write_text("\n".join(L) + "\n")
    print("\n".join(L[:6]))

if __name__ == "__main__":
    main()
