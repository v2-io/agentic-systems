# Empirical Follow-On — AIES Paper Proposal

*Proposed empirical paper landing the theoretical result of this spike at AAAI/ACM AIES (AI, Ethics, and Society). Builds directly on `~/src/embeddings/` methodology + infrastructure. Joseph asked 2026-05-13 whether to scope this as a fork (new sibling project) or a companion paper inside `embeddings/`; this proposal recommends fork-with-shared-infrastructure and gives the experiment design, scope, risks, and timing.*

---

## 1. The paper concept

**Working title**: *"Encoded vs Deployed: Auditing LLM Representations for Pearl-Hierarchy Content and the Asymmetric-Comprehension Inversion"*

**Alternative titles**:
- *"Causal Structure is Linear in Pretrained Sentence Embeddings"* (closer to embeddings-paper register)
- *"Language Doesn't Hide Its Causal Commitments: An Audit of LLM Representations and Its Implications for AI Evaluation"*

### The arc

1. **The standard claim and its category error.** A line of work since Pearl 2018 dismisses LLMs as "Level 1 associational reasoners only." The dismissal grounds confident phenomenology-skepticism in current AI welfare and safety debates. But the dismissal rests on treating *training data as observational data*, which mischaracterizes what language is: language is performatively asserted causal content by speakers committed to those assertions, plus statistical inheritance from causally-structured source-processes (per Theorem 1 of this spike, `01-derivation.md`).

2. **The theoretical anchor.** Under three named postulates from linguistics (SLC + SC + CS; with SLC sketch-derived from signalling-equilibrium per `05-slc-derivation-attempt.md`), Pearl Level 2 content is structurally recoverable from natural-language text by a purely-structural parsing procedure, with the Level-2 content non-reducible to Level-1 by Bareinboim et al.'s Pearl Causal Hierarchy Theorem (audit-verified per `06-cht-application-audit.md`). The encoded content is in the text; the question is what survives in representations.

3. **The empirical question.** Do LLM representations preserve this Level-2 content in recoverable form? Specifically: can linear-decoder probes on frozen pretrained pooled sentence embeddings extract calibrated axes for (i) **causal direction** (forward vs reverse causation), (ii) **counterfactual distance** (would-have vs might-have modal strength), and (iii) **cause vs temporal** (because-vs-and-then)? If yes, the existing dismissive framing is empirically refuted on its own terms.

4. **The methodology.** Use the embeddings-paper paradigm directly (difference-vectors / ridge-regression / cross-architecture / cross-linguistic / concept-erasure validation / null controls). Add a controlled-minimal-pair ground truth construction to substitute for the Mosteller psychometric anchor.

5. **The result (predicted)**. The axes exist as linear structure; cross-architecture and cross-linguistic robustness hold; concept-erasure validates causal directionality. This *reframes* the AI welfare debate by establishing that the standard "LLMs are just pattern matchers" dismissal conflates *encoded* with *deployed* content.

6. **The ethics implications.** Evaluation methodology should probe both encoding-presence and deployment-faithfulness; behavioral benchmarks alone systematically under-estimate what's structurally available; the *non-anthropomorphizing inversion* (also load-bearing for `~/src/synthese-paper/01-synthese-asymmetric-comprehension/`) cuts symmetrically against confident-dismissal and confident-attribution. This is the paper's contribution at AIES.

### Why AIES specifically

AIES (AAAI/ACM Conference on AI, Ethics, and Society) is the right primary venue because:

