# Spike: Finding 7 — Narrowing P5 from "exact exteriorized chronica" to "committed-state subset"

**Status:** Promotion-ready repair drafted; awaiting Joseph's review.
**Source finding:** `audits/pending-findings-2026-04-22.md` lines 272–298 (Codex audit 2026-04-22, Finding 4).
**Target segment:** `02-tst-core/src/obs-software-epistemic-properties.md` (P5 at lines 56–62; supporting Discussion at line 84).
**Scope:** P5 + its Consequence + the P5 Discussion paragraph. The headline (line 15) is left to C-BP3; see §4 below.

---

## 1. The diagnosis in one paragraph

P5 currently asserts that git records the chronica $\mathcal{C}_t$ "without information loss" and that "git's scope matches the chronica's definition precisely for the codebase domain." But $\mathcal{C}_t$ is defined in `#def-chronica` as the *complete* sequence $(o_1, a_1, \ldots, a_{t-1}, o_t)$ of agent–environment interactions — every observation and every action. `#scope-developer-agent` enumerates many software observation channels (IDE state, runtime logs, monitoring alerts, code-review threads, colleague queries, build-system signals, conversations) that are *not* in git. Git records *committed* codebase state transitions exactly; it does not record the full software chronica. `#hyp-causal-discovery-from-git` already concedes that the chain from git data to AAD quantities is empirical and unresolved. P5 is the only place in the segment that contradicts those companion claims, and it does so at the strongest possible verbal pitch ("exact," "without information loss," "precisely"). The repair is to narrow the equivalence claim to the committed-state subset, retain the comparative-advantage claim at lower strength, and tag the consequence (P5 Consequence) as the empirical hypothesis that it actually is.

---

## 2. Proposed revised passages

The following replaces lines 56–62 (P5 + Consequence) and line 84 (the P5 paragraph in Discussion). All other parts of the segment are untouched in this spike.

### 2a. Revised P5

