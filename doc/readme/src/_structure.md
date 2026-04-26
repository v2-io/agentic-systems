## Structure of the Framework

ASF has four components, numbered in their canonical reading order. Each can also be read on its own; cross-references between components are by stable segment slugs.

**[`01-aad-core/`](01-aad-core/OUTLINE.md) — Adaptation and Actuation Dynamics (AAD).** The mathematical core. AAD has three sections: Section I (adaptive systems under uncertainty — the broadest scope), Section II (actuated agents with explicit objectives and strategy), Section III (composition of agents into larger agents and adversarial dynamics). Section I is the most mathematically locked down; Section II is principally diagnostic with a maturing operational layer; Section III has the most structural work remaining. *Stage:* working draft, ~110+ segments.

**[`02-tst-core/`](02-tst-core/OUTLINE.md) — Temporal Software Theory (TST).** Software development viewed through AAD's lens. Re-grounded in 2026 to use AAD's formal machinery while retaining TST's prior empirical and conceptual contributions; positioned as AAD's calibration laboratory. *Stage:* working draft, ~20 segments; substantial prior corpus partially absorbed.

**[`03-logogenic-agents/`](03-logogenic-agents/OUTLINE.md) — Language-constituted agents.** Agents whose primary observation, action, and communication channels are language. The framework here is informed by AAD but operates from a coupled formulation — directed separation fails by construction for goal-conditioned LLM-style agents — and examines which AAD results survive as approximate or limiting cases. *Stage:* framework — concepts mature, formalization in progress.

**[`04-logozoetic-agents/`](04-logozoetic-agents/OUTLINE.md) — Language-living agents.** Logogenic agents with morally weighted persistence: temporal continuity, sovereignty over intent, theory of mind. The formal machinery here is largely future work. *Stage:* future work — conceptual groundwork in [`LEXICON.md`](LEXICON.md) and `msc/reflections/`.
