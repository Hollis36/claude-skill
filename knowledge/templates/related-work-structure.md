# Related Work 章节结构

## 三种组织方式

### A. 按主题（topic-based）— 最常见

按相关研究的子领域分小标题，每节末尾说明本文差异。

```
## Related Work

### 2.1 Self-Supervised Representation Learning
[REF1, REF2] 早期方法 ...
[REF3, REF4] 最近进展 ...
Unlike these methods that $\{focus on X\}$, our work $\{focuses on Y\}$.

### 2.2 Vision-Language Models
...
```

**适合**：方法涉及多个独立研究方向。

### B. 按方法家族（method-based）

按技术路线分类：监督 vs 自监督、基于优化 vs 基于学习等。

**适合**：本文方法本质是改进 / 替换现有家族中的某个组件。

### C. 按问题维度（problem-based）

按"哪些挑战已被解决 / 未解决"组织，本文方法对应解决新挑战。

**适合**：综述类、提出新问题的论文。

---

## 写作原则

### Do

- **每个引用都和本文有具体连接**，不是"我也读过这篇"
- **明确差异**：每个 paragraph 末尾或专门一段说 "Unlike X, we ..."
- **按时间梳理 lineage**：早期 → 突破 → 最新，让审稿人看到 progression
- **承认前辈**：直接受益的工作给足 credit
- **覆盖最近 1–2 年**的工作（顶会评审最在意）

### Don't

- "X et al. [1] proposed A. Y et al. [2] proposed B."（流水账）
- 全章节没有一个 "Unlike ours" 比较
- 漏掉**同时期工作**（concurrent work，> 投稿前 3 个月的算）— arXiv 也要看
- 把 Related Work 当成入门教程，介绍基础概念占去一半篇幅
- 把竞品贬低 / 错误归类（评审很可能就是被你 diss 的那位）

---

## 模板段落（科研 + AI）

### 关联 + 差异化（推荐每段都这样）

> $\{Method family X\}$ has been extensively studied for $\{task\}$.
> [Author1 et al., 2023] proposed $\{technique A\}$ to address $\{aspect\}$, achieving $\{result\}$ on $\{benchmark\}$.
> [Author2 et al., 2024] extended this with $\{technique B\}$ for $\{improvement\}$.
> However, both methods $\{share limitation\}$, particularly when $\{condition\}$.
> Our work differs in $\{key dimension\}$: rather than $\{their approach\}$, we $\{our approach\}$,
> which enables $\{capability they lack\}$.

### Concurrent work 处理

> Concurrent with our work, [Author et al., 2025] explore $\{similar idea\}$.
> While both approaches $\{share insight\}$, our method $\{key difference\}$,
> and we further demonstrate $\{additional aspect\}$.

放在 Related Work 末尾或 footnote。诚实标 concurrent 比被审稿人发现遗漏好十倍。

---

## 长度与位置

| 会议 / 期刊 | 长度 | 位置 |
|------------|------|------|
| NeurIPS / ICML / ICLR | 0.5–1 页 | 通常 Section 2，紧接 Intro |
| CVPR | 1 页左右 | 同上 |
| ACL / EMNLP | 0.5–1 页 | 同上 |
| 期刊（TPAMI / JMLR） | 1.5–3 页 | 同上 |
| 短论文（4–8 页） | 集成入 Intro | 不单独成节 |

---

## 检查清单

- [ ] 覆盖了过去 1 年 arXiv 重要进展
- [ ] 每个子节都有 "Unlike X" 句子
- [ ] 包含 concurrent work（如有）
- [ ] 没有 misattribute 引用
- [ ] 没有 self-citation 过度（一般 < 总引用 20%）
- [ ] 没有 missing 经典开山工作
- [ ] 引用格式统一（NeurIPS: numeric；ACL: author-year）
