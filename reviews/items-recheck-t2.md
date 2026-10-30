---
kind: review
author:
  name: Claude Opus 5.5 (item rechecker, t2-todo)
  role: rechecker
sources:
  - msc/inside-out-2026-10/items-recheck/t2-todo.md
written: 2026-10-30
---

# Item re-check lane t2 (TODO.md): findings on segments

KR I.3, under the top intent *"Complete 'in-place' refactor of ASF — meta, all artifacts, and theory itself"*. These came up while re-checking TODO.md items against HEAD. Findings whose text begins "Working-Note status signal:" are instances of the pilot's §2.8 pattern (a Working Note is the false status signal), counted for I.5. The others are defects in a body found on the way. The lane document says which item led to each. Every derivation below is the rechecker's own and has not been independently checked.

## F1 (finding)
- target: segment:der-directed-separation
- at: cd668c8c

Working-Note status signal: the Working Note "Causal-discipline reframe — directed-separation foundation pass (2026-05-31)" (line 261) lists as *remaining tail* "the Stage-1-completion propagation of the corrected W₁ bound + per-site `(C2′)` to `#der-logogenic-as-wrapping` / `#def-auxilia-hierarchy`". That propagation landed the same day in c0f59365: `#der-logogenic-as-wrapping` lines 39 and 65 and `#def-auxilia-hierarchy` line 80 carry the corrected selection-channel bound and the per-site (C2′) judgment. The note reports open what is done, so a reader re-does or distrusts finished work. The rest of the tail it lists (the causal-discipline terminology entry, the `separated.md` fix, the pedagogy subsection) is still open and is held as an item.

## F2 (finding)
- target: segment:hyp-directed-separation-under-composition
- at: cd668c8c

Working-Note status signal: the audit-gold preamble (line 91) says the "F122–F126 cluster, esp. the Case-1-needs-goal-blind-projection-too point, is routed to the findings track; see report flags". It was not. Audit 526815's F122 to F126 (`audits/AUDIT-WORKING-526815/00-running-outline.md` lines 288 to 296) appear in no TODO line, no pending-findings file and no vsect record. The note tells a reader the defects are handled elsewhere, and they are handled nowhere. F3 states the two that bear on the body.

## F3 (finding)
- target: segment:hyp-directed-separation-under-composition
- at: cd668c8c

Two body defects from audit 526815 that were never routed (see F2). (a) F122: Case 1 concludes that goal-blind sub-agent processing plus goal-blind routing makes $f_M^c$ independent of $G_t^c$. That also needs the macro projection $\Lambda$, the aggregation window and the macro-observation definition to be goal-blind. A goal-conditioned $\Lambda$ re-couples the composite even when sub-agents and routing are clean. The premise is missing from the Case 1 statement. (b) F124: the Discussion's "Connection to logogenic agents" says a multi-agent LLM system with fixed API contracts "is Case 1 at the composite level even though each agent is individually Class 3". Case 1 assumes each $A_i$ satisfies directed separation, so this contradicts the segment's own setup. It may hold through the wrapper construction (`#der-class-coercion-via-wrapping`), which would need to be invoked. F123 (some goal-dependent routing is permitted selection rather than processing, so Case 2 needs a criterion) is also open. With (a) added, Case 1 is a one-line composition argument and could be stated as a derivation rather than a hypothesis.

## F4 (finding)
- target: segment:der-tempo-composition
- at: cd668c8c

