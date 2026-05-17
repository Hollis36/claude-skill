# /init — 初始化新论文项目

从 `projects/_template/` 拷贝出一个新论文目录，填好元数据，让 agent 立刻能进入项目模式。

## 用户必须给的 4 件事

如果用户没说全，**一次问完**（不要逐条问）：
1. **关键词命名**（slug）— 用于目录名，例如 `attention-routing` / `efficient-rag`。避免真实论文标题（怕被偷看）
2. **目标 venue + year** — 决定模板格式、deadline 参考
3. **当前 phase** — `idea` / `experimenting` / `drafting` / `under-review` / `rebuttal` / `revising`
4. **核心 claim 一句话** — 写进 README 元数据，agent 后续起草时参考

可选：deadline、reviewer 数量（若 rebuttal phase）、合作者。

## Agent 流程

### Step 1：检查冲突
```bash
test -d projects/<slug> && echo "exists, abort"
```
若已存在，**问用户**：覆盖 / 起新名 / 取消？不要默默覆盖。

### Step 2：拷贝模板
```bash
cp -r projects/_template projects/<slug>
```

### Step 3：填 `projects/<slug>/README.md` 元数据
替换 YAML-like 元数据块中的占位符为用户给的值。**不要保留 `[Tentative title]` 这种占位符**，至少填关键字段。

### Step 4：若 phase = rebuttal / revising
- 提示用户："你有 reviewer 数量和大致基调吗？我直接帮你建好 `response/rebuttal-tracker.md` 的行"
- 用户给 → 填 tracker 的 Reviewer 汇总表 + 各 reviewer 的 Q 行（初始 status 全 TODO，完成度 0%）
- 用户没给 → 保留模板原样

### Step 5：若 venue 有 deadline
- 读 `knowledge/venues/<venue>.md`
- 若知识库有该 venue 的典型 deadline → 提醒用户确认实际年份的 deadline（年度可能变）
- 知识库没有 → 提醒用户自己查官网，标 `[TODO: 确认 deadline]`

### Step 6：报告
告诉用户：
- 项目目录路径
- 已填充的元数据字段
- 待填充的字段（`[TODO: ...]` 列表）
- 建议下一步：`/morning` 跑一次看 agent 输出 / 或先填完元数据

## 红线

1. **不许覆盖已有目录** — 必须先问
2. **不许编 deadline** — 不确定就标 `[TODO: 确认]`
3. **不许跳过 README 填充** — 否则后续 agent 进项目模式没法工作
4. **不要 commit** — 让用户审完再 commit；用户说 commit 才 commit
5. **不要把元数据写入主仓库公开部分** — `projects/<slug>/` 默认被 `.gitignore` 屏蔽（除 `_template`）

## 示例（用户输入完整信息）

**用户**：
```
/init slug=attention-routing venue=NeurIPS 2026 phase=rebuttal
claim: 我们提出 attention routing，在 long-context 任务上比 SOTA 减少 30% latency 同时保持精度
deadline: 2026-05-22 17:00 UTC
reviewers: R1 偏正 (rating 6), R2 偏负 (rating 4), R3 强正 (rating 7)
```

**Agent**：
1. 检查 `projects/attention-routing/` 不存在 ✅
2. `cp -r projects/_template projects/attention-routing`
3. 编辑 README：填 title=Attention Routing for Long-Context、target_venue=NeurIPS、target_year=2026、deadline=2026-05-22 17:00 UTC、phase=rebuttal、core_claim=...
4. 编辑 rebuttal-tracker：填 R1/R2/R3 三行汇总（rating + 风险等级），各 reviewer Q 区段留模板占位
5. 输出：

   ```
   Created projects/attention-routing/ from template.
   Filled: title, venue, year, deadline, phase, claim, reviewer summary
   TODO (you): reviewer questions (R1×3, R2×5, R3×2 见你 review)
                core_baselines, core_datasets

   下一步：
   - 把每个 reviewer 的具体 question 粘进 rebuttal-tracker.md，我帮你按类型分类
   - 或先 /morning 看 agent 当前能给出什么计划（reviewer Q 没填的话会催你填）
   ```

$ARGUMENTS
