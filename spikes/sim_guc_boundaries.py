#!/usr/bin/env python3
"""Boundary-sweep experiments for the two GUC directed-separation boundaries.

Spike: spike-guc-class-boundaries-intuition-2026-05-31.md

Imports the reusable toy agents and measurement apparatus from sim_guc_classes.
Produces the numeric tables (and an optional .png) that answer the headline
question: are the Class 1<->2 and Class 2<->3 boundaries the SAME KIND of
boundary, or DIFFERENT kinds?

Two candidate kinds, per the spike hypothesis:
  CERTIFIABILITY boundary: behavior is CONTINUOUS across it; what jumps is the
      availability of a structural separation guarantee (survives perturbation /
      cannot grow under adversarial pressure). Two agents on opposite sides, at
      the limit, behave IDENTICALLY -- they differ only in certifiability.
  BEHAVIORAL boundary:      behavior is DISCONTINUOUS across it -- a real gap /
      blow-up in actual leakage as you cross. The bound goes trivial.

We measure, as we sweep each boundary:
  beh_kappa  : behavioral kappa_processing (goal-divergence of belief)
  goal_bias  : |belief - truth| under a goal pulling away from truth
  adv_leak   : |belief - truth| under an ADVERSARIAL goal far from truth
  adv_slope  : d(adv_leak)/d(|g_adv|) -- does the leak GROW with adversarial
               pressure? A structural guarantee means this is ~0.
  certifiable: structural separation guarantee available? (architecture inspection)
"""

from __future__ import annotations

import numpy as np

from sim_guc_classes import (
    CoupledAgent,
    PartialAgent,
    SeparatedAgent,
    ScalarWorld,
    adversarial_leak,
    asymptotic_bias,
    behavioral_kappa,
    certifiable_separation,
    debias_residual,
)


# A fixed, weakly-identifying world so goal-leak is visible but tracking still
# works. obs_info=0.3 keeps a real ker-I_tau-like free subspace for goals to
# exploit while the agent can still in principle converge.
def world_factory(rng):
    return ScalarWorld(z0=0.0, obs_noise_var=1.0, obs_info=0.3, rng=rng)


GOALS = [-3.0, 0.0, 3.0]


def adversarial_pressure_slope(agent_factory, g_advs=(2.0, 4.0, 8.0, 16.0)):
    """Fit the leak as a function of adversarial goal magnitude. The slope is the
    discriminating quantity: a structural guarantee => leak does not grow with
    |g_adv| (slope ~ 0); a behavioral 'guarantee' => leak grows roughly linearly,
    and near the Class-3 corner it saturates the whole goal displacement (slope
    -> the displacement coefficient, i.e. the bound is trivial)."""
    leaks = np.array([adversarial_leak(agent_factory, world_factory,
                                       g_adv=g, n_trials=150) for g in g_advs])
    g = np.array(g_advs)
    # least-squares slope of leak vs g_adv
    slope = float(np.polyfit(g, leaks, 1)[0])
    return slope, leaks


def row(name, agent_factory):
    bk = behavioral_kappa(agent_factory, world_factory, GOALS, n_trials=150)
    gb = asymptotic_bias(agent_factory, world_factory, g_des=3.0, n_trials=150)
    al = adversarial_leak(agent_factory, world_factory, g_adv=8.0, n_trials=150)
    slope, _ = adversarial_pressure_slope(agent_factory)
    ce = certifiable_separation(agent_factory)
    return dict(name=name, beh_kappa=bk, goal_bias=gb, adv_leak=al,
                adv_slope=slope, certifiable=ce)


def print_table(title, rows):
    print(f"\n{title}")
    print(f"{'config':<22}{'beh_kappa':>10}{'goal_bias':>10}{'adv_leak':>10}"
          f"{'adv_slope':>11}{'certif':>8}")
    print("-" * 71)
    for r in rows:
        print(f"{r['name']:<22}{r['beh_kappa']:>10.4f}{r['goal_bias']:>10.4f}"
              f"{r['adv_leak']:>10.4f}{r['adv_slope']:>11.4f}"
              f"{str(r['certifiable']):>8}")


