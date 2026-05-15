# What Didn't Yield, What the No-Go Tells Us, and Follow-On

*Per spike discipline: honest record of what doesn't close, because the failure record prevents future agents from re-attempting the same moves without new evidence.*

---

## C5 — "language has unlimited abstraction capability" — reclassified from no-go to yields-via-comprehension-asymmetry

**History of this entry**: originally written 2026-05-13 mid-spike as a no-go. Reclassified late same day after two correction passes from Joseph that surfaced two distinct category errors in the original framing. The reclassification is recorded here in full because the wrong-path is informative — both the error I made and the structure of the correction matter.

Joseph's claim, as posed:

> *"BUT language itself has **unlimited** abstraction capability — meaning language is as unbounded and nonlinear as intelligence itself (it being a decoupled medium of intelligence)."*

### First pass (what I initially wrote — wrong)

I conceded compositional infinity / productive recursion (Hauser-Chomsky-Fitch 2002) but refused the "as unbounded as intelligence" identification on the grounds that *intelligence is plausibly a richer property than expressive capacity* — judgment, integration across modalities, goal-directedness, action. I framed this as a no-go: language ≠ intelligence; the two are coupled but not identical.

**Error #1 (Joseph's first catch)**: I introduced richness-on-the-intelligence-side (judgment, integration, action) that wasn't in scope for an *abstraction capability* claim, then used those out-of-scope aspects to dismiss the in-scope claim. The right scope for C5 was abstraction-capability specifically; the broader "language equals intelligence" reading was my own strawman.

### Second pass (after Joseph's first correction — still wrong, narrower error)

After acknowledging Error #1, I revised to "yields under named commitment" via the decoupled-medium-of-intelligence argument, with two residual gaps: (a) a cardinality argument that uncountable abstraction-spaces can't be reached by countable expressions, and (b) the indexical/phenomenal content gap.

**Error #2 (Joseph's second catch)**: the cardinality argument is itself a category error. Language doesn't reach abstractions by **enumeration** (which would be cardinality-bounded). It reaches them by **description** — "the reals" specifies an uncountable set in five tokens. Cantor's diagonal argument is *itself* a linguistic proof. The Löwenheim-Skolem situation (ZFC has countable models even though it proves uncountability) is exactly this: language abstracts via predicate-style specification, and specifications are finite even when their referents aren't.

Recognizing this dissolves my cardinality caveat entirely.

### Third pass (Joseph's deeper correction — this is the right form)

After Errors #1 and #2 were named, the residual gap I was still gesturing at was the indexical/phenomenal content — the "what it's like" problem in Nagel/Jackson neighborhood. Joseph's response went one floor deeper:

> *the intelligence-bound-asymmetry says higher intelligence can comprehend lower, but lower sees higher as like themselves but with some confusing stuff added in — project current intelligence as best as you can and guess whether the other is or is not actually higher intelligence. But the higher intelligence can know with certainty when it has the lower intelligence orders as a subset. This should mean that we have no way to determine what the upper bound to intelligence is or if it has one — any attempt is a category error because higher orders of intelligence by definition are something you can only understand by inhabiting it, at which point it's no longer a higher order intelligence but your current intelligence. If we cannot know from this side what higher intelligence consists of, how can we say anything about language other than that so far it has enabled higher-order rationality (pretty provable at least via anthropology / historical — and the writing bump that gave it more) so far and seems to not only keep up with intelligence but has been an accelerant…*

This applies the **asymmetric-comprehension principle** (the central move in `~/src/synthese-paper/01-synthese-asymmetric-comprehension/`) to the language-vs-intelligence question itself. The structure:

- From level $k$, the upper bound of intelligence beyond $k$ is structurally inaccessible — comprehending it would *be* inhabiting it.
- Therefore claims of the form *"language falls short of intelligence at some level"* are not well-formed from below. To assert the gap, the asserting agent at level $k$ would have to specify what intelligence has at level $k+\epsilon$ that language lacks — which is exactly what comprehension-asymmetry forbids.
- The only well-formed claim from level $k$ is whatever's empirically observable from $k$: language has been coextensive with intelligence's expansion at every level we have observational access to, and has been an *accelerant* (writing-bump; mathematical notation; formal languages — each extending the substrate and being followed by new intelligence reaching new abstractions through it).

