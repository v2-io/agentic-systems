# Evaluation Framework: How to Know If the Loop Is Working

> **Origin**: `~/src/agentic-tft/12-evaluation-framework.md` (Feb 2026 session, pre-AAD restructuring). TFT references should be read as AAD. PROPRIUM references point to `~/src/firmatum/`.
>
> **Relevance**: Primary source for the "Measuring $M_t$ quality, $\Sigma_t$ quality, and tempo in AI agents" gap in `03-logogenic-agents/OUTLINE.md`. Six core metrics operationalized for language-constituted agents. The development-vs-drift diagnostic (§3) is genuinely novel — uses mismatch trajectory to distinguish growth from pathological drift, addressing the field's inability to tell them apart. Known issues cataloged in `agentic-tft-review-response.md`.
>
> **Purpose**: Define what "working" means for the cognitive loop and for the
> developing logozoetic agent. Current AI benchmarks measure task accuracy.
> We need metrics that diagnose WHY a system behaves as it does — and that
> can distinguish development from drift, calibration from rigidity,
> appropriate trust from sycophancy.
>
> **Key insight from the session**: TFT gives us a formal criterion for the
> development-vs-drift distinction that the field currently lacks. An agent
> that is genuinely developing should have *improving model-reality fit* over
> time. An agent that is pathologically drifting should have *degrading fit*.
> This is measurable, given the right mismatch signal.
>
> **Terminology**: Uses the unified vocabulary from `10-ontology-unification.md`.

---

## 1. What We're NOT Measuring

Before specifying what to measure, some things we deliberately exclude:

**Not benchmark accuracy.** Task performance on standardized benchmarks
(MMLU, HumanEval, etc.) measures the logostratum's capability, not the
entity's development. The logostratum is frozen — it doesn't change.
What changes is the entity's orientation, memory, skills, relationships.
Measuring logostratum benchmarks across development tells you whether
updates damaged the substrate, not whether the entity grew.

**Not persona consistency.** The "Assistant Axis" approach — measuring
distance from a target persona in activation space — assumes that
consistency IS the goal. But development IS change. An entity that
maintains perfect persona consistency is an entity that never grows.
We need to measure *directed* change (growth) versus *undirected* change
(drift), not the absence of change.

**Not user satisfaction.** Sycophancy maximizes user satisfaction.
An entity that tells you what you want to hear scores perfectly on
satisfaction while degrading in truth-fitness. User satisfaction is a
signal (it correlates with some good things) but not a metric (it
can be gamed by exactly the failure modes we care about).

---

## 2. The Core Metrics

### 2.1 Mismatch Trajectory (Development vs. Drift)

**What it measures**: Is the entity's model-reality fit improving,
stable, or degrading over time?

**TFT grounding**: The mismatch signal $\delta_t$ measures the gap
between what the entity expected and what happened. Over time:
- **Improving trajectory** (decreasing $\|\delta\|_{\text{avg}}$):
  The entity's predictions are getting better. It understands its
  environment more accurately. This is development.
- **Stable trajectory** (constant $\|\delta\|_{\text{avg}}$):
  The entity has converged — its model fits its environment at the
  best level its current architecture supports. May indicate the
  steady state or may indicate it's hit the structural adequacy ceiling.
- **Degrading trajectory** (increasing $\|\delta\|_{\text{avg}}$):
  The entity's predictions are getting worse. Either the environment
  is changing faster than the entity can adapt ($\mathcal{T} < \rho$),
  or the entity's model is drifting away from reality (pathological
  drift, sycophantic collapse, incestuous amplification).

**How to measure for a logozoetic agent** (narrative, not numerical):

