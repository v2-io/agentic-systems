*Feeds **C.2** (C2, C3), **B.1** (Part II records) and **C.1** (the defects these commits replaced) in `INTENT.md`. Top intent (Joseph, 2026-10-30): "Complete 'in-place' refactor of ASF — meta, all artifacts, and theory itself." Typed checks: `reviews/part-ii-check-1.md` and its three companions.*

# Part II integration, independent check 1

*Claude Opus 5.5, independent checker of `253d2bca`..`279b2699`, read at `6511154d`. Written for the next integrator, who has not read the four review records. Each item below names the record that carries its derivation, instance and repair text; the records are the evidence, this is the map.*

## How the check was done

I split the landing three ways and asked three peers (Opus 5.5) to check one part each, cold first, without reading the integrator's account until they had their own read. The identification side (C2) is in `reviews/part-ii-check-1-identification.md`. Allocation versus distortion (C3) is in `reviews/part-ii-check-1-distortion.md`. The B.1 record corrections of `8f7dd870` are in `reviews/part-ii-check-1-b1-records.md`. I kept the cross-cutting work for myself: drains across the repository, the A5 relettering, the Hafez figures at the primary, generated outputs, the ledger, and the places where the three clusters' findings meet (`reviews/part-ii-check-1.md`).

I read each peer's record whole. Before relying on their headline instances, I re-ran or re-derived them: the four scripts that carry the no-go-scope, $\kappa$-zero-collider and right-rung findings; both of the B.1 checker's right-rung instances, by hand; and the distortion checker's three "wants a second mind" results, by hand.

Every check binds to the text at `6511154d` or earlier, and none of the checked segments changed after `279b2699`. The new check scripts sit beside the spikes' own scripts, named `check-part-ii-check-1-*`.

Mechanical state: `bin/refresh-all --check` is current, `bin/lint-outline` is clean, and `md-press` would change nothing in any file the five commits touched.

## The verdict, in one paragraph

The integration's frame holds, and all four of us would keep it as the spine. Its three separations survived every probe at the level of the frame:

- identification of action effects;
- goal-dependence of a belief, bounded in transferred goal information;
- distortion of a belief, a reliability loss.

So did most of what landed in their name: ignorability free at the policy's own inputs, the coin-retention clause, the g-formula average, the intention-to-treat reading, the V7 collider, the log-ratio range bound, Otto–Villani with the right reference measure, the retirement of $\mathcal A$, the 5a value-of-information zero, and the right-rung counterexample.

What did not hold is mostly about the *scope of an exact sentence*. In about a dozen places the body says "exact", "iff", "exactly when" or "for free" past what is proved, and in each a constructed instance a dozen lines long settles it. Most of the repairs strengthen rather than soften. Separately, the drains of retired statements are incomplete at more than twenty sites inside and outside `src/`. And the ledger is missing the reviser's classification for fourteen edited segments.

C2 and C3 should not be marked landed-and-verified under C.2 yet. They are landed, and checked, with the defects below open.

## What a next integrator would do first

These are ranked by how much rests on them. Within each, the cited record holds the instance and the replacement text.

**1. Fix the event, $\kappa$ and causal discipline as one move.** (Distortion F1, F3; identification F3; cross-cutting F11.)

The landing pinned $e_\tau$ to include the realized action, which is right for the V7 collider. In the same landing it declined the C3 spike's L0 *because* adding the action to the conditioning set makes the independence vacuous under injective policies. With the action in $e_\tau$, the independence as written *is* that vacuous version, and the regression guard at `#der-directed-separation` `:269` now contradicts the Scope Condition at `:53`.

The consequences:
- Under the operating law, $\kappa_{\text{processing}}$'s numerator and denominator are both identically zero for every update when the policy is injective in the goal. Causal discipline is then undefined, or satisfied by Class 3 agents, and the appendix's bound reads $0 \leq 0$ (distortion C6, F3).
- If the update drops the action instead, the collider at $M_t$ reopens at $\kappa = 0$ exactly: $0.82$ on-policy against $0.50$ interventional, with an exogenous goal and bounded signaling (identification C4, F3). That refutes `#def-value-object`'s "the claim rides only on the zero" and the only stated instance of `#der-directed-separation`'s scoping-rule record.

