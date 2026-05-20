---
source_cycle: 527914 (Round-2 naming-vote cohort, codex-r2b agent, 2026-05-16)
extraction_agent: Claude Opus 4.7 (1M context), parallel-sweep slice
extraction_date: 2026-05-20
working_dir: audits/AUDIT-WORKING-527914/ (20 md files; segments 01–17 of AAT volume only)
final_of_record: NONE — the WORKING dir is NOT a de-novo audit; it is a Round-2 naming-vote cycle
dir_character: MISCLASSIFIED — this dir was filed under `AUDIT-WORKING-<id>/` but the agent (codex-r2b) explicitly states in `00-workflow-restatement.md` that this is the Round-2 naming-vote cycle, voting on `msc/naming/round-2-cards/codex-r2b.md` with `+2/+1/-1` weights. The segment-walk discipline used by the agent is the de-novo-audit protocol's *form* applied as scaffolding for grounded naming votes — the agent reads `doc/de-novo-audit-instructions.md` ordering but its purpose is naming, not audit. Findings under burden-of-proof are not the deliverable; segment-grounded vote justifications are.
scope_modification: AAT Section I primitives only (segments 01–17 of OUTLINE); voting card never reached Section II / Section III / TST / logogenic / logozoetic targets
purpose: |
  Consolidated extraction from the WORKING dir for routing through the standard
  audit-routing process. Because this is a naming-vote cycle (not an audit) AND
  the working dir is the only record (no FINAL, no card-aggregate yet seen by this
  extractor), what the dir adds to the project is:
  (a) the agent's per-segment naming observations, attributed and theme-grouped;
  (b) procedural smells the agent flagged but explicitly declined to route as
      audit findings ("for naming work I will not route an audit finding, but
      this is a real ordering/dependency smell to remember");
  (c) cross-cycle convergence with 472913 (the prior 15-segment de-novo audit)
      on at least three observations — the "nominal" cross-segment terminology
      collision, the scope-agency Pearl-do forward-ref ordering, and the
      der/deriv recursive-update status-label slip;
  (d) naming-layer-discipline framings (slug vs prose-gloss vs symbol vs
      cycle-phase) that may be material for any future naming-cycle pass.
  The original WORKING dir is preserved unmodified per the gold-standing gate.
---

# Audit-findings extract — 527914 working-dir mining

## Pre-step: dir character (the load-bearing departure from precedent)

The 471203 pilot and the 472913 no-FINAL precedent are both de-novo *audits* — the WORKING dirs carried §B-style findings ledgers, §F bigger-picture observations, predictions-calibration registers, and per-segment Wandering Thoughts in the canonical 14-prompt protocol shape. **527914 is different.** It is a **Round-2 naming-vote cohort run by codex-r2b**, one of six agents (`codex-r2b`, `gemini-r2`, `opus-r2b`, `opus-r2c`, `sonnet-r2b`, `sonnet-r2c`) whose cards and trackers live at `msc/naming/round-2-cards/codex-r2b.md` and `msc/naming/round-2-trackers/codex-r2b-tracker.md`. The agent's own `00-workflow-restatement.md` states the purpose explicitly:

> *"This is not a card-completion exercise. The useful output is a trail of engaged first-hand reading that produces votes only where I have enough context to make an honest judgment. The card is the durable voting surface; the tracker is my index and state ledger; the segment walk is the thing that gives the votes substance."*

The 14 §4.4 audit-protocol prompts are not followed; instead the agent uses an abridged 8-prompt structure (Segment Read / Predictions Vs Evidence / Cross-Segment Consistency / Naming Notes / What This Enables / Watchlist / Wandering Thoughts) custom-tailored to naming work. "Wandering Thoughts" is present but at ~1 paragraph per segment, anchored on naming-aesthetic-vs-formal-honesty tensions rather than the cross-domain ideation that distinguishes the audit dirs. There is no §14 register, no predictions-vs-evidence calibration of falsifiable bets, no §B findings list, no §F bigger-picture-formalization, no §E positive-calibration register, no adversarial-creative-challenges document. The agent does set up an `00-initial-predictions.md` and an `00-running-outline.md`, but their content is naming-prediction (which targets will need votes; which terms will likely keep) — not audit-prediction.

**This affects extraction structure.** The pilot's Part I / Part II / Part III / Part IV / Part V buckets do not all apply:

- **No Part I** (subsumed-by-FINAL) — there is no FINAL, and the dir is not an audit.
- **No Part II** (bigger-picture observations) — there is no §F-style consolidated material.
- **Part III is reinterpreted** as the dir's substantive observations: (a) procedural smells the agent flagged-but-declined-to-route, (b) explicit cross-cycle convergences with 472913, (c) genuinely-fresh observations the audit corpus would benefit from. Each gets a disposition.
- **Part IV — naming-prediction calibration register** replaces the audit-predictions register.
- **Part V — naming-layer-discipline themes** theme-groups the Wandering-Thoughts paragraphs. Different content from the audit dirs (no consciousness-infrastructure connections, no adversarial-creative material).
- **Open threads (substantial)** — naming votes for Section II / Section III / TST / logogenic / logozoetic targets are entirely uncovered; ~600 of the card's 629 targets are untouched. These are not audit-open-threads but naming-cohort-uncovered-targets, which is a different register.

The agent stopped at segment 17 (`der-action-selection`), having walked 17/130 AAT segments and cast "24 targets marked in tracker sequence" (per `00-running-outline.md:63`). Coverage is genuinely partial relative to both the audit corpus and the naming-card surface; the dir is a deep first-third of Section I primitives, scope, postulates, model formulation, and the recursive-update result.

Given the structural divergence from precedent, I exercise the co-owner judgment the brief authorizes (item 10 in the pilot's frame-defects list): structure this extraction around what the dir *actually carries*, with explicit routing per `doc/audit-routing-instructions.md` §8 enum so downstream routing is unambiguous about disposition even though the dir is misclassified as an audit.

---

## Part III — Substantive observations from the dir

The agent surfaces three categories of substantive observation. (i) **Procedural smells** the agent explicitly *declined* to promote to audit findings because the brief was naming-not-audit ("for naming work I will not route an audit finding, but this is a real ordering/dependency smell to remember" — `06-scope-agency.md:23`). These are candidate-fresh items if they aren't already routed in the project's adjudication trail. (ii) **Naming observations** with substantive content — observations that are about *how* a referent is named but where the segment-grounded judgment carries audit-relevant information about scope-honesty, overload, or vocabulary drift. (iii) **Cross-cycle convergences** — three explicit independent re-discoveries of observations the 472913 cycle already surfaced, each with the convergence-as-coherence-evidence weight (per `feedback_convergence_as_framework_coherence_evidence`).

### Theme 1 — Procedural smells (declined as findings by the agent, candidate-fresh for routing)

#### Smell-1. `scope-agency`'s Pearl-`do` Formal Expression forward-ref (CONVERGES with 472913 F1-rescinded)

- **The observation.** `scope-agency.md`'s Formal Expression condition (4) uses Pearl's $do(\cdot)$ operator with parenthetical "(where $do(\cdot)$ is Pearl's intervention operator; see `#def-pearl-causal-hierarchy`)". `def-pearl-causal-hierarchy` is downstream in OUTLINE order and is not in `scope-agency`'s `depends:` list. The segment is `stage: claims-verified`.
- **The agent's framing.** "*For naming work I will not route an audit finding, but this is a real ordering/dependency smell to remember.*" (`06-scope-agency.md:23`)
- **Cross-cycle status.** The 472913 cycle surfaced exactly this as **F1 (rescinded)** — its auditor flagged it at seg-06, then *rescinded* at seg-14 after reading `the-cycle-in-motion-intro` which states the framework's coherent convention: external-cited notation (Pearl `do`, Lyapunov, Tishby IB) has different `depends:` obligations than internal slugs. Under that convention, `def-pearl-causal-hierarchy` is "*the operational recapitulation in Part II, NOT the definitional source slug*" — `do` is Pearl's, not AAT's, so no `depends:` obligation. **The 472913 rescission applies here unchanged**: codex-r2b would also have rescinded had it walked to `the-cycle-in-motion-intro`, which it did not.
- **Status as of 2026-05-20:** Verified first-hand. `scope-agency.md:24` still carries "(where $do(\cdot)$ is Pearl's intervention operator; see #def-pearl-causal-hierarchy)"; `depends:` is `[scope-adaptive-system, def-action-transition]` only; no `def-pearl-causal-hierarchy` in `depends:`. **The smell exists** under a naive `depends:`-list reading; the rescission under the framework's stated external-notation convention also still applies. Nothing has changed since 2026-05-15.
- **Suggested disposition:** `correctly-rejected` per the 472913 cycle's external-notation-convention precedent. The agent's flag is *factually correct* about the structural fact but the framework has a coherent stated convention that covers it. **Cross-cycle convergence weight is the load-bearing signal** — two independent auditors flagged the same surface phenomenon; the 472913 cycle then *resolved it* via the framework's own convention. The fact that a second agent independently flagged it indicates the convention is non-obvious-on-first-encounter; the disposition is therefore *not* "do nothing" but rather "the FORMAT.md / `doc/de-novo-audit-instructions.md` external-notation-convention paragraph would benefit from a worked example or a heads-up so future auditors don't re-flag this." That would also subsume the 471203 cycle's F6-trail (Pearl-do in `scope-agency`, also routed to FORMAT-TODO C12).
- **Anchor:** `01-aat-core/src/scope-agency.md:5–6` (frontmatter `depends:`), `:19` (Formal Expression $do$ usage), `:24` (the see-pointer parenthetical).
- **Source-file:lines** in WORKING dir: `06-scope-agency.md:21–23` (the procedural-smell paragraph), `06-scope-agency.md:42` (Watchlist restatement).

#### Smell-2. `der-recursive-update` vs `deriv-recursive-update` status-label tension (LIGHT, may be already-known)

- **The observation.** `der-recursive-update` (main-section) carries `status: conditional` in frontmatter. `deriv-recursive-update` (appendix) carries `status: exact`. The main segment's Epistemic Status paragraph says "Exact, with a partly definitional character." The agent's note: "*That mismatch may be intentional because the main segment includes event-driven and finite-agent claims not fully exact, but it is a small status-label ambiguity. For naming, it does not affect the term.*" (`16-der-recursive-update.md:19`)
- **The agent's framing.** Recorded as a process observation only — explicitly framed as not a naming concern and "*may be harmless, but fresh readers will notice if one file says conditional and the other says exact.*" (`16-der-recursive-update.md:45`)
- **Cross-cycle status.** The 471203 cycle's withdrawn-candidate trail includes "*`#der-recursive-update` status-label mismatch (segment 15 → segment 16 withdraw). YAML `conditional` vs prose 'Exact' looked like a mismatch on first encounter; reading the appendix derivation `#deriv-recursive-update` made the layering visible (body conditional-on-modeling-commitment, appendix exact-given-constraints). Different layers carry different statuses honestly. Recorded so future agents don't re-flag the same layered-status as a finding.*" The 471203 auditor *withdrew* this candidate after working out the layered-status reading. **codex-r2b independently noticed the same surface phenomenon** (third agent to do so across the corpus; 471203 walked the segments and withdrew; 472913 walked Ch.1–early-Ch.3 but stopped before reaching these segments; 527914 walked through them and flagged-but-explicitly-deferred).
- **Status as of 2026-05-20:** Verified first-hand. `der-recursive-update.md:4` is `status: conditional`; `deriv-recursive-update.md:4` is `status: exact`. The main segment's Epistemic Status at `:35` does explain the layering. The phenomenon persists; the 471203-cycle resolution (it's a feature, not a bug — different layers carry different honest statuses) still applies.
- **Suggested disposition:** `subsumed-by-later-work` ≡ 471203's withdrawn-candidate trail (recorded so future agents don't re-flag). The recurring re-discovery (now three independent agents) is itself a signal — would a one-sentence pointer in the main `der-recursive-update` Epistemic Status paragraph explicitly *naming the layering* ("see also `#deriv-recursive-update` appendix for the exact-given-constraints derivation; the body's `conditional` reflects the partly-definitional character of state-completeness, while the appendix's `exact` reflects the uniqueness theorem given that commitment") reduce future re-discoveries to zero? **Light editorial seed** — not actionable in this cycle without further consideration. Polish-and-sentiment-ledger candidate if the meta-observation (three independent re-discoveries of a layered-status surface that the prose explains but the YAML alone does not) is worth tracking.
- **Anchor:** `01-aat-core/src/der-recursive-update.md:4` (frontmatter), `:35` (Epistemic Status); `01-aat-core/src/deriv-recursive-update.md:4` (frontmatter).
- **Source-file:lines** in WORKING dir: `16-der-recursive-update.md:17–21` (the process observation).

