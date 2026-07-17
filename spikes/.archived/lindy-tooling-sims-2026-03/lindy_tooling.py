#!/usr/bin/env python3
"""
Simulation of Lindy-effect based tooling decisions in software development.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple
import json

def simulate_lindy_development(v0: float = 1.0, 
                               alpha: float = 0.1, 
                               noise_factor: float = 0.2, 
                               max_features: int = 100, 
                               runs: int = 1000,
                               seed: int = None) -> List[Dict]:
    """
    Simulate development with Lindy effect and myopic tooling decisions.
    
    At each step k:
    1. Estimate future features: n_future = k * (1 + noise)
    2. Decide on tooling based on current v and expected n_future
    3. Update velocity and continue
    """
    if seed is not None:
        np.random.seed(seed)
    
    results = []
    
    for run in range(runs):
        k = 1  # Features completed
        v = v0  # Current velocity
        total_time = 0
        velocities = [v0]
        times = [0]
        tooling_decisions = [0]  # Track when tooling happens
        
        while k < max_features:
            # Lindy expectation with noise
            noise = np.random.normal(0, noise_factor)
            n_expected = max(1, int(k * (1 + noise)))
            
            # Critical threshold for this iteration
            n_crit = v**2 / alpha
            
            # Myopic tooling decision
            if n_expected > n_crit:
                t_tool = max(0, (np.sqrt(n_expected * alpha) - v) / alpha)
                # Update velocity
                v = np.sqrt(n_expected * alpha)
                tooling_decisions.append(1)
            else:
                t_tool = 0
                tooling_decisions.append(0)
            
            # Time for this feature
            time_this_feature = t_tool + 1/v
            total_time += time_this_feature
            
            # Record state
            k += 1
            velocities.append(v)
            times.append(total_time)
            
        results.append({
            'total_features': k,
            'total_time': total_time,
            'final_velocity': v,
            'velocities': velocities,
            'times': times,
            'tooling_decisions': tooling_decisions
        })
    
    return results

def analyze_results(results: List[Dict]) -> Dict:
    """Analyze Monte Carlo simulation results."""
    
    # Average trajectory
    max_len = max(len(r['times']) for r in results)
    avg_times = np.zeros(max_len)
    avg_velocities = np.zeros(max_len)
    counts = np.zeros(max_len)
    
    for r in results:
        n = len(r['times'])
        avg_times[:n] += r['times']
        avg_velocities[:n] += r['velocities']
        counts[:n] += 1
    
    # Avoid division by zero
    counts[counts == 0] = 1
    avg_times /= counts
    avg_velocities /= counts
    
    # Key statistics
    final_times = [r['total_time'] for r in results]
    final_velocities = [r['final_velocity'] for r in results]
    
    # When does first tooling happen?
    first_tooling = []
    for r in results:
        tooling_indices = [i for i, t in enumerate(r['tooling_decisions']) if t == 1]
        if tooling_indices:
            first_tooling.append(tooling_indices[0] + 1)  # +1 because we start at k=1
        else:
            first_tooling.append(None)
    
    first_tooling_clean = [f for f in first_tooling if f is not None]
    
    stats = {
        'mean_time': np.mean(final_times),
        'std_time': np.std(final_times),
        'median_time': np.median(final_times),
        'percentile_25_time': np.percentile(final_times, 25),
        'percentile_75_time': np.percentile(final_times, 75),
        'mean_final_velocity': np.mean(final_velocities),
        'std_final_velocity': np.std(final_velocities),
        'avg_trajectory_times': avg_times,
        'avg_trajectory_velocities': avg_velocities,
        'first_tooling_mean': np.mean(first_tooling_clean) if first_tooling_clean else None,
        'first_tooling_std': np.std(first_tooling_clean) if first_tooling_clean else None,
        'prop_with_tooling': len(first_tooling_clean) / len(results)
    }
    
    return stats

def compare_with_theory(v0: float, alpha: float, K: int) -> Dict:
    """Compare simulation with theoretical predictions."""
    
    # Theoretical predictions
    k_star = np.ceil(v0**2 / alpha)
    
    # Theoretical time for myopic strategy (approximation)
    if K <= k_star:
        theory_time_myopic = K / v0
    else:
        theory_time_myopic = k_star / v0 + 3 * np.sqrt(K / alpha) - 3 * np.sqrt(k_star / alpha)
    
    # Theoretical time if we knew K in advance (global optimal)
    if K > v0**2 / alpha:
        theory_time_global = (np.sqrt(K * alpha) - v0) / alpha + K / np.sqrt(K * alpha)
    else:
        theory_time_global = K / v0
    
    # Theoretical final velocity
    if K > k_star:
        theory_final_v = np.sqrt(K * alpha)
    else:
        theory_final_v = v0
    
    return {
        'k_star': k_star,
        'theory_time_myopic': theory_time_myopic,
        'theory_time_global': theory_time_global,
        'theory_final_velocity': theory_final_v,
        'penalty_ratio': theory_time_myopic / theory_time_global if theory_time_global > 0 else 1
    }

def plot_results(results: List[Dict], stats: Dict, theory: Dict, 
                 v0: float, alpha: float, save_path: str = None):
    """Create visualization of simulation results."""
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Plot 1: Time vs Features (sample trajectories)
    ax1 = axes[0, 0]
    # Plot a sample of trajectories
    sample_size = min(20, len(results))
    for i in range(sample_size):
        ax1.plot(range(len(results[i]['times'])), results[i]['times'], 
                alpha=0.3, color='blue', linewidth=0.5)
    # Plot average
    ax1.plot(range(len(stats['avg_trajectory_times'])), 
            stats['avg_trajectory_times'], 
            color='red', linewidth=2, label='Average')
    ax1.set_xlabel('Features Completed')
    ax1.set_ylabel('Cumulative Time')
    ax1.set_title('Time to Complete Features')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # Plot 2: Velocity Evolution
    ax2 = axes[0, 1]
    # Plot sample velocities
    for i in range(sample_size):
        ax2.plot(range(len(results[i]['velocities'])), results[i]['velocities'],
                alpha=0.3, color='green', linewidth=0.5)
    # Plot average
    ax2.plot(range(len(stats['avg_trajectory_velocities'])), 
            stats['avg_trajectory_velocities'],
            color='red', linewidth=2, label='Average')
    # Plot theoretical sqrt(k*alpha)
    k_values = np.arange(1, len(stats['avg_trajectory_velocities']) + 1)
    theoretical_v = np.where(k_values > theory['k_star'], 
                             np.sqrt(k_values * alpha), v0)
    ax2.plot(range(len(theoretical_v)), theoretical_v,
            'k--', linewidth=2, label=f'Theory: √(kα)')
    ax2.set_xlabel('Features Completed')
    ax2.set_ylabel('Velocity')
    ax2.set_title('Velocity Evolution')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    # Plot 3: Distribution of Total Times
    ax3 = axes[1, 0]
    final_times = [r['total_time'] for r in results]
    ax3.hist(final_times, bins=30, alpha=0.7, color='purple', edgecolor='black')
    ax3.axvline(stats['mean_time'], color='red', linestyle='-', linewidth=2, 
               label=f'Mean: {stats["mean_time"]:.2f}')
    ax3.axvline(theory['theory_time_myopic'], color='green', linestyle='--', 
               linewidth=2, label=f'Theory (myopic): {theory["theory_time_myopic"]:.2f}')
    ax3.axvline(theory['theory_time_global'], color='blue', linestyle='--', 
               linewidth=2, label=f'Theory (global): {theory["theory_time_global"]:.2f}')
    ax3.set_xlabel('Total Time')
    ax3.set_ylabel('Frequency')
    ax3.set_title(f'Distribution of Total Time (n={len(results)} runs)')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Plot 4: First Tooling Decision
    ax4 = axes[1, 1]
    first_tooling = []
    for r in results:
        tooling_indices = [i for i, t in enumerate(r['tooling_decisions']) if t == 1]
        if tooling_indices:
            first_tooling.append(tooling_indices[0] + 1)
    
    if first_tooling:
        ax4.hist(first_tooling, bins=20, alpha=0.7, color='orange', edgecolor='black')
        ax4.axvline(theory['k_star'], color='red', linestyle='--', linewidth=2,
                   label=f'Theory k*: {theory["k_star"]:.0f}')
        if stats['first_tooling_mean']:
            ax4.axvline(stats['first_tooling_mean'], color='blue', linestyle='-', 
                       linewidth=2, label=f'Mean: {stats["first_tooling_mean"]:.1f}')
    ax4.set_xlabel('Feature Number')
    ax4.set_ylabel('Frequency')
    ax4.set_title('First Tooling Investment')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.suptitle(f'Lindy-Effect Tooling Simulation (v₀={v0}, α={alpha})', fontsize=14)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()

def run_robustness_analysis():
    """Test robustness to different noise levels."""
    
    noise_levels = [0.0, 0.1, 0.2, 0.3, 0.5]
    v0 = 1.0
    alpha = 0.1
    max_features = 50
    runs = 500
    
    results_by_noise = {}
    
    print("Running robustness analysis...")
    print("-" * 60)
    
    for noise in noise_levels:
        print(f"\nNoise factor: {noise}")
        results = simulate_lindy_development(
            v0=v0, alpha=alpha, noise_factor=noise,
            max_features=max_features, runs=runs, seed=42
        )
        stats = analyze_results(results)
        theory = compare_with_theory(v0, alpha, max_features)
        
        results_by_noise[noise] = {
            'stats': stats,
            'theory': theory
        }
        
        print(f"  Mean time: {stats['mean_time']:.2f} ± {stats['std_time']:.2f}")
        print(f"  Theory (myopic): {theory['theory_time_myopic']:.2f}")
        print(f"  Theory (global): {theory['theory_time_global']:.2f}")
        print(f"  Final velocity: {stats['mean_final_velocity']:.2f} ± {stats['std_final_velocity']:.2f}")
        print(f"  Theory velocity: {theory['theory_final_velocity']:.2f}")
        print(f"  First tooling at: {stats['first_tooling_mean']:.1f} ± {stats['first_tooling_std']:.1f}" 
              if stats['first_tooling_mean'] else "  No tooling triggered")
    
    return results_by_noise

if __name__ == "__main__":
    # Set parameters
    v0 = 1.0  # Initial velocity
    alpha = 0.1  # Tooling effectiveness
    noise_factor = 0.2  # Noise in Lindy estimates
    max_features = 50
    runs = 1000
    
    print("=" * 60)
    print("LINDY-EFFECT TOOLING SIMULATION")
    print("=" * 60)
    print(f"\nParameters:")
    print(f"  Initial velocity (v₀): {v0}")
    print(f"  Tooling effectiveness (α): {alpha}")
    print(f"  Noise factor: {noise_factor}")
    print(f"  Max features: {max_features}")
    print(f"  Number of runs: {runs}")
    
    # Run main simulation
    print(f"\nRunning {runs} simulations...")
    results = simulate_lindy_development(
        v0=v0, alpha=alpha, noise_factor=noise_factor,
        max_features=max_features, runs=runs, seed=42
    )
    
    # Analyze results
    stats = analyze_results(results)
    theory = compare_with_theory(v0, alpha, max_features)
    
    # Print results
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    
    print(f"\nTime to complete {max_features} features:")
    print(f"  Simulation mean: {stats['mean_time']:.2f}")
    print(f"  Simulation std: {stats['std_time']:.2f}")
    print(f"  25th percentile: {stats['percentile_25_time']:.2f}")
    print(f"  Median: {stats['median_time']:.2f}")
    print(f"  75th percentile: {stats['percentile_75_time']:.2f}")
    
    print(f"\nTheoretical predictions:")
    print(f"  Myopic strategy: {theory['theory_time_myopic']:.2f}")
    print(f"  Global optimal: {theory['theory_time_global']:.2f}")
    print(f"  Penalty ratio: {theory['penalty_ratio']:.2%}")
    
    print(f"\nFinal velocity:")
    print(f"  Simulation mean: {stats['mean_final_velocity']:.2f}")
    print(f"  Simulation std: {stats['std_final_velocity']:.2f}")
    print(f"  Theoretical: {theory['theory_final_velocity']:.2f}")
    
    print(f"\nFirst tooling investment:")
    print(f"  Theoretical k*: {theory['k_star']:.0f}")
    if stats['first_tooling_mean']:
        print(f"  Simulation mean: {stats['first_tooling_mean']:.1f}")
        print(f"  Simulation std: {stats['first_tooling_std']:.1f}")
    print(f"  Proportion with tooling: {stats['prop_with_tooling']:.1%}")
    
    # Create visualizations
    print("\nGenerating plots...")
    plot_results(results, stats, theory, v0, alpha, 
                save_path='/Users/josephwecker-v2/planning/simulations/lindy_results.png')
    
    # Run robustness analysis
    print("\n" + "=" * 60)
    print("ROBUSTNESS ANALYSIS")
    print("=" * 60)
    robustness_results = run_robustness_analysis()
    
    # Save results to JSON
    output_data = {
        'parameters': {
            'v0': v0,
            'alpha': alpha,
            'noise_factor': noise_factor,
            'max_features': max_features,
            'runs': runs
        },
        'stats': {k: v for k, v in stats.items() 
                 if not isinstance(v, np.ndarray)},
        'theory': theory,
        'robustness': {
            noise: {
                'mean_time': res['stats']['mean_time'],
                'std_time': res['stats']['std_time'],
                'mean_final_velocity': res['stats']['mean_final_velocity'],
                'theory_time': res['theory']['theory_time_myopic']
            } for noise, res in robustness_results.items()
        }
    }
    
    with open('/Users/josephwecker-v2/planning/simulations/lindy_results.json', 'w') as f:
        json.dump(output_data, f, indent=2)
    
    print("\nResults saved to lindy_results.json and lindy_results.png")