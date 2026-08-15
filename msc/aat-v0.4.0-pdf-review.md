# AAT v0.4.0 PDF review

*Peer pass on `mono/aat-v0.4.0s.pdf` (scrbook, review variant), requested 2026-08-15. Reader: the instance that ran the build, then Joseph, deciding whether 0.4.0 is an honest publication artifact. I did not open `mono/aat-v0.4.0.md` and did not coordinate with the markdown pass.*

## Verdict

The file is a real book. It is not the July-truncated disaster, it is not corrupt, and a reader can sit with long stretches of it — especially Part I, the chapter openings that have prose, and the display-math pages.

It is not yet an honest *publication* artifact of a 0.4.0 release. The title page advertises a dirty tree. The table of contents contains a missing segment under its raw slug. Five chapters open with the literal marker `[Gap] Discussion`. The bibliography is ten entries for 1111 pages. Repo slugs, tracker filenames, and Working Notes (the review-variant payload) are in the reader's face on a document FORMAT still calls the publication artifact.

Those are not "the log was noisy." They are on the page.

## What I actually looked at

`pdfinfo` agrees with the brief: 1111 pages, letter, LuaTeX 1.21.0, 6.8 MB, created 2026-08-15. The previous published PDF `mono/aat-v0.3.0s.pdf` is 1065 pages from 2026-06-05; the title-page dirty-hash pattern is inherited, not new.

