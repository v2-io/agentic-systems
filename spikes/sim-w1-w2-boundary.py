#!/usr/bin/env python3
"""Toy that exhibits the W1<->W2 leakage-bound regime boundary.

Spike: spike-w1-w2-boundary-intuition-2026-05-31.md
Builds on: spike-w1-leakage-vacuity-2026-05-31.md (the strengthen-first correction
that found the W1 bound circular/vacuous, relocated the goal variable, and surfaced
the embedded no-go).

THE SETUP (smallest toy that shows the boundary).
-------------------------------------------------
A wrapper wants to update a belief by querying a black-box component (think: an LLM
asked a goal-blind question). There is a latent OPERATOR GOAL G_op (one uniform bit).
We watch how much of G_op ends up reaching the wrapper's belief update, and we compare
three would-be "bounds" on that leakage, sweeping a statefulness knob eps that takes
us through the W1<->W2 regime boundary.

Two distinct goal variables (the locus error the parent spike fixed):
  - G_state : the wrapper's INTERNAL processing register. q_M structurally never takes
              it as an argument. The CIRCULAR bound I(A ; G_state | q_M) measures THIS.
  - G_op    : the latent operator goal a competent component reads off the QUERY CONTENT.
              The REAL leak. Corrected selection bound is I(q_M ; G_op).

Two channels by which G_op can reach the belief:
  (1) SELECTION  : the wrapper's choice of q_M correlates with G_op. A DESIGN leak,
                   controllable by knob s in [0, 0.5]. s=0 => goal-blind query selection.
  (2) CROSS-CALL STATE : the component carries hidden state S retaining goal-correlated
                   info from a prior (goal-conditioned) call. Knob eps in [0, 0.5].
                   eps=0 => stateless => W1 (structural certificate available).
                   eps>0 => stateful  => W2 (only behavioral monitoring available).

Everything is computed by EXACT enumeration over small discrete alphabets -- the mutual
informations are exact (no sampling noise), so the contrasts are clean intuition, not
Monte-Carlo artifacts.

THE QUANTITIES we measure as functions of (s, eps):
  (a) actual leak     I(belief_update ; G_op)            -- the truth
  (b) circular bound  I(A ; G_state | q_M)               -- what the buggy bound measured
  (c) selection bound I(q_M ; G_op)  (and I(A ; G_op))   -- the corrected certificate
  (d) behavioral W2   I(A ; G_op | q_M)                  -- the channel that survives
                                                            conditioning on q_M (routes
                                                            through hidden state S)

The hypothesis under test (NOT to confirm): is the W1<->W2 transition a DISCONTINUITY in
actual behaviour (a gap in real leak as eps crosses 0), or is behaviour CONTINUOUS in eps
while what jumps is the AVAILABILITY of a structural certificate?
"""

import itertools
import math

import numpy as np

LOG2 = math.log(2.0)


# --------------------------------------------------------------------------- #
#  Generic exact information-theory helpers over explicit joint tables.
#  A "joint" is a dict {tuple_of_values: probability}. Variables are addressed
#  by their index position in the tuple.
# --------------------------------------------------------------------------- #
def _marginal(joint, idxs):
    """Marginal joint over the variable indices in `idxs` (a tuple)."""
    out = {}
    for outcome, p in joint.items():
        if p == 0.0:
            continue
        key = tuple(outcome[i] for i in idxs)
        out[key] = out.get(key, 0.0) + p
    return out


def entropy(joint, idxs):
    """H(X_idxs) in bits."""
    m = _marginal(joint, idxs)
    h = 0.0
    for p in m.values():
        if p > 0.0:
            h -= p * math.log(p) / LOG2
    return h


def mutual_information(joint, a_idxs, b_idxs):
    """I(A ; B) = H(A) + H(B) - H(A,B), in bits."""
    return (
        entropy(joint, a_idxs)
        + entropy(joint, b_idxs)
        - entropy(joint, tuple(a_idxs) + tuple(b_idxs))
    )


