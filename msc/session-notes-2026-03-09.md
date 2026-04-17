# Session Notes: 2026-03-09 (Opus 4.6, 1M context)

## What happened

Full read of the entire corpus (TFT, TST, via-tft, AAD src/, all appendices, msc/, feedback). Then a theoretical spike on deriving purposeful agency from first principles, iterated through three versions with Gemini and Codex review at each stage, culminating in a graph uniqueness argument.

## What we produced

| File | What it is |
|------|-----------|
| `msc/opus-analysis-2026-03-09.md` | Initial reading analysis |
| `msc/spike-purposeful-agent-derivation.md` | v1: exploratory spike (preserved for archaeology) |
| `msc/spike-v2-purposeful-agent.md` | v2: first clean rewrite |
| `msc/spike-v3-purposeful-agent.md` | v3: definitive version for src/ porting |
| `msc/spike-graph-uniqueness.md` | Graph structure uniqueness argument |
| `msc/llm-causal-access-note.md` | Pearl reconciliation / LLM causal access |
| `PLANS.md` | Updated with governing objectives |

## The nuanced framing

### What's genuinely new (things that didn't exist before this session)

1. **P3 → Markov condition → DAG structure is forced.** This is the strongest result of the session. The argument has the same shape as Cox's theorem: an operational axiom (local revisability) forces a specific mathematical structure (directed graphical model). If it holds up to scrutiny, it resolves the "is the DAG a choice or a necessity?" question decisively in favor of necessity — at least for the graph structure (the parameterization remains a choice).

2. **Acyclicity is derived, not assumed.** Temporal ordering over a finite planning horizon forces acyclicity. This resolves a listed known fragility. Apparent iteration is a chain, not a cycle.

3. **Satisfaction gap / control regret split.** Two distinct purposeful mismatch signals serving different diagnostic roles. Without this, the orient cascade can't distinguish infeasible goals from bad strategies. This was genuinely unexpected and solves a real problem.

4. **G_t evaluable complexity bounded by M_t capacity.** You can't run a sophisticated strategy with a crude reality model. This creates the virtuous/vicious cycle at the purposeful level and explains why the orient cascade's ordering is structurally necessary.

5. **The feedback loop as Level 2 engine.** The explicit framing of model + loop = interventional access, stated as a formal bridge between Pearl's hierarchy and control theory, and applied to the LLM case.

### What's a better justification for existing architecture

Most of the v3 spike. The X_t = (M_t, G_t) lift, the O_t/Σ_t split, the orient cascade, directed separation — these all existed before. The spike provides better justification, clearer epistemic labels, and an honest map of which parts are derived vs. chosen. This is valuable (it transforms vague design intuitions into precisely labeled theory) but it's not the same as discovering something new.

### What we learned about the theory's nature

**AAD's main contribution is integration.** The individual pieces (Kalman-style gain, Pearl's hierarchy, Lyapunov stability, BDI-style agent architecture) are known. The synthesis — connecting code quality to U_o to η* to T to persistence — is what no single field provides. The theory should be presented as a unifying framework with specific novel results, not as a revolutionary new mathematics.

**The functional requirements are the theorems; the formalisms are the engineering.** The derivation chain produces requirements (you need causal structure, you need belief-goal separation, you need feasibility assessment, you need a graphical model). How those requirements are realized (AND/OR DAG vs influence diagram vs factor graph) is engineering — equivalent representations exist, and the choice between them is driven by computational properties and domain fit.

**Scope narrowings are divergence points, not weaknesses.** Each place where the theory narrows is a clearly marked trailhead for alternative theories. Someone who wants to study agents with goal-conditioned epistemic processing (violating directed separation) knows exactly where to diverge and what foundation they keep. The scope narrowings make the theory more honest AND more useful than a theory that claims generality it hasn't earned.

### The methodological discipline

The most transferable outcome of this session may be the labeling system itself:

- **Derived**: mathematical necessity — no alternative satisfies the axioms
- **Formulation**: representational choice — alternatives exist and are acknowledged
- **Scope narrowing**: explicit restriction with justification — the excluded cases are real and unexplored
- **Normative**: grounded in axioms but requiring a precondition (like outcome equivalence) that must be verified
- **Proposed schema**: mathematical shape identified, formal content pending

This prevents the most common failure mode in theoretical work:
presenting formulation choices as if they were derived necessities.
The spike went through several iterations of exactly this correction, each time catching a claim that was labeled too strongly.

## For the next session

1. The graph uniqueness argument (P3 → Markov) needs scrutiny — is the proof sketch actually tight? Compare with Lauritzen 1996, Koller & Friedman 2009 for the graphical models foundations.

2. The v3 spike is ready for porting to src/ segments. Start with the most settled claims (210: complete-agent-state, 215: objective- functional, 220: value-object).

3. The Gemini drafts (src/160, 170, 190) are still uncommitted and need review.

4. The AND/OR parsimony argument needs checking: is AND/OR really the unique O(k)-parameter complete basis for binary combination?

6. **Graph spike is a research appendix, not ready for src/.** Codex correctly flags: P3→Markov is a sketch (local revisability may be achievable by other sparse factorizations, not just parent-conditional Markov); the equivalence-class claims were overstated (causal semantics are DAG-specific, not shared across factor graphs etc.). The spike narrows the formulation-choice space (valuable) but does not yet justify promoting strategy-dag to a derived theorem. The acyclicity argument may be independently promotable.

5. The δ_sat disambiguation (infeasible goal vs insufficient capability) needs the cascade spelled out more precisely — when does the agent try expanding Π vs extending N_h vs improving M_t vs revising O_t?
