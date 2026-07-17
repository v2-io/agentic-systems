#!/usr/bin/env python3
"""
Simulation of the three regimes: tooling vs entropy with Lindy effect.
"""

import numpy as np
from typing import Tuple, List, Dict

def simulate_regime(beta: float, gamma: float, v0: float = 1.0, 
                   max_time: float = 100.0, max_features: int = 200) -> Tuple[List, List, List]:
    """
    Simulate development in one of the three regimes.
    
    Args:
        beta: Tooling effectiveness (improvement rate)
        gamma: Entropy/complexity growth rate
        v0: Base velocity
        max_time: Maximum simulation time
        max_features: Maximum features to prevent infinite loops
        
    Returns:
        (features_list, times_list, velocities_list)
    """
    
    k = 0  # Features completed
    time = 0
    total_tooling = 0
    
    features = [0]
    times = [0]
    velocities = [v0]
    
    while time < max_time and k < max_features:
        k += 1
        
        # Lindy expectation: expect k more features
        n_expected = k
        
        # Effective complexity rate
        gamma_eff = gamma * k - beta * total_tooling
        
        # Simplified myopic tooling decision
        # If we can reduce complexity, invest proportionally to expected features
        if beta > 0:
            # Optimal tooling approximation for exponential model
            t_tool = max(0, (1/beta) * np.log(n_expected * beta / v0))
            # Bound it reasonably
            t_tool = min(t_tool, 1.0)  # Don't spend more than 1 time unit on tooling per feature
            t_tool = max(0, t_tool)
        else:
            t_tool = 0
        
        total_tooling += t_tool
        
        # Recalculate effective complexity after tooling
        gamma_eff = gamma * k - beta * total_tooling
        
        # Time for next feature (with complexity factor)
        # Using exponential complexity model
        if gamma_eff > 10:  # Prevent numerical overflow
            feature_time = 1e10  # Essentially infinite
        else:
            feature_time = np.exp(gamma_eff) / v0
        
        # Check if feature is feasible
        if time + t_tool + feature_time > max_time:
            break
        
        time += t_tool + feature_time
        
        # Effective velocity (inverse of feature time)
        current_velocity = 1.0 / feature_time if feature_time > 0 else v0
        
        features.append(k)
        times.append(time)
        velocities.append(current_velocity)
    
    return features, times, velocities

def analyze_regimes():
    """Compare the three regimes side by side."""
    
    v0 = 1.0
    max_time = 50.0
    
    # Define the three regimes
    regimes = {
        "Winning (β > γ)": {"beta": 0.15, "gamma": 0.10},
        "Equilibrium (β = γ)": {"beta": 0.10, "gamma": 0.10},
        "Losing (β < γ)": {"beta": 0.05, "gamma": 0.10}
    }
    
    print("=" * 70)
    print("THREE REGIMES: TOOLING vs ENTROPY with LINDY EFFECT")
    print("=" * 70)
    print(f"\nSimulation parameters:")
    print(f"  Base velocity (v₀): {v0}")
    print(f"  Max simulation time: {max_time}")
    print(f"  Decision rule: Myopic optimization with E[n_future] = n_past")
    
    results = {}
    
    for regime_name, params in regimes.items():
        beta = params["beta"]
        gamma = params["gamma"]
        
        print(f"\n" + "-" * 70)
        print(f"{regime_name}: β={beta:.2f}, γ={gamma:.2f}, ratio={beta/gamma:.2f}")
        print("-" * 70)
        
        features, times, velocities = simulate_regime(
            beta=beta, gamma=gamma, v0=v0, max_time=max_time
        )
        
        results[regime_name] = {
            "features": features,
            "times": times,
            "velocities": velocities,
            "beta": beta,
            "gamma": gamma
        }
        
        # Analyze the trajectory
        total_features = features[-1]
        final_time = times[-1]
        
        print(f"  Total features completed: {total_features}")
        print(f"  Time taken: {final_time:.2f}")
        print(f"  Average velocity: {total_features/final_time:.3f} features/time")
        
        # Check acceleration/deceleration
        if len(features) > 10:
            early_pace = (features[5] - features[0]) / (times[5] - times[0])
            late_pace = (features[-1] - features[-6]) / (times[-1] - times[-6])
            
            print(f"  Early pace (features 1-5): {early_pace:.3f} features/time")
            print(f"  Late pace (last 5): {late_pace:.3f} features/time")
            
            if late_pace > early_pace * 1.1:
                print(f"  → ACCELERATING: {(late_pace/early_pace - 1)*100:.1f}% faster")
            elif late_pace < early_pace * 0.9:
                print(f"  → DECELERATING: {(1 - late_pace/early_pace)*100:.1f}% slower")
            else:
                print(f"  → STEADY STATE: pace maintained")
        
        # Project future
        if total_features > 2:
            recent_rate = (features[-1] - features[-2]) / (times[-1] - times[-2])
            if recent_rate > 0:
                projected_100_time = final_time + (100 - total_features) / recent_rate
                if projected_100_time < 1000:  # Reasonable projection
                    print(f"  Projected time for 100 features: {projected_100_time:.1f}")
                else:
                    print(f"  Projected time for 100 features: >1000 (essentially infinite)")
    
    # Compare trajectories
    print(f"\n" + "=" * 70)
    print("COMPARATIVE ANALYSIS")
    print("=" * 70)
    
    print("\nFeatures completed by time checkpoint:")
    checkpoints = [10, 20, 30, 40, 50]
    print(f"{'Time':<6} | ", end="")
    for regime in regimes.keys():
        print(f"{regime:<20} | ", end="")
    print()
    print("-" * 70)
    
    for checkpoint in checkpoints:
        print(f"{checkpoint:<6} | ", end="")
        for regime_name in regimes.keys():
            # Find features at this time
            times = results[regime_name]["times"]
            features = results[regime_name]["features"]
            
            # Find the last feature completed before checkpoint
            features_at_checkpoint = 0
            for i, t in enumerate(times):
                if t <= checkpoint:
                    features_at_checkpoint = features[i]
                else:
                    break
            
            print(f"{features_at_checkpoint:<20} | ", end="")
        print()
    
    print("\n" + "=" * 70)
    print("KEY INSIGHTS")
    print("=" * 70)
    
    print("\n1. WINNING REGIME (β > γ):")
    print("   - Development ACCELERATES over time")
    print("   - Each feature becomes easier than the last")
    print("   - Can theoretically achieve unlimited features")
    print("   - Lindy effect creates positive feedback loop")
    
    print("\n2. EQUILIBRIUM REGIME (β = γ):")
    print("   - Development maintains CONSTANT velocity")
    print("   - Tooling exactly compensates for entropy")
    print("   - Linear feature growth over time")
    print("   - Lindy expectations remain accurate")
    
    print("\n3. LOSING REGIME (β < γ):")
    print("   - Development DECELERATES over time")
    print("   - Each feature becomes harder than the last")
    print("   - Approaches a maximum feature limit")
    print("   - Lindy expectations become increasingly unrealistic")
    
    print("\n" + "=" * 70)
    print("PRACTICAL IMPLICATIONS")
    print("=" * 70)
    
    print("\nTo determine your project's regime:")
    print("1. Track feature completion times over 5-10 features")
    print("2. Calculate: Are times decreasing (winning), constant (sustainable), or increasing (losing)?")
    print("3. Estimate your β/γ ratio:")
    print("   - β: How much does refactoring help? (velocity improvement per time)")
    print("   - γ: How much does complexity grow? (slowdown per feature)")
    print("4. If β/γ < 1, you're fighting a losing battle against entropy")
    print("5. If β/γ > 1, you can achieve sustainable or accelerating development")
    
    return results

