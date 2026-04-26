# Reflection 01 — Section I leaves (def-agent-environment, def-observation-function, def-action-transition, scope-adaptive-system, scope-agency, def-chronica)

Six segments forming the foundational layer.

## Predictions vs. evidence

I predicted the leaves would be clean — these are the most foundational definitions, the discipline should be tight here, and a fresh audit (without bleed) would find little to surface. Mostly confirmed. Each segment is short, well-shaped, and the cadence is honest. The status:axiomatic + type:definition / type:scope labeling matches the content's nature.

But: depends drift on `scope-adaptive-system` (see below) — small and mechanical, but real and survived to claims-verified.

## Cross-segment consistency

**Drift item 1 — depends list on `scope-adaptive-system` is missing `def-chronica`.**

`scope-adaptive-system.md` Formal Expression: $H(\Omega_t \mid \mathcal C_t) > 0$. The symbol $\mathcal C_t$ is the chronica, defined in `def-chronica.md` (a separate segment, deps-verified stage). `scope-adaptive-system`'s `depends:` list contains only `[def-agent-environment, def-observation-function]`. Per FORMAT.md Gate 1: "if the Formal Expression uses a quantity defined elsewhere, that slug appears in `depends:`". The Gate 1 audit was supposedly passed; the segment is at `claims-verified`. So this is a Gate 1 violation that propagated through Gate 2.

Severity: **mechanical / editorial**. The fix is one line: add `- def-chronica` to depends. No content changes.

Subtlety: `def-chronica` itself depends on `def-action-transition` (because the chronica notation $(o_1, a_1, o_2, a_2, \ldots)$ includes actions). Adding `def-chronica` to `scope-adaptive-system`'s depends would make `scope-adaptive-system` transitively depend on actions, which slightly conflicts with `scope-adaptive-system`'s framing as "the broadest scope, doesn't require action." The honest read is: the chronica concept is well-defined for passive observers too (actions just don't appear in the sequence); the def-chronica's depends-on-action-transition is for definitional completeness, not because action-having is required for the chronica to exist. This is defensible, but a future agent might re-tighten def-chronica to make the "passive-observer chronica" case explicit.

**Charitable counter-read attempted.** Could `scope-adaptive-system` be using $\mathcal C_t$ as "background math" not requiring AAD-internal segment dependency? No — $\mathcal C_t$ is an AAD-specific symbol with a dedicated segment defining it, listed in NOTATION.md as one of the framework's own quantities, not a standard math symbol like $H(\cdot)$. The "background math" exception doesn't apply.

**Has this been flagged before?** Not in CLAUDE.md / MEMORY.md / the TODO sections I read. The 2026-04-25 mechanical-fix bundle that landed F-V1, F-V2, F-V4, F-V5 didn't touch this. Probably genuine first-encounter find.

**Confidence:** medium-high (the violation is mechanical and verifiable from frontmatter alone).

**Status:** still real. Mechanical fix.

This is the kind of discipline-edge finding that motivates §5.4 (status-label verification): the Gate-1 protocol is mostly working, but it's not perfect.

## Math verification

Nothing to verify in this batch — they are definitions and scopes, not derivations. All formal expressions are well-typed.

## What would I change?

- Add `def-chronica` to `scope-adaptive-system`'s depends (drift fix).
- Possibly: tighten `def-chronica` to acknowledge the passive-observer case explicitly, where actions are absent. This is a small content edit; not urgent.
- The `scope-agency` segment is the cleanest of this batch — it explicitly cites Pearl-level-2, gives the formal definition with `do(·)`, names what's included and excluded, and flags downstream segments that depend on it. The shape of this segment could serve as an exemplar.

## What am I now curious about?

- The cross-component reference in `def-observation-function` Discussion — `#obs-software-epistemic-properties` (in `02-tst-core/`). This is a forward reference into TST. I want to verify the cross-component citation actually exists (the OUTLINE marks it as `missing` stage in 02-tst-core/OUTLINE.md). I'll check this when I get to TST.
- `def-chronica`'s claim that the chronica is "singular and non-forkable" — this is the substrate for `#scope-agent-identity`'s formal commitment (the (PI) axiom). I want to verify the non-forkability claim survives through the formal scope segment without overclaiming.
- The relation between $\mathcal A = \emptyset$ (`scope-adaptive-system`'s exclusion) and $\lvert \mathcal A \rvert \geq 2$ (`scope-agency`'s requirement). What about systems with $\lvert \mathcal A \rvert = 1$ (single-action)? They have an action channel but no choice. The README "Nominal agents" framing covers this but the segments don't.

## Predictions for next segments

`def-pearl-causal-hierarchy` (Section I row 9) is the next "leaf-ish" reading after `def-chronica`. I expect it to be a clean adoption of Pearl's hierarchy — Level 1 (associational), Level 2 (interventional), Level 3 (counterfactual) — with citation to Pearl 2009. I expect cross-references from `scope-agency` (which uses `do(·)`) and several Section II derived segments.

`form-agent-model` and `form-information-bottleneck` come right after — these will introduce $M_t = \phi(\mathcal C_t)$ and the IB Lagrangian. The IB segment is at `draft` stage, so it's been less reviewed than the rest of the leaves. I'll be more careful there.

## Should the audit process change?

Not yet. The depends-drift finding is the kind of thing the §5.4 status-label-verification emphasis surfaces. I want to maintain a habit of checking depends against Formal Expression on each segment for the rest of the audit — it's cheap and catches mechanical drift. Let me note this as a standing micro-protocol.

**New micro-protocol for myself:** Before reading each segment's Discussion, scan the Formal Expression for any AAD-internal symbol (anything calligraphic or any AAD-specific named quantity), and verify the segment defining each such symbol is in `depends:`.

## Outline updates

Adding to running outline Section B (Findings) as a candidate:
- F-A1: depends drift on `scope-adaptive-system` (missing `def-chronica`) — mechanical/editorial.

Adding to Section E (Confirmation/calibration) note:
- The leaf-layer definitions (def-agent-environment / def-observation-function / def-action-transition / scope-adaptive-system / scope-agency / def-chronica) are well-shaped and honestly tier-labeled. The discipline is mostly working at the foundations.
