# Spike: Goal-information flow duality — is (C2′) the belief-side twin of action-side bounded-signaling?

**Status**: derivation/analysis spike complete. **Verdict: a genuine structural duality, but a *partial* one** — the two conditions are two faces of a single invariant (*the wrapper boundary admits a structural goal-leakage certificate iff every goal→target path factors through one designated, observable channel; statefulness/rich-behavior reopens an unobservable bypass*), and the certifiability-vs-behavioral dichotomy recurs on the action-out side **exactly**. But the duality breaks on one axis precisely, and the break is itself informative. The honest landing is **(B) a small new recognition** — a shared structural pattern that licenses a one-statement scope condition on the action side mirroring (C2′), with the asymmetry named — *not* a grand conservation law (that over-reaches; §5).
**Date**: 2026-05-31
**Kind**: exploratory theory spike (read-only on canon; no segment edits, no `status:` changes, no git).
**Trigger**: `spike-w1-leakage-vacuity-2026-05-31.md` §7 third open item — *"§4's unobservable-channel no-go is structurally the belief-side twin of the action-side bounded-signaling assumption … Whether they are the same theorem viewed from two sides is a tidy conjecture I did not chase."* Also flagged open in `#disc-w1-structural-bound-boundary` §Discussion "Relation to the action-side bounded-signaling assumption" and `#der-class-coercion-via-wrapping` Working Notes (via the boundary segment).
**Reads (canon, no edits)**: `#der-directed-separation`, `#der-class-coercion-via-wrapping`, `#disc-w1-structural-bound-boundary`, `#disc-adversarial-coupling-pressure`; the two boundary-intuition spikes (`spike-w1-w2-boundary-intuition-2026-05-31.md`, `spike-guc-class-boundaries-intuition-2026-05-31.md`).

---

## 0. The question, stated precisely

AAT's directed-separation wrapper imposes two boundary conditions on goal-information flow that *look* dual:

- **(C2′)** (belief-side, goal flowing **inward toward belief**): for the W₁ structural leakage bound to exist, no goal-correlated component state may flow *into* the goal-blind belief call across the call boundary. When it holds the leakage bound is *structural*; when it fails only a *behavioral* bound survives — a **certifiability** discontinuity (`#disc-w1-structural-bound-boundary`).
- **Bounded-signaling** (action-side, goal flowing **outward toward observers**): the channel from $G_t$ to the world is assumed to run *only* through action choice, so action coarseness $\lvert\mathcal A\rvert$ upper-bounds the rate goal-content leaks *out* to observers. Fails for behaviorally-rich agents (`#der-directed-separation` §Discussion "Bounded-signaling"; saturated adversarially in `#disc-adversarial-coupling-pressure`).

Four questions, taken in order:

1. **Is the duality real or a surface analogy?** (§1–§2)
2. **Is there a unifying invariant** — a "goal-information budget / conservation" with (C2′) and bounded-signaling as its two faces? (§3, and the honest deflation in §5)
3. **Does the certifiability-vs-behavioral split recur on the action-out side** — a "structural bounded-signaling certificate" available under some condition, behavioral-only otherwise, mirroring W₁/W₂? (§4)
4. **If real, what new statement does it license, and where does it land** (per math-lives-in-segments)? (§6)

Strengthen-first posture: try to make the duality a *theorem* (a single invariant specializing to both) before settling for "merely analogous." Where it fails, characterize the break exactly — a clean negative on the strong form is a full result.

---

## 1. The two structures, written in one notation

Both are statements about a *latent goal variable* reaching a *target* through a *designated channel*, with a structural bound that holds iff a Markov chain holds.

### 1.1 Belief-side ((C2′), from `#der-class-coercion-via-wrapping` + `#disc-w1-structural-bound-boundary`)

