# Batch 10 — Appendices interleaved (catch-up)

Joseph reminder: pull appendices when first referenced. Earlier batches only pulled  
`#deriv-recursive-update`, `#deriv-observation-ambiguity-bias-bound`, `#deriv-self-actuation-grounding`.  
This batch backfills the load-bearing ones along the walk order.

## Order of first reference → appendix

| First main segment | Appendix / template |
|---|---|
| `#der-recursive-update` | `#deriv-recursive-update` ✓ earlier |
| `#emp-update-gain` | `#deriv-fisher-local-update-gain`, `#deriv-adaptive-gain-dynamics` |
| `#def-adaptive-tempo` | `#deriv-tempo-additivity`, `#deriv-fisher-local-update-gain` |
| `#hyp-mismatch-dynamics` | `#deriv-sector-condition` |
| `#der-gain-sector-bridge` | `#deriv-gain-sector` |
| `#result-sector-condition-stability` | `#deriv-sector-condition`, `#result-sector-persistence-template` |
| `#result-persistence-condition` | `#result-sector-persistence-template`, `#deriv-persistence-cost` |
| `#disc-stability-certificate` | `#result-certificate-existence` |
| (fluid-limit claims) | `#deriv-discrete-sector-condition` |
| (Model S pathwise) | `#deriv-stochastic-non-exit` |
| `#def-strategy-dag` | `#deriv-graph-structure-uniqueness` |
| `#der-orient-cascade` / observability | `#deriv-edge-credence-dynamics` |
| `#def-value-object` / sat-gap | `#deriv-convention-monotonicity` |
| `#disc-continuity-stance` | `#deriv-self-actuation-grounding` ✓ earlier |
| Class-3 bias | `#deriv-observation-ambiguity-bias-bound` ✓ earlier |

Not fully body-read yet (still open if deepening further):  
`#deriv-adaptive-gain-dynamics`, `#deriv-matrix-persistence-condition`, `#result-contraction-template`,  
`#deriv-critical-mass-composition`, `#deriv-mechanism-counterfactual-separation`,  
`#deriv-causal-ib-lmi` / `#deriv-causal-ib-exploration`, `#deriv-strategy-cost-regret-bound`,  
`#deriv-reward-channel-learning-no-go`, `#deriv-strategic-composition`.

---

## What I hadn't anticipated in the appendices

### Lyapunov spine (`#deriv-sector-condition` + `#result-sector-persistence-template`)

- **Lemma A.1N tightness is class-level, not agent-level.** Floor failure loses the *certificate*; escape is forced only for radially tight (linear) correctors. The “dip counterexample” — weak spot the trajectory never reaches — is pedagogically brutal and correct.
- **Corollary A.1S.1 containment dichotomy:** Model D → $P(\tau_R<\infty)=0$; Model S → $P(\tau_R<\infty)=1$ for *any* $\alpha$. Correction strength cannot interpolate. Pathwise forever is categorically Model-D-only. Structural adaptation under stochastic environments is *generic eventual*, not edge-case. That rewrites the mood of `#result-structural-adaptation-necessity`.
- **Template as taxonomic economy:** epistemic, strategic, team, closure, tempo, adversarial, identity-continuity = same (T1–T3) with different $(\xi, F, \rho_\xi, R)$. Persistence and destabilization are one inequality flipped.
- **One-point vs two-point again:** (T2) one-point for single-agent; composition bridge needs DA2'-inc two-point. Monotone-operator lineage named as specialization, not invention.

### Certificate existence (`#result-certificate-existence`)

- Operator-sector in *some* metric ⟺ exponential stability — equivalence, not analogy.
- **R0-loss ⟸ R0-strict ⟸ R1 ⟸ R2** ladder: certificate without contraction (imaginary-axis eigenvalues) is a real rung, not a failure. Fisher forced only at R2.
- Naming $\mathcal{M}$ (the metric) rather than $V=e^\top\mathcal{M}e$ is what makes the meta-facets expressible.

### Gain exactness (`#deriv-fisher-local-update-gain`, `#deriv-gain-sector`)

- $\eta^\ast = U_M/(U_M+U_o)$ falls out three ways (Laplace, Bregman/KL Pythagorean, Cramér-Rao precision add) — agreement *is* the Fisher-local regime.
- Matrix $K=(H_M+H_L)^{-1}H_L$ is the primitive; scalar tempo is shared-eigenbasis collapse.
- Bridge is **conditional on directional fidelity**, not free from gain form alone — pathological $R_{90°}g$ exists.

### Discrete fluid limit (`#deriv-discrete-sector-condition`)

- Continuous needs only one-sided sector; discrete needs **DA2'b Lipschitz** because of $(\eta^\ast)^2\|F_d\|^2$ term. Fluid limit zero-gap Model D; $O(\eta c_{\max})$ Model S. Completes Part I formal chain.

### Stochastic non-exit no-go (`#deriv-stochastic-non-exit`)

- Ville/Doob route fails: compensated supermartingale is *sign-indefinite inside the basin*. Unbounded scale function ⇒ no non-constant bounded harmonic ⇒ no horizon-independent non-exit. Reusable signature for future stochastic-containment attempts.

### Persistence cost (`#deriv-persistence-cost`)

- Threshold says *possible*; $\dot R \geq n\alpha/2$ nats/time says *sustained cost*. Kalman-Bucy saturates. Survival = burn rate. $C \geq \mathcal{T}/2$ as first-class prerequisite — channel is part of staying in scope.

### Tempo additivity (`#deriv-tempo-additivity`)

- Signed $\Delta$: redundancy *and* synergy. Additive form is **not** a general upper bound. Echo-chamber closed-form penalty + saturation (shared bias floor). Two no-gos: CMI cannot be the correction; no convention-free per-channel split for $n\geq 3$.

### Strategy appendices

- **Graph uniqueness** (`#deriv-graph-structure-uniqueness`): *sufficient* for DAG+Markov, not Cox-strength necessary. Acyclicity proved from time; Markov under causal sufficiency. Honest gap.
- **Edge credence** (`#deriv-edge-credence-dynamics`): full topology set — AND depth-gates, OR exploration-gates, unobservable intermediate kills per-edge sector (plan-level salvage), L1' unobservable-$C$ refuted by Cramér-Rao (identifiability floor Instance 2). B.5 plan-confidence transfer is credit-assignment-free.
- **Convention monotonicity** (`#deriv-convention-monotonicity`): right rung free; left rung false without order-consistency; RH-1/2/3 force it. Counterexample of myopic dead-end exists.

---

## How this changes the experiential read

1. **Part I climax is the dichotomy + no-go pair**, not just $\alpha>\rho/R$. Stochastic life means you will eventually need structural change; parametric persistence is mean-square / fixed-time, never eternal pathwise.
2. **Template is the hidden spine of Part III** — adversarial, team, closure all just specialize $\rho_\xi$.
3. **Gain “exact” is Fisher-local exact** — empirical label on the main segment is honest about outside that regime.
4. **Observability dominance is not handwave** — B.2–B.3 prove freeze / plan-level collapse.
5. **Composition’s bridge lemma need for DA2'-inc** is why discrete appendix exists, not pedantry.

## Still-open appendix pull list (if continuing)

Priority if Joseph wants full AAT-appendix experience next:  
`#deriv-adaptive-gain-dynamics` (mood/MG coupling), `#deriv-matrix-persistence-condition`, `#result-contraction-template`, `#deriv-critical-mass-composition`, `#deriv-mechanism-counterfactual-separation`, `#deriv-reward-channel-learning-no-go` (agency-death input leg), `#deriv-causal-ib-lmi`.
