# Temporal Feedback Theory: Novelty, Utility, and Comparative Analysis

## Executive Summary

Temporal Feedback Theory (TFT) is an ambitious axiomatic framework that attempts to unify adaptive feedback systems — Kalman filtering, reinforcement learning, PID control, Bayesian inference, Boyd's OODA loop, biological adaptation, and organizational learning — under a single formal structure built from two axioms (causal structure and the model axiom) and a scope definition. The theory is well-constructed, epistemically transparent, and makes several genuinely novel contributions, but it also overlaps substantially with existing frameworks, particularly Friston's Free Energy Principle (FEP) and established results in control theory and information theory. This analysis evaluates TFT's novelty, compares it against the closest competing frameworks, and assesses its likely utility.[^1]

## The Core Architecture

TFT builds from a scope definition (TF-01: agents coupled to environments under uncertainty) and two axioms: TF-02 (causal structure grounded in temporal ordering, incorporating Pearl's causal hierarchy) and TF-03 (any persisting agent maintains a model functioning as a compressed sufficient statistic of its interaction history). From these, TFT derives the mismatch signal (TF-05), update gain with the uncertainty ratio principle (TF-06), action selection and deliberation costs (TF-07/09), structural adaptation necessity (TF-10), adaptive tempo and persistence thresholds (TF-11), and Lyapunov stability results for adversarial dynamics (Appendix A).[^2][^1]

The explicit epistemic labeling — axiom, derived, empirical claim, hypothesis, discussion — applied to every proposition is a notable methodological strength that most competing frameworks lack.[^1]

## Closest Competing Frameworks

### Free Energy Principle / Active Inference (Friston)

The FEP is TFT's most direct competitor. Both aim to unify perception, learning, and action under a single formal framework for adaptive agents. Both treat the agent as maintaining an internal model that generates predictions, with the mismatch between prediction and observation as the core adaptive signal. Both derive action as serving dual roles — reducing prediction error through both model updating (perception) and environment manipulation (action).[^3][^4][^5]

| Dimension | TFT | FEP / Active Inference |
|-----------|-----|------------------------|
| Grounding | Temporal ordering + information theory | Variational inference + thermodynamics |
| Core signal | Mismatch \(\delta_t = o_t - \hat{o}_t\) | Variational free energy \(F\) |
| Update rule | \(\eta^* = U_M/(U_M + U_o)\) | Gradient descent on \(F\) |
| Action objective | CIY-integrated policy (TF-08) | Expected free energy minimization |
| Exploration-exploitation | Explicit deliberation cost formalization | Epistemic/pragmatic value decomposition |
| Structural adaptation | Explicit proposition (10.1) with destruction-creation cycle | Model comparison via free energy |
| Adversarial dynamics | Lyapunov-based destabilization proofs | Minimal treatment |
| Maturity | Working draft, no empirical validation | ~15 years of development, substantial empirical work[^6] |
| Accessibility | Modular, axiomatic, readable | Notoriously difficult to understand[^6] |

Key difference: TFT grounds causality in temporal ordering as the most primitive notion and explicitly incorporates Pearl's causal hierarchy as three levels of epistemic access. FEP grounds in variational inference with thermodynamic motivation but has been criticized for the unclear dialectical relationships between its mathematical and empirical claims. TFT's deliberate decision *not* to assume a thermodynamic connection is philosophically interesting and avoids some of FEP's controversies.[^6][^1]

### Conant-Ashby Good Regulator Theorem and Ashby's Requisite Variety

TFT's TF-03 (model axiom) is closely related to the Good Regulator theorem — "every good regulator of a system must be a model of that system". However, TFT extends this significantly by formalizing *what kind of model* through the information bottleneck framework (model as sufficient statistic on a rate-distortion curve) and by establishing model class fitness \(\mathcal{F}(\mathcal{M})\) as a quantitative measure. Ashby's Law of Requisite Variety — "only variety can absorb variety" — maps to TFT's requirement that adaptive tempo must exceed environmental change rate (\(\mathcal{T} > \rho\)), but TFT provides a much richer quantitative treatment.[^7][^8][^9][^1]

### Predictive Processing / Prediction Error Minimization

The predictive processing framework (Clark, Hohwy) posits that the brain minimizes prediction error through hierarchical generative models. TFT's mismatch signal is structurally identical to prediction error, and TFT's hierarchical temporal nesting (TF-11) parallels predictive processing's hierarchical model. However, TFT is domain-general rather than neuroscience-specific, and adds the quantitative machinery of adaptive tempo, persistence thresholds, and adversarial dynamics that predictive processing lacks.[^10][^11]

### Information Bottleneck (Tishby)

TFT explicitly uses Tishby's information bottleneck as its model compression framework in TF-03. This is an acknowledged incorporation, not an independent discovery. The novel contribution is applying it specifically as the criterion for model optimality in an agent-environment feedback loop, connecting it to model class fitness and the structural adaptation trigger.[^12][^13][^14]

### Boyd's OODA Loop

TFT explicitly aims to formalize Boyd's OODA loop and claims to derive several of Boyd's qualitative insights as quantitative theorems. The OODA loop has been criticized as "vague enough that its defenders and attackers can each see what they want to see in it" and "not incorrect, but neither is it unique or especially profound". TFT's primary value proposition for Boyd's framework is converting qualitative military doctrine into falsifiable mathematics — particularly the tempo advantage ratio \(\mathcal{T}_A/\mathcal{T}_B\), the persistence threshold, and the Lyapunov formalization of the "effects spiral".[^15][^16][^17][^1]

### Two-Timescale Stochastic Approximation

TFT's temporal nesting (TF-11) with the convergence constraint \(\nu_{n+1} \ll \nu_n\) is closely related to the well-established theory of two-timescale stochastic approximation (TTSA) and singular perturbation methods. TTSA already provides formal convergence guarantees for multi-timescale learning systems, and TFT's Appendix A sketch of N-timescale stability via Tikhonov's theorem is standard singular perturbation theory. The formal machinery exists; TFT's contribution here is the *interpretive* framework connecting it to adaptive agents across domains.[^18][^19][^15]

## Genuinely Novel Contributions

Several elements of TFT appear to be genuinely original or to combine existing ideas in ways not previously formalized:

### Adaptive Tempo as Unified Scalar

The definition \(\mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)*}\) — combining event rate and update quality into a single measure of adaptive capacity — is a clean conceptual contribution. While Boyd qualitatively noted that orientation quality matters as much as loop speed, and the OODA literature informally discusses "tempo advantage", TFT appears to be the first to define this as a precise mathematical quantity with derivable consequences.[^16][^20][^21]

