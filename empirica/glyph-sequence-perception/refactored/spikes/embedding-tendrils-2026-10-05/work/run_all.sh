#!/bin/zsh
# The spike's pipeline, in the order it was run (2026-10-05). Each step is resumable or cached.
# Slow steps: embed_hf / embed (minutes per model), llm_next (about 30-75 min each on an M4 Max), probe (frontier calls).
set -e
cd "${0:A:h}"
python3 extract.py r011 && python3 gt.py r011          # study answers -> derived/answers-r011.jsonl, gt-r011.json
python3 extract.py r012 && python3 gt.py r012          # (r012 only used for the glyph universe and seen-glyph list)
python3 gt_survey.py                                    # derived/gt-survey.json
python3 tok_census.py                                   # tokenizer [UNK] census
python3 embed.py all-minilm glyph name                  # ollama
python3 embed.py bge-m3 glyph name                      # ollama (slow: ~15 min per form)
python3 embed_hf.py Qwen/Qwen3-Embedding-0.6B glyph name both
python3 embed_hf.py Qwen/Qwen3-Embedding-4B glyph        # the 'name' form was started and stopped (machine load); not run
HF_HUB_OFFLINE=1 python3 llm_next.py node                 # complete: 1,822 instances, ~29 min
HF_HUB_OFFLINE=1 python3 llm_next.py ctx --only-agreed     # STOPPED at 302 instances (Joseph: machine running hot); partial
python3 probe.py sample && python3 probe.py run sonnet55 gemini38flash grok46 && python3 probe.py gt
PROBE_SET=carry python3 probe.py sample && PROBE_SET=carry python3 probe.py run sonnet55 gemini38flash grok46 && PROBE_SET=carry python3 probe.py gt
# (not run: HF_HUB_OFFLINE=1 python3 llm_next.py node --gt probe)
# evaluations (print tables; write derived/*.json)
R=(cp 'name>cp+num' emb:all-minilm__glyph emb:all-minilm__name emb:bge-m3__glyph emb:bge-m3__name
   emb:hf-Qwen3-Embedding-0.6B__glyph emb:hf-Qwen3-Embedding-0.6B__name emb:hf-Qwen3-Embedding-4B__glyph emb:hf-Qwen3-Embedding-4B__name
   llm:Qwen3-8B-node-r011 'mix:cp|name>cp+num' 'mix:cp|emb:all-minilm__name')
python3 eval_retrieval.py ${R:#*4B__name}
python3 eval_retrieval.py --only-in Qwen3-8B-ctx-r011 cp 'name>cp+num' emb:all-minilm__name emb:hf-Qwen3-Embedding-0.6B__glyph llm:Qwen3-8B-node-r011 llm:Qwen3-8B-ctx-r011 'mix:cp|llm:Qwen3-8B-ctx-r011' 'mix:cp|emb:all-minilm__name'
python3 eval_retrieval.py --gt survey --truth first1 ${${R:#llm:*}:#*4B__name}
python3 eval_retrieval.py --gt probe --truth first1 ${${R:#llm:*}:#*4B__name}
python3 eval_retrieval.py --gt probe --truth any2 ${${R:#llm:*}:#*4B__name}
python3 probe_strata.py
python3 eval_triads.py cp 'name>cp+num' emb:all-minilm__name emb:hf-Qwen3-Embedding-0.6B__glyph emb:hf-Qwen3-Embedding-0.6B__name emb:bge-m3__glyph
python3 eval_lines.py hf-Qwen3-Embedding-0.6B__glyph hf-Qwen3-Embedding-0.6B__name all-minilm__name bge-m3__name bge-m3__glyph
python3 eval_axis.py hf-Qwen3-Embedding-0.6B__glyph hf-Qwen3-Embedding-0.6B__name all-minilm__name bge-m3__name bge-m3__glyph
python3 probe_linear.py all-minilm__name && python3 probe_linear.py all-minilm__name --residual --steps 150
python3 classify_far.py r011 first2 && python3 classify_far.py survey first1
python3 family_cp.py probe r011 && python3 carry_eval.py && python3 series_ends.py && python3 carry_test.py
python3 breakdown.py retrieval-r011-first2.json 10 cp 'name>cp+num' emb:all-minilm__name emb:hf-Qwen3-Embedding-0.6B__glyph 'mix:cp|emb:all-minilm__name'
