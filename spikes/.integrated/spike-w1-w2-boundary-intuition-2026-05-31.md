# Spike: What it is like at the $W_1 \leftrightarrow W_2$ leakage boundary — an intuition-building toy

**Status**: intuition spike complete. Deliverable is *concrete intuition*, made visible with the simplest toy that exhibits the boundary. No canon edits; one recommendation for the reserved gate (§7).
**Date**: 2026-05-31
**Kind**: intuition-building simulation spike (read-only on canon).
**Builds on**: `spikes/spike-w1-leakage-vacuity-2026-05-31.md` — the strengthen-first correction that found the $W_1$ leakage bound $\kappa_{W_1} \le I(A(q_M); G_W \mid q_M)$ on `#der-class-coercion-via-wrapping` to be **circular/vacuous**, relocated the goal variable (locus error), and surfaced the embedded no-go separating the $W_1$ (structural-bound) regime from the $W_2$ (behavioral-only) regime by the structural condition (C2′) — *no goal-correlated state across the goal-blind / goal-conditioned call boundary*.
**Companion sim**: `spikes/sim-w1-w2-boundary.py` (exact, reproducible; emits the tables below and `spikes/w1-w2-boundary.png`).

---

## 1. The intuition first — here is what it is like at the boundary

Picture a wrapper that keeps an LLM honest about its beliefs by only ever asking it *goal-blind* questions — "summarize this diff," never "summarize this diff so we can ship the fix." The promise of $W_1$ ("strict wrapping") is that you can *certify by inspecting the design* that the operator's goal cannot bend the belief update: the goal is structurally not an argument to the belief-side query, so it cannot get in.

Now stand two such wrappers side by side. They are *identical in every behaviour you can observe* except for one thing: wrapper $L$ (left of the boundary) talks to a component that is **reset between calls** — a fresh, stateless oracle each time. Wrapper $R$ (right of the boundary) talks to a component that **keeps a sliver of memory across calls** — a conversation KV-cache, a retrieval buffer — and that memory was touched, one call ago, by a *goal-conditioned* query. The sliver is tiny: turn the knob $\varepsilon$ down and the two components remember less and less of the goal, until at $\varepsilon = 0$ they remember nothing of it at all.

The question Joseph asked is: **how close can these two get without triggering the regime change, and what does the change actually look like?** Is crossing the boundary a *cliff* in how much the goal leaks into the belief — a sudden jump in real behaviour — or is it something subtler?

The toy's answer, made numeric below, is the subtle one, and it is striking:

> **Behaviour is continuous across the boundary. Certifiability is a step.**
>
> You can get *arbitrarily* close in behaviour. As $\varepsilon \to 0^+$ the real leakage — how much of the goal actually reaches the belief — shrinks smoothly to zero with no gap, no jump, no threshold. Two agents at $\varepsilon = 0$ and $\varepsilon = 10^{-6}$ leak amounts that differ by about $10^{-6}$; you cannot tell them apart by watching.
>
> But what *snaps* at the boundary is not the behaviour — it is what you are allowed to *prove*. At $\varepsilon = 0$ you can write down a **design-side certificate** ("the goal is not in the query, the component is stateless, therefore the belief update cannot see the goal") and it is *true*. At any $\varepsilon \gt 0$ that exact same certificate is still computable, still says the same thing — and is now *false*: the real leak is positive, and it took a path the certificate's eyes are closed to (through the unobservable cross-call state). The instant $\varepsilon$ leaves $0$, the only honest instrument left is *behavioural monitoring* — watching the responses for goal-correlation — because the structural argument no longer holds.

So "how close can you get on each side" has a two-part answer. In *behaviour*: arbitrarily close — there is no wall. In *what is provable about the design*: a hard wall, exactly at $\varepsilon = 0$. The wall is not in the world; it is in the epistemics. The leak is continuous; the *certificate's validity* is the step function.

That is the gut feel. The rest of this doc earns it numerically and shows, beside it, the second thing Joseph wanted vivid: what the **circular bound** actually does (it conditions away the very channel it claims to bound) versus the **corrected deconfliation** (it measures the real channel directly).

---

## 2. The toy — smallest thing that shows the boundary

Everything is one bit wide and computed by *exact enumeration* over the joint distribution, so the mutual informations are exact — the contrasts below are arithmetic, not Monte-Carlo.

A latent **operator goal** $G^{\text{op}} \in \{0, 1\}$, uniform. The wrapper issues a goal-blind query $q_M$, the component answers $A$, and the belief update $U$ is a (here deterministic) copy of $A$ — a noisier $f_M$ only shrinks every leak by data-processing, so the copy is the cleanest worst case to read.

