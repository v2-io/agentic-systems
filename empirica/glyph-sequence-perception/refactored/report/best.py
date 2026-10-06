#!/usr/bin/env python3
"""A read-off (concern 5): the best-confirmed stretches of sequence in the tree right now. It reads the tree and writes
BEST.md; nothing reads BEST.md back (the planner never sees it), so its definition of "best" cannot steer probing, the
tree, priority or the port. Its criteria are its own, stated here; they are not the walk's (the planner's view).

Two channels of answers, never pooled (METHODOLOGY §4):
  SHOWN    answers to contexts a mind was shown (the first glyph of a continue answer, a what-comes-next proposal).
  WRITTEN  the later glyphs of a continue answer: the mind's continuation at a context it wrote itself.
Seed votes help find candidates but never confirm a link.

A link a-b of a candidate run, read in either direction (a sequence and its reverse are one sequence, METHODOLOGY §2):
  SHOWN-CONFIRMED  in one direction, the longest shown context ending at the earlier glyph (within the run) has the
                   later glyph as its most-agreed continuation, with agreement >= THETA from >= 2 families; and in the
                   other direction the longest shown context does not name a DIFFERENT glyph (that would make a-b a
                   branch, not a link: e.g. `㉏ ㉐ -> ㉑` forward, but `㉕ ... ㉑ -> ⑳` backward).
  WRITTEN-CARRIED  not shown-confirmed; in one direction, the written answers at every context that is a suffix of the
                   run before the link (the minds' own preceding glyphs agreeing with the run) name the later glyph
                   with agreement >= THETA, from >= 2 families; and no shown answer contradicts it: not the shown
                   context in that direction (a different glyph, or "none" -- momentum past a felt end), nor a
                   different glyph in the other direction.
Tables:
  Stretches: maximal runs of shown-confirmed links, >= 3 glyphs. The best-confirmed sequences.
  Carried by written answers: maximal runs of shown-confirmed or written-carried links holding at least one
                   written-carried link, >= 3 glyphs. Generation by the minds awaiting confirmation when shown
                   (the planner asks such contexts shown, and puts momentum past ends to recognition).
Rotations of one run, all confirmed, are listed once and marked as wrapping: a cycle confirmed link by link (distinct
from a manifested cycle, which a mind wrote round twice). Candidates are walks of the tree with seed votes, and of the tree with written answers pooled in; overlapping runs
are merged and their links judged again on the merged run (a link's context depends on the run before it).
Ranked by length, then mean agreement. THETA = 0.75 is a read-off cut chosen without evidence; it gates nothing.
"""
import collections, pathlib, sys

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

def shown_support(Tp, run, x):
    """x after run, on shown answers -> (agreement, families, unreasoned k, n) or None"""
    ctx, rk = shown_top(Tp, run)
    if rk and rk[0][0] == x:
        agr, nfam, _ = rk[0][1]
        if agr >= THETA and nfam >= 2:
            u = Tp.unreasoned.get(ctx, [])
            return agr, nfam, sum(1 for f in u if f == x), len(u)
    return None

def written_support(Tp, run, x):
    """x after run, on written answers whose context is a suffix of run -> (agreement, families naming x) or None"""
    per = collections.defaultdict(list)
    for j in range(2, min(TR.MAXK, len(run)) + 1):
        for f, xs in Tp.written.get(tuple(run[-j:]), {}).items():
            per[f] += xs
    if not per:
        return None
    shares = {f: sum(1 for y in xs if y == x) / len(xs) for f, xs in per.items()}
    agr = sum(shares.values()) / len(shares)
    nfam = sum(1 for v in shares.values() if v > 0)
    return (agr, nfam) if agr >= THETA and nfam >= 2 else None

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

def judge(g, Tp):
    """-> per link i (g[i]-g[i+1]): ("S", agr, fam, uk, un) | ("W", agr, fam) | None"""
    out = []
    n = len(g)
    for i in range(n - 1):
        a, b = g[i], g[i + 1]
        fwd, bwd = g[:i + 1], g[i + 1:][::-1]              # run before b (forward); run before a (backward)
        s_f = shown_support(Tp, fwd, b) if len(fwd) >= 2 else None
        s_b = shown_support(Tp, bwd, a) if len(bwd) >= 2 else None
        st = None
        if s_f and not contradicts(Tp, bwd, a, none_counts=False):
            st = ("S",) + s_f
        if s_b and not contradicts(Tp, fwd, b, none_counts=False) and (st is None or s_b[0] > st[1]):
            st = ("S",) + s_b
        if st is None:
            w_f = written_support(Tp, fwd, b) if len(fwd) >= 2 else None
            w_b = written_support(Tp, bwd, a) if len(bwd) >= 2 else None
            if w_f and not contradicts(Tp, fwd, b, none_counts=True) and not contradicts(Tp, bwd, a, none_counts=False):
                st = ("W",) + w_f
            elif w_b and not contradicts(Tp, bwd, a, none_counts=True) and not contradicts(Tp, fwd, b, none_counts=False):
                st = ("W",) + w_b
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
        L.append(f"| {i} | `{' '.join(s['glyphs'])}`{' ↻ (wraps)' if s.get('wraps') else ''} | {len(s['glyphs'])} | {s['agreement']:.2f} | {s['families_min']} | {f'{k}/{n}' if n else '(none)'} |")
    if len(kept) > TOP:
        L += ["", f"*{len(kept) - TOP} shorter stretches not shown.*"]
    L += ["", "## Carried by written answers (awaiting shown confirmation)", "",
          f"Runs in which some links are carried only by **written** answers. In the stated direction, all written answers whose context matches the run before the link name the next glyph, with agreement ≥ {THETA} from ≥ 2 families, and no shown answer contradicts it. In particular, a shown \"none\" at that point (momentum past a felt end) excludes the link. These are the minds' own generation, not yet confirmed when shown. Long runs here are often code-chart walks: a mind carrying on through a block in code-point order. The planner asks such contexts shown, and puts written continuations past shown ends to recognition.", "",
          "| # | run | glyphs | written links / shown links | mean agreement | families (min over links) |", "|---|---|---|---|---|---|"]
    for i, s in enumerate(carried[:TOP_WRITTEN], 1):
        L.append(f"| {i} | `{' '.join(s['glyphs'])}`{' ↻ (wraps)' if s.get('wraps') else ''} | {len(s['glyphs'])} | {s['written_links']} / {s['shown_links']} | {s['agreement']:.2f} | {s['families_min']} |")
    if len(carried) > TOP_WRITTEN:
        L += ["", f"*{len(carried) - TOP_WRITTEN} shorter runs not shown.*"]
    (ROOT / "BEST.md").write_text("\n".join(L) + "\n")
    print("\n".join(L[:6]))

if __name__ == "__main__":
    main()