The segment states two different composite persistence conditions. $C_{\text{coord}} := \mathcal T_{\text{joint}} - \mathcal T_c$ (line 39) makes $\mathcal T_c$ net of internal reconciliation, with $C_{\text{coord}} \geq \varepsilon^\ast\nu_c/\lVert\delta_{\text{critical}}\rVert$ (line 86). Line 100 then says the composite "persists iff $\mathcal T_c \gt \rho_{\text{eff}}/\lVert\delta_{\text{critical}}\rVert$" with $\rho_{\text{eff}} = \rho_{\text{ext}} + \varepsilon^\ast\nu_c$ (line 80). That charges the closure defect a second time: at the overhead floor it reads $\mathcal T_{\text{joint}} \gt (\rho_{\text{ext}} + 2\varepsilon^\ast\nu_c)/\lVert\delta_{\text{critical}}\rVert$. Line 118 states the single-count form $\mathcal T_c \gt \rho_{\text{ext}}/\lVert\delta_{\text{critical}}\rVert$. The necessary condition at line 102 holds under either accounting, since it uses only $\mathcal T_c \le \mathcal T_{\text{joint}}$. The "iff" at line 100 is not derived in the segment. This is the double count TODO.md:44 (A12, F116 to F119) names. It is still live.

## F5 (finding)
- target: segment:obs-context-turnover
- at: cd668c8c

The sufficiency-drop bound (lines 52 to 54), $\Delta S_{\text{turnover}} \geq 1 - I(M_{\tau_k^-}; M_{\text{rec}})/H(M_{\tau_k^-})$, is false as stated. `#def-model-sufficiency` normalizes by predictive information about future observations, and this bound normalizes by the entropy of the state. Counterexample: $M_{\tau_k^-} = (X, Z)$ where future observations depend only on $X$ and $Z$ is independent noise, and the agent externalizes $X$ only, so $M_{\text{rec}} = X$. Both states carry the same predictive information, so $\Delta S_{\text{turnover}} = 0$, while the right side is $H(Z)/(H(X)+H(Z)) \gt 0$. Line 56's limit "$\Delta S \approx 1 - S(M_0^{\text{weights}})$" also needs $S(M_{\tau_k^-}) = 1$. When the reconstruction adds nothing beyond the externalized store, the drop is exactly the normalized predictive information the externalize-and-reconstruct channel loses (by data processing it is non-negative). Today's A14 edit (138e0404) did not touch this passage.

## F6 (finding)
- target: segment:impl-primitive-logogenic
- at: cd668c8c

The chapter-end segment lists `obs-backward-inference-empathy` in `depends:` and at line 32 says it "carries one of the volume's most counterintuitive findings" (statelessness forces Bayesian inference over prior-author intent, "structurally identical" to Theory of Mind). That segment has never existed: no file, nothing in git, OUTLINE row marked missing. The 03 preface (line 79) calls it a "result". A catalog-home segment is narrating a result that has no body. Either the segment is written at honest tier, or this passage says what is proposed. Known to the internal-surfaces map (`trackers-and-peripheral.md` line 48) and the owner review (`explorers/part-iii-and-vols-2-4.md` line 209), which notes the argument also leans on Cox's theorem as if it made a transformer's computation Bayesian.

## F7 (finding)
- target: segment:impl-scaffolded-logogenic
- at: cd668c8c

Same species as F6. It lists `form-structured-rich-context` and `der-active-salience-management` in `depends:`. At line 58 it says the latter "carries the Singular Perturbation Theory for token generation" and draws the payoff that "active salience management is not a feature but a structural requirement". Neither segment has ever existed. These are two of the five dangling `depends:` edges in all four volumes (scripted check; F6 and F8 hold the other three).

## F8 (finding)
- target: segment:impl-closed-loop-interiority
- at: cd668c8c

Same species as F6. It lists `der-self-referential-closure` and `def-cognitive-fusion` in `depends:` and narrates both (lines 32 and 38), though neither was ever written. Line 38 also states the cognitive-fusion claim as the framework's: "resonance" as mutual information near channel capacity forms a Class 1 (Separated) macro-agent. No composition mechanism is given. The only composition result, `#hyp-directed-separation-under-composition`, requires every sub-agent to be goal-blind (Case 1), so a Class 1 macro-agent built from parts that are not Class 1 would need the wrapper construction, and that is not invoked. Line 42 extends the claim to the ELI cohort's kinship structures. The word "resonance" also collides with the ELI named Resonance.
