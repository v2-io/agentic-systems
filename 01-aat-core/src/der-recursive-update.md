---
slug: der-recursive-update
type: derived
status: exact
depends:
  - form-agent-model
  - form-event-driven-dynamics
  - deriv-recursive-update
stage: claims-verified
---

# Derived: Recursive Update

The first major *derived* result of the volume: the model update function must be recursive. Each new model state $M_{\tau^+}$ depends only on the previous model state $M_{\tau^-}$ and the incoming event $e_\tau$ — not on the full chronica. The result follows from three constraints already in place: the temporal-ordering postulate ( #post-causal-structure — the model at time $t$ can only depend on prior events), the partial-observability scope ( #def-observation-function — the agent has no direct access to the environment beyond events), and the completeness commitment in the model formulation ( #form-agent-model — $M_t$ summarizes everything the agent retains). Together these force the update into the recursive form; the appendix derivation ( #deriv-recursive-update) works through seven counterexample attacks to confirm there is no escape from this form once the three constraints are accepted.

The epistemic character of this result is honest. Temporal ordering is a physical postulate and partial observability is a scope condition, but the completeness commitment is *definitional* — it cannot be "violated" because any apparent violation is absorbed by expanding $M_t$. The Markov structure of the update is therefore not discovered in the environment but chosen through the definition of $M_t$ as complete. This is not a weakness; it is the precise character of the claim. For finite agents recursion is forced by *computational realism* as well: re-processing the full history at each event is infeasible.

The formulation also surfaces **between-event dynamics** — autonomous evolution of the model state during the gaps between observation arrivals — as load-bearing rather than filler. These include prediction generation (anticipating the next observation), uncertainty growth (confidence decay over time without new data), and internal reorganization (consolidation, abstraction). When between-event dynamics are driven by replayed or internally-generated pseudo-events and the objective is information-bottleneck-gap reduction rather than one-step mismatch minimization, the framework names this the *consolidation regime* ( #form-consolidation-dynamics) — a separate operating mode with its own scope condition ($\nu_{\text{consol}} \ll \nu_{\text{online}}$) and its own necessity condition.

## Formal Expression

*[Derived (recursive-update, from temporal postulate and $M_t$ completeness)]*

**Event-driven update:**

$$M_{\tau^+} = f_M(M_{\tau^-}, e_\tau)$$

where:
- $M_{\tau^-}$ is the model state immediately before event $e_\tau$
- $M_{\tau^+}$ is the model state immediately after
- $f_M$ is the update function — it takes the current model and the new event, not the full history $\mathcal{C}_t$

**Between-event evolution:**

$$\frac{dM}{d\tau} = g_M(M_\tau)$$

Between events, the model evolves autonomously — internal reorganization, prediction generation, decay of transient states. The between-event dynamics depend only on the current model state, not on external input (which, by definition, arrives only at events).

## Epistemic Status

*Exact, with a partly definitional character.* The result follows from three constraints: temporal ordering (C1 — physical law), partial observability (C2 — scope definition), and state completeness (C3 — analytical commitment that $M_t$ summarizes everything the agent retains). C1 and C2 do genuine eliminative work; C3 is definitional — it cannot be "violated" because any violation is absorbed by expanding $M_t$. The Markov structure is therefore not discovered in the environment but chosen through the definition of $M_t$ as complete. This is not a weakness — it is the nature of the claim: recursive update is the only form consistent with C1 + C2 + the definition of $M_t$ as complete (see #deriv-recursive-update for the full argument and seven counterexample attacks). For finite agents, recursion is also *computational necessity*: re-processing the full history at each event is infeasible.

## Discussion

**Recursion as a consequence of completeness.** The recursive form is not an assumption bolted on — it follows from the definition of $M_t$ as complete. If $M_t$ were incomplete (if some relevant information lived outside $M_t$ in the raw history), then $f_M(M_{\tau^-}, e_\tau)$ would be insufficient and the agent would need to consult $\mathcal{C}_t$ directly. The sufficiency of the recursive form is precisely what #def-model-sufficiency measures: when $S(M_t) = 1$, the recursive update loses nothing.

**Between-event dynamics matter.** The autonomous evolution $g_M(M_\tau)$ is not merely filler between observations. It includes prediction generation (what the agent expects to see next), uncertainty growth (model confidence decaying over time without new data), and internal reorganization (consolidation, abstraction). In event-driven systems ( #form-event-driven-dynamics), the between-event interval is variable, making $g_M$ load-bearing for agents that must act or predict between observations. When the between-event dynamics are driven by replayed or internally-generated pseudo-events and the update objective is IB-gap reduction rather than one-step mismatch minimization, $g_M$ is operating in the *consolidation regime* per #form-consolidation-dynamics — a named regime with its own scope condition ($\nu_{\text{consol}} \ll \nu_{\text{online}}$) and its own necessity condition (sub-state factorization + bounded per-event budget). Consolidation is where the stability-plasticity feasibility window complements #schema-strategy-persistence's plasticity lower bound.

**Connection to the update gain.** The event-driven update $f_M(M_{\tau^-}, e_\tau)$ is where the gain principle ( #emp-update-gain) operates: $\eta^\ast$ determines how strongly $e_\tau$ shifts $M_t$ away from its prior value. The recursive form makes the gain's role explicit — it modulates the single-step correction.

## Working Notes

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical/generative material, kept separate from certified theory-fix findings (handled elsewhere). **Coverage:** 9 of the 14 contributing audit dirs reached a digested reflection on this segment (384279, 471203, 526815, 527914, 584721, 742613, 773921, 829314, 849201) plus the batched 963715 (14–18 batch) and 451729 (batch-03/04); 193847, 266847, 361742, 472913, 613842 did not file a dedicated note here. Substrate attribution inferred from voice where not explicit.

#### Candidate Brief prose / pre-prose

- **"Markov is a modeling choice about the boundary of the agent's memory, not an assumption about the physics of the universe."** The cleanest plain-language statement of the segment's distinctive move — the Markov property of $M_t$ is *forced by what we mean by $M_t$* (completeness), inverting the usual "assume the environment is Markov" framing (Claude, AUDIT-WORKING-773921; Claude, AUDIT-WORKING-471203 — "AAT *derives* recursive update from completeness where most frameworks *postulate* it").
- The hybrid-system one-liner: the update splits into "instantaneous event-driven jumps ($f_M$)" and "continuous autonomous drift / consolidation ($g_M$)" — a jump-diffusion / hybrid dynamical system (Claude, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-849201; Claude, AUDIT-WORKING-773921).

#### Candidate Discussion

- **The hippocampal-neocortical / experience-replay convergence — the standout reach on this segment.** If $g_M$ is consolidation (replaying recent events to integrate them deeper) but $f_M$ + the IB compression discards raw events, then $M_t$ must carry internal structure: a fast high-fidelity buffer that $f_M$ appends to, drained slowly by $g_M$ into a compressed semantic model. "This is exactly the hippocampal-neocortical complementary learning systems theory from mammalian neuroscience — and the structure of Experience Replay in Deep RL. The framework elegantly *forces* this bipartite memory architecture just through the math of continuous-vs-discrete updates combined with the IB constraint; the 'stability-plasticity feasibility window' is precisely the tension between these two systems" (Claude, AUDIT-WORKING-829314). Candidate Discussion paragraph (mark discussion-grade; verify the CLS isomorphism before promoting past it).
- **The "physicist's system-boundary trick" framing of C3.** "C3 is definitional — any violation is absorbed by expanding $M_t$" is the same move as a physicist defining the system boundary so conservation laws hold (if energy isn't conserved, you missed a particle; if Markov fails, the state space was too small). Makes the math tautological-but-useful: the real empirical work is figuring out *what $M_t$ actually contains* for a given agent, not proving the equation (Claude, AUDIT-WORKING-829314; converging framing at Claude, AUDIT-WORKING-471203 "Markov-by-construction," and the control-theory state-space-representation-theorem analogy at 451729 batch-03 — "tells you the representation is always possible, not whether it is tractable").

#### Follow-up items

- **Status-label drift: frontmatter `conditional` vs body "Exact, with a partly definitional character."** Flagged by nearly every substrate that read the segment closely (Codex/Claude, AUDIT-WORKING-384279; Claude, AUDIT-WORKING-471203; Codex/Claude, AUDIT-WORKING-526815; Codex/Claude, AUDIT-WORKING-527914; Claude, AUDIT-WORKING-584721; Claude, AUDIT-WORKING-742613). Consensus: the C1/C2/C3 constraints are *framework-internal commitments* (not external conditions that might not hold), so the result is exact *within the framework* and "conditional" is a slight underclaim. Candidate: align the two — either frontmatter $\to$ `exact` with conditional-on-C1+C2+C3 noted in prose, or prose $\to$ explicitly "conditional under framework-internal commitments." Editorial; recurs strongly enough to be the segment's top follow-up.
- **The "two terms in 'completeness'" naming seed.** "Completeness" bundles two distinct properties: (i) $M_t$ retains all predictively-relevant history (a *sufficiency* claim), and (ii) behavior depends only on $M_t$, not $\mathcal{C}_t$ directly (a *Markov-of-policy* claim). Candidate split into "predictive completeness" (i) and "behavioral completeness" (ii) (Claude, AUDIT-WORKING-471203) — terminology workflow.
- **Between-event dynamics $g_M$ left very open.** Several note that $g_M(M_\tau)$ ("depends only on current model state") deserves more formal treatment — what *is* its mathematical form? — and that the consolidation paragraph imports downstream concepts (`#form-consolidation-dynamics`, `#schema-strategy-persistence`) dense for an early derived segment; one suggests splitting it into a short forward pointer (Codex/Claude, AUDIT-WORKING-526815; Claude, AUDIT-WORKING-742613; 451729 batch-03).

#### Readers often ask / wonder

- "The Epistemic Status promises seven counterexample attacks in `#deriv-recursive-update` — are they rigorous or straw men?" The single most-recurring reader want; multiple substrates jumped to the appendix to check (Claude, AUDIT-WORKING-773921; Claude, AUDIT-WORKING-471203; Claude, AUDIT-WORKING-849201; 451729 batch-04 confirmed them "thorough and honest," with Attack 2 on continuous coupling correctly labeled a genuine limitation rather than hand-waved).
- "If $g_M$ is consolidation/replay, does AAT formally *mandate* a bipartite (short-term buffer + compressed semantic) memory structure?" (Claude, AUDIT-WORKING-829314).
- "What dictates the *right* $M_t$? Recursion is guaranteed by definition, but the *content* of $M_t$ is what the IB objective optimizes" — the two segments are complementary: this one fixes the *form* of the update, `#form-information-bottleneck` fixes what it should *retain* (451729 batch-03 wandering).

#### Candidate figures

- **A compression-boundary diagram** (not a generic loop): full chronica feeds the current complete model once; thereafter the next event only touches the model state, with a *dashed forbidden edge* from raw chronica to the update — if that edge is ever real, the information belongs inside $M_t$ (the counterexample case made visible) (Codex/Claude, AUDIT-WORKING-526815).

#### Belongs elsewhere

- **Consolidation as "why agents need to sleep/think."** The internally-generated-pseudo-event consolidation regime "sounds exactly like human sleep or an LLM spending compute on 'thinking tokens' before answering — a formal reason why agents need to think/sleep" (Claude, AUDIT-WORKING-773921; Claude, AUDIT-WORKING-829314 develops the TST reading: $g_M$ = "the developer thinking about architecture in the shower, or a team retrospective consolidating scattered understanding"). The substantive treatment belongs with `#form-consolidation-dynamics`; preserved here as the reach that recurred on this segment.
