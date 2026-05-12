# frozen_string_literal: true
#
# common/lib/ingest.rb — Stage 1 of the markdown-first build pipeline.
#
# See msc/markdown-first-pipeline.md for the full architecture. In short:
# given an OUTLINE.md and the segments it references, Ingest produces:
#
#   mono/.build/<slug>/index.md         Assembly manifest (mono-meta + chunk list)
#   mono/.build/<slug>/chunks/<name>.md Per-chunk print-ready markdown
#
# Chunks are addressable units. Each segment becomes one chunk (named by slug).
# Structural prose (volume preface, part preface) becomes synthetic-name chunks.
# Cross-references stay unresolved (`#slug-name` markers) — Stage 2 (assemble)
# substitutes resolved labels when stitching the assembled markdown.
#
# Header bumping happens here, container-aware: a segment's authored H1 lands
# at H4 in a main-matter context, at H3 in an appendix context (where the
# appendix segment IS the chapter). The chunk's body therefore has the volume-
# context-appropriate heading levels.
#
# Status / stage / slug / type / label / container ride on a metadata block
# immediately after each chunk's H1 — a sequence of `**Key**: value` lines
# per the contract in msc/markdown-first-pipeline.md.

require 'digest'
require 'fileutils'
require 'pathname'

$LOAD_PATH.unshift(__dir__) unless $LOAD_PATH.include?(__dir__)
require 'outline_walker'

