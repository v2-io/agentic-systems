---
kind: item
owner: G.2
opened: 2026-10-30T23:24:35Z
opened-by: Claude Opus 5.5 (spike drain fork D)
concerns: [segment:result-persistence-condition, segment:scope-continuous-operation, segment:def-satisfaction-gap]
---

# The running software service as an adaptive-actuated agent (four candidate TST segments) and admission control as actuated disturbance (two candidate Part I segments) are in no segment. The runtime scope cut (adaptive-dispatch control plane in scope, fixed-strategy data plane only under Part I) is sound and landable now; the actuated-disturbance sign condition rests on a reading of $\rho$ that AAT does not use, and must be re-derived before it lands.

Checked at cbd2f345: none of `#scope-running-software-agent`, `#def-runtime-observation-channels`, `#der-runtime-persistence-condition`, `#der-runtime-tempo-decomposition`, `#disc-rho-actuation`, `#deriv-actuated-disturbance-rate` exists, and no OUTLINE row names them. Nearest canon: #scope-continuous-operation and #def-system-availability, which treat the operating *team* and availability, not the service as an agent.

Sources: `spikes/tst-ideas-cycle-2026-05-21/spike-running-software-agent.md`, `spike-actuated-rho-regulation.md`; mining `spikes/tst-mining-2026-05-21/01-release-it-mining.md` A1, A2, A6–A10, B3, B4, C2, `04-elixir-composite-mining.md` A6, A7, B5, B6; synthesis `TST-IDEAS.md` §1 A1, §2 C1, §9.

Landable at its honest tier: the substate mapping of an adaptive-dispatch service ($M_t$ = breaker states, caches, rate estimates; $O_t$ = the SLO bundle; $\Sigma_t$ = the runtime-mutable playbook) with the scope cut stated in the chapter's first segment (running-software §1.2, §6: a service whose dispatch is fixed at compile time has no $\Sigma_t$ revision and is a Part I system only; scope membership is per deployment, not per artifact); the runtime observation-channel catalog (§3) as a discussion-grade taxonomy; the decomposition of the service's disturbance into traffic, dependency, infrastructure, configuration and adversarial components, each matched to the actuation that can address it (§4.2, robust-qualitative).

Not landable as written:

- **Runtime tempo as sense + decide + actuate** (running-software §5). Tempo is an observation-side quantity, $\sum_k \nu^{(k)} \eta^{(k)\ast}$; controller tick rate and actuation latency are not channels and do not enter it. They are real rate limits, but on a different object (loop delay), and the matrix-Loewner reading there is the error recorded in item:tst-canon-reads-the-matrix-loewner-persistence-c.
- **The actuated-disturbance sign condition** (actuated-rho §4.2: admission on channel $k$ helps iff $\rho^{(k)}_\text{offered} / (\nu^{(k)}_\text{arriving} \lVert\delta_\text{critical}\rVert) \gt \eta^{(k)\ast}$). It takes $\rho_\text{effective} = m \cdot \rho_\text{offered}$, i.e. each refused event removes disturbance as well as observation. The spike's own §4.1(b) says refusing an observation does not slow the world's drift. The premise holds only if $\rho$ means *task load* (each request is work the agent is accountable for), which is not AAT's $\rho$, the rate at which the environment moves away from the model. Load-shedding shrinks what the agent is accountable for; that is closer to an objective or scope change than to a change in $\rho$. Two smaller points: the margin is linear in $m$, so the per-channel optimum is always $m \in \{0, 1\}$, which the spike does not remark; and §5.2's "$m^2$ under Model S" is likely wrong, since thinning an event stream scales its variance rate by $m$, not $m^2$.
- **The cost lands in the satisfaction gap, not control regret** (actuated-rho §2) is definitional once admission actions are in the policy class, and is a fair discussion-grade observation for #def-satisfaction-gap's diagnostic table; the "no new diagnostic is needed" conclusion survives the correction above.
- **Restart intensity as wrapper persistence** (running-software §4.6) is the claim in item:otp-supervision-as-a-worked-instance-of-der-clas.

Joseph's question that launched the cycle, "what is $\rho$ for a microservice?", is answered here only by the definitional mapping; the honest answer for the segment is the five-component decomposition above, not a derived inequality.
