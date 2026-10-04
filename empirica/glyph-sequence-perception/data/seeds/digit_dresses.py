#!/usr/bin/env python3
"""Write digit-dresses.jsonl: one lattice seed, dress x value (1-9). Unicode names are used only to enumerate."""
import hashlib, json, pathlib, unicodedata as U
ONES = "1¹₁①⑴⒈❶➀➊⓵１🄂🯱𝟏𝟙𝟣𝟭𝟷"
W = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
cells = {}
for one in ONES:
    for v in range(1, 10):
        ch = str(v) if one == "1" else U.lookup(U.name(one).replace("ONE", W[v - 1]))
        assert U.numeric(ch) == v
        cells[f"{one}|{v}"] = ch
here = pathlib.Path(__file__).parent
rec = {"id": hashlib.sha256(b"seed|digit-dresses|0").hexdigest()[:16], "kind": "lattice",
       "glyphs": list(cells.values()), "factors": {"dress": list(ONES), "value": list(range(1, 10))}, "cells": cells,
       "author": "Joseph (question, 2026-10-04); entered by Claude Opus 5.5", "date": "2026-10-04",
       "origin": "Joseph: are the digit families ordered relative to one another, e.g. ① vs ⑴ vs ❶ vs 🯱 at equal value?",
       "bump": 2.0}
(here / "digit-dresses.jsonl").write_text(json.dumps(rec, ensure_ascii=False) + "\n")
print(len(cells), "glyphs")
