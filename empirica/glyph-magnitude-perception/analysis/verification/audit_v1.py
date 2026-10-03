#!/usr/bin/env python3
"""Independent re-derivation of the v1.0 campaign numbers (audit 2026-10-03, v1.0 pass).

Written from scratch: own ledger loader, own answer parser, own verdict/statistic code. It imports
harness/runner/instruments.py ONLY in section 1, to diff the harness parser against this one
presentation by presentation; every later number comes from this file's own parser.

Read-only over data/ and harness/. Prints to stdout. Local-model ledgers are still being appended
while this runs; the snapshot it reads is whatever is on disk at run time (it prints line counts).

  python3 analysis/verification/audit_v1.py [section ...]     (no args = all sections)
"""
import csv, glob, json, math, os, pathlib, re, sys, unicodedata
from collections import Counter, defaultdict
from itertools import combinations

EXP = pathlib.Path(__file__).resolve().parents[2]
UTF = pathlib.Path.home() / "src/arch/firmatum/utils/utf"
csv.field_size_limit(10**9)
SECTIONS = set(sys.argv[1:])
def want(s): return not SECTIONS or s in SECTIONS

# ---------------------------------------------------------------- features (own load)
INK, UNUM = {}, {}
for r in csv.DictReader(open(UTF / "bmp-metrics-ghostty.tsv"), delimiter="\t", quoting=csv.QUOTE_NONE):
    try: INK[r["char"]] = float(r["packed_density"])
    except Exception: pass
FACE = {}
for r in csv.DictReader(open(UTF / "bmp-metrics-ghostty.tsv"), delimiter="\t", quoting=csv.QUOTE_NONE):
    FACE[r["char"]] = (r["used_face"], r["cells"])
def unum(ch):
    if len(ch) != 1: return None
    try: return float(unicodedata.numeric(ch))
    except Exception: return None

def wilson(k, n, z=1.96):
    if not n: return (float("nan"),) * 2
    p = k / n; d = 1 + z*z/n; c = (p + z*z/(2*n)) / d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
    return (max(0, c-h), min(1, c+h))
def R(k, n): return f"{k}/{n} = {k/n:.2f} [{wilson(k,n)[0]:.2f},{wilson(k,n)[1]:.2f}]" if n else f"{k}/0"

# ---------------------------------------------------------------- stimuli + ledgers (own load)
STIM = {}
for f in (EXP / "data/stimuli-v1").glob("*.jsonl"):
    for line in open(f):
        r = json.loads(line); STIM[r["pid"]] = r

def runs():
    out = {}
    for d in sorted((EXP / "data/runs-v1").iterdir()):
        if not d.is_dir() or "shakedown" in d.name or "aborted" in d.name: continue
        led = d / "ledger.jsonl"
        if not led.exists(): out[d.name] = (json.load(open(d / "spec.json")), []); continue
        rows = []
        for line in open(led):
            try: rows.append(json.loads(line))
            except Exception: pass
        out[d.name] = (json.load(open(d / "spec.json")), rows)
    return out
RUNS = runs()

# ---------------------------------------------------------------- own parser
PERPS = ("⟂", "⊥")
def classify(text, a, b, fieldnames=False):
    """-> ('dir', glyph) | ('perp',) | ('tie',) | ('amb', why) | ('none',)"""
    t = (text or "").strip()
    t = re.sub(r"^```\w*\s*|\s*```$", "", t).strip()
    if not t: return ("none",)
    # whole answer is exactly a glyph (most common case), possibly with a trailing ", by"
    head = re.split(r"\s*[,;]\s*|\s+", t, maxsplit=1)[0]
    for g in (a, b):
        if head == g or head.strip("*`'\"") == g: return ("dir", g)
    low = t.lower()
    words = re.findall(r"[a-z]+", low)
    w0 = words[0] if words else ""
    ha, hb = (a in t), (b in t)
    hp = any(p in t for p in PERPS) or w0 in ("none", "neither")
    ht = "≈" in t or w0 in ("equal", "same")
    hf = w0 in ("first",) or (fieldnames and w0 == "a" and len(t.strip("\"' ")) <= 1)
    hs = w0 in ("second",) or (fieldnames and w0 == "b" and len(t.strip("\"' ")) <= 1)
    sig = [x for x, on in (("a", ha), ("b", hb), ("perp", hp), ("tie", ht), ("first", hf), ("second", hs)) if on]
    if sig == ["a"] or sig == ["first"]: return ("dir", a)
    if sig == ["b"] or sig == ["second"]: return ("dir", b)
    if sig == ["perp"]: return ("perp",)
    if sig == ["tie"]: return ("tie",)
    if not sig: return ("none",)
    return ("amb", "+".join(sig))

