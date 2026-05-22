# §1 cluster — Effects-Spiral promotion attempt (strengthen-first pass #2)

*Strengthen-first pass on the synthesis's claim that `#der-adversarial-destabilization`'s Effects-Spiral can be lifted from `discussion-grade` to `conditional-derived` for the constant-sum sub-scope via CPT 2021 Theorem 19 + Proposition 17. This file asks: does that lifting actually work? — and if not, what is the honest residual?*

## The state of the Effects-Spiral

Per `#der-adversarial-destabilization` (§ "Corollary: The Effects Spiral", lines 57–65; Epistemic Status line 71):

> The effects spiral (corollary) is *discussion-grade* — the positive-feedback mechanism is qualitatively clear, but formalizing the $\gamma_A(\Vert\delta_B\Vert)$ functional form and proving instability under it requires specifying how an agent's degrading model affects its action quality, which the theory does not yet formalize.

The mechanism schematic:
$$\Vert\delta_B\Vert \uparrow \;\Rightarrow\; B\text{'s actions become erratic} \;\Rightarrow\; \gamma_A \uparrow \;\Rightarrow\; \rho_B \uparrow \;\Rightarrow\; \Vert\delta_B\Vert \uparrow$$

The open piece: $\gamma_A$ as an *increasing function* of $\Vert\delta_B\Vert$, with a derivable instability theorem under it.

## What CPT Theorem 19 + Prop 17 give

CPT 2021 Theorem 19 (verbatim from `ref/converted/cheung-piliouras-tao-2021-passivity-regret/cheung-piliouras-tao-2021-passivity-regret.md` line 352):

> Poincaré recurrence occurs in the strategy space $\Delta$ for any dynamical game system where (1) each agent employs a learning dynamic which is a convex combination of FTRL; and (2) the underlying game is a graphical constant-sum game with a fully-mixed Nash equilibrium.

The mechanism (CPT §6, condensed in `00-status-and-cpt-draft.md` line 41):
1. Lossless (storage) MLO + lossless (storage) game operator ⟹ lossless DGS ⟹ $L_1 + L_2$ is a constant-of-motion.
2. The game dynamic is divergence-free (game payoff $p_i$ doesn't depend on agent $i$'s own cumulative payoff $q_i$).
3. Trajectories stay in level sets of $L_1 + L_2$; level sets are bounded; volume-preserving + bounded orbits ⟹ Poincaré recurrence.

**What this licenses:** under (1)+(2) [convex-combination FTRL + graphical-constant-sum with fully-mixed Nash], the joint dynamic does NOT converge to Nash — it cycles forever. This is a *theorem*, exact.

## The candidate promotion: "Effects-Spiral conditional-derived for constant-sum sub-scope"

The synthesis's claim is that this CPT result provides a *derivation* of the Effects-Spiral for the constant-sum sub-scope. Let me trace whether it actually does.

### Step 1: state-space alignment

`#der-adversarial-destabilization` works in **error space**: $\delta_B$ is agent $B$'s mismatch state, evolving under $\dot\delta_B = -F_B(\delta_B) + w_B(t)$ with $w_B$ containing the coupling term $\gamma_A \mathcal T_A$. The Effects-Spiral says $\Vert\delta_B\Vert \to \infty$ as the spiral runs.

CPT's Theorem 19 works in **strategy space**: $\mathbf x(t) \in \Delta$ recurs to within any $\epsilon$-neighborhood of its initial point. The strategy space is *bounded* (simplex), so trajectories cannot escape to infinity — they orbit.

**These are different conclusions.** The Effects-Spiral predicts unbounded $\Vert\delta_B\Vert$ (or until structural adaptation triggers); CPT Theorem 19 predicts bounded recurrent orbits. They are not the same dynamic phenomenon.

### Step 2: what CPT says about the "spiral" pattern

Look at what CPT's mechanism predicts for a constant-sum two-player game (the simplest non-trivial case): the joint dynamic spirals around the Nash equilibrium with constant energy, *forever, on a fixed orbit*. There is no spiraling-out — the orbit is *closed* (or more precisely, recurrent). The agent's strategy never moves further from Nash than its initial level set permits.

In Effects-Spiral vocabulary: $\Vert\delta_B\Vert$ does NOT increase under CPT Theorem 19's hypotheses. It stays bounded forever, oscillating. The "spiral" in CPT is geometric (a literal spiral orbit in strategy space) but it is **not** a destabilization — it is recurrence at fixed energy.

**The Effects-Spiral in AAT is a destabilization spiral** — $\Vert\delta_B\Vert$ grows past $R_B$, the agent's stability region collapses. CPT's spiral is a recurrence spiral — $\Vert\delta_B\Vert$ stays bounded on a level set forever.

**These are not the same phenomenon.** The synthesis conflated two different "spiral" patterns: CPT's geometric-orbit recurrence (which is a *negative* result for convergence-to-Nash analysis) and AAT's positive-feedback destabilization (which is an *instability* result for adaptive-agent persistence).

### Step 3: where the CPT machinery actually does apply to AAT

CPT Theorem 19 + Prop 17 *does* land somewhere in AAT — but it lands on `#deriv-strategic-composition`'s cyclic sub-scope ($\beta'$), not on `#der-adversarial-destabilization`'s Effects-Spiral. Specifically:

- For an agent operating in the FTRL family (replicator dynamic, gradient descent, MW — `#deriv-strategic-composition` sub-scope $\beta'$), against a graphical-constant-sum game with fully-mixed Nash, the joint dynamic is Poincaré recurrent in strategy space.
- This is the **no-convergence** result for the strategic-composition $\beta'$ sub-scope: agents do not converge to Nash, they recur. Per `#disc-stability-certificate`'s notation, the joint dynamic at the Nash equilibrium has Case-(iii) linearization (by §02 Result 4 above), i.e., R0-loss.
- This makes the R0-loss landing rigorous *for the strategic-composition $\beta'$ sub-scope*: the joint dynamic of FTRL × graphical-constant-sum-game is in R0-loss class.

This is a legitimate landing — it gives a concrete agent class instantiating R0-loss in AAT's existing taxonomy. But it does **not** lift the Effects-Spiral; it lifts a *different* claim: the no-convergence claim for cyclic strategic interactions.

### Step 4: what the Effects-Spiral actually needs (and CPT doesn't provide)

For the Effects-Spiral lift to be a real derivation, we need:
- A specification of $\gamma_A(\Vert\delta_B\Vert)$ as an increasing function. CPT does not address this; CPT's $\gamma$-equivalent (the coupling matrix $\mathbf A^{ik}$ in the graphical constant-sum game) is a **fixed matrix**, not a state-dependent function.
- A demonstration that under this state-dependent $\gamma$, the joint dynamics has an unstable manifold escaping the stability region. CPT proves the *opposite*: the joint dynamics on its level set is bounded recurrent.

The Effects-Spiral mechanism — "agent's degrading model makes it more legible to the adversary, increasing coupling effectiveness" — is a **nonlinearity in the coupling** that CPT's linear-coupling-matrix framework does not model. The two settings are structurally different.

### Step 5: is there *any* nearby strengthening?

There is a real strengthening available, but it is **not** the Effects-Spiral lift. It is the *converse* claim:

**Claim (R0-loss-implies-no-spiral, conditional).** If a target agent $B$ is operating in an FTRL family and the joint dynamic with adversary $A$'s (FTRL-family) update satisfies CPT Theorem 19's hypotheses (graphical-constant-sum payoff structure, fully-mixed Nash, fixed coupling matrix), then **the Effects-Spiral does NOT occur**: the joint dynamic is Poincaré recurrent on a bounded level set, $\Vert\delta_B\Vert$ does not escape past $R_B$.

This is a useful claim — it carves out a class of adversarial settings where the Effects-Spiral provably cannot occur (because the coupling is matrix-fixed and the storage geometry forces bounded orbits). It is the **dual** of the Effects-Spiral, not a derivation of it. It belongs as a discussion note in `#der-adversarial-destabilization` ("the Effects-Spiral requires state-dependent coupling — under fixed-matrix coupling in the FTRL+constant-sum regime, CPT 2021 Theorem 19 gives bounded recurrence instead, so the spiral cannot occur in that sub-scope").

## Honest verdict on strengthen-first pass #2

**The synthesis's proposed promotion does not survive close examination.** CPT Theorem 19 does not derive the Effects-Spiral for the constant-sum sub-scope. It addresses a different phenomenon (bounded recurrent orbits in strategy space) and rules out the state-space behavior the Effects-Spiral predicts (unbounded mismatch growth in error space).

What survives:
- **R0-loss instantiation:** FTRL × graphical-constant-sum-with-fully-mixed-Nash is a concrete agent class realizing R0-loss in AAT taxonomy. This is a real landing — it gives `#result-certificate-existence`'s new R0-loss rung a worked-out instance with citation. Tier: *exact*, by CPT 2021 Theorem 19 (Poincaré recurrence; the linearization at Nash has Case-(iii) imaginary-axis-semisimple spectrum by §02 Result 4).
- **No-spiral converse:** the same hypotheses *rule out* the Effects-Spiral in this sub-scope. Tier: *exact*, by the same theorem. This belongs as Discussion in `#der-adversarial-destabilization` and as Discussion in `#deriv-strategic-composition` $\beta'$.
- **Effects-Spiral remains discussion-grade.** The state-dependent-coupling formalization is genuinely open and is not addressed by the cluster. The synthesis's proposed lift was a false strengthening — and noticing that *is* a strengthen-first outcome: we have a sharper picture of what would actually be needed to lift the Effects-Spiral (state-dependent $\gamma$, instability proof under it) versus what CPT provides (state-independent $\gamma$, bounded recurrence).

## What to do in the verdict

- Land the R0-loss instantiation (FTRL × graphical-constant-sum) as a worked-out example under `#result-certificate-existence` once the new R0-loss rung is added (gated on §02 Result 1+2+3 lifting). Tier: exact.
- Add a Discussion note in `#der-adversarial-destabilization` recording the no-spiral converse (CPT Th 19 *rules out* Effects-Spiral in the FTRL+constant-sum sub-scope; the Effects-Spiral requires structurally different coupling). Tier: discussion / cited.
- Add a Discussion note in `#deriv-strategic-composition` $\beta'$ identifying the FTRL+constant-sum case as the R0-loss instantiation of the cyclic-distributional regime. Tier: cited.
- Effects-Spiral remains `discussion-grade`. The genuine promotion path (state-dependent coupling + instability proof) is `spikes/PROPOSED.md` Tier 1's existing item ("Effects-spiral eigenvalue condition — concrete agent classes") — that work is **not subsumed** by this cluster; the cluster surfaces that CPT does not address it.

## Why this is a strengthen-first success, not a failure

The conservative move (the soft-landing) would have accepted the synthesis's "Effects-Spiral conditional-derived" claim and let the apparent promotion stand. The strengthen-first move was to **work through the alignment carefully**: CPT acts on strategy space, AAT's Effects-Spiral acts on error space; CPT's coupling is matrix-fixed, AAT's Effects-Spiral requires state-dependent coupling; CPT predicts boundedness, AAT's Effects-Spiral predicts escape. The two patterns are *opposed* in conclusion, not aligned.

Catching this prevents a real overclaim. The verdict's correct posture is: the cluster delivers a *different* strengthening than the synthesis advertised — landing R0-loss with a worked instance and giving the no-spiral converse as a Discussion-level safety result. The Effects-Spiral lift is **refuted** as a CPT-derived promotion; the proper path remains the existing Tier-1 spike-proposal targeting state-dependent coupling.

This is exactly the strengthen-first pattern from `~/.claude/memory/epistemic-discipline/integration-is-replacement.md`: the *refuted* candidate promotion is *deleted* from the proposal slate (not kept-softened-with-a-pointer), and the *genuinely-true* converse claim is named explicitly as present truth.
