# Prior-Art Analysis: Shared Intent, Trust, and Bandwidth

**Target Claim:**
AAT frames inter-agent coordination strictly as an Information Bottleneck (IB) compression problem. "Shared Intent" is the IB-optimal compression of a sender's purposeful state (objective + strategy), preserving only what is relevant for joint action. From this, AAT derives the **Auftragstaktik Principle**: under limited bandwidth, it is mathematically optimal to prioritize sharing *objectives* over *strategies* over *models*.

Furthermore, AAT extends its geometric update gain to a **Communication Gain** ($\eta_{ji}^*$) that discounts incoming information by four distinct uncertainties: receiver model uncertainty, channel noise, source competence (epistemic uncertainty), and source alignment (teleological uncertainty). Because misplaced trust in an adversarial setting triggers a catastrophic Effects Spiral, AAT mandates a **risk-asymmetric (quantile/CVaR)** trust meta-model rather than a mean-expected Bayesian trust model.

---

## 1. State of the Field & Scientific Precedence

The Undermind search demonstrates that applying rate-distortion and information-theoretic limits to Multi-Agent Reinforcement Learning (MARL) and organizational design is a highly mature field. AAT's components—bandwidth-limited communication, delegation, separated trust models, and risk-sensitive evaluation—all possess deep structural priors.

### Pillar 1: Information Bottleneck in MARL Communication
The direct application of the Information Bottleneck to multi-agent communication is well established.
- **Wang et al. (2019)** in *Learning Efficient Multi-agent Communication: An Information Bottleneck Approach* proved that limited bandwidth requires low-entropy messages and explicitly used IB to learn compact communication protocols.
- **Mostaani et al. (2020)** formulated "task-based information compression," showing that communicating observations to maximize joint reward under rate limits is precisely a rate-distortion problem. 

### Pillar 2: Organizational Bandwidth and "Auftragstaktik"
The principle of prioritizing *what* over *how* (Auftragstaktik / Mission Command) has been formalized in organizational economics.
- **Dessein (2002)** in *Authority and Communication in Organizations* proved that a principal prefers to delegate control (share the objective and let the agent act) rather than communicate detailed state/strategy information, provided the incentive conflict (alignment) is not too large relative to uncertainty. 
- **Segal (2001)** analyzed coordination complexity, proving that transferring complete strategies requires exponentially more communication bandwidth than simply allocating authority based on shared objectives.

