#!/usr/bin/env python3
"""Sequences as the loop grows them -- Joseph's methodology (2026-10-04) as the structure, with nothing discarded:

  "various minds start to find a sequence -- call it a sequence of three glyphs. The priority is then to extend that
   sequence to the right and to the left as far as they will go ... I would expect a little bit of branching etc."
  "I don't understand why there is some sort of consolidation work anymore at all, really, that throws away good data
   because it's not supported *enough* ... when we're still hot and exploring even completely random stuff"

Every answer is data; support orders and is shown, it never removes anything.

  KERNEL   any triad some answer gave a middle to (a triad given two different middles is two kernels).
  CLAIM    a mind's statement that x comes directly next to q: a what-comes-next or a between proposal. (Consecutive
           glyphs in an order answer are not claims: the minds ordered a subset, so neighbours there need not be
           adjacent. Their triples count as triad answers instead.)
  STEP     from an end ...p q to a claimed neighbour x of q, where some answer gave q as the middle of {p, q, x}; inward,
           x between u v where x was claimed next to both and some answer gave x as the middle of {u, x, v}.
           Each end takes its best-supported step (answers for that middle, then claims); every other step there is
           itself a kernel and grows into its own sequence, so branches appear as sequences sharing a stretch.
  CYCLE    a step back to the first glyph closes the sequence there (Joseph: "clamp after one repeat"). Needs >= 4
           glyphs: on 3 glyphs all three triples are the same triad, so "each between the others" is three answers
           disagreeing about one triad, not a loop.
  PROPOSED claims at an end that no answer has tested yet: listed at the end, not glued on (they are what the
           planner tests next).
  A row whose glyphs all lie in a longer row in the same order is that row at an earlier stage of growth, shown once
  as the longer. Lines and cycles are never merged: a cycle claims its closure, and the line through the same glyphs
  keeps its own support.

  growth.py [RID] [--data DIR]   -> DIR/growth/<RID>.json, DIR/standings/<RID>.md, and for the study STANDINGS.md
"""
import argparse, collections, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from common import EXP
import model as M
import round as RD

def tallies(obs, fam):
    """triple -> Counter(outcome -> answers); outcome is ('mid', g), ('none',) or ('two', x, y).
    triple -> middle -> set of (mind, family)."""
    cnt = collections.defaultdict(collections.Counter)
    who = collections.defaultdict(lambda: collections.defaultdict(set))
    for o in obs:
        cnt[o["tri"]][tuple(o["out"])] += 1
        if o["out"][0] == "mid":
            who[o["tri"]][o["out"][1]].add((o["mind"], fam.get(o["mind"], o["mind"])))
    return cnt, who

def claims(parsed, pres):
    """unordered pair {q, x} -> number of proposals putting x directly next to q."""
    c = collections.Counter()
    for r in parsed:
        if r["status"] != "ok":
            continue
        p = pres[r["pid"]]; a = r["answer"]
        if not isinstance(a, dict):
            continue
        if p["kind"] == "next":
            for x in a.get("proposals", []):
                if x != p["shown"][-1]:
                    c[frozenset((p["shown"][-1], x))] += 1
        elif p["kind"] == "between":
            gi = p["shown"].index("GAP"); l, rr = p["shown"][gi - 1], p["shown"][gi + 1]
            for x in a.get("proposals", []):
                if x not in (l, rr):
                    c[frozenset((l, x))] += 1; c[frozenset((x, rr))] += 1
    return c

