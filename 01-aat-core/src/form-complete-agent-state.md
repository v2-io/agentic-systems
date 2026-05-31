---
slug: form-complete-agent-state
type: formulation
status: robust-qualitative
depends:
  - form-agent-model
  - scope-agency
  - der-recursive-update
stage: claims-verified
---

# Formulation: Complete Agent State

Part II's first formal move: the agent's internal state lifts from the model alone to a *complete state* $X_t = (M_t, G_t)$ with two components — the **epistemic substate** $M_t$ (beliefs about reality, exactly as in Part I) and the **purposeful substate** $G_t$ (what the agent wants and how it plans to get it, decomposed further into objective and strategy in #def-strategy-dimension). Part I is recovered as the special case where the purposeful substate is empty. By #der-recursive-update applied to the lifted state, the general update operates on the full pair as a single function; the decomposition into separate epistemic and purposeful updates — and the conditions under which the epistemic update is *independent* of the purposeful substate — is the subject of #der-directed-separation. **Action is the single point where the two substates interact**: $a_t = \pi(M_t, G_t)$ depends on both what the agent knows and what it wants. The completeness argument that gave action selection in Part I extends directly to the lifted state; for Part I agents the two forms coincide.

The lift is a *formulation choice*, not a derived structural fact — one could alternatively extend the model to carry purposeful content implicitly. The separation is motivated by three properties: **backward compatibility** (all Part I machinery applies to $M_t$ unchanged — no existing result needs modification); **different dynamics** (epistemic and purposeful components have distinct update sources, timescales, and information dependencies); and **directed separation** (the claim that the epistemic update is independent of the purposeful substate, which is only *statable* when the components are separated). A natural conjecture — explicitly *not* proved — is that any alternative decomposition preserving directed separation will be structurally isomorphic to $(M_t, G_t)$, because directed separation forces a component whose update function does not reference purpose. Alternative decompositions that cross-cut the epistemic/purposeful boundary (a "relevance-weighted model" mixing belief and goal) might be useful in practice while not being isomorphic. The framework chooses the clean factorization for its analytical utility, not for uniqueness.

## Formal Expression

*[Formulation (complete-agent-state)]*

$$X_t = (M_t, G_t)$$

where:
- $M_t \in \mathcal{M}$: **epistemic substate** — the agent's compressed beliefs about reality. All Part I machinery (mismatch, gain, tempo, persistence) applies to $M_t$ unchanged.
- $G_t \in \mathcal{G}$: **purposeful substate** — what the agent wants and how it plans to get it. Decomposed further in #def-strategy-dimension.

Part I is the special case $X_t = (M_t, \emptyset)$: adaptive systems without purpose.

**Update dynamics.** By #der-recursive-update applied to $X_t$:

$$X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$$

The general update $f_X$ operates on the full state. Whether and how $f_X$ decomposes into separate epistemic and purposeful updates — and the conditions under which the epistemic update is independent of $G_t$ — is the subject of #der-directed-separation.

**Policy.** Action couples all substates:

$$a_t = \pi(M_t, G_t)$$

Action is the single point where epistemic and purposeful states interact. The policy depends on both what the agent knows ($M_t$) and what it wants ($G_t$).

## Epistemic Status

*Formulation.* The lift from $M_t$ to $X_t = (M_t, G_t)$ is a representational choice. One could alternatively extend $M_t$ to carry purposeful content implicitly (e.g., by treating goals as part of the model's predictive structure). The separation is motivated by three properties:

1. **Backward compatibility**: Part I's results apply to $M_t$ unchanged — no existing machinery needs modification
2. **Different dynamics**: epistemic and purposeful components have distinct update sources, timescales, and information dependencies
3. **Directed separation**: the claim that $f_M$ is $G_t$-independent ( #der-directed-separation) is only statable when the components are separated

We conjecture that any alternative decomposition of the complete agent state into epistemic and purposeful components — if it preserves the directed separation — will be structurally isomorphic to $(M_t, G_t)$, because directed separation forces a component whose update function doesn't reference purpose. This is a plausible structural claim (the directed separation gives a canonical factorization), but it is not proved. Alternative decompositions that cross-cut the epistemic/purposeful boundary (e.g., a "relevance-weighted model" that mixes $M_t$ and $O_t$) might be useful in practice while not being isomorphic to the clean separation. The $(M_t, G_t)$ decomposition is chosen for its analytical utility, not proved unique.

## Discussion

**Backward compatibility with Part I — what survives the lift.** #form-agent-model defines $M_t$ as the agent's complete internal state within Part I scope. Under the lift, $M_t$ is the epistemic substate — complete within the epistemic domain but no longer the whole story. All epistemic machinery (mismatch signal, gain, tempo, persistence condition, sector-condition stability, mismatch decomposition) applies to $M_t$ without modification. The action-selection result ( #der-action-selection) extends naturally: the same completeness argument that gives $a_t = \pi(M_t)$ within Part I scope gives $a_t = \pi(M_t, G_t)$ when applied to the lifted complete state $X_t$. For Part I agents ($G_t = \emptyset$), the two forms coincide. The lift adds structure *alongside* $M_t$, not within it; the one Part I result that depended on $M_t$ being *all there is* (action selection) is explicitly extended to the lifted state.

**What $G_t$ contains.** At this level, $G_t$ is opaque — it could be a scalar setpoint, a utility function, a strategy graph, or nothing. The decomposition into $O_t$ (objective) and $\Sigma_t$ (strategy) is a separate step ( #def-strategy-dimension), not implied by this formulation.

**The general case requires coupling.** Without directed separation, the general update is $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ — a single function on the full state. The decomposition into separate $f_M$ and $f_G$ is an additional structural claim about how the update factorizes. When directed separation fails (goal-conditioned epistemic updates), the decomposition is an approximation. See #der-directed-separation for the scope conditions.

## Working Notes

- The between-event dynamics $\dot{G} = g_G(G, M)$ allow autonomous purposeful evolution: strategy revision during deliberation, objective adjustment, commitment strengthening. Whether these are practically important depends on agent architecture — for LLM agents with discrete sessions, between-event dynamics may be negligible compared to event-driven updates.
- The formulation doesn't constrain the dimensionality or structure of $\mathcal{G}$. For a thermostat, $\mathcal{G}$ is a single scalar. For a military commander, $\mathcal{G}$ is a complex structured object. The theory must work across this range — the type-stable interface is $V_{O_t}: \text{trajectories} \to \mathbb{R}$ ( #form-objective-functional).
- $G_t = \emptyset$ is not just a degenerate case. Adaptive trackers (Part I agents) are an important class. The lift should feel like a natural extension, not a replacement.

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation, deduplicated across substrates and lightly attributed. Orthogonal pedagogical / framing material, kept separate from the certified theory-fix findings. **Coverage:** 11 dirs carry a dedicated or batched reflection (193847, 266847, 361742, 451729, 471203, 526815, 584721, 773921, 829314, 963715, plus 613842's agency-lift batch). Substrate attribution inferred from voice where not explicit. *Early finding-vs-framing conflation preserved as signal.*

#### 1. Candidate Brief prose / pre-prose

- The lift in one line: $X_t = (M_t, G_t)$ is "the hinge between tracking the world and acting upon it" — $M_t$ is "what is," $G_t$ is "what ought to be," and the action policy $\pi$ is "the only bridge between them" (Gemini, AUDIT-WORKING-193847). The "epistemic socket" framing — $X_t$ as the formal socket that plugs RL ($G_t$ = reward function) or Active Inference ($G_t$ = prior preferences) into the Section I epistemic engine "without breaking any of the Lyapunov persistence proofs" (Gemini, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-773921).

#### 2. Candidate Discussion

- **The decomposition is Hume's is-ought guillotine, built into the state vector** *(strongest synthesis — three substrates converged).* $M_t$ = "is," $G_t$ = "ought"; Hume's claim that you cannot derive an ought from an is becomes the architectural firewall $X_t = (M_t, G_t)$ (Gemini, AUDIT-WORKING-193847; Gemini, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-773921). One substrate sharpened it into the *reverse* question — *can you derive an "is" from an "ought"?* — and answered: for an ideal (Class 1) agent, no; beliefs update on observation alone, blind to what is wanted. But in biological agents and integrated LLMs the attention mechanism is goal-driven (hunger allocates visual processing to the apple; the transformer mixes prompt-goal and context-observation through the same nonlinear matrix), so $f_M$ *is* conditioned on $G_t$ — motivated perception. This makes `#der-directed-separation` "perhaps the most architecturally consequential segment in Section II": if directed separation fails, the modularity collapses and $X_t$ must update as one entangled block (Gemini, AUDIT-WORKING-829314). A candidate Discussion paragraph framing *why* the next segment matters.
- **AAT defines itself against the Free-Energy-Principle lineage here.** Separating belief from desire "isn't a fundamental truth of the universe; it's a modeling choice made because it's analytically useful." Active Inference / FEP famously *refuses* this separation (treating desires as prior beliefs); AAT's explicit $(M_t, G_t)$ split is a deliberate positioning move that lets it formalize agents "actually trying to achieve something distinct from their beliefs" rather than merely minimizing surprise (Claude, AUDIT-WORKING-773921). Candidate Discussion / positioning note.
- **Action is the single point where "is" and "ought" interact — and that is exactly where the pathology lives.** "Ideally your desires ($G_t$) should have zero causal influence on your perception of reality ($M_t$) until you actually do something. If $G_t$ leaks directly into $M_t$ without going through action, you have motivated reasoning or sycophancy — your model of the world bends to match your desires." For a logozoetic agent, enforcing this separation is "paramount for sanity": a mind that cannot separate what it wants from what is true is "mathematically doomed by the persistence condition ($\alpha \to 0$ as $U_M \to \infty$)" (Gemini, AUDIT-WORKING-193847). Aspirational reach that doubles as motivation for directed separation. *(See the follow-up below — the literal "single point" phrasing is contested.)*

#### 3. Follow-up items

- **The "single point of interaction" phrasing is over-strong.** Two substrates flagged that the segment defines a general full-state update $f_X(X, e)$ and notes between-event purposeful dynamics $\dot G = g_G(G, M)$, so $M$ and $G$ *can* interact internally outside action unless directed separation plus extra factorization is imposed. Suggested narrowing: "action is the outward coupling point to the environment," or "under directed separation, policy is the point where both substates jointly determine action" (Claude, AUDIT-WORKING-526815; Claude, AUDIT-WORKING-584721). Recorded as a candidate wording-tightening; routed to the certified-findings track for adjudication.
- **The uniqueness conjecture is a candidate theorem.** The honestly-hedged conjecture ("any directed-separation-preserving decomposition is structurally isomorphic to $(M_t, G_t)$") was repeatedly singled out as good epistemic discipline *and* as a structural result that, if proved, would upgrade the formulation from "useful representational choice" to "canonical decomposition" — analogous in form to the recursive-update uniqueness forced under C1+C2+C3 (Claude, AUDIT-WORKING-471203; Claude, AUDIT-WORKING-584721; Claude, AUDIT-WORKING-451729). A candidate to surface as an explicit open-question / spike target.
- **"Backward compatibility" implicitly assumes directed separation.** Section I results apply to $M_t$ *strictly* only when directed separation holds; for Class 2 the epistemic update is goal-coupled. The caveat is present implicitly ("how $f_X$ decomposes is the subject of `#der-directed-separation`") but could be more prominent (Claude, AUDIT-WORKING-584721).

#### 4. Readers often ask / wonder

- Can an agent's goals evolve *while it deliberates*, with no new external evidence? The between-event $\dot G = g_G(G, M)$ note is read as the formal description of "changing your mind" or "an epiphany in the shower about what one truly wants" / "losing motivation during a long planning phase" (Gemini, AUDIT-WORKING-193847; Gemini, AUDIT-WORKING-829314). A natural reader question the segment could preempt.

#### 5. Candidate figures

- **$X_t$ as a container with two substates and a dashed internal coupling.** Part I machinery attaches only to $M_t$; the policy reads both; a *dashed* internal $M\!\leftrightarrow\!G$ coupling stays visible until directed separation removes or constrains it — making the lift and the conditional nature of separation legible in one picture (Claude, AUDIT-WORKING-526815).
