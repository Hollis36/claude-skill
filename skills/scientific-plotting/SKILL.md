---
name: scientific-plotting
description: |
  科研绘图助手，用于创建高质量的学术论文图表。支持统计图表（柱状图、折线图、散点图、箱线图、小提琴图）、科学示意图（流程图、机制图）、数据可视化（热力图、网络图）、高级图表（雷达图、Sankey图、分面图）。集成SciencePlots v2.2.1、Plotly交互式可视化、Plotnine等2025-2026最新工具。使用Python (matplotlib/seaborn/scienceplots/plotly/plotnine)、R (ggplot2) 等工具。当用户需要：(1) 绘制论文图表、(2) 数据可视化、(3) 创建科学示意图、(4) 调整图表样式符合期刊要求时触发。关键词：画图、绘图、可视化、plot、figure、chart、科研绘图。
license: Complete terms in LICENSE.txt
---

# 科研绘图助手

创建符合学术出版标准的高质量图表。

## 友邻 skill

| 投稿场景 | 推荐 |
|---------|------|
| **CS / AI 顶会**（NeurIPS / ICML / ICLR / CVPR / ACL） | **本 skill** — 集成 statannotations、forest plot、显著性 bracket、跨 venue 模板 |
| **Nature / CNS / NMI 系** | **`nature-figure`** (https://github.com/Yuan1z0825/nature-skills) — 单一标准下更深入的设计哲学和多 panel 层次原则 |
| IEEE / ACS / RSC / Elsevier | 本 skill — 各 venue 规格都内建 |

两边互不冲突；Nature/CNS 提交可以两个都开，互相参考。本 skill 已经吸收了 nature-figure 的几个核心想法（语义配色、subfigure 层次、可编辑 SVG）— 见下方"核心原则"。

## 核心原则（开画前先读）

### 1. 图作为论证

每张图独立回答一个论文级问题。开画前先写 caption 第一句"This figure shows ..."，写不出来就不画。

### 2. Multi-panel 层次

反对等尺寸 2×2 网格。推荐"主题 panel（占视觉焦点 2-2.5×）+ 1-2 个从属证据 panel"。

```python
# 推荐
fig, axes = plt.subplots(1, 2, figsize=(7, 3),
                          gridspec_kw={"width_ratios": [2.5, 1]})
panel_main_argument(axes[0])      # 主结论
panel_supporting_evidence(axes[1]) # 为什么 work / 代价是什么
```

### 3. 语义配色跨图一致

一篇论文里 "Ours" 在每张图都用同一个颜色。建立 `METHOD_COLOR` 字典，所有 figure 脚本统一查表：

```python
SEMANTIC = {
    "hero":     "#0F4D92",  # Ours
    "baseline": "#B64342",  # 主竞争者
    "variant":  "#8BCF8B",  # Ours 的正向变体（ablation +X）
    "support":  "#42949E",  # 参考方法 / 次要 baseline
    "neutral":  "#767676",  # 弱基线 / 参考线
    "negative": "#D55E00",  # 失败案例 / drop
}
```

### 4. 防冗余 checklist

不要画"同数据两种表示"、"子集+父集并列"、"两个 ranking 同样方法"、"absolute+absolute 趋势一样"这四种冗余 panel。

### 5. 可编辑 SVG 用于投稿后改字

`svg.fonttype = 'none'` 让 SVG 里文字保持 `<text>` 元素，审稿人挑 typo 时 Inkscape 直接改不用重跑代码。

完整原则参见 `knowledge/methods/figure-standards.md`，可执行实现参见 `projects/_template/figures/matplotlib_settings.py`。

## 工作流程

1. 明确图表类型和数据来源
2. **应用上述核心原则**（层次、配色、防冗余）
3. 选择合适的绘图工具
4. 应用学术样式和配色
5. 输出符合期刊要求的格式（推荐 PDF + 可编辑 SVG）

## 图表类型指南

### 统计图表
| 数据类型 | 推荐图表 | 工具 |
|---------|---------|------|
| 分类比较 | 柱状图/条形图 | matplotlib/seaborn |
| 时间序列 | 折线图 | matplotlib |
| 相关性 | 散点图 | seaborn |
| 分布 | 箱线图/小提琴图 | seaborn |
| 比例 | 饼图/甜甜圈图（谨慎使用） | matplotlib |
| 多维比较 | 雷达图/蜘蛛图 | matplotlib |
| 流向关系 | Sankey流向图 | plotly |
| 多变量分组 | 分面图 (Facet Grid) | plotnine/seaborn |
| 增减变化 | 瀑布图 | matplotlib |

### 科学可视化
| 数据类型 | 推荐图表 | 工具 |
|---------|---------|------|
| 矩阵数据 | 热力图 | seaborn/matplotlib |
| 关系网络 | 网络图 | networkx |
| 高维数据 | PCA/t-SNE/UMAP | sklearn + matplotlib |
| 地理数据 | 地图 | folium/geopandas |
| 3D数据 | 3D图表 | plotly |
| 统计显著性 | 带显著性标注的图 | statannotations |

## SciencePlots（一行代码变身期刊级图表）

```python
# 安装: pip install scienceplots
import scienceplots
import matplotlib.pyplot as plt

# IEEE风格（自动应用所有IEEE格式规范）
plt.style.use(['science', 'ieee'])

# Nature风格
plt.style.use(['science', 'nature'])

# Science期刊风格
plt.style.use(['science', 'science'])

# 色盲友好（与其他样式叠加使用）
plt.style.use(['science', 'ieee', 'colorblind'])

# CJK字体支持（中文/日文/韩文）
plt.style.use(['science', 'cjk-sc-font'])  # 简体中文

# 可堆叠样式组合示例
plt.style.use(['science', 'ieee', 'no-latex'])  # 无需安装LaTeX

# 完整示例
with plt.style.context(['science', 'ieee']):
    fig, ax = plt.subplots(figsize=(3.5, 2.5))
    ax.plot([1, 2, 3, 4], [1, 4, 9, 16], label='$y = x^2$')
    ax.legend()
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    fig.savefig('figure.pdf', bbox_inches='tight')
```

SciencePlots v2.2.1 支持的样式（50+期刊预设）：
- 基础：`science`, `ieee`, `nature`, `scatter`, `high-vis`
- 期刊：`acs`, `rsc`, `aip`, `std-colors`
- 辅助：`colorblind`, `bright`, `no-latex`, `cjk-sc-font`

## 期刊格式规范

### IEEE格式规范

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

### Nature / Science 格式规范

```python
# Nature图表规范
NATURE_SINGLE = (89/25.4, 60/25.4)   # 89mm单栏
NATURE_DOUBLE = (183/25.4, 120/25.4) # 183mm双栏

NATURE_STYLE = {
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'Arial'],
    'font.size': 7,
    'axes.labelsize': 7,
    'xtick.labelsize': 6,
    'ytick.labelsize': 6,
    'legend.fontsize': 6,
    'figure.dpi': 300,
    'lines.linewidth': 0.75,
}
```

### ACS / RSC 化学期刊规范

```python
# ACS图表规范
ACS_SINGLE = (3.25, 2.25)  # 3.25 inches单栏
ACS_DOUBLE = (7.0, 4.5)    # 7 inches双栏
ACS_STYLE = {
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica'],
    'font.size': 8,
    'axes.labelsize': 8,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 7,
}

# RSC图表规范
RSC_SINGLE = (8.0/2.54, 5.5/2.54)  # 8cm单栏
RSC_DOUBLE = (17.0/2.54, 8.5/2.54) # 17cm双栏
```

### Elsevier 图表规范

```python
# Elsevier图表规范
ELSEVIER_SINGLE = (90/25.4, 60/25.4)   # 90mm单栏
ELSEVIER_DOUBLE = (190/25.4, 120/25.4) # 190mm双栏
ELSEVIER_STYLE = {
    'font.size': 8,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
}
```

## Python绘图模板

### 基础设置（含字体嵌入最佳实践）

```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 字体嵌入（确保PDF/EPS中字体可嵌入，避免投稿问题）
plt.rcParams['pdf.fonttype'] = 42   # TrueType字体嵌入PDF
plt.rcParams['ps.fonttype'] = 42    # TrueType字体嵌入PS/EPS
plt.rcParams['svg.fonttype'] = 'none'  # SVG文字保持可编辑（投稿后改label用）

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
        'pdf.fonttype': 42,
        'ps.fonttype': 42,
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

### Statannotations 统计显著性标注

```python
# 安装: pip install statannotations
from statannotations.Annotator import Annotator
import seaborn as sns

fig, ax = plt.subplots(figsize=(4, 3))
data = ...  # 你的数据 DataFrame

# 绘制箱线图
order = ['Group A', 'Group B', 'Group C']
sns.boxplot(x='group', y='value', data=data, order=order, ax=ax)

# 添加统计显著性标注
pairs = [('Group A', 'Group B'), ('Group A', 'Group C'), ('Group B', 'Group C')]
annotator = Annotator(ax, pairs, data=data, x='group', y='value', order=order)
annotator.configure(test='Mann-Whitney', text_format='star', loc='outside')
annotator.apply_and_annotate()

plt.tight_layout()
```

### Plotly 交互式科学可视化

```python
import plotly.graph_objects as go
import plotly.express as px

# 3D散点图
fig = px.scatter_3d(df, x='x', y='y', z='z',
                    color='category', size='weight',
                    title='3D Scientific Visualization')
fig.update_layout(
    scene=dict(
        xaxis_title='X Axis',
        yaxis_title='Y Axis',
        zaxis_title='Z Axis',
    )
)

# HTML导出（用于网页/演示）
fig.write_html('interactive_figure.html')

# 静态图导出（需要安装 kaleido）
# pip install kaleido
fig.write_image('figure.pdf', width=700, height=500)
fig.write_image('figure.png', width=1400, height=1000, scale=2)

# Sankey流向图
fig_sankey = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color='black', width=0.5),
        label=['A', 'B', 'C', 'D'],
        color='blue'
    ),
    link=dict(
        source=[0, 1, 0, 2],
        target=[2, 3, 3, 3],
        value=[8, 4, 2, 8]
    )
)])
```

### Plotnine (Python ggplot2)

```python
# 安装: pip install plotnine
from plotnine import (ggplot, aes, geom_point, geom_line, geom_bar,
                       facet_wrap, theme_classic, labs, scale_color_brewer)
