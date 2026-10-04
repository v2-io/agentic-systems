#!/usr/bin/env python3
"""Exploratory feature-correlate probe: is ladder order LINEARLY readable from off-the-shelf text
embeddings of single glyphs, and is there a family-general 'more' direction?

Tier: exploratory (the probe ladders are analyst-chosen, their orders anecdote-tier; embedding
models are not the judges, so this measures what a representation of the codepoint carries, not
what any judge perceives). Joseph, 2026-08-25: "actual defensible metrics or combinations
(including linear semantic vectors etc.) ... highly correlated with certain sequences or families".

Tests, per embedding model:
  T1 within-family: |Spearman| between family order and the family's first principal component.
     Baseline: same statistic for random same-size glyph sets drawn from the v1.0 uniform tail.
  T2 cross-family transfer: ridge regression embedding -> within-family rank in [0,1], trained on all
     OTHER families, scored by Spearman on the held-out family (leave-one-family-out). Baseline:
     identical pipeline with ranks permuted within each training family (fated, 20 permutations).
Embeddings are cached under ~/.cache/gmp-judges/embeddings/ (derived, disposable).
"""
import json, math, pathlib, random, sys, urllib.request
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "runner"))
from fate import rng

EXP = pathlib.Path(__file__).resolve().parents[2]
CACHE = pathlib.Path.home() / ".cache/gmp-judges/embeddings"; CACHE.mkdir(parents=True, exist_ok=True)
MODELS = ["bge-m3", "qwen3-embedding", "nomic-embed-text", "mxbai-embed-large", "embeddinggemma:300m", "snowflake-arctic-embed2"]

LADDERS = {  # ascending; analyst-chosen probe ladders (pilot-validated or uncontroversial), HYPOTHETICAL labels
    "dice": "⚀⚁⚂⚃⚄⚅", "lower-eighths": "▁▂▃▄▅▆▇█", "left-eighths": "▏▎▍▌▋▊▉", "shade": "░▒▓█",
    "pie": "○◔◑◕●", "moon": "🌑🌒🌓🌔🌕", "disc-size": "·•●⬤", "braille-fill": "⣀⣤⣶⣿",
    "primes": "′″‴⁗", "integrals": "∫∬∭⨌", "rods": "𝍠𝍡𝍢𝍣𝍤", "ogham": "ᚁᚂᚃᚄᚅ",
    "circled": "①②③④⑤⑥⑦⑧⑨⑩", "neg-circled": "❶❷❸❹❺❻❼❽❾❿", "roman": "ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ",
    "roman-lc": "ⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹ", "superscript": "⁰¹²³⁴⁵⁶⁷⁸⁹", "subscript": "₀₁₂₃₄₅₆₇₈₉",
    "eighths": "⅛¼⅜½⅝¾⅞", "cjk": "一二三四五六七八九", "circled-cjk": "㊀㊁㊂㊃㊄㊅㊆㊇㊈",
    "si-length": "㎚㎛㎜㎝㎞", "medals": "🥉🥈🥇", "volume": "🔈🔉🔊", "dots-vert": "․‥…",
    "dot-count": "⁖⁘⁙", "tally-lines": "⚊⚌☰", "sovereign": "䷁䷗䷒䷊䷡䷪䷀", "tone-bars": "˩˨˧˦˥",
    "suzhou": "〡〢〣〤〥〦〧〨〩", "dingbat-sans": "➀➁➂➃➄➅➆➇➈➉",
}

