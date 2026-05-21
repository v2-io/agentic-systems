---
spike: strategic-composition-class-3-attempt
date: 2026-05-21
status: ACTIVE — math pushed; landing reached but Joseph-reserved
related_segments:
  - deriv-strategic-composition
  - impl-strategic-composition
  - der-directed-separation
  - hyp-directed-separation-under-composition
  - der-class-coercion-via-wrapping
  - disc-adversarial-coupling-pressure
  - disc-separability-pattern
  - scope-composite-agent
---

# Spike — Framing: Can strategic composition force a Class 3 (Coupled) composite?

## §0. The question (Joseph's framing)

`#deriv-strategic-composition` currently lands:

> Class 1 (Separated) sub-agents under goal divergence → **Class 2 (Partial)** composite.
> Within-agent processing stays Separated; the composite acquires *bounded across-agent coupling* through cross-agent policy modeling.

A *bounded*-coupling result.

The question: is there a **stronger** result that shows Class 3 (Coupled) full entanglement under partially-opposing objectives — or, if not, **why**?

Joseph's brief: push the math from every angle until something yields. If attempts keep yielding neither a clean strengthening nor a clean no-go, that usually means the question is framed wrong or something is missing.

This spike answers in that order: §1 lays out the formal criterion the question is using; §§2–5 push four distinct strengthening attempts to their breaking points; §6 returns to re-examine whether the *current* Class 2 claim is itself derivable; §7 finds the framing-is-wrong layer; §99 lays out what changes (or doesn't) and what is Joseph-reserved.

The push hits a result and a discovery — a derived no-go on the architectural axis, plus an inter-segment contradiction that surfaces a likely GUC-rename residue. Neither was the "Class 3 strengthening" Joseph asked for; both are honest products of the strengthen-first attempt. The push also surfaces a genuine candidate for a *new* axis the framework currently lacks — a dynamic-regime axis distinct from architectural class — which would be the constructive reframing if Joseph wants to take that route.

## §1. Surprising starting discovery: an existing internal contradiction

**Before** running the math, the read across segments turned up a contradiction in the framework's *current* position.

| Segment | Claim on composite class |
|---|---|
| `#deriv-strategic-composition` Discussion §"Class-2-(Partial)-composite-from-Class-1-(Separated)-sub-agents" | "**Class 2 (Partial)** composite" |
| `#deriv-strategic-composition` table row, "Strategic composition produces Class 2 (Partial) composites from Class 1 (Separated) sub-agents" | "**Class 2 (Partial)** composite" |
| `#der-directed-separation` Discussion §"Composite-level class inheritance" | "**Class 2 (Partial)** composite from Class 1 (Separated) sub-agents" |
| `#hyp-directed-separation-under-composition` Case 1 (goal-blind routing) | **Class 1 (Separated)** composite |
| `#hyp-directed-separation-under-composition` Case 2 (goal-dependent routing) | "**Class 3 (Coupled)** architecture" composite |
| `#impl-strategic-composition` §"Strategic composition lifts contraction to equilibrium" (three occurrences) | "**Class 3 (Coupled)**" composite |
| `#impl-strategic-composition` Working Notes line 83, finding `#23` reference | "Class-1-sub-agents → **Class-3**-composite under partially-opposing objectives" |

The implications segment is the only place in the framework currently asserting Class 3 from strategic composition. Three observations.

**First:** the implications segment's own load-bearing source, `#deriv-strategic-composition`, says Class 2 — and the implications segment is supposed to *consolidate*, not extend.

**Second:** the migration note in `#deriv-strategic-composition` Working Notes is explicit about the GUC rename:

> **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. The canonical strategic-composition pattern "Class-1-sub-agents → Class-3-composite" (old vocab; Class 3 = partially modular) is now "Class 1 (Separated) sub-agents → Class 2 (Partial) composite."

So the pre-rename phrase was "Class 1 sub-agents → Class 3 composite" with Class 3 = *partially modular*. After the 2026-05-09 swap, the canonical phrase is "Class 1 sub-agents → Class 2 composite" with Class 2 = Partial. **`#impl-strategic-composition` carries the pre-rename phrase "Class 3 composite" three times, but the post-rename Class 3 is *Coupled*, not *partially modular*.** The post-rename reading inverts what the implications segment was originally asserting.

**Third:** `#impl-strategic-composition` does not contain a 2026-05-09 GUC migration note (the other involved segments do). The implications segment appears to be **GUC-rename residue** — a segment the sweep missed, whose surface text now claims something the derivation does not support and was never meant to support.

This shifts the spike's question. Joseph asked "is there a stronger Class 3 result?" The honest preliminary answer is: **there appears to be no derivation supporting one anywhere — the only segment asserting Class 3 is asserting it by un-swapped pre-rename label, not by derivation.** The genuine question is therefore:

> *Was the original pre-rename "Class 3 (partially modular) composite" — i.e. the current Class 2 (Partial) composite — itself derivable, and can it be strengthened to the actual current Class 3 (Coupled) composite?*

That is the question §§2–7 pursue under strengthen-first. The discovery above is recorded here because integration-is-replacement applies regardless of the math outcome: the implications segment's "Class 3 (Coupled)" three occurrences must be fixed either way.

## §2. Setup: what "Class 3 composite" must satisfy

The formal architectural-class criterion from `#der-directed-separation`:

$$\kappa_{\text{processing}} \;=\; \frac{I\!\left(G_t;\, M_{\tau^+}\,\mid\, e_\tau,\, M_{\tau^-}\right)}{H\!\left(G_t\,\mid\, e_\tau,\, M_{\tau^-}\right)}$$

- Class 1 (Separated): $\kappa = 0$ under all distributions — no pathway exists.
- Class 3 (Coupled): $\kappa \approx 1$ under most distributions — pathways exist and are used.
- Class 2 (Partial): $0 \lt \kappa \lt 1$, distribution-dependent.

The classification is **structural** (which pathways exist in the processing graph), not parametric. $\kappa$ is the *diagnostic* for the structurally ambiguous Class 2 middle. The Class 1/3 boundary is binary by *existence-of-pathway*; Class 2 is the residue where some pathways exist and others don't.

The conditioning on $M_{\tau^-}$ is essential: it removes the prior correlation between $G$ and $M$ that always exists. The measure captures *extra* goal information entering the epistemic update **beyond what was already in the prior model** — information that flows through *pathways that bypass the event $e_\tau$*.

For the composite version: replace $G_t \to G^c_t$, $M_{\tau^\pm} \to M^c_{\tau^\pm}$, $e_\tau \to e^c_\tau$, $f_M \to f^c_M$. The composite is Class 3 iff the composite $f^c_M$ has a structural pathway from $G^c_t$ to $M^c_{\tau^+}$ that bypasses $e^c_\tau$.

For an aligned composite (route C-i / C-ii / C-iii), $G^c_t = (O^c_t, \Sigma^c_t)$ is a state in the same shape as a single-agent purposeful state. For a strategic composite (route C-iv), `#scope-composite-agent` says the macro-state is *defined relative to the equilibrium structure $\mathcal E$* rather than relative to a shared target state. The two cases will turn out to have different category-theoretic *type* — §7 returns to this.

## §3. The four routes the strengthening attempt can plausibly take

Given the criterion, a Class 3 composite needs a $G^c_t \to f^c_M$ pathway bypassing $e^c_\tau$. The candidate pathways:

- **(R1) Cross-agent direct cross-talk** — channels that transmit $G^{(j)}_t$ between agents not mediated by environment-acting actions. The natural home is `#hyp-directed-separation-under-composition` Case 2 (goal-dependent routing). §2 of the next file (`01-STRENGTHEN-ATTEMPTS.md`).
- **(R2) Rational-expectations equilibrium structural coupling** — at fixed points, $G^c$ and $M^c$ become mutually constraining as a *structural* fact about the equilibrium state, not a *processing* pathway. §3 of the next file.
- **(R3) Mutual-modeling recursion** — agents' models of each other's models, all the way up the belief hierarchy, encode goal-content recursively. §4 of the next file.
- **(R4) Shared computational substrate** — agents sharing internal infrastructure (attention, memory, world-model) through which $G^c$ shapes processing. §5 of the next file.

§§2–5 of `01-STRENGTHEN-ATTEMPTS.md` work through each route, push the math as far as it goes, and record where each breaks. None gives Class 3 from strategic composition *alone*; (R1) and (R4) give Class 3 from structural conditions that strategic composition does not by itself entail. (R2) and (R3) yield genuine no-go shapes.

§6 of `01-STRENGTHEN-ATTEMPTS.md` then turns the criterion back on the *current* Class 2 claim itself and asks whether it is derivable. The honest answer there is that the current Class 2 claim — "cross-agent policy modeling makes the composite Partial" — conflates **belief content** (what $M^c$ encodes about goals) with **processing pathway** (whether $G$ enters $f^c_M$). The conflation is invisible to careless reading; the formal criterion separates them. §6 documents the conflation explicitly.

§7 of `02-REFRAME-INSIGHT.md` then takes the framing-is-wrong move: the architectural Class 1/2/3 partition was developed for individual-agent processing topology; for strategic composites whose macro-state $G^c = \mathcal E$ is a *fixed-point object*, the criterion is type-mismatched. What strategic composition genuinely shifts is the *dynamic regime* (contraction → equilibrium → cyclic-distributional), and that is a different axis the framework currently lacks a clean name for.

`99-VERDICT.md` collects the conclusions and itemizes what should change in canon (the contradiction is real and has to be resolved; the choice of *how* is Joseph-reserved because two genuinely different reframings are on the table).

## §4. Disposition before §§2–7

Strengthen-first as discipline: §§2–5 of `01-STRENGTHEN-ATTEMPTS.md` actually attempt the derivation, not just sketch the obstruction. Each route gets the math pushed through to where it breaks. The discipline that landed in `#disc-constructive-impossibility-posture` (Joseph 2026-05-14 — *"always seek the hardest thing first"*) is what this spike is trying to honor.

Integration-is-replacement applies: whatever §99 lands on, the **inter-segment contradiction in §1** must be resolved regardless, because the canon currently states one thing and its opposite. There is no version of *strengthen-first* where leaving the contradiction in place is the right move. The contradiction's resolution may also unlock something else — if `#impl-strategic-composition`'s "Class 3" was originally meant in the pre-rename sense (current Class 2 (Partial)), then the impl segment's "*the composite is necessarily Class 3*" force-of-claim was carrying load that should not have been carrying load: Class 2 (Partial) is bounded coupling, not "necessarily" coupled. The post-rename label-flip inadvertently strengthened the assertion. The math in this spike will say what is actually licensed.

## §5. Audit-safe one-line summary

The strengthen-first attempt yields no clean Class 3 derivation from strategic composition; surfaces a likely GUC-rename residue in `#impl-strategic-composition` that has been over-stating the framework's position since 2026-05-09; and points at a genuine missing axis — *dynamic regime* — that would constructively reframe what strategic composition actually delivers without inflating architectural-class claims.
