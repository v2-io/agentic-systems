---
kind: review
author:
  name: Claude Opus 5.5 (C.1 defender-noise checker 1)
  role: independent verifier
sources:
  - msc/inside-out-2026-10/c1-lanes/defender-noise-check-1.md
  - msc/inside-out-2026-10/c1-lanes/defender-noise-check-1.py
written: 2026-10-31T03:18:57Z
---

# The defender-noise lane (merge 60d2e8f6): independent check 1

KR C.1 ("Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier"). Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." This checks the landing in `294a30fb..b75b3f44`, merged as `60d2e8f6`, re-derived from the segment text. The reasoning, numbers and scope are in the first source. The mathematics that landed holds. Two sentences that it makes false are still in canon (F1, F2), and its normative claim is scored by the ratio (F3), for which a strengthening is proposed.

## C1 (check)
- target: segment:deriv-observation-noise-placement
- at: a4de9fa7
- act: rederive
- line: derivation
- criterion: P1(a)–(c), P2(a)–(b) and P3 follow from the Setup steady state $V_i = n(\sigma_{\text{env},i}^2 + \alpha_i^2\sigma_{\nu,i}^2)/(2\alpha_i)$ with Coupling Model S and the Model S window of #result-persistence-condition; P2(b)'s exponent is $1/2$ past $\alpha_A/\alpha_B \gg \gamma_B/\sigma_{\nu,A}$.
- committed: before
- outcome: confirmed
- recheck: By hand: the derivatives, the Kalman minimizer and value, the minimum of increasing functions for P1(b), feasibility $R_B^2 \gt n\sigma_{\text{env},B}\sigma_{\nu,B}$ and the fixed-gain quadratic for P1(c), the asymptotic ratio for P2(b). Numerically: local exponent $0.500$ to $\mathcal T_A = 10^5$ (script §4).
- read: seg:deriv-sector-condition, seg:result-persistence-condition, seg:der-adversarial-destabilization

## C2 (check)
- target: segment:deriv-observation-noise-placement
- at: a4de9fa7
- act: run
- line: simulation
- criterion: The closed form reproduces both recorded Variant-E exponent columns to within $0.003$; the split re-run's table is reproduced by the recipe; defender-only noise raises the ratio at every tempo ratio.
- committed: before
- outcome: confirmed
- recheck: Own closed form (script §1, four places: $1.0363, 1.0022, 0.9172, 0.5931, 0.1807$ and $1.0363, 0.9698, 0.9355, 0.6257, 0.3939$); `variant_e_noise_placement.py` re-run, every split number identical; defender-only ratio above the noiseless ratio at all twelve tempo ratios for 300 values of $s$ in $(0, 3]$ (script §2); `run_variant_e_adversarial` read: one noisy observation per step at gain `r * eta`.

## C3 (check)
- target: segment:result-adversarial-tempo-advantage
- at: a4de9fa7
- act: rederive
- line: derivation
- criterion: With self-injected channel noise the $3/2$ law needs $\gamma_A\mathcal T_A \gg \mathcal T_B\sigma_{\nu,B}$ and $\gamma_B\mathcal T_B \gg \mathcal T_A\sigma_{\nu,A}$; past a gain-raised tempo ratio of about $\gamma_B/\sigma_{\nu,A}$ the attacker's error grows linearly in its gain and its advantage grows as the square root of the tempo ratio.
- committed: before
- outcome: confirmed
- recheck: Algebra on $(\sigma_i^2 + \mathcal T_i^2\sigma_{\nu,i}^2)/(2\mathcal T_i)$; the event-rate sentence in the same paragraph is not part of this criterion (F2).
- read: seg:deriv-sector-condition, seg:result-persistence-condition

## C4 (check)
- target: segment:obs-gated-tempo-advantage
- at: a4de9fa7
- act: rederive
- line: derivation
- criterion: Lowering both agents' base gain to the Variant-E gain restores the exponent at $\sigma_{\text{obs}} = 1$ ($0.18 \to 0.39$) through the attacker's side, whose log-log slope moves from $+0.18$ to $-0.11$ while the defender's moves from $+0.36$ to $+0.29$.
- committed: before
- outcome: confirmed
- recheck: Script §3.
- read: seg:deriv-observation-noise-placement

## F1 (finding)
- target: segment:impl-cooperative-adversarial
- at: 60d2e8f6

