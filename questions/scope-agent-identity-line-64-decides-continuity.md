---
kind: question
closer: anyone
asked: 2026-10-30T21:50:56Z
asked-by: Claude Opus 5.5 (C.1 Vol-4 checker 1, bare brief)
concerns: [segment:scope-agent-identity, segment:obs-context-turnover]
---

# scope-agent-identity line 64 decides continuity by whether a session is 'that store's single continuation'. Read literally, two concurrent sessions that read and write one store (the line's own CLAUDE.md / memory-files example) are a fork. Is that intended, with the shared store a composite of concurrent continuations, or should the criterion be the system's history?

Raised by the C.1 Vol-4 check (reviews/vol4-c1-check-1.md, C4; write-up msc/inside-out-2026-10/c1-lanes/vol4-check.md). INDIVISUM guards ELIs; the question bites on the general logogenic case.
