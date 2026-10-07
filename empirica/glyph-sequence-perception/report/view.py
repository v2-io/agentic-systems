#!/usr/bin/env python3
"""A read-off (concern 5): perceived orders, the catalog's view, written to CATALOG-VIEW.md beside BEST.md.

Since 2026-10-06 (catalog build 6) it leads with the runs whose ORDER the minds are shown to perceive: recognised by the
catalog, beyond their own shuffled glyphs (the paired contrast), with no relation to a given, and with no code-point
order (monotone, rotated or interleaved) that the encoding could supply. Every other recognised run follows, by reason.
Joseph: "It's become very difficult to find any interesting / meaningful sequences"; "so many of these are basically
just snippets of the unicode spec". The earlier design below is kept as history.

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

def pair_cell(pr):
    if not pr:
        return "–"
    return f"{pr['own'][0]}/{pr['own'][1]} vs {pr['shuffles'][0]}/{pr['shuffles'][1]}"

def reason(r):
    """why a recognised run is not on the perceived list (the first that applies), or None"""
    if r["given_kind"]:
        return "given"
    if r["code_order"] and r["code_order"] != "none":
        return "encoded:" + r["code_order"]
    if not r["paired"]:
        return "shuffles never asked"
    if r["paired"]["lb"] <= 0:
        return "not beyond its own shuffles"
    return None

REASONS = [("given", "Related to a given", "an alphabet or number line in some dress, or one glyph across dresses (single-dress given walks are on `CATALOG-GIVEN.md`)"),
           ("encoded:monotone", "Order supplied by the encoding: code points monotone", "every step up, or every step down, in code points: the code chart's own order"),
           ("encoded:rotated", "Order supplied by the encoding: a rotated code-point order", "monotone after one wrap (a cycle encoded in order: clocks, zodiac, a block's end back to its start); counted from 5 glyphs"),
           ("encoded:interleaved", "Order supplied by the encoding: two code-point orders interleaved", "alternate glyphs form two monotone code-point orders in one direction (hours and half-hours, two cases of an alphabet); counted from 6 glyphs"),
           ("not beyond its own shuffles", "Not beyond its own shuffles", "the minds call the same glyphs coherent in other orders about as often: the set coheres, the order isn't shown to"),
           ("shuffles never asked", "Its own shuffles never asked", "recognised against pooled controls only")]

def table(L, rs, whole, numbered=True):
    L += ["| # | run | n | bytes | own vs its shuffles | order ≥ | R | BF | yes/n | weakest | splits | BEST |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(rs, 1):
        w = whole.get(key(r["glyphs"]))
        bv = {"beyond": "recognised", "below": "rejected", None: "undecided"}[w["verdict"]] if w else "–"
        lb = num(r["paired"]["lb"]) if r["paired"] else "–"
        L.append(f"| {i} | {code(''.join(BE.shown_order(list(r['glyphs']))))} | {r['length']} | {BE.us(r['glyphs']):.1f} | "
                 f"{pair_cell(r['paired'])} | {lb} | {num(r['r_strength'])} ± {num(r['r_sd'], '{:.2f}')} | {bf(r['r_bf'])} | "
                 f"{fams(r['r_families'])} | {r['weakest_link'] if r['weakest_link'] is not None else '–'} | {splits(r['content_splits'])} | {bv} |")
    L.append("")

def main():
    man = q("select doc from catalog.manifest")
    man = man[0] if man else {}
    rows = q("select row_to_json(r) from (select glyphs, length, chart_class, sources, r_strength, r_sd, r_bf, r_families, "
             "recognised, chart_state, name_state, view, contested, contested_asked, weakest_link, o_strength, o_bf, "
             "content_splits, given_kind, given_walk, paired, code_order from catalog.records) r")
    bfc = man.get("params", {}).get("BF_CERTAIN", 10.0)
    recs = TR.load()                                 # BEST's verdicts, on the answers as they stand now
    Tp = TR.Tree(recs, seeds=False)
    whole = BE.wholes(Tp)

    rec = [r for r in rows if r["recognised"]]
    perceived = [r for r in rec if reason(r) is None]
    perceived.sort(key=lambda r: (-r["paired"]["lb"], -r["length"], r["glyphs"]))
    by_reason = collections.defaultdict(list)
    for r in rec:
        if reason(r):
            by_reason[reason(r)].append(r)

    cat = {key(r["glyphs"]): r for r in rows}
    asked = {k: r for k, r in cat.items() if "asked whole" in (r.get("sources") or [])}
    best_rec = {k for k, w in whole.items() if w["verdict"] == "beyond"}
    cat_rec = {k for k, r in asked.items() if r["recognised"]}

    L = ["# Perceived orders: the catalog's view", "",
         f"*Generated by `report/view.py` from the catalog in Postgres: build `{man.get('build', '?')}`, model `{man.get('model', '?')}`, finished {man.get('finished', '?')}, {man.get('counts', {}).get('answers', '?')} answers, sealed answers dropped {man.get('sealed_dropped', '?')}. A read-off: nothing reads it back. The BEST column is BEST's own verdict on the answers as they stood when this page was written.*", "",
         "## What this page shows", "",
         "Runs whose **order** the minds perceive, as far as the data can tell it apart from two things that look the same in a yes/no answer (Joseph, 2026-10-06: *\"so many of these are basically just snippets of the unicode spec\"*; *\"they believe this is a meaningful sequence??\"* of `1₁𝟷𝟏𝟙⓵➊¹①⑴🯱𝟭➀１⒈𝟣❶🄂`):", "",
         "- **A set that coheres in any order.** The catalog's recognition (R) compares a run's \"yes, coherent\" rate with *pooled* control rates, so eighteen ones, or a block of related symbols, pass it in any order. Here a run must also beat **its own glyphs shuffled** (its paired controls, asked beside it): the 90% lower bound of own − shuffles above zero (**order ≥**).",
         "- **An order the encoding supplies.** A run whose code points are monotone, monotone after one wrap, or two monotone orders interleaved can be called coherent by reading the code chart, without perceiving anything. Those are listed below by kind, not here. Real orders Unicode happens to encode in order (zodiac, moon phases, clock faces) fall there too: from these answers, perceiving them can't be told apart from reading the chart.",
         "- **The givens.** A run related to an alphabet or number line, in any dress (Joseph: *\"all the different encodings of essentially the same alphabet and digits ... a whole world that we can just call 'given'\"*).", "",
         f"Of the {len(rec):,} runs the catalog recognises (R, Bayes factor ≥ {bfc:g}), **{len(perceived):,}** pass all three:", "",
         "| | runs |", "|---|---|", f"| recognised by the catalog | {len(rec):,} |"]
    for k, title, _ in REASONS:
        L.append(f"| {title.lower()} | {len(by_reason.get(k, [])):,} |")
    L += [f"| **perceived orders** | **{len(perceived):,}** |", "",
          "*Columns. **bytes**: the mean UTF-8 length of the run's glyphs (1 = ASCII … 4 = astral planes). **own vs its shuffles**: \"yes\"/answers for the run, then for its own glyphs shuffled. **order ≥**: the 90% lower bound of the difference (Jeffreys means). **R**: the catalog's recognition strength against pooled controls ± sd, and **BF** its Bayes factor. **yes/n**: per family. **weakest**: the weakest link state on the run (CATALOG §8: 1 evidence at the link's full context … 5 none). **splits**: links where families' most named continuations differ (firm: certainty ≥ 0.9). **BEST**: BEST's verdict on the same run.*", "",
          f"## Perceived orders ({len(perceived):,})", "", "*Ordered by **order ≥**, then length.*", ""]
    table(L, perceived, whole)
    L += ["## Recognised, but the order isn't shown to be perceived", ""]
    for k, title, text in REASONS:
        rs = sorted(by_reason.get(k, []), key=lambda r: (-r["length"], r["glyphs"]))
        L += [f"### {title} ({len(rs):,})", "", f"*{text[0].upper() + text[1:]}.*", ""]
        if rs:
            table(L, rs, whole)
        else:
            L += ["*None.*", ""]
    L += ["## Limits of this build", "",
          "- **Recognition is R against pooled controls, filtered here by the paired contrast.** CATALOG §9's combination rule is under review: a logit model with a criterion and slope per mind beat it on held-out cohere answers (`spikes/family-disagreement-2026-10-06/`), and isn't in the catalog yet.",
          "- **The routes.** CATALOG §11's groups (by the chart and name routes) are on every record as `view`; the name route is unmeasured on every record, so nearly all fall in \"undecided\" and the groups don't sort anything yet.",
          "- **The encoded-order rule** reads code points only. A perceived order that happens to be monotone in code points (most real orders Unicode encodes in sequence) is listed with the encoded ones; the instruments that could separate them (lookalike substitution, the name-only question) haven't decided enough runs yet.",
          f"- **Beside BEST:** of runs asked whole, BEST recognises {len(best_rec):,}, the catalog {len(cat_rec):,}, both {len(best_rec & cat_rec):,}. BEST also compares against pooled shuffles, so it carries the same set-coherence problem.", ""]
    (ROOT / "CATALOG-VIEW.md").write_text("\n".join(L) + "\n")
    print(f"CATALOG-VIEW.md: {len(rec)} recognised; perceived {len(perceived)}; " + ", ".join(f"{k} {len(by_reason.get(k, []))}" for k, _, _ in REASONS))

if __name__ == "__main__":
    main()
