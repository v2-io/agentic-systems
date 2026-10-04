"""Signa pair x judge matrix. Cell: + = author's direction (later rung wins both orders), - = against,
p = consistent ⟂, t = consistent ≈, m = mixed (e.g. one order ⟂, other directed), f = flip (opposite winners),
? = an order unparsed/missing. Felt-distance shown for + / - when both orders agree on it (s/m/v)."""
import itertools
from common import *

order_j = ["opus55", "sonnet55", "sonnet5", "haiku45", "sonnet55[sheet]", "grok46[sheet]", "gemini31pro[sheet]",
           "gemini38flash[sheet]", "glimmer30b[sheet]", "llama32-3b", "qwen25-3b"]
data = {}
for run in runs("signa-perp"):
    rows, pres = parsed_presentations(run, "consumer-signa-pairs.jsonl")
    data[judge_of(run)] = pair_verdicts(rows, pres)
code = {"cdir": None, "cperp": "p", "ctie": "t", "mixed": "m", "flip": "f", "incomplete": "?"}
lines = []
hdr = "pair      seg     " + " ".join(f"{j[:9]:>9s}" for j in order_j)
lines.append(hdr)
tally = {j: {} for j in order_j}
for a, b in itertools.combinations(SIGNA, 2):
    k = frozenset((a, b))
    seg = "lines" if IDX[b] <= 5 else ("circles" if IDX[a] >= 6 else "seam")
    cells = []
    for j in order_j:
        kind, w, (v0, v1) = data[j][k]
        if kind == "cdir":
            c = "+" if w == b else "-"
            if v0[2] and v0[2] == v1[2]: c += v0[2][0]
        else:
            c = code[kind]
        cells.append(f"{c:>9s}")
    lines.append(f"{a}<{b}  ({IDX[a]:2d},{IDX[b]:2d}) {seg:7s} " + " ".join(cells))
txt = "\n".join(lines)
print(txt)
open(ROOT / "reading/tables/signa-pair-matrix.txt", "w").write(__doc__ + "\nSIGNA author order: " + "".join(SIGNA) + "\n\n" + txt + "\n")
