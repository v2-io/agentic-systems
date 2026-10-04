"""Synthetic worlds and minds, for validating the loop before any real call (PLAN.md §8 step 5).

A world plants sequences (with crossings, ties, a holistic one and a splice trap) among distractor glyphs.
A synthetic mind answers sheets by sampling the same generative model the fit assumes, plus its own
nuisance parameters, and writes its answer as the JSON text a real mind would, so parsing is exercised.
"""
import json, math
from common import R, ok_glyph
import model as M

def world_default():
    """Glyphs are drawn from real ranges only so they render; their meaning is irrelevant here."""
    A = [chr(0x2460 + i) for i in range(8)]                 # ①..⑧        long plain sequence
    B = [chr(0x2776 + i) for i in range(6)]                 # ❶..❻        crosses A? no; shares a bridge below
    C = [chr(0x2581 + i) for i in range(7)]                 # ▁..▇        plain
    D = [chr(0x25CB), chr(0x25D4), chr(0x25D1), chr(0x25D5), chr(0x25CF)]   # ○◔◑◕●  holistic (sets only)
    E = [chr(0x2680 + i) for i in range(6)]                 # ⚀..⚅        with a tie: ⚂=⚃ at one step
    bridge = A[4]                                           # ⑤ also sits inside the second splice-trap sequence
    F = [chr(0x2474 + i) for i in range(3)] + [bridge] + [chr(0x2474 + i) for i in range(3, 6)]   # ⑴⑵⑶⑤⑷⑸⑹
    seqs = {"A": [[g] for g in A], "C": [[g] for g in C], "D": [[g] for g in D],
            "E": [[E[0]], [E[1]], [E[2], E[3]], [E[4]], [E[5]]], "F": [[g] for g in F], "B": [[g] for g in B]}
    planted = set(g for s in seqs.values() for st in s for g in st)
    distract, i = [], 0
    while len(distract) < 160:
        cp = 0x2600 + R("synth-distract", {"i": i}).randrange(0x300); i += 1
        ch = chr(cp)
        if ch not in planted and ch not in distract and ch.isprintable() and ok_glyph(ch):
            distract.append(ch)
    return {"seqs": seqs, "distractors": distract,
            "holistic": ["D"],
            # noisy seeds: a reversed A missing a glyph, C with an interloper, F spliced into A at the bridge
            "seeds": [{"sid": "seedA", "glyphs": A[::-1][:-1]}, {"sid": "seedC", "glyphs": C[:4] + [distract[0]] + C[4:]},
                      {"sid": "seedSplice", "glyphs": A[:4] + [bridge] + F[4:]}, {"sid": "seedE", "glyphs": E},
                      {"sid": "seedD", "glyphs": D}]}

def minds_default():
    """name -> (family, theta, s3, s4 per planted sequence). B is planted but perceived by one family only."""
    base = {"eps": 0.08, "nn": 0.7, "nt": 0.1, "beta": 0.34, "tau": 0.7}
    def s(all3, all4, hol=("D",), only=None):
        out = {}
        for k in ("A", "B", "C", "D", "E", "F"):
            out[k] = (0.05 if k in hol else all3, all4)
        if only is not None:
            out["B"] = (0.0, 0.0) if not only else (all3, all4)
        return out
    return {
        "synA": ("famX", dict(base), s(0.9, 0.9, only=True)),
        "synB": ("famX", dict(base, eps=0.15, beta=0.7), s(0.8, 0.85, only=True)),       # slot-biased
        "synC": ("famY", dict(base, nn=0.95, eps=0.05), s(0.6, 0.8, only=False)),       # ⟂-prone
        "synD": ("famZ", dict(base, eps=0.4, nn=0.2, beta=0.6), s(0.5, 0.6, only=False)),  # noisy guesser
    }

