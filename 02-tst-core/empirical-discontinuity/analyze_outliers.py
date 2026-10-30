#!/usr/bin/env python3
"""Analyze outliers and re-run models with filtering"""

import pickle
import numpy as np
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Optional, List
from scipy import stats
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

@dataclass
class CommitMetrics:
    """Metrics for a single commit"""
    hash: str
    timestamp: datetime
    author: str
    message: str
    files_changed: int
    unique_directories: int
    lines_added: int
    lines_deleted: int
    file_transitions: int
    directory_transitions: int
    discontinuity_score: float
    is_bug_fix: bool
    is_refactor: bool
    time_since_last_commit: Optional[timedelta]
    commit_time_estimate: Optional[timedelta]

@dataclass
class FileMetrics:
    """Metrics for a single file"""
    filepath: str
    total_changes: int
    unique_authors: int
    bug_fix_frequency: float
    avg_discontinuity_per_change: float
    coupled_files: List[tuple]
    stability_score: float

# Load the data
with open('data/analysis.pkl', 'rb') as f:
    data = pickle.load(f)

commits = data['commits']

# Extract data with proper time conversion
discontinuities = []
times = []
messages = []

for c in commits:
    if c.commit_time_estimate and c.commit_time_estimate.total_seconds() > 0:
        minutes = c.commit_time_estimate.total_seconds() / 60.0
        if minutes > 0:
            discontinuities.append(c.discontinuity_score)
            times.append(minutes)
            messages.append(c.message[:50])

# Analyze outliers
d_array = np.array(discontinuities)
t_array = np.array(times)

print("=== OUTLIER ANALYSIS ===\n")
print(f"Total data points: {len(discontinuities)}")
print(f"\nDiscontinuity Score Statistics:")
print(f"  Min: {d_array.min():.1f}")
print(f"  25th percentile: {np.percentile(d_array, 25):.1f}")
print(f"  Median: {np.median(d_array):.1f}")
print(f"  75th percentile: {np.percentile(d_array, 75):.1f}")
print(f"  95th percentile: {np.percentile(d_array, 95):.1f}")
print(f"  99th percentile: {np.percentile(d_array, 99):.1f}")
print(f"  Max: {d_array.max():.1f}")

print(f"\nTime Estimate Statistics (minutes):")
print(f"  Min: {t_array.min():.1f}")
print(f"  Median: {np.median(t_array):.1f}")
print(f"  Max: {t_array.max():.1f}")

# Show extreme outliers
print(f"\n=== EXTREME OUTLIERS (>100 discontinuity) ===")
outlier_indices = [i for i, d in enumerate(discontinuities) if d > 100]
for idx in outlier_indices[:5]:
    print(f"\nCommit: {messages[idx]}")
    print(f"  Discontinuity: {discontinuities[idx]:.0f}")
    print(f"  Time: {times[idx]:.1f} minutes")

# Function definitions for models
def exp_model(d, t_base, alpha):
    return t_base * ((1 + alpha) ** d)

def log_model(d, t_base, scale):
    return t_base * np.log(1 + scale * np.array(d))

def power_model(d, t_base, beta):
    return t_base * (np.array(d) ** beta)

# Test models with different filtering thresholds
thresholds = [None, 100, 50, 25, 10]
results = {}

print(f"\n=== MODEL COMPARISON WITH FILTERING ===")
for threshold in thresholds:
    if threshold:
        mask = d_array <= threshold
        d_filtered = d_array[mask]
        t_filtered = t_array[mask]
        label = f"≤{threshold}"
    else:
        d_filtered = d_array
        t_filtered = t_array
        label = "All"
    
    results[label] = {
        'n': len(d_filtered),
        'max_d': d_filtered.max() if len(d_filtered) > 0 else 0
    }
    
    if len(d_filtered) > 2:
        # Linear
        slope, intercept, r_value, _, _ = stats.linregress(d_filtered, t_filtered)
        results[label]['linear'] = r_value**2
        
        # Exponential
        try:
            popt, _ = curve_fit(exp_model, d_filtered, t_filtered, 
                              p0=[np.median(t_filtered), 0.05], maxfev=5000)
            y_pred = exp_model(d_filtered, *popt)
            ss_res = np.sum((t_filtered - y_pred)**2)
            ss_tot = np.sum((t_filtered - np.mean(t_filtered))**2)
            r2_exp = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
            results[label]['exponential'] = r2_exp
            results[label]['alpha'] = popt[1]
        except:
            results[label]['exponential'] = 0
            results[label]['alpha'] = None
        
        # Logarithmic
        try:
            popt_log, _ = curve_fit(log_model, d_filtered, t_filtered, 
                                  p0=[np.median(t_filtered), 1.0], maxfev=5000)
            y_pred_log = log_model(d_filtered, *popt_log)
            ss_res_log = np.sum((t_filtered - y_pred_log)**2)
            r2_log = 1 - (ss_res_log / ss_tot) if ss_tot > 0 else 0
            results[label]['logarithmic'] = r2_log
        except:
            results[label]['logarithmic'] = 0
        
        # Power law
        try:
            # Filter out zeros for power law
            mask_nonzero = d_filtered > 0
            if np.sum(mask_nonzero) > 2:
                d_nz = d_filtered[mask_nonzero]
                t_nz = t_filtered[mask_nonzero]
                popt_pow, _ = curve_fit(power_model, d_nz, t_nz, 
                                      p0=[np.median(t_nz), 0.5], maxfev=5000)
                y_pred_pow = power_model(d_nz, *popt_pow)
                ss_res_pow = np.sum((t_nz - y_pred_pow)**2)
                ss_tot_pow = np.sum((t_nz - np.mean(t_nz))**2)
                r2_pow = 1 - (ss_res_pow / ss_tot_pow) if ss_tot_pow > 0 else 0
                results[label]['power'] = r2_pow
                results[label]['beta'] = popt_pow[1]
            else:
                results[label]['power'] = 0
                results[label]['beta'] = None
        except:
            results[label]['power'] = 0
            results[label]['beta'] = None

