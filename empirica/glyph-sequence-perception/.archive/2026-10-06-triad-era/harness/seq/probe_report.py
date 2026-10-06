#!/usr/bin/env python3
"""Report on a probe round (round.py probe): what each mind did with each probed seed.

  probe_report.py RID          -> data/rounds/RID/probe-report.md (and printed)

For a `sequence` seed, its written order is used only as a DESCRIPTIVE reference ("does the answer agree with
the order the seed states?"); nothing here feeds the fit or the queue. For a `set` seed there is no reference, and the report
shows how each mind groups and orders the set.

Per mind, over the seed's triads (each shown in 3 rotations):
  agree      share of triad answers whose middle is the reference middle
  none/two   shares of ⟂ and "only two go together"
  left out   per glyph: share of the triads containing it in which the answer was "two" without it
  3/3        share of triads given the same answer in all three rotations
Per mind, over the order items: each answer's lines verbatim (sequences, extra), so placements can be read directly.
"""
import collections, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from common import EXP, read_jsonl
import round as RD

def main():
    rid = sys.argv[1]
    d = EXP / "data"; rd = d / "rounds" / rid
    plan = json.load(open(rd / "plan.json"))
    seeds = {x["sid"]: x for x in read_jsonl(d / "seeds.jsonl")}
    for x in RD.domain_seeds():
        seeds.setdefault(x["sid"], x)
    items, pres, parsed, sheets = RD.load_all(d)
    mine = [r for r in parsed if r["round"] == rid]
    it_here = {i["iid"]: i for i in read_jsonl(rd / "items.jsonl")}
    L = [f"# Probe report — {rid}", "", f"*{plan.get('why', '')}*", "",
         f"Minds: {', '.join(plan['minds'])}. {plan['presentations']} presentations on {plan['sheets']} sheets "
         f"(1–5 presentations each). Triads in all three Latin rotations; order items in {2} independent shuffles.", ""]
    for sid in plan["probe"]:
        sd = seeds[sid]; g = list(dict.fromkeys(sd["glyphs"])); ref = {x: i for i, x in enumerate(g)}
        L += [f"## `{''.join(g)}` ({sd['type']}, seed {sid})", ""]
        tri = collections.defaultdict(lambda: collections.defaultdict(list))   # mind -> iid -> answers by rep
        for r in mine:
            p = pres[r["pid"]]; it = it_here.get(p["iid"])
            if not it or it["source"].get("ref") != sid or p["kind"] != "triad":
                continue
            tri[r["mind"]][p["iid"]].append(r["answer"] if r["status"] == "ok" else ("unparsed",))
        if sd["type"] == "sequence":
            L += ["Triads: agreement with the written order (direction-free), per mind.", "",
                  "| mind | triads | answers | agree | ⟂ | two | other order | 3/3 same | most left out |", "|---|---|---|---|---|---|---|---|---|"]
        else:
            L += ["Triads (no reference order), per mind.", "", "| mind | triads | answers | ordered | ⟂ | two | 3/3 same | most left out |", "|---|---|---|---|---|---|---|---|"]
        for m in sorted(tri):
            c = collections.Counter(); same = 0; nfull = 0; left = collections.Counter(); hold = collections.Counter()
            for iid, ans in tri[m].items():
                t = items[iid]["glyphs"]
                for x in t:
                    hold[x] += len(ans)
                if len(ans) == 3:
                    nfull += 1; same += len({str(a) for a in ans}) == 1
                for a in ans:
                    if a[0] == "mid":
                        if sd["type"] == "sequence":
                            tm = sorted(t, key=lambda x: ref[x])[1]
                            c["agree" if a[1] == tm else "other"] += 1
                        else:
                            c["ordered"] += 1
                    elif a[0] == "two":
                        c["two"] += 1; left[[x for x in t if x not in a[1:]][0]] += 1
                    else:
                        c[a[0]] += 1
            n = sum(c.values())
            lo = max(((left[x] / hold[x], x) for x in hold if hold[x]), default=(0, ""))
            lo_s = f"`{lo[1]}` {lo[0]:.2f}" if lo[0] > 0 else "—"
            if sd["type"] == "sequence":
                L.append(f"| {m} | {len(tri[m])} | {n} | {c['agree']/n:.2f} | {c['none']/n:.2f} | {c['two']/n:.2f} | {c['other']/n:.2f} | "
                         f"{same/max(1,nfull):.2f} ({nfull}) | {lo_s} |")
            else:
                L.append(f"| {m} | {len(tri[m])} | {n} | {c['ordered']/n:.2f} | {c['none']/n:.2f} | {c['two']/n:.2f} | {same/max(1,nfull):.2f} ({nfull}) | {lo_s} |")
        if sd["type"] == "sequence":
            L += ["", "Agreement per adjacent link of the written order: triads holding both glyphs of the link whose answer agrees with the order, all minds pooled, then per mind.", ""]
            links = list(zip(g, g[1:]))
            L += ["| link | " + " | ".join(sorted(tri)) + " |", "|---|" + "---|" * len(tri)]
            for a_, b_ in links:
                row = []
                for m in sorted(tri):
                    k = n = 0
                    for iid, ans in tri[m].items():
                        t = items[iid]["glyphs"]
                        if a_ in t and b_ in t:
                            tm = sorted(t, key=lambda x: ref[x])[1]
                            for an in ans:
                                n += 1; k += an[0] == "mid" and an[1] == tm
                    row.append(f"{k}/{n}")
                L.append(f"| `{a_}{b_}` | " + " | ".join(row) + " |")
        L += ["", "Order items: every answer (sequence lines; extra).", ""]
        for r in sorted(mine, key=lambda r: (r["mind"], r["pid"])):
            p = pres[r["pid"]]; it = it_here.get(p["iid"])
            if not it or it["source"].get("ref") != sid or p["kind"] != "order":
                continue
            if r["status"] != "ok":
                s = "unparsed"
            elif r["answer"].get("none"):
                s = "⟂"
            else:
                s = " / ".join(" ".join("=".join(st) if st != "GAP" else "…" for st in line) for line in r["answer"]["lines"])
                if r["answer"].get("extra") or r["answer"].get("omitted"):
                    s += "  · extra: " + "".join(r["answer"].get("extra", []) + r["answer"].get("omitted", []))
            L.append(f"- {r['mind']}: shown `{''.join(p['shown'])}` → {s}")
        L.append("")
    out = "\n".join(L) + "\n"
    (rd / "probe-report.md").write_text(out)
    print(out)

if __name__ == "__main__":
    main()
