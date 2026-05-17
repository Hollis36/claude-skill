# /plot — 论文级绘图

调用 `skills/scientific-plotting/` 完成绘图任务，并强制应用 `knowledge/methods/figure-standards.md` 中的期刊规范。

## 流程

1. **问清楚（如未指明）**：
   - 数据来源（DataFrame / CSV / 列表）
   - 图表类型（柱状 / 折线 / 散点 / 热力 / ...）
   - 目标投稿（决定单/双栏、字号、配色）
   - 是否要可比较的多 panel

2. **强制规范**（不需用户提醒）：
   - `pdf.fonttype = 42`
   - 字号 ≥ 7pt
   - 色盲安全配色（除非用户指定）
   - 误差条标明 std / SEM / CI
   - Caption 自包含

3. **输出**：
   - 完整可运行 Python 脚本
   - 用 `plt.savefig('figure_N.pdf', dpi=300, bbox_inches='tight')`
   - 同时输出 PNG 预览（便于在聊天里看）

4. **检查清单**（生成后自查）：
   - [ ] 坐标轴标签带单位
   - [ ] 图例不挡数据
   - [ ] 黑白打印仍可读
   - [ ] 误差条 + n 标注
   - [ ] 显著性标注（若适用）

## 进阶

- SciencePlots 一行启用：`plt.style.use(['science', 'ieee'])`
- 多 panel：`fig, axes = plt.subplots(1, 3, figsize=(7, 2.5))`，统一 sharey
- 显著性标注：`statannotations` 库

$ARGUMENTS
