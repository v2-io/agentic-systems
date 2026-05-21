# Prior-Art Analysis: Information Bottleneck Unification

**Target Claim:**
AAT demonstrates how the Information Bottleneck (IB) principle serves as a unified variational framework across the agent's entire cognitive architecture: reality modeling ($M_t$), strategic planning ($\Sigma_t$), and communication. Specifically, in the strategy layer, AAT formulates the cognitive cost of a strategy as an IB objective balancing description length against decision-relevance. 

Crucially, AAT derives this variational form strictly as an upper bound on decision-theoretic regret. Under deterministic optimal policies, AAT proves that this regret-bound derivation mathematically forces the specific direction of the KL-divergence term (reverse-KL, $\pi^\ast$-first) to avoid the "forward-KL infinity degeneracy" and the "Shannon-zero degeneracy." AAT explicitly contrasts this with Active Inference, achieving the same "variational inference" shape but deriving it natively from control-theoretic regret rather than assuming "preferences as priors."

---

## 1. State of the Field & Scientific Precedence

The Undermind search reveals a massive, highly active literature unifying information theory, compression, and optimal control. The idea of using variational free energy or rate-distortion theory as a universal objective for bounded rational agents is one of the most thoroughly explored paradigms in modern theoretical AI.

### Pillar 1: Information Theory of Decisions and Actions
The direct application of the Information Bottleneck to action selection is canonical.
- **Tishby and Polani (2011)** in *Information Theory of Decisions and Actions* pioneered the formalization of agency as an information channel. They explicitly modeled the trade-off between the expected utility of an action and the Shannon information required to process the state-to-action mapping.
- **Fox and Tishby (2016)** extended this to *Minimum-Information LQG Control*, formulating the bounded controller strictly as a sequential rate-distortion problem, establishing the exact math AAT uses to balance compression against control performance.
- **Genewein, Leibfried, and Braun (2015)** and **Ortega et al. (2015)** formalized *Information-Theoretic Bounded Rationality*, proving that agents trading off utility maximization against information-processing costs inherently optimize a free-energy functional.

### Pillar 2: Control as Inference (KL Control)
The mathematical unification of optimal control and probabilistic inference is well established.
- **Todorov (2006)** introduced *Linearly-Solvable MDPs*, showing that by adding a KL-divergence control cost penalizing deviation from uncontrolled dynamics, the Bellman equation becomes linear and optimal control reduces to an inference problem.
- **Kappen (2005, 2009)** generalized this into *Path Integral Control*, proving that stochastic optimal control problems can be universally reformulated as Kullback-Leibler (KL) minimization problems.

### Pillar 3: Active Inference and Free Energy
- **Friston, FitzGerald, Rigoli, et al. (2015, 2017)** provide the most famous unified variational framework: Active Inference. Here, both perception and action minimize a single variational free energy bound. Crucially, Active Inference achieves this unification by encoding goals as prior beliefs ($C(o) = \log P_{\text{pref}}(o)$), treating action selection as inferring the trajectory that makes preferred outcomes most likely.

---

## 2. Key Anchor Papers (Available in `/ref`)

1. **Tishby, N., & Polani, D. (2011). Information Theory of Decisions and Actions.** (`ref/tishby-polani-2011-info-decision-action.pdf`)
   *Significance:* The seminal text establishing the application of information capacity limits and rate-distortion theory directly to agentic action selection.
2. **Ortega, P. A., et al. (2015). Information-Theoretic Bounded Rationality.** 
   *Significance:* Provides the axiomatic justification for using free energy functionals to characterize decision-making under resource limitations.
3. **Todorov, E. (2006). Linearly-solvable Markov decision problems.** 
   *Significance:* The foundational paper for "KL Control," demonstrating that penalizing policies via KL-divergence transforms control into inference.
4. **Friston, K. J., et al. (2015). Active inference and epistemic value.** 
   *Significance:* The definitive formulation of how expected free energy unifies pragmatic (utility) and epistemic (information) value into a single variational objective.

---

## 3. Conclusion on Novelty & Overlap

The core concept of unifying an agent's architecture under a single variational/information-theoretic objective (like IB or Free Energy) is **highly precedented and represents settled science**. Tishby, Todorov, Ortega, and Friston have thoroughly established the equivalence of control, inference, and compression. AAT does not claim novelty in the "shape" of the IB objective.

**AAT's Novel Contribution:**
AAT's novelty here is entirely **derivational and epistemological**, specifically regarding *how* the variational shape is justified.

1. **Deriving the KL-Direction via Regret Bounds:** In standard KL-control (Todorov) and Bounded Rationality (Ortega), the KL-divergence term is usually introduced axiomatically as a regularizer or cost-of-computation. AAT achieves **pure mathematical novelty** by proving that the specific KL term must be *reverse-KL* ($\pi^\ast$-first) to avoid mathematical singularities. AAT derives this by proving that the IB objective acts as a strict upper bound on decision-theoretic regret (via Pinsker's and Bretagnolle-Huber identities). AAT shows that if the opposite KL direction were used, the bound evaluates to $+\infty$ whenever the strategy places any mass off the deterministic optimum. 
2. **Escaping the "Preferences as Priors" Trap:** AAT explicitly positions its derivation against Active Inference. By deriving the variational objective strictly from a decision-theoretic regret bound, AAT achieves the elegant "variational inference" shape of Friston's Free Energy without ever having to assume "preferences as priors" (which collapses the diagnostic orthogonality AAT requires, as discussed in Topic 13). 

AAT's contribution is showing that one can arrive at the universal variational architecture of Active Inference through the rigorous, deterministic survival bounds of control theory, patching the epistemological holes in the process.