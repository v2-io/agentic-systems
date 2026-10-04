#!/usr/bin/env python3
"""Stimuli for the 'dress' follow-up to the coordinator's 'ones' probe (exploratory; not a v1.0 instrument).

The 18 digit 'dresses' of the ones probe (plain, superscript, subscript, circled, parenthesized, full stop,
negative circled, dingbat circled sans, dingbat negative circled sans, double circled, fullwidth, comma,
segmented, math bold, double-struck, sans, sans bold, monospace), each taken at other values.
Unicode names are used only to ENUMERATE the stimuli, never as data.

  dress-pairs.jsonl
    slice "same-4", "same-8": every dress pair at equal value (153 each)   -> is the dress order value-invariant?
    slice "cross-4-5": for every unordered dress pair (A,B): A(4) vs B(5) and B(4) vs A(5)  (306)
                       -> does a dress difference ever outweigh a one-step value difference?
    every pair in both orders.
  dress-gestalt.jsonl: the 18 eights, 3 fated shuffles.

usage: dress_stimuli.py ROOT   (writes ROOT/data/stimuli-v1/dress-*.jsonl; ROOT has harness/runner)
"""
import json, pathlib, sys, unicodedata as U
from itertools import combinations
ROOT = pathlib.Path(sys.argv[1])
sys.path.insert(0, str(ROOT / "harness/runner"))
from fate import rng, digest
TAG = "gmp-dress-0.1"
ONES = "1¹₁①⑴⒈❶➀➊⓵１🄂🯱𝟏𝟙𝟣𝟭𝟷"
WORD = {1: "ONE", 4: "FOUR", 5: "FIVE", 8: "EIGHT"}

def at(one, v):
    if one == "1": return str(v)
    name = U.name(one).replace("ONE", WORD[v])
    ch = U.lookup(name)
    assert U.numeric(ch) == v, (one, v, name)
    return ch

dress = {one: {v: at(one, v) for v in (4, 5, 8)} for one in ONES}
rows = []
def add(slice_, a, b, da, db):
    for order, (x, y) in enumerate(((a, b), (b, a))):
        r = {"set": "dress", "slice": slice_, "order": order, "a": x, "b": y,
             "dress_a": da if order == 0 else db, "dress_b": db if order == 0 else da}
        r["pid"] = "D" + digest({"tag": TAG, **r})[:12]
        rows.append(r)
for v in (4, 8):
    for A, B in combinations(ONES, 2):
        add(f"same-{v}", dress[A][v], dress[B][v], A, B)
for A, B in combinations(ONES, 2):
    add("cross-4-5", dress[A][4], dress[B][5], A, B)
    add("cross-4-5", dress[B][4], dress[A][5], B, A)
out = ROOT / "data/stimuli-v1"
with open(out / "dress-pairs.jsonl", "w") as f:
    for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")
eights = [dress[o][8] for o in ONES]
with open(out / "dress-gestalt.jsonl", "w") as f:
    for sh in range(3):
        g = list(eights); rng(TAG, "dress-gestalt-shuffle", {"shuffle": sh}).shuffle(g)
        r = {"set": "gestalt", "seq": "eights", "kind": "dress", "shuffle": sh, "glyphs": g, "intended": eights}
        r["pid"] = "DG" + digest({"tag": TAG, **r})[:12]
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(rows), "presentations;", " ".join(eights))
