# Running outline

Audit id: 526815
Date: 2026-05-15

## Current scope

Modified de novo audit of AAT only. I have read the audit instructions, top-level `OUTLINE.md`, and `01-aat-core/OUTLINE.md`. I have not read other component outlines and will not do so until AAT segment work is complete, per Joseph's instruction.

Missing AAT outline rows encountered so far: Strategy Dynamics chapter intro `--GAP--`, The Orient Cascade chapter intro `--GAP--`, Composition Machinery chapter intro `--GAP--`, Unity/Communication/Shared Intent chapter intro `--GAP--`, and Strategic Composition and Channel Effects chapter intro `--GAP--` have no source files to read.

## Working report shape

1. Scope and method
   - Modified orientation path.
   - First-hand segment reading in AAT outline order.
   - Per-segment reflections plus diagram artifacts.

2. Findings under burden of proof
   - Dependency graph / outline-order violations.
   - Scope/status mismatches.
   - Math or example verification failures.
   - Cross-segment drift around certificate, directed separation, identifiability floors, and composition.

3. Rescinded candidates
   - Candidate issues that were resolved by later text or Phase-2 triangulation.

4. Coverage statement
   - Exact segments read.
   - Segment files skipped because missing.
   - Math/external citation checks actually performed.
   - Priming limitations from modified protocol.

5. What holds
   - Places where the framework's caveat discipline, proof structure, or scope lattice held under pressure.

6. Hypothesis-tier observations
   - Potential reorganizations or conceptual diagrams that emerged but were not findings.

7. Process feedback
   - Whether the per-segment diagram cadence helped or distorted comprehension.
   - Whether the modified "AAT first, no other outlines" posture created local vocabulary gaps.

## Live finding candidates

F1 candidate - broad adaptive scope includes passive/no-control systems, but `def-agent-environment` requires agents to produce actions that affect `Omega`. `scope-agency`, `post-causal-structure`, and now `def-agent-spectrum` confirm agency as a narrower action-with-effect scope and explicitly keep passive trackers/Bayesian learners in Section I adaptive scope, so F1 is localized to the initial base definition.

F2 candidate - `post-composition-consistency` declares only `scope-agency` as a dependency but embeds detailed downstream composition/contraction machinery (`scope-composite-agent`, `form-composition-closure`, `result-contraction-template`, `der-tempo-composition`, `result-persistence-condition`, etc.) inside Formal Expression and Epistemic Status. Core postulate fits early; derived payload appears out of canonical order.

F3 candidate - `form-information-bottleneck` claims exact applied IB theorem but displays optimization over deterministic-looking `phi`, while the original IB theorem optimizes over conditional encoders `p(tilde{x}|x)` / `p(M|C)`. Fix may be as simple as saying `phi` denotes a stochastic encoder/Markov kernel or scoping to deterministic IB.

F4 soft candidate - `def-model-class-fitness` defines `F(Mclass)` as a class-only ceiling, but `def-model-sufficiency` made `S(M)` policy-, task-, denominator-, and trajectory-relative. This may be inherited implicitly, but structural-adaptation uses should propagate the relativity explicitly.

F5 candidate - `form-event-driven-dynamics` defines event information content as `I(e_tau; Omega_tau | M_{tau^-})` but explains it as realized surprise of a specific event. Mutual information is an expected channel/random-variable quantity; realized event content would usually be pointwise mutual information, surprisal, or posterior information gain such as a KL update.

F6 candidate - `der-recursive-update` declares `deriv-recursive-update` as a dependency even though that proof artifact appears later in the AAT outline, and its discussion imports later consolidation/stability-plasticity machinery. `der-action-selection` repeats the pattern by giving a helpful Section II lift and action-fluency discussion that cite future segments (`form-complete-agent-state`, `der-deliberation-cost`, `result-persistence-condition`, `der-directed-separation`, etc.). `emp-update-gain` and `def-causal-information-yield` continue the pattern with later Fisher/adaptive-gain, unified-policy, communication, adversarial, and Section III references. The local core claims are often derivable from already-read material; proof/downstream payloads are out of outline order.

F7 soft candidate - `def-mismatch-signal` has frontmatter `status: axiomatic` but its epistemic section says the mismatch signal is definitional. This may be taxonomy drift rather than substantive error.

F8 soft candidate - `result-mismatch-decomposition` is exact only under the fresh-noise assumption (GA-1), which is invoked in the derivation and epistemic status but not represented in the segment's declared dependencies. If GA-1 is a global assumption rather than a segment, the dependency/status metadata may need a way to expose it.

F9 candidate - `emp-update-gain` presents `eta*=U_M/(U_M+U_o)` while allowing `U_M` to be "predictive variance or entropy" and `U_o` to be observation noise. The ratio is only dimensionally meaningful when both quantities are expressed in a common uncertainty metric/space (scalar aligned variances, mapped covariances, Fisher curvatures, etc.). The later matrix/natural-gradient discussion partly addresses this, but the headline formula needs the common-metric condition.

F10 candidate - `def-adaptive-tempo` defines tempo as `sum nu^(k) eta^(k)*` and calls it effective rate of useful information acquisition, but `eta` is update gain/correction fraction rather than event information content. Earlier `form-event-driven-dynamics` defined event information content, yet the scalar tempo formula omits any per-event information payload. The formula is dimensionally a quality-adjusted correction-event rate unless a normalized-event or Fisher-information-payload assumption is added.

F11 soft candidate - `hyp-mismatch-dynamics` labels Model D as deterministic bounded disturbance `||w(t)|| <= rho` but derives equality `||delta||_ss = rho/T` by setting the scalar derivative to zero. Equality holds for constant/worst-case aligned disturbance; arbitrary bounded time-varying disturbance gives an ultimate-bound inequality such as `limsup ||delta|| <= rho/T`.

F12 candidate - `der-deliberation-cost` formalizes deliberation benefit as `Delta eta*`, an update-gain improvement, but many stated examples and the action-fluency discussion concern policy/action-value improvements from planning. The segment acknowledges direct action-value benefit is outside the derivation, so the result is valid as epistemic/gain-improving deliberation but narrower than the title/examples imply.

F13 candidate - `der-gain-sector-bridge` derives `alpha = eta* c_min`, while persistence uses `alpha > rho/R` as a correction rate and adaptive tempo is `T = nu eta*`. The bridge omits the event-rate factor unless `F` is already a time-aggregated correction field or `c_min` includes rate. Later prose says `alpha = T` exactly for linear correction, so the per-event vs per-time normalization needs to be explicit.

F14 candidate - `result-sector-condition-stability` states Model S disturbance as `E||w(t)||^2 = sigma_w^2` but gives RMS bound `sigma_w sqrt(n/(2alpha))`. That RMS formula matches isotropic per-coordinate diffusion amplitude `sigma_w`; if `sigma_w^2` is total vector disturbance power, the factor of `sqrt(n)` is not correct. Model S needs a precise SDE/covariance convention.

F15 soft candidate - `result-persistence-condition` per-dimension Model S line uses `eta_k > c*rho_k^2/delta_critical,k^2`, while surrounding persistence formulas use `T_k` or `alpha` as correction rates. This looks like notation drift unless `eta_k` has been redefined as a per-dimension tempo/rate.

F16 soft candidate - `scope-agent-identity` treats chronica/trajectory `C_t` as non-copyable, but earlier chronica notation reads like an ordered event/history record, whose representation can be copied. The non-forkability claim is right for the causal trajectory token, not for a mathematical record of the prefix; the segment should distinguish record from causal token.

F17 candidate - `impl-persistence-and-limits` states that an information-rate floor `dot R >= n alpha/2` nats/time converts via Landauer to roughly `0.35 n alpha k_B T` per unit time. Under the standard convention, Landauer cost is `k_B T` per nat, so `n alpha/2` nats/time gives `0.5 n alpha k_B T` per time. The `0.35` coefficient needs a stated convention or correction.

F18 soft candidate - `form-complete-agent-state` says action is "the single point where epistemic and purposeful states interact," but the segment also defines a general full-state update `f_X(X,e)` and notes between-event dynamics `dot G=g_G(G,M)`. The claim should be narrowed to outward environment coupling or conditioned on directed separation/factorization.

F19 candidate - `der-directed-separation` defines `kappa_processing = I(G_t; M_{tau+} | e_tau, M_{tau-}) / H(G_t | e_tau, M_{tau-})`, but the denominator can be zero when the goal is already determined by the conditioned variables. The diagnostic needs a nonzero-denominator support condition, limiting convention, or fallback to the unnormalized conditional mutual information.

F20 soft candidate - `der-directed-separation` names a bounded-signaling assumption as implicit: goal state reaches the world only through action, with action coarseness limiting goal leakage. This should probably be promoted to an explicit scope assumption because rich behavior can leak goals through timing, style, attention, tool selection, or other side channels even when event processing is nominally separated.

F21 soft candidate - `form-objective-functional` defends `V_{O_t}: trajectories -> R` by saying an acting agent has implicitly scalarized and that choosing `a` over `a'` imposes a total ordering. A choice gives a local preference/selection relation, not by itself a total real-valued ordering over trajectories; the scalar interface is best treated as an explicit scalar-objective or current-timescale-scalarization scope condition.

F22 soft candidate - `disc-continuity-stance` says continuity stance and persistence machinery are formally independent. They are conceptually separable, but `O_t` affects policy/action and therefore event exposure, repair behavior, redundancy, resource allocation, and other variables that can affect actual persistence dynamics. The claim should be softened to "valuation of persistence is distinct from persistence capacity."

F23 candidate - `def-value-object` says that when predictive sufficiency holds and directed separation holds, `Q_O` is causally valid. The `do(a)` query also requires causal/action-transition structure or interventional identifiability in `M_t`; observational predictive sufficiency plus goal-blind epistemic processing does not by itself guarantee valid interventional expectations.

F24 candidate - `def-value-object` claims exact monotonicity `A_O^(1) <= A_O^RH <= A_O^B`. Receding-horizon replanning with shorter horizon `N_r` is not generally guaranteed to outperform current-policy continuation on the full evaluated horizon `N_h`; myopic replanning can be worse unless additional alignment, terminal-value, fallback, or full-horizon comparison assumptions are added.

F25 soft candidate - `def-strategy-dimension` cleanly decomposes `G_t=(O_t,Sigma_t)`, but for reactive controllers and end-to-end learned policies the objective/strategy split may be analyst-ascribed rather than internally represented as separable state. The segment should distinguish literal internal state from functional decomposition.

F26 candidate - `causal-access-intro` frames the adaptive loop as a Level-2 data engine. Executed actions are physical interventions, but logged on-policy action-outcome pairs are not automatically clean samples of `P(o | do(a))` when policy selection depends on latent state that also affects outcomes. The text should separate physical intervention, intervention-character data, and identifiable interventional distribution.

F27 soft candidate - `causal-access-intro` displays the unified policy objective with `lambda(M_t)`, while `def-value-object` just argued the value of exploration should depend on `(M_t, O_t, N_h)`. This may be legacy shorthand, but the intro should either adopt `lambda(M_t,O_t,N_h)` or label the scalar equation as the older heuristic CIY form.

F28 candidate - `def-pearl-causal-hierarchy` says the mismatch signal conditioned on the agent's own action is an interventional signal. Conditioning on an action chosen by a policy is not the same as `do(a)` unless assignment is randomized, adjusted, unconfounded, or otherwise identifiable. This is a sharper instance of the loop-as-Level-2 slippage in F26.