def build(obs, parsed, pres, fam):
    cnt, who = tallies(obs, fam)
    adj = claims(parsed, pres)
    nbr = collections.defaultdict(set)
    for pair in adj:
        if len(pair) == 2:
            q, x = tuple(pair)
            nbr[q].add(x); nbr[x].add(q)
    third = collections.defaultdict(set)              # unordered pair -> glyphs answered in a triad with it
    for t in cnt:
        a, b, c = t
        third[(a, b)].add(c); third[(a, c)].add(b); third[(b, c)].add(a)
    def mid(a, m, b):
        return cnt.get(tuple(sorted((a, m, b))), {}).get(("mid", m), 0)
    def pairk(u, v):
        return (u, v) if u <= v else (v, u)
    def grow(s):
        """Place, one at a time and best-supported first, every glyph some answer puts beyond an end or between two
        neighbours; close a cycle when answers put the first glyph beyond the last (>= 4 glyphs)."""
        cyc = False
        while True:
            best = None
            ins = set(s)
            pairs = list(zip(s, s[1:])) + ([(s[-1], s[0])] if cyc else [])
            for i, (u, v) in enumerate(pairs):            # between u and v
                for x in third.get(pairk(u, v), ()):
                    if x not in ins:
                        k = mid(u, x, v)
                        if k and (best is None or (k, x) > best[0]):
                            best = ((k, x), "in", i, x)
            if not cyc:
                for side in ("R", "L"):
                    p, q = (s[-2], s[-1]) if side == "R" else (s[1], s[0])
                    for x in third.get(pairk(p, q), ()):
                        if x not in ins or (x == (s[0] if side == "R" else s[-1]) and len(s) >= 4):
                            k = mid(p, q, x)
                            if k and x in ins:      # closing: the wrap triple must be answered too
                                k = min(k, mid(q, x, s[1] if side == "R" else s[-2]))
                            if k and (best is None or (k, x) > best[0]):
                                best = ((k, x), side, None, x)
            if best is None:
                return s, cyc
            _, how, i, x = best
            if how == "in":
                s = s[:i + 1] + [x] + s[i + 1:]
            elif x in s:
                cyc = True
            elif how == "R":
                s = s + [x]
            else:
                s = [x] + s
    found, seen = [], set()
    for t, c in sorted(cnt.items()):
        for out in sorted(c):
            if out[0] != "mid":
                continue
            m = out[1]; a, b = [g for g in t if g != m]
            if not mid(a, m, b):
                continue
            s, cyc = grow([a, m, b])
            if cyc:
                rots = [s[i:] + s[:i] for i in range(len(s))]
                key = ("cycle", tuple(min(rots + [r[::-1] for r in rots])))
            else:
                key = ("line", tuple(min(s, s[::-1])))
            if key not in seen:
                seen.add(key); found.append({"glyphs": list(key[1]), "cyclic": key[0] == "cycle"})
    def in_order(small, big):
        """small's glyphs appear in big in small's order (either direction; cyclically if big is a cycle)."""
        g = big["glyphs"]
        if small["cyclic"] != big["cyclic"]:      # a cycle claims its closure; a line does not -- both are kept
            return False
        pos = {x: i for i, x in enumerate(g)}
        if any(x not in pos for x in small["glyphs"]):
            return False
        n = len(g)
        for seq in (small["glyphs"], small["glyphs"][::-1]):
            ps = [pos[x] for x in seq]
            if big["cyclic"]:
                ps = [(p - ps[0]) % n for p in ps]
            if all(a < b for a, b in zip(ps, ps[1:])):
                return True
        return False
    found.sort(key=lambda s: (-len(s["glyphs"]), -s["cyclic"], s["glyphs"]))
    kept, by_glyph = [], collections.defaultdict(list)
    for s in found:
        cands = set(range(len(kept)))
        for x in s["glyphs"]:
            cands &= set(by_glyph[x])
            if not cands:
                break
        if not any(in_order(s, kept[j]) for j in cands):
            for x in s["glyphs"]:
                by_glyph[x].append(len(kept))
            kept.append(s)
    fams = sorted(set(fam.values()))
    # the rank is over the families still being asked (those that answered in the latest round): a paused family
    # (Glimmer, since r003) would otherwise cap every sequence first asked after it paused
    last = max((r.get("round", "") for r in parsed), default="")
    live = sorted({fam.get(r["mind"], r["mind"]) for r in parsed if r.get("round") == last}) or fams
    for s in kept:
        g = s["glyphs"]
        seq = g + g[:2] if s["cyclic"] else g
        steps = []
        for a, m, b in zip(seq, seq[1:], seq[2:]):
            t = tuple(sorted((a, m, b))); c = cnt.get(t, collections.Counter())
            ws = who.get(t, {}).get(m, set())
            rival = max((k for o, k in c.items() if o[0] == "mid" and o[1] != m), default=0)
            steps.append({"triple": [a, m, b], "answers": c[("mid", m)], "other": sum(c.values()) - c[("mid", m)],
                          "rival": rival, "minds": sorted({w[0] for w in ws}), "families": sorted({w[1] for w in ws})})
        s["steps"] = steps
        s["family_share"] = {f: sum(f in st["families"] for st in steps) / len(steps) for f in fams}
        # how universally and how consistently the minds give each step: (families giving it / all families) x
        # (answers giving it / all answers to that triad), averaged over steps. It orders rows; it removes none.
        s["stability"] = sum(len(set(st["families"]) & set(live)) / len(live) * st["answers"] / max(1, st["answers"] + st["other"])
                             for st in steps) / len(steps)
        s["weakest"] = min(st["answers"] for st in steps)
        s["answers"] = sum(st["answers"] for st in steps)
        s["proposed"] = {}
        if not s["cyclic"]:
            for p, q in ((g[-2], g[-1]), (g[1], g[0])):
                s["proposed"][q] = sorted((x for x in nbr.get(q, ()) if x not in g and mid(p, q, x) == 0),
                                          key=lambda x: (-adj[frozenset((q, x))], x))
        # branch proposals inside the row: glyphs minds proposed next to an interior glyph q (every glyph of a cycle),
        # not in the row, and not yet tested -- no answer has put q between x and either of q's neighbours
        s["proposed_inside"] = {}
        n = len(g)
        idx = range(n) if s["cyclic"] else range(1, n - 1)
        for i in idx:
            q = g[i]; nb = (g[i - 1], g[(i + 1) % n])
            xs = sorted((x for x in nbr.get(q, ()) if x not in g and all(mid(u, q, x) == 0 for u in nb)),
                        key=lambda x: (-adj[frozenset((q, x))], x))
            if xs:
                s["proposed_inside"][q] = xs
    kept.sort(key=lambda s: (-s["stability"], -len(s["glyphs"]), -s["answers"], s["glyphs"]))
    return kept, fams, live

