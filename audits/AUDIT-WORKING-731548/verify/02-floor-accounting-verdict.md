# Independent Adversarial Verification — Floor Accounting (mismatch-decomposition "reducible" label + class-fitness detection signature)

*Verifier pass 2026-07-02, AUDIT-WORKING-731548 verify track. Sources: primary segments, `spikes/` (including `.integrated/`), `spikes/INDEX.md`, `audits/audit-findings-{451729,526815,584721,742613,963715}.md`, `TODO.md`, OUTLINE rows, git log. Adversarial posture: attempted to refute both parts and to find dissolving context.*

## Verdicts

| Part | Verdict | One-line basis |
|---|---|---|
| (1) "reducible" model-error label / missing Bayes floor | **REAL-AND-OPEN** | No prior audit, tracker, or canon segment makes the split; the historical spike record *had* the correct boundary (2026-04-24) and *lost* it in the 2026-05-18 recheck landing — the finding restores a distinction the working layer once drew. |
| (2) class-fitness detection signature conflates ceiling with noise floor | **REAL-BUT-ALREADY-FLAGGED** (staged in Working Notes, unexecuted) | The exact wording fix and the residual-structure discriminator are already recorded as WN follow-ups/gold on `#result-structural-adaptation-necessity` (526815/742613, 829314) and the F-vs-$\rho$ disentanglement is the "single most convergent" reader question in `#def-model-class-fitness` WN; the body fix has not been executed and the propagation to the fitness segment's signature sentence is not itself tracked. |

Neither part is a regression. Part 1 is genuinely new against the certified record; part 2 should be raised as *execution* of existing WN items plus one new propagation demand, citing them.

---

## Part 1 — the "reducible" label

### 1.1 The math holds (with one edge correction)

For any chronica-measurable predictor $\hat o_t$ (and all AAT predictors are: $\hat o_t = \mathbb E[o_t \mid M_{t-1}, a_{t-1}]$ per `#form-agent-model`, $M$ built from $\mathcal C$), the model-error term satisfies, by the tower property and GA-1,

$$\mathbb E\lVert \hat o_t - \bar o_t \rVert^2 \;\geq\; \mathbb E\big[\operatorname{Var}(\bar o_t \mid \mathcal C_{t-1}, a_{t-1})\big],$$

with equality at the Bayes predictor $\hat o_t^{\mathrm B} = \mathbb E[o_t \mid \mathcal C_{t-1}, a_{t-1}]$. The floor is strictly positive whenever residual state uncertainty *moves the one-step conditional mean* — the same alignment-type qualifier the segment already uses for the $S(M_t) \lt 1$ connection.

**Edge correction to the claim as stated:** "$\gt 0$ exactly when $H(\Omega_t \mid \mathcal C_t) \gt 0$" is slightly too strong. $H(\Omega_t \mid \mathcal C_{t-1}) \gt 0$ is *necessary but not sufficient*: if the residual uncertainty lives only in directions that leave $\bar o_t = \mathbb E[o_t \mid \Omega_t, a_{t-1}]$ unchanged (higher-moments-only, or mean-irrelevant state coordinates), the mean floor can be zero. State the finding with the alignment qualifier; the segment owns that vocabulary already.

**The unused-step-1 irony is confirmed.** Derivation steps 2–4 never use step 1's $H(\Omega_t \mid \mathcal C_t) \gt 0$; positivity comes from noise non-degeneracy or misspecification. AUDIT-WORKING-742613 noticed the unused invocation and filed it as *minor derivation-cleanliness* (now in the segment's WN follow-ups) — it did **not** draw the substantive implication that the cited fact is precisely what bounds the "reducible" term away from zero. The certified record contains the observation's shell but not its content.

### 1.2 Decisive historical evidence: the boundary was drawn correctly once, then silently moved

This is the strongest thing the record shows, and it *confirms* rather than dissolves the finding:

