"""Is the Claude minds' extra endorsement of contiguous runs self-preference (runs Claude minds wrote) or chart
reliance? The contiguity offset per mind (cohere_logit's regression) refitted within run sources: survey seeds
written by a Claude surveyor, by the Grok surveyor (grok-1), and the tree's walks. Runs are attributed to a source by
the cohere question's `source.from` (planner metadata, read here only to split; nothing is evidence of anything)."""
import collections, sys
sys.argv = sys.argv[:1]
import cohere_logit as CL
import lib
sys.path.insert(0, str(lib.ROOT)); import run as RUN
surv = {s.get("sid"): (s.get("surveyor") or "") for s in RUN.seeds()}
def fam_of(sv):
    sv = sv.lower()
    return "grok" if sv.startswith("grok") else ("claude" if sv.startswith(("sonnet", "fable", "opus", "haiku")) else ("human" if "joseph" in sv else "other:" + sv))
src = {}
for r in CL.recs:
    if r["kind"] != "cohere" or (r.get("tags") or {}).get("control"): continue
    f = (r.get("source") or {}).get("from") or ""
    q = CL.ckey(r)
    if f.startswith("seed:survey:"):
        src[q] = "seed by " + fam_of(surv.get("survey:" + f.split(":")[2], "?"))
    elif f in ("walk", "written", "pick-branch", "reordered"):
        src[q] = f
print(collections.Counter(src.values()))
for S in ("seed by claude", "seed by grok", "walk", "written", "pick-branch"):
    print(f"\n-- source: {S}")
    for m in ("sonnet55", "opus55", "haiku45nt", "grok46", "gemini38flash"):
        X, Y = [], []
        for q, d in CL.ans.items():
            if src.get(q) != S or m not in d or len(d) < 2: continue
            b = CL.fit_beta(d, excl=(m,)); cc = CL.F.chart_class(CL.glyph[q])
            for y in d[m]:
                X.append([1.0, b, 1.0 if cc == "contiguous" else 0.0]); Y.append(y)
        nc = sum(x[2] for x in X)
        if len(Y) < 40 or nc < 10 or nc == len(Y): print(f"   {m:14s} n={len(Y)} contiguous={int(nc)} (too few)"); continue
        w, se = CL.logreg(X, Y)
        print(f"   {m:14s} n={len(Y):5d} contiguous={int(nc):4d}  s={w[1]:.2f}  c_contig={w[2]:+.2f}±{se[2]:.2f}")
