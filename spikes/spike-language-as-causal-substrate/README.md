# Spike — Language as Inherent Causal Substrate

**Status**: Strengthening spike, in progress 2026-05-13. Multi-angle attempt; mixed result.

**Provenance**: Joseph's 2026-05-13 prompt, asking whether the standing plausibility-grade claim that "language has inherent causal structure built in" (currently in `msc/llm-causal-access-note.md` and `ref/agentic-tft/agentic-tft-narrative-as-implementation.md`) can be pushed to derivation-grade. Joseph framed the prompt explicitly in strengthen-before-soften posture: push the math as far as it goes; either it yields, or the no-go tells us what's actually true about the thing.

**Bottom line (as of 2026-05-13, mid-spike)**:

| sub-claim | status | route |
|---|---|---|
| **C1 — Discourse-act encoding (Level 2 content is *in* the text)** | **succeed-at-claim** under {2 postulates + 1 sketch-derived} after `05-slc-derivation-attempt.md` lifted (SLC); audit-clean per `06-cht-application-audit.md` | discourse-act / convention-of-use argument + Bareinboim-Correa-Ibeling-Icard 2022 PCH non-reduction (audit-verified) |
| **C2 — Reichenbachian inheritance (correlation in text ⇒ causal structure in source-thought)** | succeed-at-claim, but **weaker than it sounds** | Reichenbach + faithfulness, modulo Cartwright-style scope conditions |
| **C3 — ICM time-asymmetry** | partial yield — **directional asymmetry derives; quantitative bound has a precisely-specified closure gap** per `07-c3-quantitative-bound-attempt.md` | Janzing-Schölkopf ICM + discourse anaphora structure; quantitative form requires (P3) verification on the directed-information candidate for $\mathcal I_c$ |
| **C4 — Causal-IB consequence (any IB-optimal compressor of natural language preserves the discourse-DAG to the extent it has predictive value)** | succeed-at-claim via existing AAD machinery | [`#deriv-causal-ib-lmi`](../../01-aat-core/src/deriv-causal-ib-lmi.md) instantiated on linguistic data; this **was already AAD-internal**, just unsurfaced |
| **C5 — Unbounded-abstraction claim** | **succeed-at-claim via comprehension-asymmetry** (reclassified 2026-05-13 after two-pass correction from Joseph) | applies the asymmetric-comprehension principle from `~/src/synthese-paper/01-synthese-asymmetric-comprehension/` — no agent at level $k$ can specify the upper bound of intelligence beyond $k$, therefore the gap-claim is not well-formed from below; what remains is the empirical observation that language has been coextensive and accelerative at every level we have access to |

The headline: **Pearl Level 2 content is structurally recoverable from natural-language text by a parsing-only procedure, with no active agent / loop / harness required**. The non-trivial part of this claim is that the Level 2 content is *not* derivable from any Level 1 (associational) summary of the text — which follows from Bareinboim et al.'s Causal Hierarchy Theorem applied to the discourse representation.

This reframes Pearl's classic objection. The right form of his critique against pre-loop LLMs is not *"they cannot do causal reasoning because they only see associations"* — language is not associations, it is **performative assertions of causation by speakers committed to those assertions**. The right form is *"they may not deploy the encoded causal content faithfully in their generative process"* — a degradation-bound, not a categorical limitation.

Joseph's separate claim that language has *unbounded* abstraction capability also yields, by a different route: applying the asymmetric-comprehension principle from the project's own synthese paper to the language-vs-intelligence question itself. From any agent's level, the upper bound of intelligence is not specifiable; therefore no gap-claim is well-formed from below. What remains is the empirical observation — language has been coextensive with intelligence and accelerative at every level we have access to. This reclassification (initially written as a no-go) is recorded in detail in `04-no-gos-and-followon.md` because the two-pass correction trail is methodologically informative: both wrong moves had the same shape — introducing an external standard above the asserter's comprehension level — and the asymmetric-comprehension principle is what reveals why both fail. The cross-paper connection means asymmetric-comprehension is doing double duty for the project: grounding the AI-welfare argument in Synthese and grounding the language-keeps-up-with-intelligence claim here.

---

## What's in this directory

