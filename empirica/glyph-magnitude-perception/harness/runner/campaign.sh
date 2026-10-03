#!/usr/bin/env bash
# v1.0 campaign: one judge's full instrument queue, run sequentially (resumable: rerun = continue).
#   campaign.sh JUDGE MODE WORKERS REPS_CONFLICT
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
J="$1"; MODE="$2"; W="${3:-4}"; RC="${4:-1}"
R="python3 $HERE/run.py"
$R triads   "$J" --mode "$MODE" --workers "$W"
$R conflict "$J" --mode "$MODE" --workers "$W" --reps "$RC"
$R holistic "$J" --mode "$MODE" --workers "$W"
$R gestalt  "$J" --mode single  --workers "$W"
for F in forced tie perp; do
  $R format "$J" --format "$F" --mode "$MODE" --workers "$W"
done
echo "CAMPAIGN DONE $J $MODE"
