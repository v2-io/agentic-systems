"""Concern 1: probing -- how a question is put, and turning a raw answer into canonical answer records
(METHODOLOGY §2a, §4). Knows nothing about sequences or why a question is asked: a question arrives with an opaque
`source` (carried as metadata only) and leaves as tagged records.

Question kinds (refactored protocol "ctx-0.1"):
  continue   a context (2-8 glyphs, oriented); the mind writes what comes after its last glyph, in order, as many as
             come naturally (up to 24), or "none". The study's main question.
  inhibit    a context and one candidate glyph; does the candidate come directly after the context's last glyph?
             "yes" / "no" / "can't tell". Context-conditioned negative (and positive) evidence (METHODOLOGY §2b).
Answer options are words, never glyphs, so no glyph is reserved (METHODOLOGY §4).

Sheets hold 1-5 questions of one kind, in a fated order (no two questions sharing a context adjacent); the sheet
size, each question's position and the sheet's instruction-sentence order are fated and recorded as tags. Every
choice is fated: seed = H(protocol || purpose || object).
"""
import hashlib, json, re, sys, pathlib, unicodedata as U

HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[1] / "core"))
import fate                                                # noqa: E402

PROTOCOL = "ctx-0.1"
MAX_SHEET = 5
MAX_CONTINUE = 24
KINDS = ("continue", "inhibit")
SYSTEM = "You are a participant in a short perception study. Answer exactly as asked."
VS = {"︎", "️"}

def R(purpose, obj):
    return fate.rng(PROTOCOL, purpose, obj)

def uid(prefix, obj):
    return prefix + fate.digest(obj)[:12]

def is_glyph(ch):
    return len(ch) == 1 and U.category(ch)[0] in "LNPS" and not ch.isspace()

def clean(s):
    """-> (text after NFC, strip, and variation-selector removal, vs_stripped)"""
    t = U.normalize("NFC", str(s)).strip()
    t2 = "".join(ch for ch in t if ch not in VS)
    return t2, t2 != t

def content_class(t):
    if len(t) != 1:
        return "string"
    c = U.category(t)
    return "unassigned" if c == "Cn" else ("mark" if c[0] == "M" else "other")

# ------------------------------------------------------------------ questions
# Controls for recognition (inhibit) questions (Joseph, 2026-10-05: "wrt 'yes' -- can't you add controls?"): a matched
# decoy at the same context, a candidate that should not continue it, put on the same sheets indistinguishably. It
# measures how readily each mind says "yes" -- acquiescence ("far": a glyph from a distant part of Unicode) and
# block-membership ("near": the same neighbourhood of the code chart, but not adjacent). The control kind is a probing
# tag on the question and its records (tags.control); a control's answers are also ordinary answers about its pair.
CONTROL_NEAR = 48                 # near decoys: within this many code points of the candidate, more than 2 away
FAR_POOL = [(0x21, 0x7E), (0xA1, 0x24F), (0x370, 0x3FF), (0x2000, 0x2BFF), (0x2E80, 0x33FF), (0x1D300, 0x1D7FF),
            (0x1F000, 0x1FBFF)]

def control_candidate(context, x, kind, rid):
    """a fated decoy for the recognition question (context, x): kind "near" or "far" -> glyph"""
    r = R("control", {"round": rid, "context": list(context), "x": x, "kind": kind})
    bad = set(context) | {x}
    last = ord(context[-1])
    if kind == "near":
        pool = [c for c in range(ord(x) - CONTROL_NEAR, ord(x) + CONTROL_NEAR + 1)
                if abs(c - ord(x)) > 2 and abs(c - last) > 2 and c > 0x20 and is_glyph(chr(c))
                and U.category(chr(c)) != "Cn" and chr(c) not in bad]
        if pool:
            return chr(r.choice(pool))
    while True:
        lo, hi = r.choices(FAR_POOL, weights=[b - a + 1 for a, b in FAR_POOL])[0]
        c = r.randint(lo, hi)
        if abs(c - ord(x)) > 4096 and abs(c - last) > 4096 and is_glyph(chr(c)) and U.category(chr(c)) != "Cn" \
                and chr(c) not in bad:
            return chr(c)

