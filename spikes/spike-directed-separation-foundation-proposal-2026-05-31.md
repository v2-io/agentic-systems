# Proposal: Re-founding the directed-separation / GUC-class typology — object-and-boundary view, the goal-blind-update noun, and the form-matters guard

**Status.** Canon-change **proposal**, not execution. Read-only on canon — this document proposes; a follow-up agent executes if the lead approves. No `*/src/*.md` edits, no `status:` changes were made by the author of this document.

**Date.** 2026-05-31.

**Kind.** Foundational reframing of `#der-directed-separation` and the GUC Class 1/2/3 typology, plus a new defined noun for results-scoping, plus the integration of the two 2026-05-31 boundary-intuition spikes and the W₁-leakage correction into a single coherent frame.

**Grounded in (read before relying on any specific recommendation):**

- `spikes/spike-guc-class-boundaries-intuition-2026-05-31.md` (Class 1↔2 and Class 2↔3 boundary kinds; `sim_guc_classes.py` / `sim_guc_boundaries.py`).
- `spikes/spike-w1-w2-boundary-intuition-2026-05-31.md` (behaviour-continuous / certifiability-step at the W₁↔W₂ boundary; `sim-w1-w2-boundary.py`).
- `spikes/spike-w1-leakage-vacuity-2026-05-31.md` (the W₁ leakage-bound correction + embedded no-go; verdict (B)+(C), drafted-not-integrated).
- Canon: `#der-directed-separation`, `#disc-partial-coupling-pathways`, `#der-belief-strategy-attractor`, `#def-agent-spectrum`, `#der-class-coercion-via-wrapping`, `#der-orient-cascade` / `#impl-orient-cascade`, `#def-value-object`, `NOTATION.md`, `LEXICON.md` (entries `separated` / `partial` / `coupled` / `directed-separation` / `goal-update-coupling-class`), `doc/naming-principles.md`.

> [!important]
> **What is reserved for Joseph (do not execute these without his ratification).** (1) The **noun choice** itself (this document proposes `goal-blind belief-update` / the noun *belief-blindness*, with two alternatives and the reasoning; the citability/lexicon-coherence call is his). (2) Whether the W₁-leakage correction lands **together with** this reframing or **separately** (recommendation below: *separately, W₁ first*). (3) Any `status:`/tier transition. (4) The placement decision for the new noun's definitional home and for the certifiability-discontinuity no-go (recommended homes given, but they touch the Meta-Architecture cluster and the appendix structure, which are Joseph-gated surfaces). Everything else in the execution spec is mechanical once those four are settled.

---

## Part 0 — The reframing in plain language (mental model first)

Picture a single knob on the side of an agent. The knob controls one thing: **how much the agent's goal is allowed to bend the way it updates its beliefs.** Turn it to zero and the agent is a perfect scientist — it reads the evidence and updates what it believes about the world without letting what it *wants* to be true touch the result. Turn it up and the agent starts to see what it wants to see.

The framework currently tells a three-box story about this knob: Class 1 (Separated), Class 2 (Partial), Class 3 (Coupled). The boxes are real and they are not going away. But told as three boxes, the story invites a reading the framework does not mean and a hostile reader will exploit: *that the boxes are a cleanliness ranking — Class 1 is the virtuous architecture, Class 3 the dirty one, and the whole apparatus is a way of looking down on LLMs.* That reading is wrong, and the two boundary-intuition spikes let us say *why* it is wrong with precision instead of protest.

The corrected mental model has two layers that compose.

**The object view (one knob, three positions, and the special status of zero).** There is one coupling — goal into belief-update — and the three classes are positions of that one knob: Class 1 is the knob *welded* at zero; Class 2 is the knob at some small setting; Class 3 is the knob turned up so far that the goal is just injected into the belief. The thing that makes Class 1 special is **not** that its knob value is the best one. It is that in a Class 1 agent *there is no knob* — the goal is not an argument to the belief-update at all, so its value is provably, perturbation-stably zero. Class 1 is "Class 2 welded at zero, by construction." This is the anti-cleanliness-ranking point stated structurally: Classes 1–3 are positions of one coupling distinguished by **what you can certify about the knob**, not by virtue. And it is defensible-not-circular precisely because the welded-zero is a *provable fact about the wiring* (the belief-update has no goal port), not a decree.

**The boundary view (the two boundaries are different kinds of thing).** Walk from Class 1 to Class 2 and you cross a boundary where *nothing about the agent's behaviour changes* — a Class 2 agent with its knob at zero is bit-for-bit identical to a Class 1 agent in everything you could ever measure. What changes is whether you can hand someone a **certificate** that says "this agent's beliefs cannot be bent by its goals." Class 1 can; Class 2-at-zero cannot (its knob could move). **Boundary 1 is where the certificate disappears.** Now walk from Class 2 to Class 3. Here behaviour *does* change, and sharply: in Class 2 the leak is self-limiting — an adversary pushing a wilder and wilder goal at the agent moves its beliefs barely at all — but at Class 3 the leak tracks the adversary's goal one-for-one. The bound on how far you can be dragged goes from "essentially flat" to "as far as the adversary likes." **Boundary 2 is where the bound disappears.** One boundary is invisible-to-behaviour and visible-only-in-the-wiring; the other is the opposite. (Both spikes, derived independently, agree on this.)

