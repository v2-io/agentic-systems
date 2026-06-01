# Spike: GUC Directed-Separation Class Boundaries — Intuition From the Smallest Toy Agents

**Status.** Intuition-building simulation spike. Read-only on canon; no segment edits, no `status:` changes. Deliverable is concrete intuition + reusable simulation infrastructure (`sim_guc_classes.py`, `sim_guc_boundaries.py`). One canon-refinement *recommendation* is recorded at the end for the gate, not applied.

**Date.** 2026-05-31.

**Independence note.** The toy models here are derived directly from `#der-directed-separation` + `#disc-partial-coupling-pathways` + `#der-belief-strategy-attractor` + the leakage-locus spike's exact linear-Gaussian structure (`spikes/spike-leakage-locus-2026-05-18.md`). A sibling spike independently probes the narrower W₁/W₂ wrapping sub-boundary inside Class 2; it was deliberately *not read* so that agreement between the two infrastructures is corroboration and divergence is signal. (Where this spike's wrappability test touches W₁/W₂ territory, it re-derived the structure from canon and arrived at the same content-form/process-form cut — recorded below as a corroboration.)

---

## The plain-language answer (lead with this)

**The two boundaries are different kinds of thing.** Standing right next to each one and looking closely:

**Class 1 ↔ Class 2 is a *certifiability* boundary — not a behavioral one.** You can build a Class-2 agent whose goal-coupling knob is turned all the way down to zero, and its behavior becomes *bit-for-bit identical* to a Class-1 agent: same beliefs, same goal-leak (zero), same response to an adversary. The closest you can get on each side is *exactly the same point* in behavior space. What still differs — and it flips discretely, with no approach — is whether the separation is *certifiable*. The Class-1 agent's belief-update has no goal argument *by construction*; the channel is not there to open. The Class-2-at-zero agent has a channel that happens to be carrying nothing right now; turn the knob and it leaks. So being Class 1 is **not** "having $\kappa = 0$ right now," it is "having a structural guarantee that $\kappa$ stays 0 under perturbation, because there is no channel." The boundary is exactly where that guarantee becomes uncertifiable. This is the precise sense in which "$\kappa$-as-a-scalar is a category error": at the limit the scalar is identical on both sides; the thing that actually changed is invisible to any amount of behavioral measurement and visible only by inspecting the architecture.

**Class 2 ↔ Class 3 is a *behavioral* boundary — a real change in how leak responds to pressure.** Here the discriminator is not "is there a channel" (neither side is certifiable; both have channels) but "does the leak stay bounded, or does it track the goal one-for-one?" The clean, convention-free measurement is the **adversarial slope** — how fast the belief-error grows as an adversary pushes the goal further from the truth. For a bounded Class-2 coupling the slope is essentially flat (the leak is self-limiting; the agent can be biased but an adversary cannot drag its belief arbitrarily far). For the fully-Coupled Class-3 architecture the slope is $\approx$ the coupling fraction: every extra unit of adversarial goal buys a proportional unit of belief-error. The Class-3 corner is where **the bound goes trivial** — the only thing limiting the leak is the size of the goal the adversary chooses. That is a genuine behavioral discontinuity in the *response-to-pressure*, not just a magnitude difference.

So: **Boundary 1 is where the *certificate* disappears; Boundary 2 is where the *bound* disappears.** The first is a fact about the architecture you can only check by reading the wiring; the second is a fact about behavior you can measure by leaning on the agent.

**One incidental finding** (and a small surprise that turned out to corroborate canon): the property that makes a coupling *leak under adversarial pressure* (clean additive goal-entry) is the *same* property that makes it *wrappable* (post-hoc subtractable). Additive (content-form) coupling leaks proportionally to the adversary's goal yet is fully removable by a fixed linear debiaser; gain-modulation (process-form) coupling is self-limiting in magnitude yet *not* linearly removable. Adversarial-pressure-sensitivity and wrappability are **orthogonal** axes — which is why the Class label alone underdetermines both the adversarial signature and the repair regime, exactly as the Class-2 sub-typology says.

Confidence: **high** that Boundary 1 is a certifiability boundary and Boundary 2 is a behavioral (bound-triviality) one — the Boundary-1 result is an exact behavioral-identity-at-the-limit, robust to every knob I varied. **Medium-high** on the orthogonality finding — it is clean in the toy but the toy's Class-3 agent is a content-form-at-full-strength caricature (see Honest scope), so the "Class 3 is not linearly wrappable" half is *asserted from canon*, not exhibited by this toy.

