# 论文英文写作风格检查

`/write` 每次产出后必跑的自查清单。读者是审稿人，每多 1 句废话都减少耐心。

## 红线（绝对禁止）

| 模式 | 例 | 改成 |
|------|-----|------|
| 过度被动语态 | "It is shown that the method achieves..." | "Our method achieves..." |
| 弱动词 | "We discuss the limitation..." | "We identify three limitations..." |
| 冗余强化 | "It is very important to note that..." | "Note that..." 或直接删 |
| ChatGPT 套话 | "Delve into / In conclusion / Moreover" | 替换或删 |
| 无量化 claim | "achieves good performance" | "achieves 87.3% accuracy" |
| 没数字的对比 | "outperforms the baseline" | "outperforms the strongest baseline by 2.6 pp ($p<0.01$)" |
| 现在分词长链 | "Building on this, leveraging X, while considering Y, the method..." | 拆成 2-3 句 |
| 含糊量词 | "various / several / multiple methods" | "three methods" 或具体列名 |

## 弱词黑名单（出现就重审）

```
good / bad
extensive / extensively
significantly improved（不带 p-value）
state-of-the-art performance（要带数字）
novel / innovative（claim 而非形容词）
robust / efficient（要量化 or 说明 vs what）
various / several / a number of
in order to → 用 "to"
utilize → 用 "use"
demonstrate → 限于 contribution list；正文用 "show"
leverage（顶会泛滥）→ 用 "use" 或 "exploit"
delve into / dive into → 改 "examine" 或 "study"
furthermore / moreover（连续多句开头）
basically / essentially
quite / very / really
```

## 句长

- **平均** 句长 ≤ 25 词
- **最长** 句 ≤ 40 词（超了拆）
- 段首句子简短一句，把论点说清

## 段落

- 一段一个 idea；超过 200 词建议拆
- **首句立论**（topic sentence），后续句支撑
- **末句过渡**到下一段（或总结），不是又起新话题

## Active voice 检测启发

被动结构高频模式（grep 出来重写）：
```
"is/are/was/were [verb-ed] by"
"has been [verb-ed]"
"can be [verb-ed]"
"it is [adj] that"
"it should be noted"
"it is worth noting"
```

允许的被动：
- 强调结果而非主体（"The model was trained on 100B tokens"）
- 主体未知或不重要（"The dataset was released in 2024"）
- 实验描述被动惯用（"Hyperparameters were tuned via grid search"）

## Contribution 列表特殊规则

写 "Our contributions are:" 后面的 bullet：
- ✅ "We **propose** ..." / "We **demonstrate** ..." / "We **release** ..."
- ❌ "Our paper proposes ..." / "This work introduces ..."
- 每条必须**带量化**或**首次性 claim**
- 不超过 4 条

## Rebuttal 特殊规则

字数严苛 → 删形容词、副词、连接词：
- "We respectfully argue that the novelty lies in" → "Novelty lies in"
- "We have conducted additional experiments showing that" → "Additional experiments show"
- "As the reviewer correctly points out, ..." → 删（评审知道自己说了什么）
- "Thank you for this insightful comment" → 整段 rebuttal 致谢一次就够

## 中式英语高频问题

| 中式 | 修 |
|------|-----|
| "We have done a lot of experiments" | "We conduct extensive experiments" → 进一步：具体数字 |
| "good performance / poor performance" | 量化 |
| "by using X, we can do Y" | "X enables Y" / "Using X, we Y" |
| "as we all know" | 删 |
| "Last but not least" | "Finally" |
| "open the door for / pave the way for" | "enable" 或 "support" |
| 主语连续 "we" 开头 5+ 句 | 换被动 / 用名词主语（"The method ..."）|

## 数字格式

- 百分数：`87.3\%` 不写 `87.30\%`（多余 0），不写 `87.3 percent`
- 提升：`+2.6 pp`（百分点）或 `+2.6\%`（相对），**用哪种全文统一**
- p 值：`$p < 0.01$` 或 `$p = 0.008$`（小于 0.001 写 `$p < 0.001$`）
- 数量：`$10^4$` 不写 `10000` 或 "ten thousand"
- 区间：`87.3 \pm 0.2`（不写 87.3±0.2，要 LaTeX `$\pm$`）

## 引用风格

- **不挤句末**：`This phenomenon was observed in long-context tasks [1, 2, 3].` ❌
  → `This phenomenon was observed in long-context tasks (Smith et al., 2023; Lee, 2024).` 或拆
- **正文动作**：`Smith et al. [1] propose ...` 用 author-as-subject
- **括号引用**：`Recent work (Smith, 2024) shows ...` 不要喧宾夺主
- **未填**：`[CITE: 描述]` 占位，**不要编 BibTeX key**

## 检查自动化

```bash
# 在草稿目录跑：
grep -rn -i -E 'delve into|in order to|utilize|leverage|demonstrate' draft/  # 弱词
grep -rn -E '\bvery |\bextensive(ly)?\b|\bvarious\b|\bsignificant\b' draft/
grep -rn -E 'It is .* that|has been|can be ' draft/  # 被动启发
awk 'NR>0 {n=split($0, a, ". "); for(i=1;i<=n;i++){w=split(a[i], b, " "); if(w>40) print FILENAME":"NR": "w" words"}}' draft/sections/*.tex  # 长句
```

`/write` agent 跑完起草后**自动执行上述 grep**，发现命中要 flag 出来。
