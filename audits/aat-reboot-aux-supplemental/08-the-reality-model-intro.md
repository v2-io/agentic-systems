# aat-reboot aux supplemental — 08 `the-reality-model-intro`

*Written 2026-09-25 by the finder for `01-aat-core/src/the-reality-model-intro.md` (Claude Opus 5.5), for the aat-reboot walkthrough. The coordinator's aux is `~/src/aat-reboot/scratch/aux/08-the-reality-model-intro.md`. Paths are relative to `~/src/arch/asf/`; line numbers are as of `875e1ac3`. Each note carries slug tags so later finders can grep for their own segment.*

## Fact-checks with positive results — please add to the Working Notes of `the-reality-model-intro`

- Checked "the four segments that follow" (:24) against `01-aat-core/OUTLINE.md:36–39`. The same four appear in the same order. Holds.
- Checked "Chapter 4 will use it to derive *structural adaptation necessity*" (:22) against the OUTLINE. `#result-structural-adaptation-necessity` sits in the fourth Part I chapter, "Persistence and Structural Limits" (`01-aat-core/OUTLINE.md:56,68`). Holds.
- Checked the sufficiency gloss (:18: "fraction of the chronica's predictive content that survives"; $S=1$ means nothing lost) against `def-model-sufficiency.md:22,31`. Holds. The intro omits the well-definedness clause (undefined when the chronica predicts nothing) and the conditioning on future actions. That's acceptable for a bridge, but both are exactly what readers ask about (Working Notes §4).
- Checked "anything not in $M_t$ is lost to the agent, by construction" (:24) against `form-agent-model.md:18`. Holds verbatim in substance.
- Checked "Tishby's information bottleneck … we adopt that framing directly" (:18) against `form-information-bottleneck.md:13` ("imports … directly"). Holds.
- Checked "#form-information-bottleneck … characterize[s] optimal compression for an agent whose target is future observations" (:24) against the binding $Y = o_{t+1:\infty} \mid a_{t:\infty}$ (`form-information-bottleneck.md:13`). Holds.
- Checked "the trigger lives in this chapter" (:22) against `def-model-class-fitness.md:14` ("the trigger this definition sets up for use later"). Holds.
- Checked the implicit requirement that there be something to predict against Tishby et al. 1999 (relata markdown :140: "The relevance variable, denoted here by Y, must not be independent from the original signal X, namely they have positive mutual information"). It matches `def-model-sufficiency`'s well-definedness clause. Holds.

## History

