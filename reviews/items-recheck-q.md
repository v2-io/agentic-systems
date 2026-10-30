---
kind: review
author:
  name: Claude Opus 5.5 (item rechecker, q-proposals lane)
  role: rechecker
sources:
  - msc/inside-out-2026-10/items-recheck/q-proposals.md
written: 2026-10-30
---

# Findings from re-checking the proposal trackers

KR I.3. These came up while judging the 75 items imported from `PROPOSALS.md`, `spikes/PROPOSED-ADVANCED.md` and `spikes/PROPOSED.md` against HEAD. F1 and F2 are the pattern the pilot named in its §2.8: a Working Note that reports something about the body which the body does not bear out. F3 to F6 are defects in bodies that a proposal had named and nobody fixed. The lane document above has the context for each.

## F1 (finding)
- target: segment:disc-stability-certificate
- at: cd668c8c

Working-Note status signal: two Working Notes (:113 and :131) say the Findings Brief's "measuring-stick" analog conflates the metric with the contraction property, so a reader might miss that the stick is chosen so corrections shrink it, and queue a sharpening. The Brief (:92, unchanged since b599c4a6) already defines the stick by that property in its first sentence: "is there a way of measuring 'how far off am I?' such that every correction the agent makes provably shrinks that measure faster than the world pushes it back out? That measuring-stick is the stability certificate." The notes report a defect the body does not have.

## F2 (finding)
- target: segment:def-action-transition
- at: cd668c8c

Working-Note status signal: the Working Note at :67 argues that `*[Definition (transition opacity)]*` may be mistyped because the atom "restricts epistemic access" ("the agent does not know $T$ exactly"). Since 492a1492 the atom says the agent *may* not know $T$, names the unknown content $\theta_T$, and says opacity is not required of every system in scope (:31-33). That introduces a named quantity, so the typing question the note keeps open no longer arises from the body. The parallel atom in `#def-observation-function` (:35-37) changed the same way.

## F3 (finding)
- target: segment:deriv-critical-mass-composition
- at: cd668c8c

(UO-mult), $\gamma(U_O) = -\gamma_{\max} U_O$, is tagged `*[Derived (unity-multiplicative-modulator, conditional on LQR-compatible action structure)]*` (:82), while the segment's own derivation table (:123) and Epistemic Status (:142) call it a discussion-grade sketch. The body also states it without the scope its own Working Note (:253) shows it needs: under resource contention, identical targets can maximize interference, so $U_O = 1$ can give $\gamma \gt 0$. The tag overstates the register and the statement lacks a non-rivalrous scope; (CM3) and (CM4) inherit both.

## F4 (finding)
- target: segment:disc-additive-coordinate-forcing
- at: cd668c8c

The table's chain row (:43) lists Cauchy-FE as the uniqueness mechanism that forces log-probability, while its own axiom cell says the chain rule is "a mathematical identity, not an AAT axiom", and the segment defines *forced* as "a uniqueness theorem on an independently-motivated AAT-internal axiom" (:20). By that definition the chain layer is not forced; the prose calls it the motivational anchor (:48, :52). Found on 2026-08-22 and routed to PROPOSALS E.3, not fixed.

## F5 (finding)
- target: segment:scope-composite-agent
- at: cd668c8c

The segment justifies being a scope condition by requiring a well-defined composite objective: "If the sub-agents' objectives do not align under any common $O_c$, then $G_c$ is ill-defined and the composite is a fiction … composition applies where $G_c$ is well-defined" (:83). Route (C-iii) admits composites with "No explicit common objective" (:44-48), and (C-iv) admits equilibrium-convergent groups that have none either. The segment's justification and two of its four routes contradict each other. This is the F-V3 finding of 2026-04-25, whose interim fix (an induced $O_c$ via the relevance variable $Y$) was never landed; the structural alternative is SP-21.

## F6 (finding)
- target: segment:disc-value-functional-grounding-floor
- at: cd668c8c

The body states as fact that the agent-side and principal-side grounding routes exhaust the escapes: "There is no third route internal to the value functional; there are no other off-substrate axes a non-degenerate non-pathological agent can be grounded on" (:101, repeated at :129). Nothing in the segment derives this; its Epistemic Status says the cluster "carries no theorem of its own" (:107), and its Working Note calls the exhaustion intuition-only (:157). The sentence wants either a derivation or a conjecture's marking.
