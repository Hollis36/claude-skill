# Skills Catalog

完整 skill 列表。优先看 [`INDEX.md`](INDEX.md) — 那里按研究阶段 + 标签组织，对 agent 选择更友好。

## 分类

- [科研 Skill（优先）](#科研-skill优先)
- [设计 / 视觉](#设计--视觉)
- [文档处理](#文档处理)
- [开发 / 工具](#开发--工具)
- [协作 / 通讯](#协作--通讯)

---

## 科研 Skill（优先）

### [paper](skills/paper/SKILL.md)
**多学科学术论文写作助手** — CS/AI、生物医学、化学、物理、材料。集成 2025-2026 AI 工具（Semantic Scholar、Elicit、Research Rabbit、Scite.ai），多期刊模板（NeurIPS/ICML/Nature/IEEE/ACS/Elsevier），Rebuttal/Response Letter 指南。

**何时用**：写论文、规划结构、起草章节、回复 reviewer。

### [review-paper-writing](skills/review-paper-writing/SKILL.md)
**综述论文写作** — MCP 生物医学工具（PubMed、bioRxiv、ChEMBL、ClinicalTrials.gov）+ AI 工具（Semantic Scholar、OpenAlex、Elicit、Research Rabbit、Connected Papers、Consensus、Scite.ai）+ PRISMA 2020 + Meta-Analysis 工作流。

**何时用**：综述、survey、systematic review、meta-analysis。

### [scientific-plotting](skills/scientific-plotting/SKILL.md)
**论文级绘图** — SciencePlots v2.2.1（一行 IEEE / Nature / ACS 期刊样式）+ Plotly 3D + Plotnine + Statannotations + 多期刊格式规范。

**何时用**：所有图表生成。配套 `knowledge/methods/figure-standards.md`。

### [graphical-abstract](skills/graphical-abstract/SKILL.md)
**期刊图形摘要** — Python (matplotlib/drawsvg)、HTML/CSS/SVG、TikZ/LaTeX、Plotly+Kaleido、Figma MCP、Banana Pro MCP。2025-2026 期刊尺寸规格（PNAS、JACS、Angewandte、Advanced Materials、Lancet、PLOS ONE）。

**何时用**：期刊要求 graphical abstract / TOC figure。

### [experiment-tracking](skills/experiment-tracking/SKILL.md)
**实验追踪 + 数据管理** — wandb / mlflow / 实验日志 / FAIR 原则。

**何时用**：设计实验追踪方案、整理 run 数据。

### [statistical-analysis](skills/statistical-analysis/SKILL.md)
**统计分析 + 报告** — 显著性检验、power analysis、APA / AMA 报告规范。

**何时用**：显著性检验、效应量、报告统计结果。配套 `knowledge/methods/statistical-testing-ml.md`。

### [reproducible-research](skills/reproducible-research/SKILL.md)
**可复现工作流** — Jupyter / Docker / Poetry / 工作流自动化。

**何时用**：准备复现包、写 Reproducibility 章节。配套 `knowledge/methods/reproducibility-checklist.md`。

### [code-review](skills/code-review/SKILL.md)
**科研代码审查** — 完整测试 + 质量检查清单。

**何时用**：提交代码前自查、code release 前评审。

### [systematic-debugging](skills/systematic-debugging/SKILL.md)
**4 阶段系统化调试** — 复现 / 假设 / 定位 / 修复 + 防回归。

**何时用**：实验结果异常、训练不收敛、数值不稳定。

---

## 设计 / 视觉

### [algorithmic-art](skills/algorithmic-art/SKILL.md)
p5.js 生成式艺术，seeded randomness + 交互参数探索。

### [canvas-design](skills/canvas-design/SKILL.md)
PNG / PDF 视觉创作，海报、静态设计。

### [frontend-design](skills/frontend-design/SKILL.md)
高质量前端 UI，避免泛 AI 美学。

### [theme-factory](skills/theme-factory/SKILL.md)
10 个预设主题，可应用于 slides / docs / HTML。

### [brand-guidelines](skills/brand-guidelines/SKILL.md)
Anthropic 品牌色彩 + 字体。

---

## 文档处理

### [docx](skills/docx/SKILL.md)
Word 文档创建 / 编辑 / 分析，支持 tracked changes、批注、格式保留。

### [pdf](skills/pdf/SKILL.md)
PDF 提取文本 / 表格、创建、合并 / 拆分、表单处理。

### [pptx](skills/pptx/SKILL.md)
PowerPoint 演示文稿，layouts、speaker notes、批注。

### [xlsx](skills/xlsx/SKILL.md)
Excel 电子表格，公式、数据分析、可视化。

---

## 开发 / 工具

### [mcp-builder](skills/mcp-builder/SKILL.md)
MCP server 开发（Python FastMCP / TypeScript SDK）。

### [web-artifacts-builder](skills/web-artifacts-builder/SKILL.md)
Claude.ai HTML artifacts（React / Tailwind / shadcn）。

### [webapp-testing](skills/webapp-testing/SKILL.md)
Playwright 测试本地 web app。

### [skill-creator](skills/skill-creator/SKILL.md)
创建新 skill 的指南。

---

## 协作 / 通讯

### [doc-coauthoring](skills/doc-coauthoring/SKILL.md)
结构化协作文档写作。

### [internal-comms](skills/internal-comms/SKILL.md)
内部沟通：status report、leadership update、newsletter、FAQ、incident report。

### [slack-gif-creator](skills/slack-gif-creator/SKILL.md)
Slack 优化的动图创建。

---

## Quick Reference

| Skill | 主要语言 | 核心工具 |
|-------|---------|---------|
| paper | 中文 | LaTeX、BibTeX、Semantic Scholar、Elicit、Scite.ai |
| review-paper-writing | 中英 | Semantic Scholar、OpenAlex、Elicit、Research Rabbit、MCP Bio-Research |
| scientific-plotting | 中文 | SciencePlots、Plotly、Plotnine、Statannotations、matplotlib、seaborn、R |
| graphical-abstract | 中文 | Python、matplotlib、drawsvg、Plotly、HTML/SVG、TikZ |
| experiment-tracking | 中英 | wandb、mlflow、FAIR |
| statistical-analysis | 中英 | scipy、statsmodels、R |
| reproducible-research | 中英 | Jupyter、Docker、Poetry |
| code-review | 中英 | pytest、ruff、mypy |
| systematic-debugging | 中英 | pdb、git bisect、logging |
| algorithmic-art | English | p5.js、JavaScript |
| canvas-design | English | Design tools、Python |
| frontend-design | English | React、HTML/CSS、JavaScript |
| theme-factory | English | Color theory、CSS |
| brand-guidelines | English | Brand assets、Design systems |
| docx | English | python-docx |
| pdf | English | PyPDF2、pdfplumber |
| pptx | English | python-pptx |
| xlsx | English | openpyxl、pandas |
| mcp-builder | English | FastMCP、TypeScript |
| web-artifacts-builder | English | React、Tailwind、shadcn/ui |
| webapp-testing | English | Playwright |
| skill-creator | English | Markdown、Documentation |
| doc-coauthoring | English | Documentation workflows |
| internal-comms | English | Corporate communications |
| slack-gif-creator | English | GIF optimization |

---

## License

各 skill 看自己的 `LICENSE.txt`。总览见 [`LICENSE.md`](LICENSE.md)。

---

## Navigation

- [README](README.md)
- [INDEX](INDEX.md) — 按阶段 / 标签
- [QUICKSTART](QUICKSTART.md)
- [CONTRIBUTING](CONTRIBUTING.md)