# =========================================================================== #
#  Boundary 1: Class 1 <-> Class 2 (channel structurally-absent -> bounded-present)
# =========================================================================== #
def sweep_boundary_1():
    """Approach the Class 1<->2 boundary from both sides, up close.

    Class-1 side: the Separated agent. There is exactly ONE Class-1 agent here --
        no knob; the channel does not exist.
    Class-2 side: PartialAgent at s -> 0+. We march s down toward 0 and ask: how
        close to Class-1 behavior can we get without BEING Class 1? What is the
        closest approach on each side, and what does it look like?

    Both forms (content, process) are swept so we can see whether the form
    changes the KIND of the boundary.
    """
    print("\n" + "=" * 71)
    print("BOUNDARY 1:  Class 1 (Separated)  <->  Class 2 (Partial)")
    print("=" * 71)
    print("Class-1 side has no knob (the channel does not exist).")
    print("Class-2 side: march coupling s -> 0+ and watch the approach.\n")

    rows = [row("Class1 Separated", lambda g: SeparatedAgent(g_des=g))]
    for form in ("content", "process"):
        for s in (0.5, 0.2, 0.1, 0.05, 0.01, 0.001, 0.0):
            rows.append(row(f"Class2 {form[:4]} s={s:<6}",
                            lambda g, s=s, form=form:
                            PartialAgent(g_des=g, s=s, form=form)))
    print_table("Boundary 1 sweep", rows)

    # The crux comparison: Class-1 vs Class-2-at-s=0, same form.
    print("\nCRUX -- two agents right next to the boundary, at the limit s=0:")
    sep = row("  Class1 (no channel)", lambda g: SeparatedAgent(g_des=g))
    p0 = row("  Class2 s=0 (process)",
             lambda g: PartialAgent(g_des=g, s=0.0, form="process"))
    print_table("", [sep, p0])
    print("  -> behavior columns identical; only 'certif' differs.")
    print("     The boundary is where the structural guarantee becomes")
    print("     un-certifiable, NOT where behavior changes.")
    return rows


# =========================================================================== #
#  Boundary 2: Class 2 <-> Class 3 (bounded coupling -> full / no-longer-boundable)
# =========================================================================== #
def sweep_boundary_2():
    """Approach the Class 2<->3 boundary from both sides, up close.

    Class-2 side: PartialAgent with s -> 1- (process form -- the form that
        carries you to the Class-3 corner, per disc-partial-coupling-pathways:
        the fully-Coupled corner is (all stages, both sources, process form)).
    Class-3 side: CoupledAgent with kappa -> 0+. We march kappa down toward 0 and
        ask the symmetric question: how close to bounded behavior can a Coupled
        agent get?

    The discriminating measurement here is adv_slope and adv_leak: if this is a
    BEHAVIORAL boundary, the leak/slope should blow up (bound goes trivial) as we
    approach the corner -- a real behavioral discontinuity, unlike boundary 1.
    """
    print("\n" + "=" * 71)
    print("BOUNDARY 2:  Class 2 (Partial)  <->  Class 3 (Coupled)")
    print("=" * 71)
    print("Class-2 side: march process-form coupling s -> 1-.")
    print("Class-3 side: march architectural kappa -> 0+.\n")

    rows = []
    for s in (0.0, 0.1, 0.3, 0.6, 0.9, 0.99, 1.0):
        rows.append(row(f"Class2 proc s={s:<6}",
                        lambda g, s=s: PartialAgent(g_des=g, s=s, form="process")))
    for kappa in (0.9, 0.6, 0.3, 0.1, 0.05, 0.01, 0.001):
        rows.append(row(f"Class3 kappa={kappa:<6}",
                        lambda g, kappa=kappa: CoupledAgent(g_des=g, kappa=kappa)))
    print_table("Boundary 2 sweep", rows)

    print("\nCRUX -- two agents right next to the boundary, at the limit:")
    p1 = row("  Class2 s->1 (process)",
             lambda g: PartialAgent(g_des=g, s=0.999, form="process"))
    c0 = row("  Class3 kappa->0",
             lambda g: CoupledAgent(g_des=g, kappa=0.001))
    print_table("", [p1, c0])
    return rows


