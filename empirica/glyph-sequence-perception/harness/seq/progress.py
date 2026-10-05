#!/usr/bin/env python3
"""Progress per round: is the loop producing more stable sequences, and at what cost?

  progress.py [--data DIR]        -> DIR/PROGRESS.md (and printed); for the real study also <study>/PROGRESS.md

For each round with a fit, using that round's evidence only up to that round:
  calls           sheets answered in that round, across minds (cost)
  presentations   answered presentations in that round, summed over minds
  scheme          the planner that drew the round (plan.json "scheme"; earlier rounds: disagreement-ranked)
  established     supported pieces (>= 3 glyphs, every link and tie witnessed) in the round's best fit
  glyphs          total glyphs in established sequences; longest; mean length
  stable          established sequences measured in >= 2 families with U >= 0.8 (support x U x sqrt(cov) is the standings' rank)
  untested        unsupported links + unwitnessed ties across all candidates (open questions)
  ends open       ends of established sequences not yet closed (see squeue.end_state)
  new             established sequences with no >= 0.7-Jaccard match in the previous round's
Synthetic runs: also planted sequences fully recovered (validate.py's criterion: Jaccard 1.0 and order agreement 1.0).
"""
import argparse, collections, json, math, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from common import EXP, read_jsonl
import model as M
import round as RD
import squeue as Q
import evidence_view as EV

