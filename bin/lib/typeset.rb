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
    # TODO: the chunk-format contract is now expressed in TWO places — the
    # bolded-key emission in ingest.rb (build_segment_chunk / build_preface_chunk)
    # and the regex-driven parse here. They have to move together when a key
    # is added or its rendering changes. Consider extracting the contract
    # into a small module (Mono::ChunkFormat) with emit + parse functions so
    # the coupling is mechanical rather than convention-based.
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
#
# TODO: revisit the AsfLatex inheritance. Most shared behavior is utility
# (math handling, eq-tags, callouts, lists, tables, prose escaping) — a
# Mono::KramdownHelpers module that both AsfLatex and AsfVolumeLatex
# `include` would be a flatter, more honest design. Inheritance currently
# pulls along segment-mode state (@segment_head_emitted, @in_epigraph)
# that's redundant when convert_header is fully overridden in volume mode.
# Refactor when the volume-mode converter grows enough to feel coupled to
# parent-class implementation details rather than to shared behavior.

class Kramdown::Converter::AsfVolumeLatex < Kramdown::Converter::AsfLatex
  # Kramdown's `to_<format>` dispatch routes `to_asf_volume_latex` to
  # this class via Kramdown::Document#to_(snake_case_format). The base
  # class's initialize already accepts asf_mode; volume mode tells the
  # converter to use this class's structural-header dispatch.

  TYPE_LABEL_REVERSE = Mono::SegmentRenderer.const_defined?(:TYPE_LABEL) ? Mono::SegmentRenderer::TYPE_LABEL.invert : {}

  def convert_root(el, opts)
    # No segment chrome at root (no segment_open / segment_close). But any
    # wrappers (epigraph / widesection / workingnotes) that the last
    # segment left open need to close at end-of-document so the LaTeX is
    # well-formed.
    body = inner(el, opts)
    body += close_open_wrappers
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
    when 4 then handle_h4(el, opts)
    else        handle_subhead_with_state(inner(el, opts).strip, level: level)
    end
  end

  # ── Segment-internal state machine (epigraph / widesection / workingnotes) ──
  #
  # Segment-internal subheads come from a segment's authored H2:
  #   - "Formal Expression", "Epistemic Status" → regular subhead
  #   - "Discussion", "Findings" → subhead + full-width wrapper
  #   - "Working Notes" → opens the workingnotes env (review variant only;
  #     :public ingest strips Working Notes upstream)
  #
  # In the assembled markdown the segment's authored H2 lands at H5
  # (main-matter) or H4 (appendix). When we cross any of these
  # subheads, OR a new segment header, OR a structural H2/H3, we
  # close any wrappers still open from the previous segment's section.
  # The first paragraph after a segment header opens a segmentepigraph
  # (the summary block); the first subhead inside the segment closes it.

  # Close any open wrappers whose level-of-origin is at or shallower than
  # `current_level`. A nil current_level (end of document, or a brand-new
  # segment header) closes every open wrapper unconditionally.
  #
  # The level discipline mirrors the segment-mode parent's `level <= 2`
  # guard: a wrapper opened by a section-grade subhead (H5 main-matter,
  # H4 appendix) survives nested H6/H5 subheads inside it. Working Notes
  # in particular has H3 children (Open question / Strengthening attempt
  # / …) that get bumped to H6 in main-matter context; those must not
  # close the workingnotes wrapper.
  def close_open_wrappers(current_level: nil)
    prefix = +''
    prefix << flush_pending_eqtag
    if @in_epigraph
      # Epigraph always closes on any new header — it's strictly the
      # "summary right after the segment header" zone.
      prefix << "\\end{segmentepigraph}\n\n"
      @in_epigraph = false
    end
    if @in_widesection && (current_level.nil? || current_level <= @widesection_level)
      prefix << "\\end{segmentwidesection}\n\n"
      @in_widesection = false
    end
    if @in_working_notes && (current_level.nil? || current_level <= @workingnotes_level)
      prefix << "\\end{workingnotes}\n\n"
      @in_working_notes = false
    end
    prefix
  end

  # Dispatch a segment-internal subhead by level *relative to the
  # segment header*. The segment header's authored H1 maps to "level
  # 0" in the segment's internal hierarchy; H2s (Formal Expression,
  # Epistemic Status, Discussion, Findings, Working Notes) → relative
  # 1; H3s (named sub-discussions inside a section like "Strong
  # Monotonicity as the Hinge…") → relative 2; H4+ → relative 3.
  #
  # This mirrors the legacy segment_renderer (per-segment :segment
  # mode) which dispatched: H2 → \segmentsubhead, H3 → bold inline
  # leader, H4+ → italic inline leader. Before this fix, the typeset
  # path was emitting \segmentsubhead for every segment-internal
  # header level, causing long H3 leaders to render as full-width
  # right-aligned labels that overflowed the page.
  def handle_subhead_with_state(title, level: 5)
    # Chapter-intro Discussion mode: all internal subheads suppressed
    # so the segment body flows as continuous chapter prose. The named
    # H2s (Formal Expression, Epistemic Status, Discussion) become
    # invisible paragraph breaks; the prose under each still renders.
    return "\\par\\medskip\n" if @suppress_segment_chrome

    prefix    = close_open_wrappers(current_level: level)
    relative  = @current_segment_header_level ? (level - @current_segment_header_level) : 1
    case relative
    when 1
      # Segment-source H2 — subhead, with optional wide-section /
      # workingnotes wrappers.
      if title == 'Working Notes'
        @in_working_notes  = true
        @workingnotes_level = level
        "#{prefix}\\begin{workingnotes}\n"
      elsif WIDE_SECTION_TITLES.include?(title)
        @in_widesection    = true
        @widesection_level = level
        "#{prefix}\\segmentsubhead{#{title}}\n\n\\begin{segmentwidesection}\n"
      elsif @in_working_notes
        "#{prefix}\\workingnotessubhead{#{title}}\n\n"
      else
        "#{prefix}\\segmentsubhead{#{title}}\n\n"
      end
    when 2
      # Segment-source H3 — bold inline leader. Reads as the start of
      # a paragraph, not a section break. Same orphan discipline as
      # the H2 subhead but less greedy on reserved vertical space.
      "#{prefix}\\needspace{3\\baselineskip}" \
        "\\par\\medskip\\noindent\\textbf{#{title}.}\\quad "
    else
      # Segment-source H4+ — italic inline leader. Even quieter than
      # the H3 leader; same paragraph-start treatment.
      "#{prefix}\\par\\noindent\\textit{#{title}.}\\quad "
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
    prefix = close_open_wrappers(current_level: 2)
    case role
    when 'Preface', 'Introduction'
      info = heading_title_after_role(el, opts)
      "#{prefix}" + (info.empty? ? "\\addchap{#{role}}\n\n" : "\\addchap{#{info}}\n\n")
    when 'Appendices'
      out = +prefix
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
      "#{prefix}#{mainmatter_marker}\\part{#{heading_title_after_role(el, opts)}}\n\n"
    else
      # No role marker — defensive fallback
      "#{prefix}\\segmentsubhead{#{inner(el, opts).strip}}\n\n"
    end
  end

  # Emit `\mainmatter\setchapterstyle{kao}` exactly once, on the first
  # transition from preface scope to main matter. The volume preface
  # (\addchap from `## *Preface*`) sits in \frontmatter scope from
  # main.tex; the first \part or first \appendices group flips us into
  # \mainmatter. After this, subsequent parts/appendices don't repeat
  # the switch.
  #
  # \asfChapterFormat customizes the kao chapter glyph (small italic
  # "Chapter"/"Appendix" word above the scaled number, no autodot) and
  # has to be emitted AFTER \setchapterstyle{kao} because kao's style
  # command overwrites \chapterformat itself.
  def mainmatter_marker
    return '' if @mainmatter_emitted
    @mainmatter_emitted = true
    "\\mainmatter\n\\setchapterstyle{kao}\n\\asfChapterFormat\n\n"
  end

  # ── H3 dispatch ─────────────────────────────────────────────────────

  def handle_h3(el, opts)
    role = role_marker(el)
    case role
    when 'Chapter'
      @just_chaptered = true
      "#{close_open_wrappers(current_level: 3)}\\chapter{#{heading_title_after_role(el, opts)}}\n\n"
    when 'Preface', 'Introduction'
      close_open_wrappers(current_level: 3)   # part-level preface/introduction — prose flows after
    else
      # No role marker; might be an appendix-segment header (with .segment
      # IAL) — in-part appendix segments are H3 because they're chapter-
      # level entities.
      if el.attr['class']&.include?('segment')
        emit_segment_header(el, opts, level: :appendix)
      else
        handle_subhead_with_state(inner(el, opts).strip, level: 3)
      end
    end
  end

  # ── H4 dispatch ─────────────────────────────────────────────────────

  # H4 can be EITHER an in-part segment header (with .segment IAL) OR a
  # subhead within an appendix segment (whose H1 was bumped to H3, so
  # the segment's authored H2 lands at H4). Disambiguate by IAL.
  def handle_h4(el, opts)
    if el.attr['class']&.include?('segment')
      emit_segment_header(el, opts, level: :section)
    else
      handle_subhead_with_state(inner(el, opts).strip, level: 4)
    end
  end

  # Emit the segment-header LaTeX + open the segmentepigraph for the
  # summary paragraph that follows. Closes any open wrappers from the
  # previous segment first.
  #
  # Special case (chapter-intro mode): when this is the FIRST segment
  # immediately following a `\chapter{...}` AND its type is
  # `discussion`, all segment chrome is suppressed — no \segmenthead,
  # no epigraph wrapper, no subhead labels for the segment's internal
  # H2s. The body content flows as plain chapter prose, treating the
  # Discussion segment as the chapter's introduction. The \label
  # survives so cross-refs to the segment's slug still resolve. The
  # @suppress_segment_chrome flag carries through until the next
  # segment header arrives (which clears it).
  def emit_segment_header(el, opts, level:)
    a = el.attr
    type_label = a['type'].to_s
    slug   = a['slug'].to_s
    status = a['status'].to_s
    stage  = @variant == :review ? a['stage'].to_s : ''
    title  = inner(el, opts).strip

    # Strip the redundant "Type: " prefix from the heading text — \segmenthead
    # already renders the type-label as part of its chrome.
    clean_title = title.sub(/\A#{Regexp.escape(type_label)}:\s*/, '')

    # Track the segment-header's absolute level so handle_subhead_with_state
    # can compute the segment-relative depth (subheads = +1, sub-subheads
    # = +2, etc.) and dispatch to the right LaTeX subhead form.
    @current_segment_header_level = (level == :appendix ? 3 : 4)

    # Chapter-intro Discussion: emit just the label (for cross-refs)
    # and let the segment body render as plain chapter prose.
    if @just_chaptered && type_label.downcase == 'discussion'
      @suppress_segment_chrome = true
      @just_chaptered = false
      prefix = close_open_wrappers
      out = +prefix
      out << "\\label{seg:#{slug}}\n\n" unless slug.empty?
      return out
    end

    @suppress_segment_chrome = false
    @just_chaptered = false

    macro = level == :appendix ? 'segmentappendixchapter' : 'segmenthead'
    # New segment header closes ALL open wrappers regardless of level —
    # we're entering a fresh segment, anything from the previous one
    # must terminate.
    prefix = close_open_wrappers
    # type_label / clean_title are already-rendered LaTeX (from kramdown's
    # inner(el, opts) for the title; from el.attr for the metadata block).
    # Don't double-escape — pass through verbatim.
    out = +"#{prefix}\\#{macro}{#{type_label}}{#{clean_title}}{#{status}}{#{stage}}\n"
    out << "\\label{seg:#{slug}}\n" unless slug.empty?
    out << "\\begin{segmentepigraph}\n"
    @in_epigraph = true
    out
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
