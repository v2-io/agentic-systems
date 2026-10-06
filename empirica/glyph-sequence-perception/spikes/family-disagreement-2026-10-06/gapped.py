"""Out-of-sample test of a pattern read off the flat triad disagreements: Grok declines betweenness ("two"/"none") on
gapped members of a series where Gemini names the middle. All triads, both eras, plain variant; triples classed from
the glyphs alone: one block, code points monotone in the sorted triple, max gap 1 (contiguous) / 2-4 (small gap) /
5+ (large gap); or more than one block. Share answering with a middle, and the share whose middle is the code-point
median, per mind. Triples holding U+2581 are left out (the known Gemini case)."""
import collections
import lib, features as F

recs, man = lib.load()
cls = lambda g: (("1blk-" + ("contig" if max(b - a for a, b in zip(o, o[1:])) == 1 else ("gap2-4" if max(b - a for a, b in zip(o, o[1:])) <= 4 else "gap5+")))
                 if len({F.block(x) for x in g}) == 1 else "multi-block") if (o := sorted(ord(x) for x in g)) else None
cell = collections.defaultdict(lambda: [0, 0, 0])
for r in recs:
    if r["kind"] != "triad" or (r.get("tags") or {}).get("variant") not in (None, "plain"): continue
    g = r.get("shown") or r.get("context")
    if not g or len(set(g)) != 3 or "▁" in g: continue
    c = cls(g)
    med = sorted(g, key=ord)[1]
    a = r.get("answer") or []
    k = cell[(r["mind"], c)]
    k[2] += 1
    if r["outcome"] == "mid":
        k[0] += 1; k[1] += (len(a) > 1 and a[1] == med)
for m in ("sonnet55", "opus55", "haiku45", "haiku45nt", "grok46", "gemini38flash", "gemini31pro", "glimmer30b-sheet"):
    row = []
    for c in ("1blk-contig", "1blk-gap2-4", "1blk-gap5+", "multi-block"):
        mid, med, n = cell[(m, c)]
        row.append(f"{c}: mid {mid/n:.2f} (median {med/max(mid,1):.2f}) n={n}" if n else f"{c}: -")
    print(f"{m:16s} " + " | ".join(row))