- **Source**: $G^{\text{op}}$, the latent operator goal.
- **Designated channel**: $q_M$, the goal-blind query the wrapper *selects* (the wrapper controls the selection policy).
- **Target**: $M_W$, the wrapper's belief, via the component response $A(q_M)$.
- **Structural bound (holds under (C2′))**: along the Markov chain $G^{\text{op}} \to q_M \to A(q_M)$, the data-processing inequality (DPI) gives
$$\kappa_{W_1}^{\text{sel}} = I\big(A(q_M);\, G^{\text{op}}\big) \le I\big(q_M;\, G^{\text{op}}\big).$$
- **Failure mode**: hidden component state $S \not\perp G^{\text{op}}$ opens a *bypass* edge $G^{\text{op}} \to S \to A(q_M)$ that does not pass through $q_M$; the Markov chain breaks; the leak survives conditioning on $q_M$; $S$ is **unobservable** to the wrapper, so no wrapper-level bound is derivable. Behavioral monitoring of $I(A(q_M); G^{\text{op}}\mid q_M)$ is all that remains.

### 1.2 Action-side (bounded-signaling, from `#der-directed-separation` §Discussion)

- **Source**: $G_t$, the agent's own goal/purposeful substate.
- **Designated channel**: $a_t = \pi(M_t, G_t)$, the discrete action, with coarseness $\lvert\mathcal A\rvert$.
- **Target**: an external observer's inference $\hat G_t$ of the goal.
- **Structural bound (holds under bounded-signaling)**: if the *only* externally-observable signal of $G_t$ is $a_t$, then along $G_t \to a_t \to \hat G_t$, DPI gives
$$I\big(\hat G_t;\, G_t\big) \le I\big(a_t;\, G_t\big) \le H(a_t) \le \log\lvert\mathcal A\rvert.$$
- **Failure mode**: a rich behavioral signature $B_t$ (prosody, latency, code-style, attention pattern) correlated with $G_t$ opens a *bypass* edge $G_t \to B_t \to \hat G_t$ that does not pass through $a_t$; the chain $G_t \to a_t \to \hat G_t$ is no longer the only path; the per-action-bit ceiling $\log\lvert\mathcal A\rvert$ no longer bounds the leak; $B_t$ is **not in the formal interface**, so the formal channel undercounts.

### 1.3 The alignment is exact on five of six structural slots

| Structural slot | Belief-side ((C2′)) | Action-side (bounded-signaling) | Same? |
|---|---|---|---|
| Latent goal source | $G^{\text{op}}$ (operator goal) | $G_t$ (own goal) | ✓ goal-source |
| Designated channel | $q_M$ (selected query) | $a_t$ (chosen action) | ✓ a chosen, finite-capacity emission |
| Capacity handle | $I(q_M; G^{\text{op}})$ — query goal-content | $\log\lvert\mathcal A\rvert$ — action coarseness | ✓ both cap the channel's goal-bandwidth |
| Bound mechanism | DPI along source→channel→target Markov chain | DPI along source→channel→target Markov chain | ✓ **identical theorem** |
| Failure = unobservable bypass | hidden state $S$: $G^{\text{op}}\to S\to A(q_M)$ | rich behavior $B_t$: $G_t\to B_t\to \hat G_t$ | ✓ bypass edge skipping the designated channel |
| **Direction of flow** | goal **in**, toward belief | goal **out**, toward observer | ✗ **opposite** |

**Five of six slots are structurally identical, and the bound mechanism — DPI along a single-channel Markov chain, broken by an unobservable bypass — is the *same theorem*.** The lone difference is the direction of flow. This is not a surface analogy: the same proof object (DPI; Markov-chain factorization; bypass-edge breaks it) does the work on both sides. **The duality is real** (answer to Q1: real, not surface).

---

## 2. The direction-reversal is a genuine duality, not just two unrelated bounds

The flip — *goal-in-toward-belief* vs *goal-out-toward-observer* — is exactly the kind of reversal that makes a duality interesting rather than a coincidence. Three things confirm it is a structural reflection across the wrapper/agent boundary, not two bounds that happen to share a proof template:

**(a) They are the two halves of the same separation statement.** `#der-directed-separation` *itself* presents them as halves: the belief-update side asserts $M_{\tau^+}\perp G_t \mid (M_{\tau^-}, e_\tau)$ (goal does not get *into* belief-processing), and the action side asserts the $G_t\to$world channel runs only through $a_t$ (goal does not get *out* except through actions). The segment's own §Discussion "Bounded-signaling" opens: *"Directed separation as stated … asserts [the belief-side independence]. Symmetrically, on the action side, the framework implicitly relies on …"* — the word *symmetrically* is canon already gesturing at the duality this spike is verifying. Directed separation is the conjunction of *goal-blind belief intake* and *goal-bounded action output*: the in-leg and the out-leg of one boundary.

