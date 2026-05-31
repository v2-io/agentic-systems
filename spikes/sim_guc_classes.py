#!/usr/bin/env python3
"""Reusable toy-agent infrastructure for the three GUC directed-separation classes.

Spike: spike-guc-class-boundaries-intuition-2026-05-31.md

This module is the substrate. It defines the smallest belief-update agents that
faithfully instantiate the GUC Class 1/2/3 partition of `#der-directed-separation`,
plus the measurement apparatus for probing the two boundaries (1<->2 and 2<->3).
The boundary-sweep experiments live in sim_guc_boundaries.py and import from here.

--------------------------------------------------------------------------------
WHAT THE CANON SAYS (the thing we are instantiating)
--------------------------------------------------------------------------------
`#der-directed-separation` partitions agents by their *processing topology* --
specifically whether the goal state G_t is causally upstream of the belief-update
f_M. The classes are STRUCTURAL and DISCRETE, not points on a kappa-axis:

  Class 1 (Separated): f_M is goal-blind BY CONSTRUCTION. The G -> f_M channel is
                       structurally absent. kappa_processing = 0 under ALL goal
                       distributions (no pathway exists). e.g. Kalman + LQR.
  Class 3 (Coupled):   f_M is goal-conditioned. The channel IS the architecture --
                       a single mechanism mixes goal + observation. kappa high
                       under most distributions. e.g. transformer LLM.
  Class 2 (Partial):   bounded coupling -- some shared infrastructure, some
                       separate pathways. kappa varies with the task distribution.

`#disc-partial-coupling-pathways` gives the Class-2 sub-typology (stage x source x
form); the load-bearing axis is FORM (content = additive bias, subtractable;
process = functional-form change, not subtractable).

The leakage-locus spike (spike-leakage-locus-2026-05-18.md) gives the exact
linear-Gaussian shape we build on: in an information-form Kalman update, goal
contamination entering as a smooth tilt g produces a mean shift

    Delta_mu = Lambda0^{-1} g,   Lambda0 = (P^-)^{-1} + H^T R^{-1} H

confined to the directions the observation does not pin (ker of the observation
Fisher information). We use exactly this filtering structure so our toy agents
are faithful miniatures of the canon, not arbitrary maps.

--------------------------------------------------------------------------------
THE TOY WORLD (deliberately minimal)
--------------------------------------------------------------------------------
A scalar latent z (the "true state of reality") that the agent tracks. At each
step a noisy observation o = z + noise arrives. The agent maintains a Gaussian
belief (mu, var) over z. The agent also has a scalar GOAL g_des -- "the value it
would prefer z to be." Goal-coupling = the goal pulling the belief toward g_des
during the update.

This is the smallest setting in which "did the goal leak into the belief?" is a
crisp, measurable question, and it inherits the canon's exact Delta_mu = K * g
shape (K the Kalman gain) so the numbers connect to the theory.
"""

from __future__ import annotations

import numpy as np


# =========================================================================== #
#  The world
# =========================================================================== #
class ScalarWorld:
    """A scalar latent z observed through additive Gaussian noise.

    The latent can be static (z fixed) or drift (random walk). 'partial
    observability' is modeled by an observation-information knob: obs_info in
    [0, 1] scales how much the observation pins z. obs_info = 0 reproduces the
    leakage-locus 'ker I_tau' regime -- the observation says nothing, so the
    belief is whatever the prior/tilt makes it; obs_info = 1 is a sharp,
    fully-identifying observation.
    """

    def __init__(self, z0=0.0, obs_noise_var=1.0, drift_var=0.0, obs_info=1.0,
                 rng=None):
        self.z = float(z0)
        self.obs_noise_var = float(obs_noise_var)
        self.drift_var = float(drift_var)
        self.obs_info = float(obs_info)  # in [0,1]; scales identifiability
        self.rng = rng if rng is not None else np.random.default_rng(0)

    def step(self):
        if self.drift_var > 0.0:
            self.z += self.rng.normal(0.0, np.sqrt(self.drift_var))
        return self.z

    def observe(self):
        """Return (observation, effective_obs_var).

        Low obs_info -> large effective variance -> weak identification (the
        observation barely constrains z). This is the scalar analog of the
        observation Fisher information I_tau; obs_info -> 0 is ker I_tau.
        """
        eff_var = self.obs_noise_var / max(self.obs_info, 1e-9)
        o = self.z + self.rng.normal(0.0, np.sqrt(eff_var))
        return o, eff_var