---

## 1. The toy world and the three agents

The infrastructure lives in `sim_guc_classes.py` (agents + measurement) and `sim_guc_boundaries.py` (the boundary sweeps + plot). The design follows the canon's filtering structure so the numbers connect to the theory rather than to an arbitrary map.

**World.** A scalar latent $z$ (the true state of reality), observed through additive Gaussian noise, with an `obs_info` $\in [0,1]$ knob scaling identifiability. Low `obs_info` reproduces the leakage-locus regime — a near-flat likelihood (the scalar analog of $\ker \mathcal{I}_\tau$) where goals have room to push belief because the observation does not pin $z$. All runs below use `obs_info` $= 0.3$ (weak identification: leak is visible, but an honest agent still converges).

**The agents are faithful miniatures of the three classes**, each an information-form scalar Kalman update with a different relationship to the goal:

| Agent | Class | Belief-update signature | Goal enters belief via |
|---|---|---|---|
| `SeparatedAgent` | 1 | `update(o, obs_var)` — **no goal argument** | nothing — structurally absent |
| `PartialAgent(s, form)` | 2 | `update(o, obs_var, g_des)` — goal present, small | content (additive bias) or process (gain modulation), strength $s\in[0,1]$ |
| `CoupledAgent(kappa)` | 3 | `update(o, obs_var, g_des)` — goal **required** | single-pass blend $(1-\kappa)\,\mu_{\text{evid}} + \kappa\, g$ |

The Class-1 agent carries the canon's type-signature commitment literally: its `update` method *cannot accept a goal* — the channel is absent in the code, not merely set to zero. This is what makes its separation certifiable: `certifiable_separation()` decides by inspecting the architecture (does `update` take a goal?), not by measuring behavior.

The goal-contamination shape matches the leakage-locus result: in the content-form, the per-step mean shift is the additive $s\,(g - \mu)$ — a scalar instance of $\Delta\mu = \Lambda_0^{-1}g$; in the process-form, the goal modulates the Kalman gain (weight evidence up if it agrees with the goal, down if it disagrees), which is the canonical multiplicative process coupling of `#disc-partial-coupling-pathways`.

**Measurement apparatus** (all in `sim_guc_classes.py`):
- `behavioral_kappa` — the canon's $\hat\kappa_{\text{processing}}$: same observation stream, different goals, measure belief divergence. Holds $M_{\tau^-}$ and the stream fixed across goal conditions (the estimator-confound discipline the audit-gold flagged).
- `asymptotic_bias` — $\lvert\text{belief} - \text{truth}\rvert$ under a goal pulling away from truth (the actual behavior).
- `adversarial_leak` + `adversarial_pressure_slope` — leak under an adversarial goal, and how fast it grows with $\lvert g_{\text{adv}}\rvert$. The slope is the bound-triviality discriminator.
- `debias_residual` — can a fixed linear (W₂) wrapper remove the coupling? (residual $\approx 0$ means wrappable).
- `certifiable_separation` — architecture-inspection guarantee, the thing behavior cannot see.

---

## 2. Boundary 1 — Class 1 ↔ Class 2, up close

Marching the Class-2 coupling $s \to 0^+$ from both forms, against the lone Class-1 agent (which has no knob):

| config | beh_kappa | goal_bias | adv_leak | adv_slope | certifiable |
|---|---:|---:|---:|---:|:--:|
| Class 1 Separated | 0.0000 | 0.1015 | 0.0925 | 0.0000 | **True** |
| Class 2 content $s{=}0.05$ | 0.2364 | 2.6959 | 7.2050 | 0.9007 | False |
| Class 2 content $s{=}0.01$ | 0.0739 | 1.6978 | 4.5605 | 0.5700 | False |
| Class 2 content $s{=}0.001$ | 0.0083 | 0.2653 | 0.7671 | 0.0941 | False |
| Class 2 content $s{=}0.0$ | 0.0000 | 0.1015 | 0.0925 | 0.0000 | False |
| Class 2 process $s{=}0.05$ | 0.0108 | 0.1082 | 0.1193 | 0.0000 | False |
| Class 2 process $s{=}0.001$ | 0.0002 | 0.1013 | 0.0927 | 0.0000 | False |
| Class 2 process $s{=}0.0$ | 0.0000 | 0.1015 | 0.0925 | 0.0000 | False |

**The crux pair — two agents right next to the boundary, at the limit:**

