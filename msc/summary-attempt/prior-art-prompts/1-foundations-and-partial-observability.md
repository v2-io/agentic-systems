Please conduct a deep prior-art search across academic literature. We are establishing scientific precedence for a theoretical framework of agency (AAT).

## The Core Idea / Claim
An agent's internal model of reality is fundamentally a many-to-one compression of a strictly irreversible, non-forkable sequence of events (the "chronica"). Because the agent has partial observability and constrained computation, its state updates must be recursive (Markovian). Furthermore, the optimal compression of this history is defined by the Information Bottleneck principle: maximizing predictive information about future observations while minimizing retained historical data.

## Boundaries of the Claim
- Assumes strict partial observability (the agent never accesses true environment states).
- Assumes computational constraints that force recursive updates (cannot store the full history).
- Domain: Theoretical computer science, control theory, reinforcement learning (RL) theory, active inference.

## What Kind of Match Counts
- Formalisms treating agent history as singular, discrete event sequences (chronica-like).
- Proofs or derivations showing that recursive/Markovian updates are structurally forced by causality or compute limits in adaptive systems.
- Papers formally applying Tishby's Information Bottleneck to predictive state representations, internal agent models, or memory in POMDPs.
- Conceptual predecessors recognizing "Model class fitness" or quantifying how much predictive info a specific representational class retains.

## What Would NOT Count
- General RL memory buffers (e.g., standard experience replay) that do not address information-theoretic compression limits.
- Standard POMDP literature that just uses belief states without framing them as an optimal rate-distortion/Information Bottleneck compression of history.

## Known Anchors
- Tishby (Information Bottleneck)
- Predictive State Representations (PSRs)
- Active Inference / Free Energy Principle

## Search Scope
- Broad conceptual predecessors and mathematical formalisms.
- Look back as far as early Cybernetics (1950s) up to modern RL theory.
- Strictly academic papers (no patents/IP).