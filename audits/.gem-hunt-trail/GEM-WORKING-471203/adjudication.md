# Gem-hunt adjudication — audit-findings-471203

*Gem-hunt cycle 2026-05-29. Slice: `audits/audit-findings-471203.md`. Report-only — no canon edits/moves/commits. Adjudicator: Claude Opus 4.8 (1M).*

## Bottom line

This audit was **well mined already**, and the extraction file (`audit-findings-471203.md`) is itself a strong second-pass mining of the WORKING dir. The prior pilot, however, **explicitly deferred** first-hand verification of its own "Fresh" items (Part III) against current `src/` ("didn't have time" — see its First-Pass Scrutiny table). That deferred work is the un-captured remainder, and it is what I did first-hand.

The dominant result is a **careful negative with a strong positive sub-finding**: of the 17 Fresh items the pilot surfaced and deferred, **all the load-bearing ones have since landed in canon — and several landed *strengthened beyond* what the audit proposed** (the central confirmation that audit dispositions are drifted proxies). The single genuinely un-captured gem of substance is small and editorial (Fresh-8). There is one real research-seed that remains open and un-tracked (Fresh-14, continuous-state structural change). Everything else is captured, superseded, or already-tracked.

No already-routed disposition was found wrong against current canon. One minor dangling-reference observation is flagged.

All loci below were opened first-hand (grep + read) in the named segments, not inferred from audit labels.

---

## (A) Ready-to-land

### A1. Fresh-8 — model-conditioned-L2 vs true-Pearl-L2 clarifying half-sentence

1. **What it is, actionably.** `#def-pearl-causal-hierarchy` states Level 2 as $P(o_t \mid do(a_{t-1}), M_{t-1})$ — conditioning the $do(\cdot)$ query on the agent's *own model* $M_{t-1}$. In Pearl's standard formulation $do(\cdot)$ is defined relative to the *true* SCM, so AAT's L2 query is a **belief-about-L2** operation: the loop genuinely generates L2 *data*, but the agent's *interpretation* of it is model-conditioned. The fix is one half-sentence in the L2 paragraph noting this, to head off the "loop generates true L2 data ⇒ agent has true L2 access" misreading.

2. **Canon loci checked (first-hand).**
   - `01-aat-core/src/def-pearl-causal-hierarchy.md:37` — the $M_{t-1}$-conditioned L2 formula; `:41` ("what will happen *because* I take this action") and `:43` ("interventional signal") do **not** name the belief-vs-true distinction.
   - `:53,55,59` (Epistemic Status / "Availability vs. exploitation") — these distinguish *structural availability* from *exploitation*, and point to the regime-indexed framing, but do not address the model-conditioning subtlety per se.
   - `01-aat-core/src/scope-edge-update-causal-validity.md:16,18,89` — the honest companion: edge credences "*claim to approximate* the interventional quantity $P(j \mid do(i), M_t)$"; three admissibility regimes A/B/C; "robust qualitative." This is where AAT's identification-strength honesty lives — but it sits in the *strategy-edge* segment, one layer downstream from where a reader first meets L2.

3. **Why a gem (wisdom).** Honesty-of-scope is AAT's load-bearing virtue. The reader who meets L2 first (in `def-pearl-causal-hierarchy`) and not the edge-update scope segment can over-read "the loop is a Level-2 engine" as conferring *true* causal access. The half-sentence makes the belief/true distinction visible at first encounter — strengthen-first: it surfaces, at the definition, the scope-honesty that the regime-A/B/C apparatus already carries downstream. Low-severity but genuinely un-captured.

