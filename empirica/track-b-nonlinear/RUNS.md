# RUNS — track-b-nonlinear

*Recorded runs backing the MANIFEST claims. Reconstructed 2026-07-16 from the committed artifacts (`.npz` outputs, results write-ups, figure sets, script defaults) — honest gaps marked; this record predates the RUNS contract, so environments were never captured.*

| Date | Piece | Parameters | Seed | Output record |
|---|---|---|---|---|
| 2026-03-09 | sim1 | script defaults (10,000 steps × 200 trials, burn-in 2,000; 5 correction functions) | 42 (in-script) | `sim1_results.npz` + 5 figures |
| 2026-03-09 | sim2 | script defaults | 42 (in-script) | `sim2_results.npz` + 6 figures |
| 2026-03-09 | variants A/B | sweep per `variant_ab_results.md` (Variant-A coupling-dominance at $\mathcal T_B = 0.1$) | 42 (in-script) | `variant_ab_results.md` tables + 6 figures |
| 2026-03-09 | variants C/D | $\eta$ sweep 0.1→0.001; $q_{\text{base}}$ sweep 0.1→0.0001 at $\eta = 0.01$; 2D analytic grid | 42 (in-script) | `variant_cd_results.md` tables + `variant_cd_results.npz` + 3 figures |
| 2026-03-09 | variants E/F | per `variant_ef_results.md` ($\sigma_{\text{obs}}$ sweep; 3-D anisotropic gains) | 42 (in-script default) | `variant_ef_results.md` tables + 6 figures |
| 2026-05-15 | causal-IB | 500 episodes × 200 steps, $\rho = 0.5$, $R = 4.0$, $U_o = 100.0$; 4 $\lambda$-policies | not recorded in write-up — check script before rerun | `variant_causal_ib_results.md` |
| 2026-05-15 | Hafez bridge | per `variant_hafez_results.md` ($P$ vs tempo over 50× $\eta$; adversarial 10:1 range) | not recorded in write-up — check script before rerun | `variant_hafez_results.md` + 7 figures |

**Known record gaps (honest, per the RUNS contract):** environments never captured (numpy/python versions unknown for the March runs); the two May runs' write-ups do not state seeds; figure regeneration from the `.npz` files has not been re-verified since March. A vivarium rerun supersedes all of this with in-vivia citations.
