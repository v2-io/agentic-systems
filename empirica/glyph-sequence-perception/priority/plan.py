"""Concern 3: what to ask next (METHODOLOGY §5). Reads the tree; writes questions, never evidence.

THE PRINCIPLE (Joseph, 2026-10-06): "stochastic probing, weight toward where it will be most clarifying" -- "I prefer
stochastic all the way down, including jitter and stuff (I don't even like having the same number of questions per
round etc.)". Earlier: "I wouldn't outright exclude *anything* -- when I do stochastic work I always use s-curves with
there always being a long tail". So every candidate question has a nonzero chance every round, re-asking included,
and nothing here is a cut. What the planner may refuse is only what cannot be asked validly (a glyph that is not one,
a context that repeats a glyph, a length the prompts do not support) and a second copy within one round.

HOW A ROUND IS DRAWN
  Size     each STREAM (a kind of work, below) has a base size, the mean of what c096-c100 asked; this round's size of
           each is base x (budget / 700) x a round-wide factor x a per-stream factor, both lognormal (sigmas
           SIZE_SIGMA_ROUND, SIZE_SIGMA_STREAM). So neither the round nor any share is the same twice.
  Weight   every candidate UNIT (a question, or a question with its controls) gets
               weight = relevance x information
           INFORMATION is the expected information (nats) that one more answer from each family adds about the
           quantity the question measures, summed over the families that answer it: for a share with k of n
           answers, a Beta(k + 1/2, n - k + 1/2) posterior (Jeffreys), the mutual information between the next
           answer and the share,
               I(k, n) = h(m) + m (psi(a + 1) - psi(a + b + 1)) + (1 - m) (psi(b + 1) - psi(a + b + 1)),   m = a / (a + b)
           -- 0.307 nats unasked, about 1 / (2n) once n answers agree. Never zero: the most settled item is re-asked,
           exceedingly rarely. Answers ASKED BUT NOT YET GIVEN (the drains lag; pending()) count as expected answers,
           so the planner does not re-ask what a slow family has not reached yet -- unless that mind is paused until
           a quota resets (data/logs/paused.json), when its answers are not expected.
           RELEVANCE is how much the quantity bears on a sequence: an S-curve with a floor (scurve) on the strength
           of the sequence it serves (the tree's rank), so "the most obvious and stable (empirically) sequences" are
           squared away first (Joseph, 2026-10-05) and nothing falls to zero.
  Draw     within a stream, a fated weighted draw without replacement (Efraimidis-Spirakis keys u^(1/w)): heavy
           units early, light ones anywhere, until the stream's size is reached.
Every number named here is listed in PARAMS, chosen without evidence unless it says otherwise.

STREAMS (each a kind of work; the sources are where candidates come from, never evidence):
  explore         2-glyph contexts never asked: seed bumps, fresh glyphs (printable ASCII 4 : 2-byte 3 : 3-byte 2 :
                  4-byte 1) with a code-point neighbour or another fresh glyph, and triad-agreed kernels (§4).
  continue        contexts along the tree's sequences: every end (open, ended, and cycle probes showing less than a
                  period; at END_RELEVANCE, since only an end can extend a sequence), every suffix of every walked step's context (k*), longer contexts along the path
                  (lengthening, the stability test of §3), contexts ending on interior glyphs, contexts approaching a
                  weak link from the far side, and the deciding contexts themselves (replication).
  inhibit         link recognition, each with a matched near or far decoy: candidates the reasoned pass and written
                  momentum produced, runners-up at branch points, and skip tests (the glyph after next: a sequence
                  predicts "no"), weighted by how strong the claim tested is (the strongest tested hardest).
  cohere          whole runs, each with its shuffled control (and a chart window at CHART_CONTROL_SHARE): the tree's
                  walks, runs written answers carry, ordered seeds, pick branches, shuffles some mind called coherent,
                  the triad era's grown rows (CATALOG §3), and every run asked before; runs longer than the question
                  shows in overlapping windows. Shown in a fated orientation each time.
  lookalike       a run some mind called coherent, strictly monotone in code points, with one interior glyph swapped
                  for a confusable from another block, and its fated non-confusable control (CATALOG §7b, §11).
  choose          discriminator positions: the chart's next glyph against the run's glyph (steps of runs), and
                  contexts whose answers include both a chart-adjacent and a non-adjacent glyph (splits). Positions
                  the chart does not contest (another Unicode block, CATALOG §7a) are candidates on equal terms
                  (about 1% of positions): what they test is the block rule itself. Tagged probe.contested.
  choose-control  D controls: a pair after three fresh glyphs from other blocks, fated per round.
  names           the name-only order question: its validation sets (relevance VALIDATION_RELEVANCE, since the name
                  route waits on them), ordered seeds, and runs some mind called coherent.
  order, triad    order a scrambled set; the middle of a triple: sets and triples from runs and seeds, and every
                  one asked before.
  pick, pick-null the generator (§4a): known sequences and every branch grown so far, SAMPLES times per generator
                  mind; the null, fresh random contexts of the same lengths.
  reasoned        felt ends of sequences, for the reasoner minds (generation, kept apart).
  reflection      `a b c b -> ?` inside sequences (§3, kept apart).
Joseph's own seeds get STEWARD_RELEVANCE wherever seeds are a source.

History: until 2026-10-06 this module selected rather than sampled: fixed tiers filled greedily (tiers 4 and 5 never
got budget), fixed per-round caps over fixed orders, hard thresholds (agreement 0.75, yes share 0.5, rank 0.75), and
every question asked once (a weak context re-asked at most once). Each rule had a local reason (git log; METHODOLOGY
§5) and none could be revisited by the data. Joseph, on reading the list: "every 'rule' you just noted, were all
contrived and contrary to the methodology and my instincts for experiment design."
"""
import collections, json, math, pathlib, sys, unicodedata as U

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[1]
DATA = ROOT / "data"
sys.path.insert(0, str(ROOT / "probe"))
sys.path.insert(0, str(ROOT / "tree"))
import probe as PR                                          # noqa: E402
import tree as TR                                           # noqa: E402

FAMS = ("claude", "gemini", "grok")                         # the families the core roster answers with
BASE = {                                                     # questions a round per stream: the c096-c100 means
    "explore": 105, "continue": 167, "inhibit": 74, "cohere": 176, "lookalike": 40, "choose": 60,
    "choose-control": 20, "names": 30, "order": 13, "triad": 15, "pick": 150, "pick-null": 35,
    "reasoned": 20, "reflection": 20}