def question(kind, context, candidate=None, source=None, variant=None, probe=None):
    c = list(context)
    assert 2 <= len(c) <= 8 and len(set(c)) == len(c) and all(is_glyph(x) for x in c), c
    key = {"kind": kind, "context": c}
    if kind == "inhibit":
        assert is_glyph(candidate) and candidate not in c, candidate
        key["candidate"] = candidate
    if variant:
        key["variant"] = variant                       # a different question from the plain one at the same context
    if probe:
        key["probe"] = probe                           # e.g. {"control": "near"}: how the question was sampled
    q = dict(key, qid=uid({"continue": "Q", "inhibit": "I"}[kind], key), source=source or {})
    return q

# ------------------------------------------------------------------ prompts
OPENER = "Quick task, first impressions please."

def _lines(kind, sheet):
    r = R("sentence-order", {"sid": sheet["sid"]})
    if kind == "continue":
        intro = "Each item below shows symbols in a sequence; the last one listed is where the sequence has got to."
        opts = ['"continue": the symbols that come after the last one, in order, as many as come naturally (up to 24)',
                '"none": true, if nothing seems to come next']
        sents = ["Go by first impressions, and judge each item on its own rather than building a scheme across items.",
                 "Any symbol may come next, whether it is shown or not; it may have no name.",
                 '"none" is expected often and is fully valuable.']
        reply = '{"id": <id>, "continue": [...]} or {"id": <id>, "none": true}'
    else:
        intro = "Each item below shows symbols in a sequence, then one candidate symbol."
        opts = ['"answer": "yes", if the candidate comes directly after the last symbol of the sequence',
                '"answer": "no", if it does not',
                '"answer": "can\'t tell", if you can\'t tell']
        sents = ["Go by first impressions, and judge each item on its own rather than building a scheme across items."]
        reply = '{"id": <id>, "answer": "yes" | "no" | "can\'t tell"}'
    r.shuffle(opts); r.shuffle(sents)
    return intro, opts, sents, reply

# Prompt variants (concern 1: tagged, never mixed silently). None is the sheet's own prompt. "no-lookup" re-asks a
# sheet after the mind reached for a tool on it (Joseph, 2026-10-05: "have the second / subsequent attempt give a more
# explicit 'without looking up …' — just based on your best initial guess"). The wording avoids naming Unicode or its
# tables, which could itself steer a mind toward chart order.
VARIANTS = {None: None, "no-lookup": "Please answer without looking anything up: just your best initial guess.",
            "reasoned": None}
# "reasoned" (Joseph, 2026-10-05: a pass "where the tool works and you can have them give their reasoned one as well
# (probably especially useful for extending a sequence etc. -- where reasoning is fine -- verification/recognition !=
# generation (more complex))"): asked of reasoner minds that have utf-mcp's lookup tools. It differs from the plain
# prompt only where it must: no "first impressions", and leave to reason and look things up. Its answers are candidates
# (generation), kept apart from the tree's evidence; recognition of them is asked separately (inhibit questions).
REASONED_OPENER = "Take your time with this task."
FIRST_IMPRESSIONS = "Go by first impressions, and judge each item on its own rather than building a scheme across items."
REASONED_SENTENCE = ("Reason as much as you like, and look symbols up with the tools provided if that helps; judge each "
                     "item on its own rather than building a scheme across items.")
NONE_INVITE = '"none" is expected often and is fully valuable.'
# The plain prompt's NONE_INVITE suits first impressions; for generation it invited a quiet "none" even where a reasoned
# answer exists (live check 2026-10-05: `𐄉 𐄈 𐄇` (Aegean 9 8 7) -> none, no lookup made). The reasoned variant asks for
# the worked-out continuation instead, keeping "none" as an answer.
REASONED_NONE = 'If you can work out what comes next, give it, even if that takes some effort; "none" if nothing does.'

