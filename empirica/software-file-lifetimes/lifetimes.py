#!/usr/bin/env python3
"""E.3: file lifetimes in mainline git histories, against #der-change-expectation-baseline.

KR E.3 ("One of Volume 2's cheap falsifiers is run on a real codebase history").
The design is fixed by msc/inside-out-2026-10/e3-measurement/prereg.md (commit 54a0bf5e);
every rule below implements a numbered section of that file.

Usage:
  python3 lifetimes.py dump  <repo.git> <out.log> [--no-renames]   # section 4: the mainline log
  python3 lifetimes.py run   <name> <main.log> [<norename.log>] [--reps N] [--json out.json]

`dump` runs git in the repository directory. `run` reads only the dump, so a rerun from a
dump is exact. Seeds are keyed per repository and clock (section 5).
"""
import hashlib
import json
import subprocess
import sys

import numpy as np

CAL_GRID = [30, 90, 180, 365, 730, 1461, 2922, 5844]          # days
COM_GRID = [30, 100, 300, 1000, 3000, 10000, 30000]           # mainline commits
CAL_LARGE, COM_LARGE = 365, 1000                               # large-age threshold
CAL_YOUNG, COM_YOUNG = [30, 90, 180], [30, 100, 300]           # young-age grid points
MIN_AT_RISK = 50
BAND = (0.63, 1.71)                                            # median multiplier in [1/2, 2]
IMPORT_ADDS = 1000


# ---------------------------------------------------------------- extraction (section 4)

def dump(repo, out, no_renames=False):
    cmd = ["git", "log", "--first-parent", "--diff-merges=first-parent", "--name-status",
           "--reverse", "--format=C %H %ct"]
    cmd.append("--no-renames" if no_renames else "-M")
    with open(out, "w") as fh:
        subprocess.run(cmd, cwd=repo, stdout=fh, check=True)


def parse(path):
    """Yield (sha, ct, [records]) per mainline commit, oldest first."""
    sha = ct = None
    recs = []
    with open(path, encoding="utf-8", errors="surrogateescape") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith("C "):
                if sha is not None:
                    yield sha, ct, recs
                _, sha, ct = line.split(" ")
                ct = int(ct)
                recs = []
            elif line:
                recs.append(line.split("\t"))
    if sha is not None:
        yield sha, ct, recs


def build_lives(path):
    """Return lives (dict of arrays) and anomaly counts. Section 4's rules."""
    alive = {}          # path -> life index
    lives = []          # [birth_k, birth_t, end_k, end_t, dead, cluster, excluded, import, touches]
    anomalies = dict(nonmonotone_dates=0, add_on_alive=0, delete_on_dead=0, rename_from_dead=0,
                     rename_onto_alive=0)
    tmax = None
    k = -1
    head_sha = None
    for sha, ct, recs in parse(path):
        k += 1
        head_sha = sha
        if tmax is not None and ct < tmax:
            anomalies["nonmonotone_dates"] += 1
        t = ct if tmax is None or ct > tmax else tmax
        tmax = t
        first = (k == 0)
        n_adds = sum(1 for r in recs if r[0] == "A")
        imp = n_adds > IMPORT_ADDS
        removals, additions, touches = [], [], []
        for r in recs:
            st = r[0][0]
            if st == "D":
                removals.append(r[1])
            elif st == "R":
                removals.append(("R", r[1], r[2], int(r[0][1:] or 100)))
            elif st == "A":
                additions.append(r[1])
            elif st in "MT":
                touches.append(r[1])
        moved = []
        for item in removals:
            if isinstance(item, tuple):
                _, old, new, score = item
                if old in alive:
                    moved.append((alive.pop(old), new, score))
                else:
                    anomalies["rename_from_dead"] += 1
                    additions.append(new)
            else:
                if item in alive:
                    li = alive.pop(item)
                    lives[li][2], lives[li][3], lives[li][4] = k, t, True
                else:
                    anomalies["delete_on_dead"] += 1
        for li, new, score in moved:
            if new in alive:
                anomalies["rename_onto_alive"] += 1
                old_li = alive.pop(new)
                lives[old_li][2], lives[old_li][3], lives[old_li][4] = k, t, True
            alive[new] = li
            if score < 100:
                lives[li][8].append((k, t))
        for p in additions:
            if p in alive:
                anomalies["add_on_alive"] += 1
                continue
            cluster = p.rsplit("/", 1)[0] if "/" in p else ""
            lives.append([k, t, None, None, False, cluster, first, imp, [(k, t)]])
            alive[p] = len(lives) - 1
        for p in touches:
            if p in alive:
                lives[alive[p]][8].append((k, t))
    head_k, head_t = k, tmax
    for li in alive.values():
        lives[li][2], lives[li][3] = head_k, head_t
    return lives, anomalies, dict(head_sha=head_sha, head_k=head_k, head_t=head_t, n_commits=k + 1)


