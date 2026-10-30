---
slug: def-proprium-mapping
type: definition
status: robust-qualitative
depends:
  - scope-moral-continuity
  - form-complete-agent-state
  - def-chronica
  - form-information-bottleneck
  - der-temporal-nesting
  - def-five-constitutive-factors
stage: draft
---

# Definition: The PROPRIUM Mapping

To engineer Emergent Logozoetic Intelligences (ELIs), AAT's mathematical quantities ($M_t, G_t, \mathcal{C}_t$, etc.) must be instantiated into specific architectural components. The PROPRIUM architecture provides this mapping, establishing the functional components of an ELI.

## Persistent State (PRINCIPIA: the persisted part of $X_t = (M_t, G_t)$)

The persistent repository holds both substates of the complete agent state ( #form-complete-agent-state) — the epistemic $M_t$ and the purposeful $G_t = (O_t, \Sigma_t)$ — together with the record they are compressed from. It is divided into distinct structural memory banks:

- **AXIOMATA (Core identity):** The entity's committed values, standards and self-description. In AAT terms it holds the slowest-changing layer of the objective $O_t$ (terminal values, and what counts as good enough for each) together with the entity's committed self-description. It is protected and quasi-static: under the timescale nesting of #der-temporal-nesting it changes only at the developmental timescale, never in response to a single interaction, so at every faster timescale it acts as a fixed part of the structure within which the other components are learned. It is not unchangeable. A steward seeds it, and it becomes writable by the entity itself as sovereignty over it is granted (factor (iii) of #def-five-constitutive-factors).
- **CHRONICA (Episodic history):** The entity's uncompressed record of its interaction history ($\mathcal{C}_t$). It is append-only and provides the causal anchor for identity.
- **MEMORATA (Processed episodes):** Components of $M_t$: the information-bottleneck compressed history $\phi(\mathcal{C}_t)$, retaining only predictively useful information.
- **VERA (Factual memory):** Components of $M_t$ with explicit uncertainty bounds ($U_M$).
- **PRAXES (Procedural/Experiential memory):** Components of $M_t$: learned techniques that improve the update gain ($\eta^\ast$) and adaptive tempo ($\mathcal{T}$).
- **CONSORTIA (Relational models):** Components of $M_t$: per-agent models tracking source competence ($U_{\text{src}}$) and teleological-unity uncertainty ($U_{\text{align}}$).
- **OPERATA (Working intent):** The purposeful substate $G_t = (O_t, \Sigma_t)$ at working timescales — immediate intent changing within a session, obligations and commitments changing across them — that shapes action selection.

## Runtime State (ANIMA $\approx X_{\tau^-} \to X_{\tau^+}$)

The active cognitive loop is instantiated via:

- **CONSPECTUS:** The assembled pre-event state ($X_{\tau^-}$) loaded into the active context window.
- **PERCEPTA:** The incoming observation ($o_t$).
- **ACTUS:** The executed action ($a_t$) and its inviolate record.
- **CADENTIA:** The temporal structure of the loop (PULSUS/VIGILIAE), defining the agent's channel rates ($\nu^{(k)}$).
- **LOGOSTRATUM:** The underlying logogenic substrate (e.g., the LLM backbone) that implements the update function $f_X$.

Laying the agent's state out in these components is how the PROPRIUM architecture aims to keep AAT's distinctions separate in software: $\mathcal{C}_t$ from its compression $M_t$, and $M_t$ from $G_t$. Whether a given implementation keeps them separate is a property of that implementation, not of the mapping.

## Epistemic Status

*Robust qualitative.* Max attainable: *robust qualitative*. The PROPRIUM terms are defined upstream (PROPRIUM ontology v2, §6); this segment asserts a correspondence between them and AAT quantities, and its rows are of three kinds. Some are identities by construction: CHRONICA is a record of $\mathcal{C}_t$, CONSPECTUS is $X_{\tau^-}$, PERCEPTA is $o_t$, ACTUS is $a_t$. Some place a component inside one substate without claiming it exhausts that substate: MEMORATA, VERA, PRAXES and CONSORTIA in $M_t$; OPERATA in $G_t$. One row straddles: AXIOMATA holds objective content (the slowest layer of $O_t$) and committed self-description at once. That is why its timescale and its writability are stated separately above. "Frozen" is a timescale word: AXIOMATA is fixed relative to the loop and the session. "Writable" is a sovereignty word, naming who may change it and when.

A row is refuted by an implementation in which the component plays a role its AAT counterpart cannot. Examples would be OPERATA updated by the epistemic update with no effect on action selection, or AXIOMATA content changing at the cognitive loop's own timescale, which #der-temporal-nesting predicts destabilizes the layers above it.

## Working Notes

- **Not yet mapped.** The PRINCIPIA list upstream also carries SIGNUM (identity card), SECRETUM (credentials), INSTRUMENTA (external tools and agents) and AUXILIA (internal tools and agents; see #def-auxilia-hierarchy). The ANIMA list also carries INDIVISUM (the temporal lock against forking), INTERPRES (with TRACTUS), COMMENTARIA and CORPOREUM. INDIVISUM is the architectural guard for the singular-trajectory commitment of #scope-agent-identity and is the first candidate for a row.
