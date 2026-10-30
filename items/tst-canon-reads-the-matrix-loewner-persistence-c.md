---
kind: item
owner: C.1
opened: 2026-10-30T23:23:16Z
opened-by: Claude Opus 5.5 (spike drain fork D)
concerns: [segment:impl-developer-agent, segment:scope-developer-agent, segment:impl-system-measures]
---

# TST canon reads the matrix-Loewner persistence condition as "the weakest channel is the bottleneck" (#impl-developer-agent :41, :43; #impl-system-measures :35), which mistakes observation channels for mismatch directions, and it sits beside #scope-developer-agent :177–181's additive form without reconciling them.

Checked at cbd2f345. #deriv-matrix-persistence-condition :31 builds the matrix tempo by *summing* channels, $\mathcal T = \sum_k \nu^{(k)} K^{(k)}$, and its binding object is the weakest *direction* of mismatch space (MP-2a, :67–71; its own :19, "bandwidth-per-direction is the binding quantity, not total bandwidth"). A channel with zero rate leaves a direction uncorrected only if no other channel's gain covers that direction. So "a developer with $\mathcal T_\text{probe} = 0$ fails persistence along the probe direction" (:43's "unmaintainability is per-channel") is true only under an unstated premise: that some mismatch directions (say, behavior on untested paths) are observable through the probe channels and through no others. That premise may well hold for software and would make a good statement; as written, canon puts a channel where a direction belongs. #impl-system-measures :35 makes the same move for availability ("the weakest-component availability is the bottleneck" via matrix-Loewner); series availability is a product law and needs no Loewner argument. #scope-developer-agent :181's example is also inconsistent with its own tables: "instant code reading" is credited to $\mathcal T_\text{explore}$, while code reading is listed as an observation channel.

The repair: state the observability premise (which state directions each channel class reaches), derive the bottleneck as the least-covered direction of $\sum_k \nu^{(k)} K^{(k)}$, and keep the additive form as what it is, the trace-level aggregate.

Sources carrying the same error, which the integrator should not land as written: `spikes/tst-ideas-cycle-2026-05-21/spike-developer-tempo-channels.md` §3.1 (writes $\mathcal T_\text{dev} = \mathrm{diag}(\mathcal T_\text{obs}, \mathcal T_\text{explore}, \mathcal T_\text{probe})$, treating channels as axes of the mismatch vector) and `spike-running-software-agent.md` §5.4 (does the same for sense/decide/actuate; "decide" and "actuate" are not observation channels at all, so they do not enter $\nu \cdot \eta^\ast$). `TST-IDEAS.md` §9 lists "matrix-Loewner weakest-channel bottleneck" as a three-spike convergence; it is one error shared, not independent support. The developer-tempo spike's other content is sound and is in item:the-2026-05-21-tst-spike-cycle-carries-four-deve (its §2 channel tables and probe-class typology, §4 chronicle-derivable estimators, and §5's refusal of the W1/W2 analogy for probe disposability).
