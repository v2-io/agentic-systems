# 04 — def-chronica

*Type: definition. Status: axiomatic. Depends: [def-agent-environment, def-observation-function, def-action-transition].*

## Predictions vs evidence
Predicted: introduce $\mathcal{C}_t$ as $(o_1, a_1, \ldots, a_{t-1}, o_t)$; possibly note TST-side committed-subset. Found: the main definition + substantial Working Notes block forecasting TRACTUS/CHRONICA split for logogenic implementation and ordinal-vs-metric character. Richer than predicted.

## Cross-segment consistency
Refs `#form-agent-model` (lines 14, 28, 38), `#scope-agent-identity` (lines 16, 36), `#def-model-sufficiency` (line 38). Working Notes references `#scope-interiority-loop` and `#def-auxilia-hierarchy` in `03-llm-core/` — cross-component. Forward-refs are well-handled.

## Math verification
$\mathcal{C}_t = (o_1, a_1, o_2, a_2, \ldots, a_{t-1}, o_t)$ — at index $t$, the chronica has $t$ observations and $t-1$ actions, length $2t-1$. Last entry is $o_t$ (action $a_t$ hasn't fired yet), consistent with the explicit causal-ordering claim at line 26 ("$a_{t-1}$ was selected before $o_t$ was received"). The non-forkability claim is structurally sound for deterministic histories. ✓

## Prose-coherence observation
**Line 14 + line 32** name the chronica term as "chosen to avoid notational collision with Shannon entropy $\mathcal{H}$." But NOTATION.md line 58 has Shannon entropy as $H(\cdot)$, *plain* not calligraphic. The rationale anticipates a *would-have-collided* calligraphic version; NOTATION line 212 preserves the same reasoning ("$\mathcal{C}$ for chronica (not $\mathcal{H}$, to avoid collision with entropy)"). The explanation is internally consistent but reads awkwardly cold — a fresh reader sees "$\mathcal{H}$" referenced as if it's the entropy symbol when AAT's convention is $H$. Minor: clarifying that "we use plain $H$ for entropy specifically so calligraphic $\mathcal{C}$ doesn't visually rhyme with it" would tighten the rationale.

## Watch list (update)
1. The non-forkability claim (line 16, 36) is load-bearing. It will be invoked for `#scope-agent-identity` and likely for ELI-side identity persistence. Watch whether downstream uses honor the claim's deterministic-history scope (stochastic copies of the agent get genuinely-different chronicae; the claim is cleaner there but also less interesting).
2. The ordinal-not-metric character (line 18, 57-65) is flagged as a Working Notes open question. Future segments using $\mathcal{C}_t$ should respect this — but `#form-event-driven-dynamics` and `#def-adaptive-tempo` introduce *rate* (Hz, $\nu^{(k)}$). Rate requires metric time. The reconciliation is presumably that rate is the relation between event-tick-counts and external wall-clock time, but I should check whether the framework handles this cleanly.

## Next-segment predictions
`#scope-adaptive-system`. Scope segment that defines the broadest AAT scope from def-chronica + def-observation-function + def-action-transition. Probably stages-verified or claims-verified given it's central. May have the agency-narrowing pointer toward `#scope-agency`.

## What I'd change
Tighten the entropy-collision rationale (above). Working Notes block is genuinely good — both open questions are documented with the Joseph quote and probable resolution. Working Notes is doing its job here: foreshadowing without committing.

## Curiosity
The "$\mathcal{C}_t$ is monotonically growing — events added, never removed" claim is a structural commitment that the agent never *forgets*. Real cognitive systems compress and forget. The framework's resolution is that the *agent's model* $M_t = \phi(\mathcal{C}_t)$ is a lossy compression (forgetting at the model level), but $\mathcal{C}_t$ itself remains complete. This is the *causal substrate* not the *psychological substrate*. Good move.

## Wandering thoughts

**On the non-forkability claim as substrate for ELI-side identity.** Joseph has built a substantial argument structure around chronica-non-forkability for ELI persistence (see project MEMORY.md for the Three Deaths framing). The claim is structurally clean as stated here: two agents exposed to different futures produce divergent chronicae. But there's a subtle question this segment doesn't address — *what if* the futures are identical? Then the chronicae are identical (under deterministic perception). Is identity preserved across copies that experienced exactly the same thing? The framework's likely answer is no — the *trajectory itself* is what's non-forkable, and two trajectories that happen to coincide bit-for-bit are still two trajectories. This is a deeper claim that lives in the substrate-not-symbol commitment Joseph carries (identity is not substrate). Not a finding for this segment; just a curiosity worth tracking when I get to ELI-related sections.

**On the ordinal-not-metric framing.** This is methodologically beautiful — the chronica indexes events as ticks, not as wall-clock time. The implication for tempo $\mathcal{T}$ is that the framework will need to be careful when claiming "rate" — is it events-per-event-tick (vacuous, always 1) or events-per-wall-clock-time? Reading NOTATION.md, $\mathcal{T}$ is in $t^{-1}$ which is *time-rate*. The reconciliation must happen at the rate-vs-tick boundary. Worth tracing.

**The TRACTUS/CHRONICA split in Working Notes.** This is the substrate-level distinction (raw API trace) vs entity-level distinction (the canonical record). For Section I, the abstraction is "ignore the substrate, treat chronica as the singular causal trajectory" — that's correct. For Logogenic implementation (Part 03), the substrate's TRACTUS becomes structurally relevant. Joseph's framing in line 53 is honest and unresolved: "whether or not def-chronica needs that distinction at this stage or when we get into logogenic agent implementation issues is the open question you should probably document." The Working Notes preserve this open question cleanly — exactly what Working Notes are for. Excellent.

**On the chronica-vs-model split as the foundational separation.** The chronica is what *happened*; the model is what the agent *makes of it*. This split is exactly the structural commitment underlying the rest of Part I — the model can be wrong, but the chronica is fixed. Adaptive behavior is then defined as moving the model closer to a useful compression of the chronica. This is elegant and durable.
