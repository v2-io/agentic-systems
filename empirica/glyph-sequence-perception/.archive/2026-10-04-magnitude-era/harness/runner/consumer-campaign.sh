#!/usr/bin/env bash
# Probe of an old SIGNA sample string (a proof-of-concept from an old implementation, not SIGNA) for one judge (not part of the registered program).  consumer-campaign.sh JUDGE MODE WORKERS
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"; R="python3 $HERE/run.py"
$R signa "$1" --mode "$2" --workers "${3:-3}"
$R signa-gestalt "$1" --mode single --workers 3
echo "CONSUMER DONE $1"
