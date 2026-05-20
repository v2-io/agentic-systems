# Supplement: notes on the walk for Joseph

Notes accumulated during the segment-by-segment walk. Numbering and content quirks worth surfacing before you read the concatenated prose.

## Numbering map and gaps

**Order followed.** Top-level `01-aat-core/OUTLINE.md`, row-by-row. The appendix-back-pointer convention from `doc/de-novo-audit-instructions.md` §4.2 (jump to an appendix segment when first referenced for a load-bearing derivation, return to OUTLINE position) was applied inconsistently in the first pass: exercised once for `deriv-recursive-update` (which became `018`), then deferred. The second-pass fix uses **symlinks** so concatenation works in either order.

**Symlink scheme — two concatenation modes.**

Each Appendix-A derivation, Appendix-A discussion meta-segment, and Appendix-B worked example has a *symlink at its first-reference point in the main-chapter walk*. Naming: `NNN[b-z]-<slug>.md` where `NNN` is the main-chapter file number whose content first invokes the appendix segment, and the letter suffix orders multiple appendices that fall after the same main file. E.g. `025b-deriv-sector-condition.md` → `106-deriv-sector-condition.md`. Forty-four symlinks total.

Two concatenation modes (no content duplication in either):

- **Mode 1 — interleaved, truncated.** Concatenate all `.md` files in lexical order *up to and including the `105*` range*:
  ```
  ls *.md | sort | awk '{if ($0 < "106") print}' | xargs cat > walk-interleaved.md
  ```
  Reads main chapters with each appendix segment landing right after its first-reference doc. The symlinks dereference; the originals at `106+` are not read (truncation handles them).

- **Mode 2 — sequential, no symlinks.** Concatenate all real files in lexical order, skipping symlinks:
  ```
  find . -maxdepth 1 -type f -name "*.md" | sort | xargs cat > walk-sequential.md
  ```
  Reads main chapters first (001-105), then all appendix files (106-151) in OUTLINE order. Symlinks are skipped by `find -type f`.

Both modes produce 145 segment files. The interleaved mode tends to read better as a continuous prose walk (proofs sit next to the results they support); the sequential mode matches OUTLINE order more strictly and reads better if you want main-then-appendix structure.

**The one inline exception.** `018-deriv-recursive-update.md` is a *real file*, not a symlink — the appendix derivation was summarized inline in the first pass before the symlink scheme was established. It reads at position 018 in both modes. There is no separate file in the `106-146` range for this segment; the appendix-A walk skipped it. The asymmetry is minor (one appendix segment lands inline rather than via symlink) and noted here so the count works.

**Gaps in numbering (OUTLINE rows marked `--GAP--` / `missing`).**

| Gap # | OUTLINE row position | What was missing |
|-------|---------------------|------------------|
| 058 | Part II Ch.4 (Strategy Dynamics) intro | `--GAP--` (intro segment not yet authored) |
| 071 | Part II Ch.5 (Orient Cascade) intro | `--GAP--` |
| 079 | Part III Ch.2 (Composition Machinery) intro | `--GAP--` |
| 086 | Part III Ch.3 (Unity, Communication, Shared Intent) intro | `--GAP--` |
| 099 | Part III Ch.5 (Strategic Composition) intro | `--GAP--` |
| 134 | Appendix A `disc-strategic-self-coupling` | `missing` (referenced by `disc-adversarial-coupling-pressure` and others as one leg of the modularity-state-dynamics M4 pattern) |
| 135 | Appendix A `disc-modularity-state-dynamics` | `missing` (the M4 meta-segment itself; forward-referenced by the M1/M2/M3 meta-segments) |
| 152 | Appendix B `worked-example-cam` | `missing` (Miller 2022 Coevolving Automata Model worked example) |

The five missing chapter-intro segments are *substantively load-bearing*. The chapters where the intro exists (Part I Ch.2/3/4; Part II Ch.2/3; Part III Ch.4) have markedly richer scaffolding than the ones where it doesn't. Reading the concatenated prose you'll feel a "drop into the technical segments without bridging" at each of 058/071/079/086/099. If those intros land later, my summaries would integrate them naturally; for now I noted the absence here so you don't read the abruptness as a defect of the summary.

The two missing `disc-*` meta-segments (134/135) are part of the framework's M4 *modularity-state-dynamics* meta-pattern, which is currently carried forward via cross-references from M1/M2/M3 and the adversarial-coupling-pressure segment. When 134/135 land, the cross-references will fill in; the surrounding segments treat the absence as a forward-reference rather than a gap.

`worked-example-cam` (152) is the only missing Appendix B example. The other four worked examples (Kalman, bandit, strategy DAG, L1 augmented) cover the linear-Gaussian / RL-bandit / Part II strategy / Correlation Hierarchy cases; the missing CAM example would have been the framework's bridge to Miller's coevolving-automata work, which is currently only referenced rather than worked.

## UX / clarity flags worth surfacing

These are places where, reading the segments in OUTLINE order with no prior, I either had to recover meaning from a later segment or where I think a reader's first pass would lose the load-bearing content. They are *UX bugs* in the sense the user asked me to flag, not theoretical defects.

### High-impact

