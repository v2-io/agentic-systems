#!/usr/bin/env python3
"""Audit checks on the exploratory embedding probe (doc §4), 2026-10-03.

Reads the cached embeddings READ-ONLY (never calls ollama, never rewrites the cache) and re-implements
the LOFO ridge + Spearman independently. Adds three checks the original does not run:
  L  leakage: glyphs shared between ladders (a held-out ladder's glyph present in training);
     LOFO re-run with every held-out glyph removed from the training set.
  CP codepoint direction, tested directly: train on all 31 ladders, then score how well the learned
     'more' direction orders random uniform-tail glyph sets BY CODEPOINT (pseudo-ladders with no
     magnitude). A codepoint-carrying direction would give mean rho >> 0 here.
  NN the numeric->non-numeric transfer split by mechanism (fill / size / count / other), because the
     original's non-numeric side includes number-denoting count ladders (dice etc.).
"""
import json, math, pathlib, random, sys
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "harness/correlates"))
EXP = pathlib.Path(__file__).resolve().parents[2]
CACHE = pathlib.Path.home() / ".cache/gmp-judges/embeddings"
LADDERS = None
src = (EXP / "harness/correlates/embed_probe.py").read_text()
ns = {}
exec(src[src.index("LADDERS = {"):src.index("def embed(")], ns)   # take the ladder table verbatim, nothing else
LADDERS = {k: list(v) for k, v in ns["LADDERS"].items()}
TAIL = json.load(open(EXP / "data/stimuli-v1/pool.json"))["uniform_tail"][:200]

def load(model):
    c = json.load(open(CACHE / f"{model.replace(':', '_')}.json"))
    out = {}
    for g, e in c.items():
        v = np.asarray(e, float); n = np.linalg.norm(v); out[g] = v / (n or 1.0)
    return out

def avg_ranks(x):
    x = np.asarray(x, float); o = np.argsort(x, kind="stable"); r = np.empty(len(x)); i = 0
    while i < len(x):
        j = i
        while j + 1 < len(x) and abs(x[o[j + 1]] - x[o[i]]) <= 1e-9 * max(1.0, abs(x[o[i]])): j += 1
        r[o[i:j + 1]] = (i + j) / 2.0; i = j + 1
    return r

def rho(a, b):
    ra, rb = avg_ranks(a), avg_ranks(b); ra -= ra.mean(); rb -= rb.mean()
    d = math.sqrt((ra ** 2).sum() * (rb ** 2).sum())
    return float((ra * rb).sum() / d) if d else 0.0

def fit(X, y, lam=1.0):
    X = np.asarray(X); y = np.asarray(y, float); mu = X.mean(0); Xc = X - mu
    a = np.linalg.solve(Xc @ Xc.T + lam * np.eye(len(X)), y - y.mean())
    w = Xc.T @ a; b = y.mean()
    return lambda Z: (np.asarray(Z) - mu) @ w + b

def lofo(E, exclude_shared=False):
    res = {}
    for f, gs in LADDERS.items():
        X, y = [], []
        for f2, gs2 in LADDERS.items():
            if f2 == f: continue
            for i, g in enumerate(gs2):
                if exclude_shared and g in gs: continue
                X.append(E[g]); y.append(i / (len(gs2) - 1))
        p = fit(X, y)([E[g] for g in gs])
        res[f] = rho(p, range(len(gs)))
    return res

shared = {}
for f, gs in LADDERS.items():
    for f2, gs2 in LADDERS.items():
        if f2 != f:
            for g in set(gs) & set(gs2):
                shared.setdefault(g, set()).update({f, f2})
print("glyphs shared between ladders:", {g: sorted(v) for g, v in shared.items()})

MECH = {"fill": ["lower-eighths", "left-eighths", "shade", "pie", "moon", "braille-fill", "sovereign"],
        "size": ["disc-size"],
        "count (number-denoting or tally)": ["dice", "primes", "integrals", "ogham", "dot-count", "tally-lines", "dots-vert", "volume"],
        "other": ["medals", "tone-bars"]}
NUMERIC = {"circled", "neg-circled", "roman", "roman-lc", "superscript", "subscript", "eighths", "cjk",
           "circled-cjk", "suzhou", "dingbat-sans", "rods", "si-length"}

for model in ("qwen3-embedding", "embeddinggemma:300m", "snowflake-arctic-embed2", "bge-m3"):
    E = load(model)
    base = lofo(E); clean = lofo(E, exclude_shared=True)
    print(f"\n{model}: LOFO mean rho {np.mean(list(base.values())):+.3f}; "
          f"with held-out glyphs removed from training {np.mean(list(clean.values())):+.3f}  "
          f"(changed: { {f: (round(base[f],2), round(clean[f],2)) for f in base if abs(base[f]-clean[f])>1e-6} })")
    # CP: does the all-ladder 'more' direction order codepoint-sorted random sets?
    X, y = [], []
    for gs in LADDERS.values():
        for i, g in enumerate(gs): X.append(E[g]); y.append(i / (len(gs) - 1))
    pred = fit(X, y)
    rnd = random.Random(20261003); sizes = [len(v) for v in LADDERS.values()]; vals = []
    for _ in range(500):
        gs = sorted(rnd.sample(TAIL, rnd.choice(sizes)), key=lambda g: ord(g[0]))
        vals.append(rho(pred([E[g] for g in gs]), range(len(gs))))
    tail_cp = rho(pred([E[g] for g in TAIL]), [ord(g[0]) for g in TAIL])
    print(f"   CP: mean rho of the ladder direction on 500 codepoint-sorted random tail sets {np.mean(vals):+.3f} "
          f"(sd {np.std(vals):.2f}); rho(prediction, codepoint) over the 200 tail glyphs {tail_cp:+.3f}")
    # NN: numeric-trained direction on non-numeric ladders, by mechanism
    X, y = [], []
    for f in NUMERIC:
        gs = LADDERS[f]
        for i, g in enumerate(gs): X.append(E[g]); y.append(i / (len(gs) - 1))
    pn = fit(X, y)
    for mech, fams in MECH.items():
        r = {f: round(rho(pn([E[g] for g in LADDERS[f]]), range(len(LADDERS[f]))), 2) for f in fams}
        print(f"   numeric->{mech}: mean {np.mean(list(r.values())):+.2f} {r}")
