#!/usr/bin/env python3
"""
Assemble a composite markdown document from an outline file.

Reads an outline file whose tables reference segment files, and assembles a
single document with:

  - Section structure (headers, scope text, separators) preserved
  - Segment content inlined with adjusted header levels
  - Academic numbering (shared counter per section: Definition I.3, Result II.7)
  - Cross-references rewritten: #slug-name → [Type S.N](#slug-name)
  - HTML anchors for working cross-references
  - Placeholders for gaps (undeveloped theory) and missing segments

Segment resolution: links in outline tables (e.g., [#slug](src/slug.md)) are
resolved relative to the outline file's directory. If the path as written
doesn't exist, the tool also tries src/{slug}.md relative to the outline.
This means outline tables can use bare slug.md or src/slug.md and both work.

Output goes to stdout by default (pipe-friendly). Use -o for file output.

Usage:
    bin/build 01-aad-core/OUTLINE.md                     # → stdout
    bin/build 01-aad-core/OUTLINE.md -o theory.md        # → file
    bin/build 01-aad-core/OUTLINE.md --strip-working-notes
    bin/build my-scratch/alt.md -o ~/Documents/out.md    # any outline, any output
"""

import argparse
import re
import sys
from pathlib import Path


# ── Text transforms ──────────────────────────────────────────────────────

def strip_frontmatter(text):
    """Remove YAML frontmatter (--- delimited block at start of file)."""
    lines = text.split('\n')
    if not lines or lines[0].strip() != '---':
        return text
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            return '\n'.join(lines[i + 1:]).lstrip('\n')
    return text


def bump_headers(text, offset):
    """Increase all markdown header levels by offset (capped at H6)."""
    def _bump(m):
        new_level = min(len(m.group(1)) + offset, 6)
        return '#' * new_level + m.group(2)
    return re.sub(r'^(#{1,6})([ \t])', _bump, text, flags=re.MULTILINE)


def strip_working_notes(text):
    """Remove the '## Working Notes' section (always the last section)."""
    matches = list(re.finditer(r'^## Working Notes\b', text, re.MULTILINE))
    if not matches:
        return text
    return text[:matches[-1].start()].rstrip('\n') + '\n'


def insert_label(text, label):
    """Insert a numbering label into the first heading of segment text."""
    def _insert(m):
        hashes, content = m.group(1), m.group(2).strip()
        cm = re.match(r'([^:]+?):\s+(.*)', content)
        if cm:
            return f'{hashes}{cm.group(1)} {label}: *{cm.group(2)}*'
        return f'{hashes}{label}. *{content}*'
    return re.sub(r'^(#{1,6}\s+)(.*)', _insert, text, count=1, flags=re.MULTILINE)


def rewrite_links(text, known_slugs):
    """Convert file-path links to internal anchor links."""
    # Any path ending in /slug.md or just slug.md → #slug (if known)
    def _rewrite(m):
        link_label, path = m.group(1), m.group(2)
        # Extract slug from path like "src/slug.md" or "slug.md"
        slug_m = re.match(r'(?:.*/)?([\w-]+)\.md$', path)
        if slug_m and slug_m.group(1) in known_slugs:
            return f'[{link_label}](#{slug_m.group(1)})'
        return m.group(0)
    return re.sub(r'\[([^\]]+)\]\(([^)]*?[\w-]+\.md)\)', _rewrite, text)


# ── Table parsing ────────────────────────────────────────────────────────

def parse_table_row(line):
    """Parse '| a | b | c |' into ['a', 'b', 'c']. Returns None if not a table row."""
    stripped = line.strip()
    if not stripped.startswith('|') or not stripped.endswith('|'):
        return None
    cells = stripped.split('|')
    return [c.strip() for c in cells[1:-1]]


def is_separator_row(cells):
    """True if this is a table header/body separator row."""
    return all(re.match(r'^[-:]+$', c) for c in cells if c)


def extract_slug_and_path(cell):
    """Extract slug and relative path from a table cell link.

    Handles:
      [#slug](src/slug.md)   → ('slug', 'src/slug.md')
      [#slug](slug.md)       → ('slug', 'slug.md')
    Returns (slug, rel_path) or (None, None).
    """
    m = re.search(r'\[#([\w-]+)\]\(([^)]+\.md)\)', cell)
    if m:
        return m.group(1), m.group(2)
    return None, None


