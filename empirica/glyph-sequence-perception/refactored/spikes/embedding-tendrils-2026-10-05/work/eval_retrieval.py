#!/usr/bin/env python3
"""Task A — tendrils as retrieval. For every next/between instance (a fixed context ending at node q), rank the whole
universe by a context-free ranker (context glyphs and q excluded) and ask where the minds' proposals land.

  python3 eval_retrieval.py [--gt r011] [--rounds r012] RANKER ...      ('cp', 'name', 'name+num', 'emb:<file>',
                                                                           'mix:A|B' = A and B interleaved)
Truth sets per instance:
  first2  proposals given as the FIRST (most fitting) choice by >=2 families      <- the headline set
  any2    proposals at any rank by >=2 families
Stratum: 'cp-near' if some truth glyph is within +-1 codepoint of q, else 'cp-far'.
Output: a table to stdout and derived/retrieval-<gt>[-rounds].json.
"""
import argparse, collections, json
import numpy as np
from lib import DER
import rankers as RK

KS = (1, 3, 10, 30, 100)
ap = argparse.ArgumentParser()
ap.add_argument("--gt", default="r011")
ap.add_argument("--rounds", default=None, help="comma list: only instances first asked in these rounds")
ap.add_argument("--truth", default="first2")
ap.add_argument("--cat", default=None, help="comma list of item sub-categories to keep (e.g. tail,explore)")
ap.add_argument("--only-in", default=None, help="restrict to instances present in derived/llm/<FILE>.json (partial runs)")
ap.add_argument("rankers", nargs="+")
a = ap.parse_args()

G = json.load(open(DER / f"gt-{a.gt}.json"))
rset = set(a.rounds.split(",")) if a.rounds else None
only = set(json.load(open(DER / "llm" / f"{a.only_in}.json"))) if a.only_in else None

def truth(I, kind):
    out = []
    for g, p in I["props"].items():
        fams = set(p["fams_first"] if kind.startswith("first") else p["fams"]) - {"muse"}
        if len(fams) >= int(kind[-1]) and g not in I["ctx_all"] and g != I["node"]:
            out.append(g)
    return out

inst, outside = [], 0
for k, I in G["instances"].items():
    if rset and I["round"] not in rset:
        continue
    if only is not None and k not in only:
        continue
    if I["node"] not in RK.IDX:
        continue
    if a.cat and not (I.get("category") and I["category"][-1] in a.cat.split(",")):
        continue
    T = truth(I, a.truth)
    Tin = [g for g in T if g in RK.IDX]
    outside += len(T) - len(Tin)
    if Tin:
        near = any(abs(ord(g) - ord(I["node"])) <= 1 for g in Tin)
        inst.append((k, I, Tin, "cp-near" if near else "cp-far"))

_lists = {}
def ranks_for(spec, q, excl, key=None):
    if spec.startswith("llm:"):
        # a generated candidate list (llm_next.py): rank = position after removing context glyphs; absent = 10**6
        f = spec[4:]
        if f not in _lists:
            _lists[f] = json.load(open(DER / "llm" / f"{f}.json"))
        r = np.full(len(RK.GL), 10**6, dtype=np.int64)
        pos = 0
        for g, p in _lists[f].get(key, []):
            if g in excl or g not in RK.IDX:
                continue
            pos += 1
            r[RK.IDX[g]] = min(r[RK.IDX[g]], pos)
        return r
    if spec.startswith("mix:"):
        A, B = spec[4:].split("|")
        ra, rb = ranks_for(A, q, excl, key), ranks_for(B, q, excl, key)
        return np.minimum(2 * ra - 1, 2 * rb)     # interleaving A,B,A,B... (upper bound: duplicates not removed)
    s = RK.get(spec)(q).copy()
    for g in excl:
        if g in RK.IDX:
            s[RK.IDX[g]] = -np.inf
    order = np.argsort(-s, kind="stable")
    r = np.empty(len(s), dtype=np.int64); r[order] = np.arange(1, len(s) + 1)
    return r

res = {}
cache = {}
for spec in a.rankers:
    per = collections.defaultdict(list)
    detail = []
    for k, I, T, stratum in inst:
        excl = set(I["ctx_all"]) | {I["node"]}
        ck = (spec, I["node"], tuple(sorted(excl))) if "llm:" not in spec else (spec, k)
        if ck not in cache:
            cache[ck] = ranks_for(spec, I["node"], excl, k)
        r = cache[ck]
        rt = sorted(int(r[RK.IDX[g]]) for g in T)
        row = {"best": rt[0], **{f"hit@{kk}": float(rt[0] <= kk) for kk in KS},
               **{f"rec@{kk}": float(np.mean([x <= kk for x in rt])) for kk in KS}, "rr": 1 / rt[0]}
        for st in ("all", stratum):
            per[st].append(row)
        detail.append({"inst": k, "node": I["node"], "truth": T, "ranks": rt, "stratum": stratum})
    res[spec] = {st: {m: float(np.mean([x[m] for x in rows])) for m in rows[0] if m != "best"} | {"n": len(rows),
                 "median_best": float(np.median([x["best"] for x in rows]))} for st, rows in per.items()}
    res[spec]["detail"] = detail

print(f"gt={a.gt} rounds={a.rounds or 'all'} cat={a.cat or 'all'} truth={a.truth}: {len(inst)} instances "
      f"({sum(1 for x in inst if x[3]=='cp-near')} cp-near, {sum(1 for x in inst if x[3]=='cp-far')} cp-far); "
      f"{outside} truth glyphs outside the universe")
for st in ("all", "cp-near", "cp-far"):
    print(f"\n[{st}]  {'ranker':44s} " + " ".join(f"hit@{k:<4d}" for k in KS) + "  MRR   med.rank")
    for spec in a.rankers:
        m = res[spec].get(st)
        if m:
            print(f"        {spec:44s} " + " ".join(f"{m[f'hit@{k}']:.3f}   " for k in KS) + f"{m['rr']:.3f}  {m['median_best']:.0f}")
tag = a.gt + (f"-only-{a.only_in}" if a.only_in else "") + (f"-{a.rounds.replace(',', '+')}" if a.rounds else "") + (f"-cat{a.cat.replace(',', '+')}" if a.cat else "") + f"-{a.truth}"
out = DER / f"retrieval-{tag}.json"
old = json.load(open(out)) if out.exists() else {}
old.update(res)
json.dump(old, open(out, "w"), ensure_ascii=False)
