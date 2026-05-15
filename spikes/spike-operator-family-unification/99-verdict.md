# 99 — Verdict: the certificate cone, the plural no-go, and what to land

## Which completion state was reached

**Completion-state 2 (succeed-at-claim, strong form) at the object level, plus a sharp *plural* no-go at the failure level.** Not state 1 — the seductive single "integrability triad" was tested and **broken** (03-L4). Not state 3 — there *is* a genuine, verified unification. The result is more useful than the triad would have been because it tells future agents exactly which unification is real and which three obstructions are irreducible, with named theorems for each.

## The unifying truth (verified)

AAD's cross-sectional structure is the geometry of **one object**: the equilibrium **certificate operator** $\mathcal M$ on the PSD cone $\mathbb S^n$ (the converse-Lyapunov metric; $=$ Fisher in the statistical sub-case, $(P^-)^{-1}$ Kalman, $\nabla^2 L$ gradient, plant-Lyapunov-metric in the Hurwitz-non-symmetric case).

- **operator-sector** $=\ \mathcal M\succ0$ on the scope ball $=$ the **cone interior**. The O-BP10 keystone ("an adaptive system is an operator whose contraction rate exceeds its disturbance rate") is **verified as an exact equivalence, not an analogy** — Prop L1-lin: one-point operator-sector in *some* inner product $\iff$ linearized equilibrium exponentially stable, by the standard Lyapunov theorem. This is the prior co-owner's stated gate ("DO NOT elevate unless O-BP10 surfaces at segment level") — **now satisfiable**: L1 is the surfacing.
- **M2 separability** $=$ the region where $\mathcal M\succ0$ (certificate-exists scope).
- **M3 additive-coordinate-forcing** $=$ *which* $\mathcal M$: Čencov forces $\mathcal M=$ Fisher uniquely in statistical scope, matched (converse-Lyapunov existence) elsewhere — this is jacobian-b1 §6/§7's verdict, now placed as the *forced-identity face* of the cone.
- **M1 identifiability-floor** $=\ \mathcal M\in\partial\mathbb S^n_{\succeq0}$ (rank-collapse): the **cone boundary**. All four M1 instances verified as certificate-rank-collapse (L3): Cramér–Rao rank-1, Bareinboim CHT, Liberzon common-Lyapunov-nonexistence, Čencov-bridge.
- **composition** $=$ whether a *common* $\mathcal M$ survives projection: the certificate-as-metric survives (Schur complement of PD is PD) but the dynamic guarantee degrades by the Mori–Zwanzig memory commutator; $\varepsilon^\ast=\lVert\mathcal C\rVert$, zero iff $\operatorname{range}P$ is $J$-invariant.

The C1 predecessor's "four instances + Λ doesn't fit" was the shadow of this: the four instances are points on one cone under different certificates; Λ "didn't fit" only because it was framed as a between-spaces surjection instead of the idempotent $P$ whose Schur/memory defect is $\varepsilon^\ast$.

## The sharp no-go (the load-bearing core — plural, not singular)

The three ways the certificate fails are **irreducibly distinct named theorems**, each invariant under the others' degrees of freedom (that mutual invariance is the proof of irreducibility):

| Failure | Named obstruction | Invariant / why no other freedom escapes it |
|---|---|---|
| **M3 / forcing** | Helmholtz–Hodge | $DF$ non-symmetric ⟹ no potential ⟹ metric matched not forced. Symmetry of $DF$; projection & rank-augmentation don't fix it. |
| **M1 / existence** | **Sylvester's law of inertia** | Congruence preserves the kernel; the *entire* metric-freedom is a congruence orbit; orbits don't cross $\partial\mathbb S^n_{\succeq0}$. Only rank-augmentation (new information) exits — not reweighting. |
| **composition** | Mori–Zwanzig / Schur | Non-invertible projection; defect is the memory commutator, $=0$ iff resolved subspace is $J$-invariant. Metric change & rank-augmentation don't fix a memory kernel. |

The single most novel recognition: **Sylvester's law of inertia is the named mechanism for the identifiability-floor's irreducibility.** `#disc-identifiability-floor` currently establishes "no reparameterization escapes the floor" per-instance by direct computation (spike-finding-13, spike-rho-factorization). Recognizing that as one theorem — congruence preserves inertia, and metric-freedom *is* the congruence orbit — converts a list of computations into a structural law and explains, in one sentence, why M1 is irreducible to operator-sector: **operator-sector is the cone interior, M1 is its boundary, and the boundary is invariant under the only freedom operator-sector has.** That sharpens the C1 predecessor's honest-but-soft "identifiability-floor is orthogonal to operator-sector" into "interior vs. boundary of one cone, held apart by an inertia invariant."

## Answer to Joseph's original question

*Is an operator-family meta-segment the strongest thing for the theory?*

Re-answered with verified content rather than judgment-from-shape:

- **Not as SP-22 (β) frames it** — "bundle nine Tier-2 spikes under `#operator-family-template`, a fourth meta-pattern alongside M1/M2/M3." That framing is now *provably* mis-stated: operator-sector is **not a peer** of M1/M2/M3. It is the **interior of the cone** whose boundary is M1, scope-of-existence is M2, forced-identity is M3. A "fourth pattern alongside" mis-describes the geometry.
- **The genuinely strong move is the spine**: a single meta/synthesis segment that names the certificate cone and exhibits M1/M2/M3/composition as its boundary / scope / forced-identity / projection-defect, with the three irreducibility theorems (Sylvester / Helmholtz / Mori–Zwanzig) as load-bearing Findings. That is not a fourth meta-pattern — it is **the segment the other three are facets of**. This is the same structural move M3 already models at smaller scale ("layer-specific manifestations of a single geometric object"), raised to the framework.
- **Honest scope on the spine's strength:** the per-instance identifications are each *exact* (proved/cited); the "all of AAD's cross-section is this cone" synthesis is *robust-qualitative* (as strong as the instances jointly). L1 is linearized/local — the level AAD's persistence results already operate at, so not a weakening relative to the rest of the theory, but it must be stated. The one-point/incremental/forced **rung ladder (R0/R1/R2, 01-L1)** must be carried explicitly.

## Landing recommendation (honest to the verdict; the framework-identity call is Joseph's)

Three decoupled items:

1. **Safe-to-land now, high-value, no decision gate — the Sylvester recognition.** Add to `#disc-identifiability-floor` a Finding: the floor's irreducibility is Sylvester's law of inertia (congruence preserves inertia; metric-freedom is the congruence orbit; only rank-augmentation exits). This unifies the existing per-instance "no reparameterization escapes" computations under one named theorem and is independently citable. Does **not** require the spine decision. Recommend landing this regardless.
2. **The spine segment — gated on a framework-identity decision (Joseph's call, structurally the same as the M4 §5.1 decision).** A new synthesis segment (provisional slug `#disc-stability-certificate` or `#disc-certificate-cone`) stating the cone, the L1 equivalence, the four-facet reading, and the three irreducibility theorems. This is a deliberate reorganization of AAD's meta-structure — it asks M1/M2/M3 to be read as facets of one object. That is a framework-voice commitment, not a mechanical landing; it deserves the same sit-with-it treatment the modularity M4 question got. Recommend: **put it to Joseph as the decision, do not author unilaterally.** If taken, it is plausibly the strongest single segment in the theory; if not, items 1 and 3 still stand.
3. **SP-22 backlog is now *decoupled and clarified*.** The nine Tier-2 spikes are *not* the spine and should not wait on it. They land per the (γ)-hybrid (each to its INDEX target: ρ-decomposition appendix, dissipativity-template appendix, PID/update-operator α-list refreshes). The spine, if taken, is what they cross-reference for the organizing geometry — not what they bundle into. This removes the SP-22 (β) temptation entirely: there is no "unified operator-family meta-segment as a backlog bin," because the genuine unification is the certificate cone (a deliberate spine) and the backlog is just triage.

The prior co-owner recommendation ("land content, DO NOT elevate to fourth meta-pattern unless O-BP10 surfaces at segment level") is **honored and updated**: do not elevate to a *fourth peer pattern* (still right — it's not a peer); the O-BP10 gate is now *met* (L1); and the correct elevation, if Joseph wants it, is not a fourth pattern but the spine the other three are facets of.

## Status ledger (spike-level)

| Result | Tier | File |
|---|---|---|
| O-BP10 = exact equivalence (operator-sector in some metric ⟺ Hurwitz certificate), linearized/local | Exact (proved; Lyapunov theorem) | 01-L1 |
| Certificate is the unifying object, wider than potential, wider than Euclidean-OS | Exact per sub-case; robust-qualitative as synthesis | 01-L1 |
| R0/R1/R2 certificate-strength ladder (one-point / incremental / Čencov-forced) | Derived (robust-qualitative) | 01-L1 |
| M1 = certificate boundary; all four instances verified | Exact per instance (Sylvester proved; CHT/Liberzon/Čencov cited) | 02-L3 |
| **Sylvester's law = the named M1-irreducibility mechanism** | **Exact (proved) — the spike's central finding** | 02-L3 |
| Composition defect = MZ memory commutator; certificate-metric survives (Schur) but dynamic guarantee doesn't | Derived (robust-qualitative; recovers prior MZ spike) | 03-L4 |
| Integrability triad (Helmholtz ≅ Sylvester ≅ MZ) — **FALSE**; three irreducible obstructions | Exact (both pairwise identities disproved) | 03-L4 |
| Four meta-patterns = interior/scope/forced-identity/boundary + projection-defect of one cone | Robust-qualitative (synthesis; instances exact) | 02-L3, 03-L4 |

## What did NOT close (honest open edges)

- L1 is linearized/local. The *global* nonlinear equivalence (one-point OS ⟺ global exponential stability) is false in general (standard); the local form is what AAD uses and is sufficient, but a spine segment must state this scope, not paper it.
- The "exactly three" failure modes is a synthesis claim at robust-qualitative. A fourth obstruction could exist (e.g., non-autonomous / time-varying certificate drift); not searched here. The three found are each exact; their *exhaustiveness* is not proved.
- Sylvester is proved for the finite-dimensional / linearized certificate. The infinite-dimensional (function-space $M_t$ for logogenic agents) extension is not checked — flagged for any future logogenic application, not load-bearing for the AAD-core claim.
- The spine's promotion is a framework-identity decision, deliberately not taken in-spike.
