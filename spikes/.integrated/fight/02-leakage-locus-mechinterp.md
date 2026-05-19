# Connection 2: Why self-play exploit-detection needs mechanistic, not behavioral, access — a floor-theoretic statement

**Thread.** Φ's second paper direction is *mechanistic interpretability of self-play policies* — circuit-level detection of exploit-prone subnetworks, "interpretability as the diagnostic instrument for combat policies." Claim under test: AAT predicts *why* this must be circuit-level rather than behavioral.

> **Loud caveat, stated first.** Connection 2's AAT-side foundation is `spike-leakage-locus-2026-05-18.md` — an exploratory spike dated one day before this one, **not promoted, not landed in any segment**. Everything below inherits that pre-landing status: it is a connection between an external problem-class and an in-flight AAT spike, legitimate as spike-grade ideation, not citable as established AAT.

## 1. The claim, and the naïve version is wrong

Naïve version: "behavioral methods are blind to goal contamination, so use circuits." This is **too coarse and is contradicted by the leakage spike itself** — AAT's *own* answer to "how do you detect goal contamination" is the **behavioral** $\hat\kappa_{\text{processing}}$ estimator (`#der-directed-separation`): present the *same event* under *two distinct goal states*, measure epistemic-content divergence. Behavioral detection is not blind in general. So the naïve framing fails on contact with the source. The real statement is sharper and survives.

## 2. The verified, precise statement

Two results from the primary sources combine into a non-coincidental bridge.

**(a) The leakage-locus structure (from `spike-leakage-locus-2026-05-18.md`, §3–4, tier: exact for lin-Gauss / robust-qual general).** Goal contamination of a goal-blind-data filter moves belief *only* along $\ker\mathcal I_\tau$ — the identifiability null space of the current latent state given the realized event — and is data-irreducible there. Surprise 1 (exact corollary): the contamination is **invisible to the agent's own posterior covariance** (only the mean moves), which is precisely *why* the leakage-detecting estimator must be the cross-goal *counterfactual* $\hat\kappa$ (same event, two goal states) rather than an uncertainty check.

**(b) The leakage locus *is* an identifiability-floor null space (the spike's §1 first connection, made load-bearing by `#disc-identifiability-floor`).** And the floor meta-segment's Sylvester-law finding states the irreducibility sharply: a rank-deficient information operator is rank-deficient in *every* coordinate (congruence preserves inertia); the floor "is escapable only by *rank-augmentation* — adding a genuinely new score component (interventional data, a side channel, a witness) — and **never by reparameterization**."

Now apply this to a **trained self-play policy**, which is what Φ produces:

> **The behavioral estimator's precondition fails for self-play policies.** $\hat\kappa$ requires counterfactual control of the goal state with the situation held fixed — present *the same event* under $G_1$ and $G_2$. For an LLM you can do this (two prompts, two objectives). A trained adversarial self-play policy has **no exposed goal input**: "defeat the opponent" is fixed and baked into the weights; there is no second goal state to present the same physical situation under. The cross-goal counterfactual that makes behavioral leakage detection possible is structurally unavailable. *(Tier: robust-qualitative — this follows from what a self-play policy structurally is, not from a model.)*

> **Therefore the floor's Sylvester clause selects the channel.** Behavioral observation of the policy lives in $\mathrm{range}\,\mathcal I_\tau$ (what behavior identifies); the exploit/contamination lives in $\ker\mathcal I_\tau$ by the Leakage Locus Lemma. With the counterfactual-goal escape gone, *cleverer behavioral metrics are reparameterizations of behavioral data* — and Sylvester's law says reparameterization cannot cross the rank boundary. The blind subspace is escapable **only** by a rank-augmenting measurement channel. Mechanistic (circuit-level) access *is* exactly the floor's "witness / side channel" category — not a reparameterization of behavior. *(Tier: verified bridge — a direct application of the floor segment's recognition-tier Sylvester finding to the self-play case.)*