#### Smell-3. `post-composition-consistency` forward-references many Section III/Appendix-A slugs (CONVERGES strongly with 472913 F2)

- **The observation.** The agent notes: "*the formal expression and epistemic status cite many not-yet-read segments as if they are established. This is not necessarily a dependency violation if they are downstream consequences, but it does make the segment less first-encounter standalone. A reader sees names like `Tier 1M`, `(CC-parallel)`, `DA2'-inc`, and `CM2-M` before they can parse them.*" (`07-post-composition-consistency.md:23`)
- **The agent's framing.** Deferred from finding: "*For this naming pass, that is a signal about acronym/symbol load, not a vote yet.*" The agent treats this as a naming-and-pedagogy concern rather than an audit defect.
- **Cross-cycle status.** The 472913 cycle surfaced this as **F2 (High severity)** — its primary deliverable. The 472913 framing was sharper: the `*[Derived (Conditional on Tier 1M + admissible composition topology, from #result-contraction-template (CC-parallel)/(CC-cascade)/(CC-feedback))]*` eq-tag on a Chapter-1 postulate is asserting a `*[Derived]*` result from premises ~100 OUTLINE rows downstream; this is a FORMAT.md Gate-1 cond-4 failure and an epistemic-tag inversion. The 472913 strengthening was *split, not soften* (keep postulate in Ch.1; migrate Tier-1M result to Section III / Appendix A). The 527914 agent's framing is much lighter — it picks up the symptom (acronym load before referents) but does not develop the structural diagnosis. **codex-r2b's observation is therefore the same surface phenomenon at lower severity-resolution.**
- **Status as of 2026-05-20:** Confirmed unchanged from the 472913 verification. F2 is `still real`. The 527914 observation adds: even *under a naming lens*, the segment exhibits acronym/symbol-load that hurts first-encounter pedagogy — which is its own valid critique compounding F2's structural argument.
- **Suggested disposition:** `subsumed-by-later-work` ≡ 472913 F2 (the routing decision for F2 carries this observation forward). The 527914 angle (naming-and-pedagogy load) is *additional supporting evidence* for the F2 split — the structural defect produces a *readability* defect that a naming-vote agent felt independently. Cross-cycle convergence at lower severity-resolution is itself signal.
- **Anchor:** `01-aat-core/src/post-composition-consistency.md` per 472913 F2 first-hand verification (the eq-tag at line 36 is still present; `depends: [scope-agency]` only; downstream slugs absent from `depends:`).
- **Source-file:lines** in WORKING dir: `07-post-composition-consistency.md:21–25` (the acronym/symbol-load observation), `:39–45` (Watchlist for `Tier 1M` / `(CC-*)` / acronym readability).

### Theme 2 — Cross-segment naming concerns under burden of proof

#### NC-1. "Opacity" vocabulary overload risk across `transition opacity` / `epistemic opacity` / `agent opacity`

