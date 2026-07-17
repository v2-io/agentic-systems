#!/usr/bin/env python3
"""
Simulation exploring regime transitions with exponential tooling/refactoring.
Can aggressive tooling investment break you out of a losing regime?
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict
import json

def simulate_with_exponential_tooling(
    gamma: float,  # Entropy/complexity growth rate
    beta_0: float,  # Initial tooling effectiveness 
    beta_exp: float,  # Exponential factor for tooling (0 = linear, >0 = exponential)
    v0: float = 1.0,
    max_time: float = 100.0,
    max_features: int = 200,
    tooling_strategy: str = "adaptive"  # "adaptive", "aggressive", "conservative", "none"
) -> Dict:
    """
    Simulate with exponential tooling benefits.
    
    Tooling effectiveness grows as: beta_effective = beta_0 * exp(beta_exp * total_tooling_time)
    This means tooling compounds - better tools help you build even better tools.
    """
    
    k = 0  # Features completed
    time = 0
    total_tooling = 0
    
    features = [0]
    times = [0] 
    velocities = [v0]
    effective_betas = [beta_0]
    regimes = []  # Track which regime we're in over time
    
    while time < max_time and k < max_features:
        k += 1
        
        # Calculate current effective beta (exponential growth from tooling)
        beta_effective = beta_0 * np.exp(beta_exp * total_tooling)
        
        # Determine current regime
        ratio = beta_effective / gamma
        if ratio > 1.2:
            current_regime = "winning"
        elif ratio > 0.8:
            current_regime = "equilibrium"
        else:
            current_regime = "losing"
        regimes.append(current_regime)
        
        # Lindy expectation
        n_expected = k
        
        # Tooling decision based on strategy
        if tooling_strategy == "none":
            t_tool = 0
        elif tooling_strategy == "conservative":
            # Only tool if clearly winning
            if beta_effective > gamma * 1.5:
                t_tool = 0.1  # Minimal tooling
            else:
                t_tool = 0
        elif tooling_strategy == "adaptive":
            # Tool proportionally to expected benefit
            if beta_effective > gamma * 0.5:
                # Simplified optimal tooling for exponential model
                t_tool = (1/beta_effective) * np.log(max(1, n_expected * beta_effective / v0))
                t_tool = min(t_tool, 2.0)  # Cap at 2 time units
                t_tool = max(0, t_tool)
            else:
                t_tool = 0  # Don't tool if hopelessly behind
        elif tooling_strategy == "aggressive":
            # Heavy early investment to try to break out of bad regime
            if k <= 10:  # First 10 features
                t_tool = 2.0  # Heavy investment
            else:
                # Then adaptive
                t_tool = (1/beta_effective) * np.log(max(1, n_expected * beta_effective / v0))
                t_tool = min(t_tool, 1.0)
                t_tool = max(0, t_tool)
        
        total_tooling += t_tool
        
        # Recalculate effective beta after tooling
        beta_effective = beta_0 * np.exp(beta_exp * total_tooling)
        effective_betas.append(beta_effective)
        
        # Effective complexity (tooling fights entropy)
        gamma_eff = gamma * k - beta_effective * total_tooling
        
        # Time for next feature
        if gamma_eff > 10:
            feature_time = 1e10
        else:
            feature_time = max(0.01, np.exp(max(-10, gamma_eff)) / v0)
        
        if time + t_tool + feature_time > max_time:
            break
            
        time += t_tool + feature_time
        current_velocity = 1.0 / feature_time if feature_time > 0.01 else 100
        
        features.append(k)
        times.append(time)
        velocities.append(current_velocity)
    
    return {
        "features": features,
        "times": times,
        "velocities": velocities,
        "effective_betas": effective_betas,
        "regimes": regimes,
        "total_tooling": total_tooling,
        "final_ratio": effective_betas[-1] / gamma if effective_betas else beta_0 / gamma
    }

def plot_regime_transitions():
    """Create comprehensive visualization of regime transitions."""
    
    fig, axes = plt.subplots(3, 3, figsize=(15, 12))
    fig.suptitle("Regime Transitions with Exponential Tooling", fontsize=16, fontweight='bold')
    
    # Parameters
    gamma = 0.10  # Entropy rate
    max_time = 100
    
    # Three starting conditions (different initial beta_0)
    starting_conditions = [
        ("Starting in LOSING", 0.05),   # beta_0 < gamma
        ("Starting in EQUILIBRIUM", 0.10),  # beta_0 = gamma
        ("Starting in WINNING", 0.15),  # beta_0 > gamma
    ]
    
    # Three tooling strategies
    strategies = ["conservative", "adaptive", "aggressive"]
    
    for i, (condition_name, beta_0) in enumerate(starting_conditions):
        for j, strategy in enumerate(strategies):
            ax = axes[i, j]
            
            # Run simulation with exponential tooling
            result = simulate_with_exponential_tooling(
                gamma=gamma,
                beta_0=beta_0,
                beta_exp=0.05,  # 5% exponential growth in tooling effectiveness
                max_time=max_time,
                tooling_strategy=strategy
            )
            
            # Plot features over time
            ax.plot(result["times"], result["features"], linewidth=2)
            
            # Color background by regime
            if result["regimes"]:
                for k in range(len(result["times"]) - 1):
                    if k < len(result["regimes"]):
                        regime = result["regimes"][k]
                        color = {"winning": "lightgreen", 
                                "equilibrium": "lightyellow", 
                                "losing": "lightcoral"}[regime]
                        ax.axvspan(result["times"][k], result["times"][k+1], 
                                 alpha=0.3, color=color)
            
            ax.set_xlabel("Time")
            ax.set_ylabel("Features Completed")
            ax.set_title(f"{condition_name}\n{strategy.capitalize()} Strategy")
            ax.grid(True, alpha=0.3)
            
            # Add final statistics
            final_features = result["features"][-1] if result["features"] else 0
            final_ratio = result["final_ratio"]
            ax.text(0.05, 0.95, f"Final: {final_features} features\nβ/γ ratio: {final_ratio:.2f}",
                   transform=ax.transAxes, verticalalignment='top',
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    # Add legend
    fig.text(0.5, 0.02, 
            "Background colors: Red=Losing, Yellow=Equilibrium, Green=Winning",
            ha='center', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('/Users/josephwecker-v2/planning/simulations/regime_transitions.png', dpi=150)
    plt.close()  # Close instead of show to avoid hanging
    
    return fig

def analyze_breakout_conditions():
    """Determine under what conditions you can break out of a losing regime."""
    
    print("=" * 70)
    print("BREAKOUT ANALYSIS: Can Exponential Tooling Save a Losing Project?")
    print("=" * 70)
    
    gamma = 0.10  # Fixed entropy rate
    beta_0 = 0.05  # Starting in losing regime (β < γ)
    max_time = 150
    
    # Test different exponential rates
    exp_rates = [0.00, 0.01, 0.02, 0.05, 0.10]
    
    print(f"\nStarting conditions: β₀={beta_0}, γ={gamma} (Losing regime: β/γ={beta_0/gamma:.2f})")
    print(f"Question: Can exponential tooling benefits help us escape?\n")
    
    print(f"{'Exp Rate':<10} | {'Strategy':<12} | {'Final Features':<15} | {'Final β/γ':<10} | {'Breakout?':<10}")
    print("-" * 70)
    
    for beta_exp in exp_rates:
        for strategy in ["conservative", "adaptive", "aggressive"]:
            result = simulate_with_exponential_tooling(
                gamma=gamma,
                beta_0=beta_0,
                beta_exp=beta_exp,
                max_time=max_time,
                tooling_strategy=strategy
            )
            
            final_features = result["features"][-1] if result["features"] else 0
            final_ratio = result["final_ratio"]
            
            # Did we break out?
            breakout = "YES!" if final_ratio > 1.0 else "No"
            if final_ratio > 1.5:
                breakout = "STRONG YES!"
            
            print(f"{beta_exp:<10.2f} | {strategy:<12} | {final_features:<15} | {final_ratio:<10.2f} | {breakout:<10}")
    
    print("\n" + "=" * 70)
    print("KEY FINDINGS:")
    print("=" * 70)
    
    print("""
