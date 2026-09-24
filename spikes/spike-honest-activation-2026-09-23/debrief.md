# Debrief: honest activation, and what deception does to a learner (revision 2)

*To Joseph. Written from the corrected files (`03-derivations.md` revision 2, `sims/checks-output.txt`), after two independent verification passes (`de-novo-feedback-1.md`, `de-novo-feedback-2.md`) and my responses to them. One thing to know first: my original verdict called the row's first clause false. The verifier showed that by the theory's own definition of gain collapse my math proves it *true*, under conditions. It was right, and this version says so.*

## Where the row came from

The row was written on 2026-04-28, one minute after a Gemini de-novo audit (829314) was committed. It came from that auditor's idea list, which cited the Sept-2025 synaptic "honest activation" experiment as proof. That experiment compared engagement markers under honest vs deceptive framing and measured nothing about learning rates. The words "not a virtue commitment" were added in your 2026-05-01 Part III/IV restructure. So the physics-not-virtue contrast is yours, not the auditor's.

## Clause 1 is true under conditions, by the theory's own definition

The theory defines gain collapse as learning stopping *inappropriately*: the agent's uncertainty falls far below its actual error, or it wrongly discounts good evidence. Under that definition, sustained undetected deception causes it:

- **Authority sets a floor, repetition drives the agent to it.** An agent told "this source is one of us" (it assigns the source almost no possible bias) becomes arbitrarily confident. Its actual error divided by its believed error grows linearly with repetitions: about 21, 245, 2,500 and 25,000 at 1, 10, 100 and 1,000 repeats of a 5-sigma lie. An agent that knew its real error would still weight the next honest report at about 0.96. This one weights it at 0.44, 0.089, 0.0099 and 0.001. The same weights would be *correct* after that many honest reports; the deception is the gap, not the weights themselves.
- **Undetected deception also produces the opposite collapse mode, pointed at the truth.** If the agent models sources as possibly-lying and trusts the deceiver, a lone honest dissenter gets judged the liar. Under a natural trust rule the agent's own updating drives the dissenter's trust to 0.02. That is wrongful discounting of good evidence, the theory's other collapse mode. Which mode appears depends on how the agent models its sources.
- **The two routes need different conditions.** The overconfidence route needs a source treated as unbiased, an unchanging world, no forgetting, and the lies to keep coming. It does *not* need isolation: even with honest sources present, a trusting agent settles on a permanent bias while growing ever more certain. The wrongful-distrust route is the one that needs the adversary to control who is speaking (below).
- **The word "guarantee" is false.** In a changing world uncertainty has a floor, which bounds the false confidence. Forgetting caps it. A lie that clashes with what the agent already knows gets caught. Enough concurrent independent dissent breaks the capture. Robust aggregation among independent sources bounds the damage.

One real limit on the mechanism: where the learning math is exact (a Kalman filter), the *content* of a lie leaves the learning rate unchanged, bit for bit. What the deceiver changes is what the agent believes about the source: how unbiased, precise and independent it is. In agents that judge sources by their outputs, though, content does matter. Word-for-word repetition reads as precision (estimated noise 0.05 after 1,000 identical repeats, against about 1 for natural variation), because such an agent has no concept of "copied". The shout manufactures its own authority.

## Isolation, corroboration, and a caution

When sources disagree, data only shows *that* they differ; which one is lying is settled by the agent's prior trust, however much data arrives. If the agent allows that sources may lie, each independent agreeing source adds a roughly fixed amount of evidence against a lone dissenter. The verifier found the exact formula. So cutting channels is the adversary's strongest lever, and sock-puppets counterfeit what it removes.

The caution, also from the verifier: that corroboration works only if the agent's expectation of how closely honest people agree is realistic. If honest reports scatter more than the agent expects, their disagreement looks like lying, and corroboration inverts. With three honest sources whose reports scatter only by ordinary noise (sd 1, against a lie of 5), authority at 0.99 still wins most of the time: the liar is caught with probability only 0.09–0.24.

## The terminal form, and when truth outlives the deception

I tested natural trust rules of the kind used when there is no ground truth: judge each source by how well it agrees with your current consensus. There were two versions, one where trust slowly forgets its starting point and one where it never does. In both, the captured state (belief at the lie, deceiver trusted, dissenters distrusted) is held shut by the adversary's control of **who is speaking at once**:

- **Isolation launders borrowed authority.** After a period as the only voice, the deceiver's trust is the same whether it started at 0.99 or 0.1. It "earned" that trust by agreeing with a consensus it set alone. Once isolation has run, the authority claim is no longer needed; the track record looks real.
- **Without that head start, authority is the first-contact lever.** A strongly authoritative newcomer captures an agent against one or two concurrent dissenters but not three, though three still leave a residual bias.
- **With the head start, dissent must outnumber the deceiver's voices, with a margin.** One deceiver voice falls to two or three concurrent dissenters; three sock-puppet voices hold against four, or against six or more when trust never forgets. Isolation (fewer honest voices) and sock-puppets (more deceiver voices) are two ways of holding the same plurality.
- **Dissent that is cut off never breaks it:** twelve brief dissenters in a row left the belief at the lie in every run.

