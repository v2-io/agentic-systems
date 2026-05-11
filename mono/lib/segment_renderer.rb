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
  end

  # ── Element converters ────────────────────────────────────────────────

  def convert_root(el, opts)
    inner(el, opts) + segment_close
  end

  # First header in the document is the segment title; subsequent headers
  # are section subheads inside the segment.
  def convert_header(el, opts)
    title = inner(el, opts).strip
    if !@segment_head_emitted
      @segment_head_emitted = true
      segment_open(title)
    else
      case el.options[:level]
      when 2
        "\\segmentsubhead{#{title}}\n\n"
      when 3
        # H3 inside a segment — kept lighter than H2 subheads
        "\\par\\medskip\\noindent\\textbf{#{title}.}\\quad "
      else
        "\\par\\noindent\\textit{#{title}.}\\quad "
      end
    end
  end

  def convert_eq_tag(el, _opts)
    "\\eqtag{#{escape_eq_tag(el.value)}}\n"
  end

  # Paragraphs — rewrite #slug cross-refs as we emit text.
  def convert_p(el, opts)
    rewritten = inner(el, opts)
    "#{rewritten}\n\n"
  end

  # Text nodes — escape LaTeX specials AND rewrite cross-refs in one pass.
  # Cross-refs come in as `#slug` literal text; rewrite to \cref{seg:slug}
  # after escaping, so the cref command isn't itself escaped. Any `#` left
  # after the cross-ref pass is a literal in prose and gets escaped to \#.
  def convert_text(el, _opts)
    escaped = escape_text(el.value)
    escaped
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
      "\\begin{equation*}\n#{value}\n\\end{equation*}\n"
    else
      "$#{value}$"
    end
  end

  # Raw passthrough for HTML elements we don't render (e.g., comments).
  def convert_html_element(_el, _opts) = ''
  def convert_xml_comment(_el, _opts)  = ''
  def convert_blank(_el, _opts)        = "\n"

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

    parts = []
    parts << "\\segmenthead{#{label}}{#{escape_text(clean)}}{#{status}}"
    parts << "\\label{seg:#{slug}}" unless slug.empty?
    # In review mode, surface the stage frontmatter as marginalia so
    # reviewers see the promotion state alongside the segment itself.
    if @variant == :review && !stage.empty?
      parts << "\\segmentstage{#{stage}}"
    end
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

  # Equation tag content (between brackets) gets the same escape, with `#`
  # escaped explicitly since we don't need to find cross-refs inside it.
  def escape_eq_tag(str)
    escape_text(str).gsub('#', '\\#')
  end
end
