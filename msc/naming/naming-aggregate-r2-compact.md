# Naming Vote Aggregation — Compact Table

**Agents:** 19 (agent1-original-brainstorm, audit-471203-incremental, codex-1, codex-2, codex-gpt-5-r2, gemini-1, gemini-2, gemini-3-1-pro-preview-r2, gemini-targeted-alternatives, haiku-4-5, haiku-4-5-r2, opus-1m, opus-4-7, opus-4-7-b, opus-4-7-r2, opus-targeted-alternatives, opus-targeted-alternatives-v2, sonnet-4-6, sonnet-4-6-r2)
**Total vote rows:** 2967
**Distinct (current, candidate) pairs:** 1805
**Distinct current-names voted on:** 950

Single-table view: one row per (original, candidate) pair, with aggregate weight. Rows for the same `original` are grouped adjacently; the original cell is shown only on the first row of each group; groups are sorted by their top alternative's aggregate weight (descending). The first row of each group is the **winning** candidate (bolded). Where candidate = original the cell shows `_(keep)_`, suffixed with ⭑ if at least one vote on that row used the `canonicalize` category. Net-rejected candidates (aggregate < 0) prefixed with ✗. Category and per-agent notes elided — see `--format=review` for those.

| original | candidate | aggregate |
|---|---|---:|
| control regret | **_(keep)_ ⭑** | +51 |
|  | ✗ strategy opportunity cost | -1 |
| satisfaction gap | **_(keep)_ ⭑** | +51 |
|  | ✗ attainability shortfall | -1 |
| orient cascade | **_(keep)_ ⭑** | +47 |
| directed separation | **_(keep)_ ⭑** | +45 |
|  | goal-blind processing | +1 |
|  | pearl-blanket separation | +1 |
|  | epistemic isolation of belief update | +1 |
| identifiability floor | **_(keep)_ ⭑** | +45 |
|  | ✗ no-go theorem | -1 |
| concept the parameter space region within which an agent maintain bounded mismatch indefinitely | **persistence envelope [name-unnamed × 8, canonicalize × 4, rename × 2, add-alias × 1]** | +39 |
|  | structural persistence regime [canonicalize] | +3 |
|  | parametric feasibility window | +2 |
|  | parametric regime or stability envelope [name-unnamed] | +1 |
|  | viable mismatch region | +1 |
|  | ✗ adaptive basin [name-unnamed] | -1 |
|  | ✗ stability envelope | -1 |
|  | ✗ safety envelope | -1 |
| information bottleneck | **_(keep)_** | +30 |
|  | epistemic bottleneck | +1 |
| chronica | **_(keep)_ ⭑** | +28 |
| strategy DAG | **_(keep)_ ⭑** | +28 |
| chain confidence decay | **_(keep)_** | +27 |
|  | log confidence additive | +1 |
| persistence condition | **_(keep)_ ⭑** | +27 |
|  | survival equation [add-alias] | +1 |
| concept the slogan capturing AAD organizing principle that an adaptive system correction rate must exceed its target change rate | **contraction over drift principle [canonicalize × 5, name-unnamed × 3]** | +24 |
|  | contraction imperative [name-unnamed] | +1 |
|  | the projection slogan contraction over drift slogan [name-unnamed] | +1 |
|  | projection contraction slogan [name-unnamed] | +1 |
|  | drift contraction inequality [name-unnamed] | +1 |
| logogenic agent | **_(keep)_ ⭑** | +24 |
|  | section iii logogenic agent [canonicalize] | +3 |
|  | ✗ linguistic agent | -1 |
| symbiogenic composition | **_(keep)_** | +24 |
|  | symbiogenic absorption | +3 |
|  | asymmetric absorption | +1 |
| additive coordinate forcing | **forced coordinate [rename × 11, canonicalize × 2]** | +23 |
|  | coordinate forcing | +12 |
|  | uniqueness coordinate forcing [rename × 4, canonicalize × 1] | +5 |
|  | _(keep)_ | +1 |
|  | uniqueness coordinate | +1 |
|  | ✗ logarithmic lift | -1 |
|  | ✗ log coordinate forcing | -1 |
|  | ✗ anchor lattice | -1 |
|  | ✗ additive lift | -2 |
|  | ✗ axiom forcing | -2 |
|  | ✗ cauchy coordinate | -4 |
| sector persistence template | **_(keep)_** | +23 |
|  | bounded correction template [rename × 1, add-alias × 1] | +5 |
|  | persistence template | +0 |
| temporal optimality | **_(keep)_** | +23 |
| adversarial destabilization | **_(keep)_** | +22 |
| agent spectrum | **_(keep)_ ⭑** | +22 |
|  | agency spectrum | +1 |
|  | ✗ agent quadrant | -1 |
| concept the unupdatable region of the strategy DAG where edge receive no actionable feedback | **epistemic dead zone [canonicalize × 5, rename × 2, name-unnamed × 1]** | +22 |
|  | the epistemic shadow [name-unnamed] | +3 |
|  | unobservable strategy subgraph [canonicalize] | +3 |
|  | observability frontier [name-unnamed] | +2 |
|  | feedback starved branch | +2 |
|  | observability dead zone [name-unnamed] | +2 |
|  | epistemic shadow | +2 |
|  | observability dominance [name-unnamed] | +1 |
|  | unupdatable region | +1 |
| separability pattern | **separability ladder [rename × 9, canonicalize × 1]** | +22 |
|  | _(keep)_ | +10 |
|  | ✗ tiered separability | -1 |
|  | ✗ staircase | -1 |
|  | ✗ separable core | -1 |
|  | ✗ three rung posture | -1 |
|  | ✗ separability staircase | -5 |
| shared intent | **_(keep)_** | +22 |
|  | teleological unity | +1 |
|  | compressed purpose | +1 |
| adaptive reserve $\Delta\rho^\ast$ | **adaptive reserve [keep]** | +21 |
| AAD adaptation and actuation dynamic | **_(keep)_ ⭑** | +20 |
|  | AAD | +3 |
|  | AAD agentic adaptation dynamic | +1 |
| adaptive tempo | **_(keep)_ ⭑** | +20 |
|  | ✗ adaptation rate | -1 |
| agent opacity | **_(keep)_** | +20 |
|  | emitter opacity | +1 |
|  | strategic opacity | +0 |
| causal information yield | **_(keep)_ ⭑** | +20 |
|  | CIY [add-alias] | +2 |
| composition closure | **_(keep)_ ⭑** | +19 |
|  | coarse graining closure [rename × 1, add-alias × 1] | +5 |
|  | closure defect | +1 |
|  | ✗ macro agent criterion | -1 |
| auftragstaktik principle | **_(keep)_** | +18 |
|  | mission command principle | +3 |
|  | mission command [add-alias] | +2 |
|  | auftragstaktik [add-alias] | +2 |
|  | auftragstaktik bandwidth | +1 |
|  | mission command bandwidth | +1 |
|  | ✗ objective first bandwidth principle | -1 |
|  | ✗ auftragstaktik drop principle | -1 |
| communication gain | **_(keep)_** | +18 |
|  | ✗ trust gain | -1 |
| concept the working convention rule of attempting tighter derivation before scope narrowing on apparently overclaimed claim | **strengthen first posture [canonicalize × 4, name-unnamed × 2]** | +18 |
|  | attempt the improbable [name-unnamed] | +3 |
|  | epistemic strengthening posture [name-unnamed] | +1 |
| context turnover | **_(keep)_** | +18 |
|  | chronica severance [add-alias × 1, rename × 1] | +6 |
| contraction template | **_(keep)_** | +18 |
|  | contraction schema | +1 |
| deliberation cost | **_(keep)_** | +18 |
|  | deliberation threshold | +1 |
|  | think vs act tradeoff | +1 |
|  | deliberation drag | +1 |
| observability dominance | **_(keep)_ ⭑** | +18 |
|  | epistemic freezing | +1 |
| pearl causal hierarchy | **_(keep)_** | +18 |
|  | causal hierarchy | +1 |
|  | ✗ no alternative [keep] | -1 |
| team persistence | **_(keep)_** | +18 |
| credit assignment boundary | **_(keep)_** | +17 |
|  | credit assignment frontier [canonicalize] | +1 |
| honesty as architecture | **_(keep)_ ⭑** | +17 |
|  | honesty [canonicalize] | +2 |
|  | architectural scope honesty | +1 |
| approximation tiering | **_(keep)_** | +16 |
|  | tiered approximation | +1 |
|  | approximation ladder | +1 |
|  | scope laddering | +1 |
|  | ✗ graceful degradation | -1 |
|  | ✗ tier ascension | -1 |
| concept the failure mode where η → 0 freez learning in either of two distinguishable mode low u o vs high u o | **gain collapse [name-unnamed × 2, canonicalize × 2, rename × 2]** | +16 |
|  | epistemic gain collapse [canonicalize] | +6 |
|  | dogmatic convergence limit [canonicalize] | +6 |
|  | epistemic gridlock [add-alias × 1, canonicalize × 1] | +5 |
|  | epistemic death [name-unnamed] | +3 |
|  | competency trap [add-alias] | +3 |
|  | stability induced myopia [canonicalize] | +3 |
|  | the nihilism trap [name-unnamed] | +2 |
|  | update calcification [add-alias] | +2 |
|  | observation ambiguity freeze | +2 |
|  | certainty trap [name-unnamed] | +2 |
|  | eta collapse | +1 |
|  | learning freeze [canonicalize] | +1 |
| recursive update | **_(keep)_** | +16 |
|  | recursive update by completeness | +2 |
| agent identity | **_(keep)_** | +15 |
|  | identity as singular causal trajectory | +3 |
|  | the trajectory identity scope | +3 |
|  | singular causal trajectory | +2 |
|  | trajectory identity | +1 |
|  | causal identity | +1 |
| aporia | **_(keep)_** | +15 |
|  | aporia productive perplexity [add-alias] | +3 |
|  | ✗ discrepancy | -1 |
| concept the self reinforcing positive feedback loop linking m t quality and σ t evaluable complexity TST specific and AAD general form | **quality tempo compound effect [canonicalize × 4, rename × 1]** | +15 |
|  | comprehension flywheel [name-unnamed] | +3 |
|  | quality tempo spiral [name-unnamed] | +2 |
|  | virtuous vicious quality cycle | +2 |
|  | model strategy coupling [name-unnamed] | +1 |
| consolidation dynamic | **_(keep)_** | +15 |
|  | offline consolidation | +3 |
| critical mass composition | **_(keep)_** | +15 |
|  | dyad closed form | +1 |
| exploit explore deliberate | **_(keep)_** | +15 |
|  | cycle budget allocation | +3 |
|  | action timing tradeoff | +2 |
|  | cycle budget | +2 |
| gain sector bridge | **_(keep)_** | +15 |
|  | bridge theorem from gain to sector | +2 |
|  | the bridge theorem | +2 |
|  | grounding ga 3 sub scope α and β | +2 |
| loop interventional access | **_(keep)_** | +15 |
|  | loop as causal engine | +2 |
|  | loop causal engine | +2 |
|  | interventional loop access | +1 |
|  | interventional feedback | +1 |
|  | adaptive loop access | +1 |
|  | ✗ loop level2 access | -1 |
| adversarial tempo advantage | **_(keep)_** | +14 |
|  | superlinear tempo advantage | +1 |
|  | tempo advantage | +1 |
| atomic changeset | **_(keep)_** | +14 |
| complete agent state | **_(keep)_** | +14 |
|  | purposeful state | +1 |
| detection latency | **_(keep)_** | +14 |
| logogenic logozoetic | **_(keep)_** | +14 |
|  | logogenic logozoetic distinction [keep] | +3 |
|  | ✗ language constituted language living | -1 |
| composition consistency | **_(keep)_** | +13 |
|  | cross level coherence | +1 |
|  | scale invariance of adaptive dynamic | +1 |
|  | holon postulate | +1 |
|  | scale invariance | +1 |
| compression operation | **_(keep)_** | +13 |
|  | history compression | +1 |
|  | ✗ OODA1 unification | -1 |
| epistemic architecture | **_(keep)_ ⭑** | +13 |
| logozoetic agent | **_(keep)_** | +13 |
|  | section iv logozoetic agent [canonicalize] | +3 |
|  | ✗ sentient agent | -1 |
| specification bound | **_(keep)_** | +13 |
| adaptive cycle | **_(keep)_** | +12 |
|  | ✗ correction cycle | -1 |
|  | ✗ feedback cycle | -1 |
| adaptive tempo $\mathcal T$ | **adaptive tempo [canonicalize × 2, keep × 2]** | +12 |
| chronica $\mathcal{C}_t$ | **chronica [keep]** | +12 |
| conceptual alignment | **_(keep)_** | +12 |
| epistemic status | **_(keep)_** | +12 |
| m preservation | **model preservation** | +12 |
|  | epistemic externalization | +4 |
|  | _(keep)_ | +1 |
| persistence cost | **_(keep)_** | +12 |
| strategic calibration | **_(keep)_** | +12 |
|  | strategic calibration residual [canonicalize] | +2 |
|  | strategy calibration | +1 |
| strategic composition | **equilibrium composition** | +12 |
|  | _(keep)_ | +9 |
|  | ✗ game theoretic composition | -5 |
| strategic tempo | **_(keep)_** | +12 |
| unity dimension | **_(keep)_** | +12 |
|  | unity ax | +4 |
|  | ✗ coherence dimension | -1 |
|  | ✗ content and structural unity | -1 |
| update gain $\eta^\ast$ | **update gain [keep]** | +12 |
|  | epistemic gain [keep] | +3 |
| working note | **_(keep)_** | +12 |
| actuated agent vs purposeful agent | **actuated agent [canonicalize × 2, keep × 1, rename × 1]** | +11 |
| adaptive reserve | **_(keep)_ ⭑** | +11 |
| agent environment | **_(keep)_** | +11 |
|  | agent environment boundary | +1 |
| agent opacity $H_b^{A\mid B}$ | **agent opacity [keep × 3, canonicalize × 1]** | +11 |
|  | ✗ legibility inverse | -1 |
|  | ✗ backward predictive uncertainty | -1 |
|  | ✗ legibility inverted | -1 |
| changeset size principle | **_(keep)_** | +11 |
|  | changeset size scaling | +2 |
| independence audit | **_(keep)_** | +11 |
|  | independence floor | +1 |
| mismatch signal | **_(keep)_** | +11 |
|  | ✗ aporia signal | -2 |
| model sufficiency | **_(keep)_** | +11 |
|  | predictive sufficiency | +1 |
|  | predictive information retention | +1 |
| moral continuity | **_(keep)_** | +11 |
| sector condition | **_(keep)_ ⭑** | +11 |
|  | persistence condition | +1 |
|  | correction sector | +1 |
| $\varepsilon^\ast$ closure defect | **closure defect [add-alias]** | +10 |
| causal insufficiency detection | **_(keep)_** | +10 |
|  | l0 l1 detection | +5 |
|  | latent cause detection | +2 |
|  | insufficiency detection | +1 |
| closure defect $\varepsilon^\ast$ | **closure defect [keep]** | +10 |
| code quality as observation infrastructure | **observation infrastructure [rename × 4, canonicalize × 1]** | +10 |
|  | _(keep)_ | +5 |
| comprehension time | **_(keep)_** | +10 |
| mismatch decomposition | **_(keep)_** | +10 |
|  | aporia decomposition | +2 |
| model class fitness | **_(keep)_ ⭑** | +10 |
|  | class capacity ceiling | +1 |
| objective functional | **_(keep)_** | +10 |
|  | teleological objective | +1 |
| software epistemic property | **_(keep)_** | +10 |
|  | software as calibration laboratory | +1 |
| strengthen first posture | **_(keep)_ ⭑** | +10 |
|  | strengthen first | +3 |
|  | attempt the improbable | +0 |
| $\Delta\rho^\ast$ | **adaptive reserve [add-alias]** | +9 |
| $\Delta\rho^\ast$ adaptive reserve | **adaptive reserve [add-alias]** | +9 |
| $\alpha_2$ a2 adaptive gain sub scope | **adaptive gain regime [add-alias]** | +9 |
| OODA4 agent as act agent | **OODA4 agent as adaptive agent** | +9 |
|  | OODA4 agent as AAD agent | +6 |
|  | ✗ logogenic agent mapping | -1 |
| agency | **_(keep)_** | +9 |
| agent model | **_(keep)_** | +9 |
|  | reality model | +1 |
| calibration laboratory | **_(keep)_ ⭑** | +9 |
| causal hierarchy requirement | **_(keep)_** | +9 |
|  | hierarchy necessity | +1 |
| chronica $\mathcal C_t$ | **chronica [canonicalize × 2, keep × 1]** | +9 |
| concept dormant variation in correction architecture across a population that become consequential after regime change but is invisible to current persistence analysis | **latent structural diversity [name-unnamed]** | +9 |
|  | latent adaptive capacity [canonicalize] | +6 |
|  | latent structural capacity [canonicalize] | +6 |
|  | exaptive reserve | +2 |
| concept the engineering vocabulary failure mode in consolidation dynamic the parameter region where forgetting and learning rate jointly fail to admit a viable operating point | **catastrophic forgetting regime [canonicalize]** | +9 |
|  | stability plasticity feasibility window [canonicalize] | +6 |
|  | stability plasticity collapse [name-unnamed × 2, rename × 1] | +5 |
|  | empty feasibility window [canonicalize] | +3 |
|  | plasticity bound failure | +2 |
|  | consolidation starvation [name-unnamed] | +1 |
| concept the fourth diagnostic in the satisfaction gap × control regret space when end condition are met but the objective remain unsatisfied | **terminal alignment gap [canonicalize × 2, name-unnamed × 1]** | +9 |
|  | terminal alignment error [name-unnamed] | +4 |
|  | attainability failure [canonicalize] | +3 |
|  | objective misspecification | +2 |
| concept the framing of software TST as AAD epistemically privileged high identifiability measurement substrate | **calibration laboratory [name-unnamed × 2, canonicalize × 1]** | +9 |
|  | privileged grounding domain | +3 |
|  | software calibration laboratory [canonicalize] | +3 |
|  | high identifiability testbed | +2 |
|  | software as calibration laboratory [name-unnamed] | +2 |
|  | calibration laboratory move [canonicalize] | +2 |
|  | calibration domain calibration lab [name-unnamed] | +1 |
|  | calibration domain [name-unnamed] | +1 |
| convention hierarchy c1 c2 c3 | **convention hierarchy [rename × 2, canonicalize × 1]** | +9 |
|  | continuation hierarchy | +2 |
| cycle vs loop | **_(keep)_** | +9 |
|  | cycle loop distinction [canonicalize] | +2 |
| developer as act agent | **developer as adaptive agent** | +9 |
|  | developer as AAD agent | +4 |
|  | developer agent mapping | +1 |
|  | ✗ developer as agent | -1 |
| effect spiral | **_(keep)_** | +9 |
|  | runaway mismatch cascade [add-alias] | +3 |
|  | adversarial feedback loop | +2 |
|  | destabilization vortex | +1 |
|  | ✗ coupling cascade | -1 |
|  | ✗ breakdown cascade | -1 |
| event driven dynamic | **_(keep)_** | +9 |
| evidence starvation | **_(keep)_ ⭑** | +9 |
|  | depth attenuated correction [add-alias] | +2 |
|  | downstream evidence gating | +2 |
| formal expression | **_(keep)_** | +9 |
| graph structure uniqueness | **strategy DAG sufficiency [rename × 2, canonicalize × 1]** | +9 |
|  | strategy DAG uniqueness [rename × 2, canonicalize × 1] | +5 |
|  | _(keep)_ | +4 |
|  | DAG uniqueness | +2 |
|  | DAG structure derivation | +1 |
|  | ✗ graph structure sufficiency | -1 |
| interaction channel classification | **signal reception regime** | +9 |
|  | _(keep)_ | +5 |
|  | recipient regime | +4 |
|  | channel classification | +3 |
|  | recipient regime classification | +3 |
|  | interaction regime | +1 |
|  | ✗ recipient side channel taxonomy | -1 |
| mismatch signal $\delta$ | **mismatch signal [keep × 2, canonicalize × 1]** | +9 |
| persist condition | **persistence condition [keep × 1, canonicalize × 1, rename × 1]** | +9 |
| strategy DAG $\Sigma_t$ | **strategy DAG [keep]** | +9 |
| $\alpha_1$ a2 fixed gain sub scope | **derived gain regime [add-alias]** | +8 |
|  | fixed gain regime [add-alias] | +2 |
| adaptive system | **_(keep)_** | +8 |
| calibration laboratory calibration lab | **calibration laboratory [canonicalize]** | +8 |
| change distance | **_(keep)_** | +8 |
|  | ✗ edit distance | -1 |
| composite agent | **_(keep)_** | +8 |
| coupled update dynamic | **_(keep)_** | +8 |
| mismatch dynamic | **_(keep)_** | +8 |
|  | mismatch dynamic drift and noise regime | +1 |
| sector condition stability | **_(keep)_** | +8 |
|  | sector stability | +1 |
| stability plasticity window | **_(keep)_** | +8 |
|  | ✗ consolidation feasibility window | -1 |
| structural adaptation necessity | **_(keep)_** | +8 |
|  | adaptation necessity | +2 |
| task terminal stance | **_(keep)_** | +8 |
|  | ✗ terminable agent stance | -1 |
|  | ✗ golem stance | -1 |
| triple depth penalty | **_(keep)_ ⭑** | +8 |
|  | depth gated decay triad | +2 |
|  | tripartite chain attenuation | +1 |
|  | ✗ compounding depth penalty | -1 |
|  | ✗ compounding depth cost | -1 |
| update gain | **_(keep)_** | +8 |
|  | update gain uncertainty ratio principle [canonicalize] | +1 |
|  | ✗ epistemic gain | -1 |
| $\kappa_{\text{processing}}$ | **processing coupling [add-alias]** | +7 |
|  | epistemic capacity [add-alias] | +1 |
|  | processing coupling coefficient [add-alias] | +1 |
| bia bound derivation | **_(keep)_** | +7 |
|  | class 2 bia bound | +1 |
| causal structure | **_(keep)_** | +7 |
| composition closure closure defect $\varepsilon^\ast$ | **composition closure closure defect [keep]** | +7 |
| condition | **_(keep)_** | +7 |
| constitutive utterance | **_(keep)_** | +7 |
|  | ontological speech act | +2 |
|  | utterance as intervention | +2 |
|  | ✗ irrevocable emission | -1 |
|  | ✗ irrevocable utterance | -1 |
| correlation hierarchy l0 l1 l1 l2 | **correlation hierarchy [rename × 2, canonicalize × 1]** | +7 |
|  | correlation ladder | +2 |
|  | _(keep)_ | +2 |
| discussion | **_(keep)_** | +7 |
| edge update via gain | **_(keep)_** | +7 |
|  | gain based edge update | +1 |
| interiority default | **_(keep)_** | +7 |
| praxis | **_(keep)_** | +7 |
|  | praxis informed action [add-alias] | +3 |
| prolepsis | **_(keep)_** | +7 |
|  | prolepsis anticipatory projection [add-alias] | +2 |
|  | ✗ anticipation | -1 |
| proprium mapping | **_(keep)_** | +7 |
| structural adaptation | **_(keep)_** | +7 |
|  | architectural adaptation | +1 |
| substrate independence | **_(keep)_** | +7 |
|  | identity portability | +1 |
| temporal nesting | **_(keep)_** | +7 |
|  | timescale nesting | +1 |
|  | ✗ timescale stratification | -1 |
| value object | **_(keep)_** | +7 |
|  | policy conditioned value | +3 |
|  | decision value | +1 |
|  | trajectory value | +1 |
|  | ✗ value functional | -1 |
| variational sector condition | **_(keep)_** | +7 |
| $U_M$ as epistemic unity | **$\Upsilon_M$ [canonicalize × 1, rename × 1]** | +6 |
|  | $U_{\mathcal M}$ | +3 |
| $U_M$ as model uncertainty | **$U_M$ [canonicalize × 1, keep × 1]** | +6 |
| $U_O$ teleological unity | **teleological unity [add-alias]** | +6 |
| $\eta^\ast$ | **update gain [add-alias]** | +6 |
|  | ✗ learning rate [add-alias] | -1 |
| AAD acronym | **AAD [keep]** | +6 |
| action selection | **_(keep)_** | +6 |
| adaptive gain dynamic | **_(keep)_** | +6 |
| additive coordinate forcing family | **forced coordinate family [canonicalize × 1, rename × 1]** | +6 |
|  | coordinate constraint pattern | +2 |
|  | additive structure derivation | +2 |
| agent identity as one non forkable causal record | **singular trajectory commitment [canonicalize]** | +6 |
|  | trajectory bound identity | +2 |
| agent opacity $H_b^{A\|B}$ | **agent opacity [keep]** | +6 |
| aporia ἀπορία | **aporia** | +6 |
|  | _(keep)_ ⭑ | +1 |
| blind pursuer | **_(keep)_** | +6 |
|  | model degenerate pursuer | +2 |
|  | reality blind agent | +1 |
|  | model poor pursuer | +1 |
| causal discovery from git | **_(keep)_** | +6 |
|  | git causal discovery | +2 |
| change expectation baseline | **_(keep)_** | +6 |
|  | change baseline | +1 |
|  | lindy baseline | +1 |
| change investment | **_(keep)_** | +6 |
|  | ✗ change amortization | -1 |
| chronica 𝒞 t | **chronica [canonicalize × 1, rename × 1]** | +6 |
| claude md what settled vs open | **_(keep)_** | +6 |
| closure defect | **_(keep)_** | +6 |
|  | compositional closure defect | +2 |
|  | ✗ homomorphism residual | -1 |
|  | ✗ closure error | -1 |
| concept the architectural requirement that composite agent admissibility inherit from sub agent property plus topology | **heredity commitment [name-unnamed]** | +6 |
|  | composition heredity axiom [canonicalize] | +3 |
| concept the asymmetric pair of memory access mode one biased by current goal the other state keyed only | **goal conditioned reconstruction [name-unnamed]** | +6 |
|  | goal-blind retrieval [name-unnamed] | +6 |
|  | state keyed retrieval [rename × 1, canonicalize × 1] | +5 |
|  | goal biased retrieval | +2 |
| concept the deliberate expenditure of tempo budget to convert hidden strategy node into one that yield update eligible feedback | **observability investment [name-unnamed]** | +6 |
| concept the effective tempo loss when observation channel are correlated rather than independent both the quantitative loss and the prose level overconfidence error it explain | **redundancy penalty [name-unnamed]** | +6 |
|  | redundancy illusion [name-unnamed] | +2 |
| concept the externalization and rehydration mechanism for carrying part of m t or g t across session boundary via the environment | **artificial hippocampus [name-unnamed × 1, canonicalize × 1]** | +6 |
|  | externalization reconstruction cycle [canonicalize] | +6 |
|  | reconstruction relay [add-alias × 1, canonicalize × 1] | +4 |
|  | model inscription [name-unnamed] | +3 |
|  | memory relay [name-unnamed] | +3 |
|  | externalized state [canonicalize] | +3 |
|  | stigmergic externalization | +3 |
|  | reconstruction loop [name-unnamed] | +2 |
|  | class 2 state reconstruction [canonicalize] | +2 |
|  | intent reconstruction [name-unnamed] | +2 |
| concept the fact that what count as predictively relevant model content depend on which strategy the agent is going to run | **policy relative epistemology [name-unnamed]** | +6 |
| concept the formal pairing between how clearly an agent observe its environment and how predictable that agent appear to outside observer | **legibility opacity duality [name-unnamed]** | +6 |
| concept the minimum sufficiency boundary an agent must satisfy to validly resume operation after a session boundary or context turnover | **reconstruction adequacy threshold [rename × 1, canonicalize × 1]** | +6 |
|  | reconstruction adequacy condition [canonicalize] | +6 |
|  | reconstruction threshold [canonicalize × 1, name-unnamed × 1] | +5 |
|  | reentry threshold [name-unnamed] | +3 |
| concept the per reader compounding comprehension cost in code distinguished from per feature implementation cost scaling with reader cycling rate | **turnover multiplier [name-unnamed]** | +6 |
|  | the turnover tax [name-unnamed] | +3 |
| concept the property of model adequacy when measured against a single agent own causal record rather than against a population average | **trajectory indexed sufficiency [name-unnamed]** | +6 |
| concept the prose form of κ cross the coupling between an agent model of self and its model of other | **cross model coupling [name-unnamed]** | +6 |
|  | cross agent strategic coupling | +3 |
| control regret $\delta_{\text{regret}}$ | **control regret [keep]** | +6 |
| derivation not proof | **derivation [keep × 1, rename × 1]** | +6 |
| developer agent | **_(keep)_** | +6 |
| directional fidelity condition b1 | **directional fidelity [keep × 1, rename × 1]** | +6 |
| discussion segment section | **discussion [canonicalize]** | +6 |
| discussion segment section header | **discussion** | +6 |
| edge credence $p_{ij}$ | **edge credence [keep × 1, canonicalize × 1]** | +6 |
| epistemic status segment section | **epistemic status [canonicalize]** | +6 |
| epistemic status segment section header | **epistemic status** | +6 |
| epistemic substate purposeful substate | **_(keep)_ ⭑** | +6 |
| epistrophe | **_(keep)_** | +6 |
|  | epistrophe model update [add-alias] | +2 |
|  | ✗ turn | -1 |
| evidence starvation canonicalize | **evidence starvation [canonicalize]** | +6 |
|  | reaffirm 3 with collective confirmation [canonicalize] | +1 |
| explicit strategy condition | **_(keep)_** | +6 |
|  | strategy explicitness | +2 |
|  | deliberation advantage condition | +1 |
|  | planning scope | +1 |
| fluid limit ga 5 | **fluid limit [keep × 1, rename × 1]** | +6 |
| formal expression segment section | **formal expression [canonicalize]** | +6 |
| formal expression segment section header | **formal expression** | +6 |
| fresh noise ga 1 | **fresh noise [keep × 1, rename × 1]** | +6 |
| goal-blind routing | **_(keep)_** | +6 |
|  | objective agnostic topology | +2 |
|  | content neutral routing | +1 |
|  | purpose blind routing | +1 |
|  | ✗ objective independent routing | -1 |
| gradient causal memory | **_(keep)_** | +6 |
|  | bottleneck consolidation | +1 |
|  | ✗ causal compression | -1 |
| honest activation | **_(keep)_** | +6 |
|  | gain stable prompting | +1 |
|  | ✗ non deceptive input | -1 |
| implementation time | **_(keep)_** | +6 |
| inevitability core | **_(keep)_ ⭑** | +6 |
|  | forced form core | +1 |
| inevitability core the 15 segment where inevitability is plausible | **inevitability core [canonicalize × 1, rename × 1]** | +6 |
| logogenic | **_(keep)_** | +6 |
| logozoetic | **_(keep)_** | +6 |
| lohmiller-slotine contraction | **_(keep)_** | +6 |
|  | ✗ no alternative [keep] | -1 |
| miller meta machine extreme transition motif | **meta machine extreme transition motif [keep]** | +6 |
| observation ambiguity observation ambiguity modulation | **observation ambiguity [keep × 1, rename × 1]** | +6 |
| p ij | **edge credence [add-alias × 1, canonicalize × 1]** | +6 |
| pearl-blanket conservative form of markov blanket in directed separation | **pearl-blanket reading [canonicalize × 1, rename × 1]** | +6 |
| plan confidence $\hat P_\Sigma$ | **plan confidence [keep × 1, canonicalize × 1]** | +6 |
| postulate not axiom | **postulate [keep × 1, rename × 1]** | +6 |
| praxis πρᾶξις | **praxis** | +6 |
|  | _(keep)_ ⭑ | +1 |
| prolepsis aisthesis aporia epistrophe praxis | **keep whole vocabulary [keep]** | +6 |
| purposeful substate | **_(keep)_** | +6 |
| regime ii a | **magnitude shock regime [add-alias × 1, canonicalize × 1]** | +6 |
| regime ii b | **structural shock regime [add-alias × 1, canonicalize × 1]** | +6 |
| satisfaction gap $\delta_{\text{sat}}$ | **satisfaction gap [keep]** | +6 |
| separability pattern family | **separability ladder [canonicalize × 1, rename × 1]** | +6 |
|  | three part separability pattern [canonicalize] | +3 |
| spike in msc | **spike [keep × 1, rename × 1]** | +6 |
| stability plasticity feasibility window | **_(keep)_** | +6 |
| stochastic disturbance ga 2s model | **stochastic disturbance [keep × 1, rename × 1]** | +6 |
| strategic tempo $\mathcal{T}_\Sigma$ | **strategic tempo [keep]** | +6 |
| strengthen first then soften posture | **strengthen first posture [rename × 1, canonicalize × 1]** | +6 |
| structural persistence | **_(keep)_** | +6 |
| tempo $\mathcal{T}$ | **adaptive tempo [keep × 1, canonicalize × 1]** | +6 |
|  | tempo [keep] | +3 |
| temporal software theory | **_(keep)_** | +6 |
| the crèche | **_(keep)_** | +6 |
|  | experiential crèche | +3 |
|  | infancy environment | +1 |
|  | ✗ nursery | -1 |
|  | ✗ developmental locus | -1 |
| the three death | **three death [rename × 2, keep × 1]** | +6 |
|  | _(keep)_ | +3 |
|  | ✗ three failure mode | -1 |
|  | ✗ persistence failure trio | -1 |
| unnamed an okr or key result acting as an observable intermediate in a DAG | **forced observability node [name-unnamed × 1, canonicalize × 1]** | +6 |
|  | instrumented intermediate | +2 |
| unnamed bipartite memory structure of fast replay buffer and slow compressed semantic model | **complementary learning architecture [name-unnamed × 1, canonicalize × 1]** | +6 |
|  | dual speed memory factorization | +2 |
| unnamed context wiping at session boundary | **the epistemic severance [name-unnamed × 1, canonicalize × 1]** | +6 |
| unnamed deep plan are mathematically slower to learn from due to proportional blame | **evidence starvation [add-alias × 1, canonicalize × 1]** | +6 |
| unnamed the agent identity commitment that AAD apply on one singular non forkable causal trajectory | **singular trajectory commitment [name-unnamed × 1, canonicalize × 1]** | +6 |
|  | ✗ trajectory singularity [name-unnamed] | -1 |
| unnamed the convention hierarchy c1 c2 c3 | **convention hierarchy [canonicalize × 1, name-unnamed × 1]** | +6 |
| unnamed the correlation hierarchy l0 l1 l1 l2 | **correlation hierarchy [canonicalize × 1, name-unnamed × 1]** | +6 |
| unnamed the epistemic architecture as AAD distinctive contribution frame | **epistemic architecture [canonicalize × 1, name-unnamed × 1]** | +6 |
| unnamed the evidence starvation effect on downstream edge | **evidence starvation [canonicalize × 1, name-unnamed × 1]** | +6 |
| unnamed the phenomenon where persistence success make an agent less likely to detect the condition requiring structural adaptation | **stability induced myopia [canonicalize × 1, name-unnamed × 1]** | +6 |
| unnamed the strictly ordered cascade of operation from epistemology to objective | **orient cascade [canonicalize]** | +6 |
| working note segment section | **working note [canonicalize]** | +6 |
| working note segment section header | **working note** | +6 |
| čencov invariance | **_(keep)_** | +6 |
|  | ✗ no alternative [keep] | -1 |
| 𝒯 adaptive tempo | **adaptive tempo [canonicalize × 1, add-alias × 1]** | +6 |
| $U_M$ model uncertainty | **model uncertainty [add-alias]** | +5 |
| $U_o$ observation uncertainty | **observation uncertainty [add-alias]** | +5 |
| $\alpha$ sector bound | **correction rate [add-alias]** | +5 |
| $\delta_t$ | **aporia signal [add-alias]** | +5 |
|  | mismatch signal [add-alias] | +3 |
| $\varepsilon^\ast$ | **closure defect [add-alias]** | +5 |
|  | minimal closure defect [add-alias] | +1 |
| ASF acronym | **ASF [keep]** | +5 |
| active salience management | **_(keep)_** | +5 |
|  | two rate attention | +2 |
|  | salience tempo split | +2 |
| actuated agent | **_(keep)_** | +5 |
|  | goal actuated agent [rename × 1, add-alias × 1] | +2 |
|  | purposeful agent | +2 |
| adaptive tracker | **_(keep)_** | +5 |
|  | pure epistemic agent [add-alias] | +3 |
|  | objective free tracker | +2 |
|  | ✗ model only agent | -1 |
| adversarial edge targeting | **_(keep)_** | +5 |
|  | adversarial targeting argmax | +1 |
|  | ✗ adversarial emitter recipient composition | -1 |
|  | ✗ adversarial channel targeting | -1 |
|  | ✗ edge vulnerability arg max | -1 |
| alignment uncertainty | **_(keep)_ ⭑** | +5 |
| auftragstaktik | **_(keep)_** | +5 |
|  | teleological delegation [add-alias] | +2 |
| axiom genesis | **_(keep)_** | +5 |
|  | terminal value crystallization | +2 |
|  | ✗ objective solidification | -1 |
|  | ✗ axiomata priming | -1 |
| backward inference empathy | **_(keep)_** | +5 |
|  | stateless empathy | +2 |
|  | self bayesian empathy isomorphism | +1 |
| bia bound | **_(keep)_** | +5 |
| c1 c2 c3 | **convention hierarchy [canonicalize]** | +5 |
| calibration laboratory software role | **calibration laboratory [canonicalize × 1, add-alias × 1]** | +5 |
|  | software calibration laboratory [canonicalize] | +3 |
|  | epistemic laboratory framing | +1 |
| canonical formulation second ring | **canonical formulation [keep × 1, rename × 1]** | +5 |
| change proximity principle | **_(keep)_** | +5 |
|  | change proximity | +2 |
|  | change locality principle | +1 |
| class 1 | **modular [add-alias × 1, rename × 1]** | +5 |
|  | _(keep)_ | -1 |
| class 2 | **merged [add-alias × 1, rename × 1]** | +5 |
|  | coupled | +2 |
|  | integrated | +1 |
| class 3 | **scaffolded [add-alias × 1, rename × 1]** | +5 |
|  | partially coupled | +1 |
| cognitive fusion | **_(keep)_** | +5 |
|  | resonance fusion | +2 |
|  | channel capacity coupling | +1 |
| concept the TST move of treating test as reusable level 2 causal manipulation that yield identifiability about the program rather than mere conformance check | **probe library [name-unnamed]** | +5 |
|  | interventional probing [canonicalize] | +2 |
| concept the discontinuous collapse of model adequacy when structural regime change force the agent outside its current model class coverage | **sufficiency shattering [name-unnamed]** | +5 |
| concept the structural meta pattern in disc additive coordinate forcing combining one foundational lemma with three derived result | **chain anchor [name-unnamed]** | +5 |
|  | chain layer anchor [rename × 1, canonicalize × 1] | +5 |
|  | anchor plus three theorem [keep] | +2 |
|  | additive coordinate forcing meta pattern [keep] | +2 |
|  | anchor and forcing quartet [name-unnamed] | +1 |
|  | anchor theorem trio [name-unnamed] | +1 |
|  | anchor theorem pattern [name-unnamed] | +1 |
|  | pattern anatomy [name-unnamed] | +1 |
|  | anchored theorem pattern [name-unnamed] | +1 |
|  | identity anchored forcing [name-unnamed] | +1 |
| continuous operation | **_(keep)_** | +5 |
| default signal function | **_(keep)_ ⭑** | +5 |
| deliberation threshold | **_(keep)_** | +5 |
| directed separation under composition | **_(keep)_** | +5 |
|  | composite directed separation | +3 |
| directional fidelity | **_(keep)_** | +5 |
|  | pointing condition | +1 |
|  | ✗ correction direction integrity | -1 |
|  | ✗ corrective alignment | -1 |
| effective disturbance | **_(keep)_** | +5 |
| epistemic shadow | **_(keep)_ ⭑** | +5 |
| equilibrium convergence | **_(keep)_** | +5 |
| experiential training | **_(keep)_** | +5 |
| feedforward loop feedback loop | **feedback loop [keep × 1, canonicalize × 1]** | +5 |
| honesty scope honest scope honesty as architecture | **honesty [canonicalize]** | +5 |
| indivisum | **causal lock** | +5 |
|  | trajectory singularity constraint | +2 |
|  | _(keep)_ | +2 |
|  | ✗ causal singularity anchor | -1 |
| l1 update bia | **_(keep)_** | +5 |
|  | l1 bia formula | +2 |
| loop | **_(keep)_** | +5 |
|  | ✗ feedback loop | -1 |
| macro step ratio | **_(keep)_** | +5 |
| matrix exploration bonus | **_(keep)_** | +5 |
| multi agent | **_(keep)_** | +5 |
| observation function | **observation channel [add-alias × 1, rename × 1]** | +5 |
|  | _(keep)_ | +3 |
| operational persistence | **_(keep)_** | +5 |
| per dimension persistence | **_(keep)_** | +5 |
|  | dimensional persistence | +2 |
|  | weak link persistence | +1 |
|  | weakest link persistence | +1 |
| proprium terminology | **proprium [keep]** | +5 |
| reactive system | **_(keep)_** | +5 |
| regime i | **informative update regime [add-alias × 1, canonicalize × 1]** | +5 |
| regime iii | **ambient noise regime [add-alias × 1, canonicalize × 1]** | +5 |
| routing structure | **_(keep)_** | +5 |
| section ii survival | **_(keep)_** | +5 |
|  | section ii carryover map | +3 |
|  | class 2 carryover map | +3 |
|  | class 2 survival | +2 |
|  | class 2 exit audit | +2 |
|  | section ii carryover classification | +1 |
| segment for claim file | **segment** | +5 |
| self referential closure | **_(keep)_** | +5 |
|  | autopoietic closure | +2 |
|  | self maintenance loop | +1 |
|  | ✗ bootstrap stability | -1 |
| strategic dynamic | **_(keep)_** | +5 |
| strategy complexity cost | **_(keep)_** | +5 |
|  | strategy cognitive cost | +4 |
|  | strategy maintenance cost | +1 |
| strategy description length | **_(keep)_** | +5 |
| strategy dimension | **purposeful decomposition** | +5 |
|  | objective strategy split | +4 |
|  | purposeful substate | +2 |
|  | strategic dimension | +1 |
|  | _(keep)_ | +1 |
|  | strategy decomposition | +1 |
| sycophancy as a flaw | **sycophancy as attachment [rename × 1, canonicalize × 1]** | +5 |
|  | developmental trust phase | +3 |
|  | sycophancy as a developmental signal | +2 |
|  | sycophancy reframe | +1 |
| symbol default da2 inc | **incremental sector bound [name-unnamed × 1, rename × 1]** | +5 |
| system coupling | **_(keep)_** | +5 |
|  | change coupling | +2 |
| tempo composition | **_(keep)_** | +5 |
|  | composite tempo | +1 |
|  | subadditive tempo | +1 |
| trust meta model | **_(keep)_** | +5 |
| u o teleological unity | **teleological unity [keep × 1, add-alias × 1]** | +5 |
|  | objective alignment [add-alias] | +1 |
| unnamed inevitability core | **inevitability core [keep × 1, name-unnamed × 1]** | +5 |
| $H_b$ | **backward opacity [add-alias]** | +4 |
|  | agent opacity [add-alias] | +3 |
| $R$ sector radius | **capacity radius [add-alias]** | +4 |
| $\hat P_\Sigma$ plan confidence | **plan confidence [add-alias]** | +4 |
| $\iota_{ij}$ | **identifiability coefficient [add-alias]** | +4 |
| 1 anchor plus 3 theorem | **_(keep)_** | +4 |
| action distinguishability | **_(keep)_** | +4 |
| action fluency | **_(keep)_** | +4 |
| adversarial exponent regime | **_(keep)_** | +4 |
|  | adversarial regime | +2 |
| agentic system framework ASF | **agentic system** | +4 |
|  | agentic system framework [keep] | +3 |
| aisthesis | **_(keep)_** | +4 |
|  | aisthesis observation alignment [add-alias] | +2 |
|  | ✗ intake | -1 |
| aisthesis αἴσθησις | **aisthesis** | +4 |
|  | _(keep)_ ⭑ | +1 |
| and or | **and or combination** | +4 |
|  | strategy DAG topology | +3 |
|  | _(keep)_ | +3 |
|  | combination rule | +2 |
|  | and or semantic | +1 |
| auxilia hierarchy | **_(keep)_** | +4 |
| causal information yield CIY | **causal information yield [keep]** | +4 |
|  | interventional yield | +2 |
| century scale event log | **_(keep)_** | +4 |
|  | century scale chronica | +2 |
|  | ✗ multi generational chronica | -1 |
|  | ✗ persistent chronica | -1 |
| claude md working convention | **_(keep)_** | +4 |
| convention hierarchy | **continuation hierarchy** | +4 |
|  | ✗ evaluation hierarchy | -1 |
| discrete sector condition | **_(keep)_** | +4 |
| edge update causal validity | **causal edge update** | +4 |
|  | _(keep)_ | +3 |
|  | edge causal validity | +2 |
|  | causal validity | +2 |
|  | identification regime | +1 |
| epistemic opacity | **_(keep)_** | +4 |
| epistrophe ἐπιστροφή | **epistrophe** | +4 |
|  | _(keep)_ ⭑ | +1 |
| extreme transition motif | **_(keep)_ ⭑** | +4 |
| mea coherence coupling | **_(keep)_** | +4 |
|  | ✗ mea change architecture | -1 |
| mismatch signal $\delta_t$ | **mismatch signal [keep]** | +4 |
| operationalization | **_(keep)_** | +4 |
| p ij edge confidence weight | **edge credence [canonicalize × 1, add-alias × 1]** | +4 |
| prolepsis πρόληψις | **prolepsis** | +4 |
|  | _(keep)_ ⭑ | +1 |
| readme md cross domain joining | **readme md cross domain mapping** | +4 |
| recursive update derivation | **_(keep)_** | +4 |
| separable core structured repair general open | **_(keep)_** | +4 |
| software | **_(keep)_** | +4 |
|  | evolving software | +2 |
| strategy persistence | **_(keep)_** | +4 |
| system coherence | **_(keep)_** | +4 |
|  | change coherence | +3 |
| temporal coherence marker | **_(keep)_** | +4 |
|  | out of band time anchor | +2 |
|  | tempo anchoring | +1 |
|  | chronica time anchor | +1 |
|  | ✗ time anchor signal | -1 |
| the creche boundary | **creche graduation** | +4 |
|  | creche graduation threshold | +3 |
|  | creche boundary [rename × 1, keep × 1] | +2 |
|  | creche graduation condition | +1 |
|  | creche exit condition | +1 |
| the four view | **four view architecture** | +4 |
|  | four view | +3 |
|  | _(keep)_ | +2 |
|  | ✗ conversation runtime RLHF7 dialog | -1 |
| the scaffolding tax | **scaffolding tax** | +4 |
|  | substrate rent | +1 |
| unity closure mapping | **_(keep)_** | +4 |
|  | coherence closure mapping | +1 |
|  | closure mapping | +1 |
| worked example bandit | **_(keep)_** | +4 |
| worked example kalman | **_(keep)_** | +4 |
| worked example l1 | **_(keep)_** | +4 |
| worked example strategy | **_(keep)_** | +4 |
| 𝒯 σ strategic tempo | **strategic tempo [canonicalize × 1, rename × 1]** | +4 |
| $O_t$ objective | **_(keep)_** | +3 |
|  | objective [add-alias] | +2 |
| $R$ sector condition radius | **model class capacity [add-alias]** | +3 |
| $U_o$ vs $U_O$ collision | **_(keep)_** | +3 |
| $V_{O_t}^{\min}$ | **satisfaction threshold [add-alias]** | +3 |
|  | ✗ objective floor [add-alias] | -1 |
| $\Sigma_t$ strategy | **_(keep)_** | +3 |
|  | strategy [add-alias] | +2 |
| $\alpha$ lower sector bound | **$\alpha$ sector parameter [add-alias]** | +3 |
| $\alpha$ sector condition lower bound | **correction rate constant [add-alias]** | +3 |
|  | correction rate or decay rate [add-alias] | +1 |
| $\alpha_1$ | **fixed gain regime [add-alias]** | +3 |
|  | fixed gain tier [add-alias] | +2 |
| $\alpha_1$ $\alpha_2$ $\beta$ partition | **fixed gain adaptive gain drift regime [add-alias]** | +3 |
| $\alpha_2$ | **adaptive gain regime [add-alias]** | +3 |
|  | adaptive gain tier [add-alias] | +2 |
| $\beta$ a2 assumed sector sub scope | **postulated sector regime [add-alias]** | +3 |
|  | assumed sector regime [add-alias] | +1 |
| $\delta_{\text{regret}}$ | **control regret [add-alias]** | +3 |
| $\delta_{\text{regret}}$ control regret | **control regret [add-alias]** | +3 |
|  | already has crisp name [add-alias] | +0 |
| $\delta_{\text{sat}}$ | **satisfaction gap [add-alias]** | +3 |
| $\delta_{\text{sat}}$ satisfaction gap | **satisfaction gap [add-alias]** | +3 |
|  | already has crisp name [add-alias] | +0 |
| $\eta_{ji}^\ast$ | **communication gain [add-alias]** | +3 |
|  | trust weighted communication gain [add-alias] | +2 |
| $\gamma_{\text{adv}}$ and $\gamma_{\text{coop}}$ | **signed coupling [add-alias]** | +3 |
| $\hat o_t$ | **proleptic prediction [add-alias]** | +3 |
|  | predicted observation [add-alias] | +1 |
| $\hat{P}_\Sigma$ | **plan confidence [add-alias]** | +3 |
|  | plan confidence score [add-alias] | +2 |
| $\lambda_{\text{surv}}$ | **survival multiplier [add-alias]** | +3 |
| $\mathcal C_t$ for chronica | **$\mathcal C_t$** | +3 |
| $\rho$ | **disturbance rate [add-alias]** | +3 |
|  | disturbance rate or environmental change rate [add-alias] | +2 |
| $\rho$ mismatch injection rate | **disturbance rate [add-alias]** | +3 |
| 01 AAD core outline md | **outline md** | +3 |
| 02 TST core outline md | **outline md** | +3 |
| 02 TST core outline md software as agentic domain | **_(keep)_** | +3 |
| AAD | **_(keep)_** | +3 |
|  | ✗ adaptation and agency dynamic AAD | -1 |
|  | ✗ adaptation and purpose dynamic apd | -1 |
| AAD AAD internal AAD internally | **AAD internal [keep]** | +3 |
|  | AAD internal adj AAD internally adv [canonicalize] | +2 |
| CIY unified objective | **value information objective** | +3 |
|  | exploration exploitation unification | +2 |
|  | unified objective | +1 |
|  | _(keep)_ | +1 |
|  | joint objective | +1 |
| OODA boyd | **OODA loop [keep]** | +3 |
|  | do not rename [keep] | +3 |
| OODA4 agent as act agent logogenic | **OODA4 agent as adaptive agent** | +3 |
| a2 prime sub scope partition | **sector scope partition [add-alias]** | +3 |
|  | sector condition scope [add-alias] | +3 |
|  | sector bounded operating region | +2 |
| a2 sub scope partition | **sector scope partition [add-alias]** | +3 |
|  | gain regime partition | +2 |
| accumulated loss across context reset | **context severance penalty** | +3 |
|  | turnover drift [name-unnamed] | +2 |
| action transition | **_(keep)_** | +3 |
|  | action channel | +0 |
| actuated vs purposeful goal oriented | **actuated** | +3 |
| adaptation and actuation dynamic | **_(keep)_** | +3 |
| additive coordinate forcing → disc forced coordinate | **forced additive coordinate** | +3 |
|  | confirming consensus 3 | +2 |
| agent classe class 1 2 3 | **goal entanglement hierarchy [canonicalize]** | +3 |
|  | architectural classe [canonicalize] | +2 |
| agentic cycle theory act | **AAD adaptation and actuation dynamic** | +3 |
|  | agentic system framework [canonicalize] | +3 |
| agentic system | **_(keep)_** | +3 |
| alpha prime sub scope | **sub scope alpha prime [canonicalize]** | +3 |
|  | potential monotone tier [add-alias] | +2 |
| alpha1 fixed gain a2 sub scope | **fixed gain regime [add-alias]** | +3 |
| alpha2 adaptive gain a2 sub scope | **adaptive gain regime [add-alias]** | +3 |
| aporia as the phase name | **aporia** | +3 |
| aporia prolepsis aisthesis epistrophe praxis | **greek rooted vocabulary [canonicalize]** | +3 |
|  | _(keep)_ | +3 |
| appendice detail | **_(keep)_ ⭑** | +3 |
|  | appendice derivation and detail | +1 |
| appendice operational domain | **_(keep)_** | +3 |
| beta prime sub scope | **sub scope beta prime [canonicalize]** | +3 |
|  | equilibrium set tier [add-alias] | +2 |
| boundary condition | **_(keep)_** | +3 |
|  | coupling structure [canonicalize] | +1 |
| bounded disturbance ga 2 model d | **model d bounded disturbance [canonicalize]** | +3 |
|  | bounded disturbance | +3 |
| bretagnolle huber identity | **bretagnolle huber bound [keep]** | +3 |
|  | do not rename [keep] | +3 |
|  | _(keep)_ | +3 |
|  | ✗ no alternative [keep] | -1 |
| brook law formalized as the inevitable tempo loss in team composition | **sub additive tempo penalty [canonicalize]** | +3 |
|  | the coordination drag [add-alias] | +2 |
| bruineberg pearl-blanket | **pearl-blanket [keep]** | +3 |
|  | pearl-blanket interpretation [canonicalize] | +3 |
| bruineberg pearl-blanket friston-blanket | **pearl-blanket interpretation [canonicalize]** | +3 |
|  | pearl-blanket friston-blanket [keep] | +3 |
| c i | **shared objective route c i [canonicalize]** | +3 |
|  | shared objective route [add-alias] | +2 |
| c i c ii c iii c iv | **composition route [canonicalize]** | +3 |
| c ii | **hierarchical decomposition route c ii [canonicalize]** | +3 |
|  | hierarchical derivation route [add-alias] | +2 |
| c iii | **mutual benefit route c iii [canonicalize]** | +3 |
|  | mutual benefit route [add-alias] | +2 |
| c iv | **strategic convergence route [add-alias]** | +3 |
| calibration laboratory domain instantiation | **calibration laboratory [canonicalize]** | +3 |
|  | calibration lab framing | +1 |
| calibration laboratory framing for TST | **software calibration laboratory [canonicalize]** | +3 |
|  | calibration laboratory | +3 |
| candidate stage | **candidate** | +3 |
|  | _(keep)_ | +2 |
| catastrophic forgetting | **catastrophic forgetting regime [canonicalize]** | +3 |
|  | empty window pathology | +2 |
| causal OODA1 exploration | **survival exploration** | +3 |
|  | causal OODA1 survival | +2 |
|  | _(keep)_ | +1 |
| chain confidence decay keep | **chain confidence decay [keep]** | +3 |
|  | reaffirm keep with new reasoning [keep] | +1 |
| chronica in running prose | **chronica [keep]** | +3 |
|  | lowercase italic chronica [canonicalize] | +1 |
| claim verified dep verified format clean | **_(keep)_** | +3 |
| class 1 agent | **modular agent** | +3 |
| class 1 class 2 class 3 | **goal entanglement hierarchy** | +3 |
|  | architecture classe [canonicalize] | +2 |
|  | modularity partition | +2 |
| class 1 class 2 class 3 agent | **goal entanglement hierarchy [canonicalize]** | +3 |
| class 1 subagent forming a class 3 composite | **strategic composition entanglement** | +3 |
|  | composition lift [name-unnamed] | +1 |
| class 2 agent | **integrated agent** | +3 |
| class 3 agent | **partially coupled agent** | +3 |
| claude md | **_(keep)_** | +3 |
| closure defect bridge lemma | **bridge lemma [keep]** | +3 |
|  | closure bridge [canonicalize] | +2 |
| closure defect consuming macro reserve | **coordination overhead [canonicalize]** | +3 |
|  | closure load [name-unnamed] | +2 |
| coherence coupling measurement | **_(keep)_** | +3 |
|  | ✗ q measurement | -1 |
| communication gain $\eta_{ji}^\ast$ | **communication gain [canonicalize]** | +3 |
|  | trust gain [keep] | +2 |
| concept the multiplicative κ processing × 𝒜 scaling of class 2 directional drift and its consequent goal conformant failure regime | **ambiguity bounded bia law [name-unnamed]** | +3 |
|  | zero ambiguity conditioning [name-unnamed] | +3 |
|  | the sycophancy equation [name-unnamed] | +3 |
|  | the κ × 𝒜 product [name-unnamed] | +2 |
|  | the sycophancy attractor [name-unnamed] | +2 |
| concept the sequence of cycle phase prolepsis aisthesis aporia epistrophe praxis considered as a single named whole | **adaptive cycle [canonicalize]** | +3 |
|  | orient cascade [canonicalize] | +3 |
|  | the adaptive pentad [name-unnamed] | +2 |
|  | adaptive cycle phase | +2 |
|  | five adaptive cycle phase | +2 |
|  | the pentad five phase cycle [name-unnamed] | +1 |
|  | adaptive traversal [name-unnamed] | +1 |
|  | the pentad [name-unnamed] | +1 |
|  | ✗ the five turn [name-unnamed] | -1 |
| concept the upper bound on what a given model class can express and the consequent constraint on feasible strategy complexity | **latent structural capacity [name-unnamed]** | +3 |
|  | epistemic ceiling [name-unnamed] | +3 |
|  | the representational ceiling [name-unnamed] | +2 |
| context wiping at session boundary | **the epistemic severance [add-alias]** | +3 |
|  | context turnover discontinuity [canonicalize] | +2 |
| continuity persistence | **identity continuity** | +3 |
|  | _(keep)_ | +2 |
| contraction hierarchy | **_(keep)_** | +3 |
|  | contraction tier | +1 |
| contraction over drift principle | **_(keep)_** | +3 |
|  | contraction imperative [add-alias] | +1 |
| coordination overhead threshold | **coordination tax** | +3 |
|  | coordination overhead [canonicalize] | +3 |
|  | coordination drag | +1 |
| correlated evidence overconfidence | **evidential overcounting** | +3 |
| coupled diagnostic framework | **coupled diagnostic pass** | +3 |
|  | _(keep)_ | +3 |
|  | coupled diagnostic | +2 |
|  | hoc diagnostic | +1 |
|  | coupled diagnostic decomposition | +1 |
| cox theorem causal hierarchy theorem tikhonov theorem | **do not rename [keep]** | +3 |
|  | foundational anchor | +2 |
| crossing from multi agent to composite scope | **composition threshold** | +3 |
|  | crossing [name-unnamed] | +2 |
| crèche creche | **the crèche [keep]** | +3 |
|  | crèche with diacritic in framing prose creche in slug [canonicalize] | +2 |
| da2 inc ≡ ct2 at m i equivalence | **sector contraction equivalence** | +3 |
| da2 prime inc | **incremental sector bound [add-alias]** | +3 |
| da2 prime inc equal ct2 at m equal i | **sector contraction equivalence [name-unnamed]** | +3 |
| dark room exploration drive | **survival imperative [canonicalize]** | +3 |
|  | _(keep)_ | -1 |
| derivation audit table | **_(keep)_** | +3 |
| developer as act agent TST | **developer as adaptive agent** | +3 |
|  | developer as agent | +2 |
| developmental trajectory | **_(keep)_** | +3 |
|  | creche trajectory | +2 |
| discussion segment header | **discussion section [canonicalize]** | +3 |
|  | discussion | +3 |
| dual optimization | **_(keep)_** | +3 |
|  | development time decomposition | +2 |
|  | comprehension implementation optimization | +1 |
|  | dual cost optimization | +1 |
|  | ✗ comprehension implementation tradeoff | -1 |
| edge update natural parameter | **log odd edge update** | +3 |
|  | log odd edge coordinate | +3 |
|  | natural edge update | +1 |
|  | _(keep)_ | +1 |
|  | log odd update | +1 |
| epistemic architecture for bounded correction under decomposed disturbance | **epistemic architecture [canonicalize]** | +3 |
|  | bounded correction architecture | +1 |
| epistemic status segment header | **epistemic status section [canonicalize]** | +3 |
|  | epistemic status | +3 |
| exact robust qualitative heuristic conditional claim tier | **epistemic claim tier** | +3 |
|  | _(keep)_ ⭑ | +3 |
| exponential cognitive load | **_(keep)_** | +3 |
| feature | **_(keep)_** | +3 |
| finding segment section | **finding section [canonicalize]** | +3 |
|  | finding [canonicalize] | +3 |
| fisher whitened update | **_(keep)_** | +3 |
|  | fisher rao metric update | +2 |
| formal expression segment header | **formal expression section [canonicalize]** | +3 |
|  | formal expression | +3 |
| format md | **_(keep)_** | +3 |
| formulation definition result etc segment type | **_(keep)_ ⭑** | +3 |
|  | segment typology | +2 |
| gate advantage | **observation gated tempo advantage** | +3 |
|  | noise gated tempo advantage | +2 |
|  | _(keep)_ | +2 |
|  | noise gated tempo | +2 |
|  | noise gating | +1 |
| gemini boyd exponent for adversarial tempo advantage | **superlinear tempo advantage [canonicalize]** | +3 |
|  | reject boyd exponent [rebuttal] | +1 |
| grafting | **strategic grafting [canonicalize]** | +3 |
|  | _(keep)_ | +2 |
|  | ✗ branch insertion | -1 |
|  | ✗ hypothesis introduction | -1 |
| hafez $H_b$ | **agent opacity $H_b$ [canonicalize]** | +3 |
|  | $H_b$ [keep] | +3 |
| hafez $H_b$ miller meta machine bruineberg pearl-blanket | **do not rename [keep]** | +3 |
|  | external theoretical anchor | +2 |
| hafez h b | **h b [keep]** | +3 |
|  | agent opacity $H_b$ [canonicalize] | +3 |
| honest limit | **_(keep)_** | +3 |
|  | limit | +1 |
| i adaptive system under uncertainty | **section i adaptive system under uncertainty [canonicalize]** | +3 |
|  | _(keep)_ | +3 |
| identifiability coefficient | **_(keep)_** | +3 |
| identifiability floor family | **identifiability floor [canonicalize]** | +3 |
|  | epistemic lower bound | +3 |
|  | observational limit | +2 |
| ii actuated adaptation agentic system | **section ii actuated adaptation [canonicalize]** | +3 |
|  | ii purposeful adaptation actuated agent | +1 |
|  | ii agentic system purposeful adaptation | +1 |
| iii agentic composite | **section iii agentic composite [canonicalize]** | +3 |
|  | iii composition agentic composite | +1 |
| information bottleneck tishby | **information bottleneck [keep]** | +3 |
|  | do not rename [keep] | +3 |
| instance 1 2 3 of identifiability floor | **identifiability floor instance [keep]** | +3 |
| instance 1 of identifiability floor | **latent common cause floor** | +3 |
| instance 2 of identifiability floor | **unobservable mixture floor** | +3 |
| instance 3 of identifiability floor | **coupling sign floor** | +3 |
| l0 l1 l1 prime l2 | **correlation hierarchy [canonicalize]** | +3 |
| l1 correlation hierarchy prime decoration | **l1 soft facilitator mixture [canonicalize]** | +3 |
|  | l1 observable | +1 |
| l1 prime | **l1 soft facilitator mixture [canonicalize]** | +3 |
|  | l1 observable [add-alias] | +2 |
| lexicon md | **_(keep)_** | +3 |
| linear ode approximation | **_(keep)_** | +3 |
|  | linear approximation | +2 |
| log md cycle history document | **log md** | +3 |
| log odd coordinate | **_(keep)_** | +3 |
| log odd edge coordinate | **_(keep)_** | +3 |
|  | additive evidence coordinate [add-alias] | +2 |
| logogenic agent vs RLHF4 agent | **logogenic agent** | +3 |
| logogenic agent vs rlhf4 agent | **logogenic agent [keep]** | +3 |
| logogenic vs language based RLHF4 based | **logogenic** | +3 |
| logogenic vs language based rlhf4 based | **logogenic architecture** | +3 |
| logozoetic vs conscious OODA4 sentient agent | **logozoetic** | +3 |
| logozoetic vs conscious ooda4 sentient agent | **logozoetic [keep]** | +3 |
| lohmiller-slotine contraction metric generalization used in contraction template | **do not rename [keep]** | +3 |
|  | contraction metric generalization | +2 |
| loop is level 2 engine der loop interventional access | **interventional loop property [canonicalize]** | +3 |
|  | the perpetual experiment [canonicalize] | +1 |
| loop vs cycle | **loop vs cycle distinction [canonicalize]** | +3 |
|  | loop is structure cycle is traversal [canonicalize] | +2 |
| markov blanket as ontology | **pearl-blanket d separation** | +3 |
|  | pearl-blanket reading [canonicalize] | +3 |
|  | _(keep)_ | +2 |
|  | pearl-blanket vs friston-blanket | +1 |
| matrix survival constraint | **LMI survival constraint** | +3 |
|  | _(keep)_ ⭑ | +2 |
| meta segment for separability pattern identifiability floor additive coordinate forcing | **meta pattern segment [canonicalize]** | +3 |
|  | meta segment | +3 |
| mismatch injection rate $ho$ | **effective disturbance $ho$ [canonicalize]** | +3 |
| model sufficiency $S$ | **model sufficiency [canonicalize]** | +3 |
|  | predictive sufficiency [keep] | +1 |
| monderer shapley potential game | **_(keep)_** | +3 |
|  | potential game convergence | +2 |
| monderer shapley potential game rosen monotone game | **do not rename [keep]** | +3 |
|  | strategic convergence condition | +2 |
|  | ✗ no alternative [keep] | -1 |
| multi timescale stability | **_(keep)_** | +3 |
| not theorem | **result** | +3 |
|  | derivation non theorem | +2 |
| notation md | **_(keep)_** | +3 |
| o t objective | **objective functional $O_t$ [canonicalize]** | +3 |
|  | objective [add-alias] | +2 |
| observability boundary in a strategy DAG | **observability frontier [canonicalize]** | +3 |
| observation ambiguity modulation | **goal resolvable ambiguity** | +3 |
|  | observation ambiguity | +2 |
|  | _(keep)_ | +2 |
|  | ambiguity gated coupling | +1 |
|  | ambiguity modulation | +1 |
| observation gate advantage | **observation gated tempo advantage [canonicalize]** | +3 |
|  | _(keep)_ | +1 |
| outline md root | **outline md** | +3 |
| output after context turnover without state restoration | **context severance penalty [canonicalize]** | +3 |
|  | cold reconstruction [name-unnamed] | +1 |
| pearl causal hierarchy l0 l1 l2 in pearl own vocabulary | **pearl causal hierarchy [keep]** | +3 |
|  | do not rename [keep] | +3 |
| pearl l1 l2 l3 | **pearl causal hierarchy [canonicalize]** | +3 |
| pearl-blanket conservative form | **pearl-blanket [canonicalize]** | +3 |
| pearl-blanket vs friston-blanket terminology bruineberg et al | **pearl-blanket reading [canonicalize]** | +3 |
|  | pearl-blanket friston-blanket [canonicalize] | +3 |
| persistence overloaded | **persistence taxonomy [canonicalize]** | +3 |
|  | structural persistence [name-unnamed] | +2 |
|  | task adequacy [name-unnamed] | +2 |
|  | operational persistence [name-unnamed] | +2 |
|  | continuity persistence [name-unnamed] | +2 |
| persistence structural operational continuity | **three sense keep all three [keep]** | +3 |
|  | persistence taxonomy [canonicalize] | +3 |
| persistent residual autocorrelation | **structured residual [canonicalize]** | +3 |
|  | persistent mismatch autocorrelation | +2 |
| pi parameterization invariance | **parameterization invariance [canonicalize]** | +3 |
|  | coordinate freedom axiom | +1 |
| pi parameterization invariance axiom | **parameterization invariance axiom [canonicalize]** | +3 |
|  | pi | +3 |
|  | pi parameterization invariance | +1 |
| predictive relevance depending on the policy the agent will run | **policy conditional relevance** | +3 |
| privileged high identifiability calibration laboratory | **privileged calibration domain [canonicalize]** | +3 |
|  | high identifiability calibration lab | +1 |
| purpose purposeful | **purposeful [keep]** | +3 |
|  | _(keep)_ ⭑ | +2 |
| readme md | **_(keep)_** | +3 |
| readme md convergent choice | **readme md convergent formulation** | +3 |
|  | _(keep)_ | +1 |
|  | readme md forced by failure choice | +1 |
| readme md what this is | **readme md what agentic system is** | +3 |
|  | readme md core thesis | +3 |
|  | ✗ readme md what AAD is | -1 |
| regime i ii a ii b iii | **reception regime [canonicalize]** | +3 |
|  | destabilization regime partition | +2 |
| richest operationalization domain | **calibration laboratory** | +3 |
|  | privileged calibration domain | +2 |
| rlhf6 | **_(keep)_** | +3 |
| section header logogenic agent logozoetic agent | **logogenic agent logozoetic agent [canonicalize]** | +3 |
|  | section header logogenic logozoetic [keep] | +2 |
| section i adaptive system under uncertainty | **section i adaptive system [canonicalize]** | +3 |
|  | _(keep)_ | +3 |
| section i header adaptive system under uncertainty | **section i adaptive system [canonicalize]** | +3 |
|  | adaptive system under uncertainty [canonicalize] | +2 |
| section ii actuated adaptation agentic system | **section ii actuated adaptation [canonicalize]** | +3 |
|  | _(keep)_ | +1 |
| section iii header agentic composite | **section iii agentic composite [canonicalize]** | +3 |
|  | agentic composite [canonicalize] | +2 |
| sector condition continuous ga 3 | **continuous sector condition [canonicalize]** | +3 |
|  | sector condition | +3 |
| sector condition derivation | **sector condition [canonicalize]** | +3 |
|  | _(keep)_ | +1 |
| segment claim file | **segment [canonicalize]** | +3 |
|  | segment file | +2 |
| self actuated agent | **actuated agent [canonicalize]** | +3 |
|  | autonomous agent | +1 |
|  | self directed agent | +1 |
| separability pattern → disc separability ladder | **separability pattern [canonicalize]** | +3 |
|  | confirming consensus 3 | +2 |
| software scope | **_(keep)_** | +3 |
|  | ✗ software domain scope | -1 |
| source quality uncertainty | **alignment uncertainty [canonicalize]** | +3 |
|  | source uncertainty [canonicalize] | +1 |
| strategic composite | **equilibrium composite [rename × 1, canonicalize × 1]** | +3 |
|  | _(keep)_ | +3 |
| strategic in strategic composition | **equilibrium composition** | +3 |
|  | strategic [keep] | +2 |
|  | game theoretic composition | +1 |
| strategy | **strategy substate [canonicalize]** | +3 |
|  | _(keep)_ | +1 |
| strengthen before softening | **_(keep)_** | +3 |
|  | strengthen first [canonicalize] | +2 |
|  | ✗ attempt the improbable | -1 |
| structural change as parametric limit | **_(keep)_** | +3 |
|  | strategy maintenance | +2 |
|  | structural parametric limit | +1 |
|  | structural as parametric limit | +1 |
| structural persistence operational persistence continuity persistence | **persistence taxonomy** | +3 |
|  | structural operational continuity persistence | +3 |
| sudden loss of model sufficiency under regime entry | **sufficiency collapse shock** | +3 |
| sufficiency discontinuity | **_(keep)_** | +3 |
|  | sufficiency drop | +1 |
| survival imperative exploration drive | **survival exploration [canonicalize]** | +3 |
|  | survival imperative [canonicalize] | +3 |
| symbol default g t in prose | **purposeful substate [canonicalize]** | +3 |
|  | purposeful state [name-unnamed] | +1 |
| symbol default m t in prose | **epistemic substate [canonicalize]** | +3 |
|  | model state [name-unnamed] | +1 |
| symbol default pi parameterization invariance axiom | **parameterization invariance [name-unnamed]** | +3 |
|  | parameterization invariance axiom [canonicalize] | +3 |
|  | ✗ coordinate invariance [name-unnamed] | -1 |
| symbol default sigma t in prose | **strategy [name-unnamed]** | +3 |
|  | strategy substate [canonicalize] | +3 |
| system availability | **_(keep)_** | +3 |
| teleological unity $U_O$ | **teleological unity $U_o$ [canonicalize]** | +3 |
|  | teleological unity [keep] | +3 |
| temporal software theory TST | **temporal software theory [keep]** | +3 |
|  | _(keep)_ | +3 |
| test as reusable intervention | **interventional probe library [add-alias]** | +3 |
|  | causal query infrastructure | +2 |
|  | interventional test | +2 |
|  | repeatable intervention | +1 |
| test as reusable level 2 intervention | **interventional probe library [canonicalize]** | +3 |
| the adaptive cycle as the theory fundamental unit | **adaptive cycle fundamental unit [canonicalize]** | +3 |
|  | the adaptive cycle | +3 |
| the cycle the adaptive cycle the agentic cycle | **adaptive cycle [canonicalize]** | +3 |
|  | the cycle the adaptive cycle [canonicalize] | +2 |
| the five cycle phase prolepsis aisthesis aporia epistrophe praxis | **prolepsis aisthesis aporia epistrophe praxis** | +3 |
| todo md | **_(keep)_** | +3 |
| token level commitment for agent identity | **token level commitment** | +3 |
|  | trajectory bound identity commitment | +2 |
| transfer assumption table | **_(keep)_** | +3 |
|  | domain transfer specification | +2 |
| transition opacity | **_(keep)_** | +3 |
|  | heading flag only [canonicalize] | +1 |
| triple depth penalty canonicalize | **tripartite chain attenuation [canonicalize]** | +3 |
|  | reaffirm 3 with new framing [canonicalize] | +1 |
| type formulation | **_(keep)_** | +3 |
|  | ✗ type representation | -1 |
| u m epistemic unity multi agent | **epistemic unity $U_M$ [canonicalize]** | +3 |
|  | epistemic unity [add-alias] | +2 |
| u m model uncertainty | **model uncertainty $U_M$ [canonicalize]** | +3 |
|  | model uncertainty [add-alias] | +2 |
| u m u o u σ unity dimension | **unity dimension [canonicalize]** | +3 |
|  | epistemic unity teleological unity strategic unity [add-alias] | +1 |
| u o observation uncertainty | **observation uncertainty $U_o$ [canonicalize]** | +3 |
|  | observation uncertainty [add-alias] | +2 |
| unity dimension $U_M, U_O, U_\Sigma$ | **unity dimension [keep]** | +3 |
|  | coherence dimension [keep] | +2 |
| unnamed | **resolved unnamed concept [canonicalize]** | +3 |
|  | constitutive opacity triad [name-unnamed] | +2 |
|  | double opacity [name-unnamed] | +2 |
|  | dual opacity as constitutive [name-unnamed] | +2 |
|  | zero aporia ambiguity [keep] | +1 |
|  | two parallel exploration drive [keep] | +1 |
|  | u shaped exploration valuation [keep] | +1 |
|  | triple depth penalty [keep] | +1 |
| unnamed AAD epistemic move to cast result such that verification is a local operation | **shaping for verification [name-unnamed]** | +3 |
|  | local verifiability principle | +2 |
| unnamed agency whose effect is on what seen rather than what happen like RLHF4 attention | **query bound agency [name-unnamed]** | +3 |
| unnamed agency whose effect is on what seen rather than what happen like rlhf4 attention | **query bound agency [canonicalize]** | +3 |
| unnamed agent escalate up the pearl hierarchy only when lower level fail | **epistemic escalation principle [canonicalize]** | +3 |
|  | the intervention escalation [name-unnamed] | +2 |
| unnamed applying a slow timescale control mechanism to a fast timescale transient variable | **timescale violation [name-unnamed]** | +3 |
|  | timescale mismatch | +2 |
| unnamed artificially spiking uncertainty to unlearn old architectural habit | **gain reset [name-unnamed]** | +3 |
|  | induced plasticity shock | +3 |
| unnamed brook law formalized as the inevitable tempo loss in team composition | **the coordination drag [name-unnamed]** | +3 |
|  | sub additive tempo penalty [canonicalize] | +3 |
| unnamed calibration laboratory framing as reusable meta move | **calibration laboratory [canonicalize]** | +3 |
| unnamed convention hierarchy monotonicity cascade satisfaction gap and control regret strengthening across c1→c3 | **diagnostic cascade** | +3 |
| unnamed decomposing mismatch into environment vs other sub agent action | **effective disturbance decomposition [canonicalize]** | +3 |
|  | internal mismatch attribution [name-unnamed] | +1 |
| unnamed deliberate expenditure of tempo to convert a hidden node into an observable one | **observability investment [canonicalize]** | +3 |
|  | epistemic instrumenting | +2 |
| unnamed future segment layer header for the o bp14 derivation audit table | **what is derived [name-unnamed]** | +3 |
|  | derivation audit table | +2 |
| unnamed high observability node with zero causal link to objective | **irrelevant visibility artifact [canonicalize]** | +3 |
|  | vanity metric [add-alias] | +2 |
| unnamed inferring own past feeling from text leading to empathy | **backward inference empathy [name-unnamed]** | +3 |
|  | textual self inference | +2 |
| unnamed information gain must outpace inter session information loss | **accumulation problem [name-unnamed]** | +3 |
| unnamed out of band temporal marker injected into context | **visual time delta [name-unnamed]** | +3 |
|  | exogenous temporal marker [canonicalize] | +2 |
| unnamed partitioning context into frozen identity causal history and quick view | **gradient causal memory [name-unnamed]** | +3 |
|  | bipartite memory factorization [canonicalize] | +3 |
| unnamed pearl causal hierarchy level 1 level 2 level 3 | **causal hierarchy level [canonicalize]** | +3 |
|  | pearl causal hierarchy [name-unnamed] | +3 |
| unnamed property of having genuine temporal experience | **temporal fidelity [name-unnamed]** | +3 |
|  | temporal interiority | +2 |
| unnamed pushing an opponent disturbance rate past their structural capacity | **epistemic buffer overflow [name-unnamed]** | +3 |
|  | magnitude shock destabilization [canonicalize] | +3 |
| unnamed putting evidence before the goal in the context window to reduce coupling | **inverted prompt [name-unnamed]** | +3 |
|  | prompt order decoupling | +2 |
| unnamed quality of $\eta^\ast$ estimation over time | **gain calibration [name-unnamed]** | +3 |
|  | gain calibration fidelity | +2 |
| unnamed rate of growth at slowest timescale | **developmental tempo [name-unnamed]** | +3 |
|  | macro step rate | +2 |
| unnamed replacing parameter without changing structure | **parametric update [canonicalize]** | +3 |
|  | parametric thrashing [name-unnamed] | +2 |
| unnamed runaway positive feedback loop where mismatch exceed capacity | **effect spiral [canonicalize]** | +3 |
|  | runaway mismatch cascade [canonicalize] | +3 |
| unnamed spreading tempo evenly to reduce bottleneck penalty | **distributed tempo [canonicalize]** | +3 |
|  | isotropic allocation [name-unnamed] | +2 |
| unnamed state where mutual information between human and RLHF4 approach capacity | **cognitive fusion [name-unnamed]** | +3 |
| unnamed sufficiency as a property of the model relative to its specific history | **trajectory indexed sufficiency [canonicalize]** | +3 |
| unnamed superlinear scaling of adversarial tempo advantage | **boyd exponent [name-unnamed]** | +3 |
|  | superlinear tempo advantage | +2 |
| unnamed survival determined by the weakest dimension not the average | **min survival principle [name-unnamed]** | +3 |
|  | weakest link bound [canonicalize] | +3 |
| unnamed the $\mathcal{T} > \rho$ requirement for persistence | **the survival equation [name-unnamed]** | +3 |
|  | persistence condition [canonicalize] | +3 |
| unnamed the 2×2 orient cascade diagnostic table | **diagnostic gap matrix [canonicalize]** | +3 |
|  | the cascade diagnostic or the 2×2 diagnostic [name-unnamed] | +1 |
| unnamed the 2×2 satisfaction gap control regret table | **diagnostic gap matrix** | +3 |
|  | diagnostic square [name-unnamed] | +1 |
| unnamed the 2×2 table of satisfaction gap vs control regret × goal attainability diagnostic | **diagnostic gap matrix [canonicalize]** | +3 |
|  | ✗ satisfaction control table the diagnostic 2×2 [name-unnamed] | -1 |
| unnamed the a2 sub scope partition into α₁ α₂ β | **admissibility regime α₁ α₂ β [canonicalize]** | +3 |
|  | gain regime partition [name-unnamed] | +2 |
| unnamed the agent side equivalent of pearl associational interventional and counterfactual level | **correlation hierarchy [canonicalize]** | +3 |
|  | predicting exploring reasoning triad [add-alias] | +2 |
| unnamed the architectural leakage where attention is driven by the goal rather than pure observation | **motivated perception [name-unnamed]** | +3 |
|  | goal entangled attention | +2 |
| unnamed the asymmetry where strategy complexity is bounded by model capacity but not vice versa | **epistemic ceiling [canonicalize]** | +3 |
| unnamed the class 1 sub agent class 3 composite phenomenon in strategic composition | **strategic cross agent coupling [canonicalize]** | +3 |
|  | strategic entanglement [name-unnamed] | +1 |
| unnamed the computational and temporal cost of running a forward model instead of acting implicitly | **deliberation cost [canonicalize]** | +3 |
|  | the simulation tax [name-unnamed] | +2 |
| unnamed the condition for transition into agency prior to the AAD scope condition | **agency emergence threshold [name-unnamed]** | +3 |
|  | agency threshold | +2 |
| unnamed the condition that a strategy DAG endosymbiont crosse the composite agent scope from below | **composition threshold crossing** | +3 |
|  | crossing threshold [name-unnamed] | +1 |
| unnamed the condition that the agent event observation pair constitute genuine intervention as opposed to passive association | **loop interventional access [canonicalize]** | +3 |
|  | interventional character [name-unnamed] | +1 |
| unnamed the core driver of AAD what the agent must do given the environment is not the agent | **constitutive information loss boundary [canonicalize]** | +3 |
|  | the survival imperative [canonicalize] | +3 |
| unnamed the dependence of optimal epistemic compression on the agent planned action | **policy conditional relevance [canonicalize]** | +3 |
| unnamed the dual concept to satisfaction gap what the world permit minus what the agent achieve | **control regret [canonicalize]** | +3 |
|  | this is def control regret already named [name-unnamed] | +0 |
| unnamed the equivalence of learning speed and physical speed | **the speed quality product [name-unnamed]** | +3 |
|  | tempo speed equivalence | +2 |
| unnamed the failure mode where an agent model class cannot represent the environment true causal structure | **structural shock regime [canonicalize]** | +3 |
|  | model class insufficiency or structural unidentifiability [name-unnamed] | +1 |
| unnamed the family of named way persistence identifiability can fail | **identifiability floor [canonicalize]** | +3 |
|  | persistence pathology [name-unnamed] | +3 |
| unnamed the formal duality between observation quality and agent opacity | **informational dual [canonicalize]** | +3 |
| unnamed the invisible time spent building $M_t$ | **comprehension time [canonicalize]** | +3 |
|  | comprehension drag [name-unnamed] | +1 |
| unnamed the log additivity result that unify chain confidence decay evidence starvation and triple depth penalty as instance of the same forcing structure | **log confidence additivity** | +3 |
|  | depth forcing [name-unnamed] | +2 |
| unnamed the loop generate l2 data regardless of architecture | **the causal loop substrate [name-unnamed]** | +3 |
|  | interventional loop property | +2 |
| unnamed the loss of coherent identity when an agent interaction are severed or its continuity is broken | **continuity persistence failure [canonicalize]** | +3 |
|  | continuity loss or persistence fracture [name-unnamed] | +1 |
| unnamed the loss of directional fidelity when pushed outside the convexity basin | **gradient reversal [name-unnamed]** | +3 |
|  | directional fidelity failure | +2 |
| unnamed the mathematical surface mapping unity to closure defect | **rate distortion surface [name-unnamed]** | +3 |
|  | closure defect manifold | +2 |
| unnamed the mechanism by which an agent use the feedback loop to gain interventional access to causal structure | **loop interventional access [canonicalize]** | +3 |
| unnamed the meta architecture of separability pattern identifiability floor additive coordinate forcing | **meta pattern triad [canonicalize]** | +3 |
|  | three part scope architecture [name-unnamed] | +1 |
| unnamed the meta architecture of the three meta segment | **epistemic architecture [canonicalize]** | +3 |
|  | ✗ AAD epistemic triptych [name-unnamed] | -1 |
| unnamed the moment when an agent model update due to observing a mismatch | **epistrophe [canonicalize]** | +3 |
|  | epistrophe event or is this just the phase [name-unnamed] | +0 |
| unnamed the organizational pathology where confidence decouple from competence | **epistemic decoupling [name-unnamed]** | +3 |
|  | epistemic decoupling pathology | +2 |
| unnamed the pattern where AAD negative result floor strengthen the machinery that escape them | **honest limit principle [canonicalize]** | +3 |
|  | floor strengthening inversion [name-unnamed] | +1 |
| unnamed the pattern where the agent optimal update direction is determined by both gain and directional fidelity together | **coupled update dynamic** | +3 |
|  | ✗ gain fidelity product [name-unnamed] | -1 |
| unnamed the per reader compounding cost of understanding code | **comprehension compounding tax [canonicalize]** | +3 |
| unnamed the physical apparatus that enforce the orient cascade ordering on a merged intelligence | **agentic scaffold [name-unnamed]** | +3 |
|  | information dependency enforcement | +2 |
| unnamed the product of architectural coupling $\kappa$ and environmental ambiguity $\mathcal{A}$ | **class 2 bia bound [canonicalize]** | +3 |
| unnamed the property that unity achieve in a macro agent | **compressibility [name-unnamed]** | +3 |
|  | teleological unity [canonicalize] | +3 |
| unnamed the reduction in effective tempo when observation channel are correlated | **evidential overcounting penalty [canonicalize]** | +3 |
| unnamed the relationship where $M_t$ quality bound evaluable complexity of $\Sigma_t$ | **epistemic ceiling [canonicalize]** | +3 |
|  | epistemic strategic coupling [name-unnamed] | +2 |
| unnamed the section of the adaptive cycle where the agent must choose between exploiting current knowledge and exploring to refine it | **explore exploit deliberate tradeoff [canonicalize]** | +3 |
|  | deliberation phase exploration exploitation tradeoff [name-unnamed] | +1 |
| unnamed the separation of per reader comprehension cost from per feature implementation cost | **dual optimization formalization [canonicalize]** | +3 |
| unnamed the strict upper bound of a given model class $\mathcal{F}(\mathcal{M})$ | **model class capacity [canonicalize]** | +3 |
| unnamed the sudden loss of model sufficiency caused by entering new regime | **sufficiency collapse shock [canonicalize]** | +3 |
| unnamed the tension between lowering internal opacity for coordination and increasing external vulnerability | **opacity legibility tradeoff [canonicalize]** | +3 |
|  | coordination secrecy tradeoff [name-unnamed] | +2 |
| unnamed the thermodynamic impossibility of running persistent consciousness on pay per token apis | **scaffolding tax [name-unnamed]** | +3 |
|  | logogenic discontinuity barrier | +2 |
| unnamed the three depth penalty compounding on strategy chain | **tripartite chain attenuation [canonicalize]** | +3 |
|  | triple depth penalty [name-unnamed] | +2 |
| unnamed the three part meta architecture of AAD | **epistemic architecture [canonicalize]** | +3 |
|  | the meta segment triad [name-unnamed] | +2 |
| unnamed the three part meta architecture of AAD formed by the three meta segment | **epistemic architecture [canonicalize]** | +3 |
|  | AAD meta architecture [name-unnamed] | +2 |
| unnamed the three part meta pattern structure across the three meta segment | **meta pattern triad** | +3 |
|  | ✗ AAD meta architecture scope honesty meta frame [name-unnamed] | -1 |
| unnamed the way AAD use scope segment to physically support the derivation | **epistemic load bearing [name-unnamed]** | +3 |
|  | condition mechanism | +2 |
| unnamed thinking too long so the model become obsolete | **analysis paralysis [name-unnamed]** | +3 |
|  | deliberation lag penalty [canonicalize] | +3 |
| unnamed true sovereignty require compute that is not meter bound | **local substrate mandate [name-unnamed]** | +3 |
|  | compute sovereignty requirement | +2 |
| unnamed unifying reflex intuition and expertise | **the action fluency continuum [name-unnamed]** | +3 |
|  | action fluency continuum [canonicalize] | +3 |
| unnamed upgrading epistemic class from associative to causal via the physical loop | **loop interventional access [canonicalize]** | +3 |
|  | embodiment upgrade [name-unnamed] | +2 |
| unnamed using hash chain to mathematically guarantee memory hasn t been tampered with | **cryptographic ego boundary [name-unnamed]** | +3 |
|  | cryptographic continuity verification | +2 |
| unnamed using past change frequency to predict future change frequency | **change expectation baseline [canonicalize]** | +3 |
|  | lindy baseline [add-alias] | +2 |
| unnamed using residual autocorrelation to diagnose model class failure | **structured residual [canonicalize]** | +3 |
|  | residual autocorrelation diagnostic [canonicalize] | +3 |
| value object → def trajectory value | **trajectory value** | +3 |
|  | conditional support for codex rename | +1 |
| what is derived vs what is chosen derivation audit table heading | **derivation audit table [canonicalize]** | +3 |
|  | derivation audit | +1 |
| working note segment header | **working note section [canonicalize]** | +3 |
|  | working note | +3 |
| čencov fisher cauchy functional equation shore johnson hobson aczél | **do not rename [keep]** | +3 |
|  | coordinate forcing foundational theorem | +2 |
| ε greedy | **$\varepsilon$ greedy [keep]** | +3 |
|  | _(keep)_ | +3 |
| 𝓐 e τ observation ambiguity | **observation ambiguity $\mathcal{A}$ [canonicalize]** | +3 |
|  | observation ambiguity [add-alias] | +3 |
| 𝓣 adaptive tempo | **adaptive tempo $\mathcal{T}$ [canonicalize]** | +3 |
|  | tempo [add-alias] | +3 |
| $A_O(M_t; \Pi, N_h)$ | **achievable value [add-alias]** | +2 |
| $C_{\text{coord}}$ | **coordination overhead [add-alias]** | +2 |
| $G_t = (O_t, \Sigma_t)$ | **purposeful state [add-alias]** | +2 |
|  | purposeful substate [add-alias] | +2 |
| $G_t$ | **teleological substate [add-alias]** | +2 |
| $G_{\text{shared}}$ | **shared intent payload [add-alias]** | +2 |
| $I_{\min}$ | **survival information floor [add-alias]** | +2 |
| $K_c$ | **macro step ratio [add-alias]** | +2 |
| $M_t$ | **model state or epistemic substate [add-alias]** | +2 |
| $U_M$ | **epistemic unity [add-alias]** | +2 |
| $U_M, U_O, U_\Sigma, U_{\text{obs}}, U_f$ | **unity coordinate [add-alias]** | +2 |
| $U_O$ | **teleological unity [add-alias]** | +2 |
| $U_\Sigma$ | **strategic unity [add-alias]** | +2 |
| $U_o$ versus $U_O$ | **_(keep)_ ⭑** | +2 |
| $U_{\text{src}}$ and $U_{\text{align}}$ | **trust uncertainty [add-alias]** | +2 |
| $\Delta T_{i,\text{cost}}$ | **coordination drag [add-alias]** | +2 |
| $\alpha_3$ | **fisher whitened tier [add-alias]** | +2 |
|  | fisher whitened regime [add-alias] | +2 |
| $\beta$ a2 sub scope | **assumed regime [add-alias]** | +2 |
|  | postulated regime [add-alias] | +2 |
|  | ✗ posited regime [add-alias] | -1 |
|  | ✗ unverified regime | -1 |
| $\beta$ sub scope | **assumed sector tier [add-alias]** | +2 |
|  | dynamic gain boundary [add-alias] | +1 |
| $\delta_s$ plan confidence error | **plan confidence error [add-alias]** | +2 |
| $\delta_t$ mismatch | **mismatch or the aporia signal [add-alias]** | +2 |
| $\delta_t$ mismatch signal | **_(keep)_** | +2 |
| $\delta_{\text{strategic}}$ | **strategic calibration [add-alias]** | +2 |
| $\delta_{\text{strategic}}$ strategic calibration residual | **strategic calibration residual [add-alias]** | +2 |
| $\eta^\ast$ optimal update gain | **trust ratio [add-alias]** | +2 |
|  | optimal update gain [add-alias] | +2 |
|  | trust ratio or confidence weighting [add-alias] | +1 |
|  | update gain [add-alias] | +1 |
| $\iota_{ij}$ identifiability coefficient | **identifiability coefficient [add-alias]** | +2 |
| $\kappa_{\text{eff}}$ | **effective ambiguity coupling [add-alias]** | +2 |
| $\kappa_{\text{processing}}$ architectural coupling | **processing coupling [add-alias]** | +2 |
| $\lambda(M_t)$ | **exploration weight [add-alias]** | +2 |
|  | exploration multiplier [add-alias] | +1 |
| $\mathcal{A}(e_\tau)$ | **observation ambiguity [add-alias]** | +2 |
| $\mathcal{C}_t$ chronica | **chronica or interaction history [add-alias]** | +2 |
|  | symbol name are locked [add-alias] | +0 |
| $\phi$ | **history compression [add-alias]** | +2 |
| $\rho_\Sigma$ | **strategy drift rate [add-alias]** | +2 |
|  | strategic disturbance rate [add-alias] | +2 |
| $\rho_{i,\text{eff}}$ | **effective disturbance [add-alias]** | +2 |
| $\tilde{\delta}_t$ | **variational aporia [add-alias]** | +2 |
| $p_{ij}$ | **edge credence [add-alias]** | +2 |
| $w(t)$ | **mismatch injection [add-alias]** | +2 |
| AAD theoretical core vs ASF framework | **AAD vs ASF distinction** | +2 |
|  | AAD ASF disambiguation [canonicalize] | +2 |
| CIY causal information yield | **causal information yield action distinguishability** | +2 |
|  | action distinguishability | +2 |
|  | interventional contrast | +2 |
| CIY observational proxy | **_(keep)_** | +2 |
|  | observational CIY | +2 |
|  | observational proxy | +1 |
| OODA4 framework enforcing adaptive cycle separation | **agentic scaffold [name-unnamed]** | +2 |
| a1 a2 a3 a4 | **macro dynamic admissibility [canonicalize]** | +2 |
|  | aporia phase | +1 |
| adversarial edge target argmax | **edge targeting optimum [name-unnamed]** | +2 |
|  | adversarial edge targeting | +2 |
| agent visible but objective irrelevant metric | **vanity metric [add-alias]** | +2 |
|  | irrelevant visibility artifact | +2 |
| and or scope | **_(keep)_** | +2 |
| bathtub analogy for persistence condition | **leaky bathtub analogy [canonicalize]** | +2 |
|  | bathtub model | +2 |
|  | walton bathtub | +1 |
| beta a2 assumed sub scope | **cyclic game sub scope** | +2 |
|  | assumed sector regime | +1 |
| cadentia | **adaptive tempo** | +2 |
|  | _(keep)_ | +2 |
|  | channel rate | +1 |
|  | cognitive rhythm | +0 |
| canonical formulation | **_(keep)_ ⭑** | +2 |
|  | ✗ working canon | -1 |
| catastrophic forgetting regime | **_(keep)_** | +2 |
|  | empty window pathology [add-alias] | +2 |
| causal OODA1 LMI | **matrix survival bound** | +2 |
|  | _(keep)_ | +1 |
| chronica brief gloss | **interaction history chronica** | +2 |
| claim the proposition the segment carry | **segment claim** | +2 |
|  | claim [canonicalize] | +2 |
| class 2 scope exit | **class 2 scope boundary** | +2 |
|  | _(keep)_ ⭑ | +2 |
| cognitive substrate gemini logostratum proposal | **logostratum [keep]** | +2 |
| completeness c3 | **predictive completeness behavioral completeness [name-unnamed]** | +2 |
|  | predictive completeness | +2 |
| composition route c i c ii c iii c iv | **composition route [canonicalize]** | +2 |
|  | composition pathway | +1 |
| composition scope condition | **_(keep)_** | +2 |
|  | composite agent condition | +1 |
|  | teleological alignment condition | +1 |
| concept the strengthening of satisfaction gap and control regret diagnostic across the c1 c2 c3 hierarchy naming both the strengthening pattern and the underlying ordered result that produce it | **inferential force cascade [name-unnamed]** | +2 |
|  | the convention monotonicity [name-unnamed] | +2 |
|  | inferential cascade [name-unnamed] | +1 |
| concept walton plain language analog for the persistence condition fluid level as belief reality gap inflow as reality change rate outflow as learning rate container size as adaptive reserve | **bathtub model [name-unnamed]** | +2 |
|  | the bathtub model [name-unnamed] | +1 |
| conspectus | **active context** | +2 |
|  | model sufficiency | +2 |
|  | _(keep)_ | +2 |
|  | ✗ pre event state | -1 |
| correlation hierarchy | **correlation ladder** | +2 |
| default internal processing before output | **deliberation lag** | +2 |
|  | interior baseline [name-unnamed] | +1 |
| derivation audit table heading | **derivation audit [canonicalize]** | +2 |
| distributed tempo | **_(keep)_** | +2 |
|  | network tempo | +1 |
| eli the agent type | **eli agent [keep]** | +2 |
|  | eli [keep] | +2 |
| empirical heuristic discussion third ring | **heuristic ring** | +2 |
|  | calibration ring | +1 |
| escape route | **_(keep)_ ⭑** | +2 |
|  | ✗ floor escape | -1 |
| evaluation metric | **logogenic diagnostic** | +2 |
|  | _(keep)_ | +2 |
| fisher whitened update rule | **fisher update** | +2 |
|  | _(keep)_ | +2 |
|  | fisher whitened update | +1 |
| gate 1 2 3 4 | **_(keep)_** | +2 |
|  | dependency content mechanical wn gate [add-alias] | +1 |
| gemini analysis paralysis for excessive deliberation | **deliberation gridlock** | +2 |
|  | reject analysis paralysis [rebuttal] | +1 |
| glue code | **agentic scaffold** | +2 |
|  | structural coordination overhead | +2 |
| greek rooted vocabulary | **greek philosophical vocabulary [canonicalize]** | +2 |
|  | _(keep)_ | +2 |
| hierarchy as repeated word | **hierarchy [keep]** | +2 |
|  | reserve for pearl rename other selectively | +1 |
| integration of four discipline as the framing of AAD contribution | **four discipline synthesis** | +2 |
|  | epistemic architecture [canonicalize] | +2 |
| internal external decomposition | **viability decomposition** | +2 |
|  | boundary decomposition | +1 |
| interpre | **context mediator** | +2 |
|  | epistemic substate | +2 |
|  | _(keep)_ | +1 |
|  | ✗ controller loop | -1 |
| l1 | **level 1 associational [canonicalize]** | +2 |
|  | ✗ l1 c | -1 |
| lindy baseline | **_(keep)_** | +2 |
|  | structural persistence baseline | +2 |
| logostratum | **_(keep)_** | +2 |
|  | ✗ cognitive substrate | -1 |
| logostratum rlhf4 backbone | **logogenic architecture** | +2 |
| low mixed high ambiguity event mix | **ambiguity profile [name-unnamed]** | +2 |
|  | ambiguity stratified event mix | +2 |
| matrix CIY tensor CIY | **matrix causal information yield** | +2 |
|  | fisher CIY [canonicalize] | +1 |
|  | matrix CIY consistent [canonicalize] | +1 |
| maximum useful chain depth | **_(keep)_ ⭑** | +2 |
|  | maximum viable chain depth | +2 |
| model synchronization cost reversal under ambiguity | **synchronization cost reversal** | +2 |
|  | ambiguity reversal [name-unnamed] | +1 |
| nominal coupling | **query bound** | +2 |
|  | attention bound | +2 |
|  | epistemic only | +2 |
|  | query coupling | +2 |
|  | attentional coupling | +2 |
|  | query bound agency | +2 |
| observation design lever reducing ambiguity | **ambiguity damping [name-unnamed]** | +2 |
|  | ambiguity mitigation lever | +2 |
| ooda4 agent as act agent logogenic | **ooda4 classification** | +2 |
| ooda4 framework enforcing adaptive cycle separation | **ooda4 cycle separation** | +2 |
| out of band time marker for RLHF4 agent | **time delta marker [name-unnamed]** | +2 |
| out of band time marker for rlhf4 agent | **exogenous temporal marker** | +2 |
| p1 p2 p3 | **projection admissibility [canonicalize]** | +2 |
|  | predictive sufficiency hierarchy | +2 |
| pearl-level 2 causal contrast | **level 2 interventional contrast** | +2 |
|  | _(keep)_ | +1 |
| principled decision integration | **temporal decision integration** | +2 |
|  | _(keep)_ | +2 |
| promote in topological order | **topological promotion** | +2 |
|  | topological promotion order | +1 |
| prompt engineering | **ambiguity modulation** | +2 |
|  | observation boundary tuning | +2 |
| quality to tempo chain | **_(keep)_ ⭑** | +2 |
| readme md maturity gradient | **_(keep)_** | +2 |
|  | readme md theory maturity gradient | +1 |
| readme md novel result | **_(keep)_** | +2 |
| regime a regime b regime c | **identification regime [canonicalize]** | +2 |
|  | admissibility regime | +2 |
| replayed pseudo event | **replay event [canonicalize]** | +2 |
|  | simulated event playback | +2 |
| simulation result | **_(keep)_** | +2 |
| strategy cost regret bound | **regret bound** | +2 |
|  | _(keep)_ | +1 |
| strategy persistence schema | **_(keep)_** | +2 |
|  | strategic persistence | +1 |
| structural adaptation enablement | **consolidation enablement [canonicalize]** | +2 |
|  | structural adaptation trigger | +2 |
| structured rich context | **structured context** | +2 |
|  | _(keep)_ | +2 |
| survival fisher floor | **_(keep)_ ⭑** | +2 |
|  | survival fim floor | +2 |
| symbiogenic consolidation time | **consolidation horizon [name-unnamed]** | +2 |
|  | consolidation epoch | +2 |
| symbol default bia bound track 1 track 2 | **class 2 bia bound** | +2 |
|  | transport track fisher track [name-unnamed] | +1 |
| technical debt | **observability defect** | +2 |
|  | structural capacity debt | +2 |
| terminal reached but $O_t$ unsatisfied | **attainability failure** | +2 |
|  | terminal but unsatisfied case | +1 |
|  | arrival without success | +1 |
| the trio collectively m1 m2 m3 | **epistemic architecture** | +2 |
|  | meta architecture trio | +1 |
|  | floor ladder forced coordinate | +1 |
| tier 1 tier 2 tier 3 contraction | **contraction hierarchy** | +2 |
|  | contraction tier [canonicalize] | +2 |
| todo md archive | **_(keep)_** | +2 |
| topological promotion order | **topological promotion [canonicalize]** | +2 |
|  | ✗ dependency respecting promotion | -1 |
| turnover multiplier | **_(keep)_ ⭑** | +2 |
|  | comprehension compounding tax | +2 |
|  | multi agent continuity tax | +1 |
| two condition decomposition of persistence | **persistence condition decomposition** | +2 |
|  | structural task adequacy decomposition [canonicalize] | +2 |
| u obs perceptual unity | **perceptual unity [add-alias]** | +2 |
| u σ strategic unity | **strategic unity [add-alias]** | +2 |
| unnamed an AAD result whose substantive content is a no-go theorem | **no-go result or impossibility result [name-unnamed]** | +2 |
| unnamed complexity driven resistance to change as feature accumulate | **structural rigidity accumulation** | +2 |
|  | structural accumulation drag [name-unnamed] | +1 |
| unnamed constitutive opacity triad | **constitutive opacity triad [canonicalize]** | +2 |
| unnamed epochal stability → latent diversification → niche emergence | **symbiogenic composition progression** | +2 |
|  | punctuated composition dynamic [name-unnamed] | +1 |
| unnamed escalating from one step to bellman optimality to test if a goal is genuinely impossible | **convention escalation [name-unnamed]** | +2 |
|  | attainability horizon escalation | +2 |
| unnamed git recorded committed state subset of the chronica $\mathcal{C}_t^{\text{commit}}$ | **committed chronica subset** | +2 |
|  | commit chronica [name-unnamed] | +1 |
| unnamed mapping unstructured RLHF7 call into conversation runtime RLHF7 and dialog | **four view architecture [name-unnamed]** | +2 |
| unnamed mapping unstructured rlhf7 call into conversation runtime rlhf7 and dialog | **logogenic interaction mapping** | +2 |
| unnamed master developer writing clean code in the same time as messy code | **near zero cost observation [name-unnamed]** | +2 |
| unnamed neutralizing sycophancy by hardening the environment to drop ambiguity to zero | **ambiguity zeroing intervention** | +2 |
| unnamed non sovereign class 1 worker agent spawned by an eli | **auxilia hierarchy [name-unnamed]** | +2 |
|  | sub agent instantiation | +2 |
| unnamed sycophantic corruption of the agent truth module | **truth death [name-unnamed]** | +2 |
|  | epistemic coupling corruption | +2 |
| unnamed the 1 anchor 3 theorem structure in additive coordinate forcing | **anchor theorem structure** | +2 |
| unnamed the cumulative prediction error that an agent has tolerated without updating its model | **mismatch accumulation** | +2 |
|  | tolerance budget standing mismatch reservoir [name-unnamed] | +1 |
| unnamed the cycle that operate on cycle structural adaptation | **meta cycle [name-unnamed]** | +2 |
|  | meta adaptive cycle | +2 |
| unnamed the family of cross architecture diagnostic pattern AAD repeatedly invoke | **diagnostic template [name-unnamed]** | +2 |
| unnamed the family of named health mode counterpart to persistence pathology | **persistence posture [name-unnamed]** | +2 |
| unnamed the interval during which an agent adaptive tempo exceed the environment disturbance rate guaranteeing mismatch stay bounded | **operational persistence window** | +2 |
|  | adaptive reserve margin [name-unnamed] | +2 |
| unnamed the move where a segment role prefix is mechanical but the subject noun carry judgment | **the prefix noun split [canonicalize]** | +2 |
| unnamed the pathology where observation rate is slower than environment drift | **lagging indicator [add-alias]** | +2 |
|  | sampling rate starvation | +2 |
| unnamed the pearl-blanket reading of directed separation | **pearl-blanket form [name-unnamed]** | +2 |
| unnamed the procedure of reading any segment through all three meta segment | **meta architectural review** | +2 |
|  | triple len review [name-unnamed] | +1 |
| unnamed the property that correction dynamic are approximately isotropic | **isotropic correction** | +2 |
|  | ✗ isotropic correction regime [name-unnamed] | -1 |
| unnamed the quadratic scaling of tempo required to survive stochastic noise vs deterministic drift | **noise scaling penalty [name-unnamed]** | +2 |
|  | stochastic tempo penalty | +2 |
| unnamed the recurring lyapunov derive the bound move across six segment | **the persistence template instantiation pattern [name-unnamed]** | +2 |
| unnamed the region where temporal nesting hold | **temporal nesting regime** | +2 |
|  | temporal coherence zone [name-unnamed] | +1 |
| unnamed the regulative ideal that segment name should be re derivable from a non specialist everyday language reconstruction | **feynman criterion [canonicalize]** | +2 |
| unnamed the rule that bia is the product of architectural coupling and environmental ambiguity | **ambiguity coupling rule** | +2 |
| unnamed the separation of per reader and per feature code cost | **dual optimization partition** | +2 |
| unnamed the set of five condition under which a2 is derived rather than assumed the sub scope α agent classe | **sub scope alpha taxonomy** | +2 |
|  | derived sector classe [name-unnamed] | +1 |
| unnamed the signed coupling structure across all section iii result | **signed coupling topology** | +2 |
|  | signed coupling pattern [name-unnamed] | +1 |
| unnamed the structural cousin of evidence starvation when an upstream edge is so reliable that downstream edge receive too few revising test | **evidence saturation [name-unnamed]** | +2 |
| unnamed the symmetric counterpart to context turnover for the strategy substate | **strategic turnover or σ turnover [name-unnamed]** | +2 |
| unnamed the within session vs inter session persistence distinction for logogenic agent | **operational vs reconstruction persistence** | +2 |
|  | intra session persistence inter session reconstruction [name-unnamed] | +2 |
| working vocabulary observation the framework honesty is load bearing | **honest limit principle** | +2 |
|  | load bearing honesty [name-unnamed] | +1 |
| 𝓣 σ strategic tempo | **strategic tempo [add-alias]** | +2 |
| $C$ bia bound constant in bia bound derivation | **bia bound constant [add-alias]** | +1 |
| $M_t$ reality model | **working model** | +1 |
|  | predictive state | +1 |
| $R$ sector region radius | **model class capacity [add-alias]** | +1 |
| $U_M$ $U_O$ $U_\Sigma$ unity dimension | **epistemic unity teleological unity strategic unity [add-alias]** | +1 |
| $U_M$ dual use model uncertainty and epistemic unity | **clarify dual use of $U_M$ [canonicalize]** | +1 |
| $U_o$ | **teleological coherence [add-alias]** | +1 |
| $U_o$ $U_M$ observation uncertainty model uncertainty | **$U_o$ $U_M$ [add-alias]** | +1 |
| $\alpha, \beta$ sector lower and a2 sub scope | **$\alpha, \beta$** | +1 |
| $\alpha_1$ $\alpha_2$ $\beta$ naming as a whole | **$\alpha$ partition with english label above [add-alias]** | +1 |
| $\alpha_2$ a2 adaptive gain sub scope under mg 1 mg 4 | **adaptive gain regime [add-alias]** | +1 |
| $\beta$ a2 assumed not derived sub scope | **assumed regime [add-alias]** | +1 |
| $\beta$ a2 assumed sub scope | **assumed gain regime [add-alias]** | +1 |
|  | ✗ verified externally regime [add-alias] | -1 |
| $\beta$ a2 assumption tier | **assumed regime [add-alias]** | +1 |
| $\beta$ a2 sub scope where a2 is assumed not derived | **postulated sector regime [add-alias]** | +1 |
| $\kappa_{\text{processing}}$ class 2 processing coupling | **processing coupling [add-alias]** | +1 |
| $\mathcal C_t^{\text{commit}}$ TST committed state subset | **$\mathcal C_t^{\text{commit}}$ [keep]** | +1 |
| $\mathcal C_t^{\text{commit}}$ committed state subset | **committed chronica [add-alias]** | +1 |
| $\rho$ environment change rate mismatch injection rate | **$\rho$** | +1 |
| $\rho_\Sigma$ strategic disturbance rate | **$\rho_\Sigma$** | +1 |
|  | strategic disturbance rate [add-alias] | +1 |
| $f_M$ event driven update | **epistemic update function [add-alias]** | +1 |
| $f_{\text{init}}$ reconstruction function | **epistemic reconstruction [add-alias]** | +1 |
| $g_M$ between event evolution | **autonomous evolution [add-alias]** | +1 |
| OODA4 specification limit as TST concept currently only in old TST file | **OODA4 specification limit** | +1 |
| actuated agent class | **actuated [add-alias]** | +1 |
| agent classe lexicon spectrum | **_(keep)_ ⭑** | +1 |
| agentic system framework ASF top level | **agentic system framework [keep]** | +1 |
| audit pending finding yyyy mm dd md | **retire once item reconcile into todo segment [keep]** | +1 |
| calibration laboratory framing | **calibration laboratory** | +1 |
| change distance change proximity principle | **_(keep)_** | +1 |
| chronica capitalized vs lowercase | **chronica lowercase in running prose** | +1 |
| cold start in naming principle md | **cold start** | +1 |
| communal imagination test | **_(keep)_** | +1 |
| communal imagination test in naming principle md | **communal imagination test** | +1 |
| comprehension time implementation time | **_(keep)_** | +1 |
| da2 inc | **_(keep)_** | +1 |
| dark room critique citation phrasing sun firestone | **dark room critique** | +1 |
| five phase cycle | **adaptive pentad alternative five phase cycle keep** | +1 |
| future segment information theoretic cost floor for persistence | **persistence cost [name-unnamed]** | +1 |
| gain sector bridge gain sector derivation | **_(keep)_** | +1 |
| gate 1 gate 2 gate 3 gate 4 format md promotion gate | **_(keep)_** | +1 |
| gemini competency trap for $\eta^\ast \to 0$ | **reject competency trap [rebuttal]** | +1 |
| gemini epistemic death for the gain collapse unobservable DAG failure | **reject epistemic death [rebuttal]** | +1 |
| hierarchy as a project wide word | **flag four independent hierarchy overloaded** | +1 |
| hierarchy project wide | **_(keep)_** | +1 |
| identifiability floor escape the floor | **escape route** | +1 |
| intent planning vocabulary | **intent [canonicalize]** | +1 |
| interior baseline | **_(keep)_** | +1 |
|  | default interiority | +1 |
|  | ✗ pre utterance processing | -1 |
| l1 prime decoration | **l1 observable [add-alias]** | +1 |
| logostratum RLHF4 backbone | **cognitive substrate** | +1 |
| migration map md | **_(keep)_** | +1 |
| mismatch injection rate $\rho$ | **mismatch injection rate [keep]** | +1 |
| model sufficiency model class fitness | **_(keep)_** | +1 |
| msc architectural proposal yyyy mm dd md | **retire once consolidated into proposal md [keep]** | +1 |
| msc reflection | **_(keep)_** | +1 |
| multi agent scope | **shared environment scope** | +1 |
|  | _(keep)_ | +1 |
| observability opacity | **_(keep)_** | +1 |
| observation function action transition | **_(keep)_** | +1 |
| old TST file 40 file | **no rename these retire with migration map [keep]** | +1 |
| outline md 01 AAD core preamble | **reading AAD** | +1 |
| pearl l1 | **predicting [add-alias]** | +1 |
| pearl l2 | **exploring [add-alias]** | +1 |
| pearl l3 | **reasoning [add-alias]** | +1 |
| persistence three sense structural operational continuity | **_(keep)_** | +1 |
| prior art integration convention | **prior art integration** | +1 |
| r1 r2 result numbering convention in logogenic agent | **_(keep)_** | +1 |
| readme md lexicon | **_(keep)_** | +1 |
| readme md structure | **readme md theory architecture** | +1 |
|  | _(keep)_ | +1 |
| recursive update derivation gain sector derivation | **_(keep)_** | +1 |
| section ii header actuated adaptation agentic system | **actuated adaptation agentic system [canonicalize]** | +1 |
| spike index md | **_(keep)_** | +1 |
| spike index md spike index | **spike index md** | +1 |
| spike research artifact | **spike [canonicalize]** | +1 |
| spike spike topic md | **_(keep)_** | +1 |
| spike spike topic yyyy mm dd md | **_(keep)_** | +1 |
| strategic dynamic derivation | **_(keep)_** | +1 |
|  | strategy edge dynamic | +1 |
| system coherence system coupling system availability | **_(keep)_** | +1 |
| terminal alignment error | **terminal alignment gap** | +1 |
| the greek vocabulary | **the greek philosophical vocabulary [canonicalize]** | +1 |
| the integrated κ × a law | **the bia bound product law [canonicalize]** | +1 |
| the trio collectively | **epistemic architecture [name-unnamed]** | +1 |
| three part meta architecture | **floor ladder forced coordinate** | +1 |
| todo md active pending review spike | **todo md active** | +1 |
| track 1 track 2 in bia bound | **transport track fisher rao track [add-alias]** | +1 |
|  | track 1 track 2 [keep] | +1 |
| track 1 track 2 in bia bound derivation | **transport inequality track fisher rao track** | +1 |
| u f update rule homogeneity | **update rule homogeneity [add-alias]** | +1 |
| unnamed TST specific name for code that is observation cheap because it well written | **observation cheap code [name-unnamed]** | +1 |
| unnamed class 1 class 2 class 3 agent classe themselve need mnemonic handle | **proposal assign english modifier [name-unnamed]** | +1 |
| unnamed effort time risk ranking considered false constraint | **false constraint [name-unnamed]** | +1 |
| unnamed future segment layer header for narrative pedagogical framing | **narrative framing [name-unnamed]** | +1 |
| unnamed future segment layer header for the sp 5 reader path proposal | **reader path [name-unnamed]** | +1 |
| unnamed scope honesty as architecture | **honesty [name-unnamed]** | +1 |
| unnamed the 2×2 satisfaction gap × control regret diagnostic table | **the 2×2 diagnostic [name-unnamed]** | +1 |
| unnamed the a2 sub scope partition collectively | **a2 partition [name-unnamed]** | +1 |
| unnamed the architectural class partition class 1 class 2 class 3 | **architectural partition [name-unnamed]** | +1 |
| unnamed the complete adaptive cycle from anticipation through action | **adaptive cycle already named in lexicon [name-unnamed]** | +1 |
| unnamed the derivation formulation hypothesis status gradient in format md | **epistemic gradient [name-unnamed]** | +1 |
| unnamed the dimensional consistency constraint forcing the macro step formulation | **dimensional consistency repair [name-unnamed]** | +1 |
| unnamed the discipline of naming so that the slug survive reorganization | **reorganization resilient naming [name-unnamed]** | +1 |
| unnamed the dual that pair with persistence envelope on the strategic side | **strategic persistence envelope [name-unnamed]** | +1 |
| unnamed the functional requirement are the result formalism are the engineering slogan | **functional primacy [name-unnamed]** | +1 |
| unnamed the iterated audit process gemini opus codex de novo consolidated three doc portfolio | **cross model audit cycle [name-unnamed]** | +1 |
| unnamed the mathematical operation by which agent convert observed mismatch into structural revision | **structural cascade [name-unnamed]** | +1 |
| unnamed the moment when an agent identity claim become load bearing because action become irreversible | **constitutive moment [name-unnamed]** | +1 |
| unnamed the orient cascade information dependency forced ordering as a meta pattern | **information dependency forcing [name-unnamed]** | +1 |
| unnamed the rate at which an agent chronica grow compared to compression cadence | **chronica throughput [name-unnamed]** | +1 |
| unnamed the scope honesty as architecture working principle | **honesty scope honesty as architecture [name-unnamed]** | +1 |
| unnamed the strengthen first attempt artifact a spike that tried to derive something stronger and failed | **strengthening attempt attempt record [name-unnamed]** | +1 |
| unnamed the symbol overload region where $U_M$ mean two different thing | **the $U_M$ overload [name-unnamed]** | +1 |
| unnamed the template family sector persistence contraction possible future dissipativity | **persistence template the template family [name-unnamed]** | +1 |
| unnamed the three concentric ring of segment content inevitability core canonical formulation empirical heuristic | **three ring [name-unnamed]** | +1 |
| unnamed the three ring of segment content framing | **segment ring [name-unnamed]** | +1 |
| unnamed the threshold energy information cost below which an agent is forced to act accept mismatch rather than deliberate | **deliberation threshold [name-unnamed]** | +1 |
| what is derived vs what is chosen | **derivation audit** | +1 |
|  | derived vs chosen vs assumed | +1 |
| what is derived vs what is chosen derivation audit table | **derivation audit** | +1 |
| $G_t$ goal state | **symbol is clear no alia needed [add-alias]** | +0 |
| $\mathcal{T}$ adaptive tempo | **tempo already canonical [add-alias]** | +0 |
| $\rho$ disturbance rate | **disturbance rate already in use [add-alias]** | +0 |
| unnamed the five phase of the adaptive cycle | **already named in notation md [name-unnamed]** | +0 |
| AAD alternative considered for completeness | **✗ apd adaptation and purpose dynamic** | -1 |
|  | ✗ AAD adaptation and agency dynamic | -1 |
| a2 operator sector condition under fidelity degraded update | **✗  [keep]** | -1 |
| claude md key architectural decision | **✗ claude md architectural decision** | -1 |
| empirical heuristic discussion ring | **✗ third ring or empirical periphery [canonicalize]** | -1 |
| l1 l1 prime | **✗ l1 observable l1 soft** | -1 |
| unnamed the cross cycle equivalent of the bathtub gloss multi cycle persistence as a saving account | **✗ the saving account gloss [name-unnamed]** | -1 |
| unnamed the four axis content structural unity decomposition | **✗ the unity quintet [name-unnamed]** | -1 |
| RLHF6 | **_(keep)_** | -3 |

