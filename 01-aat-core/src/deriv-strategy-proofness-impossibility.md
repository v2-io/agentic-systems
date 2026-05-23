---
slug: deriv-strategy-proofness-impossibility
type: derivation
status: conditional
depends:
  - scope-composite-agent
  - deriv-strategic-composition
  - disc-implementation-impossibility
stage: draft
---

# Derivation: Strategy-Proofness Impossibility (Gibbard-Satterthwaite)

The first charter instance of `#disc-implementation-impossibility`: Gibbard 1973 and Satterthwaite 1975 forbid an external designer from constructing a dominant-strategy incentive-compatible (DSIC), non-dictatorial, surjective social-choice function over $\geq 3$ alternatives under unrestricted preferences. The AAT-side translation locates the designer's task in the composite-agent setting ( `#scope-composite-agent`), recognizes the agents as composite sub-agents reporting preferences derived from their objectives $O_t^{(i)}$, and maps the four standard escapes against AAT machinery — with the preference-domain-restriction escape (single-peaked / single-crossing) named precisely as *adjacent to but not identical with* the sub-scope $\alpha'$ machinery of `#deriv-strategic-composition`. The 2026-05-20 strengthen-first arm confirmed the adjacency is not identity: sub-scope $\alpha'$ secures best-response *convergence* under fixed reports; GS forbids *strategy-proof revelation*. The honest map of where AAT meets mechanism design is the contribution; the imported theorem is classical.

## Formal Expression

### Setting

Let $A$ be a finite alternative set with $\lvert A \rvert \geq 3$, and let $L$ denote the set of strict linear orderings on $A$. A **social-choice function** is a map $f: L^n \to A$ that aggregates $n$ agents' reported preferences $R = (R_1, \ldots, R_n) \in L^n$ into a single outcome $f(R) \in A$.

Three constraints define the designer's regime:

*[Definition (dsic, strategy-proofness / dominant-strategy incentive compatibility)]*

$$\forall i,\ \forall R_{-i}\in L^{n-1},\ \forall R_i, R'_i \in L:\quad f(R_i, R_{-i}) \,R_i\, f(R'_i, R_{-i}).$$

Truth-telling is a dominant strategy: no agent $i$ can profit from misreporting given any reports by the others.

*[Definition (non-dictatorial)]*

