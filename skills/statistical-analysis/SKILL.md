---
name: statistical-analysis
description: |
  统计分析与报告助手，帮助科研人员进行正确的统计检验和结果报告。支持Python (scipy/statsmodels/pingouin)和R统计分析、功效分析和样本量计算、APA/AMA统计报告规范、常见统计陷阱避免(p-hacking/多重比较)。当用户需要：(1) 选择合适的统计检验方法、(2) 进行数据统计分析、(3) 计算样本量和功效、(4) 按规范报告统计结果时触发。关键词：统计检验、t检验、ANOVA、回归分析、样本量计算、统计报告。
license: Apache-2.0
---

# 统计分析与报告助手

帮助科研人员选择合适的统计方法、正确进行分析、避免常见陷阱、规范报告结果。

## 核心功能

### 1. 统计方法选择指南
### 2. Python 和 R 统计分析工作流
### 3. 功效分析和样本量计算
### 4. 统计报告规范（APA/AMA）
### 5. 常见统计陷阱避免

## 统计方法选择流程图

```
开始
  │
  ├─ 数据类型？
  │   ├─ 连续型 → 是否满足正态分布？
  │   │              ├─ 是 → 几组比较？
  │   │              │      ├─ 2组 → 独立/配对？
  │   │              │      │      ├─ 独立 → t检验
  │   │              │      │      └─ 配对 → 配对t检验
  │   │              │      └─ 3组+ → ANOVA → 事后检验
  │   │              └─ 否 → 几组比较？
  │   │                     ├─ 2组 → Mann-Whitney U / Wilcoxon
  │   │                     └─ 3组+ → Kruskal-Wallis → Dunn检验
  │   │
  │   ├─ 分类型 → 几组比较？
  │   │            ├─ 2组 → 卡方检验 / Fisher精确检验
  │   │            └─ 3组+ → 卡方检验
  │   │
  │   └─ 相关性分析 → 数据类型？
  │                    ├─ 连续+正态 → Pearson相关
  │                    ├─ 连续+非正态 → Spearman相关
  │                    └─ 分类+分类 → 卡方检验
```

## 常用统计检验

### 1. t检验（Independent/Paired t-test）

**适用场景**：比较两组连续型数据的均值差异（数据需满足正态分布）

#### Python实现

```python
import numpy as np
import pandas as pd
from scipy import stats
import pingouin as pg

# 示例数据
group1 = np.array([23, 25, 27, 29, 31, 33, 35])
group2 = np.array([18, 20, 22, 24, 26, 28, 30])

# 1. 检验正态性（Shapiro-Wilk检验）
stat1, p1 = stats.shapiro(group1)
stat2, p2 = stats.shapiro(group2)
print(f"Group 1 正态性检验: W={stat1:.4f}, p={p1:.4f}")
print(f"Group 2 正态性检验: W={stat2:.4f}, p={p2:.4f}")

# 2. 检验方差齐性（Levene检验）
stat_levene, p_levene = stats.levene(group1, group2)
print(f"方差齐性检验: F={stat_levene:.4f}, p={p_levene:.4f}")

# 3. 独立样本t检验
t_stat, p_value = stats.ttest_ind(group1, group2)
print(f"\nt检验结果: t={t_stat:.4f}, p={p_value:.4f}")

# 4. 计算效应量（Cohen's d）
mean_diff = np.mean(group1) - np.mean(group2)
pooled_std = np.sqrt(((len(group1)-1)*np.var(group1, ddof=1) +
                       (len(group2)-1)*np.var(group2, ddof=1)) /
                      (len(group1)+len(group2)-2))
cohens_d = mean_diff / pooled_std
print(f"Cohen's d = {cohens_d:.4f}")

# 使用pingouin库（推荐，输出更全面）
result = pg.ttest(group1, group2)
print("\n使用pingouin:")
print(result)

# 配对t检验
paired_data1 = np.array([85, 88, 90, 87, 92, 89, 91])
paired_data2 = np.array([83, 86, 88, 85, 90, 87, 89])
t_paired, p_paired = stats.ttest_rel(paired_data1, paired_data2)
print(f"\n配对t检验: t={t_paired:.4f}, p={p_paired:.4f}")
```

