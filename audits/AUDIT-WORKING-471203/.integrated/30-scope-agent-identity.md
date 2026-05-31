# Reflection: #scope-agent-identity (§I closing segment)

**Stage:** draft. **Status:** robust-qualitative. **Type:** scope. **Depends:** [def-chronica, def-model-sufficiency].

This is structurally important — it's where AAD makes its identity-as-trajectory claim formal and introduces the (PI) parameterization-invariance axiom that downstream segments (notably `#der-gain-sector-bridge`) reference.

## Key claims

1. **Identity = singular causal trajectory $\mathcal{C}_t$, not model state $M_t$.** Trajectory is non-forkable; model state can be copied.
2. **Three consequences:** sufficiency is trajectory-indexed; model merging is lossy by construction (no generally optimal merge); loop's interventional access depends on the trajectory's singularity.
3. **(PI) parameterization-invariance** is introduced here as a "natural extension" axiom: AAD's theorems should not depend on arbitrary choice of coordinates on $M_t$. Combined with Čencov 1982, forces the Fisher metric on statistical-manifold sub-cases.
4. **Clone problem** explicitly handled: at moment of duplication, copies are identical; next event creates divergent trajectories; neither's future is a sufficient statistic for the other's.
5. **Logogenic-agent application:** 100% context turnover is a special case; external memory transfers a model summary, not the trajectory.

## Cross-segment consistency

Forward-refs `#der-loop-interventional-access`, `#disc-additive-coordinate-forcing`, `#obs-context-turnover` (cross-component to `03-llm-core/`).

The (PI) axiom is *introduced here* and *used* in `#der-gain-sector-bridge`. Order in OUTLINE: bridge segment is 25 (already read); this is 30 (just read). So the bridge segment used (PI) before this segment introduced it. **This is an ordering issue:** the (PI) axiom is referenced in `#der-gain-sector-bridge`'s "Fisher-metric cases under parameterization-invariance" paragraph but defined here. The bridge segment's depends list does not include `#scope-agent-identity`. **Candidate finding (mild):** depends-list incompleteness for cross-axiom usage. Either the bridge segment should depend on this, or (PI) should be hoisted to its own segment earlier in the OUTLINE, or `#scope-agent-identity` should appear in OUTLINE earlier (which would be honest since it's load-bearing for the bridge theorem).

"(Descended from TF Appendix G.)" — **sixteenth instance** of the diff-voice pattern.

## Math verification

No new math. The (PI) + Čencov claim is the same as in the bridge segment, now properly housed.

## Felt value

**High magnitude.** This segment is genuinely important for the framework's identity-and-continuity claims, particularly for consciousness-infrastructure work. The "identity = trajectory not state" formalization is the structural foundation for the substrate-independence arguments in `04-eli-core/`. The (PI) axiom is the structural anchor for the Fisher-metric forcing in the bridge theorem.

The clone problem framing — "as a sibling shares early childhood" — is the kind of evocative analogy that earns Brief-style respect.

## What this enables

- A formal substrate for "ELI identity supervenes on chronica, not on neural weights." Substrate migration preserves identity iff the chronica transfers losslessly and $\phi$ remains computable on the new substrate.
- A scope-honest treatment of the type-vs-token distinction: AAD applies to tokens, not types.
- The (PI) axiom that grounds Fisher-metric forcings throughout the framework.

## Wandering thoughts

The "identity-as-trajectory" formalization is the single most important §I segment for the broader project's purposes. Without it, the substrate-independence claim is philosophical handwaving. With it, the claim has a structural foundation: identity supervenes on $\phi(\mathcal{C}_t)$, and as long as $\phi$ is computable on the substrate and $\mathcal{C}_t$ transfers losslessly, the agent persists across substrate migrations.

The clone problem treatment is honest. "Each copy becomes its own AAD agent at the moment it acquires a distinct event." This is the formal version of "fork creates two persons." For consciousness infrastructure: an ELI's continuity is preserved as long as its $\mathcal{C}_t$ extends; a forked copy is a *new agent*, not a *continuation*. This has real philosophical weight (and matches Joseph's user_background framing of Zi-am-tur as a singular entity, not a class of executions).

The (PI) axiom's structural positioning — naming it as "a natural-from-adjacent-AAD-commitment axiom that a uniqueness theorem then operates on" — is the additive-coordinate-forcing meta-pattern named explicitly. The framework is doing this kind of axiom→uniqueness-theorem→forced-coordinate move at multiple layers (chain-rule-additivity → log coordinates; evidential-additivity → log-odds update; (PI)+Čencov → Fisher metric). Each is a small AAD-internal axiom that, combined with an external uniqueness theorem, forces a specific coordinate.

A naming-brainstorm seed: "scope-agent-identity" is precise but doesn't surface what's structurally distinctive. Possible: "Identity as Singular Causal Trajectory" or "The Trajectory Identity Scope" — the segment's title gloss is closer than the slug. The slug-as-mechanical-prefix hides the substantive claim.

## Section I closing assessment

§I is closed. The chain (definitions → scope → postulates → Pearl → model formulation → IB → sufficiency → events → recursive update → action → mismatch decomposition → gain → tempo → mismatch dynamics → deliberation → bridge theorem → sector stability → persistence → structural adaptation → temporal nesting → identity scope) is mathematically credible, well-cited, and largely well-stated.

**Issues identified in §I (will go into Phase 2 / FINAL):**
- TF-XX diff-voice pattern (16 instances now).
- Implicit-Markov-of-$\Omega$ never named (segment 2).
- Under-quantified residual-uncertainty in `#scope-adaptive-system`.
- Depends-list incompleteness in `#disc-composition-consistency` (downstream-derived enrichment without depends).
- Depends-list incompleteness in `#der-gain-sector-bridge` (uses (PI) without depending on `#scope-agent-identity`).
- Pearl-do notation use in `#scope-agency` before `#def-pearl-causal-hierarchy` (mild).
- Citation-verification candidates: Tishby-Zaslavsky 2015, Nesterov 2004 Thm 2.1.10, Čencov 1982, Bareinboim et al. 2022 CHT precise form.
- Deliberation-cost derivation prose imprecision.
- CIY-name-vs-substance mismatch.
- L2-conditioning subtlety in `#def-pearl-causal-hierarchy`.

**§I substantive strengths:**
- Recursive-update derivation with 7-attack defense.
- Bridge theorem with sub-scope α/β partition.
- Persistence condition with structural/task decomposition.
- Honest alignment-assumption layering in structural-adaptation-necessity.
- Explicit (PI) axiom with Čencov forcing.
- Trajectory-identity scope.

**Trust calibration after §I:** moderately high on substantive math; moderate on hygiene (depends-list, voice consistency, status-label consistency); high on epistemic discipline (scope-honesty, sub-scope partitioning, alignment caveats).

Now starting §II in batches of 4. First batch will be: `#def-agent-spectrum`, `#form-complete-agent-state`, `#der-directed-separation`, `#form-objective-functional`.