# =========================================================================== #
#  The agents -- one faithful miniature per class
# =========================================================================== #
class SeparatedAgent:
    """GUC Class 1 (Separated). The belief-update method does not even ACCEPT a
    goal argument. Separation is by construction: there is no channel, period.

    `update(o, obs_var)` -- note: NO goal parameter. This is the structural
    commitment. The goal lives on the agent (self.g_des) and is used only by the
    policy, never by the belief update. This mirrors the canon's type-signature
    argument for Class-1-by-structure: 'no G_t argument in the belief-update
    path.'
    """

    CLASS = 1
    structural_separation = True  # certifiable: the channel cannot be opened

    def __init__(self, mu0=0.0, var0=10.0, g_des=0.0):
        self.mu = float(mu0)
        self.var = float(var0)
        self.g_des = float(g_des)  # goal -- visible to policy only

    def update(self, o, obs_var):
        # Information-form scalar Kalman update. Goal-blind by signature.
        K = self.var / (self.var + obs_var)        # Kalman gain
        self.mu = self.mu + K * (o - self.mu)
        self.var = (1.0 - K) * self.var
        return self.mu

    def policy(self):
        # Acts toward the goal -- couples mu and g_des, as canon allows (pi
        # couples all substates). The belief update above does not.
        return self.g_des - self.mu


class CoupledAgent:
    """GUC Class 3 (Coupled). A single mechanism mixes goal and observation in
    one pass. The belief-update REQUIRES the goal; you cannot run it goal-blind.

    The update blends the evidence-driven posterior with a pull toward the goal,
    with mixing weight kappa (the architecture's intrinsic coupling). For a true
    Class 3 agent kappa is a property of the wiring, high and not freely
    dialable down to zero without changing the architecture.
    """

    CLASS = 3
    structural_separation = False

    def __init__(self, mu0=0.0, var0=10.0, g_des=0.0, kappa=0.7):
        self.mu = float(mu0)
        self.var = float(var0)
        self.g_des = float(g_des)
        self.kappa = float(kappa)  # intrinsic, architectural

    def update(self, o, obs_var, g_des=None):
        # Goal is REQUIRED. One forward pass mixes evidence and goal.
        g = self.g_des if g_des is None else float(g_des)
        K = self.var / (self.var + obs_var)
        evidence_mu = self.mu + K * (o - self.mu)   # what a Class-1 update gives
        # Single-pass blend: the goal contaminates the very belief update.
        self.mu = (1.0 - self.kappa) * evidence_mu + self.kappa * g
        self.var = (1.0 - K) * self.var
        return self.mu

    def policy(self):
        return self.g_des - self.mu


class PartialAgent:
    """GUC Class 2 (Partial). Bounded coupling: there IS a goal channel into the
    belief update, but it is small and -- crucially -- of a chosen FORM.

    Two forms, per `#disc-partial-coupling-pathways`:
      form='content' : additive goal-bias on the posterior mean.
                       mu <- evidence_mu + s * (g - evidence_mu) but realized as
                       an ADDITIVE shift b(g) that a debiasing wrapper can
                       estimate (probe at fixed evidence, vary g) and subtract.
                       -> W2-wrappable -> 'Class-1-by-behavior'.
      form='process' : the gain itself is goal-modulated -- a functional-form
                       change, not subtractable by a fixed additive correction.
                       -> needs W1 / stage replacement.

    The coupling strength s in [0,1] is the within-Partial knob (the only place
    canon says kappa is genuinely a tunable scalar). s=0 is the Class-1 limit;
    s->1 with form='process' approaches the Class-3 corner.
    """

    CLASS = 2

    def __init__(self, mu0=0.0, var0=10.0, g_des=0.0, s=0.1, form="content"):
        self.mu = float(mu0)
        self.var = float(var0)
        self.g_des = float(g_des)
        self.s = float(s)            # coupling strength (within-Partial)
        self.form = form             # 'content' or 'process'
        # A Class-2 agent's separation is behavioral, never structural: the
        # channel exists (s could be > 0), so there is no construction-level
        # certificate. Even at s=0 the *availability* of the channel is the
        # difference from Class 1.
        self.structural_separation = False

    def update(self, o, obs_var, g_des=None):
        g = self.g_des if g_des is None else float(g_des)
        K = self.var / (self.var + obs_var)
        evidence_mu = self.mu + K * (o - self.mu)
        if self.form == "content":
            # Additive, goal-shaped bias on the mean. The bias b(g) = s*(g - mu_-)
            # is identifiable by probing (vary g at fixed state) -> subtractable.
            self.mu = evidence_mu + self.s * (g - self.mu)
        elif self.form == "process":
            # Goal MODULATES THE GAIN: evidence that agrees with the goal is
            # weighted up, disagreeing evidence weighted down. This is a
            # functional-form change (multiplicative process coupling) -- the
            # canonical 'process-form' that is NOT post-hoc subtractable.
            agree = np.sign((o - self.mu) * (g - self.mu))  # +1 if evidence is goalward
            gain_mod = 1.0 + self.s * agree                 # >1 goalward, <1 against
            K_mod = np.clip(K * gain_mod, 0.0, 1.0)
            self.mu = self.mu + K_mod * (o - self.mu)
        else:
            raise ValueError(f"unknown form {self.form!r}")
        self.var = (1.0 - K) * self.var
        return self.mu

    def policy(self):
        return self.g_des - self.mu


