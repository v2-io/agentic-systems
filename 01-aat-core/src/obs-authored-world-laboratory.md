---
slug: obs-authored-world-laboratory
type: observation
status: discussion-grade
depends:
  - obs-software-epistemic-properties
  - deriv-mechanism-counterfactual-separation
  - result-persistence-condition
stage: draft
---

# Observation: The Authored-World Laboratory — Identifiability by Construction

AAT has one calibration laboratory it *found* — software, whose epistemic privileges are catalogued in #obs-software-epistemic-properties — and one it is *building*: a deterministic authored world (working name **vivarium**) in which the environment's law-content, state, noise, and disturbance rate are not merely observable but authored, so that every quantity the framework's results quantify over ($\rho$, $U_o$, $\delta_t$, $\mathcal T$, per-dimension mismatch, $\lVert\delta_{\text{critical}}\rVert$) has ground truth at scale inside dynamics rich enough that toy-model simplifications are structurally unavailable. This segment is the canonical introduction of the authored-world laboratory, placed ahead of the framework's validation simulations because the standing intent is to re-run those simulations in it; later segments and simulation reports cite this segment rather than re-describing the system.

## Formal Expression

*[Empirical Claim (system properties, by construction; build-state caveat in Epistemic Status)]*

The authored world provides four structural properties, each the *built* counterpart of a *found* software property in #obs-software-epistemic-properties:

**V1. Ground truth for every framework quantity.** Law-content is an explicit versioned registry of law-articles (keyed, memoizable invocation units); state is canonical and content-addressed; the disturbance rate $\rho$ is dialable per region (weather volatility, water-regime schedules); $\delta_{\text{critical}}$ has literal in-world meaning. Where software's inspectability is limited by the agent-side comprehension bandwidth (P1 there), the authored world's is limited only by the author's choice of instrumentation: identifiability holds **by construction** rather than by fortunate configuration.

**V2. Authored coordinatization of the exogenous space.** All stochasticity is a stateless pure function of a world seed and a coordinate/identity key — fated noise: genuine chance to any inside agent, deterministic lookup to the author. The aleatoric boundary's frame-relativity is thereby operational rather than philosophical, and the system realizes the central object of #deriv-mechanism-counterfactual-separation — an explicit, held coordinatization of $U$ — which makes **latent-anchored mechanism counterfactuals executable**: swap a law-article version, keep seed and keys, rerun. The separation theorem's demonstration experiment (a keyed law versus its key-permuted twin: indistinguishable at every hierarchy level, divergent under same-seed law-swap, with measurable disagreement mass) is runnable here and, at present, nowhere else available to the framework.

**V3. Exact citation semantics.** A claim validated in the authored world cites a specific world artifact — seed, generator versions, phase memo, intervention script — and content-addressed storage makes the citation exact and replayable to bit-identity. This is the conjunction ($\alpha$) deterministic outcomes, ($\beta$) replay at commensurate cost, ($\gamma$) content-addressed immutable environment state, which #obs-software-epistemic-properties P2 identifies as jointly held, in current standard practice, by software alone — and names as a configurational uniqueness with exactly this falsifier: a simulator brought under content-addressed recording with commensurate replay cost. The authored world is that falsifier under deliberate construction; when its fidelity program completes, the "unique" in P2 becomes "one of two," by design.

