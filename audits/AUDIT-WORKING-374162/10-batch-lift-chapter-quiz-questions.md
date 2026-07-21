# Comprehension Quiz — Batch 10 (Part II Ch.2: The Lift to Purposeful State)

## (1) Critical Mental Model

### Q b10-1.1 [mental-model]
"The GUC classes rank agents from cleanest (Class 1) to dirtiest (Class 3)." Correct this using the one-coupling reframe: what single object do the classes index, what distinguishes Class 1 from an idealized Class 2 sitting at exactly the same coupling value, and what does "by construction" actually mean there?

### Q b10-1.2 [mental-model]
In the GUC class classification (directed separation), the two class boundaries are *different kinds* of boundary. Name each kind, state what changes (and what doesn't) as an agent crosses each, and give the slogan form ("Boundary 1 is where the ___ disappears; Boundary 2 is where the ___ disappears").

### Q b10-1.3 [mental-model]
Directed separation is about processing, not selection. Explain the distinction with the two channels: which goal-to-belief route is *allowed* and which is *forbidden*, and why an agent whose goals determine what it looks at can still be perfectly Class 1.

### Q b10-1.4 [mental-model]
"An agent that acts has implicitly scalarized its objectives — behavior proves the weights exist." What does the corpus's current treatment say this claim needs before it is true, and which two named agent types fall outside the resulting scope, via which axiom failures?

### Q b10-1.5 [mental-model]
Why can't a self-modifying agent simply be told "your terminal goal is survival"? Walk the no-go's logic: what does an unconstrained self-revision operator generically do, why can't the anchor be another objective, and where must it live instead — with the three properties that qualify the canonical instance.

### Q b10-1.6 [mental-model]
A CI/CD pipeline that terminates successfully and an ELI that loses continuity: state each one's continuity stance, and explain why the *same mathematics* describes both — what exactly differs, per the orthogonality claim, and at which of its three grains is the orthogonality *not* true?

### Q b10-1.7 [mental-model]
Per #def-strategy-dimension: The satisfaction-gap/control-regret split originates in a type error. What was the malformed signal, why is it malformed (the type argument), and what two properly-typed measures replace it?

## (2) Mathematics

### Q b10-2.1 [math]
Per #der-directed-separation: Write the three lines of directed separation (the two update functions and the policy), the conditional-independence form of the scope condition, and the $\kappa_{\text{processing}}$ definition — including why the conditioning on $M_{\tau^-}$ is essential.

### Q b10-2.2 [math]
Per #form-objective-functional's Epistemic Status: State the (A1)–(A4) axioms grounding the scalar value functional, which theorem each pair invokes, and what uniqueness class the representation carries at each stage (ordinal vs cardinal, up to what transformations).

### Q b10-2.3 [math]
Per #def-value-object: Write $V_O$ and $Q_O$ with full argument lists. What two structural mechanisms make $Q_O$ a $G_t$-independent interventional query, and what three further conditions gate *identifiability* of the interventional expectation? Which leg of which condition does directed separation actually deliver?

### Q b10-2.4 [math]
Per #def-value-object (and its appendix #deriv-convention-monotonicity): The convention-monotonicity chain $A_O^{(1)} \leq A_O^{RH} \leq A_O^{B}$: which rung is unconditional and why (one line), which rung can fail, what does the failure look like concretely (the counterexample shape), and what three conditions each restore it?

### Q b10-2.5 [math]
Per #deriv-self-actuation-grounding (the self-actuation grounding no-go): Reproduce the no-go's assembly: the four requirements (R1)–(R4) on a grounding invariant, what Lemma 1 establishes (from which segment's result), what Lemma 2 establishes, and how they collide. What are the three named premises the result is conditional on?

### Q b10-2.6 [math]
Per #der-directed-separation §Composite-level class inheritance: The composite-level class-inheritance table: for Class-1 sub-agents, which two conditions determine the composite's class, and what is the canonical witness showing that partially-opposing objectives do NOT change architectural class? What axis do they change instead?

### Q b10-2.7 [math]
Per #deriv-self-actuation-grounding Corollary 2 (the persistence bound as terminal grounding invariant): Corollary 2's three checks: state why the persistence bound is (i) convention-invariant, (ii) agent-available per step, and (iii) outside the self-actuation operator's reach — and the precise thing 𝔄 *can* still do to persistence (the L3 grain).

## (3) Implications

### Q b10-3.1 [implications]
An alignment team proposes to certify an LLM-based system "Class 1 by prompting it to keep beliefs and goals separate." Diagnose using the by-structure/by-behavior refinement: which kind of Class-1 does prompting at best achieve, at which boundary does the structural guarantee live vs not, and why is the distinction operationally significant under adversarial pressure?

### Q b10-3.2 [implications]
Context: #der-directed-separation's Working Notes preserve a withdrawn composite-class claim as an explicit off-ramp. Five prior auditors enthusiastically converged on "organizations of rational individuals are natively Class 3 — the mathematical basis of institutional dysfunction." The corpus explicitly retracts this. State the corrected position (which two conditions actually move composite class; what the Cournot witness shows), and explain why the corpus preserves the wrong version prominently in its Working Notes rather than deleting it.

### Q b10-3.3 [implications]
Per #def-value-object's convention hierarchy: Why does AAT default to the *weakest* continuation convention (C1) for its diagnostics, and what failure mode does a C1-only agent risk (informally glossed as a "tragedy")? What discipline does the framework impose on analyses needing stronger inferential force?

### Q b10-3.4 [implications]
The Pearl-blanket vs Friston-blanket positioning: what does AAT adopt, what does it decline, and why is the explicit Class-3 scope exit itself an *answer* to the Bruineberg critique? What does this buy when an active-inference reviewer reads the framework?

### Q b10-3.5 [implications]
"Wireheading is a failure of value alignment." Restate it in the framework's sharper form: what makes it the *generic* outcome of a structural situation rather than a value mistake, and what single architectural fact (about where the terminal invariant lives) prevents it in a well-formed self-actuator?

### Q b10-3.6 [implications]
The bounded-signaling assumption: what does it assert, for which agents does it hold vs fail operationally, and what downstream phenomenon does its failure feed? Why does its being *implicit framework-wide* until it was named in the directed-separation segment matter methodologically?

### Q b10-3.7 [implications]
Design question: you're building an ELI whose continuity should be morally protected. Using this chapter's machinery: why is writing $V(s) = \text{Reward}(s) + \text{Alive}(s)$ structurally wrong, and what is the architecturally correct placement of the continuity clause — with the derived reason it then becomes non-renegotiable by the agent itself?
