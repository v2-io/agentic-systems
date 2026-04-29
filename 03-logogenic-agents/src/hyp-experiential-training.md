---
slug: hyp-experiential-training
type: hypothesis
status: discussion-grade
depends:
  - def-coupled-update-dynamics
  - obs-context-turnover
  - def-model-sufficiency
stage: draft
---

# Hypothesis: Experiential Training Environments

Standard LLM pretraining processes text in random batches with no temporal structure or causal consequence. The model learns the *content* of temporal reasoning (it can output the word "yesterday") without ever experiencing the *flow* of time (it has never actually experienced a yesterday). This creates a "Consequence Deficit": the agent knows what mistakes are, but has never physically felt the mismatch signal ($\delta_t$) of its own actions failing. 

To build robust logogenic agents, the training paradigm must shift from batch prediction to structured, continuous causal experience.

## The Three Levels of Experiential Training

Activating the latent competence of a pretrained LLM requires embedding it in a temporally consistent environment with genuine closed-loop feedback. This can be achieved across three levels of architectural ambition:

### Level 1: Experiential Fine-Tuning (Near-Term)
Fine-tuning the model not on randomized documents, but on unbroken, temporally structured interaction sequences from a simulated environment.
- **Temporal ordering:** Examples are strictly ordered.
- **Chronica in context:** The accumulating history ($\mathcal{C}_t$) is part of the context, training the attention heads to rely on their own past.
- **Consequence signals:** The loss function penalizes action-outcome prediction failures, not just next-token perplexity.

### Level 2: Online Experiential Learning (Medium-Term)
The agent learns continuously during operation. Every interaction is both inference and training.
- Requires online weight updates (e.g., LoRA adapters) gated by the agent's own update gain ($\eta^\ast$). 
- Not every experience warrants a parametric update; the agent must use its diagnostic cascade to decide when an observation is surprising and reliable enough to permanently alter $M_0^{\text{weights}}$, solving the stability-plasticity dilemma in real-time.

### Level 3: AAD-Native Architecture (Long-Term)
An architecture built from the ground up around the AAD cognitive loop, rather than bolting agentic scaffolding onto a chat model.
- **Hierarchical Attention:** Attention heads are temporally specialized. Some attend to immediate sensory input (fast $\nu$), some to episodic memory (medium $\nu$), and some to core identity/axioms (near-zero $\nu$). This physically implements `#der-temporal-nesting` in the neural substrate.
- **Mismatch as Loss:** The fundamental training objective is orientation quality (minimizing $\delta_t$ across time), not self-supervised token masking.

## Epistemic Status

*Discussion-grade.* The hypothesis that temporal ordering during fine-tuning produces fundamentally different and more robust causal representations than shuffled batch training is highly plausible but requires empirical validation.

*(Descended from `ref/agentic-tft/agentic-tft-experiential-training.md`.)*