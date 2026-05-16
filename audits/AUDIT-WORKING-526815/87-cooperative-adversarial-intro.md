# 87 - cooperative-adversarial-intro

Source: `01-aat-core/src/cooperative-adversarial-intro.md`

## First-pass understanding

This chapter introduction frames cooperation and adversarial pressure as one signed-coupling disturbance ledger. Communication raises the receiver's effective correction tempo, while cooperative action lowers the disturbance faced by the receiver; adversarial action raises that disturbance. The consultant/employee distinction is a good mental model because it prevents a single ally event from being counted twice.

The intro also pulls several later headline claims forward: squared adversarial tempo advantage, effects spirals, and four recipient-side regimes. That is useful pedagogically but creates a status hazard. Since the Working Notes say the intro carries no formal claim of its own, the vivid claims here should remain signposts until their derivations are read.

## Diagram attempt

I drew the chapter's core as a persistence ledger. Communication affects the correction side; cooperative and adversarial actions affect the disturbance side with opposite signs. The diagram includes two audit guards: the disturbance ledger needs a nonnegative convention, and speed advantage depends on the coupled product rather than tempo alone.

## Findings and watches

- F182 candidate: the disturbance decomposition `rho_i = rho_env + sum gamma_adv T_j - sum gamma_coop T_j` needs a nonnegative/floor convention or interpretation as a signed effective load. Otherwise sufficiently strong cooperation can make a disturbance rate negative.
- F183 candidate: the intro says `gamma_A -> 0` plus infinite tempo still fails to destabilize. The operative quantity is the product/coupling term `gamma_A T_A` relative to the target's correction and reserve; `gamma -> 0` and `T -> infinity` is path-dependent unless `gamma = 0` exactly or the product is bounded.
- F184 soft candidate: pulling the squared mismatch ratio into the intro is pedagogically useful, but the formula should keep its assumptions attached every time: deterministic coupling-dominant disturbance, compatible steady-state conventions, and whatever symmetry/baseline conditions the later result requires.
- F185 candidate: the effects-spiral explanation requires an additional feedback model in which `B`'s degradation increases `A`'s coupling effectiveness or legibility. That is plausible, but it is not automatic from mismatch exceeding reserve.
- F186 candidate: Regime III is described as below the observability floor but also as events being processed until tempo is consumed. Below-observability events and low-priority-but-processed events need separate threshold conventions, or the regime should be defined as aggregate/filtering overhead rather than unobserved event content.
- F187 watch: the four-regime classification claims three independent boundary conditions. Check the later classification segment for whether the boundaries are actually independent or only conceptually separable.
- F188 watch: the intro carries strong later claims while declaring no formal claim of its own. Treat it as roadmap language, not as independent support for squared advantage, effects spiral, or recipient-regime taxonomy.

## Local verdict

The signed-coupling ledger is a strong organizing idea. The final audit should preserve the communication/action accounting distinction, while making sure the roadmap does not outrun the assumptions and derivations in the later chapter files.

