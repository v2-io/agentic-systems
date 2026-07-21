# Comprehension Quiz — Batch 3 (through `der-recursive-update` + appendix)

*Coverage: cumulative through model sufficiency, class fitness, the Chapter-3 intro, event-driven dynamics, and the recursive-update pair (body + appendix derivation).*

## (1) Critical Mental Model

### Q b03-1.1 [mental-model]
A colleague says: "AAT proves that any adaptive agent's update must be Markovian." Correct this to the claim the corpus actually makes. Your answer should name the three constraints, say which do eliminative work and which is definitional, and state what "cannot be violated" means for the definitional one.

### Q b03-1.2 [mental-model]
Distinguish model sufficiency $S(M_t)$ from model-class fitness $\mathcal F(\mathcal M)$ in one sentence each, then state the operational rule: which observable pattern tells an agent it is facing a class ceiling rather than (a) still-incomplete learning or (b) an irreducibly noisy world? Be precise about what the discriminator is and is *not*.

### Q b03-1.3 [mental-model]
"A model with sufficiency $S(M_t) = 1$ makes correct predictions about the world." What does this inference miss? Explain exactly what $S$ does and does not measure, the scenario in which a fully sufficient model is systematically wrong, and which quantity in the framework carries the accuracy question instead.

### Q b03-1.4 [mental-model]
The appendix deriving the recursive-update result (a Formal Expression $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$ under three named constraints) mounts seven counterexample attacks against it. One attack is conceded as a *genuine limitation* rather than reduced to the recursive form. Which one, what is the concession, and what does the framework say the analogous result is in that setting?

### Q b03-1.5 [mental-model]
Why does the framework bother with an *event-driven* formulation when discrete time is so much more familiar? State the relationship between the two formulations (which is the special case of which, and under what condition), and give one class of real agent for which discrete time is genuinely inadequate.

### Q b03-1.6 [mental-model]
What are "between-event dynamics" $g_M$, why are they *not* filler, and what named operating regime do they enter when driven by internally-generated pseudo-events with an IB-gap-reduction objective?

## (2) Mathematics

### Q b03-2.1 [math]
Write the definition of $S(M_t)$ exactly (the ratio form), identify what the numerator and denominator each measure, and state the well-definedness condition and what kind of environment violates it.

### Q b03-2.2 [math]
Write $\mathcal F(\mathcal M)$ and the structural-inadequacy condition. Then: why can't the agent just compute $\mathcal F$ directly, and what does that imply about how the structural-adaptation trigger must operate in practice?

### Q b03-2.3 [math]
In the appendix deriving the recursive-update result (three constraints, event time $\tau$): reproduce the skeleton of the uniqueness derivation — list the full universe of information available at event time $\tau$, and show which constraint eliminates (or absorbs) each element, ending at the surviving pair. What lemma gives the measure-theoretic version?

### Q b03-2.4 [math]
The recursive-update appendix mounts a battery of attacks against its own result. Trap: "An agent that keeps a complete log of raw events violates the recursive-update result, since its update can consult history directly." Resolve this using the derivation's own argument (which attack is this, and what is the verdict?).

### Q b03-2.5 [math]
Define event information content $\mathcal I(e_\tau)$ as written. A prior-audit seam: what is the mismatch between the notation and the prose interpretation (expected vs realized), and which alternative object would capture the prose's meaning?

### Q b03-2.6 [math]
Sufficiency is policy-relative and trajectory-relative. State what each relativity means formally (what must be held fixed for $S$-comparisons to be meaningful; what object indexes $S$ per agent), and give the consequence for two copies of the same $M_t$ on divergent event streams.

### Q b03-2.7 [math]
From the Chapter-3 intro's preview: write the optimal-gain form and the tempo definition, and state the *epistemic tier* the corpus assigns the gain form outside the linear-Gaussian case (careful — the intro says something precise here that a summary flattens into "derived").

## (3) Implications

### Q b03-3.1 [implications]
A team's ML system shows large, persistent prediction error after months of training with converged parameters and abundant data. Using the model-sufficiency / class-fitness machinery: what *one further property* of the residuals must you check before recommending an architecture change, and what does each outcome of that check imply (structured vs white)?

### Q b03-3.2 [implications]
The completeness commitment C3 "cannot be violated because any violation is absorbed by expanding $M_t$." Explain why the framework insists this is *not* a weakness (what analytical commitment is being made, and where does the real empirical work relocate to)?

### Q b03-3.3 [implications]
An external memory system (notes, databases, RAG stores) seems to let an agent "consult history outside its model." Reconcile this with the recursive-update result, and then give the *genuinely* interesting structural point a prior auditor extracted: why do agents build external memory at all, given lossy internal compression?

### Q b03-3.4 [implications]
The framework says a conservative policy can hold $S$ high while exploration makes $S$ drop. Explain the mechanism (what changes when the policy changes — the model? the world?), and what this implies about the coupling between epistemic state and strategy that later Parts will have to manage.

### Q b03-3.5 [implications]
The appendix deriving the recursive-update result closes with a "what is derived vs. what is chosen" table and a battery of seven counterexample attacks against its own result. Why is that presentation form itself a *contribution*, beyond the specific result it defends? What does it give a reader that a bare "Theorem + proof" presentation does not, and what does the framework risk if downstream segments cite the result while dropping the completeness-commitment (C3) caveat?

### Q b03-3.6 [implications]
The Kuhn analogy: a prior auditor proposed that $\mathcal F(\mathcal M) \lt 1-\varepsilon$ formalizes paradigm crisis (normal science = parametric update; revolution = class change). Steelman the analogy in AAT vocabulary, then name one place it must be checked before being promoted past discussion-grade (what would make it isomorphic rather than evocative?).
