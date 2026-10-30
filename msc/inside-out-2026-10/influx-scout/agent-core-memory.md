# Memory scout: `~/src/agent-core/memory/` and `~/src/agent-core/msc/`

KR3.1 (feeds KR3.3). Terminology items also feed KR2.5; external-literature items feed KR2.4.

*Scout pass, 2026-10-30, Opus 5.5. Every canon claim below was checked against `~/src/arch/asf/0*/src/` at `5ade664d` (2026-08-24, the last segment commit; the working tree has no segment changes). The corpus's ASF reading (`research/asf_bridge.md`) is dated 2026-10-27, so it read the same canon I checked. Line numbers refer to that tree.*

## 0. What this corner is, and dates

- **`memory/`**: a course on human and machine memory models, written in one day (2026-10-27) by one Opus 5.5 instance for Joseph. It has reference lessons `00`–`17` (plus `09b`, `12b`, `A1`), a narrative `P1-the-story.md`, an interactive Ladder (`tutorial/`), ledgers (`PHENOMENA.md`, `ENGINEERING.md`, `GLOSSARY.md`), code (`code/memlab/`), and eight raw research notes (`research/`, about 570 KB). Git history: `9d0db1d` (2026-10-28 13:38, first commit), `7311e4d` (Ladder split), `de70ef5` (2026-10-28 15:38, fixes after a first full read).
- **`msc/`**: experiential reading notes on every lesson, written by a second Opus 5.5 instance on 2026-10-28, plus `memory-reading-synthesis.md` and `HANDOFF.md`. Committed in `27458ca` (2026-10-28 21:05). HANDOFF still says `msc/` is untracked and asks for Joseph's consent before committing, because agent-core is public and the notes discuss Joseph, the estate and ASF. The commit came after HANDOFF was written. Whether Joseph authorized it is worth confirming, but it is outside KR3.1.
- **The ASF-bearing core** is `research/asf_bridge.md` (557 lines, 2026-10-27). It quotes segments verbatim, carries their status and stage, and rates every memory-to-AAT correspondence strictly as identity / formal analogue / loose analogy / none. Lesson `15-asf-and-memory.md` (99 lines) distills it. Lessons 01, 06, 08, 09b, 10, 11, 12, 12b and 17 each carry a "Bridges" or AAT section built on it.

## 1. The single most useful instrument for "what is being theorized"

**`research/asf_bridge.md` §2–§3** (lines 290–396). §2 places each AAT surprise and information quantity at its level (residual, likelihood gradient, normalized magnitude, mutual information) and says whether it is pointwise. §3 is a two-way correspondence table with strict ratings. Read together, they give the clearest outside statement I have seen of what AAT's memory machinery *is*:

- an uncertainty-weighted (Kalman/RLS) adaptive estimator with exponential forgetting;
- a survival inequality (the persistence condition);
- a CLS-shaped necessity argument for offline consolidation;
- an information-bottleneck objective.

It is **not** a theory of retrieval, segmentation, trace interference or pointwise surprise; those are rated "none". This is Joseph's "clarity on what is being theorized" concern, answered from outside. I'd recommend that whoever does KR3.3 treat this table, not the flag list, as the primary clarity instrument. Possible landing: a Discussion paragraph in `form-agent-model` or a chapter-end `impl-*` segment that says what the machinery is in standard terms. Argument for setting it aside: it is an external reading, and its ratings are judgment calls. Even so, the ratings I spot-checked held up.

## 2. Items by provenance class

The KR3.3 action differs by class: (a) already in canon's own Working Notes but never landed, so it is integration debt, not a discovery; (b) new to canon, verified by me; (c) a corpus claim I found incomplete, or that canon partly answers already; (d) synthesis proposals at their stated credence.

### (a) Already in canon's Working Notes, never landed

