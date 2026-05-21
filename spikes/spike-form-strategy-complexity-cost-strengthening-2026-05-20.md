---
purpose: Strengthening attempt — `form-strategy-complexity-cost` `discussion-grade` → `robust-qualitative`
date: 2026-05-20
agent: Opus 4.7 (1M)
target_segment: 01-aat-core/src/form-strategy-complexity-cost.md
completion_state: A (Strengthened to the claim)
parent_cycle: 451729 D.1 Gate Verification, Phase 4b
---

# Spike: `form-strategy-complexity-cost` discussion-grade → robust-qualitative

*Research spike. Not canon. Math derived here that warrants segment land-in is identified in §4; this spike itself proposes only a frontmatter+Epistemic Status edit — the segment's body already carries the strengthened content.*

## §1 — Context

### The audit observation

The 451729 D.1 Gate verification ([`msc/451729-d1-gate-verification-2026-05-20.md`](../msc/451729-d1-gate-verification-2026-05-20.md) §5) noted that `form-strategy-complexity-cost` carries `status: discussion-grade` while the segment's own "Max attainable" line in its Epistemic Status announces:

> *robust-qualitative for the IB objective with the direction-forced derivation; conditional for the specific functional form (linear vs. square-root in KL).*

The Gate verification agent's read: *"a reasonable interpretation: the segment could potentially promote to `robust-qualitative` once the dependency chain stabilizes — its current `discussion-grade` is conservative."*

This spike runs the **strengthen-first protocol** on that observation: attempt the upgrade, demonstrate it is honest, identify any structural obstruction, route to a clean canon disposition (or surface a no-go).

### Substrate evidence pointing at strengthening

Three pieces of substrate make the upgrade hypothesis credible *before* the math is checked:

1. **The appendix is already at `robust-qualitative`.** [`deriv-strategy-cost-regret-bound`](../01-aat-core/src/deriv-strategy-cost-regret-bound.md) carries the load-bearing derivations (the BH identity §4, the matched lower bound, the direction-forcing derivation §5, the chain-rule uniqueness §6.1, the Fenchel-Bregman identification §6.3) and is labeled `status: robust-qualitative` with exact-tier sub-claims explicitly enumerated in its "Max attainable" line. A formulation segment that depends on an appendix should not, in general, sit a full two tiers below the appendix.
2. **The KL-direction derivation has landed.** Commits `e777f01` and `f70fb68` (2026-04-22) landed the Pinsker / Csiszár / Aczél-Daróczy citations and the chain-rule axiom motivation. Commit `1bffa60` propagated the Bretagnolle-Huber identity (AF-11/AF-12). The "Regret-bound derivation of KL direction" paragraph in the segment is no longer hand-wavy — it now compactly recapitulates the appendix derivation with a forward pointer.
3. **Comparable formulation segments sit at `robust-qualitative`.** [`form-agent-model`](../01-aat-core/src/form-agent-model.md), [`form-event-driven-dynamics`](../01-aat-core/src/form-event-driven-dynamics.md), [`form-complete-agent-state`](../01-aat-core/src/form-complete-agent-state.md), [`form-consolidation-dynamics`](../01-aat-core/src/form-consolidation-dynamics.md), [`form-structural-change-as-parametric-limit`](../01-aat-core/src/form-structural-change-as-parametric-limit.md) are all `formulation` + `robust-qualitative`. [`form-information-bottleneck`](../01-aat-core/src/form-information-bottleneck.md) hits `exact` only because it is a verbatim recapitulation of an external theorem. The strategy-complexity-cost segment is the only formulation-type segment in this neighbourhood at `discussion-grade`.

### The frame of this spike

This is **not** a math-derivation spike — the math is in [`deriv-strategy-cost-regret-bound`](../01-aat-core/src/deriv-strategy-cost-regret-bound.md). This is a **tier-honesty audit**: does the current segment body, taken as a whole, honestly carry `robust-qualitative` under FORMAT.md's tier definition? The question is whether `discussion-grade` is **conservative** (a soft-cautioning artifact of the segment's pre-regret-bound state, never updated when the body advanced) or **correct-as-stated** (some specific claim in the segment is genuinely qualitative-by-analogy and not survivable across assumptions).

Strengthen-first applies in its sharper form here: if the segment-body math is in fact robust-qualitative and the tier label is conservative, leaving it at `discussion-grade` is *itself* a soft-counsel-against-ambition failure — it under-states the canon's honest position.