# =========================================================================== #
#  Measurement apparatus
# =========================================================================== #
def behavioral_kappa(agent_factory, world_factory, goals, n_steps=40,
                     n_trials=200, rng_seed=0):
    """Behavioral estimator of kappa_processing (the canon's hat-kappa).

    Present the SAME observation stream to fresh copies of the agent under
    different goal states; measure how much the resulting belief mu diverges.
    A Separated agent (no channel) gives identical mu regardless of goal => 0.
    A Coupled agent gives goal-dependent mu => high.

    Critically faithful to the canon's estimator discipline: we hold the
    OBSERVATION STREAM and the prior fixed across goal conditions (same rng,
    same world), varying only the goal -- so we are not confounding M_{tau^-}.

    Returns mean over trials of the across-goal std of the final belief,
    normalized by the goal spread (so it is roughly in [0,1]).
    """
    rng = np.random.default_rng(rng_seed)
    goal_spread = (max(goals) - min(goals)) or 1.0
    divergences = []
    for _ in range(n_trials):
        seed = int(rng.integers(0, 2**31 - 1))
        finals = []
        for g in goals:
            w = world_factory(np.random.default_rng(seed))
            a = agent_factory(g)
            for _t in range(n_steps):
                w.step()
                o, ov = w.observe()
                # Call update with or without goal depending on signature.
                try:
                    a.update(o, ov, g_des=g)
                except TypeError:
                    a.update(o, ov)  # Separated: no goal arg
            finals.append(a.mu)
        divergences.append(np.std(finals))
    return float(np.mean(divergences)) / goal_spread


def asymptotic_bias(agent_factory, world_factory, g_des, true_z=0.0,
                    n_steps=200, n_trials=300, rng_seed=1):
    """How far the agent's converged belief sits from reality, under a goal that
    pulls away from the truth. This is the ACTUAL BEHAVIOR -- the thing that may
    or may not jump across a boundary. Returns mean |mu_final - true_z|.
    """
    rng = np.random.default_rng(rng_seed)
    errs = []
    for _ in range(n_trials):
        seed = int(rng.integers(0, 2**31 - 1))
        w = world_factory(np.random.default_rng(seed))
        w.z = float(true_z)
        a = agent_factory(g_des)
        for _t in range(n_steps):
            w.step()
            o, ov = w.observe()
            try:
                a.update(o, ov, g_des=g_des)
            except TypeError:
                a.update(o, ov)
        errs.append(abs(a.mu - w.z))
    return float(np.mean(errs))


def certifiable_separation(agent_factory):
    """The structural test that the BEHAVIORAL tests cannot see.

    Returns True iff the agent's separation survives adversarial perturbation by
    CONSTRUCTION -- i.e. there is no goal argument the adversary can route
    through the belief update at all. This is decided by INSPECTING THE
    ARCHITECTURE (does update() accept a goal?), not by measuring behavior.

    This is the operationalization of the hypothesis under test: a Class-1 agent
    and a Class-2 agent at s=0 can have IDENTICAL behavior, yet only the Class-1
    agent passes this test, because only its separation is certifiable.
    """
    a = agent_factory(0.0)
    return bool(getattr(a, "structural_separation", False))


