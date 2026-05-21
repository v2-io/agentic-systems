---
purpose: Strengthening spike for `schema-strategy-persistence` — attempt to lift `status: sketch` to `conditional` (or higher) following the §D.3 landing of the exact form $(1-\lambda)/(2-\lambda)$ and the hard ceiling $\rho_\Sigma \geq R_\Sigma/2$.
date: 2026-05-20
agent: Opus 4.7 (1M context), spike sub-agent under parent adjudication 451729 D.1 Phase 4a
target_segment: 01-aat-core/src/schema-strategy-persistence.md
completion_state_pending: Outcome A (with stronger candidates surfaced — see §3)
adjudication_parent: msc/451729-d1-gate-verification-2026-05-20.md §6
---

# Spike: Strengthening `schema-strategy-persistence` (sketch → conditional or higher)

## 1. Context

The Gate-2 verification cycle for audit 451729's D.1 hypothesis identified `schema-strategy-persistence` as the strongest candidate for status promotion in the Class A set. The segment currently carries `status: sketch`, but the §D.3 landing on 2026-05-12 (commit `b9b146c`) added substantive math:

- **The exact steady-state sector parameter** under exponential forgetting: $\alpha_\Sigma^{\text{ss}} = (1-\lambda)/(2-\lambda)$, derived from the canonical Beta-Bernoulli $\alpha = 1/(n+1)$ with the effective sample size $n_{\text{eff}} = 1/(1-\lambda)$ that stabilizes the discounted update.
- **The hard ceiling** $\rho_\Sigma \geq R_\Sigma/2$: when disturbance-to-reserve ratio reaches half, no $\lambda \in (0,1)$ satisfies the forgetting prerequisite. Surfacing this ceiling was the §D.3 strengthen-first result — it had been *hidden* by the prior linear approximation $\alpha_\Sigma^{\text{ss}} \approx 1-\lambda$.

The §D.3 work was the strengthening; this spike's question is whether the segment's current `status: sketch` label still tracks truth, or whether — per `doc/audit-routing-instructions.md` §4–6 and the integration-is-replacement discipline (`~/.claude/memory/epistemic-discipline/integration-is-replacement.md`) — leaving `sketch` in place after the landing is the "down-tier exact result because it is new" failure mode.

