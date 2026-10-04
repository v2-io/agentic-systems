import collections
from vload import *
FR = ["opus55","sonnet55","sonnet5","haiku45","grok46[sheet]","gpt56terra[sheet]","gemini31pro[sheet]","gemini38flash[sheet]","sonnet55[sheet]"]
rows = []
res = {}
for rid in runs("holistic-perp-"):
    j = rid.split("-", 3)[3] + ("[sheet]" if "-sheet-" in rid else "")
    j = j.replace("-sheet[sheet]", "[sheet]")
    ans = pair_answers(rid)
    byp = collections.defaultdict(dict)
    for (p, rep), v in ans.items():
        s = STIM[p]; byp[(s["seq"], frozenset((s["a"], s["b"])))][s["order"]] = (v, s)
    c = collections.defaultdict(collections.Counter)
    for (seq, k), d in byp.items():
        if 0 not in d or 1 not in d: c[seq]["missing"] += 1; continue
        vd = verdict_pair(d[0][0], d[1][0], d[0][1]["a"], d[0][1]["b"])
        kind = vd[0] if isinstance(vd, tuple) else vd
        c[seq]["n"] += 1; c[seq][kind] += 1
        if kind == "cdir":
            s0 = d[0][1]; it = s0["intended"]  # intended indices for (a,b)
            hi = s0["a"] if it[0] > it[1] else s0["b"]
            c[seq]["agree"] += vd[1] == hi
    res[j] = c
for seq in ["dice","unfold","risebar","elab-n","elab-s","elab-l"]:
    print(seq, "  ".join(f"{j}:{res[j][seq]['cdir']}/{res[j][seq]['n']}={res[j][seq]['cdir']/max(res[j][seq]['n'],1):.2f}(agr{res[j][seq]['agree']})" for j in FR if j in res))
