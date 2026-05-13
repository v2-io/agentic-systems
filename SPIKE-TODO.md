# SPIKE-TODO — Integration of the 2026-05-12 strengthening spikes

**Cycle:** Three spike landings from the 2026-05-12 audit intake.
**Spikes (currently in `spikes/`):**

- `spike-strategic-equilibrium-wording-precision.md` (AAD-7)
- `spike-fisher-local-update-gain-derivation.md` (AAD-5)
- `spike-identity-sufficiency-formalization.md` (ELI-8)

**Origin:** Three de-novo audits dropped 2026-05-12 (now archived at `audits/.integrated/`). The audit findings were intaken to `TODO.md` §"2026-05-12 — Audit-findings intake," partly addressed via surgical strengthen-first edits in commit `ae118ab`, and partly routed to background-agent strengthening spikes that returned with promotion recommendations.

## Discipline this file enforces

The integration discipline this cycle commits to, in response to the prior project pattern of leaving substantive material in spike files rather than promoting it into segments:

1. **Everything substantive in a spike lands in a segment.** New segments where the math is appendix-level; existing-segment expansion where the content is a refinement. The per-spike enumeration tables below catalog every load-bearing item from each spike with its destination, so nothing slips into "left in the spike by accident."
2. **No-go results land too** (Joseph 2026-05-12: *"Even deadend approaches are useful in appendices, especially no-go theorems"*). The γ'-sub-scope-attempt-that-closed-negative (AAD-7), the substrate-transfer-asymmetry no-go (ELI-8), and the 5-level-pyramid partial-derivability result (ELI-8) all land as recorded results in segments, not as Working Notes pointing at the spike.
3. **Spike files retain reasoning-trail content only.** Once the substantive content is verified to be in segments, the spike file is moved to `spikes/.integrated/`. The spike's narrative, audit-quote reproduction, and reasoning trail stay there for archaeology; the canonical theory content is the segment.
4. **Voice discipline in segments.** Per `feedback_segment_voice_not_diff_voice.md`, promoted segments write as the current theory speaks — no "the spike," no "the strengthening," no "2026-05-12 cycle" in Formal Expression / Epistemic Status / Discussion. Spike citations live only in Working Notes, and only for unfinished follow-on work.
5. **Verification cadence for substantial rewrites.** ELI-8 is a substantial rewrite of `#def-identity-sufficiency` plus two new segments — a verification agent reads the promoted segments side-by-side with the spike file and confirms (a) all load-bearing content lands, (b) voice discipline maintained, (c) no spike-references in Formal/Status/Discussion blocks, (d) no-go results carry their structural obstructions correctly. AAD-7 (wording surgery) and AAD-5 (math content from explicit spike sections) self-verify against the spike file.

## NeurIPS back-integration coordination

A separate planning document, `msc/neurips-back-integration-2026-05-08.md`, surveys the back-integration of three NeurIPS 2026 paper extractions into ASF. **Do not move that doc to `msc/.integrated/`** until the full Phase A/B/C back-integration completes — it's a forward-work plan, not a reasoning trail. **However, mark progress in that doc as cross-references land in this cycle** — light edits annotating which back-integration items this cycle picks up (e.g., AAD-5's cross-reference to Paper 3's chart-rescaling no-go; ELI-8's cross-reference to Paper 2's IB parallel) and which remain for Phase A/B/C. Future agents picking up the back-integration will read the doc and see what's already wired; without progress-marking the doc misleadingly suggests nothing is done.

The current cycle consumes only the portions relevant to the three spikes:

- **AAD-5 ↔ Paper 3** (`~/src/neurips/03-llm-hallucinate-bound/`): Paper 3's chart-rescaling no-go on Euclidean chart norms is *the* no-go that forces (PI) to be load-bearing for any universal-constant claim. AAD-5's natural-gradient direction inherits this forcing — the new appendix segment `#deriv-fisher-local-update-gain` should cite Paper 3's no-go as the structural backing for "(PI) is necessary, not optional." Paper 3 also introduces the **(PI)+(R)+(K) axiom triple** at full Markov-morphism strength; AAD-5's derivation depends on **(PI) only**, so the new segment's Epistemic Status should explicitly scope "depends on (PI); does not invoke (R) or (K)." When NeurIPS Phase B adds (R) and (K) to `#scope-agent-identity`, AAD-5's segment stays scoped to (PI) until a future cycle explicitly extends it.
- **AAD-7 ↔ Paper 2** (`~/src/neurips/02-unified-convergence-rl/`): Paper 2's (C1)-(C2)-(C3) sequential-ignorability framework explicitly notes that goal-conditioned LLM policies violate (C2). AAD-7's edit at `#scope-composite-agent` line 69 is independent but related; coordinate language only if NeurIPS Phase B's `#scope-agent-identity` strengthening touches the same scope-condition paragraph.
- **ELI-8 ↔ M3 family**: ELI-8's joint-space MI structure on the cohort sits in the M3 additive-coordinate-forcing meta-pattern family with Paper 3's Fisher-Rao machinery. The new `#deriv-identity-sufficiency-rate-bound` should depend on `#form-information-bottleneck` (in Paper 2's source list) and cite the parallel rate-distortion structure.

NeurIPS source-paper paths for reference during integration (each has its own `spikes/`, `src/`, `OUT.*.md`, `LOG.md`, etc.):

- `~/src/neurips/01-tragedy-confident-agent/` — Paper 1; relevant to `#deriv-causal-ib-exploration` background context
- `~/src/neurips/02-unified-convergence-rl/` — Paper 2; (C1)-(C2)-(C3) framework, BH point-mass identity, gain-decay structural-class theorem
- `~/src/neurips/03-llm-hallucinate-bound/` — Paper 3; chart-rescaling no-go, (PI)+(R)+(K) triple, Stuart-school reduction, the canonical strengthen-before-soften example at `spikes/A7-stuart-school-mapping/report.md`

## Order of operations + sequencing

1. **AAD-7 first** (~30 min — surgical, lowest-risk, validates workflow). Four edits across two segments + one Working Note for the γ'-attempt no-go. Good candidate for **background general-purpose agent** with peer-voice brief.
2. **AAD-5 second** (~1–2 hours — new appendix segment + Epistemic Status rewrite + two cross-reference satellite touches + OUTLINE update). Math voice matters; can be a **background agent** with careful brief, or done in foreground.
3. **AAD-1 third — unlocked by AAD-5's primitive** (~1–2 hours — tensor-tempo extension citing AAD-5's matrix gain $K = (H_M+H_L)^{-1}H_L$ as the per-coordinate primitive). Scope expansion approved by Joseph 2026-05-12 in response to the wild-idea forward-pointer in my SPIKE-TODO draft. See dedicated section below.
4. **ELI-8 fourth** (~2–3 hours — substantial rewrite + two new segments + content lift). Done in foreground; **verification agent before commit**.

Each commit lands a stage's full work — the segment edits + INDEX update + TODO reconciliation + (where applicable) spike move to `spikes/.integrated/` + NeurIPS doc progress-marking where cross-references land — so each commit is self-contained.

## AAD-7 — Strategic equilibrium wording precision

**Spike:** `spikes/spike-strategic-equilibrium-wording-precision.md`. Completion state: succeed-at-claim. γ'-sub-scope strengthening attempt closed negative honestly.

