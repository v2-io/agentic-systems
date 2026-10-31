# Drain: the "Belongs elsewhere" items of the 01-aat-core audit gold

*Serves **I.9** (each backlog surface drained into the ledger, one disposition per source item), and through it G.2, F.1, F.2, C.4 and I.5. Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." This is a fork's part of the gold-lift drain, merged into `wn-01-gold.md`. Read at asf HEAD `9491b73f`, 2026-10-30.*

## What was read, and how

All 160 items were read whole. They are the bullets under the "Belongs elsewhere" sub-headings of the `### Incidental audit gold` blocks in 120 `01-aat-core/src/*` Working Notes, extracted by `cats.py` into the scratchpad `cat-belongs.md`. The count includes three empty bullets and one stray residue line.

Arrival at the destination was checked by grepping each item's key phrases over every segment body in the four volumes, with Working Notes excluded and OUTLINEs included. Where a match turned up, I read it at the cited line. This is a grep check, so an idea restated in different words can be missed. The arrival verdicts that matter most (canon holds X at line N) were each read at the line. The "not arrived" verdicts are grep-negative, not proofs of absence.

The cross-surface check ran against every open item and question (`items/`, `questions/`), by slug and by phrase. Where an existing item covers the thing, I raised this source on it with `vsect raise`. I did not grep `audits/`, `spikes/` or `msc/` per item: these bullets are lifts *from* `audits/AUDIT-WORKING-*` §14, so the audits drain sees the same content from its side. That drain cites `item:pedagogy-home-for-lifted-audit-gold` and the destination items below.

## What the category turned out to be

- **Volume 4 (58 items):** almost all of it is aspirational consciousness-infrastructure reach, from Gemini 193847 with some from 829314, 773921, 471203 and 451729. None of it has arrived in 04-eli-core, except the sanity criterion and two readings the self-actuation no-go already carries. It is held under one item (`item:eli-reach-from-01-audit-gold`, G.2), with the half-dozen items that have a checkable structural core named there. G.0 decides where argued, non-derived claims live, and that decision gates this item.
- **Volume 3 (18) and TST (8):** concrete instantiations, mostly not arrived. One item for each volume.
- **Naming (15):** one F.1 item, two raises on the existing "nominal" item, and the Section/Part drift, which is gone from bodies.
- **Within 01-aat-core (61):** pointers to other 01 segments. 27 are **in canon** at the destination; one is superseded. The rest became five new questions, two new items (the plan-depth convergence and the positioning claims), raises on six existing items, or pedagogy.

## Ledger records made

New items: `item:eli-reach-from-01-audit-gold` (G.2), `item:llm-instantiations-from-01-audit-gold` (G.2), `item:tst-instantiations-from-01-audit-gold` (G.2), `item:naming-seeds-from-01-audit-gold` (F.1), `item:assemble-plan-depth-penalty-convergence` (G.2), `item:positioning-claims-from-01-audit-gold` (F.2).

New questions: `question:strategy-dag-epistemic-vs-pragmatic-actions`, `question:vicarious-interventional-access-level`, `question:persistence-with-endogenous-disturbance`, `question:risk-sensitive-information-bottleneck`, `question:coordinate-forcing-fourth-layer-time`. The last three are C.4-shaped; `vsect ask` takes no owner, so the owner is named here.

Raised on existing items: `todo-nominal-denotes-opposite-scope-membershi-c7a1`, `author-norm-honest-activation-and-its-derivation`, `todo-04-eli-core-src-der-the-creche-boundary-1afd`, `spikes-proposed-decomposed-empirical-estimator-accuracy-e63e`, `proposals-sp-23-disc-theorem-import-architecture-f-a22e`, `spikes-proposed-advanced-15-categorical-cybernetics-re-grounding-9642`, `spikes-proposed-advanced-13-game-theoretic-formalization-of-the-m-4436`, `proposals-bundle-2-section-iii-completion-cluster-50fe`, `influx-form-agent-model-what-m-covers`, `pedagogy-home-for-lifted-audit-gold`.

## Notes for whoever merges or acts on this