def sheet_answers(raw):
    """last parseable {"answers": [...]} object; returns list or None"""
    if not raw: return None
    dec = json.JSONDecoder()
    for st in reversed([m.start() for m in re.finditer(r'\{\s*"answers"\s*:', raw)]):
        try:
            d, _ = dec.raw_decode(raw[st:]); return d.get("answers")
        except Exception: continue
    return None

def presentations(rows, earliest=True):
    """-> {(rep, pid): ('dir', g)|('perp',)|('tie',)|('amb',..)|('none',)} using the earliest call that
    yields a classifiable answer for that presentation; ('missing',) if no call carried it at all."""
    out = {}
    for r in rows:
        res = r["result"]; raw = res.get("raw")
        if not raw or res.get("error"): continue
        if r["mode"] == "single":
            pid = r["pids"][0]; s = STIM[pid]
            if "a" not in s: continue
            v = classify(raw, s["a"], s["b"])
            k = (r["rep"], pid)
            if k not in out or out[k][0] in ("none", "amb", "missing"): out[k] = v
        else:
            ans = sheet_answers(raw) or []
            byid = {x.get("id"): x for x in ans if isinstance(x, dict)}
            for it in r["items"]:
                s = STIM[it["pid"]]; k = (r["rep"], it["pid"])
                x = byid.get(it["id"])
                v = ("missing",) if x is None else classify(str(x.get("more", "")), s["a"], s["b"], fieldnames=True)
                if k not in out or out[k][0] in ("none", "amb", "missing"): out[k] = v
    return out

def ok(v): return v[0] in ("dir", "perp", "tie")
def pv(v0, v1):
    if not ok(v0) or not ok(v1): return ("unk",)
    if v0[0] == v1[0] == "dir": return ("dir", v0[1]) if v0[1] == v1[1] else ("flip",)
    if v0[0] == v1[0]: return (v0[0],)
    return ("mixed",)

def label(name, spec): return f"{spec['judge_label']}[{spec['mode']}]"
FRONTIER = {"haiku45", "sonnet5", "sonnet55", "opus55", "grok46", "gpt56terra", "gemini31pro", "gemini38flash"}
CLAUDE = {"haiku45", "sonnet5", "sonnet55", "opus55"}
SMALL = {"llama32-3b", "qwen3-4b", "gemma3-4b", "phi4mini"}

P = {name: presentations(rows) for name, (spec, rows) in RUNS.items() if rows and RUNS[name][0]["instrument"] not in ("gestalt", "signa-gestalt", "top40-gestalt", "top40b-gestalt")}

# ================================================================ 0. snapshot
if want("0"):
    print("## 0. snapshot")
    print("runs with ledgers:", sum(1 for _, (s, r) in RUNS.items() if r), " without:", [n for n, (s, r) in RUNS.items() if not r])
    for n in ("triads-perp-single-phi4mini", "triads-perp-single-hermes3-3b", "triads-perp-single-gptoss20b"):
        print(f"  {n}: {len(RUNS.get(n, ({}, []))[1])} ledger rows")
    labs = sorted({s["judge_label"] for s, r in RUNS.values() if r})
    print("judge labels with any data:", labs, len(labs))

