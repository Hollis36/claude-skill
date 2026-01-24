# 摘要图模板库

## 目录

1. [流程型模板](#流程型模板)
2. [对比型模板](#对比型模板)
3. [层次型模板](#层次型模板)
4. [放射型模板](#放射型模板)
5. [混合型模板](#混合型模板)

---

## 流程型模板

适用于：方法流程、实验步骤、数据处理管线

### 水平流程（3步）

```
┌─────────┐     ┌─────────┐     ┌─────────┐
│  Step 1 │ ──▶ │  Step 2 │ ──▶ │  Step 3 │
│  Input  │     │ Process │     │  Output │
└─────────┘     └─────────┘     └─────────┘
```

### 水平流程（5步带分支）

```
┌───────┐   ┌───────┐   ┌───────┐   ┌───────┐   ┌───────┐
│ Data  │──▶│ Pre-  │──▶│ Model │──▶│ Post- │──▶│Result │
│       │   │process│   │       │   │process│   │       │
└───────┘   └───────┘   └───┬───┘   └───────┘   └───────┘
                            │
                        ┌───▼───┐
                        │Ablation│
                        └───────┘
```

### 垂直流程

```
    ┌─────────────────┐
    │   Raw Data      │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │  Preprocessing  │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │   Training      │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │   Evaluation    │
    └─────────────────┘
```

---

## 对比型模板

适用于：方法对比、Before/After、多方案评估

### 左右对比

```
┌─────────────────┐         ┌─────────────────┐
│                 │         │                 │
│    Previous     │   VS    │     Ours        │
│    Method       │         │    Method       │
│                 │         │                 │
│  ✗ Slow         │         │  ✓ Fast         │
│  ✗ Inaccurate   │         │  ✓ Accurate     │
└─────────────────┘         └─────────────────┘
```

### 多列对比

```
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│Method A │  │Method B │  │Method C │  │  Ours   │
├─────────┤  ├─────────┤  ├─────────┤  ├─────────┤
│ ██░░░░  │  │ ███░░░  │  │ ████░░  │  │ ██████  │
│  60%    │  │  75%    │  │  85%    │  │  95%    │
└─────────┘  └─────────┘  └─────────┘  └─────────┘
```

---

## 层次型模板

适用于：系统架构、模型结构、分层设计

### 三层架构

```
┌─────────────────────────────────────────────┐
│              Application Layer              │
├─────────────────────────────────────────────┤
│               Service Layer                 │
├─────────────────────────────────────────────┤
│                Data Layer                   │
└─────────────────────────────────────────────┘
```

### 模型架构（神经网络）

```
┌─────────────────────────────────────────────┐
│                  Output                     │
└──────────────────────┬──────────────────────┘
                       │
┌──────────────────────▼──────────────────────┐
│              Decoder Layers                 │
│   ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐       │
│   │Attn │  │ FFN │  │Attn │  │ FFN │       │
│   └─────┘  └─────┘  └─────┘  └─────┘       │
└──────────────────────┬──────────────────────┘
                       │
┌──────────────────────▼──────────────────────┐
│              Encoder Layers                 │
│   ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐       │
│   │Attn │  │ FFN │  │Attn │  │ FFN │       │
│   └─────┘  └─────┘  └─────┘  └─────┘       │
└──────────────────────┬──────────────────────┘
                       │
┌──────────────────────▼──────────────────────┐
│                  Input                      │
└─────────────────────────────────────────────┘
```

---

## 放射型模板

适用于：核心概念展示、多应用场景、特性展示

### 中心放射

```
                    ┌─────────┐
                    │  App 1  │
                    └────┬────┘
                         │
    ┌─────────┐     ┌────▼────┐     ┌─────────┐
    │  App 4  ├─────┤  CORE   ├─────┤  App 2  │
    └─────────┘     └────┬────┘     └─────────┘
                         │
                    ┌────▼────┐
                    │  App 3  │
                    └─────────┘
```

### 环形布局

```
              Feature 1
                 ╱╲
                ╱  ╲
    Feature 6 ╱    ╲ Feature 2
              │    │
              │CORE│
              │    │
    Feature 5 ╲    ╱ Feature 3
                ╲  ╱
                 ╲╱
              Feature 4
```

---

## 混合型模板

适用于：复杂系统、多阶段研究、综合展示

### 流程+对比混合

```
┌─────────────────────────────────────────────────────────┐
│                    PROBLEM SETTING                       │
└───────────────────────────┬─────────────────────────────┘
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
     ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
     │  Baseline   │ │   Ours v1   │ │   Ours v2   │
     └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
            │               │               │
            ▼               ▼               ▼
     ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
     │   65.2%     │ │   78.5%     │ │   89.3%     │
     └─────────────┘ └─────────────┘ └─────────────┘
```

### 输入-处理-输出完整版

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  ┌─────────┐                                     ┌─────────┐   │
│  │  Image  │─┐                               ┌──▶│  Label  │   │
│  └─────────┘ │   ┌─────────────────────┐    │   └─────────┘   │
│              ├──▶│                     │────┤                  │
│  ┌─────────┐ │   │      Our Model      │    │   ┌─────────┐   │
│  │  Text   │─┤   │                     │    └──▶│  Score  │   │
│  └─────────┘ │   └─────────────────────┘        └─────────┘   │
│              │              │                                  │
│  ┌─────────┐ │              ▼                                  │
│  │  Meta   │─┘   ┌─────────────────────┐                      │
│  └─────────┘     │   Loss Function     │                      │
│                  └─────────────────────┘                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Python实现：流程型模板

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

def create_flow_template(steps, colors=None, figsize=(10, 4)):
    """
    创建水平流程图模板

    Args:
        steps: list of str, 步骤名称
        colors: list of str, 每步颜色(可选)
        figsize: tuple, 图像尺寸
    """
    n = len(steps)
    if colors is None:
        colors = ['#4A90D9', '#E74C3C', '#2ECC71', '#F39C12', '#9B59B6'][:n]

    fig, ax = plt.subplots(figsize=figsize, dpi=300)
    ax.set_xlim(0, n * 3)
    ax.set_ylim(0, 3)
    ax.set_aspect('equal')
    ax.axis('off')

    box_width, box_height = 2, 1.2
    y_center = 1.5

    for i, (step, color) in enumerate(zip(steps, colors)):
        x = i * 3 + 0.5

        # 绘制方框
        box = FancyBboxPatch((x, y_center - box_height/2),
                             box_width, box_height,
                             boxstyle="round,pad=0.05,rounding_size=0.15",
                             facecolor=color, edgecolor='none')
        ax.add_patch(box)

        # 添加文字
        ax.text(x + box_width/2, y_center, step,
                ha='center', va='center', fontsize=11,
                color='white', fontweight='bold')

        # 添加箭头（除最后一个）
        if i < n - 1:
            arrow = FancyArrowPatch((x + box_width + 0.1, y_center),
                                   (x + box_width + 0.9, y_center),
                                   arrowstyle='-|>', mutation_scale=15,
                                   color='#555555', linewidth=2)
            ax.add_patch(arrow)

    return fig, ax

# 使用示例
fig, ax = create_flow_template(['Data', 'Preprocess', 'Train', 'Evaluate'])
plt.savefig('flow_template.png', bbox_inches='tight', dpi=300)
```

---

## SVG模板：可编辑版本

```svg
<svg width="1800" height="600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#667eea"/>
      <stop offset="100%" style="stop-color:#764ba2"/>
    </linearGradient>
    <linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#f093fb"/>
      <stop offset="100%" style="stop-color:#f5576c"/>
    </linearGradient>
    <linearGradient id="grad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#4facfe"/>
      <stop offset="100%" style="stop-color:#00f2fe"/>
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="2" dy="4" stdDeviation="4" flood-opacity="0.2"/>
    </filter>
  </defs>

  <!-- Step 1 -->
  <rect x="100" y="200" width="400" height="200" rx="20"
        fill="url(#grad1)" filter="url(#shadow)"/>
  <text x="300" y="310" text-anchor="middle" fill="white"
        font-family="Arial" font-size="32" font-weight="bold">Input Data</text>

  <!-- Arrow 1 -->
  <path d="M520 300 L620 300" stroke="#666" stroke-width="4"
        marker-end="url(#arrowhead)"/>

  <!-- Step 2 -->
  <rect x="700" y="200" width="400" height="200" rx="20"
        fill="url(#grad2)" filter="url(#shadow)"/>
  <text x="900" y="310" text-anchor="middle" fill="white"
        font-family="Arial" font-size="32" font-weight="bold">Processing</text>

  <!-- Arrow 2 -->
  <path d="M1120 300 L1220 300" stroke="#666" stroke-width="4"
        marker-end="url(#arrowhead)"/>

  <!-- Step 3 -->
  <rect x="1300" y="200" width="400" height="200" rx="20"
        fill="url(#grad3)" filter="url(#shadow)"/>
  <text x="1500" y="310" text-anchor="middle" fill="white"
        font-family="Arial" font-size="32" font-weight="bold">Results</text>

  <!-- Arrowhead marker -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7"
            refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#666"/>
    </marker>
  </defs>
</svg>
```