**(b) The conditioning that closes one is the dual of the conditioning that closes the other.** On the belief side the *processing* channel $G_W^{\text{state}}\to A(q_M)\mid q_M$ is closed structurally (Theorem 1), and the residual is the *selection* channel $G^{\text{op}}\to q_M$. On the action side the dual decomposition holds: the *policy-emission* channel $G_t\to a_t$ is the structurally-acknowledged channel (the agent legitimately acts on its goal), and the residual leak is the *side-channel* $G_t\to B_t$ that the formalism does not designate. In both cases: one channel is **named and bounded**, the other is **unbounded because it is off-interface**. The selection/processing distinction of `#der-directed-separation` is the belief-side instance; the action/side-channel distinction is its mirror.

**(c) The wrapper geometry literally reflects them.** Picture the wrapper as a box. (C2′) governs what crosses the boundary *inbound* on the belief call; bounded-signaling governs what crosses *outbound* on the action emission. They are the same boundary read in the two crossing directions. The "unobservable bypass" in each case is a path that crosses the boundary *without going through the designated port* — inbound through component state $S$ (which lives inside the black box, below the query port), outbound through behavioral richness $B_t$ (which lives outside the action port, in the agent's full physical/textual emission).

**Verdict on Q1/Q2-structure: a genuine structural duality.** The same DPI-Markov-chain object, reflected across the wrapper boundary, with goal-flow direction reversed. This is the tidy conjecture of the parent spike's §7, and it holds.

---

## 3. The unifying invariant — stated at the right altitude

The shared content is a single recognition. State it as a *pattern* (the honest tier; see §5 for why not more):

> **Single-channel goal-leakage pattern.** Let a latent goal variable $G$ reach a target $T$ across a system boundary. Suppose the design *designates* one channel $c$ (a query selection; an action emission) as the only intended carrier of goal-content across that boundary, and let $\mathrm{cap}(c)$ be a design-controllable handle on that channel's goal-bandwidth ($I(c; G)$; $\log\lvert\mathcal A\rvert$). Then:
>
> 1. **(Structural certificate, available iff single-channel-factorization holds.)** If every $G\to T$ path factors through $c$ — i.e. $G\to c\to T$ is a Markov chain — then by the data-processing inequality $I(T; G) \le I(c; G) \le \mathrm{cap}(c)$, a bound *derivable from the design of $c$ alone*.
> 2. **(Certifiability discontinuity at off-channel reopening.)** If any path $G\to U\to T$ exists with $U$ **off-interface** (unobservable / unmodeled at the boundary: hidden component state $S$; rich behavioral signature $B_t$), the Markov chain breaks, the structural certificate is *unavailable* (it computes a value that is now false), and only a *behavioral* bound — direct monitoring of $I(T;G\mid c)$ — remains.

(C2′) is this pattern with $G=G^{\text{op}}$, $c=q_M$, $T=M_W$, off-channel $U=S$, flowing **inward**. Bounded-signaling is the same pattern with $G=G_t$, $c=a_t$, $T=\hat G_t$, off-channel $U=B_t$, flowing **outward**.

This is a real invariant — but it is an **invariant of *form* (a shared structural template), not a conserved *quantity*.** That distinction is the whole of §5, and getting it right is what keeps the result honest.

### 3.1 What "budget" correctly means here, and what it does not

The handle $\mathrm{cap}(c)$ is a *per-channel capacity ceiling*, and it is genuinely design-controllable on both sides — drive $I(q_M; G^{\text{op}})\to 0$ by goal-blind query selection; drive $\log\lvert\mathcal A\rvert$ down by coarsening the action interface. This is the legitimate, defensible reading of a "goal-information budget": **each designated channel has a goal-bandwidth ceiling the designer can lower, and the structural guarantee is exactly the DPI statement that the target cannot learn more goal than the channel carries.** That much is a theorem (the DPI), instantiated twice.

What is **not** licensed (and §5 shows why) is a *conservation* statement of the form "total goal-information across the boundary is fixed; what doesn't leak out must stay in" or "in-budget + out-budget = const." There is no conserved total — the two channels carry *different goal variables* ($G^{\text{op}}$ the operator's, $G_t$ the agent's own) to *different targets*, and goal-information is freely copyable (it is not a flow-conserved quantity like probability mass or energy). The invariant is the *pattern*, reused; not a quantity, conserved.

---

## 4. The certifiability-vs-behavioral split recurs on the action-out side — exactly

This is the sharpest confirmation, and it answers Q3 cleanly. The W₁/W₂ structural-vs-behavioral dichotomy is **not** specific to wrapping; it is a consequence of the single-channel pattern, so it must recur wherever the pattern instantiates. It does, on the action side, with the same two-part shape the boundary-intuition spikes found for W₁/W₂.

**The action-side analog of W₁ (structural certificate available).** An agent whose *entire externally-observable emission is the action sequence* — a chess engine that emits only moves, a programmatic controller that emits only its control vector, a text agent on a channel that is **provably** token-only with fixed latency and no timing/formatting side-band — admits a *structural bounded-signaling certificate*: by construction the only $G_t\to$world path is $G_t\to a_t$, so $I(\hat G_t; G_t)\le \log\lvert\mathcal A\rvert$ is certifiable by inspecting the *interface*, exactly as W₁'s bound is certifiable by inspecting the *query type signature*. Call this the **action-side (C2′)-analog**: *no goal-correlated off-action emission channel*.

**The action-side analog of W₂ (behavioral-only).** An agent with rich, uncontrolled behavioral output — a human (prosody, micro-expression, latency), an embodied robot (motion signature), an LLM whose deployment leaks timing/formatting/token-distribution side-bands — has goal-correlated emission *outside* the designated action. No structural bound on $I(\hat G_t; G_t)$ is derivable from the action interface; only *behavioral monitoring* (measure how much an adversarial inferrer actually recovers) bounds the leak. This is W₂ on the output side: the separation lives at a behavioral boundary, fragile and empirically-estimated.

**And the discontinuity is the same kind — certifiability, not behavior.** Run the boundary-intuition spikes' move on the action side. Parameterize the off-action leakage by $\varepsilon$ = the goal-correlation in the behavioral side-channel $B_t$ ($\varepsilon=0$: emission is action-only; $\varepsilon\gt 0$: a sliver of goal-correlated prosody/latency). Then, by direct transcription of `#disc-w1-structural-bound-boundary`'s argument:

- **Behavior is continuous in $\varepsilon$.** The actual goal-information an observer can recover is a continuous function of $\varepsilon$ through $0$ — a tiny behavioral side-channel leaks a tiny amount.
- **The certificate's validity is a step.** At $\varepsilon=0$ the interface-inspection certificate ("the only emission is $a_t$, so the leak is $\le\log\lvert\mathcal A\rvert$") is *true*. At any $\varepsilon\gt 0$ the same certificate still computes the same ceiling but is now *false* — the real leak took the off-action path the certificate's eyes are closed to, and can exceed $\log\lvert\mathcal A\rvert$. Only behavioral monitoring of what an inferrer recovers remains honest.

So the **W₁/W₂ split is a special case of a more general structural/behavioral split that the single-channel pattern forces**, and it appears on the action-out side as a *structural-bounded-signaling-certificate* (available iff no goal-correlated off-action emission) vs *behavioral-bounded-signaling* (otherwise), discontinuous in certifiability exactly as W₁/W₂ is. **Q3: yes, the recurrence is exact**, including the certifiability-discontinuity character.

This also re-frames `#disc-adversarial-coupling-pressure`'s bounded-signaling treatment: that segment notes the assumption "fails operationally" against capable adversarial inferrers and that this is *why* the bias bound's $C$ becomes adversarially-tight. In the present language: the adversary is the entity that *forces the action side past its $\varepsilon=0$ certificate* by reading the off-action behavioral channel — the action-side dual of a stateful component that forces W₁ past (C2′). The adversarial-coupling-pressure saturation case is the action-side $\varepsilon\gt 0$ regime made hostile.

---

## 5. Where the duality breaks — and why the break is the result, not a defect

Strengthen-first demands the maximally-ambitious form be attempted: *one theorem, a conserved goal-budget, specializing to both conditions.* It does **not** hold, and the precise break is worth more than a forced unification would be. Three asymmetries, in increasing depth:

**(B1) Different goal variables, different targets — no conserved total.** The belief side carries the *operator's* latent goal $G^{\text{op}}$ to the *wrapper's belief*; the action side carries the *agent's own* goal $G_t$ to an *external observer's inference*. These are not two flows of one substance across one cut — they are two distinct (source, target) pairs that merely *share a structural template*. A conservation law needs a single conserved quantity flowing through a cut; there is none here. Goal-information is moreover *copyable* (Shannon information is not flow-conserved like mass), so even within one side "what leaks here cannot leak there" fails. **This kills the "budget/conservation" framing as a quantity** and is the main reason §3 lands the invariant as a *pattern*, not a law. (Answer to Q2: the unifying object is a shared template, not a conservation law. The strong form is *refuted*, cleanly.)

**(B2) The designated channel is legitimate-but-blind on one side, legitimate-and-used on the other.** On the belief side, the designated channel $q_M$ is required to be *goal-blind by selection* — the goal-content in $q_M$ is a *leak to be minimized*, and the ideal is $I(q_M; G^{\text{op}})=0$. On the action side, the designated channel $a_t$ is the channel through which the agent *legitimately and necessarily acts on its goal* — the goal-content in $a_t$ is *the point of acting*, not a leak; $I(a_t; G_t)=0$ would mean the agent's actions are goal-independent (no agency). So the two "designated channels" have opposite normative status: $q_M$ should be goal-empty, $a_t$ should be goal-full. The DPI bound is identical, but *what the designer wants the channel to carry* is reversed along with the flow direction. This is a refinement of the duality, not a break of it — but it shows the duality is a reflection that *also flips the sign of desirability*, which a naive "same condition twice" reading would miss.

**(B3) Observability of the off-channel differs in locus, and this is the deepest asymmetry.** The belief-side off-channel $S$ is *inside the black-box component* — below the wrapper's query port, unobservable because the wrapper has no access to component internals. The action-side off-channel $B_t$ is *outside the agent's action port* — in the agent's full physical/textual emission, "unobservable" only in the sense that *the formalism does not model it*, but in fact **fully observable to a sufficiently capable external party** (that is exactly what the adversarial inferrer in `#disc-adversarial-coupling-pressure` exploits). So the two "unobservable bypasses" are unobservable to *different parties*: $S$ is unobservable to the *wrapper/designer*; $B_t$ is unobservable to the *formalism* but the *adversary sees it fine*. This asymmetry is load-bearing: it explains why the belief-side failure is a *certification* problem (the designer cannot prove the bound) while the action-side failure is an *exploitation* problem (an adversary can actively read and weaponize the leak). The certifiability discontinuity is the same shape (§4), but its *consequence* differs — lost proof vs opened attack surface.

**Net.** The strong form (single conserved budget, one theorem) is **refuted** by (B1). The duality that *does* hold is the single-channel-leakage *pattern* of §3 with the certifiability/behavioral split of §4 — real, structural, and reflected-with-sign-flips across the wrapper boundary (B2, B3). This is the honest landing: a genuine partial duality with three named asymmetries, the most consequential being (B3)'s locus-of-unobservability difference. Per integration-is-replacement, the negative on the strong form *is* present truth and is demonstrated here, not softened away.

---

## 6. What this licenses, and where it would land (math-lives-in-segments)

If the gate finds this worth landing, it is a *recognition* result at `discussion-grade` — a shared structural pattern plus a previously-unstated action-side scope condition — not a new derivation (the DPI is already in canon, twice). Two concrete, separable moves:

**Move A — promote the action-side scope condition to a named, first-class condition mirroring (C2′).** `#der-directed-separation` §Discussion "Bounded-signaling" and `#disc-adversarial-coupling-pressure` §Scope both currently state bounded-signaling as an *implicit assumption surfaced in prose*. The duality licenses stating it as a *structural scope condition with a certificate*, in the same shape as (C2′):

> **(BS) No goal-correlated off-action emission.** The agent's externally-observable emission carries no goal-content beyond the action $a_t$. Equivalently, $\hat G_t$ (any observer's goal-inference) is conditionally independent of $G_t$ given $a_t$: $G_t\to a_t\to\hat G_t$ is a Markov chain. Under (BS), $I(\hat G_t; G_t)\le I(a_t; G_t)\le\log\lvert\mathcal A\rvert$ is a *structural* bound certifiable from the action interface; when (BS) fails (rich behavioral side-channel), only a *behavioral* bound remains — the certifiability discontinuity of `#disc-w1-structural-bound-boundary`, on the output side.

