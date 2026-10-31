---
kind: item
owner: C.1
opened: 2026-10-31T02:12:27Z
opened-by: Claude Opus 5.5 (audits drain)
concerns: [segment:scope-continuous-operation, segment:def-system-availability]
---

# TST's continuous-operation extension adds user time and developer time at an unstated 1:1 rate. #def-system-availability:28 ('from the user's perspective, downtime is lost time. The temporal optimality postulate therefore applies to operational time as well as development time') and #scope-continuous-operation:33 (effective time includes P(failure) x T_recovery) sum the two into one objective with no conversion factor, although an hour of downtime for many users and an hour of one developer's time are not the same quantity. One sentence naming the exchange rate as a parameter (with 1:1 as a special case) keeps the scope extension honest and makes the postulate's equivalence precondition checkable. Source: audits/.gem-hunt-trail/GEM-WORKING-849201/adjudication.md A1 (849201 Fresh-9; the gem-hunt's only 'ready' soft item); audits/polish-and-sentiment-ledger.md S41.
