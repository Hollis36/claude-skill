# Quickstart — 5 分钟上手

这是 Hollis 的科研知识库，不是通用 skill 商店。本文教你两件事：
1. 让 agent 接管这个仓库
2. 起步写一篇新论文

## 一、让 agent 接管

任何 agent 进入此仓库后，第一步读 `CLAUDE.md`，第二步读 `INDEX.md`。

如果你用 Claude Code，把仓库 clone 下来直接 `cd` 进去开会话即可：

```bash
git clone https://github.com/Hollis36/cluade_skill.git
cd cluade_skill
claude  # 启动 Claude Code，自动识别 CLAUDE.md
```

如果想让 slash command 全局可用：

```bash
ln -s $(pwd)/commands ~/.claude/commands/research
```

之后任何项目里都能用 `/paper`、`/plot`、`/review` 等。

## 二、起步写一篇新论文

### 1. 复制项目模板

```bash
cp -r projects/_template projects/my-new-paper
cd projects/my-new-paper
```

### 2. 填元数据

编辑 `projects/my-new-paper/README.md`，填：
- 标题
- 目标投稿（NeurIPS / ICML / ICLR / CVPR / ACL）
- 截止时间
- 核心 claim 1 句话

### 3. 让 agent 接手

```
# 在 Claude Code 中
我开始 projects/my-new-paper，目标投 NeurIPS 2026。
帮我看一下 venues/neurips.md，确认 deadline 和格式要求，
然后帮我起草 Introduction（参考 templates/intro-hook.md）。
```

agent 会自动读：
- `knowledge/venues/neurips.md` — 格式 / 截止 / checklist
- `knowledge/templates/intro-hook.md` — Intro 模板
- 调 `skills/paper/` 起草具体内容

## 常见任务速查

| 我要做什么 | 输入 | 用到的资源 |
|----------|------|----------|
| 起草任意章节 | `/paper 写 Method 3.2 节，主题是 ...` | `skills/paper/` + `templates/method-section.md` |
| 写综述 | `/review 关于 X 主题` | `skills/review-paper-writing/` |
| 画论文图 | `/plot 用 data/results.csv 画主表 bar chart` | `skills/scientific-plotting/` + `methods/figure-standards.md` |
| 调试代码 | `/debug 训练 loss 出现 NaN` | `skills/systematic-debugging/` |
| 跑统计检验 | `/stat 比较 5 seed 下方法 A vs B` | `methods/statistical-testing-ml.md` |
| 复现性检查 | `/repro 投稿前自查` | `methods/reproducibility-checklist.md` |
| 写 rebuttal | `/rebuttal` 然后粘贴 reviews | `templates/rebuttal.md` |
| 查会议信息 | `/venue NeurIPS` | `knowledge/venues/neurips.md` |

## 知识库怎么扩

- **新文献笔记**：复制 `knowledge/references/_template.md`，命名 `firstauthor-year-keyword.md`
- **新会议**：在 `knowledge/venues/` 加 `<venue>.md`，参考已有结构
- **新模板**：在 `knowledge/templates/` 加，登记到 `INDEX.md`
- **新方法卡**：在 `knowledge/methods/` 加，登记到 `INDEX.md`

## 不该放的东西

- ❌ 完整论文草稿（用 `projects/`，自动 gitignore）
- ❌ 原始数据集 / 模型权重（太大，用外部存储）
- ❌ 私人 / 机密信息（API key、合作者隐私）
- ❌ 一时兴起的实验代码（沉淀到 skill 再进库）

## 故障排查

| 症状 | 处理 |
|------|------|
| agent 没注意到 CLAUDE.md | 显式说"先读 CLAUDE.md 和 INDEX.md" |
| agent 选错 skill | 直接用 slash command 强制指定 |
| 知识库内容过时 | 提醒 agent 用 WebFetch 验证再回答 |
| slash command 不生效 | 检查 `~/.claude/commands/` symlink 是否存在 |

## 下一步

- 看 [`INDEX.md`](INDEX.md) 了解所有 skill / 知识条目
- 看 [`SKILLS_CATALOG.md`](SKILLS_CATALOG.md) 了解每个 skill 详细说明
- 看 [`CONTRIBUTING.md`](CONTRIBUTING.md) 学怎么新增 skill
