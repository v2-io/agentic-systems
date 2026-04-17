---
slug: observability-dominance
type: derived
status: robust-qualitative
depends:
  - strategy-dag
  - update-gain
stage: draft
---

# Derived: Observability Dominance

Unobservable strategy edges cannot be updated — the gain principle drives their update rate to zero. This means the agent's effective strategy is limited to the parts it can observe, regardless of the nominal confidence in unobservable paths. Observability dominates nominal confidence in determining which strategies are epistemically alive.

## Formal Expression

*[Derived (observability-dominance, from update-gain + strategy-dag)]*

For a path $P$ through $\Sigma_t$, the **path observability**:

$$\text{obs}(P) = \min_{v \in P} \sigma_v$$

where $\sigma_v$ is the observability of node $v$ — how well the agent can determine whether $v$ has been achieved. The weakest link determines the path's observability.

**Observability-adjusted confidence:**

$$\text{conf}_{\text{obs}}(P) = \text{conf}(P) \cdot \text{obs}(P)$$

When $\sigma_v \approx 0$ for any node $v$ on the path: by #update-gain, $\eta_{\text{edge}} = U_{\text{edge}} / (U_{\text{edge}} + U_{\text{obs}}) \to 0$ as $U_{\text{obs}} \to \infty$. The edges connecting to $v$ are **frozen at their prior** — the agent cannot update them regardless of what happens. The path is epistemically dead.

## Epistemic Status

*Robust qualitative.* The mechanism (high observation noise → low gain → frozen edges) is a direct consequence of #update-gain's uncertainty ratio. The specific functional form ($\text{conf}_{\text{obs}} = \text{conf} \cdot \text{obs}$) is a first-order approximation — the actual relationship between observability and effective confidence is more complex (it depends on how many observations are accumulated, the prior strength, and the noise structure). The qualitative prediction (low observability → frozen beliefs → ineffective strategy) is robust.

## Discussion

**Observability as the gateway to learning.** An agent choosing between a strong-but-blind path (high $\text{conf}(P)$, low $\text{obs}(P)$) and a weak-but-visible path (lower $\text{conf}(P)$, high $\text{obs}(P)$) should prefer the visible one. After one attempt: the visible path yields large $\eta_{\text{edge}}$ — the agent quickly learns whether it works and can redirect. The blind path yields tiny $\eta_{\text{edge}}$ — the agent is still guessing after $n$ attempts. Observability enables learning; opacity prevents it.

**Unobservable regions are absorbing.** Once significant strategy investment operates through unobservable nodes: frozen beliefs → no mismatch signal → no reason to revise → the agent cannot learn and cannot recognize that it cannot learn. Escape requires external shock, proactive observability investment (instrumenting previously unmonitored nodes), or another agent whose observations cover the blind spot ( #communication-gain).

**Connection to #code-quality-as-observation-infrastructure (cross-component reference — see `02-tst-core/`).** In the software domain, code quality directly determines $\sigma_v$ — well-structured code with good tests makes strategy steps (features, refactors, deployments) observable. Poor code quality reduces observability, freezing the developer's causal beliefs about what changes will accomplish. This makes code quality a strategic concern, not just an aesthetic one.

**Optimal decomposition depth.** Finer decomposition (more intermediate nodes) provides earlier failure detection — detect a problem at step $k$ rather than discovering it at step $n$. But finer decomposition also increases the number of uncertain edges ( #chain-confidence-decay). The optimal decomposition depth balances incremental confirmation against compound decay: decompose as finely as observation channels allow, but no finer.

**Quantitative content from the two-edge case.** The analysis in #strategic-dynamics-derivation (Props B.2-B.3) instantiates this result for the minimal multi-edge chain $A \to B \to G$, giving the qualitative claims above precise mathematical form.

*Observable intermediate $B$.* When the agent can observe whether $B$ was achieved, each edge gets independent Bayesian updates. The per-edge sector parameters are $\alpha_1 = 1/(n_1+1)$ and $\alpha_2 = \theta_1/(n_2+1)$, where $\theta_1$ is the true success probability of the first edge. The overall sector parameter is $\alpha_\Sigma = \min(\alpha_1, \alpha_2)$ — a weakest-link result. The $\theta_1$ factor in $\alpha_2$ is the **evidence-starvation effect**: downstream edge 2 can only be tested when upstream edge 1 succeeds (with probability $\theta_1$), so its effective correction rate is attenuated by $\theta_1$. For a depth-$d$ chain, this generalizes to $\alpha_k = \prod_{j<k}\theta_j / (n_k+1)$ — the deepest edge faces exponential attenuation. This is derived for the two-edge case and conjectured (with clear inductive mechanism) for depth-$d$.

*Unobservable intermediate $B$.* When the agent observes only the terminal outcome $y_G$, per-edge identification fails entirely. The marginal Bayesian update has a systematic bias: the zero-correction-at-truth property (A1) is violated with bias $O(1/n)$. The agent's point-estimate updates for each edge are downward-biased because success always credits both edges fully ($\alpha_k \to \alpha_k + 1$), but failure distributes blame fractionally via proportional attribution. The proportional-blame update turns out to be exactly the marginal Bayesian point estimate — not a heuristic — but it discards the posterior correlation that failure introduces between the edge beliefs.

The consequence is stronger than "frozen edges": unobservable intermediates don't just prevent updating — they make per-edge identification impossible, forcing the agent to plan-level aggregation. If the agent tracks $\hat{\Phi} = p_1 p_2$ as a single Beta on the plan's overall success probability, the single-edge sector condition applies with $\alpha_{\Sigma,\text{plan}} = 1/(n_\Phi + 1)$. But diagnostic resolution is lost: the agent knows the plan is failing but cannot localize which step needs revision.

*The observability investment tradeoff.* Making $B$ observable yields a quantifiable improvement in $\alpha_\Sigma$: from the plan-level rate $1/(n_\Phi+1)$ to the per-edge weakest-link rate $\min(1/(n_1+1), \theta_1/(n_2+1))$. The improvement is positive whenever $\theta_1 > 1/2$ and experience is distributed similarly across edges. This gives the observability-dominance principle concrete economic content: the value of instrumenting an intermediate node is the difference in sector parameters, which translates directly to persistence margin.

## Working Notes

- The absorbing-state property of unobservable regions is a strong prediction. In organizational settings, it predicts that departments with poor measurement (R&D, strategy groups, some management functions) will develop persistent, untested beliefs about their own effectiveness. The theory predicts this is structural (frozen $\eta_{\text{edge}}$), not motivational.
- Observability is not binary — it's a spectrum. Partial observability (noisy observations of intermediate results) gives partial gain, which gives slow but nonzero learning. The diagnostic question is whether the learning rate is fast enough to maintain strategy persistence given the environment's rate of change ($\rho$).
