#!/usr/bin/env python3
"""
Lint markdown files against ACT's FORMAT.md conventions.

Usage:
    bin/lint-md.py [--fix] [files...]

If no files given, lints all top-level *.md files.
With --fix, applies safe auto-fixes and re-reports remaining issues.

Exit code 0 = clean, 1 = violations found.

Checks implemented (see FORMAT.md for rationale):
  - math-spacing:     no space after opening $ or before closing $
  - pipe-in-math:     use \\vert not | ; \\Vert not \\|
  - angle-in-math:    use \\lt \\gt not < >
  - asterisk-in-math: use \ast not * in inline math
  - begin-align:      use \begin{aligned} not \begin{align}
  - obsidian-spacing:  space before #slug in parens
  - bare-greek:       Unicode Greek math vars outside $
  - bare-ascii-math:  ASCII math patterns like M_t outside $
  - display-math-blanks: $$ needs blank lines around it
  - hard-wrap:        lines broken at fixed column width (auto-fixable)
  - text-underscore:  _ inside \text{} breaks GitHub (auto-fixable → -)
  - emphasis-vuln:    multiple $..._...$ spans risk GitHub emphasis (auto-fixable)
  - latex-outside:    LaTeX commands outside $ suggest missing delimiters
"""

import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Hard-wrap detection: lines shorter than this that end mid-sentence
# and are followed by a continuation line suggest hard-wrapping.
HARD_WRAP_MAX = 90

# Unicode Greek letters that should be inside $...$ when used as math variables.
GREEK_MATH = {
    'Σ': r'\Sigma', 'σ': r'\sigma', 'δ': r'\delta', 'ε': r'\varepsilon',
    'η': r'\eta', 'ρ': r'\rho', 'α': r'\alpha', 'β': r'\beta',
    'γ': r'\gamma', 'λ': r'\lambda', 'π': r'\pi', 'τ': r'\tau',
    'μ': r'\mu', 'φ': r'\phi', 'θ': r'\theta', 'ω': r'\omega',
    'Ω': r'\Omega', 'Π': r'\Pi',
}

# Ancient Greek words (etymology) — should NOT be flagged
GREEK_WORDS = re.compile(
    r'[\u0370-\u03FF\u1F00-\u1FFF][\u0370-\u03FF\u1F00-\u1FFF]+'
)

# ASCII math variable patterns that should be in $...$
ASCII_MATH_VAR = re.compile(
    r'(?<![`$\\a-zA-Z_])'  # not preceded by code/math/word chars
    r'([A-Z]_[a-z{}]|[a-z]_[A-Z])'  # e.g., M_t, f_M
    r'(?![`])'  # not followed by backtick
)

# LaTeX commands that only make sense in math mode — strong signal
# of missing $ delimiters when found outside math spans.
LATEX_OUTSIDE_MATH = re.compile(
    r'\\(?:frac|sum|prod|int|partial|mathcal|mathbb|mathbf|mathrm|'
    r'hat|tilde|bar|vec|dot|ddot|mid|vert|lvert|rvert|lVert|rVert|Vert|'
    r'leq|geq|neq|to|rightarrow|leftarrow|Sigma|delta|varepsilon|'
    r'alpha|beta|gamma|lambda|eta|rho|pi|tau|mu|phi|theta|omega|'
    r'text|operatorname|begin|end|cdot|times|sqrt|infty|forall|exists|'
    r'in|subset|supset|cup|cap|land|lor|neg|lvert|rvert)(?![a-zA-Z])'
)

# LaTeX commands where single-char arguments can safely have braces removed.
# \hat{P}_ → \hat P_ (makes _ follow alpha, preventing GitHub emphasis)
BRACE_REMOVABLE_CMDS = (
    'hat', 'tilde', 'bar', 'vec', 'dot', 'ddot', 'check', 'breve',
    'acute', 'grave', 'widehat', 'widetilde', 'overline',
    'mathcal', 'mathbb', 'mathbf', 'mathrm', 'mathit', 'mathsf',
    'mathtt', 'boldsymbol', 'bm',
)


# ---------------------------------------------------------------------------
# State-tracking helpers
# ---------------------------------------------------------------------------

class MathContext:
    """Track whether we're in code blocks."""

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
            if stripped.startswith('```') and stripped.rstrip('`') in ('', stripped.split('`')[0]):
                self.in_code_block = False
                return True
        return self.in_code_block


