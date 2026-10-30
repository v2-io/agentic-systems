*Feeds **KR C.1** (integrator-items A1). The independent check of the status-propagation exactness result landed in `#deriv-graph-structure` §"Exactness of Status Propagation" (commit `33bf185d`, renamed in `471aa7ce`). Verifier: a general-purpose Claude Opus 5.5 agent launched by the C.1 integrator on 2026-10-30, with a bare brief: re-derive the section from what is written and try to break it. It read the uncommitted section; its findings were applied before the commit. Below is its reply, wording verbatim, math converted to LaTeX. After it is how each finding was disposed of. Scripts: `A1-checks/` (`verifier-check.py` is the verifier's; `prop.py`, `rand.py`, `sign2.py` are the integrator's; run any of them with `python3 <path>`).*

# A1 independent verification

## The verifier's reply

I'd hold the section at **exact** with five wording repairs. The theorem and both directions of its proof hold as written, and so does the sign theorem in the scope it states. The problems are in the sentences around them, and one of them is inside the Result paragraph itself. I also found one strengthening and one adjacent defect in Step 3(d). I edited nothing.

**How I checked.** I wrote a script that builds about 3,000 random AND/OR graphs (2 to 6 nodes) under your structural equations. For each it computes the true $P(X_v)$ by enumerating every leaf draw and edge transmission, then compares against the forward pass at every node.

- **Iff:** zero violations. Every node where propagation was exact had one path from each ancestor, and every node that failed had two.
- **All-AND and all-OR signs:** zero violations.
- **Proofs re-derived by hand:**
  - ($2 \Rightarrow 1$): if two parents of $u$ shared an ancestor-or-self $w$, $w$ would have two paths to $v$.
  - ($1 \Rightarrow 2$): degrees add because the polynomial ring is an integral domain, and every node has a leaf at or above it.
  - Tree $\Leftrightarrow$ polytree under rootedness, and the multitree example $c$, $d$.
  - Note that ($1 \Rightarrow 2$) never uses edge credences as indeterminates. Any fixed positive edge credences give failure at generic leaf credences, which is a slightly stronger statement if you want it.

**Fixes to the statements**

1. **Multitree sentence (inside the Result).** "No node has two parents with a common ancestor" is false if "ancestor" means a strict ancestor.
   - Counterexample: the triangle $a \to b$, $a \to c$, $b \to c$. Here $a$ is a parent and also an ancestor of the other parent, so the clause is satisfied, yet there are two paths $a \to c$. The forward pass gives $0.496$ at $c$ against a true $0.412$.
   - Fix: either say "ancestor-or-self," or drop the clause and keep "at most one directed path between any two nodes," which is the standard definition.
   - This sentence needs the repair before the paragraph can carry "exact."
2. **"Needs C to enter each branch as a hard gate (edge credence 1)."** The edge credence is not what matters.
   - The transmission variables are separate per edge, so a $C$-edge credence below $1$ can be moved onto the branch's side: $C \wedge E_{C,i} \wedge D_i \wedge E_{D,i} = C \wedge (E_{C,i} \wedge D_i \wedge E_{D,i})$.
   - Witness: $C$-edge credences $0.6$ and $0.5$. The truth is $0.47185232$ and the tree rewrite gives $0.47185232$.
   - What the identity needs is that $C$ enters each branch as an AND-parent, so the branch fails when $C$ fails. That is exactly $\theta_{\text{child}\mid\neg C} = 0$, the strict-prerequisite condition. Fix: "$C$ must enter each branch as an AND-parent."
3. **Cutset conditioning "at $2^k$ forward passes."** This fails when a cutset node is internal and one of its ancestors also reaches the root another way.
   - Conditioning on $C$ changes the posterior of $C$'s ancestors, and a forward pass cannot see that.
   - Counterexample: $L \to C$, $C \to A$, $C \to B$, $L \to Z$, root $= \mathrm{AND}(A, B, Z)$, every credence $0.8$ except $p_L = 0.6$. The truth is $0.12583$; the naive two-pass sum is $0.07550$.
   - The claim holds when the cutset is made of sources, or of exogenous variables clamped to $0/1$. With those clamped, propagation is exact whenever every unclamped exogenous variable has at most one path to $v$ (same proof as $2 \Rightarrow 1$). Pearl's actual algorithm instantiates the cutset as evidence and runs polytree belief propagation, which is not a forward-only pass.
   - Your sentence that L1′ and explicit conditioning are cutset conditioning survives, because in those cases $C$ is a leaf.
4. **"Enters the forward pass as $p_\ell^N$."** True of the degree, not the value. For $\mathrm{OR}(C, C)$ with $p = 0.3$, the forward pass gives $0.51$, while $p^2 = 0.09$ and the truth is $0.3$.
   - Exact replacement: the forward pass at $v$ equals the true probability on the *path-unfolded tree*. That tree copies each node once per path to $v$, each copy with its own independent noise. This is immediate from the recursion, and "degree = path count" becomes a corollary of it.
