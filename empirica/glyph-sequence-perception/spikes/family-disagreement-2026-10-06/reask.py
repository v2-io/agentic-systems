"""How often a context is re-asked of a mind in a later round, by that mind's first answer there (continue answers,
plain variant): the adaptive selection that strengthening-2 §1 conditions on."""
import collections, irt
items, seq, S, N, X = irt.load("continue-stop")
for mm in ("sonnet55", "grok46", "haiku45nt"):
    c = collections.Counter()
    for q in items:
        L = sorted(seq[q].get(mm, []))
        if not L: continue
        c[(L[0][1], any(rd > L[0][0] for rd, _ in L[1:]))] += 1
    for y in (0, 1):
        n = c[(y, True)] + c[(y, False)]
        print(f"{mm:10s} first answer {'stop' if y else 'continue'}: n={n:6d}  re-asked in a later round {c[(y, True)]:5d} = {c[(y, True)] / n:.3f}")
