# frozen_string_literal: true
#
# mono/lib/outline_walker.rb
#
# Walk a component OUTLINE.md and return an ordered manifest of items
# tagged by their structural role. The role at each header level is
# explicitly named in source via an italic-prefix convention:
#
#   # *Volume* Adaptation and Actuation Dynamics (AAD)
#   ## *Frontmatter*
#   ## *Part* Adaptive Systems Under Uncertainty
#   ### *Preface*
#   ### *Chapter* The Coupled Loop: Ontology and Scope
#   ## *Appendices* Details
#
# Role-per-level vocabulary:
#   H1: Volume
#   H2: Frontmatter | Part | Appendices
#   H3: Preface | Chapter
#
# Role matching rules:
#   - The role is the FIRST whitespace-delimited word inside `*...*`.
#   - Trailing `:` immediately after the role word, or `:` immediately
#     after the closing `*`, are ignored (`*Chapter:*`, `*Chapter*:` both
#     match role Chapter).
#   - Anything after the first word in the italic span is "info-suffix"
#     and is ignored — `*Chapter 22*` matches Chapter, `*Chapter 4: Persistence*`
#     also matches Chapter.
#
# Implicit defaults:
#   - Inside *Part*, prose between the Part H2 and the first table is the
#     Preface (no explicit ### *Preface* header needed).
#   - Inside *Part*, segment tables not preceded by a *Chapter* H3 belong
#     to one implicit Chapter (the walker pretends `### *Chapter*` was there).
#   - Inside *Appendices*, segments-as-chapters: each segment row becomes
#     an appendix chapter, no intermediate grouping.
#
# Manifest item kinds:
#   { kind: :volume,      title:, level: 1 }
#   { kind: :frontmatter, level: 2 }
#   { kind: :part,        title:, level: 2 }
#   { kind: :appendices,  title:, level: 2 }
#   { kind: :preface,     level: 3, implicit: bool }
#   { kind: :chapter,     title:, level: 3, implicit: bool }
#   { kind: :segment,     slug:, path:, type:, claim:, container: :part|:appendices }
#   { kind: :missing,     slug:, type:, claim:, container: :part|:appendices }
#   { kind: :gap,         description: }
#   { kind: :scope,       content: }    # italic-wrapped paragraph
#   { kind: :prose,       content: }    # plain prose paragraph
#   { kind: :image,       alt:, src: }  # ![...](...)

require 'pathname'

