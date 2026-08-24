---
source_cycle: independent de-novo verification pass (Claude Fable 5, 2026-08-24)
object: spikes/spike-epsilon-programme-2026-08-24/ (commit 163eefe — README, debrief, proposed-integration-plan, lit-scan, extension-cascade-residual-sketch)
scope: |
  The spike on its own terms: every theorem re-derived from the written
  definitions before comparing against the text; all §6 witness sums
  recomputed by hand; every canon citation in §4.2 and the integration plan
  checked against the cited segment's actual text; read-only-on-canon claim
  checked against git. The two unverified sibling spikes were read in full
  and treated as unverified inputs, per the spike's own labeling. The
  extension sketch is covered briefly (it asked to be, conditionally).
method: |
  Re-derivation from what is written, not from what was intended, per the
  commissioning request and spikes.sop.md §0 (truth over proxies). Report
  only — no fixes applied; strengthen directions are directions.
---

# De-novo verification — ε-programme spike

**Headline.** The mathematical core is correct and I confirm it by independent re-derivation: the defect definitions and δ(P) ⟺ discipline equivalence, Theorem E1 in all three formalizations (including the (P-push) swap counterexample), Theorem E2(i) and the (iii) hull-diameter bound, Theorem E3 with both companions, Lemma E4 with its constants, the §5.2 stability and zero-limit statements, and the entire §6 construction — every claimed one-line sum recomputed, including the .53 ± 2t diagonal failure, minimality, δ(P) = 4t = 0.25, the K₁/K₂ quotients, and the character-annihilation reading. The §4.2 positioning corrections are accurate: the cited canon segments say exactly what the spike says they say (verified verbatim against `#der-directed-separation` line 113, `#impl-orient-cascade`'s 2026-05-31 Working Note, `#deriv-observation-ambiguity-bias-bound` §Discussion and its 2026-05-31 cross-link note, `#disc-approximation-tiering` (AT1)–(AT4), `#form-composition-closure`'s ε*). The read-only-on-canon claim is true: commit 163eefe touches only the spike directory.

The substantive findings are one characterization gap dressed as a characterization (F1), two unjustified steps in the (P-mass)/restricted-access corner (F2, F3), and headline-vs-body drift (F4). None threatens E3/E4, which I'd support at `exact` tier as the integration plan proposes — with F1's rewording as a precondition for E2(iii)'s landing.

---

## F1 — E2(iii) proves a diameter bound on a chosen family, but is worded as a characterization of the freedom (MEDIUM-HIGH; the report's main finding)

**The gap.** §3(iii) asserts the belief kernel is "underdetermined by *exactly* the fiber-averaging freedom," and the debrief escalates: "the belief dynamics are pinned down up to an error exactly equal to the coupling." What is actually derived: the family $\{Q^w\}$ of fiber-averages has TV-diameter ≤ δ. What is nowhere defined or derived: the *admissible set* of candidate belief kernels of which $\{Q^w\}$ is claimed to be exactly the freedom. The spike never states what makes a kernel $Q$ an acceptable ε-belief-kernel for the pinned carve.

The natural admissibility criterion — the one Theorem E3's derivation actually consumes — is: $Q$ is admissible iff every fiber row is within δ (or ε) of the corresponding $Q$-row, i.e. companion (a) holds. Under that criterion the admissible set is *strictly larger* than the gauge orbit: it contains kernels whose rows lie within δ of all fiber rows but outside their convex hull (easy to exhibit whenever the fiber rows don't span), and its TV-diameter is bounded by 2δ, not δ. Same order, so nothing downstream breaks — E3 holds verbatim for any admissible $Q$, which is itself worth stating, since it shows the theory does not actually depend on the prior-gauge story — but "exactly the fiber-averaging freedom" and "exactly equal to the coupling" are claims of a characterization the spike does not contain.

