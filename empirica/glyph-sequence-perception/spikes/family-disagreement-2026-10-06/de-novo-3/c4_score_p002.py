"""De novo 3: score p002 under the three pre-registered models and the local-pool baseline (b-pred-p002.json, written
19:31:19, before p002.jsonl was recorded at 19:31:43), per mind, by prereg2_check.py's rule. Also a 'mixture' row:
for each model, the per-context log score difference against the baseline, to see where the losses sit."""
import json, math, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent; SP = HERE.parent; STUDY = SP.parents[1]
pre = json.load(open(SP / "prereg-third-minds.json")); base = json.load(open(HERE / "b-pred-p002.json"))
by = {c["context"]: c for c in pre["contexts"]}
ans = collections.defaultdict(dict)
for l in open(STUDY / "data" / "answers" / "p002.jsonl"):
    r = json.loads(l)
    if r["outcome"] in ("continuation", "none"): ans[r["mind"]]["".join(r["context"])] = int(r["outcome"] == "none")
for m in ("opus55", "haiku45nt", "haiku45"):
    a = ans[m]; ls = {}
    for mo in ("2mf", "irtu", "lnb", "pool"):
        ps = [(base["p_stop"][m][c] if mo == "pool" else by[c]["p_stop"][m][mo]) for c in a]
        ls[mo] = sum(math.log(p if y else 1 - p) for p, y in zip(ps, a.values()))
    # split by whether the mind had its own earlier answers on the context
    own = {c: by[c]["answers_so_far_incl_p001"].get(m, [0, 0])[1] > 0 for c in a}
    sub = {}
    for mo in ("2mf", "irtu", "lnb", "pool"):
        for flag in (True, False):
            cs = [c for c in a if own[c] == flag]
            ps = [(base["p_stop"][m][c] if mo == "pool" else by[c]["p_stop"][m][mo]) for c in cs]
            sub[(mo, flag)] = (sum(math.log(p if a[c] else 1 - p) for p, c in zip(ps, cs)), len(cs), sum(a[c] for c in cs))
    print(f"{m}: stops {sum(a.values())} of {len(a)}; log scores " + "  ".join(f"{k} {v:.2f}" for k, v in ls.items()))
    for flag in (True, False):
        n, k = sub[("pool", flag)][1:]
        print(f"   contexts {'with' if flag else 'without'} the mind's own earlier answers: n={n}, stops {k}; " + "  ".join(f"{mo} {sub[(mo, flag)][0]:.2f}" for mo in ("2mf", "irtu", "lnb", "pool")))
