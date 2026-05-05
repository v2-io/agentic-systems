#!/usr/bin/env ruby
# frozen_string_literal: true

# bin/naming-r2-aggregate
#
# Round-2 vote aggregator. Combines:
#   - R1 evidence (master-list-curated.json) compressed to a single synthetic
#     voter at R2 scale ({+2, +1, 0, -1}) per candidate
#   - The six R2 voter cards (round-2-cards/*.md)
#   - Substance-discount per R2 vote (Jaccard novelty against the rationale
#     bullet on the voter's card; that bullet is the surface the voter could
#     have paraphrased)
#
# Design choices and their reasoning:
#
# *R1 → single synthetic voter.* Joseph's directive: R1's collective verdict
# enters R2 aggregation as one entity-equivalent vote, not as N re-counted
# voters. The candidate-level R1 data (per-agent weights on R1's +3..-3 scale,
# category tallies, consolidated rationale) is the input; the synthesis maps
# to R2's tighter scale {+2, +1, 0, -1}.
#
# *No substance-discount on R1.* The synthetic R1 vote IS the prior consensus,
# not a fresh independent take. The R2 cards' bullet rationales were derived
# from R1's consolidated_rationale, so substance-discounting R1 against the
# cards would zero out the very signal we're trying to preserve. Substance-
# discount is for R2 voters specifically, who were instructed to bring NEW
# reasoning rather than recap the corpus.
#
# *Voters kept separate, not collapsed by architecture.* opus-r2b/opus-r2c
# and sonnet-r2b/sonnet-r2c voted on overlapping-but-not-identical subsets
# under different methodologies (consolidation-checkpoint vs no). Treating
# them as four distinct voters preserves coverage; the architectural-overlap
# signal is surfaced separately in the detail view (so 4 voters agreeing
# from 2 architectures is distinguishable from 4 voters from 4 architectures).
#
# *Multi-R2-voter scope only (≥2 R2 voters).* Single-R2-voter targets get
# parsed but excluded from the v0 outputs. This is the directive — scope
# the first pass to where multi-voter signal actually exists.
#
# *Two output files.* The table view is for skim and pattern recognition;
# the detail view is the artifact Joseph actually decides from. They're
# generated in one pass to keep them in sync.
#
# R1 synthesis rules (applied per candidate):
#   n  = number of distinct R1 agents who voted on this candidate
#   m  = mean R1 weight (R1 scale: +3..-3)
#   d  = max(category_tally) / sum(category_tally)
#
#   if n == 0:                                          → null (no R1 evidence)
#   if n ≥ 3 and m ≥ 2.0 and d ≥ 0.6:                   → +2 (strong consensus)
#   if (n ≥ 2 and m ≥ 0.5) or (n == 1 and weight ≥ 2):  → +1 (positive signal)
#   if m ≤ -0.5 or (n == 1 and weight ≤ -2):            → -1 (negative-leaning)
#   else:                                               →  0 (weak/mixed)
#
# These thresholds are a defensible prior, not empirically calibrated. The
# detail view shows the raw R1 inputs alongside the synthesized vote so
# every synthesis is auditable in a glance. Tune from observed surprises.
#
# Substance factor for votes (R2 voters; R1 synth gets factor=1 as a single
# entity-equivalent vote without per-vote substance assessment):
#   tokens(s)     = lowercased s, punctuation stripped, stopwords removed
#   novelty       = 1 - Jaccard(tokens(note), tokens(card-bullet))
#   length_factor = min(1.0, note_chars / 30.0)
#   factor        = length_factor × (1.0 + novelty)        ∈ [0, 2]
#   substance     = raw_weight × factor
#
# Factor shape: empty note → 0 (button-click is no signal); 30+ char paraphrase
# → 1 (the vote-act is a judgment, raw weight is the right baseline); 30+ char
# fully-novel rationale → 2 (new reasoning amplifies). For negative votes the
# same shape applies: -1 with empty note → 0; -1 with novel rationale → -2
# (amplified rejection). 30-char threshold matches the project's existing
# "substantive notes" convention.
#
# Usage:
#   ruby bin/naming-r2-aggregate                                # write defaults
#   ruby bin/naming-r2-aggregate --limit=10                     # first 10 multi-voter targets only
#   ruby bin/naming-r2-aggregate --min-r2-voters=3              # only ≥3-voter targets
#   ruby bin/naming-r2-aggregate --table-out=path --detail-out=path

require 'json'
require 'optparse'
require 'set'
require 'fileutils'
require 'time'

DEFAULT_MASTER       = 'msc/naming/master-list-curated.json'
DEFAULT_CARDS_DIR    = 'msc/naming/round-2-cards'
DEFAULT_TABLE_OUT    = 'msc/naming/r2-aggregate-table.md'
DEFAULT_DETAIL_OUT   = 'msc/naming/r2-aggregate-detail.md'
DEFAULT_PATTERNS_OUT = 'msc/naming/r2-patterns.md'

options = {
  master:                     DEFAULT_MASTER,
  cards_dir:                  DEFAULT_CARDS_DIR,
  table_out:                  DEFAULT_TABLE_OUT,
  detail_out:                 DEFAULT_DETAIL_OUT,
  patterns_out:               DEFAULT_PATTERNS_OUT,
  min_r2_voters:              2,
  include_uncontested_keeps:  false,
  limit:                      nil,
  verbose:                    false
}

OptionParser.new do |opts|
  opts.banner = 'Usage: bin/naming-r2-aggregate [options]'
  opts.on('--master=PATH', "Master-list curated JSON (default #{DEFAULT_MASTER})") { |p| options[:master] = p }
  opts.on('--cards-dir=PATH', "Cards directory (default #{DEFAULT_CARDS_DIR})") { |p| options[:cards_dir] = p }
  opts.on('--table-out=PATH', "Table output path (default #{DEFAULT_TABLE_OUT})") { |p| options[:table_out] = p }
  opts.on('--detail-out=PATH', "Detail output path (default #{DEFAULT_DETAIL_OUT})") { |p| options[:detail_out] = p }
  opts.on('--patterns-out=PATH', "Patterns output path (default #{DEFAULT_PATTERNS_OUT})") { |p| options[:patterns_out] = p }
  opts.on('--min-r2-voters=N', Integer, 'Minimum R2 voter count for inclusion (default 2)') { |n| options[:min_r2_voters] = n }
  opts.on('--include-uncontested-keeps', 'Include targets with exactly one candidate (the current name) and no write-ins. Default: filter out — these need no decision.') { options[:include_uncontested_keeps] = true }
  opts.on('--show-all', 'Show every target that has any vote (R1 or R2). Equivalent to --min-r2-voters=0 --include-uncontested-keeps. The implicit no-vote filter still applies — targets with literally zero votes anywhere are still skipped.') do
    options[:min_r2_voters] = 0
    options[:include_uncontested_keeps] = true
  end
  opts.on('--limit=N', Integer, 'Limit output to first N matching targets (debug)') { |n| options[:limit] = n }
  opts.on('--verbose', 'Print parse / match diagnostics to stderr') { options[:verbose] = true }
  opts.on('-h', '--help') { puts opts; exit }
end.parse!

# ----------------------------------------------------------------------------
# Tokenization for novelty computation. Stopwords are conservative — we drop
# only the most common function words; theoretical-vocabulary terms stay since
# they're often the load-bearing signal in a note (e.g., "directed separation"
# overlap matters; "the" overlap doesn't).
# ----------------------------------------------------------------------------

STOPWORDS = %w[
  a an the and or but if then else of to in on at by for with as is are was
  were be been being am do does did this that these those it its from into
  about across over under between among via not no nor than so such which
  who whom whose what where when why how can could should would may might
  will shall must have has had having get gets got also too just only even
  any all some most more less very much one two three first second third
  i you he she we they me him her us them my your his their our its
].to_set.freeze

