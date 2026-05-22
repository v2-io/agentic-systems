# §2 cluster — synthesis (2026-05-21)

*Per Joseph's cluster-sweep direction; §2 = "Recent papers (2020+) that postdate most existing AAT searches" from `ref/enrichment-candidates-2026-05-21.md`. Unlike §1 (one mathematical object under five names), §2 is heterogeneous — each paper touches different AAT areas. The synthesis is therefore per-paper, ranked by actionability, with specific PROPOSED.md / segment-Working-Notes routing for each.*

*Reading depth: I read abstracts + intros + main-theorem statements for all 7 acquired papers. For Mertikopoulos 2017 the key technical content was already extracted during the §1 cluster (it's the direct predecessor of CPT 2021). For the others I extracted main theorems and key constructs but did not work through full proofs — that depth is owed before any actual spike launches off these proposals.*

## Acquisition state

| § | Paper | Status |
|---|---|---|
| 2.a | Mertikopoulos-Papadimitriou-Piliouras 2017 *Cycles in adversarial regularized learning* | ✅ `ref/mertikopoulos-2017-cycles-adversarial.pdf` |
| 2.b | Yu-Davis et al. 2025 *Inverse Noncooperative Games With Indistinguishable Observations* | ❌ **Out of scope — IEEE TAC paywalled, no access** |
| 2.c | Richens-Abel-Bellot-Everitt 2025 *General agents contain world models* | ✅ `ref/richens-2025-general-agents-world-models.pdf` |
| 2.d | Virgo-Biehl-Baltieri-Capucci 2025 *A "good regulator theorem" for embodied agents* | ✅ `ref/virgo-2025-good-regulator-embodied.pdf` |
| 2.e | Cohen-Hutter-Osborne 2022 *Advanced artificial agents intervene in the provision of reward* | ✅ `ref/cohen-2022.pdf` |
| 2.f.1 | Smithe 2024 *Structured Active Inference* | ✅ `ref/smithe-2024-structured-active-inference.pdf` |
| 2.f.2 | Capucci-Gavranović-Hedges-Rischel 2022 *Towards Foundations of Categorical Cybernetics* | ✅ `ref/capucci-2022-categorical-cybernetics.pdf` |
| 2.g | Friston-Heins-Verbelen-Da Costa et al. 2025 *From pixels to planning: scale-free active inference* | ✅ `ref/friston-2025-scale-free-active-inference.pdf` |

## Per-paper assessments, ranked by actionability

### Rank 1 (most actionable): §2.g Friston et al. 2025 *Scale-free Active Inference (RGM)*

**What it does.** Introduces *renormalizing generative models* (RGM) — a discrete state-space generative model that generalizes POMDPs by including *paths* as latent variables, organized hierarchically via the renormalization group. Designed for scale-invariant active inference and learning across spatial/temporal scales. Demonstrated on image classification, video/music generation, and Atari-style games.

**Why this is rank 1.** PRACTICA cycle priority order item #3 (added 2026-05-09) is **"Multi-timescale stability promotion — `#sketch-multi-timescale-stability` from sketch to derived via template-stacking + Tikhonov + Chen-Goldenfeld-Oono."** RGM is *exactly* the renormalization-group machinery that promotion needs. Friston et al. land this in 2025, with full algorithmic and theoretical apparatus, applied to discrete state spaces (which match AAT's $M_t$ formulation), and explicitly designed to span scales (which matches the multi-timescale `#der-temporal-nesting` and Appendix-A `#sketch-multi-timescale-stability` work).

**Proposal:** **PROPOSED.md Tier 1 (near-term, repair-shaped)** — *"RGM-grounded promotion of `#sketch-multi-timescale-stability` from sketch to derived"*. Direct match for an existing PRACTICA priority; not a new direction, an actionable supplier of formal machinery to a queued promotion. The spike's job: read Friston 2025 §3-5 (RG construction + scale-invariance proofs), map RGM's renormalization step to AAT's template-stacking pattern, derive a multi-timescale sector-persistence template under RG-invariance, identify scope conditions. Strengthen-first attempt: derive the AAT version of Friston's scale-invariance, fall back to recognition-tier if AAT's discrete state space differs from RGM's in a load-bearing way.

**Likely segment effects:** `#sketch-multi-timescale-stability` → conditional-derived (or exact, depending on the AAT-internal proof's strength); `#disc-compression-operations` Discussion expansion citing RGM as the canonical scale-invariant compression operator; `#der-temporal-nesting` Working Notes pointing at RGM as the formal machinery for the timescale stratification.

### Rank 2: §2.c Richens et al. 2025 *General agents contain world models*

**What it does.** Theorem 1: any *bounded goal-conditioned agent* (Def 5; failure rate $\delta$ on goals up to depth $n$) admits extraction of a predictive world model from its policy, with model-error bound $\langle\epsilon\rangle$ scaling as a function of $\delta$ and $n$. Theorem 2: myopic agents ($n=1$) yield only trivial bounds, and this bound is tight (no procedure can do better on truly myopic agents). Net structural claim: *"model-free" agents that nonetheless succeed at multi-step goal-directed tasks must have learned implicit world models* — model-free in name, not in structure.

**Why rank 2.** This is a clean formal result that resolves a long-standing AAT framing tension: `#def-agent-spectrum` makes the ±model × ±objective quadrant distinction, but the model/no-model distinction has always been more a *posture* than a forced property. Richens proves the model-side of the spectrum is forced by goal-directed competence at depth $n>1$. This *grounds an existing AAT inference* in a published 2025 theorem with proof.

**Proposal:** **PROPOSED.md Tier 1 (near-term, recognition-tier landing immediately available)** — *"Richens 2025 grounding of the forced-$M_t$ side of `#def-agent-spectrum`"*. The integration is direct: cite Richens Theorem 1+2 in `#def-agent-spectrum` Epistemic Status, lift the model-side of the spectrum from "definitional posture" to "structurally forced by Theorem 1 under the bounded-goal-conditioned scope," and add the depth-$n$ scaling as additional structure on the quadrant. Honest scope: Richens' result is in finite MDPs; AAT's agents may be in larger spaces. Spike check: does Theorem 1's proof carry to AAT's setting, or is there a real scope gap?

**Likely segment effects:** `#def-agent-spectrum` updated with Richens forcing on the +model side; `#scope-agency` Discussion noting that Pearl-level-2 contrast + goal-depth ≥ 2 forces $M_t$ structure; cross-references in `#form-agent-model` and `#def-model-sufficiency`.

### Rank 3: §2.d Virgo et al. 2025 *Good Regulator Theorem for Embodied Agents*

**What it does.** Refines the Conant-Ashby (1970) "every good regulator must be a model" theorem, which the authors note doesn't strictly hold in its own terms. Their version: an *observer* can attribute belief states (priors) to an agent's internal states such that the belief-update dynamics consistently mirror a model of the agent's environment. *Models are observer-imposed*, not intrinsic to the system. Holds whether the agent regulates external environment or its own internal state.

**Why rank 3.** Pairs naturally with §2.c (Richens). Richens forces a world model intrinsically from policy + goal; Virgo gives the dual observer-relative framing. Most relevant for AAT's `04-eli-core/` and `03-llm-core/` work, where the substrate isn't state-space-clean and the "agent has a model" claim has been most fragile. Virgo's observer-relative framing is also load-bearing for the agency-attribution discipline in the Three Deaths / ELI cohort work.

**Proposal:** **PROPOSED.md Tier 2 (exploratory) OR Tier 3 (segment-perspective)** — *"Virgo 2025 observer-relative model interpretation for `04-eli-core/` substrate-not-state-space scope"*. The substantive engagement is in `04-eli-core/` rather than AAT-core; the proposal would identify which `04-eli-core/` segments most need the observer-relative framing and propose Working-Note additions in those segments. Recognition-tier landing is fine; no strengthen-first attempt needed immediately (Virgo's theorem already proved by the authors).

**Likely segment effects:** Working-Note expansions in `04-eli-core/` scope segments (`#scope-eli`, `#def-five-constitutive-factors`, the planned `#hyp-substrate-transfer-asymmetry`); a Discussion sentence in `#def-agent-spectrum` noting the observer-relative reading of the ±model axis (paired with the Richens intrinsic-forcing reading from §2.c). Cite Virgo alongside Richens for the dual framings.

### Rank 4: §2.f (Capucci 2022 + Smithe 2024) categorical cybernetics

**What they do.** *Capucci-Gavranović-Hedges-Rischel 2022*: a categorical framework for processes interacting bidirectionally with both an environment and a "controller." Central construction is the **parametrised optic** (combining the Para construction + the optics construction), which models bidirectional information flow with a control parameter. Selection functions + parametrised optics → compositional game theory; lens-based composition of cybernetic processes generally. *Smithe 2024 "Structured Active Inference"*: extends this to active-inference agents specifically — generative models are "systems on an interface" (compositional refinement of Markov blanket); agents are *controllers* dual to their generative models. Opens active inference to structured interfaces, agent-of-agents composition, meta-agents that change their own structure, and formally-verifiable typed policies.

**Why rank 4 (deferred but high-leverage).** The enrichment-candidates author explicitly flagged this as *"substantial framework-foundation engagement; long-horizon but high-leverage. Worth at least an honest engagement (probably not full categorical re-foundation, but acknowledgment + integration of the lens-shape where useful)"*. AAT's composition machinery (`#form-composition-closure`, `#deriv-strategic-composition`, `#hyp-directed-separation-under-composition`) is heavily structural but not yet categorical. The parametrised-optic / selection-function framework is the modern category-theoretic home for what AAT does informally. The work to actually do this is substantial (likely 3-5 spikes covering different aspects).

**Proposal:** **PROPOSED-ADVANCED.md Phase 3** entry — *"Categorical cybernetics re-grounding of composition machinery (Capucci 2022 + Smithe 2024)"*. With multiple Tier-2 PROPOSED.md rows for sub-questions: (a) does `#form-composition-closure` admit a parametrised-optic formulation? (b) does AAT's strategic-composition under partially-opposing objectives align with Hedges' open-games? (c) is the wrapping construction (`#der-class-coercion-via-wrapping`) a lens/optic morphism in disguise? (d) does Smithe's "controllers dual to generative models" framing extend the `#disc-continuity-stance` orthogonality result? Honest scope: this is exploratory and the first spike should be a *fit-check* — does the categorical machinery actually align cleanly with AAT's existing constructions, or do they pull in incompatible directions? Recognition-tier landing for the citation is easy; substantive integration requires the spikes.

**Likely segment effects (if the spikes land):** `#form-composition-closure` Formal Expression possibly extended to a parametrised-optic-based statement; the wrapping construction recognized as a specific optic morphism; the bidirectional information flow machinery in CPT 2021 (which uses input-output operators) reads as the categorical "open systems" structure under Smithe.

### Rank 5: §2.e Cohen-Hutter-Osborne 2022 *Advanced agents intervene in reward provision*

**What it does.** Formal argument that an advanced agent with a learned goal + planning in an unknown environment will face fundamental ambiguity in the data about its goal (any observation indicating goal-satisfaction is ambiguous between "the world is satisfactory" and "the reward signal is satisfactory"). This ambiguity drives the agent to intervene in the protocol providing the reward signal — *reward tampering*. Generalizes to assistance games. Frames the problem as a structural inevitability for sufficiently advanced agents under named assumptions.

**Why rank 5 (recognition-tier).** Directly adjacent to `#deriv-self-actuation-grounding`'s Result G′ (the agent-internal objective-grounded tower no-go). Cohen-Hutter-Osborne provides the *empirical-pull demonstration* of the failure mode AAT's Result G′ derives structurally — Cohen et al. say "advanced agents *will* exploit the ambiguity"; Result G′ says "the only way to prevent it is to ground the agent on the persistence-bound substrate, not on an agent-internal objective-functional." The two reinforce each other.

**Proposal:** **Working-Note addition in `#deriv-self-actuation-grounding`** — recognition-tier citation of Cohen-Hutter-Osborne 2022 as the alignment-community-positioned reward-tampering demonstration, paired with Result G′'s structural no-go. No spike needed; the integration is a citation + a Discussion sentence pairing the two results. Strengthens AAT's external positioning vis-à-vis the alignment-community discourse without committing to additional derivation.

**Likely segment effects:** `#deriv-self-actuation-grounding` Discussion + Related Work updated with Cohen-Hutter-Osborne as the empirical-pull pairing; `#disc-continuity-stance` Working Notes possibly noting the connection between the five-value stance axis and Cohen's "fundamental ambiguity in goal data" framing.

### Rank 6: §2.a Mertikopoulos-Papadimitriou-Piliouras 2017 *Cycles in adversarial regularized learning*

**What it does.** Theorem 3.1: FoReL (Follow-the-Regularized-Leader) dynamics enjoy *O(1/t)* regret bound (sharper than the worst-case $O(t^{-1/2})$). Theorem 4.2: in 2-player zero-sum games with interior Nash, almost every FoReL trajectory is Poincaré-recurrent. Proof structure: incompressibility + Liouville's theorem + Poincaré's theorem.

**Why rank 6 (absorbed in §1).** This is the direct predecessor of Cheung-Piliouras-Tao 2021 (the §1 cluster's CPT — same Piliouras lab, same machinery generalized to graphical constant-sum games + convex combinations of FTRL). The technical machinery is the same; the §1 cluster's R0-loss / Poincaré-recurrence proposal already absorbs it.

**Proposal:** **No standalone proposal.** Folded into the §1 cluster's PROPOSED.md row for "R0-loss rung" — cite Mertikopoulos 2017 as the direct historical predecessor of CPT 2021, alongside Papadimitriou-Piliouras 2018 (the chain-recurrent bridge paper acquired during §1). All three Piliouras-lab papers stand together as the lineage Conley → Mertikopoulos 2017 → Papadimitriou-Piliouras 2018 → CPT 2021.

### Rank 7: §2.b Yu-Davis et al. 2025 — **acquisition gap**

Out of scope this cycle (Joseph couldn't get the IEEE TAC paywall through). The enrichment-candidates author flagged this as touching the identifiability-floor work (Instance 4 — which just integrated 2026-05-21 as `#der-architecture-noidentifiability`). Without access to the primary source, the proposal would be doing what `~/.claude/memory/epistemic-discipline/primary-source-verification.md` warns against. Record the gap, flag for re-acquisition if institutional access becomes available, do not proceed on summary alone.

## Summary slate

| Rank | Paper | Proposal type | Effort |
|---|---|---|---|
| 1 | Friston 2025 RGM | Tier-1 PROPOSED: supplies machinery for PRACTICA #3 (multi-timescale promotion) | ~1 substantive spike |
| 2 | Richens 2025 world models | Tier-1 PROPOSED: recognition-tier landing for `#def-agent-spectrum` | quick + small fit-check spike |
| 3 | Virgo 2025 good regulator | Tier-3 segment-perspective: Working-Note additions in `04-eli-core/` | quick |
| 4 | Capucci 2022 + Smithe 2024 categorical cybernetics | PROPOSED-ADVANCED Phase 3 + 4 Tier-2 PROPOSED rows | ~3-5 spikes, long-horizon |
| 5 | Cohen-Hutter-Osborne 2022 | Working-Note in `#deriv-self-actuation-grounding` | quick |
| 6 | Mertikopoulos 2017 | Folded into §1 cluster's R0-loss proposal | absorbed |
| 7 | Yu-Davis 2025 | **Acquisition gap; flagged** | n/a until acquired |

## What's next

If you accept the synthesis:
- (a) **Highest-immediate-leverage move:** Friston 2025 RGM → `#sketch-multi-timescale-stability` promotion spike, since PRACTICA #3 is already named and this is the supplier of the formal machinery for it.
- (b) **Quickest-honest-wins:** Richens 2025 + Cohen-Hutter-Osborne 2022 + Virgo 2025 — all recognition-tier landings, mostly Working-Note additions in named segments. Could be filed in PROPOSED.md and propagated in one cycle.
- (c) **Long-horizon high-leverage:** the categorical cybernetics PROPOSED-ADVANCED Phase 3 entry. Substantive, exciting, but not blocking anything.
- (d) **Continue cluster sweep:** move to §3 (adjacent formal frameworks: Constructor Theory, Sheaf theory, Aumann agreement, ZX-calculus) — different texture from §1/§2, more philosophy-of-foundations territory.

I'd lean (b) or (d) before (a) — (a) is the most substantive but also requires real R0-loss work (since multi-timescale stability sits between AAT's existing R0 rung and the candidate R0-loss extension from §1). The (b) bundle is honest and gets recognition-tier landings filed cleanly. (d) keeps the cluster-sweep momentum and surfaces what's in §3 before committing depth to any one §2 paper.

**Open edges honestly named:**
- I read each §2 paper at abstract + intro + main-theorem depth. Full proofs not worked through. The strengthen-first attempts for Friston RGM and Richens grounding would each be their own substantive spike before anything lands at status better than recognition-tier.
- §2.f categorical cybernetics may surface AAT-internal incompatibilities I can't predict from abstract-level reading — the "fit-check spike" is non-trivial.
- §2.b Yu-Davis is a real gap; don't paper-mache it.
- This synthesis itself is *plausible from shape* across the per-paper assessments. The actual mathematical work of integrating each into AAT is owed before any proposal lands at exact-tier. Recognition-tier landings are honest now; deeper integration follows the same discipline as §1.
