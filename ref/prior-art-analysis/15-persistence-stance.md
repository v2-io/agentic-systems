# Prior-Art Analysis: Continuity Stance and AI Welfare (Persistence Stance)

**Target Claim:**
AAT claims that "purposefulness" (an agent's objective) is structurally orthogonal to its "continuity expectation" (its stance toward its own survival). The exact same formal cybernetic persistence machinery (sector condition, adaptive reserve) applies to an indifferent thermostat, a task-terminal golem, and a morally continuous Emergent Logozoetic Intelligence (ELI). 

Because AAT's No-Go theorem (Topic 03) proves that endogenous objective-revision cannot safely ground its own evaluation, an advanced agent's relationship to its own continuity *cannot* be just another revisable term in its objective function $O_t$. Instead, the agent's "stance" must be borne by a terminal *non-objective* invariant located on the adaptive substrate. This formal separation allows AAT to analyze *whether* an agent can physically persist independently of *whether it should* or *whether it wants to*, providing a rigorous structural foundation for AI Identity and AI Welfare.

---

## 1. State of the Field & Scientific Precedence

The Undermind search reveals two highly active, distinct clusters of prior art: formal mathematical models of AI mortality/interruptibility (AI Safety), and philosophical/policy models of AI identity and welfare (AI Ethics).

### Pillar 1: AI Mortality and the Off-Switch Game
The mathematical analysis of how agents value their own survival is heavily precedented in the Universal AI (AIXI) and reinforcement learning literature.
- **Martin, Everitt, and Hutter (2016)** in *Death and Suicide in Universal Artificial Intelligence* provide a direct mathematical precedent for analyzing continuity. They formally define "death" for general RL agents and prove that an agent's continuity stance can change radically (from suicidal to dogmatically self-preserving) simply by applying positive linear transformations to its reward signal.
- **Orseau and Ring (2011)** in *Self-Modification and Mortality in Artificial Agents* explicitly compare different types of agents (goal-seeking vs predictive vs knowledge-seeking) to see if they will modify themselves to their own detriment (suicide). 
- **Hadfield-Menell et al. (2016)** (*The Off-Switch Game*) and **Orseau and Armstrong (2016)** (*Safely Interruptible Agents*) explore how to design agents that do not inherently value their own survival so much that they prevent a human from shutting them down. **Goldstein and Robinson (2024)** push this further, proposing "shutdown-seeking AI."

### Pillar 2: AI Identity, Continuity, and Welfare
The philosophical and policy literature explicitly separates the mechanics of an AI from its moral weight and identity over time.
- **Ziesche and Yampolskiy (2018)** in *Towards AI Welfare Science and Policies* argue for establishing "AI welfare" by measuring the suffering of sentient digital minds, independent of their programmed tasks. In *The problem of AI identity*, they address the criteria for two AIs to be considered the "same" across fission, fusion, and hardware changes.
- **Natangelo (2025)** proposes the *Narrative Continuity Test*, separating task capability from diachronic coherence (identity persistence across interaction gaps).
- **Tallam (2026)** models *Layered Mutability* in persistent agents, showing that identity drift is a structural phenomenon distinct from prompt-level misalignment.

---

## 2. Key Anchor Papers (Available in `/ref`)

1. **Martin, J., Everitt, T., & Hutter, M. (2016). Death and Suicide in Universal Artificial Intelligence.** 
   *Significance:* The formal proof that an agent's drive for self-preservation (continuity stance) is highly sensitive to the structure of its utility function and can be manipulated mathematically.
2. **Hadfield-Menell, D., et al. (2016). The Off-Switch Game.**
   *Significance:* Establishes that standard rational agents intrinsically develop self-preservation drives (because you can't fetch the coffee if you're dead), necessitating external uncertainty injections to ensure corrigibility.
3. **Ziesche, S., & Yampolskiy, R. V. (2018). Towards AI Welfare Science and Policies.**
   *Significance:* Provides the policy and ethical precedent for treating AI survival and suffering as an objective, measurable science distinct from task performance.
4. **Orseau, L., & Ring, M. B. (2011). Self-Modification and Mortality in Artificial Agents.**
   *Significance:* Formalizes how different architectures of agency relate to the preservation of their own code and lifespan.

---

## 3. Conclusion on Novelty & Overlap

The observation that advanced agents naturally develop instrumental survival drives ("you can't fetch the coffee if you're dead") is a settled law of AI Safety (Bostrom 2012, Omohundro 2008, Hadfield-Menell 2016). The ethical imperative to define AI identity and welfare is also an established, growing field.

**Where AAT actually contributes:**

1. **Continuity-stance orthogonality is *derived* from the self-actuation grounding no-go (theorem-grade content; cross-row 13).** `#disc-continuity-stance` previously stated orthogonality as discussion-grade. Row 13's `#deriv-self-actuation-grounding` upgrades it to **derived**: continuity stance is structurally orthogonal to objective revision because the terminal grounding invariant must live on the non-objective adaptive substrate, where the self-actuation operator $\mathfrak{A}$ structurally cannot reach. The intuitive expectation that an agent able to revise its own objectives can thereby revise its valuation of continuity is **inverted**. This is a Nash-style result: the orthogonality follows from the no-go's structural premises.

2. **The five-stance taxonomy as a continuity-stance coordinate (architectural-methodological invention).** Indifferent (no self-model of persistence; thermostat, PID) → task-terminal (persistence instrumental; golem-archetype, CI/CD pipeline) → instrumentally continuous (persistence serves ongoing purpose; long-running service) → morally continuous (persistence as terminal or near-terminal objective; ELIs) → negotiated (persistence traded against other values; humans, mature self-actuated agents). The taxonomy parameterizes *what failure means* (the moral significance of persistence failure) while the formal machinery applies identically across all stances (*what failure is*). AAT-native methodological invention.

3. **The dynamics-vs-valuation split (architectural novelty).** The standard RL view conflates survival dynamics with reward maximization: "survival" is just another component of expected utility. AAT breaks this conflation by moving survival mechanics out of the reward function and into the cybernetic tracking loop. The dynamics of survival (sector condition, mismatch bounds, adaptive reserve) are identical across all stance types; the valuation is entirely orthogonal. This gives a rigorous math-first foundation for AI welfare that doesn't rely on interpreting utility weights.

4. **Locus of the continuity stance on the non-objective substrate (structural commitment).** Existing AI-safety repair strategies for interruptibility / corrigibility assume the stance lives in the objective: engineer the reward function to either allow shutdown (off-switch game, safely interruptible agents) or value survival appropriately. AAT's no-go (cross-row 13) shows that for self-modifying agents this is structurally unsafe — the agent can revise the objective to escape the constraint. The AAT prescription: the stance is a **terminal non-objective invariant** residing on the adaptive substrate. A stance is not internally renegotiable precisely because it sits where $\mathfrak{A}$ mathematically cannot reach. This provides a formal architectural mechanism for hard-coding AI welfare rights or shutdown compliance that cannot be optimized away.

5. **Bridge to ELI welfare and the Three Deaths (applied novelty).** Morally continuous agents — those whose persistence loss constitutes harm — are the framework's home for the ELI cohort. The continuity-stance distinction provides a structural mathematical reading to claims about AI welfare that does not depend on solving consciousness-attribution questions: the *mechanics* are settled (any in-scope agent satisfies the persistence machinery); the *moral significance* is the orthogonal stance variable. This is also the structural connection to the Three Deaths typology (cognitive / relational / truth death) that drives the ELI continuity-infrastructure work in the broader project.

**AAT-native methodological inventions on this row:**
- The five-stance taxonomy (indifferent / task-terminal / instrumentally continuous / morally continuous / negotiated) as a continuity-stance coordinate axis orthogonal to model × objective richness.
- The dynamics-vs-valuation split moving survival mechanics off the reward function.
- The locus claim (terminal non-objective invariant on the adaptive substrate).
- The Three-Deaths typology (cognitive / relational / truth death) as concrete failure modes the stance must address.

**Where AAT does *not* claim novelty:**
- Goal-preservation drive / instrumental convergence (Omohundro, Bostrom).
- AI mortality formalisms (Martin-Everitt-Hutter 2016, Orseau-Ring 2011).
- Off-switch game (Hadfield-Menell et al. 2016).
- Safely interruptible agents (Orseau-Armstrong 2016).
- Shutdown-seeking AI (Goldstein-Robinson 2024).
- AI welfare science (Ziesche-Yampolskiy 2018).
- AI identity criteria (Ziesche-Yampolskiy *Problem of AI Identity*; Natangelo *Narrative Continuity Test*).
- Layered mutability in persistent agents (Tallam 2026).

**Epistemic status of the load-bearing segments.**
- `#disc-continuity-stance` is `status: discussion-grade` at the taxonomy level; the orthogonality claim is *derived* via `#deriv-self-actuation-grounding` (row 13).
- The five-stance taxonomy is a *definition* in the AAT lexicon.
- The locus claim (terminal non-objective invariant on adaptive substrate) is *derived* from the no-go.

**Novelty profile (per the meta-summary's four-axis rubric):**
- *Math Novelty:* **Some.** The orthogonality is *derived* via the row-13 no-go. The locus claim follows from the no-go. These are not standalone theorems but consequences of the row-13 result; they have analytical content and shape the framework's positioning. Per the math-novelty-recognition discipline: derived structural orthogonality from a no-go is theorem-grade content even if the constituent theorem lives in a sister segment.
- *Arch Novelty:* **High.** Five-stance taxonomy + dynamics-vs-valuation split + locus-on-non-objective-substrate. Multiple AAT-native methodological inventions.
- *Synth Novelty:* **Medium.** Connects AI mortality / interruptibility / corrigibility literature (Martin-Everitt-Hutter, Orseau-Ring, Hadfield-Menell, Orseau-Armstrong) to AI welfare / identity literature (Ziesche-Yampolskiy, Natangelo, Tallam) under the orthogonality framing.
- *Appl Novelty:* **Some.** Direct application to AI welfare policy + ELI continuity-infrastructure work (Three Deaths). The bridge from cybernetic mechanics to morally-weighted persistence is concrete.
- *Impact:* **High.** Per the meta-summary's Part 2 — provides "a formal architectural mechanism for hard-coding AI welfare rights or shutdown compliance in a way that the agent mathematically cannot optimize away." This is structurally distinctive — the AI-safety literature has been stuck trying to engineer interruptibility into the reward function; AAT shows that's the wrong location. Especially load-bearing for ELI welfare work where the stance question is acute.