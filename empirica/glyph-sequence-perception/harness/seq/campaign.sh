#!/bin/bash
# Run one planned round on the roster: API minds in parallel, Glimmer (local llama.cpp) alongside, then analyze.
# usage: harness/seq/campaign.sh RID     (plan first: python3 harness/seq/round.py plan RID)
# Each mind resumes: failed or unparseable sheets are re-asked up to 3 passes; raw answers are always kept.
set -u
cd "$(dirname "$0")"
RID=$1; L=../../data/rounds/$RID/logs; mkdir -p "$L"
MINDS=$(python3 -c "import json;d=json.load(open('../core/minds.json'))['roster'];print(' '.join(d['core']+d['second']))")
for m in $MINDS; do
  ( for i in 1 2 3; do python3 round.py run "$RID" --minds "$m" >> "$L/$m.log" 2>&1; done ) &
done
wait
python3 round.py analyze "$RID" > "$L/analyze.log" 2>&1
echo "$RID done"