**1. `def-strategy-dimension` (#042) names the strategy-objective split but defers the strategy DAG to Ch.3.** Reading Part II Ch.1 in order, the reader meets *strategy* as an opaque slot for ~3 chapters before it acquires structure. The intervening segments (`def-value-object`, the Pearl hierarchy recap, `der-causal-hierarchy-requirement`, `der-loop-interventional-access`, the CIY admissibility regimes) all reference the strategy in a way that *would read better* if the reader had even a sketch of what `Σ_t` looks like structurally. **Suggestion:** the chapter intro for Ch.2 (which currently exists, `#causal-access-intro`) could carry a one-paragraph forward-pointer to the AND/OR DAG commitment. Or the `def-strategy-dimension` segment could carry a one-paragraph teaser of the DAG it's deferring. The current state has the reader carrying an undefined object through ~30k tokens of prose.

**2. The `--GAP--` chapter intros (058/071/079/086/099) make the affected chapters substantially harder to read.** Most painful at 058 (Strategy Dynamics) and 099 (Strategic Composition) — both are *load-bearing* chapters whose machinery I had to reconstruct from the segments themselves. The chapter-end implications segments help (they exist and are good), but they're at the *end*; a chapter intro is what tells the reader where they are going as they're reading. **Suggestion:** these five chapter intros are a high-leverage authoring target — they're the closest thing in the framework to where a fresh reader's path through the technical content gets lost.

**3. The recurring `bare-prose shorthand: the term "X" is sanctioned within this segment after the first compound-form introduction` convention is doing important UX work but the reader has to absorb it implicitly.** Where I noticed this most: `multi-agent routing structure` (in `scope-multi-agent`), `strategic grafting` (in `form-structural-change-as-parametric-limit`), several others. The convention is fine; an explicit one-line statement of it in `FORMAT.md` would let a reader know that compound terms are sanctioned-shorthand within the home segment rather than the global lexicon.

### Medium-impact

**4. The four-instance additive-coordinate-forcing meta-pattern (chain → divergence → update → metric) takes a reader several reads to see as a single object.** The four anchoring segments (`der-chain-confidence-decay`, `deriv-strategy-cost-regret-bound` §6.1, `deriv-edge-update-natural-parameter`, `der-gain-sector-bridge` Fisher cases via `scope-agent-identity`) are scattered across Parts I/II/III + Appendix A. The meta-segment `disc-additive-coordinate-forcing` exists and does this well, but it lives in Appendix A. **Suggestion:** the appendix discussion segment carries the catalog cleanly; a one-paragraph forward-pointer to the meta-pattern in (e.g.) `der-chain-confidence-decay`'s Discussion section would let readers see the anchor-of-three-downstream-layers framing on first encounter rather than waiting for the appendix.

**5. The identifiability-floor pattern's four formal instances (Bareinboim CHT for L0-detection; Cramér-Rao for L1' mixture under unobservable common cause; Liberzon common-Lyapunov-nonexistence for composite contraction; heteroscedastic-Gaussian for universal information-to-distance constant) take a similar number of reads to see as one pattern.** The meta-segment `disc-identifiability-floor` is well-written and does this work; the cross-references from the four home segments (`der-causal-insufficiency-detection`, `deriv-edge-credence-dynamics` Prop B.7, `deriv-critical-mass-composition`, `deriv-observation-ambiguity-bias-bound`) all point to the meta-segment. The cross-references seem adequate; this one's borderline-noticing-only.

**6. Two segments use the phrase "exact" in a way that could mislead.** `result-certificate-existence` is "exact (linearized/local)" — easy to miss the parenthetical and assume the result holds globally. `result-mismatch-decomposition` is "exact under fresh-noise (GA-1)" — the segment is explicit but the global assumption is named in NOTATION.md rather than in the segment itself. Both could carry a one-line explicit scope statement near the result so a reader can't misread the "exact" tier without seeing the scope.

### Low-impact

**7. The `dual-role` of teleological unity $U_O$ — both a (C-i) scope-route quantity and a downstream rate-distortion parameter — is honestly disclosed in `def-unity-dimensions`'s Discussion but I had to read it twice to be sure I had it right.** This is a *scope-honesty success* — the segment is explicit. But it's the kind of thing a reader might miss on a single pass.

**8. The Pearl-blanket vs Friston-blanket positioning in `der-directed-separation`'s Discussion is well-written but its load-bearing role for the framework's broader scope-honesty posture is buried in the segment's Discussion.** The implication that AAT's explicit Class-3 scope exit is *itself* an answer to the Bruineberg-et-al critique of the Friston-blanket reading is a meaningful methodological contribution; surfacing it in the chapter-end implications could lift it.

## What didn't trip me up

For symmetry: a few things that I expected to be confusing on first read turned out fine. The convention hierarchy (C1/C2/C3) and its monotonicity result is *crisp* in `def-value-object` and gets re-cited cleanly. The strategy-DAG's L0/L1/L1'/L2 Correlation Hierarchy is *thoroughly worked* in `def-strategy-dag` and the worked example `example-L1`. The signed-coupling structure (cooperative as negative term, adversarial as positive term, both in one inequality) is *load-bearing* and the framework keeps it visible throughout Part III Ch.4 and Ch.5.

## One stylistic observation, take or leave

The framework's signature posture — *naming an information-theoretic floor and the unique broadly-available escape via AAT machinery* — recurs as a methodological commitment across the identifiability-floor instances. It is one of the framework's most distinctive *postures*. The chapter-end implications segments name this posture explicitly each time; the home segments name it instance-by-instance; the meta-segment `disc-identifiability-floor` makes it explicit at the pattern level. Reading the concatenated prose, the posture is *visible* — which I think is a success, not a defect. But there might be one good place upfront (perhaps in the Volume introduction, or in a dedicated section of `CLAUDE.md`-equivalent prose) to name the posture as a *methodological commitment* of the framework. It would help a reader read each instance as "the framework doing what it commits to do" rather than as four independent moves that happen to look similar.

— end supplement —
