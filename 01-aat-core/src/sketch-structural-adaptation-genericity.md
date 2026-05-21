---
slug: sketch-structural-adaptation-genericity
type: sketch
status: sketch
depends:
  - deriv-sector-condition
  - deriv-stochastic-non-exit
  - result-structural-adaptation-necessity
stage: draft
---

# Sketch: Does the Model-S Containment Dichotomy License Structural-Adaptation Genericity?

The Model-S segments claim Corollary A.1S.1 "sharpens the hand-off into `#result-structural-adaptation-necessity` — the structural-adaptation trigger is *generic, not exceptional*, for a sufficiently long-lived agent." This sketch isolates that hand-off as an open question: as stated it is plausibly a mild overclaim, and the honest move is to *derive the bridge* rather than soften the prose.

## The Open Question

*[Discussion]*

`#deriv-sector-condition` Corollary A.1S.1 establishes (exactly) that under additive stochastic forcing the persistence-region first-exit probability is $P(\tau_R \lt \infty) = 1$ — a long-lived agent leaves the sector-condition region $\mathcal B_R$ with certainty. The Model-S segments and `#deriv-stochastic-non-exit` then assert this "sharpens the hand-off" so that structural adaptation is *generic, not exceptional*.

But `#result-structural-adaptation-necessity` derives necessity from a **different trigger**: model-class inadequacy ($\mathcal F(\mathcal M) \lt 1 - \varepsilon$ — no model in the current class can represent reality). It does not reference Model-S, region-exit, or Corollary A.1S.1; its mechanism is fitness-driven, not noise-driven. And the corollary's own explicit instance (the OU benchmark) is **positively recurrent**: the process exits any bounded region a.s. *and returns* a.s. — exit-and-return, not escape.

So there is a gap between what Cor A.1S.1 proves and what the hand-off prose claims:

- **What the corollary licenses (honest narrow claim):** the *pathwise-forever parametric-containment guarantee* is structurally unavailable under stochastic forcing; a long-lived agent generically enters the regime where the parametric persistence guarantee is no longer *proven* (the out-of-region regime `#result-structural-adaptation-necessity` addresses).
- **What it does not license without further argument:** that *model-class* structural adaptation is generically *necessary*. Recurrent region-exit (exit-and-return) is not model-class inadequacy; a transient noise excursion beyond $\mathcal B_R$ that the (un-posited-but-possibly-still-inward) correction pulls back is not a structural-adaptation trigger in the `#result-structural-adaptation-necessity` sense.

## Proposed Direction (rigor pending)

*[Discussion]*

Per strengthen-before-soften, the preferred resolution is **derive the bridge**, not tighten the prose. Candidate conditions under which certain region-exit *would* imply structural-adaptation necessity, to be attempted:

1. **A2' genuinely fails outside $\mathcal B_R$** (not merely "not posited"): if the correction function provably ceases to point inward beyond $R$ for the agent's model class, then a.s. exit composes with non-recovery, and recurrent exit *does* force the structural regime. This connects to the sub-scope $\beta$ / model-class-capacity reading of $R$ in `#form-sector-condition`.
2. **Excursion statistics interact with $\mathcal F(\mathcal M)$:** if recurrent large excursions degrade *effective* model-class fitness (the model fitted within $\mathcal M$ becomes systematically wrong during excursions faster than it re-converges between them), the noise-driven and fitness-driven triggers couple, and genericity follows from the coupling rather than from exit alone.
3. **Timescale-separation argument:** if structural adaptation operates so much slower than parametric correction that the *fraction of time* spent out-of-region (positive under recurrence, however small) accumulates an unbounded structural-adaptation debt over an unbounded horizon.

Each is a derivation target; any one that closes turns the hand-off from asserted to proven and is a genuine strengthening (a new conditional result, not a softening). If all provably fail, the honest outcome is the no-go protocol applied to the hand-off claim (per `doc/audit-routing-instructions.md` §4) and the Model-S Discussion/Findings prose tightened to the narrow licensed claim above — but only *after* the strengthening attempt is exhausted and recorded.

## Epistemic Status

*Sketch.* Direction identified, formalization not attempted. This segment makes **no** claim that the bridge holds or fails; it records that the hand-off currently asserted in `#deriv-sector-condition` / `#deriv-stochastic-non-exit` Discussion/Findings is **plausibly a mild overclaim at the Discussion/Findings tier** (a Gate-2 class concern: a claim that *sounds* like it follows from Cor A.1S.1 but is not derived from it), and that the resolution path is to attempt the bridge derivation. The narrow licensed claim (pathwise-parametric-guarantee unavailability ⇒ generic entry into the out-of-region *regime*) is sound and uncontroversial; the disputed increment is "⇒ model-class structural adaptation is generically *necessary*." Ceiling: a closed bridge would be `derived (conditional)` on the named condition; a clean impossibility would be a no-go result. Until attempted, this stays `sketch`.

## Discussion

Why this matters enough to surface rather than leave as a soft ledger row: the genericity claim is load-bearing downstream — it is the form in which the Model-S no-go's consequence reaches the ELI / long-lived-agent persistence framing ("in any genuinely stochastic environment, structural adaptation is not an edge case"). If the bridge holds under a named condition, that is a sharp, citable strengthening of exactly the kind the framework's no-go signature tends to produce. If it does not, the framework's honesty requires the hand-off prose to state only the narrow licensed claim. Either way the question should be visible in the argument's structure, not invisible in a tracking file — which is the point of carrying it as an `exploratory` OUTLINE node.

## Working Notes

- Provenance: parent-generated 2026-05-16 during the audit-routing cycle, from a first-hand deep-read of `#result-structural-adaptation-necessity` against the Model-S segments (not a cluster audit finding). Originally filed as consolidated-ledger research-seed **S30**; Joseph adjudicated it up to a first-class `exploratory` OUTLINE node ("it will get its day in the light") rather than a soft ledger row. The ledger row is correspondingly demoted to a pointer here.
- Segment-vs-spike judgment (recorded so it is not re-litigated): this is recognized open *territory* between two landed results with **no attempt yet** — segment-shaped (visible structural node), not spike-shaped (a spike is the reasoning trail of an *attempt*). The spike is the eventual *work*: when this is picked up, a strengthening spike attempts directions 1–3; math lands back here (or in a new derivation/result segment), per `math-lives-in-segments`.
- Related: the `#disc-identifiability-floor` family — if the bridge is a no-go, the "no horizon-independent non-exit certificate" structural absence may itself compose with a structural-adaptation-necessity floor; worth checking whether this is an identifiability-floor-shaped instance.
