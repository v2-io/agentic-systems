---
slug: conditional
schema_version: 1
term: conditional
name: Conditional
brief: "An epistemic status: depends on explicitly named local assumptions that are not globally established."
layer: framing-vocabulary
status: canon
tags: [epistemic_vocabulary]
seq: 4
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [exact, robust-qualitative, hypothesis]
aliases: []
do_not_confuse: [exact, hypothesis]
---

`status: conditional` indicates that a claim holds — potentially with `exact` strength — under
explicitly named local assumptions that are not established elsewhere in the framework's dependency
chain. The conditions are stated in the segment itself (in the Epistemic Status section or via
equation-level `*[Derived (Conditional on ...)]*` tags).

The difference from `exact`: `exact` claims depend only on premises that are established by the
`depends:` chain; `conditional` claims additionally require assumptions stated locally that may or
may not hold in any given application.

The difference from `hypothesis`: a `conditional` claim is not awaiting validation — it is
provably true given its stated conditions. The uncertainty is in whether the conditions hold, not
in the derivation given the conditions.

When reviewing a segment marked `conditional`, the key question is: can the local conditions be
established from the global dependency chain? If yes, the status should be upgraded to `exact`
(with the conditions moved to `depends:`). If no, the conditions should be clearly stated and
their verification delegated to the applying context.

Defined in [`FORMAT.md`](../../FORMAT.md) §`status` — epistemic strength.
