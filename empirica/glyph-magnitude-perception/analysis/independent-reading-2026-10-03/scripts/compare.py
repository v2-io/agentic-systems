"""Place signa among the other authored sequences, using the same scoring for all.

Pairwise score per (sequence, judge), ADJACENT STEPS ONLY (the only unit top-40 has):
  with  = consistent-directed in the author's direction (later rung wins both orders)
  against = consistent-directed against it
  perp  = consistent-perp;  other = mixed/flip/tie/incomplete
Gestalt per (sequence, judge): over the 3 shuffles, mean tau over the glyphs the judge ordered,
coverage = glyphs placed in the main order / set size, n_perp, n_extra_used.
Writes reading/tables/compare-*.tsv and prints a digest."""
import collections, json, statistics as stx
from common import *

OUT = ROOT / "reading/tables"; OUT.mkdir(parents=True, exist_ok=True)


# ---------- sequences: name -> (stimfile, row filter -> key, intended order)
def top40_sequences(fname, setname):
    rows = [json.loads(l) for l in open(STIM / fname)]
    seqs = collections.defaultdict(list)
    for r in rows: seqs[r["cand"]].append(r)
    return seqs

cands = {c["cand"]: c for c in json.load(open(STIM / "top40-candidates.json"))["candidates"]}

def step_scores(run, fname, groupkey, intended_of):
    rows, pres = parsed_presentations(run, fname)
    # group rows by sequence
    by = collections.defaultdict(dict)
    for pid, st in rows.items():
        by[groupkey(st)][pid] = st
    out = {}
    for seq, rs in by.items():
        order = intended_of(seq)
        adj = {frozenset(p) for p in zip(order, order[1:])}
        pv = pair_verdicts(rs, {p: pres[p] for p in rs if p in pres})
        c = collections.Counter()
        for k, (kind, w, _) in pv.items():
            if k not in adj: continue
            if kind == "cdir":
                lo, hi = sorted(k, key=order.index)
                c["with" if w == hi else "against"] += 1
            elif kind == "cperp": c["perp"] += 1
            else: c["other"] += 1
        c["n"] = sum(1 for k in pv if k in adj)
        out[seq] = c
    return out

def gestalt_scores(run, fname, seqkey):
    rows = stim_rows(fname)
    by = collections.defaultdict(list)
    for r in ledger(run):
        st = rows[r["pids"][0]]
        raw = r["result"].get("raw")
        if not raw or r["result"].get("error"): continue
        by[seqkey(st)].append((st, I.parse_gestalt(raw, st["glyphs"])))
    out = {}
    for seq, lst in by.items():
        taus, cov, nperp, nextra, norder = [], [], 0, 0, 0
        for st, g in lst:
            if g["kind"] == "perp": nperp += 1; continue
            if g["kind"] != "order": continue
            norder += 1
            t, n = kendall_tau(g["order"], st["intended"])
            if t is not None: taus.append(abs(t))
            cov.append(len(set(g["order"]) & set(st["intended"])) / len(set(st["intended"])))
            if g["extra"]: nextra += 1
        out[seq] = dict(n=len(lst), norder=norder, nperp=nperp, nextra=nextra,
                        tau=stx.mean(taus) if taus else None, cov=stx.mean(cov) if cov else None)
    return out

pair_rows = []; gest_rows = []
# top-40 a and b
for pref, fname, gpref, gfname in (("top40-perp", "top40-steps.jsonl", "top40-gestalt", "top40-gestalt.jsonl"),
                                   ("top40b-perp", "top40b-steps.jsonl", "top40b-gestalt", "top40b-gestalt.jsonl")):
    for run in runs(pref):
        sc = step_scores(run, fname, lambda st: st["cand"], lambda c: cands[c]["glyphs"])
        for seq, c in sc.items():
            pair_rows.append(("top40", f"cand-{seq}", "".join(cands[seq]["glyphs"]), cands[seq]["n_surveyors"], judge_of(run), c))
    for run in runs(gpref):
        for seq, g in gestalt_scores(run, gfname, lambda st: st["seq"]).items():
            ci = int(seq.split("-")[1])
            gest_rows.append(("top40", seq, "".join(cands[ci]["glyphs"]), cands[ci]["n_surveyors"], judge_of(run), g))
