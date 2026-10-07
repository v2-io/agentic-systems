#!/usr/bin/env python3
"""Whether the encoding supplies a run's order: shared by the catalog build (build 6, record field code_order) and the
planner (stochastic-5, ENCODED_RELEVANCE), so the two can't drift apart. Joseph, 2026-10-06: "so many of these are
basically just snippets of the unicode spec"; "Far too many resources spent in the end on 'given' sequences with their
known trivial permutations and snippets of the unicode panes."
"""
import functools

@functools.lru_cache(maxsize=None)
def _code_order(g):
    """whether the encoding supplies the run's order: "monotone" (code points strictly up or down), "rotated" (monotone
    after one wrap: a cycle encoded in order, 🕙🕚🕛🕐), "interleaved" (two monotone halves, alternate glyphs, in one
    direction: a b A B, hours and half-hours), or "none"."""
    cp = [ord(c) for c in g]
    def mono(x, d=None):
        ups = all(b > a for a, b in zip(x, x[1:])); downs = all(b < a for a, b in zip(x, x[1:]))
        return ("up" if ups else "down" if downs else None) if d is None else (ups if d == "up" else downs)
    def rot(x, d):                                # a rotation counts only from 5 glyphs: a random order of n is a
        return len(x) >= 5 and any(mono(x[k:] + x[:k], d) for k in range(1, len(x)))   # rotation of a monotone
                                                  # one with probability 2n/n! (1 at n = 3, 1/3 at 4, 1/12 at 5)
    if len(cp) < 3:
        return "none"
    if mono(cp):
        return "monotone"
    if rot(cp, "up") or rot(cp, "down"):
        return "rotated"
    if len(cp) >= 6:                              # halves of 3 or more, each monotone (or rotated, from 5) in one direction
        a, b = cp[0::2], cp[1::2]
        for d in ("up", "down"):
            if (mono(a, d) or rot(a, d)) and (mono(b, d) or rot(b, d)):
                return "interleaved"
    return "none"


def code_order(g):
    return _code_order(tuple(g))
