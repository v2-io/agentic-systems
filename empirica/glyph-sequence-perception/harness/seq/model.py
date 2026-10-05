"""The evidence model and its annealed fit (PLAN.md §2).

Observations. Every parsed triad answer is one triple observation. Every parsed order answer on k glyphs
becomes C(k,3) triple observations with composite-likelihood weight w(k) = log(k!/2) / (C(k,3) log 3), so an
order answer counts for about as much information as the order it states, not C(k,3) independent triads.
A triple observation carries: mind, triple, the order those three were shown in (for slot bias), the outcome,
ctx (glyphs shown in the item: 3 for a triad, k for an order), forced (no ⟂ offered), tie_ok (ties offered).

State. Sigma = a list of candidate sequences; each a list of steps, each step a list of glyphs (a tie when
longer than one). Candidates may share glyphs; orientation is irrelevant. Per mind m and candidate c: s3(m,c)
(perception in triads) and s4(m,c) (in sets of 4+); per mind: eps (noise rate), nn / nt (noise share of
none / two), beta (noise preference for the shown middle), tau (tie use when a tie is perceived and offered).

Answer probability of a triple observation for mind m (no ⟂ offered = forced; see _predict):
    P = (1-eps) * Perc + eps * Noise
    Perc = p3 * Mix_{c in C3}[pred_c] + (1-p3) * (p2 * Mix_{c in C2}[two(pair_c)] + (1-p2) * none)
where C3 / C2 are candidates holding all three / exactly two of the triple, p3 = max s over C3 (a mind perceives
a triple through a sequence; restating the same structure in overlapping candidates must not compound), and the
mixtures weight candidates by s.

Fit. Maximise  sum_obs w * log P  -  LAMBDA_C * |Sigma|  -  LAMBDA_G * sum |c|  by simulated annealing over
Sigma, refitting s for the candidates a move touches (grid profile likelihood) and the nuisance parameters
between sweeps. Restarts with a tabu on minima found give alternative explanations; sampling at T = 1 after
cooling gives posterior samples, whose disagreement drives the next round's queue (bald()).
"""
import math, itertools, collections
from common import R

OUTS = None  # outcomes are tuples: ("mid", g) ("tie2", end, a, b) ("tie3",) ("two", a, b) ("none",)
GRID = (0.0, 0.03, 0.1, 0.2, 0.35, 0.5, 0.65, 0.8, 0.9, 0.97)
LAMBDA_C, LAMBDA_G, LAMBDA_W = 1.0, 2.0, 12.0
GRID_COARSE = (0.0, 0.1, 0.35, 0.65, 0.9)
WITNESS_MIN = 2
EPS_PRIOR = 20.0   # log-prior weight: Beta(1, 21)-like on the noise rate
MIN_LEN = 3
P_TIE_NOISE = 0.02

def w_order(k):
    return math.log(math.factorial(k) / 2) / (math.comb(k, 3) * math.log(3))

# ------------------------------------------------------------------ observations
def observations(parsed_rows, pres_by_pid):
    """parsed_rows: [{mind, pid, status, answer}] -> triple observations (list of dicts)."""
    obs = []
    for r in parsed_rows:
        if r["status"] != "ok":
            continue
        p = pres_by_pid[r["pid"]]
        f = p.get("factors", {"perp": True, "tie": False})
        shown = [g for g in p["shown"] if g != "GAP"]
        base = {"mind": r["mind"], "forced": not f.get("perp", True), "tie_ok": bool(f.get("tie")), "pid": r["pid"]}
        if p["kind"] == "triad":
            obs.append({**base, "tri": tuple(sorted(shown)), "shown": tuple(shown), "out": tuple(r["answer"]),
                        "ctx": 3, "w": 1.0})
        elif p["kind"] == "order":
            a, k = r["answer"], len(shown)
            w = w_order(k)
            line_of, step_of = {}, {}
            for li, line in enumerate(a.get("lines") or []):
                si = 0
                for st in line:
                    if st == "GAP":
                        continue
                    for g in st:
                        line_of[g] = li; step_of[g] = si
                    si += 1
            for t in itertools.combinations(shown, 3):   # t is in shown (display) order
                ls = [line_of.get(g) for g in t]
                if a.get("none") or all(x is None for x in ls):
                    out = ("none",)
                else:
                    cnt = collections.Counter(x for x in ls if x is not None)
                    li, n = cnt.most_common(1)[0]
                    if n == 3:
                        st = [step_of[g] for g in t]
                        out = _order_outcome(t, st)
                    elif n == 2:
                        x, y = sorted(g for g in t if line_of.get(g) == li)
                        out = ("two", x, y)
                    else:
                        out = ("none",)
                obs.append({**base, "tri": tuple(sorted(t)), "shown": tuple(t), "out": out, "ctx": k, "w": w})
    return obs