So AAT does not merely *suggest* Φ's method choice; the identifiability-floor + leakage-locus machinery **derives the category of the required instrument**: for trained self-play policies, exploit-detection is floor-limited behaviorally and escapable only by a rank-augmenting mechanistic channel. Φ's "interpretability as the diagnostic instrument for combat policies" is, in AAT's vocabulary, *rank-augmentation of the information operator where behavioral reparameterization is Sylvester-forbidden.*

## 3. The connection is bidirectional, and it lands on the leakage spike's own open questions

The leakage-locus spike explicitly leaves two author-gated open questions that an adversarial-self-play substrate is *purpose-built* to exercise:

- **Open-Q3 (spike §9):** "this looks like a *mechanism-level* account of strategic self-coupling (the middle M4 operation) — the Leakage Locus would say strategic self-coupling necessarily routes through $\ker\mathcal{I}$." A self-play policy learning to exploit an opponent **is** strategic self-coupling (the M4 middle operation, self-driven modularity decrease that *enables* the exploit). The leakage-locus prediction is therefore concrete and falsifiable on a Φ-Arena-like substrate: *exploit circuits should concentrate in the behaviorally-unidentified subspace* — invisible to behavioral matchup metrics, visible to circuit-level probes targeted at the low-curvature subspace of the posterior precision (the spike's "principled target" for $\hat\kappa$). A built benchmark would test whether M4's middle operation routes through $\ker\mathcal{I}$ as the spike conjectures.
- **Open-Q4 (spike §9):** whether "goal-corruptible subspace" is a new identifiability-floor instance or a re-description of an existing one. Adversarial self-play gives the *empirical* discriminant the analysis alone cannot: if exploit-contamination is data-irreducible in the behaviorally-null subspace exactly as the Lemma predicts, that is evidence it is the floor's structure, not a separate phenomenon.

Value-direction, honest: AAT (the leakage-locus + floor machinery) **predicts** Φ's method-category and makes a **falsifiable prediction** a built Φ-Arena could test; Φ has no result to give AAT. The teaching is that the Φ problem-class is the natural empirical home for two questions the leakage spike already isolated as the open author-decisions — it does not answer them, it shows they are *testable* rather than only arguable.

## 4. Tiers (honest)

| Sub-claim | Tier | Basis |
|---|---|---|
| Naïve "behavioral is blind" framing | **rejected** | contradicted by `#der-directed-separation`'s behavioral $\hat\kappa$ |
| Leakage confined to $\ker\mathcal I_\tau$, invisible to own covariance | **exact (lin-Gauss) / robust-qual** — *inherited, pre-landing* | `spike-leakage-locus-2026-05-18.md` §3–4 (unlanded spike) |
| $\hat\kappa$ counterfactual-goal precondition fails for trained self-play policies | **robust-qualitative** | structural property of self-play policies (no exposed goal input) |
| Mechanistic access = the floor's rank-augmenting channel; behavioral metrics Sylvester-forbidden from escaping | **verified bridge** | direct application of `#disc-identifiability-floor` Sylvester finding (recognition-tier) |
| Φ-Arena could test null-space concentration of exploit circuits / M4-middle routing (leakage spike Open-Q3) | **hypothesis (falsifiable, untested)** | no benchmark exists; the prediction is well-posed |

## 5. Candidate landings — all author-gated, not folded silently

- This thread is **not** a candidate landing on its own; it is downstream of `spike-leakage-locus-2026-05-18.md` resolving first. The leakage spike's own §9 Open-Q3 (reconcile with strategic-self-coupling / M4) and Open-Q4 (new floor instance vs re-description) are the gating author-decisions; this thread's contribution is the observation that **both are empirically posable on an adversarial-embodied substrate**, which is context for those decisions, not a resolution of them.
- If the leakage spike lands its appendix segment, a single Discussion sentence there ("the behaviorally-unidentified leakage subspace is why exploit-detection in goal-baked policies — e.g. adversarial self-play — is escapable only by mechanistic rank-augmentation, not better behavioral metrics") would be the natural cross-reference. Gated on that spike's landing and on Joseph; not executed here.
- No segment edit is made by this spike.
