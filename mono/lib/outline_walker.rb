# frozen_string_literal: true
#
# mono/lib/outline_walker.rb
#
# Walk a component OUTLINE.md and return an ordered manifest of items:
#
#   { kind: :section, level:, title: }
#   { kind: :scope,   content: }            # italic paragraph between sections
#   { kind: :prose,   content: }            # plain prose paragraph
#   { kind: :segment, slug:, path:, type:, claim: }
#   { kind: :missing, slug:, type:, claim: } # listed in outline; no src file
#   { kind: :gap,     description: }        # --GAP-- row
#
# The walker is deliberately tolerant: outlines drift in shape over time
# (preamble structures vary, segment status badges appear as inline tags),
# and the build pipeline shouldn't break when a component reshuffles. We
# extract what we recognize and pass the rest through as prose.
#
# Comparable to bin/build (Python) and bin/build-tex (Ruby) for the
# common parts of outline shape, simplified because we only need ordered
# manifest output, not LaTeX assembly.

require 'pathname'

module Mono
  module OutlineWalker
    module_function

    # Walk OUTLINE.md at +outline_path+. Returns ordered list of items.
    # The outline file is in component_dir; segment paths are resolved
    # relative to that directory (`src/<slug>.md`).
    def walk(outline_path)
      outline_path = Pathname.new(outline_path)
      component_dir = outline_path.dirname
      lines = outline_path.read.split("\n")

      # Skip optional YAML frontmatter so the parser doesn't see `---`
      # delimiters as table separators or section breaks.
      idx = 0
      if lines[0]&.strip == '---'
        idx += 1
        idx += 1 until idx >= lines.length || lines[idx].strip == '---'
        idx += 1
      end

      items = []
      in_table = false
      while idx < lines.length
        line = lines[idx]
        stripped = line.strip
        cells = parse_table_row(line)

        if cells
          in_table = true
          unless separator_row?(cells)
            item = parse_table_entry(cells, component_dir)
            items << item if item
          end
          idx += 1
          next
        end

        # We just exited a table block (cells nil after being in one).
        in_table = false if in_table && cells.nil?

        case stripped
        when /^(\#{1,6})[ \t]+(.+)$/
          items << { kind: :section, level: Regexp.last_match(1).length,
                     title: Regexp.last_match(2).strip }
        when /\A\*(.+)\*\z/m
          # Italic-wrapped paragraph (FORMAT idiom for scope text under
          # section headers). The outline conventionally puts these as
          # single-line italic paragraphs.
          items << { kind: :scope, content: Regexp.last_match(1).strip }
        when '', /\A-{3,}\s*\z/
          # blank line or horizontal rule
          nil
        else
          items << { kind: :prose, content: stripped }
        end
        idx += 1
      end
      items
    end

    # ── helpers ──────────────────────────────────────────────────────────

    def parse_table_row(line)
      s = line.strip
      return nil unless s.start_with?('|') && s.end_with?('|')

      s.split('|')[1..-2].map(&:strip)
    end

    def separator_row?(cells)
      cells.all? { |c| c.empty? || c.match?(/\A[-:]+\z/) }
    end

    # Table row schema (from FORMAT.md): | § | Type | N | Tag | Claim | Stage |
    # Tag column carries the slug as [#slug](path). N column is mostly empty
    # — overrides the auto-counter when set. We don't need N for assembly.
    def parse_table_entry(cells, component_dir)
      return nil if cells.empty?

      if cells.any? { |c| c.include?('--GAP--') }
        # Any non-gap cell that isn't a section marker (single uppercase
        # roman) becomes the description.
        desc = cells.reject { |c| c.empty? || c.include?('--GAP--') || c.match?(/\A[IVSA]+\z/) }
        return { kind: :gap, description: desc.last || 'Open question' }
      end

      slug, rel_path = nil
      cells.each do |c|
        m = c.match(/\[#([\w-]+)\]\(([^)]+\.md)\)/)
        next unless m

        slug = m[1]
        rel_path = m[2]
        break
      end
      return nil unless slug

      type  = (cells[1] || '').strip
      claim = (cells[4] || '').strip
      path = component_dir / rel_path
      # Fallback path resolution: bare slug.md or src/slug.md.
      path = component_dir / 'src' / "#{slug}.md" unless path.exist?

      if path.exist?
        { kind: :segment, slug: slug, path: path, type: type, claim: claim }
      else
        { kind: :missing, slug: slug, type: type, claim: claim }
      end
    end
  end
end
