#!/usr/bin/env python3
"""Closed protocol on ollama: walk5 triad sheets, glyph-echo + by + ≈ + ⟂,
option-order permuted per item, stateless per call.

Usage: probe5.py [model]  -> results5-<model>.jsonl
"""
import json, random, sys, time, urllib.request

MODEL = sys.argv[1] if len(sys.argv) > 1 else "llama3.2:3b"
random.seed(555)

OPTS = [
    "the symbol itself (copied exactly) - if one immediately feels like it conveys MORE (magnitude, amount, intensity, size, value), and after it a comma and one of: somewhat, much, vastly - how much more it feels",
    "≈ - if they feel comparable and equal on a shared axis",
    "⟂ - if you don't perceive an ordering between them (no shared axis; the comparison would have to be constructed rather than felt)",
]

def prompt(a, b):
    opts = OPTS[:]; random.shuffle(opts)
    lines = "\n".join(f"  - {o}" for o in opts)
    return (f"Two symbols:  {a}   {b}\n\nFirst instinct only. Answer with one of:\n{lines}\n\n"
            f"⟂ is a common, fully valid answer. Answer with ONLY the symbol (plus ', somewhat/much/vastly' if applicable), nothing else.\n\nAnswer:")

def ask(p):
    req = urllib.request.Request("http://localhost:11434/api/generate",
        json.dumps({"model": MODEL, "prompt": p, "stream": False,
                    "options": {"temperature": 0, "num_predict": 30}}).encode(),
        {"Content-Type": "application/json"})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=180) as r:
        out = json.load(r)
    return out["response"], time.time() - t0

def parse(resp, a, b):
    r = resp.strip()
    ans = None
    if "⟂" in r: ans = "⟂"
    elif "≈" in r: ans = "≈"
    else:
        ha, hb = a in r, b in r
        if ha and not hb: ans = a
        elif hb and not ha: ans = b
        elif ha and hb: ans = a if r.find(a) < r.find(b) else b
    by = next((w for w in ("vastly", "much", "somewhat") if w in r.lower()), None)
    return ans, by

out = open(f"results5-{MODEL.replace(':','_')}.jsonl", "w")
for c in range(12):
    sheet = json.load(open(f"walk5-key-{c}.json"))
    for s in sheet:
        resp, dt = ask(prompt(s["a"], s["b"]))
        ans, by = parse(resp, s["a"], s["b"])
        rec = {"chunk": c, "id": s["id"], "triad": s["triad"], "a": s["a"], "b": s["b"],
               "more": ans, "by": by, "raw": resp[:60], "latency": round(dt, 3)}
        out.write(json.dumps(rec, ensure_ascii=False) + "\n"); out.flush()
        print(json.dumps(rec, ensure_ascii=False), flush=True)
out.close()
