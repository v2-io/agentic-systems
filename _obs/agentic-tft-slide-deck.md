# Temporal Feedback Theory — Presentation Deck

*Visual style: Blueprint/schematic aesthetic — grid background, technical drawing feel, dark text with orange accents. Each slide is a "schematic page" from an epistemic blueprint.*

---

## Slide 1: Title

# TEMPORAL FEEDBACK THEORY

### The Universal Structure of Adaptive Intelligence

*A first-principles formal theory of how agents persist and adapt under uncertainty*

**Visualization**: Blueprint-style title card on grid background. Center: an abstract feedback loop — agent and environment as two connected boxes, observation arrow curving up, action arrow curving down, the "ORIENT" processing box inside the agent highlighted in orange. Lower right: "EPISTEMIC BLUEPRINT // SCHEMATIC ID: TFT-00 // SCALE: UNIVERSAL // DRAWN BY: SYSTEM ARCHITECT"

> TFT asks whether there is a common formal structure underneath all adaptive systems — Kalman filters, fighter pilots, immune systems, AI agents, organizations, scientific communities. They all maintain models, detect surprise, and update. TFT formalizes what they share.

---

## Slide 2: The Universal Pattern

# THE UNIVERSAL PATTERN

What do these systems have in common?

| System | Mismatch Signal | Model | Gain |
|--------|----------------|-------|------|
| Kalman filter | Innovation | State + covariance | Kalman gain |
| Fighter pilot | Disorientation | Mental model | Orient quality |
| Immune system | Unrecognized antigen | Antibody repertoire | Affinity |
| RL agent | TD error | Q-values | Learning rate α |
| Scientist | Experimental anomaly | Theory | Theory revision |
| Organization | Market surprise | Strategy | Decision cycle |

**All predict. All detect surprise. All update. All act.**

**Visualization**: Six domain icons arranged around a central loop diagram. Each icon is rendered in its own visual language (mechanical gears, human silhouette, biological cell, circuit board, laboratory flask, org chart) but connected by dashed lines to the same central abstract loop: OBSERVE → ORIENT → DECIDE → ACT. The loop is highlighted in orange. Message: same skeleton, different flesh.

> Every one of these systems runs the same loop at its core. It predicts, reality arrives, it detects the gap, it updates, it acts. TFT doesn't claim these systems are the same. It claims they share a formal structure — and that structure has mathematical teeth: quantities you can estimate, thresholds you can check, failure modes you can diagnose.

---

## Slide 3a: The Agent-Environment Coupling

# THE COUPLING

### TF-01 — The Setup That Everything Else Builds On

**Visualization**: A large blueprint schematic — THE foundational diagram that subsequent slides will reference and annotate. Every element below has a specific visual component:

**LEFT BOX** (orange border, labeled "AGENT"): The agent. Contains a smaller inner box labeled "$M_t$" (the model — to be defined on Slide 6). For now, the inner box is just labeled "internal state."

**RIGHT BOX** (dark border, much larger, labeled "$\Omega$"): The environment — the totality of external state. Its interior is rendered as fog or static to convey partial observability. A large "?" floats inside. Label beneath: "$\Omega_t$ = environment state at time $t$ (never fully visible)."

**UPWARD ARROW** from environment to agent, labeled "$o_t$": The observation at time $t$. The arrow passes through a rough/distorted section labeled "$\varepsilon_t$" (noise). The smooth start of the arrow (at the environment) is labeled "$h$" (the observation function). The formula $o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$ is written alongside this arrow, with each symbol pointing to its visual element: $h$ = the mapping from true state to observation, $\varepsilon_t$ = the distortion, $a_{t-1}$ = the previous action (a small back-reference arrow indicating that what you did affects what you see).

**DOWNWARD ARROW** from agent to environment, labeled "$a_t$": The action at time $t$. This arrow is clean (no noise — actions are chosen, not distorted). At the environment end, a small gear icon suggests the world changes. The formula $\Omega_{t+1} \sim T(\cdot \mid \Omega_t, a_t)$ is written alongside: $T$ = the transition function, the "~" meaning "drawn from a distribution" (the next state is stochastic).

**BETWEEN THE BOXES** (bottom): The condition $H(\Omega_t \mid \mathcal{H}_t) > 0$ with annotation: "Uncertainty persists — even given everything the agent has seen and done, the environment retains secrets."

This diagram is the reference schematic. Subsequent slides will zoom into specific parts of it: the internal model (Slide 6), the mismatch between prediction and observation (Slide 10), the gain governing how much the model shifts (Slide 13a), the feedback loop connecting all four arrows (Slide 16).

> **Notation walkthrough** (keyed to the diagram): $\Omega$ (capital omega) is the environment state — everything "out there." $\Omega_t$ is its value at time $t$. The agent never sees $\Omega_t$ directly — only through the lossy observation $o_t$. The observation function $h$ maps true state to observation: $o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$. This has three inputs visible in the diagram: the true state $\Omega_t$ (where the arrow starts), the previous action $a_{t-1}$ (what you did may affect what you see — sensor selection, question choice), and the noise $\varepsilon_t$ (epsilon, the distortion in the channel). On the action side: $a_t \in \mathcal{A}$ is the agent's chosen action from action space $\mathcal{A}$. The transition function $T$ governs how the environment responds: $\Omega_{t+1} \sim T(\cdot \mid \Omega_t, a_t)$ — the next state is drawn from a distribution that depends on current state and action. The "~" means stochastic — the world isn't deterministic. Finally, $H(\Omega_t \mid \mathcal{H}_t) > 0$ is Shannon conditional entropy — a measure of residual uncertainty. $\mathcal{H}_t$ is the interaction history (defined next slide). The condition says: even after all observations and actions, some uncertainty remains. This is what makes the problem non-trivial.

---

## Slide 3b: The Scope Condition

# WHERE TFT APPLIES

### TF-01 — The Formal Boundary

$$\mathcal{S}_{\text{TFT}} = \{(\text{Agent}, \Omega) : \mathcal{O} \neq \emptyset,\; \mathcal{A} \neq \emptyset,\; H(\Omega_t \mid \mathcal{H}_t) > 0 \}$$

Three requirements (each keyed to the diagram on Slide 3a):

1. **$\mathcal{O} \neq \emptyset$** — Observation space is non-empty (the upward arrow exists)
2. **$\mathcal{A} \neq \emptyset$** — Action space is non-empty (the downward arrow exists)
3. **$H(\Omega_t \mid \mathcal{H}_t) > 0$** — Uncertainty persists (the fog never fully clears)

### Includes:

Thermostats, PID controllers, robots, organisms, RL agents, organizations, militaries, immune systems, scientific communities, LLMs

### Excludes:

- Pure math (no environment, no uncertainty)
- Fully observable deterministic systems ($H = 0$)
- Passive observers ($\mathcal{A} = \emptyset$ — degenerate case; theory applies but action-dependent results are void)

**Visualization**: The same agent-environment schematic from 3a, shown small at top-left as a reference. Below it: a grid of system icons, each with a checkmark (included) or X (excluded). The included systems each have a miniature version of the coupling diagram showing their specific $\mathcal{O}$ and $\mathcal{A}$. The excluded systems show the missing element: pure math has no environment box, deterministic systems have no fog in the environment, passive observers have no downward arrow.

> **Notation**: $\mathcal{S}_{\text{TFT}}$ (calligraphic S) is the set of all agent-environment pairs where TFT applies — the theory's scope. The curly braces $\{\ldots\}$ define a set by listing its conditions. $\mathcal{O}$ (calligraphic O) is the observation space — the set of all possible signals the agent can receive. $\neq \emptyset$ means "is not empty" — at least one observation type exists. $\mathcal{A}$ (calligraphic A) is the action space — the set of all actions available to the agent. $H(\Omega_t \mid \mathcal{H}_t)$ is conditional Shannon entropy: a non-negative number measuring how much uncertainty about $\Omega_t$ remains after conditioning on the full interaction history $\mathcal{H}_t = (o_1, a_1, o_2, a_2, \ldots, o_t)$. When $H = 0$, the history tells you everything — the problem is trivial. When $H > 0$, the world retains secrets no matter how much you've observed. TFT lives in the $H > 0$ world.

---

## Slide 4: The Arrow of Time

# THE ARROW OF TIME

### TF-02 — Axiom (the theory's only axiom)

$$\mathcal{H}_t = (o_1, a_1, o_2, a_2, \ldots, a_{t-1}, o_t)$$

This ordering is **irreversible**.

$a_{t-1}$ was chosen **before** $o_t$ was received.

The agent **could not** have used $o_t$ to choose $a_{t-1}$.

This isn't notation. It's physics.

**Visualization**: A bold horizontal arrow pointing right (the timeline). Above the arrow: observation dots (o₁, o₂, o₃) at their temporal positions. Below: action dots (a₁, a₂, a₃). Each action dot has a forward-facing "causal cone" — a shaded triangle extending rightward, showing that it can only influence future events. The key visual: the cones never extend backward. Below the timeline, two labels with arrows: "← MISMATCH (retrospective)" and "ACTION (prospective) →."

> **Notation**: $\mathcal{H}_t$ is the interaction history — the complete ordered record of every observation and action up to time $t$. The subscript $t$ indexes time; $o_t$ is the observation at $t$, $a_{t-1}$ is the action taken just before $o_t$ arrived. The ordering is not a modeling choice — it reflects the irreversible physical fact that causes precede effects. This asymmetry is the foundation of everything that follows. Mismatch is retrospective: comparing a prediction made before an observation with the observation that arrived after. Action is prospective: using the current model to influence future events.

---

## Slide 5: Three Levels of Knowing

# THREE LEVELS OF EPISTEMIC ACCESS

### Pearl's Causal Hierarchy, Grounded in Temporal Structure

**Level 1 — Association**: $P(o_t \mid \mathcal{H}_{<t})$ — *What will I observe?*

**Level 2 — Intervention**: $P(o_t \mid do(a_{t-1}), M_{t-1})$ — *What if I* do *this?*

**Level 3 — Counterfactual**: $P(o_t^{a'} \mid a, o)$ — *What* would *have happened?*

### Causal Information Yield (CIY):

$$\text{CIY}(a; M) = \mathbb{E}_{a' \sim q}\!\left[D_{\text{KL}}\!\left(P(o \mid do(a), M) \,\|\, P(o \mid do(a'), M)\right)\right] \geq 0$$

**The feedback loop's unique contribution**: by acting and observing, the agent gains Level 2 access — causal information that no amount of passive observation can provide.

**Visualization**: Three stacked layers, increasingly deep/illuminated. Top layer (pale): a flat scatter plot — "correlation, pattern." Middle layer (vivid, orange): a hand pulling a lever, gears turning — "intervention, causal mechanism." Bottom layer (bright): a forking path — the road taken (solid) and the road not taken (ghostly) — "counterfactual." A vertical axis on the right: "Increasing epistemic depth ↓." CIY is positioned between Levels 1 and 2 as the bridge.

> **Notation**: $P(o_t \mid \mathcal{H}_{<t})$ is a conditional probability — "the probability of observing $o_t$ given everything that happened before $t$." The $do(\cdot)$ operator is Pearl's intervention operator — it distinguishes "what will I see if I *do* this" (causal) from "what tends to follow this in the historical record" (correlational). $P(o_t^{a'} \mid a, o)$ is a counterfactual probability — "what *would* I have observed under action $a'$, given that I actually did $a$ and saw $o$." CIY — Causal Information Yield — measures how much an action $a$ reveals about the causal structure: it's the expected KL divergence (a measure of distributional difference) between the outcome of doing $a$ versus doing alternatives drawn from a reference distribution $q$. CIY is always ≥ 0: zero for passive observers, positive when actions causally alter what is observed. $D_{\text{KL}}$ is the Kullback-Leibler divergence — it quantifies how different two probability distributions are.

