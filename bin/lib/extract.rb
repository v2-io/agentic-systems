# frozen_string_literal: true
#
# bin/lib/extract.rb — Mono::Extract
#
# Parse a segment file into structured per-segment data suitable for handing
# to a Liquid template. Companion to bin/build-markdown; see
# msc/build-markdown-design.md for the design and the data-model contract.
#
# Not shared with Mono::Ingest: the typeset pipeline needs header-bumped /
# metadata-block-prefixed chunks; this returns raw sections by name. The
# abstractions diverge enough that duplicating ~20 lines of frontmatter and
# H2-splitting primitives is cheaper than factoring out a shared interface
# that fits neither pipeline well.
#
# Output (string-keyed for Liquid traversal via `.`):
#
#   {
#     'frontmatter' => { ...all YAML keys preserved... },
#     'title' => {
#       'raw'    => 'Definition: Adaptive Tempo',
#       'prefix' => 'Definition',   # nil if H1 has no ": "
#       'prose'  => 'Adaptive Tempo',
#     },
#     'brief' => '...raw markdown between H1 and first H2, any length...',
#     'sections' => {
#       'formal_expression' => {
#         'heading'     => 'Formal Expression',
#         'raw'         => '...full markdown body including any H3 subheadings...',
#         'subsections' => [{ 'name' => '...', 'body' => '...' }, ...],
#       },
#       # any other H2s the segment defines, same shape, keys normalized
#     },
#   }
#
# Section keys are normalized (lowercased, non-alphanumeric → underscore) so
# Liquid templates can access via `.` (`seg.sections.formal_expression`).
# The original H2 heading text is preserved as `heading` for display.

require 'pathname'
require 'yaml'

module Mono
  module Extract
    module_function

    # Top-level entry. Given a segment path, return the structured hash.
    def parse(path)
      path = Pathname.new(path)
      text = path.read

      frontmatter, body = split_frontmatter(text, path: path)
      parsed = parse_body(body)

      {
        'frontmatter' => frontmatter,
        'title'       => parsed[:title],
        'brief'       => parsed[:brief],
        'sections'    => parsed[:sections],
      }
    end

    # ── frontmatter ────────────────────────────────────────────────────

    def split_frontmatter(text, path:)
      return [{}, text] unless text.start_with?("---\n")

      end_idx = text.index(/^---\s*$/, 4)
      raise "frontmatter not terminated: #{path}" unless end_idx

      yaml_text = text[4...end_idx]
      body      = text[(end_idx + 3)..].sub(/\A\s*\n/, '')
      fm        = YAML.safe_load(yaml_text, permitted_classes: [Symbol, Date, Time]) || {}
      [fm, body]
    end

    # ── body walk ──────────────────────────────────────────────────────
    #
    # Line-driven state machine. States:
    #   :pre_title       — before the H1 (or no H1 found)
    #   :brief           — after H1, before first H2
    #   :section_body    — inside an H2 section, no H3 yet
    #   :subsection_body — inside an H3 subsection
    #
    # Fenced code blocks (```, ~~~) are tracked so that #-prefixed lines
    # inside code don't get mistaken for headers.

    def parse_body(body)
      title_raw       = nil
      brief_lines     = []
      sections        = {}  # normalized-key → hash (insertion order preserved)
      current_section = nil
      current_subsec  = nil
      state           = :pre_title
      in_fence        = false
      fence_char      = nil

      body.each_line do |line|
        stripped = line.chomp

        # Fence toggling — `\`\`\`` or `~~~`, at least 3, line-start (optional indent).
        if (fm = stripped.match(/\A\s*(`{3,}|~{3,})/))
          marker_char = fm[1][0]
          if in_fence && marker_char == fence_char
            in_fence = false
            fence_char = nil
          elsif !in_fence
            in_fence = true
            fence_char = marker_char
          end
          # Fall through — fence lines are content of the current state.
        end

        unless in_fence
          if (m = stripped.match(/\A# (.+)\z/))
            if state == :pre_title
              title_raw = m[1]
              state = :brief
              next
            end
            # H1 elsewhere is unusual; treat as content.
          elsif (m = stripped.match(/\A## (.+)\z/))
            heading        = m[1]
            key            = normalize_section_key(heading)
            current_section = { heading: heading, raw_lines: [], subsections: [] }
            sections[key]  = current_section
            current_subsec = nil
            state          = :section_body
            next
          elsif (m = stripped.match(/\A### (.+)\z/))
            if (state == :section_body || state == :subsection_body) && current_section
              current_subsec = { name: m[1], body_lines: [] }
              current_section[:subsections] << current_subsec
              current_section[:raw_lines] << line
              state = :subsection_body
              next
            end
          end
        end

        record_line(state, line, brief_lines, current_section, current_subsec)
      end

      {
        title:    parse_title(title_raw),
        brief:    brief_lines.join.strip,
        sections: finalize_sections(sections),
      }
    end

    def record_line(state, line, brief_lines, current_section, current_subsec)
      case state
      when :brief
        brief_lines << line
      when :section_body
        current_section[:raw_lines] << line if current_section
      when :subsection_body
        current_section[:raw_lines] << line if current_section
        current_subsec[:body_lines]  << line if current_subsec
      end
    end

    def finalize_sections(sections)
      result = {}
      sections.each do |key, sec|
        result[key] = {
          'heading'     => sec[:heading],
          'raw'         => sec[:raw_lines].join.strip,
          'subsections' => sec[:subsections].map do |sub|
            { 'name' => sub[:name], 'body' => sub[:body_lines].join.strip }
          end,
        }
      end
      result
    end

    # ── title ──────────────────────────────────────────────────────────

    def parse_title(raw)
      return { 'raw' => nil, 'prefix' => nil, 'prose' => nil } if raw.nil?

      if (m = raw.match(/\A([^:]+): (.+)\z/))
        { 'raw' => raw, 'prefix' => m[1].strip, 'prose' => m[2].strip }
      else
        { 'raw' => raw, 'prefix' => nil, 'prose' => raw }
      end
    end

    # ── section-key normalization ──────────────────────────────────────

    # Lowercase, runs of non-alphanumeric collapsed to a single underscore,
    # leading/trailing underscores stripped. So:
    #   'Formal Expression'              → 'formal_expression'
    #   'Findings (cycle 5)'              → 'findings_cycle_5'
    #   'What Is Derived vs. What Is …'   → 'what_is_derived_vs_what_is_'
    # Stable enough for Liquid `.`-access; collisions on different sections
    # would surface as a section overwriting another, which is loud enough
    # to catch in practice.
    def normalize_section_key(heading)
      heading.downcase
             .gsub(/[^a-z0-9]+/, '_')
             .sub(/\A_+/, '')
             .sub(/_+\z/, '')
    end
  end
end
