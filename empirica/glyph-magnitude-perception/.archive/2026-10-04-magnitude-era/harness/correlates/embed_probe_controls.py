#!/usr/bin/env python3
"""Controls for embed_probe.py (exploratory tier).

C1 codepoint confound: many ladders are filed in codepoint order, and byte-level embeddings of
   neighbouring codepoints differ systematically, so a 'more' direction could just be a codepoint
   direction. Report LOFO transfer separately for ladders whose order is codepoint-ascending
   (Spearman(cp, order) >= 0.8) vs not (< 0.8, incl. reversed/scrambled filings).
C2 number vs non-number: train only on numeric-notation ladders, test on non-numeric ladders, and
   the reverse -- is the direction that orders denoted number the same one that orders fill/size/count?
"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import embed_probe as P

NUMERIC = {"circled", "neg-circled", "roman", "roman-lc", "superscript", "subscript", "eighths", "cjk",
           "circled-cjk", "suzhou", "dingbat-sans", "rods", "si-length"}

def main():
    fams = {k: list(v) for k, v in P.LADDERS.items()}
    cpmono = {f: P.spearman([ord(g) for g in gs], list(range(len(gs)))) for f, gs in fams.items()}
    res = {}
    for model in ("qwen3-embedding", "embeddinggemma:300m", "snowflake-arctic-embed2", "bge-m3"):
        E = {g: P.unit(e) for g, e in P.embed(model, sorted({g for v in fams.values() for g in v})).items()}
        t2 = json.load(open(P.EXP / "analysis/embed-probe-v0.json"))[model]["T2"]
        asc = [t2[f] for f in fams if cpmono[f] >= 0.8]; non = [t2[f] for f in fams if cpmono[f] < 0.8]
        def cross(train, test):
            X, y = [], []
            for f in train:
                for i, g in enumerate(fams[f]):
                    X.append(E[g]); y.append(i / (len(fams[f]) - 1))
            pred = P.ridge_dual(X, y, 1.0)
            return {f: round(P.spearman([pred(E[g]) for g in fams[f]], list(range(len(fams[f])))), 2) for f in test}
        num = [f for f in fams if f in NUMERIC]; non_num = [f for f in fams if f not in NUMERIC]
        n2v = cross(num, non_num); v2n = cross(non_num, num)
        res[model] = {"LOFO_codepoint_ascending": (round(P.mean(asc), 2), len(asc)),
                      "LOFO_not_codepoint_ascending": (round(P.mean(non), 2), len(non)),
                      "not_ascending_families": {f: (round(cpmono[f], 2), t2[f]) for f in fams if cpmono[f] < 0.8},
                      "numeric->nonnumeric_mean": round(P.mean(list(n2v.values())), 2), "numeric->nonnumeric": n2v,
                      "nonnumeric->numeric_mean": round(P.mean(list(v2n.values())), 2), "nonnumeric->numeric": v2n}
        r = res[model]
        print(f"{model:<24} LOFO cp-ascending {r['LOFO_codepoint_ascending']} | not-ascending {r['LOFO_not_codepoint_ascending']} | "
              f"num->non {r['numeric->nonnumeric_mean']:+.2f} | non->num {r['nonnumeric->numeric_mean']:+.2f}")
        print("    not-ascending (cp-rho, LOFO rho):", r["not_ascending_families"])
    json.dump(res, open(P.EXP / "analysis/embed-probe-v0-controls.json", "w"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    main()
