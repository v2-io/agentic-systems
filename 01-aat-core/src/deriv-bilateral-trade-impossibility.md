---
slug: deriv-bilateral-trade-impossibility
type: derivation
status: conditional
depends:
  - scope-composite-agent
  - deriv-strategic-composition
  - disc-implementation-impossibility
stage: draft
---

# Derivation: Bilateral Trade Impossibility (Myerson-Satterthwaite)

The second charter instance of `#disc-implementation-impossibility`: Myerson & Satterthwaite 1983 forbid an external designer from constructing an ex-post efficient, Bayesian incentive compatible, individually rational, budget-balanced bilateral-trade mechanism when buyer and seller have private valuations drawn from overlapping continuous distributions. The AAT-side translation locates the buyer and seller as a two-sub-agent composite per `#scope-composite-agent`; recognizes that the two-agent strategic-composition machinery of `#deriv-strategic-composition` applies cleanly to the agents' best-response dynamics *given* a fixed mechanism but does not cover the designer's mechanism-choice problem; and honestly maps the four classical escapes as almost entirely outside AAT's current canon. The contribution here is *boundary precision*: bilateral-trade impossibility is *adjacent to* AAT (the strategic-composition layer engages the agents-given-mechanism dynamics) but the designer's task lives in mechanism-design proper. The honest scope-mark is the contribution.

## Formal Expression

### Setting

Two parties: a buyer $B$ with private valuation $v_b \in [0, \bar v_b]$ drawn from distribution $F_b$ with density $f_b$, and a seller $S$ with private valuation $v_s \in [0, \bar v_s]$ drawn from distribution $F_s$ with density $f_s$. The supports overlap: there exists a non-empty interval $[a, b] \subseteq [0, \bar v_b] \cap [0, \bar v_s]$ such that $f_b$ and $f_s$ are both strictly positive on $[a, b]$. A **direct mechanism** is a pair $(p, x)$ where $p: [0, \bar v_b] \times [0, \bar v_s] \to [0, 1]$ is the trade probability and $x: [0, \bar v_b] \times [0, \bar v_s] \to \mathbb{R}$ is the buyer's expected payment to the seller (with the seller receiving $x$). Equivalently with interim allocation rules $\bar p_b(v_b), \bar p_s(v_s)$ and interim transfer rules $\bar x_b(v_b), \bar x_s(v_s)$ for buyer-and-seller respectively.

Four constraints define the designer's regime:

*[Definition (ex-post-efficient)]* $p(v_b, v_s) = 1 \iff v_b \geq v_s$. Trade occurs exactly when the buyer values the good at least as much as the seller.

*[Definition (bayesian-ic, BIC)]* Each agent's truthful reporting is a Bayesian best response given the other's truthful strategy:

$$v_b \bar p_b(v_b) - \bar x_b(v_b) \;\geq\; v_b \bar p_b(\hat v_b) - \bar x_b(\hat v_b) \quad \forall v_b, \hat v_b,$$

and symmetrically for the seller (with the sign reversed since the seller is paid).

*[Definition (individual-rationality, IR)]* Both parties participate voluntarily: expected interim payoff is nonnegative for every type:

$$v_b \bar p_b(v_b) - \bar x_b(v_b) \;\geq\; 0 \quad \forall v_b, \quad\text{and}\quad \bar x_s(v_s) - v_s \bar p_s(v_s) \;\geq\; 0 \quad \forall v_s.$$

*[Definition (budget-balance)]* No external subsidy: the buyer's expected payment exactly equals the seller's expected receipt:

$$\mathbb{E}[x(v_b, v_s)] \;=\; 0\text{ (net designer-side)}.$$

### External theorem

*[Postulate (myerson-satterthwaite-1983, imported), exact]*

> **Theorem (Myerson & Satterthwaite 1983).** If $f_b$ and $f_s$ are strictly positive on a common open interval and the supports overlap, no direct mechanism $(p, x)$ is simultaneously ex-post efficient, BIC, IR, and budget-balanced.

