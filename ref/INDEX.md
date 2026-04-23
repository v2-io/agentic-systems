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
| `bareinboim-2022-pearl-hierarchy.pdf` | Bareinboim, E., Correa, J. D., Ibeling, D. & Icard, T. (2022). "On Pearl's Hierarchy and the Foundations of Causal Inference." Ch. 1 in *Probabilistic and Causal Inference: The Works of Judea Pearl*, ACM Books (also Columbia CausalAI Lab TR R-60 at causalai.net/r60.pdf). Theorem 1 (Causal Hierarchy Theorem, p.22). | `#causal-hierarchy-requirement`, `#causal-insufficiency-detection`, `#loop-interventional-access`, `#identifiability-floor`, `#pearl-causal-hierarchy`, `#strategic-dynamics-derivation` |
| *(not in ref/ — standard textbook)* | Pearl, J. (2009). *Causality* (2nd ed.), Cambridge UP. Definition 7.1.1; Theorem 1.4.1. | `#graph-structure-uniqueness`, `#pearl-causal-hierarchy` |
| *(not in ref/ — standard textbook)* | Spirtes, P., Glymour, C. & Scheines, R. (2000). *Causation, Prediction, and Search* (2nd ed.), MIT Press (open-access on MIT Press Direct). Theorem 3.4 (CMC). | `#graph-structure-uniqueness` |
| *(not in ref/ — standard textbook)* | Lauritzen, S. (1996). *Graphical Models*, Oxford UP. Theorem 3.27. | `#graph-structure-uniqueness` |

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
| `parr-pezzulo-2022-active-inference-book.pdf` | Parr, T. & Pezzulo, G. (2022). *Active Inference: The Free Energy Principle in Mind and Brain*. MIT Press. Chapter 2 ("The Low Road to Active Inference") is cited. | `#loop-interventional-access` |
| `bruineberg-2022-emperors-markov-blankets.pdf` | Bruineberg, J., Dolega, K., Dewhurst, J. & Baltieri, M. (2022). "The Emperor's New Markov Blankets." *Behavioral and Brain Sciences* 45:e69. Introduces the verbatim Pearl-blanket / Friston-blanket distinction (p.3, credit to Martin Biehl in footnote 3). | `#directed-separation`, `#loop-interventional-access` |
| `aguilera-2022-how-particular-fep.pdf` | Aguilera, M., Millidge, B., Tschantz, A. & Buckley, C. L. (2022). "How particular is the physics of the free energy principle?" *Physics of Life Reviews* 40:24–50. FEP-flow narrow-validity critique. | `#sector-persistence-template` |
| `sun-firestone-2020-dark-room.pdf` | Sun, Z. & Firestone, C. (2020). "The dark room problem." *Trends in Cognitive Sciences* 24(5):346–348. | `#satisfaction-gap`, `#control-regret` |
| `clark-2013-whatever-next.pdf` | Clark, A. (2013). "Whatever next? Predictive brains, situated agents, and the future of cognitive science." *Behavioral and Brain Sciences* 36(3):181–204. | `#compression-operations` |
| `wiener-1948-cybernetics.pdf` | Wiener, N. (1948). *Cybernetics: Or Control and Communication in the Animal and the Machine*. MIT Press. | `#loop-interventional-access` |

### Agent-based modeling / coevolution

| Filename | Citation | AAD sites |
|---|---|---|
| `miller-2022-ex-machina.pdf` | Miller, J. H. (2022). *Ex Machina: Coevolving Machines and the Origins of the Social Universe*. SFI Press, 410 pp. | `#composition-closure` (§3.3 meta-machine), `#composition-scope-condition` (Ch. 1 IAM), `#strategy-complexity-cost` (Table 12.2), `#structural-adaptation-necessity` (five-phase motif) |
| `2026-hafez.2602.22519v1.pdf` | Hafez, A. et al. (2026). Informational Cost of Agency / Information Digital Twin series. arXiv:2603.01283 et al. $H_b$ backward-predictive-uncertainty measure; 89% vs 44% detection accuracy. | `#adversarial-destabilization`, `#directed-separation`, `#causal-hierarchy-requirement`, `#agent-spectrum` |

### Context / comparative framework

| Filename | Citation | AAD sites |
|---|---|---|
| `the-gaa-framework-model-of-adaptive-systems-baigozin-2025.pdf` | Baigozin (2025). The GAA framework — context/comparative reading. | (reference only) |

## Non-PDF files in `ref/`

- `INDEX.md` — this file (tracked).
- `.gitignore` — excludes `*.pdf` from git (tracked).
- `summary-taking-ai-welfare-seriously.md` — markdown summary (tracked).
- `arXiv-2503.00237v1/` — source directory for a paper's LaTeX source (tracked as-is).

## Audit trail

A project-wide citation audit completed 2026-04-23 (commits `7456ec3`, `6567914`, `f61e62f`) verified 26 of the above citations at PDF level or via publisher TOCs. Zero confirmed attribution errors project-wide. See `TODO.md` §"Citations Audit — COMPLETE 2026-04-23" for detail.