### Pillar 3: Multi-Dimensional Trust and Risk Sensitivity
The AI Trust literature explicitly separates competence from alignment/sincerity.
- **Villata et al. (2012)** and **Smith and desJardins (2009, 2005)** introduced multi-dimensional formal trust frameworks that explicitly evaluate agents on two separate axes: *competence* (probability of successful execution/accurate modeling) and *integrity/sincerity* (alignment with the principal's goals). This maps exactly to AAT's separation of $U_{\text{src}}$ and $U_{\text{align}}$.
- **Chow et al. (2015)** established the framework for risk-sensitive CVaR (Conditional Value-at-Risk) optimization in MDPs, demonstrating that bounding worst-case modeling errors requires using risk quantiles rather than risk-neutral expectations.

---

## 2. Key Anchor Papers (Available in `/ref`)

1. **Wang, R., et al. (2019). Learning Efficient Multi-agent Communication: An Information Bottleneck Approach.**
   *Significance:* Directly precedes AAT's use of IB to compress purposeful state in MARL under bandwidth constraints.
2. **Dessein, W. (2002). Authority and Communication in Organizations.**
   *Significance:* The economic formalization of Auftragstaktik, proving the optimality of delegation over detailed communication.
3. **Villata, S., et al. (2012). Trusting the Messenger and the Message.**
   *Significance:* Establishes the necessity of separating source competence from source sincerity in multi-agent trust models.
4. **Chow, Y., et al. (2015). Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach.**
   *Significance:* Provides the mathematical foundation for using risk-asymmetric (CVaR) quantiles to prevent catastrophic failure in MDPs.

---

## 3. Conclusion on Novelty & Overlap

The core components of AAT's shared intent and trust model are highly precedented. The application of IB to multi-agent communication is standard in recent MARL (Wang 2019). The separation of trust into competence and integrity is standard in Multi-Agent Systems (Smith 2005). The economic logic of Auftragstaktik is established (Dessein 2002).

**Where AAT actually contributes:**

1. **Shared intent as the third of four AAT compression operations (architectural-synthetic novelty; cross-row 19).** The IB compression of $G_t^{\text{full}} = (O_t, \Sigma_t)$ to $G_t^{\text{shared}}$ for relevance variable $a_t^{\text{coordinated}}$ is the *third* of AAT's four compression operations (epistemic model / strategy DAG / shared intent / composition projection). Placing inter-agent communication in the same compression family as belief construction, strategy formation, and macro-projection is an AAT-native architectural move. The U-medium honest distinction (shared shape, NOT single optimization problem) applies here just as for the other instances.

2. **The Auftragstaktik Principle as a *derived* prediction (theorem-grade content).** From the IB compression structure of shared intent: under limited bandwidth, prioritize **objectives** (compact, slow-changing) over **strategies** (moderate size, moderate change rate) over **strategic details** (large, fast-changing, low coordination value). This is not an economic choice or managerial convention — it follows structurally from the rate-distortion form: objectives give long shelf-life per bit transmitted when $\nu_O \ll \nu_\Sigma$. Dessein 2002 / Segal 2001 give economic ancestry; AAT's derivation route is information-bottleneck rather than incentive-compatibility.

3. **The Communication Gain Operator (theorem-grade math; AAT-native methodological invention).** Extends the Kalman/Fisher gain $\eta^* = U_M / (U_M + U_o)$ to a four-component form:
$$\eta_{ji}^* = \frac{U_M}{U_M + U_o + U_{\text{src}} + U_{\text{align}}}$$
where $U_{\text{src}}$ is source epistemic uncertainty and $U_{\text{align}}$ is source teleological uncertainty. This unifies pure sensor noise (rows 02/03) with game-theoretic deception (multi-agent trust) into a single computable geometric update scalar. Nash-style derivation: extension of Fisher-gain machinery to communication-with-trust setting in an AAT-internal axiomatic setting.

4. **Risk-asymmetric (CVaR) trust as structural requirement (synthetic novelty + theorem-grade content; cross-row 10).** AAT mandates a CVaR-quantile trust meta-model rather than mean-expected Bayesian trust. The reason is structural: misplaced trust in an adversarial setting triggers the row-10 Effects Spiral (the adversary's coupling term $\gamma_A$ amplifies once $B$ is past reserve). Mean-expected trust is incompatible with the spiral's positive-feedback structure; CVaR is necessary to bound the tail-event-driven destabilization. This makes risk-asymmetric trust a *structural requirement* rather than a preference. Chow et al. 2015 give the CVaR-optimization-in-MDPs ancestor; AAT's contribution is the structural-necessity linkage to the effects spiral.

5. **Multi-dimensional trust unified with the IB compression and Fisher-gain machinery (synthetic novelty).** Villata et al. 2012, Smith & desJardins 2005/2009 separate competence from sincerity. AAT places this in the same Fisher-gain coordinate system as observation quality, with $U_{\text{src}}$ and $U_{\text{align}}$ as named entries in the gain denominator. The two-axis trust framework is *integrated* into the cybernetic tracking machinery rather than treated as a separate management overlay.

6. **Connection to context-window discipline for AAT-internal agents (applied novelty).** The shared-intent compression is also useful for an agent preserving its own state across context boundaries — the language-model 100% context turnover problem. Store the IB-compressed purposeful state, not the full state. This is a concrete bridge to the `04-eli-core/` continuity-infrastructure work (where context-window resets are a primary substrate concern).

**AAT-native methodological inventions on this row:**
- The four-component Communication Gain $\eta_{ji}^* = U_M / (U_M + U_o + U_{\text{src}} + U_{\text{align}})$ unifying sensor noise and trust into the Fisher-gain framework.
- The CVaR-trust-as-structural-requirement linkage to the row-10 effects spiral.
- The placement of shared intent as the third of four compression operations (cross-row 19).
- The Auftragstaktik Principle as derived from rate-distortion structure (not economic theory).
- The Brave/conservative trust prior options and the dynamic-tightening update rule (cf. `hyp-communication-gain` Working Notes).

**Where AAT does *not* claim novelty:**
- IB compression for MARL communication (Wang et al. 2019, Mostaani 2020).
- The economic formalization of delegation / commander's intent (Dessein 2002, Segal 2001).
- The competence-vs-sincerity trust decomposition (Villata 2012, Smith & desJardins 2005/2009).
- CVaR optimization in MDPs (Chow et al. 2015).
- The Auftragstaktik concept itself (military doctrine from at least Moltke the Elder, 19th c.).
- The Fisher gain itself (Amari, classical adaptive filtering).

**Epistemic status of the load-bearing segments.**
- `#def-shared-intent` is `status: discussion-grade` (the IB formulation makes strong assumptions: sender knows jointly optimal action, lossless compression, fixed $\beta$).
- `#hyp-communication-gain` is `status: hypothesis-grade` (the four-component gain extension is structurally motivated but not yet validated empirically).
- `#hyp-auftragstaktik-principle` is `status: hypothesis-grade` (the bandwidth-prioritization prediction follows from the IB structure under the stated rate assumptions).
- `#impl-unity-communication` is `status: discussion-grade` (placement of shared intent inside the chapter-end implications).

**Novelty profile (per the meta-summary's four-axis rubric):**
- *Math Novelty:* **Some.** The communication-gain extension is theorem-grade derivation (Fisher-gain machinery extended to trust-augmented setting). The CVaR-trust-as-structural-requirement linkage to the spiral is derived from row 10's persistence machinery. Discussion-grade at the IB-formulation level; theorem-grade at the gain and persistence levels.
- *Arch Novelty:* **High.** Communication Gain with four-component trust expansion; CVaR-trust-as-structural-requirement; placement of shared intent in the compression-operations family; the brave-vs-conservative trust prior dynamics.
- *Synth Novelty:* **Medium.** Brings together IB-for-MARL-communication, multi-dimensional trust, CVaR risk-sensitive control, and Auftragstaktik economic theory under one Fisher-gain framework.
- *Appl Novelty:* **Some.** Direct application to multi-agent coordination + context-window discipline for AAT-internal agents (the LLM 100% context turnover bridge to 04-eli-core).
- *Impact:* **Medium.** Memo: "high impact if the IB-Auftragstaktik bandwidth-optimal claim becomes standard language for organizational communication design." The CVaR-trust-as-structural-requirement linkage is sharp enough to be useful, but the impact ceiling is bounded by the segments being discussion-grade and hypothesis-grade rather than derived.