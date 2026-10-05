#!/usr/bin/env python3
"""Concern 4: port the triad era's answers into the refactored study's canonical answer records (METHODOLOGY §6).

  port_triad_era.py            -> ../data/answers/triad-era.jsonl  and  ../data/answers/PORT-REPORT.md

Answers only: nothing derived (rows, fits, standings) crosses. Every record keeps its tags (round, sheet, position,
sheet size, offered options, mind, family, model, adapter, prompt and system hashes, parser). The item's source --
why it was asked -- travels as `source`, which the tree never reads.

Source of truth read: ../../data/rounds/*/{items,presentations,sheets}.jsonl and raw/<mind>/ledger.jsonl (verbatim
model output), re-parsed with the triad-era parser (../../harness/seq/parse.py) exactly as the triad era did. Per
(sheet, mind) the last successful call is the answer (the triad era's rule: earlier attempts are retries); a sheet
whose every call for that mind failed yields one `call-failed` record per presentation, so failures are not silently
missing (the pilot found they cluster by glyph).

Record kinds (`kind`) and outcomes (`outcome`):
  next      context -> continuation: outcome "proposals" (proposals = single glyphs, rank kept) or "none"
  between   left GAP right -> outcome "proposals" or "none"  (two-sided fill; not a continuation)
  triad     outcome "mid" / "two" / "none" / "tie2" / "tie3"   (constraints, never edges)
  order     outcome "lines" (lines, extra, omitted) or "none"  (constraints, never edges)
  any kind  outcome "unparsed" (reason) or "call-failed" (reason)
Proposal content check (the refactored study's own glyph definition, METHODOLOGY §6): after NFC and after stripping
variation selectors U+FE0E/U+FE0F (presentation requests, recorded in `vs_stripped`), a proposal is a GLYPH if it is
ONE assigned codepoint of general category L, N, P or S that is not whitespace. Unlike the triad era's ok_glyph there
is no banned list: its {⟂, ⊥, ≈} never appeared in any prompt (checked 2026-10-05 over every ledger), so excluding
them would have removed real proposals (≈ ×11). Everything else is kept in `other_content` with its rank and a class,
never split into glyphs:
  unassigned   one codepoint with no character assigned (a mind extending a block past its end: U+1D2F4, U+1F02F)
  mark         one combining mark (category M), e.g. Balinese ᬄ
  string       several codepoints: numerals like "10", "١٠", words and fragments, keycaps like 3️⃣
  other        a control, format or whitespace character
"""
import collections, hashlib, json, pathlib, sys, unicodedata as U

HERE = pathlib.Path(__file__).resolve()
STUDY = HERE.parents[2]                       # .../glyph-sequence-perception
OUT = HERE.parents[1] / "data" / "answers"
sys.path.insert(0, str(STUDY / "harness" / "seq"))
from common import read_jsonl                 # noqa: E402  (triad-era helper, used as-is)
import parse as P                              # noqa: E402

VS = {"︎", "️"}

def families():
    m = json.load(open(STUDY / "harness" / "core" / "minds.json"))["minds"]
    return {k: v["family"] for k, v in m.items()}

def is_glyph(ch):
    return len(ch) == 1 and U.category(ch)[0] in "LNPS" and not ch.isspace()

def content_class(t):
    if len(t) != 1:
        return "string"
    cat = U.category(t)
    if cat == "Cn":
        return "unassigned"
    if cat[0] == "M":
        return "mark"
    return "other"

def glyph_of(s):
    """-> (glyph or None, cleaned text, vs_stripped)"""
    t = U.normalize("NFC", s).strip()
    t2 = "".join(ch for ch in t if ch not in VS)
    return (t2 if is_glyph(t2) else None), t2, (t2 != t)

def split_props(props):
    gl, other, vs = [], [], False
    for rank, x in enumerate(props, 1):
        g, t, stripped = glyph_of(x)
        vs = vs or stripped
        if g is not None:
            gl.append({"g": g, "rank": rank})
        else:
            other.append({"s": x, "rank": rank, "class": content_class(t)})
    return gl, other, vs

def aid(*parts):
    return "A" + hashlib.sha256(json.dumps(parts, ensure_ascii=False).encode()).hexdigest()[:16]