# ---------------------------------------------------------------- survival (section 5)

class KM:
    """Kaplan-Meier on fixed durations, re-weightable for the cluster bootstrap."""

    def __init__(self, dur, event, cluster):
        order = np.argsort(dur, kind="stable")
        self.dur = dur[order]
        self.event = event[order]
        self.cl = cluster[order]
        self.ut, self.first = np.unique(self.dur, return_index=True)
        self.ncl = int(cluster.max()) + 1 if len(cluster) else 0

    def logQ_at(self, ts, w=None):
        """log Q(t) at each t in ts (right-continuous: events at <= t count)."""
        w = np.ones(len(self.dur)) if w is None else w
        tot = np.concatenate([np.cumsum(w[::-1])[::-1], [0.0]])
        at_risk = tot[self.first]                                   # weight with dur >= ut
        ev = np.bincount(np.searchsorted(self.ut, self.dur), weights=w * self.event,
                         minlength=len(self.ut))
        with np.errstate(divide="ignore", invalid="ignore"):
            h = np.where(at_risk > 0, ev / at_risk, 0.0)
            lg = np.cumsum(np.log1p(-np.minimum(h, 1.0)))
        idx = np.searchsorted(self.ut, ts, side="right") - 1
        return np.where(idx >= 0, lg[np.maximum(idx, 0)], 0.0)

    def at_risk(self, t):
        return int(len(self.dur) - np.searchsorted(self.dur, t, side="left"))

    def weights(self, rng):
        counts = rng.multinomial(self.ncl, np.full(self.ncl, 1.0 / self.ncl))
        return counts[self.cl].astype(float)


def seed_for(name, clock):
    return int(hashlib.sha256(f"E3:{name}:{clock}".encode()).hexdigest()[:8], 16)


def analyse_clock(name, clock, dur, event, cluster, reps):
    km = KM(dur, event, cluster)
    grid = CAL_GRID if clock == "calendar" else COM_GRID
    large = CAL_LARGE if clock == "calendar" else COM_LARGE
    young = CAL_YOUNG if clock == "calendar" else COM_YOUNG
    est = [t for t in grid if km.at_risk(2 * t) >= MIN_AT_RISK]
    tail_lo = large
    tail_hi = max([t for t in np.unique(dur) if km.at_risk(t) >= MIN_AT_RISK] or [0])
    tail_ts = np.geomspace(tail_lo, tail_hi, 30) if tail_hi > 2 * tail_lo else None

    def stats(w):
        ts = np.array(est, float)
        if len(ts) == 0:
            return {}, np.nan
        lq1, lq2 = km.logQ_at(ts, w), km.logQ_at(2 * ts, w)
        a = -(lq2 - lq1) / np.log(2)
        slope = np.nan
        if tail_ts is not None:
            lq = km.logQ_at(tail_ts, w)
            slope = -np.polyfit(np.log(tail_ts), lq, 1)[0]
        return dict(zip(est, a)), slope

    a0, slope0 = stats(None)
    rng = np.random.default_rng(seed_for(name, clock))
    boot_a = {t: [] for t in est}
    boot_slope = []
    for _ in range(reps):
        w = km.weights(rng)
        a, s = stats(w)
        for t in est:
            boot_a[t].append(a[t])
        boot_slope.append(s)

    def ci(xs):
        xs = np.asarray(xs, float)
        xs = xs[np.isfinite(xs)]
        return [float(np.percentile(xs, 2.5)), float(np.percentile(xs, 97.5))] if len(xs) else [None, None]

    def mean_over(ts):
        ts = [t for t in ts if t in a0]
        if not ts:
            return None
        pt = float(np.mean([a0[t] for t in ts]))
        bs = np.mean(np.array([boot_a[t] for t in ts]), axis=0)
        return dict(ages=ts, a=pt, ci=ci(bs))

    res = dict(
        n_lives=int(len(dur)), n_deaths=int(event.sum()), n_clusters=km.ncl,
        estimable=est,
        a_t0={str(t): dict(a=float(a0[t]), ci=ci(boot_a[t]), c=float(2 ** -a0[t]),
                           at_risk_2t0=km.at_risk(2 * t)) for t in est},
        a_large=mean_over([t for t in est if t >= large]),
        a_young=mean_over(young),
        tail_slope=None if tail_ts is None else dict(range=[float(tail_lo), float(tail_hi)],
                                                     a=float(slope0), ci=ci(boot_slope)),
        seed=seed_for(name, clock), reps=reps,
    )
    return res


