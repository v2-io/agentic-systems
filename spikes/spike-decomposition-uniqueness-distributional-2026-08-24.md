# Spike: the distributional analog of decomposition uniqueness — the expected obstruction dissolves, and the real break is somewhere better

*2026-08-24, second spike of the cycle. Joseph-commissioned follow-on to `spike-decomposition-uniqueness-2026-08-24.md`, whose results were pathwise (structural representation, exogenous noise fixed) and whose Working Notes flagged the distributional/kernel-level analog as the main open line, with strong-lumpability meet-closure named as the suspected obstruction. Disposition per `spikes.sop.md` §0/§0c. **Read-only on canon: no segment, OUTLINE, or `status:` edited by this spike.** Integration thoughts are parked in `spike-decomposition-uniqueness-distributional-2026-08-24-integration-suggestions.md` for the separate verification/integration agents — suggestions, not a work order.*

## 0. Verdict in four lines

1. **My own prior diagnosis was wrong, in both directions.** The lumpability meet-closure failure I flagged as the obstruction never touches the main theorem — the pathwise canonicity proof routes through one specific partition and its universal property, not through the congruence lattice. **The canonicity theorem lifts to kernels essentially verbatim** (§2), under exactly the hypothesis canon already names: causal discipline, $\kappa_{\text{processing}} \equiv 0$, which turns out to be *literally* the kernel-level form of epistemic closure.
2. **A representation theorem falls out en route** (§3): a joint update kernel admits a separated decomposition distributionally **iff** it admits a structural (randomized-function) realization with *private, independent* noise for the two components. So the pathwise spike's "structural representation" scope assumption was not a loss of generality — and "directed separation, distributionally" = "pathwise separation + noise privacy," which is a sharper statement than either alone.
3. **The genuine break is the Class-3 corollary, and it breaks worse — and more interestingly — than expected.** For goal-coupled kernels the "largest belief-like factor" is **not well-defined distributionally**: an explicit 8-state agent (§4) has two *incomparable minimal* belief-candidate quotients, each of which hides the goal-leak by merging a different pair of belief-values, with no common refinement that is itself a factor. Under goal-coupling, *what counts as belief is a convention* — you choose which leak you agree not to resolve — and maximal choices can be mutually incompatible.
4. The pathwise and distributional pictures now cohere completely: for causally-disciplined agents they agree and are representation-independent (§2–3); for Class 3 the pathwise congruence-closure object is representation-*dependent* and the distributional object is non-canonical — **the same fact seen from two sides** (§4.4).

## 1. The distributional formalization — getting the definitions to say what canon means

