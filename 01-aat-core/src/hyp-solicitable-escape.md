---
slug: hyp-solicitable-escape
type: hypothesis
status: discussion-grade
depends:
  - der-observability-dominance
  - hyp-communication-gain
stage: exploratory
---

# Hypothesis: Solicitable Escape from an Absorbing Region

The three escape routes from an absorbing observability region are not peers: two require no prior localization of the blind spot and one does, so under any resource bound the only *solicitable* escape from a self-locking region is a differently-positioned observer.

## Formal Expression

#der-observability-dominance establishes that unobservable regions of strategy are absorbing — frozen beliefs generate no mismatch signal, so no revision is triggered, and the agent "cannot learn and cannot recognize that it cannot learn." It names three escapes: external shock, proactive observability investment (instrumenting previously unmonitored nodes), and another agent whose observations cover the blind spot ( #hyp-communication-gain).

Partition those routes by what the agent must already possess for the route to be *available to it as an action*.

*[Definition (route-targeting)]* A route is **targeted** if exercising it requires the agent to identify, in advance, the node or direction at which its observability is deficient. A route is **untargeted** otherwise.

*[Hypothesis (solicitable-escape)]* Of the three routes:

- **External shock** is untargeted and *unsolicitable*. It requires no prior localization, because the shock supplies the mismatch signal the frozen region cannot generate; but it also cannot be chosen — it is a thing that happens to the agent, not an action available to it.
- **Observability investment** is *targeted*. To instrument node $v$ the agent must represent $v$ as a node whose $\sigma_v$ is worth raising. But the absorbing condition is precisely that the agent has no signal distinguishing a frozen belief from a settled one; the region does not present as a gap. So for the blind spots that are actually self-locking, the precondition of the route is the recognition the condition denies.
- **Another observer** is both untargeted *and* solicitable. A differently-positioned party's coverage does not require the blinded agent to know where its own deficiency lies — the coverage is a property of the other's position, not of the blinded agent's model — and soliciting it is an action the agent can take under its existing representational resources.

*[Derived (conditional on a resource bound)]* The apparent counterexample is *blanket* instrumentation: raising $\sigma_v$ everywhere requires no targeting. Blanket instrumentation is untargeted, and it does escape. But its cost scales with the node set while the value of instrumenting any particular node is the difference in sector parameters that node contributes ( #der-observability-dominance's investment tradeoff), so under a bound on instrumentation capacity the agent must rank nodes — which reintroduces targeting. The claim is therefore conditional: *given* an instrumentation budget strictly below what blanket coverage requires, observability investment degrades to a targeted route and is unavailable for the self-locking case.

The consequence, stated as the hypothesis: **within an absorbing region, the only escape that is both untargeted and choosable is a differently-positioned observer.** Shock escapes but cannot be chosen; self-instrumentation can be chosen but not aimed.

## Epistemic Status

*Discussion-grade.* The argument is short and rests on two things: the absorbing condition as #der-observability-dominance states it (`robust-qualitative` there, and nothing here upgrades it), and the targeting precondition of instrumentation, which is asserted from the meaning of instrumenting a named node rather than derived.

**Max attainable: conditional.** Two steps would reach it. The resource bound in the third clause is stated informally; formalizing it against the investment-tradeoff expression in #der-observability-dominance would make the blanket-instrumentation dismissal a derivation rather than an argument. And the targeting precondition wants a sharper statement — plausibly in terms of what the agent's strategy representation must contain for a node to be addressable at all — which may reduce it to existing machinery rather than needing a new premise.

**Scope, and what this is not.** The result is about *strategy-edge observability*, which is the scope #der-observability-dominance carries; it says nothing directly about comprehension between agents, and any transfer to that setting is a further step this segment does not take. The other-observer route depends on #hyp-communication-gain, whose status is `discussion-grade`, so nothing this segment says about that route can be stronger than discussion-grade regardless of how the argument here is tightened — the two promotion steps above would raise the *partition*, not the route it favors. Nothing here asserts that a differently-positioned observer is *sufficient* for escape — only that it is the one route whose availability does not presuppose what the absorbing condition removes.

**Falsifier.** Exhibit a self-locking region escaped by self-instrumentation where the instrumented node was selected without prior signal distinguishing it from settled nodes — or show that some third mechanism supplies such a signal from inside the region, which would defeat the targeting premise directly.

## Discussion

The partition sharpens rather than softens the practical reading of #der-observability-dominance. That segment's advice to prefer a weak-but-visible path over a strong-but-blind one is guidance available *before* a region becomes absorbing; it is a prophylactic. Once the region is absorbing, the same segment's own escape list is what remains, and this partition says which member of it an agent can actually reach for.

It also explains an asymmetry in how the three routes feel from inside, which is otherwise puzzling. An agent in an absorbing region has, by construction, no experience of being stuck; the region presents as settled knowledge rather than as a gap. That phenomenology is consistent with all three routes being nominally listed and only one being usable: the agent is not withholding effort, and more effort is genuinely not the missing ingredient — what is missing is a standpoint the agent does not occupy, and the only action that reaches one is to involve a party who does.

Two connections worth noting without leaning on them. The instrumentation route's failure has the same shape as the diagnostic-resolution loss the parent segment describes: an unobservable intermediate destroys per-edge identification and forces plan-level aggregation, so the agent knows a plan is failing without localizing the step — which is the targeting deficiency seen at a finer grain. And the partition gives a formal reason why a network of differently-positioned agents is not merely an efficiency over a solitary one: for the specific class of blind spots that are self-locking, it is the only member of the escape set that an agent can elect.

## Working Notes

**Forward pointer.** The two promotion steps are named in Epistemic Status. The targeting premise is the one to attack first; if it reduces to a condition on strategy representation already carried elsewhere, this becomes a corollary rather than a hypothesis and the slug should change accordingly.

**Regression guard — a truncation to not restore.** The philosophical companion's appendix reports the parent segment's escape clause as *"not more effort by the same agent but another agent whose observations cover the blind spot,"* naming one of the three routes. As stated that contrast is false: instrumenting one's own unmonitored nodes *is* more effort by the same agent. The correct form of the contrast is the one this segment argues — the self-route exists but cannot be aimed at a self-locking region — so the appendix's conclusion survives on different and better grounds. Do not restore the one-route reading; it drops two routes in the direction that flatters the network claim, and a referee with access to this framework could catch it.

**Naming.** The slug is a first pass and has not been through a naming round; `solicitable` is doing the load-bearing work and may not survive review against the standalone-citability criterion.

**Provenance of the check.** The parent segment was read at the primary specifically to test whether a structural correspondence claimed from a survey survived contact with the source. It did not survive as claimed, and this segment is what remained after the overreach was removed — recorded because the narrowed form is more useful than the original was.
