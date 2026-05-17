# Rebuttal Tracker

Reviewer × Question 矩阵。Agent 进入 rebuttal 模式时**先读这个**。

## 元数据

- **Venue / Round**: [NeurIPS 2025 Rebuttal Round 1]
- **Deadline**: [YYYY-MM-DD HH:MM TZ]
- **字数 / 页数限制**: [6 页 PDF / 5000 字符 / 1 页 / ...]
- **已用**: [X 字 / Y 页]

## Reviewer 汇总

| Reviewer | Conf | Rating | 主基调 | # Questions | # 已回应 | 风险 |
|---------|------|--------|-------|------------|----------|------|
| R1      | 4    | 6      | 偏正  | 3          | 0        | 低 |
| R2      | 3    | 4      | 偏负  | 5          | 0        | **高** |
| R3      | 5    | 7      | 强正  | 2          | 0        | 低 |

## 问题清单（按 reviewer × question）

### R1

| ID | Question (一句话) | 类型 | 状态 | 需要补 | 完成度 | 回应文件 |
|----|------------------|------|------|-------|--------|---------|
| R1-Q1 | Method 中 X 步骤不清晰 | 澄清 | TODO | 改 method | 0% | rebuttal_round1.md §R1 |
| R1-Q2 | 与 baseline Y 对比缺失 | 实验 | TODO | 跑 baseline Y | 0% | rebuttal_round1.md §R1 |
| R1-Q3 | Limitations 不够 | 写作 | TODO | 扩 limitations | 0% | draft + rebuttal §R1 |

### R2

| ID | Question | 类型 | 状态 | 需要补 | 完成度 | 回应文件 |
|----|---------|------|------|-------|--------|---------|
| R2-Q1 | Novelty 质疑 | 论证 | TODO | 列对比表 | 0% | rebuttal_round1.md §R2 |
| R2-Q2 | 缺统计显著性 | 实验+分析 | TODO | 重跑 + Wilcoxon | 0% | §R2 + 改 §4.2 |
| R2-Q3 | 缺 ablation Z | 实验 | TODO | 跑 ablation Z | 0% | §R2 + 改 §4.3 |
| R2-Q4 | "不 work on dataset D2" | 论证+实验 | TODO | 解释 + 1 个补救实验 | 0% | §R2 |
| R2-Q5 | 复现性担忧 | 文档 | TODO | 匿名 repo | 0% | §R2 |

### R3

| ID | Question | 类型 | 状态 | 需要补 | 完成度 | 回应文件 |
|----|---------|------|------|-------|--------|---------|
| R3-Q1 | typo / 小问题 | 改稿 | TODO | 直接改 | 0% | camera-ready |
| R3-Q2 | 建议方向延伸 | 讨论 | TODO | 1 段补充 discussion | 0% | §R3 |

## 类型分类

- **澄清** (Clarification) — 重写 method 段落 / 加图 / 加例子
- **论证** (Argument) — 列对比、强化 contribution claim、引相关工作
- **实验** (Experiment) — 补 baseline / ablation / 新数据集
- **写作** (Writing) — 扩 limitations / discussion / typo
- **文档** (Documentation) — 复现、code release

## 实验补全计划

按"高 ROI / 低成本"排：

| Priority | 实验 | 关联 questions | 预估时间 | 状态 |
|----------|-----|----------------|---------|------|
| P0 | Baseline Y on D1, D2 | R1-Q2 | 4h | TODO |
| P0 | Statistical re-eval (5 seeds + Wilcoxon) | R2-Q2 | 6h | TODO |
| P1 | Ablation Z | R2-Q3 | 3h | TODO |
| P2 | Mitigation for D2 | R2-Q4 | 6h | TODO（看时间）|

## 字数 / 页数预算

| Section | 估字数 | 实际 |
|---------|--------|------|
| 致谢 / 总览 | 50 | - |
| R1 (3 Q) | 400 | - |
| R2 (5 Q) | 800 | - |
| R3 (2 Q) | 200 | - |
| Summary of changes | 150 | - |
| **合计** | **1600 / 限制** | - |

## 风险与依赖

- **R2 是 reject 主力**，所有 P0 实验必须能 work
- 若 Baseline Y 在 D1 上反超我们 → 全面调整 claim，找 AC
- Statistical re-eval 若改变显著性结论 → 整篇 main result 都要更新

## Agent 工作流提示

每次 rebuttal session，agent 应：
1. 先扫此表，告诉我哪些 P0 还没动
2. 写 response 前，确认对应行的"完成度"为 80%+
3. 写完一段后，更新对应行的"完成度"和"实际字数"
4. 任何被引用的新数字，必须在 `data/results.csv` 能找到
