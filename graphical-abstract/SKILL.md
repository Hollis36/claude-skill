---
name: graphical-abstract
description: |
  学术论文摘要结构图(Graphical Abstract/TOC图)创建助手。支持多种工具：Python (matplotlib/PIL/drawsvg)、HTML/CSS/SVG、TikZ/LaTeX、Figma MCP、Banana Pro MCP。当用户需要：(1) 绘制论文摘要图/TOC图、(2) 创建研究流程示意图、(3) 设计期刊投稿用的图形摘要、(4) 制作学术海报的核心图示时触发。关键词：graphical abstract、摘要图、TOC图、流程图、示意图、机制图、架构图。
---

# 摘要结构图创建助手

创建高质量的学术论文图形摘要(Graphical Abstract)和目录图(TOC)。

## 工具选择指南

| 场景 | 推荐工具 | 优势 |
|-----|---------|------|
| 包含数据图表 | Python matplotlib | 数据与示意图无缝结合 |
| 复杂流程/架构 | HTML/SVG | 灵活布局，易于迭代 |
| LaTeX论文配套 | TikZ | 风格统一，矢量输出 |
| 精美设计稿 | **Figma MCP** | 专业设计，协作方便 |
| 快速原型 | **Banana Pro MCP** | AI辅助生成，速度快 |

## 期刊尺寸规范

```python
# 常见期刊Graphical Abstract尺寸
JOURNAL_SIZES = {
    'cell': (1800, 1200),      # Cell系列: 1800x1200 px, 300 DPI
    'nature': (180, 180),       # Nature: 180x180 mm (正方形)
    'science': (900, 600),      # Science: 宽高比3:2
    'elsevier': (531, 300),     # Elsevier: 531x300 px (5x3 cm @300DPI)
    'acs': (3.25, 1.75),        # ACS: 3.25x1.75 inches
    'wiley': (500, 250),        # Wiley: 宽高比2:1
    'rsc': (560, 280),          # RSC: 8x4 cm @300DPI
}

# 通用尺寸 (inches)
SIZES_INCH = {
    'landscape': (8, 4),        # 横向 2:1
    'square': (6, 6),           # 正方形
    'wide': (10, 4),            # 超宽 5:2
}
```

## 设计原则

1. **视觉流向**: 左→右 或 上→下，符合阅读习惯
2. **信息层次**: 3-5个关键步骤，不超过7个元素
3. **色彩统一**: 使用2-3种主色，保持一致性
4. **留白充足**: 元素间距 ≥ 元素尺寸的20%
5. **字体清晰**: 最小字号12pt，Sans-serif字体

## 工具一：Python方案

### 基础模板

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

def create_graphical_abstract(figsize=(8, 4), dpi=300):
    """创建摘要图画布"""
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.set_aspect('equal')
    ax.axis('off')
    return fig, ax

def add_box(ax, x, y, width, height, text, color='#4A90D9', text_color='white'):
    """添加带文字的方框"""
    box = FancyBboxPatch((x, y), width, height,
                         boxstyle="round,pad=0.05,rounding_size=0.2",
                         facecolor=color, edgecolor='none')
    ax.add_patch(box)
    ax.text(x + width/2, y + height/2, text,
            ha='center', va='center', fontsize=10,
            color=text_color, fontweight='bold')

def add_arrow(ax, start, end, color='#333333'):
    """添加箭头"""
    arrow = FancyArrowPatch(start, end,
                            arrowstyle='-|>',
                            mutation_scale=15,
                            color=color, linewidth=2)
    ax.add_patch(arrow)

# 使用示例
fig, ax = create_graphical_abstract()
add_box(ax, 0.5, 2, 2, 1, 'Input\nData', '#E74C3C')
add_arrow(ax, (2.7, 2.5), (3.3, 2.5))
add_box(ax, 3.5, 2, 2, 1, 'Model', '#3498DB')
add_arrow(ax, (5.7, 2.5), (6.3, 2.5))
add_box(ax, 6.5, 2, 2, 1, 'Output', '#2ECC71')
plt.savefig('graphical_abstract.png', bbox_inches='tight', pad_inches=0.1)
```

### 复杂布局模板

```python
def create_pipeline_abstract():
    """创建流水线式摘要图"""
    fig = plt.figure(figsize=(10, 5), dpi=300)

    # 使用GridSpec灵活布局
    gs = fig.add_gridspec(2, 4, hspace=0.3, wspace=0.3)

    # 顶部：主流程
    ax_main = fig.add_subplot(gs[0, :])
    ax_main.axis('off')

    # 底部：细节面板
    ax1 = fig.add_subplot(gs[1, 0])
    ax2 = fig.add_subplot(gs[1, 1])
    ax3 = fig.add_subplot(gs[1, 2])
    ax4 = fig.add_subplot(gs[1, 3])

    return fig, (ax_main, ax1, ax2, ax3, ax4)