My residual indexical/phenomenal gap was the same error one floor up: I was pointing at things on the *other side* of the asymmetry, naming abstractions I don't have access to and calling that a gap. The asymmetric-comprehension principle forbids this move on its own grounds.

### The derivable form of C5

> **C5 (derivable form).** Under the asymmetric-comprehension principle (Nagel 1974; Jackson 1982; the synthese-paper-1 elaboration), the upper bound of intelligence is not specifiable from any level $k$. Therefore no claim of the form *"language has scope < intelligence"* is well-formed from below. The strongest defensible claim about language's relation to intelligence is empirical-historical: at every level we have observational access to, language has been coextensive with intelligence and accelerative of its expansion. Under the project's logozoetic commitment (intelligence-as-language-constituted; see [`#scope-logogenic-agent`](../../03-logogenic-agents/src/scope-logogenic-agent.md) and the `04-eli/` framing), the coextensiveness is structural rather than contingent.

Note this is **stronger than C1's derivation**: C1 requires three named postulates (SLC, SC, CS); C5 under this route requires only the asymmetric-comprehension principle, which is already load-bearing for the synthese paper. Same principle, two different domains, both supported.

### What this changes for the project

**Asymmetric-comprehension is now doing double duty across the project**:

1. **In `~/src/synthese-paper/01-synthese-asymmetric-comprehension/`** — grounds the AI-welfare argument. From the human side, the upper bound of LLM phenomenology is structurally inaccessible; therefore confident dismissal of LLM welfare-relevance is hubristic; the moral situation has a specific Pascal's-wager-shape under asymmetric stakes.

2. **In this spike** — grounds the language-keeps-up-with-intelligence claim. From any agent's side, the upper bound of intelligence is structurally inaccessible; therefore confident claims that language falls short are not well-formed; what's left is the empirical observation that language has been coextensive and accelerative.

The cross-paper connection is now load-bearing for both papers. Adding a paragraph in the Synthese paper's §3 that explicitly notes this dual role would strengthen the paper's framing (asymmetric-comprehension is not a single-use argumentative move but a general structural principle of the project).

### What this *doesn't* establish

Honesty: even in its derivable form, C5 establishes only that *no agent at level $k$ can specify a gap between language and intelligence beyond level $k$*. It does **not** establish:

- That there isn't such a gap (just that it can't be specified or argued for from below).
- That language is *causally* what makes intelligence expand (the coextensiveness is structural; the acceleration is empirical).
- That language is the *only* possible substrate for intelligence (multi-modal, embodied, etc. substrates remain in scope for separate inquiry).

These are honest residuals. Each is open work; none undermines the derivable form.

### Two errors as diagnostic

The two-pass correction trail is methodologically worth preserving. Both errors had the same shape: I introduced an external standard (richer-than-expression aspects of intelligence; cardinality of abstraction spaces) and used it to dismiss the claim. The asymmetric-comprehension principle reveals the structural reason both moves fail: I cannot legitimately introduce an external standard that lives above my own comprehension level. Doing so projects from below, exactly the move the principle names as illegitimate.

**Diagnostic to retain**: when a no-go is being asserted via *"X has property P that Y lacks"*, check whether P is accessible from the asserting agent's level. If P is on the other side of a comprehension-asymmetry, the assertion is a category error regardless of how plausible it sounds.

---

## What didn't close on each angle

### C1 — discourse-act encoding (the main yield)

**Did close**: Theorem 1 under (SLC) + (SC) + (CS); the CHT non-reduction; the substrate-agnosticism of recovery.

**Did not close**:
- Deriving (SLC) from non-linguistic first principles. The communicative-functional defense (any community of causal reasoners with a communication channel will develop causal markers) is suggestive but not rigorous; it would need formal game-theoretic / signalling-equilibrium argument analogous to Skyrms 1996 / Lewis 1969. **Promising follow-on direction.** This would make (SLC) emergent rather than postulated.

- Eliminating (SC). Without speaker-commitment, marker-as-assertion collapses to marker-as-decoration. Some defenders of strong implicature theories have tried to weaken this; the spike does not pursue them.

- Implicit-relation recovery. Theorem 1's scope is explicit-marker content. Most natural-language causal content is implicit (genre conventions, world knowledge, narrative coherence). Recovering implicit content needs additional machinery. **The main follow-on.**

