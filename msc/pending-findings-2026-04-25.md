# Pending Findings — 2026-04-25 (from 2026-04-24 fresh-pass audit triad)

Three independent de novo audits ran in the same session on 2026-04-24: a primary pass by Claude Opus 4.7 (1M context) which initially produced "zero findings" then absorbed five-plus findings from independent Gemini and Codex re-audits of the same material. The session source document is `msc/audit-2026-04-24-fresh-pass.md` (likely to scroll out of attention; this file extracts what survives).

The audit's sustained engagement with ~45 of 109 AAD-core segments + selected TST segments + first-hand external-citation verification (Bretagnolle-Huber, Otto-Villani 2000) produced two kinds of output:

1. **Five verified findings + three partial findings** under burden-of-proof discipline. All were missed by the primary audit and surfaced by Gemini/Codex; the primary auditor's "Reading-mode failures" post-mortem is preserved in the source document and folded into the improved `msc/de-novo-audit-instructions.md`.
2. **One genuinely additive architectural proposal (B7)** plus six framing-level observations (B1–B6) that are mostly confirmation that the existing portfolio is on track. B7 is captured as **SP-21** in `PROPOSALS.md`. B1–B6 are captured below as orientation rather than separate proposals — they map onto SP-7, SP-9, SP-14, etc.

This document is integration only. Execution paths are flagged per finding; landing happens via TODO.md → segment edits.

**Read alongside.** `PROPOSALS.md` §G (SP-21 entry); TODO.md "Active — Pending Findings" (2026-04-25 batch).

---

## Provenance and confidence note

The primary audit's "zero findings" was a false negative caused by charitable reading on worked-example math and weak cross-segment consistency checks. The five verified findings emerged from Gemini/Codex independent passes; the primary auditor then verified each first-hand against segment text and re-derived the math where applicable. The current author (Claude Opus 4.7, 2026-04-25 session) further verified F-V1, F-V2, F-V3, F-V4, F-V5 against current src text first-hand before authoring this document. **Burden-of-proof discipline is therefore strong on the five verified findings**; partial findings are captured at the audit's confidence levels.

---

## Finding overlap map

| Audit source | Finding | Consolidated ID | Type | Confidence |
|---|---|---|---|---|
| Gemini | Discrete-to-continuous Model S variance gap mis-stated as $O((\eta^*)^2)$ | **F-V1** | Math error | High |
| Codex | `scope-multi-agent` excludes adversarial composites; `scope-composite-agent` admits via C-iv | **F-V2** | Cross-segment contradiction | High |
| Codex | C-iii mutual-benefit composites lack coherent $G_c = (O_c, \Sigma_c)$ | **F-V3** | Internal inconsistency (overlaps F8) | High |
| Codex | Sign error in zero-sum worked example in `deriv-strategic-composition` | **F-V4** | Math error in worked example | High |
| Codex | TST `scope-developer-agent` doesn't surface Class 2 caveats from logogenic-agents | **F-V5** | Cross-component integration debt | Medium-high → confirmed High this session |
| Gemini | "Not a discretization artifact" framing in `result-adversarial-tempo-advantage` is too strong | **P-V1** | Framing | Medium-high |
| Gemini | "Linear projections of linear dynamics are exact" in `result-unity-closure-mapping` is loose | **P-V2** | Framing | Medium |
| Codex | `hyp-causal-discovery-from-git` "causal direction for free" overstates `post-causal-structure` | **P-V3** | Framing (single sentence) | High |

---

## F-V1: Discrete-to-continuous Model S variance gap mis-stated

**Affected segments:**
- `01-aad-core/src/deriv-discrete-sector-condition.md` §"Recovery of continuous result" (line 147) and §"Fluid Limit Theorem" (line 163)
- `01-aad-core/src/detail-linear-ode-approximation.md` §6 "Discrete-time connection" (line 154) and Epistemic Status (line 186)

**Problematic passage** (`deriv-discrete-sector-condition.md` line 147): "The discrete-to-continuous gap for Model S variance is $O((\eta^\ast)^2 c^2_{\max})$ — the $(\eta^\ast)^2 \lVert F_d\rVert^2$ term that vanishes in the fluid limit."

**Direct re-derivation from the segment's own DA.1S** (verified by current author 2026-04-25):

