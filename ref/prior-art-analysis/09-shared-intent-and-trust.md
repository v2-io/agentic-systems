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

**AAT's Novel Contribution:**
AAT's contribution here is almost entirely **Architectural Synthesis**, explicitly linking communication limits directly to the agent's internal control-theoretic variables.

1. **Unified Capacity Allocation:** While MARL researchers use IB to optimize neural network messages, and economists use game theory to model delegation, AAT unifies them by placing them on the same physical cybernetic metric: **Adaptive Tempo**. AAT frames Auftragstaktik not just as an economic choice, but as a mathematically required bandwidth allocation that minimizes the "closure defect" of a composite agent.
2. **The Communication Gain Operator:** AAT takes the Kalman/Fisher gain operator derived in its core tracking loop and structurally expands its denominator to include the trust terms ($\eta_{ji}^* = U_M / (U_M + U_o + U_{\text{src}} + U_{\text{align}})$). This elegantly unifies pure sensor noise with game-theoretic deception into a single, computable geometric update scalar. 
3. **Triggering the Effects Spiral:** By mandating a risk-asymmetric (CVaR) trust model, AAT explicitly links multi-agent trust directly back to its "Effects Spiral" No-Go theorem (Topic 08). It frames risk-asymmetric trust not merely as a preference, but as a structural requirement to prevent the adversary's $\gamma$-coupling term from collapsing the agent's Lyapunov persistence bound.