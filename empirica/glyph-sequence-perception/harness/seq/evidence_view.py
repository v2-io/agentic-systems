#!/usr/bin/env python3
"""Sequences built directly from witnessed triples, without the likelihood model (a second view, 2026-10-04).

  evidence_view.py [RID] [--top N]   -> data/standings/<RID>-evidence.md / .json; prints a comparison with the fit

WITNESSED TRIPLE: a triple whose answers (all minds, all presentations; order items counted as their implied triples)
name the same middle at least twice, and in at least half of all its answers (none / two / other middle included).
Same rule as the fit's witness and the standings' confirmed links. A tie answer witnesses a tie the same way.

CHAINS. Start from every witnessed triple a-m-b (as a path; direction-free). Extend an end (p, q) by every glyph x
with a witnessed triple p-q-x (q in the middle), unless the chain already holds x, or some other chain glyph y has a
witnessed triple on {y, q, x} whose middle contradicts the chain order. A witnessed triple says its middle lies BETWEEN
the others, not that they are adjacent, so candidates are transitively reduced: x is dropped when another candidate y is
witnessed between q and x. Several remaining x (mutually unordered) = a FORK: each continuation becomes its own chain. Chains contained in a longer one (same order) are folded into it, and so are near-restatements (>= 70% of their glyphs
in a longer chain, same order); a folded chain's extra glyphs are listed as hints at its host (not placed). Nothing here is guessed:
every adjacent step of every chain is the middle of a witnessed triple.

PER FAMILY: the share of the chain's adjacent triples (consecutive glyph triples) that are also witnessed using only
that family's answers (families with >= 2 answers on the triple count as measured). U = mean over measured families.
BRANCH POINTS: glyphs at which chains of this view fork, or which two distinct chains share.
"""
import argparse, collections, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from common import EXP, minds as load_minds
import model as M
import round as RD

MAX_CHAINS = 4000

def witnessed(tally):
    """tally: Counter of outcomes -> the witnessed outcome or None."""
    n = sum(tally.values())
    if not n:
        return None
    out, k = tally.most_common(1)[0]
    if out[0] in ("mid", "tie2", "tie3") and k >= 2 and k >= 0.5 * n:
        return out
    return None