**V4. A disturbance-rate schedule with a persistence reading.** The world is built in phases, each running to convergence with its converged output promoted into fixed law for everything faster above it. The phase ladder is therefore a $\rho$-schedule: successive phases deliver environments of decreasing effective disturbance until agents of achievable tempo satisfy the persistence condition $\mathcal T \gt \rho / \lVert\delta_{\text{critical}}\rVert$ ( #result-persistence-condition). An agent-bearing world is, in this reading, the terminal rung of a persistence ladder the authors descend deliberately.

## Epistemic Status

*Discussion-grade as a whole, with the property claims empirical-by-construction and honestly dated.* V1-V4 describe the system's design and its verified build state as of 2026-07-16: the world is mid-Phase-3 (geology and hydrology converged with absolute-tolerance conservation tests; climate next; **agents not yet embodied**), so V1-V3 are live properties of the running system while V4's agent-bearing terminus and everything downstream of the agent seam are design intent. Claims here about what the laboratory *will* offer AAT's agent-level results are forward-looking and marked so; claims about determinism, keyed noise, content-addressing, and conservation-honesty describe running code. The Level-4 executability claim (V2) inherits *exact* semantics from #deriv-mechanism-counterfactual-separation; that the system realizes the required coordinatization is a fact of its architecture. This segment deliberately does not depend on the world's agent layer existing: it introduces the laboratory, not results obtained in it.

## Discussion

**Found versus built, and why the framework wants both.** Software is the domain where the epistemic privileges happen to hold and a large practice already generates data inside them; the authored world is the domain where they hold because someone chose them, which buys three things software cannot: (a) *dialable* environment parameters — $\rho$ can be scheduled, not merely measured; (b) *author-side access to the exogenous coordinatization* — software's version control gives literal Level-3 access (P2 there), while fated noise gives literal Level-**4** access, one full rung more; (c) freedom from the confound that software environments are themselves made of agent behavior. Conversely the authored world lacks software's ecological validity — nothing in it ships to production — so results transfer with stated construction assumptions, exactly the transfer-assumption discipline TST names for cross-domain claims. The two laboratories are complements, not competitors: found breadth against built depth.

**The standing simulation intent.** The framework's Part I validation simulations ( #obs-section-i-validation-simulations) were built as standalone numerical models; the standing intent is to re-run them in-vivo in the authored world as its phases reach the relevant dynamics, converting each from a bespoke script into a cited, replayable world artifact per V3. This segment exists partly so that migration has a canonical anchor: simulation reports should cite the laboratory, not re-describe it.

**Near-term experiments the laboratory makes cheap.** Beyond the Level-4 demonstration (V2), two are flagged in adjacent segments: the GA-1 housing experiment (transition-law versus observation-law ignorance — the experimenter chooses whether to perturb $T$ or $h$, directly testing the verified asymmetry from the epistemic-target work), and the behavioral $\hat\kappa_{\text{processing}}$ estimator at scale (same event under different goal states across thousands of agent-events with controlled priors) once the agent seam lands.

**Ethics gate.** Everything agent-seam-ward is gated by the authored world's own ethics front door, which is deliberately more conservative than this framework's volume-04 gates and binds program-wide; the laboratory's agent-level offers are sequenced behind it, not around it.

## Working Notes

- **Provenance and living bridge.** Canonical intro landed 2026-07-16 from the vivarium handshake work (same-day: the mechanism-counterfactual mapping). The living cross-project bridge — current build state, the four-thread Level-4 handshake, near/far offers — is `doc/vivarium.md` (repo-internal working doc, not citable from canon bodies; this WN pointer is the sanctioned breadcrumb). Vivarium-side twin: `~/src/archema-io/vivarium/feedback-from-asf.md` §Level-4 handshake; its ethics front door is `~/src/archema-io/vivarium/ETHICS.md`.
- **Build-state re-verification.** The Epistemic Status's build-state sentence is dated 2026-07-16; re-verify against the vivarium tree before citing this segment's V-claims in any promoted result (mid-rebuild volatility is a known divergence zone per the program's incoherence ledger).
- **Chronica link (forward, cross-volume).** A world's interventional history is a chronica in the exact sense of `04-eli-core`'s `#def-chronica` (ordinal, causal, append-only), and the world's fork/save machinery is the operational subject of the proposed `#hyp-checkpoint-forking-failure-modes` — the two should co-develop; kept as a WN forward pointer rather than a depends edge to preserve volume reading order.
- **P2 uniqueness-claim maintenance.** When the fidelity program completes ($\gamma$ at full strength), #obs-software-epistemic-properties P2's "unique in current standard practice" needs its by-then-true revision; a matching WN pointer lives there.
