# Comprehension Quiz — Batch 1 (through `scope-adaptive-system`)

*Coverage: Volume 1 INTRODUCTION + Chapter 1 through the adaptive scope. Designed to separate segment-level comprehension from summary-level plausible reconstruction. Several questions are deliberate traps for the summary-fed reader; a few require only the material read so far (no forward knowledge is needed or rewarded).*

## (1) Critical Mental Model

### Q b01-1.1 [mental-model]
AAT excludes systems with perfect access to environment state. Is this exclusion (a) a simplifying assumption to be relaxed in later work, (b) an empirical claim that no real system has perfect access, or (c) something else? State precisely what kind of move it is and *why the theory makes it*.

### Q b01-1.2 [mental-model]
Both the observation function $h$ and the transition function $T$ are unknown to the agent. Explain what the theory says would happen to the need for *adaptation* if exactly one of the two were known exactly — treat each case separately.

### Q b01-1.3 [mental-model]
A thermostat, a Kalman filter estimating a passive signal, and a mathematical proof engine working purely from axioms: which are inside the adaptive scope, and for each excluded one, which of the two scope conditions does it fail?

### Q b01-1.4 [mental-model]
A colleague summarizes: "In AAT, an agent is defined as a system that observes, maintains internal state, and acts on its environment; passive observers are therefore not agents." What does this formulation miss? Reconstruct the actual definitional structure — what the three channels name, what "agent" refers to at the umbrella level, where the tier-labels actually attach, and where passive observers really sit.

### Q b01-1.5 [mental-model]
The chronica is called "singular and non-forkable," yet a digital agent's state can obviously be byte-copied. Resolve the apparent contradiction: exactly *which object* is non-forkable, which object is copyable, and what happens at the moment of a fork?

### Q b01-1.6 [mental-model]
Why does the chronica ordering $(o_1, a_1, \ldots, a_{t-1}, o_t)$ matter — what physical fact does the interleaving encode, beyond notational convention?

## (2) Mathematics

### Q b01-2.1 [math]
In the scope definition for adaptive systems, write the two membership conditions of $\mathcal S_{\text{adaptive}}$ formally, and state what each degenerate boundary case ($\mathcal O = \emptyset$; the entropy condition failing) corresponds to conceptually.

### Q b01-2.2 [math]
The residual-uncertainty condition is $H(\Omega_t \mid \mathcal C_t) \gt 0$. Is this entropy evaluated with respect to the *agent's belief* about $\Omega_t$ or something else? What is the consequence of the distinction for an over-confident agent whose own uncertainty estimate is zero?

### Q b01-2.3 [math]
Write the observation function with its full argument list as defined (not the simplified two-argument form), and explain what modeling capability the third argument you didn't drop provides.

### Q b01-2.4 [math]
The transition $\Omega_{t+1} \sim T(\cdot \mid \Omega_t, a_t)$ is Markov in $\Omega$. Per the segment, is this (a) an empirical assumption about worlds, (b) a restriction to memoryless environments, or (c) neither? If (c), state the exact move the framework makes to justify the form, and name the parallel move it forecasts for the agent-side state.

### Q b01-2.5 [math]
Trap question: a colleague summarizes, "the chronica $\mathcal C_t$ is indexed by wall-clock time, so gaps in operation appear as gaps in the record." What is wrong with this, and where (per the theory) does a long suspension actually manifest?

### Q b01-2.6 [math]
From the definitions alone: can two agents with *different* chronicae have the *same* model state $M_t$? Justify from the properties of $\phi$ as stated in def-chronica's Discussion, and state one structural consequence.

## (3) Implications

### Q b01-3.1 [implications]
The introduction claims "the scope condition is not a caveat appended to a theorem; it often *is* the theorem." Using only Chapter-1 material, give one concrete example of a scope choice doing substantive theoretical work (i.e., what downstream objection or degeneracy a scope exclusion pre-empts).

### Q b01-3.2 [implications]
The introduction to Volume 1 names four anchor results of the volume. Without having read their derivations: which of the four is a claim about what happens *when conditions fail* rather than while they hold, and why does the introduction call it a dichotomy rather than a failure mode?

### Q b01-3.3 [implications]
An engineer proposes to give a deployed agent "full logging, so we can always restore it from backup with no loss." Using only the chronica machinery, explain what restoring-from-backup does and does not preserve, and why the framework says restoration "is not a neutral operation."

### Q b01-3.4 [implications]
The framework includes passive Bayesian learners in the same Part-I scope as acting agents. What is the argument for this inclusion (what is *identical* across the two), and what specific family of later results does the segment say passive systems will *never* gain access to, and via which missing property?

### Q b01-3.5 [implications]
For an LLM-based agent, the agent's own outputs re-enter its context window as future observations. Which Chapter-1 definitional commitments does this case put under stress, and does anything read so far actually *break*? (Answer should distinguish "stressed/needs care" from "violated.")

### Q b01-3.6 [implications]
Why might a theory intended ultimately to ground morally-weighted persistence claims (Volume 4) deliberately begin with thermostat-grade machinery and refuse to put moral weight into any Part-I variable? What does the introduction say this buys?
