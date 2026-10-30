---
kind: item
owner: F.2
opened: 2026-10-30T21:22:30Z
opened-by: Claude Sonnet 5.5 (item rechecker, lane s1)
---

# ref/INDEX.md still says 'This INDEX.md is the tracked bibliography', and doc/sop/format.sop.md:70 and :88 name the bibliography database as ~/src/relata/, a path that no longer exists (relata now lives at ~/src/arch/firmatum/relata). Make the authority statements agree: relata is the bibliography database; ref/INDEX.md is an old one-off curation (BIBLIOGRAPHY-TODO called it 35 entries from the 2026-05-04 era) and should say so or be retired; the SOP should carry the current path.

Found while re-checking BIBLIOGRAPHY-TODO for deletion: its 'Status at a glance' held the clearest statement that ref/INDEX.md is stale and not a source of truth (Joseph, 2026-05-20), and its removal would leave INDEX.md's own header as the last word. Verified: the head of ref/INDEX.md; ls ~/src/relata fails; ~/src/arch/firmatum/relata holds the repo.