module Mono
  module Ingest
    module_function

    # Top-level entry. Produces `<stage>/index.md` and `<stage>/chunks/`.
    # Returns the index path.
    def ingest(spec, stage:, variant: :review)
      chunks_dir = stage / 'chunks'
      FileUtils.rm_rf(chunks_dir)
      FileUtils.mkdir_p(chunks_dir)

      state = IngestState.new(spec: spec, variant: variant, chunks_dir: chunks_dir)
      Mono::OutlineWalker.walk(spec[:outline]).each do |item|
        state.process(item)
      end
      state.finalize!

      index_path = stage / 'index.md'
      index_path.write(state.render_index)
      index_path
    end

    # FORMAT.md type strings (lowercase, hyphenated) → display labels for
    # the chunk header. Same mapping the LaTeX renderer uses, kept here
    # so ingest is self-contained.
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

    # ── alpha-alph numbering for appendix chapters ────────────────────────
    #
    # Mirrors the LaTeX-side \AlphAlph macro (common/preamble/setup.tex).
    # Appendix segments are chapters; their label is the chapter letter.
    # 1 → A, 26 → Z, 27 → AA, …, 52 → AZ, 53 → BA, … so the AAD Details
    # appendix (32+ chapters) doesn't overflow.
    def alpha_alph(n)
      return '' if n < 1
      if n <= 26
        ('A'.ord + n - 1).chr
      else
        first  = (n - 1) / 26
        second = (n - 1) % 26 + 1
        "#{('A'.ord + first - 1).chr}#{('A'.ord + second - 1).chr}"
      end
    end

    # ── helpers shared between IngestState and the module ────────────────

    # Bump every markdown header level by `offset` (capped at H6). Used so
    # a segment's authored H1 lands at H4 main-matter or H3 appendix; the
    # segment's H2 subheadings (Formal Expression / Epistemic Status / …)
    # follow proportionally.
    def bump_headers(text, offset)
      return text if offset.zero?
      text.gsub(/^(\#{1,6})([ \t])/) do
        hashes = ::Regexp.last_match(1)
        sep    = ::Regexp.last_match(2)
        new_level = [hashes.length + offset, 6].min
        ('#' * new_level) + sep
      end
    end

    # Strip the YAML frontmatter block at the start of segment files.
    def strip_yaml_frontmatter(text)
      return text unless text.start_with?("---\n")
      idx = text.index(/^---\s*$/, 4)
      idx ? text[(idx + 3)..].sub(/\A\s*\n/, '') : text
    end

    # Strip the trailing `## Working Notes` section. By FORMAT convention
    # it's always the last section.
    def strip_working_notes(text)
      idx = text.rindex(/^##[ \t]+Working Notes\b/m)
      idx ? "#{text[0...idx].rstrip}\n" : text
    end

    # Rewrite file-path links to internal anchor links where the path
    # resolves to a known slug. `[label](path/to/foo.md)` becomes
    # `[label](#foo)` when `foo` is a known slug in the volume.
    def rewrite_local_links(text, known_slugs)
      text.gsub(/\[([^\]]+)\]\(([^)]*?([\w-]+)\.md)\)/) do
        label, slug = ::Regexp.last_match(1), ::Regexp.last_match(3)
        known_slugs.include?(slug) ? "[#{label}](##{slug})" : ::Regexp.last_match(0)
      end
    end

    # ── IngestState: the state machine that processes walker events ──────

    class IngestState
      attr_reader :manifest

      # Walker prose-noise patterns — currently we DON'T filter; the
      # HTML-comment discipline (applied in outline_walker.walk) is the
      # contract for excluding content. Kept here as a placeholder for
      # any conventions we promote to global noise later.
      KNOWN_NOISE = [].freeze

      def initialize(spec:, variant:, chunks_dir:)
        @spec       = spec
        @variant    = variant
        @chunks_dir = chunks_dir

        # Volume-wide slug index (computed once at start so cross-refs and
        # local link rewrites can resolve forward references).
        @known_slugs = collect_known_slugs(spec[:outline])

        # Outline-level structure being built.
        @manifest = []

        # Active prose buffer when we're collecting volume preface,
        # part preface, or chapter-rationale prose. `kind` names the
        # buffer's home; lines accumulate in `lines`.
        @buffer       = nil  # nil | { kind: :volume_preface | :part_preface | :chapter_rationale, lines: [...], title: nil }

        # Counters for label assignment.
        @part_n         = 0   # 1-based; reset never (continues across appendices for index display)
        @chapter_n      = 0   # 1-based, global across the volume (matches LaTeX chapter counter)
        @section_n      = 0   # 1-based, resets per chapter (per-chapter segment counter)
        @appendix_n     = 0   # 1-based, ticks across appendix segments
        @in_appendix    = false
      end

      # Process a single walker event.
      def process(item)
        case item[:kind]
        when :volume         then handle_volume(item)
        when :preface        then handle_preface(item)
        when :part           then handle_part(item)
        when :appendices     then handle_appendices(item)
        when :chapter        then handle_chapter(item)
        when :prose, :scope  then handle_prose(item)
        when :image          then handle_image(item)
        when :segment        then handle_segment(item)
        when :missing        then handle_missing(item)
        when :gap            then handle_gap(item)
        end
      end

      # Flush any trailing buffer at end of walk.
      def finalize!
        flush_buffer!
      end

      # Render the index.md content. Structured manifest lives in the YAML
      # frontmatter under `entries:` (Stage 2 consumes this); the markdown
      # body is a human-readable summary of the same data so anyone opening
      # `index.md` can read the volume structure at a glance.
      def render_index
        outline_hash = Digest::SHA256.hexdigest(@spec[:outline].read)[0, 12]
        fm = {
          'title'         => @spec[:title],
          'short_title'   => @spec[:short_title],
          'slug'          => @spec[:slug],
          'major'         => @spec[:major],
          'minor'         => @spec[:minor],
          'patch'         => @spec[:patch],
          'cover_svg'     => @spec[:cover_svg]&.basename.to_s,
          'toc_enabled'   => @spec[:toc_enabled],
          'variant'       => @variant.to_s,
          'generated_at'  => Time.now.utc.strftime('%Y-%m-%dT%H:%M:%SZ'),
          'outline_hash'  => outline_hash,
          'counts' => {
            'parts'      => @part_n,
            'chapters'   => @chapter_n,
            'appendices' => @appendix_n,
          },
          'entries' => @manifest.map { |e| entry_to_yaml_hash(e) },
        }
        require 'yaml' unless defined?(YAML)
        yaml = YAML.dump(fm)
        yaml = yaml.sub(/\A---\s*\n/, '')  # strip leading --- so we add our own

        body = []
        body << "# Build Index — #{@spec[:title]}"
        body << ''
        body << 'Generated assembly manifest. The machine-readable structure'
        body << 'lives in the YAML frontmatter under `entries:`; the summary'
        body << 'below mirrors it for human inspection.'
        body << ''
        @manifest.each { |entry| render_manifest_entry(entry, body) }

        "---\n#{yaml}---\n\n#{body.join("\n")}\n"
      end

      private

      # Convert a manifest entry to a hash with string keys, suitable for
      # YAML serialization. Stage 2 reads these back. Keys are stable;
      # adding a new key here means Stage 2 (and downstream renderers)
      # can rely on its presence.
      def entry_to_yaml_hash(entry)
        h = { 'kind' => entry[:kind].to_s }
        entry.each do |k, v|
          next if k == :kind
          h[k.to_s] = v.is_a?(Pathname) ? v.to_s : v
        end
        h
      end

      def render_manifest_entry(entry, body)
        case entry[:kind]
        when :part
          body << ''
          body << "## Part #{entry[:roman]} — #{entry[:title]}"
          body << ''
        when :appendices
          body << ''
          body << "## Appendices: #{entry[:title]}"
          body << ''
        when :chapter
          body << "### Chapter #{entry[:n]} — #{entry[:title]}"
          body << ''
        when :preface_chunk
          body << "- `#{entry[:chunk]}` — *kind: #{entry[:role]}*, " \
                  "*hash: #{entry[:hash]}*"
        when :rationale_chunk
          body << "- `#{entry[:chunk]}` — *kind: chapter-rationale*, " \
                  "*hash: #{entry[:hash]}*"
        when :segment_chunk
          parts = []
          parts << "*slug: `#{entry[:slug]}`*"
          parts << "*type: #{entry[:type]}*"
          parts << "*label: #{entry[:label]}*"
          parts << "*container: #{entry[:container]}*"
          parts << "*hash: #{entry[:hash]}*"
          body << "- `#{entry[:chunk]}` — #{parts.join(', ')}"
        when :missing
          parts = []
          parts << "*slug: `#{entry[:slug]}`*"
          parts << "*type: #{entry[:type]}*"
          parts << "*label: #{entry[:label]}*"
          parts << "*container: #{entry[:container]}*"
          body << "- *missing* — #{parts.join(', ')} — #{entry[:claim].inspect}"
        when :gap
          body << "- *gap* — #{entry[:description].inspect}"
        end
      end

      # ── event handlers ────────────────────────────────────────────────

      def handle_volume(_item)
        # Walker emits :volume with the title; metadata already lives in
        # mono-meta.yaml so we don't need to redundantly capture it here.
      end

      def handle_preface(item)
        flush_buffer!
        kind = item[:level] == 2 ? :volume_preface : :part_preface
        title = item[:title].to_s.strip
        title = nil if title.empty?
        @buffer = { kind: kind, lines: [], title: title }
      end

      def handle_part(item)
        flush_buffer!
        @part_n += 1
        @manifest << {
          kind: :part,
          n: @part_n,
          roman: roman_numeral(@part_n),
          title: item[:title].to_s,
        }
      end

      def handle_appendices(item)
        flush_buffer!
        @in_appendix = true
        @part_n += 1  # appendix parts still count for outline numbering
        @manifest << {
          kind: :appendices,
          n: @part_n,
          roman: roman_numeral(@part_n),
          title: item[:title].to_s,
        }
      end

      def handle_chapter(item)
        flush_buffer!
        # Implicit chapter (walker auto-inserts when prose precedes the
        # first explicit *Chapter* heading): only counts if it has a
        # title. The walker emits implicit chapters with title:nil when
        # a chapter heading was missing.
        return if item[:implicit] && item[:title].nil?

        @chapter_n += 1
        @section_n  = 0
        @manifest << {
          kind: :chapter,
          n: @chapter_n,
          title: item[:title].to_s,
        }
        # Open a chapter-rationale buffer to capture any prose between
        # this chapter heading and the first segment row. Empty buffers
        # produce no chunk.
        @buffer = { kind: :chapter_rationale, lines: [], title: nil, chapter_n: @chapter_n }
      end

      def handle_prose(item)
        return unless @buffer  # outside any buffer scope — drop silently
        @buffer[:lines] << item[:content]
      end

      def handle_image(_item)
        # SVG→PDF pipeline pending. Defer.
      end

      def handle_segment(item)
        flush_buffer!
        path = item[:path]
        type_label = normalize_type_label(item[:type])

        container = item[:container] == :appendices ? 'appendix-chapter' : 'section'
        label = if container == 'appendix-chapter'
                  @appendix_n += 1
                  Mono::Ingest.alpha_alph(@appendix_n)
                else
                  @section_n += 1
                  "#{@chapter_n}.#{@section_n}"
                end

        source = path.read
        body = Mono::Ingest.strip_yaml_frontmatter(source)
        body = Mono::Ingest.strip_working_notes(body) if @variant == :public

        # Header bumping: segment's authored H1 → H4 (main-matter section) or
        # H3 (appendix chapter). Subheadings follow proportionally.
        bump_offset = container == 'appendix-chapter' ? 2 : 3
        body = Mono::Ingest.bump_headers(body, bump_offset)
        body = Mono::Ingest.rewrite_local_links(body, @known_slugs)
        # Inside-math pipe substitution — `|` and `\|` become `\vert` /
        # `\Vert` so kramdown's table parser doesn't carve a math
        # expression like `$\lVert x \rVert = |y| \cdot |z|$` into
        # spurious table columns when the chunk is later processed in
        # the assembled-markdown context.
        body = Mono::SegmentRenderer.preprocess_math_pipes(body)

        # Pull title out of the (bumped) first heading so the chunk's
        # metadata block can sit right under it. The kramdown converter
        # also needs the type-stripped clean title in the metadata, so
        # the H1 line is preserved verbatim and Title is captured for
        # the renderer to access.
        title_match = body.match(/^(\#{1,6})[ \t]+(.+)$/)
        clean_title = title_match ? title_match[2].sub(/\A#{Regexp.escape(type_label)}:\s*/, '') : item[:claim]

        chunk_text = build_segment_chunk(
          body:        body,
          slug:        item[:slug],
          type_label:  type_label,
          status:      read_segment_status(source),
          stage:       read_segment_stage(source),
          label:       label,
          container:   container,
          title:       clean_title,
        )

        chunk_path = @chunks_dir / "#{item[:slug]}.md"
        chunk_path.write(chunk_text)
        hash = Digest::SHA256.hexdigest(chunk_text)[0, 12]

        @manifest << {
          kind:       :segment_chunk,
          slug:       item[:slug],
          type:       type_label,
          label:      label,
          container:  container,
          chunk:      "chunks/#{chunk_path.basename}",
          hash:       hash,
          source:     path.relative_path_from(ROOT_DIR_FOR_INGEST),
        }
      end

      def handle_missing(item)
        flush_buffer!
        type_label = normalize_type_label(item[:type])
        container = item[:container] == :appendices ? 'appendix-chapter' : 'section'
        label = if container == 'appendix-chapter'
                  @appendix_n += 1
                  Mono::Ingest.alpha_alph(@appendix_n)
                else
                  @section_n += 1
                  "#{@chapter_n}.#{@section_n}"
                end

        @manifest << {
          kind:      :missing,
          slug:      item[:slug],
          type:      type_label,
          label:     label,
          container: container,
          claim:     item[:claim].to_s,
        }
      end

      def handle_gap(item)
        @manifest << { kind: :gap, description: item[:description].to_s }
      end

      # ── buffer flushing ──────────────────────────────────────────────

      def flush_buffer!
        return unless @buffer
        buf = @buffer
        @buffer = nil
        md = buf[:lines].join("\n\n").strip
        return if md.empty?

        # `explicit_title` is the H2/H3 info-suffix the author wrote (or
        # nil when the heading is bare `## *Preface*`); the chunk's
        # `**Title**:` metadata records it only when set, so the assembler
        # can emit `## *Preface*` without a redundant suffix when the
        # author didn't provide one. `display_title` is what shows up as
        # the chunk's H1 — defaulted to "Preface" for the volume-preface
        # chunk since a chunk file needs *some* H1 to scan as standalone.
        case buf[:kind]
        when :volume_preface
          chunk_name = 'volume-preface.md'
          role = 'volume-preface'
          explicit_title = buf[:title]
          display_title  = explicit_title || 'Preface'
        when :part_preface
          chunk_name = "part-#{@part_n}-preface.md"
          role = 'part-preface'
          explicit_title = buf[:title]
          display_title  = nil
        when :chapter_rationale
          chunk_name = "chapter-#{buf[:chapter_n]}-rationale.md"
          role = 'chapter-rationale'
          explicit_title = nil
          display_title  = nil
        else
          return
        end

        chunk_text = build_preface_chunk(
          body: md, role: role,
          display_title: display_title, explicit_title: explicit_title,
        )
        chunk_path = @chunks_dir / chunk_name
        chunk_path.write(chunk_text)
        hash = Digest::SHA256.hexdigest(chunk_text)[0, 12]

        @manifest << {
          kind:  :preface_chunk,
          role:  role,
          chunk: "chunks/#{chunk_name}",
          hash:  hash,
        }
      end

      # ── chunk file rendering ─────────────────────────────────────────

      def build_segment_chunk(body:, slug:, type_label:, status:, stage:, label:, container:, title:)
        meta = [
          "**Slug**: `#{slug}`",
          "**Type**: #{type_label}",
        ]
        meta << "**Status**: #{status}" unless status.empty?
        meta << "**Stage**: #{stage}"   unless stage.empty?
        meta << "**Label**: #{label}"
        meta << "**Container**: #{container}"

        # Insert metadata block immediately after the first heading.
        body_with_meta = body.sub(/^(\#{1,6}[ \t].+\n)/) do
          "#{Regexp.last_match(1)}\n#{meta.join("\n")}\n\n"
        end
        # If no heading was found (shouldn't happen for well-formed segments)
        # prepend the metadata so it's still visible.
        if body_with_meta == body
          body_with_meta = "#{meta.join("\n")}\n\n#{body}"
        end

        body_with_meta
      end

      def build_preface_chunk(body:, role:, display_title:, explicit_title:)
        meta = ["**Role**: #{role}"]
        meta << "**Title**: #{explicit_title}" if explicit_title

        if display_title && role == 'volume-preface'
          "# #{display_title}\n\n#{meta.join("\n")}\n\n#{body}\n"
        else
          "#{meta.join("\n")}\n\n#{body}\n"
        end
      end

      # ── small utilities ──────────────────────────────────────────────

      def collect_known_slugs(outline_path)
        # The walker pre-scan covers the same ground; doing a quick pass
        # over the outline text is cheaper and self-contained.
        slugs = []
        outline_path.read.scan(/\[#([\w-]+)\]\(/) { |m| slugs << m[0] }
        slugs.uniq
      end

      # Normalize the type string from an outline row. OUTLINE.md cells
      # like "Derived + Scope" or "Discussion + Hypothesis" announce a
      # segment that fills two roles; for label/display purposes we use
      # the primary (leftmost) type. `worked example`/`Worked Example`
      # case variants normalize through TYPE_LABEL.
      def normalize_type_label(raw)
        primary = raw.to_s.split('+').first.to_s.strip
        key = primary.downcase
        TYPE_LABEL[key] || primary.split.map(&:capitalize).join(' ')
      end

      def read_segment_status(source)
        fm = parse_segment_frontmatter(source)
        fm['status'].to_s
      end

      def read_segment_stage(source)
        fm = parse_segment_frontmatter(source)
        fm['stage'].to_s
      end

      def parse_segment_frontmatter(source)
        return {} unless source.start_with?("---\n")
        idx = source.index(/^---\s*$/, 4)
        return {} unless idx
        yaml_text = source[4...idx]
        require 'yaml' unless defined?(YAML)
        YAML.safe_load(yaml_text) || {}
      rescue StandardError
        {}
      end

      def roman_numeral(n)
        return n.to_s if n > 50  # guard against runaway counts
        symbols = %w[X IX V IV I]
        values  = [10, 9, 5, 4, 1]
        out = +''
        rem = n
        symbols.each_with_index do |sym, i|
          while rem >= values[i]
            out << sym
            rem -= values[i]
          end
        end
        out
      end
    end

    # Tiny accessor so handle_segment can express path-relative-to-root
    # without each call needing the constant. Set by build-monograph at
    # invocation time.
    ROOT_DIR_FOR_INGEST = Pathname.new(File.expand_path('../../..', __dir__))
  end
end
