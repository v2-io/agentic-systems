# TF-05: The Mismatch Signal (Derived)

The discrepancy between model prediction and actual observation — the **mismatch signal** — is the fundamental driver of model adaptation. In the adaptive loop's vocabulary (TF-00): *prolepsis* (the model's anticipation) meets *aisthesis* (the world's response), and their difference is *aporia* — the moment of recognizing that reality differs from expectation.

## Definition

Given model $M_{t-1}$ and prior action $a_{t-1}$, the model generates a **prediction** of the next observation:

*[Definition]*
$$\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$$

or, more generally, a predictive distribution $P(o_t \mid M_{t-1}, a_{t-1})$.

The **mismatch signal** (prediction error):

*[Definition (mismatch-signal)]*
$$\delta_t = o_t - \hat{o}_t$$

This is the primary mismatch definition, used in the mismatch dynamics (TF-11, Appendix A) and in the decomposition of Proposition 5.1 below.

In the distributional case, the mismatch generalizes to the **score-function mismatch**:

*[Definition (score-mismatch)]*
$$\tilde{\delta}_t = -\nabla_M \log P(o_t \mid M_{t-1}, a_{t-1})$$

which points in the direction of steepest increase in the likelihood of the actual observation under the model — i.e., the direction the model should move. $\tilde{\delta}_t$ lives in the tangent space $T_M\mathcal{M}$, while $\delta_t$ lives in observation space $\mathcal{O}$.

**When each applies.** The prediction error $\delta_t$ is the natural object when $\mathcal{O}$ is a vector space (the typical case for control, tracking, and regression). The score-function mismatch $\tilde{\delta}_t$ is appropriate when the model space $\mathcal{M}$ is a differentiable manifold — for instance when $\mathcal{M}$ is a parameter space for a probabilistic model. It is particularly useful when the observation space $\mathcal{O}$ is not a vector space (e.g., categorical outcomes) or when the model's predictive distribution is the natural object. For discrete or combinatorial model spaces (antibody repertoires, organizational procedures), neither applies directly; the mismatch must be quantified through an appropriate divergence measure (e.g., KL divergence between predicted and observed distributions). The two coincide up to scaling under Gaussian models. When TF-06's update rule writes $M_t = M_{t-1} + \eta \cdot g(\delta_t)$, the transform $g$ maps from $\delta_t$'s space to the model's update space: $g: \mathcal{O} \to T_M\mathcal{M}$ for prediction errors; $g: T_M\mathcal{M} \to T_M\mathcal{M}$ for score-function mismatches (where $g$ may be the inverse Fisher information for natural gradient, or the identity for vanilla gradient descent).

**Note on units and interpretation.** The prediction error $\delta_t = o_t - \hat o_t$ lives in observation space $\mathcal{O}$, while the score-function mismatch $\tilde{\delta}_t = -\nabla_M \log P$ lives in the tangent space $T_M\mathcal{M}$. For the mismatch dynamics in TF-11 (which use $\Vert\delta\Vert$ as a scalar magnitude), we adopt the information-theoretic interpretation: $\Vert\delta\Vert$ measures the magnitude of the agent's "surprise" — formally, the deviation of the observation from the model's prediction as measured by the negative log-likelihood or an equivalent information-theoretic divergence. Under Gaussian models, the squared prediction error $\Vert\delta_t\Vert^2$ is proportional to the negative log-likelihood, so $\delta_t$ and $\tilde{\delta}_t$ are monotonically related and the dynamics are equivalent up to scaling. For non-Gaussian models, $\tilde{\delta}_t$ is the natural generalization. The key requirement is that $\Vert\delta\Vert$, $\mathcal{T}$, and $\rho$ in TF-11's ODE share consistent units; TF-00's dimensional analysis verifies this using "surprise" ($-\log P$) as the unit of mismatch.

**Bridge from physical to surprise units.** When $\delta_t = o_t - \hat o_t$ is in physical units (meters, dollars, etc.), the $\Vert\delta\Vert$ that enters the mismatch dynamics (TF-11, Appendix A) should be understood as the **Mahalanobis distance**: $\Vert\delta_t\Vert_{\Sigma} = \sqrt{\delta_t^T \Sigma^{-1} \delta_t}$ where $\Sigma$ is the observation noise covariance. This normalization maps physical prediction error to dimensionless surprise-equivalent units (under Gaussian models, $\Vert\delta_t\Vert_{\Sigma}^2$ is exactly the NLL contribution up to a constant). The mismatch decomposition, dynamics, and all downstream results operate on this normalized quantity. When implementing TFT for a specific system, choosing a consistent mismatch normalization is the first operationalization step (see Appendix B, step 1).

## Proposition 5.1: Mismatch Inevitability

**Statement.** For any agent-environment pair in $\mathcal S_{\text{TFT}}$ (TF-01), the expected squared mismatch is strictly positive whenever at least one of the following holds:

1. Observation noise is non-degenerate: $\mathrm{Var}(o_t \mid \Omega_t, a_{t-1}) \gt 0$ on a set of positive probability.
2. One-step predictive mean misspecification is non-zero: $\hat o_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}] \neq \bar o_t = \mathbb{E}[o_t \mid \Omega_t, a_{t-1}]$ on a set of positive probability.