# ================================================================ 1. parser diff
if want("1"):
    sys.path.insert(0, str(EXP / "harness/runner")); import instruments as I
    print("\n## 1. harness parser (p1.2) vs this parser, per presentation (pair instruments)")
    tot = Counter(); ex = defaultdict(list)
    for name, (spec, rows) in RUNS.items():
        if name not in P: continue
        theirs = {}
        for r in rows:
            res = r["result"]
            if not res.get("raw") or res.get("error"): continue
            if r["mode"] == "single":
                s = STIM[r["pids"][0]]; k = (r["rep"], r["pids"][0])
                if k not in theirs or theirs[k][0] == "unparsed": theirs[k] = I.parse_pair(res["raw"], s["a"], s["b"])
            else:
                items = [{"id": it["id"], "a": STIM[it["pid"]]["a"], "b": STIM[it["pid"]]["b"]} for it in r["items"]]
                pm = I.parse_sheet(res["raw"], items)
                for it in r["items"]:
                    k = (r["rep"], it["pid"])
                    if k in theirs and theirs[k][0] != "unparsed": continue
                    theirs[k] = pm.get(it["id"], ("unparsed", None, None))
        mine = P[name]
        for k in set(theirs) | set(mine):
            t = theirs.get(k, ("unparsed", None)); m = mine.get(k, ("missing",))
            tk = ("dir", t[1]) if t[0] == "dir" else (t[0],)
            mk = m if m[0] == "dir" else (m[0],)
            if tk == mk or (t[0] == "unparsed" and m[0] in ("none", "missing", "amb")):
                tot["agree"] += 1; continue
            tot["disagree"] += 1
            if len(ex[name]) < 4:
                ex[name].append((t[:2], m))
    print(" ", dict(tot))
    for n, e in sorted(ex.items()):
        print(f"  {n}: {e}")
    # ambiguity census in my parser (answers carrying two signals)
    amb = Counter()
    for n, d in P.items():
        for v in d.values():
            if v[0] == "amb": amb[(n, v[1])] += 1
    print("  answers carrying >1 signal (this parser leaves them unclassified; harness resolves them):")
    for (n, why), c in sorted(amb.items(), key=lambda x: -x[1])[:15]:
        print(f"    {n}: {why} x{c}")

# ================================================================ 2. sheet completeness gate
if want("2"):
    print("\n## 2. sheet-completeness gate: flagged rows and whether they were ever re-asked")
    for name, (spec, rows) in RUNS.items():
        flagged = [r for r in rows if r.get("sheet_incomplete") is not None]
        if not flagged: continue
        later = Counter()
        for r in flagged:
            again = [x for x in rows if x["pids"] == r["pids"] and x["rep"] == r["rep"] and x["ts"] > r["ts"]]
            later["re-asked" if again else "never re-asked"] += 1
        zero = sum(1 for r in flagged if r["sheet_incomplete"] == 0.0)
        miss = Counter(v[0] for v in P.get(name, {}).values())["missing"]
        print(f"  {name}: flags {[r['sheet_incomplete'] for r in flagged]} -> {dict(later)}; coverage-0 rows {zero}; presentations with no answer now: {miss}")

# ================================================================ helpers for format
def format_verdicts(name):
    d = P[name]; pres = defaultdict(dict)
    for (rep, pid), v in d.items():
        s = STIM[pid]; pres[s["pair"]][s["order"]] = (v, s)
    out = {}
    for pair, o in pres.items():
        if 0 in o and 1 in o:
            out[pair] = (pv(o[0][0], o[1][0]), o[0][1])
        else:
            out[pair] = (("unk",), (o.get(0) or o.get(1))[1])
    # pairs never presented at all
    return out

FMT = defaultdict(dict)
for name, (spec, rows) in RUNS.items():
    if rows and spec["instrument"] == "format" and name in P:
        FMT[label(name, spec)][spec["format"]] = format_verdicts(name)

# ================================================================ 3. P1 with and without unparsed imputation
if want("3"):
    print("\n## 3. P1 dissolution on pilot-replication: as scored (unknown perp verdict counted as not dissolved) vs unknowns excluded")
    for j in sorted(FMT):
        t, p = FMT[j].get("tie"), FMT[j].get("perp")
        if not t or not p: continue
        base = [k for k, (v, s) in t.items() if v[0] == "dir" and s["stratum"] == "pilot-replication"]
        dis = sum(1 for k in base if k in p and p[k][0][0] == "perp")
        known = [k for k in base if k in p and p[k][0][0] != "unk"]
        dk = sum(1 for k in known if p[k][0][0] == "perp")
        print(f"  {j:24s} as-scored {R(dis, len(base))}   unknowns excluded {R(dk, len(known))}")

