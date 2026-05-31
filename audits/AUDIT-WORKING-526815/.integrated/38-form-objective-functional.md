# 38 - form-objective-functional

Source: `01-aat-core/src/form-objective-functional.md`

## First-pass understanding

This segment makes `O_t` the objective component of `G_t` and gives it one public interface: a real-valued functional `V_{O_t}: trajectories -> R`. The point is type stability. Targets, regions, constraints, utilities, and arbitrary trajectory functionals may differ internally, but the rest of AAT can ask one question: how good is this trajectory under the current objective?

The real-valued codomain is not presented as merely notational. The segment defends it as a comparability commitment: if the agent chooses among alternatives, it has at least locally scalarized its priorities. It also admits the restriction: genuinely unresolved Pareto or vector objectives require an extension, and scalar diagnostics such as satisfaction gap and control regret become weaker or qualitative under that extension.

## Diagram attempt

The useful picture is a funnel. Many objective representations flow through a single evaluation surface, producing scalar values for trajectory comparison and threshold tests. The side channel is important too: vector/Pareto objectives do not fit cleanly through the funnel unless scalarized or decomposed into terminal constraint tests.

## Findings and watches

- Candidate finding: the revealed-preference argument overstates what action implies. Choosing one action over another imposes at most a local choice relation at that moment; it does not by itself imply a total order or real-valued utility over all trajectories. The scalar interface is a legitimate scope restriction, but the defense should cite or state the extra completeness/continuity/independence assumptions needed for real-valued representation.
- Watch: `trajectories` are used as the functional domain, while examples are written over terminal or time-indexed states `s_T, s_t`. That is probably harmless shorthand, but AAT should define whether `tau` is a world-state trajectory, a chronica prefix, an action-observation trajectory, or a complete-state trajectory.
- Watch: the claim that structural results survive vector-valued extension is plausible but not established in this segment. Because I am not reading spikes or later files yet, I am carrying that as an unverified forward-looking claim.
- Watch: the AND-node workaround handles independent threshold constraints, but it does not preserve tradeoff magnitudes inside the feasible region. The segment says this, and later diagnostics should not quietly regain scalar precision for those cases.

## Local verdict

The interface is clean and probably necessary for the scalar diagnostic machinery that is coming. The main audit pressure is about scope language: scalar `V_O` should be framed as "current-timescale scalarization" or "scalar-objective fragment," not as something forced by agency alone.