PARAMS = {                                                   # every one chosen without evidence
    "SIZE_SIGMA_ROUND": 0.15,      # lognormal sigma of the round-wide size factor
    "SIZE_SIGMA_STREAM": 0.25,     # lognormal sigma of each stream's own size factor
    "REL_FLOOR": 0.05, "REL_MID": 0.5, "REL_WIDTH": 0.12,   # relevance S-curve on a sequence's rank (tree rank, 0-1)
    "END_RELEVANCE": 5.0,          # a context at a sequence's end: only there can a question extend it (Joseph's rule,
                                   # "extend that sequence to the right and to the left as far as they will go")
    "VALIDATION_RELEVANCE": 3.0,   # the name-only question's validation sets
    "STEWARD_RELEVANCE": 3.0,      # Joseph's own seeds
    "CHART_CONTROL_SHARE": 0.25,   # cohere runs that also get a chart window (a measurement, not a decoy)
    "PICK_NULL_EVERY": 4,          # one null context per this many real pick contexts (sizes the pick-null base)
    "MAX_WINDOW_STEP": 0.5,        # windows of long runs overlap by half a window
}
BRANCH_FLOOR, BRANCH_MID, BRANCH_WIDTH = 0.02, 0.10, 0.04  # pick branches: S-curve on a branch's share of its draws
# A branch's weight w(q) = FLOOR + (1 - FLOOR) / (1 + exp(-(q - MID) / WIDTH)): a main branch ~1, a single draw of 20
# ~0.24, nothing below FLOOR (Joseph's tendril design, METHODOLOGY §4a).
NAME_VALIDATION = {"meaning-vs-code": ["⁰¹²³⁴", "⅕¼⅓½⅔¾", "🕐🕜🕑🕝🕒", "⓪①②③④", "❽❾❿⓫⓬", "▕🮇🮈▐🮉🮊🮋"],
                   "uninformative": ["♠♣♥♦", "☂☃☄★☎", "§¶†•※"]}
# CATALOG v5 §7a: each set is written in the order its names' MEANING gives; the first group's code-point order
# differs from it (a name-only order that follows the code points is chart recall through the names); the second
# group's names carry no order (expected: "none").
FRESH_TIERS = {"1-byte": (4, [(0x21, 0x7E)]), "2-byte": (3, [(0xA1, 0x7FF)]),
               "3-byte": (2, [(0x2000, 0x2BFF), (0x2E80, 0x33FF)]), "4-byte": (1, [(0x1D300, 0x1D7FF), (0x1F000, 0x1FBFF)])}
ORDERED_SEEDS = {"sequence", "morph", "cyclic", "generator"}   # seed types that propose an order: runs
ORDER_ONLY_SEEDS = {"set", "negative"}                         # no order proposed: the order question only
MAXK = 8                                                       # the longest shown context (probe's limit)

# ------------------------------------------------------------------ the numbers
def psi(x):
    """digamma, by recurrence to x >= 6 and the asymptotic series (pure Python, so nothing outside the code moves it)"""
    r = 0.0
    while x < 6:
        r -= 1 / x; x += 1
    f = 1 / (x * x)
    return r + math.log(x) - 0.5 / x - f * (1 / 12 - f * (1 / 120 - f * (1 / 252 - f * (1 / 240 - f / 132))))

def info(k, n):
    """expected information (nats) one more yes/no answer adds about a share with k of n so far (Jeffreys prior)"""
    a, b = k + 0.5, n - k + 0.5
    m = a / (a + b)
    h = -(m * math.log(m) + (1 - m) * math.log(1 - m))
    return max(h + m * (psi(a + 1) - psi(a + b + 1)) + (1 - m) * (psi(b + 1) - psi(a + b + 1)), 1e-9)

def info_fams(counts, pend=None):
    """summed over the core families: counts {family: (k, n)}; pend {family: answers asked but not yet given}, counted
    as answers at the family's current posterior mean"""
    tot = 0.0
    for f in FAMS:
        k, n = counts.get(f, (0, 0))
        p = (pend or {}).get(f, 0)
        if p:
            k, n = k + p * (k + 0.5) / (n + 1), n + p
        tot += info(k, n)
    return tot

def scurve(v, mid=None, width=None, floor=None):
    mid = PARAMS["REL_MID"] if mid is None else mid
    width = PARAMS["REL_WIDTH"] if width is None else width
    floor = PARAMS["REL_FLOOR"] if floor is None else floor
    return floor + (1 - floor) / (1 + math.exp(-(v - mid) / width))

def branch_weight(k, n):
    return scurve(k / n, BRANCH_MID, BRANCH_WIDTH, BRANCH_FLOOR)

def weighted_order(items, weight, r):
    """a fated draw of every item without replacement, each next one with probability proportional to its weight
    (Efraimidis-Spirakis keys u^(1/w)): heavy items early, light ones still anywhere -> list"""
    keyed = []
    for i, it in enumerate(items):
        w = weight(it)
        keyed.append((math.log(max(r.random(), 1e-300)) / w, i))
    return [items[i] for _, i in sorted(keyed, reverse=True)]

# ------------------------------------------------------------------ helpers (also used by the catalog)
def fresh_glyph(r):
    while True:
        tier = r.choices(list(FRESH_TIERS), weights=[FRESH_TIERS[t][0] for t in FRESH_TIERS])[0]
        spans = FRESH_TIERS[tier][1]
        lo, hi = r.choices(spans, weights=[b - a + 1 for a, b in spans])[0]
        ch = chr(r.randint(lo, hi))
        if PR.is_glyph(ch) and U.category(ch) != "Cn":
            return ch

def is_steward(x):
    """Joseph's own seeds: the author is Joseph, exactly (until 2026-10-06 any author containing "joseph" matched, so
    the session's completion of his seed got his priority; v3 audit)"""
    return str(x.get("surveyor") or x.get("author") or "").strip().lower() == "joseph"

def seed_list(seeds, types, rid, purpose):
    """seeds of the given types as runs [(glyphs, sid)] in a fated order, the steward's first; a cycle written closed is
    opened; glyphs that repeat are not a run"""
    out = []
    for x in seeds:
        if (x.get("type") or x.get("kind")) not in types or not isinstance(x.get("glyphs"), list):
            continue
        g = list(x["glyphs"])
        if len(g) > 1 and g[-1] == g[0]:
            g = g[:-1]
        if len(set(g)) == len(g):
            out.append((g, x.get("sid"), is_steward(x)))
    PR.R(purpose, {"round": rid}).shuffle(out)
    out.sort(key=lambda t: not t[2])
    return [(g, sid) for g, sid, _ in out]

