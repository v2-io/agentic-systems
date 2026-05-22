# Spike: Actuated $\rho$-Regulation — the Persistence Inequality with Both Sides Under Partial Agent Control

**Status.** Open spike, ~segment-grade derivation drafted. Not yet integrated. Candidate landing: new AAT segment `#disc-rho-actuation` (discussion-grade meta-pattern) with a derived companion `#deriv-actuated-disturbance-rate` (theorem-grade for the conditions under which admission-control is feasible and the sat-gap is the *exclusive* price paid).

**Date.** 2026-05-21.

**Pressure point.** AAT's central inequality (`#result-persistence-condition`, operational form $\mathcal T \gt \rho / \lVert \delta_{\text{critical}}\rVert$) is currently stated with $\rho$ as exogenous — the environment imposes a disturbance rate, the agent must maintain tempo above the threshold. The Release It! demand-control patterns (backpressure, load-shedding, handshaking, self-denial, governor) — surfaced by the 2026-05-21 TST mining (`spikes/tst-mining-2026-05-21/01-release-it-mining.md` A6, and called out in `TST-IDEAS.md` §C1 as the highest-yield genuinely-new-AAT-structure finding of the cycle) — invert the picture: a running agent has actions in its repertoire that *modulate its own incoming $\rho$*. Backpressure slows upstream producers. Load shedding refuses observations. Handshaking declares capacity. Token-bucket and leaky-bucket are specific implementations. The persistence inequality becomes $\mathcal T \gt \rho_{\text{effective}} / \lVert \delta_{\text{critical}}\rVert$ with $\rho_{\text{effective}} \le \rho_{\text{offered}}$ achievable via admission-control. The cost is paid as a satisfaction-gap (work refused).

This spike works the structural shape to derivation-grade, names the conditions under which it holds, identifies what still needs theorem-grade work, and surfaces interfaces for the parallel `spike-running-software-agent.md` synthesis pass.

---

## 0. What I'm strengthening before softening

Per `feedback_math_novelty_recognition` and the project CLAUDE.md *Math-novelty recognition — do not deflate* discipline: the strengthen-first claim being attempted here is **substantive new structure**, not "an instantiation of existing machinery." The existing persistence-inequality treats $\rho$ as a parameter of the environment. The claim is that, for an admissible class of agents, $\rho$ *as it enters the inequality* is itself a controlled variable, and the cost of the control is paid in a different AAT-native diagnostic ($\delta_{\text{sat}}$). The inequality with both sides under partial agent control — and the structurally derivable cost-of-control accounting — is the new theoretical apparatus, not a reinterpretation of existing terms. The strengthen-first move is therefore to *derive* the apparatus, not to softly observe "and you could think of $\rho$ as controlled, sometimes." Where the derivation needs more than spike-grade work to close, I name the gap precisely.

The Honesty Call from `TST-IDEAS.md` §C1 is load-bearing and is held throughout: $\rho_{\text{effective}}$ is the *agent's perceived environmental disturbance rate* (its $\rho$ as it enters the agent's mismatch dynamics), not the queueing-theoretic arrival rate at an external admission point. The connection to Little's Law is suggestive but not isomorphic. Section 4 disciplines this carefully.

---

## 1. The structural setup

### 1.1 The standing definitions this builds on

From the existing AAT corpus:

- **Mismatch signal** (`#def-mismatch-signal`): $\delta_t = o_t - \hat o_t$. The signal that drives every adaptive update. *Definitional.*
- **Adaptive tempo** (`#def-adaptive-tempo`): $\mathcal T = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$. The agent's effective rate of acquiring useful information. *Definitional.*
- **Persistence condition** (`#result-persistence-condition`), linear operational form under Model D: $\mathcal T \gt \rho / \lVert \delta_{\text{critical}}\rVert$. *Exact* for linear correction; *useful approximation* for mildly nonlinear correction. The form most downstream applications cite.
- **Action and transition** (`#def-action-transition`): the agent has an action space $\mathcal A$; actions affect the environment via $\Omega_{t+1} \sim T(\cdot \mid \Omega_t, a_t)$. *Definitional.*
- **Satisfaction gap** (`#def-satisfaction-gap`): $\delta_{\text{sat}} = V_{O_t}^{\min} - A_O(M_t; \Pi, N_h)$. Positive when the objective is unmet under the best available policy. *Exact as a definition.*
- **Control regret** (`#def-control-regret`): $\delta_{\text{regret}} = A_O - V_O(M_t, \pi_{\text{current}}; N_h) \ge 0$. The orthogonal diagnostic to $\delta_{\text{sat}}$. *Exact as a definition.*

The standing reading is: in $\mathcal T \gt \rho / \lVert \delta_{\text{critical}}\rVert$, the agent controls $\mathcal T$ through actions that increase $\nu^{(k)}$ or $\eta^{(k)\ast}$ (build better observation channels, tighten the prior, calibrate the update gain). The agent does *not* control $\rho$; $\rho$ is set by the environment.

### 1.2 The structural move: admission-control as a distinct action class

The structural claim is that the agent's action space $\mathcal A$ partitions, for an admissible class of agents, into two structurally distinct sub-spaces:

$$\mathcal A = \mathcal A_{\text{adaptive}} \sqcup \mathcal A_{\text{admission}}$$

*[Definition (action-space-partition), proposed]*

- **$\mathcal A_{\text{adaptive}}$ — adaptive actions.** Actions that change the environment state $\Omega_t$ (interventional probes, executions of $\Sigma_t$ that pursue $O_t$, environment modifications). These are the actions `#def-action-transition` formalizes via the transition function $T$.
- **$\mathcal A_{\text{admission}}$ — admission-control actions.** Actions that modulate which environment events become observations admitted into the agent's mismatch-dynamics path. These do *not* change $\Omega_t$; they change the *mapping* from $\Omega_t$ to the agent's observed event stream.

