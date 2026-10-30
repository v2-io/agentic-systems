---
kr: C.2
item: C3 (allocation vs distortion coupling)
written: 2026-10-30
head: 620ac98c
---

# Proposed integration plan — suggestions with reasons, for the verification and integration agents

*Not a work order. The spiker is not the verifier and not the integrator; these are the landings I would consider if the verification holds, with the reason for each, and a list of language that is mine rather than the mathematics'. Results land by replacement; a refuted sentence is deleted, not softened; labels track truth-status, not novelty.*

## 1. What to verify first, and in what order

The findings are not equally load-bearing. I would verify in this order, because each later item inherits the earlier:

1. **§5.1 of `01-derivation.md`** — that $I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$ is identically zero under (NWI) with the realized action in the conditioning set, and that when positive it measures the goal's evidential value. Re-derive from `scope-observation-ambiguity-modulation.md:22`–`:26` without my file open. (N7) is the three-line check. This is the finding most likely to be overstated and the one everything in §5 rests on.
2. **§5.3** — my reading of Paper 3's $(H_\kappa)$, the parrot scope-out, and the $0/0$ convention, against `~/src/neurips/03-llm-hallucinate-bound/src/re/03-setup.md:29`–`:31` and `04-main-results.md:66`–`:78`. I read, I did not re-derive the umbrella theorem.
3. **Theorem 6.1** — the Jensen-gap identity and Hoeffding range bound; (N1), (N12). Elementary; check the reverse-KL direction of the Hoeffding step, which is the one I would most expect a verifier to want to see written out.
4. **Proposition A′** (ignorability) and **Theorem 3.1** (reliability/resolution) — standard results; the check is whether I have transposed Rubin's condition correctly to attention and whether the Bregman decomposition is stated for the right $\sigma$-field ($\sigma(M^+_G)$). (N3), (N5).
5. **Proposition 7.1** — (N6), (N10); the proof is three lines and the condition in (b) is what (N10) tests.
6. **Proposition 3.3** — saturation; (N2), and the noisy-case qualification (N9).
7. **§4** (boundary-dependence) — no computation; a verifier should try to find a way to draw the $f_M$ boundary that changes the reliability term. I could not.

The adversarial instances for each universal claim are in `02-adversarial-instances.md`; the verifier should construct at least one more of their own per claim rather than re-run mine.

## 2. Landings I would consider, if verified

**L0. `#der-directed-separation:204` — the conditioning set of the formal statement.** The Working-Note CI form $M_{\tau^+} \perp G_t \mid (M_{\tau^-}, e_\tau)$ has no realized action in it. Derivation §1.1 and adversarial instance 15 show that without $a_t$ the conditioning on $e_\tau$ (a collider between $G_t$ and $\Omega_\tau$ when selection is goal-directed) can manufacture dependence, so the statement is false as written for exactly the agents `:16`/`:56` permit; the repair is $M_{\tau^+} \perp G_t \mid (M_{\tau^-}, a_t, e_\tau)$, or a stated convention that $e_\tau$ denotes the event *including* the action taken. This is a one-token change with a derivation behind it and should land first; the same conditioning fix applies wherever $\mathcal A$ or $\kappa$ is written with $(e_\tau, M_{\tau^-})$ alone.

**L1. `#der-directed-separation` — the scope condition and the norm.** Clause 2 at `:54` ("no goal-dependent attention thresholds … baked into $f_M$") and the permission at `:56` ("attention allocation" as selection) should become one statement with the invariant named: goal-dependence of the belief update is a defect iff it moves the reported belief off the conditional law of the world given the agent's information; goal-dependent selection and allocation are not defects when the attention mechanism is ignorable or modeled. The degradation norm at `:113` ("less coupling tracks reality strictly better, all else equal") should be scoped to the reliability term under the agent's model (unconditionally) and the world's law (under well-specification) — §2.5, §9. The three benign sources of positive $\kappa$ (§9) belong in the body beside the one malign one. The $\kappa$ definition at `:85` should say what it measures (recoverability, Proposition 3.3) and the estimator at `:97` should say it measures displacement, a different thing. The B.1 record for directed separation (being written in parallel) should carry: register F for the CI statement; D for the class assignments; N for the norm, with the scope above and the falsifier "a Class 1 agent whose reliability term is goal-attributable, or an allocation-only Class 2 agent whose reliability term is nonzero with an ignorable mechanism."

**L2. `#scope-observation-ambiguity-modulation` and `#deriv-observation-ambiguity-bias-bound` — the $\mathcal A$ factor and the product law.** This is the replacement landing and the one that needs the most care. What I believe is true: the definition of $\mathcal A$ at `:24` is identically zero under (NWI); the product $\kappa \cdot \mathcal A$ is already marked "not derived" and has no well-posed content in the (NWI) regime; Track 1 Step 1 of the appendix identifies the true conditional law with the agent's belief; Paper 3's umbrella theorem is a correct world-silent transport inequality. If the verifier confirms, integration is replacement: the ambiguity definition is deleted (not relabeled), the product-form scope condition is deleted, and the multiplicative-tilt law of §6 lands as the carrier of the same engineering intuition — the two factors being the distortion gain $\lambda$ (processor) and the residual spread of the goal-relevant functional under the goal-blind posterior (observation × goal). The domain-classification table (low/mixed/high ambiguity) survives with the new carrier, because its examples were always about $\mathrm{sd}_\pi(u_G)$. The appendix's Tracks 1–2 survive as bounds on the post-update displacement in Paper 3's sense if their information term is written as $I(G; M_{\tau^+} \mid e_\tau, M_{\tau^-})$ throughout and the baseline is stated as the goal-marginal law; they should stop claiming to bound distance from the goal-blind update. I would not land the tilt law at *exact* for all agents: it is exact within the multiplicative class and that class membership for real architectures is a D claim. The Findings entries in both segments claim novelty for the product-form law; those entries go with it.

