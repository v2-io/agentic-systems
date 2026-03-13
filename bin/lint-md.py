#!/usr/bin/env python3
"""
Lint markdown files against ACT's FORMAT.md conventions.

Usage:
    bin/lint-md.py [--fix] [files...]

If no files given, lints all top-level *.md files.
With --fix, applies safe auto-fixes and re-reports remaining issues.

Exit code 0 = clean, 1 = violations found.
"""

import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Unicode Greek letters that, when used as math variables (not etymology),
# should be inside $...$. We look for these followed by subscript patterns
# or used standalone as variables.
GREEK_MATH = {
    'Σ': r'\Sigma', 'σ': r'\sigma', 'δ': r'\delta', 'ε': r'\varepsilon',
    'η': r'\eta', 'ρ': r'\rho', 'α': r'\alpha', 'β': r'\beta',
    'γ': r'\gamma', 'λ': r'\lambda', 'π': r'\pi', 'τ': r'\tau',
    'μ': r'\mu', 'φ': r'\phi', 'θ': r'\theta', 'ω': r'\omega',
    'Ω': r'\Omega', 'Π': r'\Pi',
}

# Ancient Greek words (etymology) — these should NOT be flagged
GREEK_WORDS = re.compile(
    r'[λόγοςζωήγένεσιςπρληψαἴσθτφέρᾶξ'
    r'ἀπορίαἐπιστφήυβωδκμνχθ]'
    r'[α-ωά-ώἀ-ᾼ]+'  # followed by more Greek chars = it's a word
)

# ASCII math variable patterns that should be in $...$
# Matches things like M_t, G_t, O_t, X_t, f_M, V_O, Q_O, N_h, etc.
ASCII_MATH_VAR = re.compile(
    r'(?<![`$\\a-zA-Z_])'  # not preceded by code/math/word chars
    r'([A-Z]_[a-z{}]|[a-z]_[A-Z])'  # e.g., M_t, f_M
    r'(?![`])'  # not followed by backtick
)


# ---------------------------------------------------------------------------
# State-tracking line scanner
# ---------------------------------------------------------------------------

class MathContext:
    """Track whether we're in code blocks, inline code, or math."""

    def __init__(self):
        self.in_code_block = False
        self.code_block_marker = ''

    def update_code_block(self, line):
        stripped = line.strip()
        if not self.in_code_block:
            if stripped.startswith('```'):
                self.in_code_block = True
                self.code_block_marker = '```'
                return True
        else:
            if stripped.startswith(self.code_block_marker) and stripped.strip('`') == '':
                # Closing ``` on its own or with just more backticks
                self.in_code_block = False
                return True
            if stripped == self.code_block_marker or stripped.startswith('```') and len(stripped.rstrip('`')) == 0:
                self.in_code_block = False
                return True
        return self.in_code_block


def find_math_spans(line):
    """Find all $...$ and $$...$$ spans in a line, returning (start, end, is_display)."""
    spans = []
    i = 0
    while i < len(line):
        # Skip backtick-quoted spans
        if line[i] == '`':
            end = line.find('`', i + 1)
            if end == -1:
                break
            i = end + 1
            continue
        if line[i] == '$':
            is_display = (i + 1 < len(line) and line[i + 1] == '$')
            if is_display:
                # Display math on single line: $$...$$
                end = line.find('$$', i + 2)
                if end != -1:
                    spans.append((i, end + 2, True))
                    i = end + 2
                    continue
                # Display math delimiter on its own (start or end)
                i += 2
                continue
            else:
                # Inline math: $...$
                end = line.find('$', i + 1)
                if end != -1:
                    spans.append((i, end + 1, False))
                    i = end + 1
                    continue
        i += 1
    return spans


def is_in_code_span(line, pos):
    """Check if position is inside a backtick code span."""
    in_code = False
    i = 0
    while i < len(line) and i < pos:
        if line[i] == '`':
            in_code = not in_code
        i += 1
    return in_code


def is_in_math(line, pos, spans):
    """Check if position is inside a math span."""
    for start, end, _ in spans:
        if start < pos < end:
            return True
    return False


