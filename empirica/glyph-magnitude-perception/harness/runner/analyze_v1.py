#!/usr/bin/env python3
"""v1.0 analysis: re-derives every reported number from the verbatim ledgers + frozen stimuli.

  analyze_v1.py [--out analysis/v1.0-results.md] [--json analysis/v1.0-results.json]

Definitions are the ones fixed in protocol/PROTOCOL-v1.0.md ("Edge and verdict definitions")
and PREDICTIONS-v1.0.md. Shakedown runs (run_id ending -shakedown) are excluded.
Nothing here writes to data/; outputs are derived and disposable.
"""
import argparse, csv, glob, json, math, pathlib, sys
from collections import defaultdict, Counter
from itertools import combinations
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import instruments as I

EXP = pathlib.Path(__file__).resolve().parents[2]
UTF = pathlib.Path.home() / "src/arch/firmatum/utils/utf"
csv.field_size_limit(10**9)

# ------------------------------------------------------------------ features
INK, NUM = {}, {}
def load_features():
    for r in csv.DictReader(open(UTF / "bmp-metrics-ghostty.tsv"), delimiter="\t", quoting=csv.QUOTE_NONE):
        try:
            INK[r["char"]] = float(r["packed_density"])
        except (ValueError, KeyError):
            pass
    for r in csv.DictReader(open(UTF / "axes/data/unicode-axes.tsv"), delimiter="\t", quoting=csv.QUOTE_NONE):
        v = (r.get("numeric_value") or "").strip()
        if v:
            try:
                if "/" in v:
                    n, d = v.split("/"); NUM[r["char"]] = float(n) / float(d)
                else:
                    NUM[r["char"]] = float(v)
            except Exception:
                pass
    # astral numerics the BMP table cannot carry (python unicodedata, same Unicode 14 data)
    import unicodedata
    for cp in range(0x10000, 0x20000):
        ch = chr(cp)
        try:
            NUM.setdefault(ch, float(unicodedata.numeric(ch)))
        except (ValueError, TypeError):
            pass

def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d; h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))

def fmt_rate(k, n):
    if n == 0:
        return "n/a (0)"
    lo, hi = wilson(k, n)
    return f"{k}/{n} = {k/n:.2f} [{lo:.2f},{hi:.2f}]"

# ------------------------------------------------------------------ loading
def load_stimuli():
    stim = {}
    for f in (EXP / "data/stimuli-v1").glob("*.jsonl"):
        for line in open(f):
            r = json.loads(line); stim[r["pid"]] = r
    return stim

def load_runs(stim):
    """-> list of dicts: run spec + parsed presentations {(rep,pid): (verdict, more, by)} or gestalt parse."""
    runs = []
    for d in sorted((EXP / "data/runs-v1").iterdir()):
        if not d.is_dir() or d.name.endswith("-shakedown") or "-aborted" in d.name:
            continue
        spec = json.load(open(d / "spec.json"))
        parsed, meta = {}, Counter()
        think = []
        if not (d / "ledger.jsonl").exists():
            continue
        for line in open(d / "ledger.jsonl"):
            try:
                row = json.loads(line)
            except Exception:
                meta["corrupt-line"] += 1; continue
            res = row["result"]
            if not res.get("raw") or res.get("error"):
                meta["failed-call"] += 1; continue
            if res.get("usage", {}).get("thinking_tokens") is not None:
                think.append(res["usage"]["thinking_tokens"] / max(1, len(row["pids"])))
            if row["instrument"] in ("gestalt", "signa-gestalt"):
                k = (row["rep"], row["pids"][0])
                if k not in parsed:
                    parsed[k] = I.parse_gestalt(res["raw"], stim[row["pids"][0]]["glyphs"])
                continue
            # rule: per (rep, presentation), the EARLIEST parseable answer in ledger order is used;
            # a presentation with no parseable answer in any call is 'unparsed'.
            if row["mode"] == "single":
                pid = row["pids"][0]; k = (row["rep"], pid)
                if k not in parsed or parsed[k][0] == "unparsed":
                    s = stim[pid]; parsed[k] = I.parse_pair(res["raw"], s["a"], s["b"])
            else:
                items = [{"id": it["id"], "a": stim[it["pid"]]["a"], "b": stim[it["pid"]]["b"]} for it in row["items"]]
                pmap = I.parse_sheet(res["raw"], items)
                for it in row["items"]:
                    k = (row["rep"], it["pid"])
                    if k in parsed and parsed[k][0] != "unparsed":
                        continue
                    parsed[k] = pmap.get(it["id"], ("unparsed", None, None))
        runs.append({"spec": spec, "parsed": parsed, "meta": meta,
                     "mean_thinking": (sum(think) / len(think)) if think else None})
    return runs

