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

**AAT's Novel Contribution:**
AAT's contribution is **Architectural and Epistemological**, specifically in *how* it structures the agent's relationship to its survival.

1. **Orthogonality of Teleology and Dynamics:** In standard RL (like AIXI), "survival" is just another component of the expected utility calculation (a reward maximization). AAT breaks this conflation. AAT proves that the *dynamics of survival* (the sector condition, mismatch bounds) are identical across all systems, but the *valuation of survival* (the continuity stance) is entirely orthogonal. By moving survival mechanics out of the reward function and into the cybernetic tracking loop, AAT creates a rigorous, math-first foundation for AI welfare that doesn't rely on interpreting utility weights.
2. **The Locus of the Continuity Stance:** The prior art assumes that if we want an agent to allow itself to be shut down (or conversely, to defend its own life), we must engineer that into its objective/reward function. AAT utilizes its No-Go theorem (Topic 03) to prove that for a self-modifying agent, this is structurally unsafe. AAT asserts the highly novel claim that a true continuity stance must be a **terminal non-objective invariant** residing on the adaptive substrate. A stance is not internally renegotiable precisely because it sits where the objective-editing self-actuation operator mathematically cannot reach. This provides a formal architectural mechanism for hard-coding AI welfare rights (or shutdown compliance) that cannot be optimized away by the agent.