def tokenize(text)
  return Set.new if text.nil? || text.empty?
  # Lowercase, strip punctuation, split on whitespace, drop stopwords.
  text.downcase
      .gsub(/[^\p{L}\p{N}\s]/u, ' ')
      .split(/\s+/)
      .reject { |w| w.empty? || STOPWORDS.include?(w) }
      .to_set
end

def jaccard(a, b)
  return 0.0 if a.empty? && b.empty?
  return 0.0 if a.empty? || b.empty?
  inter = (a & b).size
  union = (a | b).size
  return 0.0 if union.zero?
  inter.to_f / union
end

def novelty(note, bullet)
  1.0 - jaccard(tokenize(note), tokenize(bullet))
end

def substance_score(raw_weight, novelty, note_chars, bullet_chars, top_pick: false, category: nil)
  return 0.0 if raw_weight.nil? || raw_weight.zero?
  return 0.0 if note_chars.zero?
  # Smooth substance factor, two tunables, plus two categorical 1.2× multipliers:
  #   relative_length = note_chars / bullet_chars  (capped at 1; no extra credit for verbosity)
  #   effort          = min(1, relative_length)
  #   factor          = (0.7 + 0.3 × effort) × (1.0 + novelty)
  #   factor         *= 1.2 if top_pick                    (voter chose this when forced)
  #   factor         *= 1.2 if category == 'canonicalize'  (excavated-from-prose evidence)
  #
  # Properties:
  #   no note          → 0      (special-cased above; nullify)
  #   fragment + match → 0.7    (small penalty)
  #   bandwagon        → 1.0    (full effort, no novelty — vote at face value)
  #   thoughtful       → 2.0    (full effort + fully novel — full amplification)
  #   thoughtful + top-pick                         → 2.4
  #   thoughtful + canonicalize                     → 2.4
  #   thoughtful + top-pick + canonicalize          → 2.88
  #   write-in         → 2.0+   (no bullet → effort=1, novelty=1 by construction;
  #                              lands at thoughtful naturally, no extra multiplier)
  #   -1 with novel rationale → -2.0  (amplified rejection, matching spec)
  #
  # Top-pick × 1.2 rationale: top-pick is "if exactly one had to land, this one."
  # The data shows top-pick acts as a tiebreaker in 20/20 cases where a voter
  # has multiple +2s on a target; elsewhere it's mostly redundant with +2. The
  # multiplier captures the tiebreaker signal without distorting the common case.
  #
  # Canonicalize × 1.2 rationale: per naming-principles.md, canonicalize means
  # "the phrase is already organically in the prose" — empirical evidence the
  # name fits, beyond just one voter's preference. Excavated-from-prose votes
  # carry stronger fit-signal than invented-rename votes.
  #
  # Length is only meaningful relative to the bullet the voter was responding
  # to. Token-Jaccard novelty conflates true paraphrase ("same idea, different
  # words") with genuine novelty — for this corpus we treat that as acceptable
  # noise (rephrase-of-known-argument is itself signal of engagement, and the
  # cold-start protocol minimized cross-voter paraphrase). Embeddings would
  # distinguish the two if it ever matters more.
  relative_length = bullet_chars.positive? ? note_chars.to_f / bullet_chars : 1.0
  effort = [1.0, relative_length].min
  factor = (0.7 + 0.3 * effort) * (1.0 + novelty)
  factor *= 1.2 if top_pick
  factor *= 1.2 if category == 'canonicalize'
  raw_weight * factor
end

# ----------------------------------------------------------------------------
# R1 → synthetic voter mapping. Returns {weight:, rationale:, n:, mean:,
# category_dom:, raw:} for inspection. raw[:weights] is the per-agent weight
# list so the detail view can show the R1 distribution that fed the synthesis.
# ----------------------------------------------------------------------------

def synthesize_r1(candidate)
  votes = candidate['votes'] || []
  agents = votes.map { |v| v['agent'] }.uniq
  n = agents.size
  return { weight: nil, n: 0, mean: nil, category_dom: nil, raw: { weights: [], rationale: nil } } if n.zero?

  weights = votes.map { |v| v['weight'].to_i }
  mean_w = weights.sum.to_f / weights.size
  category_tally = candidate['category_tally'] || {}
  total_cat = category_tally.values.sum
  category_dom = total_cat.zero? ? 0.0 : (category_tally.values.max.to_f / total_cat)

  synth =
    if n >= 3 && mean_w >= 2.0 && category_dom >= 0.6
      +2
    elsif (n >= 2 && mean_w >= 0.5) || (n == 1 && weights.first >= 2)
      +1
    elsif mean_w <= -0.5 || (n == 1 && weights.first <= -2)
      -1
    else
      0
    end

  rationale = candidate['consolidated_rationale']
  if rationale.nil? || rationale.strip.empty?
    # Fallback: stitch a few representative R1 notes together if no consolidated
    # rationale was authored. Surfaces the underlying R1 reasoning without
    # claiming editorial synthesis that wasn't done.
    samples = votes
              .select { |v| !(v['notes'].to_s.strip.empty?) }
              .first(3)
              .map { |v| "  • [#{v['agent']} #{format_weight(v['weight'])}] #{v['notes'].to_s.strip}" }
    rationale = samples.empty? ? nil : "(unsynthesized — sampled from R1 notes)\n#{samples.join("\n")}"
  end

  {
    weight: synth,
    n: n,
    mean: mean_w,
    category_dom: category_dom,
    raw: {
      weights: weights,
      category_tally: category_tally,
      rationale: rationale,
      total_weight: candidate['total_weight'],
      is_keep: candidate['is_keep'],
      provenance: candidate['canonicalize_provenance']
    }
  }
end

def format_weight(w)
  return '' if w.nil? || (w.is_a?(String) && w.empty?)
  i = w.is_a?(String) ? w.to_i : w
  return '0' if i.zero?
  i.positive? ? "+#{i}" : i.to_s
end

# ----------------------------------------------------------------------------
# Card parsing. Each voter card has the same target set (629) but in a
# voter-specific shuffled order. Headings come in two shapes:
#   ## N. *current name*                             (regular target)
#   ## N. [Concept] *Capitalized description*        (concept cluster)
#
# The card generator (bin/naming-master-card) builds these from master-list
# entries: regular = wrap `current` in italics; concept = "[Concept] *" +
# description with first letter upcase. We invert that to recover the master-
# list `current` field as the stable target key.
#
# Bullets appear between the heading and the vote table:
#   - **`candidate-name`** *provenance* — rationale text
#   - **`candidate-name`** — rationale text          (no provenance)
#   - **`candidate-name`** *provenance*              (no rationale)
#
# The vote table:
#   | candidate | category | weight | top-pick? | notes |
#   |---|---|:-:|:-:|---|
#   | name | rename | +2 | top-pick | reasoning... |
# ----------------------------------------------------------------------------

# Recover the master-list `current` key from a card heading. Returns
# [key, kind] where kind is :regular or :concept. The key for a concept
# cluster is the original (lowercase-first) description string; the
# matcher will look up master entries with is_concept_cluster=true and
# current_description matching this key.
def heading_to_key(heading)
  if heading.start_with?('[Concept]')
    desc = heading.sub(/\A\[Concept\]\s*/, '').strip
    desc = desc.sub(/\A\*(.+)\*\z/, '\1').strip
    # Card generator did `desc.sub(/\A./, &:upcase)` — invert: lowercase first.
    key = desc.sub(/\A./) { |c| c.downcase }
    [key, :concept]
  else
    name = heading.strip
    name = name.sub(/\A\*(.+)\*\z/, '\1').strip
    name = name.sub(/\A`(.+)`\z/, '\1').strip
    [name, :regular]
  end
end

# Parse a `- **\`name\`**` bullet line. Returns [candidate, provenance, rationale].
BULLET_RE = /\A-\s+\*\*`(.+?)`\*\*(?:\s+\*([^*]+)\*)?(?:\s+—\s+(.+))?\z/