def find_math_spans(line):
    """Find all $...$ and $$...$$ spans in a line, returning (start, end, is_display)."""
    spans = []
    i = 0
    while i < len(line):
        if line[i] == '`':
            end = line.find('`', i + 1)
            if end == -1:
                break
            i = end + 1
            continue
        if line[i] == '$':
            is_display = (i + 1 < len(line) and line[i + 1] == '$')
            if is_display:
                end = line.find('$$', i + 2)
                if end != -1:
                    spans.append((i, end + 2, True))
                    i = end + 2
                    continue
                i += 2
                continue
            else:
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
# Per-line checks
# ---------------------------------------------------------------------------

def check_math_spacing(line, lineno, spans):
    """Rule: no space after opening $ or before closing $."""
    issues = []
    for start, end, is_display in spans:
        if is_display:
            continue
        content = line[start:end]
        if len(content) > 2 and content[1] == ' ':
            issues.append((lineno, start + 1,
                           f'space after opening $: {content[:20]}...'))
        if len(content) > 2 and content[-2] == ' ':
            issues.append((lineno, end - 2,
                           f'space before closing $: ...{content[-20:]}'))
    return issues


def check_pipe_in_math(line, lineno, spans):
    """Rule: use \\vert not | inside math; \\Vert not \\| inside math."""
    issues = []
    for start, end, _ in spans:
        content = line[start:end]
        for m in re.finditer(r'(?<!\\)(?<!l)(?<!r)\|', content):
            pos = m.start()
            preceding = content[max(0, pos - 6):pos]
            if not re.search(r'\\[lr]?vert$|\\mid$|\\lVert$|\\rVert$|\\Vert$', preceding):
                issues.append((lineno, start + pos,
                               f'bare | in math — use \\vert, \\lvert/\\rvert, or \\mid'))
        for m in re.finditer(r'\\\|', content):
            pos = m.start()
            preceding = content[max(0, pos - 2):pos]
            if preceding not in ('\\l', '\\r'):
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
    """Rule: use \\ast not bare * in inline $...$."""
    issues = []
    for start, end, is_display in spans:
        if is_display:
            continue
        content = line[start:end]
        for m in re.finditer(r'(?<!\\)\*', content):
            issues.append((lineno, start + m.start(),
                           'bare * in inline math — use \\ast (markdown italic conflict)'))
    return issues


def check_begin_align(line, lineno):
    """Rule: use \\begin{aligned} not \\begin{align} inside $$."""
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
            before = line[max(0, pos - 1):pos]
            after = line[pos + 1:pos + 3] if pos + 1 < len(line) else ''
            greek_range = re.compile(r'[\u0370-\u03FF\u1F00-\u1FFF]')
            if (before and greek_range.search(before)) or (after and greek_range.search(after[0:1])):
                continue
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
        ctx = line[max(0, pos - 2):pos]
        if ctx.endswith('`') or ctx.endswith('#'):
            continue
        snippet = m.group()
        issues.append((lineno, pos,
                       f'bare math variable outside $: {snippet}'))
    return issues


def check_text_underscore_in_math(line, lineno, spans):
    """Rule: _ inside \\text{} breaks GitHub rendering."""
    issues = []
    for start, end, _ in spans:
        content = line[start:end]
        for m in re.finditer(r'\\text\{([^}]*_[^}]*)\}', content):
            issues.append((lineno, start + m.start(),
                           f'_ inside \\text{{}} — use - or space: '
                           f'\\text{{{m.group(1)}}}'))
    return issues


def check_underscore_emphasis(line, lineno, spans):
    """Warn when multiple inline $..._...$ could trigger GitHub emphasis.

    GitHub's markdown parser can match _ across different $...$ spans as
    emphasis delimiters, breaking both math expressions.  This happens
    when _ follows a non-alphanumeric character (like }) — GFM treats
    such _ as a potential emphasis opener/closer.
    """
    vulnerable = []
    for start, end, is_display in spans:
        if is_display:
            continue
        content = line[start:end]
        # _ preceded by non-alpha (like }) can trigger emphasis
        for m in re.finditer(r'(?<![a-zA-Z])_', content):
            vulnerable.append(start + m.start())

    if len(vulnerable) >= 2:
        return [(lineno, vulnerable[0],
                 f'{len(vulnerable)} inline math spans with emphasis-vulnerable _ '
                 f'— GitHub may break rendering (fix: remove optional braces before _)')]
    return []


def check_latex_outside_math(line, lineno, spans):
    """Detect LaTeX commands outside math spans — suggests missing $ delimiters."""
    issues = []
    for m in LATEX_OUTSIDE_MATH.finditer(line):
        pos = m.start()
        if is_in_any_special(line, pos, spans):
            continue
        issues.append((lineno, pos,
                       f'LaTeX command outside math: {m.group()} (missing $ delimiters?)'))
    return issues


