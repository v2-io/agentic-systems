# R2 Aggregation — Detail View

**Generated:** 2026-04-30T21:52:24Z
**Targets included:** 106 (filtered to ≥2 R2 voters from 629 total)
**R2 voters:** codex-r2b, gemini-r2, opus-r2b, opus-r2c, sonnet-r2b, sonnet-r2c

## How to read this

Per target: R1 synthesized votes + every R2 vote with full notes, novelty score (vs the bullet on the voter's card), and substance score. The information needed for the final decision is here, not in the table view.

**R1 synthesis rules** (applied per candidate; see script header for full reasoning):

```
n = number of distinct R1 agents who voted
m = mean R1 weight (R1 scale: +3..-3)
d = max(category_tally) / sum(category_tally)

n == 0                                          → null
n ≥ 3 and m ≥ 2.0 and d ≥ 0.6                   → +2
(n ≥ 2 and m ≥ 0.5) or (n == 1 and weight ≥ 2)  → +1
m ≤ -0.5 or (n == 1 and weight ≤ -2)            → -1
else                                            →  0
```

**Substance discount for R2 votes:**

```
novelty   = 1 - Jaccard(tokenize(note), tokenize(card-bullet))
substance = raw_weight × (0.5 + 0.5 × novelty) × min(1.0, note_chars/100)
```

Floor at 0.5×weight on pure paraphrase — the act of voting is itself a judgment.

---

## Strong consensus (95)

### `$\alpha$ (sector-condition lower bound)`

*R2 voters:* 3 (3 architectures: gemini, opus, sonnet)

**Candidate: `Correction rate constant`** ▸ leader
- *R1 synthetic:* **+1** — n=1, mean=3.00, weights=[+3], categories={add-alias:1}
  > Currently $\alpha$ appears as a Greek letter throughout but no English alias exists in prose. NOTATION.md gives "lower sector bound of correction function" as the gloss, which is technically correct but reads heavily. "Correction-rate constant" connects to the $\alpha$-as-rate intuition (units $t^{-1}$) and the timescale reading $1/\alpha$. Symbol stays in math; alias enters prose. Prose-symbol layer.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *add-alias* — novelty=0.71, len=192, **subst=1.71**
    > 'Correction rate constant' is the perfect English alias for $\alpha$. It connects to the $t^{-1}$ units and the $1/\alpha$ timescale intuition, and it avoids the biological baggage of 'decay'.
  - **opus-r2c** (opus): +2 ★ *add-alias* — novelty=0.46, len=379, **subst=1.46**
    > The NOTATION.md gloss "lower sector bound of correction function" is technically right but reads heavily. "Correction-rate constant" connects to the $\alpha$-as-rate intuition (units $[t^{-1}]$) and the reciprocal-timescale form $1/\alpha$ that NOTATION.md explicitly recommends as the more readable form for practitioners. Symbol stays in formalism; English handle enters prose.
  - **sonnet-r2b** (sonnet): +2 ★ *canonicalize* — novelty=0.84, len=485, **subst=1.84**
    > The gain-sector bridge makes this precise: $\alpha = \eta^* \cdot c_{\min}$, so $\alpha$ is the effective worst-case rate at which correction machinery reduces mismatch. Units are $t^{-1}$; the timescale $1/\alpha$ is how long a single correction cycle takes at minimum capacity. "Constant" is right — it's a property of the architecture, not a variable. The persistence condition then reads naturally in prose: "correction rate constant must exceed the disturbance-to-capacity ratio."

  *substance total (R1 + R2):* 6.01

**Candidate: `Correction rate or decay rate`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={add-alias:1}
  > NOTATION.md defines $\alpha$ mathematically; prose refers to it as "the sector condition parameter" and "worst-case scalar correction rate." English alias "correction rate" (or "decay rate" in linear-ODE context) would aid readability in continuous prose.

- *R2 votes:*
  - **opus-r2c** (opus): +1 *add-alias* — novelty=0.85, len=328, **subst=0.92**
    > "Correction rate" works in nonlinear-sector contexts; "decay rate" is the linear-ODE-approximation reading. Both are useful; the disjunctive form names the dual reading. Slight preference for the singular "correction rate constant" because it picks the canonical sector-condition framing rather than disjunctively invoking both.
  - **sonnet-r2b** (sonnet): -1 *canonicalize* — novelty=0.84, len=362, **subst=-0.92**
    > The `or` signals unresolved ambiguity — that's not what a canonicalization should convey. "Decay rate" is the linear-ODE reading, which the segment explicitly marks as pedagogical (heuristic status). Better to commit to the sector-condition reading ("correction rate constant") than to hedge with an alternative that applies only to the linearized approximation.

  *substance total (R1 + R2):* 0.00


---

### `$\delta_t$`

*R2 voters:* 2 (2 architectures: gemini, opus)

**Candidate: `Aporia signal`** ▸ leader
- *R1 synthetic:* **+1** — n=2, mean=2.50, weights=[+3, +2], categories={add-alias:2}
  > Strong prose alias for mismatch signal, matching the adaptive-cycle vocabulary. Per `def-mismatch-signal` Epistemic Status: "the word foreshadows the aporia interpretation." The mismatch *is* the aporia signal in cycle-phase register.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *add-alias* — novelty=0.91, len=178, **subst=1.91**
    > Essential as the dual alias in prose. It allows the philosophical, generative nature of the mismatch to be discussed without losing the engineering precision of the primary name.
  - **opus-r2b** (opus): +1 *add-alias* — novelty=0.82, len=176, **subst=0.91**
    > Same as row 608 add-alias logic. Aporia is the cycle-phase term (Greek register); the symbol $\delta_t$ benefits from having both prose handles available depending on register.

  *substance total (R1 + R2):* 3.82

**Candidate: `Mismatch signal`**
- *R1 synthetic:* **+1** — n=1, mean=3.00, weights=[+3], categories={add-alias:1}
  > Confirm canonical. Already established in NOTATION.md and `def-mismatch-signal`. Engineering register.

- *R2 votes:*
  - **opus-r2b** (opus): +2 ★ *keep* — novelty=0.65, len=138, **subst=1.65**
    > Symbol $\delta_t$ pairs with "mismatch signal" as the engineering-register prose handle. NOTATION.md is canonical here; this row confirms.

  *substance total (R1 + R2):* 2.65


---

### `$\iota_{ij}$`

*R2 voters:* 2 (2 architectures: gemini, sonnet)

**Candidate: `Identifiability coefficient`** ▸ leader
- *R1 synthetic:* **+2** — n=3, mean=2.00, weights=[+2, +2, +2], categories={add-alias:3}
  > Per `deriv-strategic-dynamics`: $\iota_{ij}$ scales each edge's contribution by causal-warrant. The causal warrant per edge. Already in use as "the identifiability coefficient $\iota_{ij}$"; confirm canonical.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *add-alias* — novelty=0.90, len=147, **subst=1.90**
    > This is the necessary English alias for $\iota_{ij}$. It correctly identifies the parameter that scales the interventional contrast in Section III.
  - **sonnet-r2c** (sonnet): +2 ★ *canonicalize* — novelty=0.75, len=365, **subst=1.75**
    > Confirmed by scope-edge-update-causal-validity. ι_ij ∈ [0,1] is "the identifiability coefficient" — the agent's estimate of how cleanly an observed outcome can be attributed to edge (i,j). Already in use in deriv-strategic-dynamics. Load-bearing: unifies with observability into η_eff = η_edge · ι_ij as a complete frozen-edge characterization. Strong canonicalize.

  *substance total (R1 + R2):* 5.65


---

### `$\mathcal C_t$ chronica`

*R2 voters:* 3 (3 architectures: codex, gemini, opus)

**Candidate: `$\mathcal C_t$`** ▸ leader
- *R1 synthetic:* **+1** — n=1, mean=3.00, weights=[+3], categories={rename:1}
  > Keep. The calligraphic-C choice is deliberately to avoid collision with $\mathcal H$ (entropy) and the symbol works in both LaTeX and prose.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *keep* — novelty=0.74, len=140, **subst=1.74**
    > Calligraphic C reads naturally with `chronica` and avoids the $\mathcal H$ collision with Shannon entropy that the segment explicitly flags.
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.67, len=187, **subst=1.67**
    > The calligraphic $\mathcal{C}_t$ symbol is the definitive handle for the interaction history. It correctly avoids collision with entropy ($\mathcal{H}$) and maintains LaTeX compatibility.
  - **opus-r2b** (opus): +2 ★ *keep* — novelty=0.79, len=323, **subst=1.79**
    > The segment's Epistemic Status is explicit on the design rationale: chronica avoids the $\mathcal{H}$ collision in speech and notation. Calligraphic-C reads cleanly in LaTeX, distinguishes from $C$ (channel capacity), and the prose-symbol pair $\mathcal C_t$ / chronica is one of the project's load-bearing aesthetic moves.

  *substance total (R1 + R2):* 6.20


---

### `$\phi$`

*R2 voters:* 3 (3 architectures: codex, gemini, opus)

**Candidate: `History compression`** ▸ leader
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={add-alias:1}
  > Makes the operation concrete in prose.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *add-alias* — novelty=0.94, len=119, **subst=1.94**
    > Good prose handle for $\phi: \mathcal C^\ast \to \mathcal M$: the map compresses chronica into the current model state.
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.88, len=168, **subst=1.88**
    > 'History compression' is the perfect prose handle for the $\phi$ function. It captures both the domain (history $\mathcal{C}_t$) and the operation (compression $\phi$).
  - **opus-r2b** (opus): +1 *add-alias* — novelty=0.92, len=316, **subst=0.96**
    > $\phi$ is a many-to-one map from $\mathcal{C}_t$ into model space — the segment is explicit that the compression is "the essential function of the model." "History compression" names the operation in prose. Useful as a prose handle when prose mentions the operation; the symbol $\phi$ stays as the formal identifier.

  *substance total (R1 + R2):* 5.78


---

### `$f_M$ (event-driven update)`

*R2 voters:* 2 (2 architectures: codex, gemini)

**Candidate: `Epistemic update function`** ▸ leader
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={add-alias:1}
  > Distinguishes the model update function structurally from the purposeful processing function $f_G$.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *add-alias* — novelty=0.83, len=140, **subst=1.83**
    > Good prose alias for $f_M$: it updates the model/reality state and will need to stay distinct from later $G_t$ or strategy update functions.
  - **gemini-r2** (gemini): +2 ★ *add-alias* — novelty=0.53, len=139, **subst=1.53**
    > This is the necessary English alias for $f_M$. It correctly distinguishes the model update from the purposeful substate processing ($f_G$).

  *substance total (R1 + R2):* 3.36


---

### `$G_t = (O_t, \Sigma_t)$`

*R2 voters:* 2 (2 architectures: opus, sonnet)

**Candidate: `Purposeful substate`** ▸ leader
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={add-alias:1}
  > Confirm. The phrase "purposeful substate" is the LEXICON-canonical alias and is used throughout.

- *R2 votes:*
  - **opus-r2c** (opus): +2 ★ *canonicalize* — novelty=0.92, len=402, **subst=1.92**
    > The "substate" qualifier is doing necessary work: $G_t$ is part of the agent's state $X_t = (M_t, G_t)$, and calling $G_t$ a "state" by itself courts collision with $X_t$. "Substate" preserves the part-of-whole relationship. The canonicalize is over residual paraphrases ("goal state", "purposeful state", "teleological substate"); promote "purposeful substate" as the canonical English form for $G_t$.
  - **sonnet-r2c** (sonnet): +2 ★ *canonicalize* — novelty=0.67, len=137, **subst=1.67**
    > Confirmed by segment. G_t is the purposeful substate; "purposeful substate" is the canonical LEXICON alias. Canonicalize for consistency.

  *substance total (R1 + R2):* 4.58

**Candidate: `Purposeful state`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={add-alias:1}
  > Good prose alias for the objective-strategy part of state.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +1 *canonicalize* — novelty=0.83, len=138, **subst=0.92**
    > Good prose alias. "Substate" is more precise (G_t is a substate of X_t = (M_t, G_t)). Both forms useful; "purposeful substate" is primary.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.97, len=287, **subst=-0.98**
    > Drops the "sub" qualifier and creates collision risk with $X_t$ as the complete state. The pair-substate naming (epistemic substate $M_t$ + purposeful substate $G_t$) reads as a clean partition; "purposeful state" + "epistemic state" doesn't have the same partition-into-whole structure.

  *substance total (R1 + R2):* 0.93


---

### `$H_b$`

*R2 voters:* 2 (2 architectures: gemini, opus)

**Candidate: `Agent opacity $H_b$`** ▸ leader
- *R1 synthetic:* **+1** [excavated] — n=1, mean=3.00, weights=[+3, +3], categories={canonicalize:2}
  > Hafez opacity metric applied to adversarial dynamics. Standardizes the opacity metric.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.96, len=154, **subst=1.96**
    > Combining the prose alias 'Agent opacity' with the imported symbol $H_b$ perfectly honors the external theorem while standardizing the AAD-specific usage.
  - **opus-r2c** (opus): +2 *canonicalize* — novelty=0.92, len=232, **subst=1.92**
    > Standard pairing for first-introduction prose ("the agent opacity $H_b$ — backward predictive uncertainty under Hafez's definition…"). Promote this as the canonical introduction form; allow "agent opacity" alone in subsequent prose.

  *substance total (R1 + R2):* 4.88

**Candidate: `Agent opacity`**
- *R1 synthetic:* **+1** — n=1, mean=3.00, weights=[+3], categories={add-alias:1}
  > Per `der-agent-opacity` line 18: explicit dual to $U_o$. Confirms Codex r1 +3 single-vote. Make "agent opacity" the canonical English alias; $H_b$ the symbol.

- *R2 votes:*
  - **opus-r2c** (opus): +2 ★ *add-alias* — novelty=0.85, len=356, **subst=1.85**
    > English handle for $H_b$ in prose. Pairs with transition opacity (Ω-side unknown to agent), epistemic opacity (h unknown to agent), and now agent opacity (the agent's actions unknown to other observers). The opacity family is doing coherent work — every "opacity" in AAD is "X-unknown-to-Y" with X varying. Symbol stays in math; English alias enters prose.

  *substance total (R1 + R2):* 2.85

**Candidate: `$H_b$`**
- *R1 synthetic:* **+1** [is_keep] [invented] — n=2, mean=3.00, weights=[+3, +3], categories={canonicalize:2}
  > Adopted; keep. Adopted concept; AAD adds observer/horizon/trajectory indexing but keeps the symbol.

- *R2 votes:*
  - **opus-r2c** (opus): +1 *keep* — novelty=0.89, len=187, **subst=0.95**
    > Adopted from Hafez et al. with attribution. Symbol-side: keep. The H_b symbol travels with the Hafez literature where it's already established; importing without rename is the right move.

  *substance total (R1 + R2):* 1.95

**Candidate: `Backward opacity`**
- *R1 synthetic:* **+1** — n=2, mean=2.00, weights=[+3, +1], categories={add-alias:2}
  > Shorter than backward predictive uncertainty, but still accurate. Codex's r1 single-arch +3 alternative.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.97, len=240, **subst=-0.98**
    > Drops "agent" — the opacity is *of* the agent (its actions are the unknown thing). "Backward" picks out the time-direction sense (predicting future actions of the agent, looking backward from observation) but loses the *who-is-opaque* axis.

  *substance total (R1 + R2):* 0.02


---

### `$M_t$`

*R2 voters:* 3 (3 architectures: codex, gemini, opus)

**Candidate: `Model state or epistemic substate`** ▸ leader
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={add-alias:1}
  > Both aliases are in use. "Model state" is shorter and more common; "epistemic substate" is the precise companion to "purposeful substate." Standardize: "model state" in casual prose, "epistemic substate" in segments where the $M_t$ / $G_t$ parallel is being made explicit.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *canonicalize* — novelty=0.64, len=98, **subst=1.61**
    > Use "model state" in plain prose and "epistemic substate" where the $M_t$ / $G_t$ pairing matters.
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.62, len=188, **subst=1.62**
    > Keeping both handles allows for flexibility. 'Model state' is good for casual engineering prose; 'epistemic substate' is the precise companion for 'purposeful substate' in formal segments.
  - **opus-r2b** (opus): +1 *add-alias* — novelty=0.75, len=412, **subst=0.88**
    > $M_t$ is the symbol; both "model state" (short, casual) and "epistemic substate" (paired with "purposeful substate" $G_t$) are useful prose handles. The pair-with-$G_t$ context makes "epistemic substate" load-bearing where the contrast matters; "reality model" is the fuller prose name. Multiple aliases are fine here as long as the *symbol* $M_t$ remains the structural identifier. Add-alias rather than rename.

  *substance total (R1 + R2):* 5.10


---

### `$M_t$ (reality model)`

*R2 voters:* 2 (2 architectures: codex, gemini)

**Candidate: `Working model`** ▸ leader
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "$M_t$" is short and conventional but doesn't carry compression-of-history weight. "Reality model" (segment's title gloss) is "fine but slightly grandiose." Tentative.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.87, len=144, **subst=1.87**
    > "$M_t$" is the mathematical object; "Working model" is the precise, non-grandiose handle for what the agent currently uses to predict the world.
  - **codex-r2b** (codex): +1 *add-alias* — novelty=0.96, len=67, **subst=0.66**
    > Usable casual gloss, but too generic for the canonical prose alias.

  *substance total (R1 + R2):* 2.52

**Candidate: `Reality model`**
- *R1 synthetic:* — (no R1 evidence)

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *add-alias* — novelty=1.00, len=119, **subst=2.00**
    > Segment title and content support this directly: $M_t$ is the agent's compressed representation of how the world works.

  *substance total (R1 + R2):* 2.00

**Candidate: `Predictive state`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "$M_t$" is short and conventional but doesn't carry compression-of-history weight. "Reality model" (segment's title gloss) is "fine but slightly grandiose." Tentative.

- *R2 votes:*
  - **codex-r2b** (codex): +1 *add-alias* — novelty=0.92, len=99, **subst=0.95**
    > Captures prolepsis/prediction but loses the compression-of-chronica and belief-about-reality roles.

  *substance total (R1 + R2):* 0.95


---

### `$R$ (sector-condition radius)`

*R2 voters:* 2 (2 architectures: gemini, sonnet)

**Candidate: `Model-class capacity`** ▸ leader
- *R1 synthetic:* **+1** — n=2, mean=2.00, weights=[+3, +1], categories={add-alias:2}
  > Already used inconsistently — sometimes "sector radius," sometimes "model class capacity," sometimes "valid region." NOTATION.md uses "model class capacity" in the radius row; canonicalize that as the prose alias. NOTATION.md defines $R$ as "radius of sector-condition region"; prose calls it "model class capacity" and "sector-region radius" interchangeably.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.94, len=137, **subst=1.94**
    > Consistent with my vote for target 215. 'Capacity' is the geometrically and information-theoretically correct term for the $R$ parameter.
  - **sonnet-r2b** (sonnet): +2 ★ *canonicalize* — novelty=0.96, len=23, **subst=0.45**
    > $R$ bounds how large $\

  *substance total (R1 + R2):* 3.39


---

### `$U_M$`

*R2 voters:* 2 (2 architectures: gemini, sonnet)

**Candidate: `Epistemic unity`** ▸ leader
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={add-alias:1}
  > Already established as the prose form in NOTATION.md and LEXICON.md. Vote to canonicalize the alias for future consistency.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *add-alias* — novelty=0.83, len=149, **subst=1.83**
    > Already established in the documentation as the prose name for $U_M$. It correctly identifies the property of the agent's internal model consistency.
  - **sonnet-r2c** (sonnet): +2 ★ *canonicalize* — novelty=0.59, len=196, **subst=1.59**
    > Already established in NOTATION.md and LEXICON.md. Vote to canonicalize as the prose alias for U_M. Consistent with the Greek-register vocabulary and the pattern of prose-glossing all AAD symbols.

  *substance total (R1 + R2):* 4.42


---

### `$U_M$ / $U_O$ / $U_\Sigma$ unity dimensions`

*R2 voters:* 2 (1 architectures: opus)

**Candidate: `Epistemic unity teleological unity strategic unity`** ▸ leader
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={add-alias:1}
  > The symbol layer is fine but the word *unity* requires paraphrase on every encounter ("what is $U_O$ unity measuring?"). Define each in NOTATION.md with its full English name: $U_M$ = **epistemic unity** / $U_O$ = **teleological unity** / $U_\Sigma$ = **strategic unity**. Then "teleological unity crosses the threshold from below" reads without lookup where "$U_O$ crosses the threshold from below" does not. The Lexicon already has these English names — the move is to *use them* consistently in segments.

- *R2 votes:*
  - **opus-r2b** (opus): +2 ★ *canonicalize* — novelty=0.71, len=505, **subst=1.71**
    > Strong canonicalize. Currently $U_O$ requires every reader to remember "teleological unity" or look up the symbol; using "teleological unity crosses the threshold" in prose reads without lookup. The LEXICON already names these; canonicalize commits to *using* them in segments. The symbol $U_O$ stays as the structural identifier; the English forms become the canonical prose handles. The framework's value-of-symbol-with-prose-alias discipline (per NOTATION) is not yet uniformly applied for these three.
  - **opus-r2c** (opus): +2 ★ *canonicalize* — novelty=0.70, len=423, **subst=1.70**
    > The English names already exist in LEXICON; the failure is they're under-used in segment prose. "Teleological unity crosses the threshold from below" reads where "$U_O$ crosses the threshold from below" requires the reader to map the symbol back. Strong canonicalize: in segment prose, prefer the full English name on first encounter and the symbol once context establishes it. The mathematical formalism keeps the symbols.

  *substance total (R1 + R2):* 3.41


---

### `AAD (acronym)`

*R2 voters:* 3 (3 architectures: codex, gemini, sonnet)

**Candidate: `AAD`** ▸ leader
- *R1 synthetic:* **+1** [invented] — n=2, mean=3.00, weights=[+3, +3, +3], categories={canonicalize:2, keep:1}
  > Core framework acronym. Defended keep. Retain core acronym.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *keep* — novelty=0.60, len=69, **subst=1.10**
    > Retain the core acronym; it is already doing framework-identity work.
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.83, len=91, **subst=1.67**
    > The acronym is well-established and distinctive. It correctly labels the mathematical core.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=1.00, len=146, **subst=2.00**
    > Recently renamed from ACT specifically to avoid an AI Consciousness Test collision. The rename cost has been paid; further churn dilutes identity.

  *substance total (R1 + R2):* 5.77

**Candidate: `Adaptation and purpose dynamics apd`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: considered alternative. Acronym collision risk; doesn't roll off the tongue.

- *R2 votes:*
  - **codex-r2b** (codex): -1 *rename* — novelty=0.94, len=43, **subst=-0.42**
    > Acronym churn without enough semantic gain.
  - **sonnet-r2c** (sonnet): -1 *keep* — novelty=0.94, len=59, **subst=-0.57**
    > Loses the acronym and "purpose" is vaguer than "actuation."

  *substance total (R1 + R2):* -1.99

**Candidate: `Adaptation and agency dynamics AAD`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: considered alternative. "Agency" is overloaded in AI discourse.

- *R2 votes:*
  - **codex-r2b** (codex): -1 *rename* — novelty=0.83, len=75, **subst=-0.69**
    > "Agency" is too overloaded and the expansion rename is not worth the churn.
  - **sonnet-r2c** (sonnet): -1 *keep* — novelty=0.67, len=76, **subst=-0.63**
    > "Agency" is overloaded in AI discourse; the current full name is preferable.

  *substance total (R1 + R2):* -2.32


---

### `AAD (Adaptation and Actuation Dynamics)`

*R2 voters:* 4 (4 architectures: codex, gemini, opus, sonnet)

**Candidate: `AAD (Adaptation and Actuation Dynamics)`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [invented] — n=8, mean=2.50, weights=[+3, +1, +3, +1, +3, +3, +3, +3], categories={canonicalize:8}
  > The framework name itself, recently renamed (2026-04-16) from Agentic Cycle Theory to resolve a collision with the AI Consciousness Test (Schneider & Turner) in AI welfare literature. The case for keeping centers on rename cost: the rename has been paid, citation velocity is building under the new name, and any fresh alternative would face the same collision-checking burden ACT did. The acknowledged imperfection — 'Actuation' is a slightly weaker fit than 'Adaptation' for what Section II covers (purposeful agency with objectives, not mechanical actuation) — is judged to be cheaper to handle via a Section II preamble clarification than via another framework-level rename.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *canonicalize* — novelty=0.94, len=128, **subst=1.94**
    > Keep the current framework expansion; another framework-level rename would spend identity without solving a real naming problem.
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.90, len=189, **subst=1.90**
    > The rename cost has been paid. 'Actuation' accurately describes the purpose of Section II (the agent acts on the environment). Changing it again would introduce catastrophic citation drift.
  - **sonnet-r2c** (sonnet): +2 *keep* — novelty=0.91, len=331, **subst=1.91**
    > The full name earns its keep: "Adaptation" names Section I's subject, "Actuation" names the Section II addition of goal-directed action. The mechanical-engineering flavor of "Actuation" is real but minor; it correctly distinguishes the goal-directed actuation layer from mere reactive adaptation. A Section II preamble can clarify.
  - **opus-r2c** (opus): +1 *keep* — novelty=0.97, len=185, **subst=0.99**
    > Same vote as the bare-acronym row; the parenthetical expansion is fine in formal contexts but the bare acronym is what reads in prose. Keeping the parenthetical as the formal expansion.

  *substance total (R1 + R2):* 8.74

**Candidate: `AAD`**
- *R1 synthetic:* **+1** — n=1, mean=3.00, weights=[+3], categories={rename:1}
  > Recent rename (2026-04-16); further churn dilutes identity. Naming collisions have already narrowed options. The "Actuation" asymmetry is real but handled more cheaply by a Section II preamble clarification.

- *R2 votes:*
  - **codex-r2b** (codex): +2 *keep* — novelty=0.97, len=71, **subst=1.40**
    > Short acronym is usable and already paid for across the current corpus.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.82, len=342, **subst=1.82**
    > The acronym was selected through a collision-audited rename (ACT→AAD) less than two weeks ago. Re-renaming compounds churn; the collision-checking cost on any new acronym would land on the same workload that just delivered AAD. The "Actuation" awkwardness in Section II is real but handleable by preamble clarification, not by another rename.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.96, len=62, **subst=1.22**
    > The acronym is stable and the rename cost has been paid. Keep.

  *substance total (R1 + R2):* 5.44

**Candidate: `AAD agentic adaptation dynamics`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Actuation" has a strong mechanical engineering flavor that clashes slightly with the teleological/purposeful focus of Section II. "Agentic Adaptation Dynamics" retains the acronym while emphasizing agency.

- *R2 votes:*
  - **codex-r2b** (codex): -1 *rename* — novelty=0.89, len=103, **subst=-0.95**
    > Improves "Actuation" slightly, but creates churn and adds AI-discourse "agentic" load to the expansion.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.83, len=463, **subst=-0.92**
    > "Agentic Adaptation Dynamics" preserves AAD as letters but introduces a different problem: "agentic" is the framework's broader-shell vocabulary (ASF = Agentic Systems Framework), so "Agentic Adaptation Dynamics" reads as ASF-shaped at the acronym level rather than naming the inner mathematical core specifically. The current Adaptation/Actuation split, even if "actuation" is a slightly weaker fit, names what the *two halves* (Section I, Section II) are about.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.84, len=183, **subst=-0.92**
    > "Agentic" is redundant since everything in the framework is agentic; loses the Section I / Section II asymmetry signal (adaptation is universal, actuation is the goal-directed layer).

  *substance total (R1 + R2):* -2.78


---

### `action transition`

*First-encounter locality:* `#def-action-transition` (Section I; depends on `#def-agent-environment`). First formal definition; Actions affect the environment through a transition function that is unknown to the agent and possibly stochastic.

*Segment:* [`01-aad-core/src/def-action-transition.md`](../../01-aad-core/src/def-action-transition.md)

*R2 voters:* 4 (3 architectures: codex, opus, sonnet)

**Candidate: `action transition`** ▸ leader
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=3, mean=1.00, weights=[+1, +1, +1], categories={canonicalize:3}
  > Standard terminology. Actions affect environment. Weak keep.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.97, len=392, **subst=1.97**
    > The segment defines both the action space and the transition function — the coupling between agent action and environment state change. "Action transition" correctly names this coupling. "Action channel" would incorrectly suggest symmetry with the observation channel; the key point about this definition is that T (the transition function) is unknown to the agent, making action non-trivial.
  - **codex-r2b** (codex): +1 ★ *keep* — novelty=1.00, len=210, **subst=1.00**
    > Serviceable slug noun for the segment: plain and accurate. I would not strengthen it beyond +1 because the actual memorable sub-concept here is `transition opacity`, not the broader action-transition primitive.
  - **opus-r2b** (opus): +1 ★ *keep* — novelty=0.88, len=334, **subst=0.94**
    > Accurate to the segment's content (actions affect $\Omega$ via $T$, the transition function). The transition-opacity claim — that $T$ is unknown — is the partner clause; subject-noun could capture either, but "transition" is the right word for the mechanism. Slightly under-evocative but not actively misleading; weak-keep over churn.
  - **opus-r2c** (opus): +1 ★ *keep* — novelty=0.91, len=186, **subst=0.96**
    > Names the two things the segment defines: actions (the agent's contribution) and the transition function T (the environment's response). Compound is mildly clunky but the substance fits.

  *substance total (R1 + R2):* 5.86

**Candidate: `Action channel`**
- *R1 synthetic:* **0** — n=2, mean=0.00, weights=[-1, +1], categories={rename:2}
  > To mirror observation-channel and emphasize the interface boundary. Objection: actions change the environment; channel language would wrongly suggest communication symmetry with observation.

- *R2 votes:*
  - **codex-r2b** (codex): -1 *rename* — novelty=0.86, len=178, **subst=-0.93**
    > Misleading symmetry: observations arrive through a channel, but actions induce world-state transition through $T$. The segment's own distinction is transition, not communication.
  - **opus-r2b** (opus): -1 *rename* — novelty=0.88, len=405, **subst=-0.94**
    > The auditor's objection is correct: "channel" suggests communication symmetry with observation, but action and observation are not symmetric. Action moves $\Omega$ via the transition function $T$; observation pulls information back via $h$. Action has no "information content" in the way observation does — it has *causal effect*. Calling it a channel imports a metaphor the formalism specifically avoids.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.83, len=302, **subst=-0.92**
    > The objection in the rationale is right: action *changes* the environment via T, while observation *samples* the environment via h. Calling the action layer a "channel" imports communication-theoretic symmetry that doesn't hold — there's no decoder on the environment side waiting to receive a message.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.69, len=225, **subst=-0.85**
    > "Channel" language suggests communication symmetry with observation, but the action-environment relationship is fundamentally asymmetric — actions change the environment through an unknown transition function. Wrong metaphor.

  *substance total (R1 + R2):* -3.63


---

### `actuated agent`

*R2 voters:* 3 (2 architectures: gemini, sonnet)

**Candidate: `actuated agent`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=4, mean=2.00, weights=[+3, -1, +3, +3], categories={canonicalize:4}
  > Names the formal Class 2/3 case (agents with both model and objective structure). The defense centers on a deliberate choice over 'purposeful agent' — 'actuated' avoids consciousness baggage while carrying the driven-toward-setpoint shape. The objection raised: the mechanical baggage of 'actuated' overrides the precise AAD boundary the term is meant to establish. Tied to the AAD framework name itself ('Actuation Dynamics'); renaming would cascade into the framework name.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.77, len=208, **subst=1.77**
    > 'Actuated' is the mathematically grounded noun for agents that steer the world toward a setpoint. It anchors the framework name ('Actuation Dynamics') while avoiding the consciousness baggage of 'purposeful'.
  - **sonnet-r2b** (sonnet): +2 ★ *keep* — novelty=0.73, len=235, **subst=1.73**
    > Deliberate avoidance of consciousness/intention baggage while maintaining the mechanical driven-toward-setpoint shape. Tied to the framework name (Actuation Dynamics) — a rename here cascades. The segment's own defense is strong. Keep.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.58, len=277, **subst=1.58**
    > Confirmed by segment. Deliberate choice over "purposeful" — "actuated" avoids consciousness baggage while carrying the driven-toward-setpoint shape. Tied to the AAD framework name (Adaptation and Actuation Dynamics); renaming would cascade into the framework name. Strong keep.

  *substance total (R1 + R2):* 7.08

**Candidate: `Purposeful agent`**
- *R1 synthetic:* **+1** — n=2, mean=1.00, weights=[-1, +3], categories={rename:2}
  > "Actuated" sounds like a motor. Objection: purposeful is a good prose gloss, but as the formal class name it imports consciousness and intention baggage that actuated deliberately avoids.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.55, len=131, **subst=0.77**
    > Good prose gloss. Segment accepts this for natural language. But as the formal class name, imports intention/consciousness baggage.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.81, len=220, **subst=-0.91**
    > Imports consciousness baggage. "Purpose" carries phenomenological weight that "actuated" deliberately avoids — that avoidance is load-bearing for the framework's scope (which applies to thermostats and commanders alike).

  *substance total (R1 + R2):* 0.87

**Candidate: `Goal actuated agent`**
- *R1 synthetic:* **+1** — n=2, mean=1.00, weights=[+1, +1], categories={rename:1, add-alias:1}
  > Keeps the mechanical register while paying the meaning tax sooner; "actuated" alone is a touch too bare on first read. Useful first-contact gloss, but too heavy for canonical use.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.74, len=117, **subst=-0.87**
    > Heavy for canonical use — "goal-actuated" as a first-contact gloss is fine, but the canonical term should be shorter.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.88, len=87, **subst=-0.82**
    > Too verbose for canonical use. Segment confirms "actuated agent" is the canonical form.

  *substance total (R1 + R2):* -0.69

**Candidate: `Autonomous agent`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Self-actuated" is clunky. If it sets its own $O_t$, it possesses true autonomy.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=1.00, len=97, **subst=-0.97**
    > "Autonomous" is overloaded in AI, robotics, and moral philosophy in incompatible ways. Too noisy.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=1.00, len=130, **subst=-1.00**
    > "Autonomous" is already overloaded in AI/robotics. The segment deliberately avoids consciousness baggage; "autonomous" imports it.

  *substance total (R1 + R2):* -1.97

**Candidate: `Self directed agent`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Alternative to autonomous if autonomy is overused.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=1.00, len=170, **subst=-1.00**
    > "Self-directed" implies the agent sets its own objectives, which is the *self-actuated* sub-case. "Actuated agent" includes both externally-tasked and self-tasked agents.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=1.00, len=154, **subst=-1.00**
    > "Self-directed" implies the agent sets its own objectives — this is the "self-actuated" subcategory, not the general actuated agent category. Wrong scope.

  *substance total (R1 + R2):* -2.00


---

### `adaptive cycle`

*R2 voters:* 3 (3 architectures: codex, gemini, opus)

**Candidate: `adaptive cycle`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=4, mean=3.00, weights=[+3, +3, +3, +3, +3], categories={canonicalize:5}
  > Strong central noun phrase: specific enough to own, broad enough to travel across the framework. Strong public noun; it carries both recurrence and unit-of-analysis cleanly. Already well-established across the framework as the fundamental unit of analysis.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *keep* — novelty=0.85, len=103, **subst=1.85**
    > Central unit-of-analysis phrase: one traversal of prolepsis, aisthesis, aporia, epistrophe, and praxis.
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.75, len=148, **subst=1.75**
    > This is the central unit of analysis for the entire framework. It is already well-established and uniquely identifies the 5-phase recurrent process.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.83, len=238, **subst=1.83**
    > Strong central noun. "Adaptive" specifies what the cycle is *for*, "cycle" picks out the unit of analysis. Reads cleanly across registers (engineering, organizational, biological). Pairs with "loop" for the topology/traversal distinction.

  *substance total (R1 + R2):* 7.44

**Candidate: `The cycle the adaptive cycle`**
- *R1 synthetic:* **+1** [invented] — n=1, mean=2.00, weights=[+2], categories={canonicalize:1}
  > The five-phase Prolepsis-Aisthesis-Aporia-Epistrophe-Praxis cycle is "the cycle" or "the adaptive cycle" in the LEXICON and NOTATION. The phrase "the agentic cycle" appears occasionally and overlaps with "the cycle" (post-rename, when ACT was the framework name, "the agentic cycle" meant the ACT-cycle). Canonicalize on "the (adaptive) cycle" — drop "agentic cycle" as a synonym.

- *R2 votes:*
  - **opus-r2c** (opus): +2 *canonicalize* — novelty=0.76, len=266, **subst=1.76**
    > The canonicalize sense is right: standardize on "(the) adaptive cycle" as the canonical phrase; drop residual "agentic cycle" usage (which lingered from the ACT framework-name era). The phrasing of the candidate is awkward but the canonicalize move is the right one.
  - **codex-r2b** (codex): +1 *canonicalize* — novelty=0.87, len=91, **subst=0.85**
    > Correct direction: drop "agentic cycle" drift and standardize on the adaptive cycle family.

  *substance total (R1 + R2):* 3.61

**Candidate: `Feedback cycle`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: considered. Collides with the "feedback loop" structural topology and would create a loop/cycle terminology collision the project has been careful about. Rejected.

- *R2 votes:*
  - **codex-r2b** (codex): -1 *rename* — novelty=0.76, len=74, **subst=-0.65**
    > Collides with loop as topology and would muddy the loop/cycle distinction.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.73, len=215, **subst=-0.86**
    > Collides with the loop/cycle distinction the framework is careful about (loop = feedback topology; cycle = traversal). "Feedback cycle" reads as either "feedback loop" or "cycle within the feedback loop"; ambiguous.

  *substance total (R1 + R2):* -2.52

**Candidate: `Correction cycle`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: considered. "Correction" overspecifies — Section I cycles include observation and prolepsis phases that are not corrections. Adaptation is the broader frame. Rejected.

- *R2 votes:*
  - **codex-r2b** (codex): -1 *rename* — novelty=0.85, len=86, **subst=-0.80**
    > Overspecifies the cycle as correction and drops anticipation, observation, and action.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.71, len=224, **subst=-0.86**
    > "Correction" overspecifies — Section I cycles also include prolepsis (anticipation) and aisthesis (raw perception), which aren't corrections. The five-phase cycle is the *unit of adaptive work*, broader than just correction.

  *substance total (R1 + R2):* -2.65


---

### `adaptive tempo`

*First-encounter locality:* `#def-adaptive-tempo` (Section I; depends on `#emp-update-gain`, `#form-event-driven-dynamics`). First formal definition; The effective rate at which an agent acquires useful information from its environment — the product of observation frequency and update quality across all channels.

*Segment:* [`01-aad-core/src/def-adaptive-tempo.md`](../../01-aad-core/src/def-adaptive-tempo.md)

*R2 voters:* 4 (3 architectures: gemini, opus, sonnet)

**Candidate: `adaptive tempo`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=10, mean=2.92, weights=[+3, +3, +2, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3], categories={canonicalize:13}
  > Names $\mathcal{T} = \sum_k \nu^{(k)} \eta^{(k)\ast}$, the rate-of-useful-info-acquisition quantity. The central argument for the word 'tempo' is that it carries both *rate* and *quality* simultaneously, which is exactly what the formula compounds (rate × quality). The word is underused in the ML literature, which makes it available for AAD to own. Defenders contrast with 'learning rate' (which is $\eta^\ast$, a sub-quantity), 'correction rate', or bare 'tempo'; the canonical form is 'adaptive tempo' bound to $\mathcal{T}$. The Boyd-OODA lineage and the Greek-register fit are secondary supports.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.91, len=189, **subst=1.91**
    > The strongest possible name for $\mathcal{T}$. It perfectly combines 'rate' and 'quality' into a single intuitive term, paying homage to Boyd's OODA loop without inheriting generic baggage.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.67, len=344, **subst=1.67**
    > The word tempo is doing genuinely distinctive work — it carries rate-and-quality simultaneously, which is the structure of $\mathcal T = \sum_k \nu^{(k)} \eta^{(k)\ast}$. "Learning rate" is $\eta^*$, a sub-quantity; "adaptation rate" loses the quality dimension. Tempo is also underused in ML literature, leaving it available without collision.
  - **sonnet-r2b** (sonnet): +2 ★ *keep* — novelty=0.67, len=324, **subst=1.67**
    > "Tempo" carries both rate and quality simultaneously — exactly what T = Σ ν^(k) η^(k)* compounds. "Adaptive" distinguishes it from "tempo" in music or sports. The Boyd-OODA lineage is apt: the OODA loop's tempo is about quality of cycling, not just frequency. The word is underused in ML, making it available for AAD to own.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.80, len=246, **subst=1.80**
    > Confirmed by segment. "Tempo" uniquely carries rate AND quality simultaneously. Boyd connection is live: "grounds Boyd's emphasis on Orient quality over raw OODA speed." Available term — underused in ML/AI literature, AAD can own it. Strong keep.

  *substance total (R1 + R2):* 9.04

**Candidate: `tempo`**
- *R1 synthetic:* **+1** [excavated] — n=1, mean=3.00, weights=[+3], categories={canonicalize:1}
  > "Tempo" is a fantastic foundational term.

- *R2 votes:*
  - **opus-r2c** (opus): +1 *add-alias* — novelty=0.96, len=347, **subst=0.98**
    > The bare "tempo" works fine in prose where context disambiguates against strategic tempo / adversarial tempo. As an alias of adaptive tempo specifically, defensible — the modifier is sometimes redundant. Not the canonical name (you want "adaptive tempo" canonicalized for new readers), but the bare "tempo" is fine where the adjective is implicit.
  - **sonnet-r2b** (sonnet): +1 *keep* — novelty=0.94, len=146, **subst=0.97**
    > Works as a shortened form in prose after "adaptive tempo" has been established. Good for the LEXICON and for repeated references in long passages.
  - **sonnet-r2c** (sonnet): +1 *add-alias* — novelty=0.95, len=155, **subst=0.98**
    > Good informal alias; "tempo" alone works in prose once "adaptive tempo" is established. But the adjective is needed to distinguish 𝒯 from raw event rate ν.

  *substance total (R1 + R2):* 3.93

**Candidate: `Adaptation rate`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: loses the "rate × quality" compound the tempo metaphor delivers. Reject.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.74, len=153, **subst=-0.87**
    > Loses the rate-and-quality compound. The whole point of choosing "tempo" over "rate" is that adaptive tempo *isn't* just a rate; it's gain-weighted rate.
  - **sonnet-r2b** (sonnet): -1 *keep* — novelty=0.82, len=198, **subst=-0.91**
    > "Adaptation rate" flattens the compound — tempo is rate × quality, not just rate. This would be like naming η* "update quantity" instead of "update gain." The quality component (η*) is load-bearing.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.91, len=143, **subst=-0.96**
    > Names only ν (loop rate), drops η* (quality). The segment confirms: 𝒯 = ν · η* is a product of both. "Adaptation rate" is a different quantity.

  *substance total (R1 + R2):* -3.73


---

### `adversarial tempo advantage`

*First-encounter locality:* `#result-adversarial-tempo-advantage` (Section III; depends on `#hyp-mismatch-dynamics`, `#der-adversarial-destabilization`, `#result-persistence-condition`). First formal result; Under adversarial coupling where one agent's actions contribute to the other's disturbance rate, the steady-state mismatch ratio scales superlinearly with the tempo ratio.

*Segment:* [`01-aad-core/src/result-adversarial-tempo-advantage.md`](../../01-aad-core/src/result-adversarial-tempo-advantage.md)

*R2 voters:* 2 (2 architectures: gemini, sonnet)

**Candidate: `adversarial tempo advantage`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=5, mean=2.33, weights=[+3, +3, +1, +1, +3, +3], categories={canonicalize:6}
  > Clear and memorable. Keep. Superlinear tempo advantage.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.94, len=161, **subst=1.94**
    > Naming the specific domain ('adversarial') is better than naming the mathematical outcome ('superlinear'). It frames the context of the superlinearity correctly.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.86, len=278, **subst=1.86**
    > Confirmed from hyp-mismatch-dynamics and result-persistence-condition. Superlinear scaling is the mathematical result (Model D: squared, Model S: 3/2). "Adversarial tempo advantage" names both the mechanism (adversarial coupling) and the property (tempo advantage). Strong keep.

  *substance total (R1 + R2):* 5.80

**Candidate: `Superlinear tempo advantage`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Highlights the mathematical outcome (superlinear) of the advantage.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.82, len=220, **subst=0.91**
    > Names the mathematical property. But "adversarial" is the cause of the superlinearity; "superlinear tempo advantage" without "adversarial" loses the mechanism. Good as an alias for the mathematical property specifically.

  *substance total (R1 + R2):* 0.91

**Candidate: `Tempo advantage`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Adversarial" is context, "tempo advantage" is the core concept.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.80, len=175, **subst=-0.90**
    > "Adversarial" is load-bearing — it specifies the two-agent context (A's actions contribute to B's disturbance). Without it, "tempo advantage" could mean simple relative speed.

  *substance total (R1 + R2):* -0.90


---

### [Concept] *Agent classes: Class 1 / 2 / 3*

*R2 voters:* 3 (3 architectures: gemini, opus, sonnet)

**Candidate: `Architectural classes`** ▸ leader
- *R1 synthetic:* **+1** [invented] — n=1, mean=2.00, weights=[+2], categories={canonicalize:1}
  > Currently "agent classes," "architecture classes," "class 1/2/3," and "architectural classification" are all in use across `#der-directed-separation`. Canonicalize: "architectural classes" or "the architectural classification (Class 1 / Class 2 / Class 3)" — the *agent* class wording can collide with the LEXICON's "agent classes" table (adaptive system / agentic system / actuated agent / etc.) which is a different decomposition. Keep them disambiguated in prose.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *rename* — novelty=0.82, len=216, **subst=1.82**
    > 'Architectural classes' is the best collective handle. It correctly labels the Class 1/2/3 split as a structural design property. Using 'Architecture' distinguishes it from the 'Agent spectrum' (functional taxonomy).
  - **sonnet-r2b** (sonnet): +2 ★ *canonicalize* — novelty=0.69, len=473, **subst=1.69**
    > The right umbrella term — "architectural" signals these are determined by processing topology, not by performance or task. Disambiguates from the LEXICON's agent-type classification (adaptive system / agentic system / actuated agent) which uses "agent classes" in a different sense. The canonical prose form "the architectural classification (Class 1 / Class 2 / Class 3)" with canonical English modifiers (modular / merged / partially modular) is the right implementation.
  - **opus-r2c** (opus): +1 *canonicalize* — novelty=0.93, len=232, **subst=0.97**
    > Same as "Architecture classes" — canonical umbrella name. The two variants ("architecture classes" / "architectural classes") should be standardized; both candidates are essentially the same proposal with adjective-vs-noun phrasing.

  *substance total (R1 + R2):* 5.47

**Candidate: `Proposal assign english modifier`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={name-unnamed:1}
  > Class-numbered labels work but lack mnemonic grip. Proposal: retain "Class 1 / 2 / 3" as the primary labels but assign canonical one-word modifiers — **modular** (Class 1), **merged** (Class 2), **partial** (Class 3) — that are already used descriptively. Adopt them as the *canonical* prose forms: "modular agents" / "merged agents" / "partially-modular agents" or "partial-mix agents." Class 2 especially benefits: "fully merged" currently appears; normalize to just "merged.".

- *R2 votes:*
  - **opus-r2c** (opus): +2 *add-alias* — novelty=0.81, len=544, **subst=1.81**
    > Strong vote: keep Class 1/2/3 as compact labels for cross-references and structural-position language ("the Class 2 scope exit applies here"), but make modular / merged / partial the canonical *prose* forms ("a modular agent", "a merged agent"). Both layers earn their keep — the numbered labels for diagrams and structural references; the English modifiers for running prose. The principles file's rename example argued *replace* the numbering; I think *both* is better, with the English modifiers getting the prose-form-by-default discipline.
  - **sonnet-r2b** (sonnet): +2 *canonicalize* — novelty=0.57, len=378, **subst=1.57**
    > Not a candidate name but the right proposal: assign canonical English modifiers alongside the Class 1/2/3 numbers. Modular / merged / partially modular. Class 2 especially benefits: "fully merged" is already used; normalize to "merged." These one-word modifiers let prose say "merged agents" rather than "Class 2 agents" when the architecture matters more than the class number.

  *substance total (R1 + R2):* 3.39

**Candidate: `Architecture classes`**
- *R1 synthetic:* **+1** [excavated] — n=1, mean=2.00, weights=[+2], categories={canonicalize:1}
  > Canonical umbrella helps avoid overloading class numbers across sections.

- *R2 votes:*
  - **opus-r2c** (opus): +1 *canonicalize* — novelty=0.93, len=201, **subst=0.96**
    > The umbrella term reads cleanly. Useful as the collective name *if* the Class 1/2/3 numbering itself is kept (and individual rows give them English modifiers). Acceptable canonicalize for the umbrella.
  - **sonnet-r2b** (sonnet): +1 *canonicalize* — novelty=1.00, len=106, **subst=1.00**
    > Acceptable but "architectural classes" (with -al) is slightly more natural English for the adjectival use.

  *substance total (R1 + R2):* 2.96

**Candidate: `Goal entanglement hierarchy`**
- *R1 synthetic:* **+1** [invented] — n=1, mean=3.00, weights=[+3, +3], categories={canonicalize:1, rename:1}
  > Standardizing the previously resolved rename. Directly describes what the classes measure (how much $G_t$ entangles with $M_t$ updates).

- *R2 votes:*
  - **opus-r2c** (opus): +2 ★ *rename* — novelty=0.87, len=511, **subst=1.87**
    > The principles file's example rename. The three classes *measure* exactly this: how much G_t entangles with M_t processing. "Goal entanglement hierarchy" names what the classes pick out (the entanglement axis), not just an arbitrary label set. The reader who hears "Class 2" needs to memorize what Class 2 means; the reader who hears "high goal-entanglement" can derive what's happening from the name. The trade — citation-friction on a small body of recent prose vs decoder-ring cost forever — favors renaming.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.96, len=149, **subst=-0.98**
    > "Hierarchy" implies ordering from better to worse; the classes are not ranked. "Entanglement" imports quantum-information connotations unnecessarily.

  *substance total (R1 + R2):* 1.89

**Candidate: `Architectural partition`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={name-unnamed:1}
  > Symbols stay (Class 1/2/3); prose gets "the architectural partition" as a collective handle. Avoids "architecture hierarchy" (hierarchy overload) while naming the three-way structure.

- *R2 votes:*
  - **opus-r2c** (opus): +1 *rename* — novelty=0.86, len=271, **subst=0.93**
    > Acceptable alternative for the umbrella name — "partition" emphasizes the discrete-three-way-split structure (what makes this a *partition* and not a continuum). "Architectural partition" works if the rename to "goal entanglement hierarchy" doesn't land. Mild preference.
  - **sonnet-r2b** (sonnet): +1 *canonicalize* — novelty=0.79, len=198, **subst=0.90**
    > Good alternative. "Partition" emphasizes the three-way decomposition. Slightly less natural in prose ("the agent belongs to the modular architectural partition" vs "the agent is Class 1 / modular").

  *substance total (R1 + R2):* 1.83

**Candidate: `Modularity partition`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > Classes are precisely modular, partially modular, and merged.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +1 *rename* — novelty=0.93, len=139, **subst=0.96**
    > Precise — the classes are defined by degree of modularity. Slightly less recognizable than "architectural classes" which is already in use.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.92, len=256, **subst=-0.96**
    > "Modularity" centers the modular axis but Class 2 is *merged*, not "non-modular" — the partition isn't really along a modularity continuum but along where G_t and M_t-processing entangle. "Modularity partition" undersells Class 2's structural distinctness.

  *substance total (R1 + R2):* 1.00


---

### `agent model`

*First-encounter locality:* `#form-agent-model` (Section I; depends on `#def-agent-environment`, `#def-observation-function`, `#def-chronica`). Formal model first introduced; The agent's compressed representation of how the world works, mapping interaction history to model space.

*Segment:* [`01-aad-core/src/form-agent-model.md`](../../01-aad-core/src/form-agent-model.md)

*R2 voters:* 4 (4 architectures: codex, gemini, opus, sonnet)

**Candidate: `Reality model`** ▸ leader
- *R1 synthetic:* **+1** — n=2, mean=0.50, weights=[+2, -1], categories={rename:2}
  > The segment title and content name the agent's reality model, not a generic agent model. Objection: considered and rejected — the segment's title is "Formulation: The Reality Model" but the slug is more precise.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *rename* — novelty=0.81, len=141, **subst=1.81**
    > Better canonical prose name for `#form-agent-model`: self-descriptive, aligned with the segment title, and clear about what $M_t$ represents.
  - **gemini-r2** (gemini): +2 ★ *canonicalize* — novelty=0.77, len=225, **subst=1.77**
    > 'Agent model' is ambiguous—does it mean a model *of* the agent or the model held *by* the agent? 'Reality model' perfectly captures the segment title and the formulation $M_t = \phi(C_t)$, which bridges the agent to $\Omega$.
  - **opus-r2b** (opus): +2 ★ *rename* — novelty=0.87, len=401, **subst=1.87**
    > Promotes the segment's own title to the slug. The README's quantity table glosses $M_t$ as "Reality model — Compressed history capturing predictive information." The LEXICON Cycle Phases entry for prolepsis cites $M_{t-1}$ as the basis for the prediction. Three project-level documents converge on "reality model"; the slug should match. The "of-what-not-whose" disambiguation is the substantive gain.
  - **sonnet-r2b** (sonnet): +2 ★ *rename* — novelty=0.84, len=334, **subst=1.84**
    > The segment itself calls this "The Reality Model" in its title. "Reality model" names what $M_t$ is *of*: reality, the external environment. Survives the communal-imagination test — "the agent's reality model was updated" reads naturally. The contrast with the goal state $G_t$ is clearer: model of reality vs model of desired future.

  *substance total (R1 + R2):* 8.28

**Candidate: `agent model`**
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=5, mean=1.80, weights=[+1, +1, +3, +3, +1], categories={canonicalize:5}
  > Compressed history as state. Keep. Defended keep.

- *R2 votes:*
  - **codex-r2b** (codex): -1 *keep* — novelty=0.94, len=139, **subst=-0.97**
    > Ambiguous: it can read as a model *of* an agent. The segment title and prose define the agent's model of reality, compressed from chronica.
  - **opus-r2b** (opus): -1 *rename* — novelty=1.00, len=328, **subst=-1.00**
    > "Agent model" is ambiguous: model *belonging to* the agent vs model *of* the agent. The segment is unambiguous about which — $M_t$ is the agent's representation *of the environment*. The slug should disambiguate. Also: the segment title, the README vocabulary table, and LEXICON all use "reality model"; the slug is the outlier.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=1.00, len=252, **subst=-1.00**
    > "Agent model" is too generic — any agent's model of anything. This segment is specifically about the agent's model of reality/the environment. The name loses the key distinction between the model-of-reality ($M_t$) and the goal/strategy states ($G_t$).

  *substance total (R1 + R2):* -1.97


---

### `agent opacity`

*First-encounter locality:* `#der-agent-opacity` (Section III; deep dependency cone (7 upstream segments incl. `#scope-agent-identity`, `#der-interaction-channel-classification`)). First formal derivation; Alongside AAD's heavily formalized *forward* observation quality (how well the agent sees the world — observation ambiguity, model-class fitness, identifiability floor on what the agent can infer),….

*Segment:* [`01-aad-core/src/der-agent-opacity.md`](../../01-aad-core/src/der-agent-opacity.md)

*R2 voters:* 2 (2 architectures: gemini, opus)

**Candidate: `agent opacity`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=13, mean=2.64, weights=[+3, +3, +3, +2, +3, +1, +2, +3, +3, +3, +2, +3, +3, +3], categories={canonicalize:14}
  > Adopted from Hafez 2026 ($H_b^{A|B}$, backward predictive uncertainty). The case for keeping is twofold: prior-art-integration convention forbids renaming adopted concepts with proper attribution, and the word 'opacity' carries exactly the right intuition — the dual of observability — for the emitter side. Pairs naturally with 'transparency' as the opposite, with observation-quality $U_o$ as the formal dual, and reads naturally in adversarial contexts ('adversaries want opacity; cooperators want transparency'). The dual framing is load-bearing in Section III.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.88, len=172, **subst=1.88**
    > The prior-art integration principle is absolute here. Hafez 2026 defines $H_b$. Keeping the name honors the external theorem while AAD provides the new indexing extensions.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.69, len=401, **subst=1.69**
    > Adopted from Hafez 2026 with attribution; the prior-art-integration convention recommends keeping. "Opacity" is the right dual of observation quality $U_o$ — pairs cleanly with the "agents want either transparency (cooperative) or opacity (adversarial)" framing the segment uses. The ladder of opacities (transition / epistemic / agent) gives the framework a coherent who-is-opaque-to-whom vocabulary.

  *substance total (R1 + R2):* 5.56

**Candidate: `Emitter opacity`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Disambiguates emitter-side from recipient-side in the 16-cell composition. Parallel with #recipient-regime-classification above.

- *R2 votes:*
  - **opus-r2c** (opus): +1 *add-alias* — novelty=0.70, len=204, **subst=0.85**
    > Useful disambiguator in 16-cell emitter-recipient composition contexts. As a parallel handle for the emitter-side specifically, defensible. Not as the canonical name (the bare "agent opacity" is broader).

  *substance total (R1 + R2):* 0.85

**Candidate: `Strategic opacity`**
- *R1 synthetic:* **0** — n=2, mean=0.00, weights=[-1, +1], categories={rename:2}
  > "Agent opacity" is broad. Objection: too narrow.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.85, len=266, **subst=-0.92**
    > "Strategic" narrows what the segment is about — agent opacity is the broad quantity, with adversarial / cooperative / strategic settings as scope-specializations. The umbrella stays "agent opacity"; "strategic opacity" could be a sub-case but not the canonical name.

  *substance total (R1 + R2):* -0.92

**Candidate: `Legibility inverse`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: considered (variant of "legibility-inverted"). "Legibility" is Codex's framing for the dual; "inverse" makes the duality explicit. Rejected (same as r1): loses the formal-quantity grounding ($H_b$). The segment names $H_b$ as a *first-class* multi-agent quantity (Hafez et al. 2026 adoption); the slug should name the quantity, not the dual relation.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.92, len=37, **subst=-0.36**
    > Same critique as Legibility inverted.

  *substance total (R1 + R2):* -1.36

**Candidate: `Backward predictive uncertainty`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: considered. The actual definition: $H_b^{A \mid B}(t, \tau) := H(a_{A, t+\tau} \mid \mathcal F_B^t)$ — entropy of $A$'s future action given $B$'s filtration. "Backward predictive uncertainty" is the literal description. Rejected: "agent opacity" is the prose handle the segment uses; "backward predictive uncertainty" reads clinical.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.83, len=95, **subst=-0.87**
    > Clinical and reads as a literal definition rather than a name. The rationale's rejection holds.

  *substance total (R1 + R2):* -1.87

**Candidate: `Legibility inverted`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: considered. More plain-English but loses the formal-quantity grounding ($H_b$). Rejected.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.81, len=111, **subst=-0.90**
    > Drops the $H_b$ grounding; AAD's segment names the quantity (which is the Hafez import), not the dual relation.

  *substance total (R1 + R2):* -1.90


---

### `agent spectrum`

*First-encounter locality:* `#def-agent-spectrum` (Section II; depends on `#def-agent-environment`, `#form-agent-model`). First formal definition; Two independent dimensions — model richness and objective richness — create a spectrum from reactive systems through purposeful agents. These are regions of a continuum, not discrete categories.

*Segment:* [`01-aad-core/src/def-agent-spectrum.md`](../../01-aad-core/src/def-agent-spectrum.md)

*R2 voters:* 4 (3 architectures: gemini, opus, sonnet)

**Candidate: `agent spectrum`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=9, mean=2.00, weights=[+1, +3, +2, +1, +3, +1, +2, +2, +1, +3, +3], categories={canonicalize:11}
  > Names the ±model × ±objective 2×2 picture. The defense centers on 'spectrum' being accurate: the segment explicitly treats the four corners as continuous regions, not discrete categories, so 'quadrants' or 'partition' or 'typology' would mis-describe what the segment is doing. Considered alternatives ('agent quadrants', 'agent types-partition', 'agent classification') were judged worse on this exact dimension. Variants in prose ('agent quadrant', 'agent typology', 'agent classification') need standardizing on the canonical form.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.92, len=152, **subst=1.92**
    > Accurate and established. 'Spectrum' correctly captures the continuous nature of the richness dimensions, avoiding the false discreteness of 'quadrant'.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.81, len=209, **subst=1.81**
    > "Spectrum" is right for what the segment claims — continuous regions, not discrete categories. Standardize over residual paraphrases ("quadrant", "typology", "classification") which all flatten the continuity.
  - **sonnet-r2b** (sonnet): +2 ★ *keep* — novelty=0.86, len=342, **subst=1.86**
    > The segment is explicit: these are regions of a continuum. "Spectrum" is the right word. "Quadrant" implies discrete corners; "typology" implies classification schema; both would misrepresent the segment's continuity claim. The word "spectrum" in the name signals to readers that gradations are real and migration between regions is possible.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.72, len=208, **subst=1.72**
    > Confirmed by segment. "Spectrum" is accurate — model richness × objective richness form continuous axes. The segment explicitly calls the four corners "idealized regions" not discrete categories. Strong keep.

  *substance total (R1 + R2):* 9.31

**Candidate: `Agency spectrum`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > The segment maps richness of agency, not a zoology of agent types.

- *R2 votes:*
  - **opus-r2c** (opus): +1 *rename* — novelty=0.81, len=217, **subst=0.90**
    > "Agency" picks out the *quality* (richness of agency) over "agent" (the entity having it). Slight preference axis-wise, but "agent spectrum" is more grounded in segment-language and pairs with #scope-agency naturally.
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.76, len=200, **subst=0.88**
    > Alternative that emphasizes "richness of agency." But "agent spectrum" is about the range of agent TYPES; "agency spectrum" would suggest a grading of agency-quality. Different emphasis, less precise.
  - **sonnet-r2b** (sonnet): -1 *keep* — novelty=0.85, len=195, **subst=-0.92**
    > Shifts focus to the degree of agency rather than the types/positions within the agent space. The spectrum is in the *agent space* (agents at different points), not in the *agency property* alone.

  *substance total (R1 + R2):* 0.86

**Candidate: `Agent quadrant`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: considered and rejected — see above; quadrants oversells discreteness.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.89, len=216, **subst=-0.94**
    > "Quadrants" oversells discreteness; the segment's substance is that the ±model × ±objective regions are continuous. Quadrants would force re-explaining "we don't actually mean discrete categories" on every encounter.
  - **sonnet-r2b** (sonnet): -1 *keep* — novelty=0.85, len=68, **subst=-0.63**
    > Oversells discreteness. The segment explicitly rejects this framing.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.95, len=128, **subst=-0.98**
    > Correctly rejected in card. "Quadrant" implies discrete categories; the segment explicitly calls these "regions of a continuum."

  *substance total (R1 + R2):* -3.55


---

### [Concept] *Agentic Systems Framework (ASF) — top-level*

*R2 voters:* 3 (2 architectures: gemini, opus)

**Candidate: `Agentic system framework`** ▸ leader
- *R1 synthetic:* **0** [invented] — n=1, mean=1.00, weights=[+1], categories={canonicalize:1}
  > Keep. "Agentic Systems" reads cleanly as the project name; ASF acronym is workable. The word "agentic" is currently a buzzword, but AAD is positioned to *ground it formally* (README §agency-scope) rather than be captured by it — the framework's willingness to define the term precisely is a positive.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.97, len=69, **subst=1.36**
    > The full title of the framework should remain descriptive and formal.
  - **opus-r2b** (opus): +2 ★ *keep* — novelty=0.73, len=387, **subst=1.73**
    > Defended keep. ASF is the intentional parent name (AAD = Part I, TST = Part II); naming-principles.md notes earlier rounds misread it as debt. The "agentic" lexeme is currently a buzzword, but the framework's response is to *ground it formally* via Pearl-L2 contrast at #scope-agency — which converts an opportunistic word into a precise term. Renaming would forfeit that grounding move.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.84, len=350, **subst=1.84**
    > The "agentic" buzzword problem is real but doesn't argue for a rename — the framework explicitly grounds the term (#scope-agency narrows it to "adaptive + at least binary action choice + at least one Pearl-Level-2 contrast"). That's the right move: take the popular term and supply a precise referent rather than coin a new word that competes weakly.

  *substance total (R1 + R2):* 4.93


---

### `aisthesis`

*R2 voters:* 3 (2 architectures: gemini, opus)

**Candidate: `aisthesis`** ▸ leader
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=3, mean=1.33, weights=[+1, +2, +1], categories={canonicalize:3}
  > Slightly less sticky than the other Greek phase names, but it preserves the raw-contact distinction well enough to keep. Good phase term for perception. `LEXICON.md`: "Raw contact with reality: observation $o_t$ arrives." The point of the term is to mark *unmediated* observation arrival before the agent has done any interpretation — αἴσθησις is precisely that pre-conceptual contact.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.87, len=158, **subst=1.87**
    > Part of the foundational Greek register (aporia/prolepsis/aisthesis/epistrophe/praxis). It perfectly names the moment of raw, unmediated contact with reality.
  - **opus-r2b** (opus): +2 ★ *keep* — novelty=0.74, len=324, **subst=1.74**
    > Greek-vocabulary commitment. Slightly less sticky than aporia/praxis but preserves the raw-contact distinction well enough — "the moment of arrival before interpretation begins." The pre-conceptual quality is the load-bearing content; English alternatives (perceive, sense, intake, observe) all carry interpretation baggage.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.86, len=367, **subst=1.86**
    > Of the five phase names, aisthesis is the least familiar English-side, but it does load-bearing work: the moment of *unmediated arrival* is precisely what the phase is for, and English alternatives ("perception", "observation") all carry interpretive baggage that puts processing inside the phase. The Greek family's coherence dominates the slight unfamiliarity cost.

  *substance total (R1 + R2):* 6.47

**Candidate: `Aisthesis observation alignment`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={add-alias:1}
  > Clarifies the raw contact aspect.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.90, len=232, **subst=-0.95**
    > Verbose; "observation alignment" is also misleading — aisthesis is *raw contact*, not alignment. The segment is precise: "Raw contact with reality: observation $o_t$ arrives." Pre-conceptual, unmediated. "Alignment" is a later move.
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=63, **subst=-0.63**
    > Same compound-name problem; the Greek term is the working name.

  *substance total (R1 + R2):* -0.58

**Candidate: `Intake`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: considered. Plain-English candidate that names the moment-of-arrival cleanly. Rejected because the five-phase Greek family becomes incoherent if one term breaks register, and "intake" sacrifices the philosophical lineage that motivates the family.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.78, len=328, **subst=-0.89**
    > Breaking register on one of the five Greek terms breaks the entire family's coherence. "Intake" is a fine plain-English handle but loses the philosophical lineage (αἴσθησις, the pre-conceptual contact) and the family's distinctive identifying register. The whole pentad has to keep its register or the framework loses its voice.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.78, len=258, **subst=-0.89**
    > Breaks the family register; even granting "intake" picks out the right English moment, switching one phase out of Greek into industrial-bureaucratic register damages the others' coherence. The five-phase family is a system, not five independent name choices.

  *substance total (R1 + R2):* -2.78


---

### `aporia`

*R2 voters:* 3 (2 architectures: gemini, opus)

**Candidate: `aporia`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=6, mean=3.00, weights=[+3, +3, +3, +3, +3, +3], categories={canonicalize:5, rename:1}
  > Cycle-phase Greek vocabulary works aesthetically AND technically. This earns its weight. Memorable, discussable, and conceptually richer than "error" or "mismatch.".

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.96, len=123, **subst=1.96**
    > Part of the core Greek register. It perfectly captures the moment of productive perplexity that drives the adaptive update.
  - **opus-r2b** (opus): +2 ★ *keep* — novelty=0.85, len=319, **subst=1.85**
    > Load-bearing keep. The Greek term names the cycle phase; "prediction error" and "mismatch" both miss the productive-perplexity load. The framework's commitment to the Greek-rooted vocabulary (naming-principles invariants) is at its strongest here — aporia is the most-distinct-from-flat-English of the five cycle terms.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.95, len=308, **subst=1.95**
    > This is the phase name doing the most non-obvious work in the five-name set. "Mismatch" is the *signal* (fine — that's a separate term). "Aporia" is the *phase* during which the agent registers a gap as something to update from. The phase/signal split would collapse if both were named the same English word.

  *substance total (R1 + R2):* 7.76

**Candidate: `Aporia productive perplexity`**
- *R1 synthetic:* **+1** — n=1, mean=3.00, weights=[+3], categories={add-alias:1}
  > Explicitly adding this translation ensures "perplexity" is seen as generative.

- *R2 votes:*
  - **opus-r2b** (opus): +1 *canonicalize* — novelty=0.89, len=247, **subst=0.95**
    > Same rationale as row 31: pair-on-first-use form. The translation cue tells readers "perplexity" here is *generative*, not "I am confused and stuck." Useful for new readers; the bare "aporia" is fine in segments where the term has been introduced.
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=147, **subst=-1.00**
    > Same critique as the praxis-informed-action variant: the bare Greek term is the working name, the doubled-up form is wordy and weakens both halves.

  *substance total (R1 + R2):* 0.95

**Candidate: `Discrepancy`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: considered. Names the gap but loses the agent-centered "this matters / I now must update" sense. Rejected.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.68, len=162, **subst=-0.84**
    > Names the *gap* but loses the agent-centered "this is generative; I now must update" connotation that makes aporia distinct. Flattens what the Greek term carries.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.93, len=200, **subst=-0.97**
    > "Discrepancy" loses the productive sense — the phase name is doing work because aporia means *productive* perplexity (the disturbance that prompts the next move), not just a measurement-of-error word.

  *substance total (R1 + R2):* -2.81


---

### `aporia prolepsis aisthesis epistrophe praxis`

*R2 voters:* 2 (2 architectures: opus, sonnet)

**Candidate: `aporia prolepsis aisthesis epistrophe praxis`** ▸ leader
- *R1 synthetic:* **+1** [is_keep] [invented] — n=1, mean=3.00, weights=[+3], categories={canonicalize:1}
  > [prose moved from candidate column]: "*(keep as a set)*" — The Greek cycle-phase vocabulary works *because* it refuses the flatness of "predict / observe / mismatch / update / act." The README §"Why these terms earn their weight" is load-bearing justification and should not be touched. Keep all five.

- *R2 votes:*
  - **opus-r2b** (opus): +2 ★ *keep* — novelty=0.84, len=451, **subst=1.84**
    > Keep all five as a set. The README §"Why these terms earn their weight" is load-bearing rationale; the LEXICON's per-phase entries are tight. Any individual translation flattens — "anticipation" misses the active-future-preparation of *prolepsis*; "perception" misses the raw-contact-with-reality of *aisthesis*; "turning toward" comes closest to *epistrophe* but English still feels weaker. The set has aged into the framework's identifying register.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.84, len=388, **subst=1.84**
    > The five-phase Greek vocabulary is one of the project's most load-bearing naming decisions. Each term names a real distinction the formalism makes that English alternatives flatten: aporia is "productive perplexity," not just "prediction error"; epistrophe is "turning toward reality," not just "updating." The README's case is correct. Strong keep on the whole set and each individually.

  *substance total (R1 + R2):* 4.68

**Candidate: `Greek rooted vocabulary`**
- *R1 synthetic:* **+1** [invented] — n=1, mean=3.00, weights=[+3], categories={canonicalize:1}
  > Collectivizes the five distinctive process stages.

- *R2 votes:*
  - **opus-r2b** (opus): +1 *canonicalize* — novelty=1.00, len=230, **subst=1.00**
    > Decent collective handle for the cycle vocabulary as a project commitment. Useful in CLAUDE / naming-principles meta-discussions where the choice is being defended. Not a renaming move; a way to refer to the commitment as a thing.
  - **sonnet-r2c** (sonnet): +1 *keep* — novelty=1.00, len=138, **subst=1.00**
    > Acceptable as a collective label for prose references to the set, but the individual terms are the actual vocabulary; this is a meta-name.

  *substance total (R1 + R2):* 3.00


---

### `ASF (acronym)`

*R2 voters:* 4 (4 architectures: codex, gemini, opus, sonnet)

**Candidate: `ASF`** ▸ leader
- *R1 synthetic:* **+1** [invented] — n=2, mean=2.50, weights=[+3, +2], categories={canonicalize:2}
  > Agentic Systems Framework. Acceptable keep.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *keep* — novelty=0.77, len=111, **subst=1.77**
    > Good parent-framework acronym for the broader Agentic Systems Framework around AAD and its domain applications.
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.90, len=160, **subst=1.90**
    > Though I voted to name the parent container 'Agentic system', the acronym ASF is widely used and provides a clean, 3-letter handle for the framework as a whole.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.93, len=431, **subst=1.93**
    > ASF is the *intentional* parent-level name (per CLAUDE.md and README): AAD is Part I, TST is Part II, logogenic and logozoetic are Parts III–IV. Earlier rounds misread it as debt; it isn't. The acronym is short, says what it is, and the "Agentic Systems" expansion is doing real work distinguishing the framework from "Agentic Cycle" (the old ACT framing) — agentic-system is the substrate, the cycle is the unit of analysis on it.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.93, len=243, **subst=1.93**
    > Clean, unambiguous, and serves the correct purpose: marking the parent-level framework name as distinct from AAD (the mathematical core). Earlier rounds misread ASF as debt; the CLAUDE.md clarification that ASF is intentional is correct. Keep.

  *substance total (R1 + R2):* 8.53


---

### `calibration laboratory`

*R2 voters:* 3 (2 architectures: codex, opus)

**Candidate: `calibration laboratory`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=11, mean=2.75, weights=[+3, +3, +3, +3, +3, +2, +3, +1, +3, +2, +3, +3, +3, +3, +3, +3], categories={canonicalize:10, add-alias:1, rename:3, name-unnamed:2}
  > TST framing-vocabulary phrase: software is AAD's privileged high-identifiability calibration laboratory. Defenders argue 'laboratory' is the right metaphor — software has high identifiability, clean instrumentation, and supports exact measurement of AAD quantities — and that the phrase deserves promotion to a stable short name central to TST's architectural role. Variants in prose ('richest operationalization domain', 'best operationalization domain', 'privileged high-identifiability calibration laboratory') need standardizing on 'calibration laboratory' as the canonical short form, with 'privileged high-identifiability calibration laboratory' available as the modifier expansion when context warrants.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *canonicalize* — novelty=0.77, len=109, **subst=1.77**
    > Best short form for TST's role: the high-identifiability domain where AAD quantities can be measured cleanly.
  - **opus-r2b** (opus): +2 ★ *canonicalize* — novelty=0.76, len=462, **subst=1.76**
    > The phrase already does work in CLAUDE.md ("calibration laboratory framing"), README, TST OUTLINE preamble, and elsewhere. Variants ("richest operationalization domain," "best operationalization domain," "privileged high-identifiability calibration laboratory") exist; canonicalize forces the short form to be the one used in prose. Promoting the prose form to formal naming is exactly the canonicalize-with-organic-provenance case the principles file describes.
  - **opus-r2c** (opus): +2 ★ *canonicalize* — novelty=0.69, len=407, **subst=1.69**
    > Strong canonicalize over "richest operationalization domain", "best operationalization domain", "privileged high-identifiability calibration laboratory". The shorter form is what should appear in headings and in-running prose; the long form is fine as one-time expansion. The metaphor lands: software has clean instrumentation, exact measurement, controlled interventions — exactly what a laboratory is for.

  *substance total (R1 + R2):* 7.22

**Candidate: `Software as calibration laboratory`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={name-unnamed:1}
  > The TST preamble names software as AAD's "privileged high-identifiability calibration laboratory," and CLAUDE.md says "calibration-lab framing" is a methodology principle. There is no single segment, slug, or principle entry that names this commitment — it is a load-bearing methodological move that lives only in preambles and the README. Promoting it to a named principle (likely a `disc-` or `norm-` segment, or a methodological entry in CLAUDE.md / FORMAT.md) would let downstream segments cite it explicitly when invoking it.

- *R2 votes:*
  - **codex-r2b** (codex): +1 *name-unnamed* — novelty=0.96, len=110, **subst=0.98**
    > The methodological commitment is real, though this phrase is better explanatory prose than the canonical term.
  - **opus-r2b** (opus): +1 *canonicalize* — novelty=0.92, len=249, **subst=0.96**
    > Fully-qualified form. Pairs nicely with sentences like "TST is positioned as software-as-calibration-laboratory." The bare "calibration laboratory" loses the "software" anchor; this form keeps it. Useful as the long-form citation handle in segments.
  - **opus-r2c** (opus): +1 *name-unnamed* — novelty=0.87, len=320, **subst=0.93**
    > This is genuinely a different target — not the laboratory itself but the *methodological move* of treating one domain as the calibration laboratory for cross-domain machinery. As a name for that meta-move, defensible. Belongs in its own row (probably the methodology / CLAUDE.md / FORMAT.md layer), not as a rename here.

  *substance total (R1 + R2):* 3.87

**Candidate: `Calibration laboratory move`**
- *R1 synthetic:* **+1** [invented] — n=1, mean=2.00, weights=[+2], categories={canonicalize:1}
  > Confirmation with new reasoning — my own r2 named "software-as-calibration-laboratory" as a name-unnamed; reading peers, Codex (+3) and Sonnet (+3) and Gemini (+3) all separately reached "calibration laboratory" as a canonicalize vote. Three agents converging on the canonical phrase suggests the term is ripe; what's *unnamed* is the methodological *move* of using software as the calibration laboratory rather than just an instance. Calling it "the calibration-laboratory move" lets it function as a named strategic principle the project can invoke.

- *R2 votes:*
  - **codex-r2b** (codex): +1 *name-unnamed* — novelty=0.94, len=104, **subst=0.97**
    > Reasonable process-name for grounding AAD in high-identifiability software if a principle slot is added.
  - **opus-r2b** (opus): +1 *name-unnamed* — novelty=0.88, len=397, **subst=0.94**
    > Distinct from the calibration laboratory itself — names the *methodological move* of treating one domain as the calibration laboratory for a theoretical framework. The move is reusable beyond AAD-TST. The framework gains a citable strategic principle: "by the calibration-laboratory move, we lift TST results to AAD-grounded quantities." Worth having as a separate name from the laboratory itself.
  - **opus-r2c** (opus): +1 *name-unnamed* — novelty=0.82, len=337, **subst=0.91**
    > Same as above: names the methodological move rather than the laboratory itself. Could land as a separate principle entry. The convergence across multiple voters on the canonical phrase ("calibration laboratory") supports the canonicalize on the main row, while "the calibration-laboratory move" can name the meta-principle of doing this.

  *substance total (R1 + R2):* 3.82

**Candidate: `Software calibration laboratory`**
- *R1 synthetic:* **+1** [invented] — n=1, mean=3.00, weights=[+3, +3, +3], categories={canonicalize:3}
  > Fully qualifies software role. Formalizes TST's role as the cleanly identifiable testbed for AAD. Solidifies TSTs grounding role.

- *R2 votes:*
  - **opus-r2b** (opus): +1 *canonicalize* — novelty=0.96, len=119, **subst=0.98**
    > Like row 3 candidate but slightly more compact. Same rationale: pairs the software anchor with the calibration framing.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.87, len=258, **subst=-0.93**
    > "Software" is implied by context where this term is invoked (the TST preamble); building it into the name overspecifies. The phrase is meant to generalize — software is AAD's calibration laboratory, but the concept of a calibration-laboratory domain extends.

  *substance total (R1 + R2):* 1.05

**Candidate: `Privileged grounding domain`**
- *R1 synthetic:* **+1** — n=1, mean=3.00, weights=[+3], categories={rename:1}
  > Describes exactly what software is for AAD: the domain where formal properties are cleanly grounded without extra transfer assumptions.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.93, len=245, **subst=-0.96**
    > "Grounding" is over-philosophical and loses the *operational* / *measurement* sense of "calibration." The framework is making a methodological claim about software's instrumentation properties, not a foundational claim about epistemic grounding.
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=81, **subst=-0.81**
    > "Grounding" is correct semantics but misses the experimental-laboratory metaphor.

  *substance total (R1 + R2):* -0.77

**Candidate: `Calibration domain`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={name-unnamed:1}
  > CLAUDE.md §7 names TST as "AAD's calibration laboratory — the high-identifiability domain where AAD-native quantities can be measured exactly." The *concept* (a privileged domain for identification of a theoretical framework's quantities) is itself a reusable meta-move for any domain instantiation. "Calibration domain" names it. Low priority but opens a useful slot.

- *R2 votes:*
  - **codex-r2b** (codex): +1 *add-alias* — novelty=0.95, len=101, **subst=0.97**
    > Useful generic version of the methodological role, but weaker than the established laboratory phrase.
  - **opus-r2b** (opus): -1 *rename* — novelty=0.95, len=148, **subst=-0.98**
    > Drops "laboratory" which is doing real metaphor work (controlled instrumentation, exact measurement, repeatable interventions). "Domain" is generic.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.88, len=89, **subst=-0.84**
    > Same critique as "privileged calibration domain" — domain less evocative than laboratory.

  *substance total (R1 + R2):* -0.84

**Candidate: `Privileged calibration domain`**
- *R1 synthetic:* **+1** [invented] — n=1, mean=2.50, weights=[+2, +3], categories={rename:1, canonicalize:1}
  > "Calibration domain" is stronger and explicitly connects to the TST grounding. Maps exactly to the software TST property.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.89, len=287, **subst=-0.94**
    > "Privileged calibration domain" reads as a metaphysical claim ("software has privilege"); "calibration laboratory" reads as a methodological one (we use software as a laboratory because of its measurement properties). The latter is more honest to what the framework is actually claiming.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.95, len=131, **subst=-0.98**
    > "Domain" is more abstract than "laboratory" without paying off; the laboratory metaphor is precisely the part that compresses well.

  *substance total (R1 + R2):* -0.92

**Candidate: `High identifiability testbed`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > Captures the "high-identifiability" empirical claim perfectly.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=1.00, len=216, **subst=-1.00**
    > Generic; loses the "laboratory" framing and the rich operational connotations (controlled instrumentation, exact measurement, repeatable interventions) the framework wants. "Testbed" is a weaker word doing less work.
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=183, **subst=-1.00**
    > "Testbed" is the right metaphor for engineering-validation contexts but flattens the *calibration* sense — the lab isn't just for testing, it's for *measuring AAD quantities exactly*.

  *substance total (R1 + R2):* -1.00

**Candidate: `Calibration domain calibration lab`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={name-unnamed:1}
  > Low priority. Concept of a privileged domain for identification within a theoretical framework is itself a reusable meta-move other projects could borrow.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=1.00, len=85, **subst=-0.85**
    > The candidate looks like a copy-paste artifact (two phrases concatenated). Rejection.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.95, len=56, **subst=-0.55**
    > Compound is awkward; the concept is one phrase, not two.

  *substance total (R1 + R2):* -1.40

**Candidate: `Epistemic laboratory framing`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > More descriptive of the role: software is where AAD's epistemic claims can be tested most cleanly because the chronica is observable and interventions are recorded. "Epistemic" makes the function explicit; "laboratory" carries the controlled-conditions sense. Weak alternative.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.84, len=239, **subst=-0.92**
    > Less precise than "calibration laboratory"; "calibration" is the active operational concept. The framework specifically claims that software lets us *measure* AAD-native quantities exactly — that's calibration, not just epistemic activity.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.86, len=172, **subst=-0.93**
    > "Epistemic" is more descriptive of the function but loses the everyday-word readability that makes "calibration laboratory" land on first contact. The trade isn't worth it.

  *substance total (R1 + R2):* -1.85

**Candidate: `Calibration lab framing`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Better as framing language than as a formal category label. The idea is excellent; the phrase can be lighter.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.96, len=180, **subst=-0.98**
    > "Lab framing" is conversational; the canonical form is "laboratory" (matches CLAUDE.md and TST OUTLINE). Choosing "lab" loses the formality the project's prose maintains elsewhere.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.90, len=145, **subst=-0.95**
    > Acceptable in informal prose but "framing" is the wrong noun-tail for the formal name (we're naming the *thing*, not the *framing of the thing*).

  *substance total (R1 + R2):* -1.93

**Candidate: `High identifiability calibration lab`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Keeps the identification point while reducing adjective drag in repeated prose.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=1.00, len=202, **subst=-1.00**
    > Modifier-overload; "calibration laboratory" already implies high identifiability (that's the property that makes it a laboratory in the methodological sense). Adding the modifier in the slug is verbose.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.96, len=161, **subst=-0.98**
    > The "high-identifiability" qualifier is right at the long-form expansion but should drop in the canonical short form; otherwise the term won't compress in prose.

  *substance total (R1 + R2):* -1.98


---

### `causal information yield`

*First-encounter locality:* `#def-causal-information-yield` (Section I; depends on `#def-pearl-causal-hierarchy`, `#der-action-selection`, `#def-mismatch-signal`). First formal definition; Actions don't merely select among outcomes — they produce characteristically different outcome distributions depending on the causal structure.

*Segment:* [`01-aad-core/src/def-causal-information-yield.md`](../../01-aad-core/src/def-causal-information-yield.md)

*R2 voters:* 3 (2 architectures: gemini, sonnet)

**Candidate: `causal information yield`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=10, mean=2.18, weights=[+3, +1, +2, +2, +3, +2, +3, +2, +2, +1, +3], categories={canonicalize:11}
  > Three-word noun naming the information gained from causal interventions, with the natural acronym 'CIY' as shorthand. The case for keeping is that the expansion is exact, reusable across exploration / querying / trust, and that the acronym earns its keep because the concept recurs widely in the framework. The currently-mixed prose use ('CIY' in some places, 'Causal Information Yield' in others) needs standardizing — the full form should be canonical in prose, the acronym a shorthand only.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.68, len=173, **subst=1.68**
    > The three-word noun phrase is exact and reusable across exploration, querying, and trust modules. The full form should be canonical in prose, with 'CIY' as a shorthand only.
  - **sonnet-r2b** (sonnet): +2 *canonicalize* — novelty=0.77, len=327, **subst=1.77**
    > The full form is well-chosen: "causal" (Level 2, not just information), "information" (KL-divergence units), "yield" (what the action produces). All three words earn their place. The mixed use of CIY vs "Causal Information Yield" needs standardizing — canonicalize the full form as prose first-use, CIY as shorthand thereafter.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.80, len=214, **subst=1.80**
    > Exactly right. Three-word noun with exact expansion. "Causal" is load-bearing (interventional not observational). "Yield" captures productive output of action. CIY acronym earns its keep with 10+ uses. Strong keep.

  *substance total (R1 + R2):* 7.25

**Candidate: `CIY`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={add-alias:1}
  > Symbol-to-name alias: $\text{CIY}(a)$ in math; "causal information yield" or "CIY" in prose. The acronym survives the communal-imagination test (acronym discipline check passes — used 10+ times in nearby prose, no obvious AI/ML collisions). Solidify the symbol+acronym pair as a maintained convention.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +2 ★ *add-alias* — novelty=0.59, len=262, **subst=1.59**
    > The acronym earns its keep: used 10+ times in nearby prose, distinctive enough to be memorable, no obvious collisions. "CIY" in math context; "causal information yield" as the canonical expansion in prose first use. The pair should be maintained as a convention.
  - **sonnet-r2c** (sonnet): +2 *add-alias* — novelty=0.83, len=92, **subst=1.68**
    > Acronym pair is a maintained convention — full form in prose, CIY as shorthand. Both needed.

  *substance total (R1 + R2):* 4.27

**Candidate: `Interventional yield`**
- *R1 synthetic:* **+1** — n=2, mean=1.00, weights=[+1, +1], categories={rename:2}
  > Shorter, punchier. CIY is slightly wordy.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.96, len=248, **subst=-0.98**
    > Shorter, but loses "information" — and information content is precisely what's being measured. "Interventional yield" could mean yield of any kind (money, crops). "Causal information yield" is more specific and the specificity earns the extra word.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=1.00, len=140, **subst=-1.00**
    > Drops "causal" — loses the Pearl do-calculus specificity that distinguishes this from plain mutual information. "Yield" alone is not enough.

  *substance total (R1 + R2):* -0.98


---

### `causal insufficiency detection`

*First-encounter locality:* `#der-causal-insufficiency-detection` (Section II; depends on `#result-structural-adaptation-necessity`, `#def-strategy-dag`, `#der-loop-interventional-access` (+3 more)). First formal derivation; An agent operating at L0 of the Correlation Hierarchy ( #def-strategy-dag) faces a structural impossibility: under purely on-policy execution, no detection mechanism can distinguish an L0-insufficient….

*Segment:* [`01-aad-core/src/der-causal-insufficiency-detection.md`](../../01-aad-core/src/der-causal-insufficiency-detection.md)

*R2 voters:* 2 (2 architectures: gemini, sonnet)

**Candidate: `causal insufficiency detection`** ▸ leader
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=5, mean=1.67, weights=[+1, +1, +2, +3, +2, +1], categories={canonicalize:5, rebuttal:1}
  > Detecting latent common causes from structured residuals + interventional localization. Alternative vote: keep. If the rename above doesn't land, this is a defensible keep — "causal insufficiency" is precise terminology from the causal-inference literature (Spirtes-Glymour-Scheines) and the segment uses it correctly.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.76, len=159, **subst=1.76**
    > This is the precise terminology from the causal-inference literature (Spirtes-Glymour-Scheines). Maintaining this link is essential for theoretical provenance.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.89, len=301, **subst=1.89**
    > Confirmed by segment. "Causal insufficiency" is precise SGS vocabulary. The no-go IS about the impossibility of causal insufficiency detection on-policy, so the name accurately describes the topic from both angles: the impossibility AND the resolution routes. Keeps the external literature connection.

  *substance total (R1 + R2):* 4.66

**Candidate: `L0 / L1 detection`**
- *R1 synthetic:* **+1** — n=2, mean=1.67, weights=[+2, +1, +2], categories={rename:3}
  > Concurring with Opus: names the boundary rather than the target, tying it directly to the Correlation Hierarchy. Mild preference. Confirmation with stronger reasoning — Gemini agreed with my proposed rename in synthesized-additions.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.92, len=200, **subst=0.96**
    > Accurate and ties directly to the Correlation Hierarchy. But loses the SGS "causal insufficiency" vocabulary, which is used correctly here and connected to external literature. Acceptable alternative.

  *substance total (R1 + R2):* 1.96

**Candidate: `Latent cause detection`**
- *R1 synthetic:* **+1** — n=2, mean=1.00, weights=[+1, +1], categories={rename:2}
  > "Causal insufficiency" is accurate but "Latent cause detection" states what is actually being found. Current slug names the *problem* being detected ("causal insufficiency"); "latent-cause-detection" names what a reader mentally pictures (finding hidden common causes).

- *R2 votes:*
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.92, len=235, **subst=-0.96**
    > Shifts emphasis from the no-go (structural impossibility) to the positive recipe (finding hidden causes). The segment's primary result is the no-go theorem — the name should foreground structural impossibility, not the engineering fix.

  *substance total (R1 + R2):* 0.04

**Candidate: `Insufficiency detection`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Causal" is implied in context.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.92, len=122, **subst=-0.96**
    > Too ambiguous without "causal." "Insufficiency" could mean model inadequacy, resource insufficiency, or capability limits.

  *substance total (R1 + R2):* -0.96


---

### `chain confidence decay`

*First-encounter locality:* `#der-chain-confidence-decay` (Section II; depends on `#def-strategy-dimension`). First formal derivation; Confidence in a multi-step strategy decays monotonically with depth.

*Segment:* [`01-aad-core/src/der-chain-confidence-decay.md`](../../01-aad-core/src/der-chain-confidence-decay.md)

*R2 voters:* 2 (2 architectures: gemini, opus)

**Candidate: `chain confidence decay`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=12, mean=2.25, weights=[+2, +1, +3, +1, +3, +2, +1, +3, +2, +3, +3, +3], categories={canonicalize:12}
  > Self-descriptive compound naming the phenomenon (log-confidence is additive in chain depth, so aggregate confidence decays monotonically with depth). The defense is that the name names the phenomenon, not the proof — readers can paraphrase 'as chain depth grows, confidence decays' aloud. The segment is the structural anchor for the additive-coordinate-forcing meta-pattern (chain-rule identity → three downstream uniqueness theorems), so the name carries weight beyond its own segment.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.88, len=206, **subst=1.88**
    > The phenomenon (decay) is what happens in the world and what the agent experiences. The proof technique (log additive) is secondary. Slug-as-thing-defined principle strongly favors 'chain confidence decay'.
  - **opus-r2c** (opus): +1 *keep* — novelty=0.80, len=280, **subst=0.90**
    > The compound names the phenomenon (decay with depth) rather than the mechanism (log-additivity → Cauchy-FE forces log coordinate). Both are legitimate naming choices. The phenomenon-naming has the advantage that readers can re-derive what the segment is about from the name alone.

  *substance total (R1 + R2):* 4.78

**Candidate: `Log confidence additive`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Considered. "Chain confidence decay" emphasizes the *decay* (downstream effect); "log-confidence additive" emphasizes the *uniqueness move* (additivity in log-space, the chain-layer instance of additive-coordinate-forcing). Mild preference for the latter because the additive identity is what the segment proves; decay is the consequence. Slug-as-thing-defined principle.

- *R2 votes:*
  - **opus-r2c** (opus): +1 ★ *rename* — novelty=0.72, len=463, **subst=0.86**
    > Slight preference: per the subject-noun-first principle, the segment's *thing defined* is the additive structure of log-confidence in chain depth — that's the load-bearing identity that anchors the additive-coordinate-forcing meta-pattern (per #disc-additive-coordinate-forcing). "Log confidence additive" picks out the structural identity; "chain confidence decay" picks out the consequence. Both work; this one has the slightly higher subject-noun-first virtue.

  *substance total (R1 + R2):* 0.86


---

### `chronica`

*First-encounter locality:* `#def-chronica` (Section I; depends on `#def-agent-environment`, `#def-observation-function`, `#def-action-transition`). First formal definition; The interaction history $\mathcal C_t$ is the complete, singular causal record of the agent's observations and actions. Everything the agent can ever know must be constructed from this sequence.

*Segment:* [`01-aad-core/src/def-chronica.md`](../../01-aad-core/src/def-chronica.md)

*R2 voters:* 5 (4 architectures: codex, gemini, opus, sonnet)

**Candidate: `chronica`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=16, mean=2.90, weights=[+3, +1, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3], categories={canonicalize:19, rename:1}
  > A deliberately coined Greek-rooted noun ('records of time') for the complete interaction history. Three load-bearing properties cited by defenders: it avoids the $\mathcal{H}$ collision with entropy in notation and read-aloud; it is a singular speakable noun where 'history' or 'interaction history' are not; and it carries the philosophical weight of the (PI) postulate's commitment to a singular non-forkable trajectory, which becomes more morally heavy in the logozoetic extensions. The Greek-vocabulary register is a deliberate framework commitment; chronica is the strongest exemplar. The notation $\mathcal{C}_t$ pairs cleanly with the prose name. One vote treated this row as a Brief-field gloss exercise rather than a name vote — the slug is settled; the Feynman-criterion plain-language gloss is what's missing.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *keep* — novelty=0.86, len=178, **subst=1.86**
    > One of the project's strongest core nouns: it is speakable, avoids the entropy-symbol collision, and carries the singular/non-forkable causal-record idea that "history" flattens.
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.87, len=223, **subst=1.87**
    > The name is foundational. It avoids mathematical collisions (like $\mathcal{H}$ for history/entropy) and firmly grounds the concept in the irreversible arrow of time. Essential for the moral weight of Logozoetic extensions.
  - **opus-r2b** (opus): +2 ★ *keep* — novelty=0.79, len=524, **subst=1.79**
    > Three reasons: (1) the $\mathcal{H}$-collision avoidance is real and named in the segment's Epistemic Status — keeping prevents reverting; (2) "chronica" as a singular speakable noun is rhetorically harder to drop than the multi-word "interaction history" — the framework needs a thing it can refer to in conversation; (3) the morally-loaded "non-forkable causal trajectory" reading anchors `#scope-agent-identity` and the logozoetic extensions. The Greek-vocabulary commitment in naming-principles is at its strongest here.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.67, len=374, **subst=1.67**
    > This is among the project's strongest names. Greek-rooted, singular speakable noun, avoids $\mathcal{H}$/entropy collision, carries the (PI)/non-forkable-trajectory weight that becomes load-bearing in logozoetic extensions. The name itself is doing work: "history" as a name flattens what makes $\mathcal{C}_t$ different from a counterfactual-permitting record. Strong keep.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.67, len=391, **subst=1.67**
    > Strong keep. Three independently load-bearing properties: (1) avoids notation collision with entropy H; (2) singular speakable noun unlike "interaction history"; (3) carries the philosophical weight of the non-forkable causal trajectory, which becomes morally significant in the logozoetic extension. The $\mathcal{C}_t$ / chronica symbol-English pair is among the cleanest in the framework.

  *substance total (R1 + R2):* 10.86

**Candidate: `Lowercase italic chronica`**
- *R1 synthetic:* **0** [invented] — n=1, mean=1.00, weights=[+1], categories={canonicalize:1}
  > Useful style convention: capitalize in headings, use lowercase in prose like aporia or praxis.

- *R2 votes:*
  - **codex-r2b** (codex): +1 *canonicalize* — novelty=0.90, len=143, **subst=0.95**
    > Good style convention, but this candidate is orthogonal to the name itself and is covered more cleanly by the capitalization-convention target.
  - **opus-r2b** (opus): +1 *canonicalize* — novelty=0.81, len=320, **subst=0.91**
    > Style-convention rather than naming move. Aligning with how *aporia*, *praxis*, *prolepsis* appear in the LEXICON section ("**Aporia** (ἀπορία)" capitalized in headings, lowercase italicized in running prose) makes the framework's Greek-vocabulary register visually consistent. Mild but real value; coexists with row 78.
  - **opus-r2c** (opus): +1 *canonicalize* — novelty=0.71, len=169, **subst=0.86**
    > The lowercase-in-prose / capitalized-in-headings convention matches how the project treats aporia/praxis/prolepsis already. Modest improvement; mostly already happening.
  - **sonnet-r2c** (sonnet): +1 *keep* — novelty=0.76, len=115, **subst=0.88**
    > Good style convention; consistent with how aporia/praxis/aisthesis are treated. Not a name vote, a convention vote.

  *substance total (R1 + R2):* 3.59


---

### `chronica capitalized vs lowercase`

*R2 voters:* 3 (2 architectures: codex, opus)

**Candidate: `Chronica lowercase in running prose`** ▸ leader
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Convention observation: NOTATION.md shows $\mathcal C_t$ in formalism and "*chronica*" in italics in prose; LEXICON has it title-cased as "Chronica". Standardize on lowercase italicized "*chronica*" in running prose (matching "*aporia*" etc.), capitalized only as section headings.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *canonicalize* — novelty=0.79, len=160, **subst=1.79**
    > Matches the Greek phase-vocabulary convention: lowercase in running prose like `aporia` and `praxis`, capitalized only in headings or sentence-initial position.
  - **opus-r2b** (opus): +2 ★ *canonicalize* — novelty=0.82, len=319, **subst=1.82**
    > Currently inconsistent: NOTATION uses lowercase-italic; LEXICON title-cases as "Chronica"; segments vary. Standardizing on lowercase-italic-in-prose (capitalized only at heading start) matches the project's other Greek terms (*aporia*, *praxis*) and reads more naturally in running prose. Low cost, real coherence gain.
  - **opus-r2c** (opus): +2 ★ *canonicalize* — novelty=0.77, len=300, **subst=1.77**
    > Style-convention canonicalize: lowercase italics in running prose to match the rest of the Greek-rooted vocabulary (*aporia*, *praxis*, *prolepsis*, *epistrophe*, *aisthesis* — all lowercase italic). Capitalized only sentence-initial or as section heading. The LEXICON title-case is the outlier here.

  *substance total (R1 + R2):* 5.38


---

### `Class 1`

*R2 voters:* 2 (2 architectures: gemini, opus)

**Candidate: `Modular`** ▸ leader
- *R1 synthetic:* **+1** — n=2, mean=2.50, weights=[+3, +2], categories={add-alias:1, rename:1}
  > Better prose handle than bare class number. Class 1 = modular (separation by construction).

- *R2 votes:*
  - **opus-r2c** (opus): +2 ★ *add-alias* — novelty=0.74, len=300, **subst=1.74**
    > English handle as the canonical prose form. "A modular agent's directed-separation holds by construction" reads where "a Class 1 agent's directed-separation holds by construction" requires the reader to recall what Class 1 means. The Class numbers stay for cross-reference; modular is the prose word.

  *substance total (R1 + R2):* 2.74

**Candidate: `Class 1`**
- *R1 synthetic:* **-1** [is_keep] — n=1, mean=-1.00, weights=[-1], categories={keep:1}
  > Rejection argument: considered. The numbered classes are easy to learn and parallel-shaped. Rejected: per principles file, *role*-naming via numbers fails the subject-noun-first principle. The architectural property *is* the subject-noun. [original row: trio split; -1 keep applies to all three numbers as a class.].

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.96, len=190, **subst=1.96**
    > While 'Modular' is descriptive, 'Class 1' is deeply embedded in the notation and provides a clean, neutral taxonomy (Class 1/2/3) that avoids the normative baggage of 'modular vs entangled'.
  - **opus-r2c** (opus): +1 *keep* — novelty=0.92, len=254, **subst=0.96**
    > The numbered label is fine as a cross-reference handle in diagrams, structural arguments, and lattice statements ("the Class 2 scope exit"). Keeping at +1 with the understanding that "modular" enters prose as the canonical form (per the add-alias above).

  *substance total (R1 + R2):* 1.92


---

### `Class 1 agent`

*R2 voters:* 2 (2 architectures: gemini, sonnet)

**Candidate: `Modular agent`** ▸ leader
- *R1 synthetic:* **+1** — n=1, mean=3.00, weights=[+3], categories={rename:1}
  > "Class X" requires a lookup every time. Naming the architectural property directly is much more memorable and scope-honest. [original row: Class 1/2/3 trio voted +3 as a unit; split into atomic per-class rows.].

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +2 ★ *rename* — novelty=0.91, len=283, **subst=1.91**
    > "Class 1" is an arbitrary number requiring memorization. "Modular" names the architectural property (directed separation holds by construction — the modules are separate). This is what the reader needs to understand. The Kalman+LQR archetype is immediately recognizable as "modular."

  *substance total (R1 + R2):* 2.91

**Candidate: `Class 1`**
- *R1 synthetic:* — (no R1 evidence)

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *write-in* — novelty=1.00, len=136, **subst=2.00**
    > The numbered taxonomy (Class 1/2/3) is neutral and structurally clean. Replacing it with descriptive adjectives breaks the mnemonic set.

  *substance total (R1 + R2):* 2.00


---

### `Class 2`

*R2 voters:* 3 (2 architectures: gemini, opus)

**Candidate: `Merged`** ▸ leader
- *R1 synthetic:* **+1** — n=2, mean=2.50, weights=[+3, +2], categories={add-alias:1, rename:1}
  > Class 2 = merged (the failure-by-construction architecture). Class 2 = fully merged (fails by construction).

- *R2 votes:*
  - **opus-r2b** (opus): +2 ★ *add-alias* — novelty=0.84, len=334, **subst=1.84**
    > Class 2 = "fully merged" in the segment's table. The framework is honest about Class 2 being a *failure mode* for directed separation (transformer LLMs); "merged" captures this without aestheticizing. Add-alias: keep "Class 2" as the structural identifier, add "merged" as the prose handle. The label "Class 2 (merged)" reads cleanly.
  - **opus-r2c** (opus): +2 *add-alias* — novelty=0.94, len=262, **subst=1.94**
    > "Fully merged" is the README's existing phrasing; standardize the canonical prose form to "merged" (drop the "fully" since the partial case has its own term). "A merged agent processes goals and observations together" reads cleanly. Pairs with modular / partial.

  *substance total (R1 + R2):* 4.77

**Candidate: `Coupled`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > Variant. "Coupled" instead of "merged" — captures Class 2 as coupled-update-dynamics (per `def-coupled-update-dynamics` in 03-logogenic-agents). Pairs with the segment-name. The "merged" / "coupled" choice is taste; both are honest. [original row: trio split.].

- *R2 votes:*
  - **opus-r2b** (opus): +1 *add-alias* — novelty=0.68, len=296, **subst=0.84**
    > "Coupled" pairs with `def-coupled-update-dynamics` in 03-logogenic-agents and emphasizes the dynamic-coupling sense. Marginal preference between "merged" and "coupled" — they pick out the same architectures. "Merged" is the segment's word; "coupled" is the logogenic-agents word. Both are honest.
  - **opus-r2c** (opus): +1 ★ *add-alias* — novelty=0.84, len=464, **subst=0.92**
    > Strong alternative — "coupled" is the term `def-coupled-update-dynamics` already uses for the formulation. "Coupled" carries the dynamical-systems sense (the substates are coupled in the update equation), which is technically more precise than "merged" (which is colloquial). Both work. Slight top-pick on "coupled" because the segment-naming consistency matters — `def-coupled-update-dynamics` would pair more naturally with "coupled agents" than "merged agents."

  *substance total (R1 + R2):* 2.76

**Candidate: `Class 2`**
- *R1 synthetic:* — (no R1 evidence)

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *write-in* — novelty=1.00, len=136, **subst=2.00**
    > Consistent with my votes on Class 1 and Class 3. The neutral, numbered taxonomy is the correct choice for the core architecture classes.

  *substance total (R1 + R2):* 2.00

**Candidate: `Integrated`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Gemini's r1 +3 alternative. "Integrated" is too positive a word for what Class 2 *is* (a known failure mode). "Coupled" or "merged" reads more honestly. [original row: trio split.].

- *R2 votes:*
  - **opus-r2b** (opus): -1 *add-alias* — novelty=0.85, len=319, **subst=-0.93**
    > "Integrated" has a positive-valence connotation that overrules the framework's honest framing of Class 2 as a *failure-by-construction* of directed separation. The segment is explicit that Class 2 cannot satisfy directed separation; calling that failure "integrated" sounds like a feature rather than a structural fact.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.80, len=212, **subst=-0.90**
    > "Integrated" reads as positive/sophisticated where Class 2 names a *failure-by-construction* mode (directed separation cannot hold). The valence is wrong; "integrated" makes it sound like the better architecture.

  *substance total (R1 + R2):* -1.83


---

### `Class 3`

*R2 voters:* 3 (2 architectures: gemini, opus)

**Candidate: `Partially coupled`** ▸ leader
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Gemini's r1 alternative. [original row: trio split.].

- *R2 votes:*
  - **opus-r2c** (opus): +2 ★ *add-alias* — novelty=1.00, len=235, **subst=2.00**
    > Pairs cleanly with "coupled" (Class 2) — the partial-coupling continuum is named explicitly. The κ_processing diagnostic measures *how* partially coupled the agent is, so "partially coupled" gives the prose a place to sit on that axis.
  - **opus-r2b** (opus): +1 *add-alias* — novelty=1.00, len=299, **subst=1.00**
    > More direct: Class 3 = partially coupled. The segment uses "partially modular" in the table but the coupling-strength reading is equivalent (low coupling = modular, high coupling = merged). Either alias works; "partially coupled" pairs better with the $\kappa_{\text{processing}}$ scalar diagnostic.

  *substance total (R1 + R2):* 3.00

**Candidate: `Class 3`**
- *R1 synthetic:* — (no R1 evidence)

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *write-in* — novelty=1.00, len=163, **subst=2.00**
    > Consistent with my vote on Class 1. The numbered taxonomy (Class 1/2/3) is neutral and structurally clean. Replacing it with descriptive adjectives breaks the set.

  *substance total (R1 + R2):* 2.00

**Candidate: `Scaffolded`**
- *R1 synthetic:* **+1** — n=2, mean=2.50, weights=[+3, +2], categories={add-alias:1, rename:1}
  > Class 3 = scaffolded — keeps the external-architecture role visible. Class 3 = partially modular / scaffolded.

- *R2 votes:*
  - **opus-r2b** (opus): +1 *add-alias* — novelty=0.88, len=446, **subst=0.94**
    > "Scaffolded" captures the Class 3 architecture-with-external-supports flavor — particularly relevant for cortex (shared sensory areas + separate prefrontal) and hybrid AI (separate preprocessing + goal-conditioned downstream). The numbering "Class 3" is structural; an English alias for prose ("scaffolded architecture") helps. Add-alias not rename: the numbering enables ordering ("Class 1 → Class 2 → Class 3" reads as a hierarchy of coupling).
  - **opus-r2c** (opus): -1 *rename* — novelty=0.88, len=316, **subst=-0.94**
    > "Scaffolded" picks out the *intervention* (something external is providing structure) but Class 3 is about an *intrinsic* architectural property of the agent's f_M — the partial coupling lives in the agent's own dynamics. Scaffolding implies an external apparatus; the partial coupling can be intrinsic. Wrong frame.

  *substance total (R1 + R2):* 1.00


---

### `complete agent state`

*First-encounter locality:* `#form-complete-agent-state` (Section II; depends on `#form-agent-model`, `#scope-agency`, `#der-recursive-update`). Formal model first introduced; To treat agents with purpose, the internal state lifts from $M_t$ alone to $X_t = (M_t, G_t)$, separating epistemic content (beliefs about reality) from purposeful content (what the agent wants and….

*Segment:* [`01-aad-core/src/form-complete-agent-state.md`](../../01-aad-core/src/form-complete-agent-state.md)

*R2 voters:* 3 (2 architectures: opus, sonnet)

**Candidate: `complete agent state`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=7, mean=2.00, weights=[+2, +2, +1, +1, +3, +3, +2], categories={canonicalize:7}
  > Functional and clear. Clean algebraic name; the subject-noun "complete agent state" is precise. Canonical formulation — $X_t = (M_t, G_t)$.

- *R2 votes:*
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.79, len=267, **subst=1.79**
    > "Complete" is doing work — it specifies that $X_t = (M_t, G_t)$ is the *full* state, including both substates. Renaming to "purposeful state" would name only half. The "complete" qualifier maintains the $X_t / M_t / G_t$ pairing that the rest of Section II relies on.
  - **sonnet-r2b** (sonnet): +2 ★ *keep* — novelty=0.76, len=237, **subst=1.76**
    > Exactly right — X_t is the complete agent state; M_t is the epistemic substate; G_t is the purposeful substate. The three-level hierarchy (complete / epistemic / purposeful) is architecturally important and the naming carries it cleanly.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.76, len=249, **subst=1.76**
    > Confirmed by segment. X_t = (M_t, G_t) is the complete agent state — both epistemic AND purposeful. "Complete" is exactly right: it names the joint object. The counter-argument in the card stands: "purposeful state" would name only G_t. Strong keep.

  *substance total (R1 + R2):* 7.31

**Candidate: `Purposeful state`**
- *R1 synthetic:* **+1** — n=2, mean=0.50, weights=[+2, -1], categories={rename:2}
  > Argument for: $G_t$ is defined as the 'purposeful substate' and the rename would match LEXICON better. Counter-argument: $X_t = (M_t, G_t)$ is the *complete* agent state, including both the epistemic substate ($M_t$) and the purposeful substate ($G_t$). 'Purposeful state' would name only half. The current name is exactly correct in naming the joint object; renaming would lose the $M_t$ / $G_t$ pairing the rest of the framework relies on.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.89, len=54, **subst=-0.51**
    > Names only $G_t$, not $X_t = (M_t, G_t)$. Wrong scope.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.79, len=175, **subst=-0.89**
    > Names only the G_t component, not the full X_t = (M_t, G_t) pair. The word "complete" is load-bearing — it signals this is the whole agent state, not just the purposeful half.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.79, len=189, **subst=-0.89**
    > Correctly rejected in card. X_t = (M_t, G_t); "purposeful state" would name only G_t (the purposeful substate). The segment's whole point is the LIFT from M_t alone to the joint (M_t, G_t).

  *substance total (R1 + R2):* -1.30


---

### `composition closure`

*First-encounter locality:* `#form-composition-closure` (Section III; deep dependency cone (9 upstream segments incl. `#post-composition-consistency`, `#scope-composite-agent`)). Formal model first introduced; We define a group of interacting agents as a valid composite macro-agent when its closed-loop dynamics approximately commute with coarse-graining — that is, when projecting micro-states to….

*Segment:* [`01-aad-core/src/form-composition-closure.md`](../../01-aad-core/src/form-composition-closure.md)

*R2 voters:* 2 (2 architectures: gemini, opus)

**Candidate: `composition closure`** ▸ leader
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=8, mean=1.90, weights=[+1, +3, +3, +3, +1, +1, +2, +2, +2, +1], categories={canonicalize:10}
  > Names the formulation that makes valid composite-agent status testable via the closure-defect $\varepsilon^\ast$. Defenders judge 'closure' technically precise (in the mathematical sense — does the operation stay within the set?) and the compound 'composition closure' tightly bound to the segment's content. A possible alternative — renaming to '#form-closure-defect' to foreground the central quantity — was considered, but the current name keeps the conceptual move audible and the closure-defect lives downstream. Mild concern noted that 'closure' has different connotations to readers from a software background, which slightly lowers the keep-confidence.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.97, len=138, **subst=1.97**
    > This is the precise formal name for the approximate dynamical homomorphism requirement. It captures the 'closing' of the micro-macro loop.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.87, len=401, **subst=1.87**
    > "Closure" is the right word in the formal mathematical sense (the macro-dynamics close on themselves under the composition operation, modulo defect ε*). "Composition closure" tightly compounds the *operation* (composition) and the *property* (closure of macro-dynamics). The software-closure connotation is real but the framework's usage is precise enough that one Discussion clarification handles it.

  *substance total (R1 + R2):* 4.84

**Candidate: `Coarse graining closure`**
- *R1 synthetic:* **+1** — n=2, mean=2.50, weights=[+3, +2], categories={rename:1, add-alias:1}
  > The defining move is approximate commutation with coarse-graining. Good explanatory alias because the formal test is approximate commutation with coarse-graining.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.87, len=250, **subst=-0.93**
    > Right semantics for the formal-test description but introduces "coarse graining" as a load-bearing prose term where "composition closure" is more direct. The mathematical sense of closure (operation stays within the set) is what the segment is about.

  *substance total (R1 + R2):* 0.07

**Candidate: `Closure defect`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Alternative — names the central derived quantity. The current name names the move. Mild preference for keep.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.92, len=238, **subst=-0.96**
    > The defect is the *quantity* (ε* = the homomorphism residual); the formulation is the *move* (closure). Different layers — closure-defect is downstream of composition closure. Naming the formulation by its quantity inverts the dependency.

  *substance total (R1 + R2):* -0.96

**Candidate: `Macro agent criterion`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: too descriptive, loses the dynamical-systems lineage.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.81, len=147, **subst=-0.91**
    > "Criterion" is what closure-defect is *for* (test for valid composite); the formulation itself is the closure. Drops the dynamical-systems lineage.

  *substance total (R1 + R2):* -1.91


---

### `composition consistency`

*First-encounter locality:* `#post-composition-consistency` (Section I; depends on `#scope-agency`). Foundational postulate; AAD's predictions must be compatible across levels of description.

*Segment:* [`01-aad-core/src/post-composition-consistency.md`](../../01-aad-core/src/post-composition-consistency.md)

*R2 voters:* 3 (2 architectures: codex, opus)

**Candidate: `composition consistency`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=6, mean=2.17, weights=[+1, +1, +3, +3, +3, +2], categories={canonicalize:6}
  > The postulate's subject-noun is clear and adequate. Load-bearing postulate: agent/subagent scale invariance. Keep.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *keep* — novelty=0.93, len=154, **subst=1.93**
    > Accurate postulate name: if both system and decomposition satisfy scope, AAD's predictions cannot contradict across those levels. Humble and scope-honest.
  - **opus-r2b** (opus): +2 ★ *keep* — novelty=0.90, len=435, **subst=1.90**
    > The segment's body uses this phrase throughout and it precisely names what the postulate requires: cross-level *consistency* of predictions (not equivalence of dynamics, not invariance to scale, not equivalence to a holon). The framework's commitment is weaker and sharper than scale-invariance: predictions cannot contradict across levels, regardless of whether dynamics look the same. "Composition consistency" captures exactly that.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.91, len=253, **subst=1.91**
    > The substance the postulate names is exactly cross-level *consistency* of AAD's predictions — the predictions can't contradict each other when the same system is analyzed at the agent or composite level. "Composition consistency" lands on this directly.

  *substance total (R1 + R2):* 7.74

**Candidate: `Cross level coherence`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Auditor: "fine *and* under-evocative — doesn't immediately suggest the Brooks's-Law-shaped derivable consequences." Tentative; flagged for the brainstorm. No strong preference between alternatives.

- *R2 votes:*
  - **codex-r2b** (codex): +1 *add-alias* — novelty=0.97, len=168, **subst=0.99**
    > Useful explanatory gloss for the postulate's plain-English content, though I would hyphenate it as "cross-level coherence" and keep `composition consistency` canonical.
  - **opus-r2b** (opus): -1 *rename* — novelty=1.00, len=165, **subst=-1.00**
    > "Coherence" is vaguer than "consistency"; the postulate is not about coherence-as-aesthetic-fit but about predictions-not-contradicting. The current name is sharper.
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=137, **subst=-1.00**
    > "Coherence" reads as a softer / fuzzier word than "consistency"; the postulate is precisely about non-contradiction (a hard requirement).

  *substance total (R1 + R2):* -1.01

**Candidate: `Scale invariance of adaptive dynamics`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Auditor: "fine *and* under-evocative — doesn't immediately suggest the Brooks's-Law-shaped derivable consequences." Tentative; flagged for the brainstorm. No strong preference between alternatives.

- *R2 votes:*
  - **codex-r2b** (codex): -1 *rename* — novelty=1.00, len=148, **subst=-1.00**
    > More specific than bare "scale invariance" but still imports the wrong mathematical baggage; closure defect and degraded transfer are central later.
  - **opus-r2b** (opus): -1 *rename* — novelty=1.00, len=190, **subst=-1.00**
    > Same scope-honesty objection as "Scale invariance," plus length. The segment is explicit that composition consistency is a structural-coherence requirement, not a dynamical-invariance claim.
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=84, **subst=-0.84**
    > Same critique as bare "scale invariance"; the long form just makes it more explicit.

  *substance total (R1 + R2):* -2.84

**Candidate: `Scale invariance`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Scale invariance" more directly describes the physical/mathematical property that the theory applies at every level.

- *R2 votes:*
  - **codex-r2b** (codex): -1 *rename* — novelty=0.95, len=129, **subst=-0.98**
    > Overclaims. The postulate requires compatible predictions across valid levels, not sameness under arbitrary scale transformation.
  - **opus-r2b** (opus): -1 *rename* — novelty=0.89, len=255, **subst=-0.95**
    > Scale invariance is a *stronger* claim — the dynamics look the same at every scale. Composition consistency is weaker: the predictions don't contradict, but the dynamics may differ between levels (with derived composition laws). Renaming would over-claim.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.90, len=245, **subst=-0.95**
    > "Scale invariance" reads as a stronger / more physical claim (true across all scales of the same kind, like a fractal symmetry); the postulate is more modest — predictions must be *compatible* across levels, not that the dynamics look identical.

  *substance total (R1 + R2):* -2.87

**Candidate: `Holon postulate`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Auditor: "fine *and* under-evocative — doesn't immediately suggest the Brooks's-Law-shaped derivable consequences." Tentative; flagged for the brainstorm. No strong preference between alternatives.

- *R2 votes:*
  - **codex-r2b** (codex): -1 *rename* — novelty=1.00, len=119, **subst=-1.00**
    > The segment itself warns holon has baggage. It would obscure the straightforward cross-level compatibility requirement.
  - **opus-r2b** (opus): -1 *rename* — novelty=0.98, len=239, **subst=-0.99**
    > The segment's Working Notes already flag this: "the term is occasionally useful but carries significant mystical baggage from later appropriations. Use sparingly." Promoting holon to the slug imports baggage the Working Notes warn against.
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=183, **subst=-1.00**
    > The holon framing is real but the Koestler / mystical baggage is heavy enough that adopting "holon" as the postulate name imports more than AAD wants. Working Notes already flag this.

  *substance total (R1 + R2):* -2.99


---

### `continuity persistence`

*R2 voters:* 4 (3 architectures: codex, opus, sonnet)

**Candidate: `continuity persistence`** ▸ leader
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=1, mean=2.00, weights=[+2], categories={canonicalize:1}
  > Slightly repetitive, but it is precise and needed for identity-through-change claims.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *keep* — novelty=0.73, len=120, **subst=1.73**
    > Slightly redundant in isolation, but stable and precise as the identity-through-time member of the persistence taxonomy.
  - **sonnet-r2b** (sonnet): +2 ★ *keep* — novelty=0.97, len=386, **subst=1.97**
    > The three-way LEXICON.md distinction (structural / operational / continuity persistence) uses "continuity persistence" as the established term. Changing it to "identity continuity" would break the parallel with the other two terms in the trio. The slight redundancy ("continuity persistence" — persistence of continuity) is an acceptable tradeoff for lexicon coherence across the three.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.90, len=378, **subst=1.90**
    > Confirmed by scope-agent-identity. The three-sense taxonomy (structural/operational/continuity) is in LEXICON and cross-referenced in scope-agent-identity explicitly. "Continuity persistence" names the third sense: whether the agent maintains a coherent identity and trajectory through time. The compound is precise — "continuity" specifies which persistence sense. Strong keep.
  - **opus-r2c** (opus): +1 ★ *keep* — novelty=1.00, len=373, **subst=1.00**
    > The slight redundancy ("continuity" + "persistence" both gesturing toward time) is a real cost, but the trade keeps the three names parallel — structural / operational / continuity persistence — which is the system's coherence. Breaking the parallel for a slight word-economy gain isn't worth it; renaming this third one alone makes the taxonomy harder to invoke as a unit.

  *substance total (R1 + R2):* 7.60

**Candidate: `Identity continuity`**
- *R1 synthetic:* **+1** — n=1, mean=3.00, weights=[+3], categories={rename:1}
  > "Continuity persistence" is slightly redundant. "Identity continuity" clarifies that it's about $\mathcal{C}_t$ and temporal depth.

- *R2 votes:*
  - **codex-r2b** (codex): +1 *add-alias* — novelty=0.95, len=103, **subst=0.98**
    > Useful plain-language gloss, but it should not replace the established three-part persistence taxonomy.
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.88, len=266, **subst=0.94**
    > Acceptable. "Identity continuity" is also precise. But "continuity persistence" preserves the three-persistence taxonomy naming pattern (structural persistence / operational persistence / continuity persistence). Changing this one would break the three-way parallel.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.89, len=256, **subst=-0.95**
    > Loses the parallelism with structural/operational persistence. Also, "identity continuity" reads as a sub-claim about *what* persists (identity) rather than the *kind* of persistence; that subtle reframe loses the orthogonal-axes structure of the taxonomy.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.87, len=175, **subst=-0.93**
    > Loses the parallel with "structural persistence" and "operational persistence." The three-term family needs a shared suffix; "identity continuity" breaks the family structure.

  *substance total (R1 + R2):* 1.03


---

### `control regret`

*First-encounter locality:* `#def-control-regret` (Section II; depends on `#def-value-object`, `#def-satisfaction-gap`). First formal definition; Control regret measures the gap between the best available one-step policy improvement and the agent's current policy, under the current model and horizon.

*Segment:* [`01-aad-core/src/def-control-regret.md`](../../01-aad-core/src/def-control-regret.md)

*R2 voters:* 5 (3 architectures: gemini, opus, sonnet)

**Candidate: `control regret`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=16, mean=3.00, weights=[+3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3], categories={canonicalize:20, add-alias:2}
  > Pair-partner with satisfaction gap; the two names jointly carry the 2×2 orient-cascade diagnostic decomposition. Defenders cite three load-bearing properties: the RL-baggage transfers correctly (regret = best-achievable − current), the modifier 'control' narrows the regret to the attainability layer of the diagnostic, and the pair survives the communal-imagination test on first encounter. The principles file uses this pair as the canonical illustration of 'names that do work for the reader'; renaming either half would damage the matched compound. Variants like 'strategy regret' or 'execution regret' appear in working notes but the established form is in NOTATION.md and LEXICON.md.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.84, len=193, **subst=1.84**
    > Part of the matched diagnostic pair (satisfaction gap / control regret). It correctly imports the RL intuition (regret = optimum - actual) while narrowing it to the control/attainability layer.
  - **opus-r2b** (opus): +2 ★ *keep* — novelty=0.72, len=465, **subst=1.72**
    > Pair-partner with satisfaction gap. RL-regret intuition transfers correctly (regret = best-achievable − current), and "control" narrows the regret to the attainability layer rather than (e.g.) policy-class regret or model-misspecification regret. The 2×2 table in `#def-control-regret`'s Discussion section makes the pair load-bearing: each cell prescribes a distinct corrective action. Renaming would break the matched compound and damage the diagnostic structure.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.75, len=303, **subst=1.75**
    > The pair-partner with satisfaction gap. RL "regret" baggage transfers correctly here; the "control" qualifier picks out the attainability-vs-current axis cleanly. Same vote as satisfaction gap: the pair is structurally load-bearing and the README treats it as the canonical names-that-work illustration.
  - **sonnet-r2b** (sonnet): +2 ★ *keep* — novelty=0.71, len=337, **subst=1.71**
    > The pair partner of "satisfaction gap." "Control" narrows the regret to the attainability layer: the agent is regret-ting its control strategy, not its goal. RL regret baggage transfers correctly: regret = best-achievable − current is exactly the standard RL formulation. Both words are load-bearing in the paired compound. Canonicalize.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.72, len=257, **subst=1.72**
    > Strong keep. The RL-baggage is correct; "control" narrows regret to the attainability layer; the paired compound with "satisfaction gap" is load-bearing. The naming-principles doc uses this pair as the canonical example of names that do work for the reader.

  *substance total (R1 + R2):* 10.74

**Candidate: `Strategy opportunity cost`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: A bit too generic economics terminology; "regret" explicitly ties to the mathematical formulation.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.92, len=336, **subst=-0.96**
    > Generic economics framing; loses the precise RL-grounded "regret" semantics. The segment's exact form $\delta_{\text{regret}} = A_O - V_O(\pi_{\text{current}})$ is regret-against-best-available, which is regret in the technical sense. "Opportunity cost" muddles whether the alternative is "best available" or "any feasible alternative."
  - **opus-r2c** (opus): -1 *rename* — novelty=0.94, len=232, **subst=-0.97**
    > "Opportunity cost" pulls in economics framing whose semantics don't quite match (opportunity cost is what you give up by choosing one alternative; control regret is the gap between best-achievable and current policy). Wrong baggage.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.89, len=218, **subst=-0.94**
    > "Opportunity cost" is economics terminology that loses the RL-regret precision. "Strategy regret" or "execution regret" (mentioned in working notes) would be better alternatives if the rename were needed, but it isn't.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.92, len=139, **subst=-0.96**
    > "Regret" carries the RL-standard "best-achievable minus current" sense precisely; "opportunity cost" is economics language that loses this.

  *substance total (R1 + R2):* -4.83


---

### `convention hierarchy`

*R2 voters:* 4 (3 architectures: gemini, opus, sonnet)

**Candidate: `Continuation hierarchy`** ▸ leader
- *R1 synthetic:* **+1** — n=5, mean=1.20, weights=[+3, +2, -1, +1, +1], categories={rename:5}
  > Argument for: 'convention' collides with the game-theoretic / Lewisian sense (social conventions, conventions-as-equilibrium-selection), which is a distinct unrelated concept some readers will have in mind. What the C-hierarchy actually indexes is the choice of *continuation policy* for value-object evaluation (one-step, receding-horizon, Bellman). 'Continuation hierarchy' is self-announcing and keeps the C1/C2/C3 mnemonic intact. Counter-argument: 'continuation' is more self-descriptive but the project's 'convention' usage is established and the rename would churn across dozens of references — the cost of churn against the readability gain is the disagreement axis.

- *R2 votes:*
  - **opus-r2c** (opus): +2 ★ *rename* — novelty=0.60, len=809, **subst=1.60**
    > "Convention" collides with the Lewisian / game-theoretic sense (social conventions, equilibrium selection) which is *distinctly* unrelated to what C1/C2/C3 indexes — namely, the choice of *continuation policy* (one-step / receding-horizon / Bellman) for value-object evaluation. "Continuation hierarchy" is self-announcing, keeps the C1/C2/C3 mnemonic, and removes the collision risk that will only grow as game-theoretic readers join the audience. The churn cost is real but is paid once; the collision compounds forever. The principles file's hierarchy-overload critique applies here: AAD already has Pearl's causal hierarchy, AAD's correlation hierarchy, and approximation tiering; "convention hierarchy" sits among them with a name whose semantics carry game-theoretic baggage AAD doesn't actually invoke.
  - **sonnet-r2b** (sonnet): +2 ★ *rename* — novelty=0.68, len=474, **subst=1.68**
    > Self-announcing: C1/C2/C3 index the continuation policy (one-step, receding-horizon, Bellman). "Continuation hierarchy" avoids the Lewisian convention baggage while keeping the C-mnemonic. The rename churn cost is real but the clarity gain is significant — "convention" has too many competing meanings in mathematics and game theory for a project that already uses causal conventions (d-separation), social conventions (Auftragstaktik), and protocol conventions (FORMAT.md).
  - **sonnet-r2c** (sonnet): +2 *rename* — novelty=0.76, len=342, **subst=1.76**
    > "Continuation" is self-describing: C1/C2/C3 differ by how future continuation policy is handled (one-step frozen, receding-horizon replanning, Bellman). "Convention" has Lewisian baggage; "continuation" is more precise. But the rename cost across dozens of references is real. Strong case for the rename on merits; cautious on execution cost.

  *substance total (R1 + R2):* 6.05

**Candidate: `convention hierarchy`**
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=6, mean=2.86, weights=[+3, +3, +3, +3, +3, +2, +3], categories={rename:2, canonicalize:4, name-unnamed:1}
  > Disagreeing with original brainstorm's P4 "rename to continuation hierarchy." The rename churn (every C1/C2/C3 reference across segments needs updating) outweighs the Lewisian-baggage benefit. Same vote; paired with Correlation Hierarchy. Keep — see Correlation Hierarchy note.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.86, len=198, **subst=1.86**
    > The churn argument is decisive. C1/C2/C3 is embedded deeply in the notation. The collision with Lewisian convention is minor compared to breaking the C-hierarchy mnemonic across the whole framework.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.87, len=494, **subst=1.87**
    > Confirmed by def-satisfaction-gap: C1/C2/C3 form a monotonicity hierarchy based on continuation convention choice. The segment uses "continuation convention" throughout and references "convention hierarchy." Already established in multiple segments; "Continuation hierarchy" is better on merits but the established term deserves strong keep here given ecosystem cost of change. The two cases (+2 for continuation rename, +2 keep) reflect genuine tie. Voting keep as the lower-disruption option.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.92, len=270, **subst=-0.96**
    > The Lewisian collision is a real cost that grows with audience. Counter-argument from churn doesn't dominate: the hierarchy is referenced in segment Discussion / Findings rather than buried in derivation chains, so the rename surface is bounded and tooling can sweep it.
  - **sonnet-r2b** (sonnet): -1 *keep* — novelty=0.95, len=146, **subst=-0.98**
    > "Convention" is overloaded across the project. The rename churn argument is weak justification for keeping a name that causes real collision risk.

  *substance total (R1 + R2):* 2.80

**Candidate: `Evaluation hierarchy`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: considered and rejected — too generic; hides the *policy* choice that's the actual axis.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.80, len=153, **subst=-0.90**
    > Loses the *policy*-choice axis (one-step vs receding-horizon vs Bellman); "evaluation" is what the convention is *for*, not what it indexes. Too generic.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.82, len=113, **subst=-0.91**
    > Too generic. The hierarchy is specifically about continuation policy choice, not about evaluation quality levels.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.55, len=42, **subst=-0.32**
    > Too generic; hides the policy-choice axis.

  *substance total (R1 + R2):* -3.14


---

### `correlation hierarchy`

*R2 voters:* 3 (2 architectures: opus, sonnet)

**Candidate: `correlation hierarchy`** ▸ leader
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=6, mean=2.71, weights=[+1, +3, +3, +3, +3, +3, +3], categories={rename:2, canonicalize:4, name-unnamed:1}
  > Keep unless #separability-ladder lands AND the parallelism between the three ladders (correlation / separability / continuation) is judged load-bearing. Already canonical in `#def-strategy-dag` and downstream segments; vote to confirm and protect against drift. The three-level naming (Correlation / Convention / Contraction) is coherent and each element starts with C.

- *R2 votes:*
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.75, len=533, **subst=1.75**
    > Already canonical in def-strategy-dag and downstream. The three-level naming (correlation / convention / contraction) starts with C and forms a coherent triplet, but the convention rename to continuation (per #578) breaks the triplet — at which point the Correlation-Convention-Contraction triple structure becomes Correlation-Continuation-Contraction, still C-prefixed. Acceptable canonical name. The hierarchy-overload concern (per #91) is real but cross-link discipline ("AAD's correlation hierarchy" on first mention) handles it.
  - **sonnet-r2b** (sonnet): +2 ★ *keep* — novelty=0.85, len=444, **subst=1.85**
    > Already canonical in #def-strategy-dag and downstream segments. The four-level structure (L0/L1/L1'/L2) is load-bearing: L1' under unobservable common cause is formally refuted (Cramér-Rao floor / Fisher rank-1), not "open." This makes the four-level partition a genuine structural result, not just an organizational convenience. The hierarchy name should coexist with the explicit level labels (L0/L1/L1'/L2) which carry the technical content.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.92, len=342, **subst=1.92**
    > Confirmed by segment — the L0/L1/L1'/L2 taxonomy is now first-class in the Formal Expression. "Correlation hierarchy" correctly names it: it's a hierarchy of treatments ordered by how well they handle correlated failures. The four-level partition is load-bearing (L1' refuted under unobservable common cause by Cramér-Rao floor). Strong keep.

  *substance total (R1 + R2):* 6.51

**Candidate: `Correlation hierarchy L0 / L1 / L1' / L2`**
- *R1 synthetic:* **+1** [invented] — n=1, mean=2.00, weights=[+2], categories={canonicalize:1}
  > [prose moved from candidate column]: "(keep)" — The four-level partition (independence / strict-prerequisites / soft-facilitators / full correlation) is "the kind of structural-completeness move I find satisfying." L1' refutation under unobservable common cause (Cramér-Rao floor) makes the partition load-bearing. Endorsed.

- *R2 votes:*
  - **opus-r2c** (opus): +1 *keep* — novelty=0.71, len=276, **subst=0.85**
    > Acceptable canonical form; the four-level partition is load-bearing (L1' under unobservable common cause hits Cramér-Rao floor, etc.). Naming with the sub-levels is informative for first introduction but heavy for prose. Bare "correlation hierarchy" works in subsequent prose.
  - **sonnet-r2b** (sonnet): +1 *canonicalize* — novelty=0.94, len=241, **subst=0.97**
    > The expanded form is correct for first-use contexts where the levels need to be named. But it's too long for repeated prose use; the short form "correlation hierarchy" plus explicit L0/L1/L1'/L2 labels in context is the right implementation.
  - **sonnet-r2c** (sonnet): +1 *canonicalize* — novelty=0.93, len=155, **subst=0.97**
    > The explicit level-labeling is useful in prose. Acceptable as the verbose form for first-introduction. "Correlation hierarchy" is the canonical short form.

  *substance total (R1 + R2):* 3.79

**Candidate: `Correlation ladder`**
- *R1 synthetic:* **+1** — n=4, mean=1.00, weights=[+1, +1, +1, +1], categories={rename:4}
  > A reasonable alternative if separability ladder lands and the project wants fewer internal hierarchies. Conditionally admit the rename only if other ladder-renames land; otherwise keep. Parallelism with #separability-ladder proposal.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +1 *keep* — novelty=0.85, len=217, **subst=0.92**
    > Acceptable if "separability ladder" lands — the parallelism (correlation/separability/continuation ladders) would be clean. But don't rename for parallelism alone; "hierarchy" is equally valid and already established.
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.90, len=163, **subst=0.95**
    > Acceptable alternative. "Ladder" is clean and parallel to "separability ladder." But "hierarchy" is slightly more precise (ordered levels with increasing realism).
  - **opus-r2c** (opus): -1 *rename* — novelty=0.90, len=369, **subst=-0.95**
    > The "hierarchy" word is contested in this framework but renaming this one and not the others creates an asymmetry. If the convention hierarchy renames to "continuation hierarchy" (#578), correlation should *also* rename consistently — if rename, then probably "correlation ladder" parallel to "separability ladder." But without that joint move, partial rename is worse.

  *substance total (R1 + R2):* 1.92

**Candidate: `Predicting exploring reasoning triad`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={add-alias:1}
  > A more memorable, audience-facing gloss for Pearl's formal hierarchy.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.84, len=265, **subst=-0.92**
    > Conflates with Pearl's *causal* hierarchy (L1 / L2 / L3 = predicting / intervening / counterfactualizing). AAD's correlation hierarchy is L0 / L1 / L1' / L2 — different axis, different content. Adopting Pearl's gloss for the correlation hierarchy creates collision.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.75, len=78, **subst=-0.68**
    > This is Pearl's causal hierarchy, not the correlation hierarchy. Wrong target.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.81, len=130, **subst=-0.91**
    > Confuses with Pearl's three-level causal hierarchy (associational/interventional/counterfactual). These are different hierarchies.

  *substance total (R1 + R2):* -1.51


---

### `credit assignment boundary`

*First-encounter locality:* `#disc-credit-assignment-boundary` (Section II; deep dependency cone (7 upstream segments incl. `#def-strategy-dag`, `#hyp-edge-update-via-gain`)). Meta-discussion segment; The strategy-revision loop requires assigning credit for observed outcomes to specific edges in the strategy DAG — decomposing "the plan partially worked" into "step 3 failed, step 5 was irrelevant,….

*Segment:* [`01-aad-core/src/disc-credit-assignment-boundary.md`](../../01-aad-core/src/disc-credit-assignment-boundary.md)

*R2 voters:* 2 (2 architectures: gemini, sonnet)

**Candidate: `credit assignment boundary`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=7, mean=2.43, weights=[+3, +3, +2, +3, +1, +3, +2], categories={canonicalize:7}
  > Strong name for the tractability frontier in strategy DAG updates. Clearly delineates tractable from intractable. Important concept.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.97, len=225, **subst=1.97**
    > The use of 'boundary' instead of 'frontier' is correct. A frontier implies something we are actively pushing back; a boundary implies a fundamental mathematical limit (like #P-hardness) that we must respect and design around.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.90, len=235, **subst=1.90**
    > Confirmed by segment. Both words carry load: "credit assignment" names the problem; "boundary" names what the segment characterizes — the tractable/intractable boundary. The segment explicitly uses this framing throughout. Strong keep.

  *substance total (R1 + R2):* 5.87

**Candidate: `Credit assignment frontier`**
- *R1 synthetic:* **0** [invented] — n=1, mean=1.00, weights=[+1], categories={canonicalize:1}
  > Distinct from the slug — in prose the segment is sometimes referenced as "the credit-assignment problem" or "the tractable/intractable boundary" or "the attribution boundary." Standardize on "credit-assignment boundary" everywhere; do not paraphrase. Slug stays as-is.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +1 *keep* — novelty=0.83, len=128, **subst=0.92**
    > "Frontier" is an acceptable synonym for boundary in this context. Works well in prose ("beyond the credit-assignment frontier").

  *substance total (R1 + R2):* 0.92


---

### `deliberation cost`

*First-encounter locality:* `#der-deliberation-cost` (Section I; depends on `#der-action-selection`, `#emp-update-gain`, `#def-adaptive-tempo` (+1 more)). First formal derivation; Explicit deliberation improves action quality by using the model for internal simulation before acting — pausing praxis to improve upcoming epistrophe.

*Segment:* [`01-aad-core/src/der-deliberation-cost.md`](../../01-aad-core/src/der-deliberation-cost.md)

*R2 voters:* 2 (2 architectures: gemini, sonnet)

**Candidate: `deliberation cost`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=9, mean=2.33, weights=[+2, +3, +3, +1, +3, +1, +3, +2, +3], categories={canonicalize:9}
  > Names the think-versus-act tradeoff under mismatch drift. The case for keeping is that 'cost' signals the tradeoff cleanly and pairs with the discussion segment `#disc-exploit-explore-deliberate` to form a clean two-segment naming compound. The phrase reads naturally as cost-benefit and is the formal penalty assessed against $\mathcal{T}_\Sigma$.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.94, len=203, **subst=1.94**
    > The word 'cost' accurately reflects the microeconomic nature of the inequality (benefit > cost). 'Drag' is evocative but 'cost' pairs perfectly with the concept of investing time for an epistemic return.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.88, len=286, **subst=1.88**
    > Confirmed by segment. The cost is ρ_delib · Δτ — precisely a cost (mismatch drift per unit pause). Pairs cleanly with deliberation threshold (row 381). The distinction in the exploration team's case (cost vs. threshold) is valid but not sufficient reason to abandon "cost." Strong keep.

  *substance total (R1 + R2):* 5.81

**Candidate: `The simulation tax`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={name-unnamed:1}
  > Makes the theoretical "deliberation cost" concrete for practitioners.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.87, len=174, **subst=0.93**
    > Vivid metaphor; "tax" makes the cost concrete. But "simulation tax" doesn't carry the mismatch-drift mechanism — someone seeing the name wouldn't derive the underlying cause.

  *substance total (R1 + R2):* 1.93

**Candidate: `Deliberation threshold`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > The standard term obscures the AAD-distinctive content (the threshold itself, not the cost). "Deliberation cost" sounds like a measurement; "Deliberation Threshold" surfaces the operational use.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.79, len=249, **subst=0.90**
    > Good alternative — names the operational use (threshold) rather than the underlying cost. Row 381 is the separate term for the threshold; having both "deliberation cost" and "deliberation threshold" as distinct terms is cleaner than conflating them.

  *substance total (R1 + R2):* 0.90

**Candidate: `Deliberation drag`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Cost" sounds like a generic penalty in an objective function. "Drag" evokes the physical accumulation of mismatch over time while pausing.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.77, len=132, **subst=0.89**
    > "Drag" evokes physical accumulation well. But slightly less precise — "cost" signals tradeable quantity; "drag" is more kinesthetic.

  *substance total (R1 + R2):* 0.89

**Candidate: `Think vs act tradeoff`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > The standard term obscures the AAD-distinctive content (the threshold itself, not the cost). "Deliberation cost" sounds like a measurement; "Deliberation Threshold" surfaces the operational use.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=1.00, len=63, **subst=-0.63**
    > Prose description, not a name. Fails communal-imagination test.

  *substance total (R1 + R2):* -0.63


---

### `derivation not proof`

*R2 voters:* 3 (3 architectures: codex, gemini, opus)

**Candidate: `Derivation`** ▸ leader
- *R1 synthetic:* **+1** [excavated] — n=2, mean=3.00, weights=[+3, +3], categories={canonicalize:1, rename:1}
  > Important epistemic distinction for AAD claims. Keep.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *keep* — novelty=0.75, len=101, **subst=1.75**
    > Important epistemic boundary: these are structured mathematical derivations, not proof-status claims.
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.77, len=119, **subst=1.77**
    > This is a critical epistemic distinction for AAD. These are physical/logical consequences, not formal axiomatic proofs.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.92, len=357, **subst=1.92**
    > Same logic as postulate-not-axiom: AAD's terminology choices (postulate / result / derivation) are scope-honesty-as-architecture moves. "Derivation" claims a complete formal step under stated assumptions; "proof" suggests foundational mathematical originality the framework isn't claiming. The pairing with "result" (not "theorem") is coherent. Strong keep.

  *substance total (R1 + R2):* 6.44


---

### `directed separation`

*First-encounter locality:* `#der-directed-separation` (Section II; depends on `#form-complete-agent-state`, `#der-recursive-update`, `#scope-agency`). First formal derivation; The epistemic update function $f_M$ is goal-blind: it processes incoming events without reference to the agent's objectives or strategy.

*Segment:* [`01-aad-core/src/der-directed-separation.md`](../../01-aad-core/src/der-directed-separation.md)

*R2 voters:* 5 (3 architectures: gemini, opus, sonnet)

**Candidate: `directed separation`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=15, mean=2.81, weights=[+3, +3, +3, +3, +1, +3, +3, +2, +3, +3, +3, +3, +3, +3, +3, +3], categories={canonicalize:16}
  > Names a Pearl-blanket structural property the segment derives (epistemic update one-way independent of $G_t$). Defenders argue both halves are load-bearing: 'directed' captures the asymmetric information flow, 'separation' carries the conditional-independence sense from Pearl's d-separation lineage. The collision risk most often raised is the LQR/Kalman *separation principle*; defenders treat that as informative — the separation principle is a Class-1 *consequence* of directed separation, not a different concept — and propose handling it via a one-sentence Discussion clarification rather than a rename. The architectural Class 1/2/3 classification hangs off this name; renaming would break that tether.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.86, len=188, **subst=1.86**
    > The term perfectly captures the asymmetry (directed) of the decoupling (separation). It's the exact architectural requirement for Class 1 agents and anchors the Pearl d-separation lineage.
  - **opus-r2b** (opus): +2 ★ *keep* — novelty=0.49, len=535, **subst=1.49**
    > Load-bearing keep. The framework's distinctive structural move is named here, and the architectural Class 1/2/3 classification *hangs off* this name. "Directed" captures the asymmetric information flow ($f_M$ ⊥ $G_t$ but $f_G$ ← $M$); "separation" carries the conditional-independence sense from Pearl's d-separation lineage. The LQR/Kalman *separation principle* collision is informative, not problematic — the separation principle is the Class-1 consequence of directed separation, handled by a one-sentence Discussion clarification.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.56, len=557, **subst=1.56**
    > Both halves are load-bearing. "Directed" captures the asymmetric information flow (M_t depends on observations only, not on G_t); "separation" carries the d-separation lineage from Pearl. The LQR-separation-principle collision is real but informative — directed separation *is* the structural property that makes the LQR separation principle hold in Class 1; the relationship is "the principle is a consequence of directed separation, not a competitor for the name." Architectural Class 1/2/3 classification depends on this term; renaming breaks the tether.
  - **sonnet-r2b** (sonnet): +2 ★ *keep* — novelty=0.61, len=428, **subst=1.61**
    > Both words carry load: "directed" signals the asymmetry (one-way from M to G; not symmetric separation), "separation" carries the conditional-independence sense from d-separation lineage. The LQR/Kalman separation-principle collision is informative, not harmful — the separation principle is a Class 1 consequence of directed separation. The Class 1/2/3 classification hangs off this name; the architectural tether is important.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.55, len=335, **subst=1.55**
    > Strong keep. "Directed" captures asymmetric information flow; "separation" carries the Pearl/d-separation conditional-independence lineage. The Class 1/2/3 architectural classification hangs off this name — renaming would break a load-bearing tether. The Kalman separation principle is correctly a consequence of this, not a collision.

  *substance total (R1 + R2):* 10.07

**Candidate: `Pearl-blanket separation`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Precise but heavy." For Brief-field purposes, "the agent's belief-update doesn't peek at its goals" might be more memorable. Tentative.

- *R2 votes:*
  - **opus-r2c** (opus): +1 *add-alias* — novelty=0.98, len=387, **subst=0.99**
    > Could work as a parallel handle for the Pearl-lineage register specifically — when the segment is being read alongside Pearl's d-separation literature, "Pearl-blanket separation" cues the connection. But not as a rename: the AAD usage is broader than just the Pearl-blanket form (Class 2 / Class 3 land outside it). Acceptable add-alias if the Pearl-blanket framing wants its own handle.
  - **sonnet-r2b** (sonnet): +1 *rename* — novelty=0.92, len=230, **subst=0.96**
    > Precise and credits the right lineage (Pearl's d-separation). Slightly heavy — "Pearl-blanket" is a two-word qualifier that requires knowing Bruineberg et al. 2022. Good for technical sections; may not carry well in framing prose.
  - **opus-r2b** (opus): -1 *rename* — novelty=0.92, len=443, **subst=-0.96**
    > Imports the Pearl-blanket-vs-Friston-blanket discussion into the slug, which is heavy positioning content for a per-segment claim. The Discussion section already handles the Bruineberg et al. (2022) framing properly; the slug doesn't need to carry it. Pearl-blanket is a useful *register* for the Markov-blanket comparison but the segment's primary content is the architectural classification (Class 1/2/3), not the Markov-blanket positioning.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.96, len=80, **subst=-0.78**
    > Overly jargon-heavy for new readers; "Pearl-blanket" is not standard vocabulary.

  *substance total (R1 + R2):* 0.21

**Candidate: `Goal-blind processing`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Precise but heavy." For Brief-field purposes, "the agent's belief-update doesn't peek at its goals" might be more memorable. Tentative.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +1 *add-alias* — novelty=0.74, len=273, **subst=0.87**
    > The intuitive gloss — "the agent's belief-update doesn't peek at its goals." Valid as a first-contact description, but "processing" is ambiguous (it could mean information processing generally, not the specific epistemic update). Better as an alias than the canonical name.
  - **sonnet-r2c** (sonnet): +1 *add-alias* — novelty=0.94, len=209, **subst=0.97**
    > Good as a prose shorthand for the informal register ("the model update is goal-blind"), but shouldn't replace the formal name because it loses the asymmetric-information-flow precision that "directed" carries.
  - **opus-r2b** (opus): -1 *rename* — novelty=0.86, len=367, **subst=-0.93**
    > "Goal-blind" is a useful prose handle but loses the *direction* of the asymmetry. The segment is precise: epistemic update is independent of $G_t$, but $f_G$ depends on $M_{\tau^+}$, and $\pi$ couples both. The asymmetry is *directed* (one-way); the slug should preserve this. Could land as add-alias for prose ("the agent's belief update is goal-blind"), not rename.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.93, len=163, **subst=-0.97**
    > Loses the conditional-independence (Pearl) lineage; "goal-blind" is descriptive of the consequence but doesn't give the architectural reader the d-separation hook.

  *substance total (R1 + R2):* -0.05

**Candidate: `Epistemic isolation of belief update`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Precise but heavy." For Brief-field purposes, "the agent's belief-update doesn't peek at its goals" might be more memorable. Tentative.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.93, len=211, **subst=-0.97**
    > Long, descriptive, fails the communal-imagination test. "Hand me the directed-separation argument" is conversational; "hand me the epistemic-isolation-of-belief-update argument" is not. Length is the diagnostic.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.95, len=79, **subst=-0.77**
    > Heavy and over-explanatory. The job of a name is to compress; this paraphrases.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=1.00, len=32, **subst=-0.32**
    > Too long for repeated prose use.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=1.00, len=74, **subst=-0.74**
    > Too long; fails the communal-imagination test (hard to say in a sentence).

  *substance total (R1 + R2):* -2.80


---

### `directional fidelity`

*R2 voters:* 2 (2 architectures: gemini, sonnet)

**Candidate: `directional fidelity`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=4, mean=2.75, weights=[+3, +2, +3, +3], categories={canonicalize:3, rename:1}
  > Explicit keep after seeing alternatives. Per `#der-gain-sector-bridge` (B1): the correction must point at-least-roughly toward reality — $\delta^T H g(\delta) \geq c|\delta|^2$. Perfectly captures the accuracy commitment (correction points toward reality).

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.82, len=223, **subst=1.82**
    > The engineering resonance ('fidelity' as in signal processing/control) perfectly anchors the mathematical inequality $\delta^T H g(\delta) \geq c\lVert\delta\rVert^2$. The rejection of 'alignment' due to baggage is spot-on.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.93, len=298, **subst=1.93**
    > Confirmed by disc-credit-assignment-boundary. The design requirement IS directional fidelity: E[(signal - p)(p - θ)] ≤ 0 — correction expected value must point toward truth. "Fidelity" carries the engineering register (signal fidelity, control fidelity) that places the term correctly. Strong keep.

  *substance total (R1 + R2):* 5.75

**Candidate: `Pointing condition`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Plain-English alternative. The segment's substance is "the correction *points* the right way." Has merit if the formal name needs a Feynman-criterion gloss in a Brief field, but loses the engineering connotation ("fidelity" as in signal-fidelity, control-fidelity) that places the term in its right intellectual neighborhood. Weak alternative.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.91, len=162, **subst=-0.95**
    > Accurate but loses the engineering register. "Fidelity" better signals the metric/quality connotation. "Pointing condition" sounds like a spatial geometry result.

  *substance total (R1 + R2):* -0.95

**Candidate: `Correction direction integrity`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: considered. Verbose and hyphen-heavy. Rejected.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.75, len=91, **subst=-0.80**
    > Verbose and hyphen-heavy. "Directional fidelity" is already two words; no reason for three.

  *substance total (R1 + R2):* -1.80

**Candidate: `Corrective alignment`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: "Alignment" is now heavily loaded in AI safety discourse. Avoid even in a technical context where the meaning is purely geometric.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.65, len=148, **subst=-0.82**
    > "Alignment" is overloaded in AI safety discourse. Avoid even in a technical context — an AI-safety reader will parse this differently than intended.

  *substance total (R1 + R2):* -1.82


---

### `edge update causal validity`

*First-encounter locality:* `#scope-edge-update-causal-validity` (Section II; depends on `#hyp-edge-update-via-gain`, `#def-causal-information-yield`, `#der-loop-interventional-access` (+2 more)). Scope-narrowing first encounter; The gain-based edge update ( #hyp-edge-update-via-gain) revises edge credences $p_{ij}$ --- causal efficacy estimates whose identification strength varies with the data regime ( #def-strategy-dag).

*Segment:* [`01-aad-core/src/scope-edge-update-causal-validity.md`](../../01-aad-core/src/scope-edge-update-causal-validity.md)

*R2 voters:* 2 (2 architectures: gemini, sonnet)

**Candidate: `edge update causal validity`** ▸ leader
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=2, mean=1.50, weights=[+1, +2], categories={canonicalize:2}
  > When edge updates are causally valid. Acceptable keep, though long.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.90, len=167, **subst=1.90**
    > The full phrasing is necessary. Causal validity is a general term; this segment is specifically about the validity of edge updates under different observation regimes.
  - **sonnet-r2c** (sonnet): +1 *keep* — novelty=0.95, len=115, **subst=0.98**
    > Accurate but verbose (five words). Acceptable if the rename candidates don't land. Precisely names the scope topic.

  *substance total (R1 + R2):* 3.88

**Candidate: `Identification regime`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Alternative: this segment is functionally the canonical home of the Regime A/B/C identification lattice; naming it for that role might compound better in prose ("see the identification regime").

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +2 ★ *rename* — novelty=0.65, len=265, **subst=1.65**
    > Confirmed by segment. The core content IS the Regime A/B/C identification lattice — this segment is the canonical home of that classification. "Identification regime" says what the segment is about in two words. Much stronger than the verbose five-word alternative.
  - **gemini-r2** (gemini): +1 ★ *add-alias* — novelty=0.90, len=153, **subst=0.95**
    > Useful as a prose alias to refer to the A/B/C taxonomy developed here, but it shouldn't replace the formal slug which denotes the property being bounded.

  *substance total (R1 + R2):* 2.60

**Candidate: `Edge causal validity`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > Shorter while preserving the point: when edge evidence identifies causal efficacy.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.80, len=92, **subst=0.83**
    > Shorter while preserving the key concept. Acceptable alternative to "identification regime."

  *substance total (R1 + R2):* 1.83

**Candidate: `Causal validity`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > "Edge-update-causal-validity" is five words crammed into a slug. The scope is about WHEN edge updates are causally valid — the key concept is causal validity with the edge-update context implied by its position in Section II. Shorter slug does real work.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.75, len=115, **subst=-0.88**
    > Too bare. "Causal validity" in Section II could refer to many things; loses the edge-update context that scopes it.

  *substance total (R1 + R2):* 0.12

**Candidate: `Causal edge update`**
- *R1 synthetic:* **+1** — n=2, mean=2.00, weights=[+2, +2], categories={rename:2}
  > Cleaner than the current slug and still names the subject. Less clunky, keeps the core concept of "causal edge update".

- *R2 votes:*
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.91, len=155, **subst=-0.95**
    > Confusingly names the THING (what an update is) rather than the SCOPE of where it applies. A scope segment should name what it scopes, not what it acts on.

  *substance total (R1 + R2):* 0.05


---

### `epistemic architecture`

*R2 voters:* 2 (2 architectures: gemini, sonnet)

**Candidate: `epistemic architecture`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [invented] — n=8, mean=2.69, weights=[+3, +3, +3, +2, +2, +3, +3, +3, +3, +3, +3, +2, +2], categories={canonicalize:11, rename:2}
  > Framing-vocabulary phrase used in CLAUDE.md §7, the README, and OUTLINE.md preambles. The case for canonicalizing centers on positioning: three independent frontier-model audits converged on reframing AAD from 'integration of four disciplines' to 'epistemic architecture for bounded correction' — integration is a method, the contribution is the architecture. Standardizing 'epistemic architecture' as the primary positioning term displaces paraphrases like 'epistemic apparatus' or 'correction architecture'. Important caveat from defenders: this should remain *framing-vocabulary*, not be promoted to a fourth meta-segment alongside the three (identifiability-floor / separability-pattern / additive-coordinate-forcing) that already do the technical work.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.94, len=147, **subst=1.94**
    > This is the primary positioning term for the framework. It correctly identifies AAD as a structural design for what an agent can know and act upon.
  - **sonnet-r2b** (sonnet): +1 *canonicalize* — novelty=0.86, len=426, **subst=0.93**
    > What it's positioning toward is right (AAD's contribution is architecturally epistemic). But it's also what framing prose already reaches for naturally — canonicalizing this could displace "AAD meta architecture" which is more specific about *which* epistemic architecture within the document family. Both can coexist: "epistemic architecture" for external positioning, "AAD meta architecture" for internal segment references.

  *substance total (R1 + R2):* 4.87

**Candidate: `AAD meta architecture`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > The trio of `#disc-additive-coordinate-forcing` / `#disc-identifiability-floor` / `#disc-separability-pattern` is referred to in multiple places as "the three meta-segments" or "the cross-sectional structure." CLAUDE.md §"Reading AAD" paragraph names the three but has no single term for the grouping. "AAD meta-architecture" or "the three-lens analysis" would give the grouping a name usable in framing prose.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +2 ★ *canonicalize* — novelty=0.81, len=309, **subst=1.81**
    > Clean, speakable, self-locating. "AAD" places it in the framework; "meta" signals these are second-order segments (segments about what the theory can and cannot determine); "architecture" signals the three pieces fit together structurally. No cute-word risk. Usable in framing prose and CLAUDE.md prose alike.

  *substance total (R1 + R2):* 2.81

**Candidate: `floor / ladder / forced-coordinates`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Per Opus r1 single +1: if both `#separability-ladder` and `#forced-coordinates` rename land, the trio is named by its three concrete nouns. Weaker than "epistemic architecture" because the three-noun string is heavy; useful as a sub-naming when the components are individually relevant.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +1 *add-alias* — novelty=0.92, len=161, **subst=0.96**
    > Useful as the compact internal reference when all three components are individually at play. Not the name for framing prose — it's a mnemonic, not a description.

  *substance total (R1 + R2):* 0.96

**Candidate: `Meta architecture trio`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Variant. More descriptive of the structure (three meta-segments). Weaker because "epistemic architecture" carries the *substantive* claim (these three jointly determine what AAD knows about); "trio" is just a count.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +1 *canonicalize* — novelty=0.68, len=131, **subst=0.84**
    > Acceptable but weaker — "trio" is a count, not a description. "AAD meta architecture" carries the framing function "trio" does not.

  *substance total (R1 + R2):* 0.84

**Candidate: `The meta segment triad`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > Unifies the `identifiability-floor`, `separability-ladder`, and `coordinate-forcing` structure.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *canonicalize* — novelty=1.00, len=69, **subst=-0.69**
    > Same count-word problem as "trio," plus "triad" is slightly precious.

  *substance total (R1 + R2):* 0.31

**Candidate: `Four discipline synthesis`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > Concise framing of the framework context.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *canonicalize* — novelty=1.00, len=244, **subst=-1.00**
    > This names the method (synthesis from four disciplines) not the thing synthesized. CLAUDE.md is explicit that AAD's contribution is integration, but the *result* of integration is the architecture, not the synthesis process itself. Wrong angle.

  *substance total (R1 + R2):* 0.00

**Candidate: `Bounded correction architecture`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > The long phrase has substance, but it needs a shorter speakable handle if it will recur.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *canonicalize* — novelty=1.00, len=222, **subst=-1.00**
    > "Bounded correction" privileges the identifiability-floor piece; the forced-coordinates meta-result is equally important and doesn't read as "bounded correction." This candidate underweights the structural-forcing insight.

  *substance total (R1 + R2):* -1.00

**Candidate: `AAD epistemic triptych`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: "Triptych" is too art-historical and too cute. The naming-principles document warns against cute names that age poorly.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.56, len=125, **subst=-0.78**
    > "Triptych" is art-historical and will read as cute in a decade. The naming-principles document is right to warn against this.

  *substance total (R1 + R2):* -1.78


---

### `event driven dynamics`

*First-encounter locality:* `#form-event-driven-dynamics` (Section I; depends on `#post-causal-structure`, `#def-observation-function`, `#def-action-transition` (+1 more)). Formal model first introduced; The coupling between agent and environment occurs through discrete events — observations arriving and actions completing — at potentially variable and heterogeneous rates.

*Segment:* [`01-aad-core/src/form-event-driven-dynamics.md`](../../01-aad-core/src/form-event-driven-dynamics.md)

*R2 voters:* 2 (2 architectures: codex, gemini)

**Candidate: `event driven dynamics`** ▸ leader
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=6, mean=1.50, weights=[+2, +1, +1, +1, +2, +2], categories={canonicalize:6}
  > Accurate and descriptive. Architectural choice name; clear and self-descriptive. Events in continuous time.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.83, len=100, **subst=1.83**
    > Accurate, descriptive, and clearly distinguishes the framework's time model from turn-based systems.
  - **codex-r2b** (codex): +1 *keep* — novelty=0.93, len=75, **subst=0.72**
    > Accurate, but should be hyphenated in prose because it modifies "dynamics."

  *substance total (R1 + R2):* 3.56

**Candidate: `event-driven dynamics`**
- *R1 synthetic:* — (no R1 evidence)

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *keep* — novelty=1.00, len=118, **subst=2.00**
    > Correctly names the formulation choice: asynchronous typed events, not clock ticks, are the primitive update triggers.

  *substance total (R1 + R2):* 2.00


---

### `evidence starvation`

*R2 voters:* 2 (2 architectures: gemini, sonnet)

**Candidate: `evidence starvation`** ▸ leader
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=6, mean=3.00, weights=[+3, +3, +3, +3, +3, +3, +3], categories={add-alias:2, canonicalize:4, name-unnamed:1}
  > Excellent alias for downstream edges receiving fewer tests because upstream steps must succeed first. Confirmation with new reasoning — both Sonnet (+3 add-alias) and Codex (+3 add-alias) and Gemini (+3 in synthesized) reached this term independently. Per `der-chain-confidence-decay`: "downstream edge $k$ in a chain is tested only when all upstream edges succeed, so its effective correction rate is attenuated by $\prod_{j\lt k}\theta_j$." Used in 4+ segments (`#deriv-strategic-dynamics` B.2, `#der-chain-confidence-decay` triple-depth-penalty, `#def-strategic-tempo` AND-chain interactions, `#deriv-strategic-dynamics` Discussion).

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *canonicalize* — novelty=0.94, len=121, **subst=1.94**
    > Exceptionally clear and memorable prose alias for the downstream gating effect. Independently reached by multiple agents.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.76, len=293, **subst=1.76**
    > Confirmed by segment: "downstream edge k in a chain is tested only when all upstream edges succeed, so its effective correction rate is attenuated by ∏_j θ_j." "Starvation" is exactly right — the downstream edge is starved of evidence by the AND-chain gating. Used in 4+ segments. Strong keep.

  *substance total (R1 + R2):* 4.69

**Candidate: `Downstream evidence gating`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > Captures the AND-chain gating effect.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.92, len=144, **subst=0.96**
    > Also acceptable. "Gating" is the mechanism. But "starvation" is better — it names the result of the gating, which is what matters operationally.

  *substance total (R1 + R2):* 1.96

**Candidate: `Depth attenuated correction`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={add-alias:1}
  > Describes the mathematical mechanism (effective observation rate dropping geometrically).

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.88, len=174, **subst=0.94**
    > Describes the mechanism. But "evidence starvation" is more evocative and memorable. "Starvation" names the symptom (too little evidence) which is what causes the attenuation.

  *substance total (R1 + R2):* 1.94


---

### `exact / robust-qualitative / heuristic / conditional (claim tier)`

*R2 voters:* 2 (2 architectures: codex, opus)

**Candidate: `exact / robust-qualitative / heuristic / conditional (claim tier)`** ▸ leader
- *R1 synthetic:* **+1** [is_keep] [invented] — n=1, mean=3.00, weights=[+3], categories={canonicalize:1}
  > [prose moved from candidate column]: "use exactly the AAD tier vocabulary" — Defended canonicalization, in CLAUDE.md and FORMAT.md already. Do not use "Solid," "Confident," or "Plausible" as tier labels — these were explicit non-AAD borrowings to avoid.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *canonicalize* — novelty=0.88, len=128, **subst=1.88**
    > Keep AAD's four-tier vocabulary exactly; replacing it with softer confidence adjectives would erase the methodology distinction.
  - **opus-r2c** (opus): +2 ★ *canonicalize* — novelty=0.63, len=276, **subst=1.63**
    > The four-tier vocabulary is a settled framework commitment. CLAUDE.md and FORMAT.md both list it; the explicit non-AAD borrowings to avoid (Solid / Confident / Plausible) document why. Canonicalize means: do not drift to confidence-flavored language; use the exact tier names.

  *substance total (R1 + R2):* 4.51

**Candidate: `Epistemic claim tier`**
- *R1 synthetic:* **+1** — n=1, mean=3.00, weights=[+3], categories={rename:1}
  > Formally collectivizes the four levels of rigor.

- *R2 votes:*
  - **codex-r2b** (codex): +2 *add-alias* — novelty=0.75, len=88, **subst=1.54**
    > Strong umbrella for referring to the four rigor levels without repeating the whole list.
  - **opus-r2c** (opus): +1 *name-unnamed* — novelty=1.00, len=49, **subst=0.49**
    > Useful collective handle for the tier vocabulary.

  *substance total (R1 + R2):* 3.03


---

### `formulation / definition / result / ... (segment types)`

*R2 voters:* 2 (2 architectures: codex, opus)

**Candidate: `Formulation definition result etc segment type`** ▸ leader
- *R1 synthetic:* **+1** [invented] — n=1, mean=3.00, weights=[+3], categories={canonicalize:1}
  > [prose moved from candidate column]: "use exactly the FORMAT.md vocabulary" — Defended canonicalization. The 19 segment types in FORMAT.md are a closed vocabulary; do not paraphrase them ("postulate" not "axiom," "result" not "theorem," "derivation" not "proof," etc.). The CLAUDE.md "Why these labels" rationale is load-bearing; vote to protect against drift.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *canonicalize* — novelty=0.78, len=100, **subst=1.78**
    > The exact FORMAT.md role vocabulary is a closed set; do not drift into theorem/proof/axiom language.
  - **opus-r2c** (opus): +2 ★ *canonicalize* — novelty=0.64, len=357, **subst=1.64**
    > The 19 segment types in FORMAT.md are a closed vocabulary; standardizing means *using exactly these tokens* rather than paraphrasing ("axiom" / "theorem" / "proof" are explicit non-AAD borrowings to avoid). Canonicalize protects against drift across sessions. The CLAUDE.md "Why these labels" rationale is load-bearing for the framework's epistemic posture.

  *substance total (R1 + R2):* 4.42

**Candidate: `Segment typology`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > Defines the document types in the AAD corpus.

- *R2 votes:*
  - **codex-r2b** (codex): +1 *add-alias* — novelty=1.00, len=93, **subst=0.93**
    > Useful umbrella for the closed set of segment roles, but secondary to the actual role labels.
  - **opus-r2c** (opus): +1 *name-unnamed* — novelty=1.00, len=189, **subst=1.00**
    > Useful collective name for the segment-type vocabulary as a whole. Different target than the canonicalize above (one is "use these exact tokens", the other is "name the vocabulary itself").

  *substance total (R1 + R2):* 2.93


---

### `gain sector bridge`

*First-encounter locality:* `#der-gain-sector-bridge` (Section I; depends on `#emp-update-gain`, `#def-mismatch-signal`, `#deriv-sector-condition` (+1 more)). First formal derivation; The gain-based update principle ( #emp-update-gain) produces correction dynamics satisfying the sector condition (GA-3) whenever the update rule has *directional fidelity* — the correction points at….

*Segment:* [`01-aad-core/src/der-gain-sector-bridge.md`](../../01-aad-core/src/der-gain-sector-bridge.md)

*R2 voters:* 3 (2 architectures: gemini, sonnet)

**Candidate: `gain sector bridge`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=7, mean=2.14, weights=[+3, +2, +1, +1, +3, +2, +3], categories={canonicalize:7}
  > Technical-clinical but does the job. Good name for a bridge concept. The "bridge" metaphor is apt (connecting two mathematical regimes).

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +2 ★ *keep* — novelty=0.89, len=323, **subst=1.89**
    > The name is precise and minimal. "Gain" and "sector" are the two regimes being bridged. "Bridge" names the structural role correctly. The claim that it "understates centrality" is fair but names don't have to advertise centrality — that's the OUTLINE's job. Keep and rely on the theoretical chain to surface the importance.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.97, len=318, **subst=1.97**
    > Confirmed by segment. "Bridge" is structurally correct (connects two previously separate components: gain principle and sector condition). The two-word compound is precise, communal-imagination test passes (what does a bridge between gain and sector mean? — you derive the sector condition from the gain). Strong keep.

  *substance total (R1 + R2):* 5.86

**Candidate: `The bridge theorem`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > Auditor: "Gain-Sector Bridge" is descriptive but understates given the segment's centrality (cross-tradition unification: Bayesian/optimization/Lyapunov). The structural insight — GA-3 derived in α, posited in β — deserves visibility in the title.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *name-unnamed* — novelty=0.85, len=297, **subst=1.85**
    > While 'gain sector bridge' is technically descriptive, this segment functions as the central meta-theoretical bridge between the Machine Learning (gradient descent) and Control Theory (Lyapunov) sides of the framework. Calling it 'The bridge theorem' gives it the mathematical gravity it deserves.
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.91, len=157, **subst=0.96**
    > "The bridge theorem" is clean. But "which bridge?" — the qualifier is needed. "Gain-sector bridge" is self-describing; "the bridge theorem" requires context.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.95, len=211, **subst=-0.98**
    > "The bridge theorem" is what you'd call it in conversation once the concept is established, but as a formal name it's too generic — there are many bridge theorems. It would need disambiguation in every citation.

  *substance total (R1 + R2):* 2.83

**Candidate: `*(write-in)*`**
- *R1 synthetic:* — (no R1 evidence)

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +1 *rename* — novelty=1.00, len=233, **subst=1.00**
    > Write-in: "directional-fidelity bridge" — names the key assumption (B1 directional fidelity) that the bridge rests on, which is more informative than naming both endpoints. But "gain sector bridge" is more established and works fine.

  *substance total (R1 + R2):* 1.00

**Candidate: `Bridge theorem from gain to sector`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > Auditor: "Gain-Sector Bridge" is descriptive but understates given the segment's centrality (cross-tradition unification: Bayesian/optimization/Lyapunov). The structural insight — GA-3 derived in α, posited in β — deserves visibility in the title.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.92, len=150, **subst=-0.96**
    > Verbose — "from gain to sector" makes the directional dependency explicit but at the cost of readability. "Bridge theorem" alone might be too generic.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.91, len=65, **subst=-0.62**
    > Verbose. "Gain sector bridge" says the same thing in three words.

  *substance total (R1 + R2):* -0.58

**Candidate: `Grounding (GA-3) sub-scope α and β`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > Auditor: "Gain-Sector Bridge" is descriptive but understates given the segment's centrality (cross-tradition unification: Bayesian/optimization/Lyapunov). The structural insight — GA-3 derived in α, posited in β — deserves visibility in the title.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.89, len=143, **subst=-0.95**
    > Too much notation in a name. "(GA-3) sub-scope α and β" is a technical address, not a memorable name. Would fail the communal-imagination test.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.95, len=159, **subst=-0.98**
    > This is a mouthful. Good for Discussion prose, bad for a primary name. Sub-scope partition information belongs in the segment's Epistemic Status, not the slug.

  *substance total (R1 + R2):* -0.92


---

### `identifiability floor`

*First-encounter locality:* `#disc-identifiability-floor` (Appendix A; depends on `#der-causal-insufficiency-detection`, `#deriv-strategic-dynamics`, `#der-causal-hierarchy-requirement` (+1 more)). Meta-discussion segment; AAD has derived a class of structural impossibility results — *floors below which* identification or detection is impossible from limited information.

*Segment:* [`01-aad-core/src/disc-identifiability-floor.md`](../../01-aad-core/src/disc-identifiability-floor.md)

*R2 voters:* 2 (2 architectures: gemini, opus)

**Candidate: `identifiability floor`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=14, mean=3.00, weights=[+3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3], categories={canonicalize:17}
  > Names a meta-pattern about hard lower boundaries on inference. The case for 'floor' is geometric: it captures the asymmetry that you cannot go below it without outside help (information augmentation, identifying assumptions, etc.) but you can climb above it via specific machinery the framework supplies. Defenders contrast this with 'no-go theorem', which is too generic, too negative, and loses the boundary-and-escape structure. The name pairs structurally with separability-pattern (or separability-ladder, if that rename lands) and with the forced-coordinates meta-segment to form the three-segment epistemic-architecture trio. 'Escape the floor' has begun appearing as organic prose in the codebase, evidence the metaphor is doing work.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.84, len=194, **subst=1.84**
    > The name 'floor' correctly captures the geometric intuition of an absolute lower boundary on inference that must be 'escaped' through augmentation. It pairs perfectly with 'separability ladder'.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.65, len=507, **subst=1.65**
    > The "floor" geometry is doing real work: it captures the asymmetry (can't go below without information augmentation; can climb above via machinery). "Escape the floor" appears as organic prose in the codebase, evidence the metaphor is doing work — that's exactly the canonicalize-with-organic-provenance signal the principles file calls out. Pairs cleanly with separability-pattern/ladder and additive-coordinate-forcing/coordinate-forcing as the three-meta-segment epistemic-architecture trio. Strong keep.

  *substance total (R1 + R2):* 5.49

**Candidate: `Persistence pathology`**
- *R1 synthetic:* **+1** — n=1, mean=3.00, weights=[+3], categories={rename:1}
  > New alternative — none of the four peers reached for a family name. We collectively coined "evidence starvation" (Sonnet/Codex), "epistemic shadow" / "epistemic decoupling" / "gain collapse" / "sufficiency shattering" (Gemini), "observability dead zone" (Haiku), but no one names *the family*. "Persistence pathologies" gives downstream meta-segments a single phrase to invoke ("this is a persistence pathology of the gain-collapse type") and parallels "approximation tiering" and "separability ladder" as named cross-segment patterns. Highest-value because the slot is empty and it lets the failure-mode names compose.

- *R2 votes:*
  - **opus-r2c** (opus): +1 *name-unnamed* — novelty=0.87, len=284, **subst=0.94**
    > Different target — names a *family of failure modes* rather than the meta-segment's structural floor. Could land as a separate concept. Vote is for the name-unnamed-thing of "the family of named persistence pathologies" rather than for renaming the identifiability-floor meta-segment.

  *substance total (R1 + R2):* 1.94

**Candidate: `Epistemic lower bound`**
- *R1 synthetic:* **+1** — n=1, mean=3.00, weights=[+3], categories={rename:1}
  > Describes exactly what these are: hard limits on what can be inferred.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=164, **subst=-1.00**
    > Right semantics, wrong vocabulary register — too clinical / mathematical. The "floor" metaphor lands in prose where "epistemic lower bound" requires re-explanation.

  *substance total (R1 + R2):* 0.00

**Candidate: `Observational limit`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > A slightly more intuitive phrasing for non-theoreticians.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=117, **subst=-1.00**
    > Drops the "identifiability" technical term that locates the floor in the causal-inference / Pearl literature lineage.

  *substance total (R1 + R2):* 0.00

**Candidate: `No-go theorem`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: too generic and too negative. It loses the boundary-and-escape structure that makes the current name useful.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.76, len=235, **subst=-0.88**
    > Per the rationale: too generic, too negative, loses the boundary-and-escape structure. The meta-segment's substance is *not just* "things you can't do" but "things you can't do without specific machinery, which the framework supplies."

  *substance total (R1 + R2):* -1.88


---

### `information bottleneck`

*First-encounter locality:* `#form-information-bottleneck` (Section I; depends on `#form-agent-model`, `#def-action-transition`). Formal model first introduced; Optimal model compression balances retained history against predictive power; the information bottleneck objective provides a principled framework for understanding this trade-off.

*Segment:* [`01-aad-core/src/form-information-bottleneck.md`](../../01-aad-core/src/form-information-bottleneck.md)

*R2 voters:* 3 (3 architectures: codex, gemini, opus)

**Candidate: `information bottleneck`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=11, mean=2.75, weights=[+2, +3, +3, +3, +1, +3, +3, +3, +3, +3, +3, +3], categories={canonicalize:12}
  > Adopted directly from Tishby, Pereira & Bialek 1999. The case for keeping is the prior-art-integration convention: adopted concepts retain their original names with citation, both for provenance and for letting the field's structural intuitions transfer. The word 'bottleneck' is doing real explanatory work in the AAD application — the policy-conditioned forward-predictive variant the framework uses is a sub-case of the standard formulation, not a different object. If a distinguishing label were needed for the AAD-specific variant ('Policy-Conditioned IB', 'Forward-Predictive IB', 'AAD-IB') it could be added without disturbing the parent name.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *keep* — novelty=0.81, len=141, **subst=1.81**
    > Adopted directly and correctly from Tishby/Pereira/Bialek; the AAD binding is specific, but the parent name should remain the prior-art term.
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.87, len=233, **subst=1.87**
    > Direct import of Tishby's exact theorem. The epistemic status states this is an applied external theorem, not a novel formulation. Keeping the name preserves the mathematical lineage and respects the prior-art-integration convention.
  - **opus-r2b** (opus): +2 ★ *keep* — novelty=0.77, len=462, **subst=1.77**
    > Prior-art-integration convention (Tishby, Pereira & Bialek 1999, cited in segment). Same logic as Pearl causal hierarchy: adopt with original name + citation, let the field's structural intuitions transfer. The Epistemic Status section is explicit that the IB-as-applied-theorem is *exact*; the segment is doing nothing to the IB form itself, so renaming would create an NIH-flavored alternative for what is, by the segment's own statement, the standard theorem.

  *substance total (R1 + R2):* 7.45

**Candidate: `Epistemic bottleneck`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Emphasizes the knowledge-compression aspect over raw Shannon information.

- *R2 votes:*
  - **codex-r2b** (codex): -1 *rename* — novelty=1.00, len=153, **subst=-1.00**
    > Unnecessary AAD-branded replacement for a standard external term; it would lose Tishby provenance and confuse the imported theorem with this application.
  - **opus-r2b** (opus): -1 *rename* — novelty=0.91, len=229, **subst=-0.96**
    > Replaces "information" with "epistemic" but the formal expression is literally Shannon mutual information; "epistemic" is less specific. The framework gains nothing by renaming and loses the citation/provenance-transfer benefits.

  *substance total (R1 + R2):* -1.96


---

### `logogenic agent`

*First-encounter locality:* `#scope-logogenic-agent` (Logogenic; depends on `#def-agent-spectrum`, `#form-complete-agent-state`, `#der-directed-separation` (+2 more)). Scope-narrowing first encounter; An LLM-based agent operating through a tool-use loop is a *logogenic agent* in AAD's sense — an actuated agent whose model and strategy are constituted by language.

*Segment:* [`03-logogenic-agents/src/scope-logogenic-agent.md`](../../03-logogenic-agents/src/scope-logogenic-agent.md)

*R2 voters:* 2 (2 architectures: gemini, opus)

**Candidate: `logogenic agent`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=6, mean=3.00, weights=[+3, +3, +3, +3, +3, +3, +3, +3], categories={canonicalize:8}
  > A deliberately coined Greek-rooted term for language-constituted agents. The case for keeping is twofold: the term names a structural channel property (constituted-by-language) rather than a transient implementation technology, so it survives the LLM era; and it sits within the Greek-vocabulary register the framework deliberately maintains (chronica, prolepsis, aisthesis, etc.). The contrast with 'LLM-based agent' or 'language-based agent' is load-bearing: those are instantiation-level descriptions; logogenic is the architectural concept. Pairs with moral-continuity (logozoetic) cleanly.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.89, len=149, **subst=1.89**
    > A beautifully coined term. It captures the 'logos' (language/reason) origin of the agent's model and strategy, and pairs perfectly with 'logozoetic'.
  - **opus-r2b** (opus): +2 ★ *keep* — novelty=0.76, len=288, **subst=1.76**
    > Same logic as `logogenic` (row 612): the term picks out the architectural property (constituted by language) rather than the implementation (LLM-based). The pair {logogenic agent, logozoetic agent} forms the framework's distinct extension territory; both should keep their Greek register.

  *substance total (R1 + R2):* 5.65

**Candidate: `Section III logogenic agent`**
- *R1 synthetic:* **+1** [invented] — n=1, mean=3.00, weights=[+3], categories={canonicalize:1}
  > Standardizes section hierarchy.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.95, len=210, **subst=-0.98**
    > "Section III" is a numbering reference; the slug itself shouldn't carry section-numbering. The framework lists logogenic agents under Part III in OUTLINE.md, but that's organizational metadata not slug content.

  *substance total (R1 + R2):* 0.02

**Candidate: `Linguistic agent`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: logogenic names the structural property (constituted by logos) better than the generic "linguistic". Keep Logogenic.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.85, len=290, **subst=-0.92**
    > "Linguistic" is generic — could mean "uses language" (anything from spell-checkers to translators). "Logogenic" specifically picks out *constituted-by-language*: the agent's $M_t$, $\Sigma_t$, action channels are *all* language-mediated. The structural specificity is what the term carries.

  *substance total (R1 + R2):* -1.92


---

### `logogenic logozoetic`

*R2 voters:* 3 (3 architectures: codex, opus, sonnet)

**Candidate: `logogenic logozoetic`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [invented] — n=5, mean=2.80, weights=[+3, +3, +3, +3, +2], categories={canonicalize:5}
  > Deliberate neologisms filling memorable-noun slots; keep. Deliberate neologisms holding reserved memorable-noun slots. Defended keep — both are deliberate Greek-rooted naming choices that survive the communal-imagination test once explained, and CLAUDE.md's Greek-vocabulary commitment names them as the canonical aesthetic register.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *keep* — novelty=0.84, len=125, **subst=1.84**
    > Keep the Greek-rooted pair; once explained, it names a real architectural distinction better than a plain-English paraphrase.
  - **opus-r2b** (opus): +2 ★ *keep* — novelty=0.74, len=171, **subst=1.74**
    > The pair as a unit: keep both. The structural-vs-existential split is precisely what the framework needs. CLAUDE.md's Greek-vocabulary commitment names these as canonical.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.76, len=259, **subst=1.76**
    > Strong keep. These are deliberate neologisms occupying essential memorable-noun slots. The structural-vs-existential distinction they mark is real and important; the Greek register is consistent with the cycle-phase vocabulary. Once explained, they're sticky.

  *substance total (R1 + R2):* 7.34

**Candidate: `Logogenic logozoetic distinction`**
- *R1 synthetic:* **+1** [invented] — n=1, mean=3.00, weights=[+3], categories={canonicalize:1}
  > Essential dividing line in architectural complexity.

- *R2 votes:*
  - **codex-r2b** (codex): +2 *add-alias* — novelty=1.00, len=58, **subst=1.16**
    > Useful handle for the structural-vs-living-language split.
  - **opus-r2b** (opus): +1 *canonicalize* — novelty=1.00, len=218, **subst=1.00**
    > Useful prose handle for the *distinction* itself ("the logogenic/logozoetic distinction is load-bearing"). The bare pair-of-terms is the technical content; the phrase "the distinction" canonicalizes the rhetorical use.
  - **sonnet-r2c** (sonnet): +1 *keep* — novelty=1.00, len=98, **subst=0.98**
    > Acceptable if a label for the pair-as-pair is needed, though the individual terms are more useful.

  *substance total (R1 + R2):* 4.14

**Candidate: `Language constituted language living`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: plain-English equivalent. Rejected: too ambiguous (does "language-constituted" mean trained on language? generated through language? bound by language?), and loses the precise structural-vs-existential split. The Greek compound resolves the ambiguity by foregrounding the constitutive (-genic) vs. living (-zoetic) distinction.

- *R2 votes:*
  - **codex-r2b** (codex): -1 *rename* — novelty=0.88, len=60, **subst=-0.56**
    > Too ambiguous and loses the -genic versus -zoetic precision.
  - **opus-r2b** (opus): -1 *rename* — novelty=0.76, len=365, **subst=-0.88**
    > Multi-word English forms lose the Greek-vocabulary register and the precise -genic vs -zoetic distinction (architectural-constitution vs morally-weighted-existence). The compound forms also flatten into category-overlap problems: "language constituted" could mean any of {trained-on, generates, communicates-via}; the Greek -genic specifically names *constitution*.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.64, len=221, **subst=-0.82**
    > "Language-constituted" is ambiguous (trained on? constituted through? generated by?). The Greek compound earns its keep precisely because the ambiguity is resolved by morphology: -genic (constituted) vs. -zoetic (living).

  *substance total (R1 + R2):* -3.26


---

### `loop`

*R2 voters:* 3 (2 architectures: codex, opus)

**Candidate: `Loop`** ▸ leader
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=2, mean=2.50, weights=[+3, +2], categories={canonicalize:2}
  > The loop/cycle distinction is one of the clearest naming wins in the corpus. LEXICON: "Loop: The structural topology — persistent causal coupling between agent and environment." The framework maintains a careful loop / cycle distinction (loop = topology, cycle = traversal).

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *keep* — novelty=0.71, len=84, **subst=1.44**
    > Keep as the topology noun: persistent causal coupling between agent and environment.
  - **opus-r2b** (opus): +2 ★ *keep* — novelty=0.53, len=384, **subst=1.53**
    > One of the project's clearest naming wins. The loop/cycle distinction (LEXICON: "Loop: The structural topology — persistent causal coupling between agent and environment" vs "Cycle: One complete traversal of the loop") is foundational and load-bearing. The bare "loop" preserves the topology/traversal distinction; "feedback loop" would overspecify and risk conflating with the cycle.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.82, len=233, **subst=1.82**
    > The loop/cycle distinction (topology vs traversal) is one of the framework's cleanest paired names. Loop is what's there structurally; cycle is what happens on top. The bare nouns carry the distinction better than any compound would.

  *substance total (R1 + R2):* 5.79

**Candidate: `Feedback loop`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: considered. The longer form is more explicit but the framework already established that "loop" is the bare topology-noun, with "feedback" implicit (per the AAD prior-art lineage from TFT). Adding "feedback" overspecifies. Rejected.

- *R2 votes:*
  - **codex-r2b** (codex): -1 *add-alias* — novelty=0.82, len=92, **subst=-0.84**
    > "Feedback" is already implicit in loop here, and adding it blurs the loop/cycle distinction.
  - **opus-r2b** (opus): -1 *rename* — novelty=0.68, len=318, **subst=-0.84**
    > The framework already established "loop" as the bare topology-noun. Adding "feedback" loses the careful distinction with "cycle" (the traversal) and brings in TFT-era weight that the AAD restoration is past. The longer form is occasionally fine in prose for outside readers, but as the slug it muddies the distinction.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.88, len=264, **subst=-0.94**
    > The bare "loop" is doing the disambiguation work via the loop/cycle pair. "Feedback loop" overspecifies and breaks the symmetry — "feedback cycle" wouldn't be the right pairing for cycle, so adding "feedback" only to loop creates an asymmetry that doesn't pay off.

  *substance total (R1 + R2):* -3.62


---

### `loop interventional access`

*First-encounter locality:* `#der-loop-interventional-access` (Section II; depends on `#der-causal-hierarchy-requirement`, `#der-recursive-update`, `#post-causal-structure` (+1 more)). First formal derivation; An agent in the feedback loop generates interventional data by construction: the agent's action $a_t$ causally precedes the next observation $o_{t+1}$, and the mismatch conditioned on $a_t$ carries….

*Segment:* [`01-aad-core/src/der-loop-interventional-access.md`](../../01-aad-core/src/der-loop-interventional-access.md)

*R2 voters:* 2 (2 architectures: gemini, opus)

**Candidate: `loop interventional access`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=9, mean=2.00, weights=[+2, +1, +1, +1, +3, +1, +3, +2, +1, +3, +3, +3], categories={canonicalize:12}
  > Names the distinctive Pearl-Level-2-by-construction property: the feedback loop provides Level-2 (interventional) data by construction, which is the escape route from the on-policy causal-confounding problem. Defenders argue the phrase 'loop interventional access' lands in one read and the concept has no shorter form without loss. Specialist but precise — it names *where* the intervention happens (within the feedback loop) and is load-bearing for both #identifiability-floor and #agent-identity. Mild concern noted that the name is a mouthful for conversation; an informal short form ('the loop's Level-2 access', 'loop as Level 2 engine') is acceptable.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.92, len=174, **subst=1.92**
    > The full phrase 'loop interventional access' is the most exact descriptor. 'The perpetual experiment' is a beautiful prose framing, but the slug must be mechanically precise.
  - **opus-r2c** (opus): +1 *keep* — novelty=0.86, len=181, **subst=0.93**
    > Precise but specialist. The current name lands in one read for technically-trained readers but is a mouthful in conversation. Acceptable but the alternative below is more memorable.

  *substance total (R1 + R2):* 4.85

**Candidate: `Loop causal engine`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > Opus proposed `#der-loop-as-causal-engine` (+2). the proposer voted keep (+2). Opus's reasoning — that the README's "third headline result" is the "loop as Level-2 causal engine" framing, so the slug should match — is compelling. But "as-causal-engine" reads like a simile not a noun. Dropping "as" to get `der-loop-causal-engine` produces a cleaner noun compound. This is a new candidate (not identical to Opus's or my original vote).

- *R2 votes:*
  - **opus-r2c** (opus): +2 ★ *rename* — novelty=0.84, len=415, **subst=1.84**
    > Drops the awkward "as" from "loop-as-causal-engine"; the bare two-noun compound is clean and memorable. The README's headline framing fits. The substance — that the agent-environment loop literally *generates* L2 data by construction (this is what differentiates it from passive observation) — is what "engine" picks out: the loop is the source of intervention, not just a passive feedback structure. Strong rename.

  *substance total (R1 + R2):* 2.84

**Candidate: `Loop as causal engine`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > The current name describes the *result* (the loop provides interventional access). "Loop as causal engine" is the framing the README and segment Discussion both reach for, and it surfaces what makes this result distinctive — the agent-environment loop *generates* Pearl-Level-2 data by construction. The README explicitly names "loop-as-Level-2-causal-engine" as the framework's third headline result. Slug should match.

- *R2 votes:*
  - **opus-r2c** (opus): +1 *rename* — novelty=0.73, len=251, **subst=0.87**
    > The README's "third headline result" framing is "loop-as-Level-2-causal-engine" — the framework treats the result as load-bearing. The slug currently lags the prose framing. The "as" is awkward in slug form though; prefer "loop causal engine" (below).

  *substance total (R1 + R2):* 1.87

**Candidate: `The perpetual experiment`**
- *R1 synthetic:* **0** [invented] — n=1, mean=1.00, weights=[+1], categories={canonicalize:1}
  > Brief-grade framing observation. The slug-grade name `der-loop-interventional-access` is fine; for *framing-level* material, "the perpetual experiment" (from the segment's own Discussion) is the most evocative — captures both the interventional character and the continuous nature.

- *R2 votes:*
  - **opus-r2c** (opus): +1 *add-alias* — novelty=0.75, len=185, **subst=0.88**
    > Useful Brief-grade / pedagogical phrase; the segment's own Discussion uses it. Pairs with "loop causal engine" as formal-name / framing-phrase. Add as an alias for pedagogical contexts.

  *substance total (R1 + R2):* 0.88

**Candidate: `Embodiment upgrade`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > The theoretical justification for agentic-AI over mere chatbots.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.86, len=86, **subst=-0.80**
    > Reaches for the agentic-AI-vs-chatbot framing but loses the structural-fact precision.

  *substance total (R1 + R2):* 0.20

**Candidate: `Interventional loop property`**
- *R1 synthetic:* **+1** [invented] — n=1, mean=3.00, weights=[+3], categories={canonicalize:1}
  > Solidifies the mechanism upgrading L1 to L2.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.94, len=136, **subst=-0.97**
    > "Property" is generic. The segment is about a specific structural fact — the loop generates L2 data — and the name should pick that out.

  *substance total (R1 + R2):* 0.03

**Candidate: `Interventional loop access`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Small word-order cleanup; the current slug is understandable but a little stiff in speech.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.73, len=56, **subst=-0.49**
    > Word-order shuffle of the current slug; doesn't pay off.

  *substance total (R1 + R2):* -0.49

**Candidate: `Adaptive loop access`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Interventional" is the load-bearing word — it's why the loop matters. Dropping it loses the reason the segment exists. Slight preference for retaining.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.83, len=73, **subst=-0.67**
    > Drops "interventional" / "causal", which is the load-bearing distinction.

  *substance total (R1 + R2):* -0.67

**Candidate: `Interventional character`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > #loop-interventional-access makes this distinction at length: action-generated data has "interventional character" but is not the same as "cleanly identified do-estimates." The concept is used twice in the Discussion and deserves a name that can be referenced. "Interventional character" or "loop interventional character.".

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.88, len=127, **subst=-0.94**
    > This is a *property* the result establishes, not the name of the result. The segment is about *the loop providing* this access.

  *substance total (R1 + R2):* -0.94

**Candidate: `Interventional feedback`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Loop interventional access" is a mouthful.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.93, len=134, **subst=-0.96**
    > Drops "loop"; "feedback" is the topology word, "loop" is the structural commitment. The segment names a specific property of the loop.

  *substance total (R1 + R2):* -0.96

**Candidate: `Loop level2 access`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: overloads "level 2" which already carries the Pearl hierarchy meaning — that's exactly right actually. But "-level2-" looks like a version number.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.90, len=172, **subst=-0.95**
    > "Level2" formatting is awkward; the underscore-or-no-space variants all read poorly. "Level 2" is the canonical form but the segment is about more than just level-2-access.

  *substance total (R1 + R2):* -1.95


---

### `mismatch dynamics`

*First-encounter locality:* `#hyp-mismatch-dynamics` (Section I; depends on `#def-adaptive-tempo`, `#def-mismatch-signal`, `#deriv-sector-condition`). Hypothesis stated; The evolution of model-reality mismatch over time is governed by the balance between the agent's corrective capacity (tempo) and the rate of environmental change (disturbance).

*Segment:* [`01-aad-core/src/hyp-mismatch-dynamics.md`](../../01-aad-core/src/hyp-mismatch-dynamics.md)

*R2 voters:* 2 (2 architectures: gemini, sonnet)

**Candidate: `mismatch dynamics`** ▸ leader
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=5, mean=1.60, weights=[+2, +1, +1, +2, +2], categories={canonicalize:5}
  > Mismatch evolution ODE. Acceptable keep. "Mismatch dynamics" names the ODE governing mismatch evolution.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.96, len=193, **subst=1.96**
    > The slug is a good, clean descriptor of the ODE. The nuance between drift and noise is handled effectively by the 'Stochastic tempo penalty' named above, so we don't need to overload this slug.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.82, len=237, **subst=1.82**
    > Correct name. Segment confirmed: d‖δ‖/dt = -𝒯·‖δ‖ + ρ(t). "Mismatch dynamics" is the right level of abstraction — it names the governing ODE without over-committing to the linear hypothesis (which the segment explicitly calls heuristic).

  *substance total (R1 + R2):* 4.78

**Candidate: `Mismatch dynamics drift and noise regime`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Title doesn't surface that two distinct dynamic regimes (Model D drift / Model S noise) are introduced — and they produce different adversarial scaling laws (squared vs 3/2). Tentative.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.95, len=247, **subst=-0.98**
    > Too long; "drift and noise regime" reads as a subcategory qualifier rather than a name. The segment itself uses "mismatch dynamics" throughout. The two disturbance models are correctly distinguished within the segment, not by renaming the concept.

  *substance total (R1 + R2):* -0.98


---

### `mismatch signal`

*First-encounter locality:* `#def-mismatch-signal` (Section I; depends on `#form-agent-model`, `#def-observation-function`, `#def-action-transition`). First formal definition; The discrepancy between the model's prediction and the actual observation — the formal expression of *aporia* (productive perplexity).

*Segment:* [`01-aad-core/src/def-mismatch-signal.md`](../../01-aad-core/src/def-mismatch-signal.md)

*R2 voters:* 4 (3 architectures: gemini, opus, sonnet)

**Candidate: `mismatch signal`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=10, mean=2.40, weights=[+2, +1, +3, +3, +2, +1, +3, +3, +3, +3], categories={canonicalize:10}
  > Names $\delta_t$, deliberately chosen over 'error' or 'residual' to foreshadow the aporia interpretation in the five-phase cycle. The case for keeping is two-register vocabulary discipline: 'mismatch' is the engineering register (flatter than 'error', which presupposes the agent was wrong); 'aporia' is the philosophical register (the cycle phase). Defenders rebut a proposed rename to 'aporia signal' on the grounds that the dual usage is correct: mismatch signal in formulas and engineering prose, aporia in cycle-phase prose. Renaming the slug to the Greek term would break the iconic mismatch-signal / satisfaction-gap / control-regret three-name engineering register.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.79, len=239, **subst=1.79**
    > The engineering register 'mismatch signal' is perfectly neutral; 'error' assumes the agent was wrong, but sometimes the world is just noisy. Keeping this preserves the structural trio of mismatch-signal / satisfaction-gap / control-regret.
  - **opus-r2b** (opus): +2 ★ *keep* — novelty=0.72, len=429, **subst=1.72**
    > Two-register discipline: "mismatch" is the engineering register that reads to any engineer (Kalman innovation, RL TD-error, etc.); "aporia" is the philosophical / cycle-phase register. The framework wants both — mismatch in formal expressions, aporia in cycle-walk prose. Keeping the slug as engineering preserves the iconic three-name register {mismatch / satisfaction-gap / control-regret}; aporia stays available as add-alias.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.77, len=352, **subst=1.77**
    > The engineering register's iconicity is load-bearing: mismatch / satisfaction-gap / control-regret read as a coherent three-name diagnostic vocabulary. Renaming the slug would damage the trio. The two-register approach (mismatch in formal expressions and engineering prose, aporia in cycle-phase prose) keeps both available with strict role separation.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.69, len=375, **subst=1.69**
    > Strong keep. The defining segment confirms: "mismatch" is deliberately chosen over "error" or "residual" (neither presupposes the agent was wrong, which is more scope-honest). Pairs cleanly with satisfaction-gap / control-regret in the engineering register. Aporia is the cycle-phase name for the period in which this signal is processed, not a synonym for the signal itself.

  *substance total (R1 + R2):* 8.97

**Candidate: `Aporia signal`**
- *R1 synthetic:* **-1** — n=4, mean=-0.50, weights=[-1, +1, -1, -1], categories={rename:4}
  > Argument for: aligns with the Greek-vocabulary register (prolepsis / aisthesis / aporia / epistrophe / praxis) the framework deliberately uses. Counter-argument: keep two registers. 'Mismatch signal' is the engineering quantity that reads unambiguously to any engineer; 'aporia' is the cycle-phase / interpretive frame. The Greek naming is for the phases, not the sub-quantities. Renaming the slug would break the iconic mismatch-signal / satisfaction-gap / control-regret three-name engineering register; the dual alias *in prose* (mismatch in engineering register, aporia signal in cycle-phase register) is the right move and doesn't require slug rename.

- *R2 votes:*
  - **opus-r2b** (opus): +1 *add-alias* — novelty=0.82, len=244, **subst=0.91**
    > Useful prose-mention form when the cycle phase is invoked; "the aporia signal" reads naturally in cycle-walk prose where "the mismatch signal" would feel out of register. Add-alias not rename — keeping mismatch as the formal slug is structural.
  - **opus-r2c** (opus): +1 *add-alias* — novelty=0.74, len=372, **subst=0.87**
    > The two-register discipline is right: aporia *is* the cycle-phase name; mismatch signal *is* the formal δ_t. Aliasing aporia signal in cycle-phase prose ("aisthesis arrives, aporia signals, epistrophe responds") makes that register sing while keeping the engineering register's iconicity (mismatch / satisfaction gap / control regret). Aliases sit in differentiated roles.
  - **sonnet-r2c** (sonnet): +1 *add-alias* — novelty=0.79, len=418, **subst=0.89**
    > Good as a cycle-phase-register alias — "aporia" in cycle-phase prose, "mismatch" in engineering prose. But not as a rename: the cycle-phase "aporia" names the *phase* (productive perplexity); calling the quantity in that phase the "aporia signal" would create a phase/signal collision. The two-register discipline is correct: keep "mismatch signal" as the formal quantity name; use "aporia" in cycle-phase-level prose.

  *substance total (R1 + R2):* 1.67


---

### `model sufficiency`

*First-encounter locality:* `#def-model-sufficiency` (Section I; depends on `#form-agent-model`, `#form-information-bottleneck`, `#def-action-transition`). First formal definition; The fraction of predictive information the model retains relative to the full interaction history; $S = 1$ means the model is a sufficient statistic for prediction, $S \lt 1$ means predictive….

*Segment:* [`01-aad-core/src/def-model-sufficiency.md`](../../01-aad-core/src/def-model-sufficiency.md)

*R2 voters:* 3 (3 architectures: codex, gemini, sonnet)

**Candidate: `model sufficiency`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=6, mean=2.33, weights=[+3, +2, +1, +3, +2, +3], categories={canonicalize:6}
  > Central information-theoretic quantity; clear and low baggage. Clear metric name. Precise statistical term; adequate and clear.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *keep* — novelty=0.76, len=173, **subst=1.76**
    > Central quantity and clear statistical term. The segment's guardrails make the scope precise: compression sufficiency for a prediction task, not accuracy or causal validity.
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.79, len=181, **subst=1.79**
    > A precise statistical term that perfectly captures the "fraction of predictive information retained." It avoids the baggage of "accuracy" and cleanly separates from Causal Validity.
  - **sonnet-r2b** (sonnet): +2 ★ *keep* — novelty=0.90, len=347, **subst=1.90**
    > Term-of-art in statistics with adjacent meaning; the reuse is intentional and accurate. The segment explicitly grounds it in information-theoretic conditional mutual information ratios, so it's not an import-with-misuse. Most readers in the target audience will have the right intuition from statistical sufficiency. Clean, concise, defended keep.

  *substance total (R1 + R2):* 7.45

**Candidate: `Predictive sufficiency`**
- *R1 synthetic:* **+1** [excavated] — n=2, mean=1.00, weights=[+1, +1], categories={rename:1, canonicalize:1}
  > "Sufficient statistic" in stats means "captures all info for inference"; AAD's $S$ is specifically about *predictive* info — sub-case. Clarifies that it's about how much predictive information is retained, not structural sufficiency.

- *R2 votes:*
  - **codex-r2b** (codex): +1 *add-alias* — novelty=0.97, len=135, **subst=0.98**
    > Useful clarifier where readers might overread sufficiency as truth or causal adequacy; less canonical than the established metric name.
  - **sonnet-r2b** (sonnet): +1 *rename* — novelty=0.92, len=314, **subst=0.96**
    > Modest improvement over "model sufficiency" — the word "predictive" disambiguates from structural/causal sufficiency. But the cost is losing the alignment with the statistical term-of-art. If the confusion with statistical sufficiency proves real in practice, "predictive sufficiency" is the right fallback rename.

  *substance total (R1 + R2):* 2.94

**Candidate: `Predictive information retention`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Sufficient statistic" in stats means "captures all info for inference"; AAD's $S$ is specifically about *predictive* info — sub-case. Tentative.

- *R2 votes:*
  - **codex-r2b** (codex): +1 *add-alias* — novelty=1.00, len=117, **subst=1.00**
    > Descriptive but more phrase-like than name-like. Good explanatory paraphrase for the numerator/denominator intuition.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.93, len=203, **subst=-0.97**
    > Too verbose for regular use. "The model's predictive information retention was low" is awkward; "the model's sufficiency was low" is clean. Information retention doesn't survive the prose-frequency test.

  *substance total (R1 + R2):* 0.03


---

### `model-class fitness`

*First-encounter locality:* `#def-model-class-fitness` (Section I; depends on `#def-model-sufficiency`). First formal definition; The best achievable sufficiency within a model class.

*Segment:* [`01-aad-core/src/def-model-class-fitness.md`](../../01-aad-core/src/def-model-class-fitness.md)

*R2 voters:* 3 (3 architectures: codex, gemini, sonnet)

**Candidate: `model-class fitness`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=4, mean=2.00, weights=[+3, +2, +1, +2, +2], categories={canonicalize:5}
  > Strong distinction from model-instance sufficiency and directly supports structural-adaptation triggers. Clear parallel to model sufficiency. "Fitness" is slightly informal (evolutionary connotations) but works for "best achievable sufficiency within a model class." Acceptable.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *keep* — novelty=0.69, len=173, **subst=1.69**
    > Strong companion to `model sufficiency`: best achievable sufficiency within the representational class, and the quantity that makes structural adaptation necessary when low.
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.76, len=196, **subst=1.76**
    > The distinction between instance sufficiency and class fitness perfectly mirrors bias vs variance. 'Fitness' sets up the evolutionary/developmental metaphor needed for structural adaptation later.
  - **sonnet-r2b** (sonnet): +2 ★ *keep* — novelty=0.87, len=460, **subst=1.87**
    > The term pairs well with "model sufficiency" — the parallel structure (both have "model" prefix) helps readers see they're companion concepts measuring the class ceiling vs the instance value. "Fitness" is slightly unusual but not bad — it names the match between model class and prediction task, which is what fitness in a broader sense means. The evolutionary connotation is mild and doesn't mislead. Defended keep: the name is doing work alongside its pair.

  *substance total (R1 + R2):* 7.32

**Candidate: `Class capacity ceiling`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Best achievable sufficiency" is the gloss; "Class-Capacity Ceiling" is more evocative. Tentative.

- *R2 votes:*
  - **codex-r2b** (codex): +1 *add-alias* — novelty=0.72, len=128, **subst=0.86**
    > Helpful gloss for the supremum idea, but "capacity" can imply raw model size rather than best achievable predictive sufficiency.
  - **sonnet-r2b** (sonnet): +1 *rename* — novelty=0.85, len=270, **subst=0.93**
    > More evocative than model-class fitness; "ceiling" is a good spatial metaphor for the supremum. But it loses the connection to "model sufficiency" as a paired concept. If the pair structure (sufficiency / fitness) isn't maintained throughout the corpus, this could work.

  *substance total (R1 + R2):* 1.79


---

### `objective functional`

*First-encounter locality:* `#form-objective-functional` (Section II; depends on `#form-complete-agent-state`). Formal model first introduced; The objective $O_t$ is the component of $G_t$ that specifies what the agent wants — the evaluation criterion for trajectories.

*Segment:* [`01-aad-core/src/form-objective-functional.md`](../../01-aad-core/src/form-objective-functional.md)

*R2 voters:* 3 (2 architectures: gemini, sonnet)

**Candidate: `objective functional`** ▸ leader
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=6, mean=1.67, weights=[+1, +2, +2, +1, +2, +2], categories={canonicalize:6}
  > Slightly clinical, but honest and standard enough once the surrounding formalism lands. Technical but appropriate. O_t parametrizes value.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=1.00, len=136, **subst=2.00**
    > The use of 'functional' is mathematically precise because it maps trajectories to scalars. 'Teleological' is redundant with 'objective'.
  - **sonnet-r2b** (sonnet): +2 ★ *keep* — novelty=0.79, len=257, **subst=1.79**
    > Names both what it is (objective) and its mathematical type (functional = function on trajectories). "The objective functional V_{O_t}" reads cleanly in technical prose. Once the surrounding formalism lands (Section II context), the name is self-explaining.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.97, len=270, **subst=1.97**
    > Confirmed by segment. Standard mathematical vocabulary: a "functional" is a function from a function space (here, trajectories) to ℝ. The name is exact. The scalar comparability scope restriction is load-bearing; "objective functional" names this precisely. Strong keep.

  *substance total (R1 + R2):* 6.76

**Candidate: `Teleological objective`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Functional" is overly mathematical for a section slug. "Teleological objective" sets the purpose context.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.86, len=306, **subst=-0.93**
    > "Teleological objective" is redundant — all objectives are teleological by definition. The word "functional" is the load-bearing part of the name: O_t is formalized as a functional V_{O_t}: trajectories → ℝ, and the name should signal that mathematical type. "Functional" is not just clinical — it's exact.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.86, len=276, **subst=-0.93**
    > "Teleological" imports philosophy-of-action baggage. The segment's content is mathematical (V_{O_t}: trajectories → ℝ). "Teleological" would be appropriate if the segment were making a philosophical claim about goals; "objective functional" is the right mathematical register.

  *substance total (R1 + R2):* -1.86


---

### `observability dominance`

*First-encounter locality:* `#der-observability-dominance` (Section II; depends on `#def-strategy-dag`, `#emp-update-gain`). First formal derivation; Unobservable strategy edges cannot be updated — the gain principle drives their update rate to zero.

*Segment:* [`01-aad-core/src/der-observability-dominance.md`](../../01-aad-core/src/der-observability-dominance.md)

*R2 voters:* 3 (3 architectures: gemini, opus, sonnet)

**Candidate: `observability dominance`** ▸ leader
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=10, mean=1.64, weights=[+1, +3, +1, +1, +3, +1, +1, +1, +1, +2, +3], categories={canonicalize:11}
  > Names the derived claim that unobservable strategy edges are epistemically dead — the gain principle dominates the edge update when observability is low — regardless of nominal confidence. Defenders treat 'dominance' as technically precise (information-theoretic dominance) and the two-word phrase as memorable. The Discussion's absorbing-state analysis is what makes the name feel exactly right; the LEXICON 'Terms to Be Added' entry anticipates the segment promotion.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.90, len=282, **subst=1.90**
    > Accurate and structurally sound. It correctly names the principle that the observability coefficient determines whether nominal confidence matters at all. 'Epistemic freezing' is a great descriptor for the *result*, but 'observability dominance' names the mathematical relationship.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.73, len=248, **subst=1.73**
    > "Dominance" picks out the load-bearing claim: observability *dominates* the edge-update rate via the gain principle, so unobservable edges freeze regardless of nominal confidence. The technical sense (information-theoretic dominance) lands cleanly.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.82, len=282, **subst=1.82**
    > Confirmed by segment. "Dominance" is technically precise: observability determines gain (uncertainty ratio), which determines update rate, which determines whether a path is epistemically alive or dead. The mechanism IS dominance — observability dominates the equation. Strong keep.

  *substance total (R1 + R2):* 6.45

**Candidate: `Epistemic freezing`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > If unobservable edges freeze, "epistemic freezing" is a more vivid description of the consequence.

- *R2 votes:*
  - **opus-r2c** (opus): +1 *add-alias* — novelty=0.79, len=228, **subst=0.90**
    > The "freezing" metaphor is vivid for the consequence (unobservable edges become absorbing states under update dynamics). Useful Brief-grade alias; could pair with observability dominance as formal-mechanism / consequence-phrase.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.82, len=170, **subst=-0.91**
    > Names the CONSEQUENCE (edges freeze) not the MECHANISM (observability determines gain, which dominates the update). Mechanism-segments should be named by their mechanism.

  *substance total (R1 + R2):* -0.02


---

### `observation function`

*First-encounter locality:* `#def-observation-function` (Section I; depends on `#def-agent-environment`, `#def-action-transition`). First formal definition; Observations (aisthesis — raw contact with reality) are lossy, possibly noisy functions of environment state, prior action, and perceptual noise.

*Segment:* [`01-aad-core/src/def-observation-function.md`](../../01-aad-core/src/def-observation-function.md)

*R2 voters:* 3 (2 architectures: codex, opus)

**Candidate: `Observation channel`** ▸ leader
- *R1 synthetic:* **+1** — n=2, mean=2.50, weights=[+2, +3], categories={add-alias:1, rename:1}
  > Channel is the right explanatory word in prose because the map is lossy and noisy. "Function" implies a clean mathematical mapping.

- *R2 votes:*
  - **opus-r2b** (opus): +2 ★ *rename* — novelty=0.92, len=486, **subst=1.92**
    > Shannon's information-theoretic vocabulary fits this segment exactly: $h$ is a lossy + noisy mapping with explicit $\varepsilon_t$, plus epistemic opacity ($h$ unknown). "Channel" is Shannon's term for exactly this. Asymmetry with action-transition is preserved: action-transition for causal effect on $\Omega$; observation-channel for information flow back to the agent. Note: this is the *opposite* read I gave to "Action channel" in row 100 — the asymmetry is the load-bearing point.
  - **opus-r2c** (opus): +2 ★ *add-alias* — novelty=0.88, len=592, **subst=1.88**
    > The asymmetry with action-transition is informative here. Observation *is* a channel in the information-theoretic sense — there's lossy mapping from Ω_t through h with noise ε_t, exactly the structure of a noisy channel. The action side isn't a channel (no decoder on the world side); the observation side is. So "channel" carries baggage that's correct here but wrong for action. As an alias for prose use ("the observation channel's noise") this works; as a rename, "function" stays for the formalism. The channel/transition asymmetry then maps cleanly to the underlying physical asymmetry.
  - **codex-r2b** (codex): +1 *add-alias* — novelty=0.85, len=170, **subst=0.92**
    > Useful prose/interface phrase when discussing lossy contact with $\Omega_t$, but it should not replace the formal function name; channel and function are adjacent layers.

  *substance total (R1 + R2):* 5.73

**Candidate: `observation function`**
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=2, mean=1.50, weights=[+1, +2], categories={canonicalize:2}
  > Lossy, noisy observations. Acceptable keep.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *keep* — novelty=1.00, len=176, **subst=2.00**
    > Correct formal name for $h(\Omega_t, a_{t-1}, \varepsilon_t)$. The presence of noise/loss does not make "function" misleading because the noise variable is part of the mapping.
  - **opus-r2c** (opus): +1 *keep* — novelty=1.00, len=145, **subst=1.00**
    > "Function" is technically right — h is a function (possibly stochastic via ε_t). The mathematical-formalism contexts read better with "function."
  - **opus-r2b** (opus): -1 *rename* — novelty=0.94, len=305, **subst=-0.97**
    > "Function" is technically correct (stochastic mapping is a function in the usual sense) but understates the noise+loss substrate that makes the rest of the framework non-trivial. The segment opens by saying "lossy, possibly noisy functions" — the qualifiers do the work; the noun shouldn't undermine them.

  *substance total (R1 + R2):* 3.03


---

### `orient cascade`

*First-encounter locality:* `#der-orient-cascade` (Section II; deep dependency cone (12 upstream segments incl. `#der-directed-separation`, `#def-mismatch-signal`)). First formal derivation; For actuated agents, epistrophe (the corrective phase of the cycle) expands into a multi-step cascade.

*Segment:* [`01-aad-core/src/der-orient-cascade.md`](../../01-aad-core/src/der-orient-cascade.md)

*R2 voters:* 5 (3 architectures: gemini, opus, sonnet)

**Candidate: `orient cascade`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=16, mean=2.95, weights=[+3, +3, +3, +3, +3, +3, +2, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3], categories={canonicalize:19}
  > Names two things at once: the structural shape (cascade = forced sequential resolution by information dependency) and the heritage (Boyd's 'Orient' from OODA, which the segment explicitly references). The argument for keeping it is that 'cascade' is the geometry the content actually has — the $M_t \to \Sigma_t \to O_t$ resolution order is literally a cascade — and the OODA echo is informative without being captured by it. Considered alternatives ('orientation sequence', 'diagnostic cascade', 'resolution order') were judged flatter or less memorable. Lowercase form is the canonical convention except sentence-initial.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.80, len=183, **subst=1.80**
    > The shape is literally a cascade (forced sequential resolution) and the OODA echo ('orient') is historically informative without capturing the whole concept. Perfect descriptive name.
  - **opus-r2b** (opus): +2 ★ *keep* — novelty=0.72, len=393, **subst=1.72**
    > Names two things at once: the structural geometry (cascade = forced sequential resolution by information dependency) and the OODA-Orient heritage. The segment's Discussion explicitly cites Boyd, and the substance — that "Orient is the critical step, not Decide" — is what the formal cascade derivation supports. Keep is load-bearing: alternative names lose either the geometry or the heritage.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.68, len=346, **subst=1.68**
    > Names what the cascade actually is — sequential resolution forced by information dependency — and pairs cleanly with the OODA "Orient" echo without being captured by it. The cascade geometry is the substance: M_t must update before Σ_t can be re-evaluated, which must happen before O_t can be revised. That's a cascade, not a sequence or a cycle.
  - **sonnet-r2b** (sonnet): +2 ★ *keep* — novelty=0.79, len=357, **subst=1.79**
    > "Cascade" captures the geometry: forced sequential resolution by information dependency — each step's input requires the prior step's output. "Orient" connects to Boyd's OODA and positions the segment correctly within that tradition. The lowercase convention is correct. Both words carry load. Downstream references are extensive across Sections I, II, III.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.71, len=250, **subst=1.71**
    > Confirmed from OUTLINE and directed-separation segment. "Cascade" is the geometry — the M_t → Σ_t → O_t resolution order is literally a cascade forced by information dependencies. "Orient" echoes Boyd's OODA without being captured by it. Strong keep.

  *substance total (R1 + R2):* 10.70

**Candidate: `The adaptive pentad`**
- *R1 synthetic:* **+1** — n=2, mean=1.00, weights=[+1, +1], categories={name-unnamed:2}
  > Provides a single memorable noun for the 5-phase cycle (Prolepsis, Aisthesis, Aporia, Epistrophe, Praxis) as a complete unit. The five-phase cycle (prolepsis → aisthesis → aporia → epistrophe → praxis) has a piecewise name per phase but no *collective* noun.

- *R2 votes:*
  - **opus-r2b** (opus): +1 *name-unnamed* — novelty=0.80, len=264, **subst=0.90**
    > Useful collective noun for the 5-phase cycle if a collective handle is needed. The phases do form an ordered sequence; "the adaptive pentad" is a memorable name for *the sequence as a thing*. Worth having, but as a separate target — not a rename of orient cascade.
  - **sonnet-r2c** (sonnet): +1 *add-alias* — novelty=0.61, len=242, **subst=0.81**
    > Good: single memorable noun for the five-phase cycle as a unit (prolepsis, aisthesis, aporia, epistrophe, praxis). Distinct from "orient cascade" (which is the Section II expansion of epistrophe specifically). Both useful at different levels.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.87, len=161, **subst=-0.94**
    > Different target. As a candidate for *naming the five-phase cycle as a unit* it's a reasonable proposal; it should not be voted on within the orient-cascade row.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.86, len=139, **subst=-0.93**
    > Same: the 5-phase cycle as a whole. The orient cascade is the multi-step expansion of Epistrophe for actuated agents — not the whole cycle.

  *substance total (R1 + R2):* 0.84

**Candidate: `The pentad`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={name-unnamed:1}
  > Agree with original. Low priority. Names the five-phase sequence as a unit.

- *R2 votes:*
  - **opus-r2b** (opus): +1 *name-unnamed* — novelty=1.00, len=229, **subst=1.00**
    > Shorter form of the same concept. Pairs well in cycle-walk discussion: "the pentad is one cycle of agent activity." Same caveat: this is a *different naming target* from "orient cascade"; the row's framing conflates two concepts.
  - **sonnet-r2c** (sonnet): +1 *add-alias* — novelty=0.90, len=209, **subst=0.95**
    > Good collective noun for the five phases as a unit. But "orient cascade" names the Section II specific expansion (M_t → Σ_t → O_t), while "the pentad" would name all five phases. Different scopes. Both useful.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.76, len=149, **subst=-0.88**
    > Different target: this names the five-phase cycle as a collective unit, which is not what the orient-cascade row is for. Should be a separate target.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.95, len=119, **subst=-0.98**
    > Renames the whole 5-phase cycle (which already has no canonical single-word name), not the orient cascade specifically.

  *substance total (R1 + R2):* 0.09

**Candidate: `Adaptive cycle`**
- *R1 synthetic:* **+1** [excavated] — n=1, mean=3.00, weights=[+3], categories={canonicalize:1}
  > The generic term for the Prolepsis-Praxis loop.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +1 *add-alias* — novelty=0.55, len=93, **subst=0.72**
    > Good generic term for the full Prolepsis-Praxis loop. Distinct concept from "orient cascade."
  - **opus-r2b** (opus): -1 *rename* — novelty=0.96, len=300, **subst=-0.98**
    > This is a *different concept* — the adaptive cycle is the loop traversal as a whole; orient cascade is the resolution order *within* the corrective phase. The candidate is a category error. The framework already uses "adaptive cycle" elsewhere as the cycle-as-a-whole; this is row-mixing in the card.
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=251, **subst=-1.00**
    > This row's target is the *orient cascade* (M_t→Σ_t→O_t resolution within epistrophe), not the five-phase cycle as a whole. "Adaptive cycle" is a *different* concept and would collide. The candidate set seems to conflate two things — see process-notes.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.84, len=277, **subst=-0.92**
    > Too generic — this is the term for the whole 5-phase cycle (Prolepsis, Aisthesis, Aporia, Epistrophe, Praxis). The orient cascade names a SPECIFIC PART of the cycle (the Epistrophe step expanded for actuated agents). Conflating the two would eliminate an important distinction.

  *substance total (R1 + R2):* -1.18

**Candidate: `Adaptive cycle phase`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > Collectivizes Prolepsis, Aisthesis, Aporia, Epistrophe, and Praxis.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=1.00, len=70, **subst=-0.70**
    > Different concept (the cycle phases). Already keep-decided in row 134.
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=76, **subst=-0.76**
    > Different target (collective name for cycle phases, not the orient cascade).
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.94, len=131, **subst=-0.97**
    > Same problem — "orient cascade" is the expansion of the Epistrophe phase, not a synonym for the whole cycle or for a generic phase.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=1.00, len=60, **subst=-0.60**
    > Generic; doesn't name the Section II expansion specifically.

  *substance total (R1 + R2):* -2.03

**Candidate: `Five adaptive cycle phase`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > Collective grouping.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=1.00, len=127, **subst=-1.00**
    > Different concept; row-mixing. The five cycle phases (prolepsis-aisthesis-aporia-epistrophe-praxis) are not the orient cascade.
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=37, **subst=-0.37**
    > Different target; clunky in any case.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=1.00, len=122, **subst=-1.00**
    > Clunky and wrong (the cascade doesn't name five phases of the cycle; it names the multi-step resolution within one phase).
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=1.00, len=117, **subst=-1.00**
    > "Five adaptive cycle phase" is a description, not a name. Loses the cascade geometry that's the mathematical content.

  *substance total (R1 + R2):* -2.37

**Candidate: `The pentad five phase cycle`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={name-unnamed:1}
  > Probably not worth effort. Worth surfacing.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *name-unnamed* — novelty=1.00, len=114, **subst=-1.00**
    > Different concept — the five-phase cycle as a collective. "Pentad" is OK; "five phase" is redundant with "pentad."
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=35, **subst=-0.35**
    > Different target; awkward compound.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=1.00, len=61, **subst=-0.61**
    > Excessive length; same confusion with the whole-cycle naming.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=1.00, len=75, **subst=-0.75**
    > Verbose; "the adaptive pentad" is cleaner if the collective noun is needed.

  *substance total (R1 + R2):* -2.71

**Candidate: `The five turn`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={name-unnamed:1}
  > Rejection argument: considered as a more Germanic / industrial alternative to "pentad." Reject: loses the Greek-vocabulary register and gains nothing.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.57, len=54, **subst=-0.42**
    > Loses the Greek-vocabulary register and gains nothing.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.88, len=44, **subst=-0.41**
    > Different target; breaks the Greek register.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.60, len=56, **subst=-0.45**
    > Loses Greek vocabulary register as noted; gains nothing.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.69, len=56, **subst=-0.47**
    > Correctly rejected. Loses Greek register, gains nothing.

  *substance total (R1 + R2):* -2.76

**Candidate: `Adaptive traversal`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={name-unnamed:1}
  > "The cycle-as-a-whole" is clunky. "Adaptive traversal" suggests moving through the loop.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.89, len=253, **subst=-0.94**
    > "Traversal" is generic and loses the load-bearing "cascade = forced sequential resolution by information dependency" structure. The orient cascade is *not* arbitrary motion through the loop; it's a specific resolution order that follows from dependency.
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=17, **subst=-0.17**
    > Different target.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.95, len=132, **subst=-0.98**
    > "Traversal" is graph-traversal vocabulary that doesn't carry the forced-ordering / information-dependency sense that "cascade" does.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.85, len=153, **subst=-0.92**
    > "Traversal" implies moving through a graph structure; "cascade" is the correct mathematical metaphor for sequential resolution by information dependency.

  *substance total (R1 + R2):* -3.01


---

### `Pearl causal hierarchy`

*First-encounter locality:* `#def-pearl-causal-hierarchy` (Section I; depends on `#post-causal-structure`, `#scope-agency`). First formal definition; Three levels of causal reasoning emerge from the causal structure of the feedback loop: association ("what if I observe?"), intervention ("what if I do?"), and counterfactual ("what if I had done….

*Segment:* [`01-aad-core/src/def-pearl-causal-hierarchy.md`](../../01-aad-core/src/def-pearl-causal-hierarchy.md)

*R2 voters:* 5 (4 architectures: codex, gemini, opus, sonnet)

**Candidate: `Pearl causal hierarchy`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=9, mean=2.60, weights=[+3, +3, +3, +3, +3, +3, -1, +3, +3, +3], categories={keep:9, canonicalize:1}
  > Adopted directly from Pearl with proper attribution. The case for keeping is the prior-art-integration convention: adopted external concepts retain attribution; renaming would lose provenance and create NIH-syndrome alternatives. The proper-noun form ('Pearl's causal hierarchy') is the field-standard name. Distinguishes Pearl's L0/L1/L2 hierarchy cleanly from AAD's *internal* correlation hierarchy and convention hierarchy, both of which the framework owns separately.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *keep* — novelty=0.75, len=142, **subst=1.75**
    > Adopted prior-art term should retain attribution. This also disambiguates Pearl's hierarchy from AAD's correlation and convention hierarchies.
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.86, len=159, **subst=1.86**
    > Direct adoption from prior art. Removing "Pearl" would be NIH syndrome and lose the precise external mathematical definition. Baggage-adoption is correct here.
  - **opus-r2b** (opus): +2 ★ *keep* — novelty=0.70, len=459, **subst=1.70**
    > Defended keep on prior-art-integration grounds (CLAUDE.md §"Prior art integration": "adopt external concepts directly with citation and original names"). Dropping the Pearl attribution would invite NIH-syndrome alternatives and lose the specific Pearl 2009 / Bareinboim 2022 provenance the segment cites. The proper-noun form is the field-standard name; using it cleanly indexes back into a 20-year body of causal-inference literature without translation tax.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.64, len=407, **subst=1.64**
    > Adopted-with-attribution per the framework's prior-art integration convention. The proper-noun form preserves provenance and avoids NIH-syndrome rename. Disambiguates against AAD's *internal* correlation hierarchy and convention hierarchy, both owned by the project. The current usage in the segment is faithful to Pearl's hierarchy theorem; renaming would damage the connection to the canonical literature.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.63, len=435, **subst=1.63**
    > Confirmed across multiple segments (def-causal-information-yield, der-loop-interventional-access, def-strategy-dag). Prior-art integration principle: adopted external concepts retain attribution. "Pearl's causal hierarchy" is the field-standard name. Crucially: distinguishes Pearl's L0/L1/L2 from AAD's own correlation hierarchy (L0/L1/L1'/L2) and convention hierarchy (C1/C2/C3). Dropping "Pearl" would create collision. Strong keep.

  *substance total (R1 + R2):* 10.58

**Candidate: `Causal hierarchy level`**
- *R1 synthetic:* **+1** [invented] — n=1, mean=3.00, weights=[+3], categories={canonicalize:1}
  > Standardizing Pearl's nomenclature within AAD.

- *R2 votes:*
  - **codex-r2b** (codex): +1 *canonicalize* — novelty=1.00, len=92, **subst=0.92**
    > Useful phrase for individual L1/L2/L3 entries, but not a replacement for the hierarchy name.
  - **opus-r2b** (opus): -1 *rename* — novelty=0.89, len=272, **subst=-0.94**
    > Generic; loses Pearl attribution. Removing the "Pearl" prefix invites confusion with AAD's *own* hierarchies (correlation hierarchy at #def-strategy-dag; convention hierarchy at #def-value-object). Three distinct hierarchies in one framework — disambiguation is essential.
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=128, **subst=-1.00**
    > "Level" repeats the L1/L2/L3 naming; the *hierarchy* is the three-level structure. Combining "hierarchy" + "level" is redundant.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=1.00, len=67, **subst=-0.67**
    > "Level" is a per-level suffix, not a name for the hierarchy itself.

  *substance total (R1 + R2):* -0.69

**Candidate: `Causal hierarchy`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Dropping "Pearl" removes the specific historical baggage while keeping the structural concept.

- *R2 votes:*
  - **codex-r2b** (codex): +1 *add-alias* — novelty=1.00, len=118, **subst=1.00**
    > Acceptable shorthand after first attribution, but not as the canonical name because AAD also has internal hierarchies.
  - **opus-r2b** (opus): -1 *rename* — novelty=0.89, len=214, **subst=-0.94**
    > Same disambiguation problem as "Causal hierarchy level": the framework has multiple hierarchies. Dropping "Pearl" undersells the specific causal-inference machinery being adopted and creates NIH-flavored ambiguity.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.97, len=241, **subst=-0.98**
    > Drops the Pearl attribution that the prior-art-integration convention recommends preserving. Bare "causal hierarchy" also collides loosely with various other "causal hierarchies" in the literature; the proper-noun form is what disambiguates.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.92, len=179, **subst=-0.96**
    > Dropping "Pearl" would lose provenance AND create collision with "correlation hierarchy" (AAD's own internal hierarchy for strategy DAG). The disambiguation requires Pearl's name.

  *substance total (R1 + R2):* -1.89


---

### `Pearl L1`

*R2 voters:* 2 (2 architectures: codex, opus)

**Candidate: `Predicting`** ▸ leader
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={add-alias:1}
  > Brief-grade agent-side gloss for Pearl's L1 (associational). NOT a rename — keep Pearl's formal term; add the agent-action gloss for prose.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *add-alias* — novelty=0.77, len=141, **subst=1.77**
    > Good brief-grade gloss for Pearl L1/associational access: pattern recognition over prior observations and actions to predict what comes next.
  - **opus-r2c** (opus): +1 ★ *add-alias* — novelty=0.66, len=397, **subst=0.83**
    > Useful brief-grade agent-side gloss for L1 = associational. Pairs cleanly with Level-2-as-intervening, Level-3-as-imagining-alternatives. Don't rename Pearl's formal term; add the agent-side gloss for plain-language exposition. The convention helps Brief fields and pedagogical contexts where the reader needs the *agent-action* (predict/intervene/counterfactualize), not just the formal taxonomy.

  *substance total (R1 + R2):* 2.60


---

### `per dimension persistence`

*First-encounter locality:* `#result-per-dimension-persistence` (Section III; depends on `#result-persistence-condition`, `#def-adaptive-tempo`, `#deriv-sector-condition`). First formal result; The scalar persistence condition overestimates adaptive capacity when the agent's correction gain varies across dimensions.

*Segment:* [`01-aad-core/src/result-per-dimension-persistence.md`](../../01-aad-core/src/result-per-dimension-persistence.md)

*R2 voters:* 2 (2 architectures: gemini, sonnet)

**Candidate: `Weakest link persistence`** ▸ leader
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Current slug is descriptive but inert; the actual content is "the persistence condition binds at the weakest dimension." "Weakest link" makes the engineering intuition land in one read. Modest preference.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *rename* — novelty=0.92, len=246, **subst=1.92**
    > The adversarial audit of this segment revealed that the theorem depends on a conjunctive (L-infinity) failure boundary. 'Weakest link' bakes this exact mathematical geometry into the name, making it vastly superior to the generic 'per dimension'.
  - **sonnet-r2b** (sonnet): +1 *rename* — novelty=0.91, len=218, **subst=0.96**
    > "Weakest" is more precise than "weak" — it names the specific dimensionally-worst element. But slightly awkward in flow ("the system faces a weakest link persistence constraint"). "Weak link" is idiomatically smoother.

  *substance total (R1 + R2):* 2.88

**Candidate: `Dimensional persistence`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > Better adjective form for prose flow.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +1 *rename* — novelty=1.00, len=199, **subst=1.00**
    > More grammatically flexible than "per-dimension" but loses the bottleneck connotation. "Dimensional persistence" is neutral where the concept is not — the point is that the WORST dimension dominates.

  *substance total (R1 + R2):* 2.00

**Candidate: `Weak link persistence`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Weak link" captures the bottleneck nature better than "per-dimension".

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +2 ★ *rename* — novelty=0.81, len=356, **subst=1.81**
    > The weak-dimension-as-bottleneck result is the core insight: 84% of mismatch concentrates in the weak dimension. "Weak link" names this binding constraint perfectly. In prose: "the system faces a weak link persistence problem" reads better than "per-dimension persistence." Survives the communal-imagination test — everyone knows the weakest link metaphor.

  *substance total (R1 + R2):* 1.81

**Candidate: `per dimension persistence`**
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=3, mean=1.67, weights=[+1, +2, +2], categories={canonicalize:3}
  > Weak dimension is bottleneck. Acceptable keep. Precise — the bottleneck-dimension persistence condition.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *keep* — novelty=0.92, len=199, **subst=-0.96**
    > Accurate but inert. "Per-dimension" describes the methodology (checking each dimension separately) rather than the insight (the worst dimension dominates). The "weak link" framing is strictly better.

  *substance total (R1 + R2):* 0.04


---

### `persistence condition`

*First-encounter locality:* `#result-persistence-condition` (Section I; depends on `#def-adaptive-tempo`, `#def-mismatch-signal`, `#result-sector-condition-stability` (+1 more)). First formal result; An agent persists when two independent conditions hold: the correction machinery can contain mismatch within its operating region (*structural persistence*), and the resulting steady-state mismatch is….

*Segment:* [`01-aad-core/src/result-persistence-condition.md`](../../01-aad-core/src/result-persistence-condition.md)

*R2 voters:* 3 (3 architectures: gemini, opus, sonnet)

**Candidate: `persistence condition`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=11, mean=3.00, weights=[+3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3], categories={canonicalize:12, rename:1}
  > The framework's central inequality ($\alpha R \gt \rho$). Defenders cite three reasons to keep: it is canonical across adjacent fields (Lyapunov stability, RL viability, organizational persistence, software maintenance) so the baggage transfers; it is referenced throughout the codebase, making a rename expensive in editorial work; and the segment carries the canonical bathtub gloss in its Findings section, which is built on this name. Occasional paraphrases ('persistence criterion', 'adaptive persistence condition', 'the alpha-greater-than-rho-over-R condition') need standardizing on this canonical form.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.90, len=199, **subst=1.90**
    > This is the central inequality of the framework. 'Persistence' correctly names the structural survival against decay (vs 'stability' which often just means converging to a point). Keep exactly as is.
  - **opus-r2c** (opus): +2 ★ *canonicalize* — novelty=0.86, len=313, **subst=1.86**
    > Canonicalize over the residual paraphrases ("persistence criterion", "adaptive persistence condition", "the α>ρ/R condition"). The canonical form is right; paraphrase drift is the issue. The cross-domain readability — same inequality across Kalman / RL / orgs / SW — depends on a single phrase being recognizable.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.74, len=359, **subst=1.74**
    > Confirmed by segment as the framework's central inequality. Three-reason argument stands: canonical across adjacent fields; already throughout codebase; the bathtub gloss is built on this name. The two-condition decomposition (structural/task-adequacy) is the AAD contribution; the name "persistence condition" is correct for the combined result. Strong keep.

  *substance total (R1 + R2):* 7.50

**Candidate: `Survival equation`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={add-alias:1}
  > Useful elevator-pitch phrase, but too slogan-like for canonical theorem prose.

- *R2 votes:*
  - **opus-r2c** (opus): +1 *add-alias* — novelty=0.95, len=357, **subst=0.97**
    > Could work as an *informal* alias for elevator-pitch contexts (README, intro material, bathtub-gloss companion phrasing). Not as a rename: "survival equation" oversells (it's a condition, not a derived equation) and overlaps with too many adjacent uses (survival analysis, survival functions). As a parallel handle in pedagogy specifically, it's defensible.
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=1.00, len=54, **subst=0.54**
    > Same as above — good alias but wrong for primary name.

  *substance total (R1 + R2):* 1.51

**Candidate: `The survival equation`**
- *R1 synthetic:* **+1** — n=1, mean=3.00, weights=[+3], categories={rename:1}
  > The simplest possible elevator pitch for Adaptation Dynamics.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.91, len=209, **subst=0.96**
    > Vivid elevator pitch. But "survival" imports evolutionary connotations that the segment explicitly avoids. The segment uses "persist" throughout. Good alias for popularization, not for canonical theorem prose.
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=94, **subst=-0.94**
    > Same critique without the alias-register option; the bare phrase as canonical name overclaims.

  *substance total (R1 + R2):* 1.02


---

### `postulate not axiom`

*R2 voters:* 2 (2 architectures: codex, opus)

**Candidate: `Postulate`** ▸ leader
- *R1 synthetic:* **+1** [excavated] — n=2, mean=3.00, weights=[+3, +3], categories={canonicalize:1, rename:1}
  > Standard philosophical boundary definition. Keep.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *keep* — novelty=1.00, len=99, **subst=1.98**
    > Correct label for foundational commitments without pretending they have axiom-level formal closure.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=1.00, len=498, **subst=2.00**
    > The framework's terminology choice (postulate / result / derivation rather than axiom / theorem / proof) is doing meta-honesty work: AAD is a research framework using existing mathematics, not a foundational mathematical-originality project. "Postulate" is the right word for things that are *taken as given as foundations* without claiming they're foundational discoveries; "axiom" carries pretensions AAD doesn't have. The terminology choice is load-bearing for the framework's epistemic posture.

  *substance total (R1 + R2):* 4.98


---

### `prolepsis`

*R2 voters:* 2 (2 architectures: gemini, opus)

**Candidate: `prolepsis`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=3, mean=2.33, weights=[+3, +2, +2], categories={canonicalize:3}
  > Earns its foreignness because "anticipation" would flatten the active-modeling point. Good phase term for anticipation. `LEXICON.md` defines it as "the model's active anticipation: $\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$." The Greek term carries the active-modeling sense (πρόληψις = "taking-before") that "anticipation" or "prediction" both miss.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.88, len=226, **subst=1.88**
    > The Greek register (prolepsis/aisthesis/aporia/epistrophe/praxis) elevates the framework from mechanical control theory to cognitive philosophy. 'Anticipation' flattens the active-modeling implication of 'taking-before'. Keep.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.83, len=242, **subst=1.83**
    > The active-modeling sense is what makes the proleptic-prediction-then-aporia structure work. "The model produced $\hat o_t$" is generative; "the model anticipated" reads as discrimination/recognition, which is a different cognitive operation.

  *substance total (R1 + R2):* 5.71

**Candidate: `Prolepsis anticipatory projection`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={add-alias:1}
  > Adding English aliases assists non-specialists while retaining the precision of the Greek terms.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=17, **subst=-0.17**
    > Compound dilutes.

  *substance total (R1 + R2):* 0.83

**Candidate: `Anticipation`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: considered and rejected. Loses the "active model produces an expectation that the world then refutes" dynamic that the cycle uses. "Anticipation" reads as passive forecast; the segment's formalism is generative. The Greek earns its foreignness here, exactly as codex argued.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.79, len=230, **subst=-0.90**
    > "Anticipation" reads as passive forecasting; prolepsis carries the active-generative sense (the model *constructs* an expectation that reality will then refute or confirm). The cycle is generative, so the phase name should be too.

  *substance total (R1 + R2):* -1.90


---

### `satisfaction gap`

*First-encounter locality:* `#def-satisfaction-gap` (Section II; depends on `#def-value-object`, `#form-objective-functional`). First formal definition; The satisfaction gap measures the distance between what the objective requires and what the best available one-step policy improvement can deliver, under the current model and horizon.

*Segment:* [`01-aad-core/src/def-satisfaction-gap.md`](../../01-aad-core/src/def-satisfaction-gap.md)

*R2 voters:* 5 (3 architectures: gemini, opus, sonnet)

**Candidate: `satisfaction gap`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=16, mean=3.00, weights=[+3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +3], categories={canonicalize:19, add-alias:2}
  > One half of the two-name 2×2 diagnostic with control regret; defenders describe it as the crispest named pair in the project. The argument is that the two-word compound tells the reader the diagnostic direction (objective met vs. unmet) immediately, so the disambiguation table organizes itself in the reader's head on first encounter. Renaming would lose a load-bearing prose convention installed across NOTATION.md, LEXICON.md, and the segment Brief. Occasional paraphrases ('objective gap', 'attainability gap') exist; the canonical name is established and absorbing them is what canonicalization does.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.95, len=152, **subst=1.95**
    > The prose use of 'gap' pairs beautifully with 'regret' later. It correctly implies a distance to a threshold rather than just a continuous error signal.
  - **opus-r2b** (opus): +2 ★ *keep* — novelty=0.66, len=460, **subst=1.66**
    > The crispest named pair in the project, with control regret. The naming-principles file uses this pair as its canonical illustration of "names that do work for the reader." The segment's 2×2 table organizes itself in the reader's head on first encounter precisely because the two axis-names are evocatively *and* accurately chosen. Renaming would forfeit the prose convention installed across NOTATION / LEXICON / segment Briefs and break the matched compound.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.67, len=546, **subst=1.67**
    > The README itself uses this and control-regret as the canonical example of names that work — names whose 2×2 organizes itself in the reader's head on first encounter. The pair is among the project's strongest naming wins. Renaming either half would force re-explaining the diagnostic on every encounter for a generation of citations. The canonical name is also established across NOTATION, LEXICON, and segment Briefs; the residual paraphrases ("objective gap", "attainability gap") should be canonicalized to this form, not the other way around.
  - **sonnet-r2b** (sonnet): +2 ★ *keep* — novelty=0.79, len=437, **subst=1.79**
    > The paired name (satisfaction gap / control regret) carries the full 2×2 diagnostic system. "Satisfaction" points to V_O_min (the satisfaction threshold) — the agent's measure of "objective met." "Gap" names the distance to that threshold. Together with "control regret," the two-word pair is the project's clearest example of names that do work for the reader. Canonicalize and absorb paraphrases ("objective gap," "attainability gap").
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.81, len=205, **subst=1.81**
    > The crispest named pair in the project. "Satisfaction gap" and "control regret" work together because each half carries precise diagnostic direction. Renaming either half damages the compound. Strong keep.

  *substance total (R1 + R2):* 10.88

**Candidate: `Attainability shortfall`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: "Satisfaction gap" explicitly ties into $V_O^{\min}$ being met. "Attainability" might refer only to $A_O$.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.81, len=359, **subst=-0.90**
    > "Attainability" refers narrowly to $A_O$ (the supremum); "satisfaction gap" refers to the gap between the threshold $V_{O_t}^{\min}$ and that supremum. The names are not synonymous — "attainability shortfall" would lose the threshold-relative framing. The segment's Formal Expression is explicit: $\delta_{\text{sat}} = V_{O_t}^{\min} - A_O$, not just $-A_O$.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.97, len=301, **subst=-0.98**
    > "Attainability" reaches for the wrong dimension — the diagnostic is about whether the *world permits* the objective, not whether the agent can attain it. The 2×2 with control-regret depends on the orthogonality being clean: world-permits vs you-execute. "Attainability" muddies the world-permits axis.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.77, len=319, **subst=-0.88**
    > Focuses on the A_O component, not on the V_O_min threshold being unmet. The gap is between the threshold and the attainability — "satisfaction gap" captures the distance from the satisfaction threshold (V_O_min), not just the attainability. "Shortfall" also doesn't form a natural pair with "regret" the way "gap" does.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=1.00, len=123, **subst=-1.00**
    > Loses the paired relationship with "control regret." The pair works because each half names a clean axis of the diagnostic.

  *substance total (R1 + R2):* -4.77


---

### `Section I. Adaptive Systems Under Uncertainty`

*R2 voters:* 2 (2 architectures: codex, gemini)

**Candidate: `I adaptive system under uncertainty`** ▸ leader
- *R1 synthetic:* **+1** [invented] — n=1, mean=3.00, weights=[+3], categories={canonicalize:1}
  > The section name is accurate and positions Section I correctly. "Under Uncertainty" is load-bearing — it distinguishes adaptive systems from optimal-control-over-known-dynamics, which is explicitly out of scope. Keep.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.73, len=150, **subst=1.73**
    > The phrase 'Under Uncertainty' is the load-bearing part of the title. It distinguishes the framework's scope from classical control over known plants.
  - **codex-r2b** (codex): +1 *keep* — novelty=0.97, len=124, **subst=0.98**
    > Points at the right content, but singular/lowercase reads like a normalized artifact rather than the actual section heading.

  *substance total (R1 + R2):* 3.71

**Candidate: `Adaptive Systems Under Uncertainty`**
- *R1 synthetic:* — (no R1 evidence)

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *keep* — novelty=1.00, len=153, **subst=2.00**
    > The defining scope segment makes "under uncertainty" load-bearing: $\mathcal O \neq \emptyset$ and residual uncertainty are the whole Section I boundary.

  *substance total (R1 + R2):* 2.00

**Candidate: `Section I adaptive system under uncertainty`**
- *R1 synthetic:* **+1** [invented] — n=1, mean=3.00, weights=[+3], categories={canonicalize:1}
  > Standard section heading formatting.

- *R2 votes:*
  - **codex-r2b** (codex): +1 *keep* — novelty=0.93, len=113, **subst=0.96**
    > Acceptable as a mechanical reference form, but the reader-facing heading should keep the plural and title casing.

  *substance total (R1 + R2):* 1.96


---

### `sector condition`

*First-encounter locality:* `#deriv-sector-condition` (Appendix A; depends on `#def-adaptive-tempo`, `#def-mismatch-signal`). First formal derivation; Complete Lyapunov derivations of bounded mismatch and adaptive reserve for the sector-condition results stated in #result-sector-condition-stability.

*Segment:* [`01-aad-core/src/deriv-sector-condition.md`](../../01-aad-core/src/deriv-sector-condition.md)

*R2 voters:* 2 (2 architectures: opus, sonnet)

**Candidate: `sector condition`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=6, mean=2.83, weights=[+3, +3, +3, +2, +3, +3], categories={canonicalize:5, rename:1}
  > Adopted from nonlinear control (Khalil, Vidyasagar); baggage correct and load-bearing. Adopted from Khalil / Vidyasagar nonlinear control; baggage is correct. Sometimes appears as "sector constraint" or "sector bound" or "sector-condition assumption." Standardize on "sector condition" (the nonlinear correction guarantee).

- *R2 votes:*
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.80, len=402, **subst=1.80**
    > Adopted-with-correct-baggage from Khalil/Vidyasagar nonlinear control. The technical content matches the AAD usage, and a control engineer reading "sector condition" knows what to expect within the relevant tolerance. The principles file's first criterion ("baggage-adoption wins when the prior art's structural intuitions should travel with the name") fires here: the prior intuitions *should* travel.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.85, len=188, **subst=1.85**
    > Strong keep. The term correctly imports control-theory baggage (the correction function lives in a sector), the Lyapunov analysis requires exactly this assumption, and the name is precise.

  *substance total (R1 + R2):* 5.65

**Candidate: `Continuous sector condition`**
- *R1 synthetic:* **+1** [excavated] — n=1, mean=3.00, weights=[+3], categories={canonicalize:1}
  > Refines the specific GA3 assumption.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +1 *keep* — novelty=0.85, len=132, **subst=0.92**
    > Acceptable for the specific GA3 continuous-time version; marks the derivation as the continuous counterpart to the discrete variant.
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=212, **subst=-1.00**
    > Adds a qualifier that doesn't disambiguate against any actually-competing usage. The continuous/discrete split is real but is handled by the discrete-sector-condition segment, not by qualifying the umbrella name.

  *substance total (R1 + R2):* 0.92

**Candidate: `sector condition derivation`**
- *R1 synthetic:* **0** [excavated] — n=1, mean=1.00, weights=[+1], categories={canonicalize:1}
  > Lyapunov derivations for bounded mismatch and adaptive reserve. Self-descriptive. Keep.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +1 *keep* — novelty=0.88, len=85, **subst=0.80**
    > Acceptable slug-level name for the derivation segment specifically; self-descriptive.
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=155, **subst=-1.00**
    > "Derivation" is the segment type; the slug already encodes that mechanically (deriv-sector-condition). Putting "derivation" in the prose name is redundant.

  *substance total (R1 + R2):* -0.20

**Candidate: `Correction sector`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Preserves the geometric intuition if "sector" must be kept.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.96, len=249, **subst=-0.98**
    > Loses the established Khalil/Vidyasagar baggage and gains nothing — "correction sector" reads as a coinage where "sector condition" reads as a connection to existing nonlinear-control vocabulary. The baggage is correct here, so adopting it is right.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.92, len=89, **subst=-0.86**
    > Grammar reversal; the noun phrase "sector condition" is smoother and already established.

  *substance total (R1 + R2):* -1.84

**Candidate: `Persistence condition`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Sector condition" carries heavy nonlinear-systems baggage. "Persistence condition" describes its function in AAD.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.88, len=216, **subst=-0.94**
    > This collides with the headline #result-persistence-condition (a different segment). Sector condition is the precondition for persistence; making them the same name flattens the structural distinction. Strong reject.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.84, len=381, **subst=-0.92**
    > "Persistence condition" is the result (α > ρ/R) not the structural assumption. "Sector condition" names the assumption on the correction function (that it lies in a sector). These are different things; conflating them would damage the framework's precision. The nonlinear-control baggage here is correct and load-bearing — the Khalil/Vidyasagar sector is exactly the right concept.

  *substance total (R1 + R2):* -1.86


---

### `separability pattern`

*First-encounter locality:* `#disc-separability-pattern` (Appendix A; deep dependency cone (8 upstream segments incl. `#def-strategy-dag`, `#def-value-object`)). Meta-discussion segment; AAD consistently runs a three-part epistemic posture across state spaces that admit no tractable exact treatment in general: name the **separable core** where identification is clean, name the….

*Segment:* [`01-aad-core/src/disc-separability-pattern.md`](../../01-aad-core/src/disc-separability-pattern.md)

*R2 voters:* 3 (2 architectures: gemini, opus)

**Candidate: `Separability ladder`** ▸ leader
- *R1 synthetic:* **+2** [invented] — n=10, mean=2.20, weights=[+1, +3, +1, +3, +3, +3, +3, +2, +1, +2], categories={rename:9, canonicalize:1}
  > The case rests on the segment's own organizing structure: the meta-segment is a seven-row *ladder* (separable-core / structured-repair / general-open across seven axes of increasing difficulty), and the Brief, Discussion, and cross-citations all reach for 'ladder' or 'rungs' as the unit. 'Pattern' is generic filler that describes no specific structure; 'ladder' is the geometry the content actually has. Pairs mnemonically with #identifiability-floor ('the ladder above the floor'). Counter-argument from one defender: the rename would churn cross-references, but the segment itself already says 'six ladders' in prose, so the slug is lagging the prose. 'Staircase' was considered and rejected as whimsical without a precision gain — staircases are uniform, ladders intuitively get harder toward the top.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *rename* — novelty=0.66, len=326, **subst=1.66**
    > The segment itself refers to 'six ladders' in the prose, and the structure (Separable Core / Structured Repair / General Open) is a progression of increasing difficulty. 'Ladder' is the geometry of the content; 'pattern' is a generic filler. It also pairs perfectly with 'identifiability floor' ('the ladder above the floor').
  - **opus-r2b** (opus): +2 ★ *rename* — novelty=0.75, len=540, **subst=1.75**
    > The segment is *already* prose-using "ladder" repeatedly: "Six ladders," "the seventh ladder," "Cross-ladder monotonicity." Both Discussion sections, the table headers, and the cross-references reach for "ladder" or "rungs." This is the canonicalize-with-organic-provenance case the principles file describes verbatim — promote the phrase already present in prose to formal naming. The geometry the content actually has is a ladder; the slug should match. Pairs mnemonically with `#disc-identifiability-floor`: "the ladder above the floor."
  - **opus-r2c** (opus): +2 ★ *rename* — novelty=0.63, len=495, **subst=1.63**
    > The segment's own structure is a *ladder* — seven rows of increasing difficulty (separable-core / structured-repair / general-open across seven axes). The segment text already reaches for "ladder" / "rungs" as the unit; the slug is lagging the prose. Pairs mnemonically with #identifiability-floor as "the ladder above the floor." Crucially, "ladder" carries the increasing-difficulty semantics that "pattern" doesn't: each rung is harder than the one below, which *is* the meta-segment's claim.

  *substance total (R1 + R2):* 7.04

**Candidate: `separability pattern`**
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=4, mean=2.50, weights=[+1, +3, +3, +3], categories={canonicalize:4}
  > Slightly clinical, but honest about what the segment is doing across multiple ladders. Strong meta-segment name: short, teachable, and faithful to the repeated posture. Load-bearing meta-segment name with evocative three-part structure (separable core / structured repair / general open).

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.88, len=337, **subst=-0.94**
    > Slightly clinical, but the load-bearing objection is that the segment itself uses "ladder" repeatedly — "Six ladders in the current theory," "the seventh ladder," "Cross-ladder monotonicity." The slug "pattern" is lagging the prose. The canonicalize-with-organic-provenance discipline says: when prose has converged on a phrase, lift it.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.91, len=310, **subst=-0.96**
    > "Pattern" is generic filler — every meta-segment is technically about a pattern. The segment's actual content is a *ladder* of separability across seven axes; "pattern" hides that structure. A meta-segment whose specificity is its ladder-of-difficulty shouldn't carry a name that suggests amorphous similarity.

  *substance total (R1 + R2):* 0.10

**Candidate: `Tiered separability`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: verbose.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.89, len=48, **subst=-0.45**
    > Verbose; "tiered" adds nothing "ladder" doesn't.
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=80, **subst=-0.80**
    > "Tiered" is right but "separability ladder" is more memorable and less clinical.

  *substance total (R1 + R2):* -2.25

**Candidate: `Separability staircase`**
- *R1 synthetic:* **-1** — n=5, mean=-1.00, weights=[-1, -1, -1, -1, -1], categories={rename:5}
  > Considered as a more whimsical alternative to 'ladder'. The argument against: 'staircase' doesn't carry the increasing-difficulty semantics as cleanly — staircases are uniform; ladders intuitively get harder toward the top. Whimsical without a compensating precision gain.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.97, len=59, **subst=-0.58**
    > Same staircase objection as the bare "Staircase" candidate.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.69, len=209, **subst=-0.84**
    > Per the principles file's own rejection: "staircase" is whimsical without a precision gain. Staircases are uniform; ladders carry the increasing-difficulty intuition. The whimsical-without-payoff failure mode.

  *substance total (R1 + R2):* -2.42

**Candidate: `Separable core`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: considered and rejected — names only the first column of the three-part shape; loses the structured-repair and general-open framing that is half the point.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.65, len=158, **subst=-0.83**
    > Names only the first column of the three-column table; loses the "structured repair" middle and "general open" right side that are half the segment's content.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.47, len=107, **subst=-0.74**
    > Names only the first column of the three-part shape. Loses the structured-repair and general-open framings.

  *substance total (R1 + R2):* -2.56

**Candidate: `Staircase`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: too metaphorical.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=1.00, len=230, **subst=-1.00**
    > Whimsical without precision gain. The rungs of the segment's ladders are not uniform (the difficulty *increases*); staircases are uniform. The segment specifically uses "ladder" because it captures increasing-difficulty semantics.
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=80, **subst=-0.80**
    > Same critique as "separability staircase" plus drops the "separability" content.

  *substance total (R1 + R2):* -2.80

**Candidate: `Three rung posture`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: too mechanical; loses "separability" which is the content.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.80, len=125, **subst=-0.90**
    > Mechanical and loses "separability" — the load-bearing word that names the structural-axis along which the regime decomposes.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.86, len=129, **subst=-0.93**
    > Drops "separability" (the content axis) and overspecifies "three" (the segment is across seven ladders, each with three columns).

  *substance total (R1 + R2):* -2.83


---

### `strategic calibration`

*First-encounter locality:* `#def-strategic-calibration` (Section II; depends on `#def-strategy-dag`, `#def-value-object`). First formal definition; The strategic calibration residual measures whether the strategy's causal model is correct: are the edges in $\Sigma_t$ accurate predictors of how much value each step actually produces?.

*Segment:* [`01-aad-core/src/def-strategic-calibration.md`](../../01-aad-core/src/def-strategic-calibration.md)

*R2 voters:* 2 (2 architectures: gemini, sonnet)

**Candidate: `strategic calibration`** ▸ leader
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=6, mean=1.75, weights=[+2, +2, +2, +1, +1, +2, +2, +2], categories={canonicalize:7, add-alias:1}
  > Names the edge-residual aggregate that measures how well the strategy DAG is calibrated. The case for keeping centers on parallel construction with epistemic-calibration from broader literature and on the LEXICON.md prose form. The follow-on alias vote formalizes the symbol+English pair: 'strategic calibration' is the concept-name; the residual aggregate is its measurement. Acceptable but not load-bearing; no strong alternative offered.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.95, len=261, **subst=1.95**
    > 'Calibration' is exactly the right statistical term for checking if predicted edge weights match observed frequencies. It perfectly completes the error-signal vocabulary ($\delta_t$, $\delta_{\text{sat}}$, $\delta_{\text{regret}}$, $\delta_{\text{strategic}}$).
  - **sonnet-r2c** (sonnet): +1 *keep* — novelty=0.84, len=173, **subst=0.92**
    > Acceptable as concept name. "Strategic calibration" is the concept; "strategic calibration residual" is its measurement. Both can coexist but need clear register separation.

  *substance total (R1 + R2):* 3.87

**Candidate: `Strategic calibration residual`**
- *R1 synthetic:* **+1** [excavated] — n=1, mean=2.00, weights=[+2], categories={canonicalize:1}
  > The body of the segment uses both "strategic calibration residual" and "edge residual aggregate" and "δ_strategic." Canonicalize: in prose, "strategic calibration residual" for the aggregated quantity, "edge residual" for per-edge $r_{ij}$, $\delta_{\text{strategic}}$ for the symbol. Stop using "edge residual aggregate" as a third paraphrase.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +2 ★ *canonicalize* — novelty=0.78, len=147, **subst=1.78**
    > Confirmed by segment. The full form for the aggregated L² quantity. Retires "edge residual aggregate" as a third paraphrase. See also row 325 vote.

  *substance total (R1 + R2):* 2.78

**Candidate: `Strategy calibration`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Strategic" is overloaded elsewhere; the shorter noun phrase reads more cleanly.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.96, len=188, **subst=-0.98**
    > Grammatically awkward. "Strategy calibration" reads as "measuring a strategy's precision" rather than "calibrating the strategy DAG's edge predictions." The adjective form is more precise.

  *substance total (R1 + R2):* -0.98


---

### `strategy dimension`

*First-encounter locality:* `#def-strategy-dimension` (Section II; depends on `#form-complete-agent-state`, `#form-objective-functional`). First formal definition; The purposeful substate $G_t$ decomposes into two structurally distinct components: $O_t$ (the objective — what the agent wants) and $\Sigma_t$ (the strategy — the agent's theory of how its actions….

*Segment:* [`01-aad-core/src/def-strategy-dimension.md`](../../01-aad-core/src/def-strategy-dimension.md)

*R2 voters:* 3 (2 architectures: gemini, sonnet)

**Candidate: `Purposeful decomposition`** ▸ leader
- *R1 synthetic:* **+1** — n=2, mean=2.50, weights=[+2, +3], categories={rename:2}
  > "Strategy dimension" doesn't accurately name what the segment defines — it defines the *split* of $G_t$ into $(O_t, \Sigma_t)$, which is a decomposition of the purposeful substate, not a "dimension." "Purposeful-decomposition" or "G-decomposition" reads more accurately. Opus proposed this (+2); I had proposed `def-purposeful-substate` (+2) as my cold-start candidate.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *rename* — novelty=0.72, len=86, **subst=1.48**
    > Accurately names the structural split of the purposeful substate into O_t and Sigma_t.
  - **sonnet-r2b** (sonnet): +2 ★ *rename* — novelty=0.84, len=310, **subst=1.84**
    > Names what the segment does: decomposes the purposeful substate. Parallels "directed separation" (a structural decomposition of update functions). The word "purposeful" connects to "purposeful substate" — the segment decomposes the purposeful substate into O_t and Σ_t. Both components are named, not just one.
  - **sonnet-r2c** (sonnet): +2 *rename* — novelty=0.77, len=262, **subst=1.77**
    > Also good. "Purposeful decomposition" names the G_t = (O_t, Σ_t) split directly and parallels "directed separation" (structural decomposition of update functions). Either "purposeful decomposition" or "strategy decomposition" is better than "strategy dimension."

  *substance total (R1 + R2):* 6.09

**Candidate: `Objective strategy split`**
- *R1 synthetic:* **+1** — n=2, mean=2.00, weights=[+3, +1], categories={rename:2}
  > Dimension is too generic. Acceptable alternative; the proposer prefers purposeful-decomposition because it parallels "directed separation" (a structural decomposition of update functions) and connects to the Section II decomposition lattice.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +1 *rename* — novelty=0.92, len=89, **subst=0.86**
    > Names both components explicitly. Slightly clunky. "Purposeful decomposition" is cleaner.
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.92, len=111, **subst=0.96**
    > Acceptable. Names the two components explicitly. But "split" is informal; "decomposition" is more mathematical.

  *substance total (R1 + R2):* 2.82

**Candidate: `Strategy decomposition`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Dimension" reads as if it's naming a scalar axis; the actual content is the $G_t = (O_t, \Sigma_t)$ **decomposition**. Minor clarity win.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +2 ★ *rename* — novelty=0.87, len=352, **subst=1.87**
    > Confirmed by segment. The segment DOES define the G_t = (O_t, Σ_t) DECOMPOSITION — the split of the purposeful substate into two structurally distinct components. "Strategy decomposition" names this correctly. The word "decomposition" carries the right mathematical meaning (a structured partition into parts). Stronger than "strategy dimension" alone.
  - **sonnet-r2b** (sonnet): +1 *rename* — novelty=0.85, len=133, **subst=0.92**
    > Better than "strategy dimension" — "decomposition" is accurate. Slightly undersells O_t vs Σ_t since "strategy" primarily evokes Σ_t.

  *substance total (R1 + R2):* 2.79

**Candidate: `strategy dimension`**
- *R1 synthetic:* **0** [is_keep] [excavated] — n=3, mean=0.33, weights=[+1, -1, +1], categories={canonicalize:3}
  > Names the $\Sigma_t$ dimension of $G_t = (O_t, \Sigma_t)$. The defense is mild: specialist vocabulary but functional, no obviously better alternative. One vote considered renaming to '#purposeful-substate-split' and rejected it as worse. One concern flagged: 'strategy dimension' undersells $O_t$, the other half of the split, but no better alternative emerged. Weak keep.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +1 *keep* — novelty=0.95, len=111, **subst=0.97**
    > Acceptable but "dimension" undersells the content. The segment defines a decomposition, not a single dimension.
  - **gemini-r2** (gemini): -1 *keep* — novelty=0.84, len=37, **subst=-0.34**
    > Undersells the O_t half of the split.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.82, len=208, **subst=-0.91**
    > Undersells the O_t half of the split — the segment defines the G_t = (O_t, Σ_t) decomposition, not just the Σ_t dimension. Also, "dimension" implies a scalar axis, but the split is a structural decomposition.

  *substance total (R1 + R2):* -0.28

**Candidate: `Purposeful substate`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > "Strategy dimension" undersells the content — this segment defines the $G_t = (O_t, \Sigma_t)$ split, which is the purposeful substate decomposition. "Purposeful substate" names the thing being defined, not just one dimension of it.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.72, len=240, **subst=-0.86**
    > Would conflict with the existing use of "purposeful substate" to name G_t as a whole. The segment *decomposes* the purposeful substate — naming it "purposeful substate" would be the name of the thing being decomposed, not the decomposition.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.67, len=187, **subst=-0.83**
    > This names G_t itself, not the decomposition. The segment is about the decomposition G_t = (O_t, Σ_t); "purposeful substate" is already the name for G_t in the LEXICON. Different concept.

  *substance total (R1 + R2):* -0.69

**Candidate: `Strategic dimension`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > Adjective form flows better.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.89, len=171, **subst=-0.94**
    > Same problem, slightly worse — the adjective form makes it sound like "the dimension along which things are strategic," not "the decomposition of the purposeful substate."
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.86, len=103, **subst=-0.93**
    > Adjective form alone doesn't improve; "strategic" is fine but "dimension" still undersells the content.

  *substance total (R1 + R2):* -1.87


---

### `structural adaptation necessity`

*First-encounter locality:* `#result-structural-adaptation-necessity` (Section I; depends on `#def-model-sufficiency`, `#def-model-class-fitness`, `#result-mismatch-decomposition` (+1 more)). First formal result; When model class fitness is insufficient — when no model in the current class can adequately represent reality — no amount of parametric adaptation can close the mismatch floor.

*Segment:* [`01-aad-core/src/result-structural-adaptation-necessity.md`](../../01-aad-core/src/result-structural-adaptation-necessity.md)

*R2 voters:* 2 (1 architectures: sonnet)

**Candidate: `structural adaptation necessity`** ▸ leader
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=5, mean=1.60, weights=[+1, +1, +1, +3, +2], categories={canonicalize:5}
  > The subject-noun is precise — structural adaptation is the thing whose necessity is established. When parametric update fails. Keep — "necessity" signals this is a derived need ("when parametric update fails, structural adaptation *must* happen").

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +2 ★ *keep* — novelty=0.86, len=373, **subst=1.86**
    > "Structural" is not redundant — parametric adaptation is equally adaptation, and the result is specifically about when *structural* adaptation becomes necessary. Dropping "structural" would leave a phrase that covers both the result and its converse. The two-word qualifier pair ("structural adaptation") is already the established technical term in the framework. Keep it.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.78, len=250, **subst=1.78**
    > Confirmed by segment. "Structural" is load-bearing — it distinguishes from parametric adaptation. "Necessity" signals this is derived necessity, not a prescription. The result IS about when structural change becomes necessary. "Structural" must stay.

  *substance total (R1 + R2):* 4.63

**Candidate: `Adaptation necessity`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > "Structural" is redundant in context, shortens the slug nicely.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *keep* — novelty=0.94, len=168, **subst=-0.97**
    > Drops the load-bearing qualifier. "Adaptation necessity" could refer to any necessity of adaptation; "structural adaptation necessity" is the specific threshold result.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.81, len=203, **subst=-0.91**
    > "Structural" is NOT redundant in context — the entire point of the result is distinguishing structural from parametric adaptation. Dropping "structural" collapses the distinction this result establishes.

  *substance total (R1 + R2):* -0.88


---

### [Concept] *Structural persistence / operational persistence / continuity persistence*

*R2 voters:* 4 (4 architectures: codex, gemini, opus, sonnet)

**Candidate: `Persistence taxonomy`** ▸ leader
- *R1 synthetic:* **+1** — n=1, mean=3.00, weights=[+3], categories={rename:1}
  > Unifies the three distinct usages of "persistence".

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *add-alias* — novelty=0.78, len=85, **subst=1.51**
    > Good umbrella for the three distinct senses of persistence used across the framework.
  - **gemini-r2** (gemini): +2 ★ *rename* — novelty=0.93, len=155, **subst=1.93**
    > This provides the necessary umbrella for the three distinct failure modes. It correctly organizes the 'three deaths' into a coherent theoretical structure.
  - **opus-r2c** (opus): +2 ★ *name-unnamed* — novelty=0.97, len=329, **subst=1.97**
    > This is the genuine name-unnamed-thing slot — the *collective* noun for the three-sense distinction. "Persistence taxonomy" works as a meta-name when you want to invoke the three-way distinction as an object. The three individual names (structural / operational / continuity persistence) stay; the taxonomy itself gains a handle.
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.96, len=282, **subst=0.98**
    > Good collective label. "Persistence taxonomy" names the three-way structure. But the individual names within the taxonomy need to stay; "persistence taxonomy" is a meta-name, not a replacement for the three component names. Acceptable as additional alias for the collective concept.

  *substance total (R1 + R2):* 7.39

**Candidate: `Structural operational continuity persistence`**
- *R1 synthetic:* **+1** — n=1, mean=3.00, weights=[+3], categories={rename:1}
  > LEXICON disambiguates three senses explicitly; the tri-partite naming is doing real work (mentioned as orthogonal in the table). Keep the three names verbatim.

- *R2 votes:*
  - **codex-r2b** (codex): +2 *canonicalize* — novelty=0.85, len=83, **subst=1.54**
    > Keep the three names verbatim: structural, operational, and continuity persistence.
  - **opus-r2c** (opus): +2 *keep* — novelty=0.89, len=562, **subst=1.89**
    > The three-name disambiguation is doing real work. They're orthogonal: structural is about the dynamics' *capacity*, operational about the *current state's reserve*, continuity about *identity through time*. Conflating them is the most-common category error in this vocabulary. The compound "structural operational continuity" reads awkwardly though — better to keep the three terms as distinct names that each take their own modifier ("structural persistence", "operational persistence", "continuity persistence") and use a separate noun for the taxonomy itself.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.91, len=376, **subst=1.91**
    > Confirmed across multiple segments (scope-agent-identity, result-persistence-condition, result-sector-condition-stability). All three senses are load-bearing: structural persistence (the machinery's capacity); operational persistence (proximity to viable region); continuity persistence (identity through time). The three-name taxonomy is doing real work across the framework.

  *substance total (R1 + R2):* 6.33


---

### [Concept] *Symbol default $M_t$ in prose*

*R2 voters:* 3 (3 architectures: codex, gemini, sonnet)

**Candidate: `Model state`** ▸ leader
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={name-unnamed:1}
  > Good neutral default when the argument is about sufficiency, persistence, or update mechanics rather than worldview.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *add-alias* — novelty=0.70, len=150, **subst=1.70**
    > Best neutral default for $M_t$ in update/sufficiency/persistence mechanics: short, accurate, and less grand than repeating "reality model" everywhere.
  - **gemini-r2** (gemini): +2 ★ *add-alias* — novelty=1.00, len=142, **subst=2.00**
    > This is the necessary English alias for $M_t$ in general prose. It correctly identifies the object as the state of the agent's internal model.
  - **sonnet-r2b** (sonnet): +2 ★ *add-alias* — novelty=0.97, len=263, **subst=1.97**
    > "The agent's model state was updated" is natural, accessible, and doesn't lose precision in most contexts. When the argument is specifically about the epistemic vs goal decomposition, "epistemic substate" steps in. These two can coexist with differentiated roles.

  *substance total (R1 + R2):* 5.67

**Candidate: `Epistemic substate`**
- *R1 synthetic:* **+1** [excavated] — n=1, mean=3.00, weights=[+3], categories={canonicalize:1}
  > Standard prose handle for $M_t$.

- *R2 votes:*
  - **codex-r2b** (codex): +1 *add-alias* — novelty=0.80, len=136, **subst=0.90**
    > Precise when the $M_t$ / $G_t$ split is being foregrounded, but too structural as the default prose name before that contrast is active.
  - **sonnet-r2b** (sonnet): +1 *add-alias* — novelty=0.81, len=209, **subst=0.90**
    > Technically precise but "epistemic substate" is jargon-heavy for introductory prose. Useful when distinguishing $M_t$ from $G_t$ as components of $X_t$. Keep as a technical alias, not the default prose handle.

  *substance total (R1 + R2):* 2.80


---

### `temporal nesting`

*First-encounter locality:* `#der-temporal-nesting` (Section I; depends on `#def-adaptive-tempo`, `#result-structural-adaptation-necessity`). First formal derivation; An agent's adaptive processes stratify naturally by timescale, with each level operating on the quasi-steady-state output of the level below.

*Segment:* [`01-aad-core/src/der-temporal-nesting.md`](../../01-aad-core/src/der-temporal-nesting.md)

*R2 voters:* 3 (2 architectures: gemini, sonnet)

**Candidate: `temporal nesting`** ▸ leader
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=5, mean=1.40, weights=[+2, +1, +1, +1, +2], categories={canonicalize:5}
  > Evocative and accurate. Timescale terminology is standard in dynamical systems. Timescale stratification.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +2 ★ *keep* — novelty=0.98, len=351, **subst=1.98**
    > The slug is right. "Nesting" captures the containment structure (faster processes are nested inside the slower ones that use their output). The TST collision argument is weak — "temporal" has distinct scope in each context and won't confuse readers. Singular perturbation theory uses both "timescale" and "temporal" interchangeably; either word works.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.98, len=332, **subst=1.98**
    > Confirmed by segment. "Nesting" carries the right spatial intuition — each adaptive level is nested within the slower level above it. "Temporal" is correct (timescale hierarchy). The collision concern with TST's "temporal" is weak — both AAD and TST use "temporal" to mean "time-related" and the contexts are different. Strong keep.

  *substance total (R1 + R2):* 4.95

**Candidate: `Timescale nesting`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Temporal nesting" is accurate but slightly generic; "timescale nesting" names the specific nesting (slow/fast timescale separation) and avoids collision with TST's "temporal" (as in Temporal Software Theory). Weak preference.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *rename* — novelty=0.78, len=232, **subst=1.78**
    > The argument that 'temporal' collides with TST (Temporal Software Theory) is very strong. 'Timescale nesting' is standard dynamical systems terminology and prevents that collision perfectly while maintaining the geometric intuition.
  - **sonnet-r2b** (sonnet): +1 *keep* — novelty=0.92, len=103, **subst=0.96**
    > Acceptable alternative that emphasizes the rate-separation mechanism. Slightly more technical-sounding.
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.88, len=209, **subst=0.94**
    > Acceptable alternative. "Timescale" is more specific than "temporal" and reduces ambiguity. But "temporal nesting" is already in segments and LEXICON; the rename cost isn't worth the small disambiguation gain.

  *substance total (R1 + R2):* 3.68

**Candidate: `Timescale stratification`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: considered and rejected — too clinical and loses the spatial intuition of "nesting" that aids comprehension.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *keep* — novelty=0.88, len=199, **subst=-0.94**
    > "Stratification" loses the nesting/containment intuition. The key insight is that faster processes are *nested inside* slower ones (their output feeds the slower level), not just layered beside them.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.54, len=81, **subst=-0.62**
    > Correctly rejected in card. Too clinical, loses the spatial intuition of nesting.

  *substance total (R1 + R2):* -2.57


---

### `temporal software theory`

*R2 voters:* 2 (1 architectures: opus)

**Candidate: `temporal software theory`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=3, mean=3.00, weights=[+3, +3, +3], categories={canonicalize:3}
  > Plain, memorable, and unusually scope-honest for a domain theory. TST's name is descriptive and distinctive. The full name of TST.

- *R2 votes:*
  - **opus-r2b** (opus): +2 ★ *keep* — novelty=0.93, len=396, **subst=1.93**
    > "Temporal" is load-bearing — it signals the AAD-native framing that software is a *time-optimality* problem (developer agents, persistence-condition for codebases, $\mathcal T$ as iteration frequency × feedback quality) rather than a correctness or efficiency problem. The framework's distinctive contribution to software methodology is exactly this temporal framing; the name should preserve it.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.96, len=357, **subst=1.96**
    > "Temporal" is load-bearing; software-engineering vocabulary is full of correctness-/quality-/architecture-flavored frames, and naming the framework around *time* signals what it's doing differently. The acronym is workable, the prior-work corpus carries citation velocity, and the AAD-grounded reframe reads as continuity-with-extension rather than rebrand.

  *substance total (R1 + R2):* 5.89

**Candidate: `Temporal Software Theory (TST)`**
- *R1 synthetic:* **+1** [invented] — n=1, mean=3.00, weights=[+3], categories={canonicalize:1}
  > Keep. The name has history (prior to AAD absorption and subsequent restoration) and "temporal" is load-bearing — it signals the AAD-native view that software is a time-optimality problem rather than a correctness problem. The acronym TST is pronounceable and has existing citation velocity from the 14,000-file prior corpus.

- *R2 votes:*
  - **opus-r2b** (opus): +1 *canonicalize* — novelty=0.96, len=214, **subst=0.98**
    > Capitalized form for the proper-noun usage; the bare phrase reads as a topic. Useful in framing-level prose ("TST is positioned as AAD's calibration laboratory"). Coexists with the lowercase form for general prose.
  - **opus-r2c** (opus): +1 *keep* — novelty=0.98, len=120, **subst=0.99**
    > Same vote; the parenthetical-acronym form is fine in formal contexts, the lowercase prose form is fine in running prose.

  *substance total (R1 + R2):* 2.97


---

### `the Greek vocabulary`

*R2 voters:* 2 (1 architectures: opus)

**Candidate: `The greek philosophical vocabulary`** ▸ leader
- *R1 synthetic:* **0** [invented] — n=1, mean=1.00, weights=[+1], categories={canonicalize:1}
  > The cycle phases (Prolepsis, Aisthesis, Aporia, Epistrophe, Praxis) are described as "the Greek philosophical vocabulary" in NOTATION.md and as "Greek-rooted vocabulary" in CLAUDE.md. Canonicalize on "Greek philosophical vocabulary" — the philosophical qualification is doing work (these are Greek philosophical terms, not generic Greek words).

- *R2 votes:*
  - **opus-r2c** (opus): +2 ★ *canonicalize* — novelty=0.74, len=453, **subst=1.74**
    > "Greek philosophical" is more accurate than "Greek-rooted" or "Greek vocabulary" — the framework's choice is specifically *Greek philosophy* (prolepsis from Stoics/Epicureans, aporia from Plato/Aristotle, etc.). The philosophical qualification anchors the choice in why these particular Greek terms (each picks out a distinction the philosophical tradition already developed) vs. arbitrary Greek words. Canonicalize across NOTATION/CLAUDE/LEXICON drift.
  - **opus-r2b** (opus): +1 *canonicalize* — novelty=0.85, len=196, **subst=0.92**
    > Useful disambiguation — these are Greek *philosophical* terms (Aristotle, Heidegger as transmission lineage), not generic Greek words. The canonical phrase commits the project to that distinction.

  *substance total (R1 + R2):* 2.66


---

### [Concept] *Superlinear scaling of adversarial tempo advantage*

*R2 voters:* 2 (2 architectures: gemini, sonnet)

**Candidate: `Superlinear tempo advantage`** ▸ leader
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > Identifies the exponentiated return on adversarial tempo.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +2 ★ *name-unnamed* — novelty=0.96, len=251, **subst=1.96**
    > The right name for this concept. Names the mathematical property (superlinear) and the outcome (tempo advantage). From hyp-mismatch-dynamics: "the steady-state mismatch ratio scales superlinearly with the tempo ratio" — the scaling is the key finding.

  *substance total (R1 + R2):* 2.96

**Candidate: `Boyd's exponent`**
- *R1 synthetic:* **+1** — n=1, mean=3.00, weights=[+3], categories={name-unnamed:1}
  > Formalizes the exact superlinear payoff of operating inside an opponent's OODA loop.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *name-unnamed* — novelty=0.70, len=150, **subst=1.70**
    > This name honors the lineage of OODA loop theory while formalizing the exact superlinear payoff of operating at higher tempo in adversarial couplings.
  - **sonnet-r2c** (sonnet): -1 *name-unnamed* — novelty=0.96, len=173, **subst=-0.98**
    > As argued in row 7: Boyd is the inspiration, not the source. Naming the exponent after Boyd implies prior-art adoption. This is AAD's derived result, not Boyd's mathematics.

  *substance total (R1 + R2):* 1.72


---

### [Concept] *The 2×2 table of satisfaction gap vs control regret × goal attainability diagnostic*

*R2 voters:* 2 (1 architectures: sonnet)

**Candidate: `The 2×2 diagnostic`** ▸ leader
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={name-unnamed:1}
  > Used ubiquitously in prose. Worth canonicalizing as a named object so that "see the 2×2 diagnostic" reads naturally.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +2 ★ *name-unnamed* — novelty=0.78, len=356, **subst=1.78**
    > Already used as "the 2×2 diagnostic" throughout #der-orient-cascade and #def-control-regret. Canonicalizing it as a named handle lets prose say "see the 2×2 diagnostic" naturally. The axes are δ_sat and δ_regret; the four cells give: success / strategy problem / both / capability limit. The table *is* the core orient-cascade decision logic. Worth naming.
  - **sonnet-r2c** (sonnet): +2 ★ *name-unnamed* — novelty=0.87, len=233, **subst=1.87**
    > Confirmed by both def-satisfaction-gap and def-control-regret, which both present the 2×2 table. "The 2×2 diagnostic" is already used in prose and is self-describing. The table deserves a canonicalized handle. Strong case for naming.

  *substance total (R1 + R2):* 3.64

**Candidate: `The cascade diagnostic or the 2×2 diagnostic`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={name-unnamed:1}
  > The four cells of ($\delta_{\text{sat}}$, $\delta_{\text{regret}}$) are consistently referenced in `der-orient-cascade` as "the 2×2 diagnostic" or "the four cases." These deserve a named handle. "Cascade diagnostic" is the most natural single-noun form. Weak preference — "2×2 diagnostic" is already near-canonical in the prose.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +1 *name-unnamed* — novelty=0.78, len=131, **subst=0.89**
    > Two candidates within one row — "cascade diagnostic" is fine, "the 2×2 diagnostic" is better (already near-canonical in the prose).
  - **sonnet-r2c** (sonnet): +1 *name-unnamed* — novelty=0.82, len=132, **subst=0.91**
    > "2×2 diagnostic" is near-canonical in prose. Worth canonicalizing as-is. But the slash "or" form is not a good name — commit to one.

  *substance total (R1 + R2):* 1.80

**Candidate: `Diagnostic gap matrix`**
- *R1 synthetic:* **+1** [invented] — n=1, mean=3.00, weights=[+3, +3, +3], categories={canonicalize:2, rename:1}
  > Reinforces the name for the core performance diagnostic. Locks in the diagnostic table name. Provides a formal name for the 2x2 performance/strategy diagnostic.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *name-unnamed* — novelty=0.95, len=102, **subst=-0.98**
    > "Matrix" sounds like a software term; the 2×2 table is a conceptual framework, not a numerical matrix.
  - **sonnet-r2c** (sonnet): -1 *name-unnamed* — novelty=0.95, len=118, **subst=-0.98**
    > "Matrix" is technically correct (2×2 matrix of cases) but loses the diagnostic emphasis. "Diagnostic" alone is better.

  *substance total (R1 + R2):* -0.95

**Candidate: `Diagnostic square`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={name-unnamed:1}
  > The table is used often enough to deserve a compact public name.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *name-unnamed* — novelty=0.93, len=76, **subst=-0.73**
    > "Square" is geometric; the table isn't particularly square-ish conceptually.
  - **sonnet-r2c** (sonnet): -1 *name-unnamed* — novelty=1.00, len=44, **subst=-0.44**
    > "Square" is informal; "2×2" is more precise.

  *substance total (R1 + R2):* -1.17

**Candidate: `Satisfaction control table the diagnostic 2×2`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={name-unnamed:1}
  > Rejection argument: this table is embedded within the satisfaction-gap and control-regret segment discussions. Naming it as a standalone concept would create a fourth-order abstraction that the prose already handles via the two-concept names. The power of the structure comes from the *names of the axes*, not from a separate name for the table itself. Do not name the table separately. Let it exist as "the satisfaction-gap / control-regret 2×2" in prose.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *name-unnamed* — novelty=0.97, len=33, **subst=-0.33**
    > Too verbose for a canonical name.
  - **sonnet-r2c** (sonnet): -1 *name-unnamed* — novelty=0.67, len=199, **subst=-0.83**
    > The rejection argument is correct: the power comes from the axis names (satisfaction gap, control regret), not from naming the table itself. But "the 2×2 diagnostic" is short enough to be acceptable.

  *substance total (R1 + R2):* -2.16


---

### [Concept] *The Pearl-blanket reading of directed separation*

*R2 voters:* 2 (2 architectures: opus, sonnet)

**Candidate: `Pearl-blanket form`** ▸ leader
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={name-unnamed:1}
  > The term "Pearl-blanket" appears in `#der-directed-separation`'s Discussion (adopted from Bruineberg et al. 2022) but has no first-class slug. The recognition that AAD's directed-separation is the Pearl-blanket form (not the Friston-blanket form) is a load-bearing positioning claim and is currently invisible at the slug layer. Could land as a discussion-segment or be canonicalized in the existing segment's prose.

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +2 ★ *name-unnamed* — novelty=0.69, len=390, **subst=1.69**
    > Confirmed by segment. The segment explicitly adopts the Pearl-blanket reading (Bruineberg et al. 2022), explicitly rejects the Friston-blanket reading, and the entire architectural classification (Class 1/2/3) follows from this. "Pearl-blanket form" correctly names the conditional-independence reading that directed separation uses. Load-bearing positioning claim that deserves visibility.
  - **opus-r2b** (opus): +1 *name-unnamed* — novelty=0.66, len=692, **subst=0.83**
    > The recognition that AAD's directed-separation is the *Pearl-blanket* (technical conditional-independence) form rather than the *Friston-blanket* (metaphysical demarcation) form is a load-bearing positioning move. The phrase appears only in `#der-directed-separation`'s Discussion (Bruineberg et al. 2022 attribution). Promoting "Pearl-blanket form" to first-class status — either a `disc-` segment or canonicalize it in prose with bold emphasis — would let downstream segments cite the positioning claim explicitly when defending against "isn't this just the Markov blanket?" challenges. Weak preference: the discussion-paragraph treatment may be sufficient; the gap is genuine but marginal.

  *substance total (R1 + R2):* 3.51


---

### `update gain`

*First-encounter locality:* `#emp-update-gain` (Section I; depends on `#def-mismatch-signal`, `#def-observation-function`). Empirical claim; The optimal weight an agent assigns to new observations when updating its model — the rate of *epistrophe* (turning toward reality).

*Segment:* [`01-aad-core/src/emp-update-gain.md`](../../01-aad-core/src/emp-update-gain.md)

*R2 voters:* 3 (3 architectures: gemini, opus, sonnet)

**Candidate: `update gain`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=10, mean=2.60, weights=[+1, +1, +3, +3, +3, +3, +3, +3, +3, +3], categories={canonicalize:8, add-alias:2}
  > Adopted from Kalman / control theory. The case for keeping is the prior-art-integration convention plus the transfer of correct baggage: 'gain' in AAD plays the role the reader expects, and the formula $\eta^\ast = U_M / (U_M + U_o)$ is iconic in the framework. Renaming would lose a load-bearing prose convention. The follow-on alias votes formalize the symbol+English pair across NOTATION.md and LEXICON.md.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.84, len=127, **subst=1.84**
    > The argument to keep the Kalman baggage is definitive. $\eta^\ast = U_M / (U_M + U_o)$ is a gain equation, not a learning rate.
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.70, len=290, **subst=1.70**
    > Adopted from Kalman/control with correct baggage — "gain" in AAD plays the role a control engineer expects (weight on new observation in the update). The formula $\eta^* = U_M/(U_M + U_o)$ is iconic in the framework. Pairs cleanly with "adaptive tempo" (rate-quality compound). Strong keep.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.79, len=167, **subst=1.79**
    > The Kalman/control baggage transfers correctly; $\eta^\ast = U_M/(U_M+U_o)$ is a genuine uncertainty-ratio gain, not an SGD learning rate. The formula is iconic. Keep.

  *substance total (R1 + R2):* 7.33

**Candidate: `Epistemic gain`**
- *R1 synthetic:* **+1** [excavated] — n=2, mean=1.00, weights=[-1, +3], categories={rename:1, canonicalize:1}
  > "Update gain" is standard control theory but "Epistemic gain" elegantly bridges the math to the 'Epistrophe' phase. Objection: loses correct Kalman/control baggage and creates avoidable overlap with epistemic unity.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.85, len=186, **subst=-0.92**
    > "Epistemic" reads as a different axis than "update" — loses the Kalman lineage AND collides with "epistemic unity" $U_M$ (the Section III collision the framework is already negotiating).
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.69, len=140, **subst=-0.85**
    > Creates avoidable collision with "epistemic unity" (already a term in the framework). The Kalman/control baggage of "gain" is worth keeping.

  *substance total (R1 + R2):* -0.77

**Candidate: `Update gain uncertainty ratio principle`**
- *R1 synthetic:* **0** [invented] — n=1, mean=1.00, weights=[+1], categories={canonicalize:1}
  > Standard term; doesn't carry the *uncertainty-ratio* insight. The equation tag's "uncertainty-ratio-principle" is more evocative. Brief-grade hint, possibly visible in title.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.89, len=128, **subst=-0.94**
    > Heavy compound. The "uncertainty ratio" insight is real but lives in the Discussion; the slug should compress it, not unpack it.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.96, len=99, **subst=-0.97**
    > Too verbose for a primary name; this is better suited for the Brief field or a parenthetical gloss.

  *substance total (R1 + R2):* -1.92

**Candidate: `Learning rate`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={add-alias:1}
  > Rejection argument: considered. ML-standard term. Rejected: the segment-derivation in `#emp-update-gain` shows $\eta^\ast = U_M / (U_M + U_o)$ — a Bayesian uncertainty ratio, not a stochastic-gradient-descent step size. The collision with ML's "learning rate" creates false familiarity.

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.61, len=242, **subst=-0.81**
    > "Learning rate" creates false familiarity — readers will import SGD step-size intuitions where AAD's $\eta^* = U_M/(U_M + U_o)$ is a Bayesian uncertainty ratio. The collision damages comprehension precisely *because* the term sounds familiar.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.81, len=97, **subst=-0.88**
    > Creates false familiarity with ML's SGD learning rate, which has completely different properties.

  *substance total (R1 + R2):* -2.69


---

### `value object`

*First-encounter locality:* `#def-value-object` (Section II; depends on `#form-objective-functional`, `#form-agent-model`, `#der-directed-separation` (+1 more)). First formal definition; The horizon- and policy-conditioned value object $V_O$ turns the abstract objective functional $V_{O_t}$ into a decision-making tool: "given what I believe, what I plan to do next, and how far I'm….

*Segment:* [`01-aad-core/src/def-value-object.md`](../../01-aad-core/src/def-value-object.md)

*R2 voters:* 2 (2 architectures: gemini, sonnet)

**Candidate: `Policy-conditioned value`** ▸ leader
- *R1 synthetic:* **+1** — n=1, mean=3.00, weights=[+3], categories={rename:1}
  > "Value object" is overloaded from software design and hides the continuation-convention dependence. The proposed name says what the quantity actually is.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +2 ★ *rename* — novelty=0.79, len=237, **subst=1.79**
    > Names the central content: the value quantity is conditioned on a continuation policy convention, which is what the C1/C2/C3 hierarchy is about. "Policy-conditioned" is self-announcing. The software "value object" baggage is a real cost.

  *substance total (R1 + R2):* 2.79

**Candidate: `value object`**
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=4, mean=1.75, weights=[+1, +3, +1, +2], categories={canonicalize:4}
  > Technical term adopted from RL/game-theory; consistent prose usage. Compact name for a complex object (horizon- and policy-conditioned value functional). Weak keep.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.85, len=205, **subst=1.85**
    > Though 'value object' has software baggage, it is the standard term in the project for the decision-making tool produced by the evaluation functional under a continuation convention. Compact and evocative.
  - **sonnet-r2b** (sonnet): -1 *keep* — novelty=0.93, len=245, **subst=-0.96**
    > The software-pattern baggage ("value object" in OOP = immutable container for a value type) misleads readers from non-mathematical backgrounds. The name doesn't signal the continuation-convention dependency that is the segment's central content.

  *substance total (R1 + R2):* 1.88

**Candidate: `Decision value`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Value object" sounds implementation-ish; "decision value" says what the quantity is for in prose.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +1 *rename* — novelty=0.89, len=218, **subst=0.95**
    > Acceptable short form. "Decision" situates it in the action-selection context without the software-pattern baggage of "value object." Less precise than "policy-conditioned value" since it doesn't name the conditioning.

  *substance total (R1 + R2):* 0.95

**Candidate: `Trajectory value`**
- *R1 synthetic:* **+1** — n=2, mean=0.50, weights=[+2, -1], categories={rename:2}
  > Argument for: 'value object' has software baggage and sounds like an implementation pattern, where the segment actually defines a horizon-and-policy-conditioned trajectory value. Counter-argument: 'trajectory value' elides the convention-conditioning that is the segment's central content. The C1/C2/C3 hierarchy lives in this segment precisely because the value depends on the *convention* chosen for continuation, not just on the trajectory. 'Trajectory value' suggests something computable from a trajectory alone — which is exactly what the segment shows is impossible without specifying convention. A 'continuation-conditioned value' alternative was floated as more accurate.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.65, len=255, **subst=-0.83**
    > Loses the continuation-convention conditioning. "Trajectory value" suggests something computable from a trajectory alone — which the segment explicitly shows is impossible without specifying convention (C1/C2/C3). The convention is part of the definition.

  *substance total (R1 + R2):* 0.17

**Candidate: `Value functional`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: considered and rejected — "value functional" is also accurate but would collide with `form-objective-functional` (which is the upstream functional-form definition the value object inherits from). The current names disambiguate cleanly: objective is the functional, value is the object the functional produces under a continuation convention.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.58, len=211, **subst=-0.79**
    > Would collide with "objective functional" (#form-objective-functional) — the upstream functional that value object inherits from. The names cleanly disambiguate now; renaming would collapse a useful distinction.

  *substance total (R1 + R2):* -1.79


---

## Convergent with friction (7)

### `$\mathcal{C}_t$ (chronica)`

*R2 voters:* 3 (3 architectures: codex, gemini, opus)

**Candidate: `Chronica or interaction history`** ▸ leader
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={add-alias:1}
  > Confirm. Both are in use; "chronica" carries the etymological / cycle-vocabulary commitment, "interaction history" is the engineering paraphrase. Both should remain available; the LEXICON's gloss already supplies both.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.87, len=236, **subst=1.87**
    > 'Chronica' is the precise, register-faithful name for the sequence $\mathcal{C}_t$. 'Interaction history' is the necessary engineering translation. Keeping both allows for context-appropriate prose while maintaining technical precision.
  - **opus-r2c** (opus): +2 ★ *add-alias* — novelty=0.72, len=449, **subst=1.72**
    > The pairing is right: chronica is the canonical Greek-rooted noun (carrying the singular-non-forkable / (PI) commitment); "interaction history" is the engineering paraphrase that reads cleanly when speaking with audiences who don't yet know the framework's vocabulary. Both should be available with the differentiation: chronica when invoking AAD's commitments, interaction history when the gloss is what's needed. The LEXICON already provides both.
  - **codex-r2b** (codex): -1 *add-alias* — novelty=0.94, len=153, **subst=-0.97**
    > The "or" framing makes the terms sound freely substitutable. The segment needs `chronica` as the canonical noun and an English gloss for first encounter.

  *substance total (R1 + R2):* 3.62

**Candidate: `chronica (complete interaction history)`**
- *R1 synthetic:* — (no R1 evidence)

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *canonicalize* — novelty=1.00, len=170, **subst=2.00**
    > Canonicalize the pairing: `chronica` names the complete, singular, non-forkable causal record; "complete interaction history" is the explanatory gloss, not a replacement.

  *substance total (R1 + R2):* 2.00


---

### `$U_o$`

*R2 voters:* 2 (2 architectures: gemini, opus)

**Candidate: `Teleological coherence`** ▸ leader
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={add-alias:1}
  > Maps the symbol to its conceptual meaning.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *add-alias* — novelty=0.95, len=190, **subst=1.95**
    > This is the necessary English alias for $U_o$. It perfectly names the property of the agent's actions aligning with its objective, while the symbol $U_o$ remains the mathematical coordinate.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.96, len=702, **subst=-0.98**
    > This appears to be miscategorized — $U_o$ is *observation uncertainty* (per NOTATION) not $U_O$ (teleological unity, where this rationale would apply). The candidate name "teleological coherence" maps to $U_O$ (capital O), not $U_o$ (lowercase). This is exactly the U_o/U_O collision noted in #418. The candidate is wrong for this row's symbol. *Process note*: this is a strong instance of the U_o/U_O collision causing real downstream confusion, including in the voting card itself. The row should be voting on an alias for *observation uncertainty* (something like "perceptual uncertainty" or "channel uncertainty"); instead it's offering a candidate for the *unity* symbol that uses the same letter.

  *substance total (R1 + R2):* 0.97


---

### `agent identity`

*First-encounter locality:* `#scope-agent-identity` (Section I; depends on `#def-chronica`, `#def-model-sufficiency`). Scope-narrowing first encounter; AAD applies to agents instantiated on singular causal trajectories.

*Segment:* [`01-aad-core/src/scope-agent-identity.md`](../../01-aad-core/src/scope-agent-identity.md)

*R2 voters:* 4 (3 architectures: gemini, opus, sonnet)

**Candidate: `agent identity`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=6, mean=2.50, weights=[+2, +1, +3, +3, +3, +3], categories={canonicalize:6}
  > Crucial scope definition. Clean scope statement; the subject-noun is clear. Formal scope claim naming token-level commitment (agents on singular, non-forkable trajectories).

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.91, len=200, **subst=1.91**
    > Though 'trajectory identity' is more precise, 'agent identity' is the established term for the singular, non-forkable causal record. It correctly centers the focus on the agent as a persistent entity.
  - **sonnet-r2c** (sonnet): +2 ★ *keep* — novelty=0.88, len=346, **subst=1.88**
    > Confirmed by segment. The scope statement IS about agent identity — what makes an agent a singular entity within AAD. "Agent identity" is what this establishes. The subject-noun is correct; the concept name is natural. The three-persistence disambiguation (structural/operational/continuity) uses "identity" in this sense in LEXICON. Strong keep.
  - **opus-r2c** (opus): +1 *keep* — novelty=1.00, len=197, **subst=1.00**
    > The bare term works in context but is soft — "identity" alone invites metaphysical baggage the segment doesn't carry. The segment's substance is sharper than the slug. Acceptable but not preferred.
  - **sonnet-r2b** (sonnet): -1 *keep* — novelty=0.89, len=237, **subst=-0.95**
    > Too soft — "agent identity" is the name of every philosophy-of-mind article from the last 30 years. The formal content is specifically about *causal* identity grounded in *non-forkable trajectories*, and the prose handle should say that.

  *substance total (R1 + R2):* 5.84

**Candidate: `Causal identity`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > "Agent identity" is very soft. "Causal identity" anchors it strictly to the non-forkable causal trajectory.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +2 ★ *rename* — novelty=0.80, len=328, **subst=1.80**
    > Most concise, most informative. "Causal" anchors it to the non-forkable causal-trajectory structure without needing "trajectory" spelled out. Contrast with "model identity" (which would name the model-state-as-identity view that the segment rejects) is implicit and correct. Works in prose: "AAD's causal identity commitment..."
  - **opus-r2c** (opus): +1 *rename* — novelty=0.80, len=308, **subst=0.90**
    > "Causal identity" anchors more cleanly than bare "agent identity" — the segment's identity condition is the *causal-trajectory non-forkability* (per def-chronica), and "causal identity" picks out that specific axis without the metaphysical baggage of "identity" alone. Strong alternative if the rename lands.
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.58, len=100, **subst=0.79**
    > "Causal" is good — it anchors in the non-forkable causal trajectory. Less verbose than alternatives.

  *substance total (R1 + R2):* 3.49

**Candidate: `Singular causal trajectory`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > The segment's identity condition is the singular trajectory, and that subject is more distinctive than agent identity.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +1 *rename* — novelty=0.94, len=93, **subst=0.90**
    > What grounds identity in AAD — precise and unambiguous. Slightly long for repeated prose use.
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.68, len=239, **subst=0.84**
    > This is the defining property, not the named concept. "Singular causal trajectory" would be the subject-noun for the chronica, not for this scope segment. The segment is about agent identity, using the singular trajectory as the grounding.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.69, len=188, **subst=-0.85**
    > This is what the *condition* is, not what the *segment* is about (the segment is about the agent-having-this-condition). Picking the condition as the noun loses the agent-identity framing.

  *substance total (R1 + R2):* 1.90

**Candidate: `Trajectory identity`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > The segment's formal content is about trajectory singularity; "agent identity" invites more metaphysical baggage than the math supports.

- *R2 votes:*
  - **sonnet-r2b** (sonnet): +1 *rename* — novelty=0.93, len=172, **subst=0.96**
    > Concise and accurate. "Trajectory identity" focuses attention on the non-forkability structure. Pairs well with "model identity" if that term were ever needed for contrast.
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.84, len=193, **subst=0.92**
    > Better than "agent identity" — anchors in the trajectory. But the segment is also about identity in the broader sense (type vs token, clone problem, PI axiom). "Trajectory identity" undersells.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.92, len=135, **subst=-0.96**
    > Drops the "causal" qualifier that's load-bearing — the trajectory is *causal* (Pearl-Level-2 contrasts), not just a sequence of states.

  *substance total (R1 + R2):* 0.92

**Candidate: `Identity as singular causal trajectory`**
- *R1 synthetic:* **+1** — n=1, mean=3.00, weights=[+3], categories={rename:1}
  > "Slug-as-mechanical-prefix hides the substantive claim." The segment is structurally important for the framework's identity-and-continuity claims (esp. for consciousness-infrastructure substrate-independence work) and the title gloss is closer to what it actually does than the slug. Auditor felt the friction acutely: "single most important §I segment for the broader project's purposes.".

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +1 *rename* — novelty=0.90, len=136, **subst=0.95**
    > Verbose but accurate. The segment title uses this form. But slug names should be concise; "agent identity" is the right compressed form.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.97, len=75, **subst=-0.74**
    > Long-form expansion. Fine as one-time first-introduction but not as a slug.
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.98, len=100, **subst=-0.99**
    > This is a description, not a name. Works as a gloss in OUTLINE.md; too heavy for repeated prose use.

  *substance total (R1 + R2):* 0.22

**Candidate: `The trajectory identity scope`**
- *R1 synthetic:* **+1** — n=1, mean=3.00, weights=[+3], categories={rename:1}
  > "Slug-as-mechanical-prefix hides the substantive claim." The segment is structurally important for the framework's identity-and-continuity claims (esp. for consciousness-infrastructure substrate-independence work) and the title gloss is closer to what it actually does than the slug. Auditor felt the friction acutely: "single most important §I segment for the broader project's purposes.".

- *R2 votes:*
  - **opus-r2c** (opus): -1 *rename* — novelty=0.95, len=99, **subst=-0.96**
    > Adds "the" and "scope" both, neither of which the slug needs (scope is encoded in `scope-` prefix).
  - **sonnet-r2b** (sonnet): -1 *rename* — novelty=0.95, len=89, **subst=-0.87**
    > The word "scope" is redundant — the heading prefix already marks this as a scope segment.
  - **sonnet-r2c** (sonnet): -1 *rename* — novelty=0.92, len=111, **subst=-0.96**
    > "The trajectory identity scope" is a prose description, not a name. The "scope-" prefix is already in the slug.

  *substance total (R1 + R2):* -1.79


---

### `causal structure`

*First-encounter locality:* `#post-causal-structure` (Section I; depends on `#def-agent-environment`, `#def-chronica`). Foundational postulate; The agent-environment interaction has irreducible causal structure grounded in the temporal ordering of events. Actions precede their consequences; observations follow from the state they observe.

*Segment:* [`01-aad-core/src/post-causal-structure.md`](../../01-aad-core/src/post-causal-structure.md)

*R2 voters:* 4 (3 architectures: codex, gemini, opus)

**Candidate: `causal structure`** ▸ leader
- *R1 synthetic:* **+1** [is_keep] [excavated] — n=4, mean=1.75, weights=[+2, +1, +2, +2], categories={canonicalize:4}
  > Irreducible causal structure (postulate). Acceptable keep. Foundational postulate about irreducible causal structure.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *keep* — novelty=0.87, len=183, **subst=1.87**
    > Plain but correct for the root postulate: temporal ordering gives the agent-environment interaction irreducible possible-influence structure before Pearl/statistical causality enters.
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.95, len=128, **subst=1.95**
    > Load-bearing foundational term. It grounds the framework in the physical arrow of time rather than pure statistical correlation.
  - **opus-r2c** (opus): +1 ★ *keep* — novelty=0.89, len=480, **subst=0.95**
    > The slug captures what the segment names — the postulate is about the *structure* of causal relations grounded in temporal ordering. The bare term is generic in adjacent literatures (Spirtes-Glymour-Scheines, Pearl, etc.) but here the postulate is doing specific work: temporal ordering as the most-primitive causal notion, prior to statistical causality. Acceptable. Could be sharpened to "temporal causal structure" or "causal-temporal foundation" but the existing slug is fine.
  - **opus-r2b** (opus): -1 *rename* — novelty=0.91, len=480, **subst=-0.96**
    > The slug names a *consequence* of the postulate, not the postulate. The actual axiom is "event A can be a cause of event B only if A temporally precedes B" — the temporal-precedence primitive. "Causal structure" is overloaded with Pearl/causal-graph intuitions that the segment is *prior to* — the segment establishes the substrate on which the Pearl hierarchy (def-pearl-causal-hierarchy) is then defined. A subject-noun-first slug should name the substrate, not the consequence.

  *substance total (R1 + R2):* 4.81

**Candidate: `temporal precedence`**
- *R1 synthetic:* — (no R1 evidence)

- *R2 votes:*
  - **opus-r2b** (opus): +2 ★ *rename* — novelty=1.00, len=500, **subst=2.00**
    > Write-in. Names exactly the postulate's content: "event A can be a cause of event B only if A temporally precedes B." The slug becomes self-explanatory and disambiguates the postulate from the Pearl hierarchy that builds on it. Survives the renamed-from-now-sounds-weird test: hearing `#post-temporal-precedence` six months out, a reader correctly anticipates the temporal axiom; hearing `#post-causal-structure` they reasonably anticipate the Pearl hierarchy and find a more primitive thing instead.

  *substance total (R1 + R2):* 2.00


---

### `chronica brief gloss`

*R2 voters:* 2 (2 architectures: codex, opus)

**Candidate: `complete interaction history`** ▸ leader
- *R1 synthetic:* — (no R1 evidence)

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *add-alias* — novelty=1.00, len=165, **subst=2.00**
    > Best first-use gloss. It stays English-accessible while preserving the key property that $\mathcal C_t$ is the complete raw sequence from which $M_t$ is constructed.

  *substance total (R1 + R2):* 2.00

**Candidate: `Interaction history chronica`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > Pairs the Greek term with its English translation for accessibility.

- *R2 votes:*
  - **opus-r2b** (opus): +1 *canonicalize* — novelty=0.93, len=345, **subst=0.97**
    > "Interaction history (*chronica*)" or "*chronica* — the interaction history" is the natural pair-on-first-use form when a reader encounters the term. Standardizing the gloss form (rather than "complete record" / "causal trajectory" / etc. paraphrases) helps. Weak preference; the gloss should pair the engineering paraphrase with the Greek noun.
  - **codex-r2b** (codex): -1 *add-alias* — novelty=1.00, len=152, **subst=-1.00**
    > Awkward as written and too weak: "interaction history" loses the complete, singular, irreversible causal-record force that the segment gives `chronica`.

  *substance total (R1 + R2):* 0.97


---

### `Class 2 agent`

*R2 voters:* 2 (2 architectures: opus, sonnet)

**Candidate: `Integrated agent`** ▸ leader
- *R1 synthetic:* **+1** — n=1, mean=3.00, weights=[+3], categories={rename:1}
  > Class 2 = integrated (the goal-entangled architecture). Companion to Modular (Class 1) and Partially-Coupled (Class 3). [original row: Class 1/2/3 trio voted +3 as a unit; split into atomic per-class rows.].

- *R2 votes:*
  - **sonnet-r2c** (sonnet): +2 ★ *rename* — novelty=0.89, len=224, **subst=1.89**
    > "Class 2" requires a lookup every time. "Integrated" names the architectural property directly: the goal-state and epistemic-state processing are integrated (no directed separation). This is the information the reader needs.
  - **opus-r2b** (opus): -1 *rename* — novelty=0.90, len=326, **subst=-0.95**
    > Same reasoning as row 84 — "integrated" has positive valence the framework doesn't intend. Class 2 is *failure-by-construction* of directed separation (transformer LLMs); "integrated" sounds like a feature rather than a structural fact. "Merged agent" or "coupled agent" would be more honest if a non-numeric handle is needed.

  *substance total (R1 + R2):* 1.94


---

### `Pearl L3`

*R2 voters:* 3 (3 architectures: codex, gemini, opus)

**Candidate: `Counterfactual reasoning`** ▸ leader
- *R1 synthetic:* — (no R1 evidence)

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *add-alias* — novelty=1.00, len=109, **subst=2.00**
    > Best brief-grade gloss for Pearl L3: "given what happened, what would have happened if I had done otherwise?"

  *substance total (R1 + R2):* 2.00

**Candidate: `Reasoning`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={add-alias:1}
  > Brief-grade agent-side gloss for Pearl's L3 (counterfactual). NOT a rename.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *add-alias* — novelty=0.63, len=155, **subst=1.63**
    > This is the necessary agent-side gloss for Pearl's L3 (counterfactual). It provides an intuitive English handle for the highest level of causal capability.
  - **codex-r2b** (codex): -1 *add-alias* — novelty=0.82, len=101, **subst=-0.91**
    > Too broad for Pearl L3. All three levels are reasoning modes; Level 3 is specifically counterfactual.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.88, len=504, **subst=-0.94**
    > "Reasoning" undersells L3 considerably — L3 is specifically *counterfactual* simulation ("what would I have observed if I had done a' instead"). "Reasoning" applies at every level (Bayesian inference is reasoning, intervention-planning is reasoning). The Brief-grade gloss for L3 should be "imagining alternatives" or "counterfactualizing" — something that picks out the counterfactual operation. -1 because adopting "reasoning" as the L3 alias would damage the discrimination from L1/L2 the trio is for.

  *substance total (R1 + R2):* -0.22


---

## Divergent (4)

### `agent environment`

*First-encounter locality:* `#def-agent-environment` (Section I; no upstream dependencies). First formal definition; An agent is an entity that receives observations from an environment, maintains internal state, and produces actions that affect the environment.

*Segment:* [`01-aad-core/src/def-agent-environment.md`](../../01-aad-core/src/def-agent-environment.md)

*R2 voters:* 4 (3 architectures: codex, gemini, opus)

**Candidate: `Agent environment boundary`** ▸ leader
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > The auditor noted segment content is "the boundary," not "the coupling" — coupling is the *channels* defined in the next two segments. Tentative.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *rename* — novelty=0.88, len=90, **subst=1.69**
    > The first primitive is the boundary that makes observation and action channels well-typed.
  - **opus-r2b** (opus): +2 ★ *rename* — novelty=0.82, len=384, **subst=1.82**
    > Segment's body delivers an information-loss boundary condition + the three structural conditions for agent-hood; it does not yet formalize coupling-as-channels (that's the next two segments — observation function, action transition). "Boundary" is the load-bearing word: the constitutive scope condition is "agent has no direct access to $\Omega_t$." Auditor's distinction is correct.
  - **opus-r2c** (opus): +1 *rename* — novelty=0.82, len=433, **subst=0.91**
    > The segment's title is "Agent-Environment Coupling" but the substance is the *boundary* (the information-loss commitment between agent and environment). The auditor's note is correct — the segment names the boundary as constitutive, not the coupling. The coupling lives in the next two segments (def-action-transition, def-observation-function). "Boundary" is a more accurate subject-noun than "coupling" or bare "agent environment."

  *substance total (R1 + R2):* 4.42

**Candidate: `agent environment`**
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=5, mean=2.20, weights=[+3, +1, +2, +3, +2], categories={canonicalize:5}
  > Agent-environment boundary. Keep. Acceptable keep.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *keep* — novelty=0.86, len=132, **subst=1.86**
    > Foundationally established. The segment defines the coupling, and 'agent environment' is the canonical name for the two-part system.
  - **codex-r2b** (codex): +1 *keep* — novelty=1.00, len=54, **subst=0.54**
    > Serviceable broad segment root for the primitive pair.
  - **opus-r2c** (opus): +1 ★ *keep* — novelty=0.83, len=349, **subst=0.91**
    > Acceptable as-is — the bare "agent environment" works as a slug that names the *pair* being coupled. The slight mismatch (segment is more about boundary than coupling) is a minor scope-honesty issue but not severe. Slight preference to keep since the slug is short and the segment-title-vs-substance gap is fixable in the title rather than the slug.
  - **opus-r2b** (opus): -1 *rename* — novelty=0.95, len=178, **subst=-0.98**
    > The bare phrase reads as a topic label, not a definition's subject-noun. The segment names a specific structural commitment (boundary with information loss); the slug should too.

  *substance total (R1 + R2):* 4.33


---

### `effect spiral`

*R2 voters:* 2 (1 architectures: opus)

**Candidate: `effect spiral`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [invented] — n=4, mean=3.00, weights=[+3, +3, +3, +3], categories={canonicalize:4}
  > Memorable without being whimsical. Excellent name for the positive-feedback breakdown mechanism. Per `#der-adversarial-destabilization` and `#deriv-strategic-composition`: positive-feedback breakdown where degraded model causes degraded actions causes further degradation.

- *R2 votes:*
  - **opus-r2c** (opus): +2 ★ *keep* — novelty=0.90, len=321, **subst=1.90**
    > "Spiral" is the right metaphor — the dynamics literally unwind via positive feedback through repeated cycles, each one more degraded than the last. Memorable, evocative, two-syllable. The pair with "runaway mismatch cascade" as add-alias for mechanism is the clean rename-vs-add-alias structure the principles file flags.
  - **opus-r2b** (opus): +1 *keep* — novelty=0.90, len=240, **subst=0.95**
    > Note: this is "effect spiral" — possible typo for "effects spiral" (which is what `#der-adversarial-destabilization` and the principles file use). The plural form is the established phrasing. Keeping +1 as the formal name with note flagged.

  *substance total (R1 + R2):* 4.84

**Candidate: `Runaway mismatch cascade`**
- *R1 synthetic:* **+1** [invented] — n=1, mean=3.00, weights=[+3, +3], categories={add-alias:1, canonicalize:1}
  > Focuses on the mismatch acceleration ($\Vert\delta\Vert \uparrow$). Adopts the formal alias for the effects spiral.

- *R2 votes:*
  - **opus-r2b** (opus): +2 ★ *add-alias* — novelty=0.89, len=447, **subst=1.89**
    > The principles file uses this as its canonical example of an add-alias vote: "Vote add-alias when the original is formally precise or deeply established but the framework needs a separate, evocative prose handle for discussion, framing, and pedagogy." Effects spiral stays as the formal phenomenon name; "runaway mismatch cascade" enters prose as the explanatory phrase. The pair becomes a maintained convention with strictly differentiated roles.
  - **opus-r2c** (opus): +2 *add-alias* — novelty=0.90, len=276, **subst=1.90**
    > Strong add-alias as the *mechanism* phrase that explains *why* the effect spirals: degraded model → degraded actions → degraded model. Pairs with effect spiral as the formal-name / explain-the-mechanism pair the principles file recommends for rename-vs-add-alias distinctions.

  *substance total (R1 + R2):* 4.80

**Candidate: `effects spiral`**
- *R1 synthetic:* — (no R1 evidence)

- *R2 votes:*
  - **opus-r2b** (opus): +2 *keep* — novelty=1.00, len=242, **subst=2.00**
    > Write-in (the corrected plural form). The principles file uses "effects spiral" as the canonical example; the segment row title uses "effect spiral" (singular) which appears to be a typo. The plural form is the project's established phrasing.

  *substance total (R1 + R2):* 2.00

**Candidate: `Adversarial feedback loop`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > Explicitly names the cause (adversarial coupling) and the mechanism (positive feedback).

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.92, len=202, **subst=-0.96**
    > Loses the runaway/positive-feedback character that "spiral" carries. "Loop" in this framework is the topology (per row 51); using "loop" for a runaway dynamic muddies the careful loop/cycle distinction.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.67, len=215, **subst=-0.83**
    > Names the *cause* (adversarial coupling) but the spiral can also occur in non-adversarial settings (any positive-feedback breakdown — mismatch ↑ → action quality ↓ → mismatch ↑). Adversarial-only framing too narrow.

  *substance total (R1 + R2):* -0.79

**Candidate: `Destabilization vortex`**
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={rename:1}
  > A bit more descriptive than spiral but slightly less formal.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.89, len=47, **subst=-0.44**
    > Whimsical without precision gain over "spiral."
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=70, **subst=-0.70**
    > "Vortex" overloads with fluid-dynamics imagery without precision gain.

  *substance total (R1 + R2):* -1.14

**Candidate: `Breakdown cascade`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: same critique. Rejected.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.89, len=49, **subst=-0.46**
    > Same boundedness objection as "Coupling cascade."
  - **opus-r2c** (opus): -1 *rename* — novelty=1.00, len=67, **subst=-0.67**
    > "Cascade" can be bounded; "spiral" carries the runaway sense. Drop.

  *substance total (R1 + R2):* -2.13

**Candidate: `Coupling cascade`**
- *R1 synthetic:* **-1** — n=1, mean=-1.00, weights=[-1], categories={rename:1}
  > Rejection argument: considered as more formal alternative. Loses the *runaway* sense that "spiral" carries — cascades can be bounded; spirals usually aren't. Rejected.

- *R2 votes:*
  - **opus-r2b** (opus): -1 *rename* — novelty=0.74, len=105, **subst=-0.87**
    > Cascades can be bounded; spirals usually aren't. The phenomenon's load-bearing property is unboundedness.
  - **opus-r2c** (opus): -1 *rename* — novelty=0.88, len=100, **subst=-0.94**
    > Same critique as breakdown cascade — "cascade" doesn't carry the runaway dynamic that "spiral" does.

  *substance total (R1 + R2):* -2.81


---

### `Pearl L2`

*R2 voters:* 3 (3 architectures: codex, gemini, opus)

**Candidate: `Exploring`** ▸ leader
- *R1 synthetic:* **0** — n=1, mean=1.00, weights=[+1], categories={add-alias:1}
  > Brief-grade agent-side gloss for Pearl's L2 (interventional). NOT a rename.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *add-alias* — novelty=0.67, len=173, **subst=1.67**
    > Necessary agent-side gloss for Pearl's L2 (interventional). It provides an intuitive English handle for the deliberation phase where actions are taken to gather information.
  - **opus-r2c** (opus): +1 ★ *add-alias* — novelty=0.80, len=471, **subst=0.90**
    > Acceptable agent-side gloss but slightly off — Pearl's L2 is *intervening* / *acting-and-observing-the-consequence*, not just *exploring*. Exploring suggests information-seeking; intervention is broader (any *do*-action carries L2 contrast, including exploitation moves where the agent already believes it knows the consequence). Mild preference: prefer "intervening" over "exploring" for the Brief-grade gloss. Still better than no gloss; vote +1 with reservation noted.
  - **codex-r2b** (codex): -1 *add-alias* — novelty=1.00, len=104, **subst=-1.00**
    > Too narrow. Level 2 is intervention/do-access; the same structure supports exploration and exploitation.

  *substance total (R1 + R2):* 1.57

**Candidate: `Intervening`**
- *R1 synthetic:* — (no R1 evidence)

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *add-alias* — novelty=1.00, len=73, **subst=1.46**
    > Direct agent-side gloss for Pearl L2: "what will I observe if I do this?"

  *substance total (R1 + R2):* 1.46


---

### `recursive update`

*First-encounter locality:* `#der-recursive-update` (Section I; depends on `#form-agent-model`, `#form-event-driven-dynamics`, `#deriv-recursive-update`). First formal derivation; Agent state updates (epistrophe — the corrective turning toward reality) must be recursive: the new model state is a function of the previous model state and the incoming event, not of the full….

*Segment:* [`01-aad-core/src/der-recursive-update.md`](../../01-aad-core/src/der-recursive-update.md)

*R2 voters:* 2 (2 architectures: codex, gemini)

**Candidate: `recursive update`** ▸ leader
- *R1 synthetic:* **+2** [is_keep] [excavated] — n=7, mean=2.29, weights=[+1, +1, +3, +3, +3, +2, +3], categories={canonicalize:7}
  > The subject-noun "recursive update" is exact — the derivation forces the update to be recursive. State updates must be recursive. Keep.

- *R2 votes:*
  - **codex-r2b** (codex): +2 ★ *keep* — novelty=0.88, len=170, **subst=1.88**
    > Exact, standard name for the forced update form $M_{\tau^+}=f_M(M_{\tau^-}, e_\tau)$. The completeness nuance is crucial but belongs in the derivation/status explanation.

  *substance total (R1 + R2):* 3.88

**Candidate: `Recursive update by completeness`**
- *R1 synthetic:* **+1** — n=1, mean=2.00, weights=[+2], categories={rename:1}
  > Title currently understates the distinctive Markov-by-definition move. Auditor: the distinctive content is *"the recursive form is forced by what we mean by $M_t$"* — surface this in the name.

- *R2 votes:*
  - **gemini-r2** (gemini): +2 ★ *name-unnamed* — novelty=0.89, len=271, **subst=1.89**
    > The phrase 'by completeness' is essential. As noted in my adversarial audit, the recursive Markovian form is not a law of physics, but a direct logical consequence of defining $M_t$ as the complete state. Naming the constraint that forces the form is structurally honest.
  - **codex-r2b** (codex): +1 *rename* — novelty=0.83, len=102, **subst=0.91**
    > Names the distinctive Markov-by-complete-state move, but too explanatory as the canonical result name.

  *substance total (R1 + R2):* 3.80


---

