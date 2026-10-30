#!/bin/bash
# Reproduces README §1 from the saved dataset in data/ (229 commits of ~/src/_core/tst, 2025-08-25..29).
# data/ is never overwritten: re-mining today's history yields different commits and cannot reproduce it.
#
# Usage: ./run_analysis.sh [<repo>]
#   With <repo>, also mines that repository's history into rerun/ (the original miner, formula-based time).
#   The elapsed-time test (README §2) runs on git log dumps: see elapsed_time.py's header.

set -e
if [ ! -f "analyze_git_history.py" ]; then
    echo "Error: run this script from the empirical-discontinuity directory"
    exit 1
fi

mkdir -p results   # analyze_outliers.py writes its figure here; results/ and rerun/ are not tracked

echo "Step 1: the original multi-form fit against commit_time_estimate (reads data/analysis.pkl)"
python3 analyze_outliers.py

echo
echo "Step 2: the same fit under other time formulas (README §1)"
python3 reproduce_estimate_fit.py data/commits.json

if [ -n "$1" ]; then
    echo
    echo "Step 3: mining $1 into rerun/"
    python3 analyze_git_history.py --repo "$1" --max-commits 500 --output rerun
    python3 reproduce_estimate_fit.py rerun/commits.json
fi
