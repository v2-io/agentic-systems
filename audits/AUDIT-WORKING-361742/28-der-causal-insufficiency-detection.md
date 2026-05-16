# Reflection: der-causal-insufficiency-detection

**Segment:** `#der-causal-insufficiency-detection`

## What this does

Proves a no-go theorem: under purely on-policy execution with scope conditions (S1)-(S5), no detection mechanism can distinguish an L0-insufficient world (latent common causes) from an L0-sufficient world matched to the on-policy regime conditionals. The two worlds are observationally equivalent. This is a strategy-layer instantiation of the Causal Hierarchy Theorem (Bareinboim et al. 2022).

Key result: the prior aggregate-residual mechanism (Φ^L0(p̂) - ȳ_G) is not just one inadequate statistic — it is *a special case of the no-go's prediction*. Under purely on-policy execution, that residual is identically zero in BOTH worlds by algebraic identity. No replacement aggregate statistic can do better.

Five circumvention routes:
- (a) ε-exploration: scope condition S1 violated
- (b) Joint sibling observability: scope condition S3 violated — the AAD-canonical route
- (c) Intermediate observability: S3 at finer grain
- (d) Structural priors: S5 violated  
- (e) Direct intervention on latent: S4 violated

The covariance test (route b) is the unique broadly-available detection mechanism: uses machinery the theory already requires (loop interventional access + SA3 exploration).

## Naming relevance

**Row 159 (causal insufficiency detection)**: The naming question has real weight here. Let me think through the candidates:

- "Latent cause detection": names what's being FOUND (hidden common causes). But the no-go frame means this is really about FAILING to detect them — the segment's primary result is the impossibility, not the detection mechanism. The rename would reframe the emphasis from the no-go (structural insight) to the detection recipe (engineering result).

- "L0/L1 detection": accurate and ties to the Correlation Hierarchy directly. But loses the causal-inference literature connection — "causal insufficiency" is Spirtes-Glymour-Scheines vocabulary, used correctly here.

- "causal insufficiency detection" (keep): captures both the no-go (detection of causal insufficiency is impossible on-policy) and the positive result (here are routes that work). The compound noun does double duty: the impossibility of detection IS the structural insight about causal insufficiency.

- "Insufficiency detection": too ambiguous without "causal."

My reading: "causal insufficiency detection" should keep because (1) the technical vocabulary is correct and connects to SGS, (2) the no-go IS about the impossibility of "causal insufficiency detection" on-policy, so the name describes the topic accurately, (3) "Latent cause detection" would shift emphasis to the positive result and lose the structural framing. Strong keep.

**Row 248 (no-go result / impossibility result)**: This segment is the clearest example of an AAD no-go theorem. The segment itself uses "no-go" extensively ("no-go theorem," "the no-go," "the no-go applies"). Naming this as a recognized claim type is legitimate. The segment's Findings Brief says "structural impossibility" — "impossibility result" is cleaner than "no-go result" (less physics-specific). Both are reasonable.

## Key distinction confirmed

The asymmetry in the no-go: it forbids on-policy *detection* of L1 from L0, but does NOT forbid on-policy parameter learning within L0. The agent can learn its L0 conditionals arbitrarily well on-policy; it just cannot determine whether those conditionals hide a latent. This sharpens the diagnosis vs calibration split.

## New concepts surfaced

**Pairwise sibling covariance test**: The primary detection mechanism. Named, with explicit preconditions. Whether it needs its own row — likely not; it's the mechanism for der-causal-insufficiency-detection, not a standalone concept.

**On-policy observational equivalence** (W_L1 ~ W_L0*): The two worlds are indistinguishable on-policy. This is the structural insight behind the no-go. Named as "observational equivalence" in the derivation.

**Censoring mechanism**: Short-circuit AND/OR evaluation is what makes on-policy data Level 1 only. Named concept in the Discussion.

**Diagnostic CIY** (the three-axis explore/exploit/diagnose): The third axis "diagnose" is new vocabulary introduced in this segment. Check card for related rows.

**Route (b) joint sibling observability**: The covariance test route. This is load-bearing for der-loop-interventional-access.

## Connection to prior segments

This segment strongly confirms der-loop-interventional-access is load-bearing (not just "useful machinery" but "the unique broadly-available violation of the no-go"). Also strengthens the orient cascade's step 4c.
