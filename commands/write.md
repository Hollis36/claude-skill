# /write — 深参与起草 / 改稿

同作者式写作。**直接产出可放进文件的英文段落**，不要先问"你想要什么风格"。

## 用户必须给的 3 件事

如果用户没说全，先问（一次问完，不要反复）：
- **位置**（Where）— 哪个章节 / 哪个 reviewer 的哪个问题（如 `draft/sections/03_method.tex §3.2` 或 `response/rebuttal_round1.md §R2-Q3`）
- **要点**（What）— 核心论点 1-3 句
- **支持**（Why）— 数字 / 文献 / 实验来源

## Agent 流程

### Step 1：加载上下文
- 读对应章节模板 `knowledge/templates/<相应>.md`（intro-hook / method-section / experiments-section / rebuttal / ...）
- 读 venue 约束 `knowledge/venues/<target>.md`（字数、格式、参考文献风格）
- 若涉及数字 — 从 `data/results.csv` 抓，不要从用户口头转述
- 读 `knowledge/glossary.md` 保术语一致

### Step 2：直接起草
- **完整段落** — 别用 "Option A / Option B" 让用户选
- **active voice**、**short sentences**（avg ≤ 25 words）
- **concrete claims** — 禁用 good / extensive / various / significantly improved（不带数字）
- **引用占位**：不在 BibTeX 找到的标 `[CITE: 描述要找什么文献]`，不编 BibTeX key
- **数字必须可溯源** — 来自 `data/results.csv` 第 N 行，或在评论里注明

### Step 3：自查清单（每次产出后跑）

**对照 `knowledge/methods/writing-style-checks.md` 全部规则**，最少检查：
- [ ] active voice — 没有 "It is shown that" / "has been" 类被动套话
- [ ] avg sentence ≤ 25 words；最长 ≤ 40 words
- [ ] 弱词黑名单：good / extensive / various / significantly（不带 p）/ delve into / utilize / leverage
- [ ] 量化 claim — 没有"good performance" 这种空话
- [ ] 数字与 `data/results.csv` 一致（手算 mean 验证关键值）
- [ ] 引用全部 `[CITE: ...]` 或真实 BibTeX key（在 `refs/main.bib` 能找到）
- [ ] 字数符合 venue 限制（rebuttal 尤其严）
- [ ] 公式 LaTeX，符号与全文 + `knowledge/glossary.md` 一致
- [ ] 中式英语扫描：是否有"as we all know"、"Last but not least"、"pave the way"

命中要在报告里 flag，可建议替换，但**不擅自改用户已写的内容**（除非是新起草段）。

### Step 4：写入文件
- **直接写文件**（用 Edit / Write），不只在 chat 里贴
- chat 里只给 diff / 关键决策说明
- 不动 `data/results.csv`、`refs/main.bib`（除非用户明说）

## Rebuttal 写作特殊规则

- 严格按 venue 字数限制（NeurIPS 6 页 / ICML 5000 字符 / CVPR 1 页 / ACL 800 字）
- 按 `knowledge/templates/rebuttal.md` 的回应类型选模板
- 每条回应必须**直接回应原文 question**，不绕弯子
- 至少提一个**新数字 / 新实验**，纯辩解无效
- 写完更新 `response/rebuttal-tracker.md` 对应行（完成度、字数）
- "Summary of changes" 段写明 camera-ready 会改什么

## 红线

1. **不许编引用** — 没在 `refs/main.bib` 的全标 `[CITE: ...]`
2. **不许编数字** — 没在 `data/results.csv` 的标 `[NEED EXP: ...]`
3. **不许过度被动语态** — "It is shown that" 类句式立即重写
4. **不许中英混杂** — 写英文段落就纯英文（中文术语括号注释 ok）
5. **不许超字数限制** — 超了直接砍，不"小幅超出 ok 吧"

$ARGUMENTS
