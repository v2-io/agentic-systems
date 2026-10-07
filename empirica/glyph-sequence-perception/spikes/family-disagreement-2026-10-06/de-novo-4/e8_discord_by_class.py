# Of commit disagreements (one stops, the other continues; first plain answers), what share sit on each context class?
import sys, collections
sys.path.insert(0, ".")
from e5_chart_given import first, cls
for a, b in (("sonnet55", "grok46"), ("opus55", "grok46"), ("sonnet55", "gemini38flash"), ("sonnet55", "haiku45nt"), ("sonnet55", "opus55")):
    n = collections.Counter(); dis = collections.Counter(); dirn = collections.Counter()
    for q, d in first.items():
        if a in d and b in d:
            c = cls[q]; n[c] += 1
            if d[a] != d[b]: dis[c] += 1; dirn[(c, "b stops" if d[b] else "a stops")] += 1
    T = sum(dis.values())
    print(f"{a} vs {b}: {T} commit disagreements of {sum(n.values())} shared contexts; by class: " +
          "  ".join(f"{c} {dis[c]} ({dis[c]/T:.0%} of disagreements; {n[c]/sum(n.values()):.0%} of contexts; {b[:5]} stops in {dirn[(c,'b stops')]})" for c in ("cg", "cn", "mono", "oth")))
