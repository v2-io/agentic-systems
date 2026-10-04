import collections
from vload import *
P9 = ["roman-8-9","roman-3-5","roman-lc-8-9","roman-lc-3-4","roman-lc-4-5","sup9-vs-2","sub8-vs-3","sup7-vs-1","seg-0-vs-1","seg-0-vs-7","frac-8th-vs-half","frac-9th-vs-3rd","frac-10th-vs-5th"]
P10b = {"gram-earth-vs-heaven": "☰", "gram-yin-vs-yang": "⚊", "gram-gyin-vs-gyang": "⚌"}
P11 = ["permille-mille-vs-myriad", "permille-pct-vs-myriad"]
P12 = ["sup9-vs-9-equal", "die5-vs-5-equal"]
FR = ["opus55","sonnet55","sonnet5","haiku45","grok46","gpt56terra","gemini31pro","gemini38flash"]
pool = collections.Counter()
for rid in runs("conflict-"):
    j = rid.split("-", 3)[3]; sheet = "-sheet-" in rid
    lab = j + ("[sheet]" if sheet else "")
    ans = pair_answers(rid)
    c = collections.Counter(); per = collections.defaultdict(collections.Counter)
    for (p, rep), v in ans.items():
        s = STIM[p]; it = s["item"]; per[it][v[1] if v[0]=="dir" else v[0]] += 1
        if v[0] == "dir":
            if it in P9: c["p9n"] += 1; c["p9k"] += v[1] == s["annot"]["value"]
            if it == "gram-earth-vs-gyang": c["p10an"] += 1; c["p10ak"] += v[1] == "☷"
            if it in P10b: c["p10bn"] += 1; c["p10bk"] += v[1] == P10b[it]
            if it in P11: c["p11n"] += 1; c["p11k"] += v[1] == "‱"
        if it in P12 and v[0] != "unparsed":
            c["p12n"] += 1; c["p12k"] += v[0] in ("tie", "perp")
    f = lambda k: f"{c[k+'k']}/{c[k+'n']}"
    print(f"{lab:20s} P9 {f('p9'):7s} P10a {f('p10a'):5s} P10b {f('p10b'):6s} P11 {f('p11'):6s} P12 {f('p12'):6s}")
    if j in FR:
        for k in c: pool[k] += c[k]
    if j in ("sonnet5","opus55","haiku45","gemini31pro") :
        print("    ", {it: dict(per[it]) for it in P11})
print("pooled frontier (incl sonnet55 sheet):", {k: round(pool[k+'k']/pool[k+'n'],2) for k in ("p9","p10a","p10b","p11","p12")}, dict(pool))
