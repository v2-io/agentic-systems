#!/usr/bin/env ruby
# frozen_string_literal: true

# bin/naming-aggregate.rb
#
# Aggregates multi-agent naming-vote tables from msc/naming/naming-votes/*.md.
# Parses markdown tables defined in doc/naming-principles.md — supports both
# the 4-column legacy R1 schema (current/new/weight/notes) and the 5-column
# current schema (current/new/category/weight/notes). Both schemas may appear
# in a single run; per-file detection is automatic.
# sums weights per (current-name, new-name-candidate) pair, preserves
# agent-attributed notes, and emits one of three output formats:
#
#   --format=review  — grouped by current-name, with tallies and all notes.
#                      The default. Useful for human review / final judgment.
#   --format=round2  — blind input for Round-2 agents. Sorted
#                      most-popular-first (by aggregate weight) but tallies
#                      are withheld to prevent bandwagon convergence.
#                      Notes retained so round-2 agents can see reasoning.
#   --format=json    — machine-readable full dump. For downstream tooling.
#
# Per the principles file: weight scale is -1 / +1 / +2 / +3. Absence is not a vote.
# Agent-id is the vote-file basename (e.g., `opus-1m.md` → agent `opus-1m`).
#
# Near-duplicate detection: names whose canonical form (lowercase, whitespace
# collapsed, non-alphanumeric stripped) matches another are flagged at the
# top of review output so reviewers can decide whether to merge.
#
# Usage:
#   ruby bin/naming-aggregate.rb                              # review to stdout
#   ruby bin/naming-aggregate.rb --format=round2              # round-2 input
#   ruby bin/naming-aggregate.rb --format=json                # JSON dump
#   ruby bin/naming-aggregate.rb --output=out/review.md       # write to file
#   ruby bin/naming-aggregate.rb --votes-dir=some/other/dir   # non-default dir

require 'json'
require 'optparse'
require 'set'

VoteRecord = Struct.new(:agent, :current, :candidate, :weight, :category, :notes, keyword_init: true)

# --- Parsing --------------------------------------------------------------

PIPE_PLACEHOLDER = ""

def split_row(line)
  trimmed = line.strip
  return nil unless trimmed.start_with?('|') && trimmed.end_with?('|')
  # Protect escaped pipes (\|) so cells containing H_b^{A\|B} etc. parse correctly.
  escaped = trimmed[1..-2].gsub('\\|', PIPE_PLACEHOLDER)
  escaped.split('|').map { |part| part.gsub(PIPE_PLACEHOLDER, '|') }
end

def separator_row?(line)
  !(line =~ /\A\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?\s*\z/).nil?
end

def header_row?(parts)
  return false unless parts.length >= 4
  s = parts[0, 5].map { |p| p.strip.downcase }
  return false unless s[0].include?('current') && s[1].include?('new')
  # 5-col: current/new/category/weight/notes
  if parts.length >= 5 && s[2].include?('categ')
    return :five_col if s[3].include?('weight')
  end
  # 4-col: current/new/weight/notes
  return :four_col if s[2].include?('weight') && s[3]&.include?('note')
  false
end

SKIP_WEIGHT_MARKERS = ['—', '--', '-', '—', 'n/a', 'na', '?', ''].freeze

def parse_weight(cell)
  stripped = cell.to_s.strip
  # Intentional non-vote markers (em-dash, "n/a", etc.) — skip quietly with :skip.
  return :skip if SKIP_WEIGHT_MARKERS.include?(stripped.downcase)
  m = stripped.match(/([+-]?\d+)/)
  m ? m[1].to_i : nil
end

def clean_name(s)
  # Preserve meaningful surrounding marks (backticks, asterisks around symbols)
  # but trim whitespace. Do NOT lowercase — case is often meaningful.
  s.strip
end

