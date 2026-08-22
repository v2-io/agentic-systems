#!/usr/bin/env python3
"""Split math-core.md into per-chapter files using OUTLINE.md chapter structure.

Approach:
  - Walk 01-aat-core/OUTLINE.md, tracking the current Part / Chapter /
    Appendix-group. Slugs appearing in chapter tables (matched via
    `[#slug](src/slug.md)`) get tagged with their owning chapter; slugs under
    an `## *Appendices* …` heading get tagged as appendix slugs.
  - Walk math-core.md, identifying each `## ` segment and its slug.
  - For each Part chapter, emit a file containing exactly the math-core
    segments whose slug was tagged to that chapter, in math-core order.
  - Appendices: group the appendix segments that actually appear in
    math-core.md (in math-core order) into uniform groups of 5. This keeps
    chapter sizes uniform; appendix entries marked `missing` in OUTLINE
    and therefore absent from math-core don't leave half-empty chapters.

Outputs land in tmp-chapters/ with order-prefixed slugified filenames so an
`ls` reads in book order.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTLINE = ROOT / "01-aat-core/OUTLINE.md"
MATH_CORE = ROOT / "math-core.md"
OUT_DIR = ROOT / "tmp-chapters"

# Match `[#slug](src/slug.md)` and similar variants inside table rows.
SLUG_REF_RE = re.compile(r"\[#([a-z0-9][a-z0-9-]*)\]\(src/\1\.md\)")

# Pull the slug declared inside each math-core ## segment body.
MC_SLUG_RE = re.compile(r"^- \*\*Slug\*\*: `([a-z0-9][a-z0-9-]*)`", re.M)


def slugify(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "untitled"


def parse_outline():
    """Return (part_chapters, appendix_slug_set, appendix_part_of).

    part_chapters    — list of (chapter_label, [slugs_in_order]) for Part chapters,
                       in book order.
    appendix_slug_set — set of slugs declared under any `## *Appendices* …` heading.
    appendix_part_of  — dict slug → the appendix-part name (e.g. "Details").
    """
    text = OUTLINE.read_text()
    current_part = None
    current_chapter = None       # for Parts: chapter heading text
    appendix_part = None         # name of the appendix group ("Details" / "Operational Domains")
    chapter_slugs: list[str] = []
    appendix_slugs: list[tuple[str, str]] = []  # [(appendix_group, slug), ...]

    chapters: list[tuple[str, list[str]]] = []

    def flush_chapter():
        nonlocal chapter_slugs, current_chapter
        if current_chapter and chapter_slugs:
            chapters.append((current_chapter, chapter_slugs))
        chapter_slugs = []

    for raw in text.splitlines():
        line = raw.rstrip()

        m_part = re.match(r"^## \*Part\* (.+)$", line)
        if m_part:
            flush_chapter()
            current_part = m_part.group(1).strip()
            current_chapter = None
            appendix_part = None
            continue

        m_app = re.match(r"^## \*Appendices\* (.+)$", line)
        if m_app:
            flush_chapter()
            current_part = None
            current_chapter = None
            appendix_part = m_app.group(1).strip()
            continue

        m_chap = re.match(r"^### \*Chapter\* +(.+)$", line)
        if m_chap:
            flush_chapter()
            current_chapter = m_chap.group(1).strip()
            continue

        # Other ### headings (Introduction / Preface) — close any open chapter
        # but don't open a new one.
        if line.startswith("### "):
            flush_chapter()
            current_chapter = None
            continue

        # Slug references in table rows.
        for m in SLUG_REF_RE.finditer(line):
            slug = m.group(1)
            if current_chapter is not None:
                chapter_slugs.append(slug)
            elif appendix_part is not None:
                appendix_slugs.append((appendix_part, slug))
            # else: outside any chapter (preface, top-level intro) — drop.

    flush_chapter()

    appendix_slug_set = {slug for _part, slug in appendix_slugs}
    appendix_part_of = {slug: part for part, slug in appendix_slugs}
    return chapters, appendix_slug_set, appendix_part_of


def parse_math_core():
    """Return [(slug, heading_text, start_line, end_line)] over math-core.md.

    start_line and end_line are inclusive 1-based line numbers.
    """
    lines = MATH_CORE.read_text().splitlines()
    segments = []
    current = None  # dict in progress

    for i, line in enumerate(lines, 1):
        if line.startswith("## "):
            if current is not None:
                current["end"] = i - 1
                segments.append(current)
            current = {
                "heading": line[3:].strip(),
                "start": i,
                "end": None,
                "slug": None,
            }
            continue

    if current is not None:
        current["end"] = len(lines)
        segments.append(current)

    # Resolve each segment's slug by scanning its body.
    for seg in segments:
        body = "\n".join(lines[seg["start"] : seg["end"]])
        m = MC_SLUG_RE.search(body)
        if m:
            seg["slug"] = m.group(1)

    return lines, segments


def write_chapter(out_path: Path, title: str, segments: list[dict], lines: list[str]) -> None:
    body_parts = [f"# {title}\n"]
    for seg in segments:
        chunk = "\n".join(lines[seg["start"] - 1 : seg["end"]])
        body_parts.append(chunk.rstrip())
        body_parts.append("")
    out_path.write_text("\n\n".join(body_parts).rstrip() + "\n")


def main():
    part_chapters, appendix_slug_set, appendix_part_of = parse_outline()
    lines, segments = parse_math_core()

    OUT_DIR.mkdir(exist_ok=True)
    for f in OUT_DIR.iterdir():
        if f.is_file() and f.name != "_split.py":
            f.unlink()

    placed: set[str] = set()
    report_lines = []
    chapter_idx = 0

    # Part chapters: emit in OUTLINE order, content in math-core order.
    for chapter_name, slugs in part_chapters:
        slug_set = set(slugs)
        belongs = [s for s in segments if s["slug"] in slug_set]
        if not belongs:
            report_lines.append(f"[skip] {chapter_name}: no segments in math-core.md")
            continue
        for s in belongs:
            placed.add(s["slug"])
        chapter_idx += 1
        fname = f"{chapter_idx:02d}-{slugify(chapter_name)}.md"
        write_chapter(OUT_DIR / fname, chapter_name, belongs, lines)
        report_lines.append(f"[wrote] {fname}  ({len(belongs)} segments)")

    # Appendices: take the appendix segments present in math-core (in math-core
    # order), group them into uniform chunks of 5 (last chunk may be short).
    appendix_present = [s for s in segments if s["slug"] in appendix_slug_set]
    GROUP = 5
    for i in range(0, len(appendix_present), GROUP):
        group = appendix_present[i : i + GROUP]
        # If all entries in this group share an appendix-part name, surface it.
        parts_in_group = {appendix_part_of.get(s["slug"], "") for s in group}
        part_label = next(iter(parts_in_group)) if len(parts_in_group) == 1 else "Mixed"
        idx_within = i // GROUP + 1
        chapter_idx += 1
        label = f"Appendix — {part_label} (group {idx_within})"
        fname = f"{chapter_idx:02d}-appendix-{slugify(part_label)}-group-{idx_within}.md"
        write_chapter(OUT_DIR / fname, label, group, lines)
        for s in group:
            placed.add(s["slug"])
        report_lines.append(f"[wrote] {fname}  ({len(group)} segments)")

    # Any math-core segments not placed in any chapter or appendix group?
    orphans = [s for s in segments if s["slug"] and s["slug"] not in placed]
    truly_unslugged = [s for s in segments if not s["slug"]]
    report_lines.append("")
    report_lines.append(f"placed:    {len(placed)} segments")
    report_lines.append(f"orphans:   {len(orphans)} segments not matched to any chapter")
    report_lines.append(f"unslugged: {len(truly_unslugged)} segments with no slug field")
    for s in orphans:
        report_lines.append(f"  orphan: {s['slug']}  ({s['heading']})")
    for s in truly_unslugged:
        report_lines.append(f"  unslugged: {s['heading']}")

    print("\n".join(report_lines))


if __name__ == "__main__":
    main()