Strengthen-before-soften (and its landing-half *integration is replacement*) governs here. The four legitimate completion-states are A/B/C/D per `doc/audit-routing-instructions.md` §3. The recorded calibration — that peer-agent confidence about strengthening outcomes is unreliable in either direction (Cluster B's Model-S spike, CHANGELOG 2026-05-16) — keeps me honest about not relaying optimism. The math has to be re-derived independently and the conditional structure named explicitly.

## 2. Attempt

### 2.1 First-hand reading

I read the full segment, `deriv-edge-credence-dynamics` (lines 1–447 — Props B.1–B.7 are the source of every $\alpha_\Sigma$ formula the schema instantiates; the unread tail 448–672 carries B.5/B.6/B.7 details that the segment cites by name and that I did not deem load-bearing for this adjudication, since the schema's strengthening question is upstream of the per-topology landings), `result-sector-persistence-template` (full), `result-persistence-condition` (full — the structural-identity claim's other half), `result-sector-condition-stability` (full), `FORMAT.md` (tier definitions and segment-set discipline), `doc/audit-routing-instructions.md` (full), the audit-451729 D.3 hypothesis text, and the canonical terminology entries (`conditional`, `robust-qualitative`, `proposed-schema`, `status-sketch`).

### 2.2 Independent re-derivation of the exact form

I re-derived the steady-state algebra from first principles, not relying on the segment text:

The discounted Beta-Bernoulli update is

$$\alpha_k \mapsto \lambda \alpha_k + y_k, \quad \beta_k \mapsto \lambda \beta_k + (1 - y_k).$$

In expectation at a fixed point (where $\hat p = \theta$):

$$\alpha^\ast = \lambda \alpha^\ast + \theta \implies \alpha^\ast = \theta/(1-\lambda),$$
$$\beta^\ast = \lambda \beta^\ast + (1-\theta) \implies \beta^\ast = (1-\theta)/(1-\lambda),$$
$$n_{\text{eff}} = \alpha^\ast + \beta^\ast = 1/(1-\lambda).$$

Substituting into Prop B.1's $\alpha_\Sigma = 1/(n+1)$ at the effective sample size:

$$\alpha_\Sigma^{\text{ss}} = \frac{1}{n_{\text{eff}} + 1} = \frac{1}{1/(1-\lambda) + 1} = \frac{1-\lambda}{1 + (1-\lambda)} = \frac{1-\lambda}{2-\lambda}. \quad \square$$

This is *algebraically exact* — the only conditions are (i) the Beta-Bernoulli edge-update model from `#deriv-edge-credence-dynamics`, and (ii) the discounted-update rule (exponential forgetting, Ljung 1987 standard). No approximation enters. The slow-forgetting linear form $1-\lambda$ is the asymptotic expansion as $\lambda \to 1$, with the $1/(2-\lambda) \to 1/(1)$ damping factor going to unity exactly in that limit and dominating elsewhere.

I numerically verified the overstatement of the linear approximation at the values the segment cites: at $\lambda = 0.5$, exact $1/3 \approx 0.333$ vs linear $0.5$ — overstatement $50\%$ (segment cites "~50%"). At $\lambda = 0.9$, exact $1/11 \approx 0.0909$ vs linear $0.1$ — overstatement $10\%$ (segment cites "~10%"). The segment's quantitative claims are correct to the digits stated.

### 2.3 Independent re-derivation of the hard ceiling

The forgetting prerequisite is $(1-\lambda)/(2-\lambda) \gt \rho_\Sigma/R_\Sigma$. Let $x = \rho_\Sigma/R_\Sigma$. Solving for the threshold $\lambda$ at which equality holds:

$$(1-\lambda) = x(2-\lambda) \implies 1 - \lambda = 2x - x\lambda \implies \lambda(x - 1) = 2x - 1 \implies \lambda = \frac{2x - 1}{x - 1} = \frac{1 - 2x}{1 - x} \quad (x \lt 1).$$

For $\lambda \in (0, 1)$ to admit a strict solution to the inequality, we need $\lambda \gt 0$ at the threshold, i.e., $(1-2x)/(1-x) \gt 0$. With $x \lt 1$ (the denominator is positive), this requires $1 - 2x \gt 0$, i.e., $x \lt 1/2$.

At $x = 1/2$ exactly: $\lambda = 0$, giving $\alpha_\Sigma^{\text{ss}} = (1-0)/(2-0) = 1/2 = x$ — equality, not strict satisfaction. For $x \gt 1/2$, no $\lambda$ satisfies the strict inequality; even $\lambda = 0$ (no memory, fully discounted history) only achieves $\alpha_\Sigma^{\text{ss}} = 1/2$.

This is a *class-level no-go on the schema's trajectory guarantee*: when disturbance reaches half the strategic reserve, the schema cannot be satisfied **at all** under exponential forgetting, regardless of $\lambda$ choice. The ceiling is sharp and structural — it is not an artifact of any tuning parameter. The supremum of $\alpha_\Sigma^{\text{ss}}$ over $\lambda \in [0, 1]$ is exactly $1/2$ (achieved as $\lambda \to 0^+$), so the schema's reachable persistence region in $(\rho_\Sigma, R_\Sigma)$ space is exactly the open half-plane $\rho_\Sigma \lt R_\Sigma/2$. $\square$

(I ran a numerical check to confirm the boundary behavior: at $x = 0.49$, $\lambda^\ast \approx 0.039$ with strict satisfaction on either side as expected; at $x = 0.50$, sup is $0.5$, achieved at $\lambda = 0$, with no strict satisfaction; at $x = 0.51$, sup is still $0.5$ at $\lambda = 0$, which is $\lt 0.51$. Confirms the analytic boundary.)

### 2.4 Identifying the conditional structure

Per the `conditional` tier definition: "depends on explicitly named local assumptions that are not globally established." The schema's load-bearing claims — the exact threshold and the hard ceiling — hold under the following explicit conditions, each of which is either an upstream postulate or a local assumption named in the segment itself:

1. **Beta-Bernoulli edge dynamics** (named in §Formal Expression and §Forgetting as Prerequisite). Established for five topologies in `#deriv-edge-credence-dynamics` Props B.1–B.6 (covering single-edge AND, two-edge AND observable, two-edge AND unobservable plan-level, two-arm OR with $\varepsilon$-greedy, L1-augmented DAG with common cause). The schema's form (single sector parameter $\alpha_\Sigma$ with persistence iff $\alpha_\Sigma \gt \rho_\Sigma/R_\Sigma$) holds *across* these five topology cases — that is the multi-instance evidentiary base. The Prop B.7 case (L1' mixture with unobservable $C$) is a *refutation* result with its own Cramér-Rao floor structure — outside the schema's persistence form but on the same theoretical surface.
2. **Exponential forgetting with discount $\lambda \in (0, 1)$** (named in §Forgetting as Prerequisite). Specified by the recurrence in §2.2 above; standard adaptive-control / online-learning machinery (Ljung 1987, the cited formal antecedent in §Findings).
3. **Sector-persistence template preconditions (T1)–(T3)** of `#result-sector-persistence-template`. The schema's persistence form is "directly by the template's Model D result"; (T1) and (T2) are established by the Prop B.1–B.6 derivations (sector condition verified globally for the canonical Beta-Bernoulli case); (T3) is the domain parameter $\rho_\Sigma$ (Model D — bounded disturbance) — left as a domain parameter per `#schema-strategy-persistence` §Discussion §3.
4. **The mismatch state choice** is named explicitly: per-edge credence error $\boldsymbol\delta_c$ or the plan-level surrogate $\delta_s$ (Prop B.5 transfer). Persistence is *proved* for these; $\delta_{\text{strategic}}$ from `#def-strategic-calibration` (the credit-assigned form) remains open, named as such in §Formal Expression and §Discussion §1.

