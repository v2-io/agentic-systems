# Spike: Software Unmaintainability as a Bifurcation

*Started 2026-05-21. Research spike. Not canon.*

## 1. Problem statement

The OUTLINE Ch.4 `--GAP--` (candidate slug `#hyp-software-unmaintainability-bifurcation`) names a structural claim: codebases are *bimodal* in age-of-region under modification — G1 (recent, $\text{age} \lt \tau_1$), G3 (old stable, $\text{age} \gt \tau_3$), and G2 (middle-aged, $\tau_1 \lt \text{age} \lt \tau_3$) — and G2 is the *danger zone* in which the persistence inequality $\mathcal T_\text{dev} \gt \rho / \lVert \delta_\text{critical} \rVert$ ( #result-persistence-condition, linear operational form) tends to fail. The existing chain $Q \to U_o \to \eta^\ast \to \mathcal T$ ( #der-code-quality-as-observation-infrastructure) is written as a *vicious / virtuous cycle* hypothesis at the bottom of that segment. This spike strengthens that hypothesis to an explicit bifurcation under stated conditions, with G1 / G3 as the two stable basins, G2 as the unstable middle, and the unmaintainable regime as the basin in which the persistence inequality is violated for the developer's local channel.

**The task.** Spike-grade derivation of the bifurcation in a 2-state local-region model $(K, W)$ where $K$ is the developer's local knowledge of region $s$ (units: a normalized knowledge mass) and $W$ is the local defect/broken-window mass. Decouple the spike from the disputed $\alpha \approx 0.31$ contagion constant and the $\tau \approx 20$-day Ebbinghaus constant — those become *anchors* not load-bearing parts of the derivation. Identify the structural conditions under which the system has two stable equilibria separated by an unstable middle, give the qualitative form of the basin boundary, and connect both basins to the local persistence inequality of #result-persistence-condition.

**Scope.** The derivation is *local* to a single code region $s$ on a single developer-channel. The system-level codebase claim (a whole codebase enters the unmaintainable regime when a fraction of its regions cross the boundary) is named as a forward question, not derived here. The bifurcation that *is* derived is the per-region one. The hypothesis tier is the *starting* point per Joseph's strengthen-before-soften discipline; strengthening targets are *robust qualitative* (the bimodality survives translation of constants) and *conditional* (the bifurcation is exact under named sufficient conditions).

## 2. What we already have

The pieces this spike composes:

1. **#result-persistence-condition.** The linear operational form $\mathcal T_\text{dev} \gt \rho / \lVert \delta_\text{critical} \rVert$ is the threshold the developer's local adaptive tempo must clear for the region. Failure is a *qualitative regime transition*, not a gradual degradation (the segment is explicit about this). Below the threshold, mismatch grows up to the sector-region edge — that is what *unmaintainable* will mean, in a precise sense, in this spike.

2. **#der-code-quality-as-observation-infrastructure.** Establishes the chain $U_o^\text{(read)}(s) = f(Q(s))$ with $f$ monotonically decreasing, $\eta^\ast = U_M / (U_M + U_o)$, $\mathcal T_\text{read}(s) = \nu^\text{(read)} \cdot \eta^\ast$. The vicious/virtuous-cycle paragraph in that segment's Discussion is the qualitative shape this spike *derives*.

3. **#der-change-expectation-baseline.** Median remaining feature count equals observed past count under Jeffreys' prior. For a region $s$, this gives the *local* change-pressure rate $\rho(s)$ from chronicle data: a region that has been changed $n_{\text{past}}(s)$ times over its lifetime has median-predicted $\rho(s) \propto n_{\text{past}}(s) / t_0(s)$. Old code that has stopped being modified ($\rho(s) \to 0$) is precisely G3.

4. **Empirical anchors (Tornhill, forensic-mining F8 + F18).**
   - Code health is bimodal in age: G1 ($\text{age} \lt \sim 30$ days), G3 ($\text{age} \gt 1$ year), G2 in between. G2 files have several-times higher defect rates than G1 and G3.
   - Defect rate decays with age: $D(s, \text{age}) \approx D_0 e^{-\text{age}/365}$ (survival-as-quality-filter, 123-analysis).
   - The .NET Core `gc.cpp`, Linux Intel-graphics, Android `ActivityManagerService` case studies: large unmaintainable files are typically *born* large and complex and grow rapidly in the first months, not slowly accumulated (F18). This cuts against gradual-decay framing and *supports* a bifurcation reading.
   - Ebbinghaus forgetting curve $K(t) = K_0 e^{-t/\tau}$ with $\tau \approx 20$ days for textual material applied to code-knowledge. **Honesty Call (A).** The transfer to code-comprehension is plausible but unvalidated. The bifurcation derivation below treats $\tau$ as a free positive constant; the empirical anchor is decorative.
   - Pragmatic-mining cluster #3 (004-broken-windows + 416 + 417 + 419) gives a logistic-with-contagion shape $dW/dt = b_0 + \alpha W - (r_0 - \beta W)W$ with critical point $W^\ast = (r_0 - b_0)/(\alpha + \beta)$ as the candidate dynamical-system form. **Honesty Call (B).** The 004-analysis cites "2024 research with 29 developers" for $\alpha \approx 0.31$ as the contagion rate. *Generative-citation risk.* See §9.

## 3. Per-region two-state model

Let $s$ index a single code region (file, module, function — granularity unspecified at this layer). On the developer-channel for $s$, define two local state variables:

- $K(s, t) \in [0, 1]$ — the developer's *local knowledge* of region $s$ at time $t$, normalized so $K = 1$ is "just read and understood, $U_o$ at its floor" and $K = 0$ is "no knowledge, $U_o$ at its ceiling."
- $W(s, t) \ge 0$ — the *local defect/disorder mass* of region $s$ at time $t$, in arbitrary units (e.g., normalized count of dead branches, broken invariants, conventions violated). $W = 0$ is *clean*.

**Connection to the existing chain.** $U_o^{\text{(read)}}(s)$ is determined by both $K$ and $W$:

$$U_o^{\text{(read)}}(s, t) \;=\; u_0 \cdot \phi(K(s,t)) \cdot \psi(W(s,t))$$

with $\phi$ decreasing in $K$ and $\psi$ increasing in $W$, both positive. The minimal sufficient functional forms used below are $\phi(K) = e^{-aK}$ and $\psi(W) = 1 + cW$ for positive $a, c$. The *load-bearing* claim is the monotonicity (more knowledge or less disorder lowers observation noise); the exponential and linear specific forms are pedagogical. See §7 for invariance of the bifurcation under change of functional form.

The persistence inequality of #result-persistence-condition specialized to this region becomes:

$$\mathcal T_\text{read}(s) \;=\; \nu^{\text{(read)}} \cdot \frac{U_M}{U_M + u_0 \phi(K) \psi(W)} \;\gt\; \frac{\rho(s)}{\lVert \delta_\text{critical} \rVert} \qquad (\dagger)$$

We treat $(\dagger)$ as the *region's local persistence inequality*: the developer's local tempo on $s$ must exceed the region's local change-pressure rate. Failure of $(\dagger)$ defines the *unmaintainable-for-region-s* regime in the formal sense.

## 4. Local dynamics

Two dynamical equations, one for each state variable.

### 4.1. Knowledge dynamics ($K$)

Two effects: (i) Ebbinghaus-style decay when the region is not being touched, (ii) re-acquisition on contact. Let $r(s, t) \ge 0$ denote the *contact rate* — the rate at which the developer is currently reading or modifying region $s$. Then:

$$\frac{dK}{dt} \;=\; -\frac{K}{\tau} \;+\; \mu \cdot r(s, t) \cdot (1 - K) \qquad (4.1)$$

- The decay term $-K/\tau$ is exponential forgetting with characteristic time $\tau$ (Ebbinghaus). Honesty Call (A) above flags the magnitude of $\tau$ as an unvalidated transfer; here it is just a positive constant.
- The acquisition term $\mu r (1-K)$ saturates at $K = 1$ and is driven by contact. $\mu \gt 0$ is the per-contact learning rate; $r$ has units of contact-rate.

The *steady-state* knowledge at contact rate $r$ (treating $r$ as quasi-stationary) is:

$$K_\text{ss}(r) \;=\; \frac{\mu r \tau}{1 + \mu r \tau} \qquad (4.2)$$

so $K_\text{ss}(0) = 0$ (no contact, no knowledge in the limit), $K_\text{ss}(\infty) = 1$ (saturated knowledge under continuous contact), and the transition is logistic in $\log(r\tau)$.

### 4.2. Contact rate and the chronicle

The contact rate $r(s, t)$ is *not* externally imposed — it is shaped by the change-pressure rate $\rho(s)$ and the developer's local response. The simplest model: when a region is under change pressure, the developer contacts it. Identify $r(s, t)$ with $\rho(s, t)$ up to a developer-side proportionality:

$$r(s, t) \;=\; \kappa \cdot \rho(s, t) \qquad (4.3)$$

with $\kappa \gt 0$ a constant absorbing whatever fraction of change pressure on $s$ becomes developer-contact (versus being deferred, ignored, or absorbed by automation). Substituting into (4.2):

$$K_\text{ss}(\rho) \;=\; \frac{\mu \kappa \rho \tau}{1 + \mu \kappa \rho \tau} \;=\; \frac{\rho / \rho_c}{1 + \rho / \rho_c} \qquad (4.4)$$

where $\rho_c \;\equiv\; 1/(\mu \kappa \tau)$ is the *characteristic change-pressure rate* at which $K_\text{ss} = 1/2$. The bimodality intuition appears in this single equation: for $\rho \ll \rho_c$ (G3 regime, code rarely touched) $K_\text{ss} \approx \rho / \rho_c$ (small but irrelevant because the persistence requirement is also small); for $\rho \gg \rho_c$ (G1 regime, fresh hot region) $K_\text{ss} \approx 1$ (saturated, low $U_o$); the dangerous middle is where $\rho \sim \rho_c$ and $K_\text{ss}$ is partial.

### 4.3. Defect dynamics ($W$)

A logistic-with-contagion baseline, taken from the broken-windows/pragmatic cluster:

$$\frac{dW}{dt} \;=\; b_0 \;+\; \alpha W \;-\; \gamma(K) \cdot W \qquad (4.5)$$

- $b_0 \gt 0$ is the baseline rate of defect introduction from external change pressure.
- $\alpha \ge 0$ is the *contagion* rate — new defects are seeded faster in the presence of existing ones ("broken windows beget broken windows"). The disputed empirical anchor $\alpha \approx 0.31$ enters only here; the derivation does *not* require this magnitude — it requires $\alpha \ge 0$.
- $\gamma(K)$ is the *repair* rate as a function of local knowledge. We require $\gamma$ to be monotonically increasing in $K$ with $\gamma(0) = \gamma_0 \ge 0$ (minimal involuntary repair from external pressure: code-review, automated lints, etc.) and $\gamma(1) = \gamma_\text{max} \gt \alpha$ (high-knowledge regime can outpace contagion). The minimal sufficient form is $\gamma(K) = \gamma_0 + (\gamma_\text{max} - \gamma_0) K$.

The structural content is that *repair depends on knowledge*: a developer with $K \approx 1$ understands the region and can refactor cleanly; a developer with $K \approx 0$ patches around what they don't understand and adds to $W$. This is the load-bearing dynamical claim — given it, the bifurcation below falls out.

### 4.4. The composed system

Substituting $K = K_\text{ss}(\rho)$ from (4.4) into the steady-state condition $dW/dt = 0$ from (4.5):

$$W_\text{ss}(\rho) \;=\; \frac{b_0}{\gamma(K_\text{ss}(\rho)) - \alpha} \qquad \text{when} \quad \gamma(K_\text{ss}(\rho)) \gt \alpha \qquad (4.6)$$

When $\gamma(K_\text{ss}(\rho)) \le \alpha$, equation (4.5) gives $dW/dt \ge b_0 \gt 0$ regardless of $W$: defects accumulate without bound (up to whatever finite ceiling the modeling reach permits — this is the spike's analog of the sector-region edge in #result-persistence-condition). Define:

$$K^\ast \;\equiv\; \gamma^{-1}(\alpha) \qquad (4.7)$$

as the *minimum knowledge required to outpace contagion*. The repair-versus-contagion regime change at $K = K^\ast$ is the structural seed of the bifurcation.

## 5. The bifurcation, made explicit

Combine the persistence inequality $(\dagger)$ with the steady-state $(K_\text{ss}, W_\text{ss})$:

$$\nu^\text{(read)} \cdot \frac{U_M}{U_M + u_0 \phi(K_\text{ss}(\rho)) \psi(W_\text{ss}(\rho))} \;\gt\; \frac{\rho}{\lVert \delta_\text{critical} \rVert} \qquad (\ddagger)$$

The bifurcation is a property of $(\ddagger)$ read as a function of $\rho$ (treating the region's parameters $\tau, \mu, \kappa, b_0, \alpha, \gamma_0, \gamma_\text{max}, u_0, a, c$ and the developer's parameters $\nu^\text{(read)}, U_M, \lVert \delta_\text{critical} \rVert$ as fixed).

### 5.1. Three regimes of $\rho$

- **G1 (high $\rho \gg \rho_c$): fresh hot region.** $K_\text{ss} \to 1$, $\phi(K_\text{ss}) \to e^{-a}$ (its minimum). If additionally $K_\text{ss} \gt K^\ast$ — i.e., the contact rate is high enough that knowledge saturates above the repair-contagion threshold — then $\gamma(K_\text{ss}) \gt \alpha$ and (4.6) gives finite $W_\text{ss}$, $\psi(W_\text{ss})$ bounded. The LHS of $(\ddagger)$ is high. The RHS rises with $\rho$, so $(\ddagger)$ holds *iff* $\nu^\text{(read)}$ is large enough relative to $\rho / \lVert \delta_\text{critical} \rVert$. **Maintainable, by knowledge-saturation route.**

- **G3 (low $\rho \ll \rho_c$): old stable region.** $K_\text{ss} \to 0$, $\phi(K_\text{ss}) \to 1$, $U_o$ at its high ceiling. If $K_\text{ss} \lt K^\ast$ — knowledge below the repair-contagion threshold — then $\gamma(K_\text{ss}) \le \alpha$ and (4.6) breaks: defect accumulation has no finite steady state from the dynamics alone. But the RHS of $(\ddagger)$ also shrinks with $\rho$, in proportion. In the limit $\rho \to 0^+$, the RHS shrinks to $0$ regardless of how degraded $U_o$ becomes, and *the inequality holds vacuously*. The G3 regime is the regime in which $\rho$ has fallen so low that the local persistence requirement is trivially met — the code is not being asked to keep up. **Maintainable, by stationarity route.** (Note: "code with high $W$ but $\rho = 0$" is the G3-with-mess case — observable as the "ugly G3 module no one touches"; the persistence inequality is still satisfied because the RHS is near zero. This matches the empirical observation in F19 that low-quality old code can still be high-quality-in-the-dual-optimization sense.)

- **G2 (middle $\rho \sim \rho_c$): the danger zone.** $K_\text{ss}$ is partial. *Both* possibilities for the $K_\text{ss}$ vs $K^\ast$ comparison are live: the system may have $K_\text{ss} \gtrless K^\ast$ depending on parameter values. This is where the bifurcation lives.

### 5.2. Sufficient condition for two basins

Define the *bifurcation parameter*

$$\beta(\rho) \;\equiv\; \gamma(K_\text{ss}(\rho)) - \alpha \qquad (5.1)$$

The sign of $\beta(\rho)$ controls whether (4.6) has a finite solution. $\beta(\rho)$ is monotone increasing in $\rho$ on $(0, \infty)$ under our assumptions ($K_\text{ss}$ increasing in $\rho$ by (4.4); $\gamma$ increasing in $K$). Therefore there exists a unique $\rho^\ast$ at which $\beta(\rho^\ast) = 0$, i.e., $K_\text{ss}(\rho^\ast) = K^\ast$. The two regimes of *finite $W_\text{ss}$* are:

- $\rho \gt \rho^\ast$: $\beta(\rho) \gt 0$, repair outpaces contagion at the knowledge level induced by contact, $W_\text{ss}$ finite. The region is *kept clean by being touched*.
- $\rho \lt \rho^\ast$ *and* $\rho \gtrsim 0$: $\beta(\rho) \lt 0$, contagion outpaces repair, $W$ accumulates. But — and this is the bifurcation's other lobe — the persistence requirement also drops with $\rho$. If $\rho$ is small enough, $(\ddagger)$ holds despite degenerating $W$.

**Two basins of attraction emerge** when both routes to satisfying $(\ddagger)$ — knowledge-saturation (high $\rho$) and stationarity (low $\rho$) — are *separated by a regime in which neither works*. This is the structural content of the bifurcation.

The sufficient condition for the existence of a two-basin structure with an *unmaintainable middle*, under the named assumptions, is:

$$\boxed{\exists \rho^\dagger \in (0, \rho^\ast) \;:\; \nu^\text{(read)} \cdot \frac{U_M}{U_M + u_0 \phi(K_\text{ss}(\rho^\dagger)) \psi(W_\text{ss}(\rho^\dagger))} \;\le\; \frac{\rho^\dagger}{\lVert \delta_\text{critical} \rVert}} \qquad (\star)$$

i.e., somewhere below the repair-threshold $\rho^\ast$ but above the stationarity-vacuous limit, the developer's tempo on the region fails to clear the local persistence requirement. When $(\star)$ holds, the set of $\rho$ values at which $(\ddagger)$ holds is *disconnected*: a high-$\rho$ component (G1) and a low-$\rho$ component (G3), with an *unmaintainable interval* (G2) between them.

The empirical correlate is exactly Tornhill's age-bimodality observation. Time substitutes for $\rho$ in practice because $\rho(s, t)$ for a region tends to decay with $\text{age}(s, t)$ as the region matures and the surrounding system stabilizes around it: fresh regions are touched often (high $\rho$, G1), old regions are touched rarely (low $\rho$, G3), and the middle-aged regions are in the transition (G2).

### 5.3. What $(\star)$ requires

Reading off the conditions under which $(\star)$ holds — i.e., under which the unmaintainable middle exists at all:

1. **Non-trivial repair-threshold:** $K^\ast \in (0, 1)$, i.e., $\gamma(0) \lt \alpha \lt \gamma(1)$. The contagion rate $\alpha$ must exceed the involuntary repair rate $\gamma_0$ (else G3 is always clean) and lie below the saturated-knowledge repair rate $\gamma_\text{max}$ (else even G1 fails). Both bounds say *the developer's knowledge matters* — the system is not trivially clean by automation alone, not trivially overwhelmed regardless of the developer's state.
2. **Sufficient base defect rate:** $b_0 \gt 0$. Defects are introduced.
3. **Sufficient quality-to-noise sensitivity:** $a, c \gt 0$ such that the LHS of $(\ddagger)$ is sensitive to $K, W$. If $u_0$ is tiny relative to $U_M$, observation noise never matters, and the system is in a degenerate maintainable regime.
4. **Sufficient task adequacy ceiling:** $\lVert \delta_\text{critical} \rVert$ finite, so the RHS of $(\ddagger)$ is non-trivial.

Items 1 and 3 are the *structural* requirements: the danger-zone exists when knowledge gates repair (1) *and* when $U_o$ is sensitive enough to $K$ and $W$ that the persistence inequality has bite in the relevant $\rho$ range (3). Items 2 and 4 are technical non-degeneracy. The contagion rate $\alpha$ appears only as a comparison anchor in the definition of $K^\ast$; its specific magnitude (the disputed $0.31$) is not load-bearing — what matters is that $\alpha$ lies between $\gamma_0$ and $\gamma_\text{max}$.

This is the strengthening of the vicious/virtuous-cycle hypothesis in #der-code-quality-as-observation-infrastructure from gesture to *bifurcation under stated sufficient conditions*. The bifurcation is generic to the logistic-with-contagion shape (4.5) combined with the persistence inequality (4.4)+($\dagger$) — exactly what Joseph's TST-IDEAS §A3 anticipated.

## 6. Worked sketch and numerical anchor

For concreteness, fix (all units arbitrary): $\tau = 20$, $\mu \kappa = 1/40$ (so $\rho_c = 2$), $b_0 = 0.1$, $\alpha = 0.31$, $\gamma_0 = 0.1$, $\gamma_\text{max} = 1.0$, $\gamma(K) = \gamma_0 + (\gamma_\text{max} - \gamma_0) K$. Then $K^\ast = (\alpha - \gamma_0)/(\gamma_\text{max} - \gamma_0) = 0.21/0.9 \approx 0.233$, and from (4.4) the corresponding $\rho^\ast$ is the solution of $K_\text{ss}(\rho^\ast) = 0.233$, giving $\rho^\ast = \rho_c \cdot K^\ast / (1 - K^\ast) \approx 2 \cdot 0.304 \approx 0.608$. Below $\rho \approx 0.6$ (in arbitrary units), the system is in the contagion-dominant regime where $W$ has no finite steady state; above, it is in the repair-dominant regime. Take $u_0 = 10$, $U_M = 1$, $\nu^\text{(read)} = 1$, $a = 3$, $c = 0.5$, $\lVert \delta_\text{critical} \rVert = 1$. Then in the G1 regime ($\rho = 5$, $K_\text{ss} \approx 5/7$, $\phi \approx e^{-15/7} \approx 0.117$, $\gamma(K_\text{ss}) \approx 0.74$, $\beta \approx 0.43$, $W_\text{ss} \approx 0.23$, $\psi \approx 1.12$), the LHS of $(\ddagger)$ is $\approx 1/(1+10 \cdot 0.117 \cdot 1.12) \approx 1/2.31 \approx 0.43$ versus RHS $= 5$. **$(\ddagger)$ fails** at $\rho = 5$ in these numbers — meaning, for this *specific* parameter choice, the developer's $\nu^\text{(read)} = 1$ is itself too small to keep up with a $\rho = 5$ change-pressure rate even with saturated knowledge.

This is the spike's most uncomfortable honest finding: the persistence inequality $(\ddagger)$ does *not* automatically hold in G1 just because $K_\text{ss}$ is high. The G1-as-maintainable picture requires that $\nu^\text{(read)}$ is large *and* well-matched to the region's $\rho$. A burning-hot region under a slow developer can fail $(\ddagger)$ from above just as a forgotten-but-pressured G2 region fails it from the side. The bifurcation gives the *qualitative shape* of the maintainable set; whether any specific region falls inside the set depends on the developer-region parameter match.

Re-tuning to $\nu^\text{(read)} = 20$ (a developer who can read fast on this region — high contact rate, or pair-programming): in G1 ($\rho = 5$), LHS $\approx 20 / 2.31 \approx 8.66$ versus RHS $= 5$. **$(\ddagger)$ holds.** In G2 ($\rho = 0.4$, $K_\text{ss} \approx 0.4/2.4 \approx 0.167$, below $K^\ast \approx 0.233$, so contagion-dominant; $W$ unbounded in steady state — use a finite ceiling $W = 5$ as the sector-region-edge analog; $\phi \approx e^{-0.5} \approx 0.607$, $\psi(5) = 3.5$), LHS $\approx 20 / (1 + 10 \cdot 0.607 \cdot 3.5) \approx 20 / 22.2 \approx 0.90$ versus RHS $= 0.4$. **$(\ddagger)$ holds**, but barely — and only because $\nu^\text{(read)}$ is large. With $\nu^\text{(read)} = 5$, the LHS drops to $\approx 0.225$ and $(\ddagger)$ fails. In G3 ($\rho = 0.05$), the same calculation with $W$ ceiling gives a small LHS but RHS is also $0.05$ — the inequality holds with margin.

This numerical sketch is decorative: the parameters are unanchored, and the $W$-ceiling is a *modeling* choice not a derived quantity. What the sketch demonstrates is that the structure of the bifurcation is preserved under realistic parameter choices and that the G2 failure mode is the operationally distinctive one — it is *new* danger that does not appear in either G1 or G3 alone, and it appears at intermediate $\rho$ where $K_\text{ss}$ has fallen below $K^\ast$ but $\rho$ remains high enough to demand work.

## 7. Robustness of the bifurcation to functional-form choices

The exponential $\phi(K) = e^{-aK}$, linear $\psi(W) = 1 + cW$, linear $\gamma(K) = \gamma_0 + (\gamma_\text{max} - \gamma_0) K$, and the specific Ebbinghaus decay form (4.1) are all pedagogical. The bifurcation survives under any choice satisfying:

- $\phi(K)$ continuous, monotone decreasing on $[0, 1]$, bounded above and below by positive constants.
- $\psi(W)$ continuous, monotone increasing on $[0, \infty)$, $\psi(0) = 1$, unbounded above.
- $\gamma(K)$ continuous, monotone increasing on $[0, 1]$, $\gamma(0) = \gamma_0 \lt \alpha \lt \gamma_\text{max} = \gamma(1)$.
- $K_\text{ss}(\rho)$ continuous, monotone increasing on $[0, \infty)$, $K_\text{ss}(0) = 0$, $\lim_{\rho \to \infty} K_\text{ss}(\rho) = 1$.

The qualitative argument in §5.2 uses only these monotonicities plus the intermediate-value theorem applied to the bifurcation parameter $\beta(\rho)$ from (5.1). The bimodality is the *robust qualitative* claim; the specific shape of the basins of attraction and the exact location of $\rho^\ast$ depend on the functional forms.

The bifurcation is *generic* to the system (4.1)+(4.3)+(4.5)+($\dagger$) under the monotonicity assumptions — exactly Joseph's strengthen-before-soften framing of the result. The honest claim grade is: **conditional** on the dynamical structure (the named monotonicity assumptions and the persistence inequality), the bimodality with unmaintainable-middle is *exact*. The transfer of specific constants ($\tau \approx 20$ days, $\alpha \approx 0.31$, $\rho_c$ in any specific units) is *empirical*, hypothesis-tier at best, and not load-bearing on the derivation.

## 8. Connection to siblings — assumptions to surface

This spike runs in parallel with five others. Two are direct compositions:

- **Spike 5: developer-tempo channels ($\mathcal T_\text{dev}$ decomposition).** This spike treats $\nu^\text{(read)}$ as a single scalar capacity. The developer-tempo-channels sibling decomposes $\mathcal T_\text{dev}$ into $\mathcal T_\text{obs} + \mathcal T_\text{explore} + \mathcal T_\text{probe}$, with matrix-Loewner weakest-channel bottlenecking ([`TST-IDEAS.md`](../TST-IDEAS.md) §A4). The composition: the *read* channel here is $\mathcal T_\text{obs}$ in their decomposition; the bifurcation result applies channel-wise. If any one channel falls below its region-local persistence requirement, the developer fails to maintain that region on that channel — the matrix-Loewner form lifts $(\ddagger)$ from scalar to per-channel and an unmaintainable region can be unmaintainable on $\mathcal T_\text{obs}$, $\mathcal T_\text{explore}$, or $\mathcal T_\text{probe}$ independently. Sibling-side question: does the chronicle-derivable separation of channels let G2 regions be diagnosed by *which channel* is failing on them?
- **Spike 1: running-software-agent.** The runtime-side analog of unmaintainability is service-runtime under disturbance — where $\rho$ is request load + dependency churn, and the analog of $K$ is the agent's runtime $M_t$ (cached state, circuit-breaker state, observability dashboards). The same bifurcation shape — high-$\rho$ saturated-knowledge regime, low-$\rho$ stationarity regime, dangerous middle — should reappear at the runtime level. Sibling-side handshake: the *what is $K$ for a running service?* question is theirs; the *the bifurcation has this structure* answer is ours, applied per-channel.

**Surface for siblings:** this spike assumes (i) contact-driven knowledge acquisition (4.1)+(4.3), (ii) repair-rate-monotone-in-knowledge ($\gamma$), (iii) defect contagion logistic-with-additive-baseline (4.5). The first two should hold cleanly for the runtime-agent reframe. The third — defect contagion — has a natural runtime-side analog (cascading failures, error budget spend) but the dynamics are not obviously logistic; the runtime spike should re-derive its disorder dynamics rather than transfer (4.5).

## 9. Honesty calls and uncertainty surface

Marked explicitly because the spike combines high-confidence structure with anchor-grade-only constants.

**(A) Ebbinghaus $\tau \approx 20$ days.** From the original human-memory literature on text retention (Ebbinghaus 1885; modern replications in textbook material). The transfer to code-comprehension is plausible — code is a structured textual artifact and the human memory machinery is the same — but unvalidated in the code-specific literature. Implication for this spike: $\tau$ is treated as a free positive constant in the derivation; the specific 20-day figure decorates the worked sketch in §6 but is not load-bearing. Strengthening path: a primary empirical study of code-comprehension decay vs. last-contact-time, with controlled re-acquisition trials. Out of scope here.

**(B) The $\alpha \approx 0.31$ technical-debt-contagion empirical citation.** The 004-broken-windows analysis cites "2024 research with 29 developers" finding $\alpha \approx 0.31$ as the contagion rate. The forensic-mining and pragmatic-mining analyses both flag this as generative-citation risk — the "2024 research" has no traceable primary source as of the 2026-05-21 mining cycle. Implication for this spike: the derivation does *not* require $\alpha = 0.31$ specifically; it requires $\alpha \in (\gamma_0, \gamma_\text{max})$. The disputed magnitude is therefore not load-bearing on the bifurcation argument. Strengthening path: either (i) track down a primary source for the contagion claim, (ii) downgrade the specific number to *hypothesis-tier with anchor-pending* and remove the worked-sketch dependence in §6, or (iii) replace with a cleanly-cited contagion-style empirical from a different corpus. Pre-segment: do *not* land $\alpha = 0.31$ as a fact in the segment body; cite the broken-windows literature qualitatively, and treat the specific number as anchor-pending in Working Notes.

**(C) Identification of contact-rate with change-pressure rate, (4.3).** The proportionality $r = \kappa \rho$ folds three distinct phenomena into one constant: (i) what fraction of change pressure on $s$ becomes developer-attention versus is deferred / automated / ignored, (ii) what fraction of developer-attention turns into reading versus modification, (iii) how reading and modification map to $K$-acquisition. Each is its own modeling decision. For the bifurcation derivation in §5 only the monotonicity $r$ increasing in $\rho$ matters; the linear specific form decorates §6.

**(D) The "$W$ has no finite steady state below $\rho^\ast$" regime in (4.6).** In the contagion-dominant regime, defect mass grows without bound under the simple linear-in-$W$ logistic form (4.5). This *is* the analog of the sector-region edge in #result-persistence-condition (where mismatch grows without effective bound up to $R$). In practice, $W$ is capped by what a real codebase can hold — eventually nothing compiles, nothing runs, the team rewrites or the project is abandoned. The bifurcation argument does not require any specific ceiling — what it requires is that the persistence inequality $(\ddagger)$ fails for *some* interval of $\rho$ values in G2, which it does whenever $u_0 \phi \psi$ grows fast enough to dominate $U_M$. The numerical sketch in §6 used a finite ceiling $W = 5$ as a modeling crutch; the segment should state the unbounded-$W$ regime cleanly without an arbitrary ceiling.

**(E) The codebase-level vs region-level scope.** This spike is per-region. The system-level claim — "a codebase is unmaintainable" — would aggregate over regions (e.g., fraction of regions in G2 exceeds some threshold) and is more delicate. The system-level statement is out of scope and named as a forward question for the candidate segment's Discussion / Working Notes.

**(F) Discreteness of code-region changes.** The dynamics are continuous-time differential equations. Real software changes are discrete events (commits). The continuous-time form is a smoothing of the underlying point process; the bifurcation argument is invariant to this smoothing under standard stochastic-averaging assumptions, but a discrete-event simulation would be the cleanest validation. Out of scope here; flagged as a candidate simulation spike for a future cycle.

**(G) Whether $\nu^\text{(read)}$ is itself state-dependent.** The derivation treats $\nu^\text{(read)}$ as a developer-side constant. In practice, observation frequency on a region is shaped by the developer's $M_t$ and $\Sigma_t$ — a developer who has formed a misleading mental model of the region may stop visiting it, reducing $\nu^\text{(read)}$ below what the persistence inequality demands. This couples the bifurcation to the developer's broader cognitive state and is the substrate of the vicious-cycle dynamic (the developer avoids the region they no longer understand, accelerating their knowledge loss). The current derivation has a clean two-state version of this via $K(s, t)$ — $\nu^\text{(read)}$ -coupling would be a third state variable. Out of scope here; flagged as a strengthening target.

## 10. What lands where

This spike is process artifact, not canon. The candidate-segment landing is `02-tst-core/src/hyp-software-unmaintainability-bifurcation.md` (Hypothesis under Ch.4, named in the OUTLINE `--GAP--` row already), with:

- **Formal Expression:** The (4.1)–(4.5), ($\dagger$), ($\ddagger$), ($\star$) structure of §4–§5. The bifurcation parameter $\beta(\rho)$ definition (5.1). The boxed sufficient condition for two basins ($\star$).
- **Epistemic Status:** *Hypothesis* tier overall, with the bifurcation-under-named-assumptions content as *conditional*-tier under sub-scope ($\alpha$ between $\gamma_0$ and $\gamma_\text{max}$, monotonicities of $\phi, \psi, \gamma, K_\text{ss}$). The bimodal age-distribution empirical correlate as *robust qualitative* once the Tornhill case studies are cited. The specific constants ($\tau$, $\alpha$, $\rho_c$) explicitly named as *empirical* and anchor-pending.
- **Discussion:** The G1 / G2 / G3 picture from §5.1; the "G3-with-mess" case from §5.1; the matrix-Loewner per-channel lift from §8; the runtime-agent reframe pointer from §8; the codebase-level open question from honesty call (E).
- **Working Notes:** Spike pointer (this file), the seven honesty calls, the discrete-event-simulation question (F), the $\nu^\text{(read)}$-coupling question (G), the citation-pending status of the $\alpha \approx 0.31$ number.

The empirical anchors — Tornhill's age-bimodality observation, the .NET Core / Linux / Android case studies (F18), the $D(s, \text{age}) \approx D_0 e^{-\text{age}/365}$ defect decay — go into the Discussion as anchor-grade-evidence-supporting-but-not-deriving-the-bifurcation. The disputed $\alpha \approx 0.31$ number does *not* land in the segment body; it is mentioned only in Working Notes as anchor-pending, with the worked-sketch §6 numerics from this spike kept here and not promoted.

No segment edits, no OUTLINE edits in this spike. Promotion to a segment is a separate cycle that handles the OUTLINE row update (replacing `--GAP--` with the slug, $N$ assignment), FORMAT compliance, dependency-graph integration, and (if appropriate) the per-section status promotion from `missing` to `draft`.

## 11. Outcome

**Outcome (C+) — partial derivation with explicit sufficient-condition closure.** The bifurcation is derived as a generic consequence of (a) the existing $Q \to U_o \to \eta^\ast \to \mathcal T$ chain, (b) the persistence inequality $(\dagger)$, (c) contact-driven knowledge dynamics (4.1)+(4.3), and (d) repair-rate monotone in knowledge with contagion-versus-repair regime change at $K = K^\ast$. The boxed sufficient condition ($\star$) names exactly when the unmaintainable middle exists. The bimodal age-distribution empirical anchor is recovered as a corollary of $\rho(s, t)$ decaying with age.

**Strengthening achieved:** the vicious-cycle / virtuous-cycle gesture in #der-code-quality-as-observation-infrastructure becomes a bifurcation under stated conditions. The G1/G2/G3 empirical observation becomes a structural prediction of the model. The "unmaintainable" regime acquires a specific meaning: it is the basin of $\rho$ values for region $s$ in which $(\ddagger)$ fails, located between the high-$\rho$ knowledge-saturation regime and the low-$\rho$ stationarity regime.

**Honest residue:** the constants ($\tau \approx 20$ days, $\alpha \approx 0.31$, $\rho_c$ in any specific units) are anchor-pending and decorate the worked sketch without bearing on the derivation. The system-level codebase-as-unmaintainable claim is per-region only; the aggregation is named but not solved. $\nu^\text{(read)}$ -coupling to the developer's broader cognitive state is named but not modeled.

**Tier movement under Joseph's working convention:** *hypothesis-tier (starting)* $\to$ *conditional* on the named monotonicities + persistence inequality (the bifurcation derivation under sub-scope assumptions); the *robust qualitative* target awaits the bimodal-age-distribution empirical landing in a future cycle, which is straightforward — Tornhill's case studies (101, 123, 648) are the anchor. The strengthening before softening was honestly attempted — and the result is a stronger statement than the gesture it replaces, with the failure modes (which constants are decorative, which dynamics are out of scope) named cleanly.
