# WORKFLOW.md — 给 agent 用的项目操作手册

Agent 进入此项目时**第一站**。每天 / 每个会话开始读本文件 + `README.md`。

## 项目状态机

任何论文项目在以下 5 个 phase 之一：

| Phase | 标志 | 主要会话模式 |
|-------|------|------------|
| `idea` | 没数据、没代码 | brainstorm + lit-review |
| `experimenting` | 在跑实验 | experiment-loop |
| `drafting` | 实验差不多了 | writing |
| `under-review` / `rebuttal` | 投了等回复 / 拿到 review | **rebuttal-mode** |
| `revising` | 走 major revision | writing + experiment |

当前 phase 写在 `README.md` 元数据里。Agent 进来先确认。

---

## 三种会话模式 — 标准开场 prompt

### 模式 A：Morning Planning（每天开始 5 分钟）

**用户输入**：
```
/morning
```

**Agent 应执行**：
1. 读 `README.md` 拿当前 phase、TODO、截止日期
2. 读 `data/run_log.md` 看昨天 / 上次实验状态
3. 若 phase = rebuttal / revising：读 `response/rebuttal-tracker.md` 看 reviewer × question 完成度
4. 输出：
   - **今日 3 件事**（按紧迫度，**给出预估时间**）
   - **昨天 / 上次的延续点**（不要让任务断片）
   - **风险预警**（卡住的实验、临近的 deadline、漏回应的 reviewer）
5. **不动手**。等用户确认后再 execute。

### 模式 B：Experiment Session（补 / 跑实验）

**用户输入**：
```
/exp <一句话假设>

背景：[一两句上下文，如哪条 reviewer comment 触发的]
配置：[关键超参 / 数据集 / baseline]
预期：[一句话假设 → 这个实验该看到什么结果]
```

**Agent 应执行**：
1. 在 `data/run_log.md` 追加一行（用日期 + run_id）
2. 若已有相似 run，警告并问是否复用
3. 生成 / 修改 `scripts/<run_id>.sh`
4. 跑前列出"运行什么 / 输出在哪 / 预计多久"
5. 跑完把结果**按 schema 写入** `data/results.csv`
6. 与预期对比，给一句话结论
7. 若结果触发新 review 回应，提醒 update `response/rebuttal-tracker.md`

### 模式 C：Writing Session（深参与起草 / 改）

**用户输入**：
```
/write <章节或回应位置>

要点：[要表达什么 — 核心论点 1-3 句]
约束：[字数 / 风格 / 必须引用的文献]
依据：[支持数字 / 参考模板]
```

**Agent 应执行**：
1. 读对应模板（`knowledge/templates/<corresponding>.md`）
2. 读 venue 约束（`knowledge/venues/<target>.md`）
3. 起草 — 直接给完整段落，不分步问"你想要什么风格"
4. **引用全标 `[CITE: ...]`**，不要编 BibTeX key
5. 起草后**自查清单**：
   - [ ] active voice
   - [ ] short sentences (avg ≤ 25 words)
   - [ ] concrete claims（无 "good"、"extensive"、"various"）
   - [ ] 数字与 `data/results.csv` 一致
6. 把改动写进对应文件，**不只在 chat 里贴**

---

## Agent 红线（任何模式都不许做）

1. **不许编引用** — BibTeX key 必须在 `refs/main.bib` 真实存在
2. **不许编实验数字** — 数字必须能溯源到 `data/results.csv` 某行
3. **不许动 `data/results.csv` 已有行** — 只能 append 新 run
4. **不许 git push** — 除非用户显式说 "push"
5. **不许跨 venue 改格式** — paper 已经定 venue，按 `knowledge/venues/<target>.md` 约束
6. **不确定就标 `[TODO: 描述]`**，绝不"看起来合理就填"

---

## 文件契约

| 文件 | 谁写 | 怎么写 |
|------|------|--------|
| `README.md` | 用户主写，agent 辅助更新 status / TODO | YAML-like 元数据顶部 |
| `data/run_log.md` | agent 写，用户读 | 每次实验追加 1 行 |
| `data/results.csv` | agent append，用户审计 | 固定 schema（见 `data/README.md`） |
| `draft/sections/*.tex` | agent 起草 → 用户改 → agent 同作者式润色 | LaTeX，`[CITE: ...]` 占位 |
| `figures/figure_*.py` | agent 写脚本 → 用户调参数 | import `matplotlib_settings` |
| `figures/figure_*.pdf` | agent 由脚本生成 | 不直接编辑 |
| `response/rebuttal-tracker.md` | agent + 用户共同维护 | Reviewer × Question 矩阵 |
| `response/rebuttal_round*.md` | agent 起草 → 用户改 → 用户提交 | 按 venue 字数限制 |
| `refs/main.bib` | 用户主写，agent 提建议 | BibTeX，避免重复 key |

---

## 一天典型循环

```
Morning:    /morning             → 列今日 3 件事
Mid-morning: /exp Q3 baseline X  → 跑实验 30min
Lunch:      [实验跑着，agent 写 rebuttal Q1] /write response Q1
Afternoon:  /exp Q5 ablation     → 跑实验
            /write response Q3 (用 Q3 新数字)
            /plot figure_4_ablation (新结果)
Evening:    /morning（明日预演） → agent 更新 README TODO，commit
```

---

## 当 Hollis 问"这个怎么办"时

Agent 决策树：
1. 是论文写作？→ 模式 C
2. 是实验 / 数据？→ 模式 B
3. 是流程 / 优先级？→ 模式 A
4. 是知识问题（统计、消融、venue）？→ 直接查 `knowledge/`，不进任何模式
5. 都不是？→ 问 Hollis 澄清，不硬塞模式
