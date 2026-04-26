import numpy as np
import matplotlib.pyplot as plt

# AAD Agent Simulation: The Value of Causal Information Yield (CIY)
# Testing different exploration heuristics (lambda functions)

class AAD_Agent:
    def __init__(self, R_capacity, rho_env, lambda_type="constant", k=1.0):
        self.R = R_capacity # Structural capacity
        self.rho = rho_env # Environmental drift rate
        self.lambda_type = lambda_type
        self.k = k
        
        # State
        self.M_t = 0.0 # Agent's belief about Omega
        self.U_M = 1.0 # Agent's uncertainty (variance)
        
        self.total_reward = 0.0
        self.survival_time = 0
        self.is_alive = True

    def get_lambda(self, alpha):
        if self.lambda_type == "constant":
            return self.k
        elif self.lambda_type == "uncertainty_scaled":
            return self.k * self.U_M
        elif self.lambda_type == "lyapunov_bounded":
            # R* = rho / alpha (steady state mismatch bound)
            # If R* approaches R, lambda should explode to force exploration
            R_star = self.rho / max(alpha, 1e-5)
            margin = self.R - R_star
            if margin <= 0:
                return float('inf') # Panic: must explore!
            return self.k * self.U_M / margin
        else:
            return 0.0

    def step(self, Omega_t):
        if not self.is_alive:
            return Omega_t
            
        # 1. Action Selection (Evaluate Q_O + lambda * CIY)
        # Action 0 (Exploit): High reward if |M_t - Omega_t| is small. High observation noise U_o = 2.0 (Low CIY).
        # Action 1 (Explore): Zero reward. Low observation noise U_o = 0.1 (High CIY).
        
        U_o_exploit = 100.0
        U_o_explore = 0.01
        
        CIY_exploit = 1.0 / U_o_exploit
        CIY_explore = 1.0 / U_o_explore
        
        # Calculate current alpha (efficiency) assuming Exploit (greedy)
        # alpha = eta * c_min. Let c_min = 1.
        eta_exploit = self.U_M / (self.U_M + U_o_exploit)
        alpha_current = eta_exploit
        
        lmbda = self.get_lambda(alpha_current)
        
        # Expected reward based on current uncertainty
        # If U_M is high, expected reward is low
        expected_reward_exploit = max(0, 1.0 - self.U_M)
        expected_reward_explore = 0.0
        
        if np.isinf(lmbda):
            action = 1 # Force explore
            U_o = U_o_explore
        else:
            score_exploit = expected_reward_exploit + lmbda * CIY_exploit
            score_explore = expected_reward_explore + lmbda * CIY_explore
            
            if score_exploit > score_explore:
                action = 0 # Exploit
                U_o = U_o_exploit
            else:
                action = 1 # Explore
                U_o = U_o_explore
                
        if action == 0:
            # Actual reward depends on true mismatch
            true_mismatch = abs(self.M_t - Omega_t)
            reward = max(0, 1.0 - true_mismatch)
            self.total_reward += reward
            
        # 2. Environment Transition
        # Omega drifts
        Omega_next = Omega_t + np.random.normal(self.rho, 0.5)
        
        # 3. Observation
        observation = Omega_next + np.random.normal(0, np.sqrt(U_o))
        
        # 4. Epistemic Update (Kalman-like)
        eta_star = self.U_M / (self.U_M + U_o)
        delta_t = observation - self.M_t
        self.M_t = self.M_t + eta_star * delta_t
        
        # Update uncertainty
        # U_M grows due to environment drift/noise, shrinks due to observation
        self.U_M = (1 - eta_star) * self.U_M + 0.5 # Base environment noise variance
        
        # 5. Check Persistence
        true_mismatch_next = abs(self.M_t - Omega_next)
        if true_mismatch_next > self.R:
            self.is_alive = False
        else:
            self.survival_time += 1
            
        return Omega_next


def run_simulations():
    N_EPISODES = 500
    N_STEPS = 200
    R_capacity = 4.0
    rho_env = 0.5
    
    results = {}
    
    strategies = [
        ("constant", 0.0), # Greedy
        ("constant", 0.005),
        ("constant", 0.01),
        ("uncertainty_scaled", 0.01),
        ("lyapunov_bounded", 0.001)
    ]
    
    for lambda_type, k in strategies:
        survivals = []
        rewards = []
        
        for _ in range(N_EPISODES):
            agent = AAD_Agent(R_capacity, rho_env, lambda_type, k)
            Omega_t = 0.0
            
            for _ in range(N_STEPS):
                Omega_t = agent.step(Omega_t)
                if not agent.is_alive:
                    break
                    
            survivals.append(agent.survival_time)
            rewards.append(agent.total_reward)
            
        results[f"{lambda_type}_{k}"] = {
            "survival_rate": np.mean(np.array(survivals) == N_STEPS),
            "mean_survival_time": np.mean(survivals),
            "mean_reward": np.mean(rewards)
        }
        
    print(f"{'Strategy':<25} | {'Survival Rate':<15} | {'Mean Reward':<15}")
    print("-" * 60)
    for name, metrics in results.items():
        print(f"{name:<25} | {metrics['survival_rate']:.2%}          | {metrics['mean_reward']:.2f}")

if __name__ == "__main__":
    run_simulations()
