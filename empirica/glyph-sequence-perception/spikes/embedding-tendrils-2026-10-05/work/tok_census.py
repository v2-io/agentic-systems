#!/usr/bin/env python3
"""How many universe glyphs does each embedding model's tokenizer even SEE? A glyph that tokenizes to [UNK] gets
the same vector as every other unknown glyph, so no embedding of the bare glyph can place it near anything.
Tokenizers fetched from Hugging Face (tokenizer files only). Model ids are the HF originals of the ollama models.
  python3 tok_census.py  -> derived/tok-census.json"""
import json, collections
from transformers import AutoTokenizer
from lib import DER
GL = json.load(open(DER / "emb" / "glyphs.json"))
MODELS = {"all-minilm": "sentence-transformers/all-MiniLM-L6-v2",
          "bge-m3": "BAAI/bge-m3",
          "paraphrase-multilingual": "sentence-transformers/paraphrase-multilingual-mpnet-base-v2",
          "mxbai-embed-large / bge-large": "BAAI/bge-large-en-v1.5",
          "nomic-embed-text": "nomic-ai/nomic-embed-text-v1.5",
          "snowflake-arctic-embed2": "Snowflake/snowflake-arctic-embed-l-v2.0",
          "granite-embedding:30m": "ibm-granite/granite-embedding-30m-english",
          "qwen3-embedding": "Qwen/Qwen3-Embedding-0.6B",
          "embeddinggemma (gemma tokenizer)": "google/embeddinggemma-300m",
          "Qwen3-8B (LLM)": "Qwen/Qwen3-8B"}
out = {}
for k, mid in MODELS.items():
    try:
        t = AutoTokenizer.from_pretrained(mid)
    except Exception as ex:
        out[k] = {"error": str(ex)[:120]}; print(k, "ERR", str(ex)[:100]); continue
    unk = t.unk_token_id
    n_unk = n_one = 0; ntok = collections.Counter()
    for g in GL:
        ids = t(g, add_special_tokens=False)["input_ids"]
        if unk is not None and unk in ids: n_unk += 1
        if len(ids) == 1 and ids[0] != unk: n_one += 1
        ntok[min(len(ids), 5)] += 1
    out[k] = {"hf": mid, "unk_share": n_unk / len(GL), "single_token_share": n_one / len(GL),
              "tokens_per_glyph": dict(sorted(ntok.items()))}
    print(f"{k:34s} UNK {n_unk/len(GL):.2f}   single-token {n_one/len(GL):.2f}   {dict(sorted(ntok.items()))}")
json.dump(out, open(DER / "tok-census.json", "w"), indent=1)
