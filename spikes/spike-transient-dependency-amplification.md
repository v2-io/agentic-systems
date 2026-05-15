# Spike: Transient Dependency Amplification and the Logogenic Lipschitz Constant

**Status.** Exploratory mathematical bridge attempt. Exact only under the linearized / affine sub-scope stated below.
**Date.** 2026-04-25.

**Pressure Point.** In `#result-coupled-diagnostic-framework`, Class 2 diagnostic error is bounded by $2L_A\lVert\Delta M_{\text{bias}}\rVert$, where $L_A$ is the Lipschitz constant of the attainability function

$$A_O(M_t;\Pi,N_h)=\sup_{\pi\in\Pi}V_O(M_t,\pi;N_h).$$

The framework correctly leaves $L_A$ domain-dependent. TST supplies a natural domain where $L_A$ should not be treated as a static scalar: software tasks whose attainability depends on a feature-local chain of coupled components, assumptions, interfaces, checks, and reasoning steps.

This spike tries to strengthen the bridge mathematically. The strongest result here is not a global theorem about all software tasks. It is an exact theorem in a local linearized sub-scope, plus a candidate route for estimating or bounding $L_A$ in logogenic software work.

## 1. Feature-Local Linearized Sub-Scope

Fix a feature, repair, or refactor $F$. Let $E_F$ be the finite-dimensional subspace of the agent's model state $M_t$ containing the task-relevant variables: components, invariants, interfaces, tests, assumptions, and intermediate reasoning states whose perturbation can affect attainability for $F$.

For a candidate policy or strategy $\pi\in\Pi_F$, write the feature-local reasoning / implementation dynamics as

$$z_{k+1}=f_{\pi,k}(z_k), \qquad z_0=P_FM_t,$$

where $P_F$ projects the full model state into the feature-local subspace. The terminal value under $\pi$ is

$$V_\pi(M_t)=\ell_\pi(z_d).$$

Linearizing around the current state gives

$$\Delta z_{k+1}=J_{\pi,k}\Delta z_k+r_{\pi,k}(\Delta z_k),$$

where $J_{\pi,k}=D f_{\pi,k}|_{z_k}$ and $r_{\pi,k}=o(\lVert\Delta z_k\rVert)$. Let

$$B_\pi=D\ell_\pi|_{z_d}.$$

Ignoring the higher-order remainder gives the first-order propagated value error:

$$\Delta V_\pi \approx B_\pi J_{\pi,d-1}\cdots J_{\pi,0}P_F\Delta M_t.$$

The operator $J_{\pi,k}$ is not identical to TST's empirical co-change matrix or to a static import graph. Those can supply estimates or structural priors. $J_{\pi,k}$ is the task-local error-propagation operator induced by the agent's current model, strategy, and environment.

## 2. Bridge Lemma: Supremum Lipschitz Bound

**Lemma 1 (Attainability Lipschitz from policy Lipschitz constants).** Suppose each policy-value map $V_\pi(M)$ is locally Lipschitz on a neighborhood $U$ with constant $L_\pi$, and let

$$A_O(M)=\sup_{\pi\in\Pi_F}V_\pi(M).$$

If $L_\ast=\sup_{\pi\in\Pi_F}L_\pi<\infty$, then $A_O$ is locally Lipschitz on $U$ with constant at most $L_\ast$.

**Proof sketch.** For any $M,M'\in U$,