F29 candidate - `der-loop-interventional-access` marks the result exact from temporal ordering and agency scope, but theorem-grade assumptions are only surfaced in Working Notes/cross-reference: positivity, sequential ignorability, and known action mechanism. The formal exact claim should either be narrowed to intervention-character data availability, or those assumptions should be promoted into Formal Expression/Epistemic Status.

F30 soft candidate - `der-loop-interventional-access` often reads as though each `(a_t,o_{t+1})` pair carries interventional information. Agency scope only guarantees at least one action contrast with causal effect; particular actions can be no-ops, effects can be delayed past `t+1`, and exogenous changes can dominate the next observation. CIY may be zero or practically unusable for a specific action/event pair.

F31 candidate - `scope-ciy-observational-proxy` defines an observational proxy using `I(o_t; a_{t-1} | M_{t-1}) - I(o_t; a_{t-1} | Omega_t, M_{t-1})`. If `Omega_t` is the true environment state, this is not generally observable; if it is estimated, the proxy inherits model-error caveats; if it is post-action state, conditioning may block/distort the causal effect.

F32 candidate - `scope-ciy-observational-proxy` Regime A says action variation provides identification for clean interventional estimates. Action variation alone is insufficient when policy-driven action choice depends on state/history that also affects outcomes; Regime A needs randomization, known action mechanism with adjustment, or sequential ignorability plus positivity.

F33 candidate - `disc-ciy-unified-objective` displays the older scalar heuristic `E[value(a)|M_t] + lambda(M_t) CIY_q(a;M_t)` even though `def-value-object` supplies `Q_O` and this segment's own Epistemic Status says the scalar form is superseded by `Q_O(a)+Tr(Lambda I_o(a))`. The segment should clearly separate historical/teaching scalar shorthand from theorem-grade matrix form.

F34 soft candidate - `disc-ciy-unified-objective` table says `lambda` reduces exactly to objects such as the Gittins index and information-directed sampling ratio. These are related exploration/exploitation solution concepts, but not literally scalar weights in an additive `lambda * CIY` objective without a derivation/mapping; "exactly derived" is likely too strong.

F35 soft candidate - `norm-explicit-strategy-condition` contrasts explicit strategy, which inherits model bias, with loop-based learning, which it says does not. Loop learning can still be biased by policy selection, confounding, partial observability, update rules, and model-mediated interpretation. The contrast should be about different bias channels, not bias versus no bias.

F36 soft candidate - `norm-explicit-strategy-condition` grounds the preference for planning in preserving persistence margin, but earlier continuity-stance work says agents differ in how they value persistence. The criterion should be conditioned on objectives for which persistence margin is instrumentally or terminally valuable.

F37 candidate - `impl-causal-access` argues sandbox data is Level 1 because sandbox trajectories are forkable, while deployment data is Level 2 because deployment trajectories are singular. In Pearl-style causal inference, repeatable/forkable experiments can be Level-2 interventional data for the sandbox causal system. The real limitation is transportability/external validity from sandbox SCM to deployment SCM, not a Pearl-level downgrade caused by forkability.

F38 candidate - `impl-causal-access` says Pearl's `do` operator needs AAT's singular non-forkable trajectory commitment. Pearl interventions are normally defined over causal models, populations, or repeatable experimental units; non-forkability is not a prerequisite for `do`. AAT may need singular trajectory for identity/continuity claims, but not for basic interventional semantics.

F39 mostly-resolved candidate - `strategy-structure-intro` says strategy-DAG acyclicity falls out of temporal ordering rather than being chosen. `def-strategy-dag` later states the needed condition explicitly: strategy nodes are time-indexed future event tokens and iterations are unrolled. The concern is localized to summary/intro wording that omits the time-unrolling condition.

F40 soft candidate - `der-chain-confidence-decay` uses "decay" language for the exact chain-rule result. The exact result is monotone non-increase; strict decay requires each added required step to have conditional success probability below 1.

F41 candidate - `scope-and-or` classifies nodes by asking whether removing one parent still allows achievement: YES -> OR, NO -> AND. Threshold structures such as 3-of-5 pass the "remove one" test but are not pure OR because no single parent is sufficient. The classification needs separate necessity/sufficiency/threshold questions.

F42 soft candidate - `scope-and-or` invokes AND/OR Boolean completeness as support for an `O(k)`-parameter representation. Functional completeness does not imply compact representation; arbitrary Boolean functions can require exponentially large AND/OR formulas or many auxiliary nodes. The segment should frame AND/OR as a compact useful fragment, not compact coverage of all Boolean structure.

F43 candidate - `def-strategy-dag` says AND/OR status propagation is correct iff the DAG is causally sufficient, and that causal sufficiency guarantees independent edge outcomes. Causal sufficiency/CMC gives conditional independence and Markov factorization over variables, not the specific noisy-AND/noisy-OR product formulas or independent per-edge contribution model. Correct propagation also requires the local AND/OR parameterization to be true.

F44 soft candidate - `def-strategy-dag` sometimes says causal insufficiency makes `hat P_Sigma` systematically overestimate success. Its own covariance table shows sign depends on topology: positive covariance makes OR estimates optimistic but AND estimates conservative. Blanket overestimation should be limited to OR-dominated redundancy structures.

F45 candidate - `def-control-regret` states `delta_regret >= 0` because the current policy cannot outperform the best in its class. This requires `pi_current in Pi` and identical model, horizon, objective, and continuation convention on both terms; otherwise non-negativity does not follow.

F46 candidate - `impl-strategy-structure` is discussion-grade but presents several proof-bearing claims as chapter-end deliverables while depending on future or meta homes (`deriv-graph-structure-uniqueness`, `der-causal-insufficiency-detection`, `disc-identifiability-floor`, `disc-additive-coordinate-forcing`). This may be acceptable synthesis, but proof credit is deferred rather than locally established.

F47 candidate - `def-strategic-calibration` declares only `def-strategy-dag` and `def-value-object` as dependencies, but its persistence/correction discussion relies on `schema-strategy-persistence`, `deriv-edge-credence-dynamics`, `disc-credit-assignment-boundary`, and `hyp-edge-update-via-gain`. Those should be exposed as forward references or dependency metadata if the discussion remains load-bearing.

F48 candidate - `der-causal-insufficiency-detection` frames on-policy data as Pearl Level 1 and loop/exploration data as supra-Level-1, but AAT actions are physical interventions. The no-go is strongest when framed as fixed-policy regime equivalence plus short-circuit censoring, not as a simple observational-vs-interventional distinction.

F49 candidate - `der-causal-insufficiency-detection` uses a positive covariance alternative hypothesis for causal insufficiency. Positive covariance is a sufficient detector for shared enabling causes, not a necessary signature of all latent common causes; negative/shared-resource latents require a different test.

F50 soft candidate - `der-causal-insufficiency-detection` says joint failure excess localizes common-cause frequency in the L1 construction step. Covariance/joint failures generally underdetermine latent frequency and conditional rates unless strict-prerequisite/single-latent assumptions or extra observations/priors are retained.

F51 candidate - `der-observability-dominance` says an agent should prefer a weak-but-visible path over a strong-but-blind path. This holds for epistemic maintenance/long-run adaptivity, but not necessarily for current objective value; exploitation can rationally favor the blind path when expected value dominates information value.

F52 candidate - `der-observability-dominance` says unobservable regions have no mismatch signal and no reason to revise, but its own two-edge analysis allows terminal plan-level aggregation to reveal plan failure. The stronger claim should be narrowed to no local edge-level mismatch/localization signal.

F53 candidate - `der-observability-dominance` claims observability investment improves `alpha_Sigma` whenever `theta_1 > 1/2` under similarly distributed experience. That threshold is not evident from the displayed formulas and needs an explicit counting convention and comparison baseline.

F54 candidate - `hyp-edge-update-via-gain`'s parallel log-odds presentation appears to conflate log-odds of an edge-truth hypothesis with the logit of a Bernoulli edge success probability/posterior mean. Beta-Bernoulli updating is additive in sufficient statistics, not automatically a scalar `lambda_new=lambda_old+ell(y)` without a specified binary hypothesis/likelihood-ratio model.

F55 candidate - `hyp-edge-update-via-gain` combines `U_edge` as Beta variance in probability space with `U_obs proportional 1/sigma_j` as an observability/noise proxy in `U_edge/(U_edge+U_obs)`. The ratio needs a common metric or should remain explicitly heuristic/structural.

F56 candidate - `hyp-edge-update-via-gain` relies on `disc-credit-assignment-boundary`, `deriv-edge-credence-dynamics`, and `deriv-edge-update-natural-parameter` for theory-level signal resolution, sector results, and coordinate forcing while not declaring them as dependencies. If those claims remain warrant-bearing, they should be exposed as dependencies or forward-proof homes.

F57 candidate - `scope-edge-update-causal-validity` treats action leaves as propositions like "action succeeds" and then says executing the action provides `do(i)`. Execution intervenes on the attempt, not directly on the success proposition; either the leaf variable should denote the attempt event or the estimand should route through `do(attempt a)` plus observed success.

F58 candidate - `scope-edge-update-causal-validity` says outcome attribution is trivially satisfied for single-parent nodes. That only holds under causal sufficiency/isolation; a represented single parent does not rule out unrepresented exogenous causes advancing the child.

F59 soft candidate - `scope-edge-update-causal-validity` presents software as Regime A with `iota approx 1`, but this holds only for well-isolated tests/actions. Flaky tests, shared infrastructure, concurrent changes, hidden dependencies, and environment drift can move software edges into Regime B.

F60 candidate - `disc-credit-assignment-boundary` claims the gradient signal satisfies per-edge directional fidelity for monotone AND/OR DAGs because `J_k >= 0`. A single plan-level residual has one sign; with mixed edge errors, broadcasting that residual through nonnegative `J_k` cannot point every edge toward its own truth. The claim supports plan-level correction or aligned-error cases, not general per-edge fidelity.

F61 candidate - `disc-credit-assignment-boundary` says the log-odds presentation eliminates the probability-space mechanical break, but the update still divides by `||J||^2`. Near-zero gradients can produce arbitrarily large log-odds updates, and zero gradient leaves the expression undefined unless a damping/support condition is added.

F62 candidate - `disc-credit-assignment-boundary` repeats the blanket claim that causal insufficiency makes `hat P_Sigma` systematically overestimate success. Bias direction depends on topology; positive covariance is optimistic for OR redundancy but can be conservative for AND prerequisites.

F63 candidate - `form-structural-change-as-parametric-limit` says adding/removing an edge is a boundary event rather than a discontinuity. This requires an ambient supergraph or hypothesis space where absent edges are represented as zero-weight edges; otherwise graph edits change dimension and are discrete.

F64 candidate - `form-structural-change-as-parametric-limit` includes `gamma` reclassification AND<->OR in the parametric-limit spectrum, but AND/OR semantics are discrete unless supplied with a soft-gate/mixture parameterization.

F65 soft candidate - `form-structural-change-as-parametric-limit` says near-zero edges consume minimal cognitive cost, while later saying each edge consumes representational capacity and evaluation time. Low credence does not reduce memory/evaluation cost unless the cost model is explicitly credence-weighted.

F66 candidate - `def-strategic-tempo` defines `T_Sigma` as a sum and describes it as the effective rate of useful strategy revision, but the persistence-relevant quantity is bottleneck/per-edge. The segment acknowledges this later; the headline should distinguish throughput tempo from persistence-effective tempo.

