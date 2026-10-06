#!/usr/bin/env python3
"""A read-off (concern 5): the best-confirmed stretches of sequence in the tree right now. It reads the tree and writes
BEST.md; nothing reads BEST.md back (the planner never sees it), so its definition of "best" cannot steer probing, the
tree, priority or the port. Its criteria are its own, stated here; they are not the walk's (the planner's view).

Two channels of answers, never pooled (METHODOLOGY §4):
  SHOWN    answers to contexts a mind was shown (the first glyph of a continue answer, a what-comes-next proposal).
  WRITTEN  the later glyphs of a continue answer: the mind's continuation at a context it wrote itself.
Seed votes help find candidates but never confirm a link.

A link a-b of a candidate run, read in either direction (a sequence and its reverse are one sequence, METHODOLOGY §2):
  SHOWN-CONFIRMED  one estimate from both reading directions: in each, the longest shown context ending at the earlier
                   glyph (within the run) gives the later glyph's agreement; the link's agreement is the MEAN over the
                   directions (families pooled), >= THETA from >= 2 families. A direction whose top answer is "none"
                   is the end of that reading and is left out; one naming a different glyph counts against (e.g.
                   `㉏ ㉐ -> ㉑` forward, but `㉕ ... ㉑ -> ⑳` backward). The mean, not the better of the two, so
                   that asking a link from its other side (as the planner's join probes do) is a test, not a
                   second chance.
  WRITTEN-CARRIED  a link with no shown estimate, the same way on written answers whose context is a suffix of the
                   run before the link (the minds' own preceding glyphs agreeing with the run), unless a shown answer
                   contradicts it ("none" -- momentum past a felt end -- or a different glyph).
Tables:
  Stretches: maximal runs of shown-confirmed links, >= 3 glyphs. The best-confirmed sequences.
  Carried by written answers: maximal runs of shown-confirmed or written-carried links holding at least one
                   written-carried link, >= 3 glyphs. Generation by the minds awaiting confirmation when shown
                   (the planner asks such contexts shown, and puts momentum past ends to recognition).
Rotations of one run, all confirmed, are listed once and marked as wrapping: a cycle confirmed link by link (distinct
from a manifested cycle, which a mind wrote round twice). Candidates are walks of the tree with seed votes, and of the tree with written answers pooled in; overlapping runs
are merged and their links judged again on the merged run (a link's context depends on the run before it).
Ranked by length, then mean agreement. Display only: a run monotonic in numeric value (or else in code points) is shown ascending. THETA = 0.75 is a read-off cut chosen without evidence; it gates nothing.
"""
import collections, pathlib, sys, unicodedata

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "tree"))
import tree as TR                                           # noqa: E402

THETA = 0.75
TOP = 150
TOP_WRITTEN = 100

def shown_top(Tp, run):
    """-> (deciding shown context, its ranked list) for what follows `run`, or (None, [])"""
    ctx = Tp.lookup(run) if len(run) >= 2 else None
    return (ctx, Tp.ranked(ctx)) if ctx else (None, [])

def contradicts(Tp, run, x, none_counts):
    """does the shown deciding context after `run` name something other than x? ("none" only if none_counts)"""
    _, rk = shown_top(Tp, run)
    if not rk:
        return False
    top = rk[0][0]
    if top == x:
        return False
    if top == TR.NONE:
        return none_counts
    return top != TR.OTHER

def shown_dir(Tp, run, x):
    """one reading direction of a link, on shown answers: at the deciding context, x's agreement (mean over families of
    each family's share naming x), the families naming x, unreasoned (k, n), and the top answer -> dict or None"""
    if len(run) < 2:
        return None
    ctx, rk = shown_top(Tp, run)
    if not rk:
        return None
    fams = {f for f, xs in Tp.nodes[ctx].items() if x in xs}
    u = Tp.unreasoned.get(ctx, [])
    return {"agr": Tp.dist(ctx).get(x, (0.0, 0, 0))[0], "fams": fams, "top": rk[0][0],
            "uk": sum(1 for f in u if f == x), "un": len(u)}

def written_dir(Tp, run, x):
    """one reading direction, on written answers whose context is a suffix of run -> dict or None"""
    if len(run) < 2:
        return None
    per = collections.defaultdict(list)
    for j in range(2, min(TR.MAXK, len(run)) + 1):
        for f, xs in Tp.written.get(tuple(run[-j:]), {}).items():
            per[f] += xs
    if not per:
        return None
    shares = {f: sum(1 for y in xs if y == x) / len(xs) for f, xs in per.items()}
    return {"agr": sum(shares.values()) / len(shares), "fams": {f for f, v in shares.items() if v > 0}}

