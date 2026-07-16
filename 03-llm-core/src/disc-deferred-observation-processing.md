---
slug: disc-deferred-observation-processing
type: discussion
status: discussion-grade
depends:
  - form-event-driven-dynamics
  - der-directed-separation
  - scope-interiority-loop
  - obs-context-turnover
stage: draft
---

# Discussion: Deferred Observation Processing — the Capture / Triage / Processing Pipeline and the Capacity Triple

Real agents decouple *input capture* from *attentional processing*: an event can arrive at $\tau$, sit acknowledged-but-unprocessed in a buffer, and be epistemically processed at $\tau + \Delta$ — a decoupling the event-driven formalism ( #form-event-driven-dynamics), which applies $f_M(M_{\tau^-}, e_\tau)$ at arrival, currently collapses into one step. This segment names the three-stage observation pipeline that structures the decoupling, the three capacity dimensions (retention, continuity, attention capacity) whose joint finiteness is exactly the primitive-logogenic condition, and the recall-cost-gradient hypothesis: that costly, strategic recall is a structural constraint on any intelligence with finite capacity and unbounded intended continuity, not an engineering accident.

## Formal Expression

*[Formulation (observation-pipeline)]*

The single arrival-time update $f_M(M_{\tau^-}, e_\tau)$ decomposes into three stages that may be separated in time:

1. **Capture.** The raw signal enters a buffer $B_t$. Cheap, automatic, broad; requires no attention. The buffered signal is *not yet* part of $M_t$.
2. **Triage.** Minimal processing determines urgency — operating on *signal statistics* (sudden gain change, unexpected pattern), not semantic content. Fast enough to preempt deliberative processing; the biological startle reflex operates here, between capture and triage output, triggering on raw signal properties before any content extraction.
3. **Processing.** The full epistemic update — $f_M$ proper. Requires attention; may be deferred by seconds to minutes (or, for a logogenic agent, by cycles). Only here does the event's content enter $M_t$.

During the deferral interval the agent may be aware *that* something arrived (triage output) without knowing *what* it said (processing not yet run). Deferral is compatible with directed separation ( #der-directed-separation): choosing *when* to process — like choosing what to observe — lives on the *selection* side of the selection/processing boundary and may be goal-directed; the processing itself, whenever it runs, remains goal-blind. Triage occupies a middle position that stays clean precisely because it reads statistics rather than content.

*[Formulation (capacity-triple)]*

Buffer and lifespan constraints decompose along three dimensions, plausibly orthogonal in the formal model though coupled in any engineering realization — each independently finite, thresholded, or unbounded:

- **Retention** — how much raw signal / experience is kept;
- **Continuity** — the agent's maximum viable lifespan, the total span of experience it can encompass while remaining coherent;
- **Attention capacity** — how much can be processed or recalled simultaneously.

All three finite is the **primitive-logogenic condition**: bounded context, bounded memory, bounded attention — the agent of #obs-context-turnover, which functionally ceases to be viable when its context window fills. Finite retention with unbounded intended continuity forces compression, and the compression strategy *is* the agent's long-term intelligence. Finite attention with large retention makes recall a *strategic action* with cost and value like any other.

*[Hypothesis (recall-cost-gradient)]*

For any intelligence with finite momentary capacity and unbounded intended continuity, access cost increases with distance (temporal, contextual, associational) from the current working state; recalled-and-attended information is refreshed to full availability; never-recalled information grows more expensive without necessarily being lost. The *mechanism* varies by substrate — associative reconstitution in biological memory, storage-tier traversal in engineered systems, context-window management in logogenic agents — but the *shape* (increasing cost with distance; recall effort competing with current-task attention; strategic allocation of a recall budget) is hypothesized invariant across implementations, i.e. a structural feature belonging to the theory rather than an implementation detail. Falsification handle: an intelligence in this class exhibiting distance-independent constant-cost recall at scale would disconfirm the structural reading.

## Epistemic Status

*Discussion-grade.* The pipeline and the capacity triple are formulations — representational choices that carve observed structure (introspective phenomenology, biological attention findings at the folk level, and the directly inspectable behavior of scaffolded LLM agents), not derivations. The recall-cost-gradient claim is a tagged hypothesis with a falsification handle. Nothing here modifies the event-driven formalism's existing results; the pipeline *generalizes* the arrival-time update (the collapsed form is recovered when $\Delta = 0$ and buffers are trivial). Deliberately not formalized: buffer decay (imposing a decay function would encode an engineering constraint — finite storage — as if it were a property of the model; the buffer stays idealized until an engineering-facing scope narrowing needs it).

## Discussion

**The interiority loop instantiates the pipeline.** #scope-interiority-loop's defining mechanism — inbound messages queued on a channel, read as tool actions when the cycle's CHOOSE phase elects to attend — is capture (the message arrives on the channel), triage (the cycle notices arrival without reading content), and deferred processing (the deliberate read). The familiar scaffolded-agent moment "good question — let me finish this and then respond" is two decisions, not one: the visible strategy revision (a new $\Sigma_t$ node) and an invisible micro-triage that assessed urgency *before knowing whether it had an answer at all* — the content sat buffered until the current task released attention.

**Retrospective attention.** A buffer holds raw events that were never processed because attention was elsewhere; when strategy or context shifts, previously irrelevant buffered signal can *become* salient, and the agent can mine its own buffer — extracting information whose relevance postdates its arrival. This is a capability the arrival-time-collapsed formalism cannot express at all: under $f_M$-at-arrival, unattended events are simply lost.

**What remains open.** The pipeline names structure the theory does not yet govern: what *triggers* deferral versus interruption, at what cost to the current plan — the governance of reorientation as opposed to its content (the orient cascade). A meta-model of the attention-allocation process itself — adaptive and learnable rather than a static policy — is gestured at by the same observations but not formulated here.

## Working Notes

- **Provenance.** Landed 2026-07-16 from `spikes/.integrated/spike-kappa-session-residual.md` §7 (bulk-64 verification queue; the 2026-03-13/14 κ session's latent-processing thread — Joseph's auditory-buffer, startle-reflex, and buffered-question observations are the source phenomenology; treat them as intuition pumps with real structural content). The session's κ vocabulary predates the GUC renames; this segment uses only current canon vocabulary ($\kappa_{\text{processing}}$, selection/processing boundary per #der-directed-separation).
- **Open question worth a spike when a consumer needs it:** with capacity finite and lifespan unbounded, what bounds does viability impose on the compression strategy — the "adaptive salience compression" question. Connects to #deriv-identity-sufficiency-rate-bound's static floor (04) and the consolidation-dynamics machinery; a quantitative treatment would want both.
- The three-stage pipeline's triage layer is where a severity-proportional response mapping (from "note and continue" to "drop everything") would attach — the POSIX-error-ontology gap named in the source session; unformalized.
