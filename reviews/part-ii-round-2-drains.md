---
kind: review
author:
  name: Claude Fable 5.1 (Part II round-2 drains)
  role: integrator
sources:
  - reviews/part-ii-check-1.md
  - reviews/part-ii-check-1-b1-records.md
  - msc/inside-out-2026-10/part-ii-check-1.md
  - msc/inside-out-2026-10/part-ii-round-2-drains.md
written: 2026-10-31
---

# Part II round 2, drains: the typed record

KR **C.1** (every verified defect replaced, then independently verified), the drains half of **C.2**, and the NOTATION piece of **F.4**, under the top intent "Complete 'in-place' refactor of ASF — meta, all artifacts, and theory itself." This record covers the carriers of statements Part II retired, outside the round-2 integrator's eight segments, as edited in worktree `agent-a6f35eff1ab6cd9c4` on top of `3d17de13` (uncommitted; HEAD moved to `d8248ca2` under me). The account is `msc/inside-out-2026-10/part-ii-round-2-drains.md`. These checks are the reviser's own; the KR asks for an independent verifier after this, and the findings of `review:part-ii-check-1` this lane lands stay open until that verifier marks them answered.

## C1 (check)
- target: segment:impl-common-roots
- act: run
- line: derivation
- criterion: After the edits, a repository-wide grep for every retired form — the product law and ambiguity factor ($\kappa \cdot \mathcal A$, $\mathcal A(e)$, $\mathcal A$-reduction, "ambiguity-gated", "ambiguity-reduction", $C\kappa I$, $C \cdot \kappa$, $\hat{\mathcal A}$, "ambiguity factor"), "forced by information dependency" / "ordering is forced", the identification letters ("(C1) positivity", "(C2) sequential ignorability", "known action-mechanism", "(C1)–(C3)"), the Hafez wording ("perturbation detection", "detection accuracy"), the goal-blind comparator ("clean (goal-blind)", $\Delta M_{\text{bias}}$ outside its two homes), and the operating-law denominator $H(G \mid e_\tau, M_{\tau^-})$ — returns in the live layers only (a) sites inside the round-2 integrator's eight segments, (b) sites held by the Volume 4 lane, (c) correct uses of a different lettered family, or (d) generated outputs that quote (c).
- committed: before
- outcome: confirmed
- recheck: `rg -n` with those patterns over the repository, excluding `.archive/`, `**/.integrated/`, `**/.archived/`, `audits/`, `spikes/`, `reviews/`, `CHANGELOG.md`, `LOG.md`, `ref/`, `releases/`, `.vsect/`, `msc/`, `empirica/`, `*.svg`, `CURRENT-VOL1*`; read each hit in place. Expected residue: `der-directed-separation.md` :273, `der-loop-interventional-access.md` :163, `scope-observation-ambiguity-modulation.md` :26 (integrator); `hyp-substrate-transfer-asymmetry.md` :85, :101, `scope-agent-identity.md` :68, :71, `obs-growth-vs-drift.md` :50, :82 (Volume 4); wrapping's (C1)–(C3) at `der-class-coercion-via-wrapping.md`, `der-class-coercion-in-composition.md` :28, `disc-w1-structural-bound-boundary.md` :59, `der-logogenic-as-wrapping.md`, `def-auxilia-hierarchy.md`, `impl-causal-access.md` :37, :81; `form-composition-closure.md` :282; the NOTATION rows that record "formerly lettered"; `FINDINGS.md` :431 and `README.md` :200 quoting wrapping's Findings.

Run twice, before and after the edits. The before-run is what produced §4 of the account (the κ-denominator carriers, the `03-llm-core/OUTLINE.md` :12 display, `result-coupled-diagnostic-framework` :89/:91, the `$\mathcal A$-reduction` sites in `scope-scaffolded-logogenic` and `impl-primitive-logogenic`, `impl-persistence-and-limits` :94, `disc-independence-audit` :35), none of which the check's F-items listed. The after-run returns exactly the expected residue.