def _order_outcome(t, st):
    d = sorted(set(st))
    if len(d) == 3:
        return ("mid", sorted(zip(st, t))[1][1])
    if len(d) == 1:
        return ("tie3",)
    lone = next(g for g, s in zip(t, st) if st.count(s) == 1)
    a, b = sorted(g for g, s in zip(t, st) if st.count(s) == 2)
    return ("tie2", lone, a, b)

# ------------------------------------------------------------------ prediction
def _pred_cand(steps_pos, tri, tie_ok, tau):
    """Distribution over outcomes for a perceived candidate that holds all of `tri`."""
    pa = [steps_pos[g] for g in tri]
    d = sorted(set(pa))
    if len(d) == 3:
        return {("mid", sorted(zip(pa, tri))[1][1]): 1.0}
    if len(d) == 1:
        out = {("mid", g): (1 - tau if tie_ok else 1.0) / 3 for g in tri}
        if tie_ok:
            out[("tie3",)] = tau
        return out
    lone = next(g for g, s in zip(tri, pa) if pa.count(s) == 1)
    pair = sorted(g for g, s in zip(tri, pa) if pa.count(s) == 2)
    out = {("mid", pair[0]): (1 - tau if tie_ok else 1.0) / 2, ("mid", pair[1]): (1 - tau if tie_ok else 1.0) / 2}
    if tie_ok:
        out[("tie2", lone, pair[0], pair[1])] = tau
    return out

def _strict(steps_pos, tri):
    """The single outcome a candidate asserts for `tri`: its middle, or its tie."""
    pa = [steps_pos[g] for g in tri]
    d = sorted(set(pa))
    if len(d) == 3:
        return ("mid", sorted(zip(pa, tri))[1][1])
    if len(d) == 1:
        return ("tie3",)
    lone = next(g for g, x in zip(tri, pa) if pa.count(x) == 1)
    a, b = sorted(g for g, x in zip(tri, pa) if pa.count(x) == 2)
    return ("tie2", lone, a, b)

def _noise(o, th):
    tri, shown = o["tri"], o["shown"]
    out = {}
    if o["forced"]:
        nn, nt = 0.0, 0.0
    else:
        nn, nt = th["nn"], th["nt"]
    ns = max(0.0, 1 - nn - nt)
    if nn:
        out[("none",)] = nn
    if nt:
        for x, y in itertools.combinations(tri, 2):
            out[("two", x, y)] = nt / 3
    mid_shown = shown[1]
    for g in tri:
        out[("mid", g)] = out.get(("mid", g), 0) + ns * (1 - P_TIE_NOISE) * (th["beta"] if g == mid_shown else (1 - th["beta"]) / 2)
    if o["tie_ok"]:
        out[("tie3",)] = ns * P_TIE_NOISE / 4
        for g in tri:
            a, b = sorted(x for x in tri if x != g)
            out[("tie2", g, a, b)] = ns * P_TIE_NOISE / 4
    else:
        for g in tri:
            out[("mid", g)] += ns * P_TIE_NOISE / 3
    return out

