"""Ranked view of the 117 top-40 candidate sequences: strict step score + per-judge whole-set
reorder distance. Uses the independent reading's loader and the builder's parser p1.3 unchanged."""
import sys, json, collections, statistics as stx, pathlib
CR = pathlib.Path("/private/tmp/claude-505/-Users-josephwecker-v2-src-arch-firmatum-utils-aspectus/fcc2ed5a-ac92-4900-9048-7c0adcf7b4bf/scratchpad/gmp-cleanroom")
sys.path.insert(0, str(CR / "reading/scripts"))
from common import *   # ROOT, STIM, ledger, stim_rows, runs, judge_of, I

FRONTIER = ["opus55", "sonnet55", "haiku45", "grok46", "gemini31pro", "gemini38flash"]
cands = {c["cand"]: c for c in json.load(open(STIM / "top40-candidates.json"))["candidates"]}
builder = json.load(open("/Users/josephwecker-v2/src/arch/asf/empirica/glyph-magnitude-perception/analysis/top40.json"))
brank = {r["cand"]: i + 1 for i, r in enumerate(builder)}

def lcs(a, b):
    m = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a)):
        for j in range(len(b)):
            m[i+1][j+1] = m[i][j] + 1 if a[i] == b[j] else max(m[i][j+1], m[i+1][j])
    return m[-1][-1]

def dist(given, order):
    seen, o = set(), []
    for g in order:
        if g in given and g not in seen: o.append(g); seen.add(g)
    f, r = lcs(given, o), lcs(given[::-1], o)
    return len(given) - max(f, r), r > f   # glyphs to move or restore; reversed?

# strict step score from the reading's table
steps = collections.defaultdict(dict)
for line in open(CR / "reading/tables/compare-steps.tsv").read().splitlines()[1:]:
    fam, seq, gl, info, j, n, w, a, p, o = line.split("\t")
    if fam != "top40": continue
    steps[int(seq.split("-")[1])][j.replace("[sheet]", "")] = (int(w), int(a), int(p), int(n))

# gestalt arrangements per judge per candidate
gest = collections.defaultdict(lambda: collections.defaultdict(list))
judges_seen = collections.Counter()
for gpref, gfname in (("top40-gestalt", "top40-gestalt.jsonl"), ("top40b-gestalt", "top40b-gestalt.jsonl")):
    rows = stim_rows(gfname)
    for run in runs(gpref):
        j = judge_of(run).replace("[sheet]", "")
        for r in ledger(run):
            res = r["result"]
            if not res.get("raw") or res.get("error"): continue
            st = rows[r["pids"][0]]
            ci = int(st["seq"].split("-")[1])
            g = I.parse_gestalt(res["raw"], st["glyphs"])
            gest[ci][j].append(g)
            judges_seen[j] += 1
LOCAL = [j for j, c in judges_seen.most_common() if j not in FRONTIER and c >= 100]

def cell(gs, given):
    if not gs: return "–"
    out = []
    for g in gs:
        if g["kind"] == "perp": out.append("⟂")
        elif g["kind"] != "order": out.append("?")
        else:
            d, rev = dist(given, g["order"])
            out.append(f"{d}{'ʳ' if rev and d < len(given) else ''}")
    return "·".join(out)

rows_out = []
for ci, c in cands.items():
    given = c["glyphs"]
    fr = [steps[ci][j] for j in FRONTIER if j in steps[ci] and steps[ci][j][3]]
    W, A = sum(w for w, a, p, n in fr), sum(a for w, a, p, n in fr)
    up = W >= A                      # ONE direction per sequence, by frontier majority
    strict = stx.mean((w if up else a) / n for w, a, p, n in fr) if fr else 0.0
    against = A if up else W
    dists = []
    for j in FRONTIER:
        for g in gest[ci].get(j, []):
            if g["kind"] == "order": dists.append(dist(given, g["order"])[0])
    md = stx.mean(dists) if dists else float("nan")
    rows_out.append((strict, -md, ci, given, against, md, '↑' if up else '↓'))
rows_out.sort(key=lambda t: (-t[0], t[5], t[2]))

H = ["#", "sequence", "n", "dir", "strict", "against", "builder #"] + FRONTIER + LOCAL
print("| " + " | ".join(H) + " |")
print("|" + "|".join(["---"] * len(H)) + "|")
for i, (strict, _, ci, given, against, md, dr) in enumerate(rows_out, 1):
    cells = [cell(gest[ci].get(j, []), given) for j in FRONTIER + LOCAL]
    seq = ''.join(given).replace('|', '\\|')
    print(f"| {i} | `{seq}` | {len(given)} | {dr} | {strict:.2f} | {against} | {brank.get(ci,'')} | " + " | ".join(cells) + " |")
print("\nLOCAL=", LOCAL, file=sys.stderr)