def parse_vote_file(path, agent_id)
  records = []
  # Dedupe exact-duplicate rows within a single file. Agents whose runs crash
  # mid-table and resume with an incremental append may re-emit a header row
  # followed by rows they already wrote. Exact-match dedup drops those without
  # warning. Same (current, candidate) with *different* weight or notes is
  # caught later by the aggregator's duplicate-vote warning.
  seen_keys = Set.new
  in_table = false
  schema = :four_col  # default; overridden by header detection
  line_no = 0
  warnings = []

  File.foreach(path, chomp: true) do |line|
    line_no += 1

    if separator_row?(line)
      next
    end

    parts = split_row(line)
    if parts.nil?
      in_table = false
      next
    end

    detected = header_row?(parts)
    if detected
      in_table = true
      schema = detected
      next
    end

    next unless in_table

    if schema == :five_col
      next if parts.length < 5
      current   = clean_name(parts[0])
      candidate = clean_name(parts[1])
      category  = parts[2].strip.empty? ? nil : parts[2].strip
      weight    = parse_weight(parts[3])
      notes     = parts[4..].join('|').strip
    else
      next if parts.length < 4
      current   = clean_name(parts[0])
      candidate = clean_name(parts[1])
      category  = nil
      weight    = parse_weight(parts[2])
      notes     = parts[3..].join('|').strip
    end

    if current.empty? || candidate.empty?
      # Silently skip — these are typically section-header rows (e.g. "| **CORE SLUGS** | | | |")
      # used by some agents to organize their tables. Not errors.
      next
    end
    if weight == :skip
      next
    end
    if weight.nil?
      weight_cell = schema == :five_col ? parts[3] : parts[2]
      warnings << "#{path}:#{line_no}: unparseable weight '#{weight_cell}' — skipped"
      next
    end

    dedup_key = [current, candidate, weight, notes]
    next if seen_keys.include?(dedup_key)
    seen_keys.add(dedup_key)

    records << VoteRecord.new(
      agent: agent_id,
      current: current,
      candidate: candidate,
      weight: weight,
      category: category,
      notes: notes
    )
  end

  warnings.each { |w| $stderr.puts "warning: #{w}" }
  records
end

# --- Aggregation ----------------------------------------------------------

AggregateResult = Struct.new(:agg, :merged_variants, keyword_init: true)

def aggregate(records)
  # Aggregate by canonical key (lowercased, alphanumerics-only) so that the same
  # concept voted on under format-variants — `satisfaction gap` / `Satisfaction gap` /
  # `"satisfaction gap"` / `#satisfaction-gap` — accumulates conviction rather than
  # splitting it. After aggregation, each canonical group is mapped back to a
  # display form: the most-frequently-occurring original variant, ties broken by
  # length (longer = more informative).
  by_canon = {}
  display_counts = Hash.new { |h, k| h[k] = Hash.new(0) }
  dup_warnings = []

  records.each do |r|
    canon_key = [canonical(r.current), canonical(r.candidate)]
    display_counts[canon_key[0]][r.current] += 1
    display_counts[canon_key[1]][r.candidate] += 1

    by_canon[canon_key] ||= { total: 0, votes: [] }

    prior = by_canon[canon_key][:votes].find { |v| v[:agent] == r.agent }
    if prior
      dup_warnings << "duplicate vote: agent #{r.agent} voted twice on canonical [#{canon_key[0]}] → [#{canon_key[1]}] " \
                      "(prior #{prior[:weight]}, new #{r.weight}); summing both"
    end

    by_canon[canon_key][:total] += r.weight
    by_canon[canon_key][:votes] << { agent: r.agent, weight: r.weight, category: r.category, notes: r.notes }
  end

  dup_warnings.each { |w| $stderr.puts "warning: #{w}" }

  # Display form IS the canonical form. Cosmetic variation (case, quotes,
  # leading hash, internal hyphens) was never voted on; consolidating to the
  # canonical removes noise from both aggregation and rendering.

  # Variants reportable: canonical → list of distinct original variants that
  # merged into it (sorted by within-canonical popularity, then alphabetic).
  merged_variants = display_counts
                      .select { |canon, forms| forms.size > 1 || (forms.size == 1 && forms.keys.first != canon) }
                      .transform_values { |forms| forms.sort_by { |form, count| [-count, form] }.map(&:first) }

  agg = {}
  by_canon.each do |(canon_current, canon_candidate), data|
    agg[[canon_current, canon_candidate]] = data
  end

  AggregateResult.new(agg: agg, merged_variants: merged_variants)
end

def group_by_current(agg)
  groups = {}
  agg.each do |(current, candidate), data|
    groups[current] ||= []
    groups[current] << {
      candidate: candidate,
      total: data[:total],
      votes: data[:votes]
    }
  end
  groups.each_value { |alts| alts.sort_by! { |a| -a[:total] } }
  groups
end

# Project-specific slug-prefix vocabulary, mirroring the role-prefix discipline
# under `bin/align-slug`. These short forms are the prefixes that actually
# appear in current slugs ({prefix}-{subject-noun}); stripping them lets
# `#def-satisfaction-gap`, `#satisfaction-gap`, and `satisfaction gap` consolidate.
# Long-form type words (`definition`, `observation`, etc.) are NOT stripped:
# they collide with subject-noun content (`observation-function` defines the
# observation-function map; stripping `observation-` would lose meaning).
SLUG_PREFIXES = %w[
  post def scope form der deriv corr hyp norm emp obs disc meas schema example result detail sketch aside
].sort_by { |p| -p.length }.freeze

