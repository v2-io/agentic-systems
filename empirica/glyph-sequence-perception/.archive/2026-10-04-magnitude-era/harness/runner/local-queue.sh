#!/usr/bin/env bash
# Run local ollama judges one at a time (RAM), waiting for weights that are still downloading.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"; LOG="${1:?logdir}"
while read -r LABEL MODEL; do
  for i in $(seq 1 240); do
    if curl -s -X POST http://localhost:11434/api/chat -d "{\"model\":\"$MODEL\",\"stream\":false,\"messages\":[{\"role\":\"user\",\"content\":\"ok\"}],\"options\":{\"num_predict\":2}}" | grep -q '"done":true'; then break; fi
    sleep 30
  done
  echo "start $LABEL $(date)"
  "$HERE/campaign.sh" "$LABEL" single 2 1 > "$LOG/$LABEL-single.log" 2>&1
  echo "done $LABEL $(date)"
done <<'Q'
llama32-3b llama3.2:3b
qwen3-4b qwen3:4b
gemma3-4b gemma3:4b
phi4mini phi4-mini
mistral7b mistral:7b
gptoss20b gpt-oss:20b
Q
echo ALL-LOCAL-DONE
