---
kind: item
owner: C.1
opened: 2026-10-31T03:50:33Z
opened-by: Claude Opus 5.5 (B.1 Part I records)
concerns: [segment:result-certificate-existence]
---

# Three defects in #result-certificate-existence. (1) 'Local nonlinear extension': '(C) holds on B_R(e*) iff the linearization is exponentially stable and the second-order remainder is dominated on the ball'. The only-if fails. F(e) = e + e^3 meets (C) with M = 1, kappa = 1 on every ball (eF = e^2 + e^4), while on |e| <= 2 the remainder bound needs c >= 2, so cR = 4 > kappa. Stability of the linearization is necessary; remainder domination is sufficient only. (Khalil Thm 4.7 is a sufficient condition.) (2) Epistemic Status, 'R0-loss scope': 'the equivalence S == 0 <=> full-state marginal stability at kappa = 0 follows from polarization plus Bendixson'. The Derivation's own counterexample J = [[1,-2],[2,-1]] (eigenvalues ±i sqrt 3, S = diag(1,-1)) has full-state marginal stability with S != 0, so the sentence holds only at M = I read as 'V = |e|^2/2 is conserved'. (3) 'Certificate' is defined by (C) with kappa > 0, and the ladder also calls M with sup kappa = 0 a certificate (R0-loss). The opening's 'a stability certificate exists for an agent exactly when the agent is exponentially stable' is false in the ladder's sense. Also: the Findings Brief equates 'the measuring-stick exists' with 'the agent can keep up', but exponential stability with kappa R < rho does not keep up; keeping up is the template's half. That sentence is A.2's surface, and item influx-intro-anchor-sentences-outrun-bodies covers INTRODUCTION headline 3's dropped 'at the linearized level'.

Found writing the B.1 Part I record; each counterexample is checked by hand in the record.
