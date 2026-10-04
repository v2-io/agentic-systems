import collections, itertools
from vload import *
ORDER = ["·","╶","╌","╍","━","═","⚬","○","◎","◉","⬤"]
idx = {g: i for i, g in enumerate(ORDER)}
LINE = set(ORDER[:6]); CIRC = set(ORDER[6:])
def branch(a, b):
    if a in LINE and b in LINE: return "line"
    if a in CIRC and b in CIRC: return "circ"
    return "seam"
FRONT = ["opus55","sonnet55","sonnet5","haiku45","sonnet55[sheet]","grok46[sheet]","gemini31pro[sheet]","gemini38flash[sheet]"]
allv = {}
for rid in runs("signa-perp-"):
    j = rid.split("-", 3)[3].replace("-sheet", "") + ("[sheet]" if "-sheet-" in rid else "")
    ans = pair_answers(rid)
    byp = collections.defaultdict(dict)
    for (p, rep), v in ans.items():
        s = STIM[p]; key = frozenset((s["a"], s["b"])); byp[key][s["order"]] = (v, s)
    V = {}
    nfirst = ndir = 0; unp = 0
    for k, d in byp.items():
        for o, (v, s) in d.items():
            if v[0] == "dir": ndir += 1; nfirst += v[1] == s["a"]
            if v[0] == "unparsed": unp += 1
        (v0, s0), (v1, s1) = d[0], d[1]
        V[k] = (verdict_pair(v0, v1, s0["a"], s0["b"]), v0, v1, s0)
    allv[j] = V
    c = collections.Counter()
    for k, (vd, v0, v1, s0) in V.items():
        a, b = s0["a"], s0["b"]; br = branch(a, b)
        kind = vd[0] if isinstance(vd, tuple) else vd
        c[(br, kind)] += 1
        if kind == "cdir":
            hi = max(a, b, key=lambda g: idx[g]); c[(br, "agree")] += vd[1] == hi
        if kind == "flip":
            c[(br, "flip_sameslot")] += (v0[1] == s0["a"]) == (v1[1] == s0["b"])  # same slot: first both or second both
    print(f"{j:22s} line cdir {c[('line','cdir')]:2d} agree {c[('line','agree')]:2d} flips {c[('line','flip')]} | circ cdir {c[('circ','cdir')]:2d} agree {c[('circ','agree')]:2d} | seam cperp {c[('seam','cperp')]:2d}/30 cdir {c[('seam','cdir')]:2d} agree {c[('seam','agree')]:2d} mixed {c[('seam','mixed')]} flip {c[('seam','flip')]} | P(first|dir) {nfirst/max(ndir,1):.2f} unp {unp}")
# within-branch and seam aggregates over frontier
tot = collections.Counter(); dis = []
for j in FRONT:
    for k, (vd, v0, v1, s0) in allv[j].items():
        if not (isinstance(vd, tuple) and vd[0] == "cdir"): continue
        a, b = s0["a"], s0["b"]; br = "within" if branch(a, b) != "seam" else "seam"
        hi = max(a, b, key=lambda g: idx[g]); tot[(br, "n")] += 1; tot[(br, "a")] += vd[1] == hi
        if vd[1] != hi: dis.append((j, br, vd[1], (a if vd[1] == b else b)))
print(dict(tot)); print("disagreements (judge, where, winner>loser):"); [print("  ", d) for d in dis]
# flips: all frontier flips, same slot?
for j in FRONT:
    for k, (vd, v0, v1, s0) in allv[j].items():
        if isinstance(vd, tuple) and vd[0] == "flip":
            print("flip", j, s0["a"], s0["b"], "o0 winner", v0[1], "o1 winner", v1[1], "same-slot" if (v0[1] == s0["a"]) == (v1[1] == s0["b"]) else "OPPOSITE-slot")