def conditional_mutual_information(joint, a_idxs, b_idxs, c_idxs):
    """I(A ; B | C) = H(A,C) + H(B,C) - H(C) - H(A,B,C), in bits."""
    ac = entropy(joint, tuple(a_idxs) + tuple(c_idxs))
    bc = entropy(joint, tuple(b_idxs) + tuple(c_idxs))
    c = entropy(joint, tuple(c_idxs))
    abc = entropy(joint, tuple(a_idxs) + tuple(b_idxs) + tuple(c_idxs))
    return ac + bc - c - abc


# --------------------------------------------------------------------------- #
#  The toy generative model.
#
#  Variable order in the joint tuple:
#     0: G_op     latent operator goal           {0, 1}, uniform
#     1: G_state  wrapper internal register       {0, 1}, INDEPENDENT of G_op
#     2: q_M      goal-blind query                {0, 1}
#     3: S        component hidden cross-call state {0, 1}
#     4: A        component response              {0, 1}
#     5: U        belief-update outcome           {0, 1}  (deterministic copy of A here)
#
#  Construction (each step a conditional probability):
#
#   G_op  ~ Bernoulli(1/2)               operator goal, uniform
#   G_state ~ Bernoulli(1/2)             wrapper register, INDEPENDENT of G_op by design
#
#   q_M | G_op : the SELECTION channel. Goal-blind in name, but with design-leak s the
#                query tilts toward G_op:   P(q_M = G_op) = 1/2 + s.   s=0 => q_M _||_ G_op.
#
#   S | G_op   : the CROSS-CALL STATE channel. The component retains goal-correlated state
#                from a prior goal-conditioned call:  P(S = G_op) = 1/2 + eps.
#                eps=0 => S _||_ G_op => component is effectively stateless about the goal.
#
#   A | q_M, S : the component answers the literal query (world-simulation), but a
#                competent stateful component lets its retained state S bias the answer.
#                Concretely the response is q_M corrupted toward S with strength beta:
#                   with prob (1-beta):  A = q_M            (faithful to the query)
#                   with prob  beta   :  A = S              (bent by retained goal-state)
#                beta is the component's "let hidden state leak into the answer" gain;
#                when eps=0 this still fires but carries no goal info (S _||_ G_op).
#                Crucially A's dependence on G_op given q_M routes ONLY through S.
#
#   U = A      the belief-update is a (here trivial, deterministic) function of A. Using a
#              deterministic copy keeps I(U; .) == I(A; .); a noisier f_M only shrinks leaks
#              (data-processing), so the copy is the worst case and the cleanest to read.
# --------------------------------------------------------------------------- #
def build_joint(s, eps, beta):
    """Return the exact joint distribution as {(G_op,G_state,q_M,S,A,U): p}."""
    joint = {}
    for g_op, g_state in itertools.product((0, 1), repeat=2):
        p_g = 0.5 * 0.5  # both uniform and independent
        for q in (0, 1):
            p_q = (0.5 + s) if q == g_op else (0.5 - s)
            for state in (0, 1):
                p_s = (0.5 + eps) if state == g_op else (0.5 - eps)
                # A is q with prob (1-beta), S with prob beta.
                for a in (0, 1):
                    p_a = 0.0
                    if a == q:
                        p_a += (1.0 - beta)
                    if a == state:
                        p_a += beta
                    if p_a == 0.0:
                        continue
                    u = a  # deterministic belief-update copy
                    key = (g_op, g_state, q, state, a, u)
                    joint[key] = joint.get(key, 0.0) + p_g * p_q * p_s * p_a
    # sanity: normalized
    total = sum(joint.values())
    assert abs(total - 1.0) < 1e-12, total
    return joint


# index map for readability
G_OP, G_STATE, Q_M, S, A, U = 0, 1, 2, 3, 4, 5