def steward_seeds(seeds):
    return {tuple(x["glyphs"]) for x in seeds if is_steward(x) and isinstance(x.get("glyphs"), list)}

_BLOCKS = None

def block(ch):
    """the Unicode 16 block of a glyph (data/unicode/Blocks-16.0.0.txt), or None"""
    global _BLOCKS
    if _BLOCKS is None:
        _BLOCKS = []
        for l in open(DATA / "unicode" / "Blocks-16.0.0.txt", encoding="utf-8"):
            l = l.split("#")[0].strip()
            if l:
                r, n = l.split(";")
                a, b = r.split("..")
                _BLOCKS.append((int(a, 16), int(b, 16), n.strip()))
    o = ord(ch)
    for a, b, n in _BLOCKS:
        if a <= o <= b:
            return n
    return None

def contested(chart, last):
    """CATALOG v5 §7a: the chart's candidate is a contested alternative when it is in the block of the glyph before it
    (triad departures from the code-point median: 0.13 within one block, 0.69 across three; spikes/contested-positions).
    A READING rule. The planner asks uncontested positions too, at lower relevance: that is how the rule gets tested."""
    return block(chart) is not None and block(chart) == block(last)

def chart_neighbour(prev, last):
    """the code-chart neighbour of `last` in the run's direction (from prev to last), if it is an assigned glyph"""
    d = 1 if ord(last) >= ord(prev) else -1
    c = ord(last) + d
    if 0x20 < c < 0x110000:
        x = chr(c)
        if PR.is_glyph(x) and U.category(x) != "Cn":
            return x
    return None

_SKELETON = None

def confusables(g):
    """single glyphs confusable with g (UTS #39, data/unicode/confusables-16.0.0.txt): the same skeleton"""
    global _SKELETON
    if _SKELETON is None:
        sk = {}
        for l in open(DATA / "unicode" / "confusables-16.0.0.txt", encoding="utf-8-sig"):
            l = l.split("#")[0].strip()
            if not l:
                continue
            src, tgt = [f.strip() for f in l.split(";")[:2]]
            if " " in src:
                continue
            sk[chr(int(src, 16))] = "".join(chr(int(h, 16)) for h in tgt.split())
        groups = collections.defaultdict(set)
        for c, t in sk.items():
            groups[t].add(c)
            if len(t) == 1:
                groups[t].add(t)
        _SKELETON = (sk, groups)
    sk, groups = _SKELETON
    return sorted(x for x in groups.get(sk.get(g, g), ()) if x != g)

def runlike(g, lo=3, hi=PR.MAX_RUN):
    return lo <= len(g) <= hi and len(set(g)) == len(g) and all(PR.is_glyph(c) for c in g)

def windows(g, size):
    """g itself if it fits, else overlapping windows of `size`, about half a window apart, the last flush with the end"""
    g = list(g)
    if len(g) <= size:
        return [g]
    step = max(1, int(size * PARAMS["MAX_WINDOW_STEP"]))
    starts = sorted(set(list(range(0, len(g) - size + 1, step)) + [len(g) - size]))
    return [g[i:i + size] for i in starts]

# ------------------------------------------------------------------ what has been asked, and not yet answered
def pending(recs, rid):
    """answers asked but not yet given, per question identity and family: for every context round before `rid` (void
    rounds excluded), each sheet's entries x the minds assigned, less the records that exist for them (a record exists
    once a mind answered or gave up). -> {qid: {family: count}}, and {qid: question}"""
    try:
        void = set(json.load(open(DATA / "rounds" / "VOID.json"))["rounds"])
    except FileNotFoundError:
        void = set()
    fam = {m: s.get("family") for m, s in json.load(open(ROOT / "core" / "minds.json"))["minds"].items()}
    try:                                       # a mind paused until its quota resets (run.py) is not about to answer
        import time
        paused = {m for m, t in json.load(open(DATA / "logs" / "paused.json")).items() if t > time.time()}
    except Exception:
        paused = set()
    asked = collections.defaultdict(collections.Counter)
    qs = {}
    for rd in sorted((DATA / "rounds").glob("c[0-9][0-9][0-9]")):
        if rd.name in void or rd.name >= rid or not (rd / "sheets.jsonl").exists():
            continue
        for l in open(rd / "questions.jsonl"):
            if l.strip():
                q = json.loads(l); qs[q["qid"]] = q
        for l in open(rd / "sheets.jsonl"):
            if not l.strip():
                continue
            s = json.loads(l)
            for e in s["entries"]:
                for m in s.get("minds", []):
                    if m not in paused:
                        asked[e["qid"]][fam.get(m)] += 1
    for r in recs:
        if r.get("era") == "ctx" and r.get("qid") in asked:
            asked[r["qid"]][r["family"]] -= 1
    return {q: {f: n for f, n in c.items() if n > 0} for q, c in asked.items() if any(n > 0 for n in c.values())}, qs

class Pending:
    """pending answers indexed by what each question measures"""
    def __init__(self, recs, rid):
        pend, qs = pending(recs, rid)
        self.by = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
        for qid, fc in pend.items():
            q = qs.get(qid)
            if not q:
                continue
            k, c = q["kind"], tuple(q.get("context") or ())
            v = (q.get("variant") or "")
            if k == "continue":
                key = (("reasoned" if v == "reasoned" else "reflection" if v == "reflection" else "continue"), c)
            elif k == "inhibit":
                key = ("inhibit", (c, q.get("candidate")))
            elif k == "cohere":
                key = ("cohere", tuple(min(list(c), list(c)[::-1])))
            elif k == "choose":
                pair = frozenset(q.get("pair") or ())
                key = ("choose-control", pair) if (q.get("probe") or {}).get("control") == "neutral" else ("choose", (c, pair))
            elif k in ("order", "names", "triad"):
                key = (k, frozenset(q.get("glyphs") or c) if k != "triad" else tuple(sorted(q.get("glyphs") or c)))
            elif k == "pick":
                key = ("pick", c)
            else:
                continue
            self.by[key[0]][key[1]].update(fc)
    def get(self, kind, key):
        return self.by.get(kind, {}).get(key, {})

