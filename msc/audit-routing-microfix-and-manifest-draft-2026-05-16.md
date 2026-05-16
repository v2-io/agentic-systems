# Micro-fix diffs + MANIFEST entries — PRE-DECISIONAL DRAFT (durable-write spec)

> **Status: working draft, not applied.** The exact specification of the
> canon/MANIFEST writes the post-gate durable batch will execute. Locks
> nothing in. Per `doc/audit-routing-instructions.md` §4.2/§8, the
> **wording-bearing artifacts here — the two no-go-adjacent canon micro-fix
> replacements (Part 1) and the 742613/613842 MANIFEST entry (Part 2.A) —
> go to a fresh independent confirmer before any durable write** (the
> soften-ghost is a wording-failure class; "I see it clearly" is exactly
> what fails there; the confirmer is the §8 gate / Joseph's agent-fabric
> substitution for the personal checkpoint). Part 2.B (bulk grouped
> graduations) is routine primary-source-verified disposition, authored at
> batch time from the adjudications + the ledger draft §C.

---

## Part 1 — Micro-fix diff specs (canon; no-go-adjacent; gate-bound)

### R1 — `01-aat-core/src/deriv-sector-condition.md:294` (Summary "What Is Derived" table cell)

**Disposition:** doc §6 worked example 1. The no-go is canon and stays
(Cor A.1S.1 + `#deriv-stochastic-non-exit`); the cell's *trailing
project-history clause* is the lone autobiographical-voice straggler the
prior honesty-cleanup missed (it purged the Epistemic-Status sentence and
the Cor A.1S.1 `## Findings` entry — verified clean; this Summary cell is
redundant with those two now-clean loci, *and* the full provenance already
lives correctly in Working Notes:354 + CHANGELOG + the routing tracker, so
the demote loses nothing). **This is a demote of redundant history-voice
from the present-truth surface, not a deletion of the no-go.**

- **BEFORE** (exact):
  `| **Cor A.1S.1: containment dichotomy $P(\tau_R\lt\infty)\in\{0,1\}$, $\alpha$-invariant** | Prop A.1 positive invariance (Model D $= 0$) + a.s. finite exit of a non-degenerate diffusion from a bounded region for any $F$ under A2' (Model S $= 1$); Khasminskii 2012 ch. 3–4 | **Proved** — new exact result; the framework previously held a false *interpolating* non-exit bound here |`
- **AFTER**:
  `| **Cor A.1S.1: containment dichotomy $P(\tau_R\lt\infty)\in\{0,1\}$, $\alpha$-invariant** | Prop A.1 positive invariance (Model D $= 0$) + a.s. finite exit of a non-degenerate diffusion from a bounded region for any $F$ under A2' (Model S $= 1$); Khasminskii 2012 ch. 3–4 | **Proved** — new exact result |`
- Net: delete `; the framework previously held a false *interpolating* non-exit bound here`. Nothing else on the line changes. Lint-check the file after (raw-math discipline; inspect the issue *list*, not the count).

### R2 — `01-aat-core/src/result-sector-persistence-template.md:88` (Epistemic Status, "On (T2) and A2' sub-scoping" paragraph)

**Disposition:** doc §6 worked example 2. **Not a ghost/status case** — the
template is `exact`, was `exact`, stays `exact`. Register-only fix: the
defensive "this is not a weakening" voice (provenance: a Codex
"you-say-it-but-it's-easy-to-miss" clarity request, not a disproved-proof
scar) becomes emphatic reader-orientation that *makes the practical-carry-
forward fact unmissable* and states the substantive reason it isn't a
weakening. Settled form agreed with Joseph this session.

