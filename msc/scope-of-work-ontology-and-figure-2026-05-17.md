# Scope-of-Work: Agent Ontology Verification + Vol-1 Introduction Figure

**Working artifact — 2026-05-17.** Design + verification trail for the Vol-1
*Introduction* "Scope of work" section and its figure. This is `msc/`
working substrate (process voice, dated, contingencies marked) — not a
segment, not auditor-safe. Future-me / future-agent / Joseph readable.

**Epistemic key used throughout:**

- `[CANON ✓]` — verified against the current canonical segments/LEXICON this session.
- `[DECIDED]` — Joseph's decision this session (binding for this work).
- `[SYNTH ?]` — my synthesis/reading; plausible, to be checked, not yet verified.
- `[WF-PENDING]` — contingent on the cold WF-strengthening spike
  (`spikes/spike-self-actuation-grounding.md` is WF-BLOCKED; a strengthening
  spike is running). Do **not** build on these until it resolves.
- `[OPEN]` — a genuine unresolved tension in the canonical material itself.

---

## 1. Task and provenance

**Goal.** A "Scope of work" section in the AAT Vol-1 *Introduction*
(`01-aat-core/INTRODUCTION.md`, transcluded via `![[INTRODUCTION]]`),
centered on one figure — a "map" of the systems ASF covers in general and
AAT in particular.

**Starting point and its status.** `[CANON ✓]`
`msc/domain-unification-2026-05-04/recommended-agent-ontology.md` and
`doc/DOMAINS.md` are a **matched pair of the same 2026-05-04 pending
proposal** — DOMAINS.md is the worked-examples sheet of that same proposal
("Working draft, exploratory"), *not* independent corroboration. Verifying
one means updating both. **DOMAINS.md is explicitly queued next, after this
hierarchy work** (Joseph) — carry the reconciliation notes here forward so
that task starts warm. `disc-continuity-stance` Working Notes already
reference the recommended-agent-ontology proposal as "active
reconsideration, pending Joseph" (tracked
`msc/naming/mini-lexicon-todo.md §13.11`) — i.e. the canonical segments are
*waiting on* this proposal's adjudication; it is not stale drift, it is a
live Joseph-pending fork the theory itself points at.

## 2. The verified canonical structure

`[CANON ✓]` **The spine is three coexisting *views*, not one ladder.** This
is the load-bearing finding for the figure:

1. **Nested formal scopes** (the actual formal spine): `#scope-adaptive-system`
   ⊃ `#scope-agency`, then the `#form-complete-agent-state` lift to
   $X_t=(M_t,G_t)$.
2. **LEXICON definitional narrowing chain** (6 steps): Adaptive system →
   Agentic system → Actuated agent → Self-actuated agent → Logogenic agent →
   ELI. This *does* ground the proposal's "Semantic Tier" spine — the chain
   is real, presented as progressive narrowing in LEXICON.
3. **`#def-agent-spectrum`: a 2×2 continuum** (model-richness ×
   objective-richness), explicitly *"regions of a continuum, not discrete
   categories"* (Reactive / Adaptive-tracker / Blind-pursuer / Actuated).

`[CANON ✓]` **Consequence for the figure.** A stepped pyramid encodes a
*total order*. The verified structure is a **partial order** containing a
genuine 2×2 plus orthogonal activation-gated axes. A pyramid would actively
misrepresent the theory — this is a correctness concern, not a stylistic one.

## 3. Joseph's decisions (binding for this work)

- `[DECIDED]` **Continuity-stance: keep orthogonal + empirical overlay.**
  Preserve the stronger orthogonality claim (canonical, load-bearing in
  `#disc-continuity-stance`); show tier-gating as an *overlay*, not a
  demotion. Note: the overlay turns out to be **derivable, not merely
  empirical** — see §5 / `[WF-PENDING]`.
- `[DECIDED]` **Tier-4: strict-narrowing + formalize Self-actuated now.**
  Canonical has no Tier-4 branching; `#self-actuated-agent` is a
  *reserved, unformalized* boundary. The proposal's "ladder branches at
  Tier 4 (humans/biology as separate lineages)" is a draft invention with
  no canonical backing — rejected. Instead: keep the strict narrowing and
  *actually formalize* the self-actuation operator. (This is what the
  self-actuation spike + the WF-strengthening spike are doing.)
- `[DECIDED]` **Figure form: bespoke spine + gated orthogonal axes.** Not a
  stepped pyramid (misrepresents — §2). A central narrowing spine with
  orthogonal axes drawn as rails that "switch on" at the tier where they
  become meaningful, and the model×objective 2×2 shown where it lives.
- `[DECIDED]` **The figure is a mental-model scaffold of the theory's
  *rhythm*.** Simplifying liberties are allowed, but it must be
  **isomorphic, not merely evocative** (project respectful-pedagogy honesty
  constraint: a reader perturbing the scaffold must get predictions that
  hold against the formalism). Lead with the mental model (Layer-0
  "preamble to the preamble"), then the precise structure.
