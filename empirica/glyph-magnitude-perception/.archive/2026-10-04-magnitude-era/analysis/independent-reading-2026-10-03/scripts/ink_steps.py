"""Does a step's rendered-ink change predict whether judges endorse the author's direction?
Over adjacent steps of every authored sequence tested pairwise (top-40 a+b, holistic sets, signa), restricted to
steps where both glyphs are in the Ghostty BMP table and neither has a UCD numeric value: bin by ink change
(later - earlier rung) and report, per bin, the fraction of (judge x step) verdicts that are consistent-directed
WITH the author, AGAINST, ⟂, other. Frontier judges only. Signa's own steps are listed individually."""
import collections, json, os, unicodedata
from common import *
INK = {}
for line in open(os.path.expanduser("~/src/arch/firmatum/utils/utf/bmp-metrics-ghostty.tsv")):
    p = line.rstrip("\n").split("\t")
    if p[0].isdigit():
        try: INK[chr(int(p[0]))] = float(p[12])
        except Exception: pass
def num(c):
    try: return unicodedata.numeric(c)
    except Exception: return None
FR = {"opus55", "sonnet55", "sonnet5", "haiku45", "sonnet55[sheet]", "grok46[sheet]", "gemini31pro[sheet]", "gemini38flash[sheet]", "gpt56terra[sheet]"}
cands = {c["cand"]: c for c in json.load(open(STIM / "top40-candidates.json"))["candidates"]}
hol = {s["name"]: s for s in json.load(open(ROOT / "harness/runner/holistic-sets-v1.json"))["sets"]}
srcs = [("top40-perp", "top40-steps.jsonl", lambda st: ("top40", st["cand"]), lambda k: cands[k[1]]["glyphs"]),
        ("top40b-perp", "top40b-steps.jsonl", lambda st: ("top40", st["cand"]), lambda k: cands[k[1]]["glyphs"]),
        ("holistic-perp", "holistic-pairs.jsonl", lambda st: ("hol", st["seq"]), lambda k: hol[k[1]]["order"] if k[1] in hol else None),
        ("signa-perp", "consumer-signa-pairs.jsonl", lambda st: ("signa", "signa"), lambda k: SIGNA)]
bins = collections.defaultdict(collections.Counter); signa_steps = collections.defaultdict(collections.Counter)
def b(d):
    return "ink drops >0.01" if d < -0.01 else ("|Δink| <= 0.01" if d <= 0.01 else "ink rises >0.01")
for pref, f, keyf, ordf in srcs:
    for run in runs(pref):
        j = judge_of(run)
        if j not in FR: continue
        rows, pres = parsed_presentations(run, f)
        by = collections.defaultdict(dict)
        for pid, st in rows.items(): by[keyf(st)][pid] = st
        for key, rs in by.items():
            order = ordf(key)
            if not order: continue
            adj = {frozenset(p): p for p in zip(order, order[1:])}
            for k, (kind, w, _) in pair_verdicts(rs, {p: pres[p] for p in rs if p in pres}).items():
                if k not in adj: continue
                lo, hi = adj[k]
                if lo not in INK or hi not in INK or num(lo) is not None or num(hi) is not None: continue
                d = INK[hi] - INK[lo]
                v = ("with" if w == hi else "against") if kind == "cdir" else ("perp" if kind == "cperp" else "other")
                if key[0] == "signa": signa_steps[(lo, hi, round(d, 3))][v] += 1
                else: bins[b(d)][v] += 1
out = ["Authored-sequence adjacent steps (top-40 + holistic, excluding signa), frontier judges, by ink change:"]
for k in ("ink drops >0.01", "|Δink| <= 0.01", "ink rises >0.01"):
    c = bins[k]; n = sum(c.values())
    out.append(f"  {k:16s} n={n:4d}  with {c['with']/n:.2f}  against {c['against']/n:.2f}  ⟂ {c['perp']/n:.2f}  other {c['other']/n:.2f}")
out.append("\nSigna steps (frontier judges):")
for (lo, hi, d), c in signa_steps.items():
    out.append(f"  {lo}→{hi}  Δink={d:+.3f}  " + "  ".join(f"{v} {c[v]}" for v in ("with", "against", "perp", "other")))
txt = "\n".join(out); print(txt)
open(ROOT / "reading/tables/ink-steps.txt", "w").write(__doc__ + "\n" + txt + "\n")
