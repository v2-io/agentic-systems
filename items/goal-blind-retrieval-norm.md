---
kind: item
owner: C.4
opened: 2026-10-30T23:32:08Z
opened-by: Claude Opus 5.5 (audits drain)
concerns: [segment:disc-m-preservation, segment:der-class-coercion-via-wrapping, segment:scope-multi-agent]
---

# Seed to attempt: goal-blind retrieval as the dual of goal-blind routing. A logogenic agent's retrieval query is written by a goal-conditioned (Class 3) model, so retrieval-augmented reconstruction is goal-conditioned before the forward pass; #disc-m-preservation:55 says only that reconstruction is query-dependent. The goal-blind-routing condition exists at #scope-multi-agent:55; the retrieval-side norm exists only as Working-Note recognition. Derive it from the routing dual and the W0/W1/W2 wrapping hierarchy (#der-class-coercion-via-wrapping): RAG is a bias amplifier unless the query is W1-shielded from the goal. Note today's #der-directed-separation (selection and allocation permitted, distortion forbidden): goal-conditioned retrieval is selection, so the question becomes whether the retrieved set is modelled by the update (allocation) or silently shapes it (distortion in effect). A concrete, testable prediction about a widely deployed pattern. Sources: audits/polish-and-sentiment-ledger.md rows S32 (audit-773921-FINAL §D H2, Gemini) and S40 (gem-hunt 829314 B-1); two independent arrivals; audits/AUDIT-WORKING-471203/68-71-logogenic-agents-sample.md ('RAG is goal-conditioned reconstruction').
