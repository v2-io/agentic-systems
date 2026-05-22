# §1 cluster — working state (2026-05-21)

*Hand-off file for the cluster-sweep cycle responding to `ref/enrichment-candidates-2026-05-21.md`. Authored mid-session at the natural break before reading the remaining §1 papers.*

## State of acquisition

| Paper | File | Status |
|---|---|---|
| Cheung-Piliouras-Tao 2021 (passivity ↔ regret ↔ Poincaré) | `cheung-piliouras-tao-2021-passivity-regret.pdf` | ✅ acquired, read |
| Omidshafiei et al. 2019 (α-Rank / MCC) | `omidshafiei-2019-alpha-rank.pdf` | ✅ acquired, not yet read |
| Balduzzi et al. 2018 (Mechanics of n-Player Differentiable Games — SGA) | `balduzzi-2018-mechanics-n-player-games.pdf` | ✅ acquired, not yet read |
| Letcher et al. 2019 (Differentiable Game Mechanics) | `letcher-2019-differentiable-game-mechanics.pdf` | ✅ acquired, not yet read |
| Candogan-Menache-Ozdaglar-Parrilo 2010 (Flows + Decompositions of Games) | `candogan-flows-alt.pdf` (arxiv 0907.1907, 22pp — the long technical-report version, closest to Math of OR full) | ✅ acquired, not yet read |
| Papadimitriou-Piliouras 2018 (From Nash Equilibria to Chain Recurrent Sets) | `papadimitriou-piliouras-2018-nash-chain-recurrent.pdf` | ✅ extra (Conley-adjacent, surfaced via Relata `chain recurrent`) |
| **Conley 1978** *Isolated Invariant Sets and the Morse Index* (AMS CBMS-RCSM #38) | — | ❌ **not on arXiv** — 78-page AMS monograph; **needs Joseph or institutional access** |
| Patrão 2014 *Existence of complete Lyapunov functions for semiflows…* | — | ❌ arxiv ID 1209.4503 I tried is a **pulsar physics paper, not Patrão's**. The correct arXiv ID is unknown to me; the paper was published in Far East J. Math. Sci. 2011. Open-access status uncertain. |
| Norton 1995 *The Conley decomposition theorem for maps: a metric approach* | — | ❌ *Topology and its Applications* — paywalled |

**Honest correction recorded:** I claimed earlier that `patrao-2014-complete-lyapunov-conley.pdf` was downloaded. It was not — the PDF that landed at that filename was a 34-page paper on Lorentz invariance with binary pulsars (Shao & Wex 2012, arXiv:1209.4503). I have removed the bad file and the spurious claim. The Patrão paper is genuinely not yet acquired.

**Practical resolution:** Omidshafiei 2019 cites Conley's chain-recurrent decomposition directly and will give effectively what the §1.a proposal needs without the original 1978 monograph (the result-statements travel; the original monograph is the historical anchor, not load-bearing for the proposal's mathematical content). Conley's monograph + Norton/Patrão should be tagged in the proposal as **prior-art-citations-only** (the proposal asserts the universality result; the citation is to the monograph that proves it, not a paper this session is verifying line-by-line). If Joseph wants me to grab Conley 1978 (PDF likely via library/inter-library loan or a saved copy he has), I'll ask in a future batch.

## What was learned from CPT 2021

*Full read. Key technical content, in the form a future-session proposal can build on.*

### CPT's setup (one paragraph)

A learning operator converts payoffs $p(t)$ to mixed strategies $x(t) = f(q(t))$ where $q(t) = q^0 + \int_0^t p(\tau) d\tau$ is the cumulative-payoff state. A game operator does the reverse. A dynamical game system (DGS) is the feedback interconnection. **Passivity** of an input-output operator means there exists a *storage function* $L: Z \to \mathbb R$ such that $L(z(t)) \le L(z^0) + \int_0^t \langle u(\tau), y(\tau)\rangle d\tau$. **Lossless** means equality. **Finitely passive/lossless** means $L$ has a finite lower bound (WLOG zero).

### The theorems load-bearing for AAT enrichment

- **Th 2 (Fox-Shamma 2013, composability).** FIC of two passive SSS with storage functions $L_1, L_2$ is passive via $L_1 + L_2$. Lossless ⊗ lossless = lossless. *AAT-relevance:* this is the compositional property AAT needs for the certificate-spine claim about composition — the storage function adds, not the certificate-metric itself. Tells us how `#form-composition-closure`'s closure-defect interacts with passivity-side composition.
- **Th 7.** Every continuous-time FTRL dynamic is finitely lossless. *AAT-relevance:* FTRL families (Multiplicative Weights, gradient descent, replicator) all sit at the **κ=0 boundary** of AAT's certificate cone, with finite storage functions. They are the canonical examples of agents whose certificate exists but doesn't contract.
- **Th 8.** Any finitely passive learning dynamic guarantees **constant regret** (not just $O(\sqrt T)$, *constant*). *AAT-relevance:* the AAT-internal diagnostic for whether the agent's update operator has finite-passive structure is bounded control-regret growth.
- **Prop 17.** A graphical constant-sum game with fully-mixed Nash → game operator is finitely lossless via the *zero* storage function. *AAT-relevance:* gives an exact mathematical home for `#deriv-strategic-composition`'s sub-scope α' constant-sum case + the adversarial limit of `#der-adversarial-destabilization`.
- **Th 19.** Convex combination of FTRL coupled with such a constant-sum game → DGS is Poincaré recurrent in strategy space. *AAT-relevance:* this is the "effects spiral" of `#der-adversarial-destabilization` at its lossless boundary, and the cyclic-distributional R2 regime AAT's dynamic-regime axis (Track A Phase 6) points at. The recurrence is *generic*, not exceptional, at the lossless boundary.