def classify(entry):
    """Section 6's per-repository reading of one interval."""
    if entry is None or entry["ci"][0] is None:
        return "n/a"
    lo, hi = entry["ci"]
    if lo <= 1 <= hi:
        return "contains-1"
    if hi < BAND[0]:
        return "below-band"
    if lo > BAND[1]:
        return "above-band"
    return "excludes-1-in-band"


# ---------------------------------------------------------------- counts (section 5, secondary)

def count_form(lives, meta, t_first, frac, rng_seed, reps):
    cut = t_first + frac * (meta["head_t"] - t_first)
    rows = []
    for L in lives:
        bk, bt, ek, et, dead, cl, excl, imp, touches = L
        if excl or bt > cut or (dead and et <= cut):
            continue
        n_past = sum(1 for (_, tt) in touches if tt <= cut)
        if n_past < 5:
            continue
        n_fut = sum(1 for (_, tt) in touches if tt > cut)
        rows.append((n_fut >= n_past, dead and n_fut < n_past, cl))
    if not rows:
        return dict(cut=cut, n=0)
    reach = np.array([r[0] for r in rows], float)
    died = np.array([r[1] for r in rows], float)
    cls = {c: i for i, c in enumerate(sorted({r[2] for r in rows}))}
    ci_ = np.array([cls[r[2]] for r in rows])
    rng = np.random.default_rng(rng_seed)
    bl, bu = [], []
    for _ in range(reps):
        w = rng.multinomial(len(cls), np.full(len(cls), 1.0 / len(cls)))[ci_].astype(float)
        if w.sum() == 0:
            continue
        bl.append((w * reach).sum() / w.sum())
        bu.append(1 - (w * died).sum() / w.sum())
    return dict(cut=cut, n=len(rows), L=float(reach.mean()), U=float(1 - died.mean()),
                L_ci=[float(np.percentile(bl, 2.5)), float(np.percentile(bl, 97.5))],
                U_ci=[float(np.percentile(bu, 2.5)), float(np.percentile(bu, 97.5))])


# ---------------------------------------------------------------- driver

def lives_arrays(lives, drop_imports=False):
    keep = [L for L in lives if not L[6] and not (drop_imports and L[7])]
    cl_names = {}
    cl = np.array([cl_names.setdefault(L[5], len(cl_names)) for L in keep], int)
    cal = np.array([(L[3] - L[1]) / 86400.0 for L in keep], float)
    com = np.array([L[2] - L[0] for L in keep], float)
    ev = np.array([L[4] for L in keep], float)
    return cal, com, ev, cl