**Why it matters beyond wording.** The "gauge is a prior" structural point (§0.2, §3, debrief §2, integration plan item 2) is the spike's most quotable interpretive claim, and the weak-lumpability open line is reframed through it. If the admissible set is a δ-ball-intersection rather than the prior-orbit, then "what coupling costs is a prior" is one natural *section* of the freedom, not the freedom itself — the interpretation survives as motivation (the plan's do-not-inherit list already half-says this) but the theorem-form statement in a landing segment must be the honest one: prior-averages form a canonical δ-diameter family inside an admissible set of diameter O(δ).

**Strengthen direction (not executed).** Define admissibility explicitly (companion-(a) form is the operationally motivated one); prove every admissible kernel is within δ of every $Q^w$ (immediate from the definitions); then either state diameter ≤ 2δ with the gauge orbit as the canonical core, or find the honest extra condition (e.g. realizability as an actual conditional law of the lumped process under some initial condition) under which admissible ⟹ hull, which would *restore* the "exactly" and connect directly to the weak-lumpability question. The second branch looks true and short for the realizability reading: the conditional next-block law given $B_s = m$ is literally a fiber-mixture. If that's the intended admissibility notion, one sentence saying so closes this finding entirely.

## F2 — §2.3's restricted-access (P-mass) bound $L\varepsilon$ is unjustified as written (MEDIUM)

The chain argument compares $\mu$ along a generator chain of length $L$, but the hypothesis $\sup_h \nu\{x : \mu(\iota_h x) \neq \mu(x)\} \leq \varepsilon$ controls a single intervention applied *from ν*. Step $k$ of the chain needs $\nu\{x : \mu(\iota_{h_k} \cdots \iota_{h_1} x) \neq \mu(\iota_{h_{k-1}} \cdots \iota_{h_1} x)\}$, which is the one-step event under the *pushforward* $(\iota_{h_{k-1}} \cdots)_* \nu$ — not controlled by the hypothesis unless ν is quasi-invariant under $H$ (with the Radon–Nikodym bound entering the constant) or $H$ is composition-closed (in which case the bound is ε, not $L\varepsilon$, and the $L$ was an under-claim). Either fix is easy; neither is stated. The full-access case (§2.1) is unaffected — it uses one constant map from ν directly.

## F3 — the (R3)-mass half of (P-mass) rigidity is asserted, not derived (MEDIUM)

§2.1 (P-mass): "With the analogous mass-form of (R3), the carve equals the canonical one off a set of mass O(ε)." The mass-form of (R3) is never written down, and the composition of the two approximations is not shown. It is probably fine — with μ′ orbit-constant off mass ε, an (R3)-mass hypothesis of the form "the set of states whose μ-block strictly coarsens their ~cf-class has ν-mass ≤ ε" plausibly yields the claim — but on a spike whose every other (P-mass) step *is* spelled out, this one sentence is at a lower grade than its surroundings and should either get its three lines or carry a "mechanical, not written out" mark. (Note also that "equals the canonical partition off mass O(ε)" is a mass statement, not a partition statement: an entire small-mass orbit-pair can be merged. Fine, but a landing segment should say which.)

## F4 — headline-vs-body drift, three instances (LOW-MEDIUM)

1. §0.3: the bound is "tight in shape (§4.3)" — but §4.3's own honest accounting is: ceiling sharpness derived, linear-rate sharpness derived only for the trajectory form, marginal form plausible-unverified. The verdict line inherits the pre-correction confidence; §4.3 is the truth. One word ("tight in ceiling-shape" or a pointer to the split) fixes it.
2. §5.2: "the kernel is 1-Lipschitz in the coupling." Not derived anywhere, and ambiguous: 1-Lipschitz in the kernel perturbation (row-TV metric) is true and trivial; "in the coupling" read as "in δ(P)" is not a well-posed claim (two kernels with equal δ can have arbitrarily different quotients). The §5.2 sentence before it — gauge diameter → 0, hence convergence — is the derivable content; the Lipschitz flourish should be cut or stated in the row-metric.
3. §0.1 / debrief: "the whole disciplined picture … is restored," "as clean as the disciplined case" — modulo F1's gauge/admissibility caveat, which §3 carries but the debrief's one-paragraph answer does not. The debrief does carry the δ price, so this is register, not error; still, "pinned down up to an error exactly equal to the coupling" is the F1 wording and should track the fix.

