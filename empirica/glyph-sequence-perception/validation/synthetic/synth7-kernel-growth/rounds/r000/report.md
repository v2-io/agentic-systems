# Round r000 — fit report

Observations (triple-level, cumulative): 7132. Minds: synA, synB, synC, synD.

## Candidate sequences (best chain), by family-mean perception

s3 = perception in triads, s4 = in sets of 4+, per family (mean over its minds). support = share of the cold-started chains (from seeds, not from the last fit) and their posterior samples holding a matching candidate.

| # | sequence | n | support | famX s3/s4 | famY s3/s4 | famZ s3/s4 |
|---|---|---|---|---|---|---|
| 0 | `⑤ ⑷ ⑸` | 3 | 1.00 | 0.89/0.97 | 0.50/0.97 | 0.65/0.97 |
| 2 | `▁ ▂ ▃ ▄ ▅ ▆ ▇` | 7 | 1.00 | 0.85/0.85 | 0.90/0.97 | 0.35/0.97 |
| 3 | `○ ◔ ◑ ◕ ●` | 5 | 1.00 | 0.05/0.89 | 0.00/0.97 | 0.80/0.65 |
| 1 | `① ② ③ ④ ⑤ ⑥ ⑦ ⑧` | 8 | 1.00 | 0.80/0.89 | 0.50/0.90 | 0.65/0.65 |
| 4 | `⚀ ⚁ ⚂ ⚄ ⚅` | 5 | 1.00 | 0.25/0.90 | 0.00/0.80 | 0.00/0.65 |
| 5 | `⚀ ⚁ ⚃=⚂ ⚄ ⚅` | 6 | 1.00 | 0.78/0.35 | 0.65/0.35 | 0.90/0.35 |

## Minds: nuisance parameters

| mind | eps | nn | nt | beta | tau |
|---|---|---|---|---|---|
| synA | 0.15 | 0.4 | 0.2 | 0.5 | 0.7 |
| synB | 0.1 | 0.4 | 0.3 | 0.8 | 0.5 |
| synC | 0.1 | 0.6 | 0.2 | 0.65 | 0.9 |
| synD | 0.6 | 0.4 | 0.3 | 0.5 | 0.1 |

## Minds: slot bias read directly from the Latin rotations (no model)

Over triads whose three rotations were all answered with an order: share of answers naming the glyph shown in the middle (1/3 = no slot preference), and share of triads given the same middle in all three rotations.

| mind | triads | middle = shown middle | same middle 3/3 |
|---|---|---|---|

## Parse status this round

- synA|ok: 310
- synB|ok: 310
- synC|ok: 310
- synD|ok: 310
