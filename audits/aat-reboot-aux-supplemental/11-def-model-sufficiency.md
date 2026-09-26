# Supplemental 11 — `def-model-sufficiency`

*Finder, 2026-09-25, as of `875e1ac3`. This is the companion to `~/src/aat-reboot/scratch/aux/11-def-model-sufficiency.md`. Tags in brackets name the slugs each note bears on.*

## Checks that passed (please add to the Working Notes of `def-model-sufficiency`)

- [def-model-sufficiency] Checked the equivalence of the two ratio forms, $1 - I(\mathcal C;Y \mid M,A)/I(\mathcal C;Y \mid A) = I(M;Y \mid A)/I(\mathcal C;Y \mid A)$, and the boundary values against the chain rule for $M_t = \phi(\mathcal C_t)$. Holds for any conditioning variable, including the literal closed-loop $A$. 451729, 738192 and 731548 confirmed the same. What fails under closed loop is the *meaning* of the denominator, not the range (aux FINDER-OBSERVED (a)).
- [def-model-sufficiency, deriv-recursive-update] Checked `deriv-recursive-update.md:197` ("when $S(M_t) = 1$, the recursive update loses nothing"). If $Y = (o_{t+1}, Y')$ is independent of $\mathcal C_t$ given $(M_t, A)$, weak union gives $Y'$ independent of $\mathcal C_t$ given $(M_t, o_{t+1}, A)$. So $(M_t, a_t, o_{t+1})$ is sufficient at $t+1$, and an $f$ that keeps it loses nothing. Holds.
- [def-model-sufficiency, example-kalman] Checked `example-kalman.md:137` ("$M_t$ as sufficient statistic") against the definition, under the known law. $(\hat x, P)$ fixes the Gaussian posterior of $x_t$, and future observations depend on the past only through $x_t$, so $S = 1$. Holds.
- [def-model-sufficiency] Checked the *adjustment* leg of :45. Conditioning on a treatment's parents satisfies the backdoor criterion. With $a_t = \pi(M_t, G_t)$ and $S = 1$, $G_t$ (a function of the history) is screened off given $M_t$, so $M_t$ alone is a valid adjustment set, up to non-history policy inputs. Holds. The *identification* leg doesn't hold; that one is in the aux, UNINTEGRATED 1.
- [def-model-sufficiency, result-mismatch-decomposition] Checked `result-mismatch-decomposition.md:49` ("insufficiency still implies positive regret under proper scoring rules") against the log-loss identity (numerator = excess log-loss, aux 08). Holds for log-loss, with equality.

## Other reflections and why they're not in the aux

- The `.integrated/` reflections (193847, 266847, 384279, 471203, 584721, 742613, 773921, 829314, 849201) were all lifted into the 2026-05-30 gold.
- 742613 F8 (no denominator condition) was resolved by AF-5 (`audit-findings-742613.md:258`).
- 829314 withdrew its divide-by-zero flag (`audit-findings-829314.md:308`).
- [def-model-sufficiency] 963715 F3: a `deps-verified` segment depends on a `draft` IB segment (`audit-findings-963715.md:56–62`; "promote the IB" is its strengthen-first fix). I omitted it because stage gating is under reconsideration and Joseph ignores `stage:` (asf project memory, `feedback_stage_gating_known_problematic.md`).
- [def-model-sufficiency] 527914 (`AUDIT-WORKING-527914/12-def-model-sufficiency.md`): keep "model sufficiency"; "trajectory-indexed sufficiency" could be a named qualifier (:29). That qualifier is subject to aux FINDER-OBSERVED (c). Its watchlist (:47–49) is good: sufficiency renamed as accuracy, $S$ used without policy or task context, aggregation across copies.
- [def-model-sufficiency, def-value-object] 374162 (`03-batch-sufficiency-cycle-reflections.md:22, :28`): uses "a model with $S=1$ is correct" as a quiz trap, and asks whether `#def-value-object` delivers the backdoor machinery promised here. It now does, as (C1)–(C3). 628417 (`batch-03-04-sufficiency-cycle.md:8, :16, :27–28`) restates the gold; its chess-engine line (high $S$, low fluency) is already in `#der-action-selection`.
- [def-model-sufficiency] 526815's checkpoint (`15-chapter-2-checkpoint.md:26`) asks "does low $S$ or low $\mathcal F$ become 'wrong about reality' rather than 'predictively insufficient for a task'?" Aux FINDER-OBSERVED (d) is the answer at this segment: $S$ can't see the agent's own decoder. Watch the Ch.4 result for this slide.

## Slug-tagged notes for later segments

- [def-model-class-fitness] Everything in the aux's FINDER-OBSERVED (a)–(e) is inherited by $\mathcal F$, on top of aux 08's codomain type-break.
  - Under the per-world law (FINDER-OBSERVED (b)), $\mathcal F$ measures how much belief-state information a store of the class's *format* can carry. It is not "can the class represent the dynamics", because the ideal decoder already knows the dynamics.
  - SP-30′'s "model-class fitness is law-representability" (`spikes/epistemic-target-ontology/03-comprehension-lift-scout.md:59`) is true only under a non-degenerate $\pi_0$ on $\theta$. That's worth deciding before the class-fitness rewrite.
  - Also, the reboot's $\mathcal F_t$ (filtration) collides with $\mathcal F(\mathcal M)$.
- [scope-agent-identity] Consequence 1, "sufficiency is trajectory-indexed" (:29, :59), isn't delivered by the ensemble definition (aux FINDER-OBSERVED (c)). There are two honest options:
  - restate it as a per-run quantity: the KL form, conditioned on the realized history, which is not in $[0,1]$;
  - or restate it as "sufficiency is a property of the loop law, the policy and $\phi$", in which case copies differ only when their loops differ.

  Consequences 2 and 3 don't rest on it.
- [example-bandit] :62 gives two reasons for $S \lt 1$.
  - Reason (1), "treats reward means as stationary", describes the agent's *interpretation*, which $S$ can't see.
  - The actual loss: $(\hat\mu, n)$ with a constant step $\alpha$ discards the pull-timing information that the per-arm Kalman posterior needs (variance grows with time since the last pull).
  - Reason (2), "no uncertainty representation", is right, if read as that loss.
- [disc-m-preservation, obs-context-turnover, 03-llm-core] $S_{\text{prior}}$ "from the pretrained weights" (`disc-m-preservation.md:70–72`) is identically 0 under the fixed-endowment convention, since a constant store retains nothing. It needs either the target-form $S$ with a random endowment (which can exceed 1), or a different quantity. That quantity would be decoder quality (log-loss of $\hat p$), which is accuracy, not sufficiency. Not checked: `obs-context-turnover.md:54` normalizes the turnover drop by $H(M)$ rather than by predictive information, which is a different quantity from $S$.
- [def-identity-sufficiency, 04-eli-core] (IS-A2)'s parenthetical, that `#def-model-sufficiency` "does not require deterministic compression", is true under open-loop or marginalized actions and false under this segment's literal closed-loop conditioning. $S_{\text{id}}$ itself marginalizes under $\pi^{\text{cont}}$ (IS-A3), so it is internally fine, and it's the better template.
- [form-information-bottleneck] The IB Lagrangian carries the same observational $I(M;Y \mid a_{t:\infty})$. 731548 (`11-form-information-bottleneck.md:11–12`) flagged the closed-loop chain failure and suggested directed information. The IB finder may want the XOR counterexample from aux 11.
- [terminology] `terminology/entries/model-sufficiency.md:19` says "$S = 1$ is exact prediction; $S = 0$ is no better than chance". The first contradicts the segment's own sufficiency-vs-accuracy paragraph; the second should read "no better than the action-conditioned marginal". The LEXICON brief (:101) is fine.
- [def-mismatch-signal] Aux FINDER-OBSERVED (d): accuracy lives in the agent's own decoder, which is what mismatch measures, so the segment's "the mismatch signal measures accuracy" is right. The mechanism given for why $S$ misses it is what's off.

## History

- The formula is TFT's (`.archive/old-tf-10-structural-adaptation.md:13–14`), with "sufficient statistic" attributed to Fisher 1922 (`old-tf-03-model.md:60,74`).
- TFT *totalized* a zero denominator as $S \equiv 1$ (:22). AF-5 (`4f0315e0`, 2026-04-25, Joseph's commit, agent co-authored) reversed that to "undefined", with the rationale in the commit body. The gold's boxed-agent line is the old convention resurfacing.
- The Discussion paragraphs were added one at a time between 2026-04-01 and 2026-04-22 (aux ADDITIONAL-NOTES 4).
- The $S = 1$ "nearly sufficient for causal validity" sentence dates from `5a330a07` (2026-04-02), before the (C1)–(C3) gate existed.

## Reasoning and worries

- **Confidence.**
  - (a) the XOR counterexample: a two-line computation, high confidence.
  - The target identity (ADDITIONAL-NOTES 1): three lines of chain rule, resting on $Y \perp \mathcal C_t \mid S_t$ under externally set actions. I'm confident, but it's unchecked.
  - (b), (c), (d): conceptual, and I'm confident. (c) disagrees with two careful prior auditors, so an independent look would be worth it before `#scope-agent-identity` is rewritten on either reading.
- **Why (a)–(c) are in the aux** despite being mine: the coordinator asked directly whether sufficiency is against a target or against observations, and how $\theta$ reads in it, and these are the three hidden choices that answer it. The rewrite would be wrong without them.
- **Worry.** The coordinator's scope predicate uses $I(S_t; o_{t+1:t+k} \mid \mathcal C_t)$ under "the agent's policy" (`adaptive-scope.md:93`). If the future actions there are conditioned *observationally* under a closed-loop policy, the same leak as (a) can inflate the scope quantity. The phrase "evaluated under the agent's own policy" reads as marginalizing, which is fine, but it's worth a sentence.
- **Not done:** a de novo check of `#der-turnover-information-recursion`'s use of $S = I_k / I(\mathcal C;Y)$ (:26); the `obs-context-turnover` bound; the IB segment's "IB-optimal $\phi^\ast$" claims.
- **Joseph's intent:** `memorata-search --joseph` turned up nothing specific to this segment. The hits were compaction summaries and other projects.

## Feedback on the brief and process

- The brief's split of fact-checks by outcome worked well here. Several prior auditors had "verified" the causal paragraph and trajectory-relativity, and listing passed checks in the aux would have hidden that they checked only one leg.
- The relata conversion queue was blocked behind an hour-long job, so I read the Barnett & Crutchfield PDF with `pdftotext`. A note in the brief that `pdftotext` on `~/.local/share/relata/pdfs/<key>.pdf` is an acceptable fallback would save the next finder a detour.
- The coordinator's drafts in `aat-reboot/src/` were very useful for aiming the aux: they let me answer the question in the reboot's own notation.