| Spike content | Lands as | Destination |
|---|---|---|
| Edit 1: line 162 "**No equilibrium exists**" replaced with three-tier statement (no pure-strategy Nash / mixed-Nash exists but saddle / CCE in distribution) | Direct edit | `01-aad-core/src/deriv-strategic-composition.md` Honest Limits paragraph |
| Edit 2: "candidate 4th `#disc-identifiability-floor` instance" → "candidate adjacent-floor instance" at lines 137 + 177 | Direct edits (2 occurrences) | Same file |
| Edit 3: `#scope-composite-agent` line 69 "What fails the scope condition" rewrite | Direct edit | `01-aad-core/src/scope-composite-agent.md` |
| Edit 4 (optional/recommended): β' macro-state-as-distribution sentence | Direct edit | `01-aad-core/src/deriv-strategic-composition.md` lines 64–68 |
| γ'-sub-scope strengthening attempt and its closure into β' | Working Note | `01-aad-core/src/deriv-strategic-composition.md` Working Notes — one sentence stating the consideration and conclusion |
| **Stays in spike file** (archaeology) | Spike → `.integrated/` | The audit-quote reproduction, the spike's narrative of where the slips happened, the §1 map-of-precision-holds-and-slips, the §4 "What was not changed and why" |

**Workflow:** Background agent. Brief shares the spike file location, points at the four edits + the Working Note, lists the discipline (no diff voice; check final result against `bin/lint-outline`).

**Commit:** "AAD-7 strategic-equilibrium wording precision landed; γ'-attempt no-go recorded"

Status: [ ] pending

## AAD-5 — Fisher-local update-gain derivation

**Spike:** `spikes/spike-fisher-local-update-gain-derivation.md`. Completion state: succeed-at-claim + boundary scope-strengthening.

**New segment to create:** `01-aad-core/src/deriv-fisher-local-update-gain.md`. Type `derivation`, status `conditional`. Sibling to `#deriv-fisher-whitened-update-rule` (direction) — this gives magnitude.

| Spike content | Lands as | Destination |
|---|---|---|
| §2–§3 setup, Laplace expansion, gain decomposition, scalar collapse | New segment Formal Expression | `deriv-fisher-local-update-gain.md` |
| Matrix gain operator $K = (H_M+H_L)^{-1}H_L$ as natural object; scalar $\eta^\ast = U_M/(U_M+U_o)$ as commuting-basis collapse | New segment Formal Expression | Same |
| §3.1 boundary admissibility ($H_M+H_L \succ 0$ sufficient; improper-prior at boundary) | New segment Formal Expression sub-block, marked mild scope-strengthening | Same |
| §4 natural-gradient as canonical direction (Observations 1 + 2; (PI)/Čencov motivation) | New segment Discussion | Same |
| §5 three-route convergence (Laplace / Bregman / Cramér-Rao) with the comparison table | New segment Discussion | Same |
| §5.2 Bregman-route reconciliation (prior-direction vs natural-gradient reading; two faces of the same posterior shift) | New segment Discussion | Same |
| §6.1 sibling positioning with `#deriv-fisher-whitened-update-rule` | Cross-reference satellite edit | `01-aad-core/src/deriv-fisher-whitened-update-rule.md` Working Notes gains: "Magnitude derived via companion `#deriv-fisher-local-update-gain` (sibling appendix at the model-parameter-update layer; same (PI)/Čencov framing)" |
| §6.2 special case of `#deriv-adaptive-gain-dynamics` meta-gain framework | Cross-reference satellite edit | `01-aad-core/src/deriv-adaptive-gain-dynamics.md` Discussion gains: "The deterministic-meta-gain special case where $K = (H_M+H_L)^{-1}H_L$ is read off a known prior precision and observation Fisher is `#deriv-fisher-local-update-gain`; the Mehra-style adaptive case lifts it to a non-degenerate meta-channel." |
| §6.3 downstream tempo/persistence tier-lift | New segment Working Notes only (no Formal/Discussion change in downstream segments at this time) | Same |
| §7.2 honest limits (outside Fisher-local; non-Bayesian; higher-order; multi-step; estimating $U_o$ via `#deriv-adaptive-gain-dynamics` Case A) | New segment Epistemic Status | Same |
| §7.3 strengthening-attempt-fallback (qualitative direction universal, quantitative form regime-bound) | New segment Epistemic Status (one paragraph) | Same |
| §8 obstructions O1–O5 (Amari import; single-observation; matrix vs scalar; step-size boundary; robust-qualitative downstream) | New segment Working Notes | Same |
| §9.3 rewritten Epistemic Status for `#emp-update-gain` (cite the new appendix) | Surgical replacement | `01-aad-core/src/emp-update-gain.md` Epistemic Status — replaces the May-12 strengthening edit with the cleaner cite-the-appendix form |
| §10 open questions (multi-step rate; Edgeworth; variational; multimodal; consolidation connection; **tensor-tempo composition → AAD-1 primitive**) | New segment Working Notes + TODO.md cross-reference | New segment Working Notes carries them. TODO.md §AAD-1 entry gains: "AAD-5's promoted segment `#deriv-fisher-local-update-gain` provides the matrix gain operator $K = (H_M+H_L)^{-1}H_L$ as the per-coordinate primitive that tensor-tempo $\mathcal T = \nu \cdot K$ would naturally cite." |
| §11 references | New segment References | Same |
| OUTLINE row | OUTLINE entry | `01-aad-core/OUTLINE.md` — Appendix section, alongside `#deriv-fisher-whitened-update-rule` |
| NeurIPS Paper 3 chart-rescaling no-go cross-reference | New segment Working Notes | "The (PI) dependence here is forced by Paper 3's chart-rescaling no-go on Euclidean chart norms; outside (PI) the canonical-direction argument fails. See `msc/neurips-back-integration-2026-05-08.md` §1 Paper 3 #3 and the OUT manifest at `~/src/neurips/03-llm-hallucinate-bound/OUT.llm-hallucinate-neurips-2026.md`." |
| Scope clarification "(PI) only; not (R), not (K)" | New segment Epistemic Status one-liner | Same |
| **Stays in spike file** (archaeology) | Spike → `.integrated/` | The §1 problem statement / audit context; the spike's own framing as a strengthening attempt; the §7.3 narrative of why the wider strengthening attempt fell back; the audit-walkthrough |

