# RG-0 Verdict: Synthesis and Decision

**Status**: complete — RG-0a, RG-0b, RG-0c all in.
**Date**: 2026-05-09 (revised same day, twice — once for framing correction, once for RG-0c integration)
**Inputs**: `00-brief.md`, `01-rg-0a-two-kalman-Kc-extension.md`, `01b-rg-0a-iterated-coarse-graining.md`, `02-prior-art-rg-ib-fep.md`.

**Framing note (added on revision).** The first draft of this verdict drifted into "is this novel? then drop" reasoning. That's the wrong frame for ASF. The project's prior-art-integration discipline (CLAUDE.md §Prior art integration) is explicit: *"AAT's contribution is integration, not invention. The individual pieces are mostly known; the synthesis is the contribution."* What we're testing is whether the RG framing is *clean theory and useful unification* — independent of whether AAT got there first. The corrected verdict adopts the framing on those terms.

---

## 1. The decision faced

The brief (`00-brief.md` §6) sets two adoption criteria. Use the RG framing as an organizing lens (proceed to RG-1..4 in some form) if the framing is coherent and useful for unifying existing material. Drop the framing only if the test fails to support its core claims *or* if it would not add clarity beyond what already exists in AAT's segments.

Read in the *clean theory and unification* frame, the relevant questions are:

(a) Does the framing's core claim — AAT-shape preserved under coarse-graining — actually hold? (Not: is this novel.)
(b) Does the framing unify previously-separate pieces of AAT (temporal nesting + composite formation + directed-separation classification + (O, Σ) decomposition) into one structural picture?
(c) Are the prior frameworks AAT adopts from named clearly enough that someone reading the AAT treatment can pick up where Friston / Mehta-Schwab / Kline-Palmer / Chen-Goldenfeld-Oono left off?

## 2. Where each thread stands

### 2.1 RG-0a — does the math support the framing?

Closed-form derivation in `01-rg-0a-two-kalman-Kc-extension.md` §2 + `01b` iterated analysis:

- **Form preservation under $\Lambda$**: ✓ holds. The AAT-Kalman shape is preserved at every level of iterated coarse-graining. (A1)–(A4) are honored at the macro level by construction in the linear-Kalman case. **This is the core claim and it survives.**
- **Heterogeneous Kalman flows to ε* = 0** at rate $(1 - K_\text{min}^*)^{K_c}$. Sufficient timescale separation absorbs structural sub-agent heterogeneity. The mechanism is clean: residual error lives in the projection's null space, which the macro-update structurally cannot access; that null-space contribution shrinks with $K_c$ as the slower filter's memory of the previous macro-boundary state decays.
- **Iterated parameter flow**: $\lambda \to \lambda^{K_c}$, monotone toward $\lambda = 0$ (memoryless / saturated-gain limit). No non-trivial scale-invariant fixed point in the linear-Kalman case.

What this *clarifies*: AAT's RG analog is **structural-RG** (the form is preserved across scales) rather than **critical-RG** (the parameters sit at critical points). This matches the IB-RG literature (Mehta-Schwab 2014 / Kline-Palmer 2022 — both structural), the FEP-RG literature (Friston 2019 *JTB* / Friston 2025 RGM — both structural), and the Schwab-deep-learning correspondence (structural). It is honest scope.

The brief's first-cut prediction — that heterogeneity would be a *relevant* operator under the flow — was overconfident. Heterogeneity is an irrelevant operator in the simple case tested. This isn't a fatal problem for the framing; it's a refinement of what kind of RG analog AAT has.

**Verdict on (a)**: ✓ Form-preservation holds; structural-RG reading supported; critical-RG language was overreach and is dropped.

### 2.2 RG-0b — does the framing unify cleanly with prior art?

Per `02-prior-art-rg-ib-fep.md`, the framing has substantial prior-art ancestry:

- **Friston 2019 *J. Theor. Biol.*** — *"a working definition of renormalization rests on... a requirement that the operation does not change the functional form of the Lagrangian."* The form-preservation move for FEP, six years earlier.
- **Friston et al. 2025 RGM** — *"The renormalization group requires that the functional form of the dynamics is conserved over levels or scales."* Develops "renormalising generative models" by construction. Explicit treatment of temporal-scale separation under coarse-graining (mirrors AAT's $\nu_{n+1} \ll \nu_n$ and $K_c$).
- **Mehta-Schwab 2014, Kline-Palmer 2022** — IB-as-RG. Kline-Palmer gives the cleanest semigroup composition rule for IB, which is the form-preservation theorem for an information-theoretic Lagrangian.
- **Chen-Goldenfeld-Oono 1996** — RG identification with singular-perturbation theory (Tikhonov, multiple-scales, slow-manifold reduction).
- **Kirchhoff 2018** — recursive Markov-blanket nesting.

Within this established frame, AAT's contributions take a synthesis form (per project conventions):

1. **Closure-defect bridge lemma as control-theoretic flow-distance bound.** The FEP-RG literature gives form-preservation; the MDP-homomorphism literature (Tabuada-Pappas, Ravindran-Barto, Abel, Subramanian, Congeduti) gives control-theoretic predictive-loss bounds. AAT's bridge lemma sits at the intersection — a *form-preservation distance bound stated as control-theoretic predictive loss*.

2. **Directed-separation classification as graded fixed-point types.** Friston's RG framing treats sparse-coupling as binary (system is renormalizable iff sparsely coupled). AAT's modular / partially modular / fully merged classification (Class 1 / 2 / 3) is the graded refinement. The Class 1 case sits at the form-preserved fixed point; Class 3 (LLMs / goal-conditioned agents) does not. *Conditional on Class-3 closure-defect analysis*, this becomes the order-parameter view.

3. ~~**(O, Σ) recursion against a typed strategy DAG.**~~ **Demoted by RG-0c V2** to "structural observation that is constructible as typed options/MAXQ." The split survives recursion (differentiating from FEP-RG) but degenerately. Not load-bearing AAT-distinctive content; if mentioned, mention as integration with options/MAXQ literature, not as invention.

4. **The persistence template as the per-scale form-preservation invariant.** `#result-sector-persistence-template` already says "applies at every level the template applies to." Reading this as the structural-RG-form-preservation statement — that the same Lyapunov inequality is the invariant under $\Lambda$ — clarifies *why* the template applies at every level rather than treating it as a coincidence across six instantiations.

**Verdict on (b)**: ✓ The framing unifies cleanly. Temporal nesting (`#der-temporal-nesting`) becomes the time-axis projection of structural-RG depth. Composite formation (`#form-composition-closure`) becomes spatial coarse-graining. The persistence template's "applies at every level" becomes the form-preservation statement. Directed-separation classes become the graded form-preservation classification. The (O, Σ) recursion is *not* the strategy-side form-preservation — RG-0c determined that lifting it to a formal structure produces typed-options/MAXQ, which is integration content (worth citing if developed) rather than load-bearing.

### 2.3 RG-0c — (O, Σ) recursion check

(c) **Returned: V2.** Per `03-rg-0c-strategy-recursion.md`, the naive (O, Σ) recursion is *explicitly forbidden* by the segments as written. `#def-strategy-dag` says verbatim: *"$O_t$ itself lives outside $\Sigma_t$; the terminal conditions are $\Sigma_t$'s internal encoding of what $O_t$ requires."* `#def-strategy-dimension` flags conflation of O and Σ as *"a type error"* AAT was built to fix. Recursing the (O, Σ) split at sub-levels reintroduces that type error.

The strengthening attempt (per project discipline): lift each internal node to a tuple $(O'_v, \Sigma'_v, M'_v)$ with indicator-functional $V_{O'_v}(\tau) = \mathbb{1}[C_v(\tau)]$. This *makes the recursion formal* — (R1)–(R3) all satisfiable — but degenerate:
- The diagnostic apparatus collapses to Boolean at sub-levels.
- The attainability $A_{O'_v}$ collapses to the propagated $s_v$.
- The temporal-nesting connection the brief wanted does not transfer through this extension.
- The resulting structure is a **typed version of options / MAXQ** — integration content, not invention content (Sutton-Precup-Singh 1999, Dietterich 2000, Ravindran-Barto 2004, Abel et al. 2020).

The split between O and Σ does survive recursion (differentiating from FEP-RG where free energy plays both roles), but in a degenerate indicator-functional form whose operational content lives only at the agent root.

**Verdict on (c)**: V2. The (O, Σ) recursion is the *weakest* of the three remaining AAT-distinctive synthesis candidates. Not load-bearing.

## 3. The honest synthesis

### 3.1 What survives

**The structural-RG framing as a unifying lens for AAT.** Form-preservation under coarse-graining (a) explains why (A1)–(A4) demand what they demand, (b) gives the persistence template's "applies at every level" claim a structural ground, (c) collapses temporal nesting and composite formation into one operation viewed from different axes, (d) clarifies that directed-separation classes are *form-preservation classes*, and (e) — pending RG-0c — gives the (O, Σ) decomposition a recursive reading.

The framing does *all five* of these without claiming first-mover novelty. It adopts the FEP-RG / IB-RG / singular-perturbation-RG infrastructure cleanly, with citations. AAT-specific synthesis content is the bridge lemma in flow-distance language, the graded directed-separation classification, and (O, Σ) recursion (pending).

### 3.2 What was overclaim

The first-cut framing's *strong-form* version (RG with non-trivial scale-invariant fixed points, critical exponents, β-functions) is not warranted by the linear-Kalman test. The brief's "irrelevant/relevant operator separation" prediction was overconfident; heterogeneity is irrelevant under $K_c$-flow on this case. The corrected framing is structural-RG, in line with FEP-RG and IB-RG, and that's enough.

### 3.3 What clarification this gives existing AAT content

Several existing pieces become legibly *one structure* under the framing:

| Existing piece | Reading under structural-RG framing |
|---|---|
| `#disc-composition-consistency` | Form-preservation postulate: AAT shape is invariant under $\Lambda$. |
| (A1)–(A4) of `#form-composition-closure` | Form-preservation conditions: macro must itself be AAT. |
| `#result-sector-persistence-template` | The per-scale form-preservation invariant — same Lyapunov inequality at every level. |
| `#der-temporal-nesting` | Time-axis projection of structural-RG depth; the 5-level table is the depth hierarchy. |
| Closure-defect ε* | Distance from the form-preserved ideal at the chosen scale. |
| Bridge lemma | Control-theoretic flow-distance bound on this distance. |
| Directed-separation classes | Form-preservation classes: Class 1 preserves AAT-shape under $\Lambda$, Class 3 does not. (Pending Class-3 closure-defect analysis to land as derived rather than suggestive — Move F.) |
| Hafez meta-machine ($\varepsilon^* = 0$ exactly) | Exact discrete instance: form-preservation is exact for finite-state product automata. |
| Brooks's Law (`#der-tempo-composition`) | Coordination overhead = tempo cost of finite ε* (departure from form-preservation). |

This table itself is the clean-theory-and-unification payoff of the framing. None of these readings overclaim. All adopt established FEP-RG / IB-RG terminology cleanly.

## 4. The decision

### 4.1 Adopt the framing with proper citation

Use structural-RG / form-preservation as the unifying organizational lens for AAT's composition + nesting material. Cite Friston 2019/2025 + IB-RG (Mehta-Schwab, Kline-Palmer) + singular-perturbation-RG (Chen-Goldenfeld-Oono) + recursive-blankets (Kirchhoff 2018) as the substrate; position AAT's content as integration (closure-defect bridge bound, graded directed-separation, (O, Σ) recursion) within that frame.

The framing should appear in:
- Discussion sections of `#disc-composition-consistency` and `#form-composition-closure` — name the form-preservation reading explicitly, cite the substrate work.
- A new meta-segment or appendix that makes the unification table (§3.3) explicit. This is the structural payoff.
- Discussion section of `#result-sector-persistence-template` — name "applies at every level" as the per-scale form-preservation invariant.
- Discussion section of `#der-temporal-nesting` — name the 5-level table as the time-axis projection of structural-RG depth.

### 4.2 Specific moves

**Move A — Adopt-and-cite Friston 2019/2025 in `#disc-composition-consistency` and `#form-composition-closure` Discussion.** Make the form-preservation reading of (A1)–(A4) explicit. Cite the substrate works. **Effort: small. High value.**

**Move B — Promote `#der-multi-timescale-stability` via template-stacking + Tikhonov + Chen-Goldenfeld-Oono.** Stand the N-level stability result on the per-scale form-preservation. The template instantiates at every level; sufficient $K_c$-separation between adjacent levels gives composite stability. **Effort: medium. Closes a known gap.**

**Move C — Two-loop worked example (parametric inner, strategic outer).** Show the form-preservation in a non-Kalman instance: $M_t$ Kalman inner + $\Sigma_t$ Beta-Bernoulli outer with $\nu_\Sigma \ll \nu_M$. Land as worked-example segment. **Effort: medium-large. Closes the "no worked nested-loop instance" gap.**

**Move D — Add a meta-segment naming the unification.** A new `#disc-structural-rg` or appendix that lays out the §3.3 table and routes to the substrate works. This is where the clean-theory-and-unification value lives. **Effort: medium. Centerpiece move.**

**Move E** — ~~(gated on RG-0c V1)~~ **Released — RG-0c returned V2.** Recommendation: **do not write `#deriv-strategy-recursion` as load-bearing AAT-distinctive content.** If the recursion ends up doing operational work in a downstream result (e.g., decomposing the persistence condition along DAG depth, or connecting evidence-starvation rates to nested-tempo separation), then write a `#disc-strategy-recursion-vs-htn` integration segment citing Sutton-Precup-Singh 1999, Dietterich 2000, Ravindran-Barto 2004, Abel et al. 2020 — *not* as a novelty claim. Until then: defer entirely.

**Move F (separate spike)** — Class-3 closure-defect analysis to test the graded-directed-separation reading. Important if we want the order-parameter view to land as derived rather than suggestive. Independent of RG framing per se; could be done as a strengthening of `#hyp-directed-separation-under-composition`.

**Open question worth flagging** (per RG-0c §7.2): is RGM-style scale-free-by-construction (Friston et al. 2025: Dirichlet hyperparameters at each scale, blocking transformations) a better match for AAT's aspirations than the recursive-AAT construction this spike attempted? If yes, that's a structural design move worth considering separately — but it would be adopting RGM rather than developing AAT-distinctive content.

### 4.3 What gets dropped

Only the *overclaim* aspects:

- "AAT as the RG of agency" or similar first-mover-novelty framing.
- "Critical-RG" language (β-functions, critical exponents, fixed-point flow) — not warranted by the linear-Kalman analysis.
- "Relevant/irrelevant operator" classification *as a load-bearing claim* — the linear-Kalman case showed everything is irrelevant, contra the brief's first-cut prediction. Could revisit if a richer case shows different behavior.

The structural-RG / form-preservation reading itself is *not* dropped; it's adopted as a clarifying lens with proper citation.

## 5. Cross-checks against project disciplines

- **Strengthen-before-softening**. Did I attempt to strengthen the framing before softening? Yes — `01b` was the strengthening attempt for the strong-form RG claim, and it failed cleanly (no non-trivial parameter fixed point in linear-Kalman). The order-parameter framing was attempted in `01` and is now flagged as "suggestive, requires Class-3 test." The (O, Σ) recursion is in flight. The form-preservation reading itself didn't need strengthening — the test confirmed it.

- **Prior-art integration discipline**. *"AAT's contribution is integration, not invention."* The revised verdict follows this cleanly — adopt FEP-RG / IB-RG / singular-perturbation-RG as substrate, position AAT's content as the synthesis (control-theoretic bridge bound, graded directed-separation, (O, Σ) recursion). The first draft of this file lost track of this discipline; the revision restores it.

- **Honest epistemic labels**. The structural-RG framing is at "Pattern-leaning-Tested" on the epistemic ladder — form-preservation is verified in the simple case; the unification across existing segments is a structural reading, not a derivation. The AAT-distinctive synthesis content (bridge lemma in flow-distance language, graded directed-separation, (O, Σ) recursion) carries its own per-piece tier labels.

- **Worthiness lens** (CLAUDE.md §How You Review Your Own Work). Is this worthy of future readers? Yes — the framing makes (A1)–(A4) legible as form-preservation rather than as an ad-hoc admissibility checklist; the persistence template's "applies at every level" gets a structural ground; the directed-separation classification gets a clean reading. Clean theory and unification benefits accrue to every future agent reading the segments.

## 6. Final recommendation

**To Joseph**:

The "AAT as RG" framing tested out as **structural-RG / form-preservation, not critical-RG**. The strong-form fixed-point version doesn't hold in the linear-Kalman case; the form-preservation version does, and is mostly inherited from Friston 2019/2025/IB-RG/singular-perturbation-RG. *That's exactly the right shape* given ASF's prior-art-integration discipline.

Recommended path: **Moves A, B, C, D in §4.2** as the immediate work. Move E gated on RG-0c. Move F as a separate spike if the directed-separation order-parameter view is something you want to develop independently of the RG framing. The unification value (§3.3 table) is the centerpiece — a meta-segment or appendix laying out the structural reading of existing AAT content under form-preservation cites the substrate work cleanly and shows what AAT adds.

If RG-0c lands V1 or V2, Move E becomes a clean strategy-DAG-side instance of the form-preservation principle. If it lands V3, drop the (O, Σ) recursion as a load-bearing claim but keep everything else.

**My judgment, revised**: this is a clean unification move with the substrate work properly named. It improves AAT's structural legibility without overclaiming. Worth pursuing.

**Final scoring (after all three of RG-0a, RG-0b, RG-0c are in)**:
- Form-preservation framing → ✓ holds, adopt with Friston 2019/2025/IB-RG/Chen-Goldenfeld-Oono citations.
- Bridge-lemma as flow-distance synthesis → ✓ AAT-distinctive (Move A or its own segment-level work).
- Directed-separation as graded form-preservation classification → ✓ AAT-distinctive *conditional on Move F*.
- (O, Σ) recursion as strategy-side form-preservation → ✗ degenerate / equivalent to typed options-MAXQ; defer entirely (RG-0c V2).

Two of three AAT-distinctive synthesis pillars survive. The third drops cleanly via the project's prior-art-integration discipline (cite, don't claim).

---

## File index (final)

- `00-brief.md` — original framing. Some predictions in it (relevant/irrelevant separation, critical-RG fixed points) are now refined; the form-preservation reading and unification claim are validated.
- `01-rg-0a-two-kalman-Kc-extension.md` — Case B closed form. ε* → 0 under $K_c$-flow at rate $(1-K_\text{min}^*)^{K_c}$.
- `01b-rg-0a-iterated-coarse-graining.md` — parameter flow has only degenerate fixed point in linear Kalman; structural-RG framing supported, critical-RG framing dropped.
- `02-prior-art-rg-ib-fep.md` — V2: substantial prior art on form-preservation (Friston, Mehta-Schwab, Kline-Palmer, Chen-Goldenfeld-Oono); AAT integrates with citation.
- `03-rg-0c-strategy-recursion.md` — V2 returned. Naive (O, Σ) recursion forbidden by `#def-strategy-dag`/`#def-strategy-dimension`; minimal-extension recursion is constructible but degenerate / equivalent to typed options-MAXQ. Not load-bearing.
- `99-verdict.md` — this file. Final.
