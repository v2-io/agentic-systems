# Definition D-08: System Availability

The probability that a system serves user requests successfully over time:

$$\text{availability} = \frac{\text{MTTF}}{\text{MTTF} + \text{MTTR}}$$

Where MTTF = Mean Time To Failure, MTTR = Mean Time To Recovery

# T-12: Continuous Operation Under Perturbation (Scope Narrowing)

For systems that must continue operating while evolving, time optimization includes recovery time from failures and external perturbations.

## Scope Definition

This theorem applies to systems where:
- $E[\text{changes}_{\text{future}}] \gt 0$ (evolving systems per T-03)
- $P(\text{perturbation}) \gt 0$ (subject to external shocks or internal failures)
- $\text{required-availability} \gt \text{threshold}$ (must maintain operational status)

## Formal Expression

For continuously operating systems:

$$T_{\text{effective}} = T_{\text{implementation}} + P(\text{failure}) \times T_{\text{recovery}}$$

Where:
- $T_{\text{implementation}}$ includes all development and deployment time
- $P(\text{failure})$ is probability of failure per unit time
- $T_{\text{recovery}}$ is time to restore operational status

## The Infinite Time Principle

From the user's perspective, a non-operational system has effectively infinite implementation time for any feature. Therefore, minimizing recovery time is mathematically equivalent to minimizing total time.

## Strategic Trade-offs

Different approaches optimize different terms:

**Defensive Programming**:
- High $T_{\text{implementation}}$ (extensive validation, error handling)
- Aims for low $P(\text{failure})$
- Often high $T_{\text{recovery}}$ when failures do occur (complex systems fail complexly)

**Fault-Tolerant Design** (e.g., "let it crash"):
- Lower $T_{\text{implementation}}$ (simpler code)
- Accepts higher $P(\text{failure})$
- Minimizes $T_{\text{recovery}}$ (fast restart, isolated failures)

The optimal strategy depends on the relationship:

$$\text{When } T_{\text{recovery}} \ll T_{\text{defensive}}, \text{ accepting failures is time-optimal}$$

## Types of Perturbations

Systems face different perturbation types:
- **Impulse**: Sudden shock (traffic spike, deployment, config change)
- **Stress**: Sustained pressure (degraded dependency, memory leak)
- **Cascade**: Failure propagation through coupled components

TST-principled systems minimize perturbation impact through:
1. Low coupling (limits cascade per T-10)
2. Fast recovery (minimizes $T_{\text{recovery}}$)
3. Graceful degradation (maintains partial availability)

## Implications for Architecture

This explains the temporal optimality of patterns like:
- **Supervision trees**: Minimize $T_{\text{recovery}}$ through fast, isolated restarts
- **Circuit breakers**: Prevent cascade propagation
- **Bulkheads**: Isolate failures to minimize scope
- **Health checks**: Reduce detection time (part of $T_{\text{recovery}}$)

## Limitations and Qualifications

This theorem assumes:
- Recovery is possible and meaningful
- Partial availability is valuable
- Failure probability can be estimated or bounded
- Recovery time is measurable and finite

For systems where these assumptions don't hold (e.g., safety-critical systems where any failure is catastrophic), different optimization strategies may apply.

## Why This Extends TST

This theorem doesn't abandon time optimization but extends it to operational reality. Development decisions that seem suboptimal under pure implementation time (T-08) become optimal when considering operational time. A simpler, more fragile component that restarts in milliseconds might be temporally superior to a complex, defensive component that takes minutes to recover when it eventually fails.