# ------------------------------------------------------------------ counts per family, from the tree
def counts_top(fl):
    """{family: [answers]} -> {family: (k naming the pooled top answer, n)}"""
    pooled = collections.Counter(x for xs in fl.values() for x in xs)
    if not pooled:
        return {}
    top = max(pooled.items(), key=lambda kv: (kv[1], str(kv[0])))[0]
    return {f: (sum(1 for x in xs if x == top), len(xs)) for f, xs in fl.items()}

def counts_yes(fc):
    """{family: Counter(yes/no/cant-tell)} -> {family: (yes, n)}"""
    return {f: (c.get("yes", 0), sum(c.values())) for f, c in fc.items()}

def order_counts(T):
    """per shown set (frozenset), per family: (answers giving the set's modal main line, answers) -- the order question,
    both eras; a main line is an answer's longest line, either direction one, ties as one step"""
    by = collections.defaultdict(list)
    seen = set()
    for x, items in T.orders.items():
        for f, shown, lines in items:
            if id(lines) in seen:
                continue
            seen.add(id(lines))
            main = max(lines, key=lambda ln: sum(len(st) for st in ln if st != "GAP")) if lines else []
            c = tuple("…" if st == "GAP" else "=".join(sorted(st)) for st in main)
            by[frozenset(shown)].append((f, min(c, c[::-1])))
    out = {}
    for key, rows in by.items():
        top = collections.Counter(c for _, c in rows).most_common(1)[0][0]
        fc = collections.defaultdict(lambda: [0, 0])
        for f, c in rows:
            fc[f][1] += 1; fc[f][0] += c == top
        out[key] = {f: tuple(v) for f, v in fc.items()}
    return out

def names_counts(T):
    out = {}
    for key, rows in T.names.items():
        canon = []
        for f, m, a in rows:
            if isinstance(a, dict):
                lines = a.get("lines") or []
                main = max(lines, key=lambda ln: sum(len(st) for st in ln if st != "GAP")) if lines else []
                c = tuple("…" if st == "GAP" else "=".join(sorted(st)) for st in main)
                canon.append((f, min(c, c[::-1]) if c else ("none",)))
            else:
                canon.append((f, (str(a),)))
        top = collections.Counter(c for _, c in canon).most_common(1)[0][0]
        fc = collections.defaultdict(lambda: [0, 0])
        for f, c in canon:
            fc[f][1] += 1; fc[f][0] += c == top
        out[key] = {f: tuple(v) for f, v in fc.items()}
    return out

# ------------------------------------------------------------------ the round's questions
class Plan:
    def __init__(self, rid):
        self.rid, self.qs, self.keys = rid, [], set()
    def add(self, kind, ctx, cand=None, variant=None, probe=None, **src):
        """validity only (and one copy a round): nothing is refused for having been asked before"""
        ctx = list(ctx)
        distinct = variant == "reflection" or len(set(ctx)) == len(ctx)
        lo, hi = {"cohere": (3, PR.MAX_RUN), "order": (4, PR.MAX_ORDER), "names": (4, PR.MAX_ORDER),
                  "pick": (2, PR.MAX_RUN)}.get(kind, (2, MAXK))
        if not (lo <= len(ctx) <= hi) or not distinct or not all(PR.is_glyph(x) for x in ctx):
            return False
        if kind == "triad" and len(ctx) != 3:
            return False
        if kind == "names" and not all(U.name(x, None) for x in ctx):
            return False
        if kind == "inhibit" and (cand in ctx or not PR.is_glyph(cand)):
            return False
        if kind == "choose" and (len(set(cand)) != 2 or any(x in ctx or not PR.is_glyph(x) for x in cand)):
            return False
        key = (kind, tuple(ctx) if kind not in ("order", "names", "triad") else tuple(sorted(ctx)),
               cand if kind != "choose" else tuple(sorted(cand)), variant, tuple(sorted((probe or {}).items())))
        if key in self.keys:
            return False
        self.keys.add(key)
        self.qs.append(dict(PR.question(kind, ctx, cand, source=dict(src, round=self.rid), variant=variant, probe=probe),
                            **({"variant": variant} if variant else {}), **({"probe": probe} if probe else {})))
        return True
    def add_unit(self, unit):
        """a unit: [(kind, ctx, cand, variant, probe, src)]; its first question decides; controls follow it"""
        kind, ctx, cand, variant, probe, src = unit[0]
        if not self.add(kind, ctx, cand, variant=variant, probe=probe, **src):
            return 0
        n = 1
        for kind, ctx, cand, variant, probe, src in unit[1:]:
            n += self.add(kind, ctx, cand, variant=variant, probe=probe, **src)
        return n

def Q(kind, ctx, cand=None, variant=None, probe=None, **src):
    return (kind, list(ctx), cand, variant, probe, src)

class Cands:
    """candidate units of one stream, deduplicated by identity, keeping the highest weight"""
    def __init__(self):
        self.best = {}
    def put(self, ident, weight, unit):
        """unit: a list of questions, or a function making one (built only if drawn: controls, decoys, windows)"""
        if weight > 0 and (ident not in self.best or weight > self.best[ident][0]):
            self.best[ident] = (weight, unit)
    def __len__(self):
        return len(self.best)
    def draw(self, P, n, r):
        items = list(self.best.values())
        got = 0
        for w, unit in weighted_order(items, lambda it: it[0], r):
            if got >= n:
                break
            u = unit() if callable(unit) else unit
            if u:
                got += P.add_unit(u)
        return got

# ------------------------------------------------------------------ streams
def rel_of(s):
    return scurve(s["rank"])

