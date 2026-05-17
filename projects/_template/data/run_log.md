# Run Log

实验追踪日志。Agent 每次跑实验前 / 后**追加一条**，不修改已有行。
重要：失败和成功**都要记**，否则同样的坑会踩第二次。

## Schema

```
## YYYY-MM-DD HH:MM | run_id

- **Hypothesis**: 一句话，要测什么 / 为什么
- **Trigger**: 自发探索 / R2-Q3 / 准备 main table / debug
- **Config**: 关键超参 + git commit hash
- **Script**: `scripts/<file>.sh`
- **Hardware**: 1×A100 / 4×3090 / CPU
- **Duration**: 估 X 小时 / 实际 Y 小时
- **Result**: 数字 + 与预期对比一句话
- **CSV rows added**: `results.csv:N..M`
- **Status**: ✅ done / 🔄 running / ❌ failed / ⏸ paused
- **Notes**: 任何意外、坑、待办
```

## 示例

## 2026-05-17 09:30 | 0042-baseline-Y-d1

- **Hypothesis**: Baseline Y 在 D1 上不如 ours（如果反超，所有 claim 重写）
- **Trigger**: R1-Q2
- **Config**: Y from official repo, lr=1e-4, bs=64, seed in {1,2,3,4,5}
- **Script**: `scripts/0042_baseline_Y.sh`
- **Hardware**: 1×A100
- **Duration**: 估 4h / 实际 5h（数据加载比预期慢）
- **Result**: 81.2 ± 0.4 vs ours 87.3 ± 0.2 → 大幅落后，**符合预期** ✅
- **CSV rows added**: `results.csv:88..92`
- **Status**: ✅ done
- **Notes**: Y 在 D1 收敛慢，需要更长 schedule；这点写进 rebuttal 解释为啥不公平时不要说"他们不行"

---

## 实际运行从下面开始

(agent 按 schema 追加)
