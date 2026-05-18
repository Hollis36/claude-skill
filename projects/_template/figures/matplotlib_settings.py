"""Shared matplotlib settings for all paper figures.

Every figure_*.py MUST start with:

    from matplotlib_settings import apply_paper_style
    apply_paper_style()

Override per-figure: pass column='single' (default) or 'double'.
For specific journal: pass venue='neurips' / 'icml' / 'ieee' / 'nature'.

Key conventions enforced (do not bypass):
- pdf.fonttype = 42 (TrueType, prevents Type-3 rejection by journals)
- svg.fonttype = 'none' (keeps text editable in Illustrator/Inkscape,
  so you can fix label typos after submission without re-rendering)
- Colorblind-safe default cycler
- Semantic colors (SEMANTIC dict) for cross-figure consistency
"""
from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# ---------- Color systems ----------

# Default cycler: colorblind-safe (Okabe–Ito)
COLORBLIND_SAFE = [
    "#0072B2",  # blue
    "#D55E00",  # vermillion
    "#009E73",  # bluish green
    "#CC79A7",  # reddish purple
    "#F0E442",  # yellow
    "#56B4E9",  # sky blue
    "#E69F00",  # orange
    "#000000",  # black
]

# Semantic colors — use THESE across ALL figures in one paper so the
# "Ours" method has the same color in Table 1, Figure 3, ablation chart, etc.
# Adopted from the nature-figure skill's hero/baseline/variant convention.
SEMANTIC = {
    "hero":     "#0F4D92",  # Your proposed method (Ours). Same blue everywhere.
    "baseline": "#B64342",  # Strongest competing baseline.
    "variant":  "#8BCF8B",  # Positive variant of Ours (e.g., ablation +X).
    "negative": "#D55E00",  # Negative finding / drop / failure case.
    "support":  "#42949E",  # Secondary baseline, supporting evidence.
    "neutral":  "#767676",  # Reference line, background, "Other".
}

# ---------- Sizing ----------

COLUMN_WIDTH = {
    "single": 3.5,
    "double": 7.0,
    "single_in_cm": 8.9 / 2.54,
    "double_in_cm": 17.8 / 2.54,
}

VENUE_BASE_SIZE = {
    "neurips": 9,
    "icml": 9,
    "iclr": 9,
    "cvpr": 8,
    "ieee": 8,
    "nature": 7,
    "acl": 9,
    "default": 9,
}


# ---------- Core style ----------

def apply_paper_style(venue: str = "default", grid: bool = False) -> None:
    base = VENUE_BASE_SIZE.get(venue, 9)
    mpl.rcParams.update(
        {
            "figure.dpi": 300,
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.02,
            "pdf.fonttype": 42,        # TrueType — required by most journals
            "ps.fonttype": 42,
            "svg.fonttype": "none",     # keep SVG text editable post-submission
            "font.family": "serif",
            "font.serif": ["Times New Roman", "CMU Serif", "DejaVu Serif"],
            "font.size": base,
            "axes.labelsize": base,
            "axes.titlesize": base + 1,
            "legend.fontsize": base - 1,
            "xtick.labelsize": base - 1,
            "ytick.labelsize": base - 1,
            "axes.linewidth": 0.8,
            "axes.grid": grid,
            "grid.linewidth": 0.4,
            "grid.alpha": 0.3,
            "lines.linewidth": 1.2,
            "lines.markersize": 4,
            "legend.frameon": False,
            "legend.handlelength": 1.5,
        }
    )
    plt.rcParams["axes.prop_cycle"] = mpl.cycler(color=COLORBLIND_SAFE)


def figsize(column: str = "single", aspect: float = 0.75) -> tuple[float, float]:
    w = COLUMN_WIDTH[column]
    return (w, w * aspect)


def save(fig, path: str, also_png: bool = True) -> None:
    fig.savefig(path)
    if also_png and path.endswith(".pdf"):
        fig.savefig(path.replace(".pdf", ".png"), dpi=300)


# ---------- Multi-panel helpers ----------