Reference. Myerson, R. B. & Satterthwaite, M. A. (1983), "Efficient mechanisms for bilateral trading," *J. Econ. Theory* 29(2):265–281. Modern textbook synthesis: Krishna, V. (2002), *Auction Theory*, Academic Press, §5.3; Mas-Colell, A., Whinston, M. D. & Green, J. R. (1995), *Microeconomic Theory*, Oxford University Press, §23.E.

### No-go

A designer demanding ex-post efficiency + BIC + IR + budget-balance cannot construct the bilateral-trade mechanism. Any candidate mechanism satisfying three of the four conditions violates the fourth. Equivalently: under private values with overlapping supports, the designer must accept a deficit (relax budget-balance), accept inefficiency (relax ex-post efficiency), accept that participation is not always individually rational, or weaken the incentive concept.

### AAT-side translation

*[Derived (aat-bilateral-trade-translation, from `#scope-composite-agent`), conditional on the buyer-seller-as-two-sub-agent reading, partial]*

Within AAT's composite-agent setting, the MS no-go translates partially:

- The "buyer" and "seller" are *sub-agents* in a two-sub-agent composite per `#scope-composite-agent`, each carrying its own objective $O_t^{(i)}$ — the buyer's $O_t^{(B)}$ rewarding acquisition at favorable price; the seller's $O_t^{(S)}$ rewarding relinquishing at favorable price.
- The "mechanism" $(p, x)$ is a designer-imposed structure on the composite's joint action space and reward redistribution — outside AAT's agent-level machinery; AAT's strategic-composition machinery in `#deriv-strategic-composition` applies to the agents' best-response dynamics *given* the mechanism $(p, x)$, not to the designer's choice of $(p, x)$.

The honest translation: the *agents-given-mechanism layer* is internal to AAT (strategic-composition machinery applies); the *mechanism-choice layer* is external. The MS no-go applies at the mechanism-choice layer; AAT does not currently cover it.

### Boundary characterization

| Escape | Mechanism-design route | AAT machinery? |
|---|---|---|
| **Subsidies** (relax budget-balance) | VCG mechanism with deficit; pivotal-mechanism transfers. The designer covers any shortfall from external resources. | **Outside AAT machinery.** AAT does not currently formalize designer-side transfer pools or subsidy budgets. |
| **Second-best mechanisms** (relax ex-post efficiency) | Myerson 1981 "Optimal auction design," *Math. Oper. Res.* 6:58–73 — characterizes revenue-optimal mechanisms with inefficient withholding in the marginal-cost-curve region; bilateral-trade analog accepts trade-failure when $v_b - v_s$ is small relative to the inefficiency cost. | **Outside AAT machinery.** Optimal-mechanism design under welfare-relaxation is the constructive side of mechanism design; deliberately excluded by the discipline filter (see `#disc-implementation-impossibility`'s "constructive mechanism-design" exclusion). |
| **Common values** (relax private values) | Information aggregation under shared-value components — Wilson 1977 "A bidding model of perfect competition," *Rev. Econ. Stud.* 44:511–518; the no-go softens because the agents' reports carry shared signal. | **Outside AAT machinery; adjacent** to `#scope-edge-update-causal-validity`'s regime-indexed identification structure. The shared-signal regime is structurally similar to AAT's partial-intervention Regime B (`#scope-edge-update-causal-validity`'s middle tier), but the formal connection has not been derived. |
| **Long-run reputation / repeated interaction** | Single-shot MS does not bind in indefinitely-repeated bilateral-trade games — Folk-theorem-style mechanisms with reputation backlash. Fudenberg-Maskin 1986 *Econometrica* 54:533–554 for the canonical Folk-theorem setup. | **Outside AAT machinery; adjacent** to the strategic-composition machinery in repeated-game form. The repeated-game extension of `#deriv-strategic-composition` is open canonical work; the MS-escape connection would land there if pursued. |

### Strengthened consequence