- **BEFORE** (exact, the paragraph's last two sentences):
  `For these, (T2) is *derived* from the update-rule structure under B1 directional fidelity. For sub-scope $\beta$ instantiations (e.g., a team where some sub-agent runs a rule-based update), (T2) must be verified per-instantiation. This is not a weakening — it is the honest sub-scope labeling inherited from #deriv-sector-condition.`
- **AFTER**:
  `For these, (T2) is *derived* from the update-rule structure under B1 directional fidelity. **Important, and easy to miss: this is not what carries forward universally.** For sub-scope $\beta$ instantiations (e.g. a team with a rule-based sub-agent) (T2) is an *empirical precondition, verified per-instantiation*, not derived. That distinction scopes which instantiations satisfy (T2) by which route; it does not touch the template's exactness, which is the conditional "(T1)–(T3) $\Rightarrow$ persistence" — anything satisfying (T2) by either route inherits the exact result.`
- Net: replace the final two sentences as above; frontmatter `status: exact`
  unchanged; no epistemic motion anywhere. Lint-check after.

### F7 — `01-aat-core/OUTLINE.md` `#der-team-persistence` row (829314-core-F7)

**Disposition:** Cluster D, co-owner direct-fix class (one OUTLINE
description cell; segment says per-sub-agent, OUTLINE mis-labels it
"Composite persistence condition"; `#deriv-critical-mass-composition` is the
composite analog). Not a wording-failure-class item (descriptive accuracy,
not no-go-adjacent) — included here for batch completeness; does not require
the §8 gate, but trivially confirmable.

- In the `[#der-team-persistence](src/der-team-persistence.md)` row's
  description cell, change `Composite persistence condition` →
  `Per-sub-agent persistence within a team (composite analog: #deriv-critical-mass-composition)`.
  Whitespace-padding in the OUTLINE table is matched at apply time
  (cell-content replacement, not full-line). While there, sanity-check the
  symmetric `#deriv-critical-mass-composition` row reads as the composite
  analog (it does, per verification — line ~360 "Closed-form composite
  sector-constant…"; no change needed there).

### NOT a micro-fix (recorded so it is not re-introduced)

- `hyp-mismatch-dynamics.md:54` — **no-op.** Already correct in η\*-order
  (`O(η* c_max)`, linear — the F-V1 fix was the η\*-power); differs from
  canonical `deriv-discrete-sector-condition` only in the prefactor, at
  explicit `*Heuristic.*` tier, with a live pointer to the sharper segment.
  The inherited "F-V1 micro-residual" framing is the mischaracterization;
  do not churn a correct segment.
- 738192-F2 line-53 recap nudge — **resolved by SN-3** (`3072667`/`2666eca`);
  not open.

---

## Part 2.A — The #1 wording artifact: 742613 / 613842 MANIFEST entry (verbatim, scrutiny-flagged)

> **Confirmer: this is the artifact prediction #1 names.** Scrutinize for
> any soften-ghost / defensive voice — any "the audit recommended a soften
> but we", "not a weakening", "previously false". The MANIFEST is a history
> layer and *may* state the state-3 disposition flatly + point to the
> canonical loci; it must not defend the ghost. Cascade closure for this
> finding is **verified clean** (routing tracker 2026-05-16 cont.2). Verbatim
> proposed entry:

```
### 2026-05-16 — Cluster B math-heavy ledgered (584721 / 613842 / 742613+SUPPLEMENT / opus-2026-04-21 / audits-2026-04-22-evening / 738192)

Adjudicated 628401; gating dispositions parent-verified primary-source.
Strengthen-before-soften had maximum bite here and the project passed
repeatedly (≈25/30 findings resolved, the majority by strengthening,
several past the audit's ask).

| Finding | Disposition |
|---|---|
| 742613-F2 / 613842-F2 — Model-S P(τ_R<∞) infinite-horizon non-exit object in `deriv-sector-condition` Prop A.1S(iii) + summary segments | **resolved by strengthening-then-no-go** (state 3). Present state: Prop A.1S carries (iii′) fixed-time/stationary tail + (iv) finite-horizon sup-bound; the infinite-horizon object is **Corollary A.1S.1** (exact) — P(τ_R<∞) is exactly {0,1}, 0 under Model D, 1 under Model S, α-invariant — Model-S half proved in `#deriv-stochastic-non-exit`. Downstream cascade verified clean (every dependent consumes the stopped bound / MS-threshold / fixed-time tail; the falsified ever-exit object is propagated nowhere). Spike: `spikes/spike-stochastic-non-exit-strengthening-2026-05-16.md`; CHANGELOG 2026-05-16. 613842-F2 ≡ 742613-F2 — same segment-state; the precise ever-exit-conflation reading governs the dedup. |
| 742613-F1 — score-function sign (`def-mismatch-signal`) | resolved (sign corrected; `def-mismatch-signal.md:34`). |
| 742613-F3/F5/F8, 584721-F-A/F-D/F-B1, opus-2026-04-21 §1–4, 738192-F1/F2 | resolved, the majority **by strengthening** (log-odds uniqueness; π*-first KL + uniqueness theorem; completeness-argument unification; BH-identity + matching lower bound; depends-graph lint clean; P3→Markov proved; opacity/IB strengthenings; `git checkout` scoped-L3 regime in the canonical TST segment, SN-3 landed `3072667`). Per-finding detail: adjudication 628401. |
| 742613-F4 / 613842-F1 — `def-adaptive-tempo status: exact` vs additive-overcount | substance resolved by strengthening (matrix-Loewner canonical, scalar = special case); narrow frontmatter/status residue tracked TODO:395/126 — not a graduation blocker. |
| 742613-F6 residue (Pearl-`do` before declaration) | `duplicate` of 471203 §B F6 ≡ 742613:254 → FORMAT-TODO C12 (existing home; do not double-track). |
| §A/§D, process-feedback, bigger-picture/synthesis | → polish-and-sentiment ledger, consolidated P-block + S-rows (one curated pass; see ledger). opus-2026-04-21 "spike-stronger-than-segment" cross-cutting pattern recorded as the *validated-and-absorbed* empirical ancestor of strengthen-before-soften, not open. |

Ledgers `pending-findings-2026-04-2{1,2,3}.md` read as evidence — **not** graduated (durable infrastructure). Files moved: `audit-584721-FINAL-2026-04-25.md`, `audit-742613-FINAL-2026-04-25.md`, `audit-742613-SUPPLEMENT-PHASE-2-TRIAGE.md`, `audit-613842-FINAL-2026-04-25.md`, `opus-audit-2026-04-21.md`, `audits-2026-04-22-evening.md`, `audit-738192-FINAL.md`.
```

> Self-check against doc §5's forbidden list, stated so the confirmer can
> verify my own: the entry states the disposition flatly ("resolved by
> strengthening-then-no-go (state 3)"), points to the canonical present-truth
> loci (Cor A.1S.1, `#deriv-stochastic-non-exit`), and contains **no** "the
> audit recommended a soften", **no** "not a weakening", **no** "previously
> false/held". The phrase "the precise ever-exit-conflation reading governs
> the dedup" is the doc §8 duplicate-precision rule stated as routing fact,
> not ghost-defense. *The confirmer's job is to find the soften-ghost I
> cannot see from inside, per prediction #1.*

## Part 2.B — Bulk grouped graduations (routine; authored at batch time from adjudications + ledger §C)

Grouped per routing-economy. Per-finding detail lives in the five
`ADJUDICATION-WORKING-{704218,628401,704182,714206,472914}/adjudication.md`
deliverables + the ledger draft §C MANIFEST-routing notes; the durable
MANIFEST entries are authored from those at batch time. Plan:

- **Cluster A — 13 self-disposed extracts** → one dated MANIFEST section,
  all `graduate`, dispositions closure-direction-correct. **A-stale
  `extracted-codex-feedback-2026-04-28` written `resolved` (corrected), NOT
  "Pending".** `bf945f78` non-independence with `extracted-audits-2026-04-22-morning`
  noted (same Opus audit; not independent corroboration). Files #9/#10/#12
  carry provenance notes (primary sources for live CLAUDE.md conventions;
  bridge-spike = research-trail). Soft → ledger S8–S15+ (consolidated).
- **Cluster C — 4 files** → one section; F-V/P-V resolved (5/8 by
  strengthening); SN-3 landed (parent direct-fix, `3072667`); F-V3/F8
  correctly-open, triple-tracked (TODO:95 + SP-21 + ledger — graduate with
  it living there, do not double-track); J1–J10 → ledger S20 (one row);
  portfolio-extract = retained-provenance; lint-state → standing-hygiene
  TODO (not a blocker).
- **Cluster D — 8 files (829314 ×4, 849201 ×4)** → one section; all
  graduation-eligible; opacity-gain ≥3-cycle convergence = the section's
  strengthen-first MANIFEST headline (stated once); 829314-core-F7 = the
  Part-1 OUTLINE micro-fix; no SUPPLEMENT exists for 829314/849201 (stated
  explicitly so a future verifier doesn't hunt one); 193847 ≠ 829314
  (coincidental digit overlap; the encounter tracker is 193847's, not a
  829314 record). Soft → ledger (S17 convergence, S18 sidecar-declined,
  S23/S24 research-seeds, S26 OUTLINE-order).
- **Cluster E — 12 files** → **one grouped entry** for the April-01/02
  consolidation chain (nested-revision lineage) with a shared
  redundancy-table justification (not 13 near-identical per-file
  justifications); the two `extracted-*` = retain-as-history (provenance);
  the lineage-doc embeds Cluster-C findings → de-dup at routing (do not
  double-track from two clusters); `analysis-2026-04-02-synthesis` is a
  curated/raw pair with the deep-reviews extract (not `diff`-duplicates —
  not independent signal). Soft → ledger S16 (one cohort sentiment row),
  S25 (451729 soft set). **`audit-451729-FINAL-2026-05-10` does NOT
  graduate** — stays open on D.1 (TODO §2026-05-10).

The four `pending-findings-2026-04-2{1,2,3,5}.md` and the 19 de-novo
`AUDIT-WORKING-*` "gold" dirs are **not** moved or touched (the latter is a
separate standing gate — consult Joseph).

---

*Inputs: the five cluster `adjudication.md` deliverables + parent
primary-source verification + Model-S cascade-closure verification.
Authoritative process: `doc/audit-routing-instructions.md`. Durable write
deferred to the post-gate batch; Part 1 + Part 2.A go to the §8 confirmer
first.*