def is_in_any_special(line, pos, spans):
    """Check if position is in code span or math span."""
    return is_in_code_span(line, pos) or is_in_math(line, pos, spans)


# ---------------------------------------------------------------------------
# Individual checks
# ---------------------------------------------------------------------------

def check_math_spacing(line, lineno, spans):
    """Rule: no space after opening $ or before closing $."""
    issues = []
    for start, end, is_display in spans:
        if is_display:
            continue
        content = line[start:end]
        # Space after opening $
        if len(content) > 2 and content[1] == ' ':
            issues.append((lineno, start + 1,
                           f'space after opening $: {content[:20]}...'))
        # Space before closing $
        if len(content) > 2 and content[-2] == ' ':
            issues.append((lineno, end - 2,
                           f'space before closing $: ...{content[-20:]}'))
    return issues


def check_pipe_in_math(line, lineno, spans):
    """Rule: use \\vert not | inside math; \\Vert not \\| inside math."""
    issues = []
    for start, end, _ in spans:
        content = line[start:end]
        # Check for bare | (not \vert, \lvert, \rvert, \mid)
        for m in re.finditer(r'(?<!\\)(?<!l)(?<!r)\|', content):
            # Make sure it's not \vert, \lvert, \rvert, \mid
            pos = m.start()
            preceding = content[max(0, pos - 6):pos]
            if not re.search(r'\\[lr]?vert$|\\mid$|\\lVert$|\\rVert$|\\Vert$', preceding):
                issues.append((lineno, start + pos,
                               f'bare | in math — use \\vert, \\lvert/\\rvert, or \\mid'))
        # Check for \| (should be \Vert or \lVert/\rVert)
        for m in re.finditer(r'\\\|', content):
            pos = m.start()
            preceding = content[max(0, pos - 2):pos]
            if preceding not in ('\\l', '\\r'):  # not \lVert or \rVert
                issues.append((lineno, start + pos,
                               f'\\| in math — use \\Vert, \\lVert/\\rVert'))
    return issues


def check_raw_angle_in_math(line, lineno, spans):
    """Rule: avoid raw < and > in math — use \\lt and \\gt."""
    issues = []
    for start, end, _ in spans:
        content = line[start:end]
        for m in re.finditer(r'(?<!\\)[<>]', content):
            ch = m.group()
            issues.append((lineno, start + m.start(),
                           f'raw {ch} in math — use \\{"lt" if ch == "<" else "gt"}'))
    return issues


def check_bare_asterisk_in_inline_math(line, lineno, spans):
    """Rule: use \\ast not bare * in inline $...$. Markdown italic parser eats bare *."""
    issues = []
    for start, end, is_display in spans:
        if is_display:
            continue  # display math on own lines is safe
        content = line[start:end]
        # Look for bare * not preceded by backslash (i.e., not \ast, \star, etc.)
        for m in re.finditer(r'(?<!\\)\*', content):
            issues.append((lineno, start + m.start(),
                           'bare * in inline math — use \\ast (markdown italic conflict)'))
    return issues


def check_begin_align(line, lineno):
    """Rule: use \\begin{{aligned}} not \\begin{{align}} inside $$."""
    issues = []
    for m in re.finditer(r'\\begin\{align\}', line):
        if not is_in_code_span(line, m.start()):
            issues.append((lineno, m.start(),
                           r'\begin{align} — use \begin{aligned} inside $$'))
    return issues


def check_obsidian_tag_spacing(line, lineno):
    """Rule: space before #slug for Obsidian — ( #foo) not (#foo)."""
    issues = []
    for m in re.finditer(r'\(#[a-z]', line):
        if not is_in_code_span(line, m.start()):
            issues.append((lineno, m.start(),
                           f'missing space before # for Obsidian: {line[m.start():m.start()+15]}'))
    return issues


