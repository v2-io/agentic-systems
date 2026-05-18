# frozen_string_literal: true
#
# mono/lib/segment_renderer.rb
#
# Render an AAT-formatted segment markdown file to LaTeX.
#
# Architecture follows neurips/bin/build's pattern (custom kramdown parser
# + custom converter) but is specialized for AAT's segment cadence as
# defined in FORMAT.md:
#
#   YAML frontmatter (slug, type, status, depends, stage)
#   # Title
#   one-sentence summary paragraph
#   ## Formal Expression  (often with equation-level *[Tag]* paragraphs)
#   ## Epistemic Status
#   ## Discussion
#   ## Findings   (optional)
#   ## Working Notes  (optional; stripped in :public variant)
#
# The frontmatter `type:` and `status:` flow into \segmenthead's third
# argument; the first H1 becomes the title. H2 sections render as
# \segmentsubhead{...}. Paragraphs whose only content is *[text]* are
# recognized as equation-level tags and emit \eqtag{text}.
#
# Cross-references `#slug-name` in running prose become \cref{seg:slug-name}
# (the segment header emits a matching \label).
#
# Variants:
#   :public   strips ## Working Notes entirely
#   :review   keeps Working Notes, surfaces the `stage:` field as marginalia
#
# Math is passed through verbatim — math-compat macros (\lt, \gt, \ast) are
# defined in the LaTeX preamble so the source markdown stays viewer-friendly.

require 'kramdown'
require 'kramdown/parser/kramdown'
require 'yaml'

