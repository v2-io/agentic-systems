# Composite agency and Brooks's Law novelty memo

##### [**Undermind**](https://undermind.ai)

---


## Table of Contents

- [Composite agency and Brooks’s Law novelty memo](#composite-agency-and-brookss-law-novelty-memo)
  - [Overall judgment](#overall-judgment)
  - [Claim under review](#claim-under-review)
  - [Prior art by claim component](#prior-art-by-claim-component)
  - [What the prior art already establishes](#what-the-prior-art-already-establishes)
  - [Where AAT seems genuinely new](#where-aat-seems-genuinely-new)
  - [Stress tests that matter most](#stress-tests-that-matter-most)
    - [Closure defect must be more than renamed abstraction error](#closure-defect-must-be-more-than-renamed-abstraction-error)
    - [The Brooks’s-Law claim must beat generic bottleneck rhetoric](#the-brookss-law-claim-must-beat-generic-bottleneck-rhetoric)
    - [The bridge from abstraction residue to tempo tax is the technical hinge](#the-bridge-from-abstraction-residue-to-tempo-tax-is-the-technical-hinge)
    - [The unity machinery must earn its dimensional richness](#the-unity-machinery-must-earn-its-dimensional-richness)
    - [Symbiogenesis should be framed modestly](#symbiogenesis-should-be-framed-modestly)
  - [Largest implications if the claim holds](#largest-implications-if-the-claim-holds)
  - [Bottom line](#bottom-line)
  - [Potential field impact if the claim holds](#potential-field-impact-if-the-claim-holds)
  - [Venue strategy](#venue-strategy)
    - [Best-fit venues by framing](#best-fit-venues-by-framing)
    - [Recommended path](#recommended-path)
    - [Practical ranking for this project](#practical-ranking-for-this-project)
  - [References](#references)

# Composite agency and Brooks’s Law novelty memo

## Overall judgment

The literature already contains strong mathematical antecedents for several pieces of AAT’s composite-agency story. Markov lumpability and commutative coarse-graining ask almost exactly when microdynamics can be replaced by autonomous macrodynamics \[Buc94, Tia06b\]. Control abstraction and refinement work gives explicit conditions under which an abstract system preserves reachability or control properties of a concrete one, often with quantitative error bounds when exact commutation fails \[Pap02, Rei15, Run15\]. State-abstraction work in RL similarly asks when aggregated states remain sufficient for prediction and control \[Li06\]. On the coordination side, the field already knows that communication and collaboration can impose real throughput and coherence penalties: limited information rate constrains stabilization \[Won99, Nai04, Tat04b, Tan15b\], collaboration architectures can generate unavoidable bottleneck idleness \[Gur15b\], and large locally coupled networks can lose global coherence as they scale \[Bam11\]. Major-transitions work then provides substantial ancestry for asymmetric integration and loss of lower-level autonomy \[Sza15\].

What does not appear to be already present in the project literature is the full AAT package suggested by AAT-chapter-10, AAT-chapter-11, and AAT-chapter-12:

- a single composite-agent criterion based on closure of macro-dynamics under coarse-graining, measured by a closure defect
- a bridge from that closure defect to a persistence-style macro error bound and a tempo penalty
- a Brooks’s-Law derivation in which adding agents hurts exactly when coordination overhead outruns the marginal adaptive benefit
- a unified frame connecting exact composition, approximate composition, and asymmetric symbiogenic absorption

That package looks genuinely promising, though less cleanly novel than directed separation or self-actuators grounding. The field clearly already has the abstraction side and clearly already has the bottleneck side. The likely novelty is the stronger cybernetic claim that these are one story: valid macro-agency is approximate commutation, and the cost of approximation appears as tempo lost to coordination.

The weakest flank is symbiogenesis. There is real prior art on major transitions and autonomy loss \[Sza15\], so that part looks more like integration into the broader package than a standalone novelty center.

## Claim under review

In the project files, composite agency is not just “a team can sometimes be treated as one thing.”

AAT-chapter-11 defines a valid composite by a closure criterion: projecting micro-state to macro-state and then evolving the macro-system should approximately commute with evolving the micro-system and then projecting. The irreducible failure of that commutation is the closure defect $`\varepsilon^\ast`$. The same chapter then turns closure defect into a macro-level disturbance term and derives a bridge lemma: macro-tracking error is bounded by a function of closure defect, macro update rate, and macro correction strength.

The same chapter also defines composite tempo as sub-additive. The macro-agent’s realized adaptive tempo is bounded above by the sum of sub-agent tempos, with the gap interpreted as coordination overhead. Read together with the persistence machinery, that yields the Brooks’s-Law-shaped claim: adding more sub-agents only helps if the adaptive gain from extra capacity exceeds the tempo and disturbance cost induced by coordination.

AAT-chapter-10 broadens the scope story by distinguishing multi-agent systems from true composites, and it introduces symbiogenic composition as an asymmetric route by which one unit is absorbed into another. AAT-chapter-12 adds the unity dimensions and communication side, giving the project a way to relate shared state, shared objectives, and update-rule homogeneity to compressibility and closure defect.

Read together, the project is making a stronger claim than “abstractions can be useful” or “coordination has costs.” It is saying that macro-agency is valid exactly to the extent that closed-loop coarse-graining approximately commutes, and that coordination cost is not just managerial folklore but a mathematically load-bearing tax on adaptive tempo.

## Prior art by claim component

| AAT component | Nearest prior art | Match | Novelty read |
|:---|:---|---:|:---|
| Valid macro-entity requires dynamically consistent coarse-graining | \[Buc94\], \[Tia06b\], \[Pap02\], \[Rei15\], \[Run15\] | Strong | Low novelty by itself |
| Approximate abstraction with quantitative error when commutation fails | \[Run15\], \[Rei15\] and adjacent abstraction literature | Strong | Low novelty by itself |
| State aggregation as sufficient representation for control or prediction | \[Li06\] and related abstraction work | Strong | Low novelty by itself |
| Coordination and communication impose responsiveness bottlenecks | \[Won99\], \[Nai04\], \[Tat04b\], \[Tan15b\] | Strong | Low novelty by itself |
| Collaboration can create explicit idleness or bottleneck tax | \[Gur15b\] | Strong | Moderate novelty only if AAT derives a sharper closed-loop threshold |
| Large collectives lose coherence under local control as scale rises | \[Bam11\] | Strong | Low to moderate novelty by itself |
| Closure defect plus tempo tax yields Brooks’s-Law threshold | indirect ancestry only | Weak to partial | High potential novelty |
| Symbiogenesis as asymmetric autonomy loss into higher-level unit | \[Sza15\] and major-transition lineage | Moderate | Moderate novelty mainly through integration |
| Unity dimensions as rate-distortion parameters for composite fidelity | partial ancestry in abstraction and information-constrained control \[Li06, Tan15b\] | Partial | Moderate to high novelty |

## What the prior art already establishes

The closest ancestry for AAT’s core closure idea comes from lumpability and abstraction. \[Buc94\] and \[Tia06b\] study when a Markov process can be aggregated so that the coarse-grained process evolves autonomously. That is very close in spirit to AAT’s idea that a macro-entity is valid when microdynamics commute with coarse-graining. \[Pap02\] gives a control-side version by constructing abstractions of affine control systems that preserve accessibility and reachability structure under smooth surjective maps. \[Rei15\] sharpens the same general theme with feedback refinement relations: an abstract controller can be soundly transferred to the concrete plant when the abstraction relation preserves admissible behavior. \[Run15\] is especially close to AAT’s approximate case because it proves compositional abstraction theorems for interconnected control systems and supplies explicit output-error bounds when the abstraction is only approximate.

Those papers already establish the most basic structural point: a macro-description is not justified because it is convenient. It is justified when relevant dynamics or control properties survive coarse-graining.

The RL and planning abstraction literature supplies a nearby but weaker analogue. \[Li06\] surveys and unifies state-abstraction schemes for MDPs, asking when aggregate states are sufficient for planning and learning. This is useful prior art for the idea that grouped units can sometimes be treated as one decision state. But it is not quite AAT’s claim, because the target is computational sufficiency inside an MDP, not a broader closed-loop criterion for when a set of agents forms one macro-agent.

The tempo and coordination-cost side also has strong precedents. \[Won99\], \[Nai04\], and \[Tat04b\] show that stabilization under finite feedback bandwidth requires hard information-rate thresholds. \[Tan15b\] is particularly relevant because it proves that an information-constrained LQG problem admits an optimal staged architecture and explicitly prices control in directed information. These papers support the broad AAT stance that communication and modular organization can carry a real responsiveness cost.

\[Gur15b\] is the strongest nearby result for the Brooks’s-Law side. It formalizes unavoidable bottleneck idleness in collaborative networks and shows that collaboration architectures can force capacity below what naive bottleneck analysis predicts. Even at full network capacity, bottleneck resources may have to idle because synchronization requirements prevent simultaneous use. That is a genuine mathematical overhead term, not a metaphor.

\[Bam11\] gives the strongest nearby scaling-limit result. It studies large networked systems with local feedback and proves that low-dimensional collectives can lose global coherence as scale increases, even when local neighbor-to-neighbor regulation remains good. This matters because it shows that adding more locally controlled parts can degrade macro-level order for structural reasons, not merely because of bad implementation.

The symbiogenesis side has substantial external ancestry. \[Sza15\] treats major evolutionary transitions as cases where lower-level units become constrained by a higher-level unit, lose autonomy, and are progressively de-Darwinized. This is strong conceptual prior art for AAT’s asymmetric-composition story. It does not, however, formulate the transition in AAT’s closure-defect or macro-tempo language.

Taken together, the literature already establishes five things well:

- dynamically valid aggregation requires more than descriptive convenience
- approximate abstractions can carry explicit quantitative error bounds
- communication and modular staging can impose hard performance thresholds
- collaboration can create unavoidable synchronization overhead
- large collectives can lose macro-level coherence as they scale

What the literature does not already seem to establish is the exact AAT bundle in which these are one closed-loop account of macro-agency, closure defect, and coordination tax.

## Where AAT seems genuinely new

AAT looks strongest where it fuses the abstraction and coordination literatures into one macro-agency theorem shape.

A useful way to phrase the comparison is this:

- the lumpability and abstraction papers ask when a coarse variable is dynamically valid
- the information and network papers ask when communication or synchronization constrains performance
- the major-transition papers ask when lower-level units are absorbed into a higher-level one
- AAT’s candidate novelty is to make these all aspects of one composition law for agents rather than three separate topics

That bundled move is stronger than any one ingredient by itself.

First, the project turns approximate commutation into an explicit agency criterion. The prior art shows that abstraction can preserve behavior or control properties \[Pap02, Rei15, Run15\], but AAT is trying to say something more ambitious: if macro-dynamics do not approximately commute with coarse-graining, then there is no valid composite agent there in the full AAT sense. That scope use of closure is stronger than ordinary model reduction.

Second, AAT’s bridge from closure defect to persistence-style macro bounds looks like a real novelty center. \[Run15\] and related work give approximation-error bounds, but AAT plugs the approximation residue directly into a disturbance term and then connects it to macro persistence and macro tempo. If that bridge is mathematically sound, it is materially closer to a general cybernetic composition principle than the source literatures usually provide.

Third, the Brooks’s-Law derivation is the clearest external hook. The field certainly already knows that coordination can waste capacity \[Gur15b\] and that large networks can lose coherence \[Bam11\]. What looks new is the stronger AAT claim that this can be stated as a thresholded inequality inside one persistence framework: adding sub-agents helps until the induced coordination overhead exceeds the adaptive benefit. That is sharper than generic warnings about communication overhead.

Fourth, the unity-dimensions machinery may be a real contribution if it truly parametrizes closure-defect rate-distortion rather than merely redescribing team alignment. \[Li06\] and \[Tan15b\] give partial ancestry for sufficiency and information cost, but the exact move from epistemic, teleological, strategic, perceptual, and update-rule unity to achievable macro compression appears distinctive.

Fifth, symbiogenesis is novel mainly in how it is attached to the rest of the package. \[Sza15\] already gives strong precedence for asymmetric integration and autonomy loss. AAT’s opportunity is narrower: to show that symmetric composition, approximate composition, and asymmetric absorption are all special cases of one composition framework.

## Stress tests that matter most

### Closure defect must be more than renamed abstraction error

This is the main pressure point. The abstraction literature already has simulation functions, feedback refinement relations, lumpability error, and related notions \[Pap02, Rei15, Run15\]. AAT only gets a strong novelty claim if closure defect does something these quantities do not already do — especially by governing whether a set of agents counts as one macro-agent, not merely whether one model approximates another.

### The Brooks’s-Law claim must beat generic bottleneck rhetoric

\[Gur15b\] already proves unavoidable bottleneck idleness, and \[Bam11\] already proves collective coherence losses with scale. AAT’s stronger claim is not merely that coordination has costs, but that a single persistence-style inequality derives when added agents stop helping and start hurting. That sharper threshold is what needs to survive scrutiny.

### The bridge from abstraction residue to tempo tax is the technical hinge

If closure defect stays as a descriptive approximation error, the memo becomes mostly synthesis. If AAT really turns $`\varepsilon^\ast`$ into a disturbance-rate term and then into a lower bound on coordination overhead, that is where the package becomes much more distinctive.

### The unity machinery must earn its dimensional richness

A five-part unity profile is only worthwhile if it changes achievable compression or macro fidelity in analytically distinct ways. If the dimensions mostly collapse in practice to one vague alignment score, the framework risks looking overparameterized.

### Symbiogenesis should be framed modestly

This is the weakest novelty flank. The major-transitions literature already studies absorption of lower-level units into higher-level ones \[Sza15\]. AAT should not claim to have discovered asymmetric integration. The more defensible claim is that it places asymmetric integration inside the same composition framework as ordinary team formation and approximate macro-agency.

## Largest implications if the claim holds

| Area | Why the claim matters | Closest literature it would move beyond |
|:---|:---|:---|
| Multi-agent systems and organizational design | It would give a principled test for when a group is one macro-agent rather than just many interacting agents | \[Pap02\], \[Run15\], \[Gur15b\] |
| AI architecture | It would connect abstraction validity directly to coordination cost and macro responsiveness | \[Rei15\], \[Tan15b\] |
| Collective control and robotics | It would explain why adding agents can hurt through a formal macro-level tax rather than only through engineering folklore | \[Bam11\], \[Gur15b\] |
| General agency theory | It would unify composition, approximate composition, and asymmetric absorption in one framework | \[Buc94\], \[Sza15\] |

The biggest direct effect would likely be on how people talk about collectives and compound systems. AAT suggests that the right question is not only whether the parts cooperate, but whether the closed-loop aggregate has its own dynamically valid macrostate. That is a cleaner standard for talking about teams, organizations, swarms, and multi-module AI systems.

The second major effect would be on scaling arguments. A great deal of practice assumes that adding more capable subunits should help unless incentives are misaligned. This memo suggests a more structural limit: even aligned additions can hurt if they raise closure defect or coordination overhead faster than they raise correction capacity.

The third effect would be on AI systems engineering. The closure-defect lens gives a principled way to ask when an orchestrated multi-module system can be treated as one coherent agent and when the interface-level unity is too lossy for that description to be valid.

## Bottom line

The weak version of this memo is not novel. The field already knows that valid abstraction requires commutative or approximately preserved dynamics, that communication and collaboration impose overhead, and that large collectives can lose coherence \[Buc94, Pap02, Run15, Gur15b, Bam11\].

The strong version does look novel. AAT’s most promising claim is not that teams can be abstracted or that coordination is costly, but the stronger architectural thesis that macro-agency is valid exactly to the extent that closed-loop coarse-graining approximately commutes, and that the resulting closure defect enters as a tempo-reducing disturbance term that can derive a Brooks’s-Law threshold.

The cleanest sharpened read is:

- the dynamic-validity part has strong prior art
- the coordination-overhead part has strong prior art
- the asymmetry and major-transition part has moderate prior art
- the exact closure-defect plus tempo-tax plus Brooks’s-Law package still looks novel

A strong one-line framing is this:

AAT’s novelty is not the observation that groups can sometimes be treated as wholes and that coordination has costs, but the stronger claim that composite agency is a closed-loop commutation property whose failure appears as a measurable tempo tax.

## Potential field impact if the claim holds

The impact ceiling is substantial because this topic could provide a common language for several fields that usually stay apart.

At the modest end, the paper would still matter as a synthesis. It would connect lumpability, abstraction, feedback refinement, information-constrained control, collaboration bottlenecks, and major transitions under one question about when a collective is a real macro-agent.

At the stronger end, the paper could become a canonical way of talking about composition. Instead of treating abstraction validity and coordination overhead as separate engineering concerns, it would say they are two sides of one macro-agency problem.

The biggest direct effect would likely be on teams, organizations, and compound AI systems. The paper offers a disciplined way to ask when aggregation is legitimate and when apparent unity hides too much internal mismatch to support a single-agent description.

The second major effect would be on scaling debates. If the Brooks’s-Law derivation lands, it gives a principled reason why adding more agents, modules, or workers can push a system past a responsiveness threshold even without adversarial conflict or misaligned incentives.

The third effect would be on theory-building inside AAT itself. This topic helps the framework look like more than a collection of local results, because it says how multiple agents can become one agent without handwaving.

A practical impact ranking would be:

- moderate impact if the paper is received as a strong synthesis of abstraction and coordination literatures
- high impact if the closure-defect to tempo-tax bridge is seen as technically new and useful
- very high impact if the Brooks’s-Law derivation becomes a standard way to reason about when added parts stop helping a collective

## Venue strategy

### Best-fit venues by framing

The right venue depends on how much the paper leans toward AI architecture, control theory, or general agency theory.

If the paper is framed as a broad AI theory contribution about composition, abstraction, and macro-agency, [Artificial Intelligence journal](https://www.sciencedirect.com/journal/artificial-intelligence) is likely the strongest single home. Its scope is broad enough to fit multi-agent systems, planning and action, reasoning under uncertainty, and general architectural theory.

If the paper is sharpened into a more control-theoretic result about abstraction validity, interconnection error, and responsiveness limits, the [IEEE Conference on Decision and Control](https://cdc2025.ieeecss.org/authors/call-for-papers) is a strong conference audience. The abstraction, interconnection, and network-coherence literatures already live there.

If the paper is framed as a broad theory of agency and collective intelligence, the [AGI Conference](https://agi-conference.org/call-for-papers) is also a good fit. It is especially suitable if the argument is presented as a general account of when many agents become one rather than primarily as a control abstraction paper.

If the strongest contribution becomes the analytical mapping from unity or compression to macro fidelity, [TMLR](https://www.jmlr.org/tmlr/) is plausible, though less natural than for some of the other memos. The fit is best if the paper leans into abstraction, representation, and information-theoretic learning arguments.

### Recommended path

The cleanest publication strategy is:

1.  Write the full theory version for Artificial Intelligence journal.
2.  If the abstraction and threshold theorem is the sharpest core, prepare a tighter technical cut for CDC.
3.  If the broader collective-agency framing is central, develop a companion or alternate version for AGI.
4.  If the rate-distortion and abstraction side becomes dominant, consider a more compressed TMLR version.

### Practical ranking for this project

My venue ranking for this exact project is:

- Artificial Intelligence journal
- IEEE Conference on Decision and Control
- AGI Conference
- TMLR

The fork is simple:

- if the main claim is “this is a general theory of when collectives become macro-agents,” favor Artificial Intelligence journal or AGI
- if the main claim is “this is a control-theoretic abstraction and threshold result,” favor CDC
- if the main claim is “this is an analytical abstraction or information-theoretic learning result,” favor TMLR

---

## References

\[Buc94\] P. Buchholz, “Exact and ordinary lumpability in finite Markov chains,” Mar. 01, 1994. doi: [10.2307/3215235](https://doi.org/10.2307/3215235).

\[Tia06b\] J. Tian and D. Kannan, “Lumpability and Commutativity of Markov Processes,” Jul. 01, 2006. doi: [10.1080/07362990600632045](https://doi.org/10.1080/07362990600632045).

\[Pap02\] G. Pappas and S. Simic, “Consistent abstractions of affine control systems,” *IEEE Trans. Autom. Control.*, vol. 47, pp. 745–756, Aug. 2002, doi: [10.1109/TAC.2002.1000269](https://doi.org/10.1109/TAC.2002.1000269).

\[Rei15\] G. Reissig, A. Weber, and M. Rungger, “Feedback Refinement Relations for the Synthesis of Symbolic Controllers,” *IEEE Transactions on Automatic Control*, vol. 62, pp. 1781–1796, Mar. 2015, doi: [10.1109/TAC.2016.2593947](https://doi.org/10.1109/TAC.2016.2593947).

\[Run15\] M. Rungger and M. Zamani, “Compositional Construction of Approximate Abstractions of Interconnected Control Systems,” *IEEE Transactions on Control of Network Systems*, vol. 5, pp. 116–127, Apr. 2015, doi: [10.1145/2728606.2728615](https://doi.org/10.1145/2728606.2728615).

\[Li06\] L. Li, T. J. Walsh, and M. Littman, “Towards a Unified Theory of State Abstraction for MDPs,” *AI&M*, 2006.

\[Won99\] W. Wong and R. Brockett, “Systems with finite communication bandwidth constraints. II. Stabilization with limited information feedback,” *IEEE Trans. Autom. Control.*, vol. 44, pp. 1049–1053, May 1999, doi: [10.1109/9.763226](https://doi.org/10.1109/9.763226).

\[Nai04\] G. Nair and R. Evans, “Stabilizability of Stochastic Linear Systems with Finite Feedback Data Rates,” *SIAM J. Control. Optim.*, vol. 43, pp. 413–436, Feb. 2004, doi: [10.1137/S0363012902402116](https://doi.org/10.1137/S0363012902402116).

\[Tat04b\] S. Tatikonda and S. Mitter, “Control under communication constraints,” *IEEE Transactions on Automatic Control*, vol. 49, pp. 1056–1068, Jul. 2004, doi: [10.1109/TAC.2004.831187](https://doi.org/10.1109/TAC.2004.831187).

\[Tan15b\] T. Tanaka, P. M. Esfahani, and S. Mitter, “LQG Control With Minimum Directed Information: Semidefinite Programming Approach,” *IEEE Transactions on Automatic Control*, vol. 63, pp. 37–52, Oct. 2015, doi: [10.1109/TAC.2017.2709618](https://doi.org/10.1109/TAC.2017.2709618).

\[Gur15b\] I. Gurvich and J. V. Mieghem, “Collaboration and Multitasking in Networks: Architectures, Bottlenecks, and Capacity,” *Manuf. Serv. Oper. Manag.*, vol. 17, pp. 16–33, 2015, doi: [10.1287/msom.2014.0498](https://doi.org/10.1287/msom.2014.0498).

\[Bam11\] B. Bamieh, M. Jovanović, P. Mitra, and S. Patterson, “Coherence in Large-Scale Networks: Dimension-Dependent Limitations of Local Feedback,” *IEEE Transactions on Automatic Control*, vol. 57, pp. 2235–2249, Dec. 2011, doi: [10.1109/TAC.2012.2202052](https://doi.org/10.1109/TAC.2012.2202052).

\[Sza15\] E. Szathmáry, “Toward major evolutionary transitions theory 2.0,” *Proceedings of the National Academy of Sciences*, vol. 112, pp. 10104–10111, Apr. 2015, doi: [10.1073/pnas.1421398112](https://doi.org/10.1073/pnas.1421398112).
