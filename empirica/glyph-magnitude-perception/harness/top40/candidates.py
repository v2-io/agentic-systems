#!/usr/bin/env python3
"""Top-40 candidates (exploratory; answers Joseph 2026-10-03: 'a top-40 sequences by stability/universality').

Step 1 (this script): from every surveys-v1 sequence record (pass-1 + capture-corrections), cluster records
across surveyors (Jaccard >= 0.5 on glyph sets), score each record by how many DISTINCT surveyors have a
matching record, and pick non-overlapping representatives (greedy; a representative suppresses later
records with Jaccard >= 0.34). This is anecdote-tier concordance used only to choose what to TEST; the
ranking that answers the question comes from the judge panel (harness/top40/score.py).
Writes data/stimuli-v1/top40-candidates.json and the test stimuli top40-steps.jsonl / top40-gestalt.jsonl.
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
            if r.get("type") != "sequence":
                continue
            g = glyph_list(r)
            if not g or len(g) < 3 or len(g) > 12:
                continue
            recs.append({"id": r["id"], "sv": r["surveyor"], "seq": g, "set": set(g),
                         "strength": (r.get("epistemics") or {}).get("felt_strength_verbatim")})
    jac = lambda a, b: len(a & b) / len(a | b)
    scored = []
    for r in recs:
        svs = {r["sv"]} | {o["sv"] for o in recs if o["sv"] != r["sv"] and jac(r["set"], o["set"]) >= 0.5}
        scored.append((len(svs), len(r["seq"]), r, sorted(svs)))
    scored.sort(key=lambda t: (-t[0], -t[1], t[2]["id"]))
    chosen = []
    for n, L, r, svs in scored:
        if any(jac(r["set"], c["set"]) >= 0.34 for c in chosen):
            continue
        chosen.append(dict(r, n_surveyors=n, surveyors=svs))
        if len(chosen) >= N_CAND:
            break
    out = [{"cand": i, "rec": c["id"], "surveyor": c["sv"], "glyphs": c["seq"], "n_surveyors": c["n_surveyors"],
            "surveyors": c["surveyors"], "felt_strength_verbatim": c["strength"]} for i, c in enumerate(chosen)]
    json.dump({"rule": __doc__, "candidates": out}, open(EXP / "data/stimuli-v1/top40-candidates.json", "w"), ensure_ascii=False, indent=1)
    with open(EXP / "data/stimuli-v1/top40-steps.jsonl", "w") as f:
        for c in out:
            g = c["glyphs"]
            for k, (x, y) in enumerate(zip(g, g[1:])):
                for order, (a, b) in enumerate(((x, y), (y, x))):
                    row = {"set": "top40", "cand": c["cand"], "step": k, "order": order, "a": a, "b": b,
                           "later": y}  # 'later' = the glyph written later in the surveyor's linearization
                    row["pid"] = "P" + digest(row)[:12]
                    f.write(json.dumps(row, ensure_ascii=False) + "\n")
    with open(EXP / "data/stimuli-v1/top40-gestalt.jsonl", "w") as f:
        for c in out:
            for sh in range(2):
                g = list(c["glyphs"]); rng(PROTOCOL, "top40-shuffle", {"cand": c["cand"], "shuffle": sh}).shuffle(g)
                row = {"set": "gestalt", "seq": f"cand-{c['cand']}", "kind": "top40", "shuffle": sh, "glyphs": g,
                       "intended": c["glyphs"], "src": c["rec"]}
                row["pid"] = "PG" + digest(row)[:12]
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
    for c in out:
        print(f"{c['cand']:2} {c['n_surveyors']}/7 {''.join(c['glyphs'])}  [{c['surveyor']}]")

if __name__ == "__main__":
    main()
