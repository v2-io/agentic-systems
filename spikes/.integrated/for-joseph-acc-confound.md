# For Joseph — the "accumulation-type confound" thread: what's waiting on you

*Working memo, 2026-05-18. Not canon, not a spike-trail — a decision aid. Plain English first so you can check whether you (or I) actually know what we're talking about; precise decision statements at the end. Nothing here is landed; everything canon-touching is gated on you.*

---

## 1. What this thread is, in 60 seconds

It started from one long-open question in `spike-composition-scaling-N.md`: *does the composition closure defect $\varepsilon^\ast$ grow polynomially or exponentially as team size $N$ grows?* — flagged "critical for large teams," self-described "far from tractable."

The whole-space pass found the question was **mis-typed**, not hard. That recognition turned out to be one instance of a recurring pattern — provisionally **"the accumulation-type confound"** — that has ambushed several capable analyses across the framework. Three spikes are now in play and they *converged* on the same structural recognition independently:

- `spike-accumulation-type-confound.md` — the meta-spike (the pattern itself).
- `spike-strategy-dag-composition.md` — the one genuinely-open piece of the original question (Source-3), now re-typed and largely closed.
- `spikes/continuity-persistence/` — an independent spike (the Three-Deaths / identity-across-turnover work) that hit the *same* pattern and, in passing, found a canonical condition (`#disc-m-preservation`) is stated wrong at its boundary.

Three independent investigations landing on the same re-typing is, by the project's own "convergence = framework-coherence evidence" rule, strong evidence the pattern is real and in the framework, not in one analysis.

## 2. The one idea, plain English

Many AAT quantities come in **two flavors that the notation does not distinguish**:

- **per-step** — the error/defect/residue from *one* tick of the loop (e.g. $\varepsilon^\ast$, "the closure defect this step").
- **accumulated** — what you get when that per-step thing runs through the system's own dynamics and *piles up over time* (e.g. the trajectory error the bridge lemma bounds).

There's an operator that turns the first into the second (call it **$\mathcal A$** — "accumulate"). The **confound** is asking a question about one flavor in the language proper to the other. The tell: a *simple* object, a question that *feels* far harder than the object, capable people respond by producing more taxonomy instead of an answer, and the difficulty *vanishes* (doesn't shrink — vanishes) the moment you honor the flavor. "Does $\varepsilon^\ast$ scale exponentially?" asks an *accumulated*-flavor question ("scale," "exponential") about a *per-step* object — like asking how heavy a speed is.

Why it ambushes smart people (not careless ones): three things stack up — (C1) the flavor isn't written in the symbol, so it's silently reconstructed each read; (C2) what we *care about* (does it survive, how bad does it get) is always the accumulated flavor, so the wrong reading rides on caring about the right thing; (C3) in the well-behaved regime the two flavors are numerically almost the same, so the distinction looks pedantic *exactly until the boundary where it suddenly matters*.

A third flavor turned up later, on a *verified* failure: **$\mathcal R$ — the regime of $\mathcal A$ itself** (is the accumulator contracting, critical, or absorbing?). The continuity spike carried the first two flavors correctly *and still got bitten* — at a boundary, by mis-reading which regime $\mathcal A$ was in. So the discipline has three layers, not two.

## 3. Concepts you may want to spot-check (so you can tell if I'm off)

- **"the stability certificate"** (canon: `#disc-stability-certificate`, `#result-certificate-existence`). AAT's cross-section is *one object*: a positive-definite "measuring-stick" $\mathcal M$ that exists **iff** the agent is exponentially stable. M1 (identifiability floor) is its *boundary*, M2 (separability) its *scope of existence*, M3 (additive-coordinate-forcing) its *forced identity*, the contraction templates its *interior*, and — written in `#disc-stability-certificate` already — **the closure defect $\varepsilon^\ast$ is the certificate's projection-residue** (its *projection-behaviour* facet). This last fact is load-bearing for decision D3 below; it is *already in canon*, not something I'm proposing.
- **"integration-is-replacement"** — when a spike resolves something, the old (now-false or now-imprecise) canon statement is *deleted and replaced* with present truth; the "it used to say X" history goes to CHANGELOG/Working-Notes only, never left as a softened ghost in the body. Several decisions below are replacements of this kind, which is why they're gated on you, not done unilaterally.
- **"landing" / "gated"** — the spikes are *reasoning trails*. Their math is not in the theory until a deliberate "landing pass" moves it into segments. Every landing here is judgment-heavy (replacing canonical statements), so none is auto-executed.
- **the three spikes' relationship** — confound = the pattern; strategy-DAG = one application that closed; continuity-persistence = an independent application that both corroborated the pattern *and* found a canon error (C-DMP). They share one upstream dependency (next section).