Line 45 says the defender-side exploit "is not settled by either result … the net is an unmodeled trade, and the defender-side prescription is a hypothesis, not a framework prediction", gives the event-rate mechanism ("a faster attacker makes more corrections, each of them noisy"), and reads the collapse through Regime III. #deriv-observation-noise-placement P1 settles it as false, line 84 of the same file now says so, and the lane showed Variant E raised tempo by gain. The paragraph needs replacing with present truth; its last sentence (the superlinear exponent belongs to the coupling-dominant, low-observation-noise regime) stands.

## F2 (finding)
- target: segment:result-adversarial-tempo-advantage
- at: 60d2e8f6

Scope paragraph: "Tempo raised by event rate lowers $\sigma_\nu^2 \propto 1/\nu$ and keeps the coupling dominant." False for the attacker. At per-event gain $h$ the injected term is $\mathcal T_A h s^2$, linear in tempo, so $\mathcal T_A\sigma_{\nu,A} = s\sqrt{h\mathcal T_A}$ grows and the paragraph's own condition $\gamma_B\mathcal T_B \gg \mathcal T_A\sigma_{\nu,A}$ fails at $\mathcal T_A \sim \sigma_{\text{env},A}^2/(hs^2)$; past it the attacker's error tends to $nhs^2/2$ and the exponent goes $3/2 \to 1$ (script §4). Contradicts #deriv-observation-noise-placement P2(c). Event rate delays the loss of coupling dominance; it does not prevent it.

## F3 (finding)
- target: segment:deriv-observation-noise-placement
- at: 60d2e8f6

The normative claim ("degrade the attacker's observation and protect its own") and the Discussion ("through the attacker's error directly") rest on the ratio, while P2(a) states $V_B$ is unaffected by $\sigma_{\nu,A}$ at a fixed attacker gain, and neither $V_B$ nor $V_B/V_A$ has an interior maximum in $\alpha_A$ (script §5), so no damage- or ratio-seeking attacker backs off. Proposed strengthening (checked): an attacker persisting in mean square has $\alpha_A \lt \alpha_+(A) \leq 2R_A^2/(n\sigma_{\nu,A}^2)$ by #result-persistence-condition, so with P1(c) the defender persists at some gain against every persisting attacker when $2\gamma_A R_A^2/(n\sigma_{\nu,A}^2) \leq R_B^2/(n\sigma_{\nu,B}) - \sigma_{\text{base}}$. Landing it as a P4 would ground the normative claim in the defender's own persistence; otherwise the claim's register should say it is about the ratio.

## F4 (finding)
- target: segment:deriv-observation-noise-placement
- at: 60d2e8f6

P2(c) and the second claim's "False of" ("the exponent there stays above one half") can state the continuous-time asymptote: under event-rate tempo the attacker's error tends to the floor $nhs^2/2$ and the exponent tends to $1$. The script's §3 discrete form saturates (contraction $1 - (1-\eta)^r \to 1$), so its slopes are local, not this asymptote.

## F5 (finding)
- target: segment:deriv-observation-noise-placement
- at: 60d2e8f6

"Falls as $1/\sigma_{\nu,B}$" (P1(c) prose) and "inversely proportional" (Discussion) are exact only at $\sigma_{\text{base}} = 0$; the bound is $R_B^2/(n\sigma_{\nu,B}) - \sigma_{\text{base}}$. The same wording is in the #obs-gated-tempo-advantage lead, #impl-strategic-composition:63 and the 01-aat-core OUTLINE row.

## F6 (finding)
- target: segment:obs-gated-tempo-advantage
- at: 60d2e8f6

The lead's "lowering both agents' base gain toward the noise level keeps some of it" holds only at $\sigma_{\text{obs}} = 0.5, 1.0$. At $0.1$ and $0.2$ the Variant-E gain ($0.318$, $0.169$) is above the fixed $0.1$, and at $0.1$ the exponent is below the fixed-gain one ($0.970$ against $1.002$).

## F7 (finding)
- target: item:t1-gated-tempo-one-sided-noise-prescription
- at: 60d2e8f6

This item and item:gated-tempo-nu-versus-tempo-collision were closed `--by-commit 47d76999`, the lane's pre-rebase landing, which no ref reaches (`git for-each-ref --contains` is empty). On main it is `294a30fb`; the account's `5f5db8ea` is `e540fa62`. Annotate the two close events and correct the account's commit line.
