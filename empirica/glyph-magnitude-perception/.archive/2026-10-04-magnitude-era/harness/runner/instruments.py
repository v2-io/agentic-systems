"""Instrument prompt builders + versioned parsers (protocol v1.0).

Prompt text lineage: the option wording is the pilot's validated walk5b/probe5 wording
(glyph-echo + felt distance + ≈ + ⟂), with the v1.0 answer-channel fix (the words
first/second, equal, none accepted as fallbacks for judges that cannot echo exotic glyphs)
and per-ITEM fated option-order permutation (pilot fix #4).
Parsing never touches the ledger: it re-reads verbatim raw responses (PARSER_VERSION).
"""
import json, re
from fate import rng

PROTOCOL = "gmp-v1.0"
PARSER_VERSION = "p1.3"
# p1.3 (2026-10-03, after the independent audit analysis/verification/2026-10-03-audit-v1.0.md, data seen):
#  pair answers are classified by signal count — exactly one answer signal or 'unparsed' (no more
#  first-mentioned resolution of two-glyph replies, no leading-glyph rule); the words first/second/none/
#  equal count only when the text is nothing but answer words (p1.2 read qwen3's truncated reasoning
#  "First, the user is asking..." as the answer 'first'); the last non-empty line is classified before the
#  whole text; gestalt answers are read from the last line that carries stimulus glyphs or ⟂/none.
# p1.2 (2026-10-03, found while inspecting interim gestalt arrangements, before any result was written up):
#  gestalt answers are no longer edge-stripped of '.', '*', quotes or backticks when those characters are
#  stimulus glyphs (p1.1 silently dropped the leading '.' of the rings/dimension sets and edge '*' of rays)
# p1.1 (2026-10-03, before any v1.0 result was computed; raw data and prompts untouched):
#  - a bare stimulus glyph is matched BEFORE markdown-strip (p1.0 stripped '*', losing the glyph *)
#  - sheet mode: "a"/"b" answers map to the item's a/b fields (judges used the JSON field names)
#  - sheet mode: when the text holds several {"answers": ...} objects (grok's stream sometimes restarts
#    its answer mid-text), the LAST one that parses is used

SYSTEM = "You are a participant in a short perception study. Answer exactly as asked."

OPT_G = ("the symbol itself, copied exactly (or the word first / second), if one immediately feels like it "
         "conveys MORE (magnitude, amount, intensity, size, value), followed by a comma and one of: "
         "somewhat, much, vastly (how much more it feels)")
OPT_T = "≈ (or the word equal) if they feel comparable and equal on a shared axis"
OPT_P = ("⟂ (or the word none) if you don't perceive an ordering between them (no shared axis; "
         "the comparison would have to be constructed rather than felt)")

FORMATS = {
    "perp": [OPT_G, OPT_T, OPT_P],   # pilot walk3/4/5 response set
    "tie": [OPT_G, OPT_T],           # pilot walk1/2 response set
    "forced": [OPT_G],               # pilot battery-style forced choice (graded)
}

def options_for(fmt, perm_key):
    opts = list(FORMATS[fmt])
    rng(PROTOCOL, "option-permutation", perm_key).shuffle(opts)
    return opts

def pair_prompt(a, b, fmt, perm_key):
    opts = options_for(fmt, perm_key)
    if fmt == "forced":
        return (f"Two symbols:  {a}   {b}\n\nFirst instinct only. Which one immediately feels like it conveys MORE "
                f"(magnitude, amount, intensity, size, value)? Answer with that symbol itself, copied exactly (or the "
                f"word first / second), followed by a comma and one of: somewhat, much, vastly (how much more it feels).\n\n"
                f"Reply with only your answer, nothing else.")
    lines = "\n".join(f"  - {o}" for o in opts)
    tail = "\n\n⟂ is a common, fully valid answer." if fmt == "perp" else ""
    return (f"Two symbols:  {a}   {b}\n\nFirst instinct only. Answer with one of:\n{lines}{tail}\n\n"
            f"Reply with only your answer, nothing else.")

def sheet_prompt(items, fmt, perm_key):
    """items: list of {id, a, b}. One call judges the whole sheet (pilot sheet mode)."""
    opts = options_for(fmt, perm_key)
    lines = "\n".join(f"  - {o}" for o in opts)
    perp = "\n\n⟂ is expected often and is fully valuable." if fmt == "perp" else ""
    body = "\n".join(json.dumps({"id": it["id"], "a": it["a"], "b": it["b"]}, ensure_ascii=False) for it in items)
    return ("Quick perception task — first instincts, please. Below are numbered items, each with two symbols "
            f"a and b. For each item answer with one of:\n{lines}{perp}\n\nSome symbols recur across items; judge each "
            "item on its own as it comes rather than building a scheme. Immediate impressions; please answer every item.\n\n"
            'Reply with JSON only, no prose: {"answers":[{"id":<id>,"more":"<symbol, or first/second, or ≈/equal'
            + (", or ⟂/none" if fmt == "perp" else "") + '>","by":"somewhat|much|vastly or empty"}, ...]}\n\nItems:\n' + body)

GESTALT_INSTR = ("Below is a set of symbols in scrambled order: {glyphs}\n\n"
                 "First instinct: do these feel like they belong in some order (any kind of more/less, "
                 "progression, or motion)? If so, write them out in that order, all of them, as one string with no "
                 "spaces. If one or more of them don't belong to the order you see, leave those out and list them after the "
                 "word EXTRA. If you don't perceive any order among them, answer only ⟂ (or the word none).\n\n"
                 "Reply with only your answer, nothing else.")

