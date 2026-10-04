"""Shared paths, protocol tag, glyph rules, JSONL helpers. See PLAN.md (study root)."""
import json, pathlib, sys, unicodedata as U

SEQ = pathlib.Path(__file__).resolve().parent
EXP = SEQ.parents[1]
sys.path.insert(0, str(EXP / "harness/core"))
from fate import rng, digest, canon  # noqa: E402

PROTOCOL = "gsp-0.1"
DATA = EXP / "data"
ROUNDS = DATA / "rounds"

# Glyphs that can never be stimuli: response vocabulary and lookalikes.
BANNED = {"⟂", "⊥", "≈"}

def ok_glyph(ch):
    return (isinstance(ch, str) and len(ch) == 1 and U.category(ch)[0] in "LNPS" and ch not in BANNED
            and not (0xFE00 <= ord(ch) <= 0xFE0F) and not ch.isspace())

def read_jsonl(p):
    p = pathlib.Path(p)
    if not p.exists():
        return []
    return [json.loads(l) for l in open(p) if l.strip()]

def write_jsonl(p, rows):
    p = pathlib.Path(p); p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")

def append_jsonl(p, row):
    p = pathlib.Path(p); p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "a") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")

def R(purpose, obj):
    """Fated RNG under this protocol."""
    return rng(PROTOCOL, purpose, obj)

def uid(prefix, obj):
    return prefix + digest({"p": PROTOCOL, **obj})[:12]

def minds():
    return json.load(open(EXP / "harness/core/minds.json"))
