---
slug: communication-gain
schema_version: 1
term: communication gain
name: Communication gain
notation: "$\\eta_{ji}^\\ast$"
brief: Trust-weighted uncertainty ratio for inter-agent channels.
layer: prose-symbol
status: canon
tags: [structural_concepts, composition]
source_type: asf
primary_source: 01-aad-core/src/hyp-communication-gain.md
first_asf_mention: 01-aad-core/src/hyp-communication-gain.md
see_also: [update-gain, unity-dimensions, composition-threshold]
aliases: []
do_not_confuse: []
---

The optimal weight agent $i$ should apply to information received from agent
$j$. Extends the single-agent [update gain](update-gain.md) with three
additional uncertainty terms — channel noise $U_{o,ji}$, source-quality
uncertainty $U_{\text{src},j}$, and alignment uncertainty $U_{\text{align},ji}$
— so that perfect-channel/perfectly-aligned sources recover full trust
($\eta_{ji}^\ast \to 1$) while noisy or misaligned sources are appropriately
discounted ($\eta_{ji}^\ast \to 0$). Specializes to the standard update gain
when $j$ is the environment.

Hypothesized in
[`#hyp-communication-gain`](../../01-aad-core/src/hyp-communication-gain.md).
