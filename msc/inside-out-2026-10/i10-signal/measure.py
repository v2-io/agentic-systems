#!/usr/bin/env python3
"""I.10: where is something written about a claim, and how much must a cold agent read?

Usage (from anywhere; paths default to this directory and the asf repo it sits in):

    python3 -I measure.py REF [REF ...] [--sample sample.tsv] [--all] [--out-dir DIR] [--label NAME]

Each REF is an asf git ref (tag, sha, branch). The influx outside asf is read
from disk once and used for every REF in the run (see METHOD.md, "Influx").
Writes, per run:  <label>-claims.tsv (one row per claim per ref) and
<label>-places.tsv (one row per claim per ref per place). Prints a summary.
"""
import argparse
import collections
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, HERE)
import i10lib as L  # noqa: E402

BUCKETS = {"spikes", "audits", "msc", "ref", "doc", "items", "questions", "reviews"}


def candidates(path, stem_count):
    """Strings whose presence in a pointing text counts as naming this place."""
    p = path[:-len(os.path.splitext(path)[1])]
    out = {path, p}
    d = os.path.dirname(path)
    depth = d.count("/") + 1 if d else 0
    if path.startswith("~/"):
        if depth >= 4:            # ~/src/repo/dir at least
            out.add(d)
    elif depth >= 2 and len(os.path.basename(d)) >= 8 and os.path.basename(d) not in BUCKETS:
        out.add(d)
    m = re.match(r"audits/(?:AUDIT-WORKING-|audit-findings-|audit-[0-9]*-?)?.*?(\d{6})", path)
    if m:
        out.add(m.group(1))  # the drains name audits by their six-digit id
    stem = os.path.basename(p)
    if stem_count[stem] == 1 and len(stem) >= 10 and "-" in stem:
        out.add(stem)
    return out


def named_in(cands, text):
    for c in cands:
        i = text.find(c)
        while i != -1:
            j = i + len(c)
            if j >= len(text) or not re.match(r"[A-Za-z0-9_-]", text[j]):
                return True
            i = text.find(c, i + 1)
    return False


def cost(text, offs):
    """(block_words, section_words): the lower and upper reading unit for these mentions."""
    blk = sum(L.words(text[x:y]) for x, y in L.blocks(text, offs)) + L.preamble(text)
    sec = sum(L.words(text[x:y]) for x, y in L.leaf_sections(text, offs))
    return min(blk, max(sec, 1)) if sec else blk, sec