def predict(o, model, mind):
    """Outcome distribution for observation `o` under the model, for `mind`."""
    th = model.theta[mind]
    tri = o["tri"]
    c3, c2 = [], []
    for ci in model.touching(tri):
        c = model.cands[ci]
        n = sum(1 for g in tri if g in c.pos)
        s = model.s(mind, ci, o["ctx"])
        if s <= 0:
            continue
        if n == 3:
            c3.append((s, ci))
        elif n == 2:
            c2.append((s, ci))
    perc = collections.defaultdict(float)
    p3 = max(s for s, _ in c3) if c3 else 0.0
    if c3:
        z = sum(s for s, _ in c3)
        for s, ci in c3:
            for k, v in _pred_cand(model.cands[ci].pos, tri, o["tie_ok"], th["tau"]).items():
                perc[k] += p3 * (s / z) * v
    p2 = max(s for s, _ in c2) if c2 else 0.0
    rest = 1 - p3
    if c2:
        z = sum(s for s, _ in c2)
        for s, ci in c2:
            x, y = sorted(g for g in tri if g in model.cands[ci].pos)
            if o["forced"]:
                perc[("mid", x)] += rest * p2 * (s / z) / 2
                perc[("mid", y)] += rest * p2 * (s / z) / 2
            else:
                perc[("two", x, y)] += rest * p2 * (s / z)
    left = rest * (1 - p2)
    if o["forced"]:
        for k, v in _noise(o, th).items():   # nothing perceived and no ⟂ offered: guess like noise
            perc[k] += left * v
    else:
        perc[("none",)] += left
    nz = _noise(o, th)
    e = th["eps"]
    keys = set(perc) | set(nz)
    return {k: (1 - e) * perc.get(k, 0.0) + e * nz.get(k, 0.0) for k in keys}

def _noise_out(o, model, mind):
    v = model.theta_ver.get(mind, 0)
    c = o.get("_nz")
    if c is None or c[0] != v or c[1] is not model:
        c = (v, model, _noise(o, model.theta[mind]).get(o["out"], 0.0))
        o["_nz"] = c
    return c[2]

def prob_out(o, model):
    """P(observed outcome) under the model: the same quantity as predict(o)[o["out"]], computed directly."""
    mind = o["mind"]; th = model.theta[mind]; tri = o["tri"]; out = o["out"]; forced = o["forced"]
    c3, c2 = [], []
    for ci in model.touching(tri):
        c = model.cands[ci]
        n = (tri[0] in c.pos) + (tri[1] in c.pos) + (tri[2] in c.pos)
        sv = model.s(mind, ci, o["ctx"])
        if sv <= 0:
            continue
        (c3 if n == 3 else c2).append((sv, ci))
    perc = 0.0
    p3 = 0.0
    if c3:
        p3 = max(sv for sv, _ in c3)   # perceived through a sequence: restating structure does not compound
        z = sum(sv for sv, _ in c3)
        if out[0] != "none" and out[0] != "two":
            for sv, ci in c3:
                perc += p3 * (sv / z) * _pred_cand(model.cands[ci].pos, tri, o["tie_ok"], th["tau"]).get(out, 0.0)
    rest = 1 - p3
    p2 = 0.0
    if c2:
        p2 = max(sv for sv, _ in c2)
        z = sum(sv for sv, _ in c2)
        for sv, ci in c2:
            cp = model.cands[ci].pos
            pr = tuple(sorted(g for g in tri if g in cp))
            if forced:
                if out[0] == "mid" and out[1] in pr:
                    perc += rest * p2 * (sv / z) / 2
            elif out[0] == "two" and (out[1], out[2]) == pr:
                perc += rest * p2 * (sv / z)
    left = rest * (1 - p2)
    nz = _noise_out(o, model, mind)
    if forced:
        perc += left * nz
    elif out[0] == "none":
        perc += left
    e = th["eps"]
    return (1 - e) * perc + e * nz

def loglik(o, model):
    return o["w"] * math.log(max(prob_out(o, model), 1e-9))

# ------------------------------------------------------------------ model state
class Cand:
    __slots__ = ("steps", "pos")
    def __init__(self, steps):
        self.steps = [list(s) for s in steps if s]
        self.pos = {g: i for i, s in enumerate(self.steps) for g in s}
    def glyphs(self):
        return [g for s in self.steps for g in s]
    def key(self):
        a = tuple(tuple(sorted(s)) for s in self.steps)
        return min(a, a[::-1])
    def __len__(self):
        return len(self.pos)

