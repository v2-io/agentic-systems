#!/usr/bin/env python3
"""Magnitude-sequence probe: recoverability + immediacy proxies via ollama.

For each sequence (ordered ascending by my recorded perception), draw stochastic
pairs, present them cold to a model, and score:
  - recoverability: pairwise accuracy vs the recorded order
  - immediacy proxy A: accuracy in 'instinct' mode (one-symbol answer, no room to decode)
  - immediacy proxy B: instinct-vs-think accuracy gap (decode dependence)
  - consistency: agreement across resamples at temperature
  - latency logged per call (weak signal; deliberation tokens inflate think mode)

Usage: probe.py [model] [pairs_per_seq] [samples]  → results JSONL + summary TSV
"""
import json, random, sys, time, urllib.request

MODEL = sys.argv[1] if len(sys.argv) > 1 else "llama3.2:3b"
PAIRS = int(sys.argv[2]) if len(sys.argv) > 2 else 6
SAMPLES = int(sys.argv[3]) if len(sys.argv) > 3 else 3
random.seed(20260825)

# (name, family, sequence ascending per my survey)
SEQS = [
    ("block-ramp",      "fill",     "▁▂▃▄▅▆▇█"),
    ("width-ramp",      "fill",     "▏▎▍▌▋▊▉█"),
    ("shade",           "fill",     "░▒▓█"),
    ("circle-fill",     "fill",     "○◔◑◕●"),
    ("moon",            "fill",     "🌑🌒🌓🌔🌕"),
    ("hexagram-sov",    "fill",     "䷁䷗䷒䷊䷡䷪䷀"),
    ("dice",            "count",    "⚀⚁⚂⚃⚄⚅"),
    ("dot-leaders",     "count",    "․‥…"),
    ("primes",          "count",    "′″‴⁗"),
    ("integrals",       "count",    "∫∬∭⨌"),
    ("braille",         "count",    "⣀⣤⣶⣿"),
    ("volume",          "count",    "🔇🔈🔉🔊"),
    ("ogham",           "count",    "ᚁᚂᚃᚄᚅ"),
    ("rod-numerals",    "count",    "𝍠𝍡𝍢𝍣𝍤"),
    ("disc-size",       "size",     "·•●⬤"),
    ("tone-bars",       "angle",    "˩˨˧˦˥"),
    ("slope-arrows",    "angle",    "↓↘→↗↑"),
    ("digits",          "denoted",  "0123456789"),
    ("circled",         "denoted",  "①②③④⑤⑥⑦⑧⑨⑩"),
    ("roman",           "denoted",  "ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ"),
    ("fractions",       "denoted",  "⅛¼⅜½⅝¾⅞"),
    ("tamil-log",       "denoted",  "௧௰௱௲"),
    ("si-length",       "compiled", "㎚㎛㎜㎝㎞"),
    ("heat",            "compiled", "🟦🟩🟨🟧🟥"),
    ("animals",         "compiled", "🐜🐁🐈🐕🐎🐘🐋"),
    ("age",             "compiled", "👶👦👨👴"),
    ("chess",           "compiled", "♙♘♗♖♕♔"),
    ("valence",         "compiled", "😭😢🙁😐🙂😄😁"),
    ("star-weight",     "star",     "🞯🞰🞱🞲🞳🞴"),
    ("star-fill",       "star",     "⚝☆★"),
    ("asterisk-count",  "star",     "⁎⁑⁂"),
    ("gematria",        "latent",   "אבגדהוזחט"),
    ("greek",           "latent",   "αβγδεζηθι"),
]

INSTINCT = ("You will see two symbols. Which represents MORE — greater magnitude, "
            "amount, intensity, or value? Answer with ONLY '<' or '>' (left<right or "
            "left>right). First instinct. No other text.\n\n{a}  ?  {b}\n\nAnswer:")
THINK = ("You will see two symbols. Which represents MORE — greater magnitude, amount, "
         "intensity, or value? Think briefly, then end your answer with exactly one "
         "line 'FINAL: <' or 'FINAL: >' (left<right or left>right).\n\n{a}  ?  {b}")

def ask(prompt, temp):
    req = urllib.request.Request("http://localhost:11434/api/generate",
        json.dumps({"model": MODEL, "prompt": prompt, "stream": False,
                    "options": {"temperature": temp, "num_predict": 200}}).encode(),
        {"Content-Type": "application/json"})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=180) as r:
        out = json.load(r)
    return out["response"], time.time() - t0, out.get("eval_count", 0)

def parse(resp, mode):
    if mode == "think":
        for line in reversed(resp.strip().splitlines()):
            if "FINAL" in line.upper():
                return ">" if ">" in line else "<" if "<" in line else None
        resp = resp.strip()[-10:]
    for ch in resp:
        if ch in "<>":
            return ch
    return None

results = []
for name, family, seq in SEQS:
    idx_pairs = set()
    while len(idx_pairs) < min(PAIRS, len(seq_l := list(seq)) * (len(seq_l)-1) // 2):
        i, j = random.sample(range(len(seq_l)), 2)
        idx_pairs.add((min(i,j), max(i,j)))
    for (i, j) in idx_pairs:
      for (a, b, truth) in ((seq_l[i], seq_l[j], "<"), (seq_l[j], seq_l[i], ">")):
        for mode, tmpl in (("instinct", INSTINCT), ("think", THINK)):
            for s in range(SAMPLES):
                resp, dt, toks = ask(tmpl.format(a=a, b=b), 0.7 if s else 0.0)
                ans = parse(resp, mode)
                rec = {"seq": name, "family": family, "a": a, "b": b, "gap": j - i,
                       "truth": truth, "mode": mode, "sample": s, "ans": ans,
                       "correct": ans == truth, "latency": round(dt, 3), "toks": toks}
                results.append(rec)
                print(json.dumps(rec, ensure_ascii=False), flush=True)

with open(f"results2-{MODEL.replace(':','_')}.jsonl", "w") as f:
    for r in results:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