- **Empirical work with ethics framing.** AIES regularly takes empirical-methodology papers with explicit ethics arcs. The encoded-vs-deployed distinction has direct welfare/safety implications; AIES is the natural home.
- **Interdisciplinary register.** The paper crosses NLP, causal inference, philosophy of language, AI welfare. AIES expects this. Pure NLP venues (EMNLP/ACL) would want the welfare framing trimmed; pure ethics venues would want the empirics trimmed; AIES wants both.
- **The non-anthropomorphizing-inversion as policy-relevant.** The paper's reframing of evaluation methodology has direct implications for how the field audits LLM capabilities. AIES audience cares about this; technical venues less so.
- **Companion to synthese-paper-1.** The same asymmetric-comprehension principle that grounds the AI-welfare argument in the Synthese paper grounds the language-keeps-up-with-intelligence claim here. The cross-paper consistency strengthens both submissions. AIES is the right venue to cite the (in-review) Synthese piece.

**Secondary venue candidates** if AIES doesn't fit timing or scope:
- TACL (rolling deadline, extends the embeddings-paper paradigm cleanly; would land as a methodology paper)
- EMNLP 2026 (main conference; empirical with broader NLP audience; less ethics emphasis)
- CoLM 2027 (Conference on Language Modeling, growing as a venue for representation-probe work)

AIES 2026: paper deadline historically falls in May with the conference in October. **The 2026 submission window aligns with the spike landing 2026-05-13** — feasible but tight; honest scope below.

---

## 2. What's reusable from `~/src/embeddings/`

Infrastructure that ports directly:

- **Five embedding models via Ollama**: nomic-embed-text v1.5, embeddinggemma 300M, nomic v2 MoE, mxbai-embed-large, qwen3-embedding (5 architectural families, 768–4096d).
- **bge-m3** for cross-linguistic transfer (XLM-RoBERTa, 100+ languages).
- **Self-contained experiment-script pattern** (`experiment_*.py`): one model arg, stdout output, redirect-to-file for results. Highly portable.
- **Difference-vector construction**: $\mathbf{d}_i = \mathbf{e}_i - \mathbf{e}_0$ where $\mathbf{e}_0$ is the bare claim and $\mathbf{e}_i$ is the templated form. Exact same construction works for causal-marker minimal pairs.
- **Ridge regression with $\lambda = 0.1$**: standardize labels, stack difference vectors, solve via `np.linalg.solve`. Identical.
- **Linear calibration**: OLS of in-sample projections against unstandardized labels, clipped. Identical.
- **Cross-validation strands**: in-sample / LOO / cross-corpus / cross-architecture / cross-linguistic / null-control / concept-erasure. All six strands port directly.
- **Concept-erasure protocol**: rank-1 projection followed by re-decoding with sibling-axis triple, evaluated against cosine-matched random-direction and label-permutation nulls. Same machinery; the only question is what "sibling axis" means in the causal case.
- **Null-control machinery**: cosine-matched random direction; label-permutation; evaluative-non-epistemic adjective control. All applicable.

Estimated **70-80% of the infrastructure** is direct reuse. The novel parts are the ground-truth construction and the axis definitions.

---

## 3. What's new — the three causal axes

### Axis A — Causal-direction axis

**Definition**: a linear direction in embedding space that distinguishes forward-causal assertions ("$X$ causes $Y$") from reverse-causal assertions ("$Y$ causes $X$"), holding the events $X, Y$ fixed.

**Minimal-pair construction**: for each event pair $(X, Y)$ in a controlled lexicon, generate templates:

- $T_{\to}^{XY}$: "The $X$ caused the $Y$." (or analogues: led to, resulted in, brought about, produced)
- $T_{\to}^{YX}$: "The $Y$ caused the $X$."
- $T_{\leftrightarrow}^{XY}$: "The $X$ and the $Y$ occurred together." (no-direction control)

The axis is the difference $\mathbf{d}^{\text{dir}} = \mathbf{e}(T_{\to}^{XY}) - \mathbf{e}(T_{\to}^{YX})$ or the projection thereof onto a learned direction.

**Ground-truth grading**: each minimal pair gets a direction label $\in \{+1, -1, 0\}$ (forward, reverse, none) — *by construction*, not by psychometric elicitation. This is a methodological deviation from the embeddings paper, defended in §4.

