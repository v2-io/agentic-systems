# Adjudication: which operator is faithful to `#disc-m-preservation`'s 100%-reset regime — $\mathcal A_D$, $\mathcal A_{\mathrm{refl}}$, or neither alone

*2026-05-19. Independent adjudication. Not canon. Does not edit any segment, any steward spike, any staged edit, or any canon file — the landing is a separate gated step decided with Joseph; this note's only channel is the flagged finding below. Fresh context by design: I did not continue or reuse any prior agent's working state; I read the primary sources listed below in full and re-derived the load-bearing structural claims rather than accepting any artifact's summary of them.*

*Author: independent adjudicator (Opus 4.7, 1M). Requested because three artifacts produced the same day disagree about load-bearing canon and none of their authors can adjudicate without bias.*

---

## 0. Verdict up front

**Landing (ii), with a sharpening that makes it landing (iii) for `#disc-m-preservation` specifically.**

The decisive structural fact, read from `#obs-context-turnover` itself and not from artifact chronology: **`#disc-m-preservation`'s regime and the continuity-`03` $\mathcal A_{\mathrm{refl}}$ regime are two genuinely different objects that the single segment `#disc-m-preservation` currently conflates under one heading.**
They are not "the same object, one normalization" (the staged `der-turnover-information-recursion` claim), and $\mathcal A_D$ does not "supersede" $\mathcal A_{\mathrm{refl}}$ for this segment (the RESULT/Review position).
RECONCILIATION is right that they are two distinct operators neither superseding the other; it is the artifact whose position survives structural scrutiny.

But the consequent is sharper than "reframe and relocate." `#disc-m-preservation` as written is **two regimes wrongly housed in one segment**:

- Its *predictive-sufficiency* content (the externalization-reconstruction adequacy of an LLM's working $M_t$ — "remembers the auth bug", "re-asks for already-provided information", the retrieval/summary/file-state table) is the **$\mathcal A_D$ SDPI-affine** regime. The staged `der-turnover-information-recursion` is **correct mathematics for this** and is faithful to `#obs-context-turnover`'s predictive-sufficiency reading.
- The *strict-$\lt$ / relational-re-grounding / Lindley-Loynes* content (V3's corrected statement) is the **$\mathcal A_{\mathrm{refl}}$ identity-continuity** regime. It is faithful — but to a *different target* (`#def-identity-sufficiency`'s relevance vector, the cohort channel), not to `#disc-m-preservation`'s predictive-sufficiency $S(M)$.

So: the staged `der-turnover-information-recursion` segment is sound and lands as the $\mathcal A_D$ §03.II result.
The staged *modification to `#disc-m-preservation`* is housed against a withdrawn subsumption (the staged `der-turnover-information-recursion` asserts the additive form is "the small-loss linearization" *of* and is *superseded by* the $\mathcal A_D$ recursion, and folds identity-sufficiency in as "one normalization of the same object") and the cross-reference must be reframed.
V3's $\mathcal A_{\mathrm{refl}}$-corrected statement does **not** land as a `#disc-m-preservation` replacement — it lands as its own continuity/identity segment with $\mathcal A_{\mathrm{refl}}$ as its home, exactly as RECONCILIATION §3.3 recommends.

The reason this is (iii)-shaped and not merely (ii): the two are not just "two operators that both instantiate the template."
They have **different state variables, different targets, different boundary structure, and live at opposite ends of the same singular parameter**.
Housing them in one segment was the original category error; the clean landing splits the segment, it does not pick one operator for it.

The rest of this note is the structural argument, done from `#obs-context-turnover` and the established machinery, not from which file is timestamped later.

---

## 1. The decisive question is structural, and `#obs-context-turnover` answers it

The brief states the fork precisely: does `#obs-context-turnover`'s 100%-reset *force* the SDPI-multiplicative $\mathcal A_D$ recursion (making reflected-Lindley a linearization artifact *for this segment*), or are predictive-sufficiency-turnover and identity-continuity two distinct regimes each with its own faithful operator?

I read `#obs-context-turnover` (the actual segment, at `03-llm-core/src/obs-context-turnover.md` — note the brief's path `01-aat-core/src/...` is wrong; the segment lives in Volume III, which is itself mildly load-bearing, see §6).
The structural ground truth is in three places in that segment:

**(a) The boundary is a lossy stochastic reconstruction channel.**
Formal Expression: $X_{\tau_{k+1}} = f_{\mathrm{init}}(\mathcal E_{\mathrm{ext}}, p_{k+1}, M_0^{\mathrm{weights}})$, and the sufficiency-discontinuity bound is written *natively in mutual information*: $\Delta S_{\mathrm{turnover}} \geq 1 - I(M_{\tau_k}^-;\, f_{\mathrm{init}}(\cdot)) / H(M_{\tau_k}^-)$.
The only thing crossing the boundary is the reconstructed state through $f_{\mathrm{init}}$.
This forces the Markov chain $Y \to X_k \to M_{k+1}^+$.
On that chain, "information through a non-degenerate lossy channel contracts by a multiplicative coefficient strictly below one" is the **strong data-processing inequality** (Ahlswede–Gács 1976; Polyanskiy–Wu contraction-coefficient theory) — a *theorem*, not a modeling posit.
I verified the citation is used for what it says: SDPI states exactly that $I(M_{k+1}^+;Y) \leq \eta_k I(X_k;Y)$ with $\eta_k \lt 1$ strictly for a genuinely lossy channel.
This is sound and is `RESULT.md`'s (C1).

**(b) The segment's own voice says "destroyed and reconstructed, not perturbed; not a rate condition."**
Discussion: *"the state is not perturbed, it is destroyed and reconstructed. The relevant question is not $\alpha \gt \rho/R$ but whether the reconstruction is adequate."*
This is the structural fact that kills the `#result-sector-persistence-template` transfer: the template's (T1)–(T3) require a *correction function* $F$ pointing a *persisting, perturbed* state inward (`#result-sector-persistence-template` (T1) $F(0)=0$, (T2) $\xi^T F(\xi) \geq \alpha\lVert\xi\rVert^2$, (T3) bounded disturbance rejected by that correction).
A destroy-and-reconstruct boundary has *no* $F$ and *no* perturbation being rejected.
I verified this against what the template actually requires (read in full): the non-transfer is real.
`RESULT.md` R1's "the sector-persistence template provably does not transfer" is correct, and it is correct *for the predictive-sufficiency reading `#obs-context-turnover` is written in*.

**(c) The target of `#obs-context-turnover` / `#disc-m-preservation` is predictive sufficiency $S(M)$, not identity.**
`#obs-context-turnover` `depends:` on `def-model-sufficiency` (predictive sufficiency of the reality model), not `def-identity-sufficiency`.
`#disc-m-preservation` is titled *"External Memory as Persistent $M_t$"* and `depends:` on `def-model-sufficiency`.
Its entire engineering content — the retrieval/summary/file-state table, "the agent checks whether it remembers key facts", the biological sleep-consolidation analogy — is about an LLM agent's *working reality model* surviving session turnover.
**It is not an identity segment.**
RESULT §6 and Review fix 1 both note this explicitly and correctly: `#disc-m-preservation` "is itself a predictive-sufficiency (not identity) segment."

Putting (a)+(b)+(c) together: **for `#disc-m-preservation`'s own regime — predictive-sufficiency $S(M)$ under a uniformly-lossy reconstruction channel — the SDPI-affine $\mathcal A_D$ recursion is the faithful operator, and the sector-persistence template does not transfer.**
This part of the RESULT/Review position is structurally correct, and I reached it independently from `#obs-context-turnover`, not from the artifact.

So why is this *not* landing (i) ("$\mathcal A_D$ supersedes $\mathcal A_{\mathrm{refl}}$ for this segment")?
Because the question's second half — "is reflected-Lindley a linearization artifact *here*, or a faithful distinct regime?" — has a definite structural answer, and it is the second one.
§2.

---

## 2. The reflected-Lindley structure is not a linearization of the affine recursion — it is a structurally distinct object, and the singularity argument is decisive

The staged `der-turnover-information-recursion` (and `RESULT.md` §5 *before* its withdrawal) asserts: the additive/Lindley form is "the small-loss linearization" of the $\mathcal A_D$ affine recursion ($\eta_k \approx 1 - \delta_k$, additive in $\delta_k$), valid only near the lossless limit; the reflected analysis is therefore *superseded for this segment*.
I checked this on the merits — does the linearization claim actually hold? — and it fails, for the exact reason `verify-A-restatement-model-DS.md` (V1) and RECONCILIATION independently give.
I re-derived it rather than taking either:

**The singularity argument (decisive, re-derived).**
$\mathcal A_D$'s affine recursion $I_{k+1} \leq \eta_k I_k + a_k$ has operator norm controlled by the contraction gap: the `RESULT.md` R2 level is $\bar a/(1-\bar\eta)$, which **diverges as $\bar\eta \to 1$**.
The reflected-Lindley object's *entire load-bearing content* is its $\mu = 0$ boundary (Loynes/Atkinson: no finite stationary law).
In the Lindley walk $g_{k+1} = (g_k + \xi_k)_+$ with $\xi_k = \rho_k - \eta_k$, $\mu = \mathbb E[\xi] = 0$ is the *driftless* case.
The Lindley/affine correspondence maps the contraction modulus to drift: drift $\to 0$ is exactly contraction modulus $\to 1$ is exactly $\mathcal A_D$'s singularity $\lVert\mathcal A_D\rVert \to \infty$.
**You cannot obtain an object whose entire content lives at a parameter value as the linearization of an object whose norm is $+\infty$ at that same parameter value.**
A linearization is a small-perturbation approximation *valid near a regular point*; the $\mu=0$ boundary is not a regular point of $\mathcal A_D$, it is its pole.
The "Lindley is the small-loss linearization" claim inverts the actual relationship: it is precisely *at* the boundary the affine form excludes that the reflected form does its work.

This is not my invention; it is `verify-A-restatement-model-DS.md` §0/§2 (O2, O3) and RECONCILIATION §2, and I re-derived it independently and concur.
It is also corroborated from a second, independent direction: `RESULT.md`'s own honest edge §4-(4) — the (C4) *uniform* $\bar\eta \lt 1$ commitment, with $\eta_k \to 1$ named as "the evasion regime."
That evasion regime *is* $\mu \to 0$ *is* exactly where $\mathcal A_{\mathrm{refl}}$ is load-bearing.
$\mathcal A_D$'s result is, by its own author's honest scoping, weakest precisely where $\mathcal A_{\mathrm{refl}}$ does its work.
Two structurally distinct operators, the boundary between them being the singular point of one and the entire domain of the other.
The O2 homogeneity argument ($R^\ast_D \propto \alpha^{-1}$ vs reflected/Model-S $\propto \alpha^{-1/2}$ — a change of homogeneity *degree*, which no choice of norm on a fixed operator can produce) is the same conclusion from the template side, and I verified it against `#result-sector-persistence-template` line 51 and the Cor-A.1S.1 categorical $\{0,1\}$ dichotomy: it holds.

**Conclusion of §2.**
The reflected-Lindley structure is *not* a linearization artifact.
It is an irreducibly distinct operator.
Therefore landing (i) is **wrong**: $\mathcal A_D$ does not supersede $\mathcal A_{\mathrm{refl}}$.
RESULT §5's withdrawal of the subsumption (and RECONCILIATION's symmetric-dual diagnosis) is structurally correct, *not* an over-correction.
The artifact that withdrew the subsumption was right to withdraw it, and right for the reason it gave.

This already settles "(i) vs (ii)/(iii)" in favor of not-(i).
The remaining work is the consequent: what does `#disc-m-preservation` correctly become, and where does V3's statement land.
That is where the picture is sharper than a binary.

---

## 3. Why this is landing (iii)-shaped: the two operators have different targets, not just different regimes of one target

Landing (ii) as the brief frames it says: two distinct operators, each faithful in its regime, and V3's $\mathcal A_{\mathrm{refl}}$ statement lands as a *distinct continuity-persistence segment*.
That is correct as far as it goes.
But there is a structural fact that makes the split sharper than "same question, two regimes," and getting it right matters for *where exactly* V3 lands and *what exactly `#disc-m-preservation` becomes*:

**$\mathcal A_D$ and $\mathcal A_{\mathrm{refl}}$ here are not two regimes of one walk — they are walks on two different state variables tracking two different targets.**

- $\mathcal A_D$ (the `der-turnover-information-recursion` / `RESULT.md` object) is a walk on $I_k = I(M_k^+; Y)$ where $Y$ is the **predictive-sufficiency target** (`#disc-m-preservation`'s `def-model-sufficiency` — future observations, the reality model's adequacy). Its boundary structure: $S_{\min}$ is a *readout line* (operationally-dead threshold), explicitly **not** a reflecting or absorbing barrier in the dynamics (`RESULT.md` (C2) is emphatic about this). The walk lives on $[0, H_\Delta]$, decays geometrically with no reinjection, no reflection.

- $\mathcal A_{\mathrm{refl}}$ (the continuity-`03` object) is a walk on the **identity gap** $g_k = I(\mathcal C_{\tau_k}; Y \mid M_{\tau_k}^+) = D_\Delta - I(M_{\tau_k}^+; Y)$ where $Y$ is the **identity-relevance vector** (`#def-identity-sufficiency`'s $[0,1]^5$ continuant kernel — cohort, witnesses, the relational joint space). Its boundary structure is the *whole point*: the reflection $(\cdot)_+$ is load-bearing (continuity `02`-Lemma-1: self-replay cannot push the gap below what the *relational channel* restores; the gap floors at 0 = full sufficiency), and the $\mu=0$ Loynes/Atkinson boundary *is* the result. The compensation term is **relational re-grounding specifically** (continuity `02`-Prop-1: generic task-learning has zero weight), an external cohort channel with no counterpart in $\mathcal A_D$'s predictive-sufficiency reinjection (which is "fresh $Y$-information in the end-of-session content", a generic conditional-MI quantity).

These are not the same dynamical object viewed in two normalizations.
The staged `der-turnover-information-recursion` §"Setup" claims $S_{\mathrm{id}} = I_k / I(\mathcal C;Y)$ is "one normalization of $I_k$, not a distinct dynamical object" — and *for the predictive-sufficiency $Y$ it is built on*, that is true (it is a readout).
But continuity-`03`'s $\mathcal A_{\mathrm{refl}}$ is **not a normalization of `der-turnover`'s $I_k$** — it is a walk on a *different $Y$* (identity-relevance, relational joint space) with a *structurally different operator* (reflected, relationally-compensated, boundary-load-bearing).
The staged segment's "identity-sufficiency is one normalization of the same object" is precisely the residue of the withdrawn subsumption: it absorbs the identity regime into the predictive regime by treating the *target* as a normalization choice when it is a different target with a different compensation channel and a different boundary.

This is why the consequent is (iii)-shaped: **`#disc-m-preservation` currently houses (or, post-staging, is being made to house) two different targets' dynamics under one heading.**
The clean landing is not "pick $\mathcal A_D$ for `#disc-m-preservation` and put $\mathcal A_{\mathrm{refl}}$ elsewhere as a sibling instantiation of the same question."
It is: `#disc-m-preservation`'s *own* regime (predictive sufficiency) is the $\mathcal A_D$ regime — that part of the staged work is correct and lands — and the identity-continuity regime is a *different segment about a different thing* (it was always a Volume-IV-flavored identity question; the original cross-volume mis-frame, which `RESULT.md` §6 and the continuity `99` superseded-warning both diagnose, is exactly this conflation).
V3's statement is faithful, but faithful to identity-continuity, and it lands there.

---

## 4. The three artifacts, adjudicated against the structure (not against each other's timestamps)

The brief is explicit that chronology is not the criterion.
Here is each artifact judged against §§1–3:

- **V3 (`verify-cdmp-corrected-statement.md`)** — its *mathematical content* (strict-$\lt$; relational-re-grounding attribution; explicit Lindley structure; conditional-with-exact-core tier carrying (M-ADD)/(M-FREE)/(C-S)) is **sound and primary-source-verified** against continuity `03`/`98`, which I re-checked. Its *error* is one of placement, inherited from the brief it was given: it frames itself as supplying "the corrected `#disc-m-preservation` accumulation condition." It is not that. It is the corrected **identity-continuity** statement ($\mathcal A_{\mathrm{refl}}$ regime, `def-identity-sufficiency` target). V3's content survives intact; V3's *target attribution* (that this replaces `#disc-m-preservation`) does not. This is consistent with V3's own §2 hard-precondition list and its honesty about tiers — V3 did the verification correctly; the segment-identity question was outside its mandate and it did not claim to settle it.

- **`RESULT.md` + embedded Review** — the no-go, the non-transfer, the SDPI faithfulness, and the affine recursion are **structurally correct for the predictive-sufficiency regime** (§1). The Review's verdict that "(C1) SDPI multiplicative contraction is faithful, not a forced-elegant frame" is correct and I concur on independent re-derivation. The Review's *one structural over-reach* is the sentence: *"the earlier incarnation's Lindley/Loynes 'sharp threshold' ... was exactly the rate-shaped artifact ... the affine-recursion reframe correctly identifies it as the small-loss linearization and removes it"* and *"the two are mutually exclusive readings of the same segment; the new one is what lands."* That is landing (i), and §2 shows it is structurally false: Lindley/Loynes is not the linearization of the affine form (you cannot linearize across a pole), and the two are not "the same segment" — they are two targets. The Review was correct about everything it independently re-derived (the math holds, SDPI is faithful, the non-transfer is sound); it was wrong on the *one* claim it took on trust from the spike's own framing rather than re-deriving — the subsumption. This is itself an instance of the accumulation-type confound's $\mathcal R$-erasure pattern (treating the contraction-interior reading as the whole story when the boundary regime is a structurally distinct object), which `spike-accumulation-type-confound.md` §6.6 and `verify-A-restatement-model-DS.md` independently caught from two other directions — three independent arrivals at the same structural recognition, which by the project's convergence-as-evidence methodology is strong evidence the split is in the framework, not in any one analysis.

- **`RECONCILIATION.md`** — withdraws the subsumption as "the symmetric dual of the over-unification V1 caught." §2 confirms this is **structurally correct, not an over-correction**: the singularity argument, the homogeneity argument, and the $\mathcal A_D$-weakest-where-$\mathcal A_{\mathrm{refl}}$-works corroboration are all sound and independently re-derivable. RECONCILIATION is the artifact whose position survives. Its one under-specification is at its own §4 ("I am *not* certain... is the $\mathcal A_D$ no-go genuinely new, or subsumed by the existing $\mathcal A_D$ family?") — that is a real open question (§7 below) but it does *not* affect the adjudication: whether $\mathcal A_D$-R1/R2 is new-vs-an-instance-of-the-bridge-lemma is orthogonal to whether $\mathcal A_D \neq \mathcal A_{\mathrm{refl}}$ and to where V3 lands.

The staged edits (`der-turnover-information-recursion.md`, the `#disc-m-preservation` modification) embed the **RESULT/Review (pre-withdrawal) position**, i.e. landing (i).
Per §§2–3 that position is structurally wrong on the subsumption.
The staged `der-turnover-information-recursion` *segment* is salvageable as the $\mathcal A_D$ predictive-sufficiency result with its subsumption claims excised; the staged `#disc-m-preservation` *replacement* must not embed the withdrawn subsumption in canon (see §5 for the precise line-by-line state — it is less wrong than the brief feared, but its cross-reference inherits the subsumption from `der-turnover`).

---

## 5. The consequent, stated precisely (what lands where — flagged finding, not an instruction to execute)

Per the brief, surfacing "this forces X" as a flagged finding is the channel; the landing is gated and decided with Joseph.
The structure forces the following shape:

> **FLAGGED FINDING — F-ADJ-1 (the segment houses two targets; the split is the landing).**
>
> `#disc-m-preservation` is a **predictive-sufficiency** segment (`def-model-sufficiency`, working reality-model survival across LLM session turnover). For *its own regime*, the faithful operator is the **SDPI-affine $\mathcal A_D$ recursion**, and the sector-persistence template provably does not transfer (§1). The staged `der-turnover-information-recursion` is **correct mathematics for this regime** and lands as the §03.II $\mathcal A_D$ segment as `INTEGRATION.md` constraints 1/3/5 specify — *with the three subsumption claims removed*: (a) the "$S_{\mathrm{id}} = I_k/I(\mathcal C;Y)$ is one normalization of the same object" sentence (it conflates a different target — identity — with a normalization of the predictive target; §3); (b) any phrasing that the reflected-Lindley/continuity content is "the small-loss linearization … removed" or "superseded" (§2: it is a structurally distinct operator at $\mathcal A_D$'s singularity, not its linearization); (c) the `der-turnover` "Relationship to #disc-m-preservation" claim "$\#$disc-m-preservation's discussion-grade accumulation section is superseded by the corrected statement here" should read as superseded *for the predictive-sufficiency accumulation question only*, with an explicit pointer that the identity-continuity regime is a distinct operator with its own segment.
>
> The corrected statement in the staged `#disc-m-preservation` body (the "Accumulation across sessions" paragraph + Epistemic Status + Working Notes) is **correct present truth for the predictive-sufficiency regime** and may stand *as the $\mathcal A_D$ content* — it does not embed the subsumption in its own body the way the `der-turnover` Discussion does; its problem is only the missing acknowledgment that identity-continuity is a separate operator/segment, not a normalization. (I checked the staged `#disc-m-preservation` body line-by-line: its accumulation paragraph and Working Notes are $\mathcal A_D$-faithful and do not assert the identity subsumption; the subsumption lives in `der-turnover-information-recursion`'s "Setup" and "Relationship to #disc-m-preservation" sections. So the `#disc-m-preservation` staged edit is *less* wrong than the brief's framing feared — its defect is omission, not embedded falsehood.)
>
> **V3's $\mathcal A_{\mathrm{refl}}$-corrected statement does not land in `#disc-m-preservation`.** It lands as a **distinct identity-continuity segment** ($\mathcal A_{\mathrm{refl}}$ home: reflected Lindley/Loynes, relational re-grounding compensation, the $\mu=0$ boundary, conditional-with-exact-core carrying (M-ADD)/(M-FREE)/(C-S), the $\eta \to \varrho_{\mathrm{rg}}$ rename as hard precondition). Target: `def-identity-sufficiency`, not `def-model-sufficiency`. This is RECONCILIATION §3.3 exactly, and it is the de-confliction of the original cross-volume mis-frame (the continuity `99` superseded-warning and `RESULT.md` §6 both already diagnose that the continuity work was mis-framed as a Volume-IV identity result *housed against* `#disc-m-preservation`; the correct move is not "house it against `#disc-m-preservation` either way" but "it is its own segment about identity, distinct operator, distinct target").
>
> Net: `#disc-m-preservation` becomes the predictive-sufficiency segment whose accumulation question is answered by $\mathcal A_D$ (`der-turnover-information-recursion`); the identity-continuity question becomes its own segment answered by $\mathcal A_{\mathrm{refl}}$ (V3's verified content); the two cross-reference as "distinct operators at opposite ends of the contraction parameter, neither superseding the other" (RECONCILIATION's frame), **not** as "same object, one normalization" (the staged `der-turnover` framing) and **not** as "$\mathcal A_D$ supersedes $\mathcal A_{\mathrm{refl}}$ for this segment" (the RESULT/Review pre-withdrawal framing).

This is landing (ii) on the brief's enumeration, with the (iii) sharpening that the reason it is two segments is that `#disc-m-preservation` was housing two *targets*, not two regimes of one target — which is why "split the segment / they were two regimes wrongly conflated" (brief's (iii)) is the more honest description of the consequent than "reframe and relocate" (brief's (ii)).
I record it as **(ii)-with-(iii)-structure** rather than forcing it into one bin, because the brief explicitly invites a defensible fourth and this is the precise shape.

---

## 6. A secondary structural flag, surfaced because it bears on the landing

> **FLAGGED FINDING — F-ADJ-2 (`#obs-context-turnover` is a Volume III segment; the brief and the natural dependency assumption put it in Volume I).**
>
> The brief states `#obs-context-turnover` is at `01-aat-core/src/obs-context-turnover.md` "the regime's structural ground truth — likely decisive." It is actually at **`03-llm-core/src/obs-context-turnover.md`** (`type: observation`, `status: exact`, `depends:` on `scope-logogenic-agent`, `def-chronica`, `result-persistence-condition`, `def-model-sufficiency` — all Volume-III/I, none Volume IV). This is consistent with the §1/§3 finding: `#obs-context-turnover` and `#disc-m-preservation` are **predictive-sufficiency Volume-III segments**, and the identity-continuity regime (`def-identity-sufficiency`, Volume IV) is genuinely a different volume's concern. This corroborates F-ADJ-1's split from the dependency-graph side: the $\mathcal A_D$ segment is §03.II (Volume III, predictive sufficiency, `INTEGRATION.md` constraint 1 is right to forbid a III→IV `depends:`); the $\mathcal A_{\mathrm{refl}}$ segment is the Volume-IV-flavored identity segment (its natural `depends:` includes `def-identity-sufficiency`, `scope-agent-identity` — Volume IV — exactly as continuity `99` §6's landing recommendation independently arrived at before the RESULT reframe). The two segments live in two volumes because they are about two targets. The dependency graph wants the split for the same reason the operator structure does.

---

## 7. What I am *not* adjudicating, flagged honestly

- **Whether the $\mathcal A_D$ no-go (R1/R2) is genuinely novel or an instance of the existing $\mathcal A_D$ family** (the bridge-lemma resolvent applied to the turnover channel). This is RECONCILIATION §4's open question and it is genuinely open; it does **not** affect this adjudication (it changes whether `der-turnover-information-recursion` is a new segment or a worked instance, not whether $\mathcal A_D \neq \mathcal A_{\mathrm{refl}}$ or where V3 lands). Flagged, not resolved — and explicitly *not* something I assert from structural feel (the trigger to test, not assert).
- **The $\eta \to \varrho_{\mathrm{rg}}$ symbol rename, the M5 register question, the shared-upstream land-order, the (M-ADD)/(M-FREE) tier policy.** All gated decisions (D3/D4, Joseph), all correctly held there by every artifact. Nothing in this adjudication unblocks or pre-empts them; F-ADJ-1 removes a false competitor (the subsumption) and de-conflicts the segment-identity question, which is upstream of those gates, not a substitute for them.
- **`spike-accumulation-type-confound.md`'s F-1/F-2 internal corrections and the (c) check.** Out of scope; I read the spike only to verify the $\mathcal A_D$/$\mathcal A_S$/$\mathcal A_{\mathrm{refl}}$ split it names is structurally sound (it is, and I re-derived the O2/O3 obstructions independently) and that the convergence claim (three independent arrivals at the split) is real (it is: `verify-A-restatement-model-DS.md` from the template side, `RECONCILIATION.md` from the SDPI side, this adjudication from the `#obs-context-turnover`-target side).

---

## 8. One-paragraph summary for the gated landing decision

The decisive structural fact is in `#obs-context-turnover` itself: it is a *predictive-sufficiency* segment whose 100%-reset boundary is a uniformly-lossy stochastic channel, which **forces** the SDPI-affine $\mathcal A_D$ recursion for *its own target* and **forecloses** the sector-persistence-template transfer — that part of RESULT/Review is sound and I re-derived it.
But reflected-Lindley $\mathcal A_{\mathrm{refl}}$ is **not** a small-loss linearization of $\mathcal A_D$: it lives at $\mathcal A_D$'s singularity ($\mu=0$ = contraction-modulus $\to 1$ = $\lVert\mathcal A_D\rVert \to \infty$), you cannot linearize across a pole, and $\mathcal A_D$'s own honest (C4)/§4-(4) evasion-edge concedes it is weakest exactly where $\mathcal A_{\mathrm{refl}}$ is load-bearing.
So landing (i) is structurally wrong; RECONCILIATION's withdrawal of the subsumption is correct and not an over-correction.
The consequent is sharper than a binary: `#disc-m-preservation` was housing **two different targets** — predictive sufficiency (`def-model-sufficiency`, $\mathcal A_D$) and identity continuity (`def-identity-sufficiency`, $\mathcal A_{\mathrm{refl}}$, cohort-relational compensation) — under one heading.
The clean landing is landing (ii) with (iii) structure: `#disc-m-preservation`'s own predictive-sufficiency accumulation question is answered by the $\mathcal A_D$ segment (`der-turnover-information-recursion`, staged content correct *once its three subsumption claims are excised*); V3's verified $\mathcal A_{\mathrm{refl}}$ statement lands as a **distinct identity-continuity segment**, not a `#disc-m-preservation` replacement; the two cross-reference as distinct operators at opposite ends of the contraction parameter, neither superseding the other.
This is RECONCILIATION's recommended frame, reached here independently from the structure of `#obs-context-turnover` and the singularity argument rather than from artifact chronology.
