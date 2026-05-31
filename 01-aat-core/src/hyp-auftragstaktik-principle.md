---
slug: hyp-auftragstaktik-principle
type: hypothesis
status: discussion-grade
depends:
  - def-shared-intent
  - def-unity-dimensions
  - def-adaptive-tempo
stage: draft
---

# Hypothesis: Auftragstaktik Principle

A bandwidth-allocation hypothesis grounded in the shared-intent IB framework (`#def-shared-intent`). For a composite agent with limited communication bandwidth, the optimal allocation prioritizes sharing **objectives over strategies over models** — $B_O \gt B_\Sigma \gt B_M$. This captures the structural insight of *Auftragstaktik* (mission-type tactics): investing communication bandwidth in shared purpose (teleological unity) while accepting lower epistemic and strategic unity, granting sub-agents autonomy to adapt locally. The model predicts the same priority ordering that military doctrine discovered empirically over centuries — and the framework offers it as a *structural prediction*, not an organizational convention.

The priority ordering follows from the IB framework: the bits with the longest shelf life and highest coordination value per bit should be transmitted first. Objectives change slowly and enable autonomous coordination — sub-agents who share objectives can independently choose compatible strategies. Models change fast and provide diminishing coordination value — two agents with the same model but different objectives still conflict. The ordering holds under stated conditions: objectives change slowly relative to strategies, which change slowly relative to models; sub-agents have sufficient local adaptive capacity to maintain their own models.

The framework is also explicit about *when the ordering reverses*. When the environment is genuinely ambiguous and local observations are insufficient (fog of war, novel codebase, unprecedented market conditions), model synchronization may be worth more than objective sharing — sub-agents who share the same wrong model at least err consistently, which is sometimes better than each having a different wrong model. The framework predicts the reversal as a *regime-dependent prescription* rather than a universal ordering.