---

## §2 — Attempt: claim-by-claim tier audit of `form-strategy-complexity-cost`'s Formal Expression

The Formal Expression has six titled blocks; tier-audit each one against FORMAT.md's definitions. The robust-qualitative bar (FORMAT.md `## Epistemic Triage`): *"the qualitative claim survives across modeling choices, though a specific functional form is approximate."* The discussion-grade bar: *"argued qualitatively or by analogy — not formally derived, not empirically validated."*

### §2.1 — Strategy description length (MDL form)

**Segment label:** "Formulation (strategy-description-length)" — equation-tag.

The Formal Expression states $\operatorname{DL}(\Sigma_t) = \operatorname{DL}_{\text{struct}}(G) + \operatorname{DL}_{\text{param}}(p \mid G)$ with two-source decomposition. The Epistemic Status says explicitly *"The description length formulation is a *formulation* — it applies standard MDL to the strategy DAG, which is a representational choice not a derived necessity."*

**Tier audit.** MDL applied to a DAG is textbook (Rissanen 1978; Grünwald 2007). The scaling claim $\operatorname{DL}(\Sigma_t) = O(|E|\log|V|)$ is a counting argument that survives the choice of code (universal codes differ by $O(\log\log)$ corrections, which are robust-qualitative). The Beta-Bernoulli $O(\log n_{ij})$-bits-per-edge claim is exact under that distributional assumption.

**Verdict on this block:** robust-qualitative cleanly. The qualitative scaling is the load-bearing claim; the constants and the universal-code choice are the approximate-form aspects.

### §2.2 — Strategy IB objective (theoretical variational form)

**Segment label:** "Formulation (strategy-IB-objective; KL-direction strengthened by regret bound — see Epistemic Status)" — equation-tag.

Three sub-claims live here:

1. **The variational form** $\Sigma_t^\ast = \arg\min[I(\mathcal C_t;\Sigma_t) + \beta_\Sigma \cdot D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})]$. Tier-audit: this is a *form*, not a derivation. It is a Lagrangian-relaxation analog of the information-theoretic-MDP objective (Tishby-Polani 2011, Rubin-Shamir-Tishby 2012, Levine 2018). Qualitatively (an information cost plus a decision-relevance cost in trade-off), it survives across assumptions. The exact Lagrangian shape (linear-in-KL) is one of two acknowledged options (the appendix's §7 trade-off). **Robust-qualitative.**

2. **The KL direction** ($\pi^\ast$-first). Tier-audit: derived as a no-go-for-forward-KL argument in [`deriv-strategy-cost-regret-bound`](../01-aat-core/src/deriv-strategy-cost-regret-bound.md) §5. Forward-KL is identically $+\infty$ under deterministic $\pi^\ast$ whenever $Q_{\Sigma_t}$ has off-optimum mass — direct calculation, exact-tier. The direction-forcing argument is *strictly stronger* than robust-qualitative on this sub-claim; the segment Epistemic Status correctly notes this.

3. **Reverse-KL uniqueness within the direction-forced family** via chain-rule additivity. Tier-audit: appendix §6.1 derives this via Hobson 1969 / Csiszár 1991 / Aczél-Daróczy 1975 Cauchy-FE machinery. Labeled `derived (conditional on chain-rule additivity axiom)`. The axiom is AAT-internally motivated as the divergence-level analog of [`der-chain-confidence-decay`](../01-aat-core/src/der-chain-confidence-decay.md) (mathematical identity, `exact`). The uniqueness is `conditional`-tier under FORMAT.md's definition (derived under an explicit local axiom not in the global `depends:` chain). The chain-rule additivity axiom is not vacuous — it is structurally motivated by an AAT commitment already at `exact` — but it is an axiom.

**Verdict on this block:** the variational form is robust-qualitative; the direction-forcing is exact; the reverse-KL uniqueness is conditional. The block as a whole sits at robust-qualitative-or-stronger.

### §2.3 — Regret-bound derivation paragraph

This block recapitulates the appendix's §4 BH identity and §3 TV bound, both proved-exact under deterministic $\pi^\ast$ + bounded value. The "asymmetry forced by regret's one-sidedness" argument (appendix §5) is exact and *independent of the chain-rule axiom* — a structural-not-axiomatic forcing.

**Verdict on this block:** the underlying claims are exact-tier under their named scope (bounded value, deterministic $\pi^\ast$). The segment's recapitulation is at-or-stronger than robust-qualitative.

### §2.4 — Operational form (DL surrogate + sample-based KL)

The operational replacement of $I(\mathcal C_t;\Sigma_t)$ by $\operatorname{DL}(\Sigma_t)$ and of the population KL by a sample estimate is *necessary because the population objective is not closed-form-computable*. This is a robust-qualitative operational claim: the qualitative structure (an MDL surrogate + a sample-based fidelity estimator) survives across operationalization choices; the specific estimator is one of many valid choices.

**Verdict:** robust-qualitative cleanly.

### §2.5 — Maximum useful chain depth $d^\ast$

**Segment label:** "Derived (Conditional on Beta-Bernoulli, per-edge persistence)" — equation-tag.

The derivation: from [`def-strategic-tempo`](../01-aat-core/src/def-strategic-tempo.md)'s per-edge persistence condition, an AND-chain of depth $d$ with parameters $(\nu, \theta, n, \rho_\Sigma, R_\Sigma)$ persists only when $\nu \cdot \theta^{d-1}/(n+1) \gt \rho_\Sigma/R_\Sigma$, solving for $d^\ast$ via the logarithmic inversion. The conditional structure is clean — Beta-Bernoulli per-edge, per-edge persistence already established upstream.

**Tier audit.** Under those named conditions, the formula is *exact* algebra. The qualitative claim (a finite depth limit exists; deeper chains accumulate uncorrectable mismatch) is robust across edge models. The specific functional form ($d^\ast = 1 + \lfloor \log(\cdot)/\log(1/\theta) \rfloor$) is exact under Beta-Bernoulli, with the logarithmic shape robust qualitatively across exponential-family edges.

**Verdict on this block:** `Derived (Conditional on ...)` is already accurate at the block level; the qualitative existence-of-depth-limit claim is robust-qualitative. This block honestly carries content stronger than the segment-wide `discussion-grade` label.

### §2.6 — Triple depth penalty (observation)

This is explicitly labeled an *observation* combining results from three independent segments. The compounding is multiplicative-in-depth, with each penalty independently established. The qualitative claim (deep AND-chains are exponentially expensive along three dimensions) is robust-qualitative; the literal product is exact under the conjunction of the three derivations' scope conditions.

**Verdict on this block:** robust-qualitative cleanly.

### §2.7 — Enriched explicit strategy condition (maintenance-cost decomposition)

The decomposition $C_{\text{maintain}} = C_{\text{represent}} + C_{\text{revise}} + C_{\text{monitor}}$ with each component mapped to a quantity defined elsewhere. This is a formulation — a partition of the maintenance-cost concept into named-elsewhere components. Qualitatively, the three-component decomposition survives across operational instantiations; the specific proportionality constants are abstract.

**Verdict on this block:** robust-qualitative — *unless* the proportionality claims ("$C_{\text{represent}} \propto \operatorname{DL}(\Sigma_t)$" etc.) are read strictly, in which case they become formulation-grade selections of how to operationalize each cost component. Either reading is at-or-stronger than `discussion-grade`.

### §2.8 — Complexity compression operations

**Segment label:** "Discussion (complexity-compression)" — equation-tag.

This block uses the IB objective to motivate three compression operations (edge pruning, node merging, depth truncation). It is labeled `Discussion` inline — the operations-as-suggestions reading is naturally discussion-grade. **This is the one block in the Formal Expression that genuinely sits at discussion-grade.**

**Verdict on this block:** discussion-grade by its own equation-tag and content. But this block is one of seven; the segment-wide tier label should reflect the **load-bearing** content, not the weakest sub-block.

### §2.9 — Block-level summary table

| Block | Block-level tier (honest) | Equation-tag label |
|---|---|---|
| Description length (MDL) | robust-qualitative | Formulation |
| Variational IB objective | robust-qualitative (direction is exact) | Formulation (KL-direction strengthened) |
| Regret-bound derivation paragraph | exact / robust-qualitative | (recap of appendix) |
| Operational form | robust-qualitative | (no eq-tag) |
| $d^\ast$ depth bound | conditional / robust-qualitative | Derived (Conditional on Beta-Bernoulli) |
| Triple depth penalty (observation) | robust-qualitative | (no eq-tag) |
| Enriched maintenance decomposition | robust-qualitative | Formulation |
| Compression operations | discussion-grade | Discussion |

Six of eight blocks honestly carry robust-qualitative-or-stronger. One block (§2.5 $d^\ast$) is sharper still — conditional with exact arithmetic under its named conditions. One block (§2.8 compression operations) is genuinely discussion-grade, and is the only block whose equation-level tag agrees with the segment-wide tier label.

---

## §3 — Outcome: (A) Strengthened to the claim

**The current `status: discussion-grade` is conservative.** The segment's load-bearing content honestly carries `robust-qualitative`:

- **The IB-objective variational form** survives across modeling assumptions (the linear-vs-square-root Lagrangian-shape choice is the residual-approximate functional-form aspect that robust-qualitative correctly captures per FORMAT.md).
- **The KL direction is forced, not posited** — direct exact-tier vacuity argument for forward-KL (appendix §5), plus an independent asymmetry-forcing argument from regret's one-sidedness (also appendix §5) that does not depend on the chain-rule axiom.
- **The depth bound $d^\ast$ qualitative structure** (deeper AND-chains hit an evidence-starvation ceiling, the ceiling depends logarithmically on $\theta$ and inverse-linearly on $\rho_\Sigma/R_\Sigma$) survives across edge models; the specific Beta-Bernoulli closed form is the conditional sharpening.
- **The maintenance-cost decomposition** with three named components survives across operational instantiations.
- **The compression operations** are honestly discussion-grade and equation-tag-labeled as such inline, which is the appropriate FORMAT.md handling of a single block that sits below the segment's overall tier (per FORMAT.md *Findings* §"Tier comes from frontmatter, not Findings" — the *frontmatter* status should reflect the segment's load-bearing tier; equation-tag labels handle sub-block calibration).

