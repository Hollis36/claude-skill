# tase-revision/ — TASE submission 修订工件包

针对 Hollis 的 TASE submission "Edge-Compensated Spray-State-Aware
Multi-Objective Planning for Robotic Spray Coating" 的修订包。

> ⚠️ 这是一个**应用案例**（applied artifact），不是通用 showcase。
> 文件里的数字（HV/IGD/attribution 等）取自该具体 paper；图布局是为
> 此论文设计的。其他 paper 不要直接复制图，但可以参考结构和 helper。

## 目录

```
tase-revision/
├── README.md                              本文件
├── LOCAL_SETUP.md                         在 Mac 本地 setup Claude Code session 的步骤
├── figures/
│   ├── matplotlib_settings.py             共享样式 + SEMANTIC 配色
│   ├── figure_5c_fixed.py + pdf/png       P0: 拆双 Y 轴（HV / IGD 各一栏）
│   ├── figure_7_consolidated.py + pdf/png P0: 5 panel → 3 panel
│   └── figure_8_differentiated.py + ...   P2: 视觉风格区分 (a)/(b)
└── text/
    └── revision_notes.md                  完整修订清单 P0/P1/P2
```

## 如何使用

**首选**：跟 [`LOCAL_SETUP.md`](LOCAL_SETUP.md) 在本地 Mac 跑 — 把整套搬下去，
在 paper 目录开本地 Claude Code session 实际改文件。

**次选**：直接在 GitHub 上看 `text/revision_notes.md` 当 review checklist
对着 main.tex 手工改。

## 总投入估算

| 阶段 | 内容 | 时间 |
|------|------|------|
| P0 | Figure 1/8 dedup + Figure 5c 拆 + Figure 7 缩 | ~2.5 h |
| P1 | n=5 解释段 + KCG 敏感性 appendix | ~1 h |
| P2 | semantic 配色 + Note checklist + 文字细节 + Figure 8 视觉 | ~2.5 h |
| **合计** | | **~6 h** |

如果时间紧，**只做 P0 也能拿走最大收益**（~50% 提升）。

## 与其他 examples/ 的关系

| 路径 | 内容 | 数据 |
|------|------|------|
| `examples/rebuttal-paper/` | NeurIPS rebuttal 工作流通用示范 | **合成数据** |
| `examples/tase-revision/` (本目录) | 真实 paper 修订应用案例 | 数字真，几何合成（Fig 7）|

## 风险提醒

1. **Figure 7 用了合成数据演示** — reviewer 会看穿。**必须**用真实点云 / 厚度 / 路径数据重跑后再交。
2. **P0-3 (Figure 7) 缩 panel 是冒险动作** — 如果你的导师 / 合作者已经认可 5 panel 版本，建议保留 5 panel 备份；据 reviewer 反应决定。
3. **跨图配色统一意味重跑所有 8 个图脚本** — 投入 1h 但要确保每个脚本能跑通。建议留 P2 到最后。

## Agent 使用提示

如果 Hollis 问 "TASE 这种 venue 怎么改 figure" 或 "怎么处理修订工件" →
agent 可参照本目录的 figure 脚本结构和 revision_notes.md 的优先级
分类方式（P0/P1/P2 + 投入估算 + 风险标注）。
