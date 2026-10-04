"""Pilot-condition arm: sonnet subagents, pilot wording, 80-item sheets, pilot-replication stratum only.
Dissolution computed exactly as P1, compared with the API sonnet55 single/sheet on the same 160 pairs."""
import collections, json
from common import *
rows = stim_rows("format-pairs.jsonl")
def pv_for(run):
    pres = collections.defaultdict(list)
    for r in ledger(run):
        if not r["result"].get("raw"): continue
        items = [{"id": it["id"], "a": rows[it["pid"]]["a"], "b": rows[it["pid"]]["b"]} for it in r["items"]]
        p = I.parse_sheet(r["result"]["raw"], items)
        for it in r["items"]:
            v = p.get(it["id"], ("unparsed", None, None)); pres[it["pid"]].append((*v, None))
    sub = {pid: st for pid, st in rows.items() if st["stratum"] == "pilot-replication"}
    by = collections.defaultdict(dict)
    for pid, st in sub.items(): by[st["pair"]][pid] = st
    out = {}
    for pair, rs in by.items():
        (k, v), = pair_verdicts(rs, {p: pres[p] for p in rs if p in pres}).items()
        out[pair] = v[0]
    pc = collections.Counter(pres[p][-1][0] for p in sub if p in pres)
    return out, pc
res = {}
for lab, tie_run, perp_run, single in (("sonnet-agent pilotcond", "format-tie-pilotcond-sonnetagent", "format-perp-pilotcond-sonnetagent", False),):
    t, tpc = pv_for(tie_run); p, ppc = pv_for(perp_run)
    base = [x for x in t if t[x] == "cdir" and p.get(x) not in (None, "incomplete")]
    d = sum(1 for x in base if p[x] == "cperp"); lo, hi = wilson(d, len(base))
    print(f"{lab}: tie mix {dict(collections.Counter(t.values()))}")
    print(f"   perp mix {dict(collections.Counter(p.values()))}; perp presentation verdicts {dict(ppc)}")
    print(f"   P1 dissolution {d}/{len(base)} = {d/len(base):.2f} [{lo:.2f},{hi:.2f}]; any-⟂-retreat (not cdir under perp) = {sum(1 for x in base if p[x]!='cdir')/len(base):.2f}")
    for r in ledger(perp_run)[:1]:
        print("   model_reported:", r["result"].get("model_reported"), "tool_uses:", r["result"].get("adapter_meta"))
