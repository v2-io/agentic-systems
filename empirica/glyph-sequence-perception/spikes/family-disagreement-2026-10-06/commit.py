"""Threshold versus content. For each pair of minds on the same questions (single first answers): did both commit
(continue with a glyph / name a middle / give an order line / choose) or both decline, and when both committed, did
they commit to the same thing? Disagreements are split into: commit-decision differs; both commit, content differs."""
import collections, itertools
import lib
from values import value, ckey

COMMIT = {"continue": lambda v: not v.startswith("∅"), "triad": lambda v: v.startswith("mid:"),
          "order": lambda v: isinstance(v, tuple), "pick": lambda v: not v.startswith("∅"),
          "next": lambda v: not v.startswith("∅")}
recs, man = lib.load()
by = collections.defaultdict(lambda: collections.defaultdict(dict))
for r in recs:
    if r["kind"] not in COMMIT or r["era"] == "seed": continue
    t = r.get("tags") or {}
    if t.get("variant") not in (None, "plain") or t.get("control"): continue
    v = value(r)
    if v is None: continue
    by[r["kind"]][ckey(r)].setdefault(r["mind"], v)
MINDS = ["sonnet55", "opus55", "haiku45nt", "haiku45", "grok46", "gemini38flash", "gemini31pro"]
for kind in ("continue", "next", "triad", "order"):
    print(f"\n== {kind}:  pair  n  | disagreements: share that are commit-decision | P(same content | both commit)")
    for a, b in itertools.combinations(MINDS, 2):
        n = dis = dec = bc = same = 0
        for d in by[kind].values():
            if a in d and b in d:
                va, vb = d[a], d[b]; n += 1
                ca, cb = COMMIT[kind](va), COMMIT[kind](vb)
                if va != vb:
                    dis += 1; dec += ca != cb
                if ca and cb:
                    bc += 1; same += va == vb
        if n >= 100:
            print(f"  {a:13s} {b:13s} n={n:6d} disagree {dis/n:.3f} | commit-decision {dec/max(dis,1):.2f} | same content {same/max(bc,1):.3f} (n={bc})")