The MS boundary lies *almost entirely outside* AAT's current machinery — and the *honest delineation* is the contribution. AAT does not claim to escape MS; AAT does not provide subsidies, optimal-mechanism design, common-value aggregation, or repeated-game reputation machinery in its current canon. The framework's contribution at this charter instance is precisely the boundary recognition: the two-agent strategic-composition machinery in `#deriv-strategic-composition` applies cleanly to the buyer-seller best-response dynamics *given* a fixed mechanism (the agents-given-mechanism layer is internal), but the designer's mechanism-choice problem (the mechanism-choice layer) is external. The two escapes flagged as *adjacent* (common-values to Regime B; repeated-interaction to repeated-strategic-composition) are open avenues if AAT extends in those directions; the two flagged as *outside* (subsidies, second-best mechanisms) belong to mechanism-design proper.

The contribution is the same kind of scope-honesty discipline `#disc-identifiability-floor` runs on the agent side and `#deriv-strategy-proofness-impossibility` runs at a different AAT-machinery-intersection: name the boundary precisely; refuse to overclaim machinery the framework does not currently supply.

## Epistemic Status

*Exact* for the imported theorem (Myerson & Satterthwaite 1983 — classical theorem with closed-form proof in the source literature; primary-source verification scheduled for promotion past `draft`).

*Conditional, partial* for the AAT-side translation — the buyer-seller-as-two-sub-agent reading is the natural composite-agent translation, but the *agents-given-mechanism layer* is the only part of the no-go internal to AAT canon; the *mechanism-choice layer* (where the no-go binds) is external. The partial-translation is honest — AAT recognizes the bilateral-trade designer-task as adjacent but does not formalize the designer-side mechanism-choice problem.

*Robust qualitative* for the boundary characterization — four escapes documented with honest scope-marks; two adjacencies named (common-values ↔ Regime B; repeated-interaction ↔ repeated-strategic-composition); no precise functional intersection derived.

Max attainable: *Exact* for the imported theorem. *Derived conditional* for the AAT translation, with the *conditional* gating on the buyer-seller-two-sub-agent reading; an alternative reading (e.g., buyer and seller as *single-agent-with-two-roles* under intertemporal preference modeling) would change the translation but is not currently in canon. *Robust qualitative* for the boundary characterization; lifting to *exact* on the common-values ↔ Regime B intersection would require formalizing the regime-correspondence, which is open.

## Discussion

**Why this is not a `#disc-identifiability-floor` instance.** Same actor-positioning argument as for the GS instance (`#deriv-strategy-proofness-impossibility`): the actor frustrated by the MS no-go is the *designer* (cannot construct a mechanism satisfying all four conditions), not an agent inferring from data. The escapes are *design-constraint relaxations* (relax budget-balance / efficiency / private-values / single-shot interaction), not information augmentations of an inferential regime. The cluster belongs in `#disc-implementation-impossibility`, not in the identifiability-floor.

