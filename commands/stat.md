# /stat — 统计检验 / 报告

调用 `skills/statistical-analysis/` + `knowledge/methods/statistical-testing-ml.md`。

## 流程

1. **确认场景**：
   - 比较 2 个还是 >2 个方法？
   - 配对样本（同 seed）还是独立样本？
   - 多数据集还是单数据集？
   - 样本量？分布是否近正态？

2. **选检验**（默认推荐 — 用户可覆盖）：
   - 2 方法、配对 seed：**Paired Wilcoxon signed-rank**
   - 多方法跨多数据集：**Friedman + Nemenyi**
   - 比例 / 准确率：**McNemar / two-proportion z-test**
   - 大样本近正态：**Paired t-test**

3. **必报数据**（不可省）：
   - 均值 ± 方差（std / SEM / 95% CI）
   - **n**（seed 数 / 样本数）
   - p-value + 检验名
   - 效应量（Cohen's d / 相对提升）
   - **多重比较修正**（Holm / FDR）若适用

4. **输出格式**：
   - 表格里数字：`87.3 ± 0.2`
   - 显著性：`*` p<0.05 / `**` p<0.01 / `***` p<0.001
   - Caption 注明：检验方法、修正方法、n、误差条含义

## 红线（立刻警告 Hollis）

- 只跑 1 个 seed 就报"提升 X%"
- p < 0.05 但效应量 < 0.1%
- 不做多重比较修正就跑 10 个数据集
- 用 t-test 但 n=3

## 配套代码（bootstrap 置信区间）

```python
import numpy as np
from scipy.stats import bootstrap, wilcoxon

method_a = np.array([0.871, 0.873, 0.869, 0.875, 0.872])  # 5 seeds
method_b = np.array([0.864, 0.867, 0.861, 0.868, 0.866])

# 显著性检验
stat, p = wilcoxon(method_a, method_b, alternative='greater')

# 95% CI for difference
diff = method_a - method_b
res = bootstrap((diff,), np.mean, confidence_level=0.95,
                n_resamples=10000, method='BCa')

print(f"A: {method_a.mean():.3f} ± {method_a.std():.3f}")
print(f"B: {method_b.mean():.3f} ± {method_b.std():.3f}")
print(f"Δ = {diff.mean():.3f} [95% CI: {res.confidence_interval.low:.3f}, "
      f"{res.confidence_interval.high:.3f}]")
print(f"Wilcoxon p = {p:.4f}")
```

$ARGUMENTS