DEFAULT_THETA = {"eps": 0.15, "nn": 0.6, "nt": 0.1, "beta": 0.34, "tau": 0.5}

class Model:
    def __init__(self, obs, minds, cands=None, theta=None, svals=None):
        self.obs = obs
        self.minds = sorted(minds)
        self.cands = {}          # id -> Cand
        self.S = {}              # (mind, cid, 3|4) -> s
        self.theta = {m: dict((theta or {}).get(m, DEFAULT_THETA)) for m in self.minds}
        self.g2obs = collections.defaultdict(set)
        for i, o in enumerate(obs):
            for g in o["tri"]:
                self.g2obs[g].add(i)
        self.g2c = collections.defaultdict(set)
        self._pen = {}
        self.theta_ver = {m: 0 for m in self.minds}
        self.next_id = 0
        for c in cands or []:
            cid = self.add(Cand(c))
            for m in self.minds:
                for k in (3, 4):
                    self.S[(m, cid, k)] = (svals or {}).get((m, tuple(map(tuple, c)), k), 0.5)
        self.ll = [0.0] * len(obs)
        self.total = 0.0

    # candidates ------------------------------------------------------
    def add(self, cand):
        cid = self.next_id; self.next_id += 1
        self.cands[cid] = cand
        for g in cand.pos:
            self.g2c[g].add(cid)
        return cid

    def remove(self, cid):
        self._pen.pop(cid, None)
        c = self.cands.pop(cid)
        for g in c.pos:
            self.g2c[g].discard(cid)
        for m in self.minds:
            for k in (3, 4):
                self.S.pop((m, cid, k), None)
        return c

    def touching(self, tri):
        cnt = collections.Counter(ci for g in tri for ci in self.g2c.get(g, ()))
        return [ci for ci, n in cnt.items() if n >= 2]

    def s(self, mind, cid, ctx):
        return self.S.get((mind, cid, 3 if ctx <= 3 else 4), 0.0)

    def obs_for(self, cand):
        """indices of observations with >= 2 glyphs in `cand`."""
        cnt = collections.Counter(i for g in cand.pos for i in self.g2obs.get(g, ()))
        return [i for i, n in cnt.items() if n >= 2]

    def witness_parts(self, cand):
        """Number of separately-witnessed pieces of `cand`: triples answered in the candidate's order at least
        twice, and by at least half of the answers they received (any minds, any presentations), are linked when they share two glyphs; glyphs in no such triple count as pieces of
        their own. A sequence claim is built from overlapping perceived triples, so pieces beyond one are
        claims nothing witnessed (interleavings, splices through a single bridge glyph)."""
        parent = {}
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x
        covered = set()
        tally = collections.defaultdict(lambda: [0, 0])     # triple -> [answers in the candidate's order, all answers]
        for i in self.obs_for(cand):
            o = self.obs[i]
            if len(set(o["tri"]) & set(cand.pos)) < 3:
                continue
            t = tally[o["tri"]]
            t[1] += 1
            if o["out"] == _strict(cand.pos, o["tri"]):   # strict: a tie is witnessed only by a tie answer
                t[0] += 1
        for tri, (ok, n) in tally.items():
            if ok < WITNESS_MIN or ok < 0.5 * n:   # witnessed: >= 2 answers in this order, and at least half of all answers
                continue
            a, b, c = tri
            prs = [(a, b), (a, c), (b, c)]
            for q in prs:
                parent.setdefault(q, q)
            r0 = find(prs[0])
            for q in prs[1:]:
                parent[find(q)] = r0
            covered.update(tri)
        roots = {find(q) for q in parent}
        return len(roots) + len(set(cand.pos) - covered)

    def cand_pen(self, cid):
        v = self._pen.get(cid)
        if v is None:
            c = self.cands[cid]
            v = LAMBDA_C + LAMBDA_G * len(c) + LAMBDA_W * max(0, self.witness_parts(c) - 1)
            self._pen[cid] = v
        return v

    def penalty(self):
        return sum(self.cand_pen(ci) for ci in self.cands)

    def objective(self):
        return self.total - self.penalty()

    # likelihood bookkeeping ------------------------------------------
    def recompute_all(self):
        self.ll = [loglik(o, self) for o in self.obs]
        self.total = sum(self.ll)

    def recompute(self, idx):
        d = 0.0
        for i in idx:
            v = loglik(self.obs[i], self); d += v - self.ll[i]; self.ll[i] = v
        self.total += d
        return d

    # parameter fitting -----------------------------------------------
    def fit_s(self, cid, idx=None, grid=GRID):
        """Grid profile-likelihood fit of s3, s4 for candidate `cid`, per mind, over its observations."""
        idx = self.obs_for(self.cands[cid]) if idx is None else idx
        by = collections.defaultdict(list)
        for i in idx:
            o = self.obs[i]; by[(o["mind"], 3 if o["ctx"] <= 3 else 4)].append(i)
        for m in self.minds:
            for k in (3, 4):
                ii = by.get((m, k))
                if not ii:
                    self.S[(m, cid, k)] = self.S.get((m, cid, 3 if k == 4 else 4), 0.0) if (m, cid, 3 if k == 4 else 4) in self.S else 0.0
                    continue
                best, bv = None, -1e18
                for v in grid:
                    self.S[(m, cid, k)] = v
                    t = sum(loglik(self.obs[i], self) for i in ii)
                    if t > bv:
                        bv, best = t, v
                self.S[(m, cid, k)] = best

    def fit_theta(self, rounds=2):
        grids = {"eps": (0.02, 0.05, 0.1, 0.15, 0.25, 0.4, 0.6, 0.8), "nn": (0.05, 0.2, 0.4, 0.6, 0.8, 0.95),
                 "nt": (0.0, 0.05, 0.1, 0.2, 0.3), "beta": (0.2, 0.34, 0.5, 0.65, 0.8, 0.95),
                 "tau": (0.1, 0.3, 0.5, 0.7, 0.9)}
        by = collections.defaultdict(list)
        for i, o in enumerate(self.obs):
            by[o["mind"]].append(i)
        for _ in range(rounds):
            for m in self.minds:
                ii = by.get(m, [])
                if not ii:
                    continue
                for name, g in grids.items():
                    best, bv = self.theta[m][name], -1e18
                    for v in g:
                        if name in ("nn", "nt") and (self.theta[m]["nt" if name == "nn" else "nn"] + v) > 1:
                            continue
                        self.theta[m][name] = v; self.theta_ver[m] += 1
                        t = sum(loglik(self.obs[i], self) for i in ii)
                        if name == "eps":
                            t += EPS_PRIOR * math.log(1 - v)   # mild prior against a mind being mostly noise
                        if t > bv:
                            bv, best = t, v
                    self.theta[m][name] = best; self.theta_ver[m] += 1
        self.recompute_all()

    # export ----------------------------------------------------------
    def snapshot(self):
        return {"cands": [{"steps": c.steps,
                           "s": {m: {"s3": self.S.get((m, ci, 3), 0.0), "s4": self.S.get((m, ci, 4), 0.0)} for m in self.minds}}
                          for ci, c in sorted(self.cands.items())],
                "theta": self.theta, "objective": self.objective(), "loglik": self.total}

