import collections, unicodedata
from vload import *
def num(g):
    try: return unicodedata.numeric(g) if len(g) == 1 else None
    except Exception: return None
def verd(rid):
    ans = pair_answers(rid); byp = collections.defaultdict(dict)
    for (p, rep), v in ans.items():
        s = STIM[p]; byp[s["pair"]][s["order"]] = (v, s)
    out = {}
    for pair, d in byp.items():
        if 0 in d and 1 in d:
            out[pair] = (verdict_pair(d[0][0], d[1][0], d[0][1]["a"], d[0][1]["b"]), d[0][1])
    return out
J = {}
for r in runs("format-"):
    _, fmt, mode, j = r.split("-", 3)
    lab = j + ("[sheet]" if mode == "sheet" else "")
    if mode == "pilotcond": continue
    J[(lab, fmt)] = verd(r)
FR = ["opus55","sonnet55","sonnet5","haiku45","sonnet55[sheet]","grok46[sheet]","gemini31pro[sheet]","gemini38flash[sheet]"]
fam = lambda j: "claude" if any(x in j for x in ("opus","sonnet","haiku")) else j[:4]
for label, filt in (("all", lambda s: True), ("no-numeric glyph", lambda s: num(s["a"]) is None and num(s["b"]) is None)):
    tot = collections.Counter(); perpair = collections.defaultdict(list)
    for j in FR:
        perp, forc = J[(j,"perp")], J[(j,"forced")]
        for pair, (v, s) in perp.items():
            if not filt(s): continue
            f = forc.get(pair)
            if not f or not (isinstance(f[0], tuple) and f[0][0] == "cdir"): continue
            if not isinstance(v, tuple) or v[0] not in ("cperp", "cdir"): continue
            kind = "diss" if v[0] == "cperp" else "surv"
            for k in FR:
                if fam(k) == fam(j): continue
                o = J[(k,"forced")].get(pair)
                if o and isinstance(o[0], tuple) and o[0][0] == "cdir":
                    tot[(kind,"n")] += 1; tot[(kind,"a")] += o[0][1] == f[0][1]
                    if kind == "diss": perpair[pair].append(o[0][1] == f[0][1])
    print(label, "cross-family dissolved %d/%d=%.2f surviving %d/%d=%.2f" % (tot[("diss","a")], tot[("diss","n")], tot[("diss","a")]/tot[("diss","n")], tot[("surv","a")], tot[("surv","n")], tot[("surv","a")]/tot[("surv","n")]), "distinct dissolved pairs", len(perpair))
    # pair-level: fraction of distinct pairs with majority agreement
    maj = sum(1 for v in perpair.values() if sum(v) > len(v)/2); print("   pairs with majority agreement", maj, "/", len(perpair))