module Mono
  module SegmentRenderer
    module_function

    # Top-level entry point. Reads a segment file, returns a LaTeX fragment.
    #
    # `container:` is the outline walker's classification of where this
    # segment lives — :part (default; renders as a \segmenthead-style
    # section) or :appendices (renders as a \segmentappendixchapter — a
    # native \chapter, since appendix segments are themselves chapter-
    # level entities per the four-volume hierarchy). build-monograph
    # passes item[:container] through.
    def render(path, variant: :public, container: :part)
      raw = File.read(path)
      front, body = split_frontmatter(raw)
      body = strip_working_notes(body) if variant == :public
      body = strip_html_comments(body)
      body = preprocess_math_pipes(body)

      doc = Kramdown::Document.new(
        body,
        input: 'AsfSegment',
        # Pass parsed frontmatter so the converter can emit \segmenthead
        # with the right type/status/title without re-parsing.
        asf_frontmatter: front,
        asf_variant:     variant,
        asf_container:   container,
      )
      doc.to_asf_latex
    end

    # Render a raw markdown fragment (no segment frontmatter / no segment
    # chrome) — used by build-monograph for volume frontmatter and Part
    # preface content. Same kramdown pipeline as render() so math, cross-
    # refs, bold/italic, links, callouts, lists all process correctly,
    # but no \segmenthead / \segmentfoot / segment-counter advance.
    def render_fragment(text, variant: :review)
      text = strip_html_comments(text)
      text = strip_paragraph_italic_wrap(text)
      text = ensure_list_blank_line(text)
      text = preprocess_math_pipes(text)

      doc = Kramdown::Document.new(
        text,
        input: 'AsfSegment',
        asf_frontmatter: {},
        asf_variant:     variant,
        asf_mode:        :fragment,
      )
      doc.to_asf_latex
    end

    # Strip HTML comments — single-line, inline, and multi-line. Pairs
    # with the same discipline applied at the walker for OUTLINE.md; both
    # places need it because segment files can also carry repo-meta
    # commentary that shouldn't reach the rendered PDF.
    def strip_html_comments(text)
      text.gsub(/<!--.*?-->/m, '')
    end

    # Kramdown (strict) requires a blank line before a list when the list
    # follows a non-list line — otherwise the list-marker lines are absorbed
    # into the preceding paragraph and render as inline text. Authors often
    # omit the blank line ("**TODO**:\n- item 1\n- item 2"), so this fixup
    # inserts it. List-to-list line transitions are left alone (a blank
    # line between sibling items would split the list).
    LIST_MARKER_RE = /\A\s*([-*+]|\d+\.)\s/
    def ensure_list_blank_line(text)
      lines  = text.split("\n", -1)
      result = []
      lines.each_with_index do |line, i|
        prev = i.positive? ? lines[i - 1] : nil
        if line.match?(LIST_MARKER_RE) && prev && !prev.strip.empty? && !prev.match?(LIST_MARKER_RE)
          result << ''
        end
        result << line
      end
      result.join("\n")
    end

    # Obsidian-style "wrap the whole paragraph in `*…*` to italicize it"
    # is an authoring tic — readable on the source side, but in the
    # printed PDF we don't want long stretches of all-italic prose. For
    # each paragraph, if it's entirely wrapped in a SINGLE asterisk on
    # each end (not the `**…**` bold form), strip the outer asterisks.
    # Internal `*emphasis*` and `**bold**` still pass to kramdown
    # unchanged and render as expected.
    def strip_paragraph_italic_wrap(text)
      text.split(/\n[ \t]*\n/).map do |para|
        stripped = para.strip
        if stripped.match?(/\A\*(?!\*).*(?<!\*)\*\z/m) &&
           !stripped.start_with?('**') && !stripped.end_with?('**')
          stripped.sub(/\A\*/, '').sub(/\*\z/, '')
        else
          para
        end
      end.join("\n\n")
    end

    # ── Helpers ────────────────────────────────────────────────────────────

    def split_frontmatter(text)
      return [{}, text] unless text.start_with?("---\n")

      _, fm, body = text.split(/^---\s*$/, 3)
      [YAML.safe_load(fm || ''), body.to_s.lstrip]
    end

    # Working Notes is always the trailing section by FORMAT discipline, so
    # truncation at the last `## Working Notes` heading is safe.
    def strip_working_notes(body)
      idx = body.rindex(/^##[ \t]+Working Notes\b/m)
      idx ? "#{body[0...idx].rstrip}\n" : body
    end

    # FORMAT.md prescribes `\vert` / `\Vert` for math bars (raw `|` breaks
    # GitHub's math renderer), but some segments still use raw `|` (and
    # `\|`, the deprecated double-bar) inside `$...$`. Two problems with
    # raw `|` for our pipeline: (1) kramdown's block-level table parser
    # sees the `|`s and tries to parse the paragraph as a table, destroying
    # the math; (2) typography is more consistent under \vert / \Vert.
    #
    # Pre-process the body before kramdown sees it. Order matters:
    # (a) $$...$$ first (so an inner $ doesn't end the span early),
    # (b) single-$ second,
    # (c) within each span, `\|` → `\Vert ` first (double-bar — handled
    #     before single, otherwise the `|` of `\|` would be rewritten),
    # (d) bare `|` (no preceding backslash) → `\vert `.
    def preprocess_math_pipes(body)
      body = body.gsub(/\$\$([\s\S]+?)\$\$/) do
        "$$#{rewrite_bars(Regexp.last_match(1))}$$"
      end
      body.gsub(/\$([^$\n]+?)\$/) do
        "$#{rewrite_bars(Regexp.last_match(1))}$"
      end
    end

    def rewrite_bars(math)
      math.gsub('\\|', '\\Vert ').gsub(/(?<!\\)\|/, '\\vert ')
    end
  end
end

# ──────────────────────────────────────────────────────────────────────────
# Parser — extends kramdown with: single-dollar inline math; equation-level
# tag recognition. Both are AAT source-side idioms that kramdown wouldn't
# pick up otherwise.
# ──────────────────────────────────────────────────────────────────────────

class Kramdown::Parser::AsfSegment < Kramdown::Parser::Kramdown
  # Kramdown's default ATX_HEADER_START has `[\t ]*` (zero-or-more space
  # after the hashes), so it eats `#slug-name` at line start as a level-1
  # header. CommonMark / GFM require at least one space; we follow that
  # stricter discipline so cross-refs at paragraph starts survive.
  ATX_HEADER_START = /^(?<level>\#{1,6})[\t ]+(?<contents>[^ \t].*)\n/

  # Obsidian-style callout: a blockquote whose first line is `[!type]`
  # (optionally with title following, and an optional anchor `^name`).
  # We claim these before the standard :blockquote parser so the type and
  # title round-trip to the converter as attributes instead of leaking
  # into the body as literal text.
  CALLOUT_START = /^#{OPT_SPACE}>[ \t]*\[!(?<type>\w+)\][+-]?/
  CALLOUT_MARKER_LINE = /\A\[!(?<type>\w+)\][+-]?[ \t]*(?<title>.*?)\s*(?:\n|\z)/m

  # Single-dollar inline math (e.g., `$x = y$`). Upstream only recognizes
  # `$$...$$`. The negative lookarounds keep us out of $$...$$'s lane.
  SINGLE_DOLLAR_MATH = /(?<!\$)\$(?!\$)([^$\n]+?)\$(?!\$)/

  # Equation-level tags: a paragraph whose ENTIRE content is *[...]*. The
  # parser recognizes this at block level so the tag round-trips as a single
  # AST node, not a chain of em/text fragments the converter would have to
  # sniff. Examples:
  #
  #   *[Derived (slug, from prior-slug)]*
  #   *[Hypothesis]*
  #   *[Postulate (slug)]*
  #
  # Captured group is the tag content (inside the square brackets).
  EQ_TAG_LINE = /\A#{OPT_SPACE}\*\[([^\]\n]+)\]\*[ \t]*(?:\n|\z)/

  def initialize(source, options)
    super
    @span_parsers.unshift(:single_dollar_math) unless @span_parsers.include?(:single_dollar_math)
    @block_parsers.unshift(:eq_tag) unless @block_parsers.include?(:eq_tag)
    # Callout parser sits just before the default :blockquote parser so the
    # `> [!type]` form gets recognized before falling through to a plain
    # blockquote with literal `[!type]` text inside.
    unless @block_parsers.include?(:callout)
      bq_idx = @block_parsers.index(:blockquote) || 0
      @block_parsers.insert(bq_idx, :callout)
    end
  end

  # Override the inherited parse_atx_header. parse_blocks first matches the
  # parent's looser start_re (zero-or-more space after the hashes); we then
  # re-check with the stricter pattern (space required) and either delegate
  # to super or bail out, letting parse_blocks try the next block parser.
  # The net effect: `#slug-name` at line start is no longer eaten as a
  # header — it falls through to paragraph text where the cross-ref regex
  # in the converter rewrites it to \cref{seg:slug-name}.
  def parse_atx_header
    return false unless @src.check(self.class::ATX_HEADER_START)

    super
  end

  def parse_single_dollar_math
    line = @src.current_line_number
    @src.pos += @src.matched_size
    @tree.children << Element.new(:math, @src[1].strip, nil,
                                  category: :span, location: line)
  end
  define_parser(:single_dollar_math, SINGLE_DOLLAR_MATH, '\\$')

  # rubocop:disable Naming/PredicateMethod -- kramdown's parse_* protocol
  # returns true/false to signal "claimed" vs "passed."
  def parse_eq_tag
    start_line = @src.current_line_number
    return false unless @src.check(EQ_TAG_LINE)

    @src.scan(EQ_TAG_LINE)
    content = @src[1].strip
    el = Element.new(:eq_tag, content, nil, location: start_line)
    @tree.children << el
    true
  end
  # rubocop:enable Naming/PredicateMethod
  define_parser(:eq_tag, EQ_TAG_LINE)

  # Slurp the contiguous `> ...` lines (same algorithm as parse_blockquote),
  # peel off the [!type] marker line, attach type/title as element
  # attributes, then recurse on the remainder so embedded tables, lists,
  # math etc. parse normally.
  # rubocop:disable Naming/PredicateMethod
  def parse_callout
    start_line = @src.current_line_number
    raw        = @src.scan(self.class::PARAGRAPH_MATCH)
    raw << @src.scan(self.class::PARAGRAPH_MATCH) until @src.match?(self.class::LAZY_END)
    raw.gsub!(self.class::BLOCKQUOTE_START, '')

    marker = raw.match(CALLOUT_MARKER_LINE)
    return false unless marker

    type  = marker[:type].downcase
    title = marker[:title].to_s.strip
    body  = raw[marker[0].length..]

    el = new_block_el(:callout, nil, nil, location: start_line)
    el.attr['data-callout-type']  = type
    el.attr['data-callout-title'] = title unless title.empty?
    @tree.children << el
    parse_blocks(el, body)
    true
  end
  # rubocop:enable Naming/PredicateMethod
  define_parser(:callout, CALLOUT_START)
end

# ──────────────────────────────────────────────────────────────────────────
# Converter — kramdown AST → LaTeX, using the segment-environment commands
# defined in mono/preamble/.
# ──────────────────────────────────────────────────────────────────────────

class Kramdown::Converter::AsfLatex < Kramdown::Converter::Latex
  # ── Init ──────────────────────────────────────────────────────────────

  TYPE_LABEL = {
    'postulate'       => 'Postulate',
    'definition'      => 'Definition',
    'scope'           => 'Scope',
    'formulation'     => 'Formulation',
    'derived'         => 'Derived',
    'result'          => 'Result',
    'corollary'       => 'Corollary',
    'hypothesis'      => 'Hypothesis',
    'normative'       => 'Normative',
    'empirical'       => 'Empirical',
    'observation'     => 'Observation',
    'discussion'      => 'Discussion',
    'measurement'     => 'Measurement',
    'proposed-schema' => 'Proposed Schema',
    'derivation'      => 'Derivation',
    'worked-example'  => 'Worked Example',
    'detail'          => 'Detail',
    'sketch'          => 'Sketch',
    'aside'           => 'Aside',
  }.freeze

  # Cross-ref pattern: standalone `#slug-name` in prose. Obsidian discipline
  # (per FORMAT.md) requires a space, line start, or open paren/bracket
  # before the `#`; the trailing boundary is anything non-slug-character.
  CROSS_REF_RE = /(?<=^|[\s(\[])#([a-z][a-z0-9-]*[a-z0-9])(?![a-z0-9-])/

  # After the cross-ref rewrite, collapse "( \cref{...}" → "(\cref{...}" so
  # the Obsidian-required leading space inside parens doesn't produce a
  # visibly-loose `( ref )` in LaTeX. Same for `[ \cref{...}`.
  COLLAPSE_INNER_SPACE_RE = /([(\[])\s+(\\cref\{)/

  def initialize(root, options)
    super
    @frontmatter   = options[:asf_frontmatter] || {}
    @variant       = options[:asf_variant] || :public
    @container     = options[:asf_container] || :part
    # :segment (default) — emit \segmenthead at first header, \segmentfoot
    # at end; treat first header as segment title, subsequent as subheads.
    # :fragment — no segment chrome; first header is just a subhead like
    # any other. Used by render_fragment for frontmatter / preface prose.
    @mode          = options[:asf_mode] || :segment
    # In fragment mode pre-set "head emitted" so the first H1/H2 doesn't
    # trigger the segment_open path.
    @segment_head_emitted = @mode == :fragment
    @section_depth = 0
    @in_working_notes = false
    @in_epigraph     = false
    @in_widesection  = false
    @pending_eqtag   = nil
    @eq_count        = 0
    @table_count     = 0
  end

  # H2 sections that render full-width (body + margin column) rather
  # than constrained to the body column — the Discussion and Findings
  # sections expand to the full segment band so they read as the wider
  # interpretive register, distinct from the formal-derivation content
  # of Formal Expression / Epistemic Status above them.
  WIDE_SECTION_TITLES = %w[Discussion Findings].freeze

  # Per-segment slug, used to build cross-ref labels for equations and
  # tables. Empty when the frontmatter doesn't specify a slug (shouldn't
  # happen for well-formed segments, but we don't want to crash on it).
  def segment_slug = (@frontmatter['slug'] || '').to_s

  # ── Element converters ────────────────────────────────────────────────

  def convert_root(el, opts)
    body = inner(el, opts)
    body += flush_pending_eqtag
    body += "\\end{segmentepigraph}\n" if @in_epigraph
    body += "\\end{segmentwidesection}\n" if @in_widesection
    body += "\\end{workingnotes}\n" if @in_working_notes
    # In fragment mode we skip segment_close — there's no segment
    # boundary to demarcate.
    @mode == :fragment ? body : body + segment_close
  end

  # First header in the document is the segment title; subsequent headers
  # are section subheads inside the segment. The H2 named "Working Notes"
  # opens the workingnotes environment instead of emitting a normal subhead,
  # so the rest of the section reads as backgrounded marginalia.
  def convert_header(el, opts)
    title = inner(el, opts).strip
    if !@segment_head_emitted
      @segment_head_emitted = true
      @in_epigraph = true
      return "#{segment_open(title)}\\begin{segmentepigraph}\n"
    end

    # If a new H2 starts while we're inside the epigraph zone, a wide
    # section, or Working Notes, close those wrappers first. Also flush
    # any pending eqtag so it doesn't leak into the next section as a
    # stray marginnote.
    prefix = flush_pending_eqtag
    if @in_epigraph && el.options[:level] <= 2
      prefix += "\\end{segmentepigraph}\n\n"
      @in_epigraph = false
    end
    if @in_widesection && el.options[:level] <= 2
      prefix += "\\end{segmentwidesection}\n\n"
      @in_widesection = false
    end
    if @in_working_notes && el.options[:level] <= 2
      prefix += "\\end{workingnotes}\n\n"
      @in_working_notes = false
    end

    if el.options[:level] == 2 && title == 'Working Notes'
      @in_working_notes = true
      return "#{prefix}\\begin{workingnotes}\n"
    end

    case el.options[:level]
    when 2
      # Discussion / Findings get a full-width wrapper opened AFTER the
      # subhead label so the section content can extend into the margin
      # column. Other H2s render at body column width as before.
      if WIDE_SECTION_TITLES.include?(title)
        @in_widesection = true
        "#{prefix}\\segmentsubhead{#{title}}\n\n\\begin{segmentwidesection}\n"
      else
        "#{prefix}\\segmentsubhead{#{title}}\n\n"
      end
    when 3
      # H3 bold inline leader — same orphan discipline as the H2 subhead,
      # just less greedy on the reserved space since it sits inline with
      # the first sentence of its paragraph.
      "#{prefix}\\needspace{3\\baselineskip}" \
        "\\par\\medskip\\noindent\\textbf{#{title}.}\\quad "
    else
      "#{prefix}\\par\\noindent\\textit{#{title}.}\\quad "
    end
  end

  # Equation-level tags are emitted lazily: the source puts `*[Tag]*` in
  # its own paragraph BEFORE the equation it labels, but \marginnote
  # attaches at the position where it's called — which leaves the tag
  # floating a line or two above the equation it tags. We hold the tag
  # content in @pending_eqtag and flush it next to the equation itself
  # (convert_math, block category). If no equation follows, the tag
  # falls back to its source-position emission at end-of-segment or when
  # a new eq_tag arrives.
  def convert_eq_tag(el, _opts)
    out = flush_pending_eqtag
    @pending_eqtag = el.value
    out
  end

  def flush_pending_eqtag
    return '' unless @pending_eqtag

    rendered = "\\eqtag{#{escape_eq_tag(@pending_eqtag)}}\n"
    @pending_eqtag = nil
    rendered
  end

  # Obsidian callouts → styled tcolorbox via the LaTeX `callout` env.
  # Type and title are emitted as macro args so the LaTeX side controls
  # color/icon per type (warning/note/info/...).
  def convert_callout(el, opts)
    type  = el.attr['data-callout-type'] || 'note'
    title = el.attr['data-callout-title'] || ''
    "\\begin{callout}{#{type}}{#{process_prose(title)}}\n" \
      "#{inner(el, opts)}" \
      "\\end{callout}\n\n"
  end

  # Paragraphs — rewrite #slug cross-refs as we emit text. Also detect
  # "leader paragraphs" — standalone bold ending in `:` like
  # `**Event-driven update:**` — and treat them as sub-sub-headings so
  # the orphan policy keeps them with the content that follows.
  def convert_p(el, opts)
    if leader_paragraph?(el)
      title = collect_text(el.children.first).chomp(':').rstrip
      return "\\needspace{4\\baselineskip}\\par\\medskip\\noindent" \
             "\\textbf{#{process_prose(title)}:}\\par\\nobreak\\smallskip\\nopagebreak[4]\n"
    end
    rewritten = inner(el, opts)
    # Flush any eqtag we held into this paragraph but didn't consume via
    # a display equation — emit at end-of-paragraph rather than holding
    # further, so the marginnote stays close to its source position
    # instead of leaking forward to the next H2 / segment boundary.
    "#{rewritten}#{flush_pending_eqtag}\n\n"
  end

  # A paragraph qualifies as a leader when its sole child is a :strong
  # element whose text content ends in `:` (the structural signal that
  # the bold is a label for following content, not an inline emphasis).
  def leader_paragraph?(el)
    return false unless el.children.size == 1

    child = el.children.first
    return false unless child.type == :strong

    collect_text(child).rstrip.end_with?(':')
  end

  # Recursively collect text-node values from an element's subtree.
  # Walk an element subtree and return its text content. Crucially,
  # MATH and CODESPAN nodes carry their content in `.value` (not in
  # children) and are otherwise invisible to a naive children-only
  # walk. For the table column-width heuristics they must contribute —
  # a cell that's just `$K_t = P_{t|t-1} H^T (...)^{-1}$` is wide and
  # atomic, and the column has to accommodate it. Returning the source
  # form with delimiters keeps the atomic-token regex in
  # atomic_token_lengths able to recognize the math span as one unit.
  def collect_text(el)
    case el.type
    when :text       then el.value.to_s
    when :math       then "$#{el.value}$"
    when :codespan   then "`#{el.value}`"
    when :smart_quote then el.value.to_s
    else
      return '' if el.children.nil?
      el.children.map { |c| collect_text(c) }.join
    end
  end

  # Text nodes — escape LaTeX specials AND rewrite cross-refs.
  def convert_text(el, _opts)
    process_prose(el.value)
  end

  # Body-text pipeline: LaTeX-escape, rewrite #slug → \cref{seg:slug},
  # collapse the Obsidian-required space inside `( \cref{...})`, then
  # escape any literal `#` that survived the cross-ref pass.
  # Shared by convert_text and by leader-paragraph rendering so all prose
  # routes through the same rewriting.
  def process_prose(str)
    escape_text(str)
      .gsub(CROSS_REF_RE) do
        slug = Regexp.last_match(1)
        # Figures are first-class atoms in the SAME #slug machinery, not
        # a parallel one: a `fig-`-prefixed slug resolves to the figure
        # label namespace (cleveref says "Figure N"), every other slug
        # to the segment namespace, exactly as before. postprocess_latex
        # only rewrites \cref{seg:…}→\externalref, so fig: refs pass clean.
        ns = slug.start_with?('fig-') ? 'fig' : 'seg'
        "\\cref{#{ns}:#{slug}}"
      end
      .gsub(COLLAPSE_INNER_SPACE_RE) { "#{Regexp.last_match(1)}#{Regexp.last_match(2)}" }
      .gsub(/(?<!\\)#/, '\\#')
  end

  # Math — pass through with minimal compatibility shims. Source uses
  # \Vert / \vert / \lt / \gt (FORMAT.md discipline; raw `|`, `<`, `>`
  # break GitHub's math renderer), and they sometimes butt up against a
  # following letter — `\Vertt` / `\ltk` parse as one undefined command in
  # LaTeX. Insert the required space. Same shim concept as old bin/md2context.
  MATH_COMPAT_SHIMS = [
    [/\\Vert([a-zA-Z])/, '\\Vert \1'],
    [/\\vert([a-zA-Z])/, '\\vert \1'],
    [/\\lt([a-zA-Z])/,   '\\lt \1'],
    [/\\gt([a-zA-Z])/,   '\\gt \1'],
    # Cross-ref slugs inside math \text{...} blocks are expository, not
    # link targets; escape the # so LaTeX doesn't read it as a parameter.
    [/(?<!\\)#([a-z])/,  '\\#\1'],
    # `_\mathcal{X}` parses fine under traditional amsmath but unicode-math
    # (LuaLaTeX) wants `_{\mathcal{X}}` for multi-char-command subscripts.
    # Same shim was in the old bin/build-tex ConTeXt path.
    [/([_^])\\([a-zA-Z]+)\{([^}]*)\}/, '\1{\\\\\2{\3}}'],
  ].freeze

  def convert_math(el, _opts)
    value = el.value.dup
    MATH_COMPAT_SHIMS.each { |pat, rep| value.gsub!(pat, rep) }
    if el.options[:category] == :block
      # Display equation — numbered (`equation`, not `equation*`) with a
      # cross-ref label of the form eq:<slug>-<n> for stable referencing.
      # The number itself reads as e.g. `(I.4)` via \numberwithin in the
      # preamble. Any pending eqtag flushes inline with the equation so
      # the marginnote aligns with the equation's first line.
      @eq_count += 1
      tag = ''
      if @pending_eqtag
        tag = "\\eqtag{#{escape_eq_tag(@pending_eqtag)}}%\n"
        @pending_eqtag = nil
      end
      label = segment_slug.empty? ? '' : "\\label{eq:#{segment_slug}-#{@eq_count}}"
      "#{tag}\\begin{equation}\n#{label}#{value}\n\\end{equation}\n"
    else
      # Inline math doesn't consume the pending eqtag.
      "$#{value}$"
    end
  end

  # Raw passthrough for HTML elements we don't render (e.g., comments).
  def convert_html_element(_el, _opts) = ''
  def convert_xml_comment(_el, _opts)  = ''
  def convert_blank(_el, _opts)        = "\n"

  # Tables — kramdown's default emits longtable{|l|l|l|} which doesn't
  # wrap, so any cell wider than its column overflows the page. We swap
  # in xltabular (longtable + tabularx, page-breakable AND wrap-on-width).
  # Columns are X (auto-wrap), alignment-aware via the array-package
  # column-modifier prefix, with per-column weights from
  # table_column_weights so a long-prose column gets more horizontal
  # share than a single-word-label column.
  #
  # Width is \linewidth — adapts to context. In a plain segment section
  # (Formal Expression, Epistemic Status), \linewidth is the body
  # column. Inside a \begin{segmentwidesection} (Discussion / Findings),
  # \linewidth is the full segment band (body + margin column). Using
  # \segmentrulewidth here unconditionally would push every table out
  # into the margin column, overflowing the page in plain-section
  # contexts. \linewidth is the right semantics: "as wide as my
  # current text column."
  #
  # TODO: dynamic column widths. Right now every X column gets equal
  # width via tabularx's default distribution, which wastes space when
  # one column has long prose and the others are short labels (e.g., the
  # "Channel k / Rate / Noise" pattern: short label / medium descriptor /
  # short noise level). Proposed direction — measure each column's max
  # content length (in chars, weighted by header vs body), normalize to
  # weights summing to N (the column count), and emit weighted columns
  # via tabularx's \hsize trick:
  #
  #   \newcolumntype{R}[1]{>{\hsize=#1\hsize\raggedright\arraybackslash}X}
  #   \begin{tabularx}{...}{R{0.4}R{1.2}R{1.4}} ...
  #
  # The renderer scans el.children for the header row + body rows,
  # computes per-column max content (collect_text length plus padding
  # for math/code), normalizes against the table's column count, and
  # emits the weighted spec. Headers and short fixed-vocabulary cells
  # (single words, numbers) get extra weight floor so a single-word
  # column stays its natural width rather than being squeezed by long
  # prose elsewhere. Worth slowing down on this — touches every table
  # in the corpus, getting it wrong is visible everywhere. Discuss
  # with Joseph before implementing; the measurement heuristic in
  # particular is taste-driven (when does long-but-uniform content
  # earn a fixed-width treatment, when does it earn extra wrap room).
  #
  # Width is \segmentrulewidth (body + margin gutter + margin), matching
  # the segment header rules and the Working Notes box so tables read as
  # full-width artifacts. (The earlier xltabular attempt at this width
  # conflicted with kaobook's margin-note machinery via booktabs' internal
  # \cmrsideswitch; plain tabularx avoids that path entirely.)
  #
  # Tufte-ish styling: heavier outer rules (\toprule[1pt]/\bottomrule[1pt]),
  # thinner header separator (default \midrule), italic header row,
  # generous row spacing (\arraystretch=1.25), no vertical rules.
  #
  # \begingroup/\endgroup scopes \arraystretch and \small — wrapping in
  # `{ ... }` around \begin{xltabular} collides with xltabular's own
  # grouping (the original "Extra endgroup" cascade).
  # Figure embed. Modelled on convert_table: an in-flow (NOT floating)
  # numbered atom with \captionof{figure} + \label{fig:<slug>} so it
  # joins cleveref / the #slug cross-ref machinery, kept whole by
  # \needspace. The src is an absolute path baked by ingest's
  # resolve_figure_embeds.
  #
  # TikZ source-of-truth (Joseph's intent), via a robust mechanism:
  # \includestandalone is structurally incompatible with this pipeline
  # (it does not run the subfile preamble — where the figure's
  # \scopeclass/\rail engine lives — and needs subfiles known at
  # main-preamble time, but figures are discovered mid-body; it
  # collapsed a 637pp build to 8pp). Instead, when a sibling `.tex`
  # exists and is newer than the render cache, recompile it with
  # lualatex to `<base>.mono.pdf` (gitignored — the build never
  # mutates the committed `<base>.pdf` preview) and \includegraphics
  # that. So the `.tex` stays canonical and vector, regenerated from
  # source, without the structural break. Priority: fresh .mono.pdf →
  # committed .pdf → src .pdf/.png → .svg via cached rsvg-convert →
  # LOUD visible placeholder (never a silent gap). Full rationale:
  # msc/figure-pipeline-buildout-2026-05-18.md.
  def convert_img(el, _opts)
    src = (el.attr['src'] || '').to_s
    return '' if src.empty?
    slug    = (el.attr['id'] || '').to_s
    caption = (el.attr['caption'] || el.attr['alt'] || '').to_s
    base    = src.sub(/\.[A-Za-z0-9]+\z/, '')
    tex     = "#{base}.tex"
    cache   = "#{base}.mono.pdf"

    if File.exist?(tex) &&
       (!File.exist?(cache) || File.mtime(tex) > File.mtime(cache))
      dir = File.dirname(tex)
      job = "#{File.basename(base)}.mono"
      ok = system('lualatex', '-interaction=nonstopmode', '-halt-on-error',
                  '-output-directory', dir, '-jobname', job, tex,
                  chdir: dir, out: File::NULL, err: File::NULL)
      warn "warn: figure recompile failed for #{tex} (using fallback)" unless ok
    end

    inc =
      if File.exist?(cache)
        "\\includegraphics[width=\\linewidth]{#{cache}}"
      elsif File.exist?("#{base}.pdf")
        "\\includegraphics[width=\\linewidth]{#{base}.pdf}"
      elsif File.exist?(src) && src =~ /\.(pdf|png)\z/i
        "\\includegraphics[width=\\linewidth]{#{src}}"
      elsif File.exist?("#{base}.svg")
        svgpdf = "#{base}.svg.pdf"
        unless File.exist?(svgpdf)
          system('rsvg-convert', '-f', 'pdf', '-o', svgpdf, "#{base}.svg")
        end
        File.exist?(svgpdf) ? "\\includegraphics[width=\\linewidth]{#{svgpdf}}" : nil
      end
    if inc.nil?
      warn "warn: figure source not found for embed: #{src}"
      inc = "\\fbox{\\parbox{0.9\\linewidth}{\\centering\\ttfamily " \
            "MISSING FIGURE\\\\#{File.basename(src)}}}"
    end

    cap   = caption.empty? ? '{}' : "{#{process_prose(caption)}}"
    label = slug.empty? ? '' : "\\label{fig:#{slug}}"
    "\\par\\medskip\n" \
      "\\needspace{8\\baselineskip}\n" \
      "\\begingroup\\centering\n" \
      "#{inc}\\par\\smallskip\n" \
      "\\captionof{figure}#{cap}#{label}\\par\n" \
      "\\endgroup\n\\par\\medskip\n\n"
  end

  def convert_table(el, opts)
    aligns  = el.options[:alignment] || []
    weights = table_column_weights(el, aligns.size)
    cols    = aligns.each_with_index.map { |a, i| column_spec(a, weights[i]) }.join
    # Vocabulary (Joseph 2026-05-12): a "narrow-area" is anywhere the
    # Tufte-style wide right margin is in play — body text in plain
    # sections sits in the narrower column with the margin column free
    # to the right. A "wide-area" is anywhere the text already spans
    # the full segment band, with both page margins equal — Discussion /
    # Findings sections are wide-area via the \begin{segmentwidesection}
    # wrapper.
    #
    # Width choice:
    # - wide-area (@in_widesection): \linewidth (which equals
    #   \segmentrulewidth via the surrounding tcolorbox). Stays wide.
    # - narrow-area with content that doesn't fit body-width:
    #   \segmentrulewidth — escape into the margin column.
    # - narrow-area with content that wraps naturally at body width:
    #   \linewidth (body column).
    #
    # The escape condition (table_should_escape_narrow?) fires only
    # in narrow-area, so a wide-area table can never accidentally
    # double-escape and overshoot the page.
    table_w = if @in_widesection
                '\\linewidth'
              elsif table_should_escape_narrow?(el, aligns.size)
                '\\segmentrulewidth'
              else
                '\\linewidth'
              end
    # Table body always renders one size smaller (\footnotesize) so wider
    # tables fit; the header row gets bumped back up to \small via
    # convert_thead so it stays readable.
    @table_count += 1
    caption_text = (el.attr['caption'] || el.attr['data-caption'] || '').to_s
    caption_arg  = caption_text.empty? ? '{}' : "{#{process_prose(caption_text)}}"
    label        = segment_slug.empty? ? '' : "\\label{tbl:#{segment_slug}-#{@table_count}}"
    # Orphan/widow protection for the caption-then-table pair: reserve
    # enough space to hold caption + a few rows. \nopagebreak between
    # caption and tabularx forbids a break in that gap; if the table is
    # taller than the remaining space, the whole thing migrates to the
    # next page rather than splitting the caption from its rows.
    "\\par\\medskip\n" \
      "\\needspace{8\\baselineskip}\n" \
      "\\begingroup\n" \
      "\\renewcommand{\\arraystretch}{1.25}%\n" \
      "\\footnotesize\n" \
      "\\captionof{table}#{caption_arg}#{label}\\par\\smallskip\n" \
      "\\nopagebreak[4]\n" \
      "\\begin{tabularx}{#{table_w}}{#{cols}}\n" \
      "\\toprule[1pt]\\addlinespace[2pt]\n" \
      "#{inner(el, opts)}" \
      "\\addlinespace[2pt]\\bottomrule[1pt]\n" \
      "\\end{tabularx}\n" \
      "\\endgroup\n\\par\\medskip\n\n"
  end

  ALIGN_CMD = {
    left:    '\\raggedright',
    right:   '\\raggedleft',
    center:  '\\centering',
    default: '\\raggedright',
  }.freeze

  # Emit a tabularx X column with weight-scaled \hsize so columns can
  # vary in width by content. Weight 1.0 is "default X share"; a row of
  # weights summing to N (column count) yields the same total table
  # width as N equal Xs would. Per-column weights computed by
  # table_column_weights from avg non-blank cell length.
  def column_spec(align, weight = 1.0)
    align_cmd = ALIGN_CMD[align] || ALIGN_CMD[:default]
    ">{\\hsize=#{format('%.3f', weight)}\\hsize#{align_cmd}\\arraybackslash}X"
  end

  # Approximate rendered length for column-weight purposes. Markdown
  # source over-counts math heavily: a 4-char command like `\hat`
  # renders as one glyph; `\mathbb{R}` is 10 source chars for one
  # blackboard letter; `\frac{n}{n+\kappa}` is 18 source chars for a
  # vertically-stacked 5-char-wide fraction. Counting source chars
  # 1-to-1 against prose chars made math columns get runaway weight
  # and crushed neighboring prose columns.
  #
  # The strip pass removes:
  # - `\command` and `\letter+` sequences (collapse to single space —
  #   the command itself renders as a glyph or controls layout, not
  #   horizontal text width)
  # - braces `{` / `}` (grouping syntax; non-rendered)
  # - math/code delimiters `$` and backticks
  # - duplicate whitespace
  # The remaining char-count tracks rendered width much more closely
  # than the raw source length did.
  CMD_RE         = /\\[a-zA-Z]+\*?/
  BRACE_RE       = /[{}]/
  DELIM_RE       = /[$`]/
  WHITESPACE_RE  = /\s+/
  def cell_visual_length(text)
    s = text.to_s
    s = s.gsub(CMD_RE, ' ').gsub(BRACE_RE, '').gsub(DELIM_RE, '').gsub(WHITESPACE_RE, ' ').strip
    s.length
  end

  # Approximate body-column width in characters at footnotesize. Used
  # to decide whether a narrow-area table's content needs to escape
  # into the margin column. \textwidth ≈ 337pt, footnotesize ≈ 13 chars
  # per inch → roughly 56 chars wide. Tune by inspecting tables that
  # should/shouldn't escape.
  NARROW_AREA_CHARS = 56

  # Slack factor on the per-column budget — only escape when an atomic
  # token exceeds the per-column-budget × this factor. 1.2 = a 20%
  # cushion before the table is forced wider. Smaller value escapes
  # more aggressively; larger keeps more tables narrow.
  NARROW_AREA_ESCAPE_SLACK = 1.2

  # TODO (narrow-direction adaptation): the converse of the escape
  # logic — a wide-area table whose content would comfortably fit at
  # body width could be narrowed to match the surrounding prose
  # column. Joseph 2026-05-12 noted Table 7.2 as an example. Rare
  # enough to defer; the structural shape is the same as escape but
  # in reverse — track in_widesection, check if E(max(per-col)) is
  # well under narrow-width budget, and emit \linewidth in a
  # specialty wrapper that overrides the surrounding widesection
  # geometry. Tabularx-inside-a-non-wide-tcolorbox would be the
  # cleanest implementation; needs care so widesection's wider
  # \linewidth doesn't carry through and re-widen.

  # TODO (snap-to-content-width): when a column's normalized weight
  # is just slightly less than ONE of the actual cell widths within
  # the column (within some epsilon), snap up to that cell width to
  # avoid wrapping just a few characters. Eliminates the case where
  # a single cell wraps at "near" the column boundary and looks
  # like a layout glitch. Joseph 2026-05-12. Concretely: for each
  # column, compute the rendered cell widths under the current
  # weight; if any cell wraps to N+1 lines when an epsilon-larger
  # column would keep it at N lines, expand the column by epsilon.
  # Renormalize so total weight still equals n_cols.

  # Decide whether a narrow-area table should escape to wide-area-width.
  # The signal is the longest atomic token (math expression or inline-
  # code span) in any column — these don't wrap, so if any column has
  # an atomic token wider than the body's per-column budget, the
  # table will visibly overflow at body width and benefits from the
  # wider register. Prose-heavy tables wrap naturally and stay narrow.
  def table_should_escape_narrow?(table_el, n_cols)
    return false if n_cols.zero?
    body_per_col = NARROW_AREA_CHARS.to_f / n_cols
    threshold = body_per_col * NARROW_AREA_ESCAPE_SLACK
    collect_table_cells(table_el).each do |row|
      row.each_with_index do |cell, i|
        next if i >= n_cols
        atomic_token_lengths(cell.to_s).each do |len|
          return true if len > threshold
        end
      end
    end
    false
  end

  # Approximate chars-per-table-row at body width / footnotesize. Used
  # to convert a column's longest single word into a weight floor — the
  # column has to be wide enough to fit that word without LaTeX falling
  # back to hyphenation ("Sepa-/rated"). 60 is empirical; tune by the
  # overfull-hbox warnings.
  TYPICAL_TABLE_CHARS = 60

  # Linear weighting by average non-blank cell length per column, with
  # a per-column floor based on the longest single word in the column.
  # Headers count as cells (they too need fit-width). Math content
  # weights via cell_visual_length (math is atomic — its rendered
  # width can't be broken across lines, so we over-allocate for it).
  #
  # The word-floor pass: each column's weight is bumped to at least
  # max_word × n_cols / TYPICAL_TABLE_CHARS so a short-avg column whose
  # body contains a 9-char word like "Separated" doesn't get squeezed
  # below its natural minimum. After flooring, weights are renormalized
  # so the row still sums to n_cols (tabularx's expected distribution).
  def table_column_weights(table_el, n_cols)
    return [] if n_cols.zero?
    per_column = Array.new(n_cols) { { lens: [], max_word: 0 } }
    collect_table_cells(table_el).each do |row|
      row.each_with_index do |cell_text, idx|
        next if idx >= n_cols
        text = cell_text.to_s.strip
        next if text.empty?
        per_column[idx][:lens] << cell_visual_length(text)
        word_max = atomic_token_lengths(text).max || 0
        per_column[idx][:max_word] = word_max if word_max > per_column[idx][:max_word]
      end
    end

    avgs  = per_column.map { |c| c[:lens].empty? ? 0.0 : c[:lens].sum.to_f / c[:lens].size }
    total = avgs.sum
    initial = total.zero? ? Array.new(n_cols, 1.0) : avgs.map { |a| a / total * n_cols }

    floors  = per_column.map { |c| c[:max_word].to_f * n_cols / TYPICAL_TABLE_CHARS }
    floored = initial.zip(floors).map { |w, f| [w, f].max }
    sum     = floored.sum
    sum.zero? ? Array.new(n_cols, 1.0) : floored.map { |w| w / sum * n_cols }
  end

  # Atomic tokens for the word-floor calculation. Math spans (`$…$`) are
  # ONE token because rendered math doesn't break at internal spaces —
  # `$K_t = P_{t|t-1} H^T \cdot R^{-1}$` is a single horizontal box that
  # has to fit on one line. Earlier word-floor logic split on every
  # whitespace and saw the math as many short tokens, so the column got
  # squeezed below the math's actual width and tabularx forced it to
  # overflow. Inline-code spans (`` ` `` … `` ` ``) behave the same way
  # — atomic at typesetting time — so they get the same treatment.
  ATOMIC_TOKEN_PATTERNS = [
    /\$[^$]+\$/,           # inline math
    /`[^`]+`/,             # inline code
  ].freeze

  # Atomic tokens contribute less aggressively to the column floor
  # than prose words: a math expression overflowing its column by a
  # few characters is visually noticeable but recoverable; a prose
  # word getting forced-hyphenated ("Sepa-/rated") is uglier and less
  # repairable. The 0.6 scale lets math claim significant column
  # share without dominating short-prose-companion columns into
  # forced hyphenation. Tune by inspecting both math-heavy and
  # short-label-heavy tables.
  #
  # TODO (column-proportionality refinement): math source length over-
  # estimates rendered visual length because LaTeX commands like
  # `\hat`, `\sum`, `\mathbb` are 4+ source chars that render as a
  # single glyph. A more accurate visual-length estimator would count
  # only backslash-led commands, dots, digits, and visible letters —
  # not the bracing/scoping overhead. Sublinear weighting (sqrt of
  # length) is also worth a pass: linear over-weights very long
  # cells; sqrt would soften the long-tail influence without losing
  # the qualitative "this column has more content" signal. Discuss
  # before changing; column proportionality and total-width
  # adaptation should evolve in separate cycles per Joseph's note.
  ATOMIC_FLOOR_SCALE = 0.6

  def atomic_token_lengths(text)
    atomic = []
    remainder = text.dup
    ATOMIC_TOKEN_PATTERNS.each do |pat|
      remainder.scan(pat) do |m|
        atomic << (cell_visual_length(m) * ATOMIC_FLOOR_SCALE).round
      end
      remainder = remainder.gsub(pat, ' ')
    end
    word_lens = remainder.split(/\s+/).reject(&:empty?).map { |w| cell_visual_length(w) }
    atomic + word_lens
  end

  # Walk a :table element and return an array of rows, each an array
  # of cell text content (post-collect_text strip). Handles both the
  # :thead/:tbody-wrapped form and the flat :tr children form that
  # kramdown can produce.
  def collect_table_cells(table_el)
    rows = []
    return rows if table_el.children.nil?
    table_el.children.each do |child|
      case child.type
      when :thead, :tbody
        child.children.each { |tr| rows << row_cells(tr) }
      when :tr
        rows << row_cells(child)
      end
    end
    rows
  end

  def row_cells(tr_el)
    return [] if tr_el.children.nil?
    tr_el.children.map { |c| collect_text(c) }
  end

  # Italic header row — the Tufte register for column labels. We render
  # each header cell with \emph rather than wrapping the whole row, so
  # cell-level math/markup inside headers still parses normally. Each
  # cell is also bumped one size up (\small) from the table-default
  # \footnotesize, so headers stay readable while body content shrinks.
  def convert_thead(el, opts)
    rows = el.children.map do |tr|
      next unless tr.type == :tr

      cells = tr.children.map { |td| "{\\small\\emph{#{inner(td, opts).strip}}}" }
      "#{cells.join(' & ')} \\\\\n"
    end.compact
    "#{rows.join}\\midrule\n"
  end

  def convert_tbody(el, opts)
    inner(el, opts)
  end

  def convert_tfoot(el, opts)
    inner(el, opts)
  end

  def convert_tr(el, opts)
    cells = el.children.map { |c| send("convert_#{c.type}", c, opts).strip }
    "#{cells.join(' & ')} \\\\\n"
  end

  def convert_td(el, opts)
    inner(el, opts).strip
  end

  # ── Segment header / footer ───────────────────────────────────────────

  def segment_open(title)
    type   = @frontmatter['type'].to_s
    slug   = @frontmatter['slug'].to_s
    status = @frontmatter['status'].to_s
    stage  = @frontmatter['stage'].to_s
    label  = TYPE_LABEL[type] || type.capitalize
    # Most segments write the H1 as "Type: Title" (FORMAT-recommended human
    # form). Strip the redundant type prefix — the header macro re-emits it.
    clean = title.sub(/\A#{Regexp.escape(label)}:\s*/, '')
    # Stage glyph appears on the far right of the header strip in review
    # mode; public-variant builds suppress it by passing the empty string.
    stage_arg = @variant == :review ? stage : ''

    # Container dispatch: appendix segments are themselves chapters per the
    # four-volume hierarchy; in-part segments are sections. \label{seg:slug}
    # always lands on the line after the heading so cross-refs resolve to
    # the right counter (chapter for appendix, section for in-part).
    macro = @container == :appendices ? 'segmentappendixchapter' : 'segmenthead'

    parts = []
    parts << "\\#{macro}{#{label}}{#{escape_text(clean)}}{#{status}}{#{stage_arg}}"
    parts << "\\label{seg:#{slug}}" unless slug.empty?
    parts << ''
    parts.join("\n")
  end

  def segment_close
    "\n\\segmentfoot\n"
  end

  # ── Escapes ──────────────────────────────────────────────────────────

  # Body-text escape: passes backslash, braces, and dollar through (raw-TeX
  # passthrough policy, same as neurips/), but escapes characters commonly
  # meant literally in prose: % & _ # ~ ^.
  ESCAPE_MAP = {
    '%' => '\\%',
    '&' => '\\&',
    '_' => '\\_',
    '~' => '\\textasciitilde{}',
    '^' => '\\textasciicircum{}',
  }.freeze
  ESCAPE_RE = /[%&_~^]/

  def escape_text(str)
    # We do NOT escape `#` here because we need to find #slug cross-refs in
    # convert_text (CROSS_REF_RE). The cross-ref rewrite happens immediately
    # after this escape; any `#` that survives should be a literal and we'd
    # need a follow-up escape pass for it. For result-persistence-condition
    # there are no literal `#` outside of cross-refs, so deferring this until
    # we hit a counterexample.
    str.gsub(ESCAPE_RE, ESCAPE_MAP)
  end

  # Equation tag content gets per-segment escape, with `$...$` math spans
  # preserved verbatim — escape_text's underscore-rewrite would otherwise
  # turn `$M_t$` into `$M\_t$` and break the subscript. `#` outside math
  # is escaped (we don't look for cross-refs inside eq-tag content).
  def escape_eq_tag(str)
    parts = str.split(/(\$[^$\n]+?\$)/)
    parts.map.with_index do |part, idx|
      idx.odd? ? part : escape_text(part).gsub('#', '\\#')
    end.join
  end
end