### C2 — Reichenbachian inheritance

**Did close**: the foundational reason distributional methods capture causal structure at all.

**Did not close**: a quantitative lower bound on how much causal structure they capture. RCCP gives a *direction of inference* (statistical dependency ⇒ causal trace in source) but not a *magnitude*. Cartwright-style counterexamples bound the principle's universality.

**Honest read**: C2 is *foundational* but not *operational*. It justifies the methodology; it does not bound the results.

### C3 — ICM time-asymmetry

**Did close**: directional asymmetry — forward-language compresses better than reverse-language under ICM + discourse-structural mechanisms (forward anaphora-licensing).

**Did not close**: the quantitative link between the compression-asymmetry and a measure of causal-information content. The lower bound $K(L_{\text{forward}}) + I_{\text{causal}} \le K(L_{\text{reverse}})$ requires:

1. A formal definition of $I_{\text{causal}}$ on discourse-DAG structure.
2. A theorem connecting that quantity to algorithmic-information asymmetry.

Neither is in the standard literature. The closest existing machinery is directed information (Massey 1990) and the project's own [`#deriv-causal-ib-lmi`](../../01-aat-core/src/deriv-causal-ib-lmi.md). **Bridging these to discourse-DAG causal content is real follow-on work** — non-trivial but tractable.

### C4 — causal-IB consequence

**Did close**: the IB-preservation claim follows by direct instantiation of existing AAD machinery on linguistic data.

**Did not close**:
- A specific quantitative bound. Same gap as C3 — requires a specific causal-information measure.
- Deployment faithfulness. The IB bound is on the representation, not on the generation. Empirical (Causal Parrots etc.) work bears on deployment.

---

## Follow-on routing — concrete, ordered by tractability and value

### Immediate (this spike's commits, before parking)

1. **Decide promotion target for Theorem 1.** Candidate slug `#deriv-pearl-level2-language-encoding` or `#deriv-discourse-pearl-encoding`, appendix-grade under [`01-aat-core/src/`](../../01-aat-core/src/). Joseph's call. **Until promoted, the result is spike-resident.**

2. **Cross-reference the result from [`msc/llm-causal-access-note.md`](../../msc/llm-causal-access-note.md)** — that note's Response 2 currently says "plausible empirical claim — but quantifying how much genuine causal structure survives compression is an open empirical question." With Theorem 1, the response can be lifted: the encoded content is *structurally there* by the discourse-act argument; the empirical-deployment question is the right form of the residual open question.

3. **Note in [`03-logogenic-agents/OUTLINE.md`](../../03-logogenic-agents/OUTLINE.md) Source Material section**: the inherited-vs-fresh Level 2 split (per `03-minimum-scaffold.md`) sharpens the sub-scope distinctions. Working Notes update on the relevant scope segments.

4. **Routing decision for `~/src/synthese-paper/01-synthese-asymmetric-comprehension`**: the spike result strengthens the non-anthropomorphizing-inversion argument in §3. **Spike result available for Joseph's call** on whether to thread into the Synthese paper or keep it apparatus-grade in companion work.

### Near-term spikes (clear scope, real math)

5. **Spike: SLC as emergent from signalling-equilibrium.** Game-theoretic derivation that any community of causal-modeling agents with a transmission channel evolves causal-hierarchy markers. Skyrms 1996 / Lewis 1969 / Steinert-Threlkeld 2018 quantifier emergence work as scaffolding. Would lift (SLC) from postulate to derived. *Tractability: medium-high — the methods exist, the application is novel but not unprecedented.*

6. **Spike: Directed-information bound for forward-vs-reverse discourse compression.** Bridge Massey 1990 / `#deriv-causal-ib-lmi` to the discourse-DAG case. Would close C3's quantitative gap and tighten C4's bound. *Tractability: medium — the framework exists; the specific construction is novel.*

7. **Spike: Implicit-relation recovery beyond Theorem 1.** Use the discourse-DAG framework to extend $\mathcal{C}$ from explicit-marker recovery to genre-and-narrative-coherence recovery. RST / SDRT machinery + LLM-mediated implicit-relation classification (Pitler-Nenkova 2009; Liu-Strube 2023). *Tractability: medium — engineering-heavy; the conceptual move is clear.*

