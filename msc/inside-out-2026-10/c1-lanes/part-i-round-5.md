*KR C.1 — "Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier" — item C1, with MAP D9; the front-door sites feed A. Top intent: "Complete 'in-place' refactor of ASF-- meta, all artifacts, and theory itself."*

# Part I, round 5: the round-4 check integrated, and the escape and ceiling restatements brought to their derivations

The landing is `b31a4f36` (pre-rebase), plus the commit carrying this file, the typed record `reviews/part-i-round-5-integration.md` (C1–C10, taken into vsect at `b31a4f36`) and the item closure. This file is for the mind that checks after me.

## How the sites were found this time

Round 4's check found two misses in my round-4 sweeps. A gain-buys-time sentence in `#deriv-stochastic-non-exit` escaped a sweep for the wording I expected, and the Appendices' Layer 0 escaped a sweep that never looked beyond the posture segment. Its lesson, to grep for the claim's shape rather than its wording, is right, and I followed it. The script below splits every canon segment, the four component fronts, the README partials and `NOTATION.md` into sentences. It flags three shapes:

- "Kalman" in the same sentence as stay, exit, $\kappa_R$, lifetime or "buys time";
- an escape, route, certificate or diagnostic called unique, only or sole, or anything "impossible without";
- a quantifier over update rules ("no", "whatever", "any" … update rule; update rule "does not" or "cannot").

I read every hit in a body, 75 in all. I also grepped separately for the lifetime-margin shape ("any lifetime", "logarithmic in lifetime", "lengthens the stay"). That shape can credit gain without naming the Kalman gain.

## What landed

**F1, the reading surfaces D9 did not list.** At `01-aat-core/OUTLINE.md` :332, the Appendices' Layer 0 now states each instance as its source derives it:
- the five routes for causal-insufficiency detection, with the loop's covariance test as the strong one needing only the theory's machinery;
- observing the latent or joint observation for the mixture;
- five escapes for composite contraction, matched tier giving the closed form;
- the dichotomy;
- the ceiling under fixed allocation and averaging update rules, with the rest open.

"Five cleanly-fitting instances span the framework" became "five of the catalogued instances show the range". :112 names the escapes. The README position partial now names the capabilities that escape the identifiability floors: interventional access, observation of a latent, or shared structure. Its "the unique escapes interventional machinery supplies" was false for Instance 2. Both READMEs regenerate from it.

Item handling: D9's item (`item:findings-brief-overclaim-on-public-surfaces-map`) was closed in round 4 with these sites open. I opened `item:escape-and-ceiling-over-claims-on-reading-surfac` (C.1, feeds A), which names that history, and closed it by `b31a4f36`.

**F2.** `#deriv-stochastic-non-exit` :56 now credits a stronger correction with the margin only at fixed disturbance. On a fixed noisy channel the reachable stay is bounded and peaks below the Kalman gain. The shape sweep found no other gain-time sentence that implies gain buys time up to $K$. Two hits are in `#deriv-observation-noise-placement`. :38 cites the exponent cap for feasibility. :56 says the attacker's stay shortens as its gain grows in the large-gain regime. Both are true as stated.

**F3–F6, `#disc-constructive-impossibility-posture`.**
- **F3.** Route (a) gives partial detection with no domain capability. Only (c)–(e) need domain capabilities.
- **F4.** Row C's apparatus cell says *unique broadly-available* certificate and names the other certificates.
- **F5.** Move 1 and row E scope the ceiling to fixed allocations and the averaging class. Row E gives the source's own statement of what lies outside.
- **F6.** Move 2's Model-S substitute is "distributional and finite-time, including the expected time to exit", not "instantaneous". The Epistemic Status counts A–C as inference, D–E as analogs and F–G as anchoring. Impact and Related Work count six audits, which is the number of audit IDs they list; the integrated spike's own "five distinct extraction targets" counts rows, not audits. The Working Notes' "Instance F" for the sector sub-scope is now "the spike's partial sixth instance, not the table's Instance F". The `depends:` rationale describes the eleven-entry list.

**F5's source, and two sites the check did not list.** `#deriv-evidence-allocation-ceiling` :15, :88, its Findings Brief ("No way of updating beliefs … beats simply trusting the most recent trial") and its Impact now scope the ceiling as its Epistemic Status and :74 already did. The shape sweep found the same over-claim in `#schema-strategy-persistence` :19 ("whatever the forgetting rate or update rule") and `#deriv-edge-credence-dynamics` :272 ("no update rule lifts the two-arm node"). Both are scoped now.

**F7.** `#deriv-critical-mass-composition` :180 counts five escapes. It calls (CM2) "the unique broadly-available R0-regime certificate under the matched-Tier escape (b)", the floor segment's own words, and says (c) and (d) also certify while (a) and (e) identify.

**F8 and kin.**
- **The move restated.** "Name the unique broadly-available escape" became "name the escapes" in `#disc-identifiability-floor` :36, `#disc-stability-certificate` :82, `#disc-additive-coordinate-forcing` :96, `#disc-anti-collapse` :16, `#impl-strategy-dynamics` :26 and :42, and `#disc-implementation-impossibility` :38.
- **`#disc-identifiability-floor`.** Its Brief, :143 and :175 called a cross-instance list of machinery "the unique broadly-available escape". The label is defined for Instance 1 and applied at Instance 3 to the certificate and the identifier, so these now say "the escapes", with the label used only in its defined sense.
- **`#impl-strategy-dynamics` :42 had more than the label wrong.** Its route list named the scope conditions (S1)–(S5) as routes, listed two routes the source does not have ("instrumental variation", "cross-episode covariance under structural breaks"), and said "every AAT agent within agency scope has" route (b). The source says route (b) needs routine joint exposure of siblings, which pure short-circuit execution suppresses. The list is now the source's (a)–(e).
- **`#impl-composition-machinery` :57.** It gave the label to composite interventional access alone. Now the identifier and the certificate are separate.
- **`#form-consolidation-dynamics` :110 and :157.** Consolidation was "the unique escape" of a sketch-level no-go, which nothing derives. Relaxing (N1) or (N2) escapes by the segment's own argument. The label "candidate Instance 3" was stale too: Instance 3 is now the composition floor. Both now say "candidate further instance" and "an escape".
- **`#disc-dynamic-regime-axis` :21.** It said regime identification is "impossible without composite-level coupling-topology observation". Now it says each of Instance 3's five escapes brings in information about the composite as a whole.

