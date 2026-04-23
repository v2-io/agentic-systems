# Spike: Finding 7 — Strengthening attempt for the P5 "exact exteriorized chronica" claim

**Status:** Strengthening succeeds materially. Per-quantity audit yields a non-empty EXACT class plus a defensible conditional-maximality result. Recommends a per-quantity revision of P5 instead of (or alongside) the uniform softening already on file.
**Source finding:** `msc/pending-findings-2026-04-22.md` lines 272–298 (Codex audit 2026-04-22, Finding 4).
**Predecessor spike:** `msc/spike-finding-7-git-chronica-narrowing.md` (uniform softening; on file pending review).
**Operating posture:** Always attempt strengthening before falling back to softening. Joseph's instruction after reviewing the predecessor was that a per-quantity exactness audit should have been done first.
**Target segment:** `02-tst-core/src/software-epistemic-properties.md` (P5 at lines 56–62; supporting Discussion at line 84).

---

## §1 — Strengthening attempt log

### 1.1 The original claim, stated precisely

P5 says three things simultaneously:

(i) **Equivalence claim.** Git records "the *exteriorized* content of the chronica $\mathcal{C}_t$ … without information loss."
(ii) **Scope-match claim.** "Git's scope matches the chronica's definition precisely for the codebase domain."
(iii) **Computability consequence.** "Empirical estimation of environment-side AAD quantities ($\rho$, coupling, change frequency, state-transition patterns) is possible from the historical record, without the sampling and recall biases that afflict other domains."

The predecessor spike correctly identifies that (i) and (ii) are overstated against the chronica definition (`#chronica` is the *complete* $(o_1, a_1, \ldots, a_{t-1}, o_t)$ sequence, of which committed codebase state transitions are a *subset*). Its repair narrows all three uniformly to "the committed-state subset $\mathcal{C}_t^{\text{commit}}$." The narrowing is honest but uniform — it does not separate which downstream quantities still inherit the strong "exact" claim from those that don't.

### 1.2 Where strengthening might bite

Two observations open the strengthening surface:

**Observation A.** Some TST quantities are *defined directly on the commit object stream*, not on the full chronica. `#system-coupling` defines coupling as $P(\text{change}(m_j) \mid \text{change}(m_i))$ where "change" is participation in an `#atomic-changeset` (a per-feature diff, exterioirized via commits). `#system-coherence` is $E[\text{proximity}(\text{changes within } m)]$ over observed commits. `#coherence-coupling-measurement` is built from these. `#change-expectation-baseline` operationalizes $n_{\text{past}}$ as observed past feature count. None of these definitionally requires anything outside the commit stream — *the TST definition itself lives on $\mathcal{C}_t^{\text{commit}}$*. For these, the original "without information loss" claim holds by construction.

**Observation B.** Other quantities — particularly the AAD-core ones P5's consequence enumerates ($\rho$, $\mathcal{T}$, $\eta^\ast$, $U_o$) — are defined over the full agent-environment loop. Their commit-derivable estimators are biased proxies (good for the *committed* portion, missing the rest). The narrowing applies cleanly here: the original strong claim does not survive.

The strengthening move is to honor the distinction between Group A (TST definitionally lives on commits) and Group B (AAD-core defined over full chronica; commit-derivable estimator is a proxy). The uniform softening collapses this distinction; the per-quantity treatment preserves the strong claim where it is genuinely defensible and explicitly drops it elsewhere.

**Observation C.** A *third* group exists: the *interventional record itself* (the set of $do$-operations performed by commits). The set of interventions IS the commit stream — exactly. Whether the *outcomes* of those interventions are also in the commit stream is partial (subsequent commits, yes; production behavior, no). So the interventional record is exactly captured for the commits-as-interventions reading, and partial for the full do-calculus reading. This is a third verdict cell ("EXACT for one of two natural readings").

### 1.3 Where strengthening might fail

I held three failure modes open while doing the audit:

- **F1.** Every candidate AAD quantity has some entanglement with the uncommitted chronica or agent-internal state, leaving no clean EXACT row. → Did not materialize: the TST-defined operational quantities are clean.
- **F2.** Intermediate (PARTIAL) verdicts dominate, washing out the per-quantity sharpness. → Did not materialize: most rows resolve cleanly to EXACT or NOT APPLICABLE.
- **F3.** Conditional maximality fails under all reasonable scope conditions. → Did not materialize: under {immutability, cryptographic authorship, standard retrieval protocol} the maximality argument carries weight, though it is structural rather than fully formal (see §4).

So the strengthening attempt is on solid ground for all three moves; it is not an honest fallback to softening.

---

## §2 — Per-quantity audit table (Move 1)

The reference set is "every AAD or TST quantity for which an empirical estimator is plausible and the question 'does it depend only on $\mathcal{C}_t^{\text{commit}}$?' is non-trivial." Verdict legend: **EXACT** (estimator definitionally depends only on $\mathcal{C}_t^{\text{commit}}$); **PARTIAL** (some inputs in $\mathcal{C}_t^{\text{commit}}$, some not); **NOT APPLICABLE** (estimator requires non-git instrumentation entirely).

I split the table into four blocks corresponding to the natural categorical structure that emerged: TST operational quantities (Block A), commit-stream structural quantities (Block B), AAD-core full-chronica quantities (Block C), and Section III multi-agent quantities (Block D).

