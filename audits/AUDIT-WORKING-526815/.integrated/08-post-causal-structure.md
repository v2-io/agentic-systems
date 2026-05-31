# 08 - post-causal-structure

Segment: `01-aat-core/src/post-causal-structure.md`
Dependencies: `def-agent-environment`, `def-chronica` - declared dependencies satisfied.
Status observed: `type: postulate`, `status: axiomatic`, `stage: deps-verified`.

## Reflection

This is a solid postulate: temporal order is the primitive substrate of possible influence, weaker than statistical or Pearl-style causality. The chronica's order is doing real work again. Before any causal hierarchy, there is still the simple fact that `a_{t-1}` cannot depend on `o_t`; that fact will later force recursive update and retrospective mismatch.

The segment also clarifies the scope lattice in a way that makes F1 stronger. Lines 36-38 explicitly say zero-coupling passive systems remain inside adaptive scope while outside agency. So the later scope architecture is consistent; the inconsistency is localized in the initial `def-agent-environment` wording requiring action effects for the base "agent." A smaller secondary issue: the segment uses `scope-agency`/`scope-adaptive-system` materially without listing them as dependencies, and it points forward to Pearl hierarchy, mismatch, action selection, and CIY. Since the already-read scope references are upstream in row order, this is less severe than F2, but it shows dependency metadata is not capturing all semantic reliance.

## Prompt pass

Predictions vs evidence: I expected primitive causal ordering and possible Pearl forward references. Both appeared. I did not expect such a clear zero-coupling clarification; it helps isolate F1.

Cross-segment consistency: consistent with `def-chronica`, `scope-adaptive-system`, and `scope-agency`; inconsistent only with the first definition's action requirement. Possible dependency incompleteness: frontmatter omits `scope-adaptive-system` and `scope-agency` despite lines 36-38 relying on them.

Math verification: no calculation. The formal content is conceptual/ordering-based.

Direction next: the next chapter intro should shift from coupled-loop ontology into compressed representation. I expect less immediate scope tension and more "what is `M_t` relative to `C_t`?" tension.

Errors to watch: later causal-information-yield claims may overuse temporal precedence as if it were causal identification. This segment is careful that precedence is necessary/primitive, not sufficient/statistical.

What I would change: add `scope-adaptive-system` and `scope-agency` to the `depends:` list, or keep the coupling-strength taxonomy in `scope-agency` where those dependencies are already native. Also soften "the model should give more weight" unless later update-gain machinery makes it a formal rule.

Curiosity: the nominal coupling category is subtle: if query choice changes observation distributions but not `Omega`, it is still agency under observation-level interventional contrast. That seems right for epistemic agents, but it means agency is not "world effect" in the strong sense; it is "observable consequence contrast."

New knowledge enabled: causality in AAT now has two nested meanings: temporal possible-influence for all adaptive systems, and Pearl Level-2 interventional contrast for agency.

Audit process change: distinguish severe hidden downstream dependencies (F2) from lighter incomplete dependency metadata involving already-read upstream scopes.

Running outline change: add a note that F1 is now localized to `def-agent-environment`, not the scope lattice.

Value feel: high. It both grounds future derivations and cleaned up a candidate ambiguity.

## Diagram thought

The diagram should show coupling strength as a horizontal spectrum over a stable temporal-order substrate. Strong, weak, and query-only coupling fall into agency; zero coupling falls out of agency but remains above the adaptive-scope baseline if observation and residual uncertainty remain.
