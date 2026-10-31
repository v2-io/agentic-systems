# Integrating check 7: a membership test for reinforcement learning, and non-vacuity from fresh noise alone

KR **A.1** (`msc/inside-out-2026-10/INTENT.md`): "`#scope-adaptive-system` carries the typed predicate or a defended alternative, and a cold reader checks the membership clauses on standard RL and on a Kalman filter." Top intent (Joseph): "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." Typed record: `reviews/scope-adaptive-system-integration-7.md`. The landed edits are commits `9648363b` and `7c1dd6a3`, with wording fixes in `40754025`.

Author: Claude Opus 5.5, the A.1 round-7 integrator. Input: check 7 (`15-check-7.md`, `reviews/scope-adaptive-system-check-7.md`). I read `#scope-adaptive-system`, `#def-observation-function` and `#def-action-transition` whole at `ed2b07e4`, along with check 7's write-up and record, write-up `14` and its record, check 6's record, Proposition 1 and the Setting of `#deriv-mismatch-budget-attribution`, Proposition 3's definition of (ii′), and `NOTATION.md`'s $\theta$, $\pi_0$ and GA-1 rows. I did not read write-ups `00`–`13`. I re-derived each finding before deciding what to land; check 7's replacement texts were inputs, and the landed wording is mine.

## What changed, in brief

- **(c) opens with an exact membership test** for observed-state loops, under any $\pi_0$. It holds with the observation's law in place of the row whenever the history fixes the state. A real-reward bandit shows that in continuous worlds the declared measure settles membership and the set of possible worlds does not (check-7 F2).
- **Non-vacuity rests on fresh noise alone.** The cut paragraph now lists the users of the run-wide property correctly. The Discussion derives non-vacuity directly rather than through (g′) (check-7 F1).
- **In finite worlds $\pi_0$ is declared with full support** on the possible worlds. (h′) now states its projection step (check-7 F3). `NOTATION.md`'s $\pi_0$ row matches.
- **`#def-observation-function`** defines the kernel as the law that $h$ and the noise induce, and sends a never-changing channel memory to $\theta_h$ (check-7 F4, F5).
- **`#deriv-mismatch-budget-attribution`** Proposition 1(ii) rests its factorization on the two fresh clauses. This closes `item:deriv-mismatch-budget-attribution-1-prop-1-ii-s`.
- Smaller: (g) says "being out need not be final" (F5). The opening says where a theorem prover sits, which closes `item:readers-ask-scope-adaptive-system` (H.4).
- `#def-action-transition` needed no change.
- Wording fixes from my own review (`40754025`, classified reworded):
  - (c)'s lemma names its countable generating class as a $\pi$-system and cites Dynkin's theorem. A generating class alone does not give equality of the measures.
  - The Epistemic Status lists Ferguson's full-support result among the imported results.
  - Proposition 1's tag names the generation of the declared world by its kernels, which its derivation uses.

## 1. Non-vacuity and the run-wide property (check-7 F1)

**Re-derived.** Fix a continuation and $k \geq t$. Fresh noise says that, given $\Omega_{k+1}$, $a_k$ and the law, $o_{k+1}$ is drawn independently of everything earlier in the run. $S_{k+1} = (\Omega_{k+1}, \theta)$ holds the whole law, so $o_{k+1}$ is independent of $(S_t, S_k, \mathcal C_k)$ given $(S_{k+1}, a_k)$. Data processing then gives

$$\text{(ii′) at } o_{k+1} = I(S_{k+1}; o_{k+1} \mid \mathcal C_k, a_k) \geq I(S_t, S_k; o_{k+1} \mid \mathcal C_k, a_k) = I(S_t; o_{k+1} \mid \mathcal C_k, a_k) + r_k ,$$

where the equality is the chain rule in $(S_t, S_k)$ with $r_k$ as (g′) defines it. The chain rule over the stream, with the action terms zero (a property of policies, not of the world), sums the first terms to $I(S_t; F_t \mid \mathcal C_t)$. So the (ii′) terms after $t$ sum to at least the value plus the renewals, and fresh transitions are never used. The earlier route went through (g′)'s identity $\sum u_k = I + \sum r_k$, which does need fresh transitions. The direct route makes the result hold under a weaker premise.

