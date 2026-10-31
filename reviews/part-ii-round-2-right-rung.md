---
kind: review
author:
  name: Claude Fable 5.1 (Part II round-2, right-rung cluster)
  role: integrator
sources:
  - msc/inside-out-2026-10/part-ii-round-2-right-rung.md
  - reviews/part-ii-check-1-b1-records.md
  - reviews/part-ii-check-1-identification.md
  - spikes/spike-loop-identification-decision-state-2026-10-30/check-part-ii-round-2-right-rung-rectangular.py
written: 2026-10-30
---

# Part II round 2, the right rung of convention monotonicity: the integrator's re-derivations and runs

KR **C.2** with **B.1** and **C.1** (`msc/inside-out-2026-10/INTENT.md`). Top intent: "Complete 'in-place' refactor of ASF-- meta, all artifacts, and theory itself." These are the checks I ran before and while landing the right-rung cluster in the worktree `agent-a6f35eff1ab6cd9c4` on top of `3d17de13`; the text checked is the uncommitted working tree there (`committed: before`), which the Part II round-2 integrator commits by naming paths. The two checkers' proposals were treated as inputs to re-derive, not as text to transcribe; where a proposal was confirmed it is recorded as confirmed by this mind's own derivation or run, and the one place I sharpened a checker's statement is C1. "Run" means a `python3 -I` script whose output is quoted; "rederive" means by hand. The account in the first source says what each finding's answer is and where it landed.

## C1 (check)
- target: segment:deriv-convention-monotonicity
- at: 3d17de13
- act: run
- line: derivation
- criterion: The rectangularity claim as landed: for a rectangular class (all time-indexed Markov policies with state-wise admissible action sets, first-action supremum over $A_\Pi(x)$), (M) and (PC) hold for every maximizer, the rung $A_O^{\text{RH}} \leq A_O^{\text{B}}$ holds on both readings for every maximizer, and (SO) is guaranteed only for the backward-induction maximizer.
- committed: before
- outcome: confirmed
- recheck: `python3 -I spikes/spike-loop-identification-decision-state-2026-10-30/check-part-ii-round-2-right-rung-rectangular.py`. Instance: $x \to s$ by $z$ or $z'$ (both pay $0$); $s$: $c$ pays $5$ to $s_1$, $d$ pays $0$ to $s_2$; $s_1$: $e_1$ pays $0$, $e_2$ pays $10$; $s_2$: $f$ pays $6$; $N_h = 3$, $N_r = 1$. All $27$ rectangular classes (every nonempty choice of admissible sets at $x$, $s$, $s_1$) enumerated, every maximizer of $V_O$ from $x$ tried as $\pi^\ast$: (M) true, (PC) true, rung true on both readings in all $27$; (SO) and (G) held for every maximizer there, because both first actions reach the same state. Instance 2: $x \to s_1$ by $a_1$ ($0$), $x \to s_2$ by $a_2$ ($0$); $s_1$: $b$ pays $10$; $s_2$: $c_1$ pays $5$, $c_2$ pays $0$; full rectangular class ($16$ policies), $8$ maximizers, (SO) holds for $4$ of them, (G) for all $8$, rung true on both readings for all $8$.

The B.1 checker's argument (its C2) says Bellman's equation on the restricted process makes $\pi^\ast$ optimal from every state. That is true of the backward-induction optimum and not of an arbitrary maximizer of $V_O$ from $x$, which is unconstrained at states its own first action does not reach (instance 2: a maximizer taking $a_1$ then $c_2$ at the unreached $s_2$ fails (SO) at $s_2$). The rung survives for every maximizer through (M) and (PC), and the appendix states it at that precision. Everything else in the checker's rectangularity paragraph held.

