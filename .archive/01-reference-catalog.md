# AAD Reference Catalog

**Status**: Working catalog of prior art and related work. Each entry needs a detailed read and assessment of relevance to AAD. Entries marked [UNREAD] have not been examined beyond abstract/search-result level. Entries marked [READ] have been read in some detail. Entries marked [CORE] are foundational references that AAD builds on or must position against.

---

## Foundational — AAD's Own Lineage

### [CORE] [READ] Temporal Feedback Theory (TFT)
- **Location**: priors/tft/
- **What**: Formal theory of adaptive agents under uncertainty. The adaptive feedback loop: mismatch, gain, tempo, persistence, adversarial dynamics.
- **Relationship to AAD**: Adaptive-systems foundation, now subsumed by AAD.
- **Key documents**: TF-00 through TF-11, Appendices A-G

### [CORE] [READ] Temporal Software Theory (TST)
- **Location**: priors/tst/
- **What**: Temporal optimization target for software engineering. 12 theorems on specification bounds, change investment, coherence-coupling, etc.
- **Relationship to AAD**: Software domain instantiation. Needs regrading — real content is an optimization objective, not a theorem of engineering.
- **Key documents**: T-01 through T-12, via-tft/ directory

### [CORE] [READ] TST-via-TFT Mapping
- **Location**: priors/tst/via-tft/
- **What**: Mapping of TST onto TFT foundations. Three-part tempo decomposition, causal extensions, simulation proposals, reformulated sketch.
- **Relationship to AAD**: Prototype domain instantiation; demonstrates how AAD's formalism applies to a specific domain.

### [CORE] [READ] Goal/Intent Gap Analysis
- **Location**: priors/tft/scratch/15-goal-intent-gap.md
- **What**: The document that identified the structural gap and proposed the restructuring into AAD.
- **Relationship to AAD**: The founding analysis. Seneca, the PID evidence, three mismatch signals, M_t/G_t parallel, theoretical architecture.

---

## Direct Competitors / Adjacent Theories

### [READ — assessed in 02-prior-art-assessment.md] Hafez et al., "A Mathematical Theory of Agency and Intelligence" (Feb 2026)
- **URL**: https://arxiv.org/abs/2602.22519
- **What**: Information-theoretic formalization of agency and intelligence.
  Introduces "bipredictability" (P) — measures how much information a system shares between observations, actions, and outcomes. Distinguishes agency (capacity to act on predictions) from intelligence (learning from interaction, self-monitoring, adapting scope). P bounded: unity in quantum systems, <=0.5 in classical, lower with agency.
- **Relationship to AAD**: Most direct recent competitor for "mathematical theory of agency." Likely complementary — their measure (bipredictability) might map to TFT quantities (eta*, T). Their distinction between agency and intelligence might parallel AAD's adaptive-systems vs. purposeful-agency distinction. MUST READ to understand overlap and differentiation.
- **Key question**: Does their formalism handle goals/intent? From the abstract, it seems focused on the observation-action-outcome loop (TFT territory) not the goal/intent layer.

### [READ — assessed in 02-prior-art-assessment.md] "Agentic AI Needs a Systems Theory" (2025)
- **URL**: https://arxiv.org/html/2503.00237v1
- **What**: Argues that agentic AI development requires a holistic, systems-theoretic perspective. A call for foundations.
- **Relationship to AAD**: Articulates the void that AAD aims to fill. Read to understand what they think is missing and whether AAD addresses it.
- **Key question**: What specific gaps do they identify? Do they point toward the goal/intent layer or focus on different concerns?

### [READ — assessed in 02-prior-art-assessment.md] IBM, "Foundations of Agentic Systems Theory" / FAST Workshop (AAAI 2026)
- **URL**: https://research.ibm.com/publications/foundations-of-agentic-systems-theory
- **Workshop**: https://fast-workshop.github.io/ (17 papers presented)
- **What**: IBM-organized workshop at AAAI 2026. The IBM paper itself is a position paper calling for a systems theory, not providing one. Workshop papers are mostly narrow/applied.
- **Relationship to AAD**: They articulate the void AAD fills. Not a competitor — a call-to-arms. Two workshop papers worth reading: Mohan "From Agentic AI to Autonomous Agents" and Bagiński & Jha "Leapsight."

### [UNREAD — MEDIUM PRIORITY] "Are Agents Just Automata?" (2025)
- **URL**: https://arxiv.org/html/2510.23487v1
- **What**: Establishes formal equivalence between agentic AI architectures and Chomsky hierarchy. Memory architecture determines computational power: simple reflex = FA, hierarchical = PDA, read/write memory = TM.
- **Relationship to AAD**: Interesting but orthogonal — this is about computational power classes, not dynamics. AAD's agents can be at any level of the Chomsky hierarchy; the theory describes their *adaptive dynamics* regardless.

