# LaTeX Templates for Large, Complex Monographs

**A Ranked Survey of Aesthetics, Usability, and Community Sentiment**
*Focus: math, philosophy, AI, and CS · Compiled May 2026*

---

## Executive summary

After surveying ~25 templates across publisher classes (Springer, AMS, Cambridge, Oxford, MIT Press, Princeton, Elsevier, World Scientific, Wiley, De Gruyter, ACM/IEEE) and community/aesthetic classes (`memoir`, KOMA-Script `scrbook`, `classicthesis`, ArsClassica, `tufte-book`, `kaobook`, Legrand Orange, ElegantBook, Dissertate, PhDThesisLaTeX), three patterns emerge:

1. **For a large, complex monograph you author yourself, the two strongest foundations are `memoir` and KOMA-Script `scrbook`** — they sit one level below opinionated visual templates and provide the structural machinery (front/main/backmatter, multi-part hierarchy, indexing, theorem hooks, customization surfaces) that long books actually need.
2. **The most-loved "aesthetic" templates (`classicthesis`, `tufte-book`, `kaobook`) carry hidden costs that scale poorly with monograph size** — broken XeLaTeX support, no-bold typography that fights math/CS notation, redefined macros that conflict with packages, or dormant maintenance.
3. **Publisher templates are mostly contractual scaffolds, not finished aesthetics.** Springer, Wiley, OUP, PUP, Elsevier, and De Gruyter re-typeset author files. Authors who care about final appearance either work with a press that accepts camera-ready PDFs (MIT Press has done it; Cambridge sometimes) or stay with AMS, where `amsbook` is the closest thing to "what you write is what's printed."

The ranking below is **for the use case you described** — a large, complex monograph by an author who cares about both typography and ergonomics. It is not a ranking of templates in general.

---

## Tier 1 — Best foundations for a self-authored monograph

### 1. KOMA-Script `scrbook` ★★★★★