From DA.1S: $V_{ss} = \sigma^2_{\text{step}}/(1 - \lambda^2_{\text{eff}})$ with $\lambda^2_{\text{eff}} = 1 - 2\eta^*c_{\min} + (\eta^*)^2 c^2_{\max}$. Substituting fluid-limit values $\sigma^2_{\text{step}} = n\sigma_w^2/\nu$ and $\eta^* = \mathcal{T}/\nu$, then Taylor-expanding at small $1/\nu$:

$$V_{ss} - V_c \approx \frac{n\sigma_w^2 c^2_{\max}}{4 c^2_{\min} \nu} = O(1/\nu) = O(\eta^*)$$

**Numerical check** (audit source, $\mathcal{T} = c_{\min} = c_{\max} = 1$, $n\sigma_w^2 = 2$): $\nu = 10$ gives gap $\approx 0.053$; $\nu = 100$ gives gap $\approx 0.005$. Ten-fold $\nu$ reduces gap ten-fold (consistent with $O(1/\nu)$), not hundred-fold (which $O(1/\nu^2)$ would require).

**Error mechanism.** The $(\eta^*)^2 c^2_{\max}$ coefficient on the recurrence's *correction term* in $1 - \lambda^2_{\text{eff}}$ is conflated with the asymptotic scaling of the *steady-state ratio*, which scales as $1/(1 - \lambda^2_{\text{eff}})$ in $\sigma^2_{\text{step}}$ — and the comparison-to-continuous involves $\sigma^2_{\text{step}}/\nu = O(1/\nu)$.

**Additional internal inconsistency** in `detail-linear-ode-approximation.md:163`: "the steady-state variance gap is $O((\eta^\ast)^2 c^2_{\max})$, which equals $O(\eta^\ast c_{\max} / \nu)$ when expressed in terms of the event rate." With $\eta^* = \mathcal{T}/\nu$, $(\eta^*)^2 c^2_{\max} = \mathcal{T}^2 c^2_{\max}/\nu^2$, but $\eta^* c_{\max}/\nu = \mathcal{T} c_{\max}/\nu^2$. These differ by a factor of $\eta^* c_{\max}$ — the sentence is internally inconsistent regardless of the asymptotic-scaling question.

**Counterevidence.** None — segment's own DA.1S formula gives $O(\eta^*)$ directly. The framework's `msc/spike-discrete-time-sector.md` (per Gemini) had it right: "$O(\eta^* c)$ correction." This is transcription drift from spike to segment.

**Status:** real, unresolved. Substantive impact on downstream is small (the gap is small either way in the fluid limit), but the asymptotic-scaling claim is wrong as stated.

**Confidence:** High (math is direct; verified two independent ways — Taylor expansion and numerical check).

**Landing path:** editorial math correction in two segments. Estimated effort: ~30 minutes for a careful agent. Mechanical; safe to delegate.

---

## F-V2: `scope-multi-agent` excludes adversarial pairs; `scope-composite-agent` admits them via C-iv

**Affected segments:**
- `01-aad-core/src/scope-multi-agent.md` lines 67–73 (Discussion §"The adversarial case is one end of a spectrum — but not a composite.")
- `01-aad-core/src/scope-composite-agent.md` lines 38–52 (C-iii and C-iv definitions) and line 89 (Discussion).

**Problematic passage** (scope-multi-agent.md:67–73): "**The adversarial case is one end of a spectrum — but not a composite.** Agents whose objectives conflict are multi-agent systems with negative teleological unity ( #def-unity-dimensions) and thus do not satisfy #scope-composite-agent: the absence of shared purpose means no composite agent exists.... Adversarial pairs are *excluded* from this scope."

**Direct counterevidence** (scope-composite-agent.md:89, verified 2026-04-25): "Adversarial pairs that admit Nash / CCE convergence via (C-iv) DO satisfy composition-scope-condition as strategic composites; adversarial pairs in cyclic / non-convergent regimes do not."

The two segments directly contradict. Route C-iv was added in the 2026-04-23 Gap A/B promotion sequence (commit `0d7b987`–`a739e9a` family); `scope-multi-agent.md` was not updated and still categorically excludes adversarial pairs.

**Status:** real, unresolved. Integration drift around a recently-added scope route.

**Confidence:** High.

**Landing path:** editorial fix in `scope-multi-agent.md` Discussion paragraph 2. The "Adversarial pairs are *excluded*" sentence becomes "Non-equilibrium-convergent adversarial pairs are *excluded* from this scope; equilibrium-convergent adversarial pairs admit composite status via (C-iv) of #scope-composite-agent — see #deriv-strategic-composition for the strategic-composite machinery." Agent-level-machinery vs. composite-level-machinery split should be retained but cleanly partitioned by C-iv. Estimated: ~20 minutes. Safe to delegate.