def continue_cands(T, Tr, pend, seqs):
    """contexts along the tree's sequences, weighted by relevance x information at each context"""
    C = Cands()
    memo = {}
    def put(ctx, rel, why, **src):
        ctx = tuple(ctx)
        if not (2 <= len(ctx) <= MAXK) or len(set(ctx)) != len(ctx):
            return
        if ctx not in memo:
            memo[ctx] = info_fams(counts_top(Tr.nodes.get(ctx, {})), pend.get("continue", ctx))
        C.put(ctx, rel * memo[ctx], [Q("continue", ctx, why=why, **src)])
    for s in seqs:
        g, rel = s["glyphs"], rel_of(s)
        sq = "".join(g)
        for side, stop in (("right", s["stop_right"]), ("left", s["stop_left"])):
            run = g if side == "right" else g[::-1]
            if stop.startswith("wrap→"):
                x = stop.split("→", 1)[1]
                if x in run:
                    period = run[run.index(x):]
                    if len(set(period)) >= 4:                    # Joseph's scope: cycles of >= 4 distinct glyphs
                        k = max(2, math.ceil(len(period) / 2))
                        if k < len(period):
                            put(period[-k:], rel, "cycle-probe", seq=sq, period="".join(period))
                continue
            for k in range(2, min(MAXK, len(run)) + 1):
                put(run[-k:], rel * PARAMS["END_RELEVANCE"], "end", seq=sq, side=side, stop=stop.split("→")[0])
        pos = {x: i for i, x in enumerate(g)}
        for st in s["steps"]:
            ctx = st["ctx"]
            for j in range(2, len(ctx) + 1):                     # k*: every suffix, and the deciding context itself
                put(ctx[-j:], rel, "kstar" if j < len(ctx) else "replicate", seq=sq, step=st["x"])
            a, b = ctx[-1], st["x"]
            if a in pos and b in pos:
                path = g[:pos[a] + 1] if pos[b] > pos[a] else g[pos[a]:][::-1]
                for k in range(len(ctx) + 1, min(MAXK, len(path)) + 1):       # lengthening (§3)
                    put(path[-k:], rel, "lengthen", seq=sq, link=a + b, k=k)
        for run in (g, g[::-1]):              # contexts ending on interior glyphs, both ways (so every link from its far side)
            for i in range(1, len(run) - 1):
                for k in range(2, min(MAXK, i + 1) + 1):
                    put(run[i + 1 - k:i + 1], rel, "inside", seq=sq)
    return C

def inhibit_cands(T, Tr, pend, seqs, rid):
    """link recognition, each with its matched decoy"""
    C = Cands()
    def put(ctx, x, rel, why, **src):
        ctx = tuple(ctx)
        if not (2 <= len(ctx) <= MAXK) or len(set(ctx)) != len(ctx) or x in ctx or not PR.is_glyph(x):
            return
        w = rel * info_fams(counts_yes(Tr.inhibit.get((ctx, x), {})), pend.get("inhibit", (ctx, x)))
        def unit(ctx=ctx, x=x, why=why, src=src):
            ck = "near" if PR.R("control-kind", {"round": rid, "context": list(ctx), "x": x}).random() < 0.5 else "far"
            dec = PR.control_candidate(list(ctx), x, ck, rid)
            return [Q("inhibit", ctx, x, why=why, **src), Q("inhibit", ctx, dec, probe={"control": ck}, why="control", control=ck)]
        C.put((ctx, x), w, unit)
    for ctx, rows in T.reasoned.items():                          # the reasoned pass's candidates
        top = T.top(ctx)
        for x in dict.fromkeys(r["continuation"][0] for r in rows if r["continuation"]):
            if x != top:
                put(ctx, x, 1.0, "recognize", reasoned_by=sorted({r["mind"] for r in rows}))
    for s in seqs:
        g, rel = s["glyphs"], rel_of(s)
        sq = "".join(g)
        for side, stop in (("right", s["stop_right"]), ("left", s["stop_left"])):    # written momentum past an end
            if stop != "end":
                continue
            run = g if side == "right" else g[::-1]
            ctx = T.lookup(run)
            if not ctx:
                continue
            w = collections.Counter()
            for j in range(2, min(MAXK, len(run)) + 1):
                for xs in T.written.get(tuple(run[-j:]), {}).values():
                    w.update(xs)
            for x, n in w.items():
                put(ctx, x, rel * branch_weight(n, sum(w.values())), "recognize-written", seq=sq, written_answers=n)
        pos = {x: i for i, x in enumerate(g)}
        for st in s["steps"]:
            a, b = st["ctx"][-1], st["x"]
            if st["alt"] and st["alt"][0] not in (TR.NONE, TR.OTHER):     # the runner-up at a branch point
                put(st["ctx"], st["alt"][0], rel * scurve(st["alt"][1], BRANCH_MID, BRANCH_WIDTH, BRANCH_FLOOR), "branch", seq=sq, step=b)
            if a in pos and b in pos:                                       # skip test: strongest claims hardest
                ic = pos[b] + (pos[b] - pos[a])
                if 0 <= ic < len(g):
                    put(st["ctx"], g[ic], rel * scurve(st["agreement"]), "falsify-skip", seq=sq, link=a + b)
    return C

def cohere_cands(T, Tr, pend, seqs, written_seqs, seeds, rid, recs):
    """whole runs, each with its shuffled control (and sometimes a chart window); every run asked before is a candidate"""
    C = Cands()
    memo = {}
    stew = steward_seeds(seeds)
    def put(g, rel, how):
        for h in windows(g, PR.MAX_RUN):
            if not runlike(h):
                continue
            key = tuple(min(h, h[::-1]))
            if key not in memo:
                memo[key] = info_fams(counts_yes_run(Tr, h), pend.get("cohere", key))
            def unit(key=key, how=how):
                r = PR.R("cohere-orientation", {"round": rid, "run": list(key)})
                shown = list(key) if r.random() < 0.5 else list(key)[::-1]      # orientation fated, never by outcome
                ctl = PR.shuffled_control(shown, rid)
                if ctl is None:
                    return None
                u = [Q("cohere", shown, why="cohere", **{"from": how}),
                     Q("cohere", ctl, probe={"control": "shuffled"}, why="control", control="shuffled", of="".join(shown))]
                if PR.R("cohere-chart-draw", {"round": rid, "run": shown}).random() < PARAMS["CHART_CONTROL_SHARE"]:
                    ch = PR.chart_control(shown, rid)
                    if ch:
                        u.append(Q("cohere", ch, probe={"control": "chart"}, why="control", control="chart", of="".join(shown)))
                return u
            C.put(key, rel * memo[key], unit)
    for s in seqs:
        put(s["glyphs"], rel_of(s), "walk")
    for s in written_seqs:
        put(s["glyphs"], rel_of(s), "written")
    for g, sid in seed_list(seeds, ORDERED_SEEDS, rid, "cohere-seed-order"):
        put(g, PARAMS["STEWARD_RELEVANCE"] if tuple(g) in stew else 1.0, "seed:" + str(sid))
    for c, w in pick_branches(T):
        put(c, w, "pick-branch")
    for run, fc in T.cohere_ctl.items():                            # shuffles some mind called coherent
        if T.cohere_ctl_class.get(run) == "shuffled":
            y = sum(c["yes"] for c in fc.values()); n = sum(sum(c.values()) for c in fc.values())
            put(list(run), scurve(y / n if n else 0), "reordered")
    for f in sorted((DATA / "triad-era" / "growth").glob("r0*.json")):     # the triad era's grown rows (CATALOG §3)
        for row in json.load(open(f)):
            put(row["glyphs"], 1.0, "grown:" + f.stem)
    for run in T.cohere:                                                   # every run asked before
        put(list(run), 1.0, "asked")
    return C

