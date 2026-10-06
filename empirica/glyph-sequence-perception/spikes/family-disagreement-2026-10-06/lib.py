"""Shared loader for the family-disagreement spike (2026-10-06).

The seal (audits/SEAL-canary-choose-2026-10-06.md) is applied FIRST, before any record is kept, counted or shown:
every `choose` and `names` record touching a canary glyph is dropped, using the catalog's own rule (catalog/build.py
`sealed`). `call-failed` records are dropped next. Answers in void rounds are kept (the tree and catalog keep them; only asking
stopped there). A snapshot of what was kept
is pickled in the session scratchpad (SNAP), with its manifest beside it, so every script in this spike reads the same
answers while the drains keep writing.
"""
import json, pathlib, pickle, sys, time, hashlib, collections

ROOT = pathlib.Path(__file__).resolve().parents[2]
SNAP = pathlib.Path("/private/tmp/claude-505/-Users-josephwecker-v2-src-arch-asf-empirica-glyph-sequence-perception/"
                    "2c3109cb-51be-4d66-937d-88f689223324/scratchpad/fd-snapshot.pkl")
CANARY = set("▁▂▃▄▅▆▇█🮆🮅🮄▀🮃🮂▔▉")

def sealed(r):
    if r.get("kind") not in ("choose", "names"):
        return False
    gs = set(r.get("context") or []) | set(r.get("candidates") or []) | set(r.get("shown") or [])
    return bool(gs & CANARY)

def build_snapshot():
    void = set(json.load(open(ROOT / "data" / "rounds" / "VOID.json"))["rounds"])
    keep, seen = [], set()
    n_sealed = n_void = n_failed = n_dup = 0
    files = sorted((ROOT / "data" / "answers").glob("*.jsonl"))
    digests = {}
    for f in files:
        b = f.read_bytes(); digests[f.name] = hashlib.sha256(b).hexdigest()[:16]
        for line in b.decode().splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            if sealed(r):                       # the seal, before anything else
                n_sealed += 1; continue
            if r.get("aid") in seen:
                n_dup += 1; continue
            seen.add(r.get("aid"))
            if r.get("round") in void:
                n_void += 1                     # kept, as the tree and catalog keep them; only asking stopped there
            if r.get("outcome") == "call-failed":
                n_failed += 1; continue
            keep.append(r)
    man = {"taken": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "kept": len(keep), "sealed_dropped": n_sealed,
           "in_void_rounds_kept": n_void, "failed_dropped": n_failed, "dup_dropped": n_dup, "files": digests}
    SNAP.parent.mkdir(parents=True, exist_ok=True)
    pickle.dump((keep, man), open(SNAP, "wb"))
    return keep, man

def load(refresh=False):
    if refresh or not SNAP.exists():
        return build_snapshot()
    return pickle.load(open(SNAP, "rb"))

FAMS = ("claude", "grok", "gemini")

if __name__ == "__main__":
    keep, man = load(refresh="--refresh" in sys.argv)
    print(json.dumps({k: v for k, v in man.items() if k != "files"}, indent=1))