F67 candidate - `def-strategic-tempo` says Regime-C edges contribute essentially nothing and cannot be improved because they cannot be tested interventionally. Observational evidence can improve associational prediction; what remains weak is interventional causal-efficacy learning.

F68 soft candidate - `def-strategic-tempo` gives `T_Sigma > |E| rho_Sigma/R_Sigma` as a necessary aggregate persistence condition. That assumes homogeneous per-edge thresholds; heterogeneous edges require an aggregate lower bound like `sum_e rho_e/R_e`, while sufficiency stays per-edge/bottleneck.

F69 candidate - `form-strategy-complexity-cost` quantitative table appears wrong for `theta=0.8`, `nu=1`, `n=100`, `rho_Sigma/R_Sigma=0.01`. The displayed condition gives `1/(100+1) < 0.01`, so even `d=1` fails and `d*` should be `0`, not `5`.

F70 candidate - `form-strategy-complexity-cost` defines `C_revise proportional sum nu_ij c_update` but describes it as proportional to strategic tempo times per-update cost. Raw processing cost scales with observation/update opportunities; strategic tempo discounts by gain and identifiability. These are not the same unless cost is per useful correction.

F71 candidate - `form-strategy-complexity-cost` relies on undeclared proof/meta homes (`disc-compression-operations`, `deriv-strategy-cost-regret-bound`) for the strengthened KL-direction and uniqueness story. If these claims remain central, those homes should be explicit dependencies or labelled appendix deferrals.

F72 candidate - `schema-strategy-persistence`'s exact forgetting prerequisite appears convention-dependent. Given the stated discounted update `alpha <- lambda alpha + y`, `beta <- lambda beta + (1-y)`, the steady post-discount-plus-sample count is `1/(1-lambda)`, so the per-observation gain appears to be `1-lambda`, not `(1-lambda)/(2-lambda)`. The hard ceiling `rho >= R/2` depends on the latter convention.

F73 candidate - `schema-strategy-persistence` gives an OR-node minimum exploration condition for the exploratory arm, but the greedy arm also needs enough allocation: `(1-epsilon)/(n_1+1) > rho/R`. The valid epsilon range should have both lower and upper bounds unless the greedy-arm condition is separately guaranteed.

F74 candidate - `form-consolidation-dynamics` states consolidation is well-defined only when `nu_consol << nu_online`. Timescale separation is needed, but useful consolidation also needs enough cadence relative to forgetting and context/event turnover; during offline windows replay update rate can exceed external event rate.

F75 candidate - `form-consolidation-dynamics` claims `I(e_replay | M_tau-) = 0` under state completeness. This holds only when replay is generated from information already inside active `M`; replay buffers, persistent files, chronica stores, and re-read text can be outside active `M` and reintroduce information through an auxiliary memory channel.

F76 candidate - `form-consolidation-dynamics` uses the simplified `(1-lambda) > rho/R` plasticity lower bound from `schema-strategy-persistence`. That lower bound is currently under convention dispute (F72), so the stability-plasticity window inherits the unresolved denominator/update-order issue.

F77 soft candidate - `form-consolidation-dynamics` says all finite-budget agents require consolidation for quality-preserving structural change. The segment's own necessity condition is stronger: `(N1)+(N2)` cross-episode integration plus insufficient per-event budget. Finite budget alone does not rule out incremental online structural adaptation.

F78 candidate - `impl-strategy-dynamics` states the forgetting prerequisite as `(1-lambda) > rho_Sigma/R_Sigma`, reverting to the simplified form despite `schema-strategy-persistence` foregrounding an exact form and despite F72's denominator-convention concern.

F79 candidate - `impl-strategy-dynamics` labels no-go boundary routes S1-S5, but `der-causal-insufficiency-detection` used S1-S5 for no-go scope conditions with different content. This creates reference ambiguity between conditions and escape routes.

F80 candidate - `impl-strategy-dynamics` says joint sibling observability under exploration is available to every AAT agent within agency scope via loop-Level-2 access. The home segment treats joint observability as an additional precondition; loop intervention alone does not guarantee it.

F81 candidate - `impl-strategy-dynamics` repeats the observability-investment claim that instrumentation improves `alpha_Sigma` whenever `theta_1 > 1/2`; this inherits F53's formula concern.

F82 candidate - `impl-strategy-dynamics` says strategic-tempo machinery is verified across "linear chain, balanced tree, unbalanced tree, full DAG with feedback," whereas the local schema segment names different verified cases. If the former list comes from a NeurIPS/proof home, it needs a clear source label.

F83 candidate - `der-orient-cascade` treats `delta_s = hat P_Sigma - Phi` as a default operational calibration signal, but `Phi` is the independence-model plan value at true edge parameters. True edge parameters are not directly available to the agent, so the segment should distinguish proof target from empirical/convergence proxy.

F84 candidate - `der-orient-cascade` step 4c triggers on persistent `delta_s approx 0` plus persistent negative plan residuals. If `delta_s` is not directly computable, 4c needs an observable substitute such as stabilized edge credences plus residual statistics.

F85 candidate - `disc-exploit-explore-deliberate`'s first-order condition omits the derivative of `||delta_post||`. If the mismatch magnitude varies with deliberation time, differentiating `Delta eta*(tau) * ||delta_post(tau)||` requires an additional term.

F86 candidate - `disc-exploit-explore-deliberate` treats control regret as the ceiling on strategic deliberation value. That ceiling is only within the current objective, policy class, model, horizon, and continuation convention; deliberation that expands `Pi` or changes representation can move the ceiling.

F87 soft candidate - `disc-exploit-explore-deliberate` uses `lambda` in qualitative boundary conditions near segments that also use `lambda` for forgetting and exploration pricing. The intended quantity should be named explicitly to avoid symbol collision.

F88 candidate - `impl-orient-cascade` is discussion-grade but presents several proof-bearing claims as if settled by the chapter: survival-imperative exploration, causal-IB LMI structure, bias-bound constants, Section II survival counts, and the scaffolding requirement. These may be supported later, but proof credit should remain with the declared future homes.

F89 candidate - `impl-orient-cascade`'s claim that scaffolded loops are structurally necessary for Class 3 substrates is too broad if read literally. The local argument supports the narrower claim that scaffolding is needed to recover AAT-grade cascade guarantees under coupled representation, attention, memory, and action channels.

F90 candidate - `impl-orient-cascade` says deliberation is "Pearl-do on a simulated trajectory." Pearl's `do` operator is an intervention in an SCM; simulated deliberation is better described as model-internal counterfactual intervention or policy/model simulation.

F91 candidate - `impl-orient-cascade` says deliberation does not relax the bandwidth floor and leaves total Shannon information rate unchanged. Internal computation cannot replace external information indefinitely, but better policies, sensing, compression, and model selection can change effective disturbance, allocation, or required rate.

F92 soft candidate - `impl-orient-cascade` presents the dual exploration laws `lambda_info proportional U_M` and `lambda_surv proportional 1/U_M`, but these depend on future derivation homes. Keep them as a synthesis target until `deriv-causal-ib-exploration` and related segments are read.

F93 candidate - `scope-multi-agent` lets `o_t^{(i)}` depend on other agents' simultaneous actions `a_t^{(\neg i)}`, while each `a_t^{(i)}` is also defined from `X_t^{(i)}`. Without an observe-then-act, act-then-observe, or simultaneous-game information-set convention, the formal time step can create an algebraic/information loop.

F94 soft candidate - `scope-multi-agent` defines goal-blind routing with independence notation such as `c_t^{(j -> i)} perp G_t^c` for a protocol rule. If `c_t` is deterministic infrastructure rather than a random variable, this should be invariance of the selected topology/protocol with respect to the composite goal, or conditional independence for a random routing-selection process.

F95 candidate - `scope-multi-agent` says Section I/II agent-level machinery applies directly to every agent in every multi-agent configuration because each satisfies `scope-agency`. Section I and some agency-scope results do apply broadly, but the outline says Part II's exact results apply to Class 1 separated agents. The sentence should distinguish general agent-level notions from directed-separation-dependent exact results.

F96 soft candidate - `scope-multi-agent` says independence is the special case requiring justification. This is a good default prior for shared environments, but too strong for independent subsystems, weakly coupled modules, or intentionally isolated channels; the claim should be framed as a modeling default rather than a universal burden.

F97 candidate - `scope-composite-agent` repeatedly grounds composite-agent status in a well-defined composite objective `O_c`, but route C-iv explicitly requires no shared objective and defines the macro-state relative to an equilibrium structure `E`. The scope condition should either generalize `G_c` beyond `(O_c, Sigma_c)` or keep strategic composites under a distinct non-`O_c` composition interface.

F98 candidate - `scope-composite-agent` C-iv risks over-admitting ordinary finite games as composite agents. Because mixed Nash and CCE existence/convergence are widely available under broad dynamics, the failure class becomes very small, and "composite agent" can collapse into "multi-agent system with reachable equilibrium support." The segment needs an additional reason why equilibrium support is enough to define composite quantities, not just game-theoretic behavior.

F99 candidate - `scope-composite-agent` C-iii's mutual-benefit route uses a relevance variable `Y` with `E[Y | joint] > E[Y | non-coop]` for each sub-agent, but `Y` is not linked to each agent's objective, utility, or participation constraint. A common variable increasing is not enough for mutual benefit unless it is valued by each agent or mapped into each `O_i`.

F100 soft candidate - `scope-composite-agent` C-i depends on an "appropriate policy divergence" and epsilon-compatibility with `O_c`-optimal policies. Because optimal policies may be nonunique and policy divergence can be behaviorally or distributionally defined, the route should specify the equivalence class or occupancy measure over which compatibility is judged.

F101 candidate - `scope-composite-agent` imports several future proof or framework homes (`def-unity-dimensions`, `result-unity-closure-mapping`, `deriv-strategic-composition`, `disc-identifiability-floor`, `hyp-symbiogenic-composition`) while declaring only three dependencies. Those references are useful discussion scaffolding, but should not count as locally verified support.

F102 candidate - `hyp-symbiogenic-composition` says that after symbiogenesis the endosymbiont persists as a specialized sub-component "not as an independent agent," while `scope-composite-agent` was defined over sub-agents each satisfying `scope-agency`. If autonomy reduction takes the absorbed entity below agency scope, the result is not clearly a composite agent under the preceding segment; it may be a single agent with an internal component.

F103 candidate - `hyp-symbiogenic-composition` lists several examples that do not obviously start with two purposeful agents satisfying `scope-agency`. Adopted vocabulary, grammar, legal precedent, and religious elements can be structures rather than agents with observations/actions/objectives. These are useful analogies, but the formal example class should distinguish agent absorption from structure grafting.

F104 soft candidate - `hyp-symbiogenic-composition` assumes `O_e -> D_e(O_h)` and the integrated objective `O_c approx O_h`. That covers host-dominant absorption, but not cases where the composite objective emerges by mutual transformation of both parties. If "symbiogenesis" is meant broadly, the host-dominance assumption should be explicit.

F105 candidate - `hyp-symbiogenic-composition` uses set union `M_h, Sigma_h union F(M_e, Sigma_e)` across model and strategy structures. The operation needs typed merge/grafting semantics with conflict resolution, interface mapping, and possible overwriting; ordinary union is too weak for integrated state.

