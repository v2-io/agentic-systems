# RUNS: software-file-lifetimes

*KR E.3. Recorded runs, per the empirica RUNS contract. The run was made on 2026-10-30 by the E.3 agent (Claude Opus 5.5).*

**Environment.**

- Python 3.11.14, numpy 2.4.1, git 2.56.0, macOS 27.0.1 (arm64).
- Script `lifetimes.py`, run as committed at `d84252d3`.
- The design was pre-registered at `54a0bf5e`.

**How each run was made.** For each repository there is a full bare clone from GitHub, taken at its default branch on 2026-10-30. The steps were:

- `lifetimes.py dump <clone> <name>.log`, which writes the mainline history with renames followed;
- the same with `--no-renames`, written to `<name>.norename.log`;
- `lifetimes.py run <name> <name>.log <name>.norename.log --reps 1000 --json <name>.json`.

The bootstrap used 1,000 replicates for the primary variant and 200 for each sensitivity variant. Seeds are keyed: the first 8 hex digits of `sha256("E3:<name>:<clock>")`, read as an integer (calendar seed, then commit seed). Sensitivity variants key on `<name>:no-renames` and `<name>:no-imports`, and the count bounds key on `counts:<cut>`.

**Rerunning.** A rerun from a dump is exact. A rerun from a clone at the recorded HEAD should reproduce the dump byte for byte, given the same git version's rename detection. The digests below are the first 16 hex digits of each file's sha256.

**Post-hoc fit** (account §3; not pre-registered). It ran on the ten primary dumps with `lifetimes.py posthoc <name>.log`, the version committed at `59d5141e`, using 200 directory-cluster bootstrap replicates, with seeds keyed on `sha256("E3:<name>:posthoc")`. Its output was printed, not saved to a file. A rerun from the dumps is exact.

The decision rules were applied with `lifetimes.py summarize --variant {primary,no-renames,no-imports}` over the ten primary JSONs. The exploratory count analysis was run with `lifetimes.py explore <name>.log` (not pre-registered).

| Repository | HEAD | Mainline commits | Lives | Seeds (calendar, commit) | dump (renames) | dump (no renames) | result JSON |
|---|---|---|---|---|---|---|---|
| git | `50fe5cc63f9c` | 24443 | 5543 | 3018093466, 497717004 | `562ad259e0a6be64` | `8f8d8bfdeabd5b7a` | `95c2d524d8f6ddc8` |
| cpython | `4a9b98115fec` | 98440 | 26849 | 3401590468, 3060109417 | `d425b55f5e1e2122` | `96a987e54d2f9ae3` | `08359ab687067a40` |
| postgres | `6cda9dfc4f97` | 65798 | 11425 | 1645520605, 1248496204 | `7cfbd93b461bf0e2` | `8c83cfdb677dac38` | `700e379bee94f942` |
| django | `a05e16a7230f` | 34112 | 9501 | 4138482681, 2433139615 | `05831fc7b1ef25e6` | `8978d4c013ad68d8` | `a6133b0fec93d7f1` |
| rails | `b8e9388a1904` | 46760 | 8516 | 3995190312, 583534259 | `aca517312720086d` | `e378d9df3f150447` | `ade40e2c0f1012f1` |
| ruby | `3c6a1c7a86b5` | 103474 | 21551 | 1633122938, 1212081920 | `5dfc6036fe0b3dee` | `8c919889e72d6a0d` | `b5dc22169e5c4918` |
| perl5 | `1b72dea75a56` | 70932 | 12498 | 3376590224, 4129083495 | `d405246c5ff0ad84` | `14ebe5ebe5517395` | `8eff6176e1e52517` |
| redis | `6a5fee675834` | 10052 | 2569 | 789798036, 3332640306 | `55adeb8e30bc012a` | `61246497860a91ce` | `ca3d94a228c4a702` |
| node | `cfea9922e7d6` | 46013 | 113627 | 3484886637, 762989275 | `756fb52ee8d907dd` | `69d49bd282330cc6` | `ac811992936d5ac7` |
| vim | `5287a96500f9` | 24710 | 9762 | 3467757273, 4024832607 | `9a6e86ec32864301` | `c1e2cc1eb75129e7` | `8cfd9865d0a47547` |
| codex | `67f0994b532b` | 12940 | 14227 | 3320670912, 3865882196 | `e6435484d784433b` | `33b1db1527cac81a` | `6282b8cee57a8442` |
| gemini-cli | `6814e00d6b14` | 6567 | 3353 | 1775305030, 3920203631 | `ede2044cdad6dbc9` | `6dd5192df82e67ac` | `47a9d01fe0c773ae` |
| obsidian-linter | `6cee2ddb207e` | 736 | 782 | 277377597, 391485843 | `e0201e046ab298be` | `68612252310b768f` | `a0d5f5c2310d1656` |
| ink | `10101266d1ab` | 785 | 393 | 2306228558, 1823996262 | `784be483e84141ea` | `a330acecdbdb77c6` | `65a3b918e204f95e` |

**Mainline commits** counts first-parent commits, which is fewer than `rev-list --count`.

**Lives** excludes files added in a history's first mainline commit.

**Gaps.** The dumps and JSONs are not committed: they total about 1 GB and are regenerated from the HEADs. They were kept in the session scratchpad, which is not durable.