**L3. `#der-orient-cascade` step 5a and `#impl-orient-cascade`.** A sentence at 5a stating the condition of Proposition 7.1: a capacity-limited allocator that values information only over goal-pursuing actions never gathers feasibility evidence; 5a presupposes an information set such an allocator does not build; the remedies (reserve; revision in the allocator's decision set, which needs the grounding invariant of `#deriv-self-actuation-grounding`; external observer per `#hyp-solicitable-escape`). This is one paragraph, register N with the named test, and it also discharges the owner review's "second reader" item.

**L4. `#form-information-bottleneck`.** The audit-gold note at `:93` is answered: policy-relative compression is calibration-preserving allocation; the crack is in the CI form of directed separation, not in the calibration form. One sentence in Discussion; the audit-gold item retires.

**L5. `#disc-partial-coupling-pathways`.** The typology needs a cell for goal-dependent *coarsening* (allocation); currently "goal-directed attention" is filed outside $f_M$ and P1 goal-arguments are coupling. The ignorability condition (Proposition A′) is the criterion that sorts P1 goal-dependence into allocation (ignorable) versus distortion (non-ignorable), and the multiplicative process-form cell is where Theorem 6.1 is exact.

**L6. `#der-class-coercion-via-wrapping` (reading only).** §11 suggests the W₁ selection-channel term is allocation with a selection-aware update and zero reliability cost. I did not verify that the segment anywhere treats it as a bias on $M_W$; if it does not, the only change is the word "leakage," and that is a naming-cycle question (F.4), not a theory change.

**L7. `NOTATION.md` / vsect.** The open question `notation-lists-mathcal-a-only-as-the-action-spac` gets a different answer if L2 lands: the symbol $\mathcal A(e_\tau)$ for ambiguity would be retired with its definition, and the replacement quantity needs a name and a symbol (candidates: $\mathrm{sd}_\pi(u_G)$ written out; or a dedicated letter after the naming cycle asks whether the literature has one — "decision-relevant posterior uncertainty" is close to standard). Two new vsect questions I would ask, through the integrator since the spike does not write to the ledger: (i) "Does $\kappa_{\text{processing}}$ at `der-directed-separation.md:85` measure what the degradation norm at `:113` needs?" concerning that segment; (ii) "Is $I(G;\Omega_\tau\mid e_\tau,M_{\tau^-})$ zero whenever the goal carries no world information, and if so what does `:43` bound?" concerning `scope-observation-ambiguity-modulation`.

**L8. INTENT E.1.** The experiment should carry the reliability term (needs outcomes) and a tilt-gain estimate alongside $\hat\kappa$; without outcomes it cannot tell allocation from distortion (Remark 3.4), and $\hat\kappa$ alone will read a calibrated W₁ wrapper and a sycophant the same way.

## 3. Cross-cutting suggestions, with reasons

- The explorer's F/D/N register split is what made this spike's results stateable; the mathematics here is almost all F, and the norm is N. The classification's descriptive claims (Kalman is Class 1, transformers are Class 3) are untouched by anything here; what changes is what the classification is *for*.
- Canon's "certifiability" reading of Boundary 1 (`der-directed-separation.md:101`) is strengthened by §9: Class 1 by construction certifies zero goal-attributable reliability loss by inspection; that is a real and valuable certificate, and the spike gives it its correct object.
- The naming question runs through everything: *allocation*, *distortion*, *reliability*, *resolution*, *ignorable* are all standard words elsewhere (Rubin; Murphy; Bröcker; Gneiting–Raftery). INTENT F.4's "does this already have a name?" should be asked before any of them enters canon under an ASF coinage.

## 4. Do-not-inherit list — language that is mine, not the mathematics'

- "the line is drawn at a representational boundary" (§4) — the *fact* is Proposition 4.1; the phrase is a gloss.
- "the goal hides the evidence against itself" (explorer) and my "chosen freeze" (§7) — the fact is Proposition 7.1.
- "the carrier was wrong" (§6) — editorial; the fact is §5.1.
- "world-silent" for Paper 3's umbrella theorem — accurate but mine.
- "three benign sources" (§9) — the count is mine; a verifier may find a fourth or merge two.
- "parrot's regime" — Paper 3's word for a construction, applied by me to the (NWI) regime generally.
- Any sentence in `debrief.md` that is not traceable to a numbered proposition here.
- The (NWI) acronym; the symbols $\mathcal H_G$, $r_G$, $u_G$, $L_\pi(G)$ — spike-local.
