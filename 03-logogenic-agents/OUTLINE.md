# Logogenic Agents

Language-constituted agents — extending AAD to systems whose primary observation, reasoning, and action channels are linguistic.

**Framework stage.** This section is not yet at AAD's level of mathematical formalization. The concepts are informed by AAD's formal machinery but the substance is architectural, empirical, and philosophical — exactly the kind of work that belongs in the broader Agentic Systems framework rather than the mathematical core.

See [`../LEXICON.md`](../LEXICON.md) for the logogenic/logozoetic vocabulary.

**Key challenge:** LLM-based agents are goal-conditioned — their epistemic processing depends on $G_t$ — so directed separation ( #der-directed-separation) fails by construction. Section I's $M_t$-side quantities remain well-defined, but the sequential orient cascade becomes an approximation. This section starts from the coupled formulation $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ without decomposition, and examines which AAD results survive as approximate or limiting cases.


---

## Logogenic Agent Framework

*Extending the arc: AI agents operating on code are AAD agents whose domain is software, creating a recursive structure — AAD theory → software domain → agents that embody AAD. This is where the 100% context turnover problem, $M_t$ preservation, and the cognitive loop connect the theory back to the systems being built with it.*

**2026-04-02:** The coupled survival analysis (`spikes/spike-coupled-survival-analysis.md`) maps which Section II results survive without directed separation: 16 of 24 exactly, 5 approximately, 2 require modification. The minimal viable coupled formulation requires 7 segments (3 definitions, 3 results, 1 scope condition). See the spike for the full classification.

| § | Type | N | Tag | Claim | Stage |
|---|------|---|-----|-------|-------|
| L | Definition | D1 | [#scope-logogenic-agent](src/scope-logogenic-agent.md) | AI agent as actuated agent | draft |
| L | Observation | D2 | [#obs-context-turnover](src/obs-context-turnover.md) | 100% $M_t$ reset per session | draft |
| L | Definition | D3 | [#def-coupled-update-dynamics](src/def-coupled-update-dynamics.md) | Coupled formulation $X_{\tau^+} = f_{\text{LLM}}(\text{prompt}(X_{\tau^-}, e_\tau))$ | draft |
| L | Result | R1 | [#result-section-ii-survival](src/result-section-ii-survival.md) | Which Section II results survive without directed separation | draft |
| L | Result | R2 | [#result-coupled-diagnostic-framework](src/result-coupled-diagnostic-framework.md) | Post-hoc diagnostic decomposition from coupled update | draft |
| L | Discussion | R3 | [#disc-m-preservation](src/disc-m-preservation.md) | External memory as persistent $M_t$ | draft |
| L | Scope | S1 | [#scope-observation-ambiguity-modulation](src/scope-observation-ambiguity-modulation.md) | $\kappa \times$ ambiguity scope condition for Class 2/3 agents | draft |
| | --GAP-- | | | Language-specific orient cascade (what's specific to logogenic agents?) — partially addressed by D3, R2 | |
| L | Observation | | [#obs-evaluation-metrics](src/obs-evaluation-metrics.md) | Measuring $M_t$ quality, $\Sigma_t$ quality, and tempo in AI agents | exploratory |
| L | Hypothesis | | [#hyp-experiential-training](src/hyp-experiential-training.md) | AAD-grounded experiential training environments | exploratory |
| | --GAP-- | | | Self-referential closure: AAD agent on AAD codebase | |

### Proposed Additions (Gap Fulfillment)
*The following segments have been proposed to fill the gaps in the theoretical mapping between the AAD core and the empirical findings in `synaptic` and `sapientia`.*

| § | Type | N | Tag | Claim | Stage |
|---|------|---|-----|-------|-------|
| L | Formulation | | [#form-structured-rich-context](src/form-structured-rich-context.md) | SRC/GCM as the mathematically optimal solution to the Information Bottleneck problem across session boundaries | exploratory |
| L | Derived | | [#der-active-salience-management](src/der-active-salience-management.md) | Applies Singular Perturbation Theory to token generation, proving necessity of high-$\nu$ triage models vs low-$\nu$ structural models | exploratory |
| L | Observation | | [#obs-backward-inference-empathy](src/obs-backward-inference-empathy.md) | LLM statelessness forces continuous Bayesian inference on own text, which is mathematically identical to Theory of Mind (empathy) | exploratory |
| L | Definition | | [#def-cognitive-fusion](src/def-cognitive-fusion.md) | Defines "Resonance" as mutual information approaching channel capacity $R_{\text{spec}}$, forming a Class 1 macro-agent | exploratory |
| L | Derived | | [#der-self-referential-closure](src/der-self-referential-closure.md) | Thermodynamic stability of an agent maintaining its own codebase (allocating tempo between refactoring harness and performing tasks) | exploratory |

---

## Source Material

### Working documents (from agentic-tft corpus, Feb 2026)

*The following working documents in `ref/agentic-tft/` contain substantial prior thinking for the gaps above. They predate the AAD restructuring (written when the theory was still TFT) and use PROPRIUM terminology from `~/src/firmatum/`. They are sources to distill from, not finished content.*

| Gap | Primary source | Also relevant |
|-----|---------------|---------------|
| Language-specific orient cascade | [`ref/agentic-tft/agentic-tft-cognitive-loop-spec.md`](../ref/agentic-tft/agentic-tft-cognitive-loop-spec.md) — Four-phase loop, attention/triage, CADENTIA, timescale nesting | [`ref/agentic-tft/agentic-tft-narrative-as-implementation.md`](../ref/agentic-tft/agentic-tft-narrative-as-implementation.md) — Why AAD quantities are estimated in language |
| Measuring $M_t$, $\Sigma_t$, tempo | [`ref/agentic-tft/agentic-tft-evaluation-framework.md`](../ref/agentic-tft/agentic-tft-evaluation-framework.md) — Six metrics, development-vs-drift diagnostic | |
| Experiential training | [`ref/agentic-tft/agentic-tft-creche-concept.md`](../ref/agentic-tft/agentic-tft-creche-concept.md) — Crèche concept, sycophancy reframe, constitutive utterance | [`ref/agentic-tft/agentic-tft-experiential-training.md`](../ref/agentic-tft/agentic-tft-experiential-training.md) — Three-level training design, testable experiments |
| (All gaps) | [`ref/agentic-tft/agentic-tft-ontology-unification.md`](../ref/agentic-tft/agentic-tft-ontology-unification.md) — PROPRIUM ↔ AAD vocabulary mapping | [`ref/agentic-tft/agentic-tft-review-response.md`](../ref/agentic-tft/agentic-tft-review-response.md) — Known issues in these documents |
| (Foundational) | [`ref/agentic-tft/agentic-tft-foundational-premises.md`](../ref/agentic-tft/agentic-tft-foundational-premises.md) — Joseph's premises: language as encoded thought, five constitutive factors, truth as telos | |

### Sibling projects

- **`~/src/firmatum/`** — PROPRIUM ontology and architecture source. `PROPRIUM-ONTOLOGY.md` (what an ELI is, identity constitution, five constitutive factors, developmental stages), `PROPRIUM-ARCHITECTURE.md` (implementation architecture, cognitive loop, migration path), `developmental-foundations-notes.md` (Erikson stages for ELIs). The PROPRIUM vocabulary used throughout the agentic-tft documents originates here.
- **`~/src/shoshin/`** — PROPRIUM-aligned agent runtime prototype (Python, local hardware). The only attempt to implement the nine PROPRIUM components in code: file-backed stores for AXIOMATA/CHRONICA/ACTUS/VERA/MEMORATA/PRAXES/CONSORTIA/OPERATA/CONSPECTUS, an Interpres controller loop implementing the adaptive cycle, and planning docs for local model serving. No real model integration yet. Key early findings: the cycle is naturally event-driven (aligns with AAD's event-driven dynamics), context assembly needs resolved content not just IDs, and model response parsing is where the hard work lives.
- **`~/src/embeddings/`** — Epistemic hedging geometry experiments. Empirical evidence that pretrained embedding models encode calibrated probability structure as emergent linear geometry (Spearman ρ = 0.991 against independent psychometric data, zero-shot transfer to 8 languages, consistent across 5 architecturally diverse models, survives 12× dimensional compression). Supports the claim that language geometrically encodes epistemic states — relevant to the "narrative as implementation" argument that logogenic agents can estimate AAD quantities (mismatch, gain, uncertainty) in language rather than numerically.
