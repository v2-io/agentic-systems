# Spike: The Objective Functional and the Revealed-Preference Defense — does "an agent that acts has scalarized" license a real-valued $V_{O_t}$ over all trajectories?

**Date:** 2026-05-30
**Type:** strengthen-first / overclaim-challenge
**Trigger:** A deeply-mathematical de-novo auditor (AUDIT-WORKING-526815) challenged the **revealed-preference defense** in `#form-objective-functional`. The defense argues the real-valued codomain $V_{O_t}: \text{trajectories} \to \mathbb{R}$ "follows from the comparability requirement (total ordering of alternatives)," grounded in: "an agent that acts has implicitly scalarized: choosing action $a$ over $a'$ imposes a total ordering at the moment of choice." The auditor's contention: a *local* choice relation (what the agent picks here-and-now) is not the same as a *total order over all trajectories*, and recovering a *representable real-valued functional* from choices requires named axioms (completeness / continuity / independence — vNM / Debreu). As written, the defense claims more than the choice data licenses. Raw note: `audits/AUDIT-WORKING-526815/.integrated/38-form-objective-functional.md`; routed candidate in the segment's `## Working Notes` "Follow-up items" §3.
**Disposition:** This spike does not modify canon. It works the decision-theory machinery to the end and drafts the proposed per-segment integration *inside this document* for an external-eye review pass. No `status:` change, no segment-body edits.

---

## 0. The challenge, stated precisely

The segment makes a logical implication chain in its Epistemic Status:

> "The claim that $V_{O_t}: \text{trajectories} \to \mathbb{R}$ is the right interface is grounded in: any evaluation criterion must ultimately answer 'how good is this trajectory?' with a scalar, because the agent must compare alternatives. **The real-valued codomain follows from this comparability requirement (total ordering of alternatives).**"

and the first of its three grounds:

> "**Revealed preference.** An agent that acts has implicitly scalarized: choosing action $a$ over $a'$ imposes a total ordering at the moment of choice. The scalar $V_{O_t}$ makes this implicit scalarization explicit. An agent that truly cannot compare alternatives cannot act coherently — it is stuck, not purposeful."

The auditor's objection has two logically distinct gaps in this chain, in increasing stakes:

1. **Local choice $\not\Rightarrow$ total order over all trajectories.** A single act selects one element of the *currently available action set* under the *current* model and state. It reveals at most a binary "$a$ chosen over $a'$ available now." Iterated over a lifetime it yields a *finite* set of pairwise revealed-preference facts on *realized* choice situations — not a complete relation on the (typically uncountable) space of *all trajectories*, most of which are never candidates at any decision point.