4. **Recommended home.** A half-sentence in the L2 paragraph of `#def-pearl-causal-hierarchy` (after `:41`), e.g. noting that conditioning on $M_{t-1}$ makes this *the agent's interventional query relative to its own model* — the loop data is genuinely L2, the agent's reading of it is model-conditioned and identification-strength-bounded (forward-pointer to `#scope-edge-update-causal-validity`'s regimes). Verification + landing are yours.

---

## (B) Research-seeds

### B1. Fresh-14 — continuous-state structural-change analog (genuinely open, un-tracked)

1. **What it is, actionably.** `#form-structural-change-as-parametric-limit` grounds "structural change is the limit of continuous edge-weight operations" on Miller (2022)'s *finite-state* neutral-mutation / extreme-transition motif. Continuous-state agents (LLMs; gradient flows in a billion-dim parameter space) have a different structural-change geometry — there is no clean "neutral mutation into an inaccessible state region" analog for a smooth parameter manifold. The framework's cross-domain structural-adaptation claim needs a continuous-state mechanism *distinct from* the Miller automaton bridge.

2. **Canon loci checked (first-hand).**
   - `01-aat-core/src/form-structural-change-as-parametric-limit.md:13,15,34,44,46` — Miller's automaton construction is applied to the **discrete** strategy-DAG (edges, prune/graft, near-zero-credence latent edges). Line 46 is explicit that this is the *finite-state* automaton setting.
   - `:48` mentions LLMs only re: *pruning under bounded context capacity* — not structural-change geometry.
   - No continuous-state / gradient-flow structural-change segment exists in `01-aat-core/src/` or `03-llm-core/src/` (checked the directory; `#result-structural-adaptation-necessity` is the model-class-change result, single-agent, not the continuous-state mechanism).

3. **Why a gem (strength + relevance).** This is a real open extension of a load-bearing cross-domain claim, directly relevant to `03-llm-core/` (fine-tuning / in-context structural adaptation) and to the "AAT's structural-adaptation machinery applies cross-domain" assertion. Strengthen-first: it would *derive* the continuous-state analog rather than soften the cross-domain claim. Not currently in `spikes/PROPOSED.md` (Fresh-4's effects-spiral and Fresh-12's $f(Q)$ bistability *are* there; this one is not).

4. **Concrete first task.** Spike: *does the strategy-DAG continuous-edge-weight limit have a clean continuous-state analog for parameter-space agents, or is a genuinely different mechanism needed?* Candidate framings to test against the Miller bridge: (a) loss-landscape mode-connectivity / basin-hopping as the "neutral drift → niche → cascade" analog; (b) lottery-ticket / sparse-subnetwork emergence as latent-structure-becoming-load-bearing. Outcome lands either as an extension to `#form-structural-change-as-parametric-limit` (continuous-state Discussion) or as a `03-llm-core/` segment. Recommend a `spikes/PROPOSED.md` entry regardless.

### B2. (Already-tracked seeds — confirm, do not re-launch)

These Fresh items are *already* captured as tracked research-seeds; named here only so they aren't re-surfaced as new:
- **Fresh-4** (effects-spiral $\gamma_A(\lVert\delta_B\rVert)$ functional form) — `spikes/PROPOSED.md` Tier 1 ("Effects-spiral eigenvalue condition"); see A-side note below, it is *strengthened* in canon.
- **Fresh-12** ($f(Q)$ code-quality bistability) — `spikes/PROPOSED.md` Tier 3 ("Code-quality bistability — 2D dynamical formalization"); `02-tst-core/src/der-code-quality-as-observation-infrastructure.md:135`.
- **Fresh-13** identity-continuity follow-ons — `spikes/continuity-persistence/` §4.2 (named in `03-llm-core/src/disc-m-preservation.md:110` Working Notes).
- **S4–S7** (PI-uniqueness, composed-impossibilities, hysteresis, CIY-name) — open on `polish-and-sentiment-ledger.md:40-43`.

---

## Captured / superseded (the careful negative — with loci proving it)

Each was checked first-hand; the audit's hint had drifted out from under its label because the content has since landed (often strengthened). **Hard-constraint check passed: none of these would have to be re-derived — they are present.**

| Fresh-ID | Audit hint | Verified canon locus | Status |
|---|---|---|---|
| **Fresh-2** | derive absorbing-state escape *economics* (qualitative → quantitative) | `der-observability-dominance.md:15,17,57` — **observability-investment tradeoff** is *derived*: $\alpha_\Sigma$ improvement from plan-level $1/(n_\Phi+1)$ to weakest-link rate, = persistence-margin gain | **Captured + strengthened** (qualitative→derived, as the audit's strengthen-first hoped) |
| **Fresh-3** | add sub-scope-$\alpha$ condition to 16-cell closed-form | `der-agent-opacity.md:161` (Working Notes) states it verbatim: closed-form arg-max "only under sub-scope $\alpha$ coupling; general non-convex coupling requires per-case optimization"; `:90` names the open sharp-functional-form | **Captured** (exactly the editorial fix proposed) |
| **Fresh-4** | formalize effects-spiral functional form (heuristic→derived) | `der-adversarial-destabilization.md:67,73` — kept honestly discussion-grade **and** added the **Cheung-Piliouras-Tao 2021 no-spiral converse** (a strengthen-first *dual* result); open piece tracked at PROPOSED Tier 1 | **Captured + strengthened**; open derivation tracked |
| **Fresh-5** | Fano-inequality 4th identifiability-floor instance | `disc-identifiability-floor.md` now has **four instances** (CHT/Cramér-Rao/Liberzon/Kalman-Ho); `:122` explicitly: "Fano degenerates at $I=0$, the right tool for the finite-sample refinement rather than the exact anchor"; `:145` cites the tested-and-routed 4th-instance spike | **Superseded** — slot filled by Kalman-Ho; Fano correctly re-placed as finite-sample refinement, not the anchor |
| **Fresh-6** | "anchor-plus-three-theorem" as M3 framing | `der-chain-confidence-decay.md:58` carries the exact framing; full catalog in `#disc-additive-coordinate-forcing` | **Captured** |
| **Fresh-7** | triple compound depth penalty as cross-segment result | `der-chain-confidence-decay.md:14,56` names the **triple penalty** (decay + starvation + cost, $d^\ast=$ min over three); `scope-edge-update-causal-validity.md:22` adds a *fourth* (identifiability) | **Captured** (richer than the audit framed) |
| **Fresh-9** | check downstream $\delta_{\text{sat}}$/$\delta_{\text{regret}}$ specify C1/C2/C3 convention | `def-value-object.md:23,51` (C1 canonical default + "comparable across analyses") and `def-satisfaction-gap.md:17,52-58` ("convention is part of the measurement; do not compare directly") establish the discipline at the source; C1-default means inheritance is correct unless overridden | **Effectively closed** — at most a one-off lint nicety, not a content gap |
| **Fresh-10** | promote TST's "three overclaim guards" to project-wide (CLAUDE.md) | `obs-software-epistemic-properties.md:95-101` carries all three verbatim; **not** in CLAUDE.md (grep empty). CLAUDE.md already has adjacent disciplines ("Math-novelty recognition", "scope precision is the CS norm") | **Captured in TST**; project-wide promotion is soft/framing only — low-value |
| **Fresh-12** | 2D $\dot Q=g(\mathcal T,Q)$ to formalize bifurcation | `der-code-quality-as-observation-infrastructure.md:135` proposes exactly this; indexed `spikes/PROPOSED.md` Tier 3 | **Captured as tracked seed** (= B2) |
| **Fresh-13** | random-walk-on-sufficiency formalization of accumulation problem | `disc-m-preservation.md:76,80,84,110` — the hypothesis-grade $\mathbb E[\Delta\epsilon_k]\le\mathbb E[\Delta I_k]$ was **deleted and replaced** by the *exact* affine information recursion $I_{k+1}\le\eta_k I_k+a_k$ in `#der-turnover-information-recursion` (multiplicative SDPI contraction, geometric no-go); identity-continuity split into a distinct operator | **Captured + strengthened beyond the audit** — textbook integration-is-replacement; the "do ELIs experience identity drift?" question now has its precise quantitative home |
| **Fresh-16** | κ_processing distribution-dependence propagation | `der-directed-separation.md:91,99` carries the caveat **and** the architectural resolution: Class 1 → κ≈0 under all distributions, Class 3 → high under most, only Class 2 distribution-variable; explicitly *replaces* the κ-as-scalar framing | **Superseded** — the worry (scalar-κ drift) is resolved at root |
| **Fresh-1 (Kind A)** | FORMAT.md needs external-standard-notation exemption | `FORMAT.md:88-93` — **"Imported external machinery with internal recapitulation — convention"** explicitly covers Pearl-$do$; cross-ref'd at `#scope-agency:30`, `#the-cycle-in-motion-intro:40` | **Captured** (Kind A closed) |
| **Fresh-17** | Hafez IDT 89%/44% citation | resolved in SUPPLEMENT §J (89.3±15.1% vs 44.0±26.1%, 168 trials; no separate IDT paper) | **Already resolved** (pilot confirmed) |

**Part I/II findings** (F1–F7 trail, §F observations): all confirmed `subsumed-by-FINAL/SUPPLEMENT/MANIFEST` and re-verified by the pilot first-hand (its First-Pass Scrutiny tables). I spot-re-checked the disposition records (`MANIFEST.md:67,139,174`; `polish-and-sentiment-ledger.md:40-43,59,78`) — consistent, no drift. Not re-listed here.

---

## Low-value / not-worth-landing

- **Fresh-1 Kind A vs Kind B *carving rationale*** (the disambiguation that the two depends-incompleteness shapes have different remediation paths). The *remediations* both landed (Kind A → FORMAT.md:88; Kind B class → PROPOSALS SP-6 / ledger S23). The carving *insight itself* lives only in the WORKING dir. It is a methodology nicety, not load-bearing math — re-derivable trivially if ever needed. No re-derivation risk; safe to leave as archaeology.
- **Fresh-9 / Fresh-16 as *sweep tasks*** — the defining segments carry the discipline correctly; a `bin/`-lint for convention/κ specification would be hygiene, not a gem. No content at risk.
- **Themes A–G (wandering-thoughts / phenomenology / naming / audit-methodology)** — the pilot already theme-grouped these and routed them (ledger P-block for methodology per `polish-and-sentiment-ledger.md:78`; naming → FINAL §F8 + S7). Theme A (consciousness-infra connections) and Theme B ("epistemic-architectural rather than mathematical" framing) are genuinely evocative, but they are framing/Brief-authoring material whose *substance* has landed where it matters (Fresh-13's identity-drift formalization being the concrete one). Theme B's "epistemic-architectural" positioning overlaps the existing CLAUDE.md "Math-novelty recognition" + "respectful pedagogy" disciplines. Not new gems.

## Already-routed dispositions checked for wrongness

None found wrong. Every audit-dispositioned-resolved item I re-opened (F1-trail stale xref, F2 status-label, F3 Markov-of-$\Omega$, F4 TF-voice, F7 Tishby) was confirmed still-resolved in current canon, and the Fresh-item "deferred" cells in the pilot's scrutiny table all resolve in the *captured/strengthened* direction. The audit's behavior matches the cycle's central thesis: flagship hints had drifted because the theory moved past them — uniformly toward *stronger* canon, not weaker.

## Minor flag (not a gem; a hygiene note for you)

`03-llm-core/src/disc-m-preservation.md:80,110` references `#der-identity-continuity-threshold`, but **no `der-identity-continuity-threshold.md` exists** in `03-llm-core/src/` (only `der-turnover-information-recursion.md` is present). This reads as a forward-reference to in-flight `spikes/continuity-persistence/` work rather than a stale dangling link — but if the identity-continuity operator is intended as landed canon, the segment is missing; if it is intentionally forward-referenced, a "(forthcoming)" marker would prevent a future auditor re-flagging it. Worth a glance at landing time. (Outside the 471203 slice strictly, but surfaced while verifying Fresh-13.)