The distinction is structural, not parametric: an action in $\mathcal A_{\text{admission}}$ leaves $\Omega_t$ invariant in distribution but changes which sub-process of $\Omega_t$'s evolution becomes input to the agent's belief-update. *Examples* (translated from Release It! demand-control catalog into AAT vocabulary):

| Pattern | Admission-control action | What it modulates |
|---|---|---|
| Backpressure | Signal upstream producer to slow event-generation rate | $\nu^{(k)}_{\text{environment-as-experienced}}$, by negotiation with the source |
| Load-shedding | Drop event at agent boundary | $\nu^{(k)}_{\text{admitted}}$, by unilateral refusal |
| Handshaking | Declare capacity bound; cooperative producers self-throttle | $\nu^{(k)}_{\text{environment-as-experienced}}$, by capacity-advertising |
| Token/leaky-bucket | Rate-limit admitted event-rate to a configured ceiling | $\nu^{(k)}_{\text{admitted}}$, structurally bounded |
| Governor | Rate-limit *actuation*, indirectly throttling response-induced rebounds | $\nu^{(k)}_{\text{admitted}}$, via $\mathcal A_{\text{adaptive}}$ self-coupling |
| Circuit-breaker open | Refuse to admit events from a regime-shifted channel | $\nu^{(k)}_{\text{admitted}} = 0$ on that channel |

