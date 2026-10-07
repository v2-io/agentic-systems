"""De novo 3: a naive competitor for round p002, written before any p002 answer was read.
'Local pool': a mind's P(stop) at a flat context is its own answers there, shrunk toward its own pooled rate over the 43
flat contexts (Jeffreys on the pool; a = 4 pseudo-answers per context). No fitted model, no other mind's answers.
Inputs: only prereg-third-minds.json's answers_so_far_incl_p001 (snapshot + p001)."""
import json, datetime, pathlib
HERE = pathlib.Path(__file__).resolve().parent
d = json.load(open(HERE.parent / "prereg-third-minds.json"))
A = 4.0
def band(ps, lo=0.025, hi=0.975):
    dist = [1.0]
    for p in ps:
        nd = [0.0] * (len(dist) + 1)
        for k, v in enumerate(dist): nd[k] += v * (1 - p); nd[k + 1] += v * p
        dist = nd
    c = 0.0; a = b = None
    for k, v in enumerate(dist):
        c += v
        if a is None and c >= lo: a = k
        if b is None and c >= hi: b = k
    return a, b
out = {"what": __doc__, "written": datetime.datetime.now().astimezone().isoformat(timespec="seconds"), "pool": {}, "p_stop": {}, "expected": {}}
for m in ("opus55", "haiku45nt", "haiku45"):
    k = sum(c["answers_so_far_incl_p001"].get(m, [0, 0])[0] for c in d["contexts"])
    n = sum(c["answers_so_far_incl_p001"].get(m, [0, 0])[1] for c in d["contexts"])
    r = (k + 0.5) / (n + 1); out["pool"][m] = [k, n, round(r, 4)]
    ps = {}
    for c in d["contexts"]:
        kk, nn = c["answers_so_far_incl_p001"].get(m, [0, 0])
        ps[c["context"]] = round((kk + A * r) / (nn + A), 4)
    out["p_stop"][m] = ps
    v = list(ps.values()); out["expected"][m] = [round(sum(v), 2), band(v)]
json.dump(out, open(HERE / "b-pred-p002.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps({k: out[k] for k in ("written", "pool", "expected")}))
