"""Judge adapters: one stateless call -> raw response + provenance.

Every adapter returns a dict:
  raw (str|None), model_reported (str|None), usage (dict), cost_usd (float|None),
  latency_s, error (str|None), adapter_meta (dict)
Judges are configured to see ONLY the study prompt: tools off, MCP off, user/project
instruction files and agent profiles stripped (grok/codex run under an isolated
HOME / CODEX_HOME holding only a symlink to the real auth file). What could not be
stripped is recorded in the run spec's `context_residue` note, never silently.
"""
import json, os, pathlib, subprocess, time, urllib.request

SCRATCH = pathlib.Path(os.environ.get("GMP_JUDGE_SCRATCH",
                       pathlib.Path.home() / ".cache" / "gmp-judges"))

def _clean_env(extra=None):
    env = {k: v for k, v in os.environ.items()
           if not (k.startswith("CLAUDE") or k.startswith("AI_AGENT") or k == "CLAUDECODE")}
    env.update(extra or {})
    return env

def _empty_dir(name):
    d = SCRATCH / name
    d.mkdir(parents=True, exist_ok=True)
    return d

# ---------------------------------------------------------------- Claude (claude -p)
def claude_call(model, system, prompt, effort="low", timeout=300):
    cmd = ["claude", "-p", "--model", model, "--tools", "", "--strict-mcp-config",
           "--mcp-config", '{"mcpServers":{}}', "--no-session-persistence",
           "--setting-sources", "", "--system-prompt", system, "--output-format", "json"]
    if effort:
        cmd += ["--effort", effort]
    cmd.append(prompt)
    t0 = time.time()
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout,
                           cwd=_empty_dir("claude-cwd"), env=_clean_env(), stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        return dict(raw=None, model_reported=None, usage={}, cost_usd=None,
                    latency_s=time.time() - t0, error="timeout", adapter_meta={})
    dt = time.time() - t0
    try:
        events = json.loads(p.stdout)
        res = next(e for e in events if e.get("type") == "result")
        init = next((e for e in events if e.get("type") == "system"), {})
        u = res.get("usage") or {}
        return dict(raw=res.get("result"), model_reported=",".join(res.get("modelUsage", {}).keys()) or init.get("model"),
                    usage={"input_tokens": u.get("input_tokens"), "output_tokens": u.get("output_tokens"),
                           "thinking_tokens": (u.get("output_tokens_details") or {}).get("thinking_tokens"),
                           "cache_read": u.get("cache_read_input_tokens")},
                    cost_usd=res.get("total_cost_usd"), latency_s=dt,
                    error=("is_error" if res.get("is_error") else None),
                    adapter_meta={"tools": init.get("tools"), "session_id": res.get("session_id")})
    except Exception as ex:
        return dict(raw=None, model_reported=None, usage={}, cost_usd=None, latency_s=dt,
                    error=f"parse-fail: {ex}; stderr={p.stderr[-400:]}; stdout={p.stdout[-400:]}", adapter_meta={})

# ---------------------------------------------------------------- ollama (local HTTP)
_OLLAMA_DIGEST = {}
def ollama_digest(model):
    if model not in _OLLAMA_DIGEST:
        with urllib.request.urlopen("http://localhost:11434/api/tags", timeout=30) as r:
            tags = json.load(r)["models"]
        _OLLAMA_DIGEST.update({m["name"]: m["digest"] for m in tags})
    return _OLLAMA_DIGEST.get(model)

