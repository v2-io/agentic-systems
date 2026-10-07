#!/usr/bin/env python3
"""Build test round p001: the 43 contexts of prereg-flat-splits.json, each asked once more as a plain continue
question, one question to a sheet (a normal sheet size, 1-5; one avoids any effect of the sheet's other questions),
to sonnet55 and grok46, the two minds the prediction names. Sheets and prompts come from probe.py unchanged.

Then: python3 run.py ask p001 --minds sonnet55 grok46; python3 run.py record p001; python3 prereg_check.py.
The prediction was committed (dc42b1cb) before this round existed.

Generalised for later test rounds: prereg_round.py RID PREREG.json MIND ... (p002: prereg-third-minds.json, opus55
haiku45nt haiku45, committed at 1a998f00 before the round existed). With no arguments it builds p001 as before."""
import json, pathlib, sys

STUDY = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(STUDY / "probe"))
import probe as PR                                    # noqa: E402

RID, PREREG, MINDS = "p001", "prereg-flat-splits.json", ["sonnet55", "grok46"]
if len(sys.argv) > 3:
    RID, PREREG, MINDS = sys.argv[1], sys.argv[2], sys.argv[3:]
HERE = pathlib.Path(__file__).resolve().parent

def main():
    rd = STUDY / "data" / "rounds" / RID
    if (rd / "sheets.jsonl").exists():
        sys.exit(f"{RID} already built (truth is append-only)")
    pre = json.load(open(HERE / PREREG))
    src = {"round": RID, "why": "prereg", "prereg": "spikes/family-disagreement-2026-10-06/" + PREREG}
    qs = [PR.question("continue", c.get("context_glyphs") or list(c["context"]), source=src) for c in pre["contexts"]]
    sheets = []
    for q in qs:
        for s in PR.sheets(RID, [q]):
            s["minds"] = list(MINDS)
            sheets.append(s)
    rd.mkdir(parents=True)
    with open(rd / "questions.jsonl", "w") as f:
        for q in qs:
            f.write(json.dumps(q, ensure_ascii=False) + "\n")
    with open(rd / "sheets.jsonl", "w") as f:
        for s in sheets:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    import unicodedata
    json.dump({"round": RID, "what": "pre-registered test of the family-disagreement spike's flat-split prediction",
               "prediction": "spikes/family-disagreement-2026-10-06/" + PREREG,
               "questions": len(qs), "sheets": len(sheets), "minds": MINDS, "unicode": unicodedata.unidata_version},
              open(rd / "plan.json", "w"), ensure_ascii=False, indent=1)
    print(f"{RID}: {len(qs)} questions, {len(sheets)} sheets, minds {MINDS}")

if __name__ == "__main__":
    main()