---

## Slide 6a: The Model — Compression

# THE MODEL

### TF-03 — Formulation

$$M_t = \phi(\mathcal{H}_t) \in \mathcal{M}$$

The model is a **compression** of the interaction history. It is the agent's **only** knowledge.

**Visualization**: ZOOMS INTO the agent box from Slide 3a's diagram. The 3a reference is shown small in the corner.

Inside the agent box, the compression is shown as a visual pipeline:

**LEFT** (sprawling, large): The full interaction history $\mathcal{H}_t = (o_1, a_1, o_2, a_2, \ldots, o_t)$ — drawn as a long, dense timeline of many events, growing over time. This is everything the agent has ever seen and done. It gets longer with every timestep.

**FUNNEL** (labeled $\phi$): A compression funnel connecting the history to the model. The funnel narrows from left to right — many events compress into a compact representation. The symbol $\phi$ is printed ON the funnel.

**RIGHT** (compact, small): The model state $M_t$ — a compact box. Its size depends on the model space $\mathcal{M}$:

| $\mathcal{M}$ | Size of box | Instance |
|---|---|---|
| $\mathbb{R}^3$ | Tiny (3 numbers) | PID controller |
| $\mathbb{R}^n \times \mathbb{S}^n_{++}$ | Small (state + covariance) | Kalman filter |
| $\Delta(\Theta)$ | Medium (distribution over parameters) | Bayesian agent |
| Neural network weights | Large (millions of parameters) | Deep learning agent |
| (Culture, procedures, beliefs) | Variable | Organization |

Show the boxes at DIFFERENT sizes to convey that model spaces vary enormously — from a PID's 3 numbers to a neural network's millions of weights to an organization's culture. All are compressions of $\mathcal{H}_t$. The compression ratio varies but the structure — history compressed into model — is universal.

> **Notation**: $M_t$ is the model state at time $t$ — the agent's entire internal representation. The subscript $t$ means it changes over time (each new event potentially updates it). $\mathcal{M}$ (calligraphic M) is the model space — the set of all models the agent COULD represent. Think of it as the container's shape: a PID controller's model space is $\mathbb{R}^3$ (three real numbers — that's all it can hold), while a neural network's model space is all possible weight configurations. $\phi$ (lowercase Greek phi) is the compression function — the mapping from the full history $\mathcal{H}_t$ (which grows without bound) to the compact model $M_t$ (which has fixed capacity). The formula $M_t = \phi(\mathcal{H}_t) \in \mathcal{M}$ says: the model is the result of compressing the history, and the result lives in the model space. The "$\in$" means "is an element of" — $M_t$ is one specific model within the space of possible models $\mathcal{M}$.

---

## Slide 6b: The Model — Sufficiency and Recursive Update

# WHAT MAKES A MODEL GOOD?

### TF-03 — Sufficiency

**Sufficiency** — does the model capture what matters for prediction?

$$S(M_t) = 1 - \frac{I(\mathcal{H}_t;\, o_{t+1:\infty} \mid M_t, a_{t:\infty})}{I(\mathcal{H}_t;\, o_{t+1:\infty} \mid a_{t:\infty})} \in [0,1]$$

When $S \approx 1$ — the **recursive update** becomes possible:

$$M_t = f(M_{t-1}, o_t, a_{t-1})$$

**Visualization**: Two parts:

**TOP — Sufficiency gauge**: A horizontal bar divided into two regions. The LEFT region (orange, labeled "What $M_t$ captures") represents the predictive information the model retains — $I(\mathcal{H}_t; \text{future} \mid a) - I(\mathcal{H}_t; \text{future} \mid M_t, a)$. The RIGHT region (gray, labeled "What $M_t$ misses") represents predictive information lost in compression — $I(\mathcal{H}_t; \text{future} \mid M_t, a)$. The ratio $S(M_t)$ is the orange fraction. Show it as a gauge reading ~0.85. Label: "S = 1 means nothing predictive was lost. S = 0 means the model captured nothing useful."

**BOTTOM — The recursive update machine**: A diagram showing the update function $f$ as a box with three inputs and one output. Inputs (arrows entering from left, top, and bottom): $M_{t-1}$ (the previous model — labeled "what I knew"), $o_t$ (the new observation — labeled "what I just saw"), $a_{t-1}$ (the last action — labeled "what I just did"). Output (arrow exiting right): $M_t$ (the updated model — labeled "what I now know"). The key annotation: "This only works when $S \approx 1$. Otherwise you need to reprocess the FULL history $\mathcal{H}_t$ — which grows without bound."

The connection to Slide 3a: the $o_t$ input is the same observation arrow from the agent-environment diagram; the $a_{t-1}$ input is the previous action arrow.

> **Notation**: $S(M_t)$ is model sufficiency — a number between 0 and 1. The formula looks complex but its meaning is simple: the numerator $I(\mathcal{H}_t; o_{t+1:\infty} \mid M_t, a_{t:\infty})$ is the mutual information between the history and the future that the model FAILS to capture — the predictive information lost in compression. The denominator $I(\mathcal{H}_t; o_{t+1:\infty} \mid a_{t:\infty})$ is the TOTAL predictive information in the history. $S = 1 - (\text{lost}/\text{total})$ — so $S = 1$ means nothing predictive was lost, $S = 0$ means everything was. The notation $o_{t+1:\infty}$ means "all future observations from $t+1$ onward" and $a_{t:\infty}$ means "all future actions." The recursive update $M_t = f(M_{t-1}, o_t, a_{t-1})$ is the payoff of sufficiency: if the model captured everything predictive, you only need three inputs — old model, new observation, last action — to compute the new model. No need to store or reprocess the growing history. This is what makes real-time adaptation physically possible. The function $f$ is the update function — in a Kalman filter it's the predict-then-correct cycle; in RL it's the TD update; in a Bayesian agent it's the posterior update.

---

## Slide 7: The Information Bottleneck

# THE COMPRESSION TRADEOFF

### TF-03 — Information Bottleneck

$$\phi^* = \arg\min_{\phi} \left[ \underbrace{I(M_t; \mathcal{H}_t)}_{\text{compression cost}} - \beta \cdot \underbrace{I(M_t; o_{t+1:\infty} \mid a_{t:\infty})}_{\text{predictive power}} \right]$$

**Visualization**: A rate-distortion curve where the AXES ARE THE FORMULA TERMS:

**X-axis**: $I(M_t; \mathcal{H}_t)$ — labeled "Compression cost: how much history the model retains." Moving right on this axis means the model keeps more of the history — richer representation, but more expensive. Units: bits (or nats) of information about the history.

**Y-axis**: $I(M_t; o_{t+1:\infty} \mid a_{t:\infty})$ — labeled "Predictive power: how much the model can predict about the future." Moving up means the model predicts better. Units: bits of information about future observations.

