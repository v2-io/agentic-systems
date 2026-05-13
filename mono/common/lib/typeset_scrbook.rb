# frozen_string_literal: true
#
# common/lib/typeset_scrbook.rb — Stage 3 (vanilla scrbook variant) of the
# markdown-first build pipeline.
#
# Reads the assembled per-volume markdown (the output of Stage 2 /
# Mono::Assemble) and emits a single body.tex suitable for LuaLaTeX
# compilation against common-scrbook/main.tex (KOMA-Script scrbook). The
# output target is a classical math monograph: single column, vanilla
# section / chapter / part hierarchy, no Tufte margin chrome, no kao
# styling. It's the same source content rendered in a different
# typographic register.
#
# The converter is Kramdown::Converter::AsfScrbookLatex, a subclass of
# AsfLatex that overrides volume-mode header dispatch to emit:
#
#   ## *Preface* [Title]    →  \addchap{Title}     (volume preface)
#   ## *Part* Title         →  \mainmatter \part{Title}
#   ## *Appendices* Group   →  \mainmatter \appendix \part{Appendices: Group}
#   ### *Chapter* Title     →  \chapter{Title}
#   #### Segment Title      →  \segmenthead{Type}{Title}{}{}\label{seg:slug}
#                              (when followed by a `**Slug**: …` metadata block;
#                              same IAL preprocessing as the kaobook converter)
#   ### Segment Title       →  \segmentappendixchapter{...}  (Container: appendix-chapter)
#   ##### Field             →  \segmentfield{Field} or \begin{workingnotes}
#                              (small italic-bold paragraph leader, NOT a
#                              numbered subsection — segment fields are
#                              labels, not citable structural divisions)
#
# Status and stage frontmatter are accepted by the macros but rendered as
# no-ops in this target — scrbook's promise is "the legible read," and
# epistemic-discipline metadata stays in the source markdown for anyone
# who wants it.
#
# Eq-tags (`*[Definition (name)]*`) render as small italic standalone
# leaders before their associated equation rather than as margin notes
# (the kaobook target uses \marginnote; scrbook has no Tufte margin).
# Same Ruby dispatch path; different LaTeX macro definition in
# common-scrbook/preamble/segment.tex.
#
# Working Notes (in --review) render as a workingnotes environment defined
# in common-scrbook/preamble/environments.tex (mdframed with thin top/
# bottom rules; \small body in a muted gray-brown). Stage-1 ingest already
# strips Working Notes for --public, so no LaTeX-side conditional is needed.

require 'kramdown'
require_relative 'segment_renderer'
require_relative 'typeset'  # for Mono::Typeset.preprocess_metadata_blocks