# ---------------------------------------------------------------------------
# Multi-line checks
# ---------------------------------------------------------------------------

def check_display_math_blank_lines(lines):
    """Rule: display math $$ must have blank lines before and after."""
    issues = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == '$$':
            if i > 0 and lines[i - 1].strip() != '':
                issues.append((i + 1, 0, '$$ should have a blank line before it'))
            if i < len(lines) - 1 and lines[i + 1].strip() != '':
                issues.append((i + 1, 0, '$$ should have a blank line after it'))
    return issues


def check_hard_wrapping(lines):
    """Detect lines broken at a fixed column width instead of letting renderers wrap.

    Heuristic: a line shorter than HARD_WRAP_MAX that ends mid-sentence
    (no terminal punctuation) and is followed by a continuation line at
    the same or expected indent level.
    """
    issues = []
    ctx = MathContext()
    in_yaml = None  # None = before first ---, True = in frontmatter
    in_display_math = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # YAML frontmatter
        if stripped == '---':
            if in_yaml is None:
                in_yaml = True
            elif in_yaml:
                in_yaml = False
            continue
        if in_yaml:
            continue

        # Code blocks
        if ctx.update_code_block(line):
            continue
        if ctx.in_code_block:
            continue

        # Display math
        if stripped == '$$':
            in_display_math = not in_display_math
            continue
        if in_display_math:
            continue

        # Skip non-prose lines
        if not stripped or stripped.startswith('#'):
            continue
        if stripped.startswith('|') and '|' in stripped[1:]:
            continue
        if stripped in ('---', '***', '- - -'):
            continue

        line_len = len(line.rstrip())
        if line_len > HARD_WRAP_MAX:
            continue

        if i + 1 >= len(lines):
            continue

        next_line = lines[i + 1]
        next_stripped = next_line.strip()

        if not next_stripped:
            continue
        if next_stripped.startswith('#') or next_stripped.startswith('$$'):
            continue
        if next_stripped.startswith('|') and '|' in next_stripped[1:]:
            continue
        if next_stripped in ('---', '***'):
            continue

        # Current line must end mid-sentence.
        # Strip trailing markdown formatting (bold **, italic _, closing ))
        # before checking for sentence-ending punctuation.
        rstripped = line.rstrip()
        end_check = rstripped.rstrip('*_)`')
        if end_check and end_check[-1] in '.!?:;':
            continue

        curr_indent = len(line) - len(line.lstrip())
        next_indent = len(next_line) - len(next_line.lstrip())

        # New list item at same or lesser indent = not continuation
        if (re.match(r'^[-*] ', next_stripped) or re.match(r'^\d+\. ', next_stripped)):
            if next_indent <= curr_indent:
                continue

        # Paragraph continuation: same indent, not a new block element.
        # If current line IS a list item, same-indent means a sibling item,
        # not a continuation — skip (continuations use content indent).
        curr_is_list = (re.match(r'^[-*] ', stripped)
                        or re.match(r'^\d+\. ', stripped))
        if next_indent == curr_indent and not curr_is_list:
            if not (re.match(r'^[-*] ', next_stripped) or re.match(r'^\d+\. ', next_stripped)):
                issues.append((i + 1, 0, f'possible hard wrap (len {line_len})'))
                continue

        # List item continuation: indented to content level
        if stripped.startswith('- ') or stripped.startswith('* '):
            if next_indent == curr_indent + 2:
                issues.append((i + 1, 0,
                               f'possible hard wrap in list item (len {line_len})'))
                continue
        m = re.match(r'^(\d+\. )', stripped)
        if m and next_indent == curr_indent + len(m.group(1)):
            issues.append((i + 1, 0,
                           f'possible hard wrap in numbered list (len {line_len})'))

    return issues


# ---------------------------------------------------------------------------
# Auto-fix functions
# ---------------------------------------------------------------------------

def fix_math_spacing(line):
    """Remove spaces after opening $ and before closing $ in inline math."""
    result = []
    i = 0
    while i < len(line):
        if line[i] == '`':
            end = line.find('`', i + 1)
            if end == -1:
                result.append(line[i:])
                break
            result.append(line[i:end + 1])
            i = end + 1
            continue
        if line[i] == '$':
            if i + 1 < len(line) and line[i + 1] == '$':
                result.append('$$')
                i += 2
                continue
            end = line.find('$', i + 1)
            if end == -1:
                result.append(line[i:])
                break
            content = line[i + 1:end]
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
    r"""Replace \| with \Vert inside math spans."""
    spans = find_math_spans(line)
    if not spans:
        return line
    for start, end, _ in reversed(spans):
        content = line[start:end]
        fixed = re.sub(r'(?<!l)(?<!r)(?<!\\)\\\|', r'\\Vert', content)
        if fixed != content:
            line = line[:start] + fixed + line[end:]
    return line


