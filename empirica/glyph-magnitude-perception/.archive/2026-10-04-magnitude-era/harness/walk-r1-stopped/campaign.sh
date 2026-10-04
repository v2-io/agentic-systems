#!/bin/bash
# Run one walk round on the panel; each judge resumes (re-asking failed/incomplete sheets) up to 3 passes.
# usage: campaign.sh ROUND
cd "$(dirname "$0")/../.."
RD=$1; L=data/walk/$RD/logs; mkdir -p $L
W=harness/walk/walk.py
pass3() { for i in 1 2 3; do python3 $W run $RD $1 --workers $2 >> $L/$1.log 2>&1; done; }
pass3 sonnet55 8 &
pass3 opus55 8 &
pass3 haiku45 8 &
pass3 grok46 3 &
( pass3 gemini38flash 1; pass3 gemini31pro 1 ) &
wait
echo ALL-DONE