The structural-vs-behavioral distinction matters. Some admission-control actions are *structural* (load-shedding at the agent boundary is enforced by the agent itself — a typed refusal, akin to a $W_1$-style structural commitment in `#der-class-coercion-via-wrapping`). Others are *behavioral* (backpressure depends on the upstream producer's cooperation — akin to $W_2$ leakage-bounded behavior). The distinction propagates into the feasibility-of-admission-control analysis in §3.

### 1.3 The modulation function

Formalize the admission-control mechanism as a modulation function on the agent's perceived disturbance rate:

*[Definition (admission-modulation), proposed]*

Let $\rho_{\text{offered}}$ be the disturbance rate *the environment would impose* on the agent absent admission-control — i.e., the unmodulated $\rho$ from `#result-persistence-condition`. Let $a_{\text{adm}} \in \mathcal A_{\text{admission}}$ index the agent's admission-control policy. Then the *agent's perceived environmental disturbance rate* is

$$\rho_{\text{effective}}(a_{\text{adm}}) = m(a_{\text{adm}}) \cdot \rho_{\text{offered}}$$

where $m : \mathcal A_{\text{admission}} \to [0, 1]$ is the *admission-control modulation function*: $m(a_{\text{adm}}) = 1$ means admit everything (the standing $\rho_{\text{effective}} = \rho_{\text{offered}}$ case); $m(a_{\text{adm}}) \to 0$ means refuse everything (no events admitted, $\rho_{\text{effective}} \to 0$); intermediate values correspond to partial admission.

Three observations frame the rest of the spike:

**(a) Per-channel structure.** The single-channel form above generalizes to the per-channel form $m^{(k)}(a_{\text{adm}}) \cdot \rho_{\text{offered}}^{(k)}$, with the agent able to apply admission-control independently per channel. This connects to `#def-adaptive-tempo`'s tensor form: when admission-control reweights channels asymmetrically, the resulting effective-$\rho$ vector inherits the same per-coordinate structure that the tempo definition handles.

**(b) Range constraint.** The codomain $[0, 1]$ is the structural commitment that admission-control can only *reduce*, not *increase*, the disturbance rate. The agent cannot manufacture disturbance from below the offered rate (it can only refuse what is presented). The upper bound $m = 1$ is the "admit-everything-offered" baseline. The lower bound $m = 0$ requires structural refusal capability (see §3).

**(c) Boundary placement is structural.** The function $m$ is well-defined only when the agent has a structurally identifiable *boundary* at which admission-control can be exercised — a place where events have arrived at the agent but have not yet entered the belief-update path. For runtime services this boundary is concrete (the request-handler at the service edge). For agents whose belief-update is interleaved with their action loop more tightly, the boundary is less obvious; see §3.

### 1.4 The modified persistence condition

The persistence condition (`#result-persistence-condition`, linear operational form, Model D) with admission-control substituted for the exogenous $\rho$:

*[Derived (actuated-persistence-condition), conditional on (R1)–(R4) below]*

$$\mathcal T \gt \frac{\rho_{\text{effective}}(a_{\text{adm}})}{\lVert \delta_{\text{critical}}\rVert} = \frac{m(a_{\text{adm}}) \cdot \rho_{\text{offered}}}{\lVert \delta_{\text{critical}}\rVert}$$

The agent now has *three* operational levers against persistence-failure: raise $\mathcal T$ (the standing tempo-side story); lower $\lVert \delta_{\text{critical}}\rVert$ in the *operational* sense of accepting more mismatch (domain-controlled, slow); lower $\rho_{\text{effective}}$ via $m$ (the new lever, dynamically actuable, with structurally derivable cost). The first two are the existing toolkit. The third is the new structure.

The conditions under which this substitution is honest — i.e., the assumptions under which $\rho_{\text{effective}}$ is the *correct* rate to enter the persistence inequality, not just a smaller number to plug in — are the load-bearing premises (R1)–(R4) in §3.

---

## 2. The cost of admission-control: a satisfaction-gap

The persistence inequality with $\rho_{\text{effective}}$ is *easier to satisfy* than with $\rho_{\text{offered}}$; admission-control is, formally, a free lever for tempo-feasibility. But it cannot be free in the AAT-native cost accounting — otherwise every persistence problem reduces to "set $m = 0$ and the inequality holds." Where does the cost go?

### 2.1 The structural claim: $\delta_{\text{sat}}$ is where the cost lands

The structural claim is that admission-control's cost is paid in the *satisfaction-gap* diagnostic (`#def-satisfaction-gap`), not the *control-regret* diagnostic (`#def-control-regret`), and not in degraded tempo.

The argument, in spike-grade form:

- Refused work corresponds to objective shortfall. If the objective $O_t$ includes terms valuing throughput, latency-tail behavior, request-success-rate, or any quantity sensitive to the *rate of admitted events being acted on*, then refusing events (admission-control with $m \lt 1$) reduces the achievable value $A_O$.
- The objective's *satisfaction threshold* $V_{O_t}^{\min}$ is not changed by admission-control — what the agent is committed to achieving is set by the objective, not by the agent's admission policy. (If the agent could rewrite $V_{O_t}^{\min}$ downward in response to admission-control, that would be an objective-revision move, not a strategy move; the Orient cascade `#der-orient-cascade` reserves objective revision as the last-resort step.)
- $\delta_{\text{sat}} = V_{O_t}^{\min} - A_O(M_t; \Pi, N_h)$ therefore *increases* under admission-control whenever the refused work is throughput-valued: $A_O$ falls, $V_{O_t}^{\min}$ stays, $\delta_{\text{sat}}$ widens.
- $\delta_{\text{regret}} = A_O - V_O(M_t, \pi_{\text{current}}; N_h)$ does *not* increase from the admission-control move alone, because admission-control is *part of* the agent's available policy — the best available policy already accounts for it. If the agent chose its admission policy optimally, $\delta_{\text{regret}}$ stays near zero; if it chose suboptimally, the regret signal is independent and lives where it always did.

This is consistent with the 2×2 diagnostic table in `#def-control-regret` Discussion: admission-control under tight tempo constraints can produce the *"Capability limit"* cell — $\delta_{\text{sat}} \gt 0$ with $\delta_{\text{regret}} \approx 0$, "optimally pursuing an unmet goal." The agent is doing as well as its policy class allows; the unmet-goal signal is real; the corrective move (per the disambiguation table in `#def-satisfaction-gap`) is to check $M_t / \Pi / N_h$ and only then consider revising $O_t$ — *not* to revise the admission policy unless a better admission policy exists within $\Pi$.

### 2.2 Why the cost-attribution is structural, not arbitrary

A reasonable challenge: "couldn't the admission-control cost equally be charged to a degraded $\mathcal T$ — fewer events admitted means fewer observations means lower effective tempo?"

The answer is no, and the reason is in the form of the persistence inequality itself. The tempo $\mathcal T = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$ is defined on *admitted* event-rates — channels that contribute to the belief-update. An admission-control action that drops events at the boundary reduces the admitted channel-rate $\nu^{(k)}_\text{adm}$, and this is precisely what shows up on both sides of the persistence inequality: it reduces the effective disturbance $\rho_\text{effective}$ (the offered disturbance, less the dropped portion) by exactly the same factor as the admitted channel-rate (the channel rate that contributes to tempo). In the regime where the dropped events would have been *informative* (high update-gain on the channel), the two effects can cancel exactly, leaving the inequality untouched; that is the **Honesty Call regime** Section 4 develops carefully.

What admission-control *cannot* charge to is regret, because the admission-control policy is part of the available policy class — within-$\Pi$ refusal of work is not a strategy mistake, it is a deliberate $\Sigma_t$ choice. Charging admission-control's cost to $\delta_{\text{sat}}$ rather than $\delta_{\text{regret}}$ tracks exactly the AAT-native distinction between "the goal is unmet given current capacity" (sat-gap) and "we could have done better with a different strategy" (regret).

This is the cleanest structural result of the spike: admission-control's cost-accounting reduces, by construction, to the existing AAT 2×2 diagnostic, with the admission action's price paid exclusively in the sat-gap cell of the diagnostic. *No new diagnostic quantity is needed.* The agent already has the apparatus to reason about the trade-off.

### 2.3 The trade-off as a constrained optimization

The structural picture this resolves into: the agent's optimal admission-control policy, given a tempo-constrained substrate and a fixed objective, solves

*[Formulation (admission-control-optimization), proposed]*

$$a_{\text{adm}}^\ast = \arg\min_{a_{\text{adm}} \in \mathcal A_{\text{admission}}} \delta_{\text{sat}}(a_{\text{adm}}) \quad \text{subject to} \quad \mathcal T \gt \frac{m(a_{\text{adm}}) \cdot \rho_{\text{offered}}}{\lVert \delta_{\text{critical}}\rVert}$$

— find the *most-admissive* policy that still satisfies persistence. The constraint binds when $\rho_{\text{offered}}/\lVert \delta_{\text{critical}}\rVert \ge \mathcal T$ (the unactuated persistence-inequality fails); below that regime, the *admit-everything* policy $a_{\text{adm}} = a_{\text{open}}$ is optimal ($\delta_{\text{sat}}$-minimizing) and the persistence-inequality is satisfied with margin. The constraint binds increasingly tightly as $\rho_{\text{offered}}$ rises. When admission-control is structurally impossible (no element of $\mathcal A_{\text{admission}}$ achieves $m \lt 1$, or no admissible $a_{\text{adm}}$ satisfies the constraint), the optimization is infeasible and the agent enters the regime where unactuated persistence fails — the **self-denial-attack regime** of §3.4.

This formulation closes the spike's core structural claim: a persistence-inequality with both sides under partial agent control, with the cost-of-control attributable cleanly to existing AAT-native machinery. Sections 3 and 4 then disciplines the *conditions* under which the construction holds and the *boundaries* across which it breaks.

---

## 3. Feasibility conditions: when admission-control is available

Admission-control is not always available. The structural conditions under which the agent can exercise admission-control are themselves the load-bearing premises of the derivation. Naming them precisely:

### 3.1 The four feasibility premises

*[Hypothesis (admission-control-feasibility-premises), spike-grade]*

The actuated-persistence-condition (§1.4) holds for an agent $A$ with admission-control policy $m$ when:

- **(R1) Refusal capability.** The agent's action space contains at least one element $a_{\text{adm}} \in \mathcal A$ whose execution produces $m(a_{\text{adm}}) \lt 1$ — i.e., the agent can refuse at least some events. This is *not* automatic. Many agent designs have no refusal-action: a sensor pipeline that polls its input has no "decline this observation" move; a hardcoded ETL job that runs on a schedule has no "I'm overloaded, skip this batch" move. The *existence* of a refusal action is a design property of the agent.

- **(R2) Identifiable admission boundary.** The agent has a structurally identifiable boundary — a point in its processing pathway — at which events have *arrived* but have not yet entered the belief-update. For runtime services this is concrete (the request handler). For agents with tighter sense-act interleaving the boundary requires explicit identification. Without an identifiable boundary, the modulation function $m$ is not well-defined: there is no point at which the admission action can be applied.

- **(R3) Modulation-action tempo.** The admission-control loop itself must operate at a tempo sufficient to react to $\rho_{\text{offered}}$. The agent must be able to *decide whether to admit* faster than events arrive. Formally: the admission-decision channel has its own $(\nu_{\text{adm}}, \eta_{\text{adm}}^\ast)$, and admission-control is *effective* only when $\nu_{\text{adm}} \gtrsim \rho_{\text{offered}}$ (the agent can decide on admission at least as fast as events present). When this fails — when $\rho_{\text{offered}}$ rises faster than the agent can sense-and-decide on admission — admission-control itself collapses; see §3.4 for the regime.

- **(R4) Bounded cost of refusal.** The cost paid in $\delta_{\text{sat}}$ for refusal is finite and increases at most boundedly with the refusal rate. In particular, the objective $O_t$ does not contain a hard-feasibility term that becomes infeasible when *any* event is refused. (When such a hard-refusal-intolerance is present, admission-control is *unavailable as a tempo-management lever* — refusing produces an immediate $A_O = -\infty$ rather than a finite $\delta_{\text{sat}}$ widening, and the optimization in §2.3 has the trivial answer "do not refuse" regardless of persistence feasibility.)

These four premises — (R1) refusal-capability, (R2) identifiable boundary, (R3) admission-decision tempo, (R4) bounded refusal-cost — partition the class of agents into *admission-controllable* and *not*. They are not assumed always to hold; they are the *axiomatic premises* of the actuated-persistence-condition. When they hold, the result follows. When they fail, the result does not apply and the agent reverts to the unactuated $\rho_{\text{offered}}$ persistence regime.

This satisfies the integration-is-replacement discipline: the unactuated persistence-condition (`#result-persistence-condition`) is not "softened" by the actuated form; it is *the same inequality, applied at the place admission-control reaches*. When (R1)–(R4) hold, $\rho_{\text{effective}}$ enters the inequality. When they fail, $\rho_{\text{offered}}$ enters. The inequality itself is unchanged.

### 3.2 The W-regime parallel: structural vs behavioral admission-control

The structural-vs-behavioral distinction that `#der-class-coercion-via-wrapping` already names for $W_1$ vs $W_2$ wrapping reappears here cleanly, and the parallel is theoretically illuminating rather than incidental.

**Structural admission-control** (load-shedding, token-bucket, leaky-bucket, hard rate-limit at agent boundary). The agent itself unilaterally refuses events at its boundary. The modulation function $m$ is enforced by the agent's own structural commitment — typed refusal, runtime-enforced rate-ceiling, hard rejection at the request handler. Leakage of refused events into the belief-update is zero by construction; the bound is *structural*, derivable from the boundary's type signature. This is the $W_1$-analog of admission-control.

**Behavioral admission-control** (backpressure, handshaking, polite cooperative throttling). The agent signals to its upstream producer that it would prefer reduced event-rate; the producer's compliance is *behavioral*. The agent's modulation function $m$ depends on the producer being a *cooperative producer*; an uncooperative producer ignores the backpressure signal and continues to offer events at the original rate. The bound is *behavioral*, bounded by the producer's compliance rate. This is the $W_2$-analog of admission-control.

The two regimes have different feasibility profiles:

- Structural admission-control is *always available given (R1)–(R4) hold* — the agent's unilateral refusal capability is sufficient. The cost is the $\delta_{\text{sat}}$ paid for the refused work and (potentially) for upstream-failure cascades the unilateral refusal triggers (the upstream producer that received a 503 may have its own persistence-inequality stressed by the unconsumed work).
- Behavioral admission-control is *available conditional on producer cooperation* — when present, it is gentler (work is not refused outright; it is rate-shaped upstream and the $\delta_{\text{sat}}$ cost is distributed across the system rather than concentrated at the boundary), but it is brittle to producer non-compliance (adversarial or self-denial-attack regimes — see §3.4).

The architectural-vs-parametric framing of GUC classes in `#der-class-coercion-via-wrapping` extends naturally: agents with structural admission-control have the *architectural* commitment to refuse-capability; agents relying on behavioral admission-control have a *parametric* relationship to the upstream's cooperation rate.

### 3.3 The agent-internal-vs-boundary feasibility gap (interface for `spike-running-software-agent.md`)

A specific feasibility concern flagged by `TST-IDEAS.md` §C1 and worth surfacing for the synthesis pass: *admission-control is non-trivial at internal-component boundaries*. The architectural picture so far has assumed an *external* boundary — the agent's edge where it meets its environment. But composite agents (the running-software-agent picture from `spike-running-software-agent.md` substrate, with components inside a wrapping construction per `#der-class-coercion-via-wrapping`) have *internal* boundaries between components, and the actuated-persistence story may want to apply at internal boundaries as well as at the system edge.

The structural question — does the modulation function $m$ admit a sensible definition at internal boundaries? — has a partial answer:

- *At internal boundaries between Class A components*, admission-control is structurally available. A component refusing to admit an event from a sibling component is a typed refusal, no different from the external case. The cost is paid in *upstream sibling's* sat-gap, not the refusing component's — which raises the principal accounting question: in a composite agent, is the sat-gap an agent-level diagnostic that aggregates across components, or a component-local one?

- *At internal boundaries involving Class B / Class C components* (per `#der-class-coercion-via-wrapping`'s component-admissibility partition), admission-control is more subtle. A Class C component (fundamentally goal-conditioned) cannot have its admission decided independently of $G_W$ — refusal would itself be a goal-conditioned action — and the structural-vs-behavioral distinction collapses.

- *At the wrapper boundary in a $W_1$ wrapping construction*, admission-control on the wrapper-to-component query channel is exactly the kind of structural commitment $W_1$ already makes — the wrapper *can* refuse to issue a goal-blind query, and the structural commitment holds. This connects admission-control directly to the existing wrapping-regime machinery.

The unresolved item: the *composite-agent sat-gap aggregation rule* under admission-control across internal boundaries. This needs care because if internal-boundary admission-control redistributes sat-gap from "the system as a whole" to "the upstream component that was refused," the diagnostic's load-bearing meaning is preserved only if the composite agent's $O_t$ aggregates component-level objectives consistently. **This is the load-bearing assumption I am flagging for the synthesis-pass reconciliation with `spike-running-software-agent.md`**: when the running-service spike formalizes the composite agent's $O_t$ structure, the actuated-$\rho$ machinery here should plug in with the sat-gap aggregation rule already determined — or the two spikes need to reconcile their assumptions in synthesis.

A *strong* version of the structural claim — needing more work than this spike provides — would derive the composite-agent sat-gap aggregation from component-level sat-gaps and the wrapping construction's class-coercion mechanics. The derivation is plausible (the wrapping construction's $W_1$/$W_2$ regime should determine how sat-gap aggregates across the wrapped boundary) but is *not closed here*. Section 5.2 names this as a follow-on derivation explicitly.

### 3.4 The self-denial-attack regime (where premises (R1)–(R4) fail catastrophically)

The Release It! "self-denial attack" pattern (mining 01-release-it-mining.md §A6, B3; analyses 033 and 038) names the regime where admission-control breaks down catastrophically: $\rho_{\text{offered}}$ spikes faster than the agent's admission-decision tempo can absorb (R3 fails); or the offered events arrive through a channel the agent has no boundary-level refusal-action on (R1 fails at that channel); or the cooperative-producer assumption underwriting behavioral admission-control breaks down (the upstream producer ignores backpressure — implicit assumption in behavioral admission-control that the spike's §3.2 structural-vs-behavioral analysis should have surfaced, and which the spike makes explicit now).

