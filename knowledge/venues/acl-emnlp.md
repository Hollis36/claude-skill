# ACL / EMNLP / NAACL

ACL 系列 NLP 顶会，统一走 **ACL Rolling Review (ARR)** 流程。

## 基本信息

- **官网**：https://www.aclweb.org / https://aclrollingreview.org
- **ARR 系统**：OpenReview
- **评审制度**：double-blind，3 位 reviewer + Senior Area Chair
- **接收率**：ACL ~25%，EMNLP ~25%，NAACL ~25%
- **录用 → 出版**：ACL Anthology（开放获取）

## ACL Rolling Review (ARR) 流程

**新模式**：先评审，后选会。

1. **提交到 ARR**（每月一轮，2 月、4 月、6 月、8 月、10 月、12 月）
2. **2 个月评审**：3 位 reviewer + 1 meta-review
3. **作者选择 commit 到具体会议**（ACL、EMNLP、NAACL、findings 等）
4. **AC 决定**接收 / 拒绝

## Timeline（按会议）

| 会议 | 投稿截止 | 通知 | 召开 |
|------|---------|------|------|
| **ACL** | 上半年 ARR cycle | 4 月底 | 7–8 月 |
| **NAACL** | 11–12 月 ARR cycle | 1 月底 | 6 月 |
| **EMNLP** | 5–6 月 ARR cycle | 9 月底 | 11–12 月 |

## 格式

- **模板**：ACL LaTeX style（单栏 ARR template）
- **长论文长度**：8 页（review）→ 9 页（camera-ready） + 不限引用 + 不限 appendix
- **短论文**：4 页 + 不限引用
- **匿名**：double-blind

## 必填材料

1. **Responsible NLP Research Checklist**（强制）— 类似 NeurIPS checklist
2. **Reproducibility Checklist**
3. **Limitations** 段落（**必填**，2022+ 强制）
4. **Ethical Considerations**（如适用）
5. **Code / Data 链接**（鼓励）

## 评审

- **Overall Assessment**: 1–5 → 决定 paper 命运
- **Soundness**: 1–5
- **Excitement**: 1–5
- **Reproducibility**: 1–5
- **Confidence**: 1–5
- **Best Paper Nomination** flag

## Rebuttal

- **ARR 标准**：1 周回应，800 字 / reviewer 限制
- **不能换 reviewer**：ARR 系统会保持同一组 reviewer 跨多次提交

## Track

- **Long Papers**（8 页）
- **Short Papers**（4 页）
- **Findings**（接受率高 ~15%，但不在主会 oral，仍进 ACL Anthology）
- **Industry Track**
- **System Demonstrations**
- **Tutorials**

## ARR Resubmission 策略

- 第一次 reject 后**保留 review + meta-review**
- 修改后下一 cycle 提交，附 **revision note** 说明改动
- 同一组 reviewer 重审（除非他们不可用）

## 写作偏好

- ACL/EMNLP 偏好**清晰、深入分析**，胜于 SOTA 数字
- **error analysis** 几乎必备
- **probing / 可解释性**实验加分
- **多语言**实验加分（不只英文）
- **LLM-as-judge** 在 NLP 接受度较高但需谨慎

## 与其他 NLP venues 差异

| 维度 | ACL/EMNLP | TACL | ICLR (NLP) |
|------|-----------|------|-----------|
| 类型 | 会议 | 期刊（→ACL 会议展示）| 会议 |
| 评审周期 | 2 月 | 4–6 月 | 5 月 |
| 长度 | 8 页 | 不限 | 10 页 |

## 检查清单

- [ ] ARR template，单栏
- [ ] 8 页正文
- [ ] Limitations 段落
- [ ] Responsible NLP Checklist
- [ ] PDF 完全匿名
- [ ] 引用格式 author-year `(Smith and Lee, 2024)`
- [ ] License 兼容（数据 / 模型）