### Persistence Threshold and Mismatch Dynamics ODE

The mismatch dynamics equation \(\frac{d|\delta|}{dt} = -\mathcal{T} \cdot |\delta| + \rho\) and its steady-state result \(|\delta|_{ss} = \rho/\mathcal{T}\) yield the persistence threshold \(\mathcal{T} > \rho\) as a necessary condition for agent viability[^16]. While conceptually related to Ashby's requisite variety, this specific formalization — relating adaptive tempo to environmental change rate with a quantitative steady-state — appears novel. The Lyapunov generalization (Appendix A, Propositions A.1–A.3) extending this to nonlinear dynamics under sector conditions is mathematically sound and adds genuine rigor[^15].

### Deliberation Cost Formalization

TF-09's treatment of deliberation cost — where deliberation of duration \(\Delta\tau\) accumulates mismatch \(\rho \cdot \Delta\tau\), establishing that deliberation is justified if and only if the action quality gain exceeds this accumulated cost — is a precise formalization of a concept that Boyd articulated qualitatively and that decision science has treated informally. The explicit connection to the explore-exploit tradeoff through accumulated mismatch during the pause is novel.[^22][^23]

### Adversarial Destabilization via Lyapunov Analysis

The formalization of "getting inside the opponent's OODA loop" as a Lyapunov instability result — particularly Proposition A.3 (adversarial destabilization when \(\gamma_A \cdot \mathcal{T}_A > \Delta\rho^*_B\)) and Corollary A.3.1 (the effects spiral as positive-feedback instability) — converts qualitative military doctrine into formal dynamical systems theory. The concept of **adaptive reserve** \(\Delta\rho^* = \alpha R - \rho\) as a single number characterizing an agent's robustness to shock is a useful conceptual tool.[^15]

### Structural Adaptation Necessity (Proposition 10.1)

The formal proof that persistent irreducible mismatch after parametric convergence is diagnostic of model class inadequacy — and that structural change is *necessary* when \(\mathcal{F}(\mathcal{M}) < 1 - \epsilon\) — connects information-theoretic model sufficiency to the practical question of when to change the model class. While Bayesian model selection, neural architecture search, and Kuhn's paradigm shifts all address this intuitively, the unified formal treatment connecting it to the information bottleneck framework appears novel.[^12]

### Action Fluency as Distinct Concept

The distinction between model sufficiency \(S(M_t)\) and action fluency — where an agent can have high sufficiency but low fluency (a chess engine with perfect rules knowledge but expensive search) or moderate sufficiency but high fluency (a trained reflex) — is a conceptually useful separation not clearly articulated in competing frameworks.[^23]

## Significant Overlaps and Acknowledged Borrowings

TFT honestly acknowledges most of its borrowings, which is a strength. Nevertheless, the degree of overlap with existing work is substantial:

- The uncertainty ratio \(\eta^* = U_M/(U_M + U_o)\) is exactly the Kalman gain in the scalar case, as TFT acknowledges. The claim that this generalizes universally is the weakest empirical claim, with TFT itself estimating ~60-65% confidence for partial unification and ~30% for full unification under one equation.[^24][^1]
- The information bottleneck framework (TF-03) is Tishby's method applied to agent models.[^13]
- Pearl's causal hierarchy (TF-02) is explicitly incorporated.[^25][^26]
- The mismatch signal (TF-05) is structurally identical to prediction error in predictive processing.[^2][^10]
- Multi-timescale nesting (TF-11) uses standard singular perturbation theory.[^19]
- The Lyapunov analysis (Appendix A) applies standard nonlinear control theory tools.[^27]

## Critical Assessment

### Strengths

- **Exceptional epistemic hygiene.** Every claim is tagged with its status (axiom, derived, hypothesis, discussion, empirical). This is rare in theoretical frameworks and makes the theory much easier to evaluate and challenge.[^1]
- **Cross-domain coherence.** The domain instantiation tables throughout the documents demonstrate genuine structural parallels across Kalman filtering, RL, PID, Bayesian inference, Boyd, biology, and organizations.[^16][^24][^12]
- **Modular axiomatic structure.** The dependency chain (TF-01 → TF-02/03 → TF-05 → TF-06 → ...) is explicit, making it clear what depends on what and where the theory is most vs. least certain.[^1]
- **Mathematical rigor where it counts.** The Lyapunov analysis (Appendix A) and the formal propositions (5.1, 10.1, 11.1) are genuine proofs, not hand-waving.[^15][^16][^12][^2]
- **Practical concepts with clear semantics.** Adaptive tempo, adaptive reserve, deliberation cost, and action fluency are concepts that practitioners across domains could use immediately.

### Weaknesses