### [UNREAD — MEDIUM PRIORITY] "The Term 'Agent' Has Been Diluted Beyond Utility and Requires Redefinition" (2025)
- **URL**: https://arxiv.org/html/2508.05338v1
- **What**: Argues for more precise definitions of "agent" in AI.
- **Relationship to AAD**: AAD's continuum (adaptive system -> purposeful agent) may provide the precision they're calling for. Read to see if AAD's definitions align with or improve on their proposals.

---

## Classical Foundations

### [CORE] [READ — via TFT] Pearl, *Causality* (2009)
- **What**: The causal hierarchy (associational, interventional, counterfactual).
  do-calculus. Structural causal models.
- **Relationship to AAD**: TF-02's axiom. Pearl's three levels are load-bearing throughout. The causal extensions in TST-via-TFT build directly on this.

### [CORE] [READ — via TFT] Boyd, "Destruction and Creation" (1976) and OODA
- **What**: The OODA loop. Orient as the most important stage. Implicit guidance and control. The effects spiral. Tempo advantage.
- **Relationship to AAD**: Boyd's Orient = where M_t and G_t interact. AAD's key claim: TFT captured the Observe and part of Orient; AAD captures the full Orient (including goal revision) and the directed action loop.

### [READ — partially, via TST-via-TFT] Clausewitz, *On War*
- **What**: Friction (the gap between plan and reality). The culminating point.
  War as continuation of politics (war has PURPOSE beyond itself).
- **Relationship to AAD**: Clausewitz's "friction" = delta_epistemic + delta_feasibility. "War is the continuation of politics" = the agent's actions serve a purpose (G_t) beyond the actions themselves.

### [UNREAD — should read more carefully] Bungay, *The Art of Action* (2011)
- **What**: Directed opportunism. The alignment model. The three gaps (knowledge, alignment, effects). Auftragstaktik / mission command.
- **Relationship to AAD**: Direct source for shared intent formalization.
  Bungay's three gaps may map cleanly to AAD's three mismatch signals.
  The alignment gap in particular may be the delta between commander's G_t and subordinate's G_t.

### [CORE] BDI — Belief-Desire-Intention (Rao & Georgeff, 1991-1995)
- **URL**: https://cdn.aaai.org/ICMAS/1995/ICMAS95-042.pdf (BDI: Theory to Practice)
- **What**: The foundational agent architecture. Beliefs = world model, Desires = goals, Intentions = committed plans. Formalized in modal logic (BDICTL).
- **Relationship to AAD**: AAD can be seen as providing the *dynamics* that BDI lacks. BDI says agents have beliefs, desires, and intentions. AAD says how those beliefs and desires update, interact, and drive action over time. BDI is the anatomy; AAD is the physiology.
- **Key limitation (from literature)**: "BDI agents lack any specific mechanisms within the architecture to learn from past behavior and adapt."

### [UNREAD — MEDIUM PRIORITY] "The Belief-Desire-Intention Ontology" (2025)
- **URL**: https://arxiv.org/html/2511.17162v1
- **What**: Recent attempt to update BDI as an ontology for modern AI systems.
- **Relationship to AAD**: Check if they've addressed BDI's dynamics gap.

### [CORE] [READ — via TFT] Kalman, "A New Approach to Linear Filtering" (1960)
- **What**: The Kalman filter. Optimal state estimation. The innovation (mismatch) signal. TFT's Appendix C worked example.
- **Relationship to AAD**: The purest case of M_t dynamics (all epistemic, no goal). Combined with LQR, it becomes LQG — the simplest case of M_t + G_t with the separation principle.

### [CORE] [READ — via TFT] Feldbaum, "Dual Control Theory" (1960)
- **What**: The insight that actions serve both control (exploitation) and identification (exploration). The original exploration-exploitation formalism.
- **Relationship to AAD**: Foundational for TF-08. Dual control is the interaction point between M_t dynamics (identification) and G_t pursuit (control). In AAD terms: actions simultaneously close delta_epistemic and delta_goal.

### [CORE] Friston, "The Free Energy Principle" (various, 2006-2025)
- **What**: Active inference. Prior preferences as goals. Free energy minimization as a unified objective for perception and action.
- **Relationship to AAD**: The most direct theoretical competitor for unifying adaptation and purpose. AAD's positioning: causal feedback dynamics are more transparent and measurable than free energy; AAD explicitly handles adversarial dynamics, shared intent, and multi-agent coupling; AAD maps to Pearl's causal hierarchy where active inference primarily operates at Level 1.

### Ashby, "Requisite Variety" / *Design for a Brain* (1952/1960)
- **What**: The law of requisite variety — a controller needs as much variety in its responses as the disturbances it faces.
- **Relationship to AAD**: Complementary to the persistence condition. Requisite variety is about the action space needed for goal-pursuit (delta_goal closure). The persistence condition is about the observation/update capacity needed for reality-tracking (delta_epistemic closure). Together they define minimum viable agency.

