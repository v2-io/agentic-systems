#!/usr/bin/env python3
"""Ingest the pilot-condition arm (Agent-tool Sonnet subagents reading pilot-worded sheet files) into
ledger form. Source = the subagent transcripts (JSONL) Claude Code wrote for each judge; the user turn
(prompt) and the final assistant text (raw response) are copied verbatim, plus model id and usage.

  ingest_pilotcond.py TRANSCRIPT.jsonl [...]
Writes data/runs-v1/format-{tie,perp}-pilotcond-sonnetagent/{spec.json,ledger.jsonl} (appends; one row per sheet).
"""
import datetime as dt, hashlib, json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import instruments as I
EXP = pathlib.Path(__file__).resolve().parents[2]
man = {m["sheet"]: m for m in json.load(open(EXP / "data/stimuli-v1/pilotcond/manifest.json"))}

def main():
    for t in sys.argv[1:]:
        ev = []
        for line in open(t):
            try: ev.append(json.loads(line))
            except Exception: pass
        prompt = next(e["message"]["content"] for e in ev if e.get("type") == "user" and isinstance(e["message"].get("content"), str))
        m = re.search(r"pilotcond/([a-z]+-o\d-s\d)\.json", prompt)
        if not m:
            print("skip (no sheet):", t); continue
        sid = m.group(1); fmt = man[sid]["fmt"]
        asst = [e for e in ev if e.get("type") == "assistant"]
        last = asst[-1]["message"]
        raw = "".join(c.get("text", "") for c in last["content"] if c.get("type") == "text")
        model = last.get("model"); usage = last.get("usage", {})
        run_id = f"format-{fmt}-pilotcond-sonnetagent"
        rdir = EXP / "data/runs-v1" / run_id; rdir.mkdir(parents=True, exist_ok=True)
        if not (rdir / "spec.json").exists():
            json.dump({"run_id": run_id, "protocol": I.PROTOCOL, "instrument": "format", "format": fmt, "mode": "pilotcond",
                       "sheet_size": 80, "reps": 1, "stimulus_file": "data/stimuli-v1/format-pairs.jsonl (pilot-replication stratum) via data/stimuli-v1/pilotcond/",
                       "judge_label": "sonnet-agent", "judge": {"adapter": "claude-code Agent tool, subagent_type general-purpose", "model": "sonnet (alias)"},
                       "adapter_version": "pilotcond-1",
                       "note": "Pilot-condition arm: pilot walk5b brief wording, sheet delivered as a JSON file the agent reads with its tools, "
                               "agent runs inside Claude Code's subagent harness (its system prompt and the user's global CLAUDE.md context load), "
                               "80 items per sheet, orders split across sheets. Built to test whether the pilot's ⟂ rates depend on judge context.",
                       "created": dt.datetime.now(dt.timezone.utc).isoformat()}, open(rdir / "spec.json", "w"), ensure_ascii=False, indent=1)
        row = {"sheet_incomplete": None, "ledger_version": 1, "run_id": run_id, "protocol": I.PROTOCOL, "instrument": "format",
               "format": fmt, "mode": "sheet", "rep": 0, "pids": [it["pid"] for it in man[sid]["items"]], "sheet": sid,
               "items": man[sid]["items"], "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(), "prompt": prompt,
               "system_sha256": None, "judge_label": "sonnet-agent", "ts": asst[-1].get("timestamp"),
               "result": {"raw": raw, "model_reported": model, "usage": {"input_tokens": usage.get("input_tokens"),
                          "output_tokens": usage.get("output_tokens")}, "cost_usd": None, "latency_s": None, "error": None,
                          "adapter_meta": {"transcript": pathlib.Path(t).name, "tool_uses": sum(1 for e in asst for c in e["message"]["content"] if c.get("type") == "tool_use")}}}
        with open(rdir / "ledger.jsonl", "a") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
        print(sid, fmt, model, len(raw))

if __name__ == "__main__":
    main()
