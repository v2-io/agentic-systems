---
slug: teleological-unity-uncertainty
schema_version: 1
term: teleological-unity uncertainty
name: Teleological-unity uncertainty
notation: $U_{\text{align},ji}$
brief: Agent $i$'s uncertainty about whether $j$'s communications serve $i$'s interests or $j$'s potentially conflicting objectives — uncertainty about $U_O$.
layer: prose-symbol
status: canon
tags: [composition, structural_concepts]
source_type: asf
primary_source: 01-aat-core/src/hyp-communication-gain.md
first_asf_mention: 01-aat-core/src/hyp-communication-gain.md
see_also: [communication-gain, unity-dimensions]
aliases: []
do_not_confuse:
  - "alignment uncertainty (the bare form is heavily overloaded in AI safety / alignment-with-human-values discourse — that's a different concept entirely)"
internal_note: F1 batch citability fix (2026-05-04). Bare 'alignment uncertainty' is heavily overloaded in AI safety (alignment-with-human-values, agent-alignment, etc.). The 'teleological-unity' framing connects this term to the project's unity vocabulary — it is specifically uncertainty about $U_O$ (teleological unity, the shared-objective dimension of unity_dimensions). Symbol $U_{\text{align},ji}$ retained for now; broader question of reframing all four uncertainty terms in the communication-gain formula through the unity vocabulary is queued separately in mini-lexicon-todo.
---

The fourth uncertainty term in the [communication gain](communication-gain.md) denominator $\eta_{ji}^* = U_{M_i}/(U_{M_i} + U_{o,ji} + U_{\text{src},j} + U_{\text{align},ji})$. Names agent $i$'s uncertainty about whether $j$'s communications serve $i$'s objectives or $j$'s own (potentially conflicting) objectives.

Connects directly to the project's unity vocabulary: $U_{\text{align},ji}$ is uncertainty about $U_O$ (the [teleological unity](unity-dimensions.md) dimension). High teleological-unity uncertainty drives $\eta_{ji}^* \to 0$ (ignore the signal); low teleological-unity uncertainty (high confidence in shared objectives) preserves trust. This is the game-theoretic variable in the communication-gain denominator — the channel-noise and source-quality terms are properties of the channel and source respectively; teleological-unity uncertainty is a property of the *relationship*.

The broader question of reframing all four uncertainty terms through the unity vocabulary is queued separately (see `msc/naming/mini-lexicon-todo.md`); this entry lands the prose-name change for the most-overloaded term ($U_{\text{align}}$).

Defined in [`#hyp-communication-gain`](../../01-aat-core/src/hyp-communication-gain.md).