Kernels replace maps: for each event $e$, a Markov kernel $P_e(X, \mathrm dX')$ on a standard Borel state space $\mathcal X$. (Standard Borel is load-bearing twice below: regular conditional probabilities exist, and Lusin–Souslin makes measurable bijections bimeasurable.)

**Definition (separated decomposition, distributional).** Measurable $\mu : \mathcal X \to \mathcal M'$, $\gamma : \mathcal X \to \mathcal G'$ with:

- **(K1) Product-completeness.** $(\mu, \gamma)$ a bimeasurable bijection onto $\mathcal M' \times \mathcal G'$.
- **(K2) Epistemic closure.** The $\mu$-pushforward of $P_e(X, \cdot)$ depends on $X$ only through $\mu(X)$: there are kernels $Q_e$ with $P_e\big(X, \mu^{-1}(A)\big) = Q_e(\mu(X), A)$.
- **(K3) Cascade form.** In the coordinates of (K1), the joint kernel factors as $P_e(\mathrm dm', \mathrm dg' \mid m, g) = Q_e(m, \mathrm dm')\, R_e\big((g, m'), \mathrm dg'\big)$ — equivalently, the conditional law of $\gamma(X^+)$ given $\mu(X^+)$ depends only on $(\gamma(X), \mu(X^+), e)$: the conditional independence $\gamma(X^+) \perp \mu(X) \mid \big(\gamma(X), \mu(X^+), e\big)$.

Three recognitions that make the definitions canonical rather than invented:

- **(K2) for a single partition is exactly Kemeny–Snell strong lumpability** of $P_e$ with respect to $\ker\mu$ (equivalently Dynkin's criterion for a function of a Markov process to be Markov, uniformly in the starting law). The whole spike is lumpability theory pointed at the belief/goal carve.
- **(K2) for the base coordinates is exactly canon's causal discipline.** $\kappa_{\text{processing}} = I(G_t;\, M_{\tau^+} \mid e_\tau, M_{\tau^-}) / H(\cdot)$ vanishes *under every input distribution* iff the $M$-marginal kernel has no $G$ argument — which is (K2). So the distributional theorem's hypothesis is not a new condition; it is `#der-directed-separation`'s $\kappa \equiv 0$, and the distributional setting is the natural home of the $\kappa$-language (the pathwise setting can only see one realization of it).
- **(K3) is *not* automatic given (K1)+(K2)** — the regular conditional of $g'$ given $m'$ always exists but is a priori a function of the whole prior state; (K3)'s content is the absence of a residual $m^-$-path into the goal coordinate. And (K3) is where the genuinely distributional subtlety of **noise sharing** lives — see §3.

Interventions: the goal-reset operators $\iota_g$ are deterministic and unchanged; allowing stochastic resets (draw $g$ from a law) generates the same orbit equivalence, so nothing downstream changes. Purity (R2) and completeness (R3) are set-level statements about $\mu$ and transfer verbatim; (R1) becomes (K1).

## 2. The expected obstruction dissolves — the canonicity theorem lifts

**The misdiagnosis, recorded first because it is the spike's most transferable content.** The prior spike's Working Notes said: *"lumpable partitions are not in general closed under common refinement, so Lemma 1's meet-closure argument does not transfer."* Both clauses are true (§4 constructs the non-closure witness first-hand). The inference was wrong, because the pathwise canonicity theorem **never used Lemma 1**. Re-reading the proof with the question "which steps consume the lattice?" gives: none — the lattice was framing (Approach 4's failure record) and fed only the Class-3 corollary's congruence *closure*. The main theorem routes through (i) one specific partition — the goal-variation orbits — shown closed directly, and (ii) the quotient's universal property. Neither step quantifies over the family of factors. *The lesson: when flagging an open analog, name which proof steps the suspected obstruction touches; an obstruction to the scaffolding is not an obstruction to the theorem.* I inherited my own framing uncritically for about an hour before checking.

**Theorem D (distributional canonicity).** Standard Borel spaces; base kernels satisfy (K1)–(K3) in the base coordinates — i.e. the agent is causally disciplined, $\kappa_{\text{processing}} \equiv 0$, with cascade-form goal update; full intervention access. Then:

**(i)** The goal-orbit partition $\{\{m\} \times \mathcal G\}$ is **strongly lumpable** for every $P_e$, with quotient kernel $Q_e$ — the belief kernel. *Check, one line:* $P_e\big((m, g),\; \{m'\}\text{-orbit}\big) = Q_e(m, \mathrm dm')$, independent of $g$ by (K2). This is the distributional commutation identity; note it is *weaker* to demand than the pathwise $F_e \circ \iota_g = \iota_{g'} \circ F_e$ (no specific $g'$ needs to exist — the goal-side randomness may smear), which is exactly why the lift is easy: the distributional statement asks less of the goal fiber.

**(ii)** Any (R2)-pure factor descends to the orbit quotient — set-level, unchanged.

**(iii)** Any separated decomposition satisfying (K1)+(R2)+(R3) has $\mu = \theta \circ q$ with $\theta$ a bijection **intertwining the kernels**: $Q'_e(\theta(\bar m), A) = \bar Q_e(\bar m, \theta^{-1}A)$ — the diagram chase is the pathwise one with pushforwards in place of compositions, using (K2) of the candidate on one side and (i) on the other. $\theta$ is bimeasurable by Lusin–Souslin (this is where standard Borel earns its keep — the one genuinely new technical condition versus the pathwise proof).

**(iv)** Gauge: fibered relabelings transfer; the (K3)-respecting subgroup's invertibility condition becomes **backward determinism** of the belief kernel ($m^-$ a.s. measurable in $(m^+, e)$), the pathwise collapse witness ($f_M \equiv 0$, XOR gauge) transfers verbatim as a point-mass kernel, and the middle of the gauge interval stays open — same shape as pathwise.

So: **canonicity holds at kernel level, under canon's own $\kappa \equiv 0$, with one added regularity hypothesis (standard Borel) and no lumpability-lattice input.** The counterexample side (underdetermination, frozen coordinates) transfers a fortiori — deterministic systems are point-mass kernels.

## 3. The representation theorem — noise privacy is what "distributional separation" adds

The pathwise spike worked in "the structural representation" as if that were one thing. Distributionally it is not: a joint kernel has many randomized-function realizations $X^+ = f(X, e, \omega)$, differing in how the exogenous noise is *shared* between the components — and pathwise separation is a property of the realization, not the kernel. The reconciliation:

**Proposition (structural realization).** A joint kernel on $\mathcal M \times \mathcal G$ satisfies (K2)+(K3) **iff** it admits a realization

$$m^+ = f_M(m^-, e, \omega_1), \qquad g^+ = f_G(g^-, m^+, e, \omega_2), \qquad \omega_1 \perp \omega_2,$$

with *private, independent* noises. *(⇐)* is a computation: the $m$-marginal has no $g$ or $\omega_2$ path (K2 ✓), and conditionally on $m^+$, $g^+$ is driven by $(g^-, m^+, \omega_2)$ alone with $\omega_2 \perp (m^-, \omega_1)$ (K3 ✓). *(⇒)* is two applications of noise outsourcing (Kallenberg 2002, the functional-representation lemma — already the citation base of `#deriv-recursive-update`'s measure-theoretic path): realize $Q_e$ by $f_M$ with fresh $\omega_1$, then realize the conditional kernel $R_e$ by $f_G$ with fresh independent $\omega_2$; (K3) is exactly what makes $R_e$'s arguments $(g^-, m^+, e)$ suffice.

Two consequences worth their own lines:

- **A shared-noise realization of a separated kernel is possible but immaterial; a kernel *requiring* shared noise is not separated.** Concretely: if $\omega$ is genuinely shared and $f_M$ is non-invertible, then conditioning on $m^+$ leaves $\omega$ correlated with $m^-$, so $g^+ \not\perp m^- \mid (g^-, m^+)$ — (K3) fails. Distributional separation is *stronger* than "some pathwise-separated realization with common randomness": it is equivalent to "some pathwise-separated realization with **private** randomness." Noise privacy is the honest distributional content of the cascade form, and it is invisible pathwise.
- **The pathwise theorem's scope assumption is discharged.** For causally-disciplined agents, applying the pathwise theorem to any private-noise realization (which exists) gives the same canonical quotient as Theorem D, and Theorem D shows the answer is realization-independent. The two spikes' results are one result at different resolutions — *for disciplined agents.* §4 shows the qualifier is sharp.

## 4. The genuine break — no canonical belief object for goal-coupled kernels

The pathwise Corollary 5 said: when separation fails, take the congruence *closure* of the orbit partition — the finest factor coarsening it — as "the largest belief-like object," with its information gap as a structural companion to $\kappa$. Pathwise this object always exists (functions compose; congruences meet-close). Distributionally the analogous object would be the **finest lumpable coarsening of the orbit partition**, and:

**Result (no-go).** It need not exist. There is an 8-state goal-coupled agent with two *incomparable minimal* lumpable coarsenings of its goal-orbit partition.

### 4.1 Why small examples provably fail (the forcing computations — a dead end that became a lemma)

First attempts at a witness kept being *forced* into consistency, and the pattern of the forcing is itself informative:

- With **3 belief-values** and candidate partitions built as $\{m_1 m_2 \mid m_3\}$ vs $\{m_1 m_3 \mid m_2\}$: lumpability of the first forces the orbit-row differences to satisfy $d_1 + d_2 = 0,\, d_3 = 0$; the second forces $d_1 + d_3 = 0,\, d_2 = 0$; jointly $d = 0$ — the orbit partition itself becomes lumpable and there is nothing incompatible to exhibit. Row-normalization plus complement-counting closes every 3-value configuration. *(This is the distributional echo of the pathwise spike's experience: candidate counterexamples that die under forcing tell you the true witness's required structure.)*
- The forcing breaks only when the two candidate partitions have a **genuine 2×2 crossing on the target side while sharing a source block**: constraints "row-differences sum to zero over each A-block" and "over each B-block" admit a nonzero solution iff the block-intersection pattern has a nontrivial kernel — the minimal such pattern is two crossed 2+2 partitions of *four* target values, i.e. $\lvert\mathcal M\rvert = 4$.

### 4.2 The witness

$\mathcal X = \mathcal M \times \mathcal G$, $\mathcal M = \{1, 2, 3, 4\}$, $\mathcal G = \{g_1, g_2\}$; orbits $O_i = \{i\} \times \mathcal G$. One event; goal frozen ($g^+ = g^-$); belief-transition rows, given as mass into $(O_1, O_2, O_3, O_4)$ with uniform split inside each target orbit:

| State | into $O_1$ | into $O_2$ | into $O_3$ | into $O_4$ |
|---|---|---|---|---|
| $(1, g_1)$ | $3/8$ | $1/8$ | $1/8$ | $3/8$ |
| $(1, g_2)$ | $1/8$ | $3/8$ | $3/8$ | $1/8$ |
| all other six states | $1/4$ | $1/4$ | $1/4$ | $1/4$ |

- **The orbit partition is not lumpable** — the two $O_1$ rows differ (the belief-marginal depends on the goal: $\kappa \gt 0$, a Class-2/3-shaped agent; the goal biases belief-drift toward $\{O_1, O_4\}$ vs $\{O_2, O_3\}$). ✓ (This is what makes it a Corollary-5 case at all.)
- **$A = \{O_1 O_2 \mid O_3 O_4\}$ is lumpable:** every row has mass $1/2$ into each $A$-block — the $g$-bias *cancels inside each block* ($3/8 + 1/8 = 1/8 + 3/8$). ✓
- **$B = \{O_1 O_3 \mid O_2 O_4\}$ is lumpable:** same cancellation along the other pairing. ✓
- **Nothing strictly between the orbits and $A$ is lumpable:** splitting either $A$-block back into orbits re-exposes a nonzero difference ($d_1 = 1/4 \neq 0$, etc.); same for $B$. So $A$ and $B$ are each **minimal** (finest) lumpable coarsenings, and they are incomparable; their common refinement — the orbit partition — is not lumpable. ∎

Row sums, cancellations, and the between-partition checks were verified by hand; they are four one-line additions each, and the table is arranged so a verifying agent can re-run them by inspection.

### 4.3 What it means

Each candidate belief object is defined by *which axis of the goal-leak it agrees not to resolve*: $A$ cannot see the leak because it merges exactly the belief-distinctions the leak lives on along one pairing; $B$ hides it along the other. Both are honest, maximal, closed, goal-blind belief-summaries — and they are **mutually incompatible**: any object refining both would resolve the leak and thereby cease to be goal-blind. Under goal-coupling, "the agent's beliefs" distributionally is not a canonical quotient but a **choice among maximal conventions**, and the choice is substantive (the two conventions retain different information about the world). The pathwise Corollary-5 gap-measure $\iota$ proposed as a $\kappa$-companion therefore needs restating: it is well-defined only *per maximal element* (or as an interval over them), not as a single number.

For the FAST paper this is a quotable sharpening of the Class-3 story: **motivated reasoning does not merely shrink the belief object — past a point, it splinters its definition.** A Class-1 or disciplined agent has a canonical answer to "what do you believe"; a coupled agent has a *frame-relative* one, and the frames can be pairwise irreconcilable. (Stated at the strength the example licenses: existence of the phenomenon, not its genericity — see §6.)

### 4.4 The two failures are one fact

Pathwise, the congruence closure exists *per structural realization* — but a goal-coupled kernel's realizations differ in noise-sharing, and the closure computed in one realization need not match another's (the witness's correlation parameter can be wired through the shared noise in the $A$-compatible or the $B$-compatible pattern). So: distribution level — no canonical object, several maximal ones; pathwise level — an object exists but depends on the realization, i.e. on *exactly the data the kernel does not determine.* The pathwise canonicity of Corollary 5 was an artifact of fixing a representation; the distributional analysis reveals which part was real (the poset of maximal belief-conventions) and which was representational (the selection of one). *Marked honestly: the two-realizations claim in this paragraph is mechanism-level reasoning, spot-checked on the witness's structure but not exhaustively computed; flagged for the verification agent rather than asserted at derivation grade.*

## 5. Failed approaches and dead ends, recorded

1. **The inherited misdiagnosis** (§2) — the meet-closure worry aimed at scaffolding, not at the theorem. Cost: an hour of attacking lumpability lattices before asking which proof step needed them. The check that broke the frame: writing the pathwise proof's dependency list step by step.
2. **Three-value witnesses for the no-go** (§4.1) — all provably forced into consistency; productive dead end, since the forcing computation yields the minimal-structure requirement (crossed 2+2 target partitions) that generated the 8-state witness directly. A 5-orbit/10-state variant with a dedicated source orbit was built first and then compressed to 8 once the forcing analysis showed sources could double as targets.
3. **Trying to state Theorem D's part (i) as a pathwise-style commutation** $P_e \circ \iota_g = \iota_{g'} \circ P_e$ — false as stated (no deterministic $g'$ exists once the goal update is stochastic); the correct statement is the weaker marginal one, and noticing that the distributional claim *asks less* is what made the lift go through. The stronger, wrong form cost one drafting pass.
4. **Attempting to make (K3) automatic** from (K1)+(K2) via regular conditional probabilities — fails; the residual $m^-$-dependence of the conditional is precisely the noise-sharing channel, which became §3's representation theorem instead. (A failure that converted into the spike's second-best result — same pattern as the parent spike's Approaches 2–4.)

## 6. Honest edges — open after this spike

- **Genericity of the splintering.** The witness proves existence. Whether incomparable maximal belief-conventions are generic for $\kappa \gt 0$ kernels, or a measure-zero coincidence pattern (the cancellation structure is a linear-algebraic condition on row differences), is open — the right question is the dimension of the variety of kernels admitting ≥ 2 minimal lumpable coarsenings of the orbit partition. Tractable-looking; not attempted.
- **Weak lumpability as an escape.** Weak (initial-law-relative) lumpability could restore a canonical belief object *relative to a prior* — interpretively suggestive (under coupling, what counts as belief may be prior-relative), machinery exists (Rogers–Pitman intertwinings), not attempted. Flagged because the interpretive payoff for `03-llm-core/` would be large if it works.
- **$\varepsilon$-versions.** Approximate lumpability ⇒ belief kernel defined up to TV-$\varepsilon$; the natural distributional home of canon's $\varepsilon(\kappa)$ degradation norm. Shape named, nothing derived.
- **The gauge middle interval** — unchanged from the parent spike, now with "backward determinism of $Q_e$" as the distributional endpoint condition.
- **Minimality of the witness** — 8 states shown sufficient and 3 belief-values shown insufficient; whether some non-product or $\lvert\mathcal G\rvert \gt 2$ trick beats 8 states is unexamined and does not matter for anything downstream.
- **Prior-art status.** Kemeny–Snell strong lumpability, Dynkin's criterion, Rogers–Pitman, and noise outsourcing (Kallenberg) are standard and cited from working knowledge; the non-lattice behavior of lumpable partitions is, I believe, known folklore — the witness here was constructed first-hand and verified, but the folklore attribution is queued for the novelty-search agent (who is also carrying the parent spike's queue). The interpretation — maximal belief-conventions under goal-coupling and the representation-dependence tie-in — is the part I have no reason to believe exists anywhere.
