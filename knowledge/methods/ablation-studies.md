# 消融实验（Ablation Studies）

## 核心问题

消融的目的是回答：**"这个组件 / 设计 / 超参的贡献有多大？"**
不是为了堆实验，是为了让审稿人相信你方法的每个部分都必要。

## 设计原则

1. **一次只动一个变量**。同时去掉两个模块得到的差异无法归因。
2. **从完整模型开始往下减**，不要从基线往上加（前者更符合"消融"语义，也更容易写表格）。
3. **每个消融对应一个明确假设**。先写出假设：「移除 X 会降低 Y 指标 Z%」，再做实验。结果与假设不符的发现更值钱。
4. **保留对照**：完整模型一行 + 每个去除一行 + 替换为简单 baseline 一行。
5. **同样 seed、同样 budget**。否则你测的可能是噪声或资源。

## 必备消融清单（CS/AI 通用）

- [ ] **每个新模块**：去掉后性能变化
- [ ] **每个 loss 项**：weight=0 时的影响
- [ ] **架构选择**：层数、宽度、激活函数
- [ ] **超参数敏感性**：lr、batch size、weight decay 至少各取 3 个值
- [ ] **数据规模**：1/4、1/2、全量训练
- [ ] **训练 trick**：augmentation、warmup、EMA 等是否真有用
- [ ] **替换为更简单的实现**：复杂模块退化为线性 / mean pooling 时的差距

## 常见陷阱

| 陷阱 | 解决 |
|------|------|
| 只跑 1 个 seed 报"提升 0.3%" | 至少 3 个 seed，报均值 ± 标准差，并做显著性检验 |
| 消融全是"加了有用"，全员正贡献 | 太完美可疑；审稿人会怀疑 cherry-picking。诚实报告无效或副作用 |
| 不同行用不同训练时长 | 固定 epoch / steps / FLOPs |
| 大模型 + 小数据消融，结论外推到大数据 | 在你能跑的最大规模上至少做一次完整消融 |
| 表格里只有最终指标 | 加上训练曲线 / 收敛步数 / 计算成本 |

## 表格模板

```
| Method                  | Acc ↑       | F1 ↑        | Params (M) | FLOPs (G) |
|-------------------------|-------------|-------------|------------|-----------|
| Full (Ours)             | 87.3 ± 0.2  | 86.1 ± 0.3  | 24.1       | 4.2       |
| w/o Module A            | 84.1 ± 0.4  | 82.7 ± 0.5  | 22.8       | 3.9       |
| w/o Loss L_aux          | 86.8 ± 0.3  | 85.6 ± 0.4  | 24.1       | 4.2       |
| Replace Module A → MLP  | 85.2 ± 0.3  | 83.9 ± 0.4  | 23.0       | 3.7       |
```

## 写作模板

> To assess the contribution of each component, we conduct ablation studies on $\{dataset\}$.
> Table $\{n\}$ reports results across $\{k\}$ random seeds.
> Removing $\{Module A\}$ drops accuracy by $\{x\}\%$, confirming its importance for $\{reason\}$.
> The auxiliary loss $L_{aux}$ contributes a smaller but consistent $\{y\}\%$ gain,
> particularly on $\{subset / condition\}$ where $\{specific observation\}$.
