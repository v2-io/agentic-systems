"""Model-free test of 'a flat split is settled' (de-novo-feedback-1 §1 and the debrief's 'asking again won't settle
anything'). Answers per (item, mind) in round order. (1) For each mind: given its first two answers agree, the share of
later answers (3rd onward) that repeat them; split by which way the first two went. (2) For pairs: items whose first two
answers from A are both 0 and from B both 1 (a flat split after two each): what A and B answered next, where they did.
Compared with the calibrated mixture model's prediction for the same next answers (posterior from all earlier answers
of every mind on that item)."""
import collections, sys
import numpy as np
import irt

name = sys.argv[1] if len(sys.argv) > 1 else "continue-stop"
variant = sys.argv[2] if len(sys.argv) > 2 else "2mf"
items, seq, S, N, X = irt.load(name)
pl, mix, fam = int(variant[0]), "m" in variant, "f" in variant
m = irt.Model(pl, mix, fam).fit(S, N, X)
M = irt.MINDS

def posterior_from(i, upto):          # posterior over components given answers in rounds < upto (all minds)
    s = np.zeros((1, len(M))); n = np.zeros((1, len(M)))
    for mm, L in seq[items[i]].items():
        for rd, y in L:
            if rd < upto: s[0, M.index(mm)] += y; n[0, M.index(mm)] += 1
    L = m.comp_loglik(s, n, X[i:i+1])[0]
    return np.exp(L - np.logaddexp.reduce(L))

print(f"== {name}, model {variant}")
print("(1) per mind: first two answers agree -> later answers repeat them (observed / model-predicted)")
for mm in M:
    c = collections.defaultdict(lambda: [0, 0, 0.0])
    for i, q in enumerate(items):
        L = sorted(seq[q].get(mm, []), key=lambda t: t[0])
        if len(L) >= 3 and L[0][1] == L[1][1] and L[2][0] > L[1][0]:
            first = L[0][1]
            r = posterior_from(i, L[2][0]); p = m.comp_probs(X[i])[:, M.index(mm)] @ r
            k = c[first]; k[0] += L[2][1] == first; k[1] += 1; k[2] += p if first == 1 else 1 - p
    row = "  ".join(f"first two {'1' if f else '0'}: {a}/{n} = {a/n:.3f} (model {e/n:.3f})" for f, (a, n, e) in sorted(c.items()) if n >= 10)
    if row: print(f"   {mm:14s} {row}")
print("(2) after a flat split (A: 0,0; B: 1,1), the next answers")
for A, B in irt.PAIRS + [("grok46", "sonnet55"), ("haiku45nt", "sonnet55"), ("grok46", "haiku45nt")]:
    a_rep = a_n = b_rep = b_n = 0; ea = eb = 0.0; nflat = 0
    for i, q in enumerate(items):
        La = sorted(seq[q].get(A, []), key=lambda t: t[0]); Lb = sorted(seq[q].get(B, []), key=lambda t: t[0])
        if len(La) >= 2 and len(Lb) >= 2 and La[0][1] == La[1][1] == 0 and Lb[0][1] == Lb[1][1] == 1:
            nflat += 1
            t0 = max(La[1][0], Lb[1][0])
            for (L, who) in ((La, "a"), (Lb, "b")):
                later = [(rd, y) for rd, y in L[2:] if rd > t0]
                if later:
                    rd, y = later[0]; r = posterior_from(i, rd)
                    p = m.comp_probs(X[i])[:, M.index(A if who == "a" else B)] @ r
                    if who == "a": a_n += 1; a_rep += y == 0; ea += 1 - p
                    else: b_n += 1; b_rep += y == 1; eb += p
    if nflat:
        print(f"   A={A:13s} stops never, B={B:13s} always: flat items {nflat:4d}; A's next answer repeats {a_rep}/{a_n} (model {ea/max(a_n,1):.2f}); B's next repeats {b_rep}/{b_n} (model {eb/max(b_n,1):.2f})")
