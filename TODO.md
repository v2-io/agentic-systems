# TODO — Deferred Organizational Items

## Project Structure

- **Root-level assembly index.** A root OUTLINE.md or INDEX.md that assembles the full "Agentic Systems book" — covering all sections including ACT core, composition, software, logogenic agents, and framework-level content. Deferred until there is organized AS content beyond ACT to assemble.

- **`framework/` directory.** For structured non-mathematical content: architectural guidance, engineering patterns, philosophical foundations (emergence conditions, identity sufficiency, constitutive choice). Currently this material lives informally in msc/ and msc/reflections/. Create when enough content warrants organization.

- **Multiple index support.** The `bin/build` tool can already assemble any outline file. Future indexes for specific outputs: a paper (Sections I+II), a preprint, a monograph, topical selections. Each would be its own OUTLINE file selecting and ordering a subset of segments.

## Content

- **~~Absorb agentic-tft content.~~** Done (2026-03-20). Eight design-relevant documents moved to `msc/agentic-tft-*.md` with origin notes and relevance pointers. Five superseded documents moved to `_obs/agentic-tft-*`. References updated in `03-logogenic-agents/OUTLINE.md` (source material table), `04-logozoetic-agents/OUTLINE.md`, `WORKBENCH.md`, and `CLAUDE.md`. The documents are *sources* for logogenic/logozoetic work, not yet distilled into segments — that distillation should happen when the scope of `03-logogenic-agents/` is decided.

- **Section IV standalone paper outline.** Fastest path to external credibility — no theoretical blockers, high internal coherence (84% self-contained dependencies). Draft outline exists at `msc/2026-03-14-section-iv-paper-outline.md`.

- **Promote segments past draft.** 89 segments at `draft`, zero past it. The 15-20 strongest segments in Sections I+II should be promoted to `candidate` stage.

## Section II Diagnostic Chain — Codex Review (2026-04-02)

Six issues identified by Codex automated review. Items 1-3 are HIGH priority (affect core diagnostic chain); 4-6 are MEDIUM.

1. **HIGH — Q_O causal validity conditions on wrong state.** `value-object.md:25` defines action value from $M_t$, but actions are chosen from $(M_t, G_t)$. Conditioning on $M_t$ alone doesn't block confounding from $G_t$. Weakens $A_O$, $\delta_{\text{sat}}$, $\delta_{\text{regret}}$ as interventional diagnostics. Fix: condition on $X_t = (M_t, G_t)$ or explicitly assume $G_t$ fixed.

2. **HIGH — Orient cascade contradicts 2×2 diagnostic.** `control-regret.md:32` includes the $\delta_{\text{sat}} > 0$, $\delta_{\text{regret}} \gg 0$ quadrant ("hard goal + weak strategy → revise $\Sigma_t$ first"). But `orient-cascade.md:28` only evaluates $\delta_{\text{regret}}$ "if feasible" (i.e., $\delta_{\text{sat}} \leq 0$), removing the exact quadrant needed to distinguish "hard goal" from "hard goal plus weak strategy."

3. **HIGH — Strategy-persistence overstates Prop B.5.** `strategy-persistence-schema.md:50` says strategic mismatch is "Resolved" citing B.5. But `strategic-dynamics-derivation.md:290` says B.5 is about plan-confidence error $\delta_s$, not the strategic-calibration residual $\delta_{\text{strategic}}$, and `:292` says extending to $\delta_{\text{strategic}}$ still requires credit-assignment machinery. Direct inconsistency.

4. **MEDIUM — Composition bridge assumes extra contraction.** `composition-closure.md:121` states bridge lemma requires macro-update contraction, `:161` admits this is additional (not from (A4)). But `tempo-composition.md:27` treats the defect→overhead link as "follows directly." Downstream prose stronger than proof status.

5. **MEDIUM — A_O mixes full-policy and one-step attainability.** `satisfaction-gap.md:19` defines $A_O$ as supremum over policies (full-policy). `value-object.md:35` uses one-step improvement with $\pi_{\text{cont}} = \pi_{\text{current}}$ as the canonical default. These differ unless $\Pi$ is restricted to one-step deviations. Meaning of control regret changes.

6. **MEDIUM — Graph-structure-uniqueness overclaims.** `:15` says four postulates "force" a DAG with Markov property, but `:179` and `:203` say P3→Markov is conditional/open. Acyclicity is strong; "forced Markov DAG" is not.

## Tooling

- **Lint-md directory arguments.** Currently accepts file paths; could accept directory paths to lint all .md files within. Low priority.
