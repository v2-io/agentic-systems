#!/usr/bin/env python3
"""Consumer probe stimuli (NOT part of the registered v1.0 program; no predictions attached).

The glyph string below is an old SIGNA sample string: a rough proof-of-concept from an old SIGNA
implementation (zoetica 06-temporal-coherence.md), not SIGNA itself; the builder's brief presented it as the
aspectus age-column ladder. This probe measures, across the
v1.0 judge panel, how that existing ladder is perceived as single glyphs: all pairs both orders (perp
format) and whole-set reconstruction. It says nothing about run-length reading in a column.
"""
import json, pathlib, sys
from itertools import combinations
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from fate import rng, digest
from instruments import PROTOCOL

EXP = pathlib.Path(__file__).resolve().parents[2]
SIGNA = ["·", "╶", "╌", "╍", "━", "═", "⚬", "○", "◎", "◉", "⬤"]

def main():
    out = EXP / "data/stimuli-v1"
    with open(out / "consumer-signa-pairs.jsonl", "w") as f:
        for a, b in combinations(SIGNA, 2):
            for order, (x, y) in enumerate(((a, b), (b, a))):
                row = {"set": "consumer-signa", "seq": "signa", "kind": "consumer-probe", "order": order, "a": x, "b": y,
                       "intended": [SIGNA.index(x), SIGNA.index(y)]}
                row["pid"] = "S" + digest(row)[:12]
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
    with open(out / "consumer-signa-gestalt.jsonl", "w") as f:
        for sh in range(3):
            g = list(SIGNA); rng(PROTOCOL, "gestalt-shuffle", {"seq": "signa", "shuffle": sh}).shuffle(g)
            row = {"set": "gestalt", "seq": "signa", "kind": "consumer-probe", "shuffle": sh, "glyphs": g, "intended": SIGNA,
                   "src": "zoetica 06-temporal-coherence.md §SIGNA (as rendered by aspectus, 2026-10-03)"}
            row["pid"] = "SG" + digest(row)[:12]
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print("consumer-signa: 55 pairs x 2 orders; 3 gestalt shuffles")

if __name__ == "__main__":
    main()
