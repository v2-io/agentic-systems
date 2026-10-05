#!/usr/bin/env python3
"""Higher-order evidence on a row: windows of 4-8 consecutive glyphs, judged as wholes (Joseph, 2026-10-05: "many
sequences don't really make sense until *more* than three glyphs in it are shown ... which branch is chosen is
almost certainly dependent on some n-gram of prior characters rather than a set of triads ... We need to up our
dimensions").

Two kinds of answers already hold windows whole; until now both were cut down to triples:
  ORDER answers   a mind shown a set S (4-8 glyphs, shuffled) writes lines. A window W (all of W in S) is GIVEN when W's
                  glyphs sit in one line in W's order (either direction); ties inside W are neutral; anything else
                  (W split across lines, set aside, or out of order) is AGAINST.
  NEXT answers    a mind shown a context ending in C (an oriented run of the row, >= 3 glyphs) proposes what comes next.
                  The window C+x (x the row's next glyph) is GIVEN when x is among its proposals, AGAINST otherwise.
  CONTINUE answers  the same with the first written glyph; and every run of 4-8 distinct glyphs the mind wrote out
                  (context + continuation, at least two written glyphs) is GIVEN.
Read-off only: nothing is filtered or gated.
"""
import collections

def index(parsed, pres, fam):
    orders, nexts, written = [], collections.defaultdict(list), collections.defaultdict(list)
    by_glyph = collections.defaultdict(set)
    for r in parsed:
        if r["status"] != "ok" or not isinstance(r["answer"], dict):
            continue
        p = pres[r["pid"]]; a = r["answer"]
        if p["kind"] == "order":
            pos = {}
            for li, line in enumerate(a.get("lines") or []):
                si = 0
                for st in line:
                    if st == "GAP":
                        continue
                    for g in st:
                        pos[g] = (li, si)
                    si += 1
            S = frozenset(g for g in p["shown"] if g != "GAP")
            k = len(orders)
            orders.append((S, pos, fam.get(r["mind"], r["mind"])))
            for g in S:
                by_glyph[g].add(k)
        elif p["kind"] in ("next", "continue"):
            ctx = list(p["shown"]); f = fam.get(r["mind"], r["mind"])
            cont = a.get("continuation") or []
            props = set(a.get("proposals") or []) if p["kind"] == "next" else set(cont[:1])
            for j in range(3, len(ctx) + 1):        # every context suffix of >= 3 glyphs is the head of a window
                nexts[tuple(ctx[-j:])].append((props, f))
            # a continuation writes whole windows itself: each run of 4-8 distinct glyphs of context + continuation
            # holding at least two written glyphs (a single written glyph is the suffix case above)
            S = ctx + cont
            for k in range(4, 9):
                for i in range(max(0, len(ctx) + 2 - k), len(S) - k + 1):
                    w = S[i:i + k]
                    if len(set(w)) == k:
                        written[tuple(min(w, w[::-1]))].append(f)
    return orders, by_glyph, nexts, written

def _monotone(st, cyclic):
    """st in order (either direction); on a cycle, up to rotation: an answer is a line, so a mind that sees the cycle
    still has to start writing it somewhere -- a window across the wrap reads as one drop (or rise), not a break."""
    up = sum(1 for x, y in zip(st, st[1:]) if y < x)
    dn = sum(1 for x, y in zip(st, st[1:]) if y > x)
    if up == 0 or dn == 0:
        return True
    if cyclic:
        return (up == 1 and st[-1] < st[0]) or (dn == 1 and st[-1] > st[0])
    return False

def window_tally(W, ix, cyclic=False):
    """(given, against, families giving) for one oriented window W (cyclic: W is a stretch of a cycle)."""
    orders, by_glyph, nexts, written = ix
    given = against = 0; fams = set()
    ids = None
    for g in W:
        ids = by_glyph.get(g, set()) if ids is None else ids & by_glyph.get(g, set())
        if not ids:
            break
    for k in ids or ():
        S, pos, f = orders[k]
        if any(g not in pos for g in W):
            against += 1; continue
        lines = {pos[g][0] for g in W}
        if len(lines) > 1:
            against += 1; continue
        st = [pos[g][1] for g in W]
        if len(set(st)) < len(st):
            continue                                    # a tie inside the window: neutral
        if _monotone(st, cyclic):
            given += 1; fams.add(f)
        else:
            against += 1
    for f in written.get(tuple(min(W, W[::-1])), ()):   # continuations that wrote the window out
        given += 1; fams.add(f)
    for seq in (W, W[::-1]):                            # next/continue answers whose context ends with the head
        for props, f in nexts.get(tuple(seq[:-1]), ()):
            if seq[-1] in props:
                given += 1; fams.add(f)
            else:
                against += 1
    return given, against, fams

def row_windows(g, cyclic, ix, kmax=8):
    """All windows of 4..kmax consecutive glyphs of the row: [(i, k, W, given, against, fams)]."""
    n = len(g); out = []
    ring = g + g[:kmax - 1] if cyclic else g
    for k in range(4, min(kmax, n) + 1):
        for i in range(n if cyclic else n - k + 1):
            W = ring[i:i + k]
            gv, ag, fs = window_tally(W, ix, cyclic)
            out.append((i, k, W, gv, ag, fs))
    return out

def summarize(g, cyclic, ix):
    return summarize_ws(row_windows(g, cyclic, ix))

def summarize_ws(ws):
    whole = [w for w in ws if w[3] > w[4]]
    broken = [w for w in ws if w[4] > w[3]]
    # minimal broken windows: no broken window strictly inside them (where the false join is)
    def inside(a, b):
        return a[1] < b[1] and b[0] <= a[0] and a[0] + a[1] <= b[0] + b[1]
    minimal = [b for b in broken if not any(inside(c, b) for c in broken)]
    unasked = [(w[0], w[1]) for w in ws if not (w[3] + w[4])]
    return {"windows": len(ws), "asked": sum(1 for w in ws if w[3] + w[4]), "unasked": unasked,
            "whole": len(whole), "broken": len(broken),
            "longest_whole": max((w[1] for w in whole), default=0),
            "breaks": ["".join(w[2]) + f" ({w[3]}:{w[4]})" for w in sorted(minimal, key=lambda w: (w[1], w[0]))[:3]]}
