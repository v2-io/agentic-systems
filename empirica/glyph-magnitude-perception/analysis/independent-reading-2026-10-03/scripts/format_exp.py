"""Format experiment (P1-P4), re-derived. Definitions follow PREDICTIONS/PROTOCOL as I read them:
 dissolution (P1) = of pairs consistent-directed under TIE, fraction consistent-perp under PERP (pilot-replication stratum)
 survival (P3)    = of pairs consistent-directed under TIE, fraction still consistent-directed under PERP, per stratum
 value-correlate  = among consistent-directed edges where both glyphs have a UCD numeric value and they differ,
                    fraction won by the larger value
Also reports, per judge x format x stratum, the pair-verdict mix, so the 'format manufactures order' question
can be read directly (cdir rate under forced vs tie vs perp)."""
import collections, unicodedata
from common import *

FRONTIER_CLAUDE = {"haiku45", "sonnet5", "sonnet55", "opus55", "sonnet55[sheet]"}
FRONTIER_OTHER = {"grok46[sheet]", "gpt56terra[sheet]", "gemini31pro[sheet]", "gemini38flash[sheet]"}
SMALL = {"llama32-3b", "gemma3-4b", "phi4mini", "qwen25-3b", "hermes3-3b", "mistral7b"}

def num(ch):
    try: return unicodedata.numeric(ch)
    except Exception: return None

def verdicts(run):
    rows, pres = parsed_presentations(run, "format-pairs.jsonl")
    by = collections.defaultdict(dict)
    for pid, st in rows.items(): by[st["pair"]][pid] = st
    out = {}
    for pair, rs in by.items():
        pv = pair_verdicts(rs, {p: pres[p] for p in rs if p in pres})
        (k, v), = pv.items()
        st = next(iter(rs.values()))
        out[pair] = (st["stratum"], k, v[0], v[1])  # stratum, glyph-set, kind, winner
    pc = collections.Counter(pres[p][-1][0] for p in rows if p in pres)
    return out, pc

data = {}
for fmt in ("forced", "tie", "perp"):
    for run in runs(f"format-{fmt}"):
        j = judge_of(run)
        data[(j, fmt)] = verdicts(run)
# pilot-condition arm
for fmt in ("tie", "perp"):
    run = f"format-{fmt}-pilotcond-sonnetagent"
    if (RUNS / run).exists():
        pass  # different stimulus file (pilotcond); handled in pilotcond.py

judges = sorted({j for j, f in data})
lines = []
P = lines.append
P("FORMAT EXPERIMENT — pair-verdict mix per judge x format (all strata pooled; n = pairs)")
P(f"{'judge':22s} {'fmt':6s} {'n':>4s} {'cdir':>6s} {'cperp':>6s} {'ctie':>6s} {'mixed':>6s} {'flip':>6s} {'incompl':>7s}  presentations-unparsed")
for j in judges:
    for fmt in ("forced", "tie", "perp"):
        if (j, fmt) not in data: continue
        v, pc = data[(j, fmt)]
        c = collections.Counter(x[2] for x in v.values()); n = len(v)
        P(f"{j:22s} {fmt:6s} {n:4d} " + " ".join(f"{c[k]/n:6.2f}" for k in ("cdir", "cperp", "ctie", "mixed", "flip")) + f" {c['incomplete']/n:7.2f}  {pc['unparsed']}/{sum(pc.values())}")
P("")
P("P1 dissolution (pilot-replication): of tie-cdir pairs, fraction cperp under perp   [threshold: Claude >=0.60, other frontier >=0.50]")
P("P3 survival: of tie-cdir pairs, fraction still cdir under perp, by stratum; P3 asks local - mixed >= 0.30 for frontier")
P("P2 small models: perp-presentation ⟂ rate < 0.30 and dissolution < 0.40")
P(f"{'judge':22s} {'P1 diss':>14s} {'[wilson]':>14s} {'surv:local':>11s} {'surv:mixed':>11s} {'surv:pilot':>11s} {'local-mixed':>11s} {'⟂/pres(perp)':>12s}")
for j in judges:
    if (j, "tie") not in data or (j, "perp") not in data: continue
    tie, _ = data[(j, "tie")]; perp, ppc = data[(j, "perp")]
    def surv(stratum, what):
        base = [p for p, x in tie.items() if x[0] == stratum and x[2] == "cdir" and p in perp and perp[p][2] != "incomplete"]
        hit = sum(1 for p in base if perp[p][2] == what)
        return hit, len(base)
    d, dn = surv("pilot-replication", "cperp")
    sl = surv("fresh-seed-local", "cdir"); sm = surv("fresh-mixed", "cdir"); sp = surv("pilot-replication", "cdir")
    f = lambda h: (h[0] / h[1]) if h[1] else float("nan")
    lo, hi = wilson(d, dn)
    pr = ppc["perp"] / sum(ppc.values()) if sum(ppc.values()) else float("nan")
    P(f"{j:22s} {d:3d}/{dn:3d}={d/dn if dn else float('nan'):.2f} [{lo:.2f},{hi:.2f}]   {f(sl):5.2f}({sl[1]:3d}) {f(sm):5.2f}({sm[1]:3d}) {f(sp):5.2f}({sp[1]:3d}) {f(sl)-f(sm):+11.2f} {pr:12.2f}")
P("")
P("P4 value-correlate of committed (cdir) edges, forced vs perp (and tie), all strata pooled")
P(f"{'judge':22s} {'forced':>16s} {'tie':>16s} {'perp':>16s}")
def valcorr(v):
    k = n = 0
    for pair, (s, key, kind, w) in v.items():
        if kind != "cdir": continue
        a, b = tuple(key)
        na, nb = num(a), num(b)
        if na is None or nb is None or na == nb: continue
        n += 1
        if w == (a if na > nb else b): k += 1
    return k, n
for j in judges:
    cells = []
    for fmt in ("forced", "tie", "perp"):
        if (j, fmt) not in data: cells.append(f"{'-':>16s}"); continue
        k, n = valcorr(data[(j, fmt)][0])
        cells.append(f"{k:4d}/{n:4d}={k/n if n else float('nan'):.2f}".rjust(16))
    P(f"{j:22s} " + " ".join(cells))
open(ROOT / "reading/tables/format-exp.txt", "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
