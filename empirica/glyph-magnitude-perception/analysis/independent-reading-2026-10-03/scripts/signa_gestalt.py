"""Signa gestalt: every arrangement verbatim, tau vs author, EXTRA."""
from common import *
for run in sorted(p.name for p in RUNS.iterdir() if p.name.startswith("signa-gestalt")):
    rows = stim_rows("consumer-signa-gestalt.jsonl")
    print("===", run)
    for r in ledger(run):
        st = rows[r["pids"][0]]
        raw = r["result"].get("raw") or ""
        if not raw or r["result"].get("error"):
            print(f"  sh{st['shuffle']}: ERROR {str(r['result'].get('error'))[:120]!r}"); continue
        g = I.parse_gestalt(raw, st["glyphs"])
        if g["kind"] != "order":
            print(f"  sh{st['shuffle']}: {g['kind']}  raw={raw[-200:]!r}"); continue
        t, n = kendall_tau(g["order"], SIGNA)
        print(f"  sh{st['shuffle']}: {''.join(g['order'])}  EXTRA={''.join(g['extra'])}  n={n} tau={t:+.2f}  dup={len(g['order'])-len(set(g['order']))}  rawtail={raw.strip()[-80:]!r}")
