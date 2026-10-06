"""Flat disagreements: questions where two raters (minds, or families pooled) each answered at least NMIN times, each
is at least UNAN unanimous, and their modal answers differ. Against a null that shuffles the rater labels among the
question's answers (keeping each rater's count): how many flat disagreements would sampling noise alone produce?"""
import collections, random, sys
import lib
from values import value, ckey

NMIN, UNAN = 3, 0.8

def load_by(kinds, group):
    recs, man = lib.load()
    by = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in recs:
        if r["kind"] not in kinds or r["era"] == "seed": continue
        if (r.get("tags") or {}).get("variant") not in (None, "plain"): continue
        v = value(r)
        if v is None: continue
        g = group(r)
        if g: by[ckey(r)][g].append(v)
    return by

def is_flat(va, vb):
    ca, cb = collections.Counter(va), collections.Counter(vb)
    (xa, na), (xb, nb) = ca.most_common(1)[0], cb.most_common(1)[0]
    return xa != xb and na / len(va) >= UNAN and nb / len(vb) >= UNAN

def run(by, A, B, perms=200):
    items = [(d[A], d[B]) for d in by.values() if len(d.get(A, [])) >= NMIN and len(d.get(B, [])) >= NMIN]
    obs = sum(is_flat(a, b) for a, b in items)
    rng = random.Random(0); null = []
    for _ in range(perms):
        c = 0
        for a, b in items:
            allv = a + b; rng.shuffle(allv)
            c += is_flat(allv[:len(a)], allv[len(a):])
        null.append(c)
    null.sort()
    return len(items), obs, sum(null) / perms, null[int(0.975 * perms)]

FAMG = lambda r: r["family"] if r["family"] in ("claude", "grok", "gemini") else None
FRONT = {"sonnet55": "claude-front", "opus55": "claude-front", "grok46": "grok", "gemini38flash": "gemini",
         "gemini31pro": "gemini", "haiku45nt": "haiku-nt", "haiku45": "haiku-t"}
if __name__ == "__main__":
    for kind in sys.argv[1:] or ["continue", "cohere", "inhibit", "triad", "order", "next", "pick"]:
        for name, grp, pairs in (
            ("families", FAMG, [("claude", "grok"), ("claude", "gemini"), ("grok", "gemini")]),
            ("groups", lambda r: FRONT.get(r["mind"]) or ({"sonnet55g": "sonnet-g", "haiku45g": "haiku-g", "grok46g": "grok-g", "gemini38flashg": "gemini-g"}.get(r["mind"])),
             [("claude-front", "grok"), ("claude-front", "gemini"), ("grok", "gemini"), ("claude-front", "haiku-nt"),
              ("claude-front", "haiku-t"), ("haiku-nt", "grok"), ("sonnet-g", "haiku-g"), ("sonnet-g", "grok-g"),
              ("haiku-g", "grok-g"), ("sonnet-g", "gemini-g"), ("grok-g", "gemini-g")])):
            by = load_by({kind}, grp)
            for A, B in pairs:
                n, obs, nm, n975 = run(by, A, B)
                if n >= 20:
                    print(f"{kind:9s} {name:8s} {A:13s} {B:10s} items={n:5d} flat={obs:4d} ({obs/n:.3f})  null mean={nm:6.1f} 97.5%={n975}")
