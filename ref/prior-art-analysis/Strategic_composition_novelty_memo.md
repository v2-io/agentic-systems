# Strategic composition novelty memo

##### [**Undermind**](https://undermind.ai)

---


## Table of Contents

- [Strategic composition novelty memo](#strategic-composition-novelty-memo)
  - [Overall judgment](#overall-judgment)
  - [Claim under review](#claim-under-review)
  - [Prior art by claim component](#prior-art-by-claim-component)
  - [What the prior art already establishes](#what-the-prior-art-already-establishes)
  - [Where AAT seems genuinely new](#where-aat-seems-genuinely-new)
  - [Stress tests that matter most](#stress-tests-that-matter-most)
    - [The inheritance claim is the key pressure point](#the-inheritance-claim-is-the-key-pressure-point)
    - [The positive-regime transfer should be framed modestly](#the-positive-regime-transfer-should-be-framed-modestly)
    - [The negative-regime story must not overclaim impossibility](#the-negative-regime-story-must-not-overclaim-impossibility)
    - [The phase-change language should be earned](#the-phase-change-language-should-be-earned)
    - [The fallback story should stay honest about equilibrium notions](#the-fallback-story-should-stay-honest-about-equilibrium-notions)
  - [Largest implications if the claim holds](#largest-implications-if-the-claim-holds)
  - [Bottom line](#bottom-line)
  - [References](#references)

# Strategic composition novelty memo

## Overall judgment

The literature already supplies most of the mathematical ingredients behind AAT’s strategic-composition story. Potential games, monotone games, variational inequalities, passivity, dissipativity, and no-regret convergence are all established literatures \[Arc20, Fox12b, Pav22, Gok23, Fac03, Har00, Gol20c\]. The field also already knows that conflict changes the dynamic picture: uncoupled player-wise dynamics do not generically converge to Nash \[Har03\], and harmonic or adversarial structure often yields recurrence or cycling rather than gradient-style convergence \[Can10c, Mer17b, Let19\].

What does not appear to be already present in the project literature is the full AAT package suggested by AAT-chapter-10 and AAT-chapter-14:

- individually separated sub-agents can compose into a strategically coupled composite under goal divergence
- the right macro-level primitive then shifts from contraction on a shared state to equilibrium existence, stability, and convergence
- persistence-style machinery transfers only on the potential and monotone sub-scope
- outside that sub-scope, the honest fallback is weaker set-level equilibrium structure rather than contraction-like guarantees

That package looks like the real novelty opportunity. Most of the ingredients are not new, but the bundled inheritance claim and the scope-honest handoff may well be.

## Claim under review

In the project files, strategic composition is not just “apply game theory when agents disagree.”

AAT-chapter-10 broadens composition scope to include strategic composites through route (C-iv): a set of agents can count as a composite not because they share an objective, but because their coupled interaction admits an equilibrium structure. That is already a meaningful reframing of what composition means.

AAT-chapter-14 then sharpens the argument. When objectives partially diverge, the right composition-level questions become equilibrium existence, stability, and convergence, not closure-defect contraction toward a shared target. Potential and monotone regimes inherit something like AAT’s persistence machinery at the equilibrium layer. Outside that sub-scope, only weaker distributional or set-convergence claims survive.

Read together, the project is making a stronger claim than “games have equilibria.” It is saying that goal divergence is a composition-level phase change: it breaks contraction-style macro inheritance and forces a different analytical regime.

## Prior art by claim component

| AAT component | Nearest prior art | Match | Novelty read |
|:---|:---|---:|:---|
| Equilibrium replaces shared-target contraction under conflicting objectives | broad game-theoretic background, especially \[Har03\], \[Can10c\], \[Let19\] | Moderate | Moderate novelty through framing and integration |
| Stability machinery transfers in favorable potential or monotone regimes | \[Arc20\], \[Fox12b\], \[Pav22\], \[Gok23\], \[Fac03\] | Strong | Low novelty by itself |
| Outside favorable structure, cycling or weaker convergence dominates | \[Mer17b\], \[Let19\], \[Har00\], \[Gol20c\] | Strong | Low novelty by itself |
| Individually separated agents compose into a strategically coupled composite under goal divergence | indirect ancestry only | Weak | High potential novelty |
| Scope-honest split between strong favorable-regime results and weaker fallback results | pieces exist separately across the literature | Partial | Moderate to high novelty in the package |

## What the prior art already establishes

The strongest favorable-regime ancestry comes from passivity, dissipativity, contraction, and variational-inequality analyses of games. \[Arc20\] gives a particularly close bridge: it decomposes a game dynamic into an evolutionary-dynamics model and a payoff-dynamics model, then proves global asymptotic stability of Nash-like equilibria under compatible dissipativity conditions. \[Fox12b\] and \[Pav22\] similarly connect passivity-style tools to convergence in stable or favorable games. \[Gok23\] makes the bridge even more explicit for distributed optimization and Nash seeking by proving contractivity conditions for pseudogradient and best-response dynamics in the right regimes. These papers provide excellent prior art for AAT’s positive transfer story on the potential and monotone sub-scope.

The decomposition literature provides the strongest ancestry for the “where the bridge fails” side. \[Can10c\] decomposes games into potential, harmonic, and nonstrategic parts. That matters here because it separates aligned gradient-like structure from cycling conflict structure. Potential components admit pure-equilibrium and optimization-like reasoning. Harmonic components generically do not. \[Let19\] gives a closely related decomposition in differentiable games: the symmetric Jacobian part behaves like a potential game, while the antisymmetric part generates Hamiltonian or rotational structure. This is extremely relevant to AAT because it shows, in a modern ML-friendly language, why conflict breaks ordinary optimization-style convergence.

\[Har03\] is one of the most useful negative baselines. It shows that uncoupled dynamics do not generically converge to Nash equilibrium, even with a unique equilibrium. That result is not the same as AAT’s composition claim, but it supports the broad message that local modularity or local player-wise updating is not enough to recover well-behaved global equilibrium structure under strategic interaction.

\[Mer17b\] gives the strongest nearby dynamic failure result. In zero-sum regularized learning, actual trajectories are Poincare recurrent rather than convergent. That is powerful evidence for AAT’s claim that outside favorable structure, last-iterate convergence is too much to promise. \[Har00\] then gives the canonical weaker fallback: regret matching leads the empirical distribution of play to correlated equilibrium. \[Gol20c\] is useful because it shows how restricted positive last-iterate results reappear in smooth monotone games, making the scope split especially clear: strong convergence is possible again, but only with stronger structure.

## Where AAT seems genuinely new

AAT looks strongest where it turns scattered facts into a composition-level inheritance story.

First, the project does not merely say that some games converge and others cycle. It says that composition itself changes type when objectives diverge. Individually separated agents can remain locally well-formed and still generate a composite whose correct macro description is strategic and equilibrium-based rather than contraction-based. That compositional inheritance claim is the most interesting novelty candidate in the whole package.

Second, AAT’s transition from contraction to equilibrium analysis is more architecturally explicit than the source literatures usually are. The control and game-theory papers mostly start from the strategic system already in hand. AAT starts from a broader agency architecture in which alignment-preserving composition and goal-divergent composition are siblings, and then identifies the point at which the former stops applying. That explicit handoff is conceptually valuable.

Third, the package is scope-honest in a way that many broad synthesis papers are not. The positive regime is not overextended. Potential and monotone structure permit transfer of persistence-style machinery. Outside that, only weaker equilibrium-set or distributional claims survive. That may sound modest, but this kind of disciplined honesty is a real contribution when the underlying literatures are often cited without careful regime boundaries.

Fourth, the route (C-iv) move in AAT-chapter-10 is stronger than it first appears. It broadens the meaning of composition from shared-purpose composites to strategic composites that are held together by equilibrium structure rather than common teleology. I do not see that exact scope move already stated in the project literature.

## Stress tests that matter most

### The inheritance claim is the key pressure point

Most of the raw mathematics already exists. The strongest novelty question is therefore not whether AAT has discovered potential games or monotone operators. It is whether prior work already states, in anything like this form, that individually separated or modular sub-agents become strategically coupled at the composite level under partial goal divergence. If not, AAT has a real opening.

### The positive-regime transfer should be framed modestly

The passivity, dissipativity, and contractivity literature is rich \[Arc20, Fox12b, Pav22, Gok23\]. AAT should not sound as if it invented the bridge from stability tools to favorable-equilibrium convergence. The novelty lies more in adaptation and packaging than in the raw mathematics.

### The negative-regime story must not overclaim impossibility

\[Mer17b\], \[Let19\], and \[Har00\] strongly support the idea that conflict often yields cycling or only set-level convergence. But AAT should keep the claim precise: not “equilibrium analysis fails,” but “last-iterate or contraction-style guarantees fail generically outside the favorable structure.” That is a stronger and more defensible statement.

### The phase-change language should be earned

“Goal divergence is a composition-level phase change” is a good line, but it needs support. The support has to be structural: the macro-state is no longer one shared target with closure-style contraction, but an equilibrium object whose dynamics are governed by the joint pseudogradient or best-response field. If that support is clear, the phrase works. If not, it risks sounding rhetorical.

### The fallback story should stay honest about equilibrium notions

One of the project’s strengths is that it distinguishes last-iterate convergence, average-play convergence, and equilibrium-set convergence. That distinction should remain sharp. \[Har00\] gives correlated-equilibrium convergence of empirical distributions; \[Gol20c\] gives restricted last-iterate results in monotone games. Those should not be blurred together.

## Largest implications if the claim holds

| Area | Why the claim matters | Closest literature it would move beyond |
|:---|:---|:---|
| Multi-agent AAT | It would identify a principled handoff from aligned composition to strategic composition | \[Arc20\], \[Gok23\], \[Can10c\] |
| Organizations and teams | It would explain why individually competent units can produce coupled macro-dynamics under partial goal divergence | broad team and game-theory background |
| Wrapped agent systems | It would give a cleaner account of when submodules stop composing like a single objective-seeking agent | \[Har03\], \[Let19\] |
| Safety and governance of agent collectives | It would justify weaker expectations outside favorable structure and stronger ones only where the game class supports them | \[Mer17b\], \[Har00\], \[Gol20c\] |

The largest direct effect would likely be on the larger AAT program itself. Strategic composition becomes the place where the theory explains why alignment-preserving machinery cannot simply be reused once goals partially diverge. That would make the overall architecture more convincing.

The second major effect would be on multi-agent system design. The memo suggests a more disciplined way to reason about partially aligned agent collectives: do not ask whether there is a Nash equilibrium in the abstract, ask whether the interaction falls into a favorable regime where stability-style guarantees survive, or only into a weaker regime where averages and supports are the best one can promise.

The third effect would be on safety and governance. AAT would support a more realistic view of agent collectives: partial alignment does not merely degrade performance smoothly, it can force a qualitative shift in the kind of guarantees available at the macro level.

## Bottom line

The weak version of this memo is not novel. The field already knows that potential and monotone games admit stronger convergence analysis, and that adversarial or harmonic structure often destroys last-iterate convergence \[Arc20, Can10c, Mer17b\].

The strong version does look novel. AAT’s most promising claim is not that conflicting agents need equilibrium analysis, but the stronger architectural thesis that goal divergence breaks contraction-style composition inheritance: even individually separated agents can compose into a strategically coupled macro-system, and the honest replacement is a tiered equilibrium story with strong results only in the favorable sub-scope and weaker set-level guarantees elsewhere.

A strong one-line framing is this:

AAT’s novelty is not the observation that strategic interaction has equilibria, but the stronger claim that goal divergence is a composition-level phase change: it breaks contraction-style macro inheritance and forces a scope-honest shift to equilibrium analysis.

---

## References

\[Arc20\] M. Arcak and N. C. Martins, “Dissipativity Tools for Convergence to Nash Equilibria in Population Games,” *IEEE Transactions on Control of Network Systems*, vol. 8, pp. 39–50, May 2020, doi: [10.1109/TCNS.2020.3029990](https://doi.org/10.1109/TCNS.2020.3029990).

\[Fox12b\] M. J. Fox and J. Shamma, “Population games, stable games, and passivity,” *2012 IEEE 51st IEEE Conference on Decision and Control (CDC)*, pp. 7445–7450, Dec. 2012, doi: [10.1109/CDC.2012.6426106](https://doi.org/10.1109/CDC.2012.6426106).

\[Pav22\] L. Pavel, “Dissipativity Theory in Game Theory: On the Role of Dissipativity and Passivity in Nash Equilibrium Seeking,” Jun. 01, 2022. doi: [10.1109/MCS.2022.3157119](https://doi.org/10.1109/MCS.2022.3157119).

\[Gok23\] A. Gokhale, A. Davydov, and F. Bullo, “Contractivity of Distributed Optimization and Nash Seeking Dynamics,” *IEEE Control Systems Letters*, vol. 7, pp. 3896–3901, Sep. 2023, doi: [10.1109/LCSYS.2023.3341987](https://doi.org/10.1109/LCSYS.2023.3341987).

\[Fac03\] F. Facchinei and J. Pang, “Finite-Dimensional Variational Inequalities and Complementarity Problems,” 2003. doi: [10.1007/b97543](https://doi.org/10.1007/b97543).

\[Har00\] S. Hart and A. Mas-Colell, “A simple adaptive procedure leading to correlated equilibrium,” Sep. 01, 2000. doi: [10.1111/1468-0262.00153](https://doi.org/10.1111/1468-0262.00153).

\[Gol20c\] N. Golowich, S. Pattathil, and C. Daskalakis, “Tight last-iterate convergence rates for no-regret learning in multi-player games,” *ArXiv*, vol. abs/2010.13724, Oct. 2020.

\[Har03\] S. Hart and A. Mas-Colell, “Uncoupled Dynamics Do Not Lead to Nash Equilibrium,” Nov. 01, 2003. doi: [10.1257/000282803322655581](https://doi.org/10.1257/000282803322655581).

\[Can10c\] O. Candogan, I. Menache, A. Ozdaglar, and P. Parrilo, “Flows and Decompositions of Games: Harmonic and Potential Games,” *Math. Oper. Res.*, vol. 36, pp. 474–503, May 2010, doi: [10.1287/moor.1110.0500](https://doi.org/10.1287/moor.1110.0500).

\[Mer17b\] P. Mertikopoulos, C. Papadimitriou, and G. Piliouras, “Cycles in adversarial regularized learning,” *ACM-SIAM Symposium on Discrete Algorithms*, pp. 2703–2717, Sep. 2017, doi: [10.1137/1.9781611975031.172](https://doi.org/10.1137/1.9781611975031.172).

\[Let19\] A. Letcher *et al.*, “Differentiable Game Mechanics,” *J. Mach. Learn. Res.*, vol. 20, pp. 84:1–84:40, May 2019.