# ------------------------------------------------------------------ link support (shared by standings and the queue)
def link_support(model, cand):
    """-> (unsupported_links, unsupported_ties, weak): links between consecutive steps and ties inside steps that no
    WITNESSED triple (>= 2 answers in the candidate's order, and a majority) holds both glyphs of. `weak` maps each
    link/tie to the number of in-order answers it has so far (0 = never asked together)."""
    tl = collections.defaultdict(lambda: [0, 0])
    for i in model.obs_for(cand):
        o = model.obs[i]
        if len(set(o["tri"]) & set(cand.pos)) == 3:
            t = tl[o["tri"]]; t[1] += 1; t[0] += o["out"] == _strict(cand.pos, o["tri"])
    wit = {tri for tri, (ok, n) in tl.items() if ok >= WITNESS_MIN and ok >= 0.5 * n}
    def held(x, y, trs):
        return any(x in t and y in t for t in trs)
    def inorder(x, y):
        return sum(ok for tri, (ok, n) in tl.items() if x in tri and y in tri)
    links, ties, weak = [], [], {}
    for a, b in zip(cand.steps, cand.steps[1:]):
        if not any(held(x, y, wit) for x in a for y in b):
            k = (a[0], b[0]); links.append(k); weak[k] = max(inorder(x, y) for x in a for y in b)
    for st in cand.steps:
        for x in st:
            for y in st:
                if x < y and not held(x, y, wit):
                    ties.append((x, y)); weak[(x, y)] = inorder(x, y)
    return links, ties, weak