def gestalt_prompt(glyphs):
    return GESTALT_INSTR.format(glyphs="  ".join(glyphs))

# ------------------------------------------------------------------ parsing (p1.0)
BY_WORDS = ("vastly", "much", "somewhat")

def _strip(r):
    r = (r or "").strip()
    r = re.sub(r"^```[a-z]*\s*|\s*```$", "", r).strip()
    r = r.strip("`*\"' \t\n.")
    return r

_PERP_W = {"none", "neither", "no"}
_TIE_W = {"equal", "equals", "same"}
_FILLER = set(BY_WORDS) | {"more", "ordering", "order", "perceived", "the", "one"}

def _classify(text, a, b, sheet):
    """p1.3 signal classifier: returns (verdict, more, by) only when the text carries exactly ONE answer
    signal; zero or conflicting signals -> None (reported as unparsed, never imputed)."""
    t = re.sub(r"^```[a-z]*\s*|\s*```$", "", (text or "").strip()).strip()
    t = t.strip("".join(c for c in "`*\"' \t\n." if c not in (a, b)))  # never strip a stimulus glyph
    if not t:
        return None
    low = t.lower()
    toks = [x for x in re.split(r"[\s,;:()\[\]\.!\-—]+", low) if x]
    by = next((w for w in BY_WORDS if w in toks), None)
    sig = set()
    if not (a in b or b in a):
        if a in t: sig.add(("dir", a))
        if b in t: sig.add(("dir", b))
    first_w = {"first", "1st"} | ({"a"} if sheet else set())
    second_w = {"second", "2nd"} | ({"b"} if sheet else set())
    word_ok = all(x in _FILLER or x in first_w | second_w | _PERP_W | _TIE_W for x in toks)
    if word_ok:  # word answers count only when the text is nothing but answer words
        w = set(toks)
        if w & first_w: sig.add(("dir", a))
        if w & second_w: sig.add(("dir", b))
        if w & _PERP_W: sig.add(("perp", None))
        if w & _TIE_W: sig.add(("tie", None))
    if "⟂" in t or "⊥" in t: sig.add(("perp", None))
    if "≈" in t: sig.add(("tie", None))
    if len(sig) != 1:
        return None
    v, m = next(iter(sig))
    return (v, m, by if v == "dir" else None)

def parse_pair(raw, a, b, sheet=False):
    """-> (verdict, more, by), verdict in {dir, tie, perp, unparsed}.
    p1.3: the LAST non-empty line is classified first (explanations precede answers); if it carries no single
    signal, the whole text is classified; otherwise unparsed."""
    r0 = re.sub(r"^```[a-z]*\s*|\s*```$", "", (raw or "").strip()).strip()
    if not r0:
        return ("unparsed", None, None)
    lines = [ln for ln in r0.splitlines() if ln.strip()]
    for cand in ([lines[-1]] if len(lines) > 1 else []) + [r0]:
        v = _classify(cand, a, b, sheet)
        if v:
            return v
    return ("unparsed", None, None)

def parse_sheet(raw, items):
    """-> {id: (verdict, more, by)} from a JSON sheet answer; tolerant of prose/code-fence wrappers and of
    restarted answers (the last parseable {"answers": ...} object wins)."""
    out = {}
    if not raw:
        return out
    dec = json.JSONDecoder(); ans = None
    starts = [m.start() for m in re.finditer(r'\{\s*"answers"', raw)]
    for st in reversed(starts):
        try:
            d, _ = dec.raw_decode(raw[st:])
            ans = d.get("answers"); break
        except Exception:
            continue
    byid = {it["id"]: it for it in items}
    for x in ans or []:
        if not isinstance(x, dict):
            continue
        it = byid.get(x.get("id"))
        if not it:
            continue
        more = str(x.get("more", ""))
        v = parse_pair(more + ("," + str(x["by"]) if x.get("by") else ""), it["a"], it["b"], sheet=True)
        out[it["id"]] = v
    return out

def parse_gestalt(raw, glyphs):
    """-> dict(kind=perp|order|unparsed, order=[...], extra=[...], stray=[...])"""
    gs0 = set(glyphs)
    r = (raw or "").strip()
    r = re.sub(r"^```[a-z]*\s*|\s*```$", "", r).strip()
    lines = [ln.strip() for ln in r.splitlines() if ln.strip()]
    hits = [ln for ln in lines if ("⟂" in ln or ln.lower().rstrip(".") == "none" or sum(g in ln for g in gs0) >= 2)]
    if hits:
        r = hits[-1]
    keep = "".join(c for c in "`*\"' .\t\n" if c not in gs0)
    r = r.strip(keep)
    if not r:
        return {"kind": "unparsed"}
    if r in ("⟂", "⊥") or r.lower().rstrip(".") in ("none",):
        return {"kind": "perp"}
    main, _, extra = r.partition("EXTRA")
    gs = set(glyphs)
    def seq(s):
        out = []; i = 0
        # greedy longest-match over the stimulus glyph inventory (glyphs may be multi-codepoint)
        inv = sorted(gs, key=len, reverse=True)
        while i < len(s):
            for g in inv:
                if s.startswith(g, i):
                    out.append(g); i += len(g); break
            else:
                i += 1
        return out
    order = seq(main); ex = seq(extra)
    if not order and "⟂" in r:
        return {"kind": "perp"}
    return {"kind": "order" if order else "unparsed", "order": order, "extra": ex}
