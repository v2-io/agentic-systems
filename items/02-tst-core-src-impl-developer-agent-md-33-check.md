---
kind: item
owner: C.1
opened: 2026-10-30T23:22:39Z
opened-by: Claude Opus 5.5 (spike drain fork D)
concerns: [segment:impl-developer-agent, segment:der-code-quality-as-observation-infrastructure]
from: item:spikes-proposed-code-quality-bistability-2d-dynamical-fo-0dc9
---

# 02-tst-core/src/impl-developer-agent.md:33, checked at cbd2f345, states the code-quality vicious/virtuous cycle as settled ("unstable with two attractors … this bifurcation is structural … the framework predicts the threshold's location"), while its home holds it hypothesis-grade and the one attempted derivation does not deliver two basins. Restate :33 at the home's tier and drop "predicts the threshold's location".

The home: #der-code-quality-as-observation-infrastructure :81, :91 ("not formally analyzed within AAT"), :127 ("hypothesis-grade pending dynamical-system verification"); #der-change-investment :63–65 ("structurally motivated but not formally derived"). :33 also asserts "below the persistence threshold, *no* investment calculus rescues the codebase", which nothing derives.

The attempted derivation, `spikes/tst-ideas-cycle-2026-05-21/spike-software-unmaintainability-bifurcation.md`, assumes (§7) that $\psi(W)$ is unbounded. Below its threshold $\rho^\ast$ the defect mass $W$ has no finite steady state (§4.4), so $\psi \to \infty$, the left side of its $(\ddagger)$ goes to $0$, and $(\ddagger)$ fails for every $\rho \in (0, \rho^\ast)$ at steady state. Its low-$\rho$ "stationarity" basin therefore exists only at $\rho = 0$ or under the $W$ ceiling that §6 uses and §9(D) says the segment should drop. What it derives is a disconnected set of parameter values, not bistability in state (there is no separatrix). The open derivation is item:spikes-proposed-code-quality-bistability-2d-dynamical-fo-0dc9, where the other sources are listed.
