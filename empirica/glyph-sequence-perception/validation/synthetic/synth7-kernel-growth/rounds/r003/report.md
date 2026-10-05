# Round r003 — fit report

Observations (triple-level, cumulative): 25296. Minds: synA, synB, synC, synD.

## Candidate sequences (best chain), by family-mean perception

s3 = perception in triads, s4 = in sets of 4+, per family (mean over its minds). support = share of the cold-started chains (from seeds, not from the last fit) and their posterior samples holding a matching candidate.

| # | sequence | n | support | famX s3/s4 | famY s3/s4 | famZ s3/s4 |
|---|---|---|---|---|---|---|
| 2 | `▁ ▂ ▃ ▄ ▅ ▆ ▇` | 7 | 1.00 | 0.94/0.97 | 0.50/0.80 | 0.80/0.97 |
| 1 | `⑧ ⑦ ⑥ ⑤ ④ ③ ② ①` | 8 | 1.00 | 0.94/0.94 | 0.50/0.97 | 0.80/0.80 |
| 0 | `○ ◔ ◑ ◕ ●` | 5 | 1.00 | 0.03/0.89 | 0.10/0.80 | 0.10/0.97 |
| 6 | `⑵ ⑤ ⑷ ⑸` | 4 | 1.00 | 0.62/0.45 | 0.35/0.90 | 0.00/0.90 |
| 4 | `⚀ ⚁ ⚂=⚃ ⚄ ⚅` | 6 | 1.00 | 0.89/0.50 | 0.65/0.50 | 0.80/0.50 |
| 3 | `⑹ ⑸ ⑷ ⑤ ⑶` | 5 | 1.00 | 0.94/0.65 | 0.50/0.50 | 0.80/0.65 |
| 5 | `⚅ ⚄ ⚂ ⚁ ⚀` | 5 | 1.00 | 0.00/0.94 | 0.00/0.65 | 0.00/0.65 |

## Minds: nuisance parameters

| mind | eps | nn | nt | beta | tau |
|---|---|---|---|---|---|
| synA | 0.15 | 0.6 | 0.2 | 0.65 | 0.7 |
| synB | 0.25 | 0.6 | 0.2 | 0.65 | 0.7 |
| synC | 0.1 | 0.6 | 0.2 | 0.65 | 0.9 |
| synD | 0.6 | 0.4 | 0.2 | 0.5 | 0.5 |

## Minds: slot bias read directly from the Latin rotations (no model)

Over triads whose three rotations were all answered with an order: share of answers naming the glyph shown in the middle (1/3 = no slot preference), and share of triads given the same middle in all three rotations.

| mind | triads | middle = shown middle | same middle 3/3 |
|---|---|---|---|
| synA | 28 | 0.33 | 0.93 |
| synB | 16 | 0.42 | 0.75 |
| synC | 6 | 0.28 | 0.83 |
| synD | 13 | 0.59 | 0.38 |

## Parse status this round

- synA|ok: 303
- synB|ok: 303
- synC|ok: 303
- synD|ok: 303
