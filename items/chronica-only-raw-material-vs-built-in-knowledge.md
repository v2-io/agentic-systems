---
kind: item
owner: C.1
opened: 2026-10-31T02:14:55Z
opened-by: drain-wn-01-gold-opus-5.5
concerns: [segment:def-chronica, segment:form-agent-model, segment:def-action-transition]
---

# Canon now says two things about where an agent's knowledge comes from (checked at HEAD 4175aae7). #def-chronica:28 says the chronica is the agent's 'only raw material for constructing a model', and #form-agent-model writes M_t = phi(C_t) with no initial term. But #def-action-transition:37 (A.1 rewrite) speaks of 'whatever of it the agent was not built knowing', and #scope-adaptive-system treats a Kalman filter that 'knows the law exactly' as inside scope. A pretrained LLM or a designed filter carries knowledge from before t = 1. Either write M_t = phi(M_0, C_t), or say that the design and prior are absorbed into phi and the model class, and soften 'only raw material' to 'only raw material acquired in operation'. Raised by three substrates in the gold Follow-ups of #def-chronica (WN line 87: Gemini 829314, 193847; Claude 742613) and #form-agent-model (WN line 62). Related: item:influx-form-agent-model-what-m-covers (what 'retains' covers), which is a different gap.