# holistic sets (class A/B) pairs + gestalt
hol = {s["name"]: s for s in json.load(open(ROOT / "harness/runner/holistic-sets-v1.json"))["sets"]}
for run in runs("holistic-perp"):
    sc = step_scores(run, "holistic-pairs.jsonl", lambda st: st["seq"],
                     lambda s: hol[s]["order"] if s in hol else None)
    for seq, c in sc.items():
        if seq in hol:
            pair_rows.append(("holistic", seq, "".join(hol[seq]["order"]), hol[seq]["kind"], judge_of(run), c))
for run in runs("gestalt-gestalt"):
    for seq, g in gestalt_scores(run, "gestalt.jsonl", lambda st: st["seq"]).items():
        gest_rows.append(("holistic", seq, "".join(hol[seq]["order"]) if seq in hol else "(noise)", hol.get(seq, {}).get("kind", "noise-foil"), judge_of(run), g))
# signa
for run in runs("signa-perp"):
    sc = step_scores(run, "consumer-signa-pairs.jsonl", lambda st: "signa", lambda s: SIGNA)
    pair_rows.append(("signa", "signa", "".join(SIGNA), "human-authored (C)", judge_of(run), sc["signa"]))
for run in runs("signa-gestalt"):
    for seq, g in gestalt_scores(run, "consumer-signa-gestalt.jsonl", lambda st: "signa").items():
        gest_rows.append(("signa", "signa", "".join(SIGNA), "human-authored (C)", judge_of(run), g))

with open(OUT / "compare-steps.tsv", "w") as f:
    f.write("family\tseq\tglyphs\tinfo\tjudge\tn_steps\twith\tagainst\tperp\tother\n")
    for fam, seq, gl, info, j, c in pair_rows:
        f.write(f"{fam}\t{seq}\t{gl}\t{info}\t{j}\t{c['n']}\t{c['with']}\t{c['against']}\t{c['perp']}\t{c['other']}\n")
with open(OUT / "compare-gestalt.tsv", "w") as f:
    f.write("family\tseq\tglyphs\tinfo\tjudge\tn\tn_order\tn_perp\tn_extra\tmean_abs_tau\tmean_coverage\n")
    for fam, seq, gl, info, j, g in gest_rows:
        f.write(f"{fam}\t{seq}\t{gl}\t{info}\t{j}\t{g['n']}\t{g['norder']}\t{g['nperp']}\t{g['nextra']}\t"
                f"{'' if g['tau'] is None else round(g['tau'],3)}\t{'' if g['cov'] is None else round(g['cov'],3)}\n")

# ---------- digest: per judge, signa's step-with rate vs the distribution over top-40 sequences
print("ADJACENT-STEP 'with author' fraction: signa vs top-40 survey sequences (same judge)")
byj = collections.defaultdict(list)
for fam, seq, gl, info, j, c in pair_rows:
    if c["n"]: byj[j].append((fam, seq, gl, c["with"] / c["n"], c["perp"] / c["n"], c["against"] / c["n"]))
for j in sorted(byj):
    t = [x for x in byj[j] if x[0] == "top40"]; s = [x for x in byj[j] if x[0] == "signa"]
    if not t or not s: continue
    sw = s[0][3]
    below = sum(1 for x in t if x[3] < sw); eq = sum(1 for x in t if x[3] == sw)
    print(f"  {j:22s} signa with={sw:.2f} perp={s[0][4]:.2f} against={s[0][5]:.2f} | top40 n={len(t)} median with={stx.median(x[3] for x in t):.2f}"
          f" mean={stx.mean(x[3] for x in t):.2f}  signa percentile={(below + eq/2)/len(t):.2f}")
print("\nGESTALT mean |tau| and coverage: signa vs top-40 (same judge)")
byg = collections.defaultdict(list)
for fam, seq, gl, info, j, g in gest_rows:
    byg[j].append((fam, seq, g))
for j in sorted(byg):
    t = [g for fam, seq, g in byg[j] if fam == "top40" and g["tau"] is not None]
    s = [g for fam, seq, g in byg[j] if fam == "signa"]
    if not t or not s: continue
    s = s[0]
    print(f"  {j:22s} signa tau={s['tau']} cov={s['cov']} extra={s['nextra']}/{s['n']} perp={s['nperp']} | top40 n={len(t)}"
          f" median tau={stx.median(g['tau'] for g in t):.2f} median cov={stx.median(g['cov'] for g in t):.2f}"
          f" extra-used seqs={sum(1 for g in t if g['nextra'])}")