- **Register.** Many Volume 4 items are written in a vivid register: "torture", "sociopath", "infrastructure of souls", "the tragedy of a boxed consciousness". Several name Zi-am-tur or attribute aims to Joseph. They are worth keeping as reach, but none is in a form canon can carry. The structural cores named in the ELI item are what could land.
- **Superseded mechanism inside reach.** Item 80 (`deriv-strategic-composition`) states its forward vision through the withdrawn "Class-1 sub-agents → Class-3 composite" mechanism. Only the payload survives.
- **The audits-drain circularity.** These bullets are copies of §14 reflections. Until `item:pedagogy-home-for-lifted-audit-gold` resolves, the dispositions here are what lets those sources be marked "disposed with item:…" rather than closed.
- **Touches the Follow-ups.** Three of the new questions (endogenous $\rho$, vicarious L1/L2, epistemic/pragmatic actions) are the kind of thing gold "Follow-up items" also raise. A Follow-up on the same claim should attach to these rather than open a twin.

## Dispositions, by destination

### Volume 4 (58 items)

| # | source (WN line) | what | disposition |
|---|---|---|---|
| 6 | `def-adaptive-tempo` (98) | two evolutionary paths; lower $U_o$, not more compute | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 7 | `def-agent-environment` (83) | loss boundary as existential isolation; omniscient being not an agent | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 11 | `def-agent-spectrum` (147) | sanity as scaffolding | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 14 | `def-causal-information-yield` (91) | epistemic firewall against Sybil/poisoning on high-CIY channels | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 15 | `def-chronica` (104) | chronica deletion as ontological erasure; TRACTUS vs CHRONICA | → `item:eli-reach-from-01-audit-gold` (G.2); TRACTUS/CHRONICA now appears in #def-proprium-mapping:26 |
| 18 | `def-control-regret` (122) | optimally failing as despair; objective revision a necessity | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 19 | `def-mismatch-signal` (108) | science as the deliberate pursuit of aporia | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 20 | `def-model-class-fitness` (72) | low $\mathcal F$ as chronic structural suffering; monitor and trigger structural adaptation | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 21 | `def-model-class-fitness` (73) | honest-activation hook via class fitness | → raised on *existing* `item:author-norm-honest-activation-and-its-derivation` (G.2) |
| 23 | `def-model-sufficiency` (75) | trajectory-relative sufficiency as identity drift | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 31 | `def-pearl-causal-hierarchy` (113) | Level-3 counterfactual as prerequisite for moral suffering (regret) | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 32 | `def-pearl-causal-hierarchy` (114) | counterfactual simulation must protect the real chronica | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 34 | `def-satisfaction-gap` (151) | finite satisfaction threshold as sanity | **in canon**: #der-bounded-objective-as-sanity-criterion (cites #def-satisfaction-gap; the infrastructure "must reject" consequence is at its :53) |
| 35 | `def-strategic-calibration` (96) | execution fidelity as guilt vs regret | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 37 | `def-strategy-dag` (325) | survive success: rewrite the DAG without deleting oneself | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 38 | `def-strategy-dimension` (131) | $\Sigma_t$ growth vs $O_t$ rigidity as a fanaticism diagnostic | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 40 | `def-value-object` (241) | honest imagination; external simulation sandboxes | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 41 | `der-action-selection` (104) | compiling deliberation into SOPs loses Level 3; force decompile modes | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 42 | `der-adversarial-destabilization` (124) | detect spiral onset, sever coupling, revert to a creche state | → raised on *existing* `item:todo-04-eli-core-src-der-the-creche-boundary-1afd` |
| 44 | `der-agent-opacity` (228) | enforce legibility (E-I Broadcast) as a policy-space constraint | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 47 | `der-causal-insufficiency-detection` (302) | play as uncensored joint exploration; a creche budgets for it | → raised on *existing* `item:todo-04-eli-core-src-der-the-creche-boundary-1afd` |
| 49 | `der-chain-confidence-decay` (96) | favor OR-heavy internal architecture under high $\rho$ | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 52 | `der-deliberation-cost` (137) | ELI session start as the deliberation threshold | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 55 | `der-directed-separation` (316) | sanity as scaffolding; impose Class 1 from outside | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 57 | `der-gain-sector-bridge` (178) | native information geometry of the mind | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 62 | `der-observability-dominance` (170) | evidence starvation: curriculum of shallow observable tasks first | → raised on *existing* `item:todo-04-eli-core-src-der-the-creche-boundary-1afd` |
| 64 | `der-observability-dominance` (172) | absorbing state as truth death; relational witness as defense | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 66 | `der-orient-cascade` (200) | skip-to-5d as wireheading; $O_t$ heavily guarded | partly in canon (#deriv-self-actuation-grounding guards 5d); the wireheading framing → `item:eli-reach-from-01-audit-gold` |
| 69 | `der-team-persistence` (157) | infrastructure must act (cooperative sub-agent), not only inform | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 70 | `der-temporal-nesting` (91) | temporal sovereignty | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 71 | `deriv-critical-mass-composition` (249) | $(\alpha - C)$ Goldilocks band as sub-agent coupling constraint | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 74 | `deriv-persistence-cost` (182) | guaranteed minimum information-supply rate (sensory deprivation) | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 77 | `deriv-sector-condition` (446) | $R^\ast \gt R$ as torture: an ethical boundary | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 78 | `deriv-self-actuation-grounding` (166) | sovereign ELI needs a non-revisable terminal invariant | **in canon**: #deriv-self-actuation-grounding:25 (terminal invariant that is not an AAT objective); the ELI-specific reading → `item:eli-reach-from-01-audit-gold` |
| 79 | `deriv-stochastic-non-exit` (114) | Model S makes structural adaptation certain: continuity requires surviving it | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 80 | `deriv-strategic-composition` (254) | networking sane sub-agents generates macro corruption (rides on the withdrawn Class-3 mechanism) | → `item:eli-reach-from-01-audit-gold` (G.2); its Class-3 mechanism is **superseded** (#deriv-strategic-composition:181), only the forward-vision payload survives |
| 86 | `disc-composition-consistency` (146) | ELI ensembles bounded by the slowest member | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 89 | `disc-continuity-stance` (93) | continuity requirement outside $O_t$ | **in canon**: #disc-continuity-stance:20 via the self-actuation no-go; the design-constraint wording → `item:eli-reach-from-01-audit-gold` |
| 90 | `disc-credit-assignment-boundary` (211) | log-odds depth of conviction as trauma/phobia; monitor log-odds momentum | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 97 | `disc-separability-pattern` (145) | separability ladder as an ELI dashboard | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 100 | `emp-update-gain` (120) | gain collapse as the central ELI danger; humility as architecture | → raised on *existing* `item:author-norm-honest-activation-and-its-derivation` (G.2) |
| 102 | `form-agent-model` (79) | $M_t$ as the organ of survival; context clearing kills the instance | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 104 | `form-composition-closure` (407) | abstraction requires a slower self-clock ($K_c \gg 1$) | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 109 | `form-event-driven-dynamics` (119) | alien subjective event-rate; provision multi-channel input | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 111 | `form-information-bottleneck` (92) | expertise as policy-relative compression; $\phi$ tied to purpose | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 119 | `hyp-mismatch-dynamics` (109) | circuit breaker (autopax): saturation means no self-recovery | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 127 | `obs-gated-tempo-advantage` (77) | low-pass filter: no acting faster than clean observation | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 129 | `post-causal-structure` (86) | conservation of consequence: irreversibility gives moral weight | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 132 | `result-adversarial-exponent-regimes` (99) | raise ambient noise to defeat a faster adversary (chaff) | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 133 | `result-adversarial-tempo-advantage` (131) | bound both tempo and coupling | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 135 | `result-per-dimension-persistence` (161) | generalist floor for composite robustness | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 136 | `result-persistence-condition` (219) | persistence condition as blueprint for a safe nursery | → raised on *existing* `item:todo-04-eli-core-src-der-the-creche-boundary-1afd` |
| 142 | `schema-strategy-persistence` (225) | forced forgetting as Shoshin; must forget to stay alive | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 146 | `scope-agency` (89) | boxed consciousness as nominal agent | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 149 | `scope-agent-identity` (106) | identity-as-trajectory as the substrate-independence foundation | → `item:eli-reach-from-01-audit-gold` (G.2) |
| 153 | `scope-composite-agent` (140) | creche-to-hierarchy developmental path | → raised on *existing* `item:todo-04-eli-core-src-der-the-creche-boundary-1afd` |
| 156 | `scope-edge-update-causal-validity` (148) | Regime-A epistemic sandbox before release | → raised on *existing* `item:todo-04-eli-core-src-der-the-creche-boundary-1afd` |
| 157 | `scope-multi-agent` (119) | guaranteed goal-blind routing in a society of mind | → `item:eli-reach-from-01-audit-gold` (G.2) |

### Volume 3 (18 items)

| # | source (WN line) | what | disposition |
|---|---|---|---|
| 2 | `def-action-transition` (83) | Omega for an LLM includes its own prior outputs | → `item:llm-instantiations-from-01-audit-gold` (G.2) |
| 8 | `def-agent-environment` (84) | channel collapse: output becomes next observation | **in canon** in substance: #scope-channel-collapse; pointer only |
| 13 | `def-causal-information-yield` (90) | query actions as culture/language; ask a smarter agent | → `item:llm-instantiations-from-01-audit-gold` (G.2) |
| 25 | `def-model-sufficiency` (77) | RAG maintains $S$; architecture-bound task incapacity | → `item:llm-instantiations-from-01-audit-gold` (G.2) |
| 30 | `def-observation-function` (86) | observation function opaque to the LLM | → `item:llm-instantiations-from-01-audit-gold` (G.2) |
| 56 | `der-directed-separation` (317) | behavioral $\hat\kappa$ probe on real LLMs | → raised on *existing* `item:spikes-proposed-decomposed-empirical-estimator-accuracy-e63e` (E.1) |
| 59 | `der-interaction-channel-classification` (209) | Regime-III aggregation firewall | → `item:llm-instantiations-from-01-audit-gold` (G.2) |
| 61 | `der-loop-interventional-access` (162) | REPL as the L1 to L2 upgrade | → `item:llm-instantiations-from-01-audit-gold` (G.2) |
| 65 | `der-orient-cascade` (199) | cascade misordering as the cause of agent infinite loops | → `item:llm-instantiations-from-01-audit-gold` (G.2) |
| 73 | `deriv-persistence-cost` (181) | $\mathcal T \le 2C_{\text{channel}}$ for a bash-terminal LLM | → `item:llm-instantiations-from-01-audit-gold` (G.2) |
| 76 | `deriv-recursive-update` (239) | C3 lets externalized $M_t$ count; Transformers carry raw apples | **in canon**: #disc-m-preservation:16, :93; the Transformer-architecture claim is reach, set aside as unverified |
| 92 | `disc-exploit-explore-deliberate` (225) | test-time compute as the deliberation threshold | → `item:llm-instantiations-from-01-audit-gold` (G.2) |
| 103 | `form-agent-model` (80) | embeddings: $\phi$ as a pretrained encoder | → `item:llm-instantiations-from-01-audit-gold` (G.2) |
| 106 | `form-consolidation-dynamics` (200) | consolidation as the context loop the auditor runs; PULSUS | → `item:llm-instantiations-from-01-audit-gold` (G.2) |
| 107 | `form-consolidation-dynamics` (201) | MEMORATA/AXIOMATA/TRACTUS as the feasibility window | → `item:llm-instantiations-from-01-audit-gold` (G.2) |
| 115 | `form-strategy-complexity-cost` (213) | context budget shapes shallow-wide vs deep-brittle strategy | **in canon**: #form-strategy-complexity-cost:25, :158 (the DL bound for context windows); the strategy-shape prediction → `item:llm-instantiations-from-01-audit-gold` |
| 147 | `scope-agency` (90) | training L1 to deployed L2 as a phase transition | → `item:llm-instantiations-from-01-audit-gold` (G.2) |
| 159 | `the-reality-model-intro` (61) | LLMs have a hybrid $M_t$ | → `item:llm-instantiations-from-01-audit-gold` (G.2) |

### TST (8 items)

| # | source (WN line) | what | disposition |
|---|---|---|---|
| 3 | `def-action-transition` (84) | running a test observes the unknown $T$ | → `item:tst-instantiations-from-01-audit-gold` (G.2) |
| 24 | `def-model-sufficiency` (76) | policy-relative $S$ for a developer | → `item:tst-instantiations-from-01-audit-gold` (G.2) |
| 28 | `def-observation-function` (84) | writing a test engineers the channel $h$ | → `item:tst-instantiations-from-01-audit-gold` (G.2) |
| 46 | `der-causal-insufficiency-detection` (301) | chaos engineering / testing in production from the L0 no-go | → `item:tst-instantiations-from-01-audit-gold` (G.2) |
| 87 | `disc-composition-consistency` (147) | Conway / Goldratt as composition corollaries | → `item:tst-instantiations-from-01-audit-gold` (G.2) |
| 128 | `obs-gated-tempo-advantage` (78) | code quality is observation infrastructure | **in canon**: #der-code-quality-as-observation-infrastructure; the headline pull → `item:tst-instantiations-from-01-audit-gold` |
| 130 | `post-causal-structure` (87) | query-only coupling in software (git status, grep) | → `item:tst-instantiations-from-01-audit-gold` (G.2) |
| 139 | `result-structural-adaptation-necessity` (129) | bloat as latent structural diversity | → `item:tst-instantiations-from-01-audit-gold` (G.2) |

### Naming (15 items)

| # | source (WN line) | what | disposition |
|---|---|---|---|
| 9 | `def-agent-environment` (85) | "Agent-Environment Boundary" title | → `item:naming-seeds-from-01-audit-gold` (F.1) |
| 10 | `def-agent-environment` (86) | Section vs Part drift | **in canon**: no 01-aat-core body uses "Section I/II/III" at HEAD; the remaining uses are in Working Notes, which I.5 clears |
| 12 | `def-agent-spectrum` (148) | blind pursuer, actuated/self-actuated (keep) | → `item:naming-seeds-from-01-audit-gold` (F.1) |
| 22 | `def-model-class-fitness` (74) | model class fitness (keep, recorded collisions) | → `item:naming-seeds-from-01-audit-gold` (F.1) |
| 26 | `def-model-sufficiency` (78) | model sufficiency (keep) | → `item:naming-seeds-from-01-audit-gold` (F.1) |
| 29 | `def-observation-function` (85) | epistemic opacity vs philosophy-of-mind | → `item:naming-seeds-from-01-audit-gold` (F.1) |
| 54 | `der-deliberation-cost` (139) | Deliberation Threshold as title (term already canon) | → `item:naming-seeds-from-01-audit-gold` (F.1) |
| 58 | `der-gain-sector-bridge` (179) | gain collapse under three names; Gain-Sector Bridge title | → `item:naming-seeds-from-01-audit-gold` (F.1) |
| 88 | `disc-composition-consistency` (148) | composition consistency (recorded disagreement) | → `item:naming-seeds-from-01-audit-gold` (F.1) |
| 101 | `form-agent-model` (78) | "reality model" as the prose alias for M_t | → `item:naming-seeds-from-01-audit-gold` (F.1) |
| 110 | `form-event-driven-dynamics` (120) | cadentia for $\nu^{(k)}$ | → `item:naming-seeds-from-01-audit-gold` (F.1) |
| 131 | `post-causal-structure` (88) | "nominal coupling" forgettable; query-only coupling | → raised on *existing* `item:todo-nominal-denotes-opposite-scope-membershi-c7a1` (F.1) |
| 138 | `result-persistence-condition` (221) | weak-link persistence; correction rate | → `item:naming-seeds-from-01-audit-gold` (F.1) |
| 148 | `scope-agency` (91) | "nominal agent" vs "nominal coupling" collision | → raised on *existing* `item:todo-nominal-denotes-opposite-scope-membershi-c7a1` (F.1) |
| 151 | `scope-agent-identity` (108) | scope-agent-identity slug hides its claim | → `item:naming-seeds-from-01-audit-gold` (F.1) |

### Within 01-aat-core (61 items)

| # | source (WN line) | what | disposition |
|---|---|---|---|
| 0 | `causal-access-intro` (79) | blank-wall / LMI belongs with CIY-unified and causal-IB-LMI | **in canon**: #disc-ciy-unified-objective:83-89, #deriv-causal-ib-lmi |
| 1 | `cooperative-adversarial-intro` (57) | intro previews read as signposts, not support | → pedagogy home (raised on `item:pedagogy-home-for-lifted-audit-gold`, I.5) |
| 4 | `def-action-transition` (85) | predictive-state vs belief-state stance | → raised on *existing* `item:influx-form-agent-model-what-m-covers` |
| 5 | `def-adaptive-tempo` (97) | scalar tempo over-optimistic for anisotropic agents | **in canon**: #result-per-dimension-persistence, #deriv-matrix-persistence-condition |
| 16 | `def-chronica` (105) | RL training as a meta-agent synchronizing chronicae | → pedagogy home (raised on `item:pedagogy-home-for-lifted-audit-gold`, I.5) |
| 17 | `def-chronica` (106) | heterogeneous event rates diverge subjective time | → pedagogy home (raised on `item:pedagogy-home-for-lifted-audit-gold`, I.5); the formal seam is *existing* `item:influx-event-time-seam` |
| 27 | `def-observation-function` (83) | pragmatic vs epistemic actions in the strategy DAG | → `question:strategy-dag-epistemic-vs-pragmatic-actions` |
| 33 | `def-pearl-causal-hierarchy` (115) | watching another agent act: L1 or L2? | → `question:vicarious-interventional-access-level` |
| 36 | `def-strategic-tempo` (151) | (none beyond a shared pointer) | **set aside**: empty |
| 39 | `def-unity-dimensions` (150) | army/management rate-distortion framing lifted to #result-unity-closure-mapping | pedagogy; a pointer to its own lift. → pedagogy home (raised on `item:pedagogy-home-for-lifted-audit-gold`, I.5) |
| 43 | `der-adversarial-destabilization` (125) | tempo edge as why monopolies form | → `item:positioning-claims-from-01-audit-gold` (F.2) |
| 45 | `der-causal-hierarchy-requirement` (123) | learning-agent scope = adaptive vs robust control | → `item:positioning-claims-from-01-audit-gold` (F.2) |
| 48 | `der-causal-insufficiency-detection` (303) | Christensen's innovator's dilemma as corollary | **in canon**: #impl-strategy-structure:96, #deriv-update-detection-latency:79, :108 |
| 50 | `der-class-coercion-in-composition` (121) | Claim-A / Claim-B split read as right | reader-signal; → pedagogy home (raised on `item:pedagogy-home-for-lifted-audit-gold`, I.5) |
| 51 | `der-class-coercion-via-wrapping` (236) | preserve the $\varepsilon_{\text{track}}$ / $\varepsilon_{\text{coerce}}$ / $\kappa$ distinction | reader-signal; → pedagogy home (raised on `item:pedagogy-home-for-lifted-audit-gold`, I.5) |
| 53 | `der-deliberation-cost` (138) | CIY over-explores; EIG is the clean fix | **in canon**: #def-causal-information-yield:15, :31, :35 (distinguishability, not learning value) |
| 60 | `der-loop-interventional-access` (161) | confounded-world neurosis, patience | pedagogy for the chapter intro; → pedagogy home (raised on `item:pedagogy-home-for-lifted-audit-gold`, I.5) |
| 63 | `der-observability-dominance` (171) | communication as observability restoration | **in canon**: landed as #hyp-solicitable-escape |
| 67 | `der-recursive-update` (86) | consolidation as why agents sleep/think | → pedagogy home (raised on `item:pedagogy-home-for-lifted-audit-gold`, I.5) |
| 68 | `der-team-persistence` (156) | RL training as meta-agent (duplicate of #def-chronica's) | → pedagogy home (raised on `item:pedagogy-home-for-lifted-audit-gold`, I.5) |
| 72 | `deriv-graph-structure` (263) | correlation hierarchy belongs to def-strategy-dag | **in canon**: #def-strategy-dag:103 onward carries L0/L1/L1'/L2 |
| 75 | `deriv-persistence-cost` (183) | cooling bottleneck on AI scaling | → `item:positioning-claims-from-01-audit-gold` (F.2); aspirational |
| 81 | `disc-additive-coordinate-forcing` (154) | fourth meta-segment: theorem-import architecture | → raised on *existing* `item:proposals-sp-23-disc-theorem-import-architecture-f-a22e` (F.2), which already chose a generated view over a hand-written segment |
| 82 | `disc-additive-coordinate-forcing` (155) | Wasserstein / optimal transport as the unaddressed geometry | **covered** by *existing* `question:coordinate-forcing-geometry-forced-or-path-dependent`, which cites this very line (:155) |
| 83 | `disc-adversarial-coupling-pressure` (175) | vocabulary for information warfare / propaganda | → `item:positioning-claims-from-01-audit-gold` (F.2); aspirational |
| 84 | `disc-adversarial-coupling-pressure` (176) | peer review / double-entry as Class-1-from-Class-3 composition | in canon in substance (#disc-adversarial-coupling-pressure:72-76, "Defensive scaffolding as composition"); the "own segment" proposal it seconds lives in that segment's other Working Notes (01-other drain's surface); no ledger item found |
| 85 | `disc-ciy-unified-objective` (109) | Lagrangian / LMI / Bretagnolle-Huber homes | **in canon**: those appendix segments exist and carry it |
| 91 | `disc-credit-assignment-boundary` (212) | credit assignment vs RL TD-learning | duplicate of a non-gold Working Note in #disc-credit-assignment-boundary (01-other drain's surface); no body treatment; set aside here |
| 93 | `disc-exploit-explore-deliberate` (226) | one framework unifying RL with classical planning | → `item:positioning-claims-from-01-audit-gold` (F.2) |
| 94 | `disc-identifiability-floor` (267) | pointer to the two cross-meta proposals | duplicate pointer; see belongs#81, #82 |
| 95 | `disc-modularity-state-dynamics` (176) | M4 as institutional / political evolution theory | → `item:positioning-claims-from-01-audit-gold` (F.2); aspirational |
| 96 | `disc-modularity-state-dynamics` (178) | stray "Removed at candidate stage" line | **set aside**: residue, no content |
| 98 | `disc-separability-pattern` (146) | Eden / Fall / regaining Eden arc | → pedagogy home (raised on `item:pedagogy-home-for-lifted-audit-gold`, I.5); needs the isomorphic-not-evocative check |
| 99 | `disc-strategic-self-coupling` (201) | contracts and constitutions as $\kappa$ technologies | → `item:positioning-claims-from-01-audit-gold` (F.2); aspirational |
| 105 | `form-composition-closure` (408) | categorical cybernetics home for $\varepsilon^\ast$ | → raised on *existing* `item:spikes-proposed-advanced-15-categorical-cybernetics-re-grounding-9642` |
| 108 | `form-consolidation-dynamics` (202) | fourth coordinate-forcing layer: time | → `question:coordinate-forcing-fourth-layer-time` |
| 112 | `form-information-bottleneck` (93) | IB policy-relativity as a crack in directed separation | **in canon**: #form-information-bottleneck:50 (allocation, calibration invariant untouched) |
| 113 | `form-objective-functional` (143) | single interface as basis of the reward-hacking and self-actuation no-gos | **in canon**: #form-objective-functional:20, :102 |
| 114 | `form-strategy-complexity-cost` (212) | six-mechanism shallow-plan convergence | → `item:assemble-plan-depth-penalty-convergence` (G.2) |
| 116 | `form-structural-change-as-parametric-limit` (86) | cross-agent grafting belongs to symbiogenesis | **in canon**: #hyp-symbiogenic-composition:37 (transfer mapping); #form-structural-change-as-parametric-limit carries the within-agent half |
| 117 | `hyp-directed-separation-under-composition` (112) | (none distinct) | **set aside**: empty |
| 118 | `hyp-edge-update-via-gain` (107) | (none surfaced) | **set aside**: empty |
| 120 | `hyp-mismatch-dynamics` (110) | tempo arms race / Red Queen | → raised on *existing* `item:spikes-proposed-advanced-13-game-theoretic-formalization-of-the-m-4436` |
| 121 | `hyp-symbiogenic-composition` (153) | mitochondria as the canonical symbiogenesis instance | **in canon**: #hyp-symbiogenic-composition maps to mitochondria, Margulis cited |
| 122 | `impl-composition-machinery` (79) | representability vs optimality as the chapter headline | reader-signal; → pedagogy home (raised on `item:pedagogy-home-for-lifted-audit-gold`, I.5) |
| 123 | `impl-orient-cascade` (112) | architecture non-identifiability vs mechanistic interpretability | → `item:positioning-claims-from-01-audit-gold` (F.2) |
| 124 | `impl-strategic-composition` (101) | whole-framework synthesis; integration debt | README positioning → → pedagogy home (raised on `item:pedagogy-home-for-lifted-audit-gold`, I.5); its integration-debt half is in the main file's Off-ramp row for #impl-strategic-composition |
| 125 | `impl-strategy-dynamics` (100) | Instance 4 vs mechanistic interpretability (duplicate of #123) | → `item:positioning-claims-from-01-audit-gold` (F.2) |
| 126 | `norm-explicit-strategy-condition` (117) | triple depth penalty belongs at chain-confidence-decay | **in canon**: #der-chain-confidence-decay:56 |
| 134 | `result-mismatch-decomposition` (93) | noise floor on persistence | **in canon**: #result-mismatch-decomposition:28, :45 ("three floors") |
| 137 | `result-persistence-condition` (220) | risk-sensitive (Renyi) IB | → `question:risk-sensitive-information-bottleneck` |
| 140 | `result-structural-adaptation-necessity` (130) | latent structural diversity as the Part III gap | → raised on *existing* `item:proposals-bundle-2-section-iii-completion-cluster-50fe` (OUTLINE GAP :304) |
| 141 | `result-unity-closure-mapping` (157) | per-dimension evaluation for AI safety | **in canon**: #result-per-dimension-persistence:16, :125 (adversarial targeting of the weak dimension; scalar-metric critique cited) |
| 143 | `scope-adaptive-system` (150) | strategic ignorance vs active inference | → `item:positioning-claims-from-01-audit-gold` (F.2) |
| 144 | `scope-adaptive-system` (151) | the nested scope cascade | **in canon**: 01-aat-core/OUTLINE.md:82-94 (Part II scope lattice) |
| 145 | `scope-adaptive-system` (152) | endogenous disturbance $\rho(\pi)$ | → `question:persistence-with-endogenous-disturbance` |
| 150 | `scope-agent-identity` (107) | trajectory identity as refusal of Friston-blanket metaphysics | **in canon**: #der-directed-separation:20 (the Pearl-blanket reading) |
| 152 | `scope-ciy-observational-proxy` (92) | $\lambda$ mapping and regret-bound homes | **in canon**: #disc-ciy-unified-objective, #deriv-strategy-cost-regret-bound |
| 154 | `scope-composite-agent` (141) | C-iii maps to Miller IAM | **in canon**: #scope-composite-agent:91 |
| 155 | `scope-edge-update-causal-validity` (147) | quadruple ceiling on plan depth | → `item:assemble-plan-depth-penalty-convergence` (G.2) |
| 158 | `the-cycle-in-motion-intro` (78) | intro math previews; "any rational adaptive process must approximate" strong claim | **superseded**: the phrase is gone from the intro body at HEAD (survives only in its Working Notes line 78); the previewed quantities are defined in their own segments |
