# Hollis 的科研知识库

> 给 agent 用的、面向 CS / AI 论文写作的私人知识库 + 可复用 skill 集。
>
> **不是**通用 skill 商店 — 这是一个为单一研究者优化的工作台。

[English](#english) | [中文](#中文)

---

## 中文

### 入口

Agent 进入此仓库后**第一步读 `CLAUDE.md`**，第二步看 `INDEX.md` 选 skill / 知识条目。

### 目录

```
.
├── CLAUDE.md            ← agent 入口（研究方向、调用约定、写作偏好）
├── INDEX.md             ← skill / 知识索引（按研究阶段 + 标签）
├── skills/              ← 25 个 skill，含 9 个科研 skill
│   ├── paper/                    多学科论文写作
│   ├── review-paper-writing/     综述 + AI 文献工具
│   ├── scientific-plotting/      论文级绘图
│   ├── graphical-abstract/       期刊图形摘要
│   ├── experiment-tracking/      实验 + FAIR 数据
│   ├── statistical-analysis/     统计检验
│   ├── reproducible-research/    复现 / Docker
│   ├── code-review/              科研代码审查
│   ├── systematic-debugging/     4 阶段调试
│   └── ... (15 个通用 skill)
├── knowledge/           ← 可复用知识库（核心新增）
│   ├── methods/         ← 方法卡（消融、评估、统计、图表、复现）
│   ├── templates/       ← 论文章节 + Rebuttal + Cover Letter 模板
│   ├── venues/          ← NeurIPS / ICML / ICLR / CVPR / ACL 投稿数据
│   ├── references/      ← 文献笔记模板
│   └── glossary.md      ← CS/AI 中英术语对照
├── projects/            ← 论文项目（.gitignore 默认排除）
│   └── _template/       ← 复制此目录起步新论文
└── commands/            ← slash command 定义
    ├── paper.md   /paper
    ├── review.md  /review
    ├── plot.md    /plot
    ├── debug.md   /debug
    ├── stat.md    /stat
    ├── repro.md   /repro
    ├── rebuttal.md /rebuttal
    └── venue.md   /venue
```

### 三层架构

| 层 | 是什么 | 例子 |
|----|-------|------|
| **Skill 层**（`skills/`） | 可执行工作流 | "怎么从头写一篇综述" |
| **知识层**（`knowledge/`） | 静态参考资料 | "NeurIPS 的 deadline / 格式 / checklist" |
| **项目层**（`projects/`） | 具体论文 | 我正在写的 paper 草稿 + 数据 + 图 |

Skill 告诉 agent **怎么做**，知识告诉 agent **依据什么做**，项目告诉 agent **对哪个工作做**。

### Agent 调用约定

- **显式 slash command**（`/paper`、`/plot` 等）→ 直接执行
- **描述任务**（"帮我写 intro"）→ agent 按 `INDEX.md` 自动挑 skill
- **找不到匹配** → 诚实告知 Hollis，不硬套

### 起步使用

1. **写论文**：先选目标会议，让 agent 读 `knowledge/venues/<venue>.md` + `knowledge/templates/` 起草
2. **画图**：`/plot` 自动应用 `figure-standards.md` 规范
3. **跑实验**：`skills/experiment-tracking/` 设计追踪方案
4. **rebuttal**：`/rebuttal` 拉模板逐条回应

### 维护原则

- 知识只放**反复用得到的**，宁缺毋滥
- 新增内容**必须**在 `INDEX.md` 登记
- skill 的 `SKILL.md` 必须有完整 frontmatter
- 隐私 / 论文草稿走 `projects/`，自动 gitignore

### 相关文档

- [`QUICKSTART.md`](QUICKSTART.md) — 5 分钟上手
- [`SKILLS_CATALOG.md`](SKILLS_CATALOG.md) — 所有 skill 详细说明
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — 新增 skill 规范
- [`LICENSE.md`](LICENSE.md) — 许可证

---

## English

A personal research knowledge base + reusable skills, designed for **a single CS/AI researcher** (Hollis) to use with their agent for paper writing.

### Entry

Agent reads `CLAUDE.md` first, then `INDEX.md` to pick the right skill or knowledge entry.

### Three-layer architecture

| Layer | What | Example |
|-------|------|---------|
| **Skills** (`skills/`) | Executable workflows | "How to write a survey from scratch" |
| **Knowledge** (`knowledge/`) | Static reference | "NeurIPS deadline / format / checklist" |
| **Projects** (`projects/`) | Specific papers | The paper I'm currently writing |

### Layout

```
.
├── CLAUDE.md            # agent entry: researcher profile, conventions, style
├── INDEX.md             # skill / knowledge index by stage + tag
├── skills/              # 25 skills, 9 research-focused
├── knowledge/           # reusable knowledge base
│   ├── methods/         # method cards (ablation, eval, stats, figures, repro)
│   ├── templates/       # section templates, rebuttal, cover letter
│   ├── venues/          # NeurIPS/ICML/ICLR/CVPR/ACL submission data
│   ├── references/      # literature note template
│   └── glossary.md      # CS/AI Chinese-English glossary
├── projects/            # paper projects (gitignored except _template/)
└── commands/            # slash command definitions
```

### Slash commands

| Command | Purpose |
|---------|---------|
| `/paper` | Draft paper sections, overall planning |
| `/review` | Survey / review paper writing |
| `/plot` | Journal-quality figures with enforced standards |
| `/debug` | 4-phase systematic debugging |
| `/stat` | Statistical testing & reporting |
| `/repro` | Reproducibility check (NeurIPS/ICML checklist) |
| `/rebuttal` | Rebuttal / Response to reviewers |
| `/venue` | Conference / journal submission info |

### License

Mixed — see `LICENSE.md`. Individual skills may have their own `LICENSE.txt`.