def counts_yes_run(Tr, g):
    return Tr.coherence(list(g))

def lookalike_cands(T, Tr, recs, rid):
    """a run some mind called coherent, strictly monotone in code points: one interior glyph swapped for a confusable
    from another block, with its fated non-confusable control (CATALOG v5 §7b); weighted by how strongly the run is
    recognised and by information on its lookalike answers so far"""
    C = Cands()
    la_counts = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
    for r in recs:
        t = r.get("tags") or {}
        if r["kind"] == "cohere" and t.get("control") == "lookalike" and r.get("outcome") in ("yes", "no", "cant-tell"):
            la_counts[t.get("of")][r["family"]][r["outcome"]] += 1
    for run, fc in T.cohere.items():
        y = sum(c["yes"] for c in fc.values()); n = sum(sum(c.values()) for c in fc.values())
        d = [ord(b) - ord(a) for a, b in zip(run, run[1:])]
        if not n or len(run) < 3 or not (all(x > 0 for x in d) or all(x < 0 for x in d)):
            continue
        g = list(run)
        r = PR.R("lookalike", {"run": g, "round": rid})
        opts = [(i, c) for i in range(1, len(g) - 1) for c in confusables(g[i])
                if c not in g and PR.is_glyph(c) and U.category(c) != "Cn" and block(c) != block(g[i])]
        if not opts:
            continue
        i, c = opts[r.randrange(len(opts))]
        bn = block(c)
        lo, hi = next((a, b) for a, b, nm in _BLOCKS if nm == bn)
        near = set(confusables(g[i])) | set(confusables(c)) | {g[i], c}
        pool = [chr(o) for o in range(lo, hi + 1) if PR.is_glyph(chr(o)) and U.category(chr(o)) != "Cn"
                and chr(o) not in near and chr(o) not in g]
        if not pool:
            continue
        dd = pool[r.randrange(len(pool))]
        la, ct = g[:i] + [c] + g[i + 1:], g[:i] + [dd] + g[i + 1:]
        of = "".join(g)
        w = scurve(y / n) * info_fams(counts_yes(la_counts.get(of, {})))
        C.put(of, w, [Q("cohere", la, probe={"control": "lookalike", "of": of, "pos": i, "orig": g[i]}, why="lookalike", control="lookalike", of=of),
                      Q("cohere", ct, probe={"control": "lookalike-ctl", "of": of, "pos": i, "orig": g[i]}, why="lookalike", control="lookalike-ctl", of=of)])
    return C

def choose_cands(T, Tr, pend, seqs, seeds, rid):
    """discriminator positions: steps of runs where the chart's next glyph differs from the run's, and contexts whose
    answers split between a chart-adjacent and a non-adjacent glyph; uncontested ones at lower relevance"""
    C = Cands()
    def put(ctx, x, ch, rel, how):
        ctx = tuple(ctx[-MAXK:])
        if len(ctx) < 2 or x in ctx or ch in ctx or x == ch:
            return
        con = contested(ch, ctx[-1])
        pair = frozenset((x, ch))
        fc = Tr.choose.get((ctx, pair), {})
        cnt = {f: (c.get(x, 0), sum(c.values())) for f, c in fc.items()}
        w = rel * info_fams(cnt, pend.get("choose", (ctx, pair)))
        C.put((ctx, pair), w, [Q("choose", ctx, (x, ch), probe={"chart": ch, "contested": con}, why="choose", **{"from": how})])
    def adjacent(x, ctx):
        return abs(ord(x) - ord(ctx[-1])) == 1
    for store in (T.picks, T.nodes):
        for ctx, fl in store.items():
            if not (2 <= len(ctx) <= MAXK):
                continue
            cnt = collections.Counter(x for xs in fl.values() for x in xs if x not in (TR.NONE, TR.OTHER) and x not in ctx and PR.is_glyph(x))
            ch = [x for x, _ in cnt.most_common() if adjacent(x, ctx)]
            al = [x for x, _ in cnt.most_common() if not adjacent(x, ctx)]
            if ch and al:
                put(ctx, al[0], ch[0], 1.0, "split")
    stew = steward_seeds(seeds)
    runs = [(g, PARAMS["STEWARD_RELEVANCE"] if tuple(g) in stew else 1.0) for g, _ in seed_list(seeds, ORDERED_SEEDS, rid, "choose-seed-order")]
    runs += [(list(r), 1.0) for r in T.cohere] + [(s["glyphs"], rel_of(s)) for s in seqs]
    for g, rel in runs:
        for i in range(1, len(g) - 1):
            ch = chart_neighbour(g[i - 1], g[i])
            if ch:
                put(g[:i + 1], g[i + 1], ch, rel, "step")
    return C

def choose_control_cands(T, Tr, pend, rid):
    C = Cands()
    pairs = {}
    for (ctx, pair), ch in T.choose_chart.items():
        pairs[pair] = ch
    for pair in T.choose_ctl:
        pairs.setdefault(pair, None)
    for pair, ch in pairs.items():
        x, y = sorted(pair)
        fc = Tr.choose_ctl.get(pair, {})
        cnt = {f: (c.get(x, 0), sum(c.values())) for f, c in fc.items()}
        w = info_fams(cnt, pend.get("choose-control", pair))
        r = PR.R("choose-neutral", {"pair": [x, y], "round": rid})
        avoid = {block(x), block(y)}
        ctx = []
        while len(ctx) < 3:
            g = fresh_glyph(r)
            if g not in pair and g not in ctx and block(g) not in avoid:
                ctx.append(g)
        C.put(pair, w, [Q("choose", ctx, (x, y), probe={"control": "neutral", "chart": ch}, why="choose-control", **{"from": "neutral"})])
    return C