> **P5. Committed-state subset of chronica recorded exactly.** Git provides a complete, immutable record of every *committed* change to the codebase: what changed, when, and by whom. The chronica $\mathcal{C}_t$ ( #def-chronica) is broader — it is the full $(o_1, a_1, \ldots, a_{t-1}, o_t)$ sequence of agent–environment interactions, of which committed codebase state transitions are one subset. Within that subset, git records the diff between commits $i$ and $i+1$ as the exact intervention that occurred, with no sampling loss and no recall bias. Outside that subset, the software chronica also includes uncommitted edits, IDE navigation and edit traces, build-system invocations, test runs and their outputs, runtime logs and metrics, monitoring alerts, code-review threads, deployment events, and out-of-band coordination (chat, tickets, in-person discussion). These channels are enumerated in #scope-developer-agent; most are recorded only in fragmentary, tool-specific stores, and many are not recorded at all.
>
> *[Empirical Claim]* For the software domain, the committed-state subset of $\mathcal{C}_t$ — call it $\mathcal{C}_t^{\text{commit}} \subset \mathcal{C}_t$ — is captured by git with negligible sampling loss and no post-hoc revision (commits are immutable), giving lower sampling and recall bias on $\mathcal{C}_t^{\text{commit}}$ than self-report instruments offer on the comparable subset in other domains. The remainder $\mathcal{C}_t \setminus \mathcal{C}_t^{\text{commit}}$ is no better captured in software than in other instrumented-but-incomplete domains; in some sub-channels (private reasoning, in-person coordination) it is worse.
>
> The chronica is, by definition, the record of interactions between agent and environment — not the agent's internal reasoning about those interactions. Git's scope matches one well-bounded slice of the chronica exactly (the committed-state slice for the codebase component of $\Omega_t$), and is silent on the rest.
>
> What git additionally does *not* record is orthogonal: the agent's internal model state $M_t$ (which beliefs drove the intervention), the strategy DAG $\Sigma_t$ (which causal hypotheses led to this choice), or the objective $O_t$ (which target the agent was pursuing). These are agent-internal and not part of the chronica by any domain's definition. Commit messages and PR descriptions are partial exteriorizations of $M_t$/$G_t$ intent, but only to the extent the agent chose to verbalize them.

### 2b. Revised P5 Consequence

> *Consequence:* For the committed-state subset $\mathcal{C}_t^{\text{commit}}$, environment-side AAD quantities ($\rho$ restricted to commit-driven disturbance, coupling structure as estimated from co-change, change frequency, state-transition patterns) can be computed directly from git without the sampling and recall biases that would dominate self-report estimates of the same quantities. *[Empirical Claim]* Whether those committed-subset estimators are good estimators of the *full-chronica* AAD quantities is an open empirical question — see #hyp-causal-discovery-from-git for the confounding structure (shared requirements, convention-driven bundling, developer knowledge state) that mediates the gap between $\mathcal{C}_t^{\text{commit}}$-derived estimates and full-$\mathcal{C}_t$ quantities. Estimation of agent-internal quantities ($M_t$ content, $\Sigma_t$ structure, $O_t$ definition) requires separate instrumentation regardless: commit messages, PR descriptions, design documents, or — for AI agents — explicit reasoning traces.

### 2c. Revised Discussion paragraph (current line 84)

> **P5 and the instrumentation boundary.** The exact-recording claim of P5 applies to the committed-state subset $\mathcal{C}_t^{\text{commit}}$ — the codebase-component-of-$\Omega_t$ state transitions that pass through `git commit`. Within that subset, recording is exact (immutable diffs, full timestamps, signed authorship). The remainder of the chronica — uncommitted work, IDE telemetry, runtime observations, build and test traces, monitoring alerts, code-review discussion, out-of-band coordination — is captured only by other tools or not at all, and the level of capture varies by team and tooling. *Agent-internal* content (why a particular intervention was chosen; which beliefs or strategies drove it) is not part of the chronica in any domain and therefore not in git's scope. Commit messages and PR descriptions are partial exteriorizations of agent intent; their quality varies enormously by authorial discipline. This is relevant for #hyp-causal-discovery-from-git: the *committed-subset* interventional record is complete, but (i) the broader chronica is only partially captured, and (ii) the confounder record is partial wherever confounders depend on agent-internal state (e.g., developer knowledge state, which is agent-internal and not part of the chronica). Treating $\mathcal{C}_t^{\text{commit}}$-derived estimates as estimates of full-$\mathcal{C}_t$ quantities is an *empirical bridging step*, not a definitional identity.

---

## 3. Side-by-side diff

### Diff 3a. P5 headline + first paragraph (line 56)

| | Current | Proposed |
|---|---|---|
| **Heading** | **P5. Exact exteriorized chronica.** | **P5. Committed-state subset of chronica recorded exactly.** |
| **Equivalence claim** | "For the *exteriorized* content of the chronica $\mathcal{C}_t$ — the sequence of codebase state transitions, their timing, and their authorship — git records this without information loss." | "The chronica $\mathcal{C}_t$ is broader — it is the full $(o_1, a_1, \ldots, a_{t-1}, o_t)$ sequence of agent–environment interactions, of which committed codebase state transitions are one subset. Within that subset, git records the diff between commits $i$ and $i+1$ as the exact intervention that occurred, with no sampling loss and no recall bias." |
| **Out-of-scope channels** | (not enumerated in P5) | New paragraph enumerating the channels in $\mathcal{C}_t \setminus \mathcal{C}_t^{\text{commit}}$, with a forward reference to `#scope-developer-agent`. |
| **Comparative-advantage claim** | (currently lives only in the Consequence as "without the sampling and recall biases that afflict other domains"; framed as fact) | Moved into P5 body, tagged *[Empirical Claim]*, and explicitly scoped to $\mathcal{C}_t^{\text{commit}}$: "lower sampling and recall bias on $\mathcal{C}_t^{\text{commit}}$ than self-report instruments offer on the comparable subset in other domains. The remainder is no better captured in software than in other instrumented-but-incomplete domains." |

### Diff 3b. "Git's scope matches" paragraph (line 58)

| Current | Proposed |
|---|---|
| "Git's scope matches the chronica's definition precisely for the codebase domain: the codebase is the environment, commits are the interventions, diffs are the state transitions, and all of these are recorded exactly." | "Git's scope matches one well-bounded slice of the chronica exactly (the committed-state slice for the codebase component of $\Omega_t$), and is silent on the rest." |

The framing "the codebase is the environment" is dropped — `#scope-developer-agent` already establishes that $\Omega_t$ extends beyond the codebase, and reasserting the equation here was the source of the overstatement.

### Diff 3c. P5 Consequence (line 62)

| Current | Proposed |
|---|---|
| "*Consequence:* Empirical estimation of environment-side AAD quantities ($\rho$, coupling, change frequency, state-transition patterns) is possible from the historical record, without the sampling and recall biases that afflict other domains. Estimation of agent-internal quantities ($M_t$ content, $\Sigma_t$ structure, $O_t$ definition) requires separate instrumentation — commit messages, PR descriptions, design documents, or for AI agents, explicit reasoning traces." | "*Consequence:* For the committed-state subset $\mathcal{C}_t^{\text{commit}}$, environment-side AAD quantities … can be computed directly from git without the sampling and recall biases that would dominate self-report estimates of the same quantities. *[Empirical Claim]* Whether those committed-subset estimators are good estimators of the *full-chronica* AAD quantities is an open empirical question — see #hyp-causal-discovery-from-git for the confounding structure … Estimation of agent-internal quantities … requires separate instrumentation regardless." |

Two changes: (i) the consequence is scoped to $\mathcal{C}_t^{\text{commit}}$ rather than the full chronica; (ii) the bridge from committed-subset estimates to full-chronica AAD quantities is tagged *[Empirical Claim]* and routed through `#hyp-causal-discovery-from-git`.

### Diff 3d. Discussion paragraph "P5 and the instrumentation boundary" (line 84)

| Current | Proposed |
|---|---|
| "The exact-chronica status of git applies to environment-side content (state transitions, timing, authorship) — matching exactly what the chronica is defined to contain." | "The exact-recording claim of P5 applies to the committed-state subset $\mathcal{C}_t^{\text{commit}}$ — the codebase-component-of-$\Omega_t$ state transitions that pass through `git commit`. Within that subset, recording is exact (immutable diffs, full timestamps, signed authorship). The remainder of the chronica … is captured only by other tools or not at all." |
| "the interventional record is complete (because it is environment-side)" | "the *committed-subset* interventional record is complete, but (i) the broader chronica is only partially captured, and (ii) the confounder record is partial wherever confounders depend on agent-internal state" |
| (no closing sentence) | Adds: "Treating $\mathcal{C}_t^{\text{commit}}$-derived estimates as estimates of full-$\mathcal{C}_t$ quantities is an *empirical bridging step*, not a definitional identity." |

---

## 4. Cross-segment check

I searched all four component `src/` trees plus root files for phrases that would inherit the overstatement. Findings:

### 4a. Direct verbal hits on the "exact exteriorized chronica" / "git's scope matches chronica precisely" framing

Only inside the target segment itself:
- `02-tst-core/src/obs-software-epistemic-properties.md:56` — the P5 heading and first paragraph (target of this repair).
- `02-tst-core/src/obs-software-epistemic-properties.md:58` — the "Git's scope matches" sentence (target of this repair).
- `02-tst-core/src/obs-software-epistemic-properties.md:84` — the Discussion paragraph "exact-chronica status of git applies to environment-side content" (target of this repair).

No other segment file in `01-aad-core/src/`, `02-tst-core/src/`, `03-logogenic-agents/src/`, or `04-eli/src/` repeats either phrase. The overstatement is contained.

### 4b. References to P5 from other segments (need consistency review)

- `02-tst-core/src/obs-software-epistemic-properties.md:72` (own §Epistemic Status, sentence about which domains lack which properties) lists "biological systems lack P1, P2, P5; military systems lack P1, P5." This sentence is about *comparative completeness*, not about the strength of P5; the narrowing does not overturn it (the committed-state subset is still better-captured in software than the analogous subset in biology or military operations). **No edit needed**, but the reviewer may want to add a parenthetical that "lacks P5" now means "lacks an exactly-recorded committed-state subset of comparable scope."

- `02-tst-core/src/obs-software-epistemic-properties.md:86` ("Multi-agent amplification" paragraph) refers to "P5 (perfect history)." This is a *paragraph-internal short tag*. After the narrowing, "perfect history" reads as overclaim by association. **Suggested edit (optional, for consistency):** change "P5 (perfect history)" to "P5 (exact committed-state record)." Trivial, but worth doing in the same pass.

- `02-tst-core/src/hyp-causal-discovery-from-git.md:84` references `#obs-software-epistemic-properties, P4` for the dependency graph, not P5. **No edit needed.**

- `02-tst-core/src/def-system-coupling.md:33` references `#obs-software-epistemic-properties, P3` for the interventional claim. **No edit needed.**

- `02-tst-core/src/scope-developer-agent.md:115` references `#obs-software-epistemic-properties, P6` for active-channel $U_o$. **No edit needed.**

- `03-logogenic-agents/src/result-section-ii-survival.md:127` ("Implications for logogenic agent engineering") cites `#obs-software-epistemic-properties` P5 explicitly for the *instrumentation-boundary framing*: "The instrumentation-boundary framing in `02-tst-core/`'s `#obs-software-epistemic-properties` P5 is the parallel observation in the software domain: statement-level survival does not imply that the quantities are cheap or automatic to extract." This citation actually *strengthens* under the proposed narrowing — the new wording makes the instrumentation boundary more explicit. **No edit needed.**

### 4c. Adjacent old-source-material file (not a segment, but flagged for archaeology)

- `02-tst-core/src/old-tst-via-tft-readme.md:28` says: "History is perfectly recorded. Git provides a complete, immutable record of every change … This is $\mathcal{C}_t$ (chronica) without information loss — the full interaction history preserved exactly." This is the original overstated claim that propagated into P5. The file is an `old-*` source-material file, not a current segment; per CLAUDE.md it lives in `src/` only until absorption is complete and is tracked in `MIGRATION-MAP.md`. **No edit needed in the spike**, but the review of P5 is the natural moment to also mark this paragraph in the source as superseded if the migration tracking still cares about it.

### 4d. Headline of `software-epistemic-properties.md` line 15

> "Software development possesses six epistemic properties that collectively make it the richest operationalization domain for AAD…"

This is Finding 15's territory and the subject of C-BP3. It is *not* edited by this spike. See §5 for the recommendation.

### 4e. Summary

The overstatement is genuinely contained: only three lines of one segment carry it directly, plus one paragraph-internal tag at line 86 that is worth tightening for consistency. No other segment file inherits the framing. One `old-*` source-material file is the upstream origin and remains in archaeology mode.

---

## 5. Scope decision flag — Finding 15 (the "richest operationalization domain" headline)

**Finding 15 status:** held for C-BP3 (software-as-calibration-laboratory reframing), per `TODO.md` line 69 and `audits/pending-findings-2026-04-22.md` lines 517–538.

**Recommendation: leave the headline alone in this spike. Do not include a minimal companion fix.**

**Justification:**

1. **The findings are genuinely separable.** Finding 7 is a *factual narrowing*: git ≠ chronica. Finding 15 is a *positioning/comparative-superlative* concern: "richest" is a ranking claim across domains, and ranking claims are a different epistemic species from subset claims. Fixing the subset claim does not require taking a position on the ranking.

2. **C-BP3 is a portfolio-level move, not a one-segment edit.** Per `msc/architectural-proposals-2026-04-22.md` lines 438–463, C-BP3 reframes software's role across TST as the *calibration-laboratory* domain for AAD, with explicit assumption-marking for transfer to other domains. The headline of `software-epistemic-properties.md` is one surface of that move; doing it piecemeal in this spike would leave the rest of TST out of register and would force a rewrite of the same headline once C-BP3 lands. Joseph's prior preference (per CLAUDE.md `feedback_architectural_proposals_vs_findings.md`) is that architectural proposals get first-class treatment, not absorption-via-Finding.

3. **The narrowing in §2 already does the load-bearing honesty work.** The proposed P5 explicitly enumerates what software *doesn't* have ($\mathcal{C}_t \setminus \mathcal{C}_t^{\text{commit}}$, agent-internal state, etc.). A reader who reaches the body will not come away believing the headline's superlative covers the full chronica, even if the headline still says "richest." So the cost of leaving the headline is bounded — it remains a positioning claim that the body conspicuously qualifies — and the benefit of *not* touching it is that C-BP3 can do the reframing coherently across all the segments it affects.

4. **Mitigating data point.** The segment's own Epistemic Status (line 72) already concedes the "richest" comparison "has not been systematic" and downgrades to *plausible*. That partial caveat survives the P5 narrowing intact and provides the bridge to C-BP3 without further edits in this spike.

**If Joseph disagrees** and wants Finding 15 closed in the same edit pass, a minimal companion fix would be: change line 15 from "the richest operationalization domain" to "a privileged high-identifiability domain" (the C-BP3 phrase) and adjust §Epistemic Status accordingly. This is 5–10 minutes of additional editorial work and would *not* preempt C-BP3's broader reframing — it would just lower-bound it. I still recommend deferring; flagging the option for transparency.

---

## 6. Open questions for Joseph

1. **`$\mathcal{C}_t^{\text{commit}}$` notation.** I've introduced the symbol $\mathcal{C}_t^{\text{commit}}$ inline as "the committed-state subset of the chronica," and used it three times across P5 + Consequence + Discussion. Two options: (a) keep it inline-defined here (current proposal — local convenience, no `NOTATION.md` edit); (b) promote it to `NOTATION.md` if you expect to reference the committed subset elsewhere (in `#hyp-causal-discovery-from-git`, `#meas-coherence-coupling`, or any TST measurement segment that operationally lives on git). My weak preference: keep it local for now, promote later if a second use site appears. Your call.

2. **Empirical-Claim tag on the comparative-advantage sentence.** I've tagged the "lower sampling and recall bias on $\mathcal{C}_t^{\text{commit}}$ than self-report in other domains" sentence as `*[Empirical Claim]*`. This is consistent with FORMAT.md (the comparison is to other domains' self-report instruments and is not derivable from the formalism — it is an observation about the world). But the segment's overall `status:` is `discussion-grade` and `type:` is `observation`, so an inline empirical tag is slightly heavier than the surrounding prose. Acceptable, or do you prefer a softer marker like `*[Discussion]*` with the empirical character carried by the surrounding language? Currently leaning toward keeping `*[Empirical Claim]*` because Finding 7 is specifically about epistemic-strength honesty.