The coherent repair has three parts that belong in one landing:
- (a) Define $\kappa$, causal discipline and the appendix's laws under the *probe law*: the goal varied at fixed inputs. This is what $\hat\kappa$ and Paper 3's estimator already measure (distortion F3).
- (b) Make the event clause part of premise 1 of `#def-value-object` (identification F3).
- (c) Type interior and processing actions as processing for the separation test.

Part (c) is the influx's open "interior-action loophole" (`influx-scout/MAP.md` §3, verify item 5; source `influx-scout/rewrites.md` row 8 and `:150`, from the aat-refactored rewrite). The pin generalized that loophole from interior actions to every goal-encoding action. The probe law alone does not close it. The calibration criterion does (cross-cutting F11, my reasoning, not run).

**2. Land the missing premise and the right definition of the defect.** (Distortion F1, F2.)

The spike's (NWI) premise did not land: the goal carries no world information beyond the prior state and the action. Without it, per-goal calibration marks the Class 1 Bayes filter as miscalibrated whenever the goal is evidence, by $0.19$ nats per goal. The certificate's "action only through the likelihood" also excludes the goal-blind update that would be calibrated.

And clause 3 and Record 4 call any *departure* from the conditional law the defect. An encode-then-ignore report departs with reliability exactly $0$, so Record 4's own falsifier fires. The defect is *miscalibration*. The fact that holds is stronger: recalibrating a report recovers exactly its reliability term at no cost in resolution. I re-derived it, and it is the tower property. The retired $\mathcal A$'s numerator turns out to measure exactly the (NWI) violation (distortion F6; I re-derived the identity). That gives the retirement a demonstrated *why* rather than a narrated one.

**3. Name the third hypothesis of the right rung.** (B.1 C1, C2; identification C7, F5. Found independently by two checkers.)

Both (PC) and (SO) silently assume the receding-horizon policy lies in $\Pi$. C2's construction stitches state-wise optima and does not deliver that for a restricted class. Two different instances (B.1: $51 \gt 10$; identification: $15 \gt 6$) satisfy (PC) and (SO) and break the rung, firing `#def-value-object`'s own record falsifier.

Separately, (SO) does not make the two readings of $A_O^{\text{B}}$ coincide ($51$ against $12$). Taking the first-action reading as canonical makes C3's "infeasible" verdict sound for *every* $\Pi$, which is a strengthening (B.1 C1).

The B.1 checker offers *rectangularity* (state-wise admissible action sets) as one headline condition implying all four. That argument is its own and has been tested only against non-rectangular instances. The carriers are listed in B.1 F1.

**4. Rescope the deterministic no-go, and turn "passes for free" around.** (Identification F1, F2.)

Canon keeps an agent's randomness in $M_t$, so a randomizing agent is deterministic in $X_t$. As written, the no-go then denies it identifies anything off-policy, which is false: all 16 one-step environments are distinguished. The boundary is determinism *in what the environment can know*. For the coin route the restriction is a property of the agent's own construction, not an assumption about the environment. The integrator's script is valid only on a two-step reading, which its docstring does not make explicit.

"A deterministic policy passes the on-policy sufficiency test for free" is false in canon's own witness: inside one $M_t$-stratum outcomes range from $0.19$ to $0.81$. The true statement is one-sided and stronger. The agent can *refute* premise 3 from its own data, but cannot confirm it. Three segments carry the false form, which entered at the C2 verifier and was carried by every later hand.

**5. The smaller derivation items, all with repair text in their records.**
- Bennett's lemma makes the tilt's sharpness dependence exact, where the body calls the leading-order $\lambda \cdot \mathrm{sd}$ exact. It also shows that at high gain "pinned" has to mean zero residual mass, not small (distortion F4).
- $d_{FR}$ is defined as half of what its constant assumes, and a global constant $2$ follows without (H4) (distortion F5).
- Clause 2's converse is stated unconditionally (distortion F7).
- 5a's always-paid-cost sentence needs the abandon sentence's qualifier (distortion F8).
- The $M_t$-form's three premises are one sufficient condition with three routes to failure, and "exactly when" repeats a refuted iff (identification F4).
- The echo example needs its second bit (identification F6).
- The aspiration hypothesis's population lies inside its own False-of (B.1 C5).
- `#form-objective-functional` equates incompleteness with the (E1) lexicographic boundary, and still offers lexicographic ordering as a scalarization (B.1 C10).
- Narrower record points: B.1 C6, C8, C11, C14; identification F7.

