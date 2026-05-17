# frozen_string_literal: true
#
# common/lib/assemble.rb — Stage 2 of the markdown-first build pipeline.
#
# Reads `mono/.build/<slug>/index.md` (with YAML manifest in frontmatter)
# and `mono/.build/<slug>/chunks/*.md`, stitches them into a single
# canonical per-volume assembled markdown, resolves `#slug-name` cross-
# refs to numbered anchor links using the label map computed during
# Stage 1, and returns the assembled text.
#
# Caller (build-monograph) writes the result to `mono/<slug>-v<sem>.md`
# as a parallel artifact to the PDF.
#
# Assembly contract — what the assembled markdown looks like:
#
#   # <Volume Title>
#
#   ## *Preface* <Title>
#
#   [volume preface body]
#
#   ## *Part* <Part I title>
#
#   [part preface body]
#
#   ### *Chapter* <Chapter title>
#
#   <a id="<slug>"></a>
#
#   #### <Type>: <Segment title>
#
#   **Slug**: `<slug>`
#   **Type**: <Type>
#   ...
#
#   [segment body with cross-refs resolved]
#
#   ##### Formal Expression
#   ...
#
#   ## *Appendices* <Group title>
#
#   <a id="<appendix-slug>"></a>
#
#   ### <Type>: <Appendix segment title>
#
#   **Slug**: `<appendix-slug>`
#   **Label**: A
#   **Container**: appendix-chapter
#   ...
#
# Structural headers carry the role-prefix italic convention (consistent
# with OUTLINE.md source). Stage 3 (typeset) reads those markers and the
# chunk metadata blocks to emit the right LaTeX structural commands.

require 'pathname'
require 'yaml'

