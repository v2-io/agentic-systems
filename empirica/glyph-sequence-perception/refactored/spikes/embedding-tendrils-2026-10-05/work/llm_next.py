#!/usr/bin/env python3
"""A local LLM's next-glyph distribution as a tendril generator (not an embedding: directional and conditional).

For each instance of the reference set, the prompt is  "Symbol sequence: g1 g2 ... gk"  (no trailing space; the
next token normally carries the space) and we read the model's next-token distribution, expanding byte-level
tokens until they complete one UTF-8 character. A glyph's score is the total probability of the token paths that
spell it (after an optional leading space). Output: a ranked candidate list per instance.

  python3 llm_next.py MODE [--gt r011] [--model Qwen/Qwen3-8B]      MODE = ctx (whole context) | node (last glyph only)
-> derived/llm/<model-slug>-<mode>-<gt>.json   {instance_key: [[glyph, prob], ...]}
"""
import argparse, json, time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.models.gpt2.tokenization_gpt2 import bytes_to_unicode
from lib import DER

ap = argparse.ArgumentParser()
ap.add_argument("mode", choices=["ctx", "node"])
ap.add_argument("--gt", default="r011")
ap.add_argument("--model", default="Qwen/Qwen3-8B")
ap.add_argument("--k1", type=int, default=300)
ap.add_argument("--k2", type=int, default=12)
ap.add_argument("--expand", type=int, default=60, help="partial-byte paths expanded per level")
ap.add_argument("--prefix", default="Symbol sequence:")
ap.add_argument("--only-agreed", action="store_true",
                help="only instances with a first-choice proposal agreed by >=2 families (the headline evaluation set)")
a = ap.parse_args()

dev = "mps"
tok = AutoTokenizer.from_pretrained(a.model)
model = AutoModelForCausalLM.from_pretrained(a.model, torch_dtype=torch.bfloat16).to(dev).eval()
b2u = bytes_to_unicode(); u2b = {v: k for k, v in b2u.items()}
VOC = tok.convert_ids_to_tokens(list(range(len(tok))))
def tbytes(i):
    t = VOC[i]
    if t is None:
        return None
    try:
        return bytes(u2b[c] for c in t)
    except KeyError:
        return None          # special / added tokens
TB = [tbytes(i) for i in range(len(VOC))]

def first_char(bs):
    """-> (char or None, complete?) after stripping ONE leading space."""
    if bs.startswith(b" "):
        bs = bs[1:]
    if not bs:
        return None, False
    n = 1 if bs[0] < 0x80 else 2 if bs[0] >> 5 == 0b110 else 3 if bs[0] >> 4 == 0b1110 else 4 if bs[0] >> 3 == 0b11110 else 0
    if n == 0:
        return None, True     # stray continuation byte: dead path
    if len(bs) < n:
        return None, False
    try:
        return bs[:n].decode("utf-8"), True
    except UnicodeDecodeError:
        return None, True

@torch.no_grad()
def next_dist(prefix_ids_list):
    L = max(len(x) for x in prefix_ids_list)
    pad = tok.pad_token_id if tok.pad_token_id is not None else 0
    ids = torch.full((len(prefix_ids_list), L), pad, dtype=torch.long)
    att = torch.zeros_like(ids)
    for i, x in enumerate(prefix_ids_list):          # left padding
        ids[i, L - len(x):] = torch.tensor(x); att[i, L - len(x):] = 1
    out = model(input_ids=ids.to(dev), attention_mask=att.to(dev))
    return torch.softmax(out.logits[:, -1, :].float(), -1).cpu()

def candidates(text):
    base = tok(text, add_special_tokens=False)["input_ids"]
    scores = {}
    frontier = [([], b"", 1.0)]                 # (extra token ids, bytes so far, path prob)
    for depth in range(4):
        if not frontier:
            break
        P = next_dist([base + f[0] for f in frontier])
        nxt = []
        for (ids, bs, p), dist in zip(frontier, P):
            k = a.k1 if depth == 0 else a.k2
            v, ix = dist.topk(k)
            for pv, i in zip(v.tolist(), ix.tolist()):
                b = TB[i]
                if b is None:
                    continue
                nb = bs + b
                ch, done = first_char(nb)
                if ch is not None:
                    scores[ch] = scores.get(ch, 0.0) + p * pv
                elif not done:
                    nxt.append((ids + [i], nb, p * pv))
        frontier = sorted(nxt, key=lambda f: -f[2])[:a.expand]
    return sorted(scores.items(), key=lambda kv: -kv[1])

G = json.load(open(DER / f"gt-{a.gt}.json"))
out_p = DER / "llm" / f"{a.model.split('/')[-1]}-{a.mode}-{a.gt}.json"
out_p.parent.mkdir(exist_ok=True)
res = json.load(open(out_p)) if out_p.exists() else {}
memo = {}
t0 = time.time()
def agreed(I):
    return any(len(set(p["fams_first"]) - {"muse"}) >= 2 for p in I["props"].values())
keys = [k for k in G["instances"] if k not in res and (not a.only_agreed or agreed(G["instances"][k]))]
for n, k in enumerate(keys):
    I = G["instances"][k]
    seq = I["ctx"] if a.mode == "ctx" else [I["node"]]
    text = a.prefix + " " + " ".join(seq)
    if text not in memo:
        memo[text] = [[g, round(p, 8)] for g, p in candidates(text)[:400]]
    res[k] = memo[text]
    if n % 100 == 0:
        print(f"{n}/{len(keys)} {time.time() - t0:.0f}s  {text!r} -> {' '.join(g for g, _ in memo[text][:8])}", flush=True)
        json.dump(res, open(out_p, "w"), ensure_ascii=False)
json.dump(res, open(out_p, "w"), ensure_ascii=False)
print("done", len(res), f"{time.time() - t0:.0f}s")
