# Robotics 主要期刊（T-RO / T-Mech / RA-L / RAS）

T-ASE 见独立文件 `tase.md`。本文覆盖其余 4 个机器人领域常投期刊。

## IEEE Transactions on Robotics (T-RO)

- **官网**：https://www.ieee-ras.org/publications/t-ro
- **定位**：机器人领域**最高级别**期刊，控制 / 算法 / 理论强
- **接收率**：约 20–25%
- **影响因子**：高 (5+)
- **周期**：6–12 月

### 格式

- IEEEtran journal，双栏
- 页数：**16 页常规上限**，可议
- 不匿名
- 强数学严谨性

### 与 T-ASE 区别

| | T-RO | T-ASE |
|---|------|-------|
| 焦点 | 算法 / 控制 / 理论新颖性 | 应用 / 部署 / 工业可行性 |
| Note to Practitioners | 不要求 | **强制** |
| 偏好实验 | 控制律证明 / 闭环稳定性 | 系统集成 / 真实工厂 case |

**关键问题**：你的 paper 应该投哪个？规则：**Note to Practitioners 写得出来 → T-ASE，写不出来或硬凑 → T-RO**。Reviewer 会借此判断 venue fit。

---

## IEEE Robotics and Automation Letters (RA-L)

- **官网**：https://www.ieee-ras.org/publications/ra-l
- **定位**：短论文期刊 + ICRA/IROS 联合 track
- **接收率**：约 30–35%
- **影响因子**：4–5
- **周期**：3–4 月（快！）

### 格式

- IEEEtran journal
- 页数：**6 页 + reference**（严格）
- 不匿名

### 投稿优势

- **滚动投稿**（无 deadline）
- **快**（3–4 月一审）
- 接受后**可选**在 ICRA 或 IROS 现场报告，无需重新评审
- 既得期刊 citation 又得 conference 曝光

### 推荐路径

任何短篇机器人工作（不需要 12 页扩展）→ **优先 RA-L** 而不是直接 ICRA / IROS。

---

## IEEE Transactions on Mechatronics (T-Mech)

- **官网**：https://www.ieee-ies.org/pubs/transactions-on-mechatronics
- **定位**：机电一体化，**强调硬件 + 控制结合**
- **接收率**：约 25%
- **周期**：6–8 月

### 与 T-ASE 区别

| | T-Mech | T-ASE |
|---|--------|-------|
| 焦点 | 机电硬件 / 传感 / 驱动设计 | 自动化系统 / 多目标优化 / 决策 |
| 软件占比 | 较低 | 较高 |
| 必备 | 硬件原型 / 实测数据 | Note to Practitioners |

**适合投 T-Mech 的 paper**：核心创新在硬件 / 传感器 / 驱动器 / 物理建模而非算法。

---

## Robotics and Autonomous Systems (RAS, Elsevier)

- **官网**：https://www.sciencedirect.com/journal/robotics-and-autonomous-systems
- **定位**：广覆盖机器人 + 自主系统期刊
- **接收率**：约 30%
- **周期**：4–8 月
- **影响因子**：3–5

### 特征

- Elsevier 体系，不是 IEEE
- 双栏，不严限页数
- 不匿名

### 何时考虑

- ICRA / IROS / RA-L 被拒后的"backup"（接受率较高）
- 工业自动化 + 机器人交叉，T-ASE 觉得太机器人、T-RO 觉得太应用 → RAS

---

## 跨期刊投稿决策树

```
你的 paper 核心贡献是什么？
│
├── 控制律 / 数学新颖性 ──→ T-RO
│
├── 工业部署 / 自动化优化 / case study ──→ T-ASE
│        └─── 写得出 Note to Practitioners 吗？写不出 → T-RO
│
├── 硬件 / 机电 / 传感器 ──→ T-Mech
│
├── 短篇 (6 页够) ──→ RA-L（+ 可挂 ICRA/IROS 报告）
│
├── 综合 / 自主系统 ──→ RAS (Elsevier)
│
└── 不确定 → 投 ICRA/IROS 拿快速 review，再扩展期刊版
```

## 通用 checklist（所有 IEEE 机器人期刊）

- [ ] IEEEtran 模板，正确 mode（journal vs conference）
- [ ] Index Terms 来自 IEEE 词表
- [ ] **Author Biographies + 照片**（accepted 后）
- [ ] **Copyright transfer / Open Access** 选择
- [ ] **Supplementary video**（机器人 paper 强烈推荐）
- [ ] Cover Letter 强调 venue fit
- [ ] References 覆盖近 3 年同 venue 论文 ≥ 5 篇
- [ ] **Limitations 节** — IEEE 机器人 reviewer 极看重诚实性

## 不要做的事

| ❌ 行为 | 后果 |
|------|------|
| 同 paper 同时投 T-ASE 和 T-RO | 直接 desk-reject + 学术不端记录 |
| ICRA 投稿前 4 个月把 paper 挂 arXiv 不匿名 | 评审者搜到 → 投稿无效 |
| Note to Practitioners 抄 abstract | reviewer 立即看出，明扣分 |
| 12 页超出 14 页限制 | 收 overlength fee，且 EIC 不开心 |
| 自引用占总引用 > 30% | reviewer 怀疑 reviewer-ring |
