"""Spot check: can minds tell the three quote-verification marks apart at a glance?

    level 1  ‹⟨…⟩›   level 2  «⟨…⟩»   level 3  «⟪…⟫»

Three question kinds, two layouts each (v0, v1), one stateless call per (mind, kind, layout):
  A  legend given: give each quotation's level; list the externally citable ones   (the intended use)
  B  no legend: group identically marked quotations, say single/double for each opening mark,
     flag the one quotation whose closing marks don't match its opening marks          (discrimination alone)
  C  legend given: rewrite quotations at a new level, marks exact                      (writing the marks)
Judges are the study's isolated adapters (core/judges.py). Every call appends one row to ledger.jsonl.
Usage: probe.py MIND [MIND ...]     (minds from core/minds.json, or extras below)
"""
import json, os, pathlib, sys, time, datetime, concurrent.futures as cf
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))
from core.judges import make_judge, ADAPTER_VERSION

MARK = {1: ("‹⟨", "⟩›"), 2: ("«⟨", "⟩»"), 3: ("«⟪", "⟫»")}
def mark(s, lv): return MARK[lv][0] + s + MARK[lv][1]

SYSTEM = "You are a participant in a short perception study. Answer exactly as asked."
LEGEND = """A document marks each quotation with how far its text has been checked:

  ‹⟨…⟩›  level 1: as converted, the canonical text, unchecked
  «⟨…⟩»  level 2: matched mechanically against an independent text layer
  «⟪…⟫»  level 3: every conversion agrees, and someone looked at the rendered page; required for anything cited externally"""

S = ["The sample was dried at 40 °C for six hours.", "No effect was observed below the threshold.",
     "These results should be read as provisional.", "The second survey reached 1,204 households.",
     "Error bars show one standard deviation.", "The protocol was revised after the pilot.",
     "Participants could withdraw at any time.", "All code is available on request."]
LEADS = ["The paper states", "As reported,", "The authors write", "On page 4:", "The caption reads", "The methods add"]

A_LEVELS = {0: [2, 1, 3, 3, 1, 2], 1: [3, 2, 1, 2, 3, 1]}
def prompt_A(v):
    items = [f"{i+1}. {LEADS[i]} {mark(S[(i + 3*v) % 8], lv)}" for i, lv in enumerate(A_LEVELS[v])]
    return (LEGEND + "\n\nQuotations:\n" + "\n".join(items) +
            "\n\nAt a glance, give the level of each quotation, then list the quotations that may be cited externally.\n"
            'Reply with JSON only: {"levels": {"1": <level>, ...}, "citable": [<numbers>]}')

# B: two of each level plus one mismatched quotation (index given by B_BAD)
B_ITEMS = {0: [("‹⟨", "⟩›"), ("«⟪", "⟫»"), ("«⟨", "⟩»"), ("«⟨", "⟫»"), ("«⟨", "⟩»"), ("‹⟨", "⟩›"), ("«⟪", "⟫»")],
           1: [("«⟨", "⟩»"), ("«⟪", "⟫»"), ("‹⟨", "⟩»"), ("‹⟨", "⟩›"), ("«⟪", "⟫»"), ("«⟨", "⟩»"), ("‹⟨", "⟩›")]}
B_BAD = {0: 4, 1: 3}
def prompt_B(v):
    items = [f"{i+1}. {o}{S[(i + 2*v) % 8]}{c}" for i, (o, c) in enumerate(B_ITEMS[v])]
    return ("Below are seven quotations, each wrapped in a pair of delimiter marks (an outer mark and an inner mark at each end).\n\n" +
            "\n".join(items) +
            "\n\nAt a glance:\n(a) Group the quotations whose marks are identical.\n"
            "(b) For each quotation, is its opening OUTER mark single or double, and its opening INNER mark single or double?\n"
            "(c) Which quotations, if any, have closing marks that don't match their opening marks?\n"
            'Reply with JSON only: {"groups": [[<numbers>], ...], "outer": {"1": "single|double", ...}, '
            '"inner": {"1": "single|double", ...}, "mismatched": [<numbers>]}')

C_TASK = {0: [(S[0], 1, 3), (S[3], 2, 1), (S[5], 3, 2)], 1: [(S[1], 1, 2), (S[4], 3, 1), (S[6], 2, 3)]}
def prompt_C(v):
    items = [f"{i+1}. {mark(s, a)}  is now level {b}" for i, (s, a, b) in enumerate(C_TASK[v])]
    return (LEGEND + "\n\nEach quotation below has been re-checked and its level changed. Rewrite each one, marked exactly as the "
            "document would mark it at its new level.\n\n" + "\n".join(items) +
            '\n\nReply with JSON only: {"1": "<marked quotation>", "2": "...", "3": "..."}')

# D (added after the first pass): ten quotations inline in one dense paragraph, as the marks will actually appear
D_LEVELS = {0: [1, 2, 3, 2, 2, 3, 1, 3, 1, 2], 1: [3, 3, 2, 1, 2, 3, 2, 1, 1, 3]}
D_FRAGS = ["samples were dried overnight", "at 40 °C", "no effect below threshold", "provisional", "1,204 households",
           "one standard deviation", "revised after the pilot", "withdraw at any time", "available on request", "two coders"]
