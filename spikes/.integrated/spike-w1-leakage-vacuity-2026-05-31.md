# Spike: The W₁ leakage bound — vacuity challenge (F127/F128) and the corrected formulation

**Status**: derivation complete. Landing state **(B)** with an embedded **(C)** structural sub-result.
**Date**: 2026-05-31
**Trigger**: AUDIT-WORKING-526815 (deeply-mathematical de-novo pass), findings F127/F128, surfaced during the 2026-05-30 gold-lift sweep. Off-ramp note recorded in `01-aat-core/src/der-class-coercion-via-wrapping.md` §"Incidental audit gold" and `audits/AUDIT-WORKING-526815/.integrated/78-der-class-coercion-via-wrapping.md`.
**Segment under challenge**: `#der-class-coercion-via-wrapping` (Theorem 2 + the W₀/W₁/W₂ regime table). Load-bearing per `CLAUDE.md` Key Architectural Decisions / Known Fragilities.
**Prior reasoning trail**: `spikes/class-coercion-wrapping/03-leakage.md` (sub-spike C, 2026-05-09) — the origin of the bound. This spike re-opens its central claim.

---

## 0. The challenge, stated precisely

The segment's W₁ row asserts the structural bound

$$\kappa_{W_1} \le I(A(q_M); G_W \mid q_M),$$

offered as the bound on the residual leakage that survives when condition (C3) — *no implicit goal-inference*, $P(A(q_M) \mid q_M, G_W) = P(A(q_M) \mid q_M)$ — is *relaxed* (Theorem 2's regime).

The auditor's objection (F127/F128): for a **stateless** component, under **exact conditioning on the fully-observed query** $q_M$,

$$I(A(q_M); G_W \mid q_M) \equiv 0,$$

because once $q_M$ is fixed the response distribution $P(A(q_M)\mid q_M)$ is fully determined — a stateless oracle has, by definition, nothing left to depend on. So the quantity the segment names as the W₁ leakage bound is *identically zero* on the very class of components (stateless oracles) the theorem models, and therefore cannot be the bound on a leakage that the segment simultaneously claims is "potentially substantial" for goal-rich LLMs. The number it computes (zero) and the phenomenon it names (residual pretraining-induced leakage) are not the same thing.

The auditor names the channels that *do* carry the leakage and that the current bound does **not** measure: query-content correlation $I(q_M; G_W)$, hidden component state, and conversation history / unobserved context.

**This spike's job**: find the truth — is the objection (A) defused by the bound's actual setting, (B) a correct diagnosis pointing at a *sharper* bound, or (C) a structural no-go on bounding W₁ leakage at all in the stateless-exact regime? Strengthen-first: attempt to make the W₁ guarantee *true and non-vacuous* before conceding any down-tier.

---

## 1. The auditor is right, and the error is precise

Work the conditional mutual information for a stateless oracle. "Stateless" means $A$'s output law depends on its input and nothing else:

$$P(A(q) \mid q, Z) = P(A(q)\mid q) \quad\text{for every side variable } Z,\ \text{in particular } Z = G_W. \tag{1}$$

But that is *exactly* the statement (C3). And the conditional mutual information

$$I(A(q_M); G_W \mid q_M) = \mathbb E_{q_M, G_W}\Big[\, D_\text{KL}\big(P(A(q_M)\mid q_M, G_W)\,\big\Vert\, P(A(q_M)\mid q_M)\big)\,\Big] \tag{2}$$

is zero **if and only if** (C3) holds (the integrand is the per-$(q_M,G_W)$ KL whose vanishing *is* (C3)). So for any **stateless** $A$, (1) ⟹ (C3) ⟹ $I(A(q_M); G_W\mid q_M)=0$.

This exposes the exact defect, and it is sharper than "the bound is loose":

> **The W₁ bound is circular, not merely vacuous.** $I(A(q_M); G_W\mid q_M)$ is not an independent quantity that *bounds* the leakage left when (C3) is relaxed. It is — up to the expectation over the worst-case $G_W$ — *the leakage itself*: it is the expected value of the very KL divergence Theorem 2 takes as its hypothesis ($D_\text{KL}(P(A(q_M)\mid q_M, G_W)\,\Vert\,P(A(q_M)\mid q_M))\le\kappa$). Compare (2) with the segment's Theorem-2 premise: the W₁ "bound" is the average of the per-query quantity that Theorem 2 *assumes is already $\le\kappa$*. Writing $\kappa_{W_1}\le I(A(q_M);G_W\mid q_M)$ therefore says "$\kappa$ is bounded by (an average of) $\kappa$." It transports no information. And for a stateless oracle it evaluates to $0$ regardless of how goal-rich the pretraining was, which is why it reads as vacuous.

So F127/F128 land. But — and this is where strengthen-first earns its keep — the *phenomenon* the segment is reaching for (an LLM, asked a goal-blind question, bending its answer toward an inferred operator goal) is **real**, and it **is** structurally boundable. The error is in *where the goal variable lives* and *what is conditioned on*. Fix those two things and the W₁ guarantee comes back stronger, not weaker.

---

## 2. The two senses of $G_W$ — the locus error

The segment silently conflates two different objects under the symbol $G_W$, and the conflation is the whole bug.

- **$G_W^{\text{state}}$ — the wrapper's purposeful-state register.** This is the $G_W$ of the type signatures: the thing $q_M$ structurally does *not* take as an argument, the thing the directed-separation theorem conditions on. It is an *internal wrapper variable*.
- **$G_W^{\text{op}}$ — the operator's latent goal / task context** that *generated* the situation the wrapper is in. This is the thing a competent LLM *infers* from query surface form (the "input-structure extraction" competence the segment's own §Discussion "Two senses of component competence" names). It is a *latent generative variable*, never an explicit argument to anything.

