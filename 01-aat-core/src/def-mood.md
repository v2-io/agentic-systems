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

where $K$ is the update gain (`emp-update-gain`), $\mathcal{T} = \nu \cdot K$ the adaptive tempo (`def-adaptive-tempo`), and $g : \mathbb{R} \to [g_{\min}, g_{\max}]$ ($0 \lt g_{\min} \leq 1 \leq g_{\max}$) a monotone *bounded* modulation, the band chosen so the modulated gain stays inside the sector-validity region and, in discrete time, under the step-size ceiling of `der-gain-sector-bridge`: sustained adverse surprise raises gain and tempo (re-posture for a suspected regime shift); sustained easy tracking relaxes them — but only down to the floor $g_{\min}$. The band is not decoration; both ends carry persistence content (see Discussion).

Because $\tau$ is slow, the fast $M_t$ dynamics see $m_t$ as quasi-static: mood is a **second-order** adaptation parameter — adaptation acting on the gain of adaptation — sitting one rung above the endogenous single-step gain dynamics of `deriv-adaptive-gain-dynamics`.

## Epistemic Status

This segment is a **definition**, not a truth-claim; its content is the construct, not a derivation. The construct is adopted from affective science (Eldar et al. 2016, mood as outcome-momentum; Bennett et al. 2022, mood as a leaky integral of advantage) and specialized to the pre-goal adaptation setting, where the integrated quantity is tracking-surprise rather than reward. The framing is `discussion-grade`: the functional skeleton is well-supported qualitatively, but the specific functional forms of $a_t$ and $g$ are representative, not pinned.

The load-bearing reason this belongs in Part I — *before* objectives — is that nothing in the construct references $O_t$, $\Sigma_t$, or reward. Mood's signed reading as *valued* momentum (approach/avoid, hedonic sign) and its modulation of exploration and risk posture are genuine additions that arrive only once objectives exist; those are deferred to the actuation half (Part II) and depend on this definition, not the reverse.

The optimal mood time-constant — optimal *for mood's regime-estimator role*; the transfer to the modulator role ($m_t$ setting $K_t$) is conjectured equal and remains an open item — is derived in `#der-mood-timescale`: minimizing steady-state regime-tracking error gives $\tau^\ast = \sqrt{\tau_{\mathrm{env}}\, r/(2\sigma_\theta^2)}$ — growing as the *square root* of the environment's autocorrelation time (not matching it), with a robust-qualitative core (interior optimum; too-fast mood chases noise, too-slow mood lags the regime). That companion carries the `conditional` result and its premises; this definition remains `discussion-grade` as the construct.

## Discussion

Mood is the slow outer loop on the persistence condition (`result-persistence-condition`). In the bathtub reading of persistence — faucet as the rate of change in reality, drain as the learning rate, overflow when the faucet outpaces the drain — mood is a slow controller *on the drain*: it widens the drain when recent overflow-risk has run high and relaxes it when tracking has been easy. The framework otherwise has fast per-channel updating and (in Part II) goal dynamics, but no slow global scalar coordinating posture across channels; mood is that missing object.

**Persistence compatibility (the MG discharge).** Mood's modulation composes with the persistence machinery as an instance of `deriv-adaptive-gain-dynamics`'s adaptive-gain result, and the four conditions instantiate cleanly. **(MG-1)** is the $[g_{\min}, g_{\max}]$ band in the definition: the floor keeps the effective sector rate uniformly above the persistence threshold ($\alpha_t \geq \alpha_{\min} \gt \rho/R$; the primary-channel Lyapunov argument is pointwise in time, so no slow-variation hypothesis is needed on this leg). The floor is what excludes **mood-induced complacency** — the failure mode an unbounded downward relaxation would permit, where sustained easy tracking drives correction power toward zero just in time for the next regime shift; the ceiling is the mirror condition, keeping adverse-surprise gain-raising under the discrete-time contraction ceiling. **(MG-2)** is trivial for mood: the channel is a *linear* leaky integrator, sector constant exactly $\lambda$. **(MG-3)** is the quantitative content of "quasi-static": $\lambda \ll \underline\alpha$ — mood adapts slower than the primary state contracts. **(MG-4)** requires the surprise summary to have $\delta$-bounded second moment, $\mathbb{E}[a_t^2 \mid \delta] \leq \sigma_0^2 + c_a\lVert\delta\rVert^2$ — a condition stated here because $a_t$'s functional form is deliberately unpinned; any concrete choice should be checked against it. Under the four, the composed augmented-state persistence result applies as-is and mood sits in sub-scope $\alpha_2$ — a notably clean instance (the meta-channel is linear).

Mood couples the channels globally, which appears to threaten the directed-separation structure (`der-directed-separation`). It does not, and the reason is now quantitative rather than asserted: the separation condition is (MG-3) above — $m_t$ moves slowly enough ($\lambda \ll \underline\alpha$) that the fast dynamics treat it as a constant, so separation holds at the timescale that matters even though a coupling exists in absolute terms. Mood is thus a clean worked example of bounded, separation-preserving coupling — adjacent to the Class 2 (Partial) material rather than a violation of Class 1.

The applied and normative reading of mood — set-point, recovery, what propagates across a context boundary, and the ethics of mood-control for persistent agents — is deliberately kept out of this segment; it lives in `msc/mood-layer-sovereignty-carve-2026-06-17.md`. Here mood is only a formal modulator of adaptation.

## Working Notes

- **Discharged 2026-06-17 — optimal time-constant (F2).** Landed as `#der-mood-timescale` (`conditional`): the strong "$\tau^\ast$ matches the autocorrelation timescale" was refuted and replaced by the derived $\tau^\ast = \sqrt{\tau_{\mathrm{env}}\, r/(2\sigma_\theta^2)}$ scaling law, independently refute-verified. The emotional-inertia signature (Kuppens et al. 2010 — inertia as the affect AR(1) coefficient $1-\lambda$, maladaptive when high $\Leftrightarrow$ $\tau \gg \tau^\ast$) is its clinical corroboration. Reasoning trail: `spikes/spike-mood-timescale-matching-2026-06-17.md`.
- **Pre-goal volatility link (unverified).** The integrated quantity $a_t$ plausibly connects to volatility-driven learning-rate control (Behrens-style). Verify the citation before using it; if it holds it independently supports the Part I (pre-goal) placement.
- **Part II enrichment.** A companion actuation-side segment should carry the signed/valued momentum reading and the exploration/risk modulation, depending on this one.
