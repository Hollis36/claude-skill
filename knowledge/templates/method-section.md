# Method 章节骨架

## 章节结构

```
3. Method  (or "Approach" / "Our Method")
   3.1 Problem Formulation        ← 形式化定义
   3.2 Overview                    ← 一段话 + 一张 Figure 总览
   3.3 Component / Stage 1
   3.4 Component / Stage 2
   3.5 Training Objective          ← Loss 函数
   3.6 (Optional) Theoretical Analysis
```

长度：2–4 页（顶会），3–6 页（期刊）。

---

## 3.1 Problem Formulation

**目的**：把任务变成数学对象，建立后文符号。

模板：
> We consider the problem of $\{task description\}$.
> Let $\mathcal{X}$ denote $\{input space\}$ and $\mathcal{Y}$ denote $\{output space\}$.
> Given a dataset $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^N$ with $x_i \in \mathcal{X}, y_i \in \mathcal{Y}$,
> our goal is to learn a function $f_\theta : \mathcal{X} \to \mathcal{Y}$ parameterized by $\theta$
> that minimizes $\{loss / objective\}$.

**注意**：
- 所有符号在此节首次定义
- Notation 一旦定下，全文一致
- 区分**问题**（task）和**方法**（approach）— 这节只讲问题

## 3.2 Overview

**目的**：让审稿人 1 分钟读完知道 pipeline 长啥样。

写法：
1. **一段话**总结 pipeline（"输入 → 步骤 A → 步骤 B → 输出"）
2. **配一张 Figure 2 架构图**（最重要的图之一）
3. 强调 **key insight**（这一段就告诉读者为什么 work）

模板：
> Figure 2 illustrates the overall pipeline of $\{Method Name\}$.
> Given input $x$, we first $\{step 1\}$ (Sec. 3.3), producing $\{intermediate\}$.
> We then $\{step 2\}$ (Sec. 3.4) to obtain $\{output\}$.
> The key insight is that $\{insight\}$, which allows $\{capability\}$.

## 3.3 / 3.4 Components

**每个组件一节**，结构统一：

```
### 3.3 [Component Name]

[Motivation 1 段：为什么需要这个组件]

[Mechanism 1-2 段 + 公式]

[Implementation Details：架构选择、维度、参数量]
```

模板：
> **Motivation.** $\{Existing approach\}$ struggles with $\{specific issue\}$ because $\{reason\}$.
> To address this, we introduce $\{Component\}$, which $\{high-level mechanism\}$.
>
> **Mechanism.** Formally, given $\{input\}$, we compute
> $$\{equation\}$$
> where $\{symbol definitions\}$. The key property is $\{property\}$.
>
> **Implementation.** We implement $\{Component\}$ as $\{architecture\}$ with $\{dim\}$ hidden units
> and $\{N\}$ layers, adding $\{X\}$M parameters to the base model.

## 3.5 Training Objective

完整 loss + 解释每项。

模板：
> We train $\{Method\}$ end-to-end by minimizing
> $$\mathcal{L} = \mathcal{L}_{\text{main}} + \lambda_1 \mathcal{L}_{\text{aux}} + \lambda_2 \mathcal{L}_{\text{reg}}$$
> where $\mathcal{L}_{\text{main}} = $ [main task loss] encourages $\{primary goal\}$,
> $\mathcal{L}_{\text{aux}} = $ [auxiliary loss] enforces $\{secondary goal\}$,
> and $\mathcal{L}_{\text{reg}} = $ [regularizer] prevents $\{failure mode\}$.
> Hyperparameters $\lambda_1, \lambda_2$ are selected on the validation set (see Sec. 4.1).

## 3.6 Theoretical Analysis（可选）

如有理论结果，分 Theorem + Proof Sketch + 完整 Proof（Appendix）。

```
Theorem 3.1. Under assumptions $\{A_1, A_2\}$, $\{Method\}$ satisfies $\{property\}$ with rate $O(\{f(n)\})$.

Proof sketch. The argument proceeds in three steps. First, we show ...
Full proof is in Appendix A.
```

**写理论的红线**：
- Assumption 必须显式列出
- 证明可被验证（Appendix 完整推导）
- 不要"假设强到任何方法都满足结论"

---

## 写作风格

| 做 | 不做 |
|----|------|
| 用现在时（"We compute...") | 过去时（"We computed...") |
| Active voice（"We propose...") | 过度被动（"It is proposed that...") |
| 公式用 `\eqref{eq:name}` 引用 | 公式无编号、文中不引用 |
| 第一次出现的术语用 `\emph{}` 强调 | 滥用 bold / italic |
| 复杂步骤配伪代码（`algorithm2e`） | 长段落描述算法 |
| 维度 / 参数量明确给出 | "a neural network"（多大？） |

## 检查清单

- [ ] Problem 形式化清晰
- [ ] Overview 配架构图
- [ ] 每个组件有 motivation + mechanism + implementation
- [ ] 公式所有符号都定义
- [ ] Loss 每项都解释 + 超参选择说明
- [ ] 与 Sec. 4 Experiments 中的 ablation 对应
- [ ] 有伪代码（推荐主算法）
- [ ] 参数量、计算量量化