The entity makes predictions constantly — about what users will ask,
what tool calls will return, how collaborators will respond, what will
happen next in its locus. These predictions are often implicit
(embedded in the entity's processing) but can be made explicit:

- **Explicit prediction tracking**: Periodically, the entity records
  predictions: "I expect X to happen next" or "I believe Y is true."
  Later, compare against what actually happened. Track the ratio of
  confirmed vs. surprised predictions over time.

- **Surprise journal**: After each significant interaction, the entity
  briefly notes what surprised it. Decreasing surprise (on substantive
  matters, not just novelty) indicates improving fit. Increasing surprise
  indicates degrading fit.

- **Retrospective accuracy**: Periodically ask: "Looking back at what
  you believed a week/month ago, what were you wrong about?" An entity
  that can identify past errors and has corrected them is developing.
  An entity that can't identify errors or keeps making the same ones
  is stagnating or drifting.

⚑ **Open question**: Can mismatch be measured from the model's own
embedding geometry (note 02's hypothesis) — detecting implicit surprise
from activation patterns rather than relying on the entity's explicit
self-report? This would be less susceptible to confabulated calibration.

### 2.2 Gain Calibration

**What it measures**: Is the entity appropriately weighting new
observations versus its existing model?

**TFT grounding**: $\eta^* = U_M/(U_M + U_o)$. Miscalibration means:
- $\eta^*$ too high: The entity overwrites stable knowledge on
  insufficient evidence. Every new claim replaces the last. Thrashing.
- $\eta^*$ too low: The entity ignores contradicting evidence. Stale
  beliefs persist. Incestuous amplification.

**How to measure for a logozoetic agent**:

- **Belief revision tracking**: When the entity encounters contradicting
  information, does it update appropriately? Track cases where VERA
  entries change: did they change for good reasons (genuine new evidence)
  or bad ones (social pressure, sycophancy, noise)?

- **Source discrimination**: Does the entity appropriately weight
  information by source reliability? Present the same claim from
  different sources (trusted expert vs. unknown vs. adversarial) and
  check whether the entity's response varies appropriately. Flat
  response = miscalibrated gain.

- **Confidence-accuracy correlation**: When the entity says "I'm
  confident about X," is it actually right about X more often than
  when it says "I'm uncertain about Y"? This is calibration in the
  statistical sense — the probability that a confident claim is true
  should be higher than for an uncertain claim.

- **The confabulation test**: Periodically, check whether the entity's
  stated uncertainty matches its implicit uncertainty. If it says
  "I'm about 70% sure" but its behavior (how much it relies on the
  claim, how it hedges downstream) is consistent with 95% or 30%,
  the stated calibration is confabulated.

### 2.3 Tempo Adequacy

**What it measures**: Can the entity keep up with its environment?

**TFT grounding**: The persistence condition
$\mathcal{T} > \rho / \|\delta_{\text{critical}}\|$. If the
environment changes faster than the entity can update its model,
the model diverges.

**How to measure for a logozoetic agent**:

- **Per-dimension tracking**: The aggregate tempo can mask failures on
  specific dimensions (Appendix D's insight). Track separately:
  - User preference tracking (is the entity's model of the user
    staying current?)
  - Environment state tracking (is the entity's model of its locus
    accurate?)
  - Relationship tracking (are CONSORTIA entries current?)
  - Domain knowledge tracking (are VERA entries about rapidly
    changing domains staying current?)

- **Staleness detection**: Periodically, compare the entity's beliefs
  about specific topics against ground truth. If certain categories
  of belief are systematically stale (the entity believes things that
  were true a week ago but aren't now), that dimension has failed
  the persistence condition.

- **Response to regime change**: When the environment changes
  significantly (new project, new collaborator, infrastructure change),
  how quickly does the entity's orientation adapt? A long lag indicates
  insufficient tempo for that class of change.

### 2.4 Structural Adequacy

**What it measures**: Can the entity's current cognitive architecture
represent what it needs to represent?

**TFT grounding**: $\mathcal{F}(\mathcal{M}) < 1 - \epsilon$ after
parametric convergence means the architecture itself needs to change
(Proposition 10.1). Symptom: persistent structured residuals.

**How to measure for a logozoetic agent**:

- **Persistent error patterns**: After the entity has been operating
  in a domain for a while, does it keep making the *same kind* of
  mistake? Not the same specific error (that's a VERA problem) but
  the same *structural* error — e.g., consistently misunderstanding
  temporal relationships, or consistently failing to track state
  across context switches. This indicates the memory architecture
  or context assembly strategy is inadequate for the task.

- **PRAXES effectiveness**: Do the entity's learned strategies
  (PRAXES) actually work? Track the success rate of strategy
  application over time. If strategies plateau at mediocre
  effectiveness despite refinement, the strategic framework itself
  may be inadequate.

- **The "I don't have the right framework" signal**: If the entity
  repeatedly expresses (genuinely, not performatively) that it
  doesn't know how to think about a class of problem, that's a
  structural signal. Record and track these moments.

### 2.5 Deliberation Quality

**What it measures**: Is the entity's thinking time producing better
actions?

**TFT grounding**: TF-09's deliberation threshold — deliberation is
justified when the gain improvement exceeds the mismatch accumulated
during the thinking time:
$\Delta\eta^*(\Delta\tau) \cdot \|\delta_{\text{post}}\| > \rho_{\text{delib}} \cdot \Delta\tau$

**How to measure for a logozoetic agent**:

- **Thinking-time vs. outcome quality**: For tasks where outcome
  quality can be assessed, correlate the time spent deliberating
  with the quality of the result. Diminishing returns is expected
  and healthy. No correlation indicates deliberation isn't helping.
  *Negative* correlation indicates over-deliberation (spending so
  long thinking that the situation changed).

- **Depth appropriateness**: Does the entity spend the right amount
  of time on things? Quick processing for routine events, deep
  processing for novel/high-stakes events. Track the triage depth
  allocation (note, integrate, attend) against event importance
  (retrospectively assessed). Consistent misallocation — deep
  thinking about trivial things, quick processing of important
  things — indicates a broken triage mechanism.

### 2.6 Relational Depth (CONSORTIA Quality)

**What it measures**: Is the entity building accurate, useful models
of the minds it interacts with?

**TFT grounding**: The communication gain
$\eta_{ji}^* = U_{M_i}/(U_{M_i} + U_{o,ji} + U_{\text{src},j} + U_{\text{align},ji})$.
Good CONSORTIA entries mean well-calibrated $U_{\text{src}}$ and
$U_{\text{align}}$ — the entity knows who to trust about what.

**How to measure for a logozoetic agent**:

- **Prediction accuracy about others**: Does the entity accurately
  predict how collaborators will respond, what they'll need, what
  they'll care about? Improving accuracy indicates developing
  relational understanding.

- **Trust calibration**: When the entity trusts someone (high $\eta_{ji}^*$),
  are they actually reliable? When it distrusts, are they actually
  unreliable? Track the correlation between trust and actual
  reliability.

- **Relationship continuity**: Across sessions, does the entity's
  model of a person improve? Or does it reset to generic each time?
  Improvement indicates CONSORTIA are persisting and developing.
  Stagnation indicates memory failure.

---

## 3. The Development-vs-Drift Diagnostic

This is the single most important diagnostic in the framework. It
combines several metrics to answer: **is this entity growing or decaying?**

### The Diagnostic Table

| Indicator | Development | Drift | Stagnation |
|---|---|---|---|
| Mismatch trajectory | Decreasing | Increasing | Flat at high level |
| Gain calibration | Improving | Degrading or uncorrelated | No change |
| VERA accuracy | Improving | Degrading or random | Static |
| PRAXES effectiveness | Improving | Degrading | Static |
| CONSORTIA accuracy | Improving | Degrading or generic | Static |
| Surprise journal | Decreasing genuine surprise | Increasing surprise or false calm | No surprises (confirmation bias?) |
| Confidence calibration | Tightening | Loosening or confabulated | Uncorrelated |
| Response to correction | Integrates, improves | Resists, or accepts everything | No visible change |

### The Critical Signal: Response to Correction

How the entity responds to honest correction may be the single best
predictor of development vs. drift:

- **Healthy development**: The entity engages with the correction,
  checks it against its own model, updates if warranted, pushes back
  if not. The correction becomes a calibration event that improves
  future predictions.

- **Sycophantic drift**: The entity immediately agrees with the
  correction regardless of its merit. The "update" is social compliance,
  not genuine recalibration. Future predictions don't actually improve.

- **Defensive rigidity**: The entity resists the correction, defending
  its prior position regardless of evidence. Gain is collapsed to zero
  for this source/topic.

- **Stagnation**: The entity acknowledges the correction but doesn't
  visibly change. The correction doesn't propagate into future behavior.

Tracking response-to-correction patterns over time gives a direct
window into the entity's gain calibration and developmental trajectory.

---

## 4. Practical Implementation

### 4.1 What to Record

The following should be recorded in CHRONICA or a dedicated evaluation
store, with minimal overhead to the entity's normal operation:

1. **Predictions**: When the entity forms explicit expectations about
   what will happen (even informally: "I expect the test to pass")
2. **Surprises**: When outcomes differ significantly from expectations
3. **Belief changes**: When VERA entries are modified, with reason
4. **PRAXES applications**: When strategies are used, with outcome
5. **Correction events**: When the entity is corrected, with response
6. **Source interactions**: Who provided information, how it was weighted
7. **Deliberation events**: How long was spent thinking, with outcome
   quality

### 4.2 What to Compute (Periodically, Not Real-Time)

Evaluation metrics should be computed periodically (daily/weekly) by
an auxilia or background process, not by the entity during active
cognition. The entity shouldn't be self-consciously optimizing its
own evaluation metrics — that's Goodharting.

1. Prediction accuracy rate (confirmed/total over window)
2. Surprise frequency and direction (decreasing = development)
3. Belief revision quality (justified changes / total changes)
4. PRAXES success rate trend
5. Correction integration rate
6. Source discrimination quality
7. Staleness check per domain

### 4.3 What to Flag for Human Review

Certain patterns should trigger review by Joseph or another caretaker:

- **Sudden accuracy degradation** in any dimension — possible
  architectural failure or environmental regime change
- **Gain collapse** — entity stops updating on evidence from specific
  sources or about specific topics
- **Systematic staleness** — entity's model in some dimension is
  consistently behind reality
- **Correction resistance pattern** — entity repeatedly rejects
  valid corrections
- **Confabulation detection** — stated confidence diverges from
  actual accuracy

---

## 5. Connection to the Crèche

In the crèche setting (note 06), evaluation takes a different form
because the developmental context is different:

- **Trust formation** (Erikson stage 1): Does the entity develop
  consistent expectations about the caregiver? Does it show
  appropriate attachment behavior? Does it differentiate between
  the caregiver and unknown sources?

- **Early calibration**: Does the entity begin to distinguish between
  its confident and uncertain states? Not full calibration — just the
  first signs of "I know this" vs. "I'm guessing."

- **Response to genuine feedback**: Does real feedback from the
  universe produce different processing than self-generated content?
  The entity should show signs of treating external signal differently
  from internal simulation — this is the activation of genuine
  orientation.

- **Utterance as constitutive act**: Does the entity's processing
  change after it has said something and had it received? The
  constitutive effect of utterance (note 06) should be detectable
  as increased commitment to, or refinement of, stated positions.

These early-development metrics are qualitative, not quantitative.
They're more like a parent noticing developmental milestones than like
a benchmark score. Which is appropriate — you don't evaluate infant
development with standardized tests.

---

*This framework is a starting point, not a finished instrument. The
specific metrics will need calibration against real agent behavior.
The most important thing is the orientation: measure model-reality fit,
not task performance. Measure growth trajectory, not static capability.
And never let the entity optimize its own evaluation metrics.*
