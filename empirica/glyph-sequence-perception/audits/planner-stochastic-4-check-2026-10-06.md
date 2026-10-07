# Check: planner stochastic-4's fixes against its audit

*2026-10-06, about 19:20–19:50. Claude Opus 5.5, the author of `planner-stochastic-4-2026-10-06.md`. Not de novo: I checked commit `3b60e765` against my own findings, and against the coordinator's account of what it did with each one. Written for the coordinator before the restart, and for Joseph.*

*What I read and ran.* The code diff of `3b60e765`: `catalog/given_walk.py`, `priority/plan.py`, `catalog/build.py`, `report/given.py`, `report/view.py`, and the changed lines of `CATALOG.md` and `METHODOLOGY.md`. I then ran three things, all from the shared scratchpad:

- **Dry plans.** The committed planner and stochastic-3, in-process, on the same answers (321,371 records, read at about 19:25), for the same three dummy round ids as before. Nothing was written in the study, and bytecode writing was off.
- **Classifier probes.** The revised classifier on hand-picked runs, pairs and sets.
- **Catalog queries.** The current build, `b20261006_190641`.

*The seal.* As before, I read no `choose` or `names` answers.

Labels: **[measured]**, **[checked]** against the code, **[reasoned]**.

## The short answer

**I see nothing that should hold the restart.**

- **G1, G2, G3, G6 and G8 do what the audit asked.** In the dry plans, questions serving a given sequence fell from 36, 16 and 23 a round to 2, 6 and 4. Dress runs and walks that change dress are asked about as often as under stochastic-3. Lookalike still asks given walks.
- **G5.** Recording the planner boundary is enough for the restart, in my view.

**G4 went one step too far.** "Windows in any alphabet" makes gapped Latin runs given: `a b d`, `p r s`, `u w y`, `a e i o u`, and pairs `b d`, `H K`. That undoes the rule that a skipped position is information.

- It isn't needed for the case it was meant to fix. With locale IDs collapsed, Russian ties Serbian at the top, so `абвгде` is already a window in a top alphabet.
- Its present cost is small: 5 catalog records (none recognised), and about one plan question in three rounds.
- I'd restrict windows to the top alphabets too, soon, but it needn't block the restart.

**Two smaller things:**

- For asked sets, the factor now reads the set in code-point order.
- The first plan after a restart takes about two minutes.

## Each finding against the fix

| finding | fix | check |
|---|---|---|
| G1 dress runs and dress-changing walks counted as given | `is_given`: one dress, kinds window / rotated / stride / reflection; the relation is kept on the record | **resolved** [checked, measured]. Related-but-not-given questions per dry round: 23, 17, 8 under stochastic-3; 19, 9, 21 now. They are no longer turned away. The catalog has 443 such records (50 recognised), now on `CATALOG-VIEW.md` |
| G2 factor followed the glyphs | `served=claim` for claims of 3+ glyphs, else the glyphs | **resolved** [measured]. Questions serving a given sequence: 36, 16, 23 → 2, 6, 4. Skip tests on given sequences: 2, 4, 1 → 1, 2, 0 |
| G3 sets sorted by the wrong index | sorted by the index in each candidate given | **resolved** [measured]: `{x,y,z}`, `{f,g,h}`, `{ъ,ы,ь}`, Fraktur J–Q and `عظغ` are now given sets. One gap remains: see N2 |
| G4 alphabet choice counted locale IDs | locale IDs collapsed; windows and rotations in any alphabet; strides and reflections in the top ones; pairs only as windows | **resolved, then overshot**: see N1. `абвгде` and `клмн` are given; `a z` and `0 9` no longer are |
| G5 control rates shift with the asked mix | the manifest records `planners`: rounds per planner | **enough for now** [reasoned]. The current manifest shows stochastic-3 at c106–c112. The relation is on every record, and a shuffled control's run is in its `source.of`, so a later build can stratify old data too. Nothing computes CATALOG §14's test 2 yet; whatever does should split at this boundary or stratify |
| G6 lookalike lost its known-answer cases | exempt | **resolved** [measured]: 5, 4, 5 lookalike questions on given walks per dry round, the same as stochastic-3 |
| G8 provenance and documents | `plan.json` hashes `givens.json` and `given_walk.py`; the manifest hashes `links.py`, `order.py`, `given_walk.py`; CATALOG header, §11, §13 and METHODOLOGY §5 updated | **resolved** [checked]. Size bound, sparse value-line pairs (`½ ⅗` is still a window) and the Roman symbol order are left, as stated; the last is noted on the page |