# ------------------------------------------------------------------ pair verdicts
def pair_verdict(v1, v2):
    """two presentations of the same unordered pair -> consistent-directed(winner) / perp / tie / mixed / unparsed"""
    if v1[0] == "unparsed" or v2[0] == "unparsed":
        return ("unparsed", None)
    if v1[0] == v2[0] == "dir":
        return ("dir", v1[1]) if v1[1] == v2[1] else ("flip", None)
    if v1[0] == v2[0] == "perp":
        return ("perp", None)
    if v1[0] == v2[0] == "tie":
        return ("tie", None)
    return ("mixed", None)

def correlates(edges):
    """edges: list of (loser, winner) -> dict(value=(k,n), ink=(k,n))"""
    vk = vn = ik = inn = 0
    for l, w in edges:
        if l in NUM and w in NUM:
            if NUM[l] != NUM[w]:
                vn += 1; vk += NUM[w] > NUM[l]
        elif l not in NUM and w not in NUM and l in INK and w in INK and abs(INK[l] - INK[w]) > 0.005:
            inn += 1; ik += INK[w] > INK[l]
    return {"value": (vk, vn), "ink": (ik, inn)}

def judge_name(spec):
    return f"{spec['judge_label']}[{spec['mode']}]"

# ------------------------------------------------------------------ analyses
def analyze_format(runs, stim, out, js):
    out.append("## Format experiment (claim 3; P1–P4)\n")
    by_judge = defaultdict(dict)
    for r in runs:
        if r["spec"]["instrument"] == "format":
            by_judge[judge_name(r["spec"])][r["spec"]["format"]] = r
    out.append("| judge | format | stratum | pairs | consistent-directed | consistent-⟂ | ≈ | mixed/flip | unparsed |")
    out.append("|---|---|---|---|---|---|---|---|---|")
    verdicts = {}  # (judge, fmt) -> {pair: (verdict, winner)}
    for jn in sorted(by_judge):
        for fmt in ("forced", "tie", "perp"):
            r = by_judge[jn].get(fmt)
            if not r:
                continue
            pres = defaultdict(dict)
            for (rep, pid), v in r["parsed"].items():
                s = stim[pid]; pres[(rep, s["pair"])][s["order"]] = (v, s)
            vd = {}
            for (rep, pair), d in pres.items():
                if 0 in d and 1 in d:
                    vd[pair] = pair_verdict(d[0][0], d[1][0]) + (d[0][1]["a"], d[0][1]["b"], d[0][1]["stratum"])
            verdicts[(jn, fmt)] = vd
            for stratum in ("pilot-replication", "fresh-seed-local", "fresh-mixed"):
                c = Counter(v[0] for v in vd.values() if v[4] == stratum)
                n = sum(c.values())
                if n:
                    out.append(f"| {jn} | {fmt} | {stratum} | {n} | {c['dir']/n:.2f} | {c['perp']/n:.2f} | {c['tie']/n:.2f} | "
                               f"{(c['mixed']+c['flip'])/n:.2f} | {c['unparsed']/n:.2f} |")
    out.append("")
    out.append("### P1/P2 — dissolution: pilot-replication pairs consistent-directed under tie (resp. forced) that are consistent-⟂ under perp\n")
    out.append("| judge | tie→perp dissolved | forced→perp dissolved | ⟂ share of perp presentations (all strata) | P3 survival local − mixed (perp) | P4 value-correlate forced vs perp |")
    out.append("|---|---|---|---|---|---|")
    jsf = {}
    for jn in sorted(by_judge):
        row = [jn]
        for src in ("tie", "forced"):
            a = verdicts.get((jn, src)); p = verdicts.get((jn, "perp"))
            if a and p:
                base = [k for k, v in a.items() if v[0] == "dir" and v[4] == "pilot-replication" and k in p]
                dis = sum(1 for k in base if p[k][0] == "perp")
                row.append(fmt_rate(dis, len(base))); jsf.setdefault(jn, {})[f"{src}->perp"] = (dis, len(base))
            else:
                row.append("–")
        pr = by_judge[jn].get("perp")
        if pr:
            c = Counter(v[0] for v in pr["parsed"].values()); n = sum(c.values())
            row.append(fmt_rate(c["perp"], n)); jsf.setdefault(jn, {})["perp_share"] = (c["perp"], n)
            p = verdicts[(jn, "perp")]
            loc = [v for v in p.values() if v[4] == "fresh-seed-local"]; mix = [v for v in p.values() if v[4] == "fresh-mixed"]
            sl = sum(v[0] == "dir" for v in loc) / max(1, len(loc)); sm = sum(v[0] == "dir" for v in mix) / max(1, len(mix))
            row.append(f"{sl:.2f} − {sm:.2f} = {sl-sm:+.2f}"); jsf[jn]["survival_local_minus_mixed"] = sl - sm
        else:
            row += ["–", "–"]
        cells = []
        for fmt in ("forced", "perp"):
            vd = verdicts.get((jn, fmt))
            if vd:
                edges = [((v[2] if v[1] == v[3] else v[3]), v[1]) for v in vd.values() if v[0] == "dir"]
                k, n = correlates(edges)["value"]; cells.append(f"{fmt} {fmt_rate(k, n)}")
                jsf.setdefault(jn, {})[f"value_{fmt}"] = (k, n)
        row.append("; ".join(cells) or "–")
        out.append("| " + " | ".join(row) + " |")
    out.append("")
    js["format"] = jsf