def add_panel_label(
    ax,
    label: str,
    loc: str = "top-left-outside",
    fontsize: float | None = None,
    weight: str = "bold",
) -> None:
    """Add a subfigure label like (a), (b), (c).

    loc options:
      - 'top-left-outside': above-left of axes (most common in ML/CS)
      - 'top-left-inside':  inside top-left corner
      - 'top-right-outside': above-right (rare)
    """
    fs = fontsize if fontsize is not None else plt.rcParams["axes.titlesize"] + 1
    if loc == "top-left-outside":
        x, y, ha, va = -0.10, 1.05, "left", "bottom"
    elif loc == "top-left-inside":
        x, y, ha, va = 0.02, 0.97, "left", "top"
    elif loc == "top-right-outside":
        x, y, ha, va = 1.0, 1.05, "right", "bottom"
    else:
        raise ValueError(f"unknown loc: {loc}")
    ax.text(x, y, label, transform=ax.transAxes,
            fontsize=fs, fontweight=weight, ha=ha, va=va)


def label_panels(axes, labels: list[str] | None = None, **kwargs) -> None:
    """Label every axes in `axes` with (a), (b), (c), ... in row-major order."""
    flat = np.asarray(axes).flatten()
    if labels is None:
        labels = [f"({chr(ord('a') + i)})" for i in range(len(flat))]
    for ax, lbl in zip(flat, labels):
        add_panel_label(ax, lbl, **kwargs)


# ---------- Higher-level plot helpers ----------

def make_grouped_bar(
    ax,
    df,                       # DataFrame with one row per (group, method)
    group_col: str,
    method_col: str,
    value_col: str,
    err_col: str | None = None,
    method_order: list[str] | None = None,
    method_colors: dict[str, str] | None = None,
    width: float = 0.18,
) -> None:
    """Grouped bar chart with consistent semantic coloring.

    Pass `method_colors` to lock e.g. {"Ours": SEMANTIC['hero'], "BaselineX": SEMANTIC['baseline']}
    """
    groups = df[group_col].drop_duplicates().tolist()
    methods = method_order or df[method_col].drop_duplicates().tolist()
    x_center = np.arange(len(groups))
    n = len(methods)
    for i, method in enumerate(methods):
        sub = df[df[method_col] == method].set_index(group_col).loc[groups]
        offsets = x_center + (i - (n - 1) / 2) * width
        color = (method_colors or {}).get(method)
        kwargs = dict(width=width, edgecolor="black", linewidth=0.4, label=method)
        if color is not None:
            kwargs["color"] = color
        if err_col is not None:
            kwargs["yerr"] = sub[err_col].to_numpy()
            kwargs["capsize"] = 2
        ax.bar(offsets, sub[value_col].to_numpy(), **kwargs)
    ax.set_xticks(x_center)
    ax.set_xticklabels(groups)


def make_forest_plot(
    ax,
    names: list[str],
    means: list[float],
    lows: list[float],
    highs: list[float],
    ref_line: float | None = None,
    hero_idx: int | None = None,
) -> None:
    """Forest plot — horizontal CI bars + point estimates.

    Ideal for rebuttal: "Method X improvement over baseline across N benchmarks."
    `hero_idx` marks one row with SEMANTIC['hero'] color (e.g., the row for "Ours").
    """
    y = np.arange(len(names))[::-1]
    for i, (m, lo, hi) in enumerate(zip(means, lows, highs)):
        color = SEMANTIC["hero"] if i == hero_idx else SEMANTIC["neutral"]
        ax.plot([lo, hi], [y[i], y[i]], color=color, linewidth=1.2)
        ax.plot([lo, lo], [y[i] - 0.15, y[i] + 0.15], color=color, linewidth=0.8)
        ax.plot([hi, hi], [y[i] - 0.15, y[i] + 0.15], color=color, linewidth=0.8)
        ax.plot(m, y[i], "o", color=color, markersize=5)
    if ref_line is not None:
        ax.axvline(ref_line, color="black", linestyle="--", linewidth=0.7,
                   alpha=0.6)
    ax.set_yticks(y)
    ax.set_yticklabels(names)
    ax.set_ylim(-0.5, len(names) - 0.5)


def add_significance_bracket(
    ax,
    x_left: float,
    x_right: float,
    y: float,
    p: float,
    height: float = 0.5,
) -> None:
    """Draw an ∗ / ∗∗ / ∗∗∗ / n.s. bracket between two x positions."""
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
            ha="center", va="bottom",
            fontsize=plt.rcParams["font.size"] - 1)