def judge(g, Tp):
    """-> per link i (g[i]-g[i+1]): ("S", agr, fam, uk, un) | ("W", agr, fam, 0, 0) | None.
    ONE estimate per link from both reading directions (a sequence and its reverse are one sequence): the mean of the
    directions' agreements, families pooled -- not the better of the two, which gave a link asked from both sides a
    second chance (and the planner's join probes ask weak links from the other side). A direction whose deciding
    context's top answer is "none" is the end of that reading and is left out; one naming a different glyph counts
    against. Shown first; a link without a shown estimate may be carried by written answers, the same way, unless a
    shown answer contradicts it (in the same direction: "none" -- momentum past a felt end -- or a different glyph)."""
    out = []
    for i in range(len(g) - 1):
        a, b = g[i], g[i + 1]
        fwd, bwd = g[:i + 1], g[i + 1:][::-1]              # run before b (forward); run before a (backward)
        ds = [d for d in (shown_dir(Tp, fwd, b), shown_dir(Tp, bwd, a)) if d and d["top"] not in (TR.NONE, TR.OTHER)]
        st = None
        if ds:
            agr = sum(d["agr"] for d in ds) / len(ds)
            fams = set().union(*(d["fams"] for d in ds))
            if agr >= THETA and len(fams) >= 2:
                st = ("S", agr, len(fams), sum(d["uk"] for d in ds), sum(d["un"] for d in ds))
        elif not any(contradicts(Tp, run, x, none_counts=True) for run, x in ((fwd, b), (bwd, a))):
            ws = [w for w in (written_dir(Tp, fwd, b), written_dir(Tp, bwd, a)) if w]
            if ws:
                agr = sum(w["agr"] for w in ws) / len(ws)
                fams = set().union(*(w["fams"] for w in ws))
                if agr >= THETA and len(fams) >= 2:
                    st = ("W", agr, len(fams), 0, 0)
        out.append(st)
    return out

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
                        "families_min": min(l[2] for l in ls),
                        "written_links": sum(1 for l in ls if l[0] == "W"), "shown_links": sum(1 for l in ls if l[0] == "S"),
                        "unreasoned": (sum(l[3] for l in ls if l[0] == "S"), sum(l[4] for l in ls if l[0] == "S"))})
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
            if key not in found or st["agreement"] > found[key]["agreement"]:
                found[key] = st
    return list(found.values())

def dedupe(items):
    """one entry per run (either orientation, the better-agreed kept); runs contained in a longer one are that one"""
    best = {}
    for s in items:
        key = tuple(min(s["glyphs"], s["glyphs"][::-1]))
        if key not in best or s["agreement"] > best[key]["agreement"]:
            best[key] = s
    # rotations of one run (either direction) can all be confirmed only if the closing link is too: one entry, marked
    # as wrapping -- a cycle confirmed link by link, which is not the same as a manifested one (written round twice)
    rot = collections.defaultdict(list)
    for key, s in best.items():
        if len(set(s["glyphs"])) == len(s["glyphs"]):
            rot[TR.canon_cycle(list(s["glyphs"]))].append(key)
    for ck, keys in rot.items():
        if len(keys) > 1:
            keep = max(keys, key=lambda k: best[k]["agreement"])
            best[keep]["wraps"] = True
            for k in keys:
                if k != keep:
                    best.pop(k)
    kept = []
    for s in sorted(best.values(), key=lambda s: (-len(s["glyphs"]), -s["agreement"])):
        g, n = s["glyphs"], len(s["glyphs"])
        if not any(n < len(k["glyphs"]) and any(k["glyphs"][i:i + n] in (g, g[::-1]) for i in range(len(k["glyphs"]) - n + 1)) for k in kept):
            kept.append(s)
    kept.sort(key=lambda s: (-len(s["glyphs"]), -s["agreement"], s["glyphs"]))
    return kept

def table(allowed, need_w, cands, Tp):
    first = collect(cands, Tp, allowed, need_w)
    merged = merge([s["glyphs"] for s in first])               # overlapping windows -> one run, judged again
    return dedupe(first + collect(merged, Tp, allowed, need_w))

