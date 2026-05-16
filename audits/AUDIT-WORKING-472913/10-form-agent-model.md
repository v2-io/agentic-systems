# 10 — form-agent-model  *(no finding; THREAD-B near-dissolved; §E exemplar)*

`type: formulation · status: robust-qualitative · stage: deps-verified · depends: [def-agent-environment, def-observation-function, def-chronica]`

## Dep-graph / DETECTOR / OUTLINE-order
Deps = 01, 03, 04 (upstream). One `*[Formulation (agent-model)]*` tag, no
`*[Derived]*` — DETECTOR clean. Discussion forward-`#`-ref to
`#def-agent-spectrum` (Part II) is legitimate (Discussion, not Formal
Expression — not F1-type). B7 alive (10/10).

## THREAD-B — near-dissolved (the gate working; candidate trending to §B.1)

Seg-09 localized the THREAD-B test here. Verdict: **the framework handles it
correctly.** The segment:
- calls it a formulation, *explicitly* ("This is a formulation choice"; "a
  modeling choice, not a derivation");
- names the loss without hedging ("$\phi$ is a many-to-one compression …
  multiple distinct histories may produce the same model state"; "Any
  information not in $M_t$ is lost to the agent");
- makes completeness **tautological-relative-to-retention** — "we assume
  $M_t$ captures everything the agent *retains*" (retains, not *needs*) — so
  completeness is definitional, and the substantive question ("is what's
  retained *enough*?") is **explicitly forwarded**: "Whether $M_t$ retains
  *enough* information is the subject of `#def-model-sufficiency`."

This is precisely seg-02's `def-action-transition` "modeling commitment about
the breadth of the named object" pattern — *but with the relocated cost's
target named in-text* rather than left implicit. THREAD-B's specific worry
(the bounded-$M_t$ vs unbounded-$\Omega$ asymmetry is a hidden, under-tracked
cost) is therefore **not a finding at the formulation layer**: the asymmetry
is *correctly absorbed* into the sufficiency/fitness machinery (the right
home — a bounded suitcase's adequacy is exactly what $S$/$\mathcal F$
measure), and the relocation is explicit, not silent. THREAD-B status:
**near-dissolved; trending to §B.1 (rescinded candidate — gate working).**
Final confirmation = `def-model-sufficiency` (seg ~12) actually *quantifies*
the forwarded residual and `def-model-class-fitness` (seg ~13) supplies the
ceiling seg-09 previewed. If both deliver, THREAD-B → rescinded with the
seg-02 "independence" claim retro-justified (both moves definitional-relative;
asymmetry lives in sufficiency, correctly). If `def-model-sufficiency` merely
defines $S$ without addressing bounded-adequacy, a residual survives.

## §E positive — exemplary type/status/ring honesty (F2 contrast)

`type: formulation` + `status: robust-qualitative` + an Epistemic Status that
*explains the pairing* ("robust — any agent that conditions on retained info
can be described this way — but the specific complete-compressed-state
commitment is a modeling choice, not a derivation"). This is exactly the
FORMAT.md Gate-2 triage done right, and matches FORMAT.md's own
canonical-formulations-ring assignment for `#form-agent-model`. Direct
contrast to F2's `*[Derived]*` tag-inversion. Calibration: the framework's
*modal* behavior is honest type/status labeling; F1/F2 are the deviations.

## Prompt walk (proportionate — no finding)

**1 Predictions.** Predicted formulation + completeness + the THREAD-B test;
all landed. Mis-guessed status (`axiomatic/formulation` → actual
`robust-qualitative`), and the actual is *better* than my guess — noting my
own calibration: I under-credited the framework's status-precision again
(same direction as the seg-05 surprise). Adjusting prior: when uncertain
between axiomatic and robust-qualitative for a formulation, AAT tends to the
more precise/honest of the two.

**2 Cross-segment.** Consistent with 01 (loss constitutive), 03 ($h$
many-to-one — note $\phi$ many-to-one is the *temporal/internal* analog of
$h$'s *instantaneous* many-to-one; the framework now has two distinct
lossy maps, world→obs ($h$) and history→model ($\phi$); watch they are not
later conflated). 04 (chronica sole raw material) honored exactly. THREAD-E
(fork-undetectability = $\phi$ non-injective) gets *direct textual support*
here: "$\phi$ is many-to-one: multiple distinct histories may produce the
same model state" is *exactly* the THREAD-E mechanism stated in the segment's
own Formal Expression — strengthens THREAD-E's §D status (the synthesis
03⊕04 I flagged is now also literally asserted in seg-10's Formal
Expression). Logged: THREAD-E mechanism confirmed in-text at seg-10; still
verify `scope-agent-identity` carries the *consequence*.

**3 Math.** None (formulation). $\phi:\mathcal C^\ast\to\mathcal M$ many-to-one
— type-correct.

**6 Next prediction.** OUTLINE next: `#form-information-bottleneck`
(`type: formulation`, OUTLINE stage `draft`). Predict: applies Tishby IB to
characterize optimal $\phi$ (compress $\mathcal C_t$ keeping predictive info
about future obs); honest prior-art adoption (Tishby cited, per seg-09's
preview and CLAUDE.md prior-art-integration discipline); `status` ~
robust-qualitative/formulation; deps include form-agent-model + def-chronica.
DETECTOR: predict clean (formulation, IB is adopted not derived-here).

**7 What I'd change.** Nothing. Model formulation segment done correctly;
another yardstick for F2.

**9/13 Enables.** Making $\phi$'s many-to-one-ness "not a deficiency — the
essential function" is the move that lets *compression quality* (not
compression *existence*) be the object of theory — the entire $S/\mathcal F$
+ IB + structural-adaptation line is licensed by this one reframing. Quietly
load-bearing despite being "just a formulation."

**12 Felt value.** Medium. No finding, but it cleanly resolves the
longest-running open thread (B) in the framework's favor and adds in-text
support to THREAD-E — net epistemic progress, and a strong §E datum.

## Wandering thoughts (≤2 ¶)

The recurring architecture is now unmistakable and worth stating as a pattern
the audit has *learned* (not just a per-segment note): AAT repeatedly
discharges a potential objection **by definition**, and its honesty is
entirely a function of *whether the relocated cost's new home is named
in-text*. Seg-01 (loss constitutive — home: the whole theory's non-vacuity).
Seg-02 (Markov-by-breadth — home: *named here* finally, sufficiency/fitness).
Seg-10 (completeness tautological — home: *explicitly forwarded* to
`def-model-sufficiency`). When the home is named (seg-10), it's exemplary;
when it's left implicit (seg-02's "independent … about breadth" with no
pointer), THREAD-B had to chase it for eight segments before it resolved. The
audit-actionable generalization: *the finding is never "they discharged a
cost by definition" — that's legitimate and pervasive; the finding is "they
discharged it and did not name where the cost went."* F1/F2/F3 all fit this
exactly (F1: do-semantics' home unstated in deps; F2: derived-result's home
is downstream-unstated; F3: "nominal"'s home ambiguous across segs). This is
the unifying shape of every finding so far and it is the sharpened form of
the integration-debt>theory-gap hypothesis: **the defects are all
unstated-relocation-targets, not wrong content.** That is a strong, testable
Phase-3 spine and I'm now actively trying to break it (seeking a finding that
is genuinely wrong *content*, not an unnamed relocation).

The other thing worth one line: $\phi$ being many-to-one is asserted in
seg-10's *Formal Expression* as "not a deficiency — the essential function."
That is the THREAD-E (fork-undetectability) mechanism stated by the theory
about itself, in the theory's own voice — which means THREAD-E is not my
imported synthesis but a consequence the framework has *already written down*
and merely not connected to `scope-agent-identity`. That nudges THREAD-E
hard toward "integration debt" (the pieces are all in-text; the connection
isn't) and away from "auditor's external observation." Good — fewer of my
findings are external impositions than I feared at the priming-disclosure
stage; they are mostly the framework's own unconnected pieces.

## Diagram

Two-layer vertical. **Anchor:** packing a *fixed-size suitcase* — $\mathcal
C_t$ = everything accumulated; $\phi$ = packing into bounded $M_t$;
"completeness" = the suitcase *is* what you take (tautological; anything left
on the bed is lost — many-to-one). The real questions: did you pack *what
you'll need* ($S$) and could *any* packing of *this* suitcase hold it
($\mathcal F$ ceiling). Perturb: shrink the suitcase ⇒ more left behind ⇒
$S$ can't hit 1 ⇒ (if best packing still fails) need a bigger suitcase
(class). **Skeleton:** $\mathcal C_t\xrightarrow{\phi\ (\text{many-to-one})}
M_t$; completeness tagged "tautological (≡ retained)"; the "enough?" question
on a *dashed legitimate-preview* arrow to `def-model-sufficiency`; and
**THREAD-B drawn resolving** — the seg-02 bounded/unbounded asymmetry shown
*absorbed into* the sufficiency/fitness box in **teal** (gate working, not
amber-finding), explicitly captioned "candidate → §B.1, the burden-of-proof
gate dissolving a concern." See `10-form-agent-model.tex`.
