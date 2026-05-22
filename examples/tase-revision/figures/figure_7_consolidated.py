"""Figure 7 fix — consolidate 5 panels to 3.

Original 5-panel layout:
  (a) Scanned geometry mesh        | (b) Local patch normals
  (c) Planned paths + edge proxy   | (d) Simulated thickness on geometry
  (e) Hard-case full point cloud

Problem: (b)(c)(d) are the same patch shown with different overlays — readers
must scan three panels to mentally assemble the pipeline. This is the
"sub-component fragmentation" anti-pattern in figure-standards.md.

Fixed 3-panel layout:
  (a) Scanned geometry mesh
  (b) Patch with COMBINED overlay: normals + planned path + thickness map
  (c) Hard-case full point cloud

This template uses synthetic geometry to illustrate the layout. Swap in
real scan data when rebuilding for the paper. Style follows TASE / IEEE.
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

from matplotlib_settings import SEMANTIC, add_panel_label, apply_paper_style, figsize, save


def panel_a_global(ax):
    """Scanned geometry mesh — wireframe + bounding box."""
    np.random.seed(0)
    n = 400
    # Synthetic point cloud shaped like an irregular industrial part
    theta = np.random.uniform(0, 2 * np.pi, n)
    r = 1 + 0.3 * np.cos(3 * theta) + 0.1 * np.random.randn(n)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax.scatter(x, y, s=1.5, color=SEMANTIC["neutral"], alpha=0.6)
    # Patch box selection
    box = plt.Rectangle((0.3, 0.2), 0.5, 0.5, fill=False,
                        edgecolor=SEMANTIC["hero"], linewidth=1.5,
                        linestyle="--")
    ax.add_patch(box)
    ax.annotate("local patch", xy=(0.55, 0.45), xytext=(1.3, 0.8),
                arrowprops=dict(arrowstyle="->", color="black", lw=0.7),
                fontsize=plt.rcParams["font.size"] - 1)
    ax.set_xlim(-1.8, 2.2)
    ax.set_ylim(-1.8, 1.8)
    ax.set_aspect("equal")
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title("Scanned mesh (full object)")


def panel_b_combined(ax):
    """Combined overlay: patch geometry + normals + planned path + thickness."""
    # Thickness colormap as background
    xx, yy = np.meshgrid(np.linspace(0, 1, 80), np.linspace(0, 1, 80))
    thickness = 0.7 + 0.3 * np.exp(-((xx - 0.5) ** 2 + (yy - 0.5) ** 2) / 0.15)
    thickness *= 1 - 0.4 * (((xx - 0.5) ** 2 + (yy - 0.5) ** 2) > 0.18)
    im = ax.imshow(thickness, extent=[0, 1, 0, 1], origin="lower",
                   cmap="RdBu_r", alpha=0.55, vmin=0.3, vmax=1.1)

    # Planned spiral path
    t = np.linspace(0, 1, 300)
    a = 0.45 * (1 - 0.85 * t)
    px = 0.5 + a * np.cos(t * 14)
    py = 0.5 + a * np.sin(t * 14)
    ax.plot(px, py, color="black", linewidth=1.0, alpha=0.9,
            label="planned path")

    # Normal vectors at sampled points
    sample = np.linspace(20, 280, 6).astype(int)
    for i in sample:
        nx, ny = -np.cos(t[i] * 14), -np.sin(t[i] * 14)
        ax.add_patch(FancyArrowPatch((px[i], py[i]),
                                     (px[i] + 0.08 * nx, py[i] + 0.08 * ny),
                                     arrowstyle="->", color=SEMANTIC["hero"],
                                     mutation_scale=8, linewidth=0.8))

    # Edge proxy boundary
    edge = plt.Rectangle((0.05, 0.05), 0.9, 0.9, fill=False,
                         edgecolor=SEMANTIC["baseline"], linewidth=1.0,
                         linestyle=":", label="edge proxy")
    ax.add_patch(edge)

    ax.set_xlim(-0.05, 1.05); ax.set_ylim(-0.05, 1.05)
    ax.set_aspect("equal")
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title("Local patch:  thickness + path + normals")

    # Shared compact legend inside panel
    legend_elements = [
        plt.Line2D([0], [0], color="black", lw=1.0, label="path"),
        plt.Line2D([0], [0], color=SEMANTIC["hero"], lw=0.8, label="normal"),
        plt.Line2D([0], [0], color=SEMANTIC["baseline"], lw=1.0,
                   linestyle=":", label="edge"),
    ]
    ax.legend(handles=legend_elements, loc="upper right",
              fontsize=plt.rcParams["font.size"] - 2,
              frameon=True, framealpha=0.9, handlelength=1.2)

    # Colorbar
    cb = plt.colorbar(im, ax=ax, fraction=0.04, pad=0.02)
    cb.set_label("film thickness (μm)", fontsize=plt.rcParams["font.size"] - 1)
    cb.ax.tick_params(labelsize=plt.rcParams["font.size"] - 2)


def panel_c_hardcase(ax):
    """Hard-case full-object point cloud with patch paths."""
    np.random.seed(1)
    n = 800
    theta = np.random.uniform(0, 2 * np.pi, n)
    phi = np.random.uniform(0, np.pi, n)
    r = 1 + 0.1 * np.random.randn(n)
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    ax.scatter(x, y, s=1.0, color=SEMANTIC["neutral"], alpha=0.4)
    # Sample patch paths overlaid
    np.random.seed(2)
    for _ in range(5):
        cx, cy = np.random.uniform(-1, 1, 2)
        t = np.linspace(0, 1, 60)
        a = 0.18 * (1 - 0.8 * t)
        px = cx + a * np.cos(t * 10)
        py = cy + a * np.sin(t * 10)
        ax.plot(px, py, color=SEMANTIC["hero"], linewidth=0.7, alpha=0.8)
    ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal")
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title("Hard case: patch paths on full cloud")


def main():
    apply_paper_style(venue="ieee")
    # 3-panel row, the middle (combined) panel is wider — main-panel hierarchy
    fig, axes = plt.subplots(1, 3, figsize=figsize("double", aspect=0.32),
                              gridspec_kw={"width_ratios": [1, 1.6, 1]})
    panel_a_global(axes[0])
    panel_b_combined(axes[1])
    panel_c_hardcase(axes[2])
    # Auto panel labels (a)(b)(c)
    for ax, lbl in zip(axes, ["(a)", "(b)", "(c)"]):
        add_panel_label(ax, lbl, loc="top-left-outside")
    fig.tight_layout()
    save(fig, "/tmp/paper_fixes/figures/figure_7_consolidated.pdf")


if __name__ == "__main__":
    main()
