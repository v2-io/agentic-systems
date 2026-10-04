"""Triads (P5-P8) re-derived.
 cycle rate (P5)  = 3-cycles / fully-oriented orientation sets (all three presentations directed), per judge
 ⟂ rate (P6)      = ⟂ presentations / parsed presentations, uniform stratum
 value-corr (P7)  = over consistent-directed pairs (both orientation sets name the same winner) where both glyphs
                    have differing UCD numeric values: fraction won by the larger value
 ink-corr (P8)    = over consistent-directed pairs, neither glyph numeric, both in the Ghostty BMP table with
                    packed_density differing by > 0.005: fraction won by the denser glyph
Also: the same correlates computed on SINGLE presentations (not requiring both orders), as a sensitivity check."""
import collections, os, unicodedata
from common import *

def num(ch):
    try: return unicodedata.numeric(ch)
    except Exception: return None

INK = {}
for line in open(os.path.expanduser("~/src/arch/firmatum/utils/utf/bmp-metrics-ghostty.tsv")):
    p = line.rstrip("\n").split("\t")
    if p[0].isdigit():
        try: INK[chr(int(p[0]))] = float(p[12])
        except Exception: pass

rows_all = stim_rows("triads.jsonl")
out = []; P = out.append
P(f"{'judge':22s} {'cyc/full':>10s} {'rate':>5s} {'[wilson]':>13s}  {'⟂unif':>6s} {'⟂xseed':>6s} {'⟂local':>6s}  {'value-corr':>14s} {'ink-corr':>14s}  {'unparsed':>8s}")
summary = {}
for run in runs("triads-perp"):
    j = judge_of(run)
    rows, pres = parsed_presentations(run, "triads.jsonl")
    last = {pid: v[-1] for pid, v in pres.items()}
    # orientation sets
    sets = collections.defaultdict(list)
    for pid, st in rows.items(): sets[(st["triad"], st["oset"])].append(pid)
    full = cyc = 0
    for key, pids in sets.items():
        vs = [last.get(p) for p in pids]
        if len(pids) == 3 and all(v and v[0] == "dir" for v in vs):
            full += 1
            wins = collections.Counter(v[1] for v in vs)
            if max(wins.values()) == 1: cyc += 1
    lo, hi = wilson(cyc, full)
    # ⟂ by stratum
    pr = {}
    for s in ("uniform", "seed-cross", "seed-local"):
        vs = [last[p] for p, st in rows.items() if st["stratum"] == s and p in last and last[p][0] != "unparsed"]
        pr[s] = sum(v[0] == "perp" for v in vs) / len(vs) if vs else float("nan")
    # pair verdicts across the two orientation sets
    byp = collections.defaultdict(dict)
    for pid, st in rows.items():
        byp[(st["triad"], frozenset((st["a"], st["b"])))][st["oset"]] = last.get(pid, ("missing", None, None, None))
    vk = vn = ik = inn = 0
    for (t, k), d in byp.items():
        v0, v1 = d.get(0), d.get(1)
        if not v0 or not v1 or v0[0] != "dir" or v1[0] != "dir" or v0[1] != v1[1]: continue
        w = v0[1]; a, b = tuple(k); l = b if w == a else a
        na, nb = num(w), num(l)
        if na is not None and nb is not None:
            if na != nb: vn += 1; vk += na > nb
        elif na is None and nb is None and w in INK and l in INK and abs(INK[w] - INK[l]) > 0.005:
            inn += 1; ik += INK[w] > INK[l]
    unp = sum(1 for v in last.values() if v[0] == "unparsed")
    summary[j] = dict(cyc=cyc, full=full, pr=pr, vk=vk, vn=vn, ik=ik, inn=inn)
    P(f"{j:22s} {cyc:4d}/{full:4d} {cyc/full if full else float('nan'):5.2f} [{lo:.2f},{hi:.2f}]  {pr['uniform']:6.2f} {pr['seed-cross']:6.2f} {pr['seed-local']:6.2f}  "
      f"{vk:4d}/{vn:4d}={vk/vn if vn else float('nan'):.2f} {ik:4d}/{inn:4d}={ik/inn if inn else float('nan'):.2f}  {unp:4d}/{len(last)}")
txt = "TRIADS (P5-P8)\n" + "\n".join(out)
print(txt); open(ROOT / "reading/tables/triads.txt", "w").write(txt + "\n")
