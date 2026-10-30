---
kr: C.2
item: C3 (allocation vs distortion coupling)
opened: 2026-10-30
head: 620ac98c
status: spike landed; awaiting independent verification (spiker ≠ verifier ≠ integrator)
---

# Spike: allocation versus distortion coupling (item C3)

**The question.** When an agent's goals influence its belief update, canon's directed-separation condition forbids it (processing must be goal-blind) while permitting goal-directed *selection* of events. The owner review's Part II explorer proposed that goal-dependence inside the update comes in two kinds — *allocation* (what gets encoded) and *distortion* (how the agent updates on what it encoded) — only the second of which corrupts belief, and asked whether canon's measure $\kappa_{\text{processing}}$ and its $\kappa \cdot \mathcal A$ bias bound can tell them apart.

**What happened, in one paragraph.** The split holds, with its conditions named: allocation preserves calibration iff the attention mechanism is ignorable in Rubin's sense or modeled; distortion strictly costs under every proper scoring rule under the agent's own model, and under the world's law when the model is right. The two are separated by the standard reliability/resolution decomposition of proper scores, which needs outcomes; $\kappa_{\text{processing}}$ cannot separate them and, as a mutual information, measures the goal's detectability in the belief rather than displacement. The selection/processing line in canon is drawn at a representational boundary and that is why it is drawn inconsistently; calibration is the invariant underneath. The bias bound's ambiguity factor $\mathcal A$ is identically zero when the goal carries no world information and positive exactly when using the goal is correct Bayesian updating, so the product law has no well-posed content in the regime the degradation norm covers; a replacement law (a Jensen-gap identity for multiplicatively tilted beliefs) carries the intended intuition with well-defined factors and is zero for allocation-only agents. Cascade step 5a is starved by a goal-allocated encoder exactly when the allocator's decision set lacks the objective-revision option.

**Where everything is.**

| File | What |
|---|---|
| `00-neighborhood-map.md` | what canon holds around the question, the live tensions, the regression check |
| `01-derivation.md` | the mathematics, claim by claim, with registers and completion states (§12) |
| `02-adversarial-instances.md` | one out-of-family instance per universal claim; what scoped and what survived |
| `sims/check.py`, `sims/check-output.txt` | exact-enumeration checks N1–N13 cited throughout |
| `lit-scan.md` | the literature scan (written by a Sonnet-class agent from the web only; its §7 is the verification status; it supplied the access condition on Prop A and the four standard names for the split) |
| `proposed-integration-plan.md` | suggestions for the verifier and integrator, in verification order, with a do-not-inherit list |
| `debrief.md` | for readers who will not read the above; written last from the corrected files |

**Discipline notes.** Write-scope was this directory only; no canon, OUTLINE, INDEX, or tracker was edited. Commits are by explicit path on the commit itself. Clock times are from `date -u`.
