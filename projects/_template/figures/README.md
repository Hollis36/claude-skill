# Figures

## 约定

- **源脚本** + **输出 PDF** 都进 git
- 脚本命名：`figure_<n>_<short_desc>.py`，例如 `figure_2_architecture.py`
- 输出命名对应：`figure_2_architecture.pdf`
- 大图（架构图）从 Figma / draw.io 导出，保留 `.fig` 源文件

## 风格统一

所有图必须 `import matplotlib_settings` 加载统一 rcParams（见 `knowledge/methods/figure-standards.md`）。

```python
# 每个绘图脚本顶部
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({
    'pdf.fonttype': 42,
    'font.family': 'serif',
    'font.size': 9,
    # ...
})
```

## 列表（论文里出现的图）

| Fig | 文件 | 用途 |
|-----|------|------|
| 1 | figure_1_teaser.pdf | Introduction teaser |
| 2 | figure_2_architecture.pdf | Method overview |
| 3 | figure_3_main_results.pdf | Main quantitative results |
| 4 | figure_4_ablation.pdf | Ablation visualization |
