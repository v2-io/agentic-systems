#!/usr/bin/env bash
# top-40 stability/universality battery for one judge (exploratory).  top40-campaign.sh JUDGE MODE WORKERS
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"; R="python3 $HERE/run.py"
$R top40 "$1" --mode "$2" --workers "${3:-3}"
$R top40-gestalt "$1" --mode single --workers "${3:-3}"
$R top40 "$1" --mode "$2" --workers "${3:-3}"   # fill pass
echo "TOP40 DONE $1"
