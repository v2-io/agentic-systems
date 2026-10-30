# Drain, fork A: the operator-layer and April–May spikes

*Serves G.2 (stranded additions landed or set aside) and C.1 (verified defects replaced) of `../INTENT.md`. Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." Fork A of the spike drain, 2026-10-30, at asf `cbd2f345`. Its parent file is `spikes.md`. Canon was not edited; the ledger edits are listed at the end.*

## What I read

- **Read whole:** `spike-update-operator-sector.md`, `spike-passivity-composition.md`, `spike-pid-a2prime.md`, `spike-alignment-impossibility.md`, `spike-transient-dependency-amplification.md`, `spike-aporia-sub-agent-adversarial.md`.
- **Read in large part:** `spike-rho-additive-variance-strengthening-2026-04-24.md` §§1–6 (§7 onward not read: dead ends and summary). `spike-bridge-lemma-nonlinear-strengthening-2026-04-24.md` §§0–7 (§§8–12 not read: tier table, summary, references). `spike-neutral-drift-endogenous-coupling-strengthening-2026-04-24.md` §0, §1, §3.4–3.5, §§8–11 (§§2, 4–7 not read beyond headings).
- **Sampled:** `spike-composition-scaling-N.md` (§1, §§8–11, headings). `spike-kl-to-state-distance-template-extraction-2026-04-24.md` (headline, outline, client survey via grep).
- **Checked against HEAD for every disposition:** the canon segments named below, grepped and read at the cited lines; pickaxe over `0*/src/*` where a spike's form might once have entered canon. Adjacent surfaces were searched for each claim: audits, Working Notes, `msc/inside-out-2026-10/` including `influx-scout/` and `internal-surfaces/`. No `memorata-search` was run.

## Dispositions, one per spike

| Spike | Disposition | Where it lives now |
|---|---|---|
| `spike-update-operator-sector.md` | **Set aside: its headline is false.** Recommend `.archived/`. | Finding appended to `item:todo-spike-update-operator-sector-orphan-regr-b62b` (G.2), with the recommendation to close it as superseded once a second mind confirms. |
| `spike-passivity-composition.md` | **Stranded, with defects to fix before landing.** It is part of CL-1. | `item:todo-spike-bridge-lemma-nonlinear-strengtheni-a707` (G.2), now the single open CL-1 item. |
| `spike-pid-a2prime.md` | **Canon defect still present** (`#der-gain-sector-bridge:76`). Part of CL-1. | Same item. The existing question `question:is-the-spr-tuned-pid-row-of-der-gain-sector-brid` was annotated. |
| `spike-bridge-lemma-nonlinear-strengthening-2026-04-24.md` | §7.1 **already in canon**. §7.2 is CL-1. §7.3 **set aside**. The §6 residuals are subsumed. | Same item. Recommend `.integrated/` when CL-1 lands. |
| `spike-rho-additive-variance-strengthening-2026-04-24.md` | **Correctly superseded** by `#deriv-mismatch-budget-attribution`. One piece exposes a **canon defect**. | New `item:internal-external-decomposition-59-states-the-co` (C.1). Finding appended to `item:rho-additive-variance-remainder-stranded` (G.2). Recommend `.archived/`. |
| `spike-neutral-drift-endogenous-coupling-strengthening-2026-04-24.md` | **Mostly in canon.** Two small scope sentences are left. One proposal is set aside. | Appended to `item:neutral-drift-spike-remainder-stranded` (G.2). Recommend `.integrated/`. |
| `spike-kl-to-state-distance-template-extraction-2026-04-24.md` | **Set aside.** Its own gating rule fired. | No open item; both ledger items for it were closed today. Recommend `.archived/`. |
| `spike-alignment-impossibility.md` | Core **already in canon**. §7 **set aside**. | No item. Recommend `.integrated/`. |
| `spike-composition-scaling-N.md` | Framing **already in canon**. One derivation remains open. | Appended to `item:todo-composition-scaling-with-n-whether-closu-b10f` (C.1). Recommend `.integrated/`. |
| `spike-transient-dependency-amplification.md` | **True and never in canon**, at conditional tier. | Appended to `item:todo-transient-dependency-amplification-spike-441c` (G.2). The research continuation is `item:spikes-proposed-advanced-3-transient-dependency-amplification-and-a826`. Stays live until landed. |
| `spike-aporia-sub-agent-adversarial.md` | **Brainstorm, held.** | Appended to `item:proposals-sp-18-internal-aporia` (unassigned). Stays live. |

