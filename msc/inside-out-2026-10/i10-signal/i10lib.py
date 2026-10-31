"""Shared machinery for the I.10 signal-against-noise measure.

Reads an asf snapshot straight from git (any ref), and the influx outside asf
from disk. Nothing is written anywhere except by the calling scripts.
See METHOD.md beside this file for what every rule means and why.
"""
import os
import re
import subprocess

HOME = os.path.expanduser("~")
TEXT_EXT = (".md", ".markdown", ".tex", ".udon")
SELF_DIR = "msc/inside-out-2026-10/i10-signal/"
EFFORT_DIR = "msc/inside-out-2026-10/"
DRAIN_DIR = "msc/inside-out-2026-10/drain/"
LEDGER_DIRS = ("items/", "questions/", "reviews/")
SEG_RE = re.compile(r"^(0[1-4]-[a-z]+-core)/src/([^/]+)\.md$")
ARCHIVED_PARTS = ("/.integrated/", "/.archived/", "/.archive/", "/.super-archive/")
FRONT_FILES = {"README.md", "README-auditor.md", "FINDINGS.md", "LEXICON.md", "OUTLINE.md"}
HISTORY_FILES = {"CHANGELOG.md", "LOG.md"}
TRACKER_FILES = {"TODO.md", "PRACTICA.md", "JOSEPH-TODO.md", "PROPOSALS.md", "ROUTING.md"}
INDEX_RE = re.compile(r"^(?:spikes/|audits/)?(?:INDEX|ROUTING|STATUS|PROPOSED[A-Z-]*|PROPOSALS|PRACTICA|[A-Z-]*TODO[A-Z-]*)\.md$")


def is_index(path):
    """Status-bearing index and tracker files at the root, spikes/ and audits/ (both snapshots)."""
    return bool(INDEX_RE.match(path))


# Noise classes: live places outside the claim's own home. Everything else is reported, not summed.
NOISE = {"own-wn", "other-wn", "spikes", "audits", "msc-effort", "msc", "trackers",
         "root-docs", "doc", "ref", "component-other", "influx"}

# ---------------------------------------------------------------- snapshot


def git(args, cwd, inp=None):
    return subprocess.run(["git", *args], cwd=cwd, input=inp, capture_output=True, check=True).stdout


def load_snapshot(repo, ref):
    """{path: text} for every tracked text file at ref (excluding .vsect/ and this measure's own dir)."""
    names = git(["ls-tree", "-r", "-z", "--name-only", ref], repo).decode().split("\0")
    names = [n for n in names if n and n.endswith(TEXT_EXT)
             and not n.startswith((".vsect/", ".claude/", SELF_DIR))]
    req = "".join(f"{ref}:{n}\n" for n in names).encode()
    out = git(["cat-file", "--batch"], repo, inp=req)
    files, i = {}, 0
    for n in names:
        nl = out.index(b"\n", i)
        size = int(out[i:nl].split()[2])
        files[n] = out[nl + 1:nl + 1 + size].decode("utf-8", "replace")
        i = nl + 1 + size + 1
    return files


def load_influx(roots_file, max_bytes=2_000_000):
    """{'~/src/...': text} for text files under the listed roots, read from disk now."""
    roots, skip_dirs, skip_paths = [], set(), []
    for line in open(roots_file):
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        if line.startswith("skip-dir "):
            skip_dirs.add(line[9:].strip())
        elif line.startswith("skip-path "):
            skip_paths.append(os.path.expanduser(line[10:].strip()))
        else:
            roots.append(os.path.expanduser(line))
    files = {}
    for root in roots:
        for d, dirs, fns in os.walk(root):
            dirs[:] = [x for x in dirs if x not in skip_dirs
                       and not any(os.path.join(d, x).startswith(p) for p in skip_paths)]
            for fn in fns:
                if not fn.endswith(TEXT_EXT):
                    continue
                p = os.path.join(d, fn)
                try:
                    if os.path.getsize(p) > max_bytes or os.path.islink(p):
                        continue
                    with open(p, encoding="utf-8", errors="replace") as fh:
                        files["~" + p[len(HOME):]] = fh.read()
                except OSError:
                    continue
    return files

# ---------------------------------------------------------------- text structure


def norm(text):
    return text.replace(HOME + "/", "~/")


def words(text):
    return len(text.split())


HEAD_RE = re.compile(r"^(#{1,6})\s")


def headings(text):
    """[(offset, level)] of ATX headings outside code fences."""
    out, off, fence = [], 0, False
    for line in text.splitlines(keepends=True):
        s = line.lstrip()
        if s.startswith("```") or s.startswith("~~~"):
            fence = not fence
        elif not fence:
            m = HEAD_RE.match(line)
            if m:
                out.append((off, len(m.group(1))))
        off += len(line)
    return out


