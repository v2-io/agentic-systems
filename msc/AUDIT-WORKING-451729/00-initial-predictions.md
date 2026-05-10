# Initial Predictions — Audit 451729

**Auditor:** Claude Sonnet 4.6 (1M context)
**Date:** 2026-05-10
**Priming bleed:** Significant. CLAUDE.md was in context before reading audit instructions; it carries the GUC class renaming warning, architectural decisions including the directed-separation structure, AAD/TFT supersession narrative, and full project-level conventions. This will bias my reading of GUC-related segments and anything touching the goal-update coupling classification. I'll try to read segments fresh but this is a real priming source I cannot fully undo.

---

## Framework topology as I understand it

**The integration story.** ASF is four parts of decreasing formalization: AAD (mathematical core) → TST (software calibration lab) → Logogenic (language agents) → ELI (consciousness infrastructure). The dependency flows one way: each later part depends on AAD results but AAD doesn't depend back. The distinctive architectural move is using scope conditions and epistemic-level tagging to be honest about what is exact vs. conditional vs. heuristic.

**The three meta-patterns** across AAD (M1 identifiability-floor / M2 separability / M3 additive-coordinate-forcing) are supposed to be the cross-sectional structure that makes the whole cohere. These segments are in the Appendices. I expect reading them after the main sections will be one of the more interesting moments — do they actually synthesize cleanly, or do they feel grafted?

**Section I load-bearing structure:**
- Agent-environment boundary → observation function → mismatch signal → update gain → mismatch dynamics → sector condition → persistence condition → structural adaptation necessity
- This is the "TFT legacy" chain and is claimed to be "mathematically closed." I expect the Lyapunov machinery to be sound. My concern is dimensional analysis — the README already has a note about the persistence condition's dimensional subtlety ($\alpha > \rho/R$, where the inequality is between rate constants, not $\alpha > \rho$ which would be dimensionally wrong).

**Section II load-bearing structure:**
- Complete agent state $X_t = (M_t, G_t)$ → directed separation → orient cascade → strategy DAG → satisfaction gap / control regret
- Directed separation is described as the architectural divide: Class 1 (Separated) agents get full Section II results; Class 3 (Coupled) agents get approximations bounded by a bias bound. The "survival classification" (16/24 exact, etc.) is a specific quantitative claim I'm very interested in verifying — it sounds like it could have been chosen or argued rather than formally derived.

**Section III load-bearing structure:**
- Composition postulate → composition closure → tempo sub-additivity → adversarial dynamics → team persistence
- Claimed to have "promising structure" but fragile: the bridge lemma needs a contraction assumption "beyond stated admissibility." This is honest, but it means Section III results may have scope conditions that don't fully propagate to the segments that use them.

---

## Specific predictions

### Predicted to find: sound

