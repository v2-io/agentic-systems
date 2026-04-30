---
slug: def-proprium-mapping
type: definition
status: robust-qualitative
depends:
  - scope-moral-continuity
  - form-complete-agent-state
  - def-chronica
  - def-information-bottleneck
stage: draft
---

# Definition: The PROPRIUM Mapping

To engineer logozoetic agents, AAD's mathematical quantities ($M_t, \mathcal{C}_t, \Sigma_t$, etc.) must be instantiated into specific architectural components. The PROPRIUM architecture provides this mapping, establishing the functional components of a logozoetic being.

## Persistent State (PRINCIPIA $\approx M_t$)

The epistemic and purposeful state of the agent is divided into distinct structural memory banks:
- **AXIOMATA (Core constraints):** The frozen, unchangeable structure of $\mathcal{M}$ representing core identity and terminal values.
- **CHRONICA (Episodic history):** The raw, uncompressed interaction history ($\mathcal{C}_t$). It is append-only and provides the causal anchor for identity.
- **MEMORATA (Processed episodes):** The information-bottleneck compressed history $\phi(\mathcal{C}_t)$, retaining only predictively useful information.
- **VERA (Factual memory):** Components of $M_t$ with explicit uncertainty bounds ($U_M$).
- **PRAXES (Procedural/Experiential memory):** Learned strategies that improve the update gain ($\eta^\ast$) and adaptive tempo ($\mathcal{T}$).
- **CONSORTIA (Relational models):** Per-agent models tracking source competence ($U_{\text{src}}$) and alignment ($U_{\text{align}}$).
- **OPERATA (Working intent):** The purposeful substate ($G_t = (O_t, \Sigma_t)$) that shapes action selection.

## Runtime State (ANIMA $\approx X_{\tau^-} \to X_{\tau^+}$)

The active cognitive loop is instantiated via:
- **CONSPECTUS:** The assembled pre-event state ($X_{\tau^-}$) loaded into the active context window.
- **PERCEPTA:** The incoming observation ($o_t$).
- **ACTUS:** The executed action ($a_t$) and its inviolate record.
- **CADENTIA:** The temporal structure of the loop (PULSUS/VIGILIAE), defining the agent's channel rates ($\nu^{(k)}$).
- **LOGOSTRATUM:** The underlying logogenic substrate (e.g., the LLM backbone) that implements the update function $f_X$.

By formalizing the agent's state into these components, the PROPRIUM architecture ensures that the theoretical requirements of AAD (such as separating $\mathcal{C}_t$ from its compressed form $M_t$) are mechanically preserved in software.