For a stateless oracle the response cannot depend on $G_W^{\text{state}}$ once $q_M$ is fixed — that is (1), and it is *correct*: the type signature genuinely closes that path. **The auditor's "vacuous" verdict is exactly right about $G_W^{\text{state}}$.** Theorem 1 (the exact form) is sound and the conditioning that makes $I(\cdot;G_W^{\text{state}}\mid q_M)=0$ is a *feature*: it certifies the structural path is closed.

The leakage the segment is *worried about* is leakage about $G_W^{\text{op}}$ — and that information does not arrive "after conditioning on $q_M$." **It arrives in $q_M$ itself.** A goal-blind query that says "summarize this auth-module diff" already carries, in its content, the operator's goal ("fix the auth bug"); the stateless oracle reads it out of the query content and bends the summary, with no dependence on any internal register at all. The leakage is real, structural, and *fully upstream of the response* — it is in the **selection of $q_M$**, not the **processing of $A(q_M)$**.

This is precisely the distinction `#der-directed-separation` draws between *selection* and *processing*. Directed separation is about processing; the segment correctly closes the processing path. But the W₁ leakage row then tries to measure a *selection-side* leak with a *processing-side* conditional mutual information — and the conditioning that's right for the processing claim ($\mid q_M$) is exactly what annihilates the selection-side signal.

---

## 3. The corrected W₁ bound (landing B)

### 3.1 What we actually want to bound

The operationally meaningful leakage is: *how much does the wrapper's belief update $M_{W,m+1}$ end up depending on the latent operator goal $G_W^{\text{op}}$, beyond what the realized observation legitimately licenses?* Two channels, and they must be separated because they have different status:

1. **Selection channel (legitimate, but it is where the leak lives).** $G_W^{\text{op}} \to$ (wrapper's history / policy $\pi_W$) $\to$ choice of $q_M$ $\to A(q_M)\to M_{W,m+1}$. The segment's own §Discussion "Quality–separation tradeoff" already gestures at this: "Maximally informed queries … increase the mutual information $I(q_M; G_W)$." That instinct is correct; it was just never carried into the bound.
2. **Processing channel (forbidden; structurally closed by W₁).** $G_W^{\text{state}} \to A(q_M)\mid q_M$. Closed for a stateless oracle by (1); this is what Theorem 1 certifies.

So the honest W₁ statement is: *the processing channel is shut (structurally, exactly), and the entire residual leakage is the selection channel, whose magnitude is governed by the goal-content of the query content itself.*

### 3.2 The bound

Let $G \equiv G_W^{\text{op}}$ be the latent operator goal, and let $q_M$ be the (random, because history-dependent) goal-blind query the wrapper issues. The quantity that controls how much $A$'s goal-blind response can reveal about / be bent by the goal is the mutual information between the **query the wrapper chose** and the **goal**:

$$\boxed{\ \kappa_{W_1}^{\text{sel}} \;:=\; I\big(A(q_M);\, G\big) \;\le\; I\big(q_M;\, G\big)\ } \tag{3}$$

The first inequality is the **data-processing inequality** along $G \to q_M \to A(q_M)$ — for a stateless oracle $A(q_M)$ is a (stochastic) function of $q_M$ alone, so $A(q_M)$ cannot carry more goal information than $q_M$ does. This is the *correct* use of DPI; the segment invoked DPI for Theorem 2 but on the wrong link. **Crucially, $I(q_M; G)$ is generically nonzero** — it is exactly the pretraining/deployment-distribution query-content/goal-content correlation the segment's prose keeps describing, now sitting in a quantity that can actually be positive. The vacuity is gone.

Two things to verify, because they are the load-bearing moves:

- **Why this is *not* the same as $I(A(q_M);G_W\mid q_M)$.** Dropping the conditioning on $q_M$ is the whole point. Conditioning on $q_M$ asks "given the exact query, does the *response* still depend on the goal?" — answer for a stateless oracle: no (that's the closed processing path). Removing the conditioning asks "across the queries the wrapper actually issues, how much goal information rides in?" — answer: as much as the query-selection policy lets in. The first is a property of the oracle's input-output law; the second is a property of the **wrapper's $q_M$-selection policy** interacting with the goal. The bound should be a property of the wrapper's design (that's what makes it *actionable*), and (3) is.
- **Why it sharpens rather than weakens the guarantee.** $I(q_M; G)$ is a quantity the **wrapper controls**. The §Discussion tradeoff becomes a theorem: maximally goal-blind queries (current observation only, no history, no system prompt) drive $I(q_M;G)\to 0$ and recover exact directed separation on the merits; maximally informed queries raise it. W₁'s guarantee is now: *choose your $q_M$-policy and you have purchased a quantitative, structurally-derived leakage ceiling* — a stronger and more useful statement than the original, which (we now see) was the zero function dressed as a bound.

### 3.3 Propagating to the wrapper state (the DPI step the segment wanted)

The wrapper update $M_{W,m+1}$ is a deterministic function of $(M_{W,m}, o_{W,m+1}, q_M, A(q_M))$. Along the Markov chain $G \to q_M \to (q_M, A(q_M)) \to M_{W,m+1}$, DPI gives

$$I\big(M_{W,m+1};\, G\ \big\vert\ M_{W,m}, o_{W,m+1}\big)\ \le\ I\big(A(q_M);\, G\ \big\vert\ M_{W,m}, o_{W,m+1}\big)\ \le\ I(q_M; G). \tag{4}$$

This is the genuinely-non-vacuous analog of Theorem 2's conclusion. It says the goal-information that reaches the wrapper's belief state is upper-bounded by the goal-content of the query-selection policy — and it conditions on $(M_{W,m}, o_{W,m+1})$, *not* on $q_M$, precisely because conditioning on $q_M$ would (correctly, for the closed processing path) zero it out and miss the selection leak.

> **Subtlety worth flagging for the integration pass.** The conditioning set in (4) matters. Conditioning on $(M_{W,m}, o_{W,m+1})$ leaves the selection-channel leak intact *only if $q_M$ is not a deterministic function of $(M_{W,m}, o_{W,m+1})$ alone* — i.e., only if the query-selection policy draws on history or context beyond the current $(M_{W,m},o_{W,m+1})$. If $q_M = q_M(M_{W,m}, o_{W,m+1})$ deterministically (the segment's stated type signature), then conditioning on $(M_{W,m}, o_{W,m+1})$ *also* fixes $q_M$, and (4) collapses to zero — recovering exactly the auditor's vacuity, one level up. This is not a bug in the bound; it is the bound telling the truth: **if the goal-blind query is a deterministic function of only the current belief and observation, then a stateless oracle genuinely leaks nothing about $G^{\text{op}}$ through the belief channel** — because the only way the goal could have entered is through $M_{W,m}$ (already conditioned) or $o_{W,m+1}$ (already conditioned, and selection-side per `#der-directed-separation`). The residual leak is real *only when* $q_M$'s selection reaches into goal-correlated history/context that is **not** in the conditioning set — i.e. exactly the auditor's "conversation history / unobserved context" channel. The corrected bound therefore *localizes* the leak with precision: it is nonzero iff the query-selection policy has a goal-correlated input outside $(M_{W,m}, o_{W,m+1})$.

So the right unconditional statement, which does not depend on the analyst's choice of conditioning set, is (3): $\kappa_{W_1}^{\text{sel}} = I(A(q_M); G) \le I(q_M; G)$, with the understanding that $q_M$ is drawn under the wrapper's actual operating policy (which generically *does* depend on goal-correlated history — that is what makes real wrappers leak).

---

## 4. The hidden-state / history channel — and the embedded no-go (landing C)

The auditor's third named channel — *hidden component state* — is where a clean structural sub-result lives, and it is worth stating as a no-go because it sharpens the W₁/W₂ boundary the segment cares about.

Drop the stateless assumption. Let $A$ carry hidden state $S$ (KV-cache across turns, retrieval memory, adaptive context). Now

$$P(A(q_M)\mid q_M, S),\qquad S \text{ correlated with } G^{\text{op}} \text{ through shared history.}$$

Even with $q_M$ structurally goal-blind and a perfectly closed type signature, $A(q_M)$ can depend on $G^{\text{op}}$ **through $S$**, and this dependence *survives conditioning on $q_M$*:

$$I\big(A(q_M);\, G^{\text{op}} \mid q_M\big)\ \ge\ 0,\quad\text{and generically } \gt 0\ \text{when } S \not\perp G^{\text{op}}\ \text{(the conditioning on } q_M \text{ no longer closes the path, because the leak routes through } S\text{).} \tag{5}$$

> **No-go (W₁ structural-bound boundary).** For a **stateful** component whose hidden state is correlated with the operator goal, *there is no bound on the belief-channel goal-leakage derivable from the wrapper's query-selection policy alone.* The leak flows through a channel ($S$) the wrapper does not observe and cannot condition on. Conditioning $I(A(q_M);G^{\text{op}}\mid q_M, S)=0$ would close it — but $S$ is unobservable by the wrapper (it is *inside* the black-box oracle), so this conditioning is not available to any wrapper-level analysis. **This is exactly the W₁/W₂ boundary, recovered as a theorem:** W₁'s structural bound (3)–(4) is available *if and only if* the component is effectively stateless across the goal-blind/goal-conditioned call boundary (condition (C2), *stationary conditional*, strengthened to *state-resetting between $q_M$ and $q_G$ calls*). When the component carries goal-correlated state across calls, only a *behavioral* bound is available — the same kind of bound W₂ has, for the same structural reason (an unconditionable goal-correlated channel). The segment currently files the structural-vs-behavioral split as a *regime choice* (how you build the wrapper); this no-go shows it is *also* forced by a *component property* (statefulness across the call boundary), independent of wrapper design.

This is a first-class structural result, not a softening: it says precisely *when* W₁'s structural guarantee exists and *when* it provably degrades to a behavioral one, and it identifies the sharp dividing condition (goal-correlated cross-call hidden state). The segment's (C2) already excludes "adaptation-during-deployment"; this no-go shows (C2) must be *strengthened* — it is not adaptation that breaks the structural bound, it is mere *goal-correlated state persistence across the call boundary*, which a frozen-weights LLM with a conversation KV-cache exhibits without any weight adaptation at all. The Working Note on "$\Sigma$-channel-suppressed W₁" (holding strategic context fixed across calls, stripping $\Sigma$-content from queries) is exactly the operational discharge of this no-go — and it should be promoted from a Working Note to a *named condition* (C2′) on which the W₁ structural bound depends.

---

## 5. Verdict

**Landing state: (B), with an embedded (C).** The auditor's vacuity finding (F127/F128) is **correct** — the stated bound $\kappa_{W_1}\le I(A(q_M);G_W\mid q_M)$ is circular (it bounds $\kappa$ by an average of $\kappa$) and evaluates to identically zero on the stateless oracle the theorem models. But the right move is *not* to delete W₁'s structural claim; it is to **relocate the goal variable and the conditioning**:

- **(B) Corrected structural bound.** $\kappa_{W_1}^{\text{sel}} = I(A(q_M); G^{\text{op}}) \le I(q_M; G^{\text{op}})$, via the data-processing inequality along $G^{\text{op}}\to q_M\to A(q_M)$. This is non-vacuous (generically positive), is a property of the **wrapper's query-selection policy** (hence actionable and design-controllable), turns the §Discussion quality–separation tradeoff into a theorem, and is *stronger* than the original because the original was the zero function. The leakage lives in the **selection** of $q_M$, not the **processing** of $A(q_M)$ — which is exactly the selection/processing distinction `#der-directed-separation` already draws.

- **(C) Embedded no-go sharpening the W₁/W₂ boundary.** The structural bound (B) exists *iff* the component does not carry goal-correlated hidden state across the call boundary. With such state, the goal-leak flows through an unobservable, unconditionable channel and only a *behavioral* bound is available — recovering the W₁/W₂ structural-vs-behavioral split as a forced consequence of a *component property* (cross-call goal-correlated statefulness), not merely a wrapper-design regime choice. This forces (C2) → (C2′): the relevant condition is not "no online adaptation" but "no goal-correlated state persistence across the goal-blind/goal-conditioned call boundary" — which a frozen-weights LLM with a conversation cache violates.

**What this does to the load-bearing status.** The W₁ regime's guarantee is *not* undercut — it is corrected and sharpened. Theorem 1 (exact directed separation under (C1)–(C3)) is **untouched and sound**; the auditor's CMI-is-zero observation is, for Theorem 1, a *confirmation* that the processing path is closed. What was broken was the *Theorem-2 residual-leakage bound* and its W₁-row summary, which named the wrong quantity. The corrected bound restores a genuine, controllable, structurally-derived leakage ceiling for the stateless-across-calls case, and the no-go honestly bounds where that ceiling stops existing.

**Confidence.** High on the diagnosis (the circularity/vacuity is elementary once the two senses of $G_W$ are separated, and is independently visible in the prior sub-spike C's own line 41 "the only path … is through *implicit inference*" — which is a selection-side, in-the-query phenomenon mislabeled as a conditional-on-$q_M$ one). High on the corrected bound (3)–(4): the DPI steps are standard and the direction is forced. High on the no-go (5): it is a direct consequence of unobservable goal-correlated state. The one item I did *not* fully close (see §6).

---

## 6. Proposed integration (draft segment text — math-lives-in-segments)

**Do not apply** — drafted here per the spike-routing convention; canon edits and status/tier transitions are reserved for the external-eye gate. The corrected content lands in `#der-class-coercion-via-wrapping`. Proposed changes:

### 6.1 New condition (C2′), tightening (C2)

> **(C2′) No goal-correlated cross-call state.** The component's hidden state does not carry information about the operator goal $G^{\text{op}}$ across the boundary between the goal-blind ($q_M$) and goal-conditioned ($q_G$) calls of a macro-step. Equivalently, $A$'s response to $q_M$ is conditionally independent of $G^{\text{op}}$ given $q_M$ and the component's *pre-call* state, and that pre-call state is goal-uncorrelated (reset, or stripped of $\Sigma/G$-content per the $\Sigma$-channel-suppressed-W₁ Working Note). (C2′) is what the *structural* W₁ bound below depends on; it strengthens (C2) — the breaking condition is not online weight-adaptation but mere goal-correlated state persistence across the call boundary, which a frozen-weights LLM with a conversation cache exhibits.

### 6.2 Replace the Theorem-2 / W₁-row leakage bound

Replace the W₁ row's `$\kappa_{W_1} \le I(A(q_M); G_W \mid q_M)$` (and the corresponding Theorem-2 framing of the residual) with the selection-channel bound. Proposed Formal-Expression insert after Theorem 2:

> *[Derived (W₁-selection-leakage-bound, from (C1)+(C2′), data-processing inequality)]*
>
> Under (C1) and (C2′), the goal-information reaching the wrapper's belief update through the goal-blind channel is bounded by the goal-content of the wrapper's query-selection policy:
>
> $$\kappa_{W_1} \;=\; I\big(A(q_M);\, G^{\text{op}}\big) \;\le\; I\big(q_M;\, G^{\text{op}}\big),$$
>
> where $G^{\text{op}}$ is the latent operator goal and $q_M$ is drawn under the wrapper's operating policy. *Proof.* $G^{\text{op}}\to q_M \to A(q_M)$ is a Markov chain under (C2′) ($A(q_M)$ depends on $G^{\text{op}}$ only through $q_M$); the data-processing inequality gives the bound. ∎
>
> The bound is a property of the wrapper's $q_M$-selection policy, not of the component's input–output law: maximally goal-blind queries (current observation only) drive $I(q_M; G^{\text{op}})\to 0$ and recover exact directed separation; richer, history-laden queries raise it. This is the formal content of the quality–separation tradeoff in §Discussion.

And the propagated form (4) as the corrected Theorem-2 conclusion (CMI version, conditioning on $(M_{W,m}, o_{W,m+1})$ — explicitly *not* on $q_M$).

### 6.3 New appendix-grade no-go segment (per math-lives-in-segments, since it is non-obvious)

A short `disc-` or appendix segment stating the W₁/W₂-boundary no-go of §4: *the structural W₁ bound exists iff (C2′) holds; under goal-correlated cross-call state the belief-channel leak is unconditionable at the wrapper level and only a behavioral (W₂-type) bound remains.* This is the "are you sure you can't just …?" kind of result — it explains why the structural/behavioral split is forced by a component property and not only by wrapper-design choice — so per *integration-is-replacement* it warrants its own demonstration rather than a parenthetical. Candidate slug: `disc-w1-structural-bound-boundary` (or fold into `#disc-partial-coupling-pathways`, which already discusses the W₁ ↔ process / W₂ ↔ content correspondence).

### 6.4 History-layer note (CHANGELOG / Working Notes only — not the body)

The "previously carried a circular/vacuous bound $I(A(q_M);G_W\mid q_M)$" record belongs in CHANGELOG and this spike, **not** in the segment body or FINDINGS (per *integration-is-replacement*: body states present truth; history lives in the history layers). The corrected bound is labeled at its honest tier — `conditional` on (C1)+(C2′) — with no "this is not a weakening" defense in the body.

---

## 7. What I could not fully resolve

- **Tightness of (3).** $I(A(q_M);G^{\text{op}})\le I(q_M;G^{\text{op}})$ is the right *upper* bound, but I did not characterize the gap. The gap is the "accuracy effect" of §Discussion "Two senses of component competence" — a high-fidelity world-simulator that answers $q_M$ on its literal content leaves goal-information *in $q_M$* unexploited in its response, so $I(A(q_M);G^{\text{op}})$ can sit well below $I(q_M;G^{\text{op}})$. Whether a *lower* bound or a sharper characterization is available (in terms of the component's input-structure-extraction competence) is open — and it connects directly to the already-open "decomposed empirical estimator" PROPOSED Tier-3 spike. I believe this is the same phenomenon viewed from the bound side, and they should be worked together.
- **Estimator.** $I(q_M; G^{\text{op}})$ is estimable (vary the latent goal across a fixed query-selection policy, measure query-distribution divergence) but $G^{\text{op}}$ is latent, so the estimator needs an operationalization of "operator goal" — likely the same construct the $\hat\kappa_{\text{processing}}$ estimator of `#der-directed-separation` uses. Not worked here.
- **Interaction with the bounded-signaling assumption.** §4's unobservable-channel no-go is structurally the *belief-side* twin of the *action-side* bounded-signaling assumption named in `#der-directed-separation` §Discussion (goal leaks through behavioral richness the formal action channel undercounts). Both are "a goal-correlated channel the formalism does not see." Whether they are the same theorem viewed from two sides is a tidy conjecture I did not chase.

---

## File index / cross-refs

- This file: `spikes/spike-w1-leakage-vacuity-2026-05-31.md`
- Challenges: `audits/AUDIT-WORKING-526815/.integrated/78-der-class-coercion-via-wrapping.md` (F127/F128)
- Segment under challenge: `01-aat-core/src/der-class-coercion-via-wrapping.md`
- Prior reasoning trail (origin of the bound): `spikes/class-coercion-wrapping/03-leakage.md`
- Companion: `01-aat-core/src/der-class-coercion-in-composition.md`, `01-aat-core/src/der-directed-separation.md`
- Related open spikes (should be worked with §7): PROPOSED Tier-3 decomposed-$\kappa$ estimator; PROPOSED Tier-2 decorrelation-by-construction (both in `der-class-coercion-via-wrapping` Working Notes).
