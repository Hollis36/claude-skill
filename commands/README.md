# Commands — Slash Commands 定义

这些 `.md` 文件是 slash command 的源定义。Hollis 直接输入 `/paper`、`/plot` 等触发对应工作流。

## 已有命令

**项目生命周期**：
| 命令 | 用途 |
|------|------|
| `/init` | 从 `projects/_template/` 起一个新论文项目（填元数据、配 rebuttal tracker） |
| `/morning` | 每日开局，列今日 3 件事 + 风险预警，不动手等确认 |
| `/exp` | 跑 / 补实验，强约束落 `data/results.csv` + `run_log.md` |
| `/write` | 深参与起草 / 改稿，直接写文件 |

**领域 skill**（按任务触发）：
| 命令 | 主要 skill / 知识 | 一句话用途 |
|------|------------------|-----------|
| `/paper` | `skills/paper/` | 起草任意论文章节、整体规划 |
| `/review` | `skills/review-paper-writing/` | 综述 / survey 写作 |
| `/plot` | `skills/scientific-plotting/` + `figure-standards.md` | 论文级绘图 |
| `/debug` | `skills/systematic-debugging/` | 4 阶段调试科研代码 |
| `/stat` | `skills/statistical-analysis/` + `statistical-testing-ml.md` | 统计检验与报告 |
| `/repro` | `skills/reproducible-research/` + `reproducibility-checklist.md` | 复现性检查 |
| `/rebuttal` | `knowledge/templates/rebuttal.md` | Rebuttal / Response 起草 |
| `/venue` | `knowledge/venues/` | 目标会议投稿信息查询 |

**关系**：`/morning` 决定今天用哪个 `/exp` `/write` 或领域 skill。`/exp` 跑完数据可能触发 `/plot` 重生成图，再触发 `/write` 把数字写进 rebuttal。

## 如何安装到本地 Claude Code

```bash
# 把整个 commands/ 目录 symlink 到本地
ln -s $(pwd)/commands ~/.claude/commands/research

# 或单独 link 某个
ln -s $(pwd)/commands/paper.md ~/.claude/commands/paper.md
```

## 新增命令

1. 在 `commands/` 下新建 `<name>.md`
2. 文件结构：
   - 标题：`# /<name> — <一句话用途>`
   - 引用相关 skill / 知识库路径
   - 写流程步骤
   - 末尾留 `$ARGUMENTS` 接用户参数
3. 在本 README + 根 `INDEX.md` 登记一行
