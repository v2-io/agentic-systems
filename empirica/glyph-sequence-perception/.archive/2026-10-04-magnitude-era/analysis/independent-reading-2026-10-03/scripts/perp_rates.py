"""Presentation-level verdict mix per judge x instrument (perp format only), and per stratum where one exists.
Puts signa's ⟂ use beside the same judge's ⟂ use on every other perp instrument."""
import collections
from common import *

inst = {"triads-perp": "triads.jsonl", "format-perp": "format-pairs.jsonl", "conflict-perp": "conflict.jsonl",
        "holistic-perp": "holistic-pairs.jsonl", "top40-perp": "top40-steps.jsonl", "top40b-perp": "top40b-steps.jsonl",
        "signa-perp": "consumer-signa-pairs.jsonl"}
tab = collections.defaultdict(dict)
for pref, f in inst.items():
    for run in runs(pref):
        rows, pres = parsed_presentations(run, f)
        j = judge_of(run)
        def mix(pids):
            c = collections.Counter(pres[p][-1][0] for p in pids if p in pres)
            n = sum(c.values())
            return (n, c["perp"] / n if n else float('nan'), c["dir"] / n if n else float('nan'), c["unparsed"] / n if n else float('nan'))
        tab[j][pref] = mix(list(rows))
        if pref in ("triads-perp", "format-perp"):
            strata = collections.defaultdict(list)
            for p, st in rows.items(): strata[st.get("stratum")].append(p)
            for s, ps in strata.items(): tab[j][f"{pref}:{s}"] = mix(ps)
        if pref == "signa-perp":
            seam = [p for p, st in rows.items() if (IDX[st['a']] <= 5) != (IDX[st['b']] <= 5)]
            within = [p for p in rows if p not in seam]
            tab[j]["signa:seam"] = mix(seam); tab[j]["signa:within"] = mix(within)
cols = ["triads-perp:uniform", "triads-perp:seed-cross", "triads-perp:seed-local", "format-perp:fresh-mixed", "format-perp:fresh-seed-local",
        "format-perp:pilot-replication", "holistic-perp", "top40-perp", "conflict-perp", "signa:seam", "signa:within"]
short = ["tri:unif", "tri:xseed", "tri:local", "fmt:mixed", "fmt:local", "fmt:pilot", "holistic", "top40", "conflict", "SIGNA:seam", "SIGNA:within"]
out = ["⟂ rate per presentation (perp format). Rows: judge. n in parentheses for signa columns.",
       f"{'judge':22s}" + "".join(f"{s:>11s}" for s in short)]
for j in sorted(tab):
    if "signa-perp" not in tab[j]: continue
    cells = []
    for c in cols:
        v = tab[j].get(c)
        cells.append(f"{v[1]:>11.2f}" if v else f"{'-':>11s}")
    out.append(f"{j:22s}" + "".join(cells))
print("\n".join(out))
open(ROOT / "reading/tables/perp-rates.txt", "w").write("\n".join(out) + "\n")
