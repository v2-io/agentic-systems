"""Each triad orientation set is cyclically arranged (AB, BC, CA), so a judge that picks by POSITION
(always the first-shown, or always the second-shown symbol) produces a 3-cycle every time. This splits each
judge's cycles into position-pure cycles (all three winners in the same slot) vs mixed-slot cycles, and reports
the judge's overall slot preference among directed triad presentations."""
import collections
from common import *
out = [f"{'judge':22s} {'cycles':>6s} {'pos-pure':>8s} {'mixed':>6s}  {'P(first|dir)':>12s} {'n dir':>6s}"]
for run in runs("triads-perp"):
    j = judge_of(run)
    rows, pres = parsed_presentations(run, "triads.jsonl")
    last = {p: v[-1] for p, v in pres.items()}
    sets = collections.defaultdict(list)
    for pid, st in rows.items(): sets[(st["triad"], st["oset"])].append(pid)
    cyc = pure = 0
    for key, pids in sets.items():
        vs = [(rows[p], last.get(p)) for p in pids]
        if len(pids) == 3 and all(v and v[0] == "dir" for _, v in vs):
            wins = collections.Counter(v[1] for _, v in vs)
            if max(wins.values()) == 1:
                cyc += 1
                slots = {("a" if v[1] == st["a"] else "b") for st, v in vs}
                pure += len(slots) == 1
    d = [(rows[p], v) for p, v in last.items() if v[0] == "dir"]
    pf = sum(1 for st, v in d if v[1] == st["a"]) / len(d) if d else float("nan")
    out.append(f"{j:22s} {cyc:6d} {pure:8d} {cyc-pure:6d}  {pf:12.2f} {len(d):6d}")
txt = "\n".join(out); print(txt)
open(ROOT / "reading/tables/triad-position.txt", "w").write(__doc__ + "\n" + txt + "\n")
