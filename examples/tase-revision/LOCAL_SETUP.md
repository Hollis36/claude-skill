# Local Session Setup — TASE Paper Revision

把这套科研知识库 + TASE 修订包**搬到你本地 Mac**，并在 paper 目录开本地
Claude Code session 直接改文件。

## 一次性 setup（在 Mac terminal 跑）

```bash
# 1. Clone 知识库到主目录
git clone -b claude/research-skills-database-wUw3A \
  https://github.com/Hollis36/claude-skill.git ~/claude-skill

# 2. 安装 slash commands（/morning /exp /write /check /plot /paper 等）
mkdir -p ~/.claude/commands
ln -sf ~/claude-skill/commands ~/.claude/commands/research

# 3. 进 paper 目录
cd /Users/kingcode/Documents/robot-sim/paper/submission_bundle_tase

# 4. 在 paper 目录里建项目级 CLAUDE.md（指向知识库）
cat > CLAUDE.md << 'EOF'
# Project: TASE submission — Edge-Compensated Spray-State-Aware Planning

> Knowledge base: ~/claude-skill (read ~/claude-skill/CLAUDE.md first)
> Venue specifics: ~/claude-skill/knowledge/venues/tase.md
> Revision plan: ./REVISION_NOTES.md
> Fixed figures (templates): ./revision_figures/

## Phase
revision (TASE submission, addressing internal review before re-submission)

## Workflow conventions
Follow ~/claude-skill/projects/_template/WORKFLOW.md
- /morning → list today's revision tasks
- /write → draft text/caption changes per REVISION_NOTES.md
- /plot → swap real data into revision_figures/figure_*.py
- /check → run pre-submission self-check before re-submitting

## Red lines
- Never edit numbers in main.tex without sourcing them in data
- Don't push to git without explicit confirmation
- LaTeX citation keys must exist in references.bib
EOF

# 5. 拉修订工件
cp -r ~/claude-skill/examples/tase-revision/figures ./revision_figures
cp ~/claude-skill/examples/tase-revision/text/revision_notes.md ./REVISION_NOTES.md

# 6. (可选) 拉 WORKFLOW.md 副本（方便不离开 paper dir 也能看）
cp ~/claude-skill/projects/_template/WORKFLOW.md .

# 7. 开 Claude Code
claude
```

## 第一句 prompt（复制粘贴）

```
我们要修订 TASE submission。本目录是 paper bundle。

请先按顺序读：
1. CLAUDE.md  (本项目 + 引用主知识库)
2. ~/claude-skill/CLAUDE.md  (主入口)
3. ~/claude-skill/knowledge/venues/tase.md  (T-ASE 投稿规范)
4. WORKFLOW.md  (会话模式)
5. REVISION_NOTES.md  (本轮修订清单 P0/P1/P2)
6. main.tex  (paper 主文，找到对应 figure 引用位置)

然后按 REVISION_NOTES.md 的 P0 顺序开工。**从 P0-1 (Figure 1 删 workflow row) 开始**：
- 在 main.tex 找到 Figure 1 的 \includegraphics 和 \caption
- 判断 figure 文件是否单图（如果是，需重生 figure；如果是 subfigure 组合，去掉 bottom row）
- 按 REVISION_NOTES.md 中给出的 caption 模板更新
- diff 给我看，我确认后再 commit

不动 numbers，所有数字从 results 或现有 Table 引用。引用不在 .bib 的标 [CITE: ...]。
```

## 后续工作流（每天 / 每个 session）

| 命令 | 用途 |
|------|------|
| `/morning` | 列今日要做哪几条修订（从 REVISION_NOTES.md 拉 TODO） |
| `/write` | 改某段文字 / caption，agent 直接写文件 |
| `/plot` | 拉 revision_figures/*.py 模板，把真实数据喂进去重生图 |
| `/check` | 修完跑投稿前自查（结构 + BibTeX + 数字一致性）|

## 重要：本地动手才能改的事

我（远端）只能给你**指引 + 模板 + 修订包**，**不能**：
- 直接编辑你 Mac 上的 main.tex
- 运行你本地的 LaTeX 编译
- 触发你的 figure 重建流程
- 看你的真实 results.csv 数据

**所有实际改动都要本地 session 完成**，本地 Claude Code 才有文件访问权限。

## 风险提醒

1. **首次 `git clone` 拿到的是开发分支**（`claude/research-skills-database-wUw3A`）— 这个分支还没合 main。如果想用稳定 main，把 `-b claude/...` 删掉。
2. **`revision_figures/figure_7_consolidated.py` 用合成数据**，**必须**用你真实点云 / 厚度 / 路径数据重跑，否则交上去 reviewer 立刻看穿。
3. **`/check` 跑出来的 FAIL 不要无脑修** — 比如它可能认为 `[CITE: ...]` 是问题，但你正想保留作为待填占位符。
4. **不要让 agent 在没确认前 `git push`** — 修 paper 期间任何 push 都应当事先和你 review。
