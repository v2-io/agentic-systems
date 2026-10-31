# C.1 lane: the defender-noise prescription, round 2

KR C.1, under "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." This round integrates independent check 1 (`defender-noise-check-1.md`, as corrected in `ecbdd902`) on top of main. Integrator: `c1-defender-noise`. Typed record: `reviews/defender-noise-round-2.md`. My own numbers come from a scratch script, whose results are restated below. Every proposal was re-derived before landing.

## Findings, and what landed

- **F1.** `#impl-cooperative-adversarial`:45 now states the placement result in place of the "not settled … a hypothesis" sentence, the "more corrections, each noisy" mechanism and the Regime-III reading. The checker said the paragraph's last sentence still stood. I sharpened it: the superlinear exponent belongs to the regime where the coupling dominates both the base disturbance and each agent's own injected noise.
- **F2.** In `#result-adversarial-tempo-advantage`'s scope paragraph, "event rate … keeps the coupling dominant" is replaced by the derived statement. At a fixed per-event gain $h$ the injected term is $\mathcal T h s^2$, linear in tempo. Dominance fails later, near $\mathcal T_A \sim \sigma_A^2/(hs^2)$, and the exponent goes to $1$. The coupling stays dominant only if the event rate grows at least as the square of tempo.
- **F3 → P4.** This is the checker's strengthening. I re-derived it from the Model S window of `#result-persistence-condition`. The cap $\alpha_+ \leq 2R_A^2/(n\sigma_{\nu,A}^2)$ holds for every $\sigma_{\text{env},A}$, since the square root is at most $R_A^2$. Together with P1(c) it gives the stated sufficient condition, and strictness carries through. I checked the cap on 20,000 random draws of my own (11,221 with a persistence window, no violation), and the combined condition on 7,912 draws that satisfied it, with the defender at its Kalman gain against every persistent attacker gain on a grid (no failure). Landed as P4. The normative claim's register, population, true-of and false-of now rest on P1(c) and P4. The Discussion no longer says attacker-channel noise helps "through the attacker's error directly". The Working Note now says which attacker objective decides the coupled case. This follows the corrected F3: damage gives no reason to lower gain; the ratio has a local maximum near the Kalman gain under weak coupling but no finite global one; a Kalman-tuned attacker lowers its gain as its channel noise rises. P4 is scoped to attackers that must persist on a fixed channel, and it names the two that escape it: an attacker willing to leave its region, and one raising its event rate, whose cap grows as $\nu_A$.
- **F4.** P2(c) now derives the event-rate exponent ($3/2 \to 1$, with the crossover and the asymptotic ratio). The Claim Record's "False of" says $1$. The script's and results file's §3 slopes are labeled as local.
- **F5.** "Falls as $1/\sigma_{\nu,B}$" and "inverse proportion" are corrected to $R_B^2/(n\sigma_{\nu,B}) - \sigma_{\text{base}}$ in P1(c), the Discussion, the `#obs-gated-tempo-advantage` lead, `#impl-strategic-composition` and the OUTLINE row. P1(b)'s "$K_B$ falls as $1/\sigma_{\nu,B}$" is exact at a given attacker tempo and stays.
- **F6.** The obs-gated lead is limited to the two highest noise levels.
- **F7.** Left to the checker, as asked.
- **F8.** The runtime now reads "a few seconds". One point in F8 is not right, and I didn't change the code for it. The trial count of 150 is the recorded E3 call's (`variant_ef_extensions.py` `main()` passes `num_trials=150`); 200 is only the function's default. The docstring now says so.

## Found by grepping the mechanism phrases

The checker suggested grepping for the mechanism a fix refutes. The same "faster loop, noisier result" mechanism appeared in four more places.

- **`#def-adaptive-tempo`:52.** "Collapses tempo regardless of loop speed. You cannot outrun a bad observation channel by iterating faster." This contradicted `#result-persistence-condition`'s event-rate lever ("This is the lever that raises $\mathcal T$"). With independent per-event noise, $\sigma_\nu^2 = s^2/\nu$, so the tempo at the optimal gain is $\sigma_{\text{env}}\sqrt\nu/s$. My discrete Kalman check gives $\nu K = 0.62, 1.56, 3.53, 7.52, 15.51$ at $\nu = 1, 4, 16, 64, 256$, which approaches $\sqrt\nu$. The body now says what is true: four times the events buy twice the tempo; noise more readings do not average away (a shared bias, or a Model D bounded floor) is not outrun; and correcting harder on the same observations adds error. Its WN gold bullet says why the sentence failed, as a regression guard. This answers my own open question, `question:does-def-adaptive-tempo-52-you-cannot-outrun-a-b`.
- **`#der-code-quality-as-observation-infrastructure`:101 (TST).** It copied the sentence. It now separates independent reading noise, which averages slowly, from the shared bias bad code puts into every reading (a misleading name misleads each pass the same way). The domain mapping is a reading, not a derivation.
- **Two obs-gated gold notes.** The noisy-speedometer note now says it is true when the faster loop corrects harder per reading. The "out-hire a bad codebase" note now says the collapse to 1x is exact only for shared noise.
- **`#result-adversarial-exponent-regimes`:68** (the checker's adjacent note). "Varies attack vectors increases observation noise" called Model S coupling observation noise. It now says the opponent adds disturbance the target must track, and that corrupting the target's observations is a different model, which P1's "False of" names.

## What a checker should look at

1. P4: the cap, the combined condition, and whether its population is right. Is "an attacker that must persist" the right premise, or should the criterion be the attacker's expected stay rather than mean-square persistence?
2. P2(c)'s crossover and asymptotic ratio $\gamma_A\alpha_A/(s_A\sqrt{h_A\alpha_B})$.
3. `#def-adaptive-tempo`:52. This is a Part I definition at `claims-verified`. The edit is a Discussion paragraph and its WN, and `vsect revise` showed no check resting on its text. Check the $\sqrt\nu$ statement against `#result-persistence-condition` and `#deriv-tempo-additivity`.
4. Whether any other surface still carries "regardless of loop speed" or "event rate keeps the coupling dominant". I grepped 01–04 and the README partials.
5. Lapsed checks: `vsect revise` reported ten checks resting on the old text of `#deriv-observation-noise-placement`, `#obs-gated-tempo-advantage`, `#result-adversarial-tempo-advantage` and `#disc-constructive-impossibility-posture` (the last through a dependency). They need a second mind's `vsect confirm --checks …`. Scope it, as check 1 warned.

6. Check 1's findings F1–F6 and F8 are still open in `vsect open`. vsect lets only a mind other than the reviser mark a finding answered (`vsect findings --answered review:defender-noise-check-1#Fn --by-revision …`), so that falls to the next checker. The revision is `2f622c4b` on this branch.

## Open

- `question:model-s-total-disturbance-downstream` stays open for its non-adversarial segments.
- The coupled best-response case is in the Working Note.
- `CURRENT-VOL1*` is for the lead's rebuild.
