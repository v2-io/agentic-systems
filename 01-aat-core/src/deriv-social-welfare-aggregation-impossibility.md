---
slug: deriv-social-welfare-aggregation-impossibility
type: derivation
status: conditional
depends:
  - scope-composite-agent
  - deriv-strategic-composition
  - form-objective-functional
  - disc-implementation-impossibility
stage: draft
---

# Derivation: Social Welfare Aggregation Impossibility (Arrow)

The third charter instance of `#disc-implementation-impossibility`: Arrow 1951 (expanded 1963) forbids an external designer from constructing a social welfare function aggregating $n$ agents' strict preference orderings into a single social preference ordering over $\geq 3$ alternatives under unrestricted domain (U), Pareto efficiency (P), Independence of Irrelevant Alternatives (IIA), and non-dictatorial (ND). The AAT-side translation locates the agents as composite sub-agents whose individual preference orderings are derived from their objectives $O_t^{(i)}$, and maps the four classical escapes with *two* AAT-machinery adjacencies named: the preference-domain-restriction escape (single-peaked / single-crossing → Condorcet-consistent rules) is *adjacent to* sub-scope $\alpha'$ of `#deriv-strategic-composition` (the same adjacency `#deriv-strategy-proofness-impossibility` names), and the cardinal-preference escape (utilitarianism, range voting) is *adjacent to* `#form-objective-functional`'s value-functional machinery — both adjacencies open avenues, not elevations to load-bearing. The contribution: two AAT-side adjacencies precisely mapped, with the cardinal-preference adjacency unique to Arrow (it does not appear in GS or MS) because Arrow's ordinal-only constraint is what AAT's value-functional formulation could in principle relax while GS's strategy-proofness regime is orthogonal to the ordinal/cardinal distinction.

## Formal Expression

### Setting

Let $A$ be a finite alternative set with $\lvert A \rvert \geq 3$, and let $L$ denote the set of strict linear orderings on $A$. A **social welfare function** is a map $F: L^n \to L$ that aggregates $n$ agents' strict preference orderings $R = (R_1, \ldots, R_n) \in L^n$ into a single social ordering $F(R) \in L$ on the same alternative set.

Four constraints define the designer's regime:

*[Definition (unrestricted-domain, U)]* The map $F$ is defined on all of $L^n$ — every possible profile of strict preference orderings is a valid input.

*[Definition (pareto-efficient, P)]* If every agent strictly prefers $a$ over $b$ (i.e., $a \,R_i\, b$ for all $i$), then the social ordering puts $a$ strictly above $b$ ($a \,F(R)\, b$).