# ── Numbering ────────────────────────────────────────────────────────────

def assign_numbers(lines):
    """Walk index tables and assign sequential labels to each segment.

    Returns dict mapping slug → (label, type_str).
    """
    numbering = {}
    current_section = None
    counter = 0
    in_table = False

    for line in lines:
        cells = parse_table_row(line)

        if cells and not in_table:
            in_table = True
            continue

        if in_table:
            if not cells:
                in_table = False
                continue
            if is_separator_row(cells):
                continue
            if any('--GAP--' in c for c in cells):
                continue

            section   = cells[0].strip() if len(cells) > 0 else ''
            type_str  = cells[1].strip() if len(cells) > 1 else ''
            n_override = cells[2].strip() if len(cells) > 2 else ''

            slug = None
            for c in cells:
                s, _ = extract_slug_and_path(c)
                if s:
                    slug = s
                    break

            if not slug:
                continue

            if section and section != current_section:
                current_section = section
                counter = 0

            if n_override:
                m = re.match(r'^([A-Za-z]+)\.(\d+)$', n_override)
                if m:
                    current_section = m.group(1)
                    counter = int(m.group(2))
                elif re.match(r'^\d+$', n_override):
                    counter = int(n_override)
                else:
                    counter += 1
            else:
                counter += 1

            numbering[slug] = (f'{current_section}.{counter}', type_str)

    return numbering


# ── Tag rewriting ────────────────────────────────────────────────────────

def _ref_display(label, type_str):
    if not type_str:
        return label
    primary = type_str.split('+')[0].strip()
    return f'{primary} {label}'


def _rewrite_tags_in_line(line, numbering):
    """Replace standalone #slug references in a single line."""
    out = []
    i = 0
    n = len(line)

    while i < n:
        ch = line[i]

        if ch == '`':
            ticks = 0
            while i + ticks < n and line[i + ticks] == '`':
                ticks += 1
            closer = '`' * ticks
            end = line.find(closer, i + ticks)
            if end != -1:
                out.append(line[i:end + ticks])
                i = end + ticks
            else:
                out.append(line[i:])
                i = n
            continue

        if ch == '$':
            if i + 1 < n and line[i + 1] == '$':
                end = line.find('$$', i + 2)
                if end != -1:
                    out.append(line[i:end + 2])
                    i = end + 2
                else:
                    out.append(line[i:])
                    i = n
            else:
                end = line.find('$', i + 1)
                if end != -1:
                    out.append(line[i:end + 1])
                    i = end + 1
                else:
                    out.append(ch)
                    i += 1
            continue

        if ch == '[':
            depth = 1
            j = i + 1
            while j < n and depth > 0:
                if line[j] == '\\':
                    j += 2
                    continue
                if line[j] == '[':
                    depth += 1
                elif line[j] == ']':
                    depth -= 1
                j += 1
            if j < n and line[j] == '(':
                k = line.find(')', j + 1)
                if k != -1:
                    out.append(line[i:k + 1])
                    i = k + 1
                    continue
            out.append(line[i:j])
            i = j
            continue

        if ch == '<' and i + 1 < n and (line[i + 1].isalpha() or line[i + 1] == '/'):
            end = line.find('>', i + 1)
            if end != -1:
                out.append(line[i:end + 1])
                i = end + 1
                continue

        if ch == '#' and (i == 0 or line[i - 1] in ' \t'):
            m = re.match(r'([a-z][a-z0-9-]*[a-z0-9])', line[i + 1:])
            if m and m.group(1) in numbering:
                slug = m.group(1)
                label, type_str = numbering[slug]
                display = _ref_display(label, type_str)
                out.append(f'[{display}](#{slug})')
                i += 1 + m.end()
                continue

        out.append(ch)
        i += 1

    return ''.join(out)


def rewrite_tags(text, numbering):
    """Rewrite all #slug cross-references to academic-style numbered links."""
    if not numbering:
        return text

    def _rewrite_link_display(m):
        slug, target = m.group(1), m.group(2)
        if slug == target and slug in numbering:
            label, type_str = numbering[slug]
            display = _ref_display(label, type_str)
            return f'[{display}](#{slug})'
        return m.group(0)

    text = re.sub(r'\[#([\w-]+)\]\(#([\w-]+)\)', _rewrite_link_display, text)

    lines = text.split('\n')
    result = []
    in_fenced = False
    in_display_math = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('```'):
            in_fenced = not in_fenced
            result.append(line)
            continue
        if in_fenced:
            result.append(line)
            continue
        if stripped == '$$':
            in_display_math = not in_display_math
            result.append(line)
            continue
        if in_display_math:
            result.append(line)
            continue
        result.append(_rewrite_tags_in_line(line, numbering))

    text = '\n'.join(result)
    text = re.sub(r'\( \[', '([', text)
    return text