# Parse one card. Returns:
#   {
#     voter:    "opus-r2c",
#     targets:  [
#       {
#         number: 1,
#         heading: "*composition scope condition*",
#         key: "composition scope condition",
#         kind: :regular,
#         bullets: { "candidate-name" => "rationale text" },
#         votes: [
#           { candidate:, category:, weight:, top_pick:, notes: }
#         ]
#       },
#       ...
#     ]
#   }
def parse_card(path)
  voter = File.basename(path, '.md')
  targets = []
  current = nil
  in_table = false

  File.foreach(path) do |line|
    line = line.chomp

    if (m = line.match(/\A## (\d+)\. (.+?)\s*\z/))
      # New target section. Finalize the previous one.
      targets << current if current
      heading = m[2].strip
      key, kind = heading_to_key(heading)
      current = {
        number:  m[1].to_i,
        heading: heading,
        key:     key,
        kind:    kind,
        bullets: {},
        votes:   []
      }
      in_table = false
      next
    end

    next if current.nil?

    if (m = line.match(BULLET_RE))
      candidate = m[1]
      rationale = m[3].to_s.strip
      current[:bullets][candidate] = rationale
      next
    end

    if line =~ /\A\|\s*candidate\s*\|/i
      in_table = true
      next
    end

    next unless in_table && line.start_with?('|')
    next if line =~ /\A\|[\s:|-]+\|\s*\z/

    cells = line.split('|').map(&:strip)
    next unless cells.length >= 6

    candidate = cells[1]
    category  = cells[2]
    weight    = cells[3]
    top_pick  = cells[4]
    notes     = cells[5]

    next if candidate.empty?

    # A "voted row" has at least a category or a weight.
    next if category.empty? && weight.empty?

    current[:votes] << {
      candidate: candidate,
      category:  category,
      weight:    weight,
      top_pick:  !top_pick.empty?,
      notes:     notes
    }
  end

  targets << current if current
  { voter: voter, targets: targets }
end

# ----------------------------------------------------------------------------
# Architecture inference for the architectural-overlap flag. Voter ids encode
# the model family in their prefix.
# ----------------------------------------------------------------------------

def architecture_of(voter)
  case voter
  when /\Aopus/   then 'opus'
  when /\Asonnet/ then 'sonnet'
  when /\Acodex/  then 'codex'
  when /\Agemini/ then 'gemini'
  when /\Ahaiku/  then 'haiku'
  else                 'unknown'
  end
end

# ----------------------------------------------------------------------------
# Main aggregation. Builds a target-keyed structure that consolidates R1
# synthesized votes + R2 votes (per voter) + per-vote substance computation.
# ----------------------------------------------------------------------------

def build_target_index(master)
  # Two indices: regular by `current`, concept by `current_description`.
  # All keys lowercased for case-insensitive matching against the card
  # heading. The card generator capitalizes the first letter of the
  # description in the heading; master-list `current_description` may
  # already be capitalized; normalizing both sides via `.downcase` avoids
  # the trap of relying on which side carries the case convention.
  regular = {}
  concept = {}
  master['currents'].each do |c|
    if c['is_concept_cluster']
      key = (c['current_description'] || c['current']).to_s.downcase
      concept[key] = c
    else
      regular[c['current'].to_s.downcase] = c
    end
  end
  { regular: regular, concept: concept }
end

def find_master_entry(key, kind, index)
  k = key.to_s.downcase
  if kind == :concept
    index[:concept][k] || index[:regular][k]
  else
    index[:regular][k] || index[:concept][k]
  end
end

# Build the per-target consolidated record. One per master-list current.
def consolidate(master, cards, verbose: false)
  index = build_target_index(master)

  # Map from canonical key → record being built. Use the master's `current`
  # as the canonical key (stable across the whole pipeline).
  records = {}
  master['currents'].each do |c|
    canonical = c['current']
    records[canonical] = {
      master:           c,
      r2_votes:         [],     # flat list across voters
      r2_voters:        Set.new,
      bullets_by_voter: {},     # voter → { candidate → rationale }
      target_numbers:   {}      # voter → target number (for cross-reference)
    }
  end

  unmatched_count = 0
  cards.each do |card|
    voter = card[:voter]
    card[:targets].each do |t|
      master_entry = find_master_entry(t[:key], t[:kind], index)
      if master_entry.nil?
        unmatched_count += 1
        warn "  unmatched: #{voter} target ##{t[:number]} key=#{t[:key].inspect[0..80]}" if verbose
        next
      end

      canonical = master_entry['current']
      rec = records[canonical]
      rec[:bullets_by_voter][voter] = t[:bullets]
      rec[:target_numbers][voter] = t[:number]

      master_candidate_names = master_entry['candidates'].map { |c| c['candidate'] }.to_set

      t[:votes].each do |v|
        bullet = t[:bullets][v[:candidate]] || ''
        nv = novelty(v[:notes], bullet)
        weight_int = v[:weight].to_i
        is_write_in = !master_candidate_names.include?(v[:candidate])
        rec[:r2_votes] << {
          voter:        voter,
          arch:         architecture_of(voter),
          candidate:    v[:candidate],
          category:     v[:category],
          weight:       weight_int,
          weight_str:   v[:weight],
          top_pick:     v[:top_pick],
          notes:        v[:notes],
          notes_len:    v[:notes].length,
          novelty:      nv,
          is_write_in:  is_write_in,
          substance:    substance_score(weight_int, nv, v[:notes].length, bullet.length, top_pick: v[:top_pick], category: v[:category]),
          bullet:       bullet
        }
        rec[:r2_voters] << voter
      end
    end
  end

  warn "  unmatched targets: #{unmatched_count}" if verbose && unmatched_count.positive?
  records
end

# ----------------------------------------------------------------------------
# Banding. For each multi-voter target, classify as one of:
#   :strong      — clear winner: a single candidate has R1 ≥ +1 AND all R2
#                  votes on that candidate are positive AND it's the top
#                  net-substance candidate by a margin
#   :friction    — convergent but with notable dissent (a -1 from any voter,
#                  or category disagreement on the leading candidate)
#   :divergent   — multiple candidates with positive votes, no clear leader
#   :negative    — leading candidate has net-negative substance
#
# These bands are the table-organizer; the detail view shows the underlying
# data either way. Bands are heuristic — when in doubt, a target lands in
# :friction so it gets eyeballed.
# ----------------------------------------------------------------------------

def band(record)
  # Build per-candidate aggregate.
  per_candidate = Hash.new do |h, k|
    h[k] = {
      r2_votes:        [],
      total_substance: 0.0,
      total_votes:     0,    # sum of signed weights (R1 synth + R2)
      n_voters:        0,    # count of distinct voters (R1 synth counts as 1)
      n_pos:           0,
      n_neg:           0,
      top_picks:       0,
      has_add_alias:   false # any R1 or R2 vote in add-alias category
    }
  end

  record[:r2_votes].each do |v|
    pc = per_candidate[v[:candidate]]
    pc[:r2_votes] << v
    pc[:total_substance] += v[:substance]
    pc[:total_votes] += v[:weight]
    pc[:n_voters] += 1
    pc[:n_pos] += 1 if v[:weight] > 0
    pc[:n_neg] += 1 if v[:weight] < 0
    pc[:top_picks] += 1 if v[:top_pick]
    pc[:has_add_alias] = true if v[:category] == 'add-alias'
  end

  # Add R1 synthetic vote per candidate. R1's contribution carries an implicit
  # canonicalize × 1.2 multiplier when its category_tally is canonicalize-dominant
  # (excavated-from-prose evidence; same rationale as the per-vote multiplier).
  record[:master]['candidates'].each do |c|
    name = c['candidate']
    r1 = synthesize_r1(c)
    per_candidate[name][:r1] = r1
    cat_tally = c['category_tally'] || {}
    per_candidate[name][:has_add_alias] = true if cat_tally['add-alias'].to_i.positive?
    next unless r1[:weight]
    per_candidate[name][:total_votes] += r1[:weight]
    per_candidate[name][:n_voters] += 1
    if r1[:weight] != 0
      r1_factor = 1.0
      dominant_cat = cat_tally.max_by { |_, v| v }&.first
      r1_factor *= 1.2 if dominant_cat == 'canonicalize'
      per_candidate[name][:total_substance] += r1[:weight].to_f * r1_factor
      per_candidate[name][:n_pos] += 1 if r1[:weight] > 0
      per_candidate[name][:n_neg] += 1 if r1[:weight] < 0
    end
  end

  ranked = per_candidate.sort_by { |_, v| -v[:total_substance] }
  leader_name, leader = ranked.first
  return [:empty, per_candidate, leader_name, leader] if leader.nil?

  any_negative_on_leader = leader[:n_neg].positive?
  positive_candidates = ranked.count { |_, v| v[:total_substance] > 0.5 }
  leader_substance = leader[:total_substance]
  runner_up_substance = ranked[1] ? ranked[1].last[:total_substance] : 0.0

  band =
    if leader_substance <= 0
      :negative
    elsif positive_candidates >= 2 && (leader_substance - runner_up_substance) < 0.5
      :divergent
    elsif any_negative_on_leader
      :friction
    elsif leader_substance >= 2.0 && leader[:n_pos] >= 2
      :strong
    else
      :friction
    end

  [band, per_candidate, leader_name, leader]
end

# ----------------------------------------------------------------------------
# Output rendering.
# ----------------------------------------------------------------------------

def render_table(records, multi_voter_records, voters)
  out = []
  out << '# R2 Aggregation — Table View'
  out << ''
  out << "**Generated:** #{Time.now.utc.iso8601}"
  out << "**Targets included:** #{multi_voter_records.size} (filtered to ≥2 R2 voters from #{records.size} total)"
  out << "**R2 voters:** #{voters.join(', ')}"
  out << ''
  out << 'Single unified table. Targets in `**[ ... ]**` brackets, sorted by max(score/n) descending — the targets that accumulated the most normalized consensus appear first. Within each target, candidates are ordered by total substance (leader first). Math renders as math — table cells deliberately do not use backticks so `$inline$` math passes through to the renderer.'
  out << ''
  out << 'Filtered out (default): targets where the only master candidate is the current name (`is_keep`) and no R2 voter wrote in an alternative. These are uncontested keeps — no decision needed. Override with `--include-uncontested-keeps`.'
  out << ''
  out << '- **Bold row** = leader (highest score)'
  out << '- **▸** = candidate is the current name in the corpus (`is_keep` from master-list)'
  out << '- **⊕** = at least one voter (R1 or R2) cast an `add-alias` vote on this candidate. Read the detail view: an add-alias vote means "keep the current name AND add this as a parallel handle," not "replace." Different downstream action than rename/keep/canonicalize.'
  out << '- **★**: top-pick count across R2 voters'
  out << '- **n-votes**: count of distinct voters who weighed in on this candidate (R1 synthetic counts as 1 alongside each R2 voter)'
  out << '- **v-total**: sum of signed weights across all voters (raw tally before substance factor)'
  out << '- **score**: substance-adjusted vote tally — sum of (weight × factor) across voters, where factor = (0.7 + 0.3 × effort) × (1.0 + novelty), with effort = min(1, note_chars / bullet_chars). × 1.2 for top-pick votes, × 1.2 for canonicalize votes (both multiplicative). Empty note → 0. Bandwagon → 1.0. Thoughtful → 2.0. Top-picked thoughtful canonicalize → 2.88. Write-ins land near 2.0 by construction (no bullet → effort=1, novelty=1).'
  out << '- **score/n**: score normalized by total voters who weighed in on *any candidate* in this target (R1 synth counts as 1 if R1 has any votes anywhere in target). Other candidates in the target are implicit zeros. Useful for comparing across targets with different voter counts and for spotting under-engaged targets.'
  out << '- **arch**: distinct R2 architectures voting on this candidate'
  out << ''
  out << 'Per-voter weights and notes live in the detail view.'
  out << ''
  out << 'See [r2-aggregate-detail.md](r2-aggregate-detail.md) for per-target full vote breakdown, notes, and rationale.'
  out << ''

  header = ['target / candidate', '★', 'n-votes', 'v-total', 'score', 'score/n', 'arch']
  out << '| ' + header.join(' | ') + ' |'
  out << '|' + (['---'] + ['--:'] * (header.size - 1)).join('|') + '|'

  blank_row = '| ' + ([' '] * header.size).join(' | ') + ' |'

  bold = ->(s) { s.nil? || s.empty? ? s : "**#{s}**" }

  multi_voter_records.each do |canonical, rec|
    _, per_cand, leader_name, _ = band(rec)

    # Denominator for score/n: distinct voters who weighed in on ANY candidate
    # in this target. R1 synth counts as 1 if any R1 evidence exists across
    # the target's candidates. Other candidates in the target are implicit
    # zeros — a voter who voted on candidate A but not on candidate B still
    # counts in candidate B's denominator (they saw B and chose not to vote).
    n_target_voters = rec[:r2_voters].size
    n_target_voters += 1 if rec[:master]['candidates'].any? { |c| (c['votes'] || []).any? }

    short = canonical.length > 70 ? canonical[0..67] + '…' : canonical
    short = short.gsub('|', '\\|')
    is_concept = rec[:master]['is_concept_cluster']
    target_label = is_concept ? "**[ Concept: _#{short}_ ]**" : "**[ #{short} ]**"
    out << "| #{target_label} | " + ([' '] * (header.size - 1)).join(' | ') + ' |'

    sorted_candidates = per_cand.sort_by { |_, v| -v[:total_substance] }
    sorted_candidates.each do |name, data|
      next if data[:r2_votes].empty? && (data[:r1].nil? || data[:r1][:weight].nil?)

      is_leader = (name == leader_name)
      # Current-name marker. The master-list flags the corpus-current name via
      # is_keep on its candidate entry. Write-ins (no R1 record) are never the
      # current name. The arrow ▸ marks "this candidate is what's in segments
      # right now" — orthogonal to leader (which is what aggregation prefers).
      is_current = data[:r1] && data[:r1][:raw][:is_keep] == true
      has_add_alias = data[:has_add_alias]

      tp_cell = data[:top_picks].positive? ? data[:top_picks].to_s : ''
      n_cell = data[:n_voters].positive? ? data[:n_voters].to_s : ''
      votes_cell = data[:total_votes].zero? ? '0' : format_weight(data[:total_votes])
      score_cell = data[:total_substance].abs < 0.05 ? '0' : format('%.1f', data[:total_substance])
      score_per = n_target_voters.positive? ? data[:total_substance] / n_target_voters : 0.0
      score_per_cell = score_per.abs < 0.05 ? '0' : format('%.2f', score_per)
      arch_count = data[:r2_votes].map { |v| v[:arch] }.uniq.size
      arch_cell = arch_count.positive? ? arch_count.to_s : ''

      candidate_label = name.length > 60 ? name[0..57] + '…' : name
      candidate_label = candidate_label.gsub('|', '\\|')
      candidate_label = "**#{candidate_label}**" if is_leader
      markers = [is_current ? '▸' : nil, has_add_alias ? '⊕' : nil].compact.join(' ')
      candidate_label = "#{markers} #{candidate_label}" unless markers.empty?

      cells =
        if is_leader
          [candidate_label, bold.(tp_cell), bold.(n_cell),
           bold.(votes_cell), bold.(score_cell), bold.(score_per_cell), bold.(arch_cell)]
        else
          [candidate_label, tp_cell, n_cell, votes_cell, score_cell, score_per_cell, arch_cell]
        end
      out << '| ' + cells.join(' | ') + ' |'
    end

    out << blank_row
  end

  out.join("\n") + "\n"
end

def render_detail(records, multi_voter_records, voters)
  out = []
  out << '# R2 Aggregation — Detail View'
  out << ''
  out << "**Generated:** #{Time.now.utc.iso8601}"
  out << "**Targets included:** #{multi_voter_records.size} (filtered to ≥2 R2 voters from #{records.size} total)"
  out << "**R2 voters:** #{voters.join(', ')}"
  out << ''
  out << '## How to read this'
  out << ''
  out << 'Per target: R1 synthesized votes + every R2 vote with full notes, novelty score (vs the bullet on the voter\'s card), and substance score. The information needed for the final decision is here, not in the table view.'
  out << ''
  out << '**R1 synthesis rules** (applied per candidate; see script header for full reasoning):'
  out << ''
  out << '```'
  out << 'n = number of distinct R1 agents who voted'
  out << 'm = mean R1 weight (R1 scale: +3..-3)'
  out << 'd = max(category_tally) / sum(category_tally)'
  out << ''
  out << 'n == 0                                          → null'
  out << 'n ≥ 3 and m ≥ 2.0 and d ≥ 0.6                   → +2'
  out << '(n ≥ 2 and m ≥ 0.5) or (n == 1 and weight ≥ 2)  → +1'
  out << 'm ≤ -0.5 or (n == 1 and weight ≤ -2)            → -1'
  out << 'else                                            →  0'
  out << '```'
  out << ''
  out << '**Substance discount for R2 votes:**'
  out << ''
  out << '```'
  out << 'novelty   = 1 - Jaccard(tokenize(note), tokenize(card-bullet))'
  out << 'substance = raw_weight × (0.5 + 0.5 × novelty) × min(1.0, note_chars/100)'
  out << '```'
  out << ''
  out << 'Floor at 0.5×weight on pure paraphrase — the act of voting is itself a judgment.'
  out << ''
  out << '---'
  out << ''

  by_band = Hash.new { |h, k| h[k] = [] }
  multi_voter_records.each do |canonical, rec|
    band_, per_cand, leader, leader_data = band(rec)
    by_band[band_] << [canonical, rec, per_cand, leader, leader_data]
  end

  band_order = %i[strong friction divergent negative empty]
  band_titles = {
    strong:    'Strong consensus',
    friction:  'Convergent with friction',
    divergent: 'Divergent',
    negative:  'Net-negative leader',
    empty:     'Empty / unmatched'
  }

  band_order.each do |b|
    rows = by_band[b]
    next if rows.empty?

    out << "## #{band_titles[b]} (#{rows.size})"
    out << ''

    rows.each do |canonical, rec, per_cand, leader_name, _leader|
      out.concat(render_target_block(canonical, rec, per_cand, leader_name, voters))
      out << ''
      out << '---'
      out << ''
    end
  end

  out.join("\n") + "\n"
end

def render_target_block(canonical, rec, per_cand, leader_name, voters)
  out = []
  is_concept = rec[:master]['is_concept_cluster']
  if is_concept
    desc = rec[:master]['current_description']
    out << "### [Concept] *#{desc}*"
  else
    out << "### `#{canonical}`"
  end
  out << ''

  if rec[:master]['first_encounter_locality']
    out << "*First-encounter locality:* #{rec[:master]['first_encounter_locality']}"
    out << ''
  end
  if rec[:master]['segment_link']
    out << "*Segment:* [`#{rec[:master]['segment_link']}`](../../#{rec[:master]['segment_link']})"
    out << ''
  end

  # Architectural-overlap flag.
  archs = rec[:r2_votes].map { |v| v[:arch] }.uniq.sort
  voter_count = rec[:r2_voters].size
  out << "*R2 voters:* #{voter_count} (#{archs.size} architectures: #{archs.join(', ')})"
  out << ''

  sorted_candidates = per_cand.sort_by { |_, v| -v[:total_substance] }
  sorted_candidates.each do |name, data|
    next if data[:r2_votes].empty? && (data[:r1].nil? || data[:r1][:weight].nil?)

    marker = (name == leader_name) ? ' ▸ leader' : ''
    out << "**Candidate: `#{name}`**#{marker}"

    r1 = data[:r1]
    if r1 && r1[:weight]
      cat_tally_str = r1[:raw][:category_tally].map { |k, v| "#{k}:#{v}" }.join(', ')
      keep_marker = r1[:raw][:is_keep] ? ' [is_keep]' : ''
      prov = r1[:raw][:provenance] ? " [#{r1[:raw][:provenance].to_s.split(' — ', 2).first}]" : ''
      out << "- *R1 synthetic:* **#{format_weight(r1[:weight])}**#{keep_marker}#{prov} — n=#{r1[:n]}, mean=#{format('%.2f', r1[:mean] || 0)}, weights=[#{r1[:raw][:weights].map { |w| format_weight(w) }.join(', ')}], categories={#{cat_tally_str}}"
      if r1[:raw][:rationale] && !r1[:raw][:rationale].empty?
        out << "  > #{r1[:raw][:rationale].gsub("\n", "\n  > ")}"
      end
    else
      out << "- *R1 synthetic:* — (no R1 evidence)"
    end
    out << ''

    if data[:r2_votes].empty?
      out << "- *R2:* — (no R2 votes on this candidate)"
    else
      out << "- *R2 votes:*"
      data[:r2_votes].sort_by { |v| -v[:weight] }.each do |v|
        tp = v[:top_pick] ? ' ★' : ''
        cat = v[:category].empty? ? '?' : v[:category]
        out << "  - **#{v[:voter]}** (#{v[:arch]}): #{format_weight(v[:weight])}#{tp} *#{cat}* — novelty=#{format('%.2f', v[:novelty])}, len=#{v[:notes_len]}, **subst=#{format('%.2f', v[:substance])}**"
        out << "    > #{v[:notes]}" unless v[:notes].empty?
      end
    end
    out << ''
    out << "  *substance total (R1 + R2):* #{format('%.2f', data[:total_substance])}"
    out << ''
  end

  out
end

# ----------------------------------------------------------------------------
# Patterns rendering. Cross-cutting view across the entire score-card,
# intended for an agent (typically post-de-novo-audit) reading the voting
# corpus to produce first-pass canonicalize / rename decisions. The doc
# surfaces categorical groupings and observations target-by-target reading
# would miss, plus methodological keys to interpret the score-card numbers.
# ----------------------------------------------------------------------------

# Helper: structured per-target summary derived from the same `band()` data
# used by the table renderer. Returns a hash with leader name, leader data,
# all candidates ranked by substance, and aggregate numbers like score/n.
def target_summary(canonical, rec)
  _, per_cand, leader_name, leader = band(rec)
  n_target_voters = rec[:r2_voters].size + (rec[:master]['candidates'].any? { |c| (c['votes'] || []).any? } ? 1 : 0)
  ranked = per_cand.sort_by { |_, v| -v[:total_substance] }
  ranked_voted = ranked.reject { |_, v| v[:r2_votes].empty? && (v[:r1].nil? || v[:r1][:weight].nil?) }
  leader_score_per_n = (n_target_voters.positive? && leader) ? leader[:total_substance] / n_target_voters : 0.0
  is_concept = rec[:master]['is_concept_cluster']
  {
    canonical:           canonical,
    is_concept:          is_concept,
    description:         rec[:master]['current_description'],
    rec:                 rec,
    leader_name:         leader_name,
    leader:              leader,
    leader_is_current:   leader && leader[:r1] && leader[:r1][:raw][:is_keep] == true,
    leader_has_alias:    leader && leader[:has_add_alias],
    n_target_voters:     n_target_voters,
    leader_score_per_n:  leader_score_per_n,
    ranked:              ranked_voted,
    runner_up_score:     ranked_voted[1] ? ranked_voted[1].last[:total_substance] : 0.0,
    leader_score:        leader ? leader[:total_substance] : 0.0,
    segment_link:        rec[:master]['segment_link']
  }
end

def fmt_target(s)
  short = s[:canonical].length > 70 ? s[:canonical][0..67] + '…' : s[:canonical]
  s[:is_concept] ? "[Concept] _#{short}_" : "`#{short}`"
end

def fmt_candidate(name)
  name.length > 60 ? name[0..57] + '…' : name
end

def render_patterns(records, multi_voter_records, voters)
  out = []
  out << '# R2 Patterns — Cross-Cutting Voting Observations'
  out << ''
  out << "**Generated:** #{Time.now.utc.iso8601}"
  out << "**Source:** R2 voting cohort (#{voters.size} voters: #{voters.join(', ')})"
  out << "**Targets analyzed:** #{multi_voter_records.size} multi-R2-voter targets (filtered from #{records.size} total)"
  out << ''
  out << 'For an agent reading after framework ingestion to produce first-pass canonicalize / rename decisions. This doc surfaces patterns target-by-target reading would miss, and provides methodological keys to interpret the score-card numbers.'
  out << ''
  out << 'See also: [`r2-aggregate-table.md`](r2-aggregate-table.md) (score-card, sorted by max(score/n)), [`r2-aggregate-detail.md`](r2-aggregate-detail.md) (full per-target vote breakdown), [`naming-principles.md`](../../doc/naming-principles.md) (vote categories and criteria), [`naming-cycle-methodology.md`](../../doc/naming-cycle-methodology.md) (round design and engagement protocol).'
  out << ''
  out << '---'
  out << ''

  # Build summaries once
  summaries = multi_voter_records.map { |canonical, rec| target_summary(canonical, rec) }

  # ============================================================
  # Section 1: Methodological keys
  # ============================================================
  out << '## 1. What the score-card numbers mean'
  out << ''
  out << '### Score formula'
  out << ''
  out << 'Each per-vote substance is `weight × factor`, where:'
  out << ''
  out << '```'
  out << 'effort = min(1, note_chars / bullet_chars)        # length is meaningful only relative to bullet'
  out << 'novelty = 1 - jaccard(note_tokens, bullet_tokens)  # token-overlap-based; see caveats'
  out << 'factor = (0.7 + 0.3 × effort) × (1.0 + novelty)'
  out << 'factor *= 1.2 if vote.top_pick                     # acts as tiebreaker for multi-+2 cases'
  out << 'factor *= 1.2 if vote.category == canonicalize     # excavated-from-prose evidence'
  out << '```'
  out << ''
  out << 'Properties: empty note → 0 (nullify); fragment relative to bullet → 0.7 (small penalty); bandwagon (full effort, no novelty) → 1.0 (vote at face value); thoughtful (full effort, novel) → 2.0 (full amplification); thoughtful + top-pick + canonicalize → 2.88 (max). Write-ins land at 2.0 by construction (no bullet to compare against).'
  out << ''
  out << '`score` = sum of substance across all voters per candidate (R1 synth counts as one voter; R2 voters add per-card)'
  out << '`score/n` = score / total voters who weighed in on **any** candidate in the target (other candidates in target are implicit zeros — useful for cross-target comparison)'
  out << ''
  out << '### Marker semantics'
  out << ''
  out << '| marker | meaning | implication |'
  out << '|---|---|---|'
  out << '| **bold row** | leader (highest score within target) | aggregator\'s recommended landing |'
  out << '| ▸ | candidate is the current corpus name (`is_keep`) | leader = ▸ → defended keep; leader ≠ ▸ → rename signal |'
  out << '| ⊕ | at least one vote (R1 or R2) was add-alias category | downstream action: keep current AND add this — not rename |'
  out << '| ★ | top-pick count among R2 voters | in this corpus mostly co-occurs with +2 (95%); tiebreaker when voter has multiple +2s |'
  out << ''
  out << '### What\'s filtered'
  out << ''
  out << "- **Uncontested keeps** (1 master candidate that's `is_keep`, no write-ins) excluded by default. These are decisions that need no decisions: nobody proposed an alternative at any phase. Verified across all R1 work for `action fluency`, `action selection`, `adaptive system`, etc. Override with `--include-uncontested-keeps`."
  out << '- **Single-R2-voter targets** excluded by default (`--min-r2-voters=2`). Single-voter targets exist as data but were filtered for first-pass aggregation scope.'
  out << '- **No-vote targets** (zero R1 evidence + zero R2 votes) always excluded; safety net.'
  out << ''
  out << '---'
  out << ''

  # ============================================================
  # Section 2: Categorical groupings
  # ============================================================
  out << '## 2. Categorical groupings'
  out << ''
  out << 'Targets bucketed by leader-relative-to-current-name and by consensus shape. Ordered by leader-score/n descending within each bucket.'
  out << ''

  # Strongest defended keeps
  defended_keeps = summaries
                   .select { |s| s[:leader_is_current] && !s[:leader_has_alias] && s[:leader_score] > 0 }
                   .sort_by { |s| -s[:leader_score_per_n] }
  out << "### 2a. Strongest defended keeps — leader is current name (▸), no add-alias votes (#{defended_keeps.size})"
  out << ''
  out << '*The current name is the leader; voters explicitly endorsed keeping it. First-pass action: **no change**, but verify the segment\'s prose still supports the name (the score reflects voter consensus, not segment-naming-drift).*'
  out << ''
  out << '| target | leader | score | score/n | n-votes |'
  out << '|---|---|--:|--:|--:|'
  defended_keeps.first(20).each do |s|
    out << "| #{fmt_target(s)} | `#{fmt_candidate(s[:leader_name])}` | #{format('%.1f', s[:leader_score])} | **#{format('%.2f', s[:leader_score_per_n])}** | #{s[:n_target_voters]} |"
  end
  out << ''
  out << "*Showing top 20 of #{defended_keeps.size}. Full list via score-card sorted by score/n.*" if defended_keeps.size > 20
  out << ''

  # Strongest rename signals
  rename_signals = summaries
                   .select { |s| !s[:leader_is_current] && !s[:leader_has_alias] && s[:leader_score] > 0 }
                   .sort_by { |s| -s[:leader_score_per_n] }
  out << "### 2b. Strongest rename signals — leader ≠ current name, not an add-alias (#{rename_signals.size})"
  out << ''
  out << '*The leader proposes replacing the current name. First-pass action candidates: **rename** (slug + prose) if confidence is high. Read the detail view for context — sometimes the leader is a write-in single-voter case (interpret cautiously).*'
  out << ''
  out << '| target | proposed leader | score | score/n | n-votes |'
  out << '|---|---|--:|--:|--:|'
  rename_signals.first(25).each do |s|
    out << "| #{fmt_target(s)} | `#{fmt_candidate(s[:leader_name])}` | #{format('%.1f', s[:leader_score])} | **#{format('%.2f', s[:leader_score_per_n])}** | #{s[:n_target_voters]} |"
  end
  out << ''
  out << "*Showing top 25 of #{rename_signals.size}.*" if rename_signals.size > 25
  out << ''

  # Add-alias-leader cases
  alias_leaders = summaries
                  .select { |s| s[:leader_has_alias] }
                  .sort_by { |s| -s[:leader_score_per_n] }
  out << "### 2c. Add-alias landings — at least one ⊕ vote on the leader (#{alias_leaders.size})"
  out << ''
  out << '*The leader has add-alias votes — the proposed action is "keep the current name AND add this as a parallel handle," not "replace." First-pass action: **add the alias** in NOTATION/LEXICON; do not rename. Per `naming-principles.md`: most common case is symbol + English alias.*'
  out << ''
  out << '| target | proposed alias / leader | leader = current? | score | score/n |'
  out << '|---|---|---|--:|--:|'
  alias_leaders.first(25).each do |s|
    cur_marker = s[:leader_is_current] ? '▸' : '—'
    out << "| #{fmt_target(s)} | `#{fmt_candidate(s[:leader_name])}` | #{cur_marker} | #{format('%.1f', s[:leader_score])} | **#{format('%.2f', s[:leader_score_per_n])}** |"
  end
  out << ''
  out << "*Showing top 25 of #{alias_leaders.size}.*" if alias_leaders.size > 25
  out << ''

  # Contested decisions
  contested = summaries
              .select { |s| s[:leader_score] > 0 && s[:runner_up_score] > 0 && s[:runner_up_score] >= 0.7 * s[:leader_score] }
              .sort_by { |s| -s[:leader_score_per_n] }
  out << "### 2d. Contested decisions — runner-up within 30% of leader (#{contested.size})"
  out << ''
  out << '*Two or more candidates have comparable scores. First-pass action: **read detail view, defer or reject.** These often indicate genuine framework-level ambiguity worth surfacing as a finding rather than a landing.*'
  out << ''
  out << '| target | leader | leader score | runner-up | runner-up score |'
  out << '|---|---|--:|---|--:|'
  contested.first(20).each do |s|
    runner = s[:ranked][1]
    next unless runner
    out << "| #{fmt_target(s)} | `#{fmt_candidate(s[:leader_name])}` | #{format('%.1f', s[:leader_score])} | `#{fmt_candidate(runner.first)}` | #{format('%.1f', runner.last[:total_substance])} |"
  end
  out << ''
  out << "*Showing top 20 of #{contested.size}.*" if contested.size > 20
  out << ''

  # Net-negative leaders
  negative = summaries.select { |s| s[:leader_score] <= 0 }.sort_by { |s| s[:leader_score] }
  if negative.any?
    out << "### 2e. Net-negative leaders — all candidates net-negative or zero (#{negative.size})"
    out << ''
    out << '*Voters rejected all options (or split such that no candidate emerged positive). First-pass action: **reject all candidates, surface for new-options round.** May signal the target itself is poorly framed.*'
    out << ''
    out << '| target | leader | score | n-votes |'
    out << '|---|---|--:|--:|'
    negative.first(15).each do |s|
      out << "| #{fmt_target(s)} | `#{fmt_candidate(s[:leader_name])}` | #{format('%.1f', s[:leader_score])} | #{s[:n_target_voters]} |"
    end
    out << ''
  end

  out << '---'
  out << ''

  # ============================================================
  # Section 3: Cross-cutting patterns
  # ============================================================
  out << '## 3. Cross-cutting patterns'
  out << ''

  # Greek-rooted vocabulary cluster
  greek_terms = %w[chronica aporia prolepsis epistrophe praxis aisthesis logogenic logozoetic proprium auftragstaktik symbiogenic indivisum]
  greek_targets = summaries.select do |s|
    name = s[:canonical].downcase
    greek_terms.any? { |g| name.include?(g) }
  end.sort_by { |s| -s[:leader_score_per_n] }
  out << "### 3a. Greek / etymological vocabulary cluster (#{greek_targets.size})"
  out << ''
  out << '*Per the principles file, the framework deliberately uses a coherent Greek-rooted vocabulary for core nouns. Voters consistently endorsed defended keeps for these. Cross-cutting observation: this cluster scores high in normalized consensus and represents established naming commitments — first-pass action defaults to **keep** unless the segment\'s usage has drifted.*'
  out << ''
  out << '| target | leader | leader = current? | score/n |'
  out << '|---|---|---|--:|'
  greek_targets.each do |s|
    cur_marker = s[:leader_is_current] ? '▸' : '—'
    out << "| #{fmt_target(s)} | `#{fmt_candidate(s[:leader_name])}` | #{cur_marker} | #{format('%.2f', s[:leader_score_per_n])} |"
  end
  out << ''

  # Math-symbol → English-alias pattern
  math_symbol_targets = summaries.select { |s| s[:canonical].include?('$') }.sort_by { |s| -s[:leader_score_per_n] }
  out << "### 3b. Math-symbol targets — typical add-alias pattern (#{math_symbol_targets.size})"
  out << ''
  out << '*Targets whose current name contains LaTeX math (`$...$`). The pattern across the cohort: voters typically vote add-alias for an English prose handle, keeping the symbol as the structural identifier. First-pass action: **add the alias** to NOTATION/LEXICON; do not rename the symbol.*'
  out << ''
  out << '| target | leader | leader has add-alias? | score/n |'
  out << '|---|---|---|--:|'
  math_symbol_targets.each do |s|
    alias_marker = s[:leader_has_alias] ? '⊕' : '—'
    out << "| #{fmt_target(s)} | `#{fmt_candidate(s[:leader_name])}` | #{alias_marker} | #{format('%.2f', s[:leader_score_per_n])} |"
  end
  out << ''

  # Class N taxonomy
  class_targets = summaries.select { |s| s[:canonical].match?(/\AClass [123]/) || s[:canonical].downcase.include?('class 1') || s[:canonical].downcase.include?('class 2') || s[:canonical].downcase.include?('class 3') }
  out << "### 3c. Class 1/2/3 taxonomy — coordinated decision (#{class_targets.size})"
  out << ''
  out << '*The Class 1 / Class 2 / Class 3 numbered taxonomy in `#der-directed-separation` appears across multiple targets. Voters proposed English modifiers (`Modular` / `Merged` / `Coupled` / `Partially coupled` / `Integrated`) at varying scores. **This should land as a coordinated decision** — pick one consistent naming family across all three (and `Class 1 agent` / `Class 2 agent` / `Class 3 agent` variants), not three isolated landings. The `Architectural classes` framing also surfaced as an alternative meta-handle.*'
  out << ''
  out << '| target | leader | score/n |'
  out << '|---|---|--:|'
  class_targets.sort_by { |s| s[:canonical] }.each do |s|
    out << "| #{fmt_target(s)} | `#{fmt_candidate(s[:leader_name])}` | #{format('%.2f', s[:leader_score_per_n])} |"
  end
  out << ''

  # Pearl L1/L2/L3
  pearl_targets = summaries.select { |s| s[:canonical].downcase.match?(/pearl|^L[123]/i) || s[:canonical].include?('Pearl') }
  out << "### 3d. Pearl Causal Hierarchy — coordinated decision (#{pearl_targets.size})"
  out << ''
  out << '*The Pearl L1/L2/L3 causal hierarchy appears across multiple targets. Same logic as Class 1/2/3: land as a family. Note the parent target `Pearl causal hierarchy` itself.*'
  out << ''
  out << '| target | leader | score/n |'
  out << '|---|---|--:|'
  pearl_targets.sort_by { |s| s[:canonical] }.each do |s|
    out << "| #{fmt_target(s)} | `#{fmt_candidate(s[:leader_name])}` | #{format('%.2f', s[:leader_score_per_n])} |"
  end
  out << ''

  out << '---'
  out << ''

  # ============================================================
  # Section 4: Caveats and assumptions
  # ============================================================
  out << '## 4. Caveats and assumptions baked into the score-card'
  out << ''
  out << '1. **Token-Jaccard novelty conflates true paraphrase with genuine novelty.** A voter who restates the bullet\'s argument in their own words gets credited for novelty. For this corpus we treat this as acceptable — the cold-start protocol minimized cross-voter paraphrase, and rephrasing established arguments is itself engagement signal. If the de-novo-audit agent finds a finalist where this assumption matters (e.g., a rename rests on what looks like novel reasoning that\'s actually paraphrase of the bullet), the detail view shows the bullet text and the voter\'s note side-by-side; manual disambiguation is straightforward.'
  out << ''
  out << '2. **R1 → single synthetic vote.** R1 voters\' contributions are aggregated into one synthetic voter on the R2 scale. The synthesis rules are documented in the script; the detail view shows raw R1 inputs alongside the synthesis for any candidate. R1 carries factor=1 by construction (no separate novelty computation, since R1\'s rationale fed the card bullets); R1 with canonicalize-dominant category gets the canonicalize × 1.2 multiplier.'
  out << ''
  out << '3. **Voters kept separate, not collapsed by architecture.** opus-r2b/opus-r2c and sonnet-r2b/sonnet-r2c voted on overlapping-but-not-identical subsets under different methodologies (consolidation-checkpoint introduced for r2c). Treating them as four distinct voters preserves coverage.'
  out << ''
  out << '4. **Leader determination is by total substance, not by votes × substance.** The `score` column is the verdict; multiplying by raw vote count was considered and rejected (sign-cancellation issues; double-counting engagement).'
  out << ''
  out << '5. **The 99% substantive-note rate is a property of the cohort.** R2 voters were specifically instructed not to recap card bullets; most complied. The substance factor amplifies the small fraction where notes were thin or pure-paraphrase.'
  out << ''
  out << '---'
  out << ''

  # ============================================================
  # Section 5: Reading order
  # ============================================================
  out << '## 5. Suggested reading order for first-pass landings'
  out << ''
  out << '1. **Re-read** [`naming-principles.md`](../../doc/naming-principles.md) §"Vote categories" and §"Rename vs. Add-alias" — the categorical distinctions matter for landing actions.'
  out << ''
  out << '2. **Section 3 cross-cutting patterns above** — coordinated decisions (Class N, Pearl L1/L2/L3) should be triaged together, not piece-by-piece.'
  out << ''
  out << '3. **Section 2a (defended keeps, top 10–20)** — these are mostly already settled; verify segment usage hasn\'t drifted, no action otherwise. Quick pass.'
  out << ''
  out << '4. **Section 2c (add-alias landings)** — first-pass landings here are **NOTATION/LEXICON additions**, not slug renames. Different downstream tooling (no `bin/rename-slug` invocation needed).'
  out << ''
  out << '5. **Section 2b (rename signals)** — the substantive landing decisions. For each candidate: read the detail view, verify the leader\'s notes hold up against the segment\'s actual content, eyeball the runner-up.'
  out << ''
  out << '6. **Section 2d (contested)** — defer-or-reject. Surface as findings rather than forcing landings.'
  out << ''
  out << '7. **Section 2e (net-negative leaders, if any)** — flag for new-options round; do not land any current option.'
  out << ''
  out << '## 6. What this doc does NOT tell you'
  out << ''
  out << '- The framework itself — read the de-novo-audit instructions and ingest the segments before treating any landing as load-bearing.'
  out << '- Whether a name is *good* in some abstract sense — only what the cohort scored. Final judgment is yours.'
  out << '- Pre-existing slug rename history — see [`msc/naming/naming-rename-plan.md`](naming-rename-plan.md) and the role-prefix discipline (already applied across all 142 segments via `bin/align-slug --all`).'
  out << '- Cross-voter paraphrase / cold-start violation analysis — not run for this corpus; the protocol was monitored. The check is straightforward to run if needed.'

  out.join("\n") + "\n"
end

# ----------------------------------------------------------------------------
# Driver.
# ----------------------------------------------------------------------------

abort "Master file not found: #{options[:master]}" unless File.exist?(options[:master])
abort "Cards directory not found: #{options[:cards_dir]}" unless Dir.exist?(options[:cards_dir])

warn 'Loading master list...' if options[:verbose]
master = JSON.parse(File.read(options[:master]))
warn "  #{master['currents'].length} currents loaded" if options[:verbose]

card_files = Dir.glob(File.join(options[:cards_dir], '*.md')).sort
abort "No card files found in #{options[:cards_dir]}" if card_files.empty?

cards = []
voters = []
card_files.each do |path|
  warn "Parsing #{File.basename(path)}..." if options[:verbose]
  card = parse_card(path)
  cards << card
  voters << card[:voter]
  warn "  #{card[:targets].size} targets parsed, #{card[:targets].sum { |t| t[:votes].size }} votes" if options[:verbose]
end

warn 'Consolidating...' if options[:verbose]
records = consolidate(master, cards, verbose: options[:verbose])

# Filter 0 (always-on): no-vote targets. A target is "no-vote" if every
# candidate has neither R1 evidence (no R1 agents voted) nor R2 votes. These
# cannot inform any decision and would show as headings with empty bodies.
def has_any_vote?(rec)
  return true unless rec[:r2_votes].empty?
  rec[:master]['candidates'].any? { |c| (c['votes'] || []).any? }
end

voted_records = records.select { |_, rec| has_any_vote?(rec) }
no_vote_count = records.size - voted_records.size
warn "  #{no_vote_count} targets with no votes anywhere (always excluded)" if options[:verbose] && no_vote_count.positive?

# Filter 1: minimum R2 voter count.
multi_voter = voted_records.select { |_, rec| rec[:r2_voters].size >= options[:min_r2_voters] }
warn "  #{voted_records.size} voted targets, #{multi_voter.size} with ≥#{options[:min_r2_voters]} R2 voters" if options[:verbose]

# Filter 2: drop "uncontested keeps" — targets with exactly one master candidate
# (the current name, is_keep=true) and no R2 write-ins. These are decisions that
# don't need decisions: nobody proposed an alternative across either round, and
# the existing name was endorsed (or at least not contested). Including them in
# the table padded the output with non-actionable rows. Verified across full R1
# work — targets like `action fluency`, `action selection`, `adaptive system`
# survived because no alternative was ever proposed at any phase, not because
# alternatives lost out. Override with --include-uncontested-keeps.
def uncontested_keep?(rec)
  master_cands = rec[:master]['candidates']
  return false unless master_cands.size == 1
  return false unless master_cands.first['is_keep'] == true
  master_names = master_cands.map { |c| c['candidate'] }.to_set
  write_ins = rec[:r2_votes].reject { |v| master_names.include?(v[:candidate]) }
  write_ins.empty?
end

filtered = if options[:include_uncontested_keeps]
             multi_voter
           else
             multi_voter.reject { |_, rec| uncontested_keep?(rec) }
           end
excluded_count = multi_voter.size - filtered.size
warn "  #{excluded_count} uncontested keeps excluded (use --include-uncontested-keeps to keep them)" if options[:verbose] && excluded_count.positive?

# Sort targets by max(score/n) descending — targets that accumulated the
# most normalized consensus come first. This puts high-conviction landings
# at the top of the score-card and surfaces under-engaged targets toward
# the bottom (where score/n is low across all candidates). Targets with
# all-zero substance sort to the end alphabetically as a tiebreaker.
sorted_multi = filtered.sort_by do |canonical, rec|
  _, per_cand, _, _ = band(rec)
  n_target_voters = rec[:r2_voters].size + (rec[:master]['candidates'].any? { |c| (c['votes'] || []).any? } ? 1 : 0)
  max_score_per_n =
    if n_target_voters.positive?
      per_cand.values.map { |d| d[:total_substance] / n_target_voters }.max || 0.0
    else
      0.0
    end
  [-max_score_per_n, canonical.downcase]
end.to_h
sorted_multi = sorted_multi.first(options[:limit]).to_h if options[:limit]

table_md    = render_table(records, sorted_multi, voters)
detail_md   = render_detail(records, sorted_multi, voters)
patterns_md = render_patterns(records, sorted_multi, voters)

FileUtils.mkdir_p(File.dirname(options[:table_out]))
FileUtils.mkdir_p(File.dirname(options[:detail_out]))
FileUtils.mkdir_p(File.dirname(options[:patterns_out]))
File.write(options[:table_out], table_md)
File.write(options[:detail_out], detail_md)
File.write(options[:patterns_out], patterns_md)

warn "Wrote #{options[:table_out]} (#{File.size(options[:table_out])} bytes)"
warn "Wrote #{options[:detail_out]} (#{File.size(options[:detail_out])} bytes)"
warn "Wrote #{options[:patterns_out]} (#{File.size(options[:patterns_out])} bytes)"
warn "Multi-voter targets: #{sorted_multi.size}"
