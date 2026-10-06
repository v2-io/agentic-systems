# Round r003 — fit report

Observations (triple-level, cumulative): 9252. Minds: synA, synB, synC, synD.

## Candidate sequences (best chain), by family-mean perception

s3 = perception in triads, s4 = in sets of 4+, per family (mean over its minds). support = share of chains and posterior samples holding a matching candidate.

| # | sequence | n | support | famX s3/s4 | famY s3/s4 | famZ s3/s4 |
|---|---|---|---|---|---|---|
| 4 | `① ② ③ ④ ⑤ ⑥ ⑦ ⑧` | 8 | 0.33 | 0.85/0.94 | 0.65/0.97 | 0.65/0.80 |
| 6 | `⑵ ⑶ ⑤ ⑷` | 4 | 1.00 | 0.94/0.73 | 0.50/0.80 | 0.97/0.97 |
| 5 | `▇ ▆ ▅ ▄ ▃ ▂ ▁` | 7 | 1.00 | 0.85/0.80 | 0.65/0.90 | 0.65/0.80 |
| 3 | `⑹ ⑸ ⑷ ⑤` | 4 | 1.00 | 0.89/0.65 | 0.50/0.65 | 0.80/0.97 |
| 1 | `⚅ ⚄ ⚂ ⚁ ⚀` | 5 | 0.33 | 0.00/0.97 | 0.00/0.80 | 0.00/0.65 |
| 2 | `○ ◔ ◑ ◕ ●` | 5 | 1.00 | 0.10/0.73 | 0.10/0.97 | 0.00/0.65 |
| 0 | `⚀ ⚁ ⚂=⚃ ⚄ ⚅` | 6 | 0.33 | 0.89/0.35 | 0.65/0.10 | 0.65/0.20 |

## Minds: nuisance parameters

| mind | eps | nn | nt | beta | tau |
|---|---|---|---|---|---|
| synA | 0.1 | 0.6 | 0.1 | 0.5 | 0.7 |
| synB | 0.25 | 0.6 | 0.2 | 0.5 | 0.9 |
| synC | 0.1 | 0.8 | 0.1 | 0.5 | 0.7 |
| synD | 0.6 | 0.4 | 0.2 | 0.5 | 0.1 |

## Minds: slot bias read directly from the Latin rotations (no model)

Over triads whose three rotations were all answered with an order: share of answers naming the glyph shown in the middle (1/3 = no slot preference), and share of triads given the same middle in all three rotations.

| mind | triads | middle = shown middle | same middle 3/3 |
|---|---|---|---|
| synA | 34 | 0.32 | 0.88 |
| synB | 19 | 0.35 | 0.84 |
| synC | 16 | 0.38 | 0.75 |
| synD | 23 | 0.54 | 0.22 |

## Parse status this round

- synA|ok: 209
- synB|ok: 209
- synC|ok: 209
- synD|ok: 209
