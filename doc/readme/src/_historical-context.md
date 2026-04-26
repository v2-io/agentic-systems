## Historical Context & Lineage

ASF descends from prior research threads:

- **Temporal Feedback Theory (TFT)** — the adaptive-systems foundation. TFT formalized mismatch signals, gain dynamics, adaptive tempo, and the persistence condition for systems coupled to a non-stationary environment. ASF subsumes TFT entirely; what was TFT now lives as Section I of AAD (Adaptation and Actuation Dynamics) and supporting appendices. See [`MIGRATION-MAP.md`](MIGRATION-MAP.md) for the absorption tracking and [`LOG.md`](LOG.md) for the cycle archaeology.
- **Temporal Software Theory (TST)** — software development as an agentic domain. Originally an independent body of work with its own corpus, TST was briefly absorbed as a section of the merged framework before being restored to its own component (`02-tst-core/`) on the grounds that it stands on its own merits as a domain instantiation. It is grounded by AAD but developed independently.
- **The PROPRIUM ontology** (`~/src/firmatum/`) — the architecture-of-identity work that informs `03-logogenic-agents/` and `04-logozoetic-agents/`.

ASF integrates established external mathematical tools — Lyapunov stability, Kalman filtering, the information bottleneck (Tishby et al.), Pearl's causal hierarchy, monotone-operator theory (Rockafellar; Bauschke-Combettes), Lohmiller-Slotine contraction analysis, Hafez's $H_b$ and $\Delta H$, Miller's coevolving automata. Adopted concepts retain their original names and citations and become first-class theory components rather than being repackaged. The integration itself is the contribution.

A naming note: the mathematical core was previously called Agentic Cycle Theory (ACT) and was renamed to AAD on 2026-04-16 to resolve a collision with "AI Consciousness Test" (Schneider & Turner) in AI welfare literature. See `msc/name-transition-aad.md` for the rationale.
