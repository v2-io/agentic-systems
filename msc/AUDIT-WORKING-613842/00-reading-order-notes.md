# Reading Order Notes

## Global dependency pass

I computed a corpus-wide dependency graph across active non-`old-*` segments in:

- `01-aad-core/src/`
- `02-tst-core/src/`
- `03-logogenic-agents/src/`

Result:

- Active segments seen: 142
- Missing dependencies at corpus level: 0
- Nontrivial strongly connected components: 1
- Size of SCC: 7

The SCC consists of:

- `#def-strategic-tempo`
- `#form-strategy-complexity-cost`
- `#hyp-edge-update-via-gain`
- `#scope-edge-update-causal-validity`
- `#deriv-strategic-dynamics`
- `#deriv-edge-update-natural-parameter`
- `#deriv-strategy-cost-regret-bound`

This means the active corpus does **not** currently admit a strict global topological order from frontmatter alone.
That is itself a process-level issue because `msc/de-novo-audit-instructions.md` assumes such an order can be honored mechanically.

## Manual break policy for the SCC

I will break the cycle this way:

1. Read the conceptual / weaker-status segments first:
   `#hyp-edge-update-via-gain`,
   `#scope-edge-update-causal-validity`,
   `#def-strategic-tempo`,
   `#form-strategy-complexity-cost`.

2. Then read the supporting derivations:
   `#deriv-strategic-dynamics`,
   `#deriv-edge-update-natural-parameter`,
   `#deriv-strategy-cost-regret-bound`.

3. Then revisit the earlier four segments and judge whether their stated dependence on later derivations is honest support, over-tight coupling, or a frontmatter-design mistake.

This preserves first-pass honesty while acknowledging that the repo's own dependency graph currently cannot.

## Other ordering notes

`03-logogenic-agents/OUTLINE.md` has at least one explicit row-order violation:
`#result-coupled-diagnostic-framework` appears before `#scope-observation-ambiguity-modulation` despite depending on it.
I will read those in dependency order, not outline order.

The component-local `bin/lint-outline` reports many "missing" dependencies in `02-tst-core/` and `03-logogenic-agents/`, but those are cross-component references rather than true corpus-level missing files.
So for audit purposes:

- corpus-wide dependency analysis is the authoritative graph
- component-local linter output is still useful for local ordering drift, but not for cross-component existence checks
