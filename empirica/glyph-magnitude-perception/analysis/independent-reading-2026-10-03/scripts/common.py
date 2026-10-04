"""Shared loaders for the independent reading. Uses the builder's parser p1.3 (harness/runner/instruments.py)
as ONE parse, and keeps raw text available so every number can be checked by eye."""
import json, pathlib, sys, collections
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "harness/runner"))
import instruments as I

RUNS = ROOT / "data/runs-v1"
STIM = ROOT / "data/stimuli-v1"

SIGNA = ["·", "╶", "╌", "╍", "━", "═", "⚬", "○", "◎", "◉", "⬤"]
IDX = {g: i for i, g in enumerate(SIGNA)}
INVALID = {"qwen3-4b"}


def ledger(run):
    p = RUNS / run / "ledger.jsonl"
    return [json.loads(l) for l in open(p)] if p.exists() else []


def spec(run):
    return json.load(open(RUNS / run / "spec.json"))


def stim_rows(fname):
    return {r["pid"]: r for r in (json.loads(l) for l in open(STIM / fname))}


def parsed_presentations(run, stimfile):
    """-> {pid: [(verdict, more, by, raw), ...]} using only valid rows (raw present, no error, sheet complete).
    For sheet runs, parse every item of each valid sheet."""
    rows = stim_rows(stimfile)
    out = collections.defaultdict(list)
    for r in ledger(run):
        res = r["result"]
        if not res.get("raw") or res.get("error") or r.get("sheet_incomplete") is not None:
            continue
        if r.get("sheet"):
            items = [{"id": it["id"], "a": rows[it["pid"]]["a"], "b": rows[it["pid"]]["b"]} for it in r["items"]]
            p = I.parse_sheet(res["raw"], items)
            for it in r["items"]:
                v = p.get(it["id"], ("unparsed", None, None))
                out[it["pid"]].append((v[0], v[1], v[2], None))
        else:
            pid = r["pids"][0]
            st = rows[pid]
            v = I.parse_pair(res["raw"], st["a"], st["b"])
            out[pid].append((v[0], v[1], v[2], res["raw"]))
    return rows, out


def pair_verdicts(rows, pres, key="pair_key"):
    """Combine the two orders of each unordered pair. Returns {frozenset(a,b): (kind, winner, (v0, v1))}.
    Uses the LAST valid presentation if a pid was asked more than once (resumes)."""
    by = collections.defaultdict(dict)
    for pid, st in rows.items():
        k = frozenset((st["a"], st["b"]))
        v = pres.get(pid)
        by[k][st["order"]] = v[-1] if v else ("missing", None, None, None)
    out = {}
    for k, d in by.items():
        v0, v1 = d.get(0, ("missing",) * 4), d.get(1, ("missing",) * 4)
        kinds = (v0[0], v1[0])
        if "missing" in kinds or "unparsed" in kinds:
            out[k] = ("incomplete", None, (v0, v1))
        elif kinds == ("dir", "dir"):
            out[k] = ("cdir", v0[1], (v0, v1)) if v0[1] == v1[1] else ("flip", None, (v0, v1))
        elif kinds == ("perp", "perp"):
            out[k] = ("cperp", None, (v0, v1))
        elif kinds == ("tie", "tie"):
            out[k] = ("ctie", None, (v0, v1))
        else:
            out[k] = ("mixed", None, (v0, v1))
    return out


def kendall_tau(order, ref):
    """Kendall tau-a between `order` (judge arrangement) and ref order over shared items."""
    shared = [g for g in order if g in ref]
    pos = {g: i for i, g in enumerate(ref)}
    n = len(shared)
    if n < 2:
        return None, n
    c = d = 0
    for i in range(n):
        for j in range(i + 1, n):
            s = pos[shared[i]] - pos[shared[j]]
            if s < 0: c += 1
            elif s > 0: d += 1
    return (c - d) / (n * (n - 1) / 2), n


def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"),) * 2
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / den
    return (max(0, c - h), min(1, c + h))


def judge_of(run):
    s = spec(run)
    return s["judge_label"].replace("-sheet", "") + ("[sheet]" if s["mode"] == "sheet" else "")


def runs(prefix):
    """Valid runs for an instrument prefix: excludes shakedowns, the aborted tool-leak run, qwen3-4b (invalid),
    and the pilot-condition arm (handled separately)."""
    return sorted(p.name for p in RUNS.iterdir() if p.name.startswith(prefix)
                  and "shakedown" not in p.name and "aborted" not in p.name and "qwen3-4b" not in p.name
                  and "pilotcond" not in p.name)
