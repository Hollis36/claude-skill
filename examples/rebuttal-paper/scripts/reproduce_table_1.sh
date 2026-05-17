#!/usr/bin/env bash
# Reproduce Main Table 1.
# Edit RUNS to add / remove configurations. Each line should produce one row
# in data/results.csv via your training/eval script.
set -euo pipefail

cd "$(dirname "$0")/.."

SEEDS=(1 2 3 4 5)
DATASETS=("D1" "D2")
METHODS=("baseline_A" "baseline_B" "ours")

for dataset in "${DATASETS[@]}"; do
  for method in "${METHODS[@]}"; do
    for seed in "${SEEDS[@]}"; do
      echo "=== $method on $dataset seed=$seed ==="
      # Replace with your real command:
      # python -m src.train --method "$method" --dataset "$dataset" --seed "$seed" \
      #     --append-results data/results.csv
    done
  done
done

echo "Table 1 reproduction complete. Inspect data/results.csv."
