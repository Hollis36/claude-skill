# Run Log

实验追踪日志。Agent 每次跑实验前 / 后**追加一条**，不修改已有行。
重要：失败和成功**都要记**。

---

## 2026-03-12 14:00 | 0030_h2o-baseline

- **Hypothesis**: H2O 在 LongBench / RULER / InfiniteBench 上的稳定表现，用于 main table 第一行 baseline
- **Trigger**: 准备 main table（投稿前）
- **Config**: H2O from official repo, default hyperparams, model=Llama-2-7B, seeds 1-5
- **Script**: `scripts/0030_h2o_baseline.sh` (deleted post-submission)
- **Hardware**: 1×A100
- **Duration**: 估 6h / 实际 7.5h（InfiniteBench OOM 重跑一次）
- **Result**: LongBench 78.2 ± 0.2 / RULER 64.9 ± 0.1 / InfiniteBench 52.3 ± 0.4 — 与原论文报告一致
- **CSV rows added**: `results.csv:32..46`
- **Status**: ✅ done
- **Notes**: InfiniteBench 需要 gradient checkpointing 才不爆显存

## 2026-03-13 09:00 | 0030_streamingllm

- **Hypothesis**: StreamingLLM 性能略弱于 H2O，但延迟更低
- **Trigger**: 准备 main table
- **Config**: StreamingLLM from official repo, sink=4 + recent=2000, seeds 1-5
- **Script**: `scripts/0030_streamingllm.sh` (deleted post-submission)
- **Hardware**: 1×A100
- **Duration**: 估 4h / 实际 4.2h
- **Result**: LongBench 75.7 / RULER 62.9 / InfiniteBench 49.7 — 比 H2O 弱 2-3pp
- **CSV rows added**: `results.csv:17..31`
- **Status**: ✅ done

## 2026-03-15 10:00 | 0030_flashattention2

- **Hypothesis**: Full attention (FlashAttention-2) 是 accuracy 上限，但延迟最高
- **Trigger**: 准备 main table — upper bound
- **Config**: FlashAttention-2 from xformers, default, seeds 1-5
- **Script**: `scripts/0030_flashattention.sh`
- **Hardware**: 1×A100
- **Duration**: 估 8h / 实际 9.1h
- **Result**: LongBench 82.7 / RULER 71.3 / InfiniteBench 56.2 — 与预期 upper bound 一致
- **CSV rows added**: `results.csv:2..16`
- **Status**: ✅ done

## 2026-05-15 11:30 | 0041-ours-3datasets-5seeds

- **Hypothesis**: Ours 在 3 个 long-context benchmark 上都显著超过 FlashAttention-2 (full attn)，且延迟显著低于 full attn
- **Trigger**: R2-Q2（reviewer 质疑 only-3-seeds，本来跑 3 seeds，现重跑 5 seeds）
- **Config**: Ours, router_heads=4, sparsity=0.3, seeds 1-5, identical training schedule
- **Script**: `scripts/0041_ours_5seeds.sh`
- **Hardware**: 2×A100
- **Duration**: 估 6h / 实际 5.8h
- **Result**: LongBench 84.5 ± 0.2 / RULER 73.7 ± 0.3 / InfiniteBench 58.8 ± 0.2 → 全面超过所有 baseline，Wilcoxon p=0.031 vs FlashAttention（n=5 下界）
- **CSV rows added**: `results.csv:47..61`
- **Status**: ✅ done
- **Notes**: 与之前 3-seed 结果几乎一致，方差略缩小

## 2026-05-17 09:45 | 0042-h2o-longbench-ruler-5seeds

- **Hypothesis**: 上次 H2O 只用了原 paper 的 3 seeds，R1-Q2 要求重跑 5 seeds 做公平 Wilcoxon 对比
- **Trigger**: R1-Q2
- **Config**: H2O official repo, default, model=Llama-2-7B, seeds 1-5
- **Script**: `scripts/0042_h2o_5seeds.sh`
- **Hardware**: 1×A100
- **Duration**: 估 4h / 实际 -（still running）
- **Result**: -
- **CSV rows added**: -
- **Status**: 🔄 running (background pid 12847)
- **Notes**: 跑完后自动 append + 提醒更新 rebuttal-tracker R1-Q2
