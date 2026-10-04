#!/usr/bin/env python3
"""Top-40 candidates (exploratory; answers Joseph 2026-10-03: 'a top-40 sequences by stability/universality').

Step 1 (this script): from every surveys-v1 sequence record (pass-1 + capture-corrections), cluster records
across surveyors (Jaccard >= 0.5 on glyph sets), score each record by how many DISTINCT surveyors have a
matching record, and pick non-overlapping representatives (greedy; a representative suppresses later
records with Jaccard >= 0.34). This is anecdote-tier concordance used only to choose what to TEST; the
ranking that answers the question comes from the judge panel (harness/top40/score.py).
Writes data/stimuli-v1/top40-candidates.json and the test stimuli top40-steps.jsonl / top40-gestalt.jsonl.

History: the first selection (batch a, candidates 0-63, already run) read only records whose kind is in `type`,
which silently dropped grok-1, sonnet-survey-3 and sonnet-survey-4 (their extractions use `record_type`). This
version keeps batch a unchanged, recomputes every candidate's surveyor support over all 7 surveys, and appends a
batch-b supplement (records with support from >= 2 surveyors not already covered), tested via top40b-*.jsonl.
"""
import json, pathlib, sys, unicodedata
from collections import defaultdict
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "runner"))
from fate import rng, digest
from instruments import PROTOCOL

EXP = pathlib.Path(__file__).resolve().parents[2]
N_CAND = 64

def glyph_list(r):
    out = []
    for c in r.get("codepoints") or []:
        if not isinstance(c, str) or not c.startswith("U+"):
            continue
        try:
            ch = chr(int(c[2:], 16))
        except ValueError:
            continue
        if ch.isspace() or unicodedata.category(ch) in ("Mn", "Me", "Cf") or 0xFE00 <= ord(ch) <= 0xFE0F:
            continue
        if ch in ("≈", "⟂", "⊥"):
            return None  # would collide with the response vocabulary
        if ch not in out:
            out.append(ch)
    return out

def main():
    recs = []
    for f in sorted((EXP / "data/surveys-v1/extracted").glob("*.jsonl")) + sorted((EXP / "data/surveys-v1/extracted/corrections").glob("*.jsonl")):
        for line in open(f):
            if not line.strip():
                continue
            r = json.loads(line)
            if (r.get("type") or r.get("record_type")) != "sequence":  # 3 of 7 extractions use record_type
                continue
            g = glyph_list(r)
            if not g or len(g) < 3 or len(g) > 12:
                continue
            recs.append({"id": r["id"], "sv": r["surveyor"], "seq": g, "set": set(g),
                         "strength": (r.get("epistemics") or {}).get("felt_strength_verbatim")})
    jac = lambda a, b: len(a & b) / len(a | b)
    def support(gset):
        return sorted({o["sv"] for o in recs if jac(gset, o["set"]) >= 0.5})
    path = EXP / "data/stimuli-v1/top40-candidates.json"
    existing = json.load(open(path))["candidates"] if path.exists() else []
    # v1 candidates (selected 2026-10-03 from only 4 surveyors because of the record_type bug) keep their ids
    # and stimuli; their surveyor support is recomputed over all 7 surveys.
    for c in existing:
        sv = support(set(c["glyphs"])); c["surveyors"] = sv; c["n_surveyors"] = len(sv)
    scored = []
    for r in recs:
        sv = support(r["set"]); scored.append((len(sv), len(r["seq"]), r, sv))
    scored.sort(key=lambda t: (-t[0], -t[1], t[2]["id"]))
    supplement = []
    for n, L, r, sv in scored:
        if n < 2:
            break
        if any(jac(r["set"], set(c["glyphs"])) >= 0.34 for c in existing + supplement):
            continue
        supplement.append({"cand": len(existing) + len(supplement), "rec": r["id"], "surveyor": r["sv"], "glyphs": r["seq"],
                           "n_surveyors": n, "surveyors": sv, "felt_strength_verbatim": r["strength"], "batch": "b"})
    if not existing:
        sys.exit("expected the v1 candidate file; this script now only appends a supplement")
    for c in existing:
        c.setdefault("batch", "a")
    json.dump({"rule": __doc__, "candidates": existing + supplement}, open(path, "w"), ensure_ascii=False, indent=1)
    with open(EXP / "data/stimuli-v1/top40b-steps.jsonl", "w") as f:
        for c in supplement:
            g = c["glyphs"]
            for k, (x, y) in enumerate(zip(g, g[1:])):
                for order, (a, b) in enumerate(((x, y), (y, x))):
                    row = {"set": "top40", "cand": c["cand"], "step": k, "order": order, "a": a, "b": b, "later": y}
                    row["pid"] = "P" + digest(row)[:12]
                    f.write(json.dumps(row, ensure_ascii=False) + "\n")
    with open(EXP / "data/stimuli-v1/top40b-gestalt.jsonl", "w") as f:
        for c in supplement:
            for sh in range(2):
                g = list(c["glyphs"]); rng(PROTOCOL, "top40-shuffle", {"cand": c["cand"], "shuffle": sh}).shuffle(g)
                row = {"set": "gestalt", "seq": f"cand-{c['cand']}", "kind": "top40", "shuffle": sh, "glyphs": g,
                       "intended": c["glyphs"], "src": c["rec"]}
                row["pid"] = "PG" + digest(row)[:12]
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
    for c in existing + supplement:
        print(f"{c['cand']:2} {c['batch']} {c['n_surveyors']}/7 {''.join(c['glyphs'])}  [{c['surveyor']}]")

if __name__ == "__main__":
    main()