This is the exact action-side transcription of (C2′)+the W₁/W₂ split. It makes the framework's two goal-flow boundary conditions *parallel and explicit* rather than one-named-one-implicit.

**Move B — a short cross-linking recognition.** A `disc-` paragraph (candidate home: extend `#disc-w1-structural-bound-boundary` §Discussion "Relation to the action-side bounded-signaling assumption", which currently says only *"Whether they are the same phenomenon viewed from two sides is left open"* — this spike closes that open item) stating the §3 single-channel pattern, the §4 recurrence of the certifiability/behavioral split on both sides, and the §5 asymmetries (especially (B3): designer-unobservable $S$ inbound = *certification* problem; adversary-observable $B_t$ outbound = *exploitation* problem). The honest tier is `discussion-grade` (a structural recognition), with the DPI specializations themselves being `exact` (they are just the DPI).

**What must NOT be written** (per integration-is-replacement / voice-discipline): no "goal-information conservation law," no "budget that sums to a constant" — (B1) refutes that, and writing it would be the inflation failure. The body should state the pattern and the *three asymmetries* as present truth; the "we considered and rejected a conservation framing" reasoning belongs here in the spike (history layer), not in any segment body.

**Meta-Architecture note.** The single-channel pattern is plausibly an M-series facet candidate (it is a cross-cutting structural recognition about *what makes a goal-leakage bound certifiable*), kin to the certifiability/modal reading already connected to `#disc-identifiability-floor` (M1). Whether it rises to a meta-segment or stays a `disc-` recognition is a gate/Joseph call — flagged, not decided.

