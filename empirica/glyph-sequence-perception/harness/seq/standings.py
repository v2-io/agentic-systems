#!/usr/bin/env python3
"""The running standings: the most stable and universal sequences in the current fit (Joseph, 2026-10-04: "a running
list of the top (at least) 40 or so stable and universal sequences").

  standings.py [RID] [--top N]      default: the latest round with a fit; N = 60

Writes data/standings/<RID>.md and .json (history, one per round) and STANDINGS.md at the study root (the current one).

Per candidate sequence of the round's best fit:
  perception(family) mean over the family's minds of max(s3, s4), counting only minds with >= MIN_EVID answered
                     triples inside the sequence; a family with no such mind is UNMEASURED (shown as -), not zero
  U                  mean perception over measured families (each family counts once)
  coverage           measured families / families on the roster
  support            share of the round's annealing chains and posterior samples holding a matching sequence
                     (glyph Jaccard >= 0.7)
  rounds             in how many rounds' best fits a matching sequence appears, of how many rounds fitted so far
  witnessed          distinct triples inside the sequence answered in its order by >= 2 answers and a majority
  weakest            the glyph whose triples inside the sequence agree least with its order (>= 3 answers), and
                     that agreement: the weakest rung
  agree              share of all answers on triples inside the sequence (any mind, any presentation) that state exactly
                     its order; the rest are none / two / another middle. A wrong rung shows up here first
  origin             'seeded' if one seed holds >= 80% of its glyphs, else 'emergent' (metadata; never used in ranking)
Ranking: support x U x sqrt(coverage), among sequences measured in >= 2 families; ties by length.
Everything is read from the round's fit and the evidence; nothing here feeds back into the queue.
"""
import argparse, collections, json, math, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from common import EXP, read_jsonl, minds as load_minds
import model as M
import round as RD

MIN_EVID = 3

def flat(steps):
    return [g for st in steps for g in st]

