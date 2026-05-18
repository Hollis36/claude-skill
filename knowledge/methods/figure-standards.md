# 期刊级图表规范

详细绘图工具见 `skills/scientific-plotting/`。本文是**审稿前的检查清单**和**模板规范**。

---

## 图作为论证（先想清楚再画）

每张图都是论文的**一个独立论证**，不是"显示数据"。开画前问 3 个问题：

1. **这张图回答什么问题？** 一句话能写出来 → 写进 figure caption 第一句
2. **没有这张图，论证还成立吗？** 如果成立 → 删掉，节省版面
3. **同一张图里每个 panel 都答**不同的**问题吗？** 是 → 留；否 → 合并或拆分

### 防冗余 checklist（多 panel 图）

容易踩的 4 个 trap，agent 画图前自查：

| Trap | 例子 | 改 |
|------|------|-----|
| **同数据两种表示** | (a) 折线图 + (b) 同数据的散点 | 留一种 |
| **子集 + 父集并列** | (a) 全数据集 mean + (b) 三个子集 mean | 把子集合并进 (a) 用颜色区分 |
| **两个 ranking** | (a) 按 accuracy 排 + (b) 按 latency 排同样方法 | 用一张散点 acc vs latency |
| **绝对值 + 绝对值** | (a) 各方法 acc + (b) 各方法 F1，且趋势一样 | 留 acc 主图，F1 进表 |

### Multi-panel 层次原则

**反对**等尺寸 2×2 网格填满 canvas。**推荐**："一个主题 panel + 1-2 个从属证据 panel"。

```
# 反模式（弱）：4 个一样大的 panel，读者不知道看哪个
fig, axes = plt.subplots(2, 2, figsize=(7, 5))

# 推荐：主面板大 2.5×，旁边小面板提供支撑证据
fig, axes = plt.subplots(1, 2, figsize=(7, 3),
                          gridspec_kw={"width_ratios": [2.5, 1]})
panel_main_argument(axes[0])      # 主结论（占视觉焦点）
panel_supporting_evidence(axes[1]) # "为什么 work" 或 "代价是什么"
```

例：主图是 accuracy bar chart，从属是 latency 或 parameter count。

### Subfigure 标注

- 永远用 `(a) (b) (c)` 格式，不要用 `A. B. C.` 或 `① ② ③`
- 标签位置：**axes 左上外侧**（最常见、最清晰）
- 字号 = axes title 字号 + 1，**bold**
- 用 `matplotlib_settings.py` 里的 `label_panels(axes)` 自动加，不要手动 `ax.text` 一个个写

---

## 语义配色（跨图一致性）

最常见的 reviewer 抱怨之一："Figure 3 里 Ours 是蓝色，Figure 5 里 Ours 怎么变红了？"

**铁律**：一篇论文中，**同一个方法在所有图里用同一个颜色**，不随机分配。

`matplotlib_settings.py` 里的 `SEMANTIC` 字典就是为此：

```python
from matplotlib_settings import SEMANTIC

METHOD_COLOR = {
    "Ours":             SEMANTIC["hero"],      # 主方法 — 蓝
    "Strong Baseline":  SEMANTIC["baseline"],   # 主竞争者 — 红
    "Reference Method": SEMANTIC["support"],    # 参考 — 青
    "Older Baseline":   SEMANTIC["neutral"],    # 弱基线 — 灰
    "Our Ablation +X":  SEMANTIC["variant"],    # Ours 变体 — 绿
}
```

每张图开头 import 这个字典，每个 method 都查表取色 — agent 画图时**强制查表**，不要 cycler 默认。

### 配色三原则

1. **每图一个克制配色族** — 一个主色 + 一个对比色 + 灰，**不要彩虹**
2. **绿/红只用于方向性**（improvement = 绿，drop = 红），不要用在分类
3. **类别 > 7 个？** — 你的图设计本身有问题，重新组织（合并、分面、聚类）

---

## 文件格式

| 用途 | 格式 | 原因 |
|------|------|------|
| 矢量主图（流程、示意） | **PDF / SVG / EPS** | LaTeX 友好，无限缩放 |
| 大数据点（>10k 点散点图） | **PNG (600 dpi)** | 矢量会爆炸 |
| 论文最终提交 | **PDF**（LaTeX `\includegraphics`） | 期刊首选 |
| 投稿系统单独要求 | **TIFF/EPS** | 检查投稿指南 |
| 投稿后**改 label**用 | **SVG with `svg.fonttype='none'`** | 文字保持可编辑，Illustrator/Inkscape 直接改不用重跑代码 |

