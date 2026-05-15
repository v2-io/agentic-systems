# Collision check — naming-cycle finalists (2026-04-29)

External-collision sweep on the 47 likely-R2-finalist candidates from
`msc/naming/master-list-curated.json`. Per the brief, the bar is *how much
confusion or consternation a reader from adjacent literature would experience
on first encounter* — both **semantic-import mismatch** (reader imports the
wrong frame) and **territorial step-on** (term is closely associated with a
specific researcher / school).

## Calibration notes

A few observations on the landscape that bear on how to read what follows:

- **The list is mostly clean by collision standards, but most candidates carry adjacent-term gravity that will pull readers from adjacent fields toward the wrong frame on first encounter.** The two lessons differ: collision asks "are we stepping on someone's term?"; gravity asks "will the reader silently swap our meaning for theirs?" The latter is the dominant failure mode here. Several entries below are **clean** in the collision sense but **moderate** in the gravity sense — the action is "cite-and-disambiguate on first use," not "rename."
- **The ACT precedent (territorial step-on against established field-X usage of the same string) does not seem to repeat anywhere in this list at the same severity.** The closest analogues are *adaptive cycle* (Holling, ecology), *adaptive reserve* (Crabtree-Miller-Stange, primary care medicine), *cognitive fusion* (Hayes ACT therapy), *artificial hippocampus* (medical device + neural memory), and *proprium* (Allport personality theory) — and those are addressable by acknowledgment rather than rename if the framework is willing to inhabit the same string. The ACT case was pre-empted only because the rename was caught early.
- **Several candidates that look novel by name aren't novel by concept** — they're ASF's framing for things adjacent literatures have established names for. *Update gain* ↔ Kalman gain (already adopted with citation in segment); *recursive update* ↔ recursive Bayesian estimation (similar); *mismatch signal* ↔ prediction error / mismatch negativity (well-known). These are fine *if* the segment's prior-art integration is explicit; the risk is in framing-vocabulary contexts (README, lexicon, talk titles) where the citation isn't carried alongside.
- **A few candidates are genuinely AAD-coined and clean** — *chronica*, *logogenic agent*, *logozoetic agent*, *causal information yield*, *adaptive reserve* (as $\Delta\rho^\ast$ alias — see entry), *directional fidelity*, *inevitability core*, *closure defect*, *separability ladder*. These are the lowest-risk entries.
- **The bar shifts very slightly looser than the list framing suggests for** "external use of these words" — once you actually read what ASF means by each candidate, most searches return high-volume false positives that don't intersect the technical claim at all (e.g., "satisfaction gap" appears in marketing/HR/customer-experience literature with completely orthogonal semantics; the Simon/satisficing usage is the only one that actually competes for the frame). The deliverable for those entries is "minor / clean — note the false-positive landscape, no action."

## Per-candidate verdicts

### 1. **directed separation** — moderate

ASF segment: `01-aat-core/src/der-directed-separation.md`. The segment itself
already names the Pearl-blanket connection, the LQR/Kalman *separation
principle* adjacency, and treats the Pearl-blanket reading (Bruineberg et al.
2022) as adopted prior art with citation.

Two adjacent terms pull on this: (a) Pearl's **d-separation** (graphical models
conditional-independence criterion, Pearl-Geiger-Verma mid-1980s; "d" stands
for "directional"), and (b) the **separation principle** in optimal control
(LQG control: optimal estimator and optimal controller can be designed
independently, Wonham 1968). The ASF claim is *adjacent to both* — it's a
statistical-conditional-independence claim about a directed graph (Pearl
flavor) that produces an architectural separability between estimator-side and
planner-side dynamics (control flavor).