**The Pareto frontier**: A concave curve showing the tradeoff. Every point on this curve is an optimal $\phi$ for some value of $\beta$. Points below the curve are suboptimal (compress the same amount but predict less). Points above are impossible (can't predict that well with that much compression).

**$\beta$ as slope**: At any point on the curve, $\beta$ is the slope of the tangent — it's how much additional predictive power you get per unit of additional compression cost. High $\beta$ → steep slope → you're willing to pay a lot in compression cost for a little more prediction (right side of curve). Low $\beta$ → shallow slope → you're compressing aggressively (left side).

**Labeled points on the curve**:
- **Far left** (extreme compression): "PID controller — $\mathbb{R}^3$ state. Retains almost nothing. Sufficient for simple dynamics."
- **Middle**: "Kalman filter — state + covariance. Balanced."
- **Far right** (maximal retention): "Full Bayesian — rich posterior. Dense memory."

**Environmental volatility overlay**: TWO versions of the curve shown (one solid, one dashed):
- **High $\rho$** (volatile, dashed): The curve is lower and shifted left — at any compression level, the predictive power is less because historical detail goes stale fast. The optimal operating point shifts LEFT. Label: "Volatile world → compress hard."
- **Low $\rho$** (stable, solid): The curve is higher — historical detail retains predictive value. The optimal point shifts RIGHT. Label: "Stable world → retain detail."

> **Notation**: $\phi^*$ is the optimal compression function — the $\phi$ from Slide 6a that minimizes this objective. $\arg\min_\phi$ means "the $\phi$ that minimizes the expression in brackets." $I(M_t; \mathcal{H}_t)$ is the mutual information between the model and the history — the x-axis of the curve. Informally: how much the model "remembers" about the history. A PID controller with 3 numbers has very low $I(M;\mathcal{H})$; a neural network with millions of weights has very high. $I(M_t; o_{t+1:\infty} \mid a_{t:\infty})$ is the mutual information between the model and all future observations conditioned on actions — the y-axis. Informally: how well the model can predict what's coming. The conditioning on $a_{t:\infty}$ means "given whatever actions the agent might take" — separating predictive power from action choice. $\beta$ (beta) is the tradeoff parameter. In the formula, it multiplies the predictive power term — so higher $\beta$ penalizes low prediction more, pushing toward richer models. On the graph, it's the slope at the operating point. $\rho$ (rho, previewing TF-11) is the environment change rate. It determines which curve you're on — volatile environments reduce the value of retained detail, shifting the entire frontier leftward. The key insight: the PID controller and the Bayesian posterior sit on the SAME curve. Neither is universally better. Each is optimal for a different $\rho$ regime.

---

## Slide 8: Events on Channels

# EVENT-DRIVEN DYNAMICS

### TF-04

Events arrive on **multiple channels** at **different rates**:

$$M_{\tau^+} = f(M_{\tau^-}, e_\tau)$$

Each channel has rate $\nu^{(k)}$ and reliability $U_o^{(k)}$.

**Event information content** — how much an event tells you beyond what you already expected:

$$\mathcal{I}(e_\tau) = I(e_\tau;\, \Omega_\tau \mid M_{\tau^-})$$

Expected events → low $\mathcal{I}$. Surprises → high $\mathcal{I}$.

*Between events, the model state may evolve autonomously — prediction, simulation, decay — or remain static.*

**Visualization**: A multi-track sequencer/timeline. Four horizontal tracks (channels) with event blips at different densities: "Vision (30 Hz)" — dense blips; "Audio (variable)" — irregular blips; "Collaborator (0.01 Hz)" — rare blips; "Internal timer (configured)" — regular, evenly-spaced blips. Each blip has a height proportional to its information content I(e_τ). Below all tracks: a model-state bar that shifts at each event, with larger shifts for taller blips. Key visual: the rare collaborator message produces the tallest blip (most informative per event), while dense vision frames produce small blips each.

> **Notation**: $e_\tau$ is an event occurring at continuous timestamp $\tau$ (as opposed to the discrete time index $t$). $M_{\tau^-}$ and $M_{\tau^+}$ are the model state just before and just after an event — the instantaneous update. $\nu^{(k)}$ is the event rate (in Hz) on channel $k$ — how often observations arrive on that channel. $U_o^{(k)}$ is the observation uncertainty specific to channel $k$ — how noisy that channel is. $\mathcal{I}(e_\tau) = I(e_\tau; \Omega_\tau \mid M_{\tau^-})$ is the event information content — the mutual information between the event and the true environment state, conditioned on the current model. High $\mathcal{I}$ means the event is surprising (the model didn't predict it); low $\mathcal{I}$ means it was expected. This is the formal foundation for the attention problem: which events deserve deep processing?

---

## Slide 9: Agent Identity (Discussion)

# THE SINGULAR CAUSAL TRAJECTORY

### TF-02 — Discussion

The interaction history $\mathcal{H}_t$ is **unique and non-forkable**.

If $M_t$ is a sufficient statistic for $\mathcal{H}_t$, and $\mathcal{H}_t$ is a singular temporal sequence, then $M_t$ represents a **singular causal trajectory**.

### The Clone Problem:

Copy $M_t$ exactly. Two identical copies. But the **very next event** — a different user, a different observation — creates two **divergent, irreversible** causal trajectories.

$$\mathcal{H}_{t+1}^{(1)} \neq \mathcal{H}_{t+1}^{(2)}$$

Neither copy's future model is a sufficient statistic for the other's trajectory.

**Identity is not the model state** (which can be copied) **but the singular causal trajectory** (which cannot).

A copy shares a **prefix** of the original's history — like a sibling sharing childhood — not the trajectory itself.

**Visualization**: A timeline that reaches a fork point labeled "COPY." Two branches diverge rightward from this point, each with its own subsequent events (different colored dots). The shared prefix (before the fork) is drawn as a single solid line. After the fork: two parallel but diverging lines, each accumulating different events. At the bottom: "Shared prefix ≠ shared identity. The trajectory is the identity."

> TFT has a specific implication for identity. An agent's causal history is unique and non-forkable. You can copy the model state — the weights, the parameters. But the very next event creates two divergent causal trajectories. Neither copy's model is a sufficient statistic for the other's history. Within TFT's formalism, identity is not the snapshot but the trajectory. A copy is a sibling who shares early childhood, not a continuation.

---

## Slide 10: The Mismatch Signal

# THE MISMATCH SIGNAL

### TF-05 — The Fundamental Driver

The model **predicts**: $\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$

Reality **delivers**: $o_t$

The **mismatch**: $\delta_t = o_t - \hat{o}_t$

**Visualization**: A ZOOM INTO the observation arrow from Slide 3a's agent-environment diagram. The full 3a diagram is shown small in the corner for reference; the observation arrow is enlarged to fill the slide.

The zoomed view shows:

**INSIDE THE AGENT BOX** (left): The model $M_{t-1}$ generates a prediction — a dashed orange line extending rightward from the agent toward where it expects the observation to land. This line is labeled $\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$ and terminates at a hollow orange circle — "where the model thinks reality will be."

**FROM THE ENVIRONMENT** (right): The actual observation $o_t$ travels along the observation arrow toward the agent. It arrives as a solid dark dot — "where reality actually is."

**THE GAP** between the hollow circle ($\hat{o}_t$) and the solid dot ($o_t$) is highlighted with an orange bracket labeled: $\delta_t = o_t - \hat{o}_t$

This gap is the mismatch signal. It is the "active ingredient" — the thing that drives ALL model adaptation.

Three instances shown (stacked or side by side):
- **Small gap** (prediction nearly matched): small $\|\delta_t\|$ → "Model predicted well. Small update."
- **Large gap** (prediction missed): large $\|\delta_t\|$ → "Model was wrong. Significant update."
- **No gap** (perfect prediction): $\delta_t = 0$ → "Nothing to learn. (But see Slide 12 — this may be a trap.)"

Below: the domain mapping — each domain's name for this same gap:

| Kalman | RL | Bayesian | PID | Boyd | Immune | Science |
|---|---|---|---|---|---|---|
| Innovation | TD error | Surprise | Error signal | Disorientation | Unknown antigen | Anomaly |

> **Notation**: $\hat{o}_t$ (read "o-hat sub t") is the model's prediction — the expected value $\mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$. The $\mathbb{E}[\cdot]$ means "expected value" — what the model thinks is most likely to happen. The conditioning bar "$\mid$" means "given": given the model state $M_{t-1}$ and the last action $a_{t-1}$. The hat ^ always means "predicted" or "estimated" in TFT. $o_t$ (no hat) is what actually arrives — the real observation. $\delta_t$ (lowercase Greek delta, subscript $t$) is their difference — the mismatch signal. Visually in the diagram: the gap between where the model thought the observation would be (hollow circle) and where it actually is (solid dot). $\|\delta_t\|$ (with double bars) is the magnitude of this gap — how big the surprise is, regardless of direction. This single quantity drives everything that follows: the gain (Slide 13a) determines how the model responds to it; the persistence threshold (Slide 23b) depends on how fast new mismatch accumulates.

---

## Slide 11: Mismatch Inevitability

# MISMATCH IS INEVITABLE

### Proposition 5.1

$$\mathbb{E}[\|\delta_t\|^2] = \underbrace{\mathbb{E}[\|\hat{o}_t - \bar{o}_t\|^2]}_{\text{MODEL ERROR} \atop \text{(reducible)}} + \underbrace{\mathbb{E}[\text{Var}(o_t \mid \Omega_t, a_{t-1})]}_{\text{OBSERVATION NOISE} \atop \text{(irreducible)}}$$

You can improve your model (shrink term 1).

You **cannot** eliminate observation noise (term 2).

**An agent that tries to drive all mismatch to zero will overfit** — adjusting its model to explain noise, degrading future predictions.

**Visualization**: A horizontal stacked bar that evolves over time (shown as several snapshots). The dark segment (irreducible noise) stays constant. The orange segment (model error) shrinks as the model improves. In the final snapshot, the orange segment is tiny but the dark segment remains. A red "danger zone" extension below zero is labeled "OVERFITTING: trying to explain noise as signal" — shown as the model error going negative (impossible, but the attempt distorts the model).

> **Notation**: $\mathbb{E}[\|\delta_t\|^2]$ is the expected squared magnitude of the mismatch — the average squared surprise. The double bars $\|\cdot\|$ denote the norm (magnitude/length) of the mismatch vector. $\bar{o}_t = \mathbb{E}[o_t \mid \Omega_t, a_{t-1}]$ is the *true* conditional mean — what you'd predict if you could see the actual environment state $\Omega_t$ (which you can't). The first term $\|\hat{o}_t - \bar{o}_t\|^2$ is the gap between the model's prediction and the true mean — this is model error, reducible by improving the model. The second term $\text{Var}(o_t \mid \Omega_t, a_{t-1})$ is the observation noise variance — the randomness in the observation channel itself, irreducible no matter how good the model. An agent that tries to drive total mismatch below this noise floor will overfit: adjusting its model to explain noise, degrading future predictions.

---

## Slide 12: The Zero-Mismatch Trap

# THE ZERO-MISMATCH TRAP

### TF-05 — When Low δ Doesn't Mean Good Model

$\delta_t \approx 0$ could mean three things:

**(a) Accurate model** — predictions genuinely match reality ✓

**(b) Confirmation bias** — only testing what you already know ✗

**(c) Low resolution** — instruments can't detect errors ✗

### The cure: **Active testing**

Choose actions specifically to generate informative mismatch signals.

Or query someone whose model differs from yours.

**Visualization**: Three "windows" side by side, each showing an agent's view of the world. (a): Clean, clear view — model matches reality. (b): Agent looking through a narrow tube — everything visible matches, but vast areas are unseen (tunnel vision). (c): Agent looking through frosted glass — can't see enough detail. Each panel is labeled with its status: ✓, ✗, ✗. Below: a figure choosing to look in a new direction (breaking out of the tunnel) — labeled "CIY-driven exploration."

> Low mismatch feels good. But it might mean you're not testing your model. Case (b) is confirmation bias — you're only observing things your model already explains. The remedy is acting specifically to generate observations that would test your model where it's weakest. This is why exploration matters — and why query actions can be so powerful. An expert with a different model can reveal blind spots you'd never find on your own.

---

## Slide 13a: The Uncertainty Ratio — Visual

# THE UNCERTAINTY RATIO

### TF-06 — What the Gain Looks Like

Total uncertainty about the next observation has two parts:

$$\underbrace{\quad U_M \quad}_{\text{model uncertainty}} + \underbrace{\quad U_o \quad}_{\text{observation uncertainty}} = \text{total uncertainty}$$

The gain $\eta^*$ is **the fraction that belongs to the model**:

$$\boxed{\eta^* = \frac{U_M}{U_M + U_o}}$$

**Visualization**: A single horizontal bar divided into two colored segments. The LEFT segment is orange, labeled $U_M$ — the model's own uncertainty about what it's about to see. The RIGHT segment is dark/gray, labeled $U_o$ — the noise in the observation channel. A bracket above the orange segment is labeled "$\eta^*$ = this fraction of the whole bar."

Three versions of the bar stacked vertically:

**Top bar**: $U_M$ is ~80% of the bar, $U_o$ is ~20%. The $\eta^*$ bracket spans most of the bar. $\eta^* \approx 0.8$. Label: "Model very uncertain, observation clean → **trust the data**"

**Middle bar**: $U_M$ ≈ $U_o$, each ~50%. $\eta^* \approx 0.5$. Label: "**Split the difference**"

**Bottom bar**: $U_M$ is ~15%, $U_o$ is ~85%. The $\eta^*$ bracket is a thin sliver. $\eta^* \approx 0.15$. Label: "Model confident, observation noisy → **trust the model**"

Key: as the orange segment shrinks (model becomes more confident), $\eta^*$ shrinks — the model becomes more resistant to observations. As it grows, $\eta^*$ grows — the model becomes more responsive. The formula IS the proportion.

> **Notation**: $U_M$ (model uncertainty) is the variance — the spread — of the model's own predictive distribution. Formally: $U_M = \text{Var}_{M_{t-1}}[\hat{o}_t \mid a_{t-1}]$. When $U_M$ is large, the model "doesn't know what's coming" — its predictions are spread over a wide range. When small, the model has a precise expectation. $U_o$ (observation uncertainty) is the variance of the observation noise $\varepsilon_t$ — how much the channel distorts the true signal. The formula $\eta^* = U_M/(U_M + U_o)$ is a ratio — geometrically, it's the orange proportion of the bar. This single visual encodes the formula and its behavior: the ratio IS the proportion. When the orange is most of the bar ($U_M \gg U_o$), $\eta^* \to 1$ — trust the data. When the gray is most ($U_M \ll U_o$), $\eta^* \to 0$ — trust the model. This ratio reappears throughout TFT: in tempo ($\mathcal{T} = \nu \cdot \eta^*$), communication gain, and adversarial dynamics. Every time you see $\eta^*$, picture this bar.

---

## Slide 13b: The Gain as Movement

# THE GAIN AS MOVEMENT

### TF-06 — What the Update Looks Like

$$M_t = M_{t-1} + \eta^* \cdot g(\delta_t)$$

In one dimension: the model **moves toward the observation** by fraction $\eta^*$ of the gap.

**Visualization**: A horizontal number line. Two points are marked:

- **Orange dot** (left): $M_{t-1}$ — the model's current position (its prediction $\hat{o}_t$)
- **Dark dot** (right): $o_t$ — where reality actually landed

The gap is labeled: "$\delta_t = o_t - \hat{o}_t$" (the mismatch from Slide 10).

Three copies of this number line, stacked, each showing a different η*:

**Line 1** ($\eta^* = 0.85$): The new model $M_t$ (shown as a new orange dot) jumps almost all the way to $o_t$. A small uncertainty-ratio bar is shown beside this line, with a large orange segment. Label: "Model uncertain → large move."

**Line 2** ($\eta^* = 0.5$): $M_t$ moves halfway. The companion bar is evenly split.

**Line 3** ($\eta^* = 0.1$): $M_t$ barely budges from $M_{t-1}$. The companion bar has a tiny orange sliver. Label: "Model confident → small move."

The key: **$\eta^*$ is the fraction of the gap the model closes.** The companion uncertainty-ratio bar from 13a shows WHY it closes that fraction — because that's how uncertain the model is relative to observation noise.

> **Notation**: The update rule $M_t = M_{t-1} + \eta^* \cdot g(\delta_t)$ says the new model is the old model shifted by a gain-weighted correction. $g(\delta_t)$ is the mismatch transform — a function that maps the raw mismatch from observation space into the model's update space. In the simplest 1D case, $g$ is the identity and the update is just $M_t = M_{t-1} + \eta^* \cdot \delta_t$: the model moves fraction $\eta^*$ of the way toward the observation. In a Kalman filter, $g = H^T$ (the transpose of the observation matrix, mapping from observation space to state space). The visual encodes the formula directly: $\eta^*$ controls how far the orange dot moves. Near 1 → jumps to the data. Near 0 → barely budges. The companion bar shows the cause: the movement fraction equals the uncertainty fraction.

---

## Slide 14: Gain Across Domains

# SAME STRUCTURE, DIFFERENT NAMES

### TF-06 — Domain Validation

| Domain | Gain Formula | Maps to η* = U_M/(U_M+U_o)? |
|--------|-------------|-------------------------------|
| **Kalman filter** | $K_t = P_{t|t-1}(P_{t|t-1} + R)^{-1}$ | **Exact** ✓ |
| **Bayesian posterior** | $w_{\text{new}} = 1/(n+\kappa)$ | **Exact** ✓ |
| **RL** (Q-learning) | $\alpha = \text{const}$ | **Degenerate** — fixed, not adaptive |
| **PID control** | $(K_p, K_i, K_d) = \text{const}$ | **Frozen** — calibrated once |
| **Adam optimizer** | Per-parameter adaptive step | **Approximate** — approaching the form |

The progression from fixed PID → adaptive Adam → Kalman gain tracks the progression toward the full uncertainty ratio.

**Visualization**: A spectrum/progression arrow from left to right. Left end: "Fixed gain (PID)" — a single static dial. Middle: "Adaptive gain (Adam, UCB)" — a dial that adjusts. Right end: "Optimal gain (Kalman)" — a dial that tracks uncertainty perfectly. Each position is labeled with its domain. The arrow is labeled "Progression toward η* = U_M/(U_M+U_o)."

> **Notation**: In the Kalman row: $K_t$ is the Kalman gain, $P_{t|t-1}$ is the prior predictive state variance (= $U_M$), and $R$ is the measurement noise variance (= $U_o$). The formula $K_t = P_{t|t-1}/(P_{t|t-1} + R)$ is literally $U_M/(U_M + U_o)$ — an exact identity. In the Bayesian row: $n$ is the number of data points seen, $\kappa$ is the prior's effective sample size (prior strength). The weight on each new datum, $1/(n+\kappa)$, decreases as $n$ grows — the model becomes more resistant to individual observations. In RL: $\alpha$ is the fixed learning rate — a constant that doesn't adapt to the agent's uncertainty state. In PID: $(K_p, K_i, K_d)$ are the proportional, integral, and derivative gains, fixed at design time. The progression from PID (frozen) → RL (constant) → Adam (per-parameter adaptive) → Kalman (fully optimal) tracks increasing sophistication in gain calibration.

---

## Slide 15: Gain Dynamics

# GAIN DYNAMICS

### TF-06 — How η* Changes Over Time

**Convergence**: Model improves → $U_M$ ↓ → $\eta^*$ ↓ → more resistant to noise

**Reset**: Environment shifts → $U_M$ should spike → $\eta^*$ ↑ → rapid relearning

**Failure to reset**: **Incestuous amplification** — the model ignores contradicting evidence because it's too confident.

### Overfitting as gain miscalibration:

| η* too high | Overreacts to noise → model thrashes |
|---|---|
| **η* too low** | **Ignores signal → model stagnates** |

**Visualization**: A time-series plot. η*(t) starts high (~0.8), curves down to steady state (~0.15). At a vertical dashed line labeled "REGIME CHANGE," a healthy agent's η* spikes back to ~0.7, then reconverges. A brittle agent's η* (red dashed line) stays flat through the regime change — and a separate line shows its mismatch diverging upward. Labels: "Healthy: admits uncertainty, relearns" vs. "Brittle: ignores the shift, fails."

> Gain dynamics matter as much as the gain itself. Early on, high gain — fast learning. As you converge, lower gain — you trust your model. But when the world fundamentally changes, the gain must reset. An agent that doesn't reset keeps trusting a stale model against contradicting evidence. Boyd called this incestuous amplification. It's the cause of brittle failure.

---

## Slide 16: The Complete Loop

# THE COMPLETE FEEDBACK LOOP

### Everything from Slides 3–15, assembled.

**Orient is the Schwerpunkt** — the center of gravity. Everything else serves orientation.

**Visualization**: A large blueprint schematic showing the feedback loop. This is the SYNTHESIS SLIDE — each component references its source slide. The layout is a four-phase cycle:

**OBSERVE** (top-left, small box): An event $e_\tau$ arrives on a channel (Slide 8). The observation $o_t$ enters the agent from the environment — this IS the upward arrow from Slide 3a, now annotated.

**ORIENT** (top-right, LARGE box — 3× bigger than others, thick orange border): This is where the mismatch and gain operate. Inside the ORIENT box, four sub-operations are shown, each referencing its slide:

1. **Predict** $\hat{o}_t$ — the hollow orange circle from Slide 10 (model generates expectation)
2. **Mismatch** $\delta_t = o_t - \hat{o}_t$ — the gap from Slide 10 (prediction vs. reality)
3. **Gain** $\eta^* = U_M/(U_M + U_o)$ — the uncertainty-ratio bar from Slide 13a (how much to trust the new data). A small version of the partitioned bar is shown.
4. **Update** $M_t = M_{t-1} + \eta^* \cdot g(\delta_t)$ — the movement on the number line from Slide 13b (model shifts toward observation). A small version of the number line is shown.

**DECIDE** (bottom-right, medium box): $a_t = \pi(M_t)$ — action selected from the updated model (Slide 17). The fluency spectrum (reflex ↔ deliberation) is shown as a small bar.

**ACT** (bottom-left, small box): Action $a_t$ executed — this IS the downward arrow from Slide 3a, now annotated. Result becomes new observation → loop back to OBSERVE.

Arrows connect the boxes in sequence: OBSERVE → ORIENT → DECIDE → ACT → OBSERVE. The arrow from ACT back to OBSERVE closes the loop.

**Corner annotation**: The full 3a agent-environment diagram shown small, with the four loop phases mapped onto it — OBSERVE on the upward arrow, ACT on the downward arrow, ORIENT and DECIDE inside the agent box.

> **Notation recap**: This slide has no new notation — it assembles what's been introduced. $o_t$ (observation, Slide 3a) enters the loop. $\hat{o}_t$ (prediction, Slide 10) is generated from $M_{t-1}$. $\delta_t$ (mismatch, Slide 10) is their difference. $\eta^*$ (gain, Slide 13a) determines how much the model shifts. $M_t$ (updated model, Slide 13b) moves toward the observation by fraction $\eta^*$. $\pi(M_t)$ (policy, Slide 17) selects the action $a_t$. The action generates new observations and the loop continues. Orient is where all the mathematics lives — predict, surprise, weight, update. The other three phases are data flow: observation in, action out, consequences back in. Boyd called Orient the Schwerpunkt — the decisive point. TFT makes precise why: it's where mismatch drives gain-weighted model updating. Everything else serves this.

---

## Slide 17: Action and Fluency

# ACTION FLUENCY

### TF-07 — From Reflex to Deliberation

$$a_t = \pi(M_t)$$

Action is a function of the model. But **how** it's computed varies:

**High fluency** (implicit): action flows directly, cheaply.
*Reflexes, expert intuition, System 1, IG&C, well-tuned PID.*

**Low fluency** (explicit): internal simulation required.
*Strategic planning, System 2, MCTS, Boyd's full Decide step.*

Formal characterization: high fluency ⟺ $\Delta\eta^*(\Delta\tau) \approx 0$
*(More thinking time wouldn't help.)*

### Pressure toward fluency:
High ρ, frequent patterns, near persistence threshold → **internalize**.
Novel, high-stakes, low ρ → **deliberate**.

**Visualization**: A horizontal spectrum bar. Left: "REFLEX" (lightning bolt icon, label "Δτ ≈ 0"). Right: "DELIBERATION" (chess piece icon, label "Δτ large"). Markers along the spectrum: reflex → instinct → habit → expertise → intuition → planning → strategy. Arrows: "High ρ pushes ← toward reflex" and "Novel/high-stakes pushes → toward deliberation."

> **Notation**: $a_t = \pi(M_t)$ says action is a function $\pi$ (pi, the policy) of the model state. Whatever the agent does comes from what it "knows." $\Delta\eta^*(\Delta\tau)$ is the gain improvement achievable from $\Delta\tau$ additional deliberation time. When this quantity is near zero for all $\Delta\tau > 0$, more thinking wouldn't improve the action — high fluency. When $\Delta\eta^*$ is large for short $\Delta\tau$, deliberation pays — low fluency. Selective pressure toward fluency: high $\rho$ (fast environments penalize delay), frequent patterns (amortize internalization cost), near persistence threshold (no slack for overhead). But deliberation remains essential for novel situations, large action spaces, and asymmetric stakes.

---

## Slide 18: Exploration and Query Actions

# ACTIONS GENERATE INFORMATION

### TF-08 — Exploration-Exploitation

$$\pi^*(M_t) = \arg\max_a \left[\underbrace{\mathbb{E}[\text{value}]}_{\text{exploit}} + \underbrace{\lambda(M_t) \cdot \text{CIY}(a; M_t)}_{\text{explore}}\right]$$

### Query actions — orders of magnitude more efficient:

Measuring a building's height:
- Drop barometer, time the fall → **1 probe, low CIY**
- Measure shadow ratios → **1 probe, low CIY**
- **Offer barometer to janitor for the answer → 1 query, enormous CIY**

The janitor's model has **already compressed** the relevant information.

Query CIY depends on **trust**: source calibration ($U_{\text{src}}$) and alignment ($U_{\text{align}}$).

**Visualization**: Left panel: an agent poking an opaque box with a stick — sparse, thin arrows return (low CIY per probe). Right panel: an agent consulting a library/expert — a dense beam of information returns (high CIY per query). The width contrast is dramatic. Below: the barometer comic strip — three panels showing the three measurement methods, with CIY values overlaid. The janitor panel has CIY orders of magnitude larger.

> **Notation**: $\pi^*(M_t)$ is the optimal policy — the action choice that maximizes the combined objective. The first term $\mathbb{E}[\text{value}(a) \mid M_t]$ is the expected value of action $a$ given the current model — the exploitation term: do what you think is best. The second term $\lambda(M_t) \cdot \text{CIY}(a; M_t)$ is the exploration bonus: CIY measures how much causal information this action would generate (defined in Slide 5), and $\lambda(M_t)$ is a weighting coefficient that prices exploration in value-equivalent units. $\lambda$ is large when $U_M$ is high (much to learn) and small when $U_M$ is low (model already good). The $\arg\max_a$ means "choose the action $a$ that maximizes this combined objective." $U_{\text{src}}$ and $U_{\text{align}}$ (defined in Slide 27) capture whether a query source is calibrated and whether it shares your goals.

---

## Slide 19: The Cost of Deliberation

# THE COST OF DELIBERATION

### TF-09 — Proposition 9.1

Deliberation improves action quality. But **the world doesn't wait.**

$$\boxed{\Delta\eta^*(\Delta\tau) \cdot \|\delta_{\text{post}}\| > \rho_{\text{delib}} \cdot \Delta\tau}$$

*Gain improvement × problem magnitude must exceed drift during thinking.*

**Optimal deliberation duration** — stop when marginal gain = marginal cost:

$$\frac{\partial \Delta\eta^*}{\partial \Delta\tau} \cdot \|\delta_{\text{post}}\| = \rho_{\text{delib}}$$

The spectrum — same tradeoff at every timescale:

| Duration | Example | ρ·Δτ cost |
|----------|---------|-----------|
| 0 (reflex) | Catch a ball | Zero |
| Seconds | Tactical maneuver | Small |
| Hours | Strategic decision | Large |
| Months | **Structural adaptation** | **Massive** |

**Visualization**: Two curves on the same axes (x = deliberation time Δτ). Curve 1 (orange, concave, rising): "Benefit: Δη*·‖δ‖." Curve 2 (dark, linear, rising): "Cost: ρ·Δτ." They cross at Δτ* (marked with a star). Left of crossing: green zone (net benefit). Right: red zone (net loss). A callout: "Structural adaptation = deliberation with massive Δτ."

> **Notation**: $\Delta\tau$ (delta-tau) is the deliberation duration — how long the agent pauses to think before acting. $\Delta\eta^*(\Delta\tau)$ is the gain improvement — how much better the agent's next update will be thanks to $\Delta\tau$ of deliberation. $\|\delta_{\text{post}}\|$ is the magnitude of the mismatch the agent will face when it resumes acting. $\rho_{\text{delib}}$ is the local mismatch drift rate during the pause — how fast the world changes while the agent thinks. The threshold inequality says: the benefit (gain improvement × problem size) must exceed the cost (drift × time). The first-order optimality condition $\partial\Delta\eta^*/\partial\Delta\tau \cdot \|\delta_{\text{post}}\| = \rho_{\text{delib}}$ gives the optimal stopping point — deliberate until the marginal benefit of one more moment of thought equals the marginal cost of one more moment of inaction.

---

## Slide 20: Structural Adaptation

# WHEN THE FRAMEWORK IS WRONG

### TF-10 — Proposition 10.1

If $\mathcal{F}(\mathcal{M}) < 1 - \epsilon$, then **no parametric adaptation within $\mathcal{M}$** can reduce mismatch below a floor.

### Diagnostic symptoms:
1. **Persistent mismatch** despite convergence
2. **Confident but wrong** — gain collapsed, predictions still poor
3. **Structured residuals** — patterns in the errors the model can't absorb

### Mechanisms of structural change:

| Mechanism | Example |
|-----------|---------|
| **Decomposition + Recombination** | Boyd's snowmobile, Kuhn's paradigm shift |
| **Expansion** | Growing a neural network, adding a department |
| **Compression** | Regularization, organizational streamlining |
| **Grafting** | Transfer learning, hiring an expert |

**Visualization**: A mismatch time-series that decreases, then flatlines at a "MISMATCH FLOOR" well above zero. The floor is clearly labeled. Below the floor (dashed line): the achievable minimum with a richer model class M'. An arrow from the floor down to the dashed line: "Structural adaptation required." In the residuals panel: a clear sinusoidal pattern — "structured residuals the model class cannot represent."

> **Notation**: $\mathcal{F}(\mathcal{M})$ is model class fitness — the best sufficiency $S(M)$ achievable by any model in the class $\mathcal{M}$. Formally: $\sup_{M \in \mathcal{M}} S(M)$. When $\mathcal{F}(\mathcal{M}) < 1 - \epsilon$ (for some margin $\epsilon > 0$), the class itself is inadequate — no model in it can capture the environment's structure. $\Phi$ is the structural update function that maps from one model class to the next: $\mathcal{M}_{t+1} = \Phi(\mathcal{M}_t, \text{performance history})$. This is a different kind of change than parametric updating — it's changing what the model CAN represent, not just its current parameters. The symptoms of need: persistent mismatch that doesn't respond to further learning, structured patterns in the residuals that the model class has no way to absorb.

---

## Slide 21: Temporal Nesting

# TEMPORAL NESTING

### TF-11 — Multiple Adaptive Timescales

| Timescale | Process | What Changes |
|-----------|---------|-------------|
| **Fastest** | Reactive response | Action from current model |
| **Fast** | Parametric update | Model parameters within $\mathcal{M}$ |
| **Slow** | Structural adaptation | Model class $\mathcal{M}$ |
| **Slowest** | Architectural change | The agent's fundamental nature |

### The convergence constraint:

$$\nu_{\text{level } n+1} \ll \nu_{\text{level } n}$$

Each level must **approximately converge** before the next slower level responds.

**Violation**: acting on transients → oscillation, instability.

**Visualization**: Nested concentric rings (like tree rings). Innermost ring (spinning fast, labeled "reactive"): thin, bright orange. Next ring (slower, "parametric"): medium, darker. Next ("structural"): thick, dark. Outermost ("architectural"): very thick, barely moving, darkest. Between each pair: the constraint symbol ≪. Domain examples beside each ring: "PID: D→P→I terms" and "Biology: reflex→learning→development→evolution."

> **Notation**: $\nu_{\text{level }n}$ is the characteristic rate of adaptive process at level $n$ — how often that level updates. The constraint $\nu_{n+1} \ll \nu_n$ (read "much less than") means slower levels must operate at much lower rates than faster ones. This is the convergence constraint: each level must approximately converge — reach a quasi-stable state — before the next slower level acts on its output. If a slower process responds to transients from the faster process before they've settled, the result is oscillation and instability. In a PID controller: D-term (fastest, high-frequency), P-term (current error), I-term (slowest, accumulated bias). In biology: reflexes (ms), learning (min), development (yr), evolution (generations).

---

## Slide 22a: Adaptive Tempo — Building the Number

# ADAPTIVE TEMPO

### TF-11 — How Fast Can You Correct Your Model?

Each observation channel contributes to the agent's total adaptive capacity:

$$\boxed{\mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)*}}$$