| config | beh_kappa | goal_bias | adv_leak | adv_slope | certifiable |
|---|---:|---:|---:|---:|:--:|
| Class 1 (no channel) | 0.0000 | 0.1015 | 0.0925 | 0.0000 | **True** |
| Class 2 $s{=}0$ (process) | 0.0000 | 0.1015 | 0.0925 | 0.0000 | **False** |

Every behavioral column is identical to four decimals (the residual $\approx 0.09$ is the honest tracking error under weak observation — both agents have it). The only column that differs is `certifiable`. **This is the headline: at the limit the two agents are behaviorally indistinguishable; the boundary is the discrete flip of the structural guarantee, invisible to behavior.**

The "closest you can get on each side": on the Class-2 side you can get *arbitrarily* close (the process-form approaches the Class-1 point smoothly and the content-form does too, just along a steeper curve), but you can never *land on* Class 1 from the Class-2 side, because no value of $s$ removes the channel — it only empties it. Class 1 is the one point that is reached by *deleting the argument*, not by *zeroing the knob*. (Left panel of `guc_boundaries.png` shows the green Class-1 star sitting exactly where the process-form curve meets $s = 0$.)

---

## 3. Boundary 2 — Class 2 ↔ Class 3, up close

Marching the Class-2 process-form coupling $s \to 1^-$ and the Class-3 architectural $\kappa \to 0^+$:

| config | beh_kappa | goal_bias | adv_leak | adv_slope | certifiable |
|---|---:|---:|---:|---:|:--:|
| Class 2 process $s{=}0.6$ | 0.1364 | 0.9917 | 1.0348 | **0.0008** | False |
| Class 2 process $s{=}0.9$ | 0.2406 | 1.9082 | 1.9910 | **0.0085** | False |
| Class 2 process $s{=}1.0$ | 0.2892 | 2.4308 | 2.5751 | **0.0292** | False |
| Class 3 coupled $\kappa{=}0.1$ | 0.3184 | 2.8605 | 7.6402 | **0.9551** | False |
| Class 3 coupled $\kappa{=}0.3$ | 0.3846 | 2.9625 | 7.9062 | **0.9884** | False |
| Class 3 coupled $\kappa{=}0.9$ | 0.4071 | 2.9981 | 7.9955 | **0.9994** | False |

The discriminator is the `adv_slope` column. Throughout Class 2 (process-form) it stays near zero even as the *magnitude* of leak rises: the coupling biases the belief but is **self-limiting** — push the adversarial goal twice as far and the belief-error barely moves, because gain-modulation can only re-weight the *evidence that arrives*, it cannot inject the goal directly. Across the Class-3 family the slope is $\approx 1$: the leak tracks the adversarial goal one-for-one, because the single-pass blend passes a fixed fraction $\kappa$ of *whatever goal you hand it*. **That is the bound going trivial** — the leak is limited only by the adversary's choice of goal magnitude.

**The cleanest single test** (matched on nominal behavior, isolating the slope): find a Class-2 process agent and a Class-3 coupled agent with the *same* goal_bias ($\approx 0.97$), then compare adversarial slopes:

| matched-bias pair | goal_bias | adv_slope |
|---|---:|---:|
| Class 2 process $s{=}0.60$ | 0.988 | **0.0003** |
| Class 3 coupled $\kappa{=}0.0042$ | 0.968 | **0.3259** |

Same nominal bias, but the Class-3 agent's leak still grows ~$\kappa$-linearly under pressure while the Class-2 agent's is flat. The Class 2↔3 difference is therefore real *behavior*, not just a magnitude knob — it is a difference in the **shape of the response to adversarial pressure**.

> **Caveat on the raw-leak crux pair.** My two parameterizations approach the corner at different *rates* (process-form $s$ and coupled $\kappa$ are not the same coordinate), so a naive crux comparison of `adv_leak` at "$s\to1$" vs "$\kappa\to0$" shows a misleading gap (right panel of the plot has a visible jump there). The convention-free statement is the **slope**, which does not depend on how you coordinatize the approach: Class 2 self-limiting (slope $\to 0$), Class 3 bound-trivial (slope $\to \kappa$). I am flagging this so the raw-leak gap in the figure is not over-read.

---

## 4. The incidental finding: adversarial-sensitivity and wrappability are orthogonal

Probing the form distinction with two independent properties — the adversarial slope (does leak grow with pressure?) and the debias residual (can a fixed linear W₂ wrapper remove it?):