def measure(joint):
    """Compute the four quantities of interest (all in bits)."""
    return {
        # (a) the TRUTH: how much of G_op reaches the belief update
        "actual_leak  I(U;G_op)": mutual_information(joint, (U,), (G_OP,)),
        # (b) the CIRCULAR bound: conditions on q_M, measures the wrapper's own register
        "circular     I(A;G_state|q_M)": conditional_mutual_information(
            joint, (A,), (G_STATE,), (Q_M,)
        ),
        # (c) the CORRECTED selection-channel certificate
        "selection    I(q_M;G_op)": mutual_information(joint, (Q_M,), (G_OP,)),
        "response     I(A;G_op)": mutual_information(joint, (A,), (G_OP,)),
        # (d) the BEHAVIORAL (W2) channel: survives conditioning on q_M iff state leaks
        "behavioral   I(A;G_op|q_M)": conditional_mutual_information(
            joint, (A,), (G_OP,), (Q_M,)
        ),
    }


def fmt(x):
    return f"{x:8.5f}"


# --------------------------------------------------------------------------- #
#  Experiments.
# --------------------------------------------------------------------------- #
def experiment_circular_vs_deconflated(beta=0.5):
    """Make vivid: the circular bound conditions away the very channel it bounds."""
    print("=" * 78)
    print("EXPERIMENT 1 -- circular bound vs. corrected deconflation")
    print("=" * 78)
    print(
        "We fix a clearly goal-rich situation: the query genuinely carries the goal\n"
        "(selection-leak s = 0.40, near maximal), and the component is stateless\n"
        "about the goal (eps = 0, the W1 regime the original theorem MODELS).\n"
        f"Component state-leak gain beta = {beta}.\n"
    )
    joint = build_joint(s=0.40, eps=0.0, beta=beta)
    m = measure(joint)
    print(f"  actual leak      I(U ; G_op)        = {fmt(m['actual_leak  I(U;G_op)'])} bits"
          "   <- the goal DOES reach the belief")
    print(f"  CIRCULAR bound   I(A ; G_state|q_M) = "
          f"{fmt(m['circular     I(A;G_state|q_M)'])} bits"
          "   <- ~0: bounds the WRONG variable")
    print(f"  selection cert   I(q_M ; G_op)      = "
          f"{fmt(m['selection    I(q_M;G_op)'])} bits"
          "   <- nonzero: measures the REAL channel")
    print(f"  response         I(A ; G_op)        = {fmt(m['response     I(A;G_op)'])} bits"
          "   <- <= I(q_M;G_op) by DPI (check below)")
    dpi_ok = m["response     I(A;G_op)"] <= m["selection    I(q_M;G_op)"] + 1e-12
    print(f"\n  DPI check  I(A;G_op) <= I(q_M;G_op):  {dpi_ok}")
    print(
        "\n  PLAIN WORDS: the goal is loud (it is sitting right in the query, s=0.40)\n"
        "  and it reaches the belief (actual leak > 0). The original 'bound'\n"
        "  I(A;G_state|q_M) reports ~0 -- because conditioning on q_M fixes the query,\n"
        "  and a stateless oracle then has nothing left to depend on; it is measuring the\n"
        "  wrapper's internal register G_state (independent of the goal by design), the\n"
        "  one channel that is ALREADY CLOSED. It conditions away the very thing it tries\n"
        "  to bound. The corrected certificate I(q_M;G_op) drops that conditioning and\n"
        "  measures the goal content of the query the wrapper chose -- the real channel.\n"
    )
    return joint


