# Experiments 章节骨架

## 章节结构

```
4. Experiments
   4.1 Experimental Setup      ← 数据、基线、指标、实现
   4.2 Main Results            ← 1-2 个核心表 + 关键发现
   4.3 Ablation Studies        ← 见 methods/ablation-studies.md
   4.4 Analysis                ← 失败案例、可视化、定性分析
   4.5 (Optional) Real-world / Out-of-distribution Tests
```

---

## 4.1 Experimental Setup

子节内分小标题（**bold**），便于审稿人快速定位。

```
**Datasets.** We evaluate on $\{D_1\}$ [REF], $\{D_2\}$ [REF], and $\{D_3\}$ [REF].
$\{D_1\}$ contains $\{N\}$ samples across $\{C\}$ classes ...
We use the standard $\{train/val/test\}$ split provided by [REF].

**Baselines.** We compare against:
(1) $\{Baseline_1\}$ [REF]: $\{one-line description\}$;
(2) $\{Baseline_2\}$ [REF]: ...;
...
For fair comparison, all baselines are re-implemented / re-trained under our experimental setup.

**Evaluation Metrics.** We report $\{M_1, M_2, M_3\}$ as defined in [REF].
Higher $\{M_1\}$ indicates $\{property\}$.

**Implementation Details.** We implement $\{Method\}$ in PyTorch and train on $\{N\}$ $\{GPU\}$ GPUs.
We use $\{optimizer\}$ with learning rate $\{lr\}$, batch size $\{bs\}$, for $\{E\}$ epochs.
We select $\{hyperparam\}$ via grid search over $\{range\}$ on the validation set.
All results are averaged over $\{K\}$ random seeds; error bars indicate $\{std / 95\% CI\}$.
```

**红线**：
- 不给 hyper 选择方式 → 审稿人质疑 fairness
- 不报 random seed 数 → 直接 reject 风险
- 用自己魔改的数据划分但不说明 → 致命

## 4.2 Main Results

**结构**：一段说看哪个表，一段说核心发现。

模板：
> Table 1 reports performance on $\{D_1\}$ across $\{N\}$ baselines.
> $\{Method\}$ achieves $\{X\%\}$ accuracy, outperforming the strongest baseline $\{B\}$ by $\{Y\%\}$ ($p < 0.01$, paired Wilcoxon).
> The improvement is particularly pronounced in $\{subset / condition\}$, where we observe $\{specific gain\}$.

**Main 表的规范**：

```
| Method        | $D_1$ Acc ↑   | $D_1$ F1 ↑    | $D_2$ Acc ↑   | $D_2$ F1 ↑    | Params ↓ | FLOPs ↓ |
|---------------|---------------|---------------|---------------|---------------|----------|---------|
| $B_1$ [REF]   | 82.1 ± 0.3    | 80.5 ± 0.4    | 75.2 ± 0.5    | 73.8 ± 0.6    | 28M      | 5.1G    |
| $B_2$ [REF]   | 84.7 ± 0.2    | 83.1 ± 0.3    | 77.9 ± 0.4    | 76.5 ± 0.5    | 31M      | 5.8G    |
| **Ours**      | **87.3 ± 0.2**| **86.1 ± 0.3**| **80.4 ± 0.3**| **79.2 ± 0.4**| **24M**  | **4.2G**|
```

- **粗体**最优
- 下划线次优
- **箭头**标方向（↑ 越大越好）
- 维持**相同列顺序**跨多个表
- 计算成本与性能放同一张表，让 trade-off 一目了然

## 4.3 Ablation Studies

详见 `knowledge/methods/ablation-studies.md`。一句话：**每个新组件 + 每个 loss 项 + 关键超参各一组消融**。

## 4.4 Analysis

不要让 Experiments 只是堆数字。Analysis 让审稿人觉得你"懂自己的方法"。

可选小节：
- **Qualitative results** — 可视化例子（好 + 坏）
- **Failure cases** — 诚实地展示失败，说明边界
- **Sensitivity analysis** — 对关键超参的鲁棒性
- **Computational efficiency** — 训练 / 推理时间、显存
- **Scaling behavior** — 数据 / 参数量增大时的表现
- **Probing / Attention 可视化** — 解释方法 why work

模板（probing）：
> To understand why $\{Method\}$ works, we visualize $\{intermediate quantity\}$ in Figure $\{n\}$.
> We observe $\{pattern\}$, consistent with our hypothesis that $\{insight\}$.
> Quantitatively, $\{metric\}$ decreases from $\{x\}$ to $\{y\}$ when $\{intervention\}$, confirming $\{mechanism\}$.

## 4.5 Real-world / OOD Tests（可选）

强论文通常有：
- **Out-of-distribution** 数据集（验证泛化）
- **Adversarial** 样本（验证鲁棒性）
- **Long-tail** / **rare class** 分析
- **Real deployment** 数据（学术 → 实际场景）

---

## 表格 / 图标规范

| 元素 | 规则 |
|------|------|
| 数字格式 | 保持小数点位数一致（建议 2 位）|
| 单位 | 列名带单位（"Time (s)"，"Params (M)"） |
| ± 后数字 | 表头或 caption 说明是 std / SEM / CI |
| 列顺序 | baseline → SOTA → ours，按性能或时间排 |
| ↑/↓ | 表头注明指标方向 |
| 加粗 | 仅用于最优值 |
| color | 慎用（黑白打印失效） |

## 检查清单

- [ ] 数据集 / 基线 / 指标 / 实现细节四要素齐全
- [ ] 至少 3 个 seed，报方差
- [ ] 显著性检验 + 多重比较修正
- [ ] 主表包含计算成本
- [ ] 消融对应 Method 中每个 design choice
- [ ] 有失败案例分析
- [ ] 与 SOTA 直接对比（公平条件下）
- [ ] 所有表格 / 图都在正文 reference 到
- [ ] Caption 自包含（能脱离正文看懂）
