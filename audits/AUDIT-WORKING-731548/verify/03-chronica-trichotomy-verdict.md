# Verdict: chronica trichotomy / M₀ prior-endowment cluster

**Verifier:** independent adversarial verification, 2026-07-02. Primary sources read: `01-aat-core/src/{def-chronica,form-agent-model,def-model-class-fitness,def-model-sufficiency,form-information-bottleneck,scope-agent-identity}.md`; `03-llm-core/src/{scope-logogenic-agent,obs-context-turnover,disc-m-preservation,der-turnover-information-recursion,hyp-experiential-training}.md`; `04-eli-core/src/der-compensation-channel-uniqueness.md`; `02-tst-core/src/scope-developer-agent.md`; `audits/pending-findings-2026-04-25.md` (F-V5); `doc/audit-routing-instructions.md` (gold-lift SOP); TODO.md, INTEGRATION-CLEANUP-TODO.md, spikes/INDEX.md, LEXICON.md; git log on the three Part-I segments.

## Verdict label

**REAL-BUT-ALREADY-HANDLED** — with one caveat sub-item that is REAL-AND-OPEN-BUT-STAGED (the Part-I one-paragraph clarification, already recorded verbatim in the designated channel), one genuinely fresh minor refinement (the $\mathcal{M}$-for-LLMs ambiguity at `def-model-class-fitness`), and **one substantive warning: the two variants of the proposed "cheap fix" are not equivalent, and the $M_t = \phi(M_0, \mathcal C_t)$ variant would break two downstream results if executed naively.**

## Decisive evidence, by sub-claim

### 1. "No explicit slot for the prior endowment" — FALSE at corpus level; TRUE only of the Part-I segment bodies, where it is a known, routed, staged item

The endowment has first-class, load-bearing treatment in the volumes where the instance lives:

- `03-llm-core/src/scope-logogenic-agent.md` §"The weight-context boundary": *"The LLM's weights encode a vast prior $M_0$… $X_t^{\text{eff}} = (M_0^{\text{weights}}, X_t^{\text{context}})$… The weights provide the prior; the context provides the update."* This is exactly the slot the claim says is missing.
- `03-llm-core/src/obs-context-turnover.md`: $M_0^{\text{weights}}$ is a formal argument of the reconstruction kernel $f_{\text{init}}(\mathcal{E}_{\text{ext}}, p_{k+1}, M_0^{\text{weights}})$, appears in the turnover sufficiency bound (fallback $\approx 1 - S(M_0^{\text{weights}})$), and its Working Notes already treat the fine-tuning axis ($M_0^{\text{w}} \to M_k^{\text{w}}$ between sessions).
- `03-llm-core/src/disc-m-preservation.md`: three-source reconstruction with an explicit $S_{\text{prior}}$ term for the pretrained weights.
- `04-eli-core/src/der-compensation-channel-uniqueness.md`: $M_0^{\text{w}}$ is a named random object under assumption **(FW)**, and the derivation *proves* $I(M_0^{\text{w}}; Y \mid \mathcal{E}_k) = 0$ for individuated identity kernels — weights supply *class*-identity, never *this individual's* continuity. Where the theory needs $M_0$ formally, it introduces it explicitly with named local assumptions.
- Precedent that the framework already enforces this: certified finding **F-V5** (`audits/pending-findings-2026-04-25.md`) used `scope-logogenic-agent` line 70 as *counterevidence* to correct a TST segment that said "context window contents" — and the fix landed (`02-tst-core/src/scope-developer-agent.md:66` now carries the Class-3 caveat). So "the theory's description of its own most important modern instance leaves out most of what the agent knows" is refuted as a corpus-level claim; the corpus has both the correct description and a track record of enforcing it.

What remains true: the **Part-I bodies** of `def-chronica` ("*only* raw material") and `form-agent-model` (realization list: "context-window contents plus retrieved memory") do not state the absorption convention locally. But this is a **known, routed item**: the 2026-05-30 gold-lift sweep (commits `598631e` A1, `c931bcc` A2) placed it in both segments' Working Notes as a follow-up item, *including the exact proposed fix*: `form-agent-model.md:62` — *"Candidate clarification (not yet a finding): write $M_t = \phi(M_0, \mathcal C_t)$, or state that $M_0$ / the model class is absorbed into $\phi$ and $\mathcal{M}$."* Per the gold-lift SOP (`doc/audit-routing-instructions.md` §~356), promotion of staged Working-Notes material into segment bodies is *"a separate, careful later pass paced with the pedagogy work."* Raising this as a fresh unaddressed finding is a regression against that routing.

### 2. Record-vs-trajectory-token — partially in the body already; the precision item is known and routed

- `scope-agent-identity`'s body already distinguishes copyable *state* ($M_t$) from non-copyable *trajectory* ($\mathcal C_t$), and the clone paragraph is careful at the fork: *"A copy shares a prefix of the original's causal history… it does not share the trajectory itself."* The "same causal history $\mathcal C_t$" sentence describes the duplication instant, where the prefix genuinely is shared — that is not a conflation, though it is loose about record vs token.
- The sharper record-vs-token point (the *record* of $\mathcal C_t$ is copyable; the *trajectory token* is not; suggested two-symbol fix $\gamma_t$) is verbatim in `scope-agent-identity` Working Notes §3 "Chronica record-vs-token notation" (Codex/Claude AUDIT-WORKING-526815/742613), plus `def-chronica` WN §3 "Digital-substrate non-forkability needs a two-sentence acknowledgment" and the one-word "state → chronica" tightening. All routed 2026-05-30. Same disposition as (1): known, staged, awaiting the promotion pass.