**Note:** F-V2 is technically subsumed by SP-21 (B7) if executed in the larger restructure. Editorial fix is independent and should land regardless — restructure is Tier 3 with an open decision point.

---

## F-V3: C-iii mutual-benefit composites lack coherent $G_c = (O_c, \Sigma_c)$

**Affected segment:** `01-aad-core/src/scope-composite-agent.md` lines 38–44 (C-iii) and line 79 (Discussion).

**Problematic passage** (lines 38–44): "**(C-iii) Mutual-benefit alignment**... Weakest route. *No explicit common objective*, but interactions are positive-sum in some dimension. Symbiotic coexistence; commensal ecologies; trading partners who share no goals beyond mutual benefit."

**Internal counterevidence** (line 79, same segment): "If the sub-agents' objectives do not align under any common $O_c$, then $G_c$ is ill-defined and the composite is a fiction."

**External counterevidence:** `form-composition-closure.md` (A1) requires the macro-state to decompose as $X_c = (M_c, G_c)$ with $G_c = (O_c, \Sigma_c)$.

The segment defines C-iii to permit composites without explicit $O_c$, then on the next page admits that without $O_c$ the composite is "a fiction." How C-iii is supposed to interact with the macro-state requirement is unspecified: induced $O_c$ from relevance variable $Y$? Different macro-object? Weaker machinery?

**Counterevidence search.** Already partially diagnosed in `msc/pending-findings-2026-04-22.md` as **F8** ("(C-iii) mutual-benefit vs (A1) decomposable $G_c$ gap"; status: "Open. 45–60 min scope-reconciliation; involves Joseph's Option A vs Option B decision"). The 2026-04-25 audit re-surfaces it as still unresolved.

**Status:** real internal inconsistency, partly diagnosed in msc/, unresolved at segment level. **F-V3 ≈ F8** — same finding from a different audit.

**Confidence:** High.

**Landing path (two paths, decision deferred to Joseph):**
- **Path A — narrow editorial.** Resolve F8/F-V3 in C-iii by making the induced-$O_c$ structure explicit: when (C-iii) holds, $O_c$ is induced from the relevance variable $Y$ (e.g., $O_c \propto Y$); macro-state requirement is preserved with a relevance-variable-derived $O_c$. ~45–60 min editorial work in `scope-composite-agent.md` and possibly `form-composition-closure.md`.
- **Path B — architectural restructure (= SP-21).** Split (C-i)–(C-iv) into distinct composite ontologies with their own macro-objects and theorem families. Each ontology is its own scope segment; `form-composition-closure.md` becomes route-conditional. Substantial architectural work. See `PROPOSALS.md` §G SP-21.

The two paths are not exclusive — Path A gives a working interim fix; Path B is the deeper move. Recommend Path A now (clears the contradiction); revisit as part of SP-21 evaluation.

---

## F-V4: Sign error in zero-sum worked example

**Affected segment:** `01-aad-core/src/deriv-strategic-composition.md` lines 70–76.

**Problematic passage** (verified 2026-04-25):
> Two agents $A, B$ with scalar actions $a_i \in [-1, 1]$ and state $s_{t+1} = s_t + a_A - a_B + w_t$, $w_t \sim \mathcal N(0, \sigma^2)$. Objectives $O_t^{(A)}(s) = s$, $O_t^{(B)}(s) = -s$ (zero-sum).
>
> The potential $\Phi(a_A, a_B) = a_A - a_B$ satisfies both agents' unilateral deviation conditions; this is a potential game. Nash equilibrium at $(a_A^\ast, a_B^\ast) = (1, -1)$ — $A$ pushes up maximally, $B$ pushes down maximally...

**Direct verification** (re-run by current author 2026-04-25):

Given $s_{t+1} = s_t + a_A - a_B + w_t$ and $O_B = -s = -s_t - a_A + a_B - w$. Then $\partial O_B/\partial a_B = +1$ (NOT $-1$, because $a_B$ enters $s$ with a $-$ sign and $O_B = -s$).

For Monderer-Shapley potential property: $\partial \Phi/\partial a_B = \partial O_B/\partial a_B = +1$. The segment's $\Phi = a_A - a_B$ gives $\partial \Phi/\partial a_B = -1$. **Sign error.**

**Correct potential:** $\Phi = a_A + a_B$. Both agents want to maximize their action.