**6. The two quantities named $\Delta M_{\text{bias}}$.** (Cross-cutting F2.)

The appendix defines it as goal-conditional against goal-marginal post-update laws, and says not to read it as bias against the goal-blind update. `#result-section-ii-survival` `:114` defines it as coupled minus goal-blind, and then bounds that with the appendix's bound. Four downstream sites compare coupled diagnostics with "clean (goal-blind)" ones through it. Coupled-minus-goal-blind is a third quantity, neither distortion nor goal-dependence. The survival result and the coupled diagnostic framework need the quantity their argument uses, and one symbol.

**7. Drains.** (Cross-cutting F1, F3–F7, F9, F10.)

The retired product law is still stated in body text:
- in full, with the "prompt engineering as $\mathcal A$-reduction" lever, at `#impl-common-roots` `:27`. This is despite `279b2699`'s "last carrier", and it contradicts `:25`.
- at `#disc-adversarial-coupling-pressure` `:22`, which contradicts `:103` of the same segment.
- in the `#disc-anti-collapse` `:36` label.
- in two Working Notes.
- in `doc/vivarium.md`, `TODO.md` and its ledger item, and four OUTLINE sites.

The "ordering is forced" sentence the B.1 checker's C16 named is still at `#der-orient-cascade` `:91`. It is also in `#impl-orient-cascade` `:77`, the terminology entry that generates LEXICON, and a figure-source comment.

A5 did not reach `#impl-causal-access`, which still says "(C1) positivity / (C2) sequential ignorability / (C3) known action-mechanism" in its body, against its own regression guard. Five more (C1)–(C3) families are undeclared in `NOTATION.md`, which says every family is declared there.

Two Hafez sites still say "89% perturbation detection" or "detection accuracy". I fetched the abstract, and the corrected sites match it exactly, including the 4.4× latency figure.

Two bodies narrate their own history: `#deriv-observation-ambiguity-bias-bound` `:130` ("A previous version of this derivation …") and `#scope-observation-ambiguity-modulation` `:66`. Integration-is-replacement puts that in the history layers.

## The influx items this check bears on

The lead asked that a check say which prior outside critique it judged answered, so the influx drain can mark it. All references are to `msc/inside-out-2026-10/influx-scout/MAP.md`.

- **§2 (C2) row and §3 D1** (behavioral-floor audits, `papers-may.md` A1; aat-refactored de novo reviewer, `rewrites.md` §2.5): *answered*. Canon's "(C2) fails generically" is gone. Ignorability holds at the policy's inputs, and what fails is positivity, which is the aat-refactored reading. The identification checker confirmed it (C1) and refined the positivity boundary (F1). behavioral-floor's (C2★) is held as a transfer condition in a Working Note.
- **§2 $\kappa$ row and §3 D11** (two definitions, two scalings; `neurips.md` §2.D, `papers-may.md` A4): *partly answered*. The linear-versus-square-root scaling is resolved in the two rewritten segments, but the linear form survives at three sites (cross-cutting F1). Paper 3's $I(G;\Omega)$-normalized definition is correctly not adopted. The check found a *new* defect in the $H$-normalized definition: it degenerates under the event pin (item 1 above).
- **§3 D10** (local $\sqrt 2$ versus global $2$; `neurips.md` §2.D, Paper 03 App D): *not answered by the integration, now independently derived*. The appendix still declines Paper 3's global constant as "unread". The distortion checker derived $\mathbb E\, d_{FR} \leq 2\sqrt I$ without (H4), and I re-derived it. That is a derivation of the $2\sqrt I$ form outside the NeurIPS chain, by two of us. The tighter $2\arccos(e^{-I/2})$ form and the saturation no-go remain verified only by that chain. This was a rediscovery of an influx item, and the drain can count it as a verification of D10's main part.
- **§3 D12** (canon bodies citing unpublished NeurIPS papers): *made slightly worse*. The appendix gained two body citations of Paper 3 (cross-cutting F8(c)).
- **§3 "Verify before landing" item 5** (the interior-action loophole; `rewrites.md` row 8, `:150`): *answered for the norm, open for $\kappa$*, and generalized by the pin (item 1 above; cross-cutting F11).
- **§3 D2** (the "iff" in `#deriv-causal-ib-lmi`): outside this landing. Still present at `:59`.