**A1. `form-consolidation-dynamics`: scope condition, replay versus retrieval, and "all finite-budget agents".** The Working Notes at line 186 (Codex/526815 F74–F77) already say three things:
- $\nu_{\text{consol}}\ll\nu_{\text{online}}$ is too strong, because offline replay rate can exceed event rate;
- $I(e^{\text{replay}}\mid M_{\tau^-})=0$ holds only for internally generated replay, not for archive or re-read retrieval, which is "a channel from auxiliary memory into active $M$";
- "all finite-budget agents require consolidation" overstates the case.

The body has not changed. The scope condition is at line 46 and in the table at line 92 ("Derived"). "All finite-budget agents require consolidation" is still at lines 24 and 84. The definition at line 20 lists "re-read paragraphs" and "replay buffers" as pseudo-events, and line 22 then asserts zero new information under C3, so the body contradicts its own Working Note.

*Biology:* the bridge note (line 164) adds that hippocampal replay is time-compressed and fast during sharp-wave ripples, so the scope condition reads the biology backwards. None of the research notes source that claim; my grep found only D'Argembeau 2021 on temporal compression in episodic recall. It is true, but in this corpus it rests on the author's own knowledge.

*Canon change, and a strengthen route rather than a soften (my inference, unverified):* the quantity that nesting actually constrains is the rate of change of $M^{\text{slow}}$, not the count of pseudo-events. `der-multi-timescale-stability` (exact, draft) already has that object: $\epsilon$ multiplies the slow level's vector field, and (C1) gives $\epsilon_{\max}$ in closed form. Many small replay steps make a slow slow-level drift. Restating the scope condition as (C1) on the slow sub-state would remove the biology objection without weakening anything. `form-consolidation-dynamics` currently has **zero** references to `der-multi-timescale-stability` (grep count 0). It depends only on the qualitative `der-temporal-nesting`.

**A2. `form-event-driven-dynamics`: $\mathcal I(e)$ is a mutual information, but the prose uses it as one event's surprise.** The Working Note at line 102 says so and gives three independent substrates. Line 17 of the body still says it "measures, for any individual event, the mutual information…". The corpus adds the standard identity: $I(E;\Omega\mid M)=\mathbb E_e[D_{\mathrm{KL}}(p(\Omega\mid e,M)\,\Vert\,p(\Omega\mid M))]$, which is *expected* Bayesian surprise (Itti & Baldi; lesson 08 Q3 derives it). Canon change: one clause in Epistemic Status, plus a separately named realized Bayesian surprise if downstream segments need a per-event quantity.

**A3. `def-chronica`: the TRACTUS/CHRONICA split, and access to the record** (Working Notes at lines 42–51 and 94). This is the canon-side hook for item B4.

**A4. `def-mood`: the "Behrens-style" link is marked unverified** (Working Note at line 55). The corpus proposes Pearce & Hall 1980 and Behrens et al. 2007. See C2 for a refinement.

### (b) New to canon, verified against the segments

**B1. $\lambda$ carries at least five meanings, and one segment uses two of them.** The corpus reports two: integration rate in `def-mood` and `der-mood-timescale`, and retention factor in `schema-strategy-persistence`, `form-consolidation-dynamics` and `deriv-update-detection-latency`. I found more:
- **log-odds natural parameter** $\lambda = \log(p/(1-p))$ in `deriv-edge-update-natural-parameter`, and $\lambda_k$ in `der-interaction-channel-classification` and `disc-credit-assignment-boundary`;
- **generalized eigenvalue** in `deriv-matrix-persistence-condition`;
- $\lambda_{\text{surv}}$ in `disc-anti-collapse`, and $\lambda_{ij}$ in `def-strategic-tempo`;
- **exploration–exploitation weight** $\lambda(M_t)$ in `def-causal-information-yield`. This is the **only** $\lambda$ entry in `NOTATION.md` (line 125).

**`deriv-update-detection-latency` uses $\lambda$ as the edge log-odds coordinate (lines 29–43: $\Delta\lambda_{\text{detect}}$, $\lambda_k^{\text{new}}$) and as the forgetting retention factor (line 65: $n_{\text{eff}}=1/(1-\lambda)$) in the same derivation.**