def good_step(st):
    return len(st["families"]) >= 2 and st["answers"] >= st["rival"]

def stable_stretches(seqs):
    """The stable read-off, per stretch rather than per row: maximal runs of consecutive steps each given by minds of
    >= 2 families with no other middle given more often, as glyph runs of >= 3, each counted once (a run inside a
    longer run, either direction, is that run). Per row, a stable stretch stopped counting the moment the row grew a
    new, not-yet-backed step (2026-10-05: 52 of the 55 'lost' stable rows at r011 had grown, e.g. α…η -> α…θ)."""
    runs = set()
    for s in seqs:
        g, steps = s["glyphs"], s["steps"]
        ok = [good_step(x) for x in steps]
        if s["cyclic"]:
            if all(ok):
                rots = [g[i:] + g[:i] for i in range(len(g))]
                runs.add(("cycle", tuple(min(rots + [r[::-1] for r in rots])))); continue
            k = ok.index(False)                    # rotate so the ring starts just after a gap
            ring = g + g[:2]
            order = list(range(k + 1, len(steps))) + list(range(0, k + 1))
            seq_steps = [(ring[i:i + 3], ok[i]) for i in order]
        else:
            seq_steps = [(g[i:i + 3], ok[i]) for i in range(len(steps))]
        cur = []
        for tri, good in seq_steps + [(None, False)]:
            if good:
                cur = cur + [tri[2]] if cur else list(tri)
            else:
                if len(cur) >= 3:
                    runs.add(("line", tuple(min(cur, cur[::-1]))))
                cur = []
    lines = sorted((r for r in runs if r[0] == "line"), key=lambda r: -len(r[1]))
    kept = [r for r in runs if r[0] == "cycle"]
    for r in lines:
        t = r[1]; n = len(t)
        inside = False
        for k_ in kept:
            big = k_[1] + (k_[1][:n - 1] if k_[0] == "cycle" else ())
            if any(big[i:i + n] in (t, t[::-1]) for i in range(len(big) - n + 1)):
                inside = True; break
        if not inside:
            kept.append(r)
    return [list(r[1]) + (["↻"] if r[0] == "cycle" else []) for r in kept]

def stable(s):
    """A read-off for STANDINGS/PROGRESS; it gates nothing. Every step given by minds of >= 2 families, and no other
    middle given more often on that triad (a rival middle is a competing perception; a none-answer is not)."""
    return all(good_step(st) for st in s["steps"])

def piece_table(obs, parsed, pres, fam):
    """All sequences for the planner (round.cmd_plan -> squeue.sequence_work), most stable first."""
    seqs, fams, live = build(obs, parsed, pres, fam)
    return [{"steps": [[x] for x in s["glyphs"]], "glyphs": s["glyphs"], "cyclic": s["cyclic"], "stability": s["stability"],
             "U": s["stability"], "families": sum(v > 0 for v in s["family_share"].values()), "support": 1.0,
             "hints": [], "forks": [], "untested": [st["triple"] for st in s["steps"] if st["answers"] == 0]} for s in seqs]