#### R实现

```r
# 独立样本t检验
group1 <- c(23, 25, 27, 29, 31, 33, 35)
group2 <- c(18, 20, 22, 24, 26, 28, 30)

# 正态性检验
shapiro.test(group1)
shapiro.test(group2)

# 方差齐性检验
var.test(group1, group2)

# t检验
t.test(group1, group2, var.equal = TRUE)

# 效应量（需要effsize包）
library(effsize)
cohen.d(group1, group2)

# 配对t检验
before <- c(85, 88, 90, 87, 92, 89, 91)
after <- c(83, 86, 88, 85, 90, 87, 89)
t.test(before, after, paired = TRUE)
```

**APA格式报告**：
```
An independent-samples t-test was conducted to compare the means
between Group 1 (M = 29.00, SD = 4.32) and Group 2 (M = 24.00, SD = 4.32).
There was a significant difference between the two groups,
t(12) = 2.50, p = .028, d = 1.16.
```

### 2. 方差分析（ANOVA）

**适用场景**：比较三组或以上连续型数据的均值差异

#### Python实现

```python
from scipy import stats
import pingouin as pg
import pandas as pd

# 示例数据
group_a = [23, 25, 27, 29, 31]
group_b = [18, 20, 22, 24, 26]
group_c = [15, 17, 19, 21, 23]

# 单因素ANOVA
f_stat, p_value = stats.f_oneway(group_a, group_b, group_c)
print(f"单因素ANOVA: F={f_stat:.4f}, p={p_value:.4f}")

# 使用pingouin进行更详细的分析
data = pd.DataFrame({
    'value': group_a + group_b + group_c,
    'group': ['A']*5 + ['B']*5 + ['C']*5
})

# ANOVA
aov = pg.anova(data=data, dv='value', between='group')
print("\nANOVA结果:")
print(aov)

# 事后检验（Tukey HSD）
posthoc = pg.pairwise_tukey(data=data, dv='value', between='group')
print("\nTukey HSD事后检验:")
print(posthoc)

# 重复测量ANOVA示例
data_rm = pd.DataFrame({
    'subject': [1, 2, 3, 4, 5] * 3,
    'time': ['T1']*5 + ['T2']*5 + ['T3']*5,
    'value': [23, 25, 27, 29, 31, 28, 30, 32, 34, 36, 33, 35, 37, 39, 41]
})

rm_aov = pg.rm_anova(data=data_rm, dv='value', within='time', subject='subject')
print("\n重复测量ANOVA:")
print(rm_aov)
```

#### R实现

```r
# 单因素ANOVA
group <- factor(c(rep("A", 5), rep("B", 5), rep("C", 5)))
value <- c(23, 25, 27, 29, 31, 18, 20, 22, 24, 26, 15, 17, 19, 21, 23)

# 进行ANOVA
model <- aov(value ~ group)
summary(model)

# 事后检验（Tukey HSD）
TukeyHSD(model)

# 效应量（eta-squared）
library(lsr)
etaSquared(model)

# 重复测量ANOVA
subject <- factor(rep(1:5, 3))
time <- factor(rep(c("T1", "T2", "T3"), each=5))
value_rm <- c(23, 25, 27, 29, 31, 28, 30, 32, 34, 36, 33, 35, 37, 39, 41)

model_rm <- aov(value_rm ~ time + Error(subject/time))
summary(model_rm)
```

**APA格式报告**：
```
A one-way ANOVA was conducted to compare the effect of treatment
on test scores across three groups. There was a significant effect
of treatment at the p < .05 level for the three conditions,
F(2, 12) = 15.43, p < .001, η² = .72. Post hoc comparisons using
the Tukey HSD test indicated that Group A (M = 27.00, SD = 3.16)
scored significantly higher than Group C (M = 19.00, SD = 3.16),
p = .001, but not significantly different from Group B (M = 22.00, SD = 3.16).
```