**Visualization**: A stacked bar chart where each bar segment represents one channel's contribution to total tempo. Each segment has:
- **Width** = $\nu^{(k)}$ (channel event rate — how often events arrive on this channel, in Hz)
- **Height** = $\eta^{(k)*}$ (channel gain — how much each event on this channel improves the model, from 0 to 1. This is the uncertainty-ratio bar from Slide 13a, now turned on its side)
- **Area** = $\nu^{(k)} \cdot \eta^{(k)*}$ (this channel's contribution to tempo)

The total area across all segments = $\mathcal{T}$ (the adaptive tempo).

**Example with three channels** (concrete numbers labeled on the diagram):

| Channel $k$ | $\nu^{(k)}$ (rate) | $\eta^{(k)*}$ (gain) | Contribution |
|---|---|---|---|
| Camera (30 Hz, noisy) | 30 | 0.02 | 0.60 |
| Collaborator (0.1 Hz, reliable) | 0.1 | 0.70 | 0.07 |
| Internal timer (1 Hz, medium) | 1.0 | 0.15 | 0.15 |
| | | **Total $\mathcal{T}$** | **0.82 s⁻¹** |

Note: The camera has the highest rate but lowest gain (noisy → $U_o$ large → $\eta^*$ small per Slide 13a). The collaborator has the lowest rate but highest gain (reliable, high CIY). Each channel's gain is its own uncertainty-ratio bar from 13a.

Single-channel special case: $\mathcal{T} = \nu \cdot \eta^*$ — just rate times quality.

> **Notation**: $\mathcal{T}$ (calligraphic T — distinguished from italic $T$ used for the transition function on Slide 3a) is adaptive tempo — the effective rate at which the agent reduces model-reality mismatch. The unit is inverse time ($t^{-1}$, or Hz) — informally, "effective corrections per second." It's a sum over channels: $\sum_k$ means "add up over all observation channels $k$." For each channel: $\nu^{(k)}$ is the event rate in Hz (from Slide 8 — how often events arrive), and $\eta^{(k)*}$ is the optimal gain on that channel (from Slide 13a — the uncertainty ratio $U_M/(U_M + U_o^{(k)})$, which depends on the channel's noise level $U_o^{(k)}$). Their product $\nu^{(k)} \cdot \eta^{(k)*}$ is this channel's contribution to total tempo — visible as the area of its bar segment. A fast but noisy channel (high $\nu$, low $\eta^*$) can contribute the same as a slow but clean channel (low $\nu$, high $\eta^*$). This is where the gain visualization from 13a connects to the dynamics: each channel has its own uncertainty-ratio bar, and the orange fraction of that bar times the channel rate gives the contribution.