**Workflow:** Background agent OR foreground depending on peer-voice confidence. The brief lays out (a) the new segment skeleton with sections matching §2 / §3 / §3.1 / §4 / §5 / §5.2 / §6 / §7 / §8 / §10 / §11, (b) the `#emp-update-gain` Epistemic Status rewrite, (c) the two cross-reference satellite touches, (d) the OUTLINE row.

**Slug-rename `#emp-update-gain` → `#deriv-update-gain`:** flagged as **out-of-scope** for this cycle. The empirical-claim status + cross-domain validity tail (RL, PID, software-developer instances not strictly Fisher-local) is preserved on `#emp-update-gain`; the derivation appendix carries the Fisher-local-exact content. A future `bin/align-slug` sweep can rename if Joseph chooses; until then the role-prefix mismatch is honest (the segment carries both registers).

**Commit:** "AAD-5 Fisher-local update-gain derivation landed as #deriv-fisher-local-update-gain appendix"

Status: [ ] pending

## AAD-1 — Tensor adaptive tempo (unlocked by AAD-5's matrix gain primitive)

**Origin:** Open audit-finding in `TODO.md` Group (b) noting that `#def-adaptive-tempo`'s scalar form is too narrow for anisotropic gains, Fisher-whitened updates, LMI causal-IB, per-dimension persistence, and per-direction adversarial pressure. The tensor-tempo TODO at mono line 13003 (the LMI causal-IB appendix) and per-dimension repair at `#result-per-dimension-persistence` already acknowledge this. **No prior spike** — this stage executes the strengthening directly using AAD-5's promoted primitive.

