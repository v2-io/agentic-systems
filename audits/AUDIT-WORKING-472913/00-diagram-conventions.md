# 00 — Diagram Conventions (locked 2026-05-15, cycle 472913)

Decision (Joseph, 2026-05-15): per-segment diagrams are **two-layer: concrete
anchor + structural skeleton**, serving the audit *and* doubling as drafts for
the monograph's respectful-pedagogy / mental-model-first layer. Grounded in the
`msc/diagrams-and-comprehension-survey.md` synthesis. These conventions are the
operationalization; they bind every diagram from segment 06 onward.

## The two-layer rule (CRA, survey §3.3 + concreteness-fading)

Every `NN-slug.tex` has two visually distinct panels in one figure (spatial
contiguity, survey §1.3/§3.5):

1. **Anchor (concrete).** An everyday physical/causal scene whose *structure is
   isomorphic* to the segment's load-bearing claim — the Walton-bathtub bar:
   a thoughtful non-specialist must be able to *re-derive the qualitative
   claim by perturbing the anchor*, without symbols. Evocative-only anchors
   are rejected (CLAUDE.md isomorphism rule = survey §3.4-H5 "deep not
   superficial").
2. **Skeleton (abstract).** The structural diagram (nodes/regions/flows) in
   AAT's own symbols — what cycle 472913 segments 01–05 already were.

A **fade bridge** ties them: the *same color* marks the same role in both
panels (cross-representational signaling, survey §3.5; Neurath "pictures
unite"). Anchor on the left/top, skeleton on the right/bottom, bridge between.

## Epistemic-status visual grammar (the survey gap; mirrors FORMAT.md eq-tags)

The diagram's line grammar mirrors the framework's *own* epistemic tags so a
diagram is simultaneously comprehension instrument and status visualization:

| Visual | Means | FORMAT.md correlate |
|---|---|---|
| **solid** edge/border | derived / exact — follows from priors | `*[Derived]*`, `status: exact` |
| **dashed** edge/border | formulation / canonical choice (alternatives exist) | `*[Formulation]*` |
| **dotted** edge/border | hypothesis / proposed — needs validation | `*[Hypothesis]*`, `type: hypothesis` |
| **amber, thick** + ⚑ | **auditor finding / open thread** (not the theory's voice) | n/a — the audit's overlay |
| **grey, faint** | excluded / degenerate / vacuous case | scope exclusions |

Auditor overlays (findings, THREAD-x) are *always* amber and *always* labelled
as the audit's voice, never mixed into the theory's solid/dashed/dotted grammar
— the reader must never mistake my conjecture for the framework's assertion.

## Cross-segment colour legend (strict — build the schema once, reuse ∀ segments)

`asfModel` teal = $M_t$/epistemic · `asfGoal` crimson = $G_t,O_t,\Sigma_t$/
purposeful · `asfCert` indigo = stability certificate / Lyapunov · `asfEnv`
olive = environment $\Omega$ · `asfWarn` amber = scope edge / **audit finding**
· `asfFaint` grey = excluded/degenerate. A reader walking all diagrams sees
one stable palette (expertise-reversal mitigation, survey §3.6).

## Gates before accepting a diagram

- **Caption-blind perceptual-inference gate** (survey §3.4-H2 / Step 5): cover
  the caption — can the load-bearing relation still be *seen*? If not, redesign,
  don't re-caption.
- **Perturbation/isomorphism gate** (CLAUDE.md): name one perturbation of the
  anchor; its predicted consequence must hold against the formalism.
- **Minimalism audit** (Tufte / survey §3.7): every mark carries semantic load
  or is cut. (Caption itself is retained as audit-archaeology bridge — a
  deliberate, documented exception to the expert-redundancy effect, survey
  Part VIII; for any diagram lifted to the monograph the caption is cut to
  signaling-only.)
- **Small multiples** (survey §4.2 / Tufte): dynamics segments (mismatch ODE,
  sector/persistence, orient cascade, strategy dynamics) use state→op→state
  triples, not one busy phase portrait.

## Iteration-budget calibration (locked seg 10)

Diagrams are a comprehension instrument, **not** the audit's deliverable —
research depth is the bottleneck (audit-instructions §1/§3.7). Therefore:
**max ONE refinement iteration per diagram** unless it *fails the
caption-blind gate outright* (genuinely unreadable / wrong structure). Minor
text↔box overlaps that do not destroy the perceptual inference are acceptable
for working artifacts and go on the optional end-budget retrofit list — they
do not justify a 3rd compile. Burning iterations on cosmetics is the
mechanical-completion pull the system prompt names; resist it. (Trigger:
seg-10 anchor took 3 iterations for diminishing return — skeleton was clean
after 1.)

## Retrofit note

Segments 01–05 diagrams are **v1 single-layer (pre-convention)**. Their
skeletons are sound and their anchors are implicit-but-strong (aperture / loop
/ fan-in collapse / ratchet / scope-region). They are *not* re-cut now —
re-cutting backward violates the one-at-a-time forward discipline and burns
budget. Flagged here as a known, optional end-of-budget retrofit pass; if
budget is tight they ship as v1 with this note. Two-layer standard binds 06→.
