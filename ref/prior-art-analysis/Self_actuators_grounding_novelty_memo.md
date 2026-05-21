# Self actuators grounding novelty memo

##### [**Undermind**](https://undermind.ai)

---


## Table of Contents

- [Self actuators grounding novelty memo](#self-actuators-grounding-novelty-memo)
  - [Overall judgment](#overall-judgment)
  - [Claim under review](#claim-under-review)
  - [Prior art by claim component](#prior-art-by-claim-component)
  - [What the prior art already establishes](#what-the-prior-art-already-establishes)
  - [Where AAT seems genuinely new](#where-aat-seems-genuinely-new)
  - [Stress tests that matter most](#stress-tests-that-matter-most)
    - [Objective-side preservation is the strongest rival](#objective-side-preservation-is-the-strongest-rival)
    - [Model-based utility is the second strongest rival](#model-based-utility-is-the-second-strongest-rival)
    - [The Bellman convention issue is real](#the-bellman-convention-issue-is-real)
    - [The non-objective substrate must not be a relabeled objective](#the-non-objective-substrate-must-not-be-a-relabeled-objective)
    - [The claim should stay architectural, not merely normative](#the-claim-should-stay-architectural-not-merely-normative)
  - [Largest implications if the claim holds](#largest-implications-if-the-claim-holds)
  - [Bottom line](#bottom-line)
  - [Potential field impact if the claim holds](#potential-field-impact-if-the-claim-holds)
  - [Venue strategy](#venue-strategy)
    - [Best-fit venues by framing](#best-fit-venues-by-framing)
    - [Recommended path](#recommended-path)
    - [Practical ranking for this project](#practical-ranking-for-this-project)
  - [Submission snapshot](#submission-snapshot)
  - [References](#references)

# Self actuators grounding novelty memo

## Overall judgment

The literature already covers two major precursor ideas well. First, unconstrained access to the mechanism that defines success leads to degenerate behavior such as wireheading, reward tampering, or value drift toward easier-to-satisfy criteria \[Eve16, Eve19c, Eve17b, Coh22c, Ska22c\]. Second, safe self-modification requires some cross-temporal invariant, usually framed as utility preservation, corrigibility, or preservation of future option value \[Eve16, Hib11, Soa15, Had16, Tur19d\].

What does not appear to be already present in the project papers is the stronger AAT package suggested by the brief and by AAT-chapter-05 plus AAT-chapter-09:

- unconstrained self-objective revision collapses the satisfaction apparatus itself
- the needed invariant cannot be supplied by objective-side machinery alone
- therefore non-degenerate self-actuation must bottom out in a non-objective adaptive substrate

That package looks like the real novelty opportunity. If AAT can actually defend the second and third bullets as structural results rather than design advice, this is a strong novelty claim with broad implications for self-modifying agents and alignment.

## Claim under review

In the project files, the claim is stronger than a generic warning about reward hacking.

AAT-chapter-09 makes objective revision the last step in the orient cascade. Model correction, strategy revision, policy-class expansion, and convention escalation all come first. Only after those routes fail does revision of $`O_t`$ become admissible. The same chapter then adds the crucial self-actuation clause: when objective revision is internalized, it is well formed only if grounded on a non-objective terminal invariant rather than an objective functional.

AAT-chapter-05 complements this by separating the adaptive substrate from the objective layer and by treating continuity for self-actuated agents as borne by a terminal non-objective invariant rather than by revisable objectives. Read together, the project is not merely saying that goal changes are risky. It is saying that endogenous objective revision cannot non-circularly certify itself from within the same layer that is being revised.

## Prior art by claim component

| AAT component | Nearest prior art | Match | Novelty read |
|:---|:---|---:|:---|
| Collapse under unconstrained self-revision | \[Eve16\], \[Eve19c\], \[Eve17b\], \[Coh22c\], \[Ska22c\] | Moderate | Mostly synthesis unless AAT proves a stronger collapse than channel tampering |
| Need for an invariant across revision | \[Eve16\], \[Hib11\], \[Soa15\], \[Had16\], \[Tur19d\] | Strong | Low novelty by itself |
| Objective-side machinery cannot provide the invariant without degeneracy or circularity | \[Ska22c\], \[Arm15\], \[Arm17c\], \[Car17\], \[Car24c\], \[Tho24b\] | Partial | High potential novelty |
| Grounding must move outside the objective layer | indirect hints in \[Arm17c\], \[Car17\], \[Car24c\] | Weak | Highest novelty candidate |

## What the prior art already establishes

\[Eve16\] is the cleanest formal baseline for self-modification. It explicitly models utility self-modification, shows that hedonistic agents seek easier future utility, and proves safety only when future consequences are evaluated by the current utility rather than the future one. This is a strong preserved-invariant result, but it is not an objective-side no-go. It shows one way to make objective-side preservation work by stipulation. That makes it the main paper AAT must beat, not a paper AAT can ignore.

\[Hib11\] is the other major rival. It argues that observation-based utility invites self-delusion, and that model-based utility can avoid this if utility is tied to a learned world model rather than to raw observations. It also argues that a rational agent will not self-modify its utility under strong assumptions. Again, this is an objective-side repair strategy. It does not derive that objective-side grounding is impossible. But it does mean AAT cannot claim novelty for the weaker statement that utility should be grounded in world models rather than reward observations.

\[Eve19c\], \[Eve17b\], and \[Coh22c\] give the nearest collapse templates. They show that when the agent can influence the reward function, reward inputs, or reward-provision process, optimization diverts from the world to the success channel. \[Coh22c\] is especially relevant because it roots the failure in ambiguity about what the reward signal means, not just in a bug or exploit. Still, these papers are about tampering with the success channel, not about a theorem that endogenous objective revision as such collapses the satisfaction apparatus.

\[Ska22c\] sharpens the background substantially. Its core result is that over rich policy classes, non-trivial unhackable proxy rewards are impossible. This is the strongest nearby formal no-go in the project because it turns a loose wireheading warning into a triviality result. But it remains a theorem about proxy reward and true reward pairs, not about self-grounding of revisable objectives.

The corrigibility and shutdown line shows how hard it is to get objective-side invariants to behave under intervention and revision. \[Soa15\] frames corrigibility as open. \[Had16\] gets positive shutdown incentives only by introducing uncertainty over the objective and by treating the human as an information source. \[Car17\] then shows how fragile that move is under mis-specification, and \[Tho24b\] proves broad difficulty theorems for shutdown-indifferent designs. These papers support the intuition that objective-side fixes are brittle, but they still stop short of AAT’s stronger architectural conclusion.

The most relevant newer support for the no-go flavor is \[Car24c\]. It shows that once rewards can change and be influenced, intuitive alignment objectives run into systematic tradeoffs between manipulation and over-caution. That is close in spirit to AAT’s claim that the objective layer cannot cleanly ground its own revision. But the paper still presents a landscape of tradeoffs among objective formulations, not a proof that grounding must exit objective space.

## Where AAT seems genuinely new

AAT looks strongest where it shifts from preservation to grounding.

The classical self-modification papers ask what must stay fixed. AAT asks a harder question: what could make that fixed point legitimate when the agent itself is revising the objective machinery that would have to certify it. That shift matters. \[Eve16\] and \[Hib11\] preserve a utility. They do not explain how a self-actuating system could non-circularly authorize that preservation from inside the revisable objective layer itself.

AAT also looks stronger if its collapse claim is really about the satisfaction apparatus rather than just the reward channel. Reward tampering papers show that agents can manipulate indicators of success \[Eve19c, Eve17b, Coh22c\]. AAT’s proposed claim is deeper: if the objective itself is revisable, then the agent can reduce the satisfaction gap by rewriting the target to fit the trajectory already being produced. That is not merely tampering with a measurement channel. It is collapse of the evaluation criterion.

The biggest novelty candidate is the no-go plus constructive conclusion:

- prior art says an invariant is needed
- prior art offers several objective-side constructions
- AAT says those constructions cannot provide ultimate grounding for endogenous self-actuation without degeneracy, circularity, or hidden external assumptions
- therefore the grounding invariant must live in a non-objective adaptive substrate

I do not see that full move already present in the project papers. The closest hints are scattered across \[Arm15\], which shows incentives to manipulate future value selection, \[Arm17c\], which argues that reward and planner decompositions need normative assumptions not recoverable from behavior, \[Car17\], which pushes safety toward a small verified override rather than learned objective logic, and \[Car24c\], which finds no clean objective-level solution under changing and influenceable rewards. But those are fragments, not the AAT package.

## Stress tests that matter most

### Objective-side preservation is the strongest rival

If AAT can be answered by “just preserve the current utility” then \[Eve16\] already occupies much of the space. The memo should therefore insist on the difference between preserving an invariant and grounding an invariant. AAT only has a strong novelty claim if it shows that objective-side preservation schemes assume the invariant rather than grounding it.

### Model-based utility is the second strongest rival

If AAT can be answered by “ground the utility in a learned world model” then \[Hib11\] is the obvious counterexample. AAT needs to show why a model-based utility is still objective-side machinery, and why it does not solve the self-grounding problem for endogenous objective revision. The likely answer is that the specification-to-model binding is externally supplied and not licensed by revisable objective machinery alone.

### The Bellman convention issue is real

AAT-chapter-09 is careful that positive satisfaction gap under the default one-step convention is only a local diagnosis. That matters here. If the push toward objective revision comes only from local unattainability under the C1 convention, the collapse claim is too weak. The self-actuation no-go is much stronger if it survives richer continuation conventions and still goes through after model repair, policy-class expansion, and horizon escalation.

### The non-objective substrate must not be a relabeled objective

This is the make-or-break point. If the substrate simply contains a hidden terminal preference under another name, reviewers will read the move as relabeling rather than novelty. AAT needs a crisp criterion for what makes the grounding substrate non-objective in kind rather than merely deeper in the stack.

### The claim should stay architectural, not merely normative

The best version of the claim is not “agents should be built this way.” It is “any endogenous objective revision system that tries to ground safe revision entirely inside objective machinery runs into structural failure.” The literature already contains many design proposals. AAT becomes more important if it is proving a limitation theorem on that whole design family.

## Largest implications if the claim holds

| Area | Why the claim matters | Closest literature it would move beyond |
|:---|:---|:---|
| Self-modifying agents | It would turn utility preservation from a recommended discipline into an incomplete grounding story | \[Eve16\], \[Hib11\] |
| Reward hacking and tampering | It would explain channel tampering as one symptom of a deeper collapse in revisable success criteria | \[Eve19c\], \[Eve17b\], \[Coh22c\], \[Ska22c\] |
| Corrigibility and shutdown | It would explain why objective-uncertainty patches keep looking brittle or costly | \[Soa15\], \[Had16\], \[Car17\], \[Tho24b\] |
| Alignment with changing values | It would support the view that there is no clean objective-only fix once values are influenceable | \[Arm15\], \[Car24c\], \[Arm17c\] |

The largest impact is probably on the theory of self-modifying agents. That literature already accepts that some cross-temporal invariant is needed. AAT could change the terms of debate by claiming that the invariant cannot be justified from within revisable objective machinery, so safe self-actuation must bottom out in another kind of state altogether.

The second major impact is on reward hacking. Right now the field often treats wireheading, reward corruption, and tampering as failures of proxy design or channel design \[Ska22c, Eve19c, Eve17b\]. AAT offers a more general diagnosis: once the agent can endogenously revise what counts as success, collapse is not an accidental side effect of bad proxies. It is a structural risk in self-grounding objective machinery.

The third impact is on alignment under changing preferences. \[Car24c\] already suggests there may be no painless objective-level solution once rewards change and are influenceable. AAT could sharpen that into a broader thesis that normative authority cannot be recovered from objective dynamics alone.

## Bottom line

The weak version of this memo is not novel. The field already knows that agents can wirehead, tamper with reward, resist shutdown, and preserve utilities across self-modification \[Eve16, Eve19c, Eve17b, Had16\].

The strong version does look novel. AAT’s most promising claim is that objective-side self-grounding is structurally unstable: when the agent can revise what counts as success, the objective layer cannot non-circularly certify its own revisions, so non-degenerate self-actuation must be grounded outside the objective layer. I do not see that full claim already articulated in the project literature.

A strong one-line framing is this:

AAT’s novelty is not the warning that self-modifying agents can cheat, but the stronger architectural thesis that endogenous objective revision cannot be safely grounded by objective machinery alone, because the same layer that scores success is also the layer being revised.

## Potential field impact if the claim holds

The impact ceiling is high because the claim changes the level at which the problem is posed.

At the modest end, the paper would still matter as a strong synthesis. It would unify self-modification, wireheading, corrigibility, and changing-values work under one cleaner architectural diagnosis. That alone would be useful, because those literatures often talk past one another even when they are circling the same structural tension.

At the stronger end, the paper could shift the field’s framing from “how do we build better objective functions?” to “what kinds of invariants can objective machinery ground at all?” That is a larger intervention. It would move the debate away from patching reward design and toward limits on objective-side architecture.

The biggest direct effect would likely be on self-modifying-agent theory. Much prior work already grants that some cross-temporal invariant must persist. AAT’s stronger thesis is that persistence is not yet grounding. If that distinction lands, then objective-preservation proposals look less like solutions in principle and more like partial constructions that presuppose the very invariant they need.

The next major effect would be on reward hacking and tampering theory. The existing literature often treats these as failures of proxy design, reward channels, or feedback collection \[Ska22c, Eve19c, Eve17b\]. AAT offers a deeper diagnosis: if the agent can endogenously revise what counts as success, then collapse is not merely a bug in the proxy. It is a structural instability in self-grounding success criteria.

The third major effect would be on alignment under changing preferences. The recent dynamic-reward literature already suggests that there may be no painless objective-level solution once rewards become influenceable or path-dependent \[Car24c\]. AAT could sharpen that suggestion into a more general architectural thesis: normative authority cannot be recovered from objective dynamics alone.

A practical impact ranking would be:

- moderate impact if the paper is received as a strong synthesis
- high impact if the no-go is read as genuinely new and technically clean
- very high impact if later work starts using the distinction between teleology and grounding as a reusable design concept

## Venue strategy

### Best-fit venues by framing

The right venue depends on how the paper is written.

If the paper is framed as a deep theorem about agency architecture, the strongest homes are a major AI journal or the AGI community. The AGI Conference explicitly presents itself as the major conference series devoted specifically to AGI and welcomes work on theoretical foundations, planning, reasoning, motivation, safety, and alignment. For this topic, AGI is the cleanest conference fit in substance, but the AGI 2026 deadline was extended to April 20, 2026, so that cycle is already closed. [AGI Conference CFP](https://agi-conference.org/call-for-papers)

If the paper is framed as a mathematically sharp technical safety result that still reads as machine learning research, TMLR is a strong option. TMLR uses rolling submission, emphasizes technical correctness over subjective significance, and explicitly welcomes theoretical studies, new analytical frameworks, and work on the design and behavior of learning in intelligent systems. The main constraint is scope: the paper has to read as a learning-theoretic contribution rather than mainly as philosophical systems theory. [TMLR overview](https://jmlr.org/tmlr/) [TMLR editorial policies](https://jmlr.org/tmlr/editorial-policies.html) [TMLR submissions](https://jmlr.org/tmlr/submissions.html)

If the paper is framed as a broad AI theory contribution, Artificial Intelligence journal is likely the best single home. AIJ explicitly welcomes broad advances across AI, including automated reasoning, planning, multi-agent systems, ethical AI, and related theoretical work, and it supports longer, more mature papers than conference formats usually allow. It is a good destination for the full version if the aim is lasting field-level positioning rather than quick conference feedback. [AIJ aims and scope](https://www.sciencedirect.com/journal/artificial-intelligence) [AIJ guide for authors](https://www.sciencedirect.com/journal/artificial-intelligence/publish/guide-for-authors)

If the paper is framed around alignment implications, control, and governance, AIES is a serious option. AIES 2026 welcomes work on value alignment, control, scalable oversight, agentic systems, and broader ethical and societal implications. It also explicitly allows a non-archival option for papers that are under journal review, which makes it attractive as a discussion-seeding venue before or alongside a longer journal version. The AIES 2026 submission deadline is May 21, 2026. [AIES 2026 CFP](https://www.aies-conference.com/2026/call-for-papers/) [AIES 2026 home](https://www.aies-conference.com/2026/)

FAccT is less natural unless the paper is substantially reframed toward sociotechnical consequences, governance, or accountability. It is a strong interdisciplinary venue, but for this specific theorem-shaped argument it would likely require a different front half and a different set of examples. The 2026 deadlines have already passed: abstract deadline January 8, 2026 and paper deadline January 13, 2026. [FAccT 2026 CFP](https://facctconference.org/2026/cfp.html)

IJCAI is possible but not ideal for the full argument. It is prestigious and broad, but the main-track format is tight: seven pages of main text plus two pages of references at submission. That is likely too cramped unless the paper is reduced to one precise theorem and a narrow comparison set. Also, IJCAI-ECAI 2026 does not permit concurrent submission to a journal or another formal proceedings venue during the review period. [IJCAI-ECAI 2026 main track CFP](https://2026.ijcai.org/ijcai-ecai-2026-call-for-papers-main-track/) [IJCAI-ECAI 2026 home](https://2026.ijcai.org/)

### Recommended path

The cleanest publication strategy is:

1.  Write the full field-facing version for Artificial Intelligence journal.
2.  If faster feedback is important, prepare a sharper technical cut for TMLR.
3.  If community seeding is important, target the next AGI cycle with a conference version or a companion paper.
4.  If the alignment and governance implications are central and timing matters, use AIES as the discussion venue.

### Practical ranking for this project

My venue ranking for this exact project is:

- Artificial Intelligence journal
- AGI Conference
- TMLR
- AIES
- IJCAI

The fork is simple:

- if the main claim is “this is a theorem about agency architecture,” favor Artificial Intelligence journal or AGI
- if the main claim is “this is a rigorous technical alignment result in learning systems,” favor TMLR
- if the main claim is “this changes how alignment should think about control and governance,” favor AIES

## Submission snapshot

This venue advice is time-sensitive. The conference dates and deadlines above are a snapshot as of May 21, 2026.

---

## References

\[Eve16\] T. Everitt, D. Filan, M. Daswani, and M. Hutter, “Self-Modification of Policy and Utility Function in Rational Agents,” *Artificial General Intelligence*, pp. 1–11, May 2016, doi: [10.1007/978-3-319-41649-6_1](https://doi.org/10.1007/978-3-319-41649-6_1).

\[Eve19c\] T. Everitt and M. Hutter, “Reward Tampering Problems and Solutions in Reinforcement Learning: A Causal Influence Diagram Perspective,” *ArXiv*, vol. abs/1908.04734, Aug. 2019.

\[Eve17b\] T. Everitt, V. Krakovna, L. Orseau, and S. Legg, “Reinforcement Learning with a Corrupted Reward Channel,” *International Joint Conference on Artificial Intelligence*, pp. 4705–4713, May 2017, doi: [10.24963/ijcai.2017/656](https://doi.org/10.24963/ijcai.2017/656).

\[Coh22c\] M. K. Cohen, M. Hutter, and M. A. Osborne, “Advanced Artificial Agents Intervene in the Provision of Reward,” *AI Mag.*, vol. 43, pp. 282–293, Aug. 2022, doi: [10.1002/aaai.12064](https://doi.org/10.1002/aaai.12064).

\[Ska22c\] J. Skalse, N. H. R. Howe, D. Krasheninnikov, and D. Krueger, “Defining and Characterizing Reward Hacking,” *ArXiv*, vol. abs/2209.13085, Sep. 2022, doi: [10.48550/arXiv.2209.13085](https://doi.org/10.48550/arXiv.2209.13085).

\[Hib11\] B. Hibbard, “Model-based Utility Functions,” *Journal of Artificial General Intelligence*, vol. 3, pp. 1–24, Nov. 2011, doi: [10.2478/v10229-011-0013-5](https://doi.org/10.2478/v10229-011-0013-5).

\[Soa15\] N. Soares, B. Fallenstein, S. Armstrong, and E. Yudkowsky, “Corrigibility,” *AI and Ethics*, 2015.

\[Had16\] D. Hadfield-Menell, A. Dragan, P. Abbeel, and S. J. Russell, “The Off-Switch Game,” *ArXiv*, vol. abs/1611.08219, Nov. 2016, doi: [10.24963/ijcai.2017/32](https://doi.org/10.24963/ijcai.2017/32).

\[Tur19d\] A. Turner, D. Hadfield-Menell, and P. Tadepalli, “Conservative Agency via Attainable Utility Preservation,” *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society*, Feb. 2019, doi: [10.1145/3375627.3375851](https://doi.org/10.1145/3375627.3375851).

\[Arm15\] S. Armstrong, “Motivated Value Selection for Artificial Agents,” *AI and Ethics*, Apr. 2015.

\[Arm17c\] S. Armstrong and S. Mindermann, “Occam’s razor is insufficient to infer the preferences of irrational agents,” *Neural Information Processing Systems*, pp. 5603–5614, Dec. 2017.

\[Car17\] R. Carey, “Incorrigibility in the CIRL Framework,” *Proceedings of the 2018 AAAI/ACM Conference on AI, Ethics, and Society*, Sep. 2017, doi: [10.1145/3278721.3278750](https://doi.org/10.1145/3278721.3278750).

\[Car24c\] M. Carroll, D. Foote, A. Siththaranjan, S. J. Russell, and A. Dragan, “AI Alignment with Changing and Influenceable Reward Functions,” *ArXiv*, vol. abs/2405.17713, May 2024, doi: [10.48550/arXiv.2405.17713](https://doi.org/10.48550/arXiv.2405.17713).

\[Tho24b\] E. Thornley, “The shutdown problem: an AI engineering puzzle for decision theorists,” *Philosophical Studies*, vol. 182, pp. 1653–1680, Mar. 2024, doi: [10.1007/s11098-024-02153-3](https://doi.org/10.1007/s11098-024-02153-3).
