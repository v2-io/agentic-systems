"""Token counts for single glyphs under cached byte-level BPE tokenizers (pure Python; reads tokenizer.json).
A familiarity proxy only: a glyph that is one token was frequent enough in a tokenizer's training text to earn a
merge. Neither tokenizer is that of a study mind (Qwen2.5; the 2023 Claude tokenizer published by Xenova)."""
import json, glob, functools, os

def _b2u():
    bs = list(range(ord("!"), ord("~") + 1)) + list(range(ord("¡"), ord("¬") + 1)) + list(range(ord("®"), ord("ÿ") + 1))
    cs = bs[:]; n = 0
    for b in range(256):
        if b not in bs:
            bs.append(b); cs.append(256 + n); n += 1
    return {b: chr(c) for b, c in zip(bs, cs)}
B2U = _b2u()

class BPE:
    def __init__(self, path):
        j = json.load(open(path))
        m = j["model"]
        self.vocab = m["vocab"]
        merges = m["merges"]
        self.rank = {}
        for i, x in enumerate(merges):
            a, b = x.split(" ") if isinstance(x, str) else x
            self.rank[(a, b)] = i
    @functools.lru_cache(maxsize=None)
    def ntok(self, s):
        parts = [B2U[b] for b in s.encode("utf-8")]
        while len(parts) > 1:
            best = None
            for i in range(len(parts) - 1):
                r = self.rank.get((parts[i], parts[i + 1]))
                if r is not None and (best is None or r < best[0]):
                    best = (r, i)
            if best is None: break
            i = best[1]
            parts = parts[:i] + [parts[i] + parts[i + 1]] + parts[i + 2:]
        return len(parts)

H = os.path.expanduser("~/.cache/huggingface/hub/")
def load(name):
    p = glob.glob(H + f"models--{name}/snapshots/*/tokenizer.json")
    return BPE(p[0]) if p else None

QWEN = load("Qwen--Qwen2.5-7B-Instruct")
CLAUDE23 = load("Xenova--claude-tokenizer")

if __name__ == "__main__":
    for g in "aAé▁▂█①㉄ᖴ𝞣亿億🂬⇒→ᄎ":
        print(g, QWEN.ntok(g) if QWEN else None, CLAUDE23.ntok(g) if CLAUDE23 else None)