Structurally, the self-denial regime corresponds to: the actuated persistence-inequality reduces to the unactuated form because admission-control cannot effectively modulate $\rho$ within the relevant time-horizon. The inequality $\mathcal T \gt \rho_{\text{offered}}/\lVert \delta_{\text{critical}}\rVert$ binds, and if it fails, the agent enters the regime of persistence-failure proper. The self-denial attack is *not* a separate failure mode beyond the existing persistence-condition story; it is the specific shape of persistence-failure *for agents whose admission-control was the design's tempo-management strategy*. Without admission-control, the agent never relied on actuating $\rho$ in the first place; with admission-control, the failure of admission-control is the proximate cause of persistence-failure, and the existing persistence-condition apparatus diagnoses it correctly.

This is the **strengthening, not weakening, of the self-denial-attack story**: AAT does not need a new failure-mode concept for self-denial; the existing persistence-condition apparatus *predicts the failure mode under exactly the conditions where premises (R1)–(R4) fail* and admission-control's $\rho$-actuation cannot hold. The Release It! pattern's empirical-engineering content gets the AAT-native frame for free.

---

## 4. The Honesty Call: $\rho_{\text{effective}}$ is the agent's perceived disturbance rate, not the queueing-theoretic arrival rate

This is the load-bearing care-point that `TST-IDEAS.md` §C1 explicitly calls out and that the analysis-text in `01-release-it-mining.md` A6 acknowledged but did not formalize.

