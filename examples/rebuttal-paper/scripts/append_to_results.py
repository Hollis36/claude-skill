"""Append experimental results to the canonical CSV.

Reads per-run JSON files and appends rows to data/results.csv with the
canonical schema: seed, dataset, method, metric_name, metric_value, std,
n_samples, notes.

Expected JSON shape (per run, one file per (method, dataset, seed)):

    {
        "method": "Baseline Y",
        "dataset": "D1",
        "seed": 1,
        "metrics": {"acc": 82.1, "f1": 80.5},
        "n_samples": 50000,
        "notes": "default hyperparams"
    }

Usage:
    python scripts/append_to_results.py \
        --run-id 0042 \
        --glob "data/runs/0042/*.json" \
        --csv data/results.csv

Append-only — never modifies existing rows.
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import sys
from pathlib import Path

SCHEMA = ["run_id", "seed", "dataset", "method", "metric_name",
          "metric_value", "std", "n_samples", "notes"]


def ensure_header(csv_path: Path) -> None:
    if csv_path.exists() and csv_path.stat().st_size > 0:
        with csv_path.open("r", newline="") as f:
            first = f.readline().strip().split(",")
        if first != SCHEMA:
            sys.exit(f"CSV schema mismatch at {csv_path}\n"
                     f"  expected: {SCHEMA}\n  found:    {first}")
        return
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="") as f:
        csv.writer(f).writerow(SCHEMA)


def append(csv_path: Path, run_id: str, json_files: list[Path]) -> int:
    n_rows = 0
    with csv_path.open("a", newline="") as f:
        writer = csv.writer(f)
        for jf in json_files:
            with jf.open() as fp:
                d = json.load(fp)
            for metric_name, metric_value in d["metrics"].items():
                writer.writerow([
                    run_id,
                    d["seed"],
                    d["dataset"],
                    d["method"],
                    metric_name,
                    metric_value,
                    d.get("std", ""),
                    d.get("n_samples", ""),
                    d.get("notes", ""),
                ])
                n_rows += 1
    return n_rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--glob", required=True, help="glob for per-run JSON files")
    ap.add_argument("--csv", default="data/results.csv")
    args = ap.parse_args()

    csv_path = Path(args.csv)
    ensure_header(csv_path)

    files = [Path(p) for p in sorted(glob.glob(args.glob))]
    if not files:
        sys.exit(f"No files matched: {args.glob}")

    n = append(csv_path, args.run_id, files)
    start_line = sum(1 for _ in csv_path.open()) - n + 1
    print(f"Appended {n} rows from {len(files)} files → "
          f"{csv_path} (lines {start_line}..{start_line + n - 1})")


if __name__ == "__main__":
    main()