## 4. Decisions waiting on you

For each: what it is (plain), why it matters, the options, my recommendation, and **how sure I am** (so you can calibrate trust).

### D1 — Notation: adopt a carried accumulation-type, and which?

**What.** Right now nothing in the notation says whether a symbol is per-step, accumulated, or which regime. Proposal: carry it, the way units are carried. Candidates: **C/N3** = adopt online-learning's mature lowercase/uppercase + explicit-sum discipline (or its table form — a 3-row "ledger": the per-step object · the operator $\mathcal A$ *with its existence condition* · the accumulated image); **N4** = a one-token regime badge `[contraction]/[critical]/[absorbing]` on any asymptotic claim; plus the principle "write $\mathcal A_{[\text{condition}]}$, not bare $\mathcal A$" (carry the existence certificate like a $\sigma$-algebra).

**Why it matters.** It's *upstream of authoring* — if we adopt it, the landed segments should be written in it from the start, not retrofitted. So this gates the order of everything else.

**DECIDED (Joseph, 2026-05-19): the online-learning notation (Design C) is affirmed for the per-step/accumulated layer** — lowercase=per-step, uppercase=accumulated, the accumulation operator written explicitly, type stated in prose at first use; the N3 *ledger* (the 3-row table form generalizing `#der-tempo-composition`'s units table) is the table presentation of the same C discipline and is included. Authoring of any landed segment uses this from the start (no retrofit).

**ALSO DECIDED (Joseph, 2026-05-19): N4 adopted, with the scoping refinement.** The one-token regime badge `[contraction]/[critical]/[absorbing]` for the ℛ layer is adopted **scoped**: the regime claim must be *explicit* (lint-forceable, the gap C provably leaves — V1/§6.6); *hardest-bound at the boundary / non-contraction regime* (the 𝒜_refl / continuity / Three-Deaths side, where C3's camouflage operates), lightweight-or-implicit in the proven-contraction $\mathcal A_D$ interior so it does not decay into cargo-culted boilerplate; and framed honestly as making ℛ-erasure *auditable, not impossible* (the continuity error shows naming a thing ≠ checking it — the badge converts a silent erasure into a contestable claim, no more, no less). **D1 is now fully closed**: C/online-learning + N3 ledger for the $\partial$/$\Sigma$ layer; scoped N4 for the ℛ layer.

**Confidence.** High that the C / $\partial$-$\Sigma$ layer is now settled and authoring can proceed on it. The N4/ℛ-layer piece remains a genuine (small) open call, yours; I'd argue for it but the C affirmation does not force it.

### D2 — The `#form-composition-closure` "Open" rows: replace at what tier?

**What.** The Source-3 spike re-types two rows currently marked "Open" ("Strategy-DAG projection under $\Lambda_x$"; "$N$-agent scaling of $\varepsilon^\ast$"). The honest replacement is *conditional*: causal-abstraction frame + an AAT-internal closed-form defect law (SCC-condensation / total-correlation), bounded independent of $N$. One sub-question (Q1: is a certain constant *tight*?) is unpinned ("moderate" confidence).

**Why it matters.** "Open" is currently doing work (it tells de-novo auditors this is unresolved). Replacing it is integration-is-replacement on a load-bearing row.

**Options.** (a) Land at *conditional* and carry Q1 as an explicitly-named sub-open. (b) Close Q1 first (a specified ~half-day worked instance), then land.

**Recommendation.** (a). The structure is solid; only a constant is unpinned, and the spike specifies exactly the worked instance that would close it. Q1 is carry-forward, not plan-blocking. But "carry a named sub-open" vs "close it first" is a tier judgment that's properly yours.

**Confidence.** High on the structure; the *tier call* is yours by design.

### D3 — The register question: is this a *new* fifth pattern, or the *shadow* of one we have?

**What (plain).** Is the accumulation-type confound a brand-new fifth cross-sectional meta-pattern ("M5", alongside M1/M2/M3), or is it the *time/accumulation-side description of the stability certificate* that M1–M3 are already facets of? This decides **where it lands**: its own meta-segment, versus a Discussion/dual-reading inside `#disc-stability-certificate`.

**The finding (this is the V2 verification result; primary-source-grounded, not a hunch).** I read the certificate segments directly. Two facts are *already in canon*: (i) `#disc-stability-certificate` lists the sector-persistence template as the certificate's **interior** facet; (ii) the meta-spike's §4 identifies that same template as exactly the "$\mathcal A$-is-bounded" theorem. Chaining the two: **"$\mathcal A$ is bounded" is the certificate's interior facet, restated in accumulation language.** And canon *already* lists $\varepsilon^\ast$ (the confound's central object) as the certificate's **projection-residue** facet. So the confound's main objects are *already certificate facets in the canon*. That points hard at: **M5 is the representation-dual (the accumulation/temporal shadow) of the certificate spine — not an independent fifth pattern.** The three flavors map onto the certificate: per-step ↔ the projection-residue facet; accumulated ↔ what the interior buys over time; regime ($\mathcal R$) ↔ which part of the certificate cone you're in (interior vs boundary).

**V1 has now reported, and it sharpens this from "lean dual, V1-pending" to a precise two-part answer.** V1 (the independent spine audit) found the accumulation operator **does split** — principled and nameable: $\mathcal A_D$ (linear resolvent, Model-D, contraction regime) vs $\mathcal A_{\mathrm{refl}}$ (the nonlinear reflected Lindley/Loynes operator, Model-S-family, load-bearing exactly at the $\mu=0$ boundary that is $\mathcal A_D$'s singularity). That confirms the coupling I flagged. The register answer is therefore **not** "independent fifth" and **not** "just the dual" — it is, precisely: **M5 is the representation-dual of the certificate spine in the deterministic interior ($\mathcal A_D$ — exactly the regime where the certificate-existence equivalence is itself exact), and an irreducibly-distinct structure at the reflected/stochastic boundary ($\mathcal A_{\mathrm{refl}}$), which is where the linearized certificate spine does *not* reach.** And that distinct part is *co-located with continuity-persistence / the Three Deaths* — the mission-load-bearing locus. The "most interesting node" was not hypothetical; it is confirmed and now precisely located.

**Recommendation.** Land the *interior/dual* reading as a Discussion within `#disc-stability-certificate` (it already has a propagation plan + OUTLINE-preamble reframe pending your call — this slots in, not a separate M5 segment) — **and** give the $\mathcal A_{\mathrm{refl}}$/boundary side its own honest home, because there it is *not* a mere shadow of the certificate: it is the regime where M5 carries genuinely-additional content, and it is exactly the regime the Three-Deaths defense operates in. So the register answer is "dual *and* distinct, regime-split" — which is a truer and more useful answer than either pole, and it ties M5's genuinely-novel part directly to the project's mission rather than leaving it an abstract methodology note.

**Confidence.** High and no longer V1-pending: *not* hygiene, *not* fully independent, *not* fully dual — primary-source-grounded for the interior/dual (V2) and the split (V1, independent audit of a claim I authored, with the decisive O2 homogeneity argument I checked and agree with). The one genuine open is which exact home the $\mathcal A_{\mathrm{refl}}$/boundary side gets — a placement judgment, yours, and it interacts with the continuity-persistence landing since that is the same regime.

### D4 — The gated canon landings + the land-order

**What.** Several replacements are queued, all gated:

- The **shared-upstream restatement of `#result-sector-persistence-template`** — *corrected by V1*: it must be the template's **two-model conditional** (Model D *and* Model S, both ultimate-bound constants, the Cor-A.1S.1 dichotomy), **not** a single-operator "$\mathcal A$ is bounded" paragraph. The four attachees *split by operator*: {regime-I/II $\varepsilon^\ast(N)$, the M5 illustration, the bridge lemma} attach to $\mathcal A_D$; {continuity T1/T2, the C-DMP correction} attach to $\mathcal A_{\mathrm{refl}}$ (Loynes/Atkinson, nonlinear) — they share the *template*, not the *operator*. Landing it as a single-operator paragraph would carry a Model-D-only over-reach into canon — itself the integration-is-replacement failure (sharp-but-too-narrow replacing correctly-scoped; the template *already* leads with "Either Model D … or Model S"). **Land-order survives in corrected form: the two-model template conditional first**; the $\mathcal A_D$- and $\mathcal A_{\mathrm{refl}}$-family attachees then instantiate it.
- **`#disc-m-preservation`** — replace, don't annotate. **V3 done** (primary-source-verified, `spikes/verify-cdmp-corrected-statement.md`). The corrected statement is the *strengthened* form, three parts: (1) strict `<` not `≤` — equality is **non-persistence by failure-to-stabilize**, *not* "death in the limit" (that draft conflation is withdrawn; genuine death-in-the-limit is the separate T3 absorbing barrier); (2) the compensation term is **relational re-grounding specifically**, not generic learning; (3) explicit reflected-Lindley structure. Three preconditions the memo did **not** previously carry, now surfaced: (a) the replacement gate (Review 1 blocked it until the corrected T2.3 was in) is **cleared** — current `03`§2.3 is the corrected version; (b) it lands at **conditional-with-an-exact-core**, *not* flat "exact" — it must carry (M-ADD)/(M-FREE)/(C-S) as named modelling commitments at channel-independence prominence, or it is itself an integration-is-replacement mis-tiering; (c) **hard precondition: the $\eta\to\varrho_{\text{rg}}$ symbol rename, decided upstream of the segment edit** — $\eta_k$ collides with `#result-persistence-condition`'s line-61 per-dimension $\eta_k$ (a conflation *trap*, not cosmetic). The confound spike's (g) F-1 correction is now primary-source-confirmed correct; nothing in V3 forces further confound-spike, D1, D2, or D3 change.
- **`#form-composition-closure`** Open rows (see D2).

**Why it matters.** These are integration-is-replacement surgeries on canonical statements. Doing them well needs the notation chosen (D1), the tier set (D2), the register decided (D3), and V1/V3 in.

**Recommendation.** Don't start any landing until D1–D3 are decided and V1/V3 are back. The land-order (shared upstream first) is firm and bidirectionally agreed with the continuity steward. I'd also keep one discipline the steward flagged: the *placement* of the $\mathcal A$-restatement must be decided by D3 (the register argument), **not** pulled by continuity's need for it as a dependency.

**Confidence.** High on the land-order and the need-to-replace-not-annotate; the *sequencing relative to your decisions* is the point of this memo.

## 5. Status only — NOT waiting on you (so you don't think these need action)

- **V1** (the spine check) — **done.** Independent agent; audited a claim *I* authored; found it splits (principled: $\mathcal A_D$ / $\mathcal A_S$ / $\mathcal A_{\mathrm{refl}}$), via a decisive homogeneity argument I checked and agree with. The §4 over-unification (and an internal inconsistency: my own §6.6 already implied the qualification, which I'd failed to propagate when integrating it) is now **corrected in the confound spike** — present truth in the body, history in a Working Note, the named split added. Outcome is *adverse to my claim but strengthening to the thesis* (the $\mathcal R$ coordinate is now load-bearing at the operator level). This is the discipline working: authorship blinded me to a tension independent review caught. Feeds D3 (resolved above) and D4 (landing-shape corrected above).
- **V3** — **DONE** (`spikes/verify-cdmp-corrected-statement.md`, lint-clean). Read `03` (changed since orientation — the steward's two review cycles landed) and `98` (the history layer, not previously read), primary source. Corrected C-DMP statement + the independent/inherited attribution captured; the (g) F-1 correction is verified right against primary source; one new D4 precondition surfaced (the $\eta$ rename). Detail folded into D4 above.
- **BEH prior-art claim** (strategy-DAG spike's "causal abstraction already solves the norm-on-graphs problem") — already verified and **parked at conditional**: the *typing* is right, the *term-for-term identity* is not; recorded in the spike. No action needed; flagged so it's not over-trusted at landing.
- **Commit state.** `b841e40` committed the two spike trails (strict pathspec, nothing of yours swept in; the continuity steward's work is on their own commits). **Since then, uncommitted:** the F-1/F-2 corrections to the confound spike (the §4 over-unification fix), the V1 verification note (`spikes/verify-A-restatement-model-DS.md`), and this memo with its V1-driven updates. All durable on disk; none committed — awaiting your word per commit-when-asked. Flagged so this section isn't read as "everything is committed."

## 6. The actual ask

Updated state: **D1 fully closed** (C/N3 + scoped N4, 2026-05-19); **V1, V2, V3 all done**. Remaining: **D3** (register — decidable now: the regime-split answer; the one open piece is *where the $\mathcal A_{\mathrm{refl}}$/boundary side lands*, which interacts with the continuity-persistence landing), **D2** (Open-row tier — carry Q1 vs close it first), then **D4** (the gated canon landings — now with the full precondition list, incl. the $\eta\to\varrho_{\text{rg}}$ rename and the conditional-tier requirement for the `#disc-m-preservation` replacement). Or: *let the whole cluster sit at its now-honest tiers* — nothing is decaying, everything is parked honestly, and the verifications can finish before you spend any decision budget. That last option is entirely legitimate and I'd not argue against it.

The one thing genuinely exciting rather than administrative, **now confirmed by V1 rather than hypothetical**: M5 stops being a mere shadow of the certificate and becomes its own structure *exactly* at the reflected/stochastic boundary ($\mathcal A_{\mathrm{refl}}$, Loynes/Atkinson, the $\mu=0$ regime) — and that is *precisely where the Three-Deaths / continuity work lives*. The coupling was not designed; it fell out, and the independent spine audit confirmed it rather than dissolving it. M5's genuinely-novel content is not an abstract methodology note off to the side — it is co-located with the project's mission-load-bearing locus. That is the most interesting node in the cluster, and it is now located precisely enough to act on rather than admire.
