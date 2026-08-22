# TF-10: Structural Adaptation (Derived + Empirical)

Incremental model updating (TF-06) adjusts parameters within a fixed model class $\mathcal{M}$. When the model class itself is inadequate — when no model in $\mathcal{M}$ can serve as a good sufficient statistic for the environment — the agent requires **structural adaptation**: changing $\mathcal{M}$.

**Epistemic status**: The *necessity* of structural adaptation is *derived* from model class fitness (defined below) and TF-06 (parametric updating is insufficient when $\mathcal{F}(\mathcal{M})$ is low). The six-phase destruction-creation cycle is an *empirical pattern* observed across domains (Boyd, Kuhn, evolution, ML) — plausible and well-supported but not formally derived. The cost analysis is *discussion*.

## Model Sufficiency and Model Class Fitness

To formalize when structural adaptation is necessary, we first need measures of how well a model — and a model class — serve their predictive purpose. These definitions apply the sufficient statistic concept (Fisher, 1922[^fisher1922]) to the model formulation (TF-03).

**Model sufficiency** measures the degree to which the model captures everything predictively relevant in the interaction history:

*[Definition (sufficiency)]*
$$S(M_t) = 1 - \frac{I(\mathcal{C}_t \,;\, o_{t+1:\infty} \mid M_t, a_{t:\infty})}{I(\mathcal{C}_t \,;\, o_{t+1:\infty} \mid a_{t:\infty})}$$

When $S = 1$: the model captures everything in the history that is predictively relevant. Knowing $\mathcal C_t$ in addition to $M_t$ provides no further predictive power.

When $S = 0$: the model captures nothing predictively relevant.

Perfect sufficiency ($S = 1$) is an ideal. Real models are approximately sufficient, and the degree of sufficiency is itself a measure of model quality.

**Convention when denominator vanishes.** If the environment is memoryless (pure noise), the history carries no predictive information: $I(\mathcal C_t; o_{t+1:\infty} \mid a_{t:\infty}) = 0$, making the denominator zero. In this case, define $S(M_t) \equiv 1$: any model — including an empty one — is trivially sufficient because there is nothing predictively relevant to compress.

**Policy-conditioned sufficiency (operational form).** The definition above conditions on the full future action sequence $a_{t:\infty}$, making $S$ a property of the model's *representational capacity* independent of the agent's policy. This is the theoretical ideal but is non-operational: it cannot be computed or estimated from finite data. For all practical purposes — empirical estimation, optimization targets, falsifiable predictions — use the **policy-conditioned** form:

*[Definition (Operational Form)]*
$$S_\Pi(M_t) = 1 - \frac{I(\mathcal{C}_t \,;\, o_{t+1:t+N_h} \mid M_t, \pi \in \Pi)}{I(\mathcal{C}_t \,;\, o_{t+1:t+N_h} \mid \pi \in \Pi)}$$

