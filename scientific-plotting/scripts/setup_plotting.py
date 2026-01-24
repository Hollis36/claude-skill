#!/usr/bin/env python3
"""
科研绘图环境初始化脚本
提供标准化的绘图设置和常用函数
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# ============ 配色方案 ============

# 学术通用配色
ACADEMIC_COLORS = {
    'blue': '#0077BB',
    'orange': '#EE7733',
    'green': '#009988',
    'red': '#CC3311',
    'purple': '#AA3377',
    'grey': '#BBBBBB',
}

# 色盲友好配色 (Paul Tol)
COLORBLIND_SAFE = ['#4477AA', '#EE6677', '#228833', '#CCBB44', '#66CCEE', '#AA3377', '#BBBBBB']

# Wong配色
WONG_COLORS = ['#000000', '#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7']

# 默认调色板
PALETTE = COLORBLIND_SAFE

# 标记符号
MARKERS = ['o', 's', '^', 'D', 'v', '<', '>', 'p', 'h']

# ============ 尺寸规范 ============

# IEEE双栏论文
IEEE_SINGLE_COL = (3.5, 2.5)    # 单栏宽度 3.5 inches
IEEE_DOUBLE_COL = (7.16, 4.0)   # 双栏宽度 7.16 inches

# Nature期刊
NATURE_SINGLE = (89/25.4, 60/25.4)   # 89mm
NATURE_DOUBLE = (183/25.4, 100/25.4) # 183mm

# 通用尺寸
FIGURE_SIZES = {
    'small': (3.5, 2.5),
    'medium': (5, 3.5),
    'large': (7, 5),
    'wide': (7, 3),
    'square': (4, 4),
}


def setup_ieee_style():
    """设置IEEE论文风格"""
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams.update({
        # 字体设置
        'font.family': 'serif',
        'font.serif': ['Times New Roman', 'DejaVu Serif'],
        'font.size': 8,
        'axes.labelsize': 8,
        'axes.titlesize': 9,
        'xtick.labelsize': 7,
        'ytick.labelsize': 7,
        'legend.fontsize': 7,

        # 数学字体
        'mathtext.fontset': 'stix',

        # 线条样式
        'axes.linewidth': 0.8,
        'axes.edgecolor': '#333333',
        'grid.linewidth': 0.5,
        'grid.alpha': 0.3,
        'lines.linewidth': 1.5,
        'lines.markersize': 4,

        # 输出质量
        'figure.dpi': 150,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.05,
        'savefig.transparent': False,

        # 图例
        'legend.frameon': False,
        'legend.borderpad': 0.3,
    })


def setup_nature_style():
    """设置Nature期刊风格"""
    plt.style.use('seaborn-v0_8-white')
    plt.rcParams.update({
        'font.family': 'sans-serif',
        'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
        'font.size': 7,
        'axes.labelsize': 8,
        'axes.titlesize': 8,
        'xtick.labelsize': 6,
        'ytick.labelsize': 6,
        'legend.fontsize': 6,
        'mathtext.fontset': 'dejavusans',
        'axes.linewidth': 0.5,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'figure.dpi': 150,
        'savefig.dpi': 300,
    })


def setup_chinese_support():
    """启用中文支持"""
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'WenQuanYi Micro Hei']
    plt.rcParams['axes.unicode_minus'] = False


def setup_latex_support():
    """启用LaTeX渲染"""
    plt.rcParams['text.usetex'] = True
    plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}\usepackage{amssymb}'


# ============ 绘图辅助函数 ============

def remove_spines(ax, keep=['bottom', 'left']):
    """移除坐标轴边框"""
    for spine in ['top', 'right', 'bottom', 'left']:
        ax.spines[spine].set_visible(spine in keep)


def add_significance(ax, x1, x2, y, p_value, height=0.02):
    """添加显著性标记"""
    if p_value < 0.001:
        text = '***'
    elif p_value < 0.01:
        text = '**'
    elif p_value < 0.05:
        text = '*'
    else:
        text = 'n.s.'

    y_range = ax.get_ylim()[1] - ax.get_ylim()[0]
    bar_height = y_range * height

    ax.plot([x1, x1, x2, x2], [y, y + bar_height, y + bar_height, y],
            lw=0.8, c='black')
    ax.text((x1 + x2) / 2, y + bar_height, text,
            ha='center', va='bottom', fontsize=7)


def save_figure(fig, name, formats=None, dpi=300):
    """保存图表为多种格式"""
    if formats is None:
        formats = ['pdf', 'png']

    for fmt in formats:
        fig.savefig(
            f'{name}.{fmt}',
            dpi=dpi if fmt == 'png' else None,
            bbox_inches='tight',
            pad_inches=0.05,
            transparent=(fmt in ['pdf', 'svg'])
        )
        print(f"Saved: {name}.{fmt}")


# ============ 常用图表模板 ============

def bar_plot(data, labels, ylabel, errors=None, colors=None, figsize=IEEE_SINGLE_COL):
    """带误差棒的柱状图"""
    fig, ax = plt.subplots(figsize=figsize)
    x = np.arange(len(labels))

    if colors is None:
        colors = PALETTE[0]

    bars = ax.bar(x, data, yerr=errors, capsize=3,
                  color=colors, edgecolor='black', linewidth=0.5)

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel(ylabel)
    remove_spines(ax)

    return fig, ax


def line_plot(x, y_list, labels, xlabel, ylabel, figsize=IEEE_SINGLE_COL):
    """多组折线图"""
    fig, ax = plt.subplots(figsize=figsize)

    for i, (y, label) in enumerate(zip(y_list, labels)):
        ax.plot(x, y, marker=MARKERS[i % len(MARKERS)], label=label,
                color=PALETTE[i % len(PALETTE)], linewidth=1.5, markersize=4)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(frameon=False, loc='best')
    remove_spines(ax)

    return fig, ax


def scatter_plot(x, y, xlabel, ylabel, hue=None, figsize=IEEE_SINGLE_COL):
    """散点图"""
    fig, ax = plt.subplots(figsize=figsize)

    if hue is None:
        ax.scatter(x, y, c=PALETTE[0], s=20, alpha=0.7, edgecolors='none')
    else:
        for i, h in enumerate(np.unique(hue)):
            mask = hue == h
            ax.scatter(x[mask], y[mask], c=PALETTE[i % len(PALETTE)],
                      s=20, alpha=0.7, edgecolors='none', label=h)
        ax.legend(frameon=False)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    remove_spines(ax)

    return fig, ax


def heatmap(data, xticklabels=None, yticklabels=None, cmap='viridis',
            figsize=IEEE_SINGLE_COL, annot=False):
    """热力图"""
    fig, ax = plt.subplots(figsize=figsize)

    im = ax.imshow(data, cmap=cmap, aspect='auto')

    if xticklabels is not None:
        ax.set_xticks(np.arange(len(xticklabels)))
        ax.set_xticklabels(xticklabels, rotation=45, ha='right')

    if yticklabels is not None:
        ax.set_yticks(np.arange(len(yticklabels)))
        ax.set_yticklabels(yticklabels)

    if annot:
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                ax.text(j, i, f'{data[i, j]:.2f}', ha='center', va='center',
                       fontsize=6, color='white' if data[i, j] > data.max()/2 else 'black')

    cbar = fig.colorbar(im, ax=ax, shrink=0.8)

    return fig, ax


# ============ 主程序 ============

if __name__ == '__main__':
    # 默认使用IEEE风格
    setup_ieee_style()
    print("科研绘图环境已初始化 (IEEE风格)")
    print(f"可用配色: ACADEMIC_COLORS, COLORBLIND_SAFE, WONG_COLORS")
    print(f"可用尺寸: IEEE_SINGLE_COL, IEEE_DOUBLE_COL, FIGURE_SIZES")
