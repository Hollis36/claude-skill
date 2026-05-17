# Attention Routing for Long-Context Inference

> ⚠️ **这是合成的示范项目** — 论文标题、数据、reviewer 评论都是为演示工作流编造的，不对应任何真实论文。
> Agent 第一步读 [`WORKFLOW.md`](WORKFLOW.md) — 操作手册。

## 项目元数据

```yaml
title: Attention Routing for Long-Context Inference
target_venue: NeurIPS
target_year: 2026
deadline: 2026-05-22 17:00 UTC
phase: rebuttal
core_claim: 学习一个轻量 router 决定 KV cache 哪些 token 参与 attention，长上下文推理延迟降低 30%，准确率下降 < 0.5%
core_baselines: H2O (zhang2023h2o), StreamingLLM (xiao2023streamingllm), FlashAttention-2 (dao2023flashattention2)
core_datasets: LongBench, RULER, InfiniteBench
collaborators: -
```

## 当前 TODO（最后由 agent 在 2026-05-17 morning 更新）

- [ ] **P0** 跑 Baseline H2O on LongBench + RULER (R1-Q2, 4h)
- [ ] **P0** Statistical re-eval on InfiniteBench (R2-Q2, 已有数据，跑 Wilcoxon 即可)
- [ ] **P0** 起草 §R2-Q1 novelty 论证（最难）
- [ ] **P1** Ablation: router head count (R2-Q3)
- [ ] **P2** Discussion 补 scaling 段落 (R3-Q1)
- [x] ~~跑 Ours 5 seeds × 3 datasets~~ (DONE 2026-05-15)
- [x] ~~起草 §R2-Q2 (statistical significance) → 95 词~~ (DONE 2026-05-16)

## 目录速查

| 路径 | 用途 |
|------|------|
| `WORKFLOW.md` | agent 操作手册 |
| `draft/sections/` | LaTeX 章节（已起草 intro 前半段 + method 完整 + experiments 部分） |
| `figures/figure_3_main_results.py` | 主表 figure 脚本 |
| `data/results.csv` | 60 行实验结果（4 methods × 3 datasets × 5 seeds） |
| `data/run_log.md` | 5 条 run 记录 |
| `response/rebuttal-tracker.md` | Reviewer × Question 矩阵（10 个问题，2 个已 DONE，1 个 IN PROGRESS） |
| `response/rebuttal_round1.md` | rebuttal 草稿（R2-Q2 + R2-Q5 已写） |
| `refs/main.bib` | 真实 BibTeX 条目（H2O / StreamingLLM / FlashAttention 等） |

## 进度日志

### 2026-05-15
- 跑完 Ours 5 seeds × 3 datasets（run 0041），结果稳定
- 数据 append 到 results.csv，Wilcoxon 显著（p<0.01 across all benchmarks）

### 2026-05-16
- 起草 R2-Q2（statistical significance）→ 95 词，引用 results.csv:31-45
- 更新 tracker

### 2026-05-17
- 今日 morning：列了 5 件事，砍掉 P2 后只做 P0×3 + P1×1
- 正在跑 run 0042 (Baseline H2O on LongBench)

## Agent 偏好

- 章节模板用 `knowledge/templates/`
- 绘图风格用 `figures/matplotlib_settings.py`
- 投稿格式按 `knowledge/venues/neurips.md`
- 引用前检查 `refs/main.bib`，没有就标 `[CITE: 描述]`
- 实验数字必须能溯源到 `data/results.csv` 某行
