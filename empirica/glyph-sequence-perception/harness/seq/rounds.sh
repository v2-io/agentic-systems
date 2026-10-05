#!/bin/bash
# Run several frontier rounds back to back: plan -> API campaign -> analyze -> commit, per round.
# usage: harness/seq/rounds.sh "RID:BUDGET RID:BUDGET ..."     e.g. "r003:400 r004:500"
set -u
cd "$(dirname "$0")"
STUDY=$(cd ../.. && pwd); ASF=$(cd ../../../.. && pwd)
for spec in $1; do
  rid=${spec%%:*}; budget=${spec##*:}
  echo "== $rid budget $budget $(date +%H:%M:%S)"
  python3 round.py plan "$rid" --budget "$budget" || { echo "PLAN FAILED $rid"; exit 1; }
  ./campaign.sh "$rid" || { echo "CAMPAIGN FAILED $rid"; exit 1; }
  grep -q "chain" "$STUDY/data/rounds/$rid/logs/analyze.log" || { echo "ANALYZE FAILED $rid"; tail -5 "$STUDY/data/rounds/$rid/logs/analyze.log"; exit 1; }
  ( cd "$ASF" && git add "empirica/glyph-sequence-perception/data" && git commit -q -m "empirica/glyph-sequence: round $rid (budget $budget) planned, answered by the API minds, fit

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01MfWNNnWTnFYD1Y8Jh7KFHF" -- "empirica/glyph-sequence-perception/data" ) && echo "COMMITTED $rid $(git -C "$ASF" log -1 --format=%h)"
  echo "== $rid done $(date +%H:%M:%S)"
done
echo "ALL ROUNDS DONE"
