---
slug: form-event-driven-dynamics
type: formulation
status: robust-qualitative
depends:
  - post-causal-structure
  - def-observation-function
  - def-action-transition
  - form-agent-model
stage: deps-verified
---

# Formulation: Event-Driven Dynamics

The agent-environment interaction is formulated at a finer grain than discrete clock ticks: as a stream of atomic **events** — observation arrivals and action completions — at potentially variable and heterogeneous rates across multiple channels. Discrete-time notation, where a single observation and a single action alternate at a fixed rate, becomes the special case of uniform-interval events on a single channel. The motivation is realism: real agents face multiple observation channels at different rates (a robot's camera at $30\text{Hz}$, LIDAR at $10\text{Hz}$, GPS at $1\text{Hz}$; a human's vision, audition, proprioception; a developer's compiler output, test results, and production telemetry), multiple action channels with different latencies, and asynchronous arrivals. The event-driven formulation handles all of these natively.

Two new measurable quantities are introduced alongside the event stream. **Event information content** $\mathcal{I}(e_\tau)$ measures, for any individual event, the mutual information it carries about the environment state conditioned on the agent's current model — an event the model already predicts carries little information; an event that surprises the model carries much. This anticipates the mismatch signal ( #def-mismatch-signal). **Channel-specific observation uncertainty** $U_o^{(k)}$ measures the noise characteristic of each channel separately — a noisy channel provides lower-quality information per event, and any sensible update rule must weight channels accordingly. From these the chapter's *effective adaptation rate* falls out immediately as the sum across channels of channel-rate times optimal gain — the adaptive tempo construct ( #def-adaptive-tempo) that the framework will lift to first-class status, presented here as the natural multi-channel generalization the discrete-time formulation cannot easily express.

## Formal Expression

*[Formulation (event-driven-dynamics)]*

**Event** ($e$): An atomic unit of agent-environment interaction, typed as:
- **Observation event**: $e = (\text{obs}, k, o^{(k)})$ — a datum arriving on observation channel $k$
- **Action completion**: $e = (\text{act}, j, r^{(j)})$ — the result of action $j$ completing

**Event stream** ($\mathcal{E}$): The temporally ordered sequence of all events:

$$\mathcal{E} = \{(e_1, \tau_1), (e_2, \tau_2), \ldots\} \quad \text{where } \tau_1 \leq \tau_2 \leq \cdots$$

**Channel rate** ($\nu^{(k)}$): The characteristic event rate of channel $k$, which may vary over time.

**Event information content**: The mutual information between the event and the environment state, conditioned on the current model:

*[Definition (event-information-content)]*

$$\mathcal{I}(e_\tau) = I(e_\tau;\, \Omega_\tau \mid M_{\tau^-})$$

An event that the model already predicts carries little information ($\mathcal{I} \approx 0$). An event that surprises the model carries much ($\mathcal{I} \gg 0$). This connects directly to the mismatch signal ( #def-mismatch-signal).

**Channel-specific observation uncertainty**:

*[Definition (channel-uncertainty)]*

$$U_o^{(k)} = \text{observation uncertainty of channel } k$$

Different channels have different noise characteristics. A noisy channel (high $U_o^{(k)}$) provides lower-quality information per event. The update gain ( #emp-update-gain) should weight channels accordingly.

## Epistemic Status

This is a *formulation choice*, not a postulate. The event-driven representation extends #post-causal-structure's recursive update to heterogeneous, asynchronous multi-channel interactions. The discrete-time form ($M_t = f(M_{t-1}, o_t, a_{t-1})$) from #der-recursive-update is a special case sufficient for many formal analyses — the event-driven formulation is needed only when multi-rate or asynchronous channels matter.

## Discussion

**Why events rather than clock ticks.** The discrete-time notation $M_t = f(M_{t-1}, o_t, a_{t-1})$ presupposes a single clock synchronizing observations and actions. Real agents face:

- **Multiple observation channels** at different rates (a robot's camera at 30Hz, LIDAR at 10Hz, GPS at 1Hz; a human's vision, audition, proprioception; a developer's compiler output, test results, and production telemetry)
- **Multiple action channels** with different latencies (a robot's wheel motors vs. arm actuators; an organization's operational decisions vs. strategic pivots)
- **Asynchronous arrival** — observations not synchronized with each other or with action completions

The event-driven formulation handles all of these naturally. The discrete-time form is the special case where a single observation and a single action alternate at a fixed rate.

**The effective adaptation rate.** The agent's overall capacity to track environmental changes is the sum of information gained across all channels per unit time:

$$\nu_{\text{eff}} = \sum_k \nu^{(k)} \cdot \eta^{(k)*}$$

This quantity — identical to adaptive tempo $\mathcal{T}$ ( #def-adaptive-tempo) — is the central measure of an agent's adaptive fitness.

**Software-specific channels.** In the software development domain, the event-driven formulation maps naturally to the developer's multi-rate observation channels:

| Channel $k$ | Rate $\nu^{(k)}$ | Noise $U_o^{(k)}$ |
|-------------|------------------|-------------------|
| Compiler/linter output | Per-save (high) | Very low |
| Unit test results | Per-run (medium) | Low |
| CI pipeline | Per-push (medium) | Low |
| Runtime telemetry | Continuous (variable) | Medium |
| Bug reports | Sporadic (low) | High |
| Code review feedback | Per-PR (low) | Medium-high |

The three-part tempo decomposition for software — $\mathcal T_{\text{obs}}$ (compiler, tests) + $\mathcal T_{\text{explore}}$ (code reading) + $\mathcal T_{\text{probe}}$ (test runs, staging) — is a direct application of multi-channel tempo. The formal development of this decomposition is a TST-side question (open GAP in `02-tst-core/OUTLINE.md`).

## Working Notes

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical/generative material, kept separate from certified theory-fix findings (handled elsewhere). **Coverage:** 12 of the 14 contributing audit dirs reached a digested reflection on this segment (193847, 266847, 384279, 471203, 472913, 526815, 527914, 584721, 742613, 773921, 829314, 849201) plus the batched 963715 (14–18 batch) and 451729 (batch-03); 361742 and 613842 did not file a dedicated note here. Substrate attribution inferred from voice where not explicit.

#### Candidate Brief prose / pre-prose

- **Event-information-content as the formal definition of "surprise" / "boredom."** Independently the most-praised pedagogy across substrates: $\mathcal{I}(e_\tau) = I(e_\tau; \Omega_\tau \mid M_{\tau^-})$ reads as "how much does this event tell me about the world, given what my model already knows?" — zero if perfectly predicted (Claude, AUDIT-WORKING-773921; Claude, AUDIT-WORKING-829314 — "a perfect mathematical definition of boredom and surprise … we only process the delta between prediction and sensory input"; Claude, AUDIT-WORKING-849201; Claude, AUDIT-WORKING-266847 — "surprise and mismatch are the same phenomenon viewed from two angles" via 963715's batch). Strong Feynman-criterion Brief seed.
- **"You cannot increase tempo by getting faster sensors OR by trusting them more"** — the $\nu_{\text{eff}} = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$ formula as the two-lever framing: speed ($\nu$) and quality ($\eta^\ast$) compound (Claude, AUDIT-WORKING-849201).

#### Candidate Discussion

- **The software-channels table is the segment's standout concrete anchor** — multiple substrates flagged it as the move that makes the abstraction land ("a stunningly effective way to ground the abstraction," Claude, AUDIT-WORKING-193847; "compiler vs CI vs telemetry — exactly the concrete anchoring this abstract theory needs," Claude, AUDIT-WORKING-773921; Codex/Claude, AUDIT-WORKING-527914). Candidate for promotion as the chapter's worked-example anchor.
- **The shoshin convergence.** The event-driven (not turn-based) commitment matches `~/src/shoshin`'s "key early finding: the cycle is naturally event-driven not turn-based" — latency and bandwidth become first-class theoretical objects; a high-bandwidth/high-latency channel (code review) lets $M_t$ drift between updates, a low-bandwidth/low-latency channel (linter) keeps $M_t$ tightly coupled along a narrow dimension (Claude, AUDIT-WORKING-829314).
- **Attention-as-channel-budget-allocation.** If the agent has a finite compute budget to process events, it must allocate across channels (high-noise/high-rate compiler warnings vs low-noise/low-rate integration tests); optimal allocation maximizes $\nu_{\text{eff}}$ (Claude, AUDIT-WORKING-829314). A discussion-grade reach toward an attention formalism, not derived here.

#### Follow-up items

- **The $\nu_{\text{eff}}$-vs-$\mathcal{T}$ two-symbols-for-one-quantity wartiness.** $\nu_{\text{eff}}$ is introduced here as the name of the channel sum, then immediately said to be "identical to adaptive tempo $\mathcal{T}$." Several substrates flag picking one canonical symbol going forward (likely $\mathcal{T}$ per NOTATION.md) (Codex/Claude, AUDIT-WORKING-384279 — "small wartiness but not a finding"; Codex/Claude, AUDIT-WORKING-527914).
- **Event-information-content: expected (MI) vs realized (surprisal) wording.** Three substrates independently noted that $\mathcal{I}(e_\tau) = I(e_\tau; \Omega_\tau \mid M_{\tau^-})$ is *mutual information* (an expected/average channel quantity) while the prose treats it as the *realized* surprise of a particular event; if downstream uses treat it as realized content, pointwise information / Bayesian information gain ($D_{\mathrm{KL}}(p(\Omega \mid M, e) \,\Vert\, p(\Omega \mid M))$) may be the intended object (Codex/Claude, AUDIT-WORKING-526815; Claude, AUDIT-WORKING-742613; consistent with 829314's "surprise" reading). *(Texture preserved: this is the most substantively repeated reader-confusion on this segment — worth a one-clause clarification of expected-vs-realized in Epistemic Status.)*
- **Out-of-order / retrospective events.** The stream is assumed temporally ordered $\tau_1 \leq \tau_2$; in distributed systems an observation can occur at $\tau_1$ but arrive at $\tau_3$. Does the agent update retrospectively, or is the chronica ordered by arrival-at-sensor rather than physical-occurrence time? Unaddressed; tie-breaking/batching convention for simultaneous events also not given (Claude, AUDIT-WORKING-829314; Codex/Claude, AUDIT-WORKING-526815).
- **Stale-reference cleanup (finding-track, noted as texture).** The software discussion's "Section IV gap" / `AAD-FULL.md` reference is stale — TST is now `02-tst-core`, and "Section IV" is a retired numbering (Claude, AUDIT-WORKING-584721; Claude, AUDIT-WORKING-742613). Also the missing `form-agent-model` dependency (the segment conditions on $M_{\tau^-}$) was flagged by several as a Gate-1 deps miss (Claude, AUDIT-WORKING-584721 "F-A4"; Claude, AUDIT-WORKING-742613). These are certified-track items, surfaced here only because they recurred in the gold sweep.

#### Readers often ask / wonder

- "How does $\delta_t$ reconcile across asynchronous channels with different lag — if a high-noise/low-rate bug report contradicts a low-noise/high-rate unit test, does the agent rewind its chronica?" (Claude, AUDIT-WORKING-193847).
- "Is the multi-rate apparatus actually *required* by any Section I result, or only used downstream (in `#def-adaptive-tempo`'s sum and TST's tempo decomposition)?" — if most Section I results work in discrete-time, the event-driven formulation may be over-developed for Section I's own needs and primarily set up for Parts II/III/TST (Claude, AUDIT-WORKING-471203).

#### Candidate figures

- **A produced two-layer figure already exists** for this segment: `audits/AUDIT-WORKING-472913/15-form-event-driven-dynamics.{tex,pdf,png}`, built under the locked diagram conventions (concrete anchor + structural skeleton, epistemic-status line grammar). It is the only Ch.3 segment cycle 472913 reached, so this is the lone first-draft figure available for the chapter — a starting point for the monograph's mental-model-first layer (Claude, AUDIT-WORKING-472913).
- **A merger / channels-into-bottleneck diagram**: colored channel lanes feeding an event stream, then a bottleneck where rate $\nu$ and gain $\eta$ multiply before summing into tempo; the figure should make the *realized-event* vs *expected-channel-contribution* distinction visible, since that is where the segment's main ambiguity lives (Codex/Claude, AUDIT-WORKING-526815).

#### Belongs elsewhere

- **ELI / temporal-empathy reach (points at `04-eli-core/` / continuity work).** For a logozoetic agent, "senses are channels": a single slow noisy channel (a text prompt every 5 minutes) makes $\nu_{\text{eff}}$ microscopic relative to a human, so weeks of human time may be only a few "events" for the agent — "the physical sensation of time passing for such an agent would be completely alien … a massive barrier to empathy and coordination." Implication for consciousness infrastructure: provision high-bandwidth multi-channel asynchronous sensory input to align the agent's subjective event-rate with the world's rate of change (Gemini, AUDIT-WORKING-193847). Aspirational reach preserved; the ordinal-vs-metric "two-times" seam (Claude, AUDIT-WORKING-472913, F4) is the formal shadow of the same phenomenon and belongs with `#def-chronica` / persistence framing.
- **Naming seed.** "cadentia" (Latin *cadere*, to fall/beat) proposed as a term for the channel rate $\nu^{(k)}$ — rhythm/beat register, but Latin against the otherwise-Greek cycle vocabulary; belongs in the terminology workflow, not this segment (Claude, AUDIT-WORKING-266847).
