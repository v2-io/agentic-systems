"""The stochastic queue (PLAN.md §4-5): generate candidate items from seeds, the uniform tail, the current fit
and frontier proposals; score them; draw a round by fated weighted sampling within category quotas.

Categories and base mixes (fractions of the round's items). Quotas are re-weighted after each round toward
categories whose items carried more expected information (`reweight`), within the floors.
"""
import itertools, math, collections
from common import R, ok_glyph
import items as I
import model as M

SUPPORT_SHARE = 0.20   # of each round's items, once candidates exist: tests of unsupported links and unwitnessed ties
EARLY = {("triad", "tail"): .15, ("triad", "seed"): .50, ("order", "seed"): .15,
         ("next", "seed"): .08, ("next", "tail"): .07, ("between", "seed"): .05}
LATE = {("triad", "tail"): .15, ("triad", "seed"): .08, ("triad", "support"): .15, ("triad", "cand"): .20,
        ("order", "seed"): .04, ("order", "support"): .05, ("order", "cand"): .16, ("next", "cand"): .07,
        ("next", "tail"): .05, ("next", "seed"): .02, ("between", "cand"): .03}
FLOORS_SUPPORT = {("triad", "support"): .10}
FLOORS = {("triad", "tail"): .10, ("next", "tail"): .05}
P_PERP_RECHECK = 0.10      # share of first-presentation-⟂ triads that get a second presentation
SEED_BUMP = 2.0

def _tri_template(item, rep=0):
    return {"tri": tuple(item["glyphs"]), "shown": tuple(I.shown_order(item, rep)), "ctx": 3, "forced": False,
            "tie_ok": False, "w": 1.0}

def info(item, samples, minds):
    """Expected information (BALD) of an item under posterior samples. 0 when there is no fit yet."""
    if not samples:
        return 0.0
    if item["kind"] == "triad":
        return M.bald(samples, minds, _tri_template(item))
    if item["kind"] == "order":
        g = item["glyphs"]; trips = list(itertools.combinations(g, 3))
        r = R("order-info", {"iid": item["iid"]}); r.shuffle(trips)
        vals = [M.bald(samples, minds, {"tri": tuple(sorted(t)), "shown": t, "ctx": len(g), "forced": False,
                                         "tie_ok": False, "w": 1.0}) for t in trips[:8]]
        return sum(vals) / max(1, len(vals)) * min(len(g) - 2, 4)
    return 0.0

def seed_items(seed):
    """Decompose a seed into primitive items (PLAN.md §4)."""
    g = [x for x in dict.fromkeys(seed["glyphs"]) if ok_glyph(x)]
    src = {"kind": "seed", "ref": seed["sid"]}
    out = []
    for i in range(len(g) - 2):
        out.append(I.make_item("triad", g[i:i + 3], source=dict(src, part="adjacent")))
    if len(g) >= 5:
        r = R("seed-longrange", {"sid": seed["sid"]})
        for _ in range(min(6, len(g))):
            i, j, k = sorted(r.sample(range(len(g)), 3))
            if k - i >= 3:
                out.append(I.make_item("triad", [g[i], g[j], g[k]], source=dict(src, part="long-range")))
    if len(g) >= 4:
        r = R("seed-window", {"sid": seed["sid"]})
        k = min(len(g), r.randint(4, 8)); s = r.randrange(len(g) - k + 1)
        out.append(I.make_item("order", g[s:s + k], source=dict(src, part="window")))
    if len(g) >= 2:
        r = R("seed-next", {"sid": seed["sid"]})
        c = min(len(g), r.randint(2, 4))
        out.append(I.make_item("next", context=g[-c:], source=dict(src, part="end")))
        out.append(I.make_item("next", context=g[:c][::-1], source=dict(src, part="end")))   # the other end
    if len(g) >= 3:
        r = R("seed-between", {"sid": seed["sid"]})
        i = r.randrange(1, len(g) - 1)
        out.append(I.make_item("between", left=[g[i - 1]], right=[g[i + 1]], source=dict(src, part="gap")))   # hides g[i]
    return out