def main():
    fam = families()
    rows, rep = [], collections.Counter()
    excluded = collections.Counter(); other_examples = collections.Counter()
    for rd in sorted(p for p in (STUDY / "data" / "rounds").iterdir() if p.is_dir()):
        rid = rd.name
        items = {it["iid"]: it for it in read_jsonl(rd / "items.jsonl")}
        pres = {p["pid"]: p for p in read_jsonl(rd / "presentations.jsonl")}
        sheets = {s["sid"]: s for s in read_jsonl(rd / "sheets.jsonl")}
        # items asked in earlier rounds (follow-ups) are listed only there
        for prev in (STUDY / "data" / "rounds").iterdir():
            if prev.is_dir() and prev.name < rid:
                for it in read_jsonl(prev / "items.jsonl"):
                    items.setdefault(it["iid"], it)
        for f in sorted((rd / "raw").glob("*/ledger.jsonl")):
            mind = f.parent.name
            calls = collections.defaultdict(list)
            for row in read_jsonl(f):
                calls[row["sid"]].append(row)
            for sid, rs in calls.items():
                sh = sheets.get(sid)
                if sh is None:
                    excluded["ledger row for an unknown sheet"] += 1
                    continue
                good = [r for r in rs if r["result"].get("raw") and not r["result"].get("error")]
                last = good[-1] if good else rs[-1]
                parsed = P.parse_sheet(last["result"]["raw"], sh) if good else {}
                base_tags = {"protocol": last.get("protocol"), "prompt_sha256": last.get("prompt_sha256"),
                             "system_sha256": last.get("system_sha256"), "adapter_version": last.get("adapter_version"),
                             "parser": P.PARSER, "calls_for_sheet": len(rs), "factors": sh.get("factors")}
                judge = last.get("judge") or {}
                for e in sh["entries"]:
                    p = pres[e["pid"]]; it = items.get(p["iid"], {})
                    rec = {"aid": aid(rid, sid, mind, e["pid"]), "era": "triad", "round": rid, "sid": sid,
                           "pid": e["pid"], "iid": p["iid"], "mind": mind, "family": fam.get(mind, judge.get("family")),
                           "model": judge.get("model"), "adapter": judge.get("adapter"), "kind": p["kind"],
                           "shown": p["shown"],
                           "tags": dict(base_tags, rep=p.get("rep"), sheet_n=p.get("sheet_n"), sheet_pos=p.get("sheet_pos"),
                                        co_sheet=p.get("co_sheet")),
                           "source": it.get("source", {})}
                    if p["kind"] == "next":
                        rec["context"] = list(p["shown"])
                    elif p["kind"] == "between":
                        gi = p["shown"].index("GAP"); rec["left"], rec["right"] = p["shown"][:gi], p["shown"][gi + 1:]
                    if not good:
                        rec["outcome"] = "call-failed"
                        rec["reason"] = str(last["result"].get("error") or "empty output")[:200]
                    else:
                        v = parsed.get(e["pid"], {"status": "unparsed", "why": "missing"})
                        if v["status"] != "ok":
                            rec["outcome"] = "unparsed"; rec["reason"] = v.get("why")
                        else:
                            a = v["answer"]
                            if p["kind"] in ("next", "between"):
                                if a.get("none"):
                                    rec["outcome"] = "none"
                                else:
                                    gl, other, vs = split_props(a["proposals"])
                                    rec["outcome"] = "proposals"; rec["proposals"] = gl
                                    if other:
                                        rec["other_content"] = other
                                        for o in other:
                                            other_examples[(o["class"], o["s"][:12])] += 1
                                    if vs:
                                        rec["vs_stripped"] = True
                            elif p["kind"] == "triad":
                                rec["outcome"] = a[0]; rec["answer"] = list(a)
                            elif p["kind"] == "order":
                                if a.get("none"):
                                    rec["outcome"] = "none"
                                else:
                                    rec["outcome"] = "lines"
                                    rec["answer"] = {"lines": a.get("lines") or [], "extra": a.get("extra") or [],
                                                     "omitted": a.get("omitted") or []}
                            else:
                                rec["outcome"] = "unparsed"; rec["reason"] = f"kind {p['kind']} not in the triad era"
                    rows.append(rec)
                    rep[(rid, p["kind"], rec["outcome"])] += 1
    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / "triad-era.jsonl", "w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")
    write_report(rows, rep, excluded, other_examples)
    print(f"ported {len(rows)} answer records -> {OUT / 'triad-era.jsonl'}")

