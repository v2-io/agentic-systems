"""Judge adapters: one stateless call -> raw response + provenance.

Copied 2026-10-04 from the archived v1.0 runner (.archive/2026-10-04-magnitude-era/harness/runner/judges.py);
change since: ollama_call takes an optional `format` (ollama JSON mode), adapter version a2-format.

Every adapter returns a dict:
  raw (str|None), model_reported (str|None), usage (dict), cost_usd (float|None),
  latency_s, error (str|None), adapter_meta (dict)
Judges are configured to see ONLY the study prompt: tools off, MCP off, user/project
instruction files and agent profiles stripped (grok/codex run under an isolated
HOME / CODEX_HOME holding only a symlink to the real auth file). What could not be
stripped is recorded in the run spec's `context_residue` note, never silently.
"""
import hashlib, json, os, pathlib, subprocess, time, urllib.request

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
UTF_MCP = pathlib.Path.home() / "src" / "arch" / "firmatum" / "utils" / "utf-mcp" / "target" / "release" / "utf-mcp"
UTF_MCP_LOG = pathlib.Path(__file__).resolve().parents[1] / "data" / "utf-mcp" / "calls.jsonl"
UTF_MCP_TOOLS = ["mcp__unicode__identify", "mcp__unicode__range", "mcp__unicode__search", "mcp__unicode__blocks"]

def utf_mcp_calls(tag):
    """the utf-mcp call-log records of one judge call (by its tag): what the mind looked up, verbatim"""
    out = []
    try:
        for l in open(UTF_MCP_LOG):
            if tag in l:
                r = json.loads(l)
                if r.get("tag") == tag and r.get("kind", r.get("event")) not in ("start", "exit"):
                    out.append(r)
    except FileNotFoundError:
        pass
    return out

def claude_call(model, system, prompt, effort="low", timeout=300, max_thinking_tokens=None, unicode_tools=False):
    """max_thinking_tokens: the thinking budget, set explicitly (MAX_THINKING_TOKENS). Unset, the judge inherits whatever
    the launching shell exports -- Joseph's exports 31000, found 2026-10-05. 0 turns thinking off for claude-haiku-4-5
    (0 thinking tokens); claude-sonnet-5-5 still thinks ~600 tokens a sheet with it (spikes/thinking-felt-2026-10-05)."""
    tag = None
    mcp = {"mcpServers": {}}
    if unicode_tools:    # the reasoned pass: utf-mcp's four read-only lookup tools and nothing else (utf-mcp README)
        tag = "gsp-" + hashlib.sha256(f"{time.time_ns()}{prompt}".encode()).hexdigest()[:16]
        UTF_MCP_LOG.parent.mkdir(parents=True, exist_ok=True)
        mcp = {"mcpServers": {"unicode": {"type": "stdio", "command": str(UTF_MCP),
                                          "args": ["--log", str(UTF_MCP_LOG), "--tag", tag]}}}
    cmd = ["claude", "-p", "--model", model, "--tools", "", "--strict-mcp-config",
           "--mcp-config", json.dumps(mcp), "--no-session-persistence",
           "--setting-sources", "", "--system-prompt", system, "--output-format", "json"]
    if unicode_tools:
        cmd += ["--allowedTools", ",".join(UTF_MCP_TOOLS)]
    if effort:
        cmd += ["--effort", effort]
    cmd.append(prompt)
    t0 = time.time()
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout,
                           cwd=_empty_dir("claude-cwd"), stdin=subprocess.DEVNULL,
                           env=_clean_env(dict({} if max_thinking_tokens is None else {"MAX_THINKING_TOKENS": str(max_thinking_tokens)},
                                               **({"CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1"} if unicode_tools else {}))))
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
                    adapter_meta=dict({"tools": init.get("tools"), "session_id": res.get("session_id")},
                                      **({"utf_mcp_tag": tag, "utf_mcp_calls": utf_mcp_calls(tag)} if tag else {})))
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