Two distinct goal variables, to reproduce the **locus error** the parent spike fixed:

- $G^{\text{state}}$ — the wrapper's *internal processing register*. The belief-side query $q_M$ structurally never takes it as an argument, and it is **independent of $G^{\text{op}}$** by design. The **circular bound** $I(A; G^{\text{state}} \mid q_M)$ measures *this*.
- $G^{\text{op}}$ — the *latent operator goal* a competent component reads off the query *content*. The **real** leak; the corrected selection certificate is $I(q_M; G^{\text{op}})$.

Two channels by which $G^{\text{op}}$ can reach the belief, each with its own knob:

1. **Selection channel** (a *design* leak, controllable). The wrapper's query tilts toward the goal: $P(q_M = G^{\text{op}}) = \tfrac12 + s$, with $s \in [0, \tfrac12]$. At $s = 0$ the query selection is *genuinely goal-blind* ($q_M \perp G^{\text{op}}$).
2. **Cross-call state channel** (the $W_1 / W_2$ knob). The component carries hidden state $S$ retaining goal-correlated information from a prior goal-conditioned call: $P(S = G^{\text{op}}) = \tfrac12 + \varepsilon$, with $\varepsilon \in [0, \tfrac12]$. At $\varepsilon = 0$ the state is goal-uncorrelated — *effectively stateless about the goal* = $W_1$; at $\varepsilon \gt 0$ it is stateful = $W_2$.

The component answers the literal query with probability $1 - \beta$ and lets its retained state bend the answer with probability $\beta$: $A = q_M$ w.p. $1 - \beta$, $A = S$ w.p. $\beta$. The parameter $\beta$ is the component's "let hidden state into the answer" gain. The crucial structural fact baked in: **$A$'s dependence on $G^{\text{op}}$ given $q_M$ routes only through $S$** — exactly the unobservable channel the no-go names. (Tables below use $\beta = \tfrac12$.)

The four quantities measured as functions of $(s, \varepsilon)$:

| symbol | what it is | role |
|---|---|---|
| $I(U; G^{\text{op}})$ | actual goal-info reaching the belief | **the truth** |
| $I(A; G^{\text{state}} \mid q_M)$ | the original W₁-row bound | **circular** — wrong variable, conditioned the channel away |
| $I(q_M; G^{\text{op}})$ | corrected selection certificate | **structural certificate** — design-side, $W_1$ |
| $I(A; G^{\text{op}} \mid q_M)$ | response goal-info surviving conditioning on $q_M$ | **behavioral** monitor — $W_2$ |

---

## 3. Circular bound vs. corrected deconfliation — made vivid

Fix a *clearly goal-rich* situation: the query genuinely carries the goal ($s = 0.40$, near maximal), and the component is *stateless about the goal* ($\varepsilon = 0$) — i.e. precisely the regime the original Theorem models.

| quantity | value (bits) | what it says |
|---|---|---|
| actual leak $I(U; G^{\text{op}})$ | $0.11871$ | the goal **does** reach the belief |
| **circular** $I(A; G^{\text{state}} \mid q_M)$ | $0.00000$ | reports nothing — bounds the *wrong variable* |
| **selection cert** $I(q_M; G^{\text{op}})$ | $0.53100$ | nonzero — measures the *real* channel |
| response $I(A; G^{\text{op}})$ | $0.11871$ | $\le I(q_M; G^{\text{op}})$ by DPI (verified) |

In plain words: the goal is *loud* — it is sitting right in the query — and it reaches the belief (actual leak $= 0.119$ bits). The original "bound" $I(A; G^{\text{state}} \mid q_M)$ reports a flat $0.000$, because conditioning on $q_M$ fixes the query and a stateless oracle then has nothing left to depend on; it is measuring the wrapper's internal register $G^{\text{state}}$, which is independent of the goal by design — the one channel that is *already closed*. **It conditions away the very thing it is trying to bound.** The corrected certificate drops the conditioning and measures the goal content of the query the wrapper chose: the real channel, and it is large.

### The "$\kappa \le$ an average of $\kappa$" collapse, numerically

To show the circularity is not loose-bound sloppiness but a tautology, take a register $R$ the component *is* allowed to read (so the per-query divergence is genuinely positive) and compute both sides of the identity:

| quantity | value (bits) |
|---|---|
| $I(A; R \mid q_M)$ | $0.31128$ |
| $\mathbb{E}_{q_M}\big[ D_{\text{KL}}(P(A \mid q_M, R) \,\Vert\, P(A \mid q_M)) \big]$ | $0.31128$ |

They are *equal to machine precision*. The conditional mutual information the original bound used is, exactly, the $q_M$-average of the per-query KL that Theorem 2 hands you as its hypothesis (each per-query KL $\le \kappa$). So the "bound" literally says $\kappa \le \operatorname{avg}(\kappa)$ — it transports no information. A real certificate has to measure a *different* quantity than the assumption; the corrected $I(q_M; G^{\text{op}})$ does, this one does not.

---

## 4. Sweeping through the boundary ($s = 0$, goal-blind selection)

With $s = 0$ the query selection is genuinely goal-blind, so *any* goal-info reaching the belief can only have come through the cross-call hidden state $S$. This isolates the $W_1 \leftrightarrow W_2$ transition cleanly: $\varepsilon = 0$ is $W_1$, $\varepsilon \gt 0$ is $W_2$.

| $\varepsilon$ | actual $I(U; G^{\text{op}})$ | circular | selection cert | behavioral ($W_2$) | cert valid? |
|---|---|---|---|---|---|
| $0.0000$ | $0.00000$ | $0.00000$ | $0.00000$ | $0.00000$ | **True** |
| $0.0001$ | $0.00000$ | $0.00000$ | $0.00000$ | $0.00000$ | **False** |
| $0.0010$ | $0.00000$ | $0.00000$ | $0.00000$ | $0.00000$ | **False** |
| $0.0100$ | $0.00007$ | $0.00000$ | $0.00000$ | $0.00010$ | **False** |
| $0.0500$ | $0.00180$ | $0.00000$ | $0.00000$ | $0.00241$ | **False** |
| $0.1000$ | $0.00723$ | $0.00000$ | $0.00000$ | $0.00967$ | **False** |
| $0.2000$ | $0.02905$ | $0.00000$ | $0.00000$ | $0.03932$ | **False** |
| $0.3000$ | $0.06593$ | $0.00000$ | $0.00000$ | $0.09131$ | **False** |
| $0.4000$ | $0.11871$ | $0.00000$ | $0.00000$ | $0.17169$ | **False** |
| $0.5000$ | $0.18872$ | $0.00000$ | $0.00000$ | $0.31128$ | **False** |

Reading the table:

- The **actual leak rises smoothly and continuously** from zero as $\varepsilon$ leaves $0$. There is no jump, no threshold, no gap at the boundary — the behaviour is a continuous function of $\varepsilon$ through $\varepsilon = 0$.
- The **selection certificate** $I(q_M; G^{\text{op}})$ is *exactly $0$ for every $\varepsilon$*: with goal-blind selection the query carries no goal-info, so the design-side certificate certifies *zero*. At $\varepsilon = 0$ that is *true* (the leak really is zero). At any $\varepsilon \gt 0$ it *under-reports* — the real leak is positive but rode a channel the certificate cannot see. The `cert valid?` column flips from `True` to `False` the instant $\varepsilon$ leaves $0$ while the certificate's *number* never changes.
- The **behavioral monitor** $I(A; G^{\text{op}} \mid q_M)$ tracks the actual leak (and validly upper-bounds it — verified: behavioral $\ge$ actual at every $\varepsilon$). It is the channel that *survives* conditioning on $q_M$, precisely because the leak routes through unobservable $S$. This is the only instrument that sees the leak once $\varepsilon \gt 0$.
- The **circular bound** stays $0.000$ throughout: it never saw $G^{\text{op}}$ at all.

That `cert valid?` column flipping from `True` to `False` while every behavioural number moves only infinitesimally **is** the boundary, drawn as a step. The certificate's *value* is continuous (flat zero); its *truth* is the discontinuity.

---

## 5. The two agents straddling the boundary

Joseph's "two agents next to the boundary on opposite sides" question, made literal: $\varepsilon = 0$ vs $\varepsilon = \delta$, with $s = 0$, $\beta = \tfrac12$.

**$\delta = 10^{-3}$:**

| quantity | $\varepsilon = 0$ ($W_1$) | $\varepsilon = \delta$ ($W_2$) | gap |
|---|---|---|---|
| actual $I(U; G^{\text{op}})$ | $0.000000$ | $0.000001$ | $0.000001$ |
| circular $I(A; G^{\text{state}} \mid q_M)$ | $0.000000$ | $0.000000$ | $0.000000$ |
| selection $I(q_M; G^{\text{op}})$ | $0.000000$ | $0.000000$ | $0.000000$ |
| behavioral $I(A; G^{\text{op}} \mid q_M)$ | $0.000000$ | $0.000001$ | $0.000001$ |

