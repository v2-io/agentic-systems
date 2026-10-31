*Feeds **B.1** in `../INTENT.md` (top intent B: every load-bearing claim says what kind of claim it is, about which agents, and what would refute it). B.1: "Every load-bearing apparatus has a record giving register, population, an instance where it is true, an instance where it is false, a falsifier, and whether it has been instantiated … someone other than the author checks each record." Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself."*

# B.1, Part I: the persistence family's records, what they exposed, what to check

*Claude Opus 5.5, B.1 Part I record author, 2026-10-30. Branch `worktree-agent-af436745a9e9c4215`, one commit carrying the seven segments, their vsect revisions, seven ledger entries and this file. Its readers are the lead, then the independent checker of each record.*

## 1. What is done and what is not

Seven Part I segments now carry a `## Claim Record`, 32 entries in all: 24 formal, 6 descriptive, 2 normative. The seven are `#result-persistence-condition` (7 entries), `#deriv-sector-condition` (7), `#deriv-stochastic-non-exit` (3), `#result-sector-condition-stability` (3), `#result-sector-persistence-template` (4), `#result-certificate-existence` (4) and `#form-sector-condition` (4). Every entry sits between Epistemic Status and Discussion, in the `doc/sop/format.sop.md` form.

**How I chose them.** A Part I segment is load-bearing apparatus if a front surface restates it (INTRODUCTION headlines 1–3, the OUTLINE Layer 0 and captions, the README partials), or if many segments rest on it (inbound `depends:`), and it carries a claim, not only a name. The persistence family meets the first test for all three Part I headlines, and the second test strongly: `#result-persistence-condition` has 28 inbound `depends:`, `#result-sector-persistence-template` 29 and `#deriv-sector-condition` 26. It is also where four C.1 rounds changed what the claims are, so the records could be written against settled text. `#result-certificate-existence` is in because headline 3 is its claim. `#form-sector-condition` is in because every persistence record's population is "correctors meeting A2'", and that segment says which agents those are.

**Not done, at the lead's direction (no further agents this session).** The rest of Part I has no records:

- *Ch. 1, ontology and scope:* `#scope-adaptive-system` (its True-of material is already derived in `spikes/epistemic-target-ontology/17-check-8.md`), `#scope-agency`, `#post-causal-structure`, `#def-observation-function`, `#def-chronica`, `#def-action-transition`, `#def-agent-environment`.
- *Ch. 2:* `#form-agent-model`, `#form-information-bottleneck`, `#def-model-class-fitness`.
- *Ch. 3:* `#def-mismatch-signal`, `#result-mismatch-decomposition`, `#emp-update-gain`, `#def-adaptive-tempo`, `#def-causal-information-yield`, `#hyp-mismatch-dynamics`, `#form-event-driven-dynamics`, `#der-recursive-update`, `#der-action-selection`.
- *Ch. 4, the rest:* `#der-gain-sector-bridge` (the sub-scope $\alpha$ grounding; it is the next record I would write), `#result-structural-adaptation-necessity`, `#result-per-dimension-persistence`, `#der-deliberation-cost`, `#der-temporal-nesting`, `#scope-agent-identity` (typed Discussion in the OUTLINE, but 19 segments rest on it and its status is `robust-qualitative`, so I count it as apparatus; the cadence exemption predates Claim Records), `#def-mood`, `#der-mood-timescale`.
- *Appendix derivations behind Part I:* `#deriv-persistence-cost` (INTRODUCTION's "a sustained cost paid in information"), `#deriv-gain-sector`, `#deriv-recursive-update`, `#deriv-discrete-sector-condition`, `#deriv-matrix-persistence-condition`, `#deriv-adaptive-gain-dynamics`, `#deriv-tempo-additivity`, `#deriv-fisher-local-update-gain`.
- *Held by the Part II round-2 lanes, left alone:* `#def-model-sufficiency` (11 inbound `depends:`; the integrator holds it) and `#impl-persistence-and-limits` (its drains hold it).

If Part I's remaining segments are taken up by chapter, I would not try to record pure definitions with no claim (`#def-agent-environment`, `#def-action-transition`) unless a definition carries a substantive commitment, as `#form-objective-functional` did.

## 2. What the records exposed

**The population axes.** Every C.1 round on Part I found the mathematics holding and a statement claiming a wider population than its derivation covers. In this family the population has five coordinates, and the records name them field by field:

1. the disturbance model: Model D (bounded; containment, positive invariance) or Model S (additive Brownian; a killed-moment scale, a finite-horizon path bound, an expected stay; certain exit);
2. the corrector: linear (the window, the Kalman cap, equality in the exit-time bound) or a general sector corrector (bounds only);
3. the disturbance fixed, or growing with the gain ($\sigma_w^2 = \sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2$ on a noisy channel);
4. the sector condition local (on $\mathcal B_R$) or global;
5. the sector bound radially tight or not: tightness alone makes the threshold an agent-level iff and the exit-time bound an equality.

A claim that leaves a coordinate unstated is read as holding at every value, and that is where the defects below come from.

**Body defects, raised in the ledger, not fixed in this lane.** Each is cited in the record as a False of, in canon's own terms (records cite canon only, so ledger slugs stay out of the bodies):

- `item:structural-failure-remedy-over-reach` (C.1). "Structural failure requires changing the correction architecture entirely" (`#result-persistence-condition`) and "requiring a new model class" (`#result-sector-condition-stability`) are false of the segments' own Model S window. Lowering an over-tuned gain restores structural persistence, and so do better observations when the window is infeasible. In `#result-sector-condition-stability`, "the sector condition fails" when $\rho/\alpha \gt R$ is also wrong: what fails is the certificate.
- `item:capacity-limit-sentence-contradicts-linear-case` (C.1). "Any monotone correction function has a capacity limit" against the same segment's linear case, $R \to \infty$.
- `item:genuinely-stochastic-is-not-unbounded-support` (C.1). Cor A.1S.1 is selected by the support of the disturbance. The hand-off sentences in three segments say "genuinely stochastic", but a random disturbance with bounded support is Model D, and its region is invariant.
- `item:template-model-s-statement-behind-its-epistemic-status` (C.1). The template's (T3) Model S line uses the pre-round-2 noise convention. Its Model S result states convergence of the unstopped moment under a local sector condition, which its own Epistemic Status denies.
- `question:template-instantiation-rows-same-argument`. The identity-continuity row is described as a discrete reflected walk, and the strategy row has a decaying sector constant. Is "the same Lyapunov argument applies in every row" true of them? I did not read the row segments, so this is a question.
- `item:certificate-existence-local-iff-and-sense-of-certificate` (C.1). The local nonlinear extension's "iff" fails in the only-if direction ($F(e) = e + e^3$). An Epistemic Status sentence contradicts the Derivation's own counterexample. "Certificate" means $\kappa \gt 0$ in the definition and $\kappa = 0$ in the ladder. The Brief equates certificate existence with keeping up, which fails when $\kappa R \lt \rho$.
- `item:form-sector-condition-regularity-and-linear-alpha` (C.1). The rule-based scope-exit paragraph says `#deriv-sector-condition` needs $C^1$, which is false: Prop A.1S needs only measurable, locally bounded $F$. "The linear case has $\alpha = \mathcal T$" holds at the optimal gain only.

These are restatement defects, mostly in Discussion and Epistemic Status paragraphs and in one Formal Expression line (the template). None touches a derivation that a C.1 round landed. Under the launch rule they are for A.2/D.3-style work or a targeted C.1 pass, not for a new round on their own.

**What "instantiated" says.** Every formal entry says "not applicable". All six descriptive entries and both normative entries say "no". Apart from the template's comparison with the free-energy flow argument, which is a claim about two published arguments, the family's descriptive load is three claims: (i) the one inequality governs Kalman filters, development teams, organizations, immune systems and evolving organisms (headline 1); (ii) real environments sort into Model D and Model S, and in "genuinely stochastic" ones every long-lived agent loses its certificate; (iii) PID, rule-based, human and organizational correctors meet A2'. Each now has a falsifier that names a measurement, and none has been run. The Kalman filter is the one True-of with external support, and only because its hypotheses are built in. INTRODUCTION's "Part I is mathematically closed with simulation validation" is E.2's claim, and these entries are E.2's target list. The measurement every falsifier needs is an estimate of $\alpha$, $R$ and $\rho$ (or $\sigma_w$) from a real error process. `#detail-operationalization` says the innovation-based recipes do not yet estimate those quantities as defined (`item:write-innovation-based-estimators-for-detail-ope`), so that item is upstream of E.2 for Part I.

**B.3's anchors test, for this family.** The persistence threshold reads in the working thesis's terms without strain: "honest contact with a world it cannot fully see", with a price that rises with what the agent asks of it. The window adds something the thesis does not yet say: on a fixed channel, trying harder makes contact worse past the Kalman gain. The certificate-existence entry is machinery, not a thesis sentence.

## 3. Rules of the form applied

I applied the three rules of `reviews/b1-part-ii-integration-1.md` :16 uniformly:

- a theorem is formal, and its population is the hypothesis class as representations;
- a claim that a named real class meets the hypotheses is a separate descriptive entry;
- Instantiated is never filled by a theorem;
- every falsifier names the tag, section or quoted clause it refutes.

I also applied check 1 §6's coverage rule: a claim another record or a conclusion rests on gets its own entry. That rule is why the adaptive reserve, the template's instantiation claim, and the persistence/destabilization identity have entries.

The SOP does not yet state these rules. Adopting them in `doc/sop/format.sop.md` would be a small edit. I did not make it, because the SOP is shared with a running Part II round.

One choice the Part II records did not face: records cite only canon and the published world. Where a record's False-of is a neighbour that only the ledger names (hysteresis, endogenous disturbance), the record describes it in canon's terms and leaves the slug out.

Two record titles carry the body's own over-claim on purpose, so the False-of has something to refute: `#result-persistence-condition`'s capacity-limit entry and `#result-sector-condition-stability`'s third entry. When C.1 repairs the sentence, the entry changes with it.

## 4. For the checker

Bind to the branch head. Each segment was taken in with `vsect revise … --answer change=reworded`, because only a record was added and no body sentence changed. That lapsed the checks resting on the old text: 55 through `#result-persistence-condition`, 33 through `#deriv-sector-condition`, 29 through `#result-sector-condition-stability` and 3 through `#deriv-stochastic-non-exit` (overlapping sets; vsect's whole-file grain). They want a confirmer pass scoped with `--checks`, not a re-check.

What I computed myself, and what I took from the segments:

- **By hand:** the certificate counterexamples ($J = [[1,-2],[2,1]]$ and the certificate $\mathcal M = I$, $\kappa = 1$; $F = e - e^3/4$ on $\lvert e\rvert \leq 1$; $F = e + e^3$ on $\lvert e\rvert \leq 2$; the trace and determinant of $[[1,-2],[2,-1]]$); the reserve example ($\alpha = 2$, $R = \rho = 1$); the window instance's endpoints against the round-2 script's printed output.
- **Quoted from the segments or the lane scripts' printed outputs, not re-run by me:** $\alpha\Phi(0)$ at threshold, the three-term expansion, the gain-maximizer table, the non-exit table, the Monte Carlo of the killed and stopped moments. Re-running `part-i-round-2.md` §§1, 4, 5, 6 and `c1-lanes/part-i-check-4.md`'s script reproduces them.
- **Not read at the primary by me:** Khasminskii 2012, Khalil 2002, Nesterov 2004, Aguilera et al. 2022 (`item:aguilera-fep-narrow-validity-citation-unchecked` stands), Conley 1978.

Suggested criteria, one per record, for you to put in your own words:

1. **`#result-persistence-condition`.** Does each population name its disturbance model, corrector class and the total-disturbance reading? Is the window True-of right ($R^2 = 1$, $K = 2$: $(0.536, 7.464)$)? Does the normative entry's False-of follow from the window paragraph? Is the descriptive "governs" entry's falsifier something a measurement could produce?
2. **`#deriv-sector-condition`.** Does each formal entry's population match its proposition's hypotheses, including (S), isotropy, and the fixed-$R$ requirement for the reserve? Is the descriptive entry's False-of (bounded-support random disturbance is Model D) right against Cor A.1S.1's "support structure"?
3. **`#deriv-stochastic-non-exit`.** Is the False-of (state-dependent noise vanishing at the boundary) a genuine exit from the population, and is the descriptive entry's population fair to the body?
4. **`#result-sector-condition-stability`.** Is the third entry's False-of (retuning and information restore structural persistence) right, and is its register normative?
5. **`#result-sector-persistence-template`.** Is the first entry's population right about local versus global (T2)? For the second entry, read `#der-identity-continuity-threshold`: is its argument the template's?
6. **`#result-certificate-existence`.** Re-derive the three counterexamples. Is "certificate" used in two senses?
7. **`#form-sector-condition`.** Is the sub-scope $\alpha$ population the body's list, with the PD question left open? Is the fourth entry's False-of right: does Prop A.1S-τ apply to the discontinuous counterexample?

Also check the seven ledger entries above against the sentences they quote, and confirm that no record cites the ledger.

## 5. Beyond the item

- **A sweep the records make cheap.** The five population coordinates in §2 are a checklist for any sentence restating a persistence result. A shape sweep over the front surfaces would flag every restatement that names none of them, the same method round 5 used for "only escape". This fits A.2 and D.3.
- **vsect grain.** Adding a record lapsed 120-odd checks that read the unchanged body. Claim-level anchors (the `###` headings are stable) would keep checks on the body bound while the record changes. The Part II author and its checker said the same.
- **On the brief.** It was right for this job. It named the KR, said what had happened today and why population is where the defects live, and pointed at the lane accounts and the ledger. The lane accounts were what made the records writable: without them I would have recorded claims that rounds 2–5 had already narrowed.

I am on the line.