def build(obs, fam):
    pooled = collections.defaultdict(collections.Counter)
    byfam = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
    for o in obs:
        pooled[o["tri"]][o["out"]] += 1
        byfam[o["tri"]][fam.get(o["mind"], o["mind"])][o["out"]] += 1
    W = {t: w for t, c in pooled.items() if (w := witnessed(c))}
    mid_of = {t: w[1] for t, w in W.items() if w[0] == "mid"}
    # extension index: (p, q) with q the middle -> glyphs x such that p-q-x witnessed
    nxt = collections.defaultdict(set)
    for t, m in mid_of.items():
        a, b = [g for g in t if g != m]
        nxt[(a, m)].add(b); nxt[(b, m)].add(a)
    def contradicts(chain, q, x):
        for y in chain:
            if y in (q, x):
                continue
            t = tuple(sorted((y, q, x)))
            w = mid_of.get(t)
            if w is not None and w != q:
                return True
        return False
    def extend(chain):
        """all maximal right-extensions of chain (list), forking where several continuations are witnessed."""
        out, stack = [], [chain]
        while stack and len(out) < MAX_CHAINS:
            c = stack.pop()
            p, q = c[-2], c[-1]
            xs = sorted(x for x in nxt.get((p, q), ()) if x not in c and not contradicts(c, q, x))
            # transitive reduction: a witnessed triple says its middle lies BETWEEN, not that the others are adjacent;
            # drop x when another candidate y is witnessed between q and x (x is reachable through y)
            # (evidence from anywhere behind: z y x with y in the middle, for any chain glyph z, puts y before x)
            xs = [x for x in xs if not any(mid_of.get(tuple(sorted((z, y, x)))) == y for y in xs if y != x for z in c)]
            if not xs:
                out.append(c)
            for x in xs:
                stack.append(c + [x])
        return out
    chains = []
    seen = set()
    for t, m in sorted(mid_of.items()):
        a, b = [g for g in t if g != m]
        for right in extend([a, m, b]):
            for full in extend(right[::-1]):
                key = tuple(full) if full[0] <= full[-1] else tuple(full[::-1])
                if key not in seen:
                    seen.add(key); chains.append(list(key))
        if len(chains) > MAX_CHAINS:
            break
    steps = [[[g] for g in c] for c in chains]
    keep = M.maximal(steps)
    chains = [chains[i] for i in keep]
    # fold near-restatements: a chain sharing >= 70% of its glyphs with a longer chain, in the same order, is folded
    # into it; its extra glyphs become hints at the longer chain (e.g. ①②③④⑤⑦⑪ into ①…⑩, hint ⑪)
    chains.sort(key=lambda c: (-len(c), c))
    kept, hints = [], collections.defaultdict(set)
    for c in chains:
        host = None
        for k in kept:
            common = [g for g in c if g in set(k)]
            if len(common) >= 0.7 * len(c):
                pk = {g: i for i, g in enumerate(k)}
                seq = [pk[g] for g in common]
                if all(a_ < b_ for a_, b_ in zip(seq, seq[1:])) or all(a_ > b_ for a_, b_ in zip(seq, seq[1:])):
                    host = tuple(k); break
        if host:
            hints[host].update(g for g in c if g not in set(host))
        else:
            kept.append(c)
    return kept, W, byfam, hints

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("round", nargs="?"); ap.add_argument("--top", type=int, default=60); ap.add_argument("--data")
    a = ap.parse_args()
    d = pathlib.Path(a.data) if a.data else EXP / "data"
    fitted = [r for r in RD.rounds(d) if (d / "rounds" / r / "fit.json").exists()]
    rid = a.round or fitted[-1]
    items, pres, parsed, sheets = RD.load_all(d, upto=rid)
    obs = M.observations(parsed, pres)
    fam = RD.family_of(d)
    fams = sorted(set(fam.values()))
    chains, W, byfam, hints = build(obs, fam)
    owners = collections.Counter(g for c in chains for g in set(c))
    rows = []
    for c in chains:
        per = {}
        for f in fams:
            meas = ok = 0
            for t3 in zip(c, c[1:], c[2:]):
                t = tuple(sorted(t3))
                tal = byfam[t].get(f)
                if tal and sum(tal.values()) >= 2:
                    meas += 1; w = witnessed(tal)
                    ok += w is not None and w == ("mid", t3[1])
            if meas:
                per[f] = ok / meas
        U = sum(per.values()) / len(per) if per else 0.0
        rows.append({"seq": c, "n": len(c), "per": per, "U": U, "families": len(per),
                     "branch_at": [g for g in c if owners[g] >= 2], "hints": sorted(hints.get(tuple(c), ()))})
    rows.sort(key=lambda r: (-(r["U"] * (r["families"] / len(fams)) ** 0.5), -r["n"]))
    stable = [r for r in rows if r["families"] >= 2 and r["U"] >= 0.8]
    L = [f"# Sequences from witnessed triples, after {rid}", "",
         f"*Generated by `harness/seq/evidence_view.py`: a second view, built without the likelihood model. Every adjacent step of every sequence is the middle of a triple the minds answered in that order at least twice, by a majority. Where an end has several witnessed continuations, the sequence forks. "
         f"{len(W)} witnessed triples; {len(rows)} sequences after folding restatements; {len(stable)} stable (two or more families measured, U ≥ 0.8).*", "",
         "**Family columns:** the share of the sequence's consecutive triples also witnessed using only that family's answers. `–` means unmeasured. **Branch at:** glyphs it shares with another sequence in this view.", "",
         "| # | sequence | n | " + " | ".join(fams) + " | U | branch at | folded-in glyphs (hints) |", "|---|---|---|" + "---|" * len(fams) + "---|---|---|"]
    for i, r in enumerate(rows[:a.top], 1):
        L.append(f"| {i} | `{' '.join(r['seq'])}` | {r['n']} | " + " | ".join(f"{r['per'][f]:.2f}" if f in r["per"] else "–" for f in fams)
                 + f" | {r['U']:.2f} | {''.join(r['branch_at'])} | {''.join(r['hints'])} |")
    # comparison with the fit-based standings
    std = d / "standings" / f"{rid}.json"
    if std.exists():
        fitrows = json.load(open(std))
        fit_seqs = [x["seq"].replace("=", " ").split() for x in fitrows if x.get("score", 0) > 0]
        def match(s, pool):
            return any(len(set(s) & set(q)) / len(set(s) | set(q)) >= 0.7 for q in pool)
        ev = [r["seq"] for r in stable]
        both = sum(1 for s in ev if match(s, fit_seqs))
        L += ["", "## Against the fit-based standings", "",
              f"- stable here and matched (glyph Jaccard ≥ 0.7) in the standings: {both} of {len(ev)}",
              f"- stable here only: {len(ev) - both}",
              f"- ranked in the standings but not matched by any sequence here: {sum(1 for s in fit_seqs if not match(s, [r['seq'] for r in rows]))} of {len(fit_seqs)}"]
    out = d / "standings"; out.mkdir(exist_ok=True)
    (out / f"{rid}-evidence.md").write_text("\n".join(L) + "\n")
    json.dump(rows, open(out / f"{rid}-evidence.json", "w"), ensure_ascii=False, indent=0)
    print("\n".join(L[:12 + min(30, len(rows))])); print("\n".join(L[-5:]))

if __name__ == "__main__":
    main()
