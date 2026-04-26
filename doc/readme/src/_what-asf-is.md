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
