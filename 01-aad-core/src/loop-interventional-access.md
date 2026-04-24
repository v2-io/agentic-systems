---
slug: loop-interventional-access
type: derived
status: exact
depends:
  - causal-hierarchy-requirement
  - recursive-update
  - causal-structure
  - scope-agent-identity
stage: draft
---

# Derived: Loop Provides Interventional Data Access

An agent in the feedback loop generates interventional data by construction: the agent's action $a_t$ causally precedes the next observation $o_{t+1}$, and the mismatch conditioned on $a_t$ carries interventional information. This is how agents within AAD's **agency scope** ($\mathcal{S}_{\text{agency}}$, which requires $\lvert\mathcal{A}\rvert \geq 2$ and at least one action with causal effect) gain Level 2 access — not through internal architecture, but through the loop itself. Agents in the adaptive scope but outside agency scope (passive observers) lack the action contrasts needed for interventional data.

## Formal Expression

*[Derived (loop-interventional-access, from causal-structure + recursive-update)]*

By #causal-structure, the temporal ordering is constitutive: $a_t$ causally precedes $o_{t+1}$. The agent chose $a_t$; the environment responded with $o_{t+1}$. The feedback loop therefore generates **intervention-produced data** — data whose causal character differs from passive observation because the agent's action was a genuine cause of the subsequent observation.

