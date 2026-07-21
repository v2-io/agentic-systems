# Answers — Batch 1 quiz

## (1) Critical Mental Model

### A b01-1.1 [mental-model]
**(c)** It is a *scope condition* — a constitutive/definitional boundary, not an assumption or empirical claim. With direct full-state access the entire adaptive machinery (mismatch, model, correction) is vacuous, so the theory draws its boundary where the machinery is non-degenerate. Consequence: perfect-information objections are out of scope by construction; no downstream result must re-earn the uncertainty premise. (Grading: "simplifying assumption" = summary-level wrong answer.)

### A b01-1.2 [mental-model]
Known $T$: action selection collapses toward optimization/planning over a known function (a solver, not an adapter) — consequence-prediction becomes computation. Known $h$ (with $T$ still unknown): uncertainty does *not* dissolve — $h$ is constitutively lossy, so $\Omega_t$ remains unrecoverable — but the perception side reduces to standard filtering against a known observation law; the distinctive AAT setting is degraded, not eliminated. The segments' claim is that the *combination* of unknown $h$ and unknown $T$ is what creates the need for adaptive behavior; each single-known case removes a different part of the problem, asymmetrically (known $T$ is the more degenerating of the two). *(Corrected after verification: an earlier version of this answer wrongly equated "known $h$" with full-state access.)*

### A b01-1.3 [mental-model]
Thermostat: inside (observes temperature under residual uncertainty). Passive Kalman filter: inside — action is *not* required for adaptive scope. Proof engine: outside, fails $\mathcal O \neq \emptyset$ (no observation channel / no agent-environment boundary), not the entropy condition.

### A b01-1.4 [mental-model]
The formulation converts a channel *inventory* into membership *requirements*, and misplaces where tier-distinctions live. "Agent" is the *umbrella* term for whatever sits on the agent side of the coupling; the coupling's three channels name what it *has*, not what must be exercised. Passive observers are agents (umbrella sense) inside the adaptive scope; they merely fail the *agency* narrowing (causal contrast). The capitalized tier-noun "Actuated Agent" is earned later at the $X_t=(M_t,G_t)$ lift.

### A b01-1.5 [mental-model]
The **chronica (trajectory)** is non-forkable; the **model state $M_t$** (lossy compression) is copyable. Copying $M_t$ gives the copy compressed memory of a history it did not live; from the first divergent event the two chronicae extend differently and neither is a sufficient statistic for the other's trajectory. Non-forkability is a claim about *trajectories*, not representations — the representation can be byte-copied; the lived causal history cannot be shared forward.

### A b01-1.6 [mental-model]
It encodes causal irreversibility: $a_{t-1}$ was committed before $o_t$ arrived, so the agent could not have used $o_t$ to choose $a_{t-1}$. The interleaving is the record of what information was available when — the substrate for every later claim about update ordering and identity.

## (2) Mathematics

### A b01-2.1 [math]
$\mathcal S_{\text{adaptive}} = \{(\text{Agent},\Omega) : \mathcal O \neq \emptyset,\ H(\Omega_t\mid\mathcal C_t) \gt 0\}$. $\mathcal O = \emptyset$ wall = pure computation (proof engine; no agent-environment boundary). $H = 0$ wall = closed-form/omniscient case (optimal control over known dynamics; nothing to adapt about). AAT is the theory of the open region between the walls.

### A b01-2.2 [math]
Neither the agent's belief nor its own estimate: it is the *true* conditional entropy — a modeler's/God's-eye predicate over the actual $\Omega_t$ given the history. An agent whose subjective uncertainty is zero while true entropy is positive is still in scope — and is precisely the delusionally-confident agent about to receive a large mismatch signal. The objective/subjective gap is where catastrophic failure lives.

### A b01-2.3 [math]
$o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$. The $a_{t-1}$ argument (the one summary readers drop) provides **active perception**: what the agent observes can depend on what it just did / where it looked, making observation quality partly under agent control (later load-bearing for software/TST and exploration).

