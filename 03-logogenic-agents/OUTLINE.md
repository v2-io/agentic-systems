# Logogenic Agents

Language-constituted agents — extending ACT to systems whose primary observation, reasoning, and action channels are linguistic.

**Framework stage.** This section is not yet at ACT's level of mathematical formalization. The concepts are informed by ACT's formal machinery but the substance is architectural, empirical, and philosophical — exactly the kind of work that belongs in the broader Agentic Systems framework rather than the mathematical core.

See [`../LEXICON.md`](../LEXICON.md) for the logogenic/logozoetic vocabulary.

**Key challenge:** LLM-based agents are goal-conditioned — their epistemic processing depends on $G_t$ — so directed separation ( #directed-separation) fails by construction. Section I's $M_t$-side quantities remain well-defined, but the sequential orient cascade becomes an approximation. This section starts from the coupled formulation $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ without decomposition, and examines which ACT results survive as approximate or limiting cases.


---

## Logogenic Agent Framework

*Extending the arc: AI agents operating on code are ACT agents whose domain is software, creating a recursive structure — ACT theory → software domain → agents that embody ACT. This is where the 100% context turnover problem, $M_t$ preservation, and the cognitive loop connect the theory back to the systems being built with it.*

| § | Type | N | Tag | Claim | Stage |
|---|------|---|-----|-------|-------|
| L | Definition | | [#ai-agent-as-act-agent](src/ai-agent-as-act-agent.md) | AI agent as actuated agent | missing |
| L | Observation | | [#context-turnover](src/context-turnover.md) | 100% $M_t$ reset per session | missing |
| L | Discussion | | [#m-preservation](src/m-preservation.md) | External memory as persistent $M_t$ | missing |
| | --GAP-- | | | Language-specific orient cascade (what's specific to logogenic agents?) | |
| | --GAP-- | | | Measuring $M_t$ quality, $\Sigma_t$ quality, and tempo in AI agents | |
| | --GAP-- | | | ACT-grounded experiential training environments | |
| | --GAP-- | | | Self-referential closure: ACT agent on ACT codebase | |

---

## Source Material (from agentic-tft corpus, Feb 2026)

*The following working documents in `msc/` contain substantial prior thinking for the gaps above. They predate the ACT restructuring (written when the theory was still TFT) and use PROPRIUM terminology from `~/src/firmatum/`. They are sources to distill from, not finished content.*

| Gap | Primary source | Also relevant |
|-----|---------------|---------------|
| Language-specific orient cascade | [`msc/agentic-tft-cognitive-loop-spec.md`](../msc/agentic-tft-cognitive-loop-spec.md) — Four-phase loop, attention/triage, CADENTIA, timescale nesting | [`msc/agentic-tft-narrative-as-implementation.md`](../msc/agentic-tft-narrative-as-implementation.md) — Why ACT quantities are estimated in language |
| Measuring $M_t$, $\Sigma_t$, tempo | [`msc/agentic-tft-evaluation-framework.md`](../msc/agentic-tft-evaluation-framework.md) — Six metrics, development-vs-drift diagnostic | |
| Experiential training | [`msc/agentic-tft-creche-concept.md`](../msc/agentic-tft-creche-concept.md) — Crèche concept, sycophancy reframe, constitutive utterance | [`msc/agentic-tft-experiential-training.md`](../msc/agentic-tft-experiential-training.md) — Three-level training design, testable experiments |
| (All gaps) | [`msc/agentic-tft-ontology-unification.md`](../msc/agentic-tft-ontology-unification.md) — PROPRIUM ↔ ACT vocabulary mapping | [`msc/agentic-tft-review-response.md`](../msc/agentic-tft-review-response.md) — Known issues in these documents |
| (Foundational) | [`msc/agentic-tft-foundational-premises.md`](../msc/agentic-tft-foundational-premises.md) — Joseph's premises: language as encoded thought, five constitutive factors, truth as telos | |
