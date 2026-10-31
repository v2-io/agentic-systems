# MANIFEST: software-file-lifetimes

*KR E.3 ("One of Volume 2's cheap falsifiers is run on a real codebase history"), under objective E ("One quantity is measured on an agent the theory did not construct"). Entered 2026-10-30.*

**What it measures.** How long source files live in the mainline histories of real git repositories, from the commit that adds a file to the commit that deletes it, with renames followed and files present at HEAD right-censored. The quantity is the local survival exponent $a(t_0) = -\log_2 [Q(2t_0)/Q(t_0)]$, where $Q$ is the Kaplan–Meier survival of a file as a function of its age. It is measured in two clocks: calendar days, and mainline commits elapsed. A secondary measure bounds the probability that a file which has received $n_{\text{past}} \ge 5$ changes receives $n_{\text{past}}$ more.

**What it tests.** `#der-change-expectation-baseline`'s prediction about software. The prediction is $a = 1$: a component's median remaining life equals its age, at every age (the scale-ignorance form) or at large age (the hazard-mixture form). Under the hazard-mixture form, $a$ is the exponent that sets the baseline's multiplier, $2^{1/a}-1$. The design, the decision rules and the agent's prior expectation were committed before any lifetime was extracted, in `msc/inside-out-2026-10/e3-measurement/prereg.md` (`54a0bf5e`).

**Population, and its limit.** Source files, as components of long-lived, maintained, many-author projects (ten, the primary set) and of four young projects (descriptive). This instantiates the claim on components, which is the use the segment's Discussion makes of the baseline. It does not test the claim about whole systems, which needs a corpus of repositories with observed ends.

**Claims.** See `RUNS.md` for the run and `msc/inside-out-2026-10/e3-measurement/account.md` for the reading. The claims, with their tiers, are stated in the consuming segment.

**Consumers.** `#der-change-expectation-baseline` (Epistemic Status).

**Artifacts.** `lifetimes.py`: `dump` writes the mainline log, `run` analyses one repository, `summarize` applies the pre-registered decision rules, and `explore` is the exploratory count analysis, which was not pre-registered. The git dumps are not committed: they are regenerated from the HEAD shas in `RUNS.md`, and their digests are recorded there.

**Vivarium.** Not applicable: these are observed histories, not simulated ones.

**Provenance.** The falsifier is (a) of `item:tst-cheap-falsifiers-and-measurement-design`, from the owner review (`msc/inside-out-2026-10/owner-review/explorers/part-iii-and-vols-2-4.md` §3.3, item 3).