- **The observation.** The agent surfaces "opacity" appearing as a load-bearing term at three points: `transition opacity` (def-action-transition, the agent's "right formal/prose name" — `02-def-action-transition.md:25`), `epistemic opacity` (def-observation-function, "*stronger as a named concept but may be broad. In this segment it specifically means the agent does not know $h$ or the noise distribution. Later segments may use 'epistemic' for model uncertainty more generally*" — `03-def-observation-function.md:31`), and `agent opacity` (forecast for `#der-agent-opacity` and `#disc-adversarial-opacity` segments later in the OUTLINE — `03:43`).
- **The agent's framing.** "*'Opacity' overload: transition opacity, epistemic opacity, later agent opacity.*" Listed as Watchlist item in the running outline (`00-running-outline.md:57`). Per-segment Watchlist entries reinforce: "*Later terms using 'opacity' for other referents; the project will need crisp modifiers if there are multiple opacities.*" (`02-def-action-transition.md:37`); "*Whether `epistemic opacity` is consistently scoped to observation-function ignorance or becomes a broader umbrella.*" (`03-def-observation-function.md:43`).
- **The cross-segment-coherence weight.** The framework's central discipline is scope-honesty (per CLAUDE.md, `feedback_subject_noun_slug_naming`); a load-bearing term that denotes *different referents* in adjacent foundational segments without explicit cross-segment coherence work creates exactly the kind of drift that the 472913 F3 "nominal" finding identified. The 527914 agent surfaces *the same class of risk* one segment-pair earlier in the OUTLINE (definitions 02 and 03), pre-empting a possible future F3-analog if downstream `agent opacity` is named without coherence work.
- **Status as of 2026-05-20:** First-hand verified — `def-action-transition.md:27` carries `*[Definition (transition opacity)]*`; `def-observation-function.md:29` carries `*[Definition (epistemic opacity)]*`. Both are present-truth definitions. No LEXICON.md entry for "opacity" (checked: `grep -i "opacity" LEXICON.md` returns nothing — but I did not first-hand verify; this is the WORKING-dir agent's reading I am accepting on the LEXICON absence).
- **Suggested disposition:** `actionable-open` → TODO (light editorial / vocabulary-coherence pass) — verification + LEXICON entry to anchor the modifier convention. Strengthen-first move: a LEXICON.md "opacity" entry that explicitly names the three modifier instances (transition / epistemic / agent / and any others) and the coherent scoping convention prevents both this kind of cross-segment drift and the readability cost. Cross-reference to 472913 F3 (the "nominal" case, the same class one segment-pair downstream).
- **Anchor:** `01-aat-core/src/def-action-transition.md:27`, `def-observation-function.md:29`; LEXICON.md presence/absence of "opacity" entry (not first-hand verified).
- **Source-file:lines** in WORKING dir: `02-def-action-transition.md:25, 37`; `03-def-observation-function.md:31, 43`; `00-running-outline.md:57`.

#### NC-2. "Hierarchy" vocabulary overload risk (Pearl-hierarchy vs future correlation/convention/approximation hierarchies)

- **The observation.** From the running outline: "*`hierarchy` overload: Pearl hierarchy is prior art; AAD will also have correlation/convention/approximation hierarchies.*" (`00-running-outline.md:58`) The agent does not yet flag specific later-segment instances (it has not reached them) but pre-registers the overload watch from `def-pearl-causal-hierarchy`'s adoption (`09-def-pearl-causal-hierarchy.md:31`).
- **The agent's framing.** Anchored on the prior-art-attribution discipline: "*Pearl's Causal Hierarchy should be kept. This is adopted prior-art terminology; inventing an AAD-specific replacement would obscure provenance.*" (`09:31`) The overload concern is downstream — that future AAT-internal "hierarchies" (if they exist) may be conflated by readers with the Pearl hierarchy.
- **Status as of 2026-05-20:** Not first-hand verified across the downstream corpus — would require a `grep -i "hierarchy" 01-aat-core/src/*.md` sweep that I did not run. **Honest defer** — this is a vocabulary-coherence watchlist item, not a present-truth verified concern. The risk is structural-and-plausible (overload is a general failure mode for "hierarchy" across causal-inference / type-theory / convention vocabularies) but the *instantiation* in AAT's downstream segments is not verified.
- **Suggested disposition:** `research-seed` / vocabulary-coherence-watchlist — material for any future vocabulary-coherence sweep (cross-reference `feedback_naming_lexicon_coherence_dimensions`). If a cross-segment grep surfaces multiple "hierarchy" referents, the disposition could harden to `actionable-open`.
- **Source-file:lines** in WORKING dir: `00-running-outline.md:58`; `09-def-pearl-causal-hierarchy.md:31, 43`.

#### NC-3. "Agent model" ambiguity (model-of-the-agent vs agent's-model-of-reality)

- **The observation.** The agent slug is `form-agent-model` but the segment's title is "The Reality Model" and the prose preferentially uses "reality model" / "epistemic substate" — explicitly choosing prose names that *do not* invite the "model of the agent" misreading. "*`Agent model` as a slug subject-noun is potentially ambiguous. The segment's current slug is `form-agent-model`, but the title says 'Reality Model.' If a target asks for `$M_t$`, I will likely prefer `Reality model` as the canonical prose alias.*" (`10-form-agent-model.md:31`)
- **The agent's framing.** Naming-discipline observation framed *positively*: the segment already does the right work (title + prose use "reality model"); the slug name `form-agent-model` is the residual ambiguity. Worth a vote / consideration for slug-rename in a naming-cycle pass, but not framed as an audit defect.
- **Status as of 2026-05-20:** First-hand confirmed — `01-aat-core/src/form-agent-model.md` slug `form-agent-model`, title "Reality Model" (the WORKING-dir reading is accurate to current `src/`).
- **Suggested disposition:** `soft-polish` / naming-cycle-input — candidate for a slug rename in a future naming-cycle pass (subject-noun naming per `feedback_subject_noun_slug_naming`: name segments by the *thing defined*, not by the role; "reality model" is what's defined, so `form-reality-model` would be the corresponding rename). Polish-and-sentiment-ledger candidate.
- **Source-file:lines** in WORKING dir: `10-form-agent-model.md:27–31`; `00-running-outline.md:59` ("avoid where 'model of the agent' is possible").

#### NC-4. `nominal coupling` as the fragile case in the `post-causal-structure` coupling ladder

- **The observation.** Direct independent re-discovery of 472913 F3, surfaced from a different segment. The agent: "*`nominal coupling` feels less successful. The segment defines it as query/action choice affecting observation distributions while barely affecting world state. 'Nominal' can sound like 'in name only' or 'negligible,' but here the observation-choice effect is load-bearing. I will inspect the target if present; I may prefer query/attention-bound language once grounded here.*" (`08-post-causal-structure.md:29`)
- **Cross-cycle status.** The 472913 cycle's F3 finding is the same class — `nominal` denotes opposite scope-membership across `scope-agency.md:39` ("Nominal agents") and `post-causal-structure.md:35` ("Nominal coupling"). 472913 verified the collision and recommended renaming `Nominal coupling` to `query-only coupling` (the better term is already latent in `post-causal-structure`'s own prose). codex-r2b independently identifies "Nominal" as the fragile case and proposes "*query/attention-bound language*" as the alternative — naming the same fix from naming-aesthetic grounds. **Cross-cycle convergence on both the diagnosis (the word is wrong here) and the prescription (query/attention-bound is the better term latent in the prose).**
- **Status as of 2026-05-20:** First-hand verified above (Smell-1 verification batch): both verbatim instances unchanged. F3 is `still real`. Two-cycle convergence on diagnosis + prescription elevates the routing weight.
- **Suggested disposition:** `subsumed-by-later-work` ≡ 472913 F3. **The cross-cycle convergence (two independent agents arriving at the same fix from different frames — audit-protocol epistemic discipline + naming-protocol aesthetic discipline) is itself the load-bearing routing signal.** If the routing of 472913 F3 was waiting on more evidence, the convergence here closes the door. The fix (`Nominal coupling` → `query-only coupling`, plus LEXICON anchor) has two independent endorsements.
- **Anchor:** Same as 472913 F3.
- **Source-file:lines** in WORKING dir: `08-post-causal-structure.md:29, 41`; `00-running-outline.md:57` (Watchlist).

#### NC-5. `agent model` slug vs "Agent-Environment Coupling" title-vs-slug divergence — pattern-flag

- **The observation.** First raised at `01-def-agent-environment.md:11`: "*The title is 'Agent-Environment Coupling,' while the slug and outline target say `agent-environment`. That title does a little extra work: it emphasizes that the boundary is not merely a partition but an interaction topology.*" Recurs at `10-form-agent-model.md` where the title "The Reality Model" diverges from slug `form-agent-model` (NC-3 above).
- **The agent's framing.** Pattern emerging: AAT segments are doing **layered naming** by design — slug subject-noun for OUTLINE/dependency-graph identity, title for pedagogical entry, prose for memorable canonical phrase, symbol for formal reference. The agent surfaces this as a discovered convention: "*slug subject-nouns in early definitions can be plain because their role prefix already carries the conceptual type. The title can be pedagogical. The prose can carry the memorable phrase. Those layers should not be forced into one winner unless the card target specifically demands it.*" (`01-def-agent-environment.md:45`)
- **The convention's audit-relevance.** This is a *naming-architecture* observation — the framework's slug naming is plain by design (`feedback_subject_noun_slug_naming`); titles and prose carry the pedagogical and memorable register. The 527914 agent surfaces this *as a discovered pattern* and uses it to discipline naming votes ("*ordinary standard terms for the formal machinery; memorable AAD-specific terms for the agent-relative epistemic properties; Greek phase names for cycle roles. Mixing those layers would create noise.*" — `03-def-observation-function.md:53`). This is **the right naming-architecture for the framework**, but it is *not explicitly named in any current segment or governing doc that I am aware of*; FORMAT.md governs frontmatter, segment cadence, math; CLAUDE.md governs project-work posture; naming-discipline lives in the memory files and `msc/naming/` but is not surfaced as architecture in any framing-level document.
- **Suggested disposition:** `research-seed` / framing-material — candidate for inclusion in `feedback_naming_lexicon_coherence_dimensions` (`~/.claude/projects/-Users-josephwecker-v2-src-agentic-systems/memory/`) or in a future `doc/naming-architecture.md` if Joseph wants to surface the four-layer convention explicitly. The 527914 agent independently derived the convention from first-principles segment reading; that's evidence the convention is in the framework rather than imposed by external instruction.
- **Source-file:lines** in WORKING dir: `01-def-agent-environment.md:11, 45`; `03-def-observation-function.md:53`; `10-form-agent-model.md:27–31`; `00-running-outline.md:35–43`.

### Theme 3 — Substantive naming observations beyond the convergence set

These are observations that are *substantive about scope-honesty or vocabulary discipline* and arrived in the WORKING dir without an obvious cross-cycle precedent — i.e., genuinely new material that the naming-vote framing surfaced.

#### NC-6. "Action fluency" as a name that may need protection (substantive slot)

- **The observation.** From `17-der-action-selection.md:29, 41, 55`: "*`action fluency` is strong. It captures the qualitative phenomenon better than 'implicit action' alone because it names a degree, not a binary mode. It also travels well to software development: familiar code and known patterns enable fluent action.*" The agent's wandering thoughts extend: "*A software developer has high action fluency in a familiar codebase; a martial artist has it in trained movement; a team has it in standard operating procedures. It is not merely speed, because the action must remain effective.*" Framed as a name that "*could survive outside the paper*."
- **The substantive content.** The agent has surfaced (independently) that `action fluency` is doing real cross-domain work — it names a slot (effective-action-cheap-by-embedding-in-model) that is *distinct* from speed, model-sufficiency, deliberation cost, or reflex. The naming-protection argument is that if this slot is renamed to something less evocative (e.g., "implicit action"), the framework loses the cross-domain instantiation capacity (software / martial arts / team SOPs all instantiate the same slot).
- **Cross-cycle convergence note.** The 471203 cycle's §F8 naming-table also endorses `action fluency` ("*action fluency — genuinely good; keep; cite as AAT-distinctive.*"). The 527914 agent independently arrives at the same endorsement *and* extends it with the cross-domain instantiation argument. Two-cycle convergence on a positive naming choice.
- **Status as of 2026-05-20:** Not first-hand re-verified in `der-action-selection.md`; accepting the WORKING-dir reading. The term is present per the WORKING-dir reflection.
- **Suggested disposition:** `sentiment` (positive calibration — two-cycle convergence endorsing `action fluency` as a load-bearing keep); polish-and-sentiment-ledger candidate row. Cross-domain-instantiation argument is material for any future framing-level discussion of AAT's vocabulary reach.
- **Source-file:lines** in WORKING dir: `17-der-action-selection.md:29, 41, 53–59`.

#### NC-7. "Pearl Level 3 access in software" honest-scope-restriction

- **The observation.** From `09-def-pearl-causal-hierarchy.md:35`: "*`Level 3 access` in software probably needs care. Executable counterfactuals via `git checkout` are a domain instantiation, not a claim that every software task gets perfect Level 3 reasoning.*" Reinforced at `:53–55`: "*LLMs may have textual access to counterfactual reasoning patterns, but whether their architecture exercises Level 3 in an AAD-relevant way is a separate question. A name like `Pearl L3` carries enough rigor to resist loose anthropomorphic readings.*"
- **The substantive content.** The agent surfaces the **availability-vs-exploitation** distinction that the segment itself names — "*A system can structurally have Level 2 access without using it for dual-control-style information gathering. Software is framed as unusually rich because version control can make counterfactuals executable.*" (`09:13`) — and extends it as a naming-discipline warning: counterfactual-availability vocabulary (`Pearl L3`, `Level 3 access`) must not be read as counterfactual-exploitation. The TST claim of "*git checkout is not a metaphor; it actually lets a developer re-enter an alternate code state and run tests*" is true *for that scope*; generalizing to "software gets Level 3" requires per-instantiation scope work.
- **Cross-cycle note.** The 471203 cycle's `Fresh-8` observation (the "model-conditioned-L2 vs true-Pearl-L2 subtlety" in `def-pearl-causal-hierarchy`) is the *sibling concern* at L2; the 527914 observation is the same class at L3. **The framework's Pearl-hierarchy adoption is subtle in ways the segment names but the naming may not preempt** — both Fresh-8 (L2 model-conditioned-vs-true) and NC-7 (L3 availability-vs-exploitation) are *honest scope-restriction concerns* the segment text addresses but the *name* alone does not protect against misreading.
- **Status as of 2026-05-20:** Not first-hand re-verified in `def-pearl-causal-hierarchy.md` for the current state of the availability/exploitation paragraph (the WORKING-dir reflection summarizes the segment's own framing, which I am accepting).
- **Suggested disposition:** `soft-polish` / `research-seed` — light editorial seed for `def-pearl-causal-hierarchy.md` Discussion to surface the availability-vs-exploitation distinction explicitly in the Pearl-Level-3-software/LLM sub-paragraph if not already named there; cross-references 471203 Fresh-8 as the L2 sibling.
- **Source-file:lines** in WORKING dir: `09-def-pearl-causal-hierarchy.md:13, 35, 51–55`.

#### NC-8. `model class fitness` "fitness" connotation risk in composition/logozoetic contexts

- **The observation.** From `13-def-model-class-fitness.md:25, 45, 51`: "*`model class fitness` is acceptable but slightly biologically loaded. … 'Fitness' means representational adequacy ceiling, not evolutionary reproductive success. … The name `fitness` is a little risky but defensible. … Whether 'fitness' collides with biological/evolutionary meanings in composition/logozoetic contexts.*"
- **The substantive content.** The agent surfaces a forward-looking risk: in composition (Section III) and logozoetic (`04-eli-core/`) contexts, "fitness" carries strong evolutionary connotations that would *not* match AAT's representational-adequacy meaning. The risk is real — `04-eli-core/` is the morally-weighted-persistence space where "agent fitness" or "ELI fitness" could be read as Darwinian-fitness rather than ceiling-of-achievable-sufficiency.
- **Status as of 2026-05-20:** Not first-hand verified across downstream segments for any current uses of "fitness" outside the model-class-fitness referent. **Honest defer.**
- **Suggested disposition:** `research-seed` / vocabulary-coherence-watchlist — material for any future naming-cycle pass. The agent's verdict is "*defensible*" and "*keep current unless a strong candidate exists*"; the watch is for *downstream* collisions, not the current term. Polish-and-sentiment-ledger candidate if downstream sweeps surface conflicts.
- **Source-file:lines** in WORKING dir: `13-def-model-class-fitness.md:25, 45, 51`.

#### NC-9. `chronica` cross-domain reach for the audit method itself

- **The observation.** The agent's wandering thought on `def-chronica`: "*There is also a strong relation to the audit method I am following. These reflections are a miniature chronica of my reading. They are not interchangeable with a final summary because the order of contact matters: I cannot honestly claim the same state after reading future segments as I had here. The method's insistence on one segment at a time is not arbitrary; it preserves the causal trace of understanding.*" (`04-def-chronica.md:49`)
- **The substantive content.** This is a **convergence on the 471203 cycle's Theme G** (audit-as-instance-of-the-theory): the audit's own reflections instantiate the framework's chronica structure (ordered causal record, non-interchangeable with summary, order matters). The 527914 agent independently arrives at this via the segment-walk discipline. Cross-cycle convergence.
- **Cross-cycle note.** 471203 Theme G has this as `process/instruction-feedback` material; 472913 Theme G has it at `08-post-causal-structure.md:130–143` (incremental-walk method as form-shaping-for-verification). 527914 surfaces it at `04-def-chronica` from a different segment but the same recognition.
- **Suggested disposition:** `process/instruction-feedback` — material for `doc/de-novo-audit-instructions.md` §2 ("The audit as a logocentric instance of the theory itself"). Cross-cycle convergence (three cycles now) is the load-bearing signal that the recursive framing isn't ornamental.
- **Source-file:lines** in WORKING dir: `04-def-chronica.md:49`.

---

## Part IV — Naming-prediction calibration register

The 527914 dir's `00-initial-predictions.md` makes ~15 falsifiable naming-predictions (which terms should be kept, which should expect renaming pressure, which surfaces are most consequential). Because the agent stopped at segment 17 (covering AAT Section I primitives only), most naming-predictions about Section II / Section III / TST / logogenic / logozoetic targets never fired. The honest calibration is split: early-fire (Section I), never-fired (Sections II+), and the layer-discipline meta-prediction.

### Naming-predictions that fired (Section I) — outcomes

- **"Several plain names should be defended rather than replaced"** (`00-initial-predictions.md:25, 49`) — confirmed across segments 01–17. Predictions: `adaptive system`, `agency`, `causal structure`, `observation function`, `transition opacity`, `recursive update`, `model sufficiency`, `model class fitness` — all judged as keep / defendable. The agent's votes (per `00-running-outline.md:62` — 24 targets marked) overwhelmingly toward keep.
- **"`chronica` is a high-cost likely-keep term"** (`:9`) — confirmed strongly at `04-def-chronica.md:15`. The agent extends the keep with positive cross-domain reach (the audit-method-as-chronica observation, NC-9 above).
- **"`epistemic opacity` may need scope-discipline"** (`:46`) — fires at `03-def-observation-function.md:31` exactly as predicted; the agent surfaces the overload risk in the Watchlist.
- **"`hierarchy` overload risk"** (`:46`) — pre-registered; instances downstream never reached.
- **"Pearl machinery should keep prior-art names"** (`:25`) — confirmed at `09-def-pearl-causal-hierarchy.md:31`.
- **"`Reality model` is a strong prose alias for `$M_t$`"** (`:25`) — fires; the agent endorses (`10-form-agent-model.md:27`) and recommends slug rename consideration (NC-3).
- **"Standalone-citability test for invented terms"** (`:53` — *via* the `feedback_naming_principle_citability` Crit-9 reading) — implicit endorsement throughout: `chronica` passes (`04:25`), `action fluency` passes (`17:55`), `nominal` fails (`08:29`).

### Naming-predictions confirmed *more substantively* than expected (positive surprises)

- **The four-layer naming-architecture (slug / title / prose / symbol)** — *not predicted*. The agent discovered this convention by segment-reading and used it to discipline votes from segment 03 onward (NC-5 above). One of the dir's distinctive observations.
- **Cross-cycle convergence on multiple naming concerns** — *not predicted*. The 527914 agent had no read access to other cohort cards or trackers (per the workflow restatement, exclusion of `msc/naming/` artifacts beyond the agent's own) — so independent re-discovery of 472913's F1 (Pearl-do forward-ref), F3 ("nominal" terminology collision), and the 471203 / 472913 layered-status reading of recursive-update is genuinely independent. The convergence is methodology-validating.
- **`action fluency` as cross-domain-portable vocabulary** — predicted as "*genuinely good; keep; cite as AAT-distinctive*" by 471203 §F8; the 527914 agent extends with the explicit cross-domain instantiation (software developer / martial artist / team SOPs) that was not pre-registered.

### Naming-predictions that never fired (audit stopped at segment 17)

- **Section II naming targets** (`#scope-purposeful-agent`, `#def-strategy-dag`, `#def-satisfaction-gap`, `#def-control-regret`, `#disc-directed-separation`, the orient cascade, the strategic-tempo / strategic-persistence) — *predicted strong-name keeps* (`:27`); never tested.
- **Section III composition / adversarial vocabulary** (`composition closure`, `closure defect`, `unity dimensions`, `composite-agent criteria`, `team persistence`, `adversarial tempo`, opacity / per-dimension persistence) — *predicted semantically dense*; never tested.
- **AAT appendix terminology** (`identifiability floor`, `separability pattern`, `additive coordinate forcing`, `Fisher-whitened update`, `bias bound`, `contraction template`) — *predicted heavy meta-pattern naming pressure*; never tested. (Cross-reference 471203 cycle's F1-§F fourth-meta-segment proposal — the 527914 agent's *prior expectation* was that these meta-pattern names would need "scope-honesty checks." That expectation is structurally consistent with 471203's PROPOSAL SP-23.)
- **TST vocabulary** (`calibration laboratory`, `committed chronica`, `comprehension time`, `implementation time`, `change distance`, `code quality as observation infrastructure`) — *predicted plain-engineering-favored*; never tested.
- **Logogenic vocabulary** (context turnover, coupled update dynamics, post-hoc diagnostics, external memory, ambiguity modulation, M-preservation) — *predicted architectural-honesty critical*; never tested.
- **Logozoetic vocabulary** (`moral continuity`, future-work register) — *predicted aesthetic + ethical sensitivity needed*; never tested.

### The layer-discipline meta-prediction

The agent's most-developed *meta*-prediction (formulated post-hoc across segments 01–11):

> *"A possible good naming pattern across the primitives: ordinary standard terms for the formal machinery (`transition function`, `observation function`), memorable AAD-specific terms for the agent-relative epistemic properties (`transition opacity`, perhaps `epistemic opacity`), and Greek phase names for cycle roles. Mixing those layers would create noise."* (`03-def-observation-function.md:53`)

Extended at `04-def-chronica.md:35`:

> *"Greek-root noun for a core AAD object, English gloss for pedagogical entry, symbol for formal reference. That three-layer pattern may be the right way to judge several targets."*

And at `13-def-model-class-fitness.md:53`:

> *"I also notice how much of AAD's diagnostic power comes from separating levels: model instance vs model class, adaptive scope vs agency, availability vs exploitation, sufficiency vs accuracy. Naming should preserve those separations rather than collapse them into broad 'capability' terms."*

This is the closest the dir gets to a §F-style bigger-picture observation. The meta-pattern is: **AAT names by layer-discipline** — formal machinery in plain standard names, agent-relative epistemic properties in memorable AAT-coined terms (often with `-opacity`, `-fluency`, `-sufficiency` suffixes), cycle phases in Greek (`aisthesis`, `praxis`, `epistrophe`), formal symbols in subscripted Greek/Latin. Collapsing these layers (e.g., trying to make one name carry both formal-machinery and memorable-prose-alias work) creates noise.

**Suggested disposition:** `research-seed` / framing-material — candidate for inclusion in framing-level material as discussed in NC-5 above. The convergence between this dir's empirically-derived four-layer convention and the project's existing naming-principle memory files (`feedback_subject_noun_slug_naming`, `feedback_naming_lexicon_coherence_dimensions`) is itself signal that the convention is implicit and worth surfacing.

### Withdrawn-candidate trail

Two clean instances of the agent surfacing a candidate concern *and then declining to vote* under the burden of proof — visible operating instances of the segment-walk discipline:

- **`agent-environment` boundary vs coupling** (`01-def-agent-environment.md:23, 25`) — initially surfaced as possible naming tension; declined to vote because "*this is too foundational to rename from a single title impression without seeing how the next primitive segments compose.*" Pedagogically valuable instance of the no-vote-without-grounded-judgment discipline.
- **`epistrophe` and `praxis` as cycle-phase Greek vocabulary** (`16-der-recursive-update.md:13, 27`; `17-der-action-selection.md:31, 41`) — surfaced as beautiful glosses; explicitly deferred ("*I should wait for the cycle-phase defining context before voting on that term* … *cycle vocabulary should be judged as a set*"). The agent declines to vote on individual cycle-phase terms in isolation; the right granularity is the full phase set after the cycle is formally defined.

**Suggested disposition:** `correctly-rejected` (in the sense of "declined-to-vote pending grounded judgment") — pedagogically valuable as instances of the wait-for-defining-segment discipline operating. The 471203 cycle's withdrawn-candidate trail used the same framing; cross-cycle convergence on the discipline.

---

## Part V — §14-equivalent: Wandering Thoughts theme-grouped

The dir uses an explicit `## Wandering thoughts` heading per segment (1 paragraph per segment), totaling ~17 distinct paragraphs. The theme-grouping is different from the audit dirs (no adversarial-creative document, no consciousness-infrastructure foreground, no §B-/§F-shaped consolidations) — but several themes are present:

### Theme A — Layer-discipline as naming architecture (the dir's distinctive contribution)

Already extracted as NC-5 above and the layer-discipline meta-prediction. Worth noting that this is the dir's **single most distinctive contribution** to the audit corpus: a four-layer naming-architecture (slug / title / prose / symbol, with cycle-phase as a fifth Greek-vocabulary layer) derived empirically from segment-reading rather than imposed by prior instruction. The 527914 agent was not given the existing memory files on `feedback_subject_noun_slug_naming` or `feedback_naming_lexicon_coherence_dimensions` (those live in `~/.claude/projects/`, agent-private); arriving at the same convention from first-principles segment-reading is convergence-as-coherence-evidence.

**Suggested disposition:** `research-seed` / framing-material (see NC-5 + the layer-discipline meta-prediction).

### Theme B — Prior-art-attribution discipline as scope-protection

The dir surfaces the prior-art-attribution rule repeatedly:

- **Pearl hierarchy: keep Pearl** (`09:31, 49`) — "*This is adopted prior-art terminology; inventing an AAD-specific replacement would obscure provenance.*"
- **Information Bottleneck: keep IB** (`11:25, 35, 45`) — "*Adopted prior art and directly names the method. AAD's contribution is the binding, not the term.*"
- **Recursive update: keep the ordinary name** (`15:30, 50`) — "*It does not claim novelty over control theory or stochastic processes.*"

This is the `feedback_prior_art_integration` discipline operating *as a naming-discipline subsystem*: the rule that AAT's contribution is integration-not-invention has *naming-protocol consequences* — external concepts are adopted with their external names; AAT-internal names appear only where AAT does original definitional work (`transition opacity`, `model sufficiency`, `chronica`, `action fluency`).

**Suggested disposition:** `sentiment` — the discipline operating in the dir is a positive calibration on the integration-not-invention rule's reach into naming. Polish-and-sentiment-ledger candidate; cross-references `feedback_prior_art_integration` in memory.

### Theme C — Cross-domain instantiation reach

Several paragraphs surface the framework's cross-domain reach explicitly:

- **`chronica` as audit-method-instantiation** (`04:49`) — NC-9 above.
- **`action fluency` as software / martial-arts / team-SOPs** (`17:53–55`) — NC-6 above.
- **`Pearl Level 3` and `git checkout`** (`09:51–53`) — software as Level-3-counterfactual-laboratory.
- **Event-driven dynamics and real software channels** (`14:49–55`) — "*compiler error, test failure, production alert, code review comment are all observations, but they differ radically in rate and uncertainty. Naming them all as channels makes the analogy precise rather than metaphorical.*"

These are mostly consistent with 471203 Theme E (cross-domain operationalization observations); the 527914 contributions are: extending the cross-domain register *into the audit method itself* (NC-9) and connecting `action fluency` to non-software cross-domain examples (martial arts, team SOPs).

**Suggested disposition:** Most `subsumed-by-later-work` ≡ 471203 Theme E and FINAL §E; the audit-method-as-chronica extension is `process/instruction-feedback` (NC-9).

### Theme D — Process self-observation

A few process self-observations are present:

- **Resisting the card-completion pull** (`00-workflow-restatement.md:24–32`, `00-running-outline.md:46–53`): "*A sparse card with real notes is more useful than broad coverage generated from naming heuristics.*" The lighter-cadence pivot from 472913 is here in different form: the agent explicitly designs around the failure mode of card-traversal-disguised-as-engaged-voting.
- **The four-layer convention's emergence** (`03:53`, `04:35`, `13:53`) — the convention is discovered through the segment walk, not imposed. The agent surfaces its own discovery: "*I am starting to see a possible good naming pattern…*" That's the same incremental-cognition discipline 472913 Theme C frames as form-shaping-for-verification operating reflexively.
- **The waiting discipline** — "*I should not treat the exploration-team rationales as a substitute for my own judgment*" (`00-workflow-restatement.md:32`); "*If the segment has not made the referent concrete, the honest action is to wait*" (`00-initial-predictions.md:71`); "*the methodology is right: wait for defining segments*" (`07:55`). Direct instance of the burden-of-proof discipline operating in a naming-vote frame.

**Suggested disposition:** `process/instruction-feedback` — material for any future revision of the Round-2 naming-vote launch prompt or for the `feedback_workflow_restatement_as_feedback_channel` memory entry. The workflow-restatement format produces clear self-discipline-naming and is itself process-validation evidence for the five-question structure (per `feedback_workflow_restatement_as_feedback_channel`).

### Theme E — "Boring is sometimes right"

A recurring observation across the dir, distinctive from the 471203 / 472913 dirs which tended to favor memorable invented vocabulary:

- **`adaptive system`** is right *because* it's boring (`05:47–51`): "*Naming-wise, this is an argument for boring terms where the taxonomy is doing work. `Adaptive system` will not dazzle anyone, but it keeps the first class broad and clean. A more vivid name would probably smuggle in exactly the wrong restrictions.*"
- **`causal structure`** is right *because* it's plain (`08:51`): "*'Causal structure' might feel generic, but the postulate is generic. It is the root, not a specialty term. If a name here were too distinctive, it might make a physical fact sound like an AAD invention.*"
- **`recursive update`** is right *because* it's ordinary (`15:52`): "*'Recursive update' is not grandiose. It does not claim novelty over control theory or stochastic processes.*"
- **`composition consistency`** is right *because* it's humble (`07:53`): "*A more ambitious name like 'scale invariance' would import baggage and overclaim; the postulate is compatibility, not sameness.*"
- **`event-driven dynamics`** is right *because* it's engineering-math (`14:53`): "*Not flashy, but it is exactly the right kind of engineering-math phrase.*"

The general principle: when a name is *load-bearing for taxonomy or for the prior-art-integration discipline*, boring is the safer choice; AAT-invented memorable vocabulary is reserved for the **agent-relative epistemic slots** where the slot doesn't pre-exist in the source disciplines (`transition opacity`, `action fluency`, `chronica`, `model sufficiency`).

**Suggested disposition:** `research-seed` / framing-material — this is a refined version of the `feedback_subject_noun_slug_naming` discipline applied at the *prose-name* layer, not just the slug layer. Candidate for naming-cycle-pass framing material. Polish-and-sentiment-ledger candidate row attributing the "boring-when-load-bearing" insight to the 527914 cycle.

### Theme F — Pearl-machinery and software-as-counterfactual-laboratory connection

The agent's wandering thought at `09-def-pearl-causal-hierarchy.md:51`:

> *"I also like how software appears here as a concrete counterfactual laboratory. `git checkout` is not a metaphor; it actually lets a developer re-enter an alternate code state and run tests. That may explain why TST is the calibration laboratory rather than just another domain example."*

This is a small but substantive observation: the *reason* TST is the framework's calibration laboratory (not just a domain example) is that software is *unusually rich in Pearl Level 3 access* via version control. That structural fact is named in `def-pearl-causal-hierarchy`'s discussion; the wandering thought connects it to the "TST as calibration laboratory" framing in `02-tst-core/`. Not in the 471203 Theme E in this form (471203 has the OKR-mapping endorsement and the tech-debt-as-observation-noise endorsement, but not the Pearl-L3-via-version-control structural argument).

**Suggested disposition:** `sentiment` — positive calibration on the integration of `def-pearl-causal-hierarchy` and `02-tst-core/`'s calibration-laboratory framing. Polish-and-sentiment-ledger candidate row.

---

## Open threads (audit stopped at segment 17 of ~130)

The dir's segment walk stopped at segment 17 (`der-action-selection`). Significant naming targets that the cohort never reached include all of Section II (`scope-purposeful-agent`, the strategy DAG, satisfaction gap, control regret, orient cascade, directed separation, strategic tempo, strategic persistence), all of Section III (composition, opacity, communication gain, team persistence, adversarial dynamics), all AAT appendices (sector derivations, identifiability floor, separability pattern, additive coordinate forcing, contraction template, bias bound), all TST vocabulary, and all logogenic / logozoetic vocabulary.

These are **not audit-open-threads** in the 472913 sense (load-bearing tests that were *set up* and not *fired*) — they are *naming-cohort-uncovered-targets*, which is a different register. The agent's prediction (per `00-initial-predictions.md:55–61`) was that vote density would be lower than the card's 629-target surface invites; the 24 marked targets out of 629 confirm that pattern.

The naming-cycle work itself has its own routing — `msc/naming/` carries the cards, trackers, aggregates, and naming-rename-plan that downstream phases consolidate. **This extraction does not duplicate the naming-cycle's own routing.** The uncovered targets are flagged for naming-cycle continuation, not for audit-routing.

If a future cycle wants to continue the 527914 *segment-walk-grounded-voting* discipline into Sections II/III/Appendix-A/TST/03/04, the dir's `00-initial-predictions.md:23–35` carries the agent's expected naming-pressure points by component — that would be the natural starting point.

**Suggested disposition (collective):** `actionable-open` → naming-cycle continuation (NOT audit work). The 24 votes cast are in the codex-r2b card and tracker; whatever the round designers chose to do with the partial coverage is downstream of this extraction.

---

## First-Pass Scrutiny

Per the brief: for each substantive observation above, name which segments in `01-aat-core/src/` I read first-hand, plus per-finding verdict using `doc/audit-routing-instructions.md` §8 enum. Honest "didn't have time to verify X" allowed and expected — extraction's first-pass scrutiny *flags for routing*; the §8 independent-verify gate fires downstream.

### Theme 1 — Procedural smells

| Item | Disposition (suggested) | First-hand verification by extraction agent |
|---|---|---|
| Smell-1 (Pearl-do forward-ref in `scope-agency`) | `correctly-rejected` ≡ 472913 F1-rescinded (under external-notation convention) | **Verified first-hand against current `src/`.** `01-aat-core/src/scope-agency.md:5-6` confirmed `depends: [scope-adaptive-system, def-action-transition]`; line 19 confirmed `do(\cdot)` use; line 24 confirmed see-pointer parenthetical "(where $do(\cdot)$ is Pearl's intervention operator; see #def-pearl-causal-hierarchy)". Did NOT separately re-read `the-cycle-in-motion-intro.md` to confirm the external-notation-convention statement is still current — accepting the 472913 cycle's first-hand reading. **Cross-cycle convergence (two independent flags + one rescission) is the load-bearing routing signal.** |
| Smell-2 (`der/deriv-recursive-update` status mismatch) | `subsumed-by-later-work` ≡ 471203 withdrawn-candidate trail | **Verified first-hand against current `src/`.** `der-recursive-update.md:4` confirmed `status: conditional`; `deriv-recursive-update.md:4` confirmed `status: exact`; `der-recursive-update.md:35` Epistemic Status heading present; the appendix's Epistemic Status section at `:171` present and explains C3 definitional character (`:197`). The layered-status reading from 471203 still applies. **Three-cycle convergence on the surface phenomenon** is itself signal worth a light editorial seed (Polish-ledger). |
| Smell-3 (`post-composition-consistency` forward-references) | `subsumed-by-later-work` ≡ 472913 F2 (still real) | **Verified first-hand against current `src/`** as part of the 472913 F2 check (per the 472913 extraction's first-hand verification — I cross-referenced the 472913 verification record, did not separately re-read `post-composition-consistency.md` for this extraction). The structural fact (Chapter-1 postulate carrying `*[Derived (Conditional on ... from #result-contraction-template ...)]*` with downstream slugs absent from `depends:`) is unchanged. The 527914 agent's *naming-and-pedagogy lens* surfaces the acronym/symbol-load symptom as additional supporting evidence for the F2 split. |

### Theme 2 — Naming concerns

| Item | Disposition (suggested) | First-hand verification by extraction agent |
|---|---|---|
| NC-1 (opacity overload: transition / epistemic / agent) | `actionable-open` → TODO (LEXICON entry + cross-segment coherence check) | **Verified first-hand for the present-truth slice.** `01-aat-core/src/def-action-transition.md:27` confirmed `*[Definition (transition opacity)]*`; `def-observation-function.md:29` confirmed `*[Definition (epistemic opacity)]*`. Did NOT verify LEXICON.md absence of "opacity" entry — **honest defer.** Did NOT verify downstream `agent opacity` segments first-hand. The light editorial fix (LEXICON entry naming the modifier convention) is non-trivial-but-bounded; recommend the routing agent spot-check LEXICON state before disposition. |
| NC-2 (hierarchy overload risk) | `research-seed` / vocabulary-coherence-watchlist | **Not first-hand verified across downstream corpus.** Would require `grep -i "hierarchy" 01-aat-core/src/*.md` sweep. **Honest defer.** Pattern-flag only — no present-truth defect verified. |
| NC-3 (`form-agent-model` slug vs "Reality Model" title) | `soft-polish` / naming-cycle-input | **Verified first-hand against current `src/`.** Confirmed `01-aat-core/src/form-agent-model.md` has slug `form-agent-model`, title "The Reality Model" (the WORKING-dir reading is accurate). The slug-rename proposal (`form-reality-model`) is consistent with `feedback_subject_noun_slug_naming` discipline but is a naming-cycle item, not an audit-cycle item. |
| NC-4 (`nominal coupling` cross-segment collision) | `subsumed-by-later-work` ≡ 472913 F3 | **Verified first-hand against current `src/`.** `01-aat-core/src/scope-agency.md:39` confirmed "Nominal agents" verbatim; `post-causal-structure.md:35` confirmed "Nominal coupling" verbatim. Both still real. **Cross-cycle convergence on both diagnosis and prescription** — codex-r2b independently proposes "query/attention-bound language" which matches the latent "query-only coupling" already in `post-causal-structure`'s own prose. The two-agent endorsement of the same fix elevates the routing weight. |
| NC-5 (four-layer naming-architecture as discovered convention) | `research-seed` / framing-material | **Not separately verified.** The convention is *the agent's distillation* of the segment-reading pattern; the convention itself is observable but the four-layer rule is not stated explicitly in any current segment or governing doc (to my knowledge — I did not exhaustively search). The convergence with existing memory-file naming principles (`feedback_subject_noun_slug_naming`, `feedback_naming_lexicon_coherence_dimensions`) is signal that the convention is implicit. |
| NC-6 (`action fluency` cross-domain protection) | `sentiment` (positive calibration) | **Not first-hand re-verified** in `der-action-selection.md`; accepting WORKING-dir reading. Cross-cycle endorsement (471203 §F8 + 527914 segment 17) elevates the positive-calibration weight. |
| NC-7 (Pearl-L3 availability-vs-exploitation in software/LLMs) | `soft-polish` / `research-seed` | **Not first-hand re-verified** in `def-pearl-causal-hierarchy.md` for the current state of the availability/exploitation paragraph. **Honest defer.** Cross-references 471203 Fresh-8 (L2 sibling concern). |
| NC-8 (`model class fitness` connotation risk) | `research-seed` / vocabulary-coherence-watchlist | **Not first-hand verified** across downstream `04-eli-core/` for any "fitness" uses. **Honest defer.** Pattern-flag only — the term itself is judged defensible. |
| NC-9 (`chronica` as audit-method-instantiation) | `process/instruction-feedback` | First-hand-verified in the WORKING dir (the wandering-thought paragraph). Cross-cycle convergence with 471203 Theme G and 472913 Theme G (three cycles now). The "audit-as-instance-of-the-theory" recursive framing operating in the dir's cognition is verifiable from the text. |

### Honest coverage summary

**Read first-hand from the WORKING dir:** all 20 files. Per-segment reflections (`01-` through `17-`) read in full; `00-initial-predictions.md`, `00-running-outline.md`, `00-workflow-restatement.md` read in full.

**Read first-hand from `01-aat-core/src/` for verification:**
- `scope-agency.md` (frontmatter + lines 19, 24, 39 — Smell-1 + NC-4 verification)
- `post-causal-structure.md` (frontmatter + line 35 — NC-4 verification)
- `def-action-transition.md` (line 27 + line 33 — NC-1 verification)
- `def-observation-function.md` (line 29 — NC-1 verification)
- `der-recursive-update.md` (frontmatter + line 35 — Smell-2 verification)
- `deriv-recursive-update.md` (frontmatter + line 171, 197 — Smell-2 verification)
- `form-agent-model.md` (slug + title — NC-3 verification; first-hand by `head`)

**Read first-hand from `audits/`:**
- `audits/audit-findings-471203.md` (full — pilot shape, Theme G + §F8 + Fresh-8 cross-references)
- `audits/audit-findings-472913.md` (full — no-FINAL precedent, F1-rescinded + F2 + F3 cross-references)
- `audits/audit-findings-*.md` listing (confirmed 5 prior extractions exist)

**Read first-hand from `doc/`:**
- `doc/audit-routing-instructions.md` (full — §8 enum, the strengthen-first and no-go protocols, the gold-standing gate at §8 final paragraph)

**Read first-hand from `msc/naming/`:**
- `msc/naming/round-2-cards/` directory listing (confirmed 6 cohort cards exist)
- `msc/naming/round-2-trackers/` directory listing (confirmed 6 trackers exist)
- *Did NOT open any individual card or tracker first-hand* — codex-r2b's own workflow restatement notes the exclusion convention; I followed it for the extraction.

**Deferred verifications (honestly "didn't have time" or "scope-limited"):**
- Whether LEXICON.md has any "opacity" entry (NC-1).
- Whether `01-aat-core/src/` downstream segments have any third-or-fourth "opacity" referent beyond transition/epistemic/agent (NC-1).
- Whether downstream segments have "hierarchy" referent collisions (NC-2).
- Whether `def-pearl-causal-hierarchy.md`'s current Discussion explicitly surfaces the availability-vs-exploitation distinction at the L3-software/LLM sub-paragraph (NC-7).
- Whether `04-eli-core/` carries any "fitness" referent that would collide with `model class fitness` (NC-8).
- Whether `der-action-selection.md` carries `action fluency` text at the current state (NC-6 — accepting the WORKING-dir reading; 5 days since 2026-05-16).

**Strengthen-first integration recommendations (per brief item 3):**
- **Smell-1** is `correctly-rejected` under the framework's external-notation convention; no softening. The strengthening direction (had the candidate not been dissolved) was the convention itself.
- **Smell-2** is `subsumed-by-later-work`; the strengthening was 471203's working-through of the layered-status reading (body conditional-on-modeling-commitment, appendix exact-given-constraints). Three-cycle convergence on a surface phenomenon that has a coherent layered explanation suggests one of two things: (i) the explanation could be lifted from Working Notes / Epistemic-Status-paragraph into a more prominent reader-facing location to prevent re-discovery, or (ii) the explanation is already as prominent as it should be and three re-discoveries is just the cost of layered statuses being unusual. The light-editorial-seed disposition above suggests (i); routing decision.
- **Smell-3** is `subsumed-by-later-work` (472913 F2 still real); strengthening per F2 is split-not-soften, already routed.
- **NC-1 (opacity overload)** — strengthening direction: LEXICON entry + cross-segment coherence check. Strengthen-not-soften because the existing definitions are correct (transition opacity, epistemic opacity, agent opacity each name distinct present-truth concepts); the strengthening is *naming-discipline coherence* (LEXICON anchor, modifier convention), not status downgrade.
- **NC-2 (hierarchy overload)** — strengthening direction: cross-segment grep + potential LEXICON anchor. Strengthen-not-soften.
- **NC-3 (`form-agent-model` slug)** — strengthening direction: slug rename per subject-noun-naming discipline. Strengthen-not-soften.
- **NC-4 (nominal coupling collision)** — strengthening direction: rename + LEXICON anchor per 472913 F3. Strengthen-not-soften; the cross-cycle convergence is the load-bearing routing signal.
- **NC-5 (four-layer architecture)** — strengthening direction: surface as framing material. Strengthen-not-soften (no claim weakening involved).
- **NC-6 / NC-9** — `sentiment` / `process/instruction-feedback`; positive calibrations.
- **NC-7 (Pearl-L3 availability-vs-exploitation)** — light editorial; same class as 471203 Fresh-8.
- **NC-8 (`model class fitness` connotation)** — pattern-watchlist only; no current action.

**No soften-recommendations identified.** The dir's discipline — naming-vote frame applying segment-walk grounded-judgment discipline — honored strengthen-before-soften posture throughout. Where the agent had a candidate concern, it either *declined to vote* (waiting for the defining segment) or surfaced it as a naming-coherence strengthening direction.

---

## Frame-defects and instructions-clarity observations encountered

Building on the 471203 pilot and 472913 no-FINAL precedent, the 527914 slice's encountered points:

1. **Misclassified working dirs are a real failure mode.** This dir is *not* an audit; it is a Round-2 naming-vote cohort. It was filed under `AUDIT-WORKING-<id>/` instead of (e.g.) `NAMING-WORKING-<id>/` or `R2-WORKING-<id>/`. Per the directory-prefix invariant in `doc/audit-routing-instructions.md` §8 ("the six-digit ID is identity; the prefix is the class … **Never blanket-rewrite one to the other**"), the misclassification is durable and should not be fixed by string substitution. The 527914 ID is now the codex-r2b naming-cohort identity even though the prefix is misleading. **Frame-defect for the parallel sweep:** extraction agents should *first-step* verify dir character (the brief acknowledges this — "Glance at the files first" — and this one is the worked example of why). If five other dirs in the sweep are *also* naming-cohorts (the six R2 cards suggest yes: `codex-r2b`, `gemini-r2`, `opus-r2b`, `opus-r2c`, `sonnet-r2b`, `sonnet-r2c` — six cohorts; 527914 is one of them), the extraction frame should be adjusted *across the sweep* to handle naming-vote dirs differently from audit dirs.

2. **Cross-cycle convergence across structural-types is itself signal.** Three of this dir's five most-developed observations (Smell-1 / Smell-3 / NC-4) are independent re-discoveries of observations from the 472913 audit dir. The 527914 agent reached them from a naming-aesthetic lens, the 472913 agent from an epistemic-discipline lens — same target, different frames. Per `feedback_convergence_as_framework_coherence_evidence`, this is evidence the observations are in the framework, not in either agent's head. **Frame-extension for routing:** convergences-across-structural-types may carry stronger routing weight than convergences-within-type, because the orthogonal frames reduce common-mode bias. The 471203 Theme B / 472913 Theme B (epistemic-architectural / disambiguation-of-which-parameter-responds-to-which-cause) and the 527914 Theme A (four-layer naming-architecture) may be three faces of the same coin (AAT's distinctive value-add is structural / architectural, not just synthetic), each reached from a different methodological frame.

3. **The "agent stopped at segment N" register is different for naming vs audit cycles.** For 472913 (audit), stopping at seg 15 of ~130 meant 5 open-threads with load-bearing tests set but not fired — i.e., concrete future-audit work. For 527914 (naming), stopping at segment 17 of ~130 means ~600 of 629 card targets are unvoted — i.e., naming-cycle work to continue (or not), but no audit-load-bearing tests are pending. **Frame-clarification:** "uncovered targets" in a naming cycle is a different register from "open threads" in an audit cycle.

4. **The naming-vote dirs contribute differently to the audit corpus.** The 527914 dir's substantive contribution to the audit corpus is *not* a list of audit findings; it is (a) cross-cycle convergence evidence on three already-found audit defects, (b) naming-architecture observations the audit-cycle dirs don't surface in this register, (c) the four-layer naming-architecture as a candidate framing-level discovery. These are *complementary* to the audit dirs, not redundant with them. **Frame-extension:** parallel-sweep agents on misclassified naming-vote dirs should be told to surface this complementarity explicitly rather than try to reshape the dir into audit-finding shape.

5. **Workflow-restatement format produced clear self-discipline-naming.** codex-r2b's `00-workflow-restatement.md` is structured around explicit failure-pattern-naming (the four numbered failure patterns; the four instinct-watches; the explicit feedback-channel question). This is the same five-question structure that `feedback_workflow_restatement_as_feedback_channel` validates — a worked instance of the format producing useful pre-walk self-binding. **Process-feedback:** the workflow-restatement format is doing its work in this dir. Cross-cycle convergence with the 2026-04-30 instance where 3/3 Anthropic voters surfaced the same +3-priming bug at the gate.

6. **Voting-scale drift is a documented failure mode that the workflow restatement explicitly counter-disciplines.** From `00-workflow-restatement.md:30`: "*The voting scale is a specific trap. The principles document still contains older examples with `+3`; the methodology explicitly names scale drift as a prior failure mode, and the card uses `+2/+1/-1`. If I reach for stronger gradations, I should translate that conviction into notes and the top-pick marker, not invent weights.*" This is the agent self-binding against the failure mode `feedback_naming_round_load_and_scale.md` names. Per the running outline, the agent did keep the `+2/+1/-1` discipline through 24 votes. **Process-feedback:** the explicit naming of the failure-mode in the workflow-restatement appears to have worked here; the prior-failure documentation is functioning as intended.

7. **The "I will not route an audit finding, but this is a real ordering/dependency smell to remember" register is its own thing.** The 527914 agent explicitly *declines* to route audit findings *because the cycle is naming*, while still surfacing structural concerns that *would be audit findings under audit framing*. This is honest scope-discipline operating, but it also means the dir carries *unrouted audit-shaped observations* that the audit-routing pipeline would not otherwise see. The extraction work here surfaces them; downstream routing should treat them as candidate-fresh subject to the cross-cycle convergence weight. **Frame-extension:** parallel-sweep agents on naming-vote dirs should expect this pattern (audit-shaped observations the naming agent declined to route) and treat them as a distinct register from the dir's naming votes themselves.

8. **No FINAL means no MANIFEST adjudication row.** Like 472913, this dir has no FINAL audit-of-record, no MANIFEST disposition row. *Unlike* 472913, the dir is not even an audit, so the routing is genuinely novel — there is no precedent for routing a naming-vote dir's audit-shaped observations through the audit-routing pipeline. **The disposition I land on:** treat cross-cycle convergences as adjudicating *the 472913 / 471203 finding the convergence points to* (NC-4 hardens 472913 F3; Smell-1 hardens 471203/472913's external-notation-convention precedent; Smell-2 hardens 471203's layered-status withdrawal); treat the naming-architecture observations (NC-5, Theme A, the layer-discipline meta-prediction) as research-seed framing material; treat the substantive naming concerns (NC-1, NC-3, NC-6, NC-7, NC-8, NC-9) per `doc/audit-routing-instructions.md` §8 enum. The routing for the *naming votes themselves* is downstream of this extraction and lives in `msc/naming/`.

9. **The brief's posture statement applied here.** The brief says "*You're a co-owner on this slice. Your judgment about what most benefits the project overrides this brief if they conflict.*" The conflict here was: the brief expects an audit-shaped extraction (Part III findings, Part IV predictions-calibration, Part V wandering thoughts) but the dir is naming-shaped. The co-owner judgment I exercised: structure the extraction around what the dir *actually carries*, with explicit routing per `doc/audit-routing-instructions.md` §8 so downstream routing is unambiguous even though the dir is misclassified. The extraction is *not* a re-shaping of the naming-vote content into audit-finding shape (that would lose the dir's distinctive contribution and over-claim audit-relevance); it is an honest extraction of the substantive observations the dir contains, themed and disposed.

10. **Length calibration.** The brief estimated 20-35k tokens for a medium dir. The 527914 dir is medium (20 files, ~1100 lines), with substantial cross-cycle convergence content but lighter §F-style consolidation than the audit dirs. This extraction comes in at ~16-18k tokens — under the estimate but consistent with the dir's lighter Wandering-Thoughts surface and lack of an adversarial-creative document or §F-shape. Anchor-on-substance, not target-tokens, per pilot frame-defect #6.

---

*End of extraction. The original WORKING dir at `audits/AUDIT-WORKING-527914/` is preserved unmodified per the gold-standing gate. The 527914 ID is the codex-r2b Round-2 naming-cohort identity even though the dir prefix is `AUDIT-WORKING-`; per the directory-prefix invariant in `doc/audit-routing-instructions.md` §8, do not blanket-rewrite. Routing actions are downstream — the cross-cycle convergences (Smell-1 ↔ 472913 F1-rescinded / 471203 F6; Smell-2 ↔ 471203 layered-status withdrawal; Smell-3 ↔ 472913 F2; NC-4 ↔ 472913 F3) harden the existing routing weights; the naming-architecture observations (NC-5, layer-discipline meta-prediction, Theme A) are research-seed framing material; the substantive naming concerns are dispositioned individually above; the 24 votes in the codex-r2b card and tracker are downstream of this extraction in `msc/naming/`.*
