# ACT Development Roadmap

## Current Approach (March 2026)

**The theory lives in `src/` as numbered claim segments.** Each file is one
claim — axiom, definition, theorem, hypothesis — following TST's cadence (one
claim per section, sentence summary, formal expression, discussion) with TFT's
epistemic system (equation-level tags, document-level epistemic status,
claim tiers from TF-00).

**`src/000-contents.md`** is the master outline — the whole proof in plain
English. It maps ~75 claims across five progressively scoping sections.
Numbers count by 10s to allow insertion; slugs in YAML frontmatter are the
stable cross-references.

### Why This Structure

The earlier approach (ACT-01 through ACT-12 as chapter-style documents) was
replaced because:
- TST's cadence is superior: each section is one quick claim, summarizable in
  a sentence, building strictly on prior ones. Not textbook chapters.
- Individual claims can be written, reviewed, and evolved independently
- Gaps between claims are visible and honest
- The structure accommodates evolution from both directions: general theory
  pushing toward domain instantiation, and domain-specific results pushing
  requirements back up
- Cross-referencing by slug (`#temporal-optimality`) is more stable than by
  document number

The existing ACT-01.md and ACT-03.md are working documents whose content is
being decomposed into individual claim segments in `src/`.

---

## What's Established

**Adaptive systems foundation** (from TFT, subsumed by ACT):
Well-developed. TF-00 through TF-11 plus appendices A-G. Maps to Section I
of the contents (~20 claims, 010–200). Simulation battery (6 variants) has
characterized the empirical landscape:

- *Appendix A (Lyapunov/sector conditions)* is the formal backbone — general,
  nonlinear, robust. Primary, not the linear ODE.
- Under stochastic disturbances, adversarial exponent is 3/2 (not 2).
  Under deterministic drift, it IS 2. The linear ODE is correct in its
  regime but not general.
- Observation quality gates tempo advantage (U_o collapses exponent).
- Scalar tempo is poor for anisotropic systems (per-dimension condition exact).
- TF-06's gain principle validated (52% mismatch reduction).

