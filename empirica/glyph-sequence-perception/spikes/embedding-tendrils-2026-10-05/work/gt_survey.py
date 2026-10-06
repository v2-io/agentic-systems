#!/usr/bin/env python3
"""A second, independently-biased reference set: the 2026-08-25 free surveys (data/surveys-v1/extracted, read only).

Each survey record of type 'sequence' is one surveyor's own written order. Every consecutive pair (in both reading
directions) is an instance: node = g_i, context = the record up to g_i, truth = g_{i+1}. 'fams_first' holds the
surveyors (not families) who wrote that step, so truth 'first1' = any surveyor, 'first2' = two or more surveyors.
Bias, stated: surveyors swept Unicode PANES (blocks), so within-block, codepoint-adjacent runs are over-represented.

  python3 gt_survey.py  -> derived/gt-survey.json
"""
import json
from lib import DER, SPIKE, ok

STUDY = SPIKE.parents[2]
src = sorted((STUDY / "data/surveys-v1/extracted").glob("*.jsonl")) + \
      sorted((STUDY / "data/surveys-v1/extracted/corrections").glob("*.jsonl"))
recs = {}
for f in src:
    for l in open(f):
        r = json.loads(l)
        if (r.get("type") or r.get("record_type")) != "sequence":
            continue
        g = []
        for c in r.get("codepoints") or []:
            if isinstance(c, str) and c.startswith("U+"):
                try:
                    g.append(chr(int(c[2:].split()[0], 16)))
                except ValueError:
                    pass
        g = [x for x in dict.fromkeys(g) if ok(x)]
        if len(g) >= 2:
            recs[r["id"]] = (r.get("surveyor"), g)      # corrections (read last) replace by id

step_by = {}
inst = {}
for rid, (sv, g) in recs.items():
    for seq, d in ((g, ">"), (list(reversed(g)), "<")):
        for i in range(len(seq) - 1):
            q, nx = seq[i], seq[i + 1]
            step_by.setdefault((q, nx), set()).add(sv)
            inst[f"{rid}{d}{i}"] = {"node": q, "ctx": seq[:i + 1], "ctx_all": sorted(set(seq[:i + 1])),
                                    "kind": "survey", "round": "survey", "category": ["survey", sv], "next": nx}
for k, I in inst.items():
    nx = I.pop("next")
    sv = sorted(step_by[(I["node"], nx)])
    I["props"] = {nx: {"fams": sv, "fams_first": sv, "minds": sv, "n": len(sv), "n_first": len(sv)}}
json.dump({"upto": "survey", "instances": inst, "triads": {}, "orderadj": {}},
          open(DER / "gt-survey.json", "w"), ensure_ascii=False)
print(f"{len(recs)} sequence records -> {len(inst)} instances; steps written by >=2 surveyors: "
      f"{sum(1 for v in step_by.values() if len(v) >= 2)} of {len(step_by)}")