def leaf_sections(text, positions):
    """Union of leaf sections (heading to next heading of any level) containing the positions."""
    hs = [h[0] for h in headings(text)]
    spans = set()
    for p in positions:
        start = max([h for h in hs if h <= p], default=0)
        end = min([h for h in hs if h > p], default=len(text))
        spans.add((start, end))
    return sorted(spans)


MARK_RE = re.compile(r"\s*([-*+]|\d+[.)])\s")


def _kind(line):
    s = line.strip()
    if not s:
        return "blank"
    if HEAD_RE.match(line):
        return "head"
    if s.startswith("|"):
        return "row"
    if MARK_RE.match(line):
        return "mark"
    return "text"


def blocks(text, positions):
    """Union of the smallest readable blocks holding the positions: a paragraph, a list item
    (its marker line to the next marker), or a table row; a mention in a heading takes the
    heading plus the block under it."""
    lines = text.splitlines(keepends=True)
    starts, off = [], 0
    for ln in lines:
        starts.append(off)
        off += len(ln)
    kinds = [_kind(ln) for ln in lines]
    spans = set()
    import bisect
    for p in positions:
        i = max(0, bisect.bisect_right(starts, p) - 1)
        if not lines:
            continue
        if kinds[i] == "row":
            spans.add((starts[i], starts[i] + len(lines[i])))
            continue
        j = i
        if kinds[i] == "head":
            k = i + 1
            while k < len(lines) and kinds[k] == "blank":
                k += 1
            i = j = k if k < len(lines) else i
        while j > 0 and kinds[j] != "mark" and kinds[j - 1] == "text":
            j -= 1
        if j > 0 and kinds[j] == "text" and kinds[j - 1] == "mark":
            j -= 1
        k = i
        while k + 1 < len(lines) and kinds[k + 1] == "text":
            k += 1
        start = starts[min(j, len(starts) - 1)]
        spans.add((start, starts[k] + len(lines[k])))
    return sorted(spans)


def preamble(text, cap=150):
    """What a reader takes in to know what a file is: its first heading and the first block after it."""
    lines = text.splitlines()
    out, seen_text = [], False
    for ln in lines:
        k = _kind(ln)
        if k == "blank" and seen_text:
            break
        if k in ("text", "mark", "row"):
            seen_text = True
        out.append(ln)
    return min(cap, words("\n".join(out)))


def split_segment(text):
    """(body, working_notes) of a segment file: WN is '## Working Notes' to the next level-2 heading."""
    m = re.search(r"^## Working Notes[^\n]*$", text, re.M)
    if not m:
        return text, ""
    nxt = re.search(r"^## (?!#)", text[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(text)
    return text[:m.start()] + text[end:], text[m.start():end]

# ---------------------------------------------------------------- classification


def classify(path):
    if path.startswith("~/"):
        return "influx-archived" if any(a in path for a in ARCHIVED_PARTS) else "influx"
    if any(a in "/" + path for a in ARCHIVED_PARTS) or path.startswith(".archive/"):
        return "archived"
    if SEG_RE.match(path):
        return "segment"
    if path.startswith(LEDGER_DIRS):
        return "ledger"
    base = os.path.basename(path)
    if path.startswith("spikes/"):
        return "spikes"
    if path.startswith("audits/"):
        return "audits"
    if path.startswith(EFFORT_DIR):
        return "msc-effort"
    if path.startswith("msc/"):
        return "msc"
    if path.startswith("terminology/"):
        return "vocab"
    if "/" not in path:
        if base in HISTORY_FILES:
            return "history"
        if base in TRACKER_FILES:
            return "trackers"
        if base in FRONT_FILES or base.startswith("CURRENT-VOL"):
            return "front"
        return "root-docs"
    if re.match(r"^0[1-4]-[a-z]+-core/", path):
        if base in FRONT_FILES or base in ("INTRODUCTION.md", "OUTLINE-accepted.md"):
            return "front"
        return "component-other"
    if path.startswith("doc/readme/src/"):
        return "front"  # README partials, generated or assembled into README.md
    if path.startswith("doc/"):
        return "doc"
    if path.startswith("ref/"):
        return "ref"
    return "other"

# ---------------------------------------------------------------- mentions


def slug_regex(slugs):
    alt = "|".join(re.escape(s) for s in sorted(slugs, key=len, reverse=True))
    return re.compile(r"(?<![A-Za-z0-9_-])(" + alt + r")(?![A-Za-z0-9_-])")


def find_mentions(files, slugs):
    """{slug: {path: [offsets]}}."""
    rx = slug_regex(slugs)
    hits = {s: {} for s in slugs}
    for path, text in files.items():
        for m in rx.finditer(text):
            hits[m.group(1)].setdefault(path, []).append(m.start())
    return hits