**Best-response check at the segment's claimed NE $(1, -1)$:** B given $a_A = 1$ wants $\min s_{t+1} = \min(s_t + 1 - a_B + w)$, achieved at $a_B = +1$ (not $-1$). So $(1, -1)$ is not a Nash equilibrium — B has a profitable deviation.

**Correct NE: $(1, 1)$**, where $\Delta s = 0$ (the actions cancel — which is the *substantive* zero-sum property: equal opposing forces yield no net displacement).

**Error mechanism.** The intuitive framing ("$A$ pushes up maximally, $B$ pushes down maximally") confuses *direction of preference for the state* with *direction of action coefficient*. B prefers low $s$, but $a_B$ enters $s$ with a $-$ sign, so B's preferred action value is high $a_B$, not low.

**Counterevidence search.** Per Codex, the same error appears in `msc/spike-strategic-composition.md` — the spike was unreviewed rather than the segment compressing away a correction. Should be verified during the fix.

**Status:** real mathematical error in a worked example. Segment was promoted in 2026-04-23 Gap A/B cycle; the sign error is post-promotion drift, not a pre-promotion residue.

**Confidence:** High.

**Landing path:** editorial math correction. Replace lines 70–76 with the corrected version: $\Phi = a_A + a_B$; NE at $(1, 1)$; sector-template instantiation re-grounded around the correct NE; brief note explaining the substantive zero-sum interpretation (equal opposing forces → no net displacement). Cross-check `msc/spike-strategic-composition.md` for the same error and either correct in place (since it's source material the segment derives from) or annotate as superseded. Estimated: ~30 minutes. Safe to delegate, but the agent should run the math.

---

## F-V5: TST `scope-developer-agent` doesn't surface Class 2 architectural caveats

**Affected segment:** `02-tst-core/src/scope-developer-agent.md` (lines 63, 73, 166).

**Counterevidence segments:** `03-logogenic-agents/src/scope-logogenic-agent.md`, `03-logogenic-agents/src/def-coupled-update-dynamics.md`, `03-logogenic-agents/src/obs-context-turnover.md`.

**Problematic passages** in `scope-developer-agent.md`:
- Line 63: "For AI agents, $M_t$ is more explicitly representable (context window contents plus persistent storage), making it closer to a directly observable quantity."
- Line 73: "Objective revision occurs via the orient cascade ( #der-orient-cascade)..."
- Line 166: "For AI agents, $M_t$ is reset to near-zero at each session start."

**Direct counterevidence** (verified 2026-04-25):
- `scope-logogenic-agent.md` lines 35–41: LLM-based agent is **Class 2 (fully merged)** with $\kappa_{\text{processing}} \approx 1$. Boundary between $M_t$ and $G_t$ "has genuine latitude."
- `scope-logogenic-agent.md` line 70: effective state is $X_t^{\text{eff}} = (M_0^{\text{weights}}, X_t^{\text{context}})$ — weights provide the prior, context provides the update. Not just context window contents.
- `def-coupled-update-dynamics.md` lines 84–86: For Class 2, "the orient cascade ( #der-orient-cascade) does not hold as a derived result. The information dependency ($M_t$ feeds into $G_t$ evaluation) still exists logically, but is not enforced by the processing architecture."
- `obs-context-turnover.md` (per audit): session-start state is reconstructed from external memory + prompt + weights, not literally near-zero.

The TST scope-developer-agent treats AI agents using standard AAD apparatus (orient cascade as derived; $M_t$ reset to near-zero; "directly observable" $M_t$) without referencing the Class 2 architectural caveat from `der-directed-separation` or the more careful logogenic treatment.

**Status:** real cross-component integration debt. The framework has the Class 2 story in `03-logogenic-agents/`; TST hasn't absorbed it.

**Confidence:** High (verified first-hand 2026-04-25).

**Landing path:** editorial, but cross-component. Three integration moves:
1. Line 63: add "(but with Class 2 / $\kappa_{\text{processing}} \approx 1$ caveat — see `#scope-logogenic-agent`)" near "directly observable quantity."
2. Line 73: caveat orient-cascade invocation as Class 1 default; for AI-agent sub-case, cross-reference `#def-coupled-update-dynamics`'s coupled formulation.
3. Line 166: rewrite "$M_t$ is reset to near-zero" — effective state at session start is weights + memory + prompt, not literally near-zero. Cross-reference `#obs-context-turnover`.

Estimated: ~30–45 minutes. Should be done by an agent that has read both TST and logogenic-agents segments to keep the integration coherent. Safe to delegate with explicit instruction to read both sides.

---

## P-V1 (partial): "Not a discretization artifact" framing too strong in `result-adversarial-tempo-advantage`

**Affected segment:** `01-aad-core/src/result-adversarial-tempo-advantage.md` Working Notes.

**Audit characterization** (Gemini, captured 2026-04-25): The Working Notes attribute the simulation $b = 1.481$ vs $b = 3/2$ gap to non-artifact precision. In fact, the discrete steady-state ratio carries a correction factor proportional to $\sqrt{(2c_{\min} - \eta^\ast_A c^2_{\max})/(2c_{\min} - \eta^\ast_B c^2_{\max})}$ that gives values slightly below 3/2 when $\eta^\ast_A > \eta^\ast_B$. 1.481 is consistent with this correction, not just numerical noise around 1.5. The framework's *asymptotic-scaling* claim (3/2 in the fluid limit) is correct; the *dismissal* of the 0.019 gap is too quick.

Compounded with F-V1, this suggests the framework's discrete-vs-continuous accounting needs a careful pass.

**Status:** characterization unverified first-hand by current author; defer to audit's Confidence: medium-high.

**Landing path:** small Working Notes edit in `result-adversarial-tempo-advantage.md`. Could bundle with F-V1 fix. Estimated: ~15 minutes after F-V1 verification.

---

## P-V2 (partial): "Linear projections of linear dynamics are exact" loose framing in `result-unity-closure-mapping`

**Affected segment:** `01-aad-core/src/result-unity-closure-mapping.md`.

**Audit characterization** (Gemini, captured 2026-04-25): The same segment qualifies the claim with three exceptions (inconsistent projection, nonlinear micro-dynamics, heterogeneous update rules), but the punchline as stated overgeneralizes to cases where the projection's range is non-invariant under the dynamics matrix in ways the three bullets don't fully cover (cross-correlation in dynamics, anisotropic noise scales). `form-composition-closure.md`'s Mori-Zwanzig zero-lag bound $\varepsilon^\ast \geq \|Q_\Lambda U P_\Lambda\|_{\text{op}}$ correctly handles the general non-invariant-subspace case. The framework has the right machinery; the unity-closure-mapping segment's punchline could be tightened.

**Status:** characterization unverified first-hand by current author; defer to audit's Confidence: medium.

**Landing path:** Editorial tightening of punchline + cross-reference to `#form-composition-closure` MZ bound. Estimated: ~20 minutes.

---

## P-V3: `hyp-causal-discovery-from-git` "causal direction for free" overstates `post-causal-structure`

**Affected segment:** `01-aad-core/src/hyp-causal-discovery-from-git.md` line 30.

**Problematic passage:** "the temporal ordering provides causal direction for free."

**Counterevidence:** `post-causal-structure.md` itself states temporal ordering is "a statement about the *structure of possible influence*, not about actual influence."

The discovery segment includes substantial confounding discussion (C1–C3) and admits the chain to AAD quantities is "entirely empirical" and the hypothesis is "discussion-grade" — so the meta-frame is honest. The specific sentence is too strong.

**Status:** unverified first-hand by current author against current segment text; audit characterization is detailed and Confidence: high. Defer first-hand re-check to fix-time.

**Landing path:** one-sentence edit. "the temporal ordering provides causal direction for free" → "the temporal ordering provides a partial-order constraint on possible directions" (or similar matching `post-causal-structure`'s posture). Estimated: ~5 minutes. Trivial to delegate.

---

## Bigger-picture observations (B1–B6 — orientation, not separate proposals)

These are framings the audit produced from sustained engagement. Most are *confirmations* that the existing portfolio is on track (mapped to existing SP-IDs); one is genuinely additive (B7 = SP-21, captured separately). They are recorded here as orientation for the next audit cycle and the next framework-face reframe pass — not as new pending work.

| ID | Observation | Status / mapping |
|---|---|---|
| **B1** | "Form-shaping for external-theorem applicability" framing is sharper than the existing integration claim | Additive to **SP-7** (epistemic architecture). One-paragraph addition to OUTLINE preamble at next framing-pass. Captured here so the framing isn't lost. |
| **B2** | (T1) target-fixing as the implicit "where is the agent pointed?" precondition | Pedagogical reading of (T1)–(T3); not a structural addition. Could land as one-liner in `result-sector-persistence-template` Discussion. Low priority. |
| **B3** | α/β sub-scope partition could be presented as a positive taxonomy rather than scope-narrowing apology | Already mostly done in `deriv-sector-condition` "External mathematical lineage" subsection. Discussion-paragraph rewrite at framing-pass time. |
| **B4** | Signed-coupling unification axis could be named at meta-level if Section III matures | Already considered and parked per `msc/spike-compositional-coordinate.md`. Audit agrees with parking — five instances is thin. Re-evaluate after Section III completion (Bundle 2). |
| **B5** | Bregman-Fenchel reframe of `disc-additive-coordinate-forcing` should be elevated | = **SP-9** in `PROPOSALS.md` §E.3. Already gated on Bundle 1 framework-face reframe + Amari-Nagaoka 2000 PDF verification. Audit confirms the reframe is real geometric convergence, not coincidence — supports SP-9 priority. |
| **B6** | Persistence-cost result deserves more prominent placement | = **SP-14** in `PROPOSALS.md` §C.3 (channel-capacity as first-class quantity). Audit confirms framework-grade importance. |
| **B7** | Composite-agent scope routes (C-i/ii/iii/iv) should split into distinct composite ontologies | = **SP-21** in `PROPOSALS.md` §G. New proposal. Subsumes F-V2, F-V3, F8 if executed. |

---

## Substantive judgments (J1–J10) — confirmation at depth

The audit's J1–J10 (substantive judgments from sustained engagement, mostly Pattern-level) are confirmation findings — they confirm framework discipline holds at the segment level for the sample read. Notable confirmations worth preserving:

- **J1**: `disc-independence-audit`'s explicit naming of integration-bridges-as-load-bearing is the framework's distinctive contribution stated concretely.
- **J2**: Twenty-plus segments exhibit the same "external theorem + AAD form-shaping" structural shape. (External theorem citations spot-checked: Bretagnolle-Huber, Otto-Villani 2000 — both accurate in current segments.) **Form-shaping is the generative move** behind the integration claim.
- **J5**: 2×2 satisfaction-gap × control-regret diagnostic genuinely additive to active inference (EFE's preferences-as-priors form structurally collapses the disambiguation).
- **J6**: Signed-coupling structure unifies five Section III results derivationally (cooperative / adversarial / critical-mass / opacity / Miller's extreme-transition motif).
- **J7**: Class 1/2/3 + continuous $\kappa_{\text{processing}}$ co-existence with appropriate operationalizations is rare in applied frameworks — most pick discrete typology *or* continuous parameter, not both.
- **J8**: Worked examples (`example-kalman`, `example-bandit`, `example-L1`) honor what they should honor — explicit "manufactured for the example" labels, "demonstrably insufficient" Q-learner, exact L0 overestimation by covariance.
- **J10**: Formal-derivation core (`deriv-sector-condition`, `deriv-strategic-dynamics`, `deriv-recursive-update`, `der-gain-sector-bridge`) is rigorous mathematics applied carefully — not gestured. Specific sophistications: converse-Lyapunov scope-marking; per-edge attribution under coupling derivation; C1/C2/C3 constraint partition with honest C3-as-definitional admission; Nesterov 2.1.10 equivalence.

These are not findings; they are evidence that the framework's segment-level discipline is real for the sample audited. Recorded so the framework's confidence in its own current state is calibrated.

---

## Coverage caveats

The fresh-pass audit read ~45 of 109 AAD-core segments + selected TST. **Not read by the primary audit**: most foundational definitions; most Section III hypotheses (`hyp-directed-separation-under-composition`, `hyp-auftragstaktik-principle`, `hyp-communication-gain`, `obs-gates-advantage`); recently-promoted (`deriv-fisher-whitened-update-rule`, `deriv-l1-update-bias`, `deriv-variational-sector-condition`, `deriv-adaptive-gain-dynamics`); most TST (~20 segments); all of `03-logogenic-agents/` (touched in F-V5 verification this session); all of `04-logozoetic-agents/`. The judgments above are weighted toward AAD-core's load-bearing centers and recently-landed novel results; whether the framework's discipline holds across the unread segments is **Hypothesis**-level rather than **Tested**.

The improved `msc/de-novo-audit-instructions.md` was written to address the failure modes that produced this coverage gap and the false-negative "zero findings." Future audits running with the improved instructions will have stronger coverage and cross-segment-consistency discipline; redundancy with this batch is expected and acceptable.

---

*This file extracts the substantive content from `msc/audit-2026-04-24-fresh-pass.md` so the findings, B7 architectural proposal, and orientation observations survive the source document's likely scroll into obscurity. Source document retained in msc/ for reasoning-trail purposes.*