module Mono
  module Assemble
    module_function

    # Top-level entry. Returns the assembled markdown text.
    def assemble(stage:)
      index_path = stage / 'index.md'
      raise "index.md not found at #{index_path}" unless index_path.exist?

      manifest = parse_index(index_path)
      label_map = build_label_map(manifest['entries'])
      render(manifest, label_map, stage)
    end

    # Parse the index.md frontmatter (YAML manifest + volume metadata).
    def parse_index(path)
      text = path.read
      raise "index.md missing frontmatter delimiter: #{path}" unless text.start_with?("---\n")

      end_marker = text.index(/^---\s*$/, 4)
      raise "index.md frontmatter not terminated: #{path}" unless end_marker

      yaml_text = text[4...end_marker]
      YAML.safe_load(yaml_text, permitted_classes: [Symbol]) || {}
    end

    # slug → { 'label' => '1.4', 'type' => 'Definition' } map for cross-ref
    # resolution. Missing-segment entries also get labels (so cross-refs
    # to not-yet-written segments still resolve to numbered placeholders).
    def build_label_map(entries)
      map = {}
      entries.each do |e|
        case e['kind']
        when 'segment_chunk', 'missing'
          slug = e['slug']
          next unless slug
          map[slug] = { 'label' => e['label'].to_s, 'type' => e['type'].to_s }
        end
      end
      map
    end

    # Walk the manifest entries in order and emit assembled markdown.
    def render(manifest, label_map, stage)
      chunks_dir = stage / 'chunks'
      out = []
      out << "# #{manifest['title']}"
      out << ''

      manifest['entries'].each do |entry|
        case entry['kind']
        when 'preface_chunk'
          out << render_preface_chunk(entry, chunks_dir, label_map)
        when 'part'
          out << "## *Part* #{entry['title']}"
          out << ''
        when 'appendices'
          out << "## *Appendices* #{entry['title']}"
          out << ''
        when 'chapter'
          out << "### *Chapter* #{entry['title']}"
          out << ''
        when 'segment_chunk'
          out << render_segment_chunk(entry, chunks_dir, label_map)
        when 'missing'
          out << render_missing(entry)
        when 'gap'
          out << render_gap(entry)
        end
      end

      out.join("\n").rstrip + "\n"
    end

    # Preface chunks differ by role:
    #   - volume-preface: chunk has its own H1; we replace it with a
    #     structural `## *Preface* Title` so the assembled markdown's
    #     H1 stays reserved for the volume title.
    #   - part-preface, chapter-rationale: no H1 in chunk; just inline
    #     the body between the surrounding structural headers.
    def render_preface_chunk(entry, chunks_dir, label_map)
      chunk_path = chunks_dir / Pathname.new(entry['chunk']).basename
      return '' unless chunk_path.exist?

      parsed = parse_chunk(chunk_path.read)
      body = resolve_cross_refs(parsed[:body], label_map)

      case entry['role']
      when 'volume-preface'
        # If the H2 *Preface* role had no info-suffix in OUTLINE.md, the
        # chunk's Title metadata is absent — emit just `## *Preface*`
        # without a trailing duplicate. Stage 3's converter defaults the
        # \addchap title to "Preface" in that case.
        title   = parsed[:metadata]['Title']
        section = parsed[:metadata]['Section'] || 'Preface'
        header  = title ? "## *#{section}* #{title}" : "## *#{section}*"
        "#{header}\n\n#{body.rstrip}\n"
      else
        "#{body.rstrip}\n"
      end
    end

    # Segment chunks emit the bumped heading + metadata block + body
    # verbatim, prepended with an HTML anchor for internal-link resolution.
    # Cross-refs in the body are resolved against the label map.
    def render_segment_chunk(entry, chunks_dir, label_map)
      chunk_path = chunks_dir / Pathname.new(entry['chunk']).basename
      return '' unless chunk_path.exist?

      raw  = chunk_path.read
      body = resolve_cross_refs(raw, label_map)

      anchor = entry['slug'] ? %(<a id="#{entry['slug']}"></a>\n\n) : ''
      "#{anchor}#{body.rstrip}\n"
    end

    # Missing segments render an inline placeholder block. The label is
    # already assigned in the manifest so cross-refs from elsewhere still
    # resolve. The container determines the heading depth (H4 main-matter,
    # H3 appendix-chapter) so the missing block nests at the same level
    # as a real segment.
    def render_missing(entry)
      level = entry['container'] == 'appendix-chapter' ? 3 : 4
      anchor = entry['slug'] ? %(<a id="#{entry['slug']}"></a>\n\n) : ''
      # Use the slug (stable, short) in the heading rather than the claim
      # text — claim columns in OUTLINE.md are often paragraph-length and
      # would (a) spill into the ToC unreadably, (b) carry markdown
      # constructs that mangle the LaTeX `\missingsegment` macro arg.
      # Full claim text appears in the body marker below.
      heading = "#{'#' * level} #{entry['type']}: `##{entry['slug']}` *(missing)*"
      # TODO: `**Status**: missing` conflates two things — the segment's
      # epistemic status (FORMAT's exact / robust qualitative / heuristic /
      # conditional taxonomy) and its existence-status (written / unwritten /
      # deprecated). Cleaner to split into separate keys (Status carries the
      # epistemic value as today; a new key like `**Existence**: missing` or
      # `**File**: missing` carries the existence axis). Revisit when a new
      # existence-state appears (e.g., `deprecated`, `withdrawn`) or when
      # the downstream renderers want to disambiguate them.
      metadata = [
        "**Slug**: `#{entry['slug']}`",
        "**Type**: #{entry['type']}",
        "**Label**: #{entry['label']}",
        "**Container**: #{entry['container']}",
        '**Status**: missing',
      ]
      stub  = "*Segment `#{entry['slug']}` not yet written.*"
      claim = entry['claim'].to_s.strip
      stub += "\n\n*Claim:* #{claim}" unless claim.empty?
      "#{anchor}#{heading}\n\n#{metadata.join("\n")}\n\n#{stub}\n"
    end

    # Gap markers are author-flagged open questions in OUTLINE.md.
    # Rendered as a quoted [Gap] block for visibility.
    def render_gap(entry)
      "> **\\[Gap\\]** #{entry['description']}\n"
    end

    # ── chunk parsing ──────────────────────────────────────────────────

    # Parse a chunk file into { heading: { level, text }, metadata: {key=>value}, body: '…' }.
    # Stage 2 needs this for preface chunks (we transform the heading);
    # segment chunks are passed through almost untouched so the parsed
    # form is mainly informational.
    def parse_chunk(text)
      lines = text.split("\n", -1)
      i = 0

      # Skip leading blank lines
      i += 1 while i < lines.size && lines[i].strip.empty?

      heading = nil
      if i < lines.size && (m = lines[i].match(/\A(\#{1,6})[ \t]+(.+)$/))
        heading = { level: m[1].length, text: m[2].strip }
        i += 1
        i += 1 while i < lines.size && lines[i].strip.empty?
      end

      metadata = {}
      while i < lines.size && (mm = lines[i].match(/\A\*\*([A-Z][A-Za-z]*)\*\*:\s*(.*)$/))
        metadata[mm[1]] = mm[2].strip.sub(/\A`(.*)`\z/, '\1')
        i += 1
      end
      i += 1 while i < lines.size && lines[i].strip.empty?

      body = lines[i..].join("\n")
      { heading: heading, metadata: metadata, body: body }
    end

    # ── cross-ref resolution ───────────────────────────────────────────

    # `#slug-name` in prose → `[Type Label](#slug-name)` using the label
    # map. The pattern requires the `#` to be at line start or preceded
    # by whitespace / `(` / `[` (matching the FORMAT.md prose convention
    # and the segment_renderer's CROSS_REF_RE). Math (`$...$` / `$$...$$`)
    # and inline code (`` ` ``) are passthrough zones — cross-refs inside
    # those are not rewritten.
    CROSS_REF_RE = /(?<=^|[\s(\[])#([a-z][a-z0-9-]*[a-z0-9])(?![a-z0-9-])/

    def resolve_cross_refs(text, label_map)
      lines = text.split("\n", -1)
      in_fenced = false
      in_math   = false

      lines.map do |line|
        stripped = line.strip
        if stripped.start_with?('```')
          in_fenced = !in_fenced
          next line
        end
        if stripped == '$$'
          in_math = !in_math
          next line
        end
        next line if in_fenced || in_math

        resolve_line(line, label_map)
      end.join("\n")
    end

    def resolve_line(line, label_map)
      out = +''
      i   = 0
      n   = line.length

      while i < n
        ch = line[i]

        # Inline code passthrough
        if ch == '`'
          run = 0
          run += 1 while i + run < n && line[i + run] == '`'
          fence = '`' * run
          finish = line.index(fence, i + run)
          if finish
            out << line[i...(finish + run)]
            i = finish + run
            next
          end
        end

        # Inline math passthrough
        if ch == '$'
          dollars = (line[i + 1] == '$') ? 2 : 1
          fence = '$' * dollars
          finish = line.index(fence, i + dollars)
          if finish
            out << line[i...(finish + dollars)]
            i = finish + dollars
            next
          end
        end

        # Markdown link passthrough — `[label](target)` — preserve as-is
        # so we don't accidentally rewrite the label or target.
        if ch == '['
          depth = 1
          j = i + 1
          while j < n && depth.positive?
            if line[j] == '\\'
              j += 2
              next
            end
            depth += 1 if line[j] == '['
            depth -= 1 if line[j] == ']'
            j += 1
          end
          if j < n && line[j] == '('
            k = line.index(')', j + 1)
            if k
              out << line[i..k]
              i = k + 1
              next
            end
          end
          out << line[i...j]
          i = j
          next
        end

        # Cross-ref candidate: `#slug` at line start or after [\s(\[]
        if ch == '#' && (i.zero? || ' ('.include?(line[i - 1]))
          rest = line[(i + 1)..]
          if (m = rest.match(/\A([a-z][a-z0-9-]*[a-z0-9])(?![a-z0-9-])/))
            slug = m[1]
            if (info = label_map[slug])
              display = "#{info['type']} #{info['label']}".strip
              out << "[#{display}](##{slug})"
              i += 1 + m[0].length
              next
            end
          end
        end

        out << ch
        i += 1
      end

      out
    end
  end
end
