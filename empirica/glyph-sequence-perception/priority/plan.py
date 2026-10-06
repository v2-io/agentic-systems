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
           SIZE_SIGMA_ROUND, SIZE_SIGMA_STREAM). Exploration is EXPLORE_SHARE of the round, the pick nulls one context
           per PICK_NULL_EVERY picked. So neither the round nor any share is the same twice.
  Weight   every candidate UNIT (a question, or a question with its controls) gets
               weight = relevance x information
           INFORMATION is the expected information (nats) that one more answer from each family adds about the
           quantity the question measures, summed over the families that answer it: for a share with k of n
           answers, a Beta(k + 1/2, n - k + 1/2) posterior (Jeffreys), the mutual information between the next
           answer and the share,
               I(k, n) = h(m) + m (psi(a + 1) - psi(a + b + 1)) + (1 - m) (psi(b + 1) - psi(a + b + 1)),   m = a / (a + b)
           -- 0.307 nats unasked, about 1 / (2n) once n answers agree. Never zero: the most settled item is re-asked,
           exceedingly rarely. It falls mostly with n; agreement moves it by at most about 30% (audit finding 3: what
           "most clarifying" should mean beyond a share's precision is Joseph's to decide). Answers ASKED BUT NOT YET
           GIVEN (the drains lag) count as expected answers within PENDING_HORIZON rounds, so the planner does not
           re-ask what a slow family has not reached yet; a family whose core minds are all paused until a quota resets
           (data/logs/paused.json) has its term left out.
           RELEVANCE is how much the quantity bears on a sequence: an S-curve with a floor (scurve) on the strength
           of the sequence it serves (the mean agreement of its walked links, not their number, so a new 3-glyph kernel
           isn't put last), so "the most obvious and stable (empirically) sequences" are squared away first (Joseph,
           2026-10-05) and nothing falls to zero.
           A source with no strength of its own gets UNRANKED_RELEVANCE, the curve's midpoint.
  Draw     in two stages (Cands.draw): CLAIM SLOTS -- what a unit's answer bears on: a sequence, a run, a position --
           drawn with replacement, each in proportion to its claim's mean unit weight; each slot takes the claim's next
           unit (its units in a fated weighted order, Efraimidis-Spirakis keys u^(1/w)). A heavy claim gets several
           questions a round, a long one no more than a short one of the same weight. Anything asked before that serves
           no current sequence, run or seed is its own claim at OFF_SEQUENCE_RELEVANCE: reachable, rarely, item by
           item. Validity refuses a continue or pick context showing a whole period of a manifested cycle.
The numbers are in PARAMS, BASE and BRANCH_*, all recorded in each round's plan.json, chosen without evidence unless
they say otherwise; explore()'s own soft numbers (the top 200 sequences, rank 0.9, redraw one in two, thirds) are not.
Planner "stochastic-2" (2026-10-06) follows a de novo audit of "stochastic-1" (audits/planner-stochastic-2026-10-06.md);
"stochastic-3" follows the auditor's check of stochastic-2 (audits/planner-stochastic-2-check-2026-10-06.md).

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
BASE = {                                                     # questions a round per stream: the c096-c100 means, drawn by
    "continue": 167, "inhibit": 74, "cohere": 176, "lookalike": 40, "choose": 60,   # the planner this one replaced (an
    "choose-control": 20, "names": 30, "order": 13, "triad": 15, "pick": 150,     # inherited allocation, to revisit);
    "reasoned": 20, "reflection": 20}                         # exploration is EXPLORE_SHARE of the round, the pick nulls
                                                              # one context per PICK_NULL_EVERY picked