## C2 (check)
- target: segment:result-coupled-diagnostic-framework
- act: rederive
- line: derivation
- criterion: With $A_O(\cdot; \Pi, N_h)$ $L_A$-Lipschitz in the belief under a metric $d$: (i) the error of a diagnostic read off the coupled belief $M^{(\text{post})}$ against its reading off the calibrated belief $\pi$ is at most $L_A \cdot d(M^{(\text{post})}, \pi) = L_A \cdot D_G$ for $\delta_{\text{sat}}$ and $2 L_A \cdot D_G$ for $\delta_{\text{regret}}$; (ii) the displacement of the diagnostic across goal states at fixed inputs is at most $L_A \cdot \lVert\Delta M_{\text{bias}}\rVert$; (iii) the two bounds are about different quantities, with a calibrated goal-dependent allocation having $\lVert\Delta M_{\text{bias}}\rVert \gt 0$ and $D_G = 0$.
- committed: before
- read: segment:result-section-ii-survival, segment:der-directed-separation, segment:scope-observation-ambiguity-modulation
- outcome: confirmed
- recheck: (i) $\lvert A(M) - A(\pi)\rvert \leq L_A d(M, \pi)$ by the Lipschitz property; $\delta_{\text{regret}} = A_O - V_O(\cdot, \pi_{\text{current}})$ and each term contributes $L_A$ (the existing factor of 2, unchanged). (ii) the same inequality between $A(M^{(g)})$ and $A(M^{(g')})$ with $d(M^{(g)}, M^{(g')})$ bounded by the goal-conditional-against-goal-marginal displacement that `#deriv-observation-ambiguity-bias-bound` defines. (iii) the integrator's `#der-directed-separation` clause 3: an update that encodes two features and reports the conditional law given one is calibrated with reliability zero and varies with the goal that chose the feature.

The block formerly bounded the error by $L_A \lVert\Delta M_{\text{bias}}\rVert$ and said "the epistemic bias … is bounded by $O(\kappa \cdot \text{ambiguity})$". The error is the distortion's; the displacement bounds the goal-dependence. The "Consequence" paragraph was a corollary in form and is the fixed-gain hypothesis in content; it is now tagged as that hypothesis's prediction. This check rests on the integrator's uncommitted `#der-directed-separation` (clause 3, (NWI), the probe law) and `#result-section-ii-survival` :114.

## C3 (check)
- target: segment:der-observability-dominance
- act: rederive
- line: derivation
- criterion: An edge into a node with no observed descendant has no likelihood term, so under edge priors independent across edges its posterior is its prior for every observation sequence; under a hierarchical or correlated prior it moves through its coupling to observed edges. Hence "with edge priors independent across edges" narrows the record's population without changing the claim.
- committed: before
- outcome: confirmed
- recheck: write the posterior over edge parameters as prior times likelihood; the likelihood is a function of the parameters of edges with observed descendants only, so it factors out of the marginal over an edge with none iff the prior factors there.

The descriptive record's first falsifier disjunct — beliefs tracking outcomes "no better than chance would predict against the frozen prior" — is what the claim predicts, so it was a confirmation, and it is gone; the real disjunct (beliefs tracking the truth with no channel) stays. The Working Note and the lifted gold now name which regime (frozen vs non-identified) a poorly measured department is in.

## C4 (check)
- target: segment:der-causal-insufficiency-detection
- act: read-check
- line: derivation
- criterion: The off-policy display $\operatorname{sign}(R) = \operatorname{sign}(\rho)$ contradicted the sentence above it ("$+$ for OR-heavy, $-$ for AND-heavy, when $\rho \gt 0$"); the display now carries $s_{\text{type}} \in \{+1, -1\}$ and agrees with the prose and with `#def-strategy-dag` :131 (overestimation at OR roots for a shared enabling cause, underestimation for exclusive alternatives). The criterion's conclusion and the record's falsifier name the two things a significant covariance between siblings with disjoint modelled ancestors can mean: a latent common cause, or a missing edge between the siblings.
- committed: before
- read: segment:def-strategy-dag
- outcome: confirmed
- recheck: compare `:113` prose with `:115` display; compare `:91` with `:215`; for the missing-edge case, two siblings with a direct edge between them and no latent have nonzero covariance and disjoint modelled ancestors, so the old conclusion ("a cause outside the graph") was false of it.

## C5 (check)
- target: segment:impl-causal-access
- act: read-check
- line: imported
- criterion: Every occurrence of "(C1)", "(C2)", "(C3)" or "(C1)–(C3)" remaining in the segment names wrapping's admissibility family of `#der-class-coercion-via-wrapping`, and every former identification-letter site now uses positivity / sequential ignorability / consistency; the five families added to `NOTATION.md` match their home segments' letters and content.
- committed: before
- read: segment:der-class-coercion-via-wrapping, segment:der-multi-timescale-stability, segment:deriv-critical-mass-composition, segment:form-composition-closure, segment:der-turnover-information-recursion, segment:scope-emergence-conditions
- outcome: confirmed
- recheck: `rg -n '\(C[123]\)' 01-aat-core/src/impl-causal-access.md` returns :37 and :81 only, both naming wrapping's; `rg -n '\(C[1-5]\)'` over the five home segments against the NOTATION rows (multi-timescale :47; critical-mass :116–:117; composition-closure :258–:260; turnover :34, :42, :44, :82, :103; emergence :20–:28).

