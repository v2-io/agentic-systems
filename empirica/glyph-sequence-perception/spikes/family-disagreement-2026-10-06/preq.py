"""Prequential (one-step-ahead) checks and scoring (Dawid). Every answer is predicted from the answers given in strictly
EARLIER rounds on the same item, by any mind. The planner's choices (what to re-ask, where) are functions of earlier
answers only, so these predictions remain valid under the study's adaptive design, where checks that drop or reorder
answers do not (strengthening 2). Answers in the same round are predicted from the same prefix.

Groups: 'first' (no earlier answer on the item), 'cross' (others answered earlier, this mind didn't), 'repeat' (this
mind answered earlier). For 'repeat', 'flip' = the answer differs from the mind's own last answer. Reported: log score,
and calibration as observed vs predicted counts of 1s (stops) and of flips, with 95% Poisson-binomial bands, per mind
and group, plus the flat-split repeat (this mind's earlier answers unanimous, some other mind's unanimous and opposite).

Adapter: comp_loglik(S, N, X) and cond_next(x, j, k, n) (checks2.py). Parameters: by default fitted on all items; with
folds, each item is scored with parameters fitted without its fold (irt.heldout's folds, rng seed 0)."""
import collections, numpy as np
import irt, checks

def prefixes(items, seq, minds):
    """rows: (item index, round, S_prefix, N_prefix, answers at that round [(mind j, y)])"""
    M = len(minds); rows = []
    for i, q in enumerate(items):
        by_r = collections.defaultdict(list)
        for mm, L in seq[q].items():
            for rd, y in L: by_r[rd].append((minds.index(mm), y))
        Sp = np.zeros(M); Np = np.zeros(M)
        for rd in sorted(by_r):
            rows.append((i, rd, Sp.copy(), Np.copy(), by_r[rd]))
            for j, y in by_r[rd]: Sp[j] += y; Np[j] += 1
    return rows

def score(adapters_by_fold, fold_of_item, items, seq, X, minds=irt.MINDS):
    rows = prefixes(items, seq, minds); out = []; pairs_out = []
    for f, ad in adapters_by_fold.items():
        gidx = [k for k, r in enumerate(rows) if (f is None or fold_of_item[r[0]] == f)]
        sel = [rows[k] for k in gidx]
        if hasattr(ad, "cond_next_row"): ad.cur = np.array(gidx)
        if not sel: continue
        Sx = np.array([r[2] for r in sel]); Nx = np.array([r[3] for r in sel]); Xx = np.array([X[r[0]] for r in sel])
        if hasattr(ad, "rows"): ad.rows = np.array([r[0] for r in sel])          # item-specific features (lnb)
        L = ad.comp_loglik(Sx, Nx, Xx); R = np.exp(L - np.logaddexp.reduce(L, 1)[:, None])
        if hasattr(ad, "rows"): ad.rows = None
        cache = {}
        for (i, rd, Sp, Np, ans), r, gk in zip(sel, R, gidx):
            qs = {}
            for j, y in ans:
                k, n = int(Sp[j]), int(Np[j])
                if hasattr(ad, "cond_next_row"):
                    key = (gk, j, k, n)
                    if key not in cache: cache[key] = ad.cond_next_row(gk, X[i], j, k, n)
                else:
                    key = (i, j, k, n) if hasattr(ad, "cond_next_item") else (X[i], j, k, n)
                    if key not in cache:
                        cache[key] = ad.cond_next_item(i, X[i], j, k, n) if hasattr(ad, "cond_next_item") else ad.cond_next(X[i], j, k, n)
                p = float(np.clip(r @ cache[key], 1e-6, 1 - 1e-6)); qs[j] = cache[key]
                others = [(jj, int(Sp[jj]), int(Np[jj])) for jj in range(len(minds)) if jj != j and Np[jj] > 0]
                grp = "repeat" if n > 0 else ("cross" if others else "first")
                own_unan = n > 0 and (k == 0 or k == n)
                opp = own_unan and any(nn >= 1 and ((kk == nn and k == 0) or (kk == 0 and k == n)) for _, kk, nn in others)
                last = None
                if n > 0:
                    L_ = sorted(seq[items[i]][minds[j]], key=lambda t: t[0]); last = [yy for rr, yy in L_ if rr < rd][-1]
                out.append(dict(i=i, j=j, y=y, p=p, grp=grp, n=n, k=k, last=last, opp=opp, rd=rd))
            # same-round pairs (one sheet, one prefix): P(the two answers differ), from the shared component posterior
            js = [(j, y) for j, y in ans]
            for u_ in range(len(js)):
                for v_ in range(u_ + 1, len(js)):
                    (ja, ya), (jb, yb) = js[u_], js[v_]
                    if ja == jb: continue
                    qa, qb = qs[ja], qs[jb]
                    pairs_out.append(dict(a=min(ja, jb), b=max(ja, jb), d=int(ya != yb), p=float(r @ (qa * (1 - qb) + qb * (1 - qa)))))
    score.pairs = pairs_out
    return out

def report(out, label, minds=irt.MINDS):
    bad = 0; ls = sum(np.log(o["p"] if o["y"] == 1 else 1 - o["p"]) for o in out)
    print(f"== {label}: prequential log score {ls:.1f} over {len(out)} answers ({ls/len(out):.4f} per answer)")
    def line(name, q, obs):
        nonlocal bad
        lo, hi = checks.band(q); f = "" if lo <= obs <= hi else "  <-- outside"; bad += bool(f)
        print(f"    {name:44s} n={len(q):5d}  obs {obs:5d} / pred {sum(q):7.1f} [{lo}-{hi}]{f}")
    for grp in ("first", "cross", "repeat"):
        print(f"  {grp}: count of stops")
        for j, mm in enumerate(minds):
            L = [o for o in out if o["j"] == j and o["grp"] == grp]
            if len(L) >= 100: line(mm, [o["p"] for o in L], sum(o["y"] for o in L))
    print("  repeat: flips (answer differs from the mind's own last answer)")
    for j, mm in enumerate(minds):
        L = [o for o in out if o["j"] == j and o["grp"] == "repeat"]
        if len(L) >= 100:
            line(mm, [1 - o["p"] if o["last"] == 1 else o["p"] for o in L], sum(o["y"] != o["last"] for o in L))
            Lo = [o for o in L if o["opp"]]
            if len(Lo) >= 30:
                line(mm + "  (flat: own unanimous, another mind opposite)", [1 - o["p"] if o["last"] == 1 else o["p"] for o in Lo], sum(o["y"] != o["last"] for o in Lo))
    pr = getattr(score, "pairs", [])
    if pr:
        print("  same-round pairs: disagreements (two minds, one sheet, one prefix)")
        cells = {}
        for x in pr: cells.setdefault((x["a"], x["b"]), []).append(x)
        for (a, b), L in sorted(cells.items()):
            if len(L) >= 300: line(f"{minds[a]} / {minds[b]}", [x["p"] for x in L], sum(x["d"] for x in L))
    print(f"  outside band: {bad}")
    return ls, bad
