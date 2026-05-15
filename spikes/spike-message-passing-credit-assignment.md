# Spike: Exact Credit Assignment in Strategy DAGs via Message Passing

**Status.** Exploratory research spike.
**Date.** 2026-04-25.
**Pressure Point.** `#disc-credit-assignment-boundary` establishes that exactly assigning blame for a failed plan across an AND/OR strategy DAG is computationally #P-hard. To cope, AAT currently proposes a heuristic $L^2$ gradient update on the log-odds coordinates (`#hyp-edge-update-via-gain`). While the gradient provides "directional fidelity," it is an approximation that ignores the joint probability structure of the DAG.

This spike attempts to map the AAT Strategy DAG to a Factor Graph and apply Variational Message Passing (VMP) to derive a bounded, principled approximation algorithm for $\delta_{\text{strategic}}$ that respects the DAG's topological constraints.

## 1. Factor Graph Formulation of $\Sigma_t$

Let $\Sigma_t = (V_t, E_t, p_t, \gamma_t)$ be the strategy DAG (`#def-strategy-dag`).
- Each node $i \in V_t$ represents a state or milestone ($X_i \in \{0, 1\}$).
- Each edge $(i, j) \in E_t$ represents an action with credence $p_{ij}$, stored as natural parameter $\lambda_{ij} = \log(p_{ij}/(1-p_{ij}))$.
- $\gamma_j \in \{\text{AND}, \text{OR}\}$ defines the logical combination rule at node $j$.

We map this to a directed Factor Graph where the joint distribution over milestones is:
$$ P(X) = \prod_{j \in V_t} P(X_j \mid \text{Pa}(X_j), \lambda_{\cdot j}) $$

For an AND node $j$ with parents $\text{Pa}(X_j)$:
$$ P(X_j = 1 \mid \text{Pa}) = \prod_{i \in \text{Pa}} X_i \cdot \sigma(\lambda_{ij}) $$

For an OR node $j$:
$$ P(X_j = 0 \mid \text{Pa}) = \prod_{i \in \text{Pa}} (1 - X_i \cdot \sigma(\lambda_{ij})) $$

## 2. The Credit Assignment Problem as Posterior Inference

During execution, the agent observes the terminal outcome $X_{\text{goal}} = y_G$. It may also observe a subset of intermediate milestones $X_{\text{obs}}$.

The credit assignment problem is to compute the posterior distribution over the unobserved edges and intermediate nodes given the outcome: $P(X_{\text{unobs}}, \lambda \mid X_{\text{obs}})$. If the agent can compute this posterior, it can perform an exact Bayesian update on the log-odds $\lambda_{ij}$.

Because the graph contains deterministic logical gates (AND/OR) and is typically a loopy DAG (due to fallback paths), exact inference is #P-hard.

## 3. Variational Message Passing (VMP)

Instead of exact inference or the $L^2$ gradient heuristic, we apply Variational Message Passing (Wainwright & Jordan 2008). The agent constructs a fully factorized approximation distribution $Q(X, \lambda) = \prod Q_i(X_i) \prod Q_{ij}(\lambda_{ij})$ and minimizes the KL divergence:
$$ \min_Q D_{\text{KL}}(Q \Vert P(\cdot \mid X_{\text{obs}})) $$

**The Message Passing Rules:**
VMP operates by passing messages between nodes and factors. Because the natural parameters $\lambda_{ij}$ are in the exponential family, the updates take a clean analytical form.

- **Forward Pass (Prediction):** Nodes pass their expected activation $\mathbb{E}_Q[X_i]$ forward through the AND/OR factors. This exactly matches the topological sort already defined in `#def-strategy-dag`.
- **Backward Pass (Credit Assignment):** The observed terminal error at $X_{\text{goal}}$ creates a mismatch signal. The VMP backward message from an AND node $j$ to its parent $i$ is weighted by the *product of the expected activations of all other parents*. 
  - *Translation:* "If the AND gate failed, and I know the other prerequisites probably succeeded, it's your fault. If the other prerequisites probably failed, I don't know whose fault it is, so I won't update your $\lambda_{ij}$ strongly."

This structural property—where backpropagated blame is gated by the success of sibling prerequisites—is a massive upgrade over the naive $L^2$ gradient, which would blindly push all parents down simultaneously.

## 4. The Mean-Field Approximation Floor

*[Candidate Formulation for #disc-identifiability-floor]*

VMP uses a mean-field approximation ($Q$ is fully factorized). This mathematically breaks correlations between parallel paths in the DAG. 

If the strategy DAG contains L1 latent common causes (`#def-strategy-dag`), VMP will systematically misattribute blame. It will treat correlated failures as independent coincidences. 

Therefore, VMP is only a valid credit-assignment mechanism for L0 DAGs. If the DAG is L1 or L2, Variational Message Passing hits a structural floor. The agent must either use a structured variational approximation (retaining specific edges in $Q$) or rely on the covariance testing described in `#der-causal-insufficiency-detection`.

## 5. Conclusion and Theoretical Impact

By framing strategy updating as Variational Inference on a Factor Graph, we mathematically bridge AAT's planning module with modern approximate Bayesian inference. 

1. **Replaces Heuristics:** It replaces the $L^2$ gradient heuristic with a principled local message-passing algorithm that naturally handles the non-linear blame gating of AND/OR nodes.
2. **Computational Tractability:** VMP runs in linear time $O(|V| + |E|)$ per iteration, resolving the #P-hard bottleneck while providing bounded approximation guarantees.
3. **Explicit Limits:** It explicitly reveals its own failure mode (mean-field approximations break on L1 correlated structures), perfectly aligning with AAT's epistemic honesty.

## 6. Adversarial Critique & Structural Repair (2026-04-25)

**Adversarial Critique:** Variational Message Passing (VMP) relies on the mean-field approximation (assuming all variables are independent in the posterior $Q$). But the Strategy DAG is built entirely of AND/OR logical gates (`#scope-and-or`). Mean-field approximations are famously catastrophic on strict deterministic logical constraints (like parity checks or AND gates) because they smear probability mass across invalid configurations. VMP will completely fail to assign credit correctly; the updates will be garbage.

**Forward-Pass Repair:** Spot on. Standard mean-field VMP is the wrong algorithm for graphs dominated by deterministic logic.
*Fix:* The agent must use Expectation Propagation (EP) or Max-Sum (Belief Propagation) on a Factor Graph where the AND/OR gates are preserved as exact, un-factorized potentials. EP approximates the messages (keeping them in the exponential family) rather than approximating the joint distribution directly. This still solves the #P-hard exact inference problem by approximating the loopy structure, but it perfectly respects the local deterministic logic of the strategy nodes.

**Promotion Plan:**
- The mathematical core must be rewritten to use Loopy Belief Propagation or Expectation Propagation rather than Mean-Field VMP.
- Once fixed, this can be promoted to `01-aat-core/src/deriv-factor-graph-credit-assignment.md`.
- This will formally replace the $L^2$ gradient heuristic mentioned in `#def-strategic-calibration` and `#disc-credit-assignment-boundary` with a rigorous, bounded approximate-inference algorithm for computing $\delta_{\text{strategic}}$.

*(End of spike.)*