- **No empirical validation.** The theory is entirely formal. FEP has ~15 years of empirical testing across neuroscience, robotics, and psychiatry. TFT has none. Some of its strongest claims (the universality of \(\eta^* = U_M/(U_M+U_o)\), the mismatch ODE) need empirical testing.[^4][^28]
- **"Structural analogy" vs. genuine unification.** The theory risks conflating structural similarity with deep identity. That Kalman gain and Bayesian posterior weight have the same form could reflect a deep universal principle or could reflect that both are special cases of convex combination under Gaussian assumptions. The README acknowledges this tension honestly (~30% confidence in full unification).[^1]
- **Multi-agent theory is thin.** Only the adversarial dyad is treated (TF-11 + Appendix A). Cooperative, competitive-cooperative, and network multi-agent dynamics — which are where the most interesting real-world complexity lives — are flagged as open problems.[^1]
- **The mismatch ODE is acknowledged as first-order approximation.** The quantitative predictions depend on a linear hypothesis that the theory itself labels as "almost certainly needing nonlinear refinement". The Lyapunov analysis partly addresses this but at the cost of losing quantitative predictions.[^16][^15]
- **Missing comparison to FEP.** While the README mentions active inference in passing, TFT does not systematically compare itself against FEP — its closest competitor. Given the overlap, an explicit differentiation section would strengthen TFT's positioning.

### Where TFT Adds Value Over Existing Frameworks

| Capability | FEP | Predictive Processing | Control Theory | Boyd/OODA | TFT |
|------------|-----|----------------------|----------------|-----------|-----|
| Formal adversarial dynamics | Minimal | No | Limited (H∞) | Qualitative | Strong (Lyapunov) |
| Cross-domain unification | Biology + cognition | Neuroscience only | Engineering only | Military only | 8+ domains |
| Epistemic transparency | Low[^6] | Medium | High | Low | Very high |
| Deliberation cost | Implicit in expected FE | Not formalized | Not applicable | Qualitative | Formal (TF-09) |
| Structural adaptation trigger | Model comparison | Model revision | Not formalized | Destruction/creation | Formal (Prop 10.1) |
| Persistence threshold | Implied | Not formalized | Stability margins | Qualitative | Formal (Prop 11.1) |
| Empirical validation | Extensive[^4] | Extensive | Extensive | Case studies | None |

## Assessment of Utility

TFT's most likely utility lies in three areas:

1. **As a pedagogical and translational framework.** By providing a consistent notation and dependency structure across domains, TFT could help practitioners in one field (e.g., control theory) recognize and borrow techniques from another (e.g., Bayesian inference). The domain instantiation tables are genuinely useful for this.

2. **As a design framework for AI agents.** The concepts of adaptive tempo, deliberation cost, action fluency, and structural adaptation necessity map directly to LLM agent design decisions — when to deliberate vs. act, when to retrain vs. fine-tune, how to balance speed vs. quality in inference pipelines. The README explicitly flags LLM training strategy as a planned companion document.[^1]

3. **As a formalization of Boyd for quantitative domains.** Military operations research, competitive strategy, and adversarial AI could benefit from TFT's quantitative treatment of tempo advantage, adaptive reserve, and the effects spiral — concepts that have been qualitative in the Boyd tradition.[^15][^16]

The theory is less likely to displace FEP in neuroscience (FEP has too much empirical infrastructure) or replace established methods in any single domain (Kalman filters, RL algorithms, PID controllers all work fine without TFT). Its value is at the interfaces — connecting domains, translating insights, and providing a common formal language.[^4]

## Conclusion

