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

**Where AAT actually contributes:**

1. **The Sector-Persistence Template as a universal agency machinery (architectural-synthetic novelty + theorem-grade content).** AAT proves that disparate agentic phenomena — epistemic belief updating, strategic plan validation, multi-agent coordination, adversarial destabilization, composite tempo accounting, wrapper-induced class coercion, resource-bounded depletion — are all instances of the *same* sector-persistence template. The template itself is `#result-sector-persistence-template` with state variable $\xi$, correction function $F$, sector parameter $\alpha$, basin radius $R$, and disturbance rate $\rho$, and the per-instance derivations transcribe the template with instance-specific bindings. Each transcription is a Nash-style theorem: new derivation using established Lur'e / Lyapunov / sector-bound machinery in an AAT-internal axiomatic setting.

2. **The Model D / Model S scaling dichotomy ($1/\alpha$ vs $1/\sqrt{\alpha}$) as AAT-derived theorem (theorem-grade math).** Widrow's LMS-filter dichotomy and Ljung-Priouret's tracking bounds give the established ancestor. AAT's specific contribution is the *exact* statement of the dichotomy inside the persistence template under named conditions (Models D and S), with the propagation through composite tempo, adversarial destabilization (giving $b = 2$ / $b = 3/2$ adversarial advantage exponents), and resource-bounded depletion. The dichotomy *as stated in the template* is AAT-internal; the propagation to multiple consequence rows is the synthesis.

3. **The information-rate floor for stochastic persistence (theorem-grade math).** Maintaining persistence against noise requires a strict minimum Shannon information acquisition rate. The Sahai-Mitter / Nair-Evans / Tatikonda-Mitter anytime-capacity result is the closest external ancestor; AAT's contribution is the application to *agent persistence* (rather than channel-rate-for-stabilization) and the link to the Model S $1/\sqrt{\alpha}$ scaling. Nash-style derivation.

4. **The Lyapunov-vs-NESS critical contrast (architectural-synthetic novelty).** AAT proves that the standard Lyapunov sector condition provides strict bounds without requiring NESS density assumptions, which Aguilera (2022) and others have shown are mathematically narrow for nonlinear systems. The same universal stability claims as Active Inference are obtained via much broader, classically established Lyapunov-control-theoretic foundations. This is structurally why AAT can apply across a wider range of agent types than FEP can — a structural contribution, not just a notational variant.

**AAT-native methodological inventions on this row:**
- The Sector-Persistence Template as a one-stop instantiation form for diverse agentic dynamics.
- The named Model D / Model S regime split with the $1/\alpha$ / $1/\sqrt{\alpha}$ scaling dichotomy.
- The adaptive-reserve quantity $\Delta \rho^\ast = \alpha R - \rho$ as a finite per-step agent-available read.
- The information-rate floor as a structural condition on agent persistence (not just stabilization of a plant).
- The Lyapunov-without-NESS positioning relative to FEP.

**Where AAT does *not* claim novelty:**
- Sector conditions / Lur'e problem (Zames 1966).
- $1/\mu$ vs $1/\sqrt{\mu}$ adaptive-filter scaling (Widrow et al. 1976, 1984; Ljung-Priouret 1991).
- Data Rate Theorem (Nair-Evans 2004, Tatikonda-Mitter 2004).
- Anytime Capacity (Sahai-Mitter 2006).
- Lestas-Vinnicombe-Paulsson fluctuation suppression limits (2010).
- Lyapunov stability / monotone-operator theory itself.

**Novelty profile (per the meta-summary's four-axis rubric):**
- *Math Novelty:* **High.** The Sector-Persistence Template plus the Model D / Model S dichotomy plus the information-rate floor plus the adaptive-reserve construct plus the multiple per-instance template transcriptions = multiple substantive theorem-grade derivations. Per the math-novelty-recognition discipline: Nash-style applications of established machinery (Zames, Widrow, Sahai-Mitter) to AAT-internal axiomatic settings are math content.
- *Arch Novelty:* **High.** Universal template + Model D / Model S split + adaptive reserve + Lyapunov-without-NESS positioning.
- *Synth Novelty:* **High.** Unifies adaptive filtering, networked control, biological persistence (Lestas), and Lyapunov stability under one agency-applicable template.
- *Appl Novelty:* **None.** No domain-specific instantiation in this row.
- *Impact:* **High.** Per the meta-summary's Part 2 — AAT provides a structurally superior alternative to FEP's NESS assumption, achieving the same universal stability claims via "mathematically unassailable control-theoretic Lyapunov bounds, entirely bypassing the fragile NESS density requirement." This is one of AAT's strongest cross-disciplinary contributions because it gives Active Inference a cleaner foundation.