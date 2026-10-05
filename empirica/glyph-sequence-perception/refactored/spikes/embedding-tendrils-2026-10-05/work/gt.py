#!/usr/bin/env python3
"""Build the spike's reference sets ("ground truths", plural on purpose) from the extracted answers.

  python3 gt.py [UPTO]  -> derived/gt-UPTO.json

1. instances: one per next/between ITEM (a fixed context). For `next`, the node is the last context glyph and the
   truth is what minds wrote after it. For `between`, two instances: the left neighbour of the gap (truth = what
   minds put in the gap) and, oriented backwards, the right neighbour (same truth). Per proposal: families, minds.
   Context glyphs are recorded so a ranker can exclude them (a tendril is for NEW glyphs).
2. triads: per triad item, the middles each family gave (any rep), and how many answers were 'none'/'two'/ties.
3. orderadj: unordered adjacent pairs in order answers, with families.
"""
import collections, json, sys
from lib import DER, answers, ok

upto = sys.argv[1] if len(sys.argv) > 1 else "r011"
A = answers(upto)
ITEMS = json.load(open(DER / f"items-{upto}.json"))

inst = {}
def add(key, node, ctx, g, r, rank=None):
    I = inst.setdefault(key, {"node": node, "ctx": ctx, "kind": r["kind"], "round": r["round"], "props": {},
                              "category": (ITEMS.get(r["iid"]) or {}).get("category"),
                              "answers": 0, "none": 0, "fams_answered": set()})
    if g is None:
        return
    p = I["props"].setdefault(g, {"fams": set(), "minds": set(), "n": 0, "fams_first": set(), "n_first": 0})
    p["fams"].add(r["family"]); p["minds"].add(r["mind"]); p["n"] += 1
    if rank == 0:   # the mind's "most fitting first" proposal
        p["fams_first"].add(r["family"]); p["n_first"] += 1

for r in A:
    if r["status"] != "ok" or r["kind"] not in ("next", "between"):
        continue
    sh = r["shown"]
    a = r["answer"]
    raw = a.get("proposals") or []
    props = [(i, x) for i, x in enumerate(raw) if ok(x)]   # rank = position in the mind's own list
    if r["kind"] == "next":
        keys = [(r["iid"] + ">", sh[-1], sh)]
    else:
        i = sh.index("GAP")
        L, R = sh[:i], sh[i + 1:]
        keys = [(r["iid"] + ">", L[-1], L), (r["iid"] + "<", R[0], list(reversed(R)))]
    for key, node, ctx in keys:
        add(key, node, ctx, None, r)
        I = inst[key]; I["answers"] += 1; I["fams_answered"].add(r["family"])
        if not raw:
            I["none"] += 1
        for rank, g in props:
            add(key, node, ctx, g, r, rank)
        I.setdefault("ctx_all", sorted(set(g for g in sh if g != "GAP")))

triads = {}
for r in A:
    if r["status"] != "ok" or r["kind"] != "triad":
        continue
    T = triads.setdefault(r["iid"], {"glyphs": sorted(r["shown"]), "mid": collections.defaultdict(set),
                                    "mid_n": collections.Counter(), "other": collections.Counter(), "answers": 0,
                                    "fams_answered": set(), "round": r["round"],
                                    "category": (ITEMS.get(r["iid"]) or {}).get("category")})
    T["answers"] += 1; T["fams_answered"].add(r["family"])
    a = r["answer"]
    if a[0] == "mid":
        T["mid"][a[1]].add(r["family"]); T["mid_n"][a[1]] += 1
    else:
        T["other"][a[0]] += 1

orderadj = collections.defaultdict(lambda: {"fams": set(), "n": 0})
for r in A:
    if r["status"] != "ok" or r["kind"] != "order" or "lines" not in r["answer"]:
        continue
    for line in r["answer"]["lines"]:
        steps = [s for s in line if s != "GAP"]
        for s1, s2 in zip(steps, steps[1:]):
            if len(s1) == 1 and len(s2) == 1:
                k = "".join(sorted(s1 + s2))
                orderadj[k]["fams"].add(r["family"]); orderadj[k]["n"] += 1

def js(o):
    if isinstance(o, set):
        return sorted(o)
    if isinstance(o, dict):
        return {k: js(v) for k, v in o.items()}
    if isinstance(o, list):
        return [js(x) for x in o]
    return o

out = {"upto": upto, "instances": js(inst), "triads": js(triads), "orderadj": js(dict(orderadj))}
json.dump(out, open(DER / f"gt-{upto}.json", "w"), ensure_ascii=False)
ni = len(inst); nprops = sum(len(I["props"]) for I in inst.values())
agreed = sum(1 for I in inst.values() for p in I["props"].values() if len(set(p["fams"]) - {"muse"}) >= 2)
print(f"{ni} instances, {nprops} distinct (instance, proposal) pairs, {agreed} agreed by >=2 families; "
      f"{len(triads)} triad items; {len(orderadj)} order-adjacent pairs")