*Which one to rename (a check for KR2.5, not a verdict):* `schema-strategy-persistence` line 133 already cites Ljung 1987 (discounted least squares) as the formal antecedent. In recursive least squares the standard symbol for the forgetting factor is $\lambda$, with $1/(1-\lambda)$ the memory length. So the forgetting-side usage matches the field's convention. Mood's $m_t=(1-\lambda)m_{t-1}+\lambda a_t$ is an exponential moving average. Its smoothing constant is conventionally $\alpha$, but $\alpha$ is taken in AAT by the sector rate; Pearce–Hall uses $\gamma$. So the mood side, and the log-odds coordinate, are the likelier rename targets. Any derivation that composes mood with the forgetting machinery should be rechecked. The `msc/15` reading note (§2c) argues this could flip the sign of a stability argument. I have not verified that.

**B2. `form-consolidation-dynamics` contradicts itself on which store holds what.** Line 22 says "hippocampus-like fast + neocortex-like slow", which is the CLS assignment. Line 56 says the sub-states "capture cross-episode regularities versus verbatim traces respectively" after listing fast then slow, which assigns regularities to the fast store. Canon change: swap the order at line 56. This is a straightforward fix.

**B3. LEXICON's feasibility-window definition disagrees with the segment.** The source is `terminology/entries/stability-plasticity-feasibility-window.md`. LEXICON.md is generated, so edit the entry and rebuild. LEXICON line 106 says "interval of **consolidation rates**", while the segment and the entry's own line 18 say the range of $\lambda$, a forgetting rate. Possibly worth more than a wording fix (my inference): `impl-scaffolded-logogenic` asserts a *lower* bound on consolidation cadence, and `form-consolidation-dynamics` asserts an *upper* one ($\nu_{\text{consol}}\ll\nu_{\text{online}}$). Together those would make a second window, on cadence, and LEXICON may be describing that one. Two windows may be conflated under one name.

**B4. Canon already has an object outside $M_t$.** `disc-deferred-observation-processing` (03-llm-core, discussion-grade), lines 15–22, introduces a buffer $B_t$ whose contents are "*not yet* part of $M_t$". Line 51 adds that "retrospective attention" is "a capability the arrival-time-collapsed formalism cannot express at all." That is the canon precedent the corpus's main structural proposal needs. The proposal (lesson 15 §2.1) is an archive outside $M_t$ read through a cue-driven reinstatement operator $R$. The corpus argues for it from first principles and does not notice that canon already opened the door. The tension it resolves is real and checkable:
- `def-proprium-mapping` lines 17–22 place CHRONICA ("raw, uncompressed … $\mathcal C_t$") and MEMORATA ($\phi(\mathcal C_t)$) both under "Persistent State (PRINCIPIA $\approx M_t$)";
- `form-agent-model` line 41 defines $M_t=\phi(\mathcal C_t)$ as a many-to-one compression;
- `der-recursive-update` derives Markov recursion from completeness, and uses "would need to consult $\mathcal C_t$ directly" as a reductio.

Read together, PROPRIUM's mapping makes $\phi$ lossless. Canon changes it would touch: `def-proprium-mapping` (move CHRONICA to an accessed archive), `form-agent-model` (completeness scoped to *active* state), `der-recursive-update` (a read operation added to $g_M$), and possibly a new formulation segment for reinstatement. Argument for caution: completeness is definitional and load-bearing for the Markov result, so the change means restating it, not deleting it. The `msc/15` reading note calls this "the most consequential single item in the course for Joseph"; I agree.

