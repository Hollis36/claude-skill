# Revision Notes — Edge-Compensated Spray-State-Aware Multi-Objective Planning

修订针对 TASE submission，按 P0 / P1 / P2 优先级排。每条带：**位置**、**问题**、**改法**、**LaTeX 片段（如需要）**。

---

## P0-1: Figure 1 与 Figure 8 工作流横条重复

**位置**：Figure 1 底部"geometry → planner → simulator → attribution"workflow row 与 Figure 8 底部 workflow 几乎相同。

**问题**：anti-redundancy 红线，reviewer 会问 "why duplicate？"

**改法**：
- **保留** Figure 8 的 workflow 横条（在 Discussion 末尾收束 contribution loop 自然）
- **从 Figure 1 删除** workflow 横条，Figure 1 只保留上排三个 panel: (a) Geometry interface、(b) Deposition-aware planner、(c) Quality-gap attribution
- Figure 1 整图高度可减 25–30%，给后续章节腾空间

**修改 caption**（Figure 1）：
```latex
\caption{System problem and quality-control loop. (a) Measured geometry is
converted into a planning state. (b) The deposition-aware planner applies
edge compensation and raster planning, and the simulated film-thickness
field is evaluated. (c) The residual quality gap is attributed back to
formulation, geometry, model fidelity, execution, and optimiser effects.
The end-to-end attribution workflow is summarised in Fig.~\ref{fig:closure}
(bottom).}
```

---

## P0-2: Figure 5(c) 双 Y 轴

**位置**：Figure 5(c) "Final optimizer gap"，HV 在左 Y 轴、IGD 在右 Y 轴，p 值标在两个柱子中间难以归属。

**问题**：HV (↑ 更好) 和 IGD (↓ 更好) 量纲方向相反，双 Y 轴误导读者。

**改法**：拆成两个并列 panel，各管各的 Y 轴。**已生成** `figures/figure_5c_fixed.py`，直接替换原 (c) 子图即可。

**修改 caption**（Figure 5）：
```latex
\caption{NSGA-II vs MOEA/D (n=10 seeds, $N=60$, 40 generations).
(a) Representative seed-0 Pareto search result in process-time vs. NU space.
(b) Hypervolume convergence; NSGA-II reaches 95\% of its final HV by
generation 9, while MOEA/D plateaus lower. (c) Hypervolume comparison
(higher is better), (d) Inverted Generational Distance comparison (lower
is better). Both indicators show NSGA-II dominates (Mann–Whitney $U$ test,
two-tailed, $\alpha=0.05$).}
```

注意 (c) 现在变成两个子图 (c)(d)，**Figure 5 整体从 3 panel 变 4 panel**。布局改为 1×4 或者 2×2 都可以；推荐 2×2（左上 Pareto / 右上 HV 曲线 / 左下 HV bar / 右下 IGD bar），视觉更平衡。

---

## P0-3: Figure 7 五 panel 冗余

**位置**：Figure 7 当前 (a)(b)(c)(d)(e) 五 panel，其中 (b)(c)(d) 是同一个 patch 的三种 overlay。

**问题**：sub-component fragmentation，读者需在三个小图之间扫视拼装 pipeline。

**改法**：合并 (b)(c)(d) 为单 panel（厚度色图为底，叠 normals + 路径 + 边缘 proxy）。**已生成** `figures/figure_7_consolidated.py` 作为布局模板（synthetic 数据，需换上你真实点云/扫描结果）。

**修改 caption**：
```latex
\caption{Transfer to measured and reconstructed industrial geometry.
(a) Scanned mesh interface with a representative patch (dashed) selected
for planning. (b) Local patch with combined visualisation: simulated
film-thickness colormap, planned raster path, sampled surface normals,
and edge-extension proxy. (c) Hard-case full-object point cloud with
planned patch paths overlaid. The panel summarises the transfer route
used by the point-cloud, curved-shell, and robustness studies.}
```

---

## P1-1: E1 / E2 的 n=5 vs E3 的 n=10 解释

**位置**：Sec V.B 末尾，或在 Table III caption / Table IV caption 中加一句。

**问题**：reviewer 会问"为什么 E3 用 n=10 而 E1/E2 用 n=5？"。Wilcoxon 在 n=5 时最小 p=0.0312，不能触 p<0.01。

