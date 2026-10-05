"""The queue: what each round asks (PLAN.md §3). One priority order, Joseph's rule as he stated it (2026-10-04):

  "various minds start to find a sequence -- call it a sequence of three glyphs. The priority is then to extend that
   sequence to the right and to the left as far as they will go while still spending time looking for other 'kernels'
   from which to explore ... square away the most obvious and stable (empirically) sequences"
  "15% of our effort was always 'hot' -- exploring the space for more kernels ... based on bumps from the original seed"

  EXPLORE_SHARE of each round: hot exploration (explore_items: seed-bumped stochastic triads, sets, next questions), and
                               the rotation follow-ups that confirm an exploratory triad two minds ordered (a kernel).
  The rest: established sequences (model.supported_pieces, folded; piece_table), most stable first, each with its work
            in the order of sequence_work, taken greedily until the round's budget is spent (round.cmd_plan).
"""
import itertools, math, collections
from common import R, ok_glyph
import items as I
import model as M

P_PERP_RECHECK = 0.10      # share of first-presentation-⟂ triads that get a second presentation
SEED_BUMP = 2.0


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
    # fold restatements: a piece contained in a longer one (same order) is part of it, not a branch; keep the longer
    # one, with the higher stability of the two (found 2026-10-04: ⓵…⓾, ⓵…⓹ and ⓷⓸⓹ were counted as three)
    keep = M.maximal([x["steps"] for x in out])
    kept = []
    for i in keep:
        x = dict(out[i])
        for j, y in enumerate(out):
            if j != i and M.contained_in(y["steps"], x["steps"]) and y["stability"] > x["stability"]:
                x["stability"], x["U"], x["families"], x["support"] = y["stability"], y["U"], y["families"], y["support"]
        kept.append(x)
    return sorted(kept, key=lambda x: -x["stability"])

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

def seed_continuations(seeds):
    """(prev, end) -> Counter of glyphs that some seed writes directly beyond `end`, coming from `prev` (either
    reading direction). Seeds only raise priority (Joseph: "based on bumps from the original seed")."""
    out = collections.defaultdict(collections.Counter)
    for sd in seeds:
        g = list(dict.fromkeys(sd["glyphs"]))
        for seq in (g, g[::-1]):
            for a, b, x in zip(seq, seq[1:], seq[2:]):
                out[(a, b)][x] += 1
    return out

def extension_items(piece, st, neighbours, round_id, seed_next=None):
    """Items at one OPEN end of an established sequence: a next item (outward context of 3-5 glyphs), triads testing
    each proposal and the strongest co-occurring neighbours against the end's last two glyphs, and one order window
    at the end with the top proposal. Priority: the sequence's stability, plus 0.25 per mind that proposed the glyph."""
    g, a, b = st["g"], st["prev"], st["end"]
    src = {"kind": "extend", "ref": "".join(piece["glyphs"]), "end": b}
    r = R("extend", {"round": round_id, "piece": piece["glyphs"], "end": b})
    out = []
    k = min(len(g), r.randint(3, 5))
    out.append((I.make_item("next", context=g[-k:], source=src), piece["stability"] + 0.3))
    # candidates beyond this end, in order: what minds proposed here; what seeds write here; what co-occurs
    sn = (seed_next or {}).get((a, b), collections.Counter())
    cands = [x for x, _ in st["proposals"].most_common() if st["tested"][x] < 3 and ok_glyph(x) and x not in g]
    cands += [x for x, _ in sn.most_common() if x not in cands and x not in g and st["tested"][x] < 3 and ok_glyph(x)]
    cands += [x for x in neighbours if x not in cands and x not in g and st["tested"][x] < 3]
    for x in cands[:4]:
        bonus = 0.25 * st["proposals"].get(x, 0) + (0.5 if sn.get(x) else 0.0)
        out.append((I.make_item("triad", [a, b, x], source=dict(src, test=x, why="proposal" if st["proposals"].get(x) else
                                ("seed" if sn.get(x) else "co-occurrence"))), piece["stability"] + bonus))
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


def explore_items(pool, lineage_bump, seeds, round_id, n_tri, n_set, n_next, n_between=0):
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
    import unicodedata as _U
    def fresh_glyph():
        """the pilot's standing long tail (walk2/4/5 rand_glyph ranges), drawn FRESH every round: any glyph in the
        symbol space can be asked, not only those in the pool (fixed 2026-10-04: a pool frozen at init had made
        glyphs like '\\' unreachable -- Joseph's spinner |/-\\ could never have been found)"""
        while True:
            cp = r.choice([r.randint(0x20, 0x2BFF), r.randint(0x1F000, 0x1FBFF), r.randint(0x2E80, 0x33FF), r.randint(0x1D300, 0x1D7FF)])
            ch = chr(cp)
            try:
                _U.name(ch)
            except ValueError:
                continue
            if ok_glyph(ch):
                return ch
    def draw_glyph():
        if r.random() < 0.5:
            return fresh_glyph()                       # half the pool draws are fresh from the whole space
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
    # far pairs (Joseph: "Given two glyphs, even quite far apart, there's some chance an LLM can detect some more glyphs
    # that are linear to those in semantic space -- or a liminal feel"): what lies between them? From one seed, two
    # glyphs >= 2 steps apart in its written order; or two seed-bumped glyphs from the whole pool.
    made = 0
    while made < n_between:
        if sd and r.random() < 0.5:
            g = [x for x in dict.fromkeys(r.choice(sd)["glyphs"]) if ok_glyph(x)]
            if len(g) < 3:
                continue
            i = r.randrange(len(g) - 2); j = r.randrange(i + 2, len(g))
            a, b, how = g[i], g[j], "seed-far-pair"
        else:
            a, b, how = draw_glyph(), draw_glyph(), "pool-far-pair"
        if a == b or not ok_glyph(a) or not ok_glyph(b):
            continue
        items.append((I.make_item("between", left=[a], right=[b], source={"kind": "explore", "how": how}), 1.0)); made += 1
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
    # interleave kinds in a fated order, so a round's exploration budget gets the mix and not just the first kind
    # (bug found 2026-10-04: generated triads-first and taken in order, the 15% was nearly all triads)
    r.shuffle(items)
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

