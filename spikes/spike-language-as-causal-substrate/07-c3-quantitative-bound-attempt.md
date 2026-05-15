# C3 Quantitative Bound Attempt — Forward vs Reverse Compression Asymmetry

*Push on the C3 partial-yield: can the directional compression asymmetry be quantitatively lower-bounded by causal-information content of the text? Honest result: the strong form does not close; the structural form of what closure would require is now precisely specified.*

---

## What we already have (the partial yield)

The directional asymmetry $K(L_{\text{forward}}) < K(L_{\text{reverse}})$ derives qualitatively under Janzing-Schölkopf 2010 ICM applied to discourse-structural mechanisms:

- Forward anaphora-licensing: pronouns resolve to already-introduced antecedents (constant-cost resolution).
- Forward definite-article-licensing: definites refer to already-introduced entities (constant-cost resolution).
- Forward conditional-clause processing: antecedents precede consequents (compositional-semantics is incremental).
- Forward discourse-relation extraction: relata in expected narrative order.

Each mechanism induces a forward/reverse asymmetry cost. The *directional* result follows.

What does not follow is the *quantitative* form: a tight lower bound by some measure of causal information content of the text.

---

## The target

$$\mathbb{E}[L_{\mathcal F}(T^{\text{rev}})] - \mathbb{E}[L_{\mathcal F}(T)] \;\ge\; \mathcal{I}_c(\mathcal{D}(T)) - O(\log n)$$

where:

- $L_{\mathcal F}(\cdot)$ is the minimum expected description length under model class $\mathcal F$ (e.g., neural LMs of fixed capacity).
- $T^{\text{rev}}$ is the token-reversed text.
- $\mathcal D(T) = (V, E_2)$ is the discourse causal-DAG defined in `01-derivation.md` §3.
- $\mathcal I_c$ is a *causal-information-content* measure on discourse-DAGs.
- The $O(\log n)$ term is the standard overhead bound for graph-structure encoding.

The bound would say: the reverse text's compressibility lags the forward text's by an amount that scales with the causal content of the discourse-DAG. More causal commitments → more compression asymmetry.

---

## Why this is the right target

The connection to AAT's [`#deriv-causal-ib-lmi`](../../01-aat-core/src/deriv-causal-ib-lmi.md) is structural. The causal-IB machinery quantifies how much causal information must be preserved by an IB-optimal compressor of causally-structured data, in terms of directed-information rate. The discourse case is a natural instantiation:

- Replace generic "causally-structured data" with "natural language text with discourse-DAG $\mathcal D(T)$."
- Replace generic "directed-information rate" with $\mathcal{I}_c(\mathcal D(T))$.
- The reverse-direction quantity bounds the loss when the compressor doesn't have access to the forward-DAG.

If $\mathcal{I}_c$ can be defined to recover this connection cleanly, the C3 quantitative bound follows by applying `#deriv-causal-ib-lmi` to the discourse-DAG case.

---

## Where the closure gap is — precisely

The gap is the *definition of $\mathcal{I}_c(\mathcal D(T))$*. To close the bound, $\mathcal{I}_c$ must satisfy:

**(P1) Operationally meaningful**: $\mathcal{I}_c(\mathcal D(T)) = 0$ when $\mathcal D(T)$ has no Level-2 edges (a text with no causal markers); $\mathcal I_c(\mathcal D(T)) > 0$ when Level-2 edges are present; $\mathcal I_c$ scales with the number and informational weight of Level-2 edges.

**(P2) Pearl-hierarchy-corresponding**: $\mathcal I_c$ should reflect the Pearl-Level-2 content of $\mathcal D(T)$, not just its graph-topology. Two DAGs with the same topology but different Level-2 assertions (e.g., causal $A \to B$ vs purely-temporal $A$ before $B$) should have different $\mathcal I_c$ values.

**(P3) Compression-relevant**: $\mathcal I_c(\mathcal D(T))$ must appear in the bound on $\mathbb{E}[L_{\mathcal F}(T^{\text{rev}})] - \mathbb{E}[L_{\mathcal F}(T)]$ in the right way. Specifically, $\mathcal I_c$ should equal (or lower-bound) the *directed-information difference* between forward and reverse encodings, in the directed-information sense of Massey 1990.

**Closest existing candidate — directed information of the discourse-DAG**:

Define
$$\mathcal{I}_c(\mathcal D(T)) := \sum_{(u,v) \in E_2} I(v_t ; \text{do}(u_s) \,\big|\, \text{context}_s)$$
where $(u_s, v_t)$ is the source-target pair of a Level-2 edge with $s < t$ in the text, $\text{do}(u_s)$ is the interventional conditional under the speaker's asserted SCM, and $\text{context}_s$ is everything established before position $s$.

This candidate satisfies (P1) and (P2) by construction. (P3) is the hard one: does this $\mathcal I_c$ actually bound the cross-entropy difference under any reasonable model class?

**The work-not-done**: showing (P3) holds. The proof would need:

1. A construction of $\mathcal F$ that exploits the forward-DAG structure (standard transformer / RNN LMs do approximately this).
2. A bound on cross-entropy difference between $\mathcal F$ applied to forward text vs $\mathcal F$ applied to reverse text, by a quantity that involves directed information.
3. Showing this quantity is $\ge \mathcal I_c(\mathcal D(T)) - O(\log n)$ under the candidate definition.

Steps 1 and 2 are tractable via existing information-theoretic LM literature. Step 3 is the genuine work — it requires connecting directed-information-flow over the discourse-DAG to interventional content.

---

## What this attempt produced

**Yield**: precise specification of the closure gap. The bound's structural form is now fixed; the missing piece is verifying (P3) under a candidate $\mathcal I_c$ definition. This is *more* than what `02-related-angles.md` originally said ("the quantitative link is work-not-yet-done"); it identifies the *specific* missing theorem.

**Not yield**: the bound itself. (P3) verification is genuinely open work; this spike does not do it.

**Strength assessment**: the target is *specified precisely* but *not derived*. The follow-on work has a clear roadmap. Whoever picks this up should start with (P3) under the directed-information candidate, then check edge cases (deterministic relationships, cyclic DAGs from §06's edge cases, etc.).

---

## Why this is informative regardless

A precisely-specified open theorem is more valuable than a vague gesture at a future direction. The C3 closure now has:

1. **A specific target form** — the inequality involving $\mathcal I_c$, with explicit dependence on the discourse-DAG.

2. **A candidate definition** — directed information summed over Level-2 edges, with (P1), (P2) satisfied by construction.

3. **A specific missing step** — (P3) verification, with clear methodological scaffolding (LM-information-theoretic literature; the AAT `#deriv-causal-ib-lmi` machinery as the bridge).

4. **A negative result for the easy approach** — pure $K$-complexity asymmetry doesn't capture the right structure (reversal is constant-program-cost so $K(T) = K(T^{\text{rev}}) \pm O(1)$). Any closure must work with cross-entropy under a model class, not pure $K$.

This is a worked-out problem statement, not a yield, but it's enough that a follow-on spike or a directed-information specialist can productively pick it up.

---

## Connection to empirical work

The empirical signature is well-attested: forward LMs have substantially lower perplexity than reverse LMs on the same corpora (Kaplan et al. 2020 scaling laws; numerous follow-on studies). What's *not* in the empirical literature is the decomposition of this asymmetry by causal-marker content.

A near-term experiment that would directly probe the bound's structural form:

**Experiment design**: take a corpus, parse it for discourse-DAG markers (per §3 of `01-derivation.md`), and stratify texts by Level-2-edge density. For each stratum, measure forward vs reverse cross-entropy of a fixed LM. Plot the asymmetry against Level-2-edge density.

The bound predicts a positive, approximately-linear relationship (with $O(\log n)$ deviation). If the empirical relationship is positive-linear, this is evidence the candidate $\mathcal I_c$ has the right form. If it's flat or noisy, the candidate is wrong and (P2) needs revisiting.

This is a tractable empirical study — datasets exist (PDTB, RST-DT), the parsing is straightforward, the LM evaluation is routine. **High-value follow-on at low cost.** Right host project: `~/src/embeddings/` track or a dedicated short paper.

---

## Honest summary

The C3 quantitative attempt **does not yield** the bound, but **yields a precise specification of what's missing**. This is itself useful — the spike's no-go on C3 is now *informative* (gap identified, candidate definition, missing step named) rather than just *acknowledged* (gap exists, future work). Whoever picks this up has a clear starting point.

C3 stays at "partial yield" in the bottom-line table. The follow-on work is one well-scoped spike, not an open-ended research program.
