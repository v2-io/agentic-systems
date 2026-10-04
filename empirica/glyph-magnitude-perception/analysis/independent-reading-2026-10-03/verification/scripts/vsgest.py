from vload import *
import itertools
ORDER = ["·","╶","╌","╍","━","═","⚬","○","◎","◉","⬤"]
def tau(order, ref):
    seen=set(); common=[]
    for g in order:
        if g in ref and g not in seen: seen.add(g); common.append(g)
    if len(common) < 2: return None, len(common)
    pos = {g: i for i, g in enumerate(ref)}
    c = d = 0
    for x, y in itertools.combinations(common, 2):
        s = (pos[x] - pos[y]); c += s < 0; d += s > 0
    return (c - d) / (c + d), len(common)
def _main():
  for rid in runs("signa-gestalt-"):
      g = gestalt_answers(rid)
      for p, a in sorted(g.items(), key=lambda kv: STIM[kv[0]]["shuffle"]):
          t, n = tau(a.get("order", []), ORDER) if a["kind"] == "order" else (None, 0)
          print(f"{rid.replace('signa-gestalt-gestalt-single-',''):14s} sh{STIM[p]['shuffle']} {a['kind']:6s} τ={'' if t is None else round(abs(t),2)} cov={n}/11 | {a['raw'].strip()[:70]!r}")

if __name__ == "__main__": _main()