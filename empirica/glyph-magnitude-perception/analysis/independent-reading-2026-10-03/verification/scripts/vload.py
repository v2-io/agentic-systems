"""Verifier's independent loader (written without reading reading/scripts/common.py).

Uses only the builder's parser p1.3 (harness/runner/instruments.py) for parsing.
Answer selection: per (pid, rep), rows in timestamp order; rows with empty raw / error are skipped;
sheet rows flagged sheet_incomplete are used only for items no complete row answered.
Among usable rows, the last PARSED answer wins; if none parsed, the presentation is 'unparsed'.
"""
import json, glob, os, sys, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
sys.path.insert(0, os.path.join(ROOT, "harness/runner"))
import instruments as I

EXCLUDE_SUBSTR = ("shakedown", "toolleak", "qwen3-4b")

def stimuli():
    pid = {}
    for f in glob.glob(os.path.join(ROOT, "data/stimuli-v1/*.jsonl")):
        for l in open(f):
            l = l.strip()
            if l:
                d = json.loads(l); pid[d["pid"]] = d
    return pid

STIM = stimuli()

def runs(prefix=""):
    out = []
    for d in sorted(glob.glob(os.path.join(ROOT, "data/runs-v1/*/"))):
        rid = os.path.basename(d.rstrip("/"))
        if any(x in rid for x in EXCLUDE_SUBSTR): continue
        if not os.path.exists(d + "ledger.jsonl"): continue
        if rid.startswith(prefix): out.append(rid)
    return out

def rows(rid):
    rs = [json.loads(l) for l in open(os.path.join(ROOT, "data/runs-v1", rid, "ledger.jsonl")) if l.strip()]
    rs.sort(key=lambda r: r["ts"])
    return rs

def pair_answers(rid):
    """-> {(pid, rep): (verdict, more, by)} for pair instruments."""
    best = {}; fallback = {}
    for r in rows(rid):
        raw = r["result"].get("raw") or ""
        if not raw or r["result"].get("error"): continue
        rep = r.get("rep", 0)
        if r["mode"] == "single":
            p = r["pids"][0]; s = STIM[p]
            v = I.parse_pair(raw, s["a"], s["b"])
            tgt = best
            res = {p: v}
        else:
            items = [{"id": it["id"], "a": STIM[it["pid"]]["a"], "b": STIM[it["pid"]]["b"], "pid": it["pid"]} for it in r["items"]]
            parsed = I.parse_sheet(raw, items)
            idmap = {it["id"]: it["pid"] for it in items}
            res = {idmap[i]: v for i, v in parsed.items()}
            # items not in parsed answer at all -> unparsed
            for it in items:
                res.setdefault(it["pid"], ("unparsed", None, None))
            tgt = fallback if r.get("sheet_incomplete") is not None else best
        for p, v in res.items():
            k = (p, rep)
            if v[0] != "unparsed" or k not in tgt:
                tgt[k] = v
    for k, v in fallback.items():
        if k not in best or (best[k][0] == "unparsed" and v[0] != "unparsed"):
            best[k] = v
    return best

def gestalt_answers(rid):
    """-> {pid: parsed dict + raw}"""
    best = {}
    for r in rows(rid):
        raw = r["result"].get("raw") or ""
        if not raw or r["result"].get("error"): continue
        p = r["pids"][0]; s = STIM[p]
        g = I.parse_gestalt(raw, s["glyphs"]); g["raw"] = raw
        if g["kind"] != "unparsed" or p not in best:
            best[p] = g
    return best

def judge_of(rid):
    parts = rid.split("-")
    # instrument-format-mode-judge...
    return rid

def verdict_pair(va, vb, a, b):
    """va = answer on order (a,b), vb on order (b,a); winners are glyphs."""
    if va is None or vb is None: return "missing"
    if va[0] == "unparsed" or vb[0] == "unparsed": return "unparsed"
    if va[0] == "dir" and vb[0] == "dir":
        return ("cdir", va[1]) if va[1] == vb[1] else ("flip", None)
    if va[0] == vb[0] == "perp": return ("cperp", None)
    if va[0] == vb[0] == "tie": return ("ctie", None)
    return ("mixed", None)

def wilson(k, n, z=1.96):
    if n == 0: return (float("nan"),) * 3
    p = k / n; d = 1 + z*z/n; c = p + z*z/(2*n); h = z*((p*(1-p)/n + z*z/(4*n*n)) ** 0.5)
    return p, (c - h)/d, (c + h)/d

FRONTIER = ["opus55", "sonnet55", "sonnet5", "haiku45", "grok46", "gpt56terra", "gemini31pro", "gemini38flash"]
