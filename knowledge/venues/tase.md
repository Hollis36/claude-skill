# IEEE Transactions on Automation Science and Engineering (T-ASE)

工业自动化 + 机器人系统 + 制造领域的旗舰期刊之一。强调**应用导向 + 实际部署洞察**。

## 基本信息

- **官网**：https://www.ieee-ras.org/publications/t-ase
- **投稿系统**：IEEE Manuscript Central / Author Portal
- **评审制度**：double-blind 可选 / single-blind 默认，3 位 reviewer + AE + EIC
- **接收率**：约 25–30%
- **录用 → 出版**：IEEE Xplore + Open Access 可选
- **影响因子**：4-6 区间（IEEE 自动化系列里中上）

## Timeline（典型期刊节奏）

| 阶段 | 时长 |
|------|------|
| 投稿 → first decision | 2–4 个月 |
| Major revision 周期 | 2 个月内提交 |
| Second decision | 1–2 个月 |
| 总周期 | 6–12 个月常见 |

无年度 deadline — rolling submission。

## 格式（与一般 IEEE Transactions 一致 + T-ASE 专属）

- **模板**：`IEEEtran.cls`（journal mode，双栏）
- **页数上限**：**常规论文 12 页**（双栏），可上诉到 14；超 14 收 overlength 费用
- **匿名**：默认不匿名（投稿时填全部作者）
- **图**：embedded PDF / EPS，TIFF 也接受
- **参考文献**：IEEE numeric `[1]`，期刊 + 会议混排

## 🔑 Note to Practitioners — T-ASE 招牌

**强制段落**（在 Abstract 后、Index Terms 前）：

> 用面向**工程师 / 制造经理 / 现场操作员**的语言，回答：
> 1. 这个工作能用在什么实际场景？
> 2. 部署前要满足什么条件？
> 3. 我能从中得到多少收益（数字）？
> 4. 哪些情况下不要用 / 注意什么？
>
> ⚠️ 不能照搬 abstract — 受众完全不同。abstract 给 reviewer 读，Note to
> Practitioners 给从未读过你 paper 的工厂自动化工程师读。

**好的 Note to Practitioners 范例（结构）**：
```
[1 句话场景]：在 X 类工业线上...
[2-3 句话发现]：本文表明 Y 现象 / 提出 Z 框架，给出 N 个可操作 regime
（mode_1 数字 / mode_2 数字 / ...）
[1-2 句话部署条件]：如果你的 [equipment] 没有 [property]，注意 +X pp 代价
[1 句话退路]：absolute targets are nominal until [validation step]
```

## 必填材料

1. **Note to Practitioners**（强制）
2. **Index Terms** — 6-10 个，IEEE 词表
3. **作者信息 + ORCID + Affiliations**
4. **Cover Letter**（强烈推荐）— 强调 application + novelty vs 现有 IEEE Transactions on Robotics / T-Mech
5. **Author Biographies + Photos**（accepted 后）
6. **Funding statement**
7. **Copyright transfer / Open Access fee** 选择

## 评审

- **Major / Minor Revision / Reject** 三档（一审很少直接 accept）
- 二审常见，三审罕见
- AE 主导，EIC 终审
- Reviewer 通常都来自工程 / 自动化领域，**对 toy benchmark 极不友好** — 必须有真实系统验证或非常充分的 simulation rationale

## 强 / 弱 paper 特征

| ✅ T-ASE 喜欢 | ❌ T-ASE 不喜欢 |
|---------------|----------------|
| 物理 / 工程 motivated 的方法 | 纯算法 trick 没工程意义 |
| 真实硬件 / 真实数据 / 工业 case study | 只有 simulation benchmark |
| 经济性 / 能耗 / 安全性 分析 | 只比 accuracy / speed |
| 失败案例诚实报告 + boundary conditions | 全部 cherry-pick |
| 与现有工业实践对比，量化提升 pp / % | 只跟其他 paper 比 |
| 实施 / 部署 checklist | 抽象 contribution 列表 |

## 同领域期刊对比

| 期刊 | 偏好 | T-ASE 比 |
|------|------|---------|
| **T-RO** (Transactions on Robotics) | 控制 / 算法纯度 | T-ASE 更应用 |
| **T-Mech** (Mechatronics) | 硬件 + 控制 | T-Mech 更硬件 |
| **RAS** (Robotics and Autonomous Systems) | 中等 application | RAS 更偏机器人，T-ASE 更偏自动化 |
| **RA-L** (RA Letters) | 短论文 (6 页) + 加 ICRA/IROS 报告 | RA-L 更快但页限严格 |

## Rebuttal 策略

- T-ASE rebuttal 一般 **以正文修订 + Response Letter** 提交，**不**像顶会那样字数严格限制
- Response Letter 标准格式：每条 review 引用 → 你的回答 → 修改位置（paper 哪段）
- **必须补实验回应**，纯辩解 reviewer 会要求 third review

## 投稿前 checklist（T-ASE 专属）

- [ ] Note to Practitioners 写完，对**非作者**读过一遍能理解
- [ ] 论文有真实 / 工业 case study，或者**说清楚** simulation 充分性
- [ ] 摘要末尾给出**可量化收益**（pp、%、s、kg、$）
- [ ] Limitations 节诚实写"什么情况下我们的方法不适用"
- [ ] References 包含至少 5 篇近 3 年 T-ASE / T-RO / T-Mech
- [ ] Cover Letter 强调 "automation science" 角度
- [ ] 不超 14 页（main + appendix；overlength 收费）
- [ ] Author Biographies 准备好（accepted 后才上传，但提早写）

## 常见 reviewer 攻击点

1. **"Why is this T-ASE rather than T-RO?"** — 必须有应用 / 部署导向，否则被 transfer to T-RO
2. **"Only simulation, no hardware validation"** — 必须正面回应，给出 sim-to-real plan
3. **"Note to Practitioners is too abstract"** — 必须给具体数字 / 场景 / 部署门槛
4. **"How does it scale to industrial line"** — throughput / cycle time / changeover cost 必备
5. **"Comparison with the prior T-ASE paper [X]"** — T-ASE reviewer 通常熟悉 venue 历史，引用本期刊近 3 年相关工作非常重要
