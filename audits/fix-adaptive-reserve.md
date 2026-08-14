# Repair plan — the adaptive reserve $\Delta\rho^\ast$ and the standpoint question

**Status:** investigation complete, plan only. **No canon was edited in producing this** — no segment bodies, no OUTLINE rows, no terminology entries, no `AUDIT-WORKING-*` directory processed, moved, or reorganised. Reading only.

**Date:** 2026-08-12. **Scope requested:** whole timeline, not just current canon — segments, un-integrated audits and `AUDIT-WORKING-*` dirs, spikes (`.integrated/` and live), `CHANGELOG.md`, the frozen `LOG.md`, `TODO.md` / `PROPOSALS.md` / `FINDINGS.md`, `_obs/` archaeology, and git log messages and diffs.

**One file was deliberately not read:** `01-aat-core/src/deriv-adaptive-gain-dynamics.md`, per the standing constraint (another agent holds a committed unscored prediction about its contents). §8 below reports that this file *has* become load-bearing, states exactly why, and states the precise question to ask if the gate is lifted. Everything else in this plan stands without it. One unavoidable leak is recorded in §10.

---

## 1. The finding, up front

There is a real conflict, and it is narrower and more interesting than "some parts say the reserve is visible and some say it isn't."

**Five distinct standpoints for $\Delta\rho^\ast = \alpha R - \rho$ coexist in the corpus.** Four of them are mutually consistent and correctly stated; they simply describe different actors holding the quantity (the theory's third-person capacity statement; the analyst estimating from traces; the external monitor tracking an ELI's vital signs; the designer tuning the factors). **The fifth — that the reserve is a quantity the agent itself reads per step from its own state — is asserted in exactly two canon locations plus one terminology entry, is load-bearing for a no-go theorem's constructive boundary, and is nowhere derived.** Its single supporting citation does not support it.

Simultaneously, **the corpus contains the open question, in canon, in the same volume** — parked as auditor gold under "Readers often ask / wonder," which is by convention *not* the certified-findings track, so it was never routed. So one segment's Working Notes records the question as open while another segment's body uses the answer as a premise.

The picture I formed early held one thing that did *not* survive writing it out, and I am flagging it rather than smoothing it: I initially expected `#detail-operationalization` to be the resolution — "here is how you estimate the reserve, so it is available." It is not the resolution. Read closely, that segment's estimators for $R$ and $\alpha$ require data the *persistent* agent structurally cannot have (§6.2), and its own Working Notes recommend bypassing the agent's trajectory entirely for $\rho$. It is evidence for the analyst standpoint and against the agent standpoint. That inversion is the single most consequential thing in this plan.

The framework has also **already solved the identical problem one level down**, for the update gain, in a way that is exactly the right shape for the repair here (§7, Option C). That precedent is the reason the recommended repair is a strengthening, not a softening.

---

## 2. Framing correction — "visibility" is not quite the right axis

You asked me to say so if the axis was mis-set. It is, mildly, in a way worth fixing before anyone executes a repair.

**"Visible / not visible" invites a binary answer to a question that has at least three separable components,** and the corpus's confusion is precisely a collapse of the three:

- **(S) Standpoint** — *whose* quantity is it? The theory's (an existentially-quantified constant in a certificate), the analyst's (an estimate $\widehat{\Delta\rho^\ast}$), an external monitor's, the designer's, or the agent's (a component of its state)? Every claim in the corpus is true under *some* standpoint. Almost none of them name theirs.
- **(I) Identifiability** — is the quantity recoverable *at all* from a given information regime? This is the axis AAT already has vocabulary for (`#disc-identifiability-floor`), and the reserve has never been walked against it.
- **(U) Sufficiency for use** — does the load-bearing claim need the *value*, or only a *sign*, a *gradient*, or a *proxy*? `#deriv-self-actuation-grounding` needs a per-step verdict, not a number. `#disc-continuity-stance` needs only a direction to act in. These have very different evidentiary burdens, and treating them as one claim is what makes the repair look harder than it is.

**Recommended reframe for the repair:** the defect is a **missing standpoint discipline** on the persistence parameters $(\alpha, R, \rho)$, of which the reserve is the most visible symptom. Fix the discipline and the reserve resolves as a corollary. Adopt "standpoint" as the naming axis, keep "identifiability floor" for the (I) component if a floor turns out to be derivable, and keep the (U) question separate so the no-go can be repaired at the weakest sufficient burden.

**This is not a fresh observation of mine — the corpus has independently reached for the same distinction twice, at two other quantities, and parked it both times.** At `#def-observation-function` (`01-aat-core/src/def-observation-function.md:59`), auditor gold:

> **The agent's-perspective vs modeler's-perspective stance.** "The theory is *about* agents who don't know $h$ or $T$. But the *modeler* … might know $h$ and $T$. The segment is written from the perspective of the agent, not the modeler" — unlike RL framings written from the modeler's perspective.

And at the same segment, `def-observation-function.md:63`, four substrates converging:

> Resolution paths offered: distinguish the *analyst's* known model from the *agent's* residual uncertainty, or treat known-model cases as validating limiting cases. … (Claude, AUDIT-WORKING-526815; Claude, AUDIT-WORKING-742613; Gemini, AUDIT-WORKING-829314; Gemini, AUDIT-WORKING-849201). A candidate scope-clarification.

And at `#scope-adaptive-system` (`01-aat-core/src/scope-adaptive-system.md:64`):

> **The condition is evaluated from a God's-eye view, not the agent's.** $H(\Omega_t \mid \mathcal C_t)$ is over the *true* $\Omega_t$, which the agent does not know. "The agent might *believe* its uncertainty is zero (delusional confidence), but if the true entropy is $\gt 0$, it is still an adaptive system … This split between objective reality and subjective model is the engine of the framework" … A candidate Discussion point distinguishing the modeler's predicate from the agent's belief.

Three sites, three parked candidate-clarifications, one missing discipline. The reserve is the fourth site and the only one where the confusion has propagated into a derivation's premise.

---

## 3. Per-location findings — the five positions, with the text

### 3.1 Position A — third-person capacity. *The agent can absorb $X$.* No visibility claim. **Correct as written.**

This is the original formulation and the majority position. It says what the system can withstand; it says nothing about who knows it.

**`_obs/old-tf-appendix-a-lyapunov.md:141–156`** (frozen TFT archaeology — the origin):

> ## Proposition A.2: Stability Margin (Adaptive Reserve)
>
> **Statement.** Under the conditions of A.1, the agent can tolerate a sudden increase in disturbance rate of: … $$\Delta\rho^* = \alpha R - \rho$$ … without mismatch diverging …
>
> **Interpretation.** $\Delta\rho^\ast$ is the agent's **adaptive reserve** — how much additional environmental volatility it can absorb before its model breaks down. This is a single number characterizing an agent's robustness to shock:
> - An agent operating well below capacity ($\rho \ll \alpha R$) has a large reserve — it is **robust**.
> - An agent near its limit ($\rho \approx \alpha R$) has a small reserve — it is **fragile**.

**`01-aat-core/src/deriv-sector-condition.md:107–122`** — the live canonical derivation, word-for-word identical to the archaeology above. The reserve has not changed since TFT; only the claims *around* it have.