### 3. 非参数检验

#### Mann-Whitney U 检验（两独立样本）

```python
from scipy import stats

group1 = [23, 25, 27, 29, 31, 33, 35]
group2 = [18, 20, 22, 24, 26, 28, 30]

u_stat, p_value = stats.mannwhitneyu(group1, group2, alternative='two-sided')
print(f"Mann-Whitney U: U={u_stat:.4f}, p={p_value:.4f}")

# 使用pingouin计算效应量
import pingouin as pg
result = pg.mwu(group1, group2)
print(result)
```

#### Wilcoxon符号秩检验（两配对样本）

```python
before = [85, 88, 90, 87, 92, 89, 91]
after = [83, 86, 88, 85, 90, 87, 89]

w_stat, p_value = stats.wilcoxon(before, after)
print(f"Wilcoxon检验: W={w_stat:.4f}, p={p_value:.4f}")
```

#### Kruskal-Wallis检验（多组独立样本）

```python
group_a = [23, 25, 27, 29, 31]
group_b = [18, 20, 22, 24, 26]
group_c = [15, 17, 19, 21, 23]

h_stat, p_value = stats.kruskal(group_a, group_b, group_c)
print(f"Kruskal-Wallis: H={h_stat:.4f}, p={p_value:.4f}")

# 事后检验（Dunn检验，需要scikit-posthocs包）
import scikit_posthocs as sp
import pandas as pd

data = pd.DataFrame({
    'value': group_a + group_b + group_c,
    'group': ['A']*5 + ['B']*5 + ['C']*5
})

dunn_result = sp.posthoc_dunn(data, val_col='value', group_col='group')
print("\nDunn事后检验:")
print(dunn_result)
```

### 4. 卡方检验

**适用场景**：分析分类变量之间的关联

```python
from scipy.stats import chi2_contingency
import pandas as pd

# 列联表
observed = pd.DataFrame({
    'Treatment': [30, 20],
    'Control': [15, 35]
}, index=['Success', 'Failure'])

print("观察频数:")
print(observed)

# 卡方检验
chi2, p_value, dof, expected = chi2_contingency(observed)
print(f"\n卡方检验: χ²={chi2:.4f}, p={p_value:.4f}, df={dof}")
print("\n期望频数:")
print(expected)

# 效应量（Cramér's V）
n = observed.sum().sum()
cramers_v = np.sqrt(chi2 / (n * (min(observed.shape) - 1)))
print(f"Cramér's V = {cramers_v:.4f}")

# Fisher精确检验（小样本）
from scipy.stats import fisher_exact
table = [[8, 2], [1, 9]]
odds_ratio, p_value = fisher_exact(table)
print(f"\nFisher精确检验: OR={odds_ratio:.4f}, p={p_value:.4f}")
```

**APA格式报告**：
```
A chi-square test of independence was performed to examine the
relation between treatment condition and outcome. The relation
between these variables was significant, χ²(1, N = 100) = 13.89,
p < .001, Cramér's V = .37.
```

### 5. 相关分析

```python
import numpy as np
from scipy import stats
import pingouin as pg

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([2.1, 4.3, 6.0, 8.2, 10.1, 12.3, 14.0, 16.2, 18.1, 20.0])

# Pearson相关（参数检验）
r_pearson, p_pearson = stats.pearsonr(x, y)
print(f"Pearson相关: r={r_pearson:.4f}, p={p_pearson:.4f}")

# Spearman相关（非参数检验）
r_spearman, p_spearman = stats.spearmanr(x, y)
print(f"Spearman相关: ρ={r_spearman:.4f}, p={p_spearman:.4f}")

# 使用pingouin（包含置信区间）
result = pg.corr(x, y, method='pearson')
print("\n使用pingouin:")
print(result)

# 偏相关（控制第三变量）
z = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
data = pd.DataFrame({'x': x, 'y': y, 'z': z})
partial_corr = pg.partial_corr(data=data, x='x', y='y', covar='z')
print("\n偏相关（控制z）:")
print(partial_corr)
```

