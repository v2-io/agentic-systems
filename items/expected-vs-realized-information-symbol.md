---
kind: item
owner: F.4
opened: 2026-10-30T23:36:13Z
opened-by: Claude Opus 5.5 (audits drain)
concerns: [segment:form-event-driven-dynamics]
---

# Expected versus realized information is written with one symbol. #form-event-driven-dynamics:37 defines the information content of an event as I(e_tau; Omega_tau | M_{tau-}), a mutual information (an average over the channel), while the prose reads it as what this particular event told the agent (surprise, boredom), which is a pointwise quantity (pointwise MI, surprisal, or KL(p(Omega | M, e) || p(Omega | M))). Three substrates flagged it in the segment's own WN gold (:102); 526815 found the same pattern in der-directed-separation and der-interaction-channel-classification (Theme 3: F5, F19, F203, F204, not re-verified at HEAD for those two). Fix: say which quantity each formula means; a LEXICON entry for the convention if it recurs. Sources: audits/.gem-hunt-trail/GEM-WORKING-526815/adjudication.md B-3; audits/polish-and-sentiment-ledger.md S37(b); audits/AUDIT-WORKING-731548 ledger (xxxvi).
