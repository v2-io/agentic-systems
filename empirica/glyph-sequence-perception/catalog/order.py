"""The catalog's O part (CATALOG v5 §6, §9), build 2: does a run's order agree with the order and triad answers about
its glyphs?

Every answer that bears on a run is a UNIT that either agrees with the run's order (either direction: a sequence and
its reverse are one) or does not, against its own chance baseline:
  triad   any asked triple of the run's glyphs (consecutive or not) answered with a middle: agrees when the middle named
          is the run's middle of the three. Baseline 1/3.
  order   any order answer (both eras; the name-only question is not O) whose main line -- its longest -- places at
          least 3 of the run's glyphs, each at a step of its own: agrees when those glyphs run in the run's order,
          either direction. Baseline 2 / m! for m glyphs placed. A line that puts two of the run's glyphs at one step
          (a tie) does not order them and is not a unit; it is counted.
Strength is the excess over chance common to a family's units -- p_u = b_u + (1 - b_u) beta, beta uniform on [0, 1] --
its posterior mean and sd per family; families combined by R's weights; certainty the Bayes factor for beta > 0 (the
same machinery as R and L). "Only two go together", "none", a run's glyphs put in "extra", and ties are their own
counts (§2b: orthogonality and ends are evidence of their own kind), never units against the order.

Not built: the Plackett-Luce fit of §9 (worths, and a concentration about the order). This build scores a given
order; it does not find the best one.
"""
import collections, math

def _main_line(lines):
    return max(lines, key=lambda ln: sum(len(st) for st in ln if st != "GAP")) if lines else []

class Order:
    def __init__(self, recs, rater):
        self.triads = collections.defaultdict(list)       # sorted triple -> [(rater, family, outcome, answer, aid)]
        self.orders = collections.defaultdict(list)       # glyph -> [(rater, family, shown, answer, aid)]
        self.triads_of = collections.defaultdict(set)     # glyph -> triples holding it
        for r in recs:
            k, o = r["kind"], r.get("outcome")
            if k == "triad" and o in ("mid", "two", "none"):
                t = tuple(sorted(r.get("shown") or r["context"]))
                self.triads[t].append((rater(r), r["family"], o, r.get("answer"), r["aid"]))
                for x in t:
                    self.triads_of[x].add(t)
            elif k == "order" and o in ("lines", "none"):
                item = (rater(r), r["family"], tuple(r.get("shown") or r["context"]), r.get("answer") or {}, r["aid"])
                for x in set(item[2]):
                    self.orders[x].append(item)

    def units(self, g):
        """-> (units [(rater, family, agree 0/1, baseline, aid)], counts of the other outcomes)"""
        pos = {x: i for i, x in enumerate(g)}
        units, other = [], collections.Counter()
        for t in set().union(*(self.triads_of.get(x, set()) for x in g)) if g else ():
            rows = self.triads[t]
            if not all(x in pos for x in t):
                continue
            mid = sorted(t, key=lambda x: pos[x])[1]
            for rt, f, o, ans, aid in rows:
                if o == "mid":
                    units.append((rt, f, int(ans[1] == mid), 1 / 3, aid))
                else:
                    other["triad-" + o] += 1
        seen = set()
        for x in g:
            for rt, f, shown, ans, aid in self.orders.get(x, []):
                if aid in seen:
                    continue
                seen.add(aid)
                if sum(1 for y in shown if y in pos) < 3:
                    continue
                if ans.get("none") or not ans.get("lines"):
                    other["order-none"] += 1
                    continue
                other["order-extra"] += sum(1 for y in ans.get("extra") or [] if y in pos)
                steps = [[y for y in st if y in pos] for st in _main_line(ans["lines"]) if st != "GAP"]
                steps = [st for st in steps if st]
                if any(len(st) > 1 for st in steps):
                    other["order-tie"] += 1
                    continue
                ps = [pos[st[0]] for st in steps]
                if len(ps) < 3:
                    other["order-short"] += 1
                    continue
                agree = all(b > a for a, b in zip(ps, ps[1:])) or all(b < a for a, b in zip(ps, ps[1:]))
                units.append((rt, f, int(agree), 2 / math.factorial(len(ps)), aid))
        return units, other

    def part(self, g, weights, bf_excess, grid):
        units, other = self.units(g)
        if not units:
            return None, other
        pts = [(i + 0.5) / grid for i in range(grid)]
        by = collections.defaultdict(list)
        for rt, f, a, b, aid in units:
            by[f].append((a, b))
        fams = {}
        for f, us in by.items():
            ll = []
            for beta in pts:
                s = 0.0
                for a, b in us:
                    p = min(max(b + (1 - b) * beta, 1e-12), 1 - 1e-12)
                    s += math.log(p) if a else math.log(1 - p)
                ll.append(s)
            m = max(ll); w = [math.exp(x - m) for x in ll]; z = sum(w)
            mean = sum(wi * bt for wi, bt in zip(w, pts)) / z
            sd = (sum(wi * (bt - mean) ** 2 for wi, bt in zip(w, pts)) / z) ** 0.5
            fams[f] = {"strength": round(mean, 4), "sd": round(sd, 4), "agree": sum(a for a, _ in us), "n": len(us)}
        num = den = var = 0.0
        for f, v in fams.items():
            wt = weights.get(f, 0.0)
            num += wt * v["strength"]; den += wt; var += (wt * v["sd"]) ** 2
        bf = bf_excess([(a, 1 - a, b) for _, _, a, b, _ in units], grid)
        return {"families": fams, "strength": (num / den) if den else None, "sd": (var ** 0.5 / den) if den else None,
                "bf": bf, "aids": [aid for *_, aid in units]}, other