**Why this matters for the math (the noun).** Once you see that Class 1 = "welded-zero + a certificate," a precise question falls out: *which downstream results actually need the certificate, and which only need the zero?* The honest answer is **almost none of them need the certificate** — Part II's results that are stated "for Separated agents" depend mathematically on the **fact** that the goal does not enter the belief-update ($\kappa = 0$), not on the *provability* of that fact. A behaviourally-idealized Class 2 agent sitting exactly at $\kappa = 0$ satisfies every one of those results, because the math integrates over the belief-update dynamics and those dynamics are identical. So the framework needs a **noun for the object "$\kappa = 0$ in behaviour"** — the thing both a Class 1 agent and an idealized-Class-2-at-zero agent *are* — so results can be scoped to *it* rather than to "Class 1," which silently over-narrows them to the certifiable case. The noun's job is **not aspirational and not normative**; it is **bookkeeping for mathematical facts**: a result that depends only on $\kappa = 0$ holds for the noun, full stop, and the certificate is a *separate axis* that buys you the *guarantee that you are at the noun*, not the result.

**And the guard against over-correcting.** Having unified the knob, the tempting next move is to make the *whole* typology one scalar — "it's all just $\kappa$, turned up by degrees." That is the *opposite* error and it is also false. Boundary 2 is not "the same knob turned up"; the coupling *changes character* there. And inside Class 2 the **form** of the coupling matters in a way no scalar captures: content-form coupling *injects* the goal (so it leaks badly under adversarial pressure, but a fixed debiaser can subtract it — W₂-wrappable); process-form coupling only *re-weights* the evidence that arrives (so it is pressure-insensitive, but a debiaser cannot remove it — needs W₁). Pressure-sensitivity and wrappability are *orthogonal axes*, so a single magnitude underdetermines both an agent's adversarial signature and its repair regime. The unification is clean for the 1↔2 boundary (one coupling; Class 1 = its certifiable zero); it must **not** be smeared across the 2↔3 boundary or used to collapse the form axis.

That is the whole reframing. The rest of this document is the precise structure and the per-segment execution spec.

---

## Part 1 — The structural frame, precisely

### 1.1 The object: one coupling, the classes as positions, Class 1 as the certifiable-by-construction zero

The single coupling is $G_t \to f_M$ (goal-state into the belief-update map), measured **as realized** by $\kappa_{\text{processing}} = I(G_t; M_{\tau^+} \mid e_\tau, M_{\tau^-}) / H(G_t \mid e_\tau, M_{\tau^-})$ (already in `#der-directed-separation`). The three classes are positions of this coupling, distinguished by **what is certifiable about it**, not by the value alone:

- **Class 1 (Separated).** The belief-update has *no goal argument* — the coupling channel is structurally absent. $\kappa \equiv 0$ is therefore a **provable, perturbation-stable property of the wiring**: there is no port through which a perturbation could open the channel. This is the affordance that lets you *certify* the zero by architecture inspection. (Spike `guc-class-boundaries` §1, §2: `certifiable_separation()` decides by reading whether `update` takes a goal argument, not by measuring behaviour.)
- **Class 2 (Partial).** The channel exists but carries bounded coupling; $\kappa \in (0, \kappa_{\max})$ as realized, and the bound is *behavioural / distribution-dependent*, not structural.
- **Class 3 (Coupled).** The channel is the architecture; the goal is upstream of every belief computation, $\kappa \to$ its ceiling.

The load-bearing reframing sentence (which the current intro *gestures at* but does not state cleanly): **Class 1 is not a separate or superior *kind* of agent — it is the position $\kappa = 0$ together with a construction-side certificate that the position is held stably. The classes index *what you can certify about one coupling*, not a hierarchy of architectural virtue.** The κ≡0 being *provable from the wiring* (no goal port) is what makes "a certificate, not a virtue" defensible rather than circular — the framework is not *decreeing* that Class 1 is clean; it is *reading off* from the type signature that the channel is absent.

### 1.2 The two boundaries — different kinds (the composed boundary view)

| | Boundary 1 (Class 1 ↔ Class 2) | Boundary 2 (Class 2 ↔ Class 3) |
|---|---|---|
| **Kind** | **Certifiability** boundary | **Behavioural** boundary |
| **What changes** | The *certificate* (architecture-inspection guarantee that $\kappa \equiv 0$). True for Class 1, unavailable for Class 2-at-zero. | The *bound* (adversarial-pressure slope of the leak). Self-limiting in Class 2 ($\approx 0$ slope), goes trivial at Class 3 ($\approx \kappa$ slope). |
| **Behaviour at the limit** | **Identical** — a Class 2 agent at $\kappa = 0$ is bit-for-bit indistinguishable from Class 1 in every measurable quantity. | **Different** — same nominal bias, opposite response to adversarial pressure (matched-bias crux pair: slope $0.0003$ vs $0.33$). |
| **How you detect it** | Only by inspecting the wiring (is there a goal port in the belief-update?). No amount of behavioural probing can certify Class 1. | By behavioural probing under adversarial pressure (lean on the goal, watch the belief-error grow). |
| **Crisp gloss** | *Boundary 1 is where the certificate disappears.* | *Boundary 2 is where the bound disappears.* |