def jac(a, b):
    a, b = set(a), set(b)
    return len(a & b) / max(1, len(a | b))

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("round", nargs="?"); ap.add_argument("--top", type=int, default=60)
    ap.add_argument("--data"); a = ap.parse_args()
    d = pathlib.Path(a.data) if a.data else EXP / "data"
    fitted = [r for r in RD.rounds(d) if (d / "rounds" / r / "fit.json").exists()]
    rid = a.round or fitted[-1]
    fit = json.load(open(d / "rounds" / rid / "fit.json"))
    items, pres, parsed, sheets = RD.load_all(d, upto=rid)
    obs = M.observations(parsed, pres)
    mod = M.from_snapshot(fit["best"], obs, fit["minds"])
    reg = load_minds()
    fam = {m: v["family"] for m, v in reg["minds"].items()}
    roster_fams = sorted({fam[m] for m in reg["roster"]["core"] + reg["roster"]["second"]})
    seeds = read_jsonl(d / "seeds.jsonl")
    past = {r: [flat(c["steps"]) for c in json.load(open(d / "rounds" / r / "fit.json"))["best"]["cands"]]
            for r in fitted if r <= rid}
    rows = []
    for (ci, c), cs, sup in zip(sorted(mod.cands.items()), fit["best"]["cands"], fit["support"]):
        g = c.glyphs()
        evid = collections.Counter()
        tally = collections.defaultdict(lambda: [0, 0])
        for i in mod.obs_for(c):
            o = mod.obs[i]
            if len(set(o["tri"]) & set(c.pos)) == 3:
                evid[o["mind"]] += 1
                t = tally[o["tri"]]; t[1] += 1
                t[0] += o["out"] == M._strict(c.pos, o["tri"])
        witnessed = sum(1 for ok, n in tally.values() if ok >= 2 and ok >= 0.5 * n)
        tot = sum(n for ok, n in tally.values())
        pg = collections.defaultdict(lambda: [0, 0])
        for tri, (ok, n) in tally.items():
            for x in tri:
                pg[x][0] += ok; pg[x][1] += n
        weak = min(((v[0] / v[1], x) for x, v in pg.items() if v[1] >= 3), default=(float("nan"), ""))
        agree = sum(ok for ok, n in tally.values()) / tot if tot else 0.0
        per = {}
        for f in roster_fams:
            ms = [m for m in fit["minds"] if fam.get(m) == f and evid[m] >= MIN_EVID]
            if ms:
                per[f] = sum(max(cs["s"][m]["s3"], cs["s"][m]["s4"]) for m in ms) / len(ms)
        U = sum(per.values()) / len(per) if per else 0.0
        cov = len(per) / len(roster_fams)
        rounds_in = sum(1 for r, cl in past.items() if any(jac(g, x) >= 0.7 for x in cl))
        first = next((r for r, cl in sorted(past.items()) if any(jac(g, x) >= 0.7 for x in cl)), rid)
        best_seed = max((len(set(g) & set(s["glyphs"])) / len(set(g)) for s in seeds), default=0)
        holistic = [f for f in roster_fams if f in per and
                    sum(cs["s"][m]["s4"] - cs["s"][m]["s3"] for m in fit["minds"] if fam.get(m) == f and evid[m] >= MIN_EVID) /
                    max(1, sum(1 for m in fit["minds"] if fam.get(m) == f and evid[m] >= MIN_EVID)) >= 0.5]
        rows.append({"seq": " ".join("=".join(st) for st in c.steps), "n": len(g), "U": U, "coverage": cov, "per": per,
                     "support": sup, "agree": agree, "weakest": [weak[1], weak[0]], "answers": tot, "rounds": rounds_in, "first": first, "witnessed": witnessed,
                     "origin": "seeded" if best_seed >= 0.8 else "emergent", "sets_only": holistic,
                     "score": sup * U * math.sqrt(cov) if len(per) >= 2 else 0.0})
    ranked = sorted(rows, key=lambda r: (-r["score"], -r["n"]))
    L = [f"# Standings after {rid}", "",
         f"*Generated by `harness/seq/standings.py` from `data/rounds/{rid}/fit.json` and the evidence through {rid} "
         f"({fit['n_obs']} triple observations; minds: {', '.join(fit['minds'])}). A running list: each round's version is kept in "
         f"`data/standings/`. Discovery-stage numbers, not claims.*", "",
         "**Columns.**",
         "- **family columns:** perception, the mean over the family's minds of the higher of its triad and set perception. Only minds with at least "
         f"{MIN_EVID} answered triples inside the sequence count; `–` means the family has not been measured on it, not that it doesn't see it.",
         "- **U:** the mean over measured families. **cov:** the share of the roster's families measured.",
         "- **support:** the share of this round's annealing chains and posterior samples holding the sequence.",
         "- **rounds:** how many of the rounds fitted so far found it.",
         "- **witn:** distinct triples answered in its order by at least two answers and a majority.",
         "- **agree:** the share of all answers on its triples that state exactly its order.",
         "- **weakest:** the rung whose triples agree least with the order, and that agreement. A misplaced rung shows up here first; a chain is as good as its weakest link.",
         "- **origin:** whether a seed holds 80% or more of it. Metadata only.",
         "- **sets only:** families that perceive it in sets but not in triads.",
         "- **Rank:** support × U × √cov, among sequences measured in two or more families.", "",
         "| # | sequence | n | " + " | ".join(roster_fams) + " | U | cov | support | rounds | witn | agree | weakest | origin | sets only |",
         "|---|---|---|" + "---|" * len(roster_fams) + "---|---|---|---|---|---|---|---|---|"]
    shown = 0
    for r in ranked:
        if r["score"] <= 0 or shown >= a.top:
            continue
        shown += 1
        seq = r["seq"].replace("|", "\\|")
        L.append(f"| {shown} | `{seq}` | {r['n']} | " + " | ".join(f"{r['per'][f]:.2f}" if f in r["per"] else "–" for f in roster_fams)
                 + f" | {r['U']:.2f} | {r['coverage']:.2f} | {r['support']:.2f} | {r['rounds']}/{len(past)} | {r['witnessed']} | {r['agree']:.2f} ({r['answers']}) | {r['weakest'][0]} {r['weakest'][1]:.2f} | {r['origin']} | "
                 + (", ".join(r["sets_only"]) or "") + " |")
    rest = [r for r in ranked if r["score"] <= 0]
    L += ["", f"{shown} ranked of {len(rows)} sequences in the fit. {len(rest)} are measured in fewer than two families, or have zero support or perception, and are not ranked."]
    out = d / "standings"; out.mkdir(exist_ok=True)
    (out / f"{rid}.md").write_text("\n".join(L) + "\n")
    json.dump(ranked, open(out / f"{rid}.json", "w"), ensure_ascii=False, indent=0)
    if d == EXP / "data":
        (EXP / "STANDINGS.md").write_text("\n".join(L) + "\n")
    print("\n".join(L[:18 + min(45, shown)]))

if __name__ == "__main__":
    main()
