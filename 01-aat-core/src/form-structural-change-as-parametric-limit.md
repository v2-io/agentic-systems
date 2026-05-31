---
slug: form-structural-change-as-parametric-limit
type: formulation
status: robust-qualitative
depends:
  - def-strategy-dag
  - result-structural-adaptation-necessity
stage: draft
---

# Formulation: Structural Change as Parametric Limit

A formulation move that dissolves the sharp line between parametric update (adjusting weights) and structural change (adding/removing edges). In the probabilistic DAG, "structural" changes to $\Sigma_t$ are *continuous operations on edge weights and node sets* — not a separate mechanism. Pruning is a credence dropping below threshold; **strategic grafting** is a new causal hypothesis initialized at a prior. The framework presents six operations on the strategy DAG ordered by typical frequency, from most to least frequent: edge reweighting, $\gamma$ reclassification (AND↔OR), pruning, strategic grafting, objective revision, and full restructure. A healthy agent does continuous strategic maintenance (reweight, occasionally prune and graft) and rarely reaches catastrophic restructuring. *Full restructure is the strategic analog of #result-structural-adaptation-necessity's model-class change* — the rare, expensive event when the entire representational structure must be replaced. *(The unqualified term "grafting" — familiar from horticulture, graph rewriting, and decision-tree learning — is sanctioned in-segment shorthand for "strategic grafting" once the canonical compound has been introduced.)*

