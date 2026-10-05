# Round r002 — fit report

Observations (triple-level, cumulative): 7732. Minds: synA, synB, synC, synD.

## Candidate sequences (best chain), by family-mean perception

s3 = perception in triads, s4 = in sets of 4+, per family (mean over its minds). support = share of chains and posterior samples holding a matching candidate.

| # | sequence | n | support | famX s3/s4 | famY s3/s4 | famZ s3/s4 |
|---|---|---|---|---|---|---|
| 3 | `▇ ▆ ▅ ▄ ▃ ▂ ▁` | 7 | 1.00 | 0.85/0.94 | 0.65/0.80 | 0.65/0.90 |
| 2 | `⚀ ⚁ ⚂=⚃ ⚄ ⚅` | 6 | 1.00 | 0.78/0.94 | 0.65/0.97 | 0.65/0.65 |
| 0 | `⑧ ⑦ ⑥ ⑤ ④ ③ ② ①` | 8 | 1.00 | 0.89/0.90 | 0.65/0.97 | 0.35/0.65 |
| 1 | `○ ◔ ◑ ◕ ●` | 5 | 1.00 | 0.07/0.81 | 0.10/0.90 | 0.00/0.80 |
| 4 | `⑤ ⑷ ⑸ ⑹` | 4 | 1.00 | 0.70/0.73 | 0.50/0.65 | 0.90/0.65 |

## Minds: nuisance parameters

| mind | eps | nn | nt | beta | tau |
|---|---|---|---|---|---|
| synA | 0.1 | 0.8 | 0.1 | 0.34 | 0.7 |
| synB | 0.15 | 0.6 | 0.2 | 0.65 | 0.9 |
| synC | 0.1 | 0.6 | 0.2 | 0.34 | 0.9 |
| synD | 0.6 | 0.4 | 0.2 | 0.5 | 0.9 |

## Minds: slot bias read directly from the Latin rotations (no model)

Over triads whose three rotations were all answered with an order: share of answers naming the glyph shown in the middle (1/3 = no slot preference), and share of triads given the same middle in all three rotations.

| mind | triads | middle = shown middle | same middle 3/3 |
|---|---|---|---|
| synA | 22 | 0.35 | 0.95 |
| synB | 8 | 0.46 | 0.75 |
| synC | 13 | 0.36 | 0.92 |
| synD | 10 | 0.67 | 0.00 |

## Parse status this round

- synA|ok: 192
- synB|ok: 192
- synC|ok: 192
- synD|ok: 192
