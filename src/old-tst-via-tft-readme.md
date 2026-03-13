# TST via TFT: Temporal Software Theory Grounded in Temporal Feedback Theory

**Status**: Exploratory sketch. These documents represent early thinking about what TST would look like if rebuilt on TFT's formal foundations, extended with causal theory, and enriched by software development's unique epistemic advantages.

**Epistemic stance**: This is hypothesis-generation, not theorem-proving. Where I'm confident, I say so. Where I'm guessing, I mark it. The goal is to map the territory well enough that the next step — whether formalization, simulation, or refutation — becomes clear.

## Why This Exists

TST (Temporal Software Theory) was developed earlier as a practical theory of software engineering optimization. TFT (Temporal Feedback Theory) was developed independently as a formal theory of adaptive agents under uncertainty. They converge on remarkably similar insights from different directions:

- TST's "vicious cycle" IS TFT's persistence failure (T < rho)
- TST's "comprehension time" IS a domain-specific mismatch signal
- TST's "refactoring decision" IS TFT's structural adaptation trigger
- TST's "n_future estimation" IS TFT's Bayesian model updating

The question: what happens if we take TST's practical insights and ground them in TFT's formal machinery — and then go further, exploiting what software development uniquely offers?

## What Software Development Uniquely Offers

Most TFT domains (organisms, militaries, immune systems) have limited epistemic access. Software development has extraordinary access:

1. **The environment is fully inspectable.** Unlike a POMDP where Omega is hidden, the codebase state is (in principle) fully observable. The partial observability comes from the *agent's* limited attention and comprehension, not from the environment hiding state. This is a crucial distinction — the observation function h is lossy because of cognitive bandwidth, not physics.

2. **Level 3 counterfactuals are literally executable.** In most domains, counterfactual reasoning ("what would have happened if...") requires model-based simulation with uncertain fidelity. In software, you can `git checkout` a past state, make the alternative decision, and *run it*. This is Level 3 epistemic access with ground-truth verification — nearly unique among TFT domains.

3. **The causal DAG is partially explicit.** Import graphs, dependency declarations, API contracts, type systems — these are explicit causal structure. Change propagation follows these paths. This is richer than what most domains offer for causal identification.

4. **History is perfectly recorded.** Git provides a complete, immutable record of every change, when, by whom, and (ideally) why. This is C_t (chronica) without information loss — the full interaction history preserved exactly.

5. **Multiple agents interact through a shared, versioned artifact.** The codebase is a shared environment modified by multiple agents (developers, CI systems, bots, AI assistants), with git providing a conflict-resolution mechanism. This is Appendix F's multi-agent coupling made concrete.

6. **The observation channel quality is under the agent's control.** Code quality IS observation channel quality. Well-written code with clear naming is low U_o (easy to read accurately). Obfuscated code is high U_o. This means agents can improve their own future observation channels by writing better code — a feedback loop within the feedback loop.

These properties make software development not just another TFT instantiation, but potentially the *best testbed* for TFT's claims — and a domain where TFT can be extended beyond its current scope.

## Documents

| File | Contents |
|------|----------|
| [mapping.md](mapping.md) | The formal TFT → software development mapping |
| [causal-extensions.md](causal-extensions.md) | Causal DAGs, counterfactuals, and what lies beyond TFT |
| [simulation-proposals.md](simulation-proposals.md) | Concrete simulations to test and extend both theories |
| [reformulated-sketch.md](reformulated-sketch.md) | Sketch of what TST-via-TFT might look like as a theory |

## Key Open Questions

1. Is TST best understood as a *specialization* of TFT (same theory, specific domain), or does the software domain introduce genuinely new structure that requires extending TFT itself?

2. The "observation channel quality is under the agent's control" property (point 6 above) creates a second-order feedback loop that TFT doesn't currently model. How should this be formalized? The agent's actions (writing code) modify both the environment state AND the observation function h. TF-01 allows action-dependent observation (o_t = h(Omega_t, a_{t-1}, epsilon_t)), but the dependence there is on the *current* action, not on accumulated past actions shaping the channel itself.

3. How do we handle the fact that the "agent" in software development is not a single entity but a succession of entities with 100% context turnover (AI agents) or partial turnover (human team members joining/leaving)? TFT treats M_t as continuous. What happens when M_t is periodically reset to near-zero?

4. Can simulation-based counterfactuals (git fork + replay) provide the empirical grounding that both TFT's linear ODE hypothesis and TST's proportionality claims currently lack?