def prompt(sheet, variant=None):
    intro, opts, sents, reply = _lines(sheet["kind"], sheet)
    extra = [VARIANTS[variant]] if VARIANTS.get(variant) else []
    opener = OPENER
    if variant == "reasoned":
        opener = REASONED_OPENER
        sents = [REASONED_SENTENCE if x == FIRST_IMPRESSIONS else REASONED_NONE if x == NONE_INVITE else x for x in sents]
    L = [opener, intro, "For each item, answer with one of:"] + [f"  - {o}" for o in opts] + sents + extra + ["", "Items:"]
    for e in sheet["entries"]:
        o = {"id": e["id"], "s": e["context"]}
        if sheet["kind"] == "inhibit":
            o["candidate"] = e["candidate"]
        L.append(json.dumps(o, ensure_ascii=False))
    L += ["", "Reply with JSON only, no prose: {\"answers\": [ ... ]}, one entry per item, each " + reply + "."]
    return "\n".join(L)

# ------------------------------------------------------------------ sheets
def sheets(round_id, questions):
    """questions of one round -> sheets (1-5 of one kind and prompt variant each), fated. A question's variant is
    q["variant"] (None: the plain first-impression prompt)."""
    out = []
    for kind, variant in sorted({(q["kind"], q.get("variant")) for q in questions}, key=lambda kv: (kv[0], kv[1] or "")):
        qs = [q for q in questions if q["kind"] == kind and q.get("variant") == variant]
        fk = {"round": round_id, "kind": kind} if variant is None else {"round": round_id, "kind": kind, "variant": variant}
        R("sheet-order", fk).shuffle(qs)
        r = R("sheet-sizes", fk)
        i = 0
        while i < len(qs):
            n = min(len(qs) - i, r.randint(1, MAX_SHEET))
            chunk = qs[i:i + n]; i += n
            # no two questions sharing a context next to each other where avoidable
            chunk.sort(key=lambda q: (R("pos", {"qid": q["qid"], "round": round_id}).random()))
            sid = uid("S", {"round": round_id, "qids": [q["qid"] for q in chunk]})
            ents = []
            for pos, q in enumerate(chunk):
                e = {"id": pos, "qid": q["qid"], "context": q["context"]}
                if kind == "inhibit":
                    e["candidate"] = q["candidate"]
                ents.append(e)
            sh = {"sid": sid, "round": round_id, "kind": kind, "protocol": PROTOCOL, "entries": ents, "sheet_n": len(ents)}
            if variant:
                sh["variant"] = variant
            sh["prompt"] = prompt(sh, variant)
            out.append(sh)
    return out

# ------------------------------------------------------------------ parsing -> canonical records
def _answers(raw):
    if not raw:
        return None
    dec = json.JSONDecoder()
    for m in reversed([m.start() for m in re.finditer(r'\{\s*"answers"', raw)]):
        try:
            d, _ = dec.raw_decode(raw[m:])
            if isinstance(d.get("answers"), list):
                return d["answers"]
        except Exception:
            continue
    return None

AGY_HARVEST = HERE.parents[1] / "data" / "agy" / "brain"

def tool_calls(row):
    """the tools a call reached for: from the ledger (agy adapter a2-transcript on), else from the harvested agy
    transcript of older calls (data/agy/brain, copied 2026-10-05)"""
    res = row.get("result") or {}
    meta = res.get("adapter_meta") or {}
    if "tool_calls" in meta:
        return meta["tool_calls"]
    cid = meta.get("conversation")
    p = AGY_HARVEST / str(cid) / ".system_generated" / "logs" / "transcript_full.jsonl"
    if not cid or not p.exists():
        return []
    return [t for l in open(p) for t in (json.loads(l).get("tool_calls") or [])]

def tool_attempt(row):
    res = row.get("result") or {}
    return res.get("error") == "tool-attempt" or (not (res.get("raw") or "").strip() and bool(tool_calls(row)))

def good_row(row):
    return bool(row["result"].get("raw")) and not row["result"].get("error")

def records(sheet, ledger_rows, mind, family, judge, questions):
    """All ledger rows of one (sheet, mind) -> one canonical record per entry and prompt variant (METHODOLOGY §6)."""
    out = []
    for variant in dict.fromkeys(r.get("variant") for r in ledger_rows):
        out += _records(sheet, [r for r in ledger_rows if r.get("variant") == variant], mind, family, judge, questions, variant)
    return out