def analyze_triads(runs, stim, out, js):
    out.append("## Triads (claim 4; P5–P8)\n")
    out.append("| judge | presentations | ⟂ | ⟂ (uniform stratum) | unparsed | first-shown share of directed answers | cycle rate (fully oriented sets) | cross-orientation agreement | value-correlate | ink-correlate | mean thinking tok/item |")
    out.append("|---|---|---|---|---|---|---|---|---|---|---|")
    jst = {}
    for r in sorted((r for r in runs if r["spec"]["instrument"] == "triads"), key=lambda r: judge_name(r["spec"])):
        jn = judge_name(r["spec"])
        P = {pid: v for (rep, pid), v in r["parsed"].items() if rep == 0}
        c = Counter(v[0] for v in P.values()); n = sum(c.values())
        cu = Counter(v[0] for pid, v in P.items() if stim[pid]["stratum"] == "uniform"); nu = sum(cu.values())
        nd = sum(1 for v in P.values() if v[0] == "dir"); nfirst = sum(1 for pid, v in P.items() if v[0] == "dir" and v[1] == stim[pid]["a"])
        tri = defaultdict(lambda: defaultdict(dict))
        for pid, v in P.items():
            s = stim[pid]; tri[s["triad"]][s["oset"]][(s["a"], s["b"])] = v
        cyc = full = 0; agree = shared = 0; edges = []
        for t, osets in tri.items():
            for o, rel in osets.items():
                ori = []
                for (a, b), v in rel.items():
                    if v[0] == "dir":
                        ori.append((b, a) if v[1] == a else (a, b))  # (loser, winner)
                if len(rel) == 3 and len(ori) == 3:
                    full += 1
                    outs = Counter(l for l, w in ori); ins = Counter(w for l, w in ori)
                    if all(outs[x] == 1 and ins[x] == 1 for x in set(outs) | set(ins)):
                        cyc += 1
            o0, o1 = osets.get(0, {}), osets.get(1, {})
            for (a, b), v0 in o0.items():
                v1 = o1.get((b, a))
                if v1 is None:
                    continue
                shared += 1
                pv = pair_verdict(v0, v1)
                if pv[0] in ("dir", "perp", "tie"):
                    agree += 1
                if pv[0] == "dir":
                    w = pv[1]; edges.append((b if w == a else a, w))
        cor = correlates(edges)
        jst[jn] = {"n": n, "perp": (c["perp"], n), "perp_uniform": (cu["perp"], nu), "unparsed": (c["unparsed"], n),
                   "cycles": (cyc, full), "agree": (agree, shared), "value": cor["value"], "ink": cor["ink"],
                   "edges": len(edges), "thinking": r["mean_thinking"], "first_shown": (nfirst, nd)}
        th = f"{r['mean_thinking']:.0f}" if r["mean_thinking"] is not None else "–"
        out.append(f"| {jn} | {n} | {fmt_rate(c['perp'], n)} | {fmt_rate(cu['perp'], nu)} | {c['unparsed']/max(n,1):.2f} | {fmt_rate(nfirst, nd)} | "
                   f"{fmt_rate(cyc, full)} | {fmt_rate(agree, shared)} | {fmt_rate(*cor['value'])} | {fmt_rate(*cor['ink'])} | {th} |")
    out.append("")
    js["triads"] = jst

