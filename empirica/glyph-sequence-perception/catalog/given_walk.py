#!/usr/bin/env python3
"""Is a run a walk over a given? (data/unicode/givens.json, built by catalog/givens.py.) Shared by the catalog build,
the CATALOG-GIVEN read-off and the planner, so the three cannot drift apart.

A run of glyphs maps to positions in a given: a letter through its base letter (any dress; givens.json's dress table),
a number through its value. The run is a walk over that given when its positions are:
  window        consecutive, one direction (a b c, 3 2 1)
  rotated       consecutive modulo the given's length, wrapping its end (8 9 0 1)
  stride        a constant step of 2 or more, with or without wrapping (a c e, B D F ... Z B)
  dress         one position in several dresses (1 ¹ ① 𝟏)
  dress-window  consecutive, each position held over one or more dresses (2 ➋ 3 ➌ 4 ➍)
  reflection    consecutive with one turnaround (possible for distinct glyphs only across dresses)
Anything else is not a walk over that given: a run that skips a position (Ο Π Ρ Τ Υ without Σ) is not given, and
that gap is information. The first matching kind in the order above wins, then the given with the most languages.
"""
import functools, json, pathlib, unicodedata as U

ROOT = pathlib.Path(__file__).resolve().parents[1]
KINDS = ["window", "dress", "dress-window", "rotated", "stride", "reflection"]

@functools.lru_cache(maxsize=1)
def load():
    d = json.load(open(ROOT / "data" / "unicode" / "givens.json", encoding="utf-8"))
    dress = {ch: tuple(v) for ch, v in d["dress"].items()}
    givens = {g["id"]: g for g in d["givens"]}
    pos = {}                                         # (letter or number glyph) -> [(gid, index)]
    for g in d["givens"]:
        for i, members in enumerate(g["positions"]):
            for ch in members:
                pos.setdefault(ch, []).append((g["id"], i))
    return givens, dress, pos, {k: d[k] for k in ("icu", "icu_unicode", "unicode_python", "pyicu")}

def label(g):
    if g["kind"] == "number":
        return f"numbers, {g['dress']}"
    langs = g["languages"]
    more = f" +{len(langs) - 3}" if len(langs) > 3 else ""
    return f"{g['script']} {g['case']} ({', '.join(langs[:3])}{more}; {g['reading']})"

def _locate(ch, givens, dress, pos):
    """-> ([(gid, index)], dress name) for one glyph"""
    if ch in pos:                                    # a letter as listed, or a number glyph of some numeric given
        hits = pos[ch]
        num = [h for h in hits if givens[h[0]]["kind"] == "number"]
        if num:                                      # numbers: every numeric given holding this value is a dress of it
            return hits, givens[num[0][0]]["dress"]
        return hits, "plain"
    if ch in dress:
        base, dn = dress[ch]
        return pos.get(base, []), dn
    return [], None

