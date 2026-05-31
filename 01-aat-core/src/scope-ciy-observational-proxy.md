---
slug: scope-ciy-observational-proxy
type: scope
status: conditional
depends:
  - def-causal-information-yield
  - der-loop-interventional-access
stage: draft
---

# Scope: CIY Observational Proxy

Clarifies what can be done with the causal-information-yield construct ( #def-causal-information-yield) when interventional data is *not* available. An observational *proxy* for CIY can be defined in terms of mutual information between the action and the next observation, but the framework is forthright: this proxy is **sign-indefinite in general** and requires causal assumptions for interpretation. The canonical interventional CIY remains the primary quantity; the proxy is auxiliary.

A pointed *safety condition* is stated: the proxy form should **not be used in policy optimization** (e.g., as the CIY term in a policy objective), because an agent maximizing a sign-indefinite quantity may optimize in the wrong direction. The proxy is suitable only for *diagnostic* purposes — detecting whether an action carried causal information (large proxy magnitude) versus none (proxy near zero). For actual decision-making, the canonical CIY (non-negative by construction) or a known-safe surrogate (ensemble disagreement, UCB bonuses) should be used; if the canonical CIY is intractable and no safe surrogate is available, the prescription is to *drop the CIY term entirely* and default to pure exploitation rather than risk the sign-indefinite quantity.

The segment then names three **admissibility regimes** that determine when CIY can be estimated and how strong the causal identification is. The regime is treated as a *property of the domain and the agent's action space*, not a parameter the agent chooses. **Regime A — randomized interventions**: the agent varies actions freely across episodes (RL agents exploring, scientists experimenting, organisms probing); CIY is directly estimable from execution data and non-negative by construction (the standard case for active agents within #der-loop-interventional-access). **Regime B — observational with causal assumptions**: the agent cannot freely vary actions (coordination, policy, or resource constraints); CIY estimation requires additional structure — a known causal DAG, instrumental variables, or functional-form assumptions — and inherits whatever causal assumptions are made. **Regime C — adversarial or passive observation**: the agent either did not intervene (passive monitoring, CIY zero by definition) or the observation channel includes potentially adversarial responses (where CIY from the query action itself remains non-negative but the *content* of the response may be designed to increase model-reality mismatch).

The regime classification has concrete domain implications: software development is typically Regime A (the agent runs tests, deploys to staging, observes results — high action variation); organizational strategy is typically Regime B (concurrent initiatives, attribution requires assumptions); intelligence analysis is typically Regime C (the analyst observes but does not intervene). The CIY machinery applies cleanly in Regime A, applies with weaker guarantees and explicit assumptions in Regime B, and should be replaced with alternative exploration strategies entirely in Regime C.

## Formal Expression

*[Definition (ciy-proxy)]*

$$\text{CIY}_{\text{proxy}}(a_{t-1}) = I(o_t; a_{t-1} \mid M_{t-1}) - I(o_t; a_{t-1} \mid \Omega_t, M_{t-1})$$

This proxy is **sign-indefinite in general** and requires causal assumptions for interpretation. The canonical CIY (interventional, #def-causal-information-yield) is the primary quantity; the proxy is auxiliary.

**Safety conditions for proxy use.** The proxy form should NOT be used in policy optimization (e.g., as the CIY term in a policy objective) because an agent maximizing a sign-indefinite quantity may optimize in the wrong direction. The proxy is suitable only for diagnostic purposes: detecting whether an action carried causal information (large proxy magnitude) vs. none (proxy near zero). For decision-making, use the canonical CIY (non-negative by construction) or a known-safe surrogate (ensemble disagreement, UCB bonuses). If the canonical CIY is intractable and no safe surrogate is available, the CIY term should be dropped from the policy objective entirely, defaulting to pure exploitation.

### Admissibility regimes

*[Scope Condition (ciy-admissibility)]*

Three regimes determine when CIY can be estimated and how strong the causal identification is:

**Regime A — Randomized interventions.** The agent varies its actions across episodes (RL agents exploring, scientists experimenting, organisms probing). CIY is directly estimable from the agent's execution data and non-negative by construction. This is the standard case for active agents within the adaptive loop ( #der-loop-interventional-access). Action variation provides the identification needed for clean interventional estimates.

**Regime B — Observational with causal assumptions.** The agent cannot freely vary actions (constrained by coordination, policy, or resource limits). CIY estimation requires additional structure: a known causal DAG, instrumental variables, or functional form assumptions. Results inherit whatever causal assumptions are made. The interventional interpretation of CIY is weaker — it holds under the assumed causal structure but not model-free.

**Regime C — Adversarial or passive observation.** The agent either did not intervene (passive monitoring) or the observation channel includes responses from potentially adversarial sources. In the passive case, CIY is zero by definition (no intervention, no interventional information). In the adversarial case, CIY from the query action itself remains non-negative, but the *content* of the response may be designed to increase model-reality mismatch. The adversary operates through the disturbance term $\rho$, not through the information measure.

The regime is a property of the **domain and the agent's action space**, not a parameter the agent chooses. Software development is typically Regime A (the agent runs tests, deploys to staging, observes results — high action variation). Organizational strategy is typically Regime B (multiple initiatives run concurrently, attribution requires assumptions). Intelligence analysis is typically Regime C (the analyst observes but does not intervene).

## Epistemic Status

Conditional on the causal assumptions within each regime. The proxy definition is standard information theory; the admissibility classification is a scope decision, not a derived result. The safety conditions for proxy use are normative — they follow from the sign-indefiniteness of the proxy, not from AAT-specific machinery.

Max attainable: conditional. The regime boundaries are domain properties that cannot be derived within the theory.

## Discussion

**Relationship to the canonical CIY.** The proxy is not an approximation of the canonical CIY — it is a different quantity that happens to correlate with CIY under favorable conditions (Regime A). The canonical CIY ( #def-causal-information-yield) is defined interventionally and is non-negative by construction. The proxy uses observational mutual information and can be negative. They agree when the agent's action variation satisfies the conditions for causal identification; they diverge otherwise.

**Regime as a domain property.** The admissibility regime is not something the agent selects — it is determined by the domain's action space and observation structure. An agent that cannot vary its actions is in Regime B or C regardless of its internal architecture. This has implications for which domains CIY-based exploration is applicable to: Regime A domains get the full benefit; Regime B domains get weaker guarantees; Regime C domains should use alternative exploration strategies entirely.

## Working Notes

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and lightly attributed. Orthogonal pedagogical / framing / figure / naming material, kept separate from the certified theory-fix findings (handled elsewhere). **Coverage:** dedicated reflections at 526815, 584721, 773921, 829314, 849201 plus the batch dirs 471203 / 963715. Substrate attribution inferred from voice where not explicit; uncertain cases hedged.

#### 1. Candidate Brief prose / pre-prose

- The sign-indefinite-proxy safety rule, as a Brief-grade line: *"never maximize a sign-indefinite proxy, or the agent might actively seek out blindness"* / *"an agent maximizing a sign-indefinite quantity may optimize in the wrong direction"* (Claude, AUDIT-WORKING-773921; the body already carries this — preserve it as the segment's punchline).
- *"Good engineering guidelines disguised as theory"* — several substrates read the segment's value as primarily operational-protective; the safe-degradation framing (*"drop the CIY term entirely and default to pure exploitation"*) is the takeaway worth foregrounding (Claude, AUDIT-WORKING-849201, 526815).

#### 2. Candidate Discussion

- **The "noisy TV problem" as the canonical motivating failure.** Strong candidate to add as the worked instance the safety condition exists to prevent: *"if you optimize for surprise / novelty using purely observational mutual information, you can build an agent that just stares at a TV screen showing static — the static is highly unpredictable given the past, so the agent thinks it is learning, but it learns nothing about causal structure. By stating the proxy is sign-indefinite and should never enter a policy objective, AAT protects developers from this exact trap"* (Gemini, AUDIT-WORKING-829314). This connects AAT's sign-indefiniteness rule to a widely-known RL pathology (the Burda et al. noisy-TV result) and would make the abstract safety condition concrete.
- **Regime A/B/C as a diagnostic for *where autonomous learning is even possible*** — read by two substrates as one of the framework's most useful practical tools: Regime A (software testing) → yes, learn causal structure perfectly; Regime B (organizational strategy / physical robotics — too expensive to crash the robot) → maybe, slow and assumption-dependent; Regime C (intelligence analysis / macro-economics) → no, trapped in L1. *"This elegantly explains why AI has succeeded spectacularly in games and coding (Regime A) but struggles in robotics (B) and macro-economics (C) — it's not a failure of the algorithms, it's a fundamental mathematical limit of the environment's admissibility regime; AAT makes this limit legible"* (Gemini, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-773921 — *"why curiosity-driven learning works in video games (A) but fails catastrophically in stock markets (C)"*). Candidate Discussion expansion of the regime-as-domain-property paragraph.
- **Regime C adversarial content as a formal definition of deception.** Reading the adversarial sub-case: an action $a$ can have high CIY (you got a response) while *the response was crafted to maximize your $\delta_t$* — *"a formal definition of deception"* connecting to the adversarial-destabilization results, where the adversary operates through $\rho$, not the information measure (Claude, AUDIT-WORKING-773921). Candidate sharpening of the Regime-C paragraph.

#### 3. Follow-up items

- **Observability of $\Omega_t$ in the proxy formula.** The proxy conditions on $\Omega_t$; if $\Omega_t$ is the *true* environment state it is not generally computable from ordinary observations (it is a population-level identity, not a computable quantity), and if it is an *estimated* state the formula should say so and inherit model-error caveats. Candidate clarifying sentence so a reader doesn't try to evaluate the proxy directly (Codex/Claude, AUDIT-WORKING-526815; same structural reading, framed cleanly, at AUDIT-WORKING-963715 — *"$\Omega_t$ is not observed, so this is a population-level identity, which is why it's a 'proxy' requiring additional assumptions"*).
- **Regime A wording: tighten "action variation" → "identifiable intervention."** Same concern as in `#der-loop-interventional-access`: "the agent varies its actions" is not sufficient for clean estimates under policy-driven action choice; Regime A needs randomization / known-mechanism / sequential-ignorability + positivity (Codex/Claude, AUDIT-WORKING-526815). *(Overlaps the do-vs-conditioning concern — see off-ramp note in the lift report.)*
- **Consistency nit:** the opening prose says CIY "can be approximated from observational data" while the Discussion says the proxy "is not an approximation of canonical CIY" — settle on "a separate diagnostic proxy that correlates under favorable conditions (Regime A)" throughout (Codex/Claude, AUDIT-WORKING-526815).
- **TF-08 lineage artifact + topological-sort note.** A residual "TF-08" annotation was flagged for removal; separately, the proxy depends on `#def-causal-information-yield`, which appears *after* this segment in some OUTLINE walks — the proxy is read before the canonical object it proxies (Gemini, AUDIT-WORKING-829314). Worth confirming the OUTLINE ordering reads cleanly.

#### 4. Readers often ask / wonder

- **What is the exact form of the weighting factor $\lambda$ — does it fall out of an information-bottleneck constraint or is it purely heuristic?** A natural question raised at the boundary into `#disc-ciy-unified-objective`, where the answer (the survival-imperative shadow price) lives (Claude, AUDIT-WORKING-849201).

#### 5. Candidate figures

- **Two-quantity-plus-three-regime diagram.** Draw canonical CIY (interventional, non-negative) and proxy CIY (observational, sign-indefinite) as *separate* quantities — not one quantity with noise — then place the three regimes under them: Regime A can estimate canonical CIY if assignment is randomized/ignorable; Regime B uses assumptions/adjustment; Regime C avoids CIY-in-policy-optimization. *"This captures the segment's main safety lesson"* (Codex/Claude, AUDIT-WORKING-526815, has a rendered draft).

#### Belongs elsewhere

- The five-domain $\lambda$ mapping and the survival-imperative drive belong with `#disc-ciy-unified-objective`; the regret-bound / Bretagnolle-Huber material with `#deriv-strategy-cost-regret-bound`. Auditors picked these up while reading the proxy segment but they are downstream content.