### 4.1 What goes wrong if we conflate

The naive reading: "admission-control is queueing-theory rate-limiting; just apply Little's Law." This is wrong in three specific ways:

**(a) $\rho$ in AAT is not arrival rate.** In the persistence inequality, $\rho$ is the *rate of environmental change driving mismatch* — the rate at which the agent's $M_t$ becomes stale relative to $\Omega_t$. In queueing theory, the arrival rate $\lambda$ is the rate of work units presenting at a server. The two coincide only in the special case where every arrival corresponds to a unit of environmental change that the agent must track. In general, environmental change can occur without arrivals (the world drifts unobserved between events) and arrivals can occur without environmental change (redundant duplicates of the same event).

**(b) Refusing a non-informative event does not reduce $\rho$.** If the agent refuses an arrival that would have been a *redundant* observation (high $U_o$ on the channel, near-zero $\eta^\ast$), no environmental-change-tracking is lost — but no $\rho_{\text{effective}}$ reduction is achieved either, because the underlying environmental drift continues unobserved at the same rate. The modulation function $m$ is a function on the rate of *informative environmental observations admitted*, not on the rate of *arrivals at the boundary*. When channels carry highly-redundant traffic, admission-control's $m$ has limited effective range — refusing redundant arrivals reduces only the redundancy, not the underlying $\rho$.

**(c) Refusing a *highly* informative event does not reduce $\rho$ proportionally.** This is the dual: if the agent refuses an arrival that would have been *uniquely* informative (low $U_o$, near-maximum $\eta^\ast$), the agent loses the ability to track a particular dimension of environmental change. The mismatch dynamics on that dimension continue *at the full unmodulated rate*; the agent simply has worse $\mathcal T$ on that dimension. In this regime, admission-control trades $\rho_{\text{effective}}$ reduction *against* $\mathcal T$ reduction on the same channel, with the trade governed by the channel's $\eta^{(k)\ast}$. The persistence-inequality LHS and RHS can move *together* under admission-control on highly-informative channels — sometimes cancellingly.

