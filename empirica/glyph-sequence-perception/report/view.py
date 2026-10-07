#!/usr/bin/env python3
"""A read-off (concern 5): the catalog's default view (CATALOG §11), written to CATALOG-VIEW.md beside BEST.md.

It reads the catalog as loaded into Postgres (schema `catalog`, the latest build) and renders §11's groups as the
build computed them (`catalog/build.py`: view_group, route_state). It decides nothing of its own: every verdict on the
page is the catalog's, except the BEST column, which is BEST's own verdict (report/best.py: wholes), set beside it so
the two standards can be compared run by run. Nothing reads CATALOG-VIEW.md back, so it cannot steer probing.

Why beside BEST and not instead of it (2026-10-06, Joseph: "How close are we to a refactored version of 'best' that
is based on the true and principled catalog?"): the view's limits are computed and printed at the top -- the name
route is unmeasured on every record, so groups 1, 2 and 5 cannot be reached; "recognised" in this build is R alone,
where §11 says R, O or L; R's combination rule is under review. BEST becomes this view once those are settled.

Usage: python3 report/view.py   (needs psql-18 and the database empirica_glyph_sequence)
"""
import collections, json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "tree")); sys.path.insert(0, str(ROOT / "report"))
import tree as TR                                           # noqa: E402
import best as BE                                           # noqa: E402

DB = "empirica_glyph_sequence"
GROUPS = ["1 intuitive", "2 independent where measurable", "3 leaning", "4 chart or branch", "5 undiscriminable", "6 undecided"]
GROUP_TEXT = {
    "1 intuitive": "both routes positive",
    "2 independent where measurable": "one route positive, the other undiscriminable",
    "3 leaning": "a route negative or mixed",
    "4 chart or branch": "a route \"chart or branch\" (the alternative the route offered was preferred, and it is also felt), none negative or mixed",
    "5 undiscriminable": "both routes undiscriminable",
    "6 undecided": "everything else: a route undecided or unmeasured, none negative, mixed or \"chart or branch\"",
}

def q(sql):
    """-> rows of one JSON column, via psql-18"""
    r = subprocess.run(["psql-18", "-d", DB, "-Atq", "-c", sql], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"view.py: psql-18 failed: {r.stderr.strip()}")
    return [json.loads(l) for l in r.stdout.splitlines() if l.strip()]

def key(g):
    g = list(g)
    return tuple(min(g, g[::-1]))

def code(s):
    """a run as an inline code span inside a table cell: pipes escaped, a backtick-safe fence"""
    s = s.replace("|", "\\|")
    fence = "``" if "`" in s else "`"
    pad = " " if s.startswith("`") or s.endswith("`") else ""
    return f"{fence}{pad}{s}{pad}{fence}"

def num(x, f="{:+.2f}"):
    return "–" if x is None else f.format(x)

def bf(x):
    if x is None:
        return "–"
    return f"{x:.3g}" if x < 1e4 else "≥1e4"

def fams(rf):
    if not rf:
        return "–"
    return " ".join(f"{BE.FA.get(f, f)} {v.get('yes', '?')}/{v.get('n', '?')}" for f, v in sorted(rf.items()))

def splits(cs):
    cs = cs or []
    firm = sum(1 for s in cs if (s.get("certainty") or 0) >= 0.9)
    return f"{len(cs)} ({firm} firm)" if cs else "–"

