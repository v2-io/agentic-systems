import collections, sys
from vload import *

def pair_verdicts(rid):
    ans = pair_answers(rid)
    byp = collections.defaultdict(dict)
    for (p, rep), v in ans.items():
        s = STIM[p]
        if s.get("set") != "format": continue
        byp[s["pair"]][s["order"]] = (v, s)
    out = {}
    for pair, d in byp.items():
        if 0 in d and 1 in d:
            (v0, s0), (v1, s1) = d[0], d[1]
            out[pair] = (verdict_pair(v0, v1, s0["a"], s0["b"]), s0["stratum"])
        else:
            out[pair] = ("missing", (d.get(0) or d.get(1))[1]["stratum"])
    return out, ans

judges = sorted({r.split("-",3)[3] for r in runs("format-")} )
modes = {}
for r in runs("format-"):
    _, fmt, mode, j = r.split("-", 3)
    modes.setdefault((j, mode), {})[fmt] = r

print("judge mode | P1 tie-cdir->perp-cperp (pilot-rep) | perp rate pres (pilot-rep) | unparsed perp | cdir share forced/tie/perp all strata | P3 surv local - mixed")
for (j, mode), fm in sorted(modes.items()):
    V = {f: pair_verdicts(r) for f, r in fm.items()}
    line = f"{j:14s} {mode:9s}"
    if "tie" in V and "perp" in V:
        tv, _ = V["tie"]; pv, pans = V["perp"]
        num = den = 0
        for pair, (v, st) in tv.items():
            if st != "pilot-replication": continue
            if isinstance(v, tuple) and v[0] == "cdir":
                pvv = pv.get(pair, ("missing", st))[0]
                if pvv in ("missing",): continue
                den += 1; num += isinstance(pvv, tuple) and pvv[0] == "cperp"
        p, lo, hi = wilson(num, den)
        line += f" P1 {num}/{den}={p:.2f} [{lo:.2f},{hi:.2f}]"
        # P1 alt: exclude pairs where perp unparsed
        num2 = den2 = 0
        for pair, (v, st) in tv.items():
            if st != "pilot-replication": continue
            if isinstance(v, tuple) and v[0] == "cdir":
                pvv = pv.get(pair, ("missing", st))[0]
                if not isinstance(pvv, tuple): continue
                den2 += 1; num2 += pvv[0] == "cperp"
        line += f" (parsed-only {num2}/{den2}={num2/max(den2,1):.2f})"
        # P3: survival = among tie-cdir pairs (per stratum), fraction still cdir same winner under perp
        surv = {}
        for stratum in ("fresh-seed-local", "fresh-mixed"):
            n = k = 0
            for pair, (v, st) in tv.items():
                if st != stratum or not (isinstance(v, tuple) and v[0] == "cdir"): continue
                pvv = pv.get(pair, ("missing",))[0]
                if not isinstance(pvv, tuple): continue
                n += 1; k += pvv[0] == "cdir"
            surv[stratum] = (k, n)
        a = surv["fresh-seed-local"]; b = surv["fresh-mixed"]
        line += f" | P3(tie-base) {a[0]}/{a[1]} vs {b[0]}/{b[1]} diff {a[0]/max(a[1],1)-b[0]/max(b[1],1):+.2f}"
    if "perp" in V:
        pv, pans = V["perp"]
        cnt = collections.Counter()
        for (p, rep), v in pans.items():
            if STIM[p]["stratum"] == "pilot-replication": cnt[v[0]] += 1
        tot = sum(cnt.values())
        line += f" | perp-pres pilotrep perp={cnt['perp']}/{tot}={cnt['perp']/max(tot,1):.2f} unp={cnt['unparsed']}"
        # small-local: ⟂ on all perp presentations
        call = collections.Counter(v[0] for v in pans.values()); tall = sum(call.values())
        line += f" all-perp={call['perp']/max(tall,1):.2f} unp={call['unparsed']}/{tall}"
    sh = []
    for f in ("forced", "tie", "perp"):
        if f in V:
            vv = V[f][0]
            c = sum(1 for v, st in vv.values() if isinstance(v, tuple) and v[0] == "cdir")
            sh.append(f"{f[0]}{c/max(len(vv),1):.2f}(n{len(vv)})")
    line += " | cdir " + " ".join(sh)
    print(line)
