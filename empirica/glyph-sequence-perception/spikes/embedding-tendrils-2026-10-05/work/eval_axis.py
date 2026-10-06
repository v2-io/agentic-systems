#!/usr/bin/env python3
"""Joseph's follow-up (2026-10-05, mid-spike): "Whatever axis or line in the embedding space you can find that has
multiple codepoints, those codepoints ordering on that axis would be the sequence order -- which is the real find."

Two checks on sets the minds themselves ordered:
  ORDER  - for each set, project its members' embeddings on the set's own first principal component and compare
           that ordering to the minds' ordering (|Spearman rho|; sign is free, a sequence reads either way).
           Comparators: codepoint order, and a shuffled-embedding control (same set, embedding rows of random
           universe glyphs) to show what PC1-ordering gives by chance for a set of that size.
  LINE   - how line-like is the set in the space? share of variance on PC1 (PC1 / total), vs the same statistic
           for random sets of the same size drawn from the same Unicode blocks (so 'same block' is not mistaken
           for 'is a line').
Reference sets (both ordered by minds, not by us):
  survey  - survey sequence records (data/surveys-v1, read-only via gt_survey's parse), length >= 4
  order   - study order answers (r011): a scrambled set the minds put in sequence; kept when >= 2 families wrote
            the same single line (up to reversal), length >= 4.

  python3 eval_axis.py EMBFILE ...
"""
import collections, json, sys
import numpy as np
from lib import DER, block, answers
import rankers as RK

rng = np.random.default_rng(7)

def sets_survey():
    G = json.load(open(DER / "gt-survey.json"))
    seqs = {}
    for k, I in G["instances"].items():
        rid, d = k[:16], k[16]
        if d != ">":
            continue
        seq = I["ctx"] + list(I["props"])
        if len(seq) > len(seqs.get(rid, [])):
            seqs[rid] = seq
    return [s for s in seqs.values() if len(s) >= 4 and all(g in RK.IDX for g in s)]

def sets_order():
    by = collections.defaultdict(lambda: collections.defaultdict(set))
    for r in answers("r011"):
        if r["kind"] != "order" or r["status"] != "ok" or "lines" not in r["answer"]:
            continue
        L = r["answer"]["lines"]
        if len(L) != 1:
            continue
        steps = [s for s in L[0] if s != "GAP"]
        if any(len(s) != 1 for s in steps):
            continue
        seq = tuple(s[0] for s in steps)
        key = min(seq, tuple(reversed(seq)))
        by[r["iid"]][key].add(r["family"])
    out = []
    for iid, d in by.items():
        for seq, fams in d.items():
            if len(set(fams) - {"muse"}) >= 2 and len(seq) >= 4 and all(g in RK.IDX for g in seq):
                out.append(list(seq))
    return out

def spearman_abs(order_true, values):
    """|rho| between the true order and an ordering by `values`. Ties are broken at random: a stable sort would keep
    tied members in their listed (= true) order and credit a collapsed embedding with the minds' answer (seen in a
    first draft: bge-m3 glyph vectors, mostly [UNK], scored 0.76)."""
    n = len(order_true)
    v = np.asarray(values, dtype=np.float64)
    v = v + rng.random(n) * 1e-9 * (np.abs(v).max() + 1e-12)
    rt = np.arange(n); rv = np.argsort(np.argsort(v))
    return abs(float(np.corrcoef(rt, rv)[0, 1])) if n > 2 else float("nan")

def pc1(C):
    Cc = C - C.mean(0)
    U, S, Vt = np.linalg.svd(Cc, full_matrices=False)
    var = S ** 2
    return Cc @ Vt[0], float(var[0] / var.sum()) if var.sum() > 0 else float("nan")

BY_BLOCK = collections.defaultdict(list)
for i, g in enumerate(RK.GL):
    BY_BLOCK[block(g)].append(i)

def report(name, sets, X):
    rho_e, rho_cp, rho_ctl, lin, lin_ctl = [], [], [], [], []
    for s in sets:
        C = np.stack([X[RK.IDX[g]] for g in s])
        proj, share = pc1(C)
        rho_e.append(spearman_abs(s, proj)); lin.append(share)
        rho_cp.append(spearman_abs(s, [ord(g) for g in s]))
        rho_ctl.append(spearman_abs(s, rng.permutation(len(s))))          # a random ordering
        # same-block random set of the same size (falls back to universe if the block is too small)
        pool = [i for g in s for i in BY_BLOCK[block(g)]]
        pool = list(set(pool) - {RK.IDX[g] for g in s})
        idx = rng.choice(pool, len(s), replace=False) if len(pool) >= len(s) else rng.integers(0, len(RK.GL), len(s))
        lin_ctl.append(pc1(X[idx])[1])
    f = lambda v: f"{np.nanmean(v):.3f}"
    print(f"  {name:40s} n={len(sets):4d}  |rho| PC1 {f(rho_e)}  codepoint {f(rho_cp)}  chance {f(rho_ctl)}   "
          f"PC1 share {f(lin)} vs same-block random {f(lin_ctl)}   PC1 beats codepoint on {np.mean(np.array(rho_e) > np.array(rho_cp) + 1e-9):.2f} of sets")
    return {"n": len(sets), "rho_pc1": float(np.nanmean(rho_e)), "rho_cp": float(np.nanmean(rho_cp)),
            "rho_chance": float(np.nanmean(rho_ctl)), "pc1_share": float(np.nanmean(lin)),
            "pc1_share_sameblock_random": float(np.nanmean(lin_ctl)),
            "pc1_beats_cp_share": float(np.mean(np.array(rho_e) > np.array(rho_cp) + 1e-9)),
            "rho_pc1_when_cp_wrong": float(np.nanmean([e for e, c in zip(rho_e, rho_cp) if c < 0.9])) if any(c < 0.9 for c in rho_cp) else None,
            "n_cp_wrong": int(sum(c < 0.9 for c in rho_cp))}

S = {"survey": sets_survey(), "order": sets_order()}
out = {}
for emb in sys.argv[1:]:
    X = np.load(DER / "emb" / f"{emb}.npy").astype(np.float32)
    X /= (np.linalg.norm(X, axis=1, keepdims=True) + 1e-9)
    print(emb)
    for k, sets in S.items():
        out[f"{emb}|{k}"] = report(k, sets, X)
        r = out[f"{emb}|{k}"]
        print(f"      sets where codepoint order is wrong (|rho|<0.9): {r['n_cp_wrong']}, PC1 |rho| on those {r['rho_pc1_when_cp_wrong']}")
p = DER / "axis.json"
old = json.load(open(p)) if p.exists() else {}
old.update(out); json.dump(old, open(p, "w"), indent=1)
