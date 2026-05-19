# 98 — Review and convergence (history layer)

*This file is the **history layer** for the continuity-persistence spike, per integration-is-replacement. The corrected statements live in the bodies (`00`–`04`, `99`); the record of **what was wrong, who caught it, and what changed** lives only here (and CHANGELOG, when this lands). It exists so the correction trail is not lost and is not smuggled into segment bodies as "this is not a weakening" defensiveness.*

**Date**: 2026-05-18. **Inputs**: independent review (general-purpose agent, opus, full tools, did not write the spike) + the independent accumulation-type meta-spike `spikes/spike-accumulation-type-confound.md`.

---

## 1. Independent review — verdict and what it caught

The reviewer attested the spine — the central unification (the static rate-distortion floor *is* the sector-persistence disturbance term under the turnover-index projection), T1's no-go, the self-replay refutation, P1's logic, P2, T2.1/2.2/2′ — as sound and the tiering *mostly* honest. It found, and I checked and concede, two real over-tierings at load-bearing points plus correct scope caveats:

| Finding | Status | Correction applied |
|---|---|---|
| **Theorem 2.3 ($\mu=0$) overclaimed + mis-cited.** Draft said "$g_k\to\infty$ a.s., null-recurrent, identity death in the limit" and cited Chung–Fuchs (i.i.d.) under the (C-S) stationary-ergodic hypothesis. A null-recurrent reflected walk does **not** converge to death a.s. — it has no finite stationary law but returns near full sufficiency i.o. | **Conceded — real error.** | `03` Theorem 2.3 rewritten: $\mu=0$ ⇒ **no finite stationary law** (Atkinson 1976, (C-S)-general) ⇒ non-persistence; the null-recurrence picture scoped to **i.i.d. only** (Chung–Fuchs). "Death in the limit" withdrawn everywhere; genuine death-in-the-limit relocated to its true home (state-dependent absorbing barrier, T3/`04`). C-DMP's strict-`<` correction **survives and is cleaner**. |
| **Bounded denominator $D$ asserted in body-voice** while its justification (continuant kernel) was parked in an honest-edge. $I(\mathcal C;Y)\le H(Y)$ is the *discrete* bound; false for the continuous graded $[0,1]^5$ relevance vector. | **Conceded — and strengthened, not tiered down.** | `00`/`01`/`02`/`03`: distortion-parameterized $D_\Delta\le\log N(\Delta)\lt\infty$ (explicit $\Delta$-grid quantizer, $k$-independent), **inherited from the static floor's own rate-distortion parameterization**. (E1) demoted from exactness-gate to interpretive identification. Strictly more faithful to the projection thesis. |
| P1 "unique" silently assumed frozen weights | Conceded | `02`§1: (FW) made explicit; fine-tuning named as a *second* (slow, coarse) channel — a sharpening (exactly two channels), not a hidden caveat. |
| D2 "$\Pr[T\lt\infty]=1$, theorematic" overshoots (ISO) alone | Conceded | `04`§3: certain absorption now carries Cor 1's recurring-sub-$D_\Delta$ hypothesis; stated as realistic, not as following from (ISO) alone. |
| Additive-Lindley form is *the* load-bearing modelling commitment, under-named | Conceded | `03`§1: named **(M-ADD)** at the prominence the canon gives channel-independence; non-additive generalization flagged open. |
| `#scope-agent-identity` already owns the "continuity persistence" LEXICON sense; "no formal content until now" too bald | Conceded | `00`§2, `03`§3: reframed as scope ↔ rate (complementary); positions against `#scope-agent-identity` explicitly. |
| The $\eta$ symbol collision is a *trap* (resembles `#result-persistence-condition` line-61 per-dim persistence inequality), not cosmetic | Conceded | `03`§5, `04`§4: elevated to landing precondition decided upstream. |

