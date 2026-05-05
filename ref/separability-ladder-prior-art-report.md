# Separability ladder prior art

##### [**Undermind**](https://undermind.ai)

---


## Table of Contents

- [Direct answer](#direct-answer)
- [Closest prior-art parallels](#closest-prior-art-parallels)
- [Pearl-lineage finding](#pearl-lineage-finding)
- [Reverse-mathematics-adjacent finding](#reverse-mathematics-adjacent-finding)
- [Restricted-intervention lineage patch](#restricted-intervention-lineage-patch)
- [Neighboring recurrence inside restricted and mediated intervention work](#neighboring-recurrence-inside-restricted-and-mediated-intervention-work)
- [Applicability screening for the restricted-intervention search](#applicability-screening-for-the-restricted-intervention-search)
- [Simon and philosophy-of-modeling finding](#simon-and-philosophy-of-modeling-finding)
- [Naming candidates from the literature](#naming-candidates-from-the-literature)
- [Assessment of the strongest candidates](#assessment-of-the-strongest-candidates)
  - [\[Hin91\]](#hin91)
  - [\[Bas20\]](#bas20)
  - [\[Mac19\]](#mac19)
  - [\[Bar22\]](#bar22)
- [Evidence register](#evidence-register)
  - [Fully read in full text](#fully-read-in-full-text)
  - [Read at abstract or metadata level](#read-at-abstract-or-metadata-level)
  - [Potential high-value next candidates](#potential-high-value-next-candidates)
- [Search scope statement](#search-scope-statement)
- [Bottom line](#bottom-line)
- [References](#references)

A cross-domain name for the exact meta-pattern was not found in the retrieved literature. The strongest verified result is narrower: the Pearl and Shpitser identification lineage gives a clean, formal instance of the pattern inside causal inference, with complete algorithms for identifiable cases, explicit augmented regimes such as surrogate experiments and transportability, and graphical certificates for non-identifiability \[Shp06, Shp08, Bar12, Bar14, Lee19\]. A follow-on search on restricted-intervention prior art materially strengthens this internal causal lineage rather than overturning the report: pre-2021 work already treats intervention availability as restricted, regime-defined, or context-dependent in Robins’s treatment-regime framework, SWIGs, and decision-theoretic causality \[Rob86, Ric13, Daw00, Daw20, Ric23\]. Those papers do not merely gesture in this direction. \[Rob86\] explicitly defines generalized treatments only where a treatment is conceptually well defined and gives the G-computation algorithm under fully randomized structured-tree assumptions, while \[Ric13\] explicitly develops SWIGs in the presence of restricted interventions and notes that Robins’s original framework never required interventions on all variables. \[Daw00\] independently treats interventions as context-specific decisions whose meaning depends on the inquiry, not as a universal operator applicable without qualification. The nearest broader abstractions still sit adjacent to the target rather than coinciding with it. \[Hin91\] is now the strongest older abstract neighbor: it treats identifiability as a generalization of definability, distinguishing what a theory fixes by itself, what becomes fixed only with auxiliary empirical results, and what remains non-identifiable for logical reasons. \[Bas20\] gives a modern cross-field theory of identification with identifiable, partially identifiable, and strongly non-identifiable regimes. \[Mac19\] names ill-posed inverse problems as a recurring cross-field pattern linking causal inference, statistics, and inverse problems. \[Bar22\] and \[Pea18\] treat Pearl’s hierarchy as a general epistemic hierarchy and compare it to other hierarchies, but neither paper names or formalizes the specific no-go plus structured-recovery template as a cross-domain abstraction.

## Direct answer

No exact named cross-domain meta-pattern was found.

The most defensible answer at the current evidence level is:

- Not found at targeted depth, with full-text verification of the highest-value papers returned by the dedicated prior-art search, now including the strongest remaining philosophy and Simon-line candidates except for the unavailable information-theory paper \[Boc20\].

What was verified:

- The causal identification lineage does instantiate the pattern very strongly inside one domain. Observational identification, surrogate experiments, transportability, stochastic interventions, and related extensions are all formulated with complete procedures and impossibility witnesses \[Shp06, Shp08, Bar12, Bar14, Lee19, Cor20\].
- The broader abstraction does appear in adjacent form. \[Hin91\] gives a genuinely general theory of identifiability in which definability from theory alone, identifiability from theory plus auxiliary empirical results, and non-identifiability are distinguished at an abstract logical level. That is a strong neighbor to the target pattern, but it does not supply the named bounded-cost repair rung or the cross-domain theorem-schema you are seeking. \[Bas20\] abstracts identification across statistics, econometrics, causal inference, and finite population settings, but its organizing language is identification regions, injectivity, and assumptions rather than a named three-rung ladder. \[Mac19\] abstracts across causal inference and inverse problems, but the named pattern there is ill-posedness rather than separable core, structured repair, and open case.
- The best Pearl-lineage meta discussion remains intra-causal. \[Bar22\] compares Pearl’s hierarchy to formal-language and complexity hierarchies and treats it as a general logical and epistemic hierarchy, yet it does not claim a unified cross-domain theorem-schema for the recurring pattern you are targeting.
- The Simon and philosophy-of-modeling line is now better constrained. \[Iwa94\] and \[Hoo12b\] strongly support hierarchy, near-decomposability, aggregation, and model families with different levels of articulation, but they do not formulate the target no-go plus structured-recovery ladder as a named cross-domain abstraction.
- The restricted-intervention follow-on search patches a real gap. It shows that \[Gha21\] should not be treated as an origin point. The missing lineage runs through Robins treatment-regime semantics \[Rob86\], the SWIG bridge \[Ric13\], and Dawid’s decision-theoretic regime-indicator program \[Daw00, Daw20\], with \[Ric23\] explicitly relating the SWIG and decision-theoretic lines. Full-text reading now makes this patch firmer. \[Rob86\] gives treatment-regime semantics with feasibility constraints and named recovery machinery through G-computation under fully randomized MCISTGs. \[Ric13\] devotes a full section to restricted interventions and explicitly states that FFRCISTGs did not require interventions on all variables. \[Daw00\] treats causal effects through decision nodes and inquiry-relative intervention meanings. This strengthens the claim that the pattern recurs across neighboring identification literatures inside causality, but it still does not supply a named cross-domain abstraction.

## Closest prior-art parallels

| Rank | Paper | What it names or formalizes | Relation to the target |
|:---|:---|:---|:---|
| 1 | \[Shp06\], \[Shp08\] | Complete identification methods, ID algorithm, hedge non-identifiability | Best formal instance-level match. Clear separable cases, systematic recovery, and no-go certificates, but confined to causal inference |
| 2 | \[Bar12\], \[Bar14\], \[Lee19\] | z-identifiability, transportability, g-identifiability | Strongest structured-repair variants. Each adds a named augmentation and a complete criterion, but still within the causal program |
| 3 | \[Rob86\], \[Ric13\], \[Daw00\], \[Daw20\], \[Ric23\] | Restricted intervention semantics, SWIGs, decision-theoretic causality | Missing lineage for restricted-intervention models. Now verified in core full texts and strongly applicable to the report patch, but still an internal causal lineage rather than a cross-domain abstraction |
| 4 | \[Rob10\], \[Rob20\], \[Ste19\], \[Dia22\], \[Shp14\] | Alternative graphical models, interventionist mediation, separable effects, edge or path interventions | Strong neighboring recurrence of the target shape inside causal identification, especially when standard interventions are infeasible or insufficient |
| 5 | \[Hin91\] | General theory of identifiability as a generalization of definability | Strong older abstract neighbor. Distinguishes theory-alone determination, determination with auxiliary empirical results, and non-identifiability, but does not provide the target repair-ladder template |
| 6 | \[Bas20\] | General theory of identification | Closest modern formal abstraction across fields. Gives identifiable, partially identified, strongly non-identifiable regimes, but not the exact ladder or repair operator template |
| 7 | \[Mac19\] | Identifiability, estimability, ill-posed inverse problems | Strong cross-field dual structure. Clear positive and no-go sides, but no bounded-cost repair rung as the central abstraction |
| 8 | \[Bar22\] | Pearl hierarchy as logical and epistemic hierarchy | Partial meta discussion. Explicitly compares Pearl’s hierarchy to other hierarchies, but does not extract the target meta-pattern |
| 9 | \[Hoo12b\], \[Iwa94\] | Hierarchies of models, causality and model abstraction | Strong philosophy and Simon-line parallels around aggregation, repair perspectives, and near-decomposability, but not a formal tractability or identifiability ladder |
| 10 | \[Kli23\], \[Tam10\], \[Man10\] | Partial identification | Strong on graded information under stronger assumptions. Weak on named repair operators and external impossibility witnesses |
| 11 | \[Dow95\], \[Dow95b\] | Fixed-parameter tractability and completeness, W-hierarchy | Strong tractability ladder. Good analogy for bounded structural augmentation, but this is runtime classification rather than identification |
| 12 | \[Ibe21\] | Topological causal hierarchy theorem | Strong no-go side with an explicit analogy to no-free-lunch results, but still causal and not a full positive ladder |
| 13 | \[Sim99\], \[Cho09\], \[Hir96\], \[Che24c\], \[Oli25b\] | Reverse mathematics and meta-mathematics of complexity | Strong hierarchy-of-strength literature. Verified weak connection to applied identifiability ladders |

## Pearl-lineage finding

The Pearl lineage is the clearest verified source of the target shape, but only as a family of internal causal formalisms.

\[Pea95\] already states the basic template in embryo. Graphs determine when causal effects are identifiable from observational data and, when they are not, can suggest additional observations or auxiliary experiments that make identification feasible. That is very close to separable core plus structured repair, but it is presented as causal methodology rather than as a reusable cross-domain abstraction.

\[Shp06\] sharpens this into a complete identification program. The ID algorithm returns an estimand when recovery is possible and fails only when a hedge certifies non-identifiability. This is the cleanest verified no-go plus recovery pairing in the corpus. \[Shp08\] extends the same logic across Pearl’s hierarchy, giving complete methods for interventional and counterfactual identification and graphical certificates of failure at each level.

The later extensions preserve the same shape while varying the repair object:

- \[Bar12\] uses surrogate experiments as the repair mechanism.
- \[Bar14\] uses selection diagrams and limited experiments across environments for transportability.
- \[Lee19\] generalizes to arbitrary collections of experimental inputs and proves completeness using hedgelets and thickets.
- \[Cor20\] extends the machinery to stochastic interventions using sigma-calculus.
- \[Shp14\] unifies node, edge, and path interventions within a single intervention hierarchy.

What is missing is the step from repeated internal generalization to explicit cross-domain abstraction. None of the full-text Pearl-lineage papers verified here say that this recurring structure is a general theorem-schema for scope-honest theorizing across applied mathematics. The closest move in that direction is \[Bar22\]. It treats Pearl’s hierarchy as a logical and epistemic hierarchy, and it explicitly compares it with formal-language and complexity hierarchies. But the paper’s thesis remains that Pearl’s hierarchy has a distinctive status, not that many structurally different hierarchies share a common separability-ladder form \[Bar22\].

## Reverse-mathematics-adjacent finding

The reverse-mathematics and hierarchy-theory literature does not, in the verified set, bridge into applied identifiability or tractability ladders in the way your question requires.

\[Sim99\] gives the canonical hierarchy of subsystem strength. \[Cho09\] presents reverse mathematics and computability as ways to calibrate theorem strength along standard proof-theoretic and computational yardsticks. \[Hir96\] makes one of the closest bridges in the retrieved set by showing parallels between finite complexity classes and the recursion-theoretic and proof-theoretic strength of infinite analogues. \[Che24c\] brings this into current complexity theory by showing that various lower-bound statements are equivalent to core combinatorial principles. \[Oli25b\] surveys the same meta-mathematical territory.

These papers do establish that hierarchies of strength, provability, and computational complexity are studied as mathematical objects. What they do not appear to do is connect those hierarchies to applied identifiability frameworks such as causal identification, partial identification, surrogate experimentation, or structured scientific repair. The retrieved evidence therefore supports a negative answer for this bridge as well: no verified paper in the set connects reverse mathematics or computability hierarchy theory to the target applied-math meta-pattern.

## Restricted-intervention lineage patch

The new search materially improves the report’s treatment of restricted or partial intervention semantics.

The main positive result is lineage, not a new cross-domain name. \[Rob86\] is the foundational anchor for treatment-regime semantics where interventions are defined through available regimes rather than treated as universally meaningful operations. It defines generalized treatments only where a treatment is conceptually feasible, and its recovery theory is built around G-computation under fully randomized structured-tree assumptions. \[Ric13\] is the key graphical bridge, making that restricted potential-outcome perspective explicit through SWIGs and devoting a full section to restricted interventions. It also states that FFRCISTGs as defined by Robins did not require interventions on all variables. \[Daw00\] and \[Daw20\] develop a parallel decision-theoretic account in which interventions are represented by decision or regime nodes and justified as context-specific actions whose meaning depends on the inquiry. \[Ric23\] then explicitly relates the SWIG and decision-theoretic lines, showing that the supposedly separate formalisms are closely aligned.

This means the withdrawn \[Gha21\] should be treated as a late synthesis attempt rather than as an origin point. The missing prior-art lineage for restricted-intervention models is real and now substantially patched.

In terms of the original separability-ladder question, these papers are applicable but only in a bounded way. They matter because they show that intervention scope, manipulability, and regime availability were already being treated as structured constraints well before 2021. They support a ladder-like reading only weakly. \[Rob86\] comes closest through a tractable core under fully randomized assumptions, structured recovery through named g-methods, and explicit warnings about non-identifiable biological effects without stronger assumptions. \[Rob10\] then sharpens the neighboring recurrence by comparing agnostic, minimal, FFRCISTG, and NPSEM models and showing how richer expanded graphs can convert a non-manipulable direct effect into a manipulable, identifiable contrast. Even so, none of these papers names the full cross-domain separable-core, structured-repair, general-open pattern as a unified abstraction.

## Neighboring recurrence inside restricted and mediated intervention work

The follow-on search also strengthens the claim that the target shape recurs across nearby identification problems within causality.

\[Rob20\] is the clearest verified example. It replaces standard natural-effect reasoning with an interventionist framework based on decomposing treatment into separable components on an expanded graph. In the clean case, edge-expanded graphs support identification. In richer cases, identification depends on the absence of a recanting witness or recanting district. This is very close to the target pattern: a clean separable core, a structured repair through a named intervention decomposition, and a no-go obstruction.

\[Rob10\] now looks more important than a mere side precursor. It compares agnostic, minimal, FFRCISTG, and NPSEM model classes, makes the identification boundary for pure direct effects explicit, and shows that a richer expanded graph can turn a non-manipulable effect in the clean graph into a manipulable and identifiable contrast. That makes it strong direct prior art for neighboring recurrence under restricted-intervention or separable-treatment reasoning, not just adjacent mediation theory.

\[Ste19\] supplies a closely related recurrence in competing-risk settings. Its separable effects are identifiable only when treatment can be decomposed into components with dismissible pathways. Without those assumptions, interpretation and identification break down. \[Dia22\] gives another neighboring recurrence using information-transfer or non-agency interventions, explicitly designed for settings where ordinary node interventions are infeasible, such as non-manipulable causes or intermediate confounding. \[Shp14\] fits the same broader neighborhood by showing that richer intervention languages recover effects that simpler formulations cannot identify.

These papers strengthen the narrow claim in the report. The pattern is not only present in classic Pearl-style effect identification; it also recurs in mediation, competing-event decomposition, edge-intervention, and restricted-intervention settings inside the wider causal-identification literature.

## Applicability screening for the restricted-intervention search

| Applicability | Papers | Why they matter for the original question |
|:---|:---|:---|
| Directly applicable as missing lineage | \[Rob86\], \[Ric13\], \[Daw00\], \[Daw20\], \[Ric23\] | Establish prior art for restricted or regime-defined intervention semantics that the withdrawn \[Gha21\] likely needed to engage |
| Strongly applicable as neighboring recurrence of the pattern | \[Rob10\], \[Rob20\], \[Ste19\], \[Dia22\], \[Shp14\] | Show clean cases, named structured intervention repairs, and obstruction results within nearby causal-identification problems |
| Applicable but mainly as philosophical or methodological framing | \[Daw10\], \[Daw02\], \[Gen05\], \[Gen07\], \[May18\], \[May14\] | Clarify piecemeal experimentation, dynamic strategies, or decision-theoretic semantics, but do not by themselves supply the target ladder |
| Weakly applicable or mostly contrastive | \[Pea19b\] | Useful mainly because it argues against restricting do semantics to manipulable variables, which marks a contrast with the restricted-intervention line rather than supporting the target pattern |
| Not usable as positive support | \[Gha21\] | Withdrawn, and the withdrawal note itself suggests missing prior work rather than a reliable anchor |

## Simon and philosophy-of-modeling finding

The Simon line is now more fully checked, and it still stops short of the target abstraction.

\[Iwa94\] develops a general account of causality and model abstraction centered on structural equations, manipulability, aggregation, and near-decomposability. It is strongest on preservation of causal ordering across levels of abstraction and on the conditions under which abstraction remains faithful. That is relevant background for the separable-core intuition, especially where weakly coupled subsystems can be treated as black boxes, but it is not organized as a three-rung tractability or identifiability ladder.

\[Hoo12b\] is the closest philosophy-of-modeling parallel in the verified set. It discusses hierarchies of models, Simon-style causal structure, and families of models with different levels of articulation. Its well-made toaster and repairman contrast comes close to a clean case versus repair case distinction, and its broader discussion of aggregation and elaboration comes close to a family resemblance with your target pattern. But the paper is best read as philosophy of modeling and perspectival causal realism, not as a formal cross-domain theorem-schema about no-go regions and structured recovery.

## Naming candidates from the literature

No existing name in the retrieved set cleanly supersedes a coinage such as separability ladder.

The nearest usable anchors are these:

| Candidate label | Source | Usefulness | Limitation |
|:---|:---|:---|:---|
| Causal hierarchy | \[Shp08\], \[Bar22\] | Strong anchor for one instance and for the idea of strict levels of inferential power | Specific to Pearl-lineage causality |
| Graphical hierarchy of interventions | \[Shp14\] | Useful when emphasizing nested intervention regimes | Still intra-causal |
| Partial identification | \[Tam10\], \[Kli23\], \[Man10\] | Strong anchor for graded informativeness under varying assumptions | Lacks the structured-repair operator idea |
| General theory of identifiability | \[Hin91\] | Strong older abstract anchor for theory alone, theory plus empirical results, and non-identifiability | Does not supply the explicit structured-repair rung or a named cross-domain ladder |
| General theory of identification | \[Bas20\] | Best nearby modern abstract language across fields | Organizes by identification region, not by repair ladder |
| Ill-posed inverse problems | \[Mac19\] | Best nearby cross-field no-go language | Centers stability and estimability rather than structured recovery |
| Fixed-parameter tractability and completeness | \[Dow95\], \[Dow95b\] | Best nearby tractability-ladder language | Runtime hierarchy, not identification hierarchy |

If a new family name is introduced, the safest positioning is that it is adjacent to these literatures rather than replacing an established cross-domain term.

## Assessment of the strongest candidates

### \[Hin91\]

This is now the strongest older abstract neighbor. It explicitly treats identifiability as a generalization of definability, separating what a theory fixes by itself from what becomes fixed only with auxiliary empirical results, and from what remains non-identifiable for logical reasons. That makes it strikingly close at the level of abstract shape. But it still does not provide the full target package: there is no named bounded-cost repair operator, no explicit cross-domain ladder label, and no theorem that scope-honest theories must instantiate this trichotomy.

### \[Bas20\]

This is the best modern abstract neighbor. It explicitly aims to unify definitions of identification across multiple fields, and it distinguishes identifiable, partially recoverable, and strongly non-identifiable regimes. That makes it highly relevant for a prior-art table. But its core language is binary relations, identification regions, and assumption-induced restrictions on the statistical universe. It does not single out a named bounded-cost repair operator as the middle rung, and it does not present a theorem that any broad-but-exact theory must take trichotomic form.

### \[Mac19\]

This is the best dual-structure neighbor. It reframes causal identification and estimation as inverse problems, with identifiability corresponding to uniqueness and estimability to well-posedness. Its strongest cross-field move is to name ill-posedness as the recurring phenomenon across causal inference, inverse problems, and robust statistics. That is very close to your negative-half and positive-half complementarity, but the middle rung is stability and regularization rather than named structured repair.

### \[Bar22\]

This is the best verified Pearl-lineage paper for meta discussion. It treats Pearl’s hierarchy as a formal structure, compares it to other hierarchies, and uses the causal hierarchy theorem to mark principled barriers to climbing from lower layers to higher ones. That said, it does not identify a recurring cross-domain three-rung pattern. Its comparisons are analogical and contrastive, not a unifying abstraction.

## Evidence register

### Fully read in full text

| Paper | Why it was fully read | Role in the report |
|:---|:---|:---|
| \[Bar22\] | Highest-value Pearl-lineage meta paper | Best evidence for and against a cross-domain reading |
| \[Shp08\] | Core completeness paper for causal hierarchy | Main instance-level formalization |
| \[Shp06\] | Foundational ID completeness paper | Main source for recovery plus no-go pairing |
| \[Lee19\] | Generalized repair regime with arbitrary experiments | Strong structured-repair evidence |
| \[Bar14\] | Transportability with limited experiments | Strong repair and impossibility evidence |
| \[Bar12\] | Surrogate experiments | Canonical bounded augmentation case |
| \[Cor20\] | Stochastic intervention extension | Shows the pattern persists inside causal generalizations |
| \[Shp14\] | Intervention hierarchy unification | Tests whether Pearl-lineage work became meta-level |
| \[Ibe21\] | Topological no-go result | Strongest impossibility-side adjacent paper |
| \[Pea95\] | Foundational causal-diagram paper | Early statement of identify or augment template |
| \[Bas20\] | Cross-field abstraction candidate | Best abstract prior-art neighbor |
| \[Mac19\] | Cross-field ill-posedness candidate | Best dual-structure prior-art neighbor |
| \[Ibe20\] | Logical-language hierarchy paper | Tests hierarchy formalization outside standard SCM prose |
| \[Che24c\] | Reverse-math candidate | Tests bridge to applied hierarchy claims |
| \[Kli23\] | Modern partial-identification review | Best recent abstract for assumption-graded information |
| \[Dow95\] | Parameterized complexity anchor | Best tractability-ladder analogue |
| \[Oli25b\] | Meta-mathematics survey | Tests modern proof-theoretic bridge |
| \[Pea18\] | AI and epistemic use of Pearl’s ladder | Broadens Pearl’s hierarchy beyond narrow causal inference |
| \[Hin91\] | Older general-identifiability candidate | Strong abstract neighbor to the target pattern |
| \[Iwa94\] | Simon-line causality and abstraction | Tests whether near-decomposability becomes a repair ladder |
| \[Hoo12b\] | Philosophy of modeling and hierarchies | Tests model-family parallels to clean and repair cases |
| \[Daw20\] | Decision-theoretic restricted-intervention anchor | Verifies regime-indicator semantics and bridges to other causal formalisms |
| \[Ric23\] | SWIG and decision-theoretic bridge | Verifies the missing lineage around restricted interventions |
| \[Rob20\] | Interventionist mediation and separable components | Strong neighboring recurrence of the target pattern |
| \[Ste19\] | Separable effects in competing events | Strong neighboring recurrence under explicit decomposition assumptions |
| \[Dia22\] | Non-agency and information-transfer interventions | Tests repair when ordinary node interventions are infeasible |
| \[Daw10\] | Dynamic treatment strategies in DT framework | Clarifies the restricted-intervention lineage and its assumptions |
| \[Rob86\] | Earliest treatment-regime anchor | Verifies feasibility-constrained interventions and g-computation lineage |
| \[Ric13\] | SWIG bridge paper | Verifies restricted interventions explicitly |
| \[Daw00\] | Early decision-theoretic anchor | Verifies inquiry-relative intervention semantics |
| \[Rob10\] | Alternative models and direct effects | Strong neighboring recurrence under expanded graphs |

### Read at abstract or metadata level

| Paper | Why kept in scope | Current status |
|:---|:---|:---|
| \[Tam10\] | Canonical partial-identification survey | Abstract and metadata read |
| \[Man10\] | Manski-line partial-identification anchor | Metadata read |
| \[Sim99\] | Canonical reverse-mathematics source | Metadata read |
| \[Cho09\] | Reverse mathematics and computability overview | Abstract and metadata read |
| \[Hir96\] | Finite complexity to infinite proof-strength bridge | Abstract and metadata read |
| \[Dow95b\] | W\[1\] completeness companion paper | Metadata read |
| \[Hua06\] | Alternative completeness result in causal ID | Abstract and metadata read |
| \[Gha21\] | Restricted intervention framework | Abstract and metadata read |
| \[Bha19\] | Missing-data identification generalization | Abstract and metadata read |
| \[Nab20\] | Missing-data completeness result | Abstract and metadata read |
| \[Boc20\] | Achievability and converse computability angle | Abstract and metadata read |
| \[Wit16\] | Parameterized complexity and computability bridge | Abstract and metadata read |
| \[Blu97\] | Broad complexity framework | Metadata only |
| \[Gha21\] | Withdrawn restricted-intervention synthesis draft | Not used as positive support |

### Potential high-value next candidates

| Paper | Reason to read next | Likely payoff |
|:---|:---|:---|
| \[Boc20\] | Achievability and converse computability | Best remaining information-theoretic candidate for the dual positive and impossibility structure |
| \[Nab20\] | Completeness in missing-data models | Could strengthen the claim that Pearl-style ladders recur within adjacent identification domains |
| \[Bha19\] | Identification algorithm beyond standard ID manipulations | Similar value to \[Nab20\] for internal recurrence |
| \[Dow95b\] | Completeness for W\[1\] | Strengthens the complexity-side analogy |

## Search scope statement

This report is based on the completed project searches Cross domain separability ladder prior art and Restricted intervention prior art for separability ladder, together with subsequent verification reads inside the project workspace. Across the two searches, the project surfaced papers spanning causal inference, econometrics, complexity theory, reverse mathematics, philosophy-adjacent structural work, mediation, restricted interventions, and information-theoretic or meta-mathematical candidates. Thirty-one papers were read in full text. The remaining candidates were checked at abstract or metadata level.

The honest depth label is still targeted rather than comprehensive. The evidence base is now stronger in the restricted-intervention and neighboring mediation literatures, and the highest-value Pearl-lineage, general-identifiability, Simon-line, and decision-theoretic candidates presently available in the project have been verified in full text. The core restricted-intervention anchors \[Rob86\], \[Ric13\], \[Daw00\], and \[Rob10\] are now checked in full text rather than only by abstract. The strongest remaining open candidate in the information-theory direction, \[Boc20\], still could not be checked in full text. The strongest defensible claim is therefore still not found at targeted depth after full-text verification of the core candidate set.

## Bottom line

The literature verified here supports a narrow and a broad claim.

The narrow claim is yes: the causal-identification literature contains multiple mature formal instances of the no-go plus structured-recovery pattern, including the Pearl-lineage identification program \[Shp06, Shp08, Bar12, Bar14, Lee19\], missing-data identification \[Bha19, Nab20\], and now more clearly the restricted-intervention and interventionist-mediation neighborhood \[Rob20, Ste19, Dia22\].

The broad claim is still no, at current depth: no paper in the verified set names or formalizes the exact cross-domain meta-pattern as a unified abstraction. The nearest neighbors are \[Hin91\] for general identifiability, \[Bas20\] for general identification, \[Mac19\] for ill-posed inverse problems, the restricted-intervention lineage \[Rob86, Ric13, Daw00, Daw20, Ric23\], the neighboring recurrence papers \[Rob10, Rob20, Ste19, Dia22\], \[Bar22\] for hierarchy-as-epistemic-structure, and \[Hoo12b\] for philosophy-of-modeling parallels. Together they provide adjacent prior art, not direct anticipation.

---

## References

\[Shp06\] I. Shpitser and J. Pearl, “Identification of Joint Interventional Distributions in Recursive Semi-Markovian Causal Models,” *AAAI Conference on Artificial Intelligence*, pp. 1219–1226, Jul. 2006.

\[Shp08\] I. Shpitser and J. Pearl, “Complete Identification Methods for the Causal Hierarchy,” *J. Mach. Learn. Res.*, vol. 9, pp. 1941–1979, Jun. 2008, doi: [10.5555/1390681.1442797](https://doi.org/10.5555/1390681.1442797).

\[Bar12\] E. Bareinboim and J. Pearl, “Causal Inference by Surrogate Experiments: z-Identifiability,” *Conference on Uncertainty in Artificial Intelligence*, pp. 113–120, Aug. 2012.

\[Bar14\] E. Bareinboim and J. Pearl, “Transportability from Multiple Environments with Limited Experiments: Completeness Results,” *Neural Information Processing Systems*, pp. 280–288, Dec. 2014.

\[Lee19\] S. Lee, J. D. Correa, and E. Bareinboim, “General Identifiability with Arbitrary Surrogate Experiments,” *Conference on Uncertainty in Artificial Intelligence*, pp. 389–398, 2019.

\[Rob86\] J. Robins, “A new approach to causal inference in mortality studies with a sustained exposure period—application to control of the healthy worker survivor effect,” 1986. doi: [10.1016/0270-0255(86)90088-6](https://doi.org/10.1016/0270-0255(86)90088-6).

\[Ric13\] T. Richardson, “Single World Intervention Graphs ( SWIGs ) : A Unification of the Counterfactual and Graphical Approaches to Causality,” 2013.

\[Daw00\] A. Dawid, “Causal Inference without Counterfactuals,” Jun. 01, 2000. doi: [10.1080/01621459.2000.10474210](https://doi.org/10.1080/01621459.2000.10474210).

\[Daw20\] P. Dawid, “Decision-theoretic foundations for statistical causality,” Apr. 26, 2020. doi: [10.1515/jci-2020-0008](https://doi.org/10.1515/jci-2020-0008).

\[Ric23\] T. Richardson and J. Robins, “Potential outcome and decision theoretic foundations for statistical causality,” *Journal of Causal Inference*, vol. 11, Jan. 2023, doi: [10.1515/jci-2022-0012](https://doi.org/10.1515/jci-2022-0012).

\[Hin91\] J. Hintikka, “Towards a General Theory of Identifiability,” 1991. doi: [10.1007/978-94-011-3346-3_7](https://doi.org/10.1007/978-94-011-3346-3_7).

\[Bas20\] G. W. Basse and I. Bojinov, “A general theory of identification,” Feb. 14, 2020.

\[Mac19\] O. J. Maclaren and R. Nicholson, “What can be estimated? Identifiability, estimability, causal inference and ill-posed inverse problems,” *ArXiv*, vol. abs/1904.02826, Apr. 2019.

\[Bar22\] E. Bareinboim, J. D. Correa, D. Ibeling, and T. F. Icard, *On Pearl’s Hierarchy and the Foundations of Causal Inference*. 2022. doi: [10.1145/3501714.3501743](https://doi.org/10.1145/3501714.3501743).

\[Pea18\] J. Pearl, “Theoretical Impediments to Machine Learning With Seven Sparks from the Causal Revolution,” *Proceedings of the Eleventh ACM International Conference on Web Search and Data Mining*, Jan. 2018, doi: [10.1145/3159652.3176182](https://doi.org/10.1145/3159652.3176182).

\[Boc20\] H. Boche, R. F. Schaefer, and H. Poor, “On the Algorithmic Computability of Achievability and Converse: ϵ-Capacity of Compound Channels and Asymptotic Bounds of Error-Correcting Codes,” *2020 IEEE International Symposium on Information Theory (ISIT)*, pp. 2008–2013, Jun. 2020, doi: [10.1109/ISIT44484.2020.9174342](https://doi.org/10.1109/ISIT44484.2020.9174342).

\[Cor20\] J. C. Correa and E. Bareinboim, “A Calculus for Stochastic Interventions: Causal Effect Identification and Surrogate Experiments,” *AAAI Conference on Artificial Intelligence*, pp. 10093–10100, Apr. 2020, doi: [10.1609/AAAI.V34I06.6567](https://doi.org/10.1609/AAAI.V34I06.6567).

\[Iwa94\] Y. Iwasaki and H. Simon, “Causality and Model Abstraction,” *Artif. Intell.*, vol. 67, pp. 143–194, May 1994, doi: [10.1016/0004-3702(94)90014-0](https://doi.org/10.1016/0004-3702(94)90014-0).

\[Hoo12b\] K. D. Hoover, “Causal structure and hierarchies of models.” *Studies in history and philosophy of biological and biomedical sciences*, vol. 43 4, pp. 778–86, Dec. 2012, doi: [10.1016/j.shpsc.2012.05.007](https://doi.org/10.1016/j.shpsc.2012.05.007).

\[Gha21\] A. Ghassami and I. Shpitser, “Partially Intervenable Causal Models,” *ArXiv*, vol. abs/2110.12541, Oct. 2021.

\[Rob10\] J. Robins and T. Richardson, “Alternative Graphical Causal Models and the Identification of Direct E!ects,” 2010. doi: [10.1093/oso/9780199754649.003.0011](https://doi.org/10.1093/oso/9780199754649.003.0011).

\[Rob20\] J. Robins, T. Richardson, and I. Shpitser, *An Interventionist Approach to Mediation Analysis*. 2020. doi: [10.1145/3501714.3501754](https://doi.org/10.1145/3501714.3501754).

\[Ste19\] M. Stensrud, J. G. Young, V. Didelez, J. Robins, and M. A. Hern’an, “Separable Effects for Causal Inference in the Presence of Competing Events,” Jan. 28, 2019. doi: [10.1080/01621459.2020.1765783](https://doi.org/10.1080/01621459.2020.1765783).

\[Dia22\] I. D’iaz, “Non-agency interventions for causal mediation in the presence of intermediate confounding,” *Journal of the Royal Statistical Society Series B: Statistical Methodology*, May 2022, doi: [10.1093/jrsssb/qkad130](https://doi.org/10.1093/jrsssb/qkad130).

\[Shp14\] I. Shpitser and E. Tchetgen, “CAUSAL INFERENCE WITH A GRAPHICAL HIERARCHY OF INTERVENTIONS.” *Annals of statistics*, vol. 44 6, pp. 2433–2466, Nov. 2014, doi: [10.1214/15-AOS1411](https://doi.org/10.1214/15-AOS1411).

\[Kli23\] B. Kline and E. Tamer, “Recent Developments in Partial Identification,” *Annual Review of Economics*, Sep. 2023, doi: [10.1146/annurev-economics-051520-021124](https://doi.org/10.1146/annurev-economics-051520-021124).

\[Tam10\] E. Tamer, “Partial Identification in Econometrics,” Aug. 11, 2010. doi: [10.1146/ANNUREV.ECONOMICS.050708.143401](https://doi.org/10.1146/ANNUREV.ECONOMICS.050708.143401).

\[Man10\] C. Manski, “Partial Identification in Econometrics,” 2010. doi: [10.1057/9780230280816_21](https://doi.org/10.1057/9780230280816_21).

\[Dow95\] R. G. Downey and M. Fellows, “Fixed-Parameter Tractability and Completeness I: Basic Results,” *SIAM J. Comput.*, vol. 24, pp. 873–921, Aug. 1995, doi: [10.1137/S0097539792228228](https://doi.org/10.1137/S0097539792228228).

\[Dow95b\] R. Downey and M. Fellows, “Fixed-Parameter Tractability and Completeness II: On Completeness for W\[1\],” *Theor. Comput. Sci.*, vol. 141, pp. 109–131, Apr. 1995, doi: [10.1016/0304-3975(94)00097-3](https://doi.org/10.1016/0304-3975(94)00097-3).

\[Ibe21\] D. Ibeling and T. F. Icard, “A Topological Perspective on Causal Inference,” *Neural Information Processing Systems*, pp. 5608–5619, Jul. 2021.

\[Sim99\] S. G. Simpson, “Subsystems of second order arithmetic,” Jan. 15, 1999. doi: [10.1017/cbo9780511581007](https://doi.org/10.1017/cbo9780511581007).

\[Cho09\] P. A. Cholak, “Computability, Reverse Mathematics and Combinatorics,” 2009.

\[Hir96\] J. Hirst and S. Lempp, “Infinite Versions of Some Problems From Finite Complexity Theory,” *Notre Dame J. Formal Log.*, vol. 37, pp. 545–553, Oct. 1996, doi: [10.1305/ndjfl/1040046141](https://doi.org/10.1305/ndjfl/1040046141).

\[Che24c\] L. Chen, J. Li, and I. C. Oliveira, “Reverse Mathematics of Complexity Lower Bounds,” *2024 IEEE 65th Annual Symposium on Foundations of Computer Science (FOCS)*, pp. 505–527, Oct. 2024, doi: [10.1109/FOCS61266.2024.00040](https://doi.org/10.1109/FOCS61266.2024.00040).

\[Oli25b\] I. C. Oliveira, “SIGACT News Complexity Theory Column 124 Meta-Mathematics of Computational Complexity Theory,” *ACM SIGACT News*, vol. 56, pp. 41–68, Mar. 2025, doi: [10.1145/3726856.3726862](https://doi.org/10.1145/3726856.3726862).

\[Pea95\] J. Pearl, “Causal diagrams for empirical research,” Dec. 01, 1995. doi: [10.1093/BIOMET/82.4.669](https://doi.org/10.1093/BIOMET/82.4.669).

\[Daw10\] A. Dawid and V. Didelez, “Identifying the consequences of dynamic treatment strategies: A decision-theoretic overview,” *ArXiv*, vol. abs/1010.3425, Oct. 2010, doi: [10.1214/10-SS081](https://doi.org/10.1214/10-SS081).

\[Daw02\] A. Dawid, “Influence Diagrams for Causal Modelling and Inference,” Aug. 01, 2002. doi: [10.1111/j.1751-5823.2002.tb00354.x](https://doi.org/10.1111/j.1751-5823.2002.tb00354.x).

\[Gen05\] S. Geneletti, “Aspects of casual inference in a non-counterfactual framework.” 2005.

\[Gen07\] S. Geneletti, “Identifying direct and indirect effects in a non‐counterfactual framework,” Apr. 01, 2007. doi: [10.1111/j.1467-9868.2007.00584.x](https://doi.org/10.1111/j.1467-9868.2007.00584.x).

\[May18\] C. Mayo-Wilson, “Causal identifiability and piecemeal experimentation,” *Synthese*, vol. 196, pp. 3029–3065, May 2018, doi: [10.1007/s11229-018-1826-4](https://doi.org/10.1007/s11229-018-1826-4).

\[May14\] C. Mayo-Wilson, “The Limits of Piecemeal Causal Inference,” Jun. 01, 2014. doi: [10.1093/bjps/axs030](https://doi.org/10.1093/bjps/axs030).

\[Pea19b\] J. Pearl, “On the Interpretation of do ( x ),” 2019.

\[Ibe20\] D. Ibeling and T. F. Icard, “Probabilistic Reasoning across the Causal Hierarchy,” *AAAI Conference on Artificial Intelligence*, pp. 10170–10177, Jan. 2020, doi: [10.1609/AAAI.V34I06.6577](https://doi.org/10.1609/AAAI.V34I06.6577).

\[Hua06\] Y. Huang and M. Valtorta, “Identifiability in Causal Bayesian Networks: A Sound and Complete Algorithm,” *AAAI Conference on Artificial Intelligence*, pp. 1149–1154, Jul. 2006.

\[Bha19\] R. Bhattacharya, R. Nabi, I. Shpitser, and J. Robins, “Identification In Missing Data Models Represented By Directed Acyclic Graphs,” *Uncertainty in artificial intelligence : proceedings of the ... conference. Conference on Uncertainty in Artificial Intelligence*, vol. 2019, Jun. 2019.

\[Nab20\] R. Nabi, R. Bhattacharya, and I. Shpitser, “Full Law Identification In Graphical Models Of Missing Data: Completeness Results,” *Proceedings of machine learning research*, vol. 119, pp. 7153–7163, Apr. 2020.

\[Wit16\] J. Witteveen and L. Torenvliet, “Fixed‐parameter decidability: Extending parameterized complexity analysis,” *Mathematical Logic Quarterly*, vol. 62, Nov. 2016, doi: [10.1002/malq.201500077](https://doi.org/10.1002/malq.201500077).

\[Blu97\] L. Blum, “Complexity and Real Computation,” Oct. 30, 1997. doi: [10.1007/978-1-4612-0701-6](https://doi.org/10.1007/978-1-4612-0701-6).
