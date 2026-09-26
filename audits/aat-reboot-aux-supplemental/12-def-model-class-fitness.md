# Supplemental 12 — `def-model-class-fitness`

*Finder, 2026-09-25, at `875e1ac3`. Companion to `~/src/aat-reboot/scratch/aux/12-def-model-class-fitness.md`. Notes are tagged with the slugs they bear on.*

## Passed checks (please add to the Working Notes of `def-model-class-fitness`)

- `[def-model-class-fitness]` Checked the B-2 companion landing (CHANGELOG 2026-07-03, `CHANGELOG.md:229`) against the body: the systematic-residual qualifier is present at :14 and in "Detecting low class fitness" (:38), and the normalized-fraction point ("an agent at $S = \mathcal F = 1$ in a noisy world still faces an arbitrarily high absolute mismatch floor") is there. Holds.
- `[def-model-class-fitness, def-model-sufficiency]` Checked "$S = \mathcal F = 1$ is compatible with an arbitrarily high absolute floor" against `def-model-sufficiency.md:22` and `result-mismatch-decomposition.md:28`. Channel noise depresses numerator and denominator together, and the ratio can stay at 1. Holds (731548's verifier did the same arithmetic, `audits/AUDIT-WORKING-731548/verify/02-floor-accounting-verdict.md:70`).
- `[def-model-class-fitness]` Checked the well-definedness inheritance. `def-model-sufficiency.md:16,26` states that `#def-model-class-fitness` inherits the zero-denominator scope. Holds upstream; this segment itself is silent (policy/trajectory relativity is still unstated, as aux 08 says).
- `[def-model-class-fitness]` Checked "the agent cannot directly compute its class fitness" against its later uses (`spikes/.integrated/VERIFICATION-2026-07-16.md:100`; `audits/fix-adaptive-reserve-AUDIT.md:154`). It's consistently read as a modeler-side quantity with an agent-side proxy. Holds.
- `[def-model-class-fitness, result-structural-adaptation-necessity]` Checked the claim that the class-vs-noise discriminator exists in canon bodies, not only in gold: `result-structural-adaptation-necessity.md:17,46,60` carry it. Holds.

## History

- Origin: TF-10 (`.archive/old-tf-10-structural-adaptation.md:33–38`), where the definition appeared with the same elementwise sup *and* an "implicit environment dependence" note ($\mathcal F(\mathcal M; T, h)$). The note wasn't carried into the segment at the 2026-03-11 migration (`1f3caedc`). `git log -S` finds the phrase only in that migration commit.
- `b1f599d4` (2026-05-21): description upgrade to two paragraphs (instance-vs-ceiling, the bias/variance parallel, operational signature).
- `c931bccb` (2026-05-30): gold lift into the Working Notes.
- `a8a1a60a` (2026-07-03): B-2 companion (systematic-residual signature). This is the last body change.
- 731548's reflection on this segment (`audits/AUDIT-WORKING-731548/13-…`) hasn't been gold-lifted. The 731548 gold lift "not started" per `CHANGELOG.md:227`; the 2026-08-22 impl passes lifted only impl-segment gold.

## Why the aux looks the way it does

- Aux 08 had already relayed the segment's unrouted 731548 items (xxix, xxxi, xxxii), the inherited relativity, the LLM ambiguity and a log-loss identity, so I gave them one sentence and spent the aux on the coordinator's stated question (fitness vs the endowment's model class).
- I put the retention/readout split in FINDER-OBSERVED rather than as a claim. It's a two-line tower-property argument and I'm confident in it, but nobody else has checked it, and it bears on how the reboot types its endowment.
- The transience inference (law share of the shortfall decays) is marked as inference. I didn't work through Bernstein–von Mises conditions for the closed-loop, policy-dependent case, and a fixed-policy assumption is doing work there (your Doob segment has the same condition).
- I left out 849201's praise of the bias/variance line (it's praise, and 963715's correction supersedes it), 742613 F8 (already landed upstream), and the adaptive-reserve plan's details beyond the one-line template note.

## Worries about what the coordinator might miss

- `[def-model-class-fitness]` The three slots in the reboot's endowment, $(\pi^E, \mathcal M, \phi)$, may be one slot too many or too few for fitness. If $\mathcal M$ is a codomain, fitness is vacuous for continuous stores; if $\phi$ is fixed, there's no sup. Whatever he chooses, `#result-structural-adaptation-necessity`'s "parametric vs structural" line will be drawn by it.
- `[def-model-class-fitness, 04-eli-core]` The honest-activation spike is two days old and not yet integrated into canon. It's easy to miss because its integration plan lists this segment only as a Working-Notes hook, but R3/R4 undercut the body's detection sentence.

## Notes for other segments (slug-tagged)

- `[result-structural-adaptation-necessity]` Steps 1 and 5 (:39, :43) treat the arg-sup $M^\ast$ as a *point* that $M_t$ reaches, while $S$ is a property of the statistic $\phi(\mathcal C_t)$. Within a run the agent executes one $\phi$; convergence of $M_t$'s values is not movement toward the arg-sup over rules. The Kalman-$\hat Q$ example in aux 12 is a minimal case.
- `[result-mismatch-decomposition, internal-external-decomposition, deriv-mismatch-budget-attribution]` Term (i) splits exactly into readout ($\mathbb E\Vert\hat o - \mathbb E[o\mid M,a]\Vert^2$) plus retention ($\mathbb E\Vert\mathbb E[o\mid M,a] - \hat o^{\mathrm B}\Vert^2$), by $\sigma(M_{t-1},a_{t-1}) \subseteq \sigma(\mathcal C_{t-1},a_{t-1})$. In log-loss: retention $= I(\mathcal C_{t-1}; o_t \mid M_{t-1}, a_{t-1})$, readout $= \mathbb E\,D(p^M\Vert q)$. This might be the missing link that `deriv-mismatch-budget-attribution.md:125` calls open ("different objects"): Proposition 4's $D(p^{\mathrm B}\Vert q^\ast)$ contains the retention leg plus the readout-leg misspecification. It also gives the spike-02 four-term decomposition a fifth row if the agent's prior differs from the modeler's. Needs independent verification.
- `[der-interaction-channel-classification]` Uses $\mathcal F(\mathcal M_B)\cdot\mathcal I_{\max}(\mathcal M_B)$ as a per-event information threshold (:52, :66). $\mathcal F$ is an infinite-horizon ratio of predictive information, so multiplying it by a per-event capacity is a new reading that the definition doesn't license. Worth checking at that segment.
- `[deriv-persistence-cost]` :156 calls the $\mathcal F \lt 1-\varepsilon$ floor "misspecification cost". $\mathcal F$ is blind to misspecification of the agent's prior (it's computed under the true law). The intended object is probably Proposition 4's ceiling or the readout leg.
- `[norm-honest-activation, def-death-as-factor-loss, hyp-communication-gain]` The integration plan's item 7 frames this segment's correction as a hook fix. My reading is that R3's "prior-determined attribution, not structured residuals" is also a counterexample scope for the *body's* detection claim. The integrator may want to touch :14/:38 when landing, not only the Working Notes.
- `[form-agent-model, der-recursive-update]` With discrete observations, an affine $f_M$ on $[0,1]$ encodes the full history injectively, so "fixed-dimensional recursive store" does not by itself bound sufficiency. Any capacity claim needs a regularity or parametric restriction on $f_M$.
- `[def-model-class-fitness]` Kleijn & van der Vaart 2006 and Shalizi 2009 are in relata without documents; `relata fetch … --apply` would get them if someone lands a misspecification object.

## Process feedback

- The brief's "don't re-surface what an earlier aux gave him" worked well here: aux 08 had done a lot of this segment's rote finding, which freed this pass for the conceptual question. It does mean aux 12 only reads well alongside aux 08. I said so up front.
- The coordinator named his question ("how fitness relates to the model class in the endowment"). That was the most useful sentence in the handoff: it turned a gather pass into an answer-shaped one without narrowing what I looked at.
- Grepping `spikes/` for the slug (not just `audits/` and CHANGELOG) was what surfaced the 2026-09-23 spike. Later finders may want to include not-yet-integrated spikes from the last week in their sweep.
