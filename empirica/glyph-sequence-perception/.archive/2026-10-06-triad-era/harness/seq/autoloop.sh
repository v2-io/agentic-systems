#!/bin/bash
# Keep running kernel-growth rounds (Joseph, 2026-10-04: "keep going as much as we can ... track the growth of stable
# sequences"). One round at a time through rounds.sh (plan -> API minds -> fit -> commit -> standings + progress).
# Stops when:
#   - data/rounds/STOP-ROUNDS exists (touch it to stop after the current round), or
#   - the method's own stop rule fires (DESIGN-scale-up, "loop until dry"): DRY_K consecutive rounds that add neither a
#     stable sequence nor a stable glyph (progress.json), or
#   - a round fails (plan, campaign or fit), so nothing runs on a broken state.
# usage: harness/seq/autoloop.sh [BUDGET] [DRY_K]     (defaults 700, 3). Log: data/logs/autoloop.log
set -u
cd "$(dirname "$0")"
STUDY=$(cd ../.. && pwd); R=$STUDY/data/rounds; LOG=$STUDY/data/logs/autoloop.log
BUDGET=${1:-700}; DRY_K=${2:-3}
mkdir -p "$STUDY/data/logs"
echo "== autoloop start $(date '+%F %T') budget $BUDGET dry_k $DRY_K" >> "$LOG"
while [ ! -e "$R/STOP-ROUNDS" ]; do
  last=$(ls -d "$R"/r[0-9][0-9][0-9] 2>/dev/null | sed 's#.*/r##' | sort -n | tail -1)
  next=$(printf "r%03d" $((10#$last + 1)))
  echo "== $next start $(date '+%F %T')" >> "$LOG"
  ./rounds.sh "$next:$BUDGET"
  if ! grep -q "STANDINGS $next" "$STUDY/data/logs/rounds-$next-$next.log" 2>/dev/null; then
    echo "!! $next did not complete; stopping (see data/logs/rounds-$next-$next.log)" >> "$LOG"; exit 1
  fi
  dry=$(python3 - "$STUDY/data/progress.json" "$DRY_K" <<'PY'
import json, sys
rows = json.load(open(sys.argv[1])); k = int(sys.argv[2])
grow = [(r["stable"], r["stable_glyphs"]) for r in rows]
d = 0
for (s0, g0), (s1, g1) in zip(grow, grow[1:]):
    d = d + 1 if (s1 <= s0 and g1 <= g0) else 0
print("DRY" if d >= k else f"growing (dry streak {d})")
PY
)
  echo "== $next done $(date '+%F %T'): $dry" >> "$LOG"
  [ "$dry" = "DRY" ] && { echo "== stopping: $DRY_K rounds without stable growth (loop until dry)" >> "$LOG"; exit 0; }
done
echo "== STOP-ROUNDS found; stopped $(date '+%F %T')" >> "$LOG"