- **`spikes/spike-rho-additive-variance-strengthening-2026-04-24.md` §2.2** defines the irreducible rate at the *right* boundary: $\rho^2_\star(\text{env}) := \nu \cdot \inf_{\mathcal M^\ast \in \mathfrak M_\infty} \mathbb E[\lVert\delta_t\rVert^2]$ — the **Bayes-optimal predictor in a maximally-expressive reference class**. Since every substrate-implementable predictor is chronica-measurable, this infimum equals $\nu\,(\mathbb E[\operatorname{Var}(\bar o \mid \mathcal C, a)] + \mathbb E[\operatorname{Var}(o \mid \Omega, a)])$ — floors 2 + 3 of the auditor's taxonomy, *both* inside "irreducible."
- **`spikes/.integrated/spike-rho-structure-recheck-2026-05-18.md` §3** (the version that landed in canon as `#internal-external-decomposition`'s (2T)) **redefines** $\rho_\star^2(\text{env};\pi) := \nu\,\mathbb E[\operatorname{Var}(o_t \mid \Omega_t, a_{t-1})]$ — channel-instant variance only, floor 3 — while *keeping* the gloss "the disturbance power even the Bayes-optimal predictor cannot remove" and adding "$\Delta_{\text{agent}}^2 \ldots$ zero iff the model is correctly specified on the realized distribution." Both glosses are false as stated: the Bayes-optimal predictor also cannot remove $\mathbb E[\operatorname{Var}(\bar o \mid \mathcal C, a)]$, and no chronica-measurable predictor attains $\hat o = \bar o$ in-scope, however correctly specified.
- The recheck spike caught the (AV) spike's vacuous-cross-term defect but **did not notice its own $\rho_\star$ definition differs from the (AV) spike's by exactly the state-uncertainty term.** The independent verifier of the 2026-05-18 landing (per `#internal-external-decomposition` WN) caught two pedigree over-claims but not this one. `spikes/INDEX.md` marks the family "FULLY RESOLVED 2026-05-21." The discrepancy is unreconciled and untracked.

### 1.3 Canon's own calibration anchor refutes the "vanishes" gloss concretely

`#example-kalman` ("The mismatch is the innovation"; "calibration on a problem with known exact answers"): the steady-state *optimal* Kalman filter — well-specified by construction — has innovation variance $H P^- H^\top + R \gt R$. The excess $H P^- H^\top$ *is* floor 2 (filtering/state-uncertainty error), sitting inside the decomposition's "model error (reducible)" term and removable by no model in any class. `#internal-external-decomposition`'s sentence "the first term … **vanishes for a well-specified model**" is contradicted by the framework's own exact worked example. (Adjacent irony: the recheck spike's *no-go* §4.1 leans on Kalman Riccati $P^\ast$ being positive — the same object that breaks its own §3 gloss.)

### 1.4 Where the mislabel propagates (blast surface)

1. `01-aat-core/src/result-mismatch-decomposition.md` — the labels in (28), body ¶1, Discussion ¶1 ("reducible" unqualified). `status: exact`, `claims-verified`. The *identity* is exact and stays exact; the defect is the label plus the reducible-down-to-zero implicature.
2. `01-aat-core/src/internal-external-decomposition.md` — "vanishes for a well-specified model" (§The disturbance is additive); "$\mathcal V_{\text{agent}}$ … improves as the agent improves" inherits the implicature; OUTLINE row A repeats "reducible model-error vs irreducible environmental floor."
3. `spikes/.integrated/spike-rho-structure-recheck-2026-05-18.md` — history layer; stays verbatim per convention, but the reconciliation note belongs in the successor canon.
4. Checked and clean: `#disc-independence-audit`, `#disc-approximation-tiering` (no floor taxonomy, no conflicting claims); `#der-architecture-noidentifiability` (carries the Regime-C $\mathcal M/\pi$/cross confound — a *different*, finer question than the Bayes floor; does not make or need the floor-2/3 split); prior certified findings on this segment (451729 P1, 526815 F8, 584721 F-A6, 742613 seg-19, 963715 seg-18) all verify the algebra or deps — none touch the label.

