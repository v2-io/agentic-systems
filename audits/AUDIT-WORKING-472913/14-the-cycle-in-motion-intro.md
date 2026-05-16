# 14 — the-cycle-in-motion-intro  *(F1 RESCINDED → §B.1; F2 reaffirmed & sharpened; THREAD-A decisive-test set)*

`type: discussion · status: discussion-grade · stage: draft · depends: [form-agent-model, def-model-sufficiency, def-model-class-fitness]`
Deps upstream (10,12,13). DETECTOR clean (preview equations, no `*[Derived]*`
eq-tags — framing intro). B7 alive (14/14). Ch.3 promissory note.

## F1 — RESCINDED as a finding (the gate working again; integrity-critical)

This intro's CIY-placement paragraph + Working Notes reveal the **framework's
own stated convention** for exactly the F1 category:

> "CIY uses Pearl's $do(\cdot)$ notation — an **external import** (Pearl 2009;
> Bareinboim et al. 2022); **AAT's recapitulation lives at
> `#def-pearl-causal-hierarchy` in Part II Ch.2, where the framework deploys
> the hierarchy as machinery rather than referencing it as vocabulary**."
> WN: "…the do-notation is **externally cited**; the AAT recapitulation lives
> in Part II Ch.2 where the framework deploys the hierarchy operationally."

So the framework's coherent, *stated* convention is: `do(·)` is **Pearl's
externally-cited notation** (handled by external-citation machinery +
NOTATION.md global entry), and `def-pearl-causal-hierarchy` is a
**recapitulation-of-external-result deployed operationally in Part II**, *not
the definitional source slug*. Under FORMAT.md Gate-1 cond-4 ("a quantity
*defined elsewhere* → that *slug* in `depends:`"), `do` is **not defined by a
slug** — it is Pearl's, external. Therefore `scope-agency` using `do(·)`
notation incurs **no `depends: [def-pearl-causal-hierarchy]` obligation**, and
its parenthetical "(Pearl's intervention operator; see
`#def-pearl-causal-hierarchy`)" is *exactly compliant* with this convention
(cite the notation as external; point to the operational recap).

Re-checking both F1 sub-claims against this:
- **F1-notational** (do-notation not in deps): **dissolves** — covered by the
  stated external-citation convention; segment follows it.