class Truth:
    def __init__(self, world, minds):
        self.world, self.minds = world, minds
        self.names = list(world["seqs"])
        self.models = {}
        for m, (fam, th, sv) in minds.items():
            mod = M.Model([], [m])
            mod.theta[m] = dict(th)
            for k in self.names:
                cid = mod.add(M.Cand(world["seqs"][k]))
                mod.S[(m, cid, 3)], mod.S[(m, cid, 4)] = sv[k]
            self.models[m] = mod

    def answer_triad(self, m, shown, f, r):
        o = {"tri": tuple(sorted(shown)), "shown": tuple(shown), "ctx": 3, "forced": not f["perp"], "tie_ok": f["tie"], "w": 1}
        dist = M.predict(o, self.models[m], m)
        out = _sample(dist, r)
        if out[0] == "none":
            return {"none": True}
        if out[0] == "two":
            return {"two": [out[1], out[2]]}
        if out[0] == "mid":
            a, b = [g for g in shown if g != out[1]]
            seq = [a, out[1], b]
        elif out[0] == "tie2":
            seq = [out[1], [out[2], out[3]]]
        else:
            seq = [list(shown)]
        return {"seq": seq if r.random() < 0.5 else seq[::-1]}

    def answer_order(self, m, shown, f, r):
        fam, th, sv = self.minds[m]
        if r.random() < th["eps"]:
            n = r.randint(3, len(shown)); return {"seqs": [shown[:n]], "extra": shown[n:]}
        lines, used = [], set()
        for k in self.names:
            st = [[g for g in s if g in shown and g not in used] for s in self.world["seqs"][k]]
            st = [s for s in st if s]
            if sum(len(s) for s in st) < 3 or r.random() >= sv[k][1 if len(shown) >= 4 else 0]:
                continue
            for s in st:
                used.update(s)
            line = [s[0] if (len(s) == 1 or not f["tie"]) else s for s in st]
            flat = []
            for s in line:
                if isinstance(s, list) and not f["tie"]:
                    flat += s
                else:
                    flat.append(s)
            lines.append(flat if r.random() < 0.5 else flat[::-1])
        rest = [g for g in shown if g not in used]
        if not f["perp"]:
            one = (lines[0] if lines else []) + [g for g in shown if g not in set(_flat(lines[:1]))]
            return {"seqs": [one]}
        if not lines:
            return {"none": True}
        return {"seqs": lines, "extra": rest}

    def answer_next(self, m, shown, f, r, between=False):
        fam, th, sv = self.minds[m]
        if between:
            gi = shown.index("GAP"); a, b = shown[gi - 1], shown[gi + 1]
        for k in self.names:
            flat = [s[0] for s in self.world["seqs"][k]]
            if between:
                if a in flat and b in flat and abs(flat.index(a) - flat.index(b)) == 2 and r.random() < sv[k][0]:
                    return {"between": [flat[(flat.index(a) + flat.index(b)) // 2]]}
                continue
            x, y = shown[-2], shown[-1]
            if x in flat and y in flat and abs(flat.index(x) - flat.index(y)) == 1 and r.random() < sv[k][0]:
                d = flat.index(y) - flat.index(x); j = flat.index(y) + d
                if 0 <= j < len(flat):
                    return {"next": [flat[j]]}
        if r.random() < th["eps"] * 0.3:
            pool = self.world["distractors"]
            return {("between" if between else "next"): [pool[r.randrange(len(pool))]]}
        return {"none": True}

    def answer_sheet(self, m, sheet):
        r = R("synth-answer", {"mind": m, "sid": sheet["sid"]})
        out = []
        for e in sheet["entries"]:
            sh, f = e["shown"], sheet["factors"]
            if sheet["kind"] == "triad":
                a = self.answer_triad(m, sh, f, r)
            elif sheet["kind"] == "order":
                a = self.answer_order(m, sh, f, r)
            else:
                a = self.answer_next(m, sh, f, r, between=sheet["kind"] == "between")
            out.append({"id": e["id"], **a})
        return json.dumps({"answers": out}, ensure_ascii=False)

def _flat(lines):
    out = []
    for l in lines:
        for s in l:
            out += s if isinstance(s, list) else [s]
    return out

def _sample(dist, r):
    x, acc = r.random() * sum(dist.values()), 0.0
    for k in sorted(dist, key=str):
        acc += dist[k]
        if x <= acc:
            return k
    return sorted(dist, key=str)[-1]
