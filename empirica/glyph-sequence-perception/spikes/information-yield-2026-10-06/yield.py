#!/usr/bin/env python3
"""Realized information gain per question: how far each round's answers moved what the question measures.

For every quantity a question measures (the planner's identities: a continue context's next glyph, an inhibit or
cohere verdict, a choose preference, a triad's middle, an order set's line, a pick context's pick) and every family,
answers are taken in round order (the triad era first, then c001 on by number). Each round's answers from one family
update a Dirichlet over the outcomes seen at that quantity (prior 1/2 on every outcome ever seen there, plus one for
an unseen outcome). The round's realized gain is KL(after || before), the Bayesian surprise in nats; the fall in the
posterior predictive entropy is reported beside it. Gains are credited to the round's questions by their `source.why`
and kind, and divided by the answers that produced them (per answer slot). The planner's expected information for
the same answer (plan.info on the share of the pooled top outcome, as stochastic-1..3 compute it) is reported beside
it, so its calibration can be read.

The seal: every choose and names record touching a canary glyph is dropped before anything is read. Controls (decoys,
shuffles, chart windows, lookalike controls, choose controls) measure a rater's base rate, not the item: kept as their
own groups. Usage: python3 yield.py [first-round] [last-round] (context rounds; default c096 c105)
"""
import collections, json, math, pathlib, sys

STUDY = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(STUDY / "priority")); sys.path.insert(0, str(STUDY / "probe")); sys.path.insert(0, str(STUDY / "tree"))
import plan as PL                                    # noqa: E402  (CANARY, info, round_num)

def rnum(r):
    if r.startswith("r"):
        return -1000 + int("".join(c for c in r[1:] if c.isdigit()) or 0)
    return PL.round_num(r) if PL.round_num(r) is not None else None

def key_outcome(r):
    """-> (quantity key, outcome) or None"""
    k, o, t = r["kind"], r.get("outcome"), r.get("tags") or {}
    c = tuple(r.get("context") or ())
    ctl = t.get("control")
    if k in ("choose", "names") and PL.CANARY & (set(c) | set(r.get("candidates") or [])):
        return None                                   # sealed
    if k in ("continue", "next"):
        v = t.get("variant")
        kind = "reasoned" if v == "reasoned" else "reflection" if v == "reflection" else "continue"
        if o == "continuation":
            out = r["continuation"][0]
        elif o == "proposals":
            ps = sorted(r.get("proposals", []), key=lambda p: p["rank"])
            out = ps[0]["g"] if ps else "<other>"
        elif o in ("none", "other"):
            out = "<" + o + ">"
        else:
            return None
        return (kind, c), out
    if k == "inhibit" and o in ("yes", "no", "cant-tell"):
        return (("inhibit-control" if ctl else "inhibit"), (c, r.get("candidate"))), o
    if k == "cohere" and o in ("yes", "no", "cant-tell"):
        g = tuple(min(list(c), list(c)[::-1]))
        return (("cohere-" + ctl) if ctl else "cohere", g), o
    if k == "choose" and o == "chose":
        pair = frozenset(r.get("candidates") or ())
        if ctl == "neutral":
            return ("choose-control", pair), r["choice"]
        return ("choose", (c, pair)), r["choice"]
    if k == "triad" and o in ("mid", "two", "none"):
        ans = r.get("answer") or []
        return ("triad", tuple(sorted(r.get("shown") or c))), (("mid", ans[1]) if o == "mid" else (o,))
    if k in ("order", "names") and o in ("lines", "none"):
        if o == "none":
            out = ("none",)
        else:
            lines = (r.get("answer") or {}).get("lines") or []
            main = max(lines, key=lambda ln: sum(len(st) for st in ln if st != "GAP")) if lines else []
            cc = tuple("…" if st == "GAP" else "=".join(sorted(st)) for st in main)
            out = min(cc, cc[::-1])
        return (k, frozenset(r.get("shown") or c)), out
    if k == "pick" and o in ("continuation", "none", "other"):
        out = r["continuation"][0] if o == "continuation" else "<" + o + ">"
        return (("pick-null" if t.get("null") else "pick"), c), out
    return None

