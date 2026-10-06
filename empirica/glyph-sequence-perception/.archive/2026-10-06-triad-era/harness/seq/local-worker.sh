#!/bin/bash
# Background worker for slow local minds (Glimmer via llama.cpp): answers every planned round in order,
# resuming, until data/rounds/STOP-LOCAL exists. Rounds are analyzed without waiting for it; its answers
# enter the cumulative evidence whenever they land (a lagging mind, as PLAN §7 allows).
# usage: harness/seq/local-worker.sh MIND     (e.g. glimmer30b-sheet; start the server first)
cd "$(dirname "$0")"
M=$1; R=../../data/rounds
while [ ! -e "$R/STOP-LOCAL" ]; do
  for rd in $(ls -d $R/r* 2>/dev/null | sort); do
    rid=$(basename "$rd"); [ -e "$rd/sheets.jsonl" ] || continue
    mkdir -p "$rd/logs"; python3 round.py run "$rid" --minds "$M" >> "$rd/logs/$M.log" 2>&1
  done
  sleep 60
done