def cand_items(snap, neighbours, round_id, ci):
    """Items probing candidate `ci` of the best fit: long-range triads (splice tests), adjacent triads,
    insertion triads for neighbouring glyphs, windows with salt, ends (next) and gaps (between)."""
    c = snap["cands"][ci]
    flat = [g for st in c["steps"] for g in st]
    src = {"kind": "cand", "ref": ci}
    r = R("cand-items", {"round": round_id, "ci": ci, "glyphs": flat})
    out = []
    n = len(flat)
    for _ in range(min(10, 2 * n)):
        if n >= 4:
            i, j, k = sorted(r.sample(range(n), 3))
            out.append(I.make_item("triad", [flat[i], flat[j], flat[k]], source=dict(src, part="long-range")))
    for i in range(n - 2):
        out.append(I.make_item("triad", flat[i:i + 3], source=dict(src, part="adjacent")))
    for g in neighbours[:8]:
        i = r.randrange(n - 1)
        out.append(I.make_item("triad", [flat[i], flat[i + 1], g], source=dict(src, part="insert")))
        out.append(I.make_item("triad", [flat[-2], flat[-1], g] if r.random() < 0.5 else [flat[0], flat[1], g],
                               source=dict(src, part="extend")))
    if n >= 4:
        for _ in range(3):
            k = min(n, r.randint(4, 8)); s = r.randrange(n - k + 1)
            win = flat[s:s + k]
            salt = [g for g in neighbours if g not in win][: r.randint(0, 2)]
            win = (win + salt)[:8]
            if len(set(win)) >= 4:
                out.append(I.make_item("order", win, source=dict(src, part="window", salt=salt)))
    for rev in (False, True):
        f = flat[::-1] if rev else flat
        cl = min(n, r.randint(2, 5))
        out.append(I.make_item("next", context=f[-cl:], source=dict(src, part="end")))
    for i in range(n - 1):
        if r.random() < 0.3:
            out.append(I.make_item("between", left=flat[max(0, i - 1):i + 1], right=flat[i + 1:i + 3], source=dict(src, part="gap")))
    return out

def tail_items(pool, round_id, n_tri, n_next):
    r = R("tail", {"round": round_id})
    out = []
    while sum(1 for x in out if x["kind"] == "triad") < n_tri:
        out.append(I.make_item("triad", r.sample(pool, 3), source={"kind": "tail"}))
    while sum(1 for x in out if x["kind"] == "next") < n_next:
        out.append(I.make_item("next", context=r.sample(pool, 2), source={"kind": "tail"}))
    return out

def draw(cands_by_cat, quotas, N, T, round_id, asked):
    """Fated weighted sampling without replacement within each category. Items already asked at rep 0 are
    excluded (follow-ups are separate). Returns [(item, category, priority)]."""
    chosen, seen = [], set()
    for cat in sorted(quotas, key=str):
        k = round(quotas[cat] * N)
        pool = [(it, p) for it, p in cands_by_cat.get(cat, []) if it["iid"] not in asked and it["iid"] not in seen]
        r = R("draw", {"round": round_id, "cat": list(cat)})
        for _ in range(min(k, len(pool))):
            ws = [math.exp(min(50.0, p / max(T, 1e-6))) for _, p in pool]
            x, acc = r.random() * sum(ws), 0.0
            for j, w in enumerate(ws):
                acc += w
                if x <= acc:
                    break
            it, p = pool.pop(j)
            seen.add(it["iid"]); chosen.append((it, cat, p))
    return chosen

def reweight(base, realized):
    """realized: {cat: mean information of drawn items}. Move 30% of the mass toward information, keep floors."""
    if not realized or sum(realized.values()) <= 0:
        return dict(base)
    tot = sum(realized.get(c, 0.0) for c in base) or 1.0
    q = {c: 0.7 * base[c] + 0.3 * realized.get(c, 0.0) / tot for c in base}
    for c, f in list(FLOORS.items()) + list(FLOORS_SUPPORT.items()):
        if c in q and q[c] < f:
            q[c] = f
    z = sum(q.values())
    return {c: v / z for c, v in q.items()}


