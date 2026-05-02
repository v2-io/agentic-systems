# Embeddings Paper Cross-Pollination Note

*Written 2026-05-01 after Joseph shared the TACL paper draft (`~/src/embeddings/paper.md`, 222 lines, May 2026 working draft). Quick note on what the paper validates for ASF and what ASF might offer the paper. Not a full integration; flags the bidirectional relevance for future cycles.*

## What the paper validates for ASF

The paper documents that **frozen pretrained pooled sentence embeddings encode a continuously calibrated verbal probability axis aligned with human psychometric data**. Specifically:

- ρ > 0.90 supervised / 0.67–0.95 LOO on Mosteller (1990) 53-expression dataset
- Cross-validates against Vogel 2022 (ρ = 0.991, MAE = 5.1%) and Wintle 2019 (ρ = 0.967, MAE = 3.6%, n ≈ 924) — three independent psychometric datasets spanning 50+ years
- Replicates across 5 architecturally diverse pretrained models (BERT, BERT-large, MoE, decoder-derived embedding heads, multilingual XLM-R)
- Zero-shot ranking transfer to 8 typologically diverse languages (mean |ρ| = 0.928)
- Survives 12× dimensional compression on Matryoshka models
- Passes permutation null-hypothesis tests (p ≤ 0.005)
- Functional validation via rank-1 concept-erasure with cosine-matched random-direction control (the embedding-class analogue of decoder-LLM activation steering)

For ASF: this is the empirical foundation for #obs-evaluation-metrics in §03.II and adjacent claims throughout Part III about logogenic agents being able to *measure* their own $U_M$ via language-geometric proxies rather than relying on numerical instrumentation. The "language as the independent medium of thought" framing (Joseph's morning) has empirical traction at the geometric level.

## What the paper does NOT do (model-class scoping)

The paper carefully distinguishes three model classes:

1. **Decoder LLM internal states** (Marks & Tegmark 2023, Bürger et al. 2024, Ji et al. 2025, Lepori et al. 2026) — linear features in residual streams; token-level causal intervention via steering / activation patching is natural because the model generates tokens.

2. **Prompted LLM behavioral verbal-probability** (Sileo & Moens 2023, Belém et al. 2024, Tang et al. 2024) — model output is the measurement; numerical interpretations of hedge expressions elicited via prompts.

3. **Pretrained pooled sentence embedding** (this paper's contribution) — frozen-geometry linear axis extracted from pooled outputs; representation-level intervention via concept erasure as the model-class analogue.

Pretrained pooled sentence embedding models are not themselves logogenic agents (they don't act through language; they compute representations). They reveal a *structural property of language-as-representation* that logogenic agents can leverage. This distinction matters for ASF's framing: the embedding paper is *empirical substrate* for the claim that language has the geometric structure ASF agents can exploit, not itself a claim about logogenic-agent architecture.

## What ASF might offer the paper (if any)

The paper's §5.3 discussion frames the convergent-measurements thesis: distributional embedding geometry and human psychometric semantics as convergent measurements of one underlying epistemic dimension. This resonates with PROPRIUM's foundational premise (`ref/agentic-tft/agentic-tft-foundational-premises.md`): *"language is encoded thought"*.

ASF's potential contribution is a *theoretical reason* the convergence should be expected: under AAD, agents that operate through language as primary channel ( #scope-logogenic-agent, #scope-channel-collapse) have epistemic state encoded in the same substrate as their environment-facing behavior. The shared substrate forces a representational compression that preserves epistemic structure — and pretrained embeddings on that substrate inherit the structure by extracting it from the corpus the substrate was trained on. Human psychometric data is one calibration source; the embedding geometry is another; both are projections of the same underlying language-as-encoded-thought claim.

This is *interpretation-grade* support, not a result the paper needs to make. The paper's model-class focus is correct as stated. ASF could optionally cite the convergent-measurements result as one interpretation of the multi-dataset convergence, but the paper's framing in measurement-theoretic terms is already adequate.

## Where this lands operationally

1. **`obs-evaluation-metrics` segment** (currently exploratory in §03.II) — when promoted to draft, the paper is the load-bearing reference. Use the paper's nuanced characterization (model-class distinction; conjunction-of-qualifiers as the novelty claim) rather than the looser "embeddings encode epistemic states linearly" framing.

2. **03 OUTLINE Source Material entry for `~/src/embeddings/`** — updated in this turn to reflect the paper's more careful framing.

3. **Future segment candidate**: `obs-language-as-epistemic-substrate` or similar discussion-grade segment that frames the embeddings work as empirical evidence for Joseph's foundational premise (language as encoded thought). Could live in §03 root common section. Low-priority follow-up.

4. **Possible cross-reference from PROPRIUM-O-v2 §4** (Identity Theory) — the embeddings paper's psychometric-cross-validation result strengthens the *substrate-independence claim* (factor ii of #def-five-constitutive-factors via $M_t = \phi(\mathcal C_t)$): if 5 architecturally distinct models converge on the same calibrated axis, the structure is substrate-independent in a measurable sense. Worth noting in `obs-substrate-independence` Working Notes when that segment is promoted.

## Bidirectional flag for future cycles

The paper and ASF are mutually-reinforcing: the paper provides empirical substrate for an ASF claim; ASF provides one possible theoretical framework for *why* the cross-model / cross-language / cross-dataset convergence the paper documents should be expected. Neither needs the other for its own validity, but joint citation in either direction is honest and useful.

If Joseph submits the paper to TACL and the paper's measurement-theoretic interpretation lands well, the ASF logogenic-agent treatment becomes one of the natural follow-ups (logogenic-agent-as-architecture leveraging pretrained-embedding-as-substrate). If ASF Part III matures and starts being cited in agentic-systems literature, the paper becomes one of the natural empirical anchors. Both directions are open; this note flags the bidirectionality for whoever picks up either thread next.
