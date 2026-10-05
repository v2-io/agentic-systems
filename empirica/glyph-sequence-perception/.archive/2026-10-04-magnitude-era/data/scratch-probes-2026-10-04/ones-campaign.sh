#!/bin/bash
cd "$(dirname "$0")"
R=harness/runner/run.py
( python3 $R ones opus55 --workers 6 > ones-logs/opus55.log 2>&1; python3 $R ones-gestalt opus55 > ones-logs/opus55-g.log 2>&1 ) &
( python3 $R ones sonnet55 --workers 6 > ones-logs/sonnet55.log 2>&1; python3 $R ones-gestalt sonnet55 > ones-logs/sonnet55-g.log 2>&1 ) &
( python3 $R ones haiku45 --workers 6 > ones-logs/haiku45.log 2>&1; python3 $R ones-gestalt haiku45 > ones-logs/haiku45-g.log 2>&1 ) &
( python3 $R ones grok46 --mode sheet --workers 2 > ones-logs/grok46.log 2>&1; python3 $R ones-gestalt grok46 > ones-logs/grok46-g.log 2>&1 ) &
( python3 $R ones gemini31pro --mode sheet --workers 1 > ones-logs/gemini31pro.log 2>&1; python3 $R ones-gestalt gemini31pro --workers 1 > ones-logs/gemini31pro-g.log 2>&1 ) &
( python3 $R ones gemini38flash --mode sheet --workers 1 > ones-logs/gemini38flash.log 2>&1; python3 $R ones-gestalt gemini38flash --workers 1 > ones-logs/gemini38flash-g.log 2>&1 ) &
( python3 $R ones llama32-3b --workers 1 > ones-logs/llama32-3b.log 2>&1; python3 $R ones-gestalt llama32-3b --workers 1 > ones-logs/llama32-3b-g.log 2>&1;
  python3 $R ones qwen25-3b --workers 1 > ones-logs/qwen25-3b.log 2>&1; python3 $R ones-gestalt qwen25-3b --workers 1 > ones-logs/qwen25-3b-g.log 2>&1 ) &
wait
echo ALL-DONE