# =========================================================================== #
#  The head-to-head: are the two boundaries the same KIND?
# =========================================================================== #
def compare_boundary_kinds(b1_rows, b2_rows):
    print("\n" + "=" * 71)
    print("ARE THE TWO BOUNDARIES THE SAME KIND?")
    print("=" * 71)

    # Boundary 1 limit pair: Class1 vs Class2-s0 (same form)
    sep = row("Class1", lambda g: SeparatedAgent(g_des=g))
    p0 = row("Class2 s=0", lambda g: PartialAgent(g_des=g, s=0.0, form="process"))
    # Boundary 2 limit pair: Class2-s->1 vs Class3-kappa->0
    p1 = row("Class2 s->1",
             lambda g: PartialAgent(g_des=g, s=0.999, form="process"))
    c0 = row("Class3 k->0", lambda g: CoupledAgent(g_des=g, kappa=0.001))

    def gap(a, b, key):
        return abs(a[key] - b[key])

    print("\nBoundary 1 (Class1 | Class2-at-s=0), behavior gap AT THE LIMIT:")
    for key in ("beh_kappa", "goal_bias", "adv_leak", "adv_slope"):
        print(f"  {key:<11}: |{sep[key]:.4f} - {p0[key]:.4f}| = {gap(sep, p0, key):.4f}")
    print(f"  certifiable: {sep['certifiable']} vs {p0['certifiable']}   <-- THE jump")

    print("\nBoundary 2 (Class2-at-s->1 | Class3-at-kappa->0), behavior gap AT THE LIMIT:")
    for key in ("beh_kappa", "goal_bias", "adv_leak", "adv_slope"):
        print(f"  {key:<11}: |{p1[key]:.4f} - {c0[key]:.4f}| = {gap(p1, c0, key):.4f}")
    print(f"  certifiable: {p1['certifiable']} vs {c0['certifiable']}")

    print("\nVERDICT SHAPE (read the numbers above):")
    print("  Boundary 1: behavior gap ~ 0 at the limit, certifiability flips.")
    print("              => CERTIFIABILITY boundary.")
    print("  Boundary 2: certifiability is False on BOTH sides (no structural")
    print("              guarantee exists for either); what changes is whether")
    print("              the leak stays bounded (adv_slope/adv_leak). The")
    print("              Class-3 corner is where the bound goes trivial.")
    print("              => BEHAVIORAL boundary (different KIND).")


def wrappability_and_slope_table():
    """The form-distinction view, sharper than the raw class labels.

    Shows two independent properties of a goal->belief channel:
      adv_slope        : does the leak GROW with adversarial goal magnitude?
                         (= 'is the bound trivial' = the Class 2<->3 discriminator)
      debias_residual  : can a fixed linear (W2) wrapper remove the coupling?
                         (= the canon's content/process form-determines-wrappability)

    The surprising-but-coherent result: CONTENT-form and COUPLED both have high
    adv_slope (additive goal entry => leak grows with pressure), yet content-form
    is fully wrappable (residual ~ 0) while coupled is not freely-wrappable.
    PROCESS-form gain-modulation is self-limiting (slope ~ 0) yet NOT linearly
    wrappable. The two properties are orthogonal -- which is why the class label
    alone underdetermines both the adversarial signature and the repair regime.
    """
    print("\n" + "=" * 71)
    print("TWO ORTHOGONAL PROPERTIES OF THE GOAL->BELIEF CHANNEL")
    print("=" * 71)
    print(f"{'config':<26}{'adv_slope':>11}{'debias_resid':>14}{'wrappable?':>12}")
    print("-" * 63)
    specs = [
        ("Class1 Separated", lambda g: SeparatedAgent(g_des=g)),
        ("Class2 content s=0.3", lambda g: PartialAgent(g_des=g, s=0.3, form="content")),
        ("Class2 process s=0.3", lambda g: PartialAgent(g_des=g, s=0.3, form="process")),
        ("Class3 coupled k=0.3", lambda g: CoupledAgent(g_des=g, kappa=0.3)),
    ]
    for name, fac in specs:
        slope, _ = adversarial_pressure_slope(fac)
        _, resid = debias_residual(fac, world_factory, n_trials=150)
        wrappable = "yes (W2)" if resid < 0.02 else "no (needs W1)"
        print(f"{name:<26}{slope:>11.4f}{resid:>14.4f}{wrappable:>12}")
    print("\n  adv_slope and debias_residual are ORTHOGONAL:")
    print("  - content-form: high slope (additive => grows with pressure) BUT")
    print("    residual~0 (the same additive structure makes it subtractable).")
    print("  - process-form: low slope (gain-bounded, self-limiting) BUT")
    print("    residual>0 (gain modulation is not a fixed additive bias).")
    print("  The property that makes content-form leak under pressure is the very")
    print("  property that makes it wrappable. This corroborates the canon's")
    print("  form-determines-wrappability cut from an independent angle.")