3. **Whether to also tighten line 86 ("P5 (perfect history)" → "P5 (exact committed-state record)").** Listed in §4b as optional. Trivial edit; only flagging because I am holding the line on "do not gold-plate" — happy to either include or omit per your preference.

4. **Whether `causal-discovery-from-git.md` should gain a backward cross-reference.** The new P5 Consequence routes the reader to `#hyp-causal-discovery-from-git` for the confounding structure. The reverse pointer already exists (causal-discovery-from-git lists software-epistemic-properties in its `depends:`). No action needed — just confirming the asymmetry is intentional.

5. **Migration-map handling of `old-tst-via-tft-readme.md` line 28.** §4c flags the upstream overstatement in the absorbed source material. Do you want this spike to also note in `MIGRATION-MAP.md` that the line-28 framing has been narrowed in the canonical segment? Or is `old-*` content explicitly out of scope until the file is fully retired?

6. **Promotion path.** This spike is a contained editorial repair. After your sign-off, the natural promotion sequence is: (i) apply the §2 edits to `software-epistemic-properties.md`; (ii) optionally apply the §4b consistency edit at line 86; (iii) close Finding 7 in `pending-findings-2026-04-22.md`; (iv) note in `TODO.md` that Finding 15 remains held for C-BP3, with this spike closing the related Finding 7. No segment downgrade needed (segment is already at `draft` and `discussion-grade`).

---

## 7. Self-check: is the finding's premise correct?

Yes. Three independent confirmations:

1. **Definitional.** `#def-chronica` (line 15) defines $\mathcal{C}_t$ as the complete observation/action sequence — not the committed-state subset. The current P5 wording asserts equivalence between the two, which is definitionally false.

2. **Operational.** `#scope-developer-agent` (lines 30–41 environment table; lines 95–113 observation channels) explicitly lists multiple software channels that are not in git: runtime logs, monitoring alerts, code review, colleague queries, IDE state, infrastructure dashboards. These are part of $\mathcal{C}_t$ for any AAD-instantiated developer agent.

3. **Already conceded in companion segment.** `#hyp-causal-discovery-from-git` (line 18, line 78, line 80) explicitly states "the chain from git data to AAD quantities is empirical and unresolved" and that "max attainable: empirical." P5's current strong-equivalence framing contradicts the companion segment that immediately depends on it. The narrowing in §2 brings P5 into register with `#hyp-causal-discovery-from-git`.

The finding is correct, the repair direction in `pending-findings-2026-04-22.md` is correct, and the §2 wording is the cleanest version of that repair I can draft without taking a position on C-BP3.