def _records(sheet, ledger_rows, mind, family, judge, questions, variant):
    good = [r for r in ledger_rows if good_row(r)]
    attempts = [r for r in ledger_rows if tool_attempt(r)]
    last = good[-1] if good else ledger_rows[-1]
    ans = _answers(last["result"].get("raw")) if good else None
    byid = {}
    for a in ans or []:
        if isinstance(a, dict) and isinstance(a.get("id"), int):
            byid.setdefault(a["id"], []).append(a)
    out = []
    for e in sheet["entries"]:
        q = questions[e["qid"]]
        key = [sheet["round"], sheet["sid"], mind, e["qid"]] + ([variant] if variant else [])
        rec = {"aid": "A" + hashlib.sha256(json.dumps(key, ensure_ascii=False).encode()).hexdigest()[:16],
               "era": "ctx", "round": sheet["round"], "sid": sheet["sid"], "qid": e["qid"], "mind": mind, "family": family,
               "model": judge.get("model"), "adapter": judge.get("adapter"), "kind": sheet["kind"], "context": list(e["context"]),
               "tags": {"protocol": PROTOCOL, "sheet_n": sheet["sheet_n"], "sheet_pos": e["id"], "calls_for_sheet": len(ledger_rows),
                        "prompt_sha256": last.get("prompt_sha256"), "system_sha256": last.get("system_sha256"),
                        "adapter_version": last.get("adapter_version"), "variant": variant, "tool_attempts": len(attempts),
                        "unicode": U.unidata_version,
                        "thinking_tokens": ((last.get("result") or {}).get("usage") or {}).get("thinking_tokens"),
                        "control": (q.get("probe") or {}).get("control")},
               "source": q.get("source", {})}
        if sheet["kind"] == "inhibit":
            rec["candidate"] = e["candidate"]
        if not good and attempts:
            rec["outcome"] = "tool-attempt"
            rec["tools"] = [{"name": t.get("name"), "args": t.get("args")} for r in attempts for t in tool_calls(r)][:6]
            out.append(rec); continue
        if not good:
            rec["outcome"] = "call-failed"; rec["reason"] = str(last["result"].get("error") or "empty output")[:200]
            out.append(rec); continue
        hits = byid.get(e["id"], [])
        if len(hits) != 1:
            rec["outcome"] = "unparsed"; rec["reason"] = "missing" if not hits else "duplicate-id"
            out.append(rec); continue
        a = hits[0]
        if sheet["kind"] == "continue":
            v = a.get("continue")
            if a.get("none") and not v:
                rec["outcome"] = "none"
            else:
                if isinstance(v, str):
                    v = list(v.replace(" ", "")) if " " not in v.strip() else v.split()
                if not isinstance(v, list) or not v:
                    rec["outcome"] = "unparsed"; rec["reason"] = "continue"
                else:
                    seq, other, vs = [], [], False
                    for pos, x in enumerate(v[:MAX_CONTINUE]):
                        t, s_ = clean(x); vs = vs or s_
                        if not t:
                            continue
                        if is_glyph(t):
                            seq.append(t)
                        else:
                            other.append({"s": t, "pos": pos, "class": content_class(t)})
                            break                 # the written path stops at the first non-glyph
                    rec["outcome"] = "continuation" if seq else ("other" if other else "unparsed")
                    rec["continuation"] = seq
                    if other:
                        rec["other_content"] = other
                    if vs:
                        rec["vs_stripped"] = True
        else:
            v = str(a.get("answer", "")).strip().lower().replace("’", "'")
            m = {"yes": "yes", "no": "no", "can't tell": "cant-tell", "cant tell": "cant-tell", "can not tell": "cant-tell",
                 "cannot tell": "cant-tell"}.get(v)
            if m:
                rec["outcome"] = m
            else:
                rec["outcome"] = "unparsed"; rec["reason"] = f"answer:{v[:20]}"
        out.append(rec)
    return out
