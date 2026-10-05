# Round r003 — fit report

Observations (triple-level, cumulative): 10040. Minds: synA, synB, synC, synD.

## Candidate sequences (best chain), by family-mean perception

s3 = perception in triads, s4 = in sets of 4+, per family (mean over its minds). support = share of chains and posterior samples holding a matching candidate.

| # | sequence | n | support | famX s3/s4 | famY s3/s4 | famZ s3/s4 |
|---|---|---|---|---|---|---|
| 0 | `⑧ ⑦ ⑥ ⑤ ④ ③ ② ①` | 8 | 1.00 | 0.85/0.97 | 0.65/0.97 | 0.80/0.65 |
| 1 | `⚅ ⚄ ⚂ ⚁ ⚀` | 5 | 1.00 | 0.00/0.94 | 0.00/0.97 | 0.00/0.65 |
| 3 | `▁ ▂ ▃ ▄ ▅ ▆ ▇` | 7 | 1.00 | 0.89/0.89 | 0.65/0.97 | 0.65/0.65 |
| 2 | `○ ◔ ◑ ◕ ●` | 5 | 1.00 | 0.03/0.81 | 0.03/0.80 | 0.00/0.80 |
| 5 | `⑹ ⑸ ⑷ ⑤ ⑶ ⑵` | 6 | 1.00 | 0.85/0.57 | 0.50/0.35 | 0.65/0.97 |
| 4 | `⑹ ⑸ ⑷ ⑶ ⑵` | 5 | 1.00 | 0.00/0.48 | 0.00/0.80 | 0.00/0.97 |
| 6 | `⚅ ⚄ ⚃=⚂ ⚁ ⚀` | 6 | 1.00 | 0.89/0.20 | 0.65/0.20 | 0.65/0.00 |

## Minds: nuisance parameters

| mind | eps | nn | nt | beta | tau |
|---|---|---|---|---|---|
| synA | 0.1 | 0.8 | 0.05 | 0.34 | 0.9 |
| synB | 0.15 | 0.6 | 0.2 | 0.65 | 0.7 |
| synC | 0.05 | 0.6 | 0.2 | 0.34 | 0.9 |
| synD | 0.6 | 0.4 | 0.2 | 0.5 | 0.7 |

## Minds: slot bias read directly from the Latin rotations (no model)

Over triads whose three rotations were all answered with an order: share of answers naming the glyph shown in the middle (1/3 = no slot preference), and share of triads given the same middle in all three rotations.

| mind | triads | middle = shown middle | same middle 3/3 |
|---|---|---|---|
| synA | 38 | 0.32 | 0.87 |
| synB | 24 | 0.39 | 0.67 |
| synC | 14 | 0.33 | 0.79 |
| synD | 22 | 0.53 | 0.05 |

## Parse status this round

- synA|ok: 210
- synB|ok: 210
- synC|ok: 210
- synD|ok: 210
