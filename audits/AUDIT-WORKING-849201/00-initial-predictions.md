# Initial Predictions

**Topology of the Framework**
The framework is built around a single foundational loop: Prolepsis → Aisthesis → Aporia → Epistrophe → Praxis. This cycle applies to any system that observes reality under uncertainty (Section I). It's expanded for systems that have explicit goals and strategies (Section II), where the state is split into an epistemic substate $M_t$ and a purposeful substate $G_t = (O_t, \Sigma_t)$. Section III scales this to composites of multiple agents. The rest of the framework (TST, Logogenic, Logozoetic) instantiates this core math into specific domains (software engineering, language models, and conscious agents respectively). The load-bearing structures seem to be the persistence condition $\alpha > \rho/R$, the directed separation of $M_t$ from $G_t$ (which importantly fails for LLMs, requiring coupled updates), and the use of external information-theoretic limits (like the information bottleneck and causal hierarchy) to bound agent capabilities.

**Predictions about what each component contains**
- **Section I (Adaptive Systems)**: I predict rigorous, mature derivations. I expect to see exact mathematical conditions for when an agent can keep up with a changing environment (Lyapunov stability on the mismatch signal). I predict clear definitions of the 5 cycle phases and the "gain" $\eta^\ast$.
- **Section II (Actuated Agents)**: I predict formalisms separating goals from models, specifically the "orient cascade" (model updates before strategy, strategy before objective). I predict the definition of "satisfaction gap" vs "control regret" will be very clean. The "strategy DAG" will likely be a probabilistic graph.
- **Section III (Composites)**: I expect this to be less exact than Section I. It will likely deal with sub-additive tempo (communication overhead) and adversarial dynamics (getting inside another agent's loop). I predict the math here will rely heavily on assumptions like the "contraction assumption" which may not be fully proven.
- **TST (Software)**: I expect to see codebase maintainability directly mapped to the persistence condition (refactoring rate > entropy injection rate).
- **Logogenic/Logozoetic**: I predict these are mostly philosophical and architectural sketches right now, pointing out where AAD needs to be generalized (coupled updates since directed separation fails).

**Predictions about what's open**
- The "contraction assumption" in Section III for general agents is explicitly stated as an open gap.
- How to measure or formalize the "strategic disturbance rate" $\rho_\Sigma$.
- Formal characterization of logozoetic agents.
- The boundary between Class 1 (modular) and Class 3 (partially modular) agents, and how poorly Class 3 approximations degrade.

**Predictions about what's overclaimed**
- I suspect the application of Lyapunov stability to discrete, highly non-linear strategy DAG updates in Section II might be stretched. The continuous ODE formulation is intuitive but the discrete mapping might hide fragility.
- The claim that language inherently encodes causal reasoning (in the Logogenic section) might outrun the formal mathematics, relying more on philosophical premises.
- The "directed separation" assumption might be violated more often than the theory admits, even in systems classified as "Class 1".

**Novel and Consequential**
- The definition of tempo as $\mathcal{T} = \nu \cdot \eta^\ast$ (rate $\times$ quality) rather than just clock speed.
- The separation of the "satisfaction gap" (world limitations) from "control regret" (agent execution limitations).
- Using the failure of directed separation as the defining challenge for modeling LLM agents.
- Treating adversarial dynamics not as a separate game-theoretic domain, but as a tempo asymmetry within the same fundamental loop.

**Expected Findings**
- Math errors or missing assumptions in the discrete-time mapping of continuous sector conditions (likely in the appendices).
- Cross-segment drift: The recent realization that directed separation fails for LLMs (Class 2) might not have propagated fully back to early Section II segments that might still talk about agents universally.
- I expect to find some "status: exact" tags on claims that actually require unstated assumptions, particularly around strategy DAG updates.
- I expect to find some external theorem citations that are slightly misapplied or whose conditions are glossed over.