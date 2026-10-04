#!/usr/bin/env python3
"""Build the frozen v1.0 stimulus sets (fated; rerunning reproduces them byte-identically).

Outputs (data/stimuli-v1/):
  pool.json              held-out pool: seed stratum (survey sequence-record glyphs never shown in
                         any pilot stimulus) + uniform tail (block-uniform over assigned graphic codepoints)
  triads.jsonl           300 triads x 6 presentations; strata: seed-local / seed-cross / uniform
  format-pairs.jsonl     320 pairs x 2 orders (format experiment; strata: pilot-replication / fresh-seed-local / fresh-mixed)
  conflict.jsonl         designer-built axis-conflict battery (claim-5 test), both orders
  holistic-pairs.jsonl   all pairs (both orders) within holistic candidates + controls
  gestalt.jsonl          scrambled sets (3 fated shuffles each): controls, pilot holistic, held-out holistic, noise foils
Every presentation row carries: pid, set, stratum, a, b (or glyphs), order, lineage note.
"""
import json, pathlib, re, sys, unicodedata
from itertools import combinations
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from fate import rng, digest, cps
from instruments import PROTOCOL

EXP = pathlib.Path(__file__).resolve().parents[2]
OUT = EXP / "data" / "stimuli-v1"
J = EXP / "data" / "judgments-v0"
BLOCKS = pathlib.Path.home() / "src/arch/firmatum/utils/utf/axes/ucd/Blocks.txt"
BANNED = {"≈", "⟂", "⊥"}  # response vocabulary + the ⟂ lookalike (pilot fix #1)

def single_glyphs(s):
    out = []
    for ch in s or "":
        cat = unicodedata.category(ch)
        if cat[0] in "LNPS" and ord(ch) > 0x7F and ch not in BANNED and not (0xFE00 <= ord(ch) <= 0xFE0F):
            out.append(ch)
    return out

def pilot_glyphs():
    seen = set()
    for f in J.glob("*.json"):
        if f.name.startswith("w") and not f.name.startswith("walk"):
            continue  # workflow outputs contain answers/prose, not stimuli; keys+chunks hold the stimuli
        seen.update(ch for ch in f.read_text() if ord(ch) > 0x7F)
    for f in (EXP / "pilot").glob("results*.jsonl"):
        for line in open(f):
            r = json.loads(line)
            seen.update(ch for k in ("a", "b") for ch in (r.get(k) or "") if ord(ch) > 0x7F)
    return seen

def blocks():
    out = []
    for line in open(BLOCKS):
        m = re.match(r"([0-9A-F]+)\.\.([0-9A-F]+); (.+)", line.strip())
        if m:
            out.append((int(m.group(1), 16), int(m.group(2), 16), m.group(3)))
    return out

