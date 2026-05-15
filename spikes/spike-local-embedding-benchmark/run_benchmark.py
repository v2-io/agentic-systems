#!/usr/bin/env python3
"""Benchmark candidate ollama embedding models on AAD-specific retrieval queries.

For each model:
  1. Embed each AAD segment (whole-segment level — single embedding per file).
     Two variants are tested:
       - 'body' — title + summary + formal-expression + first ~1500 chars.
       - 'frontmatter+title' — slug + title + summary only (terse).
     We use 'body' as the primary scoring variant; the terse variant is ablation.
  2. Embed each benchmark query.
  3. Compute cosine similarity, retrieve top-K, score against ground-truth.
  4. Report per-query rank of primary answer + MRR + Recall@5.

Models tested are listed in MODELS below. Add/remove freely.
Run from spike directory:
    python run_benchmark.py
Outputs:
    results.json  — full per-query rankings
    summary.md    — ranked summary table
"""
from __future__ import annotations

import json
import math
import re
import sys
import time
from pathlib import Path

import ollama  # uses local ollama daemon

SPIKE_DIR = Path(__file__).resolve().parent
REPO_ROOT = SPIKE_DIR.parent.parent
SRC_DIRS = [
    REPO_ROOT / "01-aat-core" / "src",
    REPO_ROOT / "03-logogenic-agents" / "src",
]

# (model_name, embedding_dim_hint, prefix_style)
# prefix_style: 'nomic' = use search_document/search_query; 'none' = raw text;
#               'bge'   = BGE-style "Represent this sentence for searching: "
MODELS = [
    ("nomic-embed-text:latest", 768, "nomic"),
    ("nomic-embed-text-v2-moe:latest", 768, "nomic"),
    ("mxbai-embed-large:latest", 1024, "none"),
    ("bge-m3:latest", 1024, "none"),
    ("snowflake-arctic-embed:latest", 1024, "none"),
    ("embeddinggemma:300m", 768, "none"),
    ("granite-embedding:30m", 384, "none"),
    ("qwen3-embedding:latest", 1024, "none"),
]

TOP_K = 10
QUERIES_PATH = SPIKE_DIR / "queries.json"


def load_queries():
    with open(QUERIES_PATH) as f:
        return json.load(f)["queries"]


def collect_segments():
    segs = {}
    for d in SRC_DIRS:
        if not d.exists():
            continue
        for path in sorted(d.glob("*.md")):
            slug = path.stem
            if slug.startswith("old-"):
                continue
            text = path.read_text(errors="replace")
            segs[slug] = {"path": str(path), "text": text}
    return segs


_FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)


def segment_body(text: str, max_chars: int = 2500) -> str:
    """Strip frontmatter, keep title + summary + formal-expression + early
    discussion. Keep terse so single-vector representation isn't dominated by
    late-segment math."""
    m = _FRONTMATTER_RE.match(text)
    if m:
        text = text[m.end():]
    return text[:max_chars].strip()


def segment_terse(text: str) -> str:
    """slug + title + one-sentence summary (first non-blank paragraph after title)."""
    body = segment_body(text, max_chars=8000)
    lines = body.splitlines()
    title = ""
    summary_lines = []
    state = "find_title"
    for line in lines:
        s = line.strip()
        if state == "find_title":
            if s.startswith("#"):
                title = s.lstrip("#").strip()
                state = "find_summary"
            continue
        if state == "find_summary":
            if not s:
                if summary_lines:
                    break
                continue
            if s.startswith("#") or s.startswith("##"):
                if summary_lines:
                    break
                continue
            if s.startswith("---"):
                continue
            summary_lines.append(s)
            if len(" ".join(summary_lines)) > 400:
                break
    return f"{title}\n\n{' '.join(summary_lines)}".strip()