def bucket(n):
    return "3" if n == 3 else "4–5" if n <= 5 else "6–7" if n <= 7 else "8–9" if n <= 9 else "10+"

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("round", nargs="?"); ap.add_argument("--data"); ap.add_argument("--top", type=int, default=300)
    a = ap.parse_args()
    d = pathlib.Path(a.data) if a.data else EXP / "data"
    rid = a.round or RD.rounds(d)[-1]
    items, pres, parsed, sheets = RD.load_all(d, upto=rid)
    obs = M.observations(parsed, pres)
    fam = RD.family_of(d)
    seqs, fams, live = build(obs, parsed, pres, fam)
    out = d / "growth"; out.mkdir(exist_ok=True)
    json.dump(seqs, open(out / f"{rid}.json", "w"), ensure_ascii=False)
    owners = collections.Counter(x for s in seqs for x in set(s["glyphs"]))
    st = stable_stretches(seqs)
    bk = collections.Counter(bucket(len([x for x in r if x != "↻"])) for r in st)
    L = [f"# Standings after {rid}", "",
         f"*Generated by `harness/seq/growth.py` from every answer through {rid}; nothing is filtered out. A sequence starts from any triad a mind gave a middle, and grows at each end by the minds' own proposals of what comes next or between. A step counts once some answer puts it in the middle. Each end takes its best-supported step; the other steps there grow into their own rows, so **branches** are rows sharing a stretch. ↻ marks a **cycle**, clamped where it returns to its start. History: `data/standings/`; full step-level data: `data/growth/{rid}.json`.*", "",
         f"**{len(seqs)} sequences.** {len(st)} **stable stretches**: runs of three or more glyphs in which every step was given by minds of two or more families, and no other middle more often; each counted once "
         f"(by length: " + ", ".join(f"{k}: {bk[k]}" for k in ("3", "4–5", "6–7", "8–9", "10+")) + ").", "",
         "**How to read a row.** A row is a sequence; a **step** is three consecutive glyphs `p q r`, and a mind *gave* the step when it answered that `q` lies between `p` and `r`. Example: `0 1 2 3` has two steps, `0 1 2` and `1 2 3`.", "",
         "- **rank**: what the rows are sorted by (and the order the planner works in). For each step, (families whose minds gave it ÷ the families still being asked: " + ", ".join(live) + ") × (answers that gave it ÷ all answers to that triad), averaged over the row's steps. 1.00 = every family still being asked gave every step and no answer disagreed.",
         "- **family columns** (" + ", ".join(fams) + "): the share of the row's steps that at least one mind of that family gave. 1.00 = that family gave every step; 0.50 = half of them; 0.00 = none, usually because it was never asked them. " + ("" if set(fams) == set(live) else "Families not being asked any more (" + ", ".join(f for f in fams if f not in live) + ": " + ", ".join(m for m, f_ in fam.items() if f_ not in live) + ", paused) mostly show 0.00 on recent rows."),
         "- **n**: glyphs in the row. **weakest**: the fewest answers that gave any one step (0 = a step no answer has given yet; the planner asks it). **against**: other answers to the row's triads (a different middle, “only two go together”, or ⟂).",
         "- **shared**: glyphs that also sit in other rows (branch points). **proposed beyond**: glyphs minds proposed next to an end that no answer has tested yet, per end (`end→proposals`, up to six). **proposed inside**: the same at glyphs inside the row, every glyph of a cycle: possible branches (`glyph→proposals`, up to four).", "",
         "| # | sequence | n | rank | " + " | ".join(fams) + " | weakest | against | shared | proposed beyond | proposed inside |",
         "|---|---|---|---|" + "---|" * len(fams) + "---|---|---|---|---|"]
    for i, s in enumerate(seqs[:a.top], 1):
        shown = " ".join(s["glyphs"]) + (" ↻" if s["cyclic"] else "")
        prop = "; ".join(f"{q}→{''.join(xs[:6])}" for q, xs in s["proposed"].items() if xs)
        inside = "; ".join(f"{q}→{''.join(xs[:4])}" for q, xs in s["proposed_inside"].items())
        L.append(f"| {i} | `{shown}` | {len(s['glyphs'])} | {s['stability']:.2f} | " + " | ".join(f"{s['family_share'][f]:.2f}" for f in fams)
                 + f" | {s['weakest']} | {sum(x['other'] for x in s['steps'])} | {''.join(x for x in s['glyphs'] if owners[x] >= 2)} | {prop} | {inside} |")
    if len(seqs) > a.top:
        L += ["", f"*{len(seqs) - a.top} more rows (lower stability) in `data/growth/{rid}.json`.*"]
    text = "\n".join(L) + "\n"
    (d / "standings").mkdir(exist_ok=True)
    (d / "standings" / f"{rid}.md").write_text(text)
    if d == EXP / "data":
        (EXP / "STANDINGS.md").write_text(text)
    print("\n".join(L[:60]))

if __name__ == "__main__":
    main()