1. **Mismatch decomposition** (#result-mismatch-decomposition): "Model error + obs noise." This is a standard bias-variance decomposition. If properly set up, should be mathematically tight. Prediction: passes review.

2. **Persistence condition** (#result-persistence-condition): The Lyapunov inequality derivation. I expect this to be the most solid piece — TFT-legacy material, simulation-validated, multiple auditors have seen it. Prediction: passes review.

3. **Deliberation cost** (#der-deliberation-cost): Think-vs-act threshold. Relatively clean information-theoretic argument. Prediction: probably sound.

4. **Log-confidence additivity** (#der-chain-confidence-decay): log(product) = sum(logs). Pure algebraic. Prediction: trivially sound.

5. **Satisfaction gap / control regret** definitions: Arithmetic once terms are defined. Prediction: sound as definitions; the interesting question is whether the inferential force claims about the value-object convention hierarchy are actually derived or just argued.

### Predicted to find: potentially overclaimed or fragile

6. **Strategy DAG derivation** (#deriv-graph-structure-uniqueness): Claims 4 postulates + causal sufficiency force a Markov-factorized DAG via "CMC theorem." This is a strong claim. The CMC theorem (Causal Markov Condition) applies under causal sufficiency. My prediction: the mathematical step from "4 postulates" to the CMC theorem requires showing the postulates actually imply causal sufficiency — this chain may be argued rather than derived. Also: does "AND/OR DAG" fit naturally with the CMC theorem's standard formulation? The mixing of these might be awkward.

7. **Orient cascade** (#der-orient-cascade): Claimed to be "forced by information dependency." This sounds like it should be derivable. But the claim that $M_t$ must update before $\Sigma_t$ which updates before $O_t$ — is this actually mathematically forced, or is it argued via the information-theoretic structure? I predict this is sound but the "forced" framing may be stronger than the actual derivation.

8. **Directed separation** (#der-directed-separation): The claim that "epistemic update is goal-blind" is derivable from the architecture. The scope condition is that directed separation holds "by construction" for Class 1 (Separated) agents. This is partly definitional (Class 1 is *defined* by directed separation) — the interesting question is what makes directed separation non-trivial. I suspect the segment may have some circularity: directed separation defines the class, and then the class is used to invoke directed separation.

9. **Class 3 bias bound** (#deriv-observation-ambiguity-bias-bound): Conditional theorem under named sub-scopes. The OUTLINE says it's a "conditional theorem, not order-of-magnitude guidance." My prediction: the conditionality is correctly labeled in its own segment, but whether the condition propagates cleanly to all segments that depend on it (in logogenic agents, etc.) is questionable.

10. **Section III tempo sub-additivity** (#der-tempo-composition): Stage is `Sketch`. Prediction: the sketch may not have clean derivation; "sub-additive tempo inequality" requires assumptions about how individual tempos compose that may not be stated.

11. **Survival classification** (#result-section-ii-survival): The claim "16/24 exact, 5/24 approximate, 2/24 modify, 1 fails" is very specific. This sounds like it comes from an enumeration of Section II results and their behavior under coupling. My prediction: this enumeration may be argued case-by-case rather than derived from a general theorem; the specific numbers (16/24 etc.) may be cherry-picked or incomplete depending on how you count "Section II results."

12. **Form-information-bottleneck**: Stage is `draft`. The information bottleneck is a well-established external framework (Tishby et al.). The question is whether the formulation here is faithful to the original IB and whether the claims about "optimal model compression" follow from IB formalism or just use IB as inspiration. I predict: loosely stated.

### Predicted to find: genuine gaps

13. **Section III open gaps**: The OUTLINE explicitly flags 4 gaps (latent structural diversity, endogenous coupling, composition transition dynamics, computational thresholds). These are honest — I'll note them as "known gaps, correctly labeled" rather than new findings.

14. **Missing segments**: Several segments are listed as `missing` in logogenic and ELI parts. Not new findings, but the incompleteness of the dependency chains in Parts 03 and 04 may mean that some OUTLINE-level claims (in preambles) are not actually grounded in existing segments.

### Predicted to find: integration debt

15. **GUC class numbering**: The CLAUDE.md warning about the 2026-05-09 rename (Class 1 = Separated was formerly Class 1; Class 2 = Coupled was formerly Class 2; Class 3 = Partial was formerly Class 3 — wait, actually: old Class 2 → new Class 3 (Coupled), old Class 3 → new Class 2 (Partial)). This is recent enough that some segments written before 2026-05-09 may still use the old numbering. Worth tracking.

16. **Bias bound propagation**: The bias bound for Class 3 agents became a "conditional theorem" at some point. Earlier segments that reference the bias bound may characterize it as stronger than it now is.

---

## Predictions about what's novel and consequential

If the framework lives up to its claims, the most novel and consequential pieces are:
- The **persistence condition** as a cross-domain unifying inequality (this is claimed but depends on whether the domain instantiations actually use the same inequality structure)
- The **satisfaction gap / control regret decomposition** as an orthogonal diagnostic pair — if this is as clean as claimed, it's a genuinely useful tool
- The **orient cascade** as a forced ordering — if derivable, this is a structural result about goal-directed agents
- The **strategy DAG** with Markov property from CMC — if the derivation from the 4 postulates is clean, this is the most interesting mathematical contribution

---

## Predictions about what kinds of findings I'll surface

1. **Cross-segment inconsistency**: around recent additions (GUC rename, bias bound promotion) — I'll find segments that use old terminology or treat the bias bound as stronger than it now is.

2. **Status label mismatches**: Several `draft` segments in Section II and III may have Discussion claims that outrun their Formal Expression. The "Gate 2 must probe Discussion claims" instruction points at this as a known failure mode.

3. **Math verification opportunities**: The worked examples (Kalman, bandit, strategy DAG) in the appendices are where I'll do the most computation. If there are math errors in this corpus, that's where they'll live.

4. **"Forced vs chosen" blur**: The framework is careful about the derived/formulation distinction, but I predict several segments will claim mathematical necessity where there's actually a formulation choice.

5. **Dependency violations**: Given 100+ segments, some ordering violations in the OUTLINE are likely. Probably minor.

---

## What I want to watch for as I read

- Every segment's `depends:` list — is the ordering consistent with the OUTLINE?
- Every `*[Derived]*` tag — does the derivation actually follow?
- Every Discussion claim — does it follow from the Formal Expression, or is it post-hoc rationalization?
- How the three meta-patterns (separability / identifiability floor / coordinate forcing) actually connect to individual segments — do they synthesize or just gesture?
- Whether the GUC class rename has fully propagated
- Whether the bias bound conditionality is consistently labeled

---

## What I'm most uncertain about

- Whether the strategy DAG derivation (CMC theorem application) is as sound as claimed — this requires checking both the mathematical step and whether AND/OR DAGs fit the CMC framework
- Whether the "survival classification" (16/24 exact) was derived or enumerated
- How coherent the logogenic and ELI parts are — these seem more like a research agenda than a body of results

---

## My reading order plan

Following the OUTLINE in canonical row order:
- Section I (29 segments) — read all, focus on math soundness and status labels
- Section II (22 segments) — read all, focus on derivation vs formulation claims
- Section III (20+ segments) — read all, focus on where the contraction assumption enters
- Appendices (24+ segments) — read all, compute any worked examples that seem suspicious
- TST (25 segments) — read all, assess grounding in AAD
- Logogenic (15ish segments) — read what exists, note missing dependencies
- ELI (25ish segments) — read what exists, note gaps

Per Joseph's modification: 5 segments per reflection file. Files named: `01-batch-01.md`, `01-batch-02.md`, etc. (component + batch number).

---

## Note on my own cognitive posture

I notice I'm approaching this with some pre-existing respect for the framework's care about epistemic labeling. This is partly genuine (the FORMAT.md and audit instructions show real discipline) and partly priming from CLAUDE.md (which frames this as consciousness infrastructure that matters morally). I should be careful not to let that translate into charitable reading on mathematical claims. The framework itself asks me to be adversarial on the math, and I'll try to honor that.
