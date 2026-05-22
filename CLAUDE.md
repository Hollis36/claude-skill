# CLAUDE.md — Agent 入口

这是 Hollis 的**科研知识库**（CS / AI 方向），不是普通 skill 集合。Agent 进入此仓库时按本文件操作。

## 用户档案

- **核心方向**：CS / AI + **机器人 / 工业自动化**（多目标优化、机器人路径规划、sim-to-real）
- **常投顶会**：
  - CS / AI：NeurIPS、ICML、ICLR、CVPR、ACL、AAAI、IJCAI、EMNLP、NAACL
  - 机器人：**ICRA、IROS、RSS、CoRL**
- **常投期刊**：
  - CS / AI：TPAMI、JMLR、Nature Machine Intelligence
  - 机器人 / 自动化：**T-ASE、T-RO、T-Mech、RA-L**（见 `knowledge/venues/`）
- **写作语言**：英文论文 + 中文沟通（默认用中文回复 Hollis，论文内容用英文）
- **工具栈**：Python（PyTorch / NumPy / matplotlib / seaborn / scipy / **MuJoCo**）、LaTeX、Git、Docker
- **机器人专项**：Franka Panda 平台、MuJoCo 3.x、多目标进化算法（NSGA-II / MOEA/D）

## 仓库布局

```
.
├── CLAUDE.md            ← 本文件，agent 第一站
├── INDEX.md             ← skill / 知识索引（按研究阶段 + 标签组织）
├── skills/              ← 25 个可执行 skill（含 9 个科研 skill）
├── knowledge/           ← 复用知识库
│   ├── methods/         ← 方法卡（消融、评估、统计、复现）
│   ├── templates/       ← 论文章节 / 回信模板
│   ├── venues/          ← 会议 / 期刊数据库
│   ├── references/      ← 文献笔记模板
│   └── glossary.md      ← 中英术语对照
├── projects/            ← 论文项目骨架
│   └── _template/       ← 新论文复制此目录起步
└── commands/            ← slash command 定义
```

## Agent 调用约定

### 任务进来时，按此顺序决策

1. **若用户在 `projects/<name>/` 下工作**：先读该项目的 `WORKFLOW.md`（项目操作手册，定义 `/morning` `/exp` `/write` 三种会话模式 + 红线 + 文件契约）。这优先于下面所有步骤。
2. **先读 `INDEX.md`** — 找到匹配当前任务的 skill 或知识条目
3. **若是论文写作**：先看 `knowledge/templates/` 是否已有对应章节模板，再看 `knowledge/venues/` 是否有目标会议的格式约束
4. **若是方法学问题**（实验设计、统计、消融）：先查 `knowledge/methods/`，再回退到对应 skill
5. **若是绘图**：直接调 `skills/scientific-plotting/`，配色和样式遵循 `knowledge/methods/figure-standards.md`（或项目内 `figures/matplotlib_settings.py`）
6. **找不到匹配**：诚实告知 Hollis，不要硬套不相关的 skill

### 项目内的工作流（重要）

当 Hollis 在 `projects/<name>/` 下工作时，agent 进入"项目模式"：

- **`/morning`**（每天开局）— 读 README + run_log + rebuttal-tracker，给 4 段输出（状态 / 今日 3 件事 / 风险 / 等确认），**不动手**
- **`/exp`**（跑实验）— 强约束落 `data/results.csv` (append-only) + `data/run_log.md`，每次预检 + 跑前确认
- **`/write`**（起草 / 改稿）— 同作者式写作，**直接写文件**，数字溯源到 results.csv，引用不编

完整规范在每个项目的 `WORKFLOW.md`（继承自 `projects/_template/WORKFLOW.md`）。

### Slash command 与自动匹配并存

- 用户**显式输入 `/paper`、`/plot`、`/review` 等**：直接执行 `commands/` 下对应文件
- 用户**描述任务（如"帮我写 intro"）**：按上面的决策流程自动挑 skill
- 两者冲突时以显式 command 为准

### 写作风格偏好

- 中文回复 Hollis 时**简洁、直接**，不堆砌客套
- 论文英文坚持 **active voice**、**short sentences**、**concrete claims**
- 禁止编造引用 — 不确定的引用标 `[CITE: 描述要找的文献]` 让 Hollis 补
- 公式优先 LaTeX，符号沿用领域惯例（参考 `knowledge/glossary.md`）

### 参考与示例

- `examples/rebuttal-paper/` 是一个**完整填好的合成示范项目**（NeurIPS rebuttal phase）。
  当 Hollis 问"这个该长什么样"或起新项目时，agent 可参照其结构。
  数据是合成的，不要当真实结果引用。

### 已知约束

- 此环境是**临时容器**（Claude Code on the web），改动要 commit + push 才保留
- 当前开发分支：`claude/research-skills-database-wUw3A`
- 仓库**不放具体论文草稿和原始数据**，只放可复用的方法和模板（`examples/` 例外，是合成示范）

## 维护原则

- 知识库**只放经验证过的、Hollis 反复用得到的东西**，宁缺毋滥
- 新增内容要在 `INDEX.md` 登记一行
- skill 的 `SKILL.md` 必须有完整 frontmatter（name / description / license）