- `[DECIDED]` **Organizing lens.** *"Primarily interested in the places
  where the scope refinement gives us a new capability and/or
  name/adjective for the agents under study."* → walk the narrowing spine;
  at each boundary name (a) the new **capability** the refinement unlocks
  and (b) the new **adjective** the agent earns. Orthogonal axes are
  precisely the places where an *activation* (not a narrowing) confers a
  new adjective. **Boundaries that buy neither a capability nor a name are
  not worth a box.**
- `[DECIDED]` **Colors: sample from the cover-page SVG**
  (`01-aat-core/AAT-cover.svg`), staying in the same saturation+lightness
  family.

## 4. Figure rendering constraint (verified — affects format choice)

`[CANON ✓]` General image rendering through the markdown-first pipeline is
**not implemented** — only the *cover* SVG has a render path
(`rsvg-convert` → single-page PDF → `\includepdf`). `FORMAT-TODO.md:205`
lists a general "Dependency-graph SVG → PDF pipeline for image rendering"
as wanted-but-unbuilt; the OUTLINE's existing `![...](src/img/*.svg)`
references carry an author comment that they do not yet render.

`[CANON ✓]` **Cover palette (extracted 2026-05-17 from `01-aat-core/AAT-cover.svg`,
cross-checked vs `AAT-cover-master.svg`).** A cool blue-slate family, low-to-mid
saturation — use these as the TikZ `\definecolor` set so the figure sits in the
cover's saturation+lightness family (Joseph's instruction):

