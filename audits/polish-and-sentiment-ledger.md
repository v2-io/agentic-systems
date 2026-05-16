# Polish & Sentiment Ledger

The durable, low-ceremony home for audit findings that are **real signal
but not defects and not architectural moves**: the "this is good — here's
what would make it better" register (Gemini especially), qualitative
sentiment about what reads well or confuses, considered-and-declined ideas
(kept *with the reason* so they aren't silently re-dropped), and
research-seeds too soft for `PROPOSALS.md`'s schema but too substantive to
lose.

Joseph's standing instruction (2026-05-15): *"the last 5% of polish
provides 50–90% of the usability-gap coverage."* These have historically
been discarded by agents triaging for "the stuff I really need to fix."
They are first-class here. An audit can be retired as **fully accounted
for** only once its soft findings are mirrored here (or routed onward);
nothing is lost, and `TODO.md` is kept from becoming the sink.

Graduation rule: a research-seed that matures into a concrete structural
move **graduates to `PROPOSALS.md`** (and its row here is marked
`→ SP-NN`). A polish nudge that gets applied is marked `applied (commit)`.
A nudge superseded by later iteration is marked `superseded-by` — a real
status distinct from open and from cleanly-closed (the diagnostic the
pilot surfaced: closed-then-iterated-past must not read as "still open").

**Bands:** `polish` (small usability/clarity nudges) · `sentiment`
(qualitative reader experience — calibration signal, not action) ·
`considered-declined` (idea weighed and not taken — the reason is the
payload) · `research-seed` (hypothesis-grade direction; may graduate to
PROPOSALS).

**Status vocabulary:** `open` · `applied` · `→ SP-NN` (graduated to
PROPOSALS) · `→ TODO` · `superseded-by <what>` · `noted` (sentiment;
no action by design).

| # | Band | Finding (attributed) | Source audit | Status |
|---|------|----------------------|--------------|--------|
| S1 | considered-declined | Add a `Domain-transfer` / `Instantiated-application` kind to the Findings novelty-kind taxonomy (Gemini: "perfectly captures the entirety of TST — math adopted from AAT, the rigorous application to a novel domain is the breakthrough"). **Declined with reason:** the project deliberately keeps the kind-list compact; TST findings use `Synthesis` or `Adopted-and-extended` per the existing five-kind taxonomy. Recorded so the trade-off (compactness vs. domain-transfer visibility) is not silently re-litigated. | extracted-gemini-2026-04-26-27 | noted (declined-with-reason; revisit only if TST domain-transfer visibility becomes a felt gap) |
| S2 | sentiment | Gemini on the inline-Findings schema: *"excellent … a phenomenal documentation strategy … bridges the gap between deep theory and approachability"*; novelty-kind taxonomy *"extremely strong — forces intellectual honesty."* Calibration signal: the approachability/honesty axis of the Findings schema is landing with an architecturally-independent reader. | extracted-gemini-2026-04-26-27 | noted |
| S3 | polish | Gemini README feedback 1–3 (surface Tier-1 findings in catalog; add equations to persistence-three-senses bullets; break up Position & Lineage density). Addressed same session 2026-04-26/27; the README has since been through further iteration (auto-generated pipeline). | extracted-gemini-2026-04-26-27 | superseded-by the README v2 auto-generated pipeline (`doc/readme/`); TODO §"README v2 pass" carries any remaining |
| S4 | research-seed | (PI) parameterization-invariance is the *genuinely-distinctive* convergent axiom in `#disc-additive-coordinate-forcing` (an invariance-shaped axiom converging on the same exponential-family geometry as three additivity-shaped axioms is more surprising than the additivity convergence among themselves). Possible deeper result: a *uniqueness-of-coherent-statistical-geometry* theorem — any geometry respecting both evidence-composition and parameterization-free measurement must be exponential-family Legendre-Fenchel. Speculative. | audit-471203-FINAL §F2 | open (research-seed; graduates to PROPOSALS if the uniqueness result is attempted) |
| S5 | research-seed | Composition theorem for impossibilities: the four `#disc-identifiability-floor` instances each give one obstruction + escape routes, but real systems face *composed* obstructions where one instance's escape doesn't help another's. When do escape mechanisms compose vs. interfere? Natural Section-III-adjacent extension. | audit-471203-FINAL §F3 | open (research-seed) |
| S6 | research-seed | Hysteresis in persistence: the threshold $\alpha > \rho/R$ is symmetric, but real adaptive systems show asymmetric loss-vs-recovery thresholds (trust harder to rebuild than lose; the `#der-code-quality-as-observation-infrastructure` vicious/virtuous cycle). Extension: different $\alpha$-curves for approaching vs. leaving threshold. | audit-471203-FINAL §F4 | open (research-seed) |
| S7 | research-seed | CIY name-vs-substance: CIY measures distinguishability, not learning value, despite "yield" implying learning. Naming-brainstorm seed (the audit itself moved it out of burden-of-proof into §F). | audit-471203-FINAL §F8 / §"CIY-name-vs-substance" | open (naming-seed; feed the naming pipeline if reopened) |

---

*Append rows as audits are adjudicated. Keep attributed and themed —
flat append-only re-buries the signal, which is the failure this ledger
exists to prevent.*