### Mechanism behind Theorem 19 (the bit AAT's R2 work most needs)

1. Lossless ⊗ lossless ⟹ DGS lossless ⟹ $L_1 + L_2$ is a **constant-of-motion**.
2. The game dynamic is **divergence-free** (because game payoff $p_i$ doesn't depend on agent $i$'s own cumulative payoff $q_i$; only on other agents'). Liouville's formula ⟹ volume-preserving.
3. Trajectories stay in level sets of $L_1 + L_2$; level sets are bounded; volume-preserving + bounded orbits ⟹ Poincaré recurrence (Theorem 18, classical).

The mechanism is: **lossless coupling + divergence-free game payoff + bounded level sets ⟹ recurrence, not convergence.** This is a *robust* dynamic regime, not pathology.

## CPT proposal sketch (draft for next session to refine into PROPOSED-ADVANCED.md Phase 3 entry)

**Title (working):** *Lossless Passivity as the Conservative Rung of the Stability-Certificate Cone (Cheung-Piliouras-Tao 2021 enrichment).*

**Gap addressed:** `#disc-stability-certificate` (line 70 + line 119) explicitly leaves open: *"Whether exactly three obstructions exhaust the failure modes is not proved; three are established and each is exact, but exhaustiveness is open"* and *"a fourth (e.g. non-autonomous certificate drift for time-varying systems) is not searched."* The R0 ⟸ R1 ⟸ R2 ladder in `#result-certificate-existence` runs from "widest one-point/local" to "Čencov-forced Fisher metric" but doesn't characterize what happens *at the boundary between certificate-interior and identifiability-floor* — agents whose certificate exists ($\mathcal M\succ 0$) but contracts at rate κ=0. CPT 2021 names that regime exactly: it is the *lossless passivity* regime.

**Direction:** Promote `#result-certificate-existence`'s R0 rung to a **two-sub-rung structure**: R0-strict (κ>0; exponential stability; the current rung) and R0-loss (κ=0; lossless passivity; Poincaré recurrence under coupling-and-boundedness, per CPT Th 19). R0-loss is *not* a failure of the certificate (certificate exists, $\mathcal M\succ 0$); it is a *qualitatively distinct dynamic mode* between "exponentially stable" (R0-strict) and "rank-deficient certificate" (the M1 boundary facet).

**Mechanics:**
1. **Bridge identification (claim):** AAT's one-point sector condition $\langle F(e), e-e^\ast\rangle_\mathcal M \ge \kappa\|e-e^\ast\|^2_\mathcal M$ at the *equality, κ=0* boundary is structurally identical to CPT's passivity inequality at equality. Verify by matching the storage function $L(z)$ to AAT's Lyapunov form $V(e) = e^\top \mathcal M e$ under the agent-class specializations CPT covers (FTRL → replicator, gradient descent, MW).
2. **Add R0-loss to the strength ladder** in `#result-certificate-existence`. R0-loss sits *between* R0-strict and the M1 identifiability-floor boundary — the certificate is $\succ 0$ (so M1 doesn't apply) but contraction is zero (so R0-strict doesn't apply).
3. **Surface the M3-vs-R0-loss distinction.** Helmholtz-failure (M3) names agents whose Jacobian is non-symmetric so no potential exists — the certificate is *matched* (converse-Lyapunov), not *forced* (Čencov). R0-loss names agents whose certificate is forced *and* contracts at zero rate — distinct from M3 (which is about *which* metric, not *what* rate). Worth confirming this is genuinely distinct rather than a refinement.
4. **Effects-spiral upgrade.** `#der-adversarial-destabilization`'s effects-spiral corollary is currently discussion-grade; the joint-Jacobian spectral-abscissa instability condition lives at exactly the lossless boundary. CPT Th 19 + Prop 17 give an exact promotion path for the *constant-sum-game special case*: convex-combination FTRL + graphical-constant-sum game with fully-mixed Nash ⟹ Poincaré recurrent ⟹ no convergence to Nash, infinite cycling, *which is exactly the effects-spiral signature*. Promote discussion-grade → conditional-derived for this sub-scope.
5. **AAT-native control-regret diagnostic.** Theorem 8 contrapositive: unbounded control regret ⟹ learning operator is not finitely passive. This is an empirically falsifiable diagnostic for the certificate-cone position of a real agent's update rule.

**Risks / strengthen-first attempts to make before softening:**
- *Plausible, not verified:* the claim that lossless dynamics live "between" R0-strict and M1 needs proof, not just shape-matching. The first spike under this proposal should formalize the inclusion of regimes and verify R0-loss is genuinely distinct from both R0-strict and the M1 boundary.
- *Watch:* CPT works in continuous-time FTRL. The discrete-time extension (Multiplicative Weights with finite step) is acknowledged as open in CPT §7. AAT's segments are continuous-time, so the immediate proposal is fine, but any logogenic application (`03-llm-core/` — discrete token updates) inherits the open question.
- *Watch:* The Poincaré-recurrence result needs the *divergence-free* game-payoff property (Liouville's formula). General games — including AAT's β' VI-tier sub-scope of `#deriv-strategic-composition` — may not have divergence-free payoff functions. The proposal's reach is exactly the games that do.

**Downstream segment effects:**
- `#result-certificate-existence` Formal Expression: R0-loss row added to the strength-ladder table; ladder becomes R0-loss ⟸ R0-strict ⟸ R1 ⟸ R2 (R0-loss is the *weakest* nontrivial certificate condition — existence with zero contraction; the others strengthen by adding contraction, then global incremental monotonicity, then Čencov forcing).
- `#disc-stability-certificate` Discussion: the "exactly three obstructions" honesty paragraph (line 70) updated to name CPT 2021 as the source of the lossless-boundary regime; the question becomes whether *interior-boundary* dynamics (lossless) are a fourth facet *or* a refinement of the Interior facet. Per the spine's own test ("is a candidate organizing pattern a new facet, or a genuinely new object?") this looks more like the latter — a refinement of the Interior facet (the *interior boundary* where contraction collapses but rank doesn't) — but the proposal should test this.
- `#der-adversarial-destabilization` Discussion + new appendix segment `#deriv-effects-spiral-constant-sum`: the constant-sum-game lossless case lifts effects-spiral from discussion-grade to conditional-derived under CPT Th 19 + Prop 17.
- `#def-control-regret` Discussion: contrapositive of CPT Th 8 added as an AAT-native diagnostic for finite-passive update structure.

**Cross-row unification claim the file author flagged (from `ref/enrichment-candidates-2026-05-21.md` §1.e):** *"AAT's tools across rows 03 / 10 / 14 / 17 are secretly the same."* I have not yet verified what specifically those CSV rows refer to in the prior-art-analysis files — that is a separate check before this proposal lands. If they are: sector-condition (passivity row), adversarial-tempo (effects-spiral row), strategic-composition (regret-shaped row), and CIY/satisfaction-gap (Poincaré-recurrent diagnostic row), then CPT genuinely *is* the unifying mathematical object underneath them.

## What's next (for the next session, in order)

1. **Read Letcher 2019 (Differentiable Game Mechanics) — SGA + continuous Helmholtz.** This is the §1.b + §1.d package. Then Candogan-Menache-Ozdaglar-Parrilo 2010 for the original Hodge/Helmholtz-of-games decomposition. The structural claim to test: AAT's R0-strict regime corresponds to the *potential* (gradient) component of Candogan's decomposition; CPT's lossless / R0-loss regime corresponds to the *harmonic* (conservative) component. Helmholtz/Hodge is then the *exact* decomposition into R0-strict + R0-loss components. If so, this is a structural enrichment of `#disc-stability-certificate`'s Interior facet itself.
2. **Read Omidshafiei 2019 (α-Rank).** Conley chain-recurrent decomposition + MCC as a dynamical solution concept. The structural claim: the *recurrent set* of CPT's lossless DGS is a chain-recurrent set in Conley's sense; MCC is the right solution concept for AAT's R2 cyclic-distributional regime.
3. **Verify the cross-row unification claim** by reading the relevant CSV files (`ref/Prior_art_for_AAT_*.csv`) to identify what rows 03 / 10 / 14 / 17 refer to.
4. **Then write the unified §1 cluster proposal** — one Phase-3 entry in `PROPOSED-ADVANCED.md` covering the full cluster (Conley + Hodge/Helmholtz + CPT + α-Rank + SGA), with five inter-linked rows in `PROPOSED.md` Tier 2. The cluster proposal positions each paper relative to the others rather than five isolated entries.
5. **Decide on PROPOSED.md row placement.** Per the index discipline: each row needs a source pointer. For §1 cluster the natural source pointer is `ref/enrichment-candidates-2026-05-21.md` (the originating document) with detail in the new Phase-3 section of `PROPOSED-ADVANCED.md`. Reciprocal links need to be added to Working Notes of any segment specifically touched (e.g. `#result-certificate-existence` Working Notes mentioning the R0-loss proposal pointer).
6. **Move on to §2 cluster** after §1 is filed.

## Files at `/tmp/aat-enrichment-cluster1/`

All PDFs + extracted text for CPT 2021 are in `/tmp/aat-enrichment-cluster1/`. These are workspace files; once proposals are filed they can be archived or removed.
