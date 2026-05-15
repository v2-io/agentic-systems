---
slug: adaptive-gain-dynamics
schema_version: 1
term: adaptive gain dynamics
name: Adaptive Gain Dynamics
notation:
brief: The extension of sector-persistence to agents whose update gain is itself a state variable — deriving four conditions (MG-1 through MG-4) under which adaptive-gain schemes stay within the A2' sub-scope.
layer: framing-vocabulary
status: canon
tags: [structural_concepts, core_quantities]
source_type: asf
primary_source: 01-aat-core/src/deriv-adaptive-gain-dynamics.md
first_asf_mention: 01-aat-core/src/deriv-adaptive-gain-dynamics.md
see_also: [adaptive-system, adaptive-tempo, adaptive-reserve, sector-condition, structural-persistence]
aliases: []
do_not_confuse: []
---

Real adaptive agents often learn their noise model (adaptive Kalman), switch regimes (IMM),
or adapt step-size online (Adam/RMSProp). When the gain $K_t$ becomes a state variable, the
question is whether the sector-persistence machinery extends to the augmented state
$z_t = (\delta_t, \tilde K_t)$.

Four conditions — **(MG-1) Primary sector floor under bounded gain error**, **(MG-2) Meta-gain
sector condition**, **(MG-3) Timescale separation** ($\alpha_K \ll \underline\alpha$), and
**(MG-4) Coupling boundedness** — together give an augmented-state sector-persistence result
via standard two-timescale Lyapunov composition (Khalil 2002 Thm 4.18). When all four are
derivable from the update-rule structure, the agent is in sub-scope $\alpha_2$ — a new tier
refining the existing A2' partition.

The sub-scope partition becomes: $\alpha_1$ (fixed-gain, A2' derived), $\alpha_2$ (adaptive-gain,
A2' derived through augmented-state Lyapunov), and $\beta$ (A2' assumed). Concrete instances:
adaptive Kalman with Mehra estimator lands in $\alpha_2$; RMSProp on strongly-convex loss lands
in $\alpha_2$ under design conditions (AMSGrad as $\alpha_2$-preserving repair); MAML outer loop
lands in $\beta$.

Derived in [`#deriv-adaptive-gain-dynamics`](../../01-aat-core/src/deriv-adaptive-gain-dynamics.md).
