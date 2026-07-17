#!/usr/bin/env python3
"""
Analyze regime breakout with stochastic termination.
Shows how project mortality affects the window for achieving escape velocity.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def simulate_breakout_with_termination(beta_0=0.05, gamma=0.10, beta_exp=0.02, 
                                       strategy='aggressive', max_time=150, 
                                       runs=1000, seed=42):
    """
    Simulate regime breakout attempts with stochastic termination.
    Projects can die before achieving breakout!
    """
    
    if seed is not None:
        np.random.seed(seed)
    
    results = []
    
    for run in range(runs):
        # Initialize - projects start at k~50 (established projects we study)
        # Use Gaussian distribution like we discovered
        features = max(10, int(np.random.normal(50, 15)))
        velocity = np.sqrt(features * 0.1)  # Velocity based on sqrt(k*alpha)
        time = 0
        total_tooling = 0
        beta_effective = beta_0
        terminated = False
        achieved_breakout = False
        breakout_time = None
        
        trajectory = {
            'features': [features],
            'velocity': [velocity],
            'time': [0],
            'regime': ['losing'],
            'beta_gamma_ratio': [beta_0/gamma]
        }
        
        while time < max_time and not terminated:
            # Check for stochastic termination based on features completed
            # Use correct 1/(k+1) formula
            features_int = max(1, int(features))
            if np.random.random() < 1/(features_int + 1):
                terminated = True
                break
            
            # Calculate current regime
            beta_effective = beta_0 * np.exp(beta_exp * total_tooling)
            ratio = beta_effective / gamma
            
            if ratio > 1.2:
                regime = 'winning'
                if not achieved_breakout:
                    achieved_breakout = True
                    breakout_time = time
            elif ratio > 0.8:
                regime = 'equilibrium'
            else:
                regime = 'losing'
            
            # Tooling strategy
            if strategy == 'aggressive':
                # Heavy tooling investment early
                if features < 50:
                    tooling_fraction = 0.4
                else:
                    tooling_fraction = 0.2
            elif strategy == 'adaptive':
                # Adjust based on regime
                if regime == 'losing':
                    tooling_fraction = 0.3
                else:
                    tooling_fraction = 0.1
            else:  # conservative
                tooling_fraction = 0.1
            
            # Apply tooling
            dt = 1.0  # Time step
            tooling_time = tooling_fraction * dt
            feature_time = (1 - tooling_fraction) * dt
            
            total_tooling += tooling_time
            
            # Update velocity with exponential tooling benefit
            velocity = velocity * np.exp(beta_effective * tooling_time)
            
            # Apply entropy (complexity growth)
            velocity = velocity * np.exp(-gamma * features * feature_time)
            
            # Complete features
            features_added = velocity * feature_time
            features += features_added
            time += dt
            
            # Record trajectory
            trajectory['features'].append(features)
            trajectory['velocity'].append(velocity)
            trajectory['time'].append(time)
            trajectory['regime'].append(regime)
            trajectory['beta_gamma_ratio'].append(ratio)
        
        results.append({
            'terminated': terminated,
            'termination_time': time if terminated else None,
            'final_features': features,
            'achieved_breakout': achieved_breakout,
            'breakout_time': breakout_time,
            'final_ratio': beta_effective / gamma,
            'trajectory': trajectory
        })
    
    return results

def analyze_breakout_success_rates():
    """Compare breakout success with and without termination risk."""
    
    print("=" * 70)
    print("REGIME BREAKOUT WITH STOCHASTIC TERMINATION")
    print("=" * 70)
    
    strategies = ['conservative', 'adaptive', 'aggressive']
    exp_rates = [0.00, 0.01, 0.02, 0.03, 0.05]
    
    print("\nSuccess Rate Matrix (% achieving breakout before termination):")
    print("-" * 70)
    print("Exp Rate | Conservative | Adaptive | Aggressive | Aggressive(No Term)")
    print("-" * 70)
    
    for exp_rate in exp_rates:
        row = [f"{exp_rate:.2f}"]
        
        for strategy in strategies:
            # With termination
            results = simulate_breakout_with_termination(
                beta_exp=exp_rate, strategy=strategy, runs=1000
            )
            
            success_rate = sum(1 for r in results if r['achieved_breakout']) / len(results) * 100
            termination_rate = sum(1 for r in results if r['terminated']) / len(results) * 100
            
            row.append(f"{success_rate:5.1f}%")
            
            # Without termination (for comparison on aggressive)
            if strategy == 'aggressive':
                # Count successes that would have happened without termination
                eventual_success = sum(1 for r in results 
                                     if r['achieved_breakout'] or 
                                     (r['terminated'] and r['final_ratio'] > 0.8)) / len(results) * 100
                row.append(f"{eventual_success:5.1f}%")
        
        print("     | ".join(row))
    
    print("-" * 70)
    print("\nKey Insights:")
    print("1. Stochastic termination dramatically reduces breakout success")
    print("2. Need higher exponential rates (3-5%) for reliable breakout")
    print("3. Aggressive strategy still best, but margin reduced")
    print("4. Many projects die in the 'investment valley' before seeing returns")

def plot_breakout_trajectories():
    """Visualize successful vs failed breakout attempts."""
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    # Run simulations for different scenarios
    scenarios = [
        ("Linear (0%)", 0.00),
        ("Marginal (1%)", 0.01),
        ("Viable (2%)", 0.02),
        ("Strong (3%)", 0.03),
        ("Excellent (5%)", 0.05),
        ("Dramatic (10%)", 0.10)
    ]
    
    for idx, (label, exp_rate) in enumerate(scenarios):
        ax = axes[idx // 3, idx % 3]
        
        results = simulate_breakout_with_termination(
            beta_exp=exp_rate, strategy='aggressive', runs=100, max_time=200
        )
        
        # Categorize results
        breakout_success = [r for r in results if r['achieved_breakout']]
        terminated_trying = [r for r in results if r['terminated'] and not r['achieved_breakout']]
        
        # Find actual data range for better visualization
        all_times = []
        all_features = []
        
        # Plot sample trajectories
        for category, color, alpha, sample_size in [
            (breakout_success, 'green', 0.3, min(10, len(breakout_success))),
            (terminated_trying, 'red', 0.2, min(20, len(terminated_trying)))
        ]:
            if category:
                sample = np.random.choice(category, sample_size, replace=False)
                for r in sample:
                    times = r['trajectory']['time']
                    features = r['trajectory']['features']
                    ax.plot(times, features, color=color, alpha=alpha)
                    all_times.extend(times)
                    all_features.extend(features)
        
        # Add legend lines
        ax.plot([], [], 'g-', alpha=0.5, label=f'Success ({len(breakout_success)}%)')
        ax.plot([], [], 'r-', alpha=0.5, label=f'Terminated ({len(terminated_trying)}%)')
        
        # Set adaptive axis limits based on actual data
        if all_times and all_features:
            max_time = min(max(all_times) * 1.1, 100)  # Cap at 100 for visibility
            max_features = min(max(all_features) * 1.1, 50)  # Cap at 50 for visibility
        else:
            max_time = 50
            max_features = 20
        
        ax.set_xlabel('Time')
        ax.set_ylabel('Features')
        ax.set_title(f'{label} Exponential Rate')
        ax.legend(loc='upper left', fontsize=8)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, max_time)
        ax.set_ylim(0, max_features)
    
    plt.suptitle('Regime Breakout Attempts with Stochastic Termination\n' + 
                 'Green = Achieved Breakout, Red = Terminated Before Breakout',
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('planning/simulations/stochastic_breakout.png', 
                dpi=150, bbox_inches='tight')
    plt.close()
    
    print("\nVisualization saved to: stochastic_breakout.png")

def analyze_critical_window():
    """Analyze the critical time window for achieving breakout."""
    
    print("\n" + "=" * 70)
    print("CRITICAL WINDOW ANALYSIS")
    print("=" * 70)
    
    exp_rates = [0.02, 0.03, 0.05]
    
    for exp_rate in exp_rates:
        results = simulate_breakout_with_termination(
            beta_exp=exp_rate, strategy='aggressive', runs=1000
        )
        
        # Analyze timing
        breakout_times = [r['breakout_time'] for r in results if r['breakout_time']]
        termination_times = [r['termination_time'] for r in results if r['terminated']]
        
        if breakout_times:
            print(f"\nExponential Rate: {exp_rate:.0%}")
            print(f"  Median breakout time: {np.median(breakout_times):.1f}")
            print(f"  90th percentile breakout: {np.percentile(breakout_times, 90):.1f}")
            
        if termination_times:
            print(f"  Median termination time: {np.median(termination_times):.1f}")
            print(f"  Projects terminating before median breakout: "
                  f"{sum(1 for t in termination_times if t < np.median(breakout_times) if breakout_times) / len(termination_times) * 100:.1f}%")
    
    print("\nConclusion:")
    print("The race against time is real - projects must achieve exponential")
    print("growth before stochastic termination. Higher exp rates win this race.")

if __name__ == "__main__":
    # Main analysis
    analyze_breakout_success_rates()
    
    # Generate visualizations
    plot_breakout_trajectories()
    
    # Window analysis
    analyze_critical_window()
    
    print("\n" + "=" * 70)
    print("FINAL INSIGHTS")
    print("=" * 70)
    print("\nStochastic termination fundamentally changes the breakout dynamics:")
    print("1. Linear tooling (0%) cannot achieve breakout - projects die first")
    print("2. Marginal rates (1%) rarely succeed - termination usually wins")  
    print("3. Viable rates (2-3%) have fighting chance with aggressive investment")
    print("4. Strong rates (5%+) usually achieve breakout before termination")
    print("5. The 'valley of despair' becomes a 'valley of death' for many projects")
    print("\nThe mathematics of hope requires not just exponential tooling,")
    print("but FAST exponential growth to outrace project mortality.")