---

## 7. Verdict

**The conjecture holds, partially and precisely.**

- **Q1 (real or surface?)** — **Real.** Five of six structural slots identical; the bound mechanism is the *same theorem* (DPI along a single-channel Markov chain, broken by an unobservable bypass), reflected across the wrapper boundary with goal-flow direction reversed. Canon already half-states it ("symmetrically …"). §1–§2.
- **Q2 (unifying invariant / conservation?)** — **A unifying *pattern*, yes; a conservation *law*, no.** The single-channel goal-leakage pattern (§3) genuinely specializes to both. The "budget/conservation" strengthening is **refuted** (§5 B1): two different goal variables, two targets, copyable information — no conserved quantity through a cut. The honest object is a shared structural template, not a flow law.
- **Q3 (certifiability-vs-behavioral recurs on the action side?)** — **Yes, exactly**, including the certifiability-discontinuity character: a *structural bounded-signaling certificate* (action-only emission) vs *behavioral-bounded-signaling* (rich side-channel), discontinuous in certifiability as $\varepsilon\to 0^+$, transcribing W₁/W₂ to the output side (§4). The adversarial-coupling-pressure saturation case is the action-side $\varepsilon\gt0$-made-hostile regime.
- **Q4 (what it licenses / where it lands?)** — A `discussion-grade` recognition: (A) promote bounded-signaling to a named structural scope condition **(BS)** mirroring (C2′), with its structural-vs-behavioral certificate; (B) a cross-linking paragraph closing the open item in `#disc-w1-structural-bound-boundary` §Discussion. *No* conservation-law language. §6.

