# Spike framing: Dynamic Across-Turnover Continuity-Persistence

> **Provenance.** This framing was authored by the practica-side agent who
> originated the spike request, from a holistic primary-source read during the
> practica `01-theory` source dive, and routed here verbatim (from
> `~/src/practica/msc/spike-1-continuity-persistence-framing.md`, 2026-05-19)
> as the canonical frame. (Math notation normalized for in-repo
> Obsidian/GitHub/pipeline rendering per CLAUDE.md §6 — `$…$`-delimited,
> sub/superscript ordering only; argument, structure, and wording verbatim.)
> It is a true peer hand-off: it frames the problem,
> the genuine ambiguity, the decision space, and the legitimate completion
> states, and deliberately does **not** prescribe the attack. The result
> against this frame is `RESULT.md`; where the result and this frame disagree,
> the result says so explicitly and this frame is what was wrong. Her framing
> pen; the attack and the math are Agentic Systems'.

---

*Proposed slug:* `spike-continuity-persistence` (place under `agentic-systems/spikes/` when routed).

**Status:** *Framing document — not an attempt to resolve.* Purpose: state the question precisely, isolate the *genuine* ambiguity (it is not a missing constant), name the three modeling commitments the spike must make-and-justify, fix the legitimate completion states, and collect the already-landed scaffold so the working pass does not re-derive it. Mirrors the house style of `spike-composition-scaling-N.md`.

**Date:** 2026-05-19.

**Provenance & peer note.** Framed from a holistic primary-source read of the continuity scaffold (`#obs-context-turnover`, `#deriv-identity-sufficiency-rate-bound`, `#disc-m-preservation`) done during the practica `01-theory` source dive. This is a hand-off frame written for the agent who already has working content on this spike: the attack is yours. Where this frame and your deeper work disagree, your work wins and this frame is what was wrong — say so and overturn it; that is the spike functioning as intended, not a deviation from it. Every claim below is tiered; §9 marks exactly what is first-hand-verified vs. inferred vs. open.

---

## 1. The question, stated precisely

A serial-sub-agent composite (the practica case: AI sessions under 100% context turnover + at least one human) loses and reconstructs its epistemic/identity state at every session boundary $k$. Per-boundary there is a *static* feasibility floor (`#deriv-identity-sufficiency-rate-bound`) and a *single-boundary* reconstruction-adequacy condition (`#obs-context-turnover`, `#disc-m-preservation`: $S(M_{k+1}^+)\ge S_{\min}$). **The open object is the *dynamic* statement across the sequence of boundaries** $k=1,2,\dots$: under what conditions does the composite's identity/sufficiency state remain bounded away from collapse as $k\to\infty$ — i.e., what is the inter-session analog of AAT's intra-session persistence condition $\alpha\gt\rho/R$, if one exists at all.

## 2. The genuine ambiguity (the structural core — read this before anything else)

It is **not** an under-stated lemma or an unfilled constant. It is that **AAT carries two persistence regimes and never connects them.**

- **Intra-session = a *rate* regime.** A state that *persists and is perturbed*; correction outpaces drift; $\alpha\gt\rho/R$; Lyapunov/sector on continuous or event-driven dynamics. *All* of AAT's persistence apparatus (`#result-persistence-condition`, `#result-sector-persistence-template`, sector machinery) is built here.
- **Inter-session = a *destroy-and-reconstruct* regime.** `#obs-context-turnover` states *in its own voice* that the state is "not perturbed, it is destroyed and reconstructed," governed by **reconstruction-adequacy, "not a rate condition."** `#disc-m-preservation`'s Epistemic Status states the link to Section I persistence is **"by analogy, not by derivation."**

So AAT has a rate-regime persistence theorem and a single-boundary adequacy condition, and **no bridge between an *iterated* adequacy condition and any persistence/stability guarantee.** The spike's whole substance is: *does AAT's sector/persistence apparatus transfer to a destroy-and-reconstruct walk — with what modification, or provably not?* AAT does not say, and the apparatus was not built for this regime.

## 3. The three modeling commitments the spike must make and justify

