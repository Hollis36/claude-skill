# INDEX — Skill & 知识检索

Agent 按此索引选择资源。每行格式：`路径 | 标签 | 适用阶段 | 何时调用`

研究阶段标签：`idea` `lit-review` `design` `experiment` `analyze` `write` `figure` `revise` `submit` `rebuttal`

---

## 科研 Skill（优先级最高）

| 路径 | 标签 | 阶段 | 何时调用 |
|------|------|------|---------|
| `skills/paper/` | 论文写作 / 多学科 | write | 起草任意章节、规划论文结构 |
| `skills/review-paper-writing/` | 综述 / 文献检索 / Semantic Scholar / OpenAlex / Elicit | lit-review write | 写综述 / survey，或大规模系统性文献调研 |
| `skills/scientific-plotting/` | 绘图 / matplotlib / seaborn / SciencePlots / plotly | figure | 任何图表生成 |
| `skills/graphical-abstract/` | 图形摘要 / TOC figure | figure submit | 期刊要求 graphical abstract |
| `skills/experiment-tracking/` | 实验记录 / FAIR / wandb / mlflow | experiment analyze | 设计实验追踪方案、整理 run 数据 |
| `skills/statistical-analysis/` | 统计检验 / power analysis / APA | analyze | 显著性检验、效应量、报告统计结果 |
| `skills/reproducible-research/` | 复现 / Docker / Jupyter / pinning | experiment submit | 准备复现包、写 Reproducibility 章节 |
| `skills/code-review/` | 代码审查 / 测试 / 科研代码质量 | experiment revise | 提交 code 前自查、code release 前评审 |
| `skills/systematic-debugging/` | 4 阶段调试 / 科研代码 | experiment | 实验结果异常、训练不收敛、数值不稳定 |

## 知识库

| 路径 | 内容 | 阶段 |
|------|------|------|
| `knowledge/methods/ablation-studies.md` | 消融实验设计原则与陷阱 | design experiment |
| `knowledge/methods/evaluation-metrics.md` | CS/AI 常见指标速查（分类 / 检测 / 生成 / NLP） | analyze write |
| `knowledge/methods/statistical-testing-ml.md` | ML 论文专用统计检验（多 seed、配对、Wilcoxon） | analyze |
| `knowledge/methods/figure-standards.md` | 期刊级图表规范（DPI、字号、配色、字体） | figure |
| `knowledge/methods/reproducibility-checklist.md` | NeurIPS/ICML reproducibility checklist 对照 | submit |
| `knowledge/methods/writing-style-checks.md` | 英文写作风格红线 + 弱词黑名单 + 自动扫描 | write revise |
| `knowledge/templates/intro-hook.md` | Introduction 章节常见开篇模板 | write |
| `knowledge/templates/related-work-structure.md` | Related Work 三种组织方式 | write |
| `knowledge/templates/method-section.md` | Method 章节骨架 | write |
| `knowledge/templates/experiments-section.md` | Experiments 章节骨架与表格规范 | write |
| `knowledge/templates/limitations-broader-impact.md` | NeurIPS 要求段落模板 | write submit |
| `knowledge/templates/rebuttal.md` | Rebuttal / Response to Reviewers 模板 | rebuttal |
| `knowledge/templates/cover-letter.md` | 期刊投稿 Cover Letter 模板 | submit |
| `knowledge/venues/neurips.md` | NeurIPS 投稿信息（deadline / format / review） | submit |
| `knowledge/venues/icml.md` | ICML 投稿信息 | submit |
| `knowledge/venues/iclr.md` | ICLR 投稿信息（OpenReview） | submit |
| `knowledge/venues/cvpr.md` | CVPR 投稿信息 | submit |
| `knowledge/venues/acl-emnlp.md` | ACL / EMNLP / NAACL 投稿信息 | submit |
| `knowledge/references/_template.md` | 文献笔记模板 | lit-review |
| `knowledge/glossary.md` | CS/AI 中英术语对照 | write |

## 项目模板与示例

| 路径 | 用途 |
|------|------|
| `projects/_template/` | 新论文项目骨架（复制后改名即可起步；`/init` 命令也用它） |
| `examples/rebuttal-paper/` | 完整填好的示范项目（合成数据，演示 rebuttal 期工作流；agent 可作 few-shot 参考） |

## Slash Commands

**项目生命周期**（配合 `projects/<name>/WORKFLOW.md`）：
| 命令 | 用途 |
|------|------|
| `/init` | 起新论文项目 — 拷模板、填元数据、建 rebuttal tracker |
| `/morning` | 每日开局 — 列今日 3 件事 + 风险预警，不动手 |
| `/exp` | 跑 / 补实验，强约束落 `data/results.csv` + `run_log.md` |
| `/write` | 深参与起草 / 改稿，直接写文件 |
| `/check` | 投稿前自查 — 结构 + 英文风格 + 数字一致性 |

**领域 skill**（按任务触发）：
| 命令 | 调用的 skill / 知识 |
|------|--------------------|
| `/paper` | `skills/paper/` |
| `/review` | `skills/review-paper-writing/` |
| `/plot` | `skills/scientific-plotting/` + `knowledge/methods/figure-standards.md` |
| `/debug` | `skills/systematic-debugging/` |
| `/stat` | `skills/statistical-analysis/` + `knowledge/methods/statistical-testing-ml.md` |
| `/repro` | `skills/reproducible-research/` + `knowledge/methods/reproducibility-checklist.md` |
| `/rebuttal` | `knowledge/templates/rebuttal.md` |
| `/venue` | `knowledge/venues/` |

## 外部友邻 Skill（按场景推荐）

仓库不收编，但场景匹配时可推荐 Hollis 安装使用：

| 外部 Skill | URL | 适用场景 | 与本库关系 |
|-----------|-----|---------|-----------|
| `nature-figure`（Yuan1z0825/nature-skills） | https://github.com/Yuan1z0825/nature-skills | Nature / CNS / NMI 系投稿的 figure 设计 | 本库 `skills/scientific-plotting/` 已吸收其"语义配色、subfigure 层次、可编辑 SVG"等想法；Nature/CNS 场景两者互补 |
| `nature-polishing`（同上仓库）| 同上 | Nature 风格英文润色（≤30 词句、英式英语）| 本库 `knowledge/methods/writing-style-checks.md` 走更通用 CS/AI 风格 |

Agent 在以下场景**主动提醒**：用户提到投 Nature / Science / Cell / NMI → 建议加装 `nature-figure`；用户要 Nature 级英文润色 → 建议 `nature-polishing`。

## 其他 Skill（非科研，按需）

| 路径 | 用途 |
|------|------|
| `skills/docx/` `skills/pdf/` `skills/pptx/` `skills/xlsx/` | 文档格式处理 |
| `skills/doc-coauthoring/` | 多人协作写作 |
| `skills/mcp-builder/` | 开发 MCP server |
| `skills/web-artifacts-builder/` `skills/webapp-testing/` | Web 开发 |
| `skills/skill-creator/` | 新建 skill 的指南 |
| `skills/algorithmic-art/` `skills/brand-guidelines/` `skills/canvas-design/` `skills/frontend-design/` `skills/theme-factory/` | 设计 / 视觉 |
| `skills/internal-comms/` `skills/slack-gif-creator/` | 协作通讯 |
