# Prior-Art Analysis: Scope Honesty via No-Gos (Tiered Approximation)

**Target Claim:**
AAT actively utilizes impossibility theorems and mathematical no-gos as "identifiability floors" to structure its architecture. Instead of treating approximations as heuristic degradations, AAT frames them as distinct, mathematically bounded tiers (e.g., L0 vs L1 vs L2 in causal hierarchies). When an exact causal or game-theoretic computation is blocked by a formal impossibility (a "no-go"), the agent acknowledges what is uncomputable and explicitly drops to a bounded approximation tier. This "scope honesty" turns negative mathematical results into constructive regime-switching boundaries for the agent's cognition.

---

## 1. State of the Field & Scientific Precedence

The Undermind search reveals a rich vein of literature concerning identifiability, unobservability, and fundamental limits in causality and control theory. The prior art establishes rigid mathematical boundaries specifying exactly when a system *cannot* infer causal reality or maintain control, providing the negative scaffolding that AAT utilizes.

### Pillar 1: Causal Identifiability and the Pearl Hierarchy
The strongest precedent for strict "identifiability floors" comes from the causal inference literature, particularly Pearl's Hierarchy (L1: Association, L2: Intervention, L3: Counterfactuals). 
- **Shpitser and Pearl (2008)** in *Complete Identification Methods for the Causal Hierarchy* provide the definitive algorithms characterizing exactly when a causal query *cannot* be computed from lower-level observational data. They give a complete graphical characterization of queries that are provably uncomputable, establishing strict boundaries on what an agent can infer.
- **Bareinboim and Pearl (2012, 2016)** extended this to transportability and data-fusion, proving completeness results that dictate when knowledge from one domain *cannot* be transferred to another without parametric assumptions. 
- **D'Amour (2019)** provides impossibility results for non-parametric identification under unobserved confounding, emphasizing the necessity of proxy variables or sensitivity analysis when exact inference hits a mathematical wall.

### Pillar 2: Information-Theoretic Limits in Control
AAT's use of no-gos extends beyond causal inference into control theory, where fundamental limits dictate when an agent can persist or stabilize.
- **Sahai and Mitter (2006)** on *Anytime Capacity* establish that Shannon capacity is insufficient for stabilizing unstable systems over noisy channels. They prove strict necessary conditions on information rates (reliability) required for stabilization—a direct precursor to AAT's use of information floors for survival.
- **Nair and Evans (2004)** derive explicit infimum data rates for stabilization under process and observation noise. When an agent drops below this data rate, control is mathematically impossible.

### Pillar 3: Elicitation and Epistemic Limits
The search also surfaced limits in multi-agent information elicitation. **Kong and Schoenebeck (2016)** and **Zheng et al. (2021)** define impossibility results for eliciting truthful posteriors in peer prediction without verification, proving what cannot be structurally known or trusted in decentralized settings.

---

## 2. Key Anchor Papers (Available in `/ref`)

1. **Shpitser, I., & Pearl, J. (2008). Complete Identification Methods for the Causal Hierarchy.** (`ref/shpitser_causal_hierarchy_2008.pdf`)
   *Significance:* The seminal paper proving exactly when effects of interventions cannot be computed from observational data, serving as the foundational "no-go" for causal identifiability.
2. **Bareinboim, E., & Pearl, J. (2016). Causal inference and the data-fusion problem.** 
   *Significance:* Establishes complete conditions for when synthesis of causal knowledge is mathematically impossible across heterogeneous domains.
3. **Sahai, A., & Mitter, S. (2006). The Necessity and Sufficiency of Anytime Capacity for Stabilization of a Linear System Over a Noisy Communication Link.**
   *Significance:* Proves that control and persistence require specific, bounded rates of information, establishing an information-theoretic "floor" below which an agent must fail.
4. **D'Amour, A. (2019). On Multi-Cause Causal Inference with Unobserved Confounding: Counterexamples, Impossibility, and Alternatives.**
   *Significance:* Highlights the hard limits of unobserved confounding, demonstrating that non-parametric identification is impossible in certain settings.

---

## 3. Conclusion on Novelty & Overlap

The mathematical "no-gos" themselves—such as the impossibility of identifying certain causal effects from observational data (Shpitser/Pearl) or the limits of stabilization over noisy channels (Sahai/Mitter)—are well-established and rigorously proven in the literature.

**AAT's Novel Contribution:** 
The novelty of AAT lies in its **architectural synthesis of these impossibility theorems**. Traditionally, an impossibility result (like unobserved confounding or non-identifiability) is treated as a failure mode for an algorithm, requiring a human statistician to step in and add parametric assumptions.

AAT, however, embeds these "no-gos" internally as **regime-switching boundaries for an autonomous agent**. By explicitly defining approximation tiers (e.g., L0 vs L1 vs L2), AAT allows the agent's architecture to detect when it hits an identifiability floor and dynamically drop to a bounded approximation stance. Turning negative methodological results into constructive, internal cognitive boundaries—"scope honesty"—represents a highly novel architectural feature that bridges theoretical impossibility with agentic engineering.