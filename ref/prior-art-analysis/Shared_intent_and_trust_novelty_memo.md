# Shared intent and trust novelty memo

##### [**Undermind**](https://undermind.ai)

---


## Table of Contents

- [Shared intent and trust novelty memo](#shared-intent-and-trust-novelty-memo)
  - [Overall judgment](#overall-judgment)
  - [Claim under review](#claim-under-review)
  - [Prior art by claim component](#prior-art-by-claim-component)
  - [What the prior art already establishes](#what-the-prior-art-already-establishes)
  - [Where AAT seems genuinely new](#where-aat-seems-genuinely-new)
  - [Stress tests that matter most](#stress-tests-that-matter-most)
    - [The hierarchy claim needs real support](#the-hierarchy-claim-needs-real-support)
    - [Shared intent must be more than generic latent communication](#shared-intent-must-be-more-than-generic-latent-communication)
    - [Competence and alignment must remain distinct in the math](#competence-and-alignment-must-remain-distinct-in-the-math)
    - [The robust uptake rule should be framed as a structural fit, not a reinvention](#the-robust-uptake-rule-should-be-framed-as-a-structural-fit-not-a-reinvention)
    - [The unified package is the real claim](#the-unified-package-is-the-real-claim)
  - [Largest implications if the claim holds](#largest-implications-if-the-claim-holds)
  - [Potential field impact if the claim holds](#potential-field-impact-if-the-claim-holds)
  - [Venue strategy](#venue-strategy)
    - [Best-fit venues by framing](#best-fit-venues-by-framing)
    - [Recommended path](#recommended-path)
    - [Practical ranking for this project](#practical-ranking-for-this-project)
  - [Submission snapshot](#submission-snapshot)
  - [Bottom line](#bottom-line)
  - [References](#references)

# Shared intent and trust novelty memo

## Overall judgment

The literature already contains strong antecedents for each half of the AAT story, but mostly in separate traditions. Information bottleneck, rate-distortion, and decentralized-control work show that communication under bandwidth limits should preserve task-relevant structure rather than raw history \[Nay12, Tan15b, Fox16c, Wan19e\]. Trust theory separately shows that rational uptake of testimony or advice depends on both competence and intent, and that robust decision rules often discount or clip advice from potentially misaligned sources rather than taking it at face value \[Sha12b, Dwo26\].

What does not appear to be already present in the project literature is the full AAT package suggested by AAT-chapter-12:

- shared intent as the information-bottleneck compression of the sender’s purposeful state
- a communication hierarchy in which objective sharing should dominate strategy sharing, which should dominate model sharing, under bandwidth limits
- a communication-gain rule that discounts uptake separately for channel noise, source competence, and source alignment
- a unified frame connecting compressed mission-style communication to downside-sensitive trust

That package looks like the real novelty opportunity. The ingredients are not new, but their unification appears materially stronger than any single prior strand.

## Claim under review

In the project files, the claim is stronger than “communicate compactly” and stronger than “trust carefully.”

AAT-chapter-12 defines shared intent as the information-bottleneck compression of the sender’s full purposeful state into the minimal sufficient statistic for coordinated action. It then proposes the Auftragstaktik principle: under bandwidth constraints, communication should prioritize objective sharing over strategy sharing over model sharing.

The same chapter then adds a separate but connected claim about trust. Communication gain should be discounted not only by ordinary channel noise, but also by uncertainty about source competence and uncertainty about teleological alignment. This makes communication uptake asymmetric and safety-sensitive by design.

Read together, the project is not just saying that messages should be compressed and informants screened. It is proposing one integrated posture: communicate purpose in compressed form, and evaluate incoming guidance through distinct epistemic and teleological uncertainties.

## Prior art by claim component

| AAT component | Nearest prior art | Match | Novelty read |
|:---|:---|---:|:---|
| Task-relevant communication as compression rather than raw sharing | \[Nay12\], \[Tan15b\], \[Fox16c\], \[Wan19e\] | Strong | Low novelty by itself |
| Shared intent as compressed purposeful state | partial ancestry in decentralized control and MARL communication \[Nay12\], \[Wan19e\] | Partial | Moderate to high novelty |
| Bandwidth-constrained communication hierarchy | organizational and control antecedents, but no exact ordering found | Weak to partial | High potential novelty |
| Trust decomposed into competence and intent or alignment | \[Sha12b\] and neighboring trust models from the search | Moderate to strong | Low to moderate novelty by itself |
| Conservative downside-sensitive uptake of advice | \[Dwo26\] and adjacent robust-trust lineage | Strong | Low novelty by itself |
| Unified formalism linking mission-style compressed communication with competence-alignment-discounted trust | not found as a single package in the retrieved papers | Weak | Highest novelty candidate |

## What the prior art already establishes

The strongest communication-side ancestry comes from decentralized control and information-constrained control. \[Nay12\] shows that partial-history-sharing control problems admit a common-information state that functions as a sufficient statistic. This is powerful support for AAT’s general stance that what should be shared is not raw history but a compressed task-relevant object. \[Tan15b\] and \[Fox16c\] give the information-theoretic control side of the story: the relevant resource is directed information or information rate, and optimal architectures trade off control performance against communication burden. Those papers are not about “shared intent” in AAT’s sense, but they provide a serious mathematical template for compressed coordination.

\[Wan19e\] is the closest modern AI-side precursor. It applies the information bottleneck principle to multi-agent communication, explicitly learning low-entropy messages that preserve task-relevant information under bandwidth constraints. This is an important baseline because it shows that task-relevant compact communication is not merely a control-theory idea. Still, the paper does not claim that what should be compressed is the full purposeful state in AAT’s sense, nor does it derive the objective-before-strategy-before-model hierarchy.

On the trust side, \[Sha12b\] is a strong conceptual anchor because it explicitly separates knowledgeability from helpfulness and mal-intent. That supports AAT’s insistence that competence and alignment should not be collapsed into one reliability score. \[Dwo26\] is the strongest retrieved match for the uptake rule itself. It proves that robust decision-making with a potentially misaligned adviser yields a trust-region strategy in belief space: reports inside a safe region are used directly, while reports outside are clipped to the nearest trusted boundary. This is very close in spirit to AAT’s claim that trust should be evaluated asymmetrically and conservatively rather than by naive expectation alone.

What is missing in the prior art is a clean bridge between these two lineages. The communication papers mostly do not model trust in a competence-versus-alignment decomposition. The trust papers mostly do not ask what kind of purposeful content should be communicated under bandwidth limits. That gap is where AAT appears most promising.

## Where AAT seems genuinely new

AAT looks strongest where it turns two separate literatures into one architecture of coordination.

First, the project does not merely say that task-relevant messages should be compressed. It says that what is being compressed is the sender’s purposeful state. That is stronger than “send an efficient message” and more structured than standard latent-communication work. It ties communication directly to objective and strategy state.

Second, the Auftragstaktik hierarchy looks like a genuine novelty candidate. The idea that communication should privilege higher-level mission content over lower-level detail has organizational and military ancestry, and there are clear mathematical predecessors in delegation and sufficient-information theory. But the exact ordering “objectives before strategies before models” does not appear to be explicitly proved in the retrieved literature. If AAT can really derive that ordering from communication constraints and timescale structure, it has a real contribution.

Third, the communication-gain rule is stronger than many trust models because it distinguishes three separate filters on incoming advice:

- channel quality
- source competence
- source alignment

That decomposition is cleaner than a generic trust score, and it fits the architecture of agent communication well.

Fourth, the deepest novelty candidate is the unification itself. The project’s distinctive move is not any one of these ingredients in isolation, but the claim that efficient mission-style communication and robust trust are two sides of the same coordination problem. I do not see that package already present in the retrieved literature.

## Stress tests that matter most

### The hierarchy claim needs real support

This is the key pressure point. The literature supports compressed sufficient communication, but not obviously the exact ordering of content types. AAT will need to show why objectives have better bandwidth-adjusted coordination value than strategies, and strategies better than models, under stated conditions. Otherwise the result will read as appealing doctrine rather than theorem.

### Shared intent must be more than generic latent communication

Modern MARL communication papers already learn compact messages \[Wan19e\]. AAT only gets a strong novelty claim if it makes clear what is distinctive about compressing purposeful state specifically, rather than arbitrary useful latent state.

### Competence and alignment must remain distinct in the math

Many trust systems blur these. AAT’s advantage is precisely that it keeps them separate. That distinction should stay explicit and load-bearing; otherwise the trust side will collapse into a familiar reputation or source-reliability model.

### The robust uptake rule should be framed as a structural fit, not a reinvention

\[Dwo26\] is a serious nearby result. AAT should not sound as if it invented conservative uptake of misaligned advice. The better claim is that it embeds a robust-trust posture into a broader communication-and-coordination architecture.

### The unified package is the real claim

If the paper is written as “here is an information bottleneck communication result” plus “here is a trust discount rule,” the novelty will look fragmented. The stronger claim is that these are one posture: compress the right thing, then trust it in the right way.

## Largest implications if the claim holds

| Area | Why the claim matters | Closest literature it would move beyond |
|:---|:---|:---|
| Multi-agent coordination | It would connect compressed communication directly to purposeful-state alignment rather than only to latent-message efficiency | \[Nay12\], \[Wan19e\] |
| Human-AI and agent-agent command structures | It would provide a formal basis for mission-style delegation under bandwidth constraints | control, team theory, and organizational antecedents |
| Trust in advisory systems | It would separate competence from alignment inside one communication architecture | \[Sha12b\], \[Dwo26\] |
| Safety of decentralized collectives | It would justify conservative uptake of strategically important advice rather than naive aggregation | \[Dwo26\] |

The largest direct effect would likely be on the design of coordination protocols for agent systems. The paper would suggest that the right question is not simply “how many bits should agents exchange,” but “which layer of purposeful state should those bits represent.” That is a more useful design question.

The second major effect would be on trust and delegation. If competence and alignment are kept separate, then systems can reason more honestly about when advice is useful but dangerous, knowledgeable but misaligned, or aligned but noisy.

The third effect would be on theory. AAT could provide a missing bridge between the control-theoretic communication literature and the trust literature, which currently feel adjacent but not unified.

## Potential field impact if the claim holds

The impact ceiling is meaningful because the paper could unify two practically important but usually separate problems: what to communicate and when to trust what is communicated.

At the modest end, the paper would still matter as a strong synthesis. It would connect information bottleneck communication, sufficient-information control, epistemic trust, and robust trust into one framework for coordination under uncertainty.

At the stronger end, the paper could influence how agent systems are built. It suggests that mission-style communication and robust trust are not organizational heuristics layered on top of a technical system; they are consequences of the same structural problem of communication under bandwidth and misalignment.

The biggest direct effect would likely be on multi-agent and human-AI coordination design. If the ordering over objectives, strategies, and models holds, then protocol design could become much more principled. Instead of defaulting to raw state sharing or verbose plan exchange, designers would have a reason to privilege compressed purpose.

The second major effect would be on advisory AI and delegation. A formal competence-versus-alignment split, combined with conservative uptake, would help clarify when advice should be clipped, ignored, or followed.

The third effect would be on theory transfer across fields. This topic naturally touches control, MARL, organizational design, and trust theory. A clean unification could travel well.

A practical impact ranking would be:

- moderate impact if the paper is received as a strong synthesis of communication and trust literatures
- high impact if the communication hierarchy is seen as technically new and useful
- very high impact if the unified communication-plus-trust posture becomes standard language for coordinated agent systems

## Venue strategy

### Best-fit venues by framing

The right venue depends on whether the paper is framed mainly as a coordination theorem, a learning-and-communication result, or an alignment-and-governance result.

If the paper is framed as a broad AI theory contribution about coordination, communication, and trust in agent systems, Artificial Intelligence journal is likely the strongest single home. AIJ explicitly welcomes broad advances in AI, including multi-agent systems, planning and action, reasoning under uncertainty, and ethical AI. That breadth fits the cross-cutting nature of this argument. [AIJ aims and scope](https://www.sciencedirect.com/journal/artificial-intelligence)

If the paper is framed more as a mathematically sharp learning-and-communication result, TMLR is plausible. TMLR explicitly invites theoretical studies, new analytical frameworks, and work on the design and behavior of learning in intelligent systems. The fit is strongest if the paper emphasizes information bottleneck communication, limited-bandwidth learning, and formal trust-updating rules rather than the broader organizational interpretation. [TMLR overview](https://www.jmlr.org/tmlr/) [TMLR editorial policies](https://www.jmlr.org/tmlr/editorial-policies.html)

If the paper is framed around alignment, oversight, delegation, and trustworthy coordination, AIES is a strong conference fit. AIES 2026 explicitly welcomes value alignment, human-AI interaction, collaboration and teaming, control and scalable oversight, and broader ethical and societal implications. It is especially attractive if the trust and delegation implications are foregrounded. The current timing matters: the AIES 2026 submission deadline is May 21, 2026. [AIES 2026 CFP](https://www.aies-conference.com/2026/call-for-papers/)

If the paper is framed as a general-intelligence coordination theory, AGI is also a good fit. The AGI call welcomes work on collaborative intelligence, multi-agent interaction, planning, reasoning, and broader implications of AGI. The deadline for AGI 2026 was extended to April 20, 2026, so that cycle is already closed. [AGI Conference CFP](https://agi-conference.org/call-for-papers)

### Recommended path

The cleanest publication strategy is:

1.  Write the full cross-disciplinary version for Artificial Intelligence journal.
2.  If the technical communication result is the sharpest core, prepare a tighter version for TMLR.
3.  If the trust, delegation, and oversight implications are central, use AIES as the conference-facing venue.

### Practical ranking for this project

My venue ranking for this exact project is:

- Artificial Intelligence journal
- TMLR
- AIES
- AGI Conference

The fork is simple:

- if the main claim is “this is a unified theory of purposeful communication and trust,” favor Artificial Intelligence journal
- if the main claim is “this is a technical information-bottleneck and update-rule result,” favor TMLR
- if the main claim is “this changes how delegation, oversight, and trustworthy coordination should be built,” favor AIES

## Submission snapshot

This venue advice is time-sensitive. The conference dates, positioning, and deadlines above are a snapshot as of May 21, 2026.

## Bottom line

The weak version of this memo is not novel. The field already knows that communication under bandwidth limits should be compressed and task-relevant, and that advice from potentially misaligned sources should be treated cautiously \[Nay12, Wan19e, Dwo26\].

The strong version does look novel. AAT’s most promising claim is not either of those points in isolation, but the stronger architectural thesis that mission-style communication and robust trust are one coordination problem: compress purposeful state into the right kind of shared intent, then discount incoming guidance by separate epistemic and teleological uncertainties using a conservative uptake rule.

A strong one-line framing is this:

AAT’s novelty is not the observation that communication should be efficient and trust should be cautious, but the stronger claim that shared intent and trust are one unified architecture of coordination under bandwidth and misalignment.

---

## References

\[Nay12\] A. Nayyar, A. Mahajan, and D. Teneketzis, “Decentralized Stochastic Control with Partial History Sharing: A Common Information Approach,” *IEEE Transactions on Automatic Control*, vol. 58, pp. 1644–1658, Sep. 2012, doi: [10.1109/TAC.2013.2239000](https://doi.org/10.1109/TAC.2013.2239000).

\[Tan15b\] T. Tanaka, P. M. Esfahani, and S. Mitter, “LQG Control With Minimum Directed Information: Semidefinite Programming Approach,” *IEEE Transactions on Automatic Control*, vol. 63, pp. 37–52, Oct. 2015, doi: [10.1109/TAC.2017.2709618](https://doi.org/10.1109/TAC.2017.2709618).

\[Fox16c\] R. Fox and N. Tishby, “Minimum-information LQG control part I: Memoryless controllers,” *2016 IEEE 55th Conference on Decision and Control (CDC)*, pp. 5610–5616, Jun. 2016, doi: [10.1109/CDC.2016.7799131](https://doi.org/10.1109/CDC.2016.7799131).

\[Wan19e\] R. Wang, X. He, R. Yu, W. Qiu, B. An, and Z. Rabinovich, “Learning Efficient Multi-agent Communication: An Information Bottleneck Approach,” *International Conference on Machine Learning*, pp. 9908–9918, Nov. 2019.

\[Sha12b\] P. Shafto, B. S. Eaves, D. Navarro, and A. Perfors, “Epistemic trust: modeling children’s reasoning about others’ knowledge and intent.” *Developmental science*, vol. 15 3, pp. 436–47, May 2012, doi: [10.1111/j.1467-7687.2012.01135.x](https://doi.org/10.1111/j.1467-7687.2012.01135.x).

\[Dwo26\] P. Dworczak and A. Smolin, “Robust Trust,” Feb. 10, 2026.