F106 soft candidate - `hyp-symbiogenic-composition` says no pre-symbiogenic projection `Lambda` can yield the post-symbiogenic composite because `O_e` changes. A static projection of the pre-state cannot, but a dynamical transition or time-indexed projection could represent the change. The distinction should be state transformation versus fixed projection, not projection impossibility in general.

F107 candidate - `hyp-symbiogenic-composition` imports future composition and appendix homes (`form-composition-closure`, `result-structural-adaptation-necessity`, `result-unity-closure-mapping`, `deriv-critical-mass-composition`, `def-shared-intent`) beyond declared dependencies. The text often labels these as open or conditional, which is good, but proof credit should remain deferred.

F108 candidate - `form-composition-closure` says closure applies to composites satisfying at least one of the three alignment routes, but `scope-composite-agent` now has four routes including C-iv strategic-equilibrium composites. Either closure excludes C-iv, or it needs a version whose macro-state is equilibrium-relative rather than objective-relative.

F109 candidate - `form-composition-closure` A1 requires `X_c=(M_c,G_c)` and the prose says non-scope systems have ill-defined `G_c=(O_c,Sigma_c)`. This inherits the C-iv typing issue: strategic composites do not necessarily have a shared `O_c`, so the closure formalism should state whether it is only for alignment composites or how `G_c` is generalized for strategic composites.

F110 candidate - `form-composition-closure` combines `epsilon_x`, `epsilon_a`, and `epsilon_o` in one norm even though state, action, and observation errors live in different spaces and units. The segment later says norms are load-bearing, but the definition needs scaling/weighting conventions before thresholds like `epsilon* < alpha_c R_c / nu_c` are meaningful.

F111 candidate - `form-composition-closure` evaluates the component defects over true micro-trajectories using true micro observation/action windows. This is a teacher-forced one-step closure test, not a free macro rollout. The bridge lemma can connect this to trajectory error only under the stated contraction assumptions and should also keep action/observation rollout consistency explicit.

F112 candidate - `form-composition-closure` P1 conditions on the aggregate action window over the same macro-step whose observation window is being predicted. If that action window includes within-step actions not available at the macro-boundary, the predictive-information condition is post-hoc rather than decision-time. It needs an information-set convention.

F113 soft candidate - `form-composition-closure` P3 strict dimensionality reduction conflicts with the meta-machine example if the product automaton is counted as exact composition. The product machine is exact but not reductive; it should be classified as exact representation, while closure-as-abstraction requires a smaller minimized machine or another P3-satisfying projection.

F114 candidate - `form-composition-closure` P2 says the Lipschitz projection yields a trajectory-error bound `L * epsilon* / alpha_c`, while the bridge lemma states `epsilon* nu_c / alpha_c`. These may be different measurement conventions, but the text should align them: macro-space tracking error, micro-space lifted error, and rate-scaled disturbance are distinct quantities.

F115 candidate - `form-composition-closure` depends on and imports several future or external proof homes (`deriv-sector-condition`, `result-sector-persistence-template`, `der-temporal-nesting`, `deriv-critical-mass-composition`, `result-contraction-template`, multiple spikes and audits). It is clear about many conditional statuses, but local proof credit should be limited to the formulation and already-read dependencies.

F116 candidate - `der-tempo-composition` defines `C_coord = sum_i T_i - T_c`, then defines realized external tempo as `T_c^ext = T_c - C_coord`. This subtracts coordination overhead twice, giving `sum_i T_i - 2 C_coord` under the definition. If `T_c` is already realized macro-tempo after coordination overhead, external tempo should be `T_c`; if `T_c` is gross composite capacity, then `C_coord` should not be defined as `sum_i T_i - T_c`.

F117 candidate - `der-tempo-composition` treats closure defect both as an added disturbance `rho_eff = rho_ext + epsilon* nu_c` and as a tempo overhead `C_coord >= epsilon* nu_c / ||delta_critical||`. These are equivalent accounting views only if used separately; using both in the same persistence inequality double counts the closure burden.

F118 candidate - `der-tempo-composition`'s displayed "equivalent" composite persistence condition `sum T_i > (rho_ext + epsilon* nu_c)/||delta_critical||` is not equivalent when `C_coord` can exceed its lower bound or when other coordination costs exist. The safer condition is `sum T_i - C_coord > rho_ext/||delta_critical||`, with the closure lower bound giving a sufficient or necessary relaxation depending on direction.

F119 soft candidate - `der-tempo-composition`'s `T_c <= sum_i T_i` needs assumptions about how individual tempos are measured and how information synergy is handled. If individual tempos are measured standalone, fusion or division of labor can create macro correction efficiency not visible in the sum. If measured as within-composite channel capacities, the inequality is more plausible but should be stated.

F120 soft candidate - `der-tempo-composition` says `epsilon*=0` makes every sub-agent correction cycle contribute directly to the macro loop. Exact representability removes closure-defect overhead, but negotiation, synchronization, redundant observations, and nonshared intent can still consume tempo unless the listed equality conditions also hold.

F121 soft candidate - `der-tempo-composition`'s Brooks's Law turning point `Delta epsilon* nu_c / ||delta_critical|| > Delta T_i` assumes `nu_c`, the critical scale, and all non-closure coordination costs remain fixed. This is a useful first-order condition, not a general turning point.

F122 candidate - `hyp-directed-separation-under-composition` Case 1 concludes that individual goal-blind processing plus goal-blind routing implies `f_M^c` is independent of `G_t^c`. That also requires the macro projection/coarse-graining and macro update interface to be goal-blind. A goal-conditioned `Lambda`, goal-conditioned aggregation window, or goal-conditioned macro observation definition can reintroduce coupling even when sub-agent processing and routing are clean.

F123 candidate - `hyp-directed-separation-under-composition` Case 2 treats goal-dependent routing as a directed-separation failure, but some routing changes can be goal-driven event selection or sensing policy, which directed separation explicitly allows at the single-agent level. The segment needs a sharper criterion separating allowed goal-dependent selection of what to observe from forbidden goal-dependent processing/infrastructure that changes how evidence is interpreted or admitted.

F124 candidate - `hyp-directed-separation-under-composition` says a fixed-API multi-agent LLM system can be Case 1 at the composite level even though each LLM agent is individually Class 3. That contradicts the formal setup, which assumes each `A_i` satisfies directed separation individually. This may be a valid wrapper/coercion claim, but it belongs under the wrapper-derived special case, not the general Case 1 hypothesis as stated.

F125 soft candidate - `hyp-directed-separation-under-composition` inherits the earlier `R_t perp G_t^c` issue: for deterministic routing infrastructure, independence notation should be invariance or a random routing-selection condition.

F126 soft candidate - `hyp-directed-separation-under-composition` says most composites of interest are Case 1. This is plausible for some designed systems but overbroad: military task organization, incident response, feature-team formation, and multi-agent AI orchestration often change channels and protocols by mission.

F127 candidate - `der-class-coercion-via-wrapping` C3 and W1 leakage discussion conflate query-content correlation with leakage conditional on the query. If `A` is stateless and `q_M` is fully observed, then `P(A(q_M) | q_M, G_W) = P(A(q_M) | q_M)` holds by construction; pretraining correlations affect outputs as a function of `q_M`, not through an additional dependence on external `G_W` after conditioning on `q_M`. Leakage should be modeled as goal information carried by the query itself, hidden component state, conversation history, or an unobserved context variable.

F128 candidate - `der-class-coercion-via-wrapping` gives the structural leakage bound `kappa_W1 <= I(A(q_M); G_W | q_M)`. Under the exact conditioning used in the theorem, this conditional mutual information is zero for a stateless component. A more useful bound may involve `I(q_M; G_W)`, hidden-state-conditioned leakage, or `I(A(q_M); G_W)` under the wrapper's query distribution.

F129 soft candidate - `der-class-coercion-via-wrapping` calls W2 a refinement within the Class 1 cell, but a single goal-conditioned call whose response is parsed into `M_W` and `G_W` does not satisfy structural directed separation. It is better labeled approximate/behavioral separation, not Class 1 except under an empirical leakage threshold convention.

F130 soft candidate - `der-class-coercion-via-wrapping` uses `X_G = X_O x X_Sigma` per `def-strategy-dimension`, but that segment is not declared as a dependency. If the type signature remains load-bearing, it should be declared or the setup should avoid relying on it.

F131 watch - `der-class-coercion-via-wrapping` C2 excludes stateful/adapting components. That is necessary for the proof but important operationally: many deployed LLM agents have conversation state, tool memory, retrieval state, or adaptive context that can carry goal information outside `q_M`.

F132 candidate - `der-class-coercion-in-composition` says satisfying (A1)-(A4) makes the wrapper a valid AAT composite agent, but `form-composition-closure` also requires `scope-composite-agent` and admissible projections `(P1)-(P3)`. This segment verifies macro-dynamics admissibility, not the full composition-closure criterion.

F133 candidate - `der-class-coercion-in-composition` does not show that a wrapper over one primitive black-box component satisfies `scope-composite-agent`, which was defined over multiple purposeful sub-agents or a route to composite purpose. A wrapped component may be a single agent architecture or tool scaffold rather than a composite agent unless a scope route is supplied.

F134 candidate - `der-class-coercion-in-composition` D-A4 transfers sector behavior from the Tier-1 belief-update map `f_M`, but (A4) in `form-composition-closure` concerns the macro correction dynamics for composite mismatch. Strategy updates, action policy, wrapper scheduling, and component response bias can affect the full closed loop; sector behavior of `f_M` alone is not sufficient without a coupling argument.

F135 candidate - `der-class-coercion-in-composition` decomposes persistence disturbance as `rho_W = rho_ext + rho_int`, with `rho_int` bounded by response variance to goal-blind queries. This omits systematic response bias, leakage, nonstationary component behavior, tool/retrieval state, and wrapper parsing errors. Variance is only one internal disturbance channel.

F136 candidate - `der-class-coercion-in-composition` mixes multiplicative and subtractive tempo accounting. If the wrapper needs `K` component calls per macro-step and the component call rate is `nu_A`, then `nu_W = nu_A/K`; tempo should scale through the reduced event rate before any additional coordination-overhead subtraction. Writing `T_W <= T_A^nominal - C_coord^wrap` needs a definition of `C_coord^wrap` that includes or excludes the `1/K` rate loss.

F137 soft candidate - `der-class-coercion-in-composition` inherits the unresolved double-accounting issues from `der-tempo-composition`, so Brooks's-Law tempo-cost claims should be kept conditional on a cleaned-up tempo ledger.

F138 soft candidate - `der-class-coercion-in-composition` depends on out-of-order proof homes (`deriv-sector-condition`, `result-sector-persistence-template`) and omits `scope-composite-agent` if composite-agent validity remains the title claim.

F139 candidate - `impl-composition-machinery` is discussion-grade but presents the critical-mass closed form, four signed special cases, identifiability-floor Instance 3, and bandwidth inflection claims as settled. These may be supported in `deriv-critical-mass-composition`, `result-sector-persistence-template`, and `disc-identifiability-floor`, but proof credit is deferred until those homes are read.

F140 candidate - `impl-composition-machinery` says `der-class-coercion-in-composition` derives that the wrapped system is a valid AAT composite agent satisfying (A1)-(A4). This inherits F132/F133: A1-A4 macro-dynamics admissibility is not the full `form-composition-closure` criterion, and wrapper composite scope/projection admissibility still need to be shown.

F141 candidate - `impl-composition-machinery` says LLM substrates are constructively in AAT scope and scaffolded loops are structurally non-optional for Class 3 substrates. The local construction supports a conditional wrapper route under component admissibility, leakage bounds, scope/projection gates, and tempo costs; it does not prove necessity for every useful Class 3 deployment.

