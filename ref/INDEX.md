# `ref/` — Reference Paper Index

This directory holds external papers cited by AAD / TST segments. **The PDFs themselves are excluded from git tracking** (see `.gitignore`) to respect academic redistribution rights — keeping them local means agents and reviewers can read the source material during derivation-trace work without publishing third-party PDFs via this repo.

This `INDEX.md` is the tracked bibliography. Each entry gives the expected filename (canonical `{author}-{year}-{short}.pdf`), the full citation, and which AAD / TST segments rely on it. If a file is missing locally, use the citation to re-acquire.

**Acquisition conventions.** Prefer open-access sources (arXiv, author homepages, publisher open-access editions). For paywalled papers, institutional access or direct preprint retrieval is expected. PDFs acquired during citation audits should be saved with the canonical filename so future audits locate them predictably.

## Canonical bibliography

### Information theory / Bayesian / functional equations

| Filename | Citation | AAD sites |
|---|---|---|
| `tishby-1999-information-bottleneck.pdf` | Tishby, N., Pereira, F. C. & Bialek, W. (1999). "The information bottleneck method." *Proc. 37th Allerton Conf.* (also arXiv:physics/0004057, 2000). | `#information-bottleneck`, `#compression-operations`, `#additive-coordinate-forcing` |
| `chechik-2005-gaussian-ib.pdf` | Chechik, G., Globerson, A., Tishby, N. & Weiss, Y. (2005). "Information Bottleneck for Gaussian Variables." *JMLR* 6:165–188. Theorem 3.1 is the Gaussian-IB frontier result. | `#compression-operations`, `#unity-closure-mapping` |
| `csiszar-1991-why-least-squares-maxent.pdf` | Csiszár, I. (1991). "Why least squares and maximum entropy? An axiomatic approach to inference for linear inverse problems." *Annals of Statistics* 19(4):2032–2066. Theorem 3 corollary + Theorem 5 (composition consistency). | `#strategy-cost-regret-bound` §6.1, `#additive-coordinate-forcing` |
| `shore-johnson-1980-axiomatic-maxent.pdf` | Shore, J. E. & Johnson, R. W. (1980). "Axiomatic derivation of the principle of maximum entropy and the principle of minimum cross-entropy." *IEEE Trans. Info. Theory* 26(1):26–37. Axiom II (system-independence) at p.28. | `#strategy-cost-regret-bound` §6.1, `#additive-coordinate-forcing` |
| `hobson-1969-theorem-information.pdf` | Hobson, A. (1969). "A new theorem of information theory." *J. Stat. Phys.* 1(3):383–391. | `#strategy-cost-regret-bound` §6.1, `#additive-coordinate-forcing` |
| `eguchi-1983-second-order-efficiency.pdf` | Eguchi, S. (1983). "Second order efficiency of minimum contrast estimators in a curved exponential family." *Annals of Statistics* 11(3):793–803. §2 contrast-function framework (the f-divergence / Fisher-metric result AAD cites); Theorem 3 is about estimator efficiency via $\Gamma^1$-transversality. | `#strategy-cost-regret-bound` §6.2 |
| `amari-2009-alpha-divergence-unique-f-bregman.pdf` | Amari, S.-i. (2009). "$\alpha$-divergence is unique, belonging to both $f$-divergence and Bregman divergence classes." *IEEE Trans. Info. Theory* 55(11):4925–4931. Theorem 1 (alpha-family uniqueness at f ∩ Bregman). | `#strategy-cost-regret-bound` §6.1, `#additive-coordinate-forcing` |
| `amari-cichocki-2010-info-geom-divergence.pdf` | Amari, S.-i. & Cichocki, A. (2010). "Information geometry of divergence functions." *Bull. Polish Acad. Sci., Tech. Sci.* 58(1):183–195. | `#strategy-cost-regret-bound` §6.2 |
| `ay-2017-information-geometry.pdf` | Ay, N., Jost, J., Lê, H. V. & Schwachhöfer, L. (2017). *Information Geometry*. Springer. | `#strategy-cost-regret-bound` §6.2 |
| `tishby-polani-2011-info-decision-action.pdf` | Tishby, N. & Polani, D. (2011). "The Information Theory of Decision and Action." In V. Cutsuridis, A. Hussain & J. G. Taylor (eds.), *Perception-Action Cycle: Models, Architectures, and Hardware*, Springer, pp. 601–636. Information-to-Go multi-information $\mathfrak{I}^\pi(s_t, a_t)$ (Eq. 15, p. 19); objective $\min_\pi[\mathfrak{I}^\pi - \beta Q^\pi]$ (Eq. 17, p. 21). §7.2 perfectly-adapted-environments degenerate case. **Not** the KL-to-reference form; that is Rubin 2012. | `#strategy-cost-regret-bound` §6.3 (info-theoretic-MDP lineage positioning) |
| `rubin-2012-trading-value-info-mdps.pdf` | Rubin, J., Shamir, O. & Tishby, N. (2012). "Trading value and information in MDPs." In T. V. Guy, M. Kárný & D. Wolpert (eds.), *Decision Making with Imperfect Decision Makers*, Springer, pp. 57–74. Control information $\Delta I(s) = D_{\mathrm{KL}}(\pi_s \Vert \rho_s)$ (agent-first, §2.2 Eq. 3 p. 4); free-energy $F_\pi = I_\pi - \beta V_\pi$ (§3.1 p. 5); Bellman recursion Theorem 1 p. 5. Framed as rate-distortion, not IB. Theorem 3 gives an independent PAC-Bayesian generalization bound for the KL-to-reference form. §3.3 deterministic-environment linearization $Z = \Phi Z$ parallels AAD's $\alpha_1$ sub-scope. **Direction is agent-first**, opposite to AAD's optimum-first. | `#strategy-cost-regret-bound` §6.2 (PAC-Bayesian motivation), §6.3 |
| `levine-2018-rl-control-as-inference.pdf` | Levine, S. (2018). "Reinforcement learning and control as probabilistic inference: tutorial and review." arXiv:1805.00909. Uses $D_{\mathrm{KL}}(q \Vert p^*)$ (proposal-first) throughout (§3.1 Eq. 11 p. 8); §5.2 p. 15 contrasts RL's mode-seeking $D_{\mathrm{KL}}(p_\theta \Vert p_{\mathrm{tgt}})$ with supervised's reverse. **Does NOT connect to IB**; connections are to Kalman duality, linearly-solvable MDPs, path-integral control, max causal entropy IRL. | `#strategy-cost-regret-bound` §6.3 |