def check_bare_unicode_greek(line, lineno, spans):
    """Flag Unicode Greek letters used as math variables outside $...$."""
    issues = []
    for ch, latex in GREEK_MATH.items():
        for m in re.finditer(re.escape(ch), line):
            pos = m.start()
            if is_in_any_special(line, pos, spans):
                continue
            # Check if this is part of a Greek word (etymology)
            # Look at surrounding chars for more Greek
            before = line[max(0, pos - 1):pos]
            after = line[pos + 1:pos + 3] if pos + 1 < len(line) else ''
            # If surrounded by other Greek-range chars, it's a word, skip
            greek_range = re.compile(r'[\u0370-\u03FF\u1F00-\u1FFF]')
            if (before and greek_range.search(before)) or (after and greek_range.search(after[0:1])):
                continue
            # It's a standalone Greek letter used as a variable
            # Get some context
            ctx = line[max(0, pos - 5):min(len(line), pos + 10)]
            issues.append((lineno, pos,
                           f'bare Greek math variable outside $: {ctx}'))
    return issues


def check_bare_ascii_math(line, lineno, spans):
    """Flag ASCII math variable patterns like M_t, G_t outside $...$."""
    issues = []
    for m in ASCII_MATH_VAR.finditer(line):
        pos = m.start()
        if is_in_any_special(line, pos, spans):
            continue
        # Also skip if inside a table's slug/link column or backtick
        ctx = line[max(0, pos - 2):pos]
        if ctx.endswith('`') or ctx.endswith('#'):
            continue
        snippet = m.group()
        issues.append((lineno, pos,
                       f'bare math variable outside $: {snippet}'))
    return issues


def check_display_math_blank_lines(lines):
    """Rule: display math $$ must have blank lines before and after."""
    issues = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == '$$':
            # Check line before
            if i > 0 and lines[i - 1].strip() != '':
                issues.append((i + 1, 0, '$$ should have a blank line before it'))
            # Check line after
            if i < len(lines) - 1 and lines[i + 1].strip() != '':
                issues.append((i + 1, 0, '$$ should have a blank line after it'))
    return issues


# ---------------------------------------------------------------------------
# Auto-fix functions
# ---------------------------------------------------------------------------

def fix_math_spacing(line):
    """Remove spaces after opening $ and before closing $ in inline math."""
    # This is trickier than it looks — need to find $...$ spans
    result = []
    i = 0
    while i < len(line):
        if line[i] == '`':
            # Skip code span
            end = line.find('`', i + 1)
            if end == -1:
                result.append(line[i:])
                break
            result.append(line[i:end + 1])
            i = end + 1
            continue
        if line[i] == '$':
            if i + 1 < len(line) and line[i + 1] == '$':
                # Display math delimiter
                result.append('$$')
                i += 2
                continue
            # Find closing $
            end = line.find('$', i + 1)
            if end == -1:
                result.append(line[i:])
                break
            content = line[i + 1:end]
            # Strip leading/trailing spaces from math content
            fixed = '$' + content.strip() + '$'
            result.append(fixed)
            i = end + 1
            continue
        result.append(line[i])
        i += 1
    return ''.join(result)


def fix_obsidian_spacing(line):
    """Add space: (#slug → ( #slug."""
    return re.sub(r'\(#([a-z])', r'( #\1', line)


def fix_backslash_pipe_in_math(line):
    """Replace \\| with \\Vert inside math spans."""
    spans = find_math_spans(line)
    if not spans:
        return line
    # Process spans in reverse so positions stay valid after replacements
    for start, end, _ in reversed(spans):
        content = line[start:end]
        fixed = re.sub(r'(?<!l)(?<!r)(?<!\\)\\\|', r'\\Vert', content)
        if fixed != content:
            line = line[:start] + fixed + line[end:]
    return line


def fix_asterisk_in_inline_math(line):
    """Replace bare * with \\ast inside inline $...$ math."""
    spans = find_math_spans(line)
    if not spans:
        return line
    # Process spans in reverse order so positions stay valid
    for start, end, is_display in reversed(spans):
        if is_display:
            continue
        content = line[start:end]
        fixed = re.sub(r'(?<!\\)\*', r'\\ast', content)
        if fixed != content:
            line = line[:start] + fixed + line[end:]
    return line


