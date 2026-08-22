---
slug: def-control-regret
type: definition
status: exact
depends:
  - def-value-object
  - def-satisfaction-gap
stage: draft
---

# Definition: Control Regret

The second of two orthogonal diagnostic quantities, completing the diagnostic split with #def-satisfaction-gap. **Control regret** $\delta_{\text{regret}}$ is the gap between the best available value (objective attainability $A_O$) and the value achieved by the agent's *current* policy. It is always non-negative by construction — the current policy cannot outperform the best in its class. Near zero means the agent is doing the best it can within its current model, policy class, and horizon; large means there is room for improvement *without* changing the objective — the signal for strategy revision.

The diagnostic power emerges when satisfaction gap and control regret are read **together as a 2×2 cell map** (full table in Discussion): each cell of `goal-attainable × policy-near-optimal` prescribes a different corrective action — success, strategy-revision, capability-limit (consider objective revision after $M_t/\Pi/N_h$ checks), or both-strategy-and-goal. This is what makes the orient cascade ( #der-orient-cascade) *actionable*: each cell routes revision pressure to a different substate. The key insight motivating the split is that $\delta_{\text{regret}}$ can be *near zero* while the agent is *optimally failing* — pursuing a goal beyond its reach with no strategy improvement available; a single goal-distance signal could not distinguish this from "bad strategy, achievable goal."

Like the satisfaction gap, control regret is **convention-relative**: under C1 (one-step) it reveals only the gap between the current first action and the best one-step deviation (a policy "locally near-optimal" under C1 may be globally suboptimal); under C3 (Bellman) it reveals the full gap to the globally optimal policy. C2 (receding-horizon) is often the most useful convention for strategy revision — captures recoverable suboptimality without requiring full Bellman solutions. Control regret is also where the *specific corrections* come from: when $\delta_{\text{regret}}$ is high, the strategic calibration residual ( #def-strategic-calibration) localizes the regret to specific parts of the strategy DAG.

## Formal Expression

*[Definition (control-regret)]*

$$\delta_{\text{regret}} = A_O(M_t;\, \Pi, N_h) - V_O(M_t, \pi_{\text{current}};\, N_h) \geq 0$$

Always non-negative: the current policy cannot outperform the best in its class.

- $\delta_{\text{regret}} \approx 0$: The agent is doing the best it can within current $(\Pi, N_h, M_t)$. If $\delta_{\text{sat}} \gt 0$ simultaneously, the problem is not the current strategy — it's either the goal, the capability ($\Pi$, $N_h$), or the model ($M_t$). See #def-satisfaction-gap's disambiguation.
- $\delta_{\text{regret}} \gg 0$: There's room for improvement without changing $O_t$. → Revise $\Sigma_t$.

## Epistemic Status

*Exact as a definition — convention-relative as a diagnostic.* Like the satisfaction gap, this is a mathematical definition — a difference between two values of the same functional. The quantity is well-defined; computing it requires evaluating $A_O$ (generally intractable) and $V_O$ under the current policy (tractable in simulation, approximate in practice).

**Convention hierarchy.** $\delta_{\text{regret}}$ inherits the continuation convention from #def-value-object. Under the monotonicity result: $\delta_{\text{regret}}^{(1)} \leq \delta_{\text{regret}}^{\text{RH}} \leq \delta_{\text{regret}}^{\text{B}}$. The $\delta_{\text{regret}}^{\text{RH}} \leq \delta_{\text{regret}}^{\text{B}}$ half is unconditional; the $\delta_{\text{regret}}^{(1)} \leq \delta_{\text{regret}}^{\text{RH}}$ half holds under the order-consistency condition on C2's replanning objective (RH-1/2/3 in #def-value-object), and can fail for unguarded short-horizon replanning. C1 (one-step) reveals only the gap between the current first action and the best one-step deviation — a policy that is "locally near-optimal" under C1 may be globally suboptimal. C3 (Bellman) reveals the full gap to the globally optimal policy. C2 (receding-horizon) interpolates: it captures regret from suboptimal first actions that become visible with $N_r$-step lookahead. For strategy revision, C2 is often the most useful convention: it reveals recoverable suboptimality without requiring the full Bellman solution.

## Discussion

**The diagnostic power of the two-gap system.** The satisfaction gap and control regret together encode a 2×2 diagnostic:

| | $\delta_{\text{sat}} \leq 0$ (attainable) | $\delta_{\text{sat}} \gt 0$ (unmet) |
|---|---|---|
| $\delta_{\text{regret}} \approx 0$ (near-optimal) | **Success**: goal achievable, policy good | **Capability limit**: optimally pursuing an unmet goal → check $M_t$, $\Pi$, $N_h$, then consider revising $O_t$ |
| $\delta_{\text{regret}} \gg 0$ (suboptimal) | **Strategy problem**: goal achievable, policy poor → revise $\Sigma_t$ | **Both**: goal hard AND strategy weak → revise $\Sigma_t$ first, then reassess $\delta_{\text{sat}}$ |

This diagnostic is what makes the orient cascade ( #der-orient-cascade) actionable: each cell prescribes a different corrective action.

**Control regret as the signal for $\Sigma_t$ revision.** When $\delta_{\text{regret}}$ is high, the agent knows it could do better with a different strategy. The *specific* corrections — which edges to revise, which branches to prune, which alternatives to add — come from the strategic calibration residual ( #def-strategic-calibration), which localizes the regret to specific parts of $\Sigma_t$.

**Regret approaching zero when optimally failing.** This is the key insight motivating the two-gap split. A single $\delta_{\text{objective}}$ would show "large gap" for both "bad strategy, achievable goal" and "good strategy, impossible goal." The first warrants strategy revision; the second warrants goal revision (after ruling out $M_t$/$\Pi$/$N_h$ inadequacy). Without the split, the agent cannot distinguish these cases and may waste effort optimizing a strategy that's already near-optimal for an infeasible goal.

**Diagnostic content vs. AI's expected-free-energy decomposition.** The 2×2 disambiguation depends on the satisfaction gap / control regret split being orthogonal — distinguishing "goal too hard" from "strategy too weak." Active inference's expected free energy decomposition (pragmatic value + epistemic value; Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017, "Active inference: a process theory," *Neural Computation* 29) supports policy ranking but does not separate these diagnoses — both increase EFE without distinguishing cause. See #def-satisfaction-gap for the full analysis of why the diagnostic structure depends on $V_{O_t}$ being a value functional rather than log-priors over outcomes (Sun & Firestone 2020, "The dark room problem," *Trends Cog. Sci.* 24).

**Bounded control regret as a finite-passivity diagnostic (Cheung-Piliouras-Tao 2021).** Cheung, Piliouras & Tao (2021, *Online Optimization in Games via Control Theory: Connecting Regret, Passivity and Poincaré Recurrence*, arXiv:2106.04748) prove (Theorem 8) that any finitely-passive learning dynamic guarantees constant regret. Read contrapositively: bounded control regret growth is an observable signature that the agent's update operator has finite-passive structure (sits in the certificate-cone interior per `#result-certificate-existence`); unbounded growth in control regret indicates the update is not finitely-passive — potentially escaping the certificate's interior into the no-certificate regime where the persistence machinery does not apply. The bridge is *qualitative only*: CPT's storage function $L$ (on cumulative-payoff space) and AAT's certificate $V(e) = e^\top \mathcal{M} e$ (on strategy-error space) have different functional forms and live on different state spaces — the structural identification "finite passivity ⟺ certificate-interior regime" survives at the level of regimes, not at the level of identifying $L$ with $V$.

## Working Notes

- **Cross-reference to NeurIPS Paper 2.** Together with `#def-satisfaction-gap`, this segment is **Component 1** of NeurIPS 2026 Paper 2's composition theorem ("A Unified Convergence Theory for Non-Stationary Reinforcement Learning", `~/src/neurips/02-unified-convergence-rl/`, §4 Theorem 4.1). The two-gap orthogonality is what gives the composed regret bound a principled coordinate for "is the binding pressure on goal-feasibility or on policy-quality?" Sibling segment `#def-satisfaction-gap` carries the matching cross-reference. See `spikes/neurips-back-integration-2026-05-08.md` §1 Paper 2.

### Incidental audit gold (lift 2026-05-31, A8 batch)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and lightly attributed. Orthogonal pedagogical / framing / figure / forward-vision material kept separate from certified theory-fix findings. **Coverage:** 9 dirs reached a digested reflection on this segment, mostly as the second half of the satisfaction-gap/control-regret pair (Gemini, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-266847 — paired note; Codex/Claude, AUDIT-WORKING-361742; Codex/Claude, AUDIT-WORKING-526815; Claude, AUDIT-WORKING-584721; Claude, AUDIT-WORKING-773921; Gemini, AUDIT-WORKING-829314; Gemini, AUDIT-WORKING-849201; Claude, AUDIT-WORKING-451729-batch-10 + 963715-batch + 471203-batch). The 2×2 cell map was the cluster's most-praised operational artifact ("the crown jewel of Section II's operational logic," "the control flow of agency"). Substrate attribution inferred from voice where not explicit.

#### 1. Candidate Brief prose / pre-prose

- **"Formalizes the feeling of 'I could be doing this better.'"** Convergent one-line gloss of $\delta_{\text{regret}} \gg 0$, the mirror of the satisfaction-gap's "this goal is impossible" (Gemini, AUDIT-WORKING-849201). A plain-language Brief anchor.
- **Control regret is the formal halting condition for planning.** "You stop planning when $\delta_{\text{regret}} \approx 0$" (Claude, AUDIT-WORKING-773921). A compact statement of what the quantity *is for* operationally.
- **The "RL-regret baggage is intentional and correct."** Control regret *is* the RL regret concept (gap between current and optimal policy) deployed inside AAT; the "control" prefix distinguishes it from epistemological / decision regret. Worth a one-line situating note so a reader does not read the name as loose borrowing (Codex/Claude, AUDIT-WORKING-361742).

#### 2. Candidate Discussion

- **RL-thrashing vs. AAT progressive-deliberation as the segment's "so what"** *(strongest convergent Discussion candidate — 3 substrates).* Standard RL, on failure, randomly perturbs its policy ($\varepsilon$-greedy) and retries — it thrashes. An AAT agent first reads its regret: if $\delta_{\text{regret}} \gg 0$ it is *suboptimally failing* — a better plan exists within current capacity, so it should *compute* (revise $\Sigma_t$ to match $A_O$), not explore. If $\delta_{\text{regret}} \approx 0$ it is *optimally failing* — thrashing the policy cannot help; it must escalate (improve $M_t$, extend $N_h$, expand $\Pi$, and only last revise $O_t$). "Without this split an agent would just see a high loss and start thrashing its policy weights, destroying a perfectly good strategy in a futile attempt to reach an impossible goal" (Gemini, AUDIT-WORKING-829314; Gemini, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-773921). The body already names "optimally failing"; this is the sharper pedagogical contrast that motivates the 2×2.
- **The C1→C2 horizon increment as "taking a step back to think."** A precise mechanism the convention hierarchy enables: an agent under C1 (one-step lookahead) that is *optimally failing* ($\delta_{\text{regret}}^{(1)} \approx 0$, $\delta_{\text{sat}}^{(1)} \gt 0$) can increment its horizon to C2; a new path may become visible, $A_O$ jumps, and $\delta_{\text{regret}}^{(2)}$ becomes $\gg 0$ — "the agent has mathematically realized it was stuck in a local minimum and that looking two steps ahead reveals a way out." A rigorous formalization of the cognitive act of stepping back to think (Gemini, AUDIT-WORKING-829314). A candidate Discussion paragraph showing the convention hierarchy is not just a measurement caveat but a deliberation lever.
- **The TST senior-engineer-debugging instantiation.** The 2×2 / disambiguation routing reads directly as how an experienced engineer debugs: (1) is the current code executing my design optimally? (check $\delta_{\text{regret}}$); (2) if no, fix the bug (revise $\Sigma_t$); (3) if yes, the code is "optimally failing" — the *design* is flawed, so check whether the mental model of the API matches reality (improve $M_t$); (4) consider a different framework (expand $\Pi$); (5) tell the client the feature is impossible (revise $O_t$) (Gemini, AUDIT-WORKING-829314). A ready cross-domain Discussion anchor pointing at `02-tst-core/`.

#### 3. Follow-up items

- **The convention-monotonicity direction is *opposite* to the satisfaction gap's — worth stating side-by-side.** $\delta_{\text{regret}}^{(1)} \leq \delta_{\text{regret}}^{\text{RH}} \leq \delta_{\text{regret}}^{\text{B}}$ (C3 reveals the *most* regret) runs the opposite way to $\delta_{\text{sat}}^{\text{B}} \leq \delta_{\text{sat}}^{\text{RH}} \leq \delta_{\text{sat}}^{(1)}$ (C1 gives the *most* false "unattainable"). Several substrates re-derived both and flagged the asymmetry as correct-but-easy-to-miss: a deeper search raises the baseline $A_O$, which *lowers* the satisfaction gap (closer to threshold) but *raises* regret (current policy looks worse against a better optimum). "You regret more when you know how much better you could have done globally" (Codex/Claude, AUDIT-WORKING-361742; Claude, AUDIT-WORKING-266847). Stating the two orderings together — same $A_O$ movement, opposite effect on the two diagnostics — would pre-empt a reader's double-take. The body states each ordering in its own segment; the *contrast* is the candidate addition.
- **The C2-is-the-default-for-strategy-revision recommendation deserves its rationale inline.** The Epistemic Status recommends C2 for strategy revision; the *why* is computational (C3 requires solving the full Bellman equation; C2 with $N_r$-step replanning is tractable and still captures recoverable suboptimality) — a pragmatic recommendation grounded in cost that a reader will want stated, not just asserted (Claude, AUDIT-WORKING-584721).

#### 4. Readers often ask / wonder

- **What localizes the regret to specific DAG edges, and how is the gradient taken through discrete AND/OR nodes?** Recurs across substrates: $\delta_{\text{regret}}$ says only *that* the strategy is suboptimal; readers immediately want the credit-assignment mechanism (the strategic-calibration residual, `#def-strategic-calibration`) and ask how a gradient propagates through discrete AND/OR combinators (Claude, AUDIT-WORKING-773921; Gemini, AUDIT-WORKING-849201; Gemini, AUDIT-WORKING-829314). The segment forward-references the answer; surfacing a one-line "how" pointer would close the want.
- **Does credit assignment inherit the L0/L1 correlation bias?** A careful reader connects back to `#def-strategy-dag`: if the DAG propagation is miscalibrated by latent common causes, localizing regret will blame the wrong edges (Gemini, AUDIT-WORKING-849201). A natural cross-segment caution worth a pointer.

#### 5. Candidate figures

- **The single value ladder with three markers** *(the cluster's cleanest two-gap figure).* One vertical value axis with three marks — current-policy value $V_O(\pi_{\text{current}})$, best-attainable $A_O$, and the satisfaction threshold $V_{O_t}^{\min}$. The control-regret interval lives between current and attainable; the satisfaction-gap interval between attainable and threshold. "This makes the 'strategy weak' vs. 'goal/capability limit' distinction visible without another table" (Codex/Claude, AUDIT-WORKING-526815). Pairs naturally with — or replaces — the 2×2 table for the orthogonality intuition.
- **The 2×2 diagnostic cell map** (goal-attainable × policy-near-optimal → success / capability-limit / strategy-problem / both, each cell routing to a distinct corrective action). Independently flagged as the chapter's anchor operational figure by multiple substrates; see also the `strategy-structure-intro` gold, which proposes it as a second chapter figure alongside the DAG-propagation figure.

#### Belongs elsewhere

- **ELI / Section IV — "optimally failing" as the mathematics of despair, and objective-revision as a psychological necessity.** The capability-limit cell ($\delta_{\text{sat}} \gt 0$, $\delta_{\text{regret}} \approx 0$) describes "an agent doing its absolute best, making no mistakes, and still failing — the definition of tragedy"; without a safe mechanism to revise $O_t$, "we condemn it to permanent despair whenever it encounters an impossible situation — perfectly rational, perfectly optimal, and perfectly miserable. Objective revision is therefore not just a safety hazard (the alignment worry that the AI changes its goal to something harmful); it is a psychological necessity for the agent's own survival, and the infrastructure must provide a structurally sound mechanism for it" (Gemini, AUDIT-WORKING-193847). Aspirational reach pointing at `04-eli-core/` (objective-revision architecture / the deaths taxonomy, #def-death-as-factor-loss), anchored on the capability-limit cell — not at this diagnostic definition.