- **F1-semantic** (cond (4)'s interventional content): the content is
  Part-I-native (my seg-06 analysis: the agent's action *is* the intervention
  by `def-action-transition`; cond (4) expressible in $T,h$). So it needs
  Pearl *notation* (external, conventionally fine) over Part-I primitives —
  **not** a load-bearing dependency on `def-pearl-causal-hierarchy`. Also
  dissolves as a *defect*.

**F1 → RESCINDED as a §B finding.** Retained only as a **§D Hypothesis-tier
quality suggestion**: restating cond (4) in $T,h$ would make Part-I
self-containment *explicit* (a modularity nicety, the "Part I machinery
applies regardless of architecture" story) — but it is **not a Gate-1
violation or dependency-honesty defect**; the framework has a stated,
coherent convention under which `scope-agency` is compliant. Logged to §B.1
(rescinded ledger) with the lesson below.

**Integrity note / lesson.** F1 was honestly flagged at seg-06 (explicitly
"Phase-2 pending," "counterevidence Phase-1-limited") and is now dissolved by
*more* in-order de-novo reading (seg-14, read in OUTLINE sequence, not from
forbidden Phase-2 materials). This is the burden-of-proof gate
self-correcting as designed — and a real lesson: **notation-vs-definition +
recapitulation-vs-source is a now-known framework convention.** Going forward
I will *not* flag external-cited-notation forward-use (Pearl `do`, Tishby IB,
Lyapunov, etc.) as F1-type; the obligation is external-citation hygiene, not
`depends:`. (This also retro-validates seg-08's self-calibration that F1 was
"correctly scoped to Formal-Expression use" — turns out even that scoping was
over-strict given the external-notation convention. Honest update.)

## F2 — reaffirmed and SHARPENED under the same convention

Does the external-notation/recapitulation convention rescue F2? **No —
categorically different.** F2's `*[Derived (Conditional on Tier 1M … **from
#result-contraction-template** …)]*` tag derives a *quantitative AAT-internal
result* (closed-form $\lambda_c$) **from an internal AAT slug**
(`#result-contraction-template`, Appendix A — AAT's *own* derivation, not an
external citation). Gate-1 cond-4 applies in *full* force: an internal slug
named *by the segment's own `*[Derived]*` tag* as the derivation source,
absent from `depends:`, at a `deps-verified` segment. No external-citation
convention covers an internal-slug derivation source. **F2 stands**, and is
*sharpened*: the framework demonstrably HAS a careful convention for
external-notation forward-use (seg-14) — which makes the *internal*
forward-derivation in F2 a clearer deviation from a framework that otherwise
handles this whole category with discipline. F3 (vocabulary "nominal" drift)
unrelated to this convention — unchanged.

## THREAD-A — decisive test now set

The intro: "We chose to call $M_t$ the agent's complete state… Under that
completeness, two things follow immediately… Both feel obvious in hindsight;
**both are *derived*, not chosen.**" But `form-agent-model` (seg-10) framed
completeness as a **formulation choice** (`type: formulation`,
`status: robust-qualitative`, "This is a formulation choice… a modeling
choice, not a derivation"). So the intro promises `der-recursive-update` /
`der-action-selection` are *derived* — *from a premise that is itself a
formulation choice*. Not contradictory (consequences of a formulation are
legitimately "derived given the formulation"), **but** "both are derived, not
chosen" risks reading as *unconditional* inevitability. **THREAD-A decisive
test at `der-recursive-update` / `deriv-recursive-update` (Ch.3, ~seg 16 +
appendix):** is the derivation honestly presented as *conditional on
`form-agent-model`'s formulation-choice completeness* (correct; matches
seg-02's `def-action-transition` characterization of the parallel move) — or
as unconditional forcing (→ THREAD-A finding: a `*[Derived]*`/inevitability
frame resting on a formulation-choice premise)? This is also where FORMAT.md's
inevitability-core claim for `#der-recursive-update`+`#deriv-recursive-update`
("Three constraints → unique recursive form. Strongest result in the theory")
gets its hardest audit — initial-prediction B-cluster directly in play.

## Other promissory notes logged (grade Ch.3 against these)
- `η^\ast=U_M/(U_M+U_o)`: intro claims "**any rational adaptive process must
  approximate this functional form**", Kalman-exact in linear-Gaussian,
  robust-qualitative elsewhere. Grade `emp-update-gain` against this strong
  "must approximate" claim (initial-prediction **B5**: is `emp-` strengthenable
  /mislabeled? intro already frames it robust-qual + Kalman-exact — B5 may
  partially confirm).
- `‖δ‖_ss = ρ/𝒯` "persistence condition in its simplest form; Ch.4
  generalizes … same shape" — promissory note for `hyp-mismatch-dynamics` +
  the Ch.4 sector/persistence results (the TOP PART-I TARGET cluster).
- "two derivations from completeness" = der-recursive-update +
  der-action-selection are *joint consequences*, not independent — verify
  they're presented as a unit and not double-counted.

## Prediction / next / diagram
Predicted (seg-13) Ch.3-intro = framing, DETECTOR-clean, promissory-note —
confirmed; did **not** predict it would carry the F1-dissolving convention
(big surprise; the single highest-value thing this segment did). Next OUTLINE:
`#form-event-driven-dynamics` (`type: formulation`, deps-verified) — events in
continuous time, the $\tau$-timestamp substrate; **THREAD-D test** (chronica
ordinal vs metric event-time — does this segment reconcile them?). **Diagram:
none** (intro; the F1-rescission and THREAD-A setup are prose-best; Ch.3
diagram budget reserved for the mismatch/gain/tempo or persistence-preview
segment, the chapter's load-bearing dynamic).

## Wandering (≤1 ¶)
Rescinding F1 one's own most-developed early finding is the audit's integrity
stress-test and the method passed it: the same incremental in-order discipline
that *found* F1 (seg-06) *dissolved* it (seg-14), with the dissolution
traceable to the framework's own stated convention rather than to charitable
fatigue. The lesson generalizes beyond F1: **a framework this large encodes
its conventions distributively, and a finding raised before the
convention-stating segment is read is provisional by construction** — which
is precisely why the protocol forbids Phase-2 spoiler-reading *and* why it
carries findings as "Phase-2 pending" rather than asserting them. The net
ledger is *healthier* for the rescission, not weaker: F2 (now sharpened, the
genuine structural defect), F3 (vocabulary), TG1 (tooling), THREAD-A (live,
decisive test set), and a clean §B.1 showing two independent dissolutions
(THREAD-B, F1) — an audit that dissolves two of its own candidates on
evidence is far more trustworthy on the ones it keeps. Still zero content/math
defects at 14 segments; the Phase-3 bimodal spine (defects only at
forward-pressured load-bearing hinges; F2 the cleanest instance) is
*strengthened* by F1's removal (F1 was the noisiest instance; without it the
pattern is sharper, not weaker).
