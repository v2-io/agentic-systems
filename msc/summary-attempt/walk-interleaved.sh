#!/usr/bin/env bash
# Walk the segment summaries in interleaved order: main chapters with each
# appendix segment inserted right after its first-reference main-chapter doc
# (via the NNN[b-z]-<slug>.md symlinks in the 001-105 range).
#
# Reads files in lexical order, truncated at "106" — appendix originals at
# 106+ are not read directly (their content reaches the output through the
# symlinks in the 001-105 range, dereferenced by `cat`).
#
# Output: walk-interleaved.md (excluded from the read by the grep filter so
# re-runs don't concatenate the previous run's output into the new one).

set -euo pipefail
cd "$(dirname "$0")"

ls *.md \
  | grep -v "^walk-" \
  | sort \
  | awk '{if ($0 < "106") print}' \
  | xargs cat > walk-interleaved.md

printf 'Wrote walk-interleaved.md: %d bytes, %d lines\n' \
  "$(wc -c < walk-interleaved.md)" "$(wc -l < walk-interleaved.md)"
