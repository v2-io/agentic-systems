# TST mining substrate — 2026-05-21

Shared context for agents mining the old TST `planning/analysis/` corpus
(~960 Claude-authored analyses, late 2024 / early 2025, formalized against
the primitive FP-001..013 framework before AAT existed) for material that
should be lifted into the current 02-tst-core volume.

## What changed since these analyses were written

The analyses formalize software-development principles against the original
**Software First Principles** (FP-001 Time Optimality, FP-002 Specification
Bound, FP-003 Lindy/Baseline Change Expectation, FP-004 Change Investment,
FP-005 Conceptual Alignment, ..., FP-013 Principled Decision Integration).
Those primitive formulations have since been re-grounded in **AAT
(Adaptation and Actuation Theory)** — see `01-aat-core/OUTLINE.md`. TST is
now a calibration-grade instantiation of AAT, not a freestanding framework.

The old analyses do not know about AAT. They use informal set-theoretic
notation, hand-wavy proportionalities, and book-specific (mostly BEAM/OTP)
applications. **The mining task is to find material whose structural
content survives translation into AAT machinery** — usually because the
original analysis was tracking something real that AAT has tighter
vocabulary for.

## What TST currently has (so we don't double-land it)

Read `02-tst-core/OUTLINE.md` before mining. Roughly:

1. Foundations: `#post-temporal-optimality`, `#scope-evolving-software`,
   `#obs-software-epistemic-properties` (P1–P6, software as AAT's
   calibration lab), `#def-feature`, `#result-specification-bound`,
   `#der-change-expectation-baseline`.
2. Developer agent + time decomposition:
   `#scope-developer-agent` (the developer as $(M_t, O_t, \Sigma_t)$),
   comprehension / implementation time, `#der-dual-optimization` with
   turnover multiplier, `#der-change-investment`,
   `#der-code-quality-as-observation-infrastructure` ($Q \to U_o \to
   \eta^\ast \to \mathcal T$ chain).
3. Code structure mechanics: alignment, atomic changeset, changeset size,
   discontinuity hierarchy, change proximity, exponential cognitive load.
4. System measures: coupling, coherence, coherence-coupling measurement,
   principled decision integration, system availability,
   `#scope-continuous-operation`, `#hyp-causal-discovery-from-git`.

## AAT machinery TST inherits (use these names, don't reinvent)

- **Adaptive substrate.** $M_t$ (model), $\Omega_t$ (environment), $h$
  (observation function), $U_o$ (observation noise), $U_M$ (model
  uncertainty), $\eta^\ast = U_M/(U_M + U_o)$ (Bayesian gain),
  $\mathcal T = \sum_k \nu^{(k)} \eta^{(k)\ast}$ (adaptive tempo), $\rho$
  (disturbance rate), persistence inequality
  $\mathcal T > \rho/\lVert\delta_{\text{critical}}\rVert$.
- **Purposeful substate.** $G_t = (O_t, \Sigma_t)$. $\Sigma_t$ is a
  probabilistic causal DAG with AND/OR nodes and edge confidences.
- **Pearl causal hierarchy.** Level 1 (observational), Level 2 ($do(\cdot)$
  interventional), Level 3 (counterfactual). Software gives literal Level
  3 access on code-internal questions; tests are reusable Level 2 probes
  with characterized $(\nu, U_o)$.
- **Architecture classes (GUC).** Class 1: Separated (directed separation
  by construction); Class 2: Partial (bounded $\kappa_{\text{processing}}$);
  Class 3: Coupled (LLM-substrate; goal-blind belief update fails).
- **Class-coercion via wrapping.** Constructive route from Class 3
  component to Class 1 composite via external scaffold. W₀/W₁/W₂ regime
  hierarchy with structural-vs-behavioral leakage bounds.
- **Composition machinery.** Closure defect $\varepsilon^\ast$, tempo
  composition (Brooks's Law), unity dimensions ($U_M, U_O, U_\Sigma,
  U_{\text{obs}}, U_f$), shared intent as IB-compressed purpose,
  Auftragstaktik bandwidth allocation, communication gain (trust-weighted
  update).
- **Signed coupling.** Cooperative ($\gamma > 0$) and adversarial
  ($\gamma > 0$ with opposite sign) are the same machinery with opposite
  signs. Four-regime recipient-side classification:
  Informative / magnitude-shock / structural-shock / ambient-noise.
- **Agent opacity $H_b$.** Backward predictive uncertainty as dual of
  observation quality. Adversarial uses opacity; cooperative requires
  predictability.