F142 candidate - `impl-composition-machinery` states `C_coord >= epsilon* nu_c` without the critical-distance normalization introduced in `der-tempo-composition`. As written, the units are wrong: `epsilon* nu_c` is a disturbance rate, not a tempo rate, unless `epsilon*` has already been normalized.

F143 candidate - `impl-composition-machinery`'s Brooks's-Law and bandwidth discussion inherits the double-accounting issues in `der-tempo-composition`. The segment treats closure defect as effective disturbance, tempo overhead, and bandwidth overhead; those need a single ledger before the derived inflection point is reliable.

F144 candidate - `impl-composition-machinery`'s composite-Level-2 escape for coupling-sign identification assumes broad availability of interventions on sub-agents and identifiable responses. Physical intervention access is not enough; the same positivity, adjustment/sequential ignorability, measurement, and transport caveats from earlier causal-access findings apply.

F145 soft candidate - `impl-composition-machinery`'s examples such as Generative Agents as canonical W1, human dual-process systems as W1-style internal scaffolding, and organizations as W1/W2 are useful analogies but need regime diagnostics. A fixed memory step or deliberative layer is not automatically strict W1 unless the belief-update path is structurally goal-blind.

F146 candidate - `def-unity-dimensions` defines epistemic unity as `U_M = I(M1;...;Mn) / H(M1,...,Mn)` and says it equals `1` for identical models. If all `n` variables are identical with entropy `H`, total correlation is `(n-1)H` and joint entropy is `H`, so the ratio is `n-1`, not `1`. The metric needs a different normalization or a capped/rescaled redundancy measure.

F147 candidate - `def-unity-dimensions` defines teleological unity as pairwise correlation of value functions over encountered trajectories. This is distribution- and policy-dependent, can be undefined for zero-variance value functions, and may miss group-level/nontransitive alignment. It needs support, variance, and aggregation conventions.

F148 candidate - `def-unity-dimensions` defines strategic unity as `1 - KL(pi_actual || pi_optimal) / KL(pi_independent || pi_optimal)`. The denominator can be zero, KL can be infinite, and the result can be negative or otherwise leave `[0,1]` without support conditions, smoothing, clipping, or a bounded divergence.

F149 soft candidate - `def-unity-dimensions` describes perceptual unity as the fraction of observation information reaching all sub-agents. Many useful composites rely on complementary private observations plus sufficient routing, not identical broadcast. The metric should distinguish common observation, routed observation, and synergistic private observation.

F150 soft candidate - `def-unity-dimensions` defines `U_f = 1 - d(f_M^1,...,f_M^n)` and says `U_f` ranges from 0 to 1, but the candidate operator/Fisher/IB distances do not automatically share that range or interpretation. The normalization is part of the definition, not a detail.

F151 candidate - `result-unity-closure-mapping` opens by conditioning on `scope-composite-agent` via four routes including C-iv, but the Working Notes say scope is satisfied via "three disjunctive routes" and exclude the strategic-equilibrium route. This repeats the C-iv typing drift and should be made consistent.

F152 candidate - `result-unity-closure-mapping` inherits F146: if `U_M` is not normalized into `[0,1]`, the claimed monotone rate-distortion surface in `U_M` has an unstable axis. Fixing `U_M` is prerequisite to using these formulas quantitatively.

F153 soft candidate - `result-unity-closure-mapping` gives observation closure `epsilon_o^2 = sigma_o^2(1-rho)/2`. Under the standard orthonormal plus/minus projection, discarded residual variance is `sigma_o^2(1-rho)`; the extra `/2` is a per-coordinate or averaging convention that should be stated.

F154 candidate - `result-unity-closure-mapping` first states `epsilon_x=0` for linear-Gaussian micro-dynamics with consistent projections, then clarifies exactness requires the projection range to be invariant under the dynamics matrix. The invariance condition is not optional; consistent projections alone do not imply zero state closure.

F155 soft candidate - `result-unity-closure-mapping` says `Delta K != 0` gives `epsilon_x > 0` even at perfect content correlation. In degenerate perfect-correlation cases the residual bracket can vanish depending on observation/noise structure. The claim should be scoped to nondegenerate correlated-but-not-collapsed cases or state the positivity conditions for `S_- - C_{+-}^2/S_+`.

F156 soft candidate - `result-unity-closure-mapping`'s monotonicity in `U_f` is only as good as the still-open operator-distance definition of `U_f`. For arbitrary update rules, the structural axis is currently a worked-example insight, not a general metric theorem.

F157 candidate - `def-shared-intent` writes the IB optimization as an argmin over representations `G_s`, but standard IB optimizes over an encoder/channel `p(G_s | G_full)`. This repeats the deterministic-encoder ambiguity from `form-information-bottleneck`.

F158 candidate - `def-shared-intent` uses `a_t^coordinated` as the relevance variable, which is too narrow for many coordination problems. Shared intent usually has to support a policy, trajectory distribution, conflict resolution, resource allocation, and replanning, not just one jointly optimal action.

F159 candidate - `def-shared-intent` says high `beta` approaches full model sharing, but the source variable is `G_t^full=(O_t,Sigma_t)`, not the epistemic model `M_t`. It should say full purposeful-state sharing unless `M_t` is added to the source.

F160 candidate - `def-shared-intent` calls shared intent the "minimal sufficient statistic" of the sender's purposeful state for coordinated behavior. The displayed IB objective gives a complexity/relevance optimum for a chosen `beta`; exact minimal sufficiency requires a separate sufficiency constraint or limiting regime.

F161 soft candidate - `def-shared-intent`'s qualitative ordering "purpose before plans before models" is plausible, but not derived from the displayed IB objective without assumptions about entropy, change rate, shelf life, and relevance of each component.

F162 candidate - `hyp-auftragstaktik-principle` states `B_O > B_Sigma > B_M`, confusing priority ordering with total bandwidth allocation. IB reasoning supports sending high marginal-value, long-shelf-life objective bits first; it does not imply the total number of objective bits must exceed strategy or model bits.

F163 candidate - `hyp-auftragstaktik-principle` treats maximizing composite tempo and minimizing coordination overhead as equivalent. Bandwidth allocation can increase aggregate correction capacity, reduce disturbance, or change local autonomy as well as coordination overhead, so the objectives are not generally equivalent.

F164 soft candidate - `hyp-auftragstaktik-principle`'s ordering depends on strong assumptions about entropy, change rates, and local observability. The segment names reversals, but the formal statement should be explicitly marginal and conditional on those rates/costs.

F165 soft candidate - `hyp-auftragstaktik-principle` says Conway's Law is a consequence. Conway's Law says system structure mirrors communication structure; deriving objective-decomposition boundaries from high `B_O` and low `B_Sigma` needs additional organizational/design assumptions.

F166 watch - `hyp-auftragstaktik-principle` inherits the unresolved IB formalization issues from `def-shared-intent`; keep it discussion-grade until the relevance variable and encoder are specified.

F167 candidate - `hyp-communication-gain`'s additive denominator is only optimal under strong common-scale, independent, approximately zero-mean uncertainty assumptions. `U_o`, `U_src`, and especially `U_align` need a precise map onto the same predictive-dispersion units before the ratio can carry Bayesian-gain force.

F168 candidate - `hyp-communication-gain` treats teleological-unity uncertainty as an additive variance term, which under-models strategic deception. Misalignment can change the message policy adversarially as a function of the receiver's trust rule, not merely add noise to an otherwise truthful signal.

F169 soft candidate - estimating `U_src + U_align` from residual variance minus channel noise is fragile. Residuals conflate sender calibration, relationship alignment, receiver model error, task nonstationarity, common shocks, and strategic regime changes; the subtraction can also go negative without a floor or model.

F170 candidate - `hyp-communication-gain`'s distributed-tempo working note adds communication tempo contributions linearly. This repeats the earlier tempo-additivity concern: messages can be redundant, correlated, delayed, costly, or strategically selected, so additive effective tempo needs independence/nonredundancy and cost conditions.

F171 soft candidate - the transitive-trust mixture formula collapses to the prior only if `P_0(s_j)` is explicitly uninformative about `theta_k` and normalized consistently. The scalar reliability `r_ji` also hides domain, calibration, and alignment dimensions that the segment otherwise separates.

F172 watch - risk-asymmetric trust should be tied to an explicit loss function or decision rule. A conservative posterior quantile is plausible for high-impact downside, but it is not implied by Bayesian reliability estimation alone.

F173 candidate - `impl-unity-communication` sometimes promotes caveated component claims into chapter-level predictions. A discussion synthesis can catalog implications, but it should preserve the proof status of unresolved unity metrics, IB encoders, bandwidth ordering, and additive trust gain.

F174 candidate - `impl-unity-communication` says structural monotonicity "survives more broadly" than the linear-Gaussian closure mapping. For arbitrary update rules and projections, monotonicity in `U_f` still needs conditions; the worked Kalman case does not establish the general claim.

F175 soft candidate - the heterogeneous-optimizer ensemble example is suggestive but under-specified. "Same content, different structural unity" needs a metric showing equivalent content while update machinery differs; different optimizers/schedules can also change learned content.

F176 candidate - `impl-unity-communication` repeats `B_O > B_Sigma > B_M`, "most closure-defect reduction comes from a small objective-sharing investment," and Conway's Law as a consequence. These inherit F162-F165 and should remain marginal/conditional, not absolute or derived.

F177 candidate - mapping cooperative coupling `gamma < 0` to `U_align -> 0` and adversarial coupling `gamma > 0` to large `U_align` is too direct. Coupling sign, objective alignment, observed source reliability, and receiver uncertainty about alignment are related but not identical variables.

F178 soft candidate - the risk-asymmetric trust story needs an explicit loss function and evidence model before deriving "high-trust relationships build slowly and break quickly." Conservative quantiles are decision-policy choices, not consequences of the reliability posterior alone.

F179 candidate - the cross-domain prescription that flat trust models systematically trust unreliable sources too much in low-stakes regimes and too little in high-stakes regimes does not follow from the displayed communication-gain formula without a risk/loss layer.

F180 soft candidate - `impl-unity-communication` says the shared-intent priority ordering is structural, not contingent, but also notes regime reversals. The structural claim should be conditional on local observability, change rates, entropy, and communication costs.

F181 watch - `impl-unity-communication` imports later chapter claims (`der-team-persistence`, `der-adversarial-destabilization`, `deriv-strategic-composition`, identifiability-floor instances) as synthesis context. Keep these as forward references until the AAT outline reaches their homes.

F182 resolved locally - `cooperative-adversarial-intro`'s raw disturbance decomposition needed a nonnegative/floor convention; `der-team-persistence` supplies `rho_i^eff = max(rho_i, 0)`. The intro should point to that convention when presenting the raw signed sum.

F183 resolved/formalized - `der-adversarial-destabilization` gives the correct product threshold `T_A > (alpha_B R_B - rho_base)/gamma_A`; the intro should use this product framing rather than "speed" alone.

F184 soft candidate - pulling the squared mismatch ratio into the intro is pedagogically useful, but the formula should keep its assumptions attached every time: deterministic coupling-dominant disturbance, compatible steady-state conventions, and whatever symmetry/baseline conditions the later result requires.

F185 resolved as caveated - `der-adversarial-destabilization` explicitly assumes `gamma_A` increases with `||delta_B||` and marks the effects spiral discussion-grade. Keep the intro's "mathematics of panic" wording tied to that caveat.

