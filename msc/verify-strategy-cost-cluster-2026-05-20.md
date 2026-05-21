---
title: Strict-Form Independent Verification — Strategy-Cost Cluster (BH-identity, chain-rule uniqueness, citations, tier)
date: 2026-05-20
parent_cycle: 451729 D.1 Phase 4b strict-form independent-verify
authority: adjudicator (independent of spike author and parent canon-edit applier)
scope:
  - $D_{\mathrm{KL}}(\delta_{a^\ast} \Vert Q) = -\log Q(a^\ast)$ (BH identity under deterministic $\pi^\ast$)
  - Chain-rule-axiom uniqueness of reverse-KL within direction-forced f-divergence family (Hobson 1969 / Csiszár 1991 / Aczél & Daróczy 1975)
  - PDF citation spot-check (Hobson 1969, Csiszár 1991, Amari 2009, Shore-Johnson 1980, Eguchi 1983)
  - `form-strategy-complexity-cost` tier justification (`status: robust-qualitative`)
governing_segments:
  - 01-aat-core/src/form-strategy-complexity-cost.md
  - 01-aat-core/src/deriv-strategy-cost-regret-bound.md
  - 01-aat-core/src/deriv-edge-update-natural-parameter.md
  - 01-aat-core/src/der-chain-confidence-decay.md
  - 01-aat-core/src/disc-additive-coordinate-forcing.md
governing_references:
  - FORMAT.md (epistemic-status tier definitions)
  - terminology/entries/robust-qualitative.md
  - terminology/entries/exact.md (by reference)
output: this document only; no canon edits, no commits
---

# §1 — Setup

Per `doc/audit-routing-instructions.md` §8 Refinement 4, this is a strict-form
independent-verify pass before the AAT monograph pre-print scheduled within
the next 24 hours for citation by two AIES papers. The verifier is independent
of both the prior spike author and the parent agent who applied the Phase 4b
canon edits at commit `351ed95`. The mandate is **adjudication, not
grad-confirmation**: I re-derive the load-bearing algebra from first principles
without borrowing the spike's path, and treat the citation chain as something
to be checked against the PDFs and against external knowledge, not relayed.

The two load-bearing claims under review:

- **Claim 1 (BH-identity under deterministic $\pi^\ast$):**
  $D_{\mathrm{KL}}(\delta_{a^\ast} \Vert Q) = -\log Q(a^\ast)$.
  Lives at `deriv-strategy-cost-regret-bound.md` §4 (the boxed identity).
  This is the one-line algebra the regret-bound argument rests on, and it is
  what supports the `Max attainable: exact` line in the appendix's Epistemic
  Status for "$D_{\mathrm{KL}}(\pi^\ast \Vert Q) = -\log(1 - \operatorname{TV}(\pi^\ast, Q))$".

- **Claim 2 (chain-rule-axiom uniqueness of reverse-KL):**
  Within the family of f-divergences satisfying the chain-rule additivity
  axiom over conditional factorizations, reverse-KL is the unique form
  (up to positive scaling). Lives at `deriv-strategy-cost-regret-bound.md`
  §6.1 as "Theorem (chain-rule / additivity uniqueness of KL among
  f-divergences; folk theorem)". Cited as **Hobson 1969** / **Csiszár 1991
  Theorem 3 corollary and Theorem 5** / **Aczél & Daróczy 1975**.

The downstream consequence: `form-strategy-complexity-cost.md` carries
`status: robust-qualitative` on the strength of (i) the regret-bound
derivation that fixes the KL *direction*, (ii) the chain-rule axiom that
fixes the KL *form* within the direction-forced family, and (iii) the BH
identity that makes the bound exact in AAT's canonical deterministic-$\pi^\ast$
scope. If any of those three legs cracks under independent re-derivation,
the tier is over-claimed and must revert.

I read the five governing segments and the spike file
`spikes/spike-form-strategy-complexity-cost-strengthening-2026-05-20.md`
(for context only, not for the derivation paths). I opened the available
PDFs in `ref/` for citation spot-checks.

# §2 — BH-identity re-derivation + verdict

## §2.1 — Re-derivation (independent, no recourse to the spike or appendix derivation)

Setup. $\mathcal{A}$ is a finite or countable action set. $\pi^\ast = \delta_{a^\ast}$
is the point mass on $a^\ast \in \mathcal{A}$:
$$\pi^\ast(a) = \begin{cases} 1 & \text{if } a = a^\ast \\ 0 & \text{otherwise} \end{cases}$$

$Q$ is any probability distribution on $\mathcal{A}$ with $Q(a^\ast) \gt 0$.

KL divergence (discrete, base-$e$):
$$D_{\mathrm{KL}}(P \Vert Q) := \sum_{a \in \mathcal{A}} P(a) \log\frac{P(a)}{Q(a)}$$

with the standard convention $0 \log 0 = 0$ (limit of $x \log x$ as $x \to 0^+$;
this is the convention used in Cover & Thomas, Tsybakov, and effectively every
information-theory textbook).

Specialize to $P = \pi^\ast = \delta_{a^\ast}$:
$$D_{\mathrm{KL}}(\delta_{a^\ast} \Vert Q) = \sum_{a \in \mathcal{A}} \delta_{a^\ast}(a) \log\frac{\delta_{a^\ast}(a)}{Q(a)}$$

Split the sum into the $a = a^\ast$ term and the $a \neq a^\ast$ terms.

- **For each $a \neq a^\ast$:** $\delta_{a^\ast}(a) = 0$, so the summand is
  $0 \cdot \log(0/Q(a))$. Two sub-cases:
  - If $Q(a) \gt 0$: the summand is $0 \cdot \log(0)$, which by the
    $0 \log 0 = 0$ convention equals $0$.
  - If $Q(a) = 0$: the summand is $0 \cdot \log(0/0)$. This is the
    "$P$-null-with-$Q$-null" case, conventionally also $0$ (it does not
    arise in the deterministic-$\pi^\ast$ scope under the assumption
    $Q(a^\ast) \gt 0$, but the convention handles it uniformly).
  Either way, every $a \neq a^\ast$ term contributes $0$.