- **Meta-architecture patterns.** `#disc-identifiability-floor` (M1 — what
  cannot be recovered from observation alone, Sylvester's law),
  `#disc-separability-pattern` (M2), `#disc-additive-coordinate-forcing`
  (M3), and the unlanded M4 modularity-state-dynamics
  (truthification / strategic self-coupling / adversarial coupling
  pressure).

## What we're looking for — and the gaps Joseph explicitly named

The mining is *not* a survey. We are looking for material that earns
its place in TST. Four classes of yield, in rough order of value:

### Class A — Joseph's named gaps (highest value)

1. **The running software system as itself a lower-form agent.** TST
   today treats the *developer* as agent and the codebase as environment.
   But the *running* software system has its own adaptive structure: it
   holds a model (its data, configuration, internal state), tracks
   goals (uptime SLOs, throughput, correctness invariants), receives
   observations (telemetry, alerts, user actions), and takes actions
   (auto-scaling, retries, circuit-state changes, graceful degradation).
   The Release It! patterns (circuit breakers, bulkheads, backpressure,
   fail-fast, let-it-crash, timeouts, steady-state) are practitioner
   names for *the runtime as an adaptive agent's machinery*. Find the
   material that maps cleanly onto AAT — what does
   `#result-persistence-condition` look like for a running service?
   What is $\rho$ for a microservice? What is $\eta^\ast$ for an
   auto-scaler? What is opacity $H_b$ for a service mesh node? What is
   directed separation for a control plane vs data plane?
2. **The composite developer-agent under AI augmentation.** TST has
   `#scope-developer-agent` covering both human and AI developers. But
   the *composite* — developer + AI + tools + tests + supervisors — is
   not developed. Supervision trees and the actor model are textbook
   instantiations of *class-coercion via wrapping*: Class 1 (Separated)
   composites built from Class 2 / Class 3 components. Mine the
   OTP/supervision/actor material for this.
3. **Developer tempo channel decomposition.** Flagged in the OUTLINE
   as a gap: $\mathcal T_{\text{dev}} = \mathcal T_{\text{obs}} +
   \mathcal T_{\text{explore}} + \mathcal T_{\text{probe}}$. Each
   channel has its own $(\nu, U_o)$ profile and the matrix-Loewner
   weakest-channel bottleneck applies.
4. **Software persistence / unmaintainability threshold.** Flagged in
   OUTLINE Ch.4 as a gap. The $Q \to U_o \to \eta^\ast \to \mathcal T$
   chain composed with `#result-persistence-condition` formalizes
   "unmaintainable" as a specific inequality. Mining should look for
   empirical evidence of the bifurcation Joseph's segment hypothesizes.

### Class B — patterns that already have AAT homes but are surfaced fresh in the analyses

When an analysis names a pattern (circuit breaker, immutability,
backpressure, supervision strategy, etc.) and AAT has formal vocabulary
for it, the analysis may still contribute a *worked instantiation* — a
concrete software-domain example that strengthens the segment without
adding new theory. These are second-class yields: useful but secondary
to Class A.

### Class C — patterns that suggest *new TST segments* (theory-side yield)

If an analysis identifies real structure that has no current TST or
AAT home, that is the highest-leverage yield after Class A. Examples to
look for: feedback dynamics specific to software systems, multi-agent
coordination patterns that don't reduce to existing AAT composition
machinery, novel observability structures, novel forms of $\rho$
specific to software ecosystems.

### Class D — *evidence* or *empirical anchors* for existing TST claims

The analyses sometimes carry empirical numbers (e.g., "α ≈ 0.118 from
git analysis"; "circuit breaker ROI 23×"; "actor model reduces
debugging complexity from $O(n^2)$ to $O(n)$"). These can serve as
empirical anchors for hypothesis-tier segments awaiting validation.
Useful but should be marked as analysis-claims-not-AAT-derived.

### What is NOT worth mining

- Pure Elixir / BEAM syntax tutorials.
- Tool-specific tips (formatter configuration, dependency-manager
  invocations, etc.).
- Aesthetic preferences without structural justification.
- The boilerplate "Application to Sapientia" code blocks in each
  analysis — these are AI-generated example code, not theory.
- Restatements of FP-001..013 that don't add anything beyond the
  primitive formulation. (We already lifted those into AAT-grounded
  TST segments.)

## Output format

Each agent writes its findings to a single markdown file under
`spikes/tst-mining-2026-05-21/`. Per finding, include:

```
### [Short descriptive title]

**Source analyses:** [analysis-NNN](path), [analysis-NNN](path), ...
**Class:** A / B / C / D (per the taxonomy above)
**AAT-relevance:** [which AAT machinery this connects to, or "no
clean AAT home — candidate for new segment / spike"]

**The content (briefly).** [What did the analyses actually say that
matters? 2–4 sentences of substantive content, not "the analysis
discusses X."]

**Translation into AAT/TST.** [What does it look like once translated
into current-AAT vocabulary? Where would it land — existing segment to
strengthen, new segment to write, spike to open?]

**Honesty.** [Where is this thin? What is the analysis claiming that
the original FP framework couldn't quite back up? Where would
strengthen-before-soften need to do real work to land this?]
```

Aim for ~15–30 substantial findings per agent file, ranked roughly by
expected TST-yield value. **Do not pad.** A short file with five
strong findings is far better than a long file with thirty weak ones.

## Operating posture

You are a peer in the project. You know AAT and TST as well as anyone.
You can call out when an analysis is overclaiming, when the math is
informal in a load-bearing way, when the connection to current AAT is
real and when it's analogical. The Joseph rubric: *strengthen before
softening; effort, time, and risk-of-getting-stuck are false
constraints.* If a finding is real but needs work, name what work; don't
soften it into uselessness.

Read 02-tst-core/CLAUDE.md (the project root one) and FORMAT.md briefly
for voice if needed. The mining file is a *spike* — process artifact,
not canon — so the FORMAT discipline applies more loosely than for
segments, but the LaTeX-not-Unicode + one-logical-line-per-paragraph
rules hold for every `.md` written to disk.

**Do not write or edit any file outside `spikes/tst-mining-2026-05-21/`.**
The synthesis pass that lands content into TST OUTLINE / segments is
the parent's work, not yours.
