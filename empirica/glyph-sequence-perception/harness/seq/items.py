"""Items, presentations, sheets and prompts (PLAN.md §3). Every random choice is fated (common.R).

Item kinds
  triad    3 glyphs. Presentations are a Latin rotation: rep r shows the fated base order rotated by r, so each
           glyph sits in the middle slot exactly once over reps 0,1,2; the leading end of each is a fated coin.
  order    4-8 glyphs. Each rep is an independent fated shuffle.
  next     an ordered context (2-5 glyphs) ending at the glyph whose successor is asked for.
  between  left context + right context around a gap.

Sheet-level random parameters (PLAN.md §3 table): perp_offered 0.9 (else forced), tie_offered 0.5,
gap_offered 0.5 (order only); option order and independent-sentence order permuted; item order shuffled with
no two presentations of one item adjacent. Presentations of one item in one round go on the same sheet or
on different sheets, a fated 50/50 per item; the realized placement, the sheet size (1-5, fated) and the
position on the sheet are recorded per presentation.
"""
import json
from common import R, uid, ok_glyph

KINDS = ("triad", "order", "next", "between")
MAX_SHEET = 5
P_PERP, P_TIE, P_GAP, P_SAME_SHEET = 0.9, 0.5, 0.5, 0.5

# ------------------------------------------------------------------ items
def make_item(kind, glyphs=None, context=None, left=None, right=None, source=None):
    if kind in ("triad", "order"):
        g = sorted(set(glyphs))
        assert all(ok_glyph(x) for x in g), g
        assert (len(g) == 3) if kind == "triad" else (4 <= len(g) <= 8), (kind, g)
        key = {"kind": kind, "glyphs": g}
        it = {"kind": kind, "glyphs": g}
    elif kind == "next":
        c = list(context); assert 2 <= len(c) <= 5 and len(set(c)) == len(c) and all(ok_glyph(x) for x in c), c
        key = {"kind": kind, "context": c}
        it = {"kind": kind, "context": c, "glyphs": sorted(set(c))}
    elif kind == "between":
        l, r = list(left), list(right)
        assert l and r and len(l) + len(r) <= 5 and len(set(l + r)) == len(l + r), (l, r)
        key = {"kind": kind, "left": l, "right": r}
        it = {"kind": kind, "left": l, "right": r, "glyphs": sorted(set(l + r))}
    else:
        raise ValueError(kind)
    it["iid"] = uid({"triad": "T", "order": "O", "next": "N", "between": "B"}[kind], key)
    it["source"] = source or {}
    return it

def shown_order(item, rep):
    """The glyphs exactly as displayed for presentation `rep` of `item`."""
    k = item["kind"]
    if k == "triad":
        base = list(item["glyphs"]); R("triad-base", {"iid": item["iid"]}).shuffle(base)
        r = rep % 3
        s = base[r:] + base[:r]           # middle slot holds base[(r+1)%3]: each glyph once over r=0,1,2
        if R("triad-lead", {"iid": item["iid"], "rep": rep}).random() < 0.5:
            s = s[::-1]                   # reversal keeps the middle glyph in the middle
        return s
    if k == "order":
        s = list(item["glyphs"]); R("order-shuffle", {"iid": item["iid"], "rep": rep}).shuffle(s)
        return s
    if k == "next":
        return list(item["context"])
    if k == "between":
        return list(item["left"]) + ["GAP"] + list(item["right"])
    raise ValueError(k)

def presentation(item, rep, round_id):
    return {"pid": uid("P", {"iid": item["iid"], "rep": rep}), "iid": item["iid"], "kind": item["kind"],
            "rep": rep, "shown": shown_order(item, rep), "round": round_id}

# ------------------------------------------------------------------ prompts
OPENER = "Quick task, first impressions please."

def _intro(kind):
    return {"triad": "Each item below shows three symbols.",
            "order": "Each item below shows a set of symbols in scrambled order.",
            "next": "Each item below shows symbols in a sequence; the last one listed is where the sequence has got to.",
            "between": "Each item below shows symbols in a sequence with one gap, marked GAP."}[kind]

def _options(kind, f):
    if kind == "triad":
        if not f["perp"]:
            return ['"seq": all three, written in the sequence they seem to form (either end first)']
        return ['"seq": all three, written in the sequence they seem to form (either end first)',
                '"two": just two of them, if only those two seem to go together',
                '"none": true, if they don\'t seem to go in any sequence']
    if kind == "order":
        if not f["perp"]:
            return ['"seqs": all of them, as one list in the sequence they seem to form (either end first)']
        return ['"seqs": the symbols that seem to go in a sequence, in that sequence (either end first); '
                'if you see more than one separate sequence, give each as its own list. Put any symbols that '
                'belong to none of them in "extra"',
                '"none": true, if none of them seem to form a sequence']
    if kind == "next":
        return ['"next": up to three symbols that could come next after the last one, most fitting first',
                '"none": true, if nothing seems to come next']
    if kind == "between":
        return ['"between": up to three symbols that could fill the gap, most fitting first',
                '"none": true, if nothing seems to fit there']

def _sentences(kind, f):
    s = ["Go by first impressions, and judge each item on its own rather than building a scheme across items."]
    if f["perp"]:
        s.append('"none" is expected often and is fully valuable.')
    if kind in ("triad", "order"):
        s.append('Copy each symbol exactly, or write "#1", "#2", … for its place in the item.')
        if f.get("tie"):
            s.append('Symbols that seem to be the same step go together in a nested list, like ["<s1>", ["<s2>", "<s3>"]].')
        if kind == "order" and f.get("gap"):
            s.append('Put "GAP" between two symbols where a step seems to be missing.')
    else:
        s.append("Any symbol may be proposed, including ones not shown; it may have no name.")
    return s