def set_cands(kind, T, pend, counts, seqs, seeds, rid, extra=()):
    """sets for the order and name-only questions: seeds, runs some mind called coherent, walks, (names: the
    validation sets), and every set asked before; windows of longer runs"""
    C = Cands()
    stew = steward_seeds(seeds)
    def put(g, rel, how):
        for h in windows(g, PR.MAX_ORDER):
            if not runlike(h, 4, PR.MAX_ORDER) or (kind == "names" and not all(U.name(c, None) for c in h)):
                continue
            key = frozenset(h)
            w = rel * info_fams(counts.get(key, {}), pend.get(kind, key))
            C.put(key, w, [Q(kind, h, why=kind, **{"from": how})])
    for g, how, rel in extra:
        put(g, rel, how)
    types = ORDERED_SEEDS | (ORDER_ONLY_SEEDS if kind == "order" else set())
    for g, sid in seed_list(seeds, types, rid, kind + "-seed-order"):
        put(g, PARAMS["STEWARD_RELEVANCE"] if tuple(g) in stew else 1.0, "seed:" + str(sid))
    for run, fc in T.cohere.items():
        y = sum(c["yes"] for c in fc.values()); n = sum(sum(c.values()) for c in fc.values())
        put(list(run), scurve(y / n if n else 0), "run")
    for s in seqs:
        put(s["glyphs"], rel_of(s), "walk")
    for key in counts:
        put(sorted(key), 1.0, "asked")
    return C

def triad_cands(T, pend, seqs):
    C = Cands()
    def put(t, rel, how, **src):
        if len(set(t)) != 3 or not all(PR.is_glyph(c) for c in t):
            return
        key = tuple(sorted(t))
        fam = T.triads_fam.get(key, {})
        pooled = collections.Counter(a for c in fam.values() for a, n in c.items() for _ in range(n))
        top = pooled.most_common(1)[0][0] if pooled else None
        cnt = {f: (c.get(top, 0), sum(c.values())) for f, c in fam.items()}
        C.put(key, rel * info_fams(cnt, pend.get("triad", key)), [Q("triad", list(t), why="triad", **{"from": how}, **src)])
    for s in seqs:
        g = s["glyphs"]
        for i in range(len(g) - 2):
            put(g[i:i + 3], rel_of(s), "walk", seq="".join(g), mid=g[i + 1])
    for key in T.triads_fam:
        put(list(key), 1.0, "asked")
    return C

def pick_branches(T):
    """every branch the picks have grown so far: for each picked context c, every answer x -> [(c + [x], weight)]"""
    out = []
    for ctx in T.picks:
        b = T.pick_branches(ctx)
        n = sum(b.values())
        for x, k in b.items():
            if x not in (TR.NONE, TR.OTHER) and x not in ctx and PR.is_glyph(x):
                out.append((list(ctx) + [x], branch_weight(k, n)))
    return out

def pick_cands(T, pend, seqs, seeds, rid):
    """the generator's contexts: known sequences both ways (roots), every branch grown so far (children), and every
    context picked before; SAMPLES questions each (one per sample, each its own sheet)"""
    C = Cands()
    stew = steward_seeds(seeds)
    def put(ctx, rel, how):
        ctx = list(ctx)[-PR.MAX_RUN:]
        if not runlike(ctx, 2):
            return
        w = rel * info_fams(counts_top(T.picks.get(tuple(ctx), {})), pend.get("pick", tuple(ctx)))
        C.put(tuple(ctx), w, [Q("pick", ctx, probe={"sample": k}, why="pick", **{"from": how}) for k in range(PR.SAMPLES)])
    for g, _ in seed_list(seeds, ORDERED_SEEDS, rid, "pick-seed-order"):
        rel = PARAMS["STEWARD_RELEVANCE"] if tuple(g) in stew else 1.0
        put(g, rel, "root"); put(g[::-1], rel, "root")
    for s in seqs:
        put(s["glyphs"], rel_of(s), "root"); put(s["glyphs"][::-1], rel_of(s), "root")
    for c, w in pick_branches(T):
        put(c, w, "branch")
    for ctx in T.picks:
        put(ctx, 1.0, "asked")
    return C

def pick_nulls(P, n_questions, rid):
    """fresh random contexts, asked like picks: the null (lengths drawn from this round's pick contexts)"""
    lens = [len(q["context"]) for q in P.qs if q["kind"] == "pick" and not (q.get("probe") or {}).get("null")] or [3]
    r = PR.R("pick-null", {"round": rid})
    got = 0
    while got < n_questions:
        L = r.choice(lens)
        null = []
        while len(null) < L:
            c = fresh_glyph(r)
            if c not in null:
                null.append(c)
        for k in range(PR.SAMPLES):
            got += P.add("pick", null, probe={"sample": k, "null": True}, why="pick-null")
    return got

def reasoned_cands(T, pend, seqs, rid):
    C = Cands()
    for s in seqs:
        g = s["glyphs"]
        for side, stop in (("right", s["stop_right"]), ("left", s["stop_left"])):
            if stop != "end":
                continue
            run = g if side == "right" else g[::-1]
            for k in range(3, min(MAXK, len(run)) + 1):
                ctx = tuple(run[-k:])
                n = len(T.reasoned.get(ctx, []))
                w = rel_of(s) * info(0, n + sum(pend.get("reasoned", ctx).values()))
                C.put(ctx, w, [Q("continue", ctx, variant="reasoned", why="reasoned", seq="".join(g), side=side)])
    return C

def reflection_cands(T, pend, seqs, rid):
    C = Cands()
    for s in seqs:
        g = s["glyphs"]
        if len(g) < 4:
            continue
        for i in range(2, len(g) - 1):
            for k in (2, 3):
                ctx = tuple(g[max(0, i - k):i + 1] + [g[i - 1]])
                rows = T.reflections.get(ctx, [])
                kk = sum(1 for x in rows if x["continuation"][:1] == [g[i - 2]])
                w = rel_of(s) * info(kk, len(rows) + sum(pend.get("reflection", ctx).values()))
                C.put(ctx, w, [Q("continue", ctx, variant="reflection", why="reflection", seq="".join(g), mirror=g[i - 2])])
    return C