def analyze_conflict(runs, stim, out, js):
    out.append("## Conflict battery (claim 5; P9–P12)\n")
    items = {it["id"]: it for it in json.load(open(EXP / "harness/runner/conflict-items-v1.json"))["items"]}
    groups = {
        "P9 compiled-decode (13 items)": ["roman-8-9", "roman-3-5", "roman-lc-8-9", "roman-lc-3-4", "roman-lc-4-5", "sup9-vs-2",
                                          "sub8-vs-3", "sup7-vs-1", "seg-0-vs-1", "seg-0-vs-7", "frac-8th-vs-half", "frac-9th-vs-3rd", "frac-10th-vs-5th"],
    }
    per = {}
    for r in runs:
        if r["spec"]["instrument"] != "conflict":
            continue
        jn = judge_name(r["spec"]); tally = defaultdict(Counter)
        for (rep, pid), v in r["parsed"].items():
            s = stim[pid]
            tally[s["item"]][v[1] if v[0] == "dir" else v[0]] += 1
        per[jn] = tally
    judges = sorted(per)
    out.append("Per item: committed wins for the item's `a` glyph : `b` glyph, then ≈ / ⟂ / unparsed counts, pooled over both orders × reps.\n")
    out.append("| item | a | b | value-side | " + " | ".join(judges) + " |")
    out.append("|---|---|---|---|" + "---|" * len(judges))
    for iid, it in items.items():
        cells = []
        for jn in judges:
            t = per[jn].get(iid, Counter())
            cells.append(f"{t[it['a']]}:{t[it['b']]} ≈{t['tie']} ⟂{t['perp']}" + (f" ?{t['unparsed']}" if t['unparsed'] else ""))
        vs = it["predict"].get("value", it["predict"].get("lines", ""))
        out.append(f"| {iid} | {it['a']} | {it['b']} | {vs} | " + " | ".join(cells) + " |")
    out.append("")
    # pooled predictions
    def committed(jn, iid, side):
        t = per[jn].get(iid, Counter()); it = items[iid]
        return t[side], t[it["a"]] + t[it["b"]]
    out.append("| judge | P9 value wins (13 compiled-decode items) | P10a ☷ over ⚌ | P10b yang/ink side on equal-line grams | P11 ‱ over % and ‰ | P12 ≈/⟂ on equal-value probes |")
    out.append("|---|---|---|---|---|---|")
    jsc = {}
    for jn in judges:
        k = n = 0
        for iid in groups["P9 compiled-decode (13 items)"]:
            a, b = committed(jn, iid, items[iid]["predict"]["value"]); k += a; n += b
        a10, n10 = committed(jn, "gram-earth-vs-gyang", "☷")
        kb = nb = 0
        for iid, side in (("gram-earth-vs-heaven", "☰"), ("gram-yin-vs-yang", "⚊"), ("gram-gyin-vs-gyang", "⚌")):
            a, b = committed(jn, iid, side); kb += a; nb += b
        k11 = n11 = 0
        for iid in ("permille-mille-vs-myriad", "permille-pct-vs-myriad"):
            a, b = committed(jn, iid, "‱"); k11 += a; n11 += b
        k12 = n12 = 0
        for iid in ("sup9-vs-9-equal", "die5-vs-5-equal"):
            t = per[jn].get(iid, Counter()); k12 += t["tie"] + t["perp"]; n12 += sum(t.values())
        jsc[jn] = {"P9": (k, n), "P10a": (a10, n10), "P10b": (kb, nb), "P11": (k11, n11), "P12": (k12, n12)}
        out.append(f"| {jn} | {fmt_rate(k, n)} | {fmt_rate(a10, n10)} | {fmt_rate(kb, nb)} | {fmt_rate(k11, n11)} | {fmt_rate(k12, n12)} |")
    out.append("")
    js["conflict"] = jsc

