"""Figure 4 — forest plot of Ours vs baselines across 3 benchmarks.

Each row is one (method, benchmark) comparison; bar shows 95% CI of the
accuracy improvement of Ours over that baseline. Reference line at 0 = no
improvement. Hero row (Ours) gets SEMANTIC['hero'] color.

Useful for rebuttal "consistency of improvement" argument that single-row
mean tables cannot show.

Run: python figure_4_forest.py
Output: figure_4_forest.pdf + .png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import bootstrap

from matplotlib_settings import (
    SEMANTIC,
    apply_paper_style,
    figsize,
    make_forest_plot,
    save,
)


def diff_ci(a: np.ndarray, b: np.ndarray) -> tuple[float, float, float]:
    diff = a - b
    res = bootstrap((diff,), np.mean, confidence_level=0.95,
                    n_resamples=10000, method="BCa")
    return float(diff.mean()), float(res.confidence_interval.low), float(res.confidence_interval.high)


def main() -> None:
    apply_paper_style(venue="neurips")

    csv_path = Path(__file__).parent.parent / "data" / "results.csv"
    df = pd.read_csv(csv_path)
    df = df[df.metric_name == "acc"]

    rows = []  # (label, mean_diff, low, high)
    for baseline in ["H2O", "StreamingLLM", "FlashAttention-2"]:
        for dataset in ["LongBench", "RULER", "InfiniteBench"]:
            ours = df[(df.method == "Ours") & (df.dataset == dataset)].sort_values("seed")["metric_value"].to_numpy()
            base = df[(df.method == baseline) & (df.dataset == dataset)].sort_values("seed")["metric_value"].to_numpy()
            m, lo, hi = diff_ci(ours, base)
            rows.append((f"vs {baseline}  /  {dataset}", m, lo, hi))

    names = [r[0] for r in rows]
    means = [r[1] for r in rows]
    lows = [r[2] for r in rows]
    highs = [r[3] for r in rows]

    fig, ax = plt.subplots(figsize=figsize("single", aspect=1.3))
    make_forest_plot(ax, names, means, lows, highs, ref_line=0.0)
    ax.set_xlabel("Accuracy improvement (pp), 95% CI")
    ax.axvspan(0, max(highs) * 1.05, color=SEMANTIC["hero"], alpha=0.05)

    out = Path(__file__).with_suffix(".pdf")
    save(fig, str(out))


if __name__ == "__main__":
    main()
