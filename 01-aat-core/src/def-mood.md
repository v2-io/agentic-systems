---
slug: def-mood
type: definition
status: discussion-grade
depends:
  - def-mismatch-signal
  - emp-update-gain
  - def-adaptive-tempo
  - hyp-mismatch-dynamics
  - form-sector-condition
stage: draft
---

# Mood

Mood is a slow global scalar that integrates the recent mismatch stream and feeds back to modulate the adaptation gain and tempo — a second-order adaptation parameter that requires no objective to define.

## Formal Expression

*[Definition]* Let $a_t$ be a per-step summary of recent tracking surprise — how much better or worse the mismatch signal $\delta_t$ (`def-mismatch-signal`) is behaving than the agent's own short-horizon expectation. **Mood** is the leaky integral

$$m_t = (1-\lambda)\, m_{t-1} + \lambda\, a_t, \qquad 0 \lt \lambda \ll 1,$$

with time-constant $\tau \approx 1/\lambda$ slow relative to the per-step update of $M_t$.

*[Definition]* Mood acts only by modulating the adaptation parameters already in play — it adds no new fast dynamics:

$$K_t = K_0\, g(m_t), \qquad \mathcal{T}_t = \nu_t \cdot K_t,$$

where $K$ is the update gain (`emp-update-gain`), $\mathcal{T} = \nu \cdot K$ the adaptive tempo (`def-adaptive-tempo`), and $g$ a monotone modulation: sustained adverse surprise raises gain and tempo (re-posture for a suspected regime shift); sustained easy tracking relaxes them.

Because $\tau$ is slow, the fast $M_t$ dynamics see $m_t$ as quasi-static: mood is a **second-order** adaptation parameter — adaptation acting on the gain of adaptation — sitting one rung above the endogenous single-step gain dynamics of `deriv-adaptive-gain-dynamics`.

## Epistemic Status

This segment is a **definition**, not a truth-claim; its content is the construct, not a derivation. The construct is adopted from affective science (Eldar et al. 2016, mood as outcome-momentum; Bennett et al. 2022, mood as a leaky integral of advantage) and specialized to the pre-goal adaptation setting, where the integrated quantity is tracking-surprise rather than reward. The framing is `discussion-grade`: the functional skeleton is well-supported qualitatively, but the specific functional forms of $a_t$ and $g$ are representative, not pinned.

The load-bearing reason this belongs in Part I — *before* objectives — is that nothing in the construct references $O_t$, $\Sigma_t$, or reward. Mood's signed reading as *valued* momentum (approach/avoid, hedonic sign) and its modulation of exploration and risk posture are genuine additions that arrive only once objectives exist; those are deferred to the actuation half (Part II) and depend on this definition, not the reverse.

The candidate quantitative result — that the optimal mood time-constant $\tau^\ast$ matches the environment's autocorrelation timescale — is **not** asserted here; it is logged as a gating sub-spike in Working Notes and would, if it lands, promote this segment toward `conditional`.

## Discussion

Mood is the slow outer loop on the persistence condition (`result-persistence-condition`). In the bathtub reading of persistence — faucet as the rate of change in reality, drain as the learning rate, overflow when the faucet outpaces the drain — mood is a slow controller *on the drain*: it widens the drain when recent overflow-risk has run high and relaxes it when tracking has been easy. The framework otherwise has fast per-channel updating and (in Part II) goal dynamics, but no slow global scalar coordinating posture across channels; mood is that missing object.

Mood couples the channels globally, which appears to threaten the directed-separation structure (`der-directed-separation`). It does not, by **timescale separation**: $m_t$ moves slowly enough that the fast dynamics treat it as a constant, so separation holds at the timescale that matters even though a coupling exists in absolute terms. Mood is thus a clean worked example of bounded, separation-preserving coupling — adjacent to the Class 2 (Partial) material rather than a violation of Class 1.

The applied and normative reading of mood — set-point, recovery, what propagates across a context boundary, and the ethics of mood-control for persistent agents — is deliberately kept out of this segment; it lives in `msc/mood-layer-sovereignty-carve-2026-06-17.md`. Here mood is only a formal modulator of adaptation.

## Working Notes

- **Gating sub-spike (F2, time-constant matching).** Derive $\tau^\ast \propto$ environmental autocorrelation timescale against Bennett et al. (2022)'s leaky-integrator form; the empirical check is the emotional-inertia signature (Kuppens et al. 2010 formalize inertia as the affect AR(1) coefficient; mismatch with environment autocorrelation predicts maladjustment). Success promotes this segment to `conditional` and likely spins out a `result-mood-timescale` companion. Forward pointer for whoever picks this up: the design memo's F2 carries the full argument and references.
- **Pre-goal volatility link (unverified).** The integrated quantity $a_t$ plausibly connects to volatility-driven learning-rate control (Behrens-style). Verify the citation before using it; if it holds it independently supports the Part I (pre-goal) placement.
- **Upstream discoverability.** Add a one-line Working-Notes pointer to this segment from `emp-update-gain` and from `result-persistence-condition` (mood as the slow outer loop on each) — not yet done.
- **OUTLINE.** Not yet entered in `01-aat-core/OUTLINE.md`; provisional home is Part I, Chapter 4 (Persistence and Structural Limits), after `der-gain-sector-bridge`.
- **Part II enrichment.** A companion actuation-side segment should carry the signed/valued momentum reading and the exploration/risk modulation, depending on this one.