---

## Slide 22b: Speed-Quality Substitutability

# SPEED × QUALITY

### TF-11 — Boyd's Insight, Formalized

Since $\mathcal{T} = \nu \cdot \eta^*$ (single channel):

$$2\nu \cdot \eta^* = \nu \cdot 2\eta^*$$

Doubling speed has the same effect as doubling quality.

They are **multiplicative** when both improve:

$$1.5\nu \cdot 1.5\eta^* = 2.25 \cdot \nu\eta^*$$

**Boyd**: Orient quality ($\eta^*$) often matters **more** than loop speed ($\nu$) — because there's usually more room to improve quality.

**Visualization**: A 2D contour plot. X-axis: $\nu$ (speed/rate). Y-axis: $\eta^*$ (quality/gain). Contour lines are hyperbolas showing iso-tempo curves — all points on the same curve have the same $\mathcal{T}$.

Three labeled points on the plot:
- **Point A** (high $\nu$, low $\eta^*$): "Fast but sloppy." Sits on a moderate-$\mathcal{T}$ contour.
- **Point B** (low $\nu$, high $\eta^*$): "Slow but precise." Sits on the SAME contour as A — same tempo despite very different speed and quality.
- **Point C** (moderate $\nu$, moderate $\eta^*$, both improved): Sits on a HIGHER contour. "Both improve → multiplicative gain."

An arrow from A toward higher $\eta^*$ is labeled "Boyd's recommendation: improve quality." An arrow from A toward higher $\nu$ is labeled "Also works, but less room." The arrow toward quality is longer — more room to move on that axis.

> **Notation**: The substitutability follows directly from the multiplicative structure $\mathcal{T} = \nu \cdot \eta^*$. The contour lines are level sets: curves where $\nu \cdot \eta^* = \text{constant}$. These are hyperbolas — the same shape as indifference curves in economics. Moving along a contour trades speed for quality at a constant tempo. Moving to a higher contour increases tempo. The multiplicative compounding: $1.5 \times 1.5 = 2.25$, not $1.5 + 1.5 = 3.0$. Improving both speed and quality by 50% each gives 125% improvement, not 200%. This is why the "both improve" point C sits on a higher contour than you might expect from linear thinking.

---

## Slide 23a: Two Competing Forces

# TWO COMPETING FORCES

### TF-11 — How Mismatch Evolves

$$\frac{d\|\delta\|}{dt} = -\underbrace{\mathcal{T} \cdot \|\delta\|}_{\text{correction}} + \underbrace{\rho}_{\text{disturbance}}$$

**Visualization**: A horizontal axis representing mismatch magnitude $\|\delta\|$, from 0 ("perfect model") on the left to large ("badly wrong") on the right. A ball sits on this axis.

Two forces act on the ball:

**LEFTWARD ARROW** (orange, "Correction: $\mathcal{T} \cdot \|\delta\|$"): Points toward zero. Length is proportional to BOTH $\mathcal{T}$ and the ball's position — **the arrow gets longer when the ball is further right.** At position 0, the arrow vanishes entirely.