### Control theory / stochastic stability

| Filename | Citation | AAD sites |
|---|---|---|
| *(not in ref/ — standard textbook)* | Khalil, H. K. (2002). *Nonlinear Systems* (3rd ed.), Prentice Hall. Theorems 4.17 (converse Lyapunov), 4.18 (ultimate boundedness); Chapters 4, 9, 11. | `#sector-condition-derivation`, `#gain-sector-derivation`, `#sector-persistence-template`, `#temporal-nesting`, `#multi-timescale-stability` |
| *(not in ref/ — standard textbook)* | Khasminskii, R. (2012). *Stochastic Stability of Differential Equations* (2nd ed.), Springer. Chapter 5 (stopping-time localization). | `#sector-condition-derivation` |
| *(not in ref/ — standard textbook)* | Nesterov, Y. (2004). *Introductory Lectures on Convex Optimization*. Springer. Theorem 2.1.10 (strong convexity ↔ gradient monotonicity). | `#sector-condition-derivation`, `#gain-sector-derivation` |
| *(not in ref/ — standard textbook)* | Cover, T. M. & Thomas, J. A. (2006). *Elements of Information Theory* (2nd ed.), Wiley. §I.12–13 (rate-distortion / Lagrangian-dual); §11.6 (Pinsker). | `#information-bottleneck`, `#compression-operations`, `#strategy-cost-regret-bound` |

### Causal inference

