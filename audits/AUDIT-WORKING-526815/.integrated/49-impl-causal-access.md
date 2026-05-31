# 49 - impl-causal-access

Source: `01-aat-core/src/impl-causal-access.md`

## First-pass understanding

This chapter-end segment gathers implications of the causal-access chapter: the loop as Level-2 substrate, the cost-benefit bridge into strategy, multi-layer identifiability-floor escapes, and a proposed "sandbox hard ceiling" for pre-deployment evaluation. Much of it is synthesis and forward linkage rather than new formal machinery.

The central repeated idea remains data character versus identification quality. The loop can produce intervention-character experience, but valid estimates require positivity, sequential ignorability or adjustment, known mechanisms, stationarity, and adequate observability. The segment is strongest when it preserves that distinction; it is weakest where it converts the distinction into categorical claims about sandbox versus deployment.

## Diagram attempt

I focused the diagram on the sandbox-ceiling claim because it is the sharpest new implication. The alternative picture is two causal systems: sandbox and deployment. Both can contain interventions. The missing piece is a transport bridge, invariance claim, or deployment monitoring, not a Pearl-level difference caused by forkability.

## Findings and watches

- Candidate finding: the sandbox hard-ceiling argument misclassifies sandbox interventions as Level 1 because sandbox trajectories are forkable. In Pearl-style causal inference, repeatable/forkable experiments can be exactly the source of Level-2 interventional data for the system being experimented on. The real limitation is transportability/external validity from sandbox SCM to deployment SCM, not that sandbox data is merely associational.
- Candidate finding: the segment says Pearl's `do` operator requires a singular non-forkable trajectory and that stripping the trajectory commitment collapses interventional content. Pearl interventions are normally defined over causal models, populations, or repeatable experimental units; non-forkability is not a prerequisite for `do`. AAT may need singular trajectory for identity claims, but not for the basic semantics of intervention.
- Candidate finding carried forward: the chapter repeatedly says deployment produces Level-2 data "for free." It produces action-generated data for the deployed system, but identified Level-2 estimates still need the formal assumptions named elsewhere. The wrap-up should keep the weaker phrasing even in summary.
- Watch: the NeurIPS C1/C2/C3 formalization is doing real work in this discussion, but it is still outside the currently read AAT segment set. Final audit should separate AAT-local claims from paper-backintegration claims.
- Watch: the active-inference/control-as-inference contrast is broad and probably needs citation-level care if it becomes a finding. I am treating it as positioning language for now, not as established by this segment.

## Local verdict

The synthesis is useful, but the sandbox-ceiling section needs substantial reframing. A defensible version is: sandbox interventions identify sandbox causal behavior; deployment claims require transport assumptions or deployment-time monitoring because the deployment causal system may differ. Forkability is not what makes data Level 1.