**RIGHTWARD ARROW** (dark, "Disturbance: $\rho$"): Points toward larger mismatch. Length is **constant** — the world changes at rate $\rho$ regardless of the model's state.

Three snapshots of the ball at different positions, stacked:

**Position A** (far right): Correction arrow much longer than disturbance. Net force: strongly leftward. "$\mathcal{T}\|\delta\| \gg \rho$ → mismatch shrinking fast."

**Position B** (at $\|\delta\| = \rho/\mathcal{T}$): Arrows are exactly equal length. Ball stationary. "**STEADY STATE**: $\|\delta\|_{ss} = \rho / \mathcal{T}$"

**Position C** (near zero): Correction arrow shorter than disturbance. Net force: rightward. "$\mathcal{T}\|\delta\| < \rho$ → mismatch growing."

The steady state is **self-correcting**: pushed too far right → correction dominates → pulls back. Pushed too far left → disturbance dominates → pushes right. Always settles at $\rho/\mathcal{T}$.

> **Notation**: $d\|\delta\|/dt$ is the instantaneous rate of change of mismatch magnitude — how fast the ball is moving and in which direction. The double-bars $\|\cdot\|$ denote the norm (magnitude/length) of the mismatch vector. The correction term $-\mathcal{T} \cdot \|\delta\|$ is negative (pointing left) and proportional to BOTH $\mathcal{T}$ (the adaptive tempo from Slide 22 — rate × quality) AND $\|\delta\|$ (current mismatch). This proportionality is crucial and visible in the diagram: the leftward arrow grows with position. It means larger errors get corrected faster — the self-stabilizing mechanism. $\rho$ (rho) is the environment change rate — measured in surprise per unit time — the rate at which reality diverges from the model due to environmental change. It's constant on the diagram (rightward arrow doesn't change with position). The steady state $\|\delta\|_{ss} = \rho/\mathcal{T}$ is the position where the arrows balance — visually, where they're the same length. Higher tempo ($\mathcal{T}$ ↑) makes the correction arrow longer at every position, pushing the balance point leftward (lower steady-state mismatch). Higher disturbance ($\rho$ ↑) makes the constant rightward arrow longer, pushing the balance point rightward.

---

## Slide 23b: The Persistence Threshold

# THE PERSISTENCE THRESHOLD

### Proposition 11.1

$$\boxed{\mathcal{T} > \frac{\rho}{\|\delta_{\text{critical}}\|}}$$

**Visualization**: The same horizontal axis from 23a, but now with a **critical line** — a vertical red dashed line at position $\|\delta_{\text{critical}}\|$. The axis is divided:

**LEFT** (green background): "MODEL WORKS — mismatch small enough for effective action"

**RIGHT** (red background): "MODEL FAILS — acting on stale/wrong information"

Three scenarios stacked:

**Scenario 1** (high $\mathcal{T}$): The steady-state ball position $\rho/\mathcal{T}$ is well left of the critical line. The correction arrow at the steady state is drawn alongside the disturbance arrow — correction is strong. **PERSIST.** Label: "High tempo → low steady-state mismatch."

**Scenario 2** (moderate $\mathcal{T}$): Ball sits just left of the critical line. **MARGINAL.** Label: "Barely adequate tempo."

**Scenario 3** (low $\mathcal{T}$): Ball sits right of the critical line, in the red zone. The correction arrow at this position is drawn alongside the disturbance arrow — but it's smaller. The ball can't be pulled left far enough. **FAIL.** Label: "Tempo too low → model useless."

Below: four icons with labels:
- Skeleton: "**Extinction** — environment changes faster than organism adapts"
- Crumbling building: "**Organizational failure** — market moves faster than company learns"
- Warning gauge: "**Control instability** — disturbances exceed controller capacity"
- Overloaded brain: "**Cognitive overload** — information faster than processing"

> **Notation**: $\|\delta_{\text{critical}}\|$ is the critical mismatch threshold — the mismatch magnitude beyond which the model can no longer support effective action. This is domain-specific and connects to task performance: in a tracking system, it might be the error at which the tracker loses the target; in an organization, the strategy-reality gap at which decisions become counterproductive. The persistence condition $\mathcal{T} > \rho/\|\delta_{\text{critical}}\|$ rearranges the steady-state formula: we need $\rho/\mathcal{T} < \|\delta_{\text{critical}}\|$, i.e., the steady-state ball must sit left of the critical line. Rearranging: $\mathcal{T} > \rho/\|\delta_{\text{critical}}\|$. When $\|\delta_{\text{critical}}\|$ is normalized to 1 (measuring mismatch in units of the critical threshold), this simplifies to $\mathcal{T} > \rho$ — tempo must exceed disturbance rate. This is the survival condition.

---

## Slide 24a: The Correction Landscape

# THE CORRECTION LANDSCAPE

### Appendix A — Lyapunov Stability

The linear ODE is a first approximation. Real correction dynamics are nonlinear. Lyapunov handles the general case.

**The sector condition** — correction always points inward:

$$\delta^T F(\mathcal{T}, \delta) \geq \alpha\|\delta\|^2 \quad \text{for } \|\delta\| \leq R$$

### Proposition A.1: Mismatch ultimately bounded by $R^* = \rho/\alpha$. Persists iff $R^* < R$.

**Visualization**: A 2D "mismatch space" — the mismatch vector $\delta = (\delta_1, \delta_2)$ plotted on a plane. Origin (0,0) = perfect model, zero mismatch.

**THREE CONCENTRIC CIRCLES**, each labeled with its symbol and meaning:

**Outermost** (radius $R$, dark dashed border): The **model class boundary**. Inside this circle, the sector condition holds — correction works. Outside: correction may break down. Label: "$R$ = model class capacity."

**Middle** (radius $R^* = \rho/\alpha$, solid orange border, light orange fill): The **ultimately bounded region** — where mismatch settles and stays. Label: "$R^* = \rho/\alpha$ = where the ball settles."

**Origin**: Zero mismatch — theoretical ideal, never quite reached because $\rho > 0$.

**FLOW ARROWS** throughout:
- Inside $R$: all arrows point INWARD, spiraling toward the $R^*$ ball. Arrows are longer at larger $\|\delta\|$ — stronger correction for larger errors.
- Inside $R^*$: arrows are shorter, approximately balanced by disturbance. Trajectories meander within this ball.
- Outside $R$ (faded region): arrows become erratic or outward — correction has broken down.

**THE GAP** between the $R^*$ circle and the $R$ circle is visually prominent, labeled with a double-headed arrow: "$\Delta\rho^* = \alpha R - \rho$" — the ADAPTIVE RESERVE.

> **Notation**: We move from the 1D number line (Slides 23a-b) to 2D mismatch space. The mismatch vector $\delta$ now has components $(\delta_1, \delta_2)$, and $\|\delta\|$ is its length — the distance from the origin. $F(\mathcal{T}, \delta)$ is the general correction function — replacing the linear $\mathcal{T} \cdot \delta$ with a potentially nonlinear function. The sector condition $\delta^T F \geq \alpha\|\delta\|^2$ is a dot-product condition: $\delta^T F$ (delta-transpose times F) measures whether the correction vector points inward (positive dot product = pushing toward origin). The condition guarantees this inward push is at least $\alpha$ times the squared distance from the origin, where $\alpha$ is the lower correction efficiency bound — the worst-case correction rate within the valid region. $R$ is the radius where this guarantee holds — beyond it, the model class is overwhelmed (TF-10 territory). $R^* = \rho/\alpha$ is where the system settles — the analog of $\rho/\mathcal{T}$ from the linear case, but now $\alpha$ replaces $\mathcal{T}$ as the operative correction parameter. The flow arrows directly visualize $F$: at each point $\delta$, the arrow shows which way the correction pushes.

---

## Slide 24b: Adaptive Reserve and Shock

# ADAPTIVE RESERVE

### Proposition A.2

$$\boxed{\Delta\rho^* = \alpha R - \rho}$$

**The gap between total correction capacity and current demand.** How much additional shock the agent can absorb before model breakdown.

**Visualization**: The same concentric-circle diagram from 24a, shown in THREE states side by side:

**STATE 1: ROBUST** (large $\Delta\rho^*$):
- $R^*$ is small relative to $R$. The orange ball is a small dot inside a large boundary circle. The gap (reserve) is wide.
- A "shock wave" approaches — the agent absorbs it easily. $R^*$ grows slightly, still well within $R$.
- Examples: "Organism in stable niche. Well-capitalized firm. Force with operational depth."

**STATE 2: FRAGILE** (small $\Delta\rho^*$):
- $R^*$ has grown to nearly fill $R$. The orange ball almost touches the outer boundary. The gap is a thin sliver.
- The same shock wave would push $R^*$ past $R$. One more disturbance and correction breaks.
- Examples: "At culmination point. Startup in volatile market. Near model capacity."

**STATE 3: FAILURE** ($\Delta\rho^* < 0$):
- $R^*$ has expanded past $R$. The orange ball exceeds the boundary.
- Flow arrows outside $R$ are erratic/outward. Correction has broken down.
- Label: "Structural adaptation required (TF-10)."

Below all three: a fuel gauge. Total capacity = $\alpha R$. Current demand = $\rho$. Remaining = $\Delta\rho^*$. When the gauge empties: model failure.

> **Notation**: $\Delta\rho^*$ (delta-rho-star) is the adaptive reserve — a single number for robustness. It's computed from three quantities visible in the diagram: $\alpha$ (the worst-case correction efficiency — how steep the inward pull is), $R$ (the model class capacity — how far the correction mechanism reaches), and $\rho$ (the current disturbance rate). The product $\alpha R$ is the total correction capacity — the maximum disturbance the system can handle. Subtract the current demand $\rho$ and you get the reserve: $\Delta\rho^* = \alpha R - \rho$. The three states in the visualization correspond to: $\Delta\rho^* \gg 0$ (robust — operating well below capacity, lots of room for shock), $\Delta\rho^* \approx 0$ (fragile — at capacity, minimal shock tolerance), and $\Delta\rho^* < 0$ (failed — correction mechanism overwhelmed, the system has left the region where its model class works, triggering structural adaptation per TF-10). The connection to adversarial dynamics: an adversary destabilizes you by adding $\gamma_A \cdot \mathcal{T}_A$ to your $\rho$, consuming your reserve (Prop A.3, Slide 26).

---

## Slide 25: Adversarial Coupling — How Tempo Becomes Disturbance

# ADVERSARIAL COUPLING

### TF-11 — A's Tempo Becomes B's Disturbance

$$\rho_B = \rho_{B,\text{base}} + \gamma_A \cdot \mathcal{T}_A$$

**Visualization**: This slide REUSES the force diagram from Slide 23a, but now for TWO agents shown side by side.

**AGENT A's force diagram** (left): The same horizontal axis from 23a. A's correction arrow (leftward, strong, proportional to $\mathcal{T}_A \cdot \|\delta_A\|$). A's disturbance arrow (rightward, moderate, length $\rho_A$). A's ball sits at a comfortable steady state (low mismatch).

**AGENT B's force diagram** (right): Same layout. B's correction arrow (leftward, proportional to $\mathcal{T}_B \cdot \|\delta_B\|$). But B's disturbance arrow is **longer** — it has two visually distinct segments:
- A dark segment of length $\rho_{B,\text{base}}$ (base environmental disturbance — same as before)
- An ORANGE segment of length $\gamma_A \cdot \mathcal{T}_A$ attached to the end (the adversarial contribution from A)

The total rightward arrow $\rho_B = \rho_{B,\text{base}} + \gamma_A \cdot \mathcal{T}_A$ is visibly longer than A's $\rho_A$.

