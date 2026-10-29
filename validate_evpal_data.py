import csv
from pathlib import Path

root = Path("data")
required = {"synthetic", "source_type", "generated_at", "generation_method", "source_reference"}
files = list(root.rglob("*.csv"))
counts = {}
problems = []
for path in files:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        counts[str(path).replace("\\", "/")] = len(rows)
        if not required.issubset(reader.fieldnames or []):
            problems.append(f"missing metadata columns: {path}")
        if not rows:
            problems.append(f"empty dataset: {path}")
        if any(row["synthetic"] != "true" or row["source_type"] != "synthetic" for row in rows):
            problems.append(f"invalid metadata values: {path}")

assert len(files) == 24, len(files)
assert counts["data/battery/soh_dataset.csv"] >= 10000
assert all(counts[f"data/ml/{name}.csv"] > 0 for name in ("train", "validation", "test", "ood_test"))
assert not problems, problems
print(f"PASS: {len(files)} CSVs, {sum(counts.values()):,} total rows, "
      f"{counts['data/battery/soh_dataset.csv']:,} SOH observations")
