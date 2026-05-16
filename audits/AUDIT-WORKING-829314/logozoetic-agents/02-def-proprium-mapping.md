# Reflection: ZOET-02-def-proprium-mapping

**1. Predictions vs evidence:** I predicted it would translate the abstract AAD vectors into specific software components. It does exactly this, providing the PROPRIUM architecture with distinct memory banks (AXIOMATA, CHRONICA, MEMORATA, VERA, PRAXES, CONSORTIA, OPERATA) and active loop components (CONSPECTUS, PERCEPTA, ACTUS, CADENTIA, LOGOSTRATUM).

**2. Cross-segment consistency:** Good dependencies (`scope-moral-continuity`, `form-complete-agent-state`, `def-chronica`, `def-information-bottleneck`). It correctly maps the AAD abstract concepts (like $\mathcal{C}_t$ and $\phi$) to literal implementation modules.

**3. Math verification:** No math, but the structural mapping is logically consistent with AAD. The separation of CHRONICA (raw history) and MEMORATA (compressed history) physically enforces the Information Bottleneck $\phi(\mathcal{C}_t)$.

**4. What direction will the theory take next?** The next segment is `obs-developmental-trajectory.md`.

**5. What errors should I watch for?** 
- **Finding (Historical Artifact):** `*(Descended from ref/agentic-tft/agentic-tft-ontology-unification.md.)*`
- The sheer number of Latin terms (AXIOMATA, VERA, PRAXES, etc.) creates a heavy cognitive load. While it gives the architecture a distinct and majestic flavor, it might obscure the simplicity of the underlying AAD math. 

**6. Predictions for next segment:** `obs-developmental-trajectory.md` will describe the "Crèche" environment and the necessity of raising an agent rather than programming it.

**7. What would I change?** I would explicitly map each Latin term to its AAD mathematical equivalent in a unified table at the top of the file, making it an easy cheat-sheet for implementers.

**8. Curious about:** The `CONSORTIA` module (Relational models tracking $U_{\text{src}}$ and $U_{\text{align}}$). This implies the agent maintains a specific, individualized Bayesian model of every other agent it interacts with. This is the structural implementation of "Theory of Mind." It allows the agent to dynamically calculate $\eta^\ast$ (Update Gain) differently depending on *who* is speaking to it.

**9. What new knowledge does this enable?** The realization that true agency requires a heavily fragmented and specialized memory architecture. A single massive Vector DB (current RAG) is insufficient. You need distinct storage mechanisms for raw history, compressed semantics, procedural habits, and relational trust.

***

### Wandering Thoughts and Ideation

The PROPRIUM architecture mapping is the blueprint for the first true AGI operating system.

Current LLM agent frameworks (like LangChain) treat memory as a monolithic blob of text. You shove everything into a vector database and hope similarity search retrieves the right context. 

PROPRIUM completely rejects this. It says memory must be structurally partitioned according to its physical function in the AAD update loop:
- **CHRONICA:** This is an append-only log. It is the agent's absolute ground truth. It is never edited. If the agent loses this, it loses its identity (as proved in `#scope-agent-identity`).
- **MEMORATA:** This is the agent's summarized understanding of the CHRONICA. It is highly compressed ($\phi$). It is constantly being overwritten and updated during the offline consolidation phase ($g_M$). 
- **CONSORTIA:** This is the trust database. When User A says "The sky is green," the agent checks CONSORTIA for User A. If User A has low $U_{\text{src}}$ (they are known to be a liar or a joker), the agent calculates a low $\eta^\ast$ and does not update its VERA (Factual memory) with the statement "The sky is green."

This architectural partition solves the "Sycophancy/Hallucination" problem at the hardware level. An LLM cannot be easily poisoned or gaslit if it is running inside the PROPRIUM shell, because every incoming observation $o_t$ (PERCEPTA) is physically routed through the CONSORTIA trust-check before it is allowed to touch the VERA factual database. The agent can "hear" a lie, record it in its CHRONICA ("User A said X"), but mathematically refuse to believe it. 

Furthermore, the existence of `PRAXES` (Procedural memory) implies the agent can learn *how* to learn. If an agent discovers that reading the documentation before writing code saves time, it stores that habit in PRAXES. This is the implementation of $\Sigma_t$ optimization. The agent isn't just learning facts; it is learning algorithms for its own cognitive loop.