**CONNECTING ARROW** between the two diagrams: from A's correction arrow (A's effective action) to the orange segment of B's disturbance arrow. Labeled: "$\gamma_A$ = coupling effectiveness — what fraction of A's tempo becomes B's problem."

The consequence is visible: B's ball settles further right (higher steady-state mismatch) because B's disturbance arrow is longer.

Symmetrically (shown lighter/smaller): B also contributes $\gamma_B \cdot \mathcal{T}_B$ to A's disturbance. But if $\gamma_A \mathcal{T}_A > \gamma_B \mathcal{T}_B$, A is disrupting B more than B is disrupting A.

> **Notation**: $\rho_B$ is B's total effective disturbance rate — what B faces on the right side of its force diagram. It has two components: $\rho_{B,\text{base}}$ (the base environmental change rate that B would face even without A — the dark segment) and $\gamma_A \cdot \mathcal{T}_A$ (the adversarial contribution — the orange segment). $\gamma_A$ (gamma-A) is the intent-weighted coupling effectiveness: what fraction of A's adaptive tempo translates into disturbance for B. It absorbs three things: coupling strength (how much A's actions physically affect B's world), action impact per cycle (how disruptive each of A's actions is), and adversarial intent (whether A is directing its actions against B). A fast learner who ignores B has $\gamma_A \approx 0$; one who weaponizes every adaptive cycle against B has $\gamma_A$ approaching 1. The key visual: the orange segment literally shows A's contribution to B's disturbance arrow. When A's tempo increases, the orange segment grows — B's disturbance gets worse — B's steady-state ball moves right.

---

## Slide 26a: Squared Tempo Advantage

# SQUARED TEMPO ADVANTAGE

### Corollary 11.2

$$\boxed{\frac{\|\delta_B\|_{ss}}{\|\delta_A\|_{ss}} = \frac{\gamma_A}{\gamma_B}\left(\frac{\mathcal{T}_A}{\mathcal{T}_B}\right)^2}$$

Tempo advantage **squares**: 2:1 → 4:1, &ensp; 3:1 → 9:1, &ensp; 5:1 → 25:1.

**Why the squaring?** A's tempo helps A *twice*:
1. Higher $\mathcal{T}_A$ → A's OWN mismatch is lower (A adapts faster)
2. Higher $\mathcal{T}_A$ → B's disturbance is HIGHER (A disrupts B faster)

Both effects compound in the ratio → the square.

**Visualization**: The two-agent force diagram from Slide 25, but now shown in three scenarios stacked:

**Scenario 1** ($\mathcal{T}_A = \mathcal{T}_B$, symmetric): Both agents' force diagrams look identical. Equal steady states. Mismatch ratio ≈ 1:1 (modified by $\gamma$ ratio). Label: "Symmetric — stalemate."

**Scenario 2** ($\mathcal{T}_A = 2\mathcal{T}_B$): A's correction arrow is twice as strong → A's ball is further left (lower mismatch). Meanwhile, A's orange contribution to B's disturbance arrow is twice as large → B's ball is further right. The combined effect: **4:1** mismatch ratio. Label: "2× tempo advantage → 4× mismatch advantage."

**Scenario 3** ($\mathcal{T}_A = 3\mathcal{T}_B$): A's mismatch is tiny. B's disturbance arrow is dominated by A's orange contribution. B's ball is far to the right. **9:1** mismatch ratio. Label: "3× tempo → 9× advantage. Boyd's 'getting inside the loop.'"

> **Notation**: $\|\delta_B\|_{ss}/\|\delta_A\|_{ss}$ is the ratio of steady-state mismatch magnitudes — how much worse B's model is than A's. The squared term $(\mathcal{T}_A/\mathcal{T}_B)^2$ arises because tempo appears on BOTH sides of the balance: in the numerator ($\mathcal{T}_A$ increases B's disturbance, pushing B's ball right) and in the denominator ($\mathcal{T}_A$ reduces A's own steady-state mismatch, pulling A's ball left). Multiply these two effects: $(\mathcal{T}_A/\mathcal{T}_B) \times (\mathcal{T}_A/\mathcal{T}_B) = (\mathcal{T}_A/\mathcal{T}_B)^2$. The $\gamma_A/\gamma_B$ prefactor captures asymmetric coupling: if A disrupts B more effectively than B disrupts A ($\gamma_A > \gamma_B$), the advantage is amplified further. This is the formal content of "getting inside the opponent's OODA loop" — derived from the coupled force diagrams, not asserted as doctrine.

---

## Slide 26b: Destabilization and the Effects Spiral

# THE EFFECTS SPIRAL

### Proposition A.3 + Corollary A.3.1

Agent A drives Agent B past its stability boundary when:

$$\boxed{\gamma_A \cdot \mathcal{T}_A > \Delta\rho^*_B}$$

*A's effective disruption exceeds B's adaptive reserve.*

**Cor. 11.2 tells you the score. Prop. A.3 tells you when the game is over.**

### The Effects Spiral — Positive-Feedback Lyapunov Instability:

$$\|\delta_B\| \uparrow \;\Rightarrow\; B\text{'s actions erratic} \;\Rightarrow\; \gamma_A \uparrow \;\Rightarrow\; \rho_B \uparrow \;\Rightarrow\; \|\delta_B\| \uparrow$$

**Visualization**: COMBINES the Lyapunov landscape from Slide 24a with the adversarial coupling from Slide 25:

**LEFT**: Agent A's Lyapunov basin (from 24a) — the concentric circles. A's ball sits comfortably inside a small $R^*_A$ circle, well within a large $R_A$ boundary. Large reserve.

**RIGHT**: Agent B's Lyapunov basin — but B's $R^*_B$ circle has been EXPANDED by A's adversarial coupling ($\gamma_A \cdot \mathcal{T}_A$ added to B's $\rho$). Three progressive panels or an animation:

1. **Before**: B's $R^*_B$ is inside $R_B$ — B is still functioning, but the gap ($\Delta\rho^*_B$) is narrowing as $\gamma_A \cdot \mathcal{T}_A$ grows.

2. **Threshold crossed**: $R^*_B$ reaches $R_B$ — B is at the boundary. The force arrows at the rim are barely inward.

3. **After**: $R^*_B > R_B$ — B has exited the basin. Flow arrows outside become erratic/outward. A **spiral** emerges — B's mismatch accelerates away from the origin. Each revolution of the spiral is visually tighter/faster. Labels on the spiral: "Model degrades → Actions worsen → Opponent exploits → Model degrades further."

Three escape routes shown as arrows breaking from the spiral: "Structural adaptation (TF-10)," "External rescue (ally stabilization)," "Cessation."

> **Notation**: The destabilization condition $\gamma_A \cdot \mathcal{T}_A > \Delta\rho^*_B$ connects two quantities from earlier slides: $\gamma_A \cdot \mathcal{T}_A$ is A's effective disruption (the orange segment from Slide 25 — how much A adds to B's disturbance), and $\Delta\rho^*_B = \alpha_B R_B - \rho_B$ is B's adaptive reserve (the gap from Slide 24b — how much additional disturbance B can absorb). When the disruption exceeds the reserve, $R^*_B$ grows past $R_B$ and B exits its Lyapunov basin. The effects spiral $\|\delta_B\| \uparrow \Rightarrow \gamma_A \uparrow$ captures the positive feedback: as B's mismatch grows past $R_B$, B's correction mechanism breaks down (the sector condition fails), B's actions become erratic (its model is too wrong to generate coherent action), which makes B *more vulnerable* to A's disruption ($\gamma_A$ increases — an erratic opponent is easier to exploit), which drives $\rho_B$ even higher, which pushes $\|\delta_B\|$ further out. The Lyapunov function $V = \frac{1}{2}\|\delta_B\|^2$ is now increasing rather than decreasing — formal instability. Boyd described this cascade from combat experience as the "effects spiral." TFT derives it from coupled Lyapunov dynamics.

---

## Slide 27: Communication Gain

# COMMUNICATION GAIN

### Appendix F — Extending the Uncertainty Ratio to Social Channels

$$\eta_{ji}^* = \frac{U_{M_i}}{U_{M_i} + U_{o,ji} + U_{\text{src},j} + U_{\text{align},ji}}$$

**Visualization**: DIRECTLY EXTENDS the uncertainty-ratio bar from Slide 13a. The bar structure is identical — $\eta_{ji}^*$ is still the orange fraction — but the right side now has THREE stacked segments instead of one:

**THE BAR** (same structure as 13a, extended):

- **LEFT** (orange segment): $U_{M_i}$ — agent $i$'s model uncertainty. Same as before.
- **RIGHT** (three stacked segments, visually distinct):
  - **Gray segment**: $U_{o,ji}$ — communication channel noise (lossy channel, ambiguity, latency)
  - **Blue segment**: $U_{\text{src},j}$ — source quality uncertainty (is $j$ calibrated? competent in this domain?)
  - **Red segment**: $U_{\text{align},ji}$ — alignment uncertainty (does $j$ share my goals, or might they be adversarial?)

$\eta_{ji}^*$ is still the orange fraction of the total bar. But the total bar is now longer — more things can suppress the gain.

**Three scenarios shown** (same stacked-bar format as 13a):

