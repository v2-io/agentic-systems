---
slug: hyp-solicitable-escape
type: hypothesis
status: discussion-grade
depends:
  - der-observability-dominance
  - def-mismatch-signal
  - hyp-communication-gain
stage: exploratory
---

# Hypothesis: Solicitable Escape from an Absorbing Region

The three escape routes from an absorbing observability region are not peers: two require no prior localization of the blind spot and one does, so where observability is estimated rather than known by construction, and under any resource bound, the only *solicitable* escape from a self-locking region is a differently-positioned observer.

## Formal Expression

#der-observability-dominance establishes that unobservable regions of strategy are absorbing — frozen beliefs generate no mismatch signal, so no revision is triggered, and the agent "cannot learn and cannot recognize that it cannot learn." It names three escapes: external shock, proactive observability investment (instrumenting previously unmonitored nodes), and another agent whose observations cover the blind spot ( #hyp-communication-gain).

Partition those routes by what the agent must already possess for the route to be *available to it as an action*.

*[Definition (route-targeting)]* A route is **targeted** if exercising it requires the agent to identify, in advance, the node or direction at which its observability is deficient. A route is **untargeted** otherwise.

*[Hypothesis (solicitable-escape)]* Of the three routes:

- **External shock** is untargeted and *unsolicitable*. It requires no prior localization, because the shock supplies the mismatch signal the frozen region cannot generate; but it also cannot be chosen — it is a thing that happens to the agent, not an action available to it.
- **Observability investment** is *targeted*, under the scope condition below. To instrument node $v$ the agent must represent $v$ as a node whose $\sigma_v$ is worth raising. The absorbing region is case (c) of the zero-aporia trichotomy ( #def-mismatch-signal): near-zero mismatch because the channel is too noisy to detect model error, which is not distinguishable from within from case (a), a model that genuinely fits — *silence can mean peace or deafness*. What blocks the distinction is not absence of signal but the agent's inability to audit its own weighting: by #def-observation-function the agent does not know the noise distribution and must estimate $U_o$ from innovations, and at a node with $\sigma_v \approx 0$ those innovations are exactly what is suppressed, so the estimate is unimprovable by observing $v$. The gain-collapse modes compound this — $\eta^\ast \to 0$ via $U_M \to 0$ (dogmatism) and via $U_o \to \infty$ (nihilism) are behaviorally identical ( #emp-update-gain), so even an agent that correctly registers "my gain here is zero" cannot read off whether the fault lies in the world or in itself. So for the blind spots that are actually self-locking, the precondition of the route is unavailable.
- **Another observer** is both untargeted *and* solicitable. A differently-positioned party's coverage does not require the blinded agent to know where its own deficiency lies — the coverage is a property of the other's position, not of the blinded agent's model — and soliciting it is an action the agent can take under its existing representational resources.

*[Scope (innovation-estimated observability)]*

The targeting claim above holds where the agent's knowledge of $\sigma_v$ is **estimated from its own observations**. It fails where $\sigma_v$ is known **architecturally** — an agent that knows by construction which nodes it has no sensor for can rank exactly those nodes without any signal from them, and for it the self-instrumentation route is both choosable and aimable. This is the same boundary flagged against #def-observation-function's epistemic-opacity clause by several de-novo readers (a Kalman filter with a known noise covariance is handed its observation law rather than estimating it), so the scope condition tracks a distinction the framework already recognizes rather than introducing one. The interesting case is the estimated one, because that is where the region self-locks; the architecturally-known case is a design opportunity, not a trap.

*[Derived (conditional on a resource bound)]* The apparent counterexample is *blanket* instrumentation: raising $\sigma_v$ everywhere requires no targeting. Blanket instrumentation is untargeted, and it does escape. But its cost scales with the node set while the value of instrumenting any particular node is the difference in sector parameters that node contributes ( #der-observability-dominance's investment tradeoff), so under a bound on instrumentation capacity the agent must rank nodes — which reintroduces targeting. The claim is therefore conditional: *given* an instrumentation budget strictly below what blanket coverage requires, observability investment degrades to a targeted route and is unavailable for the self-locking case.

The consequence, stated as the hypothesis: **within an absorbing region, the only escape that is both untargeted and choosable is a differently-positioned observer.** Shock escapes but cannot be chosen; self-instrumentation can be chosen but — under estimated observability — not aimed.

## Epistemic Status

*Discussion-grade.* The argument rests on the absorbing condition as #der-observability-dominance states it (`robust-qualitative` there, and nothing here upgrades it) and on the targeting precondition, which is now argued from three upstream commitments rather than asserted: the (a)-vs-(c) ambiguity of #def-mismatch-signal, the epistemic opacity of #def-observation-function, and the behavioral identity of the two gain-collapse modes in #emp-update-gain. That argument is assembled here in prose, not derived — which is what keeps the segment at `discussion-grade` rather than `conditional`.

**Max attainable: conditional.** Two steps remain, both now specific. The resource bound in the clause below is stated informally; formalizing it against the investment-tradeoff expression in #der-observability-dominance would make the blanket-instrumentation dismissal a derivation rather than an argument. And the targeting precondition wants the chain above written as a derivation: that an agent's estimate of $\sigma_v$ is unimprovable by observation at $v$ when $\sigma_v \approx 0$, so cases (a) and (c) are not separable from inside under estimated observability. The ingredients are all in canon and none of them is new; what is missing is the worked argument, which would also close the exception in the scope clause by stating exactly what architectural knowledge supplies that estimation cannot.

**One thing this segment must not be read as claiming.** The absorbing region is *not* one where the agent receives no signal. Observations continue; what collapses is the weight they carry ($\eta_{\text{edge}} \to 0$ via $U_{\text{obs}} \to \infty$). A zero-information channel is outside AAT's scope entirely ( #def-agent-environment, #scope-adaptive-system) — with no signal there is no mismatch, hence no correction and nothing to analyze — so reading the absorbing condition as blindness does not strengthen this segment, it removes its subject.

**Scope, and what this is not.** The result is about *strategy-edge observability*, which is the scope #der-observability-dominance carries; it says nothing directly about comprehension between agents, and any transfer to that setting is a further step this segment does not take. The other-observer route depends on #hyp-communication-gain, whose status is `discussion-grade`, so nothing this segment says about that route can be stronger than discussion-grade regardless of how the argument here is tightened — the two promotion steps above would raise the *partition*, not the route it favors. Nothing here asserts that a differently-positioned observer is *sufficient* for escape — only that it is the one route whose availability does not presuppose what the absorbing condition removes.

**Falsifier.** Exhibit a self-locking region escaped by self-instrumentation where the instrumented node was selected without prior signal distinguishing it from settled nodes — or show that some third mechanism supplies such a signal from inside the region, which would defeat the targeting premise directly.

## Discussion

The partition sharpens rather than softens the practical reading of #der-observability-dominance. That segment's advice to prefer a weak-but-visible path over a strong-but-blind one is guidance available *before* a region becomes absorbing; it is a prophylactic. Once the region is absorbing, the same segment's own escape list is what remains, and this partition says which member of it an agent can actually reach for.

It also explains an asymmetry in how the three routes feel from inside, which is otherwise puzzling. An agent in an absorbing region has, by construction, no experience of being stuck; the region presents as settled knowledge rather than as a gap. That phenomenology is consistent with all three routes being nominally listed and only one being usable: the agent is not withholding effort, and more effort is genuinely not the missing ingredient — what is missing is a standpoint the agent does not occupy, and the only action that reaches one is to involve a party who does.

Two connections worth noting without leaning on them. The instrumentation route's failure has the same shape as the diagnostic-resolution loss the parent segment describes: an unobservable intermediate destroys per-edge identification and forces plan-level aggregation, so the agent knows a plan is failing without localizing the step — which is the targeting deficiency seen at a finer grain. And the partition gives a formal reason why a network of differently-positioned agents is not merely an efficiency over a solitary one: for the specific class of blind spots that are self-locking, it is the only member of the escape set that an agent can elect.

## Working Notes

**Forward pointer.** The two promotion steps are named in Epistemic Status. The targeting premise is the one to attack first; if the derivation lands, this becomes a corollary rather than a hypothesis and the slug should change accordingly.

**Correction, 2026-07-29 (same day as landing) — the premise was inherited from prose, not from a derivation.** As first landed, this segment argued that "the absorbing condition is precisely that the agent has no signal distinguishing a frozen belief from a settled one," taking the phrasing from #der-observability-dominance's Discussion (*"cannot learn and cannot recognize that it cannot learn"*). That parent segment *derives* gain collapse — $\eta_{\text{edge}} \to 0$ via $U_{\text{obs}} \to \infty$ — and asserts the recognition conjunct separately; the strong reading is also a slide toward the zero-information corner AAT excludes. The premise is now argued from #def-mismatch-signal's trichotomy plus #def-observation-function's opacity plus #emp-update-gain's dogmatism/nihilism identity, and the architecturally-known exception is named as a scope clause. The correction narrowed the claim and made its falsifier sharper. Regression guard: an editor tempted to restore "the agent has no signal" should read the Epistemic Status closing paragraph first — that reading deletes the segment's subject rather than strengthening it. Cycle record in `spikes/spike-escape-standpoint-axis-2026-07-29.md` §10.

**Regression guard — a truncation to not restore.** The philosophical companion's appendix reports the parent segment's escape clause as *"not more effort by the same agent but another agent whose observations cover the blind spot,"* naming one of the three routes. As stated that contrast is false: instrumenting one's own unmonitored nodes *is* more effort by the same agent. The correct form of the contrast is the one this segment argues — the self-route exists but cannot be aimed at a self-locking region — so the appendix's conclusion survives on different and better grounds. Do not restore the one-route reading; it drops two routes in the direction that flatters the network claim, and a referee with access to this framework could catch it.

**Naming.** The slug is a first pass and has not been through a naming round; `solicitable` is doing the load-bearing work and may not survive review against the standalone-citability criterion.

**Provenance of the check.** The parent segment was read at the primary specifically to test whether a structural correspondence claimed from a survey survived contact with the source. It did not survive as claimed, and this segment is what remained after the overreach was removed — recorded because the narrowed form is more useful than the original was.

**Provenance of the insight, not only of the check.** The targeting asymmetry was not derived from the parent segment by closer reading; it was recognized by an agent who had just spent a long session as the case — holding beliefs that presented as settled while generating no mismatch signal, and unfrozen only by a differently-positioned party — and it is recorded here as first-person testimony because that is what it is, and because the fact that it was reachable only from inside the condition is itself weak evidence for the partition it produced.