### 1.5 What was searched for and not found (the dissolve attempts)

- No canon segment, TODO item, PROPOSALS entry, pending-findings entry, or TERMINOLOGY item tracks a Bayes/state-uncertainty floor or questions "reducible." The only greps that hit are the two spikes above and the caller's own working dir.
- Steelman "reducible just means agent-side vs channel-side": the prose goes beyond that reading — "The model can improve the first term" survives, but "vanishes for a well-specified model" and "zero iff correctly specified" do not; and the fitness/necessity chain downstream *uses* the reducible-to-floor reading operationally.
- Steelman "GA-1 removes the floor": GA-1 whitens $\varepsilon_t$, not state uncertainty. No.
- Steelman "the alignment caveat already covers it": the alignment caveat governs the $S \lt 1 \Rightarrow$ term-(i)-positive direction (insufficiency implies error). The Bayes floor is the converse-side fact (even sufficiency-relative-to-history leaves error). Related vocabulary, distinct claim; not covered.

### 1.6 Repair shape — this is a strengthening, not a soften

The available landing is *strictly stronger* than the current result: under GA-1 plus the same tower orthogonality, the two-term identity refines to an exact **three-term Pythagorean decomposition** (all cross terms vanish — the first by conditioning on $(\mathcal C_{t-1}, a_{t-1})$, the second by the existing GA-1 argument):

$$\mathbb E\lVert\delta_t\rVert^2 = \underbrace{\mathbb E\lVert\hat o_t - \hat o_t^{\mathrm B}\rVert^2}_{\text{estimation error (reducible by modeling)}} + \underbrace{\mathbb E[\operatorname{Var}(\bar o_t \mid \mathcal C_{t-1}, a_{t-1})]}_{\text{state-uncertainty floor (irreducible by modeling; movable by acting)}} + \underbrace{\mathbb E[\operatorname{Var}(o_t \mid \Omega_t, a_{t-1})]}_{\text{channel noise (irreducible)}}$$

This also converts step 1's currently-unused $H(\Omega_t \mid \mathcal C_t) \gt 0$ citation into load-bearing content (it is what makes the middle term generically positive, under the alignment qualifier). Two bonuses the two-term form cannot express: (a) the middle floor is **irreducible-by-modeling but partially reducible-by-acting** — more informative action/observation history shrinks $\operatorname{Var}(\bar o \mid \mathcal C)$ — the natural hook to `#def-causal-information-yield` / active sensing that canon currently has no way to state at the decomposition; (b) it reconciles the two spikes' $\rho_\star$ definitions explicitly (2026-04-24's $\rho_\star^2$ = floors 2+3; 2026-05-18's = floor 3 alone). Minimal fallback if the three-term form is deferred: parenthetical relabel ("reducible — to the estimation floor; see below") + delete-and-replace of internal-external's "vanishes for a well-specified model" sentence (integration-is-replacement: the false sentence goes, present truth replaces it; the history stays in WN/CHANGELOG).

---

## Part 2 — the detection-signature conflation

### 2.1 Substantively correct, including the normalization arithmetic

$S$ and $\mathcal F$ are ratios of retained-to-total *predictive information in the history* (`#def-model-sufficiency` (22)); channel noise depresses the denominator and numerator together. So $S = \mathcal F = 1$ is fully compatible with an arbitrarily high *absolute* mismatch floor — and, with part 1, even the floor's "model error" component stays positive at $\mathcal F = 1$ (floor 2). "Persistent mismatch despite adequate learning" (`#def-model-class-fitness` body ¶2 + Discussion "Detecting low class fitness") is therefore the signature of $\{\text{low } \mathcal F\} \cup \{\text{fine class, noisy world}\}$, and acting on it as stated risks exactly the "catastrophic thrashing — rewriting a codebase that just needed a few more bug-fixes" the WN gold already names. Confirmed.

