#!/usr/bin/env bash
# Walk the segment summaries in sequential order: main chapters first (001-105),
# then Appendix A (106-146), then Appendix B (147-151), all in OUTLINE order.
#
# Skips symlinks via `find -type f`, so each appendix segment appears exactly
# once in its appendix-section position (the symlinks at NNN[b-z]- positions
# are filtered out).
#
# Output: walk-sequential.md (excluded from the read by the -not -name filter
# so re-runs don't concatenate the previous run's output into the new one).

set -euo pipefail
cd "$(dirname "$0")"

find . -maxdepth 1 -type f -name "*.md" -not -name "walk-*.md" \
  | sort \
  | xargs cat > walk-sequential.md

printf 'Wrote walk-sequential.md: %d bytes, %d lines\n' \
  "$(wc -c < walk-sequential.md)" "$(wc -l < walk-sequential.md)"