$$A_O(M)-A_O(M')=\sup_\pi V_\pi(M)-\sup_\pi V_\pi(M')\leq \sup_\pi\left(V_\pi(M)-V_\pi(M')\right)\leq L_\ast\lVert M-M'\rVert.$$

Swap $M,M'$ for the reverse inequality. Thus $\lvert A_O(M)-A_O(M')\rvert\leq L_\ast\lVert M-M'\rVert$.

**Corollary 1 (Feature-local transient-gain bound).** Under the linearized sub-scope,

$$L_A(F,M_t)\leq \sup_{\pi\in\Pi_F}\left\lVert B_\pi J_{\pi,d-1}\cdots J_{\pi,0}P_F\right\rVert + O(\varepsilon_F),$$

where $\varepsilon_F$ is the local radius over which the neglected nonlinear remainders matter. In the affine sub-scope ($r_{\pi,k}=0$ and $\ell_\pi$ affine), this bound is exact:

$$L_A(F,M_t)\leq \sup_{\pi\in\Pi_F}\left\lVert B_\pi J_{\pi,d-1}\cdots J_{\pi,0}P_F\right\rVert.$$

If a single policy $\pi^\ast$ is uniquely active in a neighborhood of $M_t$, then locally

$$D_MA_O = B_{\pi^\ast}J_{\pi^\ast,d-1}\cdots J_{\pi^\ast,0}P_F,$$

so the local Lipschitz constant in that smooth region is the operator norm of this product.

**Interpretation.** This is the clean bridge. The logogenic constant $L_A$ is controlled, in this sub-scope, by terminal value sensitivity $B_\pi$, feature projection $P_F$, and finite-horizon propagation gain through the task-local operators $J_{\pi,k}$.

## 3. Non-Normal Transient Amplification

Assume the feature-local propagation structure is acyclic after strategy unrolling or after condensing strongly connected components. The induced block operator can be topologically ordered:

$$
N_\pi=
\begin{bmatrix}
0 & 0 & 0 & \cdots & 0\\
J_{\pi,0} & 0 & 0 & \cdots & 0\\
0 & J_{\pi,1} & 0 & \cdots & 0\\
\vdots & & \ddots & \ddots & \vdots\\
0 & \cdots & 0 & J_{\pi,d-1} & 0
\end{bmatrix}.
$$

In the pure DAG case, $N_\pi$ is nilpotent, so every eigenvalue is zero. Eigenvalue analysis therefore says nothing useful about finite-horizon error amplification. The relevant quantity is the singular-value gain:

$$\left\lVert J_{\pi,d-1}\cdots J_{\pi,0}\right\rVert.$$

**Proposition 1 (Branching transient-growth example).** Consider a depth-$d$ layered dependency tree with effective branching factor $B$ and uniform edge gain $g$. A scalar root error is copied to every descendant with multiplicative gain $g$ per layer. The root-to-leaf propagation operator $G_d:\mathbb R\to\mathbb R^{B^d}$ satisfies

$$\lVert G_d\rVert = |g|^d\sqrt{B^d}=(|g|\sqrt B)^d.$$

The corresponding block-DAG operator is nilpotent, but its finite-horizon root-to-depth-$d$ gain grows exponentially whenever $|g|\sqrt B>1$.

**Proof.** $G_dx$ is a vector of length $B^d$ whose every coordinate equals $g^dx$. Therefore

$$\lVert G_dx\rVert_2=\sqrt{B^d}|g|^d|x|,$$

and the operator norm is $(|g|\sqrt B)^d$.

**Caveat.** This is a growth construction, not a universal lower bound. If terminal value averages leaves with normalization, if aggregation contracts, or if modular boundaries prevent copied errors from aligning, the effective $B_\pi G_d$ can be much smaller. The amplified directions matter only when they align with terminal value sensitivity $B_\pi$ and with the actual bias direction $\Delta M_{\text{bias}}$.

**Risk statement.** Deep tasks are not hard merely because they touch many files. They become fragile when the feature-local operator has high finite-horizon gain along directions that both (a) the agent is likely to misrepresent and (b) terminal attainability is sensitive to.

## 4. Checkpoint-Contraction Theorem

Tool use changes the operator product. A compiler, typechecker, test runner, linter, runtime probe, or targeted inspection introduces an observation/correction map

$$P_k:E_F\to E_F.$$

The leading-order checkpointed dynamics are

$$\Delta z_{k+1}=P_kJ_{\pi,k}\Delta z_k+\epsilon_k,$$

where $\epsilon_k$ is fresh error injected by the checkpoint result or by the agent's interpretation of it.

**Lemma 2 (Checkpoint product bound).** Partition the task into blocks with unchecked propagation operators

$$G_b=J_{t_b-1}\cdots J_{t_{b-1}}.$$

If each checkpointed block satisfies

$$\lVert P_bG_b\rVert\leq q_b,$$

then the homogeneous error after $m$ blocks satisfies

$$\lVert\Delta z_{t_m}\rVert\leq\left(\prod_{b=1}^m q_b\right)\lVert\Delta z_0\rVert.$$

With fresh checkpoint interpretation errors bounded by $\lVert\epsilon_b\rVert\leq \bar\epsilon$, and uniform $q_b\leq q<1$,

$$\lVert\Delta z_{t_m}\rVert\leq q^m\lVert\Delta z_0\rVert+\frac{1-q^m}{1-q}\bar\epsilon.$$

**Proof.** The homogeneous result is submultiplicativity. The inhomogeneous result is the standard linear recurrence bound

$$e_{b+1}\leq qe_b+\bar\epsilon.$$

**Consequence.** Tools are not automatically helpful. They help when they contract the error directions that the preceding block amplifies, and when the new error introduced by reading the tool output is small enough.

## 5. Singular-Subspace Coverage

Let an unchecked block have singular value decomposition

$$G=U\Sigma V^\top.$$

The dangerous output directions are the left singular vectors associated with large singular values. An idealized checkpoint that contracts the top-$r$ amplified output subspace by factor $\eta<1$ has the form

$$P_{\eta,r}=\eta U_rU_r^\top + (I-U_rU_r^\top).$$

Then

$$\lVert P_{\eta,r}G\rVert=\max(\eta\sigma_1,\sigma_{r+1}).$$

This gives a precise coverage condition: a checkpoint bounds the block only if it observes and corrects the singular directions that dominate the unchecked gain. A test suite that misses the high-gain failure mode may have little effect on the relevant $L_A$ bound even if it is useful elsewhere.

**Corollary 2 (Checkpoint-frequency threshold for the branching model).** In Proposition 1, let $\Gamma=|g|\sqrt B>1$. Suppose a checkpoint is inserted every $h$ layers and contracts the amplified subspace by factor $\eta$. Each block has gain at most

$$q=\eta\Gamma^h.$$

Uniform contraction requires

$$\eta\Gamma^h<1,$$

or equivalently

$$h<\frac{\log(1/\eta)}{\log\Gamma}.$$

This is a concrete mathematical version of the engineering intuition: the more entangled the task and the weaker the checkpoint, the more frequently the agent must observe/correct to keep diagnostic error bounded.

## 6. Relation to TST Quantities

TST's `#def-system-coupling` gives an empirical asymmetric quantity

$$P(\text{change}(m_j)\mid\text{change}(m_i)).$$

That is not identical to $J_{\pi,k}$, but it is a plausible estimator or structural prior for entries in a task-local propagation operator. Static dependency graphs, import graphs, type dependencies, test coverage, and the agent's explicit strategy DAG supply additional priors. A future derived segment would need to specify a construction such as:

$$\widehat J_F = W_{\text{static}}S_F + W_{\text{cochange}}C_F + W_{\text{strategy}}\Sigma_F + W_{\text{semantic}}R_F,$$

with weights justified by the observation regime. This spike does not derive that estimator; it identifies the operator that such an estimator would need to approximate.

**Natural metric: the Fisher metric.** The operator norms $\lVert B_\pi J_{\pi,d-1}\cdots J_{\pi,0}P_F\rVert$ above are stated metric-free; the bound's tightness depends on the chosen norm. The natural choice is already AAD-internal: the Fisher metric on the agent's model state is forced by the (PI) parameterization-invariance axiom in `#scope-agent-identity` together with Čencov 1982 uniqueness — derived in `#deriv-fisher-whitened-update-rule` and recorded as the 4th primary instance of `#disc-additive-coordinate-forcing`. Norming the $J_{\pi,k}$ products in the Fisher metric makes $L_A$ reparameterization-invariant by construction; a Lipschitz constant computed in arbitrary task-specific Euclidean coordinates can be made loose or misleading by reparameterization, but the Fisher-metric form cannot. Future promotion should specify Fisher-metric operator norms unless the sub-scope explicitly admits Euclidean coordinates (e.g., when $P_F$ already lifts to an information-geometric basis).

**Companion in survival-imperative form.** The matrix-form machinery here parallels the Linear Matrix Inequality on the Fisher Information Matrix in `#deriv-causal-ib-lmi`. There, the agent's directional-FIM constraint $\mathbb E_\pi[\mathcal I_o(a)] \succeq \mathcal I_{\min}$ forces the action policy to span the drifting eigenspace of the environmental disturbance; here, the agent's strategy DAG induces a finite-horizon propagation operator whose singular structure determines feature-local error amplification. Both are Fisher-geometric matrix bounds on multivariate dynamics: the LMI side governs *observation-channel adequacy* against environmental drift, the transient-amplification side governs *reasoning-chain stability* against representation-error propagation. A unified treatment is plausible but not attempted here. Together with `#result-contraction-template`'s matrix-form sector machinery, AAD now has three matrix-form bound families on multivariate dynamics — Section III contraction, Section II survival-LMI, and the candidate Section II/TST transient-amplification bound this spike sketches.

## 7. Implications

**For TST.** `#hyp-exponential-cognitive-load` should be refined from discontinuity-count scaling to dependency-operator scaling. Ten independent file edits can remain close to additive. A depth-ten chain of mutually constraining edits can exhibit high transient gain.

**For logogenic agents.** $L_A$ is plausibly feature-local and checkpoint-sensitive. A large context window is not automatically harmful. It becomes harmful when it increases the entangled effective subspace without adding localization, decomposition, or corrective observations.

**For tool use.** Tool calls are not merely implementation conveniences. In coupled tasks they can serve as contraction operators that prevent representation error from propagating unchecked through the strategy. The useful condition is not "run tools"; it is "run tools that cover the currently amplified error subspace."

## 8. Epistemic Status

Exact within the affine feature-local sub-scope:
- Lemma 1: the supremum of uniformly Lipschitz policy values is Lipschitz.
- Corollary 1: the local linearized bound by $\lVert B_\pi J_{\pi,d-1}\cdots J_{\pi,0}P_F\rVert$.
- Proposition 1: the branching transient-growth construction.
- Lemma 2: checkpoint product and recurrence bounds.
- Singular-subspace coverage formula for the idealized checkpoint $P_{\eta,r}$.

Still open:
- A canonical construction of $E_F$ and $J_{\pi,k}$ from TST quantities.
- Nonlinear remainder bounds large enough for real logogenic tasks.
- Treatment of cyclic dependencies beyond SCC condensation or local unrolling.
- Empirical estimates of feature-local transient gain in real codebases.
- Whether actual LLM/tool loops implement anything close to the idealized $P_k$ operators.
- Lower bounds showing unavoidable failure for a class of tasks rather than only worst-case vulnerability.

Promotion route: formalize a narrow software sub-scope, define $\widehat J_F$, prove a local theorem with remainder terms, state a checkpoint coverage condition in observable quantities, and validate that the resulting gain predicts observed degradation or recovery in logogenic software tasks.

## 9. Recommended Moves

- Keep the concept as a Working Note in `03-llm-core/src/result-coupled-diagnostic-framework.md`.
- Do not replace `#hyp-exponential-cognitive-load` yet; use this spike to refine its Working Notes toward dependency-structure sensitivity.
- Treat a future `02-tst-core/src/der-transient-dependency-amplification.md` as blocked on a formal construction of $J_F$ and a proved checkpoint-coverage condition.

*(End of spike.)*