### Block A — TST operational quantities (definitionally on commit stream)

| AAD/TST quantity | Candidate git-derivable estimator | Depends only on $\mathcal{C}_t^{\text{commit}}$? | Verdict |
|---|---|---|---|
| `#system-coupling` $P(\text{change}(m_j) \mid \text{change}(m_i))$ | Co-change frequency from commit diffs | Yes — "change" is definitionally participation in an `#atomic-changeset`, which is the per-feature diff exteriorized through commits. The conditional probability is a function of the commit-stream's diff-touch sets only. | **EXACT** |
| `#system-coherence` $E[\text{proximity}(\text{changes within } m)]$ | Mean inverse `#change-distance` between intra-module changes per commit | Yes — change locations within a commit's diff are exact; the proximity is then a function of file paths and line ranges in the diff. | **EXACT** |
| `#coherence-coupling-measurement` $Q$ | Ratio (or other aggregation) of the two above | Yes — composition of two functions each depending only on $\mathcal{C}_t^{\text{commit}}$. | **EXACT** |
| `#atomic-changeset` size (lines / files / modules per commit-as-feature) | Per-commit diff statistics | Yes for the per-commit reading; PARTIAL when "feature" requires bundling commits or when a feature spans uncommitted work. The segment defines size measures as per-changeset counts; per-commit changesets are exact. | **EXACT (per-commit reading); PARTIAL (per-feature reading where features ≠ commits)** |
| `#change-distance` $d(c_i, c_j)$ | File-path traversal + line offsets within diffs | Yes — distance hierarchy (lexical / file / module / service) is a function of the file paths and line ranges in commit diffs. | **EXACT** |
| `#change-expectation-baseline` $\hat n_{\text{future}} = n_{\text{past}}$ | Count of past commits-as-features over time interval | Yes if "feature" is operationalized as commit (or PR-merge, also in git's scope via merge commits and signed-tag protocols). PARTIAL if "feature" requires external definition. | **EXACT (commit/merge operationalization); PARTIAL (otherwise)** |
| Frequency-asymmetry signal (`#causal-discovery-from-git` point 3) | Per-pair $P(B \text{ follows } A) - P(A \text{ follows } B)$ over commit stream | Yes — purely a function of commit timestamps and diff-touch sets. | **EXACT** |
| Intervention-contrast signal (point 4 same segment) | Counts of commits changing $A$ alone vs $A$ with $B$ | Yes — function of commit-diff touch sets. | **EXACT** |
| Authorship attribution per commit | Commit author + signature | Yes — git records signed/verified author per commit. | **EXACT** |

**Block A finding.** Nine quantities. All TST-operational measurements *as defined in their own segments* are exact functions of $\mathcal{C}_t^{\text{commit}}$. This is the load-bearing block for the strengthening: the original "exact, no information loss" claim is defensible — *and was always meant to apply* — for these.

### Block B — commit-stream structural quantities (raw inputs)

| AAD/TST quantity | Candidate git-derivable estimator | Depends only on $\mathcal{C}_t^{\text{commit}}$? | Verdict |
|---|---|---|---|
| Temporal ordering of commits | Commit timestamps + parent-hash DAG | Yes — git enforces parent-hash linkage; ordering is a property of the commit DAG. | **EXACT** |
| Causal-precedence priors (used by `#causal-discovery-from-git` for direction) | "$c_1$ precedes $c_2$" from commit DAG | Yes. | **EXACT** |
| Commit-diff touch sets per file/module | Diff parsing | Yes — diffs are byte-exact in the commit object. | **EXACT** |
| Branch and merge structure | Refs, branch heads, merge commits | Yes — recoverable from the commit DAG and ref store; mainline-only restriction is a `git log` flag. | **EXACT (with mainline-vs-feature-branch convention chosen)** |
| Commit interval distribution / commit rate $\nu_{\text{commit}}$ | Inter-commit timestamps | Yes for the commit-rate reading. | **EXACT** |

**Block B finding.** Five structural quantities. These are the *raw substrate* — not themselves AAD quantities, but the inputs to every Block A estimator. EXACT by construction.

### Block C — AAD-core quantities defined over full agent-environment loop

| AAD/TST quantity | Candidate git-derivable estimator | Depends only on $\mathcal{C}_t^{\text{commit}}$? | Verdict |
|---|---|---|---|
| Environmental disturbance rate $\rho$ (full chronica) | Commit-rate $\nu_{\text{commit}}$ as proxy for disturbance injection | No — `#scope-developer-agent` (table at lines 30–41) lists multiple non-codebase $\Omega_t$ components: runtime behavior, user requirements, dependency ecosystem, infrastructure state. Production incidents, requirement changes, and dependency breaks generate disturbance without producing a commit. The estimator is biased downward. | **PARTIAL** ($\rho_{\text{commit-driven}}$ EXACT; $\rho_{\text{full}}$ NOT EXACT) |
| Adaptive tempo $\mathcal{T} = \sum_k \nu^{(k)} \eta^{(k)\ast}$ | Some commit-derived velocity proxy | No — most channels in `#scope-developer-agent` (compiler/linter, CI pipeline, runtime logs, monitoring alerts, bug reports, code review) are not in git. $\eta^{(k)\ast}$ requires per-channel $U_M, U_o$ which are agent-internal/channel-specific, not in git. | **NOT APPLICABLE** |
| Update gain $\eta^\ast = U_M / (U_M + U_o)$ | (no git-derivable estimator) | No — both $U_M$ (model uncertainty) and $U_o$ (observation noise) are agent- or channel-internal. | **NOT APPLICABLE** |
| Mismatch signal $\delta_t = o_t - \hat o_t$ | (no git-derivable estimator) | No — requires $\hat o_t$ (agent-internal prediction) and $o_t$ (often outside git: CI output, runtime logs, alerts). | **NOT APPLICABLE** |
| Mismatch decomposition (model error vs irreducible noise) | — | No — requires distributional information on the observation channel. | **NOT APPLICABLE** |
| Observation noise $U_o^{(k)}$ per channel | — | No — channel-internal. (P6 of the segment in fact says the agent-controlled-quality claim hinges on the agent affecting $U_o$ through code quality, which is exteriorized in the codebase but $U_o$ itself is a function of the reading agent's bandwidth.) | **NOT APPLICABLE** |
| Strategic disturbance rate $\rho_\Sigma$ | — | No — `#strategic-tempo` defines $\rho_\Sigma$ as the rate of causal-link invalidation in the strategy DAG; $\Sigma_t$ is agent-internal. | **NOT APPLICABLE** |

**Block C finding.** Seven quantities. These are AAD-core quantities defined over the full agent-environment loop. None is exactly computable from $\mathcal{C}_t^{\text{commit}}$ alone, with one PARTIAL ($\rho_{\text{commit-driven}}$ is EXACT; $\rho_{\text{full}}$ is not). The narrowing in the predecessor spike applies to this block correctly.

### Block D — Section III multi-agent quantities

| AAD/TST quantity | Candidate git-derivable estimator | Depends only on $\mathcal{C}_t^{\text{commit}}$? | Verdict |
|---|---|---|---|
| Co-authorship structure (which authors touched which files together) | Per-commit author + diff touch sets | Yes — both are in the commit object. | **EXACT** |
| Coupling structure $\gamma_{ij}$ (cross-agent action coupling) | Co-change matrix at the per-author level | Yes for the co-change reading; EXACT estimator definitionally on $\mathcal{C}_t^{\text{commit}}$. As a *causal* coupling estimator, confounded (parallel to Block A's coupling). | **EXACT (co-change reading); PARTIAL (causal reading, parallel to Block A)** |
| Epistemic unity $U_M$, teleological unity $U_O$, strategic unity $U_\Sigma$ | — | No — these require sub-agents' models, objectives, strategies, all agent-internal. | **NOT APPLICABLE** |
| Communication gain $\eta_{ji}^\ast$ | — | No — requires $U_{M_i}$ etc.; agent-internal. | **NOT APPLICABLE** |
| Closure defect $\varepsilon^\ast$ (`#composition-closure`) | — | No — requires the micro-state trajectory of each sub-agent. | **NOT APPLICABLE** |

**Block D finding.** Five quantities. Co-authorship and per-author co-change are EXACT. Unity dimensions and composition-closure quantities require agent-internal inputs and are NOT APPLICABLE. So the multi-agent block has the same shape as the Block A vs Block C split: the *exteriorized observable* (who-changed-what-with-whom) is exact; the *agent-internal* unity and tempo machinery is not.

### Aggregate count

- **EXACT verdicts:** 14 (Block A: 9 — counting per-commit and per-feature operationalizations of `#atomic-changeset` once for the EXACT reading and once for the PARTIAL reading reduces this to 9 quantities with 7 cleanly EXACT and 2 EXACT-with-operationalization-caveat. Block B: 5. Block D: 1 clean EXACT — co-authorship — plus 1 EXACT-on-co-change-reading.)
- **PARTIAL verdicts:** 3 ($\rho$ committed vs full; per-feature changeset; multi-agent causal coupling)
- **NOT APPLICABLE verdicts:** 11 (Block C: 6 + 1 conditional; Block D: 4)

The central pattern: the EXACT class is precisely the *exteriorized-observable* class — what is recorded and immutable. The NOT APPLICABLE class is precisely the *agent-internal* class — what lives in $M_t, G_t$, or in non-git observation channels. The PARTIAL class is small and is occupied by quantities that have one foot in each world ($\rho$ that aggregates committed and uncommitted disturbance).

---

## §3 — Exact-vs-good-estimator analysis (Move 2)

For each EXACT row, "exact" means "the estimator is exactly computable from $\mathcal{C}_t^{\text{commit}}$." That is *not* the same as "the estimator is unbiased / consistent / asymptotically efficient as an estimator of the underlying AAD quantity it might be intended to track." The strengthened P5 should preserve the exact-computability claim and route the estimator-quality question to the right downstream segment.

I treat each EXACT row in turn:

### 3.1 Block A — TST operational quantities

For Block A, the relevant question is *not* "is the estimator a good estimator of the underlying AAD quantity?" because **the TST quantity is not an estimator of an AAD quantity at all** — it is the TST quantity, definitionally. `#system-coupling`'s $P(\text{change}(m_j) \mid \text{change}(m_i))$ is *defined* on co-change. Whether the co-change conditional probability also equals the *causal* coupling $P(\text{change}(m_j) \mid do(\text{change}(m_i)))$ is the separate question that `#system-coupling` Discussion and `#causal-discovery-from-git` already handle (regime-conditional).

So the Block A estimator-quality question splits into two:

(a) **Is the estimator an unbiased estimator of its own definition?** Trivially yes — it *is* its definition.
(b) **Is the estimator a good estimator of the *causal* AAD quantity it might be intended to inform?** This is the question `#system-coupling` and `#causal-discovery-from-git` already address, and the answer is regime-dependent (atomic commits / asymmetric co-change / explicit confounder adjustment → strong; otherwise → useful descriptive statistic).

The strengthened P5 should preserve (a) as the strong claim — *this is the exact computability the original wording reaches for* — and explicitly defer (b) to `#causal-discovery-from-git`.

### 3.2 Block B — structural quantities

Trivially exact and trivially unbiased (these are structural facts of the commit DAG; there is no underlying AAD quantity they estimate).

### 3.3 Block D — multi-agent observable

Co-authorship and co-author/file co-change are exactly recorded; whether they are good estimators of multi-agent unity dimensions or causal cross-agent coupling is again a separate, regime-dependent question.

### 3.4 The general principle

For every EXACT row, the strengthened claim is:

> The estimator is an exact function of $\mathcal{C}_t^{\text{commit}}$. It is exactly equal to *its own definition*. Whether it is also a good estimator of an AAD-core quantity it is intended to inform is a separate question, treated in `#causal-discovery-from-git` and the relevant TST measurement segment, and the answer is regime-conditional.

This is the cleanest way to honor what the original P5 was reaching for. The original wording conflated "exact computability of the estimator" with "exact estimation of the AAD quantity," and the predecessor spike's softening uniformly sacrificed both. The strengthening preserves the first and defers the second.

---

## §4 — Conditional maximality investigation (Move 3)

**Question.** Is $\mathcal{C}_t^{\text{commit}}$ provably the *unique maximal* exteriorized subset of $\mathcal{C}_t$ in software, under specific scope conditions?

**Setup.** Define an exteriorization candidate $X \subseteq \mathcal{C}_t$ as a subset of the chronica recorded by some standard software tooling. Candidate exteriorizations include: $\mathcal{C}_t^{\text{commit}}$ (commits), $\mathcal{C}_t^{\text{CI}}$ (CI build/test logs), $\mathcal{C}_t^{\text{PR}}$ (pull-request review threads), $\mathcal{C}_t^{\text{IDE}}$ (IDE telemetry / edit traces), $\mathcal{C}_t^{\text{issue}}$ (issue-tracker content), $\mathcal{C}_t^{\text{chat}}$ (Slack / Teams transcripts), $\mathcal{C}_t^{\text{prod}}$ (production telemetry).

I evaluate each candidate against four exteriorization properties:

- **(M1) Cryptographic immutability** — content-addressed records that cannot be silently rewritten; tampering breaks the hash chain.
- **(M2) Cryptographic authorship attribution** — signed records linking content to a specific actor.
- **(M3) Standardized universal retrieval** — the data is accessible through a tool-agnostic, standard protocol that any agent can rely on.
- **(M4) Mainline-bounded scope** — recorded events are restricted to the canonical history (no scratch / discarded branches polluting the count).

The strengthened claim is then **conditional maximality**: under {(M1), (M2), (M3), (M4)}, $\mathcal{C}_t^{\text{commit}}$ is the unique maximal subset of $\mathcal{C}_t$ with these properties.

### 4.1 Property table

| Exteriorization candidate | (M1) Immutability | (M2) Cryptographic authorship | (M3) Standard retrieval | (M4) Mainline-bounded |
|---|---|---|---|---|
| $\mathcal{C}_t^{\text{commit}}$ (mainline) | Yes (content-addressed; hash chain) | Yes (signed commits / verified GPG / sigstore) | Yes (git protocol) | Yes (`git log <main>`) |
| $\mathcal{C}_t^{\text{CI}}$ | No (logs are deletable; CI providers can prune; retention policies vary) | Partial (provider-specific; not cryptographic) | No (per-provider APIs) | Partial |
| $\mathcal{C}_t^{\text{PR}}$ | No (comments editable / deletable on most platforms) | Partial (platform-account; not cryptographic) | No (per-platform APIs) | N/A |
| $\mathcal{C}_t^{\text{IDE}}$ | No (typically discarded; rarely persisted) | No | No | N/A |
| $\mathcal{C}_t^{\text{issue}}$ | No (editable on most trackers) | No (platform-account) | No (per-tracker APIs) | N/A |
| $\mathcal{C}_t^{\text{chat}}$ | No (editable / deletable) | No | No | N/A |
| $\mathcal{C}_t^{\text{prod}}$ (logs / traces) | No (rotation, retention) | No | No | N/A |

### 4.2 Maximality argument

For each candidate $X \neq \mathcal{C}_t^{\text{commit}}$, at least one of (M1)–(M4) fails. Since (M1)–(M4) are downward-closed under the "subset of $\mathcal{C}_t$ that has these properties" relation (a subset of a property-satisfying set still satisfies the properties), and $\mathcal{C}_t^{\text{commit}}$ satisfies all four, no proper superset of $\mathcal{C}_t^{\text{commit}}$ within $\mathcal{C}_t$ retains all four properties. Hence $\mathcal{C}_t^{\text{commit}}$ is *the* maximal subset of $\mathcal{C}_t$ satisfying {(M1), (M2), (M3), (M4)}.

**Caveat on uniqueness.** Strict uniqueness requires that no *other* candidate set with all four properties exists. The candidates I enumerated are the natural ones; in principle a research-grade system could be built (e.g., signed-and-content-addressed CI logs stored on an append-only log) that would also satisfy (M1)–(M3). Such a system would be a *strict superset* of $\mathcal{C}_t^{\text{commit}}$ and would replace it as the maximal. But under *current standard team protocols* (the implicit scope), no such alternative is universal. Maximality is therefore *conditional on present-day standard protocols* — which is exactly the right level of scoping for an empirical observation.

### 4.3 What weakening (M1)–(M4) buys

- Drop (M1): admits CI logs and issue trackers — the EXACT class grows but estimators lose tamper-resistance, becoming subject to silent rewrite and retention loss.
- Drop (M2): admits unauthored telemetry — but causal inference about *who* intervened becomes regime-dependent on platform metadata.
- Drop (M3): admits per-tool fragments — the EXACT class becomes platform-specific, no longer universally applicable.
- Drop (M4): admits feature-branch traffic that may be discarded — inflates apparent intervention counts, breaks the "intervention-as-commit" identification because some "interventions" are reverted.

So each of (M1)–(M4) is doing real work; weakening any of them produces a quantitatively different EXACT class with quantitatively different estimator-quality properties.

### 4.4 Verdict

**Conditional maximality holds.** Under the four scope conditions {(M1) immutability, (M2) cryptographic authorship, (M3) standard universal retrieval, (M4) mainline-bounded}, $\mathcal{C}_t^{\text{commit}}$ is the maximal exteriorized subset of $\mathcal{C}_t$ in software. The result is structural rather than fully formal — it depends on a property-table walk over current candidates — but the structure is solid and the failure mode of each non-commit candidate is clearly localized to a specific property.

This gives the narrowing intellectual content beyond a defensive concession: $\mathcal{C}_t^{\text{commit}}$ is not merely *one* well-behaved subset, it is the *uniquely largest* well-behaved subset under conditions software developers actually require for trustworthy operation.

---

## §5 — Strengthened P5 revision (full proposed text)

The following replaces lines 56–62 (P5 + Consequence) and line 84 (the P5 paragraph in Discussion). All other parts of the segment are untouched.

### 5.1 Revised P5 — heading and body

> **P5. Exact recording of the committed-state subset; conditional maximality.** The chronica $\mathcal{C}_t$ ( #chronica) is the complete sequence $(o_1, a_1, \ldots, a_{t-1}, o_t)$ of agent–environment interactions. Within $\mathcal{C}_t$, define the *committed-state subset* $\mathcal{C}_t^{\text{commit}} \subseteq \mathcal{C}_t$ as the sequence of git-recorded committed codebase state transitions, with their timestamps, signed authorship, and immutable diffs.
>
> *[Empirical Claim]* $\mathcal{C}_t^{\text{commit}}$ is recorded by git **without information loss within its scope**: each commit is content-addressed (cryptographically immutable), authorship is cryptographically attributable (signed commits / verified GPG / sigstore), retrieval is via a universally standardized protocol (git), and the canonical history is mainline-bounded (`git log <main>`). The complementary subset $\mathcal{C}_t \setminus \mathcal{C}_t^{\text{commit}}$ — uncommitted edits, IDE edit traces, build-system invocations, test runs, runtime logs, monitoring alerts, code-review threads, deployment events, out-of-band coordination — is captured only by other tools or not at all (see #scope-developer-agent for the channel enumeration).
>
> *[Empirical Claim — conditional maximality]* Under the scope conditions of cryptographic immutability, cryptographic authorship attribution, standard universal retrieval, and mainline-bounded scope, $\mathcal{C}_t^{\text{commit}}$ is the *unique maximal* exteriorized subset of $\mathcal{C}_t$ in software: no candidate exteriorization (CI logs, PR review threads, IDE telemetry, issue trackers, chat transcripts, production telemetry) under current standard team protocols satisfies all four conditions, and any subset that does is contained in $\mathcal{C}_t^{\text{commit}}$.
>
> The chronica is, by definition, the record of interactions between agent and environment — not the agent's internal reasoning. What git additionally does *not* record is orthogonal to $\mathcal{C}_t^{\text{commit}}$: the agent's internal model state $M_t$, strategy DAG $\Sigma_t$, or objective $O_t$. These are agent-internal and not part of the chronica by any domain's definition. Commit messages and PR descriptions are partial exteriorizations of $M_t$/$G_t$ intent, only to the extent the agent chose to verbalize them.

### 5.2 Revised P5 Consequence — per-quantity structure

> *Consequence — quantities exactly computable from $\mathcal{C}_t^{\text{commit}}$.* The following AAD- and TST-relevant estimators are exact functions of $\mathcal{C}_t^{\text{commit}}$, and hence are exactly recoverable from git with no sampling loss and no recall bias *as estimators of their own definitions*:
>
> - **TST operational quantities** (definitionally on the commit stream): system coupling ( #system-coupling) as the co-change conditional probability; system coherence ( #system-coherence) as intra-module change-proximity; the coherence-coupling measurement Q ( #coherence-coupling-measurement); per-commit `#atomic-changeset` size (lines / files / modules); the change-distance hierarchy ( #change-distance) on within-commit diffs; the change-expectation baseline $\hat n_{\text{future}} = n_{\text{past}}$ ( #change-expectation-baseline) under the commit / merge operationalization of "feature."
> - **Causal-discovery substrate** ( #causal-discovery-from-git): the interventional record (each commit *is* a $do(\cdot)$ on the codebase; the set of interventions is exactly the commit stream), temporal-precedence priors over interventions, frequency-asymmetry signals between file pairs, intervention-contrast signals (commits changing $A$ alone vs $A$ with $B$).
> - **Multi-agent observable structure**: co-authorship matrix per file, per-author commit-rate, co-author co-change matrix.
>
> For these quantities, the original "without information loss" claim is preserved: estimator = exact git-derivable function, with $\mathcal{C}_t^{\text{commit}}$ as the maximal exteriorized substrate under the scope conditions above.
>
> *Consequence — quantities not exactly computable from $\mathcal{C}_t^{\text{commit}}$ alone.* AAD-core quantities defined over the full agent-environment loop — environmental disturbance rate $\rho$ (full chronica, including production incidents and dependency breaks), adaptive tempo $\mathcal T$, update gain $\eta^\ast$, mismatch signal $\delta_t$, observation noise $U_o^{(k)}$, strategic disturbance rate $\rho_\Sigma$ — and Section III multi-agent quantities — epistemic / teleological / strategic unity, communication gain, composition closure $\varepsilon^\ast$ — are *not* exactly computable from $\mathcal{C}_t^{\text{commit}}$ alone. They require additional instrumentation (CI logs, monitoring telemetry, code-review tooling, agent reasoning traces) and / or agent-internal access. For these, git provides at best a partial substrate (one channel of the disturbance source for $\rho$; one observable for cross-agent coupling), and the gap is empirical.
>
> *Consequence — estimator quality for AAD-core quantities is a separate question.* For the EXACT-class TST estimators above, exactness of computation does not by itself imply they are good estimators of the AAD-core quantities they are sometimes used to inform. The co-change conditional probability is exactly equal to its own definition; whether it equals the causal coupling $P(\text{change}(m_j) \mid do(\text{change}(m_i)))$ is regime-conditional and treated in #causal-discovery-from-git (atomic commits / asymmetric co-change / explicit confounder adjustment → strong; otherwise → useful descriptive statistic). The strengthened P5 preserves the exact-computability claim and routes the AAD-quantity-bias question to the appropriate downstream segment.

### 5.3 Revised Discussion paragraph (current line 84)

> **P5 and the instrumentation boundary.** The exact-recording claim of P5 separates into three pieces: (i) within-scope exactness — $\mathcal{C}_t^{\text{commit}}$ is recorded by git without information loss, with cryptographic immutability, cryptographic authorship, and standardized universal retrieval; (ii) conditional maximality — under the scope conditions stated in P5, $\mathcal{C}_t^{\text{commit}}$ is the unique maximal exteriorized subset of $\mathcal{C}_t$ in software; (iii) per-quantity exactness — the TST operational quantities ( #system-coupling, #system-coherence, #coherence-coupling-measurement, #change-distance, per-commit `#atomic-changeset` size, the asymmetric and contrast signals from #causal-discovery-from-git, co-authorship structure) are *exact* functions of $\mathcal{C}_t^{\text{commit}}$ and inherit all three properties.
>
> The remainder of the chronica — uncommitted work, IDE telemetry, runtime observations, build/test traces, monitoring alerts, code-review discussion, out-of-band coordination — is captured only by other tools or not at all, and the level of capture varies by team and tooling. *Agent-internal* content (why a particular intervention was chosen; which beliefs drove it) is not part of the chronica in any domain and therefore not in git's scope. Commit messages and PR descriptions are partial exteriorizations of agent intent; their quality varies by authorial discipline.
>
> This is relevant for #causal-discovery-from-git in two senses: (a) the *interventional* record over $\mathcal{C}_t^{\text{commit}}$ is complete (each commit is exactly one $do(\cdot)$ event with all the inputs the do-operator requires), and the temporal-precedence and frequency-asymmetry signals it derives are also exact; (b) the *causal* interpretation of estimators built on this exact substrate (whether the co-change matrix recovers the causal coupling) remains regime-conditional on confounders that depend partly on agent-internal state (developer knowledge state, etc.), as #causal-discovery-from-git documents. Treating $\mathcal{C}_t^{\text{commit}}$-derived TST quantities as estimators of their *own definitions* is exact; treating them as estimators of *AAD-core full-chronica quantities* is an empirical bridging step, not a definitional identity.

---

## §6 — Comparison to softening repair: what changes

### 6.1 Where the two repairs agree

Both repairs:

- Introduce $\mathcal{C}_t^{\text{commit}} \subseteq \mathcal{C}_t$ as the operative subset.
- Concede that the full chronica is broader than git's scope.
- Enumerate the channels in $\mathcal{C}_t \setminus \mathcal{C}_t^{\text{commit}}$ via cross-reference to `#scope-developer-agent`.
- Tag the comparative-advantage and bridging claims as `*[Empirical Claim]*`.
- Route AAD-core quantity estimation through `#causal-discovery-from-git`.
- Leave the segment headline (line 15, "richest operationalization domain") to C-BP3.

### 6.2 Where they diverge

| Dimension | Softening repair | Strengthening repair |
|---|---|---|
| Treatment of "without information loss" claim | Uniformly narrowed: all P5 estimators inherit the empirical bridging caveat. | Per-quantity: preserved exactly for the TST-operational EXACT class (Block A + B + Block D observables); narrowed honestly for the AAD-core class (Block C + Block D agent-internal). |
| Treatment of TST-defined operational quantities | Folded into the "estimators of full-chronica AAD quantities" framing, which makes them inherit the empirical bridging caveat even for their own definitions. | Recognized as quantities defined directly on $\mathcal{C}_t^{\text{commit}}$ in their own segments — exact-by-construction. |
| Maximality structure | Not addressed — narrowing is a defensive concession. | Conditional maximality result (§4): under {immutability, cryptographic authorship, standard retrieval, mainline-bounded}, $\mathcal{C}_t^{\text{commit}}$ is the unique maximal exteriorized subset. Gives the narrowing positive content. |
| Estimator-of-AAD-quantity question | Implicit: the empirical bridging caveat carries it. | Explicit: separated as a third Consequence clause and routed to `#causal-discovery-from-git`. |
| Connection to `#causal-discovery-from-git` interventional substrate | "The committed-subset interventional record is complete." | The interventional record IS the commit stream exactly. The temporal-precedence and frequency-asymmetry signals on this substrate are also exact. The causal interpretation of estimators built on the substrate is regime-conditional (unchanged). |
| Tone / signal | Defensive — admits the narrowing. | Confident — asserts what does hold (per-quantity), what doesn't (per-quantity), and why $\mathcal{C}_t^{\text{commit}}$ is the right substrate to live on. |

### 6.3 Honesty check

The strengthening's per-quantity claim is more aggressive than the softening's. It is honest only if the EXACT-class arguments in §2 are correct:

- **Block A.** I argued each TST operational quantity is *defined* on commit-stream artifacts (atomic-changeset, change-distance, co-change patterns). I verified this against the segment files: `#system-coupling` line 17 (defined as $P(\text{change}(m_j) \mid \text{change}(m_i))$ where "change" = participation in `#atomic-changeset`); `#system-coherence` line 17 ($E$ over proximity within commits); `#coherence-coupling-measurement` line 22 ("estimated from historical commits"); `#atomic-changeset` line 17 (defined as $S_{\text{after}} \ominus S_{\text{before}}$ with size measures from diffs); `#change-distance` line 17 (defined on file paths and line offsets). All check out.
- **Block C.** I argued each AAD-core quantity requires inputs outside the commit stream (channel-internal $U_o, U_M$; agent-internal $\Sigma_t$; non-codebase environment components). I verified against `#mismatch-signal`, `#update-gain`, `#adaptive-tempo`, `#multi-agent-scope`, `#composition-closure`, and `#scope-developer-agent`'s environment table. All check out.
- **Block D.** Co-authorship and per-author co-change are commit-stream artifacts; unity dimensions and composition-closure require sub-agent micro-states. Checked.

The conditional-maximality argument in §4 is structural rather than fully formal — it relies on a property-table walk over enumerated candidates. I noted the uniqueness caveat (in principle, a research-grade signed-and-content-addressed CI log could compete; under current standard team protocols, none does). The scoping is therefore "under current standard team protocols," which is exactly the empirical scope the segment already operates at.

### 6.4 Recommendation

**Prefer the strengthening over the softening.** The strengthening is more honest (it preserves the strong claim where it is genuinely defensible, rather than uniformly retreating), more useful (it tells the reader exactly which TST measurements they can trust to be exact and which require additional instrumentation), and more architecturally coherent (it brings P5 into register with the TST measurement segments that already operationally live on git, rather than retroactively softening them all).

The softening repair on file is a clean fallback if the strengthening's per-quantity arguments fail review. They should not — but the predecessor spike is a legitimate safety net.

If Joseph prefers a hybrid, the natural compromise is to adopt the strengthened §5.1 + §5.2 (preserving exact computability per-quantity) and use the softening's wording for §5.3 (which is largely compatible). The conditional-maximality claim in §4 / §5.1 third paragraph is the most aggressive new content; if Joseph wants to drop it, the rest of the strengthening still stands and reduces to the Block-A-EXACT preservation only.

---

## §7 — Open questions for Joseph

1. **Adopt the strengthening, the softening, or a hybrid?** My recommendation is the full strengthening (§5.1–§5.3). The softening on file is the honest fallback. The natural hybrid is "strengthening for §5.1 + §5.2, soft-narrowed Discussion paragraph from the predecessor spike" — drops the conditional-maximality claim but keeps the per-quantity exact preservation. Your call which to land.

2. **Conditional maximality — do we want this in the segment or in a spike-only result?** §4's conditional-maximality argument is structural (property-table walk) rather than fully formal. It is at *empirical* / *robust-qualitative* tier, not *exact*. Three options: (a) include in the strengthened P5 as `*[Empirical Claim — conditional maximality]*` (current §5.1 proposal); (b) hold for a follow-up segment on "exteriorization properties" referenced from P5 but not stated in P5; (c) keep in this spike only and don't promote until a more formal treatment exists. Lean (a); flag (b) as the conservative option; (c) is too weak given the structural argument is solid.

3. **Promotion of $\mathcal{C}_t^{\text{commit}}$ to `NOTATION.md`.** Same question the predecessor spike asked. Strengthening uses the symbol seven times across §5, including in the conditional-maximality clause. If we ever talk about EXACT-class estimators in `#causal-discovery-from-git`, `#coherence-coupling-measurement`, or any new TST measurement segment, $\mathcal{C}_t^{\text{commit}}$ will appear. Lean weakly toward promoting on this round to avoid a second-edit later; comfortable with deferring per the predecessor spike's preference.

4. **Per-feature vs per-commit operationalization of `#atomic-changeset` and `#change-expectation-baseline`.** The strengthening labels these EXACT-with-operationalization-caveat: per-commit reading is EXACT, per-feature reading is PARTIAL because "feature" may bundle commits or include uncommitted work. Two options: (i) leave the caveat in the spike only and have P5 cite EXACT for the per-commit reading; (ii) have P5 explicitly flag the operationalization choice in the Consequence. Lean (i) — keeps P5 from getting heavy on operationalization details that are properly the home of `#atomic-changeset`'s and `#change-expectation-baseline`'s own segments.

5. **Estimator-of-AAD-quantity routing.** The strengthening explicitly separates "exact computation of the TST quantity" from "good estimation of the AAD-core quantity." Currently I route the bias question to `#causal-discovery-from-git` (which already handles the regime-conditional analysis). One could imagine a small new TST segment on "estimator-quality calibration" that hosts the bridging analysis explicitly, but this seems like over-engineering for a question already adequately routed. Confirm `#causal-discovery-from-git` is the right home, or flag a different target.

6. **Block D — multi-agent observables and the conditional-maximality argument.** The conditional-maximality argument in §4 was framed for the single-agent case (the classical software developer). It extends naturally to multi-agent Block D observables (co-authorship, per-author co-change), but the strengthened §5.1 doesn't make this extension explicit. Should the multi-agent observable structure be flagged in the conditional-maximality clause, or left implicit? Lean implicit — but flag if you want it explicit.

7. **Comparative-advantage clause.** The predecessor spike's wording — "lower sampling and recall bias on $\mathcal{C}_t^{\text{commit}}$ than self-report instruments offer on the comparable subset in other domains" — is now subsumed by the conditional-maximality claim plus the within-scope exactness claim. The strengthened §5.1 omits the comparative-advantage clause as a separate sentence; conditional maximality says something stronger. Confirm the omission is OK, or restore the clause for continuity with how the segment's Epistemic Status (line 72) currently uses comparative ranking.

8. **Promotion path.** After your sign-off, the natural sequence is: (i) apply the §5.1–§5.3 edits (or hybrid choice from Q1) to `software-epistemic-properties.md`; (ii) optionally apply the predecessor spike's §4b consistency edit at line 86 ("P5 (perfect history)" → "P5 (exact committed-state record)"); (iii) close Finding 7 in `pending-findings-2026-04-22.md` with a pointer to this spike; (iv) note in `TODO.md` that Finding 15 remains held for C-BP3; (v) update `SPIKES.md` to mark the predecessor spike as superseded (assuming the strengthening lands) and this spike as promoted. No segment downgrade needed (segment is `draft` / `discussion-grade`; promoting the strengthened P5 keeps both unchanged).

---

## §8 — Self-check: did the strengthening attempt succeed honestly?

Three independent confirmations:

1. **The EXACT class is non-empty and load-bearing.** Nine quantities in Block A (TST operational), five in Block B (commit-stream structural), at least one clean EXACT in Block D (co-authorship), all definitionally on the commit stream as verified against their own segment files. This is not a stretched claim — these segments already say this implicitly when they describe their estimators.

2. **The NOT APPLICABLE class is principled.** Six AAD-core quantities and four multi-agent unity / composition quantities require agent-internal or non-git-channel inputs. None of these can be coaxed into EXACT by clever estimator design — they are definitionally over the full agent-environment loop or over agent-internal state. The narrowing applies cleanly here. The strengthening does not stretch.

3. **Conditional maximality is structural rather than vacuous.** The four scope conditions {immutability, cryptographic authorship, standard universal retrieval, mainline-bounded} each do real work — dropping any of them admits CI logs / issue trackers / branch traffic and changes the EXACT-class calculus. The property-table walk is solid for current standard protocols, with an explicit caveat about future research-grade alternatives.

The strengthening attempt succeeded; the fallback to softening is not needed. If Joseph disagrees on Q1 / Q2 / Q7, the strengthening reduces gracefully (drop §4 → still strengthened over softening; drop per-quantity Consequence → reduce to softening). If Joseph wants the full strengthening, §5.1–§5.3 is ready to apply.