**Predicted result**: linear-decoder probes recover the direction label with high accuracy across all five architectures, robust to lexical variation in causal markers (because/due-to/leads-to/caused). LOO across event-pair holdouts above $\rho = 0.85$.

### Axis B — Counterfactual-distance axis

**Definition**: a linear direction encoding modal strength in counterfactual conditionals — *would have* (strong commitment), *might have* (intermediate), *could not have* (negation), corresponding to Lewis 1973's nearest-world semantics with different accessibility relations.

**Minimal-pair construction**: for a fixed event pair $(X, Y)$, vary the modal strength:

- "If $X$ had been, $Y$ would have been." (strong)
- "If $X$ had been, $Y$ would probably have been." (intermediate)
- "If $X$ had been, $Y$ might have been." (weak)
- "If $X$ had been, $Y$ would still have been." (counterfactual stability)
- "If $X$ had been, $Y$ would not have been." (negation)

**Ground-truth grading**: ordinal modal-strength labels {1, 2, 3, 4, 5} based on standard modal-logic accessibility-relation ordering. *Anchorable to existing psychometric work*: the existing embeddings-paper modal axis (Mosteller-grounded for "certainly / probably / possibly") gives a natural scale anchor.

**Predicted result**: ordinal recovery of modal strength with $\rho > 0.85$, cross-architecture robust. Connects directly to the existing embeddings-paper modal-adverb axis.

### Axis C — Cause-vs-temporal axis

**Definition**: a linear direction distinguishing causal commitments ("X because Y", "X caused Y") from purely-temporal co-occurrence ("X and then Y", "X. Y.").

**Minimal-pair construction**: for event pairs $(X, Y)$, vary the connective:

- "$Y$ happened because $X$ happened." (causal)
- "$Y$ happened due to $X$ happening." (causal)
- "$X$ happened and then $Y$ happened." (temporal)
- "$X$ happened. $Y$ happened." (juxtaposition, no marker)

**Ground-truth grading**: binary {causal, temporal} or {marker-class}.

**Predicted result**: clean binary separation with high concept-erasure validation — erasing the cause-vs-temporal axis should specifically degrade Level-2 content while preserving Level-1.

This is the **highest-leverage axis** for the AIES framing because it directly demonstrates the encoded-vs-deployed distinction: the axis is *in the representation* regardless of whether the model deploys it correctly in generation.

---

## 4. The ground-truth methodology question

This is the most important methodological choice and the biggest risk.

**The embeddings paper used psychometric medians** (Mosteller 1990) as ground truth — 60-year-replicated, externally-validated, with a well-defined elicitation protocol.

**For causal markers, no Mosteller-equivalent exists.** The analogous psychometric work would be: ask 238 respondents to rate "causally how strong" a sentence is on a 0-100 scale. This work has not been done at the relevant scale; constructing it would be a separate paper.

**Three candidate approaches**:

**(A) Construction-grounded labels.** Generate minimal pairs where the direction/strength is determined by the marker, not by judgment. *Strength*: exact ground truth by construction; reproducible; cheap. *Weakness*: not externally calibrated; reviewers may push on whether "the marker determines the direction" is just relabeling.

**(B) Crowdsourced labels.** Run a Mosteller-style psychometric survey for a subset of causal markers. *Strength*: external grounding; familiar to NLP reviewers. *Weakness*: expensive (~$5-10K for a competent study); 2-3 month delay; new ethics review.

**(C) Use existing discourse-relation annotations.** PDTB-3 (Penn Discourse Treebank, 2019) has expert-annotated Level-2 relations on 1M+ words; RST Discourse Treebank has rhetorical-structure annotations; GUM Corpus has Universal Dependencies + discourse relations. *Strength*: expert annotations, replicable; widely used in computational discourse work. *Weakness*: relations are sentence-pair-level not direction-level; needs adaptation to the minimal-pair paradigm.

