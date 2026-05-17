"""Shared matplotlib settings for all paper figures.

Every figure_*.py MUST start with:

    from matplotlib_settings import apply_paper_style
    apply_paper_style()

Override per-figure: pass column='single' (default) or 'double'.
For specific journal: pass venue='neurips' / 'icml' / 'ieee' / 'nature'.
"""
from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt


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


def apply_paper_style(venue: str = "default", grid: bool = False) -> None:
    base = VENUE_BASE_SIZE.get(venue, 9)
    mpl.rcParams.update(
        {
            "figure.dpi": 300,
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.02,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
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
