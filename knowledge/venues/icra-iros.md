# ICRA / IROS — 机器人两大顶会

两个机器人方向最主流会议，年度交替主导（ICRA 春、IROS 秋）。投稿圈高度重叠，paper 风格区别细微但存在。

## ICRA — IEEE International Conference on Robotics and Automation

- **官网**：https://www.ieee-icra.org
- **主办**：IEEE Robotics and Automation Society (RAS)
- **评审**：double-blind，3 位 reviewer + AE
- **接收率**：约 40–45%
- **附加 track**：与 **RA-L** (Robotics and Automation Letters) 联合 — RA-L 接收的论文可选择在 ICRA 报告

### Timeline（典型）

| 阶段 | 时间 |
|------|------|
| Paper Submission | 9 月中（前一年）|
| Author Response (Rebuttal) | 12 月 |
| Author Notification | 1 月底 |
| Camera-ready | 2–3 月 |
| 会议召开 | 5 月末 / 6 月初 |

### 格式

- **模板**：`IEEEtran.cls`（conference mode，双栏）
- **页数**：6 页 main + 2 页 reference（共 8 页）；超 6 页需付页费
- **匿名**：double-blind 严格 — 不可署名、不可自引"our previous work [X]"
- **arXiv preprint**：允许，但**不能**在投稿 PDF 中暴露身份

## IROS — IEEE/RSJ International Conference on Intelligent Robots and Systems

- **官网**：https://iros.org
- **主办**：IEEE RAS + RSJ + 工程计算
- **评审**：double-blind，3 位 reviewer
- **接收率**：约 45–48%（略高于 ICRA）
- **附加 track**：同 RA-L 联合

### Timeline（典型）

| 阶段 | 时间 |
|------|------|
| Paper Submission | 3 月初 |
| Notification | 6 月底 |
| Camera-ready | 7 月底 |
| 会议召开 | 10 月 |

### 格式

- **模板**：`IEEEtran.cls`
- **页数**：6 页 main + 2 页 reference
- **匿名**：double-blind

## ICRA vs IROS — 选哪个？

| 维度 | ICRA | IROS |
|------|------|------|
| Prestige | 略高 | 接近 |
| 接收率 | 40% | 45% |
| 风格偏好 | 控制 / 算法 / 学习 | 系统集成 / 应用 / 多领域交叉 |
| 截止 | 9 月 | 3 月 |
| 会议地点 | 全球轮换 | 全球轮换 |
| 与 RA-L 联合 | 是 | 是 |

**实用决策**：哪个截止快投哪个，被拒后改投另一个 — paper 重复用 80% 内容，调 figure 和 8 页限。

## RA-L 联合 track（值得了解）

**Robotics and Automation Letters** 是 ICRA/IROS 的"期刊 sibling"：
- **6 页限**（严格）
- **滚动投稿**（任何时候）
- 接受后**可选**在 ICRA 或 IROS 现场报告（无额外评审）
- **接收率 30–35%**，比 ICRA/IROS 略难
- 通常**优先投 RA-L** — 如果接受了既得期刊又得 conference 报告

## 必备材料

1. **PDF**（IEEEtran，6 + 2 页或 6 页 RA-L）
2. **Supplementary video**（强烈推荐机器人 paper，30s–3min）
3. **Index Terms**（IEEE 词表）
4. **PaperPlaza / RAS PaperCept** 投稿系统 metadata

## 评审

- **Score**: -3 to +3 typical, with weight = confidence
- 评审周期 60–90 天
- **Rebuttal 6000 字符**（ICRA）/ **类似 RA-L** — 严格字符限制
- 通常 1 轮 rebuttal，AE 决定

## 强 / 弱 paper

| ✅ ICRA/IROS 喜欢 | ❌ 不喜欢 |
|------|------|
| 真实机器人实验（哪怕 simulation 主体）| 纯数学 / 纯算法 paper |
| 视频清晰展示能力 | 没视频 |
| 故障模式 / 边界情况分析 | 全是"100% 成功" |
| Open-source code & data | "Code available upon acceptance" |
| 与 SOTA baseline 真实对比 | 只跟自己以前的版本比 |

## Rebuttal 策略（ICRA / IROS）

- **6000 字符限制**（含空格）
- 分 reviewer 答复，每 reviewer 一段
- **不能加新实验图** — 只能引用 supplementary
- 引用 line / paragraph 号回应具体批评
- 末尾"Summary of changes": camera-ready 会改什么

## 与 T-ASE 区别

| | T-ASE | ICRA / IROS |
|---|-------|------------|
| 类型 | 期刊 | 会议 |
| 页数 | 12–14 | 6+2 |
| 周期 | 6–12 月 | 4–5 月 |
| 应用 angle | 必备（Note to Practitioners） | 不强制 |
| Code | 鼓励 | 鼓励 |
| 复用同 paper | 可以扩展 → 期刊版（30%+ 新内容）| 直接投 |

**典型路径**：先 ICRA / IROS 发 conference 版 → 实验扩充 → 投 T-ASE / T-RO 期刊版。

## 检查清单

- [ ] IEEEtran 模板，conference mode
- [ ] 主文 ≤ 6 页（不含 reference）
- [ ] PDF 匿名（去 author + acknowledgments + 自引）
- [ ] Supplementary video（**强烈建议**）
- [ ] References ≥ 15 篇，含 5+ 近 2 年 ICRA / IROS / RA-L
- [ ] Code 链接（可匿名，camera-ready 公开）
- [ ] Index Terms 来自 IEEE 词表