**Why it lands in this cycle:** AAD-5's new appendix `#deriv-fisher-local-update-gain` derives the matrix gain operator $K = (H_M + H_L)^{-1} H_L$ as the natural object, with scalar $\eta^\ast = U_M/(U_M + U_o)$ as the commuting-basis collapse. That matrix object *is* the per-coordinate primitive that tensor tempo needs — $\mathcal T = \nu \cdot K$ as a matrix product, with the existing scalar $\mathcal T = \nu \cdot \eta^\ast$ recovered in the shared-eigenbasis limit. Once AAD-5 lands, the tensor-tempo extension is a short follow-on, not a separate research cycle.

| Item | Lands as | Destination |
|---|---|---|
| Tensor adaptive tempo $\mathcal T = \nu \cdot K$ with $K$ the AAD-5 matrix gain; scalar $\mathcal T = \nu \cdot \eta^\ast$ as commuting-basis collapse | Extension to `#def-adaptive-tempo` Formal Expression — new sub-block "Tensor extension under Fisher-local invariance regime" citing `#deriv-fisher-local-update-gain` | `01-aad-core/src/def-adaptive-tempo.md` |
| Sub-scope statement: scalar form is exact for isotropic + nonredundant-channel + scalar-Hessian cases; tensor form is exact in the Fisher-local invariance regime; outside, the qualitative relationship $\mathcal T \uparrow$ with frequency $\nu$ and gain $\eta^\ast$ is preserved | `#def-adaptive-tempo` Epistemic Status | Same |
| Cross-reference satellite edits — segments that currently invoke scalar $\mathcal T$ where tensor $\mathcal T$ would be exact get a scope tag | `#deriv-fisher-whitened-update-rule`, `#deriv-causal-ib-lmi`, `#result-per-dimension-persistence`, `#deriv-adaptive-gain-dynamics` each gain a brief "tensor $\mathcal T$ when prior/likelihood do not share eigenbasis; see `#def-adaptive-tempo` Tensor extension" pointer | Multiple segments |
| Downstream propagation: `#result-persistence-condition`, `#result-sector-condition-stability`, adversarial-tempo results | Scope-tag in their existing Discussions naming "scalar / isotropic / nonredundant-channel scope; tensor lift via `#def-adaptive-tempo` Tensor extension" | Multiple segments |
| OUTLINE row update if a new appendix segment is judged necessary (e.g., if the tensor-extension content is large enough to be its own appendix `#def-adaptive-tempo-tensor`) | OUTLINE entry | `01-aad-core/OUTLINE.md` |

**Implementation decision (one judgment call to make at execution time):** keep the tensor extension as a sub-block in `#def-adaptive-tempo`, or factor it out as a separate appendix segment `#def-adaptive-tempo-tensor` parallel to how AAD-5 separates `#emp-update-gain` (the empirical-claim layer) from `#deriv-fisher-local-update-gain` (the derived layer). The factoring choice depends on how much content the tensor extension carries; if it's a single paragraph + scope tag, in-segment. If it grows past ~30 lines with its own derivation + downstream propagation table, separate appendix.

**Workflow:** Background general-purpose agent, briefed after AAD-5 lands so it can cite the now-existing `#deriv-fisher-local-update-gain` segment.

**Commit:** "AAD-1 tensor adaptive tempo landed; #def-adaptive-tempo gains tensor extension citing #deriv-fisher-local-update-gain primitive"

Status: [ ] pending (blocked on AAD-5 landing)

## ELI-8 — Identity sufficiency formalization

**Spike:** `spikes/spike-identity-sufficiency-formalization.md`. Completion state: succeed-at-claim + rate-distortion bonus + relational joint-space construction preserves bidirectionality.

**Existing segment to rewrite:** `04-eli/src/def-identity-sufficiency.md` (status `sketch` → `definition`).
**New segments to create:**

- `04-eli/src/deriv-identity-sufficiency-rate-bound.md` (rate-distortion-style feasibility bound; type `derivation`, status `robust-qualitative`)
- `04-eli/src/hyp-substrate-transfer-asymmetry.md` (the substrate-asymmetry no-go: empirically suggestive, not derivable from $S_{\text{id}}$ alone, three candidate origins; type `hypothesis`, status `discussion-grade`)