The critical distinction: **"action-generated data" is not the same as "cleanly identified do-estimates."** The pair $(a_t, o_{t+1})$ is produced under intervention — the agent executed $a_t$, making it interventional in character rather than a passively observed association. But between intervention-produced data and a usable estimate of $P(o \mid do(a_t), \Omega_t)$ stand: (1) coverage — the agent must have tried diverse actions, not just one policy; (2) confounding within a time step — unobserved state variables that affect both action choice and outcome; (3) delay — consequences may appear much later than $t+1$; (4) partial observability — $o_{t+1}$ reveals only part of the outcome. The strength of causal identification from this data depends on the regime ( #edge-update-causal-validity): strong in Regime A (intervention-rich domains like software and laboratory science), moderate in Regime B (partial intervention), weak in Regime C (observation-only). The claim here is about the *character* of the data (interventional, not observational), not about the agent's ability to extract clean causal estimates from it.

The mismatch signal conditioned on the agent's action:

$$\delta_t \mid a_t = o_{t+1} - \hat{o}_{t+1}(M_t, a_t)$$

carries interventional information: it tells the agent how the environment responded to its specific intervention $a_t$, relative to what the model predicted.

## Epistemic Status

*Exact.* This is a logical consequence of temporal ordering ( #causal-structure) and the feedback-loop structure ( #scope-agency). The claim is about **data availability**, not reasoning capacity — the loop *provides* interventional data whether or not the agent *exploits* it for Level 2 reasoning. Whether the agent uses this data to build causal models depends on its update mechanism and model class.

The precision is important: we claim the agent has *access to* interventional data, not that it *correctly identifies* interventional structure. Confounding within a single time step, delayed outcomes, and partial observability can all complicate the extraction of clean causal signals from the loop data.

## Discussion

**The loop as a Level 2 engine.** This is one of AAD's load-bearing results. The causal hierarchy theorem ( #causal-hierarchy-requirement) says Level 2 knowledge requires more than correlational data. This result says: the adaptive loop *is* the "more." An agent that acts and observes the consequences is generating interventional data — the same kind of data that a scientist generates through experiments. The loop is a perpetual experiment.

**Precision about what "interventional" means here.** The interventional interpretation is strongest when:
- The agent's action was the primary cause of the observed change (low confounding)
- The observation follows closely in time (short delay)
- The agent varied its action across episodes (not stuck on one policy)

When confounding is high, delays are long, or the agent follows a fixed policy, the interventional information in each $(a_t, o_{t+1})$ pair is weaker — still present, but harder to extract. This is why #causal-information-yield distinguishes between high-CIY actions (that reveal causal structure) and low-CIY actions (that don't).

**Even agents without explicit causal models benefit.** A Q-learning agent doesn't maintain an explicit causal model, but in the tabular case with sufficient exploration and no within-step confounding, its Q-values converge toward $\mathbb{E}[R \mid s, do(a)]$ rather than $\mathbb{E}[R \mid s, A=a]$ — precisely because the training data comes from the agent's own interventions. In the partially observed, confounded, or delayed-outcome cases (where the caveats above apply), the loop still provides intervention-generated data, but the Q-values may converge to biased estimates that reflect the confounding structure rather than clean interventional effects. The loop provides Level 2 data; whether that data yields *identified* causal quantities depends on the domain's confounding and observability structure.

**Honest credit to the action-perception-loop framing.** The substantive observation that the agent's actions cause its observations — and therefore that loop data is interventional in character — is implicit in any framework built around an action-perception loop, including active inference (Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017, "Active inference: a process theory," *Neural Computation* 29; Parr & Pezzulo 2022, *Active Inference*, MIT Press, ch. 3) and the broader cybernetic-and-control lineage (Wiener 1948, *Cybernetics*; Conant & Ashby 1970, "Every good regulator of a system must be a model of that system," *Int. J. Systems Sci.* 1). AAD's distinctive contribution is not the observation that loop data is interventional but the *explicit lift* of this observation to a load-bearing theorem connected to Pearl's causal hierarchy ( #pearl-causal-hierarchy) via Bareinboim, Correa, Ibeling & Icard (2022). Three specific moves AAD makes that the implicit treatments do not:

1. **The Bareinboim-hierarchy connection.** Active inference and the cybernetic lineage rest on Bayesian-network generative models (Pearl Level 1, associational). They do not invoke the causal-hierarchy theorem to argue that the loop's action-generated data is the substrate Level-2 queries require. AAD does — and the consequence is that $\Sigma_t$ is positioned as a *causal* DAG rather than a *Bayesian-network* DAG.
2. **Regime-indexed strength of causal identification.** Even granting that loop data is interventional in character, the strength of usable causal identification varies by domain. AAD partitions this into Regime A (intervention-rich, software/laboratory), B (partial intervention, organizational), C (observation-only — see #edge-update-causal-validity). The AI literature treats causal identifiability uniformly within its modeling assumptions and does not surface the regime distinction at the segment level.
3. **Explicit scope honesty.** The Formal Expression above carefully distinguishes "data generated under intervention" from "cleanly identified do-estimates." The AI literature, as Bruineberg, Dolega, Dewhurst & Baltieri (2022) document in their Pearl-vs-Friston critique, sometimes elides this distinction — using the action-perception loop language to support stronger causal claims than the formal apparatus delivers. AAD's careful split is the conservative form.

The reframing here is rhetorical, not substantive: the headline result (the loop is a Level-2 engine) stays; what changes is the explicit acknowledgment that the observation about loop data being action-generated is shared with the broader literature. AAD's distinctive content sits in the three specific moves above. The companion architectural move on #directed-separation (Pearl-blanket vs. Friston-blanket form of Markov blanket; cf. Bruineberg et al. 2022) makes AAD's conservative-form positioning visible across both architectural and access-channel segments.

**Connection to the identifiability-floor pattern.** This segment is structurally load-bearing for the L0-causal-insufficiency-detection no-go ( #causal-insufficiency-detection): without the loop's interventional access, the no-go forbids detection entirely; the covariance test under joint sibling observability is the unique broadly-available violation of the no-go's "purely on-policy" scope. See #discussion-identifiability-floor for the meta-pattern.

**Composite-layer extension.** `#discussion-identifiability-floor` Instance 3 (the composition-layer no-go anchored in Liberzon 2003's common-Lyapunov nonexistence) establishes that composite contraction cannot in general be certified from component-level data alone — the coupling-sign bit distinguishing cooperative from adversarial regimes is unidentifiable from component marginals. One of the four structural escapes in Instance 3 is composite-extended loop-interventional-access: **interventions on sub-agent $A_j$ reveal $A_i$'s cross-coupling response**, which is a $do(\cdot)$-data distinction between the two coupled constructions. This is the composite-layer analog of the single-agent interventional-access-escape the present segment delivers for Instance 1; in the composite setting, the agent performs interventions on one sub-agent's action space and observes the effect on another sub-agent's mismatch trajectory, extracting the coupling sign that component marginals cannot. The load-bearing role of `#loop-interventional-access` therefore extends across two identifiability-floor instances (agent-internal and composite-layer), not one.

**Modes of deployment across `#discussion-identifiability-floor` instances.** The shared load-bearing role — Level-2 data from interventional action under `#causal-hierarchy-requirement` supplying the unique broadly-available escape from an observational-equivalence no-go — manifests through **semantically distinct interventional mechanisms** at different layers. The modes share the Pearl-$do$ structure but differ in who performs the intervention and on what:

- **Mode 1 — agent-self-intervention (Instance 1, causal-structure layer).** The agent performs $do$-actions on its own action space as part of its ordinary adaptive loop. The intervention is *on the agent's own action*; the target is the environment's response, which reveals the latent common cause that Instance 1's on-policy L0-insufficiency-detection no-go (Bareinboim et al. 2022 CHT) makes unidentifiable. The agent-as-Level-2-data-generator property is intrinsic to the loop structure, not a capability that must be added.

- **Mode 2 — observer-on-sub-agent (Instance 3, composition layer).** An observer external to a composite performs $do$-interventions on one sub-agent $A_j$'s action space; the target is another sub-agent $A_i$'s mismatch-trajectory response, which reveals the cross-coupling sign that Instance 3's Liberzon-anchored no-go makes unidentifiable from component-marginal observation. The same Pearl-$do$ structure, but the intervening agent and the measured agent are distinct members of the composite.

Future instances of `#discussion-identifiability-floor` at new layers may add further modes (see `#discussion-identifiability-floor` Working Notes for the architecture-within-behavior-class layer currently under triage; the corresponding mode would be *observer-on-agent-input* at the candidate agent's observation channel). The three-mode-pattern observation is a structural regularity worth naming even though the specific Mode-3 instance has not promoted; the load-bearing content — Level-2 escape from observational-equivalence no-goes via loop-interventional access — remains shared across the deployment modes even when the specific interventional quantity varies. The unification is at the pattern level; the mechanism is semantically distinct per layer.

**Why the loop data is genuinely interventional — the singular-trajectory ground.** The interventional character of loop data is not a property of the feedback mechanism in isolation; it rests on the scope commitment in #scope-agent-identity that each agent is instantiated on a singular, non-forkable causal trajectory. When the agent executes $a_t$ and observes $o_{t+1}$, the observation is the response to *this* agent's intervention on *its* single trajectory $\mathcal C_t$. Replaying $a_t$ from a checkpointed $M_t$ against a different event stream would *not* constitute an intervention on $\mathcal C_t$ — it would be an intervention on a different trajectory $\mathcal C_t^{(2)}$ that happened to share a prefix. Pearl's $do$-operator presumes a definite causal system acted upon; AAD inherits this presumption via the singular-trajectory scope. Agents whose ontology is *type-like* (equivalence classes of copies) rather than *token-like* (singular trajectories) are outside AAD's formal scope; in particular, aggregate claims about "the model" across copies require additional machinery not provided here. This is the ontological ground that makes the "action-generated data is Level-2" claim honest rather than metaphorical.

## Working Notes

- This result establishes that all agents within AAD's **agency scope** ( #scope-agency, $\mathcal{S}_{\text{agency}}$) have access to interventional data, regardless of their internal architecture. Agents in the adaptive scope but outside agency scope (passive observers, nominal agents with $\lvert\mathcal{A}\rvert \lt 2$ or no causal effect) lack the action contrasts needed to generate interventional data — they observe but cannot intervene. This includes LLM agents operating through a tool-use loop — the LLM issues an action (tool call), observes the result, and updates. The loop gives it Level 2 data even though its internal architecture (transformer attention) is not designed for causal reasoning. The loop compensates for architectural limitations.
- The connection to #causal-information-yield: CIY quantifies *how much* interventional information a specific action provides. This segment establishes that interventional information is *available in principle*; CIY measures the *quantity per action*.