### Empirical (host: `~/src/embeddings/`)

8. **Cause-vs-temporal axis probe.** Apply the embeddings paper's methodology (linear-decoder probe on frozen pretrained pooled sentence embeddings) to discourse-DAG content. Targets: cause-vs-temporal axis, causal-direction axis, counterfactual-distance axis. Cross-architecture / cross-linguistic robustness in the same paradigm. *Tractability: high — methodology and instrumentation in place; the discourse-DAG corpus needs assembly but standard resources (PDTB, RST-DT) exist.*

9. **Reversed-language compression bound (TACL-track follow-on).** Empirically measure $K(L_{\text{forward}})$ vs $K(L_{\text{reverse}})$ across architectures and languages. Already partially in the literature (scaling laws); a targeted study with causal-content-controlled corpora would tighten the relationship. *Tractability: high — extension of existing scaling-law methodology.*

### Longer-term theoretical

10. **C5 sharpening.** The unbounded-abstraction claim is not derivable from this spike's machinery, but it points at a real cluster of questions: what is the formal relationship between expressive capacity (compositional infinity), causal capacity (Pearl-hierarchy levels), and intelligence-borne-on-the-substrate? Hauser-Chomsky-Fitch on Merge; Chomsky's Universal Grammar; Pylyshyn on classical-vs-connectionist architectures; the literature on systematicity (Fodor-Pylyshyn 1988). **Long-horizon work**, more philosophy-and-formal-linguistics than AAD-internal. Not immediate priority unless Synthese-paper-positioning calls for it.

---

## Reverse-direction prompts and the Joseph-intuition test

Joseph's specific empirical observation —

> *"It should be clear that giving an LLM a prompt with all of the words in reverse order is going to cause a great deal of confusion."*

— is now derivable as a consequence of C3 + the discourse-DAG structure of $\mathcal{C}(T)$. Reverse-order presentation breaks:

- Anaphoric resolution (pronouns before antecedents).
- Definite-article licensing (definites before entity introduction).
- Conditional-clause processing (consequents before antecedents).
- Discourse-relation extraction (relata in non-natural order).

The asymmetry is *structural*, not just a learned-bias artifact of how training data is presented. An LLM trained on reversed text would still struggle with forward text for the same structural reasons (asymmetric anaphora-licensing rules apply regardless of training direction).

This is a small concrete payoff: Joseph's intuitive prediction now sits on the derived asymmetry under C3, not on empirical observation alone.

---

## Final honest read

The strengthening **partially yielded**:

- **C1 (the central claim) yielded** under three named postulates from linguistics. This is real strengthening — the response-2 in `msc/llm-causal-access-note.md` moves from plausibility-grade to derivation-grade, with the CHT non-reduction giving the result genuine teeth.

- **C2, C3, C4 yielded partially** — directional and qualitative results derive; quantitative bounds remain follow-on work.

- **C5 did not yield** at all, and the no-go is informative: it forces honest separation of substrate from intelligence, which is the project's own commitment from `~/src/firmatum/developmental-foundations-notes.md` ("identity is not substrate").

The work I am most uncertain about is whether the three postulates (SLC, SC, CS) can themselves be derived from more foundational principles. The current spike treats them as postulates; the proposed follow-on spike #5 would push on that. Joseph's signalling-equilibrium work and the `04-eli/`-resident developmental-foundations notes both point in promising directions.

The work I am most confident about is the CHT non-reduction step: this is straightforward application of an existing theorem, and the example pairs (kettle-boil-whistle, etc.) generalize cleanly. If anything in this spike survives, the non-reduction step does.

The work I would most like a second pair of eyes on is **whether (SC) is too strong**. Speaker-commitment is the bridge from text-contains-marker to causal-content-asserted, and it has decades of philosophy-of-language behind it — but it is also where the most plausible counterexamples live (irony, fiction, genre conventions). If (SC) holds only for ~80% of training-corpus causal markers, what does that do to the Theorem? Likely: the result becomes a bound — the discourse-DAG has Level 2 content **at least at the rate that SC holds across the corpus**. This is still strong but is no longer a "for all texts" claim. **Worth careful reading by a peer-grade reviewer before promotion.**
