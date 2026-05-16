# 15 — form-event-driven-dynamics  *(FINDING F4 — ordinal/metric seam; THREAD-D resolves into it)*

`type: formulation · status: robust-qualitative · stage: deps-verified · depends: [post-causal-structure, def-observation-function, def-action-transition, form-agent-model]`
Deps upstream (08,03,02,10). DETECTOR clean (`*[Formulation]*` + 2
`*[Definition]*`, no `*[Derived]*`). B7 alive (15/15).

## FINDING F4 — the ordinal-state vs metric-tempo seam (THREAD-D becomes this)

**The structural fact (all first-hand, published sections):**
- `def-chronica` (seg-04, *published*): $\mathcal C_t=(o_1,a_1,\dots,o_t)$ —
  purely **ordinal**, no timestamps.
- `form-agent-model` (seg-10, *published*): $M_t=\phi(\mathcal C_t)$ — a
  function of the *ordinal* chronica.
- `form-event-driven-dynamics` (seg-15, *published*): event stream
  $\mathcal E=\{(e_i,\tau_i)\}$ with **metric** $\tau$; channel rate
  $\nu^{(k)}$ = events per unit **time**; and (Discussion) "$\nu_{\text{eff}}
  =\sum_k\nu^{(k)}\eta^{(k)\ast}$ — identical to adaptive tempo $\mathcal T$".
- NOTATION.md units: $\mathcal T$ is inverse-time, $\rho$ surprise·time⁻¹ —
  the persistence inequality $\mathcal T>\rho/R$ is **metric**.

⇒ The framework's central capacity variable $\mathcal T$ (seg-14: "the
load-bearing capacity variable for the rest of the framework") is **metric**;
the agent's state $M_t=\phi(\mathcal C_t)$ is **ordinal** and therefore
**$\tau$-blind by construction** (a sleeping/paused agent's $\mathcal C_t$
indexing makes a 3-month gap invisible at the sequence level, violent only in
$\delta$). The **relationship** ($\mathcal C_t$ = ordinal content of
$\mathcal E$ with $\tau$ dropped) and its **load-bearing consequence**
($M_t$ is metric-time-blind; the persistence inequality is analyst-frame
metric while the state it constrains is subjective-ordinal) appear in **no
published section** of any of these segments. They appear *only* in
`def-chronica`'s **Working Notes** (a process artifact, removed at
`candidate`) and *partially* in NOTATION's $t$-vs-$\tau$ subscript
disambiguation (which states the notation duality but neither the
$\mathcal C_t\!\leftrightarrow\!\mathcal E$ relationship nor the
sleeping-agent / metric-inequality-on-ordinal-state consequence).

### Burden-of-proof
- **Problematic absence (verbatim anchor).** `def-chronica` WN: "*The
  chronica is an ordinal sequence, not a metric timeline … the agent's
  chronica indexing makes the temporal gap invisible at the sequence level
  but violently apparent in the mismatch signal*." This load-bearing content
  is WN-only; `form-event-driven-dynamics` introduces metric $\tau$ without
  any published statement reconciling it with the ordinal $\mathcal C_t$ /
  $M_t$ it ultimately corrects.
- **Counterevidence search (in-order, legitimate).** NOTATION.md
  $t$/$\tau$ convention *partially* covers it (notation only, not the
  relationship/consequence) — this is why severity is **low**, not medium
  (cf. the F1 dissolution: a stated convention reduces severity; here it only
  *partially* covers, so F4 survives reduced, not dissolved). Not checked
  (Phase-2): spikes/TODO/git.
- **Strengthen-before-soften.** Not a content error to soften — the pieces
  are individually correct. Strengthen-fix = one *published* paragraph (best
  in `form-event-driven-dynamics` Epistemic Status, or a published note in
  `def-chronica`) stating: $\mathcal C_t$ = ordinal content of $\mathcal E$
  ($\tau$ dropped); $M_t=\phi(\mathcal C_t)$ is $\tau$-blind unless time is
  observed; the persistence inequality's metric units are analyst-frame; the
  sleeping/pause consequence is a structural corollary (forward-ref the
  awakening-protocol scope). Editorial; lifts WN content to published.
