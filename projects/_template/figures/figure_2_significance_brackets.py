"""Example figure — multi-panel comparison with significance brackets.

Demonstrates two common rebuttal needs:
1. Multi-panel layout sharing y-axis
2. Significance annotations (∗ / ∗∗ / ∗∗∗) based on p-values

Run: python figure_2_significance_brackets.py
Output: figure_2_significance_brackets.pdf + .png

Bracket logic is implemented manually (no statannotations dependency)
so this works in any clean Python env.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib_settings import apply_paper_style, figsize, save


def add_significance_bracket(
    ax,
    x_left: float,
    x_right: float,
    y: float,
    p: float,
    height: float = 0.5,
    line_kwargs: dict | None = None,
) -> None:
    """Draw a significance bracket spanning (x_left, x_right) at height y.

    p mapping: <0.001 → ***, <0.01 → **, <0.05 → *, else n.s.
    """
    if p < 0.001:
        label = "∗∗∗"
    elif p < 0.01:
        label = "∗∗"
    elif p < 0.05:
        label = "∗"
    else:
        label = "n.s."

    lk = {"color": "black", "linewidth": 0.8}
    if line_kwargs:
        lk.update(line_kwargs)

    ax.plot([x_left, x_left, x_right, x_right],
            [y, y + height, y + height, y], **lk)
    ax.text((x_left + x_right) / 2, y + height + 0.05, label,
            ha="center", va="bottom", fontsize=plt.rcParams["font.size"])


def panel(ax, df: pd.DataFrame, title: str, p_values: dict[tuple[str, str], float]) -> None:
    methods = df["method"].tolist()
    x = np.arange(len(methods))
    ax.bar(x, df["acc_mean"], yerr=df["acc_std"], capsize=3,
           edgecolor="black", linewidth=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(methods, rotation=15)
    ax.set_title(title)
    ax.set_ylim(78, 92)

    # Stack brackets above the tallest bar
    y_top = (df["acc_mean"] + df["acc_std"]).max() + 0.8
    method_to_x = {m: i for i, m in enumerate(methods)}
    for (a, b), p in p_values.items():
        if a in method_to_x and b in method_to_x:
            add_significance_bracket(ax, method_to_x[a], method_to_x[b], y_top, p)
            y_top += 1.5


def main() -> None:
    apply_paper_style(venue="neurips")

    # Real version: pull from data/results.csv via stats.py or pandas groupby
    d1 = pd.DataFrame({
        "method": ["Baseline A", "Baseline B", "Ours"],
        "acc_mean": [82.1, 84.7, 87.3],
        "acc_std": [0.3, 0.2, 0.2],
    })
    d2 = pd.DataFrame({
        "method": ["Baseline A", "Baseline B", "Ours"],
        "acc_mean": [75.2, 77.9, 80.4],
        "acc_std": [0.5, 0.4, 0.3],
    })

    # Pairwise p-values from paired Wilcoxon (compute via scripts/stats.py)
    p_d1 = {("Ours", "Baseline B"): 0.008, ("Ours", "Baseline A"): 0.001}
    p_d2 = {("Ours", "Baseline B"): 0.012, ("Ours", "Baseline A"): 0.003}

    fig, axes = plt.subplots(1, 2, figsize=figsize("double", aspect=0.40), sharey=True)
    panel(axes[0], d1, "D1 (ImageNet)", p_d1)
    panel(axes[1], d2, "D2 (COCO)", p_d2)
    axes[0].set_ylabel("Accuracy (%)")
    fig.tight_layout()

    out = Path(__file__).with_suffix(".pdf")
    save(fig, str(out))


if __name__ == "__main__":
    main()