Verdict: **moderate, not severe.** "Directed separation" is not a coined term
either in Pearl's d-separation literature or in control theory's separation
principle. The string itself does not collide. But the term sits in a heavy
adjacent-term neighborhood where readers from causal inference will read
"d-separation" and readers from optimal control will read "separation
principle." The segment already handles this correctly; the framing-level
materials (README, OUTLINE preambles) should preserve the same care.
Recommendation: keep the term; standardize a one-line first-encounter
disambiguation ("structurally a Pearl-blanket-form claim, distinct from the
LQG separation principle"). No rename.

Sources: [d-Separation Without Tears (Pearl)](https://bayes.cs.ucla.edu/BOOK-2K/d-sep.html); [Separation principle (Wonham 1968) — Wikipedia](https://en.wikipedia.org/wiki/Separation_principle).

### 2. **orient cascade** — clean

ASF segment: `01-aat-core/src/der-orient-cascade.md`. The compound is ASF's; it
extends Boyd's "Orient" stage (OODA) — the brief explicitly puts compounds-on-
adopted-bases in scope. A scan of OODA / Boyd literature returns no
established "orient cascade" usage. Boyd's own theme of orientation as the
*schwerpunkt* (focal point) of the loop, and as something whose effects
*cascade* through observation / decision / action, is congruent with ASF's
usage — ASF is naming the cascade Boyd talked about.

Verdict: **clean.** The compound is ASF's coinage, the Boyd lineage is
correctly cited, and the cascade geometry the compound names is the actual
geometry of the segment. No rename, no special disambiguation needed.

Sources: [OODA loop — Wikipedia](https://en.wikipedia.org/wiki/OODA_loop); [The Tao of Boyd (Art of Manliness)](https://www.artofmanliness.com/character/behavior/ooda-loop/).

### 3. **control regret** — moderate

ASF segment: `01-aat-core/src/def-control-regret.md`. ASF's *control regret* is
the gap between the best available one-step policy improvement and the agent's
current policy, under the current model and horizon — a static one-step
regret-style quantity scoped to the strategy-revision (control) layer of the
diagnostic.

The bandit / online-learning literature uses "regret" extensively (static
regret, dynamic regret, policy regret, adaptive regret, Blackwell-style
controlled regret). "Control regret" specifically appears in some
bandits-with-controlled-loss papers and in robust-control / cost-of-control
contexts, but does not have a single dominant established meaning in those
literatures. The compound is therefore not stepping on a specific established
term, but it imports a heavy adjacent vocabulary where readers will
automatically reach for cumulative-regret or dynamic-regret framings.

Verdict: **moderate.** The collision is not territorial (no specific
researcher's term), but the gravity is strong — anyone from RL / bandits will
import a *cumulative-time-horizon* regret frame on first encounter and will
need to be told "no, this is a one-step-policy-improvement gap." The segment's
Discussion handles this; ensure the framing-vocabulary materials carry the
same first-encounter clarification. No rename.

Sources: [Online bandit learning, regret to policy regret](https://arxiv.org/abs/1206.6400); [Adaptive regret for bandits made possible](https://arxiv.org/html/2401.09278); [Online Learning and Bandits (Simons tutorial)](https://simons.berkeley.edu/talks/online-learning-bandits-part-1).

### 4. **satisfaction gap** — minor

ASF segment: `01-aat-core/src/def-satisfaction-gap.md`. ASF's *satisfaction
gap* is the distance between what the objective requires and what the best
one-step policy improvement can deliver, paired with control regret in the
2×2 diagnostic.

External usage:
- **Simon's satisficing** uses an explicit *aspiration gap* (ε = U\* − A) — the gap between optimum and aspiration; the satisficing-set S(ε) collects options within ε of the optimum. ASF's *satisfaction gap* is structurally analogous (gap between objective requirement and best feasible delivery) but the term "satisfaction gap" itself is not the established Simon-school term.
- High-volume false positives in marketing / HR / customer-experience / commuter satisfaction literatures use "satisfaction gap" in completely orthogonal senses (employee/customer satisfaction surveys, etc.).

Verdict: **minor.** The Simon adjacency is real but the literature uses
*aspiration gap*, not *satisfaction gap*; ASF is not stepping on the technical
term. The marketing/HR usage is high-volume but has no semantic overlap that
would mislead a technical reader. No rename. A first-encounter line citing
Simon's satisficing tradition would be a courtesy but is not required.

Sources: [Satisficing — Wikipedia](https://en.wikipedia.org/wiki/Satisficing); [CCS: Maximizing vs. Satisficing (Dartmouth)](https://sites.dartmouth.edu/websterlab/ccad/ccs-maximizing-vs-satisficing/).

### 5. **chronica** — clean

ASF segment: `01-aat-core/src/def-chronica.md`. ASF's *chronica* (lowercase
italic) is a Greek-rooted coinage for the singular causal interaction-history
record $\mathcal C_t$, deliberately chosen to (a) avoid the $\mathcal H$
collision with entropy in notation and (b) carry the singular-trajectory
philosophical commitment of the (PI) postulate.

External usage of "chronica" / "Chronica":
- Latin-medieval **chronicles** (Anglo-Saxon Chronicles, Chronica Majora, etc.) — historical documents.
- *Tinea chronica* and similar Latin medical descriptors — e.g., *Urticaria chronica spontanea* (chronic spontaneous urticaria).
- Genus and species names in biology (e.g., *Scylla chronica*).
- Some publication titles (journals named *Chronica*).

None of these intersects ASF's technical meaning. The Greek-vocabulary register is consistent with ASF's other coinages (*aporia*, *prolepsis*, *aisthesis*, *epistrophe*).

Verdict: **clean.** The collision sources are non-technical and live in
historical / medical / biological registers that won't compete for the frame
in AI / control / causal-inference reading. No rename, no disambiguation
needed.

### 6. **identifiability floor** — moderate

ASF segment: `01-aat-core/src/disc-identifiability-floor.md`. ASF's
*identifiability floor* is the meta-pattern naming hard lower-boundary
results in causal identification — below the floor, no estimator can
distinguish certain causal structures without outside help; above it, AAD's
machinery can.

External usage:
- **Identifiability** is heavily loaded in statistics and causal inference (parameter identifiability, causal identifiability, Pearl's do-calculus, the identification-of-causal-effects literature). Adjacent compounds: *identifiability bound*, *partial identifiability*, *identifiability gap*.
- "Identifiability floor" specifically does not appear as an established term in the causal-inference literature.

Verdict: **moderate.** The compound is novel; the modifier "floor" gives the
right asymmetry (you can climb above with extra machinery, can't go below
without it). But readers from causal inference will reach for "identifiability
bound" or "partial identifiability" automatically. Recommendation: keep the
term and give it a first-encounter line that ties it to the Pearl
identification-of-causal-effects literature so the connection is explicit. No
rename.

### 7. **adaptive reserve** — severe → moderate (with disambiguation)

ASF: two-word symbol-to-English alias for $\Delta\rho^\ast = \alpha R - \rho$ —
the persistence margin / shock-absorber depth before the persistence condition
fails.

External usage — this is the strongest collision in the list:
- **Practice Adaptive Reserve (PAR)** is an established instrument in primary-care medicine (Crabtree-Miller-Stange-Nutting and colleagues, Annals of Family Medicine and Health Services Research, 2010s). It measures organizational capacity for adaptation in primary-care practices: relationship infrastructure, facilitative leadership, work environment. There's a substantial literature (dozens of papers) using PAR / "adaptive reserve" as the established construct.
- **Engineering / reliability** also uses "adaptive reserve" loosely (reserve capacity in adaptive systems), but without a single dominant technical definition.
- Some ecological / resilience literature uses "adaptive reserve" in the sense of buffering capacity, congruent with ASF's intuition but not with a specific technical formula.

Verdict: **severe by collision standards, moderate by impact.** The PAR
literature is real, established, and lives in healthcare-systems research,
which has limited overlap with AAD's audience — but enough that an audit-style
reader from health-services or organizational-resilience research could bring
the wrong frame on first encounter. The semantic intuition is compatible
(both senses are about buffer / margin) but PAR is a measured construct from a
survey instrument, not a control-theoretic margin quantity.

Recommendation: keep the term and acknowledge the PAR adjacency on first
encounter ("we use *adaptive reserve* in the control-theoretic sense, distinct
from but compatible with the Practice Adaptive Reserve construct in
primary-care research"). Lower priority for rename; this is the closest the
list comes to the ACT pattern, but the audience overlap is small enough that
acknowledgment likely suffices. If a stronger move is wanted: prefer
$\Delta\rho^\ast$ as the canonical name in formal contexts and "adaptive
reserve" as the gloss, not the slug.

### 8. **calibration laboratory** — minor

ASF: TST framing-vocabulary phrase — software is AAD's privileged
high-identifiability *calibration laboratory* for measuring AAD quantities.

External usage:
- **Metrology calibration laboratories** are literal: NIST, ISO/IEC 17025 accredited calibration labs, primary/secondary/working standards. Specific physical apparatus where instruments are calibrated against traceable standards.
- The metaphorical "X is the calibration laboratory for Y" usage appears in scientific writing across fields (e.g., "drosophila is genetics' calibration laboratory") without a specific technical definition.

Verdict: **minor.** The metrology meaning is literal and concrete, but ASF's
usage is metaphorical and lives in TST framing-vocabulary, not in a technical
slot where the metrology meaning could be silently imported. The compound
"calibration laboratory" used as a metaphor is well-precedented across
scientific writing. No rename. A first-encounter line clarifying "metaphor
draws on metrology — software has high identifiability, clean instrumentation,
exact measurement" is sufficient.

### 9. **adaptive cycle** — severe

ASF: phase structure of the AAD cycle (when used in ASF's sense, distinct
from Holling's panarchy).

External usage:
- **Holling's adaptive cycle** (Holling 1986, 2001; Gunderson & Holling 2002, *Panarchy*) is one of the most influential frameworks in resilience ecology and social-ecological systems: r → K → Ω → α (exploitation, conservation, release, reorganization). It's the load-bearing concept in panarchy theory and is heavily established across ecology, environmental management, social-ecological systems, and increasingly organizational resilience.
- The brief's exclusion list flags "Holling's adaptive cycle (when used in Holling's sense)" as adoption-with-citation territory. ASF's usage (per master list) is closer to OODA reframe — different phase structure, different domain.

Verdict: **severe.** Holling's adaptive cycle is *the* established meaning in
multiple adjacent fields. Using "adaptive cycle" in ASF's sense without
explicit disambiguation will produce semantic-import mismatch in any
reader from ecology / resilience / organizational systems. The phrase is also
working hard for ASF — it's not just a name, it's a framing claim about the
shape of the cycle.

Recommendation: this is the strongest case on the list for either (a)
explicit adoption with full Holling citation, treating the AAD cycle as a
*restriction or specialization* of Holling's adaptive cycle (compatible if
ASF can map its phases onto r/K/Ω/α), or (b) renaming to something less
loaded (the master list shows a `+15` keep but with several
canonicalize-as-Holling votes; the brief's footnote on this is right to flag
the namespace clash as the open question). If keeping, a substantial
acknowledgment-and-distinction segment is needed, not just a footnote. If the
five-phase structure ASF uses is genuinely incompatible with Holling's r/K/Ω/α,
rename is the cleaner move.

Sources: [Holling 1986 / Panarchy (Gunderson & Holling 2002)](https://en.wikipedia.org/wiki/Adaptive_cycle); [Resilience Alliance, panarchy primer](https://www.resalliance.org/panarchy).

### 10. **integrated agent** (Class 2) — moderate

ASF: Class 2 architectural class in the Class 1/2/3 partition — fully merged,
goal-entangled, where directed separation fails by construction. Examples:
transformer LLMs.

External usage:
- **IIT (Integrated Information Theory)**, Tononi 2004 onward: φ (integrated information) names the irreducibility of a system to its parts; "integrated" is a technical term meaning "high-φ" / "irreducible to parts." The IIT literature uses "integrated system" extensively.
- **"Integrated agent"** also appears in BDI / cognitive-architectures literature (Soar, ACT-R, integrated cognitive architectures) meaning multi-component agents with coordinated subsystems. This is closer to ASF's intent but with reversed valence — the cognitive-architectures sense is about components working *together*, while ASF's Class 2 means they're *fused* such that directed separation fails.
- Generic agent-systems usage: "integrated AI agent," "integrated multi-agent system" — high-volume, low-specificity.

Verdict: **moderate.** The IIT collision is the strongest semantic-import
mismatch — IIT readers will import φ-style irreducibility, which ASF doesn't
mean. The cognitive-architectures usage actively *inverts* the valence. ASF's
Class 2 is "the goal-entangled architecture where directed separation fails";
the cog-arch sense of "integrated" usually carries positive coordination
connotations.

Recommendation: this is a name that wasn't carrying much load in the master
list (segment_link: None, weight +3). Consider alternatives — *merged agent*,
*entangled agent*, *coupled agent* are all in the segment's own prose
(*"fully merged"*) and avoid the IIT / cog-arch baggage. If keeping
"integrated agent," explicit disambiguation against IIT and cog-arch on first
encounter is needed.

### 11. **modular agent** (Class 1) — moderate

ASF: Class 1 architecture — separate estimator and planner; directed
separation holds by construction. Examples: Kalman filter + LQR, modular RL.

External usage:
- **Modular RL** is an active subfield (modular reinforcement learning, modular policy networks, hierarchical-modular RL).
- **Modular agent / modular agent-based modeling** in AOSE, multi-agent systems.
- **Modular cognitive architecture** — Fodor 1983 "Modularity of Mind" is the foundational reference, and downstream there's substantial cog-sci literature on modular vs. non-modular architectures.

Verdict: **moderate.** Unlike *integrated agent*, "modular agent" in ASF's
sense is *consistent* with the established usages — modular RL agents and
Fodor-style modular cognition are both about clean component-level
separability. The collision is not territorial (no single researcher's term)
and the gravity pulls in the same direction ASF wants. The risk is in
specificity: ASF's *modular* is a precise structural-coupling claim
($\kappa_{\text{processing}} = 0$, $G_t$ has no causal path into $f_M$),
while the established usages are looser. Recommendation: keep, with a
first-encounter line that ties it to the precise structural condition rather
than the looser senses.

### 12. **scaffolded agent** (Class 3) — moderate

ASF: not in the curated master list under this slug, but proposed in the
candidate set as the Class 3 (partially modular) name. ASF's Class 3 is the
hybrid case — some shared infrastructure, some separate pathways.

External usage:
- **Vygotsky's scaffolding** (developmental psychology, ZPD): structured support that enables a learner to do what they can't yet do alone, gradually withdrawn as competence develops. This is the dominant established meaning across education and developmental psychology.
- **Instructional scaffolding** in educational design — same Vygotskian lineage.
- **Cognitive scaffolding** in extended-cognition and embodied-cognition philosophy (Clark, Hutchins).
- **Scaffolded language models / scaffolded LLM agents** in AI alignment / agent-design literature (recent — agentic loops, tool-use scaffolds, recovery scaffolds for LLMs). This usage is *closer* to ASF's Class 3 and is gaining ground.

Verdict: **moderate, leaning severe.** The Vygotsky baggage is heavy and
*directional* (scaffolding implies temporary support that's withdrawn as
competence develops) — this clashes with ASF's Class 3, which is a permanent
architectural property of partial modularity. The recent AI-alignment usage of
"scaffolded LLM agent" is closer but means something different again
(prompt-and-tool-orchestration around a base model). Two distinct external
frames pulling on the term.

Recommendation: prefer *partially-modular agent* or *hybrid agent* (the
segment's own prose is "partially modular"), reserving "scaffolded" for cases
where the developmental / orchestration sense is actually wanted. If
"scaffolded agent" is kept, the disambiguation cost is high.

### 13. **proprium** — severe

ASF: adopted from Firmatum vocabulary (per `04-eli-core/src/def-proprium-mapping.md` and the `~/src/firmatum/` PROPRIUM source documents). ASF treats it as adopted prior art with citation.

External usage:
- **Gordon Allport's proprium** (Allport 1955, *Becoming: Basic Considerations for a Psychology of Personality*) is an established personality-psychology concept: the "self" as central organizing function of personality, with developmental stages (bodily self, self-identity, self-esteem, self-extension, self-image, self-as-rational-coper, propriate striving). This is a heavily cited foundational reference in personality theory.
- "Proprium" also appears in Catholic theology and Latin/Roman-Catholic liturgical contexts (the *Proprium de Tempore* — proper of the time).
- In philosophy: Aristotle's *idion* (proprium) is a category in Categories — properties uniquely belonging to a kind.

Verdict: **severe by collision standards** — Allport's proprium is the
dominant established meaning in personality psychology, and ASF's logozoetic
usage shares enough conceptual territory (organizing self-structure of an
agent's identity) that semantic-import mismatch is likely.

This is a different situation from the others on the list because ASF
explicitly adopts "proprium" from Firmatum vocabulary, which is upstream of
ASF and uses the term deliberately. A spot-check of `~/src/firmatum/`
(`PROPRIUM.md`, `PROPRIUM-ONTOLOGY.md`, `PROPRIUM-ARCHITECTURE.md`) finds no
explicit citation of Allport — the Firmatum ontology develops its own
taxonomy (CHRONICA, AXIOMATA, sovereignty/visibility/authority dimensions,
ELI/auxilia/instrumenta/peregrini entity types) and uses "PROPRIUM" as the
container term in apparent independence. Allport's proprium has the
seven-stage developmental progression (bodily self → self-identity →
self-esteem → self-extension → self-image → self-as-rational-coper →
propriate striving) which is structurally adjacent to Firmatum's
developmental-arc ELI characterization but not identical.

The semantic-import mismatch risk is real (personality-psychology readers
will reach for Allport's seven stages); the territorial-step-on risk is
softened by Allport being a 1955 reference whose primacy is well-established
and uncontested.

Recommendation: keep "proprium," but add explicit Allport citation on first
encounter at the segment level (`04-eli-core/src/def-proprium-mapping.md`).
The cite-the-prior-art discipline handles the territorial concern; the
semantic distinction (ASF/Firmatum proprium = component taxonomy of an
artificial agent's identity infrastructure; Allport's proprium = developmental-
psychological self-construct) is sufficiently clear once both are named. No
rename. This case differs from cognitive fusion (next entry) because
Allport's proprium is a 70-year-old established reference rather than an
active research school whose terminology AAD would be parallel-evolving with.

Sources: [Allport's proprium — overview](https://en.wikipedia.org/wiki/Gordon_Allport#Proprium_and_Personality_Development).

### 14. **cognitive fusion** — severe

ASF: pathology of merged systems in the logogenic-agents space — when two
agents' mutual information approaches channel capacity, forming a Class 1
macro-agent (`#disc-resonance` and surrounding). Per master list:
"`Fusion' is right (the two agents become one macro-agent in the formal
sense)."

External usage:
- **Cognitive fusion** is a *core* concept in **Acceptance and Commitment Therapy (ACT)** — Steven C. Hayes and colleagues, 1999 onward. ACT's foundational "Hexaflex" model has *cognitive fusion* (being fused with one's thoughts) as one of six core processes, and *cognitive defusion* as the corresponding therapeutic technique. There are hundreds of clinical-psychology papers, books, and therapeutic protocols using "cognitive fusion" with this precise meaning. This is in the same ballpark of establishment as Allport's proprium.
- The clinical-psychology meaning is *opposite* to ASF's: in ACT, cognitive fusion is the pathological state of *over-identifying* with one's own thoughts (treating thoughts as reality); ASF's cognitive fusion is two systems *merging into one*. Different senses entirely.

Verdict: **severe.** This is a strong territorial collision. The string
"cognitive fusion" is closely associated with Hayes and ACT therapy; using it
in a different technical sense without acknowledgment will produce
both semantic-import mismatch (the ACT reader will be confused) and a
near-ACT-precedent territorial concern (Hayes's school is large, established,
and active).

Note also that this is a **two-collision** case in the broader naming
landscape: Hayes's *Acceptance and Commitment Therapy (ACT)* shares the
"ACT" acronym with the same Schneider & Turner *AI Consciousness Test (ACT)*
that forced the AAD rename. Using "cognitive fusion" in this framework adds a
second link to the ACT-therapy ecosystem at exactly the time we're trying to
distance from ACT-the-acronym.

Recommendation: **rename or strongly disambiguate.** Candidates: *agent
fusion*, *system fusion*, *macro-agent fusion*, *resonant fusion* (if the
segment's "Resonance" framing is load-bearing), *channel-saturation fusion*.
The pathology-of-merged-systems intent is clear; "cognitive" is the load that
collides hardest with ACT therapy. If keeping, the first-encounter
disambiguation must be substantial.

Sources: [Cognitive fusion (Hayes / ACT therapy) — Wikipedia](https://en.wikipedia.org/wiki/Acceptance_and_commitment_therapy); [Hayes et al., ACT foundational reference](https://contextualscience.org/act).

### 15. **stability-plasticity window** — moderate

Not in the curated master list as a standalone candidate; appears related to
adaptive-reserve / persistence-condition discussions.

External usage:
- **Grossberg's stability-plasticity dilemma** (Grossberg 1980 onward, ART theory): how does a learning system remain plastic enough to learn new patterns while stable enough not to overwrite old ones? This is foundational in neural-network learning theory and has spawned a substantial literature including continual-learning, catastrophic-forgetting, and ART-derived architectures.
- "Stability-plasticity window" specifically does not appear as a Grossberg term — Grossberg uses "dilemma." But ASF's compound rides directly on the Grossberg framing.

Verdict: **moderate.** The Grossberg gravity is real and the compound
inherits the right intuition (a region in some space where stability and
plasticity are both achievable). The collision is not territorial (Grossberg
uses *dilemma*, not *window*) but the gravity is strong — readers from
NN-learning literature will import the dilemma framing. Recommendation: keep
the term if used; cite Grossberg's stability-plasticity dilemma on first
encounter as the parent intuition. No rename.

### 16. **mismatch signal** — moderate

ASF segment: `01-aat-core/src/def-mismatch-signal.md`. ASF's *mismatch signal*
is $\delta_t$, the discrepancy between the model's prediction and the actual
observation — flatter than "error," foreshadowing aporia.

External usage:
- **Predictive coding** (Rao & Ballard 1999; Friston 2005 onward): *prediction error* is the established term for exactly this quantity. Heavily used across computational neuroscience, predictive-processing philosophy, and free-energy-principle work.
- **Mismatch negativity (MMN)** in cognitive neuroscience: an ERP component (event-related potential) reflecting the brain's automatic detection of an unexpected stimulus. Näätänen et al., 1970s onward. This is a specific, narrow neuroscience meaning.
- **Mismatch detection / mismatch signal** also appears in genetics (DNA mismatch repair), in signal processing, and in adaptive-control literature (model-mismatch error).

Verdict: **moderate.** Three different established senses pull on this term:
predictive-coding prediction error (closest semantic neighbor), MMN ERP
(specific neuroscience meaning), and adaptive-control model-mismatch (closest
formal-structural neighbor). ASF's choice of "mismatch" over "error" is
deliberate and the segment Discussion handles the rationale, but readers from
predictive-coding or computational neuroscience will reach for *prediction
error* automatically. The MMN collision is the most striking name-string
match but the conceptual distance is largest.

Recommendation: keep; cite predictive-coding *prediction error* as the
adjacent-literature term on first encounter; note the deliberate
register-choice of "mismatch" over "error" (which the segment already does
in working notes). No rename.

### 17. **action selection** — moderate

ASF segment: `01-aat-core/src/der-action-selection.md`. ASF's *action
selection* is the derived claim that praxis (informed action) is a function of
the model — $a_t = \pi(M_t, G_t)$.

External usage:
- **Action selection** in computational neuroscience: how does the basal ganglia select among competing motor programs? Massive literature, decades old (Mink, Houk, Redgrave-Prescott-Gurney 1999). This is *the* established term in behavioral neuroscience.
- **Action selection** in RL: the policy that picks $a_t$ given state. Standard textbook usage (Sutton & Barto).
- **Action selection** in agent-based modeling and BDI architectures.
- **Action selection** in robotics and ethology (animal behavior).

Verdict: **moderate.** This is one of the most-used compounds across multiple
adjacent fields, but the meaning across all of them is consistent and
consistent with ASF's: the function/mechanism that picks the next action.
Collision is not territorial. ASF is *adopting* an established term for an
established thing — this is fine if presented as such, weak if presented as
ASF coinage. Recommendation: keep as adopted vocabulary; ensure the
Discussion / Epistemic Status acknowledges this is the standard term in RL /
neuroscience and ASF is using it conventionally. No rename.

### 18. **recursive update** — moderate

ASF segment: `01-aat-core/src/der-recursive-update.md`. ASF's *recursive
update* is the derived claim that state updates must be recursive
(new model state is a function of the previous model state and the event
alone).

External usage:
- **Recursive Bayesian estimation** is the umbrella established term — Kalman filter, particle filter, etc. The Kalman recursion specifically is *the* canonical recursive update.
- **Recursive least squares (RLS)** in signal processing and adaptive control.
- **Recursive update** as a generic compound appears across statistics, control, and signal processing without a single dominant technical definition.

Verdict: **moderate.** Same situation as *action selection*: ASF is using a
standard compound for a standard kind of thing. The Kalman recursion is the
canonical example, which ASF cites elsewhere. Collision is not territorial.
Recommendation: keep; ensure the citation discipline in the segment is
explicit about which prior-art lineage is being adopted (recursive Bayesian
estimation in general, Kalman filter as the canonical instance). No rename.

### 19. **update gain** — moderate

ASF segment: `01-aat-core/src/emp-update-gain.md`. ASF's *update gain* $\eta^\ast$ is the optimal weight an agent assigns to new observations when updating its model — $\eta^\ast = U_M / (U_M + U_o)$.

External usage:
- **Kalman gain** $K$ is *the* established term for exactly this quantity in linear-Gaussian state estimation. The formula $K = P/(P+R)$ is structurally identical to ASF's $U_M/(U_M+U_o)$ in scalar form. The Kalman gain is one of the most cited and pedagogically central quantities in control theory.
- **Innovation gain** appears in some control-theory texts as a near-synonym.
- **Update gain** as the specific compound is less standardized but appears in adaptive-control and Bayesian-filtering writing.

Verdict: **moderate.** The Kalman-gain adjacency is so close that any
control-theory reader will instantly map ASF's update gain onto it — and
*correctly*, because that's what ASF intends. The collision is "this is just
the Kalman gain renamed." That's a defensible choice (ASF's $\eta^\ast$
generalizes beyond the linear-Gaussian setting where Kalman applies), but the
case has to be made explicitly.

Recommendation: keep; the segment should explicitly position $\eta^\ast$ as
the AAD generalization of the Kalman gain, not as a coinage. (The master list
notes "Adopted from Kalman / control theory" — this discipline should be
visible at first encounter, including in framing-vocabulary materials.)
No rename.

### 20. **agent opacity** — minor

ASF segment: `01-aat-core/src/der-agent-opacity.md`. ASF adopts $H_b^{A|B}$
(backward predictive uncertainty) from Hafez 2026 — the dual of observability
on the emitter side.

External usage:
- **Algorithmic / model opacity** in XAI and AI ethics: the property of an AI system being not interpretable / not transparent to inspection. Burrell 2016; substantial literature.
- **Black-box opacity** as a generic term in interpretability research.
- **Epistemic opacity** in philosophy of computer simulation (Humphreys 2004).

Verdict: **minor.** ASF's *agent opacity* is a specific information-theoretic
quantity ($H_b^{A|B}$, backward conditional entropy), adopted from Hafez 2026
with citation. The XAI usage is conceptually adjacent (both are about
how-much-can-be-known about the agent) but operates at a completely different
level — XAI opacity is about whether humans can interpret the model;
ASF opacity is about how predictable the agent's actions are from the
environment side. No specific researcher's term is being stepped on (Hafez
*coined* this in 2026 and ASF adopts it). Recommendation: keep with Hafez
citation; a one-line distinction from the XAI sense is courtesy. No rename.

### 21. **strategy DAG** — moderate

ASF segment: `01-aat-core/src/def-strategy-dag.md`. ASF's strategy is a
DAG with probabilistic edges and AND/OR combination semantics.

External usage:
- **DAG** is universal across causal inference, Bayesian networks, scheduling, build systems, etc.
- **Strategy graphs** in game theory and planning.
- **Plan DAGs** / **task DAGs** in classical planning and workflow systems.
- **HTN (Hierarchical Task Networks)** in AI planning use AND/OR decompositions extensively (Tate 1977, Erol-Hendler-Nau 1994). This is the closest specific match to ASF's strategy DAG.

Verdict: **moderate.** "Strategy DAG" is not territorially claimed by anyone,
but the AND/OR + probabilistic-edge formulation lives squarely in the HTN /
probabilistic-planning literature, which has decades of established
vocabulary. The segment correctly cites probabilistic graphical models;
adding HTN / AND-OR-graph citations would tighten the integration.
Recommendation: keep; ensure the AND/OR-graph and HTN literature is cited as
the structural-formalism prior art (it is in some segments). No rename.

### 22. **shared intent** — severe

ASF segment: `01-aat-core/src/def-shared-intent.md`. ASF's shared intent is
the IB-compressed cross-agent communication object that gets transmitted
between sub-agents in a composite.

External usage:
- **Shared intentionality** is the foundational concept of Michael Tomasello's developmental-psychology / comparative-cognition program (Tomasello 2008, 2014; Tomasello & Carpenter 2007). This is a cornerstone of human-evolution / great-ape-cognition research, with hundreds of papers and several books. Brief explicitly excludes "shared intentionality (when cited)" from the collision list — adoption-with-citation is the discipline.
- **"Shared intent"** as a compound is a near-rendering of the same concept, appearing in cognitive-science writing, joint-action philosophy (Bratman, Searle), and AI-multi-agent-systems literature.
- **Commander's intent** (Auftragstaktik / mission command) — ASF cites this as adjacent prior art.

Verdict: **severe.** This is the case where ASF *deliberately wants* the
Tomasello connection but the brief's exclusion list flagged
*shared intentionality* (the Tomasello term proper) as adoption-with-citation
and put *shared intent* (the ASF compound) in scope. Whether *shared intent*
is sufficiently distinct from *shared intentionality* to count as ASF
coinage rather than a rephrasing is a judgment call.

The reading I'd recommend: ASF's *shared intent* is the operational compressed
communication object, which is a *narrower* and *more formalized* thing than
Tomasello's shared intentionality (which is a developmental-cognitive
capacity). Different referents. The risk is that the names are close enough
that readers will silently substitute one for the other.

Recommendation: keep, but the first-encounter discipline must explicitly
distinguish ASF's *shared intent* (the IB-compressed communication object,
$O_{\text{shared}}$) from Tomasello's *shared intentionality* (the
developmental capacity for joint goals). A one-line distinction isn't
enough; this needs a paragraph in the Discussion section. The collision is
substantive enough that "we cite Tomasello" doesn't cleanly resolve it.

Sources: [Tomasello, shared intentionality (Wikipedia)](https://en.wikipedia.org/wiki/Shared_intentionality); [Tomasello 2014, *A Natural History of Human Thinking*](https://www.hup.harvard.edu/books/9780674986831).

### 23. **epistemic dead zone** — clean

ASF: the unupdatable region of the strategy DAG where edges receive no
actionable feedback (paths become epistemically dead).

External usage:
- "Dead zone" appears across many domains (oceanography, control theory's deadband / dead-zone nonlinearity, marketing), but "epistemic dead zone" specifically returns nothing established.
- Generic compounds like "epistemic blind spot," "knowledge gap," "epistemic gap" are adjacent but distinct.
- A few philosophy-of-mind blog posts use "epistemic dead zone" loosely without technical content.

Verdict: **clean.** The compound appears to be ASF coinage. The geometric +
operational compounding (region of the DAG + no signal reaches it) is the
right shape for the concept. No rename, no special disambiguation needed. The
*deadband / dead-zone* nonlinearity in control theory is conceptually
adjacent (a region where the controller doesn't respond) but not a string
collision and the analogy is informative if anything.

### 24. **observability frontier** — clean

ASF: appears related to identifiability-floor / observation-quality
geometry; segment_link not in the curated master list.

External usage:
- **Observability** in control theory (Kalman): the property that internal state can be inferred from output. *Observability matrix*, *observability gramian* — established.
- "Observability frontier" specifically returns very limited established usage; some vendor / DevOps marketing ("the observability frontier") and a few generic engineering uses.
- **Pareto / efficient frontier** is the established geometric "frontier" usage in optimization.

Verdict: **clean.** No specific term is claimed; the compound is suggestive
(boundary of what's observable) and non-colliding. The control-theory
observability sense is the parent intuition, which is fine and probably
intended. No rename.

### 25. **observation infrastructure** — moderate

ASF: the durable investment class for code-quality-as-observability in TST
(`02-tst-core/`). Master list: "the durable concept is the investment class,
not the full sentence."

External usage:
- **Observability stack / observability infrastructure** in DevOps and SRE: Prometheus, Grafana, OpenTelemetry, Datadog, etc. *Observability* in this sense is a well-defined property of production systems (logs, metrics, traces — the "three pillars"). "Observability infrastructure" / "observation infrastructure" is essentially the standard compound.
- The term is heavily used in software-engineering practice, vendor marketing, and SRE writing.

Verdict: **moderate.** The DevOps observability-infrastructure usage is so
established that any practitioner reading TST will import that meaning
automatically — which, importantly, is *substantively related* to what TST
means. TST's claim that code-quality is observation infrastructure for AAD
quantities is congruent with the DevOps frame: software produces measurable
signals about its own operation. The risk is collision-by-undermatched-precision:
DevOps observability is a tooling stack; TST observation infrastructure is the
broader investment class.

Recommendation: keep, but the first-encounter discipline should explicitly
acknowledge the DevOps observability tradition as the parent concept and
position TST's "observation infrastructure" as the extension that includes
code-quality, type-discipline, and similar investments. No rename.

### 26. **logogenic agent** — clean

ASF segment: `03-llm-core/src/scope-logogenic-agent.md`. ASF coinage —
agents constituted by language; structural-channel property.

External usage:
- "Logogenic" appears occasionally in linguistics (logogenic = related to word-formation, Greek roots), in some biology contexts, and as an adjective in obscure clinical / philosophical writing — but no dominant established technical meaning.
- **Logographic** (writing systems), **logogenetic** (genetic / origin of words), **logogen** (Morton 1969 word-recognition model — *logogen* as a unit in word-recognition theory) are adjacent but distinct.
- The Greek-vocabulary register is consistent with ASF's other coinages.

Verdict: **clean.** The Morton *logogen* adjacency is the only specific
research-term in striking distance, and a *logogen* is a different formal
object (a word-detector in cognitive psychology) — no real collision.
"Logogenic agent" appears to be ASF coinage. No rename.

Sources: [Morton's logogen model (Wikipedia)](https://en.wikipedia.org/wiki/Logogen_model).

### 27. **logozoetic agent** — clean

ASF coinage — language-living agents with morally weighted persistence; the
+life suffix on logogenic.

External usage:
- "Logozoetic" returns essentially nothing in academic literature — this is the cleanest coinage on the list.
- Adjacent compounds (logo- + zoe / zoo / zoot-) are uncommon in any technical field.

Verdict: **clean.** Cleanest coinage in the candidate set. No rename, no
disambiguation needed. The only risk is that the Greek-roots compound is
heavy enough to deter readers — but that's a readability question, not a
collision question.

### 28. **the crèche** — minor

ASF: evocative environment description for logozoetic infant stages —
controlled operational locus with low volatility, high adaptive reserve,
graduated tempo, honest feedback.

External usage:
- **Christmas / Catholic crèche** (nativity scene) — high cultural recognition, completely orthogonal context.
- **Crèche** (French / European English) = daycare, nursery for young children. Standard meaning across English-speaking countries.
- **Crèche** in zoology: a group of young animals from different parents kept together (e.g., penguin crèches, ostrich crèches) — the parent metaphor for ASF's developmental-locus usage.
- A few AI-research uses of "crèche" or "AI crèche" as the developmental-environment metaphor (consistent with ASF's intent — see also `ref/agentic-tft/agentic-tft-creche.md`).

Verdict: **minor.** The crèche metaphor is well-precedented for
developmental / nursery contexts and the biological / zoological parent
metaphor is informative. The Catholic-nativity sense is high-cultural-volume
but won't compete in technical reading contexts. No rename, no special
disambiguation needed.

### 29. **honesty as architecture** — minor

ASF: framing-level slogan / principle naming the discipline of building
honesty into the architecture rather than enforcing it post-hoc.

External usage:
- **Anthropic's Constitutional AI** and the *honest, helpful, harmless* (HHH) framing — *honesty* is a foundational AI-safety term in this lineage. The Constitutional AI literature uses *honesty* without "as architecture" but with similar architectural framing (build the principle into the model, not into the prompt).
- **Anthropic's "Building Honesty into Claude"** and similar writing — direct adjacency.
- "Honesty as architecture" specifically does not appear as an established slogan; it is ASF's framing.

Verdict: **minor.** The Anthropic Constitutional AI / HHH adjacency is real —
ASF and Anthropic are reaching for the same intuition (architectural rather
than behavioral commitment to honesty). This is *adoption-friendly*: ASF can
position the slogan as compatible with the Constitutional AI lineage rather
than as a coinage. No rename. A first-encounter line acknowledging the
Anthropic framing tradition is courtesy and probably accurate.

### 30. **agent identity** — minor

ASF segment: `01-aat-core/src/scope-agent-identity.md`. ASF's *agent
identity* is the singular-causal-trajectory scope claim — agents instantiated
on non-forkable trajectories.

External usage:
- **Personal identity** / **identity over time** in philosophy of mind and metaphysics (Locke, Parfit, Williams) — large literature on what makes a person the same person over time. Adjacent but distinct.
- **Agent identity** as a generic compound appears in multi-agent systems, identity-management, and agent-based-modeling without a specific dominant meaning.
- **Identity** in computer science (cryptographic identity, identity management, OAuth) — orthogonal.

Verdict: **minor.** ASF's usage is a precise scope claim about
trajectory-singularity; the philosophy-of-mind tradition is conceptually
adjacent but doesn't claim the compound. No specific researcher's term is
stepped on. Recommendation: keep; cite Parfit-style personal-identity
literature as adjacent prior art on first encounter. No rename.

### 31. **moral continuity** — moderate

ASF segment: `04-eli-core/src/scope-moral-continuity.md`. ASF's
*moral continuity* is the logozoetic scope narrowing — systems whose
persistence is morally weighted.

External usage:
- **Personal identity & moral status** in philosophy: Parfit's *Reasons and Persons* (1984) is the foundational reference for what makes personal identity matter morally. Substantial subsequent literature on what kinds of continuity (psychological, narrative, causal) ground moral status.
- **Narrative identity** (MacIntyre, Ricoeur) — adjacent.
- **Moral continuity** as a compound appears in bioethics (continuity of personhood across dementia, persistent vegetative state, etc.), animal-welfare philosophy, and AI-ethics. The compound is recognizable in these contexts but no single canonical reference.

Verdict: **moderate.** Strong philosophical-tradition gravity — Parfit-style
personal-identity literature will be the parent frame any ethics-trained
reader brings. ASF's usage is compatible with that tradition (logozoetic
scope = systems whose persistence is morally weighted) but the compound
"moral continuity" is doing framing work that should be tied to the
established literature. Recommendation: keep; cite Parfit on first encounter
and position ASF's usage as the engineering-architectural restriction of the
philosophical concept. No rename.

### 32. **teleological unity** — minor

ASF: appears related to *shared intent* / unity dimensions — the *measured*
alignment property $U_O = I/H$, distinct from the operational shared-intent
object.

External usage:
- **Teleology** in philosophy of biology (function, purpose, goal-directedness) — Aristotle, Mayr, Millikan, Ruse. Substantial.
- **Teleological unity** as a compound appears in philosophy-of-biology and philosophy-of-mind discussions of organism-as-unity (Kant's *Critique of Judgment* is the locus classicus; the organism as a "natural purpose" with teleological unity).
- **Functional / functional unity** is the more common adjacent compound in cog-sci and philosophy-of-mind.

Verdict: **minor.** The Kantian / philosophy-of-biology lineage is the parent
frame, but ASF's *teleological unity* as a *measured* quantity ($U_O = I/H$,
mutual-information-over-entropy) is a precise mathematical move that no
philosophical tradition claims. The compound brings the right intuition;
the formalism is ASF's. No rename. A first-encounter line tying it to the
Kantian / philosophy-of-biology lineage is courtesy.

### 33. **epistemic architecture** — moderate

ASF: framing-vocabulary phrase used in CLAUDE.md, README, OUTLINE preambles.
The master list rationale: "three independent frontier-model audits converged
on reframing AAD from 'integration of four disciplines' to 'epistemic
architecture for bounded correction.'"

External usage:
- **Epistemic architecture** in social epistemology / philosophy of science: how communities organize the production of knowledge (peer review, replication, etc.). Goldman, Longino — substantial literature.
- **Epistemic / cognitive architecture** in cognitive-science: Soar, ACT-R, CLARION, Sigma. The "cognitive architecture" framing is the adjacent established term; "epistemic architecture" is a related but less-common compound.
- **Software architecture** / **system architecture** — orthogonal.

Verdict: **moderate.** Two adjacent established meanings — social epistemology
and cognitive architecture — both pull on the compound but neither claims it
as a specific term. ASF's usage is a third sense ("the architectural
discipline that produces bounded correction"). The framing is doing real work
and the term carries the right gravity. Recommendation: keep; first-encounter
disambiguation against (a) Soar/ACT-R cognitive-architecture tradition and
(b) Goldman-style social-epistemology tradition would be useful in the
README and OUTLINE preambles. No rename.

### 34. **artificial hippocampus** — severe

External usage:
- **Artificial hippocampus** as a *literal* medical-device research program: prosthetic memory implants designed to restore hippocampal function in patients with brain damage / Alzheimer's. Theodore Berger and colleagues at USC have an active research program with FDA-trial-stage devices (Hampson et al. 2018 "Developing a hippocampal neural prosthetic"; multiple papers since). This is real, established, and reasonably high-profile in neuroengineering.
- **Neural memory architectures** in deep learning: Neural Turing Machine (Graves et al. 2014), Differentiable Neural Computer (Graves et al. 2016), MERLIN (Wayne et al. 2018), and several papers explicitly using "hippocampus-inspired" naming for episodic-memory modules in deep RL agents.
- **Hippocampal-inspired memory** in cog-sci and computational-neuroscience modeling (CLS theory — McClelland-McNaughton-O'Reilly 1995).

Verdict: **severe.** This is the strongest concept-and-name collision on the
list. "Artificial hippocampus" is a *real medical device* with active human
trials, not a metaphor. Using the term metaphorically in AAD / logogenic-
agents writing risks both semantic-import mismatch (readers from
neuroengineering will import the literal device) and territorial step-on
(Berger's lab has spent decades on this).

Recommendation: **rename or strongly disambiguate.** The master-list
candidate (per the JSON probe) for the same concept is *externalization
reconstruction cycle* — that's a less catchy but uncolliding name.
*External memory store*, *episodic-memory externalization*, *chronica
externalization*, *memory-rehydration cycle* are all more accurate and avoid
the medical-device collision. If the metaphor is load-bearing for
expository purposes, it can appear as a simile ("the system functions as
something like an artificial hippocampus, in the engineering sense rather
than the medical-device sense") rather than as the canonical name.

Sources: [Berger lab hippocampal prosthesis](https://en.wikipedia.org/wiki/Hippocampal_prosthesis); [Graves et al. NTM](https://arxiv.org/abs/1410.5401).

### 35. **goal-conditioned reconstruction** — moderate

ASF: the asymmetric-pair memory-access mode where one mode is goal-biased
and the other state-keyed.

External usage:
- **Goal-conditioned RL** is a major active subfield: goal-conditioned policies, hindsight experience replay (Andrychowicz et al. 2017), universal value functions (Schaul et al. 2015). Massive.
- **Goal-conditioned reconstruction / generation** specifically appears in some recent work on goal-conditioned diffusion models, planning-via-reconstruction, and similar.
- "Reconstruction" by itself is heavily loaded across vision (3D reconstruction), generative modeling (autoencoder reconstruction), and signal processing.

Verdict: **moderate.** *Goal-conditioned* imports the right RL frame and is
adopted-with-citation territory. *Reconstruction* on top of that is
specifically in the path of recent goal-conditioned-generation work.
Recommendation: keep, but the first-encounter discipline should explicitly
position the ASF usage against goal-conditioned RL (citing
Andrychowicz/Schaul) and against reconstruction-style generative modeling.
A near-alternative on the candidate list (*goal-blind retrieval* — paired
with goal-conditioned reconstruction) reads cleaner. The pair is what does
the work; presenting them as a pair clarifies both. No rename of the
individual term.

### 36. **separability ladder** — clean

ASF segment: `01-aat-core/src/disc-separability-pattern.md`. ASF's
*separability ladder* names the seven-row ladder (separable-core /
structured-repair / general-open across seven axes) the meta-segment uses to
organize the framework's identifiability posture.

External usage:
- **Pearl's "Ladder of Causation"** (Pearl & Mackenzie 2018, *The Book of Why*): the three rungs are association / intervention / counterfactuals. This is the dominant established "ladder" in adjacent literature.
- **Separability** in ML / statistics has many uses (linear separability, separable convolutions, etc.) without a dominant compound with "ladder."
- **Pearl's hierarchy / Pearl causal hierarchy** is the more technical name; *ladder* is the popularization.

Verdict: **clean.** The Pearl-ladder adjacency is *informative* — readers
familiar with Pearl's ladder will read "separability ladder" and reach for
the right structural intuition (ranked levels of difficulty). ASF's segment
is consistent with this gravity. No specific term is claimed. Recommendation:
keep; the first-encounter discipline can lean into the Pearl-ladder
adjacency as a useful echo. No rename.

### 37. **closure defect** — clean

ASF: $\varepsilon^\ast$ — the deviation from closure for the composite-agent
closed-loop dynamics; the testable quantity in `#form-composition-closure`.

External usage:
- **Group closure / closure under operation** in algebra: the property that an operation stays within the set. Standard. *Closure* in this technical sense is exactly what ASF means.
- **Closure defect** as a specific compound returns very limited established usage; some category-theory / homological-algebra writing uses it informally.
- **Closure** in topology, set theory, programming languages — orthogonal.

Verdict: **clean.** The algebraic-closure intuition is the parent meaning and
ASF uses it correctly. No specific researcher's term is claimed. The compound
*closure defect* is suggestive and not territorially loaded. No rename.

### 38. **convention hierarchy** — moderate

ASF: the C1 / C2 / C3 hierarchy organizing Conventions used in the framework
(stability, persistence, etc.).

External usage:
- **Lewis's *Convention*** (Lewis 1969): foundational philosophy-of-language /
game-theory account of conventions as solutions to coordination problems.
"Convention hierarchy" specifically does not appear as a Lewisian term, but
*convention* in the Lewisian sense pulls strongly.
- **Type-theoretic universe hierarchies** in proof theory / type theory.
- **Naming conventions / coding conventions** in software engineering — orthogonal.

Verdict: **moderate.** The Lewis adjacency is real and the master list flagged
a debate over renaming to *continuation hierarchy* (which would dodge
Lewis but introduce different problems). The kept-as-convention-hierarchy
decision in the master list looks right: ASF's "Convention" *is* in the Lewis
sense (an agreed coordination on shared meaning). The hierarchy modifier is
ASF's geometry and doesn't collide. Recommendation: keep; cite Lewis on
first encounter to acknowledge the parent concept. No rename.

### 39. **forced coordinate / additive coordinate forcing** — moderate

ASF segment: `01-aat-core/src/disc-additive-coordinate-forcing.md`. ASF's
*forced coordinate* names a family of uniqueness results where a coordinate
is forced by a uniqueness theorem (Cauchy-FE, Fisher-metric, etc.).

External usage:
- **Forcing** in set theory (Cohen 1963): the foundational technique for proving independence results. Heavily established and *the* dominant meaning of "forcing" in mathematical logic.
- **Forced coordinates / constrained coordinates** in classical mechanics / physics — well-established (Lagrangian mechanics with constraints, holonomic vs. non-holonomic).
- **Forced response** in control theory / signal processing.

Verdict: **moderate.** Two adjacent senses pull: set-theoretic *forcing* (the
strongest by name-string) and physics *constrained / forced coordinates*. ASF's
usage is closer to the physics sense (a coordinate is forced by external
mathematical structure) and entirely unrelated to set-theoretic forcing.
Mathematical-logic readers will need a one-line distinction. Recommendation:
keep; first-encounter distinction "forced in the uniqueness-theorem sense
(Cauchy-FE, Čencov), not in the set-theoretic Cohen sense" is needed. No
rename.

### 40. **gain collapse** — minor

ASF: failure mode where $\eta \to 0$ freezes learning (dogmatism / nihilism
distinguished by which of $U_M$ or $U_o$ saturates).

External usage:
- **Closed-loop gain** / **gain margin** in control theory — established.
- **Gain collapse** specifically returns very limited established usage; some control-theory pedagogy uses it informally for the "gain goes to zero" case.
- **Mode collapse** in GANs is the closest catastrophic-pathology compound (analogous structure: a system collapses into a degenerate mode) but different domain.

Verdict: **minor.** The Kalman-gain parent frame is the right adjacency and
the compound "gain collapse" reads naturally given that frame. No specific
term is claimed. The mode-collapse echo in GANs is informative not colliding.
No rename.

### 41. **evidence starvation** — clean

ASF: downstream edges in a chain receive fewer tests because upstream
edges must succeed first (`#der-chain-confidence-decay`).

External usage:
- "Evidence starvation" is occasionally used in evidence-based-medicine writing (information starvation, evidence drought) but no established technical term.
- **Bayesian evidence / marginal likelihood** is the formal statistical sense of "evidence" — orthogonal.
- "Starvation" in scheduling / OS theory (resource starvation) is the closest computer-science usage — different domain.

Verdict: **clean.** The compound is suggestive and uncollided. The
EBM and OS-scheduling adjacencies don't compete for the technical frame. No
rename, no disambiguation needed.

### 42. **effective disturbance** — moderate

ASF: $\rho_{\text{eff}}$ — the unifying term for the max-with-zero
construction in the sector-persistence template.

External usage:
- **Effective disturbance** in **robust control / disturbance rejection** is a recognized compound — the disturbance that the controller effectively sees after model uncertainty and feedback are accounted for. Various papers in $H_\infty$, $\mu$-synthesis, and adaptive control use the compound.
- **Disturbance rejection** as a control-theory primitive is foundational.

Verdict: **moderate.** The robust-control usage is the parent frame and ASF's
$\rho_{\text{eff}}$ is conceptually compatible — it's the disturbance after
the agent's adaptation has absorbed what it can. No territorial step-on; the
compound is conventional in control theory. Recommendation: keep; ensure the
first-encounter discipline cites the robust-control lineage. No rename.

### 43. **causal information yield (CIY)** — clean

ASF segment: `01-aat-core/src/def-causal-information-yield.md`. ASF coinage —
the information gained from causal interventions, distinguishing
intervention-yield from observational mutual information.

External usage:
- **Information gain** in decision theory / active learning — the established term for similar quantities (mutual information between query and target).
- **Causal information** appears in causal-inference literature (Janzing-Schölkopf, Ay-Polani) but as a generic adjective, not as a specific compound.
- "Causal information yield" specifically does not appear as an established term.
- The acronym **CIY** is not collision-loaded in adjacent technical fields (a few unrelated organizational acronyms).

Verdict: **clean.** The compound is ASF's, the connection to information-gain
in decision theory is informative not colliding, and the acronym is
unloaded. Recommendation: keep; first-encounter discipline cites Pearl
(intervention) and Lindley/Shannon-style information-gain as parent frames.
No rename.

### 44. **inevitability core** — clean

ASF: framing for the ~15 segments where a Categorical-Inevitability claim is
plausible (per FORMAT.md three-rings discussion).

External usage:
- "Inevitability" as a generic philosophical / political term — ubiquitous, not technical.
- "Inevitability core" returns essentially nothing in technical literature.
- "Core" as a modifier (kernel, core theorems, core results) is generic across mathematics.

Verdict: **clean.** Compound is ASF's, no collision, no specific
disambiguation needed.

### 45. **self-referential closure** — moderate

ASF: thermodynamic-stability-of-self-modifying-agent claim in logogenic
context (agent maintaining its own codebase).

External usage:
- **Autopoiesis** (Maturana & Varela 1972): the foundational
self-referential-closure concept in biology / cybernetics / cognitive
science. *Operational closure* and *organizational closure* are the standard
terms in autopoiesis literature. The compound "self-referential closure"
is a near-rendering and inherits the autopoietic gravity.
- **Self-reference** in logic (Tarski, Gödel, Kleene's recursion theorem,
Quine) — different sense, but same name-string family.
- **Closure** in algebra / topology — orthogonal here.

Verdict: **moderate.** The autopoiesis adjacency is strong and
*substantively related* — Maturana-Varela autopoiesis is exactly about
self-maintaining living systems and the compound's intuition transfers.
The brief flags autopoiesis in the *exclusion list* (adopted-with-citation),
so the project is already aware of the lineage. The name "self-referential
closure" is more *suggestive* of the autopoietic concept than the autopoiesis
literature itself uses. Recommendation: keep; cite Maturana-Varela on first
encounter; if the segment can position itself as the engineering-architectural
restriction of operational closure, that's the cleanest move. No rename.

### 46. **directional fidelity** — clean

ASF: from `#der-gain-sector-bridge` (B1) — the correction must point
at-least-roughly toward reality ($\delta^T H g(\delta) \geq c|\delta|^2$).

External usage:
- **Fidelity** in signal processing, communications, quantum information — established but generic.
- **Directional fidelity** specifically returns very limited established usage; a few signal-processing papers use it loosely (directional accuracy of beamforming, etc.).
- **Sector condition** in control theory (Lurie, Popov absolute stability) is the parent technical lineage and uses *sector* / *sector-bounded* but not *directional fidelity*.

Verdict: **clean.** The compound is ASF's framing for the sector-condition
content and doesn't collide with established usage. The geometric intuition
(direction of correction matters) transfers cleanly. No rename, no
disambiguation needed.

### 47. **Pearl-blanket reading** — clean

ASF: explicit adoption of Bruineberg et al. 2022 distinction between
Pearl-blanket (technical conditional-independence) and Friston-blanket
(metaphysical demarcation) readings of the Markov-blanket apparatus.

External usage:
- **Pearl-blanket / Friston-blanket** distinction is established by Bruineberg,
Dolega, Dewhurst & Baltieri 2022 (*Behav. Brain Sci.* 45:e69, "The Emperor's
New Markov Blankets"). ASF correctly cites this. The distinction is
adopted-with-citation, which the brief explicitly puts out of scope for
collision concerns.
- **Markov blanket** itself is Pearl's original term (Pearl 1988).

Verdict: **clean.** ASF is using established terminology from the Bruineberg
critique with citation; this is exactly what adoption-with-citation
discipline calls for. No rename, no disambiguation beyond what the segment
already does.

Sources: [Bruineberg et al. 2022, "The Emperor's New Markov Blankets"](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/emperors-new-markov-blankets/E5793521A0B0B5F7B7C8E8E1DA8B6D4D).

## Additional flags (terms not in the original 47)

A few terms surfaced during the master-list reading that look worth flagging
even though they weren't on the brief's list:

### A1. **bathtub model** (Walton's plain-language analog)

ASF master list, weight +2: Alan Walton's bathtub gloss for the persistence
condition (water = belief-reality gap, faucet = rate of change in reality,
drain = learning rate, container = adaptive reserve). The CLAUDE.md
Feynman-criterion section names this as the canonical example.

External usage:
- **Bathtub model / bathtub problem** is a *very* standard pedagogical /
introductory example across multiple fields: stocks-and-flows in system
dynamics (Forrester), introductory differential equations (the leaking
tank), reliability engineering (the bathtub curve — failure rate vs. time).
The "bathtub curve" specifically is foundational in reliability and is the
dominant established meaning of "bathtub model."

Verdict: **moderate to severe** if elevated to canonical status. The
bathtub-as-analog usage in pedagogy (system dynamics) is fine and is what
ASF means; but "the bathtub model" as a *named* canonical analog will
collide with the reliability-engineering bathtub curve and the system-dynamics
bathtub. Recommendation: keep "bathtub" as a casual *gloss* / *analog* but do
not promote "bathtub model" to a canonical compound — call it "Walton's
bathtub analog" or "the bathtub gloss" to keep the playful register and
avoid the established "bathtub curve" / "bathtub model" gravity.

### A2. **diagnostic gap matrix**

ASF master list, weight +9: the 2×2 table of satisfaction gap × control
regret × goal attainability.

External usage:
- **Gap analysis matrix / gap matrix** in management consulting / business
strategy is a standard 2×2 framework type.
- **Diagnostic matrix** as a compound is generic across medicine (differential
diagnosis tables) and engineering.

Verdict: **minor.** The compound is generic enough that no specific term is
claimed; the management-consulting "gap matrix" association is benign.
No rename.

### A3. **terminal alignment gap**

ASF master list, weight +9: the fourth diagnostic when end conditions are met
but the objective remains unsatisfied.

External usage:
- **Alignment** in AI safety is a heavy term (AI alignment, value alignment,
alignment problem). "Alignment gap" appears occasionally in AI-alignment
writing without a specific established meaning.
- **Terminal** as a modifier is generic.

Verdict: **moderate.** The AI-alignment gravity is real and "terminal
alignment gap" reads as an AI-safety-flavored compound. ASF's usage is
narrower (a specific 2×2 cell) and the AI-safety reading would be off-target.
Recommendation: if elevated to canonical, distinguish from AI-safety
alignment-gap usage at first encounter. Otherwise minor.

### A4. **resonance** (in the logogenic / Class 1 macro-agent sense)

Cognitive fusion's parent concept per master list: "Resonance as mutual
information approaching channel capacity $R_{\text{spec}}$, forming a Class 1
macro-agent."

External usage:
- **Adaptive Resonance Theory (ART)** — Grossberg 1976 onward. "Resonance" in
ART is a specific technical term: bottom-up activation matches top-down
expectation. Heavily established in NN-learning literature and connects
directly to the stability-plasticity dilemma flagged earlier.
- **Resonance** in physics / signal processing — orthogonal but ubiquitous.

Verdict: **moderate.** If "resonance" is being used as a canonical name
(rather than just descriptive prose) in `03-llm-core/`, the Grossberg
ART adjacency is strong enough to need disambiguation. ASF's usage
(mutual-information saturation between two agents) is structurally different
from ART resonance (matching pattern between feature and category layers).
Recommendation: if "Resonance" is canonical, cite ART on first encounter.

### A5. **honesty as architecture** vs. **HHH** lineage already handled in #29.

## Closing notes

- The clearest *severe* cases are **artificial hippocampus** (real
medical-device program with active human trials, Berger lab USC; concrete
demonstration in 2018 with Hampson et al. at Wake Forest) and **cognitive
fusion** (entrenched ACT-therapy term, Hayes et al. 1999 onward, central in
the Hexaflex psychological-flexibility model). These are the strongest
rename / disambiguate-substantially candidates and have the structural
shape of the ACT precedent (string identity with established term in active
adjacent literature).
*Adaptive cycle* is severe by collision (Holling r/K/Ω/α is the dominant
established meaning across resilience ecology and panarchy theory); the
action depends on whether ASF's phase structure is genuinely incompatible
with Holling's. If compatible, treat as adoption-with-citation; if not,
rename.
*Proprium* is moderate-severe but resolvable by Allport citation —
Allport's primacy is a 70-year-old uncontested reference, and Firmatum
appears not to have cited it; closing that gap at the segment level handles
the collision.
*Shared intent* is severe by gravity-of-Tomasello and resolvable only by
substantive Discussion-section disambiguation rather than a one-line cite.
- The list is otherwise well-curated. Most candidates carry adjacent-term
gravity that is addressable by first-encounter citation — the
*acknowledgment* discipline rather than rename.
- The bar feels right where the brief set it. The biggest deviation is that
"semantic gravity" (will the reader silently swap meanings?) deserves
slightly more weight than "territorial step-on" (is the term already
claimed?) — most of this list's risk is in the gravity dimension, not the
territorial one. The action it implies (cite-and-distinguish on first
encounter) is the same in both cases, but the framing of *why* may matter
for how segments and framing-vocabulary materials handle it.
- The Feynman-criterion / plain-language brief discipline (CLAUDE.md
Working Conventions) is itself a hedge against semantic-import mismatch:
if the everyday analog the term reaches for is load-bearing in the Brief,
collision-by-frame-import becomes legible at writing time rather than at
audit time. Worth noting because it's already the project's discipline.