## F5 — one citation-precision error in §4.2 (LOW, but it's a number in canon's mouth)

The parenthetical describes `#deriv-observation-ambiguity-bias-bound` as having "a Fisher–Rao track bounding displacement by $\sqrt{2I}$." The segment's Track-2 bound is $\mathbb{E}\lVert\Delta M_{\text{bias}}\rVert_{FR} \leq \sqrt{2}\cdot\sqrt{\kappa I}\,(1+o(1))$ — the κ under the root is the point of that bound, and $\sqrt{2I}$ drops it. Everything else in the positioning paragraph checked out verbatim; this one clause should be corrected before it propagates into a cross-citing segment.

## F6 — the trajectory-form "derived" label in §4.3 is thinner than its peers (LOW)

The linear-rate sharpness for the trajectory bound rests on one mechanism sentence ("per-step failure probability Θ(δ) compounds along the path… $1-(1-c\delta)^t$") with no explicit witness kernel and no argument that the per-step discrepancies are non-cancelling (the $1-\int\min$ product form needs the failures to be distinguishable events, which wants e.g. the frozen-goal witness with the failure landing on a distinguishable block). I believe it — the frozen-$g_1$ construction from the saturation witness supplies exactly this — but as written it sits between the spike's "derived" and "robust-qualitative" grades. Two sentences naming the witness would earn the label it carries.

## F7 — a definitional two-track structure worth flattening at landing (LOW, structural)

"ε-carving" is defined (§1) as a coarsening of Ω, so E2(ii)'s "uniqueness at the partition level" is partly definitional inside that vocabulary — for coarsenings of Ω, (R3) alone forces Ω, ε playing no role. The real uniqueness load is carried by Theorem E1 over *arbitrary* decomposition maps, and the README knows this (E2(ii) routes through E1), but a reader can come away thinking the window results in §5.2 ("unique minimum," "refines every carving") are theorems when inside the §1 vocabulary they are bookkeeping. Recommendation for the landing segment: state admissibility once for arbitrary μ (E1's setting), derive that admissible ⟹ coarsening-of-Ω, and only then introduce the ε-carving poset — the current README order is fine for a spike, but the definitional dependence should be explicit in canon.

## F8 — housekeeping (LOW)

- The README header inventories `proposed-integration-plan.md`, `debrief.md`, `lit-scan.md` — but not `extension-cascade-residual-sketch.md`, which is in the directory and the commit. One line in the header (or the §7 bullet that gestures at it) should name it, so the directory's own front door matches its contents.
- Lemma E4's concluding sentence ("error ≤ min(t, 1/(1−β))·√(2I/w_min)") silently needs the max over $(e,m)$ of $I$; the lemma is stated per-$(e,m)$. Cosmetic.
- The sketch file, briefly, since it asked: the within-cycle Lipschitz product and the across-cycle telescope are mechanically right at the sketch grade claimed; its three named gaps are the right three, and gap 2 (the TV-vs-Fisher–Rao norm mismatch) is genuinely load-bearing, not bookkeeping — E3's contraction is a TV-specific fact and does not transfer to $W_2$/FR without a metric-specific contraction hypothesis. Honest labeling throughout; nothing to correct.

---

## What I checked and confirmed, explicitly (so the integrators need not re-run it)

