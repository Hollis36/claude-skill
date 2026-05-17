# Rebuttal / Response to Reviewers 模板

## Rebuttal 原则（按重要度排序）

1. **态度卑微而有力**：感谢 → 直接回应 → 让步或反驳 → 承诺
2. **新实验 > 嘴上辩解** — 哪怕只补 1 个数字
3. **逐条回应**，不要合并 reviewer 关心点
4. **不卑不亢**：错就承认，对就坚持
5. **字数严格控制**：NeurIPS / ICML 通常 1 页 / reviewer

---

## 整体结构

```
## Response to Reviewer #X (Confidence Y)

We thank Reviewer X for the thoughtful comments and the recognition that
$\{positive point from review\}$. Below we address each concern.

**[Q1] $\{Brief paraphrase of question\}$**

$\{Direct response 1-3 sentences\}$. We have $\{new experiment / clarification\}$.
[New result if any: 1-2 lines of numbers]

**[Q2] $\{Next question\}$**

...

**Summary of changes.** We will revise the manuscript to:
(a) $\{change 1\}$;
(b) $\{change 2\}$;
(c) $\{change 3\}$.
```

---

## 应对各类常见 critique

### "Lack of novelty" / "Incremental"

```
**[Novelty]** We appreciate the concern. We respectfully argue that the novelty lies in
$\{specific aspect 1\}$ and $\{specific aspect 2\}$, which are distinct from prior work:
[ref A] addresses $\{X\}$ but assumes $\{Y\}$; [ref B] focuses on $\{Z\}$ in a different
setting. Our $\{key insight\}$ enables $\{capability\}$ that neither achieves
(see Tab. $\{N\}$ for direct comparison).
```

### "Missing baseline X"

```
**[Baseline X]** Thank you for pointing to [X]. We have implemented and evaluated [X]
under our experimental setup; results are in the table below. Our method outperforms [X]
by $\{margin\}$ on $\{D_1\}$ and $\{margin\}$ on $\{D_2\}$. We will add this to the camera-ready.

| Method | $D_1$ | $D_2$ |
|--------|-------|-------|
| [X]    | 82.1  | 75.3  |
| Ours   | 87.3  | 80.4  |
```

### "Missing ablation Y"

```
**[Ablation Y]** We agree this is important. We conducted the requested ablation:
removing $\{component\}$ drops $\{metric\}$ by $\{X\%\}$ on $\{D\}$, confirming its necessity.
The full ablation will be included in the revised Section 4.3.
```

### "Why doesn't your method work on Z?"

```
**[Performance on Z]** This is a fair observation. We attribute the lower performance
on $\{Z\}$ to $\{specific reason\}$, evidenced by $\{analysis\}$. To partially address this,
we $\{mitigation\}$, improving from $\{a\}$ to $\{b\}$ on Z (Tab. updated).
We will discuss this limitation explicitly in Section $\{Limitations\}$.
```

### "Concerns about statistical significance / few seeds"

```
**[Statistical significance]** We have re-run the main experiments with 5 random seeds
(previously 3). The improvements remain significant: $\{Method\}$ vs $\{best baseline\}$
yields $p = \{value\}$ (paired Wilcoxon, one-sided). Updated table with mean ± std and
p-values is below. We will replace the original results in the revision.
```

### "Method description unclear"

```
**[Clarity of Method]** We apologize for the confusion. We will revise Section $\{N\}$ to:
(i) add pseudocode for $\{Algorithm\}$;
(ii) clarify the role of $\{component\}$ with an illustrative example;
(iii) explicitly define $\{symbol\}$ on first use.
A draft of the revised paragraph is provided below: [...]
```

### "Why not use SOTA model X as backbone?"

```
**[Choice of backbone]** Our experiments use $\{backbone\}$ for fair comparison with
[REFs that also use this]. To address the reviewer's question, we additionally ran
$\{Method\}$ on $\{SOTA backbone\}$: $\{result\}$, showing consistent improvements across
backbones. We will add backbone-ablation in Appendix.
```

### "Method only marginally beats X"

```
**[Marginal improvement]** While the absolute improvement on $\{D_1\}$ is modest ($\{x\}\%$),
the gain is statistically significant ($p < 0.01$) and consistent across $\{N\}$ benchmarks.
More importantly, $\{Method\}$ achieves this with $\{fewer params / less compute\}$
(Tab. $\{N\}$), and the improvement on $\{harder subset\}$ is substantially larger ($\{y\}\%$).
We agree that on $\{D_2\}$ both methods are saturated and will highlight this in the discussion.
```

### "Concerns about reproducibility"

```
**[Reproducibility]** We will release code, configs, and checkpoints upon acceptance.
For the rebuttal, we provide an anonymous repository: $\{anon URL\}$.
All hyperparameters are listed in Appendix $\{X\}$; the main experiments can be reproduced
with `bash scripts/reproduce_table_1.sh` in $\{Y\}$ hours on $\{hardware\}$.
```

---

## 该承认错误的时候

被指出**真实**错误时（计算错误、bug、claim 过强）：

```
**[Error in $\{X\}$]** The reviewer is correct. We discovered $\{specific issue\}$ and
have rerun the affected experiments. The corrected results are: $\{new numbers\}$.
While the qualitative conclusion ($\{conclusion\}$) holds, we will update Tab. $\{N\}$ and
revise the relevant claim in Section $\{Y\}$.
```

承认不丢分；不承认被反复戳穿才丢分。

---

## 该坚持的时候

被批评但 reviewer 误解时：

```
**[Clarification on $\{point\}$]** We respectfully clarify that $\{our actual claim/method\}$,
not $\{reviewer's interpretation\}$. This is detailed in Section $\{X\}$, line $\{Y\}$:
"$\{quote\}$". We acknowledge this may have been unclear and will rephrase to:
"$\{clearer rephrasing\}$".
```

不要直接说 "reviewer is wrong"。用 "we respectfully clarify" / "we may have been unclear" 转移焦点。

---

## Author Response 之外的策略

1. **Rebuttal 期间补实验**：哪怕只补 1 个 baseline / 1 个 ablation，比纯辩解强 10 倍
2. **跨 reviewer 共享回应**：如果两个 reviewer 问类似问题，统一回答 + 互相 reference
3. **Tagging meta-reviewer**：写 "We hope the AC will consider that $\{positive points from R1, R2\}$"，帮 AC 整合分歧
4. **Plot 修改前后对比**：贴一张表格"Before / After"显示新结果，视觉冲击大
5. **保持版本控制**：每个 reviewer 一个文件，便于 AC 检阅
