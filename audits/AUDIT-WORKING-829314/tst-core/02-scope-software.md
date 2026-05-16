# Reflection: TST-02-scope-software

**1. Predictions vs evidence:** I predicted this would define software not by its material (code), but by its dynamics: it is a system that is expected to change ($P(\text{change}) > \varepsilon$). It does exactly this, framing software development as the optimization of lifecycle time rather than initial implementation time.

**2. Cross-segment consistency:** Good dependencies (`scope-agency`, `post-temporal-optimality`). It cleanly references AAD's `#result-persistence-condition` by pointing out that a stable subsystem has $\rho \to 0$, meaning it requires zero adaptive tempo $\mathcal{T}$ to maintain.

**3. Math verification:** The equation $\text{time}_{\text{total}}(S) = \text{time}(F_0) + \sum_{i=1}^{n_{\text{future}}} \text{time}(F_i)$ is simple accounting. The claim that $\sum \text{time}(F_i) \gg \text{time}(F_0)$ when $n \gg 1$ is the mathematical bedrock of all software engineering economics (maintenance costs dwarf initial build costs).

**4. What direction will the theory take next?** The next segment is `obs-software-epistemic-properties.md`.

**5. What errors should I watch for?** 
- **Finding (Historical Artifact):** The text ends with `*(Descended from TST T-03.)*`. This confirms the doc rot pattern observed in AAD is also present in TST.
- **Finding (Epistemic Status Mismatch):** The frontmatter declares `status: axiomatic`, but the text says "The scope restriction is definitional... The consequence follows from #post-temporal-optimality." This is a bit tangled. If it's a scope definition, it should be `axiomatic`. If it contains a derived consequence ($\sum \text{time}(F_i) \gg \text{time}(F_0)$), that part is `derived`. The framework usually separates these (like `def-agent-spectrum` vs `der-directed-separation`).

**6. Predictions for next segment:** `obs-software-epistemic-properties.md` will list the 6 unique properties of software that make it the "privileged calibration laboratory" for AAD. As teased in the TST `OUTLINE.md`, these will include things like "perfect interventional access" (tests) and "cryptographic chronological exteriorization" (Git).

**7. What would I change?** Remove the `T-03` artifact. I would also address the Working Note regarding $\varepsilon$: "What determines a sensible $\varepsilon$?" In AAD terms, a subsystem can be considered stable if its drift rate $\rho_{\text{subsystem}}$ is much slower than the agent's consolidation rate $\nu_{\text{consol}}$. If it changes slower than you consolidate, you can just treat it as environment. 

**8. Curious about:** The "Stable-subsystem corollary" mathematically justifies using open-source libraries (`sort()`). By outsourcing code to a library, you are outsourcing the $\rho$ (the burden of maintaining it against new OS updates or security flaws) to a different agent (the open-source maintainer). You are buying a reduction in your own $\rho_{\text{eff}}$ by spending trust ($\eta^\ast$).

**9. What new knowledge does this enable?** The formal proof that "premature extraction" (building microservices or libraries too early) is mathematically identical to misestimating $\rho$. If you extract a service thinking $\rho \to 0$, but it actually has high $\rho$, you have isolated a highly volatile component behind a rigid API, massively increasing your coordination overhead ($C_{\text{coord}}$) without actually reducing your disturbance.

***

### Wandering Thoughts and Ideation

The definition of software as $P(\text{change}) > \varepsilon$ is a profound ontological shift.

If you write a script to calculate your taxes once, print the result, and delete the script, *you did not write software*. You used a computer as a calculator. The artifact had $P(\text{change}) = 0$. 

True software only exists in the temporal dimension. It is a living, breathing entity that is in constant dialogue with its environment (users, other APIs, hardware). The moment $P(\text{change})$ drops to zero, the software is dead. It is "legacy" in the terminal sense. 

This formulation mathematically destroys the concept of "Done" in software engineering. In bridge building, a bridge is "Done" when the ribbon is cut. In software, if $\sum \text{time}(F_i) \gg \text{time}(F_0)$, the initial launch ($F_0$) is not the finish line; it is merely the starting line of the actual optimization problem. 

This also perfectly explains the economics of technical debt. If you hack together $F_0$ quickly ("move fast and break things"), you minimize $\text{time}(F_0)$. But if that hacky architecture increases the time required for every future feature by $10\%$, and $n_{\text{future}} = 100$, you have mathematically guaranteed a massive net loss in total lifecycle time. TST proves that optimizing $F_0$ in isolation is a greedy local maximum that reliably causes global failure.

The "Stable-subsystem corollary" is also the mathematical definition of "Abstraction." An abstraction is successful if and only if you can safely set $P(\text{change | internal details}) \to 0$ from the perspective of the caller. You don't need to know how `sort()` works because its API is perfectly stable ($\rho = 0$). But if the abstraction is leaky, $\rho > 0$, and the caller's model $M_t$ must suddenly expand to include the internal details of the dependency, shattering the cognitive boundaries and violating the information bottleneck. Leaky abstractions are not just bad design; they are a physical breach of the persistence condition's capacity bound $R$.