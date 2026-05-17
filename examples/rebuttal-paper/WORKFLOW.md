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

---

## Worked Examples（rebuttal / revision 场景）

下面三个完整会话演示，agent 出 prompt 时直接对照。

### 示例 1：`/morning` 一次完整执行

**用户输入**：
```
/morning
```

**Agent 行动**（先读文件，**不动手**）：
- 读 `README.md` → phase=rebuttal, deadline 2026-05-22 17:00 UTC（还有 5 天）
- 读 `data/run_log.md` → 最近一次 `0041-ours-d3-5seeds`，✅ 已完成，结果符合预期
- 读 `response/rebuttal-tracker.md` → R2 是主力批评者，5 个 Q，0% 完成；P0 实验有 2 个未开始

**Agent 输出**（严格 4 段）：

```
A. 状态摘要
- Phase: rebuttal | Deadline: 2026-05-22 17:00 UTC (剩 5 天 8 小时)
- 上次会话：跑完 0041-ours-d3-5seeds，R2-Q2 (统计显著性) 数据齐了，但还没写
- 在跑：无；卡住：无；待跑：Baseline Y (R1-Q2)、Ablation Z (R2-Q3)

B. 今日 3 件事
1. [120 min] /exp 跑 Baseline Y on D1+D2 (5 seeds) — 解 R1-Q2，P0
2. [45 min]  /write response §R2-Q2 — 数据已有，用 templates/rebuttal.md 显著性模板
3. [60 min]  /exp 启动 Ablation Z（后台跑，明天看结果）— 解 R2-Q3，P0

C. 风险预警
- R2 5 个问题里 P0 占 2 个，今天必须开两个
- R1-Q2 (Baseline Y) 若反超我们 → 全篇 claim 要调，提前 ping 合作者预警
- 距 deadline 仅 5 天，写作时间预算 = 总时间 - 实验时间，建议每天封顶 4 小时实验

D. 确认这个计划？要 reorder / 加 / 删什么？
```

用户回："OK，但今天我只有半天，去掉第 3 项" → agent 调整后开始执行第 1 项。

---

### 示例 2：`/exp` 跑 Baseline Y

**用户输入**：
```
/exp baseline Y on D1+D2

背景：R1-Q2，reviewer 说我们没和 Y 对比。Y 是 NeurIPS 2024 SOTA。
配置：Y from official repo (github.com/X/Y), 默认超参; seeds 1-5; D1=ImageNet, D2=COCO
预期：Y 应弱于 ours 但不会差太多（5-10% gap）。若反超 = 灾难。
```

**Agent 行动**：

1. **预检**：
   - `git status` 干净？✅
   - 搜 `run_log.md` 有无相似 run → 无
2. **建 run_id**：上次是 0041 → 用 `0042-baseline-Y-d1d2`
3. **写入 run_log.md**（status: 🔄 running）
4. **生成脚本** `scripts/0042_baseline_Y.sh`：
   ```bash
   #!/usr/bin/env bash
   set -euo pipefail
   for dataset in D1 D2; do
     for seed in 1 2 3 4 5; do
       python -m baseline_Y.train --dataset "$dataset" --seed "$seed" \
         --output "data/runs/0042/${dataset}_seed${seed}.json"
     done
   done
   python scripts/append_to_results.py --run-id 0042 \
     --glob "data/runs/0042/*.json" --method "Baseline Y"
   ```
5. **跑前确认**：

   ```
   将运行：bash scripts/0042_baseline_Y.sh
   预计：~4 小时（10 个 train run, 单 A100 ~25 min/run）
   输出：data/runs/0042/*.json → 汇总到 data/results.csv
   建议后台跑（run_in_background=True）
   Go?
   ```