def main():
    man = q("select doc from catalog.manifest")
    man = man[0] if man else {}
    rows = q("select row_to_json(r) from (select glyphs, length, chart_class, sources, r_strength, r_sd, r_bf, r_families, "
             "recognised, chart_state, name_state, view, contested, contested_asked, weakest_link, o_strength, o_bf, "
             "content_splits, given_kind, given_walk from catalog.records) r")
    bfc = man.get("params", {}).get("BF_CERTAIN", 10.0)

    # BEST's verdicts on the same answers as they stand now (the catalog's build may be a round older: see the header)
    recs = TR.load()
    Tp = TR.Tree(recs, seeds=False)
    whole = BE.wholes(Tp)

    cat = {key(r["glyphs"]): r for r in rows}
    asked = {k: r for k, r in cat.items() if "asked whole" in (r.get("sources") or [])}
    groups = collections.defaultdict(list)
    given_rec = [r for r in rows if r["recognised"] and r["given_walk"]]
    for r in rows:
        if r["recognised"] and not r["given_walk"]:       # given walks are on CATALOG-GIVEN.md (Joseph, 2026-10-06)
            groups[r["view"]].append(r)
    n_rec = sum(len(v) for v in groups.values())
    name_states = collections.Counter(r["name_state"] for r in rows)
    o_only = sum(1 for r in rows if not r["recognised"] and (r["o_bf"] or 0) >= bfc and (r["o_strength"] or 0) > 0)

    # reconciliation, over runs asked whole
    best_rec = {k for k, w in whole.items() if w["verdict"] == "beyond"}
    cat_rec = {k for k, r in asked.items() if r["recognised"]}
    both = best_rec & cat_rec
    best_only = best_rec - cat_rec
    cat_only = cat_rec - best_rec
    not_in_cat = {k for k in best_rec if k not in asked}

    def why_best_only(k):
        r = asked.get(k)
        if r is None:
            return "not a catalog record asked whole"
        if r["r_bf"] is None:
            return "catalog has no R (no rater with controls)"
        if (r["r_strength"] or 0) <= 0:
            return "catalog strength ≤ 0"
        if r["r_bf"] < 3:
            return "catalog BF < 3"
        return f"catalog BF 3–{bfc:g}"
    reasons = collections.Counter(why_best_only(k) for k in best_only)
    def why_cat_only(k):
        w = whole.get(k)
        if w is None:
            return "BEST has no whole-run entry"
        return "BEST rejects" if w["verdict"] == "below" else "BEST undecided"
    reasons_c = collections.Counter(why_cat_only(k) for k in cat_only)

    L = ["# The catalog's default view", "",
         f"*Generated by `report/view.py` from the catalog in Postgres: build `{man.get('build', '?')}`, model `{man.get('model', '?')}`, finished {man.get('finished', '?')}, {man.get('counts', {}).get('answers', '?')} answers, sealed answers dropped {man.get('sealed_dropped', '?')}. A read-off: nothing reads it back. This is CATALOG §11's default view, the groups as the catalog's build computed them. It stands **beside** `BEST.md` and doesn't replace it yet, for the reasons under *Where the view stands*. The BEST column is BEST's own verdict on the answers as they stood when this page was written, which may be a round newer than the build.*", "",
         "## Where the view stands", "",
         f"**{n_rec} runs recognised** by the catalog (R, whole-run recognition beyond shuffled controls, Bayes factor ≥ {bfc:g} with positive strength) that aren't walks over a given, of {len(rows)} records. Another **{len(given_rec)}** recognised runs walk a given (an alphabet or a number line in one dress: windows, rotations, strides…); they are on `CATALOG-GIVEN.md` (Joseph: *\"we'll focus on probing things that aren't given, and focus CATALOG-VIEW.md on things that aren't given\"*).", "",
         "| group | meaning | runs |", "|---|---|---|"]
    for g in GROUPS:
        L.append(f"| {g} | {GROUP_TEXT[g]} | {len(groups.get(g, []))} |")
    L += ["",
          "**What limits it now** (each computed from this build):", "",
          f"- **The name route is not measured.** Name route states on all {len(rows)} records: " + ", ".join(f"{s} {n}" for s, n in name_states.most_common()) + ". The build holds it at \"unmeasured\" until the name-only question is validated (CATALOG §7a), so groups 1, 2 and 5 cannot be reached, and nearly every recognised run lands in group 6. This is the main thing between this view and a useful one.",
          f"- **\"Recognised\" is R alone.** §11 says R, O or L beyond its contrast. Counting O as built would add {o_only} records not recognised by R. That is about {o_only / max(n_rec, 1):.0f} times R's count, large enough that O's certainty needs checking before it can recognise anything (it is agreement of triad and order answers against chance, the build's stand-in for Plackett–Luce). L isn't counted either.",
          "- **R's combination rule is under review.** In the family-disagreement spike, a logit model with a criterion and a slope per mind, controls treated as items, beat this build's Abbott model on held-out cohere answers. Two independent verifications reproduced that comparison (`spikes/family-disagreement-2026-10-06/de-novo-feedback-2.md`); the second found the model still lacks a mind × item term, so it isn't in the catalog yet.", "",
          "## Beside BEST", "",
          f"Both decide the same thing, a run asked whole, by different standards. BEST: per family, the yes rate against the family's shuffled rate, families averaged with equal weight, 90% one-sided. The catalog: per rater against its controls by chart class (Abbott), families weighted by their discrimination, Bayes factor ≥ {bfc:g}.", "",
          "| | runs |", "|---|---|",
          f"| asked whole (catalog records) | {len(asked)} |",
          f"| asked whole (BEST) | {len(whole)} |",
          f"| recognised by both | {len(both)} |",
          f"| by BEST only | {len(best_only)} |",
          f"| by the catalog only | {len(cat_only)} |", ""]
    if best_only:
        L += ["*BEST only, by the catalog's reading:* " + "; ".join(f"{r} {n}" for r, n in reasons.most_common()) + ".", ""]
    if cat_only:
        L += ["*Catalog only, by BEST's reading:* " + "; ".join(f"{r} {n}" for r, n in reasons_c.most_common()) + ".", ""]
    L += ["## The groups", "",
          "*Each group ordered by length, then by R's 90% lower bound (strength − 1.28 sd). **bytes**: the mean UTF-8 length of the run's glyphs (1 = ASCII … 4 = astral planes; BEST's *us*). **R**: the catalog's strength on the identified scale (the excess yes rate beyond the controls), ± sd. **BF**: its Bayes factor. **yes/n**: per family. **chart**: the chart route's state; contested positions asked / contested. **weakest**: the weakest link state on the run (CATALOG §8: 1 evidence at the link's full context; 2 stable at a suffix; 3 at a suffix only, lengthening untested; 4 picks beyond 8 glyphs; 5 none). **splits**: links where families' most named continuations differ (firm: certainty ≥ 0.9). **O**: order agreement's strength and Bayes factor (not used for recognition in this build). **BEST**: BEST's verdict on the same run.*", ""]
    for g in GROUPS:
        rs = groups.get(g, [])
        L += [f"### {g} ({len(rs)})", ""]
        if not rs:
            L += ["*None in this build.*", ""]
            continue
        rs.sort(key=lambda r: (-r["length"], -((r["r_strength"] or 0) - 1.2816 * (r["r_sd"] or 0)), r["glyphs"]))
        L += ["| # | run | n | bytes | class | R | BF | yes/n | chart | weakest | splits | O | BEST |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for i, r in enumerate(rs, 1):
            w = whole.get(key(r["glyphs"]))
            bv = {"beyond": "recognised", "below": "rejected", None: "undecided"}[w["verdict"]] if w else "–"
            ca = f"{r['chart_state']} {r['contested_asked']}/{r['contested']}" if r["contested"] else r["chart_state"]
            o = f"{num(r['o_strength'])} ({bf(r['o_bf'])})" if r["o_strength"] is not None else "–"
            L.append(f"| {i} | {code(''.join(BE.shown_order(list(r['glyphs']))))} | {r['length']} | {BE.us(r['glyphs']):.1f} | {r['chart_class']} | "
                     f"{num(r['r_strength'])} ± {num(r['r_sd'], '{:.2f}')} | {bf(r['r_bf'])} | {fams(r['r_families'])} | {ca} | "
                     f"{r['weakest_link'] if r['weakest_link'] is not None else '–'} | {splits(r['content_splits'])} | {o} | {bv} |")
        L.append("")
    (ROOT / "CATALOG-VIEW.md").write_text("\n".join(L) + "\n")
    print(f"CATALOG-VIEW.md: {n_rec} recognised; " + ", ".join(f"{g.split(' ', 1)[1]} {len(groups.get(g, []))}" for g in GROUPS)
          + f"; beside BEST: both {len(both)}, BEST only {len(best_only)}, catalog only {len(cat_only)}")

if __name__ == "__main__":
    main()
