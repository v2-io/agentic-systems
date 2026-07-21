# Batches 3–4 — Sufficiency → Cycle Engine
**Batch 3:** `#def-model-sufficiency`, `#def-model-class-fitness`, `#the-cycle-in-motion-intro`, `#form-event-driven-dynamics`, `#der-recursive-update`  
**Interleaved appendix:** `#deriv-recursive-update` (first reference)  
**Batch 4:** `#der-action-selection`, `#def-mismatch-signal`, `#result-mismatch-decomposition`, `#emp-update-gain` (+ start of tempo/CIY next)

## What I hadn't anticipated

**Sufficiency is not accuracy.** $S=1$ means nothing left in the history for prediction that the model missed — the history itself can still lie. "I learned everything I could from this biased tape." Separation is clean and important.

**Three-term mismatch decomposition (not two).** Estimation | state-uncertainty floor | channel noise. The middle floor is irreducible by *modeling* but movable by *acting* — that's the door CIY walks through. I expected classic bias-variance; the three-way Pythagorean with Bayes predictor as middle reference is sharper.

**Recursive update uniqueness is definitional at C3.** The appendix is honest: C1/C2 eliminate; C3 is analytical commitment ("if Markov fails, expand $M$"). Physicist's system-boundary trick. The seven attacks are the pedagogical gold — uniqueness by elimination, not "we assume Markov."

**Between-event $g_M$ is load-bearing**, not filler — prediction, uncertainty growth, consolidation. Jump-diffusion hybrid. Sleep/think/replay forced by form.

**Action fluency ≠ model sufficiency.** Chess engine: high S, low fluency. Reflex: opposite. Pressure toward implicit action from persistence (tempo penalty on deliberation).

**Gain collapse = hollow epistrophe.** Cycle runs, mismatch arrives, agent doesn't turn. Truth death is already visible as $\eta^\ast \to 0$ (spurious $U_M\to0$ or $U_o\to\infty$). Opacity of $U_o$ resolved by estimating from innovations — meta-adaptive gain.

**Zero mismatch ambiguity.** Peace or deafness. Confirmation bias indistinguishable from perfect knowledge until you intervene.

**Event $\mathcal{I}(e)$ as formal surprise/boredom.** Multi-channel software table is the pedagogy that makes abstract rates real.

## Wandering thoughts

- **Class fitness as Kuhn formalized / permission to stop gradient descent.** Structured residual signature (not absolute level) as diagnostic — white residual = noisy world, structured = wrong class. How to tell low $\mathcal{F}$ from high $\rho$ remains the burning reader question for Ch.4.
- **Trajectory-indexed $S$** — two forks of same $M_t$ have different sufficiency on different lives. Identity already quantitative.
- **Exploration shatters sufficiency** by changing $a_{t:\infty}$ — policy and $M$ co-define what "enough" means.
- **Agent cannot see the three-term split** — only $\delta$. Active testing required to estimate floors. Identifiability of "bad model vs noisy channel" is structural not statistical.
- **Pedagogy of the cycle intro:** $\eta^\ast = U_M/(U_M+U_o)$ then $\mathcal{T}=\nu\cdot\eta$ then $\lVert\delta\rVert_{ss}=\rho/\mathcal{T}$ — you could almost re-derive the chapter from HFT-with-garbage-model (zero tempo) vs slow-but-high-gain human.

## Questions

1. Residual structure diagnostic for class ceiling vs volatility — how sharp at `#result-structural-adaptation-necessity`?
2. Does correlated sensor noise (GA-1 failure) get a named failure mode downstream?
3. Non-parametric $U_M$ for neural nets — ensembles/dropout as permanent open?
4. Does $g_M$ formally mandate bipartite memory (hippocampal / replay)?
5. Score-function sign convention — any residual ambiguity for gradient updates?
