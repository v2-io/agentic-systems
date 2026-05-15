---
slug: regime-typed-effective-disturbance
schema_version: 1
term: regime-typed effective disturbance
name: Regime-typed effective disturbance
notation: $\rho_B^{\text{eff}}$
brief: AAT-distinctive decomposition of recipient-side effective disturbance rate by regime — Informative (negative), magnitude-shock, structural-shock, ambient-noise — with three independent boundaries in AAT-native quantities.
layer: prose-symbol
status: canon
tags: [composition, structural_concepts, core_quantities]
source_type: asf
primary_source: 01-aat-core/src/der-interaction-channel-classification.md
first_asf_mention: 01-aat-core/src/der-interaction-channel-classification.md
see_also: [communication-gain, adversarial-destabilization]
aliases: ["effective disturbance (when regime-typed decomposition is in scope)"]
do_not_confuse:
  - "effective disturbance (bare control-theory term — robust control, disturbance-rejection literature; AAT-generic, not the regime-typed decomposition)"
internal_note: F1 batch citability fix (2026-05-04). Bare 'effective disturbance' is heavy in robust-control / disturbance-rejection literature; the 'regime-typed' qualifier names the AAT-distinctive content (regime decomposition with signed Regime-I term).
---

The recipient-side decomposition of effective disturbance rate by regime, where each regime is defined by an event's relationship to the recipient's model class, observability floor, and correction capacity:

- **Regime I** (Informative): events that contribute *negatively* to $\rho_B^{\text{eff}}$ — cooperative events, well-calibrated signals, learning opportunities. The sign-flip from the standard control-theory positive-only "effective disturbance" framing is the key AAT-distinctive content.
- **Regime II-a** (magnitude-shock): events whose magnitude exceeds the recipient's correction-capacity per cycle.
- **Regime II-b** (structural-shock): events outside the recipient's model class, contributing the structural mismatch floor.
- **Regime III** (ambient-noise): events below the observability floor, contributing through ambient variance.

The compound decomposition is:

$$\rho_B^{\text{eff}} = \underbrace{\sum_{\text{II-a}}}_{\text{magnitude}} + \underbrace{\sum_{\text{II-b}}}_{\text{structural floor}} + \underbrace{\sum_{\text{III}}}_{\text{ambient}} - \underbrace{\sum_{\text{I}}}_{\text{informative correction}}$$

Three independent boundaries (I-a, I-b, I-c) in AAT-native quantities define the regime classification — see [`#der-interaction-channel-classification`](../../01-aat-core/src/der-interaction-channel-classification.md).

The bare term *effective disturbance* (without the regime-typed qualifier) remains the standard control-theory handle and is correctly used in segments where the AAT-internal regime decomposition is not in scope (e.g., generic Lyapunov persistence statements, cross-domain transfer discussions).