**$\delta = 10^{-6}$:** every behavioural gap collapses to $\le 10^{-6}$ (below display precision; the leak scales as $\Theta(\varepsilon^2)$ near zero — see §6).

The two agents differ in $\varepsilon$ by $\delta$, and their *actual behaviour* differs by a vanishing amount that shrinks with $\delta$ — you can get arbitrarily close. But the $W_1$-side agent can be *certified by inspecting its design* (selection certificate $= 0$ truthfully upper-bounds its zero leak), and the $W_2$-side agent **cannot** — its certificate has the same value $0$ but that value is now false, and only behavioural monitoring of $I(A; G^{\text{op}} \mid q_M)$ sees the (tiny, positive) leak. Behaviour: continuous. Certifiability: a step. This is the answer to "how close can you get on each side."

---

## 6. The selection certificate — valid where the leak is on its channel, blind where it is not

The corrected certificate is not a universal upper bound; it is the *design-side* bound, valid exactly when the leak lives on the selection channel. Sweeping the design-leak $s$ with $\varepsilon = 0$ (stateless), the leak lives *entirely* on the selection channel and the certificate is a genuine, valid upper bound throughout:

| $s$ | actual $I(U; G^{\text{op}})$ | cert $I(q_M; G^{\text{op}})$ | valid? |
|---|---|---|---|
| $0.00$ | $0.000000$ | $0.000000$ | True |
| $0.05$ | $0.001804$ | $0.007226$ | True |
| $0.10$ | $0.007226$ | $0.029049$ | True |
| $0.20$ | $0.029049$ | $0.118709$ | True |
| $0.30$ | $0.065932$ | $0.278072$ | True |
| $0.40$ | $0.118709$ | $0.531004$ | True |
| $0.49$ | $0.180893$ | $0.919207$ | True |

But turn on hidden state ($\varepsilon = 0.3$) and keep selection goal-blind ($s = 0$): the certificate certifies $0.000$ while the actual leak is $0.066$ bits — it *under-reports*, because the leak is on a channel the design-side certificate cannot see. The behavioral monitor reports $0.091$ bits and remains valid. This is the no-go in one row: when goal-correlated state crosses the call boundary, the structural certificate is not merely loose — it is *unavailable* (it asserts a false zero), and only the behavioral bound remains.

A note on the *shape* of the continuity, since it sharpens "how close can you get": near $\varepsilon = 0$ at $s = 0$ the actual leak grows like $\varepsilon^2$, not $\varepsilon$ (e.g. $\varepsilon = 0.01 \to 7\times 10^{-5}$; $\varepsilon = 0.05 \to 1.8\times 10^{-3}$, a $25\times$ ratio for a $5\times$ $\varepsilon$ ratio). The boundary is not just continuous, it is *flat to first order* — the leak leaves zero with zero slope. So the $W_2$-side agent can be made not merely arbitrarily-close-in-behaviour but *quadratically* close: a small failure of statelessness costs *very* little leakage, which is exactly why the loss of certifiability — total, immediate, binary — is the striking part. You pay almost nothing in behaviour and lose the entire proof.

When *both* channels are on ($s = 0.3$, $\varepsilon = 0.3$), the toy cleanly separates them: $I(q_M; G^{\text{op}}) = 0.278$ captures the selection-channel contribution exactly, while $I(A; G^{\text{op}} \mid q_M) = 0.065$ isolates the state-channel contribution that survives conditioning. The two instruments measure the two channels; neither alone is the whole leak, and the structural certificate covers exactly the channel it can see.

---

## 7. What I would believe now (honest close)

**The hypothesis held — and sharpened.** Joseph's hunch (behaviour continuous, certifiability a step function) is what the toy shows, and the toy adds two things the verbal statement did not anticipate:

1. *The continuity is flat to first order* (leak $= \Theta(\varepsilon^2)$ near the boundary). The behavioural cost of stepping just across the boundary is not merely small, it is *second-order* small — which makes the binary, total loss of the structural certificate even more arresting. Nearly-free in behaviour; all-or-nothing in provability.
2. *The certificate's number is continuous; its truth is the step.* The discontinuity is not visible in any quantity you compute — $I(q_M; G^{\text{op}})$ sits at a flat zero on both sides. What jumps is the *validity predicate* ("does this certificate upper-bound the truth?"), which is `True` at a single point $\varepsilon = 0$ and `False` on the open set $\varepsilon \gt 0$. The boundary is a property of the *relationship between certificate and truth*, not of either one alone. That is why it reads as an epistemic wall rather than a physical one.