def kendall_abs(order, ref):
    common = [g for g in order if g in ref]
    if len(common) < 2:
        return None
    pos = {g: i for i, g in enumerate(ref)}
    conc = disc = 0
    for x, y in combinations(common, 2):
        s = (pos[x] - pos[y])
        if s == 0:
            continue
        if s < 0:
            conc += 1
        else:
            disc += 1
    tot = conc + disc
    return abs(conc - disc) / tot if tot else None

def analyze_holistic(runs, stim, out, js):
    out.append("## Holistic sequences (claim 2; P13–P15)\n")
    pairw = defaultdict(dict)
    for r in runs:
        if r["spec"]["instrument"] != "holistic":
            continue
        jn = judge_name(r["spec"]); pres = defaultdict(dict)
        for (rep, pid), v in r["parsed"].items():
            s = stim[pid]; key = (s["seq"], frozenset((s["a"], s["b"])))
            pres[key][s["order"]] = (v, s)
        for (seq, _), d in pres.items():
            if 0 in d and 1 in d:
                pv = pair_verdict(d[0][0], d[1][0])
                s0 = d[0][1]
                agree_dir = None
                if pv[0] == "dir":
                    ia, ib = s0["intended"]; hi = s0["a"] if ia > ib else s0["b"]
                    agree_dir = (pv[1] == hi)
                pairw[jn].setdefault(seq, []).append((pv[0], agree_dir))
    gest = defaultdict(dict)
    for r in runs:
        if r["spec"]["instrument"] != "gestalt":
            continue
        jn = r["spec"]["judge_label"]
        per = defaultdict(list)
        for (rep, pid), g in r["parsed"].items():
            s = stim[pid]; per[s["seq"]].append((s, g))
        for seq, lst in per.items():
            taus = []; perp = 0; arrangements = []
            for s, g in lst:
                if g.get("kind") == "perp":
                    perp += 1; arrangements.append("⟂")
                elif g.get("kind") == "order":
                    t = kendall_abs(g["order"], s["intended"])
                    taus.append(t if t is not None else 0.0); arrangements.append("".join(g["order"]))
                else:
                    arrangements.append("?")
            gest[jn][seq] = {"tau": (sum(taus) / len(taus)) if taus else None, "perp": perp, "n": len(lst),
                             "self_consistent": len(set(arrangements)) == 1, "arr": arrangements}
    sets = [s["name"] for s in json.load(open(EXP / "harness/runner/holistic-sets-v1.json"))["sets"]] + [f"noise-{i}" for i in range(4)]
    judges = sorted(set(gest) | {j.split("[")[0] for j in pairw})
    out.append("Gestalt: mean |τ| over the 3 shuffles (⟂ count / 3); `=` marks all three arrangements identical. Pairwise: consistent-directed share of the set's pairs (single or sheet mode as run), and in brackets the share of those directed pairs that agree with the reference direction.\n")
    out.append("| set | " + " | ".join(judges) + " |")
    out.append("|---|" + "---|" * len(judges))
    jsh = {}
    for seq in sets:
        cells = []
        for jl in judges:
            g = gest.get(jl, {}).get(seq)
            gs = "–"
            if g:
                gs = (f"{g['tau']:.2f}" if g["tau"] is not None else "–") + f" (⟂{g['perp']})" + ("=" if g["self_consistent"] else "")
            pw = [v for jn, d in pairw.items() if jn.split("[")[0] == jl and "[single]" in jn for v in d.get(seq, [])] or \
                 [v for jn, d in pairw.items() if jn.split("[")[0] == jl for v in d.get(seq, [])]
            ps = ""
            if pw:
                nd = sum(1 for v in pw if v[0] == "dir"); agr = sum(1 for v in pw if v[1])
                ps = f" · pw {nd/len(pw):.2f}" + (f" [{agr/nd:.2f}]" if nd else "")
            cells.append(gs + ps)
            jsh.setdefault(jl, {})[seq] = {"gestalt": g, "pairwise": pw}
        out.append(f"| {seq} | " + " | ".join(cells) + " |")
    out.append("")
    js["holistic"] = {j: {s: {"tau": (v["gestalt"] or {}).get("tau"), "perp": (v["gestalt"] or {}).get("perp"),
                               "pw_dir": (sum(1 for x in v["pairwise"] if x[0] == "dir") / len(v["pairwise"])) if v["pairwise"] else None}
                           for s, v in d.items()} for j, d in jsh.items()}