*[Definition (independence-of-irrelevant-alternatives, IIA)]* The social ordering's comparison of any pair $(a, b)$ depends only on the individuals' comparisons of $(a, b)$ — not on their comparisons involving any third alternative $c$. Formally: for any two profiles $R, R'$ such that each agent ranks $a$ and $b$ the same way in $R$ and $R'$, the social orderings $F(R)$ and $F(R')$ rank $a, b$ the same way.

*[Definition (non-dictatorial, ND)]* No agent $i^\ast$ such that for every profile $R$ and every pair $a, b$ with $a \,R_{i^\ast}\, b$ strictly, the social ordering $F(R)$ also puts $a$ above $b$ — i.e., no agent's strict preferences are imposed on society regardless of others.

### External theorem

*[Postulate (arrow-1951-1963, imported), exact]*

> **Theorem (Arrow 1951, 1963).** If $\lvert A \rvert \geq 3$, then no social welfare function $F: L^n \to L$ is simultaneously U, P, IIA, and ND.

References. Arrow, K. J. (1951, 2nd ed. 1963), *Social Choice and Individual Values*, Yale University Press. The expanded 1963 edition adds the simplified proof and discusses extensions. Modern proof structures: Geanakoplos, J. (2005), "Three brief proofs of Arrow's impossibility theorem," *Econ. Theory* 26:211–215; Reny, P. J. (2001), "Arrow's theorem and the Gibbard-Satterthwaite theorem: a unified approach," *Econ. Letters* 70:99–105 (geometric/topological unification with GS).

### No-go

A designer demanding U + P + IIA + ND cannot construct the social welfare function. Any candidate $F$ satisfying three of the four conditions violates the fourth.

### AAT-side translation

*[Derived (aat-social-welfare-translation, from `#scope-composite-agent` + `#form-objective-functional`), conditional on the composite-aggregation-mechanism reading]*

Within AAT's composite-agent setting, the Arrow no-go translates as follows:

- The "agents" are *sub-agents* in a composite per `#scope-composite-agent`, each carrying its own objective $O_t^{(i)}$ inducing a preference ordering $R_i \in L$ over composite-level alternatives $A$ (the joint outcomes reachable through the composite's strategic-composition machinery). The ordinal preference $R_i$ is the ordering induced by sub-agent $i$'s value functional $V_{O_t^{(i)}}(\tau)$ on the alternative set $A$.
- A "social welfare function" $F: L^n \to L$ is a *meta-aggregation mechanism* the designer imposes — a rule that takes the sub-agents' ordinal preferences (or reports thereof) and produces a single social ordering on $A$. The designer's task is to choose $F$.
- The IIA condition is the load-bearing one structurally: it requires that the social comparison of $a, b$ depend *only* on individuals' ordinal comparisons of $a, b$, not on their comparisons involving any other alternative — an *ordinal-only* informational restriction.

The Arrow theorem then states: under U + P + IIA + ND, no such $F$ exists. The designer faces a structural impossibility on what can be aggregated over the composite of sub-agents under ordinal-only information.

### Boundary characterization

| Escape | Mechanism-design / social-choice route | AAT machinery? |
|---|---|---|
| **Preference-domain restriction** | Single-peaked preferences (Black 1948) admit Condorcet-consistent rules including the median voter; single-crossing extends this. Domain restriction circumvents U. | **Adjacent to AAT machinery.** Sub-scope $\alpha'$ of `#deriv-strategic-composition` (potential / monotone game structure) is *adjacent to* single-peaked / single-crossing — the same adjacency `#deriv-strategy-proofness-impossibility` names. *Not identical*: sub-scope $\alpha'$ secures best-response convergence in the composite-dynamics, not Condorcet-consistent aggregation in the welfare function. |
| **Weakened IIA** | Positional methods — Borda count (1781), range voting, Coombs method. Each uses ranks-and-positions across the full ordering, not just pairwise comparisons. | **Outside AAT machinery.** Positional aggregation is not in AAT canon. |
| **Supermajority requirements** | Replace simple-majority with $k/n$ thresholds for $k \gt n/2$; admits constitutional / veto-respecting aggregators (e.g., the unanimity rule, two-thirds-majority rules). | **Outside AAT machinery.** Supermajority-thresholding mechanisms not in AAT canon. |
| **Cardinal preferences** | Relax ordinal-only IIA; allow social aggregation over cardinal utilities — utilitarian summation, weighted utilitarianism, range voting (treating ratings as cardinal). Sen 1970, *Collective Choice and Social Welfare*, Holden-Day, §3 gives the canonical treatment of cardinal-extension escapes. | **Adjacent to AAT machinery.** `#form-objective-functional`'s value-functional $V_{O_t}(\tau)$ carries cardinal value content — the value functional is real-valued, not ordinal-only. *Not identical*: AAT's value-functional formalism is per-sub-agent and per-trajectory, not a designer-side aggregation rule across sub-agents; lifting to aggregator-form requires a representational choice (utilitarian summation, weighted utilitarianism, etc.) that AAT does not currently make canonical. |

### Strengthened consequence

Arrow is the cluster instance with *two* AAT-side adjacencies:

**Adjacency 1: sub-scope $\alpha'$ ↔ preference-domain restriction.** Shared with `#deriv-strategy-proofness-impossibility`. Sub-scope $\alpha'$ of `#deriv-strategic-composition` (potential / monotone game structure) is adjacent to the single-peaked / single-crossing preference-domain restriction that admits Condorcet-consistent rules. The adjacency-without-identity is the same as in GS: sub-scope $\alpha'$ guarantees best-response *convergence* under fixed preferences, not Condorcet-consistent *aggregation* in the welfare function. The two are structurally related (both restrict preference structure to admit aggregation/convergence guarantees on a one-dimensional issue space) but operate at different layers of the composite-agent dynamics.

**Adjacency 2: cardinal preferences ↔ `#form-objective-functional`.** This adjacency is *unique to Arrow* among the three charter instances — GS's strategy-proofness regime is orthogonal to the ordinal/cardinal distinction (the manipulation no-go applies to any social-choice function on preference orderings regardless of whether utilities are ordinal or cardinal); MS's bilateral-trade setting already operates over cardinal valuations $v_b, v_s$ so the Arrow IIA escape doesn't apply. For Arrow specifically, the ordinal-only IIA restriction is what AAT's value-functional formulation could *in principle* relax — the value functional $V_{O_t}$ is real-valued and carries cardinal information per sub-agent. The adjacency is *open*: lifting AAT's per-sub-agent value-functional to a designer-side aggregator (utilitarian summation, weighted utilitarianism, range voting) requires a representational choice AAT does not currently make canonical. The open avenue is whether AAT extends to a designer-side welfare-aggregation formalism via the value-functional's cardinal content; if it does, Arrow's cardinal-preference escape would gain AAT-machinery internal content.

The other two escapes (weakened IIA via positional methods; supermajority requirements) belong entirely to social-choice theory and are honestly documented as outside AAT canon.

## Epistemic Status

*Exact* for the imported theorem (Arrow 1951, 1963 — classical theorem with closed-form proof in the source literature; multiple modern proofs available, e.g., Geanakoplos 2005, Reny 2001; primary-source verification scheduled for promotion past `draft`).

*Conditional* for the AAT-side translation — the composite-aggregation-mechanism reading is the natural composite-agent translation; alternative readings (treating sub-agents as factor-coalitions in a richer game; treating the social ordering as a $\Sigma$-level commitment device) exist and would map Arrow into different AAT-side vocabulary.

*Robust qualitative* for the boundary characterization — two named adjacencies (sub-scope $\alpha'$ ↔ preference-domain-restriction shared with GS; `#form-objective-functional` ↔ cardinal-preferences unique to Arrow); two outside AAT canon (positional methods, supermajority).

Max attainable: *Exact* for the imported theorem. *Derived conditional* for the AAT translation. *Robust qualitative* for the boundary characterization. The cardinal-preference adjacency could lift to *derived conditional* if AAT canonicalizes a designer-side welfare-aggregator construction over the per-sub-agent value functionals; that extension is open and would be its own framework-scope decision.

## Discussion

**Why this is not a `#disc-identifiability-floor` instance.** Same actor-positioning argument as GS and MS: the actor frustrated by the Arrow no-go is the *designer* (cannot construct a welfare function satisfying all four conditions), not an agent inferring from data. The escapes are *design-constraint relaxations* (relax U via domain restriction; relax IIA via positional methods or cardinal preferences; relax majority via supermajority), not information augmentations of an inferential regime. The cluster belongs in `#disc-implementation-impossibility`, not in the identifiability-floor.

**The cardinal-preference adjacency is structurally unique to Arrow.** Among the three charter instances of `#disc-implementation-impossibility`, only Arrow's IIA constraint produces a cardinal/ordinal distinction that AAT's value-functional formalism could engage. GS's strategy-proofness no-go applies regardless of utility cardinality; MS's bilateral-trade setting already operates over cardinal valuations. Arrow alone forbids aggregation under *ordinal-only* information, which is the constraint AAT's real-valued $V_{O_t}$ could relax. The adjacency is *open* — AAT does not currently formalize a designer-side aggregator that consumes the per-sub-agent value functionals — but it is the open avenue most specifically illuminating about how the framework might engage social-choice theory in the future.

**Peer voice with the social-choice literature.** The imported theorem is classical; the proof structure (Arrow 1951 via the decisive-set / dictator-pivotal-position argument; Geanakoplos 2005's three brief proofs; Reny 2001's geometric/topological unification with GS) is mature. AAT does not re-prove the theorem; AAT does not displace the standard escape routes; AAT does not claim that the value-functional formalism solves social-choice theory. The segment's contribution is honest recognition of the two adjacencies — sub-scope $\alpha'$ (shared with GS) and `#form-objective-functional`'s cardinal value content (unique to Arrow) — with the imported theorem cited under its original name and full bibliographic references.

**Relationship to `#form-objective-functional`.** The cardinal-preference adjacency raises an open question about the value-functional's downstream extension. `#form-objective-functional` formalizes $V_{O_t}(\tau)$ as the agent's value functional over trajectories; the cardinal content is *within-agent* (used for the agent's own choice). Arrow's cardinal-preference escape would lift this to *cross-agent* (used by a designer to aggregate across sub-agents). Whether such a lift is a natural extension of AAT or requires new framework machinery (a designer-side aggregator separate from the per-sub-agent value functional) is the open question. The 2026-05-22 Cohen-2022 strengthening cycle landed `#deriv-reward-channel-learning-no-go` as a sister segment to `#deriv-self-actuation-grounding` recognizing the *single-interface narrowness* of $V_{O_t}$ at the within-agent layer; a parallel cross-agent narrowness question (whether $V_{O_t}$ aggregates honestly across sub-agents) is structurally adjacent but not yet posed in canon.

## Findings

### The Arrow Translation and Its Two AAT-Side Adjacencies

**Brief:** Arrow's theorem says that no social welfare function — no rule for aggregating individuals' preferences into a single social preference ordering — can simultaneously satisfy four reasonable demands: be defined for every possible profile (unrestricted domain), respect unanimous preferences (Pareto efficiency), depend on each pair only through how individuals rank that pair (independence of irrelevant alternatives), and not be dictatorial (no single individual always decides). The classical escapes have been studied for decades — restrict the preference domain (single-peaked preferences admit the median voter / Condorcet rules), use a positional method (Borda count, range voting), require supermajorities, or allow cardinal preferences (weighted utilitarianism rather than ordinal-only aggregation). The contribution here is two named adjacencies on the AAT side: the preference-domain-restriction escape is *adjacent to* sub-scope $\alpha'$ of the strategic-composition machinery — same adjacency as GS — and the cardinal-preference escape is *adjacent to* the framework's value-functional formalism (which carries cardinal value content per sub-agent). The cardinal adjacency is structurally unique to Arrow: GS's strategy-proofness is orthogonal to the cardinal/ordinal distinction; MS already operates over cardinal valuations. Both adjacencies are *adjacent without being identical* — open avenues if the framework extends in those directions, not current elevations of AAT machinery to load-bearing. The other two escapes (positional methods, supermajority) belong entirely to social-choice theory and are honestly documented as outside AAT canon. The map of where the framework meets Arrow is the contribution; the theorem is classical.

**Impact:** Closes the third charter-instance slot of `#disc-implementation-impossibility` with the cluster's *richest* AAT-side adjacency map — two named adjacencies, one shared with GS (sub-scope $\alpha'$ ↔ preference-domain restriction) and one unique to Arrow (`#form-objective-functional` ↔ cardinal preferences). The Arrow-unique cardinal-preference adjacency is the open avenue most specifically illuminating about how the framework might engage social-choice theory in the future: AAT's per-sub-agent value functional $V_{O_t}$ carries cardinal value content, and lifting it to a designer-side cross-agent aggregator (utilitarian summation, weighted utilitarianism) is the natural extension that would give the Arrow cardinal-preference escape AAT-machinery internal content. Whether such an extension is a natural growth of AAT or requires new framework machinery is the open question raised by the adjacency. Together with the GS instance (named adjacency, no open avenue) and MS instance (no current adjacency, two open avenues), the cluster's three charter instances span the full range of how AAT meets the designer-side impossibility cluster.

**Novelty Claim:** *Claim recognition* of the AAT-side translation of Arrow's theorem under the composite-aggregation-mechanism reading (sub-agents per `#scope-composite-agent`; preference orderings induced by per-sub-agent $V_{O_t^{(i)}}$; designer-chosen aggregator $F$ producing social ordering); *claim differentiation* on the cardinal-preference adjacency being structurally unique to Arrow within the cluster — GS's strategy-proofness is orthogonal to the cardinal/ordinal distinction; MS's bilateral-trade setting already operates over cardinal valuations; only Arrow's ordinal-only IIA constraint produces a cardinal/ordinal distinction that AAT's value-functional formalism could engage. The imported theorem is classical (Arrow 1951, 1963); the AAT-side translation, the two-adjacency boundary characterization, and the cardinal-preference adjacency as the Arrow-unique open avenue are the contributions.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| The imported theorem | Arrow, K. J. (1951, 2nd ed. 1963), *Social Choice and Individual Values*, Yale University Press (found pre-2026) | *formal antecedent* — primary-source verification scheduled for promotion past `draft` |
| Modern proof structure | Geanakoplos, J. (2005), "Three brief proofs of Arrow's impossibility theorem," *Econ. Theory* 26:211–215 (found pre-2026); Reny, P. J. (2001), "Arrow's theorem and the Gibbard-Satterthwaite theorem: a unified approach," *Econ. Letters* 70:99–105 (found 2026-05-20) | *adjacent literature* — Geanakoplos for the constraint-regime formulation; Reny for the geometric-topological unification with GS that informs `#disc-implementation-impossibility`'s mechanism-family discussion |
| Single-peaked preferences as the domain-restriction escape | Black, D. (1948), "On the rationale of group decision-making," *J. Polit. Econ.* 56:23–34 (found pre-2026) | *adjacent literature* — the canonical escape; the sub-scope $\alpha'$ adjacency is named relative to this (shared with `#deriv-strategy-proofness-impossibility`) |
| Cardinal-preference escapes via weighted utilitarianism | Sen, A. (1970), *Collective Choice and Social Welfare*, Holden-Day, §3 (found pre-2026) | *adjacent literature* — the canonical treatment of cardinal-extension escapes; the `#form-objective-functional` adjacency is named relative to this (unique to Arrow within the cluster) |
| Borda count (positional method escape) | Borda, J.-C. (1781), "Mémoire sur les élections au scrutin," *Histoire de l'Académie Royale des Sciences* (found pre-2026) | *adjacent literature* — outside AAT machinery; documented as honest scope-mark |

**Search Log:**

- 2026-05-22 (*intuition-only* on the cardinal-preference adjacency): The cardinal-preference escape's connection to `#form-objective-functional` is named here for the first time; the natural correspondence (AAT's real-valued $V_{O_t}$ carries cardinal value content per sub-agent; lifting to a designer-side aggregator is a representational choice) is intuitive but not derived. Targeted future search candidates: utilitarian and weighted-utilitarian social welfare functions (Harsanyi 1955, *J. Polit. Econ.* 63:309–321; Sen 1970 §3 cardinal-comparability spectrum); range voting and ratings-based methods (Smith 2000 and follow-ups); whether the per-sub-agent value functional's cardinal content can be made canonically aggregable without introducing new framework machinery.
- 2026-05-22 (*intuition-only* on the composite-aggregation-mechanism reading): Same composite-revelation-mechanism reading as `#deriv-strategy-proofness-impossibility`. Alternative readings exist (treating $F$ as a $\Sigma$-level commitment device; treating sub-agents as factor-coalitions in a richer cooperative game); not pursued here.
- 2026-05-20 (*targeted, the strengthen-first arm on GS-as-Instance-4 of `#disc-identifiability-floor`*): The 2026-05-20 spike (`spikes/.integrated/spike-4th-identifiability-floor-instance-2026-05-20.md` §5) flagged Arrow alongside Myerson-Satterthwaite as candidate instances of a sister meta-segment if mechanism design becomes a first-class framework concern. Arrow is the third charter instance landing in this cycle.

## Working Notes

- **Provenance.** Authored 2026-05-22 as commit 4 of the post-Track-CR Track-B cycle, executing `spikes/implementation-impossibility-meta-segment-plan.md` §4.c. The 2026-05-20 strengthen-first arm record at `spikes/.integrated/spike-4th-identifiability-floor-instance-2026-05-20.md` §5 flagged Arrow as a candidate instance of the sister meta-segment route.
- **Open before `candidate`.** (a) Primary-source verification of Arrow 1951 / 1963 — the theorem statement above is taken from the textbook syntheses and modern proof papers (Geanakoplos 2005, Reny 2001); direct primary-source reading is queued. (b) The cardinal-preference ↔ `#form-objective-functional` adjacency is currently *robust qualitative* — there is no derived identification of AAT's value-functional with a designer-side aggregator; lifting the adjacency to *derived conditional* would require either canonicalizing a designer-side welfare-aggregation construction over the per-sub-agent $V_{O_t^{(i)}}$, or honestly determining that no such construction is natural within AAT's current scope. (c) The shared sub-scope-$\alpha'$ adjacency with `#deriv-strategy-proofness-impossibility` inherits the open-derivation flagged there: whether single-peaked preferences on an issue-space *derivably* induce a potential-game structure under best-response dynamics is the parameter-level identification question; if it lands, both GS and Arrow's sub-scope-$\alpha'$ adjacencies lift to *exact* simultaneously.
- **The cluster's range, complete after this commit.** The three charter instances of `#disc-implementation-impossibility` now span the full range of AAT/mechanism-design boundary types: GS (one named adjacency, no open avenue), MS (no current adjacency, two open avenues), Arrow (one shared named adjacency, one Arrow-unique open avenue). That range is the cluster's epistemic content — the framework recognizes where its machinery contributes, where it sits adjacent, where it has open avenues, and where the boundary is outside entirely. The cluster's discipline filter admits all three; future candidate instances (Roberts 1979 affine-maximizers, Skalse 2022 reward-hacking) would be evaluated against the same filter in a future cycle.
- **The Arrow-unique cardinal adjacency as the cluster's most-illuminating open question.** Among all the adjacencies and avenues across the three charter instances, the cardinal-preference ↔ `#form-objective-functional` adjacency is the one most directly illuminating about how AAT might grow into mechanism design proper. The value functional already carries cardinal content per sub-agent; the only remaining structural question is whether cross-agent aggregation is a natural extension of the framework or requires distinct designer-side machinery. Flagging this here so future framework-scope decisions can engage the question with full provenance.