These conditions are all **explicit and locally named** in the segment, in upstream segments cited by `depends:`, or both. Within the named conditions, the two load-bearing pieces — the exact $(1-\lambda)/(2-\lambda)$ and the hard ceiling — are *algebraically exact* (re-derived above without slack).

This is the conditional-tier signature: provably true under stated conditions, where the uncertainty lives in whether the conditions hold (which mismatch state, which topology, whether forgetting is in fact exponential vs some other discounting scheme), not in the derivation.

### 2.5 Where the schema sits in the type-status grid

The segment's `type: proposed-schema` is the right type — per the canonical entry, "the mathematical *shape* of a claim ... before the formal content is complete." The schema is the form $\alpha_\Sigma \gt \rho_\Sigma/R_\Sigma$, which is a shape that instantiates across multiple mismatch-state choices. The §D.3 work did not change the type to `result` (which would require collapsing to a single instantiation), but it *did* fill in formal content for the specific mismatch states named.

Crucially, the tier-and-type axes are orthogonal (per FORMAT.md and the `proposed-schema` entry). A `proposed-schema` can carry `status: conditional` if its load-bearing instantiations are themselves at `exact`-under-conditions and the schema's role is to organize them. Looking at the type/status table in `FORMAT.md`:

- `type: result` + `status: exact` would be: collapse the schema to one canonical mismatch-state choice with one canonical topology. This is what `#result-persistence-condition` and `#result-sector-condition-stability` do for the epistemic case.
- `type: proposed-schema` + `status: conditional` would be: keep the schema as a schema (it organizes multiple instances), and label its truth status as holding-under-named-conditions. This matches the actual state of the segment after §D.3.