import pandas as pd

# 基础散点图（Grammar of Graphics语法）
p = (ggplot(df, aes('x', 'y', color='group'))
     + geom_point(size=2, alpha=0.7)
     + geom_line()
     + facet_wrap('~condition', ncol=2)  # 分面图
     + theme_classic()
     + labs(title='Title', x='X Label', y='Y Label', color='Group')
     + scale_color_brewer(type='qual', palette='Set1')
)

# 保存为高分辨率图像
p.save('figure.pdf', width=7, height=5, units='in', dpi=300)
```

### 高级图表类型

#### 雷达图 / 蜘蛛图

```python
import numpy as np
import matplotlib.pyplot as plt

def radar_chart(categories, values_list, labels, figsize=(5, 5)):
    N = len(categories)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=figsize, subplot_kw=dict(polar=True))

    for values, label in zip(values_list, labels):
        values += values[:1]
        ax.plot(angles, values, linewidth=2, linestyle='solid', label=label)
        ax.fill(angles, values, alpha=0.1)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, size=9)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    return fig, ax
```

#### 分面图 (Facet Grid)

```python
import seaborn as sns

# Seaborn FacetGrid
g = sns.FacetGrid(df, col='condition', row='group',
                  height=2.5, aspect=1.2)
g.map_dataframe(sns.scatterplot, x='x', y='y', alpha=0.6)
g.add_legend()
g.set_axis_labels('X Label', 'Y Label')
g.set_titles(col_template='{col_name}', row_template='{row_name}')
```

#### 瀑布图

```python
def waterfall_chart(values, labels, figsize=(6, 4)):
    fig, ax = plt.subplots(figsize=figsize)
    cumulative = 0
    bottoms = []
    for i, (val, lbl) in enumerate(zip(values, labels)):
        color = '#2ECC71' if val >= 0 else '#E74C3C'
        ax.bar(i, abs(val), bottom=min(cumulative, cumulative + val),
               color=color, edgecolor='white', linewidth=0.5)
        cumulative += val
        bottoms.append(cumulative)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    return fig, ax