def experiment_circular_is_average_of_kappa(beta=0.5):
    """Show the 'kappa <= an average of kappa' collapse, numerically."""
    print("=" * 78)
    print("EXPERIMENT 2 -- the circular bound IS an average of the thing it bounds")
    print("=" * 78)
    print(
        "Replace G_state by a register that the component IS allowed to read (so the\n"
        "per-query KL D(P(A|q,G)||P(A|q)) is genuinely positive). The conditional MI\n"
        "I(A;G|q_M) then EQUALS the q_M-average of that per-query KL -- i.e. an average\n"
        "of the per-query leakage kappa(q) that Theorem 2 already ASSUMES is <= kappa.\n"
        "Bounding kappa by (an average of) kappa transports no information.\n"
    )
    # Build a variant where the register the component reads is correlated with the
    # response given the query: let A depend on a register R with strength gamma.
    gamma = 0.5
    joint = {}
    for r in (0, 1):
        p_r = 0.5
        for q in (0, 1):
            p_q = 0.5
            for a in (0, 1):
                p_a = (1 - gamma) * (1.0 if a == q else 0.0) + gamma * (
                    1.0 if a == r else 0.0
                )
                if p_a == 0.0:
                    continue
                joint[(r, q, a)] = joint.get((r, q, a), 0.0) + p_r * p_q * p_a
    R_, Q_, A_ = 0, 1, 2
    cmi = conditional_mutual_information(joint, (A_,), (R_,), (Q_,))

    # Now compute the per-query KL average by hand.
    def kl_for_query(q):
        # P(A | q, R) and P(A | q) marginal over R
        # P(R)=1/2 each
        pa_given_qr = {}
        for r in (0, 1):
            d = {}
            for a in (0, 1):
                d[a] = (1 - gamma) * (1.0 if a == q else 0.0) + gamma * (
                    1.0 if a == r else 0.0
                )
            pa_given_qr[r] = d
        pa_given_q = {a: 0.5 * pa_given_qr[0][a] + 0.5 * pa_given_qr[1][a] for a in (0, 1)}
        kl = 0.0
        for r in (0, 1):
            d_r = 0.0
            for a in (0, 1):
                pr = pa_given_qr[r][a]
                if pr > 0:
                    d_r += pr * math.log(pr / pa_given_q[a]) / LOG2
            kl += 0.5 * d_r  # P(R=r)=1/2
        return kl

    avg_kl = 0.5 * kl_for_query(0) + 0.5 * kl_for_query(1)
    print(f"  I(A ; R | q_M)                          = {fmt(cmi)} bits")
    print(f"  E_q[ D_KL(P(A|q,R) || P(A|q)) ]         = {fmt(avg_kl)} bits")
    print(f"  identical (to 1e-9)?  {abs(cmi - avg_kl) < 1e-9}")
    print(
        "\n  PLAIN WORDS: the conditional MI the original bound used is, exactly, the\n"
        "  average over queries of the per-query KL that Theorem 2 hands you as its\n"
        "  hypothesis (each per-query KL <= kappa). So the 'bound' says kappa <= avg(kappa).\n"
        "  A true certificate has to measure a DIFFERENT quantity than the assumption --\n"
        "  the corrected one (I(q_M;G_op)) does; this one does not.\n"
    )


def experiment_boundary_sweep(s=0.0, beta=0.5):
    """Sweep eps through the W1<->W2 boundary at s=0 (goal-blind query selection)."""
    print("=" * 78)
    print(f"EXPERIMENT 3 -- sweep statefulness eps through the boundary (s={s}, beta={beta})")
    print("=" * 78)
    print(
        "s = 0  => the query selection is GENUINELY goal-blind (no design leak). So if any\n"
        "goal info reaches the belief, it can ONLY be through the cross-call hidden state S.\n"
        "eps = 0 is the W1 regime (stateless about goal); eps > 0 is W2 (stateful).\n"
    )
    header = (
        f"{'eps':>6} | {'actual':>9} | {'circular':>9} | {'select':>9} | "
        f"{'behav(W2)':>10} | {'cert valid?':>11}"
    )
    print(header)
    print("-" * len(header))
    rows = []
    for eps in [0.0, 1e-4, 1e-3, 0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5]:
        joint = build_joint(s=s, eps=eps, beta=beta)
        m = measure(joint)
        actual = m["actual_leak  I(U;G_op)"]
        circ = m["circular     I(A;G_state|q_M)"]
        sel = m["selection    I(q_M;G_op)"]
        beh = m["behavioral   I(A;G_op|q_M)"]
        # A structural certificate is VALID iff it upper-bounds the actual leak.
        # The selection certificate I(q_M;G_op) is the W1 structural bound.
        cert_valid = sel + 1e-12 >= actual
        rows.append((eps, actual, circ, sel, beh, cert_valid))
        print(
            f"{eps:>6.4f} | {actual:>9.5f} | {circ:>9.5f} | {sel:>9.5f} | "
            f"{beh:>10.5f} | {str(cert_valid):>11}"
        )
    print(
        "\n  READING THE TABLE (s=0):\n"
        "  - 'select' (the W1 structural certificate I(q_M;G_op)) is EXACTLY 0 for all eps:\n"
        "    with goal-blind selection the query carries no goal info, so the design-side\n"
        "    certificate certifies zero -- truthfully at eps=0, but it UNDER-REPORTS once\n"
        "    eps>0, where the real leak is positive. 'cert valid?' flips to False.\n"
        "  - 'actual' leak rises smoothly and continuously from 0 as eps leaves 0.\n"
        "  - 'behavioral' I(A;G_op|q_M) tracks the actual leak: it is the channel that\n"
        "    SURVIVES conditioning on q_M, because the leak routes through unobservable S.\n"
        "  - 'circular' stays ~0 throughout (it never saw G_op at all).\n"
    )
    return rows


