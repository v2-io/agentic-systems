# Comprehension Quiz — Batch 6 (through `der-mood-timescale`, incl. `deriv-gain-sector` Props B.1–B.4)

## (1) Critical Mental Model

### Q b06-1.1 [mental-model]
"The persistence condition is $\mathcal T \gt \rho/\Vert\delta_{\text{critical}}\Vert$." This is the most-quoted form in the corpus — and it is a special case expressing only *one* of two conditions. Identify which condition it expresses, under what structural assumptions it is the whole story, and what it silently omits (and therefore overstates) when correction saturates.

### Q b06-1.2 [mental-model]
An agent fails to persist. The framework says the remedy depends on *which* condition failed. Give the remedy menu for task inadequacy and the qualitatively different remedy for structural failure, and explain why "hire more people / add more compute" can be exactly wrong in one of the two cases.

### Q b06-1.3 [mental-model]
What did the gain-sector bridge change about the epistemic standing of the persistence results — what was GA-3 before the bridge, what is it after, and for which agents does it remain a primitive posit? (One sentence each.)

### Q b06-1.4 [mental-model]
What is mood, in AAT's Part-I sense? Give: the object type (what kind of quantity), what it integrates, what it modulates, why it can be defined *before* objectives exist, and the name of the failure mode the modulation band's floor exists to prevent.

### Q b06-1.5 [mental-model]
"Mood inertia should match how fast the world changes." Correct this using the derived mood-timescale scaling law — state the actual relationship and the qualitative reason both extremes (no inertia; never-recovering mood) are suboptimal *for the same reason at opposite ends*.

### Q b06-1.6 [mental-model]
Why doesn't mood — a global scalar coupling all channels — violate directed separation (previewed) / the framework's separation structure? Name the quantitative condition that does the work.

## (2) Mathematics

### Q b06-2.1 [math]
Lay out the α-notation ladder precisely: per-event sector efficiency, per-time sector rate, and adaptive tempo — formulas, units, and the exact condition under which $\alpha = \mathcal T$.

### Q b06-2.2 [math]
In the gain-sector bridge derivation (and its appendix's Prop B.4): State B1 (directional fidelity) and the bridge theorem's conclusion. Then Prop B.4's asymmetry: which sector condition is *equivalent* to local strong convexity, which is strictly weaker, which one does AAT's persistence machinery actually require, and which does the composition bridge lemma require? Sketch the counterexample that separates them.

### Q b06-2.3 [math]
For the matrix Kalman filter: in which inner product does the sector condition hold natively, what is the sector parameter (eigenvalue form), what happens in unobservable directions, and what is the cost of transferring the statement to the Euclidean norm? Under which named axiom does that cost vanish, and via whose theorem?

### Q b06-2.4 [math]
Write the operational persistence condition as a conjunction (both gates, Model D), and identify which gate binds when $\Vert\delta_{\text{critical}}\Vert \lt R$ vs when $R \lt \Vert\delta_{\text{critical}}\Vert$.

### Q b06-2.5 [math]
In the segment defining mood — where mood's persistence-compatibility is discharged as an instance of the adaptive-gain-dynamics MG conditions: Define mood formally (the leaky integral and the modulation law), and state the four MG conditions' instantiations for the mood channel — in particular which condition encodes "quasi-static," as what inequality, and what the mood channel's own sector constant is (with the reason it's exactly that).

### Q b06-2.6 [math]
In the mood-timescale result, derive (or reconstruct) its skeleton: the assumed regime process, the loss, the two-term structure of $J(\lambda)$ (name what each term prices), the leading-order optimum, and the resulting scaling law. What tier does each of the three traveling claims carry (MSE formula / scaling law / interior-optimum shape)?

### Q b06-2.7 [math]
For the scalar Kalman filter (the gain-sector derivation's Prop B.1): what exactly is the sector parameter, and why is the bound tight? Give the steady-state limiting behaviors of $K_{ss}$ in the two regimes ($Q \gg R_{obs}$, $Q \ll R_{obs}$).

## (3) Implications

### Q b06-3.1 [implications]
A reviewer says: "Your persistence theorems assume the sector condition, so the whole framework is assumption-driven." Construct the two-part reply the corpus supports: what the bridge derives and for whom, and what the framework honestly concedes — including why the concession (sub-scope β + five failure modes) is a strength rather than a retreat.

### Q b06-3.2 [implications]
An LLM-based agent's scaffolding wants a "frustration/confidence" state variable that slowly adjusts how aggressively the agent updates on surprises. Map this onto AAT's mood construct: what the variable should integrate, what bounds its modulation must respect and why (two distinct persistence-content reasons, one per end of the band), and what timescale relationship must hold relative to the agent's fast update loop.

### Q b06-3.3 [implications]
The one-point/two-point sector distinction seems like a technicality. Show it isn't: which framework capability *breaks* if you only have the one-point form, and what does this predict about the difficulty gap between proving single-agent persistence and proving composite-agent results?

### Q b06-3.4 [implications]
Why does the framework place mood in Part I rather than Part II, and what does this placement claim about the relationship between affect and goals? What signed/valued aspects of mood does the placement explicitly defer, and to where?

### Q b06-3.5 [implications]
The emotional-inertia literature (affect AR(1) coefficients, inertia maladaptive when high) is cited in the mood-timescale derivation. State precisely what normative reading the derivation gives that literature, what the pathology actually is (careful — it is not "slowness"), and what epistemic weight the corpus assigns to this corroboration.

### Q b06-3.6 [implications]
An agent's operational form passes ($\mathcal T$ comfortably above $\rho/\Vert\delta_{\text{critical}}\Vert$), computed with scalar tempo over its five telemetry channels. Give the two distinct ways this pass could be false comfort, and the sharper conditions that would have to be checked.