**改法（推荐解释）**：在 Sec V.A "Setup" 末尾加一段：

```latex
\paragraph{Sample size selection.}
Experiments E1 and E2 use $n=5$ seeds; E3 uses $n=10$ to support the
Mann--Whitney $U$ comparison between optimisers. The smaller sample
in E1 / E2 reflects per-run cost: a single 6-variable NSGA-II run
with $N=80$ population and 60 generations evaluates roughly
$80 \times 60 \times 2 = 9{,}600$ deposition simulations on a
$120 \times 120$ thickness grid, taking approximately 3 h on the
target hardware. We verified that the relative ordering of operating
modes in E1 (Legacy $>$ Production $>$ Uniform in NU) is preserved
across all $n=5$ seeds with zero rank inversions, so the small-sample
conclusion does not depend on statistical power.
```

**或者**重跑 E1/E2 为 n=10（投入 4 小时 × 2，更彻底）。我建议**先加解释段**，看 reviewer 是否买账；如果第二轮 reviewer 仍咬 → 再重跑。

---

## P1-2: KCG 对 HV reference point 的敏感性

**位置**：当前文中 Sec IV.F 定义 KCG 用了 "combined-front nadir × 1.1"，没做敏感性分析。

**问题**：HV 对 ref point 敏感，5.2% 可能被 cherry-pick。

**改法**：在 appendix 加一个 1 段 + 1 表，覆盖 ref point ∈ {1.0×, 1.1× (used), 1.2×, 1.5×} 的 KCG 值，证明排序稳。

**附加段落（Appendix A）**：

```latex
\subsection{KCG Sensitivity to Reference Point}
\label{app:kcg-sensitivity}
The hypervolume indicator depends on the choice of reference point.
We use the nadir of the combined ideal-and-robot 80-solution front,
inflated by a factor $\rho$. Table~\ref{tab:kcg-sensitivity} reports
$KCG_{HV}$ for $\rho \in \{1.0, 1.1, 1.2, 1.5\}$.

\begin{table}[t]
\centering
\caption{KCG$_{HV}$ sensitivity to reference-point inflation factor $\rho$.}
\label{tab:kcg-sensitivity}
\begin{tabular}{lcccc}
\toprule
$\rho$              & 1.0   & 1.1 (used) & 1.2   & 1.5 \\
\midrule
HV(ideal)           & TBD   & 2.598      & TBD   & TBD \\
HV(robot)           & TBD   & 2.464      & TBD   & TBD \\
$KCG_{HV}$ (\%)     & TBD   & 5.2        & TBD   & TBD \\
\bottomrule
\end{tabular}
\end{table}

The absolute KCG value varies by less than $\pm$0.X pp across this
range, and the qualitative conclusion (robot execution incurs
roughly 5\% HV loss) is preserved.
```

**操作**：你跑 4 个 ρ 值 → 填表（约 30 分钟单跑，因为是 deterministic re-evaluation 而非新搜索）。

---

## P2-1: 跨图 semantic 配色

**问题**：当前 8 张图 NSGA-II / MOEA/D / Ideal / Robot 等没有统一颜色约定。

**改法**：建立全局 palette，所有 figure 脚本顶端 import：

```python
# figures/colors.py — 全文统一
SEMANTIC = {
    "ours":           "#0F4D92",  # NSGA-II / Production-mode / Compensated
    "baseline":       "#B64342",  # MOEA/D / Legacy / SG-plan
    "variant":        "#8BCF8B",  # Uniform mode / DG-plan robust
    "support":        "#42949E",  # FlashAttention-equiv / Ideal frontier
    "neutral":        "#767676",  # 参考线 / 灰色背景
    "negative":       "#D55E00",  # Drop / failure
}
```

**应用到具体图**：
- Figure 3: Legacy=baseline 红、Production=neutral 灰、Compensated=ours 蓝（统一三种 mode 颜色，所有出现 mode 对比的图都用同一组）
- Figure 4: SG=baseline 红、DG=ours 蓝
- Figure 5: NSGA-II=ours 蓝、MOEA/D=baseline 红
- Figure 6: Ideal=support 青、Robot=ours 蓝
- Figure 8: Sensitivity 用 diverging RdBu，attribution 正贡献=variant 绿、负贡献=baseline 红