The current `type: proposed-schema` + `status: sketch` is the *pre*-§D.3 labeling. The §D.3 landing made the schema's load-bearing instantiations algebraically exact (under named conditions) and added a class-level no-go (the hard ceiling). `sketch` no longer tracks present truth.

### 2.6 Is there a stronger landing than `conditional`?

I considered three candidate higher-tier landings:

**(a) `robust-qualitative`.** This is the wrong direction — the qualitative claim ("forgetting prerequisite exists") was already established; the §D.3 work made the *quantitative form* exact. `robust-qualitative` would be a *demotion* from what is actually in hand, since it explicitly states "specific form is approximate" — the opposite of where the math now sits.

**(b) `exact`.** This would require the conditions in §2.4 to be globally established by the dependency chain, not stated as local assumptions. They are not — choice of mismatch state, choice of topology (which of B.1–B.6), and the exponential-forgetting model are all local choices, not framework-global commitments. So `exact` is unreachable at the schema-level. A *spawned segment* that collapses to a specific topology + specific mismatch state + the exponential-forgetting model could be `type: result, status: exact` (mirroring how `#result-sector-condition-stability` instantiates the template) — see §4 for the recommended canon disposition.

**(c) `type: result, status: exact` via a hard-ceiling appendix.** The hard ceiling $\rho_\Sigma \geq R_\Sigma/2$ is *itself* a result strong enough to stand alone: a class-level no-go on the schema's reachable persistence region under any $\lambda$. This is the (B) "Strengthened past the claim" landing on the four-state ledger — the spike produces a result the original claim did not contain. The natural canonical home is a new appendix segment co-located with `#deriv-edge-credence-dynamics`, type `derivation`, status `exact` (algebraically exact, no slack, conditions named), surfaced as a Finding (the hard ceiling already has a Brief-grade statement in the schema's existing Findings entry; it would migrate to the appendix with strengthened Impact and the algebra shown in §2.3).

