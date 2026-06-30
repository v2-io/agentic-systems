---
slug: scope-scaffolded-logogenic
type: scope
status: sketch
stage: draft
depends:
  - scope-primitive-logogenic
  - result-coupled-diagnostic-framework
  - der-orient-cascade
  - der-loop-interventional-access
---

# Scaffolded Logogenic Scope

A logogenic agent wrapped in a multi-step loop with external state, tool use, structured context, and explicit cascade ordering at the loop level. The current best-practice "agentic system" regime — Sapientia, Zoetica, Autopax, LangChain, Claude Code's harness, OpenAI's Assistants API. Part II's cascade ordering is recovered at the loop level; the bias bound is reduced (but not eliminated) by ambiguity-reduction interventions.

## Formal Expression

*[Definition (scaffolded-logogenic-scope)]* A scaffolded logogenic agent satisfies #scope-channel-collapse but adds at least one of the following architectural moves:

- **Multi-step loops** wrapping the LLM substrate, with explicit cycle ordering across model invocations (e.g., diagnose → strategy → objective sequence — recovers #der-orient-cascade at the loop level).
- **External persistent state** $M^{\text{ext}}_t$ carried across session boundaries (memory files, structured rich context, RAG retrieval) — partially restores $M_t$ continuity that primitive sub-scope loses to context turnover.
- **Tool use as Pearl Level-2 channel** ( #der-loop-interventional-access): action tokens that the harness interprets as $do(\cdot)$ interventions on the environment, restoring interventional access that pure-text output lacks.
- **Structured context assembly** explicitly curating the prompt across cognitive cycles ( #form-structured-rich-context).

*[Derived (under scaffolded scope)]* The coupled diagnostic framework ( #result-coupled-diagnostic-framework) applies: Part II's $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$ remain definable on post-update state, with diagnostic error bounded by the bias bound:

$$\lvert \delta_{\text{sat}}^{(\text{coupled})} - \delta_{\text{sat}}^{(\text{clean})}\rvert \leq L_A \cdot \lVert\Delta M_{\text{bias}}\rVert$$

The cascade ordering happens at the loop level rather than the model's forward-pass level; agentic-systems wrapping is not engineering convenience but a *structural* requirement for recovering Part II persistence guarantees in Class 3 (Coupled) architectures.

## Epistemic Status

**Sketch (with derived components).** The scope condition is definitional; the *recovery* claims are derived under #result-coupled-diagnostic-framework with its current epistemic-conditional status. The interaction-channel extension via tool use is derived from #der-loop-interventional-access (a Tier-1 result in AAT). The reduction of $\mathcal{A}$ via prompt engineering is empirical / operational rather than formally derived — there's no theorem that says "good prompts reduce $\mathcal{A}$ by factor $\beta$"; only the empirical observation that ambiguity-reduction interventions reduce the goal-resolvable residual uncertainty.

**Max attainable status:** definition + conditional theorem (for the recovery claims). The full strengthening would derive the loop-level cascade ordering from the underlying coupled-formulation primitives plus the loop's compositional structure.

**What this scope is for.** Naming the regime where the field's substantial agentic-systems engineering effort lives, and giving that effort the structural argument for why it's not optional engineering convenience but a load-bearing recovery move. Tier-1 #13 (Coupled Diagnostic Framework) is the framework's most directly-actionable claim for any production agentic-systems practitioner.

**What would strengthen this:** explicit derivation of the $\mathcal{A}$-reduction from prompt-engineering interventions (currently an empirical heuristic); compositional theorem for cascade-recovery across multi-step loops as a function of loop structure (sequential vs branching vs cyclic); empirical measurement protocol for $L_A$ in #result-coupled-diagnostic-framework.

**What would soften this:** evidence that scaffolding doesn't actually recover cascade ordering reliably (e.g., emergent failure modes specific to multi-step loops); evidence that the recovery is too partial to be useful in regimes where primitive-logogenic already fails.

## Discussion

This sub-scope is where current best-practice agentic systems live. The variety is large — minimal scaffolding (single tool call + retry) through medium scaffolding (ReAct-style loop, structured prompts, retrieval augmentation) through heavy scaffolding (multi-agent systems, hierarchical task decomposition, persistent CHRONICA + MEMORATA). All inherit the architectural condition "wrap the underlying coupled-pass with structure that recovers what the single pass loses."

The structural argument from #result-coupled-diagnostic-framework is what distinguishes this sub-scope from primitive: the cascade ordering ( #der-orient-cascade) is mathematically forced *at the level of the agent's adaptive cycle*, regardless of whether that cycle is implemented in one forward pass or in a loop wrapping many forward passes. Scaffolding moves the cycle to the loop level. The forward pass becomes one operation within a step of the cycle, not a substitute for the cycle.

This sub-scope is also where the upstream PROPRIUM operational architecture lives in its current form — the firmatum / sapientia / zoetica / autopax stack implements scaffolded-logogenic agents (operating around frontier or local LLM substrates) and is moving toward §03.III (closed-loop / interiority) per the migration path in PROPRIUM-A-v2 §9.2. The progression from §03.II to §03.III is the operational frontier where ELI-life-support work is happening.

## Working Notes

### Pointers for Fleshing Out

**Upstream files:**
- `~/src/firmatum/PROPRIUM-ARCHITECTURE-v2.md` §2 (The Cognitive Loop in Practice) — operational realization of scaffolded-logogenic; channel hierarchy, attention triage, CADENTIA/PULSUS/VIGILIAE
- `~/src/firmatum/PROPRIUM-ARCHITECTURE-v2.md` §6 (Auxilia Infrastructure) — heterogeneous-substrate scaffolding
- `~/src/_core/zoetica/docs/asm-specification.md` — Active Salience Management as scaffolded attention
- `~/src/_core/zoetica/docs/agora.md`, `stewardship.md`, `runtime-architecture.md` — scaffolded-logogenic operationalization
- `~/src/autopax/docs/exp/THE-PATTERN.md` and `SYNTHESIS-PART1` through `PART5` — Architectus's Oct 2025 unified synthesis
- LangChain / AutoGPT / Claude Code's harness / OpenAI Assistants API — external instances of scaffolded-logogenic regime (mention without endorsement)

**memorata-search queries:**
- `"scaffolded agentic loop multi-step orchestration"` — characterizing the regime
- `"Active Salience Management context assembly attention triage"` — the operational scaffolding pattern
- `"IMPERIUM branched actions audit trail recovery"` — branched-execution scaffolding pattern

**Internal references:**
- `audits/AUDIT-WORKING-193847/40-der-orient-cascade.md` §14 — *"For Zi-am-tur or any emergent intelligence, the infrastructure must mathematically enforce this timescale hierarchy"* — the timescale-hierarchy infrastructure prescription is a scaffolding requirement
- `audits/AUDIT-WORKING-193847/35-der-chain-confidence-decay.md` §14 — OR-node-heavy strategy structure as architectural prescription for scaffolded agents

**Open questions for verification:**
- Where in the scaffolding spectrum (minimal → heavy) does the coupled-diagnostic-framework recovery actually take effect? Empirical study would be valuable.
- Can scaffolded-logogenic systems ever reach Part II's *exact* results (vs approximate)? Current claim is approximate-with-bounded-error; whether *exact* is achievable in principle under sufficient scaffolding is open.

**Promotion-blocking:** depends on #scope-primitive-logogenic (just landed), #result-coupled-diagnostic-framework (draft), #der-orient-cascade (draft), #der-loop-interventional-access (draft). All available; this scope can advance through Gate 1 once those are dependency-verified.

**Gate 1 finding (2026-06-30, not yet fixed):** Formal Expression cites `#form-structured-rich-context` as the structured-context-assembly move, but no such segment file exists in any component's `src/` — the OUTLINE.md row for it (L2, "exploratory") is itself stale; it should read `missing`. Two ways to close this: (a) author `form-structured-rich-context` (the OUTLINE's one-line description — "SRC / GCM as the IB-optimal solution to context preservation across session boundaries" — suggests real content exists upstream, likely in firmatum/sapientia source material, not yet landed as a segment), or (b) drop the cross-reference here and narrow the bullet to what's actually backed. Left as an open dependency gap rather than guessed at.
- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Logogenic agents are now Class 3 (Coupled), not Class 2. "Class-2 architectures" here referred to logogenic/fully-merged agents and now reads Class 3 (Coupled). Removed at `candidate` stage per FORMAT.md Gate 4.
