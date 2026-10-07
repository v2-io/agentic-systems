"""De novo 3, check 6: how big are the 'sequences' (block-set groups) the sequence-level effect is estimated over?"""
import sys, collections, pathlib, numpy as np
SP = pathlib.Path(__file__).resolve().parent.parent; sys.path.insert(0, str(SP)); import os; os.chdir(SP)
import irt, features as F
items, seq, S, N, X = irt.load("continue-stop")
grp = [frozenset(F.block(g) for g in q[1]) for q in items]
ni = collections.Counter(grp); na = collections.Counter()
for i, g in enumerate(grp): na[g] += N[i].sum()
tot = N.sum(); print(f"items {len(items)}, answers {int(tot)}, block-set groups {len(ni)}")
sz = np.array(sorted(ni.values(), reverse=True)); print("items per group: median", np.median(sz), "groups with 1 item", int((sz == 1).sum()), "with >= 20 items", int((sz >= 20).sum()))
top = na.most_common(10); print("answers in the 10 largest groups: %.2f" % (sum(v for _, v in top) / tot))
for g, v in top: print("   ", sorted(g), int(v), ni[g])
print("single-block groups' share of answers: %.2f" % (sum(v for g, v in na.items() if len(g) == 1) / tot))
print("per-answer scale: 1,500 nats / answers = %.4f nats per answer; per item = %.3f" % (1500 / tot, 1500 / len(items)))