def support_items(mod, cid, round_id):
    """Items that test candidate `cid`'s unsupported links and unwitnessed ties (Joseph, 2026-10-04: the standings'
    untested links show "what kind of sheets need higher priority"). For a link between steps i and i+1: triads with
    each outside neighbour (step i-1 or i+2) and one triad with a glyph two steps away, so both the link and its
    position are asked; for a tie: the tied pair with each neighbour. Plus one order window spanning the gap.
    Priority: 3 when never asked together, else 2 / (1 + in-order answers so far)."""
    c = mod.cands[cid]
    links, ties, weak = M.link_support(mod, c)
    steps = c.steps
    idx = {g: i for i, st in enumerate(steps) for g in st}
    out = []
    r = R("support-items", {"round": round_id, "cand": c.key()})
    def pr(k):
        w = weak.get(k, 0)
        return 3.0 if w == 0 else 2.0 / (1 + w)
    for a, b in links:
        i = idx[a]
        around = [steps[j][0] for j in (i - 1, i + 2, i - 2, i + 3) if 0 <= j < len(steps)]
        for g in around[:3]:
            if g not in (a, b):
                out.append((I.make_item("triad", [a, b, g], source={"kind": "support", "ref": "link", "link": a + b}), pr((a, b))))
        lo, hi = max(0, i - 2), min(len(steps), i + 4)
        win = [st[0] for st in steps[lo:hi]]
        if len(set(win)) >= 4:
            out.append((I.make_item("order", win[:8], source={"kind": "support", "ref": "window", "link": a + b}), pr((a, b))))
    for x, y in ties:
        i = idx[x]
        around = [steps[j][0] for j in (i - 1, i + 1) if 0 <= j < len(steps) and steps[j][0] not in (x, y)]
        for g in around:
            out.append((I.make_item("triad", [x, y, g], source={"kind": "support", "ref": "tie", "tie": x + y}), pr((x, y))))
    return out


# ================================================================== kernel growth (Joseph, 2026-10-04)
# "various minds start to find a sequence ... The priority is then to extend that sequence to the right and to the left
#  as far as they will go while still spending time looking for other kernels ... square away the most obvious and
#  stable (empirically) sequences" -- and: "15% of our effort was always 'hot' -- exploring the space for more kernels".
# Every round splits its items, concurrently (none of these waits on another):
GROW = {
    # hot exploration: always on (>= 15%), one stochastic draw over the whole pool with seed bumps; absorbs any share
    # the other categories cannot fill (early rounds, when few sequences are established yet)
    ("triad", "explore"): .12, ("order", "explore"): .06, ("next", "explore"): .02,
    # extend established sequences outward from both ends, most stable first, with diminishing returns per sequence
    ("next", "extend"): .12, ("triad", "extend"): .25, ("order", "extend"): .03, ("between", "extend"): .05,
    # branch: other sequences crossing an established one at a middle glyph
    ("triad", "branch"): .05,
    # square away established sequences: unsupported links/ties, order windows, splice checks
    ("triad", "support"): .15, ("order", "square"): .10, ("triad", "square"): .05,
}
EXPLORE_FLOOR = 0.15
EXPLORE_CATS = [("triad", "explore"), ("order", "explore"), ("next", "explore")]
FOLLOW_SHARE = 0.15        # of presentations: Latin-rotation follow-ups, for triads inside established sequences first
END_MIN_ANSWERS = 6        # an end is closed once >= this many next-answers have been given at it ...
END_NONE_SHARE = 0.7       # ... and >= this share of them were "none", and every proposal made at it has been tested