6. 用户 "go" → 后台启动
7. **跑完**：
   - Append 10 行到 `data/results.csv`（schema 一致）
   - 更新 `run_log.md`：
     ```
     - Status: ✅ done
     - Duration: 估 4h / 实际 4.2h
     - Result: Y on D1 = 82.1±0.4, on D2 = 75.3±0.5 → 落后 ours 5.2pp / 4.9pp，符合预期 ✅
     - CSV rows added: results.csv:93..102
     ```
   - **提醒**：
     ```
     R2-Q2 (Baseline Y) 数据齐了，建议下一步：
     → /write response §R1-Q2  (用新数字)
     → 或 rebuild figure_3_main_results 把 Y 加进对比图
     ```

---

### 示例 3：`/write` 起草 rebuttal R2-Q2

**用户输入**：
```
/write response/rebuttal_round1.md §R2-Q2

要点：R2 质疑我们没报统计显著性。我们重跑了 5 seeds + Wilcoxon 都显著 (p<0.01)。
约束：NeurIPS rebuttal，整体 6 页限，本节预算 200 词。
依据：data/results.csv 行 88-92 (ours 5 seeds), 行 50-54 (best baseline 5 seeds)
```

**Agent 行动**：

1. **加载上下文**：
   - 读 `knowledge/templates/rebuttal.md` → 找 "Concerns about statistical significance" 模板
   - 读 `knowledge/venues/neurips.md` → 确认 6 页 PDF / 字号 / 引用格式
   - 读 `data/results.csv:88-92` 和 `:50-54` → 算 mean ± std + 跑 Wilcoxon
2. **直接起草**（写入 `response/rebuttal_round1.md` §R2-Q2，不只在 chat 贴）：

   ```markdown
   **[R2-Q2] Statistical significance.** We re-ran main experiments with 5 random seeds
   (previously 3). Improvements remain significant: on D1, $\{Ours\}$ achieves
   $87.3 \pm 0.2$ vs $\{Strongest Baseline\}$ $84.7 \pm 0.2$ ($p = 0.008$, paired
   Wilcoxon signed-rank, one-sided, Holm-corrected). On D2, $80.4 \pm 0.3$ vs
   $77.9 \pm 0.4$ ($p = 0.012$). We have updated Table 1 with mean ± std and
   significance annotations. The full 5-seed results are also released in our
   anonymous code repository for verification.
   ```
3. **自查清单**：
   - [x] active voice
   - [x] 数字与 results.csv 一致（手算 mean 验证）
   - [x] 无 "good"、"extensive"、"significantly"（除非配 p-value）
   - [x] ~95 词，远低于 200 预算 ✅
   - [x] 引用：本段无新文献
4. **写完更新 tracker**：

   ```diff
   - | R2-Q2 | 缺统计显著性 | 实验+分析 | TODO | 重跑 + Wilcoxon | 0% | rebuttal §R2 |
   + | R2-Q2 | 缺统计显著性 | 实验+分析 | DONE | ✓ | 100% (95w) | rebuttal §R2 |
   ```
5. **报告给用户**：

   ```
   写入了 response/rebuttal_round1.md §R2-Q2 (95 词)
   更新了 rebuttal-tracker.md R2-Q2 行
   还差：R2-Q1 / Q3 / Q4 / Q5；Table 1 需要重生成带显著性标注
   要现在 /plot figure_3 加显著性？还是先 /write R2-Q1？
   ```

---

## FAQ / 棘手情况

| 情况 | 处理 |
|------|------|
| 用户给的数字 chat 里说的，和 results.csv 不符 | 以 results.csv 为准，问用户哪个对 |
| 用户想跑实验但脏 working tree | 警告 + 建议先 commit 或 stash |
| 实验跑了一半失败 | 在 run_log 记 `❌ failed`，写 root cause，**不**自动重跑 |
| Rebuttal 字数超了 | **立即砍**，找冗余句删，不要 "稍微超出一点" |
| 用户问"这个改完能不能直接 push" | 不要自动 push，列改动 → 等用户说 push |
| 用户在 chat 里粘了 reviewer 评论但没说哪个 reviewer | 问 reviewer 编号，不要猜 |
| 同一个数字在 paper 多处出现 | grep 全文，一起改，不要漏
