# Initial predictions

Audit id: 526815
Date: 2026-05-15
Orientation actually read: `doc/de-novo-audit-instructions.md`, top-level `OUTLINE.md`, and `01-aat-core/OUTLINE.md`.

Priming / deviation note: Joseph explicitly modified the protocol: read only the full/top-level outline and then the AAT outline, start directly at `01-aat-core/OUTLINE.md` rather than README or top-level orientation files, and do not read the other component outlines until AAT segments are done. I therefore did not read `README-auditor.md`, `LEXICON.md`, `NOTATION.md`, `FORMAT.md`, CLAUDE/project top-level files, prior audits, spikes, live tracking, or the other component outlines.

## Topology as I understand it

AAT is the mathematical core and is arranged as a progression from bare agent-environment coupling, through compressed epistemic state, dynamic mismatch correction, persistence conditions, purposeful state, strategy/causal access, and finally composition. The top-level picture in the outline says the spine is not simply "adaptive feedback loop" but "existence and behavior of a stability certificate": the theory asks when some metric/certificate exists, when that metric is forced, where it goes blind, and what projection/composition does to its guarantee.

The dependency story appears to be row-order linearized within AAT, with Appendix A serving two roles: proof/detail backstops for earlier mainline claims and late meta-pattern synthesis. I expect the row order to be mostly coherent in Part I and more strained in Part II/III because many late appendix/meta-pattern segments seem to support claims already announced in prefaces and chapter-end implications. The canonicalization target I will watch first is whether mainline segments depend on appendix proofs, which is allowed only under the appendix-back-pointer convention, or on future non-appendix segments, which would be a critical dependency-order finding.

## Component-level predictions

Part I should establish the minimum ontology: boundary, action transition, observation loss/noise, history, adaptive scope, agency scope, and causal-structure postulates. I expect the first few definitions to be mostly scope-setting rather than mathematically risky. The likely defects are hidden overbreadth: e.g. "environment" or "agent" definitions smuggling purpose into the adaptive-system layer, or `scope-agency` relying on Level-2 causal contrast before Pearl machinery has been imported in Part II.

The reality-model chapter should convert chronica into compressed model state, then introduce information bottleneck language and sufficiency/fitness. I expect a possible tension between generic information bottleneck optimality and operational measurability: the framework may use IB as a clean conceptual primitive while later segments require specific Fisher/KL/Lyapunov quantities. I will watch whether "optimal compression" is formulated as a definition, an idealization, or an empirical claim.

The cycle-in-motion chapter should derive the update recursion from history completeness, action as a function of model/state, mismatch as prediction error, decomposition into model error and observation noise, update gain, causal information yield, adaptive tempo, and mismatch ODE. The likely math-risk zone starts at `result-mismatch-decomposition`, `emp-update-gain`, and `hyp-mismatch-dynamics`: decomposition can be tautological unless assumptions on noise/model error are clear; optimal gain can silently assume Gaussian/quadratic structure; ODE language can overclaim from discrete event updates.

The persistence chapter should connect deliberation cost, gain-sector bridge, Lyapunov sector stability, bounded mismatch, structural adaptation necessity, timescale nesting, and identity. My strongest prior is that real findings, if any, will cluster around scope labels here: sector conditions are legitimate but can be accidentally treated as derived from gain rather than requiring directional fidelity and disturbance bounds. `result-persistence-condition` and `result-sector-condition-stability` are load-bearing enough that I expect careful caveats; if they are absent or only in notes, that is report-worthy.

Part II should lift from adaptive tracking to purposeful state: objective `O_t`, strategy `Σ_t`, value object conventions, and directed separation. The outline itself says Part II exactness depends on Class 1 separated architecture while Class 3 coupled agents only get survival/approximation results. I predict drift risk: some Part II segments may still read as universal over purposeful agents despite the preface's scope lattice. `der-directed-separation` is likely load-bearing and should be status-checked aggressively.

The causal-access chapter should import Pearl/Bareinboim hierarchy and argue that planning requires Level-2 causal access, with feedback loops as interventional data engines. I expect a possible distinction problem between "has acted and observed consequences" and "has identifiable causal effects"; the outline already gestures at CIY/EIG honesty and observational proxies, so a good version will separate data character from identification quality.

The strategy-structure chapter should build a probabilistic DAG, confidence decay, AND/OR scope, satisfaction gap, and control regret. I predict `der-chain-confidence-decay` will be a good early test of additive-coordinate forcing: if log-confidence additivity is derived only under independence assumptions, later correlated-failure machinery must not treat it as unconditional. I will watch for independence assumptions being named in formal expressions rather than only in discussion.

The strategy-dynamics chapter looks fertile for findings because many entries are draft and conceptually dense: strategic calibration, latent common-cause detection, observability dominance, edge-update via gain, structural change as parametric limit, strategic tempo, complexity cost, strategy persistence, and consolidation. I expect some claims to be honestly hypothesis/formulation grade; a finding would be a status mismatch where a draft/hypothesis segment is used downstream as if exact.

The orient-cascade chapter should derive resolution order by information dependency and then split exploit/explore/deliberate. I predict the cascade will be strong where the system is separated and brittle where the observation/model/goal path is coupled. I will watch whether the chapter explicitly requires both directed separation and learning-agent scope, as the AAT preface says.

Part III should turn scale-invariance into closure defect and composition. I expect the composition postulate appears very early in Part I but is only made operational much later; this may be intentional but "possibly out of place" in the outline is already a signal to inspect whether early readers are asked to accept a postulate whose terms are not yet available.

Composition machinery should define closure defect, tempo composition, directed-separation under composition, and wrapper/class-coercion routes. I predict possible overclaim around wrapper constructions: a wrapper can restore an external Class 1 interface while leaving substrate coupling behaviorally relevant. The outline seems aware of structural-vs-behavioral leakage, so the audit question is whether that caveat is load-bearing or decorative.

Unity/communication should parameterize closure through shared models/objectives/strategy/observation and trust-weighted communication gain. I expect the math to be less mature and more formulation-grade. The main risk is treating unity dimensions as independent axes when real shared-intent/communication channels are correlated.

Cooperative/adversarial coupling should unify signs of coupling, team persistence, adversarial destabilization, recipient-side regime taxonomy, and superlinear tempo advantage. The most likely math issue is exponent/regime overreach: superlinear advantage claims usually depend heavily on assumptions about scaling, saturation, observation noise, and attacker/defender resource coupling.

Strategic composition should move from contraction to equilibrium/game machinery. I predict the potential/monotone game sub-scope will be honest but narrow, and that the transition from partially opposed objectives to composite class refinement will be the place to check for category drift.

Appendix A is likely not "appendix" in the weak sense: it contains proof kernels and late meta-pattern segments that may be load-bearing for the main text. I expect the permitted appendix-back-pointer exception to fire frequently. I will be especially cautious around `deriv-discrete-sector-condition`, `result-certificate-existence`, `deriv-graph-structure-uniqueness`, `disc-stability-certificate`, `disc-identifiability-floor`, `result-contraction-template`, `deriv-matrix-persistence-condition`, and `deriv-fisher-local-update-gain`.

Appendix B worked examples should be math-verified if I reach them and especially if the final report relies on them. I expect the Kalman example to be strongest, bandit/strategy examples to expose convention hierarchy boundaries, and L1 common-cause example to test whether identifiability-floor language is operational or only conceptual.

## Predictions about what is open

The framework likely still has open boundaries around general nonlinear/nonseparable systems, composition closure beyond structured tiers, coupled Class 3 agents, strategic dynamics under latent common causes, and population-level transition dynamics. The outline explicitly names multiple GAP rows and missing meta-segments, so "open work exists" is not itself a finding. A finding would require a supposedly verified/current segment to rely on a missing piece as if it had been supplied.

I expect some terms will be introduced before fully stabilized, especially "certificate", "closure defect", "unity", "tempo", "fitness", "sufficiency", and "objective". Since I am not reading `LEXICON.md` under the modified prompt, I will judge whether the segment itself carries enough local definition rather than importing external vocabulary infrastructure.

## Predictions about overclaim

The likely overclaim patterns are:

- Lyapunov sector results being rhetorically treated as global or general when only local/metric/structured-sector conditions support them.
- IB/KL/Fisher machinery treated as uniquely forced in contexts outside the statistical or axiom-specified regime.
- Planning/strategy claims applying to all purposeful agents despite pre-compiled controllers and Class 3 coupled agents requiring narrower treatment.
- Composition/wrapping claims implying substrate truthification rather than interface-level coercion with leakage.
- Adversarial tempo claims implying universal superlinear advantage rather than regime-specific scaling.

## What would be most novel if it holds

The most consequential structure would be the stability-certificate cross-section: one certificate object tying persistence, separability, coordinate forcing, identifiability floors, and projection/composition behavior together. If that unification survives detailed reading, it is stronger than a bag of analogies; it gives a reusable epistemic architecture for checking whether a domain-specific agent theory is exact, approximate, or blocked.

The second most consequential result would be the survival lattice for Part II: if the framework can say exactly which purposeful-agent results survive from separated agents into coupled/substrate architectures, it gives downstream LLM-agent work a disciplined way to avoid both naive modularity assumptions and vague "everything is coupled" pessimism.

## Findings I expect to surface

I expect a small number of dependency/order issues, especially where Appendix A proof machinery or late meta-pattern language is referenced before the outline walk reaches it. I expect several candidate scope/status mismatches that may be rescinded once the full segment is read, because the outline preface is unusually explicit about scope honesty. I expect fewer simple algebra errors in early Part I than in late appendix or worked-example material, simply because early Part I is likely over-audited relative to newer late additions.

My working emphasis will be: dependency order, scope/status honesty, and selective math verification where a worked example or explicit counterexample is load-bearing. I will also make a small TikZ or diagram artifact alongside each reflection when a visual model clarifies the new understanding.
