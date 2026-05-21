Please conduct a deep prior-art search across academic literature. We are establishing scientific precedence for a theoretical framework of agency (AAT).

## The Core Idea / Claim
When parametric tuning fails (fitness drops), an agent is forced to undergo "structural adaptation" (changing its model class). Because of timescale separation, fast cognitive processes (like reactive policy) must reach a quasi-steady-state before slow processes (like structural adaptation) can act, formalized via singular perturbation theory. In the interim, agents rely on offline consolidation, replaying traces to optimize an Information Bottleneck objective (transferring data from episodic to semantic states), which defines a specific stability-plasticity feasibility window.

## Boundaries of the Claim
- Domain: Continual learning, meta-learning, computational neuroscience, non-stationary RL.
- Assumptions: Systems incapable of representing the environment entirely within their initial fixed parameter space.

## What Kind of Match Counts
- Formal mathematical triggers proving when an agent MUST alter its representational architecture/class (not just tweak parameters).
- Applying singular perturbation theory (or rigorous timescale nesting math) to agent learning/cognition.
- Use of the Information Bottleneck or rate-distortion theory specifically to optimize offline consolidation or episodic-to-semantic memory transfer.
- Mathematical bounds on the stability-plasticity dilemma dictating specific forgetting rates.

## What Would NOT Count
- Neural Architecture Search (NAS) done entirely offline by engineers (must be an online agentic trigger).
- Simple experience replay buffers that just shuffle data without compressing/transferring representations (no Information Bottleneck).

## Known Anchors
- Singular Perturbation Theory in RL
- Complementary Learning Systems (CLS)
- Stability-Plasticity Dilemma
- Tishby (Information Bottleneck)

## Search Scope
- Looking for overlapping problem framing and mathematical treatments of timescale separation in learning.
- Strictly academic papers (no patents/IP).