These three failure-modes of the naive queueing-theory reading are real and structural. The honest formulation has to handle them.

### 4.2 The disciplined formulation

The disciplined version of the modulation function:

*[Formulation (channel-specific-modulation), spike-grade]*

For each observation channel $k$ at the agent boundary, admission-control modulates the channel's contribution to *both* $\rho_{\text{effective}}^{(k)}$ *and* $\nu^{(k)}$ (and thus $\mathcal T$) according to:

$$\rho_{\text{effective}}^{(k)}(a_{\text{adm}}) = m^{(k)}(a_{\text{adm}}) \cdot \rho_{\text{offered}}^{(k)}$$

$$\nu^{(k)}_{\text{admitted}}(a_{\text{adm}}) = m^{(k)}(a_{\text{adm}}) \cdot \nu^{(k)}_{\text{arriving}}$$

— admission-control affects both sides of the persistence inequality on the affected channel. The net effect on persistence-margin from refusing fraction $1 - m^{(k)}$ of channel-$k$ arrivals is:

$$\Delta(\mathcal T - \rho_{\text{effective}}/\lVert \delta_{\text{critical}}\rVert) = -\eta^{(k)\ast} \cdot (1 - m^{(k)}) \cdot \nu^{(k)}_{\text{arriving}} + \frac{(1 - m^{(k)}) \cdot \rho_{\text{offered}}^{(k)}}{\lVert \delta_{\text{critical}}\rVert}$$

The first term is the *loss* to tempo on channel $k$ from refusing informative events; the second is the *gain* from no longer being responsible for tracking the refused events' environmental change.

The trade collapses to a per-channel admission-control sign condition:

$$\text{admission-control on channel } k \text{ is net-positive for persistence} \iff \frac{\rho_{\text{offered}}^{(k)}}{\nu^{(k)}_{\text{arriving}} \cdot \lVert \delta_{\text{critical}}\rVert} \gt \eta^{(k)\ast}$$

**Reading this condition:** the LHS is the disturbance-per-arrival ratio normalized by tolerance; the RHS is the channel's information-yield per arrival. Admission-control helps persistence on channel $k$ when the channel carries more disturbance-per-event than information-per-event — i.e., when refusing events disposes of more rho-burden than tempo-contribution.

This is a structurally clean result and it disciplines the *naive* claim that "admission-control reduces $\rho_{\text{effective}}$ helpfully." It does — but only on channels where the disturbance-to-information ratio crosses the channel's update-gain threshold. On channels where every event is uniquely informative (high $\eta^{(k)\ast}$, low redundancy), admission-control does *not* help persistence, even though it reduces $\rho_{\text{offered}}^{(k)}$ — because the same admission-control reduces $\nu^{(k)}$ proportionally and the agent loses tempo it cannot afford to lose.

### 4.3 What this rescues from the Honesty Call

