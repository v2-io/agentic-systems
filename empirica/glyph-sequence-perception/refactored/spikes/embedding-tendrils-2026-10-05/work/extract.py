#!/usr/bin/env python3
"""Extract every parsed answer through a round into one flat JSONL in this spike's derived/ dir.

Read-only use of the study harness (round.load_all + parse). Nothing in data/ or harness/ is written.
  python3 extract.py [UPTO]        default UPTO=r011  -> derived/answers-UPTO.jsonl
"""
import json, pathlib, sys
SPIKE = pathlib.Path(__file__).resolve().parents[1]
STUDY = SPIKE.parents[2]
sys.path.insert(0, str(STUDY / "harness/seq"))
import round as RD  # noqa: E402

upto = sys.argv[1] if len(sys.argv) > 1 else "r011"
fam = {k: v["family"] for k, v in json.load(open(STUDY / "harness/core/minds.json"))["minds"].items()}
items, pres, parsed, sheets = RD.load_all(STUDY / "data", upto=upto)
out = SPIKE / "derived" / f"answers-{upto}.jsonl"
n = 0
with open(out, "w") as f:
    for r in parsed:
        p = pres[r["pid"]]
        if p["round"] > upto:
            continue
        rec = {"round": p["round"], "mind": r["mind"], "family": fam.get(r["mind"], r["mind"]),
               "kind": p["kind"], "iid": p["iid"], "rep": p["rep"], "shown": p["shown"],
               "status": r["status"], "answer": r.get("answer")}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n"); n += 1
json.dump({iid: {"category": it.get("category"), "source": it.get("source"), "round": it.get("round")}
           for iid, it in items.items()}, open(SPIKE / "derived" / f"items-{upto}.json", "w"), ensure_ascii=False)
print(n, "->", out)
