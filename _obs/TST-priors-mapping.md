# TST Prior Work and Source Material

*Cut from 02-tst-core/OUTLINE.md on 2026-05-11. Inventory of the substantial prior research corpus at ~/src/_core/tst/ (960 analyses, Obsidian vault, empirical tools), what has been absorbed into 02-tst-core, and what remains.*


*TST has a substantial prior research corpus at `~/src/_core/tst/` (960 analyses, Obsidian vault, empirical tools). Most of this content has been absorbed. Source material lives in `src/old-tst-*` files, empirical tools in `empirical-discontinuity/`, simulations in `simulations/`, and literature review in `lit-review/`.*

### Absorbed into `src/old-tst-*`

**Earlier TST formalization** (same claims, SE-literature derivation path):
- `old-tst-software-first-principles` — The 13 original "First Principles" (FP-001–FP-013) with full discussion
- `old-tst-t01` through `old-tst-t15` — Earlier theorem statements (T-01–T-15)
- `old-tst-d01` through `old-tst-d08` — Earlier definition statements (D-01–D-08)
- `old-tst-appendix-a-version-mapping` — Mapping between FP-* and T-* numbering

**Synthesis and meta-analysis**:
- `old-tst-960-analysis-synthesis` — Synthesis of 960 SE literature analyses: validated discoveries, mathematical frameworks, speculative hypotheses
- `old-tst-comprehensive-synthesis` — Full mathematical theory of software evolution
- `old-tst-synthesis-theoretical-foundations` — Complete definitions and formal theorem statements
- `old-tst-synthesis-executive-summary` — Synthesis across 7 research domains with empirical validation
- `old-tst-meta-analysis-topology` — Topological analysis of cross-references
- `old-tst-meta-analysis-priority-rankings` — Priority-ranked findings
- `old-tst-research-findings-top-100` — Top 100 findings from the analysis corpus
- `old-tst-exemplar-analyses` — Collection of highest-quality individual analyses
- `old-tst-general-discussion` — General discussion from the theory section

**Mathematical grounding**:
- `old-tst-lindy-foundations` + `old-tst-lindy-math-foundations` — Bayesian derivation of Lindy via Jeffreys prior, maximum entropy, hazard rates → #der-change-expectation-baseline
- `old-tst-ai-specification-limit` — As implementation time → 0, specification quality becomes sole determinant → #obs-software-epistemic-properties, #scope-developer-agent
- `old-tst-proximity-coherence-for-ai` — Proximity/coherence/coupling analysis specific to AI agents
- Prior art for #result-specification-bound (Austin, Putnam, Shannon) is in `lit-review/` — see `specification-bound-prior-art.md`, `formal-bounds-on-implementation-speed.md`, `putnam-vs-tst-bounds.md`

**TFT bridge work** (maps TFT/AAD concepts to the software domain):
- `old-tst-via-tft-readme` — Why software is uniquely suited as AAD testbed (6 epistemic properties)
- `old-tst-via-tft-mapping` — Detailed TFT↔software domain mapping (~8,500 words)
- `old-tst-via-tft-causal-extensions` — Causal DAGs in software, Level 2/3 reasoning, counterfactual via git
- `old-tst-via-tft-reformulated-sketch` — S-00 through S-14 structured outline
- `old-tst-via-tft-simulation-proposals` — 6 concrete simulation proposals ranked by expected value

### Absorbed into directories

- **`empirical-discontinuity/`** — Git-based empirical validation toolkit for #hyp-exponential-cognitive-load. Validates $T = T_{\text{base}} \times (1+\alpha)^d$ with $\alpha \approx 0.118$ for normal development (d ≤ 25). Includes analysis scripts, methodology, findings, and visualization.
- **`simulations/`** — Stochastic Lindy Effect simulations: corrected model, Gaussian start, math verification, regime transitions, three-regime comparison, stochastic breakout. Validates survival distributions for #der-change-expectation-baseline.
- **`lit-review/`** — 29+ files: literature review across 7 research domains (optimal control, economic models, spectral graph theory, species-specific comprehension, stochastic processes, hybrid systems), Undermind paper reviews (10 papers), prior art for T-01, highest-cited SE works, research goals.

### Not yet absorbed (at `~/src/_core/tst/`)

- **`vault/03-library/analyses/`** — 965 structured analyses from 5 books (Pragmatic Programmer, Release It!, Programming Elixir, Designing Elixir Systems, Metaprogramming Elixir), each mapped to TST principles with mathematical formalization. These are concrete examples grounding principles in practice.
