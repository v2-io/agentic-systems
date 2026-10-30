---
kind: item
owner: G.2
opened: 2026-10-30T23:26:34Z
opened-by: drain-influx-2
concerns: [segment:obs-context-turnover, segment:def-chronica]
---

# #obs-context-turnover lacks a turnover carve that shipping systems now force. Canon already has the intra-session analog (line 78, 'Context window as finite in-context record'); what it lacks: (a) a three-way carve of session turnover, epoch turnover (compaction: the window rebuilt mid-session from a summary) and rendered-view turnover (a per-request projection over a kept record); (b) that f_init is multi-authored (harness template, a summarizer model, the provider) and in some products opaque to the agent and user (encrypted compaction items; provider-held conversation state); (c) that E_ext now includes server-held state the user cannot read; (d) a definitional question for #def-chronica: is sealed, provider-readable reasoning part of C_t? 'Compaction' is the 2026 product and API term (11+ vendor groups), with zero hits in canon (F.1 naming question). The segment's line 93 leaves f_init deliberately unformalized; this is the empirical layer it needs, at tier empirical with the basis named (wire, source, docs). Sources: ~/src/agent-core/anatomy-of-an-agent/README.md §2.4, §7.6, §8.3 (2026-10-21; it misreads canon as covering only session boundaries, so cite the carve, not the misreading); harness-velocity's compaction records; the context-saliency notes (~/src/arch/msc/context-saliency/). Relayed in influx-scout/agent-core-rest.md §2.A points 1, 5, 6. Built partly from Joseph's transcripts: carry no session measurements.
