# ML 论文的统计检验

ML 论文常被批评"没有统计严谨性"，但又不能照搬医学统计。本文给 CS/AI 场景的最小可用方案。

## 第一原则：报告分布而非点估计

最低要求：**每个数字至少 3 个独立 seed，报 mean ± std**。
更好：5–10 个 seed，外加 95% bootstrap CI。
只跑 1 个 seed 就报"提升 0.3%" — 审稿人一行 reject。

## 选检验

| 场景 | 推荐检验 | 备注 |
|------|---------|------|
| 同数据集上 method A vs B 多 seed | **Paired Wilcoxon signed-rank** | 不假设正态，配对处理 seed 配对 |
| 多数据集上 A vs B | **Wilcoxon signed-rank**（每个数据集一对值） | Demšar 2006 标准做法 |
| 多算法对比（>2） | **Friedman + Nemenyi post-hoc** | Demšar 2006；画 critical difference 图 |
| 大样本、近正态 | Paired t-test | 检查正态性 |
| 比例 / 准确率（n 大） | Two-proportion z-test 或 McNemar | McNemar 处理配对 |
| 排名比较 | Mann-Whitney U | 不要求正态 |

**不要做的事**：
- 用 t-test 但样本只有 3 — 检验本身没意义，直接报均值和方差
- p-hacking — 跑十个 seed 选最好的三个报
- 只报 p-value 不报效应量（提升 0.1% 即使显著也无意义）

## 效应量

p-value 说"差异不是随机"，效应量说"差异有多大"。两个都要。

| 指标 | 计算 | 解读 |
|------|------|------|
| **Cohen's d** | $(\mu_1 - \mu_2) / \sigma_{pooled}$ | 0.2 小 / 0.5 中 / 0.8 大 |
| **相对提升 %** | $(m_1 - m_2) / m_2 \times 100$ | 论文里最常见 |
| **绝对提升** | $m_1 - m_2$ | 接近天花板时更诚实 |

## 多重比较修正

跑 10 个数据集 × 5 个 baseline 就是 50 次检验，随便都能"显著"。
- **Bonferroni**：保守，$\alpha / n$
- **Holm-Bonferroni**：略宽松，逐步比较，推荐
- **Benjamini-Hochberg (FDR)**：控制假阳性比例，大规模比较用

## 置信区间（bootstrap）

```python
import numpy as np
from scipy.stats import bootstrap

scores = np.array([0.872, 0.869, 0.875, 0.871, 0.873])  # 5 个 seed
res = bootstrap((scores,), np.mean, confidence_level=0.95,
                n_resamples=10000, method='BCa')
print(f"{scores.mean():.3f} [{res.confidence_interval.low:.3f}, "
      f"{res.confidence_interval.high:.3f}]")
```

## LLM 评估的特殊处理

- **Win rate** 需要二项检验置信区间（Wilson interval）
- **LLM-as-judge**：报告判官 inter-judge agreement（kappa）；与人类评分相关性
- **Position bias**：交换答案位置重测一半

## 报告模板

> We report mean ± standard deviation over 5 random seeds.
> Statistical significance is assessed via the paired Wilcoxon signed-rank test (one-sided, $\alpha = 0.05$).
> When comparing across multiple datasets, we apply Holm-Bonferroni correction.
> 95% confidence intervals are computed via BCa bootstrap with $10^4$ resamples.
> Effect sizes are reported as relative improvement over the strongest baseline.

## 推荐参考文献（让 agent 替你引用时检索）

- Demšar (2006). *Statistical Comparisons of Classifiers over Multiple Data Sets*. JMLR.
- Dror et al. (2018). *The Hitchhiker's Guide to Testing Statistical Significance in NLP*. ACL.
- Bouthillier et al. (2021). *Accounting for Variance in Machine Learning Benchmarks*. MLSys.
