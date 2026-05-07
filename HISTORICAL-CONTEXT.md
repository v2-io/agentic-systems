# Historical Context, Position & Lineage

The long-form positioning document for the Agentic Systems Framework (ASF). The README's *Position & Lineage* section is a four-paragraph distillation of this material; the substance lives here.

This document covers what the framework is at the level of distinctive contribution, the multi-decade arc of partial unifications it joins, where it differs from contemporary peer frameworks (active inference, IBM's systems-theory call, Hafez's bi-predictability work, Miller's coevolving automata, others), and how the work itself developed.

---

## What ASF Is

At the level of *integration*, ASF connects four mature disciplines under a common formalism: control theory's stability machinery (Lyapunov, contraction analysis, monotone operators), causal inference's interventional reasoning (Pearl's hierarchy, identifiability theory), information theory's compression and channel-capacity arguments (Shannon rate-distortion, the information bottleneck), and agent architecture's structural decomposition (modular vs coupled processing topologies). These are the substrate.

At the level of *distinctive contribution*, ASF is an **epistemic architecture for bounded correction under decomposed disturbance** — a way of organizing the conditions under which the integrated machinery's results actually apply. Three structural moves carry most of the load:

**Scope-honesty as architecture, not annotation.** Scope conditions and operational limits are made visible at the segment level rather than buried as caveats. Each segment names what it depends on, what it claims, and where it ceases to apply. The framework's conservatism is what makes its results compose; an integration that overclaimed and then silently retreated would be much weaker than one that names its scope up front.

**Three cross-cutting meta-patterns** that name the theory's positive, negative, and constructive halves:

- A *separability pattern* — where AAD can decompose problems into a separable core, where it has structured repair for partial decomposability, and where the general case remains open.
- An *identifiability-floor pattern* — structural no-go results drawn from external information-theoretic theorems naming what *cannot* be identified from observational data alone, and what unique escape AAD's interventional machinery supplies in each case.
- An *additive-coordinate-forcing pattern* — places where AAD-internally-motivated additivity axioms force the natural coordinate to be logarithmic at multiple layers (chain confidences, divergences between distributions, edge update rules, the metric on the parameter manifold).

**Software as the privileged calibration laboratory.** Software is treated not as the "best operationalization domain" but as the specifically high-identifiability laboratory in which AAD's quantitative machinery can be most cleanly grounded — where edge interventions can sometimes be literally interventional (tests, deploys, `git bisect`), where the chronica is partially exteriorized with cryptographic immutability over its committed subset, and where causal structure is partially declared rather than inferred. Other domains inherit AAD's machinery under explicitly named transfer assumptions, not by direct equivalence. This makes overclaim under domain transfer structurally hard to commit accidentally.

The integration *is* the substrate; the epistemic architecture is what makes the integration distinctive rather than reducible to its parts. Reading the framework through both lenses tends to be more productive than reading it through either alone.

---

## A field-level need, articulated repeatedly

The case for a unifying agentic-systems theory has been made across several decades from multiple directions, and was renewed explicitly by Miehling et al. in their 2025 ICML position paper *"Agentic AI Needs a Systems Theory"* (arXiv:2503.00237). That paper's argument is that the field's focus on individual model capabilities — measured in isolation, evaluated against task-bounded benchmarks — systematically underestimates both the true capabilities and the emergent risks of agents acting in the world. It advocates a systems-theoretic perspective covering agent-environment, agent-agent, and agent-human dynamics together; introduces a working definition of *functional agency* (action-toward-objective + outcome model + adaptation of the model); and characterizes agency as a spectrum along three axes (action generation, outcome model, adaptation). The paper is, by design, a call rather than a developed theory.

The Agentic Systems Framework (ASF) reads as a substantive answer to that call. The convergence is more interesting than direct response would be: the work that became ASF (originally Temporal Feedback Theory and Temporal Software Theory; see *How this work developed* below) had independently arrived at substantially the same diagnostic — that adaptive-purposeful agency required mathematical dynamics rather than capability checklists — and had developed the formal apparatus for it before the IBM paper was encountered. The functional-agency three-condition definition and the spectrum framing map directly into ASF's existing agent-class hierarchy; ASF adopts both as cross-references rather than as derivations. Convergent independent development of the same diagnostic across separate research efforts is itself signal that the field-level need is real.

---

## The longer arc

The arc this work joins runs through several decades of partial unifications, each contributing machinery the present synthesis still relies on:

- **Cybernetics** (Wiener 1948 *Cybernetics*; Ashby 1956 *Introduction to Cybernetics*; Conant & Ashby 1970 "Every Good Regulator of a System Must Be a Model of That System") — the original feedback-loop tradition, establishing that goal-directed behavior in any substrate (mechanical, biological, social) shares a common control-theoretic shape. Hafez et al.'s 2026 paper restates this lineage explicitly, and ASF inherits its event-driven cycle framing from the same root.
- **Control theory** (Lyapunov; Kalman 1960; Khalil 2002 *Nonlinear Systems*; Lohmiller & Slotine 1998 contraction analysis; Rockafellar 1970 / Bauschke & Combettes 2017 monotone-operator theory) — the quantitative stability machinery that underwrites ASF's persistence condition, sector machinery, and Section III contraction template.
- **Bounded rationality and decision theory** (Simon; Russell & Norvig agent classes; Bratman BDI architecture) — the recognition that real agents reason and act under resource and information constraints, and the architectural vocabulary (belief / desire / intention) that ASF's $G_t = (O_t, \Sigma_t)$ split shadows in formal terms.
- **Causal inference** (Pearl 2009 *Causality*; Bareinboim et al. 2022 Pearl-hierarchy formalization including the Causal Hierarchy Theorem) — the interventional / counterfactual distinction that ASF uses to derive what's identifiable from observational data and where structural identifiability floors lie.
- **Information theory** (Shannon rate-distortion; Tishby, Pereira & Bialek 1999 information bottleneck; Tishby & Polani 2011, Rubin et al. 2012, Levine 2018 information-theoretic MDPs) — the compression-and-channel-capacity machinery that grounds ASF's strategy-cost and observation-channel results.
- **Active inference and the free-energy principle** (Friston 2010, 2017, 2019, 2023; Da Costa et al. 2020; Sajid et al. 2021; Parr & Pezzulo 2022) — the most comprehensive recent attempt at a unifying agentic theory, and the framework with which ASF has the deepest principled engagement.
- **Coevolving automata and SFI complexity** (Miller 2022 *Ex Machina: Coevolving Machines and the Origins of the Social Universe*) — the constructive tradition for emergence of agentic structure from simple interacting components.
- **Information-theoretic measurement of agency** (Hafez et al. 2026 *A Mathematical Theory of Agency and Intelligence*) — recent work positing bi-predictability as a substrate-independent diagnostic.

Each of these contributes adopted machinery to ASF; the framework's contribution lies in their integration plus the epistemic-architecture moves described above.

---

## Where ASF differs from contemporary peers

A small number of contemporary frameworks are pursuing related aims. ASF's relationship to each is worth naming explicitly — both for honest credit and because the differences point at what each contributes that the others do not.

### Active inference and the free-energy principle

ASF and active inference share substantial machinery: both use Bayesian agents, both formalize action-perception loops, both connect epistemic and instrumental drives, and both can be cast as compression problems. They diverge on what is foundational. Active inference begins from a single optimization principle (minimize variational free energy / maximize Bayesian model evidence) and recovers perception, action, and learning as cases. ASF begins from operational requirements on a feedback-coupled adaptive system — the persistence template, causal access via the loop, directed separation as architectural classification — and uses information-theoretic compression as one modeling move rather than as the master objective. ASF treats objectives as value functionals on trajectories rather than encoding preferences as priors over outcomes, sidestepping the "dark room" objection (Sun & Firestone 2020). On scope: Aguilera et al. (2022) showed that the FEP-flow stability argument applies in a narrower parameter regime than typically claimed; ASF's sector-Lyapunov machinery makes the standard control-theoretic claim and applies wherever the sector and tempo conditions hold. On agent identity: Bruineberg et al. (2022) distinguish "Pearl blankets" (statistical conditional independence, well-defined) from "Friston blankets" (metaphysical, overrunning the formalism); ASF's directed-separation classification (Class 1 / Class 2 / Class 3) is a Pearl-blanket move with explicit scope honesty rather than a Friston-blanket move.

A constructive observation worth recording: ASF's survival Lagrangian $\mathcal L_\text{AAD}(a) = \mathbb E[Q_O(a)] + \text{Tr}(\Lambda \cdot \mathcal I_o(a))$ — derived from the matrix-form Causal-IB result (`#deriv-causal-ib-lmi`) — *recovers* the standard Expected Free Energy functional under three explicit structural restrictions: (i) collapsing $Q_O$ to a log-prior over outcomes (the dark-room collapse, which loses the satisfaction-gap / control-regret diagnostic); (ii) replacing the directional matrix shadow price $\Lambda$ with a scalar isotropic price $\lambda I$ (which forces uniform information-seeking and loses the targeted-exploration property); (iii) treating the action-outcome map as associational rather than interventional (which collapses Pearl Level 2 to Level 1 and loses the causal-insufficiency-detection content). This is candidate-formulation grade rather than a dominance theorem — sophisticated active-inference variants include epistemic value and richer generative models, and the comparison applies cleanly only to default forms — but it makes precise *which architectural commitments* separate the two frameworks. The full derivation is in `spikes/spike-fep-suboptimal-approximation.md`.

The full per-mapping audit (28 concept comparisons; 5 clean / 12 partial / 7 divergent / 4 no-fit) lives in `spikes/spike-active-inference-vs-aad.md`. ASF treats active inference as a *neighboring theory with shared machinery and divergent foundational stance* — not as a parent and not as a competitor, but with a precise account of where the divergent commitments leave each framework's reach.

### IBM 2025 (Miehling et al., functional agency and systems theory)

ASF takes IBM's call at face value and adopts the functional-agency three-condition characterization and the agency-as-spectrum framing directly into the agent-class hierarchy. Where IBM names the questions, ASF develops the mathematics. The convergence on the same diagnostic from independent starting points strengthens both projects' positioning.

### Hafez et al. 2026 (*A Mathematical Theory of Agency and Intelligence*)

Hafez introduces *bi-predictability* $P$ — the shared fraction of information across observations, actions, and outcomes relative to the loop's total informational budget — and proves regime-dependent bounds: $P \leq 1$ attainable in quantum interactions; $P \leq 0.5$ classically; lower once agency (action selection introducing internal degrees of freedom) is introduced. The paper distinguishes *agency* (capacity to act on predictions) from *intelligence* (additionally learning from interaction, self-monitoring effectiveness, adapting the scope of observations / actions / outcomes), and validates the bounds in physical (double-pendulum), reinforcement-learning, and multi-turn LLM systems. The empirical headline — an Information Digital Twin monitoring $P$ in real time detected coupling degradation at substantially higher accuracy than reward-based baselines — is independent confirmation that loop-structural diagnostics outperform task-performance proxies. ASF's relationship to Hafez is *complementary*: Hafez supplies a substrate-independent diagnostic metric whose dynamics ASF predicts; ASF supplies the goal-and-strategy machinery that Hafez explicitly does not address ("what is the coupling for?"). A separate Hafez paper introducing the backward-predictive-uncertainty measure $H_b$ feeds Section III's agent-opacity work; cross-mapping work and the bridge simulations live in `spikes/spike-hafez-integration-audit.md` and `_obs/02-prior-art-assessment.md`.

### Miller 2022 (*Ex Machina*, Coevolving Automata Model)

Miller and the broader Santa Fe Institute complexity tradition supply constructive mechanisms for composition dynamics — the extreme transition motif (pre-transition / neutral drift / niche creation / cascading displacement / consolidation) for structural change in populations; the meta-machine as exact composition algebra for two-Moore-machine product automata; the ICE threshold (≥2 states + ≥2 rounds for social behavior); and Table 12.2's exact enumeration of behavioral possibilities at each complexity level. Several of Section III's named GAPs (latent structural diversity, endogenous coupling, composition transition dynamics, computational thresholds for social behavior) explicitly point at Miller as the source for the mechanisms ASF is missing. The relationship is genuinely complementary: ASF provides the persistence, identification, and contraction machinery for analyzing composite agents; Miller provides the dynamics by which such composites come to exist, restructure through neutral drift, and undergo phase transitions. Bridge work in `spikes/spike-miller-act-bridge.md`.

### Baigozin 2025 (the GAA framework)

A recent adjacent attempt at adaptive-systems formalization. Used in 2026-04 as a comparative-framework reading that prompted six new ASF segments to land via a brainstorm cycle (`#deriv-critical-mass-composition`, `#der-interaction-channel-classification`, `#form-consolidation-dynamics`, `#deriv-persistence-cost`, `#deriv-adaptive-gain-dynamics`, `#deriv-detection-latency`); see CHANGELOG.

### OODA loop (Boyd) and military / decision-cycle traditions

Boyd's Observe-Orient-Decide-Act framing predates much of the academic literature and remains the most widely-recognized informal statement of the adaptive cycle. ASF's five-phase Greek vocabulary (prolepsis / aisthesis / aporia / epistrophe / praxis) is partly a response to OODA's flatness — the formal cycle makes distinctions OODA collapses (anticipation vs perception; mismatch detection vs gain-weighted correction; the orient cascade's structural ordering of model / strategy / objective revision).

---

## How this work developed

ASF developed bottom-up rather than top-down. The starting observation, accumulated across separate research threads from late 2025 through early 2026, was that essentially the same cycle structure was recurring across very different domains: software-development workflows, organizational dynamics, biological control systems, language-constituted agents, cognitive architectures. The first formalization effort was *Temporal Software Theory (TST)* — a corpus of empirical and conceptual work on software development as an agentic domain, accumulated since August 2025 — followed by *Temporal Feedback Theory (TFT)*, which extracted the adaptation-specific machinery as standalone mathematics. Adjacent work on PROPRIUM (an architecture-of-identity ontology, early 2026) and on the geometric structure of epistemic states in language models (CMCL submission, January 2026) brought in considerations of agent identity and language-as-medium that the original mathematics did not have to address.

The agentic-systems repository was founded in March 2026 (initially under the name Agentic Cycle Theory, renamed to AAD in April 2026 to resolve a collision with "AI Consciousness Test" in the AI welfare literature). What had begun as cross-domain pattern-matching turned out, once formalized, to generate substantial additional results that had not been visible at the level of the informal patterns: acyclicity of strategy graphs forced by temporal ordering rather than assumed; the Markov property derived from causal sufficiency via the CMC theorem rather than postulated; the satisfaction-gap / control-regret decomposition; the identifiability-floor pattern naming structural no-go results from external information-theoretic theorems and the unique escapes AAD machinery supplies; the additive-coordinate-forcing pattern showing AAD's coordinate choices at four distinct layers all sit on a single underlying geometric object; the composition bridge lemma; the contraction template generalization. None of these were design goals; they fell out of working through the formalism with care.

This is the order the work belongs in: the patterns came first and motivated the synthesis; the formalism then disciplined the patterns and produced new structure beyond what the informal observations had captured. The framework's distinctive epistemic architecture (described above) is the structural shape that emerged from the discipline, not a starting design choice. The convergent independent arrival at the same field-level diagnostic — ASF's via cross-domain pattern-matching, IBM's via systems-theoretic critique of capabilities-centric AI development, Hafez's via thalamocortical-inspired information-theoretic measurement — is itself one of the strongest signals that the underlying need is real.