def contained_in(small, big):
    """True if every glyph of `small` is in `big` and their order agrees (either direction; ties in `big` allow any
    order of the tied glyphs). A contained sequence restates part of a longer one; it is not a branch."""
    ps = {g: i for i, st in enumerate(big) for g in st}
    g = [x for st in small for x in st]
    if not all(x in ps for x in g):
        return False
    seq = [ps[x] for x in g]
    return all(a <= b for a, b in zip(seq, seq[1:])) or all(a >= b for a, b in zip(seq, seq[1:]))

def maximal(seqs, key=len):
    """Indices of the sequences (step-lists) not contained in a longer (or, at equal length, earlier) one."""
    order = sorted(range(len(seqs)), key=lambda i: (-sum(len(st) for st in seqs[i]), i))
    keep = []
    for i in order:
        if not any(contained_in(seqs[i], seqs[j]) for j in keep):
            keep.append(i)
    return sorted(keep)

def supported_pieces(model, cand):
    """Split `cand` at every unsupported link and unwitnessed tie (see link_support): -> list of step-lists.
    Only these pieces count as established sequences (standings and the queue use the same rule)."""
    tl = collections.defaultdict(lambda: [0, 0])
    for i in model.obs_for(cand):
        o = model.obs[i]
        if len(set(o["tri"]) & set(cand.pos)) == 3:
            t = tl[o["tri"]]; t[1] += 1; t[0] += o["out"] == _strict(cand.pos, o["tri"])
    wit = {tri for tri, (ok, n) in tl.items() if ok >= WITNESS_MIN and ok >= 0.5 * n}
    def held(x, y):
        return any(x in t and y in t for t in wit)
    runs, cur = [], []
    for st in cand.steps:
        if any(not held(x, y) for x in st for y in st if x < y):
            if cur:
                runs.append(cur)
            runs.append([st]); cur = []
            continue
        if cur and not any(held(x, y) for x in cur[-1] for y in st):
            runs.append(cur); cur = []
        cur.append(st)
    if cur:
        runs.append(cur)
    return runs

# ------------------------------------------------------------------ annealing
def _neighbours(model, cand, k=40):
    """glyphs that co-occur with members of `cand` in a non-none outcome, most frequent first."""
    cnt = collections.Counter()
    for g in cand.pos:
        for i in model.g2obs.get(g, ()):
            o = model.obs[i]
            if o["out"][0] != "none":
                for h in o["tri"]:
                    if h not in cand.pos:
                        cnt[h] += 1
    return [g for g, _ in cnt.most_common(k)]

def _apply(model, kind, payload):
    """Apply a structural move; returns an undo closure, or None if the move is not applicable."""
    if kind == "replace":                      # payload: (cid or None, new steps or None)
        cid, steps = payload
        old = model.cands.get(cid) if cid is not None else None
        olds = {k: v for k, v in model.S.items() if cid is not None and k[1] == cid}
        idx = set(model.obs_for(old)) if old else set()
        if old:
            model.remove(cid)
        new_id = None
        if steps:
            c = Cand(steps)
            if len(c) < MIN_LEN or len(c.pos) != len(c.glyphs()):
                if old:
                    model.cands[cid] = old
                    for g in old.pos:
                        model.g2c[g].add(cid)
                    model.S.update(olds)
                return None
            new_id = model.add(c)
            idx |= set(model.obs_for(c))
            model.fit_s(new_id, list(idx), grid=GRID_COARSE)
        d = model.recompute(idx)
        def undo():
            if new_id is not None:
                model.remove(new_id)
            if old:
                model.cands[cid] = old
                for g in old.pos:
                    model.g2c[g].add(cid)
                model.S.update(olds)
            model.recompute(idx)
        return d, undo, new_id
    raise ValueError(kind)