The Honesty Call from `TST-IDEAS.md` §C1 — that $\rho_{\text{effective}}$ is not the queueing-theoretic arrival rate and Little's Law is suggestive-not-isomorphic — is held by §4.2's disciplined channel-specific formulation. The modulation function $m^{(k)}$ is *channel-specific*, *informativeness-weighted*, and *not a global rate-limit applied uniformly*. The connection to queueing-theory is real for the special case where channels are fungible (one channel, all events equally informative, high redundancy), and this is the regime where Release It! patterns operate in their cleanest form (HTTP request handlers, where requests are largely fungible at the load-shedder's resolution). But the *general AAT formulation* is per-channel and informativeness-weighted, and the disciplined sign-condition in §4.2 makes the regime in which admission-control helps explicit.

This is the strengthen-first move on the formalization itself: the cleanest result is *not* "admission-control reduces $\rho$" — it is "admission-control net-helps persistence under a precisely-stated per-channel disturbance-to-information sign condition, *and fails to help on high-informative-yield channels*." The negative-result content — that admission-control is not universally net-positive — is itself a load-bearing AAT-internal result. The persistence inequality remains the central inequality; the spike clarifies the conditions under which the new lever bites.

---

## 5. What this spike establishes, and what still needs work

### 5.1 What is closed at spike-grade

- **The structural action-space partition** (§1.2): $\mathcal A = \mathcal A_{\text{adaptive}} \sqcup \mathcal A_{\text{admission}}$, with the two sub-spaces distinguished by whether the action modifies $\Omega_t$ or modifies the mapping from $\Omega_t$ to the agent's admitted observations.
- **The modulation function** (§1.3): $m : \mathcal A_{\text{admission}} \to [0, 1]$, with structural commitments (codomain bounded, boundary-placement structural).
- **The actuated persistence-condition** (§1.4): $\mathcal T \gt m(a_{\text{adm}}) \cdot \rho_{\text{offered}} / \lVert \delta_{\text{critical}}\rVert$, conditional on (R1)–(R4).
- **The cost-attribution structural-result** (§2): admission-control's price is paid in $\delta_{\text{sat}}$, not $\delta_{\text{regret}}$, and reduces to the existing AAT 2×2 diagnostic — *no new diagnostic quantity is needed*.
- **The four feasibility premises** (R1)–(R4) (§3.1): refusal-capability, identifiable-boundary, admission-decision-tempo, bounded-refusal-cost.
- **The W-regime parallel** (§3.2): structural vs behavioral admission-control mirroring the $W_1$ vs $W_2$ wrapping-regime distinction.
- **The self-denial-attack regime** (§3.4): the existing persistence-condition apparatus diagnoses the failure-mode without needing new structure.
- **The disciplined channel-specific formulation** (§4.2): admission-control net-helps persistence on channel $k$ iff the disturbance-to-information sign condition holds — *not universally*.

### 5.2 What needs more than spike-grade work (named follow-ons)

These are not "this is hard" deferrals — they are precisely-named derivations that the segment-grade landing of `#disc-rho-actuation` and `#deriv-actuated-disturbance-rate` will need.

- **Composite-agent sat-gap aggregation under admission-control across internal boundaries.** The unresolved item from §3.3. The derivation likely runs through the wrapping construction's $W_1/W_2$ regime: a $W_1$-wrapped component's internal sat-gap aggregates structurally to the wrapper's sat-gap; a $W_2$-wrapped component's aggregates behaviorally with a bounded leakage term. The full derivation is *not* worked here; it is the load-bearing interface with the running-software-agent spike. **This is required for the segment landing.**

- **The behavioral-admission-control leakage bound.** §3.2 names structural and behavioral admission-control by analogy to $W_1$ and $W_2$, but the *leakage bound* for behavioral admission-control (analogous to $W_2$'s behavioral-compliance bound) is not derived here. Concretely: when an uncooperative producer ignores backpressure with rate $\beta$, the agent's effective $m$ is bounded above by $(1 - (1-m_{\text{nominal}}) \cdot \beta)$ — but this is conjectural, not derived. The derivation would parallel `#der-logogenic-as-wrapping`'s $W_2$ leakage-rate machinery and is required to close the behavioral-admission-control branch of the segment.

- **The matrix-Loewner extension.** `#def-adaptive-tempo`'s tensor extension and `#deriv-matrix-persistence-condition` handle anisotropic tempo via matrix-Loewner inequalities. The actuated-persistence story here is stated scalar-form-per-channel. The honest matrix-Loewner statement — where admission-control modulates a per-coordinate $\rho$ vector against a matrix-Loewner persistence condition — would integrate cleanly with the existing apparatus but is *not* worked here. The scalar form is the load-bearing case for the running-software-agent worked example (where channels are largely diagonal in the operational sense); the matrix form is the natural-formalization for anisotropic-correction agents (logogenic agents with cross-dimensional update-gain, per `#deriv-fisher-local-update-gain`).

- **The cost-shadow under stochastic disturbance.** `#deriv-persistence-cost` derives the information-rate floor $\dot R \ge n\alpha/2$ for sustained Shannon-information acquisition under Model S. The actuated-$\rho$ story should compose with this — admission-control reduces $\rho$, which should reduce the sustained information-rate the agent needs to acquire — but the composition rule is not worked here. The Model-S analog of the actuated persistence-condition is $\alpha \gt n\sigma_w^2 \cdot m^2 / (2\lVert \delta_{\text{critical}}\rVert^2)$ (the $m^2$ entering because $\rho$ is variance-rate-like under Model S), and the corresponding information-rate floor moves with $m^2$ rather than $m$. This is a derivation, not a spike-grade item, and is required for the segment to integrate consistently with the cost-shadow machinery.

- **The per-dimension actuated form.** `#result-per-dimension-persistence` gives the per-dimension persistence form $\mathcal T_k \gt \rho_k / \delta_{\text{critical},k}$. The actuated-per-dimension form is $\mathcal T_k \gt m^{(k)} \cdot \rho^{(k)}_{\text{offered}} / \delta_{\text{critical},k}$ and the weakest-dimension principle still binds. The derivation is straightforward (the per-dimension result lifts directly), but the spike does not work it explicitly.

### 5.3 The integration-as-replacement question

Per `feedback_integration_is_replacement`: when this spike lands, the `#result-persistence-condition` segment body should be *minimally* edited — *not* extended with "this can be generalized to actuated $\rho$, see..."; the persistence-condition's inequality is unchanged. The actuated story belongs in its own segment (`#disc-rho-actuation` / `#deriv-actuated-disturbance-rate`) that *applies* the persistence-condition with $\rho_{\text{effective}}$ as input, under premises (R1)–(R4). The persistence-condition segment carries the central inequality; the actuated segment carries the conditions under which $\rho$-as-it-enters-the-inequality is itself a controlled variable. The integration is replacement of the *implicit* "$\rho$ is exogenous" reading of the persistence-condition with the *explicit* "$\rho$ is exogenous in this scope; see the actuated segment for the regime where premises (R1)–(R4) hold" framing — a clarifying refinement, not a softening.

The body-signal to watch in the integration: the urge to write *"the persistence-condition has been extended to include actuated $\rho$"* into the persistence-condition body is the tell that the ghost is not deleted. The persistence-condition is *unchanged*; the actuated segment is a new, distinct result with its own premises and its own scope. They sit alongside.

---

## 6. Connection to other 2026-05-21 spikes

This spike runs in parallel with five others; the relevant interfaces:

- **`spike-running-software-agent.md`** (A1 of TST mining). The running-service persistence-condition $\mathcal T_{\text{runtime}} \gt \rho_{\text{env}}/\lVert \delta_{\text{critical}}\rVert$ is one of the cleanest worked-examples of the actuated-$\rho$ picture this spike develops. Specifically: the running-service spike's substrate (`#der-runtime-persistence-condition`) will instantiate this spike's actuated form with $m$ given by the service's load-shedding / backpressure / circuit-breaker policy, the four premises (R1)–(R4) interpreted at the service-edge level. **Synthesis-pass interface:** the running-service spike needs to inherit this spike's assumptions about agent-internal-vs-boundary admission-control feasibility (§3.3) and either confirm or refine the composite-agent sat-gap aggregation rule. Either spike could be the one that closes the aggregation derivation; if neither does, the segment-grade landing will need a third pass.

- **`spike-class-coercion-via-supervision.md`** (A2 of TST mining). The OTP supervision pattern as a class-coercion-via-wrapping instantiation. The W₁/W₂ regime parallel for admission-control (§3.2 of this spike) interlocks with the supervision spike's wrapping-regime analysis: a $W_1$-wrapped component can have *structural* admission-control on its query-channel by construction (the wrapper refuses the goal-blind query); a $W_2$-wrapped component's admission-control is behavioral. **Reconciliation:** when the supervision spike formalizes restart-strategy ↔ leakage-bound mappings, this spike's structural-vs-behavioral admission-control distinction is the same axis at the boundary-action layer rather than the state-leakage layer. Both spikes should land with consistent vocabulary on the structural-vs-behavioral distinction.

- **`spike-software-unmaintainability-bifurcation.md`** (A3 of TST mining). The G2-danger-zone bifurcation in software-persistence at the developer scale. The persistence-condition that spike works with is the unactuated $\rho$ form (developer-team-cannot-easily-actuate codebase change-rate — though *self-imposed change-freezes* and *technical-debt-paydown sprints* are arguably admission-control at the developer-agent layer). The interaction is light but worth noting: if the developer agent has structural admission-control over $\rho$ (via change-freezes, scope discipline, etc.), the unmaintainability bifurcation may have *one more* regime where admission-control rescues the persistence margin — at the cost of feature-throughput-objective sat-gap. The synthesis pass might want to surface this in the bifurcation spike.

- **The remaining two spikes (substrate-modifying actions, ETS-as-third-W-regime if re-opened).** Lower-priority interaction: substrate-modifying actions are a different action-class extension, orthogonal to admission-control's action-class extension; the segment-level placement may want to consider whether $\mathcal A = \mathcal A_{\text{adaptive}} \sqcup \mathcal A_{\text{admission}}$ should generalize to a three-way partition $\mathcal A_{\text{adaptive}} \sqcup \mathcal A_{\text{admission}} \sqcup \mathcal A_{\text{substrate}}$. Out of scope for this spike but worth flagging.

---

## 7. Recommended landing

The structural shape of the segment-grade landing, contingent on Joseph's review and on the §5.2 follow-on derivations closing:

**Primary segment:** `#disc-rho-actuation` (discussion-grade meta-pattern). Authored in `01-aat-core/src/`. Carries the action-space partition, the modulation function, the actuated persistence-condition statement, the cost-attribution to sat-gap, the structural-vs-behavioral admission-control distinction, and the self-denial-attack-regime framing. Discussion-grade because the load-bearing structural claim (cost paid in sat-gap, not regret) is more about the *AAT-native diagnostic mapping* than about a new mathematical result.

**Companion segment:** `#deriv-actuated-disturbance-rate` (theorem-grade). Carries the formal statement of the actuated persistence-condition under premises (R1)–(R4), the disciplined per-channel sign-condition from §4.2, the leakage-bound derivation for behavioral admission-control (when the §5.2 derivation closes), and the composite-agent sat-gap aggregation result (when the §5.2 derivation closes). Theorem-grade because, with the follow-on derivations closed, the result *is* a derivation: under (R1)–(R4) and the channel-specific sign condition, admission-control net-helps persistence by a precisely-bounded margin, with the cost paid in sat-gap by a precisely-derivable amount.

**OUTLINE placement.** Most naturally in `01-aat-core/OUTLINE.md` under the persistence-and-limits chapter, immediately after `#result-persistence-condition` and `#result-per-dimension-persistence` — the persistence-condition is the standing inequality; the actuated form is what happens when an admission-controllable agent is the subject.

**TST instantiation.** A worked-example segment `#example-backpressure-as-rho-actuation` in the new runtime-agent chapter (when the chapter lands per A1 of the mining). Demonstrates the move concretely on an HTTP service's request-handler boundary with token-bucket / load-shedding / circuit-breaker / backpressure as the modulation-function family.

---

## 8. Working notes — for the agent landing this

A few process-grade notes for the future agent integrating this:

- The action-space partition (§1.2) is the *least-committed* structural claim — it is presented as a *proposed* definition. An alternative formulation has $\mathcal A_{\text{admission}}$ as a *subset* (not a complement) of $\mathcal A_{\text{adaptive}}$, with admission-actions seen as a special class of adaptive-actions that act on the agent's own boundary rather than on $\Omega_t$. The partition framing is cleaner for the segment-grade derivation but may need defense if a reviewer pushes on it.

- The cost-attribution to sat-gap (§2) is the *strongest* structural claim and is the spike's headline yield. If a reviewer challenges anything else, this should be the result defended; everything else is supporting structure for it. The derivation in §2.2 is the load-bearing argument and should be tightened to theorem-grade in the segment landing.

- The per-channel sign-condition in §4.2 is the *most-precise* result and is what disciplines the naive queueing-theory reading. The derivation is straightforward from the persistence-inequality with the channel-specific modulation; the segment-grade version should carry the derivation explicitly (it is a one-liner from the inequality).

- The four feasibility premises (R1)–(R4) (§3.1) are the *most-likely-to-be-debated*. (R3) in particular (admission-decision tempo must keep up with offered rate) is a non-trivial sub-claim that needs its own anchoring — possibly to the matrix-Loewner weakest-channel discipline in `#deriv-matrix-persistence-condition` since admission-decision is itself one of the agent's channels.

- The Honesty Call discipline in §4 is what the spike protects most carefully and is the *most-likely-to-be-eroded* in the segment landing if cycle-pressure builds toward "let's just call it queueing-theory rate-limiting." Hold the line: it is *not* queueing-theory rate-limiting; it is informativeness-weighted per-channel admission-control with a derived sign-condition.

- This spike is consistent with the integration-is-replacement discipline: the persistence-condition segment is *not* edited to incorporate actuated $\rho$. The actuated story lives in its own segment that *applies* the persistence-condition under additional structural premises. The two sit alongside. The body of the persistence-condition segment carries the central inequality with $\rho$ as it appears; the actuated segment carries the conditions under which $\rho$-as-it-enters-the-inequality is itself an action-conditioned variable.
