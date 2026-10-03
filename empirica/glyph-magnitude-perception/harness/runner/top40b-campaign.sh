#!/usr/bin/env bash
# top-40 supplement (batch b) for one judge.  top40b-campaign.sh JUDGE MODE WORKERS
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"; R="python3 $HERE/run.py"
$R top40b "$1" --mode "$2" --workers "${3:-3}"
$R top40b-gestalt "$1" --mode single --workers "${3:-3}"
$R top40b "$1" --mode "$2" --workers "${3:-3}"
echo "TOP40B DONE $1"