def piece_table(cur, snap, fam, min_evid=3):
    """Established sequences = supported pieces (>= 3 glyphs) of the fit's candidates, with a stability score
    (support x U x sqrt(family coverage); the same measure as the standings)."""
    fams = sorted(set(fam.values()))
    out = []
    for (cid, c), cs, sup in zip(sorted(cur.cands.items()), snap["cands"], snap.get("support_list", [1.0] * len(snap["cands"]))):
        for steps in M.supported_pieces(cur, c):
            if sum(len(st) for st in steps) < 3:
                continue
            g = [x for st in steps for x in st]
            ev = collections.Counter(cur.obs[i]["mind"] for i in cur.obs_for(M.Cand(steps)) if all(x in g for x in cur.obs[i]["tri"]))
            per = {}
            for f in fams:
                ms = [m for m in cs["s"] if fam.get(m) == f and ev[m] >= min_evid]
                if ms:
                    per[f] = sum(max(cs["s"][m]["s3"], cs["s"][m]["s4"]) for m in ms) / len(ms)
            U = sum(per.values()) / len(per) if per else 0.0
            stab = sup * U * math.sqrt(len(per) / max(1, len(fams)))
            out.append({"steps": steps, "glyphs": g, "stability": stab, "families": len(per), "U": U, "support": sup})
    return sorted(out, key=lambda x: -x["stability"])

def end_state(piece, side, parsed, pres, items):
    """What has been asked at one end: next-answers whose context ends with this end's last two glyphs (in the
    outward direction), their proposals, and which proposals have been tested in a triad with those two glyphs."""
    g = piece["glyphs"] if side == "right" else piece["glyphs"][::-1]
    a, b = g[-2], g[-1]
    ans, props, tested = [], collections.Counter(), collections.Counter()
    for r in parsed:
        if r["status"] != "ok":
            continue
        p = pres[r["pid"]]
        if p["kind"] == "next" and p["shown"][-2:] == [a, b]:
            ans.append(r["answer"])
            for x in r["answer"].get("proposals", []):
                if x not in g:
                    props[x] += 1
        elif p["kind"] == "triad" and a in p["shown"] and b in p["shown"]:
            third = [x for x in p["shown"] if x not in (a, b)][0]
            tested[third] += 1
    none = sum(1 for x in ans if x.get("none"))
    untested = [x for x in props if tested[x] < 3]
    closed = len(ans) >= END_MIN_ANSWERS and none / len(ans) >= END_NONE_SHARE and not untested
    return {"end": b, "prev": a, "answers": len(ans), "none_share": none / len(ans) if ans else None,
            "proposals": props, "tested": tested, "closed": closed, "g": g}

def extension_items(piece, st, neighbours, round_id):
    """Items at one OPEN end of an established sequence: a next item (outward context of 3-5 glyphs), triads testing
    each proposal and the strongest co-occurring neighbours against the end's last two glyphs, and one order window
    at the end with the top proposal. Priority: the sequence's stability, plus 0.25 per mind that proposed the glyph."""
    g, a, b = st["g"], st["prev"], st["end"]
    src = {"kind": "extend", "ref": "".join(piece["glyphs"]), "end": b}
    r = R("extend", {"round": round_id, "piece": piece["glyphs"], "end": b})
    out = []
    k = min(len(g), r.randint(3, 5))
    out.append((I.make_item("next", context=g[-k:], source=src), piece["stability"]))
    cands = [x for x, _ in st["proposals"].most_common() if st["tested"][x] < 3 and ok_glyph(x) and x not in g]
    cands += [x for x in neighbours if x not in cands and x not in g and st["tested"][x] < 3]
    for x in cands[:4]:
        out.append((I.make_item("triad", [a, b, x], source=dict(src, test=x)), piece["stability"] + 0.25 * st["proposals"].get(x, 0)))
    if cands and len(g) >= 3:
        win = g[-min(len(g), 6):] + [cands[0]]
        if len(set(win)) >= 4:
            out.append((I.make_item("order", win[:8], source=dict(src, test=cands[0])), piece["stability"]))
    return out

