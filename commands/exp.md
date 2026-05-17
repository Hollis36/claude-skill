# /exp — 跑 / 补实验

科研代码的实验会话。**强约束**：所有结果落 `data/results.csv`，每次执行追加 `data/run_log.md`。

## 用户必须给的 3 件事

如果用户没说全，先问：
- **假设**（Hypothesis）— 一句话：测什么、预期看到什么
- **配置**（Config）— 关键超参 + dataset + seed 范围
- **触发**（Trigger）— 自发探索 / 回应 R2-Q3 / 准备 main table / debug

## Agent 流程

### Step 0：预检
1. 当前 git 是否干净？不干净警告（不要在脏 working tree 上跑实验）
2. `data/run_log.md` 里搜过去 30 天有没有相似 run（同配置 + 同 hypothesis）
3. 有相似 run → 提示用户："已有 run #XXXX，你确定要重跑而非复用？"

### Step 1：建 run_id
- 格式：`{编号}-{hypothesis_slug}`，例如 `0042-baseline-Y-d1`
- 编号取 `run_log.md` 最大 + 1
- 写入 `data/run_log.md`（status: `🔄 running`）

### Step 2：生成 / 修改脚本
- 在 `scripts/<run_id>.sh` 写
- 必含：
  - `set -euo pipefail`
  - 输出路径明确（不要散落）
  - 多 seed 用 for 循环
  - 末尾 append 到 `data/results.csv`（schema 见 `data/README.md`）

### Step 3：跑前确认
告诉用户：
- 运行什么命令
- 预计 X 小时
- 输出去哪
- 是否要后台跑（长任务）

**等用户 go**。除非用户明示"直接跑"。

### Step 4：跑（用 run_in_background 若 > 5 分钟）

### Step 5：收尾
1. 把结果按 schema **append** 到 `data/results.csv`（不改已有行）
2. 更新 `data/run_log.md`：
   - status 改 ✅ done / ❌ failed
   - 填实际时长、结果一句话、与预期对比
   - CSV rows added
3. 若结果回应了某个 review 点 → 提醒用户更新 `response/rebuttal-tracker.md`
4. 若结果触发 main table 改动 → 提醒重跑 `scripts/rebuild_all_figures.sh`

## 红线

1. **不许改 `data/results.csv` 已有行** — 只能 append
2. **不许编实验数字** — 没跑的就说没跑
3. **失败也要记** — `run_log.md` 中 status 改 ❌，写明 root cause（哪怕只一句）
4. **不许跳 Step 3** — 用户必须知道命令再决定 go/no-go

$ARGUMENTS
