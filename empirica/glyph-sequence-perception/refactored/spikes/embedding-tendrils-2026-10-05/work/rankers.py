"""Context-free tendril rankers over the spike universe (derived/emb/glyphs.json).

Each ranker maps a node glyph q to a score per universe glyph (higher = proposed earlier).
  cp          codepoint distance (the study's current faint prior), ties broken toward +1
  name        Unicode-name token overlap (cosine over name-token sets), random ties
  name>cp     `name`, ties broken by codepoint distance
  name>cp+num `name>cp`, plus a bonus when both glyphs carry a Unicode numeric value one apart
  emb:<file>  cosine in a cached embedding (derived/emb/<file>.npy)
"""
import json, re
import numpy as np
from lib import DER, ucd

EMB = DER / "emb"
GL = json.load(open(EMB / "glyphs.json"))
IDX = {g: i for i, g in enumerate(GL)}
CP = np.array([ord(g) for g in GL], dtype=np.int64)
# Ties are broken by a fixed random jitter unless a ranker NAMES its tiebreak ("name>cp"): an earlier draft broke
# embedding ties by codepoint distance, which made a collapsed embedding (all-minilm maps 23,541 of 25,362 glyphs to
# one vector) look nearly as good as codepoint order. Credit must go to the information the ranker itself carries.
JITTER = np.random.default_rng(20261005).random(len(GL)) * 1e-9

def cp_scores(q):
    d = CP - ord(q)
    return -np.abs(d).astype(np.float64) + 0.25 * (d > 0)

_tok = None
def _tokens():
    global _tok
    if _tok is None:
        import scipy.sparse as sp
        vocab, rows, cols = {}, [], []
        for i, g in enumerate(GL):
            n = (ucd().get(g) or [""])[0]
            toks = set(re.split(r"[ \-]+", n)) - {""}
            for t in toks:
                rows.append(i); cols.append(vocab.setdefault(t, len(vocab)))
        M = sp.csr_matrix((np.ones(len(rows), dtype=np.float32), (rows, cols)), shape=(len(GL), len(vocab)))
        norm = np.sqrt(np.asarray(M.sum(1)).ravel()) + 1e-9
        _tok = (M, norm)
    return _tok

def name_scores(q):
    M, norm = _tokens()
    i = IDX[q]
    s = np.asarray((M @ M[i].T).todense()).ravel() / (norm * norm[i])
    return s + JITTER

def name_cp_scores(q):
    """name similarity, ties broken by codepoint distance (a composite, named as such)"""
    return name_scores(q) - JITTER - 1e-7 * np.abs(CP - ord(q))

_num = None
def name_num_scores(q):
    global _num
    if _num is None:
        _num = np.array([(ucd().get(g) or [0, 0, None])[2] if (ucd().get(g) or [0, 0, None])[2] is not None else np.nan
                         for g in GL], dtype=np.float64)
    s = name_cp_scores(q)
    nq = _num[IDX[q]]
    if not np.isnan(nq):
        s = s + 0.5 * (np.abs(np.nan_to_num(_num, nan=1e9) - nq) == 1)
    return s

_emb = {}
def emb_scores(fname, q):
    if fname not in _emb:
        X = np.load(EMB / f"{fname}.npy").astype(np.float32)
        X /= (np.linalg.norm(X, axis=1, keepdims=True) + 1e-9)
        _emb[fname] = X
    X = _emb[fname]
    return (X @ X[IDX[q]]).astype(np.float64) + JITTER

def get(spec):
    if spec == "cp":
        return cp_scores
    if spec == "name":
        return name_scores
    if spec == "name>cp":
        return name_cp_scores
    if spec == "name>cp+num":
        return name_num_scores
    if spec.startswith("emb:"):
        f = spec[4:]
        return lambda q: emb_scores(f, q)
    raise KeyError(spec)
