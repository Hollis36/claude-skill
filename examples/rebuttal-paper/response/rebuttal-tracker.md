# Rebuttal Tracker

## 元数据

- **Venue / Round**: NeurIPS 2026 Rebuttal Round 1
- **Deadline**: 2026-05-22 17:00 UTC（还有 5 天）
- **字数 / 页数限制**: 6 页 PDF（含图表）
- **已用**: 约 1.5 页 / 6 页

## Reviewer 汇总

| Reviewer | Conf | Rating | 主基调 | # Questions | # 已回应 | 风险 |
|---------|------|--------|-------|------------|----------|------|
| R1      | 4    | 6      | 偏正  | 3          | 0        | 中 |
| R2      | 3    | 4      | 偏负  | 5          | 2        | **高** |
| R3      | 5    | 7      | 强正  | 2          | 0        | 低 |

## 问题清单

### R1 (rating 6, "above acceptance threshold")

| ID | Question | 类型 | 状态 | 需要补 | 完成度 | 回应文件 |
|----|---------|------|------|-------|--------|---------|
| R1-Q1 | Section 3.2 router design 不清晰，特别是 score function 的设计动机 | 澄清 | TODO | 改 method §3.2 + 加 toy example | 0% | rebuttal_round1.md §R1, draft §3.2 |
| R1-Q2 | 缺与 H2O 的公平 5-seed 对比，原 H2O 论文用 3 seeds | 实验 | IN PROGRESS | 跑 run 0042（已启动） | 60% | rebuttal_round1.md §R1 |
| R1-Q3 | Limitations 太简短，没讨论 router 学习失败的边界条件 | 写作 | TODO | 扩 Limitations 段 | 0% | draft + rebuttal §R1 |

### R2 (rating 4, "marginally below threshold") — 主威胁

| ID | Question | 类型 | 状态 | 需要补 | 完成度 | 回应文件 |
|----|---------|------|------|-------|--------|---------|
| R2-Q1 | Novelty 质疑：与 H2O 的核心差异不清楚 | 论证 | TODO | 列对比表 + 重写 contribution | 10% | rebuttal_round1.md §R2 |
| R2-Q2 | 缺统计显著性，3 seeds 不够 | 实验+分析 | DONE | run 0041 (5 seeds) + Wilcoxon | 100% (95w) | rebuttal_round1.md §R2 |
| R2-Q3 | 缺 router head 数量的 ablation | 实验 | TODO | 跑 ablation: heads ∈ {1,2,4,8} | 0% | §R2 |
| R2-Q4 | "在 InfiniteBench 上不 work" — 误读，但要解释 | 论证 | TODO | 解释 + 指 Table 2 | 0% | §R2 |
| R2-Q5 | 复现性担忧，无 code | 文档 | DONE | 匿名 repo + 说明文档 | 100% (60w) | rebuttal_round1.md §R2 |

### R3 (rating 7, "good paper")

| ID | Question | 类型 | 状态 | 需要补 | 完成度 | 回应文件 |
|----|---------|------|------|-------|--------|---------|
| R3-Q1 | 建议讨论 scaling 到 70B 模型的可能性 | 讨论 | TODO | discussion 加 1 段 | 0% | rebuttal_round1.md §R3 + draft §Discussion |
| R3-Q2 | 1 个 typo（§4.2 第 3 段） | 改稿 | TODO | 直接改 | 0% | camera-ready |

## 类型分类

- **澄清**：R1-Q1（重写 method 段）
- **论证**：R2-Q1（核心 — novelty 防守）, R2-Q4
- **实验**：R1-Q2（pending）, R2-Q3
- **写作**：R1-Q3, R3-Q1
- **文档**：R2-Q5 ✅
- **改稿**：R3-Q2（trivial）

## 实验补全计划（按 P0/P1/P2 + ROI）

| Priority | 实验 | 关联 Q | 预估时间 | 状态 |
|----------|-----|--------|---------|------|
| P0 | H2O 5 seeds on LongBench/RULER | R1-Q2 | 4h | 🔄 running (0042) |
| P0 | Wilcoxon on existing data | R2-Q2 | 5 min | ✅ done |
| P0 | Router head ablation {1,2,4,8} | R2-Q3 | 8h | TODO |
| P1 | Anonymous code release | R2-Q5 | 1h | ✅ done |
| P2 | InfiniteBench 失败案例分析 | R2-Q4 | 2h（分析）| TODO |

## 字数 / 页数预算

| Section | 估字数 | 实际 | 状态 |
|---------|--------|------|------|
| 致谢 / 总览 | 50 | 47 | ✅ |
| R1 (3 Q) | 350 | 0 | 0% |
| R2 (5 Q) | 800 | 155 | 19% |
| R3 (2 Q) | 200 | 0 | 0% |
| Summary of changes | 150 | 0 | 0% |
| **合计** | **1550** | **202** | **13%** |

## 风险与依赖

- **R2 是 reject 主力**：4 分 + 3 confidence，若不能从 4 升到 5+，AC 大概率 reject
- **R2-Q1 (novelty) 是最难一关**：纯论证，必须借实验数据增强说服力
- **R1-Q2 若 H2O 反超我们**（极不可能但要预案）→ 全篇 main table 重排
- 距 deadline 5 天，每天预算：实验 4h + 写作 3h + buffer 1h