The status is *discussion-grade*. The priority ordering is a qualitative prediction supported by extensive military-organizational evidence (Bungay's analysis of Clausewitz, Wehrmacht doctrine, modern mission command), but it is not derived — the IB optimization would need to be solved explicitly with realistic cost functions to confirm the ordering. The empirical evidence is strong but comes primarily from one domain (military command); generalization to software teams, AI agent swarms, and other settings is plausible but unverified. Whether the IB-optimal-bandwidth-allocation *mechanism* is actually the reason Auftragstaktik works empirically — versus other mechanisms (psychological, organizational, traditional) — is an open question.

## Formal Expression

*[Hypothesis (auftragstaktik-principle)]*

Let a composite agent's total inter-agent communication bandwidth be $B = B_O + B_\Sigma + B_M$, allocated across objective sharing ($B_O$), strategy coordination ($B_\Sigma$), and model synchronization ($B_M$).

The hypothesis: the allocation that maximizes composite tempo $\mathcal{T}_c$ (or equivalently, minimizes coordination overhead $C_{\text{coord}}$) prioritizes:

$$B_O \gt B_\Sigma \gt B_M$$

when:
- Objectives change slowly relative to strategies: $\nu_O \ll \nu_\Sigma$
- Strategies change slowly relative to models: $\nu_\Sigma \ll \nu_M$
- Sub-agents have sufficient local adaptive capacity: each $\mathcal{T}_i \gt \rho_i^{\text{local}} / \Vert\delta_{\text{critical}}^i\Vert$

The priority ordering follows from the IB framework ( #def-shared-intent): the bits with the longest shelf life and highest coordination value per bit should be transmitted first. Objectives change slowly and enable autonomous coordination (sub-agents who share objectives can independently choose compatible strategies). Models change fast and provide diminishing coordination value (two agents with the same model but different objectives still conflict).

## Epistemic Status

*Discussion-grade.* Max attainable: empirical. The priority ordering is a qualitative prediction grounded in the IB framework and supported by extensive military-organizational evidence (Bungay's analysis of Clausewitz, Wehrmacht doctrine, modern mission command). But it is not derived — the IB optimization would need to be solved explicitly with realistic cost functions to confirm the ordering, and the conditions under which the ordering reverses (e.g., when model synchronization is critical because the situation is genuinely ambiguous) are not characterized. The empirical evidence is strong but comes primarily from one domain (military command); generalization to software teams, AI agent swarms, and other settings is plausible but unverified.

## Discussion

**When the ordering reverses.** The prioritization $B_O \gt B_\Sigma \gt B_M$ assumes sub-agents can independently construct adequate local models. When the environment is genuinely ambiguous and local observations are insufficient (fog of war, novel codebase, unprecedented market conditions), model synchronization may be worth more than objective sharing — sub-agents who share the same wrong model at least err consistently, which is sometimes better than each having a different wrong model.

**Bungay's evidence.** In *The Art of Action*, Bungay documents that organizations consistently fail by inverting this priority: they over-invest in controlling *how* subordinates act (strategy sharing, $B_\Sigma$) rather than ensuring subordinates understand *why* (objective sharing, $B_O$). The result: subordinates who follow instructions precisely but cannot adapt when conditions change, because they lack the teleological context to improvise intelligently.

**The software team instantiation.** A well-functioning development team has:
- High $B_O$: clear product goals, understood by all (sprint goals, feature objectives)
- Moderate $B_\Sigma$: architectural decisions shared, implementation details autonomous
- Low $B_M$: each developer builds their own mental model of the code they touch; full codebase understanding is neither expected nor efficient

When this inverts (micromanagement of implementation details, unclear product goals), team tempo drops — consistent with the Auftragstaktik prediction.

**Connection to Conway's Law.** Conway's Law (system structure mirrors communication structure) is a consequence: when $B_\Sigma$ is low and $B_O$ is high, sub-agents coordinate through shared objectives rather than explicit action coordination, producing systems whose boundaries reflect objective decomposition rather than communication channels.

## Working Notes
- The formal IB derivation of the priority ordering would need: (1) a model of how each unity dimension contributes to composite tempo, (2) the rate of change of each shared quantity ($\nu_O$, $\nu_\Sigma$, $\nu_M$), (3) the communication cost per bit for each type. The qualitative argument is that objectives are compact and slow-changing (high bits-per-cost, long shelf life), while models are large and fast-changing (low bits-per-cost, short shelf life). Formalizing this is tractable but has not been done.
- The principle may need qualification for AI agent teams where model synchronization is cheap (shared vector databases, persistent memory) but objective alignment is hard (prompt engineering, RLHF). The cost structure differs from human organizations.

### Incidental audit gold (lift 2026-05-31)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical / framing material, kept separate from the certified theory-fix findings (the marginal-vs-total-allocation findings F162–F166 from AUDIT-WORKING-526815 are routed for adjudication — see the off-ramp note at the end). **Coverage:** two dirs carry a dedicated reflection (526815, 849201). Substrate attribution inferred from voice where not explicit.

#### 1. Candidate Brief prose / pre-prose

- The plain payoff: the segment "provides an information-theoretic justification for Mission Command / Agile methodologies" and "proves why micromanagement fails in volatile environments" (Claude, AUDIT-WORKING-849201). Candidate Brief framing.
- The shelf-life mechanism in one line: because objectives change slowly ($\nu_O \ll \nu_\Sigma \ll \nu_M$), "sending them provides a long 'shelf life' for the communicated bits" — the bandwidth allocation as a knapsack problem, maximize coordination value subject to bandwidth $B$ (Claude, AUDIT-WORKING-849201).

#### 2. Candidate Discussion (and the standout forward-vision)

- **AI agent teams plausibly *invert* the human Auftragstaktik ordering (the standout reach here).** For humans, $B_M$ (transmitting your entire mental model) is effectively impossible while $B_O$ ("take that hill") is cheap — hence objective-first. For AI agents the cost structure flips: $B_M$ is cheap (share the vector database, synchronize weights) while $B_O$ is notoriously hard (the alignment problem / RLHF). "The theory naturally predicts that multi-AI systems will optimally organize themselves very differently than human organizations" — the ordering is dictated by the *relative costs*, which are hardware/substrate-dependent, not by the human-derived $B_O \gt B_\Sigma \gt B_M$ template (Claude, AUDIT-WORKING-849201). This is high-value forward-vision pointing at the multi-AI-safety / composite-ELI program; the existing second Working Note states the cost-structure asymmetry, and this elaborates it into a concrete prediction worth promoting. *(Verify before promotion: that "synchronize weights = cheap $B_M$" survives the directed-separation and identity constraints elsewhere in the framework.)*
- **Empirical grounding in Prussian/military organizational history.** The reference to Stephen Bungay's *The Art of Action* grounds the abstract IB ordering in "200 years of Prussian/military organizational empirical data" (Claude, AUDIT-WORKING-849201) — a candidate citation/anchor for the Discussion's organizational-doctrine paragraph.

#### 3. Follow-up items

- **Do not blindly import the human ordering into software/AI architectures.** When the theory is applied to AI teams, the math dictates the ordering from relative communication costs, which are substrate-dependent — a watch-item for downstream applications (Claude, AUDIT-WORKING-849201). Pairs with the inversion insight above.

#### 4. Readers often ask / wonder

- **How does the theory define "trust" mathematically?** A natural bridge question this segment raises and #hyp-communication-gain answers (Claude, AUDIT-WORKING-849201) — useful as a forward pointer at the end of this segment.

#### Off-ramp (NOT gold — routed to certified-findings track)

- AUDIT-WORKING-526815 raised findings on this segment that are strengthen-first / scope-precision candidates, flagged here only so they are not lost: **F162** — $B_O \gt B_\Sigma \gt B_M$ "confuses priority ordering with total bandwidth allocation"; IB reasoning supports sending high-marginal-value, long-shelf-life objective bits *first*, but does not imply the total number of objective bits must exceed strategy or model bits (restate as "prioritize objective information at the margin under scarce bandwidth"); **F163** — maximizing composite tempo and minimizing coordination overhead are not equivalent in general; **F164** (soft) — the ordering depends on strong assumptions about entropy, change rates, and local observability, and the formal statement should be explicitly marginal and conditional; **F165** (soft) — the Conway's-Law claim is too strong as stated (deriving objective-decomposition boundaries from high $B_O$/low $B_\Sigma$ needs additional organizational/design assumptions); **F166** (watch) — the principle inherits the unresolved IB-formalization issues from #def-shared-intent; keep discussion-grade until the relevance variable and encoder are specified. *These are scope-precision tightenings, not no-gos; routed for adjudication on the strengthen-first track.*