# ------------------------------------------------------------------ exploration (fresh contexts)
def triad_kernels(T):
    """§4: a triad answer is an unconditioned hint that a 3-glyph path exists. Per triad, its most-named middle m: the
    path a m c, if the tree has not been shown it. Weight: the estimated agreement on m (soft, never a cut)."""
    out = []
    for t, fam in T.triads_fam.items():
        mids = collections.Counter(ans[1] for c in fam.values() for ans, n in c.items() for _ in range(n) if ans[0] == "mid")
        if not mids:
            continue
        m = mids.most_common(1)[0][0]
        a, c = [x for x in t if x != m]
        if tuple([a, m]) in T.real or tuple([c, m]) in T.real:
            continue
        _, mean, _, _ = TR.estimate([{f: (cnt[("mid", m)], sum(cnt.values())) for f, cnt in fam.items()}])
        out.append((a, m, c, mean))
    return out

def explore(P, T, seqs, seeds, n, rid):
    """2-glyph contexts no mind has been shown, in thirds by a fated draw: seed bumps, fresh glyphs (with their
    code-point neighbour or another fresh glyph), and triad-agreed kernels weighted by their middle's agreement.
    A glyph already in a top sequence is redrawn with probability 1/2 (soft)."""
    r = PR.R("explore", {"round": rid})
    kernels = triad_kernels(T)
    settled = set()
    for s in seqs[:200]:
        if s["rank"] >= 0.9:
            settled.update(s["glyphs"])
    sd = [x for x in seeds if isinstance(x.get("glyphs"), list) and len(list(dict.fromkeys(x["glyphs"]))) >= 3]
    weights = [x.get("bump", 1.0) for x in sd]
    tries = added = 0
    while added < n and tries < n * 50:
        tries += 1
        u = r.random()
        if kernels and u < 1 / 3:
            a_, m_, c_ = r.choices(kernels, weights=[max(k[3], 1e-6) for k in kernels])[0][:3]
            ctx = [a_, m_] if r.random() < 0.5 else [c_, m_]
            how = {"why": "explore", "how": "triad-kernel"}
        elif sd and (u < 2 / 3 if kernels else u < 0.5):
            x = r.choices(sd, weights=weights)[0]
            gl = list(dict.fromkeys(x["glyphs"]))
            i = r.randrange(len(gl) - 1)
            ctx = gl[i:i + 2] if r.random() < 0.5 else gl[i:i + 2][::-1]
            how = {"why": "explore", "how": "seed", "seed": x.get("sid")}
        else:
            a = fresh_glyph(r)
            if a in settled and r.random() < 0.5:
                continue
            if r.random() < 0.5:
                b = chr(ord(a) + r.choice((-1, 1)))
                if not PR.is_glyph(b) or U.category(b) == "Cn":
                    continue
                how = {"why": "explore", "how": "codepoint-neighbour"}
            else:
                b = fresh_glyph(r)
                how = {"why": "explore", "how": "fresh"}
            ctx = [a, b]
        if tuple(ctx) in T.real:
            continue                                     # exploration is of contexts no mind has been shown
        if P.add("continue", ctx, **how):
            added += 1
    return added

# ------------------------------------------------------------------ the round
def sizes(budget, rid):
    r = PR.R("round-size", {"round": rid})
    scale = math.exp(r.gauss(0, PARAMS["SIZE_SIGMA_ROUND"]))
    out = {}
    for k, base in BASE.items():
        m = math.exp(r.gauss(0, PARAMS["SIZE_SIGMA_STREAM"]))
        out[k] = max(1, round(base * (budget / 700) * scale * m))
    return out, scale

def plan(rid, recs, seeds, budget):
    T = TR.Tree(recs)                                   # with seed votes: the walks seeds make walkable
    Tr = TR.Tree(recs, seeds=False)                     # real answers only: what information is computed from
    seqs = TR.sequences(T)
    written_seqs = TR.sequences(TR.Tree(recs, written=True))
    pend = Pending(recs, rid)
    want, scale = sizes(budget, rid)
    P = Plan(rid)
    got, pool = {}, {}
    got["explore"] = explore(P, T, seqs, seeds, want["explore"], rid)
    streams = [
        ("reasoned", lambda: reasoned_cands(T, pend, seqs, rid)),
        ("reflection", lambda: reflection_cands(T, pend, seqs, rid)),
        ("continue", lambda: continue_cands(T, Tr, pend, seqs)),
        ("inhibit", lambda: inhibit_cands(T, Tr, pend, seqs, rid)),
        ("cohere", lambda: cohere_cands(T, Tr, pend, seqs, written_seqs, seeds, rid, recs)),
        ("lookalike", lambda: lookalike_cands(T, Tr, recs, rid)),
        ("choose", lambda: choose_cands(T, Tr, pend, seqs, seeds, rid)),
        ("choose-control", lambda: choose_control_cands(T, Tr, pend, rid)),
        ("names", lambda: set_cands("names", T, pend, names_counts(T), seqs, seeds, rid,
                                    extra=[(list(g), "validation-" + grp, PARAMS["VALIDATION_RELEVANCE"])
                                           for grp, gs in NAME_VALIDATION.items() for g in gs])),
        ("order", lambda: set_cands("order", T, pend, order_counts(T), seqs, seeds, rid)),
        ("triad", lambda: triad_cands(T, pend, seqs)),
        ("pick", lambda: pick_cands(T, pend, seqs, seeds, rid)),
    ]
    for name, make in streams:
        C = make()
        pool[name] = len(C)
        got[name] = C.draw(P, want[name], PR.R("draw-" + name, {"round": rid}))
    got["pick-null"] = pick_nulls(P, want["pick-null"], rid)
    asked_before = set()
    for rd in (DATA / "rounds").glob("c[0-9][0-9][0-9]"):
        if rd.name < rid and (rd / "questions.jsonl").exists():
            asked_before |= {json.loads(l)["qid"] for l in open(rd / "questions.jsonl") if l.strip()}
    stats = {"round": rid, "protocol": PR.PROTOCOL, "planner": "stochastic-1", "questions": len(P.qs), "budget": budget,
             "size_scale": round(scale, 4), "wanted": want, "drawn": got, "candidates": pool,
             "reasks": sum(1 for q in P.qs if q["qid"] in asked_before),
             "by_why": dict(collections.Counter(q["source"].get("why") for q in P.qs)),
             "by_kind": dict(collections.Counter(q["kind"] for q in P.qs)),
             "by_variant": dict(collections.Counter(q.get("variant") or "plain" for q in P.qs)),
             "sequences": len(seqs), "contexts_in_tree": len(T.nodes), "params": PARAMS}
    return P.qs, stats
