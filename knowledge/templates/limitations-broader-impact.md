# Limitations & Broader Impact 段落

NeurIPS 2021 起强制 Broader Impact，2022 起强制 Limitations。
ICML、ACL 也普遍要求。位置一般在 Conclusion 之前或之后，或作为独立 section。

## Limitations

### 该说什么

- **方法本身的边界**：什么场景失效、什么假设可能破
- **实验范围限制**：数据规模、领域、语言
- **计算 / 资源限制**：训练 / 推理成本
- **理论缺陷**：未证明的 claim、依赖的强假设

### 不该说什么

- 把它写成 future work 列表（"我们没做 X，但以后会做"）
- 写成"局限是太厉害以至于"这种伪谦虚
- 把它当成 disclaimer（"如有错误请联系作者"）

### 模板

> Despite the strong empirical results, $\{Method\}$ has several limitations.
>
> First, our evaluation is limited to $\{language / domain / scale\}$.
> While we expect $\{Method\}$ to generalize to $\{adjacent setting\}$, this has not been empirically verified.
>
> Second, $\{Method\}$ assumes $\{assumption\}$, which may not hold in $\{scenario\}$.
> When this assumption is violated, we observe $\{degradation\}$ (Appendix $\{X\}$).
>
> Third, training $\{Method\}$ requires $\{compute resource\}$, limiting accessibility for
> researchers without large-scale infrastructure. We partly address this by releasing
> pretrained checkpoints.
>
> Finally, our method inherits limitations of $\{underlying component\}$, including $\{specific issue\}$.
> Addressing these limitations is an important direction for future work.

### 长度

1 段（200–300 字）足够。期刊版本可扩展。

---

## Broader Impact (NeurIPS 风格)

### 该说什么

- 正面应用 — 1–2 个具体场景
- 潜在误用 — 直面，不回避
- 偏见 / 公平性问题
- 环境影响（大模型训练）
- 失败可能造成的伤害（决策系统类）

### 不该说什么

- 千篇一律的"AI 可以造福人类"
- "Our work has no societal impact"（评审会扣分）
- 列举一堆与本工作无关的 AI 风险

### 模板

> $\{Method\}$ enables $\{capability\}$, with potential positive applications in $\{domain 1\}$
> (e.g., $\{example\}$) and $\{domain 2\}$. By $\{specific benefit\}$, it could reduce
> $\{cost / barrier\}$ for $\{user group\}$.
>
> However, $\{Method\}$ also presents risks. $\{Risk 1\}$ could be misused for $\{specific misuse\}$.
> We mitigate this by $\{mitigation\}$, although $\{residual risk\}$ remains.
>
> Like other $\{model class\}$, $\{Method\}$ may exhibit $\{bias type\}$ inherited from
> $\{training data\}$. Practitioners deploying $\{Method\}$ in $\{sensitive setting\}$
> should conduct domain-specific fairness audits.
>
> Training $\{Method\}$ consumed approximately $\{X\}$ GPU-hours, corresponding to
> roughly $\{Y\}$ kg CO$_2$eq based on $\{location / grid\}$ [REF]. We release
> pretrained models to avoid redundant retraining.

---

## NeurIPS Checklist 对应回答

提交 checklist 时这两节对应：
- "Did you discuss the limitations of your work?" → Limitations section
- "Did you describe the potential negative societal impacts?" → Broader Impact section
- "Did you describe potential malicious or unintended uses?" → 同上

**直接答 Yes** 并标具体 section。No 或 N/A 需要充分理由。

---

## 学术诚信声明（部分会议要求）

- **Use of LLMs / AI tools**：按会议政策声明 ChatGPT / Claude 使用范围
  - 仅 grammar polishing → 不需详细说明，但建议致谢
  - 用于代码 / 实验设计 → 详细说明，列出贡献边界
  - 用于撰写章节 → 多数会议禁止
- **NeurIPS 2024+**：明确要求声明 LLM 使用情况，否则视为违规
