# frozen_string_literal: true
#
# mono/lib/segment_renderer.rb
#
# Render an AAD-formatted segment markdown file to LaTeX.
#
# Architecture follows neurips/bin/build's pattern (custom kramdown parser
# + custom converter) but is specialized for AAD's segment cadence as
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
    def render(path, variant: :public)
      raw = File.read(path)
      front, body = split_frontmatter(raw)
      body = strip_working_notes(body) if variant == :public
      body = preprocess_math_pipes(body)

      doc = Kramdown::Document.new(
        body,
        input: 'AsfSegment',
        # Pass parsed frontmatter so the converter can emit \segmenthead
        # with the right type/status/title without re-parsing.
        asf_frontmatter: front,
        asf_variant:     variant,
      )
      doc.to_asf_latex
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
# tag recognition. Both are AAD source-side idioms that kramdown wouldn't
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
    @segment_head_emitted = false
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
    body + segment_close
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
  def collect_text(el)
    return el.value.to_s if el.type == :text

    el.children.map { |c| collect_text(c) }.join
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
      .gsub(CROSS_REF_RE) { "\\cref{seg:#{Regexp.last_match(1)}}" }
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
  # Columns become `X` (equal-share wrapping), alignment-aware via the
  # array-package column-modifier prefix.
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
  def convert_table(el, opts)
    aligns = el.options[:alignment] || []
    cols   = aligns.map { |a| column_spec(a) }.join
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
      "\\begin{tabularx}{\\segmentrulewidth}{#{cols}}\n" \
      "\\toprule[1pt]\\addlinespace[2pt]\n" \
      "#{inner(el, opts)}" \
      "\\addlinespace[2pt]\\bottomrule[1pt]\n" \
      "\\end{tabularx}\n" \
      "\\endgroup\n\\par\\medskip\n\n"
  end

  COLUMN_SPEC = {
    left:    '>{\\raggedright\\arraybackslash}X',
    right:   '>{\\raggedleft\\arraybackslash}X',
    center:  '>{\\centering\\arraybackslash}X',
    default: '>{\\raggedright\\arraybackslash}X',
  }.freeze

  def column_spec(align)
    COLUMN_SPEC[align] || COLUMN_SPEC[:default]
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
    # form). Strip the redundant type prefix — \segmenthead already shows it.
    clean = title.sub(/\A#{Regexp.escape(label)}:\s*/, '')
    # Stage glyph appears on the far right of the header strip in review
    # mode; public-variant builds suppress it by passing the empty string.
    stage_arg = @variant == :review ? stage : ''

    parts = []
    parts << "\\segmenthead{#{label}}{#{escape_text(clean)}}{#{status}}{#{stage_arg}}"
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