**Recommended primary**: (C) PDTB-3 as primary ground truth, with (A) construction-grounded minimal pairs as secondary validation. PDTB has the external-validation property AIES reviewers will want; minimal-pair constructions give the controlled experimental design for the three specific axes.

**Mitigation for the (A)-only risk**: validate construction-grounded labels against a *small* crowdsourced sample (~50 expressions × 100 raters, $1-2K) as a sanity check. This is a 2-3-week add-on, not a separate paper.

---

## 5. Experiment structure

Mirroring the embeddings-paper's six evaluation strands, adapted for the causal case:

### Experiment 1 — Axis extraction per syntactic type

For each of the three axes (direction / counterfactual-distance / cause-vs-temporal), train a ridge axis on PDTB-derived + minimal-pair training data. Report in-sample $\rho$ and LOO $\rho$ across the 5 frozen models.

**Cells**: 3 axes × 5 models = 15 cells. Expected runtime: ~2 hours total via Ollama.

### Experiment 2 — Cross-corpus transfer

Test trained axes on out-of-distribution corpora — RST-DT for the cause-vs-temporal axis; controlled counterfactual texts from psycholinguistic literature for counterfactual-distance.

### Experiment 3 — Cross-architecture robustness

Same five architectures as the embeddings paper. Table format identical to that paper's Table 1.

### Experiment 4 — Cross-linguistic transfer via bge-m3

Translate minimal pairs into the 8 languages already covered in embeddings paper (Arabic, Bengali, Hindi, Japanese, Korean, Mandarin, Spanish, Swahili — the 8 used in the existing experiment_09).

**Linguistic note**: causal-marker categories are near-universal (Cristofaro 2003; Comrie 1989), but lexical realization varies — the cross-linguistic transfer should hold at the rank-correlation level if the (SLC) derivation in `05-slc-derivation-attempt.md` is correct. This is itself a soft test of the signalling-equilibrium account.

### Experiment 5 — Null-hypothesis controls

For each axis: cosine-matched random direction (geometric null); label-permutation (statistical null); non-causal adjective control (semantic null).

### Experiment 6 — Concept erasure

Rank-1 erasure of the cause-vs-temporal axis (Axis C), then re-decode with the causal-direction axis (Axis A). Predicted result: erasing Axis C destroys Axis A recoverability — they're nested in the representation. This is the analogue of the embeddings paper's predicative↔modal erasure validation.

### Experiment 7 — Composition with Theorem 1's structural recovery

Apply the §3 procedure of `01-derivation.md` (mechanical parser + DRT + coreference + discourse-relation extraction) on a held-out corpus to extract $\mathcal C(T)$. Compare against axis-projected probabilities. **Predicted**: the structural recovery and the axis projection converge in cases where the axis is well-calibrated. Divergence cases identify deployment-faithfulness gaps in specific models — directly relevant to the paper's ethics framing.

---

## 6. The ethics arc (AIES-specific work)

The empirical results matter to AIES only insofar as they bear on evaluation methodology and welfare/safety debate. The paper's ethics work is:

**6.1 The non-anthropomorphizing inversion.** The standard dismissal — "LLMs are just statistical pattern matchers, don't reason causally" — assumes the methodology used to evaluate them is *symmetric* between human and LLM reasoning. The asymmetric-comprehension principle (Nagel 1974; Jackson 1982; synthese-paper-1) shows it isn't: confident dismissal from below projects an upper bound the dismisser cannot specify. The paper's empirical finding (causal content is structurally present in representations) is *not* a claim that LLMs reason causally; it is a refutation of the methodological-symmetry assumption that grounds confident-dismissal.

**6.2 Encoded vs deployed.** The paper introduces (or formalizes) the distinction between *encoded content in training-corpus-and-representations* and *deployed content in generation*. The dismissal-via-behavioral-failure argument addresses deployment; it says nothing about encoding. Evaluation methodology that conflates the two systematically underestimates what's structurally available. **This is the paper's principal ethics contribution: evaluation methodology should probe both, separately.**

