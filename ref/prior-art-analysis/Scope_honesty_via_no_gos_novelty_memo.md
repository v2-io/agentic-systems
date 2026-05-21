# Scope honesty via no gos novelty memo

##### [**Undermind**](https://undermind.ai)

---


## Table of Contents

- [Scope honesty via no gos novelty memo](#scope-honesty-via-no-gos-novelty-memo)
  - [Overall judgment](#overall-judgment)
  - [Claim under review](#claim-under-review)
  - [Prior art by claim component](#prior-art-by-claim-component)
  - [What the prior art already establishes](#what-the-prior-art-already-establishes)
  - [Where AAT seems genuinely new](#where-aat-seems-genuinely-new)
  - [Stress tests that matter most](#stress-tests-that-matter-most)
    - [The claim must be about repeated use, not one elegant example](#the-claim-must-be-about-repeated-use-not-one-elegant-example)
    - [The escape routes must be structurally specific](#the-escape-routes-must-be-structurally-specific)
    - [The no-gos must remain genuinely load-bearing](#the-no-gos-must-remain-genuinely-load-bearing)
    - [The cross-family unification must not collapse into metaphor](#the-cross-family-unification-must-not-collapse-into-metaphor)
    - [The framework should not overclaim generality](#the-framework-should-not-overclaim-generality)
  - [Largest implications if the claim holds](#largest-implications-if-the-claim-holds)
  - [Bottom line](#bottom-line)
  - [Potential field impact if the claim holds](#potential-field-impact-if-the-claim-holds)
  - [Venue strategy](#venue-strategy)
    - [Best-fit venues by framing](#best-fit-venues-by-framing)
    - [Recommended path](#recommended-path)
    - [Practical ranking for this project](#practical-ranking-for-this-project)
  - [References](#references)

# Scope honesty via no gos novelty memo

## Overall judgment

The literature already contains a strong lineage for one major part of AAT’s claim: impossibility results can be used constructively, not just negatively. The clearest and most mature example is the causal identifiability and transportability program. In that literature, one first specifies an information regime, then proves what cannot be identified from it, and then uses the same graphical machinery to characterize the extra observations, interventions, or cross-domain data needed to escape the impossibility \[Pea95d, Shp08, Bar12b, Bar12c, Bar13b, Bar14b, Lee19b, Lee20h, Pea12b, Shp14\]. Information-constrained control provides a second relevant lineage: below certain rate or capacity thresholds stabilization is impossible, while richer feedback structure is the named escape \[Tat04b, Nai04, Sah06\].

What does not appear to be already present in the project literature is the full AAT package suggested by the relevant chapters:

- no-go theorems used repeatedly as a framework-level scope-honesty device rather than as isolated technical facts
- a recurring regime pattern of the form “task impossible from information regime R, but recoverable via structural escape Y” across multiple non-equivalent theorem families
- Pearl-style intervention access as one recurring escape valve inside a larger cross-instance methodological posture
- a unified claim that these impossibility results make AAT’s own machinery look load-bearing rather than ornamental

That package looks more novel than it may first appear. The individual impossibility results are not new. The likely novelty is the meta-methodological posture: AAT seems to be treating impossibility theorems as a disciplined way to mark scope boundaries and then to justify why its structural commitments matter.

This is not the cleanest “new theorem” memo in the project. It is closer to a framework-methodology contribution. But within that category, it looks unusually defensible because the causal literature gives a very strong exact precedent for one part of the posture, while the broader multi-instance unification still seems missing.

## Claim under review

In the project files, the claim is not merely that AAT cites no-go theorems when convenient.

The stronger claim is that AAT repeatedly uses external impossibility results to do three things at once:

- show that a task is not recoverable from the currently available information
- make the framework’s scope limits explicit and honest
- identify a named structural escape route that restores identifiability or tractability under a richer regime

The motivating examples span distinct technical settings. In one case, observational structure is insufficient and interventional access through the action loop is the escape. In another, component marginals do not certify composite contraction and richer observer or intervention structure is needed. In another, a universal information-to-distance constant fails under coordinate choice and parameterization-invariant structure becomes the escape. The project’s claim is therefore about a recurring explanatory pattern, not one theorem family.

Read this way, the project is making a stronger methodological claim than “negative results are useful.” It is saying that impossibility theorems can function as a systematic scope-honesty apparatus inside a positive theory of agency.

## Prior art by claim component

| AAT component | Nearest prior art | Match | Novelty read |
|:---|:---|---:|:---|
| Impossibility results used constructively rather than as inquiry-stoppers | \[Pea95d\], \[Shp08\], \[Pea12b\], \[Bar12b\], \[Bar12c\], \[Bar13b\], \[Shp14\] | Strong | Low novelty by itself |
| Explicit regime shift from observational insufficiency to interventional escape | \[Pea95d\], \[Shp08\], \[Bar12b\], \[Shp14\] | Strong | Low novelty by itself |
| Same calculus used across identification, transportability, and data fusion | \[Pea12b\], \[Bar13b\], \[Lee20h\] | Strong | Low novelty by itself |
| No-go plus escape posture generalized across multiple non-causal theorem families | distributed ancestry only, including \[Tat04b\], \[Nai04\], \[Sah06\] | Partial | Moderate to high novelty |
| Framework-level pattern where impossibility clarifies what AAT machinery is load-bearing | indirect ancestry only | Weak | High potential novelty |
| Cross-instance unification of causal, estimation, contraction, and invariance no-gos | not found as an existing package | Weak | Highest novelty candidate |

## What the prior art already establishes

The strongest exact lineage is the Pearl-Shpitser-Bareinboim program. \[Pea95d\] is especially important because it already states the posture in unusually explicit terms. Causal diagrams are not treated as passive summaries of assumptions. They are treated as active devices for determining whether available assumptions suffice, and if they do not, for suggesting what extra observations or auxiliary experiments would make the inference possible. That is extraordinarily close to AAT’s intended methodological tone.

\[Shp08\] strengthens this by giving complete identification methods across the causal hierarchy. The broad point is not merely that some effects are identifiable and others are not. It is that the hierarchy itself marks what lower information regimes cannot recover, and the formalism says when one must move to richer intervention classes. \[Shp14\] pushes the same general posture further by treating node, edge, and path interventions as a structured hierarchy, with different identification power attached to each level.

The Bareinboim line then generalizes the exact same logic across new regimes. \[Bar12b\] asks when ordinary observation is insufficient but surrogate experiments on another variable can identify the target effect. \[Bar12c\] and \[Bar13b\] do the same for transportability across environments, using selection diagrams to characterize exactly when source-domain experiments and target-domain observations do or do not suffice. The key methodological point is that failure is not left as a vague warning. It is upgraded into theorem-backed non-identifiability, and the framework names the escape route precisely. \[Pea12b\] is especially valuable as a unifier because it places identification, transportability, and meta-synthesis inside one do-calculus-based program.

That literature already establishes one exact pattern very strongly:

- specify the information regime
- characterize what is impossible under that regime
- identify the richer structural regime that escapes the impossibility
- use the same formalism for both the no-go and the escape

Information-constrained control gives a distributed but relevant analogue. \[Tat04b\], \[Nai04\], and \[Sah06\] show that stabilization is impossible below rate or reliability thresholds fixed by plant dynamics, while richer communication structure is the named escape. This is not as close to AAT’s methodological self-description as the causal literature is, but it supports the broader idea that impossibility can be used constructively to make a framework’s structural demands look principled rather than ad hoc.

What the prior art does not seem to provide is a cross-family meta-framework that repeatedly does this across causal identification, estimation floors, contraction certification, and parameterization invariance inside one general theory of agency.

## Where AAT seems genuinely new

AAT looks strongest where it abstracts the causal program’s methodological posture and reuses it across different theorem families.

A useful way to phrase the comparison is this:

- the causal literature already has a mature “regime, impossibility, escape” pattern
- the information-constrained control literature has local analogues of the same pattern
- AAT’s candidate novelty is to elevate that pattern into a recurring design principle for a whole agency framework rather than for one technical subfield

That move is stronger than simply citing several negative results.

First, the project seems to treat no-go theorems as scope-honesty machinery rather than rhetorical support. That matters. Many papers cite impossibility results as caveats. AAT appears to use them as a recurrent structural device for saying what the framework can and cannot claim.

Second, the project’s claimed escape routes are internal to its architecture. In the causal case, interventional access through the loop is not just an external theorem import. It is something the framework already treats as structurally available for agents in scope. That gives the impossibility result a very specific role: it helps explain why the loop’s interventional structure is load-bearing.

Third, the project is unusual in trying to align several different impossibility types under one posture. The motivating cases differ a lot: non-identifiability from observational data, inability to decompose from component marginals, failure of universal Euclidean information-to-distance constants, and so on. If AAT can really show that all of these are instances of one “honest scope boundary plus named structural escape” discipline, that looks materially new.

Fourth, the novelty is not only philosophical. It has technical bite if the framework consistently distinguishes:

- what follows under the current information regime
- what does not follow under the current regime
- what extra structure would be sufficient

That is a concrete methodological virtue, not just a style preference.

## Stress tests that matter most

### The claim must be about repeated use, not one elegant example

The causal literature already gives AAT a strong exact precedent. So the novelty cannot be that one impossibility theorem is used constructively. The novelty has to be that AAT makes this a recurring framework-level pattern across multiple instances.

### The escape routes must be structurally specific

If the memo only says “add more information,” the claim becomes trivial. The strength of the causal lineage is that the escape routes are named and regime-specific: interventions, surrogate experiments, transport formulas, heterogeneous-domain fusion \[Bar12b, Bar13b\]. AAT needs that same specificity.

### The no-gos must remain genuinely load-bearing

A danger here is that the no-go theorems become decorative. The memo is strongest if removing them would materially weaken AAT’s justification for why certain architectural commitments are necessary. In the best version, the impossibility result is what turns an architectural preference into a necessity claim under stated scope conditions.

### The cross-family unification must not collapse into metaphor

This is the main pressure point. It is easy to say that several negative results all “feel similar.” The stronger claim is that they play the same methodological role: each marks the exact boundary of a regime and names the kind of structural enrichment needed to cross it.

### The framework should not overclaim generality

The most defensible version is not “all good theories use no-gos this way.” It is narrower: AAT exhibits a recurring and unusually disciplined use of impossibility results as scope-honesty apparatus. That is enough.

## Largest implications if the claim holds

| Area | Why the claim matters | Closest literature it would move beyond |
|:---|:---|:---|
| AI theory methodology | It would offer a disciplined way to use impossibility results to mark scope and justify structure | \[Pea95d\], \[Pea12b\] |
| Agent architecture | It would clarify which parts of the framework are necessary responses to identifiable information limits | causal and information-constrained-control lineages |
| Scientific communication | It would model a way for theory papers to be ambitious without pretending universal scope | distributed negative-results literature |
| Cross-field synthesis | It would show that causal, control, and invariance no-gos can play parallel roles inside one theory | no direct single precursor found |

The biggest direct effect would likely be on how AAT presents itself. This memo suggests that one of the framework’s real strengths is not only what it proves, but how honestly it marks where proof cannot go without extra structure. That kind of discipline is rare and valuable.

The second effect would be on methodological taste. AAT would be saying that impossibility results are not merely obstacles. They are also tools for deciding what machinery must be built into a serious theory.

The third effect would be on external reception. Reviewers are often skeptical of broad frameworks because they blur what is proved, what is hoped, and what is out of scope. If AAT really uses no-go theorems to keep those categories separate, that could make the whole project look more trustworthy.

## Bottom line

The weak version of this memo is not novel. The field already knows, especially from the causal-identification literature, that impossibility results can be used constructively to diagnose insufficient assumptions and to suggest richer experimental or observational regimes \[Pea95d, Shp08, Bar12b, Bar13b, Pea12b\].

The strong version does look novel. AAT’s most promising claim is not that impossibility results are useful, but the stronger framework-level thesis that external no-go theorems can serve as a recurring scope-honesty apparatus across multiple theorem families: each identifies what the current regime cannot support, and each helps show why AAT’s own structural machinery is necessary rather than optional.

The cleanest sharpened read is:

- the causal version of the posture has strong prior art
- the broader constructive use of impossibility has partial prior art
- the cross-family meta-methodological unification still looks novel

A strong one-line framing is this:

AAT’s novelty is not the observation that some inferences are impossible, but the stronger claim that impossibility results can be used as a recurring scope-honesty apparatus that reveals which pieces of an agency framework are structurally load-bearing.

## Potential field impact if the claim holds

The impact ceiling is moderate but real. This is not the sort of memo that wins by a single flashy theorem. It wins by improving how a broad theory is built and defended.

At the modest end, the paper would matter as a methodological synthesis. It would connect the causal-identification tradition, information-constrained control, and related negative-result literatures under one constructive stance toward impossibility.

At the stronger end, it could improve how ambitious AI theory papers are written. Instead of hiding scope limits or papering them over with intuition, it would make those limits explicit and then show what extra structure buys a principled escape.

The biggest direct effect would likely be internal to AAT. This posture helps the whole framework look more mature because it tells the reader not just what the theory says, but why it refuses to say more in the wrong regimes.

A practical impact ranking would be:

- moderate impact if the paper is received as a strong methodological synthesis
- high impact if the scope-honesty posture is seen as a distinctive and reusable way to build broad theories
- very high impact if later framework papers begin explicitly organizing their claims around “regime, impossibility, structural escape” patterns

## Venue strategy

### Best-fit venues by framing

The right venue depends on whether the paper is framed as causal-methodology transfer, general AI theory, or philosophy-of-method in technical form.

If the paper is framed as a broad AI theory and methodology contribution about how agency theories should mark scope and justify structure, Artificial Intelligence journal is likely the strongest single home. It is broad enough to host work that is partly technical and partly architectural in its contribution.

If the paper is framed as a general-intelligence theory contribution, AGI is also a good fit. This is especially true if the paper is presented as a meta-level discipline for building broad theories of agency rather than as a narrow causal-inference result.

If the causal-identification side becomes dominant and the paper is rewritten around the transfer of identifiability-style methodology into agent theory, UAI is the most natural specialist audience, though only if the argument remains technically tight enough to be legible as more than framework commentary.

TMLR is possible but less natural than for some other memos. The fit is best only if the paper leans heavily into analytical framework design for learning systems rather than into philosophy-of-theory concerns.

### Recommended path

The cleanest publication strategy is:

1.  Write the full framework-facing version for Artificial Intelligence journal.
2.  If the broader agency-theory positioning is central, prepare a shorter companion version for AGI.
3.  If the causal-methodology transfer becomes the sharpest core, consider a more technically focused version for UAI.

### Practical ranking for this project

My venue ranking for this exact project is:

- Artificial Intelligence journal
- AGI Conference
- UAI
- TMLR

The fork is simple:

- if the main claim is “this is a methodological principle for broad agency theories,” favor Artificial Intelligence journal or AGI
- if the main claim is “this imports and generalizes identifiability-style scope discipline,” consider UAI
- if the main claim is “this is an analytical framework for learning-system scope discipline,” consider TMLR

---

## References

\[Pea95d\] J. Pearl, “Causal diagrams for empirical research,” Dec. 01, 1995. doi: [10.1093/BIOMET/82.4.669](https://doi.org/10.1093/BIOMET/82.4.669).

\[Shp08\] I. Shpitser and J. Pearl, “Complete Identification Methods for the Causal Hierarchy,” *J. Mach. Learn. Res.*, vol. 9, pp. 1941–1979, Jun. 2008, doi: [10.5555/1390681.1442797](https://doi.org/10.5555/1390681.1442797).

\[Bar12b\] E. Bareinboim and J. Pearl, “Causal Inference by Surrogate Experiments: z-Identifiability,” *Conference on Uncertainty in Artificial Intelligence*, pp. 113–120, Aug. 2012.

\[Bar12c\] E. Bareinboim and J. Pearl, “Transportability of Causal Effects: Completeness Results,” *AAAI Conference on Artificial Intelligence*, pp. 698–704, Jul. 2012, doi: [10.1609/aaai.v26i1.8232](https://doi.org/10.1609/aaai.v26i1.8232).

\[Bar13b\] E. Bareinboim and J. Pearl, “A General Algorithm for Deciding Transportability of Experimental Results,” *arXiv.org*, vol. 1, pp. 107–134, May 2013, doi: [10.1515/jci-2012-0004](https://doi.org/10.1515/jci-2012-0004).

\[Bar14b\] E. Bareinboim and J. Pearl, “Transportability from Multiple Environments with Limited Experiments: Completeness Results,” *Neural Information Processing Systems*, pp. 280–288, Dec. 2014.

\[Lee19b\] S. Lee, J. D. Correa, and E. Bareinboim, “General Identifiability with Arbitrary Surrogate Experiments,” *Conference on Uncertainty in Artificial Intelligence*, pp. 389–398, 2019.

\[Lee20h\] S. Lee, J. D. Correa, and E. Bareinboim, “General Transportability - Synthesizing Observations and Experiments from Heterogeneous Domains,” *AAAI Conference on Artificial Intelligence*, pp. 10210–10217, Apr. 2020, doi: [10.1609/aaai.v34i06.6582](https://doi.org/10.1609/aaai.v34i06.6582).

\[Pea12b\] J. Pearl, “The Do-Calculus Revisited,” *Conference on Uncertainty in Artificial Intelligence*, pp. 3–11, Aug. 2012.

\[Shp14\] I. Shpitser and E. Tchetgen, “CAUSAL INFERENCE WITH A GRAPHICAL HIERARCHY OF INTERVENTIONS.” *Annals of statistics*, vol. 44 6, pp. 2433–2466, Nov. 2014, doi: [10.1214/15-AOS1411](https://doi.org/10.1214/15-AOS1411).

\[Tat04b\] S. Tatikonda and S. Mitter, “Control under communication constraints,” *IEEE Transactions on Automatic Control*, vol. 49, pp. 1056–1068, Jul. 2004, doi: [10.1109/TAC.2004.831187](https://doi.org/10.1109/TAC.2004.831187).

\[Nai04\] G. Nair and R. Evans, “Stabilizability of Stochastic Linear Systems with Finite Feedback Data Rates,” *SIAM J. Control. Optim.*, vol. 43, pp. 413–436, Feb. 2004, doi: [10.1137/S0363012902402116](https://doi.org/10.1137/S0363012902402116).

\[Sah06\] A. Sahai and S. Mitter, “The Necessity and Sufficiency of Anytime Capacity for Stabilization of a Linear System Over a Noisy Communication Link&#8212;Part I: Scalar Systems,” *IEEE Transactions on Information Theory*, vol. 52, pp. 3369–3395, Jan. 2006, doi: [10.1109/TIT.2006.878169](https://doi.org/10.1109/TIT.2006.878169).