```

#### 甜甜圈图

```python
def donut_chart(values, labels, colors=None, figsize=(5, 5)):
    fig, ax = plt.subplots(figsize=figsize)
    wedges, texts, autotexts = ax.pie(
        values, labels=labels, colors=colors,
        autopct='%1.1f%%', startangle=90,
        wedgeprops={'linewidth': 2, 'edgecolor': 'white'}
    )
    # 甜甜圈效果
    centre_circle = plt.Circle((0, 0), 0.6, fc='white')
    ax.add_patch(centre_circle)
    ax.set_aspect('equal')
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

## 输出规范（矢量图最佳实践）

```python
# 保存为多种格式（含字体嵌入）
def save_figure(fig, name, formats=['pdf', 'png', 'svg']):
    # 确保字体嵌入（避免投稿时字体缺失问题）
    plt.rcParams['pdf.fonttype'] = 42
    plt.rcParams['ps.fonttype'] = 42

    for fmt in formats:
        fig.savefig(f'{name}.{fmt}',
                    dpi=300 if fmt == 'png' else None,
                    bbox_inches='tight',
                    pad_inches=0.05,
                    transparent=True if fmt in ['pdf', 'svg'] else False)
        print(f'Saved: {name}.{fmt}')
```

| 格式 | 用途 | DPI | 字体嵌入 |
|-----|------|-----|---------|
| PDF | 论文投稿、矢量图 | 矢量 | `pdf.fonttype=42` |
| EPS | 部分期刊（Elsevier等）| 矢量 | `ps.fonttype=42` |
| PNG | 网页、PPT | 300-600 | 不适用 |
| SVG | 可编辑矢量图 | 矢量 | 内嵌 |
| TIFF | 部分期刊要求 | 300-600 | 不适用 |