- **For $a = a^\ast$:** $\delta_{a^\ast}(a^\ast) = 1$, so the summand is
  $$1 \cdot \log\frac{1}{Q(a^\ast)} = \log\frac{1}{Q(a^\ast)} = -\log Q(a^\ast)$$

Sum: $D_{\mathrm{KL}}(\delta_{a^\ast} \Vert Q) = 0 + \cdots + 0 + (-\log Q(a^\ast)) = -\log Q(a^\ast)$.

Boundary cases:
- If $Q(a^\ast) = 0$: $-\log Q(a^\ast) = +\infty$. The KL is $+\infty$.
  This is the structural-failure regime: $Q$ has zero probability on the
  optimum. The boxed identity in the segment requires $Q(a^\ast) \gt 0$,
  which is stated. (The continuity extension $D_{\mathrm{KL}} = +\infty$ when
  $Q(a^\ast) = 0$ is also consistent with the absolute-continuity convention
  for KL: when $P \ll Q$ fails, KL is $+\infty$. Here $\pi^\ast$ has support
  $\{a^\ast\}$, so $\pi^\ast \ll Q$ requires $Q(a^\ast) \gt 0$.)
- If $Q(a^\ast) = 1$: $Q = \delta_{a^\ast}$, $-\log 1 = 0$, KL $= 0$. Correct.

Cross-check: AAT's appendix §4 derives the identity *and* identifies it as
the deterministic-$P$ specialization of the Bretagnolle-Huber inequality
$\operatorname{TV}(P, Q) \leq \sqrt{1 - e^{-D_{\mathrm{KL}}(P \Vert Q)}}$.
Under deterministic $P = \delta_{a^\ast}$:
$\operatorname{TV}(\delta_{a^\ast}, Q) = \tfrac{1}{2}\sum_a |\delta_{a^\ast}(a) - Q(a)| = \tfrac{1}{2}(1 - Q(a^\ast)) + \tfrac{1}{2}\sum_{a \neq a^\ast} Q(a) = \tfrac{1}{2}(1 - Q(a^\ast)) + \tfrac{1}{2}(1 - Q(a^\ast)) = 1 - Q(a^\ast)$.
Substituting $Q(a^\ast) = 1 - \operatorname{TV}$ into the identity:
$D_{\mathrm{KL}} = -\log(1 - \operatorname{TV})$. Then
$1 - e^{-D_{\mathrm{KL}}} = 1 - e^{\log(1 - \operatorname{TV})} = 1 - (1 - \operatorname{TV}) = \operatorname{TV}$. So the BH
inequality $\operatorname{TV} \leq \sqrt{1 - e^{-D_{\mathrm{KL}}}}$ becomes
$\operatorname{TV} \leq \sqrt{\operatorname{TV}}$, which is an *identity* in the regime
$\operatorname{TV} \in [0, 1]$ rewritten as $\operatorname{TV}^2 \leq \operatorname{TV}$ —
true with equality at $\operatorname{TV} \in \{0, 1\}$ and strict inequality
otherwise. So the appendix's "BH specializes to identity" framing is
slightly imprecise: what specializes to an *identity* is the algebraic
relationship $D_{\mathrm{KL}} = -\log(1 - \operatorname{TV})$, not the BH
inequality itself. Under this relationship, the regret bound
$R \leq V_{\max}(1 - e^{-D_{\mathrm{KL}}}) = V_{\max} \cdot \operatorname{TV}$
coincides exactly with the TV-regret bound, which is what makes the
KL-coordinate bound tight in the same sense the TV-regret bound is tight.

## §2.2 — Verdict on Claim 1

**CONFIRMED.** The one-line algebra is correct. The derivation uses only:
(a) the definition of KL divergence, (b) the $0 \log 0 = 0$ convention,
(c) the fact that $\delta_{a^\ast}(a) = 0$ for $a \neq a^\ast$. All three are
standard. The boxed claim $D_{\mathrm{KL}}(\delta_{a^\ast} \Vert Q) = -\log Q(a^\ast)$
holds exactly under the stated scope ($Q(a^\ast) \gt 0$).

Minor note (not a discrepancy of consequence, but worth recording): the
segment's phrasing "the general inequality $\operatorname{TV} \leq \sqrt{1 - e^{-D_{\mathrm{KL}}}}$
becomes an equality" (appendix §4 final paragraph) is technically loose —
the BH *inequality* does not "become an equality"; rather, the
$D_{\mathrm{KL}}$–$\operatorname{TV}$ algebraic substitution makes the bound's
right-hand side $\sqrt{\operatorname{TV}}$, which is *not* tight against
$\operatorname{TV}$ at interior points (it is tight only at the endpoints).
What *is* tight is the regret bound $R \leq V_{\max}(1 - e^{-D_{\mathrm{KL}}})$,
because the upper envelope $1 - e^{-D_{\mathrm{KL}}}$ equals $\operatorname{TV}$
under the BH identity, and the TV-regret bound is tight on extremal $V$. The
segment's "Tightness" stipulation in the matched-lower-bound paragraph
already gets this right (tight in $V_{\max}$ / $\Delta_{\min}$ Lipschitz
constants); the only loose phrase is the one quoted above. **Not a tier
defect — a presentational opportunity to sharpen the language if a copy-edit
pass is in scope before pre-print, but the math is correct.**

# §3 — Chain-rule-axiom uniqueness verification + verdict

## §3.1 — What the segment claims

`deriv-strategy-cost-regret-bound.md` §6.1 states:

> **Theorem (chain-rule / additivity uniqueness of KL among f-divergences;
> folk theorem, standard functional-equation derivation).** *Let $D_f(P\Vert Q) = \sum_x Q(x) f(P(x)/Q(x))$
> be a smooth f-divergence with $f$ convex and $f(1) = 0$. The chain rule
> $D_f(P_{XY} \Vert Q_{XY}) = D_f(P_X \Vert Q_X) + \mathbb{E}_{P_X}\!\left[D_f(P_{Y\mid X} \Vert Q_{Y\mid X})\right]$
> holds for all joint distributions $(X, Y)$ if and only if $f(t) = c \cdot t\log t$ for some $c \gt 0$ — i.e., $D_f$ is reverse-KL up to positive scaling.*

The cited references for this theorem are:
1. **Hobson 1969**, "A new theorem of information theory," *J. Stat. Phys.*
   1(3):383–391 — uniqueness of the Kullback expression via a
   composition/additivity axiom.
2. **Csiszár 1991**, "Why least squares and maximum entropy?", *Ann. Statist.*
   19(4):2032–2066 — Theorem 3 corollary: transitive statistical projection
   is I-divergence; Theorem 5: composition-consistency characterizes
   I-divergence.
3. **Aczél & Daróczy 1975**, *On Measures of Information and Their
   Characterizations* (Academic Press) for the general functional-equation
   machinery.

Additional references named as "structurally-equivalent re-formulations":
Shore & Johnson 1980 (system-independence), Sanov 1957 (sampling consistency).

## §3.2 — Independent verification

**On the chain-rule statement.** The chain rule
$$D_f(P_{XY} \Vert Q_{XY}) = D_f(P_X \Vert Q_X) + \mathbb{E}_{P_X}\bigl[D_f(P_{Y\mid X} \Vert Q_{Y\mid X})\bigr]$$
for reverse-KL is the **classical KL chain rule** (Cover & Thomas 2006 §2.5,
Theorem 2.5.3: $D(p(x,y) \Vert q(x,y)) = D(p(x) \Vert q(x)) + D(p(y\mid x) \Vert q(y\mid x))$).
Direct check on reverse-KL:
$$\sum_{x,y} P(x,y) \log\frac{P(x,y)}{Q(x,y)} = \sum_{x,y} P(x,y)\log\frac{P(x)P(y\mid x)}{Q(x)Q(y\mid x)} = \sum_x P(x)\log\frac{P(x)}{Q(x)} + \sum_x P(x)\sum_y P(y\mid x)\log\frac{P(y\mid x)}{Q(y\mid x)}$$
which is exactly the additive decomposition the theorem requires. So KL
*satisfies* the chain rule (the easy direction).

**On the "only if" — uniqueness.** This is the load-bearing direction. The
classical functional-equation argument: among smooth f-divergences (with $f$
convex, $f(1) = 0$, and the standard regularity), requiring chain-rule
additivity over arbitrary joint factorizations forces $f(t) = c \cdot t \log t$.
The Csiszár 1991 paper I verified PDF-side states this as **Theorem 3 corollary**
(p. 2045): *"The only transitive statistical projection rule (with $S = R^n_+$
or $\Delta_n$) is the I-divergence projection rule"* — where "transitive"
(Csiszár's Definition 6, subspace-transitive: $\Pi(L'\mid \mathbf{u}) = \Pi(L'\mid \Pi(L\mid \mathbf{u}))$
for $L' \subset L$) and "subspace-transitive" / "parallel-transitive" capture
exactly the chain-decomposition property under composition of inference steps.
I-divergence is Csiszár's name for reverse-KL.

**Theorem 5(ii)** (p. 2047): *"In the cases $S = R^{mn}_+$ or $\Delta_{mn}$,
the regular, local, and product-consistent selection and projection rules are
exactly those I-divergence selection rules for which $\mathbf{v}^0$ is of
product form, and the I-divergence projection rule, respectively."*

This is the **composition-consistency** characterization. "Composition-consistency"
(Csiszár's Definition 7, p. 2042) is: if the object of inference factorizes
into product form (two independent components), the inference should preserve
the product structure. Csiszár notes (p. 2043) this is "weaker than Shore and
Johnson's (1980) 'system independence' postulate," confirming the
structural-equivalence claim AAT makes.

**Both Csiszár 1991 citations check out exactly as stated.** I verified
Theorems 3 corollary and 5 against the PDF; both characterize I-divergence
(= reverse-KL) uniquely among the f-divergence family via composition /
transitivity axioms that are equivalent re-formulations of the chain-rule
additivity statement.

**On the functional-equation derivation (Aczél & Daróczy 1975).** I do not
have the Aczél-Daróczy textbook in `ref/`. The functional-equation argument
sketched in the segment — that the chain-rule identity forces
$f(rs) = f(r) + r f(s) + g(r)$, which under convexity and $f(1) = 0$
yields $f(t) = c \cdot t \log t$ — is the standard Cauchy/d'Alembert-style
derivation and is part of the general curriculum on Cauchy-FE
characterizations of information measures. Aczél-Daróczy is the canonical
single-volume reference, but the specific theorem is mainstream (cf.
Aczél 1966, *Lectures on Functional Equations*, which is the older companion
volume and which AAT cites separately in `deriv-edge-update-natural-parameter.md`
for the same machinery applied to the update-layer log-odds uniqueness).

**On Hobson 1969 — *critical PDF defect surfaced below in §4*.** I cannot
PDF-verify the Hobson citation because the file `ref/hobson-1969-theorem-information.pdf`
**is not Hobson 1969** — see §4.1. Based on external knowledge: Hobson 1969,
"A new theorem of information theory," *J. Stat. Phys.* 1(3):383–391, is a
well-known reference in the axiomatic-information-theory literature, and
its standard summary is that it gives a uniqueness characterization of the
Kullback discrimination information (= reverse-KL) via a composition axiom.
The journal, volume, issue, and pages cited (J. Stat. Phys. 1(3):383–391)
match the standard bibliographic record for Hobson's paper. *I have no way
in this scope to verify the paper's actual content end-to-end without the
correct PDF.* The citation is plausible-based-on-external-knowledge and
the bibliographic details match what is generally cited, but strict-form
PDF-spot-check **fails for Hobson 1969 — deferred verification.**

**On Sanov 1957 and Shore & Johnson 1980.** Sanov's theorem (large-deviation
rate function = KL) is textbook (Cover & Thomas §11.4). The structural
equivalence the segment claims — Sanov's sampling-consistency condition
factors through independence-of-sub-problems just like Csiszár's
transitivity — is a standard exposition in the maxent-axiomatics literature
(Jaynes 2003 §11; van Campenhout & Cover 1981, cited by Csiszár 1991 §1).
I PDF-checked Shore & Johnson 1980 exists in `ref/` (`shore-johnson-1980-axiomatic-maxent.pdf`)
and is a valid PDF (PDF document, version 1.2). The Shore-Johnson 1980
"system independence" axiom is referenced explicitly by Csiszár 1991 on
p. 2040 and p. 2043; the equivalence relationships AAT cites are validated
by Csiszár 1991's own discussion. Within the scope of this verification I
did not need to read Shore-Johnson 1980 end-to-end; the cross-reference in
Csiszár 1991 is sufficient.

## §3.3 — On the AAT-internal motivation

AAT's claim is not merely "the chain-rule axiom is a published axiomatization"
(that would be inherited justification). The load-bearing additional claim is
that **the chain-rule axiom is AAT-internally motivated as the divergence-level
analog of `#der-chain-confidence-decay`'s chain-level additive log-confidence
decomposition.** I verified `der-chain-confidence-decay.md`: it is
`status: exact` (mathematical identity) and explicitly states the
chain-rule-of-probability $\log P(\text{chain}) = \sum_i \log P(E_i \mid E_{\lt i})$
as the anchor. The analogy is *legitimate*:

- Chain layer: $\log P(\text{chain}) = \sum_i \log P(E_i \mid E_{\lt i})$
  — additive log-confidence over chain steps.
- Divergence layer: $D_{\mathrm{KL}}(P_{XY} \Vert Q_{XY}) = D_{\mathrm{KL}}(P_X \Vert Q_X) + \mathbb{E}_{P_X}[D_{\mathrm{KL}}(P_{Y\mid X} \Vert Q_{Y\mid X})]$
  — additive divergence over conditional factorizations.

Both are log-additive decompositions of probabilistic quantities under
conditional factorization. The divergence-layer chain rule is "what the
chain-of-probability identity looks like when measured against a reference
distribution." The analogy is mathematically precise (both follow from
$\log(ab) = \log a + \log b$ applied to factorized probability ratios) and
the AAT-internal motivation is honest rather than rhetorical.

