"""Glyph covariates of a context, from its glyphs alone (de-novo-feedback-3 §2b's list): contiguous, monotone (not
contiguous), one block, number of blocks, length and its square (centred), log size of the last step. The familiarity
flag x stays separate (irt.load's X)."""
import math, numpy as np
import features as F

NAMES = ["contiguous", "monotone", "one_block", "n_blocks", "length", "length_sq", "log_last_step"]
def covs(items):
    rows = []
    for q in items:
        c = list(q[1]); cc = F.chart_class(c); nb = len({F.block(g) for g in c}); L = len(c)
        step = abs(ord(c[-1]) - ord(c[-2])) if L >= 2 else 0
        rows.append([cc == "contiguous", cc == "monotone", nb == 1, nb, L, L * L, math.log1p(step)])
    A = np.array(rows, float)
    A[:, 3:] = (A[:, 3:] - A[:, 3:].mean(0)) / A[:, 3:].std(0)
    return A