Under either condition:

*[Derived]*
$$\mathbb{E}[\Vert\delta_t\Vert^2] \gt 0$$

**Assumptions.** At least one of the two conditions in the statement holds. A practical bridge from the sufficiency measure (TF-10) is:

- $S(M_t) \lt 1$ implies predictive information is lost relative to the full history.
- To conclude positive one-step squared-error mismatch from this alone requires an additional alignment assumption: the lost predictive information affects the one-step conditional mean under the chosen action conditioning.

Without that alignment assumption, insufficiency still implies positive regret under suitable proper scoring rules, but not necessarily positive one-step mean error.

**Illustrative example.** Consider an environment where $o_t \in \{-1, +1\}$ with equal probability, independently drawn each step. The full history $\mathcal C_t$ carries no predictive information (memoryless environment), so $S(M_t) = 1$ trivially — any model is sufficient. Now suppose $o_t$ is instead determined by a hidden binary state $z \in \{A, B\}$ that flips rarely: under $z = A$, $o_t$ is drawn from $\{-1, +1\}$ with probabilities $(0.9, 0.1)$; under $z = B$, with $(0.1, 0.9)$. A model that tracks only the *mean* of $o_t$ and ignores which regime is active — predicting $\hat o_t = 0$ always — has $S \lt 1$ (it fails to capture the predictive structure in the history). Yet its one-step conditional mean prediction *can* coincidentally match $\bar o_t = \mathbb{E}[o_t \mid \Omega_t, a_{t-1}]$ during regime transitions, or more generally, the lost information may affect higher moments or longer-horizon predictions without affecting the one-step mean. This is why condition (2) in the proposition statement explicitly requires $\hat o_t \neq \bar o_t$, not merely $S \lt 1$.

**Proof sketch.**

1. By TF-01, $H(\Omega_t \mid \mathcal C_t) \gt 0$ — the environment retains residual uncertainty even given the full interaction history.
2. By TF-03, the model generates predictions $\hat o_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$.
3. Decompose the mismatch into model error and noise. Let $\bar o_t = \mathbb{E}[o_t \mid \Omega_t, a_{t-1}]$ be the true conditional mean (conditioning on both the environment state and the action, since the observation function $h$ may depend on $a_{t-1}$ per TF-01). Then:

*[Derived (Proof Step)]*
$$\mathbb{E}[\Vert\delta_t\Vert^2] = \mathbb{E}[\Verto_t - \hat{o}_t\Vert^2] = \underbrace{\mathbb{E}[\Vert\hat{o}_t - \bar{o}_t\Vert^2]}_{\text{(i) model prediction error}} + \underbrace{\mathbb{E}[\text{Var}(o_t \mid \Omega_t, a_{t-1})]}_{\text{(ii) observation noise}}$$

   (This uses an implicit assumption from TF-01's observation model: the observation noise $\varepsilon_t$ at time $t$ is conditionally independent of the agent's prior history $\mathcal C_{t-1}$ given the environment state $\Omega_t$ and the action $a_{t-1}$. This is the standard "fresh noise" assumption in state-space models — the noise is a property of the observation channel at the moment of observation, not of the agent's past. Given this, the cross-term vanishes by the tower property: condition on $(\Omega_t, a_{t-1})$, under which $\bar o_t = \mathbb{E}[o_t \mid \Omega_t, a_{t-1}]$ is a constant and $\hat o_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$ is determined by $(\mathcal C_{t-1}, a_{t-1})$, so $\bar o_t - \hat o_t$ is fixed. The remaining factor $\mathbb{E}[o_t - \bar o_t \mid \Omega_t, a_{t-1}] = 0$ by definition of $\bar o_t$, giving $\mathbb{E}[(o_t - \bar o_t)(\bar o_t - \hat o_t) \mid \Omega_t, a_{t-1}] = 0$. Taking outer expectations yields the result. This is orthogonality, not independence — the two terms are uncorrelated but need not be independent. Note that term (ii) now depends on $a_{t-1}$: when the action affects the observation mechanism, different actions yield different noise levels — exactly the sensor-selection scenario in Appendices B-C.)

4. **Term (ii):** Under condition (1), $\mathbb{E}[\text{Var}(o_t \mid \Omega_t, a_{t-1})] \gt 0$, which alone gives $\mathbb{E}[\Vert\delta_t\Vert^2] \gt 0$.
5. **Term (i):** Under condition (2), $\hat o_t \neq \bar o_t$ on a set of positive probability, so $\mathbb{E}[\Vert\hat o_t - \bar o_t\Vert^2] \gt 0$.
6. Either source of positivity suffices; both hold simultaneously in typical settings. $\square$

**Corollary.** Mismatch signals are structurally persistent in realistic TFT regimes. They can be reduced (by improving predictive adequacy, shrinking term (i)) but not eliminated when observation noise is non-degenerate (term (ii)). In deterministic, noiseless, perfectly specified special cases, the mismatch can vanish; TFT treats these as limiting edge cases rather than the typical adaptive regime.

## Why This Is Derived, Not Axiomatic

The proposition above makes precise what was previously stated informally: the mismatch signal follows from TF-03 (the model generates predictions from compressed history) and TF-01 (observations arrive from an uncertain environment). Given any model that predicts and any observation that arrives, their difference exists. The mismatch signal is not an additional assumption but a *consequence* of having a predictive model in an uncertain world.

## Properties

**Vanishing mismatch**: If the model perfectly predicts observations, $\delta_t = 0$ for all $t$. The model needs no updating (but see the ambiguity warning below).

**Decomposition**: The expected squared mismatch decomposes as (from the proof of Proposition 5.1):

*[Derived (mismatch-decomposition)]*
$$\mathbb{E}[\Vert\delta_t\Vert^2] = \underbrace{\mathbb{E}[\Vert\hat{o}_t - \bar{o}_t\Vert^2]}_{\text{model error (reducible)}} + \underbrace{\mathbb{E}[\text{Var}(o_t \mid \Omega_t, a_{t-1})]}_{\text{observation noise (irreducible)}}$$

where $\bar o_t = \mathbb{E}[o_t \mid \Omega_t, a_{t-1}]$. The model can only drive the first term toward zero. The second term — **aleatoric uncertainty** — is a property of the observation channel (and possibly the action), not the model. An agent that tries to eliminate all mismatch (including irreducible noise) will **overfit**: adjusting its model to explain noise, degrading future predictions.

**Information content**: The mismatch signal carries information about the gap between model and reality:

*[Discussion — Informational Interpretation]*
$$I(\delta_t; \Omega_t \mid M_{t-1}) \gt 0 \quad \text{when the model is imperfect}$$

An agent that ignores mismatch signals loses information. An agent that overreacts to them treats noise as signal. The optimal response — the update gain — is the subject of TF-06.

## The Zero-Mismatch Ambiguity

$\delta_t \approx 0$ does **not** necessarily indicate model adequacy. It indicates that predictions match observations, which may occur because:

**(a) Accurate model.** The model genuinely reflects reality. (*Desirable.*)

**(b) Insufficient exploration.** The agent is only observing aspects of the environment that its model already explains, while remaining ignorant of aspects where the model is wrong. (*Dangerous — confirmation bias.*)

**(c) Low channel resolution.** The observation channel is too noisy or low-bandwidth to detect model errors. (*Architectural limitation.*)

Only (a) is desirable. Cases (b) and (c) represent situations where the mismatch signal is **uninformative** — not because the model is good, but because the agent isn't generating observations that would *test* the model.

This ambiguity is why **active testing** — choosing actions specifically to generate informative mismatch signals — can be valuable for agents that have the capacity to vary their actions (TF-07 or TF-08). An agent that only exploits its model (acting to maximize predicted reward) will tend toward case (b). An agent that explores (acting to maximize expected information from $\delta$) will discover model errors faster. When reliable external models are accessible (other agents, reference sources), **query actions** (TF-07 or TF-08) can resolve this ambiguity far more efficiently than direct probing — the external model's response effectively tests the agent's model against a different, potentially superior compression of the same environment.

## Domain Instantiations

| Domain | Mismatch signal $\delta_t$ |
|--------|---------------------------|
| Kalman filter[^kalman1960] | Innovation: $\tilde y_t = y_t - H\hat x_{t \mid t-1}$ |
| RL (TD learning) | TD error: $r_t + \gamma \max_{a'} Q(s', a') - Q(s_t, a_t)$ |
| Bayesian inference | Surprise: $-\log P(D_t \mid \theta_{\text{MAP}})$ |
| PID control | Error: $e_t = r_t - y_t$ (setpoint − measurement) |
| Active inference | Free energy gradient: $\nabla_\mu F$ |
| Scientific method | Experimental anomaly: observation contradicting theory |
| Boyd's OODA | Disorientation: outcomes contradicting mental model |
| Immune system | Unrecognized antigen: pathogen not matching antibody repertoire |

---

[^kalman1960]: Kalman, R. E. (1960). "A new approach to linear filtering and prediction problems." *J. Basic Engineering (ASME)*, 82(1), 35–45.
[^rao1999]: Rao, R. P. N. & Ballard, D. H. (1999). "Predictive coding in the visual cortex." *Nature Neuroscience*, 2(1), 79–87.
[^geman1992]: Geman, S., Bienenstock, E., & Doursat, R. (1992). "Neural networks and the bias/variance dilemma." *Neural Computation*, 4(1), 1–58.