**Asymmetric direction-forcing is the load-bearing strengthening result.** The 2026-04-22 cycle (commits `e777f01` / `f70fb68`) and the 2026-04-24 BH-identity landing (the §4 promotion in the appendix to *exact identity under deterministic $\pi^\ast$*) collectively moved the segment from "uses reverse-KL because that's what the IB literature does" to "uses reverse-KL because forward-KL is identically $+\infty$ under canonical scope, asymmetry is forced by regret's one-sidedness, *and* reverse-KL is uniquely chain-rule-additive within the direction-forced family." The `discussion-grade` label predates this arc; it was never updated.

**Is `conditional` available instead?** Considered. `conditional` (per FORMAT.md) means "depends on explicitly named local assumptions" with derivation-strength `exact` under those conditions. The reverse-KL uniqueness sub-claim alone is at this tier (chain-rule additivity axiom). But the *segment* carries multiple claims at varying tiers; the segment-wide label tracks the load-bearing content. Conditional is appropriate at the sub-claim level (the appendix's equation-tag labels handle this); it is *too narrow* as the segment-wide label because much of the segment (MDL, qualitative depth bound, decomposition) is robust-qualitative rather than `exact-under-named-conditions`. **`robust-qualitative` is the correct segment-wide tier.**

**Comparative ceiling.** The Max-attainable line already says *"robust-qualitative for the IB objective with the direction-forced derivation; conditional for the specific functional form."* The line was true when the appendix was at robust-qualitative; the segment can now honor its own ceiling.

---

## §4 — Recommended canon disposition

### §4.1 — Frontmatter edit (the load-bearing change)

```diff
 ---
 slug: form-strategy-complexity-cost
 type: formulation
-status: discussion-grade
+status: robust-qualitative
 depends:
   - def-strategic-tempo
   - form-information-bottleneck
   - norm-explicit-strategy-condition
   - der-chain-confidence-decay
   - form-structural-change-as-parametric-limit
   - def-value-object
   - form-objective-functional
 stage: draft
 ---
```

Also missing from the `depends:` list: [`deriv-strategy-cost-regret-bound`](../01-aat-core/src/deriv-strategy-cost-regret-bound.md), which the segment cross-references inline ("see #deriv-strategy-cost-regret-bound §6.1") and on which the strengthened KL-direction claim depends. The appendix is itself an appendix to *this* segment (its body says "this appendix derives that..."), so the dependency direction is `form-strategy-complexity-cost` → `deriv-strategy-cost-regret-bound`. **Recommend adding `deriv-strategy-cost-regret-bound` to `depends:`** so the dependency DAG reflects the segment's actual reasoning chain.

```diff
 depends:
   - def-strategic-tempo
   - form-information-bottleneck
   - norm-explicit-strategy-condition
   - der-chain-confidence-decay
   - form-structural-change-as-parametric-limit
   - def-value-object
   - form-objective-functional
+  - deriv-strategy-cost-regret-bound
```

### §4.2 — Epistemic Status clarifying edits (optional but recommended)

The current Epistemic Status paragraph is already substantively honest under `robust-qualitative` — the "Max attainable: *robust-qualitative* for the IB objective with the direction-forced derivation" line will be read more naturally with the frontmatter at `robust-qualitative` (the gap between current status and ceiling closes).

Suggested clarifying edits (not strictly required for the tier promotion; recommended for **internal consistency**):

- The current Epistemic Status ends with: *"The DL formulation is standard; the depth bound could reach exact status for specific edge models."* This is still honest under `robust-qualitative`; consider sharpening to: *"The depth bound is currently `Derived (Conditional on Beta-Bernoulli, per-edge persistence)` and reaches exact under those named conditions; the qualitative existence-of-ceiling claim is robust-qualitative."*

- The "compression operations are *discussion-grade*" sentence remains accurate at the **sub-block** level (equation-tag `*[Discussion]*` already carries this) and should be preserved verbatim; the segment-wide tier in the frontmatter is independent of any single sub-block.

- Consider adding a one-line ceiling-acknowledgment at the very end of the Epistemic Status, in the style other segments use: *"The segment's tier reflects the load-bearing IB-objective + direction-forced + depth-bound + decomposition content; the compression-operations block (§2.8 in the audit) remains `*[Discussion]*` at equation-tag level."* This would close any "but block X is discussion-grade" objection a future reader might raise.

### §4.3 — Findings section (optional cycle move, **not required for tier promotion**)

The segment has *no* `## Findings` section. Several of its load-bearing claims (the direction-forced reverse-KL via the regret-bound argument; the depth-bound $d^\ast$ with its three-penalty compounding; the maintenance-cost decomposition operationalizing #norm-explicit-strategy-condition) would qualify for FINDINGS catalog entries per FORMAT.md §Findings — *"a result, a recognition, a partition, a synthesis."* 

However: the appendix [`deriv-strategy-cost-regret-bound`](../01-aat-core/src/deriv-strategy-cost-regret-bound.md) is the natural home for the regret-bound and chain-rule-uniqueness Findings (it's where the derivations actually live), and a Findings section there is not yet present either. The depth-bound and decomposition are more clearly this segment's. **Recommend deferring Findings authoring to a separate cycle** — it is independently valuable content authoring, not a precondition for the tier change. Adding a Findings section here is not necessary to honestly carry `robust-qualitative`.

### §4.4 — Stage

`stage: draft` is appropriate. The segment has not been through Gate 1–4 promotion. The tier-change is independent of the stage advancement and does not bypass the gate process.

---

## §5 — Honest scope statement

### What this spike verified

1. **Read in full:** the target segment, the upstream IB segment, the upstream chain-confidence-decay segment, the regret-bound appendix, the meta-pattern segment, and FORMAT.md tier definitions. Verified the regret-bound derivation chain (Pinsker as loose general form, BH-identity as tight under deterministic $\pi^\ast$, chain-rule axiom motivation) is honestly carried in the appendix at `robust-qualitative` with exact-tier sub-claims enumerated.
2. **Tier-audited block-by-block** the segment's Formal Expression against FORMAT.md's `robust-qualitative` and `discussion-grade` definitions, with explicit verdicts and the comparative table at §2.9.
3. **Cross-checked sibling formulation segments** (form-agent-model, form-event-driven-dynamics, form-complete-agent-state, etc.) — all at robust-qualitative; the target segment is the lone discussion-grade formulation in the neighborhood.
4. **Identified the dependency-list gap**: `deriv-strategy-cost-regret-bound` should be in `depends:` since the appendix is referenced inline and the strengthened KL-direction derivation depends on it.

### What this spike did *not* re-derive

- **The chain-rule additivity uniqueness theorem (Hobson 1969 / Csiszár 1991).** Re-verified the citations are present in the appendix; did not re-execute the Cauchy-FE derivation. The appendix carries Aczél & Daróczy 1975 §4 as the standard reference for the functional-equation derivation. Strict-form independent re-derivation deferred (see §5 next step).
- **The Bretagnolle-Huber identity.** Re-verified the appendix's direct calculation in §4 ($D_{\mathrm{KL}}(\delta_{a^\ast} \Vert Q) = -\log Q(a^\ast)$ for deterministic point-mass) — this is elementary and checks out. Did not independently re-derive the general BH inequality.
- **Pinsker's inequality.** Standard textbook (Tsybakov 2009 §2.4; Cover & Thomas 2006 §11.6); not re-derived.
- **The depth-bound algebra under Beta-Bernoulli.** The derivation $\nu \cdot \theta^{d-1}/(n+1) \gt \rho_\Sigma/R_\Sigma \Rightarrow d^\ast = 1 + \lfloor\log(\cdot)/\log(1/\theta)\rfloor$ is straightforward log-inversion. Inspected; not formally re-checked under independent assumptions.

### Strict-form independent-verify next step

If the parent agent wants strict-form verification before landing the tier change, the natural escalation is:

1. **PDF spot-check** of the Hobson 1969 / Csiszár 1991 chain-rule axiomatic-uniqueness claim against the published statements (the citation correction in the appendix's Working Notes — *"Csiszár 1972, Amari 2009 Theorem 1, and Amari & Cichocki 2010 Prop 3.2 do not contain the chain-rule uniqueness theorem; the correct attributions are above"* — explicitly flags that prior drafts mis-cited; the *correct* citations should be PDF-verified once if not already).
2. **Independent verification of the BH-identity-under-deterministic-$\pi^\ast$ algebra** (this is a one-line calculation; cheap to re-execute).

Neither is required to land the tier promotion — the appendix is already at `robust-qualitative` and the present segment's body recapitulates its conclusions accurately. But both are appropriate before claiming the segment cleared a Gate 2 pass at the new tier.

### Strengthen-first posture honored

The strengthen-first reflex applies sharply here: the segment's tier label was conservative (under-stating the canon's honest position), the **strengthen** move (raise the label to the load-bearing tier) is the correct discharge direction, and the soften alternative (leave at discussion-grade because "the segment is mostly discussion content") would require ignoring (i) the regret-bound derivation that has *already landed*, (ii) the exact BH identity, (iii) the chain-rule uniqueness theorem, and (iv) the qualitative depth-bound. None of those is discussion-grade; treating the segment as if they were not present would be the failure mode.

### No no-go encountered

This is an (A) outcome — strengthened-to-the-claim. No no-go was uncovered: the body's load-bearing content honestly carries `robust-qualitative` per FORMAT.md's tier definitions. The strengthening here is **label-to-body realignment**, not new mathematics — the body was already strengthened in prior cycles; the frontmatter never caught up.

### Frame defects noted

One frame defect in the brief worth surfacing: the brief asked whether `robust-qualitative` is the right next tier *or whether something stronger (`conditional`?) is available.* Answered above (§3): `conditional` is too narrow as the segment-wide tier because most blocks are tier-broader than that single-condition reading. The sub-claim that is conditional (chain-rule uniqueness) is already labeled so via the appendix's equation-tag; segment-wide `robust-qualitative` is the right level. `exact` is unavailable because the segment is a *formulation*-type and most of the content has acknowledged-approximate functional form (the linear-vs-square-root Lagrangian-shape choice, the MDL coding-scheme choice, the maintenance-cost proportionality constants).

---

## §6 — Summary for parent

- **Completion state:** (A) — Strengthened to the claim.
- **Load-bearing result:** the segment's tier label `discussion-grade` is conservative; the segment-body's load-bearing content honestly carries `robust-qualitative` per FORMAT.md's tier definitions. The strengthening that warrants the upgrade has *already landed* in the body (regret-bound derivation, BH identity, chain-rule uniqueness, depth-bound algebra, decomposition); only the frontmatter label was never updated.
- **Recommended canon edit:** frontmatter `status: discussion-grade` → `status: robust-qualitative`; add `deriv-strategy-cost-regret-bound` to `depends:`. Two minor Epistemic Status clarifying edits are optional (§4.2). No segment-body math changes required.
- **Strict-form next step (independent-verify):** PDF spot-check of Hobson 1969 / Csiszár 1991 citations (the appendix's own Working Notes flag a prior mis-citation that was corrected; one more cycle of verification is appropriate); independent re-verification of the BH-identity one-line algebra (cheap).
- **Honest scope deferrals:** none of the math was re-derived here; the spike's role was tier-honesty audit against existing-derived content. The body math has been derived in `deriv-strategy-cost-regret-bound` and prior cycles; this spike confirms the tier label has fallen behind.

*This spike file is the record. The parent commits the canon change after spot-check.*