def propose(model, r):
    """-> (cid or None, new steps or None) for one random structural move."""
    cids = sorted(model.cands)
    moves = ["spawn"] if not cids else ["spawn", "add", "add", "remove", "move", "swap", "tie", "untie", "split", "merge", "drop"]
    mv = r.choice(moves)
    if mv == "spawn":
        # from an observed ordered triple that no candidate holds whole
        for _ in range(20):
            o = model.obs[r.randrange(len(model.obs))]
            if o["out"][0] != "mid":
                continue
            if any(sum(1 for g in o["tri"] if g in model.cands[ci].pos) == 3 for ci in model.touching(o["tri"])):
                continue
            m = o["out"][1]; a, b = [g for g in o["tri"] if g != m]
            return None, [[a], [m], [b]]
        return None, None
    cid = r.choice(cids); c = model.cands[cid]; steps = [list(s) for s in c.steps]
    if mv == "add":
        nb = [g for g in _neighbours(model, c) if g not in c.pos]
        if not nb:
            return None, None
        g = nb[min(len(nb) - 1, int(r.expovariate(0.3)))]
        slot = r.randrange(2 * len(steps) + 1)
        if slot % 2 == 0:
            steps.insert(slot // 2, [g])
        else:
            steps[slot // 2].append(g)
        return cid, steps
    if mv == "remove":
        g = r.choice(c.glyphs())
        steps = [[x for x in s if x != g] for s in steps]
        return cid, [s for s in steps if s]
    if mv == "move":
        g = r.choice(c.glyphs())
        steps = [s for s in ([[x for x in s if x != g] for s in steps]) if s]
        slot = r.randrange(2 * len(steps) + 1)
        if slot % 2 == 0:
            steps.insert(slot // 2, [g])
        else:
            steps[slot // 2].append(g)
        return cid, steps
    if mv == "swap" and len(steps) >= 2:
        i = r.randrange(len(steps) - 1); steps[i], steps[i + 1] = steps[i + 1], steps[i]
        return cid, steps
    if mv == "tie" and len(steps) >= 2:
        i = r.randrange(len(steps) - 1); steps[i] = steps[i] + steps.pop(i + 1)
        return cid, steps
    if mv == "untie":
        ties = [i for i, s in enumerate(steps) if len(s) > 1]
        if not ties:
            return None, None
        i = r.choice(ties); s = steps[i]; g = r.choice(s); s.remove(g)
        steps.insert(i + (1 if r.random() < 0.5 else 0), [g])
        return cid, steps
    if mv == "split" and len(steps) >= 2 * MIN_LEN:
        i = r.randrange(MIN_LEN, len(steps) - MIN_LEN + 1)
        return ("split", cid, steps[:i], steps[i:]), None
    if mv == "merge" and len(cids) >= 2:
        other = r.choice([x for x in cids if x != cid])
        b = [list(s) for s in model.cands[other].steps]
        if set(c.pos) & set(model.cands[other].pos):
            return None, None
        a = steps if r.random() < 0.5 else steps[::-1]
        b = b if r.random() < 0.5 else b[::-1]
        return ("merge", cid, other, a + b), None
    if mv == "drop":
        return cid, None
    return None, None

def step(model, T, r):
    """One Metropolis step. Returns True if accepted."""
    p = propose(model, r)
    if p == (None, None):
        return False
    before = model.objective()
    first = p[0]
    undos = []
    if isinstance(first, tuple) and first[0] == "split":
        _, cid, a, b = first
        res = _apply(model, "replace", (cid, a))
        if res is None:
            return False
        undos.append(res[1])
        res2 = _apply(model, "replace", (None, b))
        if res2 is None:
            for u in reversed(undos):
                u()
            return False
        undos.append(res2[1])
    elif isinstance(first, tuple) and first[0] == "merge":
        _, cid, other, steps = first
        res = _apply(model, "replace", (other, None)); undos.append(res[1])
        res2 = _apply(model, "replace", (cid, steps))
        if res2 is None:
            for u in reversed(undos):
                u()
            return False
        undos.append(res2[1])
    else:
        cid, steps = p
        res = _apply(model, "replace", (cid, steps))
        if res is None:
            return False
        undos.append(res[1])
    delta = model.objective() - before
    if delta >= 0 or r.random() < math.exp(delta / max(T, 1e-6)):
        return True
    for u in reversed(undos):
        u()
    return False

def prune(model):
    changed = True
    while changed:
        changed = False
        for cid in sorted(model.cands):
            if cid not in model.cands:
                continue
            before = model.objective()
            res = _apply(model, "replace", (cid, None))
            if res and model.objective() > before + 1e-9:
                changed = True; continue
            if res:
                res[1]()
            c = model.cands.get(cid)
            if not c:
                continue
            for g in list(c.glyphs()):
                c = model.cands.get(cid)
                if not c or g not in c.pos or len(c) <= MIN_LEN:
                    break
                steps = [s for s in ([[x for x in st if x != g] for st in c.steps]) if s]
                before = model.objective()
                res = _apply(model, "replace", (cid, steps))
                if res is None:
                    continue
                if model.objective() > before + 1e-9:
                    changed = True; cid = res[2]
                else:
                    res[1]()

def anneal(model, seed_obj, iters=4000, T0=8.0, T1=0.3, theta_every=800, sample_every=0, n_samples=0):
    """Cool from T0 to T1, then (optionally) sample at T = 1. Returns list of posterior snapshots."""
    r = R("anneal", seed_obj)
    for ci in list(model.cands):
        model.fit_s(ci)
    model.recompute_all()
    samples = []
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / max(1, iters - 1))
        step(model, T, r)
        # structure first: nuisance parameters stay at their defaults for the first half, so that an empty model
        # cannot settle into "every answer is noise" before any candidate has had a chance (seen on real r000 data)
        if theta_every and it >= iters // 2 and (it + 1) % theta_every == 0:
            for ci in list(model.cands):
                model.fit_s(ci)
            model.fit_theta(1)
    for ci in list(model.cands):
        model.fit_s(ci)
    model.fit_theta(1)
    # greedy polish at T -> 0, then a deterministic prune: drop any candidate, or any glyph, whose removal improves the objective
    for it in range(iters // 4):
        step(model, 1e-3, r)
    prune(model)
    if n_samples:
        for it in range(n_samples * sample_every):
            step(model, 1.0, r)
            if (it + 1) % sample_every == 0:
                samples.append(model.snapshot())
    return samples

# ------------------------------------------------------------------ information (queue priority)
def bald(snapshots, minds, tri_obs_template):
    """Mutual information between the outcome of a would-be observation and the model, averaged over minds.
    snapshots: list of Model objects (posterior samples); tri_obs_template: dict like an observation, minus mind/out."""
    tot = 0.0
    for m in minds:
        ps = []
        for mod in snapshots:
            if m not in mod.theta:
                continue
            ps.append(predict({**tri_obs_template, "mind": m}, mod, m))
        if not ps:
            continue
        keys = set().union(*ps)
        mean = {k: sum(p.get(k, 0) for p in ps) / len(ps) for k in keys}
        H = lambda d: -sum(v * math.log(v) for v in d.values() if v > 1e-12)
        tot += H(mean) - sum(H(p) for p in ps) / len(ps)
    return tot / max(1, len(minds))

def from_snapshot(snap, obs, minds):
    m = Model(obs, minds)
    m.theta = {k: dict(v) for k, v in snap["theta"].items()}
    for k in minds:
        m.theta.setdefault(k, dict(DEFAULT_THETA))
    for c in snap["cands"]:
        cid = m.add(Cand(c["steps"]))
        for mind in minds:
            sv = c["s"].get(mind, {"s3": 0.0, "s4": 0.0})
            m.S[(mind, cid, 3)] = sv["s3"]; m.S[(mind, cid, 4)] = sv["s4"]
    m.recompute_all()
    return m
