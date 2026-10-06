"""The catalog's links (CATALOG v5 §4-§6, §8, §9): every link c -> x at its own context c, with

  G   generation, in three channels kept apart: SHOWN (the first glyph a mind wrote after the context it was shown, or
      a triad-era `next` answer's first proposal, its rank kept), WRITTEN (each later glyph of a continue answer, at
      the context the mind had itself written: everything shown and written before it, its last <= 8 glyphs trimmed
      back to the nearest repeat, as the tree does), and PICKED (forced single picks, nulls excluded). Per rater and
      per family: k naming x of n answers at c. Raw shares with Jeffreys intervals; the calibrated likelihood ratio of
      §9 is a later build.
  L   recognition: inhibit answers at (c, x), controls excluded, against each rater's NEAR decoy rate -- per rater
      Abbott's (p - c) / (1 - c), precision-weighted within a family, families combined by their discrimination on
      R's "other" class (the R part's weights); certainty a Bayes factor for beta > 0 with one beta common to the
      raters, each with its own c (as build 0's R).

and, for links inside a record's run, a STATE (§8), per reading direction, the better kept:
  1 full      evidence at its own full-prefix context (the whole run before it, when that is 2-8 glyphs)
  2 stable    evidence at a suffix of it, and the longest showable context (the full prefix, or its last 8 glyphs)
              has been shown to minds with no other glyph as their top answer (lengthening tested to the cap, no flip)
  3 suffix    evidence at a suffix only: the longest showable context not shown, or shown with another glyph on top
              (a FLIP, flagged)
  4 picks     pick evidence at a context of 9-24 glyphs only (beyond what shown questions reach)
  5 none
"Evidence" is >= EVIDENCE_MIN answers naming x (any channel) or saying yes to it (L). Nothing is pooled across context
lengths: a link at a long context and at its suffix are different propositions (§4).

Reasoned and reflection answers, pick nulls and seed votes are not G (METHODOLOGY §3, §4; CATALOG §5); seeds enter
later as their own rater. Never reads `source`.
"""
import collections, math

NONE, OTHER = "<none>", "<other>"
MAXK = 8
PICK_MAXK = 24

def rater(r):
    t = r.get("tags") or {}
    return f'{r["mind"]}|{t.get("variant") or "plain"}|{r.get("era")}'

def beta_mv(k, n):
    a, b = k + 0.5, n - k + 0.5
    return a / (a + b), a * b / ((a + b) ** 2 * (a + b + 1))

def written_contexts(ctx, seq):
    """(context, next) for every glyph after the first of a continue answer, as tree.Tree builds `written`"""
    out = []
    S = list(ctx) + list(seq)
    for i in range(1, len(seq)):
        c2 = list(S[max(0, len(ctx) + i - MAXK):len(ctx) + i])
        while len(set(c2)) < len(c2):
            c2 = c2[1:]
        if len(c2) >= 2:
            out.append((tuple(c2), seq[i]))
    return out