```

## 工具二：HTML/SVG方案

适合复杂交互式设计，可导出为PNG/PDF。

```html
<!DOCTYPE html>
<html>
<head>
<style>
.ga-container {
  width: 1800px;
  height: 1200px;
  background: white;
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding: 40px;
  font-family: 'Arial', sans-serif;
}
.ga-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
}
.ga-box {
  width: 280px;
  height: 180px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 24px;
  font-weight: bold;
  text-align: center;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
.ga-arrow {
  font-size: 48px;
  color: #666;
}
.step1 { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
.step2 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
.step3 { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
.ga-label {
  font-size: 18px;
  color: #333;
  font-weight: 500;
}
</style>
</head>
<body>
<div class="ga-container">
  <div class="ga-step">
    <div class="ga-box step1">Input<br/>Data</div>
    <div class="ga-label">Step 1</div>
  </div>
  <div class="ga-arrow">→</div>
  <div class="ga-step">
    <div class="ga-box step2">Processing<br/>Model</div>
    <div class="ga-label">Step 2</div>
  </div>
  <div class="ga-arrow">→</div>
  <div class="ga-step">
    <div class="ga-box step3">Results<br/>Output</div>
    <div class="ga-label">Step 3</div>
  </div>
</div>
</body>
</html>
```

使用Playwright截图导出：
```python
from playwright.sync_api import sync_playwright

def export_html_to_image(html_path, output_path, width=1800, height=1200):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': width, 'height': height})
        page.goto(f'file://{html_path}')
        page.screenshot(path=output_path, type='png')
        browser.close()
```

## 工具三：TikZ/LaTeX方案

```latex
\documentclass[tikz,border=10pt]{standalone}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows.meta,positioning,shadows}

\begin{document}
\begin{tikzpicture}[
    node distance=2.5cm,
    box/.style={
        rectangle, rounded corners=8pt,
        minimum width=3cm, minimum height=1.5cm,
        text centered, font=\sffamily\bfseries,
        drop shadow, text=white
    },
    arrow/.style={-{Stealth[length=8pt]}, thick, color=gray}
]

% 定义颜色
\definecolor{step1}{HTML}{E74C3C}
\definecolor{step2}{HTML}{3498DB}
\definecolor{step3}{HTML}{2ECC71}

% 节点
\node[box, fill=step1] (input) {Input\\Data};
\node[box, fill=step2, right=of input] (model) {Model};
\node[box, fill=step3, right=of model] (output) {Output};

% 箭头
\draw[arrow] (input) -- (model);
\draw[arrow] (model) -- (output);

\end{tikzpicture}
\end{document}
```

## 工具四：Figma MCP集成

当安装了Figma MCP服务器时，可直接调用Figma API创建设计。

### 使用流程

1. 确认MCP连接：检查Figma MCP是否可用
2. 创建设计文件：使用MCP工具创建新文件
3. 添加元素：通过API添加形状、文本、箭头
4. 导出图片：导出为PNG/PDF格式

### 常用MCP调用模式

```
# 创建新文件
figma_create_file(name="Graphical Abstract", width=1800, height=1200)

# 添加矩形
figma_create_rectangle(x=100, y=400, width=300, height=200,
                       fill_color="#4A90D9", corner_radius=12)

# 添加文本
figma_create_text(x=250, y=500, text="Input Data",
                  font_size=24, font_weight="bold", color="#FFFFFF")

# 添加箭头
figma_create_arrow(start_x=420, start_y=500, end_x=520, end_y=500)

# 导出
figma_export(format="png", scale=2)
```

## 工具五：Banana Pro MCP集成

Banana Pro提供AI辅助图像生成能力。

### 使用场景

- 生成背景插图
- 创建图标元素
- 风格化处理

### 调用模式

```
# 生成科研风格背景
banana_generate(prompt="scientific abstract background, minimalist,
                blue gradient, molecular structure silhouette",
                width=1800, height=1200, style="academic")

# 生成图标
banana_generate(prompt="flat icon of neural network, white background,
                simple geometric style", width=200, height=200)
```

## 配色方案

```python
# 学科专用配色
PALETTES = {
    'cs_ai': ['#4A90D9', '#7B68EE', '#00CED1', '#FF6B6B', '#48D1CC'],
    'biology': ['#27AE60', '#E74C3C', '#3498DB', '#F39C12', '#9B59B6'],
    'chemistry': ['#1ABC9C', '#E67E22', '#3498DB', '#E74C3C', '#9B59B6'],
    'physics': ['#2C3E50', '#3498DB', '#E74C3C', '#F39C12', '#1ABC9C'],
    'medical': ['#E74C3C', '#3498DB', '#2ECC71', '#F39C12', '#95A5A6'],
}

# 渐变色对
GRADIENTS = {
    'blue': ('#667eea', '#764ba2'),
    'pink': ('#f093fb', '#f5576c'),
    'cyan': ('#4facfe', '#00f2fe'),
    'orange': ('#fa709a', '#fee140'),
    'green': ('#38ef7d', '#11998e'),
}
```

## 输出检查清单

- [ ] 尺寸符合目标期刊要求
- [ ] DPI ≥ 300
- [ ] 文字清晰可读（缩小50%后仍可辨认）
- [ ] 色彩对比度足够
- [ ] 无版权问题的图标/素材
- [ ] 文件格式正确（通常PNG/TIFF）