5. **Setting: "Causal sufficiency makes the leaf draws and the transmissions mutually independent."** This misattributes one of the two independences.
   - Causal sufficiency makes exogenous terms independent *across* nodes.
   - Independence of the several transmissions *into one node* is the independence-of-causal-influence assumption that comes with noisy-AND/OR (Heckerman & Breese's term). If those correlate, even a tree is wrong.
   - The tag already names the structural equations as a premise, so the label is fine; only the sentence needs fixing. `def-strategy-dag` line 82 has the same parenthetical.
6. **Minor, Step 3(e): "exogenous independence is necessary."** This isn't proved.
   - Correlated exogenous terms can match the forward pass at particular credences. For example, $R = \mathrm{AND}(\ell_1, \ell_2, \ell_3)$ with dependent leaves but $P(111) = p_1 p_2 p_3$ is still computed correctly.
   - "For all credences" is not defined for a dependence structure that has no parameters.
   - Suggested wording: "the forward pass assumes it, and it is not sufficient."

**Strengthening the sign theorem**

The node types that set the sign are only those of the *reconvergent* nodes: nodes with two parents whose ancestor-or-self sets meet. Every other node can be either type.

- **Proof.** Both formulas are nondecreasing in their inputs. At a node whose parents are not reconvergent, the parents are independent, so the formula is exact given exact inputs and carries any bias in its inputs through with the same sign. Association is needed only at reconvergent nodes. By induction:
  - if every reconvergent node is AND, then $s \leq P$ everywhere;
  - if every reconvergent node is OR, then $s \geq P$ everywhere.
- **Empirical check.** 156 random mixed graphs whose reconvergent nodes all had one type (87 AND, 69 OR) gave zero violations.
- **"No general sign" holds only once reconvergent types mix.** It can then flip within one graph. Take root $= \mathrm{OR}(X, Y)$, where $X$ is an AND reconvergence of leaf $C$ and $Y$ is an OR reconvergence of leaf $D$, all edges at credence $1$. At $(c, d) = (0.5, 0.01)$ the error is $-0.240$; at $(0.01, 0.5)$ it is $+0.245$.
- **What it buys.**
  - It proves the sign of `def-strategy-dag`'s "naive L1 gives the same overestimate." That graph reconverges at an OR root; the error there is $c \cdot d_1 \cdot d_2 \cdot (1-c) = 0.1008$, matching $0.877 - 0.776$.
  - It covers the realistic plan shape: OR near the root and AND inside.
- **Possible next step.** The same argument should work with *associated* rather than independent exogenous terms, which is the monotone latent-cause case. That would generalize the two-sibling $\pm\mathrm{Cov}$ table to any number of siblings and any depth. I haven't checked this numerically.

This is my derivation, so it needs checking by someone else before it lands.

**Adjacent defect: Step 3(d)**

P3 asks to update a component *and its consequences* without recomputing. The Causal Markov Condition makes each node's conditional distribution local; it does not make revising the consequences local.

- In your minimal case, observe $A = 1$. That forces $C = 1$, $B = 1$ and $R = 1$. The local move (set $s_A = 1$ and propagate forward) gives $R = 0.5$.
- Local forward revision is exact only on a tree. That is the same condition the new section derives, and the same root cause: the forward pass ignores dependence through shared ancestors.
- So "local revision is automatically correct for any causally sufficient DAG" overclaims, in 3(d), the Assembling paragraph, the Epistemic Status, and the "P3→Markov: resolved" Working Note.
- This doesn't change the new section's label, but it is the same defect and could be fixed in the same cycle.

**Other places to check** (as they read now, given your parallel edits)

- `def-strategy-dag.md` line 101, L0 row: "no node feeds two parents" should say "no node has two children."
- `der-orient-cascade.md:91`: "equals actual plan success only when the DAG is causally sufficient." This leaves out the tree condition.
- `example-strategy.md:388` and its table row: "the AND/OR propagation is correct." Is that toy graph a tree?
- `example-L1.md:16`: correct as written for the factored tree; worth one check that it says "tree."

**Clarity and citations**

- The section reads clearly. The minimal case and the multitree example are both good teaching devices.
- None of the four new sources (Pearl 1988, Esary-Proschan-Walkup 1967, Lauritzen & Spiegelhalter 1988, Vesely et al. 1981) is in `ref/`. The citations match my memory and fit the claims as used, but I didn't check them against the sources.
- Two precision notes on the citations:
  - Junction-tree cost is exponential in the treewidth of the *moral* graph. Noisy-OR nodes with many parents make that large unless the node is factored.
  - Pearl's propagation needs singly connected (polytree) graphs because it handles evidence. A forward pass with no evidence needs only the weaker multitree condition. That is worth one sentence, since it explains why your multitree case exists.

## Disposition

| Finding | Outcome |
|---|---|
| Iff and both proof directions | Held; landed at `exact` under the stated premises |
| Fixes 1–5 | Applied as worded, in `#deriv-graph-structure` and in `#def-strategy-dag` (:82 parenthetical, L1 paragraph, explicit-conditioning bullet), `#example-L1`, the `strategy-plan-confidence` term entry |
| Fix 6 | Applied: "the forward pass assumes it, and that independence is not sufficient" |
| Fixed edge credences suffice for failure | Landed as one sentence after the derivation |
| Reconvergent-node sign strengthening | Re-derived by the integrator (monotone passthrough at non-reconvergent nodes, association at reconvergent ones). `A1-checks/sign2.py` found 400/400 mixed graphs with no violation, and the sign-flip figures were recomputed by hand. Landed at `exact`, replacing the all-AND/all-OR statement |
| Associated-exogenous generalization | Not checked; open, a C.2 candidate |
| Step 3(d) | Fixed in the same commit: the CMC makes the representation local; forward revision of consequences is exact on trees and evidence propagation on polytrees. Assembly, Epistemic Status and the P3 Working Note follow |
| `def-strategy-dag` L0 row; `der-orient-cascade:91` | Fixed |
| `example-strategy:149`, `:388` | Not fixed. The toy is a tree, but its leaves "arm $k$ is best" are mutually exclusive, so the leaf draws are dependent: the latent-cause failure, not reconvergence. Handed to the lead |
| Citations not in `ref/` | Not checked against the primaries; Heckerman & Breese 1996 added on the verifier's pointer, also unchecked. An F.3 item |
| Moral-graph treewidth; Pearl evidence vs forward pass | Both sentences landed |