def fix_angle_brackets_in_math(line):
    """Replace raw < and > with \\lt and \\gt inside math."""
    spans = find_math_spans(line)
    if not spans:
        return line
    for start, end, _ in reversed(spans):
        content = line[start:end]
        fixed = re.sub(r'(?<!\\)<', r'\\lt', content)
        fixed = re.sub(r'(?<!\\)>', r'\\gt', fixed)
        if fixed != content:
            line = line[:start] + fixed + line[end:]
    return line


def fix_begin_align(line):
    r"""Replace \begin{align} with \begin{aligned}."""
    return line.replace(r'\begin{align}', r'\begin{aligned}').replace(
        r'\end{align}', r'\end{aligned}')


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def lint_file(filepath, fix=False):
    """Lint a single file. Returns list of (file, line, col, message)."""
    path = Path(filepath)
    text = path.read_text()
    lines = text.split('\n')
    all_issues = []
    ctx = MathContext()

    # Per-line checks
    for i, line in enumerate(lines):
        lineno = i + 1

        # Track code blocks
        if ctx.update_code_block(line):
            if ctx.in_code_block:
                continue
            continue
        if ctx.in_code_block:
            continue

        # Skip table header separator rows
        if re.match(r'^\|[-\s|:]+\|$', line.strip()):
            continue

        spans = find_math_spans(line)

        all_issues.extend(
            (str(path), ln, col, msg)
            for ln, col, msg in check_math_spacing(line, lineno, spans)
        )
        all_issues.extend(
            (str(path), ln, col, msg)
            for ln, col, msg in check_pipe_in_math(line, lineno, spans)
        )
        all_issues.extend(
            (str(path), ln, col, msg)
            for ln, col, msg in check_raw_angle_in_math(line, lineno, spans)
        )
        all_issues.extend(
            (str(path), ln, col, msg)
            for ln, col, msg in check_bare_asterisk_in_inline_math(line, lineno, spans)
        )
        all_issues.extend(
            (str(path), ln, col, msg)
            for ln, col, msg in check_begin_align(line, lineno)
        )
        all_issues.extend(
            (str(path), ln, col, msg)
            for ln, col, msg in check_obsidian_tag_spacing(line, lineno)
        )
        all_issues.extend(
            (str(path), ln, col, msg)
            for ln, col, msg in check_bare_unicode_greek(line, lineno, spans)
        )
        all_issues.extend(
            (str(path), ln, col, msg)
            for ln, col, msg in check_bare_ascii_math(line, lineno, spans)
        )

    # Multi-line checks
    all_issues.extend(
        (str(path), ln, col, msg)
        for ln, col, msg in check_display_math_blank_lines(lines)
    )

    # Apply fixes if requested
    if fix and all_issues:
        fixed_lines = []
        ctx = MathContext()
        for line in lines:
            if ctx.update_code_block(line):
                fixed_lines.append(line)
                continue
            if ctx.in_code_block:
                fixed_lines.append(line)
                continue
            line = fix_math_spacing(line)
            line = fix_obsidian_spacing(line)
            line = fix_backslash_pipe_in_math(line)
            line = fix_asterisk_in_inline_math(line)
            line = fix_angle_brackets_in_math(line)
            line = fix_begin_align(line)
            fixed_lines.append(line)

        new_text = '\n'.join(fixed_lines)
        if new_text != text:
            path.write_text(new_text)
            # Re-lint to show remaining issues
            return lint_file(filepath, fix=False)

    return all_issues


def main():
    args = sys.argv[1:]
    fix = '--fix' in args
    if fix:
        args.remove('--fix')

    if not args:
        # Default: top-level *.md files
        root = Path(__file__).resolve().parent.parent
        args = sorted(str(p) for p in root.glob('*.md'))

    total = 0
    for filepath in args:
        issues = lint_file(filepath, fix=fix)
        for fpath, lineno, col, msg in issues:
            print(f'{fpath}:{lineno}:{col}: {msg}')
            total += 1

    if total:
        print(f'\n{total} issue(s) found.')
        return 1
    else:
        print('All clean.')
        return 0


if __name__ == '__main__':
    sys.exit(main())
