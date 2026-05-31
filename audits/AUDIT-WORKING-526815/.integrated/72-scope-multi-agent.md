# 72 - scope-multi-agent

Source: `01-aat-core/src/scope-multi-agent.md`

## First-pass understanding

This segment opens Part III by defining the broad multi-agent setting: several AAT agents interact through a shared environment, with observations and transitions coupled by the other agents' actions. It also introduces a useful routing/content distinction. The communication infrastructure can be goal-blind even though individual messages naturally reflect the sender's goals through policy.

The important local move is scope separation. All interacting agents live in multi-agent scope, but only some configurations qualify as composite agents. Cooperative teams, equilibrium-convergent strategic pairs, cyclic adversaries, and asymmetric attacker/target setups are intentionally sorted into different machinery buckets.

## Diagram attempt

I drew a two-layer picture: agents and shared environment at the bottom, routing infrastructure over the top. The visual point is that message content may be goal-colored while the routing layer can still be goal-blind or goal-dependent.

## Findings and watches

- F93 candidate: the formal timing lets `o_t^{(i)}` depend on other agents' simultaneous actions `a_t^{(\neg i)}`, while each `a_t^{(i)}` is also defined from `X_t^{(i)}`. Unless the segment specifies observe-then-act, act-then-observe, or simultaneous-game information sets, this creates a possible algebraic/information loop.
- F94 soft candidate: `goal-blind-routing` uses independence notation such as `c_t^{(j -> i)} perp G_t^c` for a protocol rule. If `c_t` is a deterministic infrastructure rule rather than a random variable, the condition should be stated as invariance of the selected topology/protocol with respect to the composite goal, or as conditional independence for a random routing-selection process.
- F95 candidate: the discussion says Section I/II agent-level machinery applies directly to every agent in every multi-agent configuration because each satisfies `scope-agency`. Section I and some agency-scope results do apply broadly, but the AAT outline says Part II's exact results apply to Class 1 separated agents. The sentence should distinguish general agent-level notions from directed-separation-dependent exact results.
- F96 soft candidate: the opening claim that independence is the special case requiring justification is directionally right for shared environments, but too strong if the agents occupy independent subsystems, weakly coupled modules, or intentionally isolated channels. The claim should be framed as a default modeling prior, not a universal burden.
- Watch: direct communication is described as a special case of action-observation coupling. That is coherent if messages are routed through the environment/boundary, but the formal decomposition should make clear whether the message channel is part of `Omega_t`, a separate boundary channel, or a shorthand observation term.

## Local verdict

The segment does useful scope work, especially the routing/content distinction. The formalism needs a crisp time-step convention before later results use inter-agent observation/action coupling for causal or stability claims.
