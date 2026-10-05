#!/usr/bin/env python3
"""Same as embed.py, but through sentence-transformers on MPS (ollama's /api/embed ran at ~25 texts/s here,
which made the 25k-glyph universe x several models impractical).

  python3 embed_hf.py HF_MODEL [FORM ...]    -> derived/emb/hf-<slug>__<form>.npy
"""
import sys, time
import numpy as np
from sentence_transformers import SentenceTransformer
from embed import EMB, glyph_list, text

model_id = sys.argv[1]
forms = sys.argv[2:] or ["glyph", "name"]
slug = "hf-" + model_id.split("/")[-1]
m = SentenceTransformer(model_id, device="mps")
gl = glyph_list()
for form in forms:
    f = EMB / f"{slug}__{form}.npy"
    if f.exists():
        print("have", f.name); continue
    t0 = time.time()
    X = m.encode([text(g, form) for g in gl], batch_size=256, normalize_embeddings=True, show_progress_bar=False)
    np.save(f, X.astype(np.float32))
    print(f"{slug} {form}: {X.shape} in {time.time() - t0:.0f}s", flush=True)
