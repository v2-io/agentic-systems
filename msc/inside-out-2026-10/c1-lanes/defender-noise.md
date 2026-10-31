# C.1 lane: the defender-noise prescription

KR C.1 (under "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself."): every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier. Items: `item:t1-gated-tempo-one-sided-noise-prescription`, and `item:gated-tempo-nu-versus-tempo-collision` (same lines). Integrator: `c1-defender-noise`. Commits are on this lane's branch, named below.

## What was false, and what is true

Volume 1 said noise on the defender's own observation channel is a cheap defense against a faster attacker. "Without changing tempo or gain" is true of that lever at fixed gain (the drain's correction, `c19dc6d7`). The prescription is false at the level that matters, and not only because re-tuning costs gain. Even at fixed gain, defender-channel noise raises the defender's error and the mismatch ratio at every tempo ratio. The exponent falls only because the defender's error gains a term the attacker does not drive, so the slope flattens while the level rises.

Derived in the new segment `#deriv-observation-noise-placement` from the Setup of `#deriv-sector-condition`, $V_i = n(\sigma_{\text{env},i}^2 + \alpha_i^2\sigma_{\nu,i}^2)/(2\alpha_i)$, with Coupling Model S:

- **P1 (defender's channel).** $\partial V_B/\partial\sigma_{\nu,B} = n\alpha_B\sigma_{\nu,B} \gt 0$ at every gain, and $V_A$ is unaffected. The attacker's per-unit-tempo effect on $V_B$ does not depend on $\sigma_{\nu,B}$. At its Kalman gain the defender's error is $n\sigma_{\text{env},B}\sigma_{\nu,B}$ and its tempo $\sigma_{\text{env},B}/\sigma_{\nu,B}$ falls. From the window of `#deriv-sector-condition` / `#result-persistence-condition`, the attacker tempo survivable at any gain is $\gamma_A\mathcal T_A \lt R_B^2/(n\sigma_{\nu,B}) - \sigma_{\text{base}}$. Model D gets a qualitative statement only.
- **P2 (attacker's channel).** This is where noise reduces the advantage. With tempo raised by gain, the exponent goes from $3/2$ to $1/2$ past the tempo ratio $\gamma_B/\sigma_{\nu,A}$, and the advantage still grows. The defender's own error falls only if the attacker lowers its gain. Event-rate tempo is in closed form only.
- **P3 (shared base noise).** The ratio compresses toward $(\alpha_A/\alpha_B)^{1/2}$. The slower agent's error rises by more, and its threshold falls.

## The simulation, re-checked

Variant E (`variant_ef_extensions.py`) put the same noise on both channels. It also raised the attacker's tempo by gain on one noisy observation per step, although its docstring says event rate. The closed form reproduces both recorded columns to within $0.003$. I re-ran the same loop with the channels separated (seed 42), and the collapse belongs to the attacker's channel. Defender-only noise at $s = 1$ gives slope $0.82$, and the ratio at $r = 4$ rises from $4.58$ to $4.93$. Attacker-only noise gives $0.40$ and $1.11$. Recipe: `empirica/track-b-nonlinear/variants/variant_e_noise_placement.py` (`python3 -I` from that directory, about a minute). Output: `variant_e_noise_placement_results.md` (MANIFEST and RUNS rows added). The "optimal" column is not each agent's optimum: the attacker runs at $r\,\eta^\ast$. The canon text no longer says it is.

## What landed

- New: `#deriv-observation-noise-placement`, with an OUTLINE row placed before `#result-adversarial-exponent-regimes`. It has a Claim Record: two formal claims and one normative, all with "Instantiated: no".
- `#obs-gated-tempo-advantage`: lead, mechanism, Epistemic Status (the table is now reproduced by the closed form), the Boyd paragraph (gain-raised vs event-rate), Practical implication, and the recipient-side paragraph. The discharged $\nu$-vs-$\mathcal T$ off-ramp is removed.
- `#result-adversarial-exponent-regimes`: line 18 (the true fixed-gain clause is kept and its cost stated) and the WN forward-vision note. Raising $\rho_{\text{base}}$ is no defense of the slower agent, and chaff is attacker-channel noise.
- `#impl-strategic-composition`: lines 60 and 62. I un-conflated the non-coupling-dominant regime from observation noise.
- `#der-interaction-channel-classification`: the two recovery bullets, the (I-c) source cells, and the "recovered restrictions" lists (five to four).
- `#impl-cooperative-adversarial`: the do-not-restore entry now points at the derivation.
- `#obs-section-i-validation-simulations`: attribution sentence and table cell.
- `#result-adversarial-tempo-advantage`: scope paragraph. "Its advantage stops growing" was false, because the ratio grows as the square root of the tempo ratio. The paragraph now points at the derivation for the exponent regimes under gain-dependent noise.
- CHANGELOG entry under 2026-10-30.
- Not done: `CURRENT-VOL1*`, which the lead rebuilds at merge. Its lines 10991, 11056 and 11144 carry the old text until then.

## What a checker should look at

1. The P1(c) bound and the fixed-gain threshold $\sqrt{2\alpha_B R_B^2/n - \alpha_B^2\sigma_{\nu,B}^2} - \sigma_{\text{base}}$. Both rest on the `#deriv-sector-condition` window, which another lane owns.
2. P2(b)'s asymptotics. I checked the $1/2$ limit numerically: local slope $0.500$ at large $\alpha_A$.
3. Whether P1(b)'s wording is right. Re-tuning lowers the defender's error below the fixed-gain value on the same channel, but not below the noise-free value, and the ratio rises along the re-tuned path. My first draft wrongly said the ratio rises "by more than at fixed gain". I corrected it before commit, and the same correction ran through four bodies ("re-tuning does not undo this", not "pays further").
4. Re-run the script. Check that the closed-form columns match `variant_ef_results.md` and that the split table matches.
5. The `#der-interaction-channel-classification` change. Its recovery list now says `#obs-gated-tempo-advantage` is not a restriction. Line 163's opacity-dual sentence ("the emitter's advantage degrades when its observations of the environment are noisy") is consistent with that and was left as is.

## Left open, on the ledger

- `question:model-s-total-disturbance-downstream`: this segment answers its adversarial-exponent part (3/2 needs the coupling to dominate each agent's injected noise; past that, 1/2 under gain-raised tempo). The per-dimension, matrix and discrete parts are untouched, so I left it open.
- `#def-adaptive-tempo`:52, "You cannot outrun a bad observation channel by iterating faster", is in tension with $\sigma_\nu^2 \propto 1/\nu$ for independent observations. I raised it as a question rather than fixing it.
- The fully coupled case, where each agent best-responds with its gain, is the segment's Working Note, with its home in `#deriv-strategic-composition`.
