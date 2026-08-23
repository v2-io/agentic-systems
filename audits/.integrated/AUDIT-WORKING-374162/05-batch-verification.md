# Batch 5 Verification — Tempo / Sector-Condition / Appendix-A Lyapunov

Checked all 20 answers against the six ground-truth segments (`def-adaptive-tempo`,
`hyp-mismatch-dynamics`, `persistence-and-limits-intro`, `der-deliberation-cost`,
`form-sector-condition`, `deriv-sector-condition`). This is the strongest batch so
far on raw fidelity — every formula, every quantifier in Lemma A.1N and Corollary
A.1S.1, and the sub-scope α/β partition are reproduced correctly, including the
subtle "necessary for the *uniform class-level* guarantee" vs. "agent-level iff
only under radial tightness" distinction the brief specifically worried about.
Direct computation confirms Prop A.1S's steady state ($\mathbb E[V]_{ss}=n\sigma_w^2/4\alpha
\Rightarrow \mathbb E[\lVert\delta\rVert^2]_{ss}=n\sigma_w^2/2\alpha$), Lemma A.1N's escape
inequality, and Prop A.2's $\Delta\rho^\ast=\alpha R-\rho$ algebra. Two findings below,
both instances of the two recurring patterns your predecessors named.

## Finding 1 — A b05-1.2: untagged WN-sourced clauses inside a body-grounded answer

The answer states, as the "practical consequence" of the $1/\mathcal T$ vs.
$1/\sqrt{\mathcal T}$ scaling laws: *"against drift, tempo investment pays linearly
(read the changelog, track the maneuver); against noise ... attack $\sigma_w$ at
its source (fix the flaky architecture, better sensors)."*

The scaling laws themselves are body text (`hyp-mismatch-dynamics` Formal
Expression + Discussion). But "read the changelog," "track the maneuver," and
"fix the flaky architecture, better sensors" are not in the body Discussion —
they're lifted near-verbatim from the segment's `## Working Notes` §"Incidental
audit gold," specifically the Claude/AUDIT-WORKING-829314 TST gloss: *"if a
library API drifts across versions, read the changelog and update — tempo works
linearly; if a system is plagued by ... noise ... you must attack $\sigma_w$
directly (fix the architecture)."* That's an auditor's candidate pedagogical
example, explicitly staged in WN as "orthogonal ... material, kept separate from
certified theory-fix findings" — not integrated body content. The answer presents
it with the same evidentiary weight as the derived scaling laws, with no
WN-provenance flag. Same pattern as prior batches: WN-sourced illustrative
material grafted onto a body-grounded answer untagged. (Compare A b05-3.2 in
this same batch, which does correctly self-flag its org-dashboard casting as
"WN-flavored" — so the discipline is present in the answer set, just not applied
here.)

## Finding 2 — A b05-3.5: a confidently-stated mechanism detail that isn't in the read segments

Question b05-3.5 asks the strengthening-attempt's failure mode. The answer
says: *"Structural failure: the compensated supermartingale candidate is
**sign-indefinite inside the basin** / the additive-noise generator has no
bounded non-constant harmonic function (recurrence — Khasminskii); no such
certificate can exist."*

The second clause ("no bounded non-constant harmonic function," Khasminskii
recurrence) is directly grounded — `deriv-sector-condition`'s Working Notes say
exactly this: *"no nonnegative supermartingale dominates $V$; additive-noise
generator has no bounded non-constant harmonic function; recurrent OU exits
a.s."* The first clause — "sign-indefinite inside the basin" — is not stated
anywhere in the six segments. It reads as a plausible technical gloss on "no
nonnegative supermartingale dominates $V$" (a sign-indefinite candidate is one
natural way such domination could fail), but the segment doesn't say this; it
just asserts the negative existence result and points the actual demonstration
at `#deriv-stochastic-non-exit`, which is out of scope for this batch and which
I have not read. This is exactly the "confident answer to an operational-detail
question the segments pose but don't derive" pattern — the answer should have
marked this clause as inference/unverified-against-this-segment-set rather than
stating it flush with the Khasminskii fact it sits next to.

Everything else in A b05-3.5 — the false claim's identity (conflating the
fixed-time second-moment tail with the ever-exit probability), the Doob/Ville
route as the attempted strengthening, the "restate as fixed-time" softening the
auditors (742613-SUPPLEMENT §2, 613842-F2) originally recommended, and the
"the no-go is the result" epistemology — is precisely and completely grounded
in the WN provenance record.

## Everything else checked clean

Spot-checked in particular because the brief called them out as
high-risk: Lemma A.1N's necessity quantifiers (b05-2.4 — "necessary and
sufficient for the *uniform* containment guarantee" attributed to the whole
class, with the extremal $F=\alpha\delta$ correctly used only as the *witness*
for that necessity claim, not conflated with a fixed-agent claim); Corollary
A.1S.1's dichotomy and its $\alpha$-invariance (b05-2.3, b05-3.1); the
Model-D/Model-S scaling exponents ($1/\alpha$ vs. $1/\sqrt\alpha$, and the
$b=2$/$b=3/2$ adversarial transfer mentioned in `hyp-mismatch-dynamics`); the
sub-scope $\alpha$/$\beta$ partition and its five/seven named classes
(b05-2.8); the deliberation-cost FOC and its $(1-\Delta\eta^\ast)$ correction
factor (b05-2.6); and the rule-based structural-Lipschitz-floor counterexample
$F(\delta)=\alpha\delta+\operatorname{sign}(\delta)$ (b05-3.3). All reproduce the
source with correct scope qualifiers.

## Beyond the quiz

Nothing new to flag in the theory itself beyond what the segments' own Working
Notes already surface as open (e.g. `deriv-sector-condition`'s own flagged
follow-up on generalizing the Model-S Itô term from isotropic $n\sigma_w^2$ to
$\operatorname{tr}(\Sigma)$ for anisotropic noise — already recorded, not new).

Happy to keep going — send batch 6 or any follow-up whenever.