### [READ — via TFT] Tishby, "The Information Bottleneck" (2000)
- **What**: Optimal compression that retains predictive power. Rate-distortion theory for learning.
- **Relationship to AAD**: TF-03's compression objective for M_t. AAD extends with a parallel compression objective for G_t (compress to prescribe, not predict — the Auftragstaktik IB).

---

## Recent Surveys and Frameworks (2024-2026)

### [UNREAD — LOW PRIORITY] "The Rise of Agentic AI: Review of Definitions, Frameworks..." (2025)
- **URL**: https://www.mdpi.com/1999-5903/17/9/404
- **What**: Comprehensive survey of agentic AI definitions, architectures, etc.
- **Relationship to AAD**: Useful for understanding the landscape. Not competing at the theoretical level but may cite relevant work.

### [UNREAD — LOW PRIORITY] "From the Logic of Coordination to Goal-Directed Reasoning" (2025)
- **URL**: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1728738/full
- **What**: Describes the "agentic turn" in AI. Four enduring properties:
  intentionality, autonomy, adaptivity, sociality.
- **Relationship to AAD**: AAD formalizes all four. Check if their "intentionality" treatment goes beyond BDI's.

### [UNREAD — LOW PRIORITY] "Agentic AI Frameworks: Architectures, Protocols, and Design Challenges" (2025)
- **URL**: https://arxiv.org/html/2508.10146v1
- **What**: Technical survey of agentic AI frameworks.
- **Relationship to AAD**: AAD is foundational theory, not a framework.
  Useful for understanding implementation landscape.

### [UNREAD — MEDIUM PRIORITY] "AI Agents vs. Agentic AI: A Conceptual Taxonomy" (2025)
- **URL**: https://arxiv.org/html/2505.10468v4
- **What**: Distinguishes AI Agents from Agentic AI. Key distinction: Agentic AI involves multi-agent collaboration, dynamic task decomposition, persistent memory, coordinated autonomy.
- **Relationship to AAD**: AAD's multi-agent dynamics (from TFT Appendix F + shared intent) may provide the theoretical foundation for what they describe architecturally.

---

## Strategic / Military Theory

### [UNREAD — MEDIUM PRIORITY] Osinga, *Science, Strategy and War: The Strategic Theory of John Boyd* (2007)
- **What**: The most thorough academic treatment of Boyd's strategic theory.
- **Relationship to AAD**: Essential for grounding AAD's Boyd connection in the primary source literature.

### [UNREAD — should eventually read] Bungay, *The Art of Action* (2011)
- **What**: Directed opportunism, alignment model, three gaps. Translates Auftragstaktik into modern organizational context.
- **Relationship to AAD**: Primary source for shared intent formalization.

### [UNREAD — should eventually read] Van Creveld, *Command in War* (1985)
- **What**: Historical analysis of command systems and the evolution from detailed orders to mission command.
- **Relationship to AAD**: Historical grounding for the shared-intent compression principle.

---

## Philosophy / Foundations

### Seneca, *Epistulae Morales*, LXXI
- **What**: "If a man knows not to which port he sails, no wind is favorable."
- **Relationship to AAD**: The founding aphorism. Captures the goal/intent gap in one sentence.

### [UNREAD — MEDIUM PRIORITY] Rindova et al., "Shaping Markets Through Temporal, Constructive, and Interactive Agency" (2020)
- **URL**: https://pubsonline.informs.org/doi/10.1287/stsc.2020.0110
- **What**: Three forms of agency: constructive, temporal, interactive.
  Temporal agency = agents' use of temporal framing to envision new possibilities.
- **Relationship to AAD**: Their "temporal agency" concept may resonate with AAD's goal-revision dynamics. Read to see if there's deeper connection.

---

## Reading Priority Queue

**Immediate (before writing any formal AAD documents):**
1. Hafez et al., "A Mathematical Theory of Agency and Intelligence" — direct competitor
2. "Agentic AI Needs a Systems Theory" — the void we're filling
3. IBM "Foundations of Agentic Systems Theory" — competing foundations attempt

**Soon (before finalizing positioning):**
4. BDI: Rao & Georgeff 1995 — understand exactly what BDI provides and doesn't
5. "The Term 'Agent' Has Been Diluted" — definitional landscape
6. "BDI Ontology" (2025) — has BDI been updated?

**Before domain instantiations:**
7. Bungay, *The Art of Action* — shared intent source
8. Osinga, *Science, Strategy and War* — Boyd primary source

**Background:**
9. Recent surveys (for landscape awareness, not theoretical depth)
10. Rindova et al. — temporal agency in strategy literature
