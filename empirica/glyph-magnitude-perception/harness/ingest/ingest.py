#!/usr/bin/env python3
"""Rebuild the derived Postgres index from the append-only JSONL truth.

Usage:  ingest.py [dbname]        (default: empirica_glyph)
Idempotent by construction: drops and re-fills survey_records from data/.
Requires psql-18 on PATH (the machine's versioned Postgres 18 binary).
"""
import csv, io, json, pathlib, subprocess, sys

DB = sys.argv[1] if len(sys.argv) > 1 else "empirica_glyph"
HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[2]                     # .../glyph-magnitude-perception
EXTRACTED = ROOT / "data" / "surveys-v1" / "extracted"

def psql(*args, dbname=DB, input=None, check=True):
    cmd = ["psql-18", "-X", "-q", "-v", "ON_ERROR_STOP=1", "-d", dbname, *args]
    return subprocess.run(cmd, input=input, text=True, capture_output=True, check=check)

def main():
    # create db if missing (template1 connection), then schema
    r = subprocess.run(["psql-18", "-X", "-tAc",
                        f"SELECT 1 FROM pg_database WHERE datname='{DB}'", "-d", "postgres"],
                       text=True, capture_output=True)
    if "1" not in r.stdout:
        subprocess.run(["createdb-18" if pathlib.Path("/opt/homebrew/bin/createdb-18").exists()
                        else "createdb", DB], check=True)
        print(f"created database {DB}")
    psql("-f", str(HERE.parent / "schema.sql"))
    psql("-c", "TRUNCATE survey_records")

    buf = io.StringIO()
    w = csv.writer(buf)
    n = 0
    files = sorted(EXTRACTED.glob("*.jsonl")) + sorted((EXTRACTED / "corrections").glob("*.jsonl"))
    for f in files:
        layer = "capture-correction" if f.parent.name == "corrections" else "pass1"
        surveyor = f.stem
        for line in open(f):
            if not line.strip():
                continue
            d = json.loads(line)
            epi = d.get("epistemics") or {}
            w.writerow([
                d.get("id"), surveyor, layer, d.get("type") or d.get("record_type"),
                str(d.get("schema_version", "")), str(d.get("source_span", "")),
                d.get("glyphs", ""), d.get("lineage") or epi.get("lineage") or "",
                epi.get("felt_strength_verbatim") or d.get("felt_strength_verbatim") or "",
                epi.get("felt_immediacy_verbatim") or d.get("felt_immediacy_verbatim") or "",
                d.get("note_verbatim", ""), json.dumps(d, ensure_ascii=False),
            ])
            n += 1
    psql("-c", "\\copy survey_records (id, surveyor, layer, record_type, schema_version, "
               "source_span, glyphs, lineage, felt_strength_verbatim, felt_immediacy_verbatim, "
               "note_verbatim, doc) FROM STDIN WITH (FORMAT csv)",
         input=buf.getvalue())
    print(f"ingested {n} records from {len(files)} files into {DB}")

    for label, q in [
        ("by surveyor/layer", "SELECT surveyor, layer, count(*) FROM survey_records GROUP BY 1,2 ORDER BY 1,2"),
        ("by type", "SELECT record_type, count(*) FROM survey_records GROUP BY 1 ORDER BY 2 DESC"),
        ("revision links", "SELECT revision_kind, count(*) FROM revision_arcs GROUP BY 1 ORDER BY 2 DESC"),
        ("dangling arc targets", "SELECT count(*) FROM revision_arcs a LEFT JOIN survey_records t ON t.id = a.to_id WHERE t.id IS NULL"),
        ("top shared codepoints", "SELECT codepoint, count(DISTINCT surveyor) s, count(*) FROM glyph_occurrences GROUP BY 1 HAVING count(DISTINCT surveyor) >= 4 ORDER BY 2 DESC, 3 DESC LIMIT 12"),
    ]:
        out = psql("-c", q).stdout.strip()
        print(f"\n== {label}\n{out}")

if __name__ == "__main__":
    main()
