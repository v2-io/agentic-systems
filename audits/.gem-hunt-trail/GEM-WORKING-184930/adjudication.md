# Gem-hunt adjudication — audit-findings-184930

*Adjudicator: Claude Opus 4.8 (1M). Date: 2026-05-29. Report-only; no canon edits, no file moves, no commits.*

## TL;DR

**This audit carries no un-captured content. Its full substance is already in canon, verified first-hand.** This is the honest, fully-successful "already in canon, here are the loci" result, not a failure to find gems.

184930 is a **stub-cycle audit**: the auditor wrote only the protocol-mandated §1–§3 *initial predictions* (six themes, seven sub-predictions) from README + OUTLINE + reference definitions, then the cycle ended **before any segment walk** — no per-segment trail, no §14 wandering thoughts, no FINAL. The predictions are *pre-segment-walk anticipations*, not findings against read material. The extraction agent (Opus 4.7) already mapped all seven to canon and confirmed 4 stronger-than-predicted, leaving 2 "deferred" pending multi-segment reads. I performed those reads first-hand. Both deferrals close as *already-in-canon*; one (P2-comp) closes as canon being **richer than the prediction**, partially disconfirming the prediction's framing.

Per the brief's caution: I checked the dispositioned-away items (the "subsumed"/"confirmed-stronger" verdicts are themselves drifted proxies) and the two deferrals specifically. Nothing surfaced that we'd have to re-derive or re-create. There is no (A) ready-to-land and no (B) research-seed gem in this slice. The value this audit retains is calibration-signal (external legibility evidence), not theory content — and that value is already correctly characterized in the extraction file itself.

---

## (A) Ready-to-land gems

**None.** No content in this audit exists outside canon.

## (B) Research-seed gems

**None.** No prediction names a direction that canon has not already taken further than the prediction anticipated.

---

## Per-prediction adjudication (first-hand loci)

The seven predictions and their disposition. Loci are segments I opened on this pass (P2-ib Part B, P2-comp) or that the extraction confirmed and I spot-checked.

### P1-forced — persistence condition as Lyapunov necessity
**Already in canon, stronger than predicted.** Prediction anticipated linear-Lyapunov derivation of $\alpha \gt \rho/R$. Canon delivers nonlinear-Lyapunov-via-**sector-condition**, strictly more general, with linear as a recovery case.
**Locus:** `01-aat-core/src/deriv-sector-condition.md`; `result-sector-condition-stability`; `result-persistence-condition`. Not a gem (the strengthening already happened and is landed).

### P1-chosen — strategy DAG as formulation choice (AND/OR single-parameter edges)
**Already in canon, with the chosen/forced seam located one level deeper than the prediction.** Canon: graph-structure-with-Markov-factorization is *derived* (sufficiency) at `deriv-graph-structure-uniqueness`; the AND/OR single-parameter *parameterization within* that structure is the chosen formulation.
**Locus:** `01-aat-core/src/def-strategy-dag.md`; `deriv-graph-structure-uniqueness`. Not a gem.