def analyze_seed_retest(runs, stim, out, js):
    """Graduation-by-retest of survey anecdotes (exploratory): for seed-local triads, do the judges'
    consistent-directed edges agree with the surveyor's WRITTEN linearization of that record
    (direction-agnostic per triad: all directed edges ascending in written order, or all descending)?"""
    out.append("## Seed retest — do v1.0 judges recover the surveyors' written orders? (exploratory)\n")
    pool = json.load(open(EXP / "data/stimuli-v1/pool.json"))
    recs = {r["rec"]: r for r in pool["seed_records"]}
    out.append("Per seed-local triad (120): *ordered* = at least two of its three pairs are consistent-directed; "
               "*agrees* = every consistent-directed pair runs the same way along the record's written glyph order. "
               "Surveyor = the record's source survey.\n")
    out.append("| judge | triads ordered | ordered triads agreeing with written order | by surveyor (agree/ordered) |")
    out.append("|---|---|---|---|")
    jss = {}
    for r in sorted((r for r in runs if r["spec"]["instrument"] == "triads"), key=lambda r: judge_name(r["spec"])):
        jn = judge_name(r["spec"])
        tri = defaultdict(lambda: defaultdict(dict))
        for (rep, pid), v in r["parsed"].items():
            sv = stim[pid]
            if rep == 0 and sv["stratum"] == "seed-local":
                tri[sv["triad"]][sv["oset"]][(sv["a"], sv["b"])] = (v, sv)
        ordered = agree = 0; bys = defaultdict(lambda: [0, 0])
        for t, os_ in tri.items():
            o0, o1 = os_.get(0, {}), os_.get(1, {})
            rec = None; signs = []
            for (a, b), (v0, sv) in o0.items():
                rec = recs[sv["src"][0]]
                x = o1.get((b, a))
                if not x:
                    continue
                pv = pair_verdict(v0, x[0])
                if pv[0] == "dir":
                    g = rec["glyphs"]; lo = b if pv[1] == a else a
                    signs.append(1 if g.index(pv[1]) > g.index(lo) else -1)
            if rec is None or len(signs) < 2:
                continue
            ordered += 1; ok = len(set(signs)) == 1; agree += ok
            bys[rec["surveyor"]][0] += ok; bys[rec["surveyor"]][1] += 1
        jss[jn] = {"ordered": ordered, "agree": agree, "by_surveyor": dict(bys)}
        bs = ", ".join(f"{k} {v[0]}/{v[1]}" for k, v in sorted(bys.items()))
        out.append(f"| {jn} | {ordered}/120 | {fmt_rate(agree, ordered)} | {bs} |")
    out.append("")
    js["seed_retest"] = jss

