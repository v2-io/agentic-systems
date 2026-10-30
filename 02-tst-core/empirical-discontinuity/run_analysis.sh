#!/bin/bash

# Simple script to run complete discontinuity analysis

echo "==================================="
echo "Empirical Discontinuity Analysis"
echo "==================================="

# Check if running from correct directory
if [ ! -f "analyze_git_history.py" ]; then
    echo "Error: Please run this script from the empirical-discontinuity directory"
    exit 1
fi

# Create output directories if they don't exist
mkdir -p data results

# Step 1: Analyze git history
echo ""
echo "Step 1: Analyzing git history..."
echo "---------------------------------"
python analyze_git_history.py --repo .. --max-commits 500 --output data

# Check if analysis succeeded
if [ $? -ne 0 ]; then
    echo "Error: Git history analysis failed"
    exit 1
fi

# Step 2: The original multi-form fit (time here is a formula; see README.md section 1)
echo ""
echo "Step 2: Fitting forms against commit_time_estimate..."
echo "-----------------------------------------------------"
python analyze_outliers.py

# Step 3: What that fit measures
echo ""
echo "Step 3: Reproducing the fit under other time formulas..."
echo "--------------------------------------------------------"
python reproduce_estimate_fit.py data/commits.json

echo ""
echo "For the elapsed-time test, dump git histories as in elapsed_time.py's header and run it on them."
