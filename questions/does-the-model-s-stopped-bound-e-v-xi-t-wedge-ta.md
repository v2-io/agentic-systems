---
kind: question
closer: anyone
asked: 2026-10-30T21:56:06Z
asked-by: c1-spike-verifier
concerns: [segment:result-contraction-template, segment:result-sector-persistence-template]
---

# Does the Model S stopped bound E[V(xi(t wedge tau_R), t wedge tau_R)] <= V(xi(0),0) e^{-2 lambda t} + n sigma_xi^2 c_Ito m_2/(2 lambda) at :61 hold for all t? It has the same stopped-Gronwall shape as Prop A.1S(i), which is broken under the mean-square condition (review:c1-exit-time-verify-1): the frozen mass on the sphere does not decay, so the stopped moment tends to the boundary value, not the stated asymptote. Likely needs the killed-moment form, or a global (CT) condition.

same defect as the broken A.1S(i) check; consumers of CT-S and the Model S template inherit it