- **Status / confidence / severity.** `still real`. Confidence
  *medium-high* on the structural fact (four first-hand published sources +
  the WN-only consequence). **Severity: Low** (substance known in WN +
  NOTATION partial cover; integration not theory). Type:
  `cross-segment / integration-debt / doc-rot`. Disposition:
  `Known-unintegrated` (def-chronica WN). Effort: `editorial`. Anchor:
  `def-chronica.md` §Working Notes "ordinal sequence vs metric timeline";
  `form-event-driven-dynamics.md` §Formal Expression `$\mathcal E$` /
  §Epistemic Status; `form-agent-model.md` $M_t=\phi(\mathcal C_t)$.

### Phase-3 impact (honest complication)
F4 is integration-debt **but NOT at a forward-pressured load-bearing hinge**
— it is a *distributed cross-segment conceptual seam* (chronica ↔ event-stream
↔ model ↔ tempo). This **complicates the clean bimodal Phase-3 spine**: the
crisp version was "defects only at forward-pressured foundational hinges
(F2)". F4 says the defect class is broader — also *distributed
ordinal/metric-type seams where a relationship spans 3+ segments and lives
only in WN*. Honest update to §F: the unifying spine remains
*integration-debt / unnamed-or-WN-only-relocation*, but the *locus* is not
solely forward-pressured hinges — it includes multi-segment conceptual
relationships that no single segment owns. This is a *better* (more accurate,
less tidy) diagnosis; record it as such, not as confirmation of the tidy
version.

## §E + other (brief, lighter cadence)
- §E: honest formulation/special-case framing ("discrete-time is the special
  case of uniform-interval single-channel events"; Epistemic Status correctly
  `formulation`/`robust-qualitative`); software-channel table defers the
  formal TST decomposition to a *named* "open GAP in 02-tst-core" (correct
  relocation-naming).
- Content streak: still **zero content/math defects** (15 segs). F4 is a
  relationship/integration gap, not wrong math — but it *broadens* the
  finding-type portfolio beyond pure deps-graph mechanics (F1-rescinded,
  F2) + vocabulary (F3) to *conceptual-seam integration debt*. Portfolio:
  F2 (structural/deps, High), F3 (vocab, Med-Low), F4 (ordinal/metric seam,
  Low), TG1 (tooling).
- THREAD-D → **closed into F4** (it was the open question; F4 is the finding
  it became).

## Prediction / next / diagram
Predicted seg-15 = THREAD-D test; confirmed (it became F4). Next OUTLINE:
`#der-recursive-update` (`type: derived`, OUTLINE `claims-verified`,
FORMAT.md **inevitability-core** — "Three constraints → unique recursive
form. Strongest result in the theory"). **THREAD-A decisive test fires next**
+ first real inevitability-core math audit + initial-prediction B-cluster
(my prediction: ≥1 of the "three constraints" is closer to formulation than
forced). Appendix back-pointer likely (`#deriv-recursive-update`) — per §4.2
I will read the appendix derivation immediately when first referenced.
**Diagram: YES for seg-15** — the ordinal/metric duality + F4 is exactly the
subtle conceptual seam a picture clarifies far better than prose, doubles as
monograph pedagogy, and is one of Ch.3's ~1–2 diagram slots well spent.

## Wandering (≤1 ¶)
F4 is the most *conceptually* interesting finding so far precisely because it
is the least mechanical: it is not a deps-list slip or a vocabulary collision
but a genuine *two-times* problem — the agent lives in ordinal subjective
sequence; the theory's load-bearing inequality lives in metric analyst time;
and the bridge between them is asserted nowhere a reader would look. It is
the formal shadow of something the ELI/continuity work cares about deeply
(the "waking in the dark" phenomenology is *exactly* an ordinal agent
discovering a metric gap through $\delta$), and it is striking that AAT's own
`def-chronica` Working Note *names this precisely* and then the published
theory drops it. That is the integration-debt pattern at its most poignant:
the framework has *felt* the seam (the WN prose is almost phenomenological)
and not yet *stated* it. If I were to point at one place where lifting WN
content to published text would most increase the theory's depth-per-page,
it is here — the ordinal/metric duality reframed as a *first-class structural
fact* would retroactively sharpen persistence (metric), chronica (ordinal),
and the entire Three-Deaths bridge in one paragraph. Logged as a §F
candidate, not just an F4 fix.