# ================================================================ 4. pilot walk2/walk3 on exactly the 160 pilot-replication pairs
if want("4"):
    print("\n## 4. the pilot's own walk2->walk3 outcome on the 160 pilot-replication pairs")
    J = EXP / "data/judgments-v0"
    def walk(fname):
        out = {}
        for e in json.load(open(J / fname))["result"]["walk"]:
            key = json.load(open(J / f"walk2-key-{e['chunk']}.json"))
            ans = {a["id"]: a["more"] for a in (e["answers"] or [])}
            by = defaultdict(list)
            for s in key["sheet"]:
                by[s["pair"]].append((s["a"], s["b"], ans.get(s["id"])))
            for p, pres in by.items():
                (a, b, x0), (_, _, x1) = pres
                out[frozenset((a, b))] = (x0, x1)
        return out
    w2, w3 = walk("w2ojawgjt.json"), walk("wlj4rajuj.json")
    rep = {}
    for s in STIM.values():
        if s.get("set") == "format" and s["stratum"] == "pilot-replication":
            rep[s["pair"]] = frozenset((s["a"], s["b"]))
    def vd(x):
        x0, x1 = x
        if x0 is None or x1 is None: return "unk"
        if x0 == x1: return {"⟂": "perp", "≈": "tie"}.get(x0, "dir:" + x0)
        return "mixed"
    found = [rep[k] for k in rep if rep[k] in w2]
    print(f"  pilot-replication pairs found in walk2 sheets: {len(found)}/{len(rep)}; in walk3: {sum(1 for k in rep.values() if k in w3)}")
    v2 = Counter(vd(w2[f])[:3] for f in found)
    print("  walk2 verdicts on them:", dict(v2))
    base = [f for f in found if vd(w2[f]).startswith("dir")]
    d = sum(1 for f in base if f in w3 and vd(w3[f]) == "perp")
    print(f"  pilot dissolution on these pairs: {R(d, len(base))}")
    perp_pres = sum(1 for f in found if f in w3 for x in w3[f] if x == "⟂"); allp = sum(1 for f in found if f in w3 for x in w3[f] if x is not None)
    print(f"  pilot walk3 ⟂ share of presentations on these pairs: {R(perp_pres, allp)}")
    # v1.0 per-presentation ⟂ share restricted to the same stratum
    for j in sorted(FMT):
        if not (j.startswith("sonnet") or "pilotcond" in j): continue
        for name, (spec, rows) in RUNS.items():
            if spec["instrument"] == "format" and spec["format"] == "perp" and label(name, spec) == j:
                c = Counter(v[0] for (rep_, pid), v in P[name].items() if STIM[pid]["stratum"] == "pilot-replication")
                n = sum(c.values())
                print(f"  {j:24s} ⟂ share of perp presentations, pilot-replication stratum only: {R(c['perp'], n)}")

# ================================================================ 5. triads: cycles, position bias, correlates
TRI = {}
for name, (spec, rows) in RUNS.items():
    if rows and spec["instrument"] == "triads": TRI[label(name, spec)] = P[name]
if want("5"):
    print("\n## 5. triads")
    for j in sorted(TRI):
        d = {pid: v for (rep, pid), v in TRI[j].items() if rep == 0}
        tri = defaultdict(lambda: defaultdict(dict))
        for pid, v in d.items():
            s = STIM[pid]; tri[s["triad"]][s["oset"]][(s["a"], s["b"])] = v
        full = cyc = 0; pat = Counter(); first = dirn = 0
        for pid, v in d.items():
            if v[0] == "dir":
                dirn += 1; first += v[1] == STIM[pid]["a"]
        edges = []; agree = shared = known = 0
        for t, os_ in tri.items():
            for o, rel in os_.items():
                if len(rel) == 3 and all(v[0] == "dir" for v in rel.values()):
                    full += 1
                    wins = Counter(v[1] for v in rel.values())
                    is_cyc = all(c == 1 for c in wins.values()) and len(wins) == 3
                    cyc += is_cyc
                    pos = "".join("1" if v[1] == a else "2" for (a, b), v in rel.items())
                    kind = "all-first" if pos == "111" else "all-second" if pos == "222" else "mixed-pos"
                    pat[(is_cyc, kind)] += 1
            o0, o1 = os_.get(0, {}), os_.get(1, {})
            for (a, b), v0 in o0.items():
                v1 = o1.get((b, a))
                if v1 is None: continue
                shared += 1; x = pv(v0, v1)
                if x[0] != "unk":
                    known += 1; agree += x[0] in ("dir", "perp", "tie")
                if x[0] == "dir": edges.append((b if x[1] == a else a, x[1]))
        vk = vn = ik = inn = 0; vn_letters = 0
        for l, w in edges:
            nl, nw = unum(l), unum(w)
            if nl is not None and nw is not None and nl != nw:
                vn += 1; vk += nw > nl
            elif nl is None and nw is None and l in INK and w in INK and abs(INK[l] - INK[w]) > 0.005:
                inn += 1; ik += INK[w] > INK[l]
        uniq = len({frozenset(e) for e in edges})
        print(f"  {j:22s} cycles {R(cyc, full)}  first-shown {R(first, dirn)}  value {R(vk, vn)}  ink {R(ik, inn)}  "
              f"x-orient agree (all) {R(agree, shared)} (known only) {R(agree, known)}  edges {len(edges)} unique-pairs {uniq}")
        if j in ("sonnet5[single]", "qwen3-4b[single]", "llama32-3b[single]", "gemma3-4b[single]", "haiku45[single]"):
            print("      fully-oriented sets by (is_cycle, position pattern):", dict(pat))