F186 clarified/partly resolved - `der-interaction-channel-classification` defines Regime III as below observability floor and contributing to variance without usable update. The intro's "processed until tempo is consumed" wording should be aligned with this: either unobserved ambient variance or low-priority processed overhead, not both without a threshold distinction.

F187 candidate - the three boundaries in `der-interaction-channel-classification` are conceptually distinct, but not independent in the ordinary variable sense because both the model-class and observability tests depend on `I(e)`. The claim should say "orthogonal diagnostic criteria" or state the independence notion.

F188 watch - `cooperative-adversarial-intro` carries strong later claims while declaring no formal claim of its own. Treat it as roadmap language, not as independent support for squared advantage, effects spiral, or recipient-regime taxonomy.

F189 candidate - `der-team-persistence`'s formal persistence condition uses `alpha_i`, while the new multi-agent machinery defines distributed tempo `T_i`. The segment needs an explicit bridge from `T_i` and communication gains to sector correction rate `alpha_i`, inheriting the earlier alpha/tempo normalization issue.

F190 candidate - `der-team-persistence`'s coupling coefficients `gamma_adv` and `gamma_coop` need units and scale conventions. Since `gamma T_j` is added to/subtracted from `rho_i`, `gamma` must convert another agent's tempo into receiver disturbance rate on the same normed mismatch scale.

F191 soft candidate - `der-team-persistence` says a single cooperative event contributes through one channel or the other, not both. That is too categorical for events with both causal and informational effects; the safer rule is causal allocation/no double counting across decomposed effects.

F192 candidate - the coordination threshold `nu_comm eta_ji^* > Delta T_cost` repeats the tempo-as-useful-rate simplification. It lacks per-message information value/relevance, redundancy, latency, and task value terms unless those are folded into `eta` or `nu`.

F193 soft candidate - diminishing returns from accumulating `U_src` and `U_o` across diverse sources is not general. Additional sources can increase noise and overhead, but can also reduce uncertainty through independent corroboration; the sign depends on source dependence and aggregation model.

F194 watch - `der-team-persistence` correctly says the disturbance decomposition is a modeling choice. Downstream theorem-grade uses should cite the decomposition as an assumption, not as something derived from the sector template.

F195 candidate - `der-adversarial-destabilization`'s Model D threshold should explicitly split the already-unstable case. If `alpha_B R_B - rho_base <= 0`, `B` already fails baseline persistence, so the adversarial tempo threshold is vacuous or zero rather than a meaningful positive threshold.

F196 candidate - Model S adds adversarial stochastic coupling as `sigma_B = sigma_base + gamma_A T_A`. For independent stochastic sources, variance/power often combines in quadrature or covariance addition, not amplitude addition; this needs a noise convention.

F197 candidate - `der-adversarial-destabilization`'s Model S scalar threshold inherits the earlier stochastic-sector convention issue around `sigma`, `n`, and covariance units. The file says scalar `n=1`, but downstream multidimensional uses need the full covariance/norm convention.

F198 candidate - "mixed cases are handled by decomposing drift and noise components and applying both bounds additively" needs a combined Lyapunov bound. Deterministic drift and stochastic diffusion do not generally combine by simply adding threshold tests.

F199 soft candidate - the claim that the decoupled analysis is "conservative" should state the beneficiary. Treating `T_A` as exogenous is best-case for the attacker and worst-case for the target, but not conservative for all uses.

F200 candidate - the qualitative opacity formula `gamma_A proportional to 1/H_b(A) * 1/H_b(B)` appears sign-ambiguous. Low target opacity `H_b(B)` plausibly helps `A`, but high adversary opacity `H_b(A)` can also make `A` harder for `B` to anticipate, increasing effective disruption rather than decreasing `gamma_A`.

F201 soft candidate - the effects-spiral text says `gamma_A(||delta_B||)` makes disturbance grow superlinearly and `dot V_B > 0` increasing. That requires conditions on the functional form and current state; monotone `gamma` alone is not enough.

F202 watch - the statement that adversarial/strategic composition lies outside contraction-metric frameworks may be too broad. It is plausible for this asymmetric disturbance model, but saddle/monotone-game dynamics can sometimes be handled with specialized contraction-like tools.

F203 candidate - `der-interaction-channel-classification` again uses mutual information notation `I(e; Omega | M)` for a realized event's information content. That repeats the earlier expected-vs-realized information issue; per-event classification needs pointwise surprise/information gain or an explicit random-variable convention.

F204 candidate - the observability boundary `I(e) * nu^(k) >= U_o,B^(k) * c_floor` is dimensionally unclear. Information rate is being compared to observation noise/uncertainty times a constant; the threshold needs a common detection-statistic scale.

F205 candidate - three binary boundary tests do not by themselves yield only four regimes. The file uses a precedence convention: fail magnitude first => II-a; else fail class => II-b; else fail observability => III; else I. That may be a good coarsening, but it is not "forced" by three independent boundaries.

F206 candidate - the regime-typed `rho_B^eff` formula adds quantities with incompatible units: `||e|| nu`, `floor(M) nu`, `sigma_e^2 nu`, and `iota I(e) nu`. It needs conversion functions into the same mismatch-disturbance-rate units before summation.

F207 candidate - the negative Regime-I term is not always structural. True cooperative information may reduce effective disturbance, but Regime-I-with-adversarial-content later in the same segment shows that an absorbable update can be harmful depending on content and alignment.

F208 soft candidate - the class boundary `F(M_B) * I_max(M_B)` is acknowledged as heuristic. Until replaced by sufficient-statistics span or projection-to-class machinery, II-b is a useful label rather than a quantitative threshold.

F209 candidate - the Kalman Case 1 expression says `s^2/(2r ln 2)` nats. Division by `ln 2` converts natural-log nats to bits; the unit label or formula is inconsistent.

F210 soft candidate - the Kalman worked case sets sector parameter `alpha_B = eta_B^*`. This inherits the earlier concern that update gain is not automatically a time-normalized sector correction rate.

F211 candidate - `der-interaction-channel-classification`'s declared dependencies omit `obs-gated-tempo-advantage`, but boundary (I-c), the boundary table, and recovery section invoke it as a source for the observability boundary.

F212 soft candidate - the claim that `result-adversarial-tempo-advantage` exponent drops toward zero in the high-`U_o` limit because fewer events land in Regime II is plausible but not derived here.

F213 watch - `der-interaction-channel-classification`'s opacity account (`gamma_A^effective = gamma_A^max f(H_b^B)`) is cleaner than the previous `1/H_b(A) * 1/H_b(B)` statement. Track which formulation becomes canonical.

F214 watch - references to spike material and Class-2 degradation (`kappa_processing`) should remain scope notes unless those artifacts are in the audited dependency path.

F215 candidate - `result-adversarial-tempo-advantage` assumes `alpha = T` exactly. This inherits the tempo-to-sector-rate bridge issue from earlier segments; without that bridge the exponent algebra is formally about `alpha` ratios, not raw adaptive tempo ratios.

F216 candidate - `result-adversarial-tempo-advantage`'s Model S inherits the additive-noise-scale assumption `sigma_eff = sigma_base + gamma T`. The `3/2` exponent is exact for that amplitude model, but different stochastic-combination conventions could change prefactors or scaling.

F217 candidate - `result-adversarial-tempo-advantage`'s declared dependencies omit proof sources used in the segment, especially `result-sector-persistence-template` / `deriv-sector-condition` for the steady-state formulas and `def-adaptive-tempo` for scalar tempo.

F218 soft candidate - the non-coupling-dominant stochastic limit is `b -> 1/2`, while the chapter intro's broad prose said the exponent approaches `1`. The intro should distinguish deterministic and stochastic non-coupling limits.

F219 candidate - simulation validation is deferred to `result-adversarial-exponent-regimes`, which is not a declared dependency and has not yet been read in this outline order. Keep simulation-backed statements provisional until that file is reached.

F220 soft candidate - the asymmetric-coupling note says `gamma_A/gamma_B` shifts the ratio without changing the exponent. This is true for constant gammas under the displayed model; it fails if coupling effectiveness depends on tempo, state, opacity, or regime assignment.

F221 watch - the finite-`nu` correction formula in Working Notes references `deriv-discrete-sector-condition` and carries a nontrivial expression. Treat it as appendix/proof-home material unless the dependency path exposes it.

F222 candidate - `impl-cooperative-adversarial` repeats the "canonical catalog home" pattern and should preserve the weakest status of each imported claim. The synthesis uses conditional and discussion-grade pieces from several files plus forward Ch.5 material.

F223 candidate - the repair mapping for magnitude shocks drifts. The classification segment ties II-a to sector radius/capacity and sustained-rate destabilization; `impl-cooperative-adversarial` says magnitude shocks respond to gain investment/lower `U_o`. That may help some cases, but it is not the same repair axis.

F224 candidate - ambient noise is described as contributing "zero" and not calling for response, but `der-interaction-channel-classification` says Regime III contributes to variance and slowly drains reserve. The implication should say filtering or infrastructure response may be appropriate when aggregate ambient load is material.

F225 candidate - the regime-typed effective-disturbance description in `impl-cooperative-adversarial` ("informative updates contribute to ordinary tempo demand; magnitude shocks to peak-load demand; structural shocks to adaptation cadence; ambient noise to zero") no longer matches the displayed `rho_eff` formula in the classification file.

F226 candidate - the claim that cheap noise injection into the defender's observation channel helps the defender against a high-tempo attacker is one-sided. Higher observation noise may gate adversarial events, but it also degrades the defender's real observations, update gain, and ordinary persistence.

F227 soft candidate - "highly-noisy environments produce more cooperative-game-like dynamics" is an unsupported cross-domain claim in `impl-cooperative-adversarial`. It needs a model distinguishing adversarial-channel noise from shared task/environment noise.

F228 candidate - "inside the opponent's loop means `T_A > T_B/k`" is not the threshold delivered by the preceding derivations. The destabilization threshold depends on `gamma_A T_A`, base disturbance, `alpha_B`, and `R_B`; the tempo ratio result depends on coupling-dominant symmetric assumptions.

F229 candidate - the contraction-obstruction section overstates the method boundary. "Contraction-metric machinery cannot handle strategic/adversarial regimes" is too broad unless scoped to the particular attracting-fixed-point/contraction template; specialized contraction/monotone-operator tools may apply in some games.

F230 soft candidate - the passivity claim "adversarial inputs drive any storage function" is too sweeping as written. It needs the specific input/output passivity assumptions and adversarial input class.

F231 soft candidate - "cooperative coupling that is too strong can produce equilibrium-stability failures" is plausible but not derived from this chapter's signed-disturbance model; it belongs with the future equilibrium machinery unless formalized locally.

F232 candidate - the final trust bridge repeats the too-direct mapping from observed cooperative/adversarial coupling to `U_align -> 0` or large. Trust uncertainty should update from evidence under a model; coupling sign is evidence, not identical to alignment certainty.

F233 watch - `deriv-strategic-composition`, Ch.5 exponent regimes, agent opacity, 16-cell targeting, and matrix-Loewner persistence are heavy forward references. Keep them as bridge material until their own AAT segments are read.

F234 candidate - `deriv-strategic-composition`'s potential-game structure alone does not imply the displayed sector inequality `dPhi/dt >= alpha_joint ||grad Phi||^2` or convergence to a selected equilibrium. That needs a dynamic aligned with the potential plus curvature/gradient-domination or local strong stability assumptions.