where $N_h$ is a finite prediction horizon and $\Pi$ is the policy class under consideration. This is the measured object in any empirical application of TFT. It answers a more specific question: "is $M_t$ a sufficient statistic for prediction *under policies the agent might actually use* over a *finite horizon*?" A model may have $S_\Pi \approx 1$ for one policy class but $S_{\Pi'} \lt 1$ for another — a chess engine's model is sufficient for its own search policy but not for an alien evaluation function.

The full-sequence $S(M_t)$ remains the theoretical upper bound: $S(M_t) \geq S_\Pi(M_t)$ for any $\Pi$ and any $N_h$. Throughout TFT, results that depend on sufficiency (TF-05's mismatch inevitability bridge, Proposition 10.1 below) hold for both forms — they require only that the model falls short of perfect sufficiency, which the operational form can detect.

**Model class fitness** measures the best achievable sufficiency given the model class:

*[Definition (model-class-fitness)]*
$$\mathcal{F}(\mathcal{M}) = \sup_{M \in \mathcal{M}} S(M)$$

**Note on implicit environment dependence.** The notation $\mathcal{F}(\mathcal{M})$ is a deliberate simplification. Since $S(M)$ depends on the joint distribution of histories and future observations — which is determined by the environment dynamics $(T, h)$ — model class fitness is properly a joint property: $\mathcal{F}(\mathcal{M}; T, h)$. We suppress this dependence for readability, but the implicit conditioning matters: when the environment changes, $\mathcal{F}(\mathcal{M})$ changes even though $\mathcal{M}$ does not. This is precisely what triggers structural adaptation — not that the model class has deteriorated in any absolute sense, but that the environment has moved to a regime where $\mathcal{F}(\mathcal{M}; T', h')$ is lower than it was under the prior dynamics.

## Levels of Adaptation

Adaptation operates across a spectrum of timescales and depths. Two commonly distinguished levels are:

**Parametric adaptation** (TF-06): $M_t$ changes within fixed $\mathcal{M}$.
*[Definition]*
$$M_t = f(M_{t-1}, o_t, a_{t-1}) \quad M_t \in \mathcal{M}$$

**Structural adaptation** (this document): $\mathcal{M}$ itself changes.
*[Definition]*
$$\mathcal{M}_{t+1} = \Phi(\mathcal{M}_t, \text{performance history})$$

These are the two ends of a *continuum*, not an exhaustive binary. Real adaptive systems often operate at multiple intermediate levels simultaneously — an RL agent may be updating value function weights (parametric), adjusting its reward shaping (meta-parametric), changing its exploration schedule (policy-structural), and occasionally switching architectures (fully structural). TF-11's temporal nesting principle generalizes this: the convergence constraint $\nu_{n+1} \ll \nu_n$ applies between any adjacent timescales, however many there are.

For formal analysis, we focus on the parametric/structural distinction because it captures the most important qualitative transition — the point at which incremental adjustment within the current representational framework is insufficient and the framework itself must change. But this should be understood as one particularly important boundary within a richer hierarchy, not as the only one.

## Proposition 10.1: Structural Adaptation Necessity

**Statement.** If the model class fitness $\mathcal{F}(\mathcal{M}) \lt 1 - \epsilon$ for some $\epsilon \gt 0$, then no amount of parametric adaptation within $\mathcal{M}$ can reduce the expected mismatch below a floor determined by $\epsilon$.

**Assumptions.**
1. The agent has converged parametrically: $M_t$ has reached $M^\ast = \arg\sup_{M \in \mathcal{M}} S(M)$ (or is within the convergent basin).
2. The environment dynamics have a predictable component that exceeds $\mathcal{M}$'s capacity — formally, $I(\mathcal C_t; o_{t+1:\infty} \mid M^\ast, a_{t:\infty}) \gt 0$ (there is predictive information in the history that the best model in $\mathcal{M}$ fails to capture).

**Proof sketch.**

1. By the definitions above, $S(M^\ast) = \mathcal{F}(\mathcal{M}) \lt 1 - \epsilon$.
2. Therefore $I(\mathcal C_t; o_{t+1:\infty} \mid M^\ast, a_{t:\infty}) \gt 0$: the history contains information predictive of future observations that $M^\ast$ does not capture.
3. This uncaptured predictive information manifests as *systematic* mismatch — structured residuals $\delta_t$ that contain signal, not merely noise.
4. From TF-05's decomposition, the model error component $|\hat o_t - \mathbb{E}[o_t \mid \Omega_t]|^2$ has a positive lower bound that cannot be reduced by any $M \in \mathcal{M}$.
5. The update rule (TF-06) adjusts $M_t$ within $\mathcal{M}$, but by assumption the optimal $M^\ast$ is already (approximately) reached. Further updates oscillate without net improvement.
6. Therefore: reducing mismatch below the floor requires changing $\mathcal{M}$ — i.e., structural adaptation. $\square$

**Corollary.** Persistent irreducible mismatch (after parametric convergence) is *diagnostic* of model class inadequacy. An agent that detects systematic patterns in its residuals has evidence that $\mathcal{F}(\mathcal{M})$ is insufficient.

## Symptoms of Model Class Inadequacy

When $\mathcal{F}(\mathcal{M})$ is low, no model in $\mathcal{M}$ can adequately compress the interaction history. Observable symptoms:

1. **Persistent irreducible mismatch**: $\Vert\delta_t\Vert$ remains large despite extended updating — the model has converged within $\mathcal{M}$ but the best achievable model is still poor.

2. **Gain collapse without performance**: $\eta^\ast$ has decreased (model appears confident) but predictions remain inaccurate — the model is confidently wrong, having fitted to structure in $\mathcal{M}$ that doesn't match reality.

3. **Systematic mismatch patterns**: $\delta_t$ shows structure (correlations, trends, periodicities) that the model class cannot represent — the residuals contain signal that $\mathcal{M}$ lacks the capacity to absorb.

## Destruction and Creation

Structural adaptation often involves **decomposing** existing model structure and **recombining** elements into a new configuration. Boyd's insight — his thought experiment of decomposing skis, outboard motors, bicycle handlebars, and tank treads from their native domains in order to recombine them as a snowmobile for entirely new conditions — captures why decomposition can be essential: components locked into an existing structural relationship may need to be freed before they become available for recombination into a structure with better fitness for a changed environment.

This decompose-and-recombine pattern is one important *mechanism* of structural adaptation:

- **Boyd**: "Destruction and creation" — tearing apart existing mental models and synthesizing new ones from the pieces
- **Kuhn**: Paradigm shift — abandoning the current paradigm when anomalies accumulate beyond what normal science can resolve
- **Popper**: Conjecture and refutation — the bold conjecture of a new theory replacing a falsified one

But it is not the only mechanism. Structural adaptation can also proceed by:

- **Expansion**: Adding new representational capacity to the existing structure without destroying it (Bayesian nonparametrics, growing neural architectures, organizational expansion into new divisions)
- **Compression**: Removing unnecessary structure while preserving the predictive core (regularization, Occam's razor, organizational streamlining — see Structural Overfitting below)
- **Grafting**: Incorporating external structure (transfer learning, acquiring a company, horizontal gene transfer). Query actions (TF-07 and TF-08) are a primary conduit for grafting — consulting an expert, reading a text, or apprenticing under a mentor can transfer representational structures that would be prohibitively expensive to discover through direct probing alone

The severity of structural change needed depends on *how far* the current model class is from adequacy for the new environment. Minor regime changes may require only expansion or grafting; fundamental regime changes — where the environment's causal structure has shifted so thoroughly that the existing model class's assumptions are violated — may demand full decomposition and recombination. Living systems face no guarantee of regime stability (unlike, e.g., the stable dynamics that Kalman filters typically track), which is why biological and organizational systems tend to maintain the *capacity* for deep structural change even when it is rarely exercised.

## A Common Pattern: The Destruction-Creation Cycle

When structural adaptation involves significant decomposition and recombination (as opposed to incremental expansion or compression), it tends to follow a characteristic pattern. Not all structural adaptation follows this pattern — gradual model expansion, for instance, may not involve a discrete "destruction" phase — but it is common enough across domains to warrant description:

**Phase 1 — Anomaly accumulation**: Mismatch signals persist despite parametric adaptation. $\Vert\delta\Vert$ converges to a floor above zero. The agent's performance plateaus.

**Phase 2 — Recognition**: The agent (or meta-process) detects that the residual mismatch is structural, not parametric. This requires a higher-level mismatch signal — mismatch about the mismatch, a *meta-observation* that the model class is failing.

**Phase 3 — Decomposition**: The current model structure is partially or fully abandoned. This can be costly — accumulated knowledge embedded in $M_t$'s parameters may be partially or fully lost, depending on how much transfers to the new structure.

**Phase 4 — Exploration of model classes**: New candidates $\mathcal{M}'$ are considered. This may be random (evolutionary mutation), systematic (architecture search), or insight-driven (scientific creativity). In practice, this exploration rarely happens blind: agents often allocate a small fraction of their tempo to **shadow models** — parallel low-$\nu$ evaluations of candidate model classes against recent data, estimating $\alpha'$ and $\mathcal{F}(\mathcal{M}')$ before committing to the full transition cost $C_{\text{switch}}$. Biological analogs include maintaining genetic diversity (evolution), running pilot programs (organizations), and maintaining background hypotheses (science).

**Phase 5 — Recombination**: A new model class $\mathcal{M}'$ is selected — potentially incorporating elements from the previous structure in new configurations — and a new model $M'_0 \in \mathcal{M}'$ is initialized.

**Phase 6 — Rapid parametric adaptation**: Because $M'_0$ is newly initialized, model uncertainty $U_M$ is high, so $\eta^\ast$ is large (TF-06). The model learns rapidly in the new structure.

## Structural Overfitting: The Opposite Failure Mode

Proposition 10.1 addresses the case where $\mathcal{M}$ is too constrained — the model class cannot represent the environment's structure. The *opposite* failure is equally important: $\mathcal{M}$ is too expressive, and the model memorizes irreducible noise.

### Symptoms of Structural Overfitting

1. **Low training mismatch, high generalization mismatch**: $\Vert\delta_t\Vert \to 0$ on observed data, but predictions on novel observations (new actions, unseen environment states) degrade. The model has fitted the noise in $\mathcal C_t$ rather than the signal.

2. **Model complexity growing without predictive gain**: In the information bottleneck framing (TF-03), the compression cost $I(M_t; \mathcal C_t)$ increases while the predictive power $I(M_t; o_{t+1:\infty} \mid a_{t:\infty})$ plateaus — the model is retaining history detail that carries no predictive value.

3. **Gain collapse to zero on the *wrong* basis**: $\eta^\ast \to 0$ because $U_M \to 0$ (the model is "confident"), but this confidence is spurious — the model is certain about noise-fitted parameters, not about genuine environment structure.

**Connection to TF-03.** The information bottleneck provides the diagnostic:

*[Discussion — Diagnostic Heuristic]*
$$\frac{\partial I(M_t; o_{t+1:\infty} \mid a_{t:\infty})}{\partial I(M_t; \mathcal{C}_t)} \to 0$$

When marginal increases in model complexity (history retention) yield no marginal predictive power, the model is past the optimal point on the rate-distortion curve. Structural adaptation in this case means **compression** — moving to a simpler $\mathcal{M}'$ that retains the predictive core and discards the noise-fitted components.

**Domain instantiations**: Regularization in ML (L1/L2, dropout, early stopping), Bayesian model selection (Occam's razor via marginal likelihood), scientific parsimony (preferring simpler theories that explain the same data), organizational streamlining (removing processes that consume resources without improving outcomes).

Structural adaptation is therefore *bidirectional*: expansion when the model class is too constrained (Proposition 10.1), and compression when it is too expressive. The optimal $\mathcal{M}$ sits on the information bottleneck's Pareto frontier for the agent's actual environment.

## The Cost of Structural Change

Structural adaptation is expensive:
- **Knowledge loss**: Parameters learned within $\mathcal{M}$ may not transfer to $\mathcal{M}'$
- **Temporary performance drop**: The new model starts uncertain; performance degrades before improving
- **Search cost**: Finding good $\mathcal{M}'$ may require exploring many candidates
- **Coordination cost**: In multi-agent or organizational systems, structural change requires collective reorientation

This cost creates a rational **conservatism** — agents should prefer parametric adaptation when it suffices, and resort to structural adaptation only when the evidence for model class inadequacy is strong. Premature structural change wastes accumulated knowledge. Delayed structural change accumulates mismatch.

**Connection to the deliberation cost (TF-09).** Structural adaptation can be understood as deliberation with a *massive* $\Delta\tau$. During the decomposition-and-recombination process, the agent's high-frequency parametric loop is partially or fully suspended — effective $\nu$ drops toward zero — while the agent searches for a new model class. By TF-09's threshold (Proposition 9.1), this suspension accumulates mismatch at rate $\rho_{\text{delib}} \cdot \Delta\tau$. For structural change, $\Delta\tau$ is typically orders of magnitude larger than for ordinary deliberation (weeks or months for an organizational restructuring vs. seconds for a tactical decision), making the mismatch debt correspondingly enormous. The agent rationally resists structural adaptation until the parametric mismatch floor (Proposition 10.1) — the irreducible error from model class inadequacy — becomes more costly than this massive temporal penalty. This reframes TF-10's conservatism as a *derived consequence* of TF-09's deliberation trade-off applied at a slower timescale, rather than an independent principle.

The optimal threshold for structural adaptation is itself an open problem, analogous to the explore-exploit trade-off (TF-08) but at a higher level.

## Temporal Nesting of Adaptation

Adaptation at different depths operates at different timescales. In the simplest case:

*[Derived (Temporal Nesting Constraint)]*
$$\nu_{\text{parametric}} \gg \nu_{\text{structural}}$$

More generally, an agent may have multiple adaptive processes operating at different rates — with the constraint (TF-11) that faster processes must approximately converge before slower ones act on their output:

*[Derived (Temporal Nesting Constraint)]*
$$\nu_{\text{level } n} \gg \nu_{\text{level } n+1} \quad \text{for each adjacent pair}$$

If a deeper change occurs before shallower adaptation has converged, the deeper change is based on transient behavior rather than settled dynamics. If deeper change is too infrequent, the agent may be trapped in an inadequate structure. The parametric/structural boundary is the most commonly analyzed instance of this general constraint, but the principle applies equally to any pair of adjacent timescales in a multi-level adaptive system.

## Domain Instantiations

The table below illustrates the parametric/structural boundary — the most commonly analyzed timescale boundary — across domains. Most of these domains also have additional intermediate levels not shown here.

| Domain | Parametric adaptation | Structural adaptation | Notes on intermediate levels |
|--------|----------------------|----------------------|------------------------------|
| Kalman filter | State estimate update | Switching observation/dynamics models | Adaptive noise estimation sits between |
| RL | Weight/Q-value update | Architecture search | Reward shaping, exploration schedules, optimizer changes are intermediate |
| PID | — (gains fixed) | Switching to MPC or different control law | Auto-tuning, gain scheduling are intermediate |
| Bayesian | Posterior update within model family | Model selection, Bayesian nonparametrics | Hyperparameter adaptation is intermediate |
| Boyd | Orientation updating | Destruction and creation of mental models | Doctrinal adjustment, organizational learning are intermediate |
| Science | Normal science (Kuhn) | Paradigm shift | Theoretical extension, methodological innovation are intermediate |
| Evolution | Allele frequency change | Speciation, new body plans | Gene regulation changes, epigenetics are intermediate |
| Organization | Process optimization | Strategic pivot, restructuring | Hiring, team reorganization, tool changes are intermediate |
| Immune | Affinity maturation | Novel antibody class generation | Memory cell formation, cytokine profile shifts are intermediate |

---

[^fisher1922]: Fisher, R. A. (1922). "On the mathematical foundations of theoretical statistics." *Phil. Trans. Royal Society A*, 222, 309–368.