def jac(a, b):
    a, b = set(a), set(b)
    return len(a & b) / max(1, len(a | b))

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--data"); a = ap.parse_args()
    d = pathlib.Path(a.data) if a.data else EXP / "data"
    synth = json.load(open(d / "pool.json")).get("synth")
    fam = RD.family_of(d)
    rows, prev_pieces = [], []
    for rid in [r for r in RD.rounds(d) if (d / "rounds" / r / "fit.json").exists()]:
        fit = json.load(open(d / "rounds" / rid / "fit.json"))
        items, pres, parsed, sheets = RD.load_all(d, upto=rid)
        obs = M.observations(parsed, pres)
        cur = M.from_snapshot(fit["best"], obs, fit["minds"])
        snap = dict(fit["best"], support_list=fit.get("support", []))
        pieces = Q.piece_table(cur, snap, fam)
        ends_open = 0
        for pc in pieces:
            for side in ("right", "left"):
                ends_open += not Q.end_state(pc, side, parsed, pres, items)["closed"]
        untested = 0
        for cid in cur.cands:
            l, t, _ = M.link_support(cur, cur.cands[cid]); untested += len(l) + len(t)
        stab_pcs = [pc for pc in pieces if pc["families"] >= 2 and pc["U"] >= 0.8]
        stable = len(stab_pcs)
        sl = sorted(len(pc["glyphs"]) for pc in stab_pcs)
        buckets = collections.Counter("3" if n == 3 else "4-5" if n <= 5 else "6-7" if n <= 7 else "8-9" if n <= 9 else "10+" for n in sl)
        new = sum(1 for pc in pieces if not any(jac(pc["glyphs"], q) >= 0.7 for q in prev_pieces))
        # the model-free view (evidence_view.py): sequences chained from witnessed triples only
        ev_chains, _, ev_byfam, _ = EV.build(obs, fam)
        fams_all = sorted(set(fam.values()))
        ev_stable = []
        for c in ev_chains:
            per = {}
            for f in fams_all:
                meas = ok = 0
                for t3 in zip(c, c[1:], c[2:]):
                    tal = ev_byfam[tuple(sorted(t3))].get(f)
                    if tal and sum(tal.values()) >= 2:
                        meas += 1; w = EV.witnessed(tal); ok += w is not None and w == ("mid", t3[1])
                if meas:
                    per[f] = ok / meas
            if len(per) >= 2 and sum(per.values()) / len(per) >= 0.8:
                ev_stable.append(len(c))
        mine = [r for r in parsed if r["round"] == rid]
        calls = sum(1 for f in (d / "rounds" / rid / "raw").glob("*/ledger.jsonl") for row in read_jsonl(f)
                    if row["result"].get("raw") and not row["result"].get("error"))
        scheme = json.load(open(d / "rounds" / rid / "plan.json")).get("scheme", "disagreement-ranked")
        lens = [len(pc["glyphs"]) for pc in pieces]
        row = {"round": rid, "scheme": scheme.split(" ")[0], "calls": calls, "presentations": len(mine), "established": len(pieces),
               "glyphs": sum(lens), "longest": max(lens, default=0), "mean_len": (sum(lens) / len(lens)) if lens else 0,
               "stable": stable, "stable_glyphs": sum(sl), "stable_median": sl[len(sl) // 2] if sl else 0,
               "b3": buckets["3"], "b4_5": buckets["4-5"], "b6_7": buckets["6-7"], "b8_9": buckets["8-9"], "b10": buckets["10+"],
               "ev_stable": len(ev_stable), "ev_stable_glyphs": sum(ev_stable),
               "untested": untested, "ends_open": ends_open, "new": new}
        if synth:
            import synth as S
            w = S.world_default()
            ok = 0
            for k, steps in w["seqs"].items():
                tg = [g for st in steps for g in st]
                for pc in pieces:
                    if set(pc["glyphs"]) == set(tg):
                        pt = {g: i for i, st in enumerate(steps) for g in st}
                        pp = {g: i for i, st in enumerate(pc["steps"]) for g in st}
                        import itertools
                        agree = all(sorted(t, key=lambda g: pt[g])[1] == sorted(t, key=lambda g: pp[g])[1]
                                    for t in itertools.combinations(tg, 3)
                                    if len({pt[g] for g in t}) == 3 and len({pp[g] for g in t}) == 3)
                        ok += agree
                        break
            row["planted_recovered"] = f"{ok}/{len(w['seqs'])}"
        rows.append(row)
        prev_pieces = [pc["glyphs"] for pc in pieces]
    cols = ["round", "scheme", "calls", "presentations", "established", "stable", "glyphs", "longest", "mean_len", "untested", "ends_open", "new"] + (["planted_recovered"] if synth else [])
    gcols = ["round", "calls", "stable", "stable_glyphs", "stable_median", "b3", "b4_5", "b6_7", "b8_9", "b10"]
    L = ["# Progress by round", "",
         f"*Generated by `harness/seq/progress.py` from the fits and evidence in `{d}`. "
         "**established:** supported sequences of three or more glyphs. "
         "**stable:** established, measured in two or more families, with perception U ≥ 0.8. "
         "**untested:** open link and tie questions across all candidates. "
         "**ends open:** ends of established sequences still being extended. "
         "**new:** established sequences not in the previous round's fit. "
         "**calls:** sheets answered that round, across minds.*", "",
         "| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for r in rows:
        L.append("| " + " | ".join(f"{r[c]:.1f}" if isinstance(r[c], float) else str(r[c]) for c in cols) + " |")
    L += ["", "## Growth of stable sequences", "",
          "*Stable: established, measured in two or more families, U ≥ 0.8. Counts by length bucket. **stable_glyphs:** total glyphs in stable sequences. **cum calls:** cumulative sheets answered. The line to watch is stable_glyphs against cum calls: is each round still adding stable structure?*", "",
          "The last two columns repeat the count with no likelihood model at all (`evidence_view.py`: sequences chained only from witnessed triples). If both views grow together, the growth is not an artifact of the fit.", "",
          "| round | cum calls | stable | stable_glyphs | median len | len 3 | 4–5 | 6–7 | 8–9 | 10+ | stable (evidence view) | their glyphs |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    cum = 0
    for r in rows:
        cum += r["calls"]
        L.append(f"| {r['round']} | {cum} | {r['stable']} | {r['stable_glyphs']} | {r['stable_median']} | {r['b3']} | {r['b4_5']} | {r['b6_7']} | {r['b8_9']} | {r['b10']} | {r['ev_stable']} | {r['ev_stable_glyphs']} |")
    json.dump(rows, open(d / "progress.json", "w"), indent=0)
    out = "\n".join(L) + "\n"
    (d / "PROGRESS.md").write_text(out)
    if d == EXP / "data":
        (EXP / "PROGRESS.md").write_text(out)
    print(out)

if __name__ == "__main__":
    main()