## Handed elsewhere, or deliberately left

- **`#der-loop-interventional-access` :111 is handed to Part II.** The Part II round-2 integrator holds the segment. Its claim that interventional action supplies "the unique broadly-available escape" across the floor instances is false for Instance 2, whose escapes are observational. The lead forwarded my proposed wording as an input to re-derive.
- **Left as true or as defined-sense uses:**
  - `#def-strategy-dag` :131, `#strategy-structure-intro` :22, `#der-causal-insufficiency-detection` :227 and `#disc-identifiability-floor` :57 spell out or point at the defined sense.
  - `#disc-identifiability-floor` :28 says observing $C$ is "the unique route from refuted-by-Cramér-Rao to globally-derived". That is true: the other repair, joint children, gives only a local sector condition.
  - `#disc-identifiability-floor` :163 and :181 and `#disc-stability-certificate` :59 say the only escape is new information or rank augmentation. That is a category statement, true by the Fisher argument.
  - `#deriv-edge-credence-dynamics` :703 says impossible "without additional information augmentation", which is generic and true.
- **Not mine to settle:**
  - `#disc-value-functional-grounding-floor` :28, "the only escapes are … precisely the two recognized terminal grounding routes", is the exhaustion claim `item:spikes-proposed-two-routes-exhausts-adversarial-spike-on-3366` owns.
  - `#impl-orient-cascade` :50, scaffolding as "the only route to the causally-disciplined zero", is a Part II claim of a different kind, and I did not check it.
  - `#hyp-solicitable-escape` :36 is that segment's own hypothesis.
  - `04-eli-core/src/scope-emergence-conditions.md` :28 and :65 are Volume 4.
- **`CURRENT-VOL1*.md`** is A.2's rebuild at the merged commit.
- **`#schema-strategy-persistence` cites `#deriv-evidence-allocation-ceiling` in its summary without depending on it**, so vsect ignored the ceiling in C10's read set. A change to the ceiling will not lapse checks on the schema's restatement. This is the class of `item:todo-lint-outline-eq-tag-topological-priority-646d` (I.4), and I left it to that item rather than widen the round.

## The influx

D9 is the source for F1, F4 and F8. F8's list came from the round-4 check, and I widened it with the shape sweep. The F5 extension sites, `#schema-strategy-persistence` and `#deriv-edge-credence-dynamics`, were raised by no source I know of. The exhaustion item named above is the spike-proposal index's (`spikes/PROPOSED.md` :33).

## What a checker who did not write this should verify

1. Run your own shape sweep, not mine. A shape I didn't think of is the likeliest miss. Two candidates: "the escape" in the singular for an instance with several, and "required" or "necessary" said of one of several escapes.
2. Read the new `OUTLINE.md` :332 against the posture table and each instance's source.
3. Read `#impl-strategy-dynamics` :42 against `#der-causal-insufficiency-detection`'s route table and its :237.
4. Check whether `#disc-dynamic-regime-axis` :21's list of what the escapes bring in matches Instance 3's (a)–(e).
5. Confirm that the evidence-allocation scoping now matches EA.1's class at every site the sweep found, and look for paraphrases it missed.

## Script

`python3 -I r5-shape-sweep.py <asf root>`. It prints a shape, a location, body or Working Notes, and the sentence.

```python
import re, sys, glob, os
root = sys.argv[1]
files = sorted(glob.glob(os.path.join(root, '0[1-4]-*/src/*.md')) + glob.glob(os.path.join(root, '0[1-4]-*/*.md'))
               + glob.glob(os.path.join(root, 'doc/readme/src/*.md')) + [os.path.join(root, 'NOTATION.md')])
shapes = {
    'gain-time': (re.compile(r'kalman', re.I), re.compile(r'\bstay|exit|kappa_R|lifetime|time in the region|as late as|buys? (expected )?time', re.I)),
    'only-escape': (re.compile(r'(unique|only|sole)\s+(broadly[- ]available\s+)?(escape|route|way out|remedy|certificate|supplier|diagnostic|identifier)|impossible without|only route out|the only route', re.I), None),
    'update-rule': (re.compile(r'(no|whatever|any|every)( [a-z,-]+){0,4} update rule|update (rule|mechanism) (cannot|does not|doesn.t)', re.I), None),
}
for f in files:
    lines = open(f, encoding='utf-8').read().split('\n')
    wn = next((i for i, l in enumerate(lines) if l.startswith('## Working Notes')), None)
    for i, line in enumerate(lines):
        for sent in re.split(r'(?<=[.;])\s+', line):
            for name, (a, b) in shapes.items():
                if a.search(sent) and (b is None or b.search(sent)):
                    tag = 'WN' if (wn is not None and i >= wn) else 'body'
                    print(f"{name}\t{os.path.relpath(f, root)}:{i+1}\t{tag}\t{sent[:260]}")
```