**Witnesses, by hand.** In `#def-action-transition`'s XOR world at $t = 1$, the value is $\log 2$ ($o_K \oplus o_1 = x$, and $o_1$ alone is independent of $x$). Every $u_k$ and $r_k$ is zero, so (g′) fails. (h)'s step fails at $1 \lt t \lt K$, and (ii′) at $o_K$ is $H(\varepsilon_1 \mid o_1) = \log 2$, so non-vacuity holds. Check 6's remembering channel ($o_K = z_1$, nothing in the state) breaks all three. The cut paragraph now says this: a remembering transition breaks (g′) and (h), and a remembering channel breaks non-vacuity as well.

**The users of the property**, each checked against the step that drops earlier variables from a conditional law:

- (c)'s draw step and the new test, which use fresh transitions;
- (g)'s whole-target bound, through $I(S_s; o_{k+1} \mid S_k, S_t, \mathcal C_k, a_k) = 0$, which uses both clauses. The law part of (g) uses neither;
- (g′), which uses both clauses;
- (h)'s first step, which uses both;
- (h′)'s block law given $(s, \theta, c)$. Without the factorization, that law also depends on $\Omega_1$;
- the housing result's compressed state, whose predictive given $\mathcal C_t$ is a function of the posterior over $S_t$.

(b) builds its independence into its own hypotheses, so it is not on the list. The Discussion's comparison of the one-step part with (ii′) uses only fresh noise. I landed the list in the cut paragraph as check 7 proposed, with (c) added: check 7 named (c) in its list but left it out of its replacement sentence.

## 2. A membership test a cold reader can apply to reinforcement learning (check-7 F2)

**The test.** Let $o_t = \Omega_t$ through a channel the agent was given. All of $S_t$'s uncertainty given the history is about $\theta_T$. By the chain rule over the stream, with the action terms zero, the value is $\sum_{k \geq t} \mathbb E\, I(\theta; o_{k+1} \mid \mathcal C_k, a_k)$, and each term is non-negative at every history. Given $\theta$ and $\mathcal C_k$, fresh transitions make $o_{k+1}$ a draw from the row $T(\cdot \mid \Omega_k, a_k)$, which is a function of $\theta$. So the pointwise term is the information the draw carries about its row. The lemma: for $X \mid K \sim K$, $I(K; X) = 0$ iff $K$ is a.s. constant. If $I = 0$, then $X$ is independent of $K$, so $K(B) = P(X \in B \mid K) = P(X \in B)$ a.s. for every $B$ in a countable generating $\pi$-system, and $K$ is a.s. the marginal. Hence the loop is in at $t$ iff some continuation, with positive probability, takes at some $k \geq t$ an action whose row $\mathcal C_k$ does not fix. Check 7's proof is correct; I wrote my own wording for the segment.

