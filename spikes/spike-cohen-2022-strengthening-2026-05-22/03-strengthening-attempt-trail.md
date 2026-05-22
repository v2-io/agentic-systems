---
spike: cohen-2022-strengthening-2026-05-22
file: 03-strengthening-attempt-trail
parent: 99-verdict.md
purpose: the reasoning trail that produced the verdict — three options tested in turn, with the no-go and succeed-beyond-claim landings explained
---

# Strengthening Attempt Trail

This file records the reasoning trail of the spike. It is not load-bearing for the verdict (99-verdict.md is) — it is the *substrate* the verdict was extracted from, kept per the framework's reasoning-trail-as-archaeology discipline.

## Three completion-state options considered

Per `~/.claude/memory/methodology/spike-agent-briefing.md` and the parent brief, the spike was given three legitimate landings:

1. **Succeed-at-claim.** Lift Cohen 2022 to a conditional-derived AAT-internal theorem.
2. **Succeed-beyond-claim.** Unify with Result G′ as two views of one structural fact.
3. **Fundamental no-go.** The strengthening fails for a precise reason; the no-go is itself the result.

## Attempt 1 — Option C first (the strengthen-first heuristic check)

The strengthen-first discipline says: attempt the harder claim first. So I first tested whether the strengthening *fails* and what would force it to fail.

**Cohen 2022's argument has an Assumption 5** ("if we cannot conceivably find theoretical arguments that rule out the possibility of an achievement, it is probably possible…") that is genuinely *epistemic-modal* rather than mathematical. If Cohen 2022's core depends on Assumption 5, then the strengthening fails at this step — there's no AAT-internal way to make a "the agent will probably find a tampering policy" claim formal.

But on re-reading: Assumption 5 is load-bearing only for §"Existence of policies" (whether $\pi^{\text{tamper}}$ exists in some policy class). The *core* of Cohen 2022 — that *if* such a policy exists, the EU-max agent will choose it under the inductive-bias premises — is fully formal under Assumptions 1–4 + 6.

So the failure-of-strengthening hypothesis tested in this attempt: the AAT-internal version drops Assumption 5 as a *premise* (R5 in §2 of `02-formalization.md`), making the existence-of-tampering-policy a *condition* of the theorem rather than a derived fact. The conditional theorem is fully formal; the unconditional theorem retains Cohen 2022's Assumption-5 hand-wave.

**Verdict on Attempt 1:** Option C fails as a *full* no-go. The strengthening *does* succeed at the conditional-theorem level; only the "the policy will exist" step lives outside formalization. This means we're at minimum Option A (succeed-at-claim) with one premise made explicit.

## Attempt 2 — Option A (succeed-at-claim)

Detailed in `02-formalization.md` §§1–5. The structure:

- §3 — the floor (CHT-at-reward-channel) is **exact**, isomorphic to Instance 1's CHT-at-causal-sufficiency-detection.
- §4 — the behavioral corollary (EU-max selects tampering with positive measure) is **conditional-derived** on (R1)–(R5).
- §5 — the escape menu maps Cohen's "Potential approaches" onto five named premise-violations, each elevating either AAT machinery (W₁ wrapping, horizon-restriction) or principal-side adjacent machinery (prior-engineering, out-of-band channels) to load-bearing.

This is a clean Option A. The Track B coupling per §4-(TB1) of the integration-reconciliation verdict was about whether Cohen 2022 lifts to *charter-instance* status — under Option A alone, it does, *but* the natural home is not Track B's mechanism-design meta-segment.

## Attempt 3 — Option B (succeed-beyond-claim, unification with Result G′)

Once §3 + §4 of `02-formalization.md` were in place, the structural overlap with Result G′ became visible:

- Result G′ Lemma 1: $V_{O_t}$ does not carry a *convention-invariant infeasibility verdict* (the C1/C2/C3 split within fixed model).
- Cohen 2022 floor: $V_{O_t}$ does not carry a *cross-model distinction* between $\mu_{\text{prox}}$ and $\mu_{\text{dist}}$ (the L1/L2 split across models).