module Mono
  module TypesetScrbook
    module_function

    # Top-level entry. Takes the assembled markdown text and returns the
    # LaTeX body. Caller writes it to the build stage's body.tex.
    def typeset(markdown_text, variant: :review)
      # Chunk-format metadata-block parsing is identical to the kaobook
      # target — segments use the same `**Slug**: …` block on every header
      # — so reuse the kaobook converter's preprocessor verbatim. If the
      # contract ever diverges, factor preprocess_metadata_blocks into a
      # shared Mono::ChunkFormat module.
      text = Mono::Typeset.preprocess_metadata_blocks(markdown_text)
      known_slugs = scan_known_slugs(text)
      doc = Kramdown::Document.new(
        text,
        input: 'AsfSegment',
        asf_variant:     variant,
        asf_mode:        :volume,
        asf_known_slugs: known_slugs,
      )
      latex = doc.to_asf_scrbook_latex
      postprocess_latex(latex, known_slugs)
    end

    # Slugs we'll emit \label{seg:<slug>} for in this volume — extracted
    # from the per-chunk metadata block. Anything cross-referenced that
    # ISN'T in this set is a sibling-volume reference (xr-hyper machinery
    # is the proper fix; for now we render a textual fallback so the
    # reader sees the slug rather than `??`).
    def scan_known_slugs(text)
      slugs = {}
      text.each_line do |line|
        m = line.match(/\A\*\*Slug\*\*:\s*`?([a-z][a-z0-9-]*[a-z0-9])`?\s*\z/)
        slugs[m[1]] = true if m
      end
      slugs
    end

    # Post-pass on the assembled LaTeX body. Two cleanups:
    #
    # (1) Sibling-volume cross-refs. Any \cref{seg:<slug>} where <slug>
    #     isn't a known label in this volume becomes \externalref{<slug>}
    #     (defined in segment.tex as a small inline marker). This replaces
    #     the LaTeX `??` with something legible.
    #
    # (2) Spurious space inside parens before \cref. Source convention
    #     `( #foo)` and `( [Type N](#foo))` both leave a literal space
    #     between `(` (or `[`) and the rendered \cref{...}. The kaobook
    #     converter's process_prose handles the bare-cross-ref form
    #     (because the whole paragraph traverses convert_text); the
    #     markdown-link form bypasses it. Single regex catches both.
    def postprocess_latex(latex, known_slugs)
      latex.gsub(/\\cref\{seg:([a-z][a-z0-9-]*[a-z0-9])\}/) do |match|
        slug = Regexp.last_match(1)
        known_slugs.key?(slug) ? match : "\\externalref{#{slug}}"
      end
       .gsub(/([(\[])\s+(\\cref\{|\\externalref\{)/) { "#{Regexp.last_match(1)}#{Regexp.last_match(2)}" }
    end
  end
end

# ──────────────────────────────────────────────────────────────────────────
# Converter — assembled volume markdown → vanilla scrbook LaTeX. Subclasses
# AsfLatex to inherit math, callouts, eq-tag dispatch, prose escaping,
# cross-ref resolution, lists, and tables. Overrides the structural
# header / link / HTML-anchor paths for the volume-context rules of the
# scrbook target.
# ──────────────────────────────────────────────────────────────────────────

class Kramdown::Converter::AsfScrbookLatex < Kramdown::Converter::AsfLatex
  # Kramdown's `to_<format>` dispatch routes `to_asf_scrbook_latex` to
  # this class via Kramdown::Document#to_(snake_case_format).

  def initialize(root, options)
    super
    @mainmatter_emitted    = false
    @appendix_emitted      = false
    @in_working_notes      = false
    @workingnotes_level    = nil
    @current_segment_header_level = nil
    @just_chaptered        = false
    @suppress_segment_chrome = false
  end

  # No segment chrome at root in volume mode — but if any wrappers (working
  # notes, in particular) are still open at end-of-document, close them so
  # the LaTeX is well-formed.
  def convert_root(el, opts)
    body = inner(el, opts)
    body += close_open_wrappers
    body
  end

  # Volume-mode header dispatch:
  #
  #   level 1                → suppress (volume title, rendered by main.tex via \maketitle)
  #   level 2 *Preface* X    → \addchap{X}
  #   level 2 *Part* X       → \mainmatter \part{X} (first \part flips to mainmatter)
  #   level 2 *Appendices* X → first appendix part: emit \appendix; then \part{Appendices: X}
  #   level 3 *Chapter* X    → \chapter{X}
  #   level 3 *Preface*      → no LaTeX; part-preface content flows after
  #   level 3 with .segment  → \segmentappendixchapter{...}
  #   level 4 with .segment  → \segmenthead{...}
  #   level 5+               → \segmentfield / workingnotes / inline leader
  def convert_header(el, opts)
    level = el.options[:level]
    case level
    when 1 then ''
    when 2 then handle_h2(el, opts)
    when 3 then handle_h3(el, opts)
    when 4 then handle_h4(el, opts)
    else        handle_subhead(inner(el, opts).strip, level: level)
    end
  end

  # ── Cross-ref resolution ────────────────────────────────────────────
  #
  # `[Type Label](#slug)` from Stage 2's resolver — emit \cref{seg:slug}
  # so cleveref's bare-number rendering (configured in
  # common-scrbook/preamble/setup.tex) lands in the PDF. The author
  # convention "see Definition #foo" → "see Definition 1.4" survives
  # unchanged: the visible "Type" prefix in the markdown link text is
  # informational for the markdown reader; LaTeX renders the number alone.
  def convert_a(el, opts)
    href = el.attr['href'].to_s
    if href.start_with?('#') && href[1..].match?(/\A[a-z][a-z0-9-]*[a-z0-9]\z/) && segment_slug?(href[1..])
      "\\cref{seg:#{href[1..]}}"
    else
      super
    end
  end

  # ── HTML anchor suppression ────────────────────────────────────────
  #
  # The assembled markdown emits <a id="slug"></a> before each segment
  # header for HTML / markdown-reader use. In LaTeX the \label inside
  # \segmenthead serves the same purpose, so suppress the HTML anchor.
  def convert_html_element(el, opts)
    if el.value == 'a' && el.attr['id'] && el.children.empty?
      ''
    else
      super
    end
  end

  # ──────────────────────────────────────────────────────────────────────
  # Wrapper-state machine
  # ──────────────────────────────────────────────────────────────────────

  # Close any open wrappers whose level-of-origin is at or shallower than
  # current_level. nil current_level (end of document, or a brand-new
  # segment header) closes everything unconditionally.
  #
  # Single wrapper to manage in scrbook: workingnotes. (Kaobook also has
  # segmentepigraph and segmentwidesection; both collapse in single-column.)
  def close_open_wrappers(current_level: nil)
    prefix = +''
    prefix << flush_pending_eqtag
    if @in_working_notes && (current_level.nil? || current_level <= @workingnotes_level)
      prefix << "\\end{workingnotes}\n\n"
      @in_working_notes = false
    end
    prefix
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
    when 'Preface'
      info = heading_title_after_role(el, opts)
      "#{prefix}" + (info.empty? ? "\\addchap{Preface}\n\n" : "\\addchap{#{info}}\n\n")
    when 'Appendices'
      out = +prefix
      out << mainmatter_marker
      unless @appendix_emitted
        out << "\\appendix\n"
        @appendix_emitted = true
      end
      out << "\\part{Appendices: #{heading_title_after_role(el, opts)}}\n\n"
      out
    when 'Part'
      "#{prefix}#{mainmatter_marker}\\part{#{heading_title_after_role(el, opts)}}\n\n"
    else
      # No role marker — defensive fallback as a segment-field-style leader.
      "#{prefix}\\segmentfield{#{inner(el, opts).strip}}\n\n"
    end
  end

  # Emit \mainmatter exactly once on the first \part / \appendices group.
  # The volume preface (\addchap from `## *Preface*`) sits in \frontmatter
  # scope from main.tex; the first \part flips us into \mainmatter.
  def mainmatter_marker
    return '' if @mainmatter_emitted
    @mainmatter_emitted = true
    "\\mainmatter\n\n"
  end

  # ── H3 dispatch ─────────────────────────────────────────────────────

  def handle_h3(el, opts)
    role = role_marker(el)
    case role
    when 'Chapter'
      @just_chaptered = true
      "#{close_open_wrappers(current_level: 3)}\\chapter{#{heading_title_after_role(el, opts)}}\n\n"
    when 'Preface'
      close_open_wrappers(current_level: 3)
    else
      # No role marker; might be an appendix-segment header (with .segment IAL).
      if el.attr['class']&.include?('segment')
        emit_segment_header(el, opts, level: :appendix)
      else
        handle_subhead(inner(el, opts).strip, level: 3)
      end
    end
  end

  # ── H4 dispatch ─────────────────────────────────────────────────────

  # H4 is either an in-part segment header (with .segment IAL) or a
  # subhead within an appendix segment (whose H1 was bumped to H3, so
  # the segment's authored H2 lands at H4). Disambiguate by IAL.
  def handle_h4(el, opts)
    if el.attr['class']&.include?('segment')
      emit_segment_header(el, opts, level: :section)
    else
      handle_subhead(inner(el, opts).strip, level: 4)
    end
  end

  # ── Segment header emission ────────────────────────────────────────

  # Emit \segmenthead (in-part) or \segmentappendixchapter (appendix)
  # plus \label for cross-refs. Closes any open wrappers from the
  # previous segment first.
  #
  # Chapter-intro Discussion mode: when a Discussion-typed segment
  # immediately follows \chapter{...}, suppress segment chrome
  # entirely — the body flows as plain chapter prose, treating the
  # Discussion as the chapter's introduction. The \label still fires
  # so cross-refs to the slug resolve. Same convention as the kaobook
  # target's chapter-intro handling.
  def emit_segment_header(el, opts, level:)
    a = el.attr
    type_label = a['type'].to_s
    slug       = a['slug'].to_s
    title      = inner(el, opts).strip

    # Strip the redundant "Type: " prefix from the heading — \segmenthead
    # embeds the type-label as part of its rendering.
    clean_title = title.sub(/\A#{Regexp.escape(type_label)}:\s*/, '')

    # Track the segment-header's absolute level so handle_subhead can
    # compute segment-relative depth (subheads = +1, etc.).
    @current_segment_header_level = (level == :appendix ? 3 : 4)

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
    prefix = close_open_wrappers
    out = +"#{prefix}\\#{macro}{#{type_label}}{#{clean_title}}{}{}\n"
    out << "\\label{seg:#{slug}}\n" unless slug.empty?
    out << "\n"
    out
  end

  # ── Segment-internal subhead dispatch ──────────────────────────────
  #
  # Levels in volume context:
  #   in-part segment header is H4 → segment-internal H2 lands at H5,
  #     H3 at H6, H4+ deeper.
  #   appendix segment header is H3 → segment-internal H2 at H4, H3 at H5.
  #
  # Compute segment-relative depth and dispatch:
  #   relative 1 (segment H2)       → \segmentfield (or workingnotes open)
  #   relative 2 (segment H3)       → bold inline leader
  #   relative 3+ (segment H4+)     → italic inline leader
  def handle_subhead(title, level:)
    # Chapter-intro Discussion mode: suppress all internal subheads so the
    # segment body flows as continuous chapter prose.
    return "\\par\\medskip\n" if @suppress_segment_chrome

    prefix   = close_open_wrappers(current_level: level)
    relative = @current_segment_header_level ? (level - @current_segment_header_level) : 1
    case relative
    when 1
      if title == 'Working Notes'
        @in_working_notes   = true
        @workingnotes_level = level
        "#{prefix}\\begin{workingnotes}\n"
      elsif @in_working_notes
        "#{prefix}\\workingnotessubhead{#{title}}\n\n"
      else
        "#{prefix}\\segmentfield{#{title}}\n\n"
      end
    when 2
      "#{prefix}\\needspace{3\\baselineskip}" \
        "\\par\\medskip\\noindent\\textbf{#{title}.}\\quad "
    else
      "#{prefix}\\par\\noindent\\textit{#{title}.}\\quad "
    end
  end

  # ── Helpers ─────────────────────────────────────────────────────────

  def segment_slug?(slug)
    @known_segment_slugs ||= {}
    @known_segment_slugs[slug] = true
  end
end

# Wire kramdown's `to_<format>` dispatch for the new converter.
module Kramdown::Document::ToAsfScrbookLatex
  def to_asf_scrbook_latex
    Kramdown::Converter::AsfScrbookLatex.convert(@root, @options).first
  end
end

Kramdown::Document.include(Kramdown::Document::ToAsfScrbookLatex)
