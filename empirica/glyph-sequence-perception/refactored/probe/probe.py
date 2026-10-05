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
def question(kind, context, candidate=None, source=None):
    c = list(context)
    assert 2 <= len(c) <= 8 and len(set(c)) == len(c) and all(is_glyph(x) for x in c), c
    key = {"kind": kind, "context": c}
    if kind == "inhibit":
        assert is_glyph(candidate) and candidate not in c, candidate
        key["candidate"] = candidate
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

def prompt(sheet):
    intro, opts, sents, reply = _lines(sheet["kind"], sheet)
    L = [OPENER, intro, "For each item, answer with one of:"] + [f"  - {o}" for o in opts] + sents + ["", "Items:"]
    for e in sheet["entries"]:
        o = {"id": e["id"], "s": e["context"]}
        if sheet["kind"] == "inhibit":
            o["candidate"] = e["candidate"]
        L.append(json.dumps(o, ensure_ascii=False))
    L += ["", "Reply with JSON only, no prose: {\"answers\": [ ... ]}, one entry per item, each " + reply + "."]
    return "\n".join(L)

# ------------------------------------------------------------------ sheets
def sheets(round_id, questions):
    """questions of one round -> sheets (1-5 of one kind each), fated."""
    out = []
    for kind in KINDS:
        qs = [q for q in questions if q["kind"] == kind]
        R("sheet-order", {"round": round_id, "kind": kind}).shuffle(qs)
        r = R("sheet-sizes", {"round": round_id, "kind": kind})
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
            sh["prompt"] = prompt(sh)
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

def records(sheet, ledger_rows, mind, family, judge, questions):
    """All ledger rows of one (sheet, mind) -> one canonical record per entry (METHODOLOGY §6 record shape)."""
    good = [r for r in ledger_rows if r["result"].get("raw") and not r["result"].get("error")]
    last = good[-1] if good else ledger_rows[-1]
    ans = _answers(last["result"].get("raw")) if good else None
    byid = {}
    for a in ans or []:
        if isinstance(a, dict) and isinstance(a.get("id"), int):
            byid.setdefault(a["id"], []).append(a)
    out = []
    for e in sheet["entries"]:
        q = questions[e["qid"]]
        rec = {"aid": "A" + hashlib.sha256(json.dumps([sheet["round"], sheet["sid"], mind, e["qid"]], ensure_ascii=False).encode()).hexdigest()[:16],
               "era": "ctx", "round": sheet["round"], "sid": sheet["sid"], "qid": e["qid"], "mind": mind, "family": family,
               "model": judge.get("model"), "adapter": judge.get("adapter"), "kind": sheet["kind"], "context": list(e["context"]),
               "tags": {"protocol": PROTOCOL, "sheet_n": sheet["sheet_n"], "sheet_pos": e["id"], "calls_for_sheet": len(ledger_rows),
                        "prompt_sha256": last.get("prompt_sha256"), "system_sha256": last.get("system_sha256"),
                        "adapter_version": last.get("adapter_version")},
               "source": q.get("source", {})}
        if sheet["kind"] == "inhibit":
            rec["candidate"] = e["candidate"]
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