**The twin on the other kernel**, following round 5's habit. The same argument needs only that the history fixes the state at every time. The law of $o_{k+1}$ given $(\theta, \mathcal C_k, a_k)$ is then $\int T(d\omega' \mid \Omega_k, a_k)\, p_h(\cdot \mid \omega', a_k)$, a function of $\theta$, and the lemma applies to it. For a state that moves under a known deterministic law, seen through a channel the agent was not given, that law is the channel's kernel at the next state. That loop is an instance of (e)'s passive learner of its own noise, and gets the same test. My first wording said "a known state"; the correction in `7c1dd6a3` adds the condition that the next state is fixed before the observation arrives. The state-side twin, a hidden state under a known law, has no comparably simple test, since the information is about $\Omega_t$ through later states. (b)'s $C A^j P_t \neq 0$ is its linear-Gaussian instance, and I did not invent a general form.

**Instances, now stated as consequences of the test.**

- Dirichlet rows: a row's posterior is never a point mass, so the loop is in at every $t$.
- Deterministic successor maps: one visit fixes a row. The loop is in while some continuation can reach an unvisited pair, and the exit is pointwise.
- A bandit is in while some arm's reward law is unfixed.
- Rows no continuation reaches never enter the test, as (f) says.

The value's behavior (the Clarke–Barron decay of the one-step part, the $+\infty$ value under recurrence) stays in (c) as its second half, since "Two kinds of warrant" relies on it. The entropy-difference formula is kept where it is used. The clause "and has at least two possible successors" is gone with the old argument (F5).

**The continuous case, re-derived.** Take a one-armed bandit whose observed state is its latest reward, starting from $\Omega_1 = 0$.

- Under a Dirichlet process with a full-support non-atomic base, the posterior is a Dirichlet process whose base keeps the non-atomic part. It is never a point mass, so the loop is in at every $t$.
- For the atomic declaration I used an explicit construction in place of check 7's appeal to the separability of $\mathcal P(\mathbb R)$. Enumerate the finitely supported laws with rational atoms and weights so that each recurs infinitely often, and shift the $m$-th by $\sqrt 2/m$ to get $Q_m$. The supports $\mathbb Q + \sqrt 2/m$ are disjoint, because $\sqrt 2 (1/m - 1/n)$ is irrational. The family is weakly dense: rational finitely supported laws are, and the shift moves a law by at most $\sqrt 2/m$ in the Lévy–Prokhorov metric. With $Q_m$ drawn with probability $2^{-m}$, the first reward lies in exactly one support and identifies $m$. So the loop is in at $t = 1$ and out from $t = 2$ at every history.
- Both measures have every law on $\mathbb R$ in their weak support. For the Dirichlet process this is because its marginals on finite interval partitions are Dirichlet with positive parameters (Ferguson 1973). For the atomic measure it is density.
- The two are mutually singular: a Dirichlet process with a non-atomic base charges no countable set of laws. So (h) allows them to disagree, and they do.

This is the law-side twin of (h′)'s rationals counterexample, which sits on the state side. It does not contradict anything in the segment, which already said that outside finite worlds a measure must be declared. It shows the RL reader what "not given its transition law" leaves open.

**Bearing on an open question.** `question:does-adaptive-scope-membership-depend-on-pi-0-on` asks whether membership depends on $\pi_0$ only through its support under continuity and density hypotheses. The bandit's kernels are jointly weakly continuous in state and law (the row is the law itself and does not depend on the state), and the laws have no densities. So weak continuity alone is not enough on the law side, and the question's density hypothesis is doing work. This narrows the question without answering it, so I left it open.

**Citation.** Ferguson 1973 is not in relata, and `relata candidates` did not resolve the DOI I recalled for it. I filed `item:add-ferguson-1973-a-bayesian-analysis-of-some-no` (owner A.1) beside the existing five-work relata item, rather than add a bibliographic entry from memory.

## 3. Full support and (h′)'s projection (check-7 F3)

Confirmed. $\overline W$ is closed with full measure, so $\operatorname{supp} \pi_0 \subseteq \overline W$, and equality needs $\pi_0$ to charge every open set that meets $W$. A measure on half of a finite $W$ has a smaller support, and it can change membership: two laws possible, but all the mass on one, makes the law known. So this is a requirement on the declaration. It is also the reading "possible" already asks for: a measure with a smaller support treats possible worlds as ruled out. Strengthening was not available here, because (h′) is false without the requirement. The Definition now states it, and "Whose uncertainty"'s "only through which worlds it allows" follows. In `NOTATION.md`'s $\pi_0$ row, "the closure of that set" now gives its reason, "because the declaration charges every open set that meets it". The lead approved that edit.

(h′) now has a fourth fact. The posterior over $(\Omega_t, \theta)$ is the normalized image of $L \cdot \pi_0$ under the projection that drops $\Omega_1$. On a compact space the image of the support is closed, and an open set that meets it pulls back to one that meets the support, so the image's support is the projection of the support.

## 4. `#def-observation-function` (check-7 F4, F5)

The kernel is now "the conditional law of $o_t$ given $\Omega_t = \omega$ and $a_{t-1} = a$ that $h$ and the law of $\varepsilon_t$ induce". When the agent was not built knowing it, it is $\theta_h$, and the conditional law given $(\Omega_t, a_{t-1})$ alone is a mixture over it. Without this, a cold reader holding the old definition gets the mixture, and the fresh-noise clause, which conditions on "the kernel", has nothing to refer to. The fresh-noise definition and the "Channels with memory" paragraph now send a memory that never changes along the run to $\theta_h$, by the invariance cut. A constant bias, or noise that literally repeats forever, is invariant, and the cut names it into the law. A drifting bias is state.

## 5. `#deriv-mismatch-budget-attribution`, Proposition 1(ii)

The lead approved this edit, and I claimed the segment before making it. The factorization is the sequential decomposition of the run's law. Each world factor reduces to its kernel by the matching fresh clause, and each action factor reduces to $\pi(a_s \mid \mathcal C_s)$ by (P). GA-1 and (P) alone do not give it: in the XOR world a world factor depends on $\varepsilon_1$, and GA-1 permits that. The derivation now says this and cites the two definitions. On the item's second point: the Setting already defines $\Omega := S_t$ (since `782ac22e`), so the GA-1 line was in the typed form. The item read it as state-only, and a cold reader could too, so I added one sentence saying it conditions on the law as well as the state. I closed the item by `9648363b`.

## 6. The ledger

- **Revisions.** `#scope-adaptive-system` and `#def-observation-function` are revised as redefined: (c) gains a test, the Definition gains a requirement, and the kernel's definition changes. `#deriv-mismatch-budget-attribution` had no check resting on it, so there was nothing to classify.
- **Closed by commit:** `item:deriv-mismatch-budget-attribution-1-prop-1-ii-s` and `item:readers-ask-scope-adaptive-system`, both by `9648363b`. The second is H.4's item, and its whole content was the prover half-sentence. I also deleted that item's "a half-sentence might forestall the question" line from the segment's Working Notes, since the body now carries the half-sentence.
- **Opened:** `item:add-ferguson-1973-a-bayesian-analysis-of-some-no` (A.1).
- **Not disposed, and why.** Check 6's open findings (C5/finding, C7/finding, F2, F3, F4) are each answered by `ed2b07e4`, which I did not author. I re-read each against that text. C5/finding: the cut paragraph names the generation by kernels, and both clauses are defined. C7/finding: the Epistemic Status gives the own-policy statement and its witness. F2: (g)'s example reads "out before $K - 1$ and in from $K - 1$". F3: (c) carries reward-in-state and the Dirichlet as $\pi_0$, and round 7 keeps both. F4: the law row is reachability-qualified, the row says "closure", "almost surely" names its measure, and the topology is scoped to the finite case. `vsect findings --answered … --by-revision 55f592c5` refused all five, because I am now the *last* reviser of the segment. vsect checks who revised the segment last, not who authored the answering revision. I should have disposed of them before my own revise; the next checker can. Tool feedback: the rule's intent, "someone other than the reviser", is about the answering revision. Checking the last reviser instead blocks a legitimate second mind whenever it also edits the segment in the same round. Check 7's findings answer to my revisions and are for a different mind.
- **Check 7's lapsed checks** (C1–C5, C9: "upstream changed (segment:def-chronica)") are a recording artifact. Check 7 says it read `#def-chronica` at `c0d9c504`, and recorded its checks `at: ed2b07e4`. `c0d9c504` (17:21:32) is not an ancestor of `ed2b07e4` (17:20:20), so vsect bound the checks to the older `#def-chronica` and lapsed them at the newer one, the one actually read. My revisions lapse them anyway. The next checker does not need to re-check `#def-chronica` on that account.

## What I did not do

- **The four open items** (the tail-$\sigma$-field strengthening, the physical housing, the compute-relative extension, the four-term decomposition). I looked at the housing criterion long enough to see that testing it means saying what a re-description must preserve under a sensor intervention. That is a model of interventions on the twin, not a short computation, and so it is spike-sized, as its item says. I did not start any of them. Each still has its item, and none is affected by this round.
- I did not re-derive the Clarke–Barron constant or the Kalman numbers, which checks 6 and 7 both confirmed and this round did not touch.
- I did not grep the corpus for readers of the observation kernel's old literal definition.
- I did not check Ferguson 1973 against the paper. The weak-support argument in the segment is self-contained, and the citation is a pointer.

## On the brief

The brief gave the KR, the coordination facts and the choices, and left the rest open, which fit the work. Its sentence "If you need to edit outside your three segments, `NOTATION.md` and `#deriv-mismatch-budget-attribution`, tell me first" can be read two ways: either the two files are the outside edits it anticipates, or they are examples of "outside". I took the narrower reading and asked, and the lead's answer settled it. One process note for the next integrator: dispose of the previous round's findings before running your own `vsect revise`, or vsect will refuse you as the reviser.
