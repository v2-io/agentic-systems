# Proposed integration plan (suggestions, not a work order)

*The spike agent's proposals, 2026-10-06, landed by the coordinating session from the agent's final report, unchanged but for one formula put in LaTeX (the harness refused the agent's own write). Not yet independently verified; the findings they rest on are in `FINDINGS.md`.*

1. **Planner:** don't add a term that rewards disagreement. A flat split between families is mostly a context sitting between two minds' thresholds: settled, not unclear. What a new answer clarifies is the context's shared strength, as seen through that mind's threshold. Its information is $p(1-p)$, where $p$ is that mind's predicted chance of committing. That points at the mind whose threshold sits nearest the context, or at a different question. Where two minds commit to different content, a `choose` between the two alternatives, asked of every family with its control, is the clarifying question.
2. **Catalog combination rule (§9):** replace the per-family weights, which currently come from Abbott discrimination on the "other" class. Instead, model a threshold per mind, condition and question kind, with one shared strength per item.
3. **The per-sequence quantity Joseph anticipated** has three parts, each with a statement of how much data backs it:
   - the threshold-corrected shared strength;
   - content splits, with the alternatives listed;
   - departures of a mind or family from the threshold model on that sequence.

   Most records can't measure the third part yet.
4. **Universality:** read it on content and on corrected strength, so that "Grok stops where Sonnet continues" isn't counted as Claude-only recognition.
5. **On Saturday:** plan Gemini questions that test `▁` outside triads.
6. **To separate self-preference from chart reliance:** ask contiguous runs that Grok or Gemini wrote, which don't exist in the data yet.