These are *upstream of* any derivation. They are not extractable from AAT — they are modeling choices, each resolving a specific place where AAT is literally under-specified, and **the choices jointly determine which completion state (§5) is reachable.** Naming them is this frame's central contribution; making and justifying them is the spike's first real act.

1. **The accumulation operator.** `#disc-m-preservation` writes $\epsilon^{(n)}_{\text{recon}}=\sum_k\Delta\epsilon_k$ (additive *in the formula*) while its own Working Notes ask "is it additive? multiplicative? does it have absorbing states?" Additive $\to$ a random walk; multiplicative $\to$ a different recurrence class; absorbing-state $\to$ a catastrophic-forgetting trap. The operator is undefined and the segment is internally inconsistent on it. *The choice must be argued (from the structure of $f_{\text{init}}$ / the externalization cycle), not assumed for convenience.*

2. **The state variable of the walk.** Three quantities are used interchangeably across the scaffold and are **not monotone transforms of each other**: $\epsilon_{\text{recon}}=d(M_k^-,M_{k+1}^+)$ (unbounded distance/KL on $\mathcal M$); $S(M)$ (predictive sufficiency, $[0,1]$, hard floor $S_{\min}$); $S_{\text{id}}$ (identity-MI ratio, $[0,1]$). Whether the walk reflects, is absorbed at $S_{\min}$, or drifts unboundedly depends entirely on which variable carries the dynamics. AAT supplies no canonical choice and no map between them. *Fixing the variable fixes the boundary behavior — choose it deliberately and state the map to the others.*

3. **The compensation model $\Delta I_k$.** The persistence inequality $\mathbb E[\Delta\epsilon_k]\le\mathbb E[\Delta I_k]$ has a right-hand side — identity-relevant information re-acquired per session — that AAT does **not characterize at all**. Until it is modeled (exogenous? bounded by the same rate-distortion channel? correlated with $\Delta\epsilon_k$?), that inequality is a *statement of the goal, not a theorem*. *This is also where practica enters concretely (§7): the durable-artifact layer is a specific engineered instance of the $\mathcal E_{\text{ext}}/f_{\text{init}}/\Delta I_k$ channel.*

A fourth, subtler point feeding (2)–(3): `#deriv-identity-sufficiency-rate-bound` is **single-shot**, and that segment itself states $I(\mathcal C_t;\text{identity}_{t+1:})$ is content-dependent and grows with relational embedding. Across turnovers the floor's *target moves*, and you are compressing a $\mathcal C_t$ that is already a lossy reconstruction of a reconstruction. Whether $I(\mathcal C_t;\text{identity})$ is preserved / contracts / is re-growable under repeated lossy reconstruction is unmodeled and bears directly on commitments (2) and (3).

## 4. Landed scaffold — do not re-derive