def measure_ref(repo, ref, slugs, influx, sample_of):
    snap = L.load_snapshot(repo, ref)
    files = dict(snap)
    files.update(influx)
    stem_count = collections.Counter(os.path.splitext(os.path.basename(p))[0] for p in files)
    seg_path = {}
    for p in snap:
        m = L.SEG_RE.match(p)
        if m:
            seg_path[m.group(2)] = p
    drain_text = L.norm("\n".join(t for p, t in snap.items() if p.startswith(L.DRAIN_DIR)))
    hits = L.find_mentions(files, slugs)
    claims, places = [], []
    for s in slugs:
        sp = seg_path.get(s)
        if sp is None:
            continue
        body, wn = L.split_segment(snap[sp])
        home_text = L.norm(snap[sp])
        led = {p: L.norm(snap[p]) for p in hits[s] if L.classify(p) == "ledger"}
        keyed = {p for p, t in led.items()
                 if re.search(r"^concerns:.*segment:" + re.escape(s) + r"(?![A-Za-z0-9_-])", t, re.M)}
        # what the ledger says about this claim: keyed records whole, others where they mention it
        led_text = "\n".join(t if p in keyed else
                              "\n".join(snap[p][x:y] for x, y in L.leaf_sections(snap[p], hits[s][p]))
                              for p, t in led.items())
        led_text = L.norm(led_text)
        row = collections.OrderedDict(ref=ref, slug=s, sample=sample_of.get(s, ""),
                                      body_words=L.words(body), own_wn_words=L.words(wn),
                                      ledger_n=len(led), ledger_keyed=len(keyed))
        lb = ls = 0
        for p in led:
            b, c = cost(snap[p], hits[s][p])
            # a record keyed to the claim is about it: read whole; otherwise read where it mentions it
            w = L.words(snap[p]) if p in keyed else None
            lb += w if w is not None else b
            ls += w if w is not None else c
        row["ledger_block_words"], row["ledger_section_words"] = lb, ls
        cat_n, acct = collections.Counter(), collections.Counter()
        cat_b, cat_s = collections.Counter(), collections.Counter()
        must_b = must_s = raw_b = raw_s = 0
        for p, offs in sorted(hits[s].items()):
            text = files[p]
            cat = L.classify(p)
            if p == sp or cat == "ledger":
                continue
            if cat == "segment":
                _, hwn = L.split_segment(text)
                wn_start = text.find(hwn) if hwn else -1
                in_wn = [o - wn_start for o in offs if wn_start != -1 and wn_start <= o < wn_start + len(hwn)]
                in_body = [o for o in offs if not (wn_start != -1 and wn_start <= o < wn_start + len(hwn))]
                host = L.SEG_RE.match(p).group(2)
                if in_body:
                    b, c = cost(text, in_body)
                    cat_n["other-body"] += 1
                    cat_b["other-body"] += b
                    cat_s["other-body"] += c
                if not in_wn:
                    continue
                cat, text, offs = "other-wn", hwn, in_wn
                hrx = re.compile(r"(?<![A-Za-z0-9_-])" + re.escape(host) + r"(?![A-Za-z0-9_-])")
                is_l = bool(hrx.search(led_text)) and re.search(r"working note", led_text, re.I) is not None
                is_d = bool(hrx.search(drain_text))
                is_h = False
            else:
                cands = candidates(p, stem_count)
                is_l = named_in(cands, led_text)
                # a drain account cannot account for itself: reading it is the cost of that route
                is_d = bool(drain_text) and not p.startswith(L.DRAIN_DIR) and named_in(cands, drain_text)
                is_h = named_in(cands, home_text)
            b, c = cost(text, offs)
            cat_n[cat] += 1
            cat_b[cat] += b
            cat_s[cat] += c
            state = "-"
            if cat in L.NOISE:
                state = "L" if is_l else "D" if is_d else "H" if is_h else "U"
                acct[state] += 1
                acct[cat + ":" + state] += 1
                raw_b += b
                raw_s += c
                if state in ("H", "U"):
                    must_b += b
                    must_s += c
            places.append((ref, s, cat, p, len(offs), b, c, L.words(text), state))
        wnw = L.words(wn)
        row["noise_places"] = sum(n for c, n in cat_n.items() if c in L.NOISE)
        for k in "LDHU":
            row["acct_" + k] = acct[k]
        row["signal_block"] = row["body_words"] + lb
        row["signal_section"] = row["body_words"] + ls
        row["raw_block"], row["raw_section"] = wnw + raw_b, wnw + raw_s
        row["must_block"], row["must_section"] = wnw + must_b, wnw + must_s
        for c in sorted(set(cat_n) | L.NOISE | {"other-body", "front", "history", "archived", "influx-archived", "vocab"}):
            row["n:" + c] = cat_n[c]
            row["b:" + c] = cat_b[c]
            row["s:" + c] = cat_s[c]
            if c in L.NOISE:
                for k in "LDHU":
                    row[f"{c}:{k}"] = acct[f"{c}:{k}"]
        claims.append(row)
    return claims, places


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("refs", nargs="+")
    ap.add_argument("--repo", default=subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=HERE,
                                                     capture_output=True, text=True).stdout.strip())
    ap.add_argument("--sample", default=os.path.join(HERE, "sample.tsv"))
    ap.add_argument("--all", action="store_true", help="census: every segment slug present at every ref")
    ap.add_argument("--roots", default=os.path.join(HERE, "influx-roots.txt"))
    ap.add_argument("--no-influx", action="store_true")
    ap.add_argument("--out-dir", default=os.path.join(HERE, "data"))
    ap.add_argument("--label", default="run")
    a = ap.parse_args()

    sample_of = {}
    if a.all:
        sets = []
        for r in a.refs:
            names = L.git(["ls-tree", "-r", "--name-only", r], a.repo).decode().split("\n")
            sets.append({L.SEG_RE.match(n).group(2) for n in names if L.SEG_RE.match(n)
                         and not os.path.basename(n).startswith("old-")})
        slugs = sorted(set.intersection(*sets))
    else:
        for line in open(a.sample):
            if line.startswith("#") or line.startswith("slug\t") or not line.strip():
                continue
            f = line.rstrip("\n").split("\t")
            sample_of[f[0]] = f[1]
        slugs = sorted(sample_of)
    influx = {} if a.no_influx else L.load_influx(a.roots)
    print(f"influx: {len(influx)} files read from disk", file=sys.stderr)

    os.makedirs(a.out_dir, exist_ok=True)
    all_claims, all_places = [], []
    for r in a.refs:
        sha = L.git(["rev-parse", "--short", r + "^{commit}"], a.repo).decode().strip()
        c, p = measure_ref(a.repo, r, slugs, influx, sample_of)
        for row in c:
            row["sha"] = sha
        all_claims += c
        all_places += p
    cols = []
    for row in all_claims:
        for k in row:
            if k not in cols:
                cols.append(k)
    with open(os.path.join(a.out_dir, f"{a.label}-claims.tsv"), "w") as fh:
        fh.write("\t".join(cols) + "\n")
        for row in all_claims:
            fh.write("\t".join(str(row.get(k, 0)) for k in cols) + "\n")
    with open(os.path.join(a.out_dir, f"{a.label}-places.tsv"), "w") as fh:
        fh.write("ref\tslug\tclass\tpath\tmentions\tblock_words\tsection_words\tfile_words\taccounted\n")
        for t in all_places:
            fh.write("\t".join(map(str, t)) + "\n")

    # summary
    groups = sorted({row["sample"] for row in all_claims})
    for g in groups:
        print(f"\n== sample stratum: {g or 'census'} ==")
        for r in a.refs:
            rows = [x for x in all_claims if x["ref"] == r and x["sample"] == g]
            if not rows:
                continue
            n = len(rows)
            med = lambda k: sorted(x[k] for x in rows)[n // 2]  # noqa: E731
            tot = lambda k: sum(x[k] for x in rows)  # noqa: E731
            print(f"{r} ({rows[0]['sha']}): claims={n} noise_places={tot('noise_places')} "
                  f"(median {med('noise_places')}) acct L/D/H/U={tot('acct_L')}/{tot('acct_D')}/"
                  f"{tot('acct_H')}/{tot('acct_U')}")
            for u in ("block", "section"):
                sig, must, raw = tot("signal_" + u), tot("must_" + u), tot("raw_" + u)
                print(f"    [{u}] signal={sig} raw_noise={raw} must_read_noise={must} "
                      f"(median {med('must_' + u)}) signal_share={sig / max(1, sig + must):.3f} "
                      f"raw_share={sig / max(1, sig + raw):.3f}")


if __name__ == "__main__":
    main()
