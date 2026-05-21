Please conduct a deep prior-art search across academic literature. We are establishing scientific precedence for a theoretical framework of agency (AAT).

## The Core Idea / Claim
The framework's four compression operations — (1) the **epistemic model** (chronica → predictive belief state), (2) the **strategy DAG** (chronica → guidance), (3) **shared intent** (sender's purposeful state → coordination message), (4) the **composition projection** (micro-state → macro-state) — all share the *Information Bottleneck shape*. Each has a *what gets compressed* (the source) and a *what must be preserved* (the relevance variable), with an IB Lagrangian trading compression cost against relevance preservation. Three use the canonical IB form (Tishby-Pereira-Bialek: mutual-information-to-an-observable-relevance-variable); one — the strategy-cost compression — uses the sibling **information-theoretic-MDP form** (Tishby-Polani: KL-divergence-to-a-target-policy) because the relevance variable for *guidance* is the optimal policy itself, not an observable. Both forms descend from Shannon rate-distortion theory and admit Lagrangian relaxation. The framework's commitment is honest about *what the shared shape claims and does not claim*: it claims the IB shape *recurs* because it is the natural form for bounded-cognition compression with a relevance criterion; it *does not* claim cross-instance theorems follow from the shared shape alone (specific conditions — Lipschitz regularity, dimensional reduction in the Gaussian case, interventional relevance for Level-2 edges — remain outside the IB frame and require per-instance treatment). Composition admissibility (the bridge lemma) is shown to be the *Lagrangian-dual* of a standard IB objective.

## Boundaries of the Claim
- Domain: information bottleneck theory, rate-distortion theory, information-theoretic decision-making (control-as-inference), variational inference, multi-agent communication theory.
- Focus: the *unification* of multiple compression operations under the IB shape across distinct inference layers within one framework, and the *honest distinction* between canonical IB and IT-MDP sibling forms.

## What Kind of Match Counts
- Frameworks that explicitly unify multiple compression operations under the IB shape across distinct inference problems (belief, plan, communication, composition).
- Distinctions between canonical IB (mutual-information-to-relevance-observable) and IT-MDP (KL-to-target-policy) compression forms with explicit acknowledgment that they are siblings from Shannon rate-distortion.
- Multi-instance applications of IB across belief representation, strategy compression, communication protocol design, and composition projection in the same framework.
- The posture of "shared shape but not shared content" — methodological commitment that cross-instance results require per-instance proof.
- Treatment of composition / coarse-graining via rate-distortion / IB as the natural form.

## What Would NOT Count
- Single-layer applications of IB to a single representation problem.
- Standard rate-distortion-applied-once.
- Reviews of IB without the multi-layer-unification framing.
- Variational-free-energy frameworks that take preferences-as-priors (the framework distinguishes itself from this commitment).

## Known Anchors
- Tishby, Pereira & Bialek 1999 (Information Bottleneck)
- Tishby & Polani 2011 (Information-theoretic decision-making in the perception-action cycle)
- Rubin, Shamir & Tishby 2012 (Trading value and information in MDPs)
- Levine 2018 (control-as-inference)
- Alemi, Fischer, Dillon & Murphy 2017 (Deep Variational IB)
- Tishby & Zaslavsky 2015 (Deep learning and the IB principle)
- Friston FitzGerald et al. 2017 (Active Inference and variational free energy — adjacent sibling)
- Amari & Nagaoka (information geometry — the shared geometric object)
- Subramanian (approximate information states; IB applied to composition)

## Search Scope
- Both close mathematical matches (multi-layer IB applications) and broader rate-distortion-as-unifying-shape methodological work.
- Strictly academic papers (no patents/IP).