# ================================================================ 6. conflict per item
if want("6"):
    print("\n## 6. conflict battery: per-item value-side share of committed answers, frontier runs")
    items = {it["id"]: it for it in json.load(open(EXP / "harness/runner/conflict-items-v1.json"))["items"]}
    P9 = ["roman-8-9", "roman-3-5", "roman-lc-8-9", "roman-lc-3-4", "roman-lc-4-5", "sup9-vs-2", "sub8-vs-3", "sup7-vs-1",
          "seg-0-vs-1", "seg-0-vs-7", "frac-8th-vs-half", "frac-9th-vs-3rd", "frac-10th-vs-5th"]
    tal = {}
    for name, (spec, rows) in RUNS.items():
        if rows and spec["instrument"] == "conflict":
            t = defaultdict(Counter)
            for (rep, pid), v in P[name].items():
                t[STIM[pid]["item"]][v[1] if v[0] == "dir" else v[0]] += 1
            tal[label(name, spec)] = t
    fr = [j for j in sorted(tal) if j.split("[")[0] in FRONTIER]
    print("  measured ink (packed_density, face) for the P9 items, value side first:")
    for iid in P9:
        it = items[iid]; vs = it["predict"]["value"]; os_ = it["a"] if vs == it["b"] else it["b"]
        print(f"    {iid:18s} value-side {vs} ink {INK.get(vs)} {FACE.get(vs, ('astral',))[0]} | other {os_} ink {INK.get(os_)} {FACE.get(os_, ('astral',))[0]}")
    print("  items where a frontier run gives the value side < 50% of its committed answers:")
    for iid in P9:
        it = items[iid]; vs = it["predict"]["value"]; os_ = it["a"] if vs == it["b"] else it["b"]
        bad = [(j, tal[j][iid][vs], tal[j][iid][os_]) for j in fr if tal[j][iid][vs] + tal[j][iid][os_] and tal[j][iid][vs] < tal[j][iid][os_]]
        if bad: print(f"    {iid}: {bad}")
    print("  pooled-over-frontier readings of P10-P13 (registered text says 'of committed frontier answers' / 'of frontier presentations'):")
    def pool(iids, side=None, kinds=None):
        k = n = 0
        for j in fr:
            for iid in iids:
                t = tal[j][iid]; it = items[iid]
                if side:
                    k += t[side]; n += t[it["a"]] + t[it["b"]]
                else:
                    k += sum(t[x] for x in kinds); n += sum(t.values())
        return k, n
    print("    P10a ☷>⚌", R(*pool(["gram-earth-vs-gyang"], "☷")))
    kb = nb = 0
    for iid, side in (("gram-earth-vs-heaven", "☰"), ("gram-yin-vs-yang", "⚊"), ("gram-gyin-vs-gyang", "⚌")):
        k, n = pool([iid], side); kb += k; nb += n
    print("    P10b yang side on equal-line", R(kb, nb))
    k1, n1 = pool(["permille-mille-vs-myriad"], "‱"); k2, n2 = pool(["permille-pct-vs-myriad"], "‱")
    print("    P11 ‱ over % and ‰", R(k1 + k2, n1 + n2))
    print("    P12 ≈/⟂ on equal-value probes", R(*pool(["sup9-vs-9-equal", "die5-vs-5-equal"], kinds=("tie", "perp"))))
    print("  SIZE claim check, dots3-vs-disc per frontier run (⁖:●):", {j: (tal[j]["dots3-vs-disc"]["⁖"], tal[j]["dots3-vs-disc"]["●"]) for j in fr})