**B5. The compensation-channel uniqueness premise.** The worked analysis already exists at `~/src/agent-core/plugins/sidecar/notes/asf-parallels/05-compensation-channel-dispute.md` (2026-10-05). Use it; I did not redo it. The textual hook I verified is `der-compensation-channel-uniqueness` line 19: $f_{\text{init}}$ has "exactly three inputs: the store $\mathcal E_k$, the new prompt / environment $p_{k+1}$, and the weights", where $\mathcal E_k$ is described as the entity's own *compressed* store. `der-identity-continuity-threshold` line 36 says "self-replay cannot reduce the gap … re-reading its own compressed store". If $\mathcal E_k$ is the full record with pointer access, then $B_k\ge I(\mathcal C;Y)$ and $\rho_k=0$ by the segment's own definition $\rho_k=(I(\mathcal C^-_{\tau_k};Y)-B_k)_+$. The ratchet then never starts. Three independent sources converge on this:
- the Codex Working Note quoted in A1 (archive retrieval is a channel into $M$);
- sidecar 05;
- lessons 09b §6 and 12b ("a fold that can be re-cut needs the full record kept recoverable").

Together with B4 this is one structural question: does the formalism have a read-the-record operation?

**B6. "REM sleep has a Shannon floor" composes two quantities of different types** (my inference, from reading both segments). `impl-scaffolded-logogenic` lines 42–46 derive a consolidation-cadence floor from the persistence information-rate floor. That floor, in `deriv-persistence-cost` line 38, is a rate at which the agent "must acquire information **from observations**". Under `form-consolidation-dynamics`'s own C3, replay pseudo-events carry zero new external information. So an acquisition floor cannot bound offline cadence. The corpus flags only the empirical side: the "<4 hours" figure is uncited, and human TMR effects appear in NREM, not REM (Hu et al. 2020; `research/dreams_nrem_rem.md`).

*Strengthen route (my sketch, unverified):* a real floor plausibly exists as a **drain-rate** condition. A finite fast store that is overwritten must be drained into the slow store at least as fast as cross-episode-relevant information arrives. That is a queue-stability condition, and AAT already has Lindley machinery for it (`result-sector-persistence-template`, `der-identity-continuity-threshold`). The same argument would also supply the missing stability upper bound $\phi(\cdot)$ on forgetting, whose candidate form in the `form-consolidation-dynamics` WN at line 162 is already drain-shaped.

**B7. Two catastrophic-forgetting accounts that don't reference each other.** One is the empty $\lambda$ window in `form-consolidation-dynamics`, which cites French 1999. The other is the (C2) violation with $L_{21}$ too large in `der-multi-timescale-stability`. A third reading, "gain too high", is in a pre-AAT ref doc. Neither segment cites the other. Separately, French 1999 is a review of interference under sequential training and its remedies (`research/consolidation_schemas_maps.md` line 32); it does not describe a forgetting-rate window, so "analogous to" is the honest citation form. Of the two, (C2) is closer to the representational-overlap mechanism. Lesson 10 §6 and lesson 15 §2.4 propose grounding $L_{21}$ as the shared-parameter update norm per item, and lesson 11 measures 2.3 versus 5.4 for a consistent versus an inconsistent item. I did not rerun that.

**B8. Citations canon lacks.** These are greps over `0*/src/*.md`, with 0 hits each. False positives such as "Polyn" inside "polynomial" were checked and excluded.
- Memory models: Anderson & Schooler, SAM, MINERVA, REM/Shiffrin, Hopfield/Ramsauer, Howard & Kahana (TCM), Polyn (CMR), Shankar & Howard (Laplace time), Zacks (EST), Gershman (latent cause), Adams & MacKay (BOCPD), Itti & Baldi.
- Consolidation and replay: Tse, go-CLS/Sun et al., Stachenfeld/Dayan (SR), Mattar & Daw, Yu & Dayan, Pearce–Hall, Grossberg.
- Terms: "Bayesian surprise", "event segmentation", "change-point", "reconsolidat", "iterated learning", "serial reproduction", "model collapse".

These belong to KR2.4 where a segment uses the concept.

### (c) Corpus claims that canon already answers, or that I found incomplete