def fix_asterisk_in_inline_math(line):
    r"""Replace bare * with \ast inside inline $...$ math."""
    spans = find_math_spans(line)
    if not spans:
        return line
    for start, end, is_display in reversed(spans):
        if is_display:
            continue
        content = line[start:end]
        fixed = re.sub(r'(?<!\\)\*', r'\\ast', content)
        if fixed != content:
            line = line[:start] + fixed + line[end:]
    return line


def fix_angle_brackets_in_math(line):
    r"""Replace raw < and > with \lt and \gt inside math."""
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
    r"""Replace \begin{align} with \begin{aligned}, skipping code spans."""
    # Process outside code spans only
    result = []
    i = 0
    while i < len(line):
        if line[i] == '`':
            end = line.find('`', i + 1)
            if end == -1:
                result.append(line[i:])
                break
            result.append(line[i:end + 1])
            i = end + 1
            continue
        result.append(line[i])
        i += 1
    out = ''.join(result)
    # Now do the replacement only on the non-code parts
    # Actually, rebuild properly: walk segments, replace only outside backticks
    parts = []
    i = 0
    while i < len(line):
        if line[i] == '`':
            end = line.find('`', i + 1)
            if end == -1:
                parts.append(line[i:])
                break
            parts.append(line[i:end + 1])  # code span, preserve
            i = end + 1
            continue
        # Find next backtick or end
        next_bt = line.find('`', i)
        if next_bt == -1:
            segment = line[i:]
            parts.append(
                segment.replace(r'\begin{align}', r'\begin{aligned}')
                       .replace(r'\end{align}', r'\end{aligned}'))
            break
        segment = line[i:next_bt]
        parts.append(
            segment.replace(r'\begin{align}', r'\begin{aligned}')
                   .replace(r'\end{align}', r'\end{aligned}'))
        i = next_bt
    return ''.join(parts)


def fix_text_underscore_in_math(line):
    r"""Replace _ with - inside \text{} in math spans."""
    spans = find_math_spans(line)
    if not spans:
        return line
    for start, end, _ in reversed(spans):
        content = line[start:end]

        def _replace_underscores(m):
            return '\\text{' + m.group(1).replace('_', '-') + '}'

        fixed = re.sub(r'\\text\{([^}]*_[^}]*)\}', _replace_underscores, content)
        if fixed != content:
            line = line[:start] + fixed + line[end:]
    return line


def fix_emphasis_braces(line):
    r"""Remove optional braces before _ in inline math to prevent GitHub emphasis.

    GitHub's markdown parser can match _ across $...$ spans as emphasis.
    This happens when _ follows non-alpha (like }).  Fix: remove optional
    braces from single-char arguments — \hat{P}_ → \hat P_ — so _ follows
    an alpha character and cannot trigger emphasis.

    Safe because LaTeX treats \hat{X} and \hat X identically for single chars.
    """
    spans = find_math_spans(line)
    if not spans:
        return line
    cmds = '|'.join(re.escape(c) for c in BRACE_REMOVABLE_CMDS)
    pattern = re.compile(r'(\\(?:' + cmds + r'))\{([a-zA-Z])\}(_)')
    for start, end, is_display in reversed(spans):
        if is_display:
            continue
        content = line[start:end]
        fixed = pattern.sub(r'\1 \2\3', content)
        if fixed != content:
            line = line[:start] + fixed + line[end:]
    return line


