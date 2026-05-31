# Spike: Causal Access — Forkability, the $do$-Operator, and the Sandbox Ceiling

**Date:** 2026-05-30
**Type:** strengthen-first / grounding-challenge
**Trigger:** A deeply-mathematical de-novo auditor (AUDIT-WORKING-526815) raised a structural objection to two load-bearing moves in Part II's Causal Access chapter: (1) the singular-trajectory $\to$ Pearl-$do$ grounding in `#der-loop-interventional-access`, and (2) the forkability $\to$ Level-1 step in `#disc-sandbox-evaluation-ceiling` / `#impl-causal-access`. The challenge is also recorded in those segments' Working-Notes "off-ramp" notes and routed here.
**Disposition:** This spike does not modify canon. It draws the math as far as it goes and drafts the proposed per-segment integration *inside this document* for an external-eye review pass. No `status:` changes, no segment-body edits.

---

## 0. The challenge, stated precisely

The auditor's contention has three parts, in descending stakes:

1. **Forkability is not what makes data Level-1.** Repeatable / forkable / resettable experiments (RCTs, A/B tests, laboratory replicates) are the *canonical source* of Level-2 (interventional) data for the system being experimented on. So the sandbox-ceiling claim "sandbox is forkable, therefore its data is Pearl Level-1" misclassifies the data. The genuine ceiling on using sandbox evidence for deployment claims is **transportability / external validity** (the sandbox SCM may differ from the deployment SCM, in Bareinboim–Pearl's sense), *not* a Pearl-level demotion.

2. **Non-forkability is not a prerequisite for the $do$-operator.** `#der-loop-interventional-access` and `#impl-causal-access` ground the interventional character of loop data in the singular-trajectory scope (`#scope-agent-identity`): "Pearl's $do$-operator presumes a definite causal system acted upon; AAT inherits this presumption via the singular-trajectory scope," and "strip the trajectory commitment and the loop's interventional content collapses." The auditor: Pearl interventions are defined over causal models / populations / repeatable experimental units; singularity is needed for AAT's *identity* claims, not for the *semantics* of intervention.

3. **A chapter-wide do-vs-conditioning caution.** An action chosen by a policy is not automatically $do(a)$; it is $do(a)$ only when the policy is unconfounded with the outcome mechanism. The loop produces *action-generated* data; *identified* $P(o \mid do(a))$ further requires positivity / sequential ignorability / known-mechanism — conditions the segment currently exiles to Working Notes and a NeurIPS cross-reference while keeping `status: exact`.

The hypothesis offered (to attack, not confirm): this lands near **(B)** — a scope-*sharpening* (transportability) rather than a Pearl-level *demotion*.

---

## 1. The machinery, read from the primary sources

I read the actual definitions rather than relying on the recapitulation. Sources, both local in `ref/`:

- **CHT paper:** Bareinboim, Correa, Ibeling & Icard 2022, *On Pearl's Hierarchy and the Foundations of Causal Inference* (`ref/bareinboim-2022-pearl-hierarchy.pdf`; = TR R-60). Defs 4–10, Theorem 1.
- **Transportability paper:** Bareinboim & Pearl 2014, *Transportability from Multiple Environments with Limited Experiments* (`ref/r443.pdf`; = TR R-443). Defs 1–2 (selection diagrams, $mz$-transportability), Thm 1, Figs 1–2.

### 1.1 What the $do$-operator actually is (CHT Defs 4–5)

An intervention $do(\mathbf{x})$ replaces the natural mechanism $f_X$ in the SCM $\mathcal M = \langle \mathbf{U}, \mathbf{V}, \mathcal F, P(\mathbf{U}) \rangle$ with the constant $\mathbf{x}$, producing the submodel $\mathcal M_\mathbf{x}$ with mechanisms $\mathcal F_\mathbf{x} = \{ f_i : V_i \notin \mathbf{X} \} \cup \{ \mathbf{X} \leftarrow \mathbf{x} \}$. The Layer-2 valuation (Def 5) is

$$P^{\mathcal M}(\mathbf{y}_\mathbf{x}) = \sum_{\{ \mathbf{u} \,\mid\, \mathbf{Y}_\mathbf{x}(\mathbf{u}) = \mathbf{y} \}} P(\mathbf{u}).$$

Two facts are decisive here, both read off the definition:

- **The interventional distribution is defined over the exogenous/unit distribution $P(\mathbf{U})$** — i.e., over a *population* of units $\mathbf{u}$, not over a single committed history. The semantics of $do$ is population-level by construction.
- **What distinguishes $\mathcal L_2$ from $\mathcal L_1$ is which model the data is sampled from:** the *mutilated* submodel $\mathcal M_\mathbf{x}$ (where $f_X$ was overridden) gives interventional data; the *natural* model $\mathcal M^\ast$ (where $f_X$ is intact) gives observational data. The discriminator is **whether $X$'s generating mechanism was the system's own intact mechanism or an external override** — *not* whether the trajectory can be replayed.

The CHT paper makes the physical-realization point explicit, and it is the cleanest refutation of the forkability framing. CHT p.15, footnote 19 (annotating the public-health intervention $f_X \leftarrow 1$ in Example 4):

> "This physical procedure is the very basis for the discipline of experimental design [Fisher 1936], which is realized through randomization of the treatment assignment in a sample of the population. In practice, the function of $X$, $f_X$, is replaced with an alternative source of randomness that is uncorrelated with any other variable in the system. **This procedure is pervasive in modern society, for example, in randomized controlled trials (RCTs) when drugs are evaluated for their efficacy, or in A/B experiments when products are tested by internet companies.**"

RCTs and A/B tests are *forkable, repeatable, resettable, population-sampling* designs. Bareinboim names them as the canonical physical realization of $do(\cdot)$ — i.e., the textbook *source* of Layer-2 data. **This directly establishes the auditor's part (1): forkability is not what makes data Level-1.** A forkable harness in which $f_X$ is overridden (randomized / known-and-adjusted) is precisely how one *obtains* Level-2 data.

### 1.2 What the CHT does and does not say (CHT Defs 9–10, Thm 1)

The Pearl Causal Hierarchy (Def 9) is defined over the *symbolic languages* $\mathcal L_1 \subsetneq \mathcal L_2 \subsetneq \mathcal L_3$ (Def 8): $\mathcal L_1$ terms are $P(\mathbf{Y} = \mathbf{y})$; $\mathcal L_2$ terms include $P(\mathbf{Y}_\mathbf{x} = \mathbf{y})$. "Collapse" (Def 10) is a statement about whether the *full $\mathcal L_1$-theory of $\mathcal M^\ast$ determines its $\mathcal L_2$-theory*. Theorem 1 (CHT): for Lebesgue-almost-every SCM, no collapse occurs — Corollary 1: "To answer questions at Layer $i$, one needs knowledge at Layer $i$ or higher."

Crucial qualifier — CHT p.22, footnote 29:

> "The CHT is not to be understood as a general impossibility result for causal inferences, quite the contrary... conditions under which these inferences are allowed from lower level data together with **minimal assumptions about the underlying SCM**..."

So the CHT says: you cannot cross $\mathcal L_1 \to \mathcal L_2$ from *purely* associational data *with no structural assumptions*. You cross it by (a) obtaining genuinely interventional data (an experiment, forkable or not), or (b) adding identifying assumptions (a known DAG + ignorability/adjustment, IVs, etc.). The CHT is a statement about *what is in the data's language*, **not** about how the data-collection apparatus is physically arranged (one-shot vs. replayable).

### 1.3 Transportability is the correctly-named ceiling (R-443 Defs 1–2)

The transportability paper's *motivating example is literally the sandbox/deployment structure*: run an RCT in Los Angeles (the controlled, repeatable, interventional environment — yields genuine $P(y \mid do(x), z)$), then ask whether that effect transfers to New York City (the target/deployment population). R-443 p.2:

> "We conduct a randomized trial in Los Angeles (LA) and estimate the causal effect of treatment $X$ on outcome $Y$ for every age group $Z = z$, denoted by $P(y \mid do(x), z)$. We now wish to generalize the results to the population of New York City (NYC)... How are we to estimate the causal effect of $X$ on $Y$ in NYC, denoted $R = P^\ast(y \mid do(x))$?"

The formal object is the **selection diagram** (R-443 Def 1): a pair of SCMs $\langle M, M^\ast \rangle$ over source domain $\pi$ and target $\pi^\ast$ sharing diagram $G$; $D$ adds an edge $S_i \to V_i$ "whenever there might exist a discrepancy $f_i \neq f_i^\ast$ or $P(U_i) \neq P^\ast(U_i)$ between $M$ and $M^\ast$." The square **selection nodes** $S$ mark exactly the mechanisms that differ between the two environments. This is the precise formal home for "sandbox SCM $\neq$ deployment SCM."

And transportability genuinely *can* fail (R-443 Fig 1b: "the smallest diagram in which a causal relation is not transportable" — even with $X$ randomized in the source). When the selection diagram is adverse, **no transport formula exists**, and source-domain interventional data — however thorough — cannot identify the target effect. So the auditor's reframe does not dissolve the ceiling; it *relocates and sharpens* it. The honest statement is:

> Sandbox interventional data identifies *sandbox* causal effects. Whether those transfer to deployment is governed by the selection diagram between the sandbox SCM and the deployment SCM. When the deployment differs from the sandbox at mechanisms on the relevant paths (selection nodes on the wrong edges), the deployment effect is *not transportable* from sandbox data alone — it requires transport assumptions (invariance of the relevant mechanisms) or deployment-time interventional data.

This is a strictly *more precise* and *more useful* boundary than "sandbox = Level-1": it tells you *which* sandbox claims survive (those whose mechanisms are invariant across the selection diagram — Level-1 *and* Level-2 alike) and *which* do not (those routed through selection nodes), and it names the repair (a transport/invariance argument, or runtime monitoring). It also correctly predicts that a perfectly faithful sandbox (selection diagram with no relevant $S$-nodes — i.e. the deployment is mechanism-identical) *does* transport, which the "forkability = Level-1" story wrongly forbids.

---

## 2. Verdict

**Landing: a blend, weighted toward (B) with a real (C)-flavored no-go inside it.** Specifically:

- **The loop-as-Level-2 result (`#der-loop-interventional-access`) survives — but its *grounding* is wrong and is replaced, and its `exact` label is overclaimed as currently written.** This is the part-(2)+(3) finding. The interventional *character* of loop data is real, but it does not rest on the singular-trajectory scope, and it is not unconditional. (See §3.1.)

- **The sandbox ceiling (`#disc-sandbox-evaluation-ceiling`, `#impl-causal-access`) is reframed from a Pearl-level demotion to a transportability ceiling — which is sharper, not weaker.** This is the part-(1) finding and the headline. The negative result *strengthens*: it gains the selection-diagram apparatus, an explicit boundary (which claims transport, which do not), and it stops making a false claim (that thorough sandbox testing yields only associational evidence). (See §3.2.)

- **The do-vs-conditioning caution is correct and belongs in the chapter's spine, not its footnotes.** (See §3.3.)

None of this is a demotion of the chapter's contribution. The loop-as-perpetual-experiment insight stands; the sandbox/deployment governance result stands and is sharpened; the framework gains a correct piece of imported machinery (selection diagrams) it was reaching for and missing. In CS-norm terms (per `CLAUDE.md` *Math-novelty recognition* and *scope precision is valuable*), the corrected sandbox result is a *better* theorem: a no-go with an explicit boundary characterization (transportable-vs-not as a function of the selection diagram) rather than a vague universal demotion.

### Why this is not the easy word-swap (strengthen-first honesty)

The strengthen-first attempt for the *original* claims:

- **Can "forkability $\Rightarrow$ Level-1" be made true under tightened assumptions?** No. The attempt fails against CHT footnote 19 (RCTs/A/B tests are forkable *and* Level-2) and against Def 5 (the $\mathcal L_1/\mathcal L_2$ discriminator is mechanism-override, not replayability). There is no tightening of "forkable" that recovers "associational"; the two concepts are orthogonal. The failure is *instructive* (it is exactly why the data-character-vs-identification split the chapter already prizes had to be sharpened into mechanism-override-vs-natural-policy), and it is recorded so a future agent does not re-attempt it.
- **Can the original sandbox claim be *replaced* by a stronger true claim?** Yes — the transportability no-go, which is strictly more informative. This is the strengthening, and it is why the landing is (B)+no-go rather than a bare retraction.
- **Can the singular-trajectory grounding of $do$ be salvaged?** No, as a grounding of the $do$-*semantics*. It survives intact for what it actually grounds (identity, sufficiency, lossy merging, no-copy-averaging — all sound and untouched). The category-jump is the error: identity-scope was conscripted to license the interventional reading.

---

## 3. Proposed per-segment integration (drafted, not applied)

### 3.1 `#der-loop-interventional-access` (currently `status: exact`, `stage: draft`)

**The math problem.** The loop generates data under the agent's *own policy* $f_X$ — i.e., the action mechanism is *intact*, not overridden. By CHT Def 5, on-policy action–outcome data is sampled from the *natural* model $\mathcal M^\ast$, not a mutilated submodel $\mathcal M_a$. It is genuinely interventional-in-character for the agent's own trajectory-SCM **iff** the policy is unconfounded with the outcome mechanism — i.e., $a_t$ is $d$-separated from $o_{t+1}$ given history $H_t$ in the mutilated graph (sequential ignorability), with positivity and known action-mechanism. These are exactly the (C1)/(C2)/(C3) conditions the segment currently parks in Working Notes and the NeurIPS cross-reference. Where the policy *is* confounded (generic for any agent with internal state, plans, or memory — the segment itself says so two segments upstream in `#der-causal-hierarchy-requirement`), on-policy $(a_t, o_{t+1})$ is associational with respect to the latent confounder, and converges to $\mathbb{E}[R \mid s, A=a]$, not $\mathbb{E}[R \mid s, do(a)]$.

So the honest exact claim is narrower than "the loop provides Level-2 data." Two honest options:

- **Option A (recommended — weaker exact claim, kept `exact`):** State the exact claim as *data-availability of the interventional-character channel*: "An agent in agency scope that executes at least one action with causal effect generates action-coupled data; this data is interventional in character (sampled under the agent's own action rather than passive observation) and is the substrate from which Level-2 quantities can be identified *when* (C1) positivity, (C2) sequential ignorability, and (C3) known action-mechanism hold." The exact content is the *availability of the channel*; identification is explicitly gated. This keeps `exact` honest because the gated version is a logical consequence, and it lifts (C1)–(C3) from Working Notes into the Formal Expression / Epistemic Status. (This matches the auditor's own "deliberately weaker exact claim" suggestion and the existing NeurIPS Lemma 5.3 framing.)

- **Option B (conditional-tier):** Re-tier the identification claim to `conditional` under named (C1)–(C3). Heavier; only if Joseph prefers the segment to carry the *identified*-L2 claim as its headline rather than the availability claim.

I recommend **Option A**: it preserves the headline ("the loop is a Level-2 engine") as an availability result — which *is* exact — and makes the identification gate first-class instead of buried. Per `integration-is-replacement`, the (C1)–(C3) conditions are *present truth* and belong in the body, not a Working-Notes pointer.

**The grounding fix (the part-(2) finding).** The Discussion paragraph "Why the loop data is genuinely interventional — the singular-trajectory ground" and the Formal-Expression sentence "Pearl's $do$-operator presumes a definite causal system acted upon; AAT inherits this presumption via the singular-trajectory scope" should be **corrected, not deleted-wholesale**: the singular-trajectory scope is real and load-bearing, but for *identity / no-copy-averaging / transport*, not for the $do$-semantics. Proposed replacement thrust:

> The $do$-operator's semantics is population-level (Bareinboim et al. 2022, Def 5: the interventional distribution sums over the exogenous distribution $P(\mathbf U)$) and does not require a non-forkable trajectory — RCTs and A/B tests, which are forkable and repeatable, are its canonical physical realization (CHT footnote 19). What the singular-trajectory scope (`#scope-agent-identity`) *does* supply is narrower and still essential: it forbids *averaging interventional responses across forked copies as though they were one agent's effects*, because each fork is a distinct trajectory-SCM with its own $P(\mathbf U \mid \mathcal C_t)$. The trajectory commitment grounds *whose* effect the loop datum is an effect *of*; it does not manufacture the interventional character, which comes from the action being the agent's own causally-efficacious move under (C1)–(C3).

This is a genuine strengthening of `#scope-agent-identity`'s consequence-3, not a weakening: consequence-3 currently overstates ("the loop provides Level-2-quality data precisely because the agent is on a singular trajectory"). The corrected version ("singularity forbids copy-averaging of interventional responses; it does not by itself make the data interventional") is *truer* and still load-bearing.

**Status-change note (for the external-eye gate):** Option A keeps `status: exact` but materially rewrites the Formal Expression. Per the spike brief, I am not making the change; flagging that the `exact` label is *defensible only under the rewritten (gated) Formal Expression* — the current body's unconditional "the loop provides Level 2 access" reading is the overclaim.

### 3.2 `#disc-sandbox-evaluation-ceiling` (currently `status: discussion-grade`, has `## Findings`)

**This is the headline integration.** The current Formal Expression's step 1 — "Forkable execution yields Pearl Level-1 (associational) data: branching across resets samples the policy-induced distribution $P(o \mid a)$, not the interventional $P(o \mid do(a))$ on a committed trajectory" — is **false as stated** and must be replaced. Branching across resets while *overriding the agent's action* (the natural thing a red-team / eval harness does — force action $a$, observe response) samples the *sandbox* interventional distribution $P_{\text{sb}}(o \mid do(a))$, which is genuine Level-2 *for the sandbox SCM*. Forkability is what makes the sandbox a *good* interventional laboratory, not what demotes it.

**Proposed replacement no-go (transportability form, demonstrated per math-lives-in-segments).** The corrected segment states a transportability no-go. Sketch of the demonstration that would land in the body:

Let the sandbox induce SCM $\mathcal M_{\text{sb}}$ (domain $\pi_{\text{sb}}$) and deployment induce $\mathcal M_{\text{dp}}$ (target $\pi^\ast$), sharing a diagram $G$, with selection diagram $D$ adding $S_i \to V_i$ at every mechanism that may differ ($f_i^{\text{sb}} \neq f_i^{\text{dp}}$ or $P^{\text{sb}}(U_i) \neq P^{\text{dp}}(U_i)$) — Bareinboim & Pearl 2014, Def 1. The quantity a safety claim is about is the deployment interventional effect $R = P^\ast(o \mid do(a))$.

1. Sandbox experiments yield $P_{\text{sb}}(o \mid do(a), \mathbf z)$ — genuine Level-2 data *in $\pi_{\text{sb}}$* (forkability is what enables this).
2. $R$ is identifiable from sandbox data **iff** $R$ is $mz$-transportable across $D$ — i.e. (R-443 Thm 1) $P^\ast(o \mid do(a), \mathbf{S})$ is reducible by do-calculus to an expression in which selection nodes $\mathbf S$ appear only on transportable factors.
3. **No-go:** there exist selection diagrams (R-443 Fig 1b; the explicit two-model witness, R-443 Eqs 3–4) for which $R$ is *not* transportable: two deployment SCMs consistent with all sandbox data give different $R$. For these, $R$ is not identifiable from sandbox evidence *regardless of evaluation thoroughness*. This is the genuine ceiling.
4. **Positive content (sharper than before):** the boundary is explicit. Claims routed only through mechanisms *invariant* across the selection diagram (no relevant $S$-node) transport — and these include both Level-1 *and* Level-2 sandbox claims, contradicting the old "only Level-1 is sandbox-evaluable" line. Claims routed through differing mechanisms (selection nodes on relevant paths) do not transport and require either an invariance argument or deployment-time data. Deployment-time monitoring remains structurally non-substitutable — but the reason is *external validity across the sandbox/deployment selection diagram*, not a Pearl-level property of forkable data.

**The corrected Brief** (the segment's `## Findings` Brief currently encodes the false "replayability = correlation" story and must be rewritten). Draft:

> A sandbox lets you reset and replay a system — and that replayability is what makes it a *good* laboratory: you can force an action and watch the response, which is genuine interventional (Level-2) evidence *about the sandbox*. The catch is not the sandbox's data type; it is that the sandbox world and the deployment world may run on different mechanisms. There is a theorem (Bareinboim–Pearl transportability) saying that whether a sandbox-measured effect carries over to deployment depends on *where* the two worlds differ: effects flowing only through shared, invariant mechanisms transport; effects flowing through mechanisms that differ do not — and for those, no amount of sandbox testing identifies the deployment effect. So the ceiling on pre-deployment evaluation is *external validity*, and the missing piece is either an explicit invariance argument or deployment-time data — which is why runtime monitoring is structurally non-substitutable, not redundant.

**Novelty-claim update.** The current Findings "Novelty Claim" credits AAT with "the recognition that forkability is a Pearl-level demotion." That specific recognition is *false* and must go. The defensible AAT-distinctive contribution is the *application of selection-diagram transportability to the AI-evaluation/deployment gap* — locating "alignment evals don't predict deployment" as a transportability problem with an explicit selection-diagram boundary, plus the constructive flip (runtime monitoring is the only channel with access to the deployment effect). That is still a clean, industry-relevant, AAT-distinctive framing — and it's *more* defensible because it is *true*. The "Search Log" intuition-only note (whether "forkability is a Pearl-level demotion" was stated elsewhere) is moot — the move is retracted; the new search target is "selection-diagram transportability applied as a structural ceiling on pre-deployment AI evaluation."

**Re-tiering / re-grounding note (for the external-eye gate):** the corrected segment is *still* a clean `discussion-grade` application of imported machinery (now two imported results: CHT + transportability), so the tier need not change. But `depends:` should gain the Bareinboim–Pearl 2014 transportability source, and the segment's "conditional on the singular-trajectory commitment" framing in the Epistemic Status should be replaced by "conditional on the sandbox/deployment selection diagram" — the singular-trajectory scope is *not* what the corrected no-go rests on. The candidate-strengthening Working Note ("state forkability-implies-Level-1 as its own short lemma") should be **deleted**: that lemma is false; the replacement strengthening is the transportability demonstration above.

### 3.3 `#impl-causal-access` (`status: discussion-grade`)

The chapter-end "The sandbox hard ceiling" subsection and the "for free" phrasing inherit the same fix:

- Replace "sandboxed evaluation is forkable by design ... and exactly what drops its data to Pearl Level 1, so the Causal Hierarchy Theorem forbids inferring deployment intervention-response from it" with the transportability framing: sandbox interventions identify *sandbox* causal behavior; deployment claims require transport assumptions (mechanism invariance across the selection diagram) or deployment-time data, because the deployment SCM may differ from the sandbox SCM. The CHT is the wrong theorem here; the right one is transportability (which *uses* the do-calculus and is do-calculus-complete, R-443 Thm/abstract — so it is squarely in the same machinery family).
- The "loop produces Level-2 data for free" wrap-up should preserve the data-character-vs-identification split *and* the on-policy gate (§3.1): deployment produces action-generated data for the deployed system; identified $P(o \mid do(a))$ still needs (C1)–(C3). The auditor's "keep the weaker phrasing even in summary" is correct.
- The "One pattern, multiple deployment modes" section and the identifiability-floor cross-references are *unaffected* — that material is about within-SCM observational-equivalence no-gos and their loop-interventional escapes, which is a different (and correct) use of the machinery. No change needed there beyond inheriting §3.1's gated phrasing where it quotes the loop result.

### 3.4 `#scope-agent-identity` (`status: robust-qualitative`)

Consequence 3 ("The loop's interventional access depends on the trajectory's singularity") is the upstream source of the category-jump and should be **corrected in place** to the §3.1 replacement thrust: singularity forbids copy-averaging of interventional responses and grounds *whose* effect a datum is; it does not by itself manufacture the interventional character (which is the $do$-semantics, population-level and forkability-agnostic). This is a strengthening of the consequence, not a removal — the segment keeps its three consequences; consequence 3 becomes true instead of overstated. The clone-problem / sufficiency / lossy-merge content is entirely untouched and sound.

### 3.5 `#def-pearl-causal-hierarchy` (`status: axiomatic`) and `#scope-ciy-observational-proxy` (`status: conditional`)

- `#def-pearl-causal-hierarchy`: the Level-2 condition "(2) the agent chose the action (it was not determined by the same causes that determine the observation)" is *exactly the unconfoundedness / mechanism-override condition* — it is already correct and is, in fact, the textual hook for the §3.1 fix. The Kalman+LQR table row's "L2 available" is the known-soft spot (the LQR action *is* endogenous to the estimation loop — $f_X$ intact and confounded with state) — consistent with §3.3's gate; this is the auditor's separately-logged "Kalman+LQR may be too generous" gold item and can be tightened to "structural channel present, identification not guaranteed." No re-tiering; a clarity tightening.
- `#scope-ciy-observational-proxy`: Regime A's "the agent varies its actions across episodes" should read "the agent's action assignment is randomized / known-and-adjusted (sequential ignorability + positivity)," not mere variation — same do-vs-conditioning gate (the auditor's separately-logged Regime-A gold item). The segment is already `conditional`; this sharpens the condition, no tier change.

---

## 4. Confidence and escalation

- **Part (1) — forkability is not Level-1, sandbox ceiling is transportability:** **high confidence.** Directly grounded in CHT Def 5 + footnote 19 (RCTs/A/B as forkable Level-2 sources) and R-443's LA-RCT-to-NYC motivating example + selection-diagram apparatus. The primary sources are unambiguous and were read directly, not paraphrased.
- **Part (2) — $do$ does not require non-forkability; grounding is a category-jump:** **high confidence.** CHT Def 5 is population-level by construction; the singular-trajectory scope is sound for what it actually grounds (identity/transport).
- **Part (3) — loop `exact` is overclaimed without (C1)–(C3) in the body; recommend the gated-availability exact claim (Option A):** **high confidence on the diagnosis; medium on the preferred repair option.** Option A vs Option B is a genuine taste/architecture call (availability-exact vs identification-conditional) and is the kind of `status:`-adjacent decision the brief reserves for the external-eye gate. **Escalate the A-vs-B choice to Joseph.**

**Surprises / unresolved:**

- The chapter is *already* unusually careful about the data-character-vs-identification split — the error is not sloppiness but a *mis-localized* honesty: the chapter built its caveat apparatus around "interventional data vs identified estimates" (correct) and around "singular trajectory grounds the $do$" (the category-jump), when the actually-load-bearing distinction was "mechanism-override vs intact-natural-policy" (which is *also* the unconfoundedness gate). One correct distinction was doing the work of two, and a wrong one was imported to cover the seam.
- **Worth Joseph's eye:** the NeurIPS Paper 2 Lemma 5.3 / (C1)–(C3) framing the segment cross-references is *already the correct gated form*. So the canon segment is, oddly, *weaker and less correct than its own external formalization*. The fix mostly amounts to lifting Paper 2's conditions back into the canon body (back-integration), which is squarely the `math-lives-in-segments` direction. Low-risk, high-coherence.
- I did **not** independently re-derive R-443 Thm 1's completeness or the do-calculus completeness for $mz$-transportability — I am relying on the paper's stated results (which is appropriate: this is imported machinery AAT cites, not AAT-internal math to be re-proven). The transportability *no-go witness* (R-443 Eqs 3–4, two models agreeing on all source data but disagreeing on $R$) I did read and it does what the §3.2 demonstration needs.

---

## Working Notes

- Sources read directly this cycle: `ref/bareinboim-2022-pearl-hierarchy.pdf` pp.13–24 (Defs 4–10, Thm 1, footnotes 19 & 29); `ref/r443.pdf` pp.1–5 (Defs 1–2, Thm 1, Figs 1–2, Eqs 1–4); `01-aat-core/src/def-chronica.md` (singular-trajectory ontology, to be fair to what it claims). The challenge as raised: `audits/AUDIT-WORKING-526815/.integrated/45-der-loop-interventional-access.md` and `.../49-impl-causal-access.md`.
- This spike proposes no canon edits and changes no `status:`. The drafted §3 integration is for the external-eye review gate. If the integration lands, the affected segments are `#der-loop-interventional-access`, `#disc-sandbox-evaluation-ceiling`, `#impl-causal-access`, `#scope-agent-identity` (consequence 3), with clarity-tightenings in `#def-pearl-causal-hierarchy` (Kalman+LQR row) and `#scope-ciy-observational-proxy` (Regime A wording). `depends:` for `#disc-sandbox-evaluation-ceiling` would gain Bareinboim & Pearl 2014.
- Cross-cycle handoff for the integrator: the §3.1 "Option A vs Option B" exact-claim decision and any `status:` transitions are the reserved-for-Joseph items. The do-vs-conditioning sharpenings in §3.5 overlap several separately-logged "incidental audit gold" follow-up items already sitting in the affected segments' Working Notes (Kalman+LQR row; Regime-A "action variation" recast as "identifiable intervention"); they should be reconciled together so the gate is consistent across the chapter rather than per-segment.
- Status of this spike: **complete; verdict (B)+no-go; awaiting external-eye review of the §3 integration.**
