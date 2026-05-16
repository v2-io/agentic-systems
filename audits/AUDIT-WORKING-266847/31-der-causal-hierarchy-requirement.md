# Reflection: der-causal-hierarchy-requirement

## What the segment does

Derives that evaluating Q_O requires Level 2 (interventional) knowledge — you can't compute do(a) from observational data alone (Bareinboim et al. 2022). Introduces the "learning-agent scope" restriction: agents that must acquire or refine Level 2 knowledge during operation. Pre-compiled agents (PID, LQR, hardcoded policies) are excluded — their causal structure was externally supplied.

## The learning-agent scope as a genuine restriction

The scope narrowing is clean and honest: learning agents are those that face uncertainty about how their actions affect the world and must reduce that uncertainty through experience. Pre-compiled controllers "know" causal structure through design, not learning — the intervention-outcome mapping is hardwired, not derived from experience. The exclusion is principled.

## The Bareinboim causal hierarchy theorem

AAD is applying an external result (Bareinboim et al. 2022: the three levels form a strict hierarchy, Level 2 ≠ Level 1 in general). The contribution is the application to purposeful agents: if you want to select actions by their consequences, you need causal structure beyond correlations. The LLM absorption note is interesting: LLMs absorb causal priors from training text, not verified interventional data — they're a prior (plausible), not a derivation. The loop verifies.

## Naming targets

"Causal hierarchy requirement" is the segment name. "Learning-agent scope" is the named sub-scope. Both are likely in the tracker.

## Connection to Hafez bi-predictability

The IDT / bi-predictability measurement is the empirical complement: Hafez measures the information-theoretic coupling of the loop; AAD explains why it's superior — the loop generates interventional data by construction. Measurement + explanation is a clean division of labor.

How valuable: 7/10 for load-bearing (learning-agent scope is the restriction that most Section II results sit within), 6/10 for surprise (the Bareinboim application is clean but not unexpected).