def interior_next(piece, round_id):
    """A what-comes-next question whose context stops INSIDE the sequence (or anywhere on a cycle), at a fated-random
    glyph and direction: where a branch could leave, the minds say what they see next there. (Found 2026-10-04: once
    0..9 grew on to 🔟, nothing ever asked what follows ...8 9 again, so 9 -> A for hex could only turn up by chance;
    co-occurrence-based branch checks cannot propose a glyph nobody has shown.)"""
    g = piece["glyphs"]; n = len(g)
    if n < 4 and not piece.get("cyclic"):
        return []
    r = R("interior-next", {"round": round_id, "piece": g})
    seq = g if r.random() < 0.5 else g[::-1]
    if piece.get("cyclic"):
        k = r.randrange(n); seq = seq[k:] + seq[:k]
        stop = n
    else:
        stop = r.randrange(2, n)                    # context ends at seq[stop-1], an interior glyph
    k = min(stop, r.randint(3, 5))
    ctx = seq[stop - k:stop]
    if len(ctx) < 2:
        return []
    return [I.make_item("next", context=ctx, source={"kind": "branch", "how": "interior-next", "ref": "".join(g), "at": ctx[-1]})]


# ================================================================== one priority order (Joseph's rule, as stated)
# "The priority is then to extend that sequence to the right and to the left as far as they will go while still
#  spending time looking for other kernels ... square away the most obvious and stable (empirically) sequences"
#  + "15% of our effort was always 'hot' -- exploring the space for more kernels ... based on bumps from the original seed"
# Replaces the category shares, per-category temperatures, decay and reserved list (2026-10-04, after Joseph asked
# "Why are we special casing?"). Two parts only:
#   EXPLORE_SHARE of presentations: hot exploration (stochastic, seed-bumped), and the rotation follow-ups that turn
#                                   an exploratory triad two minds ordered into a confirmed kernel;
#   the rest: ONE ordered list. Sequences most stable first; within each sequence, its work in this order:
#       1 open ends: what-comes-next question at each end, then the best untested candidate beyond each end
#       2 its unconfirmed links (support triads)
#       3 rotation follow-ups of its triads
#       4 the remaining candidates beyond its ends
#       5 one squaring window (order item) and one long-range check, if long
#       6 one interior what-comes-next (where a branch could leave), one branch check, gaps (between)
#   taken greedily until the budget is spent. Ties are broken by fated order.
EXPLORE_SHARE = 0.15

def sequence_work(pc, ends, cooc, seed_next, support_by_glyph, follow_by_glyph, round_id):
    """The ordered work list for one established sequence: [(tier, item_or_followup)]."""
    work = []
    tri_extra = []
    for st in ends:
        if st["closed"] or pc.get("cyclic"):
            continue
        nb = list(pc.get("hints", [])) + [x for x in cooc.get(st["end"], []) if x not in pc.get("hints", [])]
        gen = extension_items(pc, st, nb, round_id, seed_next)
        nx = [it for it, _ in gen if it["kind"] == "next"]
        tr = [it for it, _ in gen if it["kind"] == "triad"]
        orw = [it for it, _ in gen if it["kind"] == "order"]
        work += [(1, it) for it in nx]
        work += [(1, it) for it in tr[:1]]
        tri_extra += tr[1:] + orw
    g = set(pc["glyphs"])
    for t in pc.get("untested", []):          # consecutive triples of the sequence no answer has given yet
        try:
            work.append((2, I.make_item("triad", list(t), source={"kind": "step", "ref": "".join(pc["glyphs"])})))
        except AssertionError:
            pass
    # unresolved forks at this sequence: ask q x y (does one lie beyond the other, or is it a real branch?)
    for f in pc.get("forks", []):
        try:
            work.append((2, I.make_item("triad", [f["at"], f["x"], f["y"]], source={"kind": "fork", "at": f["at"]})))
        except AssertionError:
            pass
    seen = set()
    for x in pc["glyphs"]:
        for it in support_by_glyph.get(x, []):
            if it["iid"] not in seen:
                seen.add(it["iid"]); work.append((2, it))
    fseen = set()
    for x in pc["glyphs"]:
        for f in follow_by_glyph.get(x, []):
            if all(y in g for y in f[0]["glyphs"]) and (f[0]["iid"], f[1]) not in fseen:
                fseen.add((f[0]["iid"], f[1])); work.append((3, f))
    work += [(4, it) for it in tri_extra]
    sq = square_items(pc, round_id)
    work += [(5, it) for it, _ in sq[:2]]
    work += [(6, it) for it in interior_next(pc, round_id)]
    br = branch_items(pc, cooc, round_id)
    work += [(6, it) for it, _ in br[:1]]
    work += [(6, it) for it, _ in gap_items(pc, round_id)[:1]]
    return work
