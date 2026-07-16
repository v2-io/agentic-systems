# empirica/ — the registered simulation & empirical-artifact corpus

*Established 2026-07-16 (Joseph: simulations get a canonical home in current form, with vivarium as the eventual official empirical venue). The name follows the project's Latin register family (regula, practica, relata, tabularium) and passes the standalone-citability test; it is confirmable in a future naming cycle without structural change.*

## What this is, and the move that makes it canon

The ratified integration principle (INTEGRATION-CLEANUP-TODO §"corrected principle", point 5) requires that simulation knowledge land self-contained in segments and that canon never cite a local *working* path — the failure it guards against is a claim whose supporting artifact dies in `/tmp` (this happened; see the l1-bias record, CHANGELOG 2026-07-16). This directory resolves the tension the same way `LEXICON.md` and `NOTATION.md` do for vocabulary: **`empirica/` is a registry that travels with the Theory, so it is canon, and canon may cite it.** A reference of the form `empirica:<experiment-slug>` (optionally `@<run-date>`) is a sanctioned canonical reference, not an integration failure. At publication, experiment directories become the archival supplement (DOI'd, relata-registered) and the citation form survives unchanged.

## Structure — one directory per experiment

```
empirica/
  README.md            — this charter
  INDEX.md             — the registry: one row per experiment
  <experiment-slug>/   — slug-named, like segments
    MANIFEST.md        — the knowledge contract (canonization instrument)
    *.py …             — the artifacts, in whatever form they exist
    RUNS.md            — run log: date, parameters, seed, environment, output digest
```

**The MANIFEST is what canonizes an experiment.** One page: what it simulates and claims (with epistemic tier per FORMAT's vocabulary); parameters and regime; the consuming segments (`#slug` list — keep bidirectional: those segments cite `empirica:<slug>` back); provenance (originating spike or cycle); and vivarium-rerun status. This is deliberately the same shape as vivarium's in-vivia citation semantics (seed + generator versions + parameters + run record), so every manifest is a proto-in-vivia citation: when an experiment reruns in vivarium, its RUNS.md entry is superseded by a vivium reference and nothing else reorganizes.

**RUNS.md is what makes a claim traceable.** A canon claim tagged *[Empirical Claim (…)]* that cites `empirica:` must trace to a recorded run — date, exact parameters, explicit seed, environment note, output (or digest of it). Per the keyed-randomness recommendation in `#obs-software-epistemic-properties` (derived from `#deriv-mechanism-counterfactual-separation`): new runs record explicit keyed seeds — behavioral equivalence of script versions cannot certify rerun-equivalence; recorded draws can. A claim whose run was never recorded is restated or rerun, not trusted (the l1-bias lesson: transcribe run parameters, never paraphrase them).

## Lifecycle

1. **Enter:** an experiment enters with a MANIFEST, however thin-but-honest (claims it *intends* are marked as such — the promise-without-predicate rule applies in spirit: nothing is "confirmed" without a recorded run).
2. **Cited:** consuming segments reference `empirica:<slug>`; the INDEX row lists them.
3. **Rerun in vivarium** (the intended future for most): RUNS entry superseded by the in-vivia citation; INDEX vivarium-column updated; the python artifact is retained as provenance or retired to `.superseded/` per the manifest's judgment.
4. **Published:** the experiment directory (or its vivarium successor) becomes the external archival object; relata carries the DOI; segments' `empirica:` references resolve through the published supplement.

## Relation to spikes/

Simulation *spikes* (exploratory, one-question probes) still live and die under `spikes/` per spikes.sop. An experiment belongs here when a canon segment *leans on it* — the moment a sim's result appears in an Epistemic Status, the sim needs a registry entry. Moving a spike's sim here on promotion is the sim-flavored instance of math-lives-in-segments.