**C1. "Normalize surprise units by the predictive covariance": canon already does this in one place.** The corpus calls it a new one-line bridge (lesson 08 §8; lesson 15 §2.3). It claims the current form overstates surprise by $\sqrt{1+P_t/R}$, 4.1× at $t=0$ with a vague prior; I did not rerun that number. But `form-composition-closure` line 318, in the verified two-Kalman case, already says "the observation norm weights by the inverse innovation covariance $S^{-1}=(P^\ast_{\text{pred}}+R)^{-1}$". Only `def-mismatch-signal` lines 20 and 50 use the observation-noise covariance $\Sigma$. So this is an internal reconciliation: `def-mismatch-signal` should adopt the innovation covariance that `form-composition-closure` already uses.

**C2. Mood is not quite Pearce–Hall, and canon already has the closer antecedent.** The corpus rates mood a "near-identity in form" with Pearce–Hall associability. Pearce–Hall integrates *unsigned* $\lvert\delta\rvert$. `def-mood` line 20 defines $a_t$ as a *signed* summary: how much better or worse tracking is than the agent's own short-horizon expectation. Gain rises with sustained adverse surprise. That is closer to innovation monitoring against expected innovation magnitude, i.e. unexpected uncertainty (Yu & Dayan 2005), and to Mehra-type adaptive Kalman estimation. `deriv-adaptive-gain-dynamics` already treats Mehra (lines 20 and 99), and `def-mood` line 46 already says mood is an instance of that segment. So the standard-term anchor is one link away inside canon. `def-mood`'s own text should name it (KR2.5), alongside Pearce–Hall and Behrens as related constructs.

**C3. `der-mood-timescale`'s optimum has a named antecedent.** The bridge note (line 194) observes that $\lambda^\ast=\sqrt{q/r}$ is the steady-state gain of the local-level (random walk plus noise) Kalman filter at low SNR. From my training, not verified here: Muth 1960 established that exponential smoothing is optimal for that model. Canon has 0 hits for Muth, local-level or exponential smoothing. Under the asf math-novelty rule this is "cite the antecedent", not "deflate". The segment's own contribution is the reading of $\tau^\ast\propto\sqrt{\tau_{\text{env}}}$ for mood and emotional inertia.

**C4. Standard names for ad hoc terms (KR2.5).** Each is from my training unless noted; please verify before adopting.
- "Stability-induced myopia" (5 segments) is, in recursive identification, the loss of estimator "alertness" as the gain decays without forgetting (Ljung; Åström & Wittenmark). Canon cites Ljung but not the term. ML's "loss of plasticity" (Dohare et al. 2024) is a *different* mechanism under a similar name, so it is a collision to avoid.
- "Stability-plasticity" originates with Grossberg (ART, 1980s); 0 hits.
- `der-turnover-information-recursion` (geometric decay through repeated lossy reconstruction unless re-injected) is formally the iterated-learning / serial-reproduction result: Bartlett 1932; Griffiths & Kalish 2007, convergence to the prior; and at text level, model collapse (Shumailov et al.). The synthesis note's "iterated summaries converge to the model's prior" (`msc/memory-reading-synthesis.md` §5) is the same object. The bridge rates it a formal analogue.
- The bridge's "term clash" note (line 364): AAT's "latent cause" (an unobserved common cause in a DAG) collides with Gershman's latent-cause inference (a latent context/generator). Worth one disambiguating clause.

**C5. The IMM/regime case is AAT's nearest object to event segmentation, and canon concedes the gap.** `deriv-update-detection-latency` says a sidecar CUSUM/GLR change detector "is always going to beat the log-odds accumulator". Lesson 08 §8 and lesson 15 §2.2 propose promoting the IMM case of `deriv-adaptive-gain-dynamics` (graded sketch) to a boundary operation: a model-selection posterior over {continue, restart, switch}, judged with hindsight. Lesson 08b's BOCPD runs show why hindsight matters: a lone outlier at P = 0.89 with no lookahead falls to 0.01 at $d=20$. `result-mismatch-decomposition` (exact, claims-verified) supplies the principled reason not to segment on every spike. That link is new and already canon-grounded on the ASF side.

### (d) Synthesis proposals, at the corpus's own credences

