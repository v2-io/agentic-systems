---
kind: item
owner: C.1
opened: 2026-10-30T23:23:49Z
opened-by: Claude Opus 5.5 (spike drain fork A)
concerns: [segment:internal-external-decomposition, segment:deriv-mismatch-budget-attribution]
---

# #internal-external-decomposition:59 states the constitutive no-go (no agent-independent rho_external with rho = rho_external * f(M) * g(pi)) as exact, but the argument given does not prove it and the universal claim has exceptions. 'A contribution that subtracts to zero cannot be represented by attenuating a fixed scalar' fails: a model factor f(M) can shrink too. The real obstruction is non-separability: a positive rho(M, pi) factors as f(M) g(pi) iff log rho is additively separable, i.e. rho(M,pi) rho(M',pi') = rho(M,pi') rho(M',pi) for all pairs. Exceptions where the product exists exactly: a policy-invariant budget (canon's own #deriv-mismatch-budget-attribution Cor 1b, with g = 1), and the rare-event Poisson-thinning regime with independent emission, model and policy gates and no channel floor (spikes/spike-rho-additive-variance-strengthening-2026-04-24.md §3.1, exact by Kingman's thinning). Strengthen rather than soften: state the separability criterion as the exact no-go, and show generic failure on canon's own worked anchor in #deriv-mismatch-budget-attribution (misspecified drift with a regulating policy: rho^2 = F + k(M) m(pi) with floor F = C + U > 0, and d^2 log(F + bc)/db dc = F/(F+bc)^2 != 0). Name the exceptions as the scope boundary. Not checked by a second mind.

Drain of spikes/: the rho-additive-variance spike's multiplicative-cascade regime is a counterexample to the no-go as stated; found while dispositioning it
