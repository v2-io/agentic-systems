import collections, itertools, unicodedata
from vload import *
T = collections.defaultdict(lambda: collections.defaultdict(list))
for p, s in STIM.items():
    if s.get("set") == "triads": T[s["triad"]][s["oset"]].append(s)
# structural check: each orientation set is cyclic (a of each = b of another, every glyph once as a and once as b)
noncyc = 0
for t, os_ in T.items():
    for o, ps in os_.items():
        A = collections.Counter(x["a"] for x in ps); B = collections.Counter(x["b"] for x in ps)
        if len(ps) != 3 or set(A) != set(B) or max(A.values()) != 1: noncyc += 1
print("triads", len(T), "non-cyclic orientation sets:", noncyc)
def has_cycle(edges):  # edges: list of (winner, loser)
    w = collections.Counter(e[0] for e in edges)
    return len(edges) == 3 and max(w.values()) == 1
res = {}
for rid in runs("triads-"):
    j = rid.split("-", 3)[3] + ("[sheet]" if "-sheet-" in rid else "")
    ans = pair_answers(rid)
    A = {p: v for (p, rep), v in ans.items()}
    fo = cyc = sameslot_fo = 0; nfirst = ndir = 0
    stable_triads = stable_cyc = 0
    perp_uni = n_uni = 0
    for t, os_ in T.items():
        dirs = {}
        for o, ps in os_.items():
            edges = []; slots = []
            for s in ps:
                v = A.get(s["pid"])
                if v is None: continue
                if s["stratum"] == "uniform" and v[0] != "unparsed":
                    n_uni += 1; perp_uni += v[0] == "perp"
                if v[0] == "dir":
                    ndir += 1; nfirst += v[1] == s["a"]
                    edges.append((v[1], s["b"] if v[1] == s["a"] else s["a"])); slots.append(v[1] == s["a"])
                dirs[(o, frozenset((s["a"], s["b"])))] = v
            if len(edges) == 3:
                fo += 1; c = has_cycle(edges); cyc += c
                ss = len(set(slots)) == 1; sameslot_fo += ss
                assert c == ss, (rid, t, o)
        # order-debiased: each unordered pair cdir across the two osets
        pairs = {k[1] for k in dirs}
        ws = []
        for pr in pairs:
            v0, v1 = dirs.get((0, pr)), dirs.get((1, pr))
            if v0 and v1 and v0[0] == "dir" and v1[0] == "dir" and v0[1] == v1[1]:
                a, b = tuple(pr); ws.append((v0[1], b if v0[1] == a else a))
        if len(ws) == 3:
            stable_triads += 1; stable_cyc += has_cycle(ws)
    res[j] = (fo, cyc, nfirst, ndir, stable_triads, stable_cyc, perp_uni, n_uni)
    p1 = nfirst / max(ndir, 1)
    print(f"{j:20s} fully-oriented {fo:4d} cycles {cyc:4d} rate {cyc/max(fo,1):.3f}  P(first|dir) {p1:.2f}  pred p^3+(1-p)^3 {p1**3+(1-p1)**3:.2f}  | order-stable triads {stable_triads:3d} cycles {stable_cyc} | uniform ⟂ {perp_uni}/{n_uni}={perp_uni/max(n_uni,1):.2f}")
