"""Pilot walk2 sheets: were both orders of a pair on the same sheet?"""
import json, os, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
where = collections.defaultdict(list)
for i in range(12):
    for it in json.load(open(os.path.join(ROOT, f"data/judgments-v0/walk2-key-{i}.json")))["sheet"]:
        where[frozenset((it["a"], it["b"]))].append(i)
print("unordered pairs", len(where), "| presentations per pair", collections.Counter(len(v) for v in where.values()),
      "| distinct sheets per pair", collections.Counter(len(set(v)) for v in where.values()))