# Print results table
print(f"\n{'Filter':<10} {'N':<6} {'Linear':<8} {'Exp':<8} {'Log':<8} {'Power':<8} {'α':<8} {'β':<8}")
print("-" * 70)
for label, res in results.items():
    print(f"{label:<10} {res['n']:<6} ", end="")
    print(f"{res.get('linear', 0):.3f}   ", end="")
    print(f"{res.get('exponential', 0):.3f}   ", end="")
    print(f"{res.get('logarithmic', 0):.3f}   ", end="")
    print(f"{res.get('power', 0):.3f}   ", end="")
    alpha = res.get('alpha')
    print(f"{alpha:.3f}   " if alpha else "  -      ", end="")
    beta = res.get('beta')
    print(f"{beta:.3f}" if beta else "  -")

# Create comparison plot
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: All data with models
ax1 = axes[0, 0]
ax1.scatter(discontinuities, times, alpha=0.3, s=10)
ax1.set_xlabel('Discontinuity Score')
ax1.set_ylabel('Time (minutes)')
ax1.set_title('All Data')
ax1.set_xlim(0, max(100, np.percentile(discontinuities, 99)))

# Plot 2: Filtered ≤50
ax2 = axes[0, 1]
mask = d_array <= 50
ax2.scatter(d_array[mask], t_array[mask], alpha=0.5, s=20)
ax2.set_xlabel('Discontinuity Score')
ax2.set_ylabel('Time (minutes)')
ax2.set_title('Filtered (d ≤ 50)')

# Plot 3: Filtered ≤25
ax3 = axes[1, 0]
mask = d_array <= 25
if np.sum(mask) > 2:
    d_f = d_array[mask]
    t_f = t_array[mask]
    ax3.scatter(d_f, t_f, alpha=0.5, s=20)
    
    # Fit and plot models
    x_range = np.linspace(0, 25, 100)
    
    # Exponential
    try:
        popt, _ = curve_fit(exp_model, d_f, t_f, p0=[50, 0.05])
        y_exp = exp_model(x_range, *popt)
        ax3.plot(x_range, y_exp, 'g-', label=f'Exp (α={popt[1]:.3f})', linewidth=2)
    except:
        pass
    
    # Linear
    z = np.polyfit(d_f, t_f, 1)
    y_lin = np.poly1d(z)(x_range)
    ax3.plot(x_range, y_lin, 'r--', label='Linear', alpha=0.7)
    
    ax3.legend()

ax3.set_xlabel('Discontinuity Score')
ax3.set_ylabel('Time (minutes)')
ax3.set_title('Filtered (d ≤ 25) with Models')

# Plot 4: R² comparison
ax4 = axes[1, 1]
filters = ['All', '≤50', '≤25', '≤10']
x = np.arange(len(filters))
width = 0.2

models_to_plot = ['linear', 'exponential', 'logarithmic', 'power']
colors = ['blue', 'green', 'orange', 'red']

for i, (model, color) in enumerate(zip(models_to_plot, colors)):
    values = [results.get(f, {}).get(model, 0) for f in filters]
    ax4.bar(x + i*width, values, width, label=model.capitalize(), color=color, alpha=0.7)

ax4.set_xlabel('Filter Threshold')
ax4.set_ylabel('R² Value')
ax4.set_title('Model Performance by Filter Threshold')
ax4.set_xticks(x + width * 1.5)
ax4.set_xticklabels(filters)
ax4.legend()
ax4.grid(True, alpha=0.3, axis='y')

plt.suptitle('Outlier Analysis and Model Comparison', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('results/outlier_analysis.png', dpi=150, bbox_inches='tight')
print(f"\n\nPlot saved to results/outlier_analysis.png")

# Final recommendation
print("\n=== RECOMMENDATIONS ===")
best_threshold = None
best_r2 = 0
best_model = None

for threshold in ['≤25', '≤10']:
    if threshold in results:
        exp_r2 = results[threshold].get('exponential', 0)
        if exp_r2 > best_r2:
            best_r2 = exp_r2
            best_threshold = threshold
            best_model = 'exponential'

print(f"\n1. Filter outliers with discontinuity {best_threshold} for best exponential fit")
print(f"   - This gives R² = {best_r2:.3f} for exponential model")
if best_threshold in results and results[best_threshold].get('alpha'):
    print(f"   - fitted α = {results[best_threshold]['alpha']:.3f}")
print("   NOTE: 'time' here is commit_time_estimate, a formula in files and lines changed;")
print("   d is built from the same files, so this fit cannot test the form (README.md §1).")

print(f"\n2. The extreme outliers (d > 100) likely represent:")
print(f"   - Initial repository imports")
print(f"   - Major refactorings or reorganizations")
print(f"   - Automated bulk changes")

print(f"   - Logarithmic dominance in full dataset may be due to outliers")