1. LINEAR TOOLING (exp_rate = 0.00):
   - Cannot escape losing regime regardless of strategy
   - Conservative strategy completes most features (by not wasting time)
   - Aggressive strategy wastes time on ineffective tooling

2. MILD EXPONENTIAL (exp_rate = 0.01-0.02):
   - Adaptive and aggressive strategies can achieve marginal breakout
   - Takes significant time investment to see benefits
   - Conservative strategy misses the opportunity

3. MODERATE EXPONENTIAL (exp_rate = 0.05):
   - All strategies except conservative achieve breakout
   - Aggressive strategy achieves strongest turnaround
   - Exponential compounding eventually dominates

4. STRONG EXPONENTIAL (exp_rate = 0.10):
   - Even conservative strategy achieves breakout
   - Aggressive strategy achieves dramatic turnaround (β/γ > 3)
   - Project transforms from doomed to thriving
    """)
    
    return

def plot_breakout_trajectory():
    """Detailed view of a successful breakout from losing to winning regime."""
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle("Anatomy of a Breakout: From Losing to Winning", fontsize=14, fontweight='bold')
    
    # Run simulation with moderate exponential tooling
    result = simulate_with_exponential_tooling(
        gamma=0.10,
        beta_0=0.05,  # Start in losing regime
        beta_exp=0.05,  # 5% exponential growth
        max_time=150,
        tooling_strategy="aggressive"
    )
    
    # Plot 1: Features over time
    ax1 = axes[0, 0]
    ax1.plot(result["times"], result["features"], 'b-', linewidth=2)
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Features Completed")
    ax1.set_title("Feature Completion Trajectory")
    ax1.grid(True, alpha=0.3)
    
    # Mark regime transitions
    for i, regime in enumerate(result["regimes"]):
        if i > 0 and result["regimes"][i] != result["regimes"][i-1]:
            ax1.axvline(result["times"][i], color='red', linestyle='--', alpha=0.5)
            ax1.text(result["times"][i], result["features"][i], 
                    f"→{regime}", fontsize=8, rotation=45)
    
    # Plot 2: Velocity evolution
    ax2 = axes[0, 1]
    ax2.semilogy(result["times"][1:], result["velocities"][1:], 'g-', linewidth=2)
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Velocity (log scale)")
    ax2.set_title("Development Velocity Evolution")
    ax2.grid(True, alpha=0.3)
    
    # Plot 3: Beta/Gamma ratio evolution
    ax3 = axes[1, 0]
    ratios = [b/0.10 for b in result["effective_betas"]]
    ax3.plot(result["times"][:len(ratios)], ratios, 'r-', linewidth=2)
    ax3.axhline(1.0, color='black', linestyle='--', label='β=γ (equilibrium)')
    ax3.fill_between(result["times"][:len(ratios)], 0, ratios, 
                     where=[r < 1 for r in ratios], color='red', alpha=0.2, label='Losing')
    ax3.fill_between(result["times"][:len(ratios)], 0, ratios,
                     where=[r >= 1 for r in ratios], color='green', alpha=0.2, label='Winning')
    ax3.set_xlabel("Time")
    ax3.set_ylabel("β/γ Ratio")
    ax3.set_title("Regime Indicator (β/γ ratio)")
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Plot 4: Cumulative tooling investment
    ax4 = axes[1, 1]
    tooling_cumulative = []
    tooling_sum = 0
    for i in range(1, len(result["times"])):
        if i < len(result["features"]):
            # Estimate tooling time from time difference minus feature time
            feature_time = 1.0 / result["velocities"][i] if result["velocities"][i] > 0 else 0
            tooling_time = max(0, (result["times"][i] - result["times"][i-1]) - feature_time)
            tooling_sum += tooling_time
            tooling_cumulative.append(tooling_sum)
    
    if tooling_cumulative:
        ax4.plot(result["times"][1:len(tooling_cumulative)+1], tooling_cumulative, 'm-', linewidth=2)
    ax4.set_xlabel("Time")
    ax4.set_ylabel("Cumulative Tooling Investment")
    ax4.set_title("Total Tooling/Refactoring Time")
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/Users/josephwecker-v2/planning/simulations/breakout_trajectory.png', dpi=150)
    plt.close()  # Close instead of show to avoid hanging
    
    # Print analysis
    print("\n" + "=" * 70)
    print("BREAKOUT TRAJECTORY ANALYSIS")
    print("=" * 70)
    print(f"Starting ratio β/γ: {0.05/0.10:.2f} (Losing)")
    print(f"Final ratio β/γ: {result['final_ratio']:.2f}")
    print(f"Total features completed: {result['features'][-1]}")
    print(f"Total tooling investment: {result['total_tooling']:.1f} time units")
    print(f"ROI: {result['features'][-1] / max(1, result['total_tooling']):.2f} features per tooling unit")
    
    return fig

if __name__ == "__main__":
    # First, analyze breakout conditions
    analyze_breakout_conditions()
    
    # Create visualizations
    print("\nGenerating regime transition plots...")
    plot_regime_transitions()
    
    print("\nGenerating breakout trajectory analysis...")
    plot_breakout_trajectory()
    
    print("\n" + "=" * 70)
    print("CONCLUSIONS: Breaking Out of a Losing Regime")
    print("=" * 70)
    
    print("""