# ── Table of contents ─────────────────────────────────────────────────────

def build_toc(toc_entries):
    if not toc_entries:
        return ''
    lines = ['## Table of Contents', '']
    for entry in toc_entries:
        kind = entry[0]
        if kind == 'section':
            _, heading, anchor = entry
            if lines[-1] != '':
                lines.append('')
            lines.append(f'**[{heading}](#{anchor})**')
            lines.append('')
        elif kind == 'segment':
            _, label, type_str, slug, title = entry
            primary = type_str.split('+')[0].strip() if type_str else ''
            if primary:
                lines.append(f'- [{primary} {label}: {title}](#{slug})')
            else:
                lines.append(f'- [{label}. {title}](#{slug})')
        elif kind == 'missing':
            _, label, type_str, slug, title = entry
            primary = type_str.split('+')[0].strip() if type_str else ''
            if primary:
                lines.append(f'- *{primary} {label}: {title}* (not yet written)')
            else:
                lines.append(f'- *{label}. {title}* (not yet written)')
        elif kind == 'gap':
            _, desc = entry
            lines.append(f'- *\\[Gap\\] {desc}*')
    lines.append('')
    return '\n'.join(lines)


def make_heading_anchor(heading_text):
    anchor = heading_text.lower().strip()
    anchor = re.sub(r'[^\w\s-]', '', anchor)
    anchor = re.sub(r'[\s]+', '-', anchor)
    return anchor


# ── Segment resolution ───────────────────────────────────────────────────

def resolve_segment(outline_dir, rel_path, slug):
    """Find a segment file, trying multiple resolution strategies.

    1. rel_path as written, relative to outline_dir
    2. src/{slug}.md relative to outline_dir (fallback)

    Returns the resolved Path or None.
    """
    # Try the path as written in the outline
    candidate = outline_dir / rel_path
    if candidate.exists():
        return candidate

    # Fallback: src/{slug}.md relative to outline
    candidate = outline_dir / 'src' / f'{slug}.md'
    if candidate.exists():
        return candidate

    return None


# ── Core builder ─────────────────────────────────────────────────────────

def collect_slugs(lines):
    slugs = set()
    for line in lines:
        cells = parse_table_row(line)
        if cells:
            for cell in cells:
                s, _ = extract_slug_and_path(cell)
                if s:
                    slugs.add(s)
    return slugs