def embed_with_model(model: str, texts, prefix_style: str, kind: str):
    """kind in {'doc', 'query'}. Handles per-model prefix conventions."""
    if prefix_style == "nomic":
        pfx = "search_document: " if kind == "doc" else "search_query: "
        prefixed = [pfx + t for t in texts]
    elif prefix_style == "bge":
        pfx = "" if kind == "doc" else "Represent this sentence for searching relevant passages: "
        prefixed = [pfx + t for t in texts]
    else:
        prefixed = list(texts)

    out = []
    # Embed one at a time for reliability across models
    for t in prefixed:
        try:
            r = ollama.embed(model=model, input=t)
            emb = r["embeddings"][0] if isinstance(r["embeddings"][0], list) else r["embeddings"]
            out.append(emb)
        except Exception as e:
            # Try truncating
            for limit in [len(t) * 3 // 4, len(t) // 2, len(t) // 4, 800]:
                try:
                    r = ollama.embed(model=model, input=t[:limit])
                    emb = r["embeddings"][0] if isinstance(r["embeddings"][0], list) else r["embeddings"]
                    out.append(emb)
                    break
                except Exception:
                    continue
            else:
                print(f"  [warn] embed failed for {model}: {e}", file=sys.stderr)
                out.append(None)
    return out


def cosine(a, b):
    if a is None or b is None:
        return -1.0
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    if na == 0 or nb == 0:
        return -1.0
    return dot / (na * nb)


def rank_for_slug(ranking, slug):
    """Return 1-indexed rank of slug in ranking, or None."""
    for i, (s, _) in enumerate(ranking, 1):
        if s == slug:
            return i
    return None


def benchmark_model(model: str, prefix_style: str, segments, queries, body_variant: str):
    print(f"\n=== {model} (variant={body_variant}) ===")
    slugs = list(segments.keys())
    if body_variant == "body":
        texts = [segment_body(segments[s]["text"]) for s in slugs]
    else:
        texts = [segment_terse(segments[s]["text"]) for s in slugs]

    t0 = time.time()
    print(f"  embedding {len(texts)} segments...")
    seg_embs = embed_with_model(model, texts, prefix_style, "doc")
    embed_time = time.time() - t0
    print(f"  done in {embed_time:.1f}s ({embed_time/len(texts)*1000:.0f}ms/seg)")

    # Embed queries
    qtexts = [q["query"] for q in queries]
    t0 = time.time()
    q_embs = embed_with_model(model, qtexts, prefix_style, "query")
    qtime = time.time() - t0
    print(f"  embedded {len(qtexts)} queries in {qtime:.1f}s")

    # Score
    per_query = []
    primary_ranks = []
    recall5_hits = 0
    recall10_hits = 0
    mrr_sum = 0.0

    for q, qe in zip(queries, q_embs):
        sims = [(slug, cosine(qe, e)) for slug, e in zip(slugs, seg_embs)]
        sims.sort(key=lambda x: x[1], reverse=True)
        top = sims[:TOP_K]

        # find best primary rank
        best_rank = None
        primary_hits = []
        for p in q["primary"]:
            r = rank_for_slug(sims, p)
            primary_hits.append({"slug": p, "rank": r})
            if r is not None and (best_rank is None or r < best_rank):
                best_rank = r

        also_hits = [{"slug": p, "rank": rank_for_slug(sims, p)} for p in q.get("also", [])]

        primary_ranks.append(best_rank if best_rank is not None else 9999)
        if best_rank is not None and best_rank <= 5:
            recall5_hits += 1
        if best_rank is not None and best_rank <= 10:
            recall10_hits += 1
        if best_rank is not None:
            mrr_sum += 1.0 / best_rank

        per_query.append({
            "id": q["id"],
            "query": q["query"],
            "best_primary_rank": best_rank,
            "primary_hits": primary_hits,
            "also_hits": also_hits,
            "top10": [{"slug": s, "sim": round(sim, 4)} for s, sim in top],
        })

    n = len(queries)
    return {
        "model": model,
        "variant": body_variant,
        "embed_time_seconds": round(embed_time, 2),
        "ms_per_segment": round(embed_time / max(1, len(texts)) * 1000, 1),
        "n_segments": len(texts),
        "n_queries": n,
        "mrr": round(mrr_sum / n, 4),
        "recall_at_5": round(recall5_hits / n, 4),
        "recall_at_10": round(recall10_hits / n, 4),
        "median_primary_rank": sorted(primary_ranks)[n // 2],
        "mean_primary_rank": round(sum(primary_ranks) / n, 2),
        "per_query": per_query,
    }


def main():
    queries = load_queries()
    segments = collect_segments()
    print(f"Loaded {len(segments)} segments, {len(queries)} queries.")

    results = []
    for model, _dim, pfx in MODELS:
        try:
            res = benchmark_model(model, pfx, segments, queries, body_variant="body")
            results.append(res)
            print(f"  MRR={res['mrr']:.3f}  R@5={res['recall_at_5']:.2f}  R@10={res['recall_at_10']:.2f}  median_rank={res['median_primary_rank']}")
        except Exception as e:
            print(f"  [error] {model}: {e}", file=sys.stderr)
            results.append({"model": model, "variant": "body", "error": str(e)})

    # Optional: ablation — top-2 models on terse variant
    body_results = [r for r in results if "error" not in r]
    body_results.sort(key=lambda r: r["mrr"], reverse=True)
    top2 = body_results[:2]
    for r in top2:
        model = r["model"]
        pfx = next(p for m, _, p in MODELS if m == model)
        try:
            res = benchmark_model(model, pfx, segments, queries, body_variant="terse")
            results.append(res)
            print(f"  [terse] {model} MRR={res['mrr']:.3f}  R@5={res['recall_at_5']:.2f}")
        except Exception as e:
            print(f"  [error terse] {model}: {e}", file=sys.stderr)

    out = SPIKE_DIR / "results.json"
    with open(out, "w") as f:
        json.dump({"results": results, "n_segments": len(segments), "n_queries": len(queries)}, f, indent=2)
    print(f"\nWrote {out}")

    # Summary table
    summary_lines = ["# Benchmark Summary\n"]
    summary_lines.append(f"_{len(segments)} segments × {len(queries)} queries; top-{TOP_K} retrieval._\n")
    summary_lines.append("| Model | Variant | MRR | R@5 | R@10 | Median rank | ms/seg |")
    summary_lines.append("|---|---|---|---|---|---|---|")
    okres = [r for r in results if "error" not in r]
    okres.sort(key=lambda r: (-r["mrr"], r["model"]))
    for r in okres:
        summary_lines.append(
            f"| `{r['model']}` | {r['variant']} | {r['mrr']:.3f} | {r['recall_at_5']:.2f} | {r['recall_at_10']:.2f} | {r['median_primary_rank']} | {r['ms_per_segment']:.0f} |"
        )
    errored = [r for r in results if "error" in r]
    if errored:
        summary_lines.append("\n## Errored models\n")
        for r in errored:
            summary_lines.append(f"- `{r['model']}`: {r['error']}")
    (SPIKE_DIR / "summary.md").write_text("\n".join(summary_lines) + "\n")
    print(f"Wrote {SPIKE_DIR / 'summary.md'}")


if __name__ == "__main__":
    main()