**APA格式报告**：
```
A Pearson correlation was run to determine the relationship between
variable X and variable Y. There was a strong, positive correlation
between the two variables, which was statistically significant,
r(8) = .99, p < .001.
```

### 6. 线性回归

```python
from scipy import stats
import statsmodels.api as sm
import pandas as pd

# 简单线性回归
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([2.1, 4.3, 6.0, 8.2, 10.1, 12.3, 14.0, 16.2, 18.1, 20.0])

# 使用scipy（简单）
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print(f"回归系数: slope={slope:.4f}, intercept={intercept:.4f}")
print(f"R² = {r_value**2:.4f}, p = {p_value:.4f}")

# 使用statsmodels（详细）
X = sm.add_constant(x)  # 添加常数项
model = sm.OLS(y, X).fit()
print("\n回归分析摘要:")
print(model.summary())

# 多元线性回归
data = pd.DataFrame({
    'y': [5, 7, 9, 11, 13, 15, 17, 19, 21, 23],
    'x1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'x2': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
})

X_multi = sm.add_constant(data[['x1', 'x2']])
model_multi = sm.OLS(data['y'], X_multi).fit()
print("\n多元回归分析:")
print(model_multi.summary())

# 检查残差正态性
residuals = model_multi.resid
stat, p = stats.shapiro(residuals)
print(f"\n残差正态性检验: W={stat:.4f}, p={p:.4f}")
```

**APA格式报告**：
```
A simple linear regression was calculated to predict Y based on X.
A significant regression equation was found, F(1, 8) = 423.45, p < .001,
with an R² of .98. Y is equal to 0.24 + 1.99(X) when X is measured in
[units]. Y increased 1.99 units for each unit of X.
```

## 功效分析和样本量计算

### Python实现（statsmodels）

```python
from statsmodels.stats.power import TTestIndPower, FTestAnovaPower
import matplotlib.pyplot as plt
import numpy as np

# t检验功效分析
analysis = TTestIndPower()

# 1. 计算样本量（给定效应量、功效、显著性水平）
effect_size = 0.5  # Cohen's d
alpha = 0.05       # 显著性水平
power = 0.80       # 统计功效

sample_size = analysis.solve_power(effect_size=effect_size,
                                   alpha=alpha,
                                   power=power,
                                   alternative='two-sided')
print(f"每组所需样本量: {np.ceil(sample_size):.0f}")

# 2. 计算功效（给定样本量、效应量）
actual_power = analysis.solve_power(effect_size=effect_size,
                                    nobs1=30,
                                    alpha=alpha,
                                    alternative='two-sided')
print(f"实际统计功效: {actual_power:.4f}")

# 3. 计算可检测的最小效应量（给定样本量、功效）
min_effect = analysis.solve_power(nobs1=30,
                                  alpha=alpha,
                                  power=power,
                                  alternative='two-sided')
print(f"可检测的最小效应量: {min_effect:.4f}")

# 4. 绘制功效曲线
effect_sizes = np.arange(0.1, 1.5, 0.1)
sample_sizes = [analysis.solve_power(effect_size=es, alpha=alpha, power=power)
                for es in effect_sizes]

plt.figure(figsize=(8, 6))
plt.plot(effect_sizes, sample_sizes)
plt.xlabel('Effect Size (Cohen\'s d)')
plt.ylabel('Sample Size per Group')
plt.title('Sample Size vs Effect Size (Power = 0.80, α = 0.05)')
plt.grid(True)
plt.savefig('power_analysis.png', dpi=300)

# ANOVA功效分析
anova_analysis = FTestAnovaPower()
k = 3  # 组数
sample_size_anova = anova_analysis.solve_power(effect_size=0.25,
                                               alpha=0.05,
                                               power=0.80,
                                               k_groups=k)
print(f"\nANOVA每组所需样本量: {np.ceil(sample_size_anova):.0f}")
```