- **`README.md`** (this file) — hypothesis, bottom line, navigation, follow-on routing
- **`01-derivation.md`** — the main derivation (C1: discourse-act encoding → Pearl Level 2 content via PCH) and its postulates
- **`02-related-angles.md`** — C2 (Reichenbachian inheritance), C3 (ICM time-asymmetry), C4 (causal-IB consequence connecting to AAD)
- **`03-minimum-scaffold.md`** — the activation-dual: what is the minimum substrate that recovers latent causal content from text? (purely structural, no interiority required)
- **`04-no-gos-and-followon.md`** — what's open, what's routed; includes the C5 reclassification with full two-pass-correction history (Joseph's cardinality catch + asymmetric-comprehension derivation)
- **`05-slc-derivation-attempt.md`** — strengthening attempt: lifts (SLC) postulate to derived via signalling-equilibrium (Lewis 1969 / Skyrms 1996 / Steinert-Threlkeld 2018 tradition). Sketch-level; lifts Theorem 1 from 3 postulates to 2 postulates + 1 sketch-derived
- **`06-cht-application-audit.md`** — rigor audit on the load-bearing PCH non-reduction step. Distinguishes "Level 1 over event-variables" vs "Level 1 over text-as-tokens"; generalizes the kettle pair to arbitrary event-pairs; scopes out three edge cases. Surfaces a notable side finding: the spike result is a candidate 6th instance of [`#disc-identifiability-floor`](../../01-aat-core/src/disc-identifiability-floor.md)
- **`07-c3-quantitative-bound-attempt.md`** — push on C3's quantitative gap. **Does not yield the bound** but produces a precisely-specified open theorem-target with (P1)-(P3) closure conditions and a candidate definition of $\mathcal I_c$. Identifies a high-value low-cost empirical follow-on (stratify corpora by Level-2-edge density, measure forward-vs-reverse cross-entropy asymmetry)

---

## How this connects to AAD's existing machinery

The standing response to Pearl's objection in AAD ([`msc/llm-causal-access-note.md`](../../msc/llm-causal-access-note.md)) is three independent arguments at different epistemic levels:

1. **The loop gives Level 2** (TF-02 / [`#der-loop-interventional-access`](../../01-aat-core/src/der-loop-interventional-access.md)) — derived, AAD-internal.
2. **Language encodes causal structure** — *previously* plausibility-grade.
3. **The symmetry argument** — philosophical, not mathematical.

This spike lifts (2) from plausibility-grade to **derivation-grade under three named postulates** (SLC, SC, CS — defined in `01-derivation.md`). The postulates are not derivable from non-linguistic first principles — they are facts about how communication systems develop — but they are well-defended in linguistics (Grice 1975, Stalnaker 1978, Lewis 1973, Karttunen 1973) and the conditional derivation is real.

The result composes with (1) to give a sharper statement of AAD's position on logogenic agents:

> *Natural language text carries Pearl Level 2 content structurally, independent of substrate. A logogenic agent — at any of the three sub-scopes in [`03-llm-core/`](../../03-llm-core/OUTLINE.md) — inherits Level 2 access from its training corpus (the language-encoded part) and from its feedback loop (the AAD-loop part). The two contributions are additive in the sense that each grants Level 2 independently; pre-loop substrate already has the language-encoded part. The loop adds **fresh** Level 2 access (interventions the agent itself performs), not Level 2 access *per se*.*

This is a non-trivial refinement of AAD's Pearl-response. It also has implications for the bias-bound machinery ([`#scope-observation-ambiguity-modulation`](../../01-aat-core/src/scope-observation-ambiguity-modulation.md), [`#deriv-observation-ambiguity-bias-bound`](../../01-aat-core/src/deriv-observation-ambiguity-bias-bound.md)): the $\kappa \cdot \mathcal{A}$ bound applies to *fresh* Level 2 access in the loop; the language-encoded Level 2 content is on a different epistemic footing (asserted by a different agent — the speaker — and inherited).

---

## Promotion targets if this lands cleanly

Tentative routing, subject to review:

- **Primary landing** — a new appendix-grade segment under [`01-aat-core/src/`](../../01-aat-core/src/), candidate slug `#deriv-pearl-level2-language-encoding` or `#deriv-discourse-pearl-encoding`, with the theorem statement and proof under three postulates. This segment becomes the structural anchor `msc/llm-causal-access-note.md` Response 2 currently lacks.

- **Secondary landing** — Discussion expansion in [`#der-loop-interventional-access`](../../01-aat-core/src/der-loop-interventional-access.md) noting that the loop's Level-2 contribution is *fresh* Level 2 (on top of language-encoded Level 2), with cross-reference to the new appendix.

- **03-llm-core impact** — the Frontmatter and `#scope-channel-collapse` should both pick up the language-encoded-Level-2 framing, since it sharpens what the sub-scopes inherit from training versus what they gain from each operational addition (scaffolding, interiority).

- **Connection to `~/src/synthese-paper/`** — the `01-synthese-asymmetric-comprehension` paper's §3 non-anthropomorphizing-inversion argument is *strengthened* by this result. The structural inversion is no longer "we can't know they don't reason causally"; it is "the causal content is provably *in* their training data, structurally; the question is faithfulness of generative deployment, not presence of source content."

- **Connection to `~/src/embeddings/`** — the IB-consequence angle (C4) is approximately what the embeddings paper's TACL-track empirical work is structurally surfacing for *epistemic* content. The analogous result for *causal* content is testable in the same paradigm (next-step embeddings work).

- **Connection to `~/src/neurips/03-llm-hallucinate-bound`** — the B-N8 architectural classification (Class 1 Separated / 2 Partial / 3 Coupled) is orthogonal to the language-encoded-Level-2 result; both apply. The paper may want a footnote noting that the κ × 𝒜 bound is on *deployment-time fresh causal access*, not on *encoded causal content in the training corpus*.

---

## Reading order if you're a future agent picking this up

1. This README to orient.
2. [`01-derivation.md`](01-derivation.md) for the central theorem.
3. [`02-related-angles.md`](02-related-angles.md) for the surrounding angles (Reichenbach, ICM, causal IB).
4. [`03-minimum-scaffold.md`](03-minimum-scaffold.md) for the activation-dual.
5. [`04-no-gos-and-followon.md`](04-no-gos-and-followon.md) for what didn't yield and what to do next.

If you're auditing whether the derivation is sound, the relevant pressure points are SLC / SC / CS in `01-derivation.md` §2; the CHT application in §4; and the no-go on C5 in `04-no-gos-and-followon.md`. The honest places this work is weakest:

1. **(SLC) is a postulate, not derivation.** Defended in linguistics; not first-principles-derivable.
2. **The ICM angle (C3) bottoms out at a postulate.** The directional asymmetry derives; the quantitative lower bound on the asymmetry by causal-information-content does not.
3. **The unbounded-abstraction claim (C5) is not derived.** It's a structural property of recursive symbolic systems; honest framing here is what the no-go gives us.

These are the right places to push next, in priority order.