## C2 (check)
- target: segment:deriv-convention-monotonicity
- at: 3d17de13
- act: run
- line: derivation
- criterion: The (M)-failure instance as landed: (PC) and (SO) hold, the stitched replanner is not a member, and $A_O^{\text{RH}} = 15 \gt 6 = A_O^{\text{B}}$ on both readings; the four-member variant with a second first action has (PC) non-trivially and the same numbers.
- committed: before
- outcome: confirmed
- recheck: same script. Two-member class $\{(z, c, e_1, f), (z, d, e_2, f)\}$: $M$ false, $PC$ true, $A^{\text{RH}} = 15$, $\sup_\Pi V = 6$, one maximizer with (SO) and (G), rung false on both readings. Four-member product $\{z, z'\} \times \{\text{tail } A, \text{tail } B\}$: $M$ false, $PC$ true, (SO) for both maximizers, $15$ against $6$, rung false on both readings. Also re-ran the identification checker's `check-part-ii-check-1-right-rung-rh-not-in-pi.py`: $\pi_{\text{RH}} = (z, c, e_2, f) \notin \Pi$, $A^{\text{RH}} = 15$, $A^{\text{B}} = 6$. The B.1 checker's own instance ($51$ against $10$) re-derived by hand with the same structure; the appendix carries $15$ against $6$ because `#def-value-object` cites those numbers.

## C3 (check)
- target: segment:deriv-convention-monotonicity
- at: 3d17de13
- act: run
- line: derivation
- criterion: The readings-part instance as landed: (M) and (SO) hold, (PC) and (G) fail, the rung holds on the first-action reading ($51 \leq 51$) and fails on the class-supremum reading ($51 \gt 12$).
- committed: before
- outcome: confirmed
- recheck: same script, instance 3: $x$: $p$ pays $2$ to $H$, $g$ pays $1$ to $D$; $H$: $u$ pays $10$; $D$: $d_1$ pays $0$, $d_2$ pays $50$; $\Pi = \{(p, u, d_2), (g, u, d_1)\}$. Output: $M$ true, $PC$ false, $A^{\text{RH}} = 51$, $\sup_\Pi V = 12$, one maximizer, (SO) true, (G) false, rung true on the $Q$-reading, false on the $V$-reading. By hand: $Q(g; \pi_A) = 1 + 50 = 51$, $Q(p; \pi_A) = 2 + 10 = 12$; the replanner's one-step window at $x$ prefers $p$ ($2 \gt 1$) so $\pi_{\text{RH}} = \pi_A$.

## C4 (check)
- target: segment:deriv-convention-monotonicity
- at: 3d17de13
- act: rederive
- line: derivation
- criterion: The instance $(x, H, D)$ as landed: (M) holds, (PC) and (SO) fail, $A_O^{\text{RH}} = 100 \gt 10 = A_O^{\text{B}}$ on both readings; with $\pi_{\text{current}} = \pi_1$, $A_O^{(1)} = 100 \gt A_O^{\text{B}}$.
- committed: before
- outcome: confirmed
- recheck: $V(\pi_1) = 1$, $V(\pi_2) = 10$, $\pi^\ast = \pi_2$; $\max_a Q(a; \pi_2) = \max(1, 10) = 10$; replanner takes $g$ at $x$ and $w$ at $H$, so $\pi_{\text{RH}} = \pi_1 \in \Pi$; $Q(p; \pi_1) = 0 + 100$; $p \oplus \pi_1 \notin \Pi$; $\pi_2$ takes $u$ at $H$ where $w$ pays more. With $\pi_{\text{current}} = \pi_1$, $A^{(1)} = \max(Q(g; \pi_1), Q(p; \pi_1)) = 100$.

## C5 (check)
- target: segment:deriv-convention-monotonicity
- at: 3d17de13
- act: rederive
- line: derivation
- criterion: The two branches as landed. (PC) with (M): $Q(a; \pi_{\text{RH}}) = V(a \oplus \pi_{\text{RH}}) \leq \sup_\Pi V \leq \sup_a Q(a; \pi^\ast)$, both readings, and the readings coincide. (SO) with (M): $Q(a; \pi_{\text{RH}}) \leq Q(a; \pi^\ast)$ for each $a$, first-action reading only; readings coincide with (G). The maximizer remark: under (PC) every maximizer gives $\sup_\Pi V$; under (SO) every (SO)-maximizer gives $\sup_a \mathbb{E}[r(a) + \sup_\Pi V(s')]$.
- committed: before
- outcome: confirmed
- recheck: (PC) applied to $\pi^\ast$ itself gives $\sup_a Q(a; \pi^\ast) \leq \sup_\Pi V$, and $\geq$ is the own-first-action step, so equality. Under (SO), $Q(a; \pi^\ast) = \mathbb{E}[r(a) + \sup_\Pi V(s', \cdot; N_h - 1)]$ for each $a$ by the hypothesis itself, so the supremum over $a$ does not depend on which (SO)-maximizer is used; under (G), $\sup_a Q(a; \pi^\ast) = Q(\pi^\ast(x); \pi^\ast) = V(\pi^\ast)$. For history-dependent $\pi$ the state $s'$ is read as the history through $a$, which the appendix now says once.

## C6 (check)
- target: segment:deriv-convention-monotonicity
- at: 3d17de13
- act: rederive
- line: derivation
- criterion: The unconditional half: $\sup_a Q(a; \pi^\ast) \geq \sup_\Pi V$ for every $\Pi$, so $\delta_{\text{sat}}^{\text{B}} \gt 0$ implies no member of $\Pi$ reaches the threshold; the converse needs (PC) or (G), and under (SO) alone certifies a first action followed by $\pi^\ast$.
- committed: before
- outcome: confirmed
- recheck: $Q(\pi^\ast(x); \pi^\ast) = V(\pi^\ast) = \sup_\Pi V$, so the supremum over $a$ is at least that. Converse: $\delta^{\text{B}} \leq 0$ means some $a$ has $Q(a; \pi^\ast) \geq V^{\min}$; the policy achieving it is $a \oplus \pi^\ast$, a member under (PC), equal to $\pi^\ast$ under (G), and otherwise possibly outside $\Pi$ (instance 3: $g \oplus \pi_A$ worth $51 \notin \Pi$).

## C7 (check)
- target: segment:deriv-convention-monotonicity
- at: 3d17de13
- act: rederive
- line: derivation
- criterion: C1 against C3 directly (the B.1 checker's C4): $A_O^{(1)} \leq A_O^{\text{B}}$ under $\pi_{\text{current}} \in \Pi$ and (PC) on both readings, or (SO) on the first-action reading, with no (M) and no order-consistency; fails without them.
- committed: before
- outcome: confirmed
- recheck: (PC): $Q(a; \pi_{\text{current}}) = V(a \oplus \pi_{\text{current}}) \leq \sup_\Pi V$. (SO): $Q(a; \pi_{\text{current}}) = \mathbb{E}[r(a) + V(s', \pi_{\text{current}})] \leq \mathbb{E}[r(a) + V(s', \pi^\ast)] = Q(a; \pi^\ast)$, using only $\pi_{\text{current}} \in \Pi$ at $s'$. Failures: $(x, H, D)$ with $\pi_{\text{current}} = \pi_1$, $100 \gt 10$; instance 3 with $\pi_{\text{current}} = \pi_A$, $A^{(1)} = 51 \gt 12 = V(\pi^\ast)$ on the class-supremum reading. This is what `#deriv-self-actuation-grounding` Lemma 1 should cite in place of the two-rung chain (F2 below).

## C8 (check)
- target: segment:def-control-regret
- at: 3d17de13
- act: rederive
- line: derivation
- criterion: Non-negativity of $\delta_{\text{regret}}$ as now stated: under C1 for every class; under C3 given $\pi_{\text{current}} \in \Pi$ on either reading; under C2 given order-consistency, and negative for an unguarded replanner on the left-rung instance.
- committed: before
- outcome: confirmed
- recheck: C1: $A^{(1)} = \sup_a Q(a; \pi_{\text{current}}) \geq Q(\pi_{\text{current}}(x); \pi_{\text{current}}) = V(\pi_{\text{current}})$. C3: $\sup_a Q(a; \pi^\ast) \geq \sup_\Pi V \geq V(\pi_{\text{current}})$ given membership. C2: $A^{\text{RH}} \geq V(\pi_{\text{RH}})$ always, and $V(\pi_{\text{RH}}) \geq V(\pi_{\text{current}})$ is the left rung's order-consistency content; left-rung instance: $A^{\text{RH}} = 1$, $V(\pi_{\text{current}}) = 10$ (patient at $x$, then $10$ in $H$), so $\delta^{\text{RH}}_{\text{regret}} = -9$.

## C9 (check)
- target: segment:def-satisfaction-gap
- at: 3d17de13
- act: rederive
- line: derivation
- criterion: The aspiration hypothesis (B.1 checker's C5): with $\pi_f$ the $\Pi$-optimum of $O_f$ and $\pi_a \in \Pi$, $V_{O_f}(\pi_a) \gt V_{O_f}(\pi_f)$ is impossible; restated for a bounded planner's reach it is a hypothesis with a nonempty population and the exact optimizer as its False-of.
- committed: before
- outcome: confirmed
- recheck: $\pi_f \in \arg\sup_{\pi \in \Pi} V_{O_f}(M_t, \pi)$ and $\pi_a \in \Pi$ give $V_{O_f}(\pi_a) \leq V_{O_f}(\pi_f)$ by the definition of a supremum; the previous Population ("whose policy under each is the optimum for that objective in $\Pi$") therefore lay inside the False-of. The restatement with $\pi_a = \mathcal{P}(O_a)$, $\pi_f = \mathcal{P}(O_f)$ leaves the displayed inequality open, which is what a hypothesis needs; `#der-orient-cascade` R2's False-of and `#disc-structural-imagination` cite the hypothesis by its tag and informal content and need no change.

## C10 (check)
- target: segment:form-objective-functional
- at: 3d17de13
- act: read-check
- line: derivation
- criterion: (B.1 checker's C10) The identity sentence equated "incommensurable objectives and no priority structure" with (E1); (E1) as the segment defines it is a strict priority; the stated exclusion is incompleteness, a failure of (A1), the Pareto case; lexicographic ordering on a continuum has no real-valued representation and so is not a diagnostic-preserving scalarization there.
- committed: before
- outcome: confirmed
- recheck: the segment's own definition of (E1): "genuinely incommensurable objectives with a strict priority but no tradeoff rate". A preference with no priority and no tradeoff rate is one in which some pairs are unranked, which is incompleteness, and a real-valued $V$ induces a complete preorder, so the interface excludes it. Debreu's $\mathbb{R}^2$ lexicographic counterexample (not order-separable, no real-valued representation) and the countable-domain representability of every complete preorder are stated from knowledge; I did not open Debreu (1954). The three carriers in the segment (the summary's Approximation sentence, the Epistemic Status identity sentence, the Approximation item) now name three exclusions and drop "lexicographic ordering" from the scalarization lists except on a countable domain.

## C11 (check)
- target: segment:def-value-object
- at: 3d17de13
- act: read-check
- line: derivation
- criterion: Does the right-rung text the Part II round-2 integrator landed in `#def-value-object` (summary :21, C3 paragraph :81, Monotonicity :91 and :101, corollary :113, Epistemic Status :137, Record 3 :169–181) say the same thing as the appendix as now landed, and is each of its statements one the appendix derives or exhibits?
- committed: before
- outcome: confirmed
- recheck: read against C1–C7 above. (M) with (PC) or (SO) on the first-action reading, matched; "(SO) alone does not make the two readings coincide", C3 above; "a prefix-closed two-member class with (SO) holding and $A_O^{\text{RH}} = 15 \gt A_O^{\text{B}} = 6$", C2; rectangular classes have all three, C1 (with the maximizer precision the appendix adds); the $(x, H, D)$ instance, C4; the unconditional half and the converse's hypotheses, C6; the C1-against-C3 direct comparison in Record 3's True-of, C7; :81's equality clause "or $\pi^\ast$'s own first action is a best first action under $\pi^\ast$ as continuation" is (G), C5. Nothing disagrees. One thing is unstated there and is F1 below.

## C12 (check)
- target: segment:deriv-convention-monotonicity
- at: 3d17de13
- act: run
- line: derivation
- criterion: After converting the Findings block to the `format.sop.md` field names, `bin/extract-findings` carries the entry into `FINDINGS.md` with no "Missing field" warning, and `bin/refresh-all --check` is clean once the README is rebuilt.
- committed: before
- outcome: confirmed
- recheck: `bin/extract-findings` wrote $50$ findings; `grep -c "Missing field" FINDINGS.md` gives $0$; the entry is at `FINDINGS.md` "Convention monotonicity holds rung by rung under named hypotheses". `bin/refresh-all --check` then showed only `README.md` stale (its findings-summary partial changed); `bin/refresh-all` rebuilt it and the check is clean. `md-press --check` on the five edited segments reports nothing to change.

## F1 (finding)
- target: segment:def-value-object

On the first-action reading, $A_O^{\text{B}} = \sup_a Q_O(M_t, a; \pi^\ast, N_h)$ (:81) depends on which maximizer serves as $\pi^\ast$ when $\Pi$ has several: maximizers of $V_O$ from $x$ can differ at states their own first action does not reach, and the first-action supremum reaches those states. Under (PC) the dependence vanishes (every maximizer gives $\sup_\Pi V_O$); under (SO) it vanishes among the maximizers satisfying (SO). The appendix now carries this as a one-paragraph remark. The definition could carry one clause at :81 — "for a maximizer $\pi^\ast$ satisfying (PC)'s or (SO)'s hypothesis the value does not depend on which maximizer is chosen; in general it does" — so that the quantity the records are about is well-defined by the definition rather than by the appendix. Not landed here: `#def-value-object` is the Part II round-2 integrator's.

## F2 (finding)
- target: segment:deriv-self-actuation-grounding

Held by the Volume 4 lane; the B.1 checker's C4 narrowing stands and the replacement text is written out in the account (§4). In short: Lemma 1's parenthesis should cite the direct C1-against-C3 comparison — "$A_O^{(1)} \leq A_O^{\text{B}}$ holds directly under $\pi_{\text{current}} \in \Pi$ and (PC) on both readings or (SO) on the first-action reading ( #deriv-convention-monotonicity, Corollary orderings), with no order-consistency and no membership of the replanner" — in place of "each rung under its own hypothesis … prefix-closure of $\Pi$ or state-wise optimality of $\pi^\ast$ for the right rung, order-consistency (RH-1/2/3) for the left"; the superset sentence then needs only those two hypotheses; and the status-table row :80 "#def-value-object Corollary (static-evaluation form, exact)" should carry them. The Assembly's use ("the only convention-invariant infeasibility verdict is the C3 reading") is unaffected, and the unconditional half makes "a genuine infeasibility verdict requires the C3/Bellman reading" true for every $\Pi$.

## F3 (finding)
- target: segment:deriv-convention-monotonicity

The `01-aat-core/OUTLINE.md` row for this segment (:341 at the working tree) still reads "right rung … exact under prefix-closure of $\Pi$ or state-wise optimality of $\pi^\ast$ (two-policy counterexample without either)". A sibling lane holds that file; the replacement row text is in the account (§4) for the Part II round-2 integrator to land. `CURRENT-VOL1.md` and `CURRENT-VOL1-APPENDICES.md` carry the superseded appendix, definition, satisfaction-gap and control-regret text at seven sites and are rebuilt, not patched (`bin/build-monograph --public --split-appendices --compact-fields --emit-current 01`); I did not run the build.

## What I did not check

Not opened: Debreu (1954), Bertsekas (2020), Rawlings, Mayne & Diehl (2017), Grüne & Pannek (2017); statements about them are from knowledge, marked `intuition-only` in the segment's Search Log as before. Not searched: the restricted-policy-class literature for the (M) membership hypothesis or for rectangularity as a named condition; the Search Log says `not-conducted`. Not re-derived: the left-rung derivations (RH-1/2/3) and the left-rung instance beyond the one line C8 uses; they were not changed. Not read: `#impl-strategy-structure` beyond :23, :43 and :72; `#deriv-self-actuation-grounding` beyond Lemma 1, the Assembly and :80. The stochastic case of (SO) with (M) is derived at the level of the expectation over $s'$ and not instanced; every instance here is deterministic. `vsect revise` on `#impl-strategy-structure` found no recorded act on that segment, so its version change is not in the ledger as a classified rewording.
