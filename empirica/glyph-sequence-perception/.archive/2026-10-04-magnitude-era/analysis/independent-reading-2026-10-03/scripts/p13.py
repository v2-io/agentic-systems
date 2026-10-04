"""P13: dice gestalt |tau| per shuffle per frontier judge; noise-foil ⟂ share of parsed frontier presentations
(errored/unparsed calls excluded from the denominator, reported separately). Also the noise-foil orders verbatim,
to show cross-judge agreement on random sets."""
import collections
from common import *
FR = ["opus55", "sonnet55", "sonnet5", "haiku45", "grok46", "gpt56terra", "gemini31pro", "gemini38flash"]
rows = stim_rows("gestalt.jsonl"); out = []
noise = collections.Counter(); orders = collections.defaultdict(list)
for run in runs("gestalt-gestalt"):
    j = spec(run)["judge_label"]
    if j not in FR: continue
    for r in ledger(run):
        st = rows[r["pids"][0]]; raw = r["result"].get("raw")
        g = I.parse_gestalt(raw, st["glyphs"]) if raw and not r["result"].get("error") else {"kind": "err"}
        if st["seq"] == "dice":
            t, n = kendall_tau(g.get("order", []), st["intended"]) if g["kind"] == "order" else (None, 0)
            out.append(f"dice {j:14s} shuffle {st['shuffle']}: {g['kind']} tau={t} n={n}")
        if st["seq"].startswith("noise"):
            noise[(j, g["kind"])] += 1
            if g["kind"] == "order": orders[st["seq"]].append(f"{j}:{''.join(g['order'])}")
for j in FR:
    p, o = noise[(j, "perp")], noise[(j, "order")]
    out.append(f"noise {j:14s} ⟂ {p}  order {o}  err/unparsed {noise[(j,'err')]+noise[(j,'unparsed')]}  ⟂/parsed={p/(p+o):.2f}")
P = sum(noise[(j, "perp")] for j in FR); O = sum(noise[(j, "order")] for j in FR)
out.append(f"noise POOLED frontier ⟂/parsed = {P}/{P+O} = {P/(P+O):.2f}")
for s, l in sorted(orders.items()): out.append(f"{s}: " + " | ".join(l))
txt = "\n".join(out); print(txt); open(ROOT / "reading/tables/p13.txt", "w").write(__doc__ + "\n" + txt + "\n")
