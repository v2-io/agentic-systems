#!/usr/bin/env python3
"""Seed sequences as tagged votes (Joseph, 2026-10-05):

  "I think you can add the seed edges as equivalent to a vote from that agent's LLM, wherever that makes sense --
   possibly marking it specifically as from the seed so potentially biased -- it will be very useful for me from a
   practical engineering perspective to get the most relevant sequences as quickly as possible, while allowing us to
   segregate those out if we need a more pure analysis for a write-up."

  port_seeds.py   -> ../data/answers/seeds.jsonl  (regenerable; records with era "seed", kind "seed")

Where it makes sense: a survey record of type sequence / morph / cyclic / generator, written by a known surveyor
model, is that model writing a path. Each glyph after the first two becomes a vote, from the surveyor's family, for
that glyph as the continuation of the context before it (its last <= 8 glyphs, back to the nearest repeat), in both
reading directions (a sequence and its reverse are one sequence). Not used: the survey's `negative` records (they
judged magnitude ladders, a different question), equivalence / set / question / meta records, and the domain seeds
in data/seeds/ (generated lattices and lists, not anyone's perception).
Surveyor -> family: grok-* -> grok; sonnet*, fable-* -> claude.
"""
import hashlib, json, pathlib, unicodedata as U

HERE = pathlib.Path(__file__).resolve()
STUDY = HERE.parents[2]
OUT = HERE.parents[1] / "data" / "answers" / "seeds.jsonl"
TYPES = {"sequence", "morph", "cyclic", "generator"}

def family(surveyor):
    s = (surveyor or "").lower()
    if s.startswith("grok"):
        return "grok"
    if s.startswith("sonnet") or s.startswith("fable"):
        return "claude"
    return None

def is_glyph(ch):
    return len(ch) == 1 and U.category(ch)[0] in "LNPS" and not ch.isspace()

def main():
    seeds = [json.loads(l) for l in open(STUDY / "data" / "seeds.jsonl") if l.strip()]
    out, used, skipped = [], 0, {}
    for sd in seeds:
        fam = family(sd.get("surveyor"))
        if sd.get("type") not in TYPES or not fam or not sd["sid"].startswith("survey:"):
            skipped[sd.get("type") if fam else "no surveyor model"] = skipped.get(sd.get("type") if fam else "no surveyor model", 0) + 1
            continue
        g = [U.normalize("NFC", x) for x in sd["glyphs"]]
        if len(g) < 3 or not all(is_glyph(x) for x in g):
            skipped["too short or non-glyph"] = skipped.get("too short or non-glyph", 0) + 1
            continue
        used += 1
        for direction, seq in (("forward", g), ("reverse", g[::-1])):
            for i in range(2, len(seq)):
                ctx = seq[max(0, i - 8):i]
                while len(set(ctx)) < len(ctx):          # back to the nearest repeat: contexts hold distinct glyphs
                    ctx = ctx[1:]
                if len(ctx) < 2 or seq[i] in ctx:
                    continue
                out.append({"aid": "A" + hashlib.sha256(json.dumps([sd["sid"], direction, i]).encode()).hexdigest()[:16],
                            "era": "seed", "round": "seed", "kind": "seed", "outcome": "continuation",
                            "mind": sd["surveyor"], "family": fam, "context": ctx, "continuation": [seq[i]],
                            "tags": {"seed_type": sd["type"], "direction": direction}, "source": {"seed": sd["sid"]}})
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w") as f:
        for r in out:
            f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")
    print(f"{used} seeds -> {len(out)} seed votes -> {OUT}; not used: {skipped}")

if __name__ == "__main__":
    main()