### R实现（pwr包）

```r
library(pwr)

# t检验功效分析
# 计算样本量
pwr.t.test(d = 0.5, sig.level = 0.05, power = 0.80, type = "two.sample")

# 计算功效
pwr.t.test(n = 30, d = 0.5, sig.level = 0.05, type = "two.sample")

# ANOVA功效分析
pwr.anova.test(k = 3, f = 0.25, sig.level = 0.05, power = 0.80)

# 相关分析功效
pwr.r.test(r = 0.3, sig.level = 0.05, power = 0.80)

# 卡方检验功效
pwr.chisq.test(w = 0.3, df = 1, sig.level = 0.05, power = 0.80)

# 绘制功效曲线
effect_sizes <- seq(0.1, 1.0, 0.1)
power_curve <- sapply(effect_sizes, function(d) {
  pwr.t.test(d = d, sig.level = 0.05, n = 30, type = "two.sample")$power
})

plot(effect_sizes, power_curve, type = "l",
     xlab = "Effect Size", ylab = "Power",
     main = "Power Curve (n=30 per group)")
abline(h = 0.80, col = "red", lty = 2)
```

## 统计报告规范

### APA 第7版格式

#### 描述性统计
```
Participants' ages ranged from 18 to 65 years (M = 32.5, SD = 10.2).
```

#### t检验
```
Independent samples t-test: t(58) = 2.45, p = .017, d = 0.65
Paired samples t-test: t(29) = 3.21, p = .003, d = 0.59
```

#### ANOVA
```
One-way ANOVA: F(2, 87) = 5.43, p = .006, η² = .11
Two-way ANOVA: F(1, 56) = 12.34, p < .001, ηp² = .18
```

#### 卡方检验
```
χ²(2, N = 150) = 8.76, p = .013, Cramér's V = .24
```

#### 相关
```
Pearson correlation: r(48) = .67, p < .001, 95% CI [.49, .79]
```

#### 回归
```
β = 0.42, SE = 0.12, t(97) = 3.50, p < .001, 95% CI [0.18, 0.66]
```

### 报告检查清单

统计结果报告时必须包含：
- [ ] 检验统计量的值（t, F, χ², r等）
- [ ] 自由度 df
- [ ] p值（精确值或 p < .001）
- [ ] 效应量（d, η², r等）
- [ ] 描述性统计（M, SD, n）
- [ ] 置信区间（95% CI）
- [ ] 样本量和功效（在方法部分）

## 常见统计陷阱及避免方法

### 1. p-Hacking（p值操纵）

**问题**：通过多次检验、选择性报告、数据窥探等方式人为降低p值

**避免方法**：
```python
# 预先注册分析计划（Pre-registration）
# 1. 在收集数据前确定：
#    - 样本量（基于功效分析）
#    - 主要结局指标
#    - 统计检验方法
#    - 显著性阈值

# 2. 如果进行多次检验，使用多重比较校正
from statsmodels.stats.multitest import multipletests

# 示例：5个假设检验
p_values = [0.03, 0.045, 0.02, 0.10, 0.01]

# Bonferroni校正
reject_bonf, pvals_bonf, _, _ = multipletests(p_values, method='bonferroni')
print("Bonferroni校正后的p值:", pvals_bonf)

# FDR (Benjamini-Hochberg)校正
reject_fdr, pvals_fdr, _, _ = multipletests(p_values, method='fdr_bh')
print("FDR校正后的p值:", pvals_fdr)
```

### 2. 多重比较问题

**问题**：进行多次统计检验会增加假阳性率

**解决方案**：
- 使用Bonferroni校正（保守）
- 使用FDR校正（较温和）
- 使用事后检验方法（Tukey HSD, Dunnett等）

### 3. 样本量不足

**问题**：样本量太小导致统计功效不足，无法检测到真实效应