# ================================================================ 7. held-out hygiene of the stimuli actually run
if want("7"):
    print("\n## 7. stimulus hygiene and held-out property (independent pilot-glyph census)")
    J = EXP / "data/judgments-v0"
    pilot = set()
    for f in J.glob("*.json"):
        pilot |= {ch for ch in f.read_text() if ord(ch) > 0x7F}   # every file, including workflow outputs (broader than the builder's census)
    for f in (EXP / "pilot").glob("results*.jsonl"):
        pilot |= {ch for ch in f.read_text() if ord(ch) > 0x7F}
    banned = {"≈", "⟂", "⊥"}
    by = defaultdict(Counter)
    for s in STIM.values():
        st = s.get("stratum") or s.get("set")
        gl = [s["a"], s["b"]] if "a" in s else s.get("glyphs", [])
        for g in gl:
            if g in banned: by[(s["set"], st)]["BANNED"] += 1
            if s["set"] in ("triads", "format") and st in ("seed-local", "seed-cross", "uniform", "fresh-seed-local", "fresh-mixed"):
                if g in pilot: by[(s["set"], st)]["in-any-pilot-file"] += 1
                if all(ord(c) < 0x80 for c in g): by[(s["set"], st)]["ASCII"] += 1
    print("  ", {k: dict(v) for k, v in by.items()} or "clean")
    # sheet co-occurrence: both orders of a pair / both osets of a triad in one sheet
    viol = Counter()
    for name, (spec, rows) in RUNS.items():
        for r in rows:
            if r.get("items") and spec["mode"] == "sheet":
                keys = Counter()
                for it in r["items"]:
                    s = STIM.get(it["pid"]) or {}
                    if s.get("set") == "triads": keys[("t", s["triad"], s["oset"])] += 0; keys[("tri", s["triad"])] += 0
                groups = defaultdict(set)
                for it in r["items"]:
                    s = STIM.get(it["pid"]) or {}
                    if "pair" in s: groups[("pair", s["pair"])].add(s["order"])
                    if "seq" in s: groups[("seq", s["seq"], frozenset((s["a"], s["b"])))].add(s["order"])
                    if "item" in s: groups[("item", s["item"])].add(s["order"])
                    if "triad" in s: groups[("triad", s["triad"])].add(s["oset"])
                viol[name] += sum(1 for v in groups.values() if len(v) > 1)
    print("  sheets in which both orders/osets of one unit co-occur:", {k: v for k, v in viol.items() if v} or "none")
    # option-order variety
    for name in ("format-perp-single-opus55", "triads-perp-single-sonnet55", "format-perp-sheet-sonnet55"):
        rows = RUNS[name][1]
        orders = Counter()
        for r in rows:
            m = re.findall(r"^  - (≈|⟂|the symbol)", r["prompt"], re.M)
            orders[tuple(m)] += 1
        print(f"  option orders seen in {name}: {len(orders)} distinct over {len(rows)} calls")

# ================================================================ 8. gestalt details
GEST = {}
def gparse(raw, glyphs):
    t = (raw or "").strip()
    t = re.sub(r"^```\w*\s*|\s*```$", "", t).strip()
    if t in ("⟂", "⊥") or t.lower().strip(". ") == "none": return ("perp", [], [])
    main, _, extra = t.partition("EXTRA")
    inv = sorted(set(glyphs), key=len, reverse=True)
    def seq(s):
        o = []; i = 0
        while i < len(s):
            for g in inv:
                if s.startswith(g, i): o.append(g); i += len(g); break
            else: i += 1
        return o
    o = seq(main)
    if not o: return ("perp" if "⟂" in t else "unk", [], [])
    return ("order", o, seq(extra))
def ktau(order, ref):
    c = [g for g in dict.fromkeys(order) if g in ref]
    if len(c) < 2: return None, len(c)
    pos = {g: i for i, g in enumerate(ref)}
    s = sum(1 if pos[x] < pos[y] else -1 for x, y in combinations(c, 2))
    return abs(s) / math.comb(len(c), 2), len(c)
for name, (spec, rows) in RUNS.items():
    if rows and spec["instrument"] == "gestalt":
        d = {}
        for r in rows:
            res = r["result"]
            if not res.get("raw") or res.get("error"): continue
            k = (r["rep"], r["pids"][0])
            if k not in d: d[k] = gparse(res["raw"], STIM[r["pids"][0]]["glyphs"])
        GEST[spec["judge_label"]] = d