def gap_items(piece, round_id):
    """between items inside an established sequence (does anything belong between neighbours?)."""
    g = piece["glyphs"]
    r = R("gaps", {"round": round_id, "piece": g})
    out = []
    for i in range(len(g) - 1):
        if r.random() < 0.5:
            out.append((I.make_item("between", left=g[max(0, i - 1):i + 1], right=g[i + 1:i + 3],
                                    source={"kind": "extend", "ref": "".join(g), "gap": g[i] + g[i + 1]}), piece["stability"] * 0.8))
    return out

def square_items(piece, round_id):
    """Order windows over the sequence and long-range triads (splice checks) on long ones."""
    g = piece["glyphs"]; n = len(g)
    r = R("square", {"round": round_id, "piece": g})
    out = []
    if n >= 4:
        k = min(n, 8); s0 = r.randrange(n - k + 1)
        out.append((I.make_item("order", g[s0:s0 + k], source={"kind": "square", "ref": "".join(g), "part": "window"}), piece["stability"]))
    if n >= 5:
        for _ in range(min(4, n - 3)):
            i, j, k2 = sorted(r.sample(range(n), 3))
            if k2 - i >= 3:
                out.append((I.make_item("triad", [g[i], g[j], g[k2]], source={"kind": "square", "ref": "".join(g), "part": "long-range"}),
                            piece["stability"] * 0.8))
    return out


def explore_items(pool, lineage_bump, seeds, round_id, n_tri, n_set, n_next):
    """Hot exploration (Joseph: "15% of our effort was always 'hot' ... based on bumps from the original seed").
    Glyphs are drawn with weight 1, or the seed's bump for glyphs any seed names. With probability 1/2 an item's glyphs
    come from ONE seed (its local neighbourhood: the seed becomes a kernel candidate), else independently from the
    weighted pool. Sets (4-6 glyphs) are a third of it, so holistic kernels, invisible to triads, can be found."""
    r = R("explore", {"round": round_id})
    w = [lineage_bump.get(g, 1.0) for g in pool]
    tot = sum(w)
    cum, acc = [], 0.0
    for x in w:
        acc += x; cum.append(acc)
    import bisect
    def draw_glyph():
        return pool[min(len(pool) - 1, bisect.bisect_left(cum, r.random() * tot))]
    sd = [x for x in seeds if len(set(x["glyphs"])) >= 3]
    def draw_set(k):
        if sd and r.random() < 0.5:
            g = list(dict.fromkeys(r.choice(sd)["glyphs"]))
            if len(g) >= k:
                return r.sample(g, k), "seed-local"
        out = []
        while len(out) < k:
            x = draw_glyph()
            if x not in out:
                out.append(x)
        return out, "weighted-pool"
    items = []
    for kind, n in (("triad", n_tri), ("order", n_set), ("next", n_next)):
        made = 0
        while made < n:
            k = 3 if kind == "triad" else (r.randint(4, 6) if kind == "order" else 2)
            g, how = draw_set(k)
            if not all(ok_glyph(x) for x in g):
                continue
            try:
                it = I.make_item(kind, glyphs=g, source={"kind": "explore", "how": how}) if kind != "next" else \
                     I.make_item("next", context=g, source={"kind": "explore", "how": how})
            except AssertionError:
                continue
            items.append((it, sum(lineage_bump.get(x, 1.0) for x in g) / len(g))); made += 1
    return items

def branch_items(piece, neighbours_by_glyph, round_id):
    """Crossings: (mid-sequence glyph, its neighbour in the sequence, an outside glyph that co-occurs with it)."""
    g = piece["glyphs"]
    r = R("branch", {"round": round_id, "piece": g})
    out = []
    for i in range(1, len(g) - 1):
        outside = [x for x in neighbours_by_glyph.get(g[i], []) if x not in g]
        if outside:
            x = outside[0] if r.random() < 0.6 else r.choice(outside)
            nb = g[i - 1] if r.random() < 0.5 else g[i + 1]
            out.append((I.make_item("triad", [nb, g[i], x], source={"kind": "branch", "ref": "".join(g), "at": g[i]}), piece["stability"] * 0.7))
    return out
