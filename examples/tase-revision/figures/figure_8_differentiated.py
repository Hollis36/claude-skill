"""Figure 8 fix — visually differentiate (a) sensitivity vs (b) attribution.

Original problem: (a) sensitivity heatmap-style bars and (b) attribution
horizontal bars use the same monochrome style, so the two panels look
like one chart at first glance.

Fixed:
  (a) Sensitivity → diverging colormap heatmap (variables × objectives)
      Green = beneficial direction, Red = harmful direction, magnitude
      encoded by saturation
  (b) Attribution → stacked +/- bar with green/red, magnitude on x-axis,
      clear distinction between positive contributions (helps) and
      negative ones (hurts)

The bottom workflow row from the original Figure 8 is retained as the
contribution-closure summary (it is removed from Figure 1 instead — see
revision_notes.md P0-1).

Numbers are illustrative; replace with your actual sensitivity matrix
and attribution decomposition.
"""
import matplotlib.pyplot as plt
import numpy as np

from matplotlib_settings import SEMANTIC, add_panel_label, apply_paper_style, figsize, save


# (a) Sensitivity: 6 variables × 4 objectives
VARIABLES = [
    "edge margin $m_e$",
    "spacing $s$",
    "speed $v$",
    "flow $\\phi$",
    "standoff $d$",
    "path type",
]
OBJECTIVES = ["NU", "Coverage", "Time", "Overspray"]
# rows = variables, cols = objectives; sign indicates direction of beneficial change
# positive = increasing this var improves the objective; negative = harms
SENSITIVITY = np.array([
    [+0.85, +0.10, -0.50, -0.20],  # edge margin (negative is uniform mode)
    [-0.60, +0.30, +0.45, -0.30],  # spacing
    [+0.20, -0.40, +0.85, +0.50],  # speed
    [+0.10, +0.65, +0.05, +0.70],  # flow
    [+0.45, +0.15, -0.05, +0.10],  # standoff
    [+0.55, +0.20, -0.30, -0.10],  # path type
])

# (b) Attribution: contribution to overall NU gap
ATTRIBUTION = [
    ("formulation", +14.7, "positive"),
    ("geometry",    +5.1,  "positive"),
    ("model fidelity", +4.0, "positive"),
    ("execution",   +2.9,  "positive"),
    ("optimiser",   -0.5,  "small"),
    ("baseline",    -24.7, "negative"),
]


def panel_a_sensitivity(ax):
    im = ax.imshow(SENSITIVITY, cmap="RdYlGn", vmin=-1, vmax=1, aspect="auto")
    ax.set_xticks(range(len(OBJECTIVES)))
    ax.set_xticklabels(OBJECTIVES)
    ax.set_yticks(range(len(VARIABLES)))
    ax.set_yticklabels(VARIABLES)
    for i in range(len(VARIABLES)):
        for j in range(len(OBJECTIVES)):
            v = SENSITIVITY[i, j]
            ax.text(j, i, f"{v:+.2f}",
                    ha="center", va="center",
                    fontsize=plt.rcParams["font.size"] - 2,
                    color="white" if abs(v) > 0.55 else "black")
    cb = plt.colorbar(im, ax=ax, fraction=0.05, pad=0.02)
    cb.set_label("normalised effect", fontsize=plt.rcParams["font.size"] - 1)
    cb.ax.tick_params(labelsize=plt.rcParams["font.size"] - 2)
    ax.set_title("Parameter–objective sensitivity")


def panel_b_attribution(ax):
    labels = [a[0] for a in ATTRIBUTION]
    values = [a[1] for a in ATTRIBUTION]
    colors = []
    for lab, v, kind in ATTRIBUTION:
        if kind == "negative":
            colors.append(SEMANTIC["baseline"])
        elif kind == "small":
            colors.append(SEMANTIC["neutral"])
        else:
            colors.append(SEMANTIC["variant"])
    y = np.arange(len(labels))[::-1]
    bars = ax.barh(y, values, color=colors,
                   edgecolor="black", linewidth=0.4)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    for i, v in enumerate(values):
        ax.text(v + (0.5 if v > 0 else -0.5), y[i],
                f"{v:+.1f} pp",
                ha="left" if v > 0 else "right", va="center",
                fontsize=plt.rcParams["font.size"] - 1)
    ax.set_xlabel("Contribution to NU (pp)")
    ax.set_xlim(-30, 20)
    ax.set_title("Quality-gap attribution")


def main():
    apply_paper_style(venue="ieee")
    fig, axes = plt.subplots(1, 2, figsize=figsize("double", aspect=0.40),
                              gridspec_kw={"width_ratios": [1.1, 1]})
    panel_a_sensitivity(axes[0])
    panel_b_attribution(axes[1])
    for ax, lbl in zip(axes, ["(a)", "(b)"]):
        add_panel_label(ax, lbl, loc="top-left-outside")
    fig.tight_layout()
    save(fig, "/tmp/paper_fixes/figures/figure_8_differentiated.pdf")


if __name__ == "__main__":
    main()