- Deepest accent: `#235a7d` (deep teal-blue) — reserve for the strongest
  emphasis (e.g., the spine's terminal tiers / the through-line).
- Slate-blue mids (tier bands / spine nodes): `#426176`, `#516570`,
  `#587c91`, `#79919e`, `#7a8aa2`.
- Periwinkle/indigo (orthogonal axis rails — distinct hue, same L/S family):
  `#68749f`, `#8992ad`, `#92a0d4`.
- Cool desaturated grays (gridlines / reserved-boundary dashed elements):
  `#a5afb3`, `#aab2ab`, `#8e8e8e`.
- Neutrals: ink `#000000`; warm near-white ground `#fdfdf6`; light fills
  `#eeeeee` / `#e3e3e3`.

Suggested mapping (to refine when authoring): spine = slate-blue mids
deepening to `#235a7d` at ELI; orthogonal axis rails = periwinkle, drawn as
"switch-on" segments; the reserved Self-actuated node = dashed in cool gray
until the WF question resolves; the 2×2 = light fills with slate borders.

`[SYNTH ?]` **Therefore the figure should be native TikZ**, not SVG/mermaid:
it renders directly through LuaLaTeX with no missing pipeline machinery, is
monograph-grade/scalable, and can take the cover palette as TikZ color
definitions. (Alternative — build the general SVG→PDF pipeline — is a
larger, separate FORMAT-TODO scope; out of scope for "help with the Scope
of work section" unless Joseph wants it.) **Flag for Joseph confirmation
before authoring the figure.**

## 5. The capability/name-delta walk (the organizing spine)

The section + figure are organized by this walk. Status-tagged per step.
"Capability" = what new theoretical machinery the refinement unlocks;
"Name" = the adjective earned; "Axis" = an orthogonal activation conferring
an adjective without narrowing the spine.

| Step | Refinement (boundary) | Capability unlocked | Name | Canon anchor |
|---|---|---|---|---|
| 1 | observation under uncertainty | Section I machinery: mismatch $\delta$, gain $\eta^\ast$, tempo $\mathcal T$, persistence condition, sector-condition stability — *"can it keep up with a changing world?"* | **adaptive** | `#scope-adaptive-system` `[CANON ✓]` |
| 2 | + binary choice + Pearl-L2 causal contrast | interventional (Level-2) data generation; causal-hierarchy requirement well-posed; causal-structure learning becomes possible | **agentic** | `#scope-agency` `[CANON ✓]`; boundary def is `[OPEN]` — see §6(A) |
| — | *axis on at step 2* | Knowledge Type becomes meaningful: does it refine its causal map online? | static / learning | proposal Axis B `[SYNTH ?]` |
| 3 | + explicit separable $G_t=(O_t,\Sigma_t)$ | orient cascade; satisfaction-gap / control-regret split; $G_t$-complexity bound; directed-separation becomes *statable* — *"is its strategy adequate?"* distinct from *"is its model accurate?"* | **actuated** | `#form-complete-agent-state`, `#der-orient-cascade` `[CANON ✓]` |
| — | *axis on at step 3* | Goal-Update Coupling becomes meaningful | separated / partial / coupled | `#der-directed-separation` `[CANON ✓]`; ordering fix §6(D) |
| 4 | + revises own $O_t$ (goal autonomy, not just solution autonomy) | the self-actuation operator $\mathfrak{A}$ = internalized orient-cascade step 5d; the terminal-grounding structure | **self-actuated** | `#self-actuated-agent` (reserved); **`[WF-PENDING]`** — Result G underproven, WF-strengthening spike running |
| 5 | + primary channels are language | directed separation fails *by construction* → Coupled by construction; coupled formulation forced | **logogenic** | `#scope-logogenic-agent` (03-llm-core) `[CANON ✓]` |
| 6 | + persistence morally weighted (five constitutive factors) | morally-continuous *by construction* | **logozoetic** / ELI | `moral-continuity` scope, `04-eli-core` `[CANON ✓]` |

`[WF-PENDING]` **The continuity-stance overlay becomes derivable here.**
The self-actuation formalization (if Result G survives strengthening)
yields: continuity stance is a property of $O_t$ (`#disc-continuity-stance`),
self-actuation is the capability to revise $O_t$ endogenously, so the
*negotiated* stance's availability is gated by the self-actuation
capability — *negotiated* = continuity term sits below the terminal
grounding invariant (revisable); *morally-continuous* = continuity term is
*in* the terminal invariant (unrevisable without degeneracy). This makes
Joseph's "keep orthogonal + overlay" decision a **derivation**, not an
empirical hand-wave — but it rides on Result G's tower, which is exactly
what the WF spike is contesting. Hold until the spike resolves.

## 6. Open canonical tensions (resolution directions)

- **(A) `[OPEN]` The Adaptive→Agentic boundary is unsettled in canonical
  itself.** Three non-equivalent definitions: `#scope-agency`
  (adaptive + $\lvert\mathcal A\rvert\geq2$ + Pearl-L2 contrast); LEXICON
  `agentic-system` ("+ outcome model + goal-directed action + model
  adaptation", boundary at `#post-causal-structure`); the proposal's
  argmax-vs-error-regulation cut (which itself notes the Pearl cut is
  "misleading" since PID *is* a Pearl intervention). *Resolution direction*
  `[SYNTH ?]`: anchor the formal boundary on `#scope-agency`'s Pearl-L2
  (it's the formal-expression anchor and what the capability "interventional
  data generation" actually requires); the LEXICON `agentic-system` gloss
  needs a one-line reconciliation — **flag, do not unilaterally rewrite the
  LEXICON entry** (terminology/entries change is its own decision).
- **(D) `[CANON ✓]` GUC axis ordering.** Canonical
  `#der-directed-separation`: Separated ($\kappa=0$) → Partial
  ($0<\kappa<1$) → Coupled ($\kappa\to1$). Proposal + DOMAINS order it
  Separated | Coupled | Partial — pedagogically inverted (Partial is
  *between* on the $\kappa$ axis). Mechanical fix in both the verified
  ontology and the figure.
- **(F) `[CANON ✓]` "Composite" is not atomic.** Canonical composition is a
  **4-route disjunction** (3 alignment routes + the strategic-equilibrium
  route C-iv, `#scope-composite-agent`) with a **two-axis unity profile**
  (4 content dims + structural $U_f$, `#def-unity-dimensions`). The
  proposal's binary Primitive/Composite is a defensible *top-level
  simplification* for the figure (per the simplifying-liberties license),
  but the verified ontology doc must not present Composite as atomic, and
  the figure must not imply it is.

## 7. What can proceed now vs. what is gated

**Can proceed now (no WF dependency):**

- The verified-ontology document (`recommended-agent-ontology.md`
  supersession): everything in §2, the §5 walk steps 1–3 and 5–6, the §6
  (A)/(D)/(F) reconciliations. Mark step 4 (self-actuated) as
  reserved-and-being-formalized, don't state Result G.
- Figure scaffolding: the spine (steps 1→6 as a narrowing column), the
  gated-axis rails (Knowledge at step 2, Coupling at step 3), the 2×2 shown
  at the Adaptive↔Actuated region, palette sampling from
  `01-aat-core/AAT-cover.svg`. Step-4 node drawn as a *reserved boundary*
  (visually distinct — e.g. dashed), not asserting the internal
  capability yet.

**Gated on the WF-strengthening spike:**

- The self-actuated tier's *capability* content (the $\mathfrak{A}$
  operator, the terminal-grounding no-go, Result G).
- The continuity-stance "becomes derivable" overlay (§5 `[WF-PENDING]`).
- Segment authoring P1–P4 (`#deriv-self-actuation-grounding`, filling
  `#self-actuated-agent`, retyping `#disc-continuity-stance`, cross-refs).

## 8. Honest open question for Joseph

`[SYNTH ?]` §4: confirm **native TikZ** for the figure (vs. building the
general SVG→PDF pipeline, which is larger and separate). My recommendation
is TikZ — robust, no new pipeline machinery, monograph-grade, palette-able.

## 9. Pointers

- Proposal pair being verified/superseded:
  `msc/domain-unification-2026-05-04/recommended-agent-ontology.md` +
  `doc/DOMAINS.md` (the latter queued next).
- Self-actuation: `spikes/spike-self-actuation-grounding.md` (WF-BLOCKED,
  audit recorded in its `## Independent Audit` section); WF-strengthening
  spike running.
- Continuity-stance reconsideration tracking:
  `msc/naming/mini-lexicon-todo.md §13.11`;
  `#disc-continuity-stance` Working Notes.
- Pedagogy posture: project CLAUDE.md "respectful pedagogy /
  mental-model-first"; the `01-aat-core/OUTLINE.md` "Reading AAT" preamble
  is the two-layer worked example to match.
