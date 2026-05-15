# 01 - def-agent-environment

Segment: `01-aat-core/src/def-agent-environment.md` (`#def-agent-environment`)

Dependencies: none. This is the first canonical segment and has an empty `depends:` list, so the dependency-order check passes.

## Segment Read

This segment defines the scope-opening object: an agent is not just something that acts, but something separated from an environment by a lossy observation boundary while maintaining internal state and producing actions that affect that environment. The important move is not the ordinary agent/environment split by itself; it is the claim that information loss is constitutive rather than incidental. Perfect access to $\Omega_t$ would make model, mismatch, gain, and adaptation vacuous.

The title is "Agent-Environment Coupling," while the slug and outline target say `agent-environment`. That title does a little extra work: it emphasizes that the boundary is not merely a partition but an interaction topology. I do not yet know whether the naming card has a target for this exact term; if it does, I expect a possible tension between `boundary` and `coupling`. The segment itself makes the loss boundary the load-bearing content, while the title foregrounds coupling.

## Predictions Vs Evidence

My prediction that Section I begins with clean formal primitives is confirmed. I expected the first definitions to avoid heavy derivation and establish the modeling surface; this does exactly that. The nuance I had not fully predicted is that direct state access is explicitly outside AAD scope, not simply a degenerate special case.

## Cross-Segment Consistency

No earlier source segments have been read, so there is no cross-segment contradiction available yet. I should watch later segments for whether they consistently treat perfect observation as outside scope or whether some downstream examples accidentally use full-state access without naming it as an approximation or external designer access.

## Naming Notes

The likely naming issue is whether future prose should call this the agent-environment "boundary" or "coupling." The definition has both: the agent is coupled through observation/action channels, but the reason AAD exists is the information-loss boundary. If a target asks for the whole segment's subject-noun, `agent-environment boundary` may be more scope-honest than `agent-environment coupling`; if a target asks for the interaction topology, `coupling` is fine.

I do not yet have a vote unless the tracker has a direct target, because this is too foundational to rename from a single title impression without seeing how the next primitive segments compose.

## What This Enables

This segment enables every later quantity to be typed: $\Omega$, $o_t$, $a_t$, internal state, and the fact that there is a channel-mediated relationship rather than omniscience. It also defines a reader expectation: AAD is not a universal theory of all systems; it starts where uncertainty is structurally present.

## Watchlist

- Downstream examples that quietly assume full observability.
- Names that collapse boundary, coupling, channel, and scope into one undifferentiated phrase.
- Any later use of `agentic` that forgets this broader agent/environment basis.

## Wandering Thoughts

The segment feels deliberately modest, which is right for a first primitive. It does not try to win the reader with a novel term. It installs the condition that makes the later theory possible: contact with reality is mediated, and mediation introduces loss.

For naming, that modesty matters. A catchy name here would probably be worse unless it points exactly at the loss boundary. Foundational primitives should become transparent after one reading. If the community is going to argue about AAD, they need not argue about what "environment" means every time; they need to remember that the environment is the inaccessible outside, not just "the rest of the system."

There is a nice asymmetry already: actions affect the environment, observations do not expose it. That is enough to make adaptation directional. The agent can perturb the world but cannot directly read it. The whole later Pearl Level 2 story is latent here before causal vocabulary appears.

I am also noticing a possible layer distinction for naming votes: slug subject-nouns in early definitions can be plain because their role prefix already carries the conceptual type. The title can be pedagogical. The prose can carry the memorable phrase. Those layers should not be forced into one winner unless the card target specifically demands it.