F235 candidate - "equilibrium stability follows from Phi's role as a joint Lyapunov function" is too broad. Increasing a potential can converge to local maxima, stationary saddles, boundary equilibria, or multiple equilibria depending on geometry and dynamics.

F236 candidate - `deriv-strategic-composition`'s sector-template transfer first sets `xi = gradient-of-potential` and then `xi = pi - pi*`. Those are different state variables unless a local Hessian/strong-convexity relation maps them.

F237 candidate - VI existence is overstated as pure-strategy Nash existence for continuous compact-convex games with continuous payoffs. A VI solution corresponds to Nash under additional differentiability/concavity-in-own-strategy assumptions; continuity alone is not enough.

F238 soft candidate - no-regret convergence to CCE needs finite or otherwise compact action sets, bounded losses/payoffs, and the right information/update protocol. State those assumptions before using the `O(1/sqrt T)` macro-state guarantee.

F239 candidate - `deriv-strategic-composition` uses B1 directional fidelity and `der-gain-sector-bridge` in the alpha-prime proof but does not declare `der-gain-sector-bridge` as a dependency.

F240 soft candidate - "contraction to shared truth is the `U_O = 1` special case" is conceptually useful but too simple. Shared objectives do not by themselves imply a unique shared truth, contraction, or closure-defect zero without the earlier composition and observability conditions.

F241 candidate - the proposed C-iv scope route changes `scope-composite-agent` but is introduced here as a formulation choice. It should be routed back to the scope segment or clearly marked as proposed extension until incorporated.

F242 candidate - the Class-1 sub-agents to Class-2 composite result depends on cross-checking `hyp-directed-separation-under-composition`, which is not declared as a dependency here and is explicitly listed as follow-up.

F243 soft candidate - mechanism-design impossibility and active-inference claims are positioned as adjacent implications, but some prose ("fails here in a derivable way") outruns what this segment derives locally.

F244 watch - the Cournot instantiation appears locally coherent and usefully separates the conceptual zero-sum corner example from the actual sector-template example.

F245 watch - the bridge from strategic composition back to `form-composition-closure` remains open because the macro-description is an equilibrium statistic/distribution rather than a state trajectory.

F246 candidate - `der-agent-opacity`'s `H_b = H(a_{A,t+tau} | F_B^t)` needs an action-space convention. For continuous actions, differential entropy is not coordinate-invariant and can be negative; parameterization-invariance and `H_b^max` normalization require discrete/quantized actions or a reference measure.

