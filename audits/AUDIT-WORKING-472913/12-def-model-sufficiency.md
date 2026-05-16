# 12 — def-model-sufficiency  *(no finding; THREAD-B → dissolved §B.1; THREAD-E advanced; strong §E)*

`type: definition · status: axiomatic · stage: deps-verified · depends: [form-agent-model, form-information-bottleneck, def-action-transition]`
Deps upstream (10,11,02). DETECTOR clean (one `*[Definition]*`). B7 alive (12/12).
*(Lighter cadence from seg 12: 14 prompts walked mentally; prose only where something surfaced.)*

## THREAD-B — DISSOLVED (→ §B.1; the burden-of-proof gate working as designed)

$S(M_t)=1-\dfrac{I(\mathcal C_t;o_{t+1:\infty}\mid M_t,a_{t:\infty})}
{I(\mathcal C_t;o_{t+1:\infty}\mid a_{t:\infty})}$. The numerator is, in the
segment's own words, "the predictive information the full history carries
about the future *beyond* what $M_t$ already captures — **the information
lost by compression**." That is *exactly and quantitatively* the residual
THREAD-B (seg 02) worried was an unnamed, under-tracked cost of the
bounded-$M_t$ Markov-by-completeness move. The cost is not hidden: it is
$1-S(M_t)$. The seg-02 "independence of the dual-Markov commitments" claim is
**retro-justified** — both moves are definitional-relative-to-the-named-object;
the bounded-vs-unbounded *asymmetry* is precisely absorbed into $S$, the
relocation target was named (segs 09/10/11) and is now *delivered* (seg 12).
**THREAD-B → rescinded candidate.** Logged to §B.1 (rescinded ledger) — the
gate visibly working: a concern chased for 10 segments, dissolved on reading
the consistently-named relocation home. This is calibration data the FINAL
reader needs (shows the audit's discipline is real, not finding-hungry).

## THREAD-E — advanced (consequence stated in the theory's own voice)

"Trajectory-relativity" ¶: "Two copies of the same $M_t$ exposed to different
event streams will each have their own $S$ measured against their own
divergent $\mathcal C_t$; neither sufficiency value is the other's… Claims of
the form 'the model has sufficiency $S$' make sense only relative to a
specific trajectory; aggregated claims across copies of a given $M_t$ require
additional machinery. This is the scope commitment in `#scope-agent-identity`."
⇒ THREAD-E's structural fact (non-forkable $\mathcal C_t$ + lossy forkable
$M_t$ ⇒ copies are non-aggregable / trajectory-indexed) is asserted *by the
theory itself*, and `#scope-agent-identity` is named the home (3rd consistent
naming). Remaining THREAD-E check at `scope-agent-identity`: confirm it
carries the *introspective-undetectability* framing specifically (seg-12
carries non-aggregability/trajectory-indexing — same structural fact; the
"undetectable from inside" consequence is the THREAD-E-specific thing to
confirm lands there). Strongly trending integration-debt-resolved-in-voice.

## §E (strong) — well-definedness excision + proactive forward scope-propagation

The scope clause is exemplary and is the **anti-F2 done proactively**:
"$S$ undefined when $I(\mathcal C_t;o_{t+1:\infty}\mid a_{t:\infty})=0$ …
predictive sufficiency is a property *of a prediction task*; there is no
prediction task to be sufficient for. **Downstream constructs that build on
$S$ — `#def-model-class-fitness` and `#result-structural-adaptation-necessity`
— inherit the same scope and are correspondingly inapplicable** in
predictively-vacuous regimes." This (a) excises-and-names the degenerate
boundary (same honesty geometry as seg-05, not absorb-as-limit), and (b)
*propagates the scope condition forward, by name, to its dependents* — the
legitimate scope-propagation direction, the exact discipline F2/F1 lapsed on,
here performed proactively and correctly. Partial reassurance for **THREAD-F**
(seg-05: worry that scope conditions don't propagate to dependents): the
framework demonstrably *can* and *does* propagate by name — THREAD-F's
specific H>0-temporal-quantifier worry still verified at the persistence
results, but the systemic version of the worry is weakened.

Also §E: predictive-vs-causal Discussion claim hard-checked (Gate-2): "$S=1$
nearly sufficient for causal validity given $a_t=\pi(M_t,G_t)$; remaining
requirement = no unmodeled common cause of action & outcome" — this is a
*correct* statement of when predictive sufficiency upgrades to backdoor-valid
interventional validity, appropriately hedged, relocation named
(`#def-value-object`, `#der-causal-hierarchy-requirement`). Holds. (Phase-3
disconfirmation attempt #2: another hard-checked content claim that *holds* —
still zero content/math defects at 12 segs.) Policy-relativity treated
*identically* to seg-11 (same $a_{t:\infty}$/$\pi_{\text{cont}}$ convention,
same forward-ref) — cross-segment math-convention consistency is high (vs F3's
*label* drift): reinforces the Phase-3 bimodal picture (rigorous with
conventions, lapses on vocabulary at forward-pressured hinges).

## Prediction / next
Predicted (seg-11) THREAD-B would dissolve here — confirmed. Next OUTLINE:
`#def-model-class-fitness` (`type: definition`, deps-verified) — the ceiling
$\mathcal F(\mathcal M)=\sup_{M\in\mathcal M}S(M)$; FORMAT.md
canonical-formulations-ring; feeds inevitability-core
`#result-structural-adaptation-necessity`. Watch: does it inherit the
seg-12 scope clause as promised (test the just-made forward-propagation), and
is the "low $\mathcal F$ ⇒ change class not parameters" seed (seg-09) stated
here as a *definition* (correct) vs prematurely *derived* (DETECTOR)?

## Diagram — deliberately skipped
THREAD-B's dissolution and the $S/\mathcal F$ structure are already
visualized in seg-10's diagram (suitcase + skeleton showing THREAD-B
absorbing into sufficiency). A seg-12 diagram would be redundant. Per the
new ~1–2-per-chapter rule, **no diagram here**; reassess a single Chapter-2
capstone at seg-13 (`def-model-class-fitness` — the ceiling that triggers the
inevitability-core structural-adaptation result; if any Ch-2 segment earns
the chapter's capstone diagram it is that one).

## Wandering (≤1 ¶, lighter)
The clean dissolution of THREAD-B is the audit's first *closed loop* and it
validates the method's epistemic integrity more than any finding would: a
concern was raised early (seg 02), tracked honestly across ten segments
without inflating it into a premature finding, and dissolved exactly when the
named relocation target delivered. That is the §3.6 discipline (no premature
"finding" under partial coverage) and the strengthen/charitable-yet-rigorous
discipline both working — and it is *only* available because the walk is
incremental and the thread was carried, not because any single segment
revealed it. A batch reader would either have missed the seg-02 seam or
"resolved" it by charitable assumption; the audit instead earned the
resolution. I'll make sure §B.1 of the FINAL foregrounds this as the
exemplar of the burden-of-proof gate, because an audit that only shows
findings looks finding-hungry; showing a well-tracked dissolution is what
makes the *kept* findings (F1/F2/F3) trustworthy.
