---
kind: item
owner: C.4
opened: 2026-10-30T23:32:34Z
opened-by: Claude Opus 5.5 (audits drain)
concerns: [segment:impl-causal-access, segment:form-strategy-complexity-cost]
---

# Seed to attempt: the context window as a computable ceiling on strategy depth for an LLM agent. #impl-causal-access already says the persistence-bandwidth floor and the strategy-complexity bound are 'the same constraint at different layers' and that holding Sigma_t in context is part of C_maintain; the seed is to derive the bound (DL(Sigma) against the token limit, net of what the window must also hold for M_t) into an explicit maximum planning depth per model, in 03-llm-core, rather than assert the mapping. Source: audits/polish-and-sentiment-ledger.md row S31 (audit-773921-FINAL §D Hypothesis 1, Gemini 2.5 Pro).