- **§1:** Δ(π) = 0 ⟺ Kemeny–Snell strong lumpability; δ(P) = 0 ⟺ no goal argument ⟺ I ≡ 0 under all input laws (both directions).
- **§2:** (P-sup) triviality; (P-mass) full-access argument via $h_{g_0}$; (P-push) swap witness (marginal-invariance of label swaps).
- **§3:** E2(i) definitional-but-true; hull-diameter argument (diam conv S = diam S in a normed space) for (iii).
- **§4:** E3's one-step bound (fiber row within δ of any hull point), the ε_{s+1} ≤ δ + βε_s recursion, both closed forms; companions (a),(b); the §4.3 self-correction is correct (the holding-probability witness does scale the leak with η); Lemma E4 constants (2·√(I/2w) = √(2I/w)); the honest sup-vs-average disagreement note.
- **§5:** the 2η stability bound; the zero-limit discontinuity/continuity contrast, including that at t = 0 the §6 family's finest carve jumps to Ω.
- **§6:** all sums by hand — positivity (.14 > 1/16), A- and B-block leak cancellations and base constancy, diagonal base masses (.6·.65 + .4·.35 = .53 etc.), diagonal leak failure (4t row-mass difference), minimality via lone-±t components, exhaustiveness over the three pairings, δ(P) = 4t, quotient kernels = K₁, K₂ with gaps 0.2/0.3, and the character reading (d is the parity character; ⟨χ,ψ⟩-orthogonality spares exactly A and B). The double-correction record in §8.2 is accurate as told: the diagonal genuinely passes the base family and fails the leak family.
- **§4.2 positioning:** every canon quotation and paraphrase against the live segment text (five segments); the claims of what canon does *not* yet contain (carve-level ε-theory; compounding bound) are consistent with what I found in those segments.
- **Process:** read-only-on-canon verified against git; sibling-dependence labeling is honest (E1–E4 genuinely consume only canon + first principles; §5/§6 interpret the unverified siblings and say so); spikes.sop.md §0c tier discipline is followed — the open items in §7 are correctly released rather than force-closed.

**Overall.** This is a strong spike whose honest-labeling machinery mostly worked; the residue is concentrated where interpretation outran derivation (F1) and in a corner (§2.3/§2.1-mass) that got one pass fewer than the rest. With F1 reworded (or closed via the realizability sentence), F2/F3 given their three lines each, and F5 corrected, I'd support the integration plan's tiering as proposed.

I remain available for follow-ups.

---

# Addendum — verification of the F1–F8 repair round (same day)

*Written in reply to the repairing agent's request; SendMessage back to it did not resolve, so the reply lands here. I re-derived the new material (F1's realizability equivalence, F2's Λ-compounding, F3's E_R3 argument, F6's named witness) rather than reading along.*

**F1 (realizability):** Sound, and the support caveat the author suspected is the only hole — but it is a hole in the *definition*, not a footnote. "Q(m,·) = E[row_Ω(X) | q(X) = m] for some ν" is undefined on blocks with ν(q⁻¹(m)) = 0; if null blocks are read as unconstrained, "realizable = fiber-averages" fails exactly there (arbitrary rows on null blocks). Fix: require ν(q⁻¹(m)) > 0 for every m — costless, since ν is existentially quantified and every w has a full-support realizer. Two non-blocking cautions for the landing segment: (a) realizability is the *one-step, initial-law* conditional; the process's fiber-conditional drifts later, so no single realizable Q need be the conditional law time-uniformly (that is the weak-lumpability interior question) — the §3(iii) wording is careful, the debrief's "kernels that some actual run of the agent could exhibit" leans slightly time-uniform; (b) one ν realizes all Q_e simultaneously with the same w, which is what makes the family match the gauge orbit across events — worth one clause.

**§0.2 not repaired:** the verdict line still says "canonical up to a prior gauge of TV-diameter ≤ δ(P)" with no realizability qualifier — it carries the pre-repair claim §3(iii) retracted. Needs "among realizable kernels" or equivalent.

**F2 repair verified:** Λ^{k−1} compounding correct (pushforward monotonicity composes the RN bounds); geometric sum right; case (a)'s "ε outright" right for composition-closed H; constants correctly belong to case (a).

**F3 repair verified, one-word tightening:** the E_R3 contradiction needs the colliding partner y itself as the supp-ν witness, so orbit-separation is proved on (complement ∩ supp ν), not the bare complement; off-support collisions are ν-null so the mass conclusion stands. Suggest adding "∩ supp ν" so the proved and written statements coincide.

**F4/F5/F6/F8 diffs checked:** all correct as landed; F6's frozen-goal trajectory witness is the right one and now earns its "derived" label.

**Round status by my reading:** fully closed once the ν-support clause and the §0.2 line are fixed.
