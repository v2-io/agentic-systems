"""Whose side does a third mind take? Over questions answered by A, B and X (single answers: each mind's first), where
A and B give different answers: the share where X gives A's answer, B's answer, or neither. If disagreement between A
and B belongs to A's family, a third mind of A's family should side with A more than a mind of another family does."""
import collections, sys
import lib
from values import value, ckey

def load(kinds):
    recs, man = lib.load()
    by = collections.defaultdict(dict)
    for r in recs:
        if r["kind"] not in kinds or r["era"] == "seed": continue
        if (r.get("tags") or {}).get("variant") not in (None, "plain"): continue
        if (r.get("tags") or {}).get("control"): continue
        v = value(r)
        if v is None: continue
        by[ckey(r)].setdefault(r["mind"], v)
    return by

if __name__ == "__main__":
    for kinds in (["continue"], ["cohere"], ["inhibit"], ["triad"], ["order"], ["choose"]):
        by = load(set(kinds))
        for A, B in (("sonnet55", "grok46"), ("sonnet55", "gemini38flash"), ("grok46", "gemini38flash")):
            print(f"{kinds[0]:8s} {A} vs {B}")
            for X in ("opus55", "haiku45nt", "haiku45", "sonnet55", "grok46", "gemini38flash", "gemini31pro"):
                if X in (A, B): continue
                c = collections.Counter()
                for d in by.values():
                    if A in d and B in d and X in d and d[A] != d[B]:
                        c["A" if d[X] == d[A] else ("B" if d[X] == d[B] else "neither")] += 1
                n = sum(c.values())
                if n >= 25:
                    print(f"   X={X:14s} n={n:5d}  sides with {A}: {c['A']/n:.2f}   with {B}: {c['B']/n:.2f}   neither: {c['neither']/n:.2f}")
