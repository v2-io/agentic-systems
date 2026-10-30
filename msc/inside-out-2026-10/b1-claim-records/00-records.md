*Feeds **B.1** in `../INTENT.md`: every load-bearing apparatus has a record giving register, population, an instance where it is true, an instance where it is false, a falsifier, and whether it has been instantiated; Part II first; a mind other than the author checks each record.*

# B.1, Part II: what the records are, what they exposed, what to check

*Claude Fable 5.1, B.1 record author, 2026-10-30. Branch `worktree-agent-af4d58fdb02765d54`, commits `b7cbcb38` and `bc80f80d` (canon and FORMAT) and the one that carries this file. Everything below is checkable at those commits; nothing here is finished-work narration, the commit bodies carry that.*

## 1. What the records are and where they live

A record is a `## Claim Record` section inside the segment, between Epistemic Status and Discussion, with one entry per distinct claim and six fixed fields: Register (formal / descriptive / normative), Population, True of, False of, Falsifier, Instantiated. The form is defined once in `doc/sop/format.sop.md` ("Claim Record"), modelled on the Findings schema so a tool can collect it the way `bin/extract-findings` collects Findings.

Why in the segment and not in a records directory: the record is theory content (what the theory claims and of whom), and canon cites only canon, so an external file would be an internal artifact the body points at; the reader meets the register where the claim is; and the body's own sentences are what the checker confirms the fields against. The fields are anchored to equation tags and section names, not line numbers. Checks go to `reviews/` as vsect review records bound to the segment version the checker read (whole-file grain; the sixteen segments were taken in with `vsect revise`, so the versions minted today are the ones to bind to).

`form-objective-functional` is the template in the sense the owner review meant: class named by representation axioms, excluded agents named by counterexample. Its record restates its Epistemic Status in the section's form so the form has one instance a reader can compare with free prose.

Sixteen segments carry records: `form-objective-functional`, `form-complete-agent-state`, `def-strategy-dimension`, `def-agent-spectrum`, `der-directed-separation`, `def-value-object`, `der-causal-hierarchy-requirement`, `der-loop-interventional-access`, `norm-explicit-strategy-condition`, `def-strategy-dag`, `def-satisfaction-gap`, `def-control-regret`, `der-causal-insufficiency-detection`, `der-observability-dominance`, `schema-strategy-persistence`, `der-orient-cascade`. Thirty-five claim entries in all: about seventeen formal, eleven descriptive, seven normative.

## 2. What the records exposed

**The shape of Part II once each apparatus names the agents it is false of.** The strong tier labels sit on the formal claims, as the owner review said. What the records make countable is the rest: about eleven descriptive claims about real agents and seven normative ones, and *none of the eighteen has been tested*. "Instantiated" says no, or not applicable, in every record except three, and those three are imports: Richens et al.'s theorem (`def-agent-spectrum`), the Hafez IDT study on simulated agents (`der-causal-hierarchy-requirement`), and revealed-preference tests in economics (`form-objective-functional`, which the body cites as lineage, not as a test of its target class). The one empirical comparison in Part II (`disc-exploit-explore-deliberate`) tests three-way allocation and went against the deliberation axis; the apparatus the Part is organized around, the 2×2, has no comparison at all. The falsifiers are now written down in the body, so E has its targets.

**Claims the bodies carried without stating.**

- `def-control-regret`: the 2×2 cell map's value rests on a normative claim the body never states: routing by the two gaps does better than routing by total shortfall. Recorded as a hypothesis with its comparison named; the identity $\delta_{\text{sat}} + \delta_{\text{regret}} = V_{O_t}^{\min} - V_O(\pi_{\text{current}})$ is recorded beside it.
- `der-directed-separation`: the degradation norm ("less coupling tracks reality strictly better") is established for coupling that changes how an agent *updates* on encoded evidence (optimality of the conditional under proper scoring rules) and not established for coupling that changes *what it encodes* under a capacity limit, which $\kappa_{\text{processing}}$ also counts. The body draws the encoding/processing boundary in two places (scope-condition clause 2; the paragraph after) without locating it. Recorded as not established, not landed either way; C.2's C3 holds the attempt. vsect question `degradation-norm-encoding-vs-updating`, awaiting C.2.
- `der-orient-cascade`: "the ordering is exact" covered a dependency (steps 1–3; 4c after 4a's convergence) and a norm (objective last; 4a before 4b). The second is not a dependency: $\delta_{\text{sat}}$ is in hand at step 2, and $\delta_{\text{strategic}}$ is computable without $\delta_s$. The body now says which is which (B.2's cascade item fell out here and was done; see §3). The norm has no stopping rule and the body's own aspiration hypothesis is the case where it is wrong. vsect question `cascade-objective-last-stopping-rule`.

**Populations the bodies name by example.** Humans are placed in two cells of the directed-separation table (cortex Class 2; motivated reasoning Class 3), so their classification is a conjecture. The sign rule is true of fault-tree arithmetic and open for humans, whose compound-event judgments depart from the product rule. The timescale ordering in `def-strategy-dimension` names its population as "many agent populations", which is not a boundary. `norm-explicit-strategy-condition`'s population is agents for whom the two approaches give equivalent outcomes, which the body says is rare.

**Letters that collide.** The records for `def-value-object` and `der-loop-interventional-access` say which (C1)–(C3) triple they mean, because `scope-edge-update-causal-validity` uses the same letters for a different triple (integrator item A5; the rename is not done).

**The one Part II prediction that reads as a prediction** is in `impl-orient-cascade` (LLMs do best on low-$\mathcal A$ tasks), outside the segments recorded here; it is still untested in the framework's terms.