def write_report(rows, rep, excluded, other_examples):
    kinds = ["next", "between", "triad", "order"]
    outcomes = sorted({k[2] for k in rep})
    rounds = sorted({k[0] for k in rep})
    L = ["# PORT-REPORT: triad era → canonical answer records", "",
         f"*Generated by `refactored/port/port_triad_era.py` from the verbatim ledgers in `data/rounds/` ({rounds[0]}–{rounds[-1]}), re-parsed with the triad-era parser `{P.PARSER}`. One record per (presentation, mind) for every sheet a mind was called on. Nothing derived is ported (METHODOLOGY §6).*", "",
         f"**{len(rows)} records.** `triad-era.jsonl` is deterministic and regenerable from the committed ledgers, so it is not committed itself (`.gitignore`); rerun `port_triad_era.py` then `spotcheck.py` to rebuild it and this report.", "",
         "## By kind and outcome", "",
         "| kind | " + " | ".join(outcomes) + " | total |", "|---|" + "---|" * (len(outcomes) + 1)]
    for k in kinds:
        tot = sum(v for (r, kk, o), v in rep.items() if kk == k)
        L.append(f"| {k} | " + " | ".join(str(sum(v for (r, kk, oo), v in rep.items() if kk == k and oo == o)) for o in outcomes) + f" | {tot} |")
    L += ["", "## By round", "", "| round | records | call-failed | unparsed |", "|---|---|---|---|"]
    for r in rounds:
        L.append(f"| {r} | {sum(v for (rr, k, o), v in rep.items() if rr == r)} | {sum(v for (rr, k, o), v in rep.items() if rr == r and o == 'call-failed')} | {sum(v for (rr, k, o), v in rep.items() if rr == r and o == 'unparsed')} |")
    fam_mind = collections.Counter((r["family"], r["mind"]) for r in rows)
    L += ["", "## By mind", "", "| family | mind | records |", "|---|---|---|"]
    L += [f"| {f} | {m} | {n} |" for (f, m), n in sorted(fam_mind.items())]
    props = [p for r in rows for p in r.get("proposals", [])]
    other = [o for r in rows for o in r.get("other_content", [])]
    L += ["", "## Proposal content (next and between)", "",
          f"- **{len(props)} proposals are single glyphs** and enter the tree as continuations or fills.",
          f"- **{len(other)} proposals are not single glyphs.** They are kept in `other_content` with their rank and class, never split:"]
    for cls in ("string", "unassigned", "mark", "other"):
        ex = [(s_, n) for (c_, s_), n in other_examples.most_common() if c_ == cls]
        if ex:
            L.append(f"  - **{cls}** ({sum(n for _, n in ex)}): " + ", ".join(f"`{s_}`" + (f" (U+{ord(s_):04X})" if len(s_) == 1 else "") + f" ×{n}" for s_, n in ex[:14]) + ("…" if len(ex) > 14 else ""))
    L += [
          f"- **{sum(1 for r in rows if r.get('vs_stripped'))} answers had a variation selector (U+FE0E/U+FE0F) stripped** from a proposal before the glyph check (`vs_stripped`)."]
    reasons = collections.Counter((r["kind"], (r.get("reason") or "")[:60]) for r in rows if r["outcome"] in ("unparsed", "call-failed"))
    L += ["", "## Unparsed and failed calls, by reason (kept as records)", "", "| kind | reason | records |", "|---|---|---|"]
    L += [f"| {k} | {why} | {n} |" for (k, why), n in reasons.most_common(25)]
    if excluded:
        L += ["", "## Excluded", ""] + [f"- {why}: {n}" for why, n in excluded.items()]
    L += ["", "## Not ported", "",
          "- **Derived artifacts:** grown rows (`data/growth/`), fits (`fit.json`, `basis-fit.json`), standings, progress, plans and queues. Each carries a rule of the old machinery.",
          "- **The magnitude era** (`.archive/2026-10-04-magnitude-era/`), which asked a different question.",
          "- **Survey records** (`data/surveys-v1/`). They are seeds (concern 3) and never answers.", ""]
    (OUT / "PORT-REPORT.md").write_text("\n".join(L))

if __name__ == "__main__":
    main()