### P2-ds — directed-separation boundary fuzziness; §II results smuggling Class 2 coupling
**Already in canon, resolved constructively.** The exact "smuggling Class 2 under Class 1 guise" failure mode is what the wrapping construction is engineered to prevent: the wrapper *structurally commits* to goal-blind belief-update queries; residual leakage is bounded structurally (W₁) or behaviorally (W₂) and named, not hidden. (Note GUC renumbering 2026-05-09: auditor's "Class 2 = LLMs" = current GUC Class 3 Coupled.)
**Locus:** `der-directed-separation.md`; `der-class-coercion-via-wrapping`; `der-logogenic-as-wrapping`; CLAUDE.md "Known Fragilities." Not a gem.

### P2-ib — IB stretched beyond epistemic state; deliberation-cost conflating processing-time with wall-clock
**Part A (IB stretched): already in canon, resolved.** The non-standard IB application (action-conditional Fisher Information Matrix as "matrix CIY") is explicit and honest about the move: the segment names the **"blank wall attack"** the scalar bound admits and lifts to an LMI on the FIM with a PSD matrix Lagrange multiplier $\Lambda$, so complementary slackness *mathematically zeros out the bonus for blank-wall actions*. The "stretch" the auditor anticipated is exactly what the segment addresses, with the residual CIY-vs-EIG (FIM = EIG-rate only under Gaussian-linear) concern openly retained.
**Locus (read first-hand):** `01-aat-core/src/deriv-causal-ib-lmi.md` (intro + Definitions matrix-ciy, lmi-survival); chain `form-information-bottleneck` → `deriv-causal-ib-exploration` → `deriv-causal-ib-lmi`.

**Part B (deliberation-cost wall-clock conflation): NO conflation present — concern is closed, not actionable.** This was the extraction's one flagged "possible actionable-open." Read first-hand: `der-deliberation-cost.md` keeps wall-clock-drift cost and information/resource cost as **separate additive terms**. The threshold is $\Delta\eta^\ast(\Delta\tau)\,\Vert\delta_{\text{post}}\Vert \gt \rho_{\text{delib}}\,\Delta\tau$, where $\rho_{\text{delib}}\,\Delta\tau$ is *mismatch drift during the pause window* (wall-clock), and computational/energetic cost enters as a **distinct** additive term $C(\Delta\tau)$ ("Resource costs beyond time" paragraph: $\ldots \gt \rho_{\text{delib}}\Delta\tau + C(\Delta\tau)$). The "Connection to temporal nesting" paragraph separately tracks internal-loop rate $\nu_{\text{internal}}$ vs external $\nu_{\text{external}}$. There is no place where information-theoretic processing is conflated with wall-clock; they are deliberately decomposed.
**Locus (read first-hand):** `01-aat-core/src/der-deliberation-cost.md` (Formal Expression; "Resource costs beyond time"; "Connection to temporal nesting"). Not a gem.

### P2-comp — composition results rely on symmetric/cooperative assumptions
**Already in canon, and the prediction's specific framing is partially DISCONFIRMED by canon being richer.** The auditor predicted composition "relies on heavily constrained symmetric or cooperative assumptions." Canon carries a **signed-$\gamma$ unification of cooperative AND adversarial coupling under a single persistence inequality**: cooperative coupling enters effective disturbance with a *negative* sign, adversarial with a *positive* sign, and `deriv-critical-mass-composition` derives (not merely bounds) the composite sector constant $\alpha_c$ for the symmetric-matched-Tier-1 dyad with the *sign of $\gamma$ entering explicitly*, recovering `der-team-persistence` (cooperative) and `der-adversarial-destabilization` (adversarial) as signed special cases, plus a weighted-Lyapunov asymmetric limit formalizing `hyp-symbiogenic-composition`'s autonomy reduction.
- *Layer 1 of the prediction (results rely on constrained assumptions)* is correct at a trivial level — canon openly names composition-transition-dynamics as an open gap and scopes the closed-form to matched-symmetric-Tier-1. That honest scoping is the CS-norm "precise scope" virtue, not timidity, and is already landed.
- *Layer 2 (constraint is specifically symmetric/cooperative)* is miscalibrated: the adversarial leg is first-class, not absent.
**Locus (read first-hand):** `der-team-persistence.md` (cooperative-adversarial disturbance decomposition, signed structure); `deriv-critical-mass-composition.md` (signed-$\gamma$ critical-mass inequality (CM2), four-limit reduction table, asymmetric-limit symbiogenesis sketch); also present: `der-adversarial-destabilization.md`, `der-agent-opacity.md`, `cooperative-adversarial-intro.md`, `impl-cooperative-adversarial.md`. Not a gem; if anything, canon is the stronger artifact.

### P3-tst — git-as-do(a) oversimplifies latent states
**Already in canon, named verbatim.** The C3 confounder ("developer knowledge state" / private causal model as selection effect) is the prediction stated; C1/C2 cover the "off-band communication" half; the causal-discovery claim is honestly demoted derived→discussion-grade with "Max attainable: *empirical*" cap for exactly this reason.
**Locus:** `02-tst-core/src/hyp-causal-discovery-from-git.md`. Not a gem.

### P4-overall — epistemic-tier discipline real; mismatch-ODE→strategy-DAG bridge is the scrutiny site
**Already in canon / corroborated.** Tier discipline confirmed by the segment-level Epistemic Status reads above (P1, P2-ib, P3). The bridging-seam location matches the framework's own load-bearing pivots (sector-bridge, `der-directed-separation`, `def-strategy-dag`) and the `disc-*` meta-segment placement. Not a gem.

---

## Genuinely valueless / fully-superseded

Nothing here is *valueless* in the sense of error — but as **theory content** the entire predictions register is fully covered by existing canon (superseding loci listed per-prediction above). Specifically:

- All seven predictions: **fully-superseded as candidate findings** by the named segments. None names content absent from canon.
- The one item the extraction left as a possible "actionable-open" (P2-ib Part B deliberation-cost conflation): **closed** by first-hand read of `der-deliberation-cost.md` — no conflation exists; the terms are deliberately decomposed.

The one thing worth *not* discarding is the extraction file's own framing of this dir's residual value: it is **external-reader calibration evidence** — seven pre-segment-walk predictions producing a high hit-rate against current `src/`, evidence the README+OUTLINE framing layer is legible to a sympathetic external reader (relevant to the CLAUDE.md "respectful pedagogy" direction). That is a meta-observation about framing quality, not a theory gem, and it is already recorded in the extraction (`audit-findings-184930.md` §II and §V). No action needed to preserve it beyond leaving the extraction file in place.

---

## Adjudicator notes

1. **Why I trust the "all in canon" conclusion despite the brief's warning that labels lie in both directions.** I did not rely on the extraction's verdicts. For the two highest-risk items — the deferral the extraction flagged as possibly actionable (P2-ib Part B) and the deferral where canon could plausibly be thin (P2-comp Layer 2) — I opened the actual segments and read the formal expressions. Both came back the *opposite* of "stale finding hides a gem": the deliberation-cost decomposition is explicit, and the composition machinery is *richer* than the prediction, carrying a signed-$\gamma$ cooperative/adversarial unification that the prediction did not anticipate.

2. **Structural reason this slice is gem-poor by construction.** A stub cycle that ended at initial-predictions produced *anticipations of what the framework would contain*, generated from the framing layer (README/OUTLINE) — not *encounters with gaps in read segments*. Predictions of the form "I expect X to be a chosen approximation / to have a fuzzy boundary / to rely on constrained assumptions" can, at best, *locate* a seam; they cannot carry un-captured content, because they were written without reading the content. The gem-bearing material in audit cycles is the *segment-walk trail and §14 wandering thoughts* — precisely what this dir lacks. This is honest scarcity, not under-mining.

3. **No strengthen-opportunity surfaced.** No prediction suggested softening a claim that canon overstates; the one near-candidate (P2-comp) resolved as canon already being stronger and broader than the prediction. There is no soften-vs-strengthen fork to flag.