The reviewer also blocked, correctly, the `#disc-m-preservation` *replacement* until T2.3 is in corrected form (replacing a soft-true sketch with a sharp-wrong claim is the precise failure integration-is-replacement prevents). `99`§6 now gates the replacement on the corrected T2.3.

**What the review did not find / explicitly did not verify:** it accepted T1 as exact, P2's tier as honest, and the substrate-asymmetry orthogonality as correct; it did **not** independently re-verify the meta-spike's canon-instance claims (b/d/f) — those remain to be spot-checked before M5 lands (primary-source-verification), not delegated.

## 2. The accumulation-type convergence — precisely what is and is not independent

`spikes/spike-accumulation-type-confound.md` (independent investigation, same day, originating from the $\varepsilon^\ast(N)$ whole-space pass) restates `#result-sector-persistence-template` as exactly an accumulation-operator boundedness theorem $\lVert\mathcal A\rVert_{\partial\to\Sigma}=\nu/\alpha$ — the **same move** this spike's `00`§2/`03`§3 makes ("the static floor *is* the disturbance term"). Three independent investigations performing the identical $\partial\to\mathcal A\to\Sigma$ re-typing is, by the project's convergence-as-coherence methodology, strong evidence the pattern (M5) is in the framework. **That convergence is genuine and independent** — it is the decisive evidence for the M5 register question and for the shared-upstream land-order (`99`§6).

**The sharp distinction that must not be blurred:** the meta-spike's instance (g) cites *this* spike's C-DMP and inherited the *draft's* boundary error ("null-recurrent (identity death in the limit)"). So:

- **Independent and corroborated (strong):** the recognition that C-DMP is a $\partial/\Sigma$ typing confound, and the template-as-$\mathcal A$-boundedness restatement. Genuinely arrived at from a different starting point.
- **Not independent, and was wrong:** the specific characterization "identity death in the limit." The meta-spike trusted this spike's draft conclusion-prose; it is the *same* error, not a second confirmation. Corrected here and (by breadcrumb) there.

This is itself a sharpening of the meta-spike's own thesis and near its open falsifier (§9): this spike *named* $\mathcal A$ (wrote the Lindley/Loynes recursion explicitly) and **still** got the $\mu=0$ boundary wrong; carrying the $\partial/\Sigma$ type catches gross mistypes but does **not** by itself protect the *within-$\Sigma$ asymptotic classification of $\mathcal A$* (the boundary recurrence behaviour). That refines the meta-spike's C1 (notational invisibility) — naming the operator is necessary but not sufficient; its boundary classification is a further layer the discipline must require *reading*, not just *marking* — and it strengthens, not weakens, the M5-not-hygiene argument.

## 3. Breadcrumb left in the meta-spike

A dated correction note was added to `spikes/spike-accumulation-type-confound.md` at instance (g) and §9 (the only minimal, attributed touch — not a rewrite of its thesis, which is not mine to edit): flags that instance (g)'s "(identity death in the limit)" inherited this spike's draft error, is corrected to "no finite stationary law / non-persistence (genuine death-in-the-limit is the state-dependent T3 barrier, not the $\mu=0$ boundary)," and that (g) **survives as a valid $\partial/\Sigma$ instance** regardless (the *typing diagnosis* is correct independently of the boundary characterization). The §9 down-staking of the unverified instance (c) — which leaned on (g) being "a confirmed stronger instance" — is annotated to note (g)'s characterization was corrected (the typing point stands; the "stronger instance" rhetoric should be read as "another $\partial/\Sigma$ instance," not "an independently-confirmed boundary result").

## 4. Net

Spine intact; two load-bearing over-tierings corrected (one became a strengthening, not a softening); scope caveats applied; convergence stated at its true strength (the typing move, independent and strong) and not beyond it (the boundary characterization, shared-source and corrected). The spike is now safe for practica and for the landing decisions to build on. Re-attestation by the same independent reviewer, on this corrected trail, is the recommended next verification step (`99`§7).
