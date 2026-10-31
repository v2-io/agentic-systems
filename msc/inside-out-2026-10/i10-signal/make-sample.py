#!/usr/bin/env python3
"""Draw the fixed I.10 claim sample once. Reruns of the measure read sample.tsv, not this.

Population: segment slugs (no old-* legacy files) present under the same slug at both
the tag and the given ref. Random stratum: 30 claims, seeded, by volume (01: 20, 02-04: 4/3/3),
with Volume 1 split into terciles of Working-Notes size at the tag. Purposive stratum: the
canon targets of influx-scout/MAP.md section 3 (labelled; it is where the drain looked).

    python3 -I make-sample.py [REF]   (default HEAD) > sample.tsv
"""
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, HERE)
import i10lib as L  # noqa: E402

TAG = "pre-integration-2026-10-30"
SEED = "I.10 2026-10-30"
PER_VOL = {"01-aat-core": 20, "02-tst-core": 4, "03-llm-core": 3, "04-eli-core": 3}
PURPOSIVE = ["der-loop-interventional-access", "impl-causal-access", "deriv-causal-ib-lmi",
             "der-turnover-information-recursion", "der-compensation-channel-uniqueness",
             "def-death-as-factor-loss", "def-model-sufficiency", "result-structural-adaptation-necessity",
             "disc-compression-operations", "form-information-bottleneck", "impl-strategy-dynamics",
             "deriv-observation-ambiguity-bias-bound", "hyp-solicitable-escape", "hyp-truth-serving-loophole",
             "disc-ciy-unified-objective", "scope-moral-continuity"]


def segs(repo, ref):
    out = {}
    for n in L.git(["ls-tree", "-r", "--name-only", ref], repo).decode().split("\n"):
        m = L.SEG_RE.match(n)
        if m and not m.group(2).startswith("old-"):
            out[m.group(2)] = (m.group(1), n)
    return out


def main():
    ref = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    repo = L.git(["rev-parse", "--show-toplevel"], HERE).decode().strip()
    a, b = segs(repo, TAG), segs(repo, ref)
    pop = sorted(s for s in a if s in b and a[s][0] == b[s][0])
    snap = L.load_snapshot(repo, TAG)
    wnw = {s: L.words(L.split_segment(snap[a[s][1]])[1]) for s in pop}
    rng = random.Random(SEED)
    rows = []
    for vol, k in PER_VOL.items():
        vs = [s for s in pop if a[s][0] == vol]
        if vol == "01-aat-core":
            vs.sort(key=lambda s: (wnw[s], s))
            t = len(vs) // 3
            parts = [("01-wn-low", vs[:t]), ("01-wn-mid", vs[t:2 * t]), ("01-wn-high", vs[2 * t:])]
            alloc = [7, 7, 6]
            for (name, part), n in zip(parts, alloc):
                rows += [(s, "random:" + name) for s in sorted(rng.sample(sorted(part), n))]
        else:
            rows += [(s, "random:" + vol[:2]) for s in sorted(rng.sample(vs, k))]
    picked = {s for s, _ in rows}
    rows += [(s, "purposive:map-s3") for s in PURPOSIVE if s in pop and s not in picked]
    print(f"# I.10 sample, drawn by make-sample.py (seed {SEED!r}) over {len(pop)} slugs present at {TAG} and {ref}")
    print("slug\tstratum\ttag_wn_words")
    for s, g in rows:
        print(f"{s}\t{g}\t{wnw[s]}")


if __name__ == "__main__":
    main()
