#!/usr/bin/env ruby
# frozen_string_literal: true

# bin/naming-aggregate.rb
#
# Aggregates multi-agent naming-vote tables from msc/naming/naming-votes/*.md.
# Parses the four-column markdown tables defined in msc/naming-principles.md,
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
# Per the principles file: weight scale is -1 / +1 / +3. Absence is not a vote.
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

VoteRecord = Struct.new(:agent, :current, :candidate, :weight, :notes, keyword_init: true)

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
  s = parts[0, 4].map { |p| p.strip.downcase }
  s[0].include?('current') && s[1].include?('new') &&
    s[2].include?('weight') && s[3].include?('note')
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
  line_no = 0
  warnings = []

  File.foreach(path, chomp: true) do |line|
    line_no += 1

    if separator_row?(line)
      # Separator between header and body; stay in current state
      next
    end

    parts = split_row(line)
    if parts.nil?
      in_table = false
      next
    end

    if header_row?(parts)
      in_table = true
      next
    end

    next unless in_table
    next if parts.length < 4

    current   = clean_name(parts[0])
    candidate = clean_name(parts[1])
    weight    = parse_weight(parts[2])
    # Rejoin any trailing fields in case notes contain unescaped pipes.
    notes     = parts[3..].join('|').strip

    if current.empty? || candidate.empty?
      # Silently skip — these are typically section-header rows (e.g. "| **CORE SLUGS** | | | |")
      # used by some agents to organize their tables. Not errors.
      next
    end
    if weight == :skip
      # Intentional non-vote (em-dash, "n/a"). Informational only.
      next
    end
    if weight.nil?
      warnings << "#{path}:#{line_no}: unparseable weight '#{parts[2]}' — skipped"
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
      notes: notes
    )
  end

  warnings.each { |w| $stderr.puts "warning: #{w}" }
  records
end

# --- Aggregation ----------------------------------------------------------

def aggregate(records)
  agg = {}
  dup_warnings = []

  records.each do |r|
    key = [r.current, r.candidate]
    agg[key] ||= { total: 0, votes: [] }

    # Warn if same agent voted twice on the same pair
    prior = agg[key][:votes].find { |v| v[:agent] == r.agent }
    if prior
      dup_warnings << "duplicate vote: agent #{r.agent} voted twice on [#{r.current}] → [#{r.candidate}] " \
                      "(prior #{prior[:weight]}, new #{r.weight}); summing both"
    end

    agg[key][:total] += r.weight
    agg[key][:votes] << { agent: r.agent, weight: r.weight, notes: r.notes }
  end

  dup_warnings.each { |w| $stderr.puts "warning: #{w}" }
  agg
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

def canonical(name)
  # For near-duplicate detection only; don't use for aggregation keys.
  name.downcase.gsub(/[^a-z0-9]+/, '').strip
end

def near_duplicates(agg)
  # Groups of current-names whose canonical form collides
  by_canon = Hash.new { |h, k| h[k] = Set.new }
  agg.each_key do |(current, _)|
    by_canon[canonical(current)].add(current)
  end
  by_canon.values.select { |names| names.length > 1 }.map(&:to_a)
end

# --- Rendering ------------------------------------------------------------

def signed(n)
  n >= 0 ? "+#{n}" : n.to_s
end

def render_review(agg, records)
  groups = group_by_current(agg)
  agents = records.map(&:agent).uniq.sort
  dups = near_duplicates(agg)

  out = []
  out << '# Naming Vote Aggregation — Review'
  out << ''
  out << "**Agents:** #{agents.join(', ')} (#{agents.length} total)"
  out << "**Total vote rows:** #{records.length}"
  out << "**Distinct (current, candidate) pairs:** #{agg.length}"
  out << "**Distinct current-names voted on:** #{groups.length}"
  out << ''

  unless dups.empty?
    out << '## ⚠ Possible near-duplicates (differ only by case/whitespace/punctuation)'
    out << ''
    out << 'These current-names have collisions under canonical form; consider whether to merge manually before landing decisions.'
    out << ''
    dups.each { |names| out << "- #{names.map { |n| "`#{n}`" }.join(' ↔ ') }" }
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

    any_notes = alts.any? { |a| a[:votes].any? { |v| !v[:notes].empty? } }
    if any_notes
      out << '**Notes:**'
      out << ''
      alts.each do |alt|
        alt[:votes].each do |v|
          next if v[:notes].empty?
          out << "- `#{alt[:candidate]}` — **#{v[:agent]} (#{signed(v[:weight])}):** #{v[:notes]}"
        end
      end
      out << ''
    end
  end

  out.join("\n") + "\n"
end

def render_round2(agg, records)
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
  out << '**Your task:** review each entry and cast your own votes following `msc/naming-principles.md`. You may add new candidates not on this list if you discover one during review. Do not read other Round-1 vote files directly — this aggregated summary is your input. Write your votes to `msc/naming/naming-votes/{your-agent-id}.md`.'
  out << ''
  out << '---'
  out << ''

  sorted_groups.each_with_index do |(current, alts), i|
    out << "## #{i + 1}. `#{current}`"
    out << ''
    candidates_line = alts.map { |a| "`#{a[:candidate]}`" }.join(', ')
    out << "**Alternatives proposed:** #{candidates_line}"
    out << ''

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

def render_json(agg, records)
  result = {
    meta: {
      agents: records.map(&:agent).uniq.sort,
      total_rows: records.length,
      distinct_pairs: agg.length,
      distinct_currents: agg.keys.map(&:first).uniq.length,
      near_duplicates: near_duplicates(agg)
    },
    pairs: agg.map do |(current, candidate), data|
      {
        current: current,
        candidate: candidate,
        total_weight: data[:total],
        votes: data[:votes]
      }
    end.sort_by { |p| [p[:current], -p[:total_weight]] }
  }
  JSON.pretty_generate(result) + "\n"
end

# --- Main -----------------------------------------------------------------

options = {
  format: 'review',
  votes_dir: 'msc/naming-votes',
  output: '-'
}

OptionParser.new do |opts|
  opts.banner = 'Usage: naming-aggregate.rb [options]'

  opts.on('--format=FORMAT', %w[round2 review json],
          'Output format: round2 (blind), review (with tallies), or json (default: review)') do |f|
    options[:format] = f
  end

  opts.on('--votes-dir=DIR', 'Directory containing *.md vote files (default: msc/naming-votes)') do |d|
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
         when 'review' then render_review(agg, records)
         when 'round2' then render_round2(agg, records)
         when 'json'   then render_json(agg, records)
         end

if options[:output] == '-'
  print output
else
  File.write(options[:output], output)
  $stderr.puts "Wrote #{options[:output]} (#{output.bytesize} bytes)"
end