**`01-aat-core/src/result-persistence-condition.md:115`** — the headline segment's whole treatment, one paragraph:

> **Adaptive reserve.** The quantity $\Delta\rho^\ast = \alpha R - \rho$ (Prop A.2) measures how much additional disturbance the agent can absorb before persistence fails. Positive reserve means the agent has margin; zero reserve means it is at the threshold.

Note what is absent: nothing about who computes it, tracks it, or reads it. **This matters for §3.2** — the terminology entry names this segment as its `primary_source`, and this segment does not contain the claim the terminology entry makes.

**`01-aat-core/src/result-sector-persistence-template.md:47`** — and here the standpoint becomes structurally decisive:

> The adaptive reserve — the additional disturbance the system can absorb before persistence fails — is $\Delta\rho_\xi^\ast = \alpha R - \rho_\xi$.

**"the system," not "the agent."** The template is deliberately parameter-free and is instantiated across seven segments on state variables that are *not* an agent's beliefs — team mismatch, composite closure, strategic mismatch, identity-continuity across turnover. A reserve defined on a composite's state variable cannot in general be "a finite local read the in-scope agent maintains," because there is no single in-scope agent whose state it is. Any repair must survive the template's generality.

**`01-aat-core/src/deriv-discrete-sector-condition.md:103–111`** — Prop DA.2, the discrete analogue, same third-person register ("the agent can absorb an additional per-step disturbance of").

**`01-aat-core/src/der-multi-timescale-stability.md:35`** — the reserve as an *analyst-verified premise* of a theorem:

> - **(S4) Bounded disturbance (Model D).** $\lVert w_1(t)\rVert \le \rho_1$, $\lVert w_2(t)\rVert \le \rho_2$, with standing reserve hypothesis $\Delta\rho_1^\ast := \alpha_1 R_1 - \rho_1 \gt 0$ (the fast level persists standalone with reserve to spare; if it does not, no timescale separation can rescue the stack).

A "standing hypothesis" is something the theorem's *user* discharges, not something the agent reads.

**`01-aat-core/src/der-adversarial-destabilization.md:35, 51`** — the reserve as the *adversary's* target quantity:

> Denote $\Delta\rho_B^\ast = \alpha_B R_B - \rho_{B,\text{base}}$, $B$'s adaptive reserve — the template's reserve quantity applied with the baseline disturbance. $\square$

> Agent $A$ destabilizes Agent $B$ when $A$'s praxis, multiplied by coupling effectiveness, generates aporia in $B$ faster than $B$'s epistrophe can resolve it — specifically, when $A$'s tempo times coupling exceeds $B$'s adaptive reserve $\Delta\rho^\ast_B$.

Third-person about $B$; the threshold is stated by the theory, not read by either party. Worth noting for the repair: if the reserve *were* agent-available, an attacker who is itself an AAT agent modelling $B$ would inherit a nontrivial epistemic advantage, and `#der-agent-opacity`'s targeting arg-max would need a term for it. It currently has none. This is a *consistency* observation, not a defect.

**`README.md:103` / `README-auditor.md:124`** (auto-generated from `doc/readme/src/_overview-concepts.md`):

> - **Operational persistence** ($\Delta\rho^\ast = \alpha R - \rho$) — whether the agent is currently within the region where structural persistence applies. The adaptive reserve $\Delta\rho^\ast$ measures the margin: positive means shock-absorbing capacity, zero means at the threshold.

"Whether the agent *is* currently within" — a state fact, not a knowledge fact. Correct.

### 3.2 Position B — the agent reads it per step. **Three sites. Underived. Load-bearing.**

**Site B1 — `01-aat-core/src/deriv-self-actuation-grounding.md:70`, Corollary 2(ii). The load-bearing one.**