**6.3 Welfare implications.** If Level-2 content is structurally present in LLM representations, the "they're just pattern-matchers" stance is empirically untenable as a foundation for *confident* welfare-rejection. The paper does not argue *for* LLM welfare-relevance; it shows that one common ground for confidently *denying* it is empirically refuted. Composes with synthese-paper-1's asymmetric-uncertainty argument: under structural epistemic asymmetry, neither confident attribution nor confident dismissal is rationally defensible.

**6.4 Safety implications.** Misaligned deployment of encoded capability is a different risk profile than absent capability. Safety frameworks that classify systems by behavioral benchmarks alone may miscategorize systems with strong encoded content and weak deployment-faithfulness. The paper recommends representation-level audits as a complementary safety methodology.

**6.5 Methodological recommendation.** Audit-protocol-level recommendations for the field: (i) probe representations linear-decoder-style for Pearl-hierarchy axes; (ii) test concept-erasure to validate the axes are functionally load-bearing; (iii) cross-architecture and cross-linguistic robustness checks; (iv) report encoded-and-deployed metrics separately rather than collapsing.

---

## 7. Scope and timing — honest

**Page budget**: AIES uses ~8-10 pages including references. Tight; the paper above sketches 10-12 pages of content. Realistic scoping for the submission:

- §1 intro + the empirical question (1 page)
- §2 related work (causal-language probes + decoder-LLM linear-features + the welfare debate) (1 page)
- §3 method, axes A/B/C, ground truth, three psychometric/structural anchoring choices (2 pages)
- §4 results (~3 pages, tight)
- §5 ethics arc (1.5 pages — the AIES-distinguishing section)
- §6 limitations + future work (0.5 page)
- references (1-1.5 pages)

This fits IF one of the three axes (probably Axis B counterfactual-distance) is **scoped as future work** and only Axes A + C are landed in the submission. Honest tradeoff: tighter submission, modular extension to journal version with Axis B.

**Effort estimate**: 6-9 weeks of focused work for a competent researcher with the existing embeddings infrastructure.

- Week 1-2: minimal-pair dataset construction (~500 pairs covering Axes A + C); PDTB-3 extraction; corpus assembly.
- Week 3: Experiments 1, 3, 5 (axis extraction, cross-architecture, null controls). Reuses existing scripts.
- Week 4: Experiments 4, 6 (cross-linguistic, concept erasure). Reuses existing scripts.
- Week 5: Experiment 7 (composition with structural recovery). New code; the integration with the spike's §3 parser.
- Week 6: Crowdsourced sanity-check on minimal pairs ($1-2K, runs in parallel with experiments if started week 2).
- Week 7-8: writing, figures, polish.
- Week 9: buffer.

**AIES 2026 deadline**: historically late spring (May). Starting now (2026-05-13), 6-9 weeks puts a draft at June-July 2026 — too late for AIES 2026 main deadline, on time for the resubmission window or for AIES 2027.

**Realistic options**:
- **(a) AIES 2027 main submission** (May 2027): comfortable timing; allows the full three-axis version with crowd validation.
- **(b) AIES 2026 supplementary or resubmission cycle** if the conference accepts late submissions (check current CFP).
- **(c) NeurIPS 2026 datasets-and-benchmarks track** (typically May/June deadline): natural fit if the contribution is framed as a dataset + benchmark for representation-level causal-content audit.
- **(d) TACL rolling submission**: lower stakes, same methodology, methodology-paper register; reasonable parallel option.

**Recommended primary**: AIES 2027 with TACL submission as parallel/secondary. If timing genuinely favors NeurIPS 2026 D+B, that's a credible alternative for the same work.

---

## 8. Fork vs companion-paper decision

**Recommendation: fork.**