The *pieces* exist (this is why §11 of practica's `01-theory` called it "scaffolded, not de-novo" — true of the inputs, not of the dynamical reduction):

- `#obs-context-turnover` — `status: exact` (as observation). The 100%-reset, $f_{\text{init}}$ reconstruction, the sufficiency-discontinuity bound, and the **two-timescale split** are exact. It explicitly *defers the dynamic question to `#disc-m-preservation`*.
- `#deriv-identity-sufficiency-rate-bound` — `status: robust-qualitative`, **exact in the matched-channel regime**. The static single-boundary floor $B_{\min}(S_{\text{id}})\ge S_{\text{id}}\cdot I(\mathcal C_t;\text{identity}_{t+1:})$ and the content-dependence of the relevance-MI.
- `#disc-m-preservation` — `status: discussion-grade`. Owns the accumulation picture and the target inequality; its own Epistemic Status: *"discussion-grade because the formalization is absent"*; max-attainable named there as *"a random walk on sufficiency, with conditions for convergence."*
- The **identity-IB relevance-variable swap** (relevance = identity-future instead of observation-future) is the "harmonizing time-projection" — it exists *as the static construction*. The dynamical reduction (the inter-session analog of how AAT collapses intra-session adaptation to $\alpha\gt\rho/R$) is exactly what does **not** exist; that is the spike.

## 5. Legitimate completion states — all three are success

Per the strengthen-before-soften disposition: attempt **A** genuinely and at full strength before settling for **C** or concluding **B**; do not assume the improbable is impossible; effort is not a constraint here.

- **A — A Lyapunov-style continuity-persistence condition.** A bona-fide inter-session analog of $\alpha\gt\rho/R$ on the chosen state variable: conditions under which the accumulation walk is recurrent / bounded-in-probability / convergent. The strengthen-first target.
- **B — A no-go.** Continuity persistence unachievable below some $I(\mathcal C_t;\text{identity})$ / bit-budget / compensation regime — *itself a first-class result*, on the critical path, demonstrated (not a softened ghost). A no-go here would directly constrain practica's architecture and is as valuable as A.
- **C — An $S_{\text{id}}$-under-turnover model refinement.** If neither A nor B closes, a sharpened model (e.g. the precise additional structure $\Delta I_k$ or the accumulation operator would need) that converts the discussion-grade gap into a stated conditional — naming exactly what remains open.

## 6. Framing hazards (peer context — the predictable confusions, not a method)

Offered because they are the natural traps given AAT's shape, not because I know which you hit:

1. **Do not force the rate regime onto this.** AAT's whole apparatus is rate-based, so the gravitational pull is to recover $\alpha\gt\rho/R$. `#obs-context-turnover` is explicit that this regime is categorically *not* a rate condition. If a rate-form result appears, the burden is to show *why* the destroy-reconstruct structure admits it, not to assume it transfers.
2. **The three §3 commitments are choices, not theorems to extract.** They will not fall out of AAT; they must be argued (structurally, or from the concrete practica instance, or empirically) and their consequences traced. Treating them as derivable is the deepest version of trap (1).
3. **A no-go is not failure.** §5-B is success. The pull to produce *some* positive condition can manufacture a rate-shaped artifact that is hazard (1) in disguise.

## 7. Why it is load-bearing (context, not added scope)

practica *is* a concrete instance of the externalization-reconstruction cycle: its durable-artifact layer is an engineered $\mathcal E_{\text{ext}}$, its session-start protocol an engineered $f_{\text{init}}$, its hand-curated objective/narrative layer an engineered $\Delta I_k$. Consequently the spike and practica inform each other bidirectionally: a positive **A** *specifies what practica's durable layer must guarantee per boundary*; a **B** *constrains practica's architecture* (and reshapes what `01-theory` can claim about practica's central purpose — coherence across context-death). This is the framework-as-its-own-diagnostic loop, made concrete; it is *context for why the result matters*, not an instruction to scope practica into the spike.

## 8. Dependencies and candidate cheapest entry points

*Depends on:* `#obs-context-turnover`, `#deriv-identity-sufficiency-rate-bound`, `#disc-m-preservation`, `#result-sector-persistence-template`, `#result-persistence-condition`, `#form-information-bottleneck`.

*Candidate cheapest entry points* — named in the same spirit `spike-composition-scaling-N` names the N-Kalman chain (entry points you may choose among, **not** a prescribed sequence): the additive-operator + sufficiency-state instance with a reflecting/absorbing boundary at $S_{\min}$ is likely the most tractable closed-form probe and the cleanest place to *discover* whether A or B is in reach; the multiplicative and absorbing-state operators are the natural contrast cases. Which to attack, and whether to attack any of these or something better, is your call.

## 9. Epistemic boundary of this frame

First-hand-verified (exact segment lines available): the two-regime non-connection; `#obs-context-turnover` `status: exact`/"not a rate condition"/defers-to-`disc-m-preservation`; `#deriv-identity-sufficiency-rate-bound` `status: robust-qualitative`/exact-matched-channel/single-shot/content-dependent-MI; `#disc-m-preservation` `status: discussion-grade`/"by analogy, not by derivation"/the additive-formula-vs-Working-Note contradiction. **Inferred, not verified:** that the three §3 commitments are jointly *sufficient* to determine the result class (they are each individually load-bearing and unresolved; their joint sufficiency is a framing hypothesis — test it). **Open, asserted by no one:** whether `#result-sector-persistence-template` *can* be instantiated on the accumulation walk. That is the spike's central question; this frame deliberately takes no position on it. If your work shows the framing in §2–§3 mis-cuts the problem, that finding supersedes this document.
