---
name: scientific-plotting
description: |
  科研绘图助手，用于创建高质量的学术论文图表。支持统计图表（柱状图、折线图、散点图、箱线图、小提琴图）、科学示意图（流程图、机制图）、数据可视化（热力图、网络图）。使用Python (matplotlib/seaborn/plotly)、R (ggplot2) 等工具。当用户需要：(1) 绘制论文图表、(2) 数据可视化、(3) 创建科学示意图、(4) 调整图表样式符合期刊要求时触发。关键词：画图、绑图、绑图、绑图、可视化、plot、figure、chart、科研绘图。
---

# 科研绘图助手

创建符合学术出版标准的高质量图表。

## 工作流程

1. 明确图表类型和数据来源
2. 选择合适的绘图工具
3. 应用学术样式和配色
4. 输出符合期刊要求的格式

## 图表类型指南

### 统计图表
| 数据类型 | 推荐图表 | 工具 |
|---------|---------|------|
| 分类比较 | 柱状图/条形图 | matplotlib/seaborn |
| 时间序列 | 折线图 | matplotlib |
| 相关性 | 散点图 | seaborn |
| 分布 | 箱线图/小提琴图 | seaborn |
| 比例 | 饼图（谨慎使用） | matplotlib |

### 科学可视化
| 数据类型 | 推荐图表 | 工具 |
|---------|---------|------|
| 矩阵数据 | 热力图 | seaborn/matplotlib |
| 关系网络 | 网络图 | networkx |
| 高维数据 | PCA/t-SNE | sklearn + matplotlib |
| 地理数据 | 地图 | folium/geopandas |

## IEEE格式规范

```python
# IEEE双栏论文图表尺寸
SINGLE_COLUMN = (3.5, 2.5)   # 单栏: 3.5 inches
DOUBLE_COLUMN = (7.16, 4.0)  # 双栏: 7.16 inches

# IEEE字体要求
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'font.size': 8,
    'axes.labelsize': 8,
    'axes.titlesize': 9,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 7,
    'figure.dpi': 300,
})
```

## Python绘图模板

### 基础设置

```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 学术风格初始化
def setup_academic_style():
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['Times New Roman', 'DejaVu Serif'],
        'mathtext.fontset': 'stix',
        'axes.linewidth': 0.8,
        'axes.edgecolor': '#333333',
        'grid.linewidth': 0.5,
        'grid.alpha': 0.3,
        'figure.dpi': 300,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.05,
    })
```

### 常用图表示例

```python
# 带误差棒的柱状图
def bar_with_error(data, labels, errors, ylabel, figsize=(3.5, 2.5)):
    fig, ax = plt.subplots(figsize=figsize)
    x = np.arange(len(labels))
    bars = ax.bar(x, data, yerr=errors, capsize=3,
                  color=COLORS['primary'], edgecolor='black', linewidth=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel(ylabel)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    return fig, ax

# 多组折线图
def multi_line(x, y_list, labels, xlabel, ylabel, figsize=(3.5, 2.5)):
    fig, ax = plt.subplots(figsize=figsize)
    for i, (y, label) in enumerate(zip(y_list, labels)):
        ax.plot(x, y, marker=MARKERS[i], label=label,
                color=PALETTE[i], linewidth=1.5, markersize=4)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(frameon=False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    return fig, ax
```

## 配色方案

详细配色方案见 [references/color-palettes.md](references/color-palettes.md)

### 快速参考

```python
# 学术常用配色
ACADEMIC_COLORS = {
    'blue': '#0077BB',
    'orange': '#EE7733',
    'green': '#009988',
    'red': '#CC3311',
    'purple': '#AA3377',
    'grey': '#BBBBBB',
}

# 色盲友好配色 (Paul Tol)
COLORBLIND_SAFE = ['#4477AA', '#EE6677', '#228833', '#CCBB44', '#66CCEE', '#AA3377']

# 期刊常用渐变
SEQUENTIAL = plt.cm.viridis  # 单色渐变
DIVERGING = plt.cm.RdBu_r    # 双向渐变
```

## 输出规范

```python
# 保存为多种格式
def save_figure(fig, name, formats=['pdf', 'png', 'svg']):
    for fmt in formats:
        fig.savefig(f'{name}.{fmt}',
                    dpi=300 if fmt == 'png' else None,
                    bbox_inches='tight',
                    pad_inches=0.05,
                    transparent=True if fmt in ['pdf', 'svg'] else False)
```

| 格式 | 用途 | DPI |
|-----|------|-----|
| PDF | 论文投稿、矢量图 | 矢量 |
| PNG | 网页、PPT | 300 |
| SVG | 可编辑矢量图 | 矢量 |
| TIFF | 部分期刊要求 | 300-600 |

## R ggplot2 模板

```r
library(ggplot2)
library(ggthemes)

# IEEE风格主题
theme_ieee <- function() {
  theme_minimal(base_size = 8, base_family = "serif") +
    theme(
      panel.grid.minor = element_blank(),
      panel.grid.major = element_line(size = 0.3, color = "grey80"),
      axis.line = element_line(size = 0.5),
      legend.position = "bottom",
      plot.title = element_text(size = 9, face = "bold"),
      axis.title = element_text(size = 8),
      legend.text = element_text(size = 7)
    )
}

# 保存图表
ggsave("figure.pdf", width = 3.5, height = 2.5, units = "in", dpi = 300)
```

## 常见问题解决

### 中文显示
```python
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
```

### LaTeX公式
```python
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
# 使用: ax.set_xlabel(r'$\alpha$ (rad)')
```

### 子图布局
```python
fig, axes = plt.subplots(2, 2, figsize=(7.16, 5))
fig.tight_layout()
# 或使用 constrained_layout=True
```