The object view and the boundary view **compose**: one coupling (object) whose three positions are separated by two boundaries of different kind (boundary). The "$\kappa$-as-a-scalar is a category error" claim, which canon already makes, gets *sharpened* into **two distinct errors at the two boundaries** (spike `guc-class-boundaries` §5): at Boundary 1 the scalar misses a **certifiability/modal** distinction (same number, different guarantee); at Boundary 2 it misses a **structural** distinction (the form + pressure-response axes a magnitude projects away).

### 1.3 The guard: do not collapse to one scalar (form matters)

The clean part of the unification — one coupling, Class 1 = its certifiable zero — must be stated **without** licensing the reverse over-correction: that the *whole* typology is one scalar dialed up by degrees. Two facts block that:

1. **Boundary 2 is a change of kind, not of magnitude.** The Class 3 coupling injects a $\kappa$-fraction of *any* goal (linear pass-through of a convex blend); the bound goes trivial. This is not "Class 2 with the knob turned up" — the *response to pressure* changes character. (Spike `guc-class-boundaries` §3.)
2. **Form is orthogonal to magnitude (and to pressure-sensitivity).** Within Class 2, content-form (additive injection) leaks proportionally under adversarial pressure *but* is linearly debiasable (W₂); process-form (gain modulation) is pressure-insensitive *but* not linearly debiasable (needs W₁). Adversarial-sensitivity ⊥ wrappability — independently reproduced by the spike, corroborating the canon's existing form-determines-wrappability cut in `#disc-partial-coupling-pathways`. A scalar underdetermines both. (Spike `guc-class-boundaries` §4.)

So the canon must carry an explicit **anti-scalar-collapse guard** alongside the anti-normative framing: *the 1↔2 unification is "one coupling, certifiable zero at one end"; it is not a license to read the 2↔3 boundary or the form axis as more-of-the-same.*

---

## Part 2 — The noun

### 2.1 What the noun is *for*

Joseph's keystone requirement: a defined **noun** for the object that is **$\kappa = 0$ (belief-update goal-blind in behaviour)** — achieved **by construction** (Class 1, certifiable) **or effectively** (a behaviourally-idealized Class 2 sitting at $\kappa = 0$, not certifiable). The noun's purpose is **mathematical-fact propagation**, not aspiration:

> A result whose derivation depends only on $\kappa = 0$ (i.e. on the belief-update dynamics being goal-blind) holds for **the noun** — both Class 1 and idealized-Class-2-at-zero — *because the math depends on the zero, not on the certificate.* Certifiability is a separate axis.

This is the fix for a real present defect. The current `#der-directed-separation` says "Class 1 (Separated): Part II's results apply exactly," and the LEXICON `separated` entry says goal-blind-by-construction "is the property that makes Part II's theoretical results applicable without further qualification." Read strictly, both attach the result to **Class 1 (the certified case)**, which **over-narrows** results whose mathematical content covers the whole noun (Class 1 *and* idealized Class 2 at zero). `#def-value-object` is the cleanest live witness: it says $Q_O$'s $G_t$-independence "holds exactly … under directed separation … exact for Class 1 (Separated) agents; degraded for Class 3 (Coupled) agents" — but mathematically the exactness is purchased by $\kappa = 0$, which an idealized Class 2 at zero also has. The certificate is not in the proof; only the zero is.

### 2.2 The recommended noun

**Recommended: the noun is `goal-blind belief-update`, and the property it names is *belief-blindness* (a belief-blind agent / the belief-blindness condition $\kappa = 0$).**

- **Slug-layer / structural identifier:** the *condition* $\kappa = 0$ is the **belief-blindness condition**; an agent (Class 1 or idealized-Class-2-at-zero) satisfying it is **belief-blind**; the property is **belief-blindness**.
- **Prose handle:** "for belief-blind agents," "the belief-blind locus $\kappa = 0$," "this result needs only belief-blindness, not the Separated certificate."

Rationale against `doc/naming-principles.md`:

- **Subject-noun-first (architectural invariant).** Names the *thing* — the agent whose belief-update is blind to its goal — not a role. Passes.
- **Reconciles with existing vocabulary without collision.** "Directed separation" is the *asymmetric-information-flow condition*; "Separated / Class 1" is the *certifiable-by-construction* position. **Belief-blindness is the behavioural fact $\kappa = 0$ that both Class 1 and idealized-Class-2-at-zero share.** It slots *between* "directed separation" (the architectural condition) and "$\kappa = 0$" (the bare scalar value), naming the result-bearing object explicitly. The existing prose already uses "goal-blind" constantly for $f_M$ (it is the canonical adjective in `#der-directed-separation`'s opening sentence and throughout) — so "belief-blind" / "belief-blindness" is *excavated* from native prose (a **canonicalize**-provenance signal, per naming-principles §"Rename vs. Canonicalize"), not coined cold. The noun is "the property the prose keeps reaching for, promoted to a named result-scoping object."
- **Standalone citability (Crit-9).** "Belief-blindness" / "belief-blind agent" is reasonably distinctive — it does not collide with a standard ML term the way "bias bound" does. It is *paired* with "directed separation" and "goal-blind," which strengthens travel (the *paired-vocabulary* route to citability the principles name). Honest caveat: "blind" carries mild metaphor baggage (blindness-as-deficit) that could read as the very normative cleanliness we are trying to *avoid* — flagged for Joseph in §2.4.
- **Lexicon-coherence.** It composes cleanly with the live vocabulary: *directed separation* (condition) → *belief-blindness / belief-blind agent* (the $\kappa=0$ object, result-bearing) → *Separated / Class 1* (belief-blind **+ certificate**) → *Partial / Class 2* (bounded $\kappa$ + $\varepsilon$-degradation) → *Coupled / Class 3* (channel-is-the-architecture). The noun fills the empty slot in that ladder.
- **Scope honesty.** Does not over-promise: it claims exactly "belief-update is blind to goal," which is what $\kappa = 0$ *is*.

### 2.3 Alternatives considered (and why not chosen)

1. **The bare-scalar name ($\kappa$-null agent / the "$\kappa = 0$ locus").** *Rejected as the primary noun.* It is precise and collision-free, but it fails memorable-noun-potential and the communal-imagination test — it is "a sequence of subscripts" of exactly the kind `doc/naming-principles.md` warns against (the "A2' sub-scope" anti-example). It is, however, the right *structural identifier in the formalism* — so the recommendation keeps "$\kappa = 0$" as the symbol and adds "belief-blindness" as the English handle, an **add-alias** pairing (symbol-to-English), which is the canonical move for exactly this situation. Use both: "$\kappa = 0$" in the math, "belief-blind" in prose.

2. **`epistemically separated` / `epistemic separation`.** *Rejected — collision risk with "directed separation."* It reads as a near-synonym of the existing backbone term and would blur the very distinction the noun exists to make sharp (condition vs. result-bearing-object vs. certified-position). The whole point is that the noun is *not* "Separated" (the certified position) and *not* a restatement of "directed separation" (the condition). A name that sounds like either defeats its purpose.

Belief-blindness wins on: native-prose provenance (canonicalize signal), filling an empty ladder slot without collision, and stating the behavioural fact rather than the architecture. Its one liability (the "blind = deficit" metaphor) is the reason the noun choice is reserved for Joseph rather than asserted.

### 2.4 The noun's definitional home and the scoping rule

**Home (recommended):** define belief-blindness **inside `#der-directed-separation`**, in a short new subsection immediately after the architectural-classification table, *before* the "Implications for theory scope" block — because the scoping rule that follows is exactly what the implications block should then use. Do **not** create a separate segment for it; per the prior-art-integration / no-orphaned-document discipline, a foundational scoping noun belongs in the spine segment that introduces the classes, not in a satellite. (The certifiability-discontinuity *no-go* is a different matter — see Part 4 — because it is a non-obvious result that earns its own demonstration.)

**The scoping rule (the load-bearing content of the noun), to state in the definitional subsection and apply in the implications block:**

> **Belief-blindness** is the condition $\kappa_{\text{processing}} = 0$ — the belief-update $f_M$ is goal-blind *in behaviour*. A **belief-blind agent** is any agent satisfying it, whether by construction (Class 1: Separated — belief-blind *and certifiable*, the channel structurally absent) or behaviourally (an idealized Class 2 at $\kappa = 0$ — belief-blind but *not certifiable*, the channel present but empty).
>
> **Scoping rule.** A Part II result whose derivation depends only on $\kappa = 0$ holds for **all belief-blind agents** — it does *not* require the Class 1 certificate. State such results "for belief-blind agents (Class 1, or idealized Class 2 at $\kappa = 0$)." Reserve "for Separated / Class 1 agents" for the strictly smaller set of claims that *additionally* require the construction-side guarantee (e.g. adversarial robustness of the separation, or any claim about *certifying* the separation rather than *using* it).
>
> **The $\varepsilon(\kappa)$-degradation norm (stated obligation, not hard requirement).** For the Class 2 ($\kappa \gt 0$) case, a result stated for the belief-blind ($\kappa = 0$) value should — *where provable, which is expected to be many cases* — carry an explicit **$\varepsilon(\kappa)$-degradation bound**: how far the result's quantity moves off its $\kappa = 0$ value as the coupling leaves zero. This is the strengthen-first / explicit-scope-condition discipline applied to result-propagation. It is the **stated norm with the proof attempted**, not a gate: a result lands at the belief-blind value first; the $\varepsilon(\kappa)$ bound is the recommended strengthening, recorded as an open strengthening in Working Notes when not yet proved.

The $\varepsilon(\kappa)$ norm has an existing anchor that makes it concrete and shows it is *already how the framework works*: `#deriv-observation-ambiguity-bias-bound` is exactly an $\varepsilon(\kappa)$-style result for the Class 3 limit (the bias-bound constant $C$ as a function of the coupling/ambiguity), and `#der-belief-strategy-attractor` is an $\varepsilon(\kappa)$-style structural result (the $O$-source bias is the bounded degradation; the $\Sigma$-source attractor is its qualitative breakdown). The norm names the pattern these already instantiate and asks new result-propagations to attempt it.

---

## Part 3 — How the W₁ correction fits, and the land-together-or-separate recommendation

### 3.1 Where the W₁ correction sits in this frame

The W₁-leakage correction (`spike-w1-leakage-vacuity`) is a **Boundary-1-kind (certifiability) finding living *inside* Class 2 / the wrapping construction** — it fits the reframe cleanly and even *exemplifies* it:

- The old bound $\kappa_{W_1} \le I(A(q_M); G_W \mid q_M)$ is circular/vacuous (it bounds $\kappa$ by an average of $\kappa$, and is identically zero for a stateless oracle). The corrected bound is the **selection channel** $\kappa_{W_1}^{\text{sel}} = I(A(q_M); G^{\text{op}}) \le I(q_M; G^{\text{op}})$ via DPI along $G^{\text{op}} \to q_M \to A(q_M)$.
- The embedded **no-go**: the structural W₁ bound exists *iff* condition (C2′) holds (no goal-correlated cross-call state); otherwise only a behavioural (W₂-type) bound remains. The W₁↔W₂ boundary-intuition spike sharpened this to the *honest framing*: it is a **certifiability discontinuity, not a behaviour discontinuity** — the leak is continuous (and $\Theta(\varepsilon^2)$-flat) in the (C2′)-violation; what snaps at the boundary is the *availability of the structural certificate*.

This is the **same shape** as Boundary 1 at the class level: *behaviour continuous, certificate a step.* The W₁↔W₂ boundary is the wrapping-construction instance of the Class-1↔2 certifiability boundary. That is a genuinely unifying recognition the reframe surfaces — and a reason the two are conceptually one family even though they should land as separate execution batches.

### 3.2 Recommendation: land the W₁ correction **separately, and first**

**Recommended: W₁ correction lands first as its own cycle; the foundational reframing lands second, citing the now-landed W₁ certifiability-discontinuity as the wrapping-level instance of Boundary 1.** Reasoning:

- **They are different scopes and different risk.** The W₁ correction is a *correctness fix* to a load-bearing construction (a circular bound must be replaced regardless of the reframe). The reframing is a *foundational re-presentation* (no result changes; framing + a new noun + scoping discipline). Bundling a correctness fix with a foundational re-presentation muddies the git seam and the review — the lead should be able to review "is the corrected bound right?" without simultaneously adjudicating "is belief-blindness the right noun?"
- **Pre-spike commit hygiene (memory: `feedback_commit_before_canon_modifying_spike`).** The W₁ fix touches `#der-class-coercion-via-wrapping`'s Theorem 2 and the regime table; committing it as its own seam isolates that diff for review/revert/attribution before the larger reframe perturbs `#der-directed-separation`.
- **Dependency direction favors W₁-first.** The reframing's certifiability-discontinuity framing (Part 1.2 / Part 4) is *strengthened* by pointing at an already-landed concrete instance (the W₁↔W₂ no-go) rather than forward-referencing an unlanded one. If the reframe lands first, it forward-references; if W₁ lands first, the reframe back-references a concrete result. Back-reference is cleaner.
- **Both are Joseph-gated regardless.** Each is a reserved decision; sequencing them does not add gates, it just orders two gates that already exist.

**The minority case for together** (recorded honestly): both turn on the *same* recognition — certifiability is a step while behaviour is continuous — and landing them together lets the canon state that recognition *once*, at the class level, with W₁ as a worked instance, avoiding a two-place statement. If the lead prefers a single coherent "certifiability vs behaviour" landing, together is defensible — but then sequence the *commits* within it: W₁ correctness fix first commit, reframe second commit, even inside one cycle.

---

## Part 4 — Per-segment execution spec (independently executable)

Direction + load-bearing sentences below; **not** necessarily final prose. The executor writes in segment-voice (present-truth, no diff-voice in bodies; history → CHANGELOG / Working Notes), runs `bin/lint-md` on every touched file, eyeballs for Unicode-in-backticks, and verifies `bin/lint-outline` is clean. Honest tiers are stated per change. Integration-is-replacement: superseded normative-leaning framing is **deleted from bodies**, not kept-softened-with-a-pointer; the "previously read as a ranking" history goes only to CHANGELOG / Working Notes.

### 4.1 `#der-directed-separation` (the core — primary change)

**(a) Sharpen the class-introduction to the object-and-boundary view — sharpen, do not bolt on.**

The current intro *already leans anti-normative* in places — "The classes are *structural and discrete*, not points on a smooth scalar" and "the κ-as-scalar framing is a category error" (the latter from `CLAUDE.md`'s Key Architectural Decision 5). So this is a **minimal truthful sharpening**, not a rewrite. Honest read of the current intro: it establishes discreteness and structure well, but it does **not** state (i) that the classes are positions of *one* coupling distinguished by *certifiability* (the reader can still come away with a cleanliness-ranking reading), nor (ii) that Class 1 is "the certifiable-by-construction zero" rather than a separate kind. The "Why the classification is not a smooth parameter" paragraph argues discreteness from "the architectural boundary is discrete" — true but it under-sells *what kind* of discreteness.

- Add, near the top of the architectural-classification subsection, the **object view** sentence (Part 1.1): *"The three classes are positions of a single coupling $G_t \to f_M$, distinguished by what is certifiable about it, not by a ranking of architectural virtue. Class 1 is not a different kind of agent: it is the position $\kappa = 0$ held by construction (the belief-update has no goal port), which is what lets the zero be certified by inspecting the wiring. The $\kappa \equiv 0$ is provable from the architecture, not decreed — that is what makes 'a certificate, not a virtue' a structural fact rather than a value judgment."* Tier: this is *robust qualitative* framing of an existing structural classification — no new result; it states what the classification already means.
- Sharpen the "Why the classification is not a smooth parameter" paragraph into the **two-boundaries-different-kinds** statement (Part 1.2 table), using the spike's two-distinct-errors characterization: *Boundary 1 (Class 1↔2) is a certifiability boundary — behaviour identical at the limit, the certificate flips; Boundary 2 (Class 2↔3) is a behavioural boundary — the adversarial-pressure bound goes from self-limiting to trivial. The category error is therefore two distinct errors: at Boundary 1 the scalar misses a certifiability/modal distinction; at Boundary 2 a structural (form + pressure-response) distinction.* Tier: *robust qualitative* (the adversarial-slope discriminator is the linear pass-through of a convex blend — established machinery, not a new theorem; the two-error characterization is framing). Cite the boundary-intuition spike in Working Notes only (spike-references-only-in-Working-Notes discipline).
- Add the **anti-scalar-collapse guard** (Part 1.3) as one sentence in the same paragraph: *the one-coupling unification is clean for the 1↔2 boundary; it is not a license to read the 2↔3 boundary or the (content/process) form axis as the same knob turned up — Boundary 2 changes the coupling's character, and form is orthogonal to magnitude (`#disc-partial-coupling-pathways`).*

**(b) Define belief-blindness + the scoping rule (Part 2.4) in a new subsection after the classification table, before "Implications for theory scope."** Tier: *definitional* for the noun; the scoping rule is a *robust qualitative* discipline (it states how results propagate; it does not itself derive a result). Include the $\varepsilon(\kappa)$-degradation norm with the `#deriv-observation-ambiguity-bias-bound` / `#der-belief-strategy-attractor` anchors as existing instances.

**(c) Re-scope the "Implications for theory scope" block to the noun.** Change "Class 1 (Separated): Part II's results apply exactly" → "Belief-blind agents (Class 1, or idealized Class 2 at $\kappa = 0$): Part II's results that depend only on $\kappa = 0$ apply exactly; the Class 1 certificate is additionally required only for claims about *certifying* the separation or about its adversarial robustness." Keep the Class 3 exit and the wrapping route-through unchanged. Tier: unchanged (the results' own tiers do not move; only the *scope label* is corrected to match the actual mathematical dependency — this is a truth-fix, an over-narrow scope being widened to its real extent).

**(d) Integration-is-replacement bookkeeping.** The history ("the implications block previously attached these results to Class 1, which over-narrowed them") goes to **CHANGELOG + this segment's Working Notes only**, never the body. No "this is not a weakening" sentence in the body — the widened scope is simply stated as present truth.

### 4.2 `#def-value-object` (the cleanest downstream witness — exemplary re-scope)

Currently: $Q_O$'s $G_t$-independence "holds exactly … under directed separation … exact for Class 1 (Separated) agents." Re-scope to: *"exact for belief-blind agents ($\kappa = 0$ — Class 1 or idealized Class 2 at zero); degraded for Class 3 (Coupled) agents where $M_t$ carries goal-conditioned bias; for Class 2 at $\kappa \gt 0$, degraded by an $\varepsilon(\kappa)$ amount (bound: open / cite if proved)."* This is the canonical worked instance of the scoping rule — do it carefully and it becomes the pattern the executor copies to the other downstream segments. Tier: unchanged (scope-label truth-fix). Note: `#def-value-object` *already* distinguishes interventional-interpretation (exact under directed separation) from identifiability-of-estimate (gated on (C1)–(C3)) after the 2026-05-30 spike landing — the belief-blindness re-scope attaches to the *interpretation* leg (the $G_t$-independence), which is the leg that depends on $\kappa = 0$.

### 4.3 Other downstream Section II segments scoped to "Separated / Class 1"

Sweep, applying the scoping rule, the segments where a result is attached to "Class 1 (Separated)" but the proof depends only on $\kappa = 0$: candidates surfaced by grep are `#der-orient-cascade` / `#impl-orient-cascade` (the *sequential resolution* depends on $f_M$ having no causal path from $G_t$ — i.e. on belief-blindness, not on the certificate), `#der-action-selection`, `#deriv-observation-ambiguity-bias-bound` (already an $\varepsilon(\kappa)$ result — confirm its scope language), and the composite-inheritance discussion. **Discipline for the executor:** for each, *read the derivation* and judge honestly whether it uses the certificate or only the zero — do **not** mass-substitute "Separated → belief-blind" mechanically (that would be the unless-clause-as-skip-license error in reverse). Where a result genuinely needs the certificate (adversarial-robustness or certifying claims), leave "Separated / Class 1." Tier: unchanged per segment; this is scope-label correction, judged case by case.

### 4.4 `#disc-partial-coupling-pathways` (form-matters guard — light touch)

Add one sentence to the Discussion making the **orthogonality of pressure-sensitivity and wrappability** explicit as the reason the scalar underdetermines repair regime *and* adversarial signature, citing the corroborating independent reproduction (boundary-intuition spike §4) in Working Notes. The segment already carries form-determines-wrappability; this is a one-line sharpening, not new content. Tier: unchanged (*discussion-grade*).

### 4.5 LEXICON entries (`separated`, `directed-separation`, + new `belief-blindness`)

- **New entry `terminology/entries/belief-blindness.md`** (via `bin/term add belief-blindness`; record a `canonicalize` decision event noting native-prose provenance — "goal-blind" throughout `#der-directed-separation`). Brief: *"The condition $\kappa_{\text{processing}} = 0$ — belief-update goal-blind in behaviour — shared by Class 1 (by construction, certifiable) and an idealized Class 2 at zero (not certifiable); the object Part II results scope to when they depend only on $\kappa = 0$, not on the Class 1 certificate."* `see_also`: directed-separation, separated, partial, goal-update-coupling-class. Layer: framing-vocabulary.
- **Edit `separated.md`:** the sentence "This is the property that makes Part II's theoretical results applicable without further qualification" is the LEXICON-level instance of the over-narrowing. Correct to: *"What distinguishes Class 1 is the **certificate** — the belief-update is architecturally forbidden from reading the goal, so $\kappa = 0$ is provable by inspection. Part II's results that depend only on $\kappa = 0$ apply to any belief-blind agent (see belief-blindness); the certificate additionally guarantees the zero is held stably."*
- **Edit `directed-separation.md`:** add a `see_also` to belief-blindness; no body change needed (it already names the condition correctly).
- Re-render `LEXICON.md` via `bin/term render`; `bin/term lint`.

### 4.6 `NOTATION.md`

The $f_M$ row already notes "Separated ($f_X^M = f_M$, no causal path from $G_t$) under directed separation in Class 1." Add a half-sentence: *"the condition $\kappa = 0$ (belief-blindness) is shared by Class 1 and idealized Class 2 at zero; Part II results scope to it, not to the Class 1 certificate."* Per the NOTATION drift caveat, keep it a locator pointer, not a definition. Tier: n/a (index).

### 4.7 Meta-Architecture cross-references (Joseph-gated surface — propose, do not execute)

The certifiability/modal framing is M1-adjacent (`#disc-identifiability-floor` — a certificate that *cannot* be obtained from behavioural data is a floor-shaped fact) and the dynamics-on-class framing is M4 (`#disc-modularity-state-dynamics`). The boundary-intuition spike §8 recommends a cross-reference from M1/M2. **Recommendation:** add a one-line cross-reference from `#der-directed-separation`'s new boundary paragraph to M1 (certifiability-as-modal-fact) and note the belief-blindness/Class-1 distinction as the agent-level shadow of M4's modularity-as-contested-property — but treat the *content* placement in the Meta-Architecture cluster as reserved for Joseph (it touches the Part-opening meta-segment structure he is actively curating).

### 4.8 The W₁-correction landing (separate cycle — spec already drafted)

If landed separately-and-first per Part 3.2, execute `spike-w1-leakage-vacuity` §6 as drafted: new condition (C2′); replace the Theorem-2 / W₁-row leakage bound with $\kappa_{W_1}^{\text{sel}} = I(A(q_M); G^{\text{op}}) \le I(q_M; G^{\text{op}})$; author the certifiability-discontinuity no-go (candidate slug `disc-w1-structural-bound-boundary`, or fold into `#disc-partial-coupling-pathways`) framed per the W₁↔W₂ boundary-intuition spike §7 as *"the structural certificate is available iff (C2′) holds; the leakage it would bound is continuous (and $\Theta(\varepsilon^2)$-flat) in the (C2′)-violation, so the discontinuity is in what is provable, not in what the agent does."* Tier: corrected bound *conditional* on (C1)+(C2′); the no-go *robust qualitative* (the spike notes the toy is suggestive-not-proof for full generality). History (the circular/vacuous prior bound) → CHANGELOG + spike + Working Notes only.

### 4.9 INDEX line

Add a line to `spikes/INDEX.md` for this proposal under a `2026-05-31` heading, marked **PROPOSAL — NO CANON EDITS, pending lead review + Joseph gates** (noun choice / land-together-or-separate / tiers / Meta-Architecture placement), pointing at this file and naming the three grounding spikes.

---

## Part 5 — Decisions surfaced for Joseph (the gate list)

1. **The noun.** *belief-blindness* / *belief-blind agent* (recommended), vs *$\kappa$-null* (precise but unmemorable — recommended *only* as the paired symbol-handle), vs *epistemic separation* (rejected, collision). The one liability of the recommendation: "blind" carries a deficit metaphor that could re-import the cleanliness-ranking connotation we are removing. Your call on whether that liability outweighs the native-prose-provenance and ladder-fit strengths.
2. **W₁ correction: together or separate.** Recommended separate-and-first (correctness fix isolated from foundational re-presentation; back-reference cleaner than forward-reference; commit-hygiene). Minority case for together if you prefer a single "certifiability vs behaviour" statement.
3. **Tiers.** All re-scopes are *scope-label truth-fixes* (results' own tiers unchanged). The new framing is *robust qualitative*; the noun is *definitional*; the scoping rule and $\varepsilon(\kappa)$ norm are *robust qualitative* disciplines. Confirm.
4. **Meta-Architecture placement.** Whether the certifiability/modal framing gets cross-referenced into M1 and the agent-level/M4 shadow noted — content placement in the actively-curated Meta-Architecture cluster is yours.
5. **$\varepsilon(\kappa)$ norm strength.** Confirmed as *stated norm with proof attempted*, not a hard requirement (per your framing). Confirm the wording lands it as discipline, not gate.

---

## Part 6 — Honest confidence, and where this could be wrong or over-reaching

**Confidence: high** on the structural diagnosis (the two boundaries are different kinds; Class 1 = certifiable-zero, not a virtue; the noun gap is real and the over-narrowing is a live defect in `#def-value-object` and the `separated` LEXICON entry). Both spikes derived the boundary-kinds independently and agree; the over-narrowing is visible in canon text, not inferred.

**Confidence: high** that the *anti-normative reframing is the right move and is a sharpening of what is already there*, not a bolt-on — the intro already says "category error" and "not a smooth scalar"; we are completing the thought, not reversing it.

**Confidence: medium-high** on the **noun choice specifically.** The *need* for a noun is high-confidence; the *name* is a genuine aesthetic-and-citability judgment (hence reserved). "Belief-blind" could read as deficit-framing — the exact normative connotation we are removing from the class typology — which would be a small self-inflicted irony. A reader who hears "belief-blind" as "impaired" rather than "goal-insulated" is the failure mode.

**Where the reframing could be *wrong* or over-reaching — three honest edges:**

1. **The noun could be a distinction without a downstream difference.** The whole justification is that results scoped "for Separated agents" over-narrow when they only need $\kappa = 0$. I verified this is *true in the text* (the labels attach to Class 1) and *true mathematically* for the cleanest case (`#def-value-object`'s $G_t$-independence is a $\kappa=0$ fact). But I did **not** exhaustively re-derive every Section II "Separated" result to confirm that *many* of them genuinely need only the zero — §4.3 explicitly hands that case-by-case reading to the executor. **If it turns out almost every load-bearing result genuinely needs the certificate** (e.g. because adversarial robustness is implicitly assumed), the noun is technically correct but operationally near-empty — it would partition a set with one important element. My belief (medium-high) is that the cascade-ordering, $Q_O$-independence, and persistence-lift results need only the zero, so the noun pays off — but this is the place I am most exposed, and it is exactly the place to *strengthen-first*: the executor should attempt the $\varepsilon(\kappa)$ bounds, because a successful $\varepsilon(\kappa)$ bound is *itself* the proof that the result-at-the-noun is the right object (it shows the result degrades continuously off the zero rather than requiring the certificate).
2. **"Certifiability is a step, behaviour is continuous" rests on toy sims, not theorems.** The boundary-intuition spikes are explicitly intuition apparatus (one-bit toys), and the W₁↔W₂ spike flags an *amplification* open edge — a cross-call state that amplifies (controls the gain, or accumulates over many calls) could in principle show threshold/super-linear behaviour, not ruled out. The reframing's *framing* (Boundary 1 invisible-to-behaviour) is robust because it rests on the *exact behavioural-identity-at-the-limit* result (a Class 2 at $\kappa=0$ *is* bit-identical to Class 1 — that part is arithmetic, not toy-suggestive). But any prose that implies "the leak is *always* continuous/flat" past the boundary would over-reach the evidence; the spec keeps the continuity claim attached to the *certificate-validity* step, which is the part that is solid.
3. **The form-matters guard and the unification pull in tension, and the canon has to hold both.** I am asking the canon to say "it's one coupling (so Class 1 isn't superior)" *and* "but don't collapse it to one scalar (form and Boundary 2 matter)." That is the correct and honest position, but it is a *subtle* two-handed message, and subtle two-handed messages are where prose drifts toward whichever hand the writer last touched. The risk is an executor (or a future trimmer) who lands the unification cleanly and lets the guard decay to a parenthetical — re-committing κ-as-scalar from the other direction, which Joseph explicitly named as the error to pre-empt. The spec puts the guard *in the same paragraph* as the unification for exactly this reason, but it is a standing fragility worth naming.

**Net:** the reframing is right and worth doing deeply; the noun is the right *kind* of move with a real naming-judgment call reserved for Joseph; the largest substantive exposure is whether enough downstream results need only the zero (resolvable by the executor's case-by-case reading + the strengthen-first $\varepsilon(\kappa)$ attempts), and the largest *presentation* exposure is keeping the form-matters guard load-bearing rather than letting the clean unification swallow it.

---

## File index / cross-refs

- This file: `spikes/spike-directed-separation-foundation-proposal-2026-05-31.md`
- Grounding spikes: `spikes/spike-guc-class-boundaries-intuition-2026-05-31.md`, `spikes/spike-w1-w2-boundary-intuition-2026-05-31.md`, `spikes/spike-w1-leakage-vacuity-2026-05-31.md`
- Primary segment to change: `01-aat-core/src/der-directed-separation.md`
- Downstream re-scope witnesses: `01-aat-core/src/def-value-object.md`, `der-orient-cascade.md` / `impl-orient-cascade.md`, `deriv-observation-ambiguity-bias-bound.md`, `der-action-selection.md`
- Form-matters guard: `01-aat-core/src/disc-partial-coupling-pathways.md`
- W₁ correction segment: `01-aat-core/src/der-class-coercion-via-wrapping.md`
- Vocabulary: `LEXICON.md` + `terminology/entries/{separated,directed-separation}.md` (+ new `belief-blindness.md`), `NOTATION.md`, `doc/naming-principles.md`
- Meta-Architecture (Joseph-gated): `#disc-identifiability-floor` (M1), `#disc-modularity-state-dynamics` (M4)