**Scenario 1** (trusted expert, clear channel): $U_{\text{src}} \approx 0$, $U_{\text{align}} \approx 0$, $U_o$ small. Only the gray segment is visible (and it's thin). Bar looks almost like 13a's standard gain. $\eta_{ji}^*$ is high. Label: "Calibrated ally on clear channel → update substantially."

**Scenario 2** (unknown source, noisy channel): $U_{\text{src}}$ and $U_o$ both large. Blue and gray segments make the right side long. $\eta_{ji}^*$ is moderate-to-low. Label: "Unknown competence, lossy channel → update cautiously."

**Scenario 3** (possible adversary): $U_{\text{align}}$ large (big red segment dominates). $\eta_{ji}^*$ is near zero. Label: "Potentially adversarial → nearly ignore."

**Bottom**: Show Slide 13a's standard bar (two segments) next to this slide's extended bar (four segments) with annotation: "When the source IS the environment, $U_{\text{src}} = U_{\text{align}} = 0$ and the blue and red segments vanish — recovering the standard gain."

Trust is itself a **meta-model** — subject to its own TFT dynamics: mismatch (trust predictions that were wrong), gain (not overreacting to single instances), structural adequacy (is your trust model rich enough?).

> **Notation**: $\eta_{ji}^*$ (eta-star, subscript $ji$) is the communication gain — how much agent $i$ should update based on a signal from agent $j$. The subscript $ji$ reads "from $j$ to $i$." It has the same structure as the standard gain from 13a — orange fraction of total bar — but the denominator is larger. The four terms in the denominator (all measured in the same predictive-variance units): $U_{M_i}$ is $i$'s own model uncertainty (the orange segment — same as TF-06). $U_{o,ji}$ is channel noise specific to the $j$→$i$ link (the gray segment — latency, ambiguity, bandwidth). $U_{\text{src},j}$ is source quality uncertainty (the blue segment) — $i$'s estimate of $j$'s calibration and domain competence. Low for a proven expert ($j$ has been right before about this topic); high for an unknown. $U_{\text{align},ji}$ is alignment uncertainty (the red segment) — $i$'s estimate of whether $j$'s signal is designed to help $i$ or to mislead. Zero for a fully trusted teammate; high for a competitor or unknown. The visual makes the formula immediate: each uncertainty source extends the right side of the bar, shrinking the orange fraction. More uncertainty about the source → lower gain → less update from that source.

---

## Slide 28: Distributed Tempo

# TEAMS CAN PERSIST WHERE INDIVIDUALS CANNOT

### Appendix F — Distributed Tempo

$$\mathcal{T}_i = \underbrace{\sum_k \nu_i^{(k)} \eta_i^{(k)*}}_{\text{observe}} + \underbrace{\sum_{j} \nu_{ji}^{\text{comm}} \, \eta_{ji}^*}_{\text{communicate}}$$

### Cooperative-adversarial disturbance decomposition:

$$\rho_i^{\text{eff}} = \rho_{i,\text{env}} + \sum_j \gamma_{j}^{\text{adv}} \mathcal{T}_j - \sum_j \gamma_{j}^{\text{coop}} \mathcal{T}_j$$

**Allies reduce your effective disturbance** by sharing preemptive information.

Team persistence: $\rho_i^{\text{eff}} / \alpha_i < R_i$

### Topology failure modes:

| Peer Network | Ensemble | Hierarchy |
|---|---|---|
| **Groupthink**: collective confidence without accuracy | **Correlated failure**: all experts wrong the same way | **Micromanagement**: ν_strategic ≈ ν_tactical → oscillation |

**Visualization**: Left: a single agent facing a large wave (ρ) — barely surviving. Right: a team of four agents linked by communication arrows facing the same wave — cooperative signals reduce the effective wave hitting each individual. The individual wave heights are visibly smaller. Below: three small network diagrams (peer, ensemble, hierarchy) each with a red failure-mode annotation.

> **Notation**: $\mathcal{T}_i$ is agent $i$'s distributed tempo — now including two sums. The first sum $\sum_k \nu_i^{(k)} \eta_i^{(k)*}$ is the direct observation tempo (same as single-agent TFT). The second sum $\sum_j \nu_{ji}^{\text{comm}} \eta_{ji}^*$ adds the communication tempo: for each neighbor $j$, multiply the rate of communication events from $j$ to $i$ ($\nu_{ji}^{\text{comm}}$) by the communication gain from $j$ ($\eta_{ji}^*$). The disturbance decomposition $\rho_i^{\text{eff}}$ separates three components: $\rho_{i,\text{env}}$ (base environmental disturbance), adversarial terms $\gamma_j^{\text{adv}} \mathcal{T}_j$ (opponents making things harder), and cooperative terms $\gamma_j^{\text{coop}} \mathcal{T}_j$ (allies reducing effective disturbance). The cooperative term is subtracted — allies *reduce* your disturbance by sharing preemptive information. This is why teams can persist where individuals cannot: $\rho_i^{\text{eff}}$ can drop below $\rho_{i,\text{env}}$ through cooperation.

---

## Slide 29: Kalman Validation

# EXACT VALIDATION: KALMAN FILTER

### Appendix C

| TFT Concept | Kalman Counterpart | Status |
|---|---|---|
| Model $M_t$ | State + covariance $(\hat{x}, P)$ | **Exact** |
| Mismatch $\delta_t$ | Innovation $\tilde{y}_t$ | **Exact** |
| Gain $\eta^*$ | Kalman gain $K = P^-/(P^-+R)$ | **Exact** |
| Tempo $\mathcal{T}$ | $\nu \cdot \bar{K}$ | **Exact** |
| CIY | KL between sensor modes | **Exact** |
| Persistence | $\mathcal{T} > \rho/\delta_c$ | **Exact** |
| Reserve | $\Delta\rho^* = \alpha R - \rho$ | **Exact** |

The Kalman filter **is** TFT, instantiated for linear-Gaussian systems.

Every quantity computable in closed form.

**Visualization**: A side-by-side flow diagram. Left: the Kalman predict-update cycle in Kalman notation. Right: the TFT observe-orient-decide-act cycle in TFT notation. Every box on the left maps 1:1 to a box on the right with "=" signs connecting them. The visual makes clear they are the same structure, different labels.

> The Kalman filter is the proof of concept. Every TFT quantity has an exact Kalman counterpart. The gain IS the uncertainty ratio. The innovation IS the mismatch signal. This isn't an analogy — it's a mathematical identity. If TFT were wrong for Kalman, it would be wrong everywhere. But it's exact.

---

## Slide 30: RL Validation

# APPROXIMATE VALIDATION: RL BANDIT

### Appendix D — Where Q-Learning Falls Short

4-armed bandit with drifting rewards. Q-learning with UCB.

### Per-arm persistence check:

$$\mathcal{T}_i = \frac{\nu}{k} \cdot \alpha = \frac{1}{4} \times 0.091 = 0.023$$

$$\rho_i = \sqrt{q} = 0.1$$

$$0.023 < 0.1 \quad \Longrightarrow \quad \textbf{PERSISTENCE FAILS}$$

### TFT diagnosis:

Fixed α is a **degenerate constant gain** — no uncertainty tracking.

Per-arm tempo insufficient — aggregate tempo masks per-dimension failure.

Remedies: higher α (more noise), focused exploration (fewer tracked arms), or move to Bayesian bandit (proper η*).

**Visualization**: Four gauge/dashboard dials — one per bandit arm. Each shows T_i (0.023) vs. ρ_i (0.1). All four needles are in the red zone. A central aggregate gauge shows T = 0.091 vs. ρ = 0.4 — also red. Label: "Aggregate tempo hides per-dimension failure. The scalar T overestimates effective adaptation."

> **Notation**: In the per-arm tempo calculation: $\nu/k$ is the per-arm observation rate — with $k = 4$ arms and $\nu = 1$ pull per step, each arm is observed at rate $1/4$. $\alpha = 0.091$ is the Q-learner's fixed learning rate (standing in for $\eta^*$). So per-arm tempo $\mathcal{T}_i = (1/4)(0.091) = 0.023$. The per-arm drift rate $\rho_i = \sqrt{q}$ where $q = 0.01$ is the random-walk variance of each arm's reward mean — giving $\rho_i = 0.1$. Since $0.023 < 0.1$, the persistence condition $\mathcal{T}_i > \rho_i$ fails per-arm. The scalar aggregate tempo $\mathcal{T} = \nu \cdot \alpha = 0.091$ against aggregate $\rho = k\sqrt{q} = 0.4$ also fails, but the *per-arm* analysis is the diagnostic: it reveals which dimensions are failing and why, where the aggregate hides the detail.

---

## Slide 31: The Cross-Domain Map

# THE UNIVERSAL PATTERN

| | Mismatch $\delta$ | Gain $\eta^*$ | Tempo $\mathcal{T}$ | Structural Change |
|---|---|---|---|---|
| **Kalman** | Innovation | Kalman gain | ν·K | Model switching |
| **Bayesian** | Surprise | Posterior weight | n/κ | Model selection |
| **RL** | TD error | Learning rate | ν·α | Architecture search |
| **PID** | Error signal | Fixed gains | ν·K_p | Controller redesign |
| **Boyd** | Disorientation | Orient quality | OODA tempo | Destruction & creation |
| **Science** | Anomaly | Theory revision | Expt rate | Paradigm shift |
| **Immune** | Unknown antigen | Antibody affinity | Encounter rate | Novel antibody class |
| **Organization** | Market surprise | Strategy update | Decision cycle | Restructuring |

Same columns. Different substrates. Same formal structure.

**Visualization**: The table above rendered as a large blueprint grid. Each column header has the TFT symbol. Each row has a domain icon. The visual emphasis is on the vertical alignment — same column, same concept, different name. Thin vertical lines connect the cells in each column. The overall effect: a periodic table of adaptive patterns.

> Eight domains, four columns. Every column is the same TFT concept in a different substrate. The mismatch signal is always the gap between expectation and reality. The gain is always the mechanism for incorporating surprise. Tempo is always rate times quality. Structural change is always the expensive, necessary response to persistent framework failure.

---

## Slide 32: Falsification Predictions

# WHAT WOULD KILL THE THEORY

### Five Testable Predictions

**Core (would break the framework):**

1. **Gain structure**: Optimal gain depends on something fundamentally different from the uncertainty ratio

2. **Persistence threshold**: Adequate tempo + adequate model class → still unbounded mismatch

**Refinement (would fix specific hypotheses):**

3. **Speed-quality substitutability**: Doubling η* ≠ doubling ν in effect

4. **Squared tempo advantage**: Adversarial advantage doesn't compound superlinearly

5. **Structural adaptation trigger**: Structured residuals persist despite provably adequate model classes

**Visualization**: Five target icons arranged in a pyramid. Top two (red, larger): "1. Gain structure" and "2. Persistence threshold" — labeled "Core: would break TFT." Bottom three (orange, smaller): predictions 3-5 — labeled "Refinement: would fix specific hypotheses." The arrangement emphasizes the load-bearing nature of 1 and 2.

> Any theory worth having can be wrong. These five predictions are testable in instrumented systems. The first two are load-bearing — if the gain structure or persistence threshold fails, the core framework is broken. The last three are refinement-level — they'd tell us specific hypotheses need revision, but the broader structure survives. This is what distinguishes a theory from a metaphor.

---

## Slide 33: What TFT Is

# WHAT TFT IS AND ISN'T

### IS:
- A **formal vocabulary** — shared language across domains
- A **structural template** — the loop every adaptive system runs
- A **diagnostic framework** — estimable quantities, checkable thresholds
- A **design framework** — principled constraints on gain, tempo, structure

### IS NOT:
- A grand unified theory
- A replacement for Kalman, RL, Bayesian inference
- A claim that all adaptive systems are "the same"
- An algorithm you implement

**TFT is to adaptive systems what thermodynamics is to heat engines.**

It constrains what's possible. It doesn't specify the design.

**Visualization**: Two columns. Left (with green checkmarks): what TFT IS — each item with an icon. Right (with red X marks): what TFT is NOT. Below: the thermodynamics analogy as a final image — a Carnot cycle diagram next to a TFT feedback loop, with the label "Constraints, not designs."

> Let me be clear about what the theory is. It's a vocabulary, a template, and a diagnostic framework. It gives you quantities to estimate, thresholds to check, and failure modes to watch for. It's not a replacement for domain-specific tools — the Kalman filter is still the Kalman filter. It's the abstraction layer that reveals what they have in common and constrains what any specific design must satisfy. Like thermodynamics: it doesn't design engines, it constrains them.

---

## Slide 34: The Open Frontier

# THE OPEN FRONTIER

| Question | Status | Impact |
|----------|--------|--------|
| Non-parametric $U_M$ | Open | Extend gain to deep learning |
| Tempo tensor | Flagged | Capture anisotropic adaptation |
| Continuous interiority | Architecture question | Central for persistent agents |
| Game-theoretic communication | Identified | Multi-agent trust dynamics |
| Thermodynamic connection | Not assumed | Deepest open question |
| Deriving λ from first principles | Domain-specific | Full explore-exploit unification |

### The theory is a beginning, not an end.

**Visualization**: A horizon scene rendered in the blueprint style. Foreground: solid, established ground — the TFT loop, the key formulas, the proven propositions (all clearly rendered). The horizon stretches out with partial structures emerging from a light grid-mist — each open question as a structure-in-progress. The feel is invitation, not uncertainty. Footer: "EPISTEMIC BLUEPRINT // TEMPORAL FEEDBACK THEORY // WORKING DRAFT"

> These are not failures — they're frontiers. Can we extend the gain to neural networks? What does continuous interiority look like? When is honest communication incentive-compatible? Each of these is a research program. TFT provides the vocabulary for asking them precisely. The theory is a beginning: a formal structure that makes these questions tractable. What comes next depends on what we build with it.

---

*EPISTEMIC BLUEPRINT // TEMPORAL FEEDBACK THEORY // WORKING DRAFT*
*45 slides (8 concepts split for stepwise notation introduction). For source material: ~/src/temporal-feedback/*