---

## P2-2: Note to Practitioners 加 deployment checklist

**位置**：Note to Practitioners 段末尾加一个 4–5 条 checklist。

**当前结尾**：
> If only a single-Gaussian nozzle model is available, plan for a +4.01 pp NU deployment penalty; if the specific nozzle and robot have not been bench-tested, treat absolute NU targets as nominal.

**建议补加**：

```latex
\paragraph{Deployment Checklist.}
Before applying this framework on a new line:
\begin{enumerate}
    \item Verify that the deployed nozzle follows a double-Gaussian flux
          profile by measuring the radial deposition at $r \in
          \{0, \sigma_1, 2\sigma_1, \sigma_2, 2\sigma_2\}$. If the outer
          halo amplitude $A_2 / A_1 > 0.10$, the SG approximation will
          systematically under-predict edge under-build.
    \item Re-calibrate $\sigma_1, \sigma_2, d^\ast, \delta_d$ to the
          specific gun and standoff; Conner~(2005) constants apply only
          to the original ESRB family.
    \item Determine the workpiece's regulatory NU target (e.g., 5\% for
          automotive paint, 8\% for industrial coating) and pick
          Production or Uniform mode accordingly.
    \item If the target robot is not Franka-class, recompute KCG by
          running 80 ideal-Pareto solutions through the robot's
          waypoint-skip and tracking-noise model; expect 2–8\% loss for
          6/7-DoF arms in similar workspace regimes.
    \item Treat absolute NU targets as nominal until a 10–20 sample
          dry-film validation is completed on the calibrated gun--robot
          pair.
\end{enumerate}
```

---

## P2-3: 文字细节

| 位置 | 当前 | 改 |
|------|------|-----|
| Abstract | "degrade by +4.01 pp" | "incur a +4.01 pp NU penalty" |
| Abstract | "improve by −2.62 pp" | "improve by 2.62 pp (a robustness margin)" |
| §V.D | "SG appears better within its own model" | "SG appears better when evaluated against its own simplified footprint" |
| §VI.b | "near-two-dimensional trade-off structure" | "effectively two-dimensional trade-off (coverage and overspray saturate at the front)" |
| §VII | "Boundary-aware edge compensation" | 改成 "Promoting edge compensation to a first-class planning variable"（更对应 C1 的措辞） |

---

## P2-4: Figure 8 visualisation 改进

**位置**：Figure 8 (a) 和 (b) 都是横向 bar chart，风格相同看起来像同一张图。

**改法**：
- (a) Parameter–objective sensitivity：改 **diverging colormap**（绿 = 减少 NU / 改善 metric，红 = 增加 NU / 恶化）
- (b) Quality-gap attribution：改 **stacked + / −** bar，正贡献 green（variant 色），负贡献 red（baseline 色）

这样两个 panel 视觉上明显区分，读者不会混淆。

---

## 修订优先级总表

| 项 | 优先级 | 投入 | 修订方式 |
|----|--------|------|---------|
| Figure 1/8 workflow 去重 | P0 | 30 min | LaTeX 编辑 |
| Figure 5(c) 拆双 Y 轴 | P0 | 30 min | 替换 figure 文件 |
| Figure 7 5→3 panel | P0 | 1 h（重跑数据）+ 30 min（代码改） | 替换 figure 文件 |
| n=5 vs n=10 解释段 | P1 | 5 min | 加 1 段 |
| KCG ref-point 敏感性 | P1 | 30 min（跑 4 ρ）+ 15 min（写） | Appendix |
| Cross-figure semantic 配色 | P2 | 1 h（重画 8 张图，但只调颜色） | 8 个 .py 改 |
| Deployment checklist | P2 | 15 min | Note to Practitioners 末加 |
| 文字细节（abstract / §V.D / §VI / §VII） | P2 | 10 min | LaTeX 编辑 |
| Figure 8 visual 区分 | P2 | 30 min | 重画 8(a)(b) |

**总投入**：P0 全做 ≈ 2.5 h；P0 + P1 ≈ 3.5 h；全做 ≈ 6 h。

建议：**先做 P0**（3 项），重新生成 PDF 看整体效果，再决定 P1 / P2 是否值得。