## R ggplot2 模板

```r
library(ggplot2)
library(ggthemes)

# IEEE风格主题
theme_ieee <- function() {
  theme_minimal(base_size = 8, base_family = "serif") +
    theme(
      panel.grid.minor = element_blank(),
      panel.grid.major = element_line(linewidth = 0.3, color = "grey80"),  # ggplot2 >= 3.4.0
      axis.line = element_line(linewidth = 0.5),
      legend.position = "bottom",
      plot.title = element_text(size = 9, face = "bold"),
      axis.title = element_text(size = 8),
      legend.text = element_text(size = 7)
    )
}

# 保存图表（嵌入字体）
ggsave("figure.pdf", width = 3.5, height = 2.5, units = "in", dpi = 300,
       device = cairo_pdf)  # cairo_pdf 确保字体嵌入
```

## 常见问题解决

### 中文显示
```python
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'WenQuanYi Micro Hei']
plt.rcParams['axes.unicode_minus'] = False

# 或使用 SciencePlots CJK 支持（需要系统安装中文字体，如 Noto Sans SC 或 Source Han Sans）
plt.style.use(['science', 'cjk-sc-font'])
```

### LaTeX公式
```python
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
# 使用: ax.set_xlabel(r'$\alpha$ (rad)')

# 无需安装LaTeX时（使用mathtext）
plt.rcParams['text.usetex'] = False
plt.rcParams['mathtext.fontset'] = 'stix'
```

### 子图布局
```python
fig, axes = plt.subplots(2, 2, figsize=(7.16, 5))
fig.tight_layout()
# 或使用 constrained_layout=True
```

## 质量检查清单

- [ ] 图表尺寸符合目标期刊要求
- [ ] 字体大小符合期刊规范（通常6-9pt）
- [ ] 分辨率 ≥ 300 DPI（线图600 DPI）
- [ ] PDF/EPS已设置 `fonttype=42` 确保字体嵌入
- [ ] 色彩方案色盲友好（使用 `colorblind` 样式验证）
- [ ] 坐标轴标签含单位
- [ ] 图例清晰，无遮挡数据
- [ ] 统计误差棒类型已在图注中说明（SD/SEM/CI）
- [ ] 统计显著性标注正确（使用 statannotations 自动化）
- [ ] 文件格式符合期刊要求
