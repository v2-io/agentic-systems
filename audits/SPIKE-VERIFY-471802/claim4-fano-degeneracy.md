# Claim 4 — Fano degeneracy: the neutral-drift Fano anchor degenerates to vacuous at I=0; Kalman-Ho is the exact-population floor, Fano only the finite-sample refinement

## What the spike claims (§4 "The Fano arm")

> Fano gives a lower bound on prediction-error probability *given* a bound
> on the channel mutual information $I(A;\mathrm{obs})$. In the
> similarity-orbit construction, $I(A;\mathrm{obs})=0$ *exactly* (the
> observation law is identical, not merely close), so Fano degenerates to
> "error probability $\ge$ prior" — true but vacuous, strictly weaker than
> the exact Kalman-Ho "indistinguishable, full stop." Fano is the right
> tool for the approximate/finite-sample version ($I>0$ small); wrong for
> the exact population no-go. A demonstrated no-go on the proposed Fano
> anchoring.

## Canon / sibling checked first-hand

- **Neutral-drift spike** proposes Fano as the candidate fourth-instance
  anchor: line 110 ("The natural formal anchor is Fano's inequality at the
  observer-side prediction task: for observers whose $H_b^{A\mid B}(t,\tau)
  \ge H_{\text{threshold}}$, there exists a lower bound on prediction-error
  probability"); line 317 lists CHT as primary, Cramér-Rao alt; line 345
  explicitly says Kalman-Ho "is another and arguably sharper for the
  linear-Gaussian case." So the neutral-drift spike *itself already
  suspected Kalman-Ho was sharper than Fano* — the verify-spike is
  sharpening a doubt the prior artifact raised, not overturning a settled
  anchor.
- **`#der-agent-opacity`** (`status: conditional`) Working Note line 156:
  "Candidate fourth-instance formalization … the most natural external-
  theorem anchor is Fano's inequality (relating $H_b$ to error-probability
  lower bounds) applied to the observer-side prediction task. **Open; not
  pursued here.**" So canon never committed to Fano; it is flagged
  candidate/open. Confirmed first-hand.

## Independent re-derivation

**Fano's inequality (standard form).** For estimating $X$ from $Y$ with
$\hat X=g(Y)$ over an alphabet of size $|\mathcal X|$:
$$P(\hat X\ne X)\ \ge\ \frac{H(X\mid Y)-1}{\log|\mathcal X|}
 \quad\Longleftrightarrow\quad
 P_e\ \ge\ 1-\frac{I(X;Y)+1}{H(X)}\ \ (\text{equivalent rearrangement}).$$
The binding content is via $I(X;Y)$: low mutual information between the
quantity of interest ($X$ = the architectural variable $A$) and the
observation $Y$ forces high error probability.

**The construction's $I$ value.** By Claim 1 (verified, with the scoping
repair: identical at the innovation/output observable), the on-policy
observation law is **literally identical** for $A$ and $A'$:
$P_{\mathrm{obs}}(\cdot\mid A)=P_{\mathrm{obs}}(\cdot\mid A')$ as measures.
Mutual information between the architectural index $A\in\{A,A'\}$ (or, more
generally, the orbit coordinate) and the observation is
$$I(A;\mathrm{obs})=\mathbb E_A\big[D_{\mathrm{KL}}(P_{\mathrm{obs}}(\cdot
\mid A)\,\|\,P_{\mathrm{obs}})\big]=0,$$
**exactly zero**, because every conditional equals the marginal (all
conditionals are the same measure). Not "small" — identically zero. This is
a direct, forced consequence of Claim 1's law-identity. **Confirmed.**

**Fano at $I=0$.** Plug $I=0$: $P_e\ge 1-\frac{0+1}{H(A)}=1-\frac{1}{H(A)}$,
i.e. (for a binary architectural choice with uniform prior, $H(A)=1$ bit)
$P_e\ge 0$ — **the trivial/vacuous bound** (or, in the $H(X\mid Y)$ form:
$H(A\mid\mathrm{obs})=H(A)$ since obs is independent of $A$, giving
$P_e\ge\frac{H(A)-1}{\log|\mathcal X|}$ which for binary uniform is
$P_e\ge0$). Fano returns "$P_e\ge$ chance" — **true but vacuous**: it says
you can do no better than the prior, which is *correct* but *strictly
weaker* than the exact statement "the two are the **same measure**, so
**no** estimator beats the prior and the floor is an exact identity, not an
inequality." **Confirmed: at $I=0$ Fano degenerates to vacuity; the
Kalman-Ho law-identity is strictly sharper (an exact equality vs. a slack
inequality).**

**Where Fano *is* the right tool.** When two architectures are *close but
not similarity-equal* — innovation spectra differ slightly, $I>0$ small —
the population law-identity argument no longer applies (the laws differ),
and the live question becomes *finite-sample*: how many samples to
distinguish two near-but-not-equal laws. There Fano (or Le Cam / Assouad)
with $I>0$ gives a genuine non-vacuous sample-complexity lower bound. So
Fano's correct role is the **finite-sample / approximate refinement**, not
the exact-population floor. **Confirmed; this is the correct division of
labor and it is a genuine *demonstrated* no-go on the proposed Fano
anchoring (the $I=0$ degeneration is exhibited, not asserted) — consistent
with the no-go-is-present-truth discipline.**

## One precision note (not a defect)

The argument's force depends on the construction being the **exact**
similarity orbit (so $I=0$ identically). The spike is careful that the
*exact* claim is sub-scope-bounded (linear-Gaussian; general case is
robust-qualitative via CHT-at-agent-as-SCM). In the general (non-Gaussian)
sub-scope, two architectures matched only at $(\alpha,R)$ but not exactly
similarity-related may have $I>0$ — and *there* Fano is live again. So the
clean statement is: **within the exact sub-scope the construction is the
$GL(n)$ orbit ⇒ $I=0$ ⇒ Fano vacuous, Kalman-Ho exact; outside, $I$ may be
$>0$ and Fano (finite-sample) is the right refinement.** The spike says
exactly this ("Fano is the right tool for the approximate/finite-sample
version"). No overclaim. The only thing I would add for a landing: state
that $I=0$ is *specific to the exact-orbit (sub-scope) construction*; the
general-scope CHT-anchored statement is not an $I=0$ statement and Fano is
not vacuous there. The spike's §8 residual-uncertainty note (3) already
flags the finite-sample Fano refinement as honestly-open — consistent.

## Verdict on Claim 4

**Confirmed, exact.** The Fano anchor proposed by the neutral-drift spike
genuinely degenerates to the vacuous bound at $I=0$, and the
similarity-orbit construction has $I=0$ *exactly* (forced from Claim 1's
law-identity). Kalman-Ho (an exact measure-identity) is strictly sharper
than Fano (a slack inequality that goes vacuous here). Fano's correct home
is the finite-sample / close-but-not-equal refinement, which the spike
correctly leaves open rather than over-claiming. This is a properly
*demonstrated* no-go on the proposed anchoring, not an assertion. Agrees
with canon, which never committed to Fano (`#der-agent-opacity` line 156
flags it "Open; not pursued here") and with the neutral-drift spike's own
suspicion (line 345) that Kalman-Ho is sharper.

Tier: **exact** (the $I=0$ degeneration is a forced one-line consequence of
Claim 1's law-identity; the finite-sample-refinement role is correctly
scoped and left open).

Loci opened: neutral-drift spike lines 110, 317, 345; `#der-agent-opacity`
Working Note line 156 (`status: conditional`, Fano flagged open); spike §4
Fano arm + §8 residual (3).
