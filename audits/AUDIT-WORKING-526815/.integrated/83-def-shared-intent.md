# 83 - def-shared-intent

Source: `01-aat-core/src/def-shared-intent.md`

## First-pass understanding

This segment defines shared intent as an Information Bottleneck compression of the sender's purposeful state `G=(O,Sigma)` for coordination. The useful insight is that coordination does not require full plan transmission; it requires enough purpose and strategy information for partners to choose compatible actions.

The definition is plausible, but the formalism is still sketch-level. A proper IB setup needs an encoder distribution or channel, a relevance variable that matches the coordination task, and a distinction between sufficiency and tradeoff-optimal compression.

## Diagram attempt

I drew shared intent as a bottleneck between full purposeful state and coordinated behavior. The diagram highlights that the compression should be over `G`, not the full model `M`, and that the relevance variable may need to be a policy/trajectory-level object rather than a single coordinated action.

## Findings and watches

- F157 candidate: the IB optimization is written as an argmin over representations `G_s`, but standard IB optimizes over an encoder/channel `p(G_s | G_full)`. This repeats the deterministic-encoder ambiguity from `form-information-bottleneck`.
- F158 candidate: the relevance variable `a_t^coordinated` is too narrow for many coordination problems. Shared intent usually has to support a policy, trajectory distribution, conflict resolution, resource allocation, and replanning, not just one jointly optimal action.
- F159 candidate: the text says high `beta` approaches full model sharing, but the source variable is `G_t^full=(O_t,Sigma_t)`, not the epistemic model `M_t`. It should say full purposeful-state sharing unless `M_t` is added to the source.
- F160 candidate: calling shared intent the "minimal sufficient statistic" is stronger than the displayed IB tradeoff. IB gives a complexity/relevance optimum for a chosen `beta`; exact minimal sufficiency requires a separate sufficiency constraint or limiting regime.
- F161 soft candidate: the qualitative ordering "purpose before plans before models" is plausible, but not derived from the displayed IB objective without assumptions about entropy, change rate, shelf life, and relevance of each component.
- Watch: real communication noise, delay, trust, and interpretation are intentionally deferred; later `hyp-communication-gain` should carry that load.

## Local verdict

The shared-intent concept is useful as a communication-compression target. The formal definition should be rewritten as a stochastic IB channel with a richer coordination relevance variable and with sufficiency claims scoped to the appropriate limit.
