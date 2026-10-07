"""Writes prereg-flat-splits.json (the strengthening-1 pre-registration), exactly as it was generated on 2026-10-06
17:28 by an inline script (de-novo-feedback-2 §4 asked for the generator to be committed). Model: irt.py variant 2mf
fitted on all continue answers in the snapshot; the flat Sonnet-continues / Grok-stops contexts; each context's
posterior given all its answers; the band from 2,000 draws (seed 7) of the context's component then Bernoulli answers.
  python3 prereg_gen.py [--out FILE]   (default: prints a comparison with the committed file, writes nothing)"""
import argparse, datetime, json, subprocess
import numpy as np
import irt

def generate():
    items, seq, S, N, X = irt.load("continue-stop")
    m = irt.Model(2, True, True).fit(S, N, X)
    M = irt.MINDS; a, b = M.index("sonnet55"), M.index("grok46")
    L = m.comp_loglik(S, N, X); R = np.exp(L - np.logaddexp.reduce(L, axis=1)[:, None])
    flat = [i for i in range(len(items)) if N[i, a] >= 2 and N[i, b] >= 2 and S[i, a] == 0 and S[i, b] == N[i, b]]
    rows = []; rng = np.random.default_rng(7); sims_g = []; sims_s = []
    for i in flat:
        P = m.comp_probs(X[i]); r = R[i]
        rows.append({"context": "".join(items[i][1]), "context_glyphs": list(items[i][1]),
                     "answers_so_far": {mm: [y for _, y in sorted(seq[items[i]][mm])] for mm in seq[items[i]]},
                     "p_stop_next": {mm: round(float(r @ P[:, j]), 3) for j, mm in enumerate(M)},
                     "unfamiliar_last_glyph": int(X[i])})
    for _ in range(2000):
        gs = ss = 0
        for i in flat:
            P = m.comp_probs(X[i]); r = R[i]; k = rng.choice(len(r), p=r / r.sum())
            gs += rng.random() < P[k, b]; ss += rng.random() >= P[k, a]
        sims_g.append(gs / len(flat)); sims_s.append(ss / len(flat))
    q = lambda v: [round(float(np.quantile(v, x)), 3) for x in (0.025, 0.5, 0.975)]
    return {"what": "Pre-registered prediction (family-disagreement spike, strengthening-1): the 43 continue contexts where Sonnet continued every time (>= 2 answers) and Grok stopped every time (>= 2 answers), on the snapshot of 2026-10-06 16:36 (snapshot/manifest.json).",
            "model": "irt.py variant 2mf (2PL mixture with per-mind familiarity), fitted on all continue answers in the snapshot; predictions use each context's posterior given all its answers",
            "written": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
            "git_head_at_writing": subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=str(irt.lib.ROOT)).stdout.strip(),
            "prediction": {"grok46_next_answer_stops_share": {"median_and_95": q(sims_g)},
                           "sonnet55_next_answer_continues_share": {"median_and_95": q(sims_s)}},
            "how_to_check": "Ask each context once more, shown, plain continue question, to sonnet55 and grok46 (fresh sheets). Count the share of Grok's answers that are 'none' and of Sonnet's that continue. A Grok share inside the band supports 'flat splits here are mostly borderline contexts, partly chance'; a share near 1 (above the band) supports 'settled, a stable mind x context difference' and means the calibrated model misses an interaction.",
            "contexts": rows}

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--out"); a = ap.parse_args()
    new = generate()
    if a.out:
        json.dump(new, open(a.out, "w"), ensure_ascii=False, indent=1)
    else:
        old = json.load(open("prereg-flat-splits.json"))
        diff = [k for k in new if k not in ("written", "git_head_at_writing") and new[k] != old.get(k)]
        print("fields differing from the committed file (write time and git head excluded):", diff or "none")