## What I recorded and changed in this cycle

- Took the four review records into `vsect`. The broken and narrowed checks open findings beside the typed ones, so expect some duplicates in `vsect open`.
- Annotated `review:part-ii-integration-1#C8`, which cites a worktree hash.
- Corrected the four worktree hashes in `CHANGELOG.md`, `spikes/INDEX.md` and both spike READMEs: `af518dd5` → `253d2bca`, `afc1840b` → `8f7dd870`, `6d4dec34` → `1dec6130`, `d981c5bb` → `18f1bb4e`. These were verified by patch-id or by a content-identical diff modulo rebase context.
- Answered the NOTATION question about the ambiguity factor, which is moot now that the factor is retired.
- Ran `vsect confirm --judgment for-checks` on fifteen version pairs whose revisers include this integration (the Part II integrator or the B.1 second mind): `def-model-sufficiency` cb015617, `def-satisfaction-gap` 65d41833 and 094c4169, `def-value-object` 7e879b9c, 983eff0f and c5883ca8, `der-directed-separation` 0d9c4785 and d7c6d09f, `form-information-bottleneck` 11e85702, `form-objective-functional` ffca37cd and dc06340d, `hyp-edge-update-via-gain` f994de59, `result-coupled-diagnostic-framework` 34713242, `result-section-ii-survival` 5f2e1a5f, and `scope-observation-ambiguity-modulation` 73a53b9f. Before each, I read the diff and the full criterion of every check the pair re-binds. Those checks are almost all Volume 4, TST and Part I checks downstream through `depends:`, plus the integrator's own C1–C8 on `983eff0f` and `d7c6d09f`; none of their criteria uses what the edit changed. The judgment is that the edit does not bear on those criteria. It says nothing about whether the re-bound checks were right, and the broken checks above sit beside them on the same versions. I left four kinds of pair unconfirmed: the `def-control-regret` pairs, whose re-bind set includes the B.1 checker's check on that segment's own text; the two pairs with no revise event (`def-satisfaction-gap` b25e6d1d, `form-objective-functional` ee71e369), since that classification is the reviser's (F12); the pairs revised only by other lanes; and every `reworded` pair outside these.
- Did not classify the fourteen unclassified edits (cross-cutting F12). That is the reviser's claim to make.
- Edited no canon.

## What was not checked

- None of the cited literature was opened by any of us, except the arXiv abstract and the Richens et al. PDF (B.1 C11).
- The horizon-$N_h$ g-formula.
- The open question on whether `#def-model-sufficiency`'s formula should hold the actions exogenous.
- The Related Work tables and A4's dual-effect rows. The distortion checker excluded them and I did not reach them.
- Paper 3's proofs.
- The B.1 checker's rectangularity argument beyond two instances.
- The mixture-LSI question on (H2) (distortion F5(d)).

Each record lists its own exclusions.

## For the system (I.4)

Two observations about the process, not the theory.

First, two of the four peer-checked failures sat exactly where every earlier hand agreed: "passes for free", and the right rung's hidden membership. They came into the record as a verifier's generalization of a two-point case, and each later hand re-derived *from the written text* rather than from an instance. The distortion checker found its blind spot in the opposite place, in what fell *between* hands: a premise stated once at the top of the spike, and a verifier aside headed "a strengthening the spike did not make". Both kinds were caught by constructing a small instance against the exact sentence. That might be worth making a standing step for any sentence labelled exact.

Second, the account's §4 grep checks would have caught the A5 and product-law residues, if run repository-wide rather than over `src/`. That is the same lesson the follow-up commit records, one layer further out.
