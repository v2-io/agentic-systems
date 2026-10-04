"""Are the edges that ⟂ removes noise, or weak-but-shared signal?
For each frontier judge J and each format-pair that J calls consistent-perp under PERP but consistent-directed
under FORCED (a 'dissolved' edge), compare J's forced winner with every OTHER frontier judge's forced winner on the
same pair (where that judge is cdir under forced). Agreement near 0.5 = the forced edge is idiosyncratic noise;
well above 0.5 = a shared, sub-threshold ordering that ⟂ suppresses. Baseline: the same agreement computed on
pairs J keeps as cdir under perp ('surviving' edges)."""
import collections, itertools
from common import *
FR = ["opus55", "sonnet55", "sonnet5", "haiku45", "sonnet55[sheet]", "grok46[sheet]", "gemini31pro[sheet]", "gemini38flash[sheet]", "gpt56terra[sheet]"]
def verd(run):
    rows, pres = parsed_presentations(run, "format-pairs.jsonl")
    by = collections.defaultdict(dict)
    for pid, st in rows.items(): by[st["pair"]][pid] = st
    out = {}
    for pair, rs in by.items():
        (k, v), = pair_verdicts(rs, {p: pres[p] for p in rs if p in pres}).items()
        out[pair] = (next(iter(rs.values()))["stratum"], v[0], v[1])
    return out
V = {}
for fmt in ("forced", "perp"):
    for run in runs(f"format-{fmt}"):
        V[(judge_of(run), fmt)] = verd(run)
lines = [f"{'judge':22s} {'dissolved n':>11s} {'agree w/ others (forced)':>25s} {'surviving n':>11s} {'agree (forced)':>15s}"]
tot = collections.Counter()
for J in FR:
    if (J, "perp") not in V or (J, "forced") not in V: continue
    perp, forc = V[(J, "perp")], V[(J, "forced")]
    res = {}
    for label, cond in (("dissolved", lambda p: perp[p][1] == "cperp"), ("surviving", lambda p: perp[p][1] == "cdir")):
        a = n = 0; m = 0
        for p in perp:
            if not cond(p) or forc.get(p, (0, 0, 0))[1] != "cdir": continue
            m += 1
            w = forc[p][2]
            for K in FR:
                if K == J or (K, "forced") not in V: continue
                o = V[(K, "forced")].get(p)
                if o and o[1] == "cdir": n += 1; a += o[2] == w
        res[label] = (m, a, n)
        tot[(label, "a")] += a; tot[(label, "n")] += n
    d, s = res["dissolved"], res["surviving"]
    lines.append(f"{J:22s} {d[0]:11d} {d[1]:7d}/{d[2]:5d}={d[1]/d[2] if d[2] else float('nan'):.2f}       {s[0]:11d} {s[1]:5d}/{s[2]:5d}={s[1]/s[2] if s[2] else float('nan'):.2f}")
lines.append(f"pooled: dissolved {tot[('dissolved','a')]}/{tot[('dissolved','n')]}={tot[('dissolved','a')]/tot[('dissolved','n')]:.2f}; surviving {tot[('surviving','a')]}/{tot[('surviving','n')]}={tot[('surviving','a')]/tot[('surviving','n')]:.2f}")
txt = "\n".join(lines); print(txt)
open(ROOT / "reading/tables/manufactured-edges.txt", "w").write(__doc__ + "\n" + txt + "\n")

# cross-FAMILY only (Claude vs non-Claude), so shared training lineage within a family cannot carry the agreement
fam = lambda j: "claude" if any(x in j for x in ("opus", "sonnet", "haiku")) else j.split("[")[0][:4]
ca = cn = sa = sn = 0
for J in FR:
    if (J, "perp") not in V or (J, "forced") not in V: continue
    perp, forc = V[(J, "perp")], V[(J, "forced")]
    for p in perp:
        if forc.get(p, (0, 0, 0))[1] != "cdir": continue
        kind = perp[p][1]
        if kind not in ("cperp", "cdir"): continue
        for K in FR:
            if fam(K) == fam(J) or (K, "forced") not in V: continue
            o = V[(K, "forced")].get(p)
            if o and o[1] == "cdir":
                if kind == "cperp": cn += 1; ca += o[2] == forc[p][2]
                else: sn += 1; sa += o[2] == forc[p][2]
line = f"cross-family only: dissolved {ca}/{cn}={ca/cn:.2f}; surviving {sa}/{sn}={sa/sn:.2f}"
print(line)
open(ROOT / "reading/tables/manufactured-edges.txt", "a").write(line + "\n")
