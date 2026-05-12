# frozen_string_literal: true
#
# common/lib/typeset.rb — Stage 3 of the markdown-first build pipeline.
#
# Reads the assembled per-volume markdown (the output of Stage 2 /
# Mono::Assemble) and emits LaTeX. Currently produces a single body.tex
# that main.tex can \input alongside the existing legacy LaTeX path —
# both code paths produce side-by-side output so the new pipeline can
# be verified against the established one before the switch.
#
# The converter is Kramdown::Converter::AsfVolumeLatex, a subclass of
# AsfLatex that adds structural-marker recognition:
#
#   ## *Preface* [Title]    →  \addchap{Title}  (volume preface)
#   ## *Part* Title         →  \part{Title}
#   ## *Appendices* Group   →  \appendix + \part{Appendices: Group} + thechapter override
#   ### *Chapter* Title     →  \chapter{Title}
#   #### Segment Title      →  \segmenthead{Type}{Title}{Status}{Stage}\label{seg:slug}
#                              (when followed by a `**Slug**: …` metadata block;
#                              segment metadata is parsed off the markdown text
#                              before kramdown sees it and attached as IAL on
#                              the header element)
#   ### Segment Title       →  \segmentappendixchapter{...}  (Container: appendix-chapter)
#
# The H1 (volume title) is suppressed — it's rendered by main.tex via
# \volumetitle from build-info.tex, and a duplicate title in body.tex
# would conflict with the cover/title-page sequence.
#
# HTML anchors <a id="slug"></a> are suppressed (the segment-header
# emission already emits \label{seg:slug}; the anchor is for HTML/
# markdown-reader use only).
#
# Resolved cross-refs of the form `[Type Label](#slug)` — produced by
# Stage 2's resolver — render through \cref{seg:slug} with the existing
# crefformat (bare number). Author-typed "Type" prefix in source prose
# survives unchanged ("see Definition #foo" → "see Definition 1.4"
# after both stages, no doubling).

require 'kramdown'
require_relative 'segment_renderer'