### 3. `def-model-class-fitness` — the finetuning-vs-in-context ambiguity is a genuinely fresh (minor) refinement

The staged gold on that segment flags the inherited policy/trajectory/well-definedness relativity, but **not** the specific ambiguity "is $\mathcal{M}$ the weight-reachable class or the context-conditioning-reachable class?" The corpus handles the *substance* at the timescale level — within-session weights frozen (`obs-context-turnover`; `hyp-experiential-training` L3 makes weight updates a deliberate, gated act), between-session fine-tuning shifts $M_0^{\text{w}} \to M_k^{\text{w}}$ — but nothing connects that two-timescale story back to $\mathcal{F}(\mathcal{M})$'s definition. A one-sentence relativity note ("$\mathcal{M}$ is indexed to the update channels available at the timescale under analysis; for a frozen-weights session, $\mathcal{M}$ is the context-reachable class and fine-tuning is a structural move") would be a genuine improvement, in the same family as the already-staged relativity note. This is the only piece of the cluster not already in the record. Route: add to `def-model-class-fitness` Working Notes follow-up items.

### 4. Would absorbing M₀ into φ break downstream derivations? — **The two fix-variants differ; one of them would.**

- **Safe variant (convention statement):** "$M_0$ / the model class is absorbed into $\phi$ and $\mathcal{M}$" — i.e., $\phi$ is agent-specific and the endowment fixes *which* $\phi$/$\mathcal{M}$ the agent has. Mathematically a no-op: nothing in Part I quantifies over $\phi$ or requires $\phi$ empty at $t=0$; $M_t$ remains a deterministic function of $\mathcal C_t$. All checked derivations survive. This also matches how `04-eli-core` treats it ((FW): weights fixed *before* the individuated trajectory).
- **Unsafe variant (new argument):** writing $M_t = \phi(M_0, \mathcal C_t)$ with $M_0$ a *random* object carrying environment information breaks at least two things:
  - `def-model-sufficiency`: the reading $S \in [0,1]$ = "fraction of predictive information retained" rests on the identity $I(\mathcal C_t; o \mid M_t, a) = I(\mathcal C_t; o \mid a) - I(M_t; o \mid a)$, which holds *because* $M_t$ is a function of $\mathcal C_t$. With an informative random $M_0$ inside $M_t$, conditioning on $M_t$ can *increase* the numerator (explaining-away), $S$ can leave $[0,1]$, and $S=1$ no longer means "sufficient statistic of $\mathcal C_t$."
  - `form-information-bottleneck`: the segment's *exact* status leans on "the Markov chain $Y - X - T$ holds **by construction**" ($X = \mathcal C_t$, $T = M_t$). An informative random $M_0$ gives $T$ an information path to $Y$ (future observations) not mediated by $X$ — the chain fails and the "exact, applied external theorem" claim with it.
  - (Identifiability/coordinate-forcing results checked at the survey level: they operate on $M_t$'s parameterization and the trajectory, not on $\phi$'s emptiness at $t=0$; no damage found under either variant.)

  So the "one cheap paragraph" is cheap only in the absorb-into-φ form. Where the theory genuinely needs $M_0$ as a random variable (turnover reconstruction, compensation-channel uniqueness), it already introduces it locally with named assumptions — the right pattern, already in use.

### 5. Is "𝒞_t = only raw material" a deliberate scoping? — Partially

Under the absorption convention, "raw material" reads as "the only *variable, agent-acquirable* input" — the prior is machinery ($\phi$, $\mathcal{M}$), not material. That reading is coherent with everything downstream (including `def-model-class-fitness`, whose whole point is that the class $\mathcal{M}$ — endowment — bounds what any amount of chronica can achieve, i.e., the framework *already* separates endowment from experience structurally). But the convention is **not currently stated** in the Part-I bodies; the strict-empiricist sentence is honestly an overclaim-as-written pending the staged clarification. The staged Working-Notes items are the corpus's own acknowledgment of exactly this.

## Regression risk of raising the cluster as fresh findings

- **High** for sub-claims 1–2 raised as "unaddressed": they re-litigate items routed 2026-05-30 through the designated gold-lift channel with the fix already recorded, and the "most important modern instance" rhetoric contradicts `scope-logogenic-agent`'s explicit treatment plus the F-V5 landed precedent.
- **High** for the fix if executed in the $\phi(M_0, \mathcal C_t)$-with-random-$M_0$ form (breaks `def-model-sufficiency` normalization + `form-information-bottleneck` exactness).
- **None** for sub-claim 3 (the $\mathcal{M}$ timescale-relativity note) — genuinely additive.

## Disposition

1. **No new finding for the M₀ slot or record-vs-token** — both are staged Working-Notes items awaiting the Brief/Discussion promotion pass; the promotion pass is the vehicle, not a fresh audit finding.
2. **When the promotion pass executes**, prefer the absorb-into-φ convention sentence over the $\phi(M_0, \mathcal C_t)$ signature change; if the signature form is ever wanted, it needs a named assumption (constant/agent-indexed $M_0$, or an (FW)-style independence clause) and a re-check of `def-model-sufficiency` + `form-information-bottleneck`. This warning is the one genuinely new *technical* content of this verification — worth carrying into the Working-Notes item so the future promoting agent inherits it.
3. **Add one Working-Notes follow-up to `def-model-class-fitness`**: $\mathcal{M}$'s relativity to available update channels / timescale (frozen-weights session vs fine-tuning), connecting to `obs-context-turnover` WN's fine-tuning note.
4. Nothing here needs Joseph before the normal promotion pass; item 2's variant-discrimination should be visible to him when that pass lands since it touches an axiomatic-tier definition's reading.
