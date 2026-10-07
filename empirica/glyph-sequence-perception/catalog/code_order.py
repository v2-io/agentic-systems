#!/usr/bin/env python3
"""Whether the encoding supplies a run's order: shared by the catalog build (build 6, record field code_order) and the
planner (stochastic-5, ENCODED_RELEVANCE), so the two can't drift apart. Joseph, 2026-10-06: "so many of these are
basically just snippets of the unicode spec"; "Far too many resources spent in the end on 'given' sequences with their
known trivial permutations and snippets of the unicode panes."
"""
import functools

# A run counts as encoded when all its glyphs are in ONE Unicode block -- one pane of the code charts -- and its code
# points run monotone (gaps and strides allowed), rotated, or interleaved. Joseph: "snippets of the unicode panes"; his
# examples (`ȞȟȡȣȤ…`, `ԘԚԜ…`, `SrQp…`) skip code points or stride, within one block. Runs across blocks don't count:
# CATALOG §7a measured that minds follow chart order no better than chance across blocks (planner stochastic-5 audit,
# P1, 2026-10-06), so a ladder like -=≡≣ or ☆⭐🌟 that rises through several blocks is the minds' own order.

import bisect, pathlib

_BLOCKS = []
for _l in open(pathlib.Path(__file__).resolve().parents[1] / "data" / "unicode" / "Blocks-16.0.0.txt", encoding="utf-8"):
    _l = _l.split("#")[0].strip()
    if _l:
        _r, _n = _l.split(";")
        _a, _b = _r.split("..")
        _BLOCKS.append((int(_a, 16), int(_b, 16), _n.strip()))
_STARTS = [a for a, _, _ in _BLOCKS]

def block(ch):
    i = bisect.bisect_right(_STARTS, ord(ch)) - 1
    return _BLOCKS[i][2] if i >= 0 and _BLOCKS[i][0] <= ord(ch) <= _BLOCKS[i][1] else None

@functools.lru_cache(maxsize=None)
def _code_order(g):
    """whether the encoding supplies the run's order, within one pane (Unicode block): "monotone" (code points rise
    throughout, or fall throughout; gaps and strides allowed), "rotated" (from 5 glyphs: two monotone pieces in one
    direction joined by a jump between the run's extreme code points, a window wrapped across a cycle encoded in order:
    🕙🕚🕛🕐🕑), "interleaved" (from 6 glyphs: alternate glyphs form two monotone runs in one direction: SrQpOn, 🕑🕝🕒🕞),
    or "none" (including every run that spans more than one block)."""
    if len(g) < 3:
        return "none"
    cp = [ord(c) for c in g]
    if all(b - a == 1 for a, b in zip(cp, cp[1:])) or all(b - a == -1 for a, b in zip(cp, cp[1:])):
        return "monotone"                         # consecutive code points: a chart snippet wherever a block ends
    if len({block(c) for c in g}) != 1 or block(g[0]) is None:
        return "none"
    def mono(x):                                  # +1 rising, -1 falling, 0 for a single glyph, else None
        if len(x) < 2:
            return 0
        if all(b > a for a, b in zip(x, x[1:])):
            return 1
        if all(b < a for a, b in zip(x, x[1:])):
            return -1
        return None
    if mono(cp) in (1, -1):
        return "monotone"
    if len(cp) >= 5:                              # a rotation counts only from 5 glyphs: a random order of n is a rotation
        lo, hi = min(cp), max(cp)                 # of a monotone one with probability 2n/n! (1 at n = 3, 1/12 at 5)
        for k in range(1, len(cp)):
            x, y = cp[:k], cp[k:]
            mx, my = mono(x), mono(y)
            d = mx if mx in (1, -1) else my
            if (d in (1, -1) and mx in (d, 0) and my in (d, 0) and {x[-1], y[0]} == {lo, hi}
                    and (max(x) < min(y) or max(y) < min(x))):      # the pieces' ranges don't overlap: a true wrap
                return "rotated"
    def rot(x, d):                                # monotone after one wrap between its extremes, from 5 glyphs
        if len(x) < 5:
            return False
        lo, hi = min(x), max(x)
        return any(mono(x[:k]) in (d, 0) and mono(x[k:]) in (d, 0) and {x[k - 1], x[k]} == {lo, hi}
                   and (max(x[:k]) < min(x[k:]) or max(x[k:]) < min(x[:k])) for k in range(1, len(x)))
    if len(cp) >= 6:                              # halves of 3 or more, each monotone (or, from 5, rotated), one direction
        a, b = cp[0::2], cp[1::2]
        for d in (1, -1):
            if (mono(a) == d or rot(a, d)) and (mono(b) == d or rot(b, d)):
                return "interleaved"
    return "none"

def code_order(g):
    return _code_order(tuple(g))
