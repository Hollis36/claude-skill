"""Figure 3 — main results across 3 long-context benchmarks.

Reads data/results.csv, computes mean ± std per (method, dataset), draws
grouped bars with significance brackets vs the strongest baseline
(FlashAttention-2).

Demonstrates:
- semantic coloring (Ours = SEMANTIC['hero'] across all figures)
- automatic panel labels via label_panels()
- statistical brackets via add_significance_bracket()

Run: python figure_3_main_results.py
Output: figure_3_main_results.pdf + .png
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import wilcoxon

from matplotlib_settings import (
    SEMANTIC,
    add_significance_bracket,
    apply_paper_style,
    figsize,
    label_panels,
    save,
)


METHOD_ORDER = ["H2O", "StreamingLLM", "FlashAttention-2", "Ours"]
DATASET_ORDER = ["LongBench", "RULER", "InfiniteBench"]

# Locked semantic colors — same in every figure of this paper
METHOD_COLOR = {
    "Ours": SEMANTIC["hero"],
    "FlashAttention-2": SEMANTIC["support"],
    "H2O": SEMANTIC["baseline"],
    "StreamingLLM": SEMANTIC["neutral"],
}


def aggregate(df: pd.DataFrame) -> dict:
    out = {}
    for method in METHOD_ORDER:
        out[method] = {}
        for dataset in DATASET_ORDER:
            vals = df[(df.method == method) & (df.dataset == dataset) &
                      (df.metric_name == "acc")]["metric_value"].to_numpy()
            out[method][dataset] = (vals.mean(), vals.std(ddof=1), vals)
    return out


def panel_main_bars(ax, data):
    n_datasets = len(DATASET_ORDER)
    n_methods = len(METHOD_ORDER)
    width = 0.20
    x_center = np.arange(n_datasets)

    for i, method in enumerate(METHOD_ORDER):
        means = [data[method][d][0] for d in DATASET_ORDER]
        stds = [data[method][d][1] for d in DATASET_ORDER]
        offsets = x_center + (i - (n_methods - 1) / 2) * width
        ax.bar(offsets, means, width, yerr=stds, capsize=2,
               color=METHOD_COLOR[method],
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
        add_significance_bracket(ax, flash_x, ours_x, y_top, p, height=0.8)

    ax.set_xticks(x_center)
    ax.set_xticklabels(DATASET_ORDER)
    ax.set_ylabel("Accuracy (%)")
    ax.set_ylim(40, 92)
    ax.legend(ncol=4, loc="lower right", bbox_to_anchor=(1.0, -0.32))


def panel_latency(ax):
    """Subordinate panel showing latency (the 'why' panel — supports accuracy story)."""
    methods = METHOD_ORDER
    latency_ms = {"H2O": 145, "StreamingLLM": 132, "FlashAttention-2": 220, "Ours": 154}
    x = np.arange(len(methods))
    colors = [METHOD_COLOR[m] for m in methods]
    ax.bar(x, [latency_ms[m] for m in methods], color=colors,
           edgecolor="black", linewidth=0.4)
    ax.set_xticks(x)
    ax.set_xticklabels(methods, rotation=20, ha="right")
    ax.set_ylabel("Latency (ms)")
    ax.axhline(latency_ms["FlashAttention-2"] * 0.7, color="black",
               linestyle="--", linewidth=0.6, alpha=0.5)
    ax.text(0.02, latency_ms["FlashAttention-2"] * 0.7 + 4, "30% under full attn",
            transform=ax.get_yaxis_transform(), fontsize=plt.rcParams["font.size"] - 1,
            color="black", alpha=0.7)


def main() -> None:
    apply_paper_style(venue="neurips")

    csv_path = Path(__file__).parent.parent / "data" / "results.csv"
    df = pd.read_csv(csv_path)
    data = aggregate(df)

    # Two-panel: main result (large, the hero) + latency (small, the supporting evidence)
    fig, axes = plt.subplots(1, 2, figsize=figsize("double", aspect=0.45),
                             gridspec_kw={"width_ratios": [2.5, 1]})
    panel_main_bars(axes[0], data)
    panel_latency(axes[1])
    label_panels(axes, ["(a)", "(b)"])
    fig.tight_layout()

    out = Path(__file__).with_suffix(".pdf")
    save(fig, str(out))


if __name__ == "__main__":
    main()