**The break is the most informative part.** The three asymmetries (§5) — different goal-variable/target pairs (kills conservation), opposite normative status of the designated channel (goal-blind query vs goal-full action), and the locus-of-unobservability difference (inside-the-box $S$ unobservable to the *designer* → certification problem; outside-the-port $B_t$ unobservable to the *formalism* but seen by the *adversary* → exploitation problem) — are what make this a duality worth naming rather than a tautology. (B3) in particular explains *why* the belief-side story is about lost proofs and the action-side story is about opened attack surface, even though the underlying DPI is identical.

**Confidence.** High on the structural duality and the DPI-pattern (§1–§3): it is elementary once both sides are written in one notation, and canon already gestures at it. High on the §4 recurrence: it is a direct transcription of the already-derived `#disc-w1-structural-bound-boundary` argument with $q_M\to a_t$, $S\to B_t$, and the certifiability-discontinuity logic is identical. High on the §5 refutation of the conservation form: (B1) is decisive (no conserved quantity exists). Medium-high on the (BS) condition being worth landing as first-class: it is a clean, true, useful parallel, but whether it earns a named-condition slot vs staying surfaced prose is a taste/gate call.

---

## 8. What I did not close

- **A quantitative joint statement.** I deliberately did *not* try to write $I(M_W; G^{\text{op}}) + I(\hat G_t; G_t) \le \text{const}$ or any summed bound, because (B1) shows there is no shared conserved quantity to bound. If a *single-side* tighter result is wanted, the open tightness question is the same one the parent spike left open: the gap between $I(A(q_M); G^{\text{op}})$ and the ceiling $I(q_M; G^{\text{op}})$ (the accuracy-vs-inference-effect decomposition, `#der-class-coercion-via-wrapping` §Discussion "Two senses of component competence") — and its action-side analog would be the gap between what an inferrer *recovers* and the ceiling $\log\lvert\mathcal A\rvert$, governed by the inferrer's competence. The two competence-gap questions are themselves dual; not chased here.
- **The amplifying-channel edge, on the action side.** `spike-w1-w2-boundary-intuition-2026-05-31.md` §7 flagged that an *amplifying* cross-call state could break the $\Theta(\varepsilon^2)$ continuity of the belief-side leak. The dual question — whether an *amplifying* behavioral side-channel (e.g. an adversary whose inference *compounds* across a behaviorally-rich interaction) could make the action-side leak super-linear or threshold in $\varepsilon$ — is open and is the natural action-side companion to that M4-amplification thread (`#disc-modularity-state-dynamics`). A toy mirroring `sim-w1-w2-boundary.py` with the channel direction reversed would test it; not built here.
- **Whether (BS) interacts with the composite-inheritance table.** Bounded-signaling is an agent-level / interface-level condition; whether it lifts to composites the way directed separation does (via routing structure + substrate sharing, `#der-directed-separation`) — i.e. whether a composite can have a structural bounded-signaling certificate its components lack, or vice versa (defensive scaffolding that *masks* behavioral side-channels?) — is unexplored and is a plausible bridge to the `#disc-adversarial-coupling-pressure` defensive-scaffolding material.

---

## File index / cross-refs

- This file: `spikes/spike-goal-flow-duality-2026-05-31.md`
- Parent (the §7 conjecture this chases): `spikes/spike-w1-leakage-vacuity-2026-05-31.md`
- Belief-side boundary (the no-go this dualizes): `01-aat-core/src/disc-w1-structural-bound-boundary.md` (its §Discussion "Relation to the action-side bounded-signaling assumption" is the open item §6 Move B would close)
- Action-side source (bounded-signaling): `01-aat-core/src/der-directed-separation.md` §Discussion "Bounded-signaling"; adversarial saturation: `01-aat-core/src/disc-adversarial-coupling-pressure.md` §Scope
- Wrapping construction + (C2′): `01-aat-core/src/der-class-coercion-via-wrapping.md`
- Intuition toys (the certifiability-discontinuity machinery transcribed in §4): `spikes/spike-w1-w2-boundary-intuition-2026-05-31.md` (+ `sim-w1-w2-boundary.py`), `spikes/spike-guc-class-boundaries-intuition-2026-05-31.md`
- No canon edits, no `status:` changes, no git. Promotion (Moves A/B) reserved for the external-eye gate / Joseph.
