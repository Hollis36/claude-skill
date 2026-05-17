"""Figure 3 — main results across 3 long-context benchmarks.

Reads data/results.csv, computes mean ± std per (method, dataset), draws
grouped bars with significance brackets vs the strongest baseline
(FlashAttention-2).

Run: python figure_3_main_results.py
Output: figure_3_main_results.pdf + .png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import wilcoxon

from matplotlib_settings import apply_paper_style, figsize, save


METHOD_ORDER = ["H2O", "StreamingLLM", "FlashAttention-2", "Ours"]
DATASET_ORDER = ["LongBench", "RULER", "InfiniteBench"]


def aggregate(df: pd.DataFrame) -> dict:
    out = {}
    for method in METHOD_ORDER:
        out[method] = {}
        for dataset in DATASET_ORDER:
            vals = df[(df.method == method) & (df.dataset == dataset) &
                      (df.metric_name == "acc")]["metric_value"].to_numpy()
            out[method][dataset] = (vals.mean(), vals.std(ddof=1), vals)
    return out


def add_bracket(ax, x_left, x_right, y, p, height=0.6):
    if p < 0.001:
        label = "∗∗∗"
    elif p < 0.01:
        label = "∗∗"
    elif p < 0.05:
        label = "∗"
    else:
        label = "n.s."
    ax.plot([x_left, x_left, x_right, x_right],
            [y, y + height, y + height, y],
            color="black", linewidth=0.7)
    ax.text((x_left + x_right) / 2, y + height + 0.1, label,
            ha="center", va="bottom", fontsize=plt.rcParams["font.size"] - 1)


def main() -> None:
    apply_paper_style(venue="neurips")

    csv_path = Path(__file__).parent.parent / "data" / "results.csv"
    df = pd.read_csv(csv_path)
    data = aggregate(df)

    fig, ax = plt.subplots(figsize=figsize("double", aspect=0.45))

    n_datasets = len(DATASET_ORDER)
    n_methods = len(METHOD_ORDER)
    width = 0.20
    x_center = np.arange(n_datasets)

    for i, method in enumerate(METHOD_ORDER):
        means = [data[method][d][0] for d in DATASET_ORDER]
        stds = [data[method][d][1] for d in DATASET_ORDER]
        offsets = x_center + (i - (n_methods - 1) / 2) * width
        ax.bar(offsets, means, width, yerr=stds, capsize=2,
               edgecolor="black", linewidth=0.4, label=method)

    # Significance brackets: Ours vs FlashAttention-2 per dataset
    for j, dataset in enumerate(DATASET_ORDER):
        flash_vals = data["FlashAttention-2"][dataset][2]
        ours_vals = data["Ours"][dataset][2]
        _, p = wilcoxon(ours_vals, flash_vals, alternative="greater")

        flash_x = x_center[j] + (METHOD_ORDER.index("FlashAttention-2") - 1.5) * width
        ours_x = x_center[j] + (METHOD_ORDER.index("Ours") - 1.5) * width
        y_top = max(data["Ours"][dataset][0] + data["Ours"][dataset][1],
                    data["FlashAttention-2"][dataset][0] +
                    data["FlashAttention-2"][dataset][1]) + 1.5
        add_bracket(ax, flash_x, ours_x, y_top, p)

    ax.set_xticks(x_center)
    ax.set_xticklabels(DATASET_ORDER)
    ax.set_ylabel("Accuracy (%)")
    ax.set_ylim(40, 92)
    ax.legend(ncol=4, loc="lower right", bbox_to_anchor=(1.0, -0.30))

    out = Path(__file__).with_suffix(".pdf")
    save(fig, str(out))


if __name__ == "__main__":
    main()
