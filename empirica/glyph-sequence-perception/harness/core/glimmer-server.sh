#!/bin/bash
# Start the Muse Glimmer 30B judge (llama.cpp llama-server + DFlash drafter) on 127.0.0.1:8080, as run 2026-10-03.
# Weights: ~/models/muse-glimmer/gguf (Joseph's T7 copy). Stop: pkill -f "llama-server -m muse-glimmer".
# One local model at a time (resource contention, Joseph 2026-10-03).
LOG=${1:-/tmp/glimmer-server.log}
cd ~/models/muse-glimmer/gguf || exit 1
nohup ~/src-ext/llama.cpp/build/bin/llama-server -m muse-glimmer-30B-kquant-dynamic.gguf -md dflash-kquant.gguf \
  --spec-type draft-dflash -c 8192 --temp 0 --host 127.0.0.1 --port 8080 > "$LOG" 2>&1 &
for i in $(seq 1 60); do curl -s http://127.0.0.1:8080/health | grep -q ok && { echo "glimmer up"; exit 0; }; sleep 5; done
echo "glimmer did not come up; see $LOG"; exit 1