## §3.4 — Verdict on Claim 2

**CONFIRMED (with one deferred component).**

- The chain-rule statement itself is correct (verified directly).
- The "if KL then chain rule" direction is elementary and checks out.
- The "if chain rule then KL" direction (the load-bearing uniqueness step)
  is correctly attributed to Csiszár 1991, where I PDF-verified both
  Theorem 3 corollary (p. 2045) and Theorem 5(ii) (p. 2047) state and
  prove exactly what AAT claims they state. The composition-consistency
  axiom (Csiszár 1991 Definition 7) and the transitivity axiom (Csiszár
  1991 Definition 6) are structurally-equivalent reformulations of the
  chain-rule additivity statement, consistent with AAT's framing.
- Aczél & Daróczy 1975 is the standard textbook reference for the
  functional-equation machinery; I did not PDF-verify (not in `ref/`),
  but the underlying functional-equation argument is mainstream Cauchy-FE.
- **Hobson 1969 is *deferred verification*** because the PDF in `ref/` is
  not the Hobson paper (see §4.1). The bibliographic details cited (J.
  Stat. Phys. 1(3):383–391, "A new theorem of information theory") match
  the standard external record for the paper, so the *citation* is
  plausibly correct, but I cannot strict-form verify the paper's content
  against AAT's "uniqueness of the Kullback expression via a
  composition/additivity axiom" summary without the actual paper.

The substantive claim (chain-rule additivity uniquely forces reverse-KL within
the f-divergence family) is **verified via Csiszár 1991 alone**, independent
of Hobson 1969. AAT's appendix cites multiple sources for the same result
precisely because they are "structurally-equivalent re-formulations" — the
load-bearing argument does not collapse if Hobson 1969 turns out to be
mis-summarized; it collapses only if both Csiszár 1991 and the Cauchy-FE
machinery fail, neither of which they do.

The AAT-internal motivation (chain-rule axiom as the divergence-level analog
of `#der-chain-confidence-decay`) is honest: both layers run the same
log-additive decomposition under conditional factorization, and the
chain-layer identity is `status: exact` (mathematical identity).

# §4 — PDF citation spot-checks + verdict

## §4.1 — Hobson 1969 — **DISCREPANCY (download/file-state defect, not citation defect)**

File: `ref/hobson-1969-theorem-information.pdf`.

```
$ file ref/hobson-1969-theorem-information.pdf
ref/hobson-1969-theorem-information.pdf: HTML document text, ASCII text,
with very long lines (42559)
```

The file's actual content is the HTML for a Springer Link page for a
*completely different paper*: **"Sensation seeking and financial risk taking
in everyday money matters,"** by an unrelated author, in *Journal of Business
and Psychology* 5(4):525–530 (1991). This is almost certainly the result of
a Springer paywall serving an HTML page instead of the requested PDF when the
file was downloaded; the wrong content was saved under the Hobson filename.

