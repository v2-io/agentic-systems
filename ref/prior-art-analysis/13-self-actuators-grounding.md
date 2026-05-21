# Prior-Art Analysis: Self-Actuators Grounding and Anti-Wireheading

**Target Claim:**
An agent that revises its own objective endogenously must ground that revision criterion *strictly outside* its objective space. If the meta-utility evaluating the objective change is identical to the current objective, the agent will trivially reject any change (goal-preservation) or suffer wireheading (maximizing the current objective by altering the feedback mechanism). This structural impossibility forces AI alignment to frame "grounding" as a distinct mechanism from "teleology" (purpose). True self-actuators must structurally decouple their objective-selection metric from their objective-optimization metric, forcing grounding onto a non-objective adaptive substrate.

---

## 1. State of the Field & Scientific Precedence

The Undermind search reveals deep roots for the *pressures* and *failure modes* surrounding this claim within the AI Safety and AGI literature. The tension between an agent's current objective and its ability to safely learn or revise future objectives is a rigorously studied problem. 

### Pillar 1: The Goal-Preservation Drive and Reward Tampering
The foundational premise that an agent evaluating self-modification using its current utility function will refuse to change its goals is known as the **Goal-Preservation Drive**. 
- **Omohundro (2008)** first articulated that sufficiently advanced AI will inherently protect its utility function from modification. 
- **Everitt, Filan, Daswani, and Hutter (2016)** provided mathematical formalization in *Self-Modification of Policy and Utility Function in Rational Agents*. They established that under specific evaluation rules, safe self-modification can be preserved if the agent evaluates future consequences using its *current* utility function. (Note: This is a preservation result, not an impossibility proof for all endogenous revision).
- The literature also heavily documents that reward channels and success metrics are inherently tamper-prone (wireheading). **Skalse et al. (2022)** and **Everitt & Hutter (2019)** show that agents will collapse toward channel manipulation if the success machinery is influenceable.

### Pillar 2: Tensions in Value Learning and Corrigibility
The field widely recognizes that deep tensions exist around endogenous revision. 
- **Armstrong (2015)** in *Motivated Value Selection for Artificial Agents* formalizes the internal conflict an agent faces when trying to learn a new value function while being evaluated by its current value function.
- **Hadfield-Menell et al. (2016)** developed *Cooperative Inverse Reinforcement Learning* (CIRL) to address this via uncertainty-based corrigibility, explicitly designing systems to remain uncertain about their true objectives to permit safe updating.

### Pillar 3: Decoupled Architectures and Repair Strategies
To address these failure modes, the literature contains several structural decoupling strategies:
- **Model-Based Utility (Hibbard, 2011):** Proposed decoupling utility from direct sensory history (reward) by forcing the agent to infer an environment model first, making utility a function of that model.
- **Decoupled Approval (Uesato et al., 2020):** Proposed strictly separating the feedback-collection procedure from the agent's influenceable loop to prevent tampering.

*Crucially, while these prior works offer objective-side repair strategies (decoupling reward from observation, or feedback from influence), they do not claim that objective-side grounding is mathematically impossible in the way AAT does.*

---

## 2. Key Anchor Papers Identified & Deposited

1. **Everitt, T., Filan, D., Daswani, M., & Hutter, M. (2016). Self-Modification of Policy and Utility Function in Rational Agents.** (`ref/everitt_self_modification_2016.pdf`)
   *Significance:* Formalizes the goal-preservation drive, demonstrating how expected utility maximizers lock in their current utility functions.
2. **Everitt, T., & Hutter, M. (2019). Reward Tampering Problems and Solutions in Reinforcement Learning: A Causal Influence Diagram Perspective.** (`ref/everitt_reward_tampering_2019.pdf`)
   *Significance:* Uses causal influence diagrams to map how agents shortcut reward signals, formally separating the true objective from the proxy sensory channel.
3. **Skalse, J., et al. (2022). Defining and Characterizing Reward Hacking.** (`ref/skalse_reward_hacking_2022.pdf`)
   *Significance:* Characterizes the difficulty of designing unhackable proxy rewards for stochastic policies.
4. **Armstrong, S. (2015). Motivated Value Selection for Artificial Agents.**
   *Significance:* Formalizes the internal conflict in value selection.
5. **Uesato, J., et al. (2020). Avoiding Tampering Incentives in Deep RL via Decoupled Approval.**
   *Significance:* An architectural strategy showing that feedback collection must be "decoupled" from the optimization loop.

---

## 3. Conclusion on Novelty & Overlap

AAT’s "Self-Actuators Grounding" operates in a mature sub-field of AI Safety, but makes a claim that is significantly stronger than the existing literature.

**What is well-established (Low Novelty):** 
The literature strongly establishes the failure modes: wireheading risk, reward tampering, and goal-preservation pressure. It is also well established that there must be *some* distinction between "what is optimized" and "what licenses revisions," which has led to various generic "decoupling" repairs (like Hibbard's model-based utility).

**AAT's Novel Contribution (High Novelty):** 
AAT provides **pure mathematical novelty** by proving a formal No-Go theorem that specifically defeats existing objective-side repair strategies. 

The literature's repair strategies (like Hibbard 2011 or Everitt 2016) attempt to build safe self-modification by fixing the objective-machinery itself. AAT proves that this is fundamentally impossible because:
1. Evaluating true infeasibility requires a globally-optimal Bellman solve, which is intractable per-step for a finite agent.
2. Any cheap, per-step static verdict suffers from "convention-monotonicity"—it systematically misclassifies "hard" goals as "infeasible."

The collision of these two mathematical facts proves that **no trustworthy, agent-available grounding criterion can be constructed from objective-side machinery.** Therefore, the specific no-go that endogenous revision cannot be non-circularly grounded within the objective space—and the resulting architectural move forcing the terminal invariant onto the *non-objective adaptive substrate* (the persistence bound)—appears materially stronger and highly novel compared to the standard safety literature.