def eligible(cp):
    if cp in (0xFFFD,) or 0xD800 <= cp <= 0xDFFF or 0xE000 <= cp <= 0xF8FF:
        return False
    ch = chr(cp)
    return unicodedata.category(ch)[0] in "LNPS" and ch not in BANNED and cp > 0x7F

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pilot = pilot_glyphs()
    # ---------------- seed stratum: survey sequence records, held-out glyphs only
    recs = []
    for f in sorted((EXP / "data/surveys-v1/extracted").glob("*.jsonl")):
        for line in open(f):
            if line.strip():
                r = json.loads(line)
                if r.get("type") == "sequence":
                    g = [c for c in single_glyphs(r.get("glyphs")) if c not in pilot]
                    g = list(dict.fromkeys(g))
                    if g:
                        recs.append({"rec": r["id"], "surveyor": r["surveyor"], "glyphs": g})
    seed_glyphs = sorted({c for r in recs for c in r["glyphs"]})
    # ---------------- uniform tail: block-uniform, then codepoint-uniform within block
    elig_blocks = []
    for lo, hi, name in blocks():
        if hi > 0x1FFFF:
            continue
        cpl = [cp for cp in range(lo, hi + 1) if eligible(cp)]
        if cpl:
            elig_blocks.append((name, cpl))
    tail = []
    i = 0
    while len(tail) < 400:
        r = rng(PROTOCOL, "uniform-tail", {"i": i}); i += 1
        name, cpl = elig_blocks[r.randrange(len(elig_blocks))]
        ch = chr(cpl[r.randrange(len(cpl))])
        if ch not in pilot and ch not in tail and ch not in seed_glyphs:
            tail.append(ch)
    pool = {"protocol": PROTOCOL, "unicode_version": unicodedata.unidata_version,
            "seed_records": recs, "seed_glyphs": seed_glyphs, "uniform_tail": tail,
            "n_blocks_eligible": len(elig_blocks), "pilot_excluded": len(pilot),
            "rule": "seed = survey sequence-record glyphs minus every non-ASCII char in any pilot stimulus/key file; "
                    "tail = block-uniform then codepoint-uniform over assigned L/N/P/S codepoints <= U+1FFFF, "
                    "minus pilot glyphs, seed glyphs, and {≈,⟂,⊥}; single codepoints only, VS stripped; ASCII excluded from both strata (pilot used ASCII digits heavily)"}
    json.dump(pool, open(OUT / "pool.json", "w"), ensure_ascii=False, indent=0)
    print(f"pool: {len(recs)} seed records, {len(seed_glyphs)} seed glyphs, {len(tail)} tail glyphs, "
          f"{len(elig_blocks)} blocks; pilot-excluded chars {len(pilot)}")

    # ---------------- triads
    local_recs = [r for r in recs if len(r["glyphs"]) >= 3]
    triads = []
    def add_triad(stratum, g3, src):
        if len(set(g3)) == 3 and tuple(sorted(g3)) not in {tuple(sorted(t["glyphs"])) for t in triads}:
            triads.append({"triad": len(triads), "stratum": stratum, "glyphs": list(g3), "src": src})
    k = 0
    while sum(t["stratum"] == "seed-local" for t in triads) < 120:
        r = rng(PROTOCOL, "triad-seed-local", {"k": k}); k += 1
        rec = local_recs[r.randrange(len(local_recs))]
        add_triad("seed-local", r.sample(rec["glyphs"], 3), [rec["rec"]])
    k = 0
    while sum(t["stratum"] == "seed-cross" for t in triads) < 90:
        r = rng(PROTOCOL, "triad-seed-cross", {"k": k}); k += 1
        rs = r.sample(recs, 3)
        add_triad("seed-cross", [r.choice(x["glyphs"]) for x in rs], [x["rec"] for x in rs])
    k = 0
    while sum(t["stratum"] == "uniform" for t in triads) < 90:
        r = rng(PROTOCOL, "triad-uniform", {"k": k}); k += 1
        add_triad("uniform", r.sample(tail, 3), ["uniform-tail"])
    with open(OUT / "triads.jsonl", "w") as f:
        for t in triads:
            A, B, C = t["glyphs"]
            # orientation set 0: AB BC CA ; set 1: BA CB AC  (pilot triad unit)
            for oset, pairs in ((0, [(A, B), (B, C), (C, A)]), (1, [(B, A), (C, B), (A, C)])):
                for a, b in pairs:
                    row = {"set": "triads", "triad": t["triad"], "stratum": t["stratum"], "oset": oset,
                           "a": a, "b": b, "src": t["src"]}
                    row["pid"] = "T" + digest(row)[:12]
                    f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"triads: {len(triads)}")

    # ---------------- format-experiment pairs
    pilot_pairs = []
    for c in range(12):
        key = json.load(open(J / f"walk2-key-{c}.json"))
        pilot_pairs += [tuple(p) for p in key["pairs"]]
    pilot_pairs = sorted(set(tuple(p) for p in pilot_pairs if len(set(p)) == 2))
    r = rng(PROTOCOL, "format-replication-sample", {"n": len(pilot_pairs)})
    rep = r.sample(pilot_pairs, 160)
    fresh_local, fresh_mixed = [], []
    k = 0
    while len(fresh_local) < 80:
        r = rng(PROTOCOL, "format-fresh-local", {"k": k}); k += 1
        rec = r.choice([x for x in recs if len(x["glyphs"]) >= 2])
        p = tuple(r.sample(rec["glyphs"], 2))
        if p not in fresh_local and p[::-1] not in fresh_local:
            fresh_local.append(p)
    k = 0
    mixed_pool = seed_glyphs + tail
    while len(fresh_mixed) < 80:
        r = rng(PROTOCOL, "format-fresh-mixed", {"k": k}); k += 1
        p = tuple(r.sample(mixed_pool, 2))
        if p not in fresh_mixed and p[::-1] not in fresh_mixed:
            fresh_mixed.append(p)
    with open(OUT / "format-pairs.jsonl", "w") as f:
        for stratum, lst in (("pilot-replication", rep), ("fresh-seed-local", fresh_local), ("fresh-mixed", fresh_mixed)):
            for i, (a, b) in enumerate(lst):
                for order, (x, y) in enumerate(((a, b), (b, a))):
                    row = {"set": "format", "pair": f"{stratum}:{i}", "stratum": stratum, "order": order, "a": x, "b": y}
                    row["pid"] = "F" + digest(row)[:12]
                    f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"format pairs: {len(rep)} + {len(fresh_local)} + {len(fresh_mixed)}")

    # ---------------- conflict battery (designer-built; annotations are HYPOTHETICAL axis labels)
    conflict = json.load(open(EXP / "harness/runner/conflict-items-v1.json"))
    with open(OUT / "conflict.jsonl", "w") as f:
        for it in conflict["items"]:
            for order, (x, y) in enumerate(((it["a"], it["b"]), (it["b"], it["a"]))):
                row = {"set": "conflict", "item": it["id"], "order": order, "a": x, "b": y, "annot": it["predict"]}
                row["pid"] = "C" + digest(row)[:12]
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"conflict items: {len(conflict['items'])}")

    # ---------------- holistic pairs + gestalt
    hol = json.load(open(EXP / "harness/runner/holistic-sets-v1.json"))
    noise = []
    for n in range(4):
        r = rng(PROTOCOL, "gestalt-noise", {"n": n})
        noise.append({"name": f"noise-{n}", "kind": "noise-foil", "order": r.sample(tail, 5 + (n % 2)), "src": "uniform-tail"})
    sets = hol["sets"] + noise
    with open(OUT / "holistic-pairs.jsonl", "w") as f:
        for s in sets:
            if not s.get("pairwise"):
                continue
            for a, b in combinations(s["order"], 2):
                for order, (x, y) in enumerate(((a, b), (b, a))):
                    row = {"set": "holistic-pairs", "seq": s["name"], "kind": s["kind"], "order": order, "a": x, "b": y,
                           "intended": [s["order"].index(x), s["order"].index(y)]}
                    row["pid"] = "H" + digest(row)[:12]
                    f.write(json.dumps(row, ensure_ascii=False) + "\n")
    with open(OUT / "gestalt.jsonl", "w") as f:
        for s in sets:
            for sh in range(3):
                g = list(s["order"])
                rng(PROTOCOL, "gestalt-shuffle", {"seq": s["name"], "shuffle": sh}).shuffle(g)
                row = {"set": "gestalt", "seq": s["name"], "kind": s["kind"], "shuffle": sh, "glyphs": g,
                       "intended": s["order"], "src": s.get("src")}
                row["pid"] = "G" + digest(row)[:12]
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"gestalt sets: {len(sets)} (x3 shuffles); pairwise sets: {sum(1 for s in sets if s.get('pairwise'))}")

if __name__ == "__main__":
    main()