F247 candidate - the reduction from `H_b^{A|B}(t,tau)` to Hafez's `H(S,A | S')` under IDT + ergodicity is not "direct substitution" as written. Future-action entropy conditional on an observer filtration and backward state-action entropy conditional on next state are different conditionings unless an explicit time-reversal/observer model equates them.

F248 candidate - calling `H_b` the formal dual of observation quality `U_o` is stronger than shown. They are opposite-direction information quantities, but a mathematical duality needs a shared channel/operator relation or adjoint construction.

F249 soft candidate - cooperative effectiveness decreasing in `H_b` is plausible for coordination, but not universal. An ally can reduce disturbance by acting independently in a delegated region without being action-legible to the receiver at each horizon.

F250 candidate - `T_A^effective = T_A * H_b/H_b^max` makes low-opacity adversarial tempo vanish. Predictable adversarial actions can still impose disturbance; opacity should modulate coupling effectiveness or neutralization probability, not necessarily multiply all adversarial tempo to zero.

F251 candidate - the bilateral opacity ratio `(H_b^{A|B}/H_b^{B|A})^2` can become singular when the denominator is near zero and assumes both agents' opacity enters symmetrically through the same multiplicative channel. It needs floors/saturation and a direction-specific coupling model.

F252 candidate - the emitter-side four-regime classification is a formulation, not a derivation parallel to the recipient regimes. The segment does not yet give boundary inequalities comparable to sector/model/observability tests.

F253 candidate - the 16-cell emitter-recipient "closed-form arg-max" is under-specified. A product of opacity-to-target and vulnerability-to-shock is a plausible score, but closed-form targeting needs edge utilities, constraints, and regime-transition probabilities.

F254 candidate - saying `der-agent-opacity` "closes" the `adversarial-edge-targeting` GAP is too strong unless that GAP is replaced by an actual source segment or formal optimization result.

F255 soft candidate - the claim that Class 3 Coupled agents have high structural opacity is architecture-plausible but not guaranteed; a coupled agent can be externally predictable if policy/output dynamics are simple or heavily instrumented.

F256 watch - Hafez/IDT empirical numbers support monitoring feasibility, not by themselves the AAT claims about Level-2 access, low-`H_b` sidecars, or opacity-sign coupling.

F257 watch - keep attacker opacity `H_b^{A|B}` distinct from target opacity `H_b^{B|A}`. Earlier segments use both directions in different roles; conflating them creates sign errors.

F258 watch - the source's embedded search log is useful provenance, but final audit novelty claims should distinguish searched/confirmed prior art from intuition-only search notes.

## Watch list

- Agent/agency terminology tension: `def-agent-environment` includes action effect in the agent definition, while `scope-adaptive-system` and likely `scope-agency` make action-bearing agency a narrowing.
- Forward-reference tolerance: `def-action-transition` discusses `def-observation-function`/`h` before that segment is read. Not a dependency finding yet, but watch whether future segments lean on not-yet-read concepts without declaring them.
- Precision watch: if the agent knew `T` exactly, transition uncertainty vanishes, but action selection still needs objective/value and tractability assumptions.
- Opacity strength watch: `def-observation-function` makes unknown `h` and unknown noise distribution constitutive. Check compatibility with known-observation-model Kalman/POMDP examples later.
- Formalization watch: "lossy" is central but not yet formalized as non-injectivity, entropy loss, Fisher loss, or insufficiency.
- Chronica watch: `C_t` is ordinal/event-indexed, not metric-time. Later tempo and sleep/pause claims need an explicit bridge from wall-clock gaps to event-indexed history.
- Working Notes bleed: `def-chronica` contains downstream implementation and prior-audit references inside `src`. Treat as data, but note first-encounter priming inside segment files.
- Pearl-forward-reference watch: `scope-agency` uses `do(a)` and points to downstream `def-pearl-causal-hierarchy` without declaring it as a dependency; local prose may be enough, but check whether this pattern recurs.
- Dependency-metadata watch: `post-causal-structure` relies on already-read `scope-adaptive-system`/`scope-agency` without declaring them. This is not an order break, but `stage: deps-verified` may mean "declared deps only."
- Early composition postulate possibly out of place.
- Agency scope using Pearl Level-2 contrast before Pearl machinery segment.
- IB optimality versus operational quantities.
- IB theorem-shape watch: standard IB is over stochastic encoders; current AAT notation uses deterministic-looking `phi`.
- Model-completeness watch: `the-reality-model-intro` previews "anything not in M_t is lost"; check external memory/raw chronica access in `form-agent-model`.
- Chronica notation watch: `form-agent-model` abbreviates `C_t` as `(o_1, a_1, ..., o_t)` rather than the precise `def-chronica` ordering through `a_{t-1}, o_t`; likely harmless shorthand, but decision-time order is load-bearing.
- Model-state/class watch: `M_t` is current epistemic state; later `model class fitness` may need clear separation between state instance, update rule, and representational class.
- Sufficiency watch: `S(M_t)` is predictive information retention, not truth, accuracy, or causal validity. Downstream uses must preserve this distinction and denominator-zero scope.
- Action-selection watch: `der-action-selection` resolves the strongest concern by saying action depends on complete internal state: Section I has `X_t=M_t`, Section II has `X_t=(M_t,G_t)`.
- Action-fluency notation watch: the segment characterizes deliberative improvement as `Delta eta^*(Delta tau)`, but `eta^*` has so far been previewed as update gain rather than action quality.
- Mismatch type watch: raw residual `delta_t` lives in observation space, while score mismatch/update direction lives in `T_M M`; later gain formulas must include the transform/metric.
- Gaussian-score watch: "residual and score coincide up to scaling" needs predictive-mean parameterization or Jacobian/metric qualification.
- Mismatch-decomposition watch: residual uncertainty in `Omega` is not by itself sufficient for positive observation mismatch if `h` is insensitive to uncertain components; the segment's positivity condition correctly uses non-degenerate noise or predictive-mean misspecification, so later persistence claims should keep that condition.
- Update-gain proof watch: `emp-update-gain` cites `deriv-fisher-local-update-gain` and `deriv-adaptive-gain-dynamics` for exactness/opacity resolution without declaring them as dependencies.
- Update-gain scalar/matrix watch: scalar `U_M/(U_M+U_o)` is exact for aligned scalar/direct-observation Kalman-like cases; high-dimensional forms require the gain operator/matrix and observation mapping.
- CIY watch: action distinguishability is model-relative, reference-distribution-relative, and KL-directional; later exploration arguments must not treat it as intrinsic EIG without uncertainty gating.
- Adaptive-tempo scalar watch: the segment explicitly treats scalar tempo as exact only under isotropic/shared-eigenbasis/nonredundant-channel assumptions and gives tensor/matrix-Loewner caveats. Later scalar persistence/adversarial claims must inherit those scope restrictions.
- Mismatch-dynamics dependency watch: `hyp-mismatch-dynamics` declares `deriv-sector-condition`, which has not yet appeared in outline order; it also cites discrete-sector and sector-stability results as proof support.
- Persistence intro watch: the structural-persistence vs task-adequacy split is load-bearing and should be preserved in later domain-transfer claims.
- Sector-region wording watch: intro says below threshold mismatch grows without effective bound "up to R"; later theorem should clarify whether this is escape, lack of guarantee, or a specific growth result.
- Deliberation-cost watch: preserve the distinction between gain-improving epistemic deliberation and action-value/policy deliberation.
- Gain-sector bridge watch: check `result-sector-condition-stability` and proof derivations for whether `alpha` is per-event efficiency, discrete-step contraction, or continuous-time correction rate.
- Sector stability watch: this result correctly uses ultimate-bound language for Model D, resolving the earlier linear-heuristic equality issue if downstream keeps the same phrasing.
- Persistence taxonomy watch: this segment separates structural, task, operational, and continuity senses; downstream claims should state which sense they mean.
- Structural-adaptation diagnostic watch: persistent mismatch is evidence for model-class inadequacy only after accounting for irreducible observation noise, nonstationarity/disturbance, insufficient tempo, and gain miscalibration; systematic residual structure is the key signal.
- Temporal-nesting watch: illustrative timescale ladder should not become a fixed ontology; the real condition is sufficient separation/quasi-steady tracking between adjacent adaptive loops.
- Agent-identity watch: keep model state, copied trajectory record, and singular causal trajectory token distinct.
- Chapter-end implications watch: `impl-persistence-and-limits` is a synthesis segment with future/appendix/cross-component dependencies; do not treat its stronger claims as verified until their home segments are read.
- Complete-state watch: decomposition `X=(M,G)` does not itself imply directed separation; it only makes the separation claim statable.
- Directed-separation watch: keep goal-conditioned event selection distinct from goal-conditioned event processing. The former is allowed in Class 1; the latter is what breaks the factorized update.
- Directed-separation diagnostic watch: behavioral tests must hold `M_{tau-}` fixed while varying `G_t`, or they confound goal conditioning with changed prior epistemic state.
- Objective-functional watch: clarify what kind of `trajectory` is evaluated by `V_O`: world-state path, chronica/action-observation sequence, or complete internal/external trajectory.
- Scalar-objective watch: vector/Pareto extensions may preserve structural ordering, but quantitative diagnostics should degrade unless a scalarization or threshold construction is supplied.
- Continuity-stance watch: five-value taxonomy is discussion-grade and under active reconsideration as tier-gated deployment vocabulary.
- Persistence/stance watch: keep "does this system persist?" distinct from "does the objective care about continuation?", while allowing objective-driven behavior to change persistence capacity.
- Value-object watch: `O_t` is treated as a fixed parameter in `Q_O`, so any downstream claim that `Q_O` depends only on `M_t` must retain the qualification "holding objective, continuation policy, and horizon fixed."
- Convention-hierarchy watch: diagnostics computed under C1/C2/C3 are not directly comparable unless the convention is included in the measurement label.
- Strategy-dimension watch: table's "objective external, strategy internal" update-source row should remain typical/provenance language, not a structural restriction, because self-actuated agents can revise objectives.
- Strategy-resource watch: commitment state, action costs, capacity constraints, and strategy compression are open rather than modeled.
- Causal-access watch: the intro is discussion-grade and carries no formal claim, but it seeds several proof-bearing claims; later segments must preserve the data-character vs identification-quality distinction.
- Positive-confound watch: durable false confidence under confounded wins requires on-policy sampling plus insufficient disconfirming interventions; later theorem/norm segments should state those conditions.
- Pearl-hierarchy watch: imported hierarchy itself is fine; AAT-specific claims should say whether they mean Level-2 availability, Level-2 exploitation, or identified Level-2 estimation.
- Software-counterfactual watch: `git checkout` can strengthen Level-3 access, but "ground-truth verification" remains mediated by tests/specs/environment determinism.
- Learning-agent-scope watch: `der-causal-hierarchy-requirement` says all remaining Section II results operate within learning-agent scope unless noted; track later examples of pre-compiled controllers/thermostats.
- Hafez/IDT watch: 2026 citation existence and headline numbers spot-checked via arXiv/search metadata, but the empirical result supports coupling-monitoring performance, not identified interventional access by itself.
- Loop-interventional-access watch: this segment is strongest when phrased as availability of intervention-character data, not clean identification or guaranteed positive information per action.
- Sequential-ignorability watch: the NeurIPS cross-reference names positivity, sequential ignorability, and known action mechanism; check whether AAT's own segment set formalizes these conditions locally.
- CIY-proxy watch: proxy is a different sign-indefinite diagnostic quantity, not a decision-safe approximation of canonical CIY.
- Regime-boundary watch: A/B/C are domain/action-space properties, but their technical boundary should track identifiability assumptions, not just whether actions vary.
- Unified-objective watch: scalar CIY objective is heuristic and vulnerable to directionally irrelevant information; exact claims appear to depend on a future matrix-LMI derivation.
- Exploration-pricing watch: `lambda` sometimes appears as `lambda(M_t)`, sometimes as depending on `(M_t,O_t,N_h)`, and sometimes as a PSD matrix `Lambda`; final audit should separate these layers.
- Explicit-strategy watch: static cost inequality only applies under comparable outcomes and common risk-adjusted cost units.
- Normative-dependency watch: explicit-strategy condition grounds itself in `result-persistence-condition` but does not declare it as dependency.
- Sandbox-ceiling watch: a defensible claim is about transport assumptions and deployment monitoring, not sandbox interventions being Level 1 by virtue of forkability.
- Cross-artifact watch: NeurIPS C1/C2/C3 formalization is doing load-bearing work but has not been read as part of AAT segment order.
- Strategy-DAG watch: exactness of acyclicity/Markov factorization depends on event-token time-unrolling and causal sufficiency; correlation hierarchy must handle the insufficiency case.
- Diagnostic-split watch: satisfaction gap/control regret are model-, policy-class-, horizon-, and convention-relative through `A_O`.
- Chain-confidence watch: `p^n` and `p^(k*d)` are illustrative independent/uniform cases; exact downstream claims need conditional/correlation-aware form.
- Adaptive-plan watch: static chain success differs from replanning, retry loops, and adaptive fallback policies.
- AND/OR watch: probability formulas assume separable parent/path contributions; correlation hierarchy must qualify shared-cause cases.
- Threshold-strategy watch: k-of-n structures are common and can become verbose under nested AND/OR despite bounded-cognition motivation.
- Strategy-DAG exactness watch: separate causal sufficiency/CMC, local AND/OR parameterization, edge-identification regime, and correlation hierarchy; they are different layers of warrant.
- Single-root watch: scalar-objective root works under current scalarization; vector/Pareto objectives need workaround or extension.
- Chapter-synthesis watch: `impl-strategy-structure` has the best local formulation of theorem-backed structure vs convergent parameterization, but imports later proof homes for graph uniqueness, causal insufficiency detection, identifiability floors, and coordinate forcing.
- Strategic-calibration watch: edge-level localization requires execution fidelity and credit assignment; otherwise the residual is an aggregate strategy alarm, not a targeted edge diagnosis.
- Causal-insufficiency watch: exact no-go is shallow/strict-prerequisite under S1-S5; broader DAG claims should retain robust-qualitative status until topology-specific constructions are supplied.
- Covariance-detector watch: joint sibling covariance is a powerful route when joint observability and stationarity hold, but it is sign/model-class specific and not a universal detector of all causal insufficiency.
- Observability-dominance watch: path observability and multiplicative confidence adjustment are first-order summaries; formal quantitative claims should route through the edge-credence dynamics proof home.
- Edge-update watch: keep Beta-Bernoulli exact gain, structural uncertainty-ratio principle, and log-odds coordinate forcing as separate layers.
- Edge-causal-validity watch: distinguish intervention-character data from identified edge estimates, and distinguish action attempts from action-success propositions.
- Credit-assignment watch: plan-level persistence, per-edge diagnostics, and exact attribution are three different levels; default gradient attribution should not be promoted past its level.
- Structural-change watch: continuity claims are representation-relative; edge pruning/grafting need an ambient zero-weight supergraph, while node/gate changes need separate embeddings.
- Strategic-tempo watch: distinguish sum/throughput, average, and bottleneck/min; downstream persistence claims should use the bottleneck.
- Strategy-complexity watch: depth bounds are sensitive to strict inequality and first-edge feasibility; numerical tables need boundary checks.
- Strategy-persistence watch: finite-gain/forgetting prerequisite is important, but exact threshold depends on discounting update order and gain denominator convention.
- Consolidation watch: distinguish internal replay from auxiliary-memory replay; zero-information claims are relative to what is included in active complete state.
- Strategy-dynamics synthesis watch: chapter-end maps should not upgrade deferred appendix claims or unresolved local caveats into settled local results.
- Orient-cascade watch: distinguish exact dependency order from conditional diagnostic content, thresholds, and computable estimators.
- Exploit/explore/deliberate watch: additive deliberation benefit is a linearization; thresholds need to state which variables are held fixed during differentiation.
- Multi-agent timing watch: same-index observations depending on same-index actions need an observe/act information-set convention.
- Composite-scope route watch: downstream Section III claims need to state whether they apply to alignment composites, strategic composites, or both.
- Symbiogenesis type watch: distinguish absorbing an agent into a component, forming a hierarchical composite of still-agentive sub-agents, and grafting non-agentic structure.
- Composition-closure watch: distinguish teacher-forced one-step closure from free macro rollout, and keep state/action/observation norm weighting explicit.
- Tempo-composition watch: keep closure-defect-as-disturbance and closure-defect-as-tempo-overhead as alternative ledgers, not simultaneous charges.
- Directed-separation-under-composition watch: add macro projection/update goal-blindness as a third gate alongside sub-agent processing and routing.
- Wrapping-leakage watch: separate leakage through query content, hidden component state/context, and behavioral noncompliance; conditioning on exact `q_M` blocks ordinary query-content correlation.
- Class-coercion-in-composition watch: distinguish macro-dynamics admissibility from full composition closure, which also needs scope and projection admissibility.
- Composition-machinery synthesis watch: preserve representability-vs-optimality, but route critical-mass, bandwidth, identifiability, and truthification payoffs through their proof homes.
- Unity-metric watch: content/structure split is useful, but metric normalization and support conventions must be fixed before quantitative use.
- Unity-closure watch: rate-distortion framing is useful, but exact claims need linear-Gaussian, norm, projection-invariance, and scope-route conditions.
- Shared-intent watch: use a stochastic IB encoder and a richer coordination relevance variable before making sufficiency claims.
- Auftragstaktik watch: formulate as marginal value-per-bit priority, not absolute bandwidth bucket inequality.
- Communication-gain watch: distinguish variance-like channel/source uncertainty from strategic alignment uncertainty before using a single additive trust denominator.
- Unity/communication synthesis watch: chapter-end implications should preserve the weakest dependency status of each claim rather than promoting local hypotheses into global predictions.
- Signed-coupling watch: keep communication-tempo gains, cooperative disturbance reduction, and adversarial disturbance amplification on separate ledgers with nonnegative effective-disturbance conventions.
- Team-persistence watch: distributed tempo must be converted into sector correction rate `alpha_i` before persistence inequalities can use it quantitatively.
- Adversarial-destabilization watch: base threshold is conditional and clean; Model S, mixed drift/noise, opacity, and effects spiral need separate assumptions.
- Interaction-classification watch: preserve the diagnostic value of the four regimes while requiring a common disturbance-rate unit ledger for aggregation.
- Tempo-advantage watch: exponent algebra is clean under the displayed model; do not detach it from `alpha=T`, exogenous tempo, coupling-dominance, and noise-combination assumptions.
- Cooperative/adversarial synthesis watch: keep the chapter map, but route operational prescriptions back through the qualified source segments.
- Strategic-composition watch: alpha-prime sector transfer needs curvature/monotonicity beyond potential existence; beta-prime gives distributional, not pointwise, macro-state.
- Agent-opacity watch: action entropy, normalization, and directionality are load-bearing; do not collapse all opacity effects into one scalar multiplier.
- Satisfaction-gap watch: inherits convention hierarchy from `def-value-object`; C2 monotonicity concern remains active.
- Attainability watch: `A_O` is a supremum over policy class, not necessarily an attained maximum.
- Control-regret watch: `delta_regret approx 0` is tolerance-relative and will depend on approximation error in estimating both `A_O` and the current-policy value.
- Event-time watch: `form-event-driven-dynamics` uses nondecreasing `tau_i`, allowing simultaneous events, but no tie-breaking/batching convention yet.
- Tempo additivity watch: `nu_eff=sum_k nu^(k) eta^(k)*` assumes usable additive channel contributions; check later for redundancy, correlation, costs, saturation, and delayed action-completion handling.
- Recursive-update watch: the result is mostly definitional Markovization by complete state. Check whether later text treats it as empirical/substantive beyond that scope.
- Between-event dynamics watch: `dM/dtau=g_M(M_tau)` is autonomous; check whether later delayed actions, scheduled goals, or elapsed-time-dependent decay require explicit time/input state.
- Gain-sector bridge demoting alpha from postulate to property: check exact assumptions.
- Directed separation scope propagation through Part II.
- Chain-confidence independence assumptions.
- Wrapper/class-coercion leakage distinction.
- Superlinear adversarial tempo assumptions.
- Appendix/meta-pattern material functioning as proof kernel rather than appendix.