TFT is a well-crafted theoretical framework that makes several genuinely novel contributions — particularly adaptive tempo, the persistence threshold, deliberation cost formalization, adversarial Lyapunov analysis, and the structural adaptation necessity proof. It has exceptional epistemic transparency and cross-domain breadth. Its primary weaknesses are the absence of empirical validation and the risk that its "unification" is more structural analogy than deep identity. Against its closest competitor (Friston's FEP), TFT offers greater accessibility, better adversarial dynamics, and explicit deliberation cost treatment, while lacking FEP's empirical base and thermodynamic grounding. The framework is most valuable as a translational and design tool — helping practitioners see common patterns across domains and making principled design decisions for adaptive systems. With empirical validation and a systematic comparison to FEP, TFT could become a useful complement to existing frameworks rather than a replacement for any one of them.

---

## References

1. [README.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/80363228/be70b765-d741-4178-a3cb-12423eb612d1/README.md?AWSAccessKeyId=ASIA2F3EMEYEYRTPHDBS&Signature=g2FSgT18rqHG%2FXHEAUUwhelDBhw%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDe4dXHmEkuvp9WxWs4KCv7yFNCy3T7m88xa5IHVaTJVgIgMQOuiJH2zIlO8cvfhaIy4G3oAYoLj%2BP05E2b3RvUoeAq8wQIThABGgw2OTk3NTMzMDk3MDUiDOHlu0Yvlfkf7WAvMCrQBOBXYcDENI%2BFDsTrDKsgk2wK3G8E6XaekUOocHtreu64Q7orBRSdQfKWOoEXR8ZB48il4OZd15Xcx%2Ba%2F8R4tpc0Jo%2FERJmp96fWz4%2FPQ9ulCSyav1wJbAink3jXVC1Q%2BVvnCmk3FWKu3ZPiucplb3QgFZEZm3aQoGEqMUe0cs3P8apqLi3ZZXUdf4buHBAmeTUQLZ5FYk5aImLQhCsa1nWAx7YWZd1c%2FwCkLiOoUmJNYkTdKUaRYJJABQ9tuXlo4RpbfuYuUJ3eqHEKZDozGthlLUzLlZhhEchu%2FB4u99mmnU1JGF3NQRdSc1Pt6lSkMuFVoyGeknrNpwcpaqKcMl6LyeUzrxnHGiyMhU0ddiCcPXyhNqEWeIClA%2Bu%2FzLKP4htlmhaK5ukb%2BVfjQw3BX0ekVTxDoQUzWUp2Rtj8soSfrDu%2BL0Pq5QNl0rzs2AMKtVmJmme52U5yE9GKDtXhVTCp5TtmBMt3h0sV1oWKzSYHCu0hy9vZ2az8D4rg4FDQfJvdBVDVujzYh0WYLexQsNUCBJ%2BZiCUGJ19yV8iG%2BOkytUitAwa%2FGDdn2dhQ17UYiOlZTXR35YAqs87I1IM5tL8bcSRIj3Kg2eF4T08lz6eDttQDf30cRvfIFSsxnWnLJMLYTmSJTICX%2FAFlCe92dziHt3OEp%2FAXn%2BBAUbPYBqt7pPOkFfTnzg5khtySSgVliSi13%2F%2BG0VnD1CVf0Ca8WISxUC%2By8bd2xiplUWmiDcCPpGR3kkMAGae1zZZ2Lg300o%2BINXAXvhXT5%2Fd8zXGjMQv4w%2Fd6JzQY6mAHMZ4XMwgvdqd53y9OjLrFzEExWMch49zjPZ9RsMdpCIdQLA%2FXd9rFqThLwL9U250FoxCCa29UAQNIiVoJVOiFq20F%2Fvjn2MP1KlT2omksN120cxSDauzzJNhdESHFXiyHYK1Rdlds1siXdtTgwQ7%2FJDBM%2BnulOsa%2F9yQDzsUTqALuKVYEbeaMZFDgR4w6ArLOVYrZd97rSiA%3D%3D&Expires=1772257057) - # Temporal Feedback Theory (TFT) — Working Draft

A first-principles formal theory of adaptive feedb...

2. [TF-05.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/80363228/3b615994-7443-45ba-bb5e-edf6c1ee61ff/TF-05.md?AWSAccessKeyId=ASIA2F3EMEYEYRTPHDBS&Signature=GjhdxpkSbrdjsSthN1inmkOLjH4%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDe4dXHmEkuvp9WxWs4KCv7yFNCy3T7m88xa5IHVaTJVgIgMQOuiJH2zIlO8cvfhaIy4G3oAYoLj%2BP05E2b3RvUoeAq8wQIThABGgw2OTk3NTMzMDk3MDUiDOHlu0Yvlfkf7WAvMCrQBOBXYcDENI%2BFDsTrDKsgk2wK3G8E6XaekUOocHtreu64Q7orBRSdQfKWOoEXR8ZB48il4OZd15Xcx%2Ba%2F8R4tpc0Jo%2FERJmp96fWz4%2FPQ9ulCSyav1wJbAink3jXVC1Q%2BVvnCmk3FWKu3ZPiucplb3QgFZEZm3aQoGEqMUe0cs3P8apqLi3ZZXUdf4buHBAmeTUQLZ5FYk5aImLQhCsa1nWAx7YWZd1c%2FwCkLiOoUmJNYkTdKUaRYJJABQ9tuXlo4RpbfuYuUJ3eqHEKZDozGthlLUzLlZhhEchu%2FB4u99mmnU1JGF3NQRdSc1Pt6lSkMuFVoyGeknrNpwcpaqKcMl6LyeUzrxnHGiyMhU0ddiCcPXyhNqEWeIClA%2Bu%2FzLKP4htlmhaK5ukb%2BVfjQw3BX0ekVTxDoQUzWUp2Rtj8soSfrDu%2BL0Pq5QNl0rzs2AMKtVmJmme52U5yE9GKDtXhVTCp5TtmBMt3h0sV1oWKzSYHCu0hy9vZ2az8D4rg4FDQfJvdBVDVujzYh0WYLexQsNUCBJ%2BZiCUGJ19yV8iG%2BOkytUitAwa%2FGDdn2dhQ17UYiOlZTXR35YAqs87I1IM5tL8bcSRIj3Kg2eF4T08lz6eDttQDf30cRvfIFSsxnWnLJMLYTmSJTICX%2FAFlCe92dziHt3OEp%2FAXn%2BBAUbPYBqt7pPOkFfTnzg5khtySSgVliSi13%2F%2BG0VnD1CVf0Ca8WISxUC%2By8bd2xiplUWmiDcCPpGR3kkMAGae1zZZ2Lg300o%2BINXAXvhXT5%2Fd8zXGjMQv4w%2Fd6JzQY6mAHMZ4XMwgvdqd53y9OjLrFzEExWMch49zjPZ9RsMdpCIdQLA%2FXd9rFqThLwL9U250FoxCCa29UAQNIiVoJVOiFq20F%2Fvjn2MP1KlT2omksN120cxSDauzzJNhdESHFXiyHYK1Rdlds1siXdtTgwQ7%2FJDBM%2BnulOsa%2F9yQDzsUTqALuKVYEbeaMZFDgR4w6ArLOVYrZd97rSiA%3D%3D&Expires=1772257057) - # TF-05: The Mismatch Signal (Derived)

The discrepancy between model prediction and actual observat...

3. [The free energy principle and active inference - Bio-protocol](https://bio-protocol.org/exchange/minidetail?id=20102445&type=30) - The free energy principle (Friston, 2010) is a theoretical framework that proposes that both biologi...

4. [Active Inference: The Free Energy Principle in Mind, Brain, and ...](https://direct.mit.edu/books/oa-monograph/5299/Active-InferenceThe-Free-Energy-Principle-in-Mind) - Active inference is a “first principles” approach to understanding behavior and the brain, framed in...

5. [A tutorial on the free-energy framework for modelling perception and ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC5341759/) - This paper provides an easy to follow tutorial on the free-energy framework for modelling perception...

6. [[PDF] Free Energy: A User's Guide - MPG.PuRe](https://pure.mpg.de/rest/items/item_3388376/component/file_3388381/content) - Active inference, whose most famous tenet is the free en- ergy principle, purports to unify explanat...

7. [Requisite Variety - an overview | ScienceDirect Topics](https://www.sciencedirect.com/topics/computer-science/requisite-variety) - Cybernetics and Second-Order Cybernetics​​ Ashby has called this principle the law of requisite vari...

8. [Good regulator theorem - Wikipedia](https://en.wikipedia.org/wiki/Good_regulator_theorem) - The good regulator theorem is a theorem conceived by Roger C. Conant and W. Ross Ashby that is centr...

9. [[PDF] every good regulator of a system must be a model of that system1](https://pespmc1.vub.ac.be/books/Conant_Ashby.pdf) - Restated somewhat less rigorously, the theorem says that the best regulator of a system is one which...

10. [[PDF] Is the Brain an Organ for Prediction Error Minimization?](https://philsci-archive.pitt.edu/18047/1/Preprint%20Is%20the%20Brain%20an%20Organ%20for%20PEM.pdf) - That is, predictive processing views “prediction-error minimization as the driving force behind lear...

11. [Is prediction error minimization all there is to the mind?](https://philosophyofbrains.com/2014/06/22/is-prediction-error-minimization-all-there-is-to-the-mind.aspx) - The prediction error minimization theory (PEM) says that the brain continually seeks to minimize its...

12. [TF-10.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/80363228/285735b2-02a8-4d35-99c6-f4483dbbf084/TF-10.md?AWSAccessKeyId=ASIA2F3EMEYEYRTPHDBS&Signature=8rzfV7Sjeap%2BoJNeX01VrKpv5kI%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDe4dXHmEkuvp9WxWs4KCv7yFNCy3T7m88xa5IHVaTJVgIgMQOuiJH2zIlO8cvfhaIy4G3oAYoLj%2BP05E2b3RvUoeAq8wQIThABGgw2OTk3NTMzMDk3MDUiDOHlu0Yvlfkf7WAvMCrQBOBXYcDENI%2BFDsTrDKsgk2wK3G8E6XaekUOocHtreu64Q7orBRSdQfKWOoEXR8ZB48il4OZd15Xcx%2Ba%2F8R4tpc0Jo%2FERJmp96fWz4%2FPQ9ulCSyav1wJbAink3jXVC1Q%2BVvnCmk3FWKu3ZPiucplb3QgFZEZm3aQoGEqMUe0cs3P8apqLi3ZZXUdf4buHBAmeTUQLZ5FYk5aImLQhCsa1nWAx7YWZd1c%2FwCkLiOoUmJNYkTdKUaRYJJABQ9tuXlo4RpbfuYuUJ3eqHEKZDozGthlLUzLlZhhEchu%2FB4u99mmnU1JGF3NQRdSc1Pt6lSkMuFVoyGeknrNpwcpaqKcMl6LyeUzrxnHGiyMhU0ddiCcPXyhNqEWeIClA%2Bu%2FzLKP4htlmhaK5ukb%2BVfjQw3BX0ekVTxDoQUzWUp2Rtj8soSfrDu%2BL0Pq5QNl0rzs2AMKtVmJmme52U5yE9GKDtXhVTCp5TtmBMt3h0sV1oWKzSYHCu0hy9vZ2az8D4rg4FDQfJvdBVDVujzYh0WYLexQsNUCBJ%2BZiCUGJ19yV8iG%2BOkytUitAwa%2FGDdn2dhQ17UYiOlZTXR35YAqs87I1IM5tL8bcSRIj3Kg2eF4T08lz6eDttQDf30cRvfIFSsxnWnLJMLYTmSJTICX%2FAFlCe92dziHt3OEp%2FAXn%2BBAUbPYBqt7pPOkFfTnzg5khtySSgVliSi13%2F%2BG0VnD1CVf0Ca8WISxUC%2By8bd2xiplUWmiDcCPpGR3kkMAGae1zZZ2Lg300o%2BINXAXvhXT5%2Fd8zXGjMQv4w%2Fd6JzQY6mAHMZ4XMwgvdqd53y9OjLrFzEExWMch49zjPZ9RsMdpCIdQLA%2FXd9rFqThLwL9U250FoxCCa29UAQNIiVoJVOiFq20F%2Fvjn2MP1KlT2omksN120cxSDauzzJNhdESHFXiyHYK1Rdlds1siXdtTgwQ7%2FJDBM%2BnulOsa%2F9yQDzsUTqALuKVYEbeaMZFDgR4w6ArLOVYrZd97rSiA%3D%3D&Expires=1772257057) - # TF-10: Structural Adaptation (Derived + Empirical)

Incremental model updating (TF-06) adjusts par...

13. [Information bottleneck method - Wikipedia](https://en.wikipedia.org/wiki/Information_bottleneck_method) - The information bottleneck can also be viewed as a rate distortion problem, with a distortion functi...

14. [[PDF] The information bottleneck method - Princeton University](https://www.princeton.edu/~wbialek/our_papers/tishby+al_99.pdf) - Rate distortion theory determines the level of inevitable expected distortion, D, given the desired ...

15. [Appendix-A-Lyapunov.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/80363228/634bc729-6638-4df9-8e3e-b98a3ca3bb71/Appendix-A-Lyapunov.md?AWSAccessKeyId=ASIA2F3EMEYEYRTPHDBS&Signature=E5GuY1evX5PA41kkzTd77jOHwR8%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDe4dXHmEkuvp9WxWs4KCv7yFNCy3T7m88xa5IHVaTJVgIgMQOuiJH2zIlO8cvfhaIy4G3oAYoLj%2BP05E2b3RvUoeAq8wQIThABGgw2OTk3NTMzMDk3MDUiDOHlu0Yvlfkf7WAvMCrQBOBXYcDENI%2BFDsTrDKsgk2wK3G8E6XaekUOocHtreu64Q7orBRSdQfKWOoEXR8ZB48il4OZd15Xcx%2Ba%2F8R4tpc0Jo%2FERJmp96fWz4%2FPQ9ulCSyav1wJbAink3jXVC1Q%2BVvnCmk3FWKu3ZPiucplb3QgFZEZm3aQoGEqMUe0cs3P8apqLi3ZZXUdf4buHBAmeTUQLZ5FYk5aImLQhCsa1nWAx7YWZd1c%2FwCkLiOoUmJNYkTdKUaRYJJABQ9tuXlo4RpbfuYuUJ3eqHEKZDozGthlLUzLlZhhEchu%2FB4u99mmnU1JGF3NQRdSc1Pt6lSkMuFVoyGeknrNpwcpaqKcMl6LyeUzrxnHGiyMhU0ddiCcPXyhNqEWeIClA%2Bu%2FzLKP4htlmhaK5ukb%2BVfjQw3BX0ekVTxDoQUzWUp2Rtj8soSfrDu%2BL0Pq5QNl0rzs2AMKtVmJmme52U5yE9GKDtXhVTCp5TtmBMt3h0sV1oWKzSYHCu0hy9vZ2az8D4rg4FDQfJvdBVDVujzYh0WYLexQsNUCBJ%2BZiCUGJ19yV8iG%2BOkytUitAwa%2FGDdn2dhQ17UYiOlZTXR35YAqs87I1IM5tL8bcSRIj3Kg2eF4T08lz6eDttQDf30cRvfIFSsxnWnLJMLYTmSJTICX%2FAFlCe92dziHt3OEp%2FAXn%2BBAUbPYBqt7pPOkFfTnzg5khtySSgVliSi13%2F%2BG0VnD1CVf0Ca8WISxUC%2By8bd2xiplUWmiDcCPpGR3kkMAGae1zZZ2Lg300o%2BINXAXvhXT5%2Fd8zXGjMQv4w%2Fd6JzQY6mAHMZ4XMwgvdqd53y9OjLrFzEExWMch49zjPZ9RsMdpCIdQLA%2FXd9rFqThLwL9U250FoxCCa29UAQNIiVoJVOiFq20F%2Fvjn2MP1KlT2omksN120cxSDauzzJNhdESHFXiyHYK1Rdlds1siXdtTgwQ7%2FJDBM%2BnulOsa%2F9yQDzsUTqALuKVYEbeaMZFDgR4w6ArLOVYrZd97rSiA%3D%3D&Expires=1772257057) - # Appendix A: Lyapunov Stability Analysis for Adaptive Tempo

**Epistemic status**: The setup and as...

16. [TF-11.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/80363228/792736ee-7a13-48f8-8f60-cb60a0421fdf/TF-11.md?AWSAccessKeyId=ASIA2F3EMEYEYRTPHDBS&Signature=37LaXg%2Bs9Zr0qn5x9bapDWf18Pk%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDe4dXHmEkuvp9WxWs4KCv7yFNCy3T7m88xa5IHVaTJVgIgMQOuiJH2zIlO8cvfhaIy4G3oAYoLj%2BP05E2b3RvUoeAq8wQIThABGgw2OTk3NTMzMDk3MDUiDOHlu0Yvlfkf7WAvMCrQBOBXYcDENI%2BFDsTrDKsgk2wK3G8E6XaekUOocHtreu64Q7orBRSdQfKWOoEXR8ZB48il4OZd15Xcx%2Ba%2F8R4tpc0Jo%2FERJmp96fWz4%2FPQ9ulCSyav1wJbAink3jXVC1Q%2BVvnCmk3FWKu3ZPiucplb3QgFZEZm3aQoGEqMUe0cs3P8apqLi3ZZXUdf4buHBAmeTUQLZ5FYk5aImLQhCsa1nWAx7YWZd1c%2FwCkLiOoUmJNYkTdKUaRYJJABQ9tuXlo4RpbfuYuUJ3eqHEKZDozGthlLUzLlZhhEchu%2FB4u99mmnU1JGF3NQRdSc1Pt6lSkMuFVoyGeknrNpwcpaqKcMl6LyeUzrxnHGiyMhU0ddiCcPXyhNqEWeIClA%2Bu%2FzLKP4htlmhaK5ukb%2BVfjQw3BX0ekVTxDoQUzWUp2Rtj8soSfrDu%2BL0Pq5QNl0rzs2AMKtVmJmme52U5yE9GKDtXhVTCp5TtmBMt3h0sV1oWKzSYHCu0hy9vZ2az8D4rg4FDQfJvdBVDVujzYh0WYLexQsNUCBJ%2BZiCUGJ19yV8iG%2BOkytUitAwa%2FGDdn2dhQ17UYiOlZTXR35YAqs87I1IM5tL8bcSRIj3Kg2eF4T08lz6eDttQDf30cRvfIFSsxnWnLJMLYTmSJTICX%2FAFlCe92dziHt3OEp%2FAXn%2BBAUbPYBqt7pPOkFfTnzg5khtySSgVliSi13%2F%2BG0VnD1CVf0Ca8WISxUC%2By8bd2xiplUWmiDcCPpGR3kkMAGae1zZZ2Lg300o%2BINXAXvhXT5%2Fd8zXGjMQv4w%2Fd6JzQY6mAHMZ4XMwgvdqd53y9OjLrFzEExWMch49zjPZ9RsMdpCIdQLA%2FXd9rFqThLwL9U250FoxCCa29UAQNIiVoJVOiFq20F%2Fvjn2MP1KlT2omksN120cxSDauzzJNhdESHFXiyHYK1Rdlds1siXdtTgwQ7%2FJDBM%2BnulOsa%2F9yQDzsUTqALuKVYEbeaMZFDgR4w6ArLOVYrZd97rSiA%3D%3D&Expires=1772257057) - # TF-11: Temporal Nesting and Adaptive Tempo (Derived + Hypothesis)

Adaptive feedback operates at m...

17. [OODA loop - Wikipedia](https://en.wikipedia.org/wiki/OODA_loop) - The OODA loop is a decision-making model developed by United States Air Force Colonel John Boyd in t...

18. [Reduced-Dimensional Reinforcement Learning Control using ...](https://arxiv.org/abs/2004.14501) - We present a set of model-free, reduced-dimensional reinforcement learning (RL) based optimal contro...

19. [Two-Timescale Stochastic Approximation - Emergent Mind](https://www.emergentmind.com/topics/two-timescale-stochastic-approximation-ttsa) - TTSA is a stochastic optimization method that updates two interdependent sequences on distinct times...

20. [OODA Loop (Observe-Orient-Decide-Act) Explained - Umbrex](https://umbrex.com/resources/frameworks/strategy-frameworks/ooda-loop/) - Is OODA just “move fast”? No. Speed without orientation amplifies errors. OODA balances tempo with q...

21. [The OODA Loop and the Half-Beat - The Strategy Bridge](https://thestrategybridge.org/the-bridge/2020/3/17/the-ooda-loop-and-the-half-beat) - While greater speed is clearly an advantage in combat, viewing the OODA Loop through the lens of fas...

22. [TF-09.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/80363228/6bc167c3-0ce3-49a4-91ca-4cdd1e596e62/TF-09.md?AWSAccessKeyId=ASIA2F3EMEYEYRTPHDBS&Signature=akKGogeq4SyOspJZT%2FKNm2lVTO8%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDe4dXHmEkuvp9WxWs4KCv7yFNCy3T7m88xa5IHVaTJVgIgMQOuiJH2zIlO8cvfhaIy4G3oAYoLj%2BP05E2b3RvUoeAq8wQIThABGgw2OTk3NTMzMDk3MDUiDOHlu0Yvlfkf7WAvMCrQBOBXYcDENI%2BFDsTrDKsgk2wK3G8E6XaekUOocHtreu64Q7orBRSdQfKWOoEXR8ZB48il4OZd15Xcx%2Ba%2F8R4tpc0Jo%2FERJmp96fWz4%2FPQ9ulCSyav1wJbAink3jXVC1Q%2BVvnCmk3FWKu3ZPiucplb3QgFZEZm3aQoGEqMUe0cs3P8apqLi3ZZXUdf4buHBAmeTUQLZ5FYk5aImLQhCsa1nWAx7YWZd1c%2FwCkLiOoUmJNYkTdKUaRYJJABQ9tuXlo4RpbfuYuUJ3eqHEKZDozGthlLUzLlZhhEchu%2FB4u99mmnU1JGF3NQRdSc1Pt6lSkMuFVoyGeknrNpwcpaqKcMl6LyeUzrxnHGiyMhU0ddiCcPXyhNqEWeIClA%2Bu%2FzLKP4htlmhaK5ukb%2BVfjQw3BX0ekVTxDoQUzWUp2Rtj8soSfrDu%2BL0Pq5QNl0rzs2AMKtVmJmme52U5yE9GKDtXhVTCp5TtmBMt3h0sV1oWKzSYHCu0hy9vZ2az8D4rg4FDQfJvdBVDVujzYh0WYLexQsNUCBJ%2BZiCUGJ19yV8iG%2BOkytUitAwa%2FGDdn2dhQ17UYiOlZTXR35YAqs87I1IM5tL8bcSRIj3Kg2eF4T08lz6eDttQDf30cRvfIFSsxnWnLJMLYTmSJTICX%2FAFlCe92dziHt3OEp%2FAXn%2BBAUbPYBqt7pPOkFfTnzg5khtySSgVliSi13%2F%2BG0VnD1CVf0Ca8WISxUC%2By8bd2xiplUWmiDcCPpGR3kkMAGae1zZZ2Lg300o%2BINXAXvhXT5%2Fd8zXGjMQv4w%2Fd6JzQY6mAHMZ4XMwgvdqd53y9OjLrFzEExWMch49zjPZ9RsMdpCIdQLA%2FXd9rFqThLwL9U250FoxCCa29UAQNIiVoJVOiFq20F%2Fvjn2MP1KlT2omksN120cxSDauzzJNhdESHFXiyHYK1Rdlds1siXdtTgwQ7%2FJDBM%2BnulOsa%2F9yQDzsUTqALuKVYEbeaMZFDgR4w6ArLOVYrZd97rSiA%3D%3D&Expires=1772257057) - # TF-09: The Cost of Deliberation (Derived)

Explicit deliberation (TF-07) improves action quality b...

23. [TF-07.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/80363228/872c3699-c33c-4e71-ba53-aaebd1da7a56/TF-07.md?AWSAccessKeyId=ASIA2F3EMEYEYRTPHDBS&Signature=cQHwhxw471Zum9BKQT%2FuZ086uwU%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDe4dXHmEkuvp9WxWs4KCv7yFNCy3T7m88xa5IHVaTJVgIgMQOuiJH2zIlO8cvfhaIy4G3oAYoLj%2BP05E2b3RvUoeAq8wQIThABGgw2OTk3NTMzMDk3MDUiDOHlu0Yvlfkf7WAvMCrQBOBXYcDENI%2BFDsTrDKsgk2wK3G8E6XaekUOocHtreu64Q7orBRSdQfKWOoEXR8ZB48il4OZd15Xcx%2Ba%2F8R4tpc0Jo%2FERJmp96fWz4%2FPQ9ulCSyav1wJbAink3jXVC1Q%2BVvnCmk3FWKu3ZPiucplb3QgFZEZm3aQoGEqMUe0cs3P8apqLi3ZZXUdf4buHBAmeTUQLZ5FYk5aImLQhCsa1nWAx7YWZd1c%2FwCkLiOoUmJNYkTdKUaRYJJABQ9tuXlo4RpbfuYuUJ3eqHEKZDozGthlLUzLlZhhEchu%2FB4u99mmnU1JGF3NQRdSc1Pt6lSkMuFVoyGeknrNpwcpaqKcMl6LyeUzrxnHGiyMhU0ddiCcPXyhNqEWeIClA%2Bu%2FzLKP4htlmhaK5ukb%2BVfjQw3BX0ekVTxDoQUzWUp2Rtj8soSfrDu%2BL0Pq5QNl0rzs2AMKtVmJmme52U5yE9GKDtXhVTCp5TtmBMt3h0sV1oWKzSYHCu0hy9vZ2az8D4rg4FDQfJvdBVDVujzYh0WYLexQsNUCBJ%2BZiCUGJ19yV8iG%2BOkytUitAwa%2FGDdn2dhQ17UYiOlZTXR35YAqs87I1IM5tL8bcSRIj3Kg2eF4T08lz6eDttQDf30cRvfIFSsxnWnLJMLYTmSJTICX%2FAFlCe92dziHt3OEp%2FAXn%2BBAUbPYBqt7pPOkFfTnzg5khtySSgVliSi13%2F%2BG0VnD1CVf0Ca8WISxUC%2By8bd2xiplUWmiDcCPpGR3kkMAGae1zZZ2Lg300o%2BINXAXvhXT5%2Fd8zXGjMQv4w%2Fd6JzQY6mAHMZ4XMwgvdqd53y9OjLrFzEExWMch49zjPZ9RsMdpCIdQLA%2FXd9rFqThLwL9U250FoxCCa29UAQNIiVoJVOiFq20F%2Fvjn2MP1KlT2omksN120cxSDauzzJNhdESHFXiyHYK1Rdlds1siXdtTgwQ7%2FJDBM%2BnulOsa%2F9yQDzsUTqALuKVYEbeaMZFDgR4w6ArLOVYrZd97rSiA%3D%3D&Expires=1772257057) - # TF-07: Action Selection (Derived)

Action selection is a **function of the model**, not a separate...

24. [TF-06.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/80363228/e5ad9912-b06d-47ef-9049-a664c40f409d/TF-06.md?AWSAccessKeyId=ASIA2F3EMEYEYRTPHDBS&Signature=YNGm3CF%2FswpZjy3zV295146svcY%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDe4dXHmEkuvp9WxWs4KCv7yFNCy3T7m88xa5IHVaTJVgIgMQOuiJH2zIlO8cvfhaIy4G3oAYoLj%2BP05E2b3RvUoeAq8wQIThABGgw2OTk3NTMzMDk3MDUiDOHlu0Yvlfkf7WAvMCrQBOBXYcDENI%2BFDsTrDKsgk2wK3G8E6XaekUOocHtreu64Q7orBRSdQfKWOoEXR8ZB48il4OZd15Xcx%2Ba%2F8R4tpc0Jo%2FERJmp96fWz4%2FPQ9ulCSyav1wJbAink3jXVC1Q%2BVvnCmk3FWKu3ZPiucplb3QgFZEZm3aQoGEqMUe0cs3P8apqLi3ZZXUdf4buHBAmeTUQLZ5FYk5aImLQhCsa1nWAx7YWZd1c%2FwCkLiOoUmJNYkTdKUaRYJJABQ9tuXlo4RpbfuYuUJ3eqHEKZDozGthlLUzLlZhhEchu%2FB4u99mmnU1JGF3NQRdSc1Pt6lSkMuFVoyGeknrNpwcpaqKcMl6LyeUzrxnHGiyMhU0ddiCcPXyhNqEWeIClA%2Bu%2FzLKP4htlmhaK5ukb%2BVfjQw3BX0ekVTxDoQUzWUp2Rtj8soSfrDu%2BL0Pq5QNl0rzs2AMKtVmJmme52U5yE9GKDtXhVTCp5TtmBMt3h0sV1oWKzSYHCu0hy9vZ2az8D4rg4FDQfJvdBVDVujzYh0WYLexQsNUCBJ%2BZiCUGJ19yV8iG%2BOkytUitAwa%2FGDdn2dhQ17UYiOlZTXR35YAqs87I1IM5tL8bcSRIj3Kg2eF4T08lz6eDttQDf30cRvfIFSsxnWnLJMLYTmSJTICX%2FAFlCe92dziHt3OEp%2FAXn%2BBAUbPYBqt7pPOkFfTnzg5khtySSgVliSi13%2F%2BG0VnD1CVf0Ca8WISxUC%2By8bd2xiplUWmiDcCPpGR3kkMAGae1zZZ2Lg300o%2BINXAXvhXT5%2Fd8zXGjMQv4w%2Fd6JzQY6mAHMZ4XMwgvdqd53y9OjLrFzEExWMch49zjPZ9RsMdpCIdQLA%2FXd9rFqThLwL9U250FoxCCa29UAQNIiVoJVOiFq20F%2Fvjn2MP1KlT2omksN120cxSDauzzJNhdESHFXiyHYK1Rdlds1siXdtTgwQ7%2FJDBM%2BnulOsa%2F9yQDzsUTqALuKVYEbeaMZFDgR4w6ArLOVYrZd97rSiA%3D%3D&Expires=1772257057) - # TF-06: The Update Gain (Derived + Empirical Claim)

The model incorporates mismatch signals throug...

25. [Pearl's Causal Hierarchy - Emergent Mind](https://www.emergentmind.com/topics/pearl-s-causal-hierarchy-pch) - Pearl's Causal Hierarchy is a structured framework categorizing causal inference into three levels—o...

26. [[PDF] 1On Pearl's Hierarchy and the Foundations of Causal Inference](https://causalai.net/r60.pdf) - The hierarchy consists of three layers (or “rungs”) encoding different concepts: the associational, ...

27. [[PDF] lyapunov-based robust and adaptive control of nonlinear](https://ncr.mae.ufl.edu/dissertations/patre.pdf) - open problem of how to obtain asymptotic stability of nonlinear systems with general sufficiently sm...

28. [[PDF] Active Inference: A Process Theory - Free Energy Principle](https://activeinference.github.io/papers/process_theory.pdf) - This article describes a process theory based on active inference and be- lief propagation. Starting...