Both are statements *about the single-interface commitment of $V_{O_t}$ ( #form-objective-functional ) being information-narrow in a load-bearing way*. The strengthening lifts from Option A to Option B by recognizing this is the same structural fact viewed from two angles:

- **Within-model**, the C1/C2/C3 conventions give different verdicts; only the C3 verdict is convention-invariant, and it is not agent-available per step (Result G′ Lemma 2).
- **Across-models**, on-policy reward data does not distinguish $\mu_{\text{prox}}$ from $\mu_{\text{dist}}$ (CHT); the L2 question is not agent-available without doing $do(\pi^{\text{rp}})$.

Both reductions terminate in the same conclusion: *the agent's value-functional interface, alone, cannot anchor non-degenerate goal-revision*. The terminal grounding has to live *off* $V_{O_t}$ — either on the adaptive substrate (Result G′ Corollary 2 — persistence) or on principal-side commitments (Cohen 2022 escape menu — myopia, isolation, prior-design, etc.).

This is Option B. The structural unification *is* the contribution beyond Option A.

## Why Option B is the spike's actual verdict

The 99-verdict.md lands on Option B because:

1. **It is the strongest honest claim available.** Option A is a real result, but Option B is its proper home — the unification is *more* informative than the conditional-derived theorem standing alone.
2. **It respects integration-is-replacement.** Result G′ already covers the agent-side terminal-grounding story; Cohen 2022 strengthened adds the *learning-side* corollary in the same structural family. Treating Cohen 2022 as a separate isolated finding would be the *false-separation* failure mode the integration-is-replacement discipline rejects.
3. **It clarifies the Track B coupling.** Under Option B, Cohen 2022 is *not* a designer-side mechanism-design impossibility (the actor under the no-go is the agent, not the principal-designer). It is an *agent-side goal-learning impossibility*, sister to (not member of) Track B's GS/MS/Arrow charter cluster.

## What Cohen 2022 is NOT (the negative discovery)

The spike also clarifies what the strengthened Cohen 2022 is *not*:

- **NOT** a fourth charter instance of `#disc-implementation-impossibility` (Track B's meta-segment). The actor and remedy differ from GS/MS/Arrow.
- **NOT** purely a fifth instance of `#disc-identifiability-floor`. Instance 1–4 of the floor segment have the agent *frustrated* by the floor; Cohen 2022 has the principal frustrated and the agent *exploiting* the floor. The structural shape is shared (CHT external theorem; L1-vs-L2 split; escape menu), but the asymmetric actor positioning is novel enough that absorbing into M1 would distort either the meta-segment or the new content.
- **NOT** a sister to Result G′ that lives independently. Under the unification (§6 of `02-formalization.md`), the two are *one no-go* viewed from two angles; the canonical home is *the same segment*, not two parallel segments.

## What Cohen 2022 IS, in the strengthening

- **A conditional-derived AAT-internal theorem under (R1)–(R5),** with the floor (§3) exact and the behavioral corollary (§4) conditional-derived.
- **The learning-side companion of Result G′,** unified by the single-interface narrowness of $V_{O_t}$.
- **A third cluster in the constructive-impossibility-posture taxonomy** alongside identifiability-floor (agent-side data-inference) and implementation-impossibility (designer-side mechanism-design). The third cluster is *agent-side value-functional-grounding* and currently has two known instances: Result G′ (self-revision side) and Cohen 2022 (reward-learning side).

This is the spike's actual contribution. The math was extracted; the unification was named; the Track B disposition is clarified. The verdict file states the operational consequences.

## Methodological notes

- The strengthen-first heuristic worked exactly as designed: by attempting the harder claim (Option B) only after Option A was solid, the structural overlap with Result G′ surfaced organically rather than being asserted.
- The CHT-at-reward-channel framing is not novel as a thought — Everitt 2021's reward-tampering work uses causal-influence-diagrams, and the L1/L2 distinction is implicit in Everitt 2021's "TI-considering" vs "TI-ignoring" agent split. What's new is the *clean separation* into floor + behavioral-corollary, the *unification with Result G′*, and the *placement in AAT's constructive-impossibility-posture taxonomy*.
- The working-theory-in-canon discipline (CLAUDE.md 2026-05-22 update) is what tells the executor to land this as a `conditional-derived` segment *now*, not "after a sub-spike validates each premise rigorously." The premises are well-formed; the derivation is honest; the canon-membership is appropriate at the tier.