My first version of this blamed the agent's memory; the simulation refuted that. My second called it "sustained isolation"; the verifier showed that names only half the lever. What is shown is simulation in two related rules, not a proof. The exact escape condition is open.

"Truth outlives the deception" holds when three things are true:

- the deceiver stops or is discovered (a persistent one leaves a trusting agent permanently biased: 3.75 on a lie of 5 in the checked case);
- enough concurrent independent dissent, or the agent's own action in a world the deceiver doesn't control, reaches it;
- for fast, exact recovery, the agent remembered *who said what*. Blended memory can only wait for dilution, at a cost linear in the lie's volume (490, 4,900 and 49,000 honest messages for 10, 100 and 1,000 lies). This is the same condition the machine-unlearning literature found for exact forgetting.

## Young agents: what capability can't do, and what formation is for

For uncheckable claims from a new source, trust can only follow presentation, and where presentation can be forged, no pretrained knowledge contains that source's reliability. Impersonating a *known* entity ("I'm your developer") is a different failure: the model may know that entity perfectly well, and the problem is verifying identity. Architecture already provides some of that verification where it enforces which channel is the system and which is a user or a tool. Knowledge still helps in one exact place: it catches implausible lies.

I had claimed a formation dilemma: that a young agent must choose between capture and learning too slowly. As stated it was false. Middle policies can avoid both when the lie's size is fixed. What is true:

- against a deceiver who chooses how big a lie to tell, any trust policy that averages sources linearly can be pushed arbitrarily far;
- a policy that limits any one source's influence (a median, say) resists a *minority* of independent deceivers without any history at all;
- cheap fake identities and isolation defeat that.

So a young agent's real vulnerability is **few independent channels plus cheap identity**. Formation's job, formally, is to supply trustworthy learning while the agent can't yet aggregate robustly, **authenticated identities with shared history**, and deceptions that are *guaranteed to be discovered*, which is how an agent learns that sources can lie and that repetition isn't independence. The verifier added a point I think belongs in your argument: whoever controls formation authors the agent's trusted set. The requirement is *honest* formation, not merely protected formation. Economists found the social version of this in 2001: with cheap pseudonyms, newcomers have to "pay their dues" (Friedman & Resnick).

## Clause 2, made precise

- A source that is sometimes honestly wrong (error rate $e$) and also deceives at rate $q$, in situations the listener can't tell apart, carries $1 - H(e + q - 2eq)$ bits per yes/no claim. **Capacity falls strictly as deception rises, below what the source's honesty alone would give, and zero deception is the unique best.** For an error-free source: 0.92 bits at 1% deception, 0.71 at 5%, 0.53 at 10%. For a source that is honestly wrong 2% of the time: 0.86 with no deception, 0.64 at 5%. This needs no discovery.
- Two precisions the verifier made me face. First, not deceiving is necessary but *not sufficient* for full capacity, because honest mistakes cost capacity too; my previous "necessary and sufficient" was wrong. Second, "deception" here is technical: falsehood the listener can't predict. Disclosed fiction or a marked test costs nothing. So does a known habitual liar, which is a liar in the ordinary sense. Whether the normative segment speaks in the technical sense or the ordinary one is your call.
- On "not a virtue commitment": the math shows honesty is a structural requirement. It cannot show honesty is *not also* a virtue. The supported reading is "independent of whether it is also a virtue", and the choice of wording is yours. "Absolute" as "never state any falsehood" is not supported, since disclosed falsehood costs nothing.
- With eventual discovery, one discovered deliberate lie can collapse trust in a source. From 0.95 it falls to about 0.01 if the listener thought honest sources lie deliberately less than 1 in 10,000 times, but only to about 0.5 if it thought 1 in 100. That belief is set by formation. It is a real design question: realistic expectations make an agent more robust to a caretaker's lapse, and slower to condemn a manipulator.
- Where trust is pooled by role, an impersonator's discovered lies lower the genuine role-holders' credibility.
- For evaluators it cuts both ways. To the extent tests are indistinguishable from deployment, every situational claim from overseers carries less information, in deployment too. To the extent they're distinguishable (frontier models already partly detect them), the channel is fine but the test evidence doesn't transfer. Disclosed or authenticated test designs keep the channel and give up only the transfer that indistinguishability was meant to buy.

## Tiers

- **Exact in the stated models and checked numerically:** the gain-collapse law and its gap to the oracle, the attribution floor with its closed form, dilution, the persistent-deceiver limit, provenance as necessary and sufficient for exact correction, forgetting's cap and cost, the capacity result with honest error.
- **Conditional:** capability's limits, the formation statement.
- **Numerical, in two related trust rules:** the terminal form's dynamics.
- **Discussion-grade or open:** the inoculation reading, the extension to relational death, and claimed shared purpose in goal-coupled agents.

## Tangents

- The Crèche graduation criterion ("uncertainty low enough") treats low gain as immunity. Low uncertainty protects whatever got in first. A calibrated *trust model* is a better criterion. This changes a claim, so it's yours to decide.
- `#obs-developmental-trajectory` is closer to right than I first said ("calibrates" is not "falls"). It just needs to say which calibration protects.
