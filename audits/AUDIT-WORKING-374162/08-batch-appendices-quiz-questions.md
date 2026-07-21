# Comprehension Quiz — Batch 8 (Part I Appendix A backfill)

*Coverage: the Appendix-A derivation layer behind Part I. This batch deliberately targets epistemic-tier discrimination — what is exact, what is conditional on which named premises, what is a proven no-go, and what the corpus itself marks as asserted-but-not-yet-derived. A summary-fed agent flattens all of these into one confidence level; these questions punish that.*

## (1) Critical Mental Model

### Q b08-1.1 [mental-model]
The corpus contains a segment whose entire content is an *open question about its own neighboring segments' prose*. Which hand-off claim does `sketch-structural-adaptation-genericity` isolate as plausibly overclaimed, what is the precise gap (what does Cor A.1S.1's own explicit instance do that breaks the inference), and what does the strengthen-before-soften discipline prescribe instead of tightening the prose?

### Q b08-1.2 [mental-model]
"The framework proves agents must spend $n\alpha/2$ nats per unit time to survive." What premises does this flatten away? List the named scope conditions of the persistence-cost bound, which filter saturates it, and what makes the bound filter- and substrate-agnostic *within* that scope.

### Q b08-1.3 [mental-model]
In the Model-S no-go (the derivation that there is no horizon-independent non-exit bound under additive stochastic forcing), explain the "reusable no-go signature": what is the three-step signature, and what is its intended function in the corpus's future epistemic economy (what does it let a future agent do *without* re-deriving anything)?

### Q b08-1.4 [mental-model]
In the discrete-time sector-condition derivation, why does discretization demand a *strictly stronger* condition than the continuous sector condition? Name the two components of DA2', say which one is new relative to A2' and why the continuous analysis never needed it, and give the class of pathological correction functions the gap admits.

### Q b08-1.5 [mental-model]
A systems engineer says: "correlated telemetry channels mean our tempo sum overcounts — we should subtract the channels' mutual information." In the tempo-additivity derivation (the scope of when the additive tempo formula holds), this contains two distinct errors. Name both (one about sign, one about the impossibility of the proposed correction), and the regime in which their intuition *is* rigorously right, with the closed-form object that replaces the MI subtraction there.

### Q b08-1.6 [mental-model]
In the tempo-additivity derivation, what does it mean that the additive-tempo equality set is "strictly larger than independence"? Describe the harmonic-mean hypersurface phenomenon and what cancels against what on it.

### Q b08-1.7 [mental-model]
The asynchrony refinement: why does *instantaneous* cross-channel noise correlation not break tempo additivity for independent Poisson event streams, and what kind of noise dependence actually does?

## (2) Mathematics

### Q b08-2.1 [math]
Reproduce the failed-certificate anatomy from the Model-S no-go (no horizon-independent non-exit bound under additive stochastic forcing): define $G(t)$ and the compensated $S(t)$, state why $G$ is not a supermartingale and why $S$ is one, and then the killing blow — where exactly is $S$ negative, and why is that region "most of the time" under the mean-square persistence condition? Name the deeper generator-level obstruction.

### Q b08-2.2 [math]
In the persistence-cost derivation, derive the bound's arithmetic: the OU rate-distortion function in the high-resolution regime, the substitution that produces $n\alpha/2$, and the Kalman-Bucy saturation identity in the scalar case (which quantity equals $\alpha/2$?).

### Q b08-2.3 [math]
In the discrete-time sector-condition derivation, write the discrete contraction computation: expand $\Vert\delta_{k+1}\Vert^2$ under the update $\delta_{k+1} = \delta_k - \eta^\ast F_d(\delta_k)$, apply DA2'a and DA2'b, state $\lambda_{\text{eff}}^2$ and the resulting step-size condition. What are the fluid-limit gaps for Model D and Model S respectively?

### Q b08-2.4 [math]
In the Fisher-local update-gain derivation, state the Fisher-local regime's three conditions (R1)–(R3) and the resulting gain operator $K$. What are the AAT-vocabulary correspondences for $U_M$ and $U_o$ in matrix form, and along which direction does the scalar $\eta^\ast = U_M/(U_M+U_o)$ collapse hold in dimensions above one — under which axiom?

