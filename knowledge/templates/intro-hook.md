# Introduction 章节模板

## 结构（CS / AI 通用 4 段式）

1. **领域开场 + 趋势**（1 段，3–5 句）
2. **现有方法 + 局限**（1–2 段）
3. **本文方法 + 核心 insight**（1 段）
4. **贡献列表**（1 段 + bullet list）

总长度：top conference 1–1.5 页，期刊 1.5–2 页。

---

## Hook 模板（开篇第一句）

### 模板 A — 趋势 / 影响驱动

> Large language models have transformed $\{domain\}$, achieving $\{achievement\}$ across $\{tasks\}$.
> However, $\{persistent limitation\}$ remains a critical obstacle to $\{real-world goal\}$.

### 模板 B — 反直觉发现驱动（开篇即抓人）

> Despite the success of $\{method family\}$ on $\{task\}$, we observe that $\{counterintuitive phenomenon\}$.
> In this work, we identify $\{root cause\}$ and propose $\{solution\}$ that $\{result\}$.

### 模板 C — 问题驱动

> A long-standing question in $\{field\}$ is whether $\{open question\}$.
> Existing approaches either $\{limitation 1\}$ or $\{limitation 2\}$, leaving $\{gap\}$ unaddressed.

### 模板 D — 应用驱动

> $\{Application\}$ requires $\{capability\}$ — yet current methods $\{fall short on specific aspect\}$,
> as evidenced by $\{quantitative gap\}$ on $\{benchmark\}$.

**避免**：
- "In recent years, AI has developed rapidly..."（写作课禁句）
- "With the rapid development of deep learning..."
- 全段都是定义和介绍，没有论点
- 第一句就长公式

## 段 2:现有方法分类 + 局限

**三段论模板**：
> Prior work falls into two categories.
> $\{Category A\}$ methods [REF] focus on $\{angle\}$, but $\{limitation A\}$.
> $\{Category B\}$ methods [REF] address $\{aspect\}$, yet $\{limitation B\}$.
> Both lines share $\{common gap\}$ that motivates our work.

**关键技巧**：批评要**具体且可验证**（"X 在 long-context 时 attention 复杂度 O(n²)"），不要笼统（"X 效果不好"）。

## 段 3:本文方法

**Insight-first 模板**：
> Our key insight is that $\{counterintuitive observation\}$.
> Building on this, we propose $\{Method Name\}$, which $\{one-sentence mechanism\}$.
> Unlike $\{prior approach\}$, our method $\{differentiator\}$, enabling $\{capability\}$.

**避免**：
- 一上来就堆模块（"Our method has three components..."）
- 没有 insight 只有 implementation 描述

## 贡献列表

3–4 条，**每条用一个动词开头**：
- We **identify** $\{problem\}$ in $\{setting\}$ and **show** $\{evidence\}$.
- We **propose** $\{Method\}$, the first $\{property\}$ approach for $\{task\}$.
- We **demonstrate** that $\{Method\}$ achieves $\{X\%\}$ improvement over $\{strongest baseline\}$ on $\{N benchmarks\}$.
- We **release** code, pretrained models, and $\{any new dataset\}$ to facilitate future research.

**贡献写作 do / don't**：
- ✅ "First to do X"（要敢肯定，但确保确实第一）
- ✅ 量化（"30% faster"，"+2.1 BLEU"）
- ❌ "We do extensive experiments"（"extensive" 是水词）
- ❌ "We show good performance"（"good" 不是贡献）
- ❌ 把方法名当贡献（"We propose XYZ" 没说 XYZ 解决什么）

## 末段 — 通向后文（可选 1 段）

> Section $\{2\}$ reviews related work.
> Section $\{3\}$ describes our method.
> Section $\{4\}$ presents experiments on $\{datasets\}$.
> Section $\{5\}$ discusses limitations and concludes.

很多 top conference 已经不写这段（占地方）。仅当论文结构非标准时才写。

## Figure 1（teaser figure）

强烈建议：introduction 配一张 teaser figure，让审稿人 30 秒看懂。
- 左边：现有方法 / 问题
- 右边：本文方法 / 结果
- 配一个最 striking 的数字
