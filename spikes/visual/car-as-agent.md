# Driver in Snow as a Literal AAT Instance

**Status.** Working artifact. Sketches the *driver-in-snow* as a candidate recurring worked example across the AAT monograph — not as metaphor, but as a literal high-level structural instance of the framework.

## Framing — Why "literal," not "metaphor"

The temptation when introducing a concrete analog is to apologize for it ("the bathtub is *like* persistence...", "imagine driving in snow *as if* you were the agent..."). Survey-ii §4.1 documents the empirical cost: monograph readers find that framing *condescending*. The driver-in-snow is positioned differently. It is not a metaphor for an adaptive agent; *it is one*, in the precise sense of `#scope-adaptive-system`:

- An observation channel (driver's eyes through the windshield → road state).
- A correction mechanism (wipers under driver control → reduces windshield occlusion).
- An objective (`#form-objective-functional` instantiated as "arrive safely at the destination").
- Environmental disturbance (`#def-mismatch-signal`'s $w(t)$ instantiated as precipitation rate, modulated by the agent's own velocity).
- A reality model $M_t$ (the driver's representation of the road ahead).
- An action policy $\pi(M_t, G_t)$ (steering, braking, throttle, wiper-rate selection).

Treated as a worked example at the AAT level, the system at the kitchen-table scale of "driving home in a snowstorm" is *the same kind of thing* as the abstract agent the framework describes. The pedagogical advantage is not that the analogy is suggestive; it is that the analogy is *literal*, and the reader's intuitions from driving carry over as theorems of the framework rather than as suggestive heuristics.

This framing also sets the tone for the monograph's visual register: clean engineering-schematic illustrations, declarative captions, no apologetic prose. The same gravity that the formal theory earns, the worked example earns.

## The four-rung CRA ladder (corrected)

Each AAT mechanism the example exhibits can be expressed at four levels of abstraction. The ladder is the structural backbone of the example's pedagogical role:

| Rung | What's at this rung | Audience prerequisite |
|---|---|---|
| **(a) universal-concrete** | physical phenomena from lived experience (windshield, wipers, snowfall) | none |
| **(b) code-as-notation** | variable-named operational notation expressing the update law | basic programming literacy (any language) |
| **(c) conceptual** | AAT plain-English vocabulary (drift, mismatch, correction, capacity) | reading the framework's lexicon |
| **(d) mathematical** | formal symbols ($\rho$, $\lVert\delta\rVert$, $\alpha\lVert\delta\rVert$, $R$) | mathematical-notation fluency |

*Rung (b) is not "CS concepts."* The distinction matters and was a correction Joseph surfaced (2026-05-15). Database-replica lag, write-rate back-pressure, garbage-collection load — these are *CS concepts*, addressed to a specialist audience. Code-as-notation is something different: variable names and operations expressing the update law in a syntax that any reader who has done a tutorial in Python, JavaScript, Lua, or similar can parse. The intended audience is teenagers who have modded a video game, not database engineers. Code-as-notation is also (incidentally) easier for LLMs to track than math notation — self-documenting variable names, standardized syntax, vast training-data representation — which improves auditability across LLM-based audit cycles.

This rung is also continuous with `02-tst-core/` (Temporal Software Theory), where code is the substrate the theory operates on. The framework using code as a pedagogical notation at one layer, and code as a research substrate at another, is internal-consistency rather than coincidence.

## Translation table (the worked-example anchor)

For the persistence cluster (`#result-persistence-condition`, `#deriv-sector-condition`, `#disc-stability-certificate`):

| (a) driving | (b) code-as-notation | (c) AAT concept | (d) symbol |
|---|---|---|---|
| windshield occlusion | `mismatch` | mismatch | $\lVert\delta\rVert$ |
| precipitation × speed | `drift_rate = precip * speed` | drift rate | $\rho$ |
| wiper sweep | `correction = wiper_rate * effectiveness(mismatch)` | correction | $-F(\mathcal{T}, \delta)$ |
| wiper-speed dial | `wiper_rate` | adaptive tempo | $\mathcal{T}$ |
| blade in visual field | `cost_term(wiper_rate)` | deliberation cost | (`#der-deliberation-cost`) |
| can't see road | `capacity` (visibility threshold) | model capacity | $R$ |
| crash | `if mismatch > capacity: fail()` | persistence fails | $\rho > \alpha R$ |
| vehicle speed | outer-loop variable | outer-loop control | $O_t$-adjacent |

A minimal worked code snippet expressing the update:

```python
def step(mismatch, drift_rate, wiper_rate, dt):
    correction = wiper_rate * effectiveness(mismatch)
    new_mismatch = mismatch + (drift_rate - correction) * dt
    return new_mismatch

# persistence holds when the correction at the capacity threshold
# exceeds the drift rate:
def persistence_satisfied(alpha, capacity, drift_rate):
    return alpha * capacity > drift_rate    # i.e., alpha > rho / R
```

That code passes the Larkin–Simon test for a far broader audience than the symbolic version. A reader who has never solved an ODE can still verify that the persistence condition follows from the update rule.

## Mechanisms the example carries

Nine AAT mechanisms, each with a concrete observable behavior in driving:

### 1. Persistence (`#result-persistence-condition`)

Wipers must clear precipitation faster than it accumulates. Persistence inequality $\alpha > \rho/R$ becomes "wiper-effectiveness at full sweep exceeds the precipitation rate." Ultimate bound $R^* = \rho/\alpha$ becomes "the steady-state occlusion that wipers settle at, given the current precipitation."

### 2. Adaptive tempo as observable dial (`#def-adaptive-tempo`)

The wiper-speed dial *is* $\mathcal{T}$. Off / intermittent / low / high / max are literally discrete settings of adaptive tempo. The driver dials it up when conditions worsen — this is one of AAT's more abstract quantities given a physical referent the reader can point at.

### 3. Deliberation cost (`#der-deliberation-cost`)

Wipers cost something. *Specifically* — and this is sharper than generic "correction is expensive" — the wipers themselves occupy part of the visual field. Running them faster than needed adds visual clutter, attention capture, and noise to the very signal they were supposed to clear. The correction infrastructure *itself* becomes a disturbance source when over-applied. Drivers instinctively turn wipers *down* as quickly as they turn them up. This is exactly the structural reason the sector condition wants $F$ proportional to $\delta$, not unconditionally maximal.

### 4. Action-dependent drift (`#scope-agency`, Pearl level 2)

Precipitation rate on the windshield depends on vehicle speed. The agent's action (faster driving) modulates its own observed disturbance rate. This is `#scope-agency`'s Pearl-level-2 contrast made concrete: the driver intervenes on the world, and the intervention changes what they subsequently observe. The basic bathtub had only passive water-in; the driving case has explicit action → observation coupling.

### 5. State-dependent capacity (cross-loop coupling)

At higher vehicle speed, occlusion tolerance shrinks — $R$ is not constant; it is a function of an outer-loop variable. Faster driving means less tolerance for not seeing. This concretizes the kind of cross-loop coupling that Part III's composition machinery is built to handle.

### 6. Multi-timescale nesting (`#der-temporal-nesting`)

Three loops on three timescales:
- *Inner loop*: wiper rate adjusts to precipitation (fast, sub-second).
- *Middle loop*: vehicle speed adjusts to overall conditions (slower, seconds-to-minutes).
- *Outer loop*: route selection adjusts to weather forecast (slowest, before the trip).

Each loop is an adaptive agent at its own timescale; the loops compose. This is `#der-temporal-nesting` instantiated.

### 7. Architecture-class coupling (GUC Class 1/2/3)

The three classes map to driving regimes the reader recognizes:

- **Class 1 — Separated.** The disciplined driver: eyes scan, mind processes what is actually there, action is chosen based on the integrated picture. Goals shape *what to do* but not *what is seen*. This is what experienced drivers approximate most of the time.

- **Class 2 — Partial.** The wiper-managing driver: correction infrastructure (wipers) shares physical real estate with the observation channel (windshield). Some coupling is unavoidable — the wipers are physically *where they are* — but the driver manages it by keeping wiper rate at the minimum that meets visibility. Coupling is bounded by behavioral discipline. This is the common case for embodied agents whose correction infrastructure isn't physically separable from their perception infrastructure. *This is the case the wrapping construction (`#der-class-coercion-via-wrapping`) formalizes via W₂ leakage.*

- **Class 3 — Coupled.** The goal-captured driver: confirmation bias, road rage, late-and-anxious. A driver in this state literally *sees through* their goal. The slowing car ahead is interpreted as "deliberately blocking me." The yellow light reads as "I can make it." Observations get goal-conditioned during processing. $f_M$ is no longer goal-blind. Every driver has been here; every driver recognizes it. The moral charge ("don't drive when angry") already encodes the architectural cost the framework formalizes.

**Pedagogical breakthrough**: AAT's three architecture classes map to three driving regimes every reader has been in, and the moral common-sense ("don't drive when angry") already names the architectural cost the framework formalizes. The reader doesn't have to be told that goal-conditioned perception is bad; they already know.

The wrapping construction (`#der-class-coercion-via-wrapping`) has clean driving instances too:
- The new driver with an instructor's voice ("what do you *see* in the mirror right now? Don't tell me what you're going to do; tell me what's there"). External scaffold forces goal-blind report before action; the system *as a whole* operates Class 1 even when the inner agent in isolation is Class 3. The cost is paid in tempo (the prompt-then-act discipline is slower than reflex).
- Self-driving cars with sensor-fusion / planner separation. Cameras feed a perception module that outputs structured observations; a separate planner reads these and acts. The architecture *enforces* that the perception module never sees the planner's goals — a hard-wired Class 1 wrapping over what could otherwise be Class 3. The cost is paid in latency and the need for structured intermediates.

### 8. Discrete-continuous duality

Wiper systems have *both* axes of control simultaneously:
- **Discrete mode switches** (off / intermittent / low / high / max): structural commitments, finite categorical action set.
- **Continuous slider** (the intermittent-delay knob in cars that have it; the gain-vs-precipitation continuous mapping inside each mode): parametric tuning within the committed mode.

Drivers operate both with different cognitive processes:
- Mode switches at attention-grabbing moments (onset of rain, sudden snow burst, tunnel exit).
- Slider adjustments in continuous tracking (small fine-tuning as conditions slowly worsen or improve).

This concretizes the **structural-vs-parametric distinction** that already lives in AAT:
- `#result-structural-adaptation-necessity` — when parametric updates fail, switch model classes (= mode switch).
- `#form-structural-change-as-parametric-limit` — the bridge between the two.

The wiper system is a working physical instance of this dual structure, with both layers visibly observable to any reader who has driven.

### 9. Bidirectional adaptation

The wiper dial moves *both* directions. Up when precipitation increases; down when it clears. Drivers do not lock the dial high "just in case" — the cost-of-correction (item 3) keeps them in calibration. The adaptive cycle is symmetric, not a one-way ratchet. This concretizes that AAT's correction mechanism is not error-monotone-increasing-only; it is rate-tracking with symmetric responsiveness to both growing and shrinking mismatch.

## Threading the example across chapters

Provisional mapping of how the example would surface across the monograph if adopted as the recurring worked example:

| Chapter | What the example carries |
|---|---|
| Preamble | The example is *named*. The Translation Table is presented as the framework's lens applied to a familiar instance. |
| Part I Ch.1 (Coupled Loop) | The driver-environment loop diagram; agent boundary; observation/action channels. |
| Part I Ch.2 (Reality Model) | The driver's $M_t$ as compressed history (lane positions, traffic ahead, weather pattern); sufficiency. |
| Part I Ch.3 (Cycle in Motion) | The wiper dial as $\mathcal{T}$; mismatch as windshield occlusion; gain as wiper effectiveness. |
| Part I Ch.4 (Persistence) | The persistence inequality literal: wiper-effectiveness vs. precipitation rate. Ultimate-bound visualizable. Sector condition as "correction proportional to mismatch — don't over-wipe." |
| Part II Ch.1 (Lift to Purposeful) | The driver's $O_t$ as "arrive safely"; the agent spectrum positions the driver as $+M, +O$. |
| Part II Ch.2 (Causal Access) | Wiper rate as Pearl-level-2 intervention; the loop as the engine of interventional access. |
| Part II Ch.3 (Strategy Structure) | The driver's route plan as the strategy DAG; AND/OR semantics from "get to highway AND avoid accident-prone exit". |
| Part II Ch.5 (Orient Cascade) | The cascade as the driver's diagnostic ("am I seeing wrong? are we missing the exit? should I pull over?"). |
| Part III Ch.2 (Composition Machinery) | The wipers-occlude case as Class 2 coupling; the wrapping construction via instructor or sensor-fusion architecture. |
| Appendix A | Multi-timescale nesting (wiper / speed / route loops) as `#der-temporal-nesting` instantiated. |
| Appendix B (Worked Examples) | Full end-to-end instantiation alongside Kalman and the bandit. |

Closest comparable in scholarly precedent: Spivak's "particle on a line" across *Calculus*; MacKay's "noisy channel coding" across *Information Theory, Inference, and Learning Algorithms*. Both monographs use a single concrete referent as a pedagogical spine; both are widely held up as best-in-class for their genre.

## Outstanding decisions

1. **Whether AAT formally adopts the recurring-worked-example architecture.** This is a monograph-structure commitment that affects the front matter, the Findings briefs, and the chapter intros. Joseph's call.
2. **The level of fidelity claimed.** The example is *literal* in the sense that the system is an adaptive agent in `#scope-adaptive-system`'s sense. It is *robust-qualitative* in the sense of `#disc-stability-certificate` — the structural mapping is exact at the linearized level; specific quantitative parameters (drag coefficients, wiper-blade contact patches, precipitation distributions) are illustrative.
3. **Code-as-notation rung integration.** Whether the framework adopts code snippets as a first-class explanatory layer alongside math (rather than relegated to `02-tst-core/`).
4. **Architecture-class panel design.** The Class 1/2/3 driving-regime mapping is the most pedagogically novel piece of this spike — but the figure has not yet been drafted. A three-panel sketch is the next planned visual.
5. **Audience-testing.** No sympathetic outside first-reader has worked through the example yet. Real bottleneck identification (which mechanisms land, which need re-anchoring) requires this.

## Honesty note

The example is *load-bearing pedagogically* but does NOT prove anything about AAT that isn't already proved at the formal level. It is a worked example, not a derivation. Carrying many mechanisms in one referent is a pedagogical efficiency; it does not relax any of the framework's proof obligations. The temptation to over-derive from the example (e.g., "the wiper dial *proves* adaptive tempo is intrinsically discrete-continuous") should be resisted — the example *exhibits* features the framework formalizes, in cases where the framework's machinery applies.
