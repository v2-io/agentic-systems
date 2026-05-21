# Prior-Art Analysis: Lyapunov Persistence and Sector Conditions

**Target Claim:**
AAT models agent survival (persistence) fundamentally as a dynamical-systems tracking problem rather than an optimization problem. The agent's correction mechanism is bounded by a "sector condition" (efficiency $\alpha$, measuring how well the correction points toward reality). Persistence is achieved only when the correction rate exceeds the effective disturbance rate divided by the agent's reserve. 

AAT derives a strict **scaling dichotomy**: against deterministic drift (Model D), mismatch scales linearly as $1/\alpha$; against stochastic noise (Model S), the root-mean-square mismatch scales as $1/\sqrt{\alpha}$. Finally, AAT links this tracking bound to information theory, proving that maintaining persistence against noise requires a strict minimum Shannon information acquisition rate (an information-rate floor).

---

## 1. State of the Field & Scientific Precedence

The Undermind search yields highly mature prior art across nonlinear control, adaptive filtering, and networked control theory. AAT's use of sector bounds, drift rejection, and information-rate floors are deeply grounded in these classic fields.

### Pillar 1: Sector Conditions and Absolute Stability
AAT's core persistence template leverages the "sector condition" ($\xi^T F(\xi) \geq \alpha \lVert \xi \rVert^2$). 
- **Zames (1966)** and the classic **Lur'e Problem** established sector bounds as the canonical way to prove absolute stability for nonlinear feedback systems using Lyapunov functions.
- In **Monotone Operator Theory (Bauschke & Combettes, 2017)**, AAT's specific local sector condition is recognized mathematically as "one-point strong monotonicity." Operator-theoretic perturbation bounds routinely use Lyapunov techniques to establish that bounded input perturbations yield bounded state errors for strongly monotone operators.

### Pillar 2: Tracking Error Scaling Dichotomy ($1/\alpha$ vs $1/\sqrt{\alpha}$)
The claim that tracking error scales fundamentally differently under deterministic drift versus stochastic noise is a canonical result in the theory of adaptive signal processing.
- **Widrow et al. (1976, 1984)** in their seminal analyses of the LMS (Least Mean Squares) adaptive filter established exactly this dichotomy. They proved that in non-stationary environments, "lag error" (from deterministic drift) decreases linearly with adaptation step-size ($\mu$), while "gradient noise" (from stochastic disturbance) increases with $\sqrt{\mu}$. 
- **Ljung and Priouret (1991)** generalized these tracking bounds for generic recursive stochastic algorithms, cementing the $1/\mu$ vs $1/\sqrt{\mu}$ trade-off as the fundamental limit of tracking non-stationary environments.

### Pillar 3: Information-Rate Floors and Control Capacity
The claim that maintaining tracking bounds requires a strict minimum Shannon information rate is thoroughly established in networked control.
- **Nair and Evans (2004)** and **Tatikonda and Mitter (2004)** established the "Data Rate Theorem," proving the minimum channel capacity required to stabilize an unstable linear system.
- **Sahai and Mitter (2006)** tightened this with *Anytime Capacity*, proving that Shannon capacity alone is insufficient for stabilization with bounded moments over noisy channels; a stricter, persistent information rate is required to prevent tail events from destroying the system.
- **Lestas, Vinnicombe, and Paulsson (2010)**, in *Nature*, applied information-theoretic bounds to biological control loops, proving strict fundamental limits on the suppression of molecular fluctuations (the "quartic root law"), which mirrors AAT's use of information floors for physical persistence.

---

## 2. Key Anchor Papers (Available in `/ref`)

1. **Sahai, A., & Mitter, S. (2006). The Necessity and Sufficiency of Anytime Capacity for Stabilization of a Linear System Over a Noisy Communication Link.**
   *Significance:* The definitive proof that persistence/stabilization over noise requires a strict, continuous minimum information rate, directly validating AAT's information-rate floor.
2. **Lestas, I., Vinnicombe, G., & Paulsson, J. (2010). Fundamental limits on the suppression of molecular fluctuations.** (`ref/lestas_fluctuations_2010.pdf`)
   *Significance:* Demonstrates how information-theoretic limits govern the physical survival and regulation of biological agents, bridging control theory and living cybernetics.
3. **Widrow, B., et al. (1976). Stationary and nonstationary learning characteristics of the LMS adaptive filter.**
   *Significance:* The seminal paper establishing the $1/\alpha$ vs $1/\sqrt{\alpha}$ scaling dichotomy for tracking error against drift versus stochastic noise.
4. **Zames, G. (1966). On the input-output stability of time-varying nonlinear feedback systems.**
   *Significance:* The foundational text for sector conditions and absolute stability in control.

---

## 3. Conclusion on Novelty & Overlap

Every mathematical component of AAT's persistence bounds—sector conditions, the $1/\alpha$ vs $1/\sqrt{\alpha}$ scaling dichotomy, and the Shannon rate floor—is a canonical, heavily-cited result in adaptive filtering and nonlinear control. 

**AAT's Novel Contribution:**
AAT achieves **architectural novelty** by elevating these physical control theorems into a universal template for epistemic and teleological agency. 

1. **Unifying the Substrate:** AAT's "Sector-Persistence Template" mathematically unifies disparate agentic phenomena—epistemic belief updating, strategic plan validation, multi-agent coordination, and adversarial destabilization—by proving they are all instances of the exact same Lur'e/Monotone-Operator problem. It proves that the same $1/\sqrt{\alpha}$ scaling law that governs a hardware LMS filter tracking a radio signal also governs a general intelligence tracking an adversary's strategy.
2. **Broader Validity than Active Inference:** AAT explicitly contrasts its Lyapunov sector approach with the Free Energy Principle (FEP). While FEP relies on the assumption that agents flow toward the minimum of a variational free energy landscape on a non-equilibrium-steady-state (NESS) density—an assumption mathematically narrow for nonlinear systems (Aguilera 2022)—AAT proves that the standard Lyapunov sector condition provides strict bounds without requiring NESS or a free energy gradient. AAT achieves the universal stability claims of Active Inference using a much broader, more rigorously established control-theoretic foundation.