2. **Total order $\not\Rightarrow$ real-valued representation.** Even granting a complete preorder $\succsim$ on trajectories, the existence of a *function* $V_{O_t}$ with $\tau \succsim \tau' \iff V_{O_t}(\tau) \ge V_{O_t}(\tau')$ is a **representation theorem**, not a definitional given. It requires more than completeness + transitivity: the standard sufficient condition is **continuity** (Debreu), and when trajectories are *lotteries* (the segment's $V_O$ takes expectations, so they are), an expected-utility representation additionally requires **independence** (von Neumann–Morgenstern). The canonical counterexample — lexicographic preferences on $\mathbb{R}^2$ — is a complete, transitive total order with **no real-valued representation at all** (Debreu 1954). And the segment's *own* exclusion ("agents with genuinely incommensurable objectives *and* no priority structure") is precisely the lexicographic / non-continuous case — so the gap is not hypothetical, it is the segment's own stated boundary, mis-filed as already handled by the "comparability" hand-wave.

The hypothesis offered (to attack, not confirm): this lands near **(B)** — the defense is recoverable as a *scoped representation result* under explicitly-named axioms, which is a strengthening (a citable theorem replaces a hand-wave), not a softening.

---

## 1. The machinery (the actual representation theorems)

These are foundational, textbook results; per `ref/INDEX.md` convention they are cited directly with full citation rather than held as local PDFs. The exact conditions matter for an auditor at this level, so I state them precisely (each verified against the standard statements this cycle).

### 1.1 Debreu's representation theorem (ordinal, deterministic outcomes)

**Debreu (1954).** Let $\succsim$ be a binary relation on a topological space $X$ (here: the trajectory space). If $\succsim$ is

- **complete** ($\forall x,y$: $x \succsim y$ or $y \succsim x$),
- **transitive**, and
- **continuous** (for every $x$, the sets $\{y : y \succsim x\}$ and $\{y : x \succsim y\}$ are closed),

and $X$ is second-countable (or: connected and separable), then there exists a **continuous** function $u: X \to \mathbb{R}$ with $x \succsim y \iff u(x) \ge u(y)$. The representation is **ordinal** — unique up to a continuous strictly-increasing transformation.

**The bite (Debreu's own counterexample).** *Lexicographic* preferences on $X = \mathbb{R}^2$ (prefer on coordinate 1; break ties on coordinate 2) are complete and transitive but **not continuous**, and admit **no** real-valued representation — not merely no continuous one, no function at all. This is exactly the structure of "two genuinely incommensurable objectives with a strict priority but no tradeoff rate." So continuity is not a technical nicety; it is the precise dividing line between objectives the scalar interface *can* represent and the ones the segment *means to exclude*.

### 1.2 von Neumann–Morgenstern (cardinal, outcomes are lotteries)

The segment's downstream value object is $V_O(M_t,\pi;N_h) = \mathbb{E}[V_{O_t}(\tau) \mid M_t, \pi]$ — an *expectation* of $V_{O_t}$ over the trajectory distribution induced by the policy. Taking that expectation as the thing maximized is an **expected-utility** posture, which is not free.

**von Neumann–Morgenstern (1944).** Let $\succsim$ be a relation on the set of lotteries (probability distributions) over an outcome set. If $\succsim$ is **complete**, **transitive**, **continuous** (Archimedean: for $p \succ q \succ r$ there is a mixture of $p,r$ indifferent to $q$), and satisfies **independence** ($p \succsim q \iff \alpha p + (1-\alpha)s \succsim \alpha q + (1-\alpha)s$ for all $s$, $\alpha \in (0,1]$), then there is a function $u$ on outcomes with $p \succsim q$ iff the $u$-expectation under $p$ is at least the $u$-expectation under $q$, i.e. $\sum_o p(o)\,u(o) \ge \sum_o q(o)\,u(o)$, with $u$ **unique up to a positive affine transformation** (cardinal).

This is the axiom set that justifies *evaluating a policy by the expectation of a fixed scalar trajectory functional* — which is exactly what $V_O$ and $Q_O$ do. Without independence one may still have an ordinal representation of preferences over lotteries, but **not** one that takes the expected-value form the value object assumes.

### 1.3 Afriat's theorem (the finite revealed-preference fact — the auditor's gap (1), made precise)

The revealed-preference argument as the segment states it (choices reveal a scalarization) is the *Samuelson (1938) / Afriat (1967)* program. The decisive finite result:

**Afriat (1967).** A *finite* dataset of choice observations is rationalizable by a continuous, monotone, concave utility function **iff** the data satisfy GARP (the Generalized Axiom of Revealed Preference — no revealed-preference cycle contains a strict relation). Equivalently, the Afriat inequalities $U_t \le U_s + \lambda_s\, p_s\cdot(x_t - x_s)$, $\lambda_s \gt 0$, are feasible.

Two facts from Afriat are exactly the auditor's point made rigorous:

- **Existence, not uniqueness.** Passing GARP *certifies that some well-behaved utility exists* consistent with the choices; it does **not** pin down a unique utility, and a fortiori does not determine $V_{O_t}$ off the observed choice situations. So a lifetime of coherent acts *under-determines* a global trajectory functional — it constrains it on the revealed comparisons and leaves it free elsewhere.
- **Coherence is a *testable hypothesis*, not an entailment of "acting."** GARP can *fail*. An agent that acts but cycles (intransitive revealed choices) has *no* rationalizing utility. "An agent that acts has implicitly scalarized" is therefore false as an unconditional entailment: acting entails a *choice function*, and a choice function admits a scalar representation **iff** it is consistent (acyclic). The segment's own "cannot act coherently — it is stuck" is doing the work of an *assumption* (coherence/consistency), smuggled in as if it were a consequence of acting.

### 1.4 Putting the chain back together

The corrected chain is:

> acting $\Rightarrow$ a choice function on action sets $\xrightarrow{\text{(coherence: GARP / completeness+transitivity)}}$ a complete preorder $\succsim$ on the relevant alternatives $\xrightarrow{\text{(continuity; + independence over lotteries)}}$ a (continuous, expected-utility) real-valued $V_{O_t}$.

Each arrow is a named axiom, not a tautology. The segment currently writes the whole chain as a single "$\Rightarrow$ from comparability." The strengthening is to *name the arrows* — which is precisely a representation theorem.

---

## 2. Verdict

**Landing: (B) — the defense holds under explicitly-named axioms, and naming them is a strengthening.** The revealed-preference *intuition* is sound as **motivation**; the *grounding* it currently asserts ("follows from the comparability requirement") **overstates**, conflating (i) the choice-function fact that acting produces, (ii) the coherence hypothesis that turns choices into a preorder, and (iii) the representation theorem that turns a preorder into a real-valued (and, for the value object, expectation-form) functional. The repair converts an overstated entailment into a precise, citable **representation result**:

> **The real-valued codomain of $V_{O_t}$ is justified as a representation of the agent's preference relation over trajectories, under (A1) completeness, (A2) transitivity, (A3) continuity (Debreu 1954) — and, because the value object evaluates policies by $\mathbb{E}[V_{O_t}]$, (A4) independence over trajectory-lotteries (von Neumann–Morgenstern 1944). These axioms are the precise content of the framework's "coherent agency" scope assumption. They can fail; the agents on which they fail are exactly the ones the segment already excludes (lexicographic / genuinely-incommensurable-with-no-tradeoff-rate — Debreu's non-continuity counterexample; intransitive / GARP-violating — Afriat).**

This is strictly *more* than the original "We ground the scalar in comparability" aspired to: it (a) tells the reader *which* agents the interface covers and *which* it provably cannot represent, with the boundary characterized by a named counterexample; (b) connects the framework's own already-stated exclusion to the theorem that explains *why* it is the exclusion; (c) supplies the expected-utility justification the value object silently relies on. Per `CLAUDE.md` *Math-novelty recognition* and the *scope-precision-is-the-CS-norm* note: a scope condition stated under named hypotheses with an explicit no-representation boundary for the complement is a **first-class result**, not a hedge — and this is a Nash-style *application* of established machinery (the representation theorems are imported, cited, and used to ground an AAT-internal interface claim), not an invention claim, so no deflation is warranted in either direction.

### Why this is not the easy word-swap (strengthen-first honesty)

The easy soften would be: "weaken the Epistemic Status from 'follows from comparability' to 'we *assume* a scalar objective; this is a scope restriction.'" That makes the local mismatch disappear and is *false to the aspiration* — the aspiration (choices ground the scalar) is *correct under the right axioms*, and there is a real theorem to be had. The strengthen-first attempt:

- **Can "acting $\Rightarrow$ scalarized" be made true as written (unconditionally)?** No. Afriat: acting produces a choice function; a choice function has a scalar representation **iff** consistent. Intransitive agents act and have no representation. There is no tightening of "acts" that recovers "scalarized" without smuggling in consistency. The failure is *instructive* — it is exactly *why* the segment's "cannot act coherently — it is stuck" sentence is load-bearing: it is the (A1)+(A2) assumption in disguise, and it should be promoted to a *named premise*, not left as rhetorical flourish.
- **Can the claim be *replaced* by a stronger true claim?** Yes — the representation result above, which is strictly more informative and supplies the value object's missing expected-utility justification. This is the strengthening, and it is why the landing is (B), not a bare scope-narrowing.
- **Is the scalar interface itself in jeopardy?** No — and this is the key result the *prior* spike (`spikes/.integrated/spike-scalar-objective-scope.md`, 2026-04-01) already established and which is *reinforced*, not undermined, here. That spike proved the scalar codomain is genuinely load-bearing for the diagnostic system: $A_O = \sup_\pi V_O$ needs a *complete ordered field* (sup is not defined on a Pareto order), and $\delta_{\text{sat}}$ / $\delta_{\text{regret}}$ need real differences and a least-upper-bound. So softening the codomain would break the diagnostics. The right move is therefore to *ground* the codomain (this spike), not to weaken it. **The two spikes are complementary halves:** 2026-04-01 answered "*is* the scalar restriction load-bearing and what is its *dimensional* scope (scalar-vs-vector)?" — yes, and vector extension degrades the diagnostics; this one answers "*by what theorem* do choices license a real-valued representation, and where is the representability boundary?" — the vNM/Debreu axioms, with the lexicographic/GARP boundary. The 2026-04-01 spike's §4.1 already gestured at this (it cites Samuelson 1938 and "mild consistency axioms (transitivity, independence)") but stopped at the gesture; it did **not** name continuity, did not surface Debreu's non-representation counterexample, did not invoke Afriat's existence-not-uniqueness, and its recommendation to "add the revealed-preference argument" to the Epistemic Status was the *under*-precise version that produced the very overstatement the auditor caught. This spike supplies the precision that recommendation lacked.

---

## 3. Proposed per-segment integration (drafted, not applied)

### 3.1 `#form-objective-functional` — Epistemic Status (the headline fix)

The "Scope restriction: scalar comparability" block currently states the three grounds with revealed-preference as an unconditional entailment. The proposed replacement keeps all three grounds as *motivation* but re-bases the load-bearing claim on the representation theorems. Drafted Epistemic-Status replacement thrust (FORMAT-clean math; one logical line per paragraph):

> **Scope restriction: scalar comparability (a representation result).** The real-valued codomain is a genuine, load-bearing restriction: the satisfaction gap ( #def-satisfaction-gap) and control regret ( #def-control-regret) read off scalar differences and a supremum, neither of which is defined on a merely partially-ordered objective space. The codomain is justified as a *representation* of the agent's preference relation $\succsim$ over trajectories. Acting produces, at each decision point, a choice over the available alternatives; **when those choices are coherent** — (A1) complete and (A2) transitive as a preorder on trajectories — and (A3) continuous (closed upper and lower contour sets), Debreu's representation theorem (Debreu 1954) supplies a continuous $V_{O_t}: \text{trajectories} \to \mathbb{R}$ with $\tau \succsim \tau' \iff V_{O_t}(\tau) \ge V_{O_t}(\tau')$, ordinal (unique up to continuous strictly-increasing transformation). Because the value object ( #def-value-object) evaluates policies by the *expectation* $\mathbb{E}[V_{O_t}(\tau)]$, the trajectories are lotteries and the expected-value form additionally invokes (A4) independence (von Neumann–Morgenstern 1944), under which $V_{O_t}$ is cardinal (unique up to positive affine transformation).
>
> These four axioms *are* the precise content of the framework's "coherent agency" scope, and they can fail. **Acting does not by itself entail a scalar objective:** a finite history of choices is rationalizable by a (well-behaved) utility iff it is acyclic (GARP; Afriat 1967), and even then it determines $V_{O_t}$ only on the revealed comparisons — existence, not uniqueness, and not a global functional. The agents on which the axioms fail are exactly the agents this interface excludes: (3a) *non-continuous / lexicographic* preferences — genuinely incommensurable objectives with a strict priority but no tradeoff rate — which by Debreu's counterexample admit *no* real-valued representation at all; and (3b) *intransitive / cyclic* agents (committees, multi-reward systems with unresolved aggregation) which violate (A2). For (3a) with multiple must-satisfy thresholds the AND-node encoding below recovers per-terminal scalars; for genuinely unresolved Pareto structure a vector-valued extension is required, under which the *structural* results of Part II survive but the *diagnostic* results degrade to set-theoretic tests (see below).

Then the existing three numbered grounds (Revealed preference / Approximation / Timescale separation) are kept but **re-cast as motivation for the axioms, not as the entailment**:

> 1. **Revealed preference (why coherence is the natural scope, not an arbitrary one).** A purposeful agent that selects actions exhibits a choice function; the framework's target — individual agents and tightly-coordinated teams under unified command — is precisely the regime in which that choice function is coherent (acyclic), so (A1)–(A2) hold and the Afriat-rationalizability hypothesis is satisfied. The scalar $V_{O_t}$ makes the resulting ordering explicit. (An agent whose revealed choices cycle is not scalar-representable — it is incoherent in the GARP sense, not merely "stuck.")
> 2. **Approximation.** [unchanged in substance; optionally note the supporting-hyperplane fact that every Pareto-optimal policy corresponds to *some* scalarization, so the scalar form represents any single frontier point and excludes only the meta-question of weight selection — from the 2026-04-01 spike §4.2.]
> 3. **Timescale separation.** [unchanged; $V_{O_t}$ is the *current* scalarization at the $\nu_O$ timescale.]

**Lexicon / forward pointers.** Add `#def-value-object` and `#def-satisfaction-gap` as the downstream consumers that *require* the representation (they already `depend:` on this segment; no `depends:` edge change needed here). The named external sources (Debreu 1954; von Neumann–Morgenstern 1944; Afriat 1967; Samuelson 1938 for the revealed-preference lineage) should be cited inline per the *prior-art integration* discipline (adopt with original names + citation; no separate positioning appendix). None are currently in `ref/INDEX.md` — they are standard textbook results, so the `ref/INDEX.md` convention is direct citation; **add INDEX rows** for the four so future citation audits locate them (suggested canonical keys: `vonneumann-morgenstern-1944-theory-of-games`, `debreu-1954-representation`, `afriat-1967-construction-utility`, `samuelson-1938-pure-theory-consumer-behaviour`).

### 3.2 `#form-objective-functional` — the intro prose paragraph (line 16) and the §3 body paragraph

The intro paragraph repeats the entailment ("choosing one action over another imposes a total ordering at the moment of choice; an agent that truly cannot compare alternatives cannot act coherently"). Soften the *entailment* verb to a *scope* verb while keeping the vividness, and add the one-clause forward pointer to the representation framing so the prose and the Epistemic Status agree:

> **Revealed preference**: a *coherent* agent that acts exhibits a choice function whose consistency (acyclicity) is exactly what lets its choices be summarized by a scalar ordering — the explicit-representation theorem is stated in the Epistemic Status; the scalar $V_{O_t}$ is that representation, not an imposition.

This is the candidate-Brief hook already staged in the segment's incidental-gold §1 ("not an imposition on reality; it is an *extraction* of the implied reality of action" — Gemini, 829314 / vNM lineage noted at 361742, 193847) — it is *correct* once "coherent" is in front of "agent," and *false* without it. Reconcile the two: the gold hook lands cleanly **only** alongside the representation framing; flag this so the later Brief-promotion pass uses the hook with the coherence qualifier, not bare.

### 3.3 The trajectory-domain under-specification (the auditor's second, separable sub-point — §3 of the note)

The same note (526815) flags that the functional domain "trajectories" is under-specified: examples are written over terminal/time-indexed states ($s_T$, $s_t$) while the codomain claim is over "trajectories," and AAT should state whether $\tau$ is a world-state trajectory, a chronica prefix, an action–observation trajectory, or a complete-state trajectory. This is a **clarity gap, separable from the representation finding** but in the same segment, so it is drafted here for the same gate. Proposed: one sentence in the Formal Expression fixing $\tau$ as a *complete-state* trajectory (the natural reading given `depends: form-complete-agent-state`), with the example-table forms ($s_T$, $s_t$) noted as projections/marginals of $\tau$, not the domain itself. (No tier impact; a definitional sharpening.) This pairs with the representation fix because the representation axioms are *over the domain* — continuity in particular is a property of $\succsim$ on whatever topological space $\tau$ inhabits, so the domain must be pinned for (A3) to be well-posed. Worth Joseph's eye on whether to fold both into one edit or keep them as two.

### 3.4 No change needed downstream — but a coherence note for `#def-value-object` / `#def-satisfaction-gap`

`#def-value-object` already uses the expectation form $\mathbb{E}[V_{O_t}]$ and `#def-satisfaction-gap` already names "the scalarization of the objective ($V_{O_t}$)" as one of its three analyst-chosen parameters and flags "the diagnostic structure depends on $V_{O_t}$ being a *value functional* on trajectories." These are *consistent with* the representation framing and need no edit. **One optional forward-pointer**: `#def-value-object`'s expectation form is exactly where (A4) independence becomes load-bearing; a one-clause Working-Note or Epistemic-Status pointer ("the expected-value form is justified by the vNM axioms named in `#form-objective-functional`") would close the loop for a reader tracing *why* policies are scored by an expectation. Low priority; not required for the fix.

---

## 4. Confidence and escalation

- **Part (1) — local choice does not entail a global total order; "acting $\Rightarrow$ scalarized" is false as an unconditional entailment:** **high confidence.** Afriat's existence-not-uniqueness and GARP-can-fail are textbook; the segment's "cannot act coherently — it is stuck" is doing the work of the coherence assumption.
- **Part (2) — total order does not entail a real-valued representation without continuity (and independence for the expectation form); the framework's own exclusion is the lexicographic/non-continuity case:** **high confidence.** Debreu's lexicographic counterexample is the canonical fact; vNM independence is exactly the expected-utility axiom the value object relies on. The mapping of the segment's "incommensurable + no priority structure" exclusion onto Debreu non-continuity is exact, not analogical.
- **Landing (B) and the proposed re-grounding:** **high confidence on the diagnosis and on the shape of the repair (name the axioms as a representation result); medium on phrasing details** — the exact wording of the Epistemic-Status replacement, and whether the four sources warrant `ref/INDEX.md` rows or inline-only citation, are the kind of `status:`-adjacent / convention calls the brief reserves for the external-eye gate. No `status:` change is implied: the segment is `axiomatic` and stays `axiomatic` — naming the axioms a formulation rests on is *what `axiomatic` means*; the fix makes the axioms explicit and honest rather than asserting them as an entailment.

**Surprises / unresolved:**

- The segment is *already* unusually careful elsewhere (the structural-survives / diagnostic-degrades split for the vector extension is praised across audits as honest). The error is **mis-localized honesty**, the same pattern the auditor's companion causal-access spike found: the segment built a careful vector-extension caveat (the *dimensional* scope) and a careful AND-node caveat (the *constraint-satisfaction* scope), but left the *representation* step (the choices-to-functional grounding) as an unguarded entailment — one correct caveat-apparatus standing in for a second one it didn't have.
- The 2026-04-01 `spike-scalar-objective-scope.md` is **archived in `.integrated/`** but its §1.1 load-bearing analysis and §2 AND-node verdict are *not visibly reflected in the current segment body* beyond the brief Pareto/AND-node paragraph — its recommendation list (§5) appears only partially landed. Worth Joseph's eye on whether that older spike's recommendations (e.g. the "objectives jointly infeasible" disambiguation row, which *did* land in `#def-satisfaction-gap`) are otherwise discharged; this spike's fix supersedes that spike's §5 "add the revealed-preference argument" item by making it precise. Reconcile so the older spike's residual is not double-counted.
- I did **not** re-derive Debreu's or vNM's theorems; per the *math-novelty / evidence-hierarchy* discipline these are imported, cited machinery (AAT *uses* them to ground an interface, it does not claim them), so relying on their standard statements is appropriate — and I verified the statements (conditions, the lexicographic counterexample, GARP-iff-rationalizable, the uniqueness classes) against the standard formulations this cycle rather than from memory alone.

---

## Working Notes

- Sources used this cycle: the standard statements of Debreu (1954) ordinal representation (complete + transitive + continuous ⟹ continuous utility; lexicographic non-representability counterexample), von Neumann–Morgenstern (1944) expected-utility (completeness + transitivity + continuity + independence ⟹ affine-unique cardinal $u$), Afriat (1967) / GARP (finite data rationalizable by continuous-monotone-concave utility iff GARP; existence not uniqueness), Samuelson (1938) revealed preference. Verified against standard course/encyclopedia statements this cycle. The challenge as raised: `audits/AUDIT-WORKING-526815/.integrated/38-form-objective-functional.md` + the routed `## Working Notes` §3 follow-up item in `#form-objective-functional`. Complementary prior spike: `spikes/.integrated/spike-scalar-objective-scope.md` (2026-04-01) — the scalar-vs-vector / load-bearing half; this spike is the representation-theorem half.
- This spike proposes no canon edits and changes no `status:`. The drafted §3 integration is for the external-eye review gate. If it lands, the affected segment is `#form-objective-functional` (Epistemic-Status re-grounding §3.1 + intro-prose reconciliation §3.2 + trajectory-domain sharpening §3.3 + four `ref/INDEX.md` rows), with an optional non-required forward-pointer in `#def-value-object` (§3.4). No downstream tier or status transitions are implied.
- Reserved-for-Joseph / external-eye: the exact Epistemic-Status wording; whether to fold the trajectory-domain sharpening (§3.3) into the same edit or keep it separate; whether the four classical sources get `ref/INDEX.md` rows or inline-only citation. The incidental-gold "extraction not imposition" Brief hook (§3.2) should be promoted only with the "coherent agent" qualifier in front — flagged so the later Brief-promotion pass does not land it bare.
- Status of this spike: **complete; verdict (B) — scoped representation result; awaiting external-eye review of the §3 integration.**