| Filename | Citation | AAD sites |
|---|---|---|
| `bareinboim-2022-pearl-hierarchy.pdf` (also `r60.pdf` = identical content; `ACMBook-published-2022.pdf` is the host volume) | Bareinboim, E., Correa, J. D., Ibeling, D. & Icard, T. (2022). "On Pearl's Hierarchy and the Foundations of Causal Inference." Ch. 1 in *Probabilistic and Causal Inference: The Works of Judea Pearl*, Geffner, H., Dechter, R. & Halpern, J. Y. (eds.), ACM Books, ISBN 978-1-4503-9587-8 (also Columbia CausalAI Lab TR R-60 at causalai.net/r60.pdf). Theorem 1 (Causal Hierarchy Theorem, p.22). | `#causal-hierarchy-requirement`, `#causal-insufficiency-detection`, `#loop-interventional-access`, `#identifiability-floor`, `#pearl-causal-hierarchy`, `#strategic-dynamics-derivation`, separability-ladder paper [B-N-Sep] cite-and-extend anchor |
| *(not in ref/ — standard textbook)* | Pearl, J. (2009). *Causality* (2nd ed.), Cambridge UP. Definition 7.1.1; Theorem 1.4.1. | `#graph-structure-uniqueness`, `#pearl-causal-hierarchy` |
| *(not in ref/ — standard textbook)* | Spirtes, P., Glymour, C. & Scheines, R. (2000). *Causation, Prediction, and Search* (2nd ed.), MIT Press (open-access on MIT Press Direct). Theorem 3.4 (CMC). | `#graph-structure-uniqueness` |
| *(not in ref/ — standard textbook)* | Lauritzen, S. (1996). *Graphical Models*, Oxford UP. Theorem 3.27. | `#graph-structure-uniqueness` |

### Identifiability / separability-ladder prior art (added 2026-05-04)

*Pearl-Shpitser-Bareinboim identification lineage, Robins / Richardson / Dawid restricted-intervention lineage, and philosophy-of-modeling parallels. Used by `~/src/agentic-systems/ref/separability-ladder-prior-art-report.md` (Undermind output 2026-05-04) and the planned standalone separability-ladder paper [B-N-Sep] (see `~/src/ops/papers/03-asf-tier2-and-cross-segment.md`). All filenames preserved as-found rather than renamed; canonical-rename suggestion in parentheses where useful.*

| Filename | Citation | Role |
|---|---|---|
| `r327.pdf` *(canonical: `shpitser-pearl-2006-identification-recursive-semi-markovian.pdf`)* | Shpitser, I. & Pearl, J. (2006). "Identification of Joint Interventional Distributions in Recursive Semi-Markovian Causal Models." *AAAI 2006*, pp. 1219-1226. Columbia CausalAI Lab TR R-327. | **[Shp06]** Foundational ID completeness paper; cleanest verified no-go-plus-recovery pairing in the Pearl lineage |
| `r336-published.pdf` *(canonical: `shpitser-pearl-2008-complete-identification-causal-hierarchy.pdf`)* | Shpitser, I. & Pearl, J. (2008). "Complete Identification Methods for the Causal Hierarchy." *J. Mach. Learn. Res.* 9:1941-1979. R-336. | **[Shp08]** Core completeness across Pearl's hierarchy; main instance-level formalization |
| `r443.pdf` *(canonical: `bareinboim-pearl-2014-transportability-multiple-environments.pdf`)* | Bareinboim, E. & Pearl, J. (2014). "Transportability from Multiple Environments with Limited Experiments: Completeness Results." *NIPS 2014*, pp. 280-288. R-443. | **[Bar14]** mz-transportability completeness; structured-repair-via-limited-experiments instance |
| `r46.pdf` *(canonical: `lee-correa-bareinboim-2019-general-identifiability.pdf`)* | Lee, S., Correa, J. D. & Bareinboim, E. (2019). "General Identifiability with Arbitrary Surrogate Experiments." *UAI 2019*, pp. 389-398. R-46 (first version May 2019; last revised Jul 2022). | **[Lee19]** g-identifiability with hedgelets and thickets; generalized structured-repair regime |
| `r269-reprint.pdf` *(canonical: `pearl-2000-comment-on-dawid.pdf`)* | Pearl, J. (2000). "Comment" [on Dawid 2000]. *JASA* 95(450):428-431. R-269. | Pearl's response to Dawid 2000; useful context for the counterfactual / decision-theoretic debate but not a separate prior-art anchor |
| `1-s2.0-0270025586900886-main.pdf` *(canonical: `robins-1986-treatment-regime-mortality-studies.pdf`)* | Robins, J. (1986). "A new approach to causal inference in mortality studies with a sustained exposure period—application to control of the healthy worker survivor effect." DOI 10.1016/0270-0255(86)90088-6. | **[Rob86]** Foundational treatment-regime semantics; G-computation under fully randomized structured-tree assumptions; restricted-intervention lineage anchor |
| `dawid_jasa2000.pdf` *(canonical: `dawid-2000-causal-inference-without-counterfactuals.pdf`)* | Dawid, A. P. (2000). "Causal Inference without Counterfactuals." *JASA* 95(450):407-424. DOI 10.1080/01621459.2000.10474210. | **[Daw00]** Decision-theoretic regime-indicator approach; restricted-intervention lineage |
| `causality-meeting6.pdf` | Dawid, A. P. (2015-11-12). "Causal Inference Without Counterfactuals" — talk slides. | Talk version of [Daw00]; same content in presentation form |