def shown_order(g):
    """presentation only (a sequence and its reverse are one sequence): a run strictly monotonic in Unicode numeric value
    (every glyph having one) is shown ascending by value -- digits split across blocks, like `¹ ² ³` (Latin-1) beside
    `⁰ ⁴ … ⁹` (U+2070-2079), are not monotonic in code points -- otherwise a run monotonic in code points is shown
    ascending (Joseph, 2026-10-05); any other run keeps the orientation it was found in"""
    vals = [unicodedata.numeric(c, None) for c in g]
    keys = vals if all(v is not None for v in vals) else [ord(c) for c in g]
    if all(b < a for a, b in zip(keys, keys[1:])):
        return g[::-1]
    return g

def recognition(recs):
    """Recognition (inhibit) answers against their controls. Per family: the share of "yes" among answers to real
    candidates, to near controls and to far controls. A candidate counts as RECOGNISED when, in >= 2 families, its yes
    share is above that family's near-control yes rate (the stricter control; far where no near rate exists yet)."""
    inh = [r for r in recs if r.get("kind") == "inhibit" and r.get("outcome") in ("yes", "no", "cant-tell")]
    rate = collections.defaultdict(lambda: collections.Counter())
    for r in inh:
        rate[(r["family"], (r.get("tags") or {}).get("control") or "real")][r["outcome"]] += 1
    def yes(f, cls):
        c = rate.get((f, cls))
        return (c["yes"] / sum(c.values()), sum(c.values())) if c else (None, 0)
    fams = sorted({r["family"] for r in inh})
    per = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
    for r in inh:
        if not (r.get("tags") or {}).get("control"):
            per[(tuple(r["context"]), r["candidate"])][r["family"]][r["outcome"]] += 1
    rec = []
    for (ctx, x), fc in per.items():
        above = []
        for f, c in fc.items():
            base = yes(f, "near")[0] if yes(f, "near")[0] is not None else yes(f, "far")[0]
            share = c["yes"] / sum(c.values())
            if base is not None and share > base:
                above.append(f)
        rec.append({"ctx": ctx, "x": x, "verdicts": {f: dict(c) for f, c in fc.items()}, "above": above})
    return fams, yes, rec