def classify(glyphs, min_len=3):
    """-> None, or {"kind", "given", "label", "start", "step", "n", "dresses"}. With min_len=2 a pair counts only as a
    window, rotation or one position in two dresses: two glyphs fix any stride, so a stride needs three."""
    glyphs = list(glyphs)
    if len(glyphs) < max(2, min_len):
        return None
    givens, dress, pos, _ = load()
    located = [_locate(ch, givens, dress, pos) for ch in glyphs]
    if any(not h for h, _ in located):
        return None
    dresses = sorted({d for _, d in located})
    # numbers: positions by value (a value is one position whichever numeric dress holds it)
    vals = [U.numeric(ch, None) for ch in glyphs]
    cands = {}
    if all(v is not None for v in vals) and all(any(givens[g]["kind"] == "number" for g, _ in h) for h, _ in located):
        for gid in {g for g, _ in located[0][0] if givens[g]["kind"] == "number"}:
            gv = givens[gid]["values"]
            if all(v in gv for v in vals):
                cands[gid] = [gv.index(v) for v in vals]
        if not cands:                                # values spread over dresses: the value line of the longest dress
            gids = {g for h, _ in located for g, _ in h if givens[g]["kind"] == "number"}
            for gid in gids:
                gv = givens[gid]["values"]
                if all(v in gv for v in vals):
                    cands[gid] = [gv.index(v) for v in vals]
    else:
        common = {g for g in set.intersection(*[{g for g, _ in h} for h, _ in located]) if givens[g]["kind"] == "alphabet"}
        # the most widely used alphabet holding every letter (by its languages), both readings of it; not any of ~400,
        # where some rare alphabet would make almost any run regular (a b d f is a stride in Ligurian's)
        top = max((len(givens[g]["languages"]) for g in common), default=0)
        for gid in common:
            if len(givens[gid]["languages"]) != top:
                continue
            idx = []
            for h, _ in located:
                ii = sorted(i for g, i in h if g == gid)
                idx.append(ii[0])
            cands[gid] = idx
    best = None
    if len(glyphs) == 2:
        cands = {g: i for g, i in cands.items() if _kind(i, len(givens[g]["positions"]), True) and
                 _kind(i, len(givens[g]["positions"]), True)[0] in ("window", "rotated", "dress")}
    if cands and len(glyphs) > 2 and all(v is not None for v in vals):  # numbers: a constant step in value is the given's n-step (⅛ ¼ ⅜ ½)
        d = [b - a for a, b in zip(vals, vals[1:])]
        if all(abs(x - d[0]) < 1e-12 for x in d) and d[0] != 0 and abs(d[0]) != 1:
            gid = min(cands, key=lambda g: (-len(givens[g]["positions"]), g))
            return dict(kind="stride", given=gid, label=label(givens[gid]), start=cands[gid][0], step=d[0],
                        n=len(givens[gid]["positions"]), dresses=dresses)
    for gid, idx in cands.items():
        n = len(givens[gid]["positions"])
        k = _kind(idx, n, len(set(dresses)) > 1 or len(set(glyphs)) != len(set(idx)))
        if k is None:
            continue
        key = (KINDS.index(k[0]), -len(givens[gid].get("languages", [])), gid)
        if best is None or key < best[0]:
            best = (key, dict(kind=k[0], given=gid, label=label(givens[gid]), start=idx[0], step=k[1], n=n, dresses=dresses))
    return best[1] if best else None

@functools.lru_cache(maxsize=None)
def classify_cached(glyphs, min_len=3, as_set=False):
    """classify() for hashable input, cached (the planner asks about the same contexts many times). as_set: the
    glyphs are an unordered set (a triad, an order or names set): is there an order of them that walks a given?
    Tried in the order of each glyph's position in its given (numbers by value)."""
    gl = list(glyphs)
    if not as_set:
        return classify(gl, min_len)
    givens, dress, pos, _ = load()
    def key(ch):
        v = U.numeric(ch, None)
        if v is not None:
            return (0, v)
        h, _ = _locate(ch, givens, dress, pos)
        return (1, min((i for _, i in h), default=10 ** 9))
    return classify(sorted(gl, key=key), min_len)

def _kind(idx, n, dressed):
    steps = [b - a for a, b in zip(idx, idx[1:])]
    msteps = [s % n for s in steps]
    if all(s == steps[0] for s in steps) and steps[0] in (1, -1):
        return ("window", steps[0])
    if dressed and all(s == 0 for s in steps):
        return ("dress", 0)
    if dressed and set(steps) <= {0, 1} and 1 in steps or dressed and set(steps) <= {0, -1} and -1 in steps:
        return ("dress-window", 1 if 1 in steps else -1)
    if all(m == msteps[0] for m in msteps) and msteps[0] in (1, n - 1):
        return ("rotated", 1 if msteps[0] == 1 else -1)
    if all(s == steps[0] for s in steps) and abs(steps[0]) >= 2:
        return ("stride", steps[0])
    if all(m == msteps[0] for m in msteps) and msteps[0] not in (0, 1, n - 1):
        return ("stride", msteps[0] if msteps[0] <= n // 2 else msteps[0] - n)
    if all(abs(s) == 1 for s in steps):
        turns = sum(1 for a, b in zip(steps, steps[1:]) if a != b)
        if turns == 1:
            return ("reflection", steps[0])
    return None

if __name__ == "__main__":
    for t in ["abc", "0123456789", "6543210987", "012345678𝟵", "ΟΠΡΤΥ", "ΑΒΓΔ", "MJGDAXUROLIFCZWTQNKHEBYV",
              "1¹₁①⑴⒈❶➀➊⓵１🄂🯱𝟏𝟙", "2➋3➌4➍", "⑦⑧⑨⑩⑪", "𝔄𝔅ℭ𝔇", "абвгдеёж", "abdf", "ⅠⅡⅢⅣ", "⅛¼⅜½", "あいうえお", "%‰‱"]:
        print(t, classify(t))