class Links:
    def __init__(self, recs):
        self.shown = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))     # ctx -> rater -> first
        self.written = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))   # ctx -> rater -> next
        self.picks = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))     # ctx -> rater -> x
        self.inhibit = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0]))        # (ctx, x) -> rater -> [yes, n]
        self.near = collections.defaultdict(lambda: [0, 0])                                            # rater -> [yes, n]
        self.aids = collections.defaultdict(list)                                                      # (channel, ctx, x) -> [aid]
        self.ranks = collections.defaultdict(list)                                                     # (ctx, x) -> next ranks
        self.fam = {}
        for r in recs:
            k, o, t = r["kind"], r.get("outcome"), r.get("tags") or {}
            if k == "seed":
                continue
            rt = rater(r)
            self.fam[rt] = r["family"]
            if k in ("continue", "next") and t.get("variant") not in ("reasoned", "reflection") \
                    and o in ("continuation", "proposals", "none", "other"):
                ctx = tuple(r["context"])
                if o == "none":
                    first = NONE
                elif k == "next":
                    props = sorted(r.get("proposals", []), key=lambda p: p["rank"])
                    first = props[0]["g"] if props else OTHER
                    for p in props:
                        self.ranks[(ctx, p["g"])].append(p["rank"])
                else:
                    seq = r.get("continuation") or []
                    first = seq[0] if seq else OTHER
                    for c2, x in written_contexts(ctx, seq):
                        self.written[c2][rt][x] += 1
                        self.aids[("W", c2, x)].append(r["aid"])
                self.shown[ctx][rt][first] += 1
                self.aids[("S", ctx, first)].append(r["aid"])
            elif k == "pick" and o in ("continuation", "none", "other") and not t.get("null"):
                ctx = tuple(r["context"])
                x = r["continuation"][0] if o == "continuation" else (NONE if o == "none" else OTHER)
                self.picks[ctx][rt][x] += 1
                self.aids[("P", ctx, x)].append(r["aid"])
            elif k == "inhibit" and o in ("yes", "no", "cant-tell"):
                y = 1 if o == "yes" else 0
                if t.get("control") == "near":
                    self.near[rt][0] += y; self.near[rt][1] += 1
                elif not t.get("control"):
                    c = self.inhibit[(tuple(r["context"]), r["candidate"])][rt]; c[0] += y; c[1] += 1
                    self.aids[("L", tuple(r["context"]), r["candidate"])].append(r["aid"])

    # ---- facts at one context
    def naming(self, ctx, x):
        """answers naming x at ctx, by channel: {"S": k, "W": k, "P": k, "L": yes}"""
        ctx = tuple(ctx)
        return {"S": sum(c.get(x, 0) for c in self.shown.get(ctx, {}).values()),
                "W": sum(c.get(x, 0) for c in self.written.get(ctx, {}).values()),
                "P": sum(c.get(x, 0) for c in self.picks.get(ctx, {}).values()),
                "L": sum(v[0] for v in self.inhibit.get((ctx, x), {}).values())}

    def evidence(self, ctx, x, minimum):
        return sum(self.naming(ctx, x).values()) >= minimum

    def shown_top(self, ctx):
        c = collections.Counter()
        for v in self.shown.get(tuple(ctx), {}).values():
            c.update(v)
        if not c:
            return None
        return max(c.items(), key=lambda kv: (kv[1], kv[0]))[0]

    # ---- the state of a link inside a run (§8)
    def state(self, run, i, minimum):
        """link run[i] -> run[i+1], read forward (prefix run[:i+1]) and backward (prefix run[i+1:] reversed); the better
        direction's state -> dict"""
        best = None
        for d, (F, x) in (("forward", (list(run[:i + 1]), run[i + 1])), ("backward", (list(run[i + 1:])[::-1], run[i]))):
            st = self._state(F, x, minimum)
            st["direction"] = d
            if best is None or st["state"] < best["state"]:
                best = st
        return best

    def _state(self, F, x, minimum):
        L = len(F)
        cap = tuple(F[-MAXK:])
        if 2 <= L <= MAXK and self.evidence(F, x, minimum):
            return {"state": 1, "context": "".join(F), "flip": False}
        suff = [j for j in range(2, min(MAXK, L) + 1) if self.evidence(F[-j:], x, minimum)]
        if suff:
            s = max(suff)
            flips = [j for j in range(s + 1, min(MAXK, L) + 1)
                     if self.shown_top(F[-j:]) not in (None, x, NONE, OTHER)]
            if len(cap) >= 2 and self.shown_top(cap) is not None and not flips:
                return {"state": 2, "context": "".join(F[-s:]), "flip": False}
            return {"state": 3, "context": "".join(F[-s:]), "flip": bool(flips)}
        for j in range(min(PICK_MAXK, L), MAXK, -1):
            if sum(c.get(x, 0) for c in self.picks.get(tuple(F[-j:]), {}).values()) >= minimum:
                return {"state": 4, "context": "".join(F[-j:]), "flip": False}
        return {"state": 5, "context": "", "flip": False}

    # ---- the link table
    def all_links(self):
        keys = set()
        for store in (self.shown, self.written, self.picks):
            for ctx, by in store.items():
                for c in by.values():
                    keys |= {(ctx, x) for x in c if x not in (NONE, OTHER)}
        keys |= set(self.inhibit)
        return sorted(keys, key=lambda kv: ([ord(c) for c in kv[0]], ord(kv[1])))

    def channel_fam(self, store, ctx, x):
        """per family: [k naming x, n answers at ctx]"""
        out = collections.defaultdict(lambda: [0, 0])
        for rt, c in store.get(tuple(ctx), {}).items():
            f = self.fam[rt]
            out[f][0] += c.get(x, 0); out[f][1] += sum(c.values())
        return {f: v for f, v in out.items()}

    def l_part(self, ctx, x, weights, bf_excess, grid):
        """L at (ctx, x): per family strength (precision-weighted Abbott) and counts; combined by `weights`; BF"""
        by = self.inhibit.get((tuple(ctx), x))
        if not by:
            return None
        fam = collections.defaultdict(lambda: [0.0, 0.0]); counts = collections.defaultdict(lambda: [0, 0]); obs = []
        for rt, (y, n) in sorted(by.items()):
            cy, cn = self.near.get(rt, (0, 0))
            if not cn:                                       # the rater's family-mates' near decoys, else nothing
                f = self.fam[rt]
                cy = sum(v[0] for r_, v in self.near.items() if self.fam.get(r_) == f)
                cn = sum(v[1] for r_, v in self.near.items() if self.fam.get(r_) == f)
            if not cn or not n:
                continue
            (m, v), (mc, vc) = beta_mv(y, n), beta_mv(cy, cn)
            a = (m - mc) / (1 - mc)
            va = (v + vc * ((1 - m) / (1 - mc)) ** 2) / (1 - mc) ** 2
            f = self.fam[rt]
            fam[f][0] += a / va; fam[f][1] += 1 / va
            counts[f][0] += y; counts[f][1] += n
            obs.append((y, n - y, mc))
        fams = {f: (s / p, (1 / p) ** 0.5) for f, (s, p) in fam.items() if p}
        num = den = var = 0.0
        for f, (a, sd) in fams.items():
            w = weights.get(f, 0.0)
            num += w * a; den += w; var += (w * sd) ** 2
        return {"families": {f: {"strength": round(a, 4), "sd": round(sd, 4), "yes": counts[f][0], "n": counts[f][1]}
                             for f, (a, sd) in fams.items()},
                "strength": (num / den) if den else None, "sd": (var ** 0.5 / den) if den else None,
                "bf": bf_excess(obs, grid) if obs else None}
