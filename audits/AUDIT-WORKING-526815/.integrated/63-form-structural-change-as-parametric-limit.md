# 63 - form-structural-change-as-parametric-limit

Source: `01-aat-core/src/form-structural-change-as-parametric-limit.md`

## First-pass understanding

This segment reframes strategy maintenance as a spectrum: ordinary reweighting, pruning, grafting, objective revision, and full restructure are not wholly separate mechanisms but increasingly expensive changes to the strategy DAG. The practical lesson is strong: healthy agents should keep reweighting, pruning, and grafting before strategic debt forces catastrophic restructure.

The formal continuity claim needs a representation choice. Pruning is continuous if the edge remains in an ambient graph and its weight approaches zero. Grafting is continuous if the potential edge already exists in a larger hypothesis space at zero weight. Node-set changes and AND/OR reclassification need an even richer embedding; otherwise they are discrete graph edits, not parametric limits.

## Diagram attempt

The diagram distinguishes two views. In a fixed ambient supergraph, an edge weight can move continuously from zero to active or active to zero. Outside that ambient graph, adding a node or changing a gate is a discrete lift into a larger representational space.

## Findings and watches

- F63 candidate: the continuity claim "adding or removing an edge is a boundary event, not a discontinuity" requires an ambient supergraph or hypothesis space in which absent edges are represented as zero-weight edges. Without that embedding, graph edit operations change dimension and are discrete.
- F64 candidate: `gamma` reclassification AND↔OR is listed among the operations in a segment about parametric limits, but AND/OR semantics are discrete unless represented by a soft gate, mixture, or other continuous parameterization. The needed parameterization is not supplied.
- F65 candidate: the neutral-variation discussion says near-zero edges consume minimal cognitive cost, while the pruning-threshold discussion says each maintained edge consumes representational capacity and evaluation time. Low credence reduces expected use, but not necessarily memory/evaluation cost unless the cost model is credence-weighted.
- Watch: the Miller automata bridge is an analogy/constructive inspiration unless the mapping from inaccessible automaton states to low-credence DAG edges is formalized.
- Watch: cross-agent grafting references symbiogenic composition, which is outside the currently read AAT path and remains deferred.

## Local verdict

The maintenance spectrum is useful and probably worth keeping. The strong formal phrase "structural change as parametric limit" should be scoped to a fixed ambient graph or paired with an explicit continuous embedding for node and gate changes.