def fix_hard_wrapping(lines):
    """Join hard-wrapped continuation lines within paragraphs and list items.

    Walks through lines, detecting paragraphs where all inner lines are
    shorter than HARD_WRAP_MAX and end mid-sentence.  Joins them into
    single lines as FORMAT.md requires.
    """
    result = []
    ctx = MathContext()
    in_yaml = None
    in_display_math = False
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # YAML frontmatter
        if stripped == '---':
            if in_yaml is None:
                in_yaml = True
            elif in_yaml:
                in_yaml = False
            result.append(line)
            i += 1
            continue
        if in_yaml:
            result.append(line)
            i += 1
            continue

        # Code blocks — pass through entirely
        if stripped.startswith('```'):
            result.append(line)
            i += 1
            while i < len(lines):
                result.append(lines[i])
                if lines[i].strip().startswith('```'):
                    i += 1
                    break
                i += 1
            continue

        # Display math — pass through
        if stripped == '$$':
            in_display_math = not in_display_math
            result.append(line)
            i += 1
            continue
        if in_display_math:
            result.append(line)
            i += 1
            continue

        # Non-prose: pass through
        if not stripped or stripped.startswith('#'):
            result.append(line)
            i += 1
            continue
        if stripped.startswith('|') and '|' in stripped[1:]:
            result.append(line)
            i += 1
            continue
        if stripped in ('---', '***', '- - -'):
            result.append(line)
            i += 1
            continue

        # Prose line — check for hard-wrapping
        line_len = len(line.rstrip())
        curr_indent = len(line) - len(line.lstrip())

        # Determine continuation indent for list items
        is_list = stripped.startswith('- ') or stripped.startswith('* ')
        m_num = re.match(r'^(\d+\. )', stripped)
        is_numbered = bool(m_num)
        if is_list:
            cont_indent = curr_indent + 2
        elif is_numbered:
            cont_indent = curr_indent + len(m_num.group(1))
        else:
            cont_indent = curr_indent

        # Try to join continuation lines if this line looks hard-wrapped
        rstripped = line.rstrip()
        end_check = rstripped.rstrip('*_)`')
        if (line_len <= HARD_WRAP_MAX and end_check
                and end_check[-1] not in '.!?:;'):
            joined = rstripped
            j = i + 1
            while j < len(lines):
                nline = lines[j]
                nstripped = nline.strip()
                nindent = len(nline) - len(nline.lstrip())

                # Stop at blank lines or block elements
                if not nstripped:
                    break
                if nstripped.startswith('#') or nstripped.startswith('$$'):
                    break
                if nstripped.startswith('```'):
                    break
                if nstripped.startswith('|') and '|' in nstripped[1:]:
                    break
                if nstripped in ('---', '***'):
                    break
                # New list item at same or lesser indent
                if (re.match(r'^[-*] ', nstripped)
                        or re.match(r'^\d+\. ', nstripped)):
                    if nindent <= curr_indent:
                        break

                # Must match continuation indent
                if nindent != cont_indent:
                    break

                # Join this continuation line
                joined = joined + ' ' + nstripped
                j += 1

                # If this continuation ends at a sentence boundary and
                # the NEXT line would not be a continuation, stop here
                if joined.rstrip()[-1:] in '.!?:;':
                    # Check if next line would also be a continuation
                    if j < len(lines):
                        peek = lines[j]
                        peek_stripped = peek.strip()
                        peek_indent = len(peek) - len(peek.lstrip())
                        if (not peek_stripped
                                or peek_stripped.startswith('#')
                                or peek_indent != cont_indent
                                or re.match(r'^[-*] ', peek_stripped)
                                or re.match(r'^\d+\. ', peek_stripped)):
                            break
                        # Next line IS a continuation — but is the current
                        # joined line now long enough to not be hard-wrapped?
                        # Keep going only if the next line is short too.
                        if len(peek.rstrip()) > HARD_WRAP_MAX:
                            break

            if j > i + 1:
                result.append(joined)
                i = j
                continue

        result.append(line)
        i += 1

    return result


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
        all_issues.extend(
            (str(path), ln, col, msg)
            for ln, col, msg in check_text_underscore_in_math(line, lineno, spans)
        )
        all_issues.extend(
            (str(path), ln, col, msg)
            for ln, col, msg in check_underscore_emphasis(line, lineno, spans)
        )
        all_issues.extend(
            (str(path), ln, col, msg)
            for ln, col, msg in check_latex_outside_math(line, lineno, spans)
        )

    # Multi-line checks
    all_issues.extend(
        (str(path), ln, col, msg)
        for ln, col, msg in check_display_math_blank_lines(lines)
    )
    all_issues.extend(
        (str(path), ln, col, msg)
        for ln, col, msg in check_hard_wrapping(lines)
    )

    # Apply fixes if requested
    if fix and all_issues:
        # Multi-line fix: hard wrapping (must run first, before per-line fixes)
        fixed_lines = fix_hard_wrapping(lines)

        # Per-line fixes
        ctx = MathContext()
        final_lines = []
        for line in fixed_lines:
            if ctx.update_code_block(line):
                final_lines.append(line)
                continue
            if ctx.in_code_block:
                final_lines.append(line)
                continue
            line = fix_math_spacing(line)
            line = fix_obsidian_spacing(line)
            line = fix_backslash_pipe_in_math(line)
            line = fix_asterisk_in_inline_math(line)
            line = fix_angle_brackets_in_math(line)
            line = fix_begin_align(line)
            line = fix_text_underscore_in_math(line)
            line = fix_emphasis_braces(line)
            final_lines.append(line)

        new_text = '\n'.join(final_lines)
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