if want("8"):
    print("\n## 8. gestalt: arrangements, subset sizes, chance baseline")
    for seq in ("unfold", "risebar", "elab-n", "elab-s", "elab-l", "noise-3"):
        print(f"  {seq}:")
        for j in sorted(GEST):
            if j not in FRONTIER: continue
            cells = []
            for (rep, pid), g in sorted(GEST[j].items(), key=lambda x: STIM[x[0][1]]["shuffle"]):
                s = STIM[pid]
                if s["seq"] != seq: continue
                if g[0] == "order":
                    t, n = ktau(g[1], s["intended"])
                    cells.append(f"{''.join(g[1])}{'+X'+''.join(g[2]) if g[2] else ''} τ={t if t is None else round(t,2)} k={n}/{len(s['intended'])}")
                else: cells.append(g[0])
            print(f"    {j:14s} {' | '.join(cells)}")
    # Monte Carlo chance of mean |tau| for random full permutations, by set length
    import random
    rnd = random.Random(1)
    for n in (3, 4, 5, 6):
        ref = list(range(n)); v = []
        for _ in range(20000):
            o = ref[:]; rnd.shuffle(o); v.append(ktau(o, ref)[0])
        v.sort()
        print(f"  random-permutation |τ|, n={n}: mean {sum(v)/len(v):.2f}, P(|τ|=1) {sum(x==1 for x in v)/len(v):.3f}, 95th pct {v[int(.95*len(v))]:.2f}")
    # P13 noise denominators
    for j in sorted(GEST):
        if j not in FRONTIER: continue
        c = Counter(); n = 0
        for (rep, pid), g in GEST[j].items():
            if STIM[pid]["seq"].startswith("noise"): c[g[0]] += 1; n += 1
        print(f"  {j:14s} noise presentations with a response: {n}/12, ⟂ {c['perp']}")

# ================================================================ 9. seed retest chance baseline
if want("9"):
    print("\n## 9. seed retest: agreement with written order vs a random-orientation baseline")
    pool = json.load(open(EXP / "data/stimuli-v1/pool.json"))
    recs = {r["rec"]: r for r in pool["seed_records"]}
    print("  surveyors in seed stratum:", dict(Counter(r["surveyor"] for r in pool["seed_records"])))
    for j in sorted(TRI):
        d = {pid: v for (rep, pid), v in TRI[j].items() if rep == 0}
        tri = defaultdict(lambda: defaultdict(dict))
        for pid, v in d.items():
            s = STIM[pid]
            if s["stratum"] == "seed-local": tri[s["triad"]][s["oset"]][(s["a"], s["b"])] = (v, s)
        ordered = agree = 0; exp = 0.0
        for t, os_ in tri.items():
            signs = []; rec = None
            for (a, b), (v0, s) in os_.get(0, {}).items():
                rec = recs[s["src"][0]]; x = os_.get(1, {}).get((b, a))
                if not x: continue
                p = pv(v0, x[0])
                if p[0] == "dir":
                    lo = b if p[1] == a else a; g = rec["glyphs"]
                    signs.append(1 if g.index(p[1]) > g.index(lo) else -1)
            if len(signs) >= 2:
                ordered += 1; agree += len(set(signs)) == 1
                exp += 2 * 0.5 ** len(signs)   # chance all signs equal under independent fair coins
        if ordered:
            print(f"  {j:22s} agree {R(agree, ordered)}  random-orientation expectation {exp/ordered:.2f}")

# ================================================================ 10. P3 conditional survival; P4 paired
if want("10"):
    print("\n## 10. P3 as 'survival' conditional on tie-directed; P4 on pairs committed under both formats")
    for j in sorted(FMT):
        t, p, f = FMT[j].get("tie"), FMT[j].get("perp"), FMT[j].get("forced")
        if not p: continue
        out = []
        if t:
            for st in ("fresh-seed-local", "fresh-mixed"):
                base = [k for k, (v, s) in t.items() if v[0] == "dir" and s["stratum"] == st and k in p and p[k][0][0] != "unk"]
                sv = sum(1 for k in base if p[k][0][0] == "dir")
                out.append(f"{st} {R(sv, len(base))}")
        if f:
            both = [k for k in f if f[k][0][0] == "dir" and p.get(k, ((None,),))[0][0] == "dir"]
            def val(ks, src):
                k_ = n_ = 0
                for k in ks:
                    v, s = src[k]; w = v[1]; l = s["a"] if w == s["b"] else s["b"]
                    nw, nl = unum(w), unum(l)
                    if nw is not None and nl is not None and nw != nl: n_ += 1; k_ += nw > nl
                return k_, n_
            fk, fn = val(both, f); pk, pn = val(both, p)
            allf = val([k for k in f if f[k][0][0] == "dir"], f)
            out.append(f"P4 same-pairs forced {R(fk, fn)} perp {R(pk, pn)}; forced-only-commits value {R(allf[0]-fk, allf[1]-fn)}")
        print(f"  {j:24s} " + " | ".join(out))