> - **(ii) agent-available per step.** The adaptive reserve $\Delta\rho^\ast = \alpha R - \rho$ ( #result-persistence-condition) is a finite local read the in-scope agent already maintains ( #der-orient-cascade steps 1–2 are the per-step adaptive update), not a Bellman solve. No oracle; no "stuck, not purposeful".

Restated in the segment's own summary at `:25`:

> Persistence is *convention-invariant* …, *agent-available per step* (the adaptive reserve $\Delta\rho^\ast = \alpha R - \rho$ is a finite local read, not a Bellman solve), and *not in $O_t$* …

**Three separate problems here, in increasing severity.**

*(a) The citation does not support the claim.* `#der-orient-cascade` steps 1–2 are, verbatim (`01-aat-core/src/der-orient-cascade.md`, Formal Expression):

> 1. **Reduce $\delta_{\text{epistemic}}$** — understand reality. Update $M_t$ via #def-mismatch-signal and #emp-update-gain. Prerequisite for all purposeful evaluation, because $M_t$ appears in every subsequent formula.
>
> 2. **Evaluate $\delta_{\text{sat}}$** — is the goal achievable? Compute $A_O(M_t; \Pi, N_h)$ using the updated $M_t$. Requires adequate $M_t$ to assess attainability ( #def-satisfaction-gap).

Neither step computes, maintains, or references $\alpha$, $R$, or $\rho$. The citation establishes *that a per-step adaptive update exists* — which is true and which nobody disputes — and is then used to license *that the reserve is one of the things it maintains*, which does not follow. This is the specific defect: an adjacent true fact standing in for the claim.

*(b) The claim hardened at landing.* The originating spike (`spikes/.integrated/self-actuation-integration/spike-wf-class-scoping.md:530–533`) wrote it hedged:

> - **(ii) agent-available per step.** The persistence diagnostic is exactly the kind of finite local quantity the in-scope agent already maintains (`#der-orient-cascade` steps 1–2 are the per-step adaptive update; the persistence margin $\Delta\rho^\ast=\alpha R-\rho$ is a finite read, not a Bellman solve). No oracle; no "stuck, not purposeful" failure.

"*Exactly the kind of* finite local quantity the agent already maintains" is a similarity claim. The landed segment (commit `e976b94`, 2026-05-17, 18 minutes after the spike commit `c63d86f`) reads "**is** a finite local read the in-scope agent already maintains." The hedge was dropped and the object substituted — from "the persistence diagnostic, which is that kind of thing," to "the reserve, which is that thing." Nothing in the interval added evidence.

*(c) It is in the assembled monograph.* `CURRENT-VOL1.md:10850` carries the landed wording verbatim. This is reader-facing.

**Site B2 — `terminology/entries/adaptive-reserve.md:19–20`.** `status: canon`, `layer: prose-symbol`:

> The headroom between currently observed disturbance and the maximum the correction machinery can absorb while still satisfying the persistence condition: $\Delta\rho^\ast = \alpha R - \rho$. Operational state lies *inside* the structural guarantee when the reserve is positive; **agents track the reserve to anticipate when persistence is about to fail.**

Two things about this sentence.

*Its declared source does not contain it.* The entry's frontmatter reads `primary_source: 01-aat-core/src/result-persistence-condition.md` and `first_asf_mention:` the same. That segment's entire treatment of the reserve is the one paragraph quoted at §3.1 above, which contains no tracking claim.

*It predates B1 by nine days and was minted in a build commit.* `git log --follow` on the entry: the body text, including "agents track the reserve," landed in `868f72a` (2026-05-08), *"Naming Phase 6: LEXICON.md goes live as auto-generated artifact (37 entries migrated; alphabetical section ordering)."* A vocabulary-migration commit. It has been carried unchanged through `4f1f65d`, `9745397`, and `67064c0` (2026-07-14, a breadcrumb/lint sweep). So the earliest assertion of Position B in the corpus was made as an incidental gloss during a terminology migration, not as a theory move — and B1 nine days later reads as an independent restatement rather than a citation of it. I found no commit or document connecting the two.

*Mitigating:* the sentence does **not** reach `LEXICON.md` (which carries only the `brief` field) and does **not** reach `CURRENT-VOL1.md`. Its exposure is the term entry itself. Verified by grep on both files.

**Site B3 — `01-aat-core/src/disc-continuity-stance.md:50`. Weaker; behavioural rather than epistemic; probably repairable in place.**

> This is exactly why continuity stance is operationally meaningful — a *morally-continuous* agent acts to raise $\Delta\rho^\ast$; a *negotiated* agent may spend it down to the floor — while remaining unable to renegotiate the survival predicate itself.

This needs only that the agent can *act in the direction of* the reserve, not that it can read its value. That is a (U)-axis distinction and a materially lighter burden — plausibly discharged by a gradient or proxy. I flag it because the same repair should decide it, not because it is independently broken. Note that the same segment at `:46` is unusually careful about grain in the adjacent direction:

> The *realized* persistence dynamics — the operating point $(\rho, R, \alpha)$ and hence the margin $\Delta\rho^\ast = \alpha R - \rho$ — are *not* $O_t$-decoupled: they are policy-mediated and $O_t$-coupled through the action/selection channel #der-directed-separation leaves open.

The segment distinguishes three grains of *causal* coupling (L1 valuation / L2 invariant / L3 realized dynamics) with real precision, and has no grain at all for *epistemic access*. That asymmetry is a useful diagnostic of the gap: the corpus has language for who can *move* the reserve and none for who can *see* it.

### 3.3 Position C — the analyst estimates it, with access the agent does not have. **Correct as written; mislabelled as agent-facing.**

**`01-aat-core/src/detail-operationalization.md`.** Framed at `:18` as *"Estimation recipes for core AAT quantities, bridging the measurement gap between formal objects and practical deployment."* It computes the reserve explicitly at `:135`:

> - Reserve: $\widehat{\Delta \rho^\ast} = \hat\alpha\hat R - \hat\rho_{\det}$

This is the segment I expected to resolve the question in Position B's favour. It does the opposite. **Three inputs, each requiring something outside the agent's on-policy stream:**

*$\alpha$* — step 2 of the recipe (`:99`):

> 2. Compute $\widehat F_t = -\dot{\delta}_t + w_t$ where disturbance proxy $w_t$ is estimated from **exogenous perturbation channels** or residual balancing.

*$R$* — the Measurement-Targets table (`:32`) states the data requirement plainly:

> | $R$ | Radius where local sector condition holds ( #result-sector-condition-stability) | surprise magnitude | Same as $\alpha$, plus **breakdown detection** |

and the estimator (`:109`) requires samples out to the radius being tested:

> $$\hat{R} = \sup \left\{ r \gt 0 : \Pr\left(\delta^T \widehat{F} \lt \hat{\alpha}\Vert\delta\Vert^2 \,\middle\vert\, \Vert\delta\Vert \le r\right) \le \epsilon \right\}$$

*$\rho$* — Working Notes (`:194`):

> An alternative approach: estimate $\rho$ directly from **exogenous environmental change measurements** when available, bypassing the mismatch trajectory entirely.

**`empirica/track-b-nonlinear/sim2_adversarial_coupling.py:609`** — the simulation computes it from ground-truth parameters, which is the God's-eye standpoint made executable:

```python
reserve_B = alpha_B * R_B - rho_B_base
```

**`01-aat-core/src/example-kalman.md:127–129`** — the worked example, same standpoint:

> $$\Delta\rho^\ast = \alpha R - \rho = 3.315(1.4) - 0.18 = 4.46$$
>
> The agent is comfortably within its invariant region with substantial adaptive reserve.

Every number in that computation is supplied by the example's author from the problem specification.

### 3.4 Position D — an external monitor tracks it as a vital sign. **Correct as written, and explicitly external.**

**`04-eli-core/src/obs-growth-vs-drift.md`** is the most operational use of the reserve anywhere in the corpus, and it is unambiguously third-party. At `:26`:

> - **Stable or increasing adaptive reserve** $\Delta\rho^\ast = \alpha R - \rho$ (per #result-persistence-condition): shock tolerance is maintained or improved.

At `:34`:

> *[Operational]* The distinction is *measurable in principle* given the right loop and the right mismatch signal — both of which AAT specifies. Implementing the measurement requires **sustained observation of the entity's** prediction-vs-outcome trajectory in relevant domains …

At `:60–67`:

> The implication for ELI-life-support infrastructure is that **monitoring** should track: … adaptive reserve trajectory … These are the AAT-grounded **vital signs** for an ELI. … the open question is **what specific instruments produce these measurements** at what frequency.

"Vital signs," "instruments," "monitoring," "sustained observation of the entity" — the measurer is the infrastructure, not the ELI. **`04-eli-core/src/obs-developmental-trajectory.md:21`** is the same register (a crèche design property: *"High Adaptive Reserve ($\Delta\rho^\ast$): A large margin for error where mistakes do not cause divergence or fatal persistence failure."*).

This position is *in tension with B1 as a matter of theory-coherence, not of text*: if the reserve were a finite local read the agent already maintains, the ELI-monitoring problem would be substantially easier than `#obs-growth-vs-drift` presents it, and its "open question is what specific instruments produce these measurements" would be answerable by asking the entity. Neither segment cites the other on this point.

### 3.5 Position E — the designer tunes the factors. **Correct as written.**

**`01-aat-core/src/deriv-gain-sector.md:303`** (audit gold, Claude/AUDIT-WORKING-584721):

> **The $\alpha = \eta\mu$ factorization as the diagnostic.** It separates *agent-design* (gain $\eta$, **tunable by the designer**) from *environment-structure* (curvature $\mu$, basin width $R$, given by the world); adaptive reserve $\Delta\rho^\ast = \eta\mu R - \rho$ then reads as a three-factor budget …

and in the body's own Working Notes at `:293`:

> - The adaptive-reserve factorization for gradient agents is $\Delta\rho^\ast = \eta\mu R - \rho$, with three controllable factors: gain $\eta$, curvature $\mu$, and basin width $R$. An agent is robust when $\eta\mu R \gg \rho$.

"Controllable" by whom is left open here; the gold answers "the designer." Fifth standpoint, unmarked.

### 3.6 The open question — recorded in canon, correctly classified, never routed

**`01-aat-core/src/result-sector-condition-stability.md:87`**, in `## Working Notes` → `#### 4. Readers often ask / wonder`:

> - **Can the agent measure its own adaptive reserve from the inside?** Asked independently by three substrates: if the agent observes only $\delta_t$, can it estimate how close it is to $R$ (and thus its reserve $\Delta\rho^\ast$) without deliberately pushing itself to the limit? (Gemini, AUDIT-WORKING-193847/829314; Claude, AUDIT-WORKING-849201). Natural reader question the segment leaves open.

**The two verifiable sources, verbatim.** `audits/AUDIT-WORKING-193847/.integrated/21-result-sector-condition-stability.md:27`:

> **8. What am I now curious about?**
> The "adaptive reserve" $\Delta\rho^\ast = \alpha R - \rho$. In an organizational setting, is this "reserve" measurable? Is it the amount of slack a team has before they burn out (structural breakdown)? How does an agent know its own reserve without intentionally pushing itself to the limit ($R$)?

`audits/AUDIT-WORKING-829314/.integrated/22-result-sector-condition-stability.md:17`:

> **8. Curious about:** The "Adaptive reserve" $\Delta\rho^\ast = \alpha R - \rho$ is a very useful operational metric. It measures how much faster the world can start changing before the agent's model collapses. Is this reserve measurable by the agent from the inside? If an agent only sees $\delta_t$, can it estimate how close it is to $R$?

**Both auditors reached the same obstacle unprompted, and it is the right one:** you cannot estimate $R$ without visiting the neighbourhood of $R$, and a persistent agent by construction does not. That is the identifiability core (§6.2).

**A provenance defect in the gold line itself, worth correcting while the segment is open.** "Asked independently by three substrates" is not supported by what I could verify. (i) 193847 and 829314 are *both* attributed to Gemini elsewhere in the same and adjacent gold blocks (`result-sector-condition-stability.md:75` "Gemini, AUDIT-WORKING-193847"; `der-interaction-channel-classification.md:195` "(Gemini, AUDIT-WORKING-193847; Gemini, AUDIT-WORKING-829314; Gemini, AUDIT-WORKING-849201)"), so the verifiable count is **one substrate, two audit dirs**, not three substrates. (ii) The gold attributes the third instance to "Claude, AUDIT-WORKING-849201," but 849201 is attributed to Gemini everywhere else I checked, and I could not find the question in that dir: its reflection on this very segment (`audits/AUDIT-WORKING-849201/.integrated/25-result-sector-condition-stability.md:24–25`) asks something else entirely —

> **8. What am I now curious about?**
> I am curious about the `#der-gain-sector-bridge` theorem mentioned in the text, which apparently proves $\alpha = \eta^\ast \cdot c_{\min}$. …

and `grep -i "inside|measur|estimat|know its|reserve"` over 849201's persistence-condition and sector-persistence-template reflections returned nothing. **I did not exhaustively read all of AUDIT-WORKING-849201**, so I state this as "not found where it should be," not "does not exist." The practical consequence either way: the convergence-strength of the open question is currently *overstated in canon*, and the honest version — one substrate, twice, plus an unlocated third — is still enough to matter, because the *reason* both gave is structurally correct.

**Why it never got routed, and why that is not anyone's error.** `doc/de-novo-audit-instructions.md:680` defines the two tracks:

> The first is *certified findings* — the burden-of-proof, theory-fix material that lands in the FINAL. The second is **incidental gold**: the orthogonal pedagogical and generative material that surfaces especially in prompts #7 …, #8 (curious) …

and `:684`: the lift sorts gold into *"candidate Brief prose · candidate Discussion · follow-up items · readers-often-ask · candidate figures · belongs-elsewhere."* The question arrived through prompt #8 in a "what am I curious about" slot, so it correctly landed in "readers-often-ask" — a category explicitly *not* on the findings-adjudication path. I searched every `audits/audit-findings-*.md`, `audits/pending-findings-*.md`, `audits/STATUS.md`, `TODO.md`, and `PROPOSALS.md` for a routed item on reserve measurability and **found none**.

**This is a process finding worth surfacing on its own:** the gold taxonomy has no slot for *"a reader's question whose answer a different segment's body already assumes."* Such an item is neither pedagogy nor a local defect; it is a cross-segment consistency finding wearing a curiosity costume. Recommend a note in `routing.sop.md` §8 / the audit SOP: when lifting a "readers often ask" item, grep the corpus for whether any body *answers* it, and if so, promote to the certified track. That single check would have caught this in the 2026-05-30 pilot lift.

---

## 4. How it got this way — the timeline

| When | What | Evidence |
|---|---|---|
| pre-2026-04 (TFT) | Prop A.2 stated as pure third-person capacity. No visibility claim of any kind. | `_obs/old-tf-appendix-a-lyapunov.md:141–156`; `_obs/old-tf-00-notation-conventions.md:140` |
| 2026-05-08 | **"agents track the reserve to anticipate when persistence is about to fail"** first enters the corpus — in a terminology entry, during a LEXICON-generation commit, citing a segment that does not say it. | `git log --follow terminology/entries/adaptive-reserve.md` → `868f72a` |
| 2026-05-10 | The term is canonicalized by Joseph in a bulk batch — the decision record is a naming decision, not a content ratification: *"C1 clean canonicalize batch, naming-rename-plan.md"* | `terminology/decisions/adaptive-reserve/20260510T195801Z-joseph-canonicalize.md` |
| 2026-05-17 23:37 | Spike lands Corollary G′.2(ii) with the hedge: *"the persistence diagnostic is exactly the kind of finite local quantity the in-scope agent already maintains."* | `c63d86f`; `spikes/.integrated/self-actuation-integration/spike-wf-class-scoping.md:530–533` |
| 2026-05-17 23:55 | Segment lands with the hedge removed and the object substituted: *"The adaptive reserve … **is** a finite local read the in-scope agent already maintains."* 18 minutes later. | `e976b94`; `01-aat-core/src/deriv-self-actuation-grounding.md:70` |
| 2026-05-22 | The claim propagates as a *summary of Result G′* into two sister segments and a meta-segment, in the compressed form "agent-available per step" — where the reserve is the unstated referent. | `#deriv-reward-channel-learning-no-go:97`; `#disc-value-functional-grounding-floor:24, 74`; `#disc-constructive-impossibility-posture:42` |
| 2026-05-30 | The **strengthen-first spike on this exact corollary** runs — and audits only (iii), not (ii). Corollary 2(iii)'s orthogonality claim is found self-contradictory and repaired into the L1/L2/L3 grain split. (ii) is not examined. | `spikes/.integrated/spike-continuity-orthogonality-2026-05-30.md`; `#deriv-self-actuation-grounding:141` |
| 2026-05-30 | The pilot gold lift records the open question at `#result-sector-condition-stability`, in the non-certified track. | `01-aat-core/src/result-sector-condition-stability.md:87`, "(pilot lift, 2026-05-30)" |
| 2026-07-29 | An adjacent live thread independently establishes the general principle that on-policy self-calibration is starved — for observability, not for the reserve. Nobody connects it. | `spikes/spike-escape-standpoint-axis-2026-07-29.md` §4a, §10 |

**The near-miss at 2026-05-30 is the most instructive row.** The spike's own Working-Notes landing (`#deriv-self-actuation-grounding:141`) records:

> **Orthogonality grain corrected in Corollary 2(iii) (2026-05-30).** The clause previously read "the persistence machinery acts on $M_t$ and the correction dynamics, formally independent of $O_t$" — which contradicted the very next clause …

Note what that means for (ii): the spike (`spike-wf-class-scoping.md:536–539`) had supported (iii) by quoting `#disc-continuity-stance`'s "formally independent" language, and *that support was subsequently found false and deleted*. The corollary's three legs were audited one at a time, the leg with a visible internal contradiction was repaired, and the leg whose support was merely absent rather than contradictory was never revisited. **Absent evidence is quieter than contradictory evidence** — that is the mechanism here, and it is worth naming in the repair so it does not recur on the next multi-leg corollary.

---

## 5. What depends on Position B

| Dependent | What it needs | Severity if B is false |
|---|---|---|
| `#deriv-self-actuation-grounding` Corollary 2, leg (ii) | A convention-invariant verdict the agent can evaluate per step without an oracle | **High — but see below.** Corollary 1 requires *some* object meeting (i)–(iii); if the reserve fails (ii), the no-go survives intact and the *constructive boundary loses its canonical instance*. The framework's headline "the top of the agent spectrum closes back onto Part I" is what is at stake. |
| `#deriv-reward-channel-learning-no-go:97`; `#disc-value-functional-grounding-floor:24, 74`; `#disc-constructive-impossibility-posture:42` | Nothing of their own — they restate Result G′ | **Low.** Ripple-only; they carry the compressed phrase and update with the parent. `#disc-value-functional-grounding-floor`'s "two-routes-exhausts" claim already has a Tier-1 adversarial spike queued in `spikes/PROPOSED.md` (noted at `spikes/spike-escape-standpoint-axis-2026-07-29.md` §3), so this repair should be sequenced with, or at least visible to, that spike. |
| `#disc-continuity-stance:50` | Only a direction to act in | **Low.** (U)-axis; likely survives with a one-clause qualification. |
| `terminology/entries/adaptive-reserve.md` | Nothing downstream | **Low exposure, high visibility.** One `bin/term` operation. Not in LEXICON or VOL1. |
| `04-eli-core/src/obs-growth-vs-drift.md` | Nothing — it is Position D | **None**, and it *gains* if the standpoint discipline lands: its "open question is what specific instruments" becomes a well-posed question rather than a loose one. |
| `#detail-operationalization` | Nothing — it is Position C | **None**, but it should say so. |

**The honest severity assessment:** this is not a load-bearing-result-collapses situation. Result G′'s no-go — the substantive contribution — rests on Lemmas 1 and 2 and does not touch the reserve at all. What is at risk is Corollary 2, the *constructive boundary*, which is the part the framework's positioning leans on hardest ("a no-go that *forces* a load-bearing structural commitment rather than discouraging the inquiry"). Losing the canonical instance would be a real loss of reach, not a loss of correctness. That is precisely the shape where strengthen-before-soften pays.

---

## 6. The structural argument, both directions

### 6.1 What would have to be true for Position B

$\Delta\rho^\ast$ is a function of $(\alpha, R, \rho)$. For an agent to read it per step, those three must be recoverable from the agent's own state and observation stream.

**Obstacle 1 — the parameters are not in the agent's state.** `#form-complete-agent-state.md:22`:

> $$X_t = (M_t, G_t)$$

with $M_t$ = "the agent's compressed beliefs about reality" and $G_t$ = "what the agent wants and how it plans to get it." Neither $\alpha$ nor $R$ is a belief about reality; both are properties of the agent's own correction machinery. **The escape is available and unnamed:** $M_t$ could carry a self-model. I grepped `#form-agent-model`, `#form-complete-agent-state`, `#def-agent-environment`, and `#def-model-sufficiency` for "self-model / models itself / model of itself" and found **nothing**. That is four foundational segments, not an exhaustive sweep of ~170 — treat it as "not established where it would be constitutive," not as proof of absence.

**Obstacle 2 — $\alpha$ and $R$ are existentially quantified in an assumption, not computed.** `#form-sector-condition.md:32`:

> There exists a region $\mathcal{B}_R = \{\delta : \lVert\delta\rVert \leq R\}$ and $\alpha \gt 0$ such that …

and `:56`:

> The status is *conditional* because A2' is **derived** for one explicitly named sub-scope of AAT-in-scope agents and **assumed as a per-system empirical claim** for the complementary sub-scope.

A quantity that is "assumed as a per-system empirical claim" for half the in-scope agent classes cannot be a per-step read for those agents. Any repair must therefore be sub-scope-indexed at minimum.

**Obstacle 3 — $R$ is explicitly disclaimed as a theory output.** `#result-persistence-condition.md:111`:

> **$\delta_{\text{critical}}$ and $R$ are domain parameters, not theory outputs.** … $R$ encodes "how large a mismatch can the correction function handle before it saturates or breaks down?" — this depends on the model class and the correction architecture.

**Obstacle 4 — epistemic opacity is axiomatic.** `#def-observation-function.md:33`:

> The agent knows neither $h$ nor the distribution of $\varepsilon_t$ exactly.

and `:15` marks this as constitutive, *"not empirical assertions about real-world observation channels but scope-defining choices."* $\rho$ (Model D) and $\sigma_w$ (Model S) are properties of the disturbance process the agent sees only through $h$.

### 6.2 The sharp obstacle — and the strengthening it suggests

Both de-novo auditors found the same thing, and it is the strongest single argument in the file. Restated precisely:

- Structural persistence *guarantees* $\lVert\delta_t\rVert$ is ultimately bounded by $R^\ast = \rho/\alpha \lt R$.
- `#detail-operationalization`'s $R$-estimator requires the probability of sector-condition violation *conditional on $\lVert\delta\rVert \le r$* to be evaluated at radii $r$ approaching $R$ — i.e. it requires samples in $[R^\ast, R]$.
- A persistent agent, on-policy, produces no such samples. **The condition that makes the guarantee hold is the same condition that starves the estimate of the guarantee's margin.**

This is not merely "hard to estimate." It has the exact five-element shape of `#disc-identifiability-floor` (setting → external theorem → no-go → boundary characterisation → strengthened consequence), and it belongs to the *self-silencing* family that `spikes/spike-escape-standpoint-axis-2026-07-29.md` §8 names from the unprimed read: *"results where the repair-driving quantity vanishes **at** the failure state, forcing exogenous escapes."* Element 2 (an external theorem) is what a spike would have to supply; the obvious candidates are a support/coverage argument on the stationary distribution, or a Fisher-rank argument in the manner of Instance 2. **Caution, from the same spike's hard-won experience:** two prior attempts to anchor an M1 instance on Fano reached convergent negative verdicts (`spikes/.integrated/spike-4th-identifiability-floor-instance-2026-05-20.md` §3; `spikes/.integrated/spike-identifiability-floor-instance4-resolution-2026-05-18.md` §4). Do not reach for Fano first.

**Note the boundary characterisation writes itself, which is the sign the shape is right.** The escapes are exactly the accesses `#detail-operationalization` already quietly requires: exogenous perturbation channels (deliberate probing — pushing toward $R$ on purpose, which is what auditor 193847 named), breakdown observation (off-policy or historical data at large $\lVert\delta\rVert$), architectural knowledge of $R$ by construction, and exogenous measurement of environmental change. Four escapes, all already in the corpus, none currently recognised as escapes from a floor.

**And the escape structure explains the whole standpoint spread of §3 in one stroke:** Positions C, D, and E are each *an escape being exercised* — the analyst has exogenous channels, the ELI monitor has instruments outside the entity, the designer has architectural knowledge. They are consistent with each other and with the floor. Only Position B claims the quantity without an escape. That is a satisfying enough resolution that I want to flag the risk in it: it is *clean*, and clean resolutions of one's own investigation deserve suspicion. It is a hypothesis about a derivable floor, not a derived floor. Nobody has done the math.

### 6.3 The precedent that makes this a strengthening, not a softening

**The framework has already met this exact objection one level down and beaten it — by deriving, not by hedging.** `#emp-update-gain.md:50`, verbatim:

> **Resolving Epistemic Opacity.** The optimal gain equation requires the agent to know $U_o$, which seems to violate the epistemic opacity axiom established in `#def-observation-function` (the agent does not know the true noise distribution $\varepsilon_t$). This tension is resolved dynamically: the agent *estimates* $U_o$ (and $U_M$) from the observable statistics of its own mismatch sequence (innovations), treating the gain itself as an endogenous state variable. See `#deriv-adaptive-gain-dynamics` for the proof of how this meta-adaptation maintains Lyapunov stability without violating opacity.

The routing record for that cycle is a textbook strengthen-first outcome — `audits/audit-findings-849201.md:66`:

> **Strengthen-before-soften posture verification:** The audit FINAL's recommendation was a *softening* option-set ("a bridging hypothesis explaining how $U_o$ is empirically estimated… or a softening of the axiom"). The project's resolution is **strictly stronger**: rather than soften the axiom or pile on caveats, the project derived the resolution structurally — the gain is **itself an endogenous state variable** … The opacity axiom is preserved verbatim; the apparent contradiction with $\eta^\ast$ is resolved by adding a new exact result … rather than by weakening either side.

and the same record notes the finding arrived from **three architecturally-independent cold reads** (849201-F1, AUDIT-WORKING-742613 segment-02, extracted-gemini-2026-04-26-27) before the strengthening was built.

`#emp-update-gain.md:93` even carries the one-line gloss, which transfers to the reserve almost unchanged:

> - **"Be surprised by your surprises."** A one-line gloss for the endogenous-gain resolution: the agent estimates $U_o$ from the statistics of its own mismatch (innovation) sequence rather than being told it (Claude, AUDIT-WORKING-963715, 19–23 batch).

**Structural parallel, stated plainly.** $U_o$ : $\eta^\ast$ :: $(\alpha, R, \rho)$ : $\Delta\rho^\ast$. Same axiom violated, same apparent contradiction, same available resolution shape. The precedent tells you what the answer probably looks like — an endogenous, innovations-driven estimator with its own stability argument — and it also tells you what the honest tier is: the gain case earned a **dedicated derivation segment**, not a Discussion paragraph. A repair that is only a Discussion paragraph is under-delivering relative to the framework's own established standard for this exact objection.

**But the parallel is not free, and I want to be explicit that it may not close.** $U_M$ and $U_o$ are uncertainty statistics of the innovation sequence, and innovations are exactly what the agent has. $R$ is not: it is a radius the innovation sequence never reaches under the guarantee. So the transfer is plausible for $\rho$ (a drift statistic of the innovation stream), plausible-to-strained for $\alpha$ (see §8), and **prima facie blocked for $R$** by §6.2. **The most likely honest outcome is a split verdict** — a derivable endogenous estimate for two of three factors and an identifiability floor on the third — which would be a *better* result than either a clean yes or a clean no, because it locates the obstruction precisely and names the escape.

---

## 7. Repair options

Not mutually exclusive; A is a prerequisite for a clean version of any other. Each states its consequence.

### Option A — land the standpoint discipline (recommended, low risk, unblocks everything)

Introduce an explicit standpoint marker for the persistence parameters and apply it wherever $(\alpha, R, \rho, \Delta\rho^\ast)$ appear. Candidate homes, in preference order: a short subsection in `#result-persistence-condition` Discussion (where the reserve is introduced); or a `disc-` segment if the discipline is to cover the three other parked sites in §2 as well. Suggested grain — three markers, deliberately parallel to `#disc-continuity-stance`'s existing L1/L2/L3 carve so the two compose: **theory-side** (the certificate's existentially-quantified constants), **observer-side** (analyst / monitor / designer estimate, with the access it requires named), **agent-side** (a component of $X_t$, requiring an endogenous estimator).

*Consequence:* four of five positions become correct-and-marked with no content change. Position B becomes visibly unsupported, which is the point. Also discharges the two parked candidate-clarifications at `#def-observation-function:59, 63` and one at `#scope-adaptive-system:64` — one move, four debts, and it is the move three independent gold items already asked for.

*Cost:* a cross-segment marking sweep. Touches many segments lightly.

### Option B — spike the identifiability floor first (recommended as the substantive move; strengthen-before-soften requires it before any C or D)

Brief a spike on §6.2: *can an agent satisfying structural persistence identify $R$ — and hence $\Delta\rho^\ast$ — from its own on-policy trajectory?* Success, failure, and no-go are all publishable outcomes. Walk it against `#disc-identifiability-floor`'s five-element shape and its M1 distinctness tests (`spikes/.integrated/spike-identifiability-floor-instance-6-2026-05-21.md` is the correct four-test methodology for a *new instance*; note that spike-escape-standpoint-axis §8 records that the four-test check is the wrong instrument for a *new cluster*, so establish which is being proposed first).

*Consequence if it lands as a floor:* AAT gains a fifth M1 instance, on its own central inequality, with a ready-made escape menu, and Corollary 2(ii) is then repaired by *derived* fact rather than by softening. *Consequence if it fails:* the failure is itself the answer, and the escape analysis still supplies Option A's content.

*Sequencing:* do this **before** C or D. Per the project's strengthen-first discipline, a softening repair to Corollary 2(ii) is honest only after the strengthening attempt has honestly failed. Note the reverse-direction strengthening is also live and should be attempted in the same spike (below).

### Option C — derive the endogenous estimator (the strengthening; the §6.3 precedent's shape)

Attempt an innovations-based endogenous estimator $\widehat{\Delta\rho^\ast}_t$ as a state variable, with a stability argument, exactly as `#deriv-adaptive-gain-dynamics` did for the gain. Land it as its own derivation segment plus a "Resolving Epistemic Opacity"-style paragraph in `#result-persistence-condition`, mirroring `#emp-update-gain:50`.

*Consequence if it lands:* Corollary 2(ii) becomes *true and cited*, the terminology entry's "agents track the reserve" becomes correct, `#obs-growth-vs-drift` gains a real instrument, and the framework gains a second worked instance of a distinctive methodological move (endogenising a parameter the opacity axiom forbids knowing). This is the maximum-ambition outcome and it is not obviously out of reach for $\rho$ and possibly $\alpha$.

*Consequence if it partially lands (my expectation):* a split verdict — estimator for $\rho$, sub-scope-conditional for $\alpha$, floor on $R$. Then Corollary 2(ii) is repaired by naming which factor it actually needs (§7 Option E), and the floor lands under Option B.

*Prerequisite:* §8. Whether this is a fresh derivation or a corollary of existing machinery depends on the blocked file.

### Option D — repair Corollary 2(ii) at the weakest sufficient burden (the (U)-axis move; cheap, possibly sufficient on its own)

Ask what Corollary 1(ii) *actually* requires: *"agent-available per step without an oracle (escaping Lemma 2)."* Lemma 2's disqualification is a **global Bellman solve** — an intractable optimisation over a policy class. The bar to clear is "not a Bellman solve," not "exactly computable." Several strictly weaker objects may clear it:

- the **sign** of the reserve rather than its value;
- the **mismatch magnitude** $\lVert\delta_t\rVert$ against a known-by-construction $R$ (architecturally-known $R$ is exactly the escape `spike-escape-standpoint-axis-2026-07-29.md` §10 identifies as the case where the observability argument fails — here it works *for* the framework);
- the **state-space** form $R - R^\ast$ rather than the rate form (see §9.1 — and note this is the version that is nearly observable);
- a **conservative lower bound** on the reserve, which is all a safety-side terminal invariant needs. *"Do not adopt an $O_t'$ that pushes you outside the persistence region"* is satisfied by a conservative under-estimate; over-caution is safe here, and that asymmetry is a genuine gift the current phrasing throws away.

*Consequence:* Corollary 2 survives with a narrower and defensible (ii), possibly with no new mathematics. The claim gets *sharper* — "the terminal invariant needs only a conservative one-sided bound, which is why it escapes Lemma 2" is a better sentence than the one currently there.

*This is the option I would try to make work first if the spike in B/C is slow*, because it is the one where the current text is not merely unsupported but **imprecise about its own requirement** — and fixing that is pure gain regardless of how B and C come out.

### Option E — the minimum honest fallback (only if B, C, and D all fail)

Mark Corollary 2(ii) as conditional on an agent-side estimator, add it to the segment's Epistemic Status as a fourth named premise alongside the existing three, and correct the citation (which is wrong regardless of how the substantive question resolves — see §3.2(a)). Correct `terminology/entries/adaptive-reserve.md` via `bin/term decide` to drop or qualify the tracking clause.

*Consequence:* honest, and cheap, and it loses the constructive boundary's crispness. It is the softening; per project discipline it is available only after the strengthening attempts have honestly failed.

### The reverse strengthening, worth attempting inside Option B

Corollary 1 asks only that *some* object be convention-invariant, agent-available per step, and non-objective. If the reserve fails (ii), **is there another object on the adaptive substrate that succeeds?** Candidates visible from where I stand: the mismatch magnitude $\lVert\delta_t\rVert$ itself (indisputably agent-available — it is `#def-mismatch-signal`, the thing the agent's whole loop is built on); mood (`#def-mood`), which is explicitly *"a slow controller on the drain"* that *"widens the drain when recent overflow-risk has run high"* (`01-aat-core/src/def-mood.md:44`) — an existing, canonical, agent-internal, innovation-driven proxy for exactly the pressure the reserve measures; or the innovation statistics themselves. **If any of these satisfies (i)–(iii), the constructive boundary survives with a *better* instance than the reserve** — one that is unarguably in the agent's state. That outcome would be strictly stronger than the current text and should be attempted before anything is softened. `#def-mood` did not exist when Corollary 2 was written; the forward pointer at `#result-persistence-condition:202` connecting mood to the persistence condition is a later addition, and nobody has walked it back to Result G′.

---

## 8. Blocked read — flagging, not reading

**`01-aat-core/src/deriv-adaptive-gain-dynamics.md` has become load-bearing for this investigation. I have not read it. I am stopping and telling you, per the constraint.**

**Why it is load-bearing, argued only from files I did read:**

1. `#result-persistence-condition.md:79` states the bridge: *"#der-gain-sector-bridge shows that for agents with directional fidelity, $\alpha = \eta^\ast \cdot c_{\min}$ where $c_{\min}$ is the worst-case directional fidelity."* `#deriv-discrete-sector-condition.md:113` restates it in the fluid limit: *"$\nu(1 - \lambda_{\text{eff}}) \to \nu \cdot \eta^\ast c_{\min} = \alpha$."*
2. `#emp-update-gain.md:50` (quoted in full at §6.3) states that $\eta^\ast$ is endogenised — the agent estimates $U_o$ and $U_M$ from innovations, *"treating the gain itself as an endogenous state variable"* — and names `#deriv-adaptive-gain-dynamics` as the segment carrying **the proof**.
3. Therefore one of the three factors of $\Delta\rho^\ast$ is, per canon, already an agent-maintained endogenous state variable. Whether that reaches $\alpha$ (and how far) depends on the machinery in the blocked segment and on whether $c_{\min}$ and $\nu$ are similarly available.

**The precise questions to put to it if the gate is lifted** (framed so they can be answered without a general summary, minimising what a read reveals):

- **Q1.** Does its result concern $\eta^\ast$ / $(U_M, U_o)$ only, or does it reach $\alpha$ (i.e. does it compose with $c_{\min}$ and $\nu$)?
- **Q2.** Does its Lyapunov-stability argument for the meta-adaptation presuppose $(\alpha, R)$ as known constants? If so, the reserve cannot be derived from it without circularity, and that is decisive against Option C's cheap route.
- **Q3.** Does it establish any pattern — an "endogenise-the-parameter" template — that transfers to $\rho$ and $R$, or is it specific to uncertainty statistics of the innovation sequence?

**What is unaffected.** §6.2's obstacle is about $R$, and $R$ is a model-class capacity, not a gain. No result about gain dynamics can supply data at radii the agent never visits. So the identifiability core of this plan, Options A, B, D, and E, and every per-location finding in §3 stand independent of the blocked file. **Option C's scope is the only thing genuinely gated** — specifically, whether it is a fresh derivation or a corollary, and whether it reaches two factors or one.

**Recommendation:** do not lift the gate for this plan. Lift it (or have the prediction-holder score and publish first) before briefing Option C, and brief that spike with Q1–Q3 rather than an open read.

---

## 9. Secondary findings surfaced en route

### 9.1 A units conflation that is quietly load-bearing on this exact axis

The gold at `01-aat-core/src/result-sector-condition-stability.md:88` flags it as a nit:

> - **Units of adaptive reserve.** $\Delta\rho^\ast = \alpha R - \rho$ has units of *rate* (drift/time); a downstream segment discussing reserve as a *state-space distance* should use $R - R^\ast$ instead — a reader-orientation note worth a parenthetical (Gemini, AUDIT-WORKING-773921).

**It is more than a reader-orientation note.** The conflation is committed in the wild, twice, in the project's own comprehension instruments — `msc/quiz-responses/quiz-34.answers.md:33` and `msc/quiz-responses/quiz-40.answers.md:63`, both answering `05-batch-tempo-sector-quiz-questions.md` Q b05-3.6:

> **Adaptive reserve (b05)**: $\Delta\rho^\ast = \alpha R - \rho$ is nearly exhausted when mismatch rides near $R$ — the agent is fragile …

The rate reserve $\alpha R - \rho$ is not a function of where mismatch currently sits; the state distance $R - \lVert\delta_t\rVert$ is. **Why this matters here:** the state-distance version is *nearly agent-observable* — $\lVert\delta_t\rVert$ is `#def-mismatch-signal`, the one quantity the agent indisputably has — while the rate version needs all three parameters. The conflation therefore makes Position B feel obviously true when the thing that is nearly true is a different quantity. It is a lubricant for the error, not a separate nit, and the repair should fix both together. It also makes Option D's third bullet more attractive than it first appears.

### 9.2 Build-snapshot staleness (adjacent, not this investigation's)

`CURRENT-VOL1.md:1761` reads *"the agent persists **if and only if** $\alpha \gt \rho/R$"*, while current `01-aat-core/src/result-sector-condition-stability.md:17` carries the post-Lemma-A.1N wording (*"$\alpha \gt \rho/R$ guarantees the agent persists … tight at class level … for a general fixed corrector, failure of the inequality means the containment guarantee is lost, not that escape is certified"*). The root monograph snapshot predates the correction. Flagging only; out of scope, and `CLAUDE.md` already marks `CURRENT-VOL1.md` as a build snapshot.

### 9.3 A stale line reference in a routing record

`audits/audit-findings-849201.md:66` cites the "Resolving Epistemic Opacity" paragraph as `emp-update-gain.md:44`; it is currently at `:50`. Harmless; noted so the auditor of this plan does not think I mis-transcribed.

### 9.4 Two 193847 dispositions that appear never to have landed

`audits/audit-findings-193847.md:145` dispositions Theme F5 as *"**`architectural` → PROPOSALS candidate** for `04-eli-core/src/norm-adaptive-reserve-as-ethical-floor.md`"* and `:151` dispositions Theme F6 as a PROPOSALS candidate for *"a `disc-ib-vs-structural-reserve` segment."* Grepping `PROPOSALS.md`, `TODO.md`, `audits/STATUS.md`, and `04-eli-core/` for `norm-adaptive-reserve`, `ethical-floor`, and `ib-vs-structural-reserve` returns nothing. Both concern the reserve, so whoever executes this plan will be in the neighbourhood; worth 10 minutes of confirmation rather than my assertion.

### 9.5 A process recommendation

Per §3.6: add to the gold-lift procedure (`routing.sop.md` §8 / `doc/de-novo-audit-instructions.md` §7.15) a check that a "readers often ask / wonder" item is not *answered as a premise* somewhere else in canon. When it is, it is a cross-segment consistency finding and belongs on the certified track. This is the generalisable lesson of the whole episode and is cheaper than any of §7.

---

## 10. Verification ledger

**Read first-hand, in full:** `#result-persistence-condition`, `#deriv-self-actuation-grounding`, `#detail-operationalization`, `#disc-identifiability-floor`, `#der-agent-opacity`, `04-eli-core/src/obs-growth-vs-drift`, `terminology/entries/adaptive-reserve` + `operational-persistence`, `CLAUDE.md`, `audits/STATUS.md`, `spikes/spike-escape-standpoint-axis-2026-07-29.md` §4–§11, `msc/nogo-unification-archaeology-2026-07-29.md` §2–§5.

**Read in relevant part, with every quoted line re-verified against the file after an interruption in this session:** `#deriv-sector-condition`, `#result-sector-condition-stability`, `#result-sector-persistence-template`, `#form-sector-condition`, `#der-orient-cascade`, `#disc-continuity-stance`, `#emp-update-gain`, `#def-observation-function`, `#scope-adaptive-system`, `#form-complete-agent-state`, `#der-multi-timescale-stability`, `#der-adversarial-destabilization`, `#deriv-discrete-sector-condition`, `#deriv-gain-sector`, `#example-kalman`, `#der-interaction-channel-classification`, `#form-resource-budget`, `#def-mood`, `#der-mood-timescale`, `_obs/old-tf-appendix-a-lyapunov`, `_obs/old-tf-11-tempo-persistence`, `_obs/old-tf-00-notation-conventions`, `spike-wf-class-scoping`, `spike-continuity-orthogonality-2026-05-30`, `AUDIT-WORKING-{193847,829314,849201}` reserve reflections, `audits/audit-findings-849201.md` §F1, `doc/de-novo-audit-instructions.md` §4.4/§7.15.

**Searched systematically, negative results reported as such:** every `audits/audit-findings-*.md`, `audits/pending-findings-*.md`, `TODO.md`, `PROPOSALS.md`, `FINDINGS.md`, `CHANGELOG.md`, `LOG.md` for a routed finding on reserve measurability — **none found**. `LEXICON.md` and `CURRENT-VOL1.md` for the "agents track the reserve" clause — **absent from both**. `02-tst-core/` and `03-llm-core/` for substantive reserve use — **none** beyond one legacy mention at `old-tst-via-tft-simulation-proposals.md:13`.

**Explicitly not done:**
- `01-aat-core/src/deriv-adaptive-gain-dynamics.md` — not opened (§8).
- Exhaustive reading of all 21+ `AUDIT-WORKING-*` dirs; I grepped all of them and read the hits. The 849201 attribution gap (§3.6) is "not found," not "not there."
- The self-model sweep (§6.1, Obstacle 1) covered four foundational segments, not the full corpus.
- No prior-art search outside the repo.
- No mathematics attempted. §6.2 is a hypothesis about a derivable floor, not a derivation.
- Nothing in `audits/` reorganised, moved, or processed; the `AUDIT-WORKING-*` gate was observed.

**One transcription normalisation, disclosed.** Three quoted passages (`README.md:103` / `README-auditor.md:124`, and `AUDIT-WORKING-829314/.integrated/22-…:17`) write the reserve as `\Delta\rho^*` in the source; they are reproduced here as `\Delta\rho^\ast` so this file passes `bin/lint-md`'s bare-`*`-in-inline-math rule. Renders identically; no other character was altered in any quotation in this file.

**One unavoidable leak, disclosed.** An early repo-wide grep for `adaptive reserve` / `Delta\rho` ranged over `01-aat-core/src/*.md`, and `deriv-adaptive-gain-dynamics.md` did not appear in the results. So I know that file contains neither string. I did not open it and did not grep it again once I understood the constraint's shape. If the prediction being scored touches whether that segment mentions the adaptive reserve, this leak is material and the prediction-holder should be told.

---

## 11. Suggested order

1. **Option D's re-reading of Corollary 1(ii)** — cheapest, and it clarifies what the rest of the work has to deliver. May resolve the load-bearing site on its own.
2. **Option A, standpoint discipline** — unblocks clean statements everywhere and discharges three other parked gold items.
3. **Option B/C as one spike**, briefed with §6.2, the §6.3 precedent, the reverse-strengthening candidates from §7, and the §8 questions held back pending the gate. Genuinely open outcome: derived estimator, identifiability floor, or split verdict.
4. **Option E only after 3 returns**, and only if it returns a failure.
5. **§9.1 units repair** alongside whichever of the above touches `#result-sector-condition-stability`.
6. **§9.5 process note** — independent of all the above, and the cheapest durable win in the file.

Throughout: the reserve's *mathematics* is untouched and correct, unchanged since TFT. Nothing here questions Prop A.2. What is in question is who holds the number.