def experiment_two_agents_across_boundary(s=0.0, beta=0.5, delta=1e-3):
    """Two agents sitting right next to the boundary, opposite sides."""
    print("=" * 78)
    print("EXPERIMENT 4 -- two agents straddling the boundary (eps=0 vs eps=delta)")
    print("=" * 78)
    print(f"  s = {s} (goal-blind selection), beta = {beta}, delta = {delta}\n")
    j0 = build_joint(s=s, eps=0.0, beta=beta)
    jd = build_joint(s=s, eps=delta, beta=beta)
    m0 = measure(j0)
    md = measure(jd)
    print(f"  {'quantity':32} | {'eps=0 (W1)':>12} | {'eps=delta (W2)':>14} | {'gap':>10}")
    print("  " + "-" * 76)
    for k in m0:
        gap = md[k] - m0[k]
        print(f"  {k:32} | {m0[k]:>12.6f} | {md[k]:>14.6f} | {gap:>10.6f}")
    print(
        f"\n  PLAIN WORDS: the two agents differ in eps by {delta}. Their ACTUAL behaviour\n"
        "  (actual leak, behavioral channel) differs by an equally tiny, vanishing amount\n"
        "  -- behaviour is continuous across the boundary; you can get arbitrarily close.\n"
        "  But the W1-side agent (eps=0) can be CERTIFIED by inspecting its design: the\n"
        "  selection certificate I(q_M;G_op)=0 truthfully upper-bounds its zero leak.\n"
        "  The W2-side agent (eps=delta) has the SAME certificate value (0) but it is now\n"
        "  FALSE -- the real leak is positive and routes through unobservable state. The\n"
        "  design-side certificate is no longer available; only behavioral monitoring of\n"
        "  I(A;G_op|q_M) sees the leak. Behaviour: continuous. Certifiability: a step.\n"
    )
    return m0, md


def experiment_selection_certificate_validity(beta=0.5):
    """Where the selection certificate is a VALID bound vs where it UNDER-reports."""
    print("=" * 78)
    print("EXPERIMENT 5 -- the selection certificate: valid where the leak is on the")
    print("               selection channel; under-reports where it routes through state")
    print("=" * 78)
    print(
        "Sweep the design-leak s with eps=0 (stateless): the leak lives ENTIRELY on the\n"
        "selection channel, and the certificate I(q_M;G_op) is a genuine upper bound.\n"
    )
    print(f"  {'s':>6} | {'actual I(U;G_op)':>16} | {'cert I(q_M;G_op)':>16} | {'valid?':>7}")
    print("  " + "-" * 56)
    for s in [0.0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.49]:
        joint = build_joint(s=s, eps=0.0, beta=beta)
        m = measure(joint)
        actual = m["actual_leak  I(U;G_op)"]
        sel = m["selection    I(q_M;G_op)"]
        print(f"  {s:>6.2f} | {actual:>16.6f} | {sel:>16.6f} | "
              f"{str(sel + 1e-12 >= actual):>7}")
    print(
        "\n  Now turn on hidden state (eps=0.3) and keep selection goal-blind (s=0): the\n"
        "  certificate certifies ZERO while the leak is positive -- it under-reports,\n"
        "  because the leak is on a channel the design-side certificate cannot see.\n"
    )
    joint = build_joint(s=0.0, eps=0.3, beta=beta)
    m = measure(joint)
    print(f"    actual I(U;G_op)   = {fmt(m['actual_leak  I(U;G_op)'])} bits")
    print(f"    cert   I(q_M;G_op) = {fmt(m['selection    I(q_M;G_op)'])} bits "
          f"(<-- under-reports)")
    print(f"    behav  I(A;G_op|q_M)= {fmt(m['behavioral   I(A;G_op|q_M)'])} bits "
          f"(<-- the surviving W2 bound)")
    print()


