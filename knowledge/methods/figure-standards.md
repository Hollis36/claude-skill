# 期刊级图表规范

详细绘图工具见 `skills/scientific-plotting/`。本文是**审稿前的检查清单**和**模板规范**。

## 文件格式

| 用途 | 格式 | 原因 |
|------|------|------|
| 矢量主图（流程、示意） | **PDF / SVG / EPS** | LaTeX 友好，无限缩放 |
| 大数据点（>10k 点散点图） | **PNG (600 dpi)** | 矢量会爆炸 |
| 论文最终提交 | **PDF**（LaTeX `\includegraphics`） | 期刊首选 |
| 投稿系统单独要求 | **TIFF/EPS** | 检查投稿指南 |

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
