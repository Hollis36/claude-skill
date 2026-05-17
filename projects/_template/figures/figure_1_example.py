"""Example figure — bar chart with error bars.

Run: python figure_1_example.py
Output: figure_1_example.pdf + figure_1_example.png

Replace data loading with your own. Keep the apply_paper_style() call
at the top and use save() at the bottom so all figures stay consistent.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib_settings import apply_paper_style, figsize, save


def main() -> None:
    apply_paper_style(venue="neurips")

    # Real version: df = pd.read_csv("../data/results.csv")
    df = pd.DataFrame(
        {
            "method": ["Baseline A", "Baseline B", "Ours"],
            "acc_mean": [82.1, 84.7, 87.3],
            "acc_std": [0.3, 0.2, 0.2],
        }
    )

    fig, ax = plt.subplots(figsize=figsize("single", aspect=0.7))
    x = np.arange(len(df))
    ax.bar(x, df["acc_mean"], yerr=df["acc_std"], capsize=3,
           edgecolor="black", linewidth=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(df["method"])
    ax.set_ylabel("Accuracy (%)")
    ax.set_ylim(80, 90)

    out = Path(__file__).with_suffix(".pdf")
    save(fig, str(out))


if __name__ == "__main__":
    main()