- **Five operating regimes** for $g_M$ (lesson 15 §5, ~55%): online update; boundary/retire; cue-driven reinstatement; retroactive tagging; offline consolidation. Each comes with a trigger, objective and failure mode. Reinstatement and boundary are called the highest-value additions. Possible home: a formulation segment extending `der-recursive-update` / `form-consolidation-dynamics`. Lesson 15 §5 still writes the cadence as $\nu_{\text{consol}}\ll\nu_{\text{online}}$, the condition A1 flags.
- **Replay regulation as the missing stability upper bound** (lesson 15 §2.6; lesson 12 §6b): order replay by Gain × Need (Mattar & Daw 2018; the need term is the successor representation) and stop when held-out predictive error stops falling (go-CLS: Sun, Advani, Spruston, Saxe & Fitzgerald 2023). go-CLS is analytically tractable in a linear teacher–student–notebook setting; equations are at `research/consolidation_schemas_maps.md` lines 365–385. That makes it a candidate for direct adoption under prior-art integration. Its stated status there is ~40% for the normative principle in humans, but the math is sound. go-CLS's result is that unregulated transfer *harms* generalization in noisy worlds. AAT's IB objective points the same way but does not derive the harm.
- **Schema effects** (lesson 15 §2.5; lesson 11 §2): make (N2)'s integration cost item-dependent, $B_{\text{consol-needed}}(e)$ = the residual after best placement in $M^{\text{slow}}$. Schema-consistent items then fail (N2) and are absorbed online. This dissolves the apparent conflict between the gain principle and Tse et al. 2007.
- **Power-law forgetting as a spectrum of $\lambda$** (lesson 01 §7, §7b; lesson 06 §7). One exponential cannot produce power-law retention. Lesson 01 §7b derives that a Gamma prior over per-item Poisson use rates gives need$(a)\propto C/(\beta+a)$, a $1/a$ tail, from rate *uncertainty* alone. Lesson 01 §7 predicts that a power-law forgetter's effective sample size, and plausibly its detection latency, grows as $T^{1-d}$; that prediction is not simulated. Whether `schema-strategy-persistence`'s inequality survives a spectrum is marked <40%. An event-indexed Laplace bank is shown to be compatible with the ordinal chronica (lesson 06 §7).
- **Goal-structured archiving is compatible with directed separation** (lesson 09b §4). `der-directed-separation` distinguishes the *processing* of events from their *selection*, so purposive folding sits on the selection side. The reverse leak (reinstated "what worked" stubs feeding $f_M$) is named as the $\Sigma$-source coupling of `der-belief-strategy-attractor`. This is a clean use of existing canon.
- **Counterfactual replay as AAT credit assignment along time** (lesson 12b §4b): links `disc-credit-assignment-boundary`, `der-observability-dominance` and `disc-structural-imagination` (pseudo-episodes live in $W_t$ until grounded). I verified the segments and the quoted phrase "observability design problem" (line 154).
- **A re-verification cadence from the persistence condition** (`msc/15-asf-and-memory-reading.md` §2d, ~60%): for each class of stored claim, the re-verification rate must exceed that domain's drift rate. This is a teaching use of `result-persistence-condition` for agent memory.

## 3. What canon has that memory theory lacks

Lesson 15 §3 and bridge §5 list these, and I'd keep them in view during KR3.3 so the map isn't all deficits:
- the persistence inequality (exact, claims-verified);
- forgetting as a dynamical necessity, plus detection latency;
- $\epsilon_{\max}$, a derived fast/slow ratio, which CLS never derives;
- (N1)+(N2) as a biology-free answer to "why consolidate";
- the mismatch decomposition, which says which errors to learn from;
- the turnover recursion.

These are teaching material for a "Reading AAT as a memory theory" layer.

## 4. Unread surface: the largest remaining item

I read `asf_bridge.md` whole, lesson 15 whole, the Bridges/AAT sections of lessons 01, 06, 08, 09b, 10, 11, 12, 12b and 17, and the `msc/` synthesis, the 15 reading note and HANDOFF. The other **seven research notes (~490 KB)** I mapped only by heading and targeted grep. HANDOFF says Joseph believes "almost all of the good novel material ended up in `research/`", and no agent has yet read them against ASF. The notes carry their own verification tags: [V] verified against a source, [V-ft] verified against full text, [K] from training knowledge, [BK] book or abstract-level. Judging by headings and my greps, the most ASF-bearing sections are:

- `event_cognition.md` **Q3**, surprise measures (lines 164–222). Its verdict at lines 219–221: raw surprisal predicts human boundaries poorly; belief-change and uncertainty measures do better (~80%); effect sizes are small (r ≈ 0.1). Line 220 is an explicit agent-theory bridge: if mismatch is precision-weighted $\delta^\top\Pi\delta$, then boundary evidence is a log-likelihood ratio of competing generative hypotheses, surprisal is the log-evidence of one hypothesis, and Bayesian surprise is the belief update (~50%). That bears on A2, C1 and C5. Note that Kumar et al. 2023's "Bayesian surprise" is a KL between successive *predictive* distributions, not Itti–Baldi's (line 218).
- `event_cognition.md` **Q8**: goals in event segmentation (line 477). Bears on 09b and $G_t$.
- `consolidation_schemas_maps.md` **§1, §4, §5**: CLS and interference; go-CLS, Spens & Burgess, and Mattar & Daw. The Mattar & Daw equations are marked [K], unchecked (line 467). §5 covers SR, TCM, TEM and transformers.
- `offline_counterfactual_segmentation.md` **Q6**: placing boundaries retrospectively by counterfactual value (line 336). **Q5**: ML analogues such as hindsight relabeling and Dyna-style dreaming. Canon has no whole-word "Dyna" hit; the 190 grep hits are "Dynamics".
- `retrieved_context_and_classical.md` **§1** (rational analysis, forgetting functions) and **§7** (the Laplace framework).
- `dreams_nrem_rem.md`: the REM/NREM evidence behind B6.
- `reality_monitoring.md`: source monitoring. It bears on `disc-structural-imagination`'s "hallucination as level-confusion" and on provenance tagging, but I did not read it.

Also unread by me: `sources/`, `ref/` (126 PDFs), and `code/` (I did not rerun any number quoted above).

## 5. Adjacent, possibly more important than this framing

- **One structural question is visible from three directions:** B4 (PROPRIUM puts the raw record inside $M_t$), B5 (identity uniqueness assumes a compressed store), and A1 (archive retrieval as a channel). Underneath all three: AAT's core has no operation for reading the record, and PROPRIUM's practice, `disc-deferred-observation-processing`, and the estate's own memory architecture all require one. If KR3.3 handles these as three separate fixes, the shared cause may be missed.
- **`def-proprium-mapping` places "terminal values" in AXIOMATA** as "frozen, unchangeable structure of $\mathcal M$" (line 20). That puts objective content in the model class, which reads as a directed-separation category slip. It's outside memory and is my reading only. One line for whoever audits 04-eli-core.
- **The published Ladder artifact is stale**, per HANDOFF (https://claude.ai/artifact/So18kreNSh2En9uLiFS9Af, pre-`de70ef5`). It's not mine to fix.
- HANDOFF's "things easy to get wrong" warns that the course's internal agreement is "coherence, not convergence": one author, one day. That applies to every corpus claim above that I did not check against canon or a primary source.

## 6. How I checked

- Canon claims: `grep`/`sed` over `~/src/arch/asf/0*/src/*.md`, `NOTATION.md`, `LEXICON.md` and `terminology/entries/`; line numbers are given at each item.
- Segment status and stage: read from frontmatter for `result-persistence-condition`, `result-mismatch-decomposition` and `der-recursive-update` (all exact, claims-verified), and for `form-consolidation-dynamics` (robust-qualitative, draft) and `def-mood` (discussion-grade, draft). All other statuses come from the bridge's §7 table, which matched every one I spot-checked.
- Absent-citation counts: case-insensitive grep, with apparent hits inspected for false positives.
- Not done: rerunning any `code/` script; reading the seven research notes in full; checking anything in `ref/` PDFs.
