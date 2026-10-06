# Round r002 — fit report

Observations (triple-level, cumulative): 19408. Minds: synA, synB, synC, synD.

## Candidate sequences (best chain), by family-mean perception

s3 = perception in triads, s4 = in sets of 4+, per family (mean over its minds). support = share of the cold-started chains (from seeds, not from the last fit) and their posterior samples holding a matching candidate.

| # | sequence | n | support | famX s3/s4 | famY s3/s4 | famZ s3/s4 |
|---|---|---|---|---|---|---|
| 3 | `▁ ▂ ▃ ▄ ▅ ▆ ▇` | 7 | 1.00 | 0.85/0.90 | 0.65/0.90 | 0.65/0.97 |
| 1 | `⑧ ⑦ ⑥ ⑤ ④ ③ ② ①` | 8 | 1.00 | 0.85/0.89 | 0.50/0.97 | 0.80/0.65 |
| 0 | `○ ◔ ◑ ◕ ●` | 5 | 1.00 | 0.03/0.85 | 0.03/0.80 | 0.20/0.90 |
| 4 | `⚅ ⚄ ⚂ ⚁ ⚀` | 5 | 1.00 | 0.00/0.85 | 0.00/0.65 | 0.00/0.80 |
| 6 | `⑵ ⑤ ⑷ ⑸` | 4 | 1.00 | 0.50/0.33 | 0.35/0.90 | 0.00/0.90 |
| 5 | `⑹ ⑸ ⑷ ⑤ ⑶` | 5 | 1.00 | 0.85/0.28 | 0.50/0.35 | 0.80/0.50 |
| 2 | `⚀ ⚁ ⚂=⚃ ⚄ ⚅` | 6 | 1.00 | 0.85/0.50 | 0.65/0.50 | 0.65/0.50 |

## Minds: nuisance parameters

| mind | eps | nn | nt | beta | tau |
|---|---|---|---|---|---|
| synA | 0.1 | 0.4 | 0.2 | 0.65 | 0.7 |
| synB | 0.15 | 0.4 | 0.2 | 0.65 | 0.7 |
| synC | 0.15 | 0.8 | 0.1 | 0.8 | 0.9 |
| synD | 0.6 | 0.4 | 0.2 | 0.5 | 0.5 |

## Minds: slot bias read directly from the Latin rotations (no model)

Over triads whose three rotations were all answered with an order: share of answers naming the glyph shown in the middle (1/3 = no slot preference), and share of triads given the same middle in all three rotations.

| mind | triads | middle = shown middle | same middle 3/3 |
|---|---|---|---|
| synA | 18 | 0.35 | 0.94 |
| synB | 11 | 0.39 | 0.82 |
| synC | 6 | 0.28 | 0.83 |
| synD | 9 | 0.67 | 0.33 |

## Parse status this round

- synA|ok: 305
- synB|ok: 305
- synC|ok: 305
- synD|ok: 305
