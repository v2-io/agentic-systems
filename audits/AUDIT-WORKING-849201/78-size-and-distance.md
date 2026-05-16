# Reflection on `emp-changeset-size-principle` and `def-change-distance`

**1. Predictions vs evidence:**
For `emp-changeset-size-principle`, I predicted a super-linear scaling law relating changeset size to time. The segment actually posited a strictly *linear* proportionality ($t_{\text{impl}} \propto \lvert\text{changeset}\rvert$) as a first-order approximation, deferring the non-linear penalties for "scattered" changes to the proximity principle.
For `def-change-distance`, I predicted a topological distance metric for codebase changes. The segment confirmed this, defining a discrete hierarchy of boundaries: lexical $\lt$ file $\lt$ module $\lt$ service.

**2. Cross-segment consistency:**
The `emp-changeset-size-principle` ties beautifully back to `#der-change-investment`: architectural patterns (like centralized config) are mathematically justified *only* if they reduce the expected $\lvert\text{changeset}\rvert$ of future features. `def-change-distance` correctly maps these boundaries back to AAD's observation channel ($h$): reading within a file is cheap (scrolling), while crossing a service boundary requires loading entirely new context (high cognitive cost).

**3. Math verification:**
The linear proportionality in the size principle is deliberately noted as an empirical heuristic rather than a derived theorem. The working notes are excellent in pointing out that 100 lines in 1 file is very different from 1 line in 100 files, perfectly setting up the need for the distance metric.

**4. What direction will the theory take next?**
Now that we have size and distance, we need to combine them to calculate the true cognitive cost of a feature. The OUTLINE lists `#der-change-proximity-principle` and `#hyp-exponential-cognitive-load` next.

**5. What errors should I now watch for?**
I must ensure the theory doesn't double-count the penalties. If size and distance are both used to predict time, they must be mathematically orthogonal or properly jointly modeled.

**6. Predictions for next segments:**
- `#der-change-proximity-principle` will state that implementation time grows as the change distance increases.
- `#hyp-exponential-cognitive-load` will hypothesize that crossing these boundaries incurs an exponentially compounding cognitive cost, formalizing why highly scattered changes are so devastating to developer tempo.

**7. What would I change?**
Nothing. The decomposition of "how hard is this feature?" into a size component (volume of work) and a distance component (scatter of work) is classic, rigorous modeling.

**8. What am I now curious about?**
How does the `empirical-discontinuity/` tool mentioned in the text actually measure these boundary crossings in Git?

**9. What new knowledge does this enable?**
It provides the objective functions for code refactoring: you either refactor to reduce the *size* of future changes, or to reduce the *distance* between them.

**10. Should the audit process change?**
No.

**12. Value feeling:**
Very practical.

**13. Contribution:**
Defines the physical dimensions of software work.