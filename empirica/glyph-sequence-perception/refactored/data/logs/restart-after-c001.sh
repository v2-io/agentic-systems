#!/bin/bash
# Detached restarter (survives the coordinating session): when the c001 loop stops on data/rounds/STOP, remove STOP
# and restart the loop with the current code (tier-first planner, agy x3, Claude-first grace).
cd "$(dirname "$0")/../.."
L=data/logs/loop.log
# Match only the loop's own markers: `record` prints outcome counts like "continue/call-failed": N on healthy rounds.
until grep -qE "^== STOP found|^!! |Traceback" "$L"; do sleep 30; done
if grep -qE "^!! |Traceback" "$L"; then echo "restart-after-c001: loop failed; not restarting" >> "$L"; exit 1; fi
pgrep -f "run.py loop" >/dev/null && { echo "restart-after-c001: a loop is already running; not starting another" >> "$L"; exit 0; }
rm -f data/rounds/STOP
echo "== restart-after-c001: restarting loop $(date '+%F %T')" >> "$L"
exec python3 -u run.py loop --budget 700 >> "$L" 2>&1