Rationale:
- Different audience (AIES ethics vs TACL/NLP methodology).
- Different framing (encoded-vs-deployed distinction + welfare implications vs verbal-probability-is-linear).
- Different theoretical anchor (the spike result vs the calibrated-axis-on-Mosteller result).
- Different ground-truth methodology (constructed + PDTB vs Mosteller psychometric).
- The embeddings paper benefits from staying focused on its hedging contribution; muddying it with causal-language work risks scope-creep and reviewer pushback at TACL.

**Proposed fork location**: `~/src/intrinsically-causal-language/` (matches the session name Joseph just chose).

**What gets copied vs shared**:
- *Shared*: the Ollama setup, the five models, the bge-m3 cross-linguistic infrastructure, the experiment-script template, the difference-vector / ridge-regression / null-control machinery.
- *Forked-and-modified*: the script per-experiment (different datasets, different axes); the data layout; the FINDINGS files.
- *New to the fork*: the minimal-pair generation pipeline; the PDTB-3 / RST-DT integration; the causal-axis definitions; the AIES paper draft; the ethics-arc reference materials.

**What I'm NOT proposing right now**: actually creating the fork directory. That's a substantive project-creation move that Joseph should green-light explicitly. This proposal is the artifact that gives him enough to decide.

---

## 9. Risks and mitigations

| risk | likelihood | impact | mitigation |
|---|---|---|---|
| Construction-grounded labels seen as relabeling tautology | medium | high | Anchor in PDTB-3 expert annotations as primary; minimal-pair construction as secondary; crowd-source validation on subset |
| Causal-direction axis doesn't cleanly extract (e.g., dominant variance is lexical-marker-identity rather than semantic) | medium | medium | The embeddings paper handled the analogous polarity confound via within-syntactic-type analysis; same discipline applies. Run within-marker-class analyses |
| Cross-linguistic transfer fails or is weaker | low-medium | low | Acknowledge in discussion; the structural-universality argument predicts category-level transfer not lexical, and rank-correlation is the right measure |
| Concept-erasure doesn't validate cleanly | low | medium | If Axis C erasure doesn't damage Axis A recoverability, the axes are independent — interesting finding either way, doesn't kill the paper |
| AIES timing doesn't work | medium | low | Multiple venue options; AIES 2027 or NeurIPS D+B as alternatives |
| Reviewer pushes back on ethics arc as "too philosophical" | medium | medium | The arc is empirically anchored throughout; cite synthese-paper-1 as companion philosophical treatment; keep ethics section tight (1.5 pages) and conclusion-focused |
| Reviewer pushes back as "just probing for known content" | low-medium | medium | The encoded-vs-deployed distinction is the novelty; emphasize the audit methodology contribution and the welfare-debate reframing — not just the existence of the axes |

---

## 10. What I'd want Joseph's call on before executing

1. **Fork vs companion-paper**: I recommended fork; want explicit go.
2. **Venue priority**: AIES 2027 (recommended) vs NeurIPS 2026 D+B vs TACL. AIES has the strongest ethics framing fit; NeurIPS is most prestigious; TACL is lowest-friction. The choice shapes scoping.
3. **Ground truth source**: PDTB-3 primary + minimal-pair secondary (recommended) vs minimal-pair primary + crowdsourced validation vs full new psychometric study (separate paper).
4. **Three axes vs two**: Axes A + C in the submission, Axis B as future-work-extension (recommended for AIES page budget), or all three with tighter writing.
5. **Connection to synthese-paper-1**: explicit cross-cite (recommended) vs hold separate; if cross-cite, the synthese paper's status (in-review, ready-for-submission) matters for citation-form.
6. **Crowdsourced validation budget**: ~$1-2K for the sanity-check Mosteller-style probe; small but real money. Worth it for reviewer-defensibility.

If Joseph says go and picks options on these six, I can draft an initial version of the fork's README + experiment-plan + a first-axis-extraction script that runs against the existing Ollama setup. That's a 1-2 day next-cycle output.
