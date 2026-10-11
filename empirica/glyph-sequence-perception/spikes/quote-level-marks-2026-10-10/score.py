"""Score ledger.jsonl: one line per (mind, kind, layout), then a per-mind summary. Exact-match scoring only."""
import json, re, sys, collections, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import probe

def parse(raw):
    if not raw: return None
    raw = re.sub(r"<think>.*?</think>", "", raw, flags=re.S)
    m = re.search(r"\{.*\}", raw, re.S)
    if not m: return None
    try: return json.loads(m.group(0))
    except Exception: return None

def lvl(x):
    """a level answer as an int: 2, "2", "level 2" -> 2; anything else -> 0 (same rule for every mind)"""
    m = re.search(r"[123]", str(x)) if x is not None else None
    return int(m.group(0)) if m and len(re.findall(r"[0-9]", str(x))) == 1 else 0

def kind_A(v, d):
    want = probe.A_LEVELS[v]
    lv = {str(k): v2 for k, v2 in (d.get("levels") or {}).items()}
    got = [lvl(lv.get(str(i+1))) for i in range(6)]
    right = sum(g == w for g, w in zip(got, want))
    cit_want = {i+1 for i, w in enumerate(want) if w == 3}
    cit = {int(x) for x in (d.get("citable") or []) if str(x).isdigit()}
    errs = [f"q{i+1}:{w}→{g}" for i, (g, w) in enumerate(zip(got, want)) if g != w]
    return right, 6, cit == cit_want, errs

def kind_D(v, d):
    want = probe.D_LEVELS[v]
    lv = {str(k): x for k, x in (d.get("levels") or {}).items()}
    got = [lvl(lv.get(str(i+1))) for i in range(10)]
    errs = [f"q{i+1}:{w}→{g}" for i, (g, w) in enumerate(zip(got, want)) if g != w]
    cit = {int(x) for x in (d.get("citable") or []) if str(x).isdigit()}
    return 10 - len(errs), 10, cit == {i+1 for i, w in enumerate(want) if w == 3}, errs

def kind_B(v, d):
    items = probe.B_ITEMS[v]; bad = probe.B_BAD[v]
    # groups: the six well-formed fall into 3 pairs; the mismatched one alone (or absent)
    true = collections.defaultdict(set)
    for i, oc in enumerate(items):
        if i+1 != bad: true[oc].add(i+1)
    true_sets = {frozenset(s) for s in true.values()}
    groups = [frozenset(int(x) for x in g if str(x).isdigit()) for g in (d.get("groups") or []) if isinstance(g, list)]
    groups_wo_bad = {g - {bad} for g in groups if g - {bad}}
    grouping_ok = groups_wo_bad == true_sets
    o = {str(k): str(x).lower() for k, x in (d.get("outer") or {}).items()}
    n = {str(k): str(x).lower() for k, x in (d.get("inner") or {}).items()}
    sd, tot, errs = 0, 0, []
    for i, (op, _) in enumerate(items):
        wo = "single" if op[0] == "‹" else "double"; wi = "single" if op[1] == "⟨" else "double"
        for name, want, got in (("outer", wo, o.get(str(i+1), "")), ("inner", wi, n.get(str(i+1), ""))):
            tot += 1
            if want in got and not (want == "single" and "double" in got): sd += 1
            else: errs.append(f"q{i+1}.{name}:{want}→{got or '∅'}")
    mm = {int(x) for x in (d.get("mismatched") or []) if str(x).isdigit()}
    return sd, tot, grouping_ok, mm == {bad}, errs, sorted(mm)

def kind_C(v, d):
    want = {str(i+1): probe.mark(s, b) for i, (s, a, b) in enumerate(probe.C_TASK[v])}
    right, errs = 0, []
    for k, w in want.items():
        g = str(d.get(k, "")).strip()
        if g == w: right += 1
        else:
            # report only the marks, which is what is being tested
            gm = re.sub(r"[A-Za-z0-9 .,°]+", "…", g)
            errs.append(f"q{k}:{probe.mark('…', probe.C_TASK[v][int(k)-1][2])}→{gm or '∅'}")
    return right, 3, errs

rows = [json.loads(l) for f in sorted(HERE.glob("ledger*.jsonl")) for l in open(f)]
if len(sys.argv) > 1: rows = [r for r in rows if r["mind"] in sys.argv[1:]]
summ = collections.defaultdict(lambda: collections.Counter())
for r in rows:
    res = r["result"]; d = parse(res.get("raw")); m, k, v = r["mind"], r["kind"], r["layout"]
    th = (res.get("usage") or {}).get("thinking_tokens")
    if res.get("error") or d is None:
        print(f"{m:15} {k}{v}  NO ANSWER ({str(res.get('error'))[:60] or 'unparsed'}) {(res.get('raw') or '')[:80]!r}")
        summ[m]["noanswer"] += 1; continue
    if k == "A":
        right, tot, cit, errs = kind_A(v, d)
        summ[m]["A_right"] += right; summ[m]["A_tot"] += tot; summ[m]["A_cit"] += cit
        print(f"{m:15} A{v}  levels {right}/{tot}  citable {'ok' if cit else 'WRONG'}  th={th}  {' '.join(errs)}")
    elif k == "B":
        sd, tot, gok, mok, errs, mm = kind_B(v, d)
        summ[m]["B_sd"] += sd; summ[m]["B_tot"] += tot; summ[m]["B_group"] += gok; summ[m]["B_mm"] += mok
        print(f"{m:15} B{v}  single/double {sd}/{tot}  groups {'ok' if gok else 'WRONG'}  mismatch {'ok' if mok else 'WRONG '+str(mm)}  th={th}  {' '.join(errs)}")
    elif k == "D":
        right, tot, cit, errs = kind_D(v, d)
        summ[m]["D_right"] += right; summ[m]["D_tot"] += tot; summ[m]["D_cit"] += cit; summ[m]["D_n"] += 1
        print(f"{m:15} D{v}  levels {right}/{tot}  citable {'ok' if cit else 'WRONG'}  th={th}  {' '.join(errs)}")
    else:
        right, tot, errs = kind_C(v, d)
        summ[m]["C_right"] += right; summ[m]["C_tot"] += tot
        print(f"{m:15} C{v}  marks {right}/{tot}  th={th}  {' '.join(errs)}")
print()
print(f"{'mind':15} {'A levels':>9} {'A citable':>9} {'B s/d':>7} {'B groups':>8} {'B mismatch':>10} {'C write':>8} {'D prose':>8} {'D cit':>6} {'no ans':>6}")
for m, c in summ.items():
    print(f"{m:15} {c['A_right']:>4}/{c['A_tot']:<4} {c['A_cit']:>7}/2 {c['B_sd']:>3}/{c['B_tot']:<3} {c['B_group']:>6}/2 {c['B_mm']:>8}/2 {c['C_right']:>4}/{c['C_tot']:<3} {c['D_right']:>4}/{c['D_tot']:<4} {c['D_cit']:>3}/{c['D_n']:<2} {c['noanswer']:>6}")
