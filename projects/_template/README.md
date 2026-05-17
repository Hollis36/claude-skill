# [Project Name] — 论文项目骨架

复制此目录后改名作起步：`cp -r projects/_template projects/your-paper-name`

## 目录结构

```
your-paper-name/
├── README.md          ← 本文件，项目元数据 + 当前状态
├── draft/             ← LaTeX 草稿
│   ├── main.tex
│   ├── sections/      ← 按章节拆分
│   └── neurips_2025.sty (或其他模板)
├── figures/           ← 论文图表（pdf / png 源文件 + 绘图脚本）
├── data/              ← 实验结果（CSV / JSON 摘要，**不放原始数据**）
├── refs/              ← BibTeX + 关键文献笔记
│   └── main.bib
└── response/          ← Rebuttal / Response to Reviewers
```

## 项目元数据（agent 读这里）

- **标题**：[Tentative title]
- **目标投稿**：[NeurIPS / ICML / ICLR / ...] [Year]
- **截止时间**：[YYYY-MM-DD]
- **当前阶段**：[idea / experimenting / drafting / submitted / under review / rebuttal / revising]
- **核心 claim**：[1 句话]
- **关键 baseline**：[名字 + 引用]
- **关键数据集**：[名字]
- **协作者**：[列出，便于 agent 称呼]

## 当前 TODO（agent 帮我更新）

- [ ] ...
- [ ] ...

## 进度日志

### YYYY-MM-DD
- 完成 / 决定 / 卡点

## Agent 工作时的偏好

- 章节模板用 `knowledge/templates/`
- 绘图风格用 `knowledge/methods/figure-standards.md`
- 投稿格式按 `knowledge/venues/<target>.md`
- 引用前检查 `refs/main.bib` 是否已收录，没有就标 `[CITE: ...]`