### A b01-2.4 [math]
**(c).** It is a modeling commitment about the *breadth of the named object*: $\Omega$ is defined as the sufficient state for its own evolution; any non-Markov world is absorbed by extending $\Omega$ with enough history (WLOG, since $\Omega$ is unbounded). Parallel move: Markov-by-completeness for the agent state $M_t$ via der-recursive-update (Constraint C3). (Bonus/depth: the parallel is asymmetric in cost — $\Omega$-side is free; $M_t$ is bounded and lossy, so its sufficiency commitment has teeth that relocate to capacity machinery.)

### A b01-2.5 [math]
The chronica is an **ordinal event-indexed sequence, not a metric timeline** — suspension is invisible at the sequence level (index advances one tick on resume). The gap manifests in the *mismatch signal*: $\Omega$ drifted during the pause while $M_t$ did not, so the resumed observation carries a large $\delta$. 

### A b01-2.6 [math]
**Yes.** $\phi$ is lossy (many-to-one), so divergent chronicae can compress to the same $M_t$. Structural consequence: a fork need not be detectable from inside — the agent cannot always tell from $M_t$ alone which branch it is on (identity-loss undetectability; the substrate of the later Three-Deaths/ELI treatment).

## (3) Implications

### A b01-3.1 [implications]
Best example: the information-loss boundary. By *excluding* the full-access case definitionally, every downstream theorem may assume genuine uncertainty without an added hypothesis, and no result can be trivialized by a perfect-information limit — the limit exits the scope. (Also acceptable: the $H\gt 0$ wall making persistence machinery non-vacuous; the Markov-as-breadth commitment discharging non-Markov objections.)

### A b01-3.2 [implications]
The **Containment Dichotomy** (anchor #2). Against bounded (Model-D) disturbance a sector-stable corrector holds a fixed region with certainty forever; against stochastic disturbance no correction strength prevents eventual exit of any fixed region w.p. 1 over an unbounded horizon. It is a *dichotomy* because both arms are exact — the stochastic arm is a proven no-go, not degradation — and its positive content is that structural adaptation (changing model *kind*) is a certain eventual necessity for long-lived agents, not an edge case. Common misquote to reject: "stochastic agents eventually die/fail."

### A b01-3.3 [implications]
Backup restoration preserves the *state* ($M_t$ and stored records) but not the *trajectory*: post-restoration, the entity extends a chronica from a point that the world has moved past, and if the original ran on after the backup, the restored copy carries compressed memory of a history that is not its own continuous causal past. Identity tracks the irreversible trajectory, not the copyable snapshot — hence "not a neutral operation." (Depth: the loss may be undetectable from inside, per 2.6.)

### A b01-3.4 [implications]
Identical: the epistemic update mathematics — mismatch-driven model correction under uncertainty is the same operation whether or not the agent caused the observations. Passive systems never gain: the interventional/causal results (Level-2 machinery, CIY, and everything purposeful in Parts II–III), via the missing property of *Pearl-level-2 causal contrast* (distinct actions yielding distinct interventional distributions) — they are "passive observers" (no choice) or "nominal agents" (choice without causal effect).

### A b01-3.5 [implications]
Stressed: the agent/environment boundary placement (own outputs become future $o_t$ — where does $\Omega$ end?); transition opacity (context-append is deterministic and known); Markov-of-$\Omega$ sizing (context window as sufficient state). Nothing yet *breaks*: $\Omega$ also contains the user/world whose dynamics remain opaque (opacity preserved), and the boundary is a modeling choice that can be drawn per analysis. The definitions flex; the stress-test is deferred to Volume 3. (Full credit requires the violated/stressed distinction, not "the definitions fail for LLMs.")

### A b01-3.6 [implications]
Because the mathematics is domain-agnostic, the framework refuses to smuggle mattering into its variables; the moral weight is "a shell around the physics, not a term inside it." What this buys: the later volumes' claims become *defensible rather than mystical* — the structural facts (identity = irreversible trajectory; coherence = sustained information cost; an objective without "enough" cannot rest) are theorems that hold regardless of one's stance on moral status, so the moral layer inherits proven structure instead of doing double duty as both physics and ethics.