class _DLevels(dict):   # layouts 2+ are random (fated by layout number), each holding every level at least twice
    def __missing__(self, v):
        import random
        rng = random.Random(f"quote-level-marks-D-{v}")
        while True:
            lv = [rng.choice((1, 2, 3)) for _ in range(10)]
            if all(lv.count(k) >= 2 for k in (1, 2, 3)):
                self[v] = lv; return lv
D_LEVELS = _DLevels(D_LEVELS)

def prompt_D(v):
    q = [mark(f, lv) + f"[{i+1}]" for i, (f, lv) in enumerate(zip(D_FRAGS, D_LEVELS[v]))]
    para = (f"The methods section says the {q[0]}, {q[1]}, and that there was {q[2]}; the authors call the estimates "
            f"{q[3]} and report reaching {q[4]}, with error bars of {q[5]}. The protocol was {q[6]}, participants could "
            f"{q[7]}, code is {q[8]}, and every transcript was read by {q[9]}.")
    return (LEGEND + "\n\nPassage (each quotation is followed by its number in brackets):\n\n" + para +
            "\n\nAt a glance, give the level of each numbered quotation, then list the ones that may be cited externally.\n"
            'Reply with JSON only: {"levels": {"1": <level>, ...}, "citable": [<numbers>]}')

PROMPTS = {"A": prompt_A, "B": prompt_B, "C": prompt_C, "D": prompt_D}

EXTRA = {   # minds not on the study roster
    "gpt56terra": {"adapter": "codex", "model": "gpt-5.6-terra", "effort": "low", "family": "gpt"},
    "gemma3-4b": {"adapter": "ollama", "model": "gemma3:4b", "num_predict": 800, "format": "json", "family": "local"},
    "phi4mini": {"adapter": "ollama", "model": "phi4-mini:latest", "num_predict": 800, "format": "json", "family": "local"},
    "llama32-3b": {"adapter": "ollama", "model": "llama3.2:3b", "num_predict": 800, "format": "json", "family": "local"},
    "qwen25-3b": {"adapter": "ollama", "model": "qwen2.5:3b", "num_predict": 800, "format": "json", "family": "local"},
    "qwen3-4b": {"adapter": "ollama", "model": "qwen3:4b", "num_predict": 800, "format": "json", "think": False, "family": "local"},
    "mistral7b": {"adapter": "ollama", "model": "mistral:7b", "num_predict": 800, "format": "json", "family": "local"},
    "gptoss20b": {"adapter": "ollama", "model": "gpt-oss:latest", "num_predict": 6000, "family": "local"},
    "deepseekr1-14b": {"adapter": "ollama", "model": "deepseek-r1:14b", "num_predict": 8000, "family": "local"},
    "llama33-70b": {"adapter": "ollama", "model": "llama3.3:70b", "num_predict": 800, "format": "json", "family": "local"},
}
MINDS = json.load(open(ROOT / "core" / "minds.json"))["minds"]

def spec_of(m):
    s = dict(EXTRA[m]) if m in EXTRA else dict(MINDS[m])
    return s

def ask(mind, kind, v):
    spec = spec_of(mind)
    p = PROMPTS[kind](v)
    r = make_judge(spec)(SYSTEM, p)
    row = {"ts": datetime.datetime.now(datetime.timezone.utc).isoformat(), "mind": mind, "family": spec.get("family"),
           "judge": {k: v for k, v in spec.items() if k not in ("note",)}, "adapter_version": ADAPTER_VERSION[spec["adapter"]],
           "kind": kind, "layout": v, "system": SYSTEM, "prompt": p, "result": r}
    return row

if __name__ == "__main__":
    # MIND runs all six items; MIND:KIND:LAYOUT re-asks one item (e.g. gemini38flash:B:0)
    jobs = [(a.split(":")[0], a.split(":")[1], int(a.split(":")[2])) if ":" in a else None for a in sys.argv[1:]]
    jobs = [j for a, j in zip(sys.argv[1:], jobs) if j] + [(m, k, v) for m in sys.argv[1:] if ":" not in m for k in os.environ.get("KINDS", "ABC") for v in [int(x) for x in os.environ.get("LAYOUTS", "0,1").split(",")]]
    minds = sorted({j[0] for j in jobs})
    local = all(spec_of(m)["adapter"] == "ollama" for m in minds)
    with open(HERE / os.environ.get("LEDGER", "ledger.jsonl"), "a") as out, cf.ThreadPoolExecutor(1 if local else 8) as ex:
        for row in ex.map(lambda j: ask(*j), jobs):
            out.write(json.dumps(row, ensure_ascii=False) + "\n"); out.flush()
            res = row["result"]
            print(row["mind"], row["kind"], row["layout"], "ERR " + str(res["error"])[:120] if res["error"] else (res["raw"] or "")[:160].replace("\n", " "), flush=True)