## 3. What changed in canon beyond the records

- `der-orient-cascade`: summary paragraph, Derivation list (split into forced / recommended), first sentence of Epistemic Status. `impl-orient-cascade` §"forced by information dependency": the dependency excludes stale-model orderings, not joint resolution, and does not by itself put objective revision last. This is the owner review's A8 and B.2's cascade item.
- `der-causal-hierarchy-requirement`, Discussion: the RL sentence was false for a fully observed MDP (A11). Scoped to partial observability or an unobserved common cause.
- `der-loop-interventional-access`, Formal Expression: "(C2) fails — generic for any agent whose action depends on internal state…" overstated. An agent whose decision state is a function of its recorded history satisfies (C2) given that history by construction; (C2) fails when a cause of the action is outside the conditioning set, and a deterministic policy then fails (C1) for untaken actions. This is the standard half of C.2's C2; the `def-model-sufficiency` mapping and the gate rewrite are left to C.2.
- `doc/sop/format.sop.md`: cadence entry and the "Claim Record" schema.

Not done, named: retyping the strategy DAG to a formulation (B.2) is a `type:`, slug and ~50-cross-reference change; the record sorts its registers so the retype is mechanical when taken up. The Related Work rows at `der-directed-separation` (A4, dual effect) were left for C.1; the record states the Class 1 anchor as "every exact Bayes filter is goal-blind" without touching the rows, so the segment now says both until A4 lands. `CURRENT-VOL1` was not rebuilt.

## 4. For the checker

A review record at `reviews/b1-part-ii-check-<n>.md`, `vsect take`-able, with one `## Cn (check)` per record or per field, target `segment:<slug>`, act `read-check` (or `rederive` where a field carries a derivation), committed `after`. Suggested criteria, one per record, in the checker's own words rather than these:

- Does each **Population** name a class by a defining property the body actually states, and does the tag or section cited scope it?
- Is each **True of** an instance the mapping of which the checker can confirm, and is an internal `example-*` labelled as consistency rather than instantiation?
- Is each **False of** outside the stated population, or a case inside it where the body itself admits failure?
- Does each **Falsifier** name an observation or construction whose outcome would refute a specific sentence of the body?
- Is every **Instantiated: no** true? (Search for any run, in `empirica/` or cited, on an agent the theory did not construct.)
- The two derivations carried inside records: the Bayes-filter computation in `der-directed-separation`'s first record, and the proper-scoring-rule argument in its fourth.
- The three body corrections in §3, each against the sentence it replaced (the diffs are in `bc80f80d` and `b7cbcb38`).

Citations introduced from recall, marked "cited from recall, primary not read in this project" in the bodies, none in relata: Gneiting & Raftery 2007; Grimm, Barreto, Singh & Silver 2020; Sims 2003; Bar-Hillel 1973; Kinny & Georgeff 1991; Cohen & Levesque 1990; Behrens, Woolrich, Walton & Rushworth 2007; Daw, Niv & Dayan 2005. `der-loop-interventional-access` refers to Q-learning convergence as "the standard result" without naming Watkins & Dayan 1992. A checker who reads any of these at the primary should say so in the review so the mark can come off.

## 5. Beyond the item

**B.3's anchors test, a first pass.** Stated in the working thesis's terms, the dynamics claims fit without strain: directed separation *is* honest contact (goal-blind belief update); the insufficiency no-go, observability dominance and loop identification are limits of what an agent can know from inside, with exploration, self-access and another observer as the ways out; the forgetting prerequisite is the price of contact rising with success, almost verbatim. Three strain. The strategy DAG as a *representation* and the objective functional are machinery, not thesis sentences, which is as it should be. The objective-last rule and the explicit-strategy condition read as design engineering; the thesis does not generate them. If B.3 adopts the thesis, those two are the places to say "and here is the engineering the thesis does not dictate."

**G.0, a criterion that fell out.** Every normative claim in Part II has a comparison that would test it; none is argued from premises a falsifier cannot reach. That suggests the line between ASF and logos: a claim with a falsifier belongs in ASF at honest tier (normative-typed, comparison named); a claim whose warrant is argument with no observation that could refute it belongs in logos. The ACA and identity material G.0 is about is of the second kind. Offered, not decided.

**B.2 and the type system.** The records show `type:` and register are different axes: `def-strategy-dag` is a definition carrying two descriptive and one normative claim; `der-orient-cascade` is "derived" and half of it is a norm. Retyping segments (B.2) fixes the headline type; the record is what keeps the other claims from inheriting it. Both are needed.

**Tooling.** (i) A `bin/extract-claims` that walks the OUTLINEs and emits the records would give A.2 and D.3 their source: a front-door sentence either traces to a record entry or it does not. Cheap; I did not build it because a generated root file is another surface and the records should be checked first. (ii) vsect's whole-file grain means every record edit lapses every check on the segment; claim-level anchors (the `### {claim}` headings are stable ids) are the natural carve, as the vsect builder predicted. (iii) md-press reads a run of `**Field:**` lines as one paragraph and proposes marking each break; blank lines between fields avoid that, and the FORMAT schema shows them that way.

**On the brief.** It was right to leave where records live open and to name `form-objective-functional` as a quality rather than a format; the advisor's one addition that mattered was that every field must be confirmable against a named text location, which is what made the form settle. The explorer's §3 was treated as a hypothesis list and each field re-derived from the body; where I disagreed with it (4a-before-4b is not a dependency; "generic" failure of (C2) is too strong but the fix is smaller than its §7.1), the record says what the body supports.

I am on the line.