**The residue.** What remains as "own glyphs walk a given" is 23, 23 and 17 questions a round (3–4%, against 8–9% under stochastic-3) [measured]. That is the stated design:

- given windows inside sequences that aren't given, e.g. `ЖЗИЙ` inside the chart walk `ЏАБВГДЕЁЖЗИЙ`;
- explore pairs kept at 0.1;
- two-glyph kernels.

**Sizes** match within one question: 891/890, 700/700, 795/795 [measured].

## N1. Windows in any alphabet make gaps given

**The cause.** About 400 alphabets now qualify for windows, and many Latin ones leave letters out. So a run that skips a letter of the usual alphabet is often a window somewhere [measured]:

| run | given as a window in |
|---|---|
| `a b d`, `b d` | Northern Sotho (`nso`) |
| `p r s`, `v w y`, `P R S` | Asu, Taita, Gusii and others |
| `u w y` | Tswana |
| `a c e`, `a c` | Makhuwa (`vmw`) |
| `a e i o u`, `H K` | Hawaiian |

The module's own docstring says a run that skips a position isn't given, *"and that gap is information"*. Under the old top-only rule, none of these were given.

**What it costs now** [measured]:

- 5 catalog records are given walks only through an alphabet that isn't a top one, none recognised: `PRSTUVWXYZ`, `aeiou`, `ÄÖÜ`, and two Mathematical sans-serif runs that skip Q. They have moved from `CATALOG-VIEW.md` to `CATALOG-GIVEN.md`.
- In three dry rounds, one plan question was weighted down only because of this: the left end of the two-glyph kernel `H K`, via Hawaiian. That kernel is just what Joseph's "extend it left and right" priority is for.

**The fix is cheap** [measured]. Restrict windows and rotations to the top alphabets as well, with locale IDs collapsed and ties kept, which the commit already does for strides. That alone recovers the Russian case: for `а`–`е` and `к`–`н`, Russian (`ce`, `ru`) ties Serbian (`bs`, `sr`) at 2 languages, and `абвгде` is a window in Russian's. It doesn't recover `ابتث`. The coordinator already noted that one as a gap in the sources.

**A related point on strides and ties.** In scripts where every alphabet has one language, "the top alphabets" means all of them; Arabic has 20 tied. So the stride restriction protects nothing there. That is how `ابتث` comes out given, as a stride in Pashto's alphabet. The current catalog has no other Arabic-script stride.

## N2. Asked sets are tested in code-point order

**The cause.** In `set_cands`, every unit now passes `served=claim`. For a set from a run, the claim is the run, which is right. For an asked set, though, the claim is `sorted(key)`, the set in code-point order. So it is classified as an ordered run, not as a set, and G3's fix doesn't reach it.

**Where it misses.** Sets whose code-point order differs from their alphabet's order [measured]:

- `{ρ, σ, ς, τ}` is given as a set, but not as `ρςστ`;
- `{𝑓, 𝑔, ℎ, 𝑖}` is given as a set, but not as `ℎ𝑓𝑔𝑖`. `ℎ` fills a hole of the Mathematical italic letters from Letterlike Symbols, so it sorts first.

**The cost** is tiny, because asked sets weigh 0.01. Order-only seeds (`type: set`) are classified in their author's order the same way.

**The fix.** Pass `served` only where the claim is a run: walks, runs some mind called coherent, and ordered seeds.

## N3. The first plan after a restart is slow

The first dry plan took 127 s; the next ones about 40 s. stochastic-3 takes about 39 s [measured]. The difference is the set rule warming its cache: it classifies each set once per candidate given, a few hundred for Latin.

The cache persists in the loop, so only the first round after a restart pays this. It's worth knowing so a slow first round isn't read as a hang.

## N4. The read-offs are already live

`run.py` runs the catalog build, `view.py` and `given.py` as subprocesses, so they use whatever code is on disk. The build `b20261006_190641` and round c112's commit (19:08) already carry the revised given rule: `given_walk` on records, and the new split between `CATALOG-VIEW.md` and `CATALOG-GIVEN.md`. That happened before the fix commit and before this check [checked]. Only the planner waits for the restart.

I found no harm in it. But "not live until audited" holds only for what the loop imports, and that is worth knowing for the next change.

## What I didn't do

- I didn't patch or test the N1 or N2 fixes.
- I didn't check the CATALOG and METHODOLOGY wording beyond what the diff shows.
- I didn't recompute the control-rate split on the new build.