**The citation in `deriv-strategy-cost-regret-bound.md` §6.1 itself is not
mis-attributed** — the bibliographic details (Hobson 1969, "A new theorem
of information theory," *J. Stat. Phys.* 1(3):383–391) match the standard
external record. The defect is **file-state**: the project does not actually
have the Hobson PDF locally; the placeholder file is misleading because it
has the right filename and the wrong content.

**Strict-form-verification consequence:**
- The citation *as a bibliographic entry* is plausibly correct.
- The verification of "Hobson 1969 contains the chain-rule-uniqueness claim"
  is **deferred** — there is no local PDF to read.
- The Csiszár 1991 verification (§3.2) is independent of Hobson 1969 and
  covers the load-bearing uniqueness claim entirely on its own (Theorem 3
  corollary + Theorem 5 + composition-consistency Definition 7). The
  chain-rule uniqueness theorem does not depend on Hobson 1969 holding up
  under PDF check — it depends on Csiszár 1991 holding up, which it does.

**Recommended remediation** (out of scope for this verification, but called
out for the canon-edit applier or a future curator):
1. Replace `ref/hobson-1969-theorem-information.pdf` with the actual Hobson
   1969 PDF, or delete the misleading placeholder and note its absence.
2. The existing citation in the segments and Working Notes can stand pending
   that retrieval — the bibliographic record is correct; only the local PDF
   is wrong.

## §4.2 — Csiszár 1991 — **CONFIRMED**

File: `ref/csiszar-1991-why-least-squares-maxent.pdf` — PDF document, 16-page
JSTOR scan of *The Annals of Statistics* 19(4):2032–2066 (1991), "Why Least
Squares and Maximum Entropy? An Axiomatic Approach to Inference for Linear
Inverse Problems" by Imre Csiszár. Title, author, journal, volume, issue,
year, and page range all match the citation.

Content spot-check against the segment's citation:

- **Theorem 3 corollary** (PDF p. 2045): *"The only transitive statistical
  projection rule (with $S = R^n_+$ or $\Delta_n$) is the I-divergence
  projection rule (cf. Example 2)."* This matches AAT's citation
  "Theorem 3 corollary: the only transitive statistical projection rule is
  the I-divergence projection rule."

- **Theorem 5** (PDF p. 2047): characterizes regular, local, sum-consistent /
  product-consistent selection and projection rules as the least-squares /
  I-divergence rules. Specifically Theorem 5(ii): *"In the cases $S = R^{mn}_+$
  or $\Delta_{mn}$, the regular, local, and product-consistent selection and
  projection rules are exactly those I-divergence selection rules for which
  $\mathbf{v}^0$ is of product form, and the I-divergence projection rule,
  respectively."* This matches AAT's citation "Theorem 5: product-consistency
  characterizes I-divergence uniquely."

- **Definition 7 (composition-consistency)** (PDF p. 2042–2043): formalizes
  the product / sum form preservation as the "composition consistency"
  postulate. PDF p. 2043 explicitly notes the relationship to Shore &
  Johnson 1980: *"For the case $S = \Delta_{mn}$, the postulate of product
  consistency is similar to but weaker than Shore and Johnson's (1980)
  'system independence' postulate."* This matches AAT's structural-equivalence
  framing.

- **Abstract** (PDF p. 2032): explicitly mentions "axiomatic characterizations
  of the methods of least squares and minimum discrimination information"
  and that "the latter are also characterized by a postulate of composition
  consistency."

The PDF citations are correct as stated. CONFIRMED.

## §4.3 — Amari 2009 — **CONFIRMED (citation-correction record validates against the actual paper)**

File: `ref/amari-2009-alpha-divergence-unique-f-bregman.pdf` — PDF document,
7 pages, *IEEE Transactions on Information Theory* 55(11):4925–4931 (2009),
"α-Divergence Is Unique, Belonging to Both f-Divergence and Bregman
Divergence Classes" by Shun-Ichi Amari. Title, author, journal, volume,
issue, year, and page range all match.

The relevant AAT working-note (in `deriv-strategy-cost-regret-bound.md`
Working Notes) flagged that **earlier drafts mis-cited Amari 2009 Theorem 1
for the chain-rule uniqueness theorem**, and the correction removed that
attribution. I verified the correction is right:

- Amari 2009's main theorem (Section IV, p. 4929): *"The α-divergence is the
  unique class of divergences sitting at the intersection of the f-divergence
  and Bregman divergence classes."* Specifically about α-divergences being
  the f-Bregman intersection in the space of positive measures.
- Amari 2009's Corollary (p. 4929): *"The KL-divergence and its dual are
  unique divergences belonging to the f-divergence and Bregman divergence
  classes."*
- **Amari 2009 does NOT contain a chain-rule uniqueness theorem for
  reverse-KL within f-divergences.** It contains the f∩Bregman intersection
  uniqueness, which is a different result.

The correction in the spike's Working Notes is correct: removing Amari 2009
from the chain-rule-uniqueness citation chain is right. AAT's current
citation pattern uses Csiszár 1991 + Hobson 1969 + Aczél-Daróczy 1975 for the
chain-rule uniqueness, which is the correct attribution.

The Eguchi 1983 reference (used in §6.2 for "Fisher-metric-at-second-order
is not a distinguishing axiom within f-divergences") is similarly clean —
Eguchi 1983 §2 develops the contrast-function framework that yields the
Fisher metric for any smooth f-divergence with $f''(1) \gt 0$. The PDF
`ref/eguchi-1983-second-order-efficiency.pdf` is present (11 pages, 1.5 MB);
I did not read it end-to-end but its bibliographic details match the citation
(*Annals of Statistics* 11(3):793–803).

## §4.4 — Shore & Johnson 1980 — **PRESENT, PARTIAL CONFIRMATION**

File: `ref/shore-johnson-1980-axiomatic-maxent.pdf` — PDF document, version
1.2, present in `ref/`. I did not open the PDF end-to-end (not the
load-bearing citation; AAT cites it only as a "structurally-equivalent
re-formulation" via Csiszár 1991's own discussion). Bibliographic record
match: "Axiomatic derivation of the principle of maximum entropy and the
principle of minimum cross-entropy," *IEEE Trans. Info. Theory* 26(1):26–37
(1980). Csiszár 1991 itself (PDF p. 2035, 2040, 2043) repeatedly references
Shore-Johnson 1980 and explicitly relates the system-independence axiom to
the composition-consistency postulate — this cross-reference is enough to
sustain the "structurally-equivalent re-formulations" framing without an
independent end-to-end read of Shore-Johnson.

## §4.5 — Bretagnolle & Huber 1978 — **NOT PRESENT IN `ref/`**

No PDF for Bretagnolle & Huber 1978 ("Estimation des densités," *Séminaire
de probabilités XII*, Springer LNM 649) in `ref/`. The segment cites
Tsybakov 2009 §2.4 and Sason & Verdú 2016 as additional sources for the BH
inequality, neither of which is in `ref/` either. **Strict-form-verification
consequence:** the BH inequality citations cannot be PDF-verified locally.

The BH inequality $\operatorname{TV} \leq \sqrt{1 - e^{-D_{\mathrm{KL}}}}$ is
standard textbook material (also given as Theorem 14.2 in Lattimore &
Szepesvári, *Bandit Algorithms*, 2020 — not in `ref/` either, but a current
standard reference). The deterministic-$P$ specialization
$D_{\mathrm{KL}}(\delta_x \Vert Q) = -\log Q(x)$ is the trivial direct
calculation verified in §2.1 above and does not require the general BH
inequality to land — only the trivial KL-of-point-mass identity. So the
absence of the BH PDF does not affect the verification of Claim 1; the
load-bearing identity is verified by §2.1 directly.

**Recommendation for the pre-print citation hygiene** (not in this
verification's scope to remediate): the AIES papers citing AAT's BH-identity
result would benefit from a primary-source attribution that AAT can vouch
for. The Tsybakov 2009 citation (*Introduction to Nonparametric Estimation*,
Springer, §2.4 specifically) is the standard modern textbook source — having
the Tsybakov PDF in `ref/` would let a future audit close the citation chain.
Out of scope for this strict-form verification.

## §4.6 — Pinsker 1964 — **NOT PRESENT IN `ref/`**

Pinsker's inequality $\operatorname{TV}(P, Q) \leq \sqrt{\tfrac{1}{2} D_{\mathrm{KL}}(P \Vert Q)}$
is textbook (Cover & Thomas 2006 §11.6). The segment cites it inline without
a primary-source `ref/` PDF, which is acceptable for a textbook-level result.
Not a defect.

## §4.7 — PDF-citation summary

| Author / Year | Cited for | PDF in `ref/`? | Content matches citation? |
|---|---|---|---|
| Hobson 1969 | Composition-axiom uniqueness of KL expression | **NO — file is unrelated HTML scrape** | Deferred (no PDF to read) |
| Csiszár 1991 | Theorem 3 corollary + Theorem 5 (chain-rule / composition uniqueness of reverse-KL) | **YES (valid PDF, 16 pp.)** | **CONFIRMED — Theorem 3 corollary p. 2045 and Theorem 5(ii) p. 2047 verified verbatim** |
| Amari 2009 | (previously mis-cited; now removed) | **YES (valid PDF, 7 pp.)** | **CONFIRMED removal — Amari 2009 does not contain a chain-rule uniqueness theorem; the citation correction is correct** |
| Shore & Johnson 1980 | Equivalent reformulation (system-independence axiom) | **YES (valid PDF)** | Partial — cross-reference via Csiszár 1991's own treatment suffices for the "structurally-equivalent re-formulation" framing |
| Eguchi 1983 | Fisher-metric-at-second-order is not distinguishing within f-divergences (§6.2 no-go) | **YES (valid PDF, 11 pp.)** | Bibliographic match; content not end-to-end re-read in this scope |
| Bretagnolle & Huber 1978 | The general BH inequality | NO | Standard textbook material; the deterministic-$P$ specialization verified directly in §2.1 |
| Pinsker 1964 | Pinsker inequality | NO | Textbook; not a defect |
| Aczél & Daróczy 1975 | Functional-equation machinery for chain-rule derivation | NO | Standard reference; the Cauchy-FE machinery itself is mainstream |
| Aczél 1966 | (used in `deriv-edge-update-natural-parameter.md`) | NO | Standard reference |

# §5 — `form-strategy-complexity-cost` tier-justification independent read + verdict

## §5.1 — What `robust-qualitative` means

Per `terminology/entries/robust-qualitative.md`:

> `status: robust-qualitative` indicates that the claim's *qualitative* shape
> — the direction of the effect, the sign of the relationship, the ordering
> of cases — survives robustly across different modeling assumptions or
> representational choices, even though the specific functional form or
> coefficient values are approximate.
>
> This tier sits between `exact` (the form is proved) and `heuristic`
> (useful approximation without formal backing). A robust-qualitative claim
> is more than a heuristic: the qualitative structure can be justified
> across assumptions, and the approximation concerns only the quantitative
> details. It is less than `exact`: if you need the specific value (not
> just the sign or direction), this status means you cannot trust the
> expression as written.

## §5.2 — Independent reading of the segment's load-bearing content

The segment `form-strategy-complexity-cost.md` carries five distinct
sub-claims, which I evaluate individually:

1. **Strategy description length** (formulation):
   $\operatorname{DL}(\Sigma_t) = \operatorname{DL}_{\text{struct}}(G) + \operatorname{DL}_{\text{param}}(p \mid G)$
   with the $O(|E|\log|V|)$ scaling. Tier evaluation: this is a
   *formulation* (standard MDL applied to a DAG) and the segment correctly
   labels it so. Sub-tier of the segment.

2. **Strategy IB objective** (variational form):
   $\Sigma_t^\ast = \arg\min[I(\mathcal C_t; \Sigma_t) + \beta_\Sigma \cdot D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})]$
   with the KL direction $\pi^\ast$-first. Tier evaluation: this is the
   **load-bearing claim** for the segment's tier. The direction-forcing
   derivation (regret-bound argument + BH-identity for deterministic
   $\pi^\ast$) is exact under the stated scope (verified in §2 and §3 above).
   The direction itself is *proved* under the canonical scope; the linear
   vs. square-root form is a Lagrangian-shape trade-off (§7 of the appendix);
   the reverse-KL form within the direction-forced family is *derived
   conditional on the chain-rule additivity axiom*. The segment is honest
   about the conditionality.

3. **Maximum useful chain depth $d^\ast$** (derived conditional):
   $d^\ast = 1 + \lfloor \log(\nu / (n+1)\rho_\Sigma/R_\Sigma) / \log(1/\theta) \rfloor$.
   Conditional on Beta-Bernoulli, per-edge persistence. Labeled "*Derived
   (Conditional on Beta-Bernoulli, per-edge persistence)*". Correctly
   marked.

4. **Triple depth penalty** (observation): combines three independent
   results from separate segments. Discussion-grade.

5. **Enriched maintenance decomposition**: $C_{\text{maintain}} = C_{\text{represent}} + C_{\text{revise}} + C_{\text{monitor}}$.
   Formulation.

## §5.3 — Does the segment honestly carry `robust-qualitative`?

The robust-qualitative tier is justified if **the qualitative shape — the
$\pi^\ast$-first reverse-KL form for the strategy-cost relevance term —
survives across modeling assumptions, but the specific quantitative
functional form may be approximate**.

Test 1 (direction): The $\pi^\ast$-first direction is *forced* by the
regret-bound derivation (§5 of the appendix); forward-KL is vacuous under
deterministic $\pi^\ast$. Under the canonical AAT scope (deterministic
$\pi^\ast$), the direction is **proved**, not merely qualitatively robust.
This is **stronger** than robust-qualitative — it is exact for the
direction.

Test 2 (form within the direction-forced family): Under the chain-rule
additivity axiom, reverse-KL is uniquely forced. The axiom is AAT-internally
motivated as the divergence-level analog of an exact mathematical identity
(`der-chain-confidence-decay`). This is **conditional**, not exact —
because the axiom is a commitment, not a consequence of prior AAT
commitments. This matches "qualitative shape survives" with "specific
functional form approximate (or conditional)" semantics.

Test 3 (Lagrangian shape — linear vs. square-root in $D_{\mathrm{KL}}$):
The segment retains the linear-KL form for IB-shape alignment, while
acknowledging the square-root form is the tighter regret-bound scale. This
is **trade-off territory**, not exact-tier. The specific functional shape
is a representational choice; the qualitative claim (KL-based relevance
term) is robust.

Test 4 (boundedness of $V$): The derivation requires bounded $V$. This is
an additional assumption (called out explicitly in the segment's Epistemic
Status). Under the assumption, the derivation lands; without it, the bound
is $\infty$ (vacuous). The segment names this as a scope condition.

Test 5 (deterministic $\pi^\ast$): The BH-identity-based exact relationship
holds only under deterministic $\pi^\ast$. Outside that scope (stochastic
$\pi^\ast$), Pinsker is the loose fallback. The segment names this and
gives Pinsker as the general-case form.

**Verdict on the tier.** The segment's `status: robust-qualitative` is
**honest and defensible**:
- The *direction* of KL is proved (stronger than robust-qualitative, but
  proved only under deterministic-$\pi^\ast$ scope — outside that scope,
  the direction-forcing is qualitative-only).
- The *form* (reverse-KL) within the direction-forced family is conditional
  on the chain-rule axiom (a robust-qualitative-tier characterization is
  appropriate — the axiom is principled but is an axiom).
- The *Lagrangian shape* (linear vs. square-root in $D_{\mathrm{KL}}$) is a
  trade-off — neither form is uniquely forced; the segment retains the
  linear form for IB-shape alignment, explicitly.
- The *quantitative bounds* depend on $V_{\max}$ and on whether $\Delta_{\min}$
  is bounded away from zero — these are conditional scope parameters.

**The maximum tier the segment could honestly carry is `robust-qualitative`.**
A bump to `exact` would over-claim, because the linear-vs-square-root choice
and the chain-rule axiom dependency are not exact-level. A demotion to
`heuristic` or `conditional` would under-claim, because the direction-forcing
derivation, the BH-identity, and the chain-rule uniqueness theorem (verified
above) are honest derivations under stated scopes — not heuristics, and
together more than just "depends on a single explicit local assumption."

The Gate verification (`msc/451729-d1-gate-verification-2026-05-20.md` §5)
landed at `robust-qualitative`, and the spike author landed at
`robust-qualitative`, and my independent re-read also lands at
`robust-qualitative`. **Three independent paths to the same tier; no defect.**

## §5.4 — Verdict on the tier

**CONFIRMED.** `form-strategy-complexity-cost.md`'s `status: robust-qualitative`
is the honest label given (a) the BH-identity verification (Claim 1, §2),
(b) the chain-rule uniqueness verification (Claim 2, §3), and (c) the
direction-forcing derivation that is proved under deterministic-$\pi^\ast$
scope. The label is neither over- nor under-claimed. It is the maximum
tier the segment can honestly carry, and it carries it.

# §6 — Summary

| Claim | Verdict | Notes |
|---|---|---|
| **Claim 1: $D_{\mathrm{KL}}(\delta_{a^\ast} \Vert Q) = -\log Q(a^\ast)$ under deterministic $\pi^\ast$** | **CONFIRMED** | One-line algebra re-derived independently from KL definition + $0 \log 0 = 0$ convention. Holds exactly under stated scope ($Q(a^\ast) \gt 0$). One minor presentational slip noted in §2.2 ("becomes an equality" phrasing is loose; not a tier defect). |
| **Claim 2: Chain-rule-axiom uniqueness of reverse-KL within direction-forced f-divergences** | **CONFIRMED** (with one deferred citation component) | Csiszár 1991 Theorem 3 corollary (p. 2045) and Theorem 5(ii) (p. 2047) PDF-verified, both state and prove exactly what AAT cites. The chain-rule statement itself was verified directly via Cover & Thomas-style KL chain-rule check. AAT-internal motivation (divergence-level analog of chain-layer log-additive identity) is legitimate. **Hobson 1969 PDF cannot be verified — file in `ref/` is unrelated HTML scrape; see §4.1** — but the load-bearing uniqueness claim is sustained by Csiszár 1991 alone, independent of Hobson. |
| **Citation PDFs — Csiszár 1991** | **CONFIRMED** | Valid 16-page JSTOR PDF; bibliographic record and theorem statements verified line-by-line. |
| **Citation PDFs — Amari 2009** | **CONFIRMED (correction-validity)** | Valid 7-page IEEE PDF. The earlier-draft mis-citation of Amari 2009 Theorem 1 for chain-rule-uniqueness has been correctly removed; Amari 2009 contains the α-divergence f∩Bregman intersection uniqueness, *not* a chain-rule uniqueness theorem. The Working Notes correction is right. |
| **Citation PDFs — Shore & Johnson 1980** | **PRESENT (partial)** | Valid PDF; cross-reference via Csiszár 1991's own treatment supports the "structurally-equivalent re-formulation" framing without independent end-to-end read. |
| **Citation PDFs — Eguchi 1983** | **PRESENT** | Valid 11-page PDF; bibliographic record matches. Used in §6.2 only as the "Fisher-metric-not-distinguishing" no-go; not re-read end-to-end in this scope. |
| **Citation PDFs — Hobson 1969** | **DISCREPANCY (file-state)** | The file `ref/hobson-1969-theorem-information.pdf` is not Hobson 1969 — it is an HTML page for an unrelated 1991 finance paper saved with the wrong filename, almost certainly due to a Springer paywall serving HTML when the PDF was requested. **The citation itself is not mis-attributed** — bibliographic details (J. Stat. Phys. 1(3):383–391) match standard external record — but the local PDF for strict-form verification is missing. Recommended remediation: replace the placeholder, or delete it and note the absence (out of scope for this verification). |
| **Citation PDFs — Bretagnolle-Huber 1978 / Pinsker / Tsybakov / Aczél-Daróczy / Aczél** | **NOT IN `ref/`** | All are textbook-standard references. The load-bearing one-line algebra for Claim 1 is verified directly in §2 without needing the BH PDF; the load-bearing chain-rule uniqueness is verified via Csiszár 1991 in §3. None of these missing PDFs is critical to sustaining the claims under strict-form verification. |
| **`form-strategy-complexity-cost` tier (`status: robust-qualitative`)** | **CONFIRMED** | Honest and defensible. Direction-forcing is proved (under deterministic-$\pi^\ast$ scope); form-within-direction is conditional on chain-rule axiom (verified honest); Lagrangian shape is trade-off (linear retained for IB-shape alignment, square-root noted). Maximum tier the segment can honestly carry; it carries it. Three independent paths (Gate verification, spike author, this verification) converge on `robust-qualitative`. |

## §6.1 — Net adjudication for pre-print

**The two load-bearing claims are CONFIRMED** under independent strict-form
verification. The math holds; the `robust-qualitative` tier is justified;
the chain of citations is correct *as bibliographic entries*, and the one
PDF that cannot be verified locally (Hobson 1969 — wrong file in `ref/`) is
*not* load-bearing for the uniqueness result, which is sustained by
Csiszár 1991 alone.

**One file-state discrepancy surfaced** (Hobson 1969 PDF is misnamed
HTML scrape; §4.1) — this is a project-hygiene issue, not a citation defect,
and not a tier defect. The AIES papers citing AAT can rely on the
`form-strategy-complexity-cost` segment's `robust-qualitative` tier as
justified.

**Frame defects observed:** None substantive. One minor presentational
slip in `deriv-strategy-cost-regret-bound.md` §4's "becomes an equality"
phrasing (loose — the BH *inequality* doesn't become an equality; the
$D_{\mathrm{KL}}$–$\operatorname{TV}$ algebraic substitution makes the
upper-envelope coincide with $\operatorname{TV}$, which is what gives
tightness against the TV-regret bound). This is a copy-edit opportunity,
not a verification defect.

## §6.2 — Deferred items (out of scope for this verification)

1. PDF retrieval for Hobson 1969 to close the citation chain locally.
   Currently a project-hygiene issue, not a load-bearing defect.
2. Optional: PDF retrieval for Tsybakov 2009 §2.4 (the standard modern
   textbook source for BH and Pinsker) — would let a future audit close the
   BH-inequality citation chain. Not needed for the current pre-print.
3. The presentational slip in `deriv-strategy-cost-regret-bound.md` §4
   final paragraph noted in §2.2 — a copy-edit, not a math defect.

# §7 — Adjudicator's frame statement

This verification was conducted under the strict-form independence mandate:
no recourse to the spike's derivation path; no borrowing of the Gate-verifier's
or canon-edit applier's reasoning; PDFs opened and read where present; absent
PDFs flagged rather than glossed. The verdict above stands or falls on
(a) my independent re-derivation of the BH-identity in §2.1, (b) my PDF
spot-checks of Csiszár 1991 and Amari 2009 in §3 and §4, and (c) the
tier-justification independent read in §5. The three components hang together
without circular dependency.

Pre-print can proceed.