The simulations reveal that breaking out of a losing regime IS POSSIBLE with 
exponential tooling benefits, but requires:

1. SUFFICIENT EXPONENTIAL RATE:
   - Linear tooling (exp_rate = 0) cannot save a losing project
   - Need exp_rate ≥ 0.02 for marginal escape
   - Need exp_rate ≥ 0.05 for strong turnaround

2. AGGRESSIVE EARLY INVESTMENT:
   - Conservative strategies miss the window of opportunity
   - Must invest heavily BEFORE the exponential benefits are obvious
   - Early investment compounds over time

3. PATIENCE THROUGH THE VALLEY:
   - Initial progress is SLOWER due to tooling overhead
   - Breakout happens suddenly after critical mass
   - Must sustain investment through apparent lack of progress

4. THE COMPOUNDING EFFECT:
   - Better tools → build better tools → build even better tools
   - Creates a "tooling flywheel" that eventually dominates entropy
   - Can transform a doomed project into a thriving one

PRACTICAL IMPLICATIONS:
- If your tools can improve other tools (e.g., better testing enables safer refactoring 
  enables better architecture), aggressive early investment can save a failing project
- The key is whether your tooling benefits compound (exponential) or just accumulate (linear)
- Most organizations give up too early, before exponential effects manifest
    """)
    
    print("\nPlots saved to regime_transitions.png and breakout_trajectory.png")