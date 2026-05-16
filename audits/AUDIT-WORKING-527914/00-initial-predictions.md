# Initial Predictions

Agent id: `codex-r2b`

Cold-start note: I read the materials the Round 2 prompt directed or allowed: `README.md`, `CLAUDE.md`, `OUTLINE.md`, component outlines, `LEXICON.md`, `NOTATION.md`, `FORMAT.md`, `PRACTICA.md`, the three instruction docs, the launch prompt, and my own card/tracker. `PRACTICA.md` contains process-level history about the prior R2 launch failure modes and approximate first-cohort coverage, but did not expose candidate-specific vote rankings or other voters' target positions. I have not opened excluded `msc/naming/` vote, aggregate, other-card, other-tracker, or archive artifacts.

## Topology As I Understand It

The framework's load-bearing spine begins in AAD Section I: agent-environment boundary, observation/action channels, chronica, causal structure, compressed model state, recursive update, mismatch, gain, adaptive tempo, sector condition, persistence, and structural adaptation. This is the exact-ish core where names should be stable, reusable, and not whimsical. Core terms such as `chronica`, `mismatch`, `update gain`, `adaptive tempo`, `sector condition`, `persistence condition`, and `adaptive reserve` are likely high-cost to churn because the rest of the framework compounds on them.

Section II adds actuation: complete agent state, goal state, objective/strategy split, directed separation, strategy DAGs, satisfaction gap, control regret, strategic calibration, strategic tempo, strategy persistence, and the orient cascade. I expect many naming targets here because the theory is doing ontology work: it has to separate model from goal from strategy, diagnostic impossibility from architectural scope, and modular from coupled agents. Names that hide scope restrictions will be dangerous here.

Section III moves into composition and adversarial dynamics: multi-agent scope, composite-agent criteria, closure defect, unity dimensions, shared intent, communication gain, team persistence, adversarial tempo, interaction-channel classifications, opacity, per-dimension persistence. I expect this to be semantically dense and less settled than Sections I-II. It probably generates many candidate names where the issue is not "which phrase is prettiest" but whether the target itself has been framed at the right abstraction level.

The appendices are not peripheral. They seem to hold the derivation machinery that gives the main sections their status: sector derivations, discrete-time bridge, graph uniqueness, strategic dynamics, edge-update coordinates, adaptive gain, identifiability floors, separability, additive coordinate forcing, contraction template, Fisher-whitened update, bias bound. I predict high naming value in appendices because appendix terms often become the prose handles for theorem-shaped moves.

TST is AAD grounded in software. Its names should often be plainer and practitioner-facing because software is the calibration laboratory and onboarding surface. I expect terms like `calibration laboratory`, `committed chronica`, `comprehension time`, `implementation time`, `change distance`, and `code quality as observation infrastructure` to matter because they translate AAD's abstract machinery into a domain where readers can inspect the referent.

Logogenic agents are where directed separation fails and the coupled formulation becomes primary. I predict the naming problem shifts from derivation labels to architectural honesty: names need to prevent readers from smuggling Class 1 modular intuitions into LLM-like Class 2 agents. Terms around context turnover, coupled update dynamics, post-hoc diagnostics, external memory, ambiguity modulation, and M-preservation are likely high leverage.

Logozoetic agents are future-work / existential vocabulary. I expect naming pressure here to be aesthetic and ethical: terms must not over-formalize what is only conceptually grounded, but they also need enough dignity and precision to avoid "sentience" / "conscious AI" collisions. `moral continuity` is likely a stable boundary name unless the segment reveals it overclaims.

## Predictions By Component

AAD Section I will probably define the formal objects cleanly, but I expect some name candidates to split on whether a term should be the mathematically standard name or an AAD-native prose handle. Examples I will watch for: whether `chronica` should remain the canonical name for complete interaction history; whether `causal structure` is too generic for the foundational postulate; whether `adaptive tempo` and `mismatch injection rate` carry enough intuition without becoming metaphors.

AAD Section II will probably reveal the strongest existing names: `satisfaction gap`, `control regret`, `directed separation`, and `orient cascade`. I predict I will keep several of these if the segments make them as load-bearing as the README suggests. I also predict some class/tier names and sub-scope symbols will need aliases, because pure numbering or Greek/subscript labels will not survive the six-month conversation test.

