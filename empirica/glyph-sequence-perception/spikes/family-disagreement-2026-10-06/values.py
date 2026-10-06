"""What one answer says, as a comparable value, per question kind (the spike's own reading; nothing here is evidence
in the study's sense). Returns None for answers that can't be compared."""

def canon_line(lines):
    """the main (first) line of an order/names answer, ties kept as sets, reversal-invariant"""
    if not lines:
        return None
    line = tuple(tuple(sorted(step)) for step in lines[0])
    rev = line[::-1]
    return min(line, rev)

def value(r):
    k, o = r["kind"], r["outcome"]
    if k in ("cohere", "inhibit"):
        return o if o in ("yes", "no", "cant-tell") else None
    if k in ("continue", "pick", "next"):
        if o == "none":
            return "∅none"
        if o == "continuation" and r.get("continuation"):
            return r["continuation"][0]
        if o == "proposals" and r.get("proposals"):
            return sorted(r["proposals"], key=lambda p: p.get("rank", 9))[0]["g"]
        if o == "tool-attempt":
            return None
        return "∅" + o
    if k == "triad":
        a = r.get("answer") or []
        if o == "mid" and len(a) > 1:
            return "mid:" + a[1]
        return o
    if k in ("order", "names"):
        if o == "lines":
            return canon_line((r.get("answer") or {}).get("lines"))
        return o
    if k == "choose":
        return r.get("choice") if o == "chose" else o
    return None

def qkey(r):
    """the question identity: qid in the context era; (iid) in the triad era (one item, several presentations)"""
    if r.get("era") == "ctx":
        return r.get("qid")
    if r.get("era") == "triad":
        return ("T", r.get("iid"))
    return None

def canon_run(g):
    g = tuple(g)
    return min(g, g[::-1], key=lambda s: [ord(x) for x in s])

def ckey(r):
    """the question identity by CONTENT, so the same question asked in different rounds (or in either orientation, for
    whole-run kinds) is one question. Kind is part of the key."""
    k = r["kind"]; c = tuple(r.get("context") or r.get("shown") or ())
    t = r.get("tags") or {}
    if k in ("continue", "next", "pick"):
        return (k, c, bool(t.get("null")))
    if k == "inhibit":
        return (k, c, r.get("candidate"))
    if k == "cohere":
        return (k, canon_run(c))
    if k in ("triad", "order", "names"):
        return (k, frozenset(r.get("shown") or c))
    if k == "choose":
        return (k, c, frozenset(r.get("candidates") or ()))
    if k == "between":
        return (k, tuple(r.get("left") or ()), tuple(r.get("right") or ()))
    return None