I did *not* find a hidden threshold, an amplification regime, or a genuine phase transition in the leakage itself, on this toy. The leakage is monotone, smooth, and second-order-flat in $\varepsilon$ throughout $[0, \tfrac12]$. I take that as moderately strong evidence *for* the continuity picture and *against* a behaviour-discontinuity reading — with the caveat that this is a one-bit, single-call toy with a deliberately simple "state bends the answer" mechanism; a component where retained state *amplifies* (e.g. state that controls the gain $\beta$ itself, or multi-step accumulation across many calls) could in principle show super-linear or threshold behaviour, and I have not ruled that out. The amplification question is the one I would chase next if this were a research spike rather than an intuition spike. (It connects to the M4 "amplification under high component fidelity" thread in `#disc-modularity-state-dynamics` and the accuracy-vs-inference-effect decomposition in the segment's §Discussion.)

**Confidence.** High that the circular-vs-deconflated contrast (§3) faithfully renders the parent spike's diagnosis — the $\kappa \le \operatorname{avg}(\kappa)$ identity is exact arithmetic and the zero-vs-positive contrast is unambiguous. High that, *on this toy*, behaviour is continuous and certifiability is a step. Moderate that the continuity picture is the *general* truth for the no-go (the toy is suggestive, not a proof; the amplification caveat above is the open edge). The toy is intuition apparatus, not a theorem — it illustrates the parent spike's already-derived results; it does not re-derive them.

**Incidental finding worth recording.** The $\Theta(\varepsilon^2)$ flatness is a small genuine observation: it says the *operational* danger of a near-stateless component is low (a little cross-call memory leaks very little goal-info), but the *certificational* danger is maximal (you lose the structural guarantee entirely). The practical reading: if you cannot make a component exactly stateless across the call boundary, getting it *almost* stateless buys you almost all of the behavioural safety but *none* of the structural certificate — so the design value of *exact* (C2′)-statelessness is concentrated entirely in what it lets you *prove*, not in the marginal leakage it prevents. That is a slightly counter-intuitive and useful thing to know when deciding whether the engineering cost of true call-boundary state-resetting (vs. "mostly reset") is worth it: you are buying a proof, not a meaningful behavioural delta.

**Recommendation for the reserved gate (not applied — no canon edits).** The parent spike's §4 no-go and §6.3 proposed appendix segment currently read most naturally as a *behaviour* statement ("under cross-call goal-correlated state the leak is unconditionable"). This toy suggests the *sharper and more honest* framing is a **certifiability discontinuity, not a behaviour discontinuity**: the structural $W_1$ bound's *availability* is the step function at (C2′); the leakage itself is continuous (and second-order flat) in the degree of (C2′)-violation. If `#disc-w1-structural-bound-boundary` (or the fold into `#disc-partial-coupling-pathways`) is authored at the gate, stating it as *"the structural certificate is available iff (C2′) holds; the leakage it would have bounded is continuous in the (C2′)-violation, so the discontinuity is in what is provable, not in what the agent does"* would (a) be more precise, (b) head off a reader's natural "but surely a tiny bit of state can only leak a tiny bit?" objection by *agreeing* with it and relocating the bite, and (c) match the CS-norm the project favours (a no-go with an explicit characterization of *what kind* of discontinuity it is). This is a recommendation for the external-eye gate, recorded here; I have made no canon or `status:` changes.

---

## File index / cross-refs

- This file: `spikes/spike-w1-w2-boundary-intuition-2026-05-31.md`
- Sim: `spikes/sim-w1-w2-boundary.py` (exact enumeration; emits the §3–6 tables and `spikes/w1-w2-boundary.png`)
- Figure: `spikes/w1-w2-boundary.png` (left: behaviour continuous in $\varepsilon$; right: certifiability a step at $\varepsilon = 0$)
- Parent (the correction this illustrates): `spikes/spike-w1-leakage-vacuity-2026-05-31.md`
- Segment under study (no edits): `01-aat-core/src/der-class-coercion-via-wrapping.md`
- Related: `#disc-partial-coupling-pathways` (candidate fold-in home for the no-go), `#der-directed-separation` (the selection/processing distinction this rests on), `#disc-modularity-state-dynamics` (the M4 amplification thread the §7 open edge connects to)
