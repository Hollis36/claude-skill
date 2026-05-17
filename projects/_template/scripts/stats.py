"""Statistical utilities for ML paper rebuttal / main-table generation.

CLI:
    python scripts/stats.py compare \
        --csv data/results.csv \
        --metric acc \
        --method-a "Ours" --method-b "Baseline B" \
        --dataset D1

Functions are also importable from notebooks.
"""
from __future__ import annotations

import argparse
import sys
from typing import Sequence

import numpy as np
import pandas as pd
from scipy.stats import bootstrap, wilcoxon


def bootstrap_ci(
    values: Sequence[float],
    confidence: float = 0.95,
    n_resamples: int = 10_000,
) -> tuple[float, float, float]:
    arr = np.asarray(list(values), dtype=float)
    if len(arr) < 2:
        return float(arr.mean()), float("nan"), float("nan")
    res = bootstrap(
        (arr,),
        np.mean,
        confidence_level=confidence,
        n_resamples=n_resamples,
        method="BCa",
    )
    return (
        float(arr.mean()),
        float(res.confidence_interval.low),
        float(res.confidence_interval.high),
    )


def paired_wilcoxon(
    a: Sequence[float], b: Sequence[float], alternative: str = "greater"
) -> tuple[float, float]:
    a_arr = np.asarray(list(a), dtype=float)
    b_arr = np.asarray(list(b), dtype=float)
    if len(a_arr) != len(b_arr):
        raise ValueError(f"len mismatch: {len(a_arr)} vs {len(b_arr)}")
    if len(a_arr) < 5:
        print(f"WARN: n={len(a_arr)} is small for Wilcoxon — interpret cautiously",
              file=sys.stderr)
    stat, p = wilcoxon(a_arr, b_arr, alternative=alternative)
    return float(stat), float(p)


def holm_correct(pvalues: Sequence[float], alpha: float = 0.05) -> list[bool]:
    pvals = list(pvalues)
    n = len(pvals)
    order = sorted(range(n), key=lambda i: pvals[i])
    significant = [False] * n
    for rank, idx in enumerate(order):
        threshold = alpha / (n - rank)
        if pvals[idx] <= threshold:
            significant[idx] = True
        else:
            break
    return significant


def compare_methods(
    csv_path: str,
    metric: str,
    method_a: str,
    method_b: str,
    dataset: str | None = None,
) -> dict:
    df = pd.read_csv(csv_path)
    df = df[df["metric_name"] == metric]
    if dataset:
        df = df[df["dataset"] == dataset]

    a = df[df["method"] == method_a].sort_values("seed")["metric_value"].to_numpy()
    b = df[df["method"] == method_b].sort_values("seed")["metric_value"].to_numpy()

    if len(a) == 0 or len(b) == 0:
        sys.exit(f"No rows for {method_a}={len(a)} or {method_b}={len(b)} "
                 f"with metric={metric} dataset={dataset}")
    if len(a) != len(b):
        print(f"WARN: unbalanced seeds (a={len(a)}, b={len(b)}); pairing first min(n)",
              file=sys.stderr)
        n = min(len(a), len(b))
        a, b = a[:n], b[:n]

    a_mean, a_lo, a_hi = bootstrap_ci(a)
    b_mean, b_lo, b_hi = bootstrap_ci(b)
    diff = a - b
    d_mean, d_lo, d_hi = bootstrap_ci(diff)
    stat, p = paired_wilcoxon(a, b, alternative="greater")

    return {
        "n_seeds": len(a),
        "method_a": {"name": method_a, "mean": a_mean, "std": float(a.std(ddof=1)),
                     "ci95": [a_lo, a_hi]},
        "method_b": {"name": method_b, "mean": b_mean, "std": float(b.std(ddof=1)),
                     "ci95": [b_lo, b_hi]},
        "diff": {"mean": d_mean, "ci95": [d_lo, d_hi]},
        "wilcoxon_p": p,
        "wilcoxon_stat": stat,
    }


def _cmd_compare(args: argparse.Namespace) -> None:
    r = compare_methods(args.csv, args.metric, args.method_a, args.method_b,
                        args.dataset)
    a, b = r["method_a"], r["method_b"]
    diff = r["diff"]
    print(f"  n_seeds: {r['n_seeds']}")
    print(f"  {a['name']:>20s}: {a['mean']:.3f} ± {a['std']:.3f} "
          f"[95% CI: {a['ci95'][0]:.3f}, {a['ci95'][1]:.3f}]")
    print(f"  {b['name']:>20s}: {b['mean']:.3f} ± {b['std']:.3f} "
          f"[95% CI: {b['ci95'][0]:.3f}, {b['ci95'][1]:.3f}]")
    print(f"  {'Δ (A − B)':>20s}: {diff['mean']:.3f} "
          f"[95% CI: {diff['ci95'][0]:.3f}, {diff['ci95'][1]:.3f}]")
    print(f"  Wilcoxon (A > B): p = {r['wilcoxon_p']:.4f}")
    sig = "*" * sum(r['wilcoxon_p'] < t for t in (0.05, 0.01, 0.001))
    print(f"  Significance: {sig or 'n.s.'}")


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    cmp_p = sub.add_parser("compare", help="A-vs-B Wilcoxon + CIs")
    cmp_p.add_argument("--csv", default="data/results.csv")
    cmp_p.add_argument("--metric", required=True)
    cmp_p.add_argument("--method-a", required=True)
    cmp_p.add_argument("--method-b", required=True)
    cmp_p.add_argument("--dataset")
    cmp_p.set_defaults(func=_cmd_compare)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