### Philosophy of modeling / Simon-line (added 2026-05-04)

| Filename | Citation | Role |
|---|---|---|
| `Causal Hierarchies published version.pdf` *(canonical: `hoover-2012-causal-structure-hierarchies-models.pdf`)* | Hoover, K. D. (2012). "Causal structure and hierarchies of models." *Studies in History and Philosophy of Biological and Biomedical Sciences* 43(4):778-786. DOI 10.1016/j.shpsc.2012.05.007. | **[Hoo12b]** Closest philosophy-of-modeling parallel; well-made-toaster vs. repairman contrast comes close to clean-case-vs-repair-case distinction; separability-ladder paper [B-N-Sep] |
| `Simon_box00027_fld01902_bdl0001_doc0001.pdf` *(canonical: `iwasaki-simon-1994-causality-model-abstraction.pdf`)* | Iwasaki, Y. & Simon, H. A. (1994). "Causality and model abstraction." *Artificial Intelligence* 67(1):143-194. DOI 10.1016/0004-3702(94)90014-0. (Filename indicates retrieval from CMU's Herbert Simon archives, box 27, folder 1902.) | **[Iwa94]** Simon-line philosophy-of-modeling parallel; structural-equation account of causality, manipulability, aggregation, near-decomposability; relevant background for separable-core intuition; separability-ladder paper [B-N-Sep] |

### Active inference / cognitive neuroscience

| Filename | Citation | AAD sites |
|---|---|---|
| `friston-2010-free-energy-principle-arxiv.pdf` | Friston, K. (2010). "The free-energy principle: a unified brain theory?" *Nature Reviews Neuroscience* 11(2):127–138 (arXiv:1001.0614). | `#information-bottleneck`, `#compression-operations` |
| `friston-2013-life-as-we-know-it.pdf` | Friston, K. (2013). "Life as we know it." *J. Royal Soc. Interface* 10(86):20130475. | `#directed-separation` |
| `friston-2017-active-inference-process-theory.pdf` | Friston, K., FitzGerald, T., Rigoli, F., Schwartenbeck, P. & Pezzulo, G. (2017). "Active inference: a process theory." *Neural Computation* 29(1):1–49 (doi 10.1162/NECO_a_00912). Pragmatic/epistemic EFE decomposition. | `#loop-interventional-access`, `#satisfaction-gap`, `#control-regret`, `#strategy-complexity-cost`, `#compression-operations` |
| `friston-2019-free-energy-particular-physics.pdf` | Friston, K. (2019). "A free energy principle for a particular physics." arXiv:1906.10184. Primary source for NESS-density framing. | `#sector-persistence-template`, `#directed-separation` |
| `friston-2023-path-integrals.pdf` | Friston, K., Da Costa, L., Sakthivadivel, D., Heins, C., Pavliotis, G., Ramstead, M. & Parr, T. (2023). "Path integrals, particular kinds, and strange things." *Physics of Life Reviews* 47. Path-integral methodological extension of FEP. | `#sector-persistence-template`, `#directed-separation` |
| `dacosta-2020-active-inference-discrete.pdf` | Da Costa, L., Parr, T., Sajid, N., Veselic, S., Neacsu, V. & Friston, K. (2020). "Active inference on discrete state-spaces: a synthesis." *J. Math. Psych.* 99. | `#satisfaction-gap`, `#compression-operations` |
| `sajid-2021-active-inference-demystified.pdf` | Sajid, N., Ball, P. J., Parr, T. & Friston, K. (2021). "Active inference: demystified and compared." *Neural Computation* 33(3):674–712. | `#satisfaction-gap` |
| `parr-pezzulo-2022-active-inference-book.pdf` (also `f000200_9780262369978.pdf` = chapter PDF from same MIT Press eBook DOI 10.7551/mitpress/12441.001.0001, different chapter page IDs) | Parr, T. & Pezzulo, G. (2022). *Active Inference: The Free Energy Principle in Mind and Brain*. MIT Press. Chapter 2 ("The Low Road to Active Inference") is cited. | `#loop-interventional-access` |
| `Lundh2026ReviewofParretal.pdf` | Lundh, L.-G. (2026). Book review of Parr, Pezzulo & Friston *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior* (MIT Press). *Journal for Person-Oriented Research* 12(1):63-69. DOI 10.17505/jpor.2026.29052. | Reception/review context for Parr-Pezzulo |
| `bruineberg-2022-emperors-markov-blankets.pdf` | Bruineberg, J., Dolega, K., Dewhurst, J. & Baltieri, M. (2022). "The Emperor's New Markov Blankets." *Behavioral and Brain Sciences* 45:e69. Introduces the verbatim Pearl-blanket / Friston-blanket distinction (p.3, credit to Martin Biehl in footnote 3). | `#directed-separation`, `#loop-interventional-access` |
| `aguilera-2022-how-particular-fep.pdf` | Aguilera, M., Millidge, B., Tschantz, A. & Buckley, C. L. (2022). "How particular is the physics of the free energy principle?" *Physics of Life Reviews* 40:24–50. FEP-flow narrow-validity critique. | `#sector-persistence-template` |
| `sun-firestone-2020-dark-room.pdf` | Sun, Z. & Firestone, C. (2020). "The dark room problem." *Trends in Cognitive Sciences* 24(5):346–348. | `#satisfaction-gap`, `#control-regret` |
| `clark-2013-whatever-next.pdf` | Clark, A. (2013). "Whatever next? Predictive brains, situated agents, and the future of cognitive science." *Behavioral and Brain Sciences* 36(3):181–204. | `#compression-operations` |
| `wiener-1948-cybernetics.pdf` | Wiener, N. (1948). *Cybernetics: Or Control and Communication in the Animal and the Machine*. MIT Press. | `#loop-interventional-access` |

### Agent-based modeling / coevolution

| Filename | Citation | AAD sites |
|---|---|---|
| `miller-2022-ex-machina.pdf` | Miller, J. H. (2022). *Ex Machina: Coevolving Machines and the Origins of the Social Universe*. SFI Press, 410 pp. | `#composition-closure` (§3.3 meta-machine), `#composition-scope-condition` (Ch. 1 IAM), `#strategy-complexity-cost` (Table 12.2), `#structural-adaptation-necessity` (five-phase motif) |
| `2026-hafez.2602.22519v1.pdf` | Hafez, W., Wei, C., Felipe, R., Nazeri, A. & Reid, C. (2026). "A Mathematical Theory of Agency and Intelligence." arXiv:2602.22519. Defines bi-predictability $P$ — the shared fraction of information across observations, actions, and outcomes relative to the loop's total informational budget — and proves regime-dependent bounds (unity attainable in quantum interactions; $P \leq 0.5$ classically; lower once agency is introduced). Distinguishes *agency* (capacity to act on predictions) from *intelligence* (additionally learning from interaction, self-monitoring effectiveness, and adapting scope of observations / actions / outcomes); current AI systems have the former but not the latter. Confirms bounds in physical (double-pendulum), RL, and multi-turn LLM systems. Inspired by thalamocortical regulation. | (cited via comparative framing in `_historical-context`; substantive integration into segments queued) |
| *(separate Hafez paper, possibly not yet acquired locally)* | Hafez, A. et al. Informational Cost of Agency / Information Digital Twin series. arXiv:2603.01283 et al. $H_b$ backward-predictive-uncertainty measure; 89% vs 44% detection accuracy. The two Hafez papers are distinct contributions; the "Mathematical Theory" paper above defines $P$ (bi-predictability), this one defines $H_b$ (backward-predictive uncertainty). Both inform Section III. | `#der-adversarial-destabilization`, `#der-directed-separation`, `#der-causal-hierarchy-requirement`, `#def-agent-spectrum` |

### Context / comparative framework

| Filename | Citation | AAD sites |
|---|---|---|
| `ssrn-5334620.pdf` *(also referenced as `the-gaa-framework-model-of-adaptive-systems-baigozin-2025.pdf`; SSRN ID 5334620 is the actual source)* | Baigozin, Y. (2025-07-01). "The General Adaptive Agency (GAA) Framework: A First-Principles Model of Adaptive Systems." Independent researcher / SSRN preprint 5334620. | Context/comparative reading |
| `Bhatia 2016 CogSci PP.pdf` *(canonical: `bhatia-2016-vector-space-semantic-models.pdf`)* | Bhatia, S. (2016). "Vector Space Semantic Models Predict Subjective Probability Judgments for Real-World Events." Department of Psychology, University of Pennsylvania. (Likely CogSci 2016 conference paper.) | Embeddings-line reference (epistemic hedging geometry / probability geometry) |

## Non-PDF files in `ref/`

- `INDEX.md` — this file (tracked).
- `.gitignore` — excludes `*.pdf` from git (tracked).
- `summary-taking-ai-welfare-seriously.md` — markdown summary (tracked).
- `arXiv-2503.00237v1/` — source directory for a paper's LaTeX source (tracked as-is).

## Known gaps (papers cited but not currently in `ref/`)

These citations appear in `~/src/agentic-systems/ref/separability-ladder-prior-art-report.md` and would benefit the planned [B-N-Sep] separability-ladder paper, but were not found locally during the 2026-05-04 PDF-identification sweep:

- **Hintikka, J. (1991). "Towards a General Theory of Identifiability."** DOI 10.1007/978-94-011-3346-3_7. Springer/Kluwer-Netherlands edited volume chapter, 1991. **The strongest older abstract anchor in the prior-art report** — distinguishes theory-alone determination, determination-with-auxiliary-empirical-results, and non-identifiability at an abstract logical level. Spot-check of unidentified PDFs in `ref/` 2026-05-04 did not locate this file. May need reacquisition.
- **Basse, G. W. & Bojinov, I. (2020). "A general theory of identification."** Closest modern formal abstraction across fields. Not yet acquired locally.
- **Maclaren, O. J. & Nicholson, R. (2019). "What can be estimated? Identifiability, estimability, causal inference and ill-posed inverse problems."** *ArXiv* 1904.02826. Best dual-structure neighbor (causal identification ↔ ill-posed inverse problems). Not yet acquired locally.
- **Robins, J., Richardson, T. & Shpitser, I. (2020). "An Interventionist Approach to Mediation Analysis."** ACM Books / DOI 10.1145/3501714.3501754. **The cleanest in-domain cite-and-extend anchor for [B-N-Sep]** — clean separable case + structured-repair via expanded-graph decomposition + recanting-witness no-go. Not yet acquired locally; high priority to acquire when paper drafting begins.
- **Richardson, T. (2013). "Single World Intervention Graphs (SWIGs)."** Restricted-intervention graphical bridge. Not yet acquired locally.
- **Dawid, A. P. (2020). "Decision-theoretic foundations for statistical causality."** *J. Causal Inference*. DOI 10.1515/jci-2020-0008. Decision-theoretic restricted-intervention. Not yet acquired locally.
- **Stensrud, M., Young, J. G., Didelez, V., Robins, J. & Hernán, M. A. (2019). "Separable Effects for Causal Inference in the Presence of Competing Events."** Neighboring recurrence in competing-events setting. Not yet acquired locally.
- **Díaz, I. (2022). "Non-agency interventions for causal mediation in the presence of intermediate confounding."** *J. Royal Statistical Society B*. Neighboring recurrence under non-manipulable causes. Not yet acquired locally.

## Audit trail

A project-wide citation audit completed 2026-04-23 (commits `7456ec3`, `6567914`, `f61e62f`) verified 26 of the above citations at PDF level or via publisher TOCs. Zero confirmed attribution errors project-wide. See `TODO.md` §"Citations Audit — COMPLETE 2026-04-23" for detail.

A second sweep on 2026-05-04 identified 13 obscure-named PDFs (`r46`, `r60`, `r269-reprint`, `r327`, `r336-published`, `r443`, `1-s2.0-0270025586900886-main`, `dawid_jasa2000`, `causality-meeting6`, `Causal Hierarchies published version`, `Simon_box00027_fld01902_bdl0001_doc0001`, `ACMBook-published-2022`, `f000200_9780262369978`, `ssrn-5334620`, `Bhatia 2016 CogSci PP`, `Lundh2026ReviewofParretal`) by reading first-page content and added their canonical citations and AAD-site mappings above. Eight prior-art papers from the separability-ladder report remain unacquired; see "Known gaps" above.