**Why the AAT translation is honestly partial.** Unlike the GS instance (where sub-scope $\alpha'$ of `#deriv-strategic-composition` has a named adjacency to the preference-domain-restriction escape), MS has *no* AAT-internal escape adjacency. The two *adjacent* escapes (common-values ↔ Regime B; repeated-interaction ↔ repeated-strategic-composition) are open extensions, not current canon. The two *outside* escapes (subsidies, second-best mechanisms) belong to mechanism-design proper. The framework's contribution at this charter instance is therefore *purely the boundary recognition*: AAT covers the agents-given-mechanism layer, not the mechanism-choice layer; the MS no-go binds at the latter.

**Peer voice with the mechanism-design literature.** The imported theorem is classical; the proof structure (Myerson-Satterthwaite via Myerson's virtual-valuations machinery) is mature. AAT does not re-prove the theorem; AAT does not displace the standard escape routes; AAT does not claim that the strategic-composition machinery extends to mechanism-choice. The segment's contribution is honest recognition of the boundary, with the imported theorem cited under its original name and full bibliographic references.

**Two open AAT-side extensions flagged.** The common-values ↔ Regime B adjacency and the repeated-interaction ↔ repeated-strategic-composition adjacency are open avenues. If AAT extends in either direction — formalizing shared-signal information regimes alongside the current intervention-regime classification, or extending strategic-composition into repeated-game form — the MS instance's boundary characterization would gain AAT-machinery content where it currently has honest scope-marks. The flags here document the avenues without committing to either extension.

## Findings

### The Bilateral Trade Boundary — Honest Scope-Marking as Contribution

**Brief:** When a buyer and seller each know their own valuation but not the other's, and the designer wants a trading mechanism that is at once fair (trade happens whenever the buyer values the good more than the seller does), incentive-honest (neither party can profitably misreport their valuation), voluntary (both parties want to participate), and self-funded (no outside subsidies), the Myerson-Satterthwaite theorem says all four cannot hold simultaneously. The classical escapes have been studied for decades — accept a budget deficit, accept inefficient withholding, exploit common-value information, or rely on long-run reputation in repeated trade. The honest contribution here is that *none* of these escapes is currently provided by the framework's machinery. The framework covers what the buyer and seller do *given* a mechanism (the two-sub-agent strategic-composition machinery applies cleanly to their best-response dynamics); the *designer's choice of mechanism* lives in mechanism-design proper, and the framework documents that boundary precisely rather than overclaiming reach. Two of the four classical escapes (common-values and repeated-interaction) are flagged as adjacent — open avenues if the framework extends in those directions — and two (subsidies and second-best mechanisms) belong entirely to mechanism design. The contribution is the map of where the framework meets the bilateral-trade boundary, not the provision of an escape.

**Impact:** The cleanest example of the `#disc-implementation-impossibility` cluster's discipline filter doing its honest work. Where the GS charter instance has a named sub-scope $\alpha'$ adjacency to make precise, the MS charter instance has *none* — the AAT-machinery contribution is purely boundary-recognition. That contrast within the cluster is itself epistemic content: the framework's contribution is precision about *where its machinery contributes* (GS: adjacent to preference-domain restriction) and *where it does not* (MS: outside almost entirely). Two open avenues flagged (common-values ↔ Regime B; repeated-interaction ↔ repeated-strategic-composition) document where future framework extensions could intersect MS without committing to either.

**Novelty Claim:** *Claim recognition* of the AAT-side translation of the Myerson-Satterthwaite theorem under the buyer-seller-as-two-sub-agent reading; *claim differentiation* on the agents-given-mechanism layer being internal to AAT and the mechanism-choice layer being external — the no-go binds at the latter, which is the honest scope-mark. The imported theorem is classical (Myerson & Satterthwaite 1983); the AAT-side translation, the boundary-characterization annotations, the honest *almost-entirely-outside* scope-mark, and the two open adjacencies (common-values, repeated-interaction) are the contributions.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| The imported theorem | Myerson, R. B. & Satterthwaite, M. A. (1983), "Efficient mechanisms for bilateral trading," *J. Econ. Theory* 29(2):265–281 (found pre-2026) | *formal antecedent* — primary-source verification scheduled for promotion past `draft` |
| Modern textbook synthesis | Krishna, V. (2002), *Auction Theory*, Academic Press, §5.3 (found pre-2026); Mas-Colell, Whinston & Green (1995), §23.E | *adjacent literature* — used for the constraint-regime formulation in the Setting above |
| Optimal mechanism design (second-best escape) | Myerson, R. B. (1981), "Optimal auction design," *Math. Oper. Res.* 6(1):58–73 (found pre-2026) | *adjacent literature* — the canonical second-best-escape construction; outside AAT canon per the discipline filter exclusion |
| Common-values bidding (adjacent escape) | Wilson, R. (1977), "A bidding model of perfect competition," *Rev. Econ. Stud.* 44(3):511–518 (found pre-2026) | *adjacent literature* — flagged as adjacent to `#scope-edge-update-causal-validity` Regime B; formal correspondence is open |
| Folk theorem (repeated-interaction escape) | Fudenberg, D. & Maskin, E. (1986), "The folk theorem in repeated games with discounting or with incomplete information," *Econometrica* 54(3):533–554 (found pre-2026) | *adjacent literature* — flagged as adjacent to repeated-strategic-composition extension of `#deriv-strategic-composition`; formal correspondence is open |

**Search Log:**

- 2026-05-22 (*intuition-only* on the buyer-seller-two-sub-agent reading): The natural composite-agent translation maps buyer and seller to two sub-agents per `#scope-composite-agent` with their own $O_t^{(i)}$. Alternative readings (single-agent-with-two-roles under intertemporal preference; large-economy aggregation limit) exist; not pursued here. Targeted future search candidates if alternative readings become relevant: Wilson 1977 large-economy bidding limit; behavioral / dual-self models of intertemporal trade.
- 2026-05-22 (*intuition-only* on the common-values ↔ Regime B adjacency): The common-values escape's structural feature (agents' reports carry shared signal about a partially-observable joint state) is reminiscent of `#scope-edge-update-causal-validity`'s Regime B (partial intervention; confounder-adjustment under side-channel observation). Whether the correspondence is formal or merely metaphorical is open. Targeted future search would compare the information-aggregation structure of common-values mechanisms (Wilson 1977; Pesendorfer-Swinkels 1997 *Econometrica* 65:1247–1281) against AAT's Regime B partial-intervention machinery.
- 2026-05-22 (*intuition-only* on the repeated-interaction ↔ repeated-strategic-composition adjacency): The repeated-bilateral-trade escape's structure (reputation backlash sustaining cooperation through grim-trigger or carrot-and-stick strategies) is the natural extension of strategic-composition to repeated games. Whether the formal correspondence holds is open. Targeted future search would compare the Folk-theorem machinery (Fudenberg-Maskin 1986; Fudenberg-Levine-Maskin 1994 *Econometrica* 62:997–1039) against a repeated-game extension of `#deriv-strategic-composition`.

## Working Notes

- **Provenance.** Authored 2026-05-22 as commit 3 of the post-Track-CR Track-B cycle, executing `spikes/implementation-impossibility-meta-segment-plan.md` §4.b. The 2026-05-20 strengthen-first arm record at `spikes/.integrated/spike-4th-identifiability-floor-instance-2026-05-20.md` §5 names MS as a candidate instance held back from the floor cluster (along with Arrow) pending the Joseph-reserved structural-canon decision on a sister meta-segment — Joseph approved the sister-meta-segment landing in this cycle; MS is the second charter instance of `#disc-implementation-impossibility`.
- **Open before `candidate`.** (a) Primary-source verification of Myerson & Satterthwaite 1983 — the theorem statement above is taken from the textbook synthesis (Krishna 2002 §5.3; Mas-Colell, Whinston & Green 1995 §23.E); direct primary-source reading is queued. (b) The two adjacent-escape correspondences (common-values ↔ Regime B; repeated-interaction ↔ repeated-strategic-composition) are *open* — flagged as adjacent in honest scope-mark, not derived. Lifting either to derived conditional would require formalizing the corresponding extension of AAT canon (`#scope-edge-update-causal-validity` Regime B's shared-signal interpretation, or a repeated-strategic-composition segment); both are open canonical work. (c) The buyer-seller-as-two-sub-agent reading is the natural composite-agent translation; alternative readings (single-agent-with-two-roles under intertemporal preference; large-economy aggregation) exist; not pursued here.
- **The honest-almost-entirely-outside scope-mark.** MS is the cluster instance where the AAT/mechanism-design boundary is *most* outside AAT — even more so than GS (where sub-scope $\alpha'$ is named-adjacent) and likely more than Arrow (where cardinal preferences are adjacent to `#form-objective-functional`). The cluster's discipline filter admits MS *because* it fits the constructive-impossibility shape (well-stated setting, external classical theorem, sharp no-go, characterized escapes); the honest scope-mark on most escapes being outside AAT canon is the segment's contribution, not a weakness. The three charter instances together illustrate the cluster's range — GS with one named adjacency, Arrow with one named adjacency plus one open avenue, MS with no current adjacencies but two open avenues.
