import collections, json
from vload import *
def verd(rid):
    ans = pair_answers(rid)
    byp = collections.defaultdict(dict)
    for (p, rep), v in ans.items():
        s = STIM[p]; byp[s["pair"]][s["order"]] = (v, s)
    out = {}
    for pair, d in byp.items():
        if 0 in d and 1 in d:
            out[pair] = verdict_pair(d[0][0], d[1][0], d[0][1]["a"], d[0][1]["b"])
    return out, ans
for rid in ["format-perp-pilotcond-sonnetagent", "format-perp-sheet-sonnet55", "format-perp-single-sonnet55", "format-perp-single-opus55"]:
    v, ans = verd(rid)
    c = collections.Counter((x[0] if isinstance(x, tuple) else x) for k, x in v.items() if k.startswith("pilot-replication"))
    n = sum(c.values())
    pp = collections.Counter(a[0] for (p, r), a in ans.items() if STIM[p]["stratum"] == "pilot-replication")
    q = pp["perp"] / sum(pp.values())
    print(rid, n, {k: round(c[k]/n, 2) for k in c}, "pres-perp", round(q, 2), "indep cperp expect", round(q*q, 2))
rs = [json.loads(l) for l in open(ROOT + "/data/runs-v1/format-perp-pilotcond-sonnetagent/ledger.jsonl")]
print([r["result"].get("model_reported") for r in rs], [r["result"].get("usage") for r in rs][:1])
# check pilotcond json a/b match stimulus pids
for r in rs:
    sheet = json.load(open(ROOT + f"/data/stimuli-v1/pilotcond/{r['sheet']}.json"))
    bad = sum(1 for it, m in zip(sheet, r["items"]) if (it["a"], it["b"]) != (STIM[m["pid"]]["a"], STIM[m["pid"]]["b"]) or it["id"] != m["id"])
    print(r["sheet"], "mismatches", bad, len(sheet))
