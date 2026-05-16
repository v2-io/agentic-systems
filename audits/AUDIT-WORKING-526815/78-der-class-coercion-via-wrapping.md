# 78 - der-class-coercion-via-wrapping

Source: `01-aat-core/src/der-class-coercion-via-wrapping.md`

## First-pass understanding

This segment proves a constructive special case: a coupled component can be wrapped by an external scaffold that maintains separate belief and goal/strategy stores. The belief-side query selector and belief update have no goal argument; the strategy-side path may use goals. Under component admissibility and no hidden goal leakage, the wrapper-level belief update is directed-separated even if the underlying component is not.

The core proof is straightforward conditional-independence reasoning. The design insight is also practical: strict wrapping buys structural separation by paying extra calls and interface discipline. The subtle part is the leakage story for LLM-like components, because conditioning on the exact query often blocks the pretraining-correlation path the text wants to measure.

## Diagram attempt

I drew the wrapper as two channels into the same component: a goal-blind belief query and a goal-conditioned strategy query. The visual focus is the possible hidden/proxy leakage path from `G_W` into the belief response, which is exactly what C3 or the KL bound must rule out.

## Findings and watches

- F127 candidate: C3 and the W1 leakage discussion conflate query-content correlation with leakage conditional on the query. If `A` is stateless and `q_M` is fully observed, then `P(A(q_M) | q_M, G_W) = P(A(q_M) | q_M)` holds by construction; pretraining correlations affect outputs as a function of `q_M`, not through an additional dependence on external `G_W` after conditioning on `q_M`. Leakage should be modeled as goal information carried by the query itself, hidden component state, conversation history, or an unobserved context variable.
- F128 candidate: the structural leakage bound `kappa_W1 <= I(A(q_M); G_W | q_M)` is questionable for the same reason. Under the exact conditioning used in the theorem, this conditional mutual information is zero for a stateless component. A more useful bound may involve `I(q_M; G_W)`, hidden-state-conditioned leakage, or `I(A(q_M); G_W)` under the wrapper's query distribution.
- F129 soft candidate: W2 is called a refinement within the Class 1 cell, but a single goal-conditioned call whose response is parsed into `M_W` and `G_W` does not satisfy structural directed separation. It is better labeled approximate/behavioral separation, not Class 1 except under an empirical leakage threshold convention.
- F130 soft candidate: the formal setup uses `X_G = X_O x X_Sigma` per `def-strategy-dimension`, but that segment is not declared as a dependency. If the type signature remains load-bearing, it should be declared or the setup should avoid relying on it.
- F131 watch: C2 excludes stateful/adapting components. That is necessary for the proof but important operationally: many deployed LLM agents have conversation state, tool memory, retrieval state, or adaptive context that can carry goal information outside `q_M`.
- Watch: The companion segment is supposed to carry AAT-composite validity and tempo cost. Do not credit those here.

## Local verdict

The wrapper proof works under a clean stateless-oracle model. The leakage section should be reframed around where goal information can actually enter: through the query, hidden state/context, or behavioral noncompliance, rather than through pretraining correlation after conditioning on the exact query.
