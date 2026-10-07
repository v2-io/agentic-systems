#!/usr/bin/env python3
"""Build a test round (p…): named runs asked of named minds with one question kind, each beside the same question
about its own glyphs shuffled (fated). Test rounds are not planned or drained; run.py asks, records and commits them
(run.py test_rounds). Questions go one to a sheet.

Usage: python3 probe/test_round.py RID KIND[,KIND...] "MIND MIND ..." RUN [RUN ...]
First use (2026-10-06): p003, Joseph's runs for the insert and remove questions --
  "There are a lot of these that I would love to ask -- 'can you make this sequence longer by inserting one or more
  missing symbols?' ┉┈┄─━▬█▌▍  _-∼≋  ˚˙·∣∥⫴  ↑↗→↘↓ (and, occasionally -- 'by removing one or more symbols')"."""
import json, pathlib, sys, unicodedata

HERE = pathlib.Path(__file__).resolve()
STUDY = HERE.parents[1]
sys.path.insert(0, str(HERE.parent))
import probe as PR                                    # noqa: E402

def main():
    rid, kinds, minds, runs = sys.argv[1], sys.argv[2].split(","), sys.argv[3].split(), sys.argv[4:]
    rd = STUDY / "data" / "rounds" / rid
    if (rd / "sheets.jsonl").exists():
        sys.exit(f"{rid} already built (truth is append-only)")
    qs = []
    for kind in kinds:
        for run in runs:
            g = list(run)
            src = {"round": rid, "why": "test", "kind": kind}
            qs.append(PR.question(kind, g, source=src))
            ctl = PR.shuffled_control(g, rid)
            if ctl:
                qs.append(PR.question(kind, ctl, source=dict(src, why="control", control="shuffled", of="".join(g)),
                                      probe={"control": "shuffled", "of": "".join(g)}))
    sheets = []
    for q in qs:
        for sh in PR.sheets(rid, [q]):
            sh["minds"] = list(minds)
            sheets.append(sh)
    rd.mkdir(parents=True)
    with open(rd / "questions.jsonl", "w") as f:
        for q in qs:
            f.write(json.dumps(q, ensure_ascii=False) + "\n")
    with open(rd / "sheets.jsonl", "w") as f:
        for sh in sheets:
            f.write(json.dumps(sh, ensure_ascii=False) + "\n")
    json.dump({"round": rid, "what": "test round (probe/test_round.py)", "kinds": kinds, "runs": runs, "minds": minds,
               "questions": len(qs), "sheets": len(sheets), "unicode": unicodedata.unidata_version},
              open(rd / "plan.json", "w"), ensure_ascii=False, indent=1)
    print(f"{rid}: {len(qs)} questions, {len(sheets)} sheets, minds {minds}")

if __name__ == "__main__":
    main()