PARAMS = {                                                   # every one chosen without evidence
    "SIZE_SIGMA_ROUND": 0.15,      # lognormal sigma of the round-wide size factor
    "SIZE_SIGMA_STREAM": 0.25,     # lognormal sigma of each stream's own size factor
    "REL_FLOOR": 0.05, "REL_MID": 0.5, "REL_WIDTH": 0.12,   # relevance S-curve on a sequence's rank (tree rank, 0-1)
    "END_RELEVANCE": 5.0,          # a context at a sequence's end: only there can a question extend it (Joseph's rule,
                                   # "extend that sequence to the right and to the left as far as they will go")
    "VALIDATION_RELEVANCE": 3.0,   # the name-only question's validation sets
    "STEWARD_RELEVANCE": 3.0,      # Joseph's own seeds
    "UNRANKED_RELEVANCE": 0.5,     # a source with no strength of its own (the triad era's grown rows, other seeds, runs
                                   # asked whole before, choose splits): the S-curve's midpoint, not its ceiling (audit
                                   # finding 2: at 1.0 such sources out-drew the tree's own walks)
    "OFF_SEQUENCE_RELEVANCE": 0.01,  # an item asked before that serves no current sequence, run or seed (a context, an
                                   # inhibit pair, a triad, a set, a pick context), each its own claim: in the check's
                                   # estimate about 2% of continue draws (0.05 gave about 10%). Chosen in the open, so the
                                   # long tail reaches individual items (Joseph: "the most improbably things to sneak in")
    "CHART_CONTROL_SHARE": 0.25,   # cohere runs that also get a chart window (a measurement, not a decoy)
    "PICK_NULL_EVERY": 4,          # one null context per this many real pick contexts (sizes the pick-null base)
    "MAX_WINDOW_STEP": 0.5,        # windows of long runs overlap by half a window
    "PENDING_HORIZON": 12,         # rounds back in which unanswered sheets still count as answers on their way (about
                                   # 3 hours of rounds; the drains go newest first)
    "EXPLORE_SHARE": 0.15,         # exploration's share of a round, before jitter (Joseph: "15% of our effort was always
                                   # 'hot'"; until 2026-10-06 a base of 105, 11% of the round)
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
CANARY = set("▁▂▃▄▅▆▇█🮆🮅🮄▀🮃🮂▔▉")                                   # audits/SEAL-canary-choose-2026-10-06.md

def blind(cnt, glyphs):
    """the seal: a choose or name-only question touching a canary glyph is weighted by how many answers it has, never by
    what they say (k = n/2), so no sealed answer can steer what is asked (audit finding 7: the planner had weighted by
    them, a faint channel into the committed questions.jsonl)"""
    if CANARY & set(glyphs):
        return {f: (n / 2, n) for f, (k, n) in cnt.items()}
    return cnt

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

ACTIVE = set(FAMS)                  # the families able to answer the stream being drawn (plan() sets it per stream, from
                                    # the roster that answers it: core, generators or reasoners). A family whose minds
                                    # there are all paused until a quota resets can't, and its term is left out, not
                                    # counted as unasked (audit finding 5; per stream since the check of stochastic-2)

def info_fams(counts, pend=None):
    """summed over the core families able to answer: counts {family: (k, n)}; pend {family: answers asked but not yet
    given}, counted as answers at the family's current posterior mean"""
    tot = 0.0
    for f in FAMS:
        if f not in ACTIVE:
            continue
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
    A READING rule. The planner asks uncontested positions too, on equal terms: that is how the rule gets tested."""
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
def round_num(name):
    """c007 -> 7; anything else -> None (matched by number, so c1000 sorts after c999)"""
    return int(name[1:]) if len(name) > 1 and name[0] == "c" and name[1:].isdigit() else None

def ctx_round_dirs():
    return sorted((p for p in (DATA / "rounds").iterdir() if p.is_dir() and round_num(p.name) is not None),
                  key=lambda p: round_num(p.name))

def paused_minds():
    """minds paused until a quota resets (run.py writes data/logs/paused.json)"""
    import time
    try:
        return {m for m, t in json.load(open(DATA / "logs" / "paused.json")).items() if t > time.time()}
    except Exception:
        return set()

def pending(recs, rid):
    """answers asked but not yet given: for the PENDING_HORIZON context rounds before `rid` (void rounds excluded), each
    sheet entry x each mind assigned and not paused, less those with a record (a mind answered or gave up), matched by
    (round, sheet, question, mind). -> {qid: {family: count}}, {qid: question}.
    Audit 2026-10-06, finding 5: counted over every round, with the drains going newest first, about 1,000 Gemini
    answers a round for c006-c027 and c080-c091 were counted as on their way though they would likely never come;
    and matching by question alone let void rounds' records and re-ask variants subtract from live copies."""
    try:
        void = set(json.load(open(DATA / "rounds" / "VOID.json"))["rounds"])
    except FileNotFoundError:
        void = set()
    fam = {m: s.get("family") for m, s in json.load(open(ROOT / "core" / "minds.json"))["minds"].items()}
    paused = paused_minds()
    here = round_num(rid) if round_num(rid) is not None else 10 ** 9
    dirs = [rd for rd in ctx_round_dirs() if rd.name not in void and round_num(rd.name) < here
            and (rd / "sheets.jsonl").exists()][-PARAMS["PENDING_HORIZON"]:]
    keep = {rd.name for rd in dirs}
    answered = {(r["round"], r.get("sid"), r.get("qid"), r["mind"]) for r in recs if r.get("era") == "ctx" and r.get("round") in keep}
    asked = collections.defaultdict(collections.Counter)
    qs = {}
    for rd in dirs:
        for l in open(rd / "questions.jsonl"):
            if l.strip():
                q = json.loads(l); qs[q["qid"]] = q
        for l in open(rd / "sheets.jsonl"):
            if not l.strip():
                continue
            s = json.loads(l)
            for e in s["entries"]:
                for m in s.get("minds", []):
                    if m not in paused and (rd.name, s["sid"], e["qid"], m) not in answered:
                        asked[e["qid"]][fam.get(m)] += 1
    return {q: dict(c) for q, c in asked.items()}, qs

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

def order_counts(recs):
    """per shown set (frozenset), per family: (answers giving the set's modal outcome, answers) -- the order question,
    both eras, every answer: a main line (an answer's longest line, either direction one, ties as one step) or "none".
    (Until the 2026-10-06 audit, finding 6, this read the tree's `orders`, which holds lines only, so 453 sets answered
    only "none" stayed at the information ceiling for ever.)"""
    by = collections.defaultdict(list)
    for r in recs:
        if r["kind"] != "order" or r.get("outcome") not in ("lines", "none"):
            continue
        if r["outcome"] == "none":
            c = ("none",)
        else:
            lines = (r.get("answer") or {}).get("lines") or []
            main = max(lines, key=lambda ln: sum(len(st) for st in ln if st != "GAP")) if lines else []
            c = tuple("…" if st == "GAP" else "=".join(sorted(st)) for st in main)
            c = min(c, c[::-1])
        by[frozenset(r.get("shown") or r["context"])].append((r["family"], c))
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
    def __init__(self, rid, cycles=()):
        self.rid, self.qs, self.keys = rid, [], set()
        self.cycles = {tuple(c) for c in cycles}                 # canonical periods of manifested cycles, >= 4 distinct
        self.cycle_lens = sorted({len(c) for c in self.cycles})
    def spoils(self, ctx):
        """does the context show a whole period of a manifested cycle, in any rotation or direction? Then a continuation
        repeats what was shown and tests nothing (METHODOLOGY §4, no spoiling; check of stochastic-2: 38 such contexts
        reached the pool through other sequences that pass through a cycle's glyphs)"""
        for p in self.cycle_lens:
            for i in range(len(ctx) - p + 1):
                if TR.canon_cycle(list(ctx[i:i + p])) in self.cycles:
                    return True
        return False
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
        if kind in ("continue", "pick") and variant != "reflection" and self.spoils(ctx):
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
    """candidate units of one stream, deduplicated by identity (the highest weight kept), each belonging to a CLAIM --
    what its answer bears on: a sequence, a run, a position, or (for a unit that stands alone) itself.

    The draw is in two stages (planner audit 2026-10-06, finding 2): claims first, by a fated weighted draw on each
    claim's mean unit weight, then within each drawn claim its units by their own weights; and breadth first -- every
    drawn claim gives its best unit before any gives a second. Without it, a source's share of the draw followed how
    many candidates it enumerated (a long sequence's hundreds of contexts outweighed a short one's few), not how much
    its answers clarify: questions within one claim measure correlated things, so their information doesn't add."""
    def __init__(self):
        self.best = {}
    def put(self, ident, weight, unit, claim=None):
        """unit: a list of questions, or a function making one (built only if drawn: controls, decoys, windows)"""
        if weight > 0 and (ident not in self.best or weight > self.best[ident][0]):
            self.best[ident] = (weight, unit, ident if claim is None else claim)
    def __len__(self):
        return len(self.best)
    def claims(self):
        return len({c for _, _, c in self.best.values()})
    def draw(self, P, n, r):
        """claim SLOTS drawn with replacement, each with probability proportional to its claim's weight (the mean of its
        units' weights); each slot takes its claim's next unit (the units of a claim in a fated weighted order). A
        heavy claim gets several questions in a round in proportion to its weight; a long claim no more than a short
        one of the same weight. (Check of stochastic-2, 2026-10-06: drawn breadth first, about 170 draws over about
        1,300 claims gave every sequence at most one question a round.)"""
        by = collections.defaultdict(list)
        for w, unit, c in self.best.values():
            by[c].append((w, unit))
        claims = list(by)
        if not claims:
            return 0
        cw = [sum(w for w, _ in by[c]) / len(by[c]) for c in claims]
        queues = {}
        got = tries = 0
        while got < n and claims and tries < 20 * n + 100:
            tries += 1
            i = r.choices(range(len(claims)), weights=cw)[0]
            c = claims[i]
            if c not in queues:
                queues[c] = collections.deque(weighted_order(by[c], lambda it: it[0], r))
            q = queues[c]
            while q:
                w, unit = q.popleft()
                u = unit() if callable(unit) else unit
                if u:
                    k = P.add_unit(u)
                    if k:
                        got += k
                        break
            if not q:                                             # exhausted: the claim leaves the draw
                del claims[i]; del cw[i]
        return got

# ------------------------------------------------------------------ streams
def rel_of(s):
    """a sequence's relevance: the S-curve on the mean agreement of its walked links -- how strongly the links found so
    far are felt, not how many there are. (Until stochastic-3 it read the tree's rank, mean agreement x min(1, walked/4),
    which put newly found 3-glyph kernels last, against Joseph's "various minds start to find a sequence -- call it a
    sequence of three glyphs. The priority is then to extend that sequence to the right and to the left as far as they
    will go"; check of stochastic-2.)"""
    return scurve(s.get("mean_agreement", s["rank"]))


def continue_cands(T, Tr, pend, seqs):
    """contexts along the tree's sequences, each sequence one claim; and every context shown before, each off-sequence
    one its own claim at OFF_SEQUENCE_RELEVANCE (audit finding 4; pooled into one claim in stochastic-2, which made them
    unreachable in practice -- check of stochastic-2)"""
    C = Cands()
    memo = {}
    def put(ctx, rel, why, claim, **src):
        ctx = tuple(ctx)
        if not (2 <= len(ctx) <= MAXK) or len(set(ctx)) != len(ctx):
            return
        if ctx not in memo:
            memo[ctx] = info_fams(counts_top(Tr.nodes.get(ctx, {})), pend.get("continue", ctx))
        C.put(ctx, rel * memo[ctx], [Q("continue", ctx, why=why, **src)], claim)
    for s in seqs:
        g, rel = s["glyphs"], rel_of(s)
        sq = "".join(g)
        is_cycle = s["stop_right"].startswith("cycle") or s["stop_left"].startswith("cycle")
        for side, stop in (("right", s["stop_right"]), ("left", s["stop_left"])):
            run = g if side == "right" else g[::-1]
            if stop.startswith("wrap→") or is_cycle:     # a manifested cycle has no end on either side
                # a wrap, or a manifested cycle (tree.sequences relabels its wrap "cycle (manifested)", and until the
                # 2026-10-06 audit, finding 1, such stops fell through to the end questions below, at END_RELEVANCE,
                # 173 of them showing the whole period)
                x = stop.split("→", 1)[1] if stop.startswith("wrap→") else run[0]
                if x in run:
                    period = run[run.index(x):]
                    if len(set(period)) >= 4:                    # Joseph's scope: cycles of >= 4 distinct glyphs
                        k = max(2, math.ceil(len(period) / 2))
                        if k < len(period):
                            put(period[-k:], rel, "cycle-probe", sq, seq=sq, period="".join(period))
                continue
            for k in range(2, min(MAXK, len(run)) + 1):
                put(run[-k:], rel * PARAMS["END_RELEVANCE"], "end", sq, seq=sq, side=side, stop=stop.split("→")[0])
        pos = {x: i for i, x in enumerate(g)}
        for st in s["steps"]:
            ctx = st["ctx"]
            for j in range(2, len(ctx) + 1):                     # k*: every suffix, and the deciding context itself
                put(ctx[-j:], rel, "kstar" if j < len(ctx) else "replicate", sq, seq=sq, step=st["x"])
            a, b = ctx[-1], st["x"]
            if a in pos and b in pos:
                path = g[:pos[a] + 1] if pos[b] > pos[a] else g[pos[a]:][::-1]
                for k in range(len(ctx) + 1, min(MAXK, len(path)) + 1):       # lengthening (§3)
                    put(path[-k:], rel, "lengthen", sq, seq=sq, link=a + b, k=k)
        for run in (g, g[::-1]):              # contexts ending on interior glyphs, both ways (so every link from its far side)
            for i in range(1, len(run) - 1):
                for k in range(2, min(MAXK, i + 1) + 1):
                    put(run[i + 1 - k:i + 1], rel, "inside", sq, seq=sq)
    for ctx in Tr.real:                                          # every context shown before, so none is out of reach
        if ctx not in C.best:
            put(ctx, PARAMS["OFF_SEQUENCE_RELEVANCE"], "asked", ("asked", ctx))
    return C

def inhibit_cands(T, Tr, pend, seqs, rid):
    """link recognition, each with its matched decoy: each sequence one claim, each reasoned-pass context one, and every
    pair asked before, each off-sequence one its own claim at OFF_SEQUENCE_RELEVANCE (audit finding 4)"""
    C = Cands()
    def put(ctx, x, rel, why, claim, **src):
        ctx = tuple(ctx)
        if not (2 <= len(ctx) <= MAXK) or len(set(ctx)) != len(ctx) or x in ctx or not PR.is_glyph(x):
            return
        w = rel * info_fams(counts_yes(Tr.inhibit.get((ctx, x), {})), pend.get("inhibit", (ctx, x)))
        def unit(ctx=ctx, x=x, why=why, src=src):
            ck = "near" if PR.R("control-kind", {"round": rid, "context": list(ctx), "x": x}).random() < 0.5 else "far"
            dec = PR.control_candidate(list(ctx), x, ck, rid)
            return [Q("inhibit", ctx, x, why=why, **src), Q("inhibit", ctx, dec, probe={"control": ck}, why="control", control=ck)]
        C.put((ctx, x), w, unit, claim)
    for ctx, rows in T.reasoned.items():                          # the reasoned pass's candidates
        top = T.top(ctx)
        for x in dict.fromkeys(r["continuation"][0] for r in rows if r["continuation"]):
            if x != top:
                put(ctx, x, 1.0, "recognize", ("reasoned", ctx), reasoned_by=sorted({r["mind"] for r in rows}))
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
                put(ctx, x, rel * branch_weight(n, sum(w.values())), "recognize-written", sq, seq=sq, written_answers=n)
        pos = {x: i for i, x in enumerate(g)}
        for st in s["steps"]:
            a, b = st["ctx"][-1], st["x"]
            if st["alt"] and st["alt"][0] not in (TR.NONE, TR.OTHER):     # the runner-up at a branch point
                put(st["ctx"], st["alt"][0], rel * scurve(st["alt"][1], BRANCH_MID, BRANCH_WIDTH, BRANCH_FLOOR), "branch", sq, seq=sq, step=b)
            if a in pos and b in pos:                                       # skip test: strongest claims hardest
                ic = pos[b] + (pos[b] - pos[a])
                if 0 <= ic < len(g):
                    put(st["ctx"], g[ic], rel * scurve(st["agreement"]), "falsify-skip", sq, seq=sq, link=a + b)
    for (ctx, x) in Tr.inhibit:                                    # every pair asked before, so none is out of reach
        if (ctx, x) not in C.best:
            put(ctx, x, PARAMS["OFF_SEQUENCE_RELEVANCE"], "asked", ("asked", ctx, x))
    return C

def cohere_cands(T, Tr, pend, seqs, written_seqs, seeds, rid, recs):
    """whole runs, each with its shuffled control (and sometimes a chart window); every run asked before is a candidate"""
    C = Cands()
    memo = {}
    stew = steward_seeds(seeds)
    def put(g, rel, how, cyclic=False):
        ws = windows(g, PR.MAX_RUN)
        for h in ws:
            if not runlike(h):
                continue
            key = tuple(min(h, h[::-1]))
            if key not in memo:          # a cycle asked whole pools its rotations (audit, smaller things)
                memo[key] = info_fams(counts_yes_run(Tr, h, cyclic and len(ws) == 1), pend.get("cohere", key))
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
        put(g, PARAMS["STEWARD_RELEVANCE"] if tuple(g) in stew else PARAMS["UNRANKED_RELEVANCE"], "seed:" + str(sid))
    for c, w in pick_branches(T):
        put(c, w, "pick-branch")
    for run, fc in T.cohere_ctl.items():                            # shuffles some mind called coherent
        if T.cohere_ctl_class.get(run) == "shuffled":
            y = sum(c["yes"] for c in fc.values()); n = sum(sum(c.values()) for c in fc.values())
            put(list(run), scurve(y / n if n else 0), "reordered")
    for f in sorted((DATA / "triad-era" / "growth").glob("r0*.json")):     # the triad era's grown rows (CATALOG §3)
        for row in json.load(open(f)):
            put(row["glyphs"], PARAMS["UNRANKED_RELEVANCE"], "grown:" + f.stem, cyclic=bool(row.get("cyclic")))
    for run in T.cohere:                                                   # every run asked before
        put(list(run), PARAMS["UNRANKED_RELEVANCE"], "asked")
    return C

def counts_yes_run(Tr, g, cyclic=False):
    return Tr.coherence(list(g), cyclic)

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
    answers split between a chart-adjacent and a non-adjacent glyph. Uncontested positions on equal terms. A run's
    positions are one claim."""
    C = Cands()
    def put(ctx, x, ch, rel, how, claim):
        ctx = tuple(ctx[-MAXK:])
        if len(ctx) < 2 or x in ctx or ch in ctx or x == ch:
            return
        con = contested(ch, ctx[-1])
        pair = frozenset((x, ch))
        fc = Tr.choose.get((ctx, pair), {})
        cnt = blind({f: (c.get(x, 0), sum(c.values())) for f, c in fc.items()}, ctx + (x, ch))
        w = rel * info_fams(cnt, pend.get("choose", (ctx, pair)))
        C.put((ctx, pair), w, [Q("choose", ctx, (x, ch), probe={"chart": ch, "contested": con}, why="choose", **{"from": how})], claim)
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
                put(ctx, al[0], ch[0], PARAMS["UNRANKED_RELEVANCE"], "split", ("split", ctx))
    stew = steward_seeds(seeds)
    U_ = PARAMS["UNRANKED_RELEVANCE"]
    runs = [(g, PARAMS["STEWARD_RELEVANCE"] if tuple(g) in stew else U_) for g, _ in seed_list(seeds, ORDERED_SEEDS, rid, "choose-seed-order")]
    runs += [(list(r), U_) for r in T.cohere] + [(s["glyphs"], rel_of(s)) for s in seqs]
    for g, rel in runs:
        claim = tuple(min(g, g[::-1]))
        for i in range(1, len(g) - 1):
            ch = chart_neighbour(g[i - 1], g[i])
            if ch:
                put(g[:i + 1], g[i + 1], ch, rel, "step", claim)
    return C

def choose_control_cands(T, Tr, pend, rid):
    """D controls: each pair after a fresh neutral context (no canary glyph in it, so no new sealed answers). A pair once
    asked after a neutral context holding a canary glyph is weighted by n alone (check of stochastic-2: 1 of 173 had
    one), found from the questions asked, never from answers."""
    C = Cands()
    tainted = set()
    for rd in ctx_round_dirs():
        if (rd / "questions.jsonl").exists():
            for l in open(rd / "questions.jsonl"):
                if '"neutral"' in l:
                    q = json.loads(l)
                    if q["kind"] == "choose" and (q.get("probe") or {}).get("control") == "neutral" and CANARY & set(q["context"]):
                        tainted.add(frozenset(q.get("pair") or ()))
    pairs = {}
    for (ctx, pair), ch in T.choose_chart.items():
        pairs[pair] = ch
    for pair in T.choose_ctl:
        pairs.setdefault(pair, None)
    for pair, ch in pairs.items():
        x, y = sorted(pair)
        fc = Tr.choose_ctl.get(pair, {})
        cnt = {f: (c.get(x, 0), sum(c.values())) for f, c in fc.items()}
        cnt = blind(cnt, (x, y) + (tuple(CANARY) if pair in tainted else ()))   # pooled over a sealed neutral context
        w = info_fams(cnt, pend.get("choose-control", pair))
        r = PR.R("choose-neutral", {"pair": [x, y], "round": rid})
        avoid = {block(x), block(y)}
        ctx = []
        while len(ctx) < 3:
            g = fresh_glyph(r)
            if g not in pair and g not in ctx and block(g) not in avoid and g not in CANARY:   # no new sealed answers
                ctx.append(g)
        C.put(pair, w, [Q("choose", ctx, (x, y), probe={"control": "neutral", "chart": ch}, why="choose-control", **{"from": "neutral"})])
    return C

def set_cands(kind, T, pend, counts, seqs, seeds, rid, extra=()):
    """sets for the order and name-only questions: seeds, runs some mind called coherent, walks, (names: the
    validation sets), and every set asked before; windows of longer runs"""
    C = Cands()
    stew = steward_seeds(seeds)
    def put(g, rel, how):
        claim = tuple(min(list(g), list(g)[::-1]))                 # a long run's windows are one claim
        for h in windows(g, PR.MAX_ORDER):
            if not runlike(h, 4, PR.MAX_ORDER) or (kind == "names" and not all(U.name(c, None) for c in h)):
                continue
            key = frozenset(h)
            cnt = counts.get(key, {})
            w = rel * info_fams(blind(cnt, h) if kind == "names" else cnt, pend.get(kind, key))
            C.put(key, w, [Q(kind, h, why=kind, **{"from": how})], claim)
    for g, how, rel in extra:
        put(g, rel, how)
    types = ORDERED_SEEDS | (ORDER_ONLY_SEEDS if kind == "order" else set())
    for g, sid in seed_list(seeds, types, rid, kind + "-seed-order"):
        put(g, PARAMS["STEWARD_RELEVANCE"] if tuple(g) in stew else PARAMS["UNRANKED_RELEVANCE"], "seed:" + str(sid))
    for run, fc in T.cohere.items():
        y = sum(c["yes"] for c in fc.values()); n = sum(sum(c.values()) for c in fc.values())
        put(list(run), scurve(y / n if n else 0), "run")
    for s in seqs:
        put(s["glyphs"], rel_of(s), "walk")
    for key in counts:
        put(sorted(key), PARAMS["OFF_SEQUENCE_RELEVANCE"], "asked")
    return C

def triad_cands(T, pend, seqs):
    C = Cands()
    def put(t, rel, how, claim=None, **src):
        if len(set(t)) != 3 or not all(PR.is_glyph(c) for c in t):
            return
        key = tuple(sorted(t))
        fam = T.triads_fam.get(key, {})
        pooled = collections.Counter(a for c in fam.values() for a, n in c.items() for _ in range(n))
        top = pooled.most_common(1)[0][0] if pooled else None
        cnt = {f: (c.get(top, 0), sum(c.values())) for f, c in fam.items()}
        C.put(key, rel * info_fams(cnt, pend.get("triad", key)), [Q("triad", list(t), why="triad", **{"from": how}, **src)], claim)
    for s in seqs:
        g = s["glyphs"]
        for i in range(len(g) - 2):
            put(g[i:i + 3], rel_of(s), "walk", "".join(g), seq="".join(g), mid=g[i + 1])
    for key in T.triads_fam:
        put(list(key), PARAMS["OFF_SEQUENCE_RELEVANCE"], "asked")
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
    def put(ctx, rel, how, claim=None):
        ctx = list(ctx)[-PR.MAX_RUN:]
        if not runlike(ctx, 2):
            return
        w = rel * info_fams(counts_top(T.picks.get(tuple(ctx), {})), pend.get("pick", tuple(ctx)))
        C.put(tuple(ctx), w, [Q("pick", ctx, probe={"sample": k}, why="pick", **{"from": how}) for k in range(PR.SAMPLES)], claim)
    for g, _ in seed_list(seeds, ORDERED_SEEDS, rid, "pick-seed-order"):
        rel = PARAMS["STEWARD_RELEVANCE"] if tuple(g) in stew else PARAMS["UNRANKED_RELEVANCE"]
        cl = tuple(min(g, g[::-1]))                                  # a sequence's two directions are one claim
        put(g, rel, "root", cl); put(g[::-1], rel, "root", cl)
    for s in seqs:
        cl = tuple(min(s["glyphs"], s["glyphs"][::-1]))
        put(s["glyphs"], rel_of(s), "root", cl); put(s["glyphs"][::-1], rel_of(s), "root", cl)
    for c, w in pick_branches(T):
        put(c, w, "branch")
    for ctx in T.picks:
        put(ctx, PARAMS["OFF_SEQUENCE_RELEVANCE"], "asked")
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
    """`a b c b -> ?` at every glyph of a sequence from its third on, both orientations -- including the sequence's own
    end, where METHODOLOGY §3 asks whether an end reflects (a line) or wraps (a cycle) (until the 2026-10-06 audit,
    finding 4, only interior glyphs in one orientation)"""
    C = Cands()
    for s in seqs:
        if len(s["glyphs"]) < 4:
            continue
        cl = tuple(min(s["glyphs"], s["glyphs"][::-1]))
        for g in (s["glyphs"], s["glyphs"][::-1]):
            for i in range(2, len(g)):
                for k in (2, 3):
                    ctx = tuple(g[max(0, i - k):i + 1] + [g[i - 1]])
                    rows = T.reflections.get(ctx, [])
                    kk = sum(1 for x in rows if x["continuation"][:1] == [g[i - 2]])
                    w = rel_of(s) * info(kk, len(rows) + sum(pend.get("reflection", ctx).values()))
                    C.put(ctx, w, [Q("continue", ctx, variant="reflection", why="reflection", seq="".join(g), mirror=g[i - 2])], cl)
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
    """this round's size of each stream: base x (budget / 700) x a round-wide and a per-stream lognormal factor; the
    exploration base is EXPLORE_SHARE of the round (budget is a scale, not a count)"""
    r = PR.R("round-size", {"round": rid})
    scale = math.exp(r.gauss(0, PARAMS["SIZE_SIGMA_ROUND"]))
    out = {}
    for k, base in BASE.items():
        m = math.exp(r.gauss(0, PARAMS["SIZE_SIGMA_STREAM"]))
        out[k] = max(1, round(base * (budget / 700) * scale * m))
    rest = sum(BASE.values()) * (budget / 700) * scale
    m = math.exp(r.gauss(0, PARAMS["SIZE_SIGMA_STREAM"]))
    out["explore"] = max(1, round(rest * PARAMS["EXPLORE_SHARE"] / (1 - PARAMS["EXPLORE_SHARE"]) * m))
    return out, scale

def plan(rid, recs, seeds, budget):
    global ACTIVE
    reg = json.load(open(ROOT / "core" / "minds.json"))
    paused = paused_minds()
    def active(roster):
        return {reg["minds"][m]["family"] for m in reg["roster"].get(roster, []) if m not in paused} & set(FAMS)
    ROSTER = {"pick": "generators", "reasoned": "reasoners"}
    ACTIVE = active("core")
    active_by = {}
    T = TR.Tree(recs)                                   # with seed votes: the walks seeds make walkable
    Tr = TR.Tree(recs, seeds=False)                     # real answers only: what information is computed from
    seqs = TR.sequences(T)
    written_seqs = TR.sequences(TR.Tree(recs, written=True))
    pend = Pending(recs, rid)
    want, scale = sizes(budget, rid)
    P = Plan(rid, [k for k, c in T.cycles.items() if c["distinct"] >= 4])
    got, pool, claims = {}, {}, {}
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
        ("order", lambda: set_cands("order", T, pend, order_counts(recs), seqs, seeds, rid)),
        ("triad", lambda: triad_cands(T, pend, seqs)),
        ("pick", lambda: pick_cands(T, pend, seqs, seeds, rid)),
    ]
    for name, make in streams:
        ACTIVE = active(ROSTER.get(name, "core")); active_by[name] = sorted(ACTIVE)
        C = make()
        pool[name] = len(C); claims[name] = C.claims()
        got[name] = C.draw(P, want[name], PR.R("draw-" + name, {"round": rid}))
    n_ctx = got["pick"] // PR.SAMPLES
    want["pick-null"] = max(1, round(n_ctx / PARAMS["PICK_NULL_EVERY"])) * PR.SAMPLES
    got["pick-null"] = pick_nulls(P, want["pick-null"], rid)
    asked_before = set()
    here = round_num(rid) if round_num(rid) is not None else 10 ** 9
    for rd in ctx_round_dirs():
        if round_num(rd.name) < here and (rd / "questions.jsonl").exists():
            asked_before |= {json.loads(l)["qid"] for l in open(rd / "questions.jsonl") if l.strip()}
    import hashlib
    h = hashlib.sha256()                     # what was read: every record's content, and the seeds (check of stochastic-2:
    for line in sorted(json.dumps(r, sort_keys=True, ensure_ascii=False) for r in recs):   # an ID can change content)
        h.update(line.encode()); h.update(b"\n")
    for x in sorted(json.dumps(x, sort_keys=True, ensure_ascii=False) for x in seeds):
        h.update(x.encode()); h.update(b"\n")
    stats = {"round": rid, "protocol": PR.PROTOCOL, "planner": "stochastic-3", "questions": len(P.qs), "budget": budget,
             "size_scale": round(scale, 4), "wanted": want, "drawn": got, "candidates": pool, "claims": claims,
             "active_families": active_by, "paused_minds": sorted(paused),
             "answers_read": {"records": len(recs), "seeds": len(seeds), "sha256": h.hexdigest()},
             "reasks": sum(1 for q in P.qs if q["qid"] in asked_before),
             "by_why": dict(collections.Counter(q["source"].get("why") for q in P.qs)),
             "by_kind": dict(collections.Counter(q["kind"] for q in P.qs)),
             "by_variant": dict(collections.Counter(q.get("variant") or "plain" for q in P.qs)),
             "sequences": len(seqs), "contexts_in_tree": len(T.nodes), "params": PARAMS, "base": BASE,
             "branch_curve": [BRANCH_FLOOR, BRANCH_MID, BRANCH_WIDTH]}
    return P.qs, stats
