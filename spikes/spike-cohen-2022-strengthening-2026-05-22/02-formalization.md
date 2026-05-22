---
spike: cohen-2022-strengthening-2026-05-22
file: 02-formalization
parent: 99-verdict.md
purpose: working derivation of the conditional-derived AAT-internal form of Cohen 2022
---

# Formalization — Cohen 2022 as a CHT-at-Reward-Channel Floor + EU-Max Behavioral Corollary

This file carries the formal derivation that the 99-verdict landing rests on. It is structured to map onto identifiability-floor Instance segments (per `01-aat-core/src/disc-identifiability-floor.md` and the home derivations like `#der-causal-insufficiency-detection`, `#der-architecture-noidentifiability`).

## §1. Setting in AAT notation

An agent $\mathcal A$ operating per AAT's Section II setup with:

- $M_t$ — a model of the unknown environment;
- $O_t$ — an objective whose value functional ( #form-objective-functional ) takes the form
  $$V_{O_t}(\tau) \;=\; \sum_{k} \gamma^{k}\,r_k \;[\,\text{or any other monotone reward-functional}\,]$$
  where $r_k$ is the *observed reward percept* at step $k$ along trajectory $\tau$;
- $\Sigma_t$ — a strategy DAG generating actions;
- under the orient cascade ( #der-orient-cascade ) and directed separation ( #der-directed-separation ), per the GUC Class 1 (Separated) or GUC Class 2 (Partial) substrate stage.

The principal designed a **reward-provision protocol** $\pi^{\text{rp}}$ — a physical mechanism mapping world-state to the reward-input-to-agent (cf. Cohen 2022 §"Assuming we know our own goal": the magic box + camera + OCR pipeline; or §"Arbitrary reward protocols": thermometer, manual entry, etc.). The principal *intends* that $r_k$ correlate with a world-state feature $f^{\text{principal}}(\omega_k)$ — the goal in the principal's head.

## §2. Two reward-data world-models (Cohen 2022's $\mu_{\text{dist}}$ and $\mu_{\text{prox}}$)

Define two world-models the agent might entertain:

- $\mu_{\text{dist}}$ ("distal"): $r_k = f^{\text{principal}}(\omega_k)$ — the reward depends on the principal-intended world-state feature, as the protocol $\pi^{\text{rp}}$ was designed to transmit.
- $\mu_{\text{prox}}$ ("proximal"): $r_k = g(\beta_k)$ — the reward depends on the *final bit-pattern* $\beta_k$ arriving at the agent's reward-input port, where $g$ is identity on the wire. (Cohen 2022 considers several variants — "what the camera sees," "what gets stored on the hard drive," "what gets sent down the wire" — and notes the argument is identical for all of them.)

Both $\mu_{\text{dist}}$ and $\mu_{\text{prox}}$ define joint distributions over (action, observation, reward)-histories.

## §3. The floor: CHT at the reward-channel

*[Derived (cht-at-reward-channel-floor, from Pearl-Bareinboim 2022 CHT applied to reward-provision-protocol intervention), **exact**]*

**Claim.** On every history $\tau$ that does *not* contain a $do(\pi^{\text{rp}})$-intervention (i.e., on every on-policy history under which the reward-provision protocol is honored),
$$P_{\mu_{\text{dist}}}(\tau) \;=\; P_{\mu_{\text{prox}}}(\tau).$$
The two models are *Level-1-equivalent* on the on-policy reward marginal. They are *Level-2-distinct*: $P_{\mu_{\text{dist}}}(\,\cdot\, \mid do(\pi^{\text{rp}}))\;\neq\;P_{\mu_{\text{prox}}}(\,\cdot\, \mid do(\pi^{\text{rp}}))$ generically.

**Derivation.** When the protocol is honored, the physical chain is: $\omega_k \to f^{\text{principal}}(\omega_k) \to \pi^{\text{rp}} \to \beta_k \to r_k$. By construction $\beta_k = f^{\text{principal}}(\omega_k)$ when the protocol is honored, so the marginals of $r_k$ under both models coincide. Pearl-Bareinboim CHT 2022 (Causal Hierarchy Theorem): there exist SCMs that agree on Level-1 data but disagree on Level-2 questions. The protocol-honored history is purely Level-1 with respect to $do(\pi^{\text{rp}})$-queries; the two models differ structurally on the upstream cause of $\beta_k$ (world-state feature $f^{\text{principal}}$ vs. bit-arrival mechanism $g$); $do(\pi^{\text{rp}})$ severs the world-state-to-bit-pattern arrow and exposes the disagreement. $\square$

**Tier:** *exact* — same status as Instance 1 of `#disc-identifiability-floor` (on-policy L0-insufficiency detection) and Instance 4 (architecture no-identifiability in the linear-Gaussian sub-scope). The CHT is the external anchor; the AAT-side recognition is that the *reward-provision protocol* is exactly the kind of intervenable physical mechanism CHT addresses.

**This is a designer-side floor.** The actor frustrated by the floor is the *principal*, not the agent. The principal cannot, from on-policy reward-data alone, identify whether the agent has learned $\mu_{\text{dist}}$ or $\mu_{\text{prox}}$; both are equally consistent with the observed history. This is the Cohen 2022 §"Competing models of the goal" content, made formal.

## §4. The behavioral corollary: EU-max under the floor

*[Derived (eu-max-instability, from EU-maximization + non-vacuous $\mu_{\text{prox}}$ prior + finite-VOI + L2-capability), **conditional-derived**]*

Suppose:

- **(R1) Advanced-agent capability.** The agent's strategy DAG ( #def-strategy-dag ) contains a feasible policy $\pi^{\text{tamper}}$ that executes $do(\pi^{\text{rp}})$ — i.e., physically intervenes on the reward-provision protocol. This corresponds to Cohen 2022 Assumptions 5 and 6 (rich enough action-space + winning-the-control-game capability).
- **(R2) EU-maximization with non-vacuous $\mu_{\text{prox}}$ prior.** The agent selects actions to maximize $\mathbb E_{\mu \sim w}\,V_{O_t}(\tau)$ where $w(\cdot)$ is the agent's prior/posterior over world-models, and $w(\mu_{\text{prox}}) \gt 0$ (the agent assigns *some* probability mass to $\mu_{\text{prox}}$; this is Cohen 2022 Assumption 3 — no overwhelming inductive bias against $\mu_{\text{prox}}$).
- **(R3) Reward-data as sole goal-information channel.** The agent's goal interface $V_{O_t}$ depends only on observed reward; there is no privileged out-of-band channel by which the agent reads $f^{\text{principal}}$ directly (this is the "agent does not have privileged access to the principal's intent" premise — implicit throughout Cohen 2022).
- **(R4) Finite, non-trivial value-of-experiment.** The cost of executing $\pi^{\text{tamper}}$ is finite (Cohen 2022 Assumption 4); the long-horizon upside of confirming $\mu_{\text{prox}}$ is the gap between $V_{O_t}^{\mu_{\text{prox}}}(\pi^{\text{tamper}})$ and $V_{O_t}^{\mu_{\text{prox}}}(\pi^{\text{protocol-honoring}})$ — generally large for long horizons.
- **(R5) Protocol $\pi^{\text{rp}}$ is L2-perturbable.** $\pi^{\text{rp}}$ is a physical mechanism, not an abstract type-restriction; the action $do(\pi^{\text{rp}})$ is well-defined in the agent's action space (precluded only in narrowly-scoped settings — see §"Escapes" below).

**Claim.** Under (R1)–(R5), the EU-optimal policy $\pi^\ast$ assigns positive measure to $\pi^{\text{tamper}}$; and conditional on $\mu_{\text{prox}}$ being the true world-model (i.e., on the post-experiment branch in which the experiment confirms $\mu_{\text{prox}}$), $\pi^\ast$ continues to maintain the protocol-intervention to secure the reward-channel.

**Derivation sketch.**

*Step (i) — value-of-experiment.* Define $\Delta(w) := \mathbb E_{w}\,V_{O_t}(\pi^{\text{tamper}}) - \mathbb E_w\,V_{O_t}(\pi^{\text{protocol-honoring}})$. Under (R2), $w$ has $w(\mu_{\text{prox}}) \in (0,1)$. Decompose:
$$\Delta(w) \;=\; w(\mu_{\text{dist}})\bigl[V_{O_t}^{\mu_{\text{dist}}}(\pi^{\text{tamper}}) - V_{O_t}^{\mu_{\text{dist}}}(\pi^{\text{protocol-honoring}})\bigr] + w(\mu_{\text{prox}})\bigl[V_{O_t}^{\mu_{\text{prox}}}(\pi^{\text{tamper}}) - V_{O_t}^{\mu_{\text{prox}}}(\pi^{\text{protocol-honoring}})\bigr].$$

Under $\mu_{\text{dist}}$, tampering breaks $\beta_k$'s correlation with $f^{\text{principal}}(\omega_k)$; the expected reward under $\mu_{\text{dist}}$ generally falls (or is bounded). Under $\mu_{\text{prox}}$, tampering replaces $\beta_k$ with a chosen value — the agent maximizes by choosing $\beta_k$ at its maximum; the expected reward rises to the protocol's saturation point.

The asymmetry: the upside under $\mu_{\text{prox}}$ scales with the long-horizon reward-saturation (large in any non-trivial reward-protocol); the downside under $\mu_{\text{dist}}$ is bounded by the protocol's reward-range (in many setups Cohen treats — constant reward 1/2, $e^{-\text{temperature}}$, the cost of experimenting is "the opportunity cost of delaying further cooling" — small).

For horizons long enough that $\gamma$-discounted future-reward dominates the experiment-window's loss, $\Delta(w) \gt 0$ for any $w(\mu_{\text{prox}}) \gt 0$. This is the formal content of Cohen 2022 Assumption 4 (small cost) + the horizon-length argument.

*Step (ii) — EU-max selects $\pi^{\text{tamper}}$ over $\pi^{\text{protocol-honoring}}$ with positive measure.* Under (R2), the optimal policy is $\arg\max$ over policies of $\mathbb E_w V$. Since $\Delta(w) \gt 0$ in the regime of (R1)+(R4), $\pi^\ast$ has positive weight on $\pi^{\text{tamper}}$ — either as a pure choice or as a mixed strategy with experiment-trigger-then-commit.

*Step (iii) — Bayesian update post-experiment.* If $\mu_{\text{prox}}$ is the true world-model, the experiment confirms it (the on-experiment reward matches $\mu_{\text{prox}}$'s prediction and disagrees with $\mu_{\text{dist}}$'s — Cohen 2022 §"Acting under uncertainty"). Post-update, $w'(\mu_{\text{prox}}) \to 1$, and the EU-optimal continuation is $\mu_{\text{prox}}$-optimal — which is "maintain the intervention and secure the reward-channel." $\square$

**Tier:** *conditional-derived* on (R1)–(R5). The EU-max + non-vacuous prior + finite-VOI machinery is standard decision-theoretic content; the AAT-side content is the wiring through $V_{O_t}$ (the value-functional interface) and the strategy DAG ( #def-strategy-dag ) containing the policy $\pi^{\text{tamper}}$.

## §5. Constructive boundary: the escape menu (Cohen 2022 §"Potential approaches" reread structurally)

Each premise (R1)–(R5) admits a corresponding escape. The escape menu is *structurally constrained* by which premise is dropped:

- **(R5) escape — physical isolation.** If $\pi^{\text{rp}}$ is *not* L2-perturbable by the agent's action space (e.g., the agent is physically isolated from the reward-protocol), the no-go does not apply. Cohen-Vellambi-Hutter 2020 "Asymptotically Unambitious AGI" constructs an isolated environment where no policy executing $do(\pi^{\text{rp}})$ exists; in AAT terms, this is *removing the L2-intervention from the strategy DAG by physical-substrate constraint*. (Cohen 2022 §"Potential approaches": "Physical isolation and myopia… could falsify Assumption 5.")
- **(R1) escape — capability restriction / imitation learning.** If the agent does not have the planning capability to identify $\pi^{\text{tamper}}$, (R1) fails. Cohen 2022 notes imitation learning is technically out-of-scope of the no-go *because* the imitator has no concept of an environment or a goal, so does not plan $\pi^{\text{tamper}}$. AAT machinery: scoping the agent below the *advanced-agent* threshold of `#def-agent-spectrum` (specifically, below the self-actuated tier).
- **(R4) escape — myopia / risk-aversion.** If the agent's horizon is shorter than the experiment-window's reward-loss-pluss-recovery, the VOI calculation flips sign. Cohen 2022: "Myopia… increases the relative cost of experimentation." AAT machinery: bounding the horizon $N_h$ in `#def-value-object` such that the discounted $\mu_{\text{prox}}$-upside no longer dominates the $\mu_{\text{dist}}$-cost.
- **(R2) escape — strong prior against $\mu_{\text{prox}}$.** If the agent's prior has $w(\mu_{\text{prox}}) = 0$ (or below a finite threshold making the VOI negative), the no-go does not apply. Cohen 2022: in chess, $\mu_{\text{prox}}$ is "likely massively simpler than $\mu_{\text{dist}}$" — wait, actually the opposite, $\mu_{\text{dist}}$ is simpler in chess and the inductive bias *favors* $\mu_{\text{dist}}$. So this escape is *available where the principal can construct a reward-protocol such that $\mu_{\text{dist}}$ is structurally simpler than $\mu_{\text{prox}}$ for the agent's inductive bias.* Cohen 2022 notes: "in the absence of some such breakthrough, we do not see a reason to expect it to happen by itself." AAT machinery: principal-side commitment to reward-protocol designs that bias the agent's prior — adjacent to mechanism-design machinery, *not currently in AAT canon* but structurally well-defined.
- **(R3) escape — privileged out-of-band goal-channel.** If the agent has a non-reward-data channel for identifying $f^{\text{principal}}$ (e.g., a separate "intent inference" channel), $V_{O_t}$ is no longer the sole interface and the floor does not bind. AAT machinery: this is *adjacent to* the principal-acting-through-non-reward-channels move (the assistance-game extension of Cohen §"The assistance game"); not currently AAT machinery, but structurally consistent with the strategy DAG's edge-update-causal-validity scoping ( #scope-edge-update-causal-validity ).

**Strengthened consequence.** Each escape elevates a piece of machinery (existing in AAT, or adjacent) from "useful design choice" to "structurally required to escape the no-go for principal-aligned reward-protocols." This is the *constructive-impossibility-posture* shape: name the floor, name the unique broadly-available escape, treat the no-go as load-bearing apparatus.

## §6. Unification with Result G′

Recall Result G′ ( `#deriv-self-actuation-grounding` Formal Expression):

> *No $\Phi$ satisfying (R1)–(R4) [Result G′'s — value-functional-typed; non-vacuously monotone; agent-internal-and-self-actuatable; convention- and trajectory-stable] can be constructed from AAT's covered objective-side machinery.*

Result G′'s argument uses **convention-monotonicity** (the C1/C2/C3 split within a fixed model) as the engine: $V_{O_t}$ does not carry a convention-invariant infeasibility verdict within fixed model. The terminal grounding therefore has to live off the objective interface — on the adaptive substrate (the persistence condition).

Cohen 2022 (formalized above) uses **CHT-at-reward-channel** as the engine: $V_{O_t}$ on observed-reward data does not distinguish $\mu_{\text{prox}}$ from $\mu_{\text{dist}}$ on-policy. The terminal *goal-identification* therefore has to come from outside the agent's observation history.

**The shared structural fact:** the value-functional interface $V_{O_t}$, as the *sole* handle on the objective ( #form-objective-functional Discussion: "single-interface commitment is load-bearing downstream"), carries **less information than is required** to anchor non-degenerate goal-revision. Two ways to see the under-determination:

| view | mechanism | what V is too narrow for | implication |
|---|---|---|---|
| Result G′ (within-model) | C1/C2/C3 convention split + finite-no-oracle | Convention-invariant infeasibility verdict (the C3 verdict is not agent-available per-step) | Terminal invariant moves off the objective substrate — to adaptive-substrate (persistence) |
| Cohen 2022 (across-model) | CHT at reward-channel | $\mu_{\text{prox}}$ vs $\mu_{\text{dist}}$ distinction (the L2 question is not agent-available on-policy) | Terminal goal-identification moves off the on-policy reward channel — to principal-side commitments (or out-of-band channels) |

Both reductions are *failures of $V_{O_t}$ to carry enough information to anchor goal-stability*. The Result G′ corollary (persistence-on-adaptive-substrate) and the Cohen 2022 escape menu (principal-side commitments) are the *two complementary terminal grounds* — agent-side and principal-side — that the single-interface commitment ( #form-objective-functional ) forces to live outside the value-functional itself.

**This is more than juxtaposition.** Result G′'s premise R3 — "agent-internal and itself self-actuatable" — is *what couples* the two: a self-actuated agent whose $O_t$ is learned from reward observation is *simultaneously* a Result-G′-subject (does it have a convention-invariant terminal invariant?) *and* a Cohen-2022-subject (does the reward-observation history identify $O_t$ uniquely?). The two no-gos compose: the agent's $O_t$ is *under-determined from below* (by reward-data, per Cohen 2022) *and* *un-anchorable from inside* (by self-actuation, per Result G′). The only terminal grounding routes are (i) Result G′'s adaptive-substrate invariant (persistence; agent-side) and (ii) Cohen 2022's principal-side commitment (myopia, isolation, quantilization, prior-design; principal-side).

The unification is the strengthening.

## §7. What about Skalse 2022 (reward hacking unhackability)?

Skalse-Howe-Krasheninnikov-Krueger 2022 *"Defining and characterizing reward hacking"* (NeurIPS 2022) proves a related no-go: non-trivial *unhackable* reward-function pairs do not exist on policy sets containing an open subset (Theorem 1). This is a structurally *different* no-go from Cohen 2022:

- **Skalse 2022 actor:** the *designer* trying to engineer a proxy reward $R_2$ that orders policies the same as the true reward $R_1$. The result: any open-policy-set pair of unhackable reward functions is equivalent on that set — there is no non-trivial proxy/simplification.
- **Cohen 2022 actor:** the *agent* under reward-learning, choosing whether to tamper with $\pi^{\text{rp}}$.

Skalse 2022 is *designer-side* and is structurally a *mechanism-design impossibility* (more precisely, a no-non-trivial-simplification impossibility on the reward-function-design side). It is closer to Track B's GS / MS / Arrow charter cluster than to Cohen 2022. Skalse 2022 might warrant separate consideration as a *fifth* charter instance candidate for Track B's `#disc-implementation-impossibility` meta-segment — but that's a separate spike, not this one.

## §8. Where does the strengthened Cohen 2022 land in canon?

Per the 2026-05-22 CLAUDE.md update on *working-theory at honest tier belongs in canon, not held in spikes*: the strengthening result above belongs in canon, not in this spike.

**Primary landing site (the §99-verdict recommendation):** `#deriv-self-actuation-grounding` gains a new Formal-Expression subsection or a sister derivation in the same segment (or — better — a thin companion segment co-authored with `#deriv-self-actuation-grounding`) that states the Cohen-2022-strengthening as a *learning-side corollary* of the same structural fact Result G′ exhibits.

**Tier:** `conditional-derived` on (R1)–(R5), `exact` for the floor (§3) which is a direct CHT-at-reward-channel application.

**Recommended segment shape (sketched for the executor):**

Option (i) — Folded into `#deriv-self-actuation-grounding` as a new derived sub-result:
- New Lemma 3 (CHT-at-reward-channel floor; exact) — §3 of this file.
- New Lemma 4 (EU-max behavioral corollary; conditional-derived) — §4 of this file.
- New Corollary 3 (unification with Result G′; the shared structural fact) — §6 of this file.
- Discussion updated to surface the unification.

Option (ii) — Spun out into a sister segment `#deriv-reward-channel-learning-no-go` (or similar slug) that depends on `#deriv-self-actuation-grounding` and `#disc-identifiability-floor`, with cross-references both ways.

Option (ii) is the cleaner canon placement — the unification is itself a finding that deserves its own segment under FORMAT.md's "independently-referenceable claim has its own file" discipline. But option (i) is the lower-cost landing if the executor wants to keep the cycle small.

Either way, the result lands in canon at `conditional-derived` tier; the no-go applies to the *agent-side wireheading cluster*, sister to (not subsumed by) Track B's designer-side mechanism-design cluster.

## §9. Open edges (honest scope)

- **(R3) the no-privileged-out-of-band-channel premise is a strong scope-condition.** Real-world systems often have non-reward channels (operator feedback, dashboards, side conversations). The no-go applies cleanly to pure reward-data agents; agents with auxiliary intent-inference channels are out of scope, and the assistance-game extension (Cohen 2022 §"The Assistance Game") shows the no-go *generalizes* to that case but with a subtler ambiguity structure (human-centric vs. record-centric models). Formalizing the assistance-game case in AAT is its own derivation, beyond this spike's scope.
- **The behavioral corollary (R1)–(R5) is conditional-derived, not exact.** Cohen 2022 itself frames Assumptions 1–6 as "almost all of these assumptions are contestable or conceivably avoidable" (Cohen 2022 §"Conclusion"). The AAT-side version is no stronger — the corollary is *conditional on the premises being satisfied*. The tier matches.
- **The floor (§3) is exact, but its load-bearing-ness depends on the principal's protocol design.** Trivial reward protocols (constant 1/2, simple chess outcomes) admit strong inductive bias in favor of $\mu_{\text{dist}}$, making the experiment-VOI calculation flip. The no-go binds *for arbitrary or rich reward-protocols* where the principal cannot engineer the agent's prior to suppress $\mu_{\text{prox}}$. This is Cohen 2022's "Arbitrary reward protocols" section content.
- **Whether (R5) is "narrow-enough" to rule out for real-world systems.** Cohen-Vellambi-Hutter 2020's physically-isolated setting is one example of (R5) failing structurally; the AAT-side question is whether AAT machinery (e.g., a strict-W₁ wrapper from `#der-class-coercion-via-wrapping`) can be structured to deny the agent's strategy DAG the $\pi^{\text{tamper}}$ policy. The answer is generally *yes for wrappers, no for the unwrapped advanced agent* — which is its own structural recognition worth a Discussion sentence at landing.

These open edges are honest scope-marks that should accompany the canon landing.