$$\neg\,\exists i^\ast:\ \forall R \in L^n,\ f(R) \text{ is } i^\ast\text{'s top-ranked alternative in } R_{i^\ast}.$$

No agent fully determines the outcome.

*[Definition (surjective)]* $f(L^n) = A$. Every alternative is reachable from some report profile.

### External theorem

*[Postulate (gibbard-satterthwaite-1973-75, imported), exact]*

> **Theorem (Gibbard 1973; Satterthwaite 1975).** If $\lvert A \rvert \geq 3$ and preferences are unrestricted (each $R_i$ ranges over all of $L$), then no social-choice function $f: L^n \to A$ is simultaneously DSIC, non-dictatorial, and surjective.

References. Gibbard, A. (1973), "Manipulation of voting schemes: a general result," *Econometrica* 41(4):587–601. Satterthwaite, M. A. (1975), "Strategy-proofness and Arrow's conditions: existence and correspondence theorems for voting procedures and social welfare functions," *J. Econ. Theory* 10(2):187–217. Modern textbook synthesis: Mas-Colell, Whinston & Green (1995), *Microeconomic Theory*, §23.C; geometric/topological proof structure shared with Arrow's theorem in Reny, P. J. (2001), "Arrow's theorem and the Gibbard-Satterthwaite theorem: a unified approach," *Econ. Letters* 70:99–105.

### No-go

A designer who insists simultaneously on DSIC, non-dictatorial, surjective, and unrestricted-preferences cannot construct the social-choice function. Any candidate $f$ satisfying three of the four conditions violates the fourth.

### AAT-side translation

*[Derived (aat-mechanism-translation, from `#scope-composite-agent` + `#deriv-strategic-composition`), conditional on the composite-revelation-mechanism reading]*

Within AAT's composite-agent setting, the GS no-go translates as follows:

- The "agents" are *sub-agents* in a composite per `#scope-composite-agent`, each carrying its own objective $O_t^{(i)}$ inducing a preference ordering $R_i \in L$ over composite-level alternatives $A$ (the joint outcomes reachable through the composite's strategic-composition machinery).
- A "social-choice function" $f: L^n \to A$ is a *mechanism* the designer (external to the composite agent) imposes — a rule that takes the sub-agents' *reports* $R = (R_1, \ldots, R_n)$ and produces a composite-level outcome. The designer's task is to choose $f$.
- "Strategy-proofness" requires that each sub-agent's truth-telling about its own $O_t^{(i)}$-induced ordering is its best-response strategy. The DSIC condition is stronger than Nash equilibrium: dominance against *all* other-agent reports, not just equilibrium-consistent ones.

The GS theorem then states: under the four stated conditions, no such mechanism exists. The designer faces a structural impossibility on what can be implemented over the composite of strategically-reporting sub-agents under unrestricted preference domain.

### Boundary characterization

| Escape | Mechanism-design route | AAT machinery? |
|---|---|---|
| **Preference-domain restriction** | Single-peaked preferences (Black 1948 *J. Polit. Econ.* 56:23–34) admit the median-voter rule; single-crossing extends this. The domain restriction circumvents the unrestricted-preferences condition. | **Adjacent to AAT machinery.** Sub-scope $\alpha'$ of `#deriv-strategic-composition` (potential / monotone game structure) is *adjacent* to single-peaked / single-crossing — both restrict the preference-or-utility structure to admit convergence/aggregation guarantees — but **not identical** (see *Sub-scope $\alpha'$ vs preference-domain restriction* below). |
| **Weakened solution concept** | Bayes-Nash incentive compatibility (BIC) instead of dominant-strategy IC — d'Aspremont & Gérard-Varet (1979) "Incentives and incomplete information," *J. Public Econ.* 11:25–45. The designer relaxes from dominance to expected-utility best-response under a common prior on others' types. | **Outside AAT machinery.** BIC requires a shared prior over types and Bayesian reasoning over expected reports; AAT's strategic-composition machinery does not currently formalize the mechanism-induced report game in BIC terms. |
| **Randomization** | Gibbard (1977) "Manipulation of schemes that mix voting with chance," *Econometrica* 45:665–681 — random-dictator and convex-combination mechanisms admit strategy-proofness in expectation. | **Outside AAT machinery.** AAT's machinery treats deterministic strategies $\Sigma_t$; randomized-mechanism design is not in canon. |
| **Restricted strategy space (enforced truth-telling)** | The revelation-principle-companion: if the designer can verify reports against ground truth (e.g., observable types), strategy-proofness becomes definitional rather than incentivized. | **Outside AAT machinery.** AAT's agent-spectrum ( `#def-agent-spectrum`) does not currently include verification-of-self-reports machinery. |

### Strengthened consequence

The boundary-precise contribution: the AAT/mechanism-design intersection is at *one* of the four GS escapes, and that intersection is *adjacent without being identical*. The honest map looks like this.

**Sub-scope $\alpha'$ vs preference-domain restriction.** The 2026-05-20 strengthen-first arm (`spikes/.integrated/spike-4th-identifiability-floor-instance-2026-05-20.md` §4) tested three reframings under which sub-scope $\alpha'$ would *be* the GS escape, and rejected all three: sub-scope $\alpha'$ secures best-response *convergence* of the composite-dynamics given a fixed mechanism, not *strategy-proofness* of the mechanism itself. Concretely: agents in a potential game (the canonical sub-scope $\alpha'$ instance) can have profitable unilateral deviations under non-truthful preference revelation even when the joint best-response dynamics under the current revelation converge. The convergence-under-current-reports guarantee that sub-scope $\alpha'$ supplies is *not* the dominance-over-all-reports guarantee DSIC requires.

The honest read: sub-scope $\alpha'$ is *adjacent to* the preference-domain-restriction escape because both restrict the preference-or-payoff structure in similar ways (single-peaked preferences exhibit a potential-game-like ordinal structure on single-dimensional issue spaces; monotone games on lattices share order-theoretic features with single-crossing preference domains), but it is *not the same restriction*. Sub-scope $\alpha'$'s contribution to the composite-agent layer is convergence-given-mechanism, not mechanism-strategy-proofness. The boundary is named precisely; AAT does not claim to escape GS, but recognizes where the framework's strategic-composition machinery sits *next to* one of GS's classical escapes.

