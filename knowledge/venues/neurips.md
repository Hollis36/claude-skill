# NeurIPS

Neural Information Processing Systems — AI / ML 顶会之一。

## 基本信息

- **官网**：https://neurips.cc
- **OpenReview**：https://openreview.net/group?id=NeurIPS.cc
- **评审制度**：double-blind，4 位 reviewer + 1 AC + SAC
- **接收率**：约 25–28%（近年）
- **录用 → 出版**：会议当年 12 月（NeurIPS Proceedings）

## Timeline（年度模式，以最新一届为准 — 投稿前确认官网）

| 阶段 | 时间（大致） |
|------|------------|
| Abstract Submission | 5 月中 |
| Full Paper Submission | 5 月下 |
| Author Response (Rebuttal) | 8 月初 |
| Author Notification | 9 月底 |
| Camera-ready | 10 月底 |
| 会议召开 | 12 月初 |

## 格式

- **模板**：NeurIPS LaTeX style（每年官网更新）
- **主文长度**：9 页（不含 references、checklist、appendix）
- **References / Appendix**：不限页数
- **匿名**：彻底匿名（去 author / acknowledgments / 自引用要写"Author et al." 形式）
- **arXiv 政策**：允许 preprint，但**不**要在 OpenReview 投稿时透露 author 身份

## 必填材料

1. **Reproducibility Checklist**（强制）—  https://neurips.cc/Conferences/[year]/PaperInformation/PaperChecklist
2. **Broader Impact** 段落（强制）
3. **Limitations** 段落（强制）
4. **LLM 使用声明**（2024+ 强制）
5. **Supplementary**（代码 / appendix） — ZIP 包

## 评审

- **每位 reviewer 必读 1–2 篇匿名 highlights**：写得清楚、动机强、实验充分
- **Confidence 1–5**：5 = "absolutely certain", 大多在 3–4
- **Rating 1–10**：通常 5 或 6 是临界，4 偏弱拒，7+ 偏接受
- **AC 决定**：综合 reviewer + 自己读 + rebuttal
- **Score 公开**：录用 / 拒稿后看到 reviewer 评分

## Rebuttal 策略

- **6 页 PDF 限制**（含图表，常见 1 页 / reviewer + 1 页 cross-review）
- **截止时间通常 1 周**
- 详见 `knowledge/templates/rebuttal.md`
- **重点补实验** > 嘴上辩解

## Track

- **Main Track** — 正会
- **Datasets and Benchmarks Track** — 数据集 / benchmark 专门 track（2021 起）
- **Workshop** — 接收率较高，截止稍晚（9–10 月）
- **Spotlights / Orals** — 评分高的自动晋级，会议口头报告

## 类似会议（同档次）

ICML、ICLR、AAAI、IJCAI、KDD（应用方向）

## 提交前 5 分钟检查

- [ ] PDF 匿名化（properties 也要清）
- [ ] 9 页内（不含 ref + checklist + appendix）
- [ ] Checklist 全部填写
- [ ] Limitations + Broader Impact 段落
- [ ] LLM 使用声明
- [ ] References 格式（NeurIPS 用 numeric `[1]`）
- [ ] Figure 字号 ≥ 7pt
- [ ] 自引用形式 "Author et al. (2024)" 而非 "Our previous work [REF]"
- [ ] Supplementary 单独打包上传