### Q b08-2.5 [math]
In the tempo-additivity derivation, give the two-channel signed-deviation formula $\Delta$ (or its structure), the exact condition for $\Delta = 0$, and one concrete synergy witness with its mechanism (why does adding a *noisier* channel sometimes dramatically increase joint information?).

### Q b08-2.6 [math]
The echo-chamber / common-source theorem (in the tempo-additivity derivation): state the common-source noise model, the Sherman-Morrison-derived joint information $f(q)$, why strict concavity of $f$ delivers strict subadditivity, and the saturation statement (what does joint information converge to as channels are added, and why can no channel count escape it?).

### Q b08-2.7 [math]
In the matrix-Loewner persistence derivation, state the matrix-Loewner persistence condition in full (both MP conditions, the Lyapunov equation for $\Sigma_\infty$), and the reduction relationships: which special cases recover the scalar and per-coordinate forms, and what is the precise sense in which per-coordinate is "unsafe"?

### Q b08-2.8 [math]
In the adaptive-gain dynamics derivation, state the four MG conditions each in one line, identify which is the transcription of temporal nesting onto Lyapunov decay rates, and describe the composed result (what Lyapunov candidate, what conclusion for the augmented state).

### Q b08-2.9 [math]
In the variational sector-condition derivation, describe the variational recovery: under what bound does sub-scope β VI promote to α′, what is the sector-constant degradation's scaling and its state-dependence (the $c_\varepsilon(\Vert\delta\Vert)$ form), and what are Regime A and Regime B with the resulting ultimate bound?

## (3) Implications

### Q b08-3.1 [implications]
Place each of these real algorithms in the A2' sub-scope ladder with the *reason* (the derivation, not the label): adaptive Kalman with Mehra-type estimation; vanilla Adam; AMSGrad; MAML; mean-field VI; natural-gradient VI. Two of these placements carry especially striking structural claims — identify them (one is an impossibility-instance on a meta-channel; one is a compute-independent sub-optimality factor).

### Q b08-3.2 [implications]
AMSGrad's max-operation on $v_t$ is usually presented as a convergence patch. Restate what it *is* in the framework's vocabulary, and explain why this reframing matters (what does it predict about which optimizer modifications will and won't restore persistence guarantees?).

### Q b08-3.3 [implications]
An architecture team argues total cross-modal bandwidth is sufficient for their vision-language pipeline. Give the appendix-level rebuttal chain: which two results compose to make bandwidth-per-direction the binding quantity, and what does the matrix-Loewner counterexample say about checking per-modality budgets in the coordinate basis?

### Q b08-3.4 [implications]
Epistemic-cartography question: rank these five claims by epistemic tier as the corpus assigns them, and for each name what would move it up a tier — (a) $P(\tau_R \lt \infty) = 1$ under Model S; (b) the $n\alpha/2$ information-rate floor; (c) the $\sqrt{\tau_{env}}$ mood-timescale law; (d) "structural adaptation is generically necessary for long-lived stochastic-environment agents"; (e) the additive-tempo formula as an operationalization.

### Q b08-3.5 [implications]
The Mehra non-identifiability case: what fails, on which channel, and why does the corpus flag it as a candidate instance of a named meta-pattern? What does this say about the limits of *learning your own noise model* from innovation statistics?

### Q b08-3.6 [implications]
The structural-adaptation-genericity sketch (§Proposed Direction) records three candidate bridge derivations that would close the genericity gap it isolates. Summarize each in a sentence, and state what the honest outcome is if all three provably fail — including which protocol then applies and what happens to the Findings prose.

### Q b08-3.7 [implications]
"Natural-gradient VI vs mean-field VI is a practical engineering preference." Upgrade this to the framework's structural claim: what exactly does mean-field lose, by what factor, why is it unrecoverable by compute or data, and what places natural-gradient VI in full sub-scope α rather than α′?
