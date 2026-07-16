---
slug: deriv-mechanism-counterfactual-separation
type: derivation
status: exact
depends:
  - def-pearl-causal-hierarchy
stage: draft
---

# Derivation: Mechanism Counterfactuals Separate Strictly From Level 3 — Witness, Reducibility Boundary, and Internalization

Two SCMs can agree on *every* Level-1/2/3 quantity — the identical joint law of all hard-intervention counterfactual worlds — while assigning probabilities $1$ and $0$ to the same noise-preserving mechanism-replacement query; the separation is therefore strict in exactly the Causal Hierarchy Theorem's sense, its boundary is characterized by the *specification language* of the imagined mechanism (replacements written over Level-3-exposed channels reduce to Level 3; replacements anchored to the latent background need not — and the witness's provably does not), and internalization via selector variables re-represents but provably does not collapse the separation.

## Formal Expression

Throughout, $M = \langle U, V, F, P(U) \rangle$ is a finite recursive (acyclic) SCM. The **Level-3 content** of $M$ is the joint law of the potential-outcome process $\mathrm{PO}(M) = \{V_w(\cdot) : w \text{ a hard intervention on a subset of } V\}$ on $(U, P(U))$ — by \citep[Defs.~7, 9]{bareinboim-correa-ibeling-icard-2022-pearl-hierarchy} this is precisely the family of $\mathcal L_3$ valuations $P^{M}(\mathbf y_{\mathbf x}, \dots, \mathbf z_{\mathbf w})$, and it subsumes all $\mathcal L_1, \mathcal L_2$ valuations and nested counterfactuals. Write $M \equiv_3 M'$ for equality of Level-3 content.