**解决方案**：
```python
# 始终进行事先功效分析
# 报告事后功效分析结果

from statsmodels.stats.power import TTestIndPower

analysis = TTestIndPower()

# 计算观察到的效应量
observed_d = (mean1 - mean2) / pooled_std

# 计算事后功效
post_hoc_power = analysis.solve_power(
    effect_size=observed_d,
    nobs1=len(group1),
    alpha=0.05
)

print(f"事后统计功效: {post_hoc_power:.4f}")
if post_hoc_power < 0.80:
    print("警告：统计功效不足，可能存在II型错误！")
```

### 4. 假设违反

**问题**：使用参数检验但数据不满足假设（如正态性、方差齐性）

**解决方案**：
```python
# 始终检验假设
from scipy import stats

# 1. 正态性检验
stat, p = stats.shapiro(data)
if p < 0.05:
    print("数据不满足正态分布，考虑使用非参数检验")

# 2. 方差齐性检验
stat, p = stats.levene(group1, group2)
if p < 0.05:
    print("方差不齐，使用Welch's t-test")
    t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=False)

# 3. 异常值检测
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1
outliers = (data < Q1 - 1.5*IQR) | (data > Q3 + 1.5*IQR)
print(f"检测到 {outliers.sum()} 个异常值")
```

### 5. 伪相关（Spurious Correlation）

**问题**：两个变量有相关性但没有因果关系（可能由第三变量导致）

**解决方案**：
```python
import pingouin as pg

# 使用偏相关控制混杂变量
data = pd.DataFrame({
    'X': x_data,
    'Y': y_data,
    'Z': confounding_variable
})

# 控制Z后X和Y的相关
partial = pg.partial_corr(data=data, x='X', y='Y', covar='Z')
print(partial)

# 或使用多元回归分析
import statsmodels.formula.api as smf
model = smf.ols('Y ~ X + Z', data=data).fit()
print(model.summary())
```

### 6. 基线不平衡

**问题**：比较组之间在基线特征上存在差异

**解决方案**：
```python
# 使用ANCOVA（协方差分析）校正基线差异
import statsmodels.api as sm
from statsmodels.formula.api import ols

# baseline: 基线测量值
# group: 分组变量
# outcome: 结局变量
data = pd.DataFrame({
    'outcome': outcome_values,
    'group': group_labels,
    'baseline': baseline_values
})

# ANCOVA模型
model = ols('outcome ~ C(group) + baseline', data=data).fit()
print(sm.stats.anova_lm(model, typ=2))
```

## Python常用统计库总结

```python
# 安装命令
pip install scipy numpy pandas statsmodels pingouin scikit-posthocs matplotlib seaborn
```

| 库 | 主要功能 | 推荐用途 |
|------|---------|----------|
| **scipy.stats** | 基础统计检验 | 快速简单分析 |
| **statsmodels** | 回归、时间序列 | 详细统计建模 |
| **pingouin** | 全面统计分析 | 效应量、功效分析 |
| **scikit-posthocs** | 事后检验 | 多重比较 |
| **numpy** | 数值计算 | 数据处理 |
| **pandas** | 数据框架 | 数据组织 |

## R常用统计包总结

```r
# 安装命令
install.packages(c("car", "pwr", "effsize", "lsr", "ggplot2", "dplyr"))
```

| 包 | 主要功能 |
|----|----------|
| **stats** | 基础统计（内置）|
| **car** | 回归诊断、ANOVA |
| **pwr** | 功效分析 |
| **effsize** | 效应量计算 |
| **lsr** | 学习统计基础 |

## 参考资源

- [APA Style Statistics Guidelines](https://apastyle.apa.org/instructional-aids/numbers-statistics-guide.pdf)
- [Statistical Tests Decision Tree](https://stats.idre.ucla.edu/other/mult-pkg/whatstat/)
- [Effect Size Calculators](https://www.psychometrica.de/effect_size.html)
- [G*Power (功效分析软件)](https://www.psychologie.hhu.de/arbeitsgruppen/allgemeine-psychologie-und-arbeitspsychologie/gpower)
- [Ten Simple Rules for Effective Statistical Practice](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004961)