def embed(model, glyphs):
    f = CACHE / f"{model.replace(':', '_')}.json"
    cache = json.load(open(f)) if f.exists() else {}
    need = [g for g in glyphs if g not in cache]
    for i in range(0, len(need), 64):
        chunk = need[i:i + 64]
        req = urllib.request.Request("http://localhost:11434/api/embed",
                                     json.dumps({"model": model, "input": chunk}).encode(), {"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=600) as r:
            out = json.load(r)["embeddings"]
        cache.update(dict(zip(chunk, out)))
    json.dump(cache, open(f, "w"))
    return {g: cache[g] for g in glyphs}

# ---- linear algebra (numpy; analysis-side code, not the stdlib harness)
import numpy as np
def pc1(X):
    X = np.asarray(X, float); Xc = X - X.mean(0)
    _, _, vt = np.linalg.svd(Xc, full_matrices=False)
    return list(Xc @ vt[0])
def rankdata(v, tol=1e-9):
    """average ranks for ties: identical embeddings (exotic glyphs often collapse to one vector) must not
    inherit an order from list position -- the first version of this probe did, and its baselines exposed it."""
    o = sorted(range(len(v)), key=lambda i: v[i]); r = [0.0] * len(v); k = 0
    while k < len(o):
        j = k
        while j + 1 < len(o) and abs(v[o[j + 1]] - v[o[k]]) <= tol * max(1.0, abs(v[o[k]])):
            j += 1
        for t in range(k, j + 1): r[o[t]] = (k + j) / 2.0
        k = j + 1
    return r
def spearman(a, b):
    ra, rb = np.array(rankdata(a)), np.array(rankdata(b))
    ra -= ra.mean(); rb -= rb.mean()
    d = math.sqrt(float((ra ** 2).sum() * (rb ** 2).sum())) or 1.0
    return float((ra * rb).sum()) / d
def ridge_dual(X, y, lam=1.0):
    X = np.asarray(X, float); y = np.asarray(y, float); mu = X.mean(0); Xc = X - mu; yb = y.mean()
    K = Xc @ Xc.T
    alpha = np.linalg.solve(K + lam * np.eye(len(K)), y - yb)
    w = Xc.T @ alpha
    return lambda x: float((np.asarray(x) - mu) @ w + yb)
def mean(v): return sum(v) / len(v)
def unit(v):
    v = np.asarray(v, float); n = np.linalg.norm(v) or 1.0
    return list(v / n)

def main():
    tail = json.load(open(EXP / "data/stimuli-v1/pool.json"))["uniform_tail"]
    fams = {k: list(v) for k, v in LADDERS.items()}
    allg = sorted({g for v in fams.values() for g in v} | set(tail[:200]))
    out = {}
    for model in MODELS:
        E = {g: unit(e) for g, e in embed(model, allg).items()}
        # T1
        t1 = {f: abs(spearman(pc1([E[g] for g in gs]), list(range(len(gs))))) for f, gs in fams.items()}
        base = []
        for k in range(200):
            r = rng("emb", "t1-baseline", {"k": k}); n = r.choice([len(v) for v in fams.values()])
            gs = r.sample(tail[:200], n); base.append(abs(spearman(pc1([E[g] for g in gs]), list(range(n)))))
        # T2
        t2 = {}
        for f, gs in fams.items():
            X, y = [], []
            for f2, gs2 in fams.items():
                if f2 == f: continue
                for i, g in enumerate(gs2):
                    X.append(E[g]); y.append(i / (len(gs2) - 1))
            pred = ridge_dual(X, y, lam=1.0)
            t2[f] = spearman([pred(E[g]) for g in gs], list(range(len(gs))))
        perm_means = []
        for k in range(20):
            vals = []
            for f, gs in fams.items():
                X, y = [], []
                for f2, gs2 in fams.items():
                    if f2 == f: continue
                    ranks = [i / (len(gs2) - 1) for i in range(len(gs2))]
                    rng("emb", "t2-perm", {"k": k, "f": f, "f2": f2}).shuffle(ranks)
                    for g, yy in zip(gs2, ranks):
                        X.append(E[g]); y.append(yy)
                pred = ridge_dual(X, y, lam=1.0)
                vals.append(spearman([pred(E[g]) for g in gs], list(range(len(gs)))))
            perm_means.append(mean(vals))
        distinct = {f: len({tuple(round(x, 6) for x in E[g]) for g in gs}) / len(gs) for f, gs in fams.items()}
        tail_distinct = len({tuple(round(x, 6) for x in E[g]) for g in tail[:200]}) / 200
        out[model] = {"distinct_frac_ladders": round(mean(list(distinct.values())), 3), "distinct_frac_tail": round(tail_distinct, 3),
                      "T1_mean_abs_rho": mean(list(t1.values())), "T1_baseline_mean": mean(base),
                      "T1_baseline_p95": sorted(base)[int(0.95 * len(base))],
                      "T2_mean_rho": mean(list(t2.values())), "T2_perm_means": [round(x, 3) for x in perm_means],
                      "T2_perm_max": max(perm_means), "T1": {k: round(v, 2) for k, v in t1.items()},
                      "T2": {k: round(v, 2) for k, v in t2.items()}}
        print(f"{model:<26} distinct ladder {out[model]['distinct_frac_ladders']:.2f} tail {out[model]['distinct_frac_tail']:.2f} | T1 mean|rho| {out[model]['T1_mean_abs_rho']:.2f} (random sets {out[model]['T1_baseline_mean']:.2f}, p95 {out[model]['T1_baseline_p95']:.2f}) | "
              f"T2 LOFO mean rho {out[model]['T2_mean_rho']:+.2f} (perm max {out[model]['T2_perm_max']:+.2f})", flush=True)
    json.dump(out, open(EXP / "analysis/embed-probe-v0.json", "w"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    main()