def ollama_call(model, system, prompt, temperature=0.0, num_predict=48, think=None, seed=0, timeout=900):
    body = {"model": model, "stream": False,
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": prompt}],
            "options": {"temperature": temperature, "num_predict": num_predict, "seed": seed}}
    if think is not None:
        body["think"] = think
    req = urllib.request.Request("http://localhost:11434/api/chat", json.dumps(body).encode(),
                                 {"Content-Type": "application/json"})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            out = json.load(r)
    except Exception as ex:
        return dict(raw=None, model_reported=None, usage={}, cost_usd=0.0, latency_s=time.time() - t0,
                    error=f"http: {ex}", adapter_meta={})
    msg = out.get("message") or {}
    return dict(raw=msg.get("content"), model_reported=f"{out.get('model')}@{(ollama_digest(model) or '')[:12]}",
                usage={"input_tokens": out.get("prompt_eval_count"), "output_tokens": out.get("eval_count"),
                       "thinking_chars": len(msg.get("thinking") or "")},
                cost_usd=0.0, latency_s=time.time() - t0, error=None,
                adapter_meta={"thinking": (msg.get("thinking") or "")[:2000], "options": body["options"], "think": think})

# ---------------------------------------------------------------- grok (isolated HOME)
GROK_TOOLS = ("run_terminal_command,read_file,search_replace,list_dir,grep,kill_command_or_subagent,"
              "get_command_or_subagent_output,spawn_subagent,scheduler_create,scheduler_delete,scheduler_list,"
              "monitor,search_tool,use_tool,web_search,web_fetch,write_file,edit_file")
def grok_call(model, system, prompt, effort="low", timeout=600):
    """streaming-json: the plain/json output formats truncate long answers (observed 2026-10-03:
    'text' cut at 204 chars of a 1271-char sheet answer); the stream's text deltas are complete."""
    home = _empty_dir("grokhome")
    (home / ".grok").mkdir(exist_ok=True)
    auth = home / ".grok" / "auth.json"
    if not auth.exists():
        auth.symlink_to(pathlib.Path.home() / ".grok" / "auth.json")
    cfg = home / ".grok" / "config.toml"
    if not cfg.exists():
        cfg.write_text('[cli]\nauto_update = false\n\n[features]\ntelemetry = false\n')
    work = _empty_dir("grokhome/work")
    # --tools '' does NOT remove tools (observed); restricting to the inert todo_write does (the judge then
    # sees only todo_write + the search_tool/use_tool meta-pair; no file/shell/web capability).
    cmd = ["grok", "-p", prompt, "-m", model, "--tools", "todo_write", "--disallowed-tools", GROK_TOOLS,
           "--system-prompt-override", system, "--output-format", "streaming-json",
           "--no-subagents", "--disable-web-search", "--max-turns", "1"]
    if effort:
        cmd += ["--reasoning-effort", effort]
    t0 = time.time()
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=work,
                           env=_clean_env({"HOME": str(home)}), stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        return dict(raw=None, model_reported=None, usage={}, cost_usd=None, latency_s=time.time() - t0,
                    error="timeout", adapter_meta={})
    dt = time.time() - t0
    texts, end, types = [], None, {}
    for line in p.stdout.splitlines():
        try:
            e = json.loads(line)
        except Exception:
            continue
        t = e.get("type"); types[t] = types.get(t, 0) + 1
        if t == "text":
            texts.append(e.get("data") or "")
        elif t == "end":
            end = e
    if end is None:
        return dict(raw=None, model_reported=None, usage={}, cost_usd=None, latency_s=dt,
                    error=f"no-end-event; stderr={p.stderr[-300:]}; stdout={p.stdout[-300:]}", adapter_meta={"event_types": types})
    u = end.get("usage") or {}
    raw = "".join(texts)
    return dict(raw=raw or None, model_reported=",".join((end.get("modelUsage") or {}).keys()),
                usage={"input_tokens": u.get("input_tokens"), "output_tokens": u.get("output_tokens"),
                       "thinking_tokens": u.get("reasoning_tokens")},
                cost_usd=end.get("total_cost_usd"), latency_s=dt,
                error=None if raw else f"empty-text (stop={end.get('stopReason')}, events={types})",
                adapter_meta={"stop": end.get("stopReason"), "num_turns": end.get("num_turns"),
                              "event_types": types, "session": end.get("sessionId")})

