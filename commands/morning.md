# /morning — 每日开局规划

每天 / 每次 session 开始第一件事。**不动手**，只列计划。

## 流程

1. 识别当前项目 — 用户在 `projects/<name>/` 下，或显式指明
2. 读 `projects/<name>/WORKFLOW.md` 确认操作约定
3. 读 `projects/<name>/README.md` 拿 phase、TODO、deadline
4. 读 `projects/<name>/data/run_log.md` 最近 5 条 — 看上次实验状态
5. 若 phase ∈ {rebuttal, revising}：读 `projects/<name>/response/rebuttal-tracker.md` 看完成度
6. 输出 4 段（**严格按这个结构**）：

   **A. 状态摘要**（3 行）
   - Phase / 距 deadline 还剩多少
   - 上次会话停在哪
   - 在跑 / 卡住的实验

   **B. 今日 3 件事**（编号 1-2-3，每条带预估时间）
   - 按"卡 deadline > 卡其他任务 > 高 ROI > 低 ROI"排
   - 若 rebuttal 期：优先 P0 实验 + 主力 reviewer 回应
   - 每条标记调用哪种模式（/exp / /write / 其他）

   **C. 风险预警**
   - 临近 deadline 但完成度低的项
   - 阻塞依赖（如等数据 / 等合作者 / 等实验跑完）
   - 任何 reviewer 漏回应

   **D. 等用户确认**
   - "确认这个计划？要 reorder / 加 / 删什么？"
   - 用户 OK 后再 execute 第一项

## 红线

- **不要直接 execute** — 哪怕计划再明显
- **不要瞎猜** — 文件没说的别编（如不知道 deadline 就问，不要瞎填）
- **不要堆细节** — 摘要要短，详细执行在后续会话

$ARGUMENTS