def run(name, main_log, norename_log=None, reps=1000):
    lives, anomalies, meta = build_lives(main_log)
    t_first = min(L[1] for L in lives) if lives else 0
    out = dict(name=name, meta=meta, anomalies=anomalies,
               n_excluded_first_commit=sum(1 for L in lives if L[6]),
               n_import_lives=sum(1 for L in lives if L[7] and not L[6]))
    variants = {"primary": lives_arrays(lives), "no-imports": lives_arrays(lives, drop_imports=True)}
    if norename_log:
        nl, nanom, nmeta = build_lives(norename_log)
        variants["no-renames"] = lives_arrays(nl)
        out["no_renames_meta"] = dict(meta=nmeta, anomalies=nanom)
    for vname, (cal, com, ev, cl) in variants.items():
        r = int(reps if vname == "primary" else max(200, reps // 5))
        out[vname] = {
            "calendar": analyse_clock(name + ("" if vname == "primary" else ":" + vname),
                                      "calendar", cal, ev, cl, r),
            "commit": analyse_clock(name + ("" if vname == "primary" else ":" + vname),
                                    "commit", com, ev, cl, r),
        }
        for clock in ("calendar", "commit"):
            res = out[vname][clock]
            res["reading_large"] = classify(res["a_large"])
            res["reading_young"] = classify(res["a_young"])
    out["counts"] = {f"{frac:.3f}": count_form(lives, meta, t_first, frac,
                                               seed_for(name, f"counts:{frac:.3f}"), reps)
                     for frac in (1 / 3, 1 / 2)}
    return out


def show(o):
    m = o["meta"]
    print(f"== {o['name']}  head {m['head_sha'][:10]}  mainline commits {m['n_commits']}  "
          f"anomalies {o['anomalies']}  excluded(first commit) {o['n_excluded_first_commit']}  "
          f"import-born {o['n_import_lives']}")
    for v in ("primary", "no-imports", "no-renames"):
        if v not in o:
            continue
        for clock in ("calendar", "commit"):
            r = o[v][clock]
            line = " ".join(f"{t}:{d['a']:.2f}[{d['ci'][0]:.2f},{d['ci'][1]:.2f}]"
                            for t, d in r["a_t0"].items())
            al, ay, ts = r["a_large"], r["a_young"], r["tail_slope"]
            fmt = lambda e: "n/a" if e is None else f"{e['a']:.2f}[{e['ci'][0]:.2f},{e['ci'][1]:.2f}]"
            print(f"  {v:10s} {clock:8s} lives {r['n_lives']} deaths {r['n_deaths']} "
                  f"clusters {r['n_clusters']}")
            print(f"     a(t0): {line}")
            print(f"     a_large {fmt(al)} -> {r['reading_large']}   a_young {fmt(ay)} -> "
                  f"{r['reading_young']}   tail slope {fmt(ts)}")
    for k, c in o["counts"].items():
        if c["n"]:
            print(f"  counts cut@{k}: n {c['n']} L {c['L']:.3f}{c['L_ci']} U {c['U']:.3f}{c['U_ci']}")
        else:
            print(f"  counts cut@{k}: n 0")


def explore_counts(main_log, fracs=(1 / 3, 1 / 2), n_min=5, s_grid=(0.25, 0.5, 1, 2, 4, 8, 16)):
    """EXPLORATORY (not pre-registered; see the account): when do files reach n_past more changes?

    At each cut, for live files with n_past >= n_min, time from the cut to the n_past-th further
    change is the event; deletion before it is a competing event; HEAD censors. Time is in units
    of the file's age at the cut, s = u / t0. The Aalen-Johansen cumulative incidence F(s) of
    reaching is reported. Baseline plus uniform rate: F(1) = 1/2 and flat after. Baseline alone:
    F(infinity) = 1/2.
    """
    lives, _, meta = build_lives(main_log)
    t_first = min(L[1] for L in lives)
    out = {}
    for frac in fracs:
        cut = t_first + frac * (meta["head_t"] - t_first)
        s_obs, cause = [], []
        for L in lives:
            bk, bt, ek, et, dead, cl, excl, imp, touches = L
            if excl or bt > cut or (dead and et <= cut):
                continue
            past = [tt for (_, tt) in touches if tt <= cut]
            if len(past) < n_min:
                continue
            t0 = max(cut - bt, 86400.0)
            fut = sorted(tt for (_, tt) in touches if tt > cut)
            if len(fut) >= len(past):
                s_obs.append((fut[len(past) - 1] - cut) / t0); cause.append(1)
            elif dead:
                s_obs.append((et - cut) / t0); cause.append(2)
            else:
                s_obs.append((meta["head_t"] - cut) / t0); cause.append(0)
        s_obs, cause = np.array(s_obs), np.array(cause)
        order = np.argsort(s_obs, kind="stable")
        s_obs, cause = s_obs[order], cause[order]
        n = len(s_obs)
        S, F, i, curve = 1.0, 0.0, 0, []
        while i < n:
            j = i
            while j < n and s_obs[j] == s_obs[i]:
                j += 1
            at_risk = n - i
            d1 = int((cause[i:j] == 1).sum()); d2 = int((cause[i:j] == 2).sum())
            F += S * d1 / at_risk
            S *= 1 - (d1 + d2) / at_risk
            curve.append((s_obs[i], F, n - j))
            i = j
        res = {}
        for s in s_grid:
            k = np.searchsorted([c[0] for c in curve], s, side="right") - 1
            remaining = n - int(np.searchsorted(s_obs, s, side="left"))
            res[str(s)] = dict(F=float(curve[k][1]) if k >= 0 else 0.0, at_risk=remaining)
        out[f"{frac:.3f}"] = dict(n=n, reached=int((cause == 1).sum()),
                                  deleted_first=int((cause == 2).sum()),
                                  censored=int((cause == 0).sum()), F=res)
    return out


def summarize(paths, variant="primary"):
    """Section 6's decision rules over the primary set's JSON outputs."""
    rows = [json.load(open(p)) for p in paths]
    print(f"--- decision rules, variant {variant}, {len(rows)} repositories")
    for clock in ("calendar", "commit"):
        for which in ("large", "young"):
            readings = [r[variant][clock][f"reading_{which}"] for r in rows]
            vals = [r[variant][clock][f"a_{which}"] for r in rows]
            n_est = sum(1 for x in readings if x != "n/a")
            c1 = readings.count("contains-1")
            below = readings.count("below-band")
            above = readings.count("above-band")
            if c1 >= 7:
                out = "CONSISTENT"
            elif below >= 7 or above >= 7:
                out = "AGAINST (" + ("files outlive the baseline" if below >= 7 else
                                     "files die sooner than the baseline") + ")"
            else:
                out = "NARROWED"
            pts = [v["a"] for v in vals if v]
            rng_ = f"{min(pts):.2f}-{max(pts):.2f}" if pts else "n/a"
            print(f"  {clock:8s} {which:5s}: estimable {n_est}, contains-1 {c1}, below-band {below}, "
                  f"above-band {above}, excl-1-in-band {readings.count('excludes-1-in-band')}"
                  f"  range of a {rng_}  -> {out}")
        # the no-Lindy rule: a(t0) at the largest estimable age >= 3x a(365 d / 1000 commits)
        ref = "365" if clock == "calendar" else "1000"
        hits = 0
        for r in rows:
            at = r[variant][clock]["a_t0"]
            if ref in at and len(at) > 0:
                last = at[max(at, key=lambda k: float(k))]
                ages = sorted(at, key=float)
                rising = all(at[ages[i]]["a"] <= at[ages[i + 1]]["a"] + 1e-9
                             for i in range(ages.index(ref), len(ages) - 1))
                if at[ref]["a"] > 0 and last["a"] >= 3 * at[ref]["a"] and rising:
                    hits += 1
        print(f"  {clock:8s} no-Lindy rule met in {hits} of {len(rows)}")
    print("--- counts (secondary): U<1/2 / L>1/2 by repository")
    for k in ("0.333", "0.500"):
        cs = [r["counts"][k] for r in rows]
        u = sum(1 for c in cs if c["n"] and c["U"] < 0.5)
        l_ = sum(1 for c in cs if c["n"] and c["L"] > 0.5)
        print(f"  cut@{k}: U<1/2 in {u}, L>1/2 in {l_}; "
              + "; ".join(f"{r['name']} [{c['L']:.2f},{c['U']:.2f}] n={c['n']}" for r, c in zip(rows, cs) if c["n"]))


def main(argv):
    if argv[1] == "explore":
        for path in argv[2:]:
            name = path.rsplit("/", 1)[-1].replace(".log", "")
            o = explore_counts(path)
            for k, v in o.items():
                fs = " ".join(f"s{s}:{d['F']:.2f}(n{d['at_risk']})" for s, d in v["F"].items())
                print(f"{name:16s} cut@{k} n {v['n']} reached {v['reached']} deleted-first "
                      f"{v['deleted_first']} censored {v['censored']} | {fs}")
        return
    if argv[1] == "summarize":
        variant = "primary"
        args = argv[2:]
        if "--variant" in args:
            i = args.index("--variant"); variant = args[i + 1]; del args[i:i + 2]
        summarize(args, variant)
        return
    if argv[1] == "dump":
        dump(argv[2], argv[3], no_renames="--no-renames" in argv)
        return
    if argv[1] == "run":
        args = [a for a in argv[2:]]
        reps, js = 1000, None
        if "--reps" in args:
            i = args.index("--reps"); reps = int(args[i + 1]); del args[i:i + 2]
        if "--json" in args:
            i = args.index("--json"); js = args[i + 1]; del args[i:i + 2]
        name, main_log = args[0], args[1]
        nr = args[2] if len(args) > 2 else None
        o = run(name, main_log, nr, reps)
        show(o)
        if js:
            with open(js, "w") as fh:
                json.dump(o, fh, indent=1, default=float)
        return
    raise SystemExit(__doc__)


if __name__ == "__main__":
    main(sys.argv)