## F1 (finding)
- target: segment:der-directed-separation

Three carriers of retired or (NWI)-conditional statements sit inside the round-2 integrator's segments and were left to that lane, reported mid-run: `:273` Working Note ("the cascade's ordering ($M_t$ first, then $G_t$) is forced by the information dependency" — the true half; "and objective revision last is a recommendation" completes it); `#der-loop-interventional-access` :163 (a struck-through resolved item carrying "(C1) positivity / (C2) sequential-ignorability / (C3) known-action-mechanism" — history, deletable under I.5); `#scope-observation-ambiguity-modulation` :26 ("which is what a goal-blind update reports" — under (NWI) only, as `#result-section-ii-survival` :114 says).

## F2 (finding)
- target: segment:hyp-substrate-transfer-asymmetry

Volume 4 carriers left to that lane: `:85` and `:101` (per-substrate $(\kappa, \mathcal A)$ profiles; "asymmetric $\kappa \cdot \mathcal A$"), `#scope-agent-identity` :68, :71 (the identification triple by its old letters), `#obs-growth-vs-drift` :50, :82 ("perturbation detection"; the integrator's open F3 from round 1). The first round left `hyp-substrate-transfer-asymmetry` with a vsect finding; nothing has landed there since.

## F3 (finding)
- target: segment:der-observability-dominance

`vsect revise` on this segment, on `#der-causal-insufficiency-detection` and on `#def-strategy-dag` took in two edits each as one revision under this lane's name: `8f7dd870`'s B.1 corrections, never classified by their reviser (the Part II check's F12), and this lane's residue edits. The classification "reworded" is this lane's claim about both. The lapsed checks `review:part-ii-check-1-b1-records#C6` and `#C8` rest on the pre-`8f7dd870` versions and wait for a second mind's `vsect confirm`; the four first-check findings on these segments (`review:b1-part-ii-check-1#C14/finding`, `#C13/finding`, `#C10/finding`, `#F4`) are marked answered by the second checker's confirmed C6, C8, C9.

## F4 (finding)
- target: segment:result-coupled-diagnostic-framework

Two open ledger items concern sentences edited here and should be read against the new text. `item:t1-coupled-diagnostic-class1-rescope` (Class 1 → causally-disciplined at :18, :26, :55, :66) is done in this edit and closes with the commit that lands it. `item:the-scaffolding-overclaim-in-volume-3-its-origin` part (1) — `#scope-scaffolded-logogenic` :30 and `#impl-scaffolded-logogenic` :28 claiming scaffolding recovers "Part II's persistence guarantees" — is replaced by the W₁ goal-blind-step-1 form with the 16-of-24 survival stated; parts (2) and (3) are untouched and the item stays open. `item:in-context-self-reflection-no-go`'s opening text reads the bound as "$L_A$ times its epistemic bias"; the bound is now $L_A$ times the distortion, and the item's reading ("you cannot prompt your way out") survives with that substitution.

## F5 (finding)
- target: segment:impl-orient-cascade

The approximate-survival overclaim F10 named in `01-aat-core/OUTLINE.md` :80 ("the bias bound … is now a conditional theorem") stood one hop downstream at `:64`, `:66` and `:70` of this segment, and the regression guard at `:75` treated $\mathcal A$ as live. All four are drained; the checker should read the chapter-close paragraphs (:64–:70) whole, since they were written as one voice and I changed three sentences in it.

## What I did not check

I did not fetch the arXiv abstract for Hafez et al.; the figures I wrote at two sites copy `#der-causal-hierarchy-requirement` :63, which the Part II checker verified against the abstract. I did not open Savage 1971, Gneiting & Raftery 2007 or Perdomo et al. 2020; the Working Note that names them says so. I did not re-read the `msc/` drain's dispositions of `msc/summary-attempt/` and the other `msc/` residue that carries old wording. I did not run `bin/refresh-all --check` (the integrator's `FINDINGS.md` regeneration was in flight in the same worktree). The two reworded chapter-end segments (`impl-orient-cascade`, `impl-common-roots`) were not read back whole by a second mind.