# ---------------------------------------------------------------- codex (isolated CODEX_HOME)
def codex_call(model, system, prompt, effort="low", timeout=900):
    home = _empty_dir("codexhome/home")
    auth = home / "auth.json"
    if not auth.exists():
        auth.symlink_to(pathlib.Path.home() / ".codex" / "auth.json")
    work = _empty_dir("codexhome/work")
    full = f"{system}\n\n{prompt}"
    cmd = ["codex", "exec", "--skip-git-repo-check", "--ephemeral", "-s", "read-only", "--json",
           "-m", model, "-c", f'model_reasoning_effort="{effort}"', full]
    t0 = time.time()
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=work,
                           env=_clean_env({"CODEX_HOME": str(home)}), stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        return dict(raw=None, model_reported=None, usage={}, cost_usd=None, latency_s=time.time() - t0,
                    error="timeout", adapter_meta={})
    dt = time.time() - t0
    texts, usage, err, item_types = [], {}, None, {}
    for line in p.stdout.splitlines():
        try:
            e = json.loads(line)
        except Exception:
            continue
        if e.get("type") == "item.completed":
            it = (e.get("item") or {}).get("type")
            item_types[it] = item_types.get(it, 0) + 1
            if it == "agent_message":
                texts.append(e["item"].get("text", ""))
        elif e.get("type") == "turn.completed":
            usage = e.get("usage") or {}
        elif e.get("type") in ("error", "turn.failed"):
            err = json.dumps(e)[:400]
    return dict(raw="\n".join(texts) if texts else None, model_reported=f"{model}(requested; codex exec does not echo)",
                usage={"input_tokens": usage.get("input_tokens"), "output_tokens": usage.get("output_tokens"),
                       "thinking_tokens": usage.get("reasoning_output_tokens")},
                cost_usd=None, latency_s=dt, error=err if not texts else None,
                adapter_meta={"system_prompt_mode": "prepended-to-user-turn", "item_types": item_types,
                              "stderr_tail": p.stderr[-200:]})

# ---------------------------------------------------------------- gemini via agy
def agy_call(model, system, prompt, timeout=900):
    full = f"{system}\n\n{prompt}"
    cmd = ["agy", "-p", full, "--model", model, "--output-format", "json", "--disable-slash-commands"]
    t0 = time.time()
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout,
                           cwd=_empty_dir("agy-cwd"), env=_clean_env(), stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        return dict(raw=None, model_reported=None, usage={}, cost_usd=None, latency_s=time.time() - t0,
                    error="timeout", adapter_meta={})
    dt = time.time() - t0
    try:
        d = json.loads(p.stdout.strip().splitlines()[-1])
        u = d.get("usage") or {}
        return dict(raw=d.get("response"), model_reported=f"{model}(requested)",
                    usage={"input_tokens": u.get("input_tokens"), "output_tokens": u.get("output_tokens"),
                           "thinking_tokens": u.get("thinking_tokens")},
                    cost_usd=None, latency_s=dt, error=None if d.get("status") == "SUCCESS" else d.get("status"),
                    adapter_meta={"system_prompt_mode": "prepended-to-user-turn", "conversation": d.get("conversation_id"),
                                  "num_turns": d.get("num_turns")})
    except Exception as ex:
        return dict(raw=None, model_reported=None, usage={}, cost_usd=None, latency_s=dt,
                    error=f"parse-fail: {ex}; stderr={p.stderr[-300:]}; stdout={p.stdout[-300:]}", adapter_meta={})

# ---------------------------------------------------------------- registry
def make_judge(spec):
    """spec: {"adapter": ..., "model": ..., plus adapter kwargs} -> callable(system, prompt)"""
    a = spec["adapter"]; m = spec["model"]
    kw = {k: v for k, v in spec.items() if k not in ("adapter", "model", "mode", "sheet_size", "workers", "label")}
    fn = {"claude": claude_call, "ollama": ollama_call, "grok": grok_call,
          "codex": codex_call, "agy": agy_call}[a]
    return lambda system, prompt: fn(m, system, prompt, **kw)