def main():
    recs = TR.load()
    Tp = TR.Tree(recs, seeds=False)                            # shown answers (nodes) + written answers (written)
    cands = [s["glyphs"] for s in TR.sequences(TR.Tree(recs, seeds=True))]
    cands += [s["glyphs"] for s in TR.sequences(TR.Tree(recs, seeds=True, written=True))]
    kept = table({"S"}, False, cands, Tp)
    carried = table({"S", "W"}, True, cands, Tp)
    def covered(g):                                            # already a confirmed stretch (or one of its rotations)
        for k in kept:
            kg = k["glyphs"]
            if TR.canon_cycle(list(g)) == TR.canon_cycle(list(kg)) and k.get("wraps"):
                return True
            n = len(g)
            if n <= len(kg) and any(kg[i:i + n] in (g, g[::-1]) for i in range(len(kg) - n + 1)):
                return True
        return False
    carried = [c for c in carried if not covered(c["glyphs"])]
    cyc = sorted((c for c in Tp.cycles.values() if c["distinct"] >= 4), key=lambda c: (-len(c["families"]), -c["answers"]))
    rounds = sorted({r["round"] for r in recs if r["round"] != "seed"}, key=lambda x: (x[0] != "r", x))
    lens = collections.Counter(min(len(s["glyphs"]), 10) for s in kept)
    L = ["# Best-confirmed sequences", "",
         f"*Generated by `refactored/report/best.py` after {rounds[-1]}. This is a read-off: nothing reads it back, so it never steers what is asked. Its criteria are its own (stated in `best.py`), not the walk's. Two channels of answers are kept apart (METHODOLOGY §4): **shown**, a mind's answer to a context it was shown; and **written**, the later glyphs of a continue answer, the mind's continuation at a context it wrote itself. A **stretch** is a run in which every link was confirmed by shown answers, reading in either direction: the longest shown context names the next glyph as its most-agreed continuation, with agreement ≥ {THETA} from ≥ 2 LLM families; and the other direction doesn't name a *different* glyph (that would make it a branch). Seed votes help find candidates but never confirm a link. The full tree, with branches and open ends, is in `SEQUENCES.md`.*", "",
         f"**{len(kept)} confirmed stretches of 3+ glyphs** (by length: " + ", ".join(f"{k if k < 10 else '10+'}: {lens[k]}" for k in sorted(lens)) + f"); **{len(cyc)} manifested cycles**; **{len(carried)} runs carried by written answers** awaiting shown confirmation.", ""]
    if cyc:
        L += ["## Cycles (manifested: a mind wrote the whole period twice)", "", "| cycle | glyphs | answers | families |", "|---|---|---|---|"]
        L += [f"| `{' '.join(c['pattern'])} ↻` | {len(c['pattern'])} | {c['answers']} | {', '.join(sorted(c['families']))} |" for c in cyc[:40]]
        L.append("")
    L += ["## Stretches", "",
          "**Unreasoned** counts, over the stretch's links at their deciding contexts, the answers given with 0 thinking tokens (measured per answer: Gemini Flash, Haiku with thinking off, Sonnet when its adaptive thinking is 0) that name the link, out of all such answers there. It shows how far a link is *recognised* rather than worked out (METHODOLOGY §4). It confirms nothing, and it is a slice of the same answers that confirm the link, not independent evidence. *(none)*: no unreasoned answers at those contexts yet.", "",
          "| # | stretch | glyphs | mean agreement | families (min over links) | unreasoned |", "|---|---|---|---|---|---|"]
    for i, s in enumerate(kept[:TOP], 1):
        k, n = s["unreasoned"]
        L.append(f"| {i} | `{' '.join(shown_order(s['glyphs']))}`{' ↻ (wraps)' if s.get('wraps') else ''} | {len(s['glyphs'])} | {s['agreement']:.2f} | {s['families_min']} | {f'{k}/{n}' if n else '(none)'} |")
    if len(kept) > TOP:
        L += ["", f"*{len(kept) - TOP} shorter stretches not shown.*"]
    L += ["", "## Carried by written answers (awaiting shown confirmation)", "",
          f"Runs in which some links are carried only by **written** answers. In the stated direction, all written answers whose context matches the run before the link name the next glyph, with agreement ≥ {THETA} from ≥ 2 families, and no shown answer contradicts it. In particular, a shown \"none\" at that point (momentum past a felt end) excludes the link. These are the minds' own generation, not yet confirmed when shown. Long runs here are often code-chart walks: a mind carrying on through a block in code-point order. The planner asks such contexts shown, and puts written continuations past shown ends to recognition.", "",
          "| # | run | glyphs | written links / shown links | mean agreement | families (min over links) |", "|---|---|---|---|---|---|"]
    for i, s in enumerate(carried[:TOP_WRITTEN], 1):
        L.append(f"| {i} | `{' '.join(shown_order(s['glyphs']))}`{' ↻ (wraps)' if s.get('wraps') else ''} | {len(s['glyphs'])} | {s['written_links']} / {s['shown_links']} | {s['agreement']:.2f} | {s['families_min']} |")
    if len(carried) > TOP_WRITTEN:
        L += ["", f"*{len(carried) - TOP_WRITTEN} shorter runs not shown.*"]
    fams, yes, rec = recognition(recs)
    if rec:
        L += ["", "## Recognition, and its controls", "",
              "Recognition (inhibit) questions ask whether a candidate comes directly after a shown run: *yes / no / can't tell*. The candidates come from reasoned answers, and from written answers that run past where shown answers end. Each one has a matched **control** at the same context, shuffled onto the same sheets: a **near** decoy, from the same neighbourhood of the code chart but not adjacent, or a **far** one, from a distant part of Unicode. Control yes-rates show how readily a family says yes. A candidate is **recognised** when its yes share beats the family's near-control rate in ≥ 2 families. Controls began in c007; until a family has a control rate, nothing of its counts as recognised.", "",
              "| family | yes: real candidates | yes: near controls | yes: far controls |", "|---|---|---|---|"]
        for f in fams:
            cells = []
            for cls in ("real", "near", "far"):
                v, n = yes(f, cls)
                cells.append(f"{v:.2f} (n={n})" if v is not None else "—")
            L.append(f"| {f} | " + " | ".join(cells) + " |")
        good = [r for r in rec if len(r["above"]) >= 2]
        L += ["", f"**{len(good)} of {len(rec)} candidates recognised.**", "",
              "| context | candidate | recognised | verdicts per family (yes / no / can't tell) |", "|---|---|---|---|"]
        for r in sorted(rec, key=lambda r: (-len(r["above"]), r["x"]))[:80]:
            v = "; ".join(f"{f} {c.get('yes', 0)}/{c.get('no', 0)}/{c.get('cant-tell', 0)}" for f, c in sorted(r["verdicts"].items()))
            L.append(f"| `{' '.join(r['ctx'])}` | `{r['x']}` | {'yes' if len(r['above']) >= 2 else 'not yet'} | {v} |")
    (ROOT / "BEST.md").write_text("\n".join(L) + "\n")
    print("\n".join(L[:6]))

if __name__ == "__main__":
    main()