def ollama_call(model, system, prompt, temperature=0.0, num_predict=48, think=None, seed=0, timeout=900, format=None):
    body = {"model": model, "stream": False,
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": prompt}],
            "options": {"temperature": temperature, "num_predict": num_predict, "seed": seed}}
    if think is not None:
        body["think"] = think
    if format is not None:
        body["format"] = format
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
GROK_TOOLS = ("search_tool,use_tool,todo_write,run_terminal_command,read_file,search_replace,list_dir,grep,kill_command_or_subagent,"
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
    # --tools '' does NOT remove tools (observed 2026-10-03), and even --tools todo_write leaves the
    # search_tool/use_tool meta-pair, which grok-4.6 used to try to look glyphs up by name mid-sheet
    # (garbling the answer). Allow-listing todo_write and then disallowing it plus the meta-pair leaves
    # the judge with an empty tool list (verified: available_commands tools == []).
    cmd = ["grok", "-p", prompt, "-m", model, "--tools", "todo_write", "--disallowed-tools", GROK_TOOLS, "--no-plan",
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
AGY_BRAIN = pathlib.Path.home() / ".gemini" / "antigravity-cli" / "brain"

def agy_steps(conversation):
    """the model's steps from agy's own transcript (thinking, tool calls), copied into the ledger: agy keeps only its
    ~500 most recent conversations (observed 2026-10-05), so the transcript is otherwise lost. The user turn is the
    ledger's own prompt and is not repeated."""
    if not conversation:
        return []
    p = AGY_BRAIN / conversation / ".system_generated" / "logs" / "transcript_full.jsonl"
    out = []
    try:
        for l in open(p):
            s = json.loads(l)
            if s.get("type") == "USER_INPUT":
                continue
            out.append({k: s[k] for k in ("step_index", "type", "status", "thinking", "content", "tool_calls",
                                           "output_tokens") if k in s})
    except Exception as ex:
        out.append({"type": "transcript-unreadable", "error": str(ex)[:200]})
    return out

AGY_TOOL_NOTICE = ("Please don't use any tools: a tool call halts this session before you can answer.")
# Joseph, 2026-10-06: "you may want to tell it that a tool call will halt the session". True of print mode, which
# soft-denies tool confirmations and ends the turn with no text (outcome tool-attempt). Said to Gemini only, the one
# family that is given tools; recorded in adapter_meta.notice and adapter version a4-tool-halt, so answers before and
# after it can be told apart. A tool attempt is still recorded, and still re-asked as no-lookup.

def agy_call(model, system, prompt, timeout=900):
    full = f"{system}\n{AGY_TOOL_NOTICE}\n\n{prompt}"
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
        steps = agy_steps(d.get("conversation_id"))
        tools = [t for s in steps for t in s.get("tool_calls", [])]
        raw = d.get("response")
        err = None if d.get("status") == "SUCCESS" else d.get("status")
        if err:                            # keep agy's own detail, so a rate limit can be told from other failures (a3)
            detail = {k: v for k, v in d.items() if k not in ("response", "usage")}
            err = f"{err}: {json.dumps(detail, ensure_ascii=False)[:400]}; stderr={p.stderr[-300:]}"
        if tools and not (raw or "").strip() and not err:
            err = "tool-attempt"          # print mode soft-denies tool confirmations; the turn then ends with no text
        return dict(raw=raw, model_reported=f"{model}(requested)",
                    usage={"input_tokens": u.get("input_tokens"), "output_tokens": u.get("output_tokens"),
                           "thinking_tokens": u.get("thinking_tokens")},
                    cost_usd=None, latency_s=dt, error=err,
                    adapter_meta={"system_prompt_mode": "prepended-to-user-turn", "notice": AGY_TOOL_NOTICE,
                                  "conversation": d.get("conversation_id"),
                                  "num_turns": d.get("num_turns"), "steps": steps, "tool_calls": tools})
    except Exception as ex:
        return dict(raw=None, model_reported=None, usage={}, cost_usd=None, latency_s=dt,
                    error=f"parse-fail: {ex}; stderr={p.stderr[-300:]}; stdout={p.stdout[-300:]}", adapter_meta={})

# ---------------------------------------------------------------- registry

# ---------------------------------------------------------------- llama.cpp server (OpenAI-compatible)
def llamacpp_call(model, system, prompt, url="http://127.0.0.1:8080/v1/chat/completions", system_suffix="",
                  temperature=0.0, max_tokens=512, timeout=900):
    body = {"model": model, "messages": [{"role": "system", "content": system + system_suffix},
                                          {"role": "user", "content": prompt}],
            "temperature": temperature, "max_tokens": max_tokens, "seed": 0}
    req = urllib.request.Request(url, json.dumps(body).encode(), {"Content-Type": "application/json"})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            out = json.load(r)
    except Exception as ex:
        return dict(raw=None, model_reported=None, usage={}, cost_usd=0.0, latency_s=time.time() - t0,
                    error=f"http: {ex}", adapter_meta={})
    ch = (out.get("choices") or [{}])[0]; msg = ch.get("message") or {}
    u = out.get("usage") or {}
    return dict(raw=msg.get("content") or None, model_reported=out.get("model"),
                usage={"input_tokens": u.get("prompt_tokens"), "output_tokens": u.get("completion_tokens"),
                       "thinking_chars": len(msg.get("reasoning_content") or "")},
                cost_usd=0.0, latency_s=time.time() - t0, error=None if msg.get("content") else f"empty (finish={ch.get('finish_reason')})",
                adapter_meta={"reasoning": (msg.get("reasoning_content") or "")[:2000], "finish": ch.get("finish_reason"),
                              "system_suffix": system_suffix})

ADAPTER_VERSION = {"claude": "a2-tools-optional", "ollama": "a2-format", "grok": "a2-no-tools", "codex": "a1", "agy": "a4-tool-halt", "llamacpp": "a1"}

def make_judge(spec):
    """spec: {"adapter": ..., "model": ..., plus adapter kwargs} -> callable(system, prompt)"""
    a = spec["adapter"]; m = spec["model"]
    kw = {k: v for k, v in spec.items() if k not in ("adapter", "model", "mode", "sheet_size", "workers", "label", "note", "INVALID", "family")}
    fn = {"claude": claude_call, "ollama": ollama_call, "grok": grok_call,
          "codex": codex_call, "agy": agy_call, "llamacpp": llamacpp_call}[a]
    return lambda system, prompt: fn(m, system, prompt, **kw)
