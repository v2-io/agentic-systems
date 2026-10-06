"""Continue answers, Sonnet vs Grok (and the others), per context: where they disagree, is it end placement (one
continues, the other stops) or a different glyph? And does Grok's stopping go with the chart's next glyph, by the
familiarity of that glyph (token count in two public byte-level BPE vocabularies) and the context's chart shape?"""
import collections, sys
import lib, tok
from values import value, ckey

def modal(vs):
    return collections.Counter(vs).most_common(1)[0][0] if vs else None

def chart_next(ctx):
    if len(ctx) < 2: return None
    d = ord(ctx[-1]) - ord(ctx[-2])
    if d == 0: return None
    try: return chr(ord(ctx[-1]) + (1 if d > 0 else -1))
    except ValueError: return None

def contiguous(ctx):
    d = [ord(b) - ord(a) for a, b in zip(ctx, ctx[1:])]
    return bool(d) and (all(x == 1 for x in d) or all(x == -1 for x in d))

def table(A="sonnet55", B="grok46", kinds=("continue",)):
    recs, man = lib.load()
    by = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in recs:
        if r["kind"] not in kinds or r["era"] == "seed": continue
        if (r.get("tags") or {}).get("variant") not in (None, "plain"): continue
        v = value(r)
        if v is None: continue
        by[ckey(r)][r["mind"]].append(v)
    rows = []
    for q, d in by.items():
        if d.get(A) and d.get(B):
            rows.append((q[1], modal(d[A]), modal(d[B]), d))
    return rows

if __name__ == "__main__":
    A, B = (sys.argv[1:3] if len(sys.argv) > 2 else ("sonnet55", "grok46"))
    rows = table(A, B)
    N = len(rows); agree = sum(a == b for _, a, b, _ in rows)
    stopA = sum(a == "∅none" and b != "∅none" and not b.startswith("∅") for _, a, b, _ in rows)
    stopB = sum(b == "∅none" and a != "∅none" and not a.startswith("∅") for _, a, b, _ in rows)
    glyph = sum(a != b and not a.startswith("∅") and not b.startswith("∅") for _, a, b, _ in rows)
    print(f"{A} vs {B}: contexts {N}; same modal answer {agree} ({agree/N:.3f}); {A} stops / {B} continues {stopA}; "
          f"{B} stops / {A} continues {stopB}; both continue, different glyph {glyph}; other {N-agree-stopA-stopB-glyph}")
    # where A continues: does B stop, by whether A's glyph is the chart's next, by familiarity and context shape
    cell = collections.defaultdict(lambda: [0, 0])
    for ctx, a, b, _ in rows:
        if a.startswith("∅") or b.startswith("∅") and b != "∅none": continue
        cn = chart_next(ctx)
        isnext = a == cn
        q = tok.QWEN.ntok(a); c = tok.CLAUDE23.ntok(a)
        fam = "1tok" if min(q, c) == 1 else "multi"
        key = (("chart-next" if isnext else "other glyph"), fam, "contig" if contiguous(ctx) else "not-contig")
        cell[key][0] += (b == "∅none"); cell[key][1] += 1
    print(f"\nwhere {A} continues: share where {B} stops instead")
    for k in sorted(cell):
        s, n = cell[k]
        print(f"  {k[0]:12s} {k[1]:6s} {k[2]:11s} {s:5d}/{n:5d} = {s/n:.3f}")
