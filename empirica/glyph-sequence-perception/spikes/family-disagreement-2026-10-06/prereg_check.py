#!/usr/bin/env python3
"""Score test round p001 against prereg-flat-splits.json.

Primary (as pre-registered, "how_to_check"): the share of grok46's answers that are "none" and of sonnet55's that
continue, against the predicted 95% bands. Secondary (not pre-registered as a test, reported beside it): each answer
scored against its own context's predicted probability -- the expected count with a Poisson-binomial 95% band, and
the log score against a "settled" model that predicts each mind repeats its earlier answers (probability 0.95, chosen
without evidence; it stands for "the flat split is a stable mind x context difference"). Answers other than a
continuation or "none" (other, unparsed, failed) are listed and left out of both shares."""
import collections, json, math, pathlib

HERE = pathlib.Path(__file__).resolve().parent
STUDY = HERE.parents[1]
SETTLED_P = 0.95

def poibin_band(ps, lo=0.025, hi=0.975):
    dist = [1.0]
    for p in ps:
        nd = [0.0] * (len(dist) + 1)
        for k, v in enumerate(dist):
            nd[k] += v * (1 - p); nd[k + 1] += v * p
        dist = nd
    c, a, b = 0.0, None, None
    for k, v in enumerate(dist):
        c += v
        if a is None and c >= lo:
            a = k
        if b is None and c >= hi:
            b = k
    return a, b

def main():
    pre = json.load(open(HERE / "prereg-flat-splits.json"))
    by_ctx = {tuple(c["context_glyphs"]): c for c in pre["contexts"]}
    recs = [json.loads(l) for l in open(STUDY / "data" / "answers" / "p001.jsonl") if l.strip()]
    got = collections.defaultdict(dict)
    other = []
    for r in recs:
        c = tuple(r["context"])
        if r["outcome"] in ("continuation", "none"):
            got[r["mind"]][c] = r["outcome"]
        else:
            other.append((r["mind"], "".join(c), r["outcome"]))
    band = pre["prediction"]
    out = []
    for m, want, key in (("grok46", "none", "grok46_next_answer_stops_share"), ("sonnet55", "continuation", "sonnet55_next_answer_continues_share")):
        a = got[m]
        k = sum(1 for o in a.values() if o == want)
        lo, med, hi = band[key]["median_and_95"]
        share = k / len(a) if a else float("nan")
        verdict = "inside" if lo <= share <= hi else ("above" if share > hi else "below")
        out.append(f"{m}: {k}/{len(a)} {'stop' if want == 'none' else 'continue'} = {share:.3f}; predicted {med} [{lo}-{hi}]: {verdict} the band")
        # secondary
        ps, ll_model, ll_settled = [], 0.0, 0.0
        for c, o in a.items():
            p_stop = by_ctx[c]["p_stop_next"][m]
            p = p_stop if want == "none" else 1 - p_stop          # predicted probability of the flat-split answer again
            ps.append(p)
            hit = (o == want)
            ll_model += math.log(p if hit else 1 - p)
            ll_settled += math.log(SETTLED_P if hit else 1 - SETTLED_P)
        b = poibin_band(ps)
        out.append(f"   secondary: expected {sum(ps):.1f} [95% {b[0]}-{b[1]}] from each context's own prediction; "
                   f"log score model {ll_model:.2f} vs settled(p={SETTLED_P}) {ll_settled:.2f} nats")
    print("\n".join(out))
    if other:
        print(f"left out ({len(other)}):", other)

if __name__ == "__main__":
    main()
