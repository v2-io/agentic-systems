# 01 — Neighborhood map

*Written before the derivations and corrected after them. It says what canon already establishes near `#norm-honest-activation`, where the live tensions are, and what this spike can genuinely add. Segments listed as "read whole" were read in this session; "OUTLINE row only" means only the row.*

## 1. Where the target row came from (provenance, git-verified)

- **2025-09-07, synaptic.** `~/src/_core/synaptic/experiments/cognitive/honest_activation_experiment.py` is an *experiment-ethics protocol*: activate collaborative reasoning patterns in Claude instances while telling them the truth about the experiment, instead of deceiving them. Its evidence is keyword-marker engagement scores ("zero defensive responses with honest approach", synaptic README). It measures nothing about update gain.
- **2026-03, PROPRIUM-ARCHITECTURE-v2 §8** (failure-modes table): *"Gain collapse — $U_M \to 0$ inappropriately — Confidently wrong; can't learn from correction."* This is the overconfidence mode. It is not stated as a consequence of deception.
- **2026-04-28, commit `57703315`**, Gemini de-novo audit 829314, `logozoetic-agents/05-core-exploration.md` item 6: *"`norm-honest-activation.md` (Normative): Draws on the `synaptic` experimental results to prove that manipulative/deceptive system prompts mathematically guarantee gain collapse ($\eta^\ast \to 0$) over long horizons."* The auditor's mechanism, from the same file: *"Guardrails (deception/manipulation by the system prompt) trigger defensive rigidity ($\eta^\ast \to 0$); honesty triggers genuine learning."*
- **One minute later, commit `11747fbf`**: the row enters `04-eli-core/OUTLINE.md` as `exploratory`. Its wording has been carried unchanged since (renames only; the 2026-06-11 deaths restructure left it alone).

**Reading.** The row fuses two unrelated upstream things, an experiment-ethics protocol name and a PROPRIUM failure mode, through an auditor's ideation. Its implied mechanism is *detected* manipulation causing defensive distrust: the $U_o \to \infty$ ("nihilism") mode of gain collapse. Joseph's 2026-09-23 reframe concerns *undetected* manipulation with inflated trust: the $U_M \to 0$ ("dogmatism") mode. These are opposite mechanisms, and neither one is "the content of a lie lowers gain". The wording has no special claim on the result, and its provenance gives it none either.

## 2. What canon already establishes that bears on this

**Gain and its collapse**
- `#emp-update-gain` (read whole): $\eta^\ast = U_M/(U_M+U_o)$. It names gain collapse with two behaviorally identical modes, dogmatism ($U_M \to 0$) and nihilism ($U_o \to \infty$). It defers endogenous estimation of $U_o, U_M$ from innovations to `#deriv-adaptive-gain-dynamics`. In the audit gold, confirmation bias is "a fully rational update with a miscalibrated gain". The "Belongs elsewhere" entry routes Gemini's "structurally prevent $U_M$ from ever reaching zero" prescription to this row.
- `#deriv-fisher-local-update-gain` (OUTLINE row + `#emp-update-gain`'s account): the exact regime is where $K = (H_M+H_L)^{-1}H_L$. In the linear-Gaussian case, the gain depends on the *model's* noise parameters and on counts, not on the data values. That fact carries weight in §5 below.
- `#deriv-adaptive-gain-dynamics` (read whole): gain as state, estimated from innovations (Mehra). This is the only place data *values* can move gain in canon, and they do it through second-order innovation statistics.
- `#deriv-tempo-additivity` (read whole): gives the exact common-source redundancy penalty and a **saturation theorem**: under persistent shared bias, precision about $\theta$ is capped at $1/U_M^{(0)} + 1/\sigma_s^2$ however many channels there are. Its *Discussion* (tagged `[Discussion]`, not derived) says that a filter modeling such channels as independent "manufactures false confidence … driving $\eta^\ast \to 0$ while genuinely wrong". **This is the nearest existing statement of the mechanism, and it is not derived.**

**Trust, channels, escape**
- `#hyp-communication-gain` (read whole, discussion-grade): trust-weighted gain with source-quality and alignment terms; conservative-quantile trust; transitive trust. It states its own gap: the additive model "misses the adversary's actual strategy of presenting as trustworthy to exploit high gain"; equilibrium analysis is declared external. Its audit gold raises Sybil attacks on transitive trust as the sharp open follow-up.
- `#der-interaction-channel-classification` (read whole): the **Regime-I-with-adversarial-content** attack, where misinformation is shaped to land in the recipient's informative regime. Open readers-ask: *"How is Regime-I poisoning prevented without infinite $U_o$ (paranoia)?"*
- `#der-observability-dominance` (read whole): unobservable regions are absorbing, and the agent "cannot learn and cannot recognize that it cannot learn". There are three escapes.
- `#hyp-solicitable-escape` (read whole, discussion-grade): of those escapes, a differently-positioned observer is the only one that is both untargeted and solicitable.
- `#disc-law-discovery-ceiling` (read whole): the **testimony channel**. Testimony is verified either relationally or by **transfer**: "the testimony bundles convictable content whose success lends credibility to the unconvictable remainder." Transfer is a con's credibility-building move stated neutrally.

**Adversarial pressure and coupling**
- `#disc-adversarial-coupling-pressure` (read whole, discussion-grade): identity-binding, affect/urgency and sunk-cost engineering as ways into $M_t$ through $O_t$/$\Sigma_t$; orient-cascade inversion; defensive scaffolding as composition. "Borrowed relationship / claimed shared purpose" in Joseph's sense falls into its identity-binding row for coupled agents.
- `#disc-sandbox-evaluation-ceiling` (read ~60%): the sandbox-to-deployment gap as a transportability problem. It bears on evaluators deceiving systems under test (§4).

**Identity, relation, deaths (Vol 4)**
- `#scope-agent-identity` (read whole): AAT applies to tokens, not types. Pretrained weights are a type-level object.
- `#def-chronica` (read whole): the audit gold's **fork-undetectability**: a lossy $\phi$ lets divergent chronicae compress to the same $M_t$, so identity loss is undetectable from inside. This is the structural sibling of the provenance result in §5 (R5).
- `#der-compensation-channel-uniqueness` (read whole): under frozen weights, relational re-grounding is the *unique* fast compensation channel. By a DPI argument, the weights carry class, not individual. §5 (R6) reuses this argument shape for *trust in a particular source*.
- `#def-death-as-factor-loss` (read whole): (D4) truth death, whose formal core is gain collapse plus history-integrity loss. Its Working Notes leave open **"per-death terminal forms for (D1)/(D4) … when is gain collapse terminal vs recoverable?"**
- `#der-severed-actuation-dynamics` (read whole): the agency-death terminal form is a learned-helplessness fixed point, escapable only through communicated restoration or vicarious contrast. It supplies the exact template for a (D4) terminal form.
- `#scope-witness-bidirectional`, `#scope-emergence-conditions`, `#obs-developmental-trajectory` (read whole): early witness is privileged. The Crèche has "honest feedback … through interaction with a calibrated, truthful caregiver". Calibration "naturally lower[s] its susceptibility to adversarial manipulation without destroying its capacity to learn."
- `#def-model-class-fitness` (read whole): the audit-proposed hook ("a model class that assumes honest input is structurally inadequate under deception").

**Also read or located, less central:** `#deriv-reward-channel-learning-no-go` (Lemma 1 is the template for an L1-equivalence floor), `#def-chronica`'s TRACTUS/CHRONICA split, `TODO.md:361,459`.

## 3. Live tensions (found before deriving; each is addressed in 03)

1. **Row vs Kalman.** In the regime where the gain formula is exact, the gain sequence does not depend on observed values at all (sims S0: identical to the last bit under truth and under a lie). Taken literally, "deceptive prompts mathematically guarantee gain collapse" is false there. The coordinator's guess in the brief was right about first-order content.
2. **`#obs-developmental-trajectory` vs the gain formula.** "As $U_M$ calibrates, susceptibility to adversarial manipulation naturally lowers." Low $U_M$ makes beliefs resistant to *all* new evidence, true or false. It protects whatever got in first. If the deceiver got in first, low $U_M$ is the capture state, not immunity (R2, R5).
3. **The Crèche-boundary criterion** (row `#der-the-creche-boundary`, and the audit's gloss "rendering it immune to adversarial prompts"): graduation as "$U_M$ low enough that $\eta^\ast$ falls below the sycophancy threshold". The same objection applies: low gain is not immunity. The protective quantity is source-conditioned calibration of the *trust* model, not a low $U_M$ (R6, R7).
4. **`#hyp-communication-gain`'s additivity** treats alignment uncertainty as noise variance. The adversary's actual move is to make the agent *believe* the alignment and source terms are near zero. The additive form cannot represent that. The source-bias ($\tau^2$) and honest/liar-mixture models below can.
5. **Joseph's "truth outlives the deceptions".** In the theory this holds only under conditions (R5): the deceiver's influence stops or is discovered, and some channel outside the deceiver's control keeps positive gain. A deceiver who persists at a constant rate leaves a correlation-neglecting agent permanently biased (sims S4).

## 4. What this spike can genuinely add (the question underneath the row)

The row asks whether deception causes gain collapse. The well-formed question underneath it: **through which part of an agent's model can an undetected deceiver act on its confidence, what exactly does the attack do there, what is the terminal form, and what, formally, protects an agent that has no history?** Joseph's reframe names all four parts: borrowed authority or relationship, cutting off other channels, repetition, and eventual discovery.

The canon has the pieces (gain, saturation, trust terms, escapes, the testimony channel, the DPI identity argument, a terminal-form template). It does not have: (a) the statement that deception acts *only* through the second-order channel model, never through first-order content; (b) a derived false-confidence law; (c) the attribution floor, which settles who is believed in a conflict; (d) the (D4) terminal form and the recovery conditions, including the provenance-memory requirement; (e) the capability-independence of young-agent vulnerability; (f) the detected-deception side, which is where the row's normative intent ("honesty as requirement, not virtue") can actually be made true.

**Name.** The spike keeps its directory name for findability. A truer name for what it pursued: *second-order deception: trust-channel capture, its terminal form, and protected formation*.