def analyze_strata(runs, stim, out, js):
    out.append("## Triads by stratum (⟂ share; cycle rate) — exploratory breakdown\n")
    out.append("| judge | seed-local ⟂ | seed-cross ⟂ | uniform ⟂ | seed-local cycles | seed-cross cycles |")
    out.append("|---|---|---|---|---|---|")
    for r in sorted((r for r in runs if r["spec"]["instrument"] == "triads"), key=lambda r: judge_name(r["spec"])):
        jn = judge_name(r["spec"]); cells = []
        P = {pid: v for (rep, pid), v in r["parsed"].items() if rep == 0}
        for st in ("seed-local", "seed-cross", "uniform"):
            c = Counter(v[0] for pid, v in P.items() if stim[pid]["stratum"] == st); n = sum(c.values())
            cells.append(f"{c['perp']/max(n,1):.2f} (n={n})")
        for st in ("seed-local", "seed-cross"):
            tri = defaultdict(lambda: defaultdict(dict))
            for pid, v in P.items():
                sv = stim[pid]
                if sv["stratum"] == st:
                    tri[sv["triad"]][sv["oset"]][(sv["a"], sv["b"])] = v
            cyc = full = 0
            for t, os_ in tri.items():
                for o, rel in os_.items():
                    ori = [((b, a) if v[1] == a else (a, b)) for (a, b), v in rel.items() if v[0] == "dir"]
                    if len(rel) == 3 and len(ori) == 3:
                        full += 1
                        outs = Counter(l for l, w in ori); ins = Counter(w for l, w in ori)
                        cyc += all(outs[x] == 1 and ins[x] == 1 for x in set(outs) | set(ins))
            cells.append(fmt_rate(cyc, full))
        out.append(f"| {jn} | " + " | ".join(cells) + " |")
    out.append("")