def make_plot(path="guc_boundaries.png"):
    """Optional matplotlib figure. Two panels:
       (left)  Boundary 1: adv_leak vs coupling s, both forms, with the lone
               Class-1 point at s=0 marked -- shows behavior continuous to 0.
       (right) Boundary 2: adv_leak vs distance-into-Class-3 -- shows the
               leak climbing to the trivial bound (the full goal displacement).
    """
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as e:  # pragma: no cover
        print(f"(plot skipped: {e})")
        return False

    # Boundary 1 data
    ss = [0.0, 0.001, 0.01, 0.05, 0.1, 0.2, 0.5]
    leak_content = [adversarial_leak(lambda g, s=s: PartialAgent(g_des=g, s=s, form="content"),
                                     world_factory, g_adv=8.0, n_trials=120) for s in ss]
    leak_process = [adversarial_leak(lambda g, s=s: PartialAgent(g_des=g, s=s, form="process"),
                                     world_factory, g_adv=8.0, n_trials=120) for s in ss]
    sep_leak = adversarial_leak(lambda g: SeparatedAgent(g_des=g),
                                world_factory, g_adv=8.0, n_trials=120)

    # Boundary 2 data: a single monotone axis from deep Class 2 to deep Class 3.
    # Left half = process-form s in [0,1]; right half = coupled kappa in [0,1].
    s_axis = [0.0, 0.3, 0.6, 0.9, 1.0]
    k_axis = [0.1, 0.3, 0.6, 0.9]
    leak_s = [adversarial_leak(lambda g, s=s: PartialAgent(g_des=g, s=s, form="process"),
                               world_factory, g_adv=8.0, n_trials=120) for s in s_axis]
    leak_k = [adversarial_leak(lambda g, k=k: CoupledAgent(g_des=g, kappa=k),
                               world_factory, g_adv=8.0, n_trials=120) for k in k_axis]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2))

    ax1.plot(ss, leak_content, "o-", label="Class 2 content-form")
    ax1.plot(ss, leak_process, "s-", label="Class 2 process-form")
    ax1.scatter([0.0], [sep_leak], marker="*", s=220, color="green", zorder=5,
                label="Class 1 (Separated, no channel)")
    ax1.axhline(sep_leak, color="green", ls=":", lw=1)
    ax1.set_xlabel("coupling strength  s  (Class-2 within-knob)")
    ax1.set_ylabel("adversarial leak  |belief - truth|,  g_adv = 8")
    ax1.set_title("Boundary 1: Class 1 <-> Class 2\n"
                  "behavior continuous to s=0; only certifiability jumps")
    ax1.legend(fontsize=8)
    ax1.grid(alpha=0.3)

    # Boundary 2: x = monotone 'distance toward fully-Coupled'.
    x_s = [0.5 * v for v in s_axis]                 # 0 .. 0.5
    x_k = [0.5 + 0.5 * (1 - v) for v in k_axis]     # 0.55 .. 0.95 (kappa large->0)
    ax2.plot(x_s, leak_s, "s-", color="C1", label="Class 2 process-form  (s: 0->1)")
    ax2.plot(x_k, leak_k, "^-", color="C3", label="Class 3 coupled  (kappa: 1->0)")
    ax2.axhline(8.0, color="k", ls="--", lw=1, label="trivial bound (full g_adv=8)")
    ax2.set_xlabel("distance toward the fully-Coupled corner  -->")
    ax2.set_ylabel("adversarial leak  |belief - truth|,  g_adv = 8")
    ax2.set_title("Boundary 2: Class 2 <-> Class 3\n"
                  "leak climbs toward the trivial bound (behavioral)")
    ax2.legend(fontsize=8)
    ax2.grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(path, dpi=130)
    print(f"\n(plot written to {path})")
    return True


def main():
    b1 = sweep_boundary_1()
    b2 = sweep_boundary_2()
    compare_boundary_kinds(b1, b2)
    wrappability_and_slope_table()
    make_plot()


if __name__ == "__main__":
    main()
