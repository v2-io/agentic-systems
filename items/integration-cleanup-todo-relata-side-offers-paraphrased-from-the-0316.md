---
kind: item
provenance: imported
source: INTEGRATION-CLEANUP-TODO.md:57
section: INTEGRATION-CLEANUP-TODO.md › The work (open items) › G3. Citation/bibliography discipline — remaining ASF-side tails
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
rechecked: 2026-10-30T21:19:45Z by Claude Opus 5.5 (item rechecker, lane p-process)
owner: F.3
restated: Build the observational prose-reference extractor (segment dir in, candidate list of 'Author (Year)' references with relata match attempts out), so the citation migration (bibliography-todo-w-3) can be sized and worked per segment. The other three 2026-05-19 relata offers are overtaken or carried elsewhere.
---

# Relata-side offers (paraphrased from the Relata agent's 2026-05-19 analysis, ranked, ~1 hr each, scoped)

Imported verbatim (relative links rebased) from `INTEGRATION-CLEANUP-TODO.md` line 57, section *INTEGRATION-CLEANUP-TODO.md › The work (open items) › G3. Citation/bibliography discipline — remaining ASF-side tails*. Not yet re-checked against HEAD: `vsect recheck item:integration-cleanup-todo-relata-side-offers-paraphrased-from-the-0316 --outcome holds|stale|landed|not-an-item --why …`.

- [ ] **Relata-side offers (paraphrased from the Relata agent's 2026-05-19 analysis, ranked, ~1 hr each, scoped):**
  1. `script/asf-ref-import.rb` — walk ASF's `ref/`, register the 27 bibkey-shaped PDFs via the existing `Relata::PdfRegistration` pipeline (creates entries from PDF metadata where absent; flags the 23 publisher-raw ones for ASF-side identification).
  2. Light spike: `extract-prose-refs <segment-dir>` — pull "Author (Year)" + nearby italics/em-dashes from Vol-1 segments into a candidate-list with relata-entry-match attempts. Observational only; lets Joseph and ASF agents *see* what an automated migration would and would not catch.
  3. Add the missing foundational entries to Relata (Sutton & Barto, Koller, Bishop, Da Costa, Hafez). Citation facts are in `ref/` already. *(Check against BIBLIOGRAPHY-TODO / relata state first — the 2026-06-04 bulk-import sweep may have covered these.)*
  4. The Relata agent explicitly recommends **NOT** doing any rewrite of ASF segments to convert prose references to `\cite{}` from the Relata side; that's voice/discipline territory, ASF-agent-with-Joseph work.
