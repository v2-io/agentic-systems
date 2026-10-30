*KR **C.2** / item C1 (expected exit time under Model S). Top intent, Joseph: "Complete 'in-place' refactor of ASF — meta, all artifacts, and theory itself."*

# Spike: exit time from the certified region under Model S (2026-10-30)

**Question.** Canon (Cor A.1S.1, `#deriv-sector-condition`; `#deriv-stochastic-non-exit`) establishes that under additive stochastic disturbance the mismatch leaves the sector-condition ball $\mathcal B_R$ with probability one for every correction strength. The owner review's Part I explorer asked *when*, and sketched $\sigma_w^2\log\mathbb{E}[\tau_R] \to \alpha R^2$ via Freidlin–Wentzell, with the FW hypotheses, the general-$F$ prefactor and a literature check owed. Brief: `msc/inside-out-2026-10/owner-review/integrator-items.md` C1.

**Verdict — strengthened past the claim.** Under A1 and A2' alone (no Lipschitz, no gradient structure, no small-noise limit), the exit time of any sector-satisfying corrector is bounded below by that of the isotropic Ornstein–Uhlenbeck process $F = \alpha\delta$ from the same radius — in mean (Theorem 1, Dynkin on the OU mean-exit function) and in distribution (Theorem 2, same-noise radial comparison). The benchmark is explicit in every dimension (Lemma 1) with Kramers asymptotic $\tfrac{\Gamma(n/2)}{2\alpha}\kappa^{-n/2}e^{\kappa}$, $\kappa = \alpha R^2/\sigma_w^2$ (Lemma 1′). Equality holds when the sector bound is radially tight — the same hypothesis that makes Lemma A.1N's Model D threshold an agent-level iff. Consequences: a finite-lifetime containment bound exponentially small in $\kappa$ (Corollary 3; canon's Prop A.1S(iv) is polynomial); the mean-square condition $\alpha \gt n\sigma_w^2/(2R^2)$ is $\kappa \gt n/2$, at which the benchmark leaves within about one correction time (Corollary 4); a tenure-indexed sufficient condition $\kappa - \tfrac n2\log\kappa \gtrsim \log\tfrac{2\alpha L}{\epsilon\Gamma(n/2)}$ (Corollary 5). The explorer's FW statement is recovered as a corollary; its owed items do not arise.

**Status.** Spike complete; awaiting independent verification (commissioned by the coordinator, not by me). No `spikes/INDEX.md` row has been added — that is outside this spike's write scope and belongs to the coordinator. Literature scan (`02-literature.md`) in progress — a Sonnet agent was cut off by a usage limit and resumed; until it lands, no novelty claim is made and two citations in the derivation are marked from memory. Nothing in canon has been edited.

## Files

| File | What |
|---|---|
| `debrief.md` | For Joseph: the problem, what was found, what it does not say, corrections made along the way — in pre-spike vocabulary |
| `01-neighborhood-map.md` | What canon already held around the question, every Working Note the result touches, scope decisions — written before deriving |
| `02-literature.md` | Web literature scan (pending) |
| `03-derivation.md` | The mathematics, every statement tiered; §8 scope lines; §9 adversarial instances with predictions written before the runs |
| `04-numerics.md` | What the checks corroborate, two predictions they corrected, one integrator artifact diagnosed, what they cannot show |
| `proposed-integration-plan.md` | For the verifier and integrator: checks ordered by damage-if-wrong, landing loci, labels, do-not-inherit list, adjacent suggestions |
| `checks.py` / `checks-output-partial.txt` | Lemma 1 vs explorer and MC; asymptotic; Corollary 4 table; adversarial set 4a–4c (run stalled at 4d by my design error, killed) |
| `checks-cont.py` / `checks-cont-output.txt` | Adversarial 4d–4e with a milder dip, the $\kappa=4$ set, lifetime bound, survival domination, $\Phi(r)$ monotonicity |
| `checks2.py` / `checks2-output.txt` | Discrete-monitoring bias vs $dt$; rotation-exact scheme for the radially tight instance |

## Scope, in one breath

Isotropic additive noise, continuous time, A2' on the closed ball. Not covered: anisotropic noise, discrete time (DA2'), state-dependent noise, heavy tails (the regime where exponential tenure genuinely fails), and the $R$-versus-breakdown-radius gap of `#sketch-structural-adaptation-genericity`, which this result times but does not close.