### 可编辑 SVG（投稿后救命）

```python
import matplotlib as mpl
mpl.rcParams['svg.fonttype'] = 'none'   # 必须！否则文字变成 path
fig.savefig('figure.svg')
```

效果：保存的 SVG 里 `<text>` 还是 `<text>`，不是 `<path d="...">`。审稿人挑出 typo 时直接 Inkscape 改完导 PDF，不用回去找数据 + 跑脚本 + 重画。

`matplotlib_settings.py` 默认已开启，正常用 `apply_paper_style()` 就有。

## 分辨率与尺寸

- **彩色图**：≥ 300 dpi（CMYK 模式期刊检查）
- **黑白线图**：≥ 600 dpi
- **单栏宽度**：~ 3.5 in / 8.9 cm（NeurIPS、IEEE）
- **双栏宽度**：~ 7.0 in / 17.8 cm
- **页面高度上限**：~ 9 in；超过会被排版工人投诉

## 字体

- **嵌入字体**（PDF）：用 matplotlib 时 `mpl.rcParams['pdf.fonttype'] = 42`（TrueType），避免 Type 3 被期刊拒
- **正文字体大小**：图内文字 ≥ 7pt（双栏图）/ 8pt（单栏图），不小于正文 -2pt
- **统一字体族**：与 LaTeX 主文一致（Times、Computer Modern 或 Helvetica）

## 配色

| 场景 | 推荐 palette |
|------|-------------|
| 分类（≤ 8 类） | tab10 / Set2 / Okabe-Ito（色盲安全） |
| 序列（顺序数据） | viridis / cividis / mako |
| 发散（有中点） | RdBu_r / coolwarm |
| 黑白打印兼容 | 用线型 / 填充图案区分，不只靠颜色 |

**色盲安全**：避免红绿对比；用 colorbrewer.org 或 `seaborn.color_palette("colorblind")` 验证。

## 必检清单（投稿前 5 分钟）

- [ ] **坐标轴标签**有单位，例如 `Accuracy (%)` 不是 `Accuracy`
- [ ] **图例位置**不挡数据；可用 `bbox_to_anchor` 移到外面
- [ ] **误差条 / 阴影**是 std / SEM / 95% CI 哪种？caption 写清楚
- [ ] **n 标注**（每组样本数 / seed 数）
- [ ] **显著性标记**（`*` p<0.05、`**` p<0.01、`***` p<0.001，或写明具体 p 值）
- [ ] **数值范围合理**，0 不要剪掉除非有理由
- [ ] **统一风格**：所有图字号、线宽、配色一致
- [ ] **subfigure 标注**（a / b / c），位置和大小统一
- [ ] **caption 自包含**，读者不看正文也能懂图
- [ ] **黑白打印** 仍可读

## 常见错误

| 错误 | 后果 | 修复 |
|------|------|------|
| 默认 matplotlib 字体（DejaVu）混入 LaTeX | 字体不一致 | 用 `usetex=True` 或换 Computer Modern |
| 3D 柱状图 / 饼图 | 评审吐槽 | 改用 2D 柱状或表格 |
| 双 y 轴乱用 | 误导读者 | 拆成两个 subplot |
| Y 轴从 70% 起，"巨大提升"假象 | 审稿人扣分 | 标注或拆段 |
| jpg 格式提交矢量图 | 期刊拒收 | 换 pdf / eps |

## matplotlib 论文级 rcParams 模板

```python
import matplotlib as mpl
mpl.rcParams.update({
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'pdf.fonttype': 42,           # TrueType, 避免 Type 3
    'ps.fonttype': 42,
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'CMU Serif'],
    'font.size': 9,
    'axes.labelsize': 9,
    'axes.titlesize': 10,
    'legend.fontsize': 8,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'axes.linewidth': 0.8,
    'lines.linewidth': 1.2,
    'lines.markersize': 4,
    'legend.frameon': False,
})
```

## SciencePlots 一行启用

```python
import scienceplots
plt.style.use(['science', 'ieee'])  # 或 'nature', 'no-latex' 若无 TeX
```

## Caption 写作模板

> **Figure N. 简短标题（≤ 一行）.** (a) 描述子图 a，包括关键发现.
> (b) 描述子图 b. Error bars indicate 95% bootstrap CI over 5 random seeds (n=5).
> Significance: ∗ p<0.05, ∗∗ p<0.01, ∗∗∗ p<0.001 (paired Wilcoxon, Holm-corrected).