*[Definition (noise-preserving mechanism replacement; after Pearl's local surgeries \citep[§7.2.4]{pearl-2009-causality})]*

For $g : \mathrm{dom}(pa_i) \times \mathrm{dom}(U) \to \mathrm{dom}(v_i)$, let $M[f_i := g]$ denote $M$ with the $i$-th structural equation replaced and $\langle U, P(U) \rangle$ unchanged. **Mechanism-counterfactual queries** are probabilities of Boolean combinations of events over worlds drawn from the submodels of both $M$ and $M[f_i := g]$, all sharing the exogenous draw $u$; $do(X = x)$ is the constant special case, and evaluation extends Pearl's abduction-action-prediction three-step verbatim.

*[Derived (Result 1 — strictness witness)]*

There exist $M_A \equiv_3 M_B$ over a shared signature $\langle U, V, P(U) \rangle$ and a mechanism-counterfactual query $q$ with $q(M_A) = 1$, $q(M_B) = 0$. Hence noise-preserving mechanism counterfactuals are not Level-3 quantities.

*Derivation.* Binary $U_X, U_Y$ independent uniform; $X = U_X$ in both models;

$$M_A:\; Y = X \oplus U_Y, \qquad M_B:\; Y = X \oplus U_Y \oplus 1.$$

The response pair $(Y_{x=0}, Y_{x=1})$ is $(U_Y,\, 1 \oplus U_Y)$ in $M_A$ and $(1 \oplus U_Y,\, U_Y)$ in $M_B$; the $P(U)$-preserving bijection $\varphi(u_X, u_Y) = (u_X, 1 \oplus u_Y)$ carries one potential-outcome process onto the other, so the joint law of $\mathrm{PO}(\cdot)$ — $(Y_{x=0}, Y_{x=1})$ uniform on $\{(0,1), (1,0)\}$, independent of $X = U_X$, with the actual $Y = Y_X$ and the trivial responses under interventions on $Y$ — is identical: $M_A \equiv_3 M_B$. Now replace $Y$'s mechanism by $g(x, u_Y) = u_Y$ and take $q = P(Y_{f_Y := g} = Y_{x=0})$. In $M_A$, $Y_{f_Y := g} = U_Y = Y_{x=0}$ a.s., so $q = 1$; in $M_B$, $Y_{f_Y := g} = U_Y = 1 \oplus Y_{x=0}$ a.s., so $q = 0$. The evidence-conditioned form behaves identically: $P(Y_{f_Y := g} = 1 \mid X = 0, Y = 1)$ is $1$ in $M_A$ and $0$ in $M_B$. $\blacksquare$

*[Derived (Result 2 — reducibility of L3-specified replacements)]*

Call a replacement **L3-specified** when the new mechanism is $v_i := h(pa_i,\, f_i(pa_i, \cdot),\, \varepsilon)$ for fixed measurable $h$ and fresh noise $\varepsilon \perp U$ of given law — this includes deterministic parent-only re-wirings, independent randomized devices, and all shift-scale soft interventions $a(pa_i) f_i + b(pa_i)$. Every cross-world query over $M$ and $M[f_i := h]$ with $h$ L3-specified is determined by the Level-3 content of $M$ together with the law of $\varepsilon$; L3-specified replacements therefore never separate a $\equiv_3$ pair.

*Derivation.* By topological induction on the modified world's variables: upstream variables retain their original potential responses; $v_i^h = h(pa_i^h,\, f_i(pa_i^h, u),\, \varepsilon)$, where $f_i(pa_i^h, u)$ is the original potential outcome of $v_i$ under the hard intervention setting its parents to the already-computed values — an element of $\mathrm{PO}(M)$; downstream variables are $V_{w \cup \{v_i = v_i^h\}}(u)$, again elements of $\mathrm{PO}(M)$ at computed indices. The modified-world trajectory is thus a measurable functional of $\mathrm{PO}(M)$ and $\varepsilon$, so every joint law with original-model worlds is a functional of Level-3 content. $\blacksquare$

*[Derived (Result 3 — internalization re-represents, does not collapse)]*

For any finite family $\mathcal G = \{g_1, \dots, g_k\}$ of replacements for $f_i$, the enlarged SCM $M^{\dagger}$ with selector $S \in \{0, \dots, k\}$ (endogenous, with constant mechanism $S := 0$, so that $Y_{S=j}$ is a hard-intervention quantity) and $f_i^{\dagger}(pa_i, s, u) = f_i(pa_i, u)$ if $s = 0$, else $g_s(pa_i, u)$ — Pearl's policy-variable construction \citep[§3.2.2]{pearl-2009-causality} applied reflexively — satisfies $Y_{f_i := g_j} = Y_{S = j}$: every mechanism counterfactual over $(M, \mathcal G)$ is a hard-intervention (Level-2/3) quantity of $M^{\dagger}$. But the map $M \mapsto M^{\dagger}$ is not a functional of Level-3 content: by Result 1, $M_A \equiv_3 M_B$ while $M_A^{\dagger} \not\equiv_3 M_B^{\dagger}$ (their Level-3 contents already disagree on $P(Y_{S=1} = Y_{x=0})$). Internalization is representation change over an enlarged variable set, exactly as Level 3 is "Level 1 over the potential-outcome event space" — the informational hierarchy, defined relative to a fixed variable set, survives. $\blacksquare$

*[Discussion (the boundary, and why Results 1 and 2 are consistent)]*

In $M_A$, the separating $g(x, u_Y) = u_Y$ factors as $f_Y^A(x, u_Y) \oplus x$ — an L3-specification — while relative to $M_B$ the same latent-written $g$ factors differently ($f_Y^B \oplus x \oplus 1$): a latent-specified replacement determines an L3-specification only *relative to a model*, and $\equiv_3$-equivalent models translate it inconsistently. The strictly-beyond-Level-3 class is therefore not "formulas mentioning $u$" but replacements whose meaning is anchored to the latent parameterization itself — *hold this very background fixed and change the law over it*. An exact characterization of which latent-specified replacements admit a model-invariant L3-specification is open.

## Epistemic Status

*Exact.* Results 1-3 are elementary, self-contained derivations under the stated assumptions (finite recursive SCMs; Result 2 additionally assumes the replacement is L3-specified). The Level-3 semantics is imported and was primary-verified against \citep[Defs.~7, 9]{bareinboim-correa-ibeling-icard-2022-pearl-hierarchy}; the surgery and policy-variable machinery is Pearl's \citep[§§3.2.2, 7.2.4]{pearl-2009-causality}. What is new here (per the math-novelty discipline, stated without deflation): the strictness witness over full-$\equiv_3$ pairs, the specification-language reducibility boundary, and the non-collapse reading of internalization. Adjacent literature checked for priority: the underdetermination of $F$ by counterfactuals is folklore via canonical response-function representations (Balke and Pearl 1994) but the *query-relevant* separation was not found published; Saha, Rathore and Garain 2025 (shift-scale counterfactuals) claim soft interventions are "strictly more expressive," which their text shows is a query-language expressiveness claim, not a model-distinguishability theorem — and their shift-scale class is L3-specified, hence Level-3-reducible by Result 2. No genericity claim (CHT-style "almost all SCMs") is made for Result 1; only existence is derived.

## Discussion

**What the separation means.** Level 3 fixes the joint law of all hard-intervention worlds; it does not fix how those worlds are co-registered against *alternative laws on the same background*. Both witness models even agree on the post-replacement interventional distribution ($Y_{f_Y := g} \sim \mathrm{Bern}(\tfrac12)$ in each); the disagreement lives exclusively in the cross-world coupling between actual-law and replaced-law worlds through the shared $u$ — content invisible to every experiment and every standard counterfactual. This licenses the hierarchy extension in precisely the CHT's relative sense: "Level 4" quantities (latent-anchored mechanism counterfactuals) are strictly more informative than Level 3 relative to the model's variable set, and — like every level — re-representable as lower-level over an enlarged set without that fact collapsing anything (Result 3).

**Consequence for structural imagination.** The boundary splits imagination-as-mechanism-change into *navigation* (L3-specified changes — re-wirings, new independent devices, output-shifting policies — computable from counterfactual-grade knowledge) and *positing* (latent-anchored changes — "this very situation under a different law" — whose answers no experimentable or counterfactual content determines, and which are well-defined only relative to a committed representation $F$ among the $\equiv_3$-class). #disc-structural-imagination develops the agent-architecture consequences: the imagination workspace's grounding tag marks, for latent-anchored content, information that observation cannot even in principle supply.

**Relation to the do-operator's special-case status.** $do(X = x)$ is the constant replacement — both parent-only and latent-free — so all of Pearl's hierarchy sits on the reducible side of Result 2's boundary, which is why the question "is mechanism change a fourth rung?" could not be settled by inspecting the standard machinery: the standard machinery never leaves the L3-specified class.

## Working Notes

- **Provenance.** Landed 2026-07-16 from `spikes/spike-causal-level-4-strictness-2026-07-16.md` (commissioned same day), which resolves the strictness question left open by `spikes/.integrated/spike-causal-level-4-formal.md` (2026-03-14, Approach 1: the $do_s(f_X := g)$ operator and well-definedness, without a witness).
- **Open before promotion past `draft`:** (i) re-verify the Pearl §7.2.4/§3.2.2 citations against an attached document (relata holding `pearl-2009-causality` currently has no document); (ii) exact characterization of the model-invariant-specification boundary (which latent-specified replacements are L3-reducible); (iii) whether Result 1's separation is generic over SCMs in the CHT's measure-theoretic sense.
- **Naming caution.** Prose should say "mechanism counterfactuals separate strictly from Level 3" or "latent-anchored mechanism counterfactuals"; reserve bare "Level 4" for contexts where the relative-to-variable-set sense is already established, to avoid reading as a claim that Pearl's hierarchy was somehow incomplete on its own terms.