The schema segment itself, with the appendix landed, would still be the right home for the *schema* (the form, the cross-topology instantiation, the connection to `#result-sector-persistence-template`'s instantiation row). Its appropriate label after both moves: `type: proposed-schema, status: conditional`. The (B) landing produces *both* the lift of the schema-as-schema (from `sketch` to `conditional`) *and* the appendix carrying the hard-ceiling no-go at `exact`.

This is the integration-is-replacement protocol's typical (A)+(B) compound landing — the schema isn't going away (it has work to do organizing the instantiations and connecting them to the template); but the bare-fact exactness of the load-bearing pieces lives in their own canonical home where downstream segments cite them directly.

## 3. Outcome

**Completion-state: A (Strengthened to the claim) with a (B) candidate (Strengthened past the claim) attached.**

- **(A) The status lift `sketch → conditional` for `schema-strategy-persistence` itself.** The exact threshold $(1-\lambda)/(2-\lambda)$ is algebraically exact under explicit local conditions named in §2.4 (Beta-Bernoulli edges; exponential forgetting; template (T1)–(T3); a mismatch state from $\{\boldsymbol\delta_c, \delta_s\}$). The conditional structure is clean — every condition is either named in the segment or in an upstream segment cited by `depends:`. The hard ceiling at $\rho_\Sigma \geq R_\Sigma/2$ is likewise algebraically exact under the same conditions. `status: conditional` tracks current truth; `sketch` does not (it under-states the §D.3 landing).

- **(B) The class-level no-go in its own canonical home.** The hard ceiling $\rho_\Sigma \geq R_\Sigma/2$ is itself a class-level no-go on the schema's reachable persistence region under any forgetting design — a stronger result than the schema's original framing carried. Naturally landed as a new appendix derivation segment co-located with `#deriv-edge-credence-dynamics`, type `derivation`, status `exact` (the conditions are then in the segment's `depends:` chain, satisfying the `exact`-vs-`conditional` distinction). Per `doc/audit-routing-instructions.md` §5 ghost-form (A) — *"its own no-go theorem, in an appendix, especially if the result is surprising or counter-intuitive"* — and per the project's `math-lives-in-segments` discipline (FORMAT.md), this is where the no-go belongs.

**The load-bearing math** (Re-derived independently above; see §2.2 and §2.3):

1. $\alpha_\Sigma^{\text{ss}} = (1-\lambda)/(2-\lambda)$ exactly, derived from the discounted-update steady state $n_{\text{eff}} = 1/(1-\lambda)$ substituted into Prop B.1's $\alpha_\Sigma = 1/(n+1)$. Conditional on Beta-Bernoulli edges + exponential forgetting.
2. The schema's reachable persistence region under any $\lambda \in [0, 1]$ is exactly the open half-plane $\rho_\Sigma \lt R_\Sigma/2$. Equivalently: $\sup_{\lambda \in [0,1]} \alpha_\Sigma^{\text{ss}}(\lambda) = 1/2$ (achieved as $\lambda \to 0^+$, i.e., maximally aggressive forgetting). The supremum is the schema-level structural cap on what forgetting can achieve.

## 4. Recommended canon disposition

**Required edits (if Joseph signs off):**

### 4.1 Schema segment frontmatter
`01-aat-core/src/schema-strategy-persistence.md`: `status: sketch` → `status: conditional`. The `type: proposed-schema` is retained (the schema is still a schema — it organizes multiple instantiations; collapse to `type: result` would require pinning a single instantiation, which is downstream work not done here). The `stage: draft` remains (Gate 1 dependency audit and Gate 2 content review would need to be run; the Working Notes section also needs to be cleaned at Gate 4 — see §4.3 below; status lift is upstream of stage advance).

### 4.2 New appendix derivation segment
`01-aat-core/src/deriv-strategic-persistence-hard-ceiling.md` (slug per FORMAT.md role-prefix mapping: `deriv-` for `derivation`-type; subject noun `strategic-persistence-hard-ceiling`). Frontmatter:

```yaml
---
slug: deriv-strategic-persistence-hard-ceiling
type: derivation
status: exact
depends:
  - schema-strategy-persistence
  - deriv-edge-credence-dynamics
  - result-sector-persistence-template
stage: draft
---
```

Body: the §2.2 and §2.3 derivations rendered in segment voice (no "this spike found ..." — segment-voice present truth per FORMAT.md). Title: *"Derivation: Hard Ceiling on Strategic-Persistence Reachability under Exponential Forgetting."* The Findings entry currently sitting in `schema-strategy-persistence.md` ("The Forgetting Prerequisite for Strategic Persistence") would be split: the exact-form half stays in the schema (its Brief and Impact are about the schema-level prerequisite); the hard-ceiling half moves to the new appendix's own Findings entry, with strengthened Impact naming the class-level cap on $\sup_\lambda \alpha_\Sigma^{\text{ss}} = 1/2$.

### 4.3 Schema-segment body edits (minimal, only what is needed to track the new conditional label)
The §Forgetting as Prerequisite text already states the exact form, the hard ceiling, and the conditional structure faithfully (it was rewritten in the §D.3 cycle). Two small clarifications would land in the same cycle:

- Add a sentence under §Forgetting as Prerequisite naming the new appendix: *"The hard-ceiling no-go above is the algebraic content of `#deriv-strategic-persistence-hard-ceiling`."*
- The Epistemic Status paragraph currently reads "*Sketch, with verified instances.*" — replace with "*Conditional, conditioned on (i) Beta-Bernoulli edge dynamics, (ii) exponential forgetting with $\lambda \in (0,1)$, (iii) template preconditions (T1)–(T3), and (iv) the mismatch state chosen from $\{\boldsymbol\delta_c, \delta_s\}$ (per the dependency on `#deriv-edge-credence-dynamics` Props B.1–B.6). Within these conditions, the exact threshold and hard ceiling are algebraically exact (see `#deriv-strategic-persistence-hard-ceiling`). $\delta_{\text{strategic}}$ remains open — see Discussion §1 and `#disc-credit-assignment-boundary`."*

### 4.4 Working Notes hygiene

The "Audit 451729 (D.3) strengthen-first edit, 2026-05-12" Working Note remains valuable as breadcrumb. The "Cross-reference to NeurIPS Paper 2" note also stays (the $\mathcal A_{\text{decay}}$ class-level structural theorem in Paper 2 is the downstream sharpening, and the cross-ref earns its place). The other items are either resolved (status flip moves them out) or current open work (the credit-assignment, stochastic-treatment, and institutional-example notes).

### 4.5 Cross-references already correct

The instantiation row in `#result-sector-persistence-template`'s Table (§"Instantiations in AAT") already names `#schema-strategy-persistence` with `(T2)` "via Beta-Bernoulli edge updates (`#deriv-edge-credence-dynamics` Props B.1–B.6); constant-$\alpha$ requires experience discounting" — that row is already truth-faithful and does not need to change. The Discussion mention "*Strategic persistence (`#schema-strategy-persistence`): ... But $\alpha_\Sigma = 1/(n+1)$ is time-varying: it decays monotonically with experience. Constant-$\alpha$ — and therefore the template's trajectory guarantee — requires experience discounting as a prerequisite, not a heuristic*" likewise already reflects the post-§D.3 state.

### 4.6 What does NOT change
- The §Findings entry's prior-art `Related Work` table — Ljung 1987 (formal antecedent), Kirkpatrick et al. 2017, Gama et al. 2014, Ashby 1956 / Conant & Ashby 1970, Leonard-Barton 1992 / Levitt & March 1988 — is faithful to the strengthened form; no entries shift in relationship-label or note. The novelty-claim posture (*differentiation* on Bayesian update dynamics with experience discounting) is appropriate at conditional-tier as it was at sketch-tier; the differentiation move is the connection from textbook mechanics to a survival inequality with environment-side parameters, which the §D.3 work made *sharper*, not different in kind.
- The five verified instances (Props B.1–B.6 in §Epistemic Status) remain the schema's evidentiary base. They do not all need to be revisited at Gate 2; that is `#deriv-edge-credence-dynamics`'s own work (which is at `status: conditional, stage: draft` already).

## 5. Honest scope statement (what I did / didn't verify, and the strict-form next step)

**Verified first-hand:**

- The schema's full text (§Formal Expression, §Forgetting as Prerequisite, §Epistemic Status, §Discussion, §Findings, §Working Notes) — including the cross-reference to NeurIPS Paper 2's $\mathcal A_{\text{decay}}$ structural-class theorem.
- `#deriv-edge-credence-dynamics` Props B.1, B.2, B.3, B.4 in full algebraic detail (lines 47–278 of that segment). B.5/B.6/B.7 read by name and statement — the schema's "five verified topologies" claim is faithful to the proposition statements, and re-verifying the B.6/B.7 algebra was unnecessary for this adjudication (the schema's lift turns on B.1 + the discounted-update steady state, not on the multi-topology landings, which are independent evidentiary content).
- `#result-sector-persistence-template` full text — the template's (T1)–(T3) precondition structure is exactly what the schema's `conditional` label conditions on.
- `#result-persistence-condition` full text — for the structural-identity claim's other half (the linear $\alpha = \mathcal T$ case where the structural-persistence inequality becomes the operational tempo-vs-disturbance inequality).
- Algebraic re-derivation of $\alpha_\Sigma^{\text{ss}} = (1-\lambda)/(2-\lambda)$ (§2.2) and the hard ceiling at $\rho_\Sigma \geq R_\Sigma/2$ (§2.3) — both independent of the segment's text.
- Numerical spot-check of the overstatement quantification at $\lambda \in \{0.5, 0.9\}$ and the boundary behavior at $\rho_\Sigma/R_\Sigma \in \{0.49, 0.50, 0.51, 0.60\}$ (Python, §2.3).
- The audit-routing-instructions four-completion-state contract, the no-go protocol, the ghost-form taxonomy, and the integration-is-replacement landing discipline (read in full).
- The `conditional` / `robust-qualitative` / `proposed-schema` / `status-sketch` canonical terminology entries.

**Not verified first-hand (honest deferred-verification):**

- Independent re-verification of Props B.5–B.7 (the L0/L1 transfer, the L1' mixture refutation under unobservable common cause). These are cited by the schema; if any of them carries a flaw, the schema's "five verified instances" claim weakens. Cluster B's experience indicates this is *not* a place to relay optimism — the Model-S spike's prediction-disconfirmation came from exactly this kind of "should be standard textbook" intuition. The strict-form independent-verify next step is to run a sub-spike that re-derives B.5–B.7 from first principles, or to grandfather them in only after their parent segment `#deriv-edge-credence-dynamics` itself advances past `status: conditional` to a verified state. I read the B.5/B.6 statements and the B.7 refutation; the algebra was not re-derived.
- The connection to NeurIPS Paper 2's $\mathcal A_{\text{decay}}$ structural-class theorem (cited in Working Notes). This is downstream sharpening and was not in scope for the schema's status lift; verifying it would lift the schema *further* (the no-go would acquire class-level company), not affect the present adjudication.
- The Working Notes claim that the stochastic treatment from track-b simulations suggests $\rho_\Sigma / \sqrt{\mathcal T_\Sigma}$ rather than $\rho_\Sigma / \mathcal T_\Sigma$ for steady-state strategic mismatch. This is genuinely an open item — it is about the Model S branch of the template applied to the strategic case, which the present spike did not touch (the §D.3 work was Model D).

**Strict-form independent-verify next step:** Before any canon write of the lift in §4.1–§4.3, a fresh reviewer (per `doc/audit-routing-instructions.md` §8 "*adjudicator ≠ grad-confirmer*"): (a) re-checks §2.2 and §2.3's algebra independently; (b) reads `#deriv-edge-credence-dynamics` Props B.1 (the source the §2.2 derivation reduces to) first-hand; (c) reads `FORMAT.md`'s `status: conditional` definition first-hand and confirms the schema's load-bearing claims sit at that tier (not above, not below); (d) reviews the proposed appendix segment text once drafted, before commit. This is the wording-failure-class external eye gate that §8 makes load-bearing.

**No-go-mode check (per `doc/audit-routing-instructions.md` §4):** No (C) outcome surfaced. The hard ceiling is *itself* a no-go theorem — but it is a no-go *internal to the schema*, not a no-go *against the schema*. The schema's persistence form ($\alpha_\Sigma \gt \rho_\Sigma/R_\Sigma$) is *not* falsified by the hard ceiling — the ceiling refines the *reachable* region in $(\rho_\Sigma, R_\Sigma)$-space rather than refuting the form. This is the integration-is-replacement protocol's "no-go is present-tense canonical truth, demonstrate it in an appendix" landing (ghost-form A in §5 of the routing doc), not the §4 falsification protocol. The schema's claim is *strengthened* by the ceiling, not undermined.

**Failure-mode self-check:** I did *not* find myself reaching for a soften move. The pull I noticed and resisted was the inverse — the temptation to over-promote to `exact` (which would be the same "down-tier-because-new" failure mode in reverse: dressing a conditional result as exact because the algebra is clean). The §2.6 analysis kept the schema at its honest tier — `conditional` — and routed the bare-fact exactness of the load-bearing pieces to where they belong (their own appendix), exactly because conflating "the algebra is exact" with "the segment can be labeled `exact`" elides the local-conditions / global-dependencies distinction that the FORMAT.md tier definitions exist to track.

---

*Spike concluded. Outcome A + B candidate, awaiting Joseph adjudication. The canon writes in §4 are scoped; the spike file itself is the durable artifact and is committed before any canon-modifying work per `doc/audit-routing-instructions.md` §8 pre-spike commit hygiene.*
