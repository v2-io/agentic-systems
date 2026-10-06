"""Reproducible content splits: questions where two raters each committed at least twice, unanimously, to DIFFERENT
contents (continue / next: different glyphs; triad: different middles). Raters: minds, and families pooled (all
answers of the family's minds, >= 3, >= 80% one content). Listed whole, with every mind's answers."""
import collections, sys
import lib
from values import value, ckey

recs, man = lib.load()
by = collections.defaultdict(lambda: collections.defaultdict(list))
for r in recs:
    if r["kind"] not in ("continue", "next", "triad") or r["era"] == "seed": continue
    t = r.get("tags") or {}
    if t.get("variant") not in (None, "plain") or t.get("control"): continue
    v = value(r)
    if v is None: continue
    by[ckey(r)][r["mind"]].append(v)
def committed(v): return not str(v).startswith("∅") and str(v) not in ("two", "none", "tie2", "tie3")
fam = lambda m: "claude" if m.startswith(("sonnet", "opus", "haiku")) else ("grok" if m.startswith("grok") else ("gemini" if m.startswith("gemini") else None))
out = []
nq = collections.Counter()
for q, d in by.items():
    F = collections.defaultdict(list)
    for m, vs in d.items():
        if fam(m): F[fam(m)] += vs
    mods = {}
    for f, vs in F.items():
        if len(vs) >= 3:
            x, n = collections.Counter(vs).most_common(1)[0]
            if n / len(vs) >= 0.8 and committed(x): mods[f] = x
    if len(mods) >= 2: nq[q[0]] += 1
    if len(set(mods.values())) >= 2:
        out.append((q, mods, d))
print("questions with >= 2 families each committed (>=3 answers, >=80%):", dict(nq))
print("of those, content splits:", collections.Counter(q[0] for q, _, _ in out))
for q, mods, d in out:
    ctx = "".join(sorted(q[1])) if isinstance(q[1], frozenset) else "".join(q[1])
    per = "; ".join(f"{m}:" + ",".join(f"{k}{v}" for k, v in collections.Counter(vs).most_common(3)) for m, vs in sorted(d.items()))
    print(f"  [{q[0]}] {ctx}  ⇒  " + " | ".join(f"{f}={x}" for f, x in sorted(mods.items())) + f"    ({per})")