AAD Section III will likely expose tension between mathematically precise but heavy names (`composition closure`, `closure defect`, `unity dimensions`) and more memorable alternatives. I predict I will be conservative on exact formal terms but more open to prose aliases for regions, regimes, and classifications that a reader needs to discuss repeatedly.

The AAD appendices will likely contain several candidates that are too appendix-shaped as current names: "derivation of X" labels, table-heading names, and meta-pattern labels. I predict `derivation audit`, `identifiability floor`, `separability pattern`, and `additive coordinate forcing` will need especially careful scope-honesty checks because meta-segment names are costly if too narrow.

TST will probably have the most practical-English candidate pressure. Names that sound good in AAD may be too academic for software readers. I predict I will prefer direct names when the referent is already familiar to engineers (`comprehension time`, `change distance`, `atomic changeset`) and resist ornate Greekization in TST unless the Greek term is already a cross-component formal object.

Logogenic/logozoetic segments will probably contain the most "future-vocabulary" risk: vivid terms that may age badly, morally loaded terms that may overstate current formal support, and inherited PROPRIUM vocabulary that may be meaningful in sibling projects but opaque in ASF. I predict I will often use `+1` rather than `+2` there unless the segment makes the term do real work.

## Predicted Open Or Overclaimed Areas

The largest overclaim risk is the boundary between exact Section II results and coupled logogenic agents. Any name implying that the clean orient cascade or directed separation applies unchanged to LLM-style agents should be treated suspiciously.

The second risk is meta-pattern overreach. `separability pattern`, `identifiability floor`, and `additive coordinate forcing` are powerful names if they cover all cited instances; if one instance sits outside the metaphor, the name should favor scope honesty over memorability.

The third risk is symbol aliasing. I expect targets for `$M_t$`, `$G_t$`, `$\Sigma_t$`, `$\mathcal C_t^{\text{commit}}$`, `$\kappa_{\text{processing}}$`, `$\Delta\rho^\ast$`, and sub-scope labels. My bias is to keep symbols formal and add prose aliases only when the prose alias has a distinct communicative role, not as interchangeable synonym clutter.

The fourth risk is collision or overloaded vocabulary. Words such as `hierarchy`, `closure`, `unity`, `agency`, `strategy`, `opacity`, `resilience`, and `sovereignty` carry adjacent-field baggage. I will treat baggage as useful when it imports the right structure and harmful when it creates false confidence.

## Novel And Consequential If The Framework Holds

The most consequential naming surface is the reusable diagnostic vocabulary: `satisfaction gap` / `control regret`, `adaptive reserve`, `directed separation`, and `calibration laboratory`. If those names hold, they let people talk about interventions without re-reading the formalism.

The second most consequential surface is the meta-pattern vocabulary. If `identifiability floor`, `separability pattern`, and `additive coordinate forcing` are accurate, they let readers recognize the framework's method rather than memorizing isolated results.

The third is the software/logogenic bridge vocabulary. Names that clarify code as observation infrastructure, committed chronica, context turnover, and coupled diagnostics could make AAD operational for the agents actually using and maintaining the repository.

## Expected Vote Patterns

I expect fewer votes early than the card's size invites. The first Section I definitions may surface only a handful of targets, and some should wait for later downstream use before I can judge whether the name carries.

When I vote, I expect many `keep +2` votes for terms that are already doing work; `+1` for acceptable finalists in noisier targets; and `-1` for candidates that are cute, too narrow, or category-confused. I expect write-ins to be rare but possible when a segment makes a target's framing feel off.

I expect to use notes to record scope and register: whether a term belongs at slug layer, prose-symbol alias layer, framing vocabulary layer, or public API layer. A good name in one layer can be wrong in another.

## What I Will Watch For During The Walk

I will watch for terms whose defining segment arrives before their card target's first random position in my tracker. The tracker is not an ordering; OUTLINE is.

I will watch for moments where the exploration rationale seems stronger than the candidate itself. The rationale may be true while the name is still awkward.

I will watch for cases where a target's current-name is a phrase from a table heading or local prose artifact rather than the actual concept readers need. Those may be target-framing notes rather than simple rename votes.

I will watch my own pull toward naming aesthetics without formal context. If the segment has not made the referent concrete, the honest action is to wait.