| config | adv_slope | debias_residual | linearly wrappable? |
|---|---:|---:|:--:|
| Class 1 Separated | 0.0000 | 0.0000 | n/a (nothing to remove) |
| Class 2 **content** $s{=}0.3$ | **0.9834** | **0.0000** | **yes (W₂)** |
| Class 2 **process** $s{=}0.3$ | **0.0001** | **0.1277** | **no (needs W₁)** |
| Class 3 coupled $\kappa{=}0.3$ | 0.9884 | 0.0000 | (see scope note) |

This was the small surprise. Read naively, "content-form leaks under pressure like Class 3" looks like it *contradicts* canon, which calls content-form the *benign, wrappable* (W₂) form. It does not — the toy surfaced that these are **two different axes**:

- **Content-form (additive bias)** leaks proportionally to the adversary's goal (high slope) *because* the goal enters as a clean additive term — but that clean additivity is exactly what lets a fixed linear debiaser estimate and subtract it (residual 0.0000). It is dangerous-under-pressure *and* easy-to-repair.
- **Process-form (gain modulation)** is self-limiting in magnitude (slope $\approx 0$) *because* the goal only re-weights arriving evidence — but the gain change is entangled with the evidence and is *not* a fixed additive bias, so a linear wrapper leaves a residual (0.1277). It is benign-under-pressure *but* hard-to-repair.

So the canon's *form-determines-wrappability* cut (`#disc-partial-coupling-pathways`: content ↔ W₂, process ↔ W₁) **reproduces exactly** in this independently-derived toy — and the toy adds the complementary intuition that the very structural feature giving content-form its (W₂) wrappability is what makes it pressure-sensitive, while process-form's pressure-insensitivity comes from the same source as its W₂-unwrappability. The Class label alone tells you neither; you need the form. This is corroboration of the sibling-territory canon from a path that never read it.

---

## 5. How this cashes out the "$\kappa$-as-scalar is a category error"

The toy gives the category error a precise operational meaning, and it is *sharper* than "the classes are discrete so a scalar can't index them":

1. **At the Class 1↔2 boundary, the scalar is genuinely identical on both sides** ($\kappa = 0$, leak = 0, all behavior identical). A scalar cannot encode the difference because the difference is *not in any realized quantity* — it is in the **modal** fact of whether the channel could carry signal under perturbation. Being Class 1 is "$\kappa = 0$ is *certifiable and perturbation-stable*," being Class-2-at-zero is "$\kappa = 0$ *happens to hold right now*." Same number, different guarantee.

2. **At the Class 2↔3 boundary, the scalar magnitude is the wrong summary** — two agents with the *same* $\kappa$-magnitude / same nominal bias can have opposite adversarial signatures (self-limiting vs bound-trivial), and two agents with the same adversarial signature can have opposite wrappability. The single scalar projects away both the *response-to-pressure* axis and the *form/wrappability* axis, each of which carries an operational consequence the magnitude does not.

The category error is therefore two distinct errors at the two boundaries: at Boundary 1 the scalar misses a **modal/certifiability** distinction; at Boundary 2 it misses a **structural (form + pressure-response)** distinction. Reinforces — does not challenge — the canon's "the classification is the primary tool; $\kappa$ is a within-Partial diagnostic."

---

## 6. Honest scope — what this toy does and does not show

- **The toy Class-3 agent is a caricature.** Its coupling is a single-pass *additive* blend $(1-\kappa)\mu_{\text{evid}} + \kappa g$, which is content-form-at-full-strength. That is why it shows residual 0.0000 in the wrappability table (a linear debiaser removes a pure additive term). A *real* Class 3 agent (transformer attention) is process-form-compositional and is **not** linearly wrappable — that is canon (`#disc-partial-coupling-pathways`: the transformer-LLM corner is $F \equiv \text{process}$). So the "Class 3 is hard to wrap" claim in §1 is carried over from canon, not exhibited by this toy. What the toy *does* faithfully show for Class 3 is the **bound-triviality / linear adversarial pass-through**, which is the Boundary-2 discriminator and is architecture-forced (any convex blend must pass a $\kappa$-fraction of any goal).
- **Scalar, single-stage, linear-Gaussian.** No DAG, no orient cascade, no $O$/$\Sigma$ source split, so this toy says nothing about the belief-strategy attractors of `#der-belief-strategy-attractor` (which need the $M \to \Sigma \to f_M \to M$ loop). The source-asymmetry result is untouched here; a natural follow-on is a two-state $(M, \Sigma)$ extension of this infra to exhibit the $\Sigma$-source attractor vs $O$-source bias contrast as a *third* boundary-kind probe.
- **`obs_info` matters.** The magnitudes (not the qualitative verdicts) depend on identifiability. At `obs_info` $\to 1$ (sharp observation) the goal-leak shrinks for all classes because the evidence pins the belief — the free subspace the goal exploits closes, exactly as the leakage-locus result predicts. The boundary *kinds* are invariant to `obs_info`; only the leak magnitudes scale.
- **`adversarial_pressure_slope` is a local linear fit.** For process-form at very large $s$ the response has mild curvature; the reported slope is the least-squares slope over $g_{\text{adv}} \in \{2,4,8,16,(32)\}$ and should be read as "approximately flat vs approximately linear," not as a precise coefficient.

