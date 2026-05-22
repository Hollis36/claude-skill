"""Figure 5(c) fix — split dual-axis HV/IGD into two side-by-side panels.

Original: one bar chart with HV on left y-axis (range ~0-8) and IGD on right
y-axis (range ~0-6), p=0.0002 annotated ambiguously between them.

Fixed: two panels, each with its own y-axis. Color-code consistently per
method (NSGA-II = hero, MOEA/D = baseline). Direction arrow per panel.

Plug into the paper as the new Figure 5(c). Numbers taken from Table V.
"""
import matplotlib.pyplot as plt
import numpy as np

from matplotlib_settings import SEMANTIC, apply_paper_style, figsize, save


METHODS = ["NSGA-II", "MOEA/D"]
METHOD_COLOR = {"NSGA-II": SEMANTIC["hero"], "MOEA/D": SEMANTIC["baseline"]}

HV_MEAN = [7.6528, 5.7588]
HV_STD  = [0.0359, 0.3552]
IGD_MEAN = [0.3994, 4.7043]
IGD_STD  = [0.0936, 1.1969]
P_HV  = 0.0002
P_IGD = 0.0002


def _panel(ax, mean, std, ylabel, direction, p):
    x = np.arange(len(METHODS))
    colors = [METHOD_COLOR[m] for m in METHODS]
    bars = ax.bar(x, mean, yerr=std, capsize=3,
                  color=colors, edgecolor="black", linewidth=0.5)
    for i, (m, s) in enumerate(zip(mean, std)):
        ax.text(i, m + s + 0.05 * max(mean), f"{m:.2f}",
                ha="center", va="bottom",
                fontsize=plt.rcParams["font.size"] - 1)
    ax.set_xticks(x)
    ax.set_xticklabels(METHODS)
    ax.set_ylabel(f"{ylabel} ({direction})")
    top = max(m + s for m, s in zip(mean, std)) * 1.25
    ax.set_ylim(0, top)
    # Significance bracket
    y_bracket = top * 0.88
    h = top * 0.03
    ax.plot([0, 0, 1, 1],
            [y_bracket, y_bracket + h, y_bracket + h, y_bracket],
            color="black", linewidth=0.7)
    star = "∗∗∗" if p < 0.001 else ("∗∗" if p < 0.01 else "∗")
    ax.text(0.5, y_bracket + h + 0.01 * top,
            f"{star}  (p = {p:.4f})", ha="center", va="bottom",
            fontsize=plt.rcParams["font.size"] - 1)


def main():
    apply_paper_style(venue="ieee")
    fig, axes = plt.subplots(1, 2, figsize=figsize("double", aspect=0.42))
    _panel(axes[0], HV_MEAN,  HV_STD,  "Hypervolume HV",            "higher is better", P_HV)
    _panel(axes[1], IGD_MEAN, IGD_STD, "Inverted gen. distance IGD", "lower is better", P_IGD)
    fig.tight_layout()
    save(fig, "/tmp/paper_fixes/figures/figure_5c_fixed.pdf")


if __name__ == "__main__":
    main()