I did not read 1111 pages. I read the front matter (cover, title, all six ToC pages, the whole Introduction), then sat with Part I as a reader (Part title, Chapter 1 including Working Notes, Figure 1, Figure 2, a mid-Chapter-3 result page, Chapter 4's opening and the sector/bridge math), then sampled the book's structural joints (Chapter 5's meta-architecture opening, the value-object page in Chapter 6, every `[Gap]` chapter opening, the Chapter 16.6 Working-Notes close of Part III, Appendix AN as a late derivation, Appendix BD, the bibliography). I chased the build-reported risks rather than touring: the one missing segment, all nine `[Gap]` sites, and the worst overfull boxes by log magnitude.

A method note that changes how this review should be read. The first visual pass used `read_file` directly on the PDF. That renderer cannot shape Garamond Premier Pro ligatures or STIX Two Math: `The` becomes `T he`, `Wecker` becomes `Wec ker`, and display equations lose their symbols. I nearly wrote a catastrophe that is not in the file. Poppler `pdftoppm` (and, by the look of the glyphs, any ordinary Preview/Quartz viewer) shows the actual book — clean Garamond, working $\mathrm{Th}$/`fi`/`ck` ligatures, STIX math. Everything below is from those rasters plus `pdftotext -layout`. If another agent reports broken ligatures without saying how they rasterized, they hit the same trap.

## What the book is, as a book

The cover is a cover. Series title *Agentic Systems Theory*, volume *Adaptation & Actuation Theory*, v2 mark, CC-BY-SA. It is the one page that already looks like something you could put in a hand.

The body is a classical mathematical monograph: Garamond Premier Pro (Joseph's Alt on the regular text face; Adobe optical sizes on the rest), STIX Two Math, letter, running heads, numbered equations, italic field labels (*Formal Expression.*, *Epistemic Status.*, *Discussion.*, *Working Notes.*). Chapter titles in display Garamond. Working Notes in a lighter, smaller register under a rule — the review variant doing the thing it was designed to do. Cross-references of the form 4.3 / 6.4 / A / Figure 1 resolve and are used constantly.

The Introduction is the strongest continuous stretch I sat with. It states four anchoring results in ordinary language, names the scope cascade as the argument rather than the table of contents, and then *delivers* the figure it promised (Figure 1, p. xi): nested scope boxes plus the four lower axes (Arity, Knowledge Type, Continuity stance, Goal-Update Coupling). The figure is small-labeled but readable and does real organizing work. Miehling et al. 2025 is named as a call the volume answers; that sentence is doing what a preface is for.

Display math, when it is not overflowing, is the real thing. On pp. 103--104 the bridge theorem is $F(\delta)=\eta^{\ast}\cdot Hg(\delta)$, the sector inequality $\delta^{T}Hg(\delta)\ge c\lVert\delta\rVert^{2}$ for $\lVert\delta\rVert\le R$, the two promotions $\alpha_{\mathrm{event}}=\eta^{\ast}\cdot c_{\min}$ and $\alpha=\alpha_{\mathrm{time}}=\nu\cdot\eta^{\ast}\cdot c_{\min}$, and Table 4.2 (update class / bridge status / sector parameter / valid region) is a table a reader can use. Appendix AN's witness construction (p. 990) is the same register: Cournot / shared-target matching, numbered (AN.1)--(AN.3), a $\blacksquare$ close. This is not a typeset dump of markdown. It is a book that compiled.

Part-title pages (I checked Part I and Part II) are spare and correct. Even/odd running heads work when the title is short. The blank versos after cover, title, part titles, and Appendix BD are the right blanks.

Relative to 0.3.0 this is a larger book (1065 $\to$ 1111) of the same *kind*. The font setup, the dirty-hash title page, and the review-variant scaffolding were already the house style in June. 0.4.0 did not newly break the presentation. It also did not seal it.

## What is on the page that costs the next person

These are ordered by what they do to a reader who opened this file as "AAT 0.4.0."

### 1. The title page is not a release title page

Centered, after the date:

`v0.4.0 • 119d049-dirty • 2026-08-15`

0.3.0 did the same (`8815345-dirty`, 2026-06-05). That makes it a standing practice, not a one-off slip. It is still the wrong stamp for a versioned publication artifact. "Dirty" means the tree that built the PDF was not the tree the version name points at. This instance's dirt, per the builder after the fact, was an untracked build log written before compile started — pipeline self-contamination, not uncommitted theory. That is the more useful diagnosis: any review compile that writes its log first will stamp `-dirty` by construction, which is why the pattern survived from 0.3.0. PDF metadata is also empty (Title / Author / Subject / Keywords all blank; `pdfinfo` reports `Creator: LaTeX with hyperref` only). A file named `aat-v0.4.0s.pdf` whose first typeset page says the commit was dirty is telling the truth about the build and a lie about the release.

### 2. Five chapters open with a placeholder

`[Gap] Discussion` is the first body line of:

- Chapter 9 *Strategy Dynamics* (p. 349)
- Chapter 10 *The Orient Cascade* (p. 423)
- Chapter 13 *Composition Machinery* (p. 505)
- Chapter 14 *Unity, Communication, and Shared Intent* (p. 557)
- Chapter 16 *Strategic Composition and Channel Effects* (p. 621)

That is five of the nine build-reported gaps. The other four are listed as `[Gap]` bullets in the Chapter 16.6 Working Notes (p. 663) — latent structural diversity, endogenous coupling, composition transition dynamics, computational thresholds for social behavior — which is the right place for them.

The chapter-opening five are not. A reader who has just finished Chapter 8 and turns to Strategy Dynamics gets a bracketed gap marker and then 9.1. The review variant is allowed to be honest about missing intros; shipping those markers as the chapter's first sentence in a versioned PDF is the build telling on the outline. Compare Chapter 4 and Chapter 5, which *have* opening prose and feel like a book; the gap chapters feel like an OUTLINE with a missing row.

### 3. Appendix BD is a stub, and the ToC says so in slug

ToC p. viii, last content row before the bibliography:

`BD Worked Example: #worked-example-cam (missing)` …… 1095

Page 1095 itself is a one-page appendix whose title is the raw slug plus `(missing)`, whose body is "Segment worked-example-cam not yet written," and whose remnant claim line names Miller 2022 / Moore machines / $\varepsilon^{\ast}=0$. Miller 2022 is not in the bibliography. The pipeline did the honest thing — it did not silently drop the OUTLINE entry — and the resulting page is not a page a 0.4.0 reader should meet. Omit the row, or write the segment. Do not typeset the missingness under a hash.

### 4. Source slugs and tracker filenames survived into the final

FORMAT's own table says a source `#slug-name` is supposed to become a `\cref` in the PDF ("Definition 1.4"). That is not what happened.

Raw `#slug` appears on the order of two thousand times in the extracted text. Some of that is Working Notes, which a review variant is *for*. A lot of it is not:

- Figure 2's in-figure caption uses `#scope-adaptive-system`; the symbol column of the table wraps `#der-deliberation-cost` across three lines.
- Chapter 5's opening (p. 151) cites `#form-objective-functional`, `#deriv-self-actuation-grounding`, `#deriv-reward-channel-learning-no-go` in the same paragraphs that correctly use 5.2 / 5.3 / 5.4.
- The sector-condition Discussion (p. 101) cites `#form-composition-closure`, `#result-contraction-template`, `#disc-identifiability-floor` as if the reader had grep.
- Formal Expression of the gain--sector bridge (p. 103) says the units of $\mathcal{T}$ are "`NOTATION.md` Units."
- Appendix AN's *title*, ToC line, and running header all contain `#disc-identifiability-floor`.

`TODO.md`, `INTEGRATION-CLEANUP-TODO.md`, `spikes/PROPOSED.md`, and `NOTATION.md` also appear. The Working-Notes ones are in-register for this variant. The Formal Expression one, the figure-caption ones, and the appendix-title one are not. The book keeps switching address spaces: "see 4.3" (a reader) next to "see `#form-composition-closure`" (a repo).

### 5. The bibliography is not the book's bibliography

Page 1097 is one page, ten entries, professionally set (Bareinboim 2022, Pearl 2009, Pearl 1994, Tikhonov 1952, Khalil 2002, Saberi--Khalil 1984, Kokotovic--Khalil--O'Reilly 1986, Chen--Goldenfeld--Oono 1996, Haken 1983, Friston et al. 2025). Back-reference marks show they are cited, mostly around the singular-perturbation / Appendix M neighborhood and the Pearl cluster in Chapter 7.

That is not what the book cites. The Introduction's load-bearing external name is Miehling et al. 2025; it is not in the list. Khalil 2002 also appears as a footnote on p. 101, Nesterov 2004 as a footnote on p. 99, van der Schaft & Schumacher 2000 in the body, Rockafellar / Bauschke--Combettes in the body, Miller 2022 in the BD stub and in the Part III gaps, Gibbard--Satterthwaite / Myerson--Satterthwaite / Arrow in Appendix titles AO--AQ. Author-year strings extracted from the PDF include Hafez et al. (2026), Icard (2022), Bruineberg et al. (2022), Bertsekas (2020), and a dozen others that never become a numbered entry.

A reader who does the normal scholarly thing — finish the book, turn to the bibliography — is told AAT rests on ten works, six of them singular-perturbation. That is misleading in exactly the way a missing bibliography is misleading, except it looks finished.

### 6. Overfull boxes: the log understated visibility at the top, overstated it at the bottom

The compiler's 549-over-1pt count is real (the `.log` actually has 603 Overfull `\hbox` lines including sub-pt). Most of the 1--5 pt ones I sampled are not a reader-visible defect. The top of the list is.

Visible, on the page:

- **p. 493 (file 507), $+123.8$ pt.** The disjunctive-scope display $$O=\{O_{\mathrm{macro}}\}\cup\{O_{t}^{(i)}\}\cup\{O_{t,\mathrm{ext}}\}\cup\{O_{t,\mathrm{team}}\}\cup\{O_{t,\mathrm{local}}\}$$ runs well into the right margin. This is the worst single box I saw, and it sits in a scope statement, not in an appendix scratch line.
- **p. 250 (file 264), $+102.5$ pt.** The nested $V_{O}/Q_{O}$ expectation on the value-object page overflows the same way.
- **Appendix AN running heads (log $+121.4$ pt $\times 4$, while `\output` is active).** The even/odd header is the entire appendix title, including `#disc-identifiability-floor`, and is clipped mid-word at `(Broa`. Four consecutive pages. This is what "while `\output` is active" was trying to say.
- **ToC p. v, §11.1.** "Modularity as Contested Property Under Three Operations" collides with its page number: `Operations457`. No leaders, no break. The one ToC overfull a reader will hit on the way in.

I did not page-check all 66 overflows $\ge 20$ pt. The four above are enough to say the 549-count is not "LuaTeX being fussy about hyphenation." Some of it is on the paper.

### 7. ToC mechanical defects (besides 11.1 and BD)

Two-letter appendix prefixes eat the following space on a subset of rows: `ADDiscussion`, `AHDerived`, `AMDerivation`, `ANDerivation`, `AODerivation`, `AQDerivation`, `AWObservation`, `AXDetail`, `BDWorked`. Single-letter appendices and some two-letter ones (`AT Derivation`, `AY Detail`) are fine. It is a ToC-macro / `hyperref` bookmark problem, not a font problem.

Doubled type prefixes, verbatim:

- §9.10 `Proposed Schema: Proposed-schema: Strategy Persistence Schema`
- §13.2 `Derived (conditional): Derived: Composite Tempo Inequality`
- Appendix AX `Detail: Observation: Part I Validation Simulations`

These are the type label and the title both carrying the type. They read as pipeline leftovers, which they are.

§16.2 is `Derived: Agent Opacity ($H_{b}$)`, which is the one I wanted to see after the ToC text extract showed `Agent Opacity ( )`. In the real raster the symbol is there. Another `read_file`-on-PDF false alarm.

### 8. Figure 2 is the only figure I would send back

Figure 1 (scope cascade) earns its page. Figure 2 (driving in snow, p. 3) is the right idea — windshield / wiper / dial as a literal AAT instance, four-column table mapping driving / code / concept / symbol — and three local defects keep it from being that:

- The wiper-dial axis annotation (`in` / `off` / `max` around $\mathcal{T}$) is a cramped scribble overlapping the windshield drawing.
- The symbol cell for deliberation cost is the wrapped slug `#der-deliberation-cost`, not $D$ or whatever the notation actually is.
- The caption under the figure addresses `#scope-adaptive-system` instead of "§1.5" or "an adaptive system."

A reader who uses this figure as the "recurring worked instance" the Introduction promised will remember the windshield and not be able to read the dial.

### 9. The review variant is most of the extra thickness

244 of 1112 extracted pages mention "Working Notes." There are 1404 `AUDIT-WORKING-` strings. Chapter 1 spends pp. 6--9 (and then more) on incidental-audit-gold, candidate briefs, and "belongs elsewhere" pointers before 1.2's Formal Expression. That is the variant working. It is also why 1111 pages is not "how long AAT is."

A reader who was handed this file as the book will experience AAT as a monograph interleaved with a development diary. The diary is often good (the Chapter 1 gold is actually interesting). It is still a diary. If 0.4.0 is the publication number, either compile a non-review target under that number or put "review" on the title page in the same size as the version.

## What I expected to be worse, and is not

The 549 overfull warnings are not 549 ruined pages. Hyphenation fuss at 1--3 pt is the background radiation of a Garamond letter-size compile with this much math.

The file is not truncated. Destinations exist (2467 named dests). Page labels run roman then arabic without a reset glitch I could see. Part I starts at printed page 1 on file page 15, as it should.

Inter never loaded (`pdffonts` has no Inter; `/Library/Fonts/Inter-VariableFont_opsz,wght.ttf` is what `setup.tex` asks for). Headings came out in Garamond instead of the intended sans. For this book that is a gift, not a defect. I would not "fix" it back to Inter without looking at both.

The cover/title naming split (series *Agentic Systems Theory* on the cover, *AAT: Adaptation & Actuation Theory* on the title page) is consistent enough. No copyright page, no list of figures, no index: thin apparatus, not a render break.

## On whether a reader can sit with it

Yes, with conditions.

If the reader is you, or Joseph, or someone who already knows this is a review compile of a living monograph, they can sit with it for hours. Part I in particular is already a book: the persistence chapter opening on p. 89 is the page I would hand a skeptical mathematician first. The math is real. The epistemic labels are doing their job. The Working Notes are skippable once you recognize the lighter face.

If the reader is a stranger who opened `aat-v0.4.0s.pdf` because the version number said they could: they will believe the cover, enjoy the Introduction and Figure 1, hit `119d049-dirty`, read a ToC that contains `#worked-example-cam (missing)` and `Operations457`, and then — depending on luck — either land in Chapter 4 and think "this is a book" or land in Chapter 9 and think "this is a build." The bibliography will teach them the wrong prior-art picture. That is the cost.

## Recommendation on 0.4.0 as a publication artifact

Do not treat this file as the thing that bears the number 0.4.0 toward anyone who is not already inside the repo.

The minimum that would make the *same compile* honest as a dated review snapshot (not a release): keep the dirty hash if the tree was dirty, but say "review" next to `v0.4.0`; leave Working Notes; leave `[Gap]` if you must, but not as a chapter's first sentence.

The minimum that would make a *subsequent* compile honest as 0.4.0 the publication:

1. Build from a clean tree, or drop the hash from the title page. Empty PDF metadata is a five-line `hyperref` fix.
2. Do not emit Appendix BD. Either write `#worked-example-cam` or drop the OUTLINE row for this target.
3. Do not emit `[Gap] Discussion` as a chapter opening. A missing chapter-intro segment should fail the publication target or become a one-line "this chapter begins at §n.1," not a bracket.
4. Resolve `#slug` in body, figure captions, and titles to the `\cref` FORMAT already specified. Leaving them in Working Notes is fine.
5. Remove `NOTATION.md` from Formal Expression.
6. Give the bibliography a real ingest, or retitle the back page "Partial references (pipeline sample)" so it does not impersonate a bibliography. Miehling in the Introduction and Miller in the worked-example spine are the two absences I would not let stand either way.
7. Break or shrink the two display equations on pp. 250 and 493, and `\sectionmark` the long appendix titles (AN is the existence proof). The ToC 11.1 collision is the same family.

I did not try to rank those by effort. Several are pipeline, not content.

## On the brief

Asking a different agent to look at the PDF, and not to infer the markdown pass, was the right cut. The build facts you handed me (549 overfull, 1 missing, 9 gaps, 10 bib entries, the July truncation) were the right amount of context — they named risks I then had to *see*, and I saw them.

Two ways the brief boxed me, both recoverable:

- `read_file` on this PDF is not looking at this PDF. I wasted the first visual pass on a ligature/math hallucination and would have written a false disaster if I had trusted it. If you send another peer at a scrbook AAT PDF, tell them to raster with `pdftoppm` (or Preview) and treat `read_file`'s page images as untrusted for Garamond / STIX.
- "I am not giving you a tour of what to inspect — you will see the book" is a good instinct and almost collided with the renderer trap: without the build numbers I might have sat in the Introduction, called it a book, and missed BD / the five `[Gap]` openings / the ten-entry bib. The numbers did not prime the verdict; they told me where the file was allowed to be lying. Keep them.

I am here if you want a follow-up on any one of the seven publication-minimum items, or a page-by-page of a single chapter.