def lgamma(x):
    return math.lgamma(x)

def kl_dirichlet(a, b):
    """KL(Dir(a) || Dir(b)) over the same categories"""
    a0, b0 = sum(a), sum(b)
    s = lgamma(a0) - sum(lgamma(x) for x in a) - lgamma(b0) + sum(lgamma(x) for x in b)
    return s + sum((x - y) * (PL.psi(x) - PL.psi(a0)) for x, y in zip(a, b))

def entropy_pred(a):
    a0 = sum(a)
    return -sum((x / a0) * math.log(x / a0) for x in a)

def main(first="c096", last="c105"):
    lo, hi = PL.round_num(first), PL.round_num(last)
    recs, seen = [], set()
    for f in sorted((STUDY / "data" / "answers").glob("*.jsonl")):
        for l in open(f):
            if l.strip():
                r = json.loads(l)
                if r.get("aid") in seen or r.get("kind") == "seed":
                    continue
                seen.add(r.get("aid"))
                n = rnum(r.get("round", ""))
                if n is None:
                    continue
                ko = key_outcome(r)
                if ko:
                    recs.append((n, r, ko))
    recs.sort(key=lambda t: t[0])
    cats = collections.defaultdict(set)                   # quantity -> outcomes ever seen
    for n, r, (q, out) in recs:
        cats[q].add(out)
    counts = collections.defaultdict(collections.Counter)   # (quantity, family) -> outcome counts so far
    by_round = collections.defaultdict(list)
    for n, r, ko in recs:
        by_round[n].append((r, ko))
    agg = collections.defaultdict(lambda: [0.0, 0.0, 0.0, 0, 0.0])   # (kind, why) -> [KL, entropy fall, expected, answers, gain ratio]
    for n in sorted(by_round):
        group = collections.defaultdict(list)
        for r, (q, out) in by_round[n]:
            group[(q, r["family"])].append((r, out))
        for (q, fam), rows in group.items():
            before = counts[(q, fam)]
            if lo <= n <= hi:
                order = sorted(cats[q], key=str) + ["<unseen>"]
                b = [before.get(o, 0) + 0.5 for o in order]
                after = collections.Counter(before)
                after.update(out for _, out in rows)
                a = [after.get(o, 0) + 0.5 for o in order]
                kl = kl_dirichlet(a, b)
                dh = entropy_pred(b) - entropy_pred(a)
                ha = entropy_pred(a)
                gr = kl / ha if ha > 0 else 0.0     # gain ratio (C4.5): gain over the intrinsic information of the
                                                    # outcome distribution it lands in -- scattered answers penalised
                top = max(before.values()) if before else 0
                expected = PL.info(top, sum(before.values()))       # per answer, as the planner computes it
                for r, out in rows:
                    why = (r.get("source") or {}).get("why") or "(none)"
                    if r.get("era") != "ctx":
                        why = "(triad era)"
                    e = agg[(q[0], why)]
                    e[0] += kl / len(rows); e[1] += dh / len(rows); e[2] += expected; e[3] += 1; e[4] += gr / len(rows)
            counts[(q, fam)].update(out for _, out in rows)
    out = []
    for (kind, why), (kl, dh, ex, n, gr) in agg.items():
        out.append((kind, why, n, kl / n, dh / n, ex / n, gr / n))
    out.sort(key=lambda t: (t[0], -t[3]))
    print(f"realized information per answer, rounds {first}-{last} (KL nats = Bayesian surprise; dH = fall in predictive entropy; expected = the planner's per-answer information)")
    print(f"{'kind':20} {'why':20} {'answers':>8} {'KL':>7} {'dH':>7} {'ratio':>7} {'expected':>8}")
    for kind, why, n, kl, dh, ex, gr in out:
        print(f"{kind:20} {why:20} {n:8d} {kl:7.3f} {dh:7.3f} {gr:7.3f} {ex:8.3f}")

if __name__ == "__main__":
    main(*sys.argv[1:3])