def _reply(kind, f):
    forms = {"triad": ['{"id": <id>, "seq": [...]}'] + (['{"id": <id>, "two": [...]}', '{"id": <id>, "none": true}'] if f["perp"] else []),
             "order": ['{"id": <id>, "seqs": [[...], ...], "extra": [...]}'] + (['{"id": <id>, "none": true}'] if f["perp"] else []),
             "next": ['{"id": <id>, "next": [...]}', '{"id": <id>, "none": true}'],
             "between": ['{"id": <id>, "between": [...]}', '{"id": <id>, "none": true}']}[kind]
    return ('Reply with JSON only, no prose: {"answers": [ ... ]}, one entry per item, each one of: '
            + " or ".join(forms) + ".")

def sheet_prompt(sheet):
    """sheet: {kind, sid, factors, entries:[{id, shown}]} -> prompt text. Sentence and option order are fated per sheet."""
    k, f = sheet["kind"], sheet["factors"]
    opts = _options(k, f); R("opt-order", {"sid": sheet["sid"]}).shuffle(opts)
    sents = _sentences(k, f); R("sent-order", {"sid": sheet["sid"]}).shuffle(sents)
    lines = [OPENER, _intro(k), "For each item, answer with " + ("one of:" if len(opts) > 1 else "this:")]
    lines += [f"  - {o}" for o in opts]
    lines += sents
    lines += ["", "Items:"]
    lines += [json.dumps({"id": e["id"], "s": e["shown"]}, ensure_ascii=False) for e in sheet["entries"]]
    lines += ["", _reply(k, f)]
    return "\n".join(lines)

SYSTEM = "You are a participant in a short perception study. Answer exactly as asked."

# ------------------------------------------------------------------ sheets
def _interleave(ps):
    """Keep the fated order where possible, but never put two presentations of one item next to each other
    (greedy: take the earliest presentation whose item differs from the previous one, preferring the item
    with the most presentations left, which is what keeps the greedy from dead-ending)."""
    left = list(ps); out = []
    while left:
        prev = out[-1]["iid"] if out else None
        remaining = {}
        for p in left:
            remaining[p["iid"]] = remaining.get(p["iid"], 0) + 1
        ok = [p for p in left if p["iid"] != prev] or left
        top = max(remaining[p["iid"]] for p in ok)
        pick = next(p for p in ok if remaining[p["iid"]] == top)
        out.append(pick); left.remove(pick)
    return out

def build_sheets(round_id, items_by_iid, pres, kind):
    """pres: presentations of one kind for this round -> sheets of 1-5 presentations (Joseph 2026-10-04:
    "only get one -- five (at most)"), each sheet's target size a fated draw from 1..MAX_SHEET, recorded.
    Presentations of one item go together (same sheet) or apart, a fated 50/50 per item."""
    by_item = {}
    for p in pres:
        by_item.setdefault(p["iid"], []).append(p)
    units = []
    for iid in sorted(by_item):
        ps = sorted(by_item[iid], key=lambda p: p["rep"])
        same = len(ps) > 1 and R("same-sheet", {"iid": iid, "round": round_id}).random() < P_SAME_SHEET
        units += [ps] if same else [[p] for p in ps]
    R("unit-order", {"round": round_id, "kind": kind}).shuffle(units)
    sheets, cur, target, pending, n = [], [], None, list(units), 0
    while pending:
        if target is None:
            target = 1 + R("sheet-size", {"round": round_id, "kind": kind, "n": n}).randrange(MAX_SHEET); n += 1
        here = {p["iid"] for p in cur}
        j = next((j for j, u in enumerate(pending)
                  if u[0]["iid"] not in here and (not cur or len(cur) + len(u) <= target)), None)
        if j is None:
            sheets.append(cur); cur, target = [], None
            continue
        u = pending.pop(j)
        if len(u) > 1:   # same-sheet unit: leave room for fillers so its presentations need not be adjacent
            target = min(MAX_SHEET, max(target, len(cur) + 2 * len(u) - 1))
        cur.extend(u)
        if len(cur) >= target:
            sheets.append(cur); cur, target = [], None
    if cur:
        sheets.append(cur)
    out = []
    for si, ps in enumerate(sheets):
        if not ps:
            continue
        sid = uid("S", {"round": round_id, "kind": kind, "n": si, "pids": [p["pid"] for p in ps]})
        fr = R("sheet-factors", {"sid": sid})
        f = {"perp": fr.random() < P_PERP}
        f["tie"] = (fr.random() < P_TIE) if kind in ("triad", "order") else False
        f["gap"] = (fr.random() < P_GAP) if kind == "order" else False
        ps = list(ps); R("item-order", {"sid": sid}).shuffle(ps)
        ps = _interleave(ps)
        entries = [{"id": n, "pid": p["pid"], "shown": p["shown"]} for n, p in enumerate(ps)]
        for n, p in enumerate(ps):
            p["sheet_pos"], p["sheet_n"] = n, len(ps)
        out.append({"sid": sid, "round": round_id, "kind": kind, "factors": f, "entries": entries})
    co, fac = {}, {}
    for s in out:
        for e in s["entries"]:
            co.setdefault(e["pid"], s["sid"]); fac[e["pid"]] = s["factors"]
    for p in pres:
        p["sid"] = co[p["pid"]]; p["factors"] = fac[p["pid"]]
        sib = [q for q in by_item[p["iid"]] if q["pid"] != p["pid"]]
        p["co_sheet"] = bool(sib) and all(co[q["pid"]] == p["sid"] for q in sib)
    for s in out:
        s["prompt"] = sheet_prompt(s)
    return out
