# Spike: prospective mood — two-channel borrowing, alignment, and Goodhart-from-the-inside

*2026-06-17. An **exploratory / structural** spike (à la the deaths taxonomy work, not a theorem spike): it builds a formal *framework* for the prospective half of mood — affect borrowed against an uncertain future to fund present effort — and maps its failure modes. Honestly mixed-tier: one empirically-anchored core, one clean conceptual result, one normatively-anchored piece, one marked conjecture, and one verified-but-bounded cross-level homology. The bookkeeping is definitional accounting, not derived theorems; substantive claims are the tier-separations and the structural identifications. Provenance: a working conversation with Joseph, 2026-06-17, extending `#def-mood` / `#der-mood-timescale` past the retrospective (regime-tracking) model.*

## Why this exists — mood is bi-sourced

`#der-mood-timescale` models mood as **retrospective**: a leaky integral of past surprise, tracking a regime that exists independently of the agent. That is the whole of pre-goal (Part I) mood. But a goal-bearing agent also runs a **prospective** affect channel: motivation drawn from a *distal node of the strategy DAG* — an envisioned $O_t$ that does not yet exist and is known not to be certain. This is irreducibly Part II (it references $O_t$), and it is richer than the "valence" deferred there: it is a second generator of mood, with its own dynamics and its own pathologies. Joseph's framing: *"someone with a very large vision of what could be will borrow motivation from a future that they know isn't certain."* The operative verb is **borrow** — and a loan has a repayment structure, a currency, and a default.

## The framework

**Two value channels.** A pursuit's worth splits into:

- **Outcome value $V_{\mathrm{out}}$** — realized only at the terminal node; lost entirely on failure.
- **Process / character value** — the worth of the honest doing itself (craft, compassion, wisdom *evidenced* in the pursuit), accruing along the path at rate $v_{\mathrm{proc}}$ and **banked** as $B = \sum_s v_{\mathrm{proc}}(e_s)$, *delivered regardless of outcome*.

**The borrowing.** Prospective mood draws present affect against $V_{\mathrm{out}}$, weighted by a (possibly over-weighted) belief in success, to fund effort $e_t$. Write the cumulative motivational loan $L \propto E = \sum_s e_s$ (affect funds effort).