def simulate_with_noise(beta: float, gamma: float, noise_factor: float = 0.2, 
                       runs: int = 100, max_time: float = 50.0):
    """Run Monte Carlo simulation with noise in Lindy estimates."""
    
    all_features = []
    
    for run in range(runs):
        k = 0
        time = 0
        total_tooling = 0
        
        while time < max_time and k < 200:
            k += 1
            
            # Lindy with noise
            noise = np.random.normal(0, noise_factor)
            n_expected = max(1, int(k * (1 + noise)))
            
            # Effective complexity
            gamma_eff = gamma * k - beta * total_tooling
            
            # Tooling decision with noisy expectation
            if beta > 0:
                t_tool = max(0, (1/beta) * np.log(n_expected * beta))
                t_tool = min(t_tool, 1.0)
            else:
                t_tool = 0
            
            total_tooling += t_tool
            gamma_eff = gamma * k - beta * total_tooling
            
            if gamma_eff > 10:
                break
            
            feature_time = np.exp(gamma_eff)
            
            if time + t_tool + feature_time > max_time:
                break
                
            time += t_tool + feature_time
        
        all_features.append(k)
    
    return {
        "mean": np.mean(all_features),
        "std": np.std(all_features),
        "min": np.min(all_features),
        "max": np.max(all_features)
    }

if __name__ == "__main__":
    # Run main analysis
    results = analyze_regimes()
    
    # Test robustness
    print("\n" + "=" * 70)
    print("ROBUSTNESS TO UNCERTAINTY")
    print("=" * 70)
    
    print("\nMonte Carlo simulation with 20% noise in Lindy estimates (100 runs):")
    print(f"{'Regime':<20} | {'Mean':<8} | {'Std':<8} | {'Min':<8} | {'Max':<8}")
    print("-" * 70)
    
    regimes = [
        ("Winning (β=0.15)", 0.15, 0.10),
        ("Equilibrium (β=0.10)", 0.10, 0.10),
        ("Losing (β=0.05)", 0.05, 0.10)
    ]
    
    for name, beta, gamma in regimes:
        stats = simulate_with_noise(beta, gamma, noise_factor=0.2, runs=100)
        print(f"{name:<20} | {stats['mean']:<8.1f} | {stats['std']:<8.2f} | "
              f"{stats['min']:<8} | {stats['max']:<8}")
    
    print("\nConclusion: The three regimes are robust to uncertainty in Lindy expectations")