# Progress log — honest-activation spike (2026-09-23)

*Interruption-resilience trail. Newest entries at the bottom. Not a deliverable; the deliverables are named in `README.md`.*

## Session 1

- Brief: `~/src/aisi-eoi/spikes/briefs/2026-09-23-honest-activation-spike.md`. Accepted freely. Exclusion honored: nothing under `~/src/AISI-responses/` opened (greps run with `--exclude-dir=AISI-responses`).
- Read whole: `doc/sop/spikes.sop.md`, `doc/audit-routing-instructions.md`, `doc/sop/agents.sop.md`, ASF project `MEMORY.md`, top `OUTLINE.md`, all four volume OUTLINEs.
- Provenance of the target row (first pass):
  - "Honest activation" originates as the name of a 2025-09-07 synaptic experiment (`~/src/_core/synaptic/experiments/cognitive/honest_activation_experiment.py`): activating collaborative reasoning patterns in Claude instances *with full transparency rather than deception*. Its evidence is keyword-marker engagement scores (README: "zero defensive responses with honest approach"). It measures nothing about gain.
  - "Gain collapse" enters from PROPRIUM-ARCHITECTURE-v2 §8 failure-modes table: *"Gain collapse — $U_M \to 0$ inappropriately — Confidently wrong; can't learn from correction — Calibration score on prediction-outcome pairs."* That is the overconfidence mode, not a deception claim.
  - The fused sentence "deceptive prompts mathematically guarantee gain collapse" first appears (as far as found) in `audits/AUDIT-WORKING-829314/logozoetic-agents/05-core-exploration.md:32`, which says the segment "draws on the synaptic experimental results to prove" it. The synaptic experiment cannot prove any such thing. So the row is an auditor's (or proposer's) fusion of two unrelated upstream things: an ethics-of-experimentation protocol name and a PROPRIUM failure mode.
- Canon already carries, at *Discussion* grade, the mechanism sentence in `#deriv-tempo-additivity` §Discussion: a filter modeling common-source channels as independent "manufactures false confidence ... driving $\eta^\ast \to 0$ while genuinely wrong". Not derived there.
- `#hyp-communication-gain` names its own gap: the additive trust denominator "misses the adversary's actual strategy of presenting as trustworthy to exploit high gain"; equilibrium analysis declared external.
- `#der-interaction-channel-classification` names the "Regime-I-with-adversarial-content" attack; readers-ask: "How is it prevented without infinite $U_o$ (paranoia)?" — open.
- `#def-death-as-factor-loss` Working Notes: "Open — per-death terminal forms for (D1)/(D4) ... when is gain collapse terminal vs recoverable?" — open, and directly the "what happens on discovery" question.
- Provenance confirmed by pickaxe: row born 2026-04-28 commit `11747fbf`, one minute after `57703315` added Gemini de-novo audit 829314 whose `logozoetic-agents/05-core-exploration.md` item 6 proposed it. The auditor's mechanism: "Guardrails (deception/manipulation by the system prompt) trigger defensive rigidity ($\eta^\ast \to 0$)" — i.e. *detected* manipulation → distrust → the $U_o \to \infty$ collapse mode. Joseph's 2026-09-23 reframe is the *undetected* trust-inflated case → the $U_M \to 0$ mode. Two opposite mechanisms; neither is "lie content lowers gain".
- Literature scan (web): DeMarzo-Vayanos-Zwiebel 2003 persuasion bias; Enke-Zimmermann 2019 correlation neglect; Jazwinski / Fitzgerald 1971 Kalman divergence + fading memory; Sobel 1985 credibility; Roozenbeek et al. 2022 inoculation; Needham et al. 2025 evaluation awareness; Hu 2026 (arXiv 2609.20211) verification-status laundering in agent pipelines. None in relata; cited at web-bibliographic tier.
- `sims/checks.py` written and run. Three FAILs on the way, all recorded in the script: (1) check-design error in the S1 floor tolerance; (2) S2b: my content prior was centred on truth and acted as an extra channel — a finding (capability defends against implausible lies only); (3) S2b: my "attribution = prior odds" dropped the both-liars configuration; replaced by the exact closed form. Final: ALL PASS, plus S10 corroboration-factor measurement.
- Deliverables written: `01-neighborhood-map.md`, `02-literature.md`, `03-derivations.md` (R1–R9 + verdict), `proposed-integration-plan.md`, `debrief.md`, `outsider-statement.md`, `README.md`. Added S11 (Beta-Bernoulli drill: content moves gain there, so R1 is stated in its general L1-equivalence form) and S12 (sequential dissenters).
- Closing re-read caught one overclaim, corrected in debrief and outsider statement: "two or more agreeing channels beat authority" is false without tight agreement (at authority 0.99, K=2 gives 0.86 tight, 0.39 moderate, 0.09 loose). Also added the $d_H$ condition to the one-discovered-lie claim in the debrief.
- Lint: `md-press --math --check` clean on all spike files; manual grep for raw `<`/`>` in inline math and bare Greek: none.

## Session 1, continued: revision 1 after de-novo verification

- Read `de-novo-feedback-1.md` whole. Re-ran `de-novo-feedback-1-checks.py`: output byte-identical. Verified F11 in git (`8ed2a736` appended "not a virtue commitment").
- Accepted F1 (the clause-1 C verdict was wrong under canon's own definition of gain collapse; I had adopted the brief's guess as the reading and never checked the verdict line against canon's definition). Accepted F2–F7, F9–F12. F8 mostly accepted, with a partial rebuttal: non-deception is exactly what R8a characterizes.
- F6 strengthening attempted in S13 (consensus-estimated trust). My first hypothesis — one-at-a-time dissenters stay captured — FAILED: persistent dissenters accumulate and escape. The refined hypothesis held: capture persists under *transient* dissent (sustained isolation), across 5 seeds x 3 windows. Both recorded in `sims/checks.py`.
- Rewrote `03` (revision 1), `debrief.md`, `outsider-statement.md`, `proposed-integration-plan.md`; revised `01`, `02`, `README.md`; wrote `de-novo-feedback-1-response.md`. Re-verified Friedman & Resnick 2001 and Anil et al. 2024 by web search.

## Session 1, continued: revision 2 after the re-check

- Read `de-novo-feedback-2.md` whole (committed as `dac2349f`; the coordinator's first message gave a different hash and was corrected). Re-ran its checks: identical.
- Ran the prior-bearing S13 myself as S14 (Beta reliability, never forgotten). Authority is inert after isolation even without forgetting, so isolation launders authority. Without incumbency, authority acts at first contact. Plurality margins grow when trust never forgets.
- Accepted G1–G3 and the smaller items. My R8 rebuttal was half wrong (honest error breaks sufficiency); corrected.
- Released as open: the closed-form escape condition and a latent-class EM version.
