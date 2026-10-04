#!/usr/bin/env python3
"""Score a synthetic run's fit against the planted truth (PLAN.md §8 step 5).

  validate.py DATA_DIR [RID]

For each planted sequence: the best-matching candidate (glyph Jaccard), whether its order agrees with the
truth on the shared glyphs (share of shared triples with the same middle, ties counted as agreeing either
way), and per-family perception. Also: splices (a candidate holding glyphs private to two planted sequences),
the holistic signature (s4 >> s3), and recovered vs planted nuisance parameters.
"""
import itertools, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import synth as S

def flat(steps):
    return [g for st in steps for g in st]

def pos(steps):
    return {g: i for i, st in enumerate(steps) for g in st}

def order_agree(truth, cand):
    pt, pc = pos(truth), pos(cand)
    shared = [g for g in pt if g in pc]
    n = ok = 0
    for t in itertools.combinations(shared, 3):
        a = sorted(t, key=lambda g: pt[g]); b = sorted(t, key=lambda g: pc[g])
        if len({pt[g] for g in t}) < 3 or len({pc[g] for g in t}) < 3:
            continue
        n += 1; ok += a[1] == b[1]
    return ok / n if n else float("nan"), len(shared)

def main():
    d = pathlib.Path(sys.argv[1])
    rid = sys.argv[2] if len(sys.argv) > 2 else sorted(p.name for p in (d / "rounds").glob("r*"))[-1]
    fit = json.load(open(d / "rounds" / rid / "fit.json"))
    w, minds = S.world_default(), S.minds_default()
    fam = {m: v[0] for m, v in minds.items()}
    cands = fit["best"]["cands"]
    print(f"round {rid}: {len(cands)} candidates, {fit['n_obs']} triple observations\n")
    print("planted | n | best cand | jaccard | order-agree (shared) | per-family max(s3,s4) truth -> fit")
    private = {}
    for k, steps in w["seqs"].items():
        others = set(g for kk, ss in w["seqs"].items() if kk != k for g in flat(ss))
        private[k] = set(flat(steps)) - others
    for k, steps in w["seqs"].items():
        tg = set(flat(steps))
        best = max(range(len(cands)), key=lambda i: len(tg & set(flat(cands[i]["steps"]))) / len(tg | set(flat(cands[i]["steps"]))), default=None)
        if best is None:
            print(f"{k}: no candidates"); continue
        cg = set(flat(cands[best]["steps"]))
        j = len(tg & cg) / len(tg | cg)
        if j == 0:
            print(f"{k} | {len(tg)} | not found"); continue
        oa, ns = order_agree(steps, cands[best]["steps"])
        fams = sorted(set(fam.values()))
        tr = {f: max(max(minds[m][2][k]) for m in minds if fam[m] == f) for f in fams}
        ft = {f: max(max(cands[best]["s"][m]["s3"], cands[best]["s"][m]["s4"]) for m in minds if fam[m] == f) for f in fams}
        s34 = {m: (cands[best]["s"][m]["s3"], cands[best]["s"][m]["s4"]) for m in minds}
        print(f"{k} | {len(tg)} | #{best} {''.join(flat(cands[best]['steps']))} | {j:.2f} | {oa:.2f} ({ns}) | "
              + " ".join(f"{f}:{tr[f]:.2f}->{ft[f]:.2f}" for f in fams))
        if k in w["holistic"]:
            print(f"   holistic: s3/s4 per mind " + " ".join(f"{m}:{a:.2f}/{b:.2f}" for m, (a, b) in s34.items()))
    print("\nsplices (candidates holding private glyphs of two planted sequences):")
    nsp = 0
    for i, c in enumerate(cands):
        cg = set(flat(c["steps"]))
        hit = [k for k in private if len(cg & private[k]) >= 2]
        if len(hit) >= 2:
            nsp += 1; print(f"  #{i} {''.join(flat(c['steps']))}  spans {hit}")
    if not nsp:
        print("  none")
    print("\nnuisance parameters truth -> fit:")
    for m, (f, th, _) in minds.items():
        ft = fit["best"]["theta"].get(m, {})
        print(f"  {m}: " + " ".join(f"{k} {th[k]}->{ft.get(k)}" for k in ("eps", "nn", "nt", "beta", "tau")))

if __name__ == "__main__":
    main()
