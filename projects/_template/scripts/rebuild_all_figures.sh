#!/usr/bin/env bash
# Rebuild every figure_*.py in ../figures/ in order.
# Run from project root: bash scripts/rebuild_all_figures.sh
set -euo pipefail

cd "$(dirname "$0")/../figures"

failed=()
for f in figure_*.py; do
  [ -f "$f" ] || continue
  echo "=== Building $f ==="
  if python "$f"; then
    echo "  ok: ${f%.py}.pdf"
  else
    echo "  FAILED: $f" >&2
    failed+=("$f")
  fi
done

if [ ${#failed[@]} -gt 0 ]; then
  echo
  echo "Failed: ${failed[*]}" >&2
  exit 1
fi
echo "All figures rebuilt."
