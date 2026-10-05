#!/usr/bin/env python3
"""Embed every universe glyph with local ollama embedding models, in several text forms. Cached per (model, form).

  python3 embed.py MODEL [FORM ...]     forms: glyph | name | both     -> derived/emb/<model>__<form>.npy (+ glyphs.json)

glyph = the bare character; name = its Unicode 16 name, lower-cased ("circled digit two");
both  = "② (circled digit two)".
"""
import json, pathlib, sys, time, urllib.request
import numpy as np
from lib import DER, universe, name

EMB = DER / "emb"; EMB.mkdir(exist_ok=True)

def glyph_list():
    p = EMB / "glyphs.json"
    if p.exists():
        return json.load(open(p))
    G = json.load(open(DER / "gt-r011.json"))
    extra = set()
    for I in G["instances"].values():
        extra.update(I["ctx_all"]); extra.update(I["props"])
    for T in G["triads"].values():
        extra.update(T["glyphs"])
    for k in G["orderadj"]:
        extra.update(k)
    try:
        G12 = json.load(open(DER / "gt-r012.json"))
        for I in G12["instances"].values():
            extra.update(I["ctx_all"]); extra.update(I["props"])
        for T in G12["triads"].values():
            extra.update(T["glyphs"])
    except FileNotFoundError:
        pass
    u = universe(extra)
    json.dump(u, open(p, "w"), ensure_ascii=False)
    return u

def text(g, form):
    n = (name(g) or "").lower()
    return {"glyph": g, "name": n, "both": f"{g} ({n})"}[form]

def _call(model, xs):
    body = json.dumps({"model": model, "input": xs, "truncate": True}).encode()
    req = urllib.request.Request("http://localhost:11434/api/embed", body, {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.load(r)["embeddings"]

def _robust(model, xs, depth=0):
    """ollama's runner sometimes resets on a large batch (seen 2026-10-05, all-minilm); retry, then split."""
    for attempt in range(2):
        try:
            return _call(model, xs)
        except Exception as ex:
            print("retry", len(xs), ex, file=sys.stderr); time.sleep(3)
    if len(xs) == 1:
        raise SystemExit(f"embed failed on {xs!r}")
    h = len(xs) // 2
    return _robust(model, xs[:h], depth + 1) + _robust(model, xs[h:], depth + 1)

def embed(model, texts, bs=64):
    out = []
    for i in range(0, len(texts), bs):
        out += _robust(model, texts[i:i + bs])
    return np.array(out, dtype=np.float32)

if __name__ == "__main__":
    model = sys.argv[1]
    forms = sys.argv[2:] or ["glyph", "name"]
    gl = glyph_list()
    for form in forms:
        f = EMB / f"{model.replace(':', '_').replace('/', '_')}__{form}.npy"
        if f.exists():
            print("have", f.name); continue
        t0 = time.time()
        X = embed(model, [text(g, form) for g in gl])
        np.save(f, X)
        print(f"{model} {form}: {X.shape} in {time.time() - t0:.0f}s", flush=True)
