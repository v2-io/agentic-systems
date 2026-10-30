---
kind: item
owner: C.1
opened: 2026-10-30T21:26:13Z
opened-by: Claude Opus 5.5 (item rechecker, t1-todo)
concerns: [segment:der-tempo-composition]
---

# #der-tempo-composition is inconsistent about C_coord. The body defines C_coord := T_joint - T_c (line 39, since b1f37c91). Its Working Notes still carry the retired C_coord = sum_i T_i - T_c (line 148, audit gold) and 'equal correction rates give eps* = 0 and C_coord = 0' (line 125), whereas line 59 makes C_coord = 0 require lossless fusion as well as eps* = 0. Make every use match the joint-baseline definition.

Split from TODO.md:498 (the 2026-08-22 impl batch's routed source-segment defects; CHANGELOG 2026-08-22, impl-unity-communication and batch two). Text confirmed unchanged at HEAD by the t1-todo rechecker.