**Purposeful agency** (ACT's novel contribution):
Maps to Section II (~15 claims, 210–350). Core structure identified (AND/OR
nodes, single-parameter edges, Orient cascade, directed separation, O_t/Σ_t
split). This section has the most gaps — strategy tempo, action-deliberation-
exploration tradeoff, cognitive cost of Σ_t, mismatch interaction ordering.

**Multi-agent / adversarial**:
Maps to Section III (~10 claims, 400–475). Adversarial results are solid
(from simulations). Cooperative dynamics (shared intent, intent decomposition)
are sketches.

**Software domain**:
Maps to Section IV (~25 claims, 500–698). TST's 12 theorems + via-tft
insights provide the content. Needs regrounding with ACT formalism and
TFT-style epistemic tags. The strongest claims: T-02 (specification bound),
T-04 (Bayesian baseline), code quality as observation infrastructure.
Weaker claims (T-08 proportionality, T-09 exponential proximity) are
hypotheses labeled honestly.

**Agentic systems**:
Maps to Section V (~5+ claims, 700+). Conceptual (100% context turnover,
M_t preservation). Agentic-tft corpus (../agentic-tft/) has substantial
thinking not yet integrated.

### Segment Files Written

- `src/010-temporal-optimality.md` — Axiom. The first claim.
- `src/180-persistence-condition.md` — Theorem. Key result from TFT.
- `src/530-specification-bound.md` — Derived. TST content regrounded.

These establish the cadence: sentence summary → formal expression with
equation-level tags → epistemic status paragraph → discussion → connections
with forward references explicitly marked.

---

## Key Decisions

- ACT supersedes TFT (not "extends")
- Theory structure: numbered claim segments in `src/`, not chapter documents
- TST cadence + TFT epistemic system as the combined standard
- AND/OR + single-p edges (drop WEIGHTED)
- Sector-condition framework primary (linear ODE pedagogical)
- O_t / Σ_t split (not G_t); point-valued G_t superseded — **under
  reconsideration**: theoretical spike (March 2026) explores whether G_t
  as a singular abstract purposeful state can be derived from first
  principles, with O_t/Σ_t emerging when goal-model complexity demands it
- Multi-agent is main content, not appendix
- Correlated observations as default
- TST gets full treatment in Section IV (not just domain table rows)
- T-01 (temporal optimality) generalized as ACT's first axiom (#010)
- Slugs as stable cross-references, not file numbers
- Every claim must be grounded — flag ungrounded assertions honestly

---

## Governing Objectives (March 2026)

The overarching goal is a unified theory — ACT — that:

1. **Subsumes TFT as the adaptive-systems foundation.** TFT's formal
   machinery (mismatch, gain, tempo, persistence, Lyapunov stability) is
   the engine. The sector-condition/Lyapunov framework (current Appendix A)
   becomes the *primary* formal path; the linear ODE becomes a pedagogical
   appendix. TFT is not extended — it is *absorbed*.

2. **Derives purposeful agency from first principles.** Start with the
   simplest possible abstract purposeful object (like M_t for reality
   models) and derive the need for richer structure (subgoals, DAGs,
   strategy representation) from mathematical necessity — specifically,
   from the causal hierarchy theorem's proof that interventional reasoning
   requires causal structure beyond predictive models. The O_t/Σ_t split,
   the AND/OR DAG, the three mismatch types should *emerge* from this
   derivation, not be assumed.

3. **Makes TST a rigorous software-domain instantiation of ACT.** TST's
   practical insights are preserved but regrounded: every claim gets TFT's
   epistemic tagging, every ungrounded assertion is either derived from ACT
   primitives, retagged as hypothesis/empirical, or removed. Causal
   modeling (Pearl's hierarchy, do-calculus, identifiability) is introduced
   where software's unique epistemic properties permit.

4. **Develops multi-agent dynamics to the degree needed for TST grounding.**
   Cooperative, adversarial, and mixed coupling. Shared intent. Team
   persistence. Not a complete multi-agent theory, but enough to ground
   software teams, adversarial dynamics, and the trust meta-model.

5. **Maintains the claim-segment structure throughout.** TST's cadence
   (one claim per section, strictly incremental) combined with TFT's
   epistemic conventions. Claims fill from both directions: general theory
   pushing toward domain, and domain results pushing requirements back up.

## What's Next (Priority Order)

1. **Derive purposeful agency from first principles (Section II)** —
   this is the hardest, most novel, and most important work. Start with
   an abstract purposeful state G_t, show where simple forms break, derive
   the need for causal/DAG structure from the causal hierarchy theorem.
   The three-mismatch-types, directed separation, and orient cascade
   should follow from this derivation. Current theoretical spike in
   `scratch/spike-purposeful-agent-derivation.md`.

2. **Review and refine Gemini drafts (src/160, 170, 190)** — these are
   uncommitted first drafts establishing three Section I claims. Need
   review for: consistency with cadence, appropriate scope (190 may bundle
   too much Section III material), and cross-reference accuracy. Break up
   and update `src/000-contents.md` as needed.

3. **Write remaining Section I segments** — definitions (020–050) and
   remaining mismatch/gain claims. These map closely from TFT. Low risk,
   high leverage for establishing the foundation.

4. **Write Section IV segments** — TST content regrounded in ACT. This
   surfaces which ACT claims the software domain depends on, pushing
   requirements back up into Sections I–III.

5. **Develop Section III to the degree needed** — multi-agent dynamics
   sufficient for TST grounding (team persistence, adversarial coupling,
   shared intent basics).

6. **Consolidate simulation results into Appendix B** — evidence base.

7. **Section V** — agentic systems. Draw from agentic-tft corpus.

---

## Context for Future Agents

**Start with `src/000-contents.md`** — this is the map. It shows every claim
we think we need, which ones are written, and where the gaps are.

**The epistemic standard is TFT's, not TST's.** Every equation gets an inline
tag (`*[Definition]*`, `*[Derived]*`, `*[Hypothesis]*`). Every segment file
gets an Epistemic Status paragraph explaining what's derived vs hypothesized
vs discussion-grade. See `priors/tft/TF-00.md` for the full conventions and
`priors/tft/TF-05.md` for a good example of the cadence.

**Every claim must be grounded.** If something is stated as fact, it needs
its own derivation or explicit grounding. Flag empirical observations that
aren't derived from the formalism. TST had some fluff ("Every enduring best
practice reduces future time") that must not transfer uncritically. The
fungibility argument for temporal optimality IS important, but assertions
about "what best practices do" require their own grounding.

**The contents file is a working draft.** Expect the ordering, numbering,
and even which claims exist to evolve. Slugs are the stable references.
Gaps will fill from both directions.

**Existing chapter-style documents** (ACT-01.md, ACT-03.md) contain sound
content that is being decomposed into `src/` segments. Don't extend those
files; create new segments in `src/` instead.

**What carries over from TFT mostly unchanged**: TF-02 (causal structure),
TF-04 (event dynamics), TF-05 (mismatch, Prop 5.1), TF-06 (gain), TF-10
(structural adaptation, Prop 10.1), Appendix A (Lyapunov). The math is
sound; what changes is framing and atomization into claims.

**TST integration**: Strongest claims (T-02, T-04) are genuinely
well-grounded. "Code quality as observation infrastructure" from via-tft is
the most valuable novel insight. Weaker claims (T-08, T-09) need honest
epistemic tags. T-01 is generalized as ACT's first axiom.

**Agentic-tft corpus** (../agentic-tft/ docs 00-14): Cognitive loop spec,
evaluation framework, crèche, narrative circle. Relevant to Section V but
not yet integrated.

---

## Open Questions

1. Does IB for shared intent produce non-obvious predictions about
   organizational communication structure?

2. Can the intent DAG handle temporal dependencies (action ordering)?

3. How does 100% context turnover interact with the intent DAG? O_t and
   Σ_t may survive context death even when M_t doesn't.

4. Is there a derivable "comprehension vs action" optimal allocation from
   the dual-mismatch framework?

5. Can Hafez's P be derived from ACT quantities? Can ΔH (strategic
   legibility) enter multi-agent adversarial dynamics?

6. Relationship between ACT and active inference's prior preferences?

7. Which physical domains have deterministic vs stochastic ρ?

8. Cognitive cost of maintaining Σ_t (the β analog for strategy).

9. DAG acyclicity scope — modeling assumption, not structural necessity.

10. δ_strategic formalization — the least crisp of the three mismatch types.

11. Whether "code quality as observation infrastructure" is unique to
    software or an instance of a general pattern (agents modifying their
    own observation channels).

---

## Ungrounded Claims to Resolve

*Claims made or implied in current documents that lack their own derivation.
These need to be either grounded, retagged as hypotheses, or removed.*

- "Every enduring best practice reduces future time" (was in 010, removed)
- "Principled implementation often costs nearly the same as quick" (TST T-06,
  empirical observation not derived — flagged in contents)
- "Comprehension dominates under high turnover" (TST T-05 implication,
  structurally motivated but quantitative relationship unformalized)
- "Code complexity accumulation rate" as instance of ρ (needed to connect
  persistence condition to software maintainability — flagged in contents)
- The virtuous/vicious cycle as persistence condition violation (structurally
  motivated, not formally derived)

---

## Validation (after theory stabilizes)

- Extend nonlinear sims to characterize regime boundaries
- Developer-as-ACT-agent on real codebase (software worked example)
- Test DAG health metrics against real project outcome data
- Multi-agent intent propagation simulation
- TST testable predictions: specification bound calibration,
  coherence-coupling measurement, temporal ordering in fine-tuning