The key insight is that this extreme case is the *limit* of the continuous process, not a separate mechanism. An agent that maintains healthy strategic hygiene rarely needs full restructure; an agent that neglects maintenance — letting failing branches persist, ignoring negative evidence — accumulates *strategic debt* until catastrophic restructuring becomes unavoidable. Miller (2022, *Ex Machina*) provides a constructive existence proof for exactly this bridge in finite-state automata: a sequence of *neutral mutations* (alterations affecting only inaccessible regions of state space) can transform a Moore machine from one behavioral equivalence class to a structurally different one without ever changing its observable behavior — until a single additional mutation opens a transition to the restructured region, causing a radical behavioral change (the *extreme transition motif*: neutral invasion → neutral drift → niche creation → cascading displacement → consolidation). The strategy-DAG analog: edges with near-zero credence ($p_{ij} \approx 0$) are the *latent structure* — they consume minimal cognitive cost ( #form-strategy-complexity-cost) but represent alternative causal hypotheses that become load-bearing if circumstances change. An agent that prunes all low-credence edges for efficiency loses this latent diversity and becomes *brittle to regime change*.

The framework also distinguishes *within-agent* grafting from *cross-agent* grafting. Within-agent grafting incorporates a new causal hypothesis into the agent's own $\Sigma_t$ (source: internal model, external information, or exploration — a stimulus rather than an integrating party). When the grafted structure originates in *another* agent and that agent's objective is also absorbed in the process, the mechanism is **symbiogenic composition** ( #hyp-symbiogenic-composition) — a bilateral cross-agent process treated separately in Part III. Biological example: mitochondria integrating into a host cell. Social analog: firm acquisitions integrate processes and decision-making authority simultaneously.

## Formal Expression

*[Formulation (structural-change-as-parametric-limit)]*

The six operations on $\Sigma_t$, ordered from most to least frequent:

| Operation | What changes | Trigger |
|-----------|-------------|---------|
| Reweighting | Edge credence $p_{ij}$ | New observation about the link ( #hyp-edge-update-via-gain) |
| $\gamma$ reclassification | Node combination type AND↔OR | Strong structural evidence that combination semantics changed |
| Pruning | Remove failed branch ($p_{ij} \to \approx 0$) | Credence drops below viability threshold |
| Strategic grafting | Add new branch ($0 \to p_{ij}$) | Discovery of a new possible path (initialized at prior) |
| Objective revision | Change terminal nodes | Feasibility failure or opportunity ( #def-satisfaction-gap) |
| Full restructure | Replace entire $\Sigma_t$ | Catastrophic failure ( #result-structural-adaptation-necessity) |

A healthy agent does continuous strategic maintenance (reweight, occasionally prune and graft) and rarely reaches catastrophic restructuring. Full restructure is the strategic analog of #result-structural-adaptation-necessity's model-class change — the rare, expensive event when the entire representational structure must be replaced.

## Epistemic Status

*Robust qualitative.* The continuity claim (structural change as parametric limit) is a property of the probabilistic representation: in a space where edges carry real-valued credences, adding or removing an edge is a boundary event, not a discontinuity. The frequency ordering of operations is an empirical pattern, not a derived result — it's consistent with the observation that deeper changes (restructuring > pruning > reweighting) require more evidence and are more costly.

## Discussion

**Connection to structural-adaptation necessity.** #result-structural-adaptation-necessity describes the rare case when the entire model class must be replaced — the agent's representational framework is fundamentally inadequate. In the strategy DAG, this corresponds to full restructure: the causal theory encoded in $\Sigma_t$ is so wrong that incremental revision (reweighting, pruning) cannot fix it. The DAG must be rebuilt from a different starting point.

The key insight is that this extreme case is the *limit* of the continuous process, not a separate mechanism. An agent that maintains healthy strategic hygiene (regular reweighting, timely pruning of failing branches, proactive grafting of alternatives) will rarely need full restructure. An agent that neglects maintenance — letting failing branches persist, ignoring negative evidence — accumulates strategic debt until catastrophic restructuring becomes unavoidable.

**Neutral variation as the constructive bridge.** This segment claims that radical restructuring is the *limit* of continuous operations, but the mechanism by which small changes accumulate into radical transformation was unspecified. Miller (2022, *Ex Machina*) provides a constructive existence proof for exactly this bridge in finite-state automata. In Moore machines, each state has accessible and inaccessible regions. A mutation that alters a transition into an inaccessible region is *neutral* — the machine's observable behavior is unchanged because those states are never visited. But such mutations alter the machine's *latent structure*: they change what the machine *would do* if novel inputs were encountered. A sequence of neutral mutations can transform a machine from one behavioral equivalence class to a structurally different one without ever changing its observable behavior — until a single additional mutation opens a transition to the restructured region, causing a radical behavioral change. In Miller's terminology, this is the *extreme transition motif*: neutral invasion → neutral drift → niche creation → cascading displacement → consolidation. The automaton setting makes the mechanism precise: "inaccessible states" are the formal representation of latent structural capacity, "neutral mutations" are the incremental changes, and "a transition opening to a previously inaccessible region" is the parametric-limit event where continuous change produces discontinuous behavioral effect. The strategy-DAG analog: edges with near-zero credence ($p_{ij} \approx 0$) are the latent structure. They consume minimal cognitive cost ( #form-strategy-complexity-cost) but represent alternative causal hypotheses that become load-bearing if circumstances change. An agent that prunes all low-credence edges for efficiency loses this latent diversity and becomes brittle to regime change.

**Pruning and grafting thresholds.** When should the agent prune (remove an edge with very low credence) rather than just keeping it at low $p_{ij}$? The answer involves the cognitive cost of maintaining edges in $\Sigma_t$ — each edge consumes representational capacity and evaluation time. For agents with bounded representational capacity (LLMs with finite context windows), pruning is necessary to keep $\Sigma_t$ within capacity. The threshold is domain-dependent and connects to the open question of cognitive cost of $\Sigma_t$ ( #def-strategy-dimension Working Notes).

**Cross-agent grafting: symbiogenic composition.** The grafting operation above is within-agent — the agent incorporates a new causal hypothesis into its own $\Sigma_t$, with the source (internal model, external information, exploration) being a stimulus rather than an integrating party. When the grafted structure originates in *another* agent and that agent's objective is also absorbed in the process, the mechanism is symbiogenic composition ( #hyp-symbiogenic-composition) — a bilateral cross-agent process rather than a unilateral within-agent operation. Biological example: mitochondria integrating into a host cell transfers gene-based structure (grafting on the host side) *and* subsumes the endosymbiont's independent objective (outside the scope of this segment's operations). Social analog: firm acquisitions integrate processes and decision-making authority simultaneously. The within-agent grafting operation is the host-side component of symbiogenesis, but symbiogenesis as a whole is governed by additional dynamics captured in #hyp-symbiogenic-composition.

## Working Notes

- The timescale ordering (reweight ≫ reclassify ≫ prune/graft ≫ revise $O_t$ ≫ full restructure) is an empirical observation that should be testable. In software development: edge reweighting ≈ updating confidence after a test passes/fails; $\gamma$ reclassification ≈ realizing two tasks are both required (not alternatives); pruning ≈ abandoning an approach that isn't working; grafting ≈ discovering a new approach; objective revision ≈ changing the feature scope; full restructure ≈ starting the project over.
- Grafting (adding new edges) is qualitatively different from other operations because it requires the agent to hypothesize a causal relationship that isn't in its current $\Sigma_t$. Where do new causal hypotheses come from? From $M_t$ (the model suggests a possible path), from external sources ( #hyp-communication-gain — another agent suggests an approach), or from exploration ( #def-causal-information-yield — the agent discovers an unexpected effect). This is the creative step in strategic revision.

### Incidental audit gold (lift 2026-05-31, batch A9)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. *Orthogonal* material (pedagogical framing, analogies, candidate figures, reader-confusion signals), staged for an eventual careful promotion pass, kept separate from the certified theory-fix findings. **Coverage for this segment:** 361742, 471203, 526815, 584721, 773921, 829314.

#### 1. Candidate Brief prose / pre-prose

- **"Perfect efficiency is perfect brittleness."** The convergent one-liner for the latent-diversity result: an agent that prunes *every* low-credence edge to save representation cost becomes optimally fitted to the current environment and helpless under a regime shift, forced into a fatal full-restructure rather than a cheap reweight (Gemini/829314, 773921; Claude/584721, 361742). Strong candidate Brief/Discussion hook.
- **The six-operation maintenance spectrum, ordered by frequency and cost** (reweight ≫ $\gamma$-reclassify ≫ prune/graft ≫ revise $O_t$ ≫ full restructure) was praised as the segment's clean organizing skeleton; the software-engineer mapping (test-pass reweight … rewrite-from-scratch) grounds it (Claude/584721, 829314).

#### 2. Candidate Discussion

- **Neutral variation as the constructive bridge, sharpened.** The Miller-2022 connection converts "radical restructuring is the *limit* of continuous operations" from a claim into a precise mechanism: near-zero-credence edges ≡ inaccessible/latent states; incremental updates ≡ neutral mutations; a previously-near-zero edge becoming load-bearing under regime change ≡ the parametric-limit event with discontinuous *behavioral* effect (Claude/361742, 584721). Candidate Discussion elaboration — "AAT does not need new discontinuous update math to handle paradigm shifts" (Gemini/829314).
- **The evolutionary-biology analog for latent diversity.** Most mutations are neutral and unselected in the current environment, but the dormant pool is what lets a population survive an ice age / new predator — applied to one agent's $\Sigma_t$, this gives "a strict mathematical justification for why organizations should tolerate 'inefficiency,' 'skunkworks,' 'weird side projects,' and 'technical debt that isn't hurting anyone' … the latent structural diversity required to survive a paradigm shift." The MDL penalty (`#form-strategy-complexity-cost`) vs. neutral-variation necessity is named as "the central architectural tradeoff of an agent's life" (Gemini/829314). Candidate Discussion centerpiece.

#### 3. Follow-up items

- *(Framing-grade follow-ups are captured above; the Codex/526815 items F63/F64/F65 route to the off-ramp — see lift report — as candidate findings: the continuity claim needs an explicit ambient supergraph / zero-weight-edge embedding to be literal; AND↔OR $\gamma$-reclassification is discrete absent a soft-gate parameterization; the "low-credence edges cost almost nothing" claim needs a credence-weighted cost model to be consistent with the pruning-threshold discussion.)*
- **Resolved process note:** an earlier audit (849201) flagged a stale "TF-10 destruction-creation" lineage reference in this segment's discussion header; it is no longer present in canon (verified 2026-05-31).

#### 4. Readers often ask / wonder

- **Where do new edges come from — does AAT have a model of creativity / hypothesis generation?** The "creative step" of grafting (positing a causal edge not in $\Sigma_t$) is the natural reader question; the segment points to $M_t$ / communication / CIY, but *generation* from $M_t$'s latent space "is still somewhat magical" — and is precisely where LLMs excel as proposal generators (Gemini/829314; Claude/849201-via-batch). Worth an explicit Discussion sentence.

#### 5. Candidate figures

- **Ambient-supergraph two-view diagram.** In a fixed ambient supergraph an edge weight slides continuously from $0$ to active (and back); *outside* that ambient graph, adding a node or flipping a gate is a discrete lift into a larger representational space. The figure makes visible exactly the scope the continuity claim needs (Codex/526815) — pedagogy + guardrail in one.

#### Belongs elsewhere

- **Cross-agent grafting → `#hyp-symbiogenic-composition` (Part III).** Within-agent grafting is the host-side component of full (bilateral, objective-absorbing) symbiogenesis; the type distinction was praised but the symbiogenesis side belongs in the composition-machinery cluster, not this Part II segment (Claude/584721, 361742; Gemini/829314).