module Mono
  module Typeset
    module_function

    # Top-level entry. Takes the assembled markdown text and returns
    # the LaTeX body. Caller writes it to the build stage's body.tex.
    def typeset(markdown_text, variant: :review)
      text = preprocess_metadata_blocks(markdown_text)
      doc = Kramdown::Document.new(
        text,
        input: 'AsfSegment',
        asf_variant: variant,
        asf_mode:    :volume,
      )
      doc.to_asf_volume_latex
    end

    # Walk the assembled markdown and transform each segment-header
    # metadata block into a kramdown IAL (inline attribute list)
    # attached to the preceding header. This lets the converter see
    # segment metadata as element attributes on the heading element
    # instead of having to look ahead in the AST.
    #
    # Input:
    #   #### Definition: Agent-Environment Coupling
    #
    #   **Slug**: `def-agent-environment`
    #   **Type**: Definition
    #   **Status**: exact
    #   **Stage**: deps-verified
    #   **Label**: 1.1
    #   **Container**: section
    #
    #   [body]
    #
    # Output:
    #   #### Definition: Agent-Environment Coupling
    #   {: .segment slug="def-agent-environment" type="Definition" status="exact" stage="deps-verified" label="1.1" container="section"}
    #
    #   [body]
    def preprocess_metadata_blocks(text)
      lines = text.split("\n", -1)
      out = []
      i = 0
      while i < lines.size
        line = lines[i]
        # Detect a header followed by a metadata block. Acceptable heading
        # levels for segment-style metadata are H3 (appendix segment) and
        # H4 (in-part segment); we let any header carry metadata so the
        # convention is robust to volume-structure tweaks.
        if line.match?(/\A\#{3,6}\s+\S/) && metadata_block_starts_at?(lines, i + 1)
          out << line
          meta, after_idx = parse_metadata_block(lines, i + 1)
          out << render_ial(meta)
          i = after_idx
          next
        end
        out << line
        i += 1
      end
      out.join("\n")
    end

    # Metadata block: optional blank line, then one or more lines of
    # `**Key**: value`, then a blank line.
    def metadata_block_starts_at?(lines, idx)
      # Skip leading blank line(s)
      idx += 1 while idx < lines.size && lines[idx].strip.empty?
      return false if idx >= lines.size
      lines[idx].match?(/\A\*\*[A-Z][A-Za-z]*\*\*:\s/)
    end

    # Returns [metadata_hash, index-after-block].
    def parse_metadata_block(lines, idx)
      idx += 1 while idx < lines.size && lines[idx].strip.empty?
      meta = {}
      while idx < lines.size && (m = lines[idx].match(/\A\*\*([A-Z][A-Za-z]*)\*\*:\s*(.*)$/))
        meta[m[1].downcase] = m[2].strip.sub(/\A`(.*)`\z/, '\1')
        idx += 1
      end
      # Consume trailing blank line so the IAL we emit fully replaces
      # the metadata block in the markdown stream.
      idx += 1 if idx < lines.size && lines[idx].strip.empty?
      [meta, idx]
    end

    # Render a metadata hash as a kramdown IAL string.
    def render_ial(meta)
      attrs = meta.map { |k, v| "#{k}=#{v.inspect}" }.join(' ')
      "{: .segment #{attrs}}"
    end
  end
end

# ──────────────────────────────────────────────────────────────────────────
# Converter — assembled volume markdown → LaTeX. Subclasses AsfLatex to
# inherit math, callouts, eq-tag, list, table, and prose handling. Overrides
# the header / link / HTML conversion paths for the volume-context rules.
# ──────────────────────────────────────────────────────────────────────────

class Kramdown::Converter::AsfVolumeLatex < Kramdown::Converter::AsfLatex
  # Kramdown's `to_<format>` dispatch routes `to_asf_volume_latex` to
  # this class via Kramdown::Document#to_(snake_case_format). The base
  # class's initialize already accepts asf_mode; volume mode tells the
  # converter to use this class's structural-header dispatch.

  TYPE_LABEL_REVERSE = Mono::SegmentRenderer.const_defined?(:TYPE_LABEL) ? Mono::SegmentRenderer::TYPE_LABEL.invert : {}

  def convert_root(el, opts)
    # No segment chrome at root (no segment_open / segment_close).
    body = inner(el, opts)
    body += flush_pending_eqtag
    body
  end

  # Volume-mode header dispatch:
  #
  #   level 1                → suppress (volume title, rendered by main.tex)
  #   level 2 *Preface* X    → \addchap{X}
  #   level 2 *Part* X       → \part{X}
  #   level 2 *Appendices* X → first appendix part: emit \appendix etc.;
  #                              then \part{Appendices: X}
  #   level 3 *Chapter* X    → \chapter{X}
  #   level 3 *Preface*      → no LaTeX; part-preface content flows after
  #   level 3 with .segment  → \segmentappendixchapter{Type}{Title}{...}
  #   level 4 with .segment  → \segmenthead{Type}{Title}{...}
  #   level 5 / 6            → \segmentsubhead{title}  (segment internal)
  def convert_header(el, opts)
    level = el.options[:level]
    case level
    when 1 then ''                                # suppress volume title
    when 2 then handle_h2(el, opts)
    when 3 then handle_h3(el, opts)
    when 4 then handle_h4_segment(el, opts)
    else        handle_subhead(inner(el, opts).strip)
    end
  end

  private

  # ── Role-prefix detection (AST-based) ───────────────────────────────
  #
  # `## *Preface*`, `## *Part* Title`, `### *Chapter* Title`, etc. — the
  # role marker is the first child of the heading element, an :em node
  # whose text is a single capitalized word. Everything after that em
  # element is the title (rendered through the normal converter path).
  ROLE_WORD_RE = /\A[A-Z][A-Za-z]+\z/

  def role_marker(el)
    return nil if el.children.nil? || el.children.empty?
    first = el.children.first
    return nil unless first.type == :em
    text = collect_text(first).strip
    text.match?(ROLE_WORD_RE) ? text : nil
  end

  # Render the heading's children, skipping the leading role-marker :em
  # if present. Includes leading-space normalization so `## *Part* Title`
  # produces "Title" not " Title".
  def heading_title_after_role(el, opts)
    children = el.children[1..] || []
    rendered = children.map { |c| send("convert_#{c.type}", c, opts) }.join
    rendered.strip
  end

  # ── H2 dispatch ─────────────────────────────────────────────────────

  def handle_h2(el, opts)
    role = role_marker(el)
    case role
    when 'Preface'
      info = heading_title_after_role(el, opts)
      info.empty? ? "\\addchap{Preface}\n\n" : "\\addchap{#{info}}\n\n"
    when 'Appendices'
      out = +''
      out << mainmatter_marker
      unless @appendix_emitted
        out << "\\appendix\n"
        out << "\\renewcommand{\\thechapter}{\\AlphAlph{\\value{chapter}}}\n"
        out << "\\asfAppendixToCremap\n"
        @appendix_emitted = true
      end
      out << "\\part{Appendices: #{heading_title_after_role(el, opts)}}\n\n"
      out
    when 'Part'
      "#{mainmatter_marker}\\part{#{heading_title_after_role(el, opts)}}\n\n"
    else
      # No role marker — render as regular section subhead. (Shouldn't
      # happen in a well-formed assembled markdown but we tolerate it.)
      handle_subhead(inner(el, opts).strip)
    end
  end

  # Emit `\mainmatter\setchapterstyle{kao}` exactly once, on the first
  # transition from preface scope to main matter. The volume preface
  # (\addchap from `## *Preface*`) sits in \frontmatter scope from
  # main.tex; the first \part or first \appendices group flips us into
  # \mainmatter. After this, subsequent parts/appendices don't repeat
  # the switch.
  def mainmatter_marker
    return '' if @mainmatter_emitted
    @mainmatter_emitted = true
    "\\mainmatter\n\\setchapterstyle{kao}\n\n"
  end

  # ── H3 dispatch ─────────────────────────────────────────────────────

  def handle_h3(el, opts)
    role = role_marker(el)
    case role
    when 'Chapter'
      "\\chapter{#{heading_title_after_role(el, opts)}}\n\n"
    when 'Preface'
      ''  # part-level preface marker — prose flows after
    else
      # No role marker; might be an appendix-segment header
      if el.attr['class']&.include?('segment')
        title = inner(el, opts).strip
        emit_segment_header(el, title, level: :appendix)
      else
        handle_subhead(inner(el, opts).strip)
      end
    end
  end

  # ── H4 dispatch ─────────────────────────────────────────────────────

  def handle_h4_segment(el, opts)
    title = inner(el, opts).strip
    if el.attr['class']&.include?('segment')
      emit_segment_header(el, title, level: :section)
    else
      handle_subhead(title)
    end
  end

  def emit_segment_header(el, title, level:)
    a = el.attr
    type_label = a['type'].to_s
    slug   = a['slug'].to_s
    status = a['status'].to_s
    stage  = @variant == :review ? a['stage'].to_s : ''

    # Strip the redundant "Type: " prefix from the heading text — \segmenthead
    # already renders the type-label as part of its chrome.
    clean_title = title.sub(/\A#{Regexp.escape(type_label)}:\s*/, '')

    macro = level == :appendix ? 'segmentappendixchapter' : 'segmenthead'
    out = +"\\#{macro}{#{escape_arg(type_label)}}{#{escape_arg(clean_title)}}{#{status}}{#{stage}}\n"
    out << "\\label{seg:#{slug}}\n" unless slug.empty?
    out << "\n"
    out
  end

  # ── Subhead (segment-internal H5 / H4 / etc.) ───────────────────────

  def handle_subhead(title)
    if WIDE_SECTION_TITLES.include?(title)
      @in_widesection = true
      "\\segmentsubhead{#{title}}\n\n\\begin{segmentwidesection}\n"
    else
      "\\segmentsubhead{#{title}}\n\n"
    end
  end

  # ── Role-prefix extraction ──────────────────────────────────────────

  ROLE_ITALIC_RE = /\A\*([A-Z][A-Za-z]+)\*\s*(.*)\z/

  def role_prefix(text)
    m = text.match(ROLE_ITALIC_RE)
    m ? [m[1], m[2].to_s.strip] : [nil, text]
  end

  # ── Link conversion — handle resolved cross-refs ────────────────────

  # `[Type Label](#slug)` from Stage 2's resolver — emit \cref{seg:slug}
  # so the bare-number rendering (via crefformat) lands in the PDF. This
  # preserves the established author convention: prose says "see Definition
  # #foo" → "see Definition 1.4" with the number alone from \cref. The
  # resolver's "Type" prefix in the link's visible text is informational
  # for the markdown reader; LaTeX renders only the number.
  def convert_a(el, opts)
    href = el.attr['href'].to_s
    if href.start_with?('#') && href[1..].match?(/\A[a-z][a-z0-9-]*[a-z0-9]\z/) && segment_slug?(href[1..])
      "\\cref{seg:#{href[1..]}}"
    else
      super
    end
  end

  # ── HTML anchor suppression ────────────────────────────────────────

  # The assembled markdown has <a id="slug"></a> before each segment
  # header for HTML/markdown-reader use. In LaTeX the \label inside
  # \segmenthead serves the same purpose, so suppress the HTML anchor.
  def convert_html_element(el, opts)
    if el.value == 'a' && el.attr['id'] && el.children.empty?
      ''
    else
      super
    end
  end

  # ── Helpers ─────────────────────────────────────────────────────────

  def segment_slug?(slug)
    # Conservative: any slug we've seen as a label/anchor target qualifies.
    # The cross-ref pattern's regex already filters to slug-shaped strings.
    @known_segment_slugs ||= {}
    @known_segment_slugs[slug] = true
  end

  def escape_arg(text)
    # Minimal LaTeX escape for macro arguments — same set the existing
    # build-monograph escape_latex covers. Backslash is preserved as
    # backslash because segment-header titles can carry math.
    text.to_s
        .gsub('&', '\\\\&')
        .gsub('%', '\\\\%')
        .gsub('#', '\\\\#')
        .gsub('_', '\\\\_')
        .gsub('~', '\\\\textasciitilde{}')
        .gsub('^', '\\\\textasciicircum{}')
  end
end

# Wire kramdown's `to_<format>` dispatch for the new converter.
module Kramdown::Document::ToAsfVolumeLatex
  def to_asf_volume_latex
    Kramdown::Converter::AsfVolumeLatex.convert(@root, @options).first
  end
end

Kramdown::Document.include(Kramdown::Document::ToAsfVolumeLatex)