- **What it is**: Markus Kohm's complete European-typography book class; not derived from `book.cls` — its own infrastructure. Current version **3.49**, documentation refreshed November 2025, PDF/UA tagging in progress. ([KOMA-Script CTAN](https://ctan.org/pkg/koma-script))
- **Aesthetics**: Tschichold-style DIV/BCOR canonical page construction, neutral defaults (Latin Modern), proportionally scaled headings, clean running heads. The visual language is "quietly correct" — perfect when you intend to dress it up yourself.
- **Why it wins for large books**: Every layout decision is exposed as a key–value option; the manual is 550+ pages but searchable; bibliography works equally well with `biblatex+biber` or `natbib`; `amsthm` integrates without fights; `scrhack` patches the few third-party-package edge cases.
- **Sentiment**:
  - *"I strongly recommend `scrbook`. That book class offers a huge amount of features for customization: if you need to adjust something in the layout, most of the times you just need to set an option. With the more than 20-year-old `book` class, you are backwards compatible to 1993 but often you need to *program* changes instead of setting options."* — [latex.org forum, 2016](https://latex.org/forum/viewtopic.php?t=27511)
  - The Packt *LaTeX Cookbook* picks `scrbook` as its default book class: *"it is ready for two-sided printing with meaningful margins and good proportions of headings and text."* ([Packt](https://subscription.packtpub.com/book/business-and-other/9781835080320/1/ch01lvl1sec05/designing-a-book))
  - *"I highly recommend to use the book class of Koma-Script for a dissertation."* — Alexander Fabisch ([blog](http://alexanderfabisch.github.io/latex-for-dissertations.html))
- **Caveats**: Some find the key=value syntax disorienting vs. classic LaTeX options ([r/LaTeX, 2024](https://www.reddit.com/r/LaTeX/comments/1hpypkg/memoir_class_vs_komascript_class/)). Internal differences from `book.cls` occasionally surface with packages that test `\if@twoside`.

### 2. `memoir` ★★★★★

- **What it is**: Peter Wilson's purpose-built monograph class (now maintained by Lars Madsen). v**3.8.4b**, November 2025. ([memoir CTAN](https://ctan.org/pkg/memoir))
- **Aesthetics**: Intentionally neutral defaults plus a buffet of built-in chapter styles (plain, Bjarne, Bjornstrup, Ruled, PetersLove, VZ series). The 600+ page `memman.pdf` is itself typeset in `memoir` — a live demo.
- **Why it wins for large books**: It absorbs the functionality of ~30 popular packages (geometry, fancyhdr, tocloft, caption, abstract, appendix, etc.) into the class itself, dramatically simplifying preambles. Native multi-index support, configurable epigraphs, anonymous breaks, comparison-mode draft tools — every machinery a long book needs.
- **Sentiment**:
  - *"If you're serious about this, use the `memoir` class, which will provide likely anything you could want in terms of typesetting facilities."* — [r/LaTeX, 2020](https://www.reddit.com/r/LaTeX/comments/jmb9j1/book_writing/)
  - *"This is the LaTeX class I use for everything. It is highly customizable, relatively easy to use, and ideally suited to book production. It has been around for a long time, is well-maintained, has a fantastic (albeit long) manual, and boasts a large user community."* — [kmhalpern.com](https://kmhalpern.com/tag/memoir-class/)
  - *"From my experience with memoir, the author has clear cut opinions about how things should be laid out in a book and openly (and rightfully) criticises university thesis guidelines that are truly ugly."* — [r/LaTeX, 2024](https://www.reddit.com/r/LaTeX/comments/1e84ejh/is_it_morally_acceptable_to_modify_templates/)
- **Caveats**: The manual literally has a chapter (Ch. 19) titled "For package users" cataloging known incompatibilities. *"Memoir and revtex4 may give a lot of troubles when we try to customize stuff."* ([latex.org, 2017](https://latex.org/forum/viewtopic.php?t=30680)). Some Koma users describe migration friction in both directions ([r/LaTeX, 2024](https://www.reddit.com/r/LaTeX/comments/1hpypkg/memoir_class_vs_komascript_class/)).

**`scrbook` vs `memoir` — how to choose**: `scrbook` if you want modern, conservatively typeset defaults and don't mind reading German-leaning documentation; `memoir` if you want maximum built-in flexibility and an English-first manual that doubles as a typography textbook. Both are equally capable for any of the four domains you mentioned.

---

## Tier 2 — Strong opinionated templates (with one big tradeoff each)

### 3. `kaobook` (Federico Marotta) ★★★★☆

- **What it is**: A Tufte-flavored monograph layout built on top of `scrbook`. 979 GitHub stars, 198 forks. Latest tagged release v0.9.7 (June 2021); issues/PRs continue. ([fmarotta/kaobook](https://github.com/fmarotta/kaobook))
- **Aesthetics**: The most sophisticated synthesis available — wide sidenote margin like Tufte, structural rigor of KOMA, margin TOC, margin citations via `sidenotesplus`, `tcolorbox`-based theorem environments, and `\pagelayout{}` to switch between wide-margin and narrow-margin layouts *within the same document*.
- **Why it works for monographs**: Inherits scrbook's full hierarchy and KOMA's customization. `biblatex`+`biber` integrated by default with margin sidenote citations — a uniquely useful feature for annotated technical books.
- **Sentiment**:
  - *"I find the kaobook class very nice and complete, and the layout seems to open up a lot of options for integrating a lot of visual information, supplementary texts, etc."* — [r/LaTeX, 2022](https://www.reddit.com/r/LaTeX/comments/xewwic/advice_on_writing_a_book_on_classes_kaobook_and/)
  - *"Kaobook looks the nicest but tufte is also popular."* — [r/LaTeX, 2020](https://www.reddit.com/r/LaTeX/comments/jmb9j1/book_writing/)
- **The catch**: *"Be aware that the author of that package re-defines quite a bunch of standard LaTeX macros which could result in some incompatibilities with other packages. The document class itself is placed on top of KOMA-Script's scrbook class, so for personal adjustments you might need to look into KOMA-Script's documentations, as well."* — [r/LaTeX, 2022](https://www.reddit.com/r/LaTeX/comments/xewwic/advice_on_writing_a_book_on_classes_kaobook_and/). Also requires `texlive-full`-class installs ([latex.org, 2020](https://latex.org/forum/viewtopic.php?t=33560)). The 2021 last-tagged-release is the wobble: power users track master on GitHub.

### 4. `classicthesis` (André Miede) ★★★★☆ for philosophy, ★★☆☆☆ for math/AI/CS

- **What it is**: A style package (over `scrbook`) implementing Robert Bringhurst's *Elements of Typographic Style*. Stable since ~2018; a [Typst port appeared January 2026](https://typst.app/universe/package/classicthesis/).
- **Aesthetics**: Palatino (URW Palladio) with optional AMS Euler math, **no bold fonts anywhere**, letterspaced small caps for emphasis, a thin gray sidebar rule, and no dotted leaders in the TOC. *"Is your reader interested in the page number or does she want to sum the numbers up?"* ([classicthesis manual](https://cs.au.dk/~bouvin/thesis/ClassicThesis.pdf))
- **Sentiment**:
  - Praise: *"A lot of thought has gone into the age old art of typesetting and typography. I therefore looked for a good LaTeX thesis template and finally found the classicthesis package by André Miede."* — [Benjamin Hopfer, 2014](https://benjaminhopfer.com/non-programming/2014/04/10/typesetting-my-masters-thesis-latex.html)
  - Critique (math context): the Palatino+Euler pairing famously divides mathematicians. From [r/math, 2021](https://www.reddit.com/r/math/comments/kqy1sc/typefaces_for_mathematics_books/): *"I prefer the combination of Palatino with AMS Euler: I don't think Computer Modern is a good match for Euler."* Counter-camps find Euler's upright math style clashing with their amsmath habits.
  - Practical: older versions had pdflatex hangs on documents with 5+ chapters ([latex.org, 2014](https://latex.org/forum/viewtopic.php?t=24979)).
- **Why the split rating**: For philosophy/humanities monographs the aesthetic is exceptional. For math, AI, CS — where bold matrices, bold theorem heads, and conventional italic math are part of the reading contract — the no-bold rule and Euler quirks create friction in every chapter.

### 5. AMS `amsbook` ★★★★☆ (within math)

- **What it is**: The American Mathematical Society's monograph class. Version **2.20.6**, frozen 2020-05-29 to preserve four decades of consistent AMS production aesthetics. ([amsbook CTAN](https://ctan.org/pkg/amsbook))
- **Aesthetics**: Computer Modern throughout, scshape theorem headings, centered chapter numbers in "CHAPTER III" style, two-column index. The HoTT book famously used `mathpazo` instead of CM with `\linespread{1.05}` (*"Palatino looks better with this"*) — illustrating a common author response to amsbook's defaults.
- **Sentiment**:
  - Pro: *"Where cmr absolutely excels is the accompanying greek, math symbols and typesetting. Nothing else comes even close in getting it readable, pleasing and uniform."* — [HN, 2021](https://news.ycombinator.com/item?id=27918190)
  - Con: *"I think that standard table of contents in amsbook looks quite ugly"* — [r/LaTeX, 2022](https://www.reddit.com/r/LaTeX/comments/vkp6w7/better_table_of_contents_in_amsbook/). The response: *"Just be sure you're not planning to submit it to anything related to the AMS if you're going to be changing that stuff; they set their format the way they intend it to be used."*
  - Igor Pak's broader systemic critique: *"math journals treat the authors like a pesky annoyance, sort of the way a local electric company treats its customers."* ([igorpak.wordpress.com](https://igorpak.wordpress.com/tag/mathematics-journals/))
- **When it's the right answer**: AMS-published monographs (Graduate Studies in Mathematics, Mathematical Surveys and Monographs, etc.), or self-publishing where CM is acceptable. Best paired with `amsthm`, `thmtools`, `imakeidx`. Note `index.sty` is incompatible due to `\@starttoc` redefinition.

---

## Tier 3 — Useful in narrow contexts

### 6. Springer `svmono` ★★★☆☆ (contractually) / ★★☆☆☆ (otherwise)

- **What it is**: Springer's house monograph class, distributed via author portal and Overleaf (template last refreshed mid-2025).
- **Pain points**: Fixed at **10pt only** — `11pt`/`12pt` options are explicitly ignored. **biblatex breaks** when `newfloat` is also loaded under XeLaTeX/LuaLaTeX (*"Package biblatex Error: Patching `\addtocontents` failed"* — [LaTeX.org, 2019](https://latex.org/forum/viewtopic.php?t=32737)). And Springer's own typesetters notoriously *undo* careful camera-ready work: *"Extra ugly is how the vertical rules have gaps in them and some cells are not completely colored… By unnecessarily reformatting all tables, Springer editors did the **complete opposite** of their own guidelines."* — [Simmo Saan, 2024](https://sim642.eu/blog/2024/07/21/springer-anti-typesetters-part-1/).
- **Verdict**: Use only if Springer has the contract. Even then, set expectations: their production team will rewrite tables, possibly lowercase tool names, and change citation formats. The same user who hit the biblatex bug noted *"Springer rejects my e-mails on the SMTP level."*

### 7. Cambridge `cambridge7A.cls` ★★★☆☆

- **What it is**: CUP's authored-book class, v3.00 gamma, last public update **2011**, distributed via AuthorNet.
- **Strengths**: Clean Times-family default (via `txfonts`), proper `\frontmatter`/`\mainmatter`/`\backmatter`, exercise environments, multi-index support, chapter-level reference machinery.
- **Pain points**: `10pt`/`11pt`/`12pt` options must NOT be used (the class sets its own measure); `index.sty` incompatible (same `\@starttoc` issue as AMS); `txfonts` requires `amsthm` to load first. Limited community discussion suggests most CUP authors use it without help — or without knowing community help exists.
- **Verdict**: A respectable default for CUP-contracted math/CS/philosophy monographs. CUP re-typesets, so this is structural, not final.

### 8. MIT Press `newmath.cls` ★★★☆☆ — with an interesting precedent

- **What it is**: Amy Hendrickson's MIT Press book class, dated ~2016.
- **Notable**: MIT Press has accepted **author-controlled camera-ready PDFs** built in `tufte-book` + LuaLaTeX (the *Algorithms for Decision Making* textbook by Kochenderfer et al., 2022). Author Tim Wheeler describes it as *"very uncommon"* but real ([blog, 2018](https://timallanwheeler.com/blog/2018/10/22/how-we-wrote-a-textbook/)). For an interdisciplinary AI/cognitive-science/philosophy-of-mind monograph headed for MIT Press, this is the path to negotiate.

### 9. ElegantBook ★★★☆☆

- 2,300 GitHub stars, last major commit December 2022. Pre-built color-coded theorem environments make it genuinely useful for math course notes / textbooks. The colored-box aesthetic is divisive at monograph length — it reads "textbook," not "treatise."

### 10. Legrand Orange Book ★★★☆☆

- Visually striking commercial-textbook look (orange accents, part pages, sidebar boxes). Last meaningful update 2016. License is CC BY-NC-SA 3.0, which can complicate institutional submissions. Good for self-published CS/AI textbooks where visual distinctiveness matters; wrong tool for a traditional academic monograph.

---

## Tier 4 — Avoid for a complex monograph

### 11. `tufte-book` ★★☆☆☆

- **What it is**: Community implementation of Edward Tufte's book design — wide right margin, sidenotes, Palatino+Helvetica+Bera Mono. Main repo largely dormant since ~2015.
- **Why it fails at scale**: *"My experience writing with the `tufte-book` class is that it's more pain than is worth it. The class has not been kept up to date with modern packages, and is in fact broken for XeLaTeX."* — [r/LaTeX, 2020](https://www.reddit.com/r/LaTeX/comments/jmb9j1/book_writing/). No `\subsubsection`; sidenote citation superscripts collide with math superscripts; sidenote vertical-collision adjustments are manual. From [chasethedevil.github.io, 2016](https://chasethedevil.github.io/post/is_tufte_overrated/): *"using superscript so much could be annoying for someone used to read math and consider superscript numbers as math symbols… there seems to be a conflict between the use of LaTeX and many Tufte guidelines."*
- **Where it's still good**: Short, prose-heavy, annotation-dense works (essays, teaching handouts, design-oriented books). Not a complex monograph.

### 12. Dissertate, PhDThesisLaTeX ★★☆☆☆ (outside their institutions)

- Institution-compliance templates — Harvard/Princeton/NYU/Berkeley generic for Dissertate; Cambridge CUED for Krishna Kumar's. Excellent within their universities; outside, they trade flexibility for compliance you don't need.

### 13. ArsClassica ★★☆☆☆

- Italian variant of classicthesis with sans-serif chapter headings. Narrower community, no advantage over classicthesis for English-language work.

### 14. Springer `llncs` / `svjour3`, IEEE `IEEEtran`, Elsevier `elsarticle` — article classes only

- No `\chapter`, no front/back matter, two-column proceedings layouts. Wrong tool for a monograph regardless of community sentiment.

### 15. Eisvogel — **not a LaTeX class**

- It's a Pandoc template. Excellent for Markdown→PDF technical reports. Not viable as a monograph class.

### 16. Princeton UP, Wiley, De Gruyter, Elsevier book, World Scientific

- None of these distribute a public, full-featured author-controlled book class. All five rely on the publisher's typesetting pipeline. Use them only when contractually obligated, and prepare your source in `book`/`amsbook`/`memoir` while you write.

---

## Recommendation matrix by domain

| Domain | Best foundation | Best aesthetic (if no math/code) | Use if obligated |
|---|---|---|---|
| **Mathematics** (theorem-dense treatise) | `memoir` or `scrbook` + `amsthm` + `thmtools` + `tikz-cd` + `cleveref` | `amsbook` for AMS prestige; `classicthesis` only if Euler math is acceptable | `amsbook` (AMS), `cambridge7A` (CUP), `svmono` (Springer) |
| **Philosophy / humanities** | `memoir` (sidefootnotes, endnotes, critical apparatus via `reledmac`, `bigfoot`) | `classicthesis` is genuinely excellent here; `tufte-book` viable for annotation-heavy works | OUP and De Gruyter both re-typeset — write in `memoir` |
| **AI / ML** | `scrbook` or `memoir` + `algorithm` + `algpseudocode` + `minted` + `bm` + `hyperref(colorlinks)` | `kaobook` for richly annotated textbook style | MIT Press `newmath`, or negotiate camera-ready (precedent exists) |
| **CS** | `scrbook` or `memoir` + `subfiles` + `minted`/`listings` + `algorithm2e` + `cleveref` | `kaobook` for textbook; ACM Books template if ACM-contracted | `svmono` (Springer LNCS-adjacent), `cambridge7A` (CUP Tracts in TCS) |

---

## Cross-cutting tooling consensus for big books

- **Bibliography**: Use **biblatex + biber**, not natbib. *"The only good reason to still use natbib over BibLaTeX is that you are forced to do so, because your journal either requires you to copy and paste the `.bbl` file into the manuscript file or simply provides a citation style that is only compatible with natbib."* — [arbitrary-but-fixed.net, 2020](https://www.arbitrary-but-fixed.net/latex/latex%20alternatives/bibtex/2020/08/14/latex-alternatives-bibtex-part2-natbib-biblatex.html). Exception: AMS publications still expect `amsalpha`/`amsplain` BibTeX styles.
- **Engine**: **LuaLaTeX** for new large books — dynamic memory (*"effectively no limitations in everyday usage"*, [HN](https://news.ycombinator.com/item?id=25331238)), native OpenType, best microtype. pdfLaTeX remains faster for pure-math AMS workflows. XeLaTeX is the legacy middle ground but development has slowed.
- **Build tool**: **`latexmk`** locally with `-pvc` for live reload, plus `subfiles` for chapter-only compilation. Tectonic gives 85% smaller, 5× faster Docker builds ([joshfinnie.com](https://www.joshfinnie.com/blog/why-i-switched-to-tectonic/)) but is XeTeX-only — incompatible with LuaLaTeX-dependent packages. Overleaf is fine up to ~500MB project size but compile timeouts bite long books on the free tier.
- **Code listings**: `minted` (Pygments-quality highlighting, needs `--shell-escape`) is the community pick; `listings` as fallback for restricted/CI builds.
- **Cross-references**: `cleveref` (`\cref{}`) is now the universal recommendation — auto-formats "Theorem 2.3", "Lemma 4.1", "Algorithm 3.2" from one command.
- **Diagrams**: `tikz-cd` has overtaken `xymatrix` for commutative diagrams ([J.S. Milne's guide](https://www.jmilne.org/not/CDGuide.html)). `tikzexternalize` is essential for diagram-heavy chapters under pdfLaTeX.

---

## My final recommendation

For a large, complex monograph that needs to look excellent and remain ergonomic for years of writing and revision, **build on `scrbook` or `memoir`** and layer your typography deliberately. If philosophy/humanities-leaning prose dominates and you accept Palatino+no-bold, `classicthesis` on `scrbook` is a genuinely beautiful shortcut. If you want a richly annotated math/CS/AI textbook with margin citations and sidenotes, `kaobook` is the most polished hybrid available — accept the redefined-macros risk and pin your dependencies.

Avoid `tufte-book` (broken XeLaTeX, no subsubsections, sidenote/math conflicts), publisher classes you aren't contractually using, and anything dormant for 5+ years if your monograph will be maintained beyond initial release.

If a publisher is already in the picture: write in `memoir`/`scrbook`, convert at submission. AMS is the rare publisher where authoring directly in their class (`amsbook`) gives you a final product close to what gets printed; Springer, OUP, PUP, Wiley, Elsevier, and De Gruyter will retypeset regardless.

---

## Supporting research files

Three detailed companion reports were generated and are available alongside this summary in the workspace:

- `research_publisher_templates.md` — full publisher-class deep-dive (~5,200 words)
- `research_community_templates.md` — full community-class deep-dive (~5,500 words)
- `research_domain_considerations.md` — per-domain monograph needs, packages, and notable books (~4,300 words)

All quotes above are linked inline to their original sources (Reddit, TeX StackExchange, Hacker News, CTAN documentation, GitHub issues, and academic/practitioner blogs).
