#!/bin/bash
# 'dress' follow-up (design/2026-10-04-plan/scripts/dress_stimuli.py in the study). Waits for the ones campaign.
cd "$(dirname "$0")"
while pgrep -f "run.py ones" >/dev/null; do sleep 20; done
R=harness/runner/run.py
( python3 $R dress opus55 --workers 6 > dress-logs/opus55.log 2>&1; python3 $R dress-gestalt opus55 > dress-logs/opus55-g.log 2>&1 ) &
( python3 $R dress sonnet55 --workers 6 > dress-logs/sonnet55.log 2>&1; python3 $R dress-gestalt sonnet55 > dress-logs/sonnet55-g.log 2>&1 ) &
( python3 $R dress haiku45 --workers 6 > dress-logs/haiku45.log 2>&1; python3 $R dress-gestalt haiku45 > dress-logs/haiku45-g.log 2>&1 ) &
( python3 $R dress grok46 --mode sheet --workers 2 > dress-logs/grok46.log 2>&1; python3 $R dress-gestalt grok46 > dress-logs/grok46-g.log 2>&1 ) &
( python3 $R dress gemini38flash --mode sheet --workers 1 > dress-logs/gemini38flash.log 2>&1; python3 $R dress-gestalt gemini38flash --workers 1 > dress-logs/gemini38flash-g.log 2>&1;
  python3 $R dress gemini31pro --mode sheet --workers 1 > dress-logs/gemini31pro.log 2>&1; python3 $R dress-gestalt gemini31pro --workers 1 > dress-logs/gemini31pro-g.log 2>&1 ) &
( python3 $R dress llama32-3b --workers 1 > dress-logs/llama32-3b.log 2>&1; python3 $R dress-gestalt llama32-3b --workers 1 > dress-logs/llama32-3b-g.log 2>&1 ) &
wait
echo ALL-DONE