module Mono
  module OutlineWalker
    module_function

    # Role validation vocabulary. Roles outside the per-level set produce
    # a warning at walk time but the item is still emitted with role nil
    # so downstream code can decide whether to bail or render generically.
    ROLES_BY_LEVEL = {
      1 => %w[Volume].freeze,
      2 => %w[Frontmatter Part Appendices].freeze,
      3 => %w[Preface Chapter].freeze,
    }.freeze

    HEADER_LINE_RE   = /\A(\#{1,6})\s+(.+?)\s*\z/
    # Captures the italic span (between unmatched `*`s) and the rest of
    # the header text. Trailing colon after the closing `*` is tolerated
    # and absorbed into the optional `(:)` group.
    ITALIC_HEADER_RE = /\A\*([^*]+)\*:?\s*(.*)\z/

    def walk(outline_path)
      outline_path  = Pathname.new(outline_path)
      component_dir = outline_path.dirname
      lines         = outline_path.read.split("\n")

      state = WalkerState.new(component_dir: component_dir)

      # Skip YAML frontmatter if present.
      idx = 0
      if lines[0]&.strip == '---'
        idx += 1
        idx += 1 until idx >= lines.length || lines[idx].strip == '---'
        idx += 1
      end

      in_table = false
      while idx < lines.length
        line     = lines[idx]
        stripped = line.strip
        cells    = parse_table_row(line)

        if cells
          in_table = true
          unless separator_row?(cells)
            state.handle_table_row(cells)
          end
          idx += 1
          next
        end

        # We just exited a table block.
        in_table = false if in_table

        if (header = parse_header(stripped))
          state.handle_header(header)
        elsif (scope = parse_scope(stripped))
          state.handle_scope(scope)
        elsif (img = parse_image(stripped))
          state.handle_image(img)
        elsif stripped.empty? || stripped.match?(/\A-{3,}\s*\z/)
          # blank line or horizontal rule — accumulate paragraph boundary
          state.flush_prose
        else
          state.add_prose_line(stripped)
        end

        idx += 1
      end

      state.finalize.items
    end

    # ── header parsing ─────────────────────────────────────────────────

    # Returns { level:, role:, title: } or nil. The italic-role-prefix
    # convention is matched if present; otherwise role is nil and title
    # is the whole header text.
    def parse_header(line)
      m = line.match(HEADER_LINE_RE)
      return nil unless m

      level = m[1].length
      text  = m[2]
      return { level: level, role: nil, title: text } unless (im = text.match(ITALIC_HEADER_RE))

      # First word inside the italic span is the role; rest of the italic
      # is info-suffix (ignored). The regex's [A-Za-z]+ stops at any
      # non-letter, so trailing `:` on the role word is naturally dropped.
      italic = im[1]
      title  = im[2].strip
      role   = italic[/\A\s*([A-Za-z]+)/, 1]
      { level: level, role: role, title: title }
    end

    def parse_scope(line)
      m = line.match(/\A\*(.+)\*\z/m)
      m && m[1].strip
    end

    def parse_image(line)
      m = line.match(/\A!\[([^\]]*)\]\(([^)]+)\)\s*\z/)
      m && { alt: m[1], src: m[2] }
    end

    # ── table parsing ──────────────────────────────────────────────────

    def parse_table_row(line)
      s = line.strip
      return nil unless s.start_with?('|') && s.end_with?('|')

      s.split('|')[1..-2].map(&:strip)
    end

    def separator_row?(cells)
      cells.all? { |c| c.empty? || c.match?(/\A[-:]+\z/) }
    end

    # ──────────────────────────────────────────────────────────────────
    # WalkerState — encapsulates the state machine: current container
    # (Part vs Appendices vs Frontmatter), whether a Chapter has been
    # seen in the current Part, accumulating prose for Preface, etc.
    # ──────────────────────────────────────────────────────────────────

    class WalkerState
      attr_reader :items

      def initialize(component_dir:)
        @component_dir = component_dir
        @items         = []
        @prose_buffer  = []
        # Current containers
        @current_h2  = nil  # :frontmatter | :part | :appendices | nil
        @current_h3  = nil  # :preface | :chapter | nil
        @chapter_seen_in_current_part = false
        @preface_seen_in_current_part = false
      end

      def add_prose_line(line)
        @prose_buffer << line
      end

      def flush_prose
        return if @prose_buffer.empty?

        # If we're inside a Part but haven't seen *Preface* or *Chapter*
        # yet, and prose is accumulating, surface an implicit Preface
        # marker before the prose lands.
        if @current_h2 == :part && @current_h3.nil? && !@preface_seen_in_current_part
          @items << { kind: :preface, level: 3, implicit: true }
          @preface_seen_in_current_part = true
          @current_h3 = :preface
        end

        @items << { kind: :prose, content: @prose_buffer.join(' ') }
        @prose_buffer = []
      end

      def handle_header(header)
        flush_prose
        level = header[:level]
        role  = header[:role]
        title = header[:title]
        validate_role(level, role)

        case level
        when 1
          @items << { kind: :volume, title: title, level: 1 }
        when 2
          handle_h2(role, title)
        when 3
          handle_h3(role, title)
        else
          # H4+ — currently no defined role; emit as prose-like heading
          @items << { kind: :prose, content: title }
        end
      end

      def handle_h2(role, title)
        case role
        when 'Frontmatter'
          @current_h2 = :frontmatter
          @current_h3 = nil
          @items << { kind: :frontmatter, level: 2 }
        when 'Part'
          @current_h2 = :part
          @current_h3 = nil
          @chapter_seen_in_current_part = false
          @preface_seen_in_current_part = false
          @items << { kind: :part, title: title, level: 2 }
        when 'Appendices'
          @current_h2 = :appendices
          @current_h3 = nil
          @items << { kind: :appendices, title: title, level: 2 }
        else
          # Unknown / missing role at H2 — best-effort treat as Part.
          @current_h2 = :part
          @current_h3 = nil
          @chapter_seen_in_current_part = false
          @preface_seen_in_current_part = false
          @items << { kind: :part, title: title, level: 2 }
        end
      end

      def handle_h3(role, title)
        case role
        when 'Preface'
          @current_h3 = :preface
          @preface_seen_in_current_part = true
          @items << { kind: :preface, level: 3, implicit: false }
        when 'Chapter'
          @current_h3 = :chapter
          @chapter_seen_in_current_part = true
          @items << { kind: :chapter, title: title, level: 3, implicit: false }
        else
          # Unknown / missing role at H3 — treat as Chapter with the
          # whole header text as title.
          @current_h3 = :chapter
          @chapter_seen_in_current_part = true
          @items << { kind: :chapter, title: title, level: 3, implicit: false }
        end
      end

      def handle_table_row(cells)
        flush_prose

        # Inside a Part, a table appearing without a preceding *Chapter*
        # H3 belongs to one implicit Chapter (FORMAT-TODO §Implicit
        # defaults). Inside Appendices, each segment-row IS a chapter
        # — no implicit grouping needed.
        if @current_h2 == :part && !@chapter_seen_in_current_part
          @items << { kind: :chapter, title: nil, level: 3, implicit: true }
          @chapter_seen_in_current_part = true
          @current_h3 = :chapter
        end

        @items << parse_segment_row(cells, container: @current_h2)
      end

      def handle_scope(content)
        flush_prose
        @items << { kind: :scope, content: content }
      end

      def handle_image(img)
        flush_prose
        @items << { kind: :image, alt: img[:alt], src: img[:src] }
      end

      def finalize
        flush_prose
        self
      end

      # ── helpers ───────────────────────────────────────────────────

      # Table row schema (FORMAT.md): | § | Type | N | Tag | Claim | Stage |
      def parse_segment_row(cells, container:)
        if cells.any? { |c| c.include?('--GAP--') }
          desc = cells.reject { |c| c.empty? || c.include?('--GAP--') || c.match?(/\A[A-Z][0-9]?\z/) }
          return { kind: :gap, description: desc.last || 'Open question' }
        end

        slug = rel_path = nil
        cells.each do |c|
          m = c.match(/\[#([\w-]+)\]\(([^)]+\.md)\)/)
          next unless m

          slug = m[1]
          rel_path = m[2]
          break
        end
        return { kind: :prose, content: cells.join(' | ') } unless slug

        type  = (cells[1] || '').strip
        claim = (cells[4] || '').strip
        path = @component_dir / rel_path
        path = @component_dir / 'src' / "#{slug}.md" unless path.exist?

        if path.exist?
          { kind: :segment, slug: slug, path: path, type: type, claim: claim, container: container }
        else
          { kind: :missing, slug: slug, type: type, claim: claim, container: container }
        end
      end

      def validate_role(level, role)
        return if role.nil? # missing role handled by per-level defaults
        return if (ROLES_BY_LEVEL[level] || []).include?(role)

        warn "outline_walker: unexpected role #{role.inspect} at level #{level} " \
             "(allowed: #{(ROLES_BY_LEVEL[level] || []).inspect})"
      end
    end
  end
end