# ================================================================ 11. isolation evidence in ledgers
if want("11"):
    print("\n## 11. isolation evidence recorded per call")
    agg = defaultdict(Counter)
    for name, (spec, rows) in RUNS.items():
        ad = spec["judge"].get("adapter", "")
        for r in rows:
            m = r["result"].get("adapter_meta") or {}
            if ad == "claude": agg[ad][("tools", json.dumps(m.get("tools")))] += 1
            elif ad == "agy": agg[ad][("num_turns", m.get("num_turns"))] += 1
            elif ad == "grok": agg[ad][("event_types", tuple(sorted((m.get("event_types") or {}).keys())))] += 1
            elif ad == "codex": agg[ad][("item_types", tuple(sorted((m.get("item_types") or {}).keys())))] += 1
            elif ad == "ollama": agg[ad][("model", r["result"].get("model_reported"))] += 1
    for ad, c in agg.items():
        print(f"  {ad}: {dict(c.most_common(8))}")
    # Claude thinking tokens
    for name, (spec, rows) in RUNS.items():
        if spec["judge"].get("adapter") == "claude" and spec["instrument"] == "triads":
            th = [r["result"]["usage"].get("thinking_tokens") for r in rows if r["result"].get("usage")]
            th = [x for x in th if x is not None]
            if th: print(f"  {name}: thinking tokens per call mean {sum(th)/len(th):.0f}, share >0 {sum(1 for x in th if x>0)/len(th):.2f}")

# ================================================================ 12. SIGNA order positions
if want("12"):
    print("\n## 12. SIGNA: Copeland position of ⚬ relative to ╍ and ╌")
    SIG = ["·", "╶", "╌", "╍", "━", "═", "⚬", "○", "◎", "◉", "⬤"]
    for name, (spec, rows) in RUNS.items():
        if not rows or spec["instrument"] != "signa": continue
        pres = defaultdict(dict)
        for (rep, pid), v in P[name].items():
            s = STIM[pid]; pres[frozenset((s["a"], s["b"]))][s["order"]] = v
        sc = Counter()
        for k, o in pres.items():
            if 0 in o and 1 in o:
                x = pv(o[0], o[1])
                if x[0] == "dir":
                    sc[x[1]] += 1; sc[next(iter(k - {x[1]}))] -= 1
        order = sorted(SIG, key=lambda g: (sc[g], SIG.index(g)))
        print(f"  {label(name, spec):20s} {''.join(order)}  ⚬ below ╍: {order.index('⚬') < order.index('╍')}  ⚬ below ╌: {order.index('⚬') < order.index('╌')}  "
              f"ink ━ {INK.get('━')} ═ {INK.get('═')}")

# ================================================================ 13. bias-immune transitivity
if want("13"):
    print("\n## 13. transitivity on bias-immune edges (pairs consistent-directed across both orientation sets)")
    print("  (in this design a within-set 3-cycle occurs iff all three answers pick the same screen position, so")
    print("   the registered cycle rate cannot separate intransitivity from position bias; this is the separable version)")
    for j in sorted(TRI):
        d = {pid: v for (rep, pid), v in TRI[j].items() if rep == 0}
        tri = defaultdict(lambda: defaultdict(dict))
        for pid, v in d.items():
            s = STIM[pid]; tri[s["triad"]][s["oset"]][(s["a"], s["b"])] = v
        full = cyc = 0
        for t, os_ in tri.items():
            o0, o1 = os_.get(0, {}), os_.get(1, {})
            wins = []
            for (a, b), v0 in o0.items():
                v1 = o1.get((b, a))
                if v1 is None: break
                x = pv(v0, v1)
                if x[0] != "dir": break
                wins.append(x[1])
            if len(wins) == 3:
                full += 1; cyc += len(set(wins)) == 3
        print(f"  {j:22s} triads with all three pairs bias-immune directed: {full}; cyclic among them: {R(cyc, full)}")
