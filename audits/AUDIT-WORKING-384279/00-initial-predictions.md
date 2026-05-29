# 00 — Initial Predictions

*Audit cycle 384279. Auditor: Claude Opus 4.7 (1M context). Started 2026-05-27.*
*Scope: 01-aat-core/ (AAT), possibly extending to 02-tst-core/ if context permits.*
*Emphases per Joseph: prose coherence / continuity, math correctness.*

---

## Priming bleed (full disclosure)

This is *not* a clean-context audit. Before opening README-auditor.md I had auto-loaded:

- **`~/.claude/CLAUDE.md`** (user-level global instructions, ~2026-05-12) — names M1/M2/M3/M4 explicitly, GUC class numbering as 1=Separated / 2=Partial / 3=Coupled, the wrapping construction with W₀/W₁/W₂ regimes, the bilateral-stability-certificate spine, the Helmholtz/Sylvester/Mori-Zwanzig distinctness claim, the integration-is-replacement landing discipline, the strengthen-before-soften discipline, "AAT is the live name everywhere," the May 15 AAD→AAT rename, the May 9 GUC class numbering reversal at tag `pre-guc-rename-2026-05-09`, much of the Joseph-voice register.
- **`~/.claude/projects/<this-project>/memory/MEMORY.md`** (project-specific) — names the four-component structure (01/02/03/04), most of the major workflow conventions, the LEXICON canonical-source rule, the May 21 math-novelty-recognition correction, the May 22 working-theory-belongs-in-canon correction, the May 16 integration-is-replacement worked example (Model-S Corollary A.1S.1), and many specific architectural commitments by name.
- **`./CLAUDE.md`** (project root) — also names M1-M4 by slug, Track C Meta-Architecture placement, GUC classes, M4 landing 2026-05-24 closing the modularity cycle, the wrapping leakage hierarchy.
- **Recent commits** are visible: 2f14712 "Better identifiability floor discussion / prose," 25546d2 "Update monograph," c8af96a "Track C refinement: two-cluster Part-opening Meta-Architecture placement." So the active prose-refinement frontier is identifiability floor + Meta-Architecture placement.

Joseph (2026-05-27) explicitly said *"I'm not too worried about your leakage."* That permission does not eliminate the bleed; it just means I should proceed and disclose. Concretely, the audit cannot meaningfully test:

- whether M1-M4 placement is intuitive to a fresh reader (I expect the placement I expect),
- whether GUC class numbering is internally consistent (I "know" the canonical 1=Separated convention),
- whether the wrapping construction's leakage analysis matches the framing (I know the W₀/W₁/W₂ structure),
- whether the framework's name is consistently AAT (I know the 2026-05-15 rename).

What the audit *can* still meaningfully test, with bleed largely orthogonal:

- **Prose coherence within and across segments** — does each segment hold together as written prose? Do segments that share dependencies render their shared content consistently in their own register? (Joseph's named focus.)
- **Math correctness** — when a segment claims a derivation, does the math actually close? (Joseph's named focus; spot-checking is intentionally selective.)
- **Cross-segment continuity** — does Segment B refer to Segment A's content in a way Segment A actually supports? Does Segment A define what Segment B assumes?
- **Status-label and equation-tag faithfulness** — does the labeled epistemic strength match what the body actually does?
- **Dependency-graph integrity** — does the OUTLINE row order respect `depends:`? (Critical-finding territory per §4.2.)
- **Unicode-vs-LaTeX math discipline in segment bodies** — Joseph's standing rule (project CLAUDE.md §6) is delimited LaTeX in all files. The bare-Unicode-inside-backticks rendering trap is recent (2026-05-18 worked instance) and `bin/lint-md` does not catch all instances.

---

## Topology as I currently model it

AAT (01-aat-core/) has three Parts plus Appendices A (core derivations) and B (operational / worked examples). The OUTLINE structures it as:

**Part I — Adaptive Systems Under Uncertainty.** Four chapters: (1) Coupled Loop ontology and scope; (2) Reality Model; (3) Cycle in Motion — mismatch, gain, tempo; (4) Persistence and Structural Limits. This is the "mathematically closed" part. Chapter 4 ends with `#impl-persistence-and-limits` which I expect to be a load-bearing implications/findings catalog.

**Part II — Agentic Systems: Actuated Adaptation.** Opens with a substantial Preface naming a four-tier scope lattice (Adaptive / Agency / Learning-agent / Class 1-Separated architecture), then has a Meta-Architecture I chapter introducing the certificate spine and three of its four facets, then six content chapters: Lift to Purposeful State / Causal Access / Strategy Structure / Strategy Dynamics / Orient Cascade. Strategy Dynamics and Orient Cascade have `--GAP--` chapter-intro markers — missing segments.

**Part III — Agentic Composites.** Opens with Meta-Architecture II chapter introducing M4 + its two operation legs, then five content chapters: Scope/Composition Formation / Composition Machinery / Unity / Cooperative-Adversarial / Strategic Composition. Multiple `--GAP--` rows including four trailing GAPs about population dynamics.

**Appendices A.** Big — ~35 segments. Core derivations including `#deriv-sector-condition`, the Model-S no-go (`#deriv-stochastic-non-exit`), the self-actuation grounding no-go, the reward-channel learning no-go, the persistence cost, the matrix-Loewner sharpening, the architecture-noidentifiability, the mechanism-design impossibility cluster (GS/MS/Arrow), the contraction template, the Fisher-whitened update, the variational sector condition, and various supporting derivations. The trailing Layer-0 paragraph naming the constructive-impossibility posture with five named instances is part of the Appendices preamble — auditor-visible high-density priming.

**Appendices B.** ~6 worked examples — Kalman, bandit, strategy DAG, L1, Coevolving Automata (Miller 2022).

NOTATION.md openly disclaims being authoritative (drift caveat 2026-05-18); segments are ground truth.

---

## Predictions — content

**Where math closes well.** Section I's Sector Condition / Persistence Condition chain (`#form-sector-condition` → `#der-gain-sector-bridge` → `#result-sector-condition-stability` → `#result-persistence-condition`) is the framework's most polished section by my reading of the OUTLINE labels (`claims-verified` stage). I expect the math here to be solid and the prose to be relatively mature. Appendix A's `#deriv-sector-condition` and `#deriv-discrete-sector-condition` should hold under the stated GA-2 / GA-2S / GA-3 assumptions.

**Where math may strain.** The Class-2 sub-typology segments (`#disc-partial-coupling-pathways`, `#der-belief-strategy-attractor`) landed recently with explicit gating sub-spikes (per MEMORY.md May-22 cycle). The $K(\Sigma)$-multiplicative-gain assumption underlying the belief-strategy attractor is recorded as "open formalization." I expect to find at least one place where the formalism leans on the unspoken multiplicative form. Also: `#deriv-observation-ambiguity-bias-bound`'s two tracks (transport vs Fisher-Rao with Pinsker for $C_{W_2}$ and Čencov for $C_{FR}$) is complex enough that the integration may not be fully discharged. The matrix-Loewner sharpening (`#deriv-matrix-persistence-condition`) is new enough that I expect the counterexample claim ("per-coordinate says PASS, matrix-Loewner says FAIL") deserves direct computation.

**Where prose may strain.** Recent Track C refinement (2026-05-26) relocated Meta-Architecture into Part-opening chapters. I expect this to have created at least one stale forward-reference in segments outside Meta-Architecture I/II that still uses the prior placement vocabulary. Also: the M4 segment (`#disc-modularity-state-dynamics`) is dense — three operations, three pairwise duals, four mechanism prior-art adoptions. I expect the prose to be ambitious and possibly to outrun the density a fresh reader could absorb cold.

**Where labels may strain.** The boundary between `derived` and `result` and `derivation` (segment type) is structurally meaningful in FORMAT.md but I expect at least one drift case where a substantial `disc-*` segment carries derivation-tier content that should be `derived`. Conversely, some `derivation`-typed Appendix-A segments may be honestly `sketch` or `conditional` given the gating premises.

**Where the OUTLINE may have a backward-pointer.** I expect at least one `depends:` entry that points downstream of the segment's OUTLINE position (excluding the Appendix-A back-pointer exception). Most likely culprit: the Meta-Architecture I chapter introducing M1/M2/M3 may depend on Section II results that are introduced after the meta-chapter. The OUTLINE explicitly opens Part II with Meta-Architecture I *before* the content chapters; that ordering is suspicious because meta-segments are usually written *after* the concrete content they meta-summarize.

**Where novelty claims may be miscalibrated.** Per MEMORY.md May-21 (math-novelty-recognition correction), LLM auditors deflate novelty claims out of trained anxiety. I should *not* do that. But the symmetric failure mode — inflating novelty claims — is also real. I expect at least one segment whose Findings block claims `novelty` where the more honest posture is `differentiation` or `recognition`, and at least one where the posture is honestly `novelty` but reads more cautiously.

---

## Predictions — prose-coherence and continuity (Joseph's named focus)

1. **"AAD" leakage.** The 2026-05-15 AAT-rename was global in segment paths but the `audits/`, `LOG.md`, `msc/`, `_obs/` archaeology is preserved verbatim. I expect to find at least one segment body where "AAD" survives in prose (rather than just in dated archaeology) — most likely in a Discussion or Working Notes block.

2. **GUC class numbering drift around the May-9 reversal.** Pre-May-9 cycles used Class 2 = Coupled. The migration was supposed to be global but I expect at least one stranded "Class 2" or "Class 3" reference in segment prose that refers to the *historical* numbering. Working Notes blocks especially.

3. **"this is not a weakening" ghost.** Per MEMORY.md May-16, this phrasing is a body-signal that a soft-deletion ghost lives in the segment. I expect to find at least one segment whose body or Findings block contains a "sharper, not weaker" or "not a weakening" defensive marker — should be in CHANGELOG/Working-Notes, not body.

4. **Sub-scope $\alpha$/$\beta$/$\alpha'/\beta'$ confusions.** Multiple segments reference these. Joseph said NOTATION.md is lagging; I expect at least one segment to use a sub-scope label inconsistently with its sibling segments.

5. **C1/C2/C3 convention hierarchy referenced in segments before introduction.** The convention hierarchy lives in `#def-value-object`. I expect at least one downstream segment to reference C1/C2/C3 without ensuring the convention is read-in-order accessible.

6. **Chapter-intro draft segments without final-quality prose.** Multiple `--GAP--` markers in Strategy Dynamics, Orient Cascade, Composition Machinery, Unity Communication, Strategic Composition. These will read as discontinuities; whether they're authentic gaps or a labeling artifact is the question.

7. **The Layer-0 Appendices preamble paragraph naming five constructive-impossibility instances.** That's a paragraph at the appendix gate. If it has drifted from the canonical text inside the named segments (#disc-constructive-impossibility-posture, the five instance segments), readers will get a stale catalog. High-leverage check.

8. **The "introduced-before-used" claim about Meta-Architecture placement.** Project CLAUDE.md (line ~91) says the two-cluster Part-opening placement obeys *introduced-before-used* — readers walking Part II encounter the spine + facets at Part II's opening before any Part II content chapter. I should verify this empirically. If even one Part II content chapter references an M1-M4 facet without the meta-chapter having introduced the *operational* meaning yet, the claim is overclaimed.

---

## Predictions — math-correctness (Joseph's named focus)

1. **`#example-kalman` and `#example-bandit`** worked examples. Joseph's protocol explicitly recommends recomputing worked examples (§5.1, §3.3). I should at minimum trace the Kalman example's gain-update arithmetic and the bandit example's regret-bound.

2. **`#deriv-matrix-persistence-condition`'s counterexample claim** — explicit $2\times 2$ counterexample with $\mathcal{T} = \begin{psmallmatrix}1&-0.9\\-0.9&1\end{psmallmatrix}$, $\Sigma_w = I$, claimed: per-coordinate says PASS but matrix-Loewner says FAIL along $(1,1)/\sqrt 2$. This is a numerical claim that should be computable directly. High-leverage check.

3. **`#deriv-stochastic-non-exit`** Model-S no-go. The claim is that the natural Ville/Doob route provably cannot exist because the only compensated supermartingale candidate is sign-indefinite inside the persistence basin. This is a structural-impossibility claim with a specific failure mode named; the body should walk the candidate construction and show why it fails. Math is verifiable in principle.

4. **`#result-persistence-condition`** scalar version $\alpha > \rho/R$ — needs dimensional check (NOTATION already warns about this) and a verification that the linear-ODE-to-sector-condition lift is faithful.

5. **`#deriv-strategic-persistence-hard-ceiling`** Prop C.1 and C.2 — $\alpha_\Sigma^{ss} = (1-\lambda)/(2-\lambda)$ exact under Beta-Bernoulli + exponential forgetting, with sup = $1/2$ at $\lambda \to 0^+$. This is a calculus claim that's directly verifiable.

6. **`#deriv-self-actuation-grounding`** Lemma 1 (convention-monotonicity, static-pointwise) colliding with Lemma 2 (finite-no-oracle per-step commitment). The premise structure matters — three named premises are claimed in the OUTLINE description. I should check that all three are actually used by the derivation rather than over-counted.

7. **Pinsker's inequality use in `#deriv-variational-sector-condition`** — the claim that $O(\sqrt\varepsilon)$ degradation of the sector constant follows from KL$\leq\varepsilon$ via Pinsker. The deflation prediction here is "trust Pinsker"; the inflation prediction is "they used Bretagnolle-Huber instead but didn't say so." Spot-check.

8. **`#der-architecture-noidentifiability`** — the claim that two AAT agents whose linearized closed-loop residual dynamics are minimal realizations related by an invertible similarity transformation produce identical on-policy summary statistics. This is a Kalman-Ho-style claim that should hold; the question is whether the linearization is needed (i.e., whether the nonlinear case also holds).

---

## Predictions — what I'd expect novel and consequential

**The big bets the framework is making.** Distilling from the OUTLINE preambles and the Layer-0 paragraph:

- The **stability-certificate spine** organizing four meta-patterns (M1-M4) as facets of a single equilibrium-stability scaffold. If this organization holds, it's a structural simplification — many AAT results that previously read as scattered are seen as facets of one object.
- The **directed-separation architectural classification** (Class 1 / 2 / 3) lifted from a scalar coupling parameter to an architectural property — this is the spine of how AAT distinguishes Kalman-LQR from LLMs from partial-modular RL. If the classification is structurally sound, it's a genuine organizing move; if `κ_processing` doesn't decompose cleanly, the trichotomy is leakier than presented.
- The **wrapping construction** showing how to coerce Class 3 to Class 1 at the wrapper level. This is the framework's most concrete constructive contribution. The W₀/W₂/W₁ regime hierarchy with the leakage analysis is the load-bearing piece.
- The **constructive-impossibility posture** — five instances of "name the floor, name the escape, treat the no-go as apparatus." If five honestly fit, that's a real style claim; if some are reach-instances, the posture overclaims.
- The **Persistence condition $\alpha > \rho/R$ as cross-domain instantiable** — Kalman / RL / organizational / software all using the same inequality with different parameter readings. This is a synthesis claim and its strength depends on the worked examples in Appendices B.

---

## Predictions — kinds of findings

- **Cross-segment drift** around the M4 landing (May 24) and Track C placement (May 26).
- **Status-label / equation-tag mismatches** in segments that landed recently, especially `der-*` segments whose underlying lemmas are still gated.
- **Soft-deletion ghosts** of integration-is-replacement violations.
- **Math errors in worked examples** — most likely arithmetic / sign / dimensional in `example-*` or in newer derivation segments.
- **OUTLINE-row backward pointers** — at least one, most likely involving Meta-Architecture I depending on Section II content.
- **Unicode-in-backticks math** somewhere — `bin/lint-md` doesn't catch it.
- **Stale forward references** from old segments to terminology Track C changed.
- **`AAD`-as-prose leakage** somewhere outside dated archaeology.

I'll update predictions if 4.5's strategic-loop revision fires before substantial walk-through.

---

## Running outline for FINAL (placeholder)

Section A: scope + bleed disclosure.
Section B: findings under burden of proof (TBD).
Section B.1: rescinded candidates (TBD).
Section C: coverage statement — what was read first-hand vs what was skipped.
Section D: hypothesis-tier observations (TBD).
Section E: what holds (TBD — keep an active list as I read).
Section F: bigger-picture observations (TBD).
Section G: process feedback (TBD — note anything about the protocol itself that surfaced).

---

*Next: begin OUTLINE walk at Part I Chapter 1: `#def-agent-environment`.*