The other three escapes belong entirely to mechanism design and social-choice theory. The framework honestly documents that, and locates its current contribution as *recognition of the boundary* rather than *provision of the escapes*.

## Epistemic Status

*Exact* for the imported theorem (Gibbard 1973, Satterthwaite 1975 — classical theorems with closed-form proofs in the source literature, primary-source verification scheduled for promotion past `draft`).

*Conditional* for the AAT-side translation — the mapping from social-choice-function to composite-mechanism-over-sub-agent-reports is mechanical under the *composite-revelation-mechanism reading* (sub-agents per `#scope-composite-agent`; reports as inputs to a designer-chosen $f$; composite outcomes as elements of $A$), but the reading itself is a representational choice; alternative AAT readings (e.g., treating sub-agents as auctioning under VCG-like settings; treating $f$ as a $\Sigma$-level commitment device) exist and would map GS to different AAT-side vocabulary.

*Robust qualitative* for the boundary characterization (sub-scope $\alpha'$ is adjacent-but-not-identical to preference-domain restriction; the other three escapes are outside AAT canon) — survives across instance details, with the specific functional adjacency (single-peaked ↔ potential-game-like structure on issue spaces) noted but not derived as identity.

Max attainable: *Exact* for the imported theorem; *derived conditional* for the AAT translation; *robust qualitative* for the boundary characterization. The AAT translation's max ceiling stays *conditional* unless an alternative reading is forced by some AAT-internal uniqueness argument (no such argument currently in hand).

## Discussion

**Why this is not a `#disc-identifiability-floor` instance.** The 2026-05-20 strengthen-first arm tested GS against the identifiability-floor's five-element shape and confirmed it fails on actor positioning: in Instances 1–4 of the floor the actor frustrated by the no-go is the *agent itself* (cannot detect, identify, certify, or recover an architectural d.o.f. from limited data), and the escape elevates *agent-side* information-augmentation machinery (loop-interventional access, latent observability, matched-Tier composite-extended observation, similarity-fiber resolution). GS's actor is the *designer*; the escapes are *design-constraint relaxations*. The cluster is structurally different and belongs in the sister meta-segment `#disc-implementation-impossibility`. This segment is GS's home there.

**Sub-scope $\alpha'$ adjacency, named precisely.** The Discussion above states sub-scope $\alpha'$ is *adjacent to* preference-domain restriction but *not identical*; this is load-bearing for the honest scope-marking discipline of `#disc-implementation-impossibility`. The framework's contribution here is recognition of where the strategic-composition machinery sits next to one of GS's classical escapes — not a claim that AAT supplies the escape. Mechanism-design proper supplies the escape; AAT documents the proximity.

**Peer voice with the mechanism-design literature.** The imported theorem is classical; the proof structure (Gibbard 1973 via the revelation-principle-style argument; Satterthwaite 1975 via direct manipulation construction; Reny 2001 via geometric/topological unification with Arrow) is mature. AAT does not re-prove the theorem; AAT does not displace the standard escape routes; AAT does not claim that the strategic-composition machinery solves mechanism design. The segment's contribution is honest recognition of the boundary, with the imported theorem cited under its original names and full bibliographic references.

**Relationship to `#deriv-strategic-composition`.** Strategic composition's Discussion section had carried "mechanism-design impossibility" as a candidate-fourth-instance flag of `#disc-identifiability-floor` (line 183); the 2026-05-20 spike correctly determined that placement was wrong on actor-positioning grounds. The flag is closed in this cycle: GS is here in the sister meta-segment, sub-scope $\alpha'$ retains its load-bearing role in strategic-composition for best-response convergence, and is *additionally* recognized as adjacent to GS's preference-domain-restriction escape under the boundary characterization above.

## Findings

### The Gibbard-Satterthwaite Translation and Its Sub-Scope $\alpha'$ Adjacency

**Brief:** The Gibbard-Satterthwaite theorem says that no voting rule can be at once strategy-proof (no one ever benefits from misreporting their preferences), non-dictatorial (no single voter always decides), surjective (every alternative is reachable), and broadly applicable (works on unrestricted preferences) when there are at least three alternatives. The classical escapes have been studied for decades — restrict the preference domain (require single-peaked preferences; the median voter rule works), allow randomization (random dictator is strategy-proof in expectation), accept a weaker incentive concept (Bayes-Nash IC under a shared prior), or constrain the strategy space (enforce truth-telling by verifying reports). The contribution here is the honest map: when the framework recognizes a composite agent whose sub-agents have their own objectives, the strategic-composition machinery's sub-scope $\alpha'$ (potential or monotone games — the regime where best-response dynamics converge) is *adjacent to* the preference-domain-restriction escape (single-peaked / single-crossing) — both restrict the preference structure to admit aggregation/convergence guarantees — but is *not the same restriction*: convergence-under-current-reports is not dominance-over-all-reports. The other three classical escapes belong entirely to mechanism design and social-choice theory; the framework documents them as outside the current canon. Mapping that boundary honestly is the contribution; the impossibility is classical.

**Impact:** Closes the candidate-fourth-instance flag in `#deriv-strategic-composition` Discussion (the 2026-05-20 strengthen-first arm's recommended disposition) by landing GS in its proper home — the designer-side `#disc-implementation-impossibility` meta-segment, with sub-scope $\alpha'$'s relationship to the preference-domain-restriction escape named precisely. The named adjacency-without-identity is the kind of scope-honesty discipline the framework runs throughout: AAT recognizes where its machinery sits next to classical mechanism-design escape routes, and refuses the temptation to overclaim that sub-scope $\alpha'$ "supplies" the escape (it does not — it supplies a different guarantee at a different layer of the composite-agent dynamics). The result is a charter instance of the designer-side cluster with the AAT/mechanism-design boundary mapped with precision rather than enthusiasm.

**Novelty Claim:** *Claim recognition* of the AAT-side translation of the Gibbard-Satterthwaite theorem into the composite-agent setting (sub-agents per `#scope-composite-agent`; reports as inputs to a designer-chosen mechanism; composite outcomes as the alternative set); *claim differentiation* on the sub-scope $\alpha'$ ↔ preference-domain-restriction adjacency: sub-scope $\alpha'$ is *adjacent to but not identical with* the GS preference-domain escape (the 2026-05-20 spike's three-reframing strengthen-first check is the documented argument). The imported theorem is classical (Gibbard 1973; Satterthwaite 1975); the AAT-side translation, the boundary-characterization annotations, and the honest adjacency-without-identity recognition are the contributions.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| The imported theorem | Gibbard, A. (1973), "Manipulation of voting schemes: a general result," *Econometrica* 41(4):587–601 (found pre-2026); Satterthwaite, M. A. (1975), "Strategy-proofness and Arrow's conditions: existence and correspondence theorems for voting procedures and social welfare functions," *J. Econ. Theory* 10(2):187–217 (found pre-2026) | *formal antecedent* — primary-source verification scheduled for promotion past `draft` |
| Modern textbook synthesis | Mas-Colell, A., Whinston, M. D. & Green, J. R. (1995), *Microeconomic Theory*, Oxford University Press, §23.C (found pre-2026) | *adjacent literature* — used for the constraint-regime formulation in the Setting above |
| Geometric/topological proof unification with Arrow | Reny, P. J. (2001), "Arrow's theorem and the Gibbard-Satterthwaite theorem: a unified approach," *Econ. Letters* 70:99–105 (found 2026-05-20 via the strengthen-first arm) | *adjacent literature* — names the topological-combinatorial mechanism shared with Arrow's theorem (Instance 3 of `#disc-implementation-impossibility`); informs the mechanism-family discussion in the meta-segment |
| Single-peaked preferences as the canonical domain-restriction escape | Black, D. (1948), "On the rationale of group decision-making," *J. Polit. Econ.* 56:23–34 (found pre-2026) | *adjacent literature* — the canonical escape; the sub-scope $\alpha'$ adjacency is named relative to this |
| Random-dictator and randomized-mechanism escapes | Gibbard, A. (1977), "Manipulation of schemes that mix voting with chance," *Econometrica* 45:665–681 (found pre-2026) | *adjacent literature* — outside AAT machinery; documented as honest scope-mark |
| Bayes-Nash IC weakening | d'Aspremont, C. & Gérard-Varet, L.-A. (1979), "Incentives and incomplete information," *J. Public Econ.* 11:25–45 (found pre-2026) | *adjacent literature* — outside AAT machinery; documented as honest scope-mark |

**Search Log:**

- 2026-05-20 (*targeted, the strengthen-first arm on GS-as-Instance-4 of `#disc-identifiability-floor`*): The 2026-05-20 spike re-derived GS against the identifiability-floor's five-element test, tested three reframings under strengthen-before-soften (GS as identifiability-of-truthful-preferences; GS as Section III multi-agent no-go on `#scope-composite-agent` (C-iv) routes; GS as alignment-design obstruction), and confirmed sub-scope $\alpha'$ does *not* escape GS (it secures best-response convergence, not strategy-proofness). The verdict's recommended disposition — route GS to a sister meta-segment if mechanism design becomes a first-class framework concern — is what this segment lands.
- 2026-05-22 (*intuition-only* on the AAT-side composite-revelation-mechanism reading): The mapping from social-choice function to composite-mechanism-over-sub-agent-reports (sub-agents per `#scope-composite-agent`; reports as inputs; composite outcomes as $A$) is the natural AAT-side reading; alternative readings exist (treating $f$ as a $\Sigma$-level commitment device; treating sub-agents as VCG-auction bidders) and would map GS to different AAT-side vocabulary. The composite-revelation reading is chosen here for parsimony with `#deriv-strategic-composition`; targeted future search candidates would be alternative-reading derivations if a downstream use of this segment requires them.

## Working Notes

- **Provenance.** Authored 2026-05-22 as commit 2 of the post-Track-CR Track-B cycle, executing `spikes/implementation-impossibility-meta-segment-plan.md` §4.a. The 2026-05-20 strengthen-first arm record at `spikes/.integrated/spike-4th-identifiability-floor-instance-2026-05-20.md` §4 carries the load-bearing argument that sub-scope $\alpha'$ is *adjacent to but not identical with* the GS preference-domain-restriction escape.
- **Open before `candidate`.** (a) Primary-source verification of Gibbard 1973 and Satterthwaite 1975 — the theorem statement above is taken from the textbook synthesis (Mas-Colell, Whinston & Green 1995 §23.C) and the geometric-proof-unification paper (Reny 2001); direct primary-source reading is queued. (b) Alternative AAT-side readings of GS — treating $f$ as a $\Sigma$-level commitment device, or treating sub-agents as VCG-auction bidders — would map GS into different AAT vocabulary; whether either alternative reading produces a stronger AAT-side derivation is a candidate sub-spike. (c) The sub-scope $\alpha'$ ↔ single-peaked-preferences adjacency is currently *robust qualitative* — there may be an AAT-internal derivation showing the structural correspondence at parameter-level (e.g., that single-peaked preferences on an issue-space induce a potential-game structure under standard best-response dynamics); the derivation is queued and would lift the adjacency claim to *exact* if it lands cleanly.
- **The composite-revelation-mechanism reading and its sub-agents.** The AAT-side translation treats the GS "agents" as sub-agents in a composite per `#scope-composite-agent`, each carrying its own objective $O_t^{(i)}$ inducing a preference ordering over composite-level alternatives. This is the most parsimonious AAT-side reading and aligns with `#deriv-strategic-composition`'s framing of strategic composition over sub-agent objectives. The reading does *not* assume sub-agents have unbounded computational capacity, do not constrain their reporting strategies to be honest, do not require shared priors — the GS no-go applies to the designer's mechanism task regardless of those details.
- **The cluster's discipline filter.** GS is the *cleanest* charter instance of `#disc-implementation-impossibility` — the discipline filter (constructive-impossibility-shape only) admits it directly: the setting is well-stated, the external theorem is classical, the no-go is sharp, the escapes are well-characterized in the literature, and the strengthened consequence (the AAT/mechanism-design boundary precisely mapped at the sub-scope $\alpha'$ adjacency) is the framework's honest contribution. The next charter instances (MS, Arrow) fit the same template with their own variations.
