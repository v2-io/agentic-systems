# Adversarial tempo and panic novelty memo

##### [**Undermind**](https://undermind.ai)

---


## Table of Contents

- [Adversarial tempo and panic novelty memo](#adversarial-tempo-and-panic-novelty-memo)
  - [Overall judgment](#overall-judgment)
  - [Claim under review](#claim-under-review)
  - [Prior art by claim component](#prior-art-by-claim-component)
  - [What the prior art already establishes](#what-the-prior-art-already-establishes)
  - [Where AAT seems genuinely new](#where-aat-seems-genuinely-new)
  - [Stress tests that matter most](#stress-tests-that-matter-most)
    - [The exponent story is the main technical pressure point](#the-exponent-story-is-the-main-technical-pressure-point)
    - [The signed-coupling unification must do real work](#the-signed-coupling-unification-must-do-real-work)
    - [The effects spiral must be more than a suggestive cartoon](#the-effects-spiral-must-be-more-than-a-suggestive-cartoon)
    - [The opacity story should not overclaim duality](#the-opacity-story-should-not-overclaim-duality)
    - [The four-regime taxonomy must earn its complexity](#the-four-regime-taxonomy-must-earn-its-complexity)
  - [Largest implications if the claim holds](#largest-implications-if-the-claim-holds)
  - [Bottom line](#bottom-line)
  - [Potential field impact if the claim holds](#potential-field-impact-if-the-claim-holds)
  - [Venue strategy](#venue-strategy)
    - [Best-fit venues by framing](#best-fit-venues-by-framing)
    - [Recommended path](#recommended-path)
    - [Practical ranking for this project](#practical-ranking-for-this-project)
  - [References](#references)

# Adversarial tempo and panic novelty memo

## Overall judgment

The literature already contains strong antecedents for most of the ingredients behind AAT’s adversarial-tempo story, but they are spread across several fairly separate traditions. Delayed-information differential games and control under communication constraints show that lag, bandwidth, and real-time information flow sharply affect whether a controller or pursuer can keep up with an opponent or plant \[Shi99b, Shi00, Tat04b, Nai04, Sah06, Kho16, Yu20c\]. Tracking and adaptive-filter results show that mismatch against drift is governed by finite adaptation bandwidth, with explicit nontrivial scaling laws under nonstationarity \[Wid76, Wid84, Guo94, Kuh97, Lju90\]. Overload and stress literatures separately show threshold effects and self-reinforcing degradation once workload outruns compensatory capacity \[Han89, Hoc97b, Hub16\]. Stealth and perception-attack work then adds the observability side: adversarial success depends on what the defender can estimate, detect, or distinguish from noise \[Bai17b, Sui20, Hua21c, Kha22\].

What does not appear to be already present in the project literature is the full AAT package suggested by AAT-chapter-13 and AAT-chapter-14:

- cooperation and adversariality as the same coupling law with opposite signs
- a closed-form adversarial tempo advantage with explicit exponent regimes, especially the squared and three-halves scaling stories
- a reserve-depletion account in which crossing the stability boundary triggers an effects spiral rather than merely a larger steady-state error
- a unified bridge from delay and bandwidth limits to overload, opacity, and typed adversarial shocks

That package looks like the real novelty opportunity. The search results are favorable to a strong synthesis claim and moderately favorable to a theorem-shaped novelty claim. The most ambitious parts are not the broad idea that tempo matters in conflict, but the exact exponent story, the signed-coupling unification, and the formal effects spiral.

## Claim under review

In the project files, the claim is stronger than the familiar slogan that getting inside an opponent’s loop is good.

AAT-chapter-13 formalizes cooperative and adversarial interaction through the same disturbance decomposition. Allies reduce effective disturbance or improve update tempo. Adversaries increase effective disturbance through coupling terms proportional to their tempo. On that basis the chapter derives destabilization thresholds, superlinear adversarial tempo advantage, and an effects spiral in which pushing an opponent past reserve can make their subsequent behavior more erratic and more exploitable.

AAT-chapter-14 extends the picture by adding observer-side and emitter-side structure. Recipient-side interactions are classified into informative updates, magnitude shocks, structural shocks, and ambient erosion. The same chapter also introduces opacity as a dual quantity to observation quality and links adversarial advantage to the product of tempo and opacity.

Read together, the project is not just saying that faster actors tend to win. It is saying that adversarial tempo is a specific closed-loop coupling phenomenon. Speed matters twice: it improves one’s own correction and it drives the opponent’s disturbance. Beyond a threshold, this can flip from a stable tracking problem into a self-reinforcing collapse regime.

## Prior art by claim component

| AAT component | Nearest prior art | Match | Novelty read |
|:---|:---|---:|:---|
| Delay and loop speed create exploitable adversarial disadvantage | \[Shi99b\], \[Shi00\], \[Tat04b\], \[Nai04\], \[Sah06\], \[Kho16\], \[Yu20c\] | Strong | Low novelty by itself |
| Tracking error is governed by finite adaptation bandwidth under drift | \[Wid76\], \[Wid84\], \[Guo94\], \[Kuh97\], \[Lju90\] | Strong | Low novelty by itself |
| Overload can become self-reinforcing and cascade | \[Han89\], \[Hoc97b\], \[Hub16\] | Strong | Low to moderate novelty by itself |
| Stealth and attack success depend on observability and detector limits | \[Bai17b\], \[Sui20\], \[Hua21c\], \[Kha22\], \[Kho18g\] | Strong | Low novelty by itself |
| Cooperation and adversariality as the same signed coupling law | nearby analogies in synchronization and command models \[Kal12, Zup20, Ahe21\] | Partial | Moderate to high novelty |
| Explicit superlinear tempo exponents for adversarial mismatch ratios | only partial ancestry from tracking and delayed control \[Kuh97, Yu20c\] | Weak to partial | High potential novelty |
| Effects spiral linking reserve breach to growing exploitability or predictability | overload and stress give partial ancestry \[Han89, Hoc97b, Hub16\] | Partial | High potential novelty |
| Unified four-regime attack taxonomy tied to recipient limits | partial ancestry in stealth, detectability, and model-mismatch literatures \[Bai17b, Sui20, Kha22\] | Weak | High potential novelty |

## What the prior art already establishes

The strongest foundation for the raw tempo claim comes from delayed-information games and communication-constrained control. \[Shi99b\] studies a pursuit-evasion game in which the pursuer has delayed information about the evader and shows that the value of the delayed-information game is never zero. \[Shi00\] continues the same line by treating compensation for imperfect information as a control problem in its own right. These are direct ancestors of the claim that lagged observation is exploitable in adversarial dynamics.

The control and information-theory side makes the threshold structure much sharper. \[Tat04b\], \[Nai04\], and especially \[Sah06\] show that stabilization over constrained channels requires sufficient real-time information flow, not merely enough asymptotic Shannon capacity. \[Sah06\] is especially important because it gives a necessity-and-sufficiency style result: for an unstable scalar plant, stabilization requires channel support that outruns the plant’s own exponential divergence, with the key threshold set by the unstable growth rate. That is a very strong precedent for the broad idea that adversarial or environmental tempo can outrun correction. \[Kho16\] adds a closely related point: timing itself carries information, but delay makes that timing information stale, producing a phase transition in the transmission rate needed for stabilization. \[Yu20c\] brings the same family of ideas into competitive control with delayed imperfect information and shows that delay can drive worst-case performance losses exponentially in unstable systems. Those papers do not prove AAT’s signed-coupling or exponent story, but they do make clear that loop speed and stale information are not just engineering details. They can change the qualitative regime.

The tracking literature provides the nearest mathematical ancestry for the claim that finite adaptive bandwidth yields nonlinear tempo effects. \[Wid76\], \[Wid84\], \[Guo94\], and \[Lju90\] establish the classic lag-noise tradeoff in tracking nonstationary targets. \[Kuh97\] is the most directly useful result in the search set because it proves upper bounds on generalization error under random drift, including a $`\gamma^{2/3}`$-type scaling for conservative trackers and linear-in-$`\gamma`$ scaling for nonconservative ones. That is not the same as AAT’s squared or three-halves exponents, but it is real prior art for nontrivial scaling of error against adaptive mismatch rather than a merely linear intuition.

The overload and stress line gives the best ancestry for panic and effects-spiral behavior. \[Han89\] and \[Hoc97b\] frame performance under stress as a compensatory process with limited energetic reserve. \[Hub16\] is even closer to the project language. It models decision teams with a nonlinear workload-accuracy curve and a positive feedback loop in which errors create more requests, which create more errors, eventually producing abrupt collapse. Importantly, the collapse is not just monotone degradation. The workload-accuracy map has a soft threshold, and a gain on incorrect-message propagation determines whether the organization stays in a stable regime or enters a cascading one. This is strong prior art for a thresholded self-reinforcing degradation story, even though it is written for organizations rather than for a general agency theorem.

The observability and opacity side is also well represented. \[Hua21c\] formalizes pursuit-evasion with strategic information acquisition and concealment, making information gathering itself a costly and exposing act. \[Bai17b\] proves a general detectability-performance tradeoff for data-injection attacks using KL-based stealth definitions, showing how much damage can be done under a given stealth budget. \[Sui20\] characterizes when stealthy and strictly stealthy attacks can drive estimation bias unbounded through output-nulling and zero-dynamics structure. \[Kha22\] is especially relevant to the AAT framing because it studies perception-based control systems and proves that attack success depends on estimation quality, stealth constraints, and what the defender can extract from perceptual channels.

Taken together, these literatures already establish four things quite well:

- lag and bandwidth limits create hard performance and stability thresholds
- finite adaptive bandwidth makes tracking error grow against drift and uncertainty, sometimes with nontrivial exponents
- overload can become a positive feedback process rather than a smooth degradation
- adversarial success depends on sensing, concealment, and detectability limits

What they do not already establish is one closed-form architecture that puts all four in the same signed-coupling frame.

## Where AAT seems genuinely new

AAT looks strongest where it turns several adjacent mechanisms into one dynamical picture.

A useful way to phrase the comparison is this:

- the delay and control papers show thresholded inability to keep up
- the tracking papers show nontrivial scaling under drift
- the overload papers show self-reinforcing collapse
- the stealth papers show that observability and concealment shape attack efficacy
- AAT’s candidate novelty is to make these all consequences of one signed disturbance-coupling picture with explicit reserve and exponent structure

That bundled move is stronger than any single ingredient on its own.

First, the project treats cooperation and adversariality as the same coupling law with opposite signs. That is stronger than merely observing that some interactions help and others hurt. The disturbance decomposition in AAT-chapter-13 uses one mathematical template and changes the sign on the coupling term. There are suggestive precedents in synchronized-oscillator and command models \[Kal12, Zup20, Ahe21\], but I do not see the same signed-coupling move worked out across tempo, reserve, and destabilization in the retrieved literature.

Second, the explicit exponent regime claim is a real novelty candidate. The literature supports threshold and scaling behavior, but the specific AAT claim that adversarial mismatch ratios scale like a squared tempo ratio under deterministic drift and like a three-halves power under stochastic coupling is much sharper than the usual OODA or bandwidth-limited-control rhetoric. The closest retrieved ancestry is the general family of tracking and delay-scaling results \[Kuh97, Yu20c\], not an already matching theorem.

Third, the effects spiral is stronger than standard overload talk if it really links reserve breach to increased adversarial leverage. \[Hub16\] clearly gives a self-reinforcing degradation loop, and the stress literature supports limited compensatory reserve \[Han89, Hoc97b\]. But AAT is making a more specific claim: degradation does not only worsen performance, it changes the coupling environment so that the adversary’s future tempo or opacity becomes more effective. That is a stronger dynamical mechanism than plain overload.

Fourth, the project’s recipient-side attack taxonomy looks materially new. The distinction among informative updates, magnitude shocks, structural shocks, and ambient erosion is not just a list of attack types. It is a claim that the right repair path depends on which boundary has failed: sector-region capacity, model-class capacity, or observability floor. I do not see this exact four-way decomposition already stated in the retrieved papers.

Fifth, the opacity move in AAT-chapter-14 is not merely another stealth variable. The project treats opacity as the dual of observation quality and then lets it modulate tempo advantage. \[Hua21c\], \[Bai17b\], \[Sui20\], and \[Kha22\] provide strong neighboring ideas, but not this exact dual-quantity packaging.

## Stress tests that matter most

### The exponent story is the main technical pressure point

This is where the memo either becomes a serious novelty claim or shrinks back toward synthesis. The literature already shows thresholds, scaling, and delay penalties. The distinctive question is whether the $`b = 2`$ and $`b = 3/2`$ laws are genuinely new consequences of AAT’s disturbance models, or whether they can be reduced to known tracking and stabilization scalings under another notation.

Right now the search supports the weaker but still useful claim that there is strong prior art for nonlinear scaling, but not an already obvious match to these exact exponents. That is good terrain for AAT, but also the place where a mathematically literate reviewer will push hardest.

### The signed-coupling unification must do real work

AAT cannot get much credit merely for saying that help and harm are opposites. The signed decomposition matters only if it lets one derive common persistence conditions, common reserve logic, or common tempo accounting for cooperative and adversarial cases. If that unification is only verbal, the novelty falls sharply.

### The effects spiral must be more than a suggestive cartoon

The overload literature already knows positive feedback and cascading collapse \[Hub16\]. AAT’s stronger claim is that crossing reserve changes the opponent’s exploitability in a way that accelerates further destabilization. That mechanism needs either a clear theorem or a disciplined schematic tied tightly to the earlier equations. Otherwise it will read as an intuitive military metaphor rather than a new result.

The clean comparison point is this: \[Hub16\] already gives error-generated workload that feeds back into more error. AAT needs to show the stronger adversarial version, where degradation changes the coupling term itself, not only the victim’s internal performance curve.

### The opacity story should not overclaim duality

There is good prior art on concealment, exposure, stealth, and detectability \[Hua21c, Bai17b, Sui20, Kha22\]. AAT should therefore claim novelty carefully here. The strongest defensible claim is not that the field lacked any formal opacity notion, but that AAT integrates opacity into the same disturbance-and-tempo machinery as its observation-side constructs.

### The four-regime taxonomy must earn its complexity

A four-way classification is only useful if it changes what one predicts or how one intervenes. If magnitude shocks call for more reserve, structural shocks call for a new model class, and ambient erosion calls for observability improvements, then the taxonomy is analytically useful. If not, it may look like a relabeling exercise.

## Largest implications if the claim holds

| Area | Why the claim matters | Closest literature it would move beyond |
|:---|:---|:---|
| Adversarial control and cyber-physical security | It would connect delay, stealth, overload, and reserve into one dynamical picture | \[Tat04b\], \[Sah06\], \[Bai17b\], \[Sui20\], \[Kha22\] |
| Military and command theory | It would give OODA-style tempo claims a more explicit threshold and instability mathematics | \[Shi99b\], \[Shi00\], \[Boy87\], \[Hub16\] |
| Agent safety under conflict | It would explain why degradation can become self-amplifying rather than merely additive | \[Han89\], \[Hoc97b\], \[Hub16\] |
| Multi-agent theory inside AAT | It would link signed coupling, opacity, and strategic interaction to the same reserve logic | \[Hua21c\], \[Yu20c\], \[Ahe21\] |

The biggest direct effect would likely be on adversarial control and agent-systems analysis. The memo suggests a cleaner vocabulary for a question people already care about but rarely formalize well: when does being faster help linearly, and when does it help superlinearly because it both improves one’s own correction and worsens the opponent’s disturbance?

The second major effect would be on failure analysis. The project implies that collapse under attack is often not a one-step threshold but a regime shift in which the victim’s own degraded state feeds back into the attacker’s coupling advantage. That would be a useful bridge between control, human-factors overload, and adversarial AI.

The third effect would be on evaluation. If recipient-side shocks really separate into informative, magnitude, structural, and erosion regimes, then resilience work can ask a sharper diagnostic question than “was the system attacked.” It can ask which boundary failed.

## Bottom line

The weak version of this memo is not novel. The field already knows that lagged information is exploitable, that control under rate and timing limits has sharp thresholds, that tracking under drift is bandwidth-limited, that overload can self-reinforce, and that stealth depends on observability and detectability \[Shi99b, Sah06, Kho16, Kuh97, Hub16, Bai17b, Kha22\].

The strong version does look novel. AAT’s most promising claim is not that tempo matters in conflict, but the stronger architectural thesis that cooperative and adversarial interaction are one signed coupling law, that tempo advantage can therefore compound superlinearly in explicit exponent regimes, and that reserve breach can trigger an effects spiral in which degradation increases future exploitability.

The cleanest sharpened read is:

- the threshold part has strong prior art
- the nonlinear-scaling part has partial prior art
- the self-reinforcing-collapse part has partial prior art
- the exact signed-coupling plus exponent-regime plus effects-spiral package still looks novel

A strong one-line framing is this:

AAT’s novelty is not the observation that faster actors often outperform slower ones, but the stronger claim that adversarial tempo is a signed closed-loop coupling phenomenon with explicit exponent regimes and a threshold beyond which failure becomes self-reinforcing.

## Potential field impact if the claim holds

The impact ceiling is high because the paper would unify several things that currently live in different conversations.

At the modest end, the paper would still matter as a strong synthesis. It would connect delayed differential games, communication-constrained control, adaptive tracking, overload theory, and stealthy attack analysis under one shared question about tempo, reserve, and exploitability.

At the stronger end, the paper could change how people talk about competitive advantage in adaptive systems. Instead of using tempo as a metaphor or an engineering intuition, it would treat tempo as a mathematically structured coupling variable whose effect depends on disturbance type, reserve, and observability.

The biggest direct effect would likely be on adversarial agent analysis and cyber-physical security. The memo suggests that some attack advantages are not best understood as larger shocks, but as faster disturbance injection into an opponent with finite adaptive reserve.

The next major effect would be on organizational and human-AI command settings. If overload and panic can be tied to the same reserve logic as adversarial disturbance, then some familiar command doctrines become interpretable as reserve-protection mechanisms rather than only as historical heuristics.

The third effect would be internal to AAT itself. This topic is one of the places where the theory could look most externally legible, because it gives concrete comparative claims and not only framework language.

A practical impact ranking would be:

- moderate impact if the paper is received as a disciplined synthesis of known ingredients
- high impact if the exponent regimes and effects spiral are seen as technically new and useful
- very high impact if later work starts using signed coupling and reserve breach as standard language for adversarial adaptive systems

## Venue strategy

### Best-fit venues by framing

The right venue depends on what kind of paper this becomes.

If the paper is framed as a broad AI theory contribution about adversarial agency, adaptive reserve, and multi-agent dynamics, [Artificial Intelligence journal](https://www.sciencedirect.com/journal/artificial-intelligence) is likely the strongest single home. Its scope is broad enough to fit planning, multi-agent systems, reasoning under uncertainty, and general architectural theory.

If the paper is sharpened into a control-theoretic result about delay, observability, and adversarial destabilization, the [IEEE Conference on Decision and Control](https://cdc2025.ieeecss.org/authors/call-for-papers) is a strong conference audience. CDC presents itself as the flagship conference of the control community and is the most natural place for a compact version centered on thresholds, tracking, and closed-loop instability.

If the paper is framed as a general agency and AGI theory result, the [AGI Conference](https://agi-conference.org/call-for-papers) is also a good fit. It is especially suitable if the signed-coupling and reserve story is presented as part of a larger theory of agency rather than only as a control result.

If the paper is framed as a learning-theoretic or analytical study of adaptive intelligent systems under adversarial dynamics, [TMLR](https://www.jmlr.org/tmlr/) is plausible. TMLR explicitly invites theoretical studies, analytical frameworks, and work on the behavior of learning in intelligent systems, but the fit is best if the paper leans into learning dynamics rather than mostly into military or command language.

### Recommended path

The cleanest publication strategy is:

1.  Write the full cross-literature version for Artificial Intelligence journal.
2.  If the most convincing core is the control-and-threshold theorem, prepare a tighter conference cut for CDC.
3.  If the broader agency framing is central, develop a companion or alternative version for AGI.
4.  If the learning-dynamics angle becomes technically dominant, prepare a more compressed version for TMLR.

### Practical ranking for this project

My venue ranking for this exact project is:

- Artificial Intelligence journal
- IEEE Conference on Decision and Control
- AGI Conference
- TMLR

The fork is simple:

- if the main claim is “this is a general theory of adversarial adaptive dynamics,” favor Artificial Intelligence journal or AGI
- if the main claim is “this is a control-theoretic threshold result about delay, rate, and destabilization,” favor CDC
- if the main claim is “this is an analytical result about learning dynamics under adversarial pressure,” favor TMLR

---

## References

\[Shi99b\] J. Shinar and V. Glizer, “Solution of a delayed Information Linear Pursuit-Evasion Game with Bounded Controls,” *IGTR*, vol. 1, pp. 197–217, Sep. 1999, doi: [10.1142/S0219198999000153](https://doi.org/10.1142/S0219198999000153).

\[Shi00\] J. Shinar, T. Shima, and V. Glizer, “On the Compensation of Imperfect Information in Dynamic Games,” *IGTR*, vol. 2, pp. 229–248, Jun. 2000, doi: [10.1142/S0219198900000160](https://doi.org/10.1142/S0219198900000160).

\[Tat04b\] S. Tatikonda and S. Mitter, “Control under communication constraints,” *IEEE Transactions on Automatic Control*, vol. 49, pp. 1056–1068, Jul. 2004, doi: [10.1109/TAC.2004.831187](https://doi.org/10.1109/TAC.2004.831187).

\[Nai04\] G. Nair and R. Evans, “Stabilizability of Stochastic Linear Systems with Finite Feedback Data Rates,” *SIAM J. Control. Optim.*, vol. 43, pp. 413–436, Feb. 2004, doi: [10.1137/S0363012902402116](https://doi.org/10.1137/S0363012902402116).

\[Sah06\] A. Sahai and S. Mitter, “The Necessity and Sufficiency of Anytime Capacity for Stabilization of a Linear System Over a Noisy Communication Link&#8212;Part I: Scalar Systems,” *IEEE Transactions on Information Theory*, vol. 52, pp. 3369–3395, Jan. 2006, doi: [10.1109/TIT.2006.878169](https://doi.org/10.1109/TIT.2006.878169).

\[Kho16\] M. J. Khojasteh, P. Tallapragada, J. Cortés, and M. Franceschetti, “The Value of Timing Information in Event-Triggered Control,” *IEEE Transactions on Automatic Control*, vol. 65, pp. 925–940, Sep. 2016, doi: [10.1109/TAC.2019.2919107](https://doi.org/10.1109/TAC.2019.2919107).

\[Yu20c\] C. Yu, G. Shi, S.-J. Chung, Y. Yue, and A. Wierman, “Competitive Control with Delayed Imperfect Information,” *2022 American Control Conference (ACC)*, pp. 2604–2610, Oct. 2020, doi: [10.23919/ACC53348.2022.9867421](https://doi.org/10.23919/ACC53348.2022.9867421).

\[Wid76\] B. Widrow, J. Mccool, M. Larimore, and C. Johnson, “Stationary and nonstationary learning characteristics of the LMS adaptive filter,” Aug. 01, 1976. doi: [10.1007/978-94-010-1223-2_23](https://doi.org/10.1007/978-94-010-1223-2_23).

\[Wid84\] B. Widrow and E. Walach, “On the statistical efficiency of the LMS algorithm with nonstationary inputs,” *IEEE Trans. Inf. Theory*, vol. 30, pp. 211–221, May 1984, doi: [10.1109/TIT.1984.1056892](https://doi.org/10.1109/TIT.1984.1056892).

\[Guo94\] L. Guo and L. Ljung, “Performance analysis of general tracking algorithms,” *Proceedings of 1994 33rd IEEE Conference on Decision and Control*, vol. 3, pp. 2851–2855 vol.3, Dec. 1994, doi: [10.1109/CDC.1994.411366](https://doi.org/10.1109/CDC.1994.411366).

\[Kuh97\] A. Kuh, “Comparison of tracking algorithms for single layer threshold networks in the presence of random drift,” *IEEE Trans. Signal Process.*, vol. 45, pp. 640–649, Mar. 1997, doi: [10.1109/78.558480](https://doi.org/10.1109/78.558480).

\[Lju90\] L. Ljung and S. Gunnarsson, “Adaptation and tracking in system identification - A survey,” *Autom.*, vol. 26, pp. 7–21, Mar. 1990, doi: [10.1016/0005-1098(90)90154-A](https://doi.org/10.1016/0005-1098(90)90154-A).

\[Han89\] P. A. Hancock and J. Warm, “A Dynamic Model of Stress and Sustained Attention,” *Human Factors: The Journal of Human Factors and Ergonomics Society*, vol. 31, pp. 519–537, Oct. 1989, doi: [10.1177/001872088903100503](https://doi.org/10.1177/001872088903100503).

\[Hoc97b\] G. R. J. Hockey, “Compensatory control in the regulation of human performance under stress and high workload; a cognitive-energetical framework.” *Biological psychology*, vol. 45 1–3, pp. 73–93, Mar. 1997, doi: [10.1016/S0301-0511(96)05223-4](https://doi.org/10.1016/S0301-0511(96)05223-4).

\[Hub16\] P. Hubbard, A. Kott, and M. Martin, “Inducing and Mitigating a Self-Reinforcing Degradation in Decision-making Teams,” *ArXiv*, vol. abs/1607.08139, Jul. 2016.

\[Bai17b\] C.-Z. Bai, F. Pasqualetti, and V. Gupta, “Data-injection attacks in stochastic control systems: Detectability and performance tradeoffs,” *ArXiv*, vol. abs/1704.00748, Apr. 2017, doi: [10.1016/j.automatica.2017.04.047](https://doi.org/10.1016/j.automatica.2017.04.047).

\[Sui20\] T. Sui, Y. Mo, D. Marelli, X. Sun, and M. Fu, “The Vulnerability of Cyber-Physical System Under Stealthy Attacks,” *IEEE Transactions on Automatic Control*, vol. 66, pp. 637–650, Feb. 2020, doi: [10.1109/TAC.2020.2987307](https://doi.org/10.1109/TAC.2020.2987307).

\[Hua21c\] Y. Huang and Q. Zhu, “A Pursuit-Evasion Differential Game with Strategic Information Acquisition,” *ArXiv*, vol. abs/2102.05469, Feb. 2021.

\[Kha22\] A. Khazraei, H. Pfister, and M. Pajic, “Attacks on Perception-Based Control Systems: Modeling and Fundamental Limits,” *IEEE Transactions on Automatic Control*, vol. 69, pp. 7726–7741, Jun. 2022, doi: [10.1109/TAC.2024.3401022](https://doi.org/10.1109/TAC.2024.3401022).

\[Kho18g\] M. J. Khojasteh, A. Khina, M. Franceschetti, and T. Javidi, “Learning-Based Attacks in Cyber-Physical Systems,” *IEEE Transactions on Control of Network Systems*, vol. 8, pp. 437–449, Sep. 2018, doi: [10.1109/TCNS.2020.3028035](https://doi.org/10.1109/TCNS.2020.3028035).

\[Kal12\] A. Kalloniatis, “On the ‘Boyd-Kuramoto Model’: Emergence in a Mathematical Model for Adversary C2 Systems,” 2012.

\[Zup20\] M. Zuparic, M. Angelova, Y. Zhu, and A. Kalloniatis, “Adversarial decision strategies in multiple network phased oscillators: The Blue-Green-Red Kuramoto-Sakaguchi model,” *Commun. Nonlinear Sci. Numer. Simul.*, vol. 95, p. 105642, Nov. 2020, doi: [10.1016/j.cnsns.2020.105642](https://doi.org/10.1016/j.cnsns.2020.105642).

\[Ahe21\] R. Ahern, M. Zuparic, K. Hoek, and A. Kalloniatis, “Unifying warfighting functions in mathematical modelling: combat, manoeuvre, and C2,” *Journal of the Operational Research Society*, vol. 73, pp. 2009–2027, Dec. 2021, doi: [10.1080/01605682.2021.1956379](https://doi.org/10.1080/01605682.2021.1956379).

\[Boy87\] C. A. R. Boyd, G. Hammond, C. LeMay, T. K. Dacus, and N. O. Looney, “A Discourse on Winning and Losing,” 1987.