def build(index_path, strip_notes=False):
    """Build the composite document.

    Resolves all paths relative to the outline file's directory.
    Returns (output_text, stats_dict, numbering_map).
    """
    outline_dir = index_path.parent
    index_text = index_path.read_text(encoding='utf-8')
    lines = index_text.split('\n')

    known_slugs = collect_slugs(lines)
    numbering = assign_numbers(lines)

    out = []
    toc_entries = []
    in_table = False
    table_entries = []   # list of (kind, slug, rel_path, claim_text)
    section_level = 2

    stats = {'included': 0, 'missing': 0, 'gaps': 0}

    def flush_table():
        nonlocal table_entries
        for entry in table_entries:
            kind = entry[0]

            if kind == 'gap':
                _, _, _, claim_text = entry
                out.append('')
                out.append(f'> **\\[GAP\\]** {claim_text}')
                out.append('')
                stats['gaps'] += 1
                toc_entries.append(('gap', claim_text))

            elif kind == 'segment':
                _, slug, rel_path, claim_text = entry
                seg_path = resolve_segment(outline_dir, rel_path, slug) if rel_path else None
                label_info = numbering.get(slug)
                label = label_info[0] if label_info else None
                type_str = label_info[1] if label_info else ''
                title = claim_text if claim_text else slug

                out.append('')
                out.append(f'<a id="{slug}"></a>')
                out.append('')

                if seg_path and seg_path.exists():
                    seg_text = seg_path.read_text(encoding='utf-8')
                    seg_text = strip_frontmatter(seg_text)
                    if strip_notes:
                        seg_text = strip_working_notes(seg_text)
                    seg_text = bump_headers(seg_text, section_level)
                    if label:
                        seg_text = insert_label(seg_text, label)
                    seg_text = rewrite_links(seg_text, known_slugs)
                    out.append(seg_text.rstrip())
                    out.append('')
                    stats['included'] += 1
                    if label:
                        toc_entries.append(('segment', label, type_str, slug, title))
                else:
                    level = section_level + 1
                    if label and type_str:
                        out.append(f'{"#" * level} {type_str} {label}: *{title}*')
                    elif label:
                        out.append(f'{"#" * level} {label}. *{title}*')
                    else:
                        out.append(f'{"#" * level} {title}')
                    out.append('')
                    out.append(f'*Segment `{slug}` has not yet been written.*')
                    out.append('')
                    stats['missing'] += 1
                    if label:
                        toc_entries.append(('missing', label, type_str, slug, title))

        table_entries = []

    i = 0
    while i < len(lines):
        line = lines[i]
        cells = parse_table_row(line)

        if cells and not in_table:
            in_table = True
            table_entries = []
            i += 1
            continue

        if in_table:
            if cells:
                if is_separator_row(cells):
                    i += 1
                    continue

                is_gap = any('--GAP--' in c for c in cells)
                if is_gap:
                    desc_candidates = [
                        c for c in cells
                        if c and '--GAP--' not in c
                        and not re.match(r'^[IVSA]+$', c.strip())
                    ]
                    gap_desc = desc_candidates[-1] if desc_candidates else 'Open question'
                    table_entries.append(('gap', None, None, gap_desc))
                else:
                    slug, rel_path = None, None
                    for c in cells:
                        s, p = extract_slug_and_path(c)
                        if s:
                            slug, rel_path = s, p
                            break
                    claim_text = cells[4].strip() if len(cells) > 4 else ''
                    if slug:
                        table_entries.append(('segment', slug, rel_path, claim_text))

                i += 1
                continue
            else:
                in_table = False
                flush_table()

        hm = re.match(r'^(#{1,6})\s', line)
        if hm:
            section_level = len(hm.group(1))
            heading_text = line[hm.end():].strip()
            if len(hm.group(1)) == 2 and heading_text:
                anchor = make_heading_anchor(heading_text)
                toc_entries.append(('section', heading_text, anchor))

        out.append(rewrite_links(line, known_slugs))
        i += 1

    if in_table:
        flush_table()

    toc_text = build_toc(toc_entries)
    if toc_text:
        insert_idx = None
        for idx, ln in enumerate(out):
            if ln.strip() == '---':
                insert_idx = idx
                break
        if insert_idx is not None:
            out[insert_idx:insert_idx] = ['', toc_text, '']

    assembled = '\n'.join(out)
    assembled = rewrite_tags(assembled, numbering)

    return assembled, stats, numbering


# ── CLI ──────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='Assemble an outline file into a composite markdown document.'
    )
    parser.add_argument(
        'outline',
        type=Path,
        help='Path to the outline file (e.g., 01-aad-core/OUTLINE.md)'
    )
    parser.add_argument(
        '-o', '--output',
        type=Path,
        default=None,
        help='Output file path (default: stdout)'
    )
    parser.add_argument(
        '--strip-working-notes',
        action='store_true',
        help='Remove ## Working Notes sections from included segments'
    )

    args = parser.parse_args()

    index_path = args.outline.resolve()
    if not index_path.exists():
        print(f'Error: {index_path} not found', file=sys.stderr)
        return 1

    text, stats, numbering = build(index_path, strip_notes=args.strip_working_notes)

    if args.output:
        output_path = args.output.resolve()
        output_path.write_text(text, encoding='utf-8')
        dest = output_path.name
    else:
        sys.stdout.write(text)
        dest = 'stdout'

    total = stats['included'] + stats['missing'] + stats['gaps']
    print(f'Built → {dest}:', file=sys.stderr)
    print(f'  {stats["included"]} segments included', file=sys.stderr)
    print(f'  {stats["missing"]} segments missing (placeholder)', file=sys.stderr)
    print(f'  {stats["gaps"]} gaps (theory not developed)', file=sys.stderr)
    print(f'  {total} total entries', file=sys.stderr)
    print(f'  {len(numbering)} slugs numbered', file=sys.stderr)

    return 0


if __name__ == '__main__':
    sys.exit(main())