- **2026-05-12, `91599699`.** The segment was created inside a rendering commit (the commit body is about table rendering and doesn't mention the intro). This first version had Formal Expression / Epistemic Status / Discussion headers and a sectioned Discussion: "The compression commitment", "Static, but already enough to fail", "What the chapter delivers", and "Pedagogical note on register".
- **2026-05-12, `ebaf24dd`, 23 minutes later.** A full rewrite into the current five-paragraph prose, after Joseph's 17:04 feedback (`~/.claude/history.jsonl:12401`: fourth-wall breaks; "something between patronizing and super-dense noise"). Again the commit body doesn't mention it. `CHANGELOG.md:1464–1483` records the six intros and the format conventions that came out of this: no FE/ES/Discussion headers, no fourth-wall talk, mine the AUDIT reflections.
- 2026-05-15: AAD→AAT rename (`9745397b`, `08b6f409`). 2026-05-22: brace sweep (`f0c46426`). 2026-05-30: gold lift (`c931bccb`), four audit dirs.
- **Where the prompts came from.** `~/.claude/history.jsonl:12372–12373` shows Joseph asked for chapter-opening Discussion segments to render as plain chapter text, then invited the agent to write intros "your pick, within AAD". :12405 suggested mining `msc/AUDIT*` reflections. :12418 set the rule "no claims in prefaces or intro discussions that aren't substantiated or first claimed in an actual claim (segment)".
- **Stale descriptions of the retired framing.** The OUTLINE row (`01-aat-core/OUTLINE.md:35`) and `CHANGELOG.md:1466` still describe it as "static-but-already-enough-to-fail". The phrase left the body in `ebaf24dd`. The 731548 auditor predicted the framing from the OUTLINE row and then "confirmed" it (`AUDIT-WORKING-731548/09-…md:3`), which shows how OUTLINE descriptions prime readers.

## What I left out of the aux, and why

- **IB deterministic-$\phi$ versus stochastic-encoder** (526815 F3; `audits/AUDIT-WORKING-526815/15-chapter-2-checkpoint.md:13`). The Tishby–Zaslavsky citation check and the verifier's $M_0$ warning also belong to the `#form-information-bottleneck` and `#form-agent-model` finders. Aux 04 already relayed the $M_0$ warning.
- **SP-24 umbrella "agent" and the "adaptive system" softening** (Working Notes §2). Aux 00 and the coordinator's MODEL already carry SP-24.
- **The LLM hybrid-$M_t$ gold.** It's already in this segment's Working Notes ("Belongs elsewhere"); the Vol-3 homes are `03-llm-core/src/obs-context-turnover.md` and `disc-m-preservation.md`.
- **The 628417 batch-02 reflection** (`audits/AUDIT-WORKING-628417/batch-02-agency-model.md`) lists this segment but says nothing specific about it.
- **The 374162 batch-02 reflections** (:17) only restate the promissory-note framing. Their paraphrase (:33) silently writes $\mathcal F = \sup_{\phi} S$, the corrected reading of the xxix type issue. That's one more data point that the codomain reading is what readers reconstruct.

## Notes for other segments (slug-tagged)

- `[def-model-class-fitness]` **Ledger xxix (sup over elements) is unrouted**; see the aux. So are (xxxi), the unbound $\varepsilon$, and (xxxii), the unpriced class-transition cost (`audits/AUDIT-WORKING-731548/13-def-model-class-fitness.md:7,11,19`). 731548 also ran the isomorphism test that the Working Notes' Kuhn item (§2) asked for. The analogy "fails at Kuhn's load-bearing feature: incommensurability", because $\mathcal F$ on a fixed task *is* a common metric (:13). The WN still carries Kuhn as a live candidate.
- `[def-model-class-fitness, result-structural-adaptation-necessity, 04-eli-core]` 731548/13:29 applies the class-vs-noise point to welfare monitoring: an infrastructure watching only mismatch misdiagnoses noisy-world agents as ceiling-pinned. That would be "the welfare equivalent of unnecessary surgery". This sharpens the ELI "chronic structural suffering" gold in the class-fitness WN.
- `[result-structural-adaptation-necessity]` **Log-loss identity** (my derivation; it's in the aux's FINDER-OBSERVED). The minimum regret over the class equals $(1-\mathcal F)\, I(\mathcal C_t; o_{t+1:\infty} \mid a_{t:\infty})$ exactly. That would replace the Formal Expression's unsupported "floor determined by $\varepsilon$" (:35) with an identity and remove the alignment assumption in the regret register. Also: step 4 (:42) claims a lower bound *uniform over the class* in the squared-mismatch register, and steps 2–3 don't deliver that. The uniform information gap ($\ge \varepsilon \cdot$ denominator) doesn't transfer to a uniform squared-error gap without a quantitative alignment modulus. Step 1's $\arg\sup$ attainment is already a gold item. **Needs independent verification before anyone lands it.**
- `[persistence-and-limits-intro]` :30 says the seed is "now grown to a derived result", but the result's status is `conditional`. It's the same "no claims in intros beyond what segments hold" pattern.
- `[the-cycle-in-motion-intro, der-recursive-update, der-action-selection]` The first draft of this intro stated that the completeness commitment is what makes `#der-recursive-update` conditional on a definitional choice. The rewrite dropped it. The Ch.3 intro's own Working Note (:65) flags the resulting "derived, not chosen" unconditional reading.
- `[form-information-bottleneck]` **Uncited prior art in relata:**
  - `creutzig-2009-past-future`, the past-future IB. Line ranges are in the aux.
  - `amir-2015-past-future`, the past-future IB *for linear feedback systems*. It's closer to agents that act. There's no markdown yet.
  - `bialek-2000-predictability` / `bialek-1999-predictive` (Bialek–Nemenman–Tishby predictive information). That quantity is `def-model-sufficiency`'s denominator. No markdown yet.

  Also, $\mathcal F$ is Tishby's symbol for the IB free-energy functional (Tishby markdown :64, :118, :245).
- `[form-agent-model]` Richens et al. 2025, "General agents contain world models", is the converse of the $M_t$ postulate. `spikes/PROPOSED.md:36` is the proposed spike; the relata entry has no document (arXiv 2506.01622 per `ref/prior-art-analysis/agentic-systems-landscape-2026-08-22.md:56`).
- `[form-agent-model, def-model-class-fitness, disc-identifiability-floor]` 731548/09:25 names a gap: "$\phi$-misspecification robustness". The theorist can't observe $\phi$ in real agents, yet every Part I result is stated on $M_t = \phi(\mathcal C_t)$. The nearest tracked item, "misspecification cost" (`TODO.md:160,188`), is a different object.
- `[01-aat-core OUTLINE, CHANGELOG]` Stale "static-but-already-enough-to-fail" row descriptions; see History above.
- `[all chapter intros]` `TODO.md:435` (the May-12 chapter-intro fresh-eyes pass) has never been run. The reboot's per-intro finders are de facto doing it; whoever closes it could cite these supplementals.

## Process feedback

- The brief was clear, and the rule that passed checks go to the supplemental kept the aux honest. The one place I hesitated: a *strengthening* that answers a failed check (the log-loss identity) fits neither "failed" nor "passed" exactly. I put it in FINDER-OBSERVED beside the failed check, because the rewrite of :22 depends on it.
- The most valuable source for intent was `~/.claude/history.jsonl` filtered by date, which gave Joseph's exact 2026-05-12 words about these intros. `memorata-search` returns JSON when not on a TTY; `--json | jq` works well.
- `relata show-markdown` can exceed a 30 s tool timeout when the PDF needs OCR (Creutzig took about 3 minutes). Background it and poll `relata prep list`. `richens-2025-general` has no document; I didn't run `relata fetch`, since it writes to the shared store.
- Siblings for Ch.1 may surface the SP-30′ / GA-1 material; the "ceiling = law-representability" link in my aux depends on it.