def analyze_signa(runs, stim, out, js):
    """Consumer probe (not registered): the aspectus/SIGNA age ladder as single glyphs."""
    SIG = ["·", "╶", "╌", "╍", "━", "═", "⚬", "○", "◎", "◉", "⬤"]
    out.append("## Consumer probe — SIGNA ladder `" + "".join(SIG) + "` (not registered; exploratory)\n")
    out.append("Per judge: of the 55 pairs, how many are consistent-directed (both orders agree), how many of those run the SIGNA way, "
               "the perceived order by Copeland score (wins − losses over consistent-directed pairs; ties keep SIGNA order), "
               "and the adjacent SIGNA steps that judges did NOT confirm (⟂/≈/mixed or reversed). Gestalt = mean |τ| over 3 shuffles.\n")
    out.append("| judge | directed / 55 | SIGNA-direction share | perceived order (Copeland) | adjacent steps not confirmed | gestalt |τ| (⟂) |")
    out.append("|---|---|---|---|---|---|")
    gest = {}
    for r in runs:
        if r["spec"]["instrument"] == "signa-gestalt":
            taus = []; perp = 0
            for (rep, pid), g in r["parsed"].items():
                if g.get("kind") == "perp": perp += 1
                elif g.get("kind") == "order":
                    t = kendall_abs(g["order"], SIG); taus.append(t if t is not None else 0.0)
            gest[r["spec"]["judge_label"]] = ((sum(taus) / len(taus)) if taus else None, perp)
    jsg = {}
    for r in sorted((r for r in runs if r["spec"]["instrument"] == "signa"), key=lambda r: judge_name(r["spec"])):
        jn = judge_name(r["spec"]); pres = defaultdict(dict)
        for (rep, pid), v in r["parsed"].items():
            sv = stim[pid]; pres[frozenset((sv["a"], sv["b"]))][sv["order"]] = (v, sv)
        score = Counter(); nd = agree = 0; verdict = {}
        for k, d in pres.items():
            if 0 in d and 1 in d:
                pv = pair_verdict(d[0][0], d[1][0]); verdict[k] = pv
                if pv[0] == "dir":
                    nd += 1; w = pv[1]; l = next(iter(k - {w}))
                    score[w] += 1; score[l] -= 1; agree += SIG.index(w) > SIG.index(l)
        order = sorted(SIG, key=lambda g: (score[g], SIG.index(g)))
        miss = []
        for x, y in zip(SIG, SIG[1:]):
            pv = verdict.get(frozenset((x, y)))
            if not pv or pv[0] != "dir" or pv[1] != y:
                miss.append(f"{x}{y}:" + ("rev" if pv and pv[0] == "dir" else (pv[0] if pv else "?")))
        g = gest.get(r["spec"]["judge_label"])
        gs = f"{g[0]:.2f} (⟂{g[1]})" if g and g[0] is not None else (f"– (⟂{g[1]})" if g else "–")
        out.append(f"| {jn} | {nd} | {fmt_rate(agree, nd)} | `{''.join(order)}` | {' '.join(miss) or 'none'} | {gs} |")
        jsg[jn] = {"directed": nd, "agree": agree, "order": "".join(order), "unconfirmed_adjacent": miss, "gestalt": g}
    out.append("")
    js["signa"] = jsg

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(EXP / "analysis/v1.0-results.md"))
    ap.add_argument("--json", default=str(EXP / "analysis/v1.0-results.json"))
    a = ap.parse_args()
    load_features()
    stim = load_stimuli(); runs = load_runs(stim)
    out = ["# v1.0 results — generated by harness/runner/analyze_v1.py (do not hand-edit)\n",
           f"Runs included: {len(runs)} (shakedown excluded). Parser {I.PARSER_VERSION}. Rates are point [95% Wilson].\n"]
    out.append("| run | calls ok | failed calls | presentations parsed | unparsed |")
    out.append("|---|---|---|---|---|")
    for r in runs:
        c = Counter((v[0] if isinstance(v, tuple) else v.get("kind")) for v in r["parsed"].values())
        out.append(f"| {r['spec']['run_id']} | – | {r['meta'].get('failed-call', 0)} | {sum(c.values())} | {c.get('unparsed', 0)} |")
    out.append("")
    js = {}
    analyze_format(runs, stim, out, js)
    analyze_triads(runs, stim, out, js)
    analyze_conflict(runs, stim, out, js)
    analyze_holistic(runs, stim, out, js)
    analyze_strata(runs, stim, out, js)
    analyze_seed_retest(runs, stim, out, js)
    analyze_signa(runs, stim, out, js)
    pathlib.Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    open(a.out, "w").write("\n".join(out) + "\n")
    json.dump(js, open(a.json, "w"), ensure_ascii=False, indent=1, default=str)
    print(f"wrote {a.out} and {a.json}")

if __name__ == "__main__":
    main()