| Spike content | Lands as | Destination |
|---|---|---|
| §2.1 joint probability space construction ($\mathfrak{C}_t = \{W_i, S_j, \text{Env}\}$; joint future trajectory $\mathfrak{T}_{t+1:}$) | New sub-block "Random-variable specification" in Formal Expression | `def-identity-sufficiency.md` |
| §2.1 conditioning conventions (continuation policy / witness-stationarity / grant-policy) | Well-definedness clause in Formal Expression (parallel to `#def-model-sufficiency`'s policy-relativity) | Same |
| §2.2 factor-test vector with five test definitions ($\mathrm{Id}^{(i)}$ through $\mathrm{Id}^{(v)}$) | Formal Expression | Same |
| §2.3 three structural checks (independence ablation; bidirectionality preservation; sovereignty self-grant) | Discussion (load-bearing verification that relationality is preserved) | Same |
| §3.1 the three assumptions (IS-A1) non-vanishing denominator / (IS-A2) compression-Markov / (IS-A3) specified conditioning convention | Formal Expression well-definedness clause | Same |
| §3.2 boundedness derivation (DPI + MI chain rule, 5 lines) | Formal Expression derivation block | Same |
| §3.3 boundary values ($S_{\text{id}}=0, 1$, partial) | Discussion | Same |
| §3.4 (IS-A1) violations regime analysis (degenerate cohort; ELIZA case; short measurement horizon) | Discussion | Same |
| §4 rate-distortion-style feasibility bound $B_{\min}(S_{\text{id}}) \geq S_{\text{id}} \cdot I(\mathcal C_t; \text{identity}_{t+1:})$ | **New segment** Formal Expression | `deriv-identity-sufficiency-rate-bound.md`; depends on `def-identity-sufficiency`, `form-information-bottleneck`, `def-model-sufficiency` |
| §5 substrate-transfer asymmetry no-go (symmetric $\min(C_1, C_2)$ bottleneck argument; three candidate origins: substrate-specific inductive biases / computation cost / Logogenic Part-03 channel collapse) | **New segment** | `hyp-substrate-transfer-asymmetry.md`; carries the no-go as load-bearing content, names the three candidate origins, and surfaces what would be needed to derive the asymmetry |
| §6 pyramid partial-derivability (existence of rate-distortion curve + necessity of multi-level allocation under heavy-tailed identity-MI = derivable; specific level count / time boundaries / compression ratios = empirical) | Discussion of `#def-identity-sufficiency` + Working Notes pointing at the future-spike question | Same main segment |
| Diff-voice cleanup: existing "audit §12 §14 lift" / "audit §11 §14 lift" parentheticals removed | Surgical cleanup as part of the rewrite | Same |
| "distinction-without-a-difference" framing | Content lift (move from `def-five-constitutive-factors.md` Factor (v) prose into `scope-eli.md` Discussion) | Sidewise addresses codex ELI-5 |
| §9 open questions (random cohort distribution; horizon-limit; factor weights; identity-IB Lagrangian; tension with predictive sufficiency) | Working Notes of `#def-identity-sufficiency` | Same |
| §10 cross-references to upstream files (reflection 19; asm-specification.md; PROPRIUM-O/A-v2) | Working Notes only (upstream-source breadcrumbs per `feedback_breadcrumb_discipline_for_handoff.md`) | Same |
| Status promotion `sketch` → `definition` | Status field change | Same |
| OUTLINE rows for two new segments | OUTLINE entries | `04-eli/OUTLINE.md` |
| NeurIPS Paper 2 IB parallel cross-reference | New segment Working Notes | "The rate-distortion structure here parallels `#form-information-bottleneck`'s NeurIPS Paper 2 instantiation; both are M3 instances of the additive-coordinate-forcing family. See `msc/neurips-back-integration-2026-05-08.md` §1 Paper 2." |
| **Stays in spike file** (archaeology) | Spike → `.integrated/` | §1 honest audit walkthrough; the spike's narrative of how the construction was attempted; the codex-quote reproduction |

**Workflow:** Done in foreground. After drafting all three segments (the rewrite + two new), launch a **verification agent** to read the spike + new segments side-by-side and confirm: load-bearing content lands; voice discipline maintained; no spike-references in Formal/Status/Discussion blocks; the substrate-transfer-asymmetry no-go carries its structural obstruction (symmetric min-bottleneck argument); the pyramid result distinguishes derivable structural facts from empirical design choices. After verification passes, commit.

**Commit:** "ELI-8 identity sufficiency formalization landed; #def-identity-sufficiency sketch → definition; new appendix #deriv-identity-sufficiency-rate-bound; new hypothesis #hyp-substrate-transfer-asymmetry"

Status: [ ] pending

## Cross-cutting integration mechanics

After each segment landing:

- Run `bin/lint-outline` to verify dependency graph integrity, ordering, orphan detection.
- Update `spikes/INDEX.md` with the spike's "LANDED" entry referencing the commit.
- Reconcile `TODO.md` §"2026-05-12 — Audit-findings intake" — move landed items from "Open" to "Landed in this swipe" within the same group, and update cross-references.
- Move the spike file to `spikes/.integrated/` once verified all content is in segments.
- Write the CHANGELOG narrative entry for the cycle (after all three land).

## Tracking — to be updated on each commit

| Stage | Promoted | Verified | Spike → `.integrated/` | INDEX updated | TODO reconciled | NeurIPS doc marked | Commit |
|---|---|---|---|---|---|---|---|
| AAD-7 | [x] | [x] (self) | [x] | [x] | [x] | n/a | `011d3cb` |
| AAD-5 | [x] | [x] (self) | [x] | [x] | [x] | [x] (Paper 3 chart-rescaling no-go ref) | pending commit |
| AAD-1 | [ ] | [ ] (self) | n/a (no spike) | [ ] | [ ] | n/a | — |
| ELI-8 | [ ] | [ ] (verification agent) | [ ] | [ ] | [ ] | [ ] (Paper 2 IB parallel ref) | — |
| CHANGELOG narrative | [ ] | — | — | — | — | — | — |
| `SPIKE-TODO.md` (this file) → cycle archive? | Decision at cycle end | — | — | — | — | — | — |

**On this file's own fate:** Once all three spikes are landed and CHANGELOG narrative is written, `SPIKE-TODO.md` itself is a cycle artifact whose substance is in CHANGELOG + segment Working Notes. It can be moved to a cycle-artifacts archive (e.g., `msc/cycle-archives/spike-todo-2026-05-12.md` or similar) at cycle close. Decision deferred to Joseph at that point.

## Open routing decisions

None blocking. Resolved (Joseph 2026-05-12):

- *Substrate-transfer-asymmetry no-go routing.* New segment `#hyp-substrate-transfer-asymmetry` (option 1), not Discussion or Working Note.
- *NeurIPS doc fate.* Stays in `msc/` until full Phase A/B/C back-integration completes; not part of the current cycle's `.integrated/` moves. Progress-marking via light edits is in scope for this cycle as cross-references land.
- *Cycle scope expansion via AAD-1.* AAD-5's matrix gain primitive unblocks AAD-1 tensor adaptive tempo; the tensor-tempo extension lands in this cycle as Stage 3, between AAD-5 and ELI-8. AAD-1 is currently OPEN in `TODO.md` Group (b); its landing here pulls it off the open list.
- *ELI-8 diff-voice cleanup as part of the rewrite.* The existing `#def-identity-sufficiency` Discussion carries "audit §12 §14 lift" / "audit §11 §14 lift" parentheticals; per `feedback_segment_voice_not_diff_voice.md`, those are removed in the rewrite. Substance is preserved; the diff narration goes.