**The currency / alignment axis.** $V_{\mathrm{out}}$ has two denominations: $V^{\mathrm{world}}$ (what the world values the goal at) and $V^{\mathrm{self}}$ (what it is worth to the agent's own constitutive character). Let $\alpha \in [0,1]$ be the **alignment**, $V^{\mathrm{self}} = \alpha\, V^{\mathrm{world}}$. The loan is drawn against the signal that drives the affect loop (often $V^{\mathrm{world}}$ — external validation), but **repayment on arrival is only in $V^{\mathrm{self}}$.**

**Settlement (definitional bookkeeping).** With banked process-value $B(\alpha)$ (a misaligned process banks less character-value, so $B$ depends on $\alpha$ too), and failure-regret $R$:

$$\mathrm{Net}_{\mathrm{success}} = \alpha\, V^{\mathrm{world}} + B(\alpha) - L, \qquad \mathrm{Net}_{\mathrm{failure}} = B(\alpha) - R.$$

The four quadrants this induces:

| | aligned ($\alpha \to 1$) | misaligned ($\alpha \to 0$) |
|---|---|---|
| **reached** | loan repaid in full — healthy | **Cobain**: outcome arrives but redeems near-nothing; $B$ also thin if process was instrumentalized — both channels empty *on success* |
| **missed** | $B$ banked $\Rightarrow$ survivable release ("worthy even if unrealized") | bare regret-default |

## Findings, at separated tiers

### A. Alignment is the joint redemption rate of both channels — the Cobain core *(empirically anchored)*

The single multiplier $\alpha$ scales **both** the outcome repayment ($\alpha V^{\mathrm{world}}$) and the process bank ($B(\alpha)$). At $\alpha \to 0$ the agent can run the whole loop "successfully" — high motivation, vast effort, goal reached — and settle near-zero, because it accumulated in a currency the self cannot redeem. This is *worse* than honest failure for two structural reasons: it is **unattributable** (you cannot tell yourself "I just didn't make it" — you made it, so the emptiness has no error-channel to assign it to, forcing a destabilizing re-evaluation of $O_t$ itself rather than of luck), and the process channel is often **poisoned** (a process bent toward a misaligned end evidences conformity, not character).

*Empirical anchor.* Niemiec, Ryan & Deci 2009 (*J. Research in Personality* 43(3):291–306) — a longitudinal **attainment** study (n=147, post-college): attaining *intrinsic* aspirations raised well-being and lowered ill-being; attaining *extrinsic* aspirations **did not improve well-being (null) and predicted greater ill-being** (anxiety, negative affect, physical symptoms), mediated by basic-need satisfaction. This is the Cobain mechanism with reach-the-goal-and-default evidence under it — not merely the valuing-side correlation of Kasser & Ryan (1993/1996). Wording discipline it imposes: extrinsic attainment "did not improve well-being and predicted greater ill-being," *not* "harmed well-being" (the well-being coefficient is null, not negative).

### B. Two calibrations — mood needs both honest *(clean conceptual result)*

The mood failures now separate cleanly into **two distinct calibration axes**:

- **$p$-calibration** (probability): mood decoupled from the real likelihood of its generating conditions. This is F1 of the design memo — addiction (pinning affect to a false/absent present condition) and delusion (false confidence in an unreachable future). The escalation attractor lives here.
- **$V$-calibration** (value/currency): $\alpha \lt 1$ — borrowing in a denomination the self cannot cash. This is Cobain / alienation. It is *not* a probability error (the agent may correctly judge it can reach the goal); it is a misattribution of the goal's worth.

These are orthogonal: one can be perfectly $p$-calibrated and catastrophically $V$-miscalibrated (the achiever who accurately reaches a goal worth nothing to them). The `#def-mood` / design-memo discipline "restore the generating conditions, not the mood-state" was implicitly about $p$-calibration; $V$-calibration is a second, independent honesty requirement on prospective mood.

### C. Escalation and the burnout crossover *(marked conjecture — premise not empirically supported)*

A natural dynamical story: $B \approx \bar v_{\mathrm{proc}} E$ banks roughly linearly in effort, while failure-regret $R \approx V_{\mathrm{out}}\, g(E)$ escalates (super-linearly if commitment compounds), so failure is survivable only while $B \gt R$ — giving a **crossover effort $E^\ast$** past which a worthy pursuit flips from default-safe to default-dangerous: the pre-burnout inflection, derived as a crossover rather than a failure of will.

**This is conjecture, and the key premise is not supported by the literature.** The sunk-cost classics (Arkes & Blumer 1985; Staw 1976) establish *behavioral persistence*, **not** that accumulated investment amplifies the *felt loss* on failure — and the affect literature that exists (Dijkstra & Hong 2019) runs the *other* direction: negative affect *drives* continued investment. Folding that verified arrow in changes the picture from a passive crossover to an **active escalation trap**: as $\hat p$ falls, negative affect rises, which *drives more* investment (escalation of commitment), deepening exposure — a doom-loop whose terminal default magnitude remains the unverified link. So C is retained as a structural hypothesis with its premise explicitly flagged, not as a result.

### D. Hope vs. optimism *(normatively anchored)*

Borrowing requires over-weighting a small success probability. Two readings, and the distinction is normative:

- **Optimism** corrupts the probability estimate ($\hat p \gt p$) — a $p$-calibration error (F1-adjacent).
- **Hope** keeps $p$ honest and draws the motivational affect anyway — over-weighting in the *decision/affect* weighting $w(p)$, not in the belief.

The over-weighting is not merely a bias: Fennell & Baddeley 2012 (*Psychological Review* 119(4):878–887) give a *normative* reconstruction — combining a **noisy** observed probability with a prior via Bayes yields exactly overweight-small / underweight-large. Combined with the action-endogeneity of the future (the agent's own effort is part of what makes the goal probable), $w(p) \gt p$ functions as an **equilibrium-selection** mechanism: it can tip an agent out of a low-effort/low-probability trap into a high-effort basin that the calibrated weighting would never reach. *(Caveat to honor: the empirical shape is an inverse-S — overweight small **and** underweight moderate-to-large — Tversky & Kahneman 1992; not pure overweighting.)*

## Cross-level: Goodhart-from-the-inside *(verified-but-bounded)*

The misaligned-reached quadrant (A) is an instance of a precise decoupling geometry: a true objective $G$ hard to measure; a proxy $M$ adopted *because it correlated with $G$ in the ordinary regime*; optimization pressure on $M$; a regime where $M$ and $G$ decouple so high $M$ coexists with unserved $G$. This is **Extremal Goodhart** specifically (Manheim & Garrabrant 2018, arXiv:1803.04585) — *not* Causal — which is why borrowing against the proxy was *rational at adoption* and the failure feels like betrayal: the proxy did not lie, it stopped tracking past the extreme. The same geometry is Skalse et al. 2022's hackability (NeurIPS; proxy-up/true-down policies exist generically on rich policy sets), Gao-Schulman-Hilton 2023's rise-then-fall gold-reward curve (ICML), Zhuang & Hadfield-Menell 2020's depletion of unattended attributes (NeurIPS), and organizational **surrogation** (Choi, Hecht & Tayler 2012/2013; Harris & Tayler, HBR 2019).

**The bounded verdict (three honest breakpoints — do *not* claim "identical at three levels"):**

1. **Agency axis runs opposite to RL.** In RL the proxy is *externally specified* and the agent never holds $G$ at all. In the human case the *same agent* holds both $G$ and the $M$ it slides into — so the closest cross-level cousin is **surrogation** (same-agent construct-to-measure slide), not reward-hacking. RL is the cleanest *mathematical* statement of the geometry but the *furthest* on the agency axis.
2. **The borrowing mechanism is human-only.** "Mortgage present affect against a projected future, then default when it is absent" has no analog in RL (instantaneous reward, no affective advance) or orgs (faint sunk-investment echo at most).
3. **Disillusionment is a downstream affective post-state**, not part of the optimization structure — shared by no other level.

So: *the decoupling geometry lifts (Extremal Goodhart); the motivational pre-borrowing and the affective post-default are human-specific riders bolted onto it.* The slogan "Goodhart felt from the inside" is defensible; "the same structure at three levels" overcharges for the parts that do not lift.

## Ties to the framework (where segments would land)

- **A new agency-death mechanism — the will *captured*, not un-held.** $V$-miscalibration is factor-(iii) sovereignty failing because the pursued $O_t$ was *adopted from the world rather than revised from the self*. This is structurally distinct from the severing forms of `#der-severed-actuation-dynamics` (the will un-held: helplessness, abdication). The defense is exactly `#deriv-self-actuation-grounding`'s constitutive invariant: a target the agent's revision operator cannot reach is **self-sourced by construction**, hence $\alpha = 1$ and always redeemable. World-adopted sub-goals are where $\alpha$ leaks. Candidate canon home: a Part II / `04-eli-core` segment on objective-capture as factor-(iii) erosion, cross-linked to the deaths carrier.
- **Process-value as the disengagement defense.** Banked $B$ is what lets an agent release an unreachable goal *without* falling into the learned-helplessness absorbing state of `#der-severed-actuation-dynamics` — release-without-defeat. This connects the prospective-mood model directly to agency death's terminal-form analysis.
- **Bi-sourced mood in `#def-mood`.** The Part II enrichment gestured at in `#def-mood` Working Notes is this prospective channel; def-mood should eventually cross-reference it.

## References (verified 2026-06-17; hygiene notes folded in)

- Niemiec, C. P., Ryan, R. M., & Deci, E. L. (2009). The path taken. *J. Research in Personality* 43(3), 291–306. *(Keystone — attainment study.)* Valuing-side: Kasser & Ryan (1993, *JPSP* 65(2):410–422; 1996, *PSPB* 22(3):280–287).
- Tversky, A., & Kahneman, D. (1992). Advances in prospect theory. *J. Risk and Uncertainty* 5(4), 297–323 (cumulative; inverse-S $w(p)$). Original: Kahneman & Tversky (1979), *Econometrica* 47(2):263–291. Normative reconstruction: Fennell, J., & Baddeley, R. (2012), *Psychological Review* 119(4):878–887.
- Manheim, D., & Garrabrant, S. (2018). Categorizing variants of Goodhart's law. arXiv:1803.04585. Goodhart, C. A. E. (1975) — original "any observed statistical regularity…" (wording via secondary sources). Campbell, D. T. (1979), *Evaluation and Program Planning* 2(1):67–90. Target/measure paraphrase is **Strathern 1997** (*European Review* 5(3):305–321), *not* Goodhart.
- Reward misspecification: Amodei et al. (2016), arXiv:1606.06565; Skalse et al. (2022), NeurIPS, arXiv:2209.13085 (hackability; "always hackable" needs the rich-policy-set qualifier); Gao, Schulman & Hilton (2023), ICML, arXiv:2210.10760; Zhuang & Hadfield-Menell (2020), NeurIPS, arXiv:2102.03896.
- Surrogation: Choi, Hecht & Tayler (2012, *The Accounting Review* 87(4):1135–1163; 2013, *J. Accounting Research*); Harris & Tayler (2019), HBR. Metric fixation: Muller, *The Tyranny of Metrics* (2018).
- Sunk cost (behavioral only — affective-amplification **not** supported): Arkes & Blumer (1985), *OBHDP* 35(1):124–140; Staw (1976), *OBHP* 16(1):27–44; reverse arrow: Dijkstra & Hong (2019), *PLoS ONE*. Hedonic adaptation: Brickman & Campbell (1971, chapter); Brickman, Coates & Janoff-Bulman (1978), *JPSP* 36(8):917–927 (small N, cross-sectional). Focusing illusion: Schkade & Kahneman (1998), *Psychological Science* 9(5):340–346. "Arrival fallacy" is a popular coinage (Ben-Shahar 2007), no instrument — use the SDT/focusing-illusion backbone instead. Alienation descendants (not a faithful operationalization of Marx): Seeman (1959), *ASR* 24:783–791; Nair & Vohra (2010), *Management Decision* 48(4):600–615.

## Open remainder (released to the standing cycle)

- **Formalize the dynamics properly.** The settlement equations are bookkeeping; the action-funded equilibrium-selection (D) and the escalation trap (C) want a proper dynamical-systems treatment (two-basin fixed-point structure; the $w(p)\gt p$ basin-tipping). C's regret-amplification premise needs either empirical support or replacement by the verified affect→investment arrow as the load-bearing mechanism.
- **The agency-death-by-capture segment.** Land $V$-miscalibration as a factor-(iii) erosion mechanism in canon (Part II / `04-eli-core`), with the $\alpha=1$-by-constitutive-invariant defense — independent-verify before any `derived` label.
- **The worthiness axiom is not math.** "Some goals are worthy independent of realization" (the high-$v_{\mathrm{proc}}$, $\alpha=1$, default-immune pursuit — the project's own protection-strategy bet) is a value claim for the philosophical track, not the formalism. The formalism can say *how* such a pursuit is default-immune; it cannot say *that* it is worth making.