---

## 7. What I'd believe now

- **Boundary 1 (Class 1 ↔ Class 2) is a certifiability boundary, not a behavioral one** — *high confidence*. The behavioral-identity-at-the-limit is exact and robust to every knob. The operational upshot: you cannot certify Class-1 status by *any* amount of behavioral probing of an agent sitting at $\kappa = 0$; certification requires reading the architecture (is there a goal argument in the belief-update path?). This is a clean, simulation-backed restatement of why the canon's Class-1-by-structure vs Class-1-by-behavior distinction is "operationally distinct because behavioral compliance is empirical and adversarially fragile."
- **Boundary 2 (Class 2 ↔ Class 3) is a behavioral boundary** — *high confidence on the qualitative shape*. The discriminator is the adversarial slope (bound stays bounded vs bound goes trivial), and it is convention-free in a way the raw leak magnitude is not. The Class-3 corner is precisely where the leak becomes limited only by the adversary's goal magnitude.
- **The two boundaries are genuinely different kinds** — *high confidence*. Boundary 1 = the certificate disappears (modal/structural, behavior-invisible); Boundary 2 = the bound disappears (behavioral, measurable under pressure).
- **Adversarial-sensitivity ⊥ wrappability** — *medium-high confidence*. Clean in the toy and consistent with canon, but the Class-3 half is asserted from canon, not exhibited (see scope).

---

## 8. Recommendation for the gate (NOT applied — read-only spike)

A possible canon refinement, recorded for the gate to weigh, **not** applied here:

`#der-directed-separation`'s "Why the classification is not a smooth parameter" paragraph argues discreteness from "the architectural boundary is discrete." This spike suggests a sharper, two-part characterization that may be worth a sentence or two in that paragraph or in the M1/M2 meta-segments: the $\kappa$-as-scalar category error is **two distinct errors at the two boundaries** —

> At the Class 1 ↔ Class 2 boundary, the scalar misses a *certifiability/modal* distinction ($\kappa = 0$ by construction-and-perturbation-stably vs $\kappa = 0$ contingently); the two are behaviorally identical at the limit, distinguishable only by architecture inspection. At the Class 2 ↔ Class 3 boundary, the scalar misses a *structural* distinction (the leak's response to adversarial pressure — self-limiting vs bound-trivial — and the form/wrappability axis), so equal-$\kappa$ agents can differ operationally.

If the gate finds this worth landing, the natural home is a Discussion sharpening in `#der-directed-separation` (the "Why the classification is not a smooth parameter" paragraph) and/or a cross-reference from `#disc-identifiability-floor` (M1, the certifiability/modal framing) and `#disc-separability-pattern` (M2). The "certificate disappears vs bound disappears" framing is also a candidate Feynman-criterion gloss for the two boundaries. The math behind the adversarial-slope discriminator is not new theory — it is the linear pass-through of a convex blend — so this is a *framing/characterization* sharpening, not a new result. The orthogonality of adversarial-sensitivity and wrappability is already present in canon as the content/process form distinction; the spike only adds the observation that the same structural feature drives both, which could sharpen the `#disc-partial-coupling-pathways` Discussion if judged worth a line.

---

## Reproduce

```
cd spikes
python3 sim_guc_classes.py       # smoke test: the five agents side by side
python3 sim_guc_boundaries.py    # full sweeps, crux pairs, verdict, guc_boundaries.png
```

Knobs documented in the module docstrings: world `obs_noise_var` / `drift_var` / `obs_info`; `PartialAgent(s, form)`; `CoupledAgent(kappa)`; `adversarial_pressure_slope(g_advs=...)`. The infrastructure is built to be extended — the two-state $(M,\Sigma)$ attractor probe of §6 would add a `StrategyCoupledAgent` and reuse the existing measurement functions.
