"""Systematic difference between two minds, with sampling noise removed.

For a question q and minds A, B with answer distributions p_A, p_B over that question's possible answers:
  w_A = sum p_A^2 (two independent answers of A agree), w_B likewise, c = sum p_A p_B (an answer of A agrees with B's).
  D = (w_A + w_B)/2 - c = (1/2) sum (p_A - p_B)^2  >= 0, zero exactly when A and B answer that question alike.
Each term is estimated without bias from the answers: w_A from all pairs of A's answers, c from all A x B pairs.
Only questions where A and B each answered at least twice are used, so every term is on the same questions.
Reported: D (mean over questions), the mean within-mind agreement W = (w_A + w_B)/2, and D/W, the share of the
agreement two answers of the same mind would have that is lost by asking the other mind instead. Standard errors by
bootstrap over questions (fated seed 0)."""
import collections, itertools, random, sys
import lib
from values import value, ckey

def prepare(kinds, era=None):
    recs, man = lib.load()
    by = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in recs:
        if r["era"] == "seed": continue
        if era and r["era"] != era: continue
        if r["kind"] not in kinds: continue
        if (r.get("tags") or {}).get("variant") not in (None, "plain"): continue
        v = value(r)
        if v is None: continue
        q = ckey(r)
        if q is None: continue
        by[q][r["mind"]].append(v)
    return by

def pair_stats(vs):
    n = len(vs)
    if n < 2: return None
    c = collections.Counter(vs)
    return (sum(x * (x - 1) for x in c.values()) / (n * (n - 1)))

def cross(va, vb):
    ca = collections.Counter(va); cb = collections.Counter(vb)
    return sum(ca[x] * cb[x] for x in ca) / (len(va) * len(vb))

def distance(by, a, b, qfilter=None, boot=300):
    rows = []
    for q, d in by.items():
        if qfilter and not qfilter(q): continue
        va, vb = d.get(a, []), d.get(b, [])
        if len(va) >= 2 and len(vb) >= 2:
            wa, wb, c = pair_stats(va), pair_stats(vb), cross(va, vb)
            rows.append((wa, wb, c))
    if len(rows) < 10:
        return None
    def summ(rs):
        W = sum((x[0] + x[1]) / 2 for x in rs) / len(rs)
        C = sum(x[2] for x in rs) / len(rs)
        return W, C, W - C
    W, C, D = summ(rows)
    rng = random.Random(0); bs = []
    for _ in range(boot):
        s = [rows[rng.randrange(len(rows))] for _ in rows]
        bs.append(summ(s)[2])
    bs.sort()
    se = (sum((x - D) ** 2 for x in bs) / len(bs)) ** 0.5
    return dict(n=len(rows), W=W, C=C, D=D, se=se, rel=D / W if W else float("nan"),
                wa=sum(x[0] for x in rows) / len(rows), wb=sum(x[1] for x in rows) / len(rows))

MINDS = ["sonnet55", "opus55", "haiku45nt", "haiku45", "grok46", "gemini38flash", "gemini31pro"]
FAM = {"sonnet55": "claude", "opus55": "claude", "haiku45nt": "claude", "haiku45": "claude", "grok46": "grok",
       "gemini38flash": "gemini", "gemini31pro": "gemini"}

if __name__ == "__main__":
    kinds = sys.argv[1:] or ["continue"]
    by = prepare(set(kinds))
    print("kinds", kinds, "questions", len(by))
    for a, b in itertools.combinations(MINDS, 2):
        s = distance(by, a, b)
        if s:
            tag = "same" if FAM[a] == FAM[b] else "cross"
            print(f"  {a:14s} {b:14s} {tag:5s} n={s['n']:5d} w_a={s['wa']:.3f} w_b={s['wb']:.3f} cross={s['C']:.3f} "
                  f"D={s['D']:.3f}±{s['se']:.3f}  D/W={s['rel']:.2f}")