## The findings that matter

### The update-operator spike's headline is false

`ROUTING` and `item:…b62b` carried this spike as a regression-cleared orphan with a "tractable landing pending": $\alpha$-op refresh into `#deriv-sector-condition`, operator-layer no-go into `#disc-identifiability-floor`. Landing it would have put a false claim into canon.

Its condition (O-A2′) asks for a positive sector constant on the vector of edge log-odds, driven by one plan-level Bernoulli outcome $y_G$. The expected update moves every edge along the single direction $\mathbf J$, so the fixed points form the level set $\{\hat P_\Sigma = \Phi\}$. That is a manifold of dimension $\lvert E\rvert - 1$, and the spike's own §1.2 says as much. No contraction to a point $\boldsymbol\lambda^\ast$ exists once $\lvert E\rvert \ge 2$.

The algebra fails at §2.2:

- $(\boldsymbol a^\top \boldsymbol e)(\boldsymbol b^\top \boldsymbol e)$ is a rank-two quadratic form.
- $\tfrac12(\boldsymbol a\boldsymbol b^\top + \boldsymbol b\boldsymbol a^\top)$ has eigenvalues $\tfrac12(\boldsymbol a\cdot\boldsymbol b \pm \lVert\boldsymbol a\rVert\lVert\boldsymbol b\rVert)$, so its least eigenvalue is at most $0$. Case 2's "PSD iff $\boldsymbol a\cdot\boldsymbol b \ge 0$" is wrong.
- Case 1's componentwise inequality fails on any $\boldsymbol e \perp \boldsymbol a$.

A two-edge AND simulation with $\theta = (0.8, 0.6)$ converged to points on $p_1 p_2 = 0.48$ that were fixed by the initial credences, not to $\theta$. The script is a scratch file and is not in the repo.

What is true here is already canon:

- persistence transfers only to the plan-level error $\delta_s$ (Prop B.5, cited at `#disc-credit-assignment-boundary:20`, `:75`);
- per-edge attribution is underdetermined when there are fewer observable nodes than edges (barrier (b), `:101–105`, and the F60 note at `:207`).

The §4.3 operator-layer Cramér–Rao break is the same rank statement. An exact pickaxe for `alpha_{\text{op}}`, `O-A2` and `O-DA.1` over `0*/src/*` is empty, so the claim never entered canon and nothing needs retracting. For the record, the 2026-05-17 pilot cleared this spike on the regression axis only. Nobody re-derived it.

### CL-1, the dissipativity template: five things the integrator should know

All five are on `item:…a707`. CL-1 had three open ledger items that were the same work. `item:…86c0` had already been closed by the p-process rechecker. I closed `item:proposals-d-9-sp-22-operator-family-tier-2-backlog-0b44` as a duplicate of `a707`; `spikes/INDEX.md:8` still names `d-9`, and the duplicate link resolves.

1. **Old class numbering.** passivity-composition §6 and bridge-lemma §2.5 call Class 2 "fully merged (LLM)" and Class 3 "partially modular". That is the pre-2026-05-09 numbering; in current canon Class 2 is Partial and Class 3 is Coupled. The "port-structure ladder" must be translated before it lands, or it will say the opposite of canon.
2. **PID passivity is misstated.** The spikes say PID is passive "iff plant positive-real". A filtered PID with nonnegative gains is itself positive-real: $\operatorname{Re} C(j\omega) = K_P + K_D\omega^2/\omega_d\,/(1+\omega^2/\omega_d^2) \ge 0$, and the integrator pole has positive residue. So it is passive whatever the plant. The relevant theorem concerns a passive controller in feedback with a (strictly) passive plant. The spike's $S_{\text{PID}}$ and $\alpha_{\text{PID}} = \gamma_p K_P/(K_P + K_D\gamma_p)$ are asserted, not derived.
3. **The Kalman-plus-PID worked example uses the wrong mechanism.** Under the separation principle, the estimation error does not depend on the control. Kalman → PID → plant is therefore a cascade: $e_K$ enters the control loop as an input. The spike instead treats it as a negative-feedback loop whose cross-terms cancel. The conclusion plausibly holds as a cascade of input-to-state-stable systems, but the derivation in §4.2–4.3 does not go through as written.
4. **The $\alpha_{\text{PID}}$ row at `#der-gain-sector-bridge:76` is a canon defect.** It is tagged Derived, but no derivation exists, and it contradicts `:108`, which places PID in sub-scope $\beta$. Under `#result-certificate-existence`, every exponentially stable linear PID loop is in sub-scope $\alpha$ in some $P$-norm, so no SPR condition is needed for membership. The open content is only the size of the constant. This agrees with the t2-todo rechecker's own algebra in the question file.
5. **A category question that may decide the landing's shape.** PID's mismatch is tracking error against a setpoint, which is goal-referenced. B1 is a property of the epistemic update. `influx-scout/rewrites-aux-canon-check.md:149` flags the same tension independently. Adjacent material: the Working Note at `#deriv-sector-condition:453` (audit 193847) says it is the integral state that breaks the memoryless sector.