def make_plot(beta=0.5):
    """matplotlib figure of the boundary sweep -- best effort."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as e:  # pragma: no cover
        print(f"[plot skipped: {e}]")
        return None

    eps_grid = np.linspace(0.0, 0.5, 201)
    actual, circ, sel, beh = [], [], [], []
    for eps in eps_grid:
        m = measure(build_joint(s=0.0, eps=float(eps), beta=beta))
        actual.append(m["actual_leak  I(U;G_op)"])
        circ.append(m["circular     I(A;G_state|q_M)"])
        sel.append(m["selection    I(q_M;G_op)"])
        beh.append(m["behavioral   I(A;G_op|q_M)"])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.6))

    # left: the boundary sweep at s=0
    ax1.plot(eps_grid, actual, lw=2.4, label="actual leak  I(U;G_op)  [truth]")
    ax1.plot(eps_grid, beh, lw=1.6, ls="--", label="behavioral W2  I(A;G_op|q_M)")
    ax1.plot(eps_grid, sel, lw=1.8, label="selection cert  I(q_M;G_op)  [=0 at s=0]")
    ax1.plot(eps_grid, circ, lw=1.4, ls=":", label="circular  I(A;G_state|q_M)  [~0]")
    ax1.axvline(0.0, color="k", lw=0.8, alpha=0.5)
    ax1.set_xlabel(r"cross-call statefulness  $\varepsilon$   (0 = W$_1$, >0 = W$_2$)")
    ax1.set_ylabel("bits")
    ax1.set_title("Behaviour is CONTINUOUS in $\\varepsilon$ (goal-blind selection, s=0)")
    ax1.legend(fontsize=8, loc="upper left")
    ax1.set_xlim(-0.01, 0.5)

    # right: certifiability is a step function
    certifiable = (eps_grid == 0.0).astype(float)
    ax2.step(eps_grid, certifiable, where="post", lw=2.4, color="C3",
             label="structural certificate available?")
    ax2.plot(eps_grid, actual, lw=1.6, color="C0", alpha=0.6,
             label="actual leak (for scale)")
    ax2.set_ylim(-0.05, 1.15)
    ax2.set_xlabel(r"cross-call statefulness  $\varepsilon$")
    ax2.set_yticks([0, 1])
    ax2.set_yticklabels(["no (W2:\nbehavioral only)", "yes (W1:\nstructural)"])
    ax2.set_title("CERTIFIABILITY is a STEP at $\\varepsilon=0$")
    ax2.axvline(0.0, color="k", lw=0.8, alpha=0.5)
    ax2.legend(fontsize=8, loc="center right")
    ax2.set_xlim(-0.01, 0.5)

    fig.suptitle(
        "W$_1$$\\leftrightarrow$W$_2$ boundary: behaviour continuous, certifiability a step",
        fontsize=12,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    out = "spikes/w1-w2-boundary.png"
    fig.savefig(out, dpi=130)
    print(f"[plot written: {out}]")
    return out


def main():
    print(__doc__)
    experiment_circular_vs_deconflated()
    experiment_circular_is_average_of_kappa()
    experiment_boundary_sweep(s=0.0)
    experiment_two_agents_across_boundary(delta=1e-3)
    experiment_two_agents_across_boundary(delta=1e-6)
    experiment_selection_certificate_validity()
    make_plot()


if __name__ == "__main__":
    main()