# Compound terms that retain their internal hyphen rather than becoming two
# separate words after the punct-to-space normalization. These are domain
# compounds where the hyphenation carries meaning (`no-go theorem` is one
# concept, not two). Add by scanning the merged-variants output; case-insensitive.
COMPOUND_EXCEPTIONS = %w[
  no-go
  goal-blind
  Pearl-blanket
  Friston-blanket
  Pearl-Level
  Cauchy-FE
  Lohmiller-Slotine
].freeze

# Acronyms preserved as uppercase in the canonical/display form. Word-boundary
# matching means `\bai\b` matches `ai-agent` but not `aim` or `rain`. Sorted
# longest-first so `POMDP` matches before the shorter `MDP`.
ACRONYMS = %w[
  POMDP RLHF OODA CMCL AAD ASF TST CIY DAG LMI MDL FEP EFE BDI LLM RAG AGI API CLI URL MDP IB UI KL AI ML RL
].sort_by { |a| -a.length }.freeze

def canonical(name)
  # Canonical form used for both aggregation key and display. Rule:
  #   1. Protect compound exceptions (`no-go`, `goal-blind`).
  #   2. Convert all ASCII punctuation to spaces (preserves non-ASCII Greek
  #      letters and math symbols as substantive content).
  #   3. Collapse whitespace, trim, lowercase ASCII.
  #   4. Strip a leading project type-prefix (`def`, `disc`, etc.) when
  #      present and the remainder is non-trivial.
  #   5. Restore compound exceptions.
  # Cosmetic variation in source votes (case, surrounding quotes, leading
  # hash, internal hyphens) collapses to a single canonical form — the
  # naming round had no votes specifically about case or punctuation.
  s = name.dup

  formula_phs = {}
  s = s.gsub(/\$[^$]+\$/) do |match|
    ph = "FRM#{formula_phs.length}"
    formula_phs[ph] = match
    ph
  end

  compound_phs = {}
  COMPOUND_EXCEPTIONS.each_with_index do |compound, i|
    ph = "CMP#{i}"
    compound_phs[ph] = compound.downcase
    s = s.gsub(/#{Regexp.escape(compound)}/i, ph)
  end

  acronym_phs = {}
  ACRONYMS.each_with_index do |acro, i|
    ph = "ACR#{i}"
    acronym_phs[ph] = acro
    s = s.gsub(/\b#{acro}\b/i, ph)
  end

  s = s.gsub(/[[:punct:]]+/, ' ')
  s = s.gsub(/\s+/, ' ').strip.downcase

  SLUG_PREFIXES.each do |prefix|
    next unless s.start_with?("#{prefix} ")
    remainder = s[(prefix.length + 1)..]
    if remainder.length >= 3
      s = remainder
      break
    end
  end

  compound_phs.each { |ph, original| s = s.gsub(ph.downcase, original) }
  acronym_phs.each  { |ph, original| s = s.gsub(ph.downcase, original) }
  formula_phs.each  { |ph, original| s = s.gsub(ph.downcase, original) }
  s
end

# --- Rendering ------------------------------------------------------------

def signed(n)
  n >= 0 ? "+#{n}" : n.to_s
end

def category_tally(alts)
  cats = alts.flat_map { |a| a[:votes].map { |v| v[:category] } }.compact
  return nil if cats.empty?
  cats.tally.sort_by { |_, count| -count }.map { |cat, count| "#{cat} × #{count}" }.join(', ')
end

def render_review(result, records)
  agg = result.agg
  merged = result.merged_variants
  groups = group_by_current(agg)
  agents = records.map(&:agent).uniq.sort

  out = []
  out << '# Naming Vote Aggregation — Review'
  out << ''
  out << "**Agents:** #{agents.join(', ')} (#{agents.length} total)"
  out << "**Total vote rows:** #{records.length}"
  out << "**Distinct (current, candidate) pairs:** #{agg.length}"
  out << "**Distinct current-names voted on:** #{groups.length}"
  out << "**Merged display-form variants (post-canonicalization):** #{merged.length}" if merged.any?
  out << ''

  unless merged.empty?
    out << '## Merged display-form variants'
    out << ''
    out << 'These names were collapsed to a canonical bucket (lowercased / alphanumerics-only) so format-variant votes consolidate. The chosen display form is the most-frequently-voted original (ties broken by length); other variants are listed for traceability.'
    out << ''
    merged.sort_by { |canon, _| canon }.each do |_canon, variants|
      next if variants.length < 2
      chosen = variants.first
      others = variants.drop(1)
      out << "- `#{chosen}` ← merged from: #{others.map { |v| "`#{v}`" }.join(', ')}"
    end
    out << ''
  end

  out << '---'
  out << ''
  out << "Groups are sorted by their *top alternative's* aggregate weight (descending). Within each group, alternatives are sorted by aggregate weight. Explicit keeps (current = candidate) are marked ⭑. Rejected candidates (total < 0) are marked ✗."
  out << ''

  sorted_groups = groups.sort_by do |current, alts|
    [-alts.map { |a| a[:total] }.max, current]
  end

  sorted_groups.each do |current, alts|
    out << "## `#{current}`"
    out << ''
    out << '| candidate | aggregate | votes |'
    out << '|---|---:|---|'
    alts.each do |alt|
      marker = if alt[:candidate] == current
                 ' ⭑'
               elsif alt[:total] < 0
                 ' ✗'
               else
                 ''
               end
      vote_str = alt[:votes]
                   .sort_by { |v| [-v[:weight], v[:agent]] }
                   .map { |v| "#{v[:agent]} #{signed(v[:weight])}" }
                   .join(', ')
      out << "| `#{alt[:candidate]}`#{marker} | #{signed(alt[:total])} | #{vote_str} |"
    end
    out << ''

    tally = category_tally(alts)
    out << "_category: #{tally}_" if tally

    any_notes = alts.any? { |a| a[:votes].any? { |v| !v[:notes].empty? } }
    if any_notes
      out << '' if tally
      out << '**Notes:**'
      out << ''
      alts.each do |alt|
        alt[:votes].each do |v|
          next if v[:notes].empty?
          out << "- `#{alt[:candidate]}` — **#{v[:agent]} (#{signed(v[:weight])}):** #{v[:notes]}"
        end
      end
      out << ''
    else
      out << '' if tally
    end
  end

  out.join("\n") + "\n"
end

def render_round2(result, records)
  agg = result.agg
  groups = group_by_current(agg)
  agents = records.map(&:agent).uniq.sort

  sorted_groups = groups.sort_by do |current, alts|
    [-alts.map { |a| a[:total] }.max, current]
  end

  out = []
  out << '# Naming Vote — Round 2 Input (Blind)'
  out << ''
  out << "**Round 1 agents:** #{agents.join(', ')}"
  out << ''
  out << 'This is the aggregated candidate list from Round 1, sorted most-popular to least-popular (tallies withheld to prevent bandwagon convergence). Each entry shows a current-name, the alternatives proposed across agents (including explicit keeps), and the reasoning notes from Round 1 agents.'
  out << ''
  out << '**Your task:** review each entry and cast your own votes following `doc/naming-principles.md`. You may add new candidates not on this list if you discover one during review. Do not read other Round-1 vote files directly — this aggregated summary is your input. Write your votes to `msc/naming/naming-votes/{your-agent-id}.md`.'
  out << ''
  out << '---'
  out << ''

  sorted_groups.each_with_index do |(current, alts), i|
    out << "## #{i + 1}. `#{current}`"
    out << ''
    candidates_line = alts.map { |a| "`#{a[:candidate]}`" }.join(', ')
    out << "**Alternatives proposed:** #{candidates_line}"
    out << ''

    tally = category_tally(alts)
    out << "_category: #{tally}_" << '' if tally

    alts.each do |alt|
      alt[:votes].each do |v|
        next if v[:notes].empty?
        out << "- `#{alt[:candidate]}` — **#{v[:agent]}:** #{v[:notes]}"
      end
    end
    out << ''
  end

  out.join("\n") + "\n"
end

def render_compact(result, records)
  agg = result.agg
  groups = group_by_current(agg)
  agents = records.map(&:agent).uniq.sort

  out = []
  out << '# Naming Vote Aggregation — Compact Table'
  out << ''
  out << "**Agents:** #{agents.length} (#{agents.join(', ')})"
  out << "**Total vote rows:** #{records.length}"
  out << "**Distinct (current, candidate) pairs:** #{agg.length}"
  out << "**Distinct current-names voted on:** #{groups.length}"
  out << ''
  out << 'Single-table view: one row per (original, candidate) pair, with aggregate weight. Rows for the same `original` are grouped adjacently; the original cell is shown only on the first row of each group; groups are sorted by their top alternative\'s aggregate weight (descending). The first row of each group is the **winning** candidate (bolded). Where candidate = original the cell shows `_(keep)_`, suffixed with ⭑ if at least one vote on that row used the `canonicalize` category. Net-rejected candidates (aggregate < 0) prefixed with ✗. Category and per-agent notes elided — see `--format=review` for those.'
  out << ''
  out << '| original | candidate | aggregate |'
  out << '|---|---|---:|'

  sorted_groups = groups.sort_by do |current, alts|
    [-alts.map { |a| a[:total] }.max, current]
  end

  pipe_safe = ->(cell) { cell.to_s.gsub('|', '\\|') }

  # Category suffix discipline: surface category mix on non-keep candidates.
  # `rename` is the default action (no suffix, avoids clutter on the common case);
  # `add-alias`, `canonicalize`, `name-unnamed`, and any non-canonical category
  # show as a suffix. Mixed-category pairs show the full tally so the
  # disagreement-on-action is visible (rename and add-alias mean different
  # downstream moves; collapsing them into one weight loses signal).
  category_suffix = ->(votes) {
    cats = votes.map { |v| v[:category] }.compact
    return '' if cats.empty?
    tally = cats.tally.sort_by { |_, c| -c }
    if tally.size == 1
      cat = tally[0][0]
      return '' if cat.downcase == 'rename'
      " [#{cat}]"
    else
      " [#{tally.map { |c, n| "#{c} × #{n}" }.join(', ')}]"
    end
  }

  sorted_groups.each do |current, alts|
    alts.each_with_index do |alt, idx|
      is_keep = (alt[:candidate] == current)
      is_winner = idx.zero?
      has_canon_vote = alt[:votes].any? { |v| v[:category]&.downcase == 'canonicalize' }

      candidate_cell = if is_keep
                         "_(keep)_#{has_canon_vote ? ' ⭑' : ''}"
                       else
                         "#{pipe_safe.call(alt[:candidate])}#{category_suffix.call(alt[:votes])}"
                       end
      candidate_cell = "✗ #{candidate_cell}" if alt[:total] < 0 && !is_keep
      candidate_cell = "**#{candidate_cell}**" if is_winner

      original_cell = idx.zero? ? pipe_safe.call(current) : ''
      out << "| #{original_cell} | #{candidate_cell} | #{signed(alt[:total])} |"
    end
  end

  out << ''
  out.join("\n") + "\n"
end

def render_json(result, records)
  agg = result.agg
  payload = {
    meta: {
      agents: records.map(&:agent).uniq.sort,
      total_rows: records.length,
      distinct_pairs: agg.length,
      distinct_currents: agg.keys.map(&:first).uniq.length,
      merged_variants: result.merged_variants.transform_values { |vs| vs }
    },
    pairs: agg.map do |(current, candidate), data|
      cats = data[:votes].map { |v| v[:category] }.compact
      {
        current: current,
        candidate: candidate,
        total_weight: data[:total],
        category_tally: cats.empty? ? nil : cats.tally,
        votes: data[:votes].map { |v| { agent: v[:agent], weight: v[:weight], category: v[:category], notes: v[:notes] } }
      }
    end.sort_by { |p| [p[:current], -p[:total_weight]] }
  }
  JSON.pretty_generate(payload) + "\n"
end

# --- Main -----------------------------------------------------------------

options = {
  format: 'review',
  votes_dir: 'msc/naming/naming-votes',
  output: '-'
}

OptionParser.new do |opts|
  opts.banner = 'Usage: naming-aggregate.rb [options]'

  opts.on('--format=FORMAT', %w[round2 review compact json],
          'Output format: round2 (blind), review (with tallies/notes), compact (per-current tables, no notes), or json (default: review)') do |f|
    options[:format] = f
  end

  opts.on('--votes-dir=DIR', 'Directory containing *.md vote files (default: msc/naming/naming-votes)') do |d|
    options[:votes_dir] = d
  end

  opts.on('--output=PATH', 'Output path (default: stdout)') do |p|
    options[:output] = p
  end

  opts.on('-h', '--help', 'Show this help') do
    puts opts
    exit
  end
end.parse!

vote_files = Dir.glob(File.join(options[:votes_dir], '*.md')).sort
abort "No vote files found in #{options[:votes_dir]}" if vote_files.empty?

records = []
vote_files.each do |path|
  agent_id = File.basename(path, '.md')
  file_records = parse_vote_file(path, agent_id)
  $stderr.puts "#{agent_id}: #{file_records.length} vote rows"
  records.concat(file_records)
end

agg = aggregate(records)

output = case options[:format]
         when 'review'  then render_review(agg, records)
         when 'round2'  then render_round2(agg, records)
         when 'compact' then render_compact(agg, records)
         when 'json'    then render_json(agg, records)
         end

if options[:output] == '-'
  print output
else
  File.write(options[:output], output)
  $stderr.puts "Wrote #{options[:output]} (#{output.bytesize} bytes)"
end