What remains of the bridge-lemma spike:

- §7.1 is canon: `#form-composition-closure:228`, `#result-contraction-template:146–150`, `#form-sector-condition:100`.
- §7.3, the iISS global lift, is set aside. Its proof sketch moves from the local Theorem 2 to a global claim without an argument, and the region-free case is already `#result-contraction-template` with (M0) holding everywhere.
- §6 R6 is subsumed by `#disc-stability-certificate`.
- §6 R-new is subsumed by the $\dot M$ term already in (CT2).

### The multiplicative no-go in `#internal-external-decomposition` is stated more strongly than it is proved

This came out of dispositioning the $\rho$ spike, and it is the one new canon defect in my part. `:59` states as exact that no agent-independent $\rho_{\text{external}}$ satisfies $\rho = \rho_{\text{external}}\, f(\mathcal M)\, g(\pi)$. The reason it gives is "a contribution that subtracts to zero cannot be represented by attenuating a fixed scalar". That does not prove the claim, because a model factor can shrink too.

**Exceptions where the product exists exactly:**

- a policy-invariant budget (canon's own `#deriv-mismatch-budget-attribution` Cor 1b, with $g \equiv 1$);
- the spike's §3.1 rare-event regime of independent Poisson thinning with no channel floor.

**The exact obstruction is non-separability.** A positive $\rho(\mathcal M, \pi)$ factors iff $\log\rho$ is additively separable. On canon's own worked anchor (misspecified drift with a regulating policy) it is not: $\rho^2 = F + k(\mathcal M)\,m(\pi)$ with floor $F \gt 0$, and $\partial^2_{bc}\log(F + bc) = F/(F+bc)^2 \neq 0$.

The strengthen-first move is to state the separability criterion as the no-go, show generic failure on that anchor, and name the exceptions as the scope boundary. Recorded as `item:internal-external-decomposition-59-states-the-co` (C.1). No second mind has checked it.

### The $\rho$ additive-variance spike is superseded, not stranded

Two G.2 items called its payload stranded; one of them was already closed. **(AV) should not land, and re-landing it would be a regression.** As the spike defines them, $\rho_\star^2 + \Delta^2_{\mathcal M} + \Delta^2_\pi$ already telescopes to $\rho^2$, so the extra $2\chi$ double-counts. Canon's corrected form says the policy is the measure, "not a fourth term".

The rest of the spike:

| Section | Disposition |
|---|---|
| §4.1 no-go | Rests on a false premise: the Bayes innovation variance depends on process and observation noise separately, not only on their sum. Its conclusion is canon by another route. |
| §3.2 tail regime | Needs the independence that canon's Prop 1 denies in general. Set aside. |
| §3.3 PID-$\rho$ | Refines a cross term canon shows does not exist. Set aside. |
| §3.4 multiplicative noise | A coordinate remark. Set aside. |
| §3.1 cascade | Survives only as the counterexample now carried by the C.1 item. |

## Smaller dispositions, with reasons

**Neutral drift.** What is already canon:

- §10.1 is `#der-architecture-noidentifiability`.
- §10.3 is escape (b) at `#disc-identifiability-floor:116`.
- §11.4 is resolved by `#disc-implementation-impossibility`.

What is left:

- §10.2: an optional sentence; `#der-agent-opacity` is filtration-indexed by construction.
- §10.5: one population-layer scope sentence in `#scope-agent-identity`.
- §10.4, the $\gamma$-from-cross-covariance estimator, is set aside. The (C1) coupling is in disturbance amplitude, $\rho^{\text{eff}} = \rho + \gamma\mathcal T_j$, not linear in $\delta$, so the A.2 Lyapunov formula does not follow, and the spike's own A.3 names the common-driver confound.
- §11.2 (endogenous $\gamma$ dynamics) is open research.

**KL-to-state template.** This is an extraction proposal, not mathematics. `item:proposals-e-2-sp-10-…` was closed today as stale under its own rule (no third client in six months). The template is the $W_2$ Otto–Villani cascade. The internal-surfaces map guessed that the $\varepsilon$-programme's Lemma E4 might be a client, but E4 is a TV/Pinsker route, the adjacent family the spike excluded from the template. No new client.

**Alignment impossibility.** Gibbard–Satterthwaite, Myerson–Satterthwaite and Arrow are canon in `#disc-implementation-impossibility`, with `#deriv-strategy-proofness-impossibility`. The §7 claims are set aside:

- "VCG gives perfect strategy-proof alignment" ignores budget balance (Myerson–Satterthwaite).
- "a native token economy is required for safety" does not follow.
- canon already places VCG-with-deficit outside its machinery (`:74`, `:113`).

The §3 "deception is mathematically inevitable" is the overclaim that the spike's own §4 already softens. The rechecker reached the same set-aside for `PROPOSED-ADVANCED #4`.

**Composition scaling with $N$.** A scoping spike with no derived content. Its framing is in `#form-composition-closure:185`/`:358`. The open case-(II) derivation is `item:…b10f`.

**Transient dependency amplification.** I re-checked the exact-tier claims and they hold:

- Lemma 1;
- Proposition 1, $\lVert G_d\rVert = (\lvert g\rvert\sqrt B)^d$;
- Lemma 2;
- $\lVert P_{\eta,r}G\rVert = \max(\eta\sigma_1, \sigma_{r+1})$.

§6's "Fisher metric is forced" overreaches: (PI) plus Čencov forces the metric on statistical manifolds, and the task-local $z$-space is not shown to be one. Land that as a recommendation. The only canon pointer to the spike is a Working Note (`#hyp-exponential-cognitive-load:92`).

**Aporia.** Brainstorm-grade. Canon already explains its motivating institutions by a different mechanism: defensive scaffolding as Class-1-from-Class-3 composition (`#disc-adversarial-coupling-pressure:82`). A spike should first ask what "aporia amplifier" predicts beyond that.

## Coupled to siblings' spikes

- CL-1's port-structure reading touches `#der-directed-separation`, which fork C's leakage-locus and strategic-self-coupling spikes also target. An integrator landing CL-1 should translate the class numbering in the same pass.
- The rechecker filed `spike-c2prime-realization-spectrum-2026-05-31.md` (fork C) under C.1 for `#def-auxilia-hierarchy`. Not mine; noted only because the CL-1 port reading and (C2′) both concern wrapper boundaries.

## Ledger edits made (uncommitted; for the parent to commit by path)

- New: `items/internal-external-decomposition-59-states-the-co.md` (C.1).
- Closed as duplicate: `item:proposals-d-9-sp-22-operator-family-tier-2-backlog-0b44` → `a707`. Its event is under `.vsect/events/item/proposals-d-9-…/`, and the item file changed.
- Appended "Source added" paragraphs to:
  - `items/todo-spike-update-operator-sector-orphan-regr-b62b.md`
  - `items/todo-spike-bridge-lemma-nonlinear-strengtheni-a707.md`
  - `items/rho-additive-variance-remainder-stranded.md`
  - `items/neutral-drift-spike-remainder-stranded.md`
  - `items/todo-transient-dependency-amplification-spike-441c.md`
  - `items/proposals-sp-18-internal-aporia.md`
  - `items/todo-composition-scaling-with-n-whether-closu-b10f.md`
  - `questions/is-the-spr-tuned-pid-row-of-der-gain-sector-brid.md`

No spike was moved: the `git mv` to `.integrated/`/`.archived/` is the parent's call, and two of the recommendations want a second mind first.