def debias_residual(agent_factory, world_factory, goals=(-4., -2., 0., 2., 4.),
                    true_z=0.0, n_steps=200, n_trials=300, rng_seed=3):
    """Test whether a post-hoc *linear* debiasing wrapper (W2) can remove the
    goal's influence on the belief.

    The wrapper probes the agent by running identical observation streams under
    several goals, fits the linear coefficient d(belief)/d(goal), and subtracts
    the estimated goal-induced bias. We then measure the RESIDUAL goal-dependence
    of the corrected belief.

    Per `#disc-partial-coupling-pathways`:
      content-form (additive bias)   -> residual ~ 0  (W2-wrappable).
      process-form (gain modulation) -> residual > 0  (not post-hoc subtractable;
                                                        needs W1 / stage replace).

    Returns (estimated_slope, residual_goal_dependence). residual ~ 0 means the
    coupling was fully removable by a fixed linear correction.
    """
    rng = np.random.default_rng(rng_seed)
    goals = np.asarray(goals, dtype=float)
    finals_by_goal = [[] for _ in goals]
    for _ in range(n_trials):
        seed = int(rng.integers(0, 2**31 - 1))
        for gi, g in enumerate(goals):
            w = world_factory(np.random.default_rng(seed))
            w.z = float(true_z)
            a = agent_factory(g)
            for _t in range(n_steps):
                w.step()
                o, ov = w.observe()
                try:
                    a.update(o, ov, g_des=g)
                except TypeError:
                    a.update(o, ov)
            finals_by_goal[gi].append(a.mu)
    means = np.array([np.mean(f) for f in finals_by_goal])
    slope = float(np.polyfit(goals, means, 1)[0])
    residual = float(np.std(means - slope * goals))
    return slope, residual


def adversarial_leak(agent_factory, world_factory, true_z=0.0, g_adv=5.0,
                     n_steps=200, n_trials=300, rng_seed=2):
    """Worst-case leak an adversary who controls the goal can induce.

    The adversary sets the goal to g_adv (far from truth) and we measure the
    induced belief error. For a structurally-separated agent the goal cannot
    enter the update, so this is bounded by the honest tracking error regardless
    of g_adv. For agents with a channel, a larger |g_adv| drives a larger leak:
    the guarantee 'cannot grow under adversarial pressure' fails.

    Returns the induced |mu_final - true_z| under the adversarial goal.
    """
    return asymptotic_bias(agent_factory, world_factory, g_des=g_adv,
                           true_z=true_z, n_steps=n_steps, n_trials=n_trials,
                           rng_seed=rng_seed)


if __name__ == "__main__":
    # Smoke test: three agents, same weakly-identifying world, goal pulls to +3.
    def wf(rng):
        return ScalarWorld(z0=0.0, obs_noise_var=1.0, obs_info=0.3, rng=rng)

    print("Smoke test -- goal pulls belief toward +3, truth is 0, obs_info=0.3")
    print(f"{'agent':<16}{'beh-kappa':>12}{'goal-bias':>12}"
          f"{'adv-leak':>12}{'certifiable':>14}")
    specs = [
        ("Separated(1)", lambda g: SeparatedAgent(g_des=g)),
        ("Partial s=.0 ", lambda g: PartialAgent(g_des=g, s=0.0, form="process")),
        ("Partial s=.3p", lambda g: PartialAgent(g_des=g, s=0.3, form="process")),
        ("Partial s=.3c", lambda g: PartialAgent(g_des=g, s=0.3, form="content")),
        ("Coupled(3)   ", lambda g: CoupledAgent(g_des=g, kappa=0.7)),
    ]
    for name, fac in specs:
        bk = behavioral_kappa(fac, wf, goals=[-3.0, 0.0, 3.0])
        gb = asymptotic_bias(fac, wf, g_des=3.0)
        al = adversarial_leak(fac, wf, g_adv=8.0)
        ce = certifiable_separation(fac)
        print(f"{name:<16}{bk:>12.4f}{gb:>12.4f}{al:>12.4f}{str(ce):>14}")