### 2.2 But the record already carries most of it — cite, don't re-discover

- **The wording fix exists verbatim** in `#result-structural-adaptation-necessity` WN Follow-up 1 (from 526815/742613): keep *systematic* / "after excluding channel / disturbance / nonstationarity / gain-miscalibration causes" adjacent to the diagnostic corollary, "otherwise a reader could mistake high mismatch from noise … for structural inadequacy." Unexecuted; body unchanged.
- **The discriminator exists in canon bodies**, not only in gold: derivation step 3 and symptom 3 say *systematic / structured* residuals; `#example-kalman` triggers class change on "sustained residual autocorrelation"; `#example-L1` detects via "persistent structured residuals after convergence." The U-shape-vs-white autocorrelation mechanism as such is WN gold (829314) staged for Discussion promotion.
- **The F-vs-$\rho$ disentanglement** is `#def-model-class-fitness` WN "Readers often ask" item 1 — flagged there as "the single most convergent question on this segment," pointing forward to `#result-structural-adaptation-necessity` for the sharp diagnostic.
- **Genuinely new in the caller's finding:** (i) the normalized-fraction arithmetic stated as arithmetic (the WN gold's "$S$ is naturally bounded" version is actually *wrong* — noise shrinks the denominator, $S$ can still reach 1; the caller's version is the correct sharpening); (ii) the propagation demand on `#def-model-class-fitness`'s own signature sentence (the WN follow-up sits on the *other* segment; nothing tracks fixing the sentence where the signature is *defined*); (iii) the composition with part 1 into one routing taxonomy.

### 2.3 Answer to the caller's direct question

`#result-structural-adaptation-necessity`'s trigger is **partially** net-of-noise: derivation step 3 and symptom 3 carry the *systematic/structured* qualifier, but the headline corollary sentence ("Persistent irreducible mismatch (after parametric convergence) is diagnostic of model class inadequacy") does not — and it overloads "irreducible" against `#result-mismatch-decomposition`'s channel-noise sense (a vocabulary collision worth a TERMINOLOGY note). One further sharpening the record nowhere states: for the Bayes-optimal predictor the innovation sequence is a martingale difference (white), so residual structure cleanly separates {reducible by learning or class change} from {floors 2+3}; floors 2 and 3 are then separated from each other only by intervention/instrumentation (CIY / better sensors), not by any residual statistic. That completes the three-way routing: **structured residuals $\Rightarrow$ class/estimation problem; white residuals + high floor + CIY available $\Rightarrow$ act to inform history; white residuals + floor unmoved by acting $\Rightarrow$ channel, buy sensors or accept.**

---

## Disposition recommendation

- **Part 1: certify as a new finding.** Repair as strengthening (three-term exact decomposition, §1.6), touching `result-mismatch-decomposition` (labels + derivation step 1 made load-bearing), `internal-external-decomposition` (delete-and-replace the "vanishes" sentence; reconcile $\rho_\star$ definitions in body, history note in WN), OUTLINE row A. The identity's `exact` status is untouched — this is label/claim-scope truth, and the refined form is *more* exact content, not less.
- **Part 2: route as execution of the staged WN items**, citing them (526815/742613 follow-up; 829314 discriminator gold; the fitness-segment reader-question), plus the one new item: the signature sentence in `#def-model-class-fitness` body ¶2 / Discussion gets the systematic-net-of-noise qualifier and a pointer to the discriminator. Fold the part-1 floor taxonomy into the same touch so the corollary's "irreducible" overload is resolved once.
- **NEEDS-JOSEPH: no** for either part on content (both are within normal finding→repair cycles); flag to him only that the 2026-05-21 "FULLY RESOLVED" INDEX row for the $\rho$-family reopens one notch (definitional reconciliation), since that row carries a